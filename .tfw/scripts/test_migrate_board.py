"""Tests for the board migration.

The migration's promises are negative ones — nothing renamed, nothing byte-changed, nothing
invented, nothing dropped — and negative promises need tests more than positive ones do,
because a bug in them looks exactly like success.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import migrate_board  # noqa: E402

# Found by marker. See the note in test_gen_index.py.
PROJECT_ROOT = migrate_board.find_project_root(Path(__file__))

DECLARED = migrate_board.FALLBACK_STATUSES

BOARD = """# Project

## Task Board

| ID | Task | Status | Notes |
|----|------|--------|-------|
| [TFW-1](tasks/TFW-1__alpha/) | First task | ✅ DONE | shipped |
| [TFW-2](tasks/TFW-2__beta/) | Second task | 🟢 RF | in progress |
| TFW-3 | Backlog idea | ⬜ TODO | never started |
| ~~[TFW-4](tasks/TFW-4__delta/)~~ — absorbed into TFW-2 | Folded in | — | |
| ~~TFW-5~~ — absorbed into TFW-1 | Also folded | — | |
| [TFW-6](tasks/TFW-6__zeta/) | Frozen task | ❄️ FROZEN | odd status |

## Something Else

Not part of the board.
"""


# Committed regression shape from the third external update. `HD-30b` is a malformed
# sub-item label beside the real `HD-30` task; it must never be shortened into that task.
HELPDESK_SHAPE = """# Helpdesk

## Task Board

