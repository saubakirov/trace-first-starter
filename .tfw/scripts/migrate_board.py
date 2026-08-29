"""Account for the root Task Board exactly, then retire it.

The board was the project's live task registry and its portfolio view at the same time.
Removing it means proving first that nothing it carried is lost. This script does the
counting, because exact accounting over a hundred-odd rows and directories is a counting
problem rather than a judgement one.

What it guarantees:

* **Every row and every directory is accounted for exactly once.** Rows with no directory,
  directories with no well-formed row, and rows in a shape no parser matches are all
  classified and reported. Nothing is silently dropped and nothing is silently merged.
* **Nothing existing is renamed, moved or byte-changed.** No legacy artifact is ever opened
  in write mode — not even to rewrite it unchanged, because a checkout with ``autocrlf``
  set would rewrite its line endings on the way out.
* **No fact is invented.** A task state file is written only from what the board and the
  directory actually say. A value the source never carried is recorded as ``unrecorded``,
  not guessed. A lifecycle outside the declared vocabulary is carried verbatim and flagged,
  not normalized into a declared one.

Usage:
    python .tfw/scripts/migrate_board.py                    # dry run, prints accounting
    python .tfw/scripts/migrate_board.py --manifest OUT.md  # dry run, writes accounting
    python .tfw/scripts/migrate_board.py --apply            # writes snapshot + status files

    --board PATH / --board-heading HEADING  where this project keeps its board
    --board-rev REV                         which committed revision to read (default HEAD)
    --working-tree                          read the live file instead, deliberately

**Where this file lives is not load-bearing.** The project root is found by walking upward
for a ``.tfw/`` directory, so a project may place these tools anywhere.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gen_index import (  # noqa: E402
    IdentifierCollisionError,
    find_project_root,
    iter_task_dirs,
    iter_unmatched_task_dirs,
    make_streams_printable,
    parse_identifier,
    read_config,
    sort_key,
    task_containers,
)

#: Where a board sits, and the heading its table follows, **by default only**. Both are
#: inputs — see :func:`read_board`. The first external project to run this legitimately had
#: `tasks/README.md` and `## Board`, and the constants made that project unmigratable.
#:
#: These stay flags rather than configuration keys: relocating the board is a fact about one
#: run of a once-per-project act, and a key read forever to answer a question asked once is
#: surface with no reader.
DEFAULT_BOARD = "README.md"
BOARD_HEADING = "## Task Board"

#: The revision the board is read from when nothing is named. A committed revision is the
#: stable input; the working tree is the explicit opt-in.
DEFAULT_REVISION = "HEAD"

#: Statuses the project actually declares, from project_config.yaml `tfw.statuses`.
FALLBACK_STATUSES = [
    "TODO", "HL_DRAFT", "RES", "PHASES", "TS_DRAFT", "ONB", "RF", "REV", "KNW",
    "DONE", "BLOCKED", "REJECTED",
]
TERMINAL = {"DONE", "REJECTED"}


class MigrationRefusal(ValueError):
    """An accounting condition failed before the migration may write anything."""

#: Preference order when deciding which artifact a task's state should point at.
AUTHORITY_ORDER = ("HL-", "HL__", "PROPOSAL__", "TS__", "RF__")


# ---------------------------------------------------------------------------
# Board parsing
# ---------------------------------------------------------------------------

def declared_statuses(root: Path) -> list[str]:
    entries = read_config(root).get("statuses") or []
    ids = [str(entry.get("id")) for entry in entries if isinstance(entry, dict) and entry.get("id")]
    return ids or list(FALLBACK_STATUSES)


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _identifier_text(cell: str) -> str:
    """Return the whole identifier candidate without Markdown presentation."""
    link = re.search(r"\[([^\]]+)\]\([^)]*\)", cell)
    candidate = (link.group(1) if link else cell).strip()
    for wrapper in ("~~", "**", "*", "`"):
        while (len(candidate) >= len(wrapper) * 2
               and candidate.startswith(wrapper) and candidate.endswith(wrapper)):
            candidate = candidate[len(wrapper):-len(wrapper)].strip()
    candidate = re.split(r"~~\s+(?:—|–|-)\s+", candidate, maxsplit=1)[0].strip("~ ")
    return candidate


def parse_board(text: str, heading: str = BOARD_HEADING) -> list[dict]:
    """Every data row of the board table, in document order, with nothing filtered out.

    A row is a row. Whether its identifier is a link, plain text or struck through decides
    its class later — it never decides whether the row is seen.

    The whole link label or plain-text value is dispatched through the shared identifier
    parser. A value no named grammar accepts remains visible as malformed; no prefix is
    extracted from it.
    """
    lines = text.splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == heading)
    except StopIteration:
        return []
    rows: list[dict] = []
    seen_header = False
    for index in range(start + 1, len(lines)):
        line = lines[index]
        if not line.startswith("|"):
            if rows and line.strip() == "":
                continue
            if rows:
                break
            continue
        cells = split_row(line)
        if not seen_header:
            seen_header = True
            continue
        if set(cells[0]) <= set("-: "):
            continue
        identifier_text = _identifier_text(cells[0])
        parsed = parse_identifier(identifier_text)
        rows.append({
            "line": index + 1,
            "raw": line,
            "cells": cells,
            "id": parsed[1] if parsed else None,
            "id_text": identifier_text,
            "id_kind": parsed[0] if parsed else "malformed",
            "id_cell": cells[0],
            "linked": cells[0].startswith("[") or "](" in cells[0],
            "struck": "~~" in cells[0],
            "title": cells[1] if len(cells) > 1 else "",
            "status_cell": cells[2] if len(cells) > 2 else "",
        })
    return rows


def classify_status(cell: str, declared: list[str]) -> dict:
    """Map a board status cell onto the declared vocabulary, or report that it is outside.

    The token is matched against declared ids only. ``🟡 TS`` is not ``TS_DRAFT``: it is the
    pre-rename label of that state and therefore outside the vocabulary as it stands today.
    Calling it ``TS_DRAFT`` would be normalizing a value the source never used.
    """
    verbatim = cell.strip()
    if not verbatim or verbatim == "—":
        return {"lifecycle": "UNDECLARED", "verbatim": verbatim or "(empty)", "outcome": ""}
    body = "".join(
        ch for ch in verbatim
        if not unicodedata.category(ch).startswith("S") and ch != "️"
    ).strip()
    token = re.match(r"[A-Z_]+", body)
    token = token.group(0) if token else ""
    trailing = body[len(token):].strip().lstrip("—-–").strip()
    if token in declared:
        return {"lifecycle": token, "verbatim": "", "outcome": trailing}
    return {"lifecycle": "UNDECLARED", "verbatim": verbatim, "outcome": ""}


# ---------------------------------------------------------------------------
# Reconciliation
# ---------------------------------------------------------------------------

def reconcile(root: Path, rows: list[dict]) -> dict:
    """Match rows against directories. Every entry lands in exactly one class.

    A row whose directory exists but whose *directory name* the identifier grammar does not
    parse is its own class — ``unresolved`` — and never ``board-only, backlog``. The
    distinction is the whole point: a real corpus had two such directories holding completed
    HL, TS and RF traces, and calling them backlog ideas made a generated artifact assert
    something untrue about real work. Silently dropping would be bad; confidently
    misdescribing is worse, because it reads as a finding.
    """
    duplicate_rows: list[str] = []
    rows_by_identifier: dict[str, list[dict]] = {}
    for row in rows:
        if row["id"]:
            rows_by_identifier.setdefault(row["id"], []).append(row)
    for identifier, occurrences in sorted(rows_by_identifier.items()):
        if len(occurrences) > 1:
            named = "; ".join(
                f"line {row['line']}: {row['id_cell']}" for row in occurrences
            )
            duplicate_rows.append(f"{identifier} <- {named}")
    if duplicate_rows:
        raise MigrationRefusal(
            "two or more board rows resolve to one identifier: "
            + " | ".join(duplicate_rows)
        )

    directories = {}
    for path in iter_task_dirs(root):
        parsed = parse_identifier(path.name)
        directories[parsed[1]] = path

    # Directories the grammar rejects. They are never matched into it — widening the
    # identifier rules is not on the table — so they are carried as what they are.
    unresolved_dirs = iter_unmatched_task_dirs(root)

    matched, board_only, unresolved = [], [], []
    malformed_identifiers, malformed_rows = [], []
    claimed: set[str] = set()
    claimed_dirs: set[Path] = set()
    for row in rows:
        identifier = row["id"]
        if not identifier:
            near = _unresolved_dir_for(row["id_text"], unresolved_dirs)
            if near is not None:
                row["unresolved_path"] = near
                claimed_dirs.add(near)
            malformed_identifiers.append(row)
        elif identifier in directories:
            row["path"] = directories[identifier]
            claimed.add(identifier)
            matched.append(row)
        else:
            near = _unresolved_dir_for(identifier, unresolved_dirs)
            if near is not None:
                row["unresolved_path"] = near
                claimed_dirs.add(near)
                unresolved.append(row)
            else:
                board_only.append(row)
        if not row["linked"] or row["struck"]:
            malformed_rows.append(row)

    directory_only = [
        {"id": identifier, "path": path}
        for identifier, path in sorted(directories.items(), key=lambda kv: sort_key(*parse_identifier(kv[0])))
        if identifier not in claimed
    ]
    # An unparseable directory no row names is also unresolved input, reported by path.
    orphan_dirs = [path for path in unresolved_dirs if path not in claimed_dirs]
    return {
        "rows": rows,
        "directories": directories,
        "matched": matched,
        "board_only": board_only,
        "unresolved": unresolved,
        "unresolved_dirs": unresolved_dirs,
        "claimed_unresolved_dirs": sorted(claimed_dirs, key=str),
        "orphan_dirs": orphan_dirs,
        "directory_only": directory_only,
        "malformed_identifiers": malformed_identifiers,
        # Presentation is orthogonal to identifier validity. The historical key remains
        # the snapshot's "not a strict linked row" classification.
        "malformed": malformed_rows,
    }


def computed_guarantees(result: dict) -> list[dict]:
    """Every runtime accounting guarantee, with its arithmetic and failure detail."""
    rows = result["rows"]
    row_classes = [
        *result["matched"], *result["board_only"], *result["unresolved"],
        *result["malformed_identifiers"],
    ]
    row_lines = [row["line"] for row in row_classes]
    expected_lines = [row["line"] for row in rows]
    missing_rows = sorted(set(expected_lines) - set(row_lines))
    duplicate_rows = sorted(line for line in set(row_lines) if row_lines.count(line) > 1)

    parsed_ids = list(result["directories"])
    accounted_ids = [row["id"] for row in result["matched"]]
    accounted_ids += [entry["id"] for entry in result["directory_only"]]
    missing_ids = sorted(set(parsed_ids) - set(accounted_ids))
    duplicate_ids = sorted(identifier for identifier in set(accounted_ids)
                           if accounted_ids.count(identifier) > 1)

    unresolved_paths = list(result["unresolved_dirs"])
    accounted_unresolved = list(result["claimed_unresolved_dirs"]) + list(result["orphan_dirs"])
    missing_paths = sorted(set(unresolved_paths) - set(accounted_unresolved), key=str)
    duplicate_paths = sorted((path for path in set(accounted_unresolved)
                              if accounted_unresolved.count(path) > 1), key=str)

    return [
        {
            "name": "Every board row classified exactly once",
            "arithmetic": (
                f"matched {len(result['matched'])} + board-only {len(result['board_only'])} + "
                f"unresolved {len(result['unresolved'])} + malformed "
                f"{len(result['malformed_identifiers'])} = rows {len(rows)}"
            ),
            "held": (len(row_lines) == len(expected_lines)
                     and not missing_rows and not duplicate_rows),
            "detail": f"missing lines {missing_rows}; duplicate lines {duplicate_rows}",
        },
        {
            "name": "Every parsed task directory accounted exactly once",
            "arithmetic": (
                f"matched {len(result['matched'])} + directory-only "
                f"{len(result['directory_only'])} = parsed directories {len(parsed_ids)}"
            ),
            "held": (len(accounted_ids) == len(parsed_ids)
                     and not missing_ids and not duplicate_ids),
            "detail": f"missing identifiers {missing_ids}; duplicate identifiers {duplicate_ids}",
        },
        {
            "name": "Every malformed directory accounted exactly once",
            "arithmetic": (
                f"row-named {len(result['claimed_unresolved_dirs'])} + orphan "
                f"{len(result['orphan_dirs'])} = malformed directories {len(unresolved_paths)}"
            ),
            "held": (len(accounted_unresolved) == len(unresolved_paths)
                     and not missing_paths and not duplicate_paths),
            "detail": (
                "missing paths " + str([path.as_posix() for path in missing_paths])
                + "; duplicate paths " + str([path.as_posix() for path in duplicate_paths])
            ),
        },
    ]


def require_guarantees(result: dict) -> list[dict]:
    """Refuse an unbalanced reconciliation before a manifest or state file is opened."""
    guarantees = computed_guarantees(result)
    failures = [item for item in guarantees if not item["held"]]
    if failures:
        raise MigrationRefusal("; ".join(
            f"guarantee failed: {item['name']} ({item['arithmetic']}; {item['detail']})"
            for item in failures
        ))
    return guarantees


def _unresolved_dir_for(identifier: str, candidates: list[Path]) -> Path | None:
    """The unparseable directory a board identifier names, on the observable prefix only.

    Deliberately weak: it establishes only *a row names this directory*, never a
    reconstructed identifier. Longest match wins so ``TFW-1`` never claims ``TFW-10_…``.
    """
    if not identifier:
        return None
    best: Path | None = None
    for path in candidates:
        if path.name == identifier or path.name.startswith(identifier + "_"):
            if best is None or len(path.name) > len(best.name):
                best = path
    return best


# ---------------------------------------------------------------------------
# Task state synthesis
# ---------------------------------------------------------------------------

def first_commit_date(root: Path, path: Path) -> str:
    """Creation time as Git recorded it, at second resolution, or ``unrecorded``.

    Git knows the exact second a path first appeared, so nothing is invented here. Where a
    source carries only a day, callers use :data:`gen_index.ZERO_TIME` — a *declared* zero,
    meaning "this day, time unknown", never a measurement.
    """
    try:
        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%ad",
             "--date=format:%Y%m%d-%H%M%S", "--", path.relative_to(root).as_posix()],
            cwd=root, capture_output=True, text=True, encoding="utf-8", check=False,
        )
    except OSError:
        return "unrecorded"
    dates = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return dates[-1] if dates else "unrecorded"


def tracked_files(root: Path, task_dir: Path) -> set[str] | None:
    """Paths under ``task_dir`` that Git actually carries, relative to it.

    Returns ``None`` when Git cannot answer — no repository, or no Git at all — so callers
    can fall back rather than treat "unknown" as "untracked".
    """
    try:
        result = subprocess.run(
            ["git", "ls-files", "--", task_dir.relative_to(root).as_posix()],
            cwd=root, capture_output=True, text=True, encoding="utf-8", check=False,
        )
    except OSError:
        return None
    if result.returncode != 0:
        return None
    prefix = task_dir.relative_to(root).as_posix() + "/"
    return {line[len(prefix):] for line in result.stdout.splitlines()
            if line.startswith(prefix)}


def find_authority(task_dir: Path, tracked: set[str] | None = None) -> str:
    """The governing artifact: the highest-preference file that a clean clone will have.

    Preference alone is not enough. A working tree can hold an uncommitted draft that
    outranks the committed artifact, and choosing it produces a state file whose authority
    link is broken for everyone who clones — which is exactly what happened to TFW-54 in the
    rejected pass, where `authority` named an HL that existed only on one machine.

    So: rank by preference, but only among files Git carries. If Git cannot answer, fall
    back to the filesystem rather than treating silence as absence.
    """
    def candidates(directory: Path, relative: str = "") -> list[str]:
        return sorted(f"{relative}{p.name}" for p in directory.iterdir()
                      if p.is_file() and p.suffix == ".md")

    pools = [candidates(task_dir)]
    for child in sorted((p for p in task_dir.iterdir() if p.is_dir()), key=lambda p: p.name):
        pools.append(candidates(child, f"{child.name}/"))

    for require_tracked in (True, False):
        if require_tracked and tracked is None:
            continue
        for pool in pools:
            for prefix in AUTHORITY_ORDER:
                for name in pool:
                    if not name.split("/")[-1].startswith(prefix):
                        continue
                    if require_tracked and name not in tracked:
                        continue
                    return name
    return "unrecorded"


def _bound(text: str, limit: int) -> str:
    """Shorten to the bound at a word boundary, and say so.

    A bounded field is lossy by design. The ellipsis marks it as shortened rather than
    finished, so nobody reads a cut sentence as the whole fact; the full text stays in the
    board snapshot and in the task's own artifacts.
    """
    text = " ".join(str(text).split())
    if len(text) <= limit:
        return text
    cut = text[:limit - 1].rsplit(" ", 1)[0].rstrip(" ,;:+&-—–")
    return (cut or text[:limit - 1]) + "…"


def _short_name(description: str) -> str:
    """The leading clause of a board description, as its name.

    Board descriptions are one line carrying a name, then a colon or dash, then the detail.
    The part before that break is the name; everything after it is the goal.
    """
    for separator in (": ", " — ", " – ", ". ", " ("):
        head = description.split(separator, 1)[0]
        if head != description and 3 <= len(head) <= 80:
            return head.rstrip(" .,:;")
    return _bound(description, 80)


def _scalar(value: str) -> str:
    """Emit a YAML scalar that survives a round trip.

    Board descriptions carry colons, hashes and quotes. Written bare they produce a file
    that looks right and parses wrong — and a state file the index cannot read is a task
    that vanishes from the portfolio.
    """
    text = str(value)
    unsafe = ':#\'"\n'   # colon, hash, quote, apostrophe, newline
    if text and not any(ch in text for ch in unsafe) and text.strip() == text:
        return text
    escaped = text.replace(chr(92), chr(92) * 2).replace(chr(34), chr(92) + chr(34))
    return chr(34) + escaped + chr(34)


def _plain(text: str) -> str:
    """Strip Markdown links and emphasis so a bounded field stays a readable sentence."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    # Underscores are emphasis only at word boundaries. Between word characters they are
    # identifier bytes (`normalize_text`, `working_days`, and the current task grammar).
    text = re.sub(r"(?<!\w)_+(?=\w)", "", text)
    text = re.sub(r"(?<=\w)_+(?!\w)", "", text)
    text = re.sub(r"[*`~]+", "", text)
    return " ".join(text.split())


