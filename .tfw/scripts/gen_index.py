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
    python .tfw/scripts/gen_index.py                 # rebuild the index
    python .tfw/scripts/gen_index.py --check index   # is the derived index current?
    python .tfw/scripts/gen_index.py --check tasks   # is each task's own state legal?
    python .tfw/scripts/gen_index.py --check project # is this project consistent with the release?

**Where this file lives is not load-bearing.** The project root is found by walking upward
for a ``.tfw/`` directory, so a project may place these tools anywhere — ``.tfw/scripts/``
is where the payload ships them and nothing depends on that. Every run prints the root it
resolved, because a wrong root must be visible rather than inferred.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Project root
# ---------------------------------------------------------------------------

#: The marker that identifies a project root. A TFW project is a directory containing this.
ROOT_MARKER = ".tfw"

#: A staging directory `update.md` Step 0 creates by cloning upstream. It contains a complete
#: `.tfw/`, so it satisfies the marker — and resolving to it would generate a project's index
#: from the upstream clone instead of the project. Skipped by name, never by depth.
STAGING_SEGMENT = ".upstream"


def make_streams_printable() -> None:
    """Let stdout and stderr carry the project's own characters, wherever they land.

    Runtime *messages* are ASCII by rule, and a test enforces it. **Content is not** — a
    migration manifest quotes a board verbatim, and a real board carries the emoji its
    project wrote. On a console whose codepage is cp1252 that is an unhandled
    ``UnicodeEncodeError``, and the first command the migration guide gives dies before it
    prints anything useful. Found by running the guide on a real external corpus.

    Written files keep ``encoding="utf-8"`` and stay exact; only console rendering degrades,
    which is the correct trade: a replacement character in a terminal beats a traceback.
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue           # a pytest capture object, or any non-TextIO replacement
        try:
            reconfigure(encoding="utf-8", errors="replace")
        except (ValueError, OSError):
            pass               # already detached, or a stream that refuses; not fatal


def find_project_root(start: Path | None = None) -> Path:
    """The project root, found by walking upward for a ``.tfw/`` directory.

    Depth arithmetic — ``Path(__file__).parents[2]`` — was the previous answer, and it made
    the tools' own location load-bearing: a project that placed them anywhere else had to
    edit ``.tfw/`` and forfeit clean updates. It was also *silently* wrong rather than
    loudly wrong, because from ``.tfw/scripts/`` the third parent happens to be the root.

    The search starts at this file's own directory, so it answers for wherever the tools
    were put rather than for wherever they were invoked from. A candidate whose path
    contains ``.upstream`` is skipped: that directory holds a full upstream clone and would
    otherwise capture the search one level early.

    Raises ``SystemExit`` when no root is found. There is no fallback — guessing a root
    means writing files into a directory nobody chose.
    """
    start = (start or Path(__file__)).resolve()
    base = start if start.is_dir() else start.parent
    for candidate in (base, *base.parents):
        if STAGING_SEGMENT in candidate.parts:
            continue
        if (candidate / ROOT_MARKER).is_dir():
            return candidate
    raise SystemExit(
        f"no project root above {base}: no directory contains {ROOT_MARKER}/.\n"
        f"  Pass --root <path> to name it explicitly."
    )


# ---------------------------------------------------------------------------
# Shared task resolver
# ---------------------------------------------------------------------------

#: Clock-derived identifier, TFW 2.0.0: the WHOLE directory name, ``YYYYMMDD-HHMMSS__slug``.
#: The timestamp alone is not an identifier — two mutually offline participants can reach
#: the same second, and only the slug distinguishes them. Two who reach the same second AND
#: the same slug created the same task, which is a signal rather than a collision to prevent.
CLOCK_ID = re.compile(r"^(?P<stamp>\d{8}-\d{6})__(?P<slug>.+)$")

#: A bare timestamp. Never a valid identifier; matched only so consumers can say why.
BARE_STAMP = re.compile(r"^\d{8}-\d{6}$")

#: Legacy identifier grammar: ``{PREFIX}-{seq}``, optionally followed by a slug.
LEGACY_ID = re.compile(r"^(?P<prefix>[A-Z][A-Z0-9]*)-(?P<seq>\d+)(?:__(?P<slug>.+))?$")

#: Directory name: ``<identifier>__<slug>`` for legacy, ``<identifier>`` for clock.
TASK_DIR = re.compile(r"^(?P<id>[^_]+(?:_[^_]+)*?)__(?P<slug>.+)$")

NEWLINE = chr(10)

#: A leading YAML front-matter block.
FRONT_MATTER = re.compile("^---" + chr(92) + "r?" + chr(92) + "n(.*?)" + chr(92) + "r?" + chr(92) + "n---" + chr(92) + "r?" + chr(92) + "n", re.S)

DEFAULT_CONTAINERS = ["tasks"]

TERMINAL = {"DONE", "REJECTED"}

STATUS_KEYS = {
    "id", "title", "goal", "value", "lifecycle", "lifecycle_verbatim",
    "owner", "authority", "outcome", "created", "updated",
}

BOUNDS = {"title": 80, "goal": 160, "value": 160, "outcome": 160, "lifecycle_verbatim": 80}

REQUIRED_KEYS = ("id", "title", "goal", "value", "lifecycle", "owner", "authority",
                 "created", "updated")

#: Fallback vocabulary when project_config.yaml cannot be read.
DECLARED_LIFECYCLES = ("TODO", "HL_DRAFT", "RES", "PHASES", "TS_DRAFT", "ONB", "RF", "REV",
                       "KNW", "DONE", "BLOCKED", "REJECTED")

#: Not selectable by a person. Migration writes it when a source held a value the
#: vocabulary does not contain, and keeps that value verbatim beside it.
UNDECLARED = "UNDECLARED"

#: `created` and `updated` carry the same grammar as the identifier: second resolution.
#: A day-resolution stamp on a corpus with several transitions a day reports nothing — the
#: rejected pass shipped TFW-60 with `created` and `updated` identical.
STAMP = re.compile(r"^\d{8}-\d{6}$")

#: What a legacy source that carried only a date migrates to. The zero time is DECLARED, not
#: measured: it says "this day, time unknown" and must never be read as second-accurate.
ZERO_TIME = "000000"


def explain_yaml_error(block: str, exc: yaml.YAMLError) -> str:
    """A parse failure named by the key it happened on, not by the exception's class name.

    ``unparseable front matter: ScannerError`` is what this used to say, and a real person
    hand-writing five state files had to find the cause by inspection. The cause was always
    the same and always mechanical: a value containing ``": "`` ends a YAML plain scalar, so
    ``title: Phase A: portable delivery`` is not a string, it is a syntax error.

    PyYAML gives a line and a column, never a key. The key is recovered from the source
    text at the marked line — which is the only place it exists.
    """
    detail = getattr(exc, "problem", None) or exc.__class__.__name__
    mark = getattr(exc, "problem_mark", None) or getattr(exc, "context_mark", None)
    if mark is None:
        return f"unparseable front matter: {detail}"

    lines = block.splitlines()
    line_number = mark.line  # 0-based, into the front-matter block
    # The key is the nearest `key:` at or above the marked line: a broken value can push the
    # reported mark onto the following line.
    key = None
    for index in range(min(line_number, len(lines) - 1), -1, -1):
        head = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", lines[index])
        if head:
            key = head.group(1)
            break
    where = f"line {line_number + 1}"
    if key is None:
        return f"unparseable front matter at {where}: {detail}"
    hint = ""
    value = lines[line_number] if line_number < len(lines) else ""
    if ": " in value.split(":", 1)[-1]:
        # ASCII only. This reaches a terminal whose encoding nobody chose, and a hint that
        # renders as replacement characters is worse than no hint.
        hint = (". A value containing \": \" ends a YAML plain scalar, so quote it: "
                f"{key}: \"...\"")
    return f"unparseable front matter: key `{key}` ({where}): {detail}{hint}"


def parse_identifier(text: str) -> tuple[str, str] | None:
    """Classify a task identifier or directory name under either grammar.

    Accepts what a consumer actually holds — a directory name — and returns
    ``(kind, identifier)``:

    * ``("clock", "20260826-143000__query_redesign")`` — the identifier is the whole name.
    * ``("legacy", "TFW-60")`` — the pre-2.0.0 grammar, where the slug is not part of it.
    * ``None`` — not an identifier. **A bare ``YYYYMMDD-HHMMSS`` lands here on purpose**: it
      is ambiguous between any two tasks created in that second, and no consumer may accept
      one as if it named exactly one task.

    One resolver, used by every consumer. Per-call-site regexes are how the previous board
    parser drifted out of sync with the board it parsed.
    """
    text = text.strip()
    if CLOCK_ID.match(text):
        return ("clock", text)
    match = LEGACY_ID.match(text)
    if match:
        return ("legacy", f"{match.group('prefix')}-{match.group('seq')}")
    return None


def sort_key(kind: str, identifier: str) -> tuple:
    """Declared sort key. Legacy tasks sort before clock tasks; within each, ascending.

    Legacy identifiers sort numerically, so ``TFW-9`` precedes ``TFW-10``. Clock
    identifiers sort by timestamp then slug — fixed-width, so lexical order on the stamp is
    chronological, and the slug only breaks a same-second tie. The newest task is last.
    """
    if kind == "legacy":
        m = LEGACY_ID.match(identifier)
        return (0, m.group("prefix"), int(m.group("seq")), "")
    m = CLOCK_ID.match(identifier)
    return (1, m.group("stamp"), 0, m.group("slug"))


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


def _walk_containers(root: Path, containers: list[str] | None = None
                     ) -> tuple[list[Path], list[Path]]:
    """Every directory the containers hold, split into ``(matched, unmatched)``.

    One walk, two answers. Previously there was one walk and one answer, and a directory
    the identifier grammar did not match was ``continue``d — dropped before any consumer
    could see it. That is how a real external corpus of four tasks was read as two, and how
    two directories holding completed HL, TS and RF traces were then rendered under a
    heading calling them *"ideas, not work in progress"*.

    Dropping silently is bad. Confidently misdescribing is worse, because it reads as a
    finding. So the rejects are returned rather than discarded, and the caller reports them
    as unresolved input.

    A container may hold task directories directly (the legacy layout) or nested under a
    creation-year folder (2.0.0). Both are searched. Matched results are sorted by the
    declared key rather than by whatever order the filesystem offered.
    """
    if containers is None:
        containers = task_containers(root)
    found: list[tuple[tuple, Path]] = []
    unmatched: list[Path] = []
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
            resolved = child.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            parsed = parse_identifier(child.name)
            if parsed is None:
                unmatched.append(child)
                continue
            found.append((sort_key(*parsed), child))
    found.sort(key=lambda pair: (pair[0], str(pair[1])))
    unmatched.sort(key=lambda path: str(path))
    return [path for _, path in found], unmatched


def iter_task_dirs(root: Path, containers: list[str] | None = None) -> list[Path]:
    """Every task directory whose name the identifier grammar matches, in declared order."""
    return _walk_containers(root, containers)[0]


def iter_unmatched_task_dirs(root: Path, containers: list[str] | None = None) -> list[Path]:
    """Every container directory the identifier grammar does **not** match.

    An additive sibling rather than a changed return type, because ``iter_task_dirs`` is
    called by ``gen_docs.py``, ``migrate_board.py`` and their tests.

    These are never *matched* into the grammar. Widening ``LEGACY_ID`` to admit the
    single-underscore form would edit an identifier rule, and the identifier rules are not
    under revision. The tool reports; a person may rename the directory to the recognized
    grammar if they want it picked up — the same shape as the ``UNDECLARED`` rule, where
    migration never normalizes and an accountable owner may resolve.
    """
    return _walk_containers(root, containers)[1]


def declared_lifecycles(root: Path) -> list[str]:
    """The lifecycle vocabulary this project declares."""
    entries = read_config(root).get("statuses") or []
    ids = [str(e.get("id")) for e in entries if isinstance(e, dict) and e.get("id")]
    return ids or list(DECLARED_LIFECYCLES)


def read_status(task_dir: Path, declared: list[str] | None = None) -> dict | None:
    """Parse ``status.md`` front matter. Returns ``None`` when the file is absent.

    A file that exists but cannot be parsed, or that breaks any rule of the closed schema,
    returns a dict carrying ``_error``: a malformed input is reported, never dropped and
    never silently repaired.
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
        return {"_error": explain_yaml_error(match.group(1), exc)}
    if not isinstance(data, dict):
        return {"_error": "front matter is not a mapping"}
    problems = validate_status(data, task_dir, declared)
    if problems:
        data["_error"] = "; ".join(problems)
    return data


