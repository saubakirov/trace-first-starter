"""Rendered-site checks sharing one MkDocs build."""

import os
from pathlib import Path
import re
import subprocess
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SITE_DIR = Path(os.environ.get("TFW_ASSURANCE_SITE_DIR", str(PROJECT_ROOT / "site")))


@pytest.fixture(scope="module", autouse=True)
def build_site():
    env = os.environ.copy()
    env["DISABLE_MKDOCS_2_WARNING"] = "true"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "mkdocs",
            "build",
            "--config-file",
            "docs/mkdocs.yml",
            "--site-dir",
            str(SITE_DIR),
        ],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
        env=env,
    )
    if result.returncode:
        pytest.fail(f"MkDocs build failed:\n{result.stderr}\n{result.stdout}")
    yield


def test_public_core_is_rendered():
    expected = (
        "index.html",
        "getting-started/index.html",
        "concepts/philosophy/index.html",
        "reference/conventions/index.html",
        "reference/glossary/index.html",
        "reference/changelog/index.html",
        "reference/compilable-contract/index.html",
    )
    assert all((SITE_DIR / path).is_file() for path in expected)
    assert len(list((SITE_DIR / "reference/workflows").rglob("index.html"))) >= 5
    assert len(list((SITE_DIR / "reference/templates").rglob("index.html"))) >= 5


def test_generated_frontmatter_does_not_render_as_body_text():
    leaked = re.compile(r"<hr />\s*<p>title: ")
    offenders = [
        page.relative_to(SITE_DIR)
        for page in SITE_DIR.rglob("index.html")
        if leaked.search(page.read_text(encoding="utf-8"))
    ]
    assert not offenders
