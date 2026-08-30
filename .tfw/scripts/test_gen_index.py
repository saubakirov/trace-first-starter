"""Tests for the derived portfolio index.

Two properties carry the weight here. **Determinism**: the same inputs must produce the
same bytes, or the index becomes a source of spurious diffs and nobody trusts a rebuild.
**Non-authority**: the index reports what it cannot read instead of dropping it, and reading
it never changes a task.
"""

from __future__ import annotations

import pathlib
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gen_index  # noqa: E402

# Found by marker, not by counting directories up. The module under test stopped
# depending on its own depth in this phase; a test that still does would break
# confusingly the moment a project places these tools somewhere else.
PROJECT_ROOT = gen_index.find_project_root(Path(__file__))


# --- the shared resolver ---------------------------------------------------

@pytest.mark.parametrize("text,expected", [
    # Current: three fields, single separators, every field whole.
    ("TFW_20260829-010832_CRSW", ("current", "TFW_20260829-010832_CRSW")),
    ("HD_20260829-010832_30B", ("current", "HD_20260829-010832_30B")),
    # The clock identifier is the WHOLE directory name.
    ("20260826-143000__query_redesign", ("clock", "20260826-143000__query_redesign")),
    ("20260826-143000__a", ("clock", "20260826-143000__a")),
    # A bare timestamp is NOT an identifier: it cannot name exactly one task.
    ("20260826-143000", None),
    # Legacy keeps its own grammar, and the slug is not part of the identifier.
    ("TFW-60", ("legacy", "TFW-60")),
    ("TFW-60__conflict_resistant_shared_workspace", ("legacy", "TFW-60")),
    ("PROJ-1", ("legacy", "PROJ-1")),
    ("2026-08-26", None),
    ("20260826-14300__x", None),   # five digits, not six
    ("tfw-60", None),              # lowercase prefix is not the grammar
    ("tfw_20260829-010832_AB", None),
    ("TFW_20260829-010832_ab", None),
    ("TFW_20260829-010832_AB_more", None),
    ("TFW__20260829-010832_AB", None),
    ("2026", None),                # a year folder is not a task
    ("", None),
])
def test_parse_identifier(text, expected):
    assert gen_index.parse_identifier(text) == expected


def test_a_bare_timestamp_is_never_accepted_as_an_identifier():
    """R3/F1. Two mutually offline participants can reach the same second.

    Only the slug distinguishes them, so a consumer handed a bare stamp cannot know which
    task is meant. Rejecting it is the whole point: revision 2 accepted it and then promised
    offline uniqueness of it, which could not hold.
    """
    assert gen_index.parse_identifier("20260826-143000") is None
    assert gen_index.BARE_STAMP.match("20260826-143000")


def test_same_second_different_slug_are_two_distinct_identifiers(tmp_path):
    """The case revision 2 could not express, and the fixture avoided."""
    a = gen_index.parse_identifier("20260826-143000__alpha")
    b = gen_index.parse_identifier("20260826-143000__beta")
    assert a is not None and b is not None
    assert a[1] != b[1], "same second with different slugs must be different identifiers"
    assert gen_index.sort_key(*a) != gen_index.sort_key(*b)


def test_same_second_same_slug_is_the_same_identifier():
    """Two offline participants who agree on second AND slug created the same task.

    That is a signal worth surfacing, not a defect to prevent — and the resolver says so by
    returning one identifier rather than two.
    """
    a = gen_index.parse_identifier("20260826-143000__alpha")
    b = gen_index.parse_identifier("20260826-143000__alpha")
    assert a == b


def test_legacy_identifiers_sort_numerically():
    """TFW-9 before TFW-10. Lexical sorting on the raw string gets this wrong."""
    ids = ["TFW-10", "TFW-9", "TFW-100", "TFW-1"]
    ordered = sorted(ids, key=lambda i: gen_index.sort_key(*gen_index.parse_identifier(i)))
    assert ordered == ["TFW-1", "TFW-9", "TFW-10", "TFW-100"]


def test_legacy_sorts_before_clock_and_newest_is_last():
    ids = ["TFW_20260826-090000_C", "20260826-090000__c", "TFW-60",
           "20250101-000000__a"]
    ordered = sorted(ids, key=lambda i: gen_index.sort_key(*gen_index.parse_identifier(i)))
    assert ordered == ["TFW-60", "20250101-000000__a", "20260826-090000__c",
                       "TFW_20260826-090000_C"]


def test_same_second_tasks_order_by_slug_not_by_filesystem():
    ids = ["20260826-090000__zeta", "20260826-090000__alpha"]
    ordered = sorted(ids, key=lambda i: gen_index.sort_key(*gen_index.parse_identifier(i)))
    assert ordered == ["20260826-090000__alpha", "20260826-090000__zeta"]


# --- fixtures --------------------------------------------------------------

