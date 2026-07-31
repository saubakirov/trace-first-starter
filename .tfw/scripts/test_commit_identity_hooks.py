from __future__ import annotations

import copy
import importlib.util
import itertools
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = Path(__file__).with_name("commit_identity_hooks.py")
SCRIPTS = SCRIPT.parent
sys.path.insert(0, str(SCRIPTS))
try:
    SPEC = importlib.util.spec_from_file_location("commit_identity_hooks", SCRIPT)
    assert SPEC and SPEC.loader
    hooks = importlib.util.module_from_spec(SPEC)
    sys.modules[SPEC.name] = hooks
    SPEC.loader.exec_module(hooks)
finally:
    sys.path.remove(str(SCRIPTS))
ci = hooks.ci
router = hooks.router
CONTEXT_FIELDS = ci.CONTEXT_FIELDS


@pytest.fixture
def contract():
    return ci.load_contract()


def git(
    repo: Path,
    *args: str,
    check: bool = True,
    isolated: bool = False,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    command = [
        "git",
        *(["-c", "core.hooksPath=.tfw/disabled-hooks"] if isolated else []),
        "-C",
        str(repo),
        *args,
    ]
    result = subprocess.run(
        command,
        text=True,
        encoding="utf-8",
        errors="surrogateescape",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        check=False,
    )
    if check:
        assert result.returncode == 0, result.stderr
    return result


def init_repo(tmp_path: Path, name: str = "repo") -> Path:
    repo = tmp_path / name
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    git(repo, "config", "--local", "user.name", "TFW Hook Fixture", isolated=True)
    git(
        repo,
        "config",
        "--local",
        "user.email",
        "hook-fixture@example.invalid",
        isolated=True,
    )
    return repo


def copy_file(source: Path, target: Path, executable: bool = False) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source.read_bytes())
    os.chmod(target, 0o755 if executable else 0o644)


def provision_runtime(repo: Path) -> None:
    for name in (
        "commit_identity.py",
        "commit_identity_router.py",
        "commit_identity_hooks.py",
    ):
        copy_file(ROOT / ".tfw" / "scripts" / name, repo / ".tfw" / "scripts" / name)
    for name in ("commit_identity.schema.json", "commit_identity_state.json"):
        copy_file(ROOT / ".tfw" / name, repo / ".tfw" / name)
    copy_file(
        ROOT / ".tfw" / "templates" / "commit_identity_state.json",
        repo / ".tfw" / "templates" / "commit_identity_state.json",
    )
    copy_file(
        ROOT / ".tfw" / "hooks" / "runtime.json",
        repo / ".tfw" / "hooks" / "runtime.json",
    )
    for name in ("prepare-commit-msg", "commit-msg"):
        copy_file(
            ROOT / ".tfw" / "hooks" / name,
            repo / ".tfw" / "hooks" / name,
            executable=True,
        )


def common_dir(repo: Path) -> Path:
    raw = git(repo, "rev-parse", "--git-common-dir", isolated=True).stdout.strip()
    candidate = Path(raw)
    return candidate.resolve() if candidate.is_absolute() else (repo / candidate).resolve()


def ledger_path(schema, repo: Path) -> Path:
    return common_dir(repo) / schema["runtime"]["private_ledger"]


def local_hook_values(repo: Path) -> list[str]:
    result = git(
        repo,
        "config",
        "--local",
        "--null",
        "--get-all",
        "core.hooksPath",
        check=False,
        isolated=True,
    )
    assert result.returncode in (0, 1)
    return [value for value in result.stdout.split("\0") if value]


def context(
    *,
    surface: str = "codex",
    task: str = "TFW-49",
    work: str = "phase-c",
    role: str = "executor",
) -> dict[str, str]:
    return {"surface": surface, "task": task, "work": work, "role": role}


def plan(contract, repo: Path, **overrides):
    schema, state = contract
    values = {
        "workflow": "handoff",
        **context(),
        "operation": "ordinary",
        "summary": "exercise repository runtime",
        "staged_paths": ci.staged_paths(repo),
    }
    values.update(overrides)
    return router.route_operation(schema, state, **values)


def stage(repo: Path, name: str = "result.txt") -> None:
    (repo / name).write_text(name, encoding="utf-8")
    git(repo, "add", "--", name, isolated=True)