| ID | Task | Status |
|---|---|---|
| [HD-30](tasks/HD-30__tickets/) | Closed ticket workflow | ✅ DONE |
| [HD-30b](tasks/HD-30__tickets/hd30b/) | `normalize_text()` keeps working_days | ✅ DONE |
| [TFW-01_single_underscore](tasks/TFW-01_single_underscore/) | Old malformed path | 🟢 RF |
| [20260829-010832__dirty](workspace/2026/20260829-010832__dirty/) | Dirty-era task | 🟢 RF |
| [TFW_20260829-010832_ABT](workspace/2026/TFW_20260829-010832_ABT/) | Current task | 🟢 RF |
"""


def _commit(root: Path, message: str = "board") -> None:
    """Commit the fixture, so the board has a committed revision to be read from."""
    if not (root / ".git").exists():
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "add", "-A"], cwd=root, check=True)
    subprocess.run(["git", "-c", "user.email=t@e", "-c", "user.name=T",
                    "commit", "-qm", message], cwd=root, check=True)


def _project(tmp_path: Path, commit: bool = True) -> Path:
    """A fixture project, **committed by default.**

    The commit is not scenery. Since the migration reads a *committed revision* by default,
    a fixture that is not a repository would force every test onto `--working-tree` — and
    then the default path, the one every real project takes, would be exercised by nothing.
    That is the shape of a check reported as passing that never ran.

    Pass ``commit=False`` to test what happens when there is no committed board.
    """
    (tmp_path / ".tfw").mkdir()
    (tmp_path / ".tfw" / "project_config.yaml").write_text(
        "tfw:\n  task_containers: [workspace, tasks]\n"
        "  statuses:\n" + "".join(f"    - id: {s}\n" for s in DECLARED),
        encoding="utf-8")
    (tmp_path / "README.md").write_text(BOARD, encoding="utf-8")
    for name in ("TFW-1__alpha", "TFW-2__beta", "TFW-4__delta", "TFW-6__zeta"):
        directory = tmp_path / "tasks" / name
        directory.mkdir(parents=True)
        (directory / f"HL-{name.split('__')[0]}__x.md").write_text("# HL\n", encoding="utf-8")
    if commit:
        _commit(tmp_path)
    return tmp_path


# --- parsing ---------------------------------------------------------------

def test_every_row_is_seen_whatever_its_shape():
    rows = migrate_board.parse_board(BOARD)
    assert [row["id"] for row in rows] == ["TFW-1", "TFW-2", "TFW-3", "TFW-4", "TFW-5", "TFW-6"]


def test_parsing_stops_at_the_end_of_the_table():
    assert "Something Else" not in "".join(r["raw"] for r in migrate_board.parse_board(BOARD))


def test_row_shape_is_recorded_not_used_to_filter():
    rows = {row["id"]: row for row in migrate_board.parse_board(BOARD)}
    assert rows["TFW-1"]["linked"] and not rows["TFW-1"]["struck"]
    assert not rows["TFW-3"]["linked"]
    assert rows["TFW-4"]["struck"] and rows["TFW-5"]["struck"]


def test_absent_board_yields_no_rows():
    assert migrate_board.parse_board("# Project\n\nNo board here.\n") == []


def test_helpdesk_shape_is_parsed_whole_or_reported_never_shortened():
    rows = migrate_board.parse_board(HELPDESK_SHAPE)
    assert [(row["id_kind"], row["id"]) for row in rows] == [
        ("legacy", "HD-30"),
        ("malformed", None),
        ("malformed", None),
        ("clock", "20260829-010832__dirty"),
        ("current", "TFW_20260829-010832_ABT"),
    ]
    assert rows[1]["id_text"] == "HD-30b"
    assert all(row["id"] != "HD-30" for row in rows[1:])


# --- status classification -------------------------------------------------

@pytest.mark.parametrize("cell,lifecycle", [
    ("✅ DONE", "DONE"),
    ("🟢 RF", "RF"),
    ("⬜ TODO", "TODO"),
    ("📝 HL_DRAFT", "HL_DRAFT"),
    ("🟢 RF (A) — execution in progress", "RF"),
])
def test_declared_values_map_to_their_id(cell, lifecycle):
    assert migrate_board.classify_status(cell, DECLARED)["lifecycle"] == lifecycle


@pytest.mark.parametrize("cell", ["❄️ FROZEN", "🟡 TS", "🚀 SHIPPED"])
def test_undeclared_values_are_carried_verbatim_never_normalized(cell):
    result = migrate_board.classify_status(cell, DECLARED)
    assert result["lifecycle"] == "UNDECLARED"
    assert result["verbatim"] == cell


def test_empty_status_is_undeclared_not_todo():
    """Guessing TODO for a blank cell would be inventing a fact."""
    assert migrate_board.classify_status("—", DECLARED)["lifecycle"] == "UNDECLARED"


def test_terminal_trailing_prose_becomes_the_outcome():
    result = migrate_board.classify_status("✅ DONE — shipped in v1.2", DECLARED)
    assert result["lifecycle"] == "DONE"
    assert result["outcome"] == "shipped in v1.2"


def test_markdown_is_removed_without_deleting_identifier_underscores():
    assert migrate_board._plain("`normalize_text()` and working_days") == (
        "normalize_text() and working_days")
    assert migrate_board._plain("_emphasis_ and **bold**") == "emphasis and bold"


# --- reconciliation --------------------------------------------------------

def test_every_row_and_directory_is_accounted_for_exactly_once(tmp_path):
    root = _project(tmp_path)
    rows = migrate_board.parse_board((root / "README.md").read_text(encoding="utf-8"))
    result = migrate_board.reconcile(root, rows)
    assert len(result["matched"]) + len(result["board_only"]) == len(rows)
    assert len(result["matched"]) + len(result["directory_only"]) == len(result["directories"])
    assert len(result["matched"]) == 4
    assert [row["id"] for row in result["board_only"]] == ["TFW-3", "TFW-5"]
    assert result["directory_only"] == []


def test_a_struck_row_over_a_real_directory_is_reported_as_malformed(tmp_path):
    root = _project(tmp_path)
    rows = migrate_board.parse_board((root / "README.md").read_text(encoding="utf-8"))
    result = migrate_board.reconcile(root, rows)
    malformed = {row["id"] for row in result["malformed"]}
    assert malformed == {"TFW-3", "TFW-4", "TFW-5"}
    assert "TFW-4" in {row["id"] for row in result["matched"]}


def test_a_directory_with_no_row_is_reported(tmp_path):
    root = _project(tmp_path)
    (root / "tasks" / "TFW-9__orphan").mkdir(parents=True)
    rows = migrate_board.parse_board((root / "README.md").read_text(encoding="utf-8"))
    result = migrate_board.reconcile(root, rows)
    assert [entry["id"] for entry in result["directory_only"]] == ["TFW-9"]


def test_two_rows_resolving_to_one_identifier_refuse_before_manifest_write(tmp_path, capsys):
    root = _project(tmp_path)
    duplicate = BOARD.replace(
        "| [TFW-2](tasks/TFW-2__beta/) | Second task | 🟢 RF | in progress |",
        "| [TFW-1__another](tasks/TFW-2__beta/) | Duplicate | 🟢 RF | in progress |",
    )
    (root / "README.md").write_text(duplicate, encoding="utf-8")
    _commit(root, "duplicate board")
    manifest = root / "MIGRATION.md"

    assert migrate_board.main(["--root", str(root), "--manifest", str(manifest)]) == 1
    assert not manifest.exists()
    message = capsys.readouterr().err
    assert "TFW-1" in message
    assert "line 7" in message and "line 8" in message
    assert "Nothing was changed" in message


def test_helpdesk_malformed_subitem_never_produces_state(tmp_path):
    (tmp_path / ".tfw").mkdir()
    (tmp_path / ".tfw" / "project_config.yaml").write_text(
        "tfw:\n  task_containers: [tasks]\n  statuses:\n    - id: TODO\n    - id: DONE\n",
        encoding="utf-8")
    (tmp_path / "README.md").write_text(HELPDESK_SHAPE, encoding="utf-8")
    task = tmp_path / "tasks" / "HD-30__tickets"
    task.mkdir(parents=True)
    (task / "HL-HD-30__tickets.md").write_text("# HL\n", encoding="utf-8")
    (tmp_path / "tasks" / "HD-30b__subitem").mkdir()
    _commit(tmp_path, "helpdesk shape")

    result, writes, _ = migrate_board.plan(tmp_path, "20260829-010832", HELPDESK_SHAPE)
    assert [row["id_text"] for row in result["malformed_identifiers"]] == [
        "HD-30b", "TFW-01_single_underscore",
    ]
    assert all("HD-30b" not in content for _, content in writes)
    manifest = migrate_board.render_manifest(tmp_path, result, ["TODO", "DONE"], writes)
    assert "`HD-30b`" in manifest
    assert "`tasks/HD-30b__subitem`" in manifest
    assert "none — malformed" in manifest


# --- task state ------------------------------------------------------------

def test_state_is_written_only_for_live_tasks_with_a_directory(tmp_path):
    root = _project(tmp_path)
    _, writes, _ = migrate_board.plan(root, "2026-08-26")
    written = [path.parent.name for path, _ in writes]
    assert written == ["TFW-2__beta", "TFW-6__zeta"]


def test_terminal_and_absorbed_tasks_receive_no_state(tmp_path):
    """TFW-1 is done; TFW-4 was absorbed. Neither is a task anyone can advance."""
    root = _project(tmp_path)
    _, writes, _ = migrate_board.plan(root, "2026-08-26")
    names = {path.parent.name for path, _ in writes}
    assert "TFW-1__alpha" not in names and "TFW-4__delta" not in names


def test_facts_the_board_never_carried_are_marked_absent_not_guessed(tmp_path):
    root = _project(tmp_path)
    _, writes, _ = migrate_board.plan(root, "2026-08-26")
    content = dict((p.parent.name, c) for p, c in writes)["TFW-2__beta"]
    assert "value: unrecorded" in content
    assert "owner: unassigned" in content


def test_undeclared_status_reaches_task_state_verbatim(tmp_path):
    root = _project(tmp_path)
    _, writes, _ = migrate_board.plan(root, "2026-08-26")
    content = dict((p.parent.name, c) for p, c in writes)["TFW-6__zeta"]
    assert "lifecycle: UNDECLARED" in content
    assert "lifecycle_verbatim: ❄️ FROZEN" in content


def test_authority_points_at_a_file_that_exists(tmp_path):
    root = _project(tmp_path)
    _, writes, _ = migrate_board.plan(root, "2026-08-26")
    for path, content in writes:
        authority = next(line.split(": ", 1)[1] for line in content.splitlines()
                         if line.startswith("authority: "))
        assert (path.parent / authority).exists(), authority


def test_written_state_parses_back_cleanly(tmp_path):
    """What migration writes must be what the index can read."""
    import gen_index
    root = _project(tmp_path)
    assert migrate_board.main(["--root", str(root), "--apply"]) == 0
    for task_dir in gen_index.iter_task_dirs(root):
        data = gen_index.read_status(task_dir)
        if data is not None:
            assert "_error" not in data, (task_dir.name, data.get("_error"))


# --- the negative guarantees ----------------------------------------------

def test_dry_run_writes_nothing(tmp_path):
    root = _project(tmp_path)
    before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
    assert migrate_board.main(["--root", str(root)]) == 0
    after = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
    assert before == after


def test_apply_leaves_every_pre_existing_file_byte_identical(tmp_path):
    root = _project(tmp_path)
    before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
    assert migrate_board.main(["--root", str(root), "--apply"]) == 0
    for path, content in before.items():
        assert path.exists(), f"{path} disappeared"
        assert path.read_bytes() == content, f"{path} changed"


def test_apply_adds_only_state_files_and_the_snapshot(tmp_path):
    root = _project(tmp_path)
    before = {p for p in root.rglob("*") if p.is_file()}
    migrate_board.main(["--root", str(root), "--apply"])
    added = sorted(p.relative_to(root).as_posix() for p in root.rglob("*")
                   if p.is_file() and p not in before)
    assert added == [
        "tasks/BOARD-SNAPSHOT.md",
        "tasks/TFW-2__beta/status.md",
        "tasks/TFW-6__zeta/status.md",
    ]


def test_apply_refuses_to_overwrite(tmp_path):
    """Re-running must not clobber state a person has since edited."""
    root = _project(tmp_path)
    assert migrate_board.main(["--root", str(root), "--apply"]) == 0
    edited = root / "tasks" / "TFW-2__beta" / "status.md"
    edited.write_text("---\nid: TFW-2\n---\nedited by hand\n", encoding="utf-8")
    assert migrate_board.main(["--root", str(root), "--apply"]) == 1
    assert "edited by hand" in edited.read_text(encoding="utf-8")


def test_snapshot_captures_every_row_verbatim(tmp_path):
    root = _project(tmp_path)
    migrate_board.main(["--root", str(root), "--apply"])
    snapshot = (root / "tasks" / "BOARD-SNAPSHOT.md").read_text(encoding="utf-8")
    for row in migrate_board.parse_board(BOARD):
        assert row["raw"] in snapshot, row["id"]
    assert "Rows captured | 6" in snapshot


def test_snapshot_keeps_backlog_rows_that_have_no_directory(tmp_path):
    """A snapshot of only finished work would delete the project's backlog."""
    root = _project(tmp_path)
    migrate_board.main(["--root", str(root), "--apply"])
    snapshot = (root / "tasks" / "BOARD-SNAPSHOT.md").read_text(encoding="utf-8")
    assert "board-only, backlog" in snapshot
    assert "board-only, absorbed elsewhere" in snapshot


