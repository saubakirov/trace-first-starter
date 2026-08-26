"""Tests for the derived portfolio index.

Two properties carry the weight here. **Determinism**: the same inputs must produce the
same bytes, or the index becomes a source of spurious diffs and nobody trusts a rebuild.
**Non-authority**: the index reports what it cannot read instead of dropping it, and reading
it never changes a task.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gen_index  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parents[2]


# --- the shared resolver ---------------------------------------------------

@pytest.mark.parametrize("text,expected", [
    ("20260826-143000", ("clock", "20260826-143000")),
    ("TFW-60", ("legacy", "TFW-60")),
    ("PROJ-1", ("legacy", "PROJ-1")),
    ("2026-08-26", None),
    ("20260826-14300", None),      # five digits, not six
    ("tfw-60", None),              # lowercase prefix is not the grammar
    ("", None),
])
def test_parse_identifier(text, expected):
    assert gen_index.parse_identifier(text) == expected


def test_legacy_identifiers_sort_numerically():
    """TFW-9 before TFW-10. Lexical sorting on the raw string gets this wrong."""
    ids = ["TFW-10", "TFW-9", "TFW-100", "TFW-1"]
    ordered = sorted(ids, key=lambda i: gen_index.sort_key(*gen_index.parse_identifier(i)))
    assert ordered == ["TFW-1", "TFW-9", "TFW-10", "TFW-100"]


def test_legacy_sorts_before_clock_and_newest_is_last():
    ids = ["20260826-090000", "TFW-60", "20250101-000000"]
    ordered = sorted(ids, key=lambda i: gen_index.sort_key(*gen_index.parse_identifier(i)))
    assert ordered == ["TFW-60", "20250101-000000", "20260826-090000"]


# --- fixtures --------------------------------------------------------------

def _status(**overrides) -> str:
    fields = {
        "id": "20260826-120000", "title": "Fixture task", "goal": "why it exists",
        "value": "what it gives", "lifecycle": "TODO", "owner": "saubakirov",
        "authority": "HL.md", "created": "2026-08-26", "updated": "2026-08-26",
    }
    fields.update(overrides)
    body = "\n".join(f"{k}: {v}" for k, v in fields.items())
    return f"---\n{body}\n---\n\n**Task state.**\n"


def _project(tmp_path: Path, containers=("workspace", "tasks")) -> Path:
    (tmp_path / ".tfw").mkdir()
    listed = ", ".join(containers)
    (tmp_path / ".tfw" / "project_config.yaml").write_text(
        f"tfw:\n  task_containers: [{listed}]\n", encoding="utf-8")
    return tmp_path


def _task(root: Path, rel: str, **overrides) -> Path:
    path = root / rel
    path.mkdir(parents=True)
    (path / "status.md").write_text(_status(**overrides), encoding="utf-8")
    return path


# --- discovery -------------------------------------------------------------

def test_finds_year_nested_and_flat_tasks(tmp_path):
    root = _project(tmp_path)
    _task(root, "workspace/2026/20260826-120000__new", id="20260826-120000")
    _task(root, "tasks/TFW-1__legacy", id="TFW-1")
    found = [p.name for p in gen_index.iter_task_dirs(root)]
    assert found == ["TFW-1__legacy", "20260826-120000__new"]


def test_ignores_directories_that_are_not_tasks(tmp_path):
    root = _project(tmp_path)
    _task(root, "tasks/TFW-1__legacy", id="TFW-1")
    (root / "tasks" / "notes").mkdir()
    (root / "tasks" / "no-double-underscore").mkdir()
    (root / "workspace").mkdir()
    assert [p.name for p in gen_index.iter_task_dirs(root)] == ["TFW-1__legacy"]


def test_container_key_is_configuration_not_a_literal(tmp_path):
    """Two different container values both resolve. Nothing hardcodes `tasks/`."""
    root = _project(tmp_path, containers=("alpha",))
    _task(root, "alpha/2026/20260826-120000__one", id="20260826-120000")
    assert len(gen_index.iter_task_dirs(root)) == 1
    (root / ".tfw" / "project_config.yaml").write_text(
        "tfw:\n  task_containers: [beta]\n", encoding="utf-8")
    assert gen_index.iter_task_dirs(root) == []


def test_default_container_when_config_is_silent(tmp_path):
    (tmp_path / ".tfw").mkdir()
    (tmp_path / ".tfw" / "project_config.yaml").write_text("tfw: {}\n", encoding="utf-8")
    assert gen_index.task_containers(tmp_path) == ["tasks"]


# --- reading task state ----------------------------------------------------

def test_reads_valid_status(tmp_path):
    root = _project(tmp_path)
    task = _task(root, "tasks/TFW-1__x", id="TFW-1", title="Readable")
    data = gen_index.read_status(task)
    assert data["title"] == "Readable"
    assert "_error" not in data


def test_absent_status_is_not_an_error(tmp_path):
    root = _project(tmp_path)
    (root / "tasks" / "TFW-1__x").mkdir(parents=True)
    assert gen_index.read_status(root / "tasks" / "TFW-1__x") is None


@pytest.mark.parametrize("content,fragment", [
    ("no front matter at all\n", "no YAML front matter"),
    ("---\n: : :\n---\n", "unparseable"),
    ("---\njust a string\n---\n", "not a mapping"),
])
def test_malformed_status_is_reported_not_raised(tmp_path, content, fragment):
    root = _project(tmp_path)
    task = root / "tasks" / "TFW-1__x"
    task.mkdir(parents=True)
    (task / "status.md").write_text(content, encoding="utf-8")
    assert fragment in gen_index.read_status(task)["_error"]


def test_unknown_key_is_reported(tmp_path):
    """The key set is closed. A field nobody reads does not belong in task state."""
    root = _project(tmp_path)
    task = root / "tasks" / "TFW-1__x"
    task.mkdir(parents=True)
    (task / "status.md").write_text(_status().replace("owner:", "journal_head: 3\nowner:"),
                                    encoding="utf-8")
    assert "unknown keys: journal_head" in gen_index.read_status(task)["_error"]


def test_bounds_are_enforced(tmp_path):
    root = _project(tmp_path)
    task = _task(root, "tasks/TFW-1__x", goal="g" * 161)
    assert "goal exceeds 160" in gen_index.read_status(task)["_error"]


# --- the index itself ------------------------------------------------------

def test_generation_is_byte_identical_across_runs(tmp_path):
    root = _project(tmp_path)
    _task(root, "tasks/TFW-1__a", id="TFW-1")
    _task(root, "workspace/2026/20260826-120000__b", id="20260826-120000")
    assert gen_index.build(root) == gen_index.build(root)


def test_freshness_comes_from_inputs_not_the_clock(tmp_path):
    """A wall-clock stamp would make two runs a minute apart differ."""
    root = _project(tmp_path)
    _task(root, "tasks/TFW-1__a", id="TFW-1", updated="2026-01-05")
    _task(root, "tasks/TFW-2__b", id="TFW-2", updated="2026-07-30")
    assert "2026-07-30" in gen_index.build(root)


def test_index_declares_that_it_is_derived(tmp_path):
    root = _project(tmp_path)
    _task(root, "tasks/TFW-1__a", id="TFW-1")
    content = gen_index.build(root)
    assert "derived and non-authoritative" in content
    assert "1 task state files" in content


def test_unresolved_inputs_are_reported_never_dropped(tmp_path):
    root = _project(tmp_path)
    _task(root, "tasks/TFW-1__ok", id="TFW-1")
    broken = root / "tasks" / "TFW-2__broken"
    broken.mkdir(parents=True)
    (broken / "status.md").write_text("not front matter\n", encoding="utf-8")
    silent = root / "tasks" / "TFW-3__silent"
    silent.mkdir(parents=True)

    content = gen_index.build(root)
    assert "TFW-2__broken" in content and "TFW-3__silent" in content
    assert "| Unresolved inputs | 2 |" in content


def test_undeclared_lifecycle_is_shown_with_its_verbatim_value(tmp_path):
    root = _project(tmp_path)
    task = root / "tasks" / "TFW-45__x"
    task.mkdir(parents=True)
    (task / "status.md").write_text(
        _status(id="TFW-45", lifecycle="UNDECLARED").replace(
            "owner:", "lifecycle_verbatim: ❄️ FROZEN\nowner:"),
        encoding="utf-8")
    content = gen_index.build(root)
    assert "UNDECLARED (`❄️ FROZEN`)" in content


def test_generating_the_index_changes_no_task_state(tmp_path):
    root = _project(tmp_path)
    task = _task(root, "tasks/TFW-1__a", id="TFW-1")
    before = (task / "status.md").read_bytes()
    gen_index.build(root)
    assert (task / "status.md").read_bytes() == before


def test_check_mode_detects_a_stale_index(tmp_path):
    root = _project(tmp_path)
    _task(root, "tasks/TFW-1__a", id="TFW-1")
    (root / "workspace").mkdir(exist_ok=True)
    assert gen_index.main(["--root", str(root)]) == 0
    assert gen_index.main(["--root", str(root), "--check"]) == 0
    _task(root, "tasks/TFW-2__b", id="TFW-2")
    assert gen_index.main(["--root", str(root), "--check"]) == 1


# --- the real repository ---------------------------------------------------

def test_committed_index_is_current():
    """The index in the tree matches what the generator produces from task state."""
    assert gen_index.main(["--root", str(PROJECT_ROOT), "--check"]) == 0
