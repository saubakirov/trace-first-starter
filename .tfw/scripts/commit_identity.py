#!/usr/bin/env python3
"""TFW C1-R commit-identity contract.

The JSON contract owns accepted production values and patterns. This module owns
loading, algorithms, stable diagnostics, CLI commands, and the structural range
audit. It does not authenticate the operator.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from string import Formatter
from typing import Any, Iterable, Mapping, Sequence


DEFAULT_SCHEMA_PATH = Path(__file__).resolve().parents[1] / "commit_identity.schema.json"
DEFAULT_STATE_PATH = Path(__file__).resolve().parents[1] / "commit_identity_state.json"
CONTEXT_FIELDS = ("surface", "task", "work", "role")


class Codes:
    ARGUMENT = "E_ARGUMENT"
    SCHEMA_JSON = "E_SCHEMA_JSON"
    SCHEMA_SHAPE = "E_SCHEMA_SHAPE"
    STATE_JSON = "E_STATE_JSON"
    STATE_SHAPE = "E_STATE_SHAPE"
    VERSION_MISMATCH = "E_VERSION_MISMATCH"
    SURFACE = "E_SURFACE"
    TASK = "E_TASK"
    WORK = "E_WORK"
    ROLE = "E_ROLE"
    SUMMARY = "E_SUMMARY"
    SUBJECT_FORMAT = "E_SUBJECT_FORMAT"
    EXPECTED_CONTEXT = "E_EXPECTED_CONTEXT"
    CONTEXT_MISMATCH = "E_CONTEXT_MISMATCH"
    TASK_NONE_DECLARATION = "E_TASK_NONE_DECLARATION"
    TASK_NONE_WORK = "E_TASK_NONE_WORK"
    TASK_NONE_PATHS = "E_TASK_NONE_PATHS"
    TASK_NONE_STAGED = "E_TASK_NONE_STAGED"
    TRAILER_PARSE = "E_TRAILER_PARSE"
    TRAILER_NAME = "E_TRAILER_NAME"
    TRAILER_VALUE = "E_TRAILER_VALUE"
    ORIGIN = "E_ORIGIN"
    RANGE_REPOSITORY = "E_RANGE_REPOSITORY"
    RANGE_SHALLOW = "E_RANGE_SHALLOW"
    RANGE_ANCHOR = "E_RANGE_ANCHOR"
    RANGE_TARGET = "E_RANGE_TARGET"
    RANGE_ANCESTRY = "E_RANGE_ANCESTRY"
    RANGE_ENUMERATION = "E_RANGE_ENUMERATION"
    RANGE_VIOLATION = "E_RANGE_VIOLATION"


@dataclass(frozen=True)
class ContractError(Exception):
    code: str
    field: str
    rule: str
    violations: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class ParsedSubject:
    form: str
    fields: Mapping[str, str]
    summary: str


class SafeArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise ContractError(Codes.ARGUMENT, "arguments", "use a documented command form")


def _load_json(path: Path, code: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        raise ContractError(code, "contract data", "must be available as valid UTF-8 JSON")
    if not isinstance(value, dict):
        raise ContractError(code, "contract data", "must be a JSON object")
    return value


def _mapping(value: Any, code: str, field: str) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        raise ContractError(code, field, "must be an object")
    return value


def _strings(value: Any, code: str, field: str) -> list[str]:
    if not isinstance(value, list) or not value or any(not isinstance(v, str) or not v for v in value):
        raise ContractError(code, field, "must be a non-empty string list")
    if len(set(value)) != len(value):
        raise ContractError(code, field, "must contain unique values")
    return value


def _compile(pattern: Any, code: str, field: str) -> re.Pattern[str]:
    if not isinstance(pattern, str):
        raise ContractError(code, field, "must be a regular-expression string")
    try:
        return re.compile(pattern)
    except re.error:
        raise ContractError(code, field, "must compile as a regular expression")


def _string(value: Any, code: str, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ContractError(code, field, "must be a non-empty string")
    return value


def _optional_strings(value: Any, code: str, field: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
        raise ContractError(code, field, "must be a string list")
    if len(set(value)) != len(value):
        raise ContractError(code, field, "must contain unique values")
    return value


def _template_fields(value: Any, expected: Iterable[str], field: str) -> str:
    template = _string(value, Codes.SCHEMA_SHAPE, field)
    fields: list[str] = []
    try:
        parts = Formatter().parse(template)
        for _, name, format_spec, conversion in parts:
            if name is None:
                continue
            if (
                not name
                or format_spec
                or conversion is not None
                or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name)
            ):
                raise ValueError
            fields.append(name)
    except (ValueError, KeyError):
        raise ContractError(
            Codes.SCHEMA_SHAPE, field, "must use simple compatible named placeholders"
        )
    required = tuple(expected)
    if len(fields) != len(required) or set(fields) != set(required):
        raise ContractError(
            Codes.SCHEMA_SHAPE, field, "must contain every required placeholder exactly once"
        )
    return template


def _required_named_groups(pattern: re.Pattern[str], expected: Iterable[str], field: str) -> None:
    if set(pattern.groupindex) != set(expected):
        raise ContractError(
            Codes.SCHEMA_SHAPE, field, "must define exactly the required named capture groups"
        )


def validate_schema(schema: Mapping[str, Any]) -> None:
    if schema.get("schema_kind") != "tfw.commit-identity-contract":
        raise ContractError(Codes.SCHEMA_SHAPE, "schema_kind", "must identify the TFW contract")
    patterns = _mapping(schema.get("patterns"), Codes.SCHEMA_SHAPE, "patterns")
    version = schema.get("contract_version")
    if not isinstance(version, str) or not _compile(
        patterns.get("contract_version"), Codes.SCHEMA_SHAPE, "patterns.contract_version"
    ).fullmatch(version):
        raise ContractError(Codes.SCHEMA_SHAPE, "contract_version", "must satisfy its owned pattern")
    grammar = _mapping(schema.get("grammar"), Codes.SCHEMA_SHAPE, "grammar")
    _string(grammar.get("name"), Codes.SCHEMA_SHAPE, "grammar.name")
    if grammar.get("field_order") != list(CONTEXT_FIELDS):
        raise ContractError(Codes.SCHEMA_SHAPE, "grammar.field_order", "must contain the four loader fields")
    identity_template = _template_fields(
        grammar.get("identity_template"), (*CONTEXT_FIELDS, "summary"), "grammar.identity_template"
    )
    ordinary_pattern = _compile(
        grammar.get("ordinary_pattern"), Codes.SCHEMA_SHAPE, "grammar.ordinary_pattern"
    )
    origin_pattern = _compile(
        grammar.get("origin_pattern"), Codes.SCHEMA_SHAPE, "grammar.origin_pattern"
    )
    _required_named_groups(
        ordinary_pattern, (*CONTEXT_FIELDS, "summary"), "grammar.ordinary_pattern"
    )
    _required_named_groups(origin_pattern, CONTEXT_FIELDS, "grammar.origin_pattern")
    forms = grammar.get("reserved_forms")
    if not isinstance(forms, list) or not forms:
        raise ContractError(Codes.SCHEMA_SHAPE, "grammar.reserved_forms", "must be a non-empty list")
    names: list[str] = []
    wrappers: list[tuple[str, str]] = []
    for index, form in enumerate(forms):
        owner = f"grammar.reserved_forms[{index}]"
        record = _mapping(form, Codes.SCHEMA_SHAPE, owner)
        name = _string(record.get("name"), Codes.SCHEMA_SHAPE, f"{owner}.name")
        prefix = record.get("prefix")
        suffix = record.get("suffix")
        if not isinstance(prefix, str) or not isinstance(suffix, str) or not (prefix or suffix):
            raise ContractError(
                Codes.SCHEMA_SHAPE, owner, "must define a non-empty prefix or suffix envelope"
            )
        names.append(name)
        wrappers.append((prefix, suffix))
    if len(set(names)) != len(names):
        raise ContractError(Codes.SCHEMA_SHAPE, "grammar.reserved_forms.name", "must use unique names")
    if len(set(wrappers)) != len(wrappers):
        raise ContractError(
            Codes.SCHEMA_SHAPE, "grammar.reserved_forms", "must use unique prefix/suffix envelopes"
        )
    fallback = _mapping(grammar.get("fallback"), Codes.SCHEMA_SHAPE, "grammar.fallback")
    _string(fallback.get("name"), Codes.SCHEMA_SHAPE, "grammar.fallback.name")
    if fallback.get("accepted") is not False:
        raise ContractError(
            Codes.SCHEMA_SHAPE, "grammar.fallback.accepted", "must remain documentation-only"
        )
    _template_fields(
        fallback.get("template"), (*CONTEXT_FIELDS, "summary"), "grammar.fallback.template"
    )
    registries = _mapping(schema.get("registries"), Codes.SCHEMA_SHAPE, "registries")
    for key in (
        "surfaces",
        "roles",
        "non_task_work",
        "repository_policies",
        "activation_statuses",
        "range_semantics",
        "pre_anchor_history",
    ):
        _strings(registries.get(key), Codes.SCHEMA_SHAPE, f"registries.{key}")
    if not isinstance(registries.get("master_work"), str) or not registries["master_work"]:
        raise ContractError(Codes.SCHEMA_SHAPE, "registries.master_work", "must be a string")
    for key in (
        "task",
        "phase_work",
        "research_work",
        "object_id",
        "safe_metadata",
        "credential_like",
        "task_path",
    ):
        _compile(patterns.get(key), Codes.SCHEMA_SHAPE, f"patterns.{key}")
    rules = _mapping(schema.get("normalization"), Codes.SCHEMA_SHAPE, "normalization").get(
        "work_rules"
    )
    if not isinstance(rules, list) or not rules:
        raise ContractError(Codes.SCHEMA_SHAPE, "normalization.work_rules", "must be a non-empty list")
    rule_names: list[str] = []
    for index, rule in enumerate(rules):
        owner = f"normalization.work_rules[{index}]"
        record = _mapping(rule, Codes.SCHEMA_SHAPE, owner)
        rule_names.append(_string(record.get("name"), Codes.SCHEMA_SHAPE, f"{owner}.name"))
        rule_pattern = _compile(
            record.get("pattern"), Codes.SCHEMA_SHAPE, f"{owner}.pattern"
        )
        group_names = tuple(rule_pattern.groupindex)
        if not group_names:
            raise ContractError(
                Codes.SCHEMA_SHAPE, f"{owner}.pattern", "must define named transform groups"
            )
        _template_fields(record.get("template"), group_names, f"{owner}.template")
        lowercase = _optional_strings(
            record.get("lowercase_groups"), Codes.SCHEMA_SHAPE, f"{owner}.lowercase_groups"
        )
        if not set(lowercase) <= set(group_names):
            raise ContractError(
                Codes.SCHEMA_SHAPE,
                f"{owner}.lowercase_groups",
                "must reference only named pattern groups",
            )
    if len(set(rule_names)) != len(rule_names):
        raise ContractError(
            Codes.SCHEMA_SHAPE, "normalization.work_rules.name", "must use unique names"
        )
    trailers = _mapping(schema.get("trailers"), Codes.SCHEMA_SHAPE, "trailers")
    for key in ("content_origin", "agent_model", "agent_session", "source_commit", "co_author"):
        _string(trailers.get(key), Codes.SCHEMA_SHAPE, f"trailers.{key}")
    if len(set(trailers.values())) != len(trailers):
        raise ContractError(Codes.SCHEMA_SHAPE, "trailers", "must use unique names")
    example = _mapping(schema.get("diagnostic_example"), Codes.SCHEMA_SHAPE, "diagnostic_example")
    for key in (*CONTEXT_FIELDS, "summary"):
        _string(
            example.get(key), Codes.SCHEMA_SHAPE, f"diagnostic_example.{key}"
        )
    cross = _mapping(schema.get("cross_field"), Codes.SCHEMA_SHAPE, "cross_field")
    if not isinstance(cross.get("none_task"), str) or not cross["none_task"]:
        raise ContractError(Codes.SCHEMA_SHAPE, "cross_field.none_task", "must be a string")
    try:
        validate_context(schema, example, structural=True)
    except ContractError as error:
        raise ContractError(
            Codes.SCHEMA_SHAPE,
            f"diagnostic_example.{error.field}",
            "must satisfy the owned registry and pattern contract",
        ) from None
    if any(ord(char) < 32 or ord(char) == 127 for char in example["summary"]):
        raise ContractError(Codes.SCHEMA_SHAPE, "diagnostic_example.summary", "must be control-free")
    try:
        rendered_identity = identity_template.format(**example)
    except (KeyError, ValueError):
        raise ContractError(
            Codes.SCHEMA_SHAPE,
            "grammar.identity_template",
            "must format the complete diagnostic example",
        ) from None
    identity_match = ordinary_pattern.fullmatch(rendered_identity)
    if identity_match is None or any(
        identity_match.group(field) != example[field] for field in (*CONTEXT_FIELDS, "summary")
    ):
        raise ContractError(
            Codes.SCHEMA_SHAPE,
            "grammar.identity_template",
            "must be compatible with grammar.ordinary_pattern",
        )
    rendered_origin = "/".join(example[field] for field in CONTEXT_FIELDS)
    origin_match = origin_pattern.fullmatch(rendered_origin)
    if origin_match is None or any(
        origin_match.group(field) != example[field] for field in CONTEXT_FIELDS
    ):
        raise ContractError(
            Codes.SCHEMA_SHAPE,
            "grammar.origin_pattern",
            "must accept the complete diagnostic context",
        )
    truth = _mapping(schema.get("truth_boundary"), Codes.SCHEMA_SHAPE, "truth_boundary")
    _string(truth.get("claim"), Codes.SCHEMA_SHAPE, "truth_boundary.claim")
    non_claims = _strings(
        truth.get("non_claims"), Codes.SCHEMA_SHAPE, "truth_boundary.non_claims"
    )
    bypasses = _strings(
        truth.get("known_bypasses"), Codes.SCHEMA_SHAPE, "truth_boundary.known_bypasses"
    )
    if set(non_claims) & set(bypasses):
        raise ContractError(
            Codes.SCHEMA_SHAPE,
            "truth_boundary",
            "must keep non-claims and known bypasses distinct",
        )


def validate_state(schema: Mapping[str, Any], state: Mapping[str, Any]) -> None:
    if state.get("state_kind") != "tfw.commit-identity-state":
        raise ContractError(Codes.STATE_SHAPE, "state_kind", "must identify TFW project state")
    if any(key in state for key in ("grammar", "patterns", "registries")):
        raise ContractError(Codes.STATE_SHAPE, "state", "must not copy universal contract data")
    if state.get("contract_version") != schema.get("contract_version"):
        raise ContractError(Codes.VERSION_MISMATCH, "contract_version", "must match the schema")
    registries = schema["registries"]
    if state.get("repository_policy") not in registries["repository_policies"]:
        raise ContractError(Codes.STATE_SHAPE, "repository_policy", "must be registered")
    activation = _mapping(state.get("activation"), Codes.STATE_SHAPE, "activation")
    if activation.get("status") not in registries["activation_statuses"]:
        raise ContractError(Codes.STATE_SHAPE, "activation.status", "must be registered")
    if activation.get("range_semantics") not in registries["range_semantics"]:
        raise ContractError(Codes.STATE_SHAPE, "activation.range_semantics", "must be registered")
    if activation.get("pre_anchor_history") not in registries["pre_anchor_history"]:
        raise ContractError(Codes.STATE_SHAPE, "activation.pre_anchor_history", "must be registered")
    anchor = activation.get("last_pre_policy_commit")
    if not isinstance(anchor, str) or not re.fullmatch(schema["patterns"]["object_id"], anchor):
        raise ContractError(Codes.STATE_SHAPE, "activation.last_pre_policy_commit", "must be a full object id")
    hooks = _mapping(state.get("hook_runtime"), Codes.STATE_SHAPE, "hook_runtime")
    if hooks.get("installed") is not False:
        raise ContractError(Codes.STATE_SHAPE, "hook_runtime.installed", "must remain false in Phase A")
    claims = _mapping(state.get("claims"), Codes.STATE_SHAPE, "claims")
    if claims.get("actor_authentication") is not False:
        raise ContractError(Codes.STATE_SHAPE, "claims.actor_authentication", "must remain false")


def load_contract(
    schema_path: Path = DEFAULT_SCHEMA_PATH,
    state_path: Path = DEFAULT_STATE_PATH,
) -> tuple[dict[str, Any], dict[str, Any]]:
    schema = _load_json(schema_path, Codes.SCHEMA_JSON)
    validate_schema(schema)
    state = _load_json(state_path, Codes.STATE_JSON)
    validate_state(schema, state)
    return schema, state


def normalize_work(schema: Mapping[str, Any], work: str) -> str:
    for rule in schema["normalization"]["work_rules"]:
        match = re.fullmatch(rule["pattern"], work)
        if not match:
            continue
        values = match.groupdict()
        for key in rule["lowercase_groups"]:
            if key in values:
                values[key] = values[key].lower()
        return rule["template"].format(**values)
    return work


def _work_valid(schema: Mapping[str, Any], work: str) -> bool:
    registries = schema["registries"]
    return (
        work == registries["master_work"]
        or work in registries["non_task_work"]
        or re.fullmatch(schema["patterns"]["phase_work"], work) is not None
        or re.fullmatch(schema["patterns"]["research_work"], work) is not None
    )


def _task_paths(schema: Mapping[str, Any], paths: Iterable[str]) -> bool:
    pattern = re.compile(schema["patterns"]["task_path"])
    return any(pattern.search(path.replace("\\", "/")) for path in paths)


def validate_context(
    schema: Mapping[str, Any],
    fields: Mapping[str, str],
    *,
    non_task: bool = False,
    staged_paths: Iterable[str] | None = None,
    structural: bool = False,
) -> None:
    if fields.get("surface") not in schema["registries"]["surfaces"]:
        raise ContractError(Codes.SURFACE, "surface", "must be registered")
    if fields.get("role") not in schema["registries"]["roles"]:
        raise ContractError(Codes.ROLE, "role", "must be registered")
    task = fields.get("task", "")
    work = fields.get("work", "")
    none_task = schema["cross_field"]["none_task"]
    if task != none_task and re.fullmatch(schema["patterns"]["task"], task) is None:
        raise ContractError(Codes.TASK, "task", "must be canonical or the guarded non-task literal")
    if not _work_valid(schema, work):
        raise ContractError(Codes.WORK, "work", "must be canonical")
    if task == none_task:
        if work not in schema["registries"]["non_task_work"]:
            raise ContractError(Codes.TASK_NONE_WORK, "work", "must be a non-task lifecycle scope")
        if not structural:
            if not non_task:
                raise ContractError(
                    Codes.TASK_NONE_DECLARATION, "task", "requires an explicit non-task declaration"
                )
            if staged_paths is None:
                raise ContractError(
                    Codes.TASK_NONE_PATHS, "staged paths", "must be checked for task-scoped names"
                )
            if _task_paths(schema, staged_paths):
                raise ContractError(
                    Codes.TASK_NONE_STAGED, "staged paths", "must not contain a canonical task scope"
                )


def _parse_subject(
    schema: Mapping[str, Any],
    subject: str,
    *,
    expected: Mapping[str, str] | None = None,
    non_task: bool = False,
    staged_paths: Iterable[str] | None = None,
    structural_only: bool = False,
) -> ParsedSubject:
    candidate = subject
    form = schema["grammar"]["name"]
    for reserved in schema["grammar"]["reserved_forms"]:
        prefix, suffix = reserved["prefix"], reserved["suffix"]
        if candidate.startswith(prefix) and (not suffix or candidate.endswith(suffix)):
            candidate = candidate[len(prefix) : len(candidate) - len(suffix) if suffix else None]
            form = reserved["name"]
            break
    match = re.fullmatch(schema["grammar"]["ordinary_pattern"], candidate)
    if match is None:
        raise ContractError(Codes.SUBJECT_FORMAT, "subject", "must use the accepted C1-R form")
    fields = {name: match.group(name) for name in schema["grammar"]["field_order"]}
    summary = match.group("summary")
    validate_context(
        schema,
        fields,
        non_task=non_task,
        staged_paths=staged_paths,
        structural=structural_only,
    )
    if not summary.strip() or any(ord(char) < 32 or ord(char) == 127 for char in summary):
        raise ContractError(Codes.SUMMARY, "summary", "must be non-empty and control-free")
    if form != schema["grammar"]["name"] and expected is None and not structural_only:
        raise ContractError(
            Codes.EXPECTED_CONTEXT,
            "expected context",
            "is required for a reserved subject form",
        )
    if expected is not None:
        validate_context(
            schema,
            expected,
            non_task=non_task,
            staged_paths=staged_paths,
            structural=structural_only,
        )
        if any(fields[name] != expected[name] for name in schema["grammar"]["field_order"]):
            raise ContractError(
                Codes.CONTEXT_MISMATCH, "expected context", "must equal all four subject fields"
            )
    return ParsedSubject(form=form, fields=fields, summary=summary)


def parse_subject(
    schema: Mapping[str, Any],
    subject: str,
    *,
    expected: Mapping[str, str] | None = None,
    non_task: bool = False,
    staged_paths: Iterable[str] | None = None,
) -> ParsedSubject:
    return _parse_subject(
        schema,
        subject,
        expected=expected,
        non_task=non_task,
        staged_paths=staged_paths,
    )


def _parse_subject_structural(schema: Mapping[str, Any], subject: str) -> ParsedSubject:
    """Parse identity structure for the independent range audit only."""
    return _parse_subject(schema, subject, structural_only=True)


def format_subject(
    schema: Mapping[str, Any],
    fields: Mapping[str, str],
    summary: str,
    *,
    non_task: bool = False,
    staged_paths: Iterable[str] | None = None,
) -> str:
    canonical = dict(fields)
    canonical["work"] = normalize_work(schema, canonical.get("work", ""))
    validate_context(schema, canonical, non_task=non_task, staged_paths=staged_paths)
    clean_summary = summary.strip()
    if not clean_summary or any(ord(char) < 32 or ord(char) == 127 for char in clean_summary):
        raise ContractError(Codes.SUMMARY, "summary", "must be non-empty and control-free")
    subject = schema["grammar"]["identity_template"].format(**canonical, summary=clean_summary)
    parse_subject(
        schema,
        subject,
        expected=canonical,
        non_task=non_task,
        staged_paths=staged_paths,
    )
    return subject


def _git(args: Sequence[str], *, cwd: Path | None = None, input_text: str | None = None) -> str:
    try:
        result = subprocess.run(
            ["git", *(["-C", str(cwd)] if cwd is not None else []), *args],
            input=input_text,
            text=True,
            encoding="utf-8",
            errors="surrogateescape",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError:
        raise ContractError(Codes.RANGE_REPOSITORY, "Git", "must be available")
    if result.returncode != 0:
        raise ContractError(Codes.RANGE_REPOSITORY, "Git operation", "must complete successfully")
    return result.stdout


def staged_paths(repo: Path) -> list[str]:
    output = _git(["diff", "--cached", "--name-only", "-z"], cwd=repo)
    return [item for item in output.split("\0") if item]


def _trailers(message: str) -> list[tuple[str, str]]:
    try:
        output = _git(["interpret-trailers", "--parse"], input_text=message)
    except ContractError:
        raise ContractError(Codes.TRAILER_PARSE, "trailers", "must be parseable by Git")
    records: list[tuple[str, str]] = []
    for line in output.splitlines():
        if ":" not in line:
            raise ContractError(Codes.TRAILER_PARSE, "trailers", "must use Git trailer syntax")
        name, value = line.split(":", 1)
        records.append((name.strip(), value.strip()))
    return records


def validate_trailers(schema: Mapping[str, Any], message: str) -> None:
    names = schema["trailers"]
    allowed = set(names.values())
    metadata = {names["agent_model"], names["agent_session"]}
    for name, value in _trailers(message):
        if name.startswith("TFW-") and name not in allowed:
            raise ContractError(Codes.TRAILER_NAME, "trailer", "must use a registered TFW name")
        if name == names["content_origin"]:
            match = re.fullmatch(schema["grammar"]["origin_pattern"], value)
            if match is None:
                raise ContractError(Codes.ORIGIN, "content origin", "must contain all four fields")
            fields = {field: match.group(field) for field in schema["grammar"]["field_order"]}
            validate_context(schema, fields, structural=True)
        elif name in metadata:
            if re.fullmatch(schema["patterns"]["safe_metadata"], value) is None or re.search(
                schema["patterns"]["credential_like"], value
            ):
                raise ContractError(Codes.TRAILER_VALUE, "optional metadata", "must be safe declared data")
        elif name == names["source_commit"]:
            if re.fullmatch(schema["patterns"]["object_id"], value) is None:
                raise ContractError(Codes.TRAILER_VALUE, "source commit", "must be a full object id")


def validate_message(
    schema: Mapping[str, Any],
    message: str,
    *,
    expected: Mapping[str, str] | None = None,
    non_task: bool = False,
    paths: Iterable[str] | None = None,
) -> ParsedSubject:
    subject = message.splitlines()[0] if message.splitlines() else ""
    parsed = parse_subject(
        schema,
        subject,
        expected=expected,
        non_task=non_task,
        staged_paths=paths,
    )
    validate_trailers(schema, message)
    return parsed


def _resolve_commit(repo: Path, revision: str, code: str, field: str) -> str:
    try:
        return _git(
            ["rev-parse", "--verify", "--end-of-options", f"{revision}^{{commit}}"], cwd=repo
        ).strip()
    except ContractError:
        raise ContractError(code, field, "must resolve to a commit")


def audit_range(
    schema: Mapping[str, Any],
    state: Mapping[str, Any],
    repo: Path,
    target: str = "HEAD",
) -> dict[str, Any]:
    validate_state(schema, state)
    try:
        if _git(["rev-parse", "--is-inside-work-tree"], cwd=repo).strip() != "true":
            raise ContractError(Codes.RANGE_REPOSITORY, "repository", "must be a Git work tree")
        if _git(["rev-parse", "--is-shallow-repository"], cwd=repo).strip() == "true":
            raise ContractError(Codes.RANGE_SHALLOW, "repository", "must contain complete history")
    except ContractError as error:
        if error.code == Codes.RANGE_SHALLOW:
            raise
        raise ContractError(Codes.RANGE_REPOSITORY, "repository", "must be a complete Git work tree")
    anchor_value = state["activation"]["last_pre_policy_commit"]
    anchor = _resolve_commit(repo, anchor_value, Codes.RANGE_ANCHOR, "activation anchor")
    target_id = _resolve_commit(repo, target, Codes.RANGE_TARGET, "target")
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), "merge-base", "--is-ancestor", anchor, target_id],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except OSError:
        raise ContractError(Codes.RANGE_REPOSITORY, "Git", "must be available")
    if result.returncode != 0:
        raise ContractError(Codes.RANGE_ANCESTRY, "activation anchor", "must be an ancestor")
    try:
        commits = [
            item
            for item in _git(["rev-list", "--reverse", f"{anchor}..{target_id}"], cwd=repo).splitlines()
            if item
        ]
    except ContractError:
        raise ContractError(Codes.RANGE_ENUMERATION, "range", "must enumerate exactly")
    violations: list[tuple[str, str]] = []
    for commit in commits:
        try:
            subject = _git(["show", "-s", "--format=%s", commit], cwd=repo).rstrip("\r\n")
            _parse_subject_structural(schema, subject)
        except ContractError as error:
            violations.append((commit, error.code))
    if violations:
        raise ContractError(
            Codes.RANGE_VIOLATION,
            "range",
            "every descendant must carry structurally valid C1-R identity",
            tuple(violations),
        )
    return {
        "status": "valid",
        "contract_version": schema["contract_version"],
        "policy": state["repository_policy"],
        "range_semantics": state["activation"]["range_semantics"],
        "anchor": anchor,
        "target": target_id,
        "commit_count": len(commits),
        "commits": commits,
        "actor_authentication": state["claims"]["actor_authentication"],
    }


def _example(schema: Mapping[str, Any] | None) -> str:
    if not schema:
        return "[surface/task/work/role] summary"
    example = schema["diagnostic_example"]
    return schema["grammar"]["identity_template"].format(**example)


def render_error(error: ContractError, schema: Mapping[str, Any] | None = None) -> str:
    lines = [
        f"{error.code}: {error.field} {error.rule}.",
        f"Correct form: {_example(schema)}",
        "Boundary: declared structural provenance; not actor authentication or acceptance.",
    ]
    lines.extend(f"Violation: {commit} {code}" for commit, code in error.violations)
    return "\n".join(lines)


def _context(args: argparse.Namespace, *, expected: bool = False) -> Mapping[str, str] | None:
    prefix = "expected_" if expected else ""
    values = {field: getattr(args, f"{prefix}{field}", None) for field in CONTEXT_FIELDS}
    present = [value is not None for value in values.values()]
    if expected and not any(present):
        return None
    if not all(present):
        raise ContractError(
            Codes.EXPECTED_CONTEXT, "expected context" if expected else "context", "requires all four fields"
        )
    return {key: str(value) for key, value in values.items()}


def _add_context(parser: argparse.ArgumentParser, *, expected: bool = False) -> None:
    prefix = "expected-" if expected else ""
    dest_prefix = "expected_" if expected else ""
    for field in CONTEXT_FIELDS:
        parser.add_argument(f"--{prefix}{field}", dest=f"{dest_prefix}{field}", required=not expected)


def _add_contract_paths(parser: argparse.ArgumentParser, *, state: bool = True) -> None:
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA_PATH)
    if state:
        parser.add_argument("--state", type=Path, default=DEFAULT_STATE_PATH)


def build_parser() -> SafeArgumentParser:
    parser = SafeArgumentParser(
        description=(
            "Validate TFW C1-R declared commit context. "
            "Structural validity is not actor authentication, Git authorship, proof, or acceptance."
        )
    )
    commands = parser.add_subparsers(dest="command", required=True)
    format_cmd = commands.add_parser("format")
    _add_contract_paths(format_cmd)
    _add_context(format_cmd)
    format_cmd.add_argument("--summary", required=True)
    format_cmd.add_argument("--non-task", action="store_true")
    format_cmd.add_argument("--repo", type=Path)

    subject_cmd = commands.add_parser("validate-subject")
    _add_contract_paths(subject_cmd)
    subject_cmd.add_argument("--subject", required=True)
    _add_context(subject_cmd, expected=True)
    subject_cmd.add_argument("--non-task", action="store_true")
    subject_cmd.add_argument("--repo", type=Path)

    message_cmd = commands.add_parser("validate-message")
    _add_contract_paths(message_cmd)
    message_cmd.add_argument("--message-file", type=Path, required=True)
    _add_context(message_cmd, expected=True)
    message_cmd.add_argument("--non-task", action="store_true")
    message_cmd.add_argument("--repo", type=Path)

    state_cmd = commands.add_parser("validate-state")
    _add_contract_paths(state_cmd)

    describe_cmd = commands.add_parser("describe")
    _add_contract_paths(describe_cmd)

    audit_cmd = commands.add_parser("audit-range")
    _add_contract_paths(audit_cmd)
    audit_cmd.add_argument("--repo", type=Path, default=Path.cwd())
    audit_cmd.add_argument("--target", default="HEAD")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    schema: Mapping[str, Any] | None = None
    try:
        args = build_parser().parse_args(argv)
        schema, state = load_contract(args.schema, args.state)
        if args.command == "validate-state":
            print(json.dumps({"status": "valid", "contract_version": schema["contract_version"]}))
            return 0
        if args.command == "describe":
            print(
                json.dumps(
                    {
                        "contract_version": schema["contract_version"],
                        "grammar": schema["grammar"]["name"],
                        "example": _example(schema),
                        "truth_boundary": schema["truth_boundary"],
                    },
                    sort_keys=True,
                )
            )
            return 0
        if args.command == "audit-range":
            print(json.dumps(audit_range(schema, state, args.repo, args.target), sort_keys=True))
            return 0
        repo_paths = staged_paths(args.repo) if args.repo is not None else None
        expected = _context(args, expected=True) if args.command != "format" else None
        if args.command == "format":
            print(
                format_subject(
                    schema,
                    _context(args) or {},
                    args.summary,
                    non_task=args.non_task,
                    staged_paths=repo_paths,
                )
            )
        elif args.command == "validate-subject":
            parsed = parse_subject(
                schema,
                args.subject,
                expected=expected,
                non_task=args.non_task,
                staged_paths=repo_paths,
            )
            print(json.dumps({"status": "valid", "form": parsed.form}, sort_keys=True))
        elif args.command == "validate-message":
            try:
                message = args.message_file.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                raise ContractError(Codes.ARGUMENT, "message file", "must be readable UTF-8")
            parsed = validate_message(
                schema,
                message,
                expected=expected,
                non_task=args.non_task,
                paths=repo_paths,
            )
            print(json.dumps({"status": "valid", "form": parsed.form}, sort_keys=True))
        return 0
    except ContractError as error:
        print(render_error(error, schema), file=sys.stderr)
        return 2
    except Exception:
        print(
            render_error(
                ContractError(Codes.ARGUMENT, "operation", "must satisfy the contract safely"),
                schema,
            ),
            file=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