def test_the_snapshot_is_readable_by_the_index_generator(tmp_path):
    import gen_index
    root = _project(tmp_path)
    migrate_board.main(["--root", str(root), "--apply"])
    assert len(gen_index.read_snapshot(root)) == 6


# --- the board source is explicit (review F9) ------------------------------

def test_an_empty_board_source_is_refused(tmp_path):
    """The defect that deleted the trace, turned into a test.

    Re-running the migration after the board had been removed read a README with no table,
    produced a snapshot reading `Rows captured | 0`, and overwrote the real one. Every row
    the board carried was lost, and the failure was silent: the run reported success.
    """
    root = _project(tmp_path)
    (root / "README.md").write_text("# Project\n\nNo board here.\n", encoding="utf-8")
    _commit(root, "board removed")
    assert migrate_board.main(["--root", str(root), "--apply"]) == 1
    assert not (root / "tasks" / "BOARD-SNAPSHOT.md").exists()


def test_an_empty_board_is_allowed_only_when_said_so_explicitly(tmp_path):
    """A project that genuinely never had a board is a real case — but it must be declared."""
    root = _project(tmp_path)
    (root / "README.md").write_text("# Project\n\nNo board here.\n", encoding="utf-8")
    _commit(root, "board removed")
    assert migrate_board.main(
        ["--root", str(root), "--apply", "--allow-empty-board"]) == 0


