from __future__ import annotations

import os
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

import yaml

ROOT_MARKER = ".tfw"

STAGING_SEGMENT = ".upstream"


def find_project_root(start: Path | None = None) -> Path:
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


CLOCK_ID = re.compile(r"^(?P<stamp>\d{8}-\d{6})__(?P<slug>.+)$")

CURRENT_ID = re.compile(
    r"^(?P<prefix>[A-Z][A-Z0-9]*)_(?P<stamp>\d{8}-\d{6})_(?P<abbr>[A-Z0-9]+)$"
)

BARE_STAMP = re.compile(r"^\d{8}-\d{6}$")

LEGACY_ID = re.compile(r"^(?P<prefix>[A-Z][A-Z0-9]*)-(?P<seq>\d+)(?:__(?P<slug>.+))?$")


class IdentifierCollisionError(ValueError):
    pass

NEWLINE = chr(10)

FRONT_MATTER = re.compile("^---" + chr(92) + "r?" + chr(92) + "n(.*?)" + chr(92) + "r?" + chr(92) + "n---" + chr(92) + "r?" + chr(92) + "n", re.S)

DEFAULT_CONTAINERS = ["workspace"]

TERMINAL = {"DONE", "REJECTED"}

COMMON_COORDINATION_KEYS = {
    "coordinator_route", "dialogue", "activation", "coordination_authority",
}
UPWARD_ROUTE_KEYS = {"upstream_route", "owner_gateway"}
COORDINATION_KEYS = COMMON_COORDINATION_KEYS | UPWARD_ROUTE_KEYS

SELECTION_KEYS = {"reporting", "selection_ref"}

STATUS_KEYS = {
    "id", "title", "goal", "value", "lifecycle", "lifecycle_verbatim",
    "owner", "authority", "outcome", "created", "updated", *COORDINATION_KEYS,
    *SELECTION_KEYS,
}

REQUIRED_KEYS = ("id", "title", "goal", "value", "lifecycle", "owner", "authority",
                 "created", "updated")

DECLARED_LIFECYCLES = ("TODO", "HL_DRAFT", "RES", "PHASES", "TS_DRAFT", "ONB", "RF", "REV",
                       "KNW", "DONE", "BLOCKED", "REJECTED")

FORWARD_TRANSITIONS = {
    ("TODO", "HL_DRAFT"),
    ("HL_DRAFT", "RES"), ("HL_DRAFT", "TS_DRAFT"), ("HL_DRAFT", "PHASES"),
    ("RES", "TS_DRAFT"), ("RES", "PHASES"),
    ("PHASES", "KNW"),
    ("TS_DRAFT", "ONB"),
    ("ONB", "RF"),
    ("RF", "REV"), ("RF", "KNW"), ("RF", "ONB"), ("RF", "TS_DRAFT"),
    ("REV", "KNW"), ("REV", "RF"), ("REV", "ONB"), ("REV", "TS_DRAFT"),
    ("KNW", "DONE"),
}

UNDECLARED = "UNDECLARED"

STAMP = re.compile(r"^\d{8}-\d{6}$")

ZERO_TIME = "000000"


def explain_yaml_error(block: str, exc: yaml.YAMLError) -> str:
    detail = getattr(exc, "problem", None) or exc.__class__.__name__
    mark = getattr(exc, "problem_mark", None) or getattr(exc, "context_mark", None)
    if mark is not None:
        line_number = mark.line
    elif hasattr(exc, "position"):
        line_number = block.count("\n", 0, exc.position)
    else:
        return f"unparseable front matter: {detail}"

    lines = block.splitlines()
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
        hint = (". A value containing \": \" ends a YAML plain scalar, so quote it: "
                f"{key}: \"...\"")
    return f"unparseable front matter: key `{key}` ({where}): {detail}{hint}"


def parse_identifier(text: str) -> tuple[str, str] | None:
    text = text.strip()
    if CURRENT_ID.fullmatch(text):
        return ("current", text)
    if CLOCK_ID.match(text):
        return ("clock", text)
    match = LEGACY_ID.match(text)
    if match:
        return ("legacy", f"{match.group('prefix')}-{match.group('seq')}")
    return None


