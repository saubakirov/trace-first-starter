#!/usr/bin/env python3
"""Verify and exercise the asymmetric TFW Assisted maintenance bridge."""

from __future__ import annotations

import argparse
import hashlib
import html
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile
import time
import unicodedata
import uuid


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
sys.dont_write_bytecode = True

MANIFEST_SCHEMA = "tfw-assisted-release-manifest-v1"
POLICY_SCHEMA = "tfw-assisted-maintenance-policy-v1"
REPORT_SCHEMA = "tfw-assisted-private-report-v1"
PROJECTION_SCHEMA = "tfw-assisted-public-candidate-v1"
MANIFEST_PATH = "maintenance/release-manifest.json"
POLICY_PATH = "maintenance/maintenance-policy.json"
SAFE_INTEGER = 9007199254740991
RESERVED = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)), *(f"lpt{i}" for i in range(1, 10))}
STOCK_HOOKS = {
    "02-assisted/.codex/hooks.json": "044013a5cb31ca8c29708b0f83d5ef0e53aecb83d12091c60434a750735043ce",
    "02-assisted/.codex/hooks/tfw-hook.ps1": "85191702eef52dc5191e27485ac50c8e27dd334e2a6bc30d82d14711829361c7",
    "02-assisted/.codex/hooks/tfw-hook.sh": "18039f1631375d7bea2332ffa0c55fdb602315d69ffa98f76f3875fca9eb5a1a",
}
PRIOR_10 = """{"edition":"TFW Assisted","files":[{"path":"02-assisted/.codex/hooks.json","sha256":"044013a5cb31ca8c29708b0f83d5ef0e53aecb83d12091c60434a750735043ce","size":2422},{"path":"02-assisted/.codex/hooks/tfw-hook.ps1","sha256":"85191702eef52dc5191e27485ac50c8e27dd334e2a6bc30d82d14711829361c7","size":15503},{"path":"02-assisted/.codex/hooks/tfw-hook.sh","sha256":"18039f1631375d7bea2332ffa0c55fdb602315d69ffa98f76f3875fca9eb5a1a","size":12851},{"path":"02-assisted/AGENTS.md","sha256":"b7e77b2dcfedf021324dfbdad2198e47af034d1b6cdb4a31b849a70792ad03db","size":13377},{"path":"02-assisted/MIGRATION.md","sha256":"243e315e8b2be57a3c6464bba3a3b7364f1c509d03f161a4b0fc4c7fb293341b","size":3676},{"path":"02-assisted/PROJECT.md","sha256":"9dc0f3aa8f7a2912f5d9fd93baa4dacaec9255c59d7d1534d573c3e47bb09f82","size":3274},{"path":"02-assisted/README.md","sha256":"93098a64554cc04648b079fe2c985cd43e51512406e0be6bb4f191b6a20c22d4","size":6847},{"path":"02-assisted/knowledge/INDEX.md","sha256":"7c66064035584a845420086963258803f88ef209b41a7d41bd8c98529ad3db7d","size":1452},{"path":"02-assisted/people/README.md","sha256":"48483a401f532239e2acb55bafb4cd1fc469fe0dde8c390ac3eeddbdb5f6c9b1","size":1564},{"path":"README.md","sha256":"b8dcf53df0cd43f7c0ed43b8bebec2a6f381cd79ea57ebc5243a8f1f957fe61e","size":3060}],"interface":"public-baseline-v1","schema":"tfw-assisted-release-manifest-v1","version":"1.0"}
"""