# --- the source is a committed revision (F8) -------------------------------

def test_the_committed_revision_is_the_default_source(tmp_path):
    """A live file that changes under the reader is not an input a migration can trust.

    During one real run the board was rewritten three times while being read. The default
    is therefore `HEAD`, and the working tree is the opt-in — the reverse of what shipped.
    """
    root = _project(tmp_path)
    (root / "README.md").write_text("# Project\n\nBoard removed.\n", encoding="utf-8")

    committed, origin = migrate_board.read_board(root)
    assert len(migrate_board.parse_board(committed)) == 6, \
        "the default source must be the committed revision, not the working tree"
    assert "HEAD" in origin

    live, live_origin = migrate_board.read_board(root, working_tree=True)
    assert migrate_board.parse_board(live) == []
    assert "working tree" in live_origin


def test_a_working_tree_change_during_a_run_does_not_affect_the_result(tmp_path):
    """AC-8's gate: change the file underneath the run and the accounting is unmoved."""
    root = _project(tmp_path)
    before, _ = migrate_board.read_board(root)
    (root / "README.md").write_text("# Project\n\n## Task Board\n\n| ID |\n|----|\n",
                                    encoding="utf-8")
    after, _ = migrate_board.read_board(root)
    assert before == after
    assert len(migrate_board.parse_board(after)) == 6