def sort_key(kind: str, identifier: str) -> tuple:
    if kind == "legacy":
        m = LEGACY_ID.match(identifier)
        return (0, m.group("prefix"), int(m.group("seq")), "")
    if kind == "clock":
        m = CLOCK_ID.match(identifier)
        return (1, m.group("stamp"), m.group("slug"), "")
    m = CURRENT_ID.match(identifier)
    return (2, m.group("stamp"), m.group("prefix"), m.group("abbr"))


def read_config(root: Path) -> dict:
    path = root / ".tfw" / "project_config.yaml"
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as handle:
        return (yaml.safe_load(handle) or {}).get("tfw", {}) or {}


def task_containers(root: Path) -> list[str]:
    value = read_config(root).get("task_containers") or DEFAULT_CONTAINERS
    if isinstance(value, str):
        value = [value]
    return [str(item).strip("/") for item in value]


def reference_containers(root: Path) -> list[str]:
    history = read_config(root).get("historical_containers", [])
    if not isinstance(history, list):
        raise ValueError("tfw.historical_containers must be a list of relative directory paths")
    for item in history:
        if (not isinstance(item, str) or not item.strip() or "\\" in item
                or Path(item).is_absolute() or ":" in item
                or ".." in Path(item).parts or not Path(item).parts
                or not (root / item).resolve().is_relative_to(root.resolve())):
            raise ValueError(f"invalid historical container path: {item!r}")
    result, seen = [], set()
    for item in [*task_containers(root), *history]:
        resolved = (root / item).resolve()
        if resolved not in seen:
            seen.add(resolved)
            result.append(item)
    return result


def _walk_containers(root: Path, containers: list[str] | None = None
                     ) -> tuple[list[Path], list[Path]]:
    if containers is None:
        containers = task_containers(root)
    found: list[tuple[tuple, Path]] = []
    unmatched: list[Path] = []
    seen: set[Path] = set()
    for container in containers:
        base = root / container
        if not base.is_dir():
            continue
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
    by_identifier: dict[str, list[Path]] = {}
    for _, path in found:
        identifier = parse_identifier(path.name)[1]
        by_identifier.setdefault(identifier, []).append(path)
    collisions = {identifier: paths for identifier, paths in by_identifier.items()
                  if len(paths) > 1}
    if collisions:
        details = []
        for identifier, paths in sorted(collisions.items()):
            names = ", ".join(
                path.relative_to(root).as_posix() for path in sorted(paths, key=str))
            details.append(f"{identifier}: {names}")
        raise IdentifierCollisionError(
            "task directory identifier collision; each identifier must resolve exactly once: "
            + "; ".join(details)
        )

    found.sort(key=lambda pair: (pair[0], str(pair[1])))
    unmatched.sort(key=lambda path: str(path))
    return [path for _, path in found], unmatched


def iter_task_dirs(root: Path, containers: list[str] | None = None) -> list[Path]:
    return _walk_containers(root, containers)[0]


def iter_unmatched_task_dirs(root: Path, containers: list[str] | None = None) -> list[Path]:
    return _walk_containers(root, containers)[1]


def declared_lifecycles(root: Path) -> list[str]:
    entries = read_config(root).get("statuses") or []
    ids = [str(e.get("id")) for e in entries if isinstance(e, dict) and e.get("id")]
    return ids or list(DECLARED_LIFECYCLES)


