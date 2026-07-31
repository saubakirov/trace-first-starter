from __future__ import annotations

import ast
import copy
import importlib.util
import itertools
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = Path(__file__).with_name("commit_identity_router.py")
SCRIPTS = SCRIPT.parent
sys.path.insert(0, str(SCRIPTS))
try:
    SPEC = importlib.util.spec_from_file_location("commit_identity_router", SCRIPT)
    assert SPEC and SPEC.loader
    router = importlib.util.module_from_spec(SPEC)
    sys.modules[SPEC.name] = router
    SPEC.loader.exec_module(router)
finally:
    sys.path.remove(str(SCRIPTS))
ci = router.ci


WORKFLOW_CASES = {
    "plan": ("coordinator", "TFW-49", "master"),
    "research": ("researcher", "TFW-49", "research-iter1"),
    "handoff": ("executor", "TFW-49", "phase-b"),
    "review": ("reviewer", "TFW-49", "phase-b"),
    "resume": ("coordinator", "TFW-49", "master"),
    "docs": ("coordinator", "TFW-49", "docs"),
    "knowledge": ("coordinator", "TFW-49", "knowledge"),
    "release": ("coordinator", "TFW-49", "release"),
    "update": ("coordinator", "TFW-49", "update"),
    "config": ("coordinator", "TFW-49", "config"),
    "init": ("coordinator", "TFW-1", "init"),
}

CANONICAL_WORKFLOWS = {
    "plan": ROOT / ".tfw" / "workflows" / "plan.md",
    "research": ROOT / ".tfw" / "workflows" / "research" / "base.md",
    "handoff": ROOT / ".tfw" / "workflows" / "handoff.md",
    "review": ROOT / ".tfw" / "workflows" / "review.md",
    "resume": ROOT / ".tfw" / "workflows" / "resume.md",
    "docs": ROOT / ".tfw" / "workflows" / "docs.md",
    "knowledge": ROOT / ".tfw" / "workflows" / "knowledge.md",
    "release": ROOT / ".tfw" / "workflows" / "release.md",
    "update": ROOT / ".tfw" / "workflows" / "update.md",
    "config": ROOT / ".tfw" / "workflows" / "config.md",
    "init": ROOT / ".tfw" / "workflows" / "init.md",
}


@pytest.fixture
def contract():
    return ci.load_contract()


def context(
    *,
    surface: str = "codex",
    task: str = "TFW-49",
    work: str = "phase-b",
    role: str = "executor",
) -> dict[str, str]:
    return {"surface": surface, "task": task, "work": work, "role": role}


def route(contract, **overrides):
    schema, state = contract
    values = {
        "workflow": "handoff",
        **context(),
        "operation": "ordinary",
        "summary": "implement routed result",
        "staged_paths": [],
    }
    values.update(overrides)
    return router.route_operation(schema, state, **values)


