"""Integration tests for the TFW documentation pipeline.

These tests run the actual MkDocs build on the real project and verify output.
They require: pip install -r docs/requirements.txt pytest
"""

import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


@pytest.fixture(scope="module", autouse=True)
def build_site():
    """Run mkdocs build once before all integration tests."""
    import os
    env = os.environ.copy()
    env["DISABLE_MKDOCS_2_WARNING"] = "true"
    result = subprocess.run(
        [
            sys.executable, "-m", "mkdocs", "build",
            "--config-file", "docs/mkdocs.yml",
        ],
        capture_output=True, text=True, cwd=str(PROJECT_ROOT),
        env=env,
    )
    if result.returncode != 0:
        pytest.fail(f"MkDocs build failed:\n{result.stderr}\n{result.stdout}")
    yield
    # No cleanup — site/ is in .gitignore


def test_static_pages_generated():
    """Key static pages exist in site/ output."""
    site = PROJECT_ROOT / "site"
    assert (site / "index.html").exists(), "index.html missing"
    assert (site / "getting-started" / "index.html").exists(), "getting-started missing"
    assert (site / "concepts" / "philosophy" / "index.html").exists(), "philosophy missing"
    assert (site / "reference" / "conventions" / "index.html").exists(), "conventions missing"
    assert (site / "reference" / "glossary" / "index.html").exists(), "glossary missing"
    assert (site / "reference" / "changelog" / "index.html").exists(), "changelog missing"


def test_knowledge_index_generated():
    """KNOWLEDGE.md compiled to knowledge-index page."""
    site = PROJECT_ROOT / "site"
    page = site / "knowledge-index" / "index.html"
    assert page.exists(), "knowledge-index page missing"
    content = page.read_text(encoding="utf-8")
    assert "Architecture" in content or "architecture" in content


def test_task_pages_generated():
    """Task artifacts are accessible."""
    site = PROJECT_ROOT / "site"
    tasks_dir = site / "tasks"
    if not tasks_dir.exists():
        pytest.skip("No tasks/ in site output")
    task_pages = list(tasks_dir.rglob("index.html"))
    assert len(task_pages) > 10, f"Expected 10+ task pages, got {len(task_pages)}"


def test_knowledge_topic_pages_generated():
    """Knowledge topic files are compiled."""
    site = PROJECT_ROOT / "site"
    knowledge_dir = site / "knowledge"
    assert knowledge_dir.exists(), "knowledge/ section missing"
    topic_pages = list(knowledge_dir.glob("*/index.html"))
    assert len(topic_pages) >= 3, f"Expected 3+ topics, got {len(topic_pages)}"


def test_workflow_pages_generated():
    """Workflow reference pages exist."""
    site = PROJECT_ROOT / "site"
    wf_dir = site / "reference" / "workflows"
    assert wf_dir.exists(), "reference/workflows/ missing"
    wf_pages = list(wf_dir.rglob("index.html"))
    assert len(wf_pages) >= 5, f"Expected 5+ workflow pages, got {len(wf_pages)}"


def test_template_pages_generated():
    """Template reference pages exist."""
    site = PROJECT_ROOT / "site"
    tpl_dir = site / "reference" / "templates"
    assert tpl_dir.exists(), "reference/templates/ missing"
    tpl_pages = list(tpl_dir.rglob("index.html"))
    assert len(tpl_pages) >= 5, f"Expected 5+ template pages, got {len(tpl_pages)}"


def test_frontmatter_in_generated_pages():
    """Generated pages have YAML frontmatter (title/source)."""
    site = PROJECT_ROOT / "site"
    # Check knowledge-index page title in HTML
    page = site / "knowledge-index" / "index.html"
    if page.exists():
        content = page.read_text(encoding="utf-8")
        # MkDocs Material puts the title in <title> tag
        assert "<title>" in content


# --- Reference Resolution Spot-Checks ---
# These tests verify that gen_docs resolved text references into HTML links.


def test_decision_refs_resolved_in_knowledge_index():
    """D{N} references in knowledge-index resolve to #architecture-decisions anchors."""
    site = PROJECT_ROOT / "site"
    page = site / "knowledge-index" / "index.html"
    if not page.exists():
        pytest.skip("knowledge-index page not built")
    content = page.read_text(encoding="utf-8")
    # D{N} refs should be resolved to anchor links (relative URL format)
    assert "#architecture-decisions" in content, \
           "D{N} references not resolved in knowledge-index"


def test_artifact_refs_resolved_in_knowledge_topics():
    """Knowledge topic files contain resolved links to task artifacts."""
    site = PROJECT_ROOT / "site"
    knowledge_dir = site / "knowledge"
    if not knowledge_dir.exists():
        pytest.skip("knowledge/ not built")
    # At least one knowledge topic should have resolved task links
    found_task_link = False
    for page in knowledge_dir.rglob("index.html"):
        content = page.read_text(encoding="utf-8")
        if "/tasks/" in content:
            found_task_link = True
            break
    assert found_task_link, \
        "No resolved artifact references found in any knowledge/ topic page"


def test_td_refs_resolved_in_output():
    """TD-{N} references resolve to /reference/tech-debt.md links."""
    site = PROJECT_ROOT / "site"
    # Search across all pages for resolved TD links
    found_td_link = False
    for page in site.rglob("index.html"):
        content = page.read_text(encoding="utf-8")
        if "/reference/tech-debt/" in content:
            found_td_link = True
            break
    assert found_td_link, "No resolved TD-{N} references found in site output"


def test_index_override_used():
    """When docs/index.md exists, it should be used instead of README.md."""
    site = PROJECT_ROOT / "site"
    index = site / "index.html"
    assert index.exists(), "index.html missing"
    content = index.read_text(encoding="utf-8")
    override = PROJECT_ROOT / "docs" / "index.md"
    if override.exists():
        override_text = override.read_text(encoding="utf-8")
        # The index page should contain text from docs/index.md, not README.md's Task Board
        if "Getting Started" in override_text:
            assert "Getting Started" in content, "Index override not applied"


def test_section_index_pages_generated():
    """Glob sections have auto-generated index pages (tasks/, knowledge/, etc.)."""
    site = PROJECT_ROOT / "site"
    for section in ["tasks", "knowledge"]:
        index = site / section / "index.html"
        assert index.exists(), f"{section}/index.html missing"
        content = index.read_text(encoding="utf-8")
        # Index should list pages as links
        assert "<a" in content, f"{section} index has no links"


def test_resolved_links_use_directory_urls():
    """Resolved artifact links use directory URLs (no .md extension)."""
    site = PROJECT_ROOT / "site"
    knowledge_dir = site / "knowledge"
    if not knowledge_dir.exists():
        pytest.skip("knowledge/ not built")
    for page in knowledge_dir.rglob("index.html"):
        content = page.read_text(encoding="utf-8")
        # Check that links to /tasks/ don't end with .md
        import re
        md_links = re.findall(r'href="/tasks/[^"]*\.md"', content)
        assert not md_links, f"Found .md links in {page}: {md_links[:3]}"