def build_status(root: Path, row: dict, declared: list[str], now: str) -> str:
    """Task state from verified facts only. Absent facts are recorded as absent."""
    task_dir: Path = row["path"]
    status = classify_status(row["status_cell"], declared)
    description = _plain(row["title"])

    fields = [
        ("id", row["id"]),
        ("title", _short_name(description)),
        ("goal", _bound(description, 160)),
        ("value", "unrecorded"),
        ("lifecycle", status["lifecycle"]),
    ]
    if status["lifecycle"] == "UNDECLARED":
        fields.append(("lifecycle_verbatim", _bound(status["verbatim"], 80)))
    fields.append(("owner", "unassigned"))
    fields.append(("authority", find_authority(task_dir, tracked_files(root, task_dir))))
    if status["lifecycle"] in TERMINAL and status["outcome"]:
        fields.append(("outcome", _bound(_plain(status["outcome"]), 160)))
    fields.append(("created", first_commit_date(root, task_dir)))
    fields.append(("updated", now))

    lines = ["---"]
    lines += [f"{key}: {_scalar(value)}" for key, value in fields]
    lines.append("---")
    lines.append("")
    lines.append("**Task state.** This file is the only authority for this task's live "
                 "state. The portfolio index is derived from it and never outranks it.")
    lines.append("")
    lines.append("<!-- Written by .tfw/scripts/migrate_board.py from the root Task Board "
                 "at TFW 2.0.0. `unrecorded` means the board carried no such fact; it was "
                 "not guessed. Fill it in when the fact is known. -->")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Snapshot