def read_status(task_dir: Path, declared: list[str] | None = None) -> dict | None:
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
    declared = declared or list(DECLARED_LIFECYCLES)
    problems: list[str] = []

    unknown = sorted(set(data) - STATUS_KEYS)
    if unknown:
        problems.append("unknown keys: " + ", ".join(unknown))

    for key in REQUIRED_KEYS:
        if not data.get(key):
            problems.append(f"missing {key}")

    lifecycle = data.get("lifecycle")
    if lifecycle and lifecycle != UNDECLARED and lifecycle not in declared:
        problems.append(
            f"lifecycle '{lifecycle}' is not declared and is not {UNDECLARED}; "
            "an out-of-vocabulary value must be carried as "
            f"{UNDECLARED} plus lifecycle_verbatim, never normalized")

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

    coordination_present = COORDINATION_KEYS.intersection(data)
    selection_present = SELECTION_KEYS.intersection(data)
    if selection_present and selection_present != SELECTION_KEYS:
        problems.append("partial current selection; reporting and selection_ref must occur together")
    route_names = coordination_present & UPWARD_ROUTE_KEYS
    missing_common = COMMON_COORDINATION_KEYS - coordination_present
    if coordination_present and (missing_common or len(route_names) != 1):
        missing = sorted(missing_common)
        if not route_names:
            missing.append("upstream_route or owner_gateway")
        if missing:
            problems.append("partial coordination routing spine; missing: " + ", ".join(missing))
        if len(route_names) == 2:
            problems.append("both upward route names are present")
    if selection_present and (not coordination_present or missing_common or len(route_names) != 1):
        problems.append("current selection requires the complete routing spine")
    if "upstream_route" in route_names and selection_present != SELECTION_KEYS:
        problems.append("new upstream_route requires reporting and selection_ref")
    if coordination_present and not missing_common and len(route_names) == 1:
        route = data.get("coordinator_route")
        if not isinstance(route, str) or not route.strip():
            problems.append("coordinator_route must be a non-empty native address string")
        if "owner_gateway" in route_names:
            gateway = data.get("owner_gateway")
            if not isinstance(gateway, str) or not re.fullmatch(
                    r"(?:owner:[a-z0-9][a-z0-9-]*|gateway:\S+)", gateway):
                problems.append("owner_gateway must be owner:{human} or gateway:{native}")
        else:
            upward = data.get("upstream_route")
            is_phase = task_dir is not None and PHASE_DIR.fullmatch(task_dir.name) is not None
            if not isinstance(upward, str):
                problems.append("upstream_route must be a string")
            elif is_phase:
                parent = read_status(task_dir.parent, declared)
                if not upward.startswith("coordinator:") or not upward[len("coordinator:"):].strip():
                    problems.append("phase upstream_route must be coordinator:{native address}")
                elif not parent or parent.get("_error") or not parent.get("coordinator_route"):
                    problems.append("phase upstream_route has no valid governing task Coordinator")
                elif upward[len("coordinator:"):] != parent["coordinator_route"]:
                    problems.append("phase upstream_route disagrees with governing task Coordinator")
                if isinstance(route, str) and upward == "coordinator:" + route:
                    problems.append("phase upward route cannot name its own Coordinator")
            elif not re.fullmatch(r"owner:[a-z0-9][a-z0-9-]*", upward) or upward != "owner:" + str(data.get("owner")):
                problems.append("task upstream_route must name its human owner")
        dialogue = data.get("dialogue")
        if dialogue not in {"tfw-gates-only", "iterative"}:
            problems.append("dialogue must be tfw-gates-only or iterative")
        activation = data.get("activation")
        if not isinstance(activation, str) or not (
                activation == "owner-only" or
                (activation.startswith("delegated:") and activation != "delegated:")):
            problems.append("activation must be owner-only or delegated:{immutable mandate ref}")
        authority = data.get("coordination_authority")
        if not isinstance(authority, str) or not re.fullmatch(
                r"\S(?:.*\S)? @ [0-9a-f]{40}", authority):
            problems.append(
                "coordination_authority must contain an exact local reference and full Git epoch")

    if selection_present == SELECTION_KEYS:
        if data.get("reporting") not in {"native-gates", "owner-transfer"}:
            problems.append("reporting must be native-gates or owner-transfer")
        selection_ref = data.get("selection_ref")
        if selection_ref == "baseline" and task_dir is not None:
            problems.extend(verify_baseline_source(data, task_dir))
        elif selection_ref != "baseline":
            match = re.fullmatch(
                r"(?P<path>(?:\.\./)?journal/[0-9]{8}-[0-9]{6}__coordination_selected__[0-9a-f]{4}\.md) @ (?P<sha>[0-9a-f]{40})",
                selection_ref if isinstance(selection_ref, str) else "")
            if not match:
                problems.append("selection_ref must be baseline or an exact coordination_selected journal path @ full commit")
            elif task_dir is not None:
                ancestor = match.group("path").startswith("../")
                is_phase = PHASE_DIR.fullmatch(task_dir.name) is not None
                if ancestor and not is_phase:
                    problems.append("ancestor selection_ref is allowed only from a phase")
                elif ancestor and not (task_dir.parent / "status.md").is_file():
                    problems.append("ancestor selection_ref requires the governing task status")
                elif not (task_dir / match.group("path")).is_file():
                    problems.append("selection_ref event is missing at its scoped path")
                else:
                    problems.extend(verify_selection_source(data, task_dir, match.group("path"),
                                                            match.group("sha")))

    for key in ("created", "updated"):
        value = data.get(key)
        if value is None:
            continue
        text = value.isoformat() if hasattr(value, "isoformat") else str(value)
        if text != "unrecorded" and not STAMP.match(text):
            problems.append(f"{key} is not YYYYMMDD-HHMMSS or 'unrecorded': {text!r}")

    if task_dir is not None:
        is_phase = PHASE_DIR.fullmatch(task_dir.name) is not None
        parsed = parse_identifier(task_dir.parent.name if is_phase else task_dir.name)
        if parsed is None:
            problems.append(f"governing directory for {task_dir.name!r} is not a task identifier")
        elif data.get("id") and str(data["id"]) != parsed[1]:
            problems.append(
                f"id {str(data['id'])!r} disagrees with its directory, which is "
                f"{parsed[1]!r}")

    return problems


