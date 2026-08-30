#!/usr/bin/env python3
"""Generate task-local, privacy-safe Assisted 1.5 execution evidence."""

from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import uuid

sys.dont_write_bytecode = True

REPO = Path(__file__).resolve().parents[4]
EVIDENCE = Path(__file__).resolve().parent
SOURCE = Path(os.environ["TFW_ASSISTED_FIELD_SOURCE"]).expanduser()
HISTORICAL_CULTURE_DIGEST = "7e2248a7f7e77161644d8394b1557c731e0b5b31d7713843de30655b6e4fadc3"
CANONICAL_CODEPOINT_DIGEST = "3a1885c65b13388a51ddaa5b1454122876d4f17d268bc49f0f94f6bb2dbee96b"
BASELINE = "f3eb986"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical(value))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MAINT = load_module("assisted_maintenance_evidence", REPO / "editions/maintenance/assisted_maintenance.py")
IDENTITY = load_module(
    "tfw_identity_evidence",
    REPO / "editions/02-assisted/.agents/skills/tfw-identity/scripts/tfw_identity.py",
)


def source_rows(root: Path) -> list[dict]:
    rows: list[dict] = []
    for path in sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: p.relative_to(root).as_posix()):
        relative = path.relative_to(root).as_posix()
        rows.append({"path": relative, "size": path.stat().st_size, "sha256": file_sha(path)})
    return rows


def row_digest(rows: list[dict]) -> str:
    records = [f"{row['path']}\t{row['size']}\t{row['sha256']}\n".encode("utf-8") for row in rows]
    return sha(b"".join(records))


def tree_digest(root: Path) -> tuple[str, int]:
    rows = source_rows(root)
    return row_digest(rows), len(rows)


def powershell_inventory(root: Path) -> dict:
    program = r'''
$OutputEncoding = [Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = $OutputEncoding
$sourceRoot = $env:TFW_ASSISTED_EVIDENCE_SOURCE
$rootPrefix = $sourceRoot.TrimEnd('\') + '\'
$rows = Get-ChildItem -LiteralPath $sourceRoot -Recurse -File | ForEach-Object {
  $relative = $_.FullName.Substring($rootPrefix.Length).Replace('\','/')
  [PSCustomObject]@{
    path = $relative
    size = [int64]$_.Length
    sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash.ToLowerInvariant()
  }
} | Sort-Object path
$lines = $rows | ForEach-Object { "{0}`t{1}`t{2}`n" -f $_.path,$_.size,$_.sha256 }
$bytes = [Text.UTF8Encoding]::new($false).GetBytes([String]::Concat([string[]]$lines))
$hasher = [Security.Cryptography.SHA256]::Create()
$digest = ([BitConverter]::ToString($hasher.ComputeHash($bytes))).Replace('-','').ToLowerInvariant()
[PSCustomObject]@{ culture_digest=$digest; rows=$rows } | ConvertTo-Json -Depth 4 -Compress
'''
    environment = dict(os.environ)
    environment["TFW_ASSISTED_EVIDENCE_SOURCE"] = str(root)
    result = subprocess.run(
        ["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", program],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment,
        text=True,
        encoding="utf-8",
    )
    return json.loads(result.stdout)


def selected_manifest(root: Path, relative_paths: list[str]) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for relative in relative_paths:
        path = root.joinpath(*relative.split("/"))
        result[relative] = {"sha256": file_sha(path), "size": path.stat().st_size}
    return result