def _status(**overrides) -> str:
    fields = {
        "id": "20260826-120000__fixture", "title": "Fixture task", "goal": "why it exists",
        "value": "what it gives", "lifecycle": "TODO", "owner": "saubakirov",
        "authority": "HL.md", "created": "20260826-120000", "updated": "20260826-120000",
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
    """Create a task directory whose state agrees with its own name, unless overridden."""
    path = root / rel
    path.mkdir(parents=True)
    parsed = gen_index.parse_identifier(path.name)
    if parsed and "id" not in overrides:
        overrides["id"] = parsed[1]
    (path / "status.md").write_text(_status(**overrides), encoding="utf-8")
    return path


# --- discovery -------------------------------------------------------------

def test_finds_year_nested_and_flat_tasks(tmp_path):
    root = _project(tmp_path)
    _task(root, "workspace/2026/20260826-120000__new")
    _task(root, "tasks/TFW-1__legacy", id="TFW-1")
    found = [p.name for p in gen_index.iter_task_dirs(root)]
    assert found == ["TFW-1__legacy", "20260826-120000__new"]


def test_a_directory_that_is_not_a_task_is_reported_never_dropped(tmp_path):
    """It is excluded from the task list AND surfaced. Both halves, or neither counts.

    Previously it was only excluded — `continue`d out of the walk before any consumer could
    see it. That is how a real external corpus of four tasks was read as two.
    """
    root = _project(tmp_path)
    _task(root, "tasks/TFW-1__legacy", id="TFW-1")
    (root / "tasks" / "notes").mkdir()
    (root / "tasks" / "no-double-underscore").mkdir()
    (root / "workspace").mkdir()
    assert [p.name for p in gen_index.iter_task_dirs(root)] == ["TFW-1__legacy"]
    reported = {p.name for p in gen_index.iter_unmatched_task_dirs(root)}
    assert reported == {"notes", "no-double-underscore"}


def test_container_key_is_configuration_not_a_literal(tmp_path):
    """Two different container values both resolve. Nothing hardcodes `tasks/`."""
    root = _project(tmp_path, containers=("alpha",))
    _task(root, "alpha/2026/20260826-120000__one")
    assert len(gen_index.iter_task_dirs(root)) == 1
    (root / ".tfw" / "project_config.yaml").write_text(
        "tfw:\n  task_containers: [beta]\n", encoding="utf-8")
    assert gen_index.iter_task_dirs(root) == []


def test_default_container_when_config_is_silent(tmp_path):
    (tmp_path / ".tfw").mkdir()
    (tmp_path / ".tfw" / "project_config.yaml").write_text("tfw: {}\n", encoding="utf-8")
    assert gen_index.task_containers(tmp_path) == ["tasks"]


def test_two_directories_resolving_to_one_identifier_stop_and_name_both(tmp_path):
    root = _project(tmp_path, containers=("tasks",))
    _task(root, "tasks/TFW-1__alpha", id="TFW-1")
    _task(root, "tasks/TFW-1__beta", id="TFW-1")

    with pytest.raises(gen_index.IdentifierCollisionError) as caught:
        gen_index.iter_task_dirs(root)

    message = str(caught.value)
    assert "TFW-1" in message
    assert "tasks/TFW-1__alpha" in message
    assert "tasks/TFW-1__beta" in message


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


# --- the full closed schema (review F6) ------------------------------------

def test_every_required_key_is_enforced(tmp_path):
    """F6. Revision 2 checked five keys of nine and called the schema closed."""
    root = _project(tmp_path)
    for key in gen_index.REQUIRED_KEYS:
        task = root / "tasks" / f"TFW-1__x"
        if task.exists():
            (task / "status.md").unlink()
        else:
            task.mkdir(parents=True)
        fields = {"id": "TFW-1"}
        text = _status(**fields)
        # drop the key under test
        kept = [ln for ln in text.splitlines() if not ln.startswith(f"{key}:")]
        (task / "status.md").write_text("\n".join(kept) + "\n", encoding="utf-8")
        error = gen_index.read_status(task).get("_error", "")
        assert f"missing {key}" in error, f"{key} was not enforced: {error!r}"


def test_lifecycle_must_come_from_the_declared_vocabulary(tmp_path):
    root = _project(tmp_path)
    task = _task(root, "tasks/TFW-1__x", lifecycle="SHIPPED")
    error = gen_index.read_status(task)["_error"]
    assert "not declared" in error and "SHIPPED" in error


def test_undeclared_lifecycle_requires_the_verbatim_value(tmp_path):
    """UNDECLARED without the original value loses the fact it exists to preserve."""
    root = _project(tmp_path)
    task = _task(root, "tasks/TFW-1__x", lifecycle="UNDECLARED")
    assert "lifecycle_verbatim is absent" in gen_index.read_status(task)["_error"]


def test_verbatim_value_without_undeclared_is_rejected(tmp_path):
    root = _project(tmp_path)
    task = _task(root, "tasks/TFW-1__x", lifecycle="TODO", lifecycle_verbatim="FROZEN")
    assert "only meaningful when lifecycle is UNDECLARED" in gen_index.read_status(task)["_error"]


def test_terminal_lifecycle_requires_an_outcome(tmp_path):
    root = _project(tmp_path)
    task = _task(root, "tasks/TFW-1__x", lifecycle="DONE")
    assert "outcome is absent" in gen_index.read_status(task)["_error"]


def test_outcome_on_a_live_task_is_rejected(tmp_path):
    """An outcome on a running task claims a result that has not happened."""
    root = _project(tmp_path)
    task = _task(root, "tasks/TFW-1__x", lifecycle="RF", outcome="shipped")
    assert "has not reached a terminal lifecycle" in gen_index.read_status(task)["_error"]


@pytest.mark.parametrize("value", [
    "26-08-2026", "2026/08/26", "August 2026", "20260826",
    "2026-08-26",   # day resolution: the precision AC-12 replaced
])
def test_stamps_must_be_second_resolution_or_unrecorded(tmp_path, value):
    """AC-12. One file carrying two precisions is what this closes.

    At day resolution `created` and `updated` are routinely identical on a corpus taking
    several transitions a day — the rejected pass shipped TFW-60 exactly that way — so
    `updated` stopped answering the question it exists for.
    """
    root = _project(tmp_path)
    task = _task(root, "tasks/TFW-1__x", created=value)
    assert "not YYYYMMDD-HHMMSS" in gen_index.read_status(task)["_error"]


def test_unrecorded_is_an_accepted_stamp(tmp_path):
    """Migration writes it when the source held no date. Absence is a fact, not an error."""
    root = _project(tmp_path)
    task = _task(root, "tasks/TFW-1__x", created="unrecorded")
    assert "_error" not in gen_index.read_status(task)


def test_id_must_agree_with_its_own_directory(tmp_path):
    """A state file naming a different task is worse than a missing one."""
    root = _project(tmp_path)
    task = _task(root, "tasks/TFW-1__x", id="TFW-999")
    error = gen_index.read_status(task)["_error"]
    assert "disagrees with its directory" in error and "TFW-1" in error


def test_a_clock_task_id_is_the_whole_directory_name(tmp_path):
    root = _project(tmp_path)
    good = _task(root, "workspace/2026/20260826-120000__alpha")
    assert "_error" not in gen_index.read_status(good)
    bad = _task(root, "workspace/2026/20260826-120001__beta", id="20260826-120001")
    assert "disagrees with its directory" in gen_index.read_status(bad)["_error"]


def test_a_malformed_state_file_stays_visible_and_non_actionable(tmp_path):
    """F6. Every schema breach must reach the index as a reported input."""
    root = _project(tmp_path)
    _task(root, "tasks/TFW-1__ok")
    _task(root, "tasks/TFW-2__broken", lifecycle="SHIPPED")
    content = gen_index.build(root)
    assert "TFW-2__broken" in content
    assert "Unresolved inputs — 1" in content
    assert "In flight — 1" in content, "a malformed task must not appear as actionable"


# --- the index itself ------------------------------------------------------

def test_generation_is_byte_identical_across_runs(tmp_path):
    root = _project(tmp_path)
    _task(root, "tasks/TFW-1__a", id="TFW-1")
    _task(root, "workspace/2026/20260826-120000__b")
    assert gen_index.build(root) == gen_index.build(root)


def test_freshness_comes_from_inputs_not_the_clock(tmp_path):
    """A wall-clock stamp would make two runs a minute apart differ."""
    root = _project(tmp_path)
    _task(root, "tasks/TFW-1__a", id="TFW-1", updated="20260105-090000")
    _task(root, "tasks/TFW-2__b", id="TFW-2", updated="20260730-140000")
    assert "20260730-140000" in gen_index.build(root)


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
    assert gen_index.main(["--root", str(root), "--check", "index"]) == 0
    _task(root, "tasks/TFW-2__b", id="TFW-2")
    assert gen_index.main(["--root", str(root), "--check", "index"]) == 1


# --- a phase carries its own state (AC-12) ---------------------------------

def _phase(task: Path, letter: str, **overrides) -> Path:
    phase = task / f"phase-{letter}"
    phase.mkdir(parents=True, exist_ok=True)
    parsed = gen_index.parse_identifier(task.name)
    fields = {"id": parsed[1] if parsed else task.name,
              "title": f"Phase {letter.upper()}",
              "authority": f"TS__phase-{letter}__x.md"}
    fields.update(overrides)
    (phase / "status.md").write_text(_status(**fields), encoding="utf-8")
    return phase


def test_a_phase_carries_its_own_state(tmp_path):
    root = _project(tmp_path)
    task = _task(root, "workspace/2026/20260826-120000__multi", lifecycle="PHASES")
    _phase(task, "a", lifecycle="DONE", outcome="shipped", owner="saubakirov")
    _phase(task, "b", lifecycle="RF", owner="reviewer")
    phases = gen_index.iter_phase_dirs(task)
    assert [p.name for p in phases] == ["phase-a", "phase-b"]
    assert gen_index.read_phase_status(phases[0])["lifecycle"] == "DONE"
    assert gen_index.read_phase_status(phases[1])["lifecycle"] == "RF"


def test_two_phases_under_two_owners_write_two_different_files(tmp_path):
    """The AC-12 gate: concurrent phases must not touch each other's files."""
    root = _project(tmp_path)
    task = _task(root, "workspace/2026/20260826-120000__multi", lifecycle="PHASES")
    a = _phase(task, "a", lifecycle="ONB", owner="saubakirov")
    b = _phase(task, "b", lifecycle="ONB", owner="reviewer")
    everything = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}

    _phase(task, "a", lifecycle="RF", owner="saubakirov")      # owner A advances A
    _phase(task, "b", lifecycle="REV", owner="reviewer")       # owner B advances B

    changed = sorted(p.relative_to(root).as_posix() for p, before in everything.items()
                     if p.read_bytes() != before)
    assert changed == [
        "workspace/2026/20260826-120000__multi/phase-a/status.md",
        "workspace/2026/20260826-120000__multi/phase-b/status.md",
    ], changed
    # and the task's own file was not touched by either
    assert (task / "status.md").read_bytes() == everything[task / "status.md"]


