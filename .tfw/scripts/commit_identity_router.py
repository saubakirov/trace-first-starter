#!/usr/bin/env python3
"""Route TFW workflow commit operations through the Phase A C1-R contract.

The Phase A JSON schema, project state, and ``commit_identity`` module remain the
semantic owners for accepted values, grammar, normalization, trailers, diagnostics,
and provenance truth. This module owns only the Phase B workflow-to-context policy
and Git-operation dispositions. It plans local operations; it does not run commits,
install hooks, change Git configuration, publish, or authenticate an actor.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import commit_identity as ci


DEFAULT_SCHEMA_PATH = ci.DEFAULT_SCHEMA_PATH
DEFAULT_STATE_PATH = ci.DEFAULT_STATE_PATH
CONTEXT_FIELDS = ci.CONTEXT_FIELDS


class RouterCodes:
    ARGUMENT = "E_ROUTER_ARGUMENT"
    OWNER = "E_ROUTER_OWNER"
    WORKFLOW = "E_ROUTER_WORKFLOW"
    ROLE = "E_ROUTER_ROLE"
    WORK = "E_ROUTER_WORK"
    TASK = "E_ROUTER_TASK"
    NON_TASK = "E_ROUTER_NON_TASK"
    STAGED_TASK = "E_ROUTER_STAGED_TASK"
    OPERATION = "E_ROUTER_OPERATION"
    SUMMARY = "E_ROUTER_SUMMARY"
    EXISTING = "E_ROUTER_EXISTING"
    TARGET = "E_ROUTER_TARGET"
    SOURCE = "E_ROUTER_SOURCE"
    AUTOSQUASH_CONTEXT = "E_ROUTER_AUTOSQUASH_CONTEXT"
    PUBLICATION = "E_ROUTER_PUBLICATION"


@dataclass(frozen=True)
class RouterError(Exception):
    code: str
    field: str
    rule: str


@dataclass(frozen=True)
class WorkflowPolicy:
    role_index: int
    task_rule: str
    work_rule: str


# These are Phase B workflow command/policy records, not accepted-value registries.
# Role and fixed-work values are resolved from the Phase A schema by position so a
# schema mutation changes or rejects router behavior instead of activating a copy.
WORKFLOW_POLICIES: Mapping[str, WorkflowPolicy] = {
    "plan": WorkflowPolicy(0, "task-required", "master-or-phase"),
    "research": WorkflowPolicy(1, "task-required", "research"),
    "handoff": WorkflowPolicy(2, "task-required", "master-or-phase"),
    "review": WorkflowPolicy(3, "task-required", "master-or-phase"),
    "resume": WorkflowPolicy(0, "task-required", "master-or-phase"),
    "docs": WorkflowPolicy(0, "task-required", "fixed"),
    "knowledge": WorkflowPolicy(0, "task-or-guarded-none", "fixed"),
    "release": WorkflowPolicy(0, "task-or-guarded-none", "fixed"),
    "update": WorkflowPolicy(0, "task-or-guarded-none", "fixed"),
    "config": WorkflowPolicy(0, "task-or-guarded-none", "fixed"),
    "init": WorkflowPolicy(0, "initialized-task", "fixed"),
}

FIXED_WORK_INDEX: Mapping[str, int] = {
    "docs": 0,
    "knowledge": 1,
    "release": 2,
    "config": 3,
    "init": 4,
    "update": 5,
}

OPERATIONS = (
    "ordinary",
    "merge",
    "amend",
    "fixup",
    "squash",
    "revert",
    "cherry-pick",
)


class SafeArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise RouterError(
            RouterCodes.ARGUMENT,
            "arguments",
            "must use a documented router command with complete explicit context",
        )


def _schema_value(values: Any, index: int, field: str) -> str:
    if not isinstance(values, list) or index < 0 or index >= len(values):
        raise RouterError(
            RouterCodes.OWNER,
            field,
            "must provide every value consumed by the approved workflow policy",
        )
    value = values[index]
    if not isinstance(value, str) or not value:
        raise RouterError(RouterCodes.OWNER, field, "must contain a usable owner value")
    return value


def _expected_role(schema: Mapping[str, Any], workflow: str) -> str:
    policy = WORKFLOW_POLICIES[workflow]
    return _schema_value(
        schema["registries"]["roles"],
        policy.role_index,
        "registries.roles",
    )


def _expected_fixed_work(schema: Mapping[str, Any], workflow: str) -> str:
    try:
        index = FIXED_WORK_INDEX[workflow]
    except KeyError:
        raise RouterError(
            RouterCodes.OWNER,
            "workflow work policy",
            "must define an approved fixed-work owner relation",
        ) from None
    return _schema_value(
        schema["registries"]["non_task_work"],
        index,
        "registries.non_task_work",
    )


def describe_workflows(schema: Mapping[str, Any]) -> list[dict[str, str]]:
    """Return the exact approved 11-workflow policy using schema-owned values."""
    records: list[dict[str, str]] = []
    for workflow, policy in WORKFLOW_POLICIES.items():
        if policy.work_rule == "fixed":
            work_rule = _expected_fixed_work(schema, workflow)
        elif policy.work_rule == "master-or-phase":
            work_rule = "schema:master-or-phase"
        elif policy.work_rule == "research":
            work_rule = "schema:research-work"
        else:
            raise RouterError(
                RouterCodes.OWNER,
                "workflow work policy",
                "must use an approved policy class",
            )
        records.append(
            {
                "workflow": workflow,
                "role": _expected_role(schema, workflow),
                "task_rule": policy.task_rule,
                "work_rule": work_rule,
            }
        )
    return records


def _staged_task_ids(schema: Mapping[str, Any], paths: Iterable[str]) -> set[str]:
    pattern = re.compile(schema["patterns"]["task_path"])
    task_ids: set[str] = set()
    for path in paths:
        normalized = path.replace("\\", "/")
        for match in pattern.finditer(normalized):
            task_ids.add(match.group("task"))
    return task_ids


def _validate_staged_task_relation(
    schema: Mapping[str, Any],
    task: str,
    staged_paths: Iterable[str] | None,
) -> None:
    if staged_paths is None or task == schema["cross_field"]["none_task"]:
        return
    staged_tasks = _staged_task_ids(schema, staged_paths)
    if staged_tasks and staged_tasks != {task}:
        raise RouterError(
            RouterCodes.STAGED_TASK,
            "staged task scopes",
            "must be empty or match exactly the current task; mixed-task work must split",
        )


def resolve_workflow_context(
    schema: Mapping[str, Any],
    *,
    workflow: str,
    surface: str,
    task: str,
    work: str,
    role: str,
    non_task: bool = False,
    staged_paths: Iterable[str] | None = None,
) -> dict[str, str]:
    """Resolve and validate one explicit workflow context."""
    if workflow not in WORKFLOW_POLICIES:
        raise RouterError(
            RouterCodes.WORKFLOW,
            "workflow",
            "must be one of the canonical workflow commands",
        )
    policy = WORKFLOW_POLICIES[workflow]
    expected_role = _expected_role(schema, workflow)
    if role != expected_role:
        raise RouterError(
            RouterCodes.ROLE,
            "role",
            "must equal the active workflow Role Lock",
        )

    canonical_work = ci.normalize_work(schema, work)
    if policy.work_rule == "fixed":
        if canonical_work != _expected_fixed_work(schema, workflow):
            raise RouterError(
                RouterCodes.WORK,
                "work",
                "must equal the workflow's schema-owned lifecycle work",
            )
    elif policy.work_rule == "master-or-phase":
        if canonical_work != schema["registries"]["master_work"] and re.fullmatch(
            schema["patterns"]["phase_work"], canonical_work
        ) is None:
            raise RouterError(
                RouterCodes.WORK,
                "work",
                "must be the schema-owned master work or a canonical phase",
            )
    elif policy.work_rule == "research":
        if re.fullmatch(schema["patterns"]["research_work"], canonical_work) is None:
            raise RouterError(
                RouterCodes.WORK,
                "work",
                "must be a canonical research iteration",
            )
    else:
        raise RouterError(
            RouterCodes.OWNER,
            "workflow work policy",
            "must use an approved policy class",
        )

    none_task = schema["cross_field"]["none_task"]
    if policy.task_rule in ("task-required", "initialized-task") and task == none_task:
        raise RouterError(
            RouterCodes.TASK,
            "task",
            "must be the explicit canonical task owned by this workflow",
        )
    if task != none_task and non_task:
        raise RouterError(
            RouterCodes.NON_TASK,
            "non-task declaration",
            "must be absent for task-scoped work",
        )
    if task == none_task and policy.task_rule != "task-or-guarded-none":
        raise RouterError(
            RouterCodes.TASK,
            "task",
            "must not use the non-task literal for this workflow",
        )

    fields = {
        "surface": surface,
        "task": task,
        "work": canonical_work,
        "role": role,
    }
    ci.validate_context(
        schema,
        fields,
        non_task=non_task,
        staged_paths=staged_paths,
    )
    _validate_staged_task_relation(schema, task, staged_paths)
    return fields


def _require_text(value: str | None, code: str, field: str, rule: str) -> str:
    if value is None or not value.strip():
        raise RouterError(code, field, rule)
    return value


def _parse_current(
    schema: Mapping[str, Any],
    subject: str,
    context: Mapping[str, str],
    *,
    non_task: bool,
    staged_paths: Iterable[str] | None,
) -> ci.ParsedSubject:
    return ci.parse_subject(
        schema,
        subject,
        expected=context,
        non_task=non_task,
        staged_paths=staged_paths,
    )


def _parse_relation(
    schema: Mapping[str, Any],
    subject: str,
    context: Mapping[str, str],
) -> ci.ParsedSubject:
    """Compare explicit identities through the public context-required parser.

    Current staged-path authority has already been validated by
    ``resolve_workflow_context``. Empty synthetic paths here let a valid guarded
    non-task source be classified against a task-scoped current context without using
    the range auditor's private structural-only path.
    """
    return ci.parse_subject(
        schema,
        subject,
        expected=context,
        non_task=True,
        staged_paths=[],
    )


def _reserved_record(schema: Mapping[str, Any], name: str) -> Mapping[str, str]:
    for record in schema["grammar"]["reserved_forms"]:
        if record["name"] == name:
            return record
    raise RouterError(
        RouterCodes.OWNER,
        "grammar.reserved_forms",
        "must provide the operation form consumed by the router",
    )


def _wrap_reserved(schema: Mapping[str, Any], name: str, subject: str) -> str:
    record = _reserved_record(schema, name)
    return f"{record['prefix']}{subject}{record['suffix']}"


def _validated_trailers(
    schema: Mapping[str, Any],
    subject: str,
    context: Mapping[str, str],
    *,
    operation: str,
    source_commit: str | None,
    content_origins: Iterable[str],
    non_task: bool,
    staged_paths: Iterable[str] | None,
) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    names = schema["trailers"]
    if source_commit is not None:
        if operation not in ("revert", "cherry-pick"):
            raise RouterError(
                RouterCodes.SOURCE,
                "source commit",
                "is available only for an explicit replay operation",
            )
        records.append({"name": names["source_commit"], "value": source_commit})
    for origin in content_origins:
        records.append({"name": names["content_origin"], "value": origin})
    if not records:
        return records
    message = subject + "\n\n" + "\n".join(
        f"{record['name']}: {record['value']}" for record in records
    )
    ci.validate_message(
        schema,
        message,
        expected=context,
        non_task=non_task,
        paths=staged_paths,
    )
    return records


def route_operation(
    schema: Mapping[str, Any],
    state: Mapping[str, Any],
    *,
    workflow: str,
    surface: str,
    task: str,
    work: str,
    role: str,
    operation: str,
    summary: str | None = None,
    existing_subject: str | None = None,
    target_subject: str | None = None,
    source_subject: str | None = None,
    source_commit: str | None = None,
    content_origins: Iterable[str] = (),
    non_task: bool = False,
    staged_paths: Iterable[str] | None = None,
) -> dict[str, Any]:
    """Return a validated, non-publishing local operation plan."""
    ci.validate_state(schema, state)
    context = resolve_workflow_context(
        schema,
        workflow=workflow,
        surface=surface,
        task=task,
        work=work,
        role=role,
        non_task=non_task,
        staged_paths=staged_paths,
    )
    if operation not in OPERATIONS:
        raise RouterError(
            RouterCodes.OPERATION,
            "operation",
            "must be an approved local Git operation intent",
        )

    disposition: str
    subject: str
    inspection_required = False
    git_option: str | None = None
    source_relation = "none"

    if operation in ("ordinary", "merge"):
        subject = ci.format_subject(
            schema,
            context,
            _require_text(
                summary,
                RouterCodes.SUMMARY,
                "summary",
                "is required for a current-context commit",
            ),
            non_task=non_task,
            staged_paths=staged_paths,
        )
        disposition = (
            "current-context-commit"
            if operation == "ordinary"
            else "current-context-merge-commit"
        )
    elif operation == "amend":
        existing = _require_text(
            existing_subject,
            RouterCodes.EXISTING,
            "existing subject",
            "is required before amend can retain or replace identity",
        )
        same_context = True
        try:
            _parse_relation(schema, existing, context)
        except ci.ContractError as error:
            if error.code != ci.Codes.CONTEXT_MISMATCH:
                raise
            same_context = False
        subject = ci.format_subject(
            schema,
            context,
            _require_text(
                summary,
                RouterCodes.SUMMARY,
                "summary",
                "is required for the amended current-context subject",
            ),
            non_task=non_task,
            staged_paths=staged_paths,
        )
        disposition = (
            "amend-same-context"
            if same_context
            else "amend-reidentify-current-context"
        )
        source_relation = "same-context" if same_context else "cross-context"
    elif operation in ("fixup", "squash"):
        target = _require_text(
            target_subject,
            RouterCodes.TARGET,
            "target subject",
            "is required for a same-context reserved operation",
        )
        try:
            parsed_target = _parse_relation(schema, target, context)
        except ci.ContractError as error:
            if error.code == ci.Codes.CONTEXT_MISMATCH:
                raise RouterError(
                    RouterCodes.AUTOSQUASH_CONTEXT,
                    "target context",
                    "must equal all four current fields; use a normal current-context follow-up",
                ) from None
            raise
        if parsed_target.form != schema["grammar"]["name"]:
            raise RouterError(
                RouterCodes.TARGET,
                "target subject",
                "must be an ordinary C1-R target rather than another reserved envelope",
            )
        subject = _wrap_reserved(schema, operation, target)
        _parse_current(
            schema,
            subject,
            context,
            non_task=non_task,
            staged_paths=staged_paths,
        )
        disposition = "same-context-reserved"
        source_relation = "same-context"
    else:
        source = _require_text(
            source_subject,
            RouterCodes.SOURCE,
            "source subject",
            "is required to decide same-context versus explicit replay",
        )
        same_context = True
        parsed_source: ci.ParsedSubject | None = None
        try:
            parsed_source = _parse_relation(schema, source, context)
        except ci.ContractError as error:
            if error.code != ci.Codes.CONTEXT_MISMATCH:
                raise
            same_context = False

        if same_context and operation == "revert" and parsed_source is not None and (
            parsed_source.form == schema["grammar"]["name"]
        ):
            subject = _wrap_reserved(schema, "revert", source)
            _parse_current(
                schema,
                subject,
                context,
                non_task=non_task,
                staged_paths=staged_paths,
            )
            disposition = "generated-replay-same-context"
            source_relation = "same-context"
        elif same_context and operation == "cherry-pick":
            subject = source
            disposition = "generated-replay-same-context"
            source_relation = "same-context"
        else:
            subject = ci.format_subject(
                schema,
                context,
                _require_text(
                    summary,
                    RouterCodes.SUMMARY,
                    "summary",
                    "is required for no-commit replay and a current-operator commit",
                ),
                non_task=non_task,
                staged_paths=staged_paths,
            )
            disposition = "no-commit-inspect-current-context"
            inspection_required = True
            git_option = "--no-commit"
            source_relation = "cross-context" if not same_context else "reserved-source"

    trailers = _validated_trailers(
        schema,
        subject,
        context,
        operation=operation,
        source_commit=source_commit,
        content_origins=content_origins,
        non_task=non_task,
        staged_paths=staged_paths,
    )
    return {
        "status": "planned",
        "workflow": workflow,
        "operation": operation,
        "context": context,
        "disposition": disposition,
        "subject": subject,
        "trailers": trailers,
        "source_relation": source_relation,
        "inspection_required": inspection_required,
        "git_option": git_option,
        "publication_authority": False,
        "hook_runtime_installed": state["hook_runtime"]["installed"],
        "actor_authentication": state["claims"]["actor_authentication"],
        "truth_boundary": schema["truth_boundary"]["claim"],
    }


def _example(schema: Mapping[str, Any] | None) -> str:
    if schema is None:
        return "[surface/task/work/role] summary"
    return schema["grammar"]["identity_template"].format(
        **schema["diagnostic_example"]
    )


def render_router_error(
    error: RouterError,
    schema: Mapping[str, Any] | None = None,
) -> str:
    return "\n".join(
        (
            f"{error.code}: {error.field} {error.rule}.",
            f"Correct form: {_example(schema)}",
            "Boundary: local declared provenance only; no publication, authentication, proof, or acceptance.",
        )
    )


def _add_contract_paths(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA_PATH)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE_PATH)


def build_parser() -> SafeArgumentParser:
    parser = SafeArgumentParser(
        description=(
            "Plan a local TFW commit operation through the Phase A C1-R contract. "
            "The router never grants publication or actor-authentication authority."
        )
    )
    commands = parser.add_subparsers(dest="command", required=True)

    describe = commands.add_parser("describe")
    _add_contract_paths(describe)

    route = commands.add_parser("route")
    _add_contract_paths(route)
    for field in ("workflow", *CONTEXT_FIELDS, "operation"):
        route.add_argument(f"--{field}", required=True)
    route.add_argument("--summary")
    route.add_argument("--existing-subject")
    route.add_argument("--target-subject")
    route.add_argument("--source-subject")
    route.add_argument("--source-commit")
    route.add_argument("--content-origin", action="append", default=[])
    route.add_argument("--non-task", action="store_true")
    route.add_argument("--repo", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    schema: Mapping[str, Any] | None = None
    try:
        # Load the default owner before argument parsing so even an incomplete CLI
        # invocation receives the schema-owned synthetic correction. Explicit
        # --schema/--state paths are loaded again after parsing.
        try:
            schema, _ = ci.load_contract()
        except ci.ContractError:
            schema = None
        args = build_parser().parse_args(argv)
        schema, state = ci.load_contract(args.schema, args.state)
        if args.command == "describe":
            print(
                json.dumps(
                    {
                        "status": "valid",
                        "contract_version": schema["contract_version"],
                        "workflows": describe_workflows(schema),
                        "operations": list(OPERATIONS),
                        "publication_authority": False,
                        "actor_authentication": state["claims"]["actor_authentication"],
                    },
                    sort_keys=True,
                )
            )
            return 0
        staged_paths = ci.staged_paths(args.repo) if args.repo is not None else None
        result = route_operation(
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
            staged_paths=staged_paths,
        )
        print(json.dumps(result, sort_keys=True))
        return 0
    except RouterError as error:
        print(render_router_error(error, schema), file=sys.stderr)
        return 2
    except ci.ContractError as error:
        print(ci.render_error(error, schema), file=sys.stderr)
        return 2
    except Exception:
        print(
            render_router_error(
                RouterError(
                    RouterCodes.ARGUMENT,
                    "operation",
                    "must satisfy the router contract safely",
                ),
                schema,
            ),
            file=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