def validate_new_status(data: dict, task_dir: Path | None = None,
                        declared: list[str] | None = None) -> list[str]:
    problems = validate_status(data, task_dir, declared)
    missing = sorted((COMMON_COORDINATION_KEYS | {"upstream_route"}) - set(data))
    if missing:
        problems.append("new status is missing coordination routing fields: " + ", ".join(missing))
    if "owner_gateway" in data:
        problems.append("new status must not issue historical owner_gateway")
    missing_selection = sorted(SELECTION_KEYS - set(data))
    if missing_selection:
        problems.append("new status is missing current selection fields: " + ", ".join(missing_selection))
    return problems


def verify_baseline_source(data: dict, task_dir: Path) -> list[str]:
    authority = data.get("coordination_authority")
    if not isinstance(authority, str) or " @ " not in authority:
        return ["baseline coordination_authority is missing"]
    path_text, commit = authority.rsplit(" @ ", 1)
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        return ["baseline immutable epoch is invalid"]
    authority_path = (task_dir / path_text).resolve()
    if not authority_path.is_file():
        return ["baseline authority artifact is unavailable"]
    try:
        root = find_project_root(task_dir)
        relative = authority_path.relative_to(root).as_posix()
        source = subprocess.run(["git", "show", f"{commit}:{relative}"], cwd=root,
                                capture_output=True, check=False)
    except (OSError, SystemExit, ValueError):
        return ["baseline authority object cannot be inspected"]
    if source.returncode or not source.stdout.startswith(b"# HL"):
        return ["baseline authority object/path is missing or mismatched"]
    return []


def verify_selection_source(data: dict, task_dir: Path, event_ref: str,
                            commit: str) -> list[str]:
    event_path = (task_dir / event_ref).resolve()
    if not event_path.is_file():
        return ["selection_ref event is missing"]
    try:
        root = find_project_root(task_dir)
        relative = event_path.relative_to(root).as_posix()
    except (SystemExit, ValueError):
        return ["selection_ref event escapes the project or project root is unavailable"]
    try:
        kind = subprocess.run(["git", "cat-file", "-t", commit], cwd=root,
                              capture_output=True, check=False)
    except OSError:
        return ["selection_ref commit inspection is unavailable"]
    if kind.returncode or kind.stdout.strip() != b"commit":
        return ["selection_ref commit object is unavailable"]
    try:
        source = subprocess.run(["git", "show", f"{commit}:{relative}"], cwd=root,
                                capture_output=True, check=False)
    except OSError:
        return ["selection_ref event inspection is unavailable"]
    committed_bytes = source.stdout.replace(b"\r\n", b"\n")
    current_bytes = event_path.read_bytes().replace(b"\r\n", b"\n")
    if source.returncode or committed_bytes != current_bytes:
        return ["selection_ref event bytes do not match the immutable commit"]
    try:
        event_text = source.stdout.decode("utf-8")
    except UnicodeDecodeError:
        return ["selection_ref event is not UTF-8"]
    match = FRONT_MATTER.match(event_text)
    if not match:
        return ["selection_ref event has no valid front matter"]
    try:
        event = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return ["selection_ref event front matter is invalid"]
    if not isinstance(event, dict) or event.get("kind") != "coordination_selected":
        return ["selection_ref object is not a coordination_selected event"]
    envelope_problems = validate_new_event(event, event_path.name)
    if envelope_problems:
        return ["selection_ref event envelope is invalid: " + "; ".join(envelope_problems)]
    if event.get("on_behalf_of") != data.get("owner"):
        return ["selection_ref event owner does not match status owner"]
    return []