def test_the_task_file_never_summarizes_phase_state(tmp_path):
    """A rollup is a second fact that must agree with the phases — the very problem the
    carrier forbids. PHASES says 'phases are running' and nothing more."""
    root = _project(tmp_path)
    task = _task(root, "workspace/2026/20260826-120000__multi", lifecycle="PHASES")
    _phase(task, "a", lifecycle="DONE", outcome="shipped")
    _phase(task, "b", lifecycle="RF")
    task_state = gen_index.read_status(task)
    assert task_state["lifecycle"] == "PHASES"
    assert "_error" not in task_state
    # nothing in the task file names a phase or a phase lifecycle
    body = (task / "status.md").read_text(encoding="utf-8")
    assert "phase-a" not in body and "phase-b" not in body


def test_phases_is_a_declared_lifecycle(tmp_path):
    root = _project(tmp_path)
    task = _task(root, "workspace/2026/20260826-120000__multi", lifecycle="PHASES")
    assert "_error" not in gen_index.read_status(task)
    assert "PHASES" in gen_index.DECLARED_LIFECYCLES


def test_the_project_declares_phases_in_its_own_config():
    """The vocabulary is configuration, not a constant in the generator."""
    assert "PHASES" in gen_index.declared_lifecycles(PROJECT_ROOT)


def test_phase_rows_render_beneath_their_task(tmp_path):
    root = _project(tmp_path)
    task = _task(root, "workspace/2026/20260826-120000__multi", lifecycle="PHASES")
    _phase(task, "a", lifecycle="DONE", outcome="shipped", owner="saubakirov")
    _phase(task, "b", lifecycle="RF", owner="reviewer")
    content = gen_index.build(root)
    lines = content.splitlines()
    task_row = next(i for i, l in enumerate(lines) if "20260826-120000__multi/status.md" in l)
    a_row = next(i for i, l in enumerate(lines) if "phase-a/status.md" in l)
    b_row = next(i for i, l in enumerate(lines) if "phase-b/status.md" in l)
    assert task_row < a_row < b_row, "phase rows must follow their task, in order"
    assert "↳" in lines[a_row] and "↳" in lines[b_row]


def test_a_malformed_phase_state_is_reported_not_dropped(tmp_path):
    root = _project(tmp_path)
    task = _task(root, "workspace/2026/20260826-120000__multi", lifecycle="PHASES")
    _phase(task, "a", lifecycle="SHIPPED")
    content = gen_index.build(root)
    assert "phase-a" in content and "not declared" in content


def test_a_phase_without_state_is_not_an_error(tmp_path):
    """A phase file is created when its directory is created, never in advance."""
    root = _project(tmp_path)
    task = _task(root, "workspace/2026/20260826-120000__multi", lifecycle="PHASES")
    (task / "phase-a").mkdir()
    assert gen_index.read_phase_status(task / "phase-a") is None
    assert "Unresolved inputs — 0" in gen_index.build(root)


# --- journal events (review F3) --------------------------------------------

class Clock:
    """A controllable clock that records every reading it was asked for.

    The point of the recording is the assertion: a candidate filename must be traceable to a
    reading. The implementation this replaces took a stamp as a parameter and produced its
    successors by arithmetic, so most candidates had never been read from anything.
    """

    def __init__(self, readings):
        self.readings = list(readings)
        self.taken = []

    def __call__(self):
        value = self.readings[min(len(self.taken), len(self.readings) - 1)]
        self.taken.append(value)
        return value


def test_two_writes_in_one_second_produce_two_files():
    """F3, the case that silently lost an event — now answered by the token.

    Two writers, same kind, same second. Revision 2 named events `<time>__<kind>.md` and
    proved concurrency with two *different* kinds, which cannot collide by construction.
    Then the actor was put in the name to separate writers, and that gave one component two
    jobs. The token does the one job that was actually needed.
    """
    taken = set()
    tokens = iter(["a1b2", "c3d4"])
    first = gen_index.event_filename("handoff", token=lambda: next(tokens), taken=taken,
                                     clock=Clock(["20260826-140000"]))
    taken.add(first)
    second = gen_index.event_filename("handoff", token=lambda: next(tokens), taken=taken,
                                      clock=Clock(["20260826-140000"]))
    assert first == "20260826-140000__handoff__a1b2.md"
    assert second == "20260826-140000__handoff__c3d4.md"
    assert first != second


def test_a_collision_is_redrawn_and_the_clock_is_read_exactly_once():
    """The machinery that waited for the second to change is gone, and should be.

    It existed because the name's uniqueness came from the second, so the only thing that
    could produce a different name was time passing. Uniqueness now comes from the token, so
    a collision is re-drawn. **One clock reading, no sleeping, and nothing to wait for.**
    """
    clock = Clock(["20260826-140000"])
    tokens = iter(["dupe", "dupe", "fresh"])
    taken = {"20260826-140000__handoff__dupe.md"}
    name = gen_index.event_filename("handoff", token=lambda: next(tokens), taken=taken,
                                    clock=clock)
    assert name == "20260826-140000__handoff__fresh.md"
    assert len(clock.taken) == 1, f"the clock must be read once, was {clock.taken}"


def test_no_stamp_is_ever_computed():
    """The prohibition the removed machinery enforced, kept as its own test.

    A stamp is used exactly as it was read: never incremented, never rounded, never composed.
    The arithmetic version wrapped `23:59:59` to `00:00:00` while keeping yesterday's date and
    shipped an event claiming to precede the one it followed. Nothing here can do that,
    because nothing here does arithmetic on a stamp at all.
    """
    source = pathlib.Path(gen_index.__file__).read_text(encoding="utf-8")
    body = source[source.index("def event_filename("):source.index("def validate_event(")]
    for forbidden in ("timedelta", "+ 1", "+1", "strftime", "fromtimestamp", "replace(second"):
        assert forbidden not in body, f"event_filename does arithmetic on a stamp: {forbidden}"

    clock = Clock(["20260826-235959"])
    name = gen_index.event_filename("transition", token=lambda: "aaaa", clock=clock)
    assert name.startswith("20260826-235959"), name
    assert name.split("__")[0] in clock.taken, "the stamp was not one the clock produced"


def test_exhausted_entropy_fails_visibly_and_invents_nothing():
    """No second is invented and no counter is added to get past it."""
    clock = Clock(["20260826-140000"])
    taken = {"20260826-140000__handoff__same.md"}
    with pytest.raises(ValueError) as excinfo:
        gen_index.event_filename("handoff", token=lambda: "same", taken=taken, clock=clock,
                                 attempts=4)
    message = str(excinfo.value)
    assert "entropy problem" in message
    assert "no second is invented" in message
    assert len(clock.taken) == 1, "a stalled draw must not start re-reading the clock"


def test_the_token_is_opaque_and_carries_no_identity():
    """Its single job is that two names differ. If it acquires a second, it is the wrong thing."""
    seen = {gen_index.event_token() for _ in range(200)}
    assert len(seen) > 150, "a token that repeats this often is not doing its one job"
    for value in seen:
        assert gen_index.EVENT_NAME.match(f"20260826-140000__handoff__{value}.md"), value
    # Not an identity: nothing DERIVES it from a handle, a profile or a provider. Scanned
    # over code with the docstring removed -- the docstring legitimately says the token needs
    # no profile, and a check that cannot tell prose from code would flag that sentence.
    body = pathlib.Path(gen_index.__file__).read_text(encoding="utf-8")
    fn = body[body.index("def event_token("):body.index("def event_filename(")]
    opening = fn.index('"""')
    code = fn[fn.index('"""', opening + 3) + 3:]
    for forbidden in ("team", "handle", "profile", "actor", "on_behalf_of", "via"):
        assert forbidden not in code, f"the token derives from {forbidden}, so it is not opaque"


