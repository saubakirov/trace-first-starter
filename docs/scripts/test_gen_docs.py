"""Unit tests for gen_docs.py transformation functions.

Tests run WITHOUT mkdocs-gen-files — only pure logic functions.
"""

import sys
from pathlib import Path

import pytest

# Add scripts dir to path so we can import gen_docs functions
# without triggering the module-level main() call (which needs mkdocs_gen_files)
sys.modules["mkdocs_gen_files"] = type(sys)("mkdocs_gen_files")  # mock module

from gen_docs import (
    extract_title,
    add_frontmatter,
    resolve_references,
    validate_sources,
    _glob_base,
    _read_task_prefix,
    _normalize_posix_path,
    _posix_relpath,
    rewrite_markdown_links,
    add_table_anchors,
)


# --- extract_title ---


class TestExtractTitle:
    def test_heading_found(self):
        assert extract_title("# My Title\nContent", "file.md") == "My Title"

    def test_no_heading_fallback_to_filename(self):
        assert extract_title("No heading here", "my_file.md") == "My File"

    def test_heading_with_special_chars(self):
        assert (
            extract_title("# RF — TFW-26 / Phase A", "rf.md")
            == "RF — TFW-26 / Phase A"
        )

    def test_second_level_heading_ignored(self):
        assert extract_title("## Not H1\ntext", "fallback.md") == "Fallback"

    def test_heading_with_trailing_whitespace(self):
        assert extract_title("# Title   \nBody", "f.md") == "Title"

    def test_nested_path_filename(self):
        result = extract_title("no heading", "tasks/TFW-18__knowledge/RF__TFW-18.md")
        assert result == "Rf  Tfw-18"


# --- add_frontmatter ---


class TestAddFrontmatter:
    def test_adds_frontmatter(self):
        result = add_frontmatter("# Title\nBody", "Title", "src.md")
        assert result.startswith("---")
        assert 'title: "Title"' in result
        assert 'source: "src.md"' in result
        assert "# Title\nBody" in result

    def test_skips_existing_frontmatter(self):
        content = "---\ntitle: Existing\n---\nBody"
        assert add_frontmatter(content, "New", "src.md") == content

    def test_blank_line_after_frontmatter(self):
        result = add_frontmatter("content", "T", "s.md")
        # Should have blank line between frontmatter and content
        assert "---\n\ncontent" in result


# --- _glob_base ---


class TestGlobBase:
    def test_tasks_glob(self):
        assert _glob_base("tasks/**/*.md") == "tasks"

    def test_knowledge_glob(self):
        assert _glob_base("knowledge/*.md") == "knowledge"

    def test_nested_glob(self):
        result = _glob_base(".tfw/workflows/**/*.md")
        assert result.replace("\\", "/") == ".tfw/workflows"

    def test_star_only(self):
        assert _glob_base("*.md") == "."


# --- resolve_references ---