PHASE_DIR = re.compile(r"^phase-(?P<letter>[a-z0-9]+)$")


def iter_phase_dirs(task_dir: Path) -> list[Path]:
    return sorted((p for p in task_dir.iterdir() if p.is_dir() and PHASE_DIR.match(p.name)),
                  key=lambda p: p.name)


def read_phase_status(phase_dir: Path, declared: list[str] | None = None) -> dict | None:
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
    problems = validate_status(data, phase_dir, declared)
    if problems:
        data["_error"] = "; ".join(problems)
    return data


EVENT_NAME = re.compile(
    r"^(?P<stamp>\d{8}-\d{6})__(?P<kind>[a-z_]+)__(?P<token>[a-z0-9][a-z0-9-]*)\.md$")

LEGACY_EVENT_NAME = re.compile(r"^(?P<stamp>\d{8}-\d{6})__(?P<kind>[a-z_]+)\.md$")

EVENT_KINDS = ("created", "dispatch", "handoff", "transition", "ownership_changed",
               "amendment_escalated", "gate_answer", "coordination_selected")
RESERVED_EVENT_KINDS = ("consolidation",)

EVENT_KEYS = {
    "time", "kind", "writer", "actor", "on_behalf_of", "via", "from", "to", "refs", "summary",
}
EVENT_REQUIRED = ("time", "kind", "on_behalf_of", "refs")

ISO_TIME = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:[+-]\d{2}:\d{2}|Z)$")
URI_SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


def team_profiles(root: Path) -> dict[str, dict]:
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
    return set(team_profiles(root))


def validate_profile(handle: str, profile: dict, profiles: dict[str, dict]) -> list[str]:
    problems: list[str] = []
    for key in ("handle", "name", "type", "since"):
        if profile.get(key) in (None, ""):
            problems.append(f"profile '{handle}' is missing {key}")
    if str(profile.get("handle", handle)) != handle:
        problems.append(f"profile '{handle}' declares handle {profile.get('handle')!r}")
    kind = profile.get("type")
    if kind not in {"human", "agent"}:
        problems.append(f"profile '{handle}' has unsupported type {kind!r}")
    if kind == "agent":
        accountable = profile.get("accountable_to")
        target = profiles.get(str(accountable)) if accountable else None
        if not accountable:
            problems.append(f"agent profile '{handle}' is missing accountable_to")
        elif target is None or target.get("type") != "human":
            problems.append(
                f"agent profile '{handle}' accountable_to does not name a human profile"
            )
        if ("may_rule_amendments" in profile and
                not isinstance(profile.get("may_rule_amendments"), bool)):
            problems.append(
                f"agent profile '{handle}' may_rule_amendments is not a YAML Boolean"
            )
    return problems


def read_stamp() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def event_token(entropy=os.urandom) -> str:
    return entropy(2).hex()


def event_filename(kind: str, token=event_token, taken=(), clock=read_stamp,
                   attempts: int = 64) -> str:
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


