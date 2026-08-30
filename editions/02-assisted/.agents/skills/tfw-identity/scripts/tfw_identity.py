#!/usr/bin/env python3
"""Fail-closed participant profiles and machine-local Assisted bindings."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
import unicodedata
import uuid


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PRODUCT = "tfw-assisted"
SCHEMA = "tfw-assisted-bindings-v1"
HANDLE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,47}$")
UUID = re.compile(r"^project_id:\s*([0-9a-fA-F-]{36})\s*$")
FIELD = {
    "identifier": re.compile(r"^\s*(?:-\s*)?Идентификатор:\s*(\S+)\s*$"),
    "display_name": re.compile(r"^\s*(?:-\s*)?Отображаемое имя:\s*(.+?)\s*$"),
    "type": re.compile(r"^\s*(?:-\s*)?Тип:\s*(\S+)\s*$"),
    "organization_role": re.compile(r"^\s*(?:-\s*)?Роль в организации:\s*(.+?)\s*$"),
    "project_role": re.compile(r"^\s*(?:-\s*)?Роль в проекте:\s*(.+?)\s*$"),
}
PROVIDERS = {"google drive", "shared drives", "my drive", "onedrive", "dropbox", "sharepoint"}
TRANSLIT = str.maketrans({
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e",
    "ж": "zh", "з": "z", "и": "i", "й": "i", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch",
    "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
    "ә": "a", "ғ": "g", "қ": "q", "ң": "n", "ө": "o", "ұ": "u", "ү": "u",
    "һ": "h", "і": "i",
})


class IdentityError(Exception):
    """An unsafe or ambiguous condition which must not be guessed through."""


def emit(value: dict) -> None:
    print(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")))


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normal(value: str) -> str:
    return unicodedata.normalize("NFKC", value).casefold().strip()


def inside(child: Path, parent: Path) -> bool:
    try:
        return os.path.commonpath([os.path.normcase(str(child)), os.path.normcase(str(parent))]) == os.path.normcase(str(parent))
    except ValueError:
        return False


def root_path(value: str) -> Path:
    root = Path(value).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise IdentityError("project root is not a directory")
    return root


def project_state(root: Path) -> tuple[str, str | None]:
    try:
        lines = (root / "PROJECT.md").read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeError) as exc:
        raise IdentityError("PROJECT.md is unavailable") from exc
    initialized = ["НЕ ИНИЦИАЛИЗИРОВАН" in line for line in lines if "Состояние:" in line]
    if len(initialized) != 1:
        raise IdentityError("PROJECT.md must contain exactly one state")
    ids = [m.group(1) for line in lines if (m := UUID.search(line))]
    if initialized[0]:
        if ids:
            raise IdentityError("uninitialized project must not contain project_id")
        return "uninitialized", None
    if len(ids) != 1:
        raise IdentityError("initialized project must contain one project_id")
    try:
        project_id = str(uuid.UUID(ids[0]))
    except ValueError as exc:
        raise IdentityError("project_id is invalid") from exc
    if project_id != ids[0].lower():
        raise IdentityError("project_id is not canonical")
    return "initialized", project_id


def profile_fields(path: Path) -> dict[str, str]:
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeError) as exc:
        raise IdentityError("profile is unreadable") from exc
    found = {key: [] for key in FIELD}
    for line in lines:
        for key, pattern in FIELD.items():
            if match := pattern.match(line):
                found[key].append(match.group(1).strip())
    if any(len(values) != 1 for values in found.values()):
        raise IdentityError(f"profile fields are missing or duplicated: {path.name}")
    return {key: values[0] for key, values in found.items()}


def profiles(root: Path) -> dict[str, dict[str, str]]:
    folder = root / "people"
    result: dict[str, dict[str, str]] = {}
    names: set[str] = set()
    if not folder.is_dir():
        return result
    for path in sorted(folder.glob("*.md"), key=lambda item: item.name.casefold()):
        if path.name.casefold() == "readme.md":
            continue
        fields = profile_fields(path)
        if normal(fields["type"]) != "человек":
            continue
        identifier = fields["identifier"]
        if not HANDLE.fullmatch(identifier) or path.stem != identifier or identifier in result:
            raise IdentityError(f"invalid or duplicate profile identifier: {path.name}")
        display = normal(fields["display_name"])
        if display in names:
            raise IdentityError("duplicate normalized display name")
        names.add(display)
        result[identifier] = fields
    return result


def people_manifest(root: Path) -> tuple[str, list[dict]]:
    entries = []
    folder = root / "people"
    if folder.is_dir():
        for path in sorted(folder.glob("*.md"), key=lambda item: item.name.casefold()):
            entries.append({"path": path.name, "size": path.stat().st_size, "sha256": file_sha(path)})
    encoded = "".join(f"{e['path']}\t{e['size']}\t{e['sha256']}\n" for e in entries).encode()
    return sha(encoded), entries


def surname_id(display: str, surname: str, disambiguator: str | None) -> str:
    words = re.findall(r"[^\W_]+", normal(display), flags=re.UNICODE)
    surname_words = re.findall(r"[^\W_]+", normal(surname), flags=re.UNICODE)
    if len(words) < 2 or not surname_words or not any(words[i:i + len(surname_words)] == surname_words for i in range(len(words))):
        raise IdentityError("an explicit surname within the full name is required")

    def slug(value: str) -> str:
        raw = unicodedata.normalize("NFKD", normal(value).translate(TRANSLIT)).encode("ascii", "ignore").decode()
        return re.sub(r"[^a-z0-9]+", "-", raw).strip("-")

    base = slug(surname)
    if not base:
        raise IdentityError("surname cannot form a portable identifier")
    if disambiguator:
        dis = normal(disambiguator)
        if dis not in words:
            raise IdentityError("disambiguator must be present in the full name")
        base += "-" + slug(disambiguator)
    candidate = base[:48].rstrip("-")
    if not HANDLE.fullmatch(candidate):
        raise IdentityError("surname identifier is invalid")
    return candidate


def render_profile(identifier: str, display: str, organization_role: str, project_role: str) -> bytes:
    values = [display.strip(), organization_role.strip(), project_role.strip()]
    if any(not value or "\n" in value or "\r" in value for value in values):
        raise IdentityError("profile values must be non-empty single lines")
    return (
        "# Профиль участника\n\n"
        f"Идентификатор: {identifier}\n"
        f"Отображаемое имя: {values[0]}\n"
        "Тип: человек\n"
        f"Роль в организации: {values[1]}\n"
        f"Роль в проекте: {values[2]}\n"
    ).encode()


def create_profile(args: argparse.Namespace, root: Path) -> dict:
    if not re.fullmatch(r"[0-9a-f]{64}", args.expected_manifest):
        raise IdentityError("expected manifest is invalid")
    before_hash, before = people_manifest(root)
    if before_hash != args.expected_manifest:
        raise IdentityError("people manifest changed")
    known = profiles(root)
    same = [key for key, value in known.items() if normal(value["display_name"]) == normal(args.display_name)]
    if len(same) == 1:
        return {"state": "exists", "participant": same[0], "people_manifest": before_hash}
    identifier = surname_id(args.display_name, args.surname, args.disambiguator)
    if identifier in known:
        raise IdentityError("surname identifier collision; clarify before writing")
    folder = root / "people"
    if not folder.is_dir():
        raise IdentityError("people directory is unavailable")
    target = folder / f"{identifier}.md"
    content = render_profile(identifier, args.display_name, args.organization_role, args.project_role)
    try:
        with target.open("xb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        after_hash, after = people_manifest(root)
        before_map = {e["path"]: e for e in before}
        after_map = {e["path"]: e for e in after}
        if any(after_map.get(key) != value for key, value in before_map.items()) or file_sha(target) != sha(content):
            raise IdentityError("profile post-read mismatch")
    except Exception:
        if target.exists() and file_sha(target) == sha(content):
            target.unlink()
        raise
    return {"state": "created", "participant": identifier, "people_manifest": after_hash}


def default_store() -> Path:
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA")
        if not base:
            raise IdentityError("LOCALAPPDATA is unavailable")
        return Path(base) / PRODUCT / "bindings.json"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / PRODUCT / "bindings.json"
    return Path(os.environ.get("XDG_STATE_HOME", str(Path.home() / ".local" / "state"))) / PRODUCT / "bindings.json"


def component_chain(path: Path) -> list[Path]:
    absolute = path.absolute()
    chain: list[Path] = []
    current = absolute
    while True:
        chain.append(current)
        if current.parent == current:
            break
        current = current.parent
    return list(reversed(chain))


def existing_parent(path: Path) -> Path:
    current = path
    while not current.exists():
        if current.parent == current:
            raise IdentityError("local store has no existing ancestor")
        current = current.parent
    return current


def provider_roots(project: Path, declared: list[str]) -> list[Path]:
    roots = [project.resolve(strict=True)]
    for key in ("OneDrive", "OneDriveCommercial", "OneDriveConsumer", "GOOGLE_DRIVE", "DROPBOX"):
        if os.environ.get(key):
            roots.append(Path(os.environ[key]).expanduser().resolve(strict=True))
    for value in declared:
        roots.append(Path(value).expanduser().resolve(strict=True))
    for index, part in enumerate(project.parts):
        if part.casefold() in PROVIDERS:
            roots.append(Path(*project.parts[:index + 1]).resolve(strict=True))
    return roots


def pinned_chain(path: Path) -> list[tuple[str, int, int]]:
    baseline = []
    device = None
    for component in component_chain(path):
        info = os.lstat(component)
        if stat.S_ISLNK(info.st_mode) or (getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)):
            raise IdentityError("ancestor is link or reparse point")
        if not stat.S_ISDIR(info.st_mode):
            raise IdentityError("ancestor is not a directory")
        if device is None:
            device = info.st_dev
        elif os.name != "nt" and info.st_dev != device:
            raise IdentityError("mount boundary is not supported")
        baseline.append((os.path.normcase(str(component)), info.st_dev, info.st_ino))
    return baseline


def windows_acl(path: Path) -> dict:
    program = r'''
$ErrorActionPreference = 'Stop'
$acl = Get-Acl -LiteralPath $env:TFW_ASSISTED_ACL_PATH
$identity = [Security.Principal.WindowsIdentity]::GetCurrent()
$owner = ([Security.Principal.NTAccount]$acl.Owner).Translate([Security.Principal.SecurityIdentifier]).Value
$rules = @($acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier]) | ForEach-Object {
  [PSCustomObject]@{ sid=$_.IdentityReference.Value; type=$_.AccessControlType.ToString(); rights=$_.FileSystemRights.ToString() }
})
[PSCustomObject]@{ current=$identity.User.Value; owner=$owner; rules=$rules } | ConvertTo-Json -Depth 4 -Compress
'''
    environment = dict(os.environ)
    environment["TFW_ASSISTED_ACL_PATH"] = str(path)
    try:
        result = subprocess.run(["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", program], env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", timeout=10)
        if result.returncode != 0:
            raise IdentityError("Windows ACL probe failed")
        return json.loads(result.stdout)
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError) as exc:
        raise IdentityError("Windows ACL probe failed") from exc


def private_permissions(path: Path) -> None:
    try:
        info = os.lstat(path)
        if os.name == "nt":
            acl = windows_acl(path)
            allowed = {acl["current"], "S-1-3-4", "S-1-5-18", "S-1-5-32-544"}
            grants = [rule for rule in acl["rules"] if rule["type"] == "Allow"]
            if acl["owner"] != acl["current"] or not any(rule["sid"] == acl["current"] and "FullControl" in rule["rights"] for rule in grants) or any(rule["sid"] not in allowed for rule in grants) or any(rule["type"] == "Deny" and rule["sid"] == acl["current"] for rule in acl["rules"]):
                raise IdentityError("private Windows ACL/owner proof failed")
        else:
            if info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
                raise IdentityError("private Unix owner/mode proof failed")
    except IdentityError:
        raise
    except OSError as exc:
        raise IdentityError("private permission probe failed") from exc


def secure_namespace(path: Path) -> None:
    if os.name == "nt":
        acl = windows_acl(path)
        result = subprocess.run(["icacls", str(path), "/inheritance:r", "/grant:r", f"*{acl['current']}:(OI)(CI)F"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
        if result.returncode != 0:
            raise IdentityError("private Windows ACL setup failed")
    else:
        os.chmod(path, 0o700)
    private_permissions(path)


def locality(store: Path, project: Path, declared: list[str], asserted: bool) -> dict:
    if not asserted:
        return {"state": "unknown", "reason": "local ownership was not asserted"}
    if not store.is_absolute() or store.name != "bindings.json" or store.parent.name != PRODUCT:
        return {"state": "unsafe", "reason": "store is outside the Assisted namespace"}
    try:
        candidate = store.absolute()
        if any(inside(candidate, root) for root in provider_roots(project, declared)):
            return {"state": "unsafe", "reason": "store is inside project or shared root"}
        namespace_exists = candidate.parent.exists()
        parent = candidate.parent if namespace_exists else existing_parent(candidate.parent)
        baseline = pinned_chain(parent)
        if namespace_exists:
            private_permissions(candidate.parent)
            if candidate.exists():
                private_permissions(candidate)
            lock = candidate.with_suffix(".lock")
            if lock.exists():
                private_permissions(lock)
        return {"state": "proven", "pin": baseline, "existing_parent": parent, "namespace_missing": not namespace_exists}
    except IdentityError as exc:
        return {"state": "unsafe" if "link or reparse" in str(exc) else "unknown", "reason": str(exc)}
    except (OSError, ValueError):
        return {"state": "unknown", "reason": "locality probe failed"}


def reprobe(decision: dict) -> None:
    if decision.get("state") != "proven":
        raise IdentityError("operational-local-v1 is not proven")
    for raw, device, inode in decision["pin"]:
        info = os.lstat(Path(raw))
        if info.st_dev != device or info.st_ino != inode:
            raise IdentityError("locality evidence changed")
        if stat.S_ISLNK(info.st_mode) or (getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)):
            raise IdentityError("locality component changed")


def parse_registry(data: bytes) -> list[dict]:
    try:
        value = json.loads(data.decode("utf-8"), object_pairs_hook=lambda pairs: pairs)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise IdentityError("registry is corrupt") from exc

    def unique(pairs, where):
        if not isinstance(pairs, list) or any(not isinstance(item, tuple) for item in pairs):
            raise IdentityError(f"registry {where} is not an object")
        result = {}
        for key, value in pairs:
            if key in result:
                raise IdentityError("registry contains duplicate keys")
            result[key] = value
        return result

    root = unique(value, "root")
    if set(root) != {"schema", "bindings"} or root["schema"] != SCHEMA or not isinstance(root["bindings"], list):
        raise IdentityError("registry schema is invalid")
    bindings = []
    seen = set()
    for raw in root["bindings"]:
        item = unique(raw, "binding")
        if set(item) not in ({"project_id", "mode"}, {"project_id", "mode", "participant"}):
            raise IdentityError("binding fields are invalid")
        try:
            project_id = str(uuid.UUID(item["project_id"]))
        except (ValueError, TypeError) as exc:
            raise IdentityError("binding project_id is invalid") from exc
        if project_id in seen or item["project_id"] != project_id:
            raise IdentityError("binding project_id is duplicate or noncanonical")
        if item["mode"] == "ask" and set(item) != {"project_id", "mode"}:
            raise IdentityError("ask binding has participant")
        if item["mode"] == "fixed" and (set(item) != {"project_id", "mode", "participant"} or not HANDLE.fullmatch(item["participant"])):
            raise IdentityError("fixed binding is invalid")
        if item["mode"] not in {"ask", "fixed"}:
            raise IdentityError("binding mode is invalid")
        seen.add(project_id)
        bindings.append(item)
    return bindings


def registry_bytes(bindings: list[dict]) -> bytes:
    return (json.dumps({"schema": SCHEMA, "bindings": bindings}, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def read_registry(store: Path) -> tuple[list[dict], bool]:
    if not store.exists():
        return [], False
    if store.is_symlink() or not store.is_file():
        raise IdentityError("registry is not a regular file")
    return parse_registry(store.read_bytes()), True


@contextmanager
def live_lock(path: Path):
    if path.exists() and (path.is_symlink() or not path.is_file()):
        raise IdentityError("registry lock is not a regular file")
    created = not path.exists()
    stream = None
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_RDWR, 0o600)
        stream = os.fdopen(descriptor, "r+b", buffering=0)
        stream.seek(0)
        if stream.read(1) == b"":
            stream.write(b"0")
            stream.flush()
            os.fsync(stream.fileno())
        stream.seek(0)
        if os.name == "nt":
            import msvcrt
            try:
                msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
            except OSError as exc:
                raise IdentityError("registry has a live foreign lock") from exc
        else:
            import fcntl
            try:
                fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError as exc:
                raise IdentityError("registry has a live foreign lock") from exc
    except IdentityError:
        if stream is not None:
            stream.close()
        if created:
            path.unlink(missing_ok=True)
        raise
    except OSError as exc:
        if stream is not None:
            stream.close()
        if created:
            path.unlink(missing_ok=True)
        raise IdentityError("registry has a live foreign lock") from exc
    try:
        yield
    finally:
        try:
            if os.name == "nt":
                import msvcrt
                stream.seek(0)
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)
        except OSError:
            pass
        if stream is not None:
            stream.close()
        if created:
            try:
                path.unlink()
            except OSError:
                pass


def update_registry(store: Path, decision: dict, replacement: dict) -> dict:
    before, existed = read_registry(store)
    created_dir = not store.parent.exists()
    temporary = None
    try:
        reprobe(decision)
        store.parent.mkdir(mode=0o700, parents=False, exist_ok=True)
        if created_dir:
            secure_namespace(store.parent)
        full_pin = pinned_chain(store.parent)
        private_permissions(store.parent)
        decision = {**decision, "pin": full_pin, "existing_parent": store.parent, "namespace_missing": False}
        reprobe(decision)
        with live_lock(store.with_suffix(".lock")):
            reprobe(decision)
            private_permissions(store.parent)
            private_permissions(store.with_suffix(".lock"))
            locked, locked_existed = read_registry(store)
            updated = [item for item in locked if item["project_id"] != replacement["project_id"]] + [replacement]
            fd, raw = tempfile.mkstemp(prefix="bindings-", suffix=".tmp", dir=store.parent)
            temporary = Path(raw)
            with os.fdopen(fd, "wb") as stream:
                stream.write(registry_bytes(updated))
                stream.flush()
                os.fsync(stream.fileno())
            os.chmod(temporary, 0o600)
            private_permissions(temporary)
            reprobe(decision)
            os.replace(temporary, store)
            temporary = None
            private_permissions(store)
            if read_registry(store)[0] != updated:
                raise IdentityError("registry post-read mismatch")
        return {"state": "updated", "mode": replacement["mode"], "store_preexisted": existed or locked_existed}
    except Exception:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        if created_dir:
            try:
                store.parent.rmdir()
            except OSError:
                pass
        raise


def resolve_text(text: str, known: dict[str, dict[str, str]]) -> dict:
    value = normal(text)
    if any(word in value.split() for word in ("общий", "shared")):
        return {"state": "resolved", "mode": "ask"}
    matches = [key for key, profile in known.items() if normal(key) in value or normal(profile["display_name"]) in value]
    if len(matches) == 1:
        return {"state": "resolved", "mode": "fixed", "participant": matches[0]}
    return {"state": "ambiguous" if matches else "new_or_unknown"}


def self_test() -> dict:
    checks = {}
    provider_environment = {key: os.environ.pop(key, None) for key in ("OneDrive", "OneDriveCommercial", "OneDriveConsumer", "GOOGLE_DRIVE", "DROPBOX")}
    try:
        temporary = tempfile.TemporaryDirectory(prefix="tfw-assisted-identity-")
        raw = temporary.name
        base = Path(raw)
        root = base / "project"
        (root / "people").mkdir(parents=True)
        (root / "PROJECT.md").write_text("Состояние: ИНИЦИАЛИЗИРОВАН\nproject_id: 00000000-0000-4000-8000-000000000001\n", encoding="utf-8")
        store = base / "local" / PRODUCT / "bindings.json"
        store.parent.parent.mkdir()
        decision = locality(store, root, [], True)
        checks["locality_proven"] = decision["state"] == "proven"
        if checks["locality_proven"]:
            result = update_registry(store, decision, {"project_id": "00000000-0000-4000-8000-000000000001", "mode": "ask"})
            checks["write_and_postread"] = result["state"] == "updated" and len(parse_registry(store.read_bytes())) == 1
            try:
                full_decision = locality(store, root, [], True)
                private_permissions(store.parent)
                private_permissions(store)
                checks["private_acl_and_full_namespace_pin"] = full_decision["state"] == "proven" and len(full_decision["pin"]) > len(decision["pin"]) and Path(full_decision["pin"][-1][0]).name == PRODUCT
            except IdentityError:
                checks["private_acl_and_full_namespace_pin"] = False
        unsafe = root / PRODUCT / "bindings.json"
        before = sorted(str(p.relative_to(root)) for p in root.rglob("*"))
        checks["project_store_rejected"] = locality(unsafe, root, [], True)["state"] == "unsafe"
        checks["unsafe_zero_write"] = before == sorted(str(p.relative_to(root)) for p in root.rglob("*"))
        checks["unknown_without_assertion"] = locality(store, root, [], False)["state"] == "unknown"
        checks["surname_cyrillic"] = surname_id("Анна Кузнецова", "Кузнецова", None) == "kuznetsova"
        checks["surname_latin"] = surname_id("Maria Smith", "Smith", None) == "smith"
        checks["surname_collision_stops"] = surname_id("Anna Smith", "Smith", None) == surname_id("Maria Smith", "Smith", None)
        cardinalities = []
        people = root / "people"
        for count in (0, 1, 3, 24):
            for profile in people.glob("*.md"):
                profile.unlink()
            for index in range(count):
                identifier = f"person-{index}"
                (people / f"{identifier}.md").write_bytes(render_profile(identifier, f"Person {index} Smith", "не указана", "не указана"))
            cardinalities.append(len(profiles(root)) == count)
        checks["profile_cardinalities"] = all(cardinalities)
        for profile in people.glob("*.md"):
            profile.unlink()
        legacy = "legacy_alias"
        (people / f"{legacy}.md").write_bytes(render_profile(legacy, "Legacy Person", "не указана", "не указана"))
        checks["legacy_identifier_preserved"] = list(profiles(root)) == [legacy]
        try:
            parse_registry(b'{"schema":"tfw-assisted-bindings-v1","schema":"x","bindings":[]}')
            checks["duplicate_registry_rejected"] = False
        except IdentityError:
            checks["duplicate_registry_rejected"] = True
        valid_fixed = registry_bytes([{"project_id": "00000000-0000-4000-8000-000000000001", "mode": "fixed", "participant": legacy}])
        valid_ask = registry_bytes([{"project_id": "00000000-0000-4000-8000-000000000001", "mode": "ask"}])
        checks["fixed_and_ask_bindings"] = parse_registry(valid_fixed)[0]["mode"] == "fixed" and parse_registry(valid_ask)[0]["mode"] == "ask"
        invalid_cases = [
            b'{"bindings":[{"mode":"fixed","participant":"bad space","project_id":"00000000-0000-4000-8000-000000000001"}],"schema":"tfw-assisted-bindings-v1"}\n',
            b'{"bindings":[{"mode":"ask","project_id":"00000000-0000-4000-8000-000000000001"},{"mode":"ask","project_id":"00000000-0000-4000-8000-000000000001"}],"schema":"tfw-assisted-bindings-v1"}\n',
        ]
        rejected = 0
        for case in invalid_cases:
            try:
                parse_registry(case)
            except IdentityError:
                rejected += 1
        checks["invalid_and_duplicate_bindings"] = rejected == len(invalid_cases)
        checks["missing_binding_selects_nobody"] = not any(item["project_id"] == "00000000-0000-4000-8000-000000000099" for item in parse_registry(valid_ask))
        shared = locality(store, root, [str(store.parent.parent)], True)
        checks["declared_shared_store_rejected"] = shared["state"] == "unsafe"

        permissive_parent = base / "permissive"
        permissive_namespace = permissive_parent / PRODUCT
        permissive_namespace.mkdir(parents=True)
        if os.name == "nt":
            subprocess.run(["icacls", str(permissive_namespace), "/grant", "*S-1-1-0:(OI)(CI)R"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        else:
            os.chmod(permissive_namespace, 0o770)
        permissive_store = permissive_namespace / "bindings.json"
        permissive_before = sorted(str(path.relative_to(permissive_parent)) for path in permissive_parent.rglob("*"))
        permissive_result = locality(permissive_store, root, [], True)
        checks["permissive_acl_zero_write"] = permissive_result["state"] == "unknown" and permissive_before == sorted(str(path.relative_to(permissive_parent)) for path in permissive_parent.rglob("*")) and not permissive_store.exists()

        substitution_parent = base / "substitution"
        substitution_namespace = substitution_parent / PRODUCT
        substitution_namespace.mkdir(parents=True)
        secure_namespace(substitution_namespace)
        substitution_pin = pinned_chain(substitution_namespace)
        held_namespace = substitution_parent / "held"
        os.replace(substitution_namespace, held_namespace)
        if os.name == "nt":
            linked = subprocess.run(["cmd", "/c", "mklink", "/J", str(substitution_namespace), str(held_namespace)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
        else:
            os.symlink(held_namespace, substitution_namespace, target_is_directory=True)
            linked = True
        try:
            reprobe({"state": "proven", "pin": substitution_pin})
            substitution_rejected = False
        except IdentityError:
            substitution_rejected = linked
        checks["namespace_substitution_zero_write"] = substitution_rejected and not any(path.name.startswith("bindings") for path in held_namespace.rglob("*")) and not (held_namespace / "bindings.lock").exists()
        if linked:
            if substitution_namespace.is_symlink():
                substitution_namespace.unlink()
            else:
                os.rmdir(substitution_namespace)
        registry_before_lock = file_sha(store)
        try:
            with live_lock(store.with_suffix(".lock")):
                with live_lock(store.with_suffix(".lock")):
                    pass
            checks["live_foreign_lock_rejected"] = False
        except IdentityError:
            checks["live_foreign_lock_rejected"] = file_sha(store) == registry_before_lock
        original_registry = store.read_bytes()
        store.write_bytes(b"corrupt\n")
        corrupt_before = file_sha(store)
        try:
            read_registry(store)
            checks["corrupt_registry_zero_write"] = False
        except IdentityError:
            checks["corrupt_registry_zero_write"] = file_sha(store) == corrupt_before
        store.write_bytes(original_registry)
        original_lstat = os.lstat

        class ReparseProxy:
            def __init__(self, value):
                self._value = value
                self.st_file_attributes = getattr(value, "st_file_attributes", 0) | getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)

            def __getattr__(self, name):
                return getattr(self._value, name)

        flagged = decision["existing_parent"]

        def reparse_lstat(value):
            observed = original_lstat(value)
            return ReparseProxy(observed) if Path(value) == flagged else observed

        try:
            os.lstat = reparse_lstat
            checks["reparse_component_rejected"] = locality(store, root, [], True)["state"] == "unsafe"
        finally:
            os.lstat = original_lstat
        full = base / "tfw" / "bindings.json"
        checks["full_namespace_rejected"] = locality(full, root, [], True)["state"] == "unsafe"
        moved = base / "local-moved"
        os.replace(store.parent.parent, moved)
        store.parent.parent.mkdir()
        try:
            reprobe(decision)
            checks["pinned_root_swap_rejected"] = False
        except IdentityError:
            checks["pinned_root_swap_rejected"] = True
        temporary.cleanup()
    finally:
        for key, value in provider_environment.items():
            if value is not None:
                os.environ[key] = value
    v8 = ("locality_proven", "write_and_postread", "private_acl_and_full_namespace_pin", "project_store_rejected", "unsafe_zero_write", "unknown_without_assertion", "declared_shared_store_rejected", "permissive_acl_zero_write", "namespace_substitution_zero_write", "live_foreign_lock_rejected", "reparse_component_rejected", "pinned_root_swap_rejected")
    return {"V7": all(checks.values()), "V8": all(checks[key] for key in v8), "checks": checks}


def parser() -> argparse.ArgumentParser:
    top = argparse.ArgumentParser(description=__doc__)
    subs = top.add_subparsers(dest="command", required=True)
    for name in ("inspect", "profile-manifest", "resolve", "create-profile", "status", "set-fixed", "set-ask"):
        item = subs.add_parser(name)
        item.add_argument("--project-root", required=True)
        if name in {"status", "set-fixed", "set-ask"}:
            item.add_argument("--store")
            item.add_argument("--shared-root", action="append", default=[])
            item.add_argument("--assert-local", action="store_true")
        if name == "resolve":
            item.add_argument("--input", required=True)
        if name == "create-profile":
            item.add_argument("--expected-manifest", required=True)
            item.add_argument("--display-name", required=True)
            item.add_argument("--surname", required=True)
            item.add_argument("--disambiguator")
            item.add_argument("--organization-role", required=True)
            item.add_argument("--project-role", required=True)
        if name == "set-fixed":
            item.add_argument("--participant", required=True)
    subs.add_parser("self-test")
    return top


def run(args: argparse.Namespace) -> dict:
    if args.command == "self-test":
        return self_test()
    root = root_path(args.project_root)
    state, project_id = project_state(root)
    known = profiles(root)
    manifest, entries = people_manifest(root)
    if args.command == "inspect":
        return {"state": state, "project_id": project_id, "human_profiles": len(known), "people_manifest": manifest}
    if args.command == "profile-manifest":
        return {"state": "ok", "profiles": len(known), "people_manifest": manifest, "entries": entries}
    if args.command == "resolve":
        if len(known) == 1:
            only = next(iter(known))
            return {"state": "one_profile", "mode": "fixed", "participant": only}
        return resolve_text(args.input, known)
    if args.command == "create-profile":
        return create_profile(args, root)
    if state != "initialized" or project_id is None:
        return {"state": "uninitialized", "human_profiles": len(known)}
    store = Path(args.store).expanduser().absolute() if args.store else default_store().absolute()
    decision = locality(store, root, args.shared_root, args.assert_local)
    if decision["state"] != "proven":
        return {"state": "session_only", "locality": decision["state"], "reason": decision["reason"]}
    bindings, _ = read_registry(store)
    current = next((item for item in bindings if item["project_id"] == project_id), None)
    if args.command == "status":
        reprobe(decision)
        if not store.parent.exists():
            if len(known) == 1:
                return {"state": "one_profile", "mode": "fixed", "participant": next(iter(known))}
            return {"state": "missing"}
        with live_lock(store.with_suffix(".lock")):
            reprobe(decision)
            locked, _ = read_registry(store)
            current = next((item for item in locked if item["project_id"] == project_id), None)
            if current is None:
                if len(known) == 1:
                    return {"state": "one_profile", "mode": "fixed", "participant": next(iter(known))}
                return {"state": "missing"}
            if current["mode"] == "fixed" and current["participant"] not in known:
                raise IdentityError("binding references an unknown participant")
            return {"state": current["mode"], "participant": current.get("participant")}
    if args.command == "set-fixed":
        if args.participant not in known:
            raise IdentityError("participant is not a valid human profile")
        replacement = {"project_id": project_id, "mode": "fixed", "participant": args.participant}
    else:
        replacement = {"project_id": project_id, "mode": "ask"}
    return update_registry(store, decision, replacement)


def main() -> int:
    try:
        emit(run(parser().parse_args()))
        return 0
    except IdentityError as exc:
        emit({"state": "error", "reason": str(exc)})
        return 4
    except Exception as exc:
        emit({"state": "error", "reason": f"unexpected failure: {type(exc).__name__}"})
        return 5


if __name__ == "__main__":
    sys.exit(main())
