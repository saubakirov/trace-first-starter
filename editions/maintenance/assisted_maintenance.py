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
import subprocess
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


def _is_link_or_reparse(info) -> bool:
    return stat.S_ISLNK(info.st_mode) or bool(getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0))


def _component_chain(path: Path) -> list[Path]:
    result = []
    current = path.absolute()
    while True:
        result.append(current)
        if current.parent == current:
            break
        current = current.parent
    return list(reversed(result))


def pin_existing(path: Path, label: str, require_directory: bool = True) -> tuple[Path, list[tuple[str, int, int]]]:
    absolute = path.expanduser().absolute()
    pin = []
    try:
        for component in _component_chain(absolute):
            info = os.lstat(component)
            if _is_link_or_reparse(info):
                raise MaintenanceError(f"{label} ancestry contains a link or reparse point")
            if component != absolute and not stat.S_ISDIR(info.st_mode):
                raise MaintenanceError(f"{label} ancestry contains a non-directory")
            pin.append((os.path.normcase(str(component)), info.st_dev, info.st_ino))
        final = os.lstat(absolute)
        if require_directory and not stat.S_ISDIR(final.st_mode):
            raise MaintenanceError(f"{label} is not a directory")
        if not require_directory and not stat.S_ISREG(final.st_mode):
            raise MaintenanceError(f"{label} is not a regular file")
        return absolute.resolve(strict=True), pin
    except MaintenanceError:
        raise
    except OSError as exc:
        raise MaintenanceError(f"{label} cannot be pinned") from exc


def recheck_pin(pin: list[tuple[str, int, int]], label: str) -> None:
    try:
        for raw, device, inode in pin:
            info = os.lstat(raw)
            if _is_link_or_reparse(info) or info.st_dev != device or info.st_ino != inode:
                raise MaintenanceError(f"{label} pin changed")
    except MaintenanceError:
        raise
    except OSError as exc:
        raise MaintenanceError(f"{label} pin is unavailable") from exc


def _windows_acl(path: Path) -> dict:
    program = r'''
$ErrorActionPreference = 'Stop'
$acl = Get-Acl -LiteralPath $env:TFW_ASSISTED_MAINTENANCE_ACL
$identity = [Security.Principal.WindowsIdentity]::GetCurrent()
$owner = ([Security.Principal.NTAccount]$acl.Owner).Translate([Security.Principal.SecurityIdentifier]).Value
$rules = @($acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier]) | ForEach-Object {
  [PSCustomObject]@{ sid=$_.IdentityReference.Value; type=$_.AccessControlType.ToString(); rights=$_.FileSystemRights.ToString() }
})
[PSCustomObject]@{ current=$identity.User.Value; owner=$owner; rules=$rules } | ConvertTo-Json -Depth 4 -Compress
'''
    environment = dict(os.environ)
    environment["TFW_ASSISTED_MAINTENANCE_ACL"] = str(path)
    try:
        result = subprocess.run(
            ["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", program],
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            timeout=10,
        )
        if result.returncode != 0:
            raise MaintenanceError("private Windows ACL probe failed")
        return json.loads(result.stdout)
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError) as exc:
        raise MaintenanceError("private Windows ACL probe failed") from exc


def private_permissions(path: Path) -> None:
    try:
        info = os.lstat(path)
        if os.name == "nt":
            acl = _windows_acl(path)
            allowed = {acl["current"], "S-1-3-4", "S-1-5-18", "S-1-5-32-544"}
            grants = [rule for rule in acl["rules"] if rule["type"] == "Allow"]
            if (
                acl["owner"] != acl["current"]
                or not any(rule["sid"] == acl["current"] and "FullControl" in rule["rights"] for rule in grants)
                or any(rule["sid"] not in allowed for rule in grants)
                or any(rule["type"] == "Deny" and rule["sid"] == acl["current"] for rule in acl["rules"])
            ):
                raise MaintenanceError("private Windows ACL/owner proof failed")
        elif info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
            raise MaintenanceError("private Unix owner/mode proof failed")
    except MaintenanceError:
        raise
    except OSError as exc:
        raise MaintenanceError("private permission probe failed") from exc