def validate_event(data: dict, filename: str,
                   profiles: dict[str, dict] | None = None) -> list[str]:
    problems: list[str] = []

    name = EVENT_NAME.match(filename)
    legacy = name is None and LEGACY_EVENT_NAME.match(filename) is not None
    if not name and not legacy:
        problems.append(
            f"filename {filename!r} is not <YYYYMMDD-HHMMSS>__<kind>__<token>.md")

    unknown = sorted(set(data) - EVENT_KEYS)
    if unknown:
        problems.append("unknown keys: " + ", ".join(unknown))

    required = EVENT_REQUIRED if not legacy else tuple(
        k for k in EVENT_REQUIRED if k != "on_behalf_of")
    for key in required:
        if not data.get(key):
            problems.append(f"missing {key}")

    if "via" in data and (not isinstance(data["via"], str) or not data["via"].strip()):
        problems.append("via must be non-empty free-form provider/tool text when present")

    kind = data.get("kind")
    if kind in RESERVED_EVENT_KINDS:
        problems.append(f"kind '{kind}' is reserved for a later phase and is not yet valid")
    elif kind and kind not in EVENT_KINDS:
        problems.append(f"kind '{kind}' is outside the closed vocabulary")

    if name and kind and name.group("kind") != kind:
        problems.append(f"filename says kind '{name.group('kind')}', body says '{kind}'")

    on_behalf_of = data.get("on_behalf_of")

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

        writer = data.get("writer")
        if writer:
            profile = profiles.get(str(writer))
            if profile is None:
                problems.append(
                    f"writer '{writer}' is not a declared team/ principal "
                    f"({', '.join(sorted(declared)) if declared else 'team/ declares nobody'})"
                )
            else:
                problems.extend(validate_profile(str(writer), profile, profiles))

    time_value = data.get("time")
    if time_value is not None:
        text = time_value.isoformat() if hasattr(time_value, "isoformat") else str(time_value)
        if not ISO_TIME.match(text):
            problems.append(f"time is not ISO 8601 with an offset: {text!r}")

    refs = data.get("refs")
    if refs is not None and (not isinstance(refs, list) or not refs):
        problems.append("refs must be a non-empty list of paths")

    has_from, has_to = data.get("from") is not None, data.get("to") is not None
    if has_from != has_to:
        problems.append("a state change needs both 'from' and 'to', or neither")

    return problems