def validate_status(data: dict, task_dir: Path | None = None,
                    declared: list[str] | None = None) -> list[str]:
    """Every rule the carrier declares, checked. Returns the problems found, in order.

    The key set is closed, so an unknown key is an error rather than an extension: a field
    nothing reads is exactly what the carrier exists to keep out. Conditional keys are
    checked both ways — present when required, and absent when not applicable — because a
    stray ``outcome`` on a live task is a claim that it finished.
    """
    declared = declared or list(DECLARED_LIFECYCLES)
    problems: list[str] = []

    unknown = sorted(set(data) - STATUS_KEYS)
    if unknown:
        problems.append("unknown keys: " + ", ".join(unknown))

    for key in REQUIRED_KEYS:
        if not data.get(key):
            problems.append(f"missing {key}")

    for key, limit in BOUNDS.items():
        value = data.get(key)
        if isinstance(value, str) and len(value) > limit:
            problems.append(f"{key} exceeds {limit} code points")

    lifecycle = data.get("lifecycle")
    if lifecycle and lifecycle != UNDECLARED and lifecycle not in declared:
        problems.append(
            f"lifecycle '{lifecycle}' is not declared and is not {UNDECLARED}; "
            "an out-of-vocabulary value must be carried as "
            f"{UNDECLARED} plus lifecycle_verbatim, never normalized")

    # Conditional keys, checked in both directions.
    if lifecycle == UNDECLARED and not data.get("lifecycle_verbatim"):
        problems.append(f"lifecycle is {UNDECLARED} but lifecycle_verbatim is absent, "
                        "so the value the source actually carried is lost")
    if lifecycle != UNDECLARED and data.get("lifecycle_verbatim"):
        problems.append("lifecycle_verbatim is only meaningful when lifecycle is "
                        f"{UNDECLARED}")
    if lifecycle in TERMINAL and not data.get("outcome"):
        problems.append(f"lifecycle is terminal ({lifecycle}) but outcome is absent")
    if lifecycle and lifecycle not in TERMINAL and data.get("outcome"):
        problems.append("outcome is set on a task that has not reached a terminal "
                        "lifecycle — it claims a result that has not happened")

    for key in ("created", "updated"):
        value = data.get(key)
        if value is None:
            continue
        text = value.isoformat() if hasattr(value, "isoformat") else str(value)
        if text != "unrecorded" and not STAMP.match(text):
            problems.append(f"{key} is not YYYYMMDD-HHMMSS or 'unrecorded': {text!r}")

    # The identifier must be the one its own directory carries. A state file that names a
    # different task is worse than a missing one: every consumer keys on `id`.
    if task_dir is not None:
        parsed = parse_identifier(task_dir.name)
        if parsed is None:
            problems.append(f"directory name {task_dir.name!r} is not a task identifier")
        elif data.get("id") and str(data["id"]) != parsed[1]:
            problems.append(
                f"id {str(data['id'])!r} disagrees with its directory, which is "
                f"{parsed[1]!r}")

    return problems