def test_no_committed_board_refuses_and_names_the_opt_in(tmp_path):
    """No silent fallback. A printed notice is the thing nobody reads."""
    root = _project(tmp_path, commit=False)
    with pytest.raises(SystemExit) as caught:
        migrate_board.read_board(root)
    message = str(caught.value)
    assert "--working-tree" in message, "the refusal must name the opt-in"
    assert "HEAD:README.md" in message, "the refusal must print the revision it tried"


def test_a_named_revision_still_works(tmp_path):
    """`--board-rev` keeps its job: reading a board removed several commits ago."""
    root = _project(tmp_path)
    first = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True,
                           text=True, check=True).stdout.strip()
    (root / "README.md").write_text("# Project\n\nBoard removed.\n", encoding="utf-8")
    _commit(root, "board removed")
    assert migrate_board.parse_board(migrate_board.read_board(root)[0]) == []
    historical, origin = migrate_board.read_board(root, revision=first)
    assert len(migrate_board.parse_board(historical)) == 6
    assert first in origin


# --- the board's location is an input, not a constant (F3) -----------------

def test_a_board_kept_outside_the_root_readme_is_found(tmp_path):
    """The finding that made this necessary, as a fixture.

    A real external project kept its board at `tasks/README.md` under `## Board`, because
    its root README is fully regenerated and a board there is destroyed. Run with the
    location hardcoded, the parser returned zero rows.
    """
    root = _project(tmp_path)
    (root / "README.md").write_text("# Generated. Do not edit.\n", encoding="utf-8")
    (root / "tasks" / "README.md").write_text(
        BOARD.replace("## Task Board", "## Board"), encoding="utf-8")
    _commit(root, "board relocated")

    text, origin = migrate_board.read_board(root, board="tasks/README.md")
    rows = migrate_board.parse_board(text, "## Board")
    assert len(rows) == 6, "a relocated board must be found when its location is given"
    assert "tasks/README.md" in origin


def test_the_row_parser_is_untouched_by_a_wider_table(tmp_path):
    """Only the locator was ever wrong. A nine-column table already parsed unmodified."""
    wide = BOARD.replace(
        "| ID | Task | Status | Notes |",
        "| ID | Task | Status | HL | TS | ONB | RF | REV | RES |")
    rows = migrate_board.parse_board(wide)
    assert [row["id"] for row in rows] == ["TFW-1", "TFW-2", "TFW-3", "TFW-4", "TFW-5", "TFW-6"]


def test_a_zero_row_result_names_relocation_before_removal(tmp_path):
    """The refusal used to offer only `--board-rev`, sending the reader to the wrong cause."""
    root = _project(tmp_path)
    (root / "README.md").write_text("# Project\n\nNo board here.\n", encoding="utf-8")
    _commit(root, "no board")
    result = subprocess.run(
        [sys.executable, str(Path(migrate_board.__file__)), "--root", str(root), "--apply"],
        capture_output=True, text=True, encoding="utf-8")
    assert result.returncode == 1
    message = result.stderr
    assert "--board " in message, "relocation must be offered"
    assert "--board-heading" in message, "a differing heading must be offered"
    assert message.index("--board ") < message.index("--board-rev"), \
        "relocation is the cause that actually occurs; it comes first"