def test_the_default_clock_is_the_system_clock():
    """With no clock injected, the reading is real — not a fixture leaking into production."""
    first = gen_index.read_stamp()
    assert gen_index.STAMP.match(first), first
    name = gen_index.event_filename("created")
    assert gen_index.EVENT_NAME.match(name), name
    assert gen_index.EVENT_NAME.match(name).group("kind") == "created"
    assert gen_index.STAMP.match(name.split("__")[0])


def _event(**overrides) -> dict:
    data = {
        "time": "2026-08-26T14:00:00+05:00", "kind": "transition",
        "actor": "saubakirov", "on_behalf_of": "saubakirov", "via": "claude",
        "from": "ONB", "to": "RF", "refs": ["status.md"], "summary": "moved to execution",
    }
    data.update(overrides)
    return {k: v for k, v in data.items() if v is not None}


@pytest.mark.parametrize("via", ["", "   ", 7])
def test_via_is_free_form_but_non_empty_when_present(via):
    problems = gen_index.validate_event(
        _event(via=via),
        "20260826-140000__transition__a1b2.md",
    )
    assert any("via must be non-empty free-form" in problem for problem in problems)


def test_via_accepts_unregistered_tool_text_and_is_optional_for_hand_edits():
    filename = "20260826-140000__transition__a1b2.md"
    assert gen_index.validate_event(_event(via="local-tool/v7"), filename) == []
    assert gen_index.validate_event(_event(via=None), filename) == []


def test_an_event_without_on_behalf_of_is_refused():
    """There is no such thing as a record nobody answers for."""
    problems = gen_index.validate_event(
        _event(on_behalf_of=None), "20260826-140000__transition__saubakirov.md")
    assert "missing on_behalf_of" in problems


def test_an_actor_is_not_validated_at_all():
    """AC-15 item 3. Tolerated, never required, never rewritten.

    The field carried two jobs — say who wrote this, and make the filename unique — and the
    two contradicted each other: a distinct writer needs a distinct value, a declared handle
    needs a profile. Two external projects resolved it the only way that let work proceed, a
    profile per session; one later deleted those profiles and its gate went red permanently,
    because events are immutable and profiles are not.

    So no rule is applied to it. Not a `team/` comparison, not a provider list, not a shape.
    Any rule would either demand an edit to an immutable file or go red when someone tidies
    `team/`.
    """
    profiles = _human()
    for value in ("claude", "codex", "claude-20260828a", "ghost", "reviewer", "bot"):
        data = _event(actor=value, on_behalf_of="saubakirov")
        problems = gen_index.validate_event(
            data, f"20260826-140000__transition__{value}.md", profiles=profiles)
        assert problems == [], (value, problems)


def test_an_event_with_no_actor_at_all_is_valid():
    """The shape every event written from 2.0.0-dirty.3 on will have."""
    data = {"time": "2026-08-26T20:56:01+05:00", "kind": "transition",
            "on_behalf_of": "saubakirov", "refs": ["status.md"]}
    assert gen_index.validate_event(
        data, "20260826-140000__transition__9f2c.md", profiles=_human()) == []
    assert "actor" not in gen_index.EVENT_REQUIRED
    assert "actor" in gen_index.EVENT_KEYS, "an existing actor must still be an accepted key"


def test_the_filename_is_not_compared_to_the_actor():
    """There is nothing left to compare, so there is no relaxed check — there is no check.

    The third component is a uniqueness token. It agrees with no field by design, and both
    shapes — a historical handle and a new token — match the same pattern, which is what
    makes the ruling cost no project any work.
    """
    data = _event(actor="reviewer", on_behalf_of="saubakirov")
    assert gen_index.validate_event(
        data, "20260826-140000__transition__saubakirov.md", profiles=_human()) == []
    assert gen_index.EVENT_NAME.match(
        "20260826-140000__transition__saubakirov.md").group("token") == "saubakirov"
    assert gen_index.EVENT_NAME.match(
        "20260826-140000__transition__9f2c.md").group("token") == "9f2c"


def test_the_provider_family_list_is_gone():
    """Its only reader was the actor gate. A list nothing reads is surface with no reader."""
    assert not hasattr(gen_index, "PROVIDER_FAMILIES")


def test_a_kind_mismatch_between_filename_and_body_is_still_caught():
    """`kind` still agrees with its filename: that component never had a second job."""
    data = _event(actor="saubakirov", on_behalf_of="saubakirov")
    data["kind"] = "handoff"
    problems = gen_index.validate_event(
        data, "20260826-140000__transition__9f2c.md", profiles=_human())
    assert any("filename says kind" in p for p in problems), problems


def _human(handle="saubakirov"):
    return {handle: {"handle": handle, "type": "human"}}


def test_on_behalf_of_must_name_a_declared_human():
    """AC-14 item 1. Accountability always resolves to a person.

    The previous check only asked whether the handle was declared. A profile declared
    `type: agent` therefore satisfied it, so a record could be answered for by a tool.
    """
    profiles = {"botty": {"handle": "botty", "type": "agent"}}
    problems = gen_index.validate_event(
        _event(actor="botty", on_behalf_of="botty"),
        "20260826-140000__transition__botty.md", profiles=profiles)
    assert any("not human" in p for p in problems), problems


def test_a_human_on_behalf_of_passes():
    problems = gen_index.validate_event(
        _event(), "20260826-140000__transition__saubakirov.md", profiles=_human())
    assert problems == [], problems


def test_an_empty_team_refuses_rather_than_skips():
    """AC-14 item 1. The defect: `or None` turned 'nobody is declared' into 'everybody
    passes', so the rule was unenforced in exactly the case where nothing answers."""
    problems = gen_index.validate_event(
        _event(), "20260826-140000__transition__saubakirov.md", profiles={})
    assert any("team/ declares nobody" in p for p in problems), problems


def test_a_legacy_event_keeps_its_actor_untouched():
    """The journal is immutable. A rule introduced later describes old entries, never edits.

    Scoped, per AC-14 item 2: the escape applies only to events identifiable as pre-rule by
    their own filename shape — a durable property of the event — never as a fallback.
    """
    problems = gen_index.validate_event(
        {"time": "2026-08-26T20:56:01+05:00", "kind": "transition", "actor": "claude-code",
         "refs": ["status.md"]},
        "20260826-205601__transition.md", profiles=_human())
    assert not any("provider family" in p for p in problems), problems
    assert not any("not a declared" in p for p in problems), problems


def test_a_three_part_filename_never_reaches_the_legacy_escape():
    """The escape is scoped to the pre-2.0.0 two-part name, and to `on_behalf_of` alone.

    A three-part name is a post-2.0.0 event whatever its third component says, so it must
    still answer for accountability. `actor` is not what the escape is about any more.
    """
    problems = gen_index.validate_event(
        {"time": "2026-08-26T20:56:01+05:00", "kind": "transition", "actor": "claude-code",
         "on_behalf_of": "nobody", "refs": ["status.md"]},
        "20260826-205601__transition__claude-code.md", profiles=_human())
    assert any("on_behalf_of" in p and "not a declared" in p for p in problems), problems
    assert not any("actor" in p for p in problems), \
        "actor must attract no complaint of any kind"


def test_profiles_are_parsed_not_inferred_from_filenames(tmp_path):
    """AC-14 item 1. The declared type lives in the body; the filename cannot carry it."""
    root = _project(tmp_path)
    team = root / "team"
    team.mkdir()
    (team / "alice.md").write_text(
        "---" + chr(10) + "handle: alice" + chr(10) + "type: human" + chr(10) + "---" + chr(10),
        encoding="utf-8")
    (team / "botty.md").write_text(
        "---" + chr(10) + "handle: botty" + chr(10) + "type: agent" + chr(10) + "---" + chr(10),
        encoding="utf-8")
    (team / "README.md").write_text("# team" + chr(10), encoding="utf-8")
    profiles = gen_index.team_profiles(root)
    assert set(profiles) == {"alice", "botty"}
    assert profiles["alice"]["type"] == "human"
    assert profiles["botty"]["type"] == "agent"


# --- the PRODUCTION path, driven as the workflows drive it (AC-14 item 3) --