class MaintenanceError(Exception):
    """An unsafe, ambiguous or noncanonical maintenance condition."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def canonical(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise MaintenanceError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _safe_numbers(value) -> None:
    if isinstance(value, float) or isinstance(value, int) and not isinstance(value, bool) and abs(value) > SAFE_INTEGER:
        raise MaintenanceError("floating-point or unsafe integer is forbidden")
    if isinstance(value, dict):
        for child in value.values():
            _safe_numbers(child)
    elif isinstance(value, list):
        for child in value:
            _safe_numbers(child)


def load_json_bytes(data: bytes, label: str, require_canonical: bool = True):
    try:
        value = json.loads(data.decode("utf-8"), object_pairs_hook=_pairs, parse_constant=lambda raw: (_ for _ in ()).throw(MaintenanceError(f"invalid number: {raw}")))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise MaintenanceError(f"{label} is not valid UTF-8 JSON") from exc
    _safe_numbers(value)
    if require_canonical and canonical(value) != data:
        raise MaintenanceError(f"{label} is not canonical JSON")
    return value


def load_json(path: Path, label: str, require_canonical: bool = True):
    if path.is_symlink() or not path.is_file():
        raise MaintenanceError(f"{label} is not a regular file")
    return load_json_bytes(path.read_bytes(), label, require_canonical)


def safe_path(raw: str) -> str:
    if not isinstance(raw, str) or not raw or raw != unicodedata.normalize("NFC", raw):
        raise MaintenanceError("path must be non-empty NFC text")
    if "\\" in raw or raw.startswith("/") or re.match(r"^[A-Za-z]:", raw) or any(ord(char) < 32 for char in raw):
        raise MaintenanceError(f"nonportable path: {raw!r}")
    parts = raw.split("/")
    for part in parts:
        stem = part.split(".", 1)[0].casefold()
        if not part or part in {".", ".."} or part[-1] in {" ", "."} or stem in RESERVED or any(char in '<>:"|?*' for char in part):
            raise MaintenanceError(f"invalid path segment: {raw!r}")
    return raw


def regular_file(root: Path, relative: str) -> Path:
    target = root.joinpath(*relative.split("/"))
    try:
        info = os.lstat(target)
    except OSError as exc:
        raise MaintenanceError(f"manifest entry is unavailable: {relative}") from exc
    if not stat.S_ISREG(info.st_mode) or stat.S_ISLNK(info.st_mode) or getattr(info, "st_nlink", 1) != 1:
        raise MaintenanceError(f"manifest entry is not a single regular file: {relative}")
    return target


def validate_manifest(value: dict, root: Path | None = None) -> dict[str, dict]:
    if not isinstance(value, dict) or set(value) != {"schema", "edition", "version", "interface", "files"}:
        raise MaintenanceError("manifest root schema is closed")
    if value["schema"] != MANIFEST_SCHEMA or value["edition"] != "TFW Assisted" or not isinstance(value["version"], str) or not isinstance(value["interface"], str):
        raise MaintenanceError("manifest authority fields are invalid")
    if not isinstance(value["files"], list):
        raise MaintenanceError("manifest files must be an array")
    result = {}
    folded = set()
    previous = None
    for entry in value["files"]:
        if not isinstance(entry, dict) or set(entry) != {"path", "size", "sha256"}:
            raise MaintenanceError("manifest entry schema is closed")
        path = safe_path(entry["path"])
        if path == MANIFEST_PATH:
            raise MaintenanceError("manifest self-entry is forbidden")
        if previous is not None and path <= previous:
            raise MaintenanceError("manifest paths are not canonically ordered")
        previous = path
        case = path.casefold()
        if path in result or case in folded:
            raise MaintenanceError("manifest path collision")
        if not isinstance(entry["size"], int) or isinstance(entry["size"], bool) or entry["size"] < 0 or entry["size"] > SAFE_INTEGER:
            raise MaintenanceError("manifest size is unsafe")
        if not isinstance(entry["sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]):
            raise MaintenanceError("manifest hash is invalid")
        if root is not None:
            actual = regular_file(root, path)
            if actual.stat().st_size != entry["size"] or file_digest(actual) != entry["sha256"]:
                raise MaintenanceError(f"manifest byte mismatch: {path}")
        result[path] = entry
        folded.add(case)
    if POLICY_PATH not in result:
        raise MaintenanceError("maintenance policy is omitted")
    return result


def validate_prior(value: dict) -> dict[str, dict]:
    if not isinstance(value, dict) or set(value) != {"schema", "edition", "version", "interface", "files"}:
        raise MaintenanceError("prior manifest schema is closed")
    if value["schema"] != MANIFEST_SCHEMA or value["edition"] != "TFW Assisted":
        raise MaintenanceError("prior manifest authority is invalid")
    if not isinstance(value["files"], list):
        raise MaintenanceError("prior manifest files must be an array")
    result = {}
    folded = set()
    previous = None
    for entry in value["files"]:
        if not isinstance(entry, dict) or set(entry) != {"path", "size", "sha256"}:
            raise MaintenanceError("prior entry schema is closed")
        path = safe_path(entry["path"])
        if previous is not None and path <= previous:
            raise MaintenanceError("prior paths are not canonically ordered")
        previous = path
        if path.casefold() in folded or not isinstance(entry["size"], int) or isinstance(entry["size"], bool) or not re.fullmatch(r"[0-9a-f]{64}", str(entry["sha256"])):
            raise MaintenanceError("prior entry is invalid")
        folded.add(path.casefold())
        result[path] = entry
    return result


def validate_policy(value: dict, current_manifest_hash: str | None = None) -> None:
    required = {"schema", "interface", "release_version", "target_only", "accepted_priors", "selectors", "retire_exact"}
    if not isinstance(value, dict) or set(value) != required or value["schema"] != POLICY_SCHEMA or value["interface"] != "assisted-maintenance-v1" or value["release_version"] != "1.5" or value["target_only"] != "preserve":
        raise MaintenanceError("maintenance policy root is invalid")
    if not isinstance(value["accepted_priors"], list) or not value["accepted_priors"]:
        raise MaintenanceError("accepted prior edges are missing")
    prior_keys = set()
    for item in value["accepted_priors"]:
        if not isinstance(item, dict) or set(item) != {"version", "interface", "manifest_sha256"} or not re.fullmatch(r"[0-9a-f]{64}", str(item["manifest_sha256"])):
            raise MaintenanceError("accepted prior edge is invalid")
        key = (item["version"], item["interface"])
        if key in prior_keys:
            raise MaintenanceError("accepted prior edge is duplicated")
        prior_keys.add(key)
        if current_manifest_hash and item["manifest_sha256"] == current_manifest_hash:
            raise MaintenanceError("current-manifest policy cycle")
    if not isinstance(value["selectors"], list) or not value["selectors"]:
        raise MaintenanceError("selectors are missing")
    seen = set()
    previous = None
    for item in value["selectors"]:
        if not isinstance(item, dict) or set(item) != {"kind", "path", "authority", "action"}:
            raise MaintenanceError("selector schema is closed")
        if item["kind"] not in {"exact", "prefix"} or item["authority"] not in {"public", "customizable", "downstream"} or item["action"] not in {"update-if-stock", "preserve"}:
            raise MaintenanceError("selector value is invalid")
        path = safe_path(item["path"])
        key = (path, item["kind"])
        if key in seen or previous is not None and key <= previous:
            raise MaintenanceError("selectors conflict or are noncanonical")
        seen.add(key)
        previous = key
    if not isinstance(value["retire_exact"], list) or len(value["retire_exact"]) != 3:
        raise MaintenanceError("exact retirement list is incomplete")
    retired = {}
    for item in value["retire_exact"]:
        if not isinstance(item, dict) or set(item) != {"path", "sha256"}:
            raise MaintenanceError("retirement entry schema is closed")
        retired[safe_path(item["path"])] = item["sha256"]
    if retired != STOCK_HOOKS:
        raise MaintenanceError("only exact known stock hooks may retire")


def classify(policy: dict, path: str) -> dict:
    exact = [item for item in policy["selectors"] if item["kind"] == "exact" and item["path"] == path]
    if len(exact) == 1:
        return exact[0]
    prefixes = [item for item in policy["selectors"] if item["kind"] == "prefix" and (path == item["path"] or path.startswith(item["path"] + "/"))]
    if not prefixes:
        raise MaintenanceError(f"unclassified source path: {path}")
    width = max(len(item["path"].split("/")) for item in prefixes)
    winners = [item for item in prefixes if len(item["path"].split("/")) == width]
    if len(winners) != 1:
        raise MaintenanceError(f"equal-specificity selector conflict: {path}")
    return winners[0]


def manifest_for_source(root: Path) -> dict:
    include = []
    for path in root.rglob("*"):
        if path.is_dir() or path.name == "release-manifest.json" or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        relative = path.relative_to(root).as_posix()
        if relative == "README.md" or relative == "ASSISTED_MAINTENANCE.md" or relative.startswith("maintenance/") or relative.startswith("02-assisted/"):
            safe_path(relative)
            regular_file(root, relative)
            include.append(relative)
    entries = [{"path": item, "size": (root / item).stat().st_size, "sha256": file_digest(root / item)} for item in sorted(include)]
    return {"schema": MANIFEST_SCHEMA, "edition": "TFW Assisted", "version": "1.5", "interface": "assisted-maintenance-v1", "files": entries}


def tree_state(root: Path) -> dict[str, dict]:
    result = {}
    if not root.exists():
        return result
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix().casefold()):
        relative = path.relative_to(root).as_posix()
        info = os.lstat(path)
        if stat.S_ISREG(info.st_mode) and not stat.S_ISLNK(info.st_mode):
            result[relative] = {"kind": "file", "size": info.st_size, "sha256": file_digest(path)}
        elif stat.S_ISDIR(info.st_mode) and not stat.S_ISLNK(info.st_mode):
            result[relative] = {"kind": "dir"}
        else:
            result[relative] = {"kind": "other"}
    return result


def entry_state(root: Path, relative: str) -> dict | None:
    path = root.joinpath(*relative.split("/"))
    if not path.exists() and not path.is_symlink():
        return None
    info = os.lstat(path)
    if not stat.S_ISREG(info.st_mode) or stat.S_ISLNK(info.st_mode):
        return {"kind": "other"}
    return {"kind": "file", "size": info.st_size, "sha256": file_digest(path)}


def same_state(left: dict | None, right: dict | None) -> bool:
    return left == right


def safe_replace(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    descriptor, raw = tempfile.mkstemp(prefix=".assisted-", suffix=".tmp", dir=target.parent)
    temporary = Path(raw)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(source.read_bytes())
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, target)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


class ProjectLock:
    def __init__(self, path: Path):
        self.path = path
        self.stream = None

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.stream = self.path.open("a+b", buffering=0)
        self.stream.seek(0)
        if self.stream.read(1) == b"":
            self.stream.write(b"0")
            self.stream.flush()
            os.fsync(self.stream.fileno())
        self.stream.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(self.stream.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            self.stream.close()
            raise MaintenanceError("another maintenance operation holds the project lock") from exc
        return self

    def __exit__(self, *_):
        try:
            if os.name == "nt":
                import msvcrt
                self.stream.seek(0)
                msvcrt.locking(self.stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.stream.fileno(), fcntl.LOCK_UN)
        finally:
            self.stream.close()


def append_journal(path: Path, event: dict) -> None:
    with path.open("ab", buffering=0) as stream:
        stream.write(canonical(event))
        os.fsync(stream.fileno())


def terminal(path: Path, value: dict) -> None:
    with path.open("xb") as stream:
        stream.write(canonical(value))
        stream.flush()
        os.fsync(stream.fileno())


def prior_from_argument(raw: str) -> tuple[dict, bytes]:
    if raw == "builtin:1.0":
        data = PRIOR_10.encode()
        return load_json_bytes(data, "built-in prior manifest"), data
    path = Path(raw).expanduser().resolve(strict=True)
    data = path.read_bytes()
    return load_json_bytes(data, "prior manifest"), data


def accepted_prior(policy: dict, prior: dict, raw: bytes) -> None:
    matches = [edge for edge in policy["accepted_priors"] if edge["version"] == prior["version"] and edge["interface"] == prior["interface"] and edge["manifest_sha256"] == digest(raw)]
    if len(matches) != 1:
        raise MaintenanceError("prior manifest/version/interface edge is not accepted")


def make_plan(stage: Path, target: Path, current: dict[str, dict], prior: dict[str, dict], policy: dict, baseline: dict) -> list[dict]:
    plan = []
    for relative, new in current.items():
        rule = classify(policy, relative)
        old = prior.get(relative)
        observed = entry_state(target, relative)
        if rule["action"] == "preserve":
            plan.append({"path": relative, "action": "preserve", "baseline": observed})
            continue
        if observed and observed.get("kind") != "file":
            raise MaintenanceError(f"classified target is not a regular file: {relative}")
        if observed and observed.get("sha256") == new["sha256"]:
            plan.append({"path": relative, "action": "unchanged", "baseline": observed})
        elif observed is None and old is None:
            plan.append({"path": relative, "action": "create", "baseline": None})
        elif observed is None:
            raise MaintenanceError(f"accepted stock file is missing: {relative}")
        elif old and observed["sha256"] == old["sha256"]:
            plan.append({"path": relative, "action": "replace", "baseline": observed})
        elif rule["authority"] == "customizable":
            plan.append({"path": relative, "action": "preserve-customized", "baseline": observed})
        else:
            raise MaintenanceError(f"public core differs from every accepted stock hash: {relative}")
    for relative, expected in STOCK_HOOKS.items():
        observed = entry_state(target, relative)
        if observed is None:
            continue
        if observed.get("kind") != "file":
            raise MaintenanceError(f"known hook path is not regular: {relative}")
        plan.append({"path": relative, "action": "delete" if observed["sha256"] == expected else "preserve-modified-hook", "baseline": observed})
    return sorted(plan, key=lambda item: item["path"])


def compare_release(source: Path, target: Path, prior_value: dict, prior_raw: bytes) -> dict:
    source = source.resolve(strict=True)
    target = target.resolve(strict=True)
    manifest_raw = (source / MANIFEST_PATH).read_bytes()
    manifest = load_json_bytes(manifest_raw, "release manifest")
    records = validate_manifest(manifest, source)
    policy = load_json(source / POLICY_PATH, "maintenance policy")
    validate_policy(policy, digest(manifest_raw))
    prior_records = validate_prior(prior_value)
    accepted_prior(policy, prior_value, prior_raw)
    baseline = tree_state(target)
    plan = make_plan(source, target, records, prior_records, policy, baseline)
    counts = {}
    for item in plan:
        counts[item["action"]] = counts.get(item["action"], 0) + 1
    return {"state": "comparison-only", "target_baseline_sha256": digest(canonical(baseline)), "actions": counts, "writes": sum(counts.get(name, 0) for name in ("create", "replace", "delete"))}


def stage_source(source: Path, stage: Path, manifest: dict, records: dict[str, dict]) -> None:
    stage.mkdir(parents=True)
    for relative in records:
        origin = regular_file(source, relative)
        destination = stage.joinpath(*relative.split("/"))
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(origin, destination)
        os.chmod(destination, stat.S_IREAD)
    staged_manifest = validate_manifest(manifest, stage)
    if staged_manifest != records:
        raise MaintenanceError("staged snapshot differs from verified source")


def make_tree_writable(root: Path) -> None:
    if not root.exists():
        return
    for path in root.rglob("*"):
        try:
            os.chmod(path, stat.S_IWRITE | stat.S_IREAD | (stat.S_IEXEC if path.is_dir() else 0))
        except OSError:
            pass


def execute_forward(source: Path, target: Path, prior_value: dict, prior_raw: bytes, operation: Path, inject_after: int = 0, inject_drift: str | None = None, recover_from: Path | None = None) -> dict:
    source = source.resolve(strict=True)
    target = target.resolve(strict=True)
    operation = operation.absolute()
    if operation.exists():
        raise MaintenanceError("operation directory must be create-once")
    if any(os.path.commonpath([str(operation), str(root)]) == str(root) for root in (source, target)):
        raise MaintenanceError("operation directory must be outside source and target")
    manifest_path = source / MANIFEST_PATH
    policy_path = source / POLICY_PATH
    manifest_raw = manifest_path.read_bytes()
    manifest = load_json_bytes(manifest_raw, "release manifest")
    records = validate_manifest(manifest, source)
    policy = load_json(policy_path, "maintenance policy")
    validate_policy(policy, digest(manifest_raw))
    prior_records = validate_prior(prior_value)
    accepted_prior(policy, prior_value, prior_raw)
    for path in records:
        classify(policy, path)
    operation.mkdir(parents=True)
    stage = operation / "source-snapshot"
    stage_source(source, stage, manifest, records)
    baseline = tree_state(target)
    plan = make_plan(stage, target, records, prior_records, policy, baseline)
    operation_id = uuid.uuid4().hex
    journal = operation / "journal.ndjson"
    report = operation / "terminal.json"
    link = None
    if recover_from:
        old = load_json(recover_from, "recovery report")
        if old.get("schema") != REPORT_SCHEMA or old.get("status") != "partial":
            raise MaintenanceError("recovery requires a validated partial report")
        link = old.get("operation_id")
    lock_key = digest(os.path.normcase(str(target)).encode())[:20]
    lock_path = operation.parent / "locks" / f"{lock_key}.lock"
    changes = 0
    with ProjectLock(lock_path):
        if inject_drift:
            drift = target.joinpath(*safe_path(inject_drift).split("/"))
            if not drift.is_file():
                raise MaintenanceError("drift fixture path must be a regular file")
            drift.write_bytes(drift.read_bytes() + b"external-drift")
        if tree_state(target) != baseline:
            make_tree_writable(stage)
            shutil.rmtree(stage)
            operation.rmdir()
            raise MaintenanceError("destination changed after complete baseline; zero maintenance writes")
        validate_manifest(manifest, stage)
        append_journal(journal, {"event": "started", "operation_id": operation_id, "recover_from": link, "planned": len(plan), "schema": REPORT_SCHEMA})
        try:
            for item in plan:
                relative = item["path"]
                if not same_state(entry_state(target, relative), item["baseline"]):
                    raise MaintenanceError(f"per-path prewrite drift: {relative}")
                action = item["action"]
                if action in {"create", "replace"}:
                    safe_replace(stage.joinpath(*relative.split("/")), target.joinpath(*relative.split("/")))
                    changes += 1
                    if entry_state(target, relative)["sha256"] != records[relative]["sha256"]:
                        raise MaintenanceError(f"postcondition failed: {relative}")
                elif action == "delete":
                    target.joinpath(*relative.split("/")).unlink()
                    changes += 1
                    if entry_state(target, relative) is not None:
                        raise MaintenanceError(f"retirement postcondition failed: {relative}")
                append_journal(journal, {"action": action, "event": "path", "path": relative})
                if inject_after and changes >= inject_after:
                    raise MaintenanceError("injected post-first-write failure")
            final = tree_state(target)
            expected = dict(baseline)
            for item in plan:
                path = item["path"]
                if item["action"] in {"create", "replace"}:
                    expected[path] = entry_state(target, path)
                    parent = Path(path).parent
                    while parent.as_posix() != ".":
                        expected.setdefault(parent.as_posix(), {"kind": "dir"})
                        parent = parent.parent
                elif item["action"] == "delete":
                    expected.pop(path, None)
            if final != expected:
                raise MaintenanceError("unexplained destination change remains")
            value = {"schema": REPORT_SCHEMA, "operation_id": operation_id, "status": "verified", "changes": changes, "recover_from": link}
            terminal(report, value)
            return value
        except Exception as exc:
            value = {"schema": REPORT_SCHEMA, "operation_id": operation_id, "status": "partial" if changes else "blocked", "changes": changes, "recover_from": link, "reason": str(exc)}
            terminal(report, value)
            raise MaintenanceError(f"forward operation {value['status']}; terminal report is create-once") from exc


def public_projection(private: dict, suppressed: bool) -> dict:
    if not isinstance(private, dict) or private.get("schema") != REPORT_SCHEMA or private.get("status") not in {"verified", "partial", "blocked"}:
        raise MaintenanceError("private report schema/status is invalid")
    core = {
        "schema": PROJECTION_SCHEMA,
        "direction": "downstream-generic-to-public-candidate",
        "interface": "assisted-maintenance-v1",
        "release_version": "1.5",
        "candidate_classes": ["documentation", "workflow", "template"],
        "requires_independent_review": True,
        "suppressed": bool(suppressed),
    }
    core["public_id"] = digest(canonical(core))
    return core


def reverse_candidate(private_path: Path, candidate_dir: Path, suppressed: bool) -> dict:
    private = load_json(private_path, "private report", require_canonical=False)
    projection = public_projection(private, suppressed)
    if candidate_dir.exists():
        raise MaintenanceError("candidate directory must be create-once")
    candidate_dir.mkdir(parents=True)
    target = candidate_dir / "public-candidate.json"
    target.write_bytes(canonical(projection))
    return projection


def synthetic_policy(prior_hash: str) -> dict:
    return {
        "schema": POLICY_SCHEMA,
        "interface": "assisted-maintenance-v1",
        "release_version": "1.5",
        "target_only": "preserve",
        "accepted_priors": [{"version": "1.0", "interface": "fixture-v1", "manifest_sha256": prior_hash}],
        "selectors": [
            {"kind": "prefix", "path": "02-assisted", "authority": "public", "action": "update-if-stock"},
            {"kind": "exact", "path": "02-assisted/PROJECT.md", "authority": "downstream", "action": "preserve"},
            {"kind": "prefix", "path": "02-assisted/шаблоны", "authority": "customizable", "action": "update-if-stock"},
            {"kind": "exact", "path": POLICY_PATH, "authority": "public", "action": "update-if-stock"},
        ],
        "retire_exact": [{"path": path, "sha256": value} for path, value in sorted(STOCK_HOOKS.items())],
    }


def fixture_release(root: Path) -> tuple[dict, dict, dict, bytes]:
    prior_file = b"old\n"
    prior = {"schema": MANIFEST_SCHEMA, "edition": "TFW Assisted", "version": "1.0", "interface": "fixture-v1", "files": [{"path": "02-assisted/README.md", "size": len(prior_file), "sha256": digest(prior_file)}]}
    prior_raw = canonical(prior)
    policy = synthetic_policy(digest(prior_raw))
    (root / "02-assisted" / "шаблоны").mkdir(parents=True)
    (root / "maintenance").mkdir()
    (root / "02-assisted" / "README.md").write_bytes(b"new\n")
    (root / "02-assisted" / "VERSION").write_bytes(b"1.5\n")
    (root / "02-assisted" / "PROJECT.md").write_bytes(b"project-owned\n")
    (root / "02-assisted" / "шаблоны" / "theme.css").write_bytes(b":root{}\n")
    (root / POLICY_PATH).write_bytes(canonical(policy))
    manifest = manifest_for_source(root)
    (root / MANIFEST_PATH).write_bytes(canonical(manifest))
    return manifest, policy, prior, prior_raw


def static_release_checks(source: Path, manifest: dict, policy: dict) -> dict:
    text_paths = [source.joinpath(*entry["path"].split("/")) for entry in manifest["files"] if entry["path"].endswith((".md", ".yaml", ".json", ".py", ".css", ".html", ".svg"))]
    text = "\n".join(path.read_text(encoding="utf-8-sig") for path in text_paths)
    required = ["1.5", "tfw-assisted", "manual", "ручн", "review"]
    forbidden = ["inno" + "force", "shared " + "drives\\it", "inno" + "force_starter", "company " + "logo"]
    return {
        "agreement": all(token.casefold() in text.casefold() for token in required),
        "neutrality": not any(token.casefold() in text.casefold() for token in forbidden),
        "hooks_absent": all(not (source / path).exists() for path in STOCK_HOOKS),
        "version_exact": (source / "02-assisted" / "VERSION").read_bytes() == b"1.5\n",
        "classified": all(classify(policy, entry["path"]) for entry in manifest["files"]),
    }


def self_test(source: Path) -> dict:
    source = source.resolve(strict=True)
    manifest_raw = (source / MANIFEST_PATH).read_bytes()
    manifest = load_json_bytes(manifest_raw, "release manifest")
    records = validate_manifest(manifest, source)
    policy = load_json(source / POLICY_PATH, "maintenance policy")
    validate_policy(policy, digest(manifest_raw))
    hostile = {}
    attacks = {
        "duplicate": b'{"schema":"x","schema":"y"}\n',
        "unsafe_integer": b'{"n":9007199254740992}\n',
        "traversal": "../x",
        "non_nfc": "e\u0301/x",
        "reserved": "02-assisted/CON.txt",
    }
    for name, attack in attacks.items():
        try:
            if name in {"duplicate", "unsafe_integer"}:
                load_json_bytes(attack, name, require_canonical=False)
            else:
                safe_path(attack)
            hostile[name] = False
        except MaintenanceError:
            hostile[name] = True
    with tempfile.TemporaryDirectory(prefix="assisted-maintenance-") as raw:
        base = Path(raw)
        fixture_source = base / "source"
        target = base / "target"
        fixture_source.mkdir()
        target.mkdir()
        _, _, prior, prior_raw = fixture_release(fixture_source)
        (target / "02-assisted" / "шаблоны").mkdir(parents=True)
        (target / "02-assisted" / "README.md").write_bytes(b"old\n")
        (target / "02-assisted" / "PROJECT.md").write_bytes(b"private-project\n")
        (target / "02-assisted" / "шаблоны" / "theme.css").write_bytes(b"custom-theme\n")
        (target / "work").mkdir()
        (target / "work" / "private.txt").write_bytes(b"keep\n")
        protected_before = {path: entry for path, entry in tree_state(target).items() if path in {"02-assisted/PROJECT.md", "02-assisted/шаблоны/theme.css", "work/private.txt"}}
        result = execute_forward(fixture_source, target, prior, prior_raw, base / "operation-ok")
        protected_after = {path: tree_state(target).get(path) for path in protected_before}
        forward_ok = result["status"] == "verified" and (target / "02-assisted" / "README.md").read_bytes() == b"new\n" and (target / "02-assisted" / "VERSION").read_bytes() == b"1.5\n"
        protected_ok = protected_before == protected_after
        partial_target = base / "partial-target"
        shutil.copytree(target, partial_target)
        (partial_target / "02-assisted" / "README.md").write_bytes(b"old\n")
        (partial_target / "02-assisted" / "VERSION").unlink()
        partial_report = base / "operation-partial" / "terminal.json"
        try:
            execute_forward(fixture_source, partial_target, prior, prior_raw, base / "operation-partial", inject_after=1)
            partial_ok = False
        except MaintenanceError:
            first_hash = file_digest(partial_report)
            first = load_json(partial_report, "partial terminal")
            partial_ok = first["status"] == "partial" and file_digest(partial_report) == first_hash
        recovered = execute_forward(fixture_source, partial_target, prior, prior_raw, base / "operation-recovery", recover_from=partial_report)
        recovery_ok = recovered["status"] == "verified" and recovered["recover_from"] is not None
        drift_target = base / "drift-target"
        shutil.copytree(target, drift_target)
        (drift_target / "02-assisted" / "README.md").write_bytes(b"old\n")
        try:
            execute_forward(fixture_source, drift_target, prior, prior_raw, base / "operation-drift", inject_drift="work/private.txt")
            drift_ok = False
        except MaintenanceError as exc:
            drift_ok = "zero maintenance writes" in str(exc) and (drift_target / "02-assisted" / "README.md").read_bytes() == b"old\n"
        private_a = {"schema": REPORT_SCHEMA, "status": "verified", "operation_id": "secret-a", "private_path": "A", "changes": 3}
        private_b = {"schema": REPORT_SCHEMA, "status": "verified", "operation_id": "secret-b", "private_path": "B", "changes": 900}
        projection_a = canonical(public_projection(private_a, False))
        projection_b = canonical(public_projection(private_b, False))
        privacy_ok = projection_a == projection_b and all(secret not in projection_a for secret in (b"secret", b"private_path", b"changes"))
        public_before = tree_state(fixture_source)
        private_file = base / "private.json"
        private_file.write_bytes(canonical(private_a))
        reverse = reverse_candidate(private_file, base / "candidate", False)
        reverse_ok = reverse["requires_independent_review"] and public_before == tree_state(fixture_source)
        make_tree_writable(base)
    identity_path = source / "02-assisted" / ".agents" / "skills" / "tfw-identity" / "scripts" / "tfw_identity.py"
    spec = importlib.util.spec_from_file_location("tfw_assisted_identity", identity_path)
    identity = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(identity)
    identity_result = identity.self_test()
    builder_path = source / "02-assisted" / "шаблоны" / "build_a4.py"
    builder_spec = importlib.util.spec_from_file_location("tfw_assisted_builder", builder_path)
    builder = importlib.util.module_from_spec(builder_spec)
    builder_spec.loader.exec_module(builder)
    template_result = builder.self_test()
    agreement = static_release_checks(source, manifest, policy)
    roles = {}
    role_text = ""
    for name in ("tfw-plan", "tfw-handoff", "tfw-review", "tfw-update", "tfw-identity"):
        skill = source / "02-assisted" / ".agents" / "skills" / name / "SKILL.md"
        metadata = skill.parent / "agents" / "openai.yaml"
        roles[name] = skill.is_file() and metadata.is_file() and len(skill.read_text(encoding="utf-8")) > 300
        role_text += "\n" + skill.read_text(encoding="utf-8").casefold()
    role_scenarios = all(token in role_text for token in ("частичн", "неоднознач", "прерыв", "параллель", "полный повторный review", "ручн")) and ("тому же executor" in role_text or "тот же executor" in role_text)
    results = {
        "V1": bool(records) and all(hostile.values()),
        "V2": agreement["classified"] and digest(PRIOR_10.encode()) == policy["accepted_priors"][0]["manifest_sha256"],
        "V3": drift_ok,
        "V4": partial_ok and recovery_ok,
        "V5": protected_ok,
        "V6": privacy_ok,
        "V7": identity_result["V7"],
        "V8": identity_result["V8"],
        "V9": template_result["ok"],
        "V10": all(agreement.values()),
        "V11": all(roles.values()) and role_scenarios,
        "V12": forward_ok and reverse_ok,
    }
    return {
        "schema": "tfw-assisted-verification-v1",
        "release_manifest_sha256": digest(manifest_raw),
        "policy_sha256": file_digest(source / POLICY_PATH),
        "results": results,
        "ok": all(results.values()),
    }


def parser() -> argparse.ArgumentParser:
    top = argparse.ArgumentParser(description=__doc__)
    subs = top.add_subparsers(dest="command", required=True)
    manifest = subs.add_parser("manifest")
    manifest.add_argument("--source-root", required=True)
    verify = subs.add_parser("verify-release")
    verify.add_argument("--source-root", required=True)
    test = subs.add_parser("self-test")
    test.add_argument("--source-root", required=True)
    compare = subs.add_parser("compare")
    compare.add_argument("--source-root", required=True)
    compare.add_argument("--target-root", required=True)
    compare.add_argument("--prior-manifest", default="builtin:1.0")
    forward = subs.add_parser("forward")
    forward.add_argument("--source-root", required=True)
    forward.add_argument("--target-root", required=True)
    forward.add_argument("--operation-dir", required=True)
    forward.add_argument("--prior-manifest", default="builtin:1.0")
    forward.add_argument("--recover-from")
    forward.add_argument("--approve-target", required=True)
    reverse = subs.add_parser("reverse-candidate")
    reverse.add_argument("--private-report", required=True)
    reverse.add_argument("--candidate-dir", required=True)
    reverse.add_argument("--suppressed", action="store_true")
    return top


def run(args: argparse.Namespace):
    if args.command == "manifest":
        return manifest_for_source(Path(args.source_root).resolve(strict=True))
    if args.command == "verify-release":
        source = Path(args.source_root).resolve(strict=True)
        manifest_raw = (source / MANIFEST_PATH).read_bytes()
        manifest = load_json_bytes(manifest_raw, "release manifest")
        validate_manifest(manifest, source)
        policy = load_json(source / POLICY_PATH, "maintenance policy")
        validate_policy(policy, digest(manifest_raw))
        return {"state": "verified", "manifest_sha256": digest(manifest_raw), "policy_sha256": file_digest(source / POLICY_PATH)}
    if args.command == "self-test":
        return self_test(Path(args.source_root))
    if args.command == "compare":
        prior, raw = prior_from_argument(args.prior_manifest)
        return compare_release(Path(args.source_root), Path(args.target_root), prior, raw)
    if args.command == "forward":
        target = Path(args.target_root).expanduser().resolve(strict=True)
        approved = Path(args.approve_target).expanduser().resolve(strict=True)
        if target != approved:
            raise MaintenanceError("exact target approval does not match target root")
        prior, raw = prior_from_argument(args.prior_manifest)
        return execute_forward(Path(args.source_root), target, prior, raw, Path(args.operation_dir), recover_from=Path(args.recover_from) if args.recover_from else None)
    return reverse_candidate(Path(args.private_report), Path(args.candidate_dir), args.suppressed)


def main() -> int:
    try:
        print(canonical(run(parser().parse_args())).decode(), end="")
        return 0
    except MaintenanceError as exc:
        print(canonical({"state": "blocked", "reason": str(exc)}).decode(), end="")
        return 4
    except Exception as exc:
        print(canonical({"state": "blocked", "reason": f"unexpected failure: {type(exc).__name__}"}).decode(), end="")
        return 5


if __name__ == "__main__":
    sys.exit(main())