# --- counting, never asserting (review E27) --------------------------------

def test_the_snapshot_row_count_equals_the_board_row_count(tmp_path):
    """A claim was accepted where a count was required. Now the count is the test."""
    root = _project(tmp_path)
    source_rows = len(migrate_board.parse_board(BOARD))
    migrate_board.main(["--root", str(root), "--apply"])
    snapshot = (root / "tasks" / "BOARD-SNAPSHOT.md").read_text(encoding="utf-8")
    assert f"Rows captured | {source_rows} |" in snapshot
    assert len(migrate_board.parse_board(BOARD)) == source_rows == 6
    # and the identifiers are physically present, not merely counted
    for row in migrate_board.parse_board(BOARD):
        assert row["id"] in snapshot, row["id"]


def test_every_board_identifier_is_named_in_the_accounting(tmp_path):
    """R3: the reconciliation lists all rows by name, and nothing is unaccounted."""
    root = _project(tmp_path)
    rows = migrate_board.parse_board(BOARD)
    result = migrate_board.reconcile(root, rows)
    _, writes, _ = migrate_board.plan(root, "2026-08-26", BOARD)
    manifest = migrate_board.render_manifest(root, result, DECLARED, writes)
    for row in rows:
        assert f"`{row['id']}`" in manifest, row["id"]


def test_manifest_computes_and_prints_each_runtime_guarantee(tmp_path):
    root = _project(tmp_path)
    result, writes, _ = migrate_board.plan(root, "20260826-120000", BOARD)
    manifest = migrate_board.render_manifest(root, result, DECLARED, writes)
    assert "## Guarantees checked" in manifest
    assert "matched 4 + directory-only 0 = parsed directories 4" in manifest
    assert manifest.count("**HELD**") == 3
    assert "## Guarantees not checked by this run" in manifest


def test_deliberately_unbalanced_result_names_failed_guarantee_and_identifier(tmp_path):
    root = _project(tmp_path)
    (root / "tasks" / "TFW-9__orphan").mkdir()
    rows = migrate_board.parse_board(BOARD)
    result = migrate_board.reconcile(root, rows)
    assert result["directory_only"][0]["id"] == "TFW-9"
    result["directory_only"].clear()

    with pytest.raises(migrate_board.MigrationRefusal) as caught:
        migrate_board.render_manifest(root, result, DECLARED, [])

    message = str(caught.value)
    assert "Every parsed task directory accounted exactly once" in message
    assert "TFW-9" in message


def test_a_snapshot_that_lost_its_rows_is_detectable_by_counting(tmp_path):
    """The check that would have caught the revision-2 failure at the time."""
    root = _project(tmp_path)
    migrate_board.main(["--root", str(root), "--apply"])
    snapshot_path = root / "tasks" / "BOARD-SNAPSHOT.md"
    good = snapshot_path.read_text(encoding="utf-8")
    assert good.count("TFW-") > 0

    snapshot_path.write_text(good.replace("| Rows captured | 6 |",
                                          "| Rows captured | 0 |"), encoding="utf-8")
    reported = int(re.search(r"Rows captured \| (\d+) \|",
                             snapshot_path.read_text(encoding="utf-8")).group(1))
    assert reported != len(migrate_board.parse_board(BOARD)), \
        "a count mismatch must be visible without reading the prose"


# --- the real repository ---------------------------------------------------

def test_repository_accounting_balances():
    """Re-runnable against the live tree: every row and directory lands exactly once."""
    rows = migrate_board.parse_board((PROJECT_ROOT / "README.md").read_text(encoding="utf-8"))
    if not rows:
        pytest.skip("board already removed — accounting is frozen in BOARD-SNAPSHOT.md")
    result = migrate_board.reconcile(PROJECT_ROOT, rows)
    assert len(result["matched"]) + len(result["board_only"]) == len(rows)
    assert len(result["matched"]) + len(result["directory_only"]) == len(result["directories"])