def initial_commit(repo: Path) -> str:
    (repo / "anchor.txt").write_text("anchor", encoding="utf-8")
    git(repo, "add", "--all", isolated=True)
    git(repo, "commit", "-q", "-m", "fixture anchor", isolated=True)
    return git(repo, "rev-parse", "HEAD", isolated=True).stdout.strip()


def test_manifest_and_runtime_inventory_are_schema_owned(contract):
    schema, state = contract
    manifest = hooks._validate_manifest(
        schema, ROOT / state["hook_runtime"]["source"], require_material=True
    )
    assert schema["contract_version"] == "1.1.0"
    assert manifest["runtime_version"] == schema["runtime"]["required_version"]
    assert [record["path"] for record in manifest["targets"]] == (
        schema["runtime"]["hook_targets"]
    )
    assert [record["entrypoint"] for record in manifest["targets"]] == (
        schema["runtime"]["hook_entrypoints"]
    )
    assert state["hook_runtime"] == {
        "required_version": schema["runtime"]["required_version"],
        "source": schema["runtime"]["source"],
    }
    assert manifest["claims"]["actor_authentication"] is False


@pytest.mark.parametrize(
    "mutation",
    [
        "kind",
        "version",
        "contract",
        "source",
        "targets",
        "path",
        "entrypoint",
        "entrypoint-noncanonical",
        "digest",
        "auth",
        "manifest-extra",
        "manifest-missing",
        "target-extra",
        "target-missing",
        "claims-extra",
        "claims-missing",
        "material",
        "target-directory",
    ],
)
def test_manifest_and_owned_material_mutations_fail_closed(contract, tmp_path, mutation):
    schema, state = contract
    repo = init_repo(tmp_path)
    provision_runtime(repo)
    root = repo / state["hook_runtime"]["source"]
    manifest_path = root / schema["runtime"]["manifest"]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if mutation == "kind":
        manifest["runtime_kind"] = "unknown"
    elif mutation == "version":
        manifest["runtime_version"] = "9.9.9"
    elif mutation == "contract":
        manifest["contract_version"] = "9.9.9"
    elif mutation == "source":
        manifest["source"] = "other/hooks"
    elif mutation == "targets":
        manifest["targets"].pop()
    elif mutation == "path":
        manifest["targets"][0]["path"] = "unknown"
    elif mutation == "entrypoint":
        manifest["targets"][0]["entrypoint"] = ""
    elif mutation == "entrypoint-noncanonical":
        manifest["targets"][0]["entrypoint"] = "arbitrary-nonempty"
    elif mutation == "digest":
        manifest["targets"][0]["sha256_lf"] = "bad"
    elif mutation == "auth":
        manifest["claims"]["actor_authentication"] = True
    elif mutation == "manifest-extra":
        manifest["unexpected"] = "shape-mutation"
    elif mutation == "manifest-missing":
        del manifest["source"]
    elif mutation == "target-extra":
        manifest["targets"][0]["unexpected"] = "shape-mutation"
    elif mutation == "target-missing":
        del manifest["targets"][0]["sha256_lf"]
    elif mutation == "claims-extra":
        manifest["claims"]["unexpected"] = False
    elif mutation == "claims-missing":
        del manifest["claims"]["actor_authentication"]
    elif mutation == "material":
        target = root / schema["runtime"]["hook_targets"][0]
        target.write_text("changed owned fixture", encoding="utf-8")
    else:
        target = root / schema["runtime"]["hook_targets"][0]
        target.unlink()
        target.mkdir()
    if mutation not in {"material", "target-directory"}:
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(hooks.HookError):
        hooks._validate_manifest(schema, root, require_material=True)