# ---------------------------------------------------------------------------

def render_snapshot(result: dict, declared: list[str], index_link: str = "../workspace/00-INDEX.md") -> str:
    rows = result["rows"]
    matched_ids = {row["id"] for row in result["matched"]}
    out: list[str] = []
    add = out.append
    add("# Board snapshot — the root Task Board at TFW 2.0.0\n")
    add("")
    add("Every data row of the root `README.md` Task Board, captured verbatim on the day")
    add("the board was removed. This is history: it is never edited, never re-sorted and")
    add("never brought up to date. Live state lives in each task's own `status.md`, and the")
    add("browsable view is rebuilt at")
    add(f"[`{index_link.lstrip('./')}`]({index_link}).")
    add("")
    add("Backlog rows are here too. Six of them are ideas that never had a task directory —")
    add("a snapshot of only finished work would have deleted the project's backlog. An idea")
    add("is picked up by creating a real task, not by resurrecting a row.")
    add("")
    add("| | |")
    add("|---|---|")
    add(f"| Rows captured | {len(rows)} |")
    add(f"| With a task directory | {len(matched_ids)} |")
    add(f"| Board-only, no directory | {len(result['board_only'])} |")
    add(f"| In a shape no strict row parser matches | {len(result['malformed'])} |")
    add(f"| With a malformed identifier | {len(result['malformed_identifiers'])} |")
    add("")

    add("## Rows\n")
    add("| ID | Task | Status | Class |")
    add("|---|---|---|---|")
    for row in rows:
        identifier = row["id"] or row["id_text"] or "(none)"
        if not row["id"]:
            klass = "malformed identifier, reported without action"
        elif row["id"] in matched_ids:
            klass = "absorbed elsewhere, directory retained" if row["struck"] else (
                "plain-text row, directory exists" if not row["linked"] else "matched")
        elif row.get("unresolved_path") is not None:
            # A directory exists; its NAME is what the grammar rejects. Never "backlog":
            # this class was invented because that label was applied to two directories
            # holding completed traces.
            klass = "board-only, directory unresolved"
        elif row["struck"]:
            klass = "board-only, absorbed elsewhere"
        else:
            klass = "board-only, backlog"
        title = _plain(row["title"]).replace("|", "\\|")
        # Rendered as text: a status cell can carry a Markdown link whose path is relative
        # to the project root and therefore broken from inside this file. The byte-verbatim
        # record is the fenced block below, not this table.
        status = _plain(row["status_cell"]).replace("|", chr(92) + "|") or "—"
        add(f"| `{identifier}` | {_bound(title, 200)} | {status} | {klass} |")
    add("")

    add("## Verbatim source\n")
    add("The rows exactly as the board carried them, links, strike-through and schema drift")
    add("included. This block is what makes the table above checkable.")
    add("")
    add("```text")
    for row in rows:
        add(row["raw"])
    add("```")
    add("")
    add("---")
    add("")
    add("*Captured once by `.tfw/scripts/migrate_board.py`. Historical — do not update.*")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Accounting manifest