def _project_with_current_event(tmp_path, on_behalf_of="saubakirov"):
    """A project holding an event of the shape the workflows write TODAY: two fields, token."""
    root = _project(tmp_path, containers=("workspace",))
    task = _task(root, "workspace/2026/20260827-100000__probe")
    journal = task / "journal"
    journal.mkdir()
    (journal / "20260827-100100__handoff__9f2c.md").write_text(
        "---" + chr(10) + "time: 2026-08-27T10:01:00+05:00" + chr(10) + "kind: handoff"
        + chr(10) + f"on_behalf_of: {on_behalf_of}" + chr(10)
        + "via: claude" + chr(10) + "refs:" + chr(10) + "  - status.md" + chr(10) + "---"
        + chr(10), encoding="utf-8")
    return root


def test_the_shape_the_workflows_write_today_validates(tmp_path):
    """The production path, covered directly rather than by a historical fixture.

    `_project_with_event` below writes a PRE-2.0.0-dirty.3 event -- actor in the filename and
    the body -- and it stays that way on purpose, because tolerating that shape is the whole
    of AC-15 item 3. But it stopped being the production shape, and a fixture that tests
    history while claiming to test production is the defect this task keeps finding.
    """
    root = _project_with_current_event(tmp_path)
    _declare(root)
    assert gen_index.main(["--root", str(root), "--check", "tasks"]) == 0


def _project_with_event(tmp_path, actor="saubakirov", on_behalf_of="saubakirov"):
    """A project holding a PRE-2.0.0-dirty.3 event: `actor` in the filename and the body.

    Deliberately the historical shape. Every event in every real corpus looks like this, and
    the tests that use this fixture are therefore exercising the tolerance path on realistic
    data rather than on a synthetic case.
    """
    root = _project(tmp_path, containers=("workspace",))
    task = _task(root, "workspace/2026/20260827-100000__probe")
    journal = task / "journal"
    journal.mkdir()
    (journal / f"20260827-100100__handoff__{actor}.md").write_text(
        "---" + chr(10) + "time: 2026-08-27T10:01:00+05:00" + chr(10) + "kind: handoff"
        + chr(10) + f"actor: {actor}" + chr(10) + f"on_behalf_of: {on_behalf_of}" + chr(10)
        + "via: claude" + chr(10) + "refs:" + chr(10) + "  - status.md" + chr(10) + "---"
        + chr(10), encoding="utf-8")
    return root


def _declare(root, handle="saubakirov", kind="human"):
    team = root / "team"
    team.mkdir(exist_ok=True)
    (team / f"{handle}.md").write_text(
        "---" + chr(10) + f"handle: {handle}" + chr(10) + f"type: {kind}" + chr(10)
        + "---" + chr(10), encoding="utf-8")


def test_check_tasks_refuses_when_team_is_absent(tmp_path):
    """Driven through `gen_index.main(--check tasks)`, the command the build gate runs.

    The earlier tests passed because they called the validator directly with an injected
    non-empty set — the one path on which this defect cannot appear.
    """
    root = _project_with_event(tmp_path)
    assert not (root / "team").exists()
    assert gen_index.main(["--root", str(root), "--check", "tasks"]) == 1


def test_check_tasks_refuses_when_team_is_empty(tmp_path):
    root = _project_with_event(tmp_path)
    (root / "team").mkdir()
    assert gen_index.main(["--root", str(root), "--check", "tasks"]) == 1


def test_check_tasks_refuses_when_accountability_is_an_agent(tmp_path):
    root = _project_with_event(tmp_path)
    _declare(root, "saubakirov", "agent")
    assert gen_index.main(["--root", str(root), "--check", "tasks"]) == 1


def test_check_tasks_passes_when_a_human_is_declared(tmp_path):
    root = _project_with_event(tmp_path)
    _declare(root, "saubakirov", "human")
    assert gen_index.main(["--root", str(root), "--check", "tasks"]) == 0


def test_collect_reports_the_undeclared_actor_in_the_index(tmp_path):
    """The other production path: `collect`, which the index is built from."""
    root = _project_with_event(tmp_path)
    (root / "team").mkdir()
    content = gen_index.build(root)
    assert "team/ declares nobody" in content


def test_the_repository_itself_declares_a_human():
    """The shipped tree must satisfy the rule it ships."""
    profiles = gen_index.team_profiles(PROJECT_ROOT)
    assert profiles, "team/ declares nobody"
    humans = [h for h, p in profiles.items() if str(p.get("type")) == "human"]
    assert humans, f"no human participant declared: {profiles}"


def test_kind_must_come_from_the_closed_vocabulary():
    problems = gen_index.validate_event(
        _event(kind="deployed"), "20260826-140000__deployed__saubakirov.md")
    assert any("outside the closed vocabulary" in p for p in problems)


def test_consolidation_is_reserved_and_not_yet_valid():
    problems = gen_index.validate_event(
        _event(kind="consolidation"), "20260826-140000__consolidation__saubakirov.md")
    assert any("reserved for a later phase" in p for p in problems)


def test_a_summary_over_the_ceiling_is_refused():
    problems = gen_index.validate_event(
        _event(summary="x" * 121), "20260826-140000__transition__saubakirov.md", 120)
    assert any("ceiling is 120" in p for p in problems)


def test_half_a_state_change_is_refused():
    problems = gen_index.validate_event(
        _event(to=None), "20260826-140000__transition__saubakirov.md")
    assert any("both 'from' and 'to'" in p for p in problems)


def test_a_composed_timestamp_shape_is_rejected():
    """The time must be ISO 8601 with an offset — a shape a typed value rarely matches."""
    problems = gen_index.validate_event(
        _event(time="2026-08-26 14:00"), "20260826-140000__transition__saubakirov.md")
    assert any("not ISO 8601" in p for p in problems)


def test_legacy_events_are_reported_as_legacy_not_as_defects(tmp_path):
    """The journal is immutable, so a later rule describes old entries and never edits them."""
    root = _project(tmp_path)
    task = _task(root, "workspace/2026/20260826-120000__alpha")
    journal = task / "journal"
    journal.mkdir()
    (journal / "20260819-140312__created.md").write_text(
        "---\ntime: 2026-08-19T14:03:12+05:00\nkind: created\nactor: saubakirov\n"
        "refs:\n  - status.md\n---\n", encoding="utf-8")
    events, problems = gen_index.read_journal(task)
    assert len(events) == 1
    assert any("predate the 2.0.0 event grammar" in p for p in problems)
    assert not any("missing on_behalf_of" in p for p in problems)


def test_a_malformed_event_reaches_the_index(tmp_path):
    root = _project(tmp_path)
    task = _task(root, "workspace/2026/20260826-120000__alpha")
    journal = task / "journal"
    journal.mkdir()
    (journal / "20260826-140000__deployed__saubakirov.md").write_text(
        "---\ntime: 2026-08-26T14:00:00+05:00\nkind: deployed\nactor: saubakirov\n"
        "on_behalf_of: saubakirov\nrefs:\n  - status.md\n---\n", encoding="utf-8")
    content = gen_index.build(root)
    assert "outside the closed vocabulary" in content


# --- the index must never become a shared write ----------------------------

def test_a_task_transition_does_not_touch_anything_shared(tmp_path):
    """The finding that rejected revision 2, turned into a test.

    A previous pass asserted that the committed index always matches the generator. That one
    assertion undid the whole phase: advancing any task made the check fail until somebody
    rewrote `workspace/00-INDEX.md`, so every transition was pushed back into one shared
    aggregate — the exact bottleneck the task exists to remove (master HL 3.1, 3.2).

    A stale index is the correct state after a transition. It must be *visible*, never
    *forbidden*.
    """
    root = _project(tmp_path)
    task = _task(root, "workspace/2026/20260826-120000__alpha")
    other = _task(root, "workspace/2026/20260826-120001__beta")
    gen_index.main(["--root", str(root)])

    everything = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}

    # A normal transition: one task's own state file, and nothing else.
    (task / "status.md").write_text(
        _status(id="20260826-120000__alpha", lifecycle="RF", updated="20260827-090000"),
        encoding="utf-8")

    changed = [p.relative_to(root).as_posix() for p, before in everything.items()
               if p.read_bytes() != before]
    assert changed == ["workspace/2026/20260826-120000__alpha/status.md"], changed
    assert (other / "status.md").read_bytes() == everything[other / "status.md"]