@pytest.mark.parametrize("entry_kind", ["file", "directory"])
@pytest.mark.parametrize("operation", ["install", "verify", "repair"])
def test_lifecycle_rejects_every_extra_reserved_target_entry(
    contract, tmp_path, entry_kind, operation
):
    schema, state = contract
    repo = init_repo(tmp_path, f"{operation}-{entry_kind}")
    provision_runtime(repo)
    extra = repo / state["hook_runtime"]["source"] / "unexpected-reserved-target"
    if entry_kind == "file":
        extra.write_text("synthetic unknown material", encoding="utf-8")
    else:
        extra.mkdir()
    before = extra.is_dir(), extra.read_bytes() if extra.is_file() else None
    with pytest.raises(hooks.HookError) as error:
        if operation == "install":
            hooks.install_runtime(schema, state, repo)
        elif operation == "verify":
            hooks.verify_installation(schema, state, repo)
        else:
            hooks.repair_runtime(
                schema,
                state,
                repo,
                ROOT / state["hook_runtime"]["source"],
            )
    assert error.value.code == hooks.HookCodes.RUNTIME_CONFLICT
    assert (extra.is_dir(), extra.read_bytes() if extra.is_file() else None) == before
    assert local_hook_values(repo) == []
    assert not ledger_path(schema, repo).exists()


@pytest.mark.parametrize("operation", ["install", "verify", "repair"])
@pytest.mark.parametrize(
    "mutation",
    ["entrypoint-noncanonical", "manifest-extra", "target-extra"],
)
def test_lifecycle_rejects_noncanonical_manifest_shapes(
    contract, tmp_path, operation, mutation
):
    schema, state = contract
    repo = init_repo(tmp_path, f"{operation}-{mutation}")
    provision_runtime(repo)
    manifest_path = (
        repo
        / state["hook_runtime"]["source"]
        / schema["runtime"]["manifest"]
    )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if mutation == "entrypoint-noncanonical":
        manifest["targets"][0]["entrypoint"] = "arbitrary-nonempty"
    elif mutation == "manifest-extra":
        manifest["unexpected"] = "shape-mutation"
    else:
        manifest["targets"][0]["unexpected"] = "shape-mutation"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    before = manifest_path.read_bytes()
    with pytest.raises(hooks.HookError):
        if operation == "install":
            hooks.install_runtime(schema, state, repo)
        elif operation == "verify":
            hooks.verify_installation(schema, state, repo)
        else:
            hooks.repair_runtime(
                schema,
                state,
                repo,
                ROOT / state["hook_runtime"]["source"],
            )
    assert manifest_path.read_bytes() == before
    assert local_hook_values(repo) == []
    assert not ledger_path(schema, repo).exists()


@pytest.mark.parametrize(
    ("mutation", "field"),
    [
        (lambda value: value["runtime"].pop("kind"), "runtime.kind"),
        (lambda value: value["runtime"].pop("hook_entrypoints"), "runtime.hook_entrypoints"),
        (
            lambda value: value["runtime"].update({"unexpected": "shape-mutation"}),
            "runtime",
        ),
        (
            lambda value: value["runtime"].update({"hook_entrypoints": ["prepare"]}),
            "runtime.hook_entrypoints",
        ),
        (
            lambda value: value["runtime"].update(
                {"hook_entrypoints": ["prepare", "prepare"]}
            ),
            "runtime.hook_entrypoints",
        ),
        (
            lambda value: value["runtime"].update(
                {"hook_entrypoints": ["prepare", "../final"]}
            ),
            "runtime.hook_entrypoints",
        ),
    ],
)
def test_runtime_schema_shape_mutations_fail_closed(contract, mutation, field):
    schema, _ = contract
    mutated = json.loads(json.dumps(schema))
    mutation(mutated)
    with pytest.raises(ci.ContractError) as error:
        ci.validate_schema(mutated)
    assert error.value.code == ci.Codes.SCHEMA_SHAPE
    assert error.value.field == field


def test_install_verify_rollback_unset_is_exact_and_idempotent(contract, tmp_path):
    schema, state = contract
    repo = init_repo(tmp_path)
    provision_runtime(repo)
    assert local_hook_values(repo) == []
    installed = hooks.install_runtime(schema, state, repo)
    assert installed["disposition"] == "installed"
    assert local_hook_values(repo) == [state["hook_runtime"]["source"]]
    assert ledger_path(schema, repo).exists()
    assert hooks.install_runtime(schema, state, repo)["disposition"] == "already-installed"
    assert hooks.verify_installation(schema, state, repo)["status"] == "valid"
    rolled = hooks.rollback_runtime(schema, state, repo)
    assert rolled["disposition"] == "rolled-back"
    assert local_hook_values(repo) == []
    assert not ledger_path(schema, repo).exists()
    assert hooks.rollback_runtime(schema, state, repo)["disposition"] == "already-rolled-back"