class TestResolveReferences:
    def test_artifact_ref_resolved(self, tmp_path):
        """RF TFW-18 → hyperlink when file exists."""
        task_dir = tmp_path / "tasks" / "TFW-18__knowledge"
        task_dir.mkdir(parents=True)
        (task_dir / "RF__TFW-18__knowledge.md").write_text("# RF")
        content = "Source: RF TFW-18 §6"
        result = resolve_references(content, project_root=tmp_path, task_prefix="TFW")
        assert "[RF TFW-18]" in result
        assert "/tasks/" in result
        assert "RF__TFW-18" in result
        # Should use directory URL, not .md
        assert ".md)" not in result

    def test_unresolved_ref_left_as_text(self, tmp_path):
        """Unresolvable ref stays as plain text."""
        content = "Source: RF TFW-999"
        result = resolve_references(content, project_root=tmp_path, task_prefix="TFW")
        assert "[" not in result or "RF TFW-999" in result
        # Should NOT be wrapped in a link
        assert "](/tasks/" not in result

    def test_existing_link_not_doubled(self, tmp_path):
        """[RF TFW-18](path) should NOT be re-wrapped."""
        content = "[RF TFW-18](tasks/TFW-18/RF.md)"
        result = resolve_references(content, project_root=tmp_path, task_prefix="TFW")
        assert content == result  # unchanged

    def test_hl_dash_ref_resolved(self, tmp_path):
        """HL-TFW-19 → hyperlink when file exists."""
        task_dir = tmp_path / "tasks" / "TFW-19__config"
        task_dir.mkdir(parents=True)
        (task_dir / "HL-TFW-19__config.md").write_text("# HL")
        content = "See HL-TFW-19 for details"
        result = resolve_references(content, project_root=tmp_path, task_prefix="TFW")
        assert "[HL-TFW-19]" in result
        assert "HL-TFW-19__config/" in result
        assert ".md)" not in result

    def test_phase_ref_resolved(self, tmp_path):
        """RF TFW-26/A → hyperlink in PhaseA subfolder."""
        phase_dir = tmp_path / "tasks" / "TFW-26__docs" / "PhaseA"
        phase_dir.mkdir(parents=True)
        (phase_dir / "RF__PhaseA__contract.md").write_text("# RF")
        content = "See RF TFW-26/A"
        result = resolve_references(content, project_root=tmp_path, task_prefix="TFW")
        assert "[RF TFW-26/A]" in result
        assert "PhaseA" in result

    def test_td_ref_resolved(self):
        """TD-59 → link to tech-debt page."""
        content = "See TD-59 for details"
        result = resolve_references(content, project_root=Path("."), task_prefix="TFW")
        assert "[TD-59]" in result
        assert "/reference/tech-debt/" in result

    def test_decision_ref_resolved(self):
        """D24 → link to knowledge-index anchor."""
        content = "Per D24, we use Pattern A"
        result = resolve_references(content, project_root=Path("."), task_prefix="TFW")
        assert "[D24]" in result
        assert "/knowledge-index/#architecture-decisions" in result

    def test_decision_ref_in_table(self):
        """D{N} in table Source column resolves."""
        content = "| D24 | decision |"
        result = resolve_references(content, project_root=Path("."), task_prefix="TFW")
        assert "[D24]" in result

    def test_decision_ref_not_in_backtick(self):
        """`D24` inside backticks should NOT resolve."""
        content = "Use `D24` format"
        result = resolve_references(content, project_root=Path("."), task_prefix="TFW")
        assert "`D24`" in result
        # The backtick-protected ref should not become a link
        assert "[D24]" not in result

    def test_pn_not_resolved(self):
        """P7 should NOT be resolved (deferred to Phase C)."""
        content = "See P7 for philosophy"
        result = resolve_references(content, project_root=Path("."), task_prefix="TFW")
        assert "P7" in result
        assert "[P7]" not in result

    def test_multiple_refs_in_one_line(self, tmp_path):
        """Multiple refs on one line all resolve independently."""
        task_dir = tmp_path / "tasks" / "TFW-18__knowledge"
        task_dir.mkdir(parents=True)
        (task_dir / "RF__TFW-18__knowledge.md").write_text("# RF")
        content = "RF TFW-18 mentions TD-59 and D24"
        result = resolve_references(content, project_root=tmp_path, task_prefix="TFW")
        assert "[RF TFW-18]" in result
        assert "[TD-59]" in result
        assert "[D24]" in result


# --- validate_sources ---