def test_a_stale_index_is_visible_but_never_blocking(tmp_path):
    """Staleness is reported by a tool that is run deliberately, not enforced on everyone."""
    root = _project(tmp_path)
    task = _task(root, "workspace/2026/20260826-120000__alpha")
    gen_index.main(["--root", str(root)])
    assert gen_index.main(["--root", str(root), "--check", "index"]) == 0

    (task / "status.md").write_text(
        _status(id="20260826-120000__alpha", lifecycle="RF", updated="20260827-090000"),
        encoding="utf-8")

    # The index is now stale, and says so when asked.
    assert gen_index.main(["--root", str(root), "--check", "index"]) == 1
    # The task is still readable and still authoritative. Nothing is blocked.
    state = gen_index.read_status(task)
    assert state["lifecycle"] == "RF" and "_error" not in state
    # And rebuilding is a deliberate act, not a side effect of the transition.
    gen_index.main(["--root", str(root)])
    assert gen_index.main(["--root", str(root), "--check", "index"]) == 0


# --- the real repository ---------------------------------------------------

def test_the_repository_index_is_readable_and_declares_its_own_freshness():
    """What the shipped index owes the project: legibility and an honest freshness claim.

    Deliberately NOT "the index is current". Requiring that would reintroduce the shared
    write; see the two tests above.
    """
    index = gen_index.output_path(PROJECT_ROOT)
    assert index.exists(), "the project must never be without a portfolio view"
    content = index.read_text(encoding="utf-8")
    assert "derived and non-authoritative" in content
    assert "Freshness" in content


# --- F4: an unmatched legacy directory is reported, never described --------

def test_the_single_underscore_legacy_form_is_reported_not_matched(tmp_path):
    """The exact fixture AC-4's gate names, and the exact defect it comes from.

    A real corpus carried `TFW-01_awesome_list_restructure` beside `TFW-3__tfw_init`. The
    grammar requires `__`, so the single-underscore form did not parse — and the run then
    rendered both of its rows under a heading reading *"They are ideas, not work in
    progress"*, about directories holding completed HL, TS and RF traces.

    It is reported, never matched. Widening `LEGACY_ID` would edit an identifier rule.
    """
    root = _project(tmp_path, containers=("tasks",))
    _task(root, "tasks/TFW-3__double__underscore", id="TFW-3")
    (root / "tasks" / "TFW-01_single_underscore").mkdir()
    (root / "tasks" / "TFW-01_single_underscore" / "HL-TFW-01__x.md").write_text(
        "# HL\n", encoding="utf-8")

    # Not matched: the identifier rules are untouched.
    assert gen_index.parse_identifier("TFW-01_single_underscore") is None
    assert [p.name for p in gen_index.iter_task_dirs(root)] == ["TFW-3__double__underscore"]

    # Reported: it appears, and not as an idea.
    rendered = gen_index.build(root)
    assert "TFW-01_single_underscore" in rendered, "an unmatched directory must appear"
    assert "Unresolved inputs" in rendered
    backlog_section = rendered.partition("## Backlog")[2].partition(chr(10) + "## ")[0]
    assert "TFW-01_single_underscore" not in backlog_section, \
        "an unmatched directory must never be classified as a backlog idea"
    assert "TFW-3__double__underscore" in rendered


def test_the_unresolved_reason_asserts_only_what_is_observable(tmp_path):
    """No generated artifact prints a reason the source did not carry.

    The failing run asserted *"backlog idea, never started"*. The only fact available was
    the directory's name, so the name is what the reason talks about.
    """
    root = _project(tmp_path, containers=("tasks",))
    (root / "tasks" / "TFW-01_legacy").mkdir(parents=True)
    rendered = gen_index.build(root)
    row = next(line for line in rendered.splitlines() if "TFW-01_legacy" in line)
    assert "grammar" in row
    assert "reported as malformed" in row
    for forbidden in ("idea", "never started", "backlog"):
        assert forbidden not in row.lower(), f"the reason asserts {forbidden!r}"


def test_an_unrendered_snapshot_class_is_reported_rather_than_skipped(tmp_path):
    """A class nobody renders disappears, and disappearing is the failure being fixed."""
    root = _project(tmp_path, containers=("tasks",))
    (root / "tasks").mkdir(exist_ok=True)
    (root / "tasks" / "BOARD-SNAPSHOT.md").write_text(
        "## Rows" + chr(10) * 2 + "| ID | Task | Status | Class |" + chr(10)
        + "|---|---|---|---|" + chr(10)
        + "| `TFW-9` | Ninth | DONE | some-class-nobody-renders |" + chr(10),
        encoding="utf-8")
    rendered = gen_index.build(root)
    assert "some-class-nobody-renders" in rendered
    assert "TFW-9" in rendered


# --- F5: the validator names the key it rejected --------------------------

@pytest.mark.parametrize("key", ["title", "goal", "value", "authority", "outcome"])
def test_a_colon_space_value_is_reported_by_key(tmp_path, key):
    """AC-5's gate: five files whose values contain a colon followed by a space.

    A person hand-wrote five state files and got `unparseable front matter: ScannerError`
    five times, with no key named, and had to find the cause by inspection. The cause is
    always the same and always mechanical: a colon-space ends a YAML plain scalar.
    """
    root = _project(tmp_path, containers=("tasks",))
    task = root / "tasks" / "TFW-1__probe"
    task.mkdir(parents=True)
    fields = {
        "id": "TFW-1", "title": "Fixture", "goal": "why", "value": "what",
        "lifecycle": "TODO", "owner": "saubakirov", "authority": "HL.md",
        "created": "20260826-120000", "updated": "20260826-120000",
    }
    fields[key] = "Phase AA: portable delivery"
    body = chr(10).join(f"{k}: {v}" for k, v in fields.items())
    (task / "status.md").write_text("---" + chr(10) + body + chr(10) + "---" + chr(10) * 2
                                    + "**Task state.**" + chr(10), encoding="utf-8")

    error = gen_index.read_status(task)["_error"]
    assert f"key `{key}`" in error, f"the error must name the key, got: {error}"
    assert "quote it" in error, "and say what to do about it"
    assert "ScannerError" not in error


def test_a_parse_failure_with_no_mark_still_reports_something_usable():
    """The fallback path is exercised, not assumed.

    A validator test that only ever takes the path where the defect cannot appear is one of
    the four forms of "a check reported as passing that never ran".
    """
    import yaml as _yaml
    markless = _yaml.YAMLError("something went wrong with no mark")
    message = gen_index.explain_yaml_error("id: X" + chr(10), markless)
    assert "unparseable front matter" in message


def test_reader_error_reports_the_key_containing_the_invalid_character():
    block = "id: TFW-1\ntitle: bad\x82value\ngoal: x\n"
    with pytest.raises(yaml.YAMLError) as caught:
        yaml.safe_load(block)

    message = gen_index.explain_yaml_error(block, caught.value)

    assert "key `title`" in message
    assert "line 2" in message


# --- AC-1: the project root is found by marker, not by depth ---------------

def test_the_root_is_found_by_marker_from_any_depth(tmp_path):
    """`parents[2]` resolved correctly from `.tfw/scripts/` **by coincidence**.

    So a source-only move would have passed every test in this repository while leaving the
    defect fully intact. The observable test is the tools at a *different depth inside* a
    project — which is exactly what a project that places them elsewhere produces.
    """
    root = _project(tmp_path, containers=("tasks",))
    for depth in ("tools", "tools/tfw", "a/b/c/d"):
        here = root / depth
        here.mkdir(parents=True)
        assert gen_index.find_project_root(here) == root.resolve(), \
            f"the root must be found from {depth}, whatever its depth"
    # And from the payload's own location, which must not be special.
    payload = root / ".tfw" / "scripts"
    payload.mkdir(parents=True)
    assert gen_index.find_project_root(payload) == root.resolve()