PHASE_DIR = re.compile(r"^phase-(?P<letter>[a-z0-9]+)$")


def iter_phase_dirs(task_dir: Path) -> list[Path]:
    """Phase directories inside a task, in declared order.

    A phase carries its own ``status.md`` on the same closed schema, written by that phase's
    owner. Two phases running under two owners are two files, so they never contend.
    """
    return sorted((p for p in task_dir.iterdir() if p.is_dir() and PHASE_DIR.match(p.name)),
                  key=lambda p: p.name)


def read_phase_status(phase_dir: Path, declared: list[str] | None = None) -> dict | None:
    """A phase's own state. Same schema as a task's, minus the directory-identifier check.

    The phase directory is named ``phase-a``, not an identifier, so the ``id`` field carries
    the *task's* identifier and agreement with the directory name is not checked here.
    """
    path = phase_dir / "status.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    if not match:
        return {"_error": "no YAML front matter"}
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return {"_error": explain_yaml_error(match.group(1), exc)}
    if not isinstance(data, dict):
        return {"_error": "front matter is not a mapping"}
    problems = validate_status(data, None, declared)
    if problems:
        data["_error"] = "; ".join(problems)
    return data


# ---------------------------------------------------------------------------
# Journal events
# ---------------------------------------------------------------------------

