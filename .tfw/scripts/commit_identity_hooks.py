#!/usr/bin/env python3
"""Repository-local TFW Commit Identity runtime and lifecycle.

The Phase A contract owns identity meaning and exact range semantics. The Phase B
router owns workflow and operation dispositions. This module owns only recognized
runtime lifecycle, private clone-local state, command-scoped context transport, and
the two Git hook stages. It never authenticates an actor or authorizes publication.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import commit_identity as ci
import commit_identity_router as router


CONTEXT_FIELDS = ci.CONTEXT_FIELDS


class HookCodes:
    ARGUMENT = "E_HOOK_ARGUMENT"
    REPOSITORY = "E_HOOK_REPOSITORY"
    RUNTIME_CONFLICT = "E_RUNTIME_CONFLICT"
    RUNTIME_MANIFEST = "E_RUNTIME_MANIFEST"
    RUNTIME_MATERIAL = "E_RUNTIME_MATERIAL"
    RUNTIME_MODE = "E_RUNTIME_MODE"
    LOCAL_CONFIG = "E_LOCAL_CONFIG"
    LEDGER = "E_RUNTIME_LEDGER"
    LEDGER_REQUIRED = "E_RUNTIME_LEDGER_REQUIRED"
    EXPECTED_CONTEXT = "E_HOOK_EXPECTED_CONTEXT"
    PLAN = "E_HOOK_PLAN"
    GIT_COMMIT = "E_HOOK_GIT_COMMIT"


@dataclass
class HookError(Exception):
    code: str
    field: str
    rule: str


class SafeArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise HookError(
            HookCodes.ARGUMENT,
            "arguments",
            "must use a documented local runtime command",
        )


def _run_git(
    repo: Path,
    args: Sequence[str],
    *,
    allowed: Iterable[int] = (0,),
    input_text: str | None = None,
    env: Mapping[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), *args],
            input=input_text,
            text=True,
            encoding="utf-8",
            errors="surrogateescape",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(env) if env is not None else None,
            check=False,
        )
    except OSError:
        raise HookError(HookCodes.REPOSITORY, "Git", "must be available")
    if result.returncode not in set(allowed):
        raise HookError(
            HookCodes.REPOSITORY,
            "local Git operation",
            "must complete without exposing subprocess output",
        )
    return result


def _repository_paths(repo: Path) -> tuple[Path, Path]:
    root_result = _run_git(repo, ["rev-parse", "--show-toplevel"])
    root_text = root_result.stdout.strip()
    if not root_text:
        raise HookError(HookCodes.REPOSITORY, "repository", "must be a Git work tree")
    root = Path(root_text).resolve()
    common_result = _run_git(root, ["rev-parse", "--git-common-dir"])
    common_text = common_result.stdout.strip()
    if not common_text:
        raise HookError(
            HookCodes.REPOSITORY, "Git common directory", "must resolve privately"
        )
    common_candidate = Path(common_text)
    common = (
        common_candidate.resolve()
        if common_candidate.is_absolute()
        else (root / common_candidate).resolve()
    )
    return root, common


def _safe_join(base: Path, relative: str, field: str) -> Path:
    candidate = (base / Path(relative)).resolve()
    try:
        candidate.relative_to(base.resolve())
    except ValueError:
        raise HookError(HookCodes.RUNTIME_MANIFEST, field, "must stay inside its owner root")
    return candidate


def _contract_for_repo(
    repo: Path,
    schema_path: Path | None = None,
    state_path: Path | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    root, _ = _repository_paths(repo)
    schema = schema_path or root / ".tfw" / "commit_identity.schema.json"
    state = state_path or root / ".tfw" / "commit_identity_state.json"
    return ci.load_contract(schema, state)


def _read_json(path: Path, field: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        raise HookError(HookCodes.RUNTIME_MANIFEST, field, "must be valid owned UTF-8 JSON")
    if not isinstance(value, dict):
        raise HookError(HookCodes.RUNTIME_MANIFEST, field, "must be an object")
    return value


def _sha256_lf(path: Path) -> str:
    try:
        data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    except OSError:
        raise HookError(
            HookCodes.RUNTIME_MATERIAL,
            "owned runtime target",
            "must be readable",
        )
    return hashlib.sha256(data).hexdigest()


def _validate_manifest(
    schema: Mapping[str, Any],
    root: Path,
    *,
    require_material: bool,
) -> dict[str, Any]:
    manifest_name = schema["runtime"]["manifest"]
    manifest = _read_json(_safe_join(root, manifest_name, "runtime manifest"), "runtime manifest")
    if manifest.get("runtime_kind") != "tfw.commit-identity-hook-runtime":
        raise HookError(
            HookCodes.RUNTIME_CONFLICT,
            "runtime manifest",
            "must identify recognized TFW ownership",
        )
    if manifest.get("runtime_version") != schema["runtime"]["required_version"]:
        raise HookError(
            HookCodes.RUNTIME_MANIFEST,
            "runtime version",
            "must match the schema-owned requirement",
        )
    if manifest.get("contract_version") != schema["contract_version"]:
        raise HookError(
            HookCodes.RUNTIME_MANIFEST,
            "contract version",
            "must match the schema owner",
        )
    if manifest.get("source") != schema["runtime"]["source"]:
        raise HookError(
            HookCodes.RUNTIME_MANIFEST,
            "runtime source",
            "must match the canonical relative owner",
        )
    claims = manifest.get("claims")
    if not isinstance(claims, dict) or claims.get("actor_authentication") is not False:
        raise HookError(
            HookCodes.RUNTIME_MANIFEST,
            "runtime claims",
            "must preserve the non-authentication boundary",
        )
    records = manifest.get("targets")
    expected = schema["runtime"]["hook_targets"]
    if not isinstance(records, list) or len(records) != len(expected):
        raise HookError(
            HookCodes.RUNTIME_MANIFEST,
            "runtime targets",
            "must equal the schema-owned hook inventory",
        )
    seen: list[str] = []
    entrypoints: list[str] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise HookError(
                HookCodes.RUNTIME_MANIFEST,
                "runtime target",
                "must be a recognized record",
            )
        target = record.get("path")
        entrypoint = record.get("entrypoint")
        digest = record.get("sha256_lf")
        if target != expected[index] or not isinstance(entrypoint, str) or not entrypoint:
            raise HookError(
                HookCodes.RUNTIME_MANIFEST,
                "runtime target",
                "must preserve owned path and entrypoint order",
            )
        if (
            not isinstance(digest, str)
            or len(digest) != 64
            or any(char not in "0123456789abcdef" for char in digest)
        ):
            raise HookError(
                HookCodes.RUNTIME_MANIFEST,
                "runtime target digest",
                "must be a lowercase SHA-256 record",
            )
        seen.append(target)
        entrypoints.append(entrypoint)
        if require_material and _sha256_lf(_safe_join(root, target, "runtime target")) != digest:
            raise HookError(
                HookCodes.RUNTIME_MATERIAL,
                "owned runtime target",
                "must match its recognized manifest",
            )
    if len(set(seen)) != len(seen) or len(set(entrypoints)) != len(entrypoints):
        raise HookError(
            HookCodes.RUNTIME_MANIFEST,
            "runtime targets",
            "must use unique paths and entrypoints",
        )
    return manifest


def _runtime_disposition(schema: Mapping[str, Any], root: Path) -> str:
    if not root.exists():
        return "missing"
    if not root.is_dir():
        return "conflict"
    manifest_path = root / schema["runtime"]["manifest"]
    try:
        entries = list(root.iterdir())
    except OSError:
        return "conflict"
    if not manifest_path.exists():
        return "missing" if not entries else "conflict"
    try:
        _validate_manifest(schema, root, require_material=False)
    except HookError:
        return "conflict"
    try:
        _validate_manifest(schema, root, require_material=True)
        return "recognized"
    except HookError as error:
        if error.code == HookCodes.RUNTIME_MATERIAL:
            return "owned-drift"
        return "conflict"


def _atomic_write(path: Path, data: bytes, mode: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tfw-{os.getpid()}.tmp")
    try:
        temporary.write_bytes(data)
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    except OSError:
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            pass
        raise HookError(
            HookCodes.RUNTIME_MATERIAL,
            "owned runtime target",
            "must update atomically",
        )


def _copy_recognized_runtime(
    schema: Mapping[str, Any],
    source_root: Path,
    target_root: Path,
) -> str:
    _validate_manifest(schema, source_root, require_material=True)
    if source_root.resolve() == target_root.resolve():
        return "recognized"
    disposition = _runtime_disposition(schema, target_root)
    if disposition == "conflict":
        raise HookError(
            HookCodes.RUNTIME_CONFLICT,
            "reserved runtime target",
            "contains material without recognized TFW ownership",
        )
    owned_names = [schema["runtime"]["manifest"], *schema["runtime"]["hook_targets"]]
    backups: dict[str, bytes | None] = {}
    for name in owned_names:
        target = _safe_join(target_root, name, "runtime target")
        try:
            backups[name] = target.read_bytes() if target.exists() else None
        except OSError:
            raise HookError(
                HookCodes.RUNTIME_MATERIAL,
                "owned runtime target",
                "must be readable before repair",
            )
    try:
        for name in schema["runtime"]["hook_targets"]:
            source = _safe_join(source_root, name, "runtime source")
            _atomic_write(
                _safe_join(target_root, name, "runtime target"),
                source.read_bytes(),
                0o755,
            )
        manifest_name = schema["runtime"]["manifest"]
        _atomic_write(
            _safe_join(target_root, manifest_name, "runtime manifest"),
            _safe_join(source_root, manifest_name, "runtime source").read_bytes(),
            0o644,
        )
        _validate_manifest(schema, target_root, require_material=True)
    except (HookError, OSError):
        for name, previous in backups.items():
            target = _safe_join(target_root, name, "runtime target")
            try:
                if previous is None:
                    target.unlink(missing_ok=True)
                else:
                    _atomic_write(
                        target,
                        previous,
                        0o755 if name in schema["runtime"]["hook_targets"] else 0o644,
                    )
            except (HookError, OSError):
                pass
        raise HookError(
            HookCodes.RUNTIME_MATERIAL,
            "owned runtime repair",
            "must complete atomically or restore prior recognized material",
        )
    return "repaired" if disposition != "missing" else "installed-material"


def _local_hook_values(repo: Path) -> list[str]:
    result = _run_git(
        repo,
        ["config", "--local", "--null", "--get-all", "core.hooksPath"],
        allowed=(0, 1),
    )
    if result.returncode == 1:
        return []
    return [value for value in result.stdout.split("\0") if value]


def _set_local_hook_values(repo: Path, values: Sequence[str]) -> None:
    _run_git(
        repo,
        ["config", "--local", "--unset-all", "core.hooksPath"],
        allowed=(0, 5),
    )
    for value in values:
        _run_git(repo, ["config", "--local", "--add", "core.hooksPath", value])


def _ledger_path(schema: Mapping[str, Any], common: Path) -> Path:
    return _safe_join(common, schema["runtime"]["private_ledger"], "private ledger")


def _load_ledger(
    schema: Mapping[str, Any],
    common: Path,
    *,
    required: bool,
) -> dict[str, Any] | None:
    path = _ledger_path(schema, common)
    if not path.exists():
        if required:
            raise HookError(
                HookCodes.LEDGER_REQUIRED,
                "private runtime ledger",
                "is required for exact rollback",
            )
        return None
    try:
        ledger = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        raise HookError(HookCodes.LEDGER, "private runtime ledger", "must be valid")
    if not isinstance(ledger, dict) or ledger.get("ledger_kind") != (
        "tfw.commit-identity-runtime-ledger"
    ):
        raise HookError(
            HookCodes.LEDGER,
            "private runtime ledger",
            "must have recognized ownership",
        )
    if (
        ledger.get("runtime_version") != schema["runtime"]["required_version"]
        or ledger.get("source") != schema["runtime"]["source"]
        or ledger.get("installed") is not True
    ):
        raise HookError(
            HookCodes.LEDGER,
            "private runtime ledger",
            "must match the required runtime",
        )
    previous = ledger.get("previous_local")
    if (
        not isinstance(previous, dict)
        or not isinstance(previous.get("present"), bool)
        or not isinstance(previous.get("values"), list)
        or any(not isinstance(value, str) for value in previous["values"])
        or previous["present"] != bool(previous["values"])
    ):
        raise HookError(
            HookCodes.LEDGER,
            "private prior local state",
            "must preserve exact presence and values",
        )
    return ledger


def _write_ledger(
    schema: Mapping[str, Any],
    common: Path,
    previous_values: Sequence[str],
) -> None:
    record = {
        "ledger_kind": "tfw.commit-identity-runtime-ledger",
        "runtime_version": schema["runtime"]["required_version"],
        "source": schema["runtime"]["source"],
        "installed": True,
        "previous_local": {
            "present": bool(previous_values),
            "values": list(previous_values),
        },
    }
    data = (json.dumps(record, indent=2, sort_keys=True) + "\n").encode("utf-8")
    _atomic_write(_ledger_path(schema, common), data, 0o600)


def verify_installation(
    schema: Mapping[str, Any],
    state: Mapping[str, Any],
    repo: Path,
) -> dict[str, Any]:
    ci.validate_state(schema, state)
    root, common = _repository_paths(repo)
    runtime_root = _safe_join(root, state["hook_runtime"]["source"], "runtime source")
    _validate_manifest(schema, runtime_root, require_material=True)
    ledger = _load_ledger(schema, common, required=True)
    if _local_hook_values(root) != [state["hook_runtime"]["source"]]:
        raise HookError(
            HookCodes.LOCAL_CONFIG,
            "repository-local hook override",
            "must equal the canonical relative runtime",
        )
    assert ledger is not None
    return {
        "status": "valid",
        "disposition": "installed",
        "runtime_version": schema["runtime"]["required_version"],
        "local_config": "relative-owned",
        "private_ledger": "present",
        "actor_authentication": False,
        "publication_authority": False,
    }


def install_runtime(
    schema: Mapping[str, Any],
    state: Mapping[str, Any],
    repo: Path,
) -> dict[str, Any]:
    ci.validate_state(schema, state)
    root, common = _repository_paths(repo)
    runtime_root = _safe_join(root, state["hook_runtime"]["source"], "runtime source")
    disposition = _runtime_disposition(schema, runtime_root)
    if disposition != "recognized":
        raise HookError(
            HookCodes.RUNTIME_CONFLICT,
            "reserved runtime target",
            "must contain the recognized versioned runtime before install",
        )
    existing = _load_ledger(schema, common, required=False)
    if existing is not None:
        result = verify_installation(schema, state, root)
        result["disposition"] = "already-installed"
        return result
    previous_values = _local_hook_values(root)
    _write_ledger(schema, common, previous_values)
    try:
        _set_local_hook_values(root, [state["hook_runtime"]["source"]])
        result = verify_installation(schema, state, root)
    except (HookError, ci.ContractError):
        try:
            _set_local_hook_values(root, previous_values)
            _ledger_path(schema, common).unlink(missing_ok=True)
        except (HookError, OSError):
            pass
        raise HookError(
            HookCodes.LOCAL_CONFIG,
            "repository-local installation",
            "must verify or restore exact prior local state",
        )
    result["disposition"] = "installed"
    return result


def repair_runtime(
    schema: Mapping[str, Any],
    state: Mapping[str, Any],
    repo: Path,
    source_root: Path,
) -> dict[str, Any]:
    ci.validate_state(schema, state)
    root, _ = _repository_paths(repo)
    target_root = _safe_join(root, state["hook_runtime"]["source"], "runtime target")
    material = _copy_recognized_runtime(schema, source_root.resolve(), target_root)
    try:
        result = verify_installation(schema, state, root)
        result["disposition"] = material if material != "recognized" else "already-valid"
        return result
    except HookError as error:
        if error.code != HookCodes.LEDGER_REQUIRED:
            raise
    result = install_runtime(schema, state, root)
    result["disposition"] = material if material != "recognized" else "installed"
    return result


def rollback_runtime(
    schema: Mapping[str, Any],
    state: Mapping[str, Any],
    repo: Path,
) -> dict[str, Any]:
    ci.validate_state(schema, state)
    root, common = _repository_paths(repo)
    ledger = _load_ledger(schema, common, required=False)
    current = _local_hook_values(root)
    if ledger is None:
        if current == [state["hook_runtime"]["source"]]:
            raise HookError(
                HookCodes.LEDGER_REQUIRED,
                "private runtime ledger",
                "is required before changing an owned local override",
            )
        return {
            "status": "valid",
            "disposition": "already-rolled-back",
            "local_config": "prior-state",
            "private_ledger": "absent",
            "actor_authentication": False,
            "publication_authority": False,
        }
    previous = ledger["previous_local"]["values"]
    _set_local_hook_values(root, previous)
    try:
        _ledger_path(schema, common).unlink()
    except OSError:
        try:
            _set_local_hook_values(root, [state["hook_runtime"]["source"]])
        except HookError:
            pass
        raise HookError(
            HookCodes.LEDGER,
            "private runtime ledger",
            "must be removed only after exact config restoration",
        )
    if _local_hook_values(root) != previous:
        raise HookError(
            HookCodes.LOCAL_CONFIG,
            "repository-local rollback",
            "must restore exact prior local state",
        )
    return {
        "status": "valid",
        "disposition": "rolled-back",
        "local_config": "prior-state",
        "private_ledger": "absent",
        "actor_authentication": False,
        "publication_authority": False,
    }


def initialize_project_state(
    schema: Mapping[str, Any],
    repo: Path,
) -> dict[str, Any]:
    root, _ = _repository_paths(repo)
    template_path = root / ".tfw" / "templates" / "commit_identity_state.json"
    output_path = root / ".tfw" / "commit_identity_state.json"
    try:
        template = json.loads(template_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        raise HookError(
            HookCodes.RUNTIME_MANIFEST,
            "project-state template",
            "must be available as valid owned UTF-8 JSON",
        )
    if not isinstance(template, dict):
        raise HookError(
            HookCodes.RUNTIME_MANIFEST,
            "project-state template",
            "must be an object",
        )
    ci.validate_state(schema, template)
    target = _run_git(
        root,
        ["rev-parse", "--verify", "--end-of-options", "HEAD^{commit}"],
        allowed=(0, 128),
    )
    state = json.loads(json.dumps(template))
    if target.returncode == 0:
        object_id = target.stdout.strip()
        if not object_id:
            raise HookError(
                HookCodes.REPOSITORY,
                "destination history",
                "must resolve an exact current commit",
            )
        state["activation"] = {
            "status": template["activation"]["status"],
            "last_pre_policy_commit": object_id,
            "range_semantics": schema["registries"]["range_semantics"][0],
            "pre_anchor_history": schema["registries"]["pre_anchor_history"][0],
        }
        disposition = "existing-history-exclusive"
    else:
        population = _run_git(root, ["rev-list", "--all", "--count"])
        try:
            existing_count = int(population.stdout.strip())
        except ValueError:
            raise HookError(
                HookCodes.REPOSITORY,
                "destination history",
                "must report a complete commit population",
            ) from None
        if existing_count:
            raise HookError(
                HookCodes.REPOSITORY,
                "destination HEAD",
                "must resolve when existing history is present",
            )
        disposition = "unborn-root-inclusive"
    ci.validate_state(schema, state)
    _atomic_write(
        output_path,
        (json.dumps(state, indent=2) + "\n").encode("utf-8"),
        0o644,
    )
    return {
        "status": "valid",
        "disposition": disposition,
        "range_semantics": state["activation"]["range_semantics"],
        "actor_authentication": False,
        "publication_authority": False,
    }


def _expected_context(
    schema: Mapping[str, Any],
    repo: Path,
    environment: Mapping[str, str],
) -> tuple[dict[str, str] | None, bool, list[str]]:
    name = schema["runtime"]["expected_context_env"]
    token = environment.get(name)
    paths = ci.staged_paths(repo)
    if token is None:
        return None, False, paths
    values = token.split("/")
    if len(values) != len(CONTEXT_FIELDS) or any(not value for value in values):
        raise HookError(
            HookCodes.EXPECTED_CONTEXT,
            "expected context",
            "must contain exactly four complete fields",
        )
    fields = dict(zip(CONTEXT_FIELDS, values))
    non_task = fields["task"] == schema["cross_field"]["none_task"]
    ci.validate_context(
        schema,
        fields,
        non_task=non_task,
        staged_paths=paths,
    )
    return fields, non_task, paths


def _read_message(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        raise HookError(
            HookCodes.ARGUMENT,
            "commit message",
            "must be readable owned UTF-8 input",
        )


def validate_hook_stage(
    schema: Mapping[str, Any],
    state: Mapping[str, Any],
    repo: Path,
    message_file: Path,
    stage: str,
    environment: Mapping[str, str],
) -> dict[str, Any]:
    ci.validate_state(schema, state)
    if stage not in {"prepare", "final"}:
        raise HookError(HookCodes.ARGUMENT, "hook stage", "must be a recognized entrypoint")
    message = _read_message(message_file)
    expected, non_task, paths = _expected_context(schema, repo, environment)
    if expected is None:
        subject = message.splitlines()[0] if message.splitlines() else ""
        ci._parse_subject_structural(schema, subject)
        ci.validate_trailers(schema, message)
        comparison = "structural-only"
    else:
        ci.validate_message(
            schema,
            message,
            expected=expected,
            non_task=non_task,
            paths=paths,
        )
        comparison = "exact-context"
    return {
        "status": "valid",
        "stage": stage,
        "context_comparison": comparison,
        "message_mutated": False,
        "actor_authentication": False,
        "publication_authority": False,
    }


def _validate_plan(
    schema: Mapping[str, Any],
    state: Mapping[str, Any],
    plan: Mapping[str, Any],
    staged_paths: Sequence[str],
) -> tuple[dict[str, str], bool, str]:
    if plan.get("status") != "planned":
        raise HookError(HookCodes.PLAN, "router plan", "must be validated and complete")
    context = plan.get("context")
    if not isinstance(context, dict) or set(context) != set(CONTEXT_FIELDS):
        raise HookError(HookCodes.PLAN, "router context", "must contain exactly four fields")
    fields = {name: context.get(name) for name in CONTEXT_FIELDS}
    if any(not isinstance(value, str) or not value for value in fields.values()):
        raise HookError(HookCodes.PLAN, "router context", "must contain complete strings")
    typed_fields = {name: str(value) for name, value in fields.items()}
    non_task = typed_fields["task"] == schema["cross_field"]["none_task"]
    ci.validate_context(
        schema,
        typed_fields,
        non_task=non_task,
        staged_paths=staged_paths,
    )
    token = "/".join(typed_fields[name] for name in schema["grammar"]["field_order"])
    if plan.get("expected_context_token") != token:
        raise HookError(
            HookCodes.PLAN,
            "expected context token",
            "must equal the validated router context",
        )
    if plan.get("required_hook_runtime") != state["hook_runtime"]:
        raise HookError(
            HookCodes.PLAN,
            "runtime requirement",
            "must equal tracked portable project state",
        )
    if (
        plan.get("publication_authority") is not False
        or plan.get("actor_authentication") is not False
        or plan.get("operation") not in router.OPERATIONS
    ):
        raise HookError(
            HookCodes.PLAN,
            "router authority",
            "must remain local, non-authenticated, and allowlisted",
        )
    subject = plan.get("subject")
    if not isinstance(subject, str):
        raise HookError(HookCodes.PLAN, "subject", "must be a validated string")
    trailers = plan.get("trailers")
    if not isinstance(trailers, list) or any(
        not isinstance(record, dict)
        or set(record) != {"name", "value"}
        or not isinstance(record["name"], str)
        or not isinstance(record["value"], str)
        for record in trailers
    ):
        raise HookError(HookCodes.PLAN, "trailers", "must be validated router records")
    message = subject
    if trailers:
        message += "\n\n" + "\n".join(
            f"{record['name']}: {record['value']}" for record in trailers
        )
    ci.validate_message(
        schema,
        message,
        expected=typed_fields,
        non_task=non_task,
        paths=staged_paths,
    )
    return typed_fields, non_task, message


def run_local_commit(
    schema: Mapping[str, Any],
    state: Mapping[str, Any],
    repo: Path,
    plan: Mapping[str, Any],
    *,
    allow_empty: bool = False,
) -> dict[str, Any]:
    root, _ = _repository_paths(repo)
    verify_installation(schema, state, root)
    staged = ci.staged_paths(root)
    context, _, message = _validate_plan(schema, state, plan, staged)
    operation = str(plan["operation"])
    command = ["commit"]
    if operation == "amend":
        command.append("--amend")
    if allow_empty:
        command.append("--allow-empty")
    command.append("--file=-")
    environment = os.environ.copy()
    environment[schema["runtime"]["expected_context_env"]] = str(
        plan["expected_context_token"]
    )
    try:
        result = _run_git(
            root,
            command,
            input_text=message + "\n",
            env=environment,
        )
    except HookError:
        raise HookError(
            HookCodes.GIT_COMMIT,
            "local commit",
            "must pass the routed carrier and repository runtime",
        ) from None
    if result.returncode != 0:
        raise HookError(
            HookCodes.GIT_COMMIT,
            "local commit",
            "must complete successfully",
        )
    commit_id = _run_git(root, ["rev-parse", "HEAD"]).stdout.strip()
    return {
        "status": "committed",
        "operation": operation,
        "commit": commit_id,
        "context": context,
        "runtime_version": schema["runtime"]["required_version"],
        "actor_authentication": False,
        "publication_authority": False,
    }


def _add_contract_paths(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--schema", type=Path)
    parser.add_argument("--state", type=Path)


def _add_route_arguments(parser: argparse.ArgumentParser) -> None:
    for field in ("workflow", *CONTEXT_FIELDS, "operation"):
        parser.add_argument(f"--{field}", required=True)
    parser.add_argument("--summary")
    parser.add_argument("--existing-subject")
    parser.add_argument("--target-subject")
    parser.add_argument("--source-subject")
    parser.add_argument("--source-commit")
    parser.add_argument("--content-origin", action="append", default=[])
    parser.add_argument("--non-task", action="store_true")
    parser.add_argument("--allow-empty", action="store_true")


def build_parser() -> SafeArgumentParser:
    parser = SafeArgumentParser(
        description=(
            "Manage the recognized repository-local TFW Commit Identity runtime. "
            "The runtime grants neither actor authentication nor publication authority."
        )
    )
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("init-state", "install", "verify", "rollback"):
        command = commands.add_parser(name)
        _add_contract_paths(command)
    repair = commands.add_parser("repair")
    _add_contract_paths(repair)
    repair.add_argument("--source-root", type=Path, required=True)
    for name in ("prepare", "final"):
        command = commands.add_parser(name)
        _add_contract_paths(command)
        command.add_argument("--message-file", type=Path, required=True)
    commit = commands.add_parser("commit")
    _add_contract_paths(commit)
    _add_route_arguments(commit)
    return parser


def _safe_result_error(error: HookError) -> str:
    return "\n".join(
        (
            f"{error.code}: {error.field} {error.rule}.",
            "Boundary: recognized repository-local TFW runtime only.",
            "Non-claims: no actor authentication, external-hook access, or publication authority.",
        )
    )


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = build_parser().parse_args(argv)
        if args.command == "init-state":
            root, _ = _repository_paths(args.repo)
            schema_path = args.schema or root / ".tfw" / "commit_identity.schema.json"
            schema = ci._load_json(schema_path, ci.Codes.SCHEMA_JSON)
            ci.validate_schema(schema)
            result = initialize_project_state(schema, args.repo)
        else:
            schema, state = _contract_for_repo(args.repo, args.schema, args.state)
        if args.command == "init-state":
            pass
        elif args.command == "install":
            result = install_runtime(schema, state, args.repo)
        elif args.command == "verify":
            result = verify_installation(schema, state, args.repo)
        elif args.command == "repair":
            result = repair_runtime(schema, state, args.repo, args.source_root)
        elif args.command == "rollback":
            result = rollback_runtime(schema, state, args.repo)
        elif args.command in {"prepare", "final"}:
            result = validate_hook_stage(
                schema,
                state,
                args.repo,
                args.message_file,
                args.command,
                os.environ,
            )
            if result["context_comparison"] == "structural-only":
                print(
                    "W_CONTEXT_ABSENT: expected context unavailable; structural validation only; "
                    "not authenticated.",
                    file=sys.stderr,
                )
        else:
            staged = ci.staged_paths(args.repo)
            plan = router.route_operation(
                schema,
                state,
                workflow=args.workflow,
                surface=args.surface,
                task=args.task,
                work=args.work,
                role=args.role,
                operation=args.operation,
                summary=args.summary,
                existing_subject=args.existing_subject,
                target_subject=args.target_subject,
                source_subject=args.source_subject,
                source_commit=args.source_commit,
                content_origins=args.content_origin,
                non_task=args.non_task,
                staged_paths=staged,
            )
            result = run_local_commit(
                schema,
                state,
                args.repo,
                plan,
                allow_empty=args.allow_empty,
            )
        print(json.dumps(result, sort_keys=True))
        return 0
    except HookError as error:
        print(_safe_result_error(error), file=sys.stderr)
        return 2
    except router.RouterError as error:
        print(router.render_router_error(error), file=sys.stderr)
        return 2
    except ci.ContractError as error:
        print(ci.render_error(error), file=sys.stderr)
        return 2
    except Exception:
        print(
            _safe_result_error(
                HookError(
                    HookCodes.ARGUMENT,
                    "runtime operation",
                    "must fail safely without disclosing local state",
                )
            ),
            file=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