def test_the_upstream_staging_clone_never_captures_the_root(tmp_path):
    """`update.md` Step 0 clones upstream into `.tfw/.upstream/`, which has a full `.tfw/`.

    Resolving to it would generate a project's index from the upstream clone instead of the
    project — silently, and with a plausible-looking result.
    """
    root = _project(tmp_path, containers=("tasks",))
    staging = root / ".tfw" / ".upstream" / ".tfw" / "scripts"
    staging.mkdir(parents=True)
    assert gen_index.find_project_root(staging) == root.resolve()


def test_no_root_refuses_rather_than_guessing(tmp_path):
    """Guessing a root means writing files into a directory nobody chose."""
    lonely = tmp_path / "not" / "a" / "project"
    lonely.mkdir(parents=True)
    with pytest.raises(SystemExit) as caught:
        gen_index.find_project_root(lonely)
    assert "--root" in str(caught.value), "the refusal must name the explicit override"


# --- AC-9: one flag, three subjects ---------------------------------------

def test_the_three_checks_are_one_flag_with_a_subject():
    """No `--validate`, no `--doctor`. When prose is needed to tell names apart, they fail."""
    assert set(gen_index.CHECKS) == {"index", "tasks", "project"}
    source = Path(gen_index.__file__).read_text(encoding="utf-8")
    for retired in ('"--validate"', '"--doctor"'):
        assert retired not in source, f"{retired} is a synonym, not a subject"


def test_check_project_reports_a_missing_team_directory(tmp_path):
    """The signal a real consumer never had: it learned `team/` was required from a
    framework test it was never told to run."""
    root = _project(tmp_path, containers=("tasks",))
    (root / ".tfw" / "VERSION").write_text("2.0.0" + chr(10), encoding="utf-8")
    (root / "tasks").mkdir(exist_ok=True)
    assert gen_index.main(["--root", str(root), "--check", "project"]) == 1


def test_check_project_reports_a_build_command_naming_a_missing_path(tmp_path):
    """`build.*` is a PROJECT section an update PRESERVES.

    So a project that updates across a release which moved a tool keeps a command naming a
    path that is gone — permanently, and silently. This check is the only thing that says so.
    """
    root = _project(tmp_path, containers=("tasks",))
    (root / ".tfw" / "VERSION").write_text("2.0.0" + chr(10), encoding="utf-8")
    (root / ".tfw" / "project_config.yaml").write_text(
        "tfw:" + chr(10) + "  task_containers: [tasks]" + chr(10)
        + "build:" + chr(10) + "  verify: python docs/scripts/gen_index.py --check tasks"
        + chr(10), encoding="utf-8")
    (root / "tasks").mkdir(exist_ok=True)
    _declare(root)
    assert gen_index.main(["--root", str(root), "--check", "project"]) == 1


def test_check_project_reports_a_retired_key(tmp_path):
    """`initial_seq` was retired at 2.0.0 and dropped by inference, not by instruction."""
    root = _project(tmp_path, containers=("tasks",))
    (root / ".tfw" / "VERSION").write_text("2.0.0" + chr(10), encoding="utf-8")
    (root / ".tfw" / "project_config.yaml").write_text(
        "tfw:" + chr(10) + "  task_containers: [tasks]" + chr(10) + "  initial_seq: 42"
        + chr(10), encoding="utf-8")
    (root / "tasks").mkdir(exist_ok=True)
    _declare(root)
    assert gen_index.main(["--root", str(root), "--check", "project"]) == 1


@pytest.mark.parametrize("retired_block", [
    "  id_max_retries: 5\n",
    "  review:\n    default_mode: code\n",
])
def test_check_project_names_each_additional_retired_key(tmp_path, capsys, retired_block):
    root = _project(tmp_path, containers=("tasks",))
    (root / ".tfw" / "VERSION").write_text("2.0.0\n", encoding="utf-8")
    (root / ".tfw" / "project_config.yaml").write_text(
        "tfw:\n  task_containers: [tasks]\n" + retired_block,
        encoding="utf-8",
    )
    (root / "tasks").mkdir(exist_ok=True)
    _declare(root)

    assert gen_index.main(["--root", str(root), "--check", "project"]) == 1
    assert "retired key" in capsys.readouterr().err


def test_check_project_passes_on_a_consistent_project(tmp_path, capsys):
    """And names what it did not check, so its silence is not read as an answer."""
    root = _project(tmp_path, containers=("tasks",))
    (root / ".tfw" / "VERSION").write_text("2.0.0" + chr(10), encoding="utf-8")
    (root / ".tfw" / "project_config.yaml").write_text(
        "tfw:" + chr(10) + '  version: "2.0.0"' + chr(10) + "  task_containers: [tasks]"
        + chr(10), encoding="utf-8")
    (root / "tasks").mkdir(exist_ok=True)
    _declare(root)
    assert gen_index.main(["--root", str(root), "--check", "project"]) == 0
    out = capsys.readouterr().out
    assert "not checked" in out
    assert "index freshness" in out


def test_check_tasks_says_it_does_not_answer_index_freshness(tmp_path, capsys):
    """The fact the deleted five-line comment used to carry, said where it is read."""
    root = _project_with_event(tmp_path)
    _declare(root)
    assert gen_index.main(["--root", str(root), "--check", "tasks"]) == 0
    assert "index freshness" in capsys.readouterr().out


def test_no_check_subject_writes_anything(tmp_path):
    """Every subject reports and exits. The moment one writes it becomes an authority."""
    root = _project_with_event(tmp_path)
    _declare(root)
    before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
    for subject in ("tasks", "project", "index"):
        gen_index.main(["--root", str(root), "--check", subject])
    after = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
    assert before == after, "a check wrote to the tree"


# --- AC-15 item 8: a phase carries its own journal ------------------------

def _event_file(directory: pathlib.Path, name: str, **overrides) -> pathlib.Path:
    directory.mkdir(parents=True, exist_ok=True)
    # The kind comes from the filename, so a fixture cannot desync the two by accident --
    # which is exactly what it did on the first attempt at this test.
    fields = {"time": "2026-08-27T10:01:00+05:00", "kind": name.split("__")[1],
              "on_behalf_of": "saubakirov", "via": "claude"}
    fields.update(overrides)
    body = "".join(f"{k}: {v}" + chr(10) for k, v in fields.items())
    body += "refs:" + chr(10) + "  - status.md" + chr(10)
    path = directory / name
    path.write_text("---" + chr(10) + body + "---" + chr(10), encoding="utf-8")
    return path


def test_a_phase_journal_is_read(tmp_path):
    """The symmetry a consumer assumed, correctly, before it was implemented.

    A phase carries its own `status.md`, so a consumer created `phase-a/journal/` too. The
    reader globbed the task's own journal once and non-recursively, so **two of that
    project's four malformed events sat there and the gate reported clean over them.**
    """
    root = _project(tmp_path, containers=("tasks",))
    task = _task(root, "tasks/TFW-1__probe", id="TFW-1")
    _event_file(task / "journal", "20260827-100100__handoff__aa11.md")
    _event_file(task / "phase-a" / "journal", "20260827-100200__transition__bb22.md")

    dirs = [d.parent.name for d in gen_index.journal_dirs(task)]
    assert dirs == ["TFW-1__probe", "phase-a"], dirs
    events, problems = gen_index.read_journal(task, profiles=_human())
    assert len(events) == 2, events
    assert problems == [], problems