#: ``<YYYYMMDD-HHMMSS>__<kind>__<token>.md``.
#:
#: **The third component has exactly one job: two writes in one second cannot share a name.**
#: It is not an identity. It names nobody, requires no profile, and is validated against
#: nothing — there is nothing to validate it against, because uniqueness is the whole of what
#: it does.
#:
#: It used to be the `actor` handle, and that is what went wrong: one component was given two
#: unrelated jobs — say who wrote this, and make the name unique — and the two collided in the
#: field. A distinct writer needs a distinct value; a declared handle needs a profile; so two
#: external projects created a profile per session, and one of them later deleted those
#: profiles and left its build gate permanently red. Events are immutable, profiles are not.
#:
#: A pre-`2.0.0-dirty.3` name carries a handle here and matches this pattern unchanged. That
#: is deliberate and it is why the ruling costs no project any work: the two shapes are
#: **syntactically identical**, so nothing has to tell them apart, and nothing does.
EVENT_NAME = re.compile(
    r"^(?P<stamp>\d{8}-\d{6})__(?P<kind>[a-z_]+)__(?P<token>[a-z0-9][a-z0-9-]*)\.md$")

#: The pre-2.0.0 event name, ``<stamp>__<kind>.md``. Events written under it are immutable
#: like every other event: a correction is a new event, never an edit. They are reported as
#: legacy rather than as defects, exactly as a legacy task identifier is.
LEGACY_EVENT_NAME = re.compile(r"^(?P<stamp>\d{8}-\d{6})__(?P<kind>[a-z_]+)\.md$")

#: Closed vocabulary. ``consolidation`` is reserved for Phases B and C and is not yet valid.
EVENT_KINDS = ("created", "dispatch", "handoff", "transition", "ownership_changed",
               "amendment_escalated")
RESERVED_EVENT_KINDS = ("consolidation",)

#: `actor` stays in the accepted set and is absent from the required one. Every event ever
#: written carries it, and an event is never edited — so tolerating it is not a courtesy, it
#: is the only reading that leaves existing corpora valid. It returns as a required field with
#: TFW-54, which is the task that will finally have a writer worth naming.
EVENT_KEYS = {"time", "kind", "actor", "on_behalf_of", "via", "from", "to", "refs", "summary"}
EVENT_REQUIRED = ("time", "kind", "on_behalf_of", "refs")

DEFAULT_SUMMARY_CEILING = 120

#: `PROVIDER_FAMILIES` was deleted here at `2.0.0-dirty.3`. Its only reader was the gate that
#: refused a provider name in `actor`, and with `actor` no longer an identity the gate has no
#: subject. Keeping the set would leave a list nothing reads — and it was never named in any
#: payload prose, so a project met it only by being refused by it.

ISO_TIME = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:[+-]\d{2}:\d{2}|Z)$")


def team_profiles(root: Path) -> dict[str, dict]:
    """Every participant declared in ``team/``, **parsed**, keyed by handle.

    Reading the filename was not enough. Accountability is a claim about a *person*, so the
    rule needs the profile's declared ``type``, and only the file body carries it.

    An empty dict means the project declares nobody — which is a reason to refuse a new
    event, never a reason to skip the check.
    """
    directory = root / "team"
    if not directory.is_dir():
        return {}
    profiles: dict[str, dict] = {}
    for path in sorted(directory.glob("*.md")):
        if path.stem == "README":
            continue
        match = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
        data = {}
        if match:
            try:
                loaded = yaml.safe_load(match.group(1))
                if isinstance(loaded, dict):
                    data = loaded
            except yaml.YAMLError:
                data = {"_error": "unparseable front matter"}
        handle = str(data.get("handle") or path.stem)
        profiles[handle] = data
    return profiles


def team_handles(root: Path) -> set[str]:
    """Declared handles only. Kept for callers that do not need the profile body."""
    return set(team_profiles(root))


def summary_ceiling(root: Path) -> int:
    """The measured entry ceiling this project declares."""
    journal = read_config(root).get("journal") or {}
    try:
        return int(journal.get("max_summary_length", DEFAULT_SUMMARY_CEILING))
    except (TypeError, ValueError):
        return DEFAULT_SUMMARY_CEILING


def read_stamp() -> str:
    """One reading of the system clock, at second resolution."""
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def event_token(entropy=os.urandom) -> str:
    """A short opaque token whose only job is that two names in one second differ.

    Four hex characters. Not an identity: it names nobody, needs no profile, is checked
    against nothing, and carries no meaning a reader could act on. If it ever acquires a
    second job, it is the wrong mechanism — that is the defect this replaced.

    ``entropy`` is injectable so a test can pin the value.
    """
    return entropy(2).hex()