def test_init_state_derives_unborn_or_existing_destination_without_starter_anchor(
    contract, tmp_path
):
    schema, _ = contract
    unborn = init_repo(tmp_path, "unborn")
    provision_runtime(unborn)
    (unborn / ".tfw" / "commit_identity_state.json").unlink()
    result = hooks.initialize_project_state(schema, unborn)
    state = json.loads(
        (unborn / ".tfw" / "commit_identity_state.json").read_text(encoding="utf-8")
    )
    assert result["disposition"] == "unborn-root-inclusive"
    assert state["activation"]["last_pre_policy_commit"] is None
    assert state["activation"]["range_semantics"] == "root-inclusive"
    ci.validate_state(schema, state)

    existing = init_repo(tmp_path, "existing")
    provision_runtime(existing)
    anchor = initial_commit(existing)
    result = hooks.initialize_project_state(schema, existing)
    state = json.loads(
        (existing / ".tfw" / "commit_identity_state.json").read_text(encoding="utf-8")
    )
    assert result["disposition"] == "existing-history-exclusive"
    assert state["activation"]["last_pre_policy_commit"] == anchor
    assert state["activation"]["range_semantics"] == "exclusive-anchor"
    assert state["activation"]["pre_anchor_history"] == "excluded"
    ci.validate_state(schema, state)


def test_install_and_rollback_restore_opaque_prior_values_without_output(
    contract, tmp_path
):
    schema, state = contract
    repo = init_repo(tmp_path)
    provision_runtime(repo)
    sentinel = "OPAQUE_FIXTURE_VALUE_DO_NOT_EMIT"
    git(
        repo,
        "config",
        "--local",
        "--add",
        "core.hooksPath",
        sentinel,
        isolated=True,
    )
    result = hooks.install_runtime(schema, state, repo)
    assert sentinel not in json.dumps(result)
    private = json.loads(ledger_path(schema, repo).read_text(encoding="utf-8"))
    assert private["previous_local"]["values"] == [sentinel]
    rolled = hooks.rollback_runtime(schema, state, repo)
    assert sentinel not in json.dumps(rolled)
    assert local_hook_values(repo) == [sentinel]


def test_exact_owned_prior_lifecycle_is_stable_and_idempotent(contract, tmp_path):
    schema, state = contract
    repo = init_repo(tmp_path)
    provision_runtime(repo)
    git(
        repo,
        "config",
        "--local",
        "core.hooksPath",
        state["hook_runtime"]["source"],
        isolated=True,
    )
    installed = hooks.install_runtime(schema, state, repo)
    assert installed["disposition"] == "installed"
    private = json.loads(ledger_path(schema, repo).read_text(encoding="utf-8"))
    assert private["previous_local"]["values"] == [state["hook_runtime"]["source"]]
    assert hooks.install_runtime(schema, state, repo)["disposition"] == "already-installed"
    assert hooks.verify_installation(schema, state, repo)["status"] == "valid"
    source = ROOT / state["hook_runtime"]["source"]
    assert hooks.repair_runtime(schema, state, repo, source)["disposition"] == "already-valid"
    assert hooks.repair_runtime(schema, state, repo, source)["disposition"] == "already-valid"
    rolled = hooks.rollback_runtime(schema, state, repo)
    assert rolled["disposition"] == "rolled-back"
    assert rolled["local_config"] == "prior-relative-owned"
    assert local_hook_values(repo) == [state["hook_runtime"]["source"]]
    assert not ledger_path(schema, repo).exists()
    repeated = hooks.rollback_runtime(schema, state, repo)
    assert repeated["disposition"] == "already-rolled-back"
    assert repeated["local_config"] == "prior-relative-owned"
    assert local_hook_values(repo) == [state["hook_runtime"]["source"]]
    assert not ledger_path(schema, repo).exists()