def test_a_malformed_phase_event_is_reported_and_named_by_its_path(tmp_path):
    """The exact failure: invisible before, and a bare filename would not locate it."""
    root = _project(tmp_path, containers=("tasks",))
    task = _task(root, "tasks/TFW-1__probe", id="TFW-1")
    _event_file(task / "phase-a" / "journal", "20260827-100200__transition__bb22.md",
                on_behalf_of="ghost")

    _, problems = gen_index.read_journal(task, profiles=_human())
    assert problems, "a malformed phase event must be reported"
    assert any("phase-a/journal/" in p for p in problems), problems
    assert gen_index.main(["--root", str(root), "--check", "tasks"]) == 1


def test_two_phases_may_hold_the_same_event_name(tmp_path):
    """Which is why a report names the path and not the bare filename."""
    root = _project(tmp_path, containers=("tasks",))
    task = _task(root, "tasks/TFW-1__probe", id="TFW-1")
    for phase in ("phase-a", "phase-b"):
        _event_file(task / phase / "journal", "20260827-100200__transition__bb22.md",
                    on_behalf_of="ghost")
    _, problems = gen_index.read_journal(task, profiles=_human())
    located = {p.split(":")[0] for p in problems}
    assert located == {"phase-a/journal/20260827-100200__transition__bb22.md",
                       "phase-b/journal/20260827-100200__transition__bb22.md"}, located


# --- a phase directory without state is named (TFW-60 Phase AC, AC-8) -----------------

def _stateless_phase(task: Path, letter: str) -> Path:
    phase = task / f"phase-{letter}"
    phase.mkdir()
    (phase / f"TS__phase-{letter}__x.md").write_text("# TS" + chr(10), encoding="utf-8")
    return phase


def test_a_live_task_with_a_stateless_phase_directory_fails_the_gate(tmp_path, capsys):
    """The fifth report: four `phase-*` directories stood without `status.md` and the gate
    answered "4 tasks validate". It validates what exists; now it also names what is missing."""
    root = _project(tmp_path, containers=("workspace",))
    _declare(root)
    task = _task(root, "workspace/2026/20260827-100000__multi", lifecycle="PHASES")
    _phase(task, "a", lifecycle="DONE", outcome="shipped")
    _stateless_phase(task, "b")
    assert gen_index.main(["--root", str(root), "--check", "tasks"]) == 1
    err = capsys.readouterr().err
    assert "phase-b" in err and "phase-a" not in err
    assert "status.md" in err


def test_a_terminal_task_with_stateless_phases_is_informational(tmp_path, capsys):
    """A phase closed before phase state existed is history, not a defect."""
    root = _project(tmp_path, containers=("workspace",))
    _declare(root)
    task = _task(root, "workspace/2026/20260827-100000__old", lifecycle="DONE", outcome="shipped")
    _stateless_phase(task, "a")
    _stateless_phase(task, "b")
    assert gen_index.main(["--root", str(root), "--check", "tasks"]) == 0
    captured = capsys.readouterr()
    assert "phase-a" in captured.out and "phase-b" in captured.out
    assert "phase-a" not in captured.err
    assert "phase state is not written by migration" in captured.out


def test_a_task_without_its_own_state_but_with_stateless_phases_is_informational(tmp_path, capsys):
    """A terminal legacy task migrated without state, by design: the gate cannot know it is
    live, and says that instead of guessing."""
    root = _project(tmp_path, containers=("tasks",))
    _declare(root)
    task = root / "tasks" / "TFW-7__legacy"
    task.mkdir(parents=True)
    (task / "HL-TFW-7__x.md").write_text("# HL" + chr(10), encoding="utf-8")
    _stateless_phase(task, "a")
    assert gen_index.main(["--root", str(root), "--check", "tasks"]) == 0
    captured = capsys.readouterr()
    assert "TFW-7__legacy" in captured.out and "phase-a" in captured.out
    assert "phase-a" not in captured.err, "informational, never a failure"


def test_a_malformed_task_state_makes_its_stateless_phases_informational(tmp_path, capsys):
    """The malformed state is already the failure; the phase line says why it is not a second."""
    root = _project(tmp_path, containers=("workspace",))
    _declare(root)
    task = _task(root, "workspace/2026/20260827-100000__broken", lifecycle="SHIPPED")
    _stateless_phase(task, "a")
    assert gen_index.main(["--root", str(root), "--check", "tasks"]) == 1
    captured = capsys.readouterr()
    assert "not declared" in captured.err
    assert "phase-a" not in captured.err
    assert "phase-a" in captured.out and "malformed" in captured.out


def test_informational_lines_are_grouped_one_per_task(tmp_path, capsys):
    root = _project(tmp_path, containers=("workspace",))
    _declare(root)
    task = _task(root, "workspace/2026/20260827-100000__old", lifecycle="DONE", outcome="shipped")
    for letter in "abc":
        _stateless_phase(task, letter)
    assert gen_index.main(["--root", str(root), "--check", "tasks"]) == 0
    lines = [l for l in capsys.readouterr().out.splitlines() if "phase-" in l]
    assert len(lines) == 1, lines
    assert all(f"phase-{letter}" in lines[0] for letter in "abc")


def test_the_gate_writes_nothing_when_it_names_a_stateless_phase(tmp_path):
    root = _project(tmp_path, containers=("workspace",))
    _declare(root)
    task = _task(root, "workspace/2026/20260827-100000__multi", lifecycle="PHASES")
    _stateless_phase(task, "b")
    before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
    gen_index.main(["--root", str(root), "--check", "tasks"])
    after = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
    assert before == after


def test_the_repository_stateless_phases_are_all_informational(capsys):
    """Measured at onboarding: 17 directories under six tasks, every one terminal by the board
    snapshot and without task-level state. One line per task, exit code unchanged."""
    assert gen_index.main(["--root", str(PROJECT_ROOT), "--check", "tasks"]) == 0
    out = capsys.readouterr().out
    lines = [l for l in out.splitlines() if "carry no status.md" in l]
    named = {l.split("/")[1].split(":")[0] for l in lines}
    assert named == {"TFW-42__research_cycle_restructure", "TFW-46__evidence_layer",
                     "TFW-47__codex_adapter_shortcut_skills", "TFW-52__tfw_light_v1",
                     "TFW-53__hl_contract_and_goal_defence", "TFW-55__canonization_program"}, named


# --- installed_from has one form (TFW-60 Phase AC, AC-5) -------------------------------

def _consistent_project(tmp_path: Path, installed_from: str) -> Path:
    root = _project(tmp_path, containers=("tasks",))
    (root / ".tfw" / "VERSION").write_text("2.0.0" + chr(10), encoding="utf-8")
    (root / ".tfw" / "project_config.yaml").write_text(
        "tfw:" + chr(10) + '  version: "2.0.0"' + chr(10) + "  task_containers: [tasks]"
        + chr(10) + f"  installed_from: '{installed_from}'" + chr(10), encoding="utf-8")
    (root / "tasks").mkdir(exist_ok=True)
    _declare(root)
    return root


@pytest.mark.parametrize("value", [
    "D:/projects/research/steps-framework@v2.0.0-dirty.4",
    "C:" + chr(92) + "work" + chr(92) + "steps-framework@v2.0.0-dirty.4",
    "/home/me/steps-framework@v2.0.0-dirty.4",
])
def test_check_project_reports_a_machine_local_installed_from(tmp_path, capsys, value):
    """Three of three local consumers wrote a drive path into a committed file. Reported, and
    the file is not rewritten: the operator records the upstream reference."""
    root = _consistent_project(tmp_path, value)
    before = (root / ".tfw" / "project_config.yaml").read_bytes()
    assert gen_index.main(["--root", str(root), "--check", "project"]) == 1
    err = capsys.readouterr().err
    assert "installed_from" in err and "machine-local" in err
    assert (root / ".tfw" / "project_config.yaml").read_bytes() == before


@pytest.mark.parametrize("value", [
    "steps-framework@v2.0.0-dirty.4",
    "https://github.com/saubakirov/trace-first-starter@v2.0.0",
    "self",
    "unrecorded",
])
def test_check_project_accepts_the_declared_installed_from_forms(tmp_path, value):
    root = _consistent_project(tmp_path, value)
    assert gen_index.main(["--root", str(root), "--check", "project"]) == 0