class TestValidateSources:
    def test_required_missing_raises(self, tmp_path):
        """Missing required source raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError, match="README.md"):
            validate_sources(tmp_path)

    def test_optional_missing_warns(self, tmp_path):
        """Missing optional source returns warning string."""
        # Create all required sources
        (tmp_path / "README.md").write_text("# README")
        (tmp_path / ".tfw").mkdir()
        (tmp_path / ".tfw" / "README.md").write_text("# TFW")
        (tmp_path / ".tfw" / "quickstart.md").write_text("# Quick Start")
        (tmp_path / ".tfw" / "conventions.md").write_text("# Conv")
        (tmp_path / ".tfw" / "glossary.md").write_text("# Gloss")
        (tmp_path / ".tfw" / "CHANGELOG.md").write_text("# CL")
        (tmp_path / ".tfw" / "compilable_contract.md").write_text("# CC")
        # KNOWLEDGE.md, TECH_DEBT.md, RELEASE.md are optional
        warnings = validate_sources(tmp_path)
        assert any("KNOWLEDGE.md" in w for w in warnings)

    def test_all_present_no_warnings(self, tmp_path):
        """All sources present → empty warnings list."""
        (tmp_path / "README.md").write_text("# R")
        tfw = tmp_path / ".tfw"
        tfw.mkdir()
        (tfw / "README.md").write_text("# T")
        (tfw / "quickstart.md").write_text("# QS")
        (tfw / "conventions.md").write_text("# C")
        (tfw / "glossary.md").write_text("# G")
        (tfw / "CHANGELOG.md").write_text("# CL")
        (tfw / "compilable_contract.md").write_text("# CC")
        (tmp_path / "KNOWLEDGE.md").write_text("# K")
        (tmp_path / "TECH_DEBT.md").write_text("# TD")
        (tmp_path / "RELEASE.md").write_text("# R")
        assert validate_sources(tmp_path) == []


# --- _read_task_prefix ---


class TestReadTaskPrefix:
    def test_reads_from_config(self, tmp_path):
        tfw = tmp_path / ".tfw"
        tfw.mkdir()
        (tfw / "project_config.yaml").write_text("tfw:\n  task_prefix: MYPROJ\n")
        assert _read_task_prefix(tmp_path) == "MYPROJ"

    def test_default_on_missing(self, tmp_path):
        assert _read_task_prefix(tmp_path) == "PROJ"


# --- _normalize_posix_path ---


class TestNormalizePosixPath:
    def test_basic_path(self):
        assert _normalize_posix_path("a/b/c") == "a/b/c"

    def test_dotdot(self):
        assert _normalize_posix_path(".tfw/../README.md") == "README.md"

    def test_dot(self):
        assert _normalize_posix_path("./conventions.md") == "conventions.md"

    def test_empty(self):
        assert _normalize_posix_path("") == "."

    def test_backslash(self):
        assert _normalize_posix_path(".tfw\\README.md") == ".tfw/README.md"


# --- _posix_relpath ---


class TestPosixRelpath:
    def test_sibling_dirs(self):
        assert _posix_relpath("reference/conventions.md", "concepts") == "../reference/conventions.md"

    def test_same_dir(self):
        assert _posix_relpath("reference/glossary.md", "reference") == "glossary.md"

    def test_root_base(self):
        assert _posix_relpath("concepts/philosophy.md", ".") == "concepts/philosophy.md"

    def test_empty_base(self):
        assert _posix_relpath("concepts/philosophy.md", "") == "concepts/philosophy.md"

    def test_deep_to_root(self):
        assert _posix_relpath("index.md", "reference/workflows") == "../../index.md"


# --- rewrite_markdown_links ---


class TestRewriteMarkdownLinks:
    def test_sibling_link_rewritten(self):
        path_map = {
            ".tfw/conventions.md": "reference/conventions.md",
            ".tfw/README.md": "concepts/philosophy.md",
        }
        content = "See [conventions.md](conventions.md) for details"
        result = rewrite_markdown_links(content, ".tfw/README.md", path_map)
        assert "../reference/conventions.md" in result

    def test_external_link_unchanged(self):
        content = "[link](https://example.com)"
        result = rewrite_markdown_links(content, "README.md", {})
        assert result == content

    def test_anchor_preserved(self):
        path_map = {
            ".tfw/conventions.md": "reference/conventions.md",
            ".tfw/README.md": "concepts/philosophy.md",
        }
        content = "[section](conventions.md#section-1)"
        result = rewrite_markdown_links(content, ".tfw/README.md", path_map)
        assert "../reference/conventions.md#section-1" in result

    def test_absolute_link_unchanged(self):
        content = "[link](/absolute/path.md)"
        result = rewrite_markdown_links(content, "README.md", {})
        assert result == content

    def test_template_placeholder_neutralized(self):
        content = "[HL](../../HL-{PREFIX}-{N}__{title}.md)"
        result = rewrite_markdown_links(content, ".tfw/templates/RES.md", {})
        assert "{PREFIX}" not in result or "`HL`" in result

    def test_image_link_unchanged(self):
        content = "[logo](brand/logo.png)"
        result = rewrite_markdown_links(content, "README.md", {})
        assert result == content

    def test_unknown_target_unchanged(self):
        content = "[link](unknown/file.md)"
        result = rewrite_markdown_links(content, "README.md", {})
        assert result == content


# --- add_table_anchors ---


class TestAddTableAnchors:
    def test_decision_anchor(self):
        content = "| D24 | Architecture decision |"
        result = add_table_anchors(content)
        assert '<span id="d24">D24</span>' in result

    def test_td_anchor(self):
        content = "| TD-72 | Some tech debt |"
        result = add_table_anchors(content)
        assert '<span id="td-72">TD-72</span>' in result

    def test_principle_anchor(self):
        content = "| P7 | Philosophy principle |"
        result = add_table_anchors(content)
        assert '<span id="p7">P7</span>' in result

    def test_no_anchor_in_text(self):
        content = "The decision D24 is important"
        result = add_table_anchors(content)
        assert result == content  # No change — D24 not at start of table row

    def test_header_row_unchanged(self):
        content = "| ID | Description |"
        result = add_table_anchors(content)
        assert result == content


# --- bare task ID resolver ---


class TestBareTaskIdResolver:
    def test_bare_id_resolved(self, tmp_path):
        task_dir = tmp_path / "tasks" / "TFW-18__knowledge"
        task_dir.mkdir(parents=True)
        (task_dir / "HL-TFW-18__knowledge.md").write_text("# HL")
        content = "See TFW-18 for details"
        result = resolve_references(content, project_root=tmp_path, task_prefix="TFW")
        assert "[TFW-18]" in result
        assert "TFW-18__knowledge" in result

    def test_bare_id_in_existing_link_skipped(self, tmp_path):
        content = "[TFW-18](tasks/TFW-18/something)"
        result = resolve_references(content, project_root=tmp_path, task_prefix="TFW")
        assert content == result

    def test_bare_id_with_suffix_skipped(self, tmp_path):
        content = "TFW-18__knowledge_consolidation"
        result = resolve_references(content, project_root=tmp_path, task_prefix="TFW")
        assert "[TFW-18__" not in result

    def test_bare_id_no_folder_unchanged(self, tmp_path):
        content = "See TFW-999"
        result = resolve_references(content, project_root=tmp_path, task_prefix="TFW")
        assert "[TFW-999]" not in result
