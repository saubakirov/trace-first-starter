"""Generate the derived portfolio index.

The index is a **projection**. Task state lives in each task's own ``status.md`` and is the
only authority for that task; this file rebuilds a browsable view of all of them and can be
deleted at any time without losing a fact.

Determinism is a hard requirement: the same inputs must produce the same bytes. Every
ordering here is an explicit sort by a declared key. Directory iteration order is never
inherited, and the freshness stamp is derived from the inputs rather than the wall clock,
so two runs a minute apart are identical.

This module is also the canonical home of the shared task resolver — ``parse_identifier``,
``read_config``, ``iter_task_dirs`` and ``read_status`` — which ``migrate_board.py`` and
``gen_docs.py`` import rather than pattern-matching per call site.

Usage:
    python docs/scripts/gen_index.py [--check]

    --check   write nothing; exit 1 if the committed index differs from what would be
              generated. Intended for the build gate.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Shared task resolver
# ---------------------------------------------------------------------------

#: Clock-derived identifier introduced in TFW 2.0.0: ``YYYYMMDD-HHMMSS``.
CLOCK_ID = re.compile(r"^(\d{8})-(\d{6})$")

#: Legacy identifier grammar: ``{PREFIX}-{seq}``.
LEGACY_ID = re.compile(r"^([A-Z][A-Z0-9]*)-(\d+)$")

#: Directory name: ``<identifier>__<slug>``.
TASK_DIR = re.compile(r"^(?P<id>[^_]+(?:_[^_]+)*?)__(?P<slug>.+)$")

NEWLINE = chr(10)

DEFAULT_CONTAINERS = ["tasks"]

TERMINAL = {"DONE", "REJECTED"}

STATUS_KEYS = {
    "id", "title", "goal", "value", "lifecycle", "lifecycle_verbatim",
    "owner", "authority", "outcome", "created", "updated",
}

BOUNDS = {"title": 80, "goal": 160, "value": 160, "outcome": 160, "lifecycle_verbatim": 80}


def parse_identifier(text: str) -> tuple[str, str] | None:
    """Classify a task identifier under either grammar.

    Returns ``(kind, identifier)`` where kind is ``"clock"`` or ``"legacy"``, or ``None``
    when the text is neither. One resolver, used by every consumer — per-call-site regexes
    are how the previous board parser drifted out of sync with the board it parsed.
    """
    text = text.strip()
    if CLOCK_ID.match(text):
        return ("clock", text)
    if LEGACY_ID.match(text):
        return ("legacy", text)
    return None


def sort_key(kind: str, identifier: str) -> tuple:
    """Declared sort key. Legacy tasks sort before clock tasks; within each, ascending.

    Legacy identifiers sort numerically, so ``TFW-9`` precedes ``TFW-10``. Clock
    identifiers sort lexically, which for a fixed-width timestamp is chronological. The
    newest task is therefore the last entry.
    """
    if kind == "legacy":
        m = LEGACY_ID.match(identifier)
        return (0, m.group(1), int(m.group(2)))
    return (1, identifier, 0)


def read_config(root: Path) -> dict:
    """Read the TFW block from ``project_config.yaml``."""
    path = root / ".tfw" / "project_config.yaml"
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as handle:
        return (yaml.safe_load(handle) or {}).get("tfw", {}) or {}


def task_containers(root: Path) -> list[str]:
    """Ordered container list. A task is created in the first; resolved across all."""
    value = read_config(root).get("task_containers") or DEFAULT_CONTAINERS
    if isinstance(value, str):
        value = [value]
    return [str(item).strip("/") for item in value]


def iter_task_dirs(root: Path, containers: list[str] | None = None) -> list[Path]:
    """Every task directory across every container, in a deterministic order.

    A container may hold task directories directly (the legacy layout) or nested under a
    creation-year folder (the layout introduced in 2.0.0). Both are searched. The result is
    sorted by the declared key rather than by whatever order the filesystem offered.
    """
    if containers is None:
        containers = task_containers(root)
    found: list[tuple[tuple, Path]] = []
    seen: set[Path] = set()
    for container in containers:
        base = root / container
        if not base.is_dir():
            continue
        # One level of year nesting is expanded; anything deeper is a task's own content.
        pending = sorted((p for p in base.iterdir() if p.is_dir()), key=lambda p: p.name)
        while pending:
            child = pending.pop(0)
            if re.fullmatch(r"\d{4}", child.name) and child.parent == base:
                pending = sorted(
                    (p for p in child.iterdir() if p.is_dir()), key=lambda p: p.name
                ) + pending
                continue
            match = TASK_DIR.match(child.name)
            if not match:
                continue
            parsed = parse_identifier(match.group("id"))
            if parsed is None or child.resolve() in seen:
                continue
            seen.add(child.resolve())
            found.append((sort_key(*parsed), child))
    found.sort(key=lambda pair: (pair[0], str(pair[1])))
    return [path for _, path in found]


def read_status(task_dir: Path) -> dict | None:
    """Parse ``status.md`` front matter. Returns ``None`` when the file is absent.

    A file that exists but cannot be parsed returns a dict carrying ``_error``: a malformed
    input is reported, never dropped.
    """
    path = task_dir / "status.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        return {"_error": "no YAML front matter"}
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return {"_error": f"unparseable front matter: {exc.__class__.__name__}"}
    if not isinstance(data, dict):
        return {"_error": "front matter is not a mapping"}
    problems = []
    unknown = sorted(set(data) - STATUS_KEYS)
    if unknown:
        problems.append("unknown keys: " + ", ".join(unknown))
    for key in ("id", "title", "lifecycle", "owner", "authority"):
        if not data.get(key):
            problems.append(f"missing {key}")
    for key, limit in BOUNDS.items():
        value = data.get(key)
        if isinstance(value, str) and len(value) > limit:
            problems.append(f"{key} exceeds {limit} code points")
    if problems:
        data["_error"] = "; ".join(problems)
    return data


# ---------------------------------------------------------------------------
# Board snapshot
# ---------------------------------------------------------------------------

def read_snapshot(root: Path) -> list[dict]:
    """Read the frozen board snapshot, if one exists.

    The snapshot is the record of tasks that closed before the migration and of backlog
    rows that never had a directory. It is historical and never changes.
    """
    path = root / "tasks" / "BOARD-SNAPSHOT.md"
    if not path.exists():
        return []
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        rows.append({
            "id": cells[0].strip("`"),
            "title": cells[1],
            "lifecycle": cells[2],
            "class": cells[3],
        })
    return rows


def snapshot_index(rows: list[dict]) -> dict[str, dict]:
    """Snapshot rows by identifier, for deciding what a directory without state is."""
    return {row["id"]: row for row in rows if row["id"] and row["id"] != "(none)"}


# ---------------------------------------------------------------------------
# Index rendering
# ---------------------------------------------------------------------------

def _cell(value: object, dash: str = "—") -> str:
    text = "" if value is None else str(value).strip()
    return text.replace("|", "\\|") if text else dash


def _link(root: Path, base: Path, target: Path) -> str:
    """A link from the index file to a task, relative to where the index actually lives.

    The index sits inside the first container, not at the project root. Emitting
    root-relative paths produces a file whose every link is broken — which is exactly what
    a corpus-wide link check catches and a reader hits on the first click.
    """
    return os.path.relpath(target, base).replace(os.sep, "/")


def collect(root: Path) -> dict:
    """Gather every input the index renders, with malformed entries kept visible."""
    containers = task_containers(root)
    base = output_path(root).parent
    snapshot = read_snapshot(root)
    by_id = snapshot_index(snapshot)

    live: list[dict] = []
    historical: list[dict] = []
    unresolved: list[dict] = []
    for task_dir in iter_task_dirs(root, containers):
        rel = _link(root, base, task_dir)
        name = TASK_DIR.match(task_dir.name)
        parsed = parse_identifier(name.group("id"))
        status = read_status(task_dir)
        if status is not None and not status.get("_error"):
            status["_path"] = rel
            status["_kind"] = parsed[0]
            status["_key"] = sort_key(*parsed)
            live.append(status)
            continue
        if status is not None:
            unresolved.append({"path": rel, "id": parsed[1], "reason": status["_error"]})
            continue
        # No state file. That is normal for a task that closed before 2.0.0 — the board
        # snapshot is its record and writing state for it would invent a live task. It is
        # only unresolved when the snapshot cannot vouch for it either.
        row = by_id.get(parsed[1])
        if row and row["class"] == "matched":
            historical.append({
                "path": rel, "id": parsed[1], "title": row["title"],
                "lifecycle": row["lifecycle"], "_key": sort_key(*parsed),
            })
        else:
            reason = (f"no status.md; board row class: {row['class']}" if row
                      else "no status.md, and no board row names it")
            unresolved.append({"path": rel, "id": parsed[1], "reason": reason})

    live.sort(key=lambda item: item["_key"])
    historical.sort(key=lambda item: item["_key"])
    backlog = [row for row in snapshot if row["class"] == "board-only, backlog"]
    absorbed = [row for row in snapshot if row["class"] == "board-only, absorbed elsewhere"]
    freshness = max((str(item.get("updated") or "") for item in live), default="")
    return {
        "containers": containers,
        "live": live,
        "historical": historical,
        "backlog": backlog,
        "absorbed": absorbed,
        "unresolved": unresolved,
        "snapshot": snapshot,
        "freshness": freshness,
        "snapshot_link": _link(root, base, root / "tasks" / "BOARD-SNAPSHOT.md"),
    }


def render(data: dict) -> str:
    live = data["live"]
    historical = data["historical"]
    backlog = data["backlog"]
    absorbed = data["absorbed"]
    unresolved = data["unresolved"]
    snapshot = data["snapshot"]
    out: list[str] = []
    add = out.append

    add("# Portfolio index")
    add("")
    add("> **This file is derived and non-authoritative.** It is rebuilt from every task's")
    add("> own `status.md` by `docs/scripts/gen_index.py`. When it disagrees with a task,")
    add("> the task is right. Delete it and nothing is lost; regenerate it and it comes")
    add("> back. Any workflow acting on a task re-reads that task's `status.md` first.")
    add("")
    add("| | |")
    add("|---|---|")
    add(f"| Source | {len(live)} task state files"
        + (f", {len(snapshot)} snapshot rows" if snapshot else "") + " |")
    add(f"| Containers searched | {', '.join(f'`{c}/`' for c in data['containers'])} |")
    add(f"| Freshness | newest task state update: {data['freshness'] or 'unknown'} |")
    add(f"| Unresolved inputs | {len(unresolved)} |")
    add("| Generator | `python docs/scripts/gen_index.py` |")
    add("")

    active = [item for item in live if str(item.get("lifecycle")) not in TERMINAL]
    closed = [item for item in live if str(item.get("lifecycle")) in TERMINAL]

    add(f"## In flight — {len(active)}")
    add("")
    if active:
        add("| Task | Lifecycle | Owner | Goal | Authority |")
        add("|---|---|---|---|---|")
        for item in active:
            lifecycle = str(item.get("lifecycle"))
            if lifecycle == "UNDECLARED":
                lifecycle = f"UNDECLARED (`{_cell(item.get('lifecycle_verbatim'))}`)"
            authority = _cell(item.get("authority"), "")
            link = (f"[{authority}]({item['_path']}/{authority})"
                    if authority and authority != "unrecorded" else "—")
            add(
                f"| [**{_cell(item.get('id'))}** — {_cell(item.get('title'))}]"
                f"({item['_path']}/status.md) | {lifecycle} | {_cell(item.get('owner'))} "
                f"| {_cell(item.get('goal'))} | {link} |"
            )
    else:
        add("No task is in flight.")
    add("")

    add(f"## Closed — {len(closed) + len(historical)}")
    add("")
    if closed or historical:
        add("| Task | Outcome | Record |")
        add("|---|---|---|")
        for item in closed:
            add(
                f"| **{_cell(item.get('id'))}** — {_cell(item.get('title'))} "
                f"| {_cell(item.get('lifecycle'))}"
                + (f" · {_cell(item.get('outcome'), '')}" if item.get("outcome") else "")
                + f" | [state]({item['_path']}/status.md) |"
            )
        for item in historical:
            add(
                f"| **{item['id']}** — {_cell(item['title'])} | {_cell(item['lifecycle'])} "
                f"| [task folder]({item['path']}/) |"
            )
    else:
        add("Nothing has closed yet.")
    add("")
    if historical:
        add(f"{len(historical)} of those closed before TFW 2.0.0 and carry no state file.")
        add("That is by design: writing state for finished work would turn a record into a")
        add("live task. Their record is the board row captured in")
        add(f"[`tasks/BOARD-SNAPSHOT.md`]({data['snapshot_link']}), and their folders are")
        add("untouched.")
        add("")

    if backlog:
        add(f"## Backlog — {len(backlog)}")
        add("")
        add("Rows the board carried that never became a task directory. They are ideas, not")
        add("work in progress. Picking one up means creating a task in")
        add(f"`{data['containers'][0]}/`, not reviving a row.")
        add("")
        add("| Idea | Recorded as |")
        add("|---|---|")
        for row in backlog:
            add(f"| `{row['id']}` — {_cell(row['title'])} | {_cell(row['lifecycle'])} |")
        add("")

    if absorbed:
        add(f"## Absorbed — {len(absorbed)}")
        add("")
        add("Rows retired when their work was folded into another task. Kept because a")
        add("reference to one of these identifiers still has to land somewhere.")
        add("")
        add("| Row | Absorbed into |")
        add("|---|---|")
        for row in absorbed:
            title = _cell(row["title"])
            head, _, tail = title.partition(" — absorbed into ")
            add(f"| `{row['id']}` — {head} | {tail or '—'} |")
        add("")

    add(f"## Unresolved inputs — {len(unresolved)}")
    add("")
    add("Reported, never dropped. An entry here names a real directory whose state could")
    add("not be established. It stays visible and non-actionable until someone decides what")
    add("it is.")
    add("")
    if unresolved:
        add("| Path | Identifier | Diagnostic |")
        add("|---|---|---|")
        for item in sorted(unresolved, key=lambda entry: entry["path"]):
            add(f"| `{item['path']}` | `{item['id']}` | {item['reason']} |")
    else:
        add("None.")
    add("")

    add("---")
    add("")
    add("*Generated by `docs/scripts/gen_index.py`. Do not edit: every change is lost on")
    add("the next run, and the authority it would contradict lives in the task folders.*")
    return NEWLINE.join(out) + NEWLINE


def build(root: Path) -> str:
    return render(collect(root))


def output_path(root: Path) -> Path:
    return root / task_containers(root)[0] / "00-INDEX.md"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--check", action="store_true",
                        help="write nothing; exit 1 if the committed index is stale")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    content = build(root)
    target = output_path(root)

    if args.check:
        current = target.read_text(encoding="utf-8") if target.exists() else None
        if current == content:
            print(f"index up to date: {target.relative_to(root).as_posix()}")
            return 0
        print(f"index is stale: {target.relative_to(root).as_posix()}", file=sys.stderr)
        return 1

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrote {target.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