def secure_private(path: Path) -> None:
    if os.name == "nt":
        acl = _windows_acl(path)
        result = subprocess.run(
            ["icacls", str(path), "/inheritance:r", "/grant:r", f"*{acl['current']}:(OI)(CI)F"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )
        if result.returncode != 0:
            raise MaintenanceError("private Windows ACL setup failed")
    else:
        os.chmod(path, 0o700 if path.is_dir() else 0o600)
    private_permissions(path)


def _ensure_directory(path: Path, label: str, require_private: bool) -> tuple[Path, list[tuple[str, int, int]]]:
    candidate = path.expanduser().absolute()
    missing: list[Path] = []
    current = candidate
    while True:
        try:
            os.lstat(current)
            break
        except FileNotFoundError:
            missing.append(current)
            if current.parent == current:
                raise MaintenanceError(f"{label} has no existing ancestor")
            current = current.parent
        except OSError as exc:
            raise MaintenanceError(f"{label} cannot be inspected") from exc
    _, pin = pin_existing(current, f"{label} existing ancestor")
    for item in reversed(missing):
        recheck_pin(pin, f"{label} existing ancestor")
        try:
            item.mkdir(parents=False)
        except OSError as exc:
            raise MaintenanceError(f"{label} cannot be created") from exc
        secure_private(item)
        _, pin = pin_existing(item, label)
    resolved, pin = pin_existing(candidate, label)
    if require_private:
        private_permissions(resolved)
    return resolved, pin


def maintenance_state_home() -> Path:
    if os.name == "nt":
        value = os.environ.get("LOCALAPPDATA")
        if not value:
            raise MaintenanceError("LOCALAPPDATA is unavailable for the private project lock")
        return Path(value)
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support"
    return Path(os.environ.get("XDG_STATE_HOME", str(Path.home() / ".local" / "state")))


def project_lock_path(
    target: Path,
    target_pin: list[tuple[str, int, int]],
    protected: list[Path],
    state_home: Path | None = None,
) -> tuple[Path, list[tuple[str, int, int]], list[tuple[str, int, int]]]:
    base = (state_home if state_home is not None else maintenance_state_home()).expanduser().absolute()
    namespace = base / "tfw-assisted"
    lock_root = namespace / "maintenance-locks-v1"
    for root in protected:
        absolute = root.expanduser().absolute()
        if _inside(lock_root, absolute) or _inside(absolute, lock_root):
            raise MaintenanceError("private project-lock root overlaps a protected root")
    _ensure_directory(base, "private state home", False)
    namespace, namespace_pin = _ensure_directory(namespace, "private Assisted state namespace", True)
    lock_root, lock_root_pin = _ensure_directory(lock_root, "private project-lock root", True)
    recheck_pin(target_pin, "target root")
    identity = {
        "device": target_pin[-1][1],
        "inode": target_pin[-1][2],
        "path": os.path.normcase(str(target)),
    }
    lock_key = digest(canonical(identity))
    return lock_root / f"target-{lock_key}.lock", namespace_pin, lock_root_pin


def _inside(candidate: Path, root: Path) -> bool:
    try:
        return os.path.commonpath([os.path.normcase(str(candidate)), os.path.normcase(str(root))]) == os.path.normcase(str(root))
    except ValueError:
        return False


def prepare_create_root(raw: Path, protected: list[Path], label: str) -> tuple[Path, list[tuple[str, int, int]]]:
    candidate = raw.expanduser().absolute()
    if candidate.exists() or candidate.is_symlink():
        raise MaintenanceError(f"{label} must be create-once")
    parent, parent_pin = pin_existing(candidate.parent, f"{label} parent")
    proposed = parent / candidate.name
    for root in protected:
        if _inside(proposed, root):
            raise MaintenanceError(f"{label} must be outside protected roots")
    return proposed, parent_pin


def create_pinned_root(candidate: Path, parent_pin: list[tuple[str, int, int]], protected: list[Path], label: str) -> list[tuple[str, int, int]]:
    recheck_pin(parent_pin, f"{label} parent")
    candidate.mkdir(parents=False)
    resolved, pin = pin_existing(candidate, label)
    if resolved != candidate or any(_inside(resolved, root) for root in protected):
        raise MaintenanceError(f"{label} resolved into a protected root")
    recheck_pin(parent_pin, f"{label} parent")
    return pin


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


def manifest_for_source(root: Path, policy: dict | None = None) -> dict:
    if policy is None:
        policy = load_json(root / POLICY_PATH, "maintenance policy")
        validate_policy(policy)
    include = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        managed = relative in {"README.md", "ASSISTED_MAINTENANCE.md", MANIFEST_PATH, POLICY_PATH} or relative.startswith("maintenance/") or relative.startswith("02-assisted/")
        if not managed:
            continue
        info = os.lstat(path)
        if _is_link_or_reparse(info) or not (stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode)):
            raise MaintenanceError(f"managed payload contains a non-regular entry: {relative}")
        if stat.S_ISDIR(info.st_mode):
            continue
        safe_path(relative)
        if relative == MANIFEST_PATH:
            regular_file(root, relative)
            continue
        rule = classify(policy, relative)
        if rule["authority"] == "downstream" and rule["kind"] == "prefix":
            continue
        regular_file(root, relative)
        include.append(relative)
    entries = [{"path": item, "size": (root / item).stat().st_size, "sha256": file_digest(root / item)} for item in sorted(include)]
    return {"schema": MANIFEST_SCHEMA, "edition": "TFW Assisted", "version": "1.5", "interface": "assisted-maintenance-v1", "files": entries}