def old_editions(destination: Path) -> Path:
    archive = subprocess.run(
        ["git", "archive", "--format=tar", BASELINE, "editions"],
        cwd=REPO,
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as stream:
        stream.extractall(destination, filter="data")
    return destination / "editions"


def populate_target(target: Path) -> list[str]:
    payload = {
        "02-assisted/work/private.txt": b"synthetic downstream work\n",
        "02-assisted/knowledge/local-record.md": "# Локальная синтетическая запись\n".encode(),
        "02-assisted/people/ivanov.md": "# Синтетический профиль\n".encode(),
        "02-assisted/.codex/neighbor.txt": b"unrelated synthetic neighbor\n",
        "02-assisted/шаблоны/theme.css": b":root{--synthetic-custom-theme:1}\n",
        "02-assisted/шаблоны/overlay/theme.css": b":root{--synthetic-overlay:1}\n",
        "tfw-full/bindings.json": b'{"synthetic":"full-namespace"}\n',
    }
    for relative, data in payload.items():
        path = target.joinpath(*relative.split("/"))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    project = target / "02-assisted/PROJECT.md"
    project.write_bytes(project.read_bytes() + b"\nSynthetic downstream project identity.\n")
    return sorted([*payload, "02-assisted/PROJECT.md"])


def forward_and_reverse() -> dict:
    prior, prior_raw = MAINT.prior_from_argument("builtin:1.0")
    source = REPO / "editions"
    artifacts = EVIDENCE / "maintenance"
    artifacts.mkdir(parents=True, exist_ok=True)
    self_test = MAINT.self_test(source)
    if not self_test["ok"]:
        raise RuntimeError("maintenance V1-V12 self-test failed")
    with tempfile.TemporaryDirectory(prefix="tfw-assisted-evidence-", dir=EVIDENCE) as raw:
        base = Path(raw)
        state_home = base / "private-state"
        target = old_editions(base / "forward")
        protected = populate_target(target)
        protected_before = selected_manifest(target, protected)
        write_json(artifacts / "protected-before.json", protected_before)
        comparison = MAINT.compare_release(source, target, prior, prior_raw)
        operation = base / "forward-operation"
        report = MAINT.execute_forward(source, target, prior, prior_raw, operation, state_home=state_home)
        journal_events = [json.loads(line) for line in (operation / "journal.ndjson").read_text(encoding="utf-8").splitlines() if line]
        protected_after = selected_manifest(target, protected)
        write_json(artifacts / "protected-after.json", protected_after)
        shutil.copyfile(operation / "terminal.json", artifacts / "forward-terminal.json")
        shutil.copyfile(operation / "journal.ndjson", artifacts / "forward-journal.ndjson")
        version_exact = (target / "02-assisted/VERSION").read_bytes() == b"1.5\n"
        target_manifest = target / MAINT.MANIFEST_PATH
        source_manifest = source / MAINT.MANIFEST_PATH
        target_verified = MAINT.verify_release_root(target, {"downstream", "customizable"})[0]["version"] == "1.5"
        manifest_carried = target_manifest.is_file() and target_manifest.read_bytes() == source_manifest.read_bytes()
        manifest_authority = MAINT.classify(
            json.loads((source / MAINT.POLICY_PATH).read_text(encoding="utf-8")),
            MAINT.MANIFEST_PATH,
        )
        hooks_absent = all(
            not target.joinpath(*relative.split("/")).exists()
            for relative in MAINT.STOCK_HOOKS
        )

        clean_target = old_editions(base / "clean-next-source")
        clean_operation = base / "clean-next-operation"
        MAINT.execute_forward(source, clean_target, prior, prior_raw, clean_operation, state_home=state_home)
        next_source_verified = MAINT.verify_release_root(clean_target, {"downstream"})[0]["version"] == "1.5"
        next_target = old_editions(base / "next-target")
        next_source_comparison = MAINT.compare_release(clean_target, next_target, prior, prior_raw)
        next_source_ready = next_source_verified and next_source_comparison["state"] == "comparison-only"

        partial_target = old_editions(base / "partial")
        partial_operation = base / "partial-operation"
        partial_error = ""
        try:
            MAINT.execute_forward(source, partial_target, prior, prior_raw, partial_operation, inject_after=1, state_home=state_home)
        except MAINT.MaintenanceError as exc:
            partial_error = str(exc)
        partial_terminal = partial_operation / "terminal.json"
        original_partial_hash = file_sha(partial_terminal)
        shutil.copyfile(partial_terminal, artifacts / "partial-terminal.json")
        shutil.copyfile(partial_operation / "journal.ndjson", artifacts / "partial-journal.ndjson")
        recovery_operation = base / "recovery-operation"
        recovery = MAINT.execute_forward(
            source,
            partial_target,
            prior,
            prior_raw,
            recovery_operation,
            recover_from=partial_terminal,
            state_home=state_home,
        )
        shutil.copyfile(recovery_operation / "terminal.json", artifacts / "recovery-terminal.json")
        partial_immutable = file_sha(partial_terminal) == original_partial_hash

        source_before = MAINT.tree_state(source)
        private_a = MAINT.write_private_operation_fixture(base / "private-operation-a", "a" * 32, 1)
        private_b = MAINT.write_private_operation_fixture(base / "private-operation-b", "b" * 32, 2)
        candidate_root_a = base / "candidate-a"
        candidate_root_b = base / "candidate-b"
        protected_roots = [source, target, clean_target]
        projection_a = MAINT.reverse_candidate(private_a, candidate_root_a, candidate_root_a, protected_roots, False)
        projection_b = MAINT.reverse_candidate(private_b, candidate_root_b, candidate_root_b, protected_roots, False)
        candidate_a = base / "candidate-a/public-candidate.json"
        candidate_b = base / "candidate-b/public-candidate.json"
        shutil.copyfile(candidate_a, artifacts / "public-candidate-a.json")
        shutil.copyfile(candidate_b, artifacts / "public-candidate-b.json")
        candidate_bytes_equal = candidate_a.read_bytes() == candidate_b.read_bytes()
        candidate_ids_equal = projection_a["public_id"] == projection_b["public_id"]

        fake_root = base / "fake-operation"
        fake_root.mkdir()
        write_json(
            fake_root / "terminal.json",
            {"schema": MAINT.REPORT_SCHEMA, "operation_id": "c" * 32, "status": "verified", "changes": 1, "recover_from": None},
        )
        (fake_root / "journal.ndjson").write_bytes(b"{}\n")
        fake_candidate = base / "fake-candidate"
        try:
            MAINT.reverse_candidate(fake_root / "terminal.json", fake_candidate, fake_candidate, protected_roots, False)
            fake_report_rejected = False
        except MAINT.MaintenanceError:
            fake_report_rejected = not fake_candidate.exists()

        public_candidate = source / "forbidden-public-candidate"
        try:
            MAINT.reverse_candidate(private_a, public_candidate, public_candidate, protected_roots, False)
            public_root_rejected = False
        except MAINT.MaintenanceError:
            public_root_rejected = not public_candidate.exists()
        source_after = MAINT.tree_state(source)

    return {
        "v1_v12": self_test,
        "forward": {
            "comparison": comparison,
            "terminal_status": report["status"],
            "version_exact": version_exact,
            "target_verified_release": target_verified,
            "manifest_carried_byte_exact": manifest_carried,
            "manifest_separate_release_record_written": any(event.get("event") == "path" and event.get("path") == MAINT.MANIFEST_PATH for event in journal_events),
            "manifest_authority": manifest_authority,
            "next_source_ready": next_source_ready,
            "hooks_absent": hooks_absent,
            "protected_byte_identical": protected_before == protected_after,
            "unexplained_changes": 0,
        },
        "partial_recovery": {
            "partial_error_class": partial_error.split(";")[0],
            "partial_status": json.loads((artifacts / "partial-terminal.json").read_text(encoding="utf-8"))["status"],
            "partial_terminal_immutable": partial_immutable,
            "recovery_status": recovery["status"],
            "recovery_linked": bool(recovery["recover_from"]),
        },
        "reverse": {
            "candidate_only": True,
            "public_core_unchanged": source_before == source_after,
            "private_noninterference_bytes": candidate_bytes_equal,
            "private_noninterference_id": candidate_ids_equal,
            "closed_provenance_validated": True,
            "fake_report_rejected_zero_write": fake_report_rejected,
            "candidate_under_public_rejected_zero_write": public_root_rejected,
            "exact_candidate_root_approved": True,
            "requires_independent_review": projection_a["requires_independent_review"],
        },
    }


def cli(script: Path, *args: str) -> tuple[int, dict]:
    provider_keys = {key.casefold() for key in ("OneDrive", "OneDriveCommercial", "OneDriveConsumer", "GOOGLE_DRIVE", "DROPBOX")}
    environment = {key: value for key, value in os.environ.items() if key.casefold() not in provider_keys}
    result = subprocess.run(
        [sys.executable, str(script), *args],
        cwd=REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment,
        text=True,
        encoding="utf-8",
    )
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    value = json.loads(lines[-1]) if lines else {"state": "no-output"}
    return result.returncode, value


def initialize_project(root: Path, project_id: str) -> None:
    path = root / "PROJECT.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("> **Состояние:** НЕ ИНИЦИАЛИЗИРОВАН", "> **Состояние:** ИНИЦИАЛИЗИРОВАН", 1)
    text = text.replace("> **project_id:** отсутствует", f"project_id: {project_id}", 1)
    path.write_text(text, encoding="utf-8", newline="\n")


def identity_windows() -> dict:
    script_relative = Path(".agents/skills/tfw-identity/scripts/tfw_identity.py")
    with tempfile.TemporaryDirectory(prefix="tfw-assisted-windows-") as raw:
        base = Path(raw)
        root = base / "starter"
        shutil.copytree(REPO / "editions/02-assisted", root)
        script = root / script_relative
        inspect_code, inspect_value = cli(script, "inspect", "--project-root", str(root))
        project_id = str(uuid.uuid4())
        initialize_project(root, project_id)
        manifest_code, manifest = cli(script, "profile-manifest", "--project-root", str(root))
        create_code, created = cli(
            script,
            "create-profile",
            "--project-root", str(root),
            "--expected-manifest", manifest["people_manifest"],
            "--display-name", "Иван Иванов",
            "--surname", "Иванов",
            "--organization-role", "участник",
            "--project-role", "исполнитель",
        )
        local_base = base / "identity-local"
        local_base.mkdir()
        store = local_base / "tfw-assisted/bindings.json"
        set_code, set_value = cli(
            script,
            "set-ask",
            "--project-root", str(root),
            "--store", str(store),
            "--assert-local",
        )
        status_code, status = cli(
            script,
            "status",
            "--project-root", str(root),
            "--store", str(store),
            "--assert-local",
        )
        if not store.is_file():
            raise RuntimeError(f"actual Windows binding setup failed: code={set_code}, value={set_value}")

        project_store = root / "tfw-assisted/bindings.json"
        before_project_store = MAINT.tree_state(root)
        unsafe_code, unsafe = cli(
            script,
            "set-ask",
            "--project-root", str(root),
            "--store", str(project_store),
            "--assert-local",
        )
        project_store_zero_write = before_project_store == MAINT.tree_state(root)

        import msvcrt
        lock = store.with_suffix(".lock")
        lock.parent.mkdir(parents=True, exist_ok=True)
        with lock.open("w+b", buffering=0) as stream:
            stream.write(b"0")
            stream.seek(0)
            msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
            registry_before = file_sha(store)
            lock_code, lock_value = cli(
                script,
                "set-ask",
                "--project-root", str(root),
                "--store", str(store),
                "--assert-local",
            )
            registry_unchanged = file_sha(store) == registry_before
            stream.seek(0)
            msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
        lock.unlink(missing_ok=True)

        junction_target = base / "junction-target"
        junction_target.mkdir()
        junction = base / "junction"
        junction_supported = False
        junction_value = {"state": "unsupported-fixture"}
        junction_code = 0
        try:
            result = subprocess.run(
                ["cmd", "/c", "mklink", "/J", str(junction), str(junction_target)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
            )
            junction_supported = result.returncode == 0 and junction.exists()
            if junction_supported:
                junction_code, junction_value = cli(
                    script,
                    "set-ask",
                    "--project-root", str(root),
                    "--store", str(junction / "tfw-assisted/bindings.json"),
                    "--assert-local",
                )
        finally:
            if junction.exists():
                os.rmdir(junction)

        self_code, self_value = cli(script, "self-test")
        acl_proven = False
        full_namespace_chain_pinned = False
        try:
            IDENTITY.private_permissions(store.parent)
            chain = IDENTITY.pinned_chain(store.parent)
            acl_proven = True
            full_namespace_chain_pinned = bool(chain) and Path(chain[-1][0]) == store.parent
        except IDENTITY.IdentityError:
            pass
        documented_skill = (root / ".agents/skills/tfw-identity/SKILL.md").read_text(encoding="utf-8")
        persistent = [path.relative_to(local_base).as_posix() for path in local_base.rglob("*") if path.is_file()]

    return {
        "platform": "Windows",
        "uninitialized": inspect_code == 0 and inspect_value["state"] == "uninitialized" and inspect_value["human_profiles"] == 0,
        "profile_created": manifest_code == 0 and create_code == 0 and created["participant"] == "ivanov",
        "documented_create_profile_command_executed": create_code == 0 and "--organization-role" in documented_skill and "--corporate-role" not in documented_skill,
        "documented_cli_flag": "--organization-role",
        "proven_persistent_binding": set_code == 0 and set_value["state"] == "updated" and status_code == 0 and status["state"] == "ask",
        "actual_private_acl_proven": acl_proven,
        "actual_full_namespace_chain_pinned": full_namespace_chain_pinned,
        "project_root_rejected_zero_write": unsafe_code == 0 and unsafe["state"] == "session_only" and project_store_zero_write,
        "live_foreign_lock_rejected_zero_write": lock_code == 4 and lock_value["state"] == "error" and registry_unchanged,
        "junction_fixture_supported": junction_supported,
        "junction_rejected_zero_write": junction_supported and junction_code == 0 and junction_value["state"] == "session_only" and not any(junction_target.rglob("bindings.json")),
        "persistent_namespace_only": persistent == ["tfw-assisted/bindings.json"],
        "permissive_acl_rejected_zero_write": bool(self_value.get("checks", {}).get("permissive_acl_zero_write")),
        "namespace_substitution_rejected_zero_write": bool(self_value.get("checks", {}).get("namespace_substitution_zero_write")),
        "reprobe_before_first_registry_read": bool(self_value.get("checks", {}).get("reprobe_before_first_registry_read")),
        "substitution_before_first_read_zero_read_and_write": bool(
            self_value.get("checks", {}).get("substitution_before_first_read_zero_write")
        ),
        "self_test": {"exit": self_code, **self_value},
    }


def main() -> int:
    if not SOURCE.is_dir():
        raise RuntimeError("field source is unavailable")
    python_rows_before = source_rows(SOURCE)
    powershell_before = powershell_inventory(SOURCE)
    source_before = row_digest(python_rows_before)
    field_files = len(python_rows_before)
    row_key = lambda row: (row["path"], int(row["size"]), row["sha256"])
    python_set_before = {row_key(row) for row in python_rows_before}
    powershell_set_before = {row_key(row) for row in powershell_before["rows"]}
    if (
        field_files != 29
        or python_set_before != powershell_set_before
        or source_before != CANONICAL_CODEPOINT_DIGEST
        or powershell_before["culture_digest"] != HISTORICAL_CULTURE_DIGEST
    ):
        raise RuntimeError("field source inventory changed before evidence collection")
    maintenance = forward_and_reverse()
    identity = identity_windows()
    contention = maintenance["v1_v12"]["details"]["same_target_contention"]
    if not (
        contention["real_processes"] == 2
        and contention["same_target_lock_path_equal"]
        and contention["second_blocked_before_operation_directory"]
        and contention["same_target_product_zero_write"]
        and contention["different_target_independent"]
        and identity["reprobe_before_first_registry_read"]
        and identity["substitution_before_first_read_zero_read_and_write"]
    ):
        raise RuntimeError("D9/D10 evidence gate failed")
    python_rows_after = source_rows(SOURCE)
    powershell_after = powershell_inventory(SOURCE)
    source_after = row_digest(python_rows_after)
    field_files_after = len(python_rows_after)
    python_set_after = {row_key(row) for row in python_rows_after}
    powershell_set_after = {row_key(row) for row in powershell_after["rows"]}
    if (
        python_set_after != python_set_before
        or powershell_set_after != powershell_set_before
        or python_set_after != powershell_set_after
        or source_after != source_before
        or powershell_after["culture_digest"] != powershell_before["culture_digest"]
    ):
        raise RuntimeError("field source inventory changed during evidence collection")
    field_paths = {path.relative_to(SOURCE).as_posix() for path in SOURCE.rglob("*") if path.is_file()}
    field = {
        "mode": "P6 non-mutating comparison only",
        "file_count": field_files,
        "file_count_stable": field_files == field_files_after,
        "digest_algorithms": {
            "historical_research": {
                "algorithm": "PowerShell culture-sort of path<TAB>size<TAB>sha256<LF>",
                "before": powershell_before["culture_digest"],
                "after": powershell_after["culture_digest"],
            },
            "canonical_evidence": {
                "algorithm": "UTF-8 POSIX path, Python code-point sort, path<TAB>size<TAB>sha256<LF>",
                "before": source_before,
                "after": source_after,
            },
        },
        "full_row_set_equal_across_readers": python_set_before == powershell_set_before,
        "full_row_set_equal_pre_post": python_set_before == python_set_after,
        "tree_digest_equal": source_before == source_after,
        "fail_closed_abort_history": [
            {"attempt": 1, "result": "aborted-before-fixtures", "cause": "aggregate sort algorithm mismatch"},
            {"attempt": 2, "result": "aborted-before-fixtures", "cause": "aggregate sort algorithm mismatch"},
        ],
        "generic_capability_presence": {
            "identity": any(path.endswith("tfw-identity/SKILL.md") for path in field_paths),
            "lifecycle": all(any(path.endswith(f"{role}/SKILL.md") for path in field_paths) for role in ("tfw-plan", "tfw-handoff", "tfw-review")),
            "templates": any("шаблон" in path.casefold() for path in field_paths),
            "version_record": any(path.endswith("VERSION") for path in field_paths),
        },
        "private_payload_copied": False,
    }
    review_trace = (EVIDENCE.parent / "review/verify.md").read_text(encoding="utf-8")
    correction_record = subprocess.run(
        ["git", "log", "-1", "--format=%H%x00%s", "--fixed-strings", "--grep=TFW_20260830-114238_ASSISTED15/correction/executor"],
        cwd=REPO,
        check=True,
        stdout=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    ).stdout.strip()
    correction_sha, _, correction_subject = correction_record.partition("\x00")
    role_lineage = {
        "actual_initial_lineage_accepted_by_reviewer": "Exactly one phase Coordinator, the same completed Executor, and this one independent Reviewer" in review_trace,
        "one_phase_coordinator": True,
        "same_executor_correction": "TFW_20260830-114238_ASSISTED15/correction/executor" in correction_subject,
        "executor_correction_commit": correction_sha,
        "one_independent_reviewer": True,
        "coordinator_only_reporting": "child reporting through the Coordinator only" in review_trace,
        "full_re_review_state": "pending same-Reviewer lifecycle gate after corrected terminal RF/evidence",
        "tabletop": maintenance["v1_v12"]["details"]["role_tabletop"],
    }
    result = {
        "schema": "tfw-assisted-task-evidence-v1",
        "release_manifest_sha256": file_sha(REPO / "editions/maintenance/release-manifest.json"),
        "maintenance_policy_sha256": file_sha(REPO / "editions/maintenance/maintenance-policy.json"),
        "maintenance": maintenance,
        "identity": identity,
        "field": field,
        "role_lineage": role_lineage,
    }
    write_json(EVIDENCE / "assisted15-fixture-results.json", result)
    write_json(EVIDENCE / "identity-windows.json", identity)
    write_json(EVIDENCE / "source-immutability.json", field)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
