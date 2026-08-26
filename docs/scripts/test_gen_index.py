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
    ids = ["20260826-090000__c", "TFW-60", "20250101-000000__a"]
    ordered = sorted(ids, key=lambda i: gen_index.sort_key(*gen_index.parse_identifier(i)))
    assert ordered == ["TFW-60", "20250101-000000__a", "20260826-090000__c"]


def test_same_second_tasks_order_by_slug_not_by_filesystem():
    ids = ["20260826-090000__zeta", "20260826-090000__alpha"]
    ordered = sorted(ids, key=lambda i: gen_index.sort_key(*gen_index.parse_identifier(i)))
    assert ordered == ["20260826-090000__alpha", "20260826-090000__zeta"]


# --- fixtures --------------------------------------------------------------

def _status(**overrides) -> str:
    fields = {
        "id": "20260826-120000__fixture", "title": "Fixture task", "goal": "why it exists",
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
    _task(root, "alpha/2026/20260826-120000__one")
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


@pytest.mark.parametrize("value", ["26-08-2026", "2026/08/26", "August 2026", "20260826"])
def test_dates_must_be_iso_or_unrecorded(tmp_path, value):
    root = _project(tmp_path)
    task = _task(root, "tasks/TFW-1__x", created=value)
    assert "not YYYY-MM-DD" in gen_index.read_status(task)["_error"]


def test_unrecorded_is_an_accepted_date(tmp_path):
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


# --- journal events (review F3) --------------------------------------------

def test_same_second_same_kind_two_actors_produce_two_files():
    """F3, the exact case that silently lost an event.

    Revision 2 named events `<time>__<kind>.md` and proved concurrency with two *different*
    kinds — which cannot collide by construction. Two writers recording the same kind in the
    same second produced one filename and one surviving event.
    """
    taken = set()
    first = gen_index.event_filename("20260826-140000", "handoff", "saubakirov", taken)
    taken.add(first)
    second = gen_index.event_filename("20260826-140000", "handoff", "codex", taken)
    assert first != second
    assert first == "20260826-140000__handoff__saubakirov.md"
    assert second == "20260826-140000__handoff__codex.md"


def test_one_actor_writing_twice_in_a_second_takes_the_next_second():
    """Not a counter: a counter is shared state, which is what this model removes."""
    taken = {"20260826-140000__handoff__saubakirov.md"}
    name = gen_index.event_filename("20260826-140000", "handoff", "saubakirov", taken)
    assert name == "20260826-140001__handoff__saubakirov.md"
    taken.add(name)
    third = gen_index.event_filename("20260826-140000", "handoff", "saubakirov", taken)
    assert third == "20260826-140002__handoff__saubakirov.md"


def test_event_naming_never_overwrites_and_never_reuses():
    taken = set()
    names = []
    for _ in range(5):
        name = gen_index.event_filename("20260826-235958", "transition", "saubakirov", taken)
        taken.add(name)
        names.append(name)
    assert len(set(names)) == 5, names
    assert "20260826-000000__transition__saubakirov.md" in names, "wraps past midnight"


def _event(**overrides) -> dict:
    data = {
        "time": "2026-08-26T14:00:00+05:00", "kind": "transition",
        "actor": "saubakirov", "on_behalf_of": "saubakirov", "via": "claude",
        "from": "ONB", "to": "RF", "refs": ["status.md"], "summary": "moved to execution",
    }
    data.update(overrides)
    return {k: v for k, v in data.items() if v is not None}


def test_an_event_without_on_behalf_of_is_refused():
    """There is no such thing as a record nobody answers for."""
    problems = gen_index.validate_event(
        _event(on_behalf_of=None), "20260826-140000__transition__saubakirov.md")
    assert "missing on_behalf_of" in problems


def test_a_provider_name_is_not_an_actor():
    """`via: claude` does not identify a writer; two Claude sessions are two actors."""
    data = _event(actor="claude", via="claude")
    problems = gen_index.validate_event(data, "20260826-140000__transition__saubakirov.md")
    assert any("filename says actor" in p for p in problems)


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
        _status(id="20260826-120000__alpha", lifecycle="RF", updated="2026-08-27"),
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
    assert gen_index.main(["--root", str(root), "--check"]) == 0

    (task / "status.md").write_text(
        _status(id="20260826-120000__alpha", lifecycle="RF", updated="2026-08-27"),
        encoding="utf-8")

    # The index is now stale, and says so when asked.
    assert gen_index.main(["--root", str(root), "--check"]) == 1
    # The task is still readable and still authoritative. Nothing is blocked.
    state = gen_index.read_status(task)
    assert state["lifecycle"] == "RF" and "_error" not in state
    # And rebuilding is a deliberate act, not a side effect of the transition.
    gen_index.main(["--root", str(root)])
    assert gen_index.main(["--root", str(root), "--check"]) == 0


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