# ---------------------------------------------------------------------------

def render_manifest(root: Path, result: dict, declared: list[str],
                    writes: list[tuple[Path, str]], title: str = "Migration accounting") -> str:
    guarantees = require_guarantees(result)
    rows = result["rows"]
    directories = result["directories"]
    out: list[str] = []
    add = out.append
    add("# " + title)
    add("")
    add("")
    add("Produced by `python .tfw/scripts/migrate_board.py --manifest`. Runtime guarantees")
    add("are shown with their arithmetic below; conditions this run did not check are named")
    add("separately. Re-runnable: the numbers are computed from the tree, not transcribed.")
    add("")
    add("## Reconciliation\n")
    add("```")
    add(f"  {len(rows):3} board data rows")
    add(f"  {len(directories) + len(result['unresolved_dirs']):3} task directories")
    add("  " + "-" * 40)
    add(f"  {len(rows) + len(directories) + len(result['unresolved_dirs']):3} source occurrences  ->  "
        f"{len(set(list(directories) + [r['id'] for r in rows if r['id']])):3} logical identities")
    add("")
    add(f"      {len(result['matched']):3}  matched       row and directory both exist")
    add(f"      {len(result['board_only']):3}  board-only    a row with no directory at all")
    add(f"      {len(result['unresolved']):3}  unresolved    a row whose directory the grammar rejects")
    add(f"      {len(result['orphan_dirs']):3}  unresolved    a rejected directory no row names")
    add(f"      {len(result['directory_only']):3}  directory-only  a directory with no row")
    add("```")
    add("")
    add(f"Rows in a shape no strict `| [ID](path)` parser matches: **{len(result['malformed'])}**. "
        "They are reported, not repaired.")
    add("")

    add("## Malformed identifiers\n")
    add("A whole identifier candidate matching none of the three named grammars. It is")
    add("reported, never shortened, and never produces task state.")
    add("")
    if result["malformed_identifiers"]:
        add("| Candidate | Board line | Directory the row names | Action |")
        add("|---|---:|---|---|")
        for row in result["malformed_identifiers"]:
            path = row.get("unresolved_path")
            directory = (f"`{path.relative_to(root).as_posix()}`" if path is not None else "none")
            add(f"| `{row['id_text'] or '(empty)'}` | {row['line']} | {directory} | "
                "none — malformed |")
    else:
        add("None.")
    add("")

    add("## Board-only rows\n")
    add("A row with **no directory at all**. A row whose directory exists but whose directory")
    add("*name* the grammar rejects is not here — it is under Unresolved inputs, because")
    add("calling it a backlog idea asserts something the source never said.")
    add("")
    if result["board_only"]:
        add("| ID | Status | Why it has no directory |")
        add("|---|---|---|")
        for row in result["board_only"]:
            reason = "absorbed into another task" if row["struck"] else "backlog idea, never started"
            add(f"| `{row['id'] or '(none)'}` | {row['status_cell'] or '—'} | {reason} |")
    else:
        add("None.")
    add("")

    add("## Unresolved inputs\n")
    add("A directory none of the three identifier grammars parses — not current")
    add("`PREFIX_YYYYMMDD-HHMMSS_ABBR`, not dirty-clock `YYYYMMDD-HHMMSS__slug`, and not")
    add("legacy `PREFIX-N` optionally followed by `__slug`.")
    add("**No state file is written for one, and nothing is asserted about whether work")
    add("happened there.** The grammar is not widened and the migration takes no action.")
    add("")
    if result["unresolved"] or result["orphan_dirs"]:
        add("| Directory | Named by a board row? | Status the board carried |")
        add("|---|---|---|")
        for row in result["unresolved"]:
            path = row["unresolved_path"].relative_to(root).as_posix()
            add(f"| `{path}` | `{row['id']}` | {row['status_cell'] or '—'} |")
        for path in result["orphan_dirs"]:
            add(f"| `{path.relative_to(root).as_posix()}` | no | — |")
    else:
        add("None — every directory name parses.")
    add("")

    add("## Directory-only entries\n")
    if result["directory_only"]:
        add("| ID | Path |")
        add("|---|---|")
        for entry in result["directory_only"]:
            add(f"| `{entry['id']}` | `{entry['path'].relative_to(root).as_posix()}` |")
    else:
        add("None — every directory is named by a row, though not every row names it in a "
            "shape a strict parser matches.")
    add("")

    add("## Malformed rows\n")
    if result["malformed"]:
        add("| ID | Form | Directory? |")
        add("|---|---|---|")
        for row in result["malformed"]:
            form = "struck through" if row["struck"] else "plain text, not a link"
            has = "yes" if row["id"] in directories else "no"
            add(f"| `{row['id'] or '(none)'}` | {form} | {has} |")
    else:
        add("None.")
    add("")

    # --- every identifier, by name -----------------------------------------
    written = {
        parsed[1] for path, _ in writes
        if (parsed := parse_identifier(path.parent.name)) is not None
    }
    resolution: list[tuple[str, str]] = []
    for row in rows:
        identifier = row["id"]
        if not identifier:
            resolution.append((row["id_text"] or "(no identifier)",
                               "malformed identifier; reported, no action"))
            continue
        where = ["snapshot"]
        if identifier in directories:
            where.append("task directory")
            if identifier in written:
                where.append("`status.md` → index")
            else:
                where.append("index (unresolved or closed)")
        elif row.get("unresolved_path") is not None:
            # The directory is real; its name is what no grammar parses. Saying so here is
            # what makes the manifest and the index agree — the index reports the same
            # directory under Unresolved inputs, for the same stated reason.
            where.append("directory whose name the grammar rejects")
            where.append("index (unresolved)")
        resolution.append((identifier, " + ".join(where)))

    add(f"## Every board identifier, by name — {len(resolution)}\n")
    add("The requirement is that each row is **classified** after the board is gone, and that")
    add("the list is produced by counting rather than asserted. A previous pass claimed")
    add("61 rows were retained while the snapshot held zero; naming them individually is what")
    add("makes that failure impossible to repeat.")
    add("")
    add("| # | Identifier | Resolves to |")
    add("|---:|---|---|")
    for number, (identifier, where) in enumerate(resolution, 1):
        add(f"| {number} | `{identifier}` | {where} |")
    add("")
    add("**Unaccounted: 0.** Every board row is classified exactly once; malformed")
    add("identifiers are reported rather than described as resolved.")
    add("")

    add("## Task state written\n")
    if writes:
        add("Only for non-terminal tasks that have a directory. Every value comes from the")
        add("board or the directory; `unrecorded` marks a fact the source never carried.")
        add("")
        add("| Task | Lifecycle | Authority | Note |")
        add("|---|---|---|---|")
        for path, content in writes:
            fields = dict(
                line.split(": ", 1) for line in content.splitlines()
                if ": " in line and not line.startswith(("**", "<!--"))
            )
            note = ""
            if fields.get("lifecycle") == "UNDECLARED":
                note = f"status `{fields.get('lifecycle_verbatim', '')}` is outside the declared vocabulary — carried verbatim"
            add(f"| `{fields.get('id')}` | {fields.get('lifecycle')} | "
                f"`{fields.get('authority')}` | {note} |")
    else:
        add("None.")
    add("")

    add("## Guarantees checked\n")
    add("| Guarantee | Arithmetic | Result |")
    add("|---|---|---|")
    for item in guarantees:
        add(f"| {item['name']} | {item['arithmetic']} | **HELD** |")
    add("")
    add("## Guarantees not checked by this run\n")
    add("Renames, moves, byte preservation and fact synthesis are protected by the")
    add("write-new-only implementation and its framework tests. This accounting run does not")
    add("claim to infer those properties from the corpus in front of it.")
    add("")
    add("---")
    add("")
    add(f"*{title}*")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def read_board(root: Path, board: str = DEFAULT_BOARD, revision: str | None = DEFAULT_REVISION,
               working_tree: bool = False) -> tuple[str, str]:
    """The board text, and a human-readable description of where it came from.

    **The location is an input, not a constant.** The first external project to run this
    kept its board at ``tasks/README.md`` under a different heading, for a documented
    reason: its root ``README.md`` is fully regenerated, so a board there is destroyed. Run
    with the location hardcoded, this returned zero rows and then sent the reader off to
    diagnose a *removed* board when the board was merely *elsewhere*.

    **The default source is a committed revision.** The board is a historical input and a
    migration whose whole value is exact accounting must not read a file that can change
    underneath it — during one real run the source changed three times while being read.
    The working tree is the explicit opt-in.

    This is one code path with :func:`read_board`'s two concerns joined on purpose. Reading
    the location from the working tree while logging a revision would produce a run whose
    log names a revision it did not read: a false provenance statement, which is worse than
    either defect on its own.

    There is **no silent fallback.** With no committed board — not a Git repository, or the
    path absent at the revision — the run refuses and names the opt-in. A printed notice is
    the thing nobody reads, and a silent live read is exactly what defaulting to a revision
    exists to remove.
    """
    if working_tree:
        path = root / board
        if not path.exists():
            raise SystemExit(
                f"no board at {board} in the working tree.\n"
                f"  Name its location with --board <path> if the project keeps it elsewhere."
            )
        return path.read_text(encoding="utf-8"), f"{board} (working tree, --working-tree)"

    result = subprocess.run(
        ["git", "show", f"{revision}:{board}"],
        cwd=root, capture_output=True, text=True, encoding="utf-8", check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or "git could not read it"
        raise SystemExit(
            f"cannot read {board} at {revision}: {detail}\n"
            f"  Tried: git show {revision}:{board}\n"
            f"  The default source is a COMMITTED revision, because a migration whose value\n"
            f"  is exact accounting must not read a file that can change while it is read.\n"
            f"  If the board lives elsewhere:      --board <path> [--board-heading '## ...']\n"
            f"  If it is at another revision:      --board-rev <commit>\n"
            f"  If it is only in the working tree: --working-tree  (deliberate, and logged)"
        )
    return result.stdout, f"git show {revision}:{board}"


def legacy_container(root: Path) -> str:
    """Where the snapshot belongs: the last configured container, which holds the old corpus."""
    containers = task_containers(root)
    return containers[-1] if containers else "tasks"


def plan(root: Path, now: str, board_text: str | None = None,
         heading: str = BOARD_HEADING
         ) -> tuple[dict, list[tuple[Path, str]], list[str]]:
    declared = declared_statuses(root)
    if board_text is None:
        board_text, _ = read_board(root)
    rows = parse_board(board_text, heading)
    result = reconcile(root, rows)
    require_guarantees(result)

    writes: list[tuple[Path, str]] = []
    for row in result["matched"]:
        status = classify_status(row["status_cell"], declared)
        if status["lifecycle"] in TERMINAL:
            continue
        if row["struck"]:
            # A struck-through row records work absorbed into another task. Its directory
            # is a trace, not a live task. Giving it state would make an entry the board
            # itself retired look actionable again; it stays an unresolved input instead,
            # visible in the snapshot and in the index's unresolved section.
            continue
        writes.append((row["path"] / "status.md",
                       build_status(root, row, declared, now), row["id"]))
    writes.sort(key=lambda item: sort_key(*parse_identifier(item[2])))
    writes = [(path, content) for path, content, _ in writes]

    # The index lives in the FIRST container; the snapshot in the last. Both come from
    # configuration, so a project that renamed either still gets a working link.
    containers = task_containers(root)
    index_link = f"../{containers[0]}/00-INDEX.md" if containers else "../workspace/00-INDEX.md"
    snapshot = render_snapshot(result, declared, index_link)
    return result, writes, [snapshot]


def main(argv: list[str] | None = None) -> int:
    make_streams_printable()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=None,
                        help="the project root. Default: found by walking upward from this "
                             "script for a .tfw/ directory, so the tools work wherever a "
                             "project places them")
    parser.add_argument("--apply", action="store_true", help="write files; default is a dry run")
    parser.add_argument("--manifest", type=Path, help="write the accounting to this path")
    parser.add_argument("--now", default=datetime.now().strftime("%Y%m%d-%H%M%S"),
                        help="the moment stamped into `updated`, YYYYMMDD-HHMMSS. Defaults "
                             "to a read of the system clock; pass a value only to make a "
                             "run reproducible in a test")
    parser.add_argument("--board", default=DEFAULT_BOARD, metavar="PATH",
                        help=f"where the board lives, relative to the project root. Default "
                             f"{DEFAULT_BOARD}. A project whose root README is regenerated "
                             f"legitimately keeps it elsewhere — tasks/README.md, for one")
    parser.add_argument("--board-heading", default=BOARD_HEADING, metavar="HEADING",
                        help=f"the Markdown heading the board table follows. Default "
                             f"{BOARD_HEADING!r}")
    parser.add_argument("--board-rev", metavar="REV", default=DEFAULT_REVISION,
                        help=f"the Git revision to read the board from. Default "
                             f"{DEFAULT_REVISION}: a committed revision is the stable input "
                             f"for a migration whose value is exact accounting")
    parser.add_argument("--working-tree", action="store_true",
                        help="read the board from the working tree instead of a committed "
                             "revision. Deliberate, and recorded in the run log — the file "
                             "can change while it is being read")
    parser.add_argument("--skip-existing", action="store_true",
                        help="write only the files that do not yet exist, instead of "
                             "refusing the whole run. Use when re-running over a corpus "
                             "whose live tasks have already moved on: their state is theirs "
                             "now, and migration must not reach back into it")
    parser.add_argument("--allow-empty-board", action="store_true",
                        help="proceed even when the board source yields zero rows. Only ever "
                             "correct when a project genuinely never had a board")
    args = parser.parse_args(argv)

    root = (args.root or find_project_root()).resolve()
    print(f"project root: {root}", file=sys.stderr)
    declared = declared_statuses(root)
    board_text, origin = read_board(root, args.board, args.board_rev, args.working_tree)
    print(f"clock read: {args.now}", file=sys.stderr)
    try:
        result, writes, (snapshot,) = plan(root, args.now, board_text, args.board_heading)
    except (MigrationRefusal, IdentifierCollisionError) as exc:
        print(f"REFUSING: {exc}\nNothing was changed.", file=sys.stderr)
        return 1
    snapshot_path = root / legacy_container(root) / "BOARD-SNAPSHOT.md"

    rows = len(result["rows"])
    print(f"board source: {origin} -> {rows} data rows", file=sys.stderr)
    if rows == 0 and not args.allow_empty_board:
        # Relocation is named FIRST. The previous message offered only --board-rev, which
        # sent the reader to diagnose a removed board while the real cause — on the one real
        # project that hit this — was a board sitting somewhere else entirely.
        print(f"REFUSING: {origin} yielded zero rows under the heading "
              f"{args.board_heading!r}.\n"
              "  A snapshot of an empty board is not a snapshot, it is a deleted trace.\n"
              "  Three causes, in the order they actually occur:\n"
              "    1. the board is ELSEWHERE -- a project whose root README is regenerated\n"
              "         keeps it somewhere safe:  --board tasks/README.md\n"
              "    2. the heading differs        --board-heading '## Board'\n"
              "    3. the board was REMOVED      --board-rev <commit-before-removal>\n"
              "  If this project genuinely never had a board, pass --allow-empty-board.",
              file=sys.stderr)
        return 1

    try:
        manifest = render_manifest(root, result, declared, writes)
    except MigrationRefusal as exc:
        print(f"REFUSING: {exc}\nNothing was changed.", file=sys.stderr)
        return 1
    if args.manifest:
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(manifest, encoding="utf-8", newline="\n")
        print(f"wrote {args.manifest}")
    else:
        print(manifest)

    if not args.apply:
        print(f"DRY RUN: would write {len(writes) + 1} files "
              f"({len(writes)} task state, 1 snapshot). Nothing was changed.", file=sys.stderr)
        return 0

    targets = [(snapshot_path, snapshot)] + writes
    existing = [path for path, _ in targets if path.exists()]
    if existing and not args.skip_existing:
        for path in existing:
            print(f"refusing to overwrite: {path}", file=sys.stderr)
        print("Migration writes new files only. Nothing was changed.",
              file=sys.stderr)
        print("  Pass --skip-existing to write the rest and leave these alone.",
              file=sys.stderr)
        return 1
    if existing:
        for path in existing:
            print(f"skipping, already exists: {path.relative_to(root).as_posix()}",
                  file=sys.stderr)
        targets = [(path, content) for path, content in targets if not path.exists()]
    for path, content in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"wrote {path.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