def test_repair_recognized_drift_and_block_unknown_material(contract, tmp_path):
    schema, state = contract
    source = ROOT / state["hook_runtime"]["source"]
    repo = init_repo(tmp_path, "drift")
    provision_runtime(repo)
    drifted = repo / state["hook_runtime"]["source"] / schema["runtime"]["hook_targets"][0]
    drifted.write_text("recognized but drifted", encoding="utf-8")
    assert hooks._runtime_disposition(schema, drifted.parent) == "owned-drift"
    result = hooks.repair_runtime(schema, state, repo, source)
    assert result["disposition"] == "repaired"
    hooks.verify_installation(schema, state, repo)

    conflict = init_repo(tmp_path, "conflict")
    target = conflict / state["hook_runtime"]["source"]
    target.mkdir(parents=True)
    unknown = target / "unknown"
    unknown.write_text("DO_NOT_TOUCH", encoding="utf-8")
    before = unknown.read_bytes()
    with pytest.raises(hooks.HookError) as error:
        hooks.repair_runtime(schema, state, conflict, source)
    assert error.value.code == hooks.HookCodes.RUNTIME_CONFLICT
    assert unknown.read_bytes() == before
    assert local_hook_values(conflict) == []


def test_main_and_linked_worktree_share_one_ledger_and_runtime(contract, tmp_path):
    schema, state = contract
    repo = init_repo(tmp_path, "main")
    provision_runtime(repo)
    initial_commit(repo)
    linked = tmp_path / "linked"
    git(repo, "worktree", "add", "-q", "-b", "linked-branch", str(linked), isolated=True)
    hooks.install_runtime(schema, state, repo)
    assert common_dir(repo) == common_dir(linked)
    assert ledger_path(schema, repo) == ledger_path(schema, linked)
    assert hooks.verify_installation(schema, state, linked)["status"] == "valid"
    hooks.rollback_runtime(schema, state, linked)
    assert local_hook_values(repo) == []
    assert not ledger_path(schema, repo).exists()


def test_prepare_and_final_are_non_mutating_with_exact_or_absent_context(
    contract, tmp_path
):
    schema, state = contract
    repo = init_repo(tmp_path)
    message = repo / "message.txt"
    subject = ci.format_subject(schema, context(), "validate hook input")
    message.write_bytes((subject + "\n").encode("utf-8"))
    before = message.read_bytes()
    environment = {
        schema["runtime"]["expected_context_env"]: "codex/TFW-49/phase-c/executor"
    }
    for stage_name in ("prepare", "final"):
        result = hooks.validate_hook_stage(
            schema, state, repo, message, stage_name, environment
        )
        assert result["context_comparison"] == "exact-context"
        assert result["message_mutated"] is False
        assert message.read_bytes() == before
        structural = hooks.validate_hook_stage(
            schema, state, repo, message, stage_name, {}
        )
        assert structural["context_comparison"] == "structural-only"
        assert message.read_bytes() == before


@pytest.mark.parametrize(
    "token",
    [
        "codex",
        "codex/TFW-49",
        "codex/TFW-49/phase-c",
        "codex/TFW-49/phase-c/executor/extra",
        "codex//phase-c/executor",
    ],
)
def test_partial_or_malformed_expected_context_fails_without_message_mutation(
    contract, tmp_path, token
):
    schema, state = contract
    repo = init_repo(tmp_path)
    message = repo / "message.txt"
    message.write_text(
        "[codex/TFW-49/phase-c/executor] safe message\n", encoding="utf-8"
    )
    before = message.read_bytes()
    with pytest.raises((hooks.HookError, ci.ContractError)):
        hooks.validate_hook_stage(
            schema,
            state,
            repo,
            message,
            "prepare",
            {schema["runtime"]["expected_context_env"]: token},
        )
    assert message.read_bytes() == before


@pytest.mark.parametrize("field", list(CONTEXT_FIELDS))
def test_stale_expected_context_fails_for_each_field(contract, tmp_path, field):
    schema, state = contract
    repo = init_repo(tmp_path)
    current = context()
    stale = dict(current)
    stale[field] = {
        "surface": "cursor",
        "task": "TFW-50",
        "work": "phase-b",
        "role": "reviewer",
    }[field]
    subject = ci.format_subject(schema, current, "safe message")
    message = repo / "message.txt"
    message.write_text(subject + "\n", encoding="utf-8")
    token = "/".join(stale[name] for name in CONTEXT_FIELDS)
    with pytest.raises(ci.ContractError) as error:
        hooks.validate_hook_stage(
            schema,
            state,
            repo,
            message,
            "final",
            {schema["runtime"]["expected_context_env"]: token},
        )
    assert error.value.code == ci.Codes.CONTEXT_MISMATCH