def event_filename(kind: str, token=event_token, taken=(), clock=read_stamp,
                   attempts: int = 64) -> str:
    """The filename for one event: ``<stamp>__<kind>__<token>.md``.

    **The clock is read once, and no second is ever invented.** The previous version read the
    clock again on every collision and waited between readings, because the name's uniqueness
    came from the second and the only thing that could change a second was time passing. It
    is worth stating what that machinery was for, since it is now gone: uniqueness comes from
    the token, so a collision is re-drawn rather than waited out.

    The prohibition it was built to enforce survives intact and is stricter than before:
    nothing here adds to, rounds or composes a stamp. There is one reading, and it is used as
    it was read.

    ``attempts`` bounds the draw so exhausted entropy fails visibly instead of looping.
    """
    taken = set(taken)
    stamp = clock()
    drawn: list[str] = []
    for _ in range(attempts):
        value = token() if callable(token) else str(token)
        drawn.append(value)
        candidate = f"{stamp}__{kind}__{value}.md"
        if candidate not in taken:
            return candidate
    raise ValueError(
        f"drew {attempts} tokens at {stamp} and every name was taken "
        f"({drawn[0]} ... {drawn[-1]}). That is an entropy problem, not a naming problem — "
        "no second is invented and no counter is added to get past it")


def validate_event(data: dict, filename: str, ceiling: int = DEFAULT_SUMMARY_CEILING,
                   profiles: dict[str, dict] | None = None) -> list[str]:
    """Every rule an event declares, checked against one file. Problems, in order.

    ``profiles`` is ``team_profiles(root)`` — the parsed participants. **An empty dict is a
    refusal, not a skip**: if the project declares nobody, a new event has nobody who answers
    for it, and that is precisely the case the rule exists to catch. Passing ``None`` means
    the caller is checking something else and has opted out; every production path supplies
    the dict.
    """
    problems: list[str] = []

    name = EVENT_NAME.match(filename)
    legacy = name is None and LEGACY_EVENT_NAME.match(filename) is not None
    if not name and not legacy:
        problems.append(
            f"filename {filename!r} is not <YYYYMMDD-HHMMSS>__<kind>__<token>.md")

    unknown = sorted(set(data) - EVENT_KEYS)
    if unknown:
        problems.append("unknown keys: " + ", ".join(unknown))

    # A legacy event predates `on_behalf_of` and the three-part filename. Demanding either
    # would demand an edit, and an event is never edited.
    required = EVENT_REQUIRED if not legacy else tuple(
        k for k in EVENT_REQUIRED if k != "on_behalf_of")
    for key in required:
        if not data.get(key):
            problems.append(f"missing {key}")

    kind = data.get("kind")
    if kind in RESERVED_EVENT_KINDS:
        problems.append(f"kind '{kind}' is reserved for a later phase and is not yet valid")
    elif kind and kind not in EVENT_KINDS:
        problems.append(f"kind '{kind}' is outside the closed vocabulary")

    if name and kind and name.group("kind") != kind:
        problems.append(f"filename says kind '{name.group('kind')}', body says '{kind}'")
    # THE FILENAME IS NOT COMPARED TO `actor`, and there is nothing left to compare. The
    # third component is a uniqueness token, not an identity, so it agrees with no field by
    # design. The old check existed because the name carried a handle; the name no longer
    # carries one, so the check has no subject rather than a relaxed one.
    #
    # `actor` ITSELF IS NOT VALIDATED AT ALL: not against `team/`, not against a provider
    # list, not for shape. Every event in every existing corpus carries it, events are
    # immutable, and profiles are not — so any rule about it would either demand an edit or
    # go red when a project tidies `team/`. One consumer's gate is red today for exactly
    # that reason. Tolerated, never required, never rewritten.

    on_behalf_of = data.get("on_behalf_of")

    # The legacy escape is scoped to events identifiable as pre-rule by their own filename
    # shape — a durable property of the event itself, not a convenience for the caller.
    if profiles is not None and not legacy:
        declared = set(profiles)
        if on_behalf_of:
            profile = profiles.get(str(on_behalf_of))
            if profile is None:
                problems.append(
                    f"on_behalf_of '{on_behalf_of}' is not a declared team/ participant "
                    f"({', '.join(sorted(declared)) if declared else 'team/ declares nobody'})")
            elif str(profile.get("type", "")).strip() != "human":
                problems.append(
                    f"on_behalf_of '{on_behalf_of}' is declared as "
                    f"'{profile.get('type') or 'no type'}', not human — accountability "
                    "always resolves to a person")

    time_value = data.get("time")
    if time_value is not None:
        text = time_value.isoformat() if hasattr(time_value, "isoformat") else str(time_value)
        if not ISO_TIME.match(text):
            problems.append(f"time is not ISO 8601 with an offset: {text!r}")

    refs = data.get("refs")
    if refs is not None and (not isinstance(refs, list) or not refs):
        problems.append("refs must be a non-empty list of paths")

    summary = data.get("summary")
    if isinstance(summary, str) and len(summary) > ceiling:
        problems.append(
            f"summary is {len(summary)} code points, ceiling is {ceiling}; "
            "move the content into an artifact and reference it from the event")

    has_from, has_to = data.get("from") is not None, data.get("to") is not None
    if has_from != has_to:
        problems.append("a state change needs both 'from' and 'to', or neither")

    return problems


def journal_dirs(task_dir: Path) -> list[Path]:
    """Every journal a task holds: its own, and one per phase directory.

    A phase carries its own `journal/` exactly as it carries its own `status.md` — the
    symmetry an external project assumed, correctly, before it was implemented. Two of that
    project's four malformed events sat in `phase-a/journal/` where nothing looked, so the
    gate reported clean over them.
    """
    found = [task_dir / "journal"]
    found += [phase / "journal" for phase in iter_phase_dirs(task_dir)]
    return [d for d in found if d.is_dir()]