def test_a_manifest_containing_the_project_own_characters_prints(tmp_path):
    """Content is not ASCII, and must survive a console whose codepage nobody chose.

    Runtime *messages* are ASCII by rule. A manifest quotes a board **verbatim**, and a real
    board carries the emoji its project wrote — so `print(manifest)` on a cp1252 console
    raised `UnicodeEncodeError` and the first command the migration guide gives died. Found
    by running the guide against a real external corpus, not by inspection.
    """
    root = _project(tmp_path)
    board = (root / "README.md").read_text(encoding="utf-8")
    assert "✅" in board, "the fixture board must carry a non-ASCII status"
    result = subprocess.run(
        [sys.executable, str(Path(migrate_board.__file__)), "--root", str(root)],
        capture_output=True, encoding="utf-8", errors="replace",
        env={**os.environ, "PYTHONIOENCODING": "cp1252"},
    )
    assert result.returncode == 0, (
        "printing a manifest must not depend on the console encoding:\n" + result.stderr)
    assert "UnicodeEncodeError" not in result.stderr
    assert "Reconciliation" in result.stdout


def test_the_written_snapshot_keeps_the_board_bytes_exactly(tmp_path):
    """Console rendering may degrade; the artifact never does.

    The verbatim block lives in the snapshot — it is the record the board's removal is
    justified by, and the manifest's tables are checkable *against* it.
    """
    root = _project(tmp_path)
    assert migrate_board.main(["--root", str(root), "--apply"]) == 0
    written = (root / "tasks" / "BOARD-SNAPSHOT.md").read_text(encoding="utf-8")
    for row in migrate_board.parse_board(BOARD):
        assert row["raw"] in written, "the verbatim block lost a row's exact bytes"
    assert "✅" in written and "❄" in written, \
        "the board's own characters must survive into the file"


# --- the status cell is parsed whole or refused (TFW-60 Phase AC, AC-8) ----------------

#: The exact row shape from the fifth external update, `kaznpu-ai-lab`. The board author wrote
#: closed phases first and the live one after; the first-token reader classified the project's
#: main task terminal and wrote nothing. Two signals follow the first token — a second status
#: symbol (`🔄`) and a second declared token (`RF`) — and either alone must refuse the cell.
AILAB_2_CELL = ("✅ DONE (A/V/B/C) · 🔄 Phase D (досборка/консистентность) — стоящий цикл правок; "
                "R1 ✅ APPROVE; R2 🟢 RF; R3 закрыт по подтверждению владельца")

KAZNPU_SHAPE = f"""# kaznpu-ai-lab

## Task Board

| ID | Task | Status | Updated |
|---|---|---|---|
| [AILAB-1](tasks/AILAB-1__init/) | Init | ✅ DONE | 2026-06-01 |
| [AILAB-2](tasks/AILAB-2__regulatory_and_org_form/) | Regulatory and org form | {AILAB_2_CELL} | 2026-08-20 |
"""


def _kaznpu(tmp_path: Path) -> Path:
    (tmp_path / ".tfw").mkdir()
    (tmp_path / ".tfw" / "project_config.yaml").write_text(
        "tfw:\n  task_containers: [workspace, tasks]\n"
        "  statuses:\n" + "".join(f"    - id: {s}\n" for s in DECLARED), encoding="utf-8")
    (tmp_path / "README.md").write_text(KAZNPU_SHAPE, encoding="utf-8")
    for name in ("AILAB-1__init", "AILAB-2__regulatory_and_org_form"):
        directory = tmp_path / "tasks" / name
        directory.mkdir(parents=True)
        (directory / f"HL-{name.split('__')[0]}__x.md").write_text("# HL\n", encoding="utf-8")
    for letter in "vbcd":
        (tmp_path / "tasks" / "AILAB-2__regulatory_and_org_form" / f"phase-{letter}").mkdir()
    _commit(tmp_path)
    return tmp_path


def test_the_ailab_2_shape_is_refused_not_read_by_its_first_token():
    """The row that closed a live task. Refused whole, carried verbatim, never terminal."""
    result = migrate_board.classify_status(AILAB_2_CELL, DECLARED)
    assert result["lifecycle"] == "UNDECLARED"
    assert result["verbatim"] == AILAB_2_CELL
    assert result["outcome"] == ""
    assert result["signals"], "the refusal names what it saw"