def verify_release_root(root: Path, mutable_authorities: set[str] | None = None) -> tuple[dict, dict[str, dict], dict, bytes]:
    mutable_authorities = mutable_authorities or set()
    root, root_pin = pin_existing(root, "release root")
    manifest_path = regular_file(root, MANIFEST_PATH)
    manifest_raw = manifest_path.read_bytes()
    manifest = load_json_bytes(manifest_raw, "release manifest")
    records = validate_manifest(manifest)
    policy = load_json(root / POLICY_PATH, "maintenance policy")
    validate_policy(policy, digest(manifest_raw))
    generated = manifest_for_source(root, policy)
    if {key: manifest[key] for key in ("schema", "edition", "version", "interface")} != {key: generated[key] for key in ("schema", "edition", "version", "interface")}:
        raise MaintenanceError("release authority fields differ from regenerated payload")
    expected = {entry["path"]: entry for entry in generated["files"]}
    if set(records) != set(expected):
        raise MaintenanceError("release manifest paths differ from regenerated allowed payload")
    for relative, stored in records.items():
        rule = classify(policy, relative)
        if rule["authority"] not in mutable_authorities and stored != expected[relative]:
            raise MaintenanceError(f"release manifest bytes differ from regenerated payload: {relative}")
    recheck_pin(root_pin, "release root")
    return manifest, records, policy, manifest_raw


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
    def __init__(self, path: Path, namespace_pin: list[tuple[str, int, int]], root_pin: list[tuple[str, int, int]]):
        self.path = path
        self.namespace_pin = namespace_pin
        self.root_pin = root_pin
        self.stream = None

    def __enter__(self):
        recheck_pin(self.namespace_pin, "private Assisted state namespace")
        recheck_pin(self.root_pin, "private project-lock root")
        private_permissions(self.path.parent.parent)
        private_permissions(self.path.parent)
        try:
            observed = os.lstat(self.path)
            if _is_link_or_reparse(observed) or not stat.S_ISREG(observed.st_mode) or getattr(observed, "st_nlink", 1) != 1:
                raise MaintenanceError("project lock is not a single regular file")
        except FileNotFoundError:
            pass
        except OSError as exc:
            raise MaintenanceError("project lock cannot be inspected") from exc
        try:
            descriptor = os.open(self.path, os.O_CREAT | os.O_RDWR, 0o600)
            current = os.fstat(descriptor)
            linked = os.lstat(self.path)
            if (
                _is_link_or_reparse(linked)
                or not stat.S_ISREG(current.st_mode)
                or getattr(current, "st_nlink", 1) != 1
                or current.st_dev != linked.st_dev
                or current.st_ino != linked.st_ino
            ):
                os.close(descriptor)
                raise MaintenanceError("project lock changed during open")
            if os.name != "nt":
                os.fchmod(descriptor, 0o600)
            self.stream = os.fdopen(descriptor, "r+b", buffering=0)
            private_permissions(self.path)
        except MaintenanceError:
            raise
        except OSError as exc:
            raise MaintenanceError("project lock cannot be opened") from exc
        locked = False
        try:
            self.stream.seek(0)
            if self.stream.read(1) == b"":
                self.stream.write(b"0")
                self.stream.flush()
                os.fsync(self.stream.fileno())
            self.stream.seek(0)
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(self.stream.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            locked = True
        except OSError as exc:
            self.stream.close()
            raise MaintenanceError("another maintenance operation holds the project lock") from exc
        try:
            recheck_pin(self.namespace_pin, "private Assisted state namespace")
            recheck_pin(self.root_pin, "private project-lock root")
            private_permissions(self.path.parent.parent)
            private_permissions(self.path.parent)
            private_permissions(self.path)
        except Exception:
            if locked:
                self._release()
            raise
        return self

    def _release(self) -> None:
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

    def __exit__(self, *_):
        self._release()


def append_journal(path: Path, event: dict) -> None:
    with path.open("ab", buffering=0) as stream:
        stream.write(canonical(event))
        os.fsync(stream.fileno())


def terminal(path: Path, value: dict) -> None:
    with path.open("xb") as stream:
        stream.write(canonical(value))
        stream.flush()
        os.fsync(stream.fileno())


def validate_terminal_report(value: dict, require_verified: bool = False) -> dict:
    if not isinstance(value, dict) or value.get("schema") != REPORT_SCHEMA or value.get("status") not in {"verified", "partial", "blocked"}:
        raise MaintenanceError("private terminal schema/status is invalid")
    expected = {"schema", "operation_id", "status", "changes", "recover_from"}
    if value["status"] != "verified":
        expected.add("reason")
    if set(value) != expected:
        raise MaintenanceError("private terminal fields are not closed")
    if not isinstance(value["operation_id"], str) or not re.fullmatch(r"[0-9a-f]{32}", value["operation_id"]):
        raise MaintenanceError("private terminal operation_id is invalid")
    if not isinstance(value["changes"], int) or isinstance(value["changes"], bool) or not 0 <= value["changes"] <= SAFE_INTEGER:
        raise MaintenanceError("private terminal changes is invalid")
    if value["recover_from"] is not None and (not isinstance(value["recover_from"], str) or not re.fullmatch(r"[0-9a-f]{32}", value["recover_from"])):
        raise MaintenanceError("private terminal recovery link is invalid")
    if value["status"] != "verified" and (not isinstance(value["reason"], str) or not value["reason"] or "\n" in value["reason"]):
        raise MaintenanceError("private terminal reason is invalid")
    if require_verified and value["status"] != "verified":
        raise MaintenanceError("reverse promotion requires a verified terminal")
    return value


def load_terminal_provenance(path: Path, protected_roots: list[Path]) -> tuple[dict, list[tuple[str, int, int]]]:
    terminal_path, terminal_pin = pin_existing(path, "private terminal", require_directory=False)
    if terminal_path.name != "terminal.json" or any(_inside(terminal_path, root) for root in protected_roots):
        raise MaintenanceError("private terminal provenance is outside the approved operation boundary")
    report = validate_terminal_report(load_json(terminal_path, "private terminal"), require_verified=True)
    journal_path = terminal_path.parent / "journal.ndjson"
    journal_path, journal_pin = pin_existing(journal_path, "private journal", require_directory=False)
    events = []
    for raw in journal_path.read_bytes().splitlines(keepends=True):
        events.append(load_json_bytes(raw, "private journal event"))
    if not events:
        raise MaintenanceError("private journal is empty")
    started = events[0]
    if not isinstance(started, dict) or set(started) != {"event", "operation_id", "recover_from", "planned", "schema"} or started["event"] != "started" or started["schema"] != REPORT_SCHEMA or started["operation_id"] != report["operation_id"] or started["recover_from"] != report["recover_from"] or not isinstance(started["planned"], int):
        raise MaintenanceError("private journal start does not bind terminal provenance")
    path_events = events[1:]
    mutations = 0
    for event in path_events:
        if not isinstance(event, dict) or set(event) != {"action", "event", "path"} or event["event"] != "path" or event["action"] not in {"create", "replace", "delete", "preserve", "preserve-customized", "unchanged"}:
            raise MaintenanceError("private journal path event is invalid")
        safe_path(event["path"])
        mutations += event["action"] in {"create", "replace", "delete"}
    if started["planned"] != len(path_events) or report["changes"] != mutations:
        raise MaintenanceError("private terminal does not match journal counts")
    recheck_pin(terminal_pin, "private terminal")
    recheck_pin(journal_pin, "private journal")
    return report, terminal_pin + journal_pin


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


def release_records(records: dict[str, dict], manifest_raw: bytes) -> dict[str, dict]:
    result = dict(records)
    result[MANIFEST_PATH] = {"path": MANIFEST_PATH, "size": len(manifest_raw), "sha256": digest(manifest_raw)}
    return result


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
    source, _ = pin_existing(source, "source root")
    target, _ = pin_existing(target, "target root")
    manifest, records, policy, manifest_raw = verify_release_root(source, {"downstream"})
    prior_records = validate_prior(prior_value)
    accepted_prior(policy, prior_value, prior_raw)
    baseline = tree_state(target)
    plan = make_plan(source, target, release_records(records, manifest_raw), prior_records, policy, baseline)
    counts = {}
    for item in plan:
        counts[item["action"]] = counts.get(item["action"], 0) + 1
    return {"state": "comparison-only", "target_baseline_sha256": digest(canonical(baseline)), "actions": counts, "writes": sum(counts.get(name, 0) for name in ("create", "replace", "delete"))}


def stage_source(source: Path, stage: Path, manifest: dict, records: dict[str, dict], manifest_raw: bytes) -> None:
    for relative in records:
        origin = regular_file(source, relative)
        destination = stage.joinpath(*relative.split("/"))
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(origin, destination)
        os.chmod(destination, stat.S_IREAD)
    target_manifest = stage.joinpath(*MANIFEST_PATH.split("/"))
    target_manifest.parent.mkdir(parents=True, exist_ok=True)
    target_manifest.write_bytes(manifest_raw)
    os.chmod(target_manifest, stat.S_IREAD)
    staged_manifest, staged_records, _, staged_raw = verify_release_root(stage, {"downstream"})
    if staged_manifest != manifest or staged_records != records or staged_raw != manifest_raw:
        raise MaintenanceError("staged snapshot differs from verified source")


def make_tree_writable(root: Path) -> None:
    if not root.exists():
        return
    for path in root.rglob("*"):
        try:
            os.chmod(path, stat.S_IWRITE | stat.S_IREAD | (stat.S_IEXEC if path.is_dir() else 0))
        except OSError:
            pass


def execute_forward(
    source: Path,
    target: Path,
    prior_value: dict,
    prior_raw: bytes,
    operation: Path,
    inject_after: int = 0,
    inject_drift: str | None = None,
    recover_from: Path | None = None,
    state_home: Path | None = None,
) -> dict:
    source, source_pin = pin_existing(source, "source root")
    target, target_pin = pin_existing(target, "target root")
    operation, operation_parent_pin = prepare_create_root(operation, [source, target], "operation directory")
    manifest, records, policy, manifest_raw = verify_release_root(source, {"downstream"})
    current_records = release_records(records, manifest_raw)
    prior_records = validate_prior(prior_value)
    accepted_prior(policy, prior_value, prior_raw)
    for path in current_records:
        classify(policy, path)
    link = None
    if recover_from:
        old = validate_terminal_report(load_json(recover_from, "recovery report"))
        if old["status"] != "partial":
            raise MaintenanceError("recovery requires a validated partial report")
        link = old.get("operation_id")
    lock_path, namespace_pin, lock_root_pin = project_lock_path(target, target_pin, [source, target, operation], state_home)
    with ProjectLock(lock_path, namespace_pin, lock_root_pin):
        recheck_pin(source_pin, "source root")
        recheck_pin(target_pin, "target root")
        recheck_pin(operation_parent_pin, "operation directory parent")
        operation_pin = create_pinned_root(operation, operation_parent_pin, [source, target], "operation directory")
        stage, stage_parent_pin = prepare_create_root(operation / "source-snapshot", [source, target], "source snapshot")
        stage_pin = create_pinned_root(stage, stage_parent_pin, [source, target], "source snapshot")
        stage_source(source, stage, manifest, records, manifest_raw)
        recheck_pin(source_pin, "source root")
        recheck_pin(target_pin, "target root")
        recheck_pin(operation_pin, "operation directory")
        recheck_pin(stage_pin, "source snapshot")
        baseline = tree_state(target)
        plan = make_plan(stage, target, current_records, prior_records, policy, baseline)
        operation_id = uuid.uuid4().hex
        journal = operation / "journal.ndjson"
        report = operation / "terminal.json"
        changes = 0
        if inject_drift:
            drift = target.joinpath(*safe_path(inject_drift).split("/"))
            if not drift.is_file():
                raise MaintenanceError("drift fixture path must be a regular file")
            drift.write_bytes(drift.read_bytes() + b"external-drift")
        if tree_state(target) != baseline:
            make_tree_writable(stage)
            shutil.rmtree(stage)
            raise MaintenanceError("destination changed after complete baseline; zero maintenance writes")
        verify_release_root(stage, {"downstream"})
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
                    if entry_state(target, relative)["sha256"] != current_records[relative]["sha256"]:
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
            verify_release_root(target, {"downstream", "customizable"})
            value = {"schema": REPORT_SCHEMA, "operation_id": operation_id, "status": "verified", "changes": changes, "recover_from": link}
            terminal(report, value)
            return value
        except Exception as exc:
            value = {"schema": REPORT_SCHEMA, "operation_id": operation_id, "status": "partial" if changes else "blocked", "changes": changes, "recover_from": link, "reason": str(exc)}
            terminal(report, value)
            raise MaintenanceError(f"forward operation {value['status']}; terminal report is create-once") from exc


def public_projection(private: dict, suppressed: bool) -> dict:
    validate_terminal_report(private, require_verified=True)
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


def reverse_candidate(private_path: Path, candidate_root: Path, approved_root: Path, protected_roots: list[Path], suppressed: bool) -> dict:
    roots = [pin_existing(root, "protected public/source/target root")[0] for root in protected_roots]
    if os.path.normcase(os.path.abspath(candidate_root)) != os.path.normcase(os.path.abspath(approved_root)):
        raise MaintenanceError("exact candidate-root approval does not match")
    private, provenance_pin = load_terminal_provenance(private_path, roots)
    projection = public_projection(private, suppressed)
    protected = roots + [Path(private_path).expanduser().absolute().parent.resolve(strict=True)]
    candidate_root, parent_pin = prepare_create_root(candidate_root, protected, "candidate root")
    candidate_pin = create_pinned_root(candidate_root, parent_pin, protected, "candidate root")
    recheck_pin(provenance_pin, "private report provenance")
    target = candidate_root / "public-candidate.json"
    with target.open("xb") as stream:
        stream.write(canonical(projection))
        stream.flush()
        os.fsync(stream.fileno())
    recheck_pin(candidate_pin, "candidate root")
    if load_json(target, "public candidate") != projection:
        raise MaintenanceError("public candidate post-read mismatch")
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
            {"kind": "exact", "path": MANIFEST_PATH, "authority": "public", "action": "update-if-stock"},
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


def role_scenario_matrix() -> dict:
    scenarios = [
        ({"name": "complete", "capability": True, "target": "exact", "active": None, "report": "complete"}, {"action": "accept-report", "reuse": "executor-1", "duplicates": 0}),
        ({"name": "partial", "capability": True, "target": "exact", "active": "executor-1", "report": "partial"}, {"action": "correct", "reuse": "executor-1", "duplicates": 0}),
        ({"name": "lost-handle", "capability": True, "target": "lost", "active": "executor-1", "report": None}, {"action": "manual-stop", "reuse": None, "duplicates": 0}),
        ({"name": "no-interrupt", "capability": True, "target": "exact", "active": "executor-1", "interrupt": False}, {"action": "wait-or-manual", "reuse": "executor-1", "duplicates": 0}),
        ({"name": "overlap", "capability": True, "target": "exact", "active": "executor-1", "dispatch": "executor-2"}, {"action": "reject-overlap", "reuse": "executor-1", "duplicates": 0}),
        ({"name": "manual-fallback", "capability": False, "target": None, "active": None}, {"action": "manual-complete", "reuse": None, "duplicates": 0}),
        ({"name": "full-re-review", "capability": True, "target": "reviewer-1", "prior": "REVISE", "contract": "full"}, {"action": "rerun-full-contract", "reuse": "reviewer-1", "duplicates": 0}),
    ]
    records = []
    for initial, expected in scenarios:
        name = initial["name"]
        if not initial.get("capability"):
            observed = {"action": "manual-complete", "reuse": None, "duplicates": 0}
        elif name == "complete":
            observed = {"action": "accept-report", "reuse": "executor-1", "duplicates": 0}
        elif name == "partial":
            observed = {"action": "correct", "reuse": initial["active"], "duplicates": 0}
        elif name == "lost-handle":
            observed = {"action": "manual-stop", "reuse": None, "duplicates": 0}
        elif name == "no-interrupt":
            observed = {"action": "wait-or-manual", "reuse": initial["active"], "duplicates": 0}
        elif name == "overlap":
            observed = {"action": "reject-overlap", "reuse": initial["active"], "duplicates": 0}
        else:
            observed = {"action": "rerun-full-contract", "reuse": initial["target"], "duplicates": 0}
        records.append({"scenario": name, "input": initial, "expected": expected, "observed": observed, "passed": observed == expected})
    return {"schema": "tfw-assisted-role-tabletop-v1", "records": records, "ok": all(record["passed"] for record in records)}


def write_private_operation_fixture(root: Path, operation_id: str, changes: int) -> Path:
    root.mkdir()
    journal = root / "journal.ndjson"
    append_journal(journal, {"event": "started", "operation_id": operation_id, "recover_from": None, "planned": changes, "schema": REPORT_SCHEMA})
    for index in range(changes):
        append_journal(journal, {"action": "create", "event": "path", "path": f"02-assisted/synthetic-{index}.md"})
    terminal_path = root / "terminal.json"
    terminal(terminal_path, {"schema": REPORT_SCHEMA, "operation_id": operation_id, "status": "verified", "changes": changes, "recover_from": None})
    return terminal_path


def real_contention_fixture(source: Path, target: Path, prior: dict, prior_raw: bytes, base: Path, state_home: Path) -> dict:
    holder_program = r'''
import importlib.util
from pathlib import Path
import sys

spec = importlib.util.spec_from_file_location("assisted_lock_holder", sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
target, target_pin = module.pin_existing(Path(sys.argv[2]), "target root")
lock_path, namespace_pin, root_pin = module.project_lock_path(target, target_pin, [target], Path(sys.argv[3]))
with module.ProjectLock(lock_path, namespace_pin, root_pin):
    print("LOCKED " + lock_path.name, flush=True)
    sys.stdin.readline()
'''
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    holder = subprocess.Popen(
        [sys.executable, "-B", "-c", holder_program, str(Path(__file__).resolve()), str(target), str(state_home)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        env=environment,
    )
    try:
        ready = holder.stdout.readline().strip()
        if not ready.startswith("LOCKED target-"):
            diagnostic = holder.stderr.read().strip()
            raise MaintenanceError(f"real lock-holder process failed: {diagnostic or ready or 'no output'}")
        target_root, target_pin = pin_existing(target, "target root")
        expected_lock, _, _ = project_lock_path(target_root, target_pin, [source, target], state_home)
        before = tree_state(target)
        losing_operation = base / "operation-contended-loser"
        try:
            execute_forward(source, target, prior, prior_raw, losing_operation, state_home=state_home)
            second_blocked = False
        except MaintenanceError as exc:
            second_blocked = "holds the project lock" in str(exc)
        same_target_zero_write = before == tree_state(target) and not losing_operation.exists()

        independent = base / "independent-target"
        independent.mkdir()
        (independent / "02-assisted").mkdir()
        (independent / "02-assisted" / "README.md").write_bytes(b"old\n")
        (independent / "02-assisted" / "PROJECT.md").write_bytes(b"independent-project\n")
        independent_result = execute_forward(
            source,
            independent,
            prior,
            prior_raw,
            base / "operation-independent-target",
            state_home=state_home,
        )
        return {
            "real_processes": 2,
            "same_target_lock_path_equal": ready == "LOCKED " + expected_lock.name,
            "second_blocked_before_operation_directory": second_blocked and not losing_operation.exists(),
            "same_target_product_zero_write": same_target_zero_write,
            "different_target_independent": independent_result["status"] == "verified",
        }
    finally:
        if holder.stdin is not None:
            try:
                holder.stdin.write("release\n")
                holder.stdin.flush()
                holder.stdin.close()
            except OSError:
                pass
        try:
            holder.wait(timeout=20)
        except subprocess.TimeoutExpired:
            holder.kill()
            holder.wait(timeout=5)


def self_test(source: Path) -> dict:
    source, _ = pin_existing(source, "release root")
    manifest, records, policy, manifest_raw = verify_release_root(source)
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
        state_home = base / "private-state"
        fixture_source = base / "source"
        target = base / "target"
        fixture_source.mkdir()
        target.mkdir()
        _, _, prior, prior_raw = fixture_release(fixture_source)
        completeness = {}

        def rejected_copy(name, mutation):
            hostile_root = base / f"hostile-{name}"
            shutil.copytree(fixture_source, hostile_root)
            mutation(hostile_root)
            try:
                verify_release_root(hostile_root)
                completeness[name] = False
            except MaintenanceError:
                completeness[name] = True

        def edit_manifest(root, transform):
            path = root / MANIFEST_PATH
            value = json.loads(path.read_text(encoding="utf-8"))
            transform(value)
            path.write_bytes(canonical(value))

        rejected_copy("omitted-payload", lambda root: edit_manifest(root, lambda value: value["files"].pop(0)))
        rejected_copy("omitted-policy", lambda root: (root / POLICY_PATH).unlink())
        rejected_copy("unexpected-payload", lambda root: (root / "02-assisted" / "unexpected.txt").write_bytes(b"unexpected\n"))
        rejected_copy("self-entry", lambda root: edit_manifest(root, lambda value: value["files"].append({"path": MANIFEST_PATH, "size": 1, "sha256": "0" * 64})))

        def nonregular(root):
            path = root / "02-assisted" / "README.md"
            path.unlink()
            path.mkdir()

        rejected_copy("nonregular", nonregular)
        (target / "02-assisted" / "шаблоны").mkdir(parents=True)
        (target / "02-assisted" / "README.md").write_bytes(b"old\n")
        (target / "02-assisted" / "PROJECT.md").write_bytes(b"private-project\n")
        (target / "02-assisted" / "шаблоны" / "theme.css").write_bytes(b"custom-theme\n")
        (target / "work").mkdir()
        (target / "work" / "private.txt").write_bytes(b"keep\n")
        contention = real_contention_fixture(fixture_source, target, prior, prior_raw, base, state_home)
        protected_before = {path: entry for path, entry in tree_state(target).items() if path in {"02-assisted/PROJECT.md", "02-assisted/шаблоны/theme.css", "work/private.txt"}}
        result = execute_forward(fixture_source, target, prior, prior_raw, base / "operation-ok", state_home=state_home)
        protected_after = {path: tree_state(target).get(path) for path in protected_before}
        target_verified = verify_release_root(target, {"downstream", "customizable"})[0]["version"] == "1.5"
        forward_ok = result["status"] == "verified" and (target / "02-assisted" / "README.md").read_bytes() == b"new\n" and (target / "02-assisted" / "VERSION").read_bytes() == b"1.5\n" and (target / MANIFEST_PATH).is_file() and target_verified
        protected_ok = protected_before == protected_after

        next_source = base / "next-source"
        next_source.mkdir()
        (next_source / "02-assisted").mkdir()
        (next_source / "02-assisted" / "README.md").write_bytes(b"old\n")
        (next_source / "02-assisted" / "PROJECT.md").write_bytes(b"project-owned\n")
        execute_forward(fixture_source, next_source, prior, prior_raw, base / "operation-next-source", state_home=state_home)
        next_target = base / "next-target"
        next_target.mkdir()
        (next_target / "02-assisted").mkdir()
        (next_target / "02-assisted" / "README.md").write_bytes(b"old\n")
        (next_target / "02-assisted" / "PROJECT.md").write_bytes(b"private-next\n")
        next_source_ok = verify_release_root(next_source, {"downstream"})[0]["version"] == "1.5" and compare_release(next_source, next_target, prior, prior_raw)["state"] == "comparison-only"
        partial_target = base / "partial-target"
        shutil.copytree(target, partial_target)
        (partial_target / "02-assisted" / "README.md").write_bytes(b"old\n")
        (partial_target / "02-assisted" / "VERSION").unlink()
        partial_report = base / "operation-partial" / "terminal.json"
        try:
            execute_forward(fixture_source, partial_target, prior, prior_raw, base / "operation-partial", inject_after=1, state_home=state_home)
            partial_ok = False
        except MaintenanceError:
            first_hash = file_digest(partial_report)
            first = load_json(partial_report, "partial terminal")
            partial_ok = first["status"] == "partial" and file_digest(partial_report) == first_hash
        recovered = execute_forward(fixture_source, partial_target, prior, prior_raw, base / "operation-recovery", recover_from=partial_report, state_home=state_home)
        recovery_ok = recovered["status"] == "verified" and recovered["recover_from"] is not None
        drift_target = base / "drift-target"
        shutil.copytree(target, drift_target)
        (drift_target / "02-assisted" / "README.md").write_bytes(b"old\n")
        try:
            execute_forward(fixture_source, drift_target, prior, prior_raw, base / "operation-drift", inject_drift="work/private.txt", state_home=state_home)
            drift_ok = False
        except MaintenanceError as exc:
            drift_ok = "zero maintenance writes" in str(exc) and (drift_target / "02-assisted" / "README.md").read_bytes() == b"old\n"

        link = base / "operation-link"
        link_created = False
        if os.name == "nt":
            link_created = subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(target)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
        else:
            os.symlink(target, link, target_is_directory=True)
            link_created = True
        before_link_attack = tree_state(target)
        try:
            execute_forward(fixture_source, target, prior, prior_raw, link / "escaped-operation", state_home=state_home)
            operation_link_ok = False
        except MaintenanceError:
            operation_link_ok = link_created and before_link_attack == tree_state(target) and not (target / "escaped-operation").exists()
        finally:
            if link_created:
                if link.is_symlink():
                    link.unlink()
                else:
                    os.rmdir(link)

        private_a = {"schema": REPORT_SCHEMA, "status": "verified", "operation_id": "a" * 32, "changes": 1, "recover_from": None}
        private_b = {"schema": REPORT_SCHEMA, "status": "verified", "operation_id": "b" * 32, "changes": 2, "recover_from": None}
        projection_a = canonical(public_projection(private_a, False))
        projection_b = canonical(public_projection(private_b, False))
        privacy_ok = projection_a == projection_b and all(secret not in projection_a for secret in (b"operation_id", b"recover_from", b"changes"))
        public_before = tree_state(fixture_source)
        private_file = write_private_operation_fixture(base / "private-operation-a", "a" * 32, 1)
        reverse = reverse_candidate(private_file, base / "candidate", base / "candidate", [fixture_source, source, target], False)
        reverse_ok = reverse["requires_independent_review"] and public_before == tree_state(fixture_source)

        fake_root = base / "fake-operation"
        fake_root.mkdir()
        (fake_root / "terminal.json").write_bytes(canonical({"schema": REPORT_SCHEMA, "status": "verified"}))
        (fake_root / "journal.ndjson").write_bytes(b"{}\n")
        try:
            reverse_candidate(fake_root / "terminal.json", base / "fake-candidate", base / "fake-candidate", [fixture_source, source, target], False)
            fake_report_ok = False
        except MaintenanceError:
            fake_report_ok = not (base / "fake-candidate").exists()
        private_b_file = write_private_operation_fixture(base / "private-operation-b", "b" * 32, 2)
        try:
            reverse_candidate(private_b_file, fixture_source / "public-mutation", fixture_source / "public-mutation", [fixture_source, source, target], False)
            public_root_ok = False
        except MaintenanceError:
            public_root_ok = not (fixture_source / "public-mutation").exists()
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
    for name in ("tfw-plan", "tfw-handoff", "tfw-review", "tfw-update", "tfw-identity"):
        skill = source / "02-assisted" / ".agents" / "skills" / name / "SKILL.md"
        metadata = skill.parent / "agents" / "openai.yaml"
        roles[name] = skill.is_file() and metadata.is_file() and len(skill.read_text(encoding="utf-8")) > 300
    role_tabletop = role_scenario_matrix()
    results = {
        "V1": bool(records) and all(hostile.values()) and all(completeness.values()),
        "V2": agreement["classified"] and digest(PRIOR_10.encode()) == policy["accepted_priors"][0]["manifest_sha256"],
        "V3": drift_ok and operation_link_ok and all(contention.values()),
        "V4": partial_ok and recovery_ok,
        "V5": protected_ok,
        "V6": privacy_ok and fake_report_ok and public_root_ok,
        "V7": identity_result["V7"],
        "V8": identity_result["V8"],
        "V9": template_result["ok"],
        "V10": all(agreement.values()),
        "V11": all(roles.values()) and role_tabletop["ok"],
        "V12": forward_ok and next_source_ok and reverse_ok,
    }
    return {
        "schema": "tfw-assisted-verification-v1",
        "release_manifest_sha256": digest(manifest_raw),
        "policy_sha256": file_digest(source / POLICY_PATH),
        "results": results,
        "details": {"manifest_hostile": completeness, "role_tabletop": role_tabletop, "same_target_contention": contention, "operation_link_rejected": operation_link_ok, "reverse_hostile": {"fake_report": fake_report_ok, "public_root": public_root_ok}, "forward_next_source": next_source_ok},
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
    reverse.add_argument("--candidate-root", required=True)
    reverse.add_argument("--approve-candidate-root", required=True)
    reverse.add_argument("--public-root", required=True)
    reverse.add_argument("--source-root", required=True)
    reverse.add_argument("--target-root", required=True)
    reverse.add_argument("--suppressed", action="store_true")
    return top


def run(args: argparse.Namespace):
    if args.command == "manifest":
        return manifest_for_source(Path(args.source_root).resolve(strict=True))
    if args.command == "verify-release":
        source = Path(args.source_root).resolve(strict=True)
        _, _, policy, manifest_raw = verify_release_root(source, {"downstream", "customizable"})
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
    return reverse_candidate(
        Path(args.private_report),
        Path(args.candidate_root),
        Path(args.approve_candidate_root),
        [Path(args.public_root), Path(args.source_root), Path(args.target_root)],
        args.suppressed,
    )


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