def read_journal(task_dir: Path, ceiling: int = DEFAULT_SUMMARY_CEILING,
                 profiles: dict[str, dict] | None = None
                 ) -> tuple[list[dict], list[str]]:
    """Every event in a task's journals, and every problem found. Nothing is dropped.

    **Every journal**, task-level and per-phase. Reading only the task's own was how a
    consumer's malformed phase events stayed invisible to a gate that reported success.

    Events written before the 2.0.0 grammar are counted and reported once, not corrected:
    the journal is immutable, so a rule introduced later can describe old entries but never
    rewrite them.
    """
    journals = journal_dirs(task_dir)
    if not journals:
        return [], []
    events, problems = [], []
    legacy = 0
    for journal in journals:
        # A phase event is reported by `phase-a/journal/<name>.md`, not by `<name>.md` alone:
        # two phases can hold the same event name, and a bare name would make one report
        # answer for a file the reader cannot find.
        prefix = "" if journal.parent == task_dir else f"{journal.parent.name}/journal/"
        for path in sorted(journal.glob("*.md"), key=lambda p: p.name):
            label = prefix + path.name
            text = path.read_text(encoding="utf-8")
            match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
            if not match:
                problems.append(f"{label}: no YAML front matter")
                continue
            try:
                data = yaml.safe_load(match.group(1))
            except yaml.YAMLError as exc:
                problems.append(f"{label}: unparseable ({exc.__class__.__name__})")
                continue
            if not isinstance(data, dict):
                problems.append(f"{label}: front matter is not a mapping")
                continue
            if EVENT_NAME.match(path.name) is None and LEGACY_EVENT_NAME.match(path.name):
                legacy += 1
            for problem in validate_event(data, path.name, ceiling, profiles):
                problems.append(f"{label}: {problem}")
            data["_file"] = label
            events.append(data)
    if legacy:
        problems.insert(0, f"{legacy} event(s) predate the 2.0.0 event grammar; immutable "
                            "by rule, so they are recorded as legacy rather than corrected")
    return events, problems


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


#: Snapshot classes this index knowingly renders. Anything else is reported as unresolved
#: rather than skipped: a class nobody renders disappears, and disappearing is the failure
#: this whole report exists to prevent.
RENDERED_SNAPSHOT_CLASSES = frozenset({
    "matched",
    "plain-text row, directory exists",
    "absorbed elsewhere, directory retained",
    "board-only, backlog",
    "board-only, absorbed elsewhere",
    "board-only, directory unresolved",
})


def snapshot_row_for_name(directory_name: str, rows: list[dict]) -> dict | None:
    """The snapshot row naming a directory whose own name the grammar does not parse.

    Matching is on the observable prefix and nothing else: a row identifier is accepted
    when the directory name is exactly it, or begins with it followed by a separator. That
    is deliberately weak — the point is only to say *a row names this directory*, never to
    reconstruct an identifier the grammar rejected.
    """
    best: dict | None = None
    for row in rows:
        identifier = row.get("id") or ""
        if not identifier or identifier == "(none)":
            continue
        if directory_name == identifier or directory_name.startswith(identifier + "_"):
            # Longest identifier wins, so `TFW-1` never claims `TFW-10_...`.
            if best is None or len(identifier) > len(best["id"]):
                best = row
    return best


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
    declared = declared_lifecycles(root)
    ceiling = summary_ceiling(root)
    profiles = team_profiles(root)
    base = output_path(root).parent
    snapshot = read_snapshot(root)
    by_id = snapshot_index(snapshot)

    live: list[dict] = []
    historical: list[dict] = []
    unresolved: list[dict] = []

    task_dirs, unmatched = _walk_containers(root, containers)

    # A directory the identifier grammar does not match is reported here and nowhere else.
    # It is NOT a backlog idea: the corpus that produced this rule held completed traces in
    # two such directories. The reason states what is observable — the name, and whether a
    # snapshot row points at it — and nothing about whether work happened, because that is
    # all this consumer knows.
    covered_by_directory: set[str] = set()
    for path in unmatched:
        row = snapshot_row_for_name(path.name, snapshot)
        if row:
            covered_by_directory.add(row["id"])
        names_it = f" Board row `{row['id']}` names it." if row else ""
        unresolved.append({
            "path": _link(root, base, path),
            "id": row["id"] if row else path.name,
            "reason": "directory name matches neither identifier grammar — not clock "
                      "`YYYYMMDD-HHMMSS__slug`, not legacy `PREFIX-N` optionally followed "
                      f"by `__slug`.{names_it} Nothing further is asserted about it: rename "
                      "it by hand to the recognized grammar to have it picked up",
        })

    # Every snapshot class this file knowingly renders. A class outside the set is reported
    # rather than skipped — the silent skip is what let two rows be rendered under a heading
    # that described them falsely, and a class nobody renders is the same defect inverted.
    for row in snapshot:
        if row["class"] in RENDERED_SNAPSHOT_CLASSES or row["id"] in covered_by_directory:
            continue
        unresolved.append({
            "path": "tasks/BOARD-SNAPSHOT.md", "id": row["id"],
            "reason": f"snapshot row class `{row['class']}` is not one this index renders"})

    for task_dir in task_dirs:
        rel = _link(root, base, task_dir)
        parsed = parse_identifier(task_dir.name)
        status = read_status(task_dir, declared)
        if status is not None and not status.get("_error"):
            status["_path"] = rel
            status["_kind"] = parsed[0]
            status["_key"] = sort_key(*parsed)
            phases = []
            for phase_dir in iter_phase_dirs(task_dir):
                phase = read_phase_status(phase_dir, declared)
                if phase is None:
                    continue
                if phase.get("_error"):
                    unresolved.append({
                        "path": f"{rel}/{phase_dir.name}", "id": parsed[1],
                        "reason": f"{phase_dir.name}/status.md: {phase['_error']}"})
                    continue
                phase["_name"] = phase_dir.name
                phase["_path"] = f"{rel}/{phase_dir.name}"
                phases.append(phase)
            status["_phases"] = phases
            live.append(status)
            # The journal is not rendered here — it is a task's own record, not portfolio
            # information. But a malformed event must not become invisible just because the
            # index has no column for it, so its problems join the unresolved report.
            _, journal_problems = read_journal(task_dir, ceiling, profiles)
            for problem in journal_problems:
                unresolved.append({"path": f"{rel}/journal", "id": parsed[1],
                                   "reason": problem})
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
        "generator": _self_path(root),
    }