@pytest.mark.parametrize("cell,why", [
    ("✅ DONE (Phase A ✅)", "a second status symbol alone"),
    ("📚 KNW (Phase B ✅ / Phase C 🟢 RF)", "symbols and a token"),
    ("✅ DONE (KNW deferred to post-HD-20)", "a second declared token alone, no emoji"),
    ("❌ REJECTED — not restored (last live status was 🟡 TS (D))", "a quoted earlier status"),
])
def test_a_second_lifecycle_signal_refuses_the_cell(cell, why):
    result = migrate_board.classify_status(cell, DECLARED)
    assert result["lifecycle"] == "UNDECLARED", why
    assert result["verbatim"] == cell


@pytest.mark.parametrize("cell,lifecycle,outcome", [
    ("✅ DONE (owner-confirmed closure; hooks runtime blocked → TD-126)", "DONE",
     "(owner-confirmed closure; hooks runtime blocked → TD-126)"),
    ("✅ DONE (deployed prod v1.9.0; 6/6 smoke green; +1 UX TD-271)", "DONE",
     "(deployed prod v1.9.0; 6/6 smoke green; +1 UX TD-271)"),
    ("🟠 ONB (A+B)", "ONB", "(A+B)"),
    ("✅ DONE — cost = 3 days, <1 % regressions", "DONE", "cost = 3 days, <1 % regressions"),
])
def test_math_and_prose_punctuation_are_not_status_signals(cell, lifecycle, outcome):
    """`+`, `→`, `=` and `<` are category Sm — prose on every board measured. Only `So`,
    where every emoji marker lives, is a status symbol (TS AC-8 R2)."""
    result = migrate_board.classify_status(cell, DECLARED)
    assert result["lifecycle"] == lifecycle
    assert result["outcome"] == outcome


def test_a_bare_variation_selector_after_the_token_is_neither_symbol_nor_text():
    cell = "✅ DONE️ — shipped"
    result = migrate_board.classify_status(cell, DECLARED)
    assert result["lifecycle"] == "DONE"
    assert result["outcome"] == "shipped"
    joined = "✅️ DONE ‍— shipped"
    assert migrate_board.classify_status(joined, DECLARED)["lifecycle"] == "DONE"


def test_a_refused_row_receives_state_and_is_never_skipped_as_terminal(tmp_path):
    root = _kaznpu(tmp_path)
    _, writes, _ = migrate_board.plan(root, "20260830-120000")
    written = {path.parent.name: content for path, content in writes}
    assert "AILAB-2__regulatory_and_org_form" in written, "the live task was skipped again"
    assert "AILAB-1__init" not in written, "a single terminal token still closes a row"
    content = written["AILAB-2__regulatory_and_org_form"]
    assert "lifecycle: UNDECLARED" in content
    assert "lifecycle_verbatim:" in content
    assert "outcome:" not in content


def test_the_manifest_lists_multi_signal_rows_under_their_own_heading(tmp_path):
    root = _kaznpu(tmp_path)
    result, writes, _ = migrate_board.plan(root, "20260830-120000")
    manifest = migrate_board.render_manifest(root, result, DECLARED, writes)
    heading = manifest.partition("## Rows carrying more than one lifecycle signal")[2]
    assert heading, "the heading is missing"
    section = heading.partition("\n## ")[0]
    assert "AILAB-2" in section and "AILAB-1" not in section
    assert "🔄" in section or "RF" in section, "the row names the signals it carries"
    # the state-written note no longer implies that every unlisted row was terminal
    assert "Only for non-terminal tasks" not in manifest


def test_the_manifest_names_every_phase_directory_and_says_who_writes_its_state(tmp_path):
    root = _kaznpu(tmp_path)
    result, writes, _ = migrate_board.plan(root, "20260830-120000")
    manifest = migrate_board.render_manifest(root, result, DECLARED, writes)
    section = manifest.partition("## Phase directories")[2].partition("\n## ")[0]
    for letter in "vbcd":
        assert f"phase-{letter}" in section, f"phase-{letter} is not named"
    assert "phase state is not written by migration" in section
    assert "status.md` by hand" in section


def test_a_project_without_phase_directories_says_so(tmp_path):
    root = _project(tmp_path)
    result, writes, _ = migrate_board.plan(root, "20260830-120000")
    manifest = migrate_board.render_manifest(root, result, DECLARED, writes)
    section = manifest.partition("## Phase directories")[2].partition("\n## ")[0]
    assert "None" in section