def test_four_surfaces_by_four_roles_are_synthetic_contract_coverage(
    contract, tmp_path
):
    schema, state = contract
    repo = init_repo(tmp_path)
    message = repo / "message.txt"
    observed = set()
    for surface, role in itertools.product(
        schema["registries"]["surfaces"], schema["registries"]["roles"]
    ):
        fields = context(surface=surface, role=role)
        message.write_text(
            ci.format_subject(schema, fields, "synthetic registry result") + "\n",
            encoding="utf-8",
        )
        token = "/".join(fields[name] for name in CONTEXT_FIELDS)
        result = hooks.validate_hook_stage(
            schema,
            state,
            repo,
            message,
            "final",
            {schema["runtime"]["expected_context_env"]: token},
        )
        assert result["actor_authentication"] is False
        observed.add((surface, role))
    assert len(observed) == 16


def test_seven_router_operations_reach_prepare_and_final_without_new_policy(
    contract, tmp_path
):
    schema, state = contract
    repo = init_repo(tmp_path)
    current = context()
    ordinary = ci.format_subject(schema, current, "source result")
    cases = {
        "ordinary": {"summary": "ordinary result"},
        "merge": {"summary": "merge result"},
        "amend": {"existing_subject": ordinary, "summary": "amend result"},
        "fixup": {"target_subject": ordinary, "summary": None},
        "squash": {"target_subject": ordinary, "summary": None},
        "revert": {"source_subject": ordinary, "summary": None},
        "cherry-pick": {"source_subject": ordinary, "summary": None},
    }
    token = "/".join(current[name] for name in CONTEXT_FIELDS)
    for operation, inputs in cases.items():
        routed = plan(contract, repo, operation=operation, **inputs)
        message = repo / f"{operation}.txt"
        text = routed["subject"]
        if routed["trailers"]:
            text += "\n\n" + "\n".join(
                f"{record['name']}: {record['value']}"
                for record in routed["trailers"]
            )
        message.write_text(text + "\n", encoding="utf-8")
        for stage_name in ("prepare", "final"):
            assert hooks.validate_hook_stage(
                schema,
                state,
                repo,
                message,
                stage_name,
                {schema["runtime"]["expected_context_env"]: token},
            )["status"] == "valid"


def test_carrier_runs_real_windows_git_commit_with_child_only_context(
    contract, tmp_path, monkeypatch
):
    schema, state = contract
    repo = init_repo(tmp_path)
    provision_runtime(repo)
    hooks.install_runtime(schema, state, repo)
    stage(repo)
    routed = plan(contract, repo)
    env_name = schema["runtime"]["expected_context_env"]
    monkeypatch.delenv(env_name, raising=False)
    result = hooks.run_local_commit(schema, state, repo, routed)
    assert result["status"] == "committed"
    assert result["actor_authentication"] is False
    assert result["publication_authority"] is False
    assert os.environ.get(env_name) is None
    assert git(repo, "show", "-s", "--format=%s", "HEAD").stdout.strip() == (
        routed["subject"]
    )


def test_carrier_rejects_forged_plan_and_unknown_operation(contract, tmp_path):
    schema, state = contract
    repo = init_repo(tmp_path)
    provision_runtime(repo)
    hooks.install_runtime(schema, state, repo)
    stage(repo)
    routed = plan(contract, repo)
    forged = copy.deepcopy(routed)
    forged["publication_authority"] = True
    with pytest.raises(hooks.HookError) as error:
        hooks.run_local_commit(schema, state, repo, forged)
    assert error.value.code == hooks.HookCodes.PLAN
    with pytest.raises(router.RouterError):
        plan(contract, repo, operation="push")