def git(repo: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        [
            "git",
            "-c",
            "core.hooksPath=.tfw/hooks",
            "-c",
            "user.name=TFW Router Fixture",
            "-c",
            "user.email=router@example.invalid",
            "-C",
            str(repo),
            *args,
        ],
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check:
        assert result.returncode == 0, result.stderr
    return result.stdout.strip()


def init_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    return repo


def commit_message(repo: Path, message: str) -> str:
    git(repo, "commit", "--allow-empty", "-m", message)
    return git(repo, "show", "-s", "--format=%B", "HEAD")


def test_exact_11_workflow_context_map_is_schema_backed(contract):
    schema, _ = contract
    records = {item["workflow"]: item for item in router.describe_workflows(schema)}
    assert list(records) == list(WORKFLOW_CASES)
    assert len(records) == 11
    for workflow, (role, task, work) in WORKFLOW_CASES.items():
        assert records[workflow]["role"] == role
        resolved = router.resolve_workflow_context(
            schema,
            workflow=workflow,
            surface="codex",
            task=task,
            work=work,
            role=role,
            staged_paths=[],
        )
        assert resolved == context(task=task, work=work, role=role)


@pytest.mark.parametrize("workflow", list(WORKFLOW_CASES))
@pytest.mark.parametrize("surface", ["antigravity", "claude-code", "codex", "cursor"])
def test_every_workflow_and_surface_resolves(contract, workflow, surface):
    schema, _ = contract
    role, task, work = WORKFLOW_CASES[workflow]
    resolved = router.resolve_workflow_context(
        schema,
        workflow=workflow,
        surface=surface,
        task=task,
        work=work,
        role=role,
        staged_paths=[],
    )
    assert resolved["surface"] == surface
    assert resolved["role"] == role


def test_unknown_workflow_and_wrong_role_fail_closed(contract):
    schema, _ = contract
    with pytest.raises(router.RouterError) as error:
        router.resolve_workflow_context(
            schema,
            workflow="task",
            **context(),
            staged_paths=[],
        )
    assert error.value.code == router.RouterCodes.WORKFLOW
    with pytest.raises(router.RouterError) as error:
        router.resolve_workflow_context(
            schema,
            workflow="handoff",
            **context(role="reviewer"),
            staged_paths=[],
        )
    assert error.value.code == router.RouterCodes.ROLE


@pytest.mark.parametrize(
    ("workflow", "work"),
    [
        ("plan", "docs"),
        ("research", "phase-b"),
        ("handoff", "research-iter1"),
        ("review", "knowledge"),
        ("resume", "release"),
        ("docs", "knowledge"),
        ("knowledge", "release"),
        ("release", "update"),
        ("update", "config"),
        ("config", "init"),
        ("init", "master"),
    ],
)
def test_workflow_work_mismatches_fail(contract, workflow, work):
    schema, _ = contract
    role, task, _ = WORKFLOW_CASES[workflow]
    with pytest.raises(router.RouterError) as error:
        router.resolve_workflow_context(
            schema,
            workflow=workflow,
            surface="codex",
            task=task,
            work=work,
            role=role,
            staged_paths=[],
        )
    assert error.value.code == router.RouterCodes.WORK


def test_known_work_normalization_is_consumed_from_phase_a(contract):
    schema, _ = contract
    resolved = router.resolve_workflow_context(
        schema,
        workflow="handoff",
        surface="codex",
        task="TFW-49",
        work="PhaseB",
        role="executor",
        staged_paths=[],
    )
    assert resolved["work"] == "phase-b"


def test_schema_role_mutation_changes_router_behavior_without_fallback(contract):
    schema, _ = contract
    fixture = copy.deepcopy(schema)
    fixture["registries"]["roles"][0] = "fixture-coordinator"
    fixture["diagnostic_example"]["role"] = "fixture-coordinator"
    ci.validate_schema(fixture)
    records = {item["workflow"]: item for item in router.describe_workflows(fixture)}
    assert records["plan"]["role"] == "fixture-coordinator"
    with pytest.raises(router.RouterError) as error:
        router.resolve_workflow_context(
            fixture,
            workflow="plan",
            surface="codex",
            task="TFW-49",
            work="master",
            role="coordinator",
            staged_paths=[],
        )
    assert error.value.code == router.RouterCodes.ROLE
    assert router.resolve_workflow_context(
        fixture,
        workflow="plan",
        surface="codex",
        task="TFW-49",
        work="master",
        role="fixture-coordinator",
        staged_paths=[],
    )["role"] == "fixture-coordinator"


def test_schema_fixed_work_mutation_changes_router_behavior(contract):
    schema, _ = contract
    fixture = copy.deepcopy(schema)
    fixture["registries"]["non_task_work"][0] = "fixture-docs"
    ci.validate_schema(fixture)
    with pytest.raises(router.RouterError):
        router.resolve_workflow_context(
            fixture,
            workflow="docs",
            surface="codex",
            task="TFW-49",
            work="docs",
            role="coordinator",
            staged_paths=[],
        )
    resolved = router.resolve_workflow_context(
        fixture,
        workflow="docs",
        surface="codex",
        task="TFW-49",
        work="fixture-docs",
        role="coordinator",
        staged_paths=[],
    )
    assert resolved["work"] == "fixture-docs"


@pytest.mark.parametrize(
    "workflow",
    ["plan", "research", "handoff", "review", "resume", "docs", "init"],
)
def test_task_none_is_rejected_for_task_owned_workflows(contract, workflow):
    schema, _ = contract
    role, _, work = WORKFLOW_CASES[workflow]
    with pytest.raises(router.RouterError) as error:
        router.resolve_workflow_context(
            schema,
            workflow=workflow,
            surface="codex",
            task="none",
            work=work,
            role=role,
            non_task=True,
            staged_paths=[],
        )
    assert error.value.code == router.RouterCodes.TASK


@pytest.mark.parametrize("workflow", ["knowledge", "release", "update", "config"])
def test_guarded_none_requires_declaration_and_staged_path_check(contract, workflow):
    schema, _ = contract
    role, _, work = WORKFLOW_CASES[workflow]
    with pytest.raises(ci.ContractError) as error:
        router.resolve_workflow_context(
            schema,
            workflow=workflow,
            surface="codex",
            task="none",
            work=work,
            role=role,
            staged_paths=[],
        )
    assert error.value.code == ci.Codes.TASK_NONE_DECLARATION
    with pytest.raises(ci.ContractError) as error:
        router.resolve_workflow_context(
            schema,
            workflow=workflow,
            surface="codex",
            task="none",
            work=work,
            role=role,
            non_task=True,
            staged_paths=None,
        )
    assert error.value.code == ci.Codes.TASK_NONE_PATHS
    resolved = router.resolve_workflow_context(
        schema,
        workflow=workflow,
        surface="codex",
        task="none",
        work=work,
        role=role,
        non_task=True,
        staged_paths=[],
    )
    assert resolved["task"] == "none"


def test_guarded_none_routes_an_ordinary_lifecycle_commit(contract):
    plan = route(
        contract,
        workflow="release",
        task="none",
        work="release",
        role="coordinator",
        non_task=True,
        staged_paths=[],
        summary="record repository lifecycle result",
    )
    assert plan["subject"] == (
        "[codex/none/release/coordinator] record repository lifecycle result"
    )
    assert plan["publication_authority"] is False


def test_task_none_source_is_structurally_comparable_for_cross_context_replay(
    contract,
):
    schema, _ = contract
    source = ci.format_subject(
        schema,
        context(task="none", work="release", role="coordinator"),
        "record repository lifecycle result",
        non_task=True,
        staged_paths=[],
    )
    plan = route(
        contract,
        operation="cherry-pick",
        source_subject=source,
        summary="replay lifecycle result for current task",
    )
    assert plan["source_relation"] == "cross-context"
    assert plan["disposition"] == "no-commit-inspect-current-context"
    assert plan["git_option"] == "--no-commit"
    assert plan["subject"].startswith("[codex/TFW-49/phase-b/executor] ")


def test_task_scoped_work_rejects_non_task_and_mixed_staged_paths(contract):
    schema, _ = contract
    with pytest.raises(router.RouterError) as error:
        router.resolve_workflow_context(
            schema,
            workflow="docs",
            surface="codex",
            task="TFW-49",
            work="docs",
            role="coordinator",
            non_task=True,
            staged_paths=[],
        )
    assert error.value.code == router.RouterCodes.NON_TASK
    with pytest.raises(router.RouterError) as error:
        router.resolve_workflow_context(
            schema,
            workflow="docs",
            surface="codex",
            task="TFW-49",
            work="docs",
            role="coordinator",
            staged_paths=[
                "tasks/TFW-49__identity/phase-b/RF.md",
                "tasks/TFW-48__method/phase-c/RF.md",
            ],
        )
    assert error.value.code == router.RouterCodes.STAGED_TASK


@pytest.mark.parametrize("operation", ["ordinary", "merge"])
def test_ordinary_and_merge_produce_current_context(contract, operation):
    plan = route(contract, operation=operation, summary="route current result")
    assert plan["subject"] == "[codex/TFW-49/phase-b/executor] route current result"
    assert plan["publication_authority"] is False
    assert plan["actor_authentication"] is False
    assert plan["hook_runtime_installed"] is False
    assert plan["inspection_required"] is False
    assert plan["git_option"] is None


@pytest.mark.parametrize("field", ["surface", "task", "work", "role"])
def test_amend_reidentifies_every_changed_context_field(contract, field):
    schema, _ = contract
    current = context()
    stale = dict(current)
    stale[field] = {
        "surface": "cursor",
        "task": "TFW-50",
        "work": "phase-a",
        "role": "reviewer",
    }[field]
    existing = ci.format_subject(schema, stale, "old result")
    plan = route(
        contract,
        operation="amend",
        existing_subject=existing,
        summary="correct current result",
    )
    assert plan["disposition"] == "amend-reidentify-current-context"
    assert plan["source_relation"] == "cross-context"
    assert plan["subject"].startswith("[codex/TFW-49/phase-b/executor] ")


def test_amend_preserves_only_exact_current_context(contract):
    schema, _ = contract
    existing = ci.format_subject(schema, context(), "old result")
    plan = route(
        contract,
        operation="amend",
        existing_subject=existing,
        summary="reword result",
    )
    assert plan["disposition"] == "amend-same-context"
    assert plan["source_relation"] == "same-context"


@pytest.mark.parametrize("operation", ["fixup", "squash"])
def test_same_context_autosquash_uses_schema_owned_reserved_form(contract, operation):
    schema, _ = contract
    target = ci.format_subject(schema, context(), "target result")
    plan = route(contract, operation=operation, target_subject=target, summary=None)
    record = next(
        item for item in schema["grammar"]["reserved_forms"] if item["name"] == operation
    )
    assert plan["subject"] == f"{record['prefix']}{target}{record['suffix']}"
    assert plan["disposition"] == "same-context-reserved"


@pytest.mark.parametrize("operation", ["fixup", "squash"])
@pytest.mark.parametrize("field", ["surface", "task", "work", "role"])
def test_cross_context_autosquash_is_rejected(contract, operation, field):
    schema, _ = contract
    stale = context()
    stale[field] = {
        "surface": "cursor",
        "task": "TFW-50",
        "work": "phase-a",
        "role": "reviewer",
    }[field]
    target = ci.format_subject(schema, stale, "target result")
    with pytest.raises(router.RouterError) as error:
        route(contract, operation=operation, target_subject=target, summary=None)
    assert error.value.code == router.RouterCodes.AUTOSQUASH_CONTEXT


def test_reserved_autosquash_target_cannot_be_nested(contract):
    schema, _ = contract
    target = ci.format_subject(schema, context(), "target result")
    reserved = router._wrap_reserved(schema, "fixup", target)
    with pytest.raises(router.RouterError) as error:
        route(contract, operation="squash", target_subject=reserved, summary=None)
    assert error.value.code == router.RouterCodes.TARGET


@pytest.mark.parametrize("operation", ["revert", "cherry-pick"])
def test_same_context_generated_replay_keeps_truthful_identity(contract, operation):
    schema, _ = contract
    source = ci.format_subject(schema, context(), "source result")
    plan = route(
        contract,
        operation=operation,
        source_subject=source,
        summary=None,
    )
    assert plan["disposition"] == "generated-replay-same-context"
    assert plan["source_relation"] == "same-context"
    assert plan["git_option"] is None
    if operation == "cherry-pick":
        assert plan["subject"] == source
    else:
        assert plan["subject"] == router._wrap_reserved(schema, "revert", source)


@pytest.mark.parametrize("operation", ["revert", "cherry-pick"])
@pytest.mark.parametrize("field", ["surface", "task", "work", "role"])
def test_cross_context_replay_requires_no_commit_and_current_operator(
    contract, operation, field
):
    schema, _ = contract
    stale = context()
    stale[field] = {
        "surface": "cursor",
        "task": "TFW-50",
        "work": "phase-a",
        "role": "reviewer",
    }[field]
    source = ci.format_subject(schema, stale, "source result")
    plan = route(
        contract,
        operation=operation,
        source_subject=source,
        summary=f"{operation} source result safely",
    )
    assert plan["disposition"] == "no-commit-inspect-current-context"
    assert plan["source_relation"] == "cross-context"
    assert plan["git_option"] == "--no-commit"
    assert plan["inspection_required"] is True
    assert plan["subject"].startswith("[codex/TFW-49/phase-b/executor] ")
    for value in stale.values():
        if value not in context().values():
            assert value not in plan["subject"]


def test_reserved_same_context_revert_source_uses_explicit_no_commit_flow(contract):
    schema, _ = contract
    ordinary = ci.format_subject(schema, context(), "target result")
    reserved = router._wrap_reserved(schema, "fixup", ordinary)
    plan = route(
        contract,
        operation="revert",
        source_subject=reserved,
        summary="revert reserved source safely",
    )
    assert plan["disposition"] == "no-commit-inspect-current-context"
    assert plan["source_relation"] == "reserved-source"


@pytest.mark.parametrize(
    ("operation", "missing_field", "code"),
    [
        ("ordinary", "summary", router.RouterCodes.SUMMARY),
        ("merge", "summary", router.RouterCodes.SUMMARY),
        ("amend", "existing_subject", router.RouterCodes.EXISTING),
        ("fixup", "target_subject", router.RouterCodes.TARGET),
        ("squash", "target_subject", router.RouterCodes.TARGET),
        ("revert", "source_subject", router.RouterCodes.SOURCE),
        ("cherry-pick", "source_subject", router.RouterCodes.SOURCE),
    ],
)
def test_operation_inputs_are_explicit(contract, operation, missing_field, code):
    values = {
        "operation": operation,
        "summary": "result",
        "existing_subject": "[codex/TFW-49/phase-b/executor] old",
        "target_subject": "[codex/TFW-49/phase-b/executor] target",
        "source_subject": "[codex/TFW-49/phase-b/executor] source",
    }
    values[missing_field] = None
    with pytest.raises(router.RouterError) as error:
        route(contract, **values)
    assert error.value.code == code


def test_unknown_operation_fails_without_action(contract):
    with pytest.raises(router.RouterError) as error:
        route(contract, operation="push")
    assert error.value.code == router.RouterCodes.OPERATION


def test_source_and_content_origin_trailers_are_schema_owned(contract):
    schema, _ = contract
    source = ci.format_subject(
        schema,
        context(surface="cursor", work="phase-a", role="reviewer"),
        "source result",
    )
    object_id = "0123456789abcdef0123456789abcdef01234567"
    origin = "claude-code/TFW-49/phase-b/executor"
    plan = route(
        contract,
        operation="cherry-pick",
        source_subject=source,
        summary="apply source safely",
        source_commit=object_id,
        content_origins=[origin],
    )
    assert plan["trailers"] == [
        {"name": schema["trailers"]["source_commit"], "value": object_id},
        {"name": schema["trailers"]["content_origin"], "value": origin},
    ]
    assert all(
        item["name"] in schema["trailers"].values() for item in plan["trailers"]
    )


def test_source_commit_is_rejected_outside_replay(contract):
    with pytest.raises(router.RouterError) as error:
        route(
            contract,
            operation="ordinary",
            source_commit="0123456789abcdef0123456789abcdef01234567",
        )
    assert error.value.code == router.RouterCodes.SOURCE


@pytest.mark.parametrize(
    ("field", "value", "code"),
    [
        ("source_commit", "short", ci.Codes.TRAILER_VALUE),
        ("content_origins", ["codex/executor"], ci.Codes.ORIGIN),
    ],
)
def test_invalid_optional_provenance_fails_through_phase_a(
    contract, field, value, code
):
    schema, _ = contract
    source = ci.format_subject(
        schema,
        context(surface="cursor", work="phase-a", role="reviewer"),
        "source result",
    )
    values = {
        "operation": "revert",
        "source_subject": source,
        "summary": "revert source safely",
        field: value,
    }
    with pytest.raises(ci.ContractError) as error:
        route(contract, **values)
    assert error.value.code == code


@pytest.mark.parametrize(
    ("operation", "expected_disposition"),
    [
        ("ordinary", "current-context-commit"),
        ("merge", "current-context-merge-commit"),
        ("amend", "amend-same-context"),
        ("fixup", "same-context-reserved"),
        ("squash", "same-context-reserved"),
        ("revert", "generated-replay-same-context"),
        ("cherry-pick", "generated-replay-same-context"),
    ],
)
def test_temporary_git_same_context_operation_matrix(
    contract, tmp_path, operation, expected_disposition
):
    schema, _ = contract
    repo = init_repo(tmp_path)
    stored_message = commit_message(
        repo,
        ci.format_subject(schema, context(), "stored current-context result"),
    )
    stored_subject = stored_message.splitlines()[0]
    inputs = {
        "operation": operation,
        "summary": (
            None
            if operation in {"fixup", "squash", "revert", "cherry-pick"}
            else f"plan {operation} result"
        ),
    }
    if operation == "amend":
        inputs["existing_subject"] = stored_subject
    elif operation in {"fixup", "squash"}:
        inputs["target_subject"] = stored_subject
    elif operation in {"revert", "cherry-pick"}:
        inputs["source_subject"] = stored_subject
    plan = route(contract, **inputs)
    assert plan["disposition"] == expected_disposition
    committed = commit_message(repo, plan["subject"])
    parsed = ci.validate_message(schema, committed, expected=context())
    assert parsed.fields == context()


@pytest.mark.parametrize(
    ("operation", "expected"),
    [
        ("amend", "amend-reidentify-current-context"),
        ("fixup", router.RouterCodes.AUTOSQUASH_CONTEXT),
        ("squash", router.RouterCodes.AUTOSQUASH_CONTEXT),
        ("revert", "no-commit-inspect-current-context"),
        ("cherry-pick", "no-commit-inspect-current-context"),
    ],
)
def test_temporary_git_cross_context_operation_matrix(
    contract, tmp_path, operation, expected
):
    schema, _ = contract
    repo = init_repo(tmp_path)
    stored_message = commit_message(
        repo,
        ci.format_subject(
            schema,
            context(surface="cursor", task="TFW-50", work="phase-a", role="reviewer"),
            "stored cross-context result",
        ),
    )
    stored_subject = stored_message.splitlines()[0]
    inputs = {
        "operation": operation,
        "summary": (
            None
            if operation in {"fixup", "squash"}
            else f"route {operation} through current context"
        ),
    }
    if operation == "amend":
        inputs["existing_subject"] = stored_subject
    elif operation in {"fixup", "squash"}:
        inputs["target_subject"] = stored_subject
    else:
        inputs["source_subject"] = stored_subject
    if operation in {"fixup", "squash"}:
        with pytest.raises(router.RouterError) as error:
            route(contract, **inputs)
        assert error.value.code == expected
        return
    plan = route(contract, **inputs)
    assert plan["disposition"] == expected
    assert plan["subject"].startswith("[codex/TFW-49/phase-b/executor] ")
    if operation in {"revert", "cherry-pick"}:
        assert plan["git_option"] == "--no-commit"


def test_temporary_git_replay_trailers_validate_through_phase_a(
    contract, tmp_path
):
    schema, _ = contract
    repo = init_repo(tmp_path)
    source_message = commit_message(
        repo,
        ci.format_subject(
            schema,
            context(surface="cursor", task="TFW-50", work="phase-a", role="reviewer"),
            "stored source result",
        ),
    )
    source_subject = source_message.splitlines()[0]
    source_oid = git(repo, "rev-parse", "HEAD")
    plan = route(
        contract,
        operation="cherry-pick",
        source_subject=source_subject,
        source_commit=source_oid,
        content_origins=["cursor/TFW-50/phase-a/reviewer"],
        summary="replay source through current context",
    )
    message = plan["subject"] + "\n\n" + "\n".join(
        f"{item['name']}: {item['value']}" for item in plan["trailers"]
    )
    committed = commit_message(repo, message)
    parsed = ci.validate_message(schema, committed, expected=context())
    assert parsed.fields == context()
    assert source_oid in committed
    assert schema["trailers"]["content_origin"] in committed


def test_task_none_route_uses_real_staged_path_guard(contract, tmp_path):
    repo = init_repo(tmp_path)
    schema, state = contract
    result = router.route_operation(
        schema,
        state,
        workflow="update",
        surface="codex",
        task="none",
        work="update",
        role="coordinator",
        operation="ordinary",
        summary="maintain non-task runtime",
        non_task=True,
        staged_paths=ci.staged_paths(repo),
    )
    assert result["context"]["task"] == "none"
    task_file = repo / "tasks" / "TFW-49__identity" / "x.txt"
    task_file.parent.mkdir(parents=True)
    task_file.write_text("x", encoding="utf-8")
    git(repo, "add", "--", "tasks/TFW-49__identity/x.txt")
    with pytest.raises(ci.ContractError) as error:
        router.route_operation(
            schema,
            state,
            workflow="update",
            surface="codex",
            task="none",
            work="update",
            role="coordinator",
            operation="ordinary",
            summary="maintain non-task runtime",
            non_task=True,
            staged_paths=ci.staged_paths(repo),
        )
    assert error.value.code == ci.Codes.TASK_NONE_STAGED


def test_cli_describe_and_route_are_machine_readable_and_non_publishing(
    contract, capsys
):
    assert router.main(["describe"]) == 0
    described = json.loads(capsys.readouterr().out)
    assert len(described["workflows"]) == 11
    assert described["operations"] == list(router.OPERATIONS)
    assert described["publication_authority"] is False
    assert described["actor_authentication"] is False
    assert (
        router.main(
            [
                "route",
                "--workflow",
                "handoff",
                "--surface",
                "codex",
                "--task",
                "TFW-49",
                "--work",
                "phase-b",
                "--role",
                "executor",
                "--operation",
                "ordinary",
                "--summary",
                "write local result",
            ]
        )
        == 0
    )
    planned = json.loads(capsys.readouterr().out)
    assert planned["status"] == "planned"
    assert planned["publication_authority"] is False


@pytest.mark.parametrize(
    "args",
    [
        ["route", "--workflow", "unknown"],
        [
            "route",
            "--workflow",
            "handoff",
            "--surface",
            "codex",
            "--task",
            "TFW-49",
            "--work",
            "phase-b",
            "--role",
            "executor",
            "--operation",
            "revert",
            "--source-subject",
            "LEAK_api_key_sk-EXAMPLE",
            "--summary",
            "safe correction",
        ],
        [
            "route",
            "--workflow",
            "handoff",
            "--surface",
            "codex",
            "--task",
            "TFW-49",
            "--work",
            "phase-b",
            "--role",
            "executor",
            "--operation",
            "ordinary",
            "--summary",
            "safe result",
            "--content-origin",
            "LEAK_api_key_sk-EXAMPLE",
        ],
    ],
)
def test_cli_failures_never_echo_arbitrary_input(args, capsys, monkeypatch):
    sentinel = "LEAK_api_key_sk-EXAMPLE"
    monkeypatch.setenv("TFW_ROUTER_SECRET", sentinel)
    assert router.main(args) == 2
    output = capsys.readouterr()
    assert sentinel not in output.out + output.err
    assert "Traceback" not in output.err
    assert "Correct form: [codex/TFW-49/phase-a/executor] describe the result" in output.err


def test_router_uses_stdlib_and_phase_a_owner_without_git_execution(contract):
    schema, _ = contract
    source = SCRIPT.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported = {
        node.names[0].name.split(".")[0]
        for node in tree.body
        if isinstance(node, ast.Import)
    } | {
        (node.module or "").split(".")[0]
        for node in tree.body
        if isinstance(node, ast.ImportFrom) and node.module != "__future__"
    }
    assert imported <= {
        "argparse",
        "commit_identity",
        "dataclasses",
        "json",
        "pathlib",
        "re",
        "sys",
        "typing",
    }
    assert "subprocess" not in imported
    for pattern in schema["patterns"].values():
        assert pattern not in source
    assert "ordinary_pattern" not in source
    assert "origin_pattern" not in source
    assert "actor authentication" not in source.lower()
    assert "truth_boundary" in source


def test_workflow_action_cues_exist_only_on_approved_action_surfaces():
    action = {"handoff", "docs", "release"}
    for name, path in CANONICAL_WORKFLOWS.items():
        text = path.read_text(encoding="utf-8")
        if name in action:
            assert "commit_identity_router.py" in text
        else:
            assert "commit_identity_router.py" not in text
    update = CANONICAL_WORKFLOWS["update"].read_text(encoding="utf-8")
    assert "git clone --depth 1" in update
    assert "current-repository commit" not in update


def test_action_cues_separate_local_completion_from_publication():
    handoff = CANONICAL_WORKFLOWS["handoff"].read_text(encoding="utf-8")
    docs = CANONICAL_WORKFLOWS["docs"].read_text(encoding="utf-8")
    release = CANONICAL_WORKFLOWS["release"].read_text(encoding="utf-8")
    assert "Commit and push ONB" not in handoff
    assert "local" in handoff and "publication" in handoff
    assert "--workflow docs" in docs and "--work docs" in docs
    assert "--role coordinator" in docs
    assert "--workflow release" in release and "--work release" in release
    assert "--role coordinator" in release
    for text in (handoff, docs, release):
        assert "separate" in text.lower()


def _consumer_block(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    start = text.index("## Commit Identity Consumer")
    tail = text[start:]
    next_heading = tail.find("\n## ", len("## Commit Identity Consumer"))
    return tail if next_heading < 0 else tail[:next_heading]


@pytest.mark.parametrize(
    ("path", "surface"),
    [
        (ROOT / ".tfw/adapters/antigravity/tfw-rules.md.template", "antigravity"),
        (ROOT / ".tfw/adapters/claude-code/CLAUDE.md.template", "claude-code"),
        (ROOT / ".tfw/adapters/codex/AGENTS.md.template", "codex"),
        (ROOT / ".tfw/adapters/cursor/tfw.mdc.template", "cursor"),
        (ROOT / ".agent/rules/tfw.md", "antigravity"),
        (ROOT / "CLAUDE.md", "claude-code"),
        (ROOT / "AGENTS.md", "codex"),
    ],
)
def test_adapter_consumer_declares_only_its_registered_surface(
    contract, path, surface
):
    schema, _ = contract
    block = _consumer_block(path)
    assert f"`{surface}`" in block
    assert "commit_identity_router.py" in block
    for other in schema["registries"]["surfaces"]:
        if other != surface:
            assert f"`{other}`" not in block
    for forbidden in ("task=", "work=", "role="):
        assert forbidden not in block


def test_installed_workflow_copies_are_exact_for_both_surfaces():
    for name, source in CANONICAL_WORKFLOWS.items():
        agent = ROOT / ".agent" / "workflows" / f"tfw-{name}.md"
        claude = ROOT / ".claude" / "commands" / f"tfw-{name}.md"
        assert agent.read_bytes() == source.read_bytes(), name
        assert claude.read_bytes() == source.read_bytes(), name


def test_codex_skill_pairs_remain_exact_and_complete():
    canonical_root = ROOT / ".tfw" / "adapters" / "codex" / "skills"
    installed_root = ROOT / ".agents" / "skills"
    canonical = sorted(canonical_root.glob("tfw-*/SKILL.md"))
    installed = sorted(installed_root.glob("tfw-*/SKILL.md"))
    assert len(canonical) == len(installed) == 11
    by_name = {path.parent.name: path for path in installed}
    for owner in canonical:
        assert owner.read_bytes() == by_name[owner.parent.name].read_bytes()


def test_codex_managed_block_matches_template_and_preserves_one_block():
    marker_start = "<!-- TFW:CODEX:START -->"
    marker_end = "<!-- TFW:CODEX:END -->"
    template = (ROOT / ".tfw/adapters/codex/AGENTS.md.template").read_text(
        encoding="utf-8"
    )
    installed = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert installed.count(marker_start) == installed.count(marker_end) == 1
    owner_block = template[template.index(marker_start) : template.index(marker_end) + len(marker_end)]
    installed_block = installed[
        installed.index(marker_start) : installed.index(marker_end) + len(marker_end)
    ]
    assert installed_block == owner_block


def test_cursor_and_legacy_copy_boundaries_remain_unchanged():
    assert not (ROOT / ".cursor" / "rules" / "tfw.mdc").exists()
    assert (ROOT / ".agent" / "workflows" / "tfw-task.md").exists()
    assert (ROOT / ".claude" / "commands" / "tfw-task.md").exists()


def test_phase_a_owners_and_state_remain_current(contract):
    schema, state = contract
    assert state["hook_runtime"]["installed"] is False
    assert state["claims"]["actor_authentication"] is False
    assert state["activation"]["last_pre_policy_commit"] == (
        "f1106186417e84cdb38e797f7af66a60885bad76"
    )
    assert router.DEFAULT_SCHEMA_PATH == ROOT / ".tfw" / "commit_identity.schema.json"
    assert router.DEFAULT_STATE_PATH == ROOT / ".tfw" / "commit_identity_state.json"
    assert schema["grammar"]["fallback"]["accepted"] is False


def test_plan_payload_never_contains_remote_authority_or_environment_data(
    contract, monkeypatch
):
    monkeypatch.setenv("TFW_ROUTER_PRIVATE_SENTINEL", "SHOULD_NOT_APPEAR")
    payload = json.dumps(route(contract), sort_keys=True)
    assert "SHOULD_NOT_APPEAR" not in payload
    assert str(ROOT) not in payload
    assert '"publication_authority": false' in payload
    for word in ("deploy", "publish", "notify", "remote tag"):
        assert word not in payload.lower()