def validate_new_event(data: dict, filename: str,
                       profiles: dict[str, dict] | None = None,
                       declared: list[str] | None = None) -> list[str]:
    problems = validate_event(data, filename, profiles)
    declared_set = set(declared or DECLARED_LIFECYCLES)
    name = EVENT_NAME.match(filename)
    if name and not re.fullmatch(r"[0-9a-f]{4}", name.group("token")):
        problems.append("new event token must be exactly four lowercase hex characters")

    time_value = data.get("time")
    if name and time_value is not None:
        text = time_value.isoformat() if hasattr(time_value, "isoformat") else str(time_value)
        if ISO_TIME.match(text):
            components_valid = True
            offset_match = re.search(r"[+-](?P<hours>\d{2}):(?P<minutes>\d{2})$", text)
            if offset_match:
                hours = int(offset_match.group("hours"))
                minutes = int(offset_match.group("minutes"))
                if minutes >= 60:
                    problems.append("time offset minutes must be between 00 and 59")
                    components_valid = False
                if hours > 14 or (hours == 14 and minutes != 0):
                    problems.append("time offset must be within -14:00 and +14:00")
                    components_valid = False
            if components_valid:
                try:
                    parsed_time = datetime.fromisoformat(text.replace("Z", "+00:00"))
                except ValueError:
                    problems.append("time must be a real calendar timestamp with a valid offset")
                else:
                    offset = parsed_time.utcoffset()
                    if offset is None or abs(offset) > timedelta(hours=14):
                        problems.append("time offset must be within -14:00 and +14:00")
                observed_stamp = re.sub(r"[-:]", "", text[:19]).replace("T", "-")
                if observed_stamp != name.group("stamp"):
                    problems.append("filename stamp and event time must name the same observed second")

    if "summary" in data:
        summary = data["summary"]
        if not isinstance(summary, str):
            problems.append("summary must be a string when present")
        elif "\n" in summary or "\r" in summary:
            problems.append("summary must be one line")

    refs = data.get("refs")
    if isinstance(refs, list):
        if any(not isinstance(ref, str) or not ref.strip() for ref in refs):
            problems.append("refs must contain non-empty relative paths")
        for ref in (item for item in refs if isinstance(item, str) and item.strip()):
            normalized = ref.strip().replace("\\", "/")
            if normalized.startswith("/") or re.match(r"^[A-Za-z]:", normalized):
                problems.append(f"ref must be relative to the task directory: {ref!r}")
                continue
            if URI_SCHEME.match(normalized):
                problems.append(
                    f"ref must be a task-relative filesystem path, not a URI: {ref!r}")
                continue
            depth = 0
            for component in normalized.split("/"):
                if component in ("", "."):
                    continue
                if component == "..":
                    depth -= 1
                    if depth < 0:
                        problems.append(f"ref escapes the task directory: {ref!r}")
                        break
                else:
                    depth += 1

    kind = data.get("kind")
    source, target = data.get("from"), data.get("to")
    if kind == "transition":
        if source is None or target is None:
            problems.append("a new transition event requires both 'from' and 'to'")
        elif source != UNDECLARED and source not in declared_set:
            problems.append(f"transition source '{source}' is not declared")
        elif target not in declared_set:
            problems.append(f"transition target '{target}' is not declared")
        elif source in TERMINAL:
            problems.append(f"terminal lifecycle '{source}' has no outgoing transition")
        elif target == "REJECTED":
            pass
        elif target == "BLOCKED" or source == "BLOCKED":
            if target in TERMINAL or source == target:
                problems.append(f"illegal transition pair: {source} -> {target}")
        elif source == UNDECLARED:
            if target in TERMINAL:
                problems.append(f"illegal transition pair: {source} -> {target}")
        elif (source, target) not in FORWARD_TRANSITIONS:
            problems.append(f"illegal transition pair: {source} -> {target}")
    elif source is not None or target is not None:
        problems.append("only a transition event may carry 'from' and 'to'")
    if kind == "gate_answer" and isinstance(refs, list):
        normalized_refs = [str(ref).replace("\\", "/") for ref in refs]
        if not any(ref.endswith("status.md") for ref in normalized_refs):
            problems.append("gate_answer refs must include the governing status.md")
        if not any(re.search(r"(?:^|/)(?:ONB|RES|RF|REVIEW|1_briefing)[^/]*\.md$", ref)
                   for ref in normalized_refs):
            problems.append("gate_answer refs must include the blocked role artifact")
        if not any(re.search(r"(?:^|/)(?:HL|TS)[^/]*\.md$", ref)
                   for ref in normalized_refs):
            problems.append("gate_answer refs must include the governing HL or TS")
    if kind == "coordination_selected" and isinstance(refs, list):
        normalized_refs = [str(ref).replace("\\", "/") for ref in refs]
        if "status.md" not in normalized_refs:
            problems.append("coordination_selected refs must include local status.md")
        if not any(re.search(r"(?:^|/)HL[^/]*\.md$", ref)
                   for ref in normalized_refs):
            problems.append("coordination_selected refs must include governing HL")
    return problems


def journal_dirs(task_dir: Path) -> list[Path]:
    found = [task_dir / "journal"]
    found += [phase / "journal" for phase in iter_phase_dirs(task_dir)]
    return [d for d in found if d.is_dir()]


def read_journal(task_dir: Path, profiles: dict[str, dict] | None = None
                 ) -> tuple[list[dict], list[str]]:
    journals = journal_dirs(task_dir)
    if not journals:
        return [], []
    events, problems = [], []
    legacy = 0
    for journal in journals:
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
            for problem in validate_event(data, path.name, profiles):
                problems.append(f"{label}: {problem}")
            data["_file"] = label
            events.append(data)
    if legacy:
        problems.insert(0, f"{legacy} event(s) predate the 2.0.0 event grammar; immutable "
                            "by rule, so they are recorded as legacy rather than corrected")
    return events, problems


def read_project_config_block(root: Path, block: str) -> dict:
    path = root / ROOT_MARKER / "project_config.yaml"
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as handle:
        document = yaml.safe_load(handle) or {}
    value = document.get(block) or {}
    if not isinstance(value, dict):
        raise ValueError(f"project_config.yaml `{block}` is not a mapping")
    return value