def test_actual_git_hooks_reject_stale_context_and_accept_structural_only(
    contract, tmp_path
):
    schema, state = contract
    repo = init_repo(tmp_path)
    provision_runtime(repo)
    hooks.install_runtime(schema, state, repo)
    subject = ci.format_subject(schema, context(), "structural direct result")
    direct = git(repo, "commit", "--allow-empty", "-m", subject)
    assert "W_CONTEXT_ABSENT" in direct.stderr
    stale_env = os.environ.copy()
    stale_env[schema["runtime"]["expected_context_env"]] = (
        "cursor/TFW-49/phase-c/executor"
    )
    rejected = git(
        repo,
        "commit",
        "--allow-empty",
        "-m",
        subject,
        check=False,
        env=stale_env,
    )
    assert rejected.returncode != 0
    assert subject not in rejected.stderr
    assert "E_CONTEXT_MISMATCH" in rejected.stderr


def test_diagnostics_do_not_echo_message_path_environment_or_private_value(
    contract, tmp_path, capsys, monkeypatch
):
    schema, state = contract
    repo = init_repo(tmp_path)
    provision_runtime(repo)
    sentinel = "LEAK_api_key_sk-EXAMPLE"
    message = repo / f"{sentinel}.txt"
    message.write_text(f"invalid {sentinel}\n", encoding="utf-8")
    monkeypatch.setenv("TFW_HOOK_FIXTURE_SECRET", sentinel)
    assert (
        hooks.main(
            [
                "prepare",
                "--repo",
                str(repo),
                "--message-file",
                str(message),
            ]
        )
        == 2
    )
    output = capsys.readouterr()
    assert sentinel not in output.out + output.err
    assert str(repo) not in output.out + output.err
    assert "Traceback" not in output.err


def test_production_source_has_no_external_discovery_or_remote_executor(contract):
    schema, _ = contract
    source = SCRIPT.read_text(encoding="utf-8")
    for forbidden in (
        "--global",
        "--show-origin",
        "git push",
        "git fetch",
        "git remote",
        "os.environ.clear",
    ):
        assert forbidden not in source
    for accepted in (
        *schema["registries"]["surfaces"],
        *schema["registries"]["roles"],
        *schema["registries"]["range_semantics"],
    ):
        assert f'"{accepted}"' not in source and f"'{accepted}'" not in source


def test_command_spy_observes_local_only_git_lifecycle(contract, tmp_path, monkeypatch):
    schema, state = contract
    repo = init_repo(tmp_path)
    provision_runtime(repo)
    observed: list[tuple[str, ...]] = []
    original = hooks._run_git

    def spy(repo_path, args, **kwargs):
        observed.append(tuple(args))
        return original(repo_path, args, **kwargs)

    monkeypatch.setattr(hooks, "_run_git", spy)
    hooks.install_runtime(schema, state, repo)
    hooks.verify_installation(schema, state, repo)
    hooks.rollback_runtime(schema, state, repo)
    flattened = "\n".join(" ".join(args) for args in observed)
    assert "--local" in flattened
    for forbidden in ("--global", "--show-origin", "push", "fetch", "remote"):
        assert forbidden not in flattened


def test_private_ledger_is_outside_worktree_and_untracked(contract, tmp_path):
    schema, state = contract
    repo = init_repo(tmp_path)
    provision_runtime(repo)
    hooks.install_runtime(schema, state, repo)
    ledger = ledger_path(schema, repo)
    assert ledger.exists()
    status = git(repo, "status", "--porcelain=v1", "-uall", isolated=True).stdout
    assert "commit_identity_runtime.json" not in status
    assert ledger.is_relative_to(common_dir(repo))