def render(data: dict) -> str:
    live = data["live"]
    historical = data["historical"]
    backlog = data["backlog"]
    absorbed = data["absorbed"]
    unresolved = data["unresolved"]
    snapshot = data["snapshot"]
    # The generator names ITSELF by where it actually is, not by a literal. A project
    # that placed the tools elsewhere gets an index naming a command it can run.
    generator = data["generator"]
    out: list[str] = []
    add = out.append

    add("# Portfolio index")
    add("")
    add("> **This file is derived and non-authoritative.** It is rebuilt from every task's")
    add(f"> own `status.md` by `{generator}`. When it disagrees with a task,")
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
    add(f"| Generator | `python {generator}` |")
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
            # Phase rows sit beneath their task, which is what the retired board's
            # per-phase columns showed. Each is read from that phase's own file — the task
            # row never summarizes them, because a rollup is a second fact to keep in sync.
            for phase in item.get("_phases") or []:
                phase_life = str(phase.get("lifecycle"))
                if phase_life == "UNDECLARED" and phase.get("lifecycle_verbatim"):
                    phase_life = f"UNDECLARED (`{_cell(phase['lifecycle_verbatim'])}`)"
                letter = phase["_name"].replace("phase-", "").upper()
                add(
                    f"| &nbsp;&nbsp;↳ [{letter} — {_cell(phase.get('title'))}]"
                    f"({phase['_path']}/status.md) | {phase_life} "
                    f"| {_cell(phase.get('owner'))} | {_cell(phase.get('goal'))} | — |"
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
    add(f"*Generated by `{generator}`. Do not edit: every change is lost on")
    add("the next run, and the authority it would contradict lives in the task folders.*")
    return NEWLINE.join(out) + NEWLINE


def build(root: Path) -> str:
    return render(collect(root))


def output_path(root: Path) -> Path:
    return root / task_containers(root)[0] / "00-INDEX.md"


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------
#
# Three questions about three subjects, behind one flag with a subject argument.
#
# There were previously two flags, `--check` and `--validate`, and
# `project_config.yaml` carried a five-line comment explaining which one the build gate
# wanted and why the other would have been wrong. A third synonym was proposed and
# rejected: when prose is required to tell your own names apart, the names are wrong, and
# the comment was the symptom rather than the fix.
#
# Every subject REPORTS AND EXITS. None of them writes, repairs or decides. The moment a
# check writes, it becomes a second authority over task state, which the model forbids.
# Each names what it did not check, because a check's silence is otherwise read as an
# answer it never gave.


def check_index(root: Path) -> int:
    """Is the derived index current?

    A deliberate freshness question. Never a gate on a task transition: that would make
    rebuilding a shared file a precondition for advancing one task, which is the single
    shared write the task-local model removed.
    """
    target = output_path(root)
    rel = target.relative_to(root).as_posix()
    current = target.read_text(encoding="utf-8") if target.exists() else None
    if current == build(root):
        print(f"index up to date: {rel}")
        print("not checked: whether task state is legal (--check tasks), "
              "whether the project matches the release (--check project)")
        return 0
    print(f"index is stale: {rel}", file=sys.stderr)
    print(f"  rebuild it deliberately: python {_self_path(root)}", file=sys.stderr)
    return 1


def check_tasks(root: Path) -> int:
    """Is each task's own state legal against the closed schema?

    This is the build gate. It reads task-local truth only, so it is unaffected by whether
    the derived index happens to be current — and it must stay that way: a gate that also
    demanded a fresh index would reintroduce the shared write.
    """
    declared = declared_lifecycles(root)
    ceiling = summary_ceiling(root)
    profiles = team_profiles(root)
    task_dirs = iter_task_dirs(root)
    failures = 0
    for task_dir in task_dirs:
        rel = task_dir.relative_to(root).as_posix()
        status = read_status(task_dir, declared)
        if status is not None and status.get("_error"):
            print(f"{rel}/status.md: {status['_error']}", file=sys.stderr)
            failures += 1
        for phase_dir in iter_phase_dirs(task_dir):
            phase = read_phase_status(phase_dir, declared)
            if phase is not None and phase.get("_error"):
                print(f"{rel}/{phase_dir.name}/status.md: {phase['_error']}",
                      file=sys.stderr)
                failures += 1
        _, journal_problems = read_journal(task_dir, ceiling, profiles)
        for problem in journal_problems:
            if "predate the 2.0.0 event grammar" in problem:
                continue  # immutable by rule; reported in the index, not a failure
            print(f"{rel}/journal/{problem}", file=sys.stderr)
            failures += 1
    if failures:
        print(f"{failures} problem(s) across {len(task_dirs)} tasks", file=sys.stderr)
        return 1
    print(f"{len(task_dirs)} tasks validate against the closed schema")
    print("not checked: index freshness -- this gate deliberately does not answer it "
          "(--check index), project consistency (--check project)")
    return 0


def check_project(root: Path) -> int:
    """Is this project consistent with the release it declares?

    The question a project has after an update, which previously had no command behind it:
    the best signal available to the first external consumer was two framework tests it was
    never told to run.

    Reports and exits. It repairs nothing, writes nothing, and is not authority over
    anything — where it disagrees with a task's own ``status.md``, the task is right.
    """
    problems: list[str] = []
    notes: list[str] = []
    config = read_config(root)

    # 1. Payload — the files the rules require a project to have.
    here = Path(__file__).resolve().parent
    for name in ("gen_index.py", "migrate_board.py"):
        if not (here / name).is_file():
            problems.append(f"payload: {name} is missing from {here}")
    version_file = root / ROOT_MARKER / "VERSION"
    if not version_file.is_file():
        problems.append(f"payload: {ROOT_MARKER}/VERSION is missing")
    else:
        shipped = version_file.read_text(encoding="utf-8").strip()
        declared_version = str(config.get("version") or "").strip()
        if declared_version and declared_version != shipped:
            problems.append(f"version: project_config.yaml says {declared_version!r}, "
                            f"{ROOT_MARKER}/VERSION says {shipped!r}")
        notes.append(f"framework version {shipped}")

    # 2. team/ — declared attribution. Absent, no event can name an accountable person.
    profiles = team_profiles(root)
    if not (root / "team").is_dir():
        problems.append("team/: the directory does not exist. Create it with its first "
                        "profile before the first durable write")
    elif not profiles:
        problems.append("team/: exists but declares nobody. A journal event's "
                        "on_behalf_of has no valid value")
    elif not any((p.get("type") or "") == "human" for p in profiles.values()):
        problems.append("team/: no profile declares type: human. on_behalf_of must always "
                        "name a human, so no event can be written")
    else:
        notes.append(f"{len(profiles)} participant(s) declared")

    # 3. Container configuration.
    containers = task_containers(root)
    if not containers:
        problems.append("task_containers: empty. Nothing can be created or resolved")
    else:
        if not (root / containers[0]).is_dir():
            problems.append(f"task_containers: the creation container "
                            f"{containers[0]!r} does not exist as a directory")
        missing = [c for c in containers[1:] if not (root / c).is_dir()]
        if missing:
            notes.append("resolution container(s) not present: " + ", ".join(missing))
        notes.append(f"creates in {containers[0]!r}, resolves across {containers}")

    # 4. Retired keys.
    for retired, why in (("initial_seq", "identifiers are clock-derived; nothing reads a "
                                        "counter"),):
        if retired in config:
            problems.append(f"retired key: tfw.{retired} is still present — {why}. Remove it")

    # 5. Build commands naming paths that exist.
    #
    # `build.*` is a PROJECT section, which `update.md` preserves rather than overwrites —
    # so a project that updates across a release that moved a tool keeps a command naming
    # a path that is gone, permanently and silently. This check is the only thing that
    # says so.
    for key, command in (read_yaml_block(root, "build") or {}).items():
        for token in str(command).split():
            if "/" in token and token.endswith(".py") and not (root / token).exists():
                problems.append(f"build.{key}: names {token}, which does not exist")

    # 6. Carrier validity — counted here, detailed by `--check tasks`.
    declared = declared_lifecycles(root)
    malformed = [d for d in iter_task_dirs(root)
                 if (read_status(d, declared) or {}).get("_error")]
    if malformed:
        problems.append(f"{len(malformed)} task(s) carry malformed state. "
                        f"Run --check tasks for the detail")

    for note in notes:
        print(f"  - {note}")
    if problems:
        print(f"{len(problems)} problem(s):", file=sys.stderr)
        for problem in problems:
            print(f"  ! {problem}", file=sys.stderr)
        return 1
    print("project is consistent with the release it declares")
    print("not checked: index freshness (--check index), the detail of each task's state "
          "(--check tasks), adapter copies against their sources, Git state, and anything "
          "inside an artifact. This reads structure, not content")
    return 0


def read_yaml_block(root: Path, block: str) -> dict:
    """A top-level block of ``project_config.yaml``. ``read_config`` returns ``tfw`` only."""
    path = root / ROOT_MARKER / "project_config.yaml"
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as handle:
        return (yaml.safe_load(handle) or {}).get(block) or {}


def _self_path(root: Path) -> str:
    """This script, named the way a person would type it from the project root."""
    try:
        return Path(__file__).resolve().relative_to(root).as_posix()
    except ValueError:
        return Path(__file__).resolve().as_posix()


CHECKS = {"index": check_index, "tasks": check_tasks, "project": check_project}


def main(argv: list[str] | None = None) -> int:
    make_streams_printable()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=None,
                       help="the project root. Default: found by walking upward from this "
                            "script for a .tfw/ directory, so the tools work wherever a "
                            "project places them")
    parser.add_argument("--check", choices=sorted(CHECKS), metavar="SUBJECT",
                        help="write nothing; report on one subject and exit. "
                             "index — is the derived index current? "
                             "tasks — is each task's own state legal? (the build gate) "
                             "project — is this project consistent with the release?")
    args = parser.parse_args(argv)

    root = (args.root or find_project_root()).resolve()
    print(f"project root: {root}", file=sys.stderr)

    if args.check:
        return CHECKS[args.check](root)

    content = build(root)
    target = output_path(root)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrote {target.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
