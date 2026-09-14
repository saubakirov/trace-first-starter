"""Small unit suite for the public documentation generator."""

import sys
from pathlib import Path

import pytest
import yaml

sys.modules["mkdocs_gen_files"] = type(sys)("mkdocs_gen_files")

from gen_docs import (  # noqa: E402
    _glob_base,
    _glob_output_path,
    _normalize_posix_path,
    _posix_relpath,
    add_frontmatter,
    extract_title,
    rewrite_markdown_links,
    validate_sources,
)


def _frontmatter(rendered: str) -> dict:
    return yaml.safe_load(rendered.split("---", 2)[1])


def test_extract_title_uses_heading():
    assert extract_title("# My Title\nContent", "file.md") == "My Title"


def test_extract_title_falls_back_to_filename():
    assert extract_title("No heading", ".tfw/my_file.md") == "My File"


@pytest.mark.parametrize("title", ['Quoted "title"', "Title: detail", "%directive"])
def test_frontmatter_is_yaml_serialized(title):
    rendered = add_frontmatter("body", title, ".tfw/source.md")
    assert _frontmatter(rendered) == {"title": title, "source": ".tfw/source.md"}


def test_existing_frontmatter_is_preserved():
    content = "---\ntitle: Existing\n---\nBody"
    assert add_frontmatter(content, "New", ".tfw/source.md") == content


def test_normalize_posix_path():
    assert _normalize_posix_path(".tfw/workflows/../templates/HL.md") == ".tfw/templates/HL.md"


def test_posix_relative_path():
    assert _posix_relpath("reference/templates/HL.md", "reference/workflows") == "../templates/HL.md"


def test_public_markdown_link_is_rewritten():
    mapping = {
        ".tfw/workflows/plan.md": "reference/workflows/plan.md",
        ".tfw/templates/HL.md": "reference/templates/HL.md",
    }
    content = "[HL](../templates/HL.md) [web](https://example.com)"
    assert rewrite_markdown_links(content, ".tfw/workflows/plan.md", mapping) == (
        "[HL](../templates/HL.md) [web](https://example.com)"
    )


def test_glob_output_mapping():
    base = _glob_base(".tfw/workflows/**/*.md")
    assert base == Path(".tfw/workflows")
    assert _glob_output_path(
        Path(".tfw/workflows/research/base.md"), base, "reference/workflows/"
    ) == "reference/workflows/research/base.md"


def test_missing_required_source_refuses(tmp_path):
    with pytest.raises(FileNotFoundError, match="README.md"):
        validate_sources(tmp_path)