def test_declared_windows_and_ubuntu_wsl_versions_and_hook_launch(
    contract, tmp_path
):
    schema, state = contract
    assert git(ROOT, "--version", isolated=True).stdout.strip() == (
        "git version 2.42.0.windows.1"
    )
    windows_python = subprocess.run(
        [sys.executable, "--version"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    ).stdout.strip()
    assert windows_python == "Python 3.13.5"
    wsl_git = subprocess.run(
        ["wsl.exe", "-d", "Ubuntu", "--", "git", "--version"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    ).stdout.strip()
    wsl_python = subprocess.run(
        ["wsl.exe", "-d", "Ubuntu", "--", "python3", "--version"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    ).stdout.strip()
    assert wsl_git == "git version 2.43.0"
    assert wsl_python == "Python 3.12.3"

    repo = init_repo(tmp_path)
    provision_runtime(repo)
    hooks.install_runtime(schema, state, repo)
    stage(repo, "wsl.txt")
    windows_path = repo.resolve()
    converted = (
        f"/mnt/{windows_path.drive[0].lower()}/"
        + windows_path.as_posix().split(":/", 1)[1]
    )
    subject = "[codex/TFW-49/phase-c/executor] exercise Ubuntu WSL runtime"
    command = (
        f"cd {json.dumps(converted)} && "
        "TFW_COMMIT_EXPECTED_CONTEXT=codex/TFW-49/phase-c/executor "
        f"git commit -m {json.dumps(subject)}"
    )
    result = subprocess.run(
        ["wsl.exe", "-d", "Ubuntu", "--", "sh", "-lc", command],
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert git(repo, "show", "-s", "--format=%s", "HEAD").stdout.strip() == subject


def test_cli_lifecycle_and_commit_payloads_are_safe(contract, tmp_path, capsys):
    repo = init_repo(tmp_path)
    provision_runtime(repo)
    assert hooks.main(["install", "--repo", str(repo)]) == 0
    installed = json.loads(capsys.readouterr().out)
    assert installed["publication_authority"] is False
    assert installed["actor_authentication"] is False
    stage(repo)
    assert (
        hooks.main(
            [
                "commit",
                "--repo",
                str(repo),
                "--workflow",
                "handoff",
                "--surface",
                "codex",
                "--task",
                "TFW-49",
                "--work",
                "phase-c",
                "--role",
                "executor",
                "--operation",
                "ordinary",
                "--summary",
                "exercise CLI carrier",
            ]
        )
        == 0
    )
    committed = json.loads(capsys.readouterr().out)
    assert committed["status"] == "committed"
    assert committed["publication_authority"] is False


def test_phase_c_workflow_gates_and_state_preservation_are_explicit():
    canonical = {
        name: (ROOT / ".tfw" / "workflows" / f"{name}.md").read_text(
            encoding="utf-8"
        )
        for name in ("init", "update", "handoff", "review", "release")
    }
    assert "commit_identity_hooks.py init-state" in canonical["init"]
    assert "commit_identity_hooks.py install" in canonical["init"]
    assert "commit_identity_hooks.py verify" in canonical["init"]
    assert "commit_identity_state.json" in canonical["update"]
    assert "NEVER overwrite" in canonical["update"]
    assert "commit_identity_hooks.py repair" in canonical["update"]
    assert "commit_identity_hooks.py verify" in canonical["update"]
    assert "commit_identity_hooks.py commit --workflow handoff" in canonical["handoff"]
    assert "commit_identity_hooks.py commit --workflow review" in canonical["review"]
    assert "commit_identity_hooks.py commit --workflow release" in canonical["release"]
    for name in ("handoff", "review", "release"):
        assert "commit_identity.py audit-range" in canonical[name]
        assert "publication" in canonical[name].lower()
    for text in canonical.values():
        assert "git config --global" not in text
        assert "--show-origin" not in text


def test_exact_five_canonical_workflows_have_ten_byte_exact_derived_copies():
    for name in ("init", "update", "handoff", "review", "release"):
        source = ROOT / ".tfw" / "workflows" / f"{name}.md"
        assert source.read_bytes() == (
            ROOT / ".agent" / "workflows" / f"tfw-{name}.md"
        ).read_bytes()
        assert source.read_bytes() == (
            ROOT / ".claude" / "commands" / f"tfw-{name}.md"
        ).read_bytes()


def test_phase_c_claim_language_keeps_structural_live_and_client_boundaries_distinct():
    conventions = (ROOT / ".tfw" / "conventions.md").read_text(encoding="utf-8")
    glossary = (ROOT / ".tfw" / "glossary.md").read_text(encoding="utf-8")
    for required in (
        "root-inclusive",
        "Git-common-dir ledger",
        "TFW_COMMIT_EXPECTED_CONTEXT",
        "structural-only",
        "Codex with the",
        "not actor authentication",
    ):
        assert required in conventions
    assert "Commit Identity Project State" in glossary
    assert "Commit Identity Runtime" in glossary
    assert "Commit Identity Runtime Ledger" in glossary
