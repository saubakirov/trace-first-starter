from __future__ import annotations

import ast
import copy
import importlib.util
import itertools
import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = Path(__file__).with_name("commit_identity.py")
SCHEMA = ROOT / ".tfw" / "commit_identity.schema.json"
STATE = ROOT / ".tfw" / "commit_identity_state.json"
STATE_TEMPLATE = ROOT / ".tfw" / "templates" / "commit_identity_state.json"
SPEC = importlib.util.spec_from_file_location("commit_identity", SCRIPT)
assert SPEC and SPEC.loader
ci = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ci
SPEC.loader.exec_module(ci)


@pytest.fixture
def contract():
    return ci.load_contract()


def git(repo: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        [
            "git",
            "-c",
            "core.hooksPath=.tfw/hooks",
            "-c",
            "user.name=TFW Fixture",
            "-c",
            "user.email=fixture@example.invalid",
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


def init_repo(tmp_path: Path, name: str = "repo") -> Path:
    repo = tmp_path / name
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    return repo


def commit(repo: Path, subject: str, name: str) -> str:
    (repo / name).write_text(name, encoding="utf-8")
    git(repo, "add", "--", name)
    git(repo, "commit", "-q", "-m", subject)
    return git(repo, "rev-parse", "HEAD")


def project_state(state, anchor: str):
    value = copy.deepcopy(state)
    value["activation"]["last_pre_policy_commit"] = anchor
    return value


def root_state(state):
    value = copy.deepcopy(state)
    value["activation"] = {
        "status": state["activation"]["status"],
        "last_pre_policy_commit": None,
        "range_semantics": "root-inclusive",
        "pre_anchor_history": "not-applicable",
    }
    return value


def test_schema_and_state_are_separate_operational_owners(contract):
    schema, state = contract
    assert schema["grammar"]["field_order"] == ["surface", "task", "work", "role"]
    assert schema["registries"]["surfaces"] == ["antigravity", "claude-code", "codex", "cursor"]
    assert schema["registries"]["roles"] == ["coordinator", "researcher", "executor", "reviewer"]
    assert schema["grammar"]["fallback"]["accepted"] is False
    assert state["contract_version"] == schema["contract_version"]
    assert state["repository_policy"] == "agent-managed"
    assert state["activation"]["last_pre_policy_commit"] == "f1106186417e84cdb38e797f7af66a60885bad76"
    assert not ({"grammar", "patterns", "registries"} & state.keys())
    assert "installed" not in state["hook_runtime"]
    assert state["hook_runtime"] == {
        "required_version": schema["runtime"]["required_version"],
        "source": schema["runtime"]["source"],
    }
    assert state["claims"]["actor_authentication"] is False
    assert schema["contract_version"] == "1.1.0"


def test_python_uses_stdlib_and_does_not_copy_production_values(contract):
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
        "argparse", "dataclasses", "json", "pathlib", "re", "string", "subprocess", "sys", "typing"
    }
    values = []
    for value in schema["registries"].values():
        values.extend(value if isinstance(value, list) else [value])
    for value in values:
        assert f'"{value}"' not in source and f"'{value}'" not in source
    for pattern in schema["patterns"].values():
        assert pattern not in source


def test_fixture_schema_mutation_changes_behavior_only_through_data(contract):
    schema, _ = contract
    fixture = copy.deepcopy(schema)
    fixture["registries"]["surfaces"].append("fixture-surface")
    ci.validate_schema(fixture)
    fields = {"surface": "fixture-surface", "task": "TFW-49", "work": "phase-a", "role": "executor"}
    assert ci.format_subject(fixture, fields, "fixture result").startswith("[fixture-surface/")
    with pytest.raises(ci.ContractError):
        ci.format_subject(schema, fields, "fixture result")
    fixture = copy.deepcopy(schema)
    fixture["patterns"]["task"] = "^LAB-[1-9][0-9]*$"
    fixture["diagnostic_example"]["task"] = "LAB-1"
    ci.validate_schema(fixture)
    assert "/LAB-2/" in ci.format_subject(
        fixture,
        {"surface": "codex", "task": "LAB-2", "work": "phase-a", "role": "executor"},
        "fixture result",
    )


@pytest.mark.parametrize(
    ("path", "field"),
    [
        (("schema_kind",), "schema_kind"),
        (("contract_version",), "contract_version"),
        (("patterns",), "patterns"),
        (("patterns", "contract_version"), "patterns.contract_version"),
        (("grammar",), "grammar"),
        (("grammar", "field_order"), "grammar.field_order"),
        (("grammar", "name"), "grammar.name"),
        (("grammar", "identity_template"), "grammar.identity_template"),
        (("grammar", "ordinary_pattern"), "grammar.ordinary_pattern"),
        (("grammar", "origin_pattern"), "grammar.origin_pattern"),
        (("grammar", "reserved_forms"), "grammar.reserved_forms"),
        (("grammar", "reserved_forms", 0, "name"), "grammar.reserved_forms[0].name"),
        (("grammar", "reserved_forms", 0, "prefix"), "grammar.reserved_forms[0]"),
        (("grammar", "fallback"), "grammar.fallback"),
        (("grammar", "fallback", "accepted"), "grammar.fallback.accepted"),
        (("grammar", "fallback", "name"), "grammar.fallback.name"),
        (("grammar", "fallback", "template"), "grammar.fallback.template"),
        (("registries",), "registries"),
        (("registries", "surfaces"), "registries.surfaces"),
        (("registries", "roles"), "registries.roles"),
        (("registries", "master_work"), "registries.master_work"),
        (("registries", "non_task_work"), "registries.non_task_work"),
        (("registries", "repository_policies"), "registries.repository_policies"),
        (("registries", "activation_statuses"), "registries.activation_statuses"),
        (("registries", "range_semantics"), "registries.range_semantics"),
        (("registries", "pre_anchor_history"), "registries.pre_anchor_history"),
        (("patterns", "task"), "patterns.task"),
        (("patterns", "phase_work"), "patterns.phase_work"),
        (("patterns", "research_work"), "patterns.research_work"),
        (("patterns", "object_id"), "patterns.object_id"),
        (("patterns", "safe_metadata"), "patterns.safe_metadata"),
        (("patterns", "credential_like"), "patterns.credential_like"),
        (("patterns", "task_path"), "patterns.task_path"),
        (("patterns", "relative_path"), "patterns.relative_path"),
        (("patterns", "environment_name"), "patterns.environment_name"),
        (("normalization",), "normalization"),
        (("normalization", "work_rules"), "normalization.work_rules"),
        (("normalization", "work_rules", 0, "name"), "normalization.work_rules[0].name"),
        (("normalization", "work_rules", 0, "pattern"), "normalization.work_rules[0].pattern"),
        (("normalization", "work_rules", 0, "template"), "normalization.work_rules[0].template"),
        (
            ("normalization", "work_rules", 0, "lowercase_groups"),
            "normalization.work_rules[0].lowercase_groups",
        ),
        (("cross_field",), "cross_field"),
        (("cross_field", "none_task"), "cross_field.none_task"),
        (("runtime",), "runtime"),
        (("runtime", "kind"), "runtime.kind"),
        (("runtime", "required_version"), "runtime.required_version"),
        (("runtime", "source"), "runtime.source"),
        (("runtime", "manifest"), "runtime.manifest"),
        (("runtime", "hook_targets"), "runtime.hook_targets"),
        (("runtime", "hook_entrypoints"), "runtime.hook_entrypoints"),
        (("runtime", "expected_context_env"), "runtime.expected_context_env"),
        (("runtime", "private_ledger"), "runtime.private_ledger"),
        (("trailers",), "trailers"),
        (("trailers", "content_origin"), "trailers.content_origin"),
        (("trailers", "agent_model"), "trailers.agent_model"),
        (("trailers", "agent_session"), "trailers.agent_session"),
        (("trailers", "source_commit"), "trailers.source_commit"),
        (("trailers", "co_author"), "trailers.co_author"),
        (("diagnostic_example",), "diagnostic_example"),
        (("diagnostic_example", "surface"), "diagnostic_example.surface"),
        (("diagnostic_example", "task"), "diagnostic_example.task"),
        (("diagnostic_example", "work"), "diagnostic_example.work"),
        (("diagnostic_example", "role"), "diagnostic_example.role"),
        (("diagnostic_example", "summary"), "diagnostic_example.summary"),
        (("truth_boundary",), "truth_boundary"),
        (("truth_boundary", "claim"), "truth_boundary.claim"),
        (("truth_boundary", "non_claims"), "truth_boundary.non_claims"),
        (("truth_boundary", "known_bypasses"), "truth_boundary.known_bypasses"),
    ],
)
def test_every_consumed_schema_owner_field_fails_closed_when_missing(contract, path, field):
    schema, _ = contract
    fixture = copy.deepcopy(schema)
    owner = fixture
    for part in path[:-1]:
        owner = owner[part]
    owner.pop(path[-1])
    with pytest.raises(ci.ContractError) as error:
        ci.validate_schema(fixture)
    assert error.value.code == ci.Codes.SCHEMA_SHAPE
    assert error.value.field == field


@pytest.mark.parametrize(
    ("mutation", "field"),
    [
        ("truth-boundary", "truth_boundary"),
        ("identity-template", "grammar.identity_template"),
    ],
)
def test_contract_loading_rejects_missing_semantic_owner_before_use(
    contract, mutation, field, tmp_path
):
    schema, state = contract
    fixture = copy.deepcopy(schema)
    if mutation == "truth-boundary":
        fixture.pop("truth_boundary")
    else:
        fixture["grammar"]["identity_template"] = "[{surface}/{task}/{work}] {summary}"
    schema_path = tmp_path / "schema.json"
    state_path = tmp_path / "state.json"
    schema_path.write_text(json.dumps(fixture), encoding="utf-8")
    state_path.write_text(json.dumps(state), encoding="utf-8")
    with pytest.raises(ci.ContractError) as error:
        ci.load_contract(schema_path, state_path)
    assert error.value.code == ci.Codes.SCHEMA_SHAPE
    assert error.value.field == field


@pytest.mark.parametrize(
    ("mutation", "field"),
    [
        ("truth-not-object", "truth_boundary"),
        ("truth-empty-claim", "truth_boundary.claim"),
        ("truth-empty-non-claims", "truth_boundary.non_claims"),
        ("truth-empty-bypasses", "truth_boundary.known_bypasses"),
        ("identity-missing-placeholder", "grammar.identity_template"),
        ("identity-unknown-placeholder", "grammar.identity_template"),
        ("identity-parser-incompatible", "grammar.identity_template"),
        ("ordinary-groups", "grammar.ordinary_pattern"),
        ("origin-groups", "grammar.origin_pattern"),
        ("normalization-template", "normalization.work_rules[0].template"),
        ("normalization-lowercase-group", "normalization.work_rules[0].lowercase_groups"),
    ],
)
def test_semantically_unusable_schema_owner_data_fails_at_load(contract, mutation, field):
    schema, _ = contract
    fixture = copy.deepcopy(schema)
    if mutation == "truth-not-object":
        fixture["truth_boundary"] = []
    elif mutation == "truth-empty-claim":
        fixture["truth_boundary"]["claim"] = ""
    elif mutation == "truth-empty-non-claims":
        fixture["truth_boundary"]["non_claims"] = []
    elif mutation == "truth-empty-bypasses":
        fixture["truth_boundary"]["known_bypasses"] = []
    elif mutation == "identity-missing-placeholder":
        fixture["grammar"]["identity_template"] = "[{surface}/{task}/{work}] {summary}"
    elif mutation == "identity-unknown-placeholder":
        fixture["grammar"]["identity_template"] = (
            "[{surface}/{task}/{work}/{role}] {summary} {unknown}"
        )
    elif mutation == "identity-parser-incompatible":
        fixture["grammar"]["identity_template"] = (
            "{summary} [{surface}/{task}/{work}/{role}]"
        )
    elif mutation == "ordinary-groups":
        fixture["grammar"]["ordinary_pattern"] = "^(?P<surface>.+)$"
    elif mutation == "origin-groups":
        fixture["grammar"]["origin_pattern"] = "^(?P<surface>.+)$"
    elif mutation == "normalization-template":
        fixture["normalization"]["work_rules"][0]["template"] = "phase-{missing}"
    else:
        fixture["normalization"]["work_rules"][0]["lowercase_groups"] = ["missing"]
    with pytest.raises(ci.ContractError) as error:
        ci.validate_schema(fixture)
    assert error.value.code == ci.Codes.SCHEMA_SHAPE
    assert error.value.field == field


@pytest.mark.parametrize(
    "work",
    ["master", "phase-a", "phase-a2", "phase-a3.4", "research-iter1", "docs", "knowledge",
     "release", "config", "init", "update", "maintenance"],
)
def test_all_work_classes_round_trip(contract, work):
    schema, _ = contract
    for surface, role in itertools.product(schema["registries"]["surfaces"], schema["registries"]["roles"]):
        fields = {"surface": surface, "task": "TFW-49", "work": work, "role": role}
        subject = ci.format_subject(schema, fields, "cross-domain result")
        parsed = ci.parse_subject(schema, subject, expected=fields)
        assert parsed.fields == fields


@pytest.mark.parametrize(
    ("legacy", "canonical"),
    [("PhaseA", "phase-a"), ("PhaseA2", "phase-a2"), ("PhaseA3.4", "phase-a3.4"),
     ("ResearchIter12", "research-iter12")],
)
def test_known_legacy_work_normalizes_only_at_format_boundary(contract, legacy, canonical):
    schema, _ = contract
    fields = {"surface": "codex", "task": "TFW-49", "work": legacy, "role": "executor"}
    assert f"/{canonical}/" in ci.format_subject(schema, fields, "normalized")
    with pytest.raises(ci.ContractError) as error:
        ci.parse_subject(schema, f"[codex/TFW-49/{legacy}/executor] not canonical")
    assert error.value.code == ci.Codes.WORK


@pytest.mark.parametrize(
    ("subject", "code"),
    [
        ("[windsurf/TFW-49/phase-a/executor] x", "E_SURFACE"),
        ("[codex/tfw-49/phase-a/executor] x", "E_TASK"),
        ("[codex/TFW-49/phase--a/executor] x", "E_WORK"),
        ("[codex/TFW-49/phase-a/maintainer] x", "E_ROLE"),
        ("[codex/latest/TFW-49/phase-a/executor] x", "E_SUBJECT_FORMAT"),
        ("[codex/TFW-49/phase-a/executor]  ", "E_SUBJECT_FORMAT"),
        ("[agent:codex][task:TFW-49][work:phase-a][role:executor] x", "E_SUBJECT_FORMAT"),
    ],
)
def test_invalid_or_fallback_subjects_fail_by_field(contract, subject, code):
    schema, _ = contract
    with pytest.raises(ci.ContractError) as error:
        ci.parse_subject(schema, subject)
    assert error.value.code == code


def test_search_keys_are_independent_and_regex_safe(contract):
    schema, _ = contract
    subject = ci.format_subject(
        schema,
        {"surface": "codex", "task": "TFW-49", "work": "phase-a3.4", "role": "executor"},
        "searchable result",
    )
    for value in ("codex", "TFW-49", "phase-a3.4", "executor"):
        assert __import__("re").search(__import__("re").escape(value), subject)


@pytest.mark.parametrize("form", ["fixup", "squash", "amend", "revert"])
def test_reserved_forms_require_exact_supplied_context(contract, form):
    schema, _ = contract
    fields = {"surface": "codex", "task": "TFW-49", "work": "phase-a", "role": "executor"}
    identity = ci.format_subject(schema, fields, "target result")
    record = next(item for item in schema["grammar"]["reserved_forms"] if item["name"] == form)
    subject = f"{record['prefix']}{identity}{record['suffix']}"
    assert ci.parse_subject(schema, subject, expected=fields).form == form
    for field in schema["grammar"]["field_order"]:
        stale = dict(fields)
        stale[field] = {
            "surface": "cursor", "task": "TFW-50", "work": "phase-b", "role": "reviewer"
        }[field]
        with pytest.raises(ci.ContractError) as error:
            ci.parse_subject(schema, subject, expected=stale)
        assert error.value.code == ci.Codes.CONTEXT_MISMATCH
    assert ci._parse_subject_structural(schema, subject).fields == fields


@pytest.mark.parametrize("form", ["fixup", "squash", "amend", "revert"])
def test_public_reserved_forms_reject_absent_expected_context(contract, form):
    schema, _ = contract
    fields = {"surface": "codex", "task": "TFW-49", "work": "phase-a", "role": "executor"}
    identity = ci.format_subject(schema, fields, "target result")
    record = next(item for item in schema["grammar"]["reserved_forms"] if item["name"] == form)
    subject = f"{record['prefix']}{identity}{record['suffix']}"
    with pytest.raises(ci.ContractError) as error:
        ci.parse_subject(schema, subject)
    assert error.value.code == ci.Codes.EXPECTED_CONTEXT
    assert error.value.field == "expected context"
    assert ci._parse_subject_structural(schema, subject).form == form


@pytest.mark.parametrize("form", ["fixup", "squash", "amend", "revert"])
def test_validate_subject_cli_reports_context_required_without_input_echo(
    contract, form, capsys
):
    schema, _ = contract
    fields = {"surface": "codex", "task": "TFW-49", "work": "phase-a", "role": "executor"}
    identity = ci.format_subject(schema, fields, "target result")
    record = next(item for item in schema["grammar"]["reserved_forms"] if item["name"] == form)
    subject = f"{record['prefix']}{identity}{record['suffix']}"
    assert ci.main(["validate-subject", "--subject", subject]) == 2
    output = capsys.readouterr()
    assert "E_EXPECTED_CONTEXT: expected context is required for a reserved subject form." in output.err
    assert subject not in output.err




def test_task_none_requires_declaration_lifecycle_and_clean_staged_names(contract, tmp_path):
    schema, _ = contract
    fields = {"surface": "codex", "task": "none", "work": "update", "role": "coordinator"}
    with pytest.raises(ci.ContractError) as error:
        ci.format_subject(schema, fields, "update runtime", staged_paths=[])
    assert error.value.code == ci.Codes.TASK_NONE_DECLARATION
    assert "/none/update/" in ci.format_subject(
        schema, fields, "update runtime", non_task=True, staged_paths=[]
    )
    for bad_work in ("master", "phase-a", "research-iter1"):
        with pytest.raises(ci.ContractError) as error:
            ci.validate_context(schema, {**fields, "work": bad_work}, non_task=True, staged_paths=[])
        assert error.value.code == ci.Codes.TASK_NONE_WORK
    repo = init_repo(tmp_path)
    (repo / "tasks" / "TFW-49__x").mkdir(parents=True)
    (repo / "tasks" / "TFW-49__x" / "x.txt").write_text("x", encoding="utf-8")
    git(repo, "add", "--", "tasks/TFW-49__x/x.txt")
    with pytest.raises(ci.ContractError) as error:
        ci.validate_context(schema, fields, non_task=True, staged_paths=ci.staged_paths(repo))
    assert error.value.code == ci.Codes.TASK_NONE_STAGED


def test_optional_origins_coauthors_and_metadata_remain_distinct(contract):
    schema, _ = contract
    message = """[codex/TFW-49/phase-a/executor] combine inseparable result

TFW-Content-Origin: claude-code/TFW-49/phase-a/executor
TFW-Content-Origin: codex/TFW-49/research-iter1/researcher
TFW-Agent-Model: gpt-5.6-sol
TFW-Agent-Session: session-opaque-1
TFW-Source-Commit: 0123456789abcdef0123456789abcdef01234567
Co-authored-by: Fixture Partner <fixture@example.invalid>
"""
    parsed = ci.validate_message(schema, message)
    assert parsed.fields["role"] == "executor"
    bad = message.replace("claude-code/TFW-49/phase-a/executor", "claude-code/executor")
    with pytest.raises(ci.ContractError) as error:
        ci.validate_message(schema, bad)
    assert error.value.code == ci.Codes.ORIGIN


@pytest.mark.parametrize(
    "mutation",
    ["version", "anchor", "registry", "hook", "hook-version", "hook-source", "auth"],
)
def test_state_failures_have_stable_codes(contract, mutation):
    schema, state = contract
    fixture = copy.deepcopy(state)
    if mutation == "version":
        fixture["contract_version"] = "2.0.0"
        code = ci.Codes.VERSION_MISMATCH
    elif mutation == "anchor":
        fixture["activation"]["last_pre_policy_commit"] = "missing"
        code = ci.Codes.STATE_SHAPE
    elif mutation == "registry":
        fixture["registries"] = {}
        code = ci.Codes.STATE_SHAPE
    elif mutation == "hook":
        fixture["hook_runtime"]["installed"] = False
        code = ci.Codes.STATE_SHAPE
    elif mutation == "hook-version":
        fixture["hook_runtime"]["required_version"] = "9.9.9"
        code = ci.Codes.STATE_SHAPE
    elif mutation == "hook-source":
        fixture["hook_runtime"]["source"] = "other/hooks"
        code = ci.Codes.STATE_SHAPE
    else:
        fixture["claims"]["actor_authentication"] = True
        code = ci.Codes.STATE_SHAPE
    with pytest.raises(ci.ContractError) as error:
        ci.validate_state(schema, fixture)
    assert error.value.code == code


@pytest.mark.parametrize(
    ("path", "code", "field"),
    [
        (("state_kind",), "E_STATE_SHAPE", "state_kind"),
        (("contract_version",), "E_VERSION_MISMATCH", "contract_version"),
        (("repository_policy",), "E_STATE_SHAPE", "repository_policy"),
        (("activation",), "E_STATE_SHAPE", "activation"),
        (("activation", "status"), "E_STATE_SHAPE", "activation.status"),
        (
            ("activation", "last_pre_policy_commit"),
            "E_STATE_SHAPE",
            "activation.last_pre_policy_commit",
        ),
        (("activation", "range_semantics"), "E_STATE_SHAPE", "activation.range_semantics"),
        (("activation", "pre_anchor_history"), "E_STATE_SHAPE", "activation.pre_anchor_history"),
        (("hook_runtime",), "E_STATE_SHAPE", "hook_runtime"),
        (
            ("hook_runtime", "required_version"),
            "E_STATE_SHAPE",
            "hook_runtime.required_version",
        ),
        (("hook_runtime", "source"), "E_STATE_SHAPE", "hook_runtime.source"),
        (("claims",), "E_STATE_SHAPE", "claims"),
        (("claims", "actor_authentication"), "E_STATE_SHAPE", "claims.actor_authentication"),
    ],
)
def test_every_consumed_state_owner_field_fails_closed_when_missing(
    contract, path, code, field
):
    schema, state = contract
    fixture = copy.deepcopy(state)
    owner = fixture
    for part in path[:-1]:
        owner = owner[part]
    owner.pop(path[-1])
    with pytest.raises(ci.ContractError) as error:
        ci.validate_state(schema, fixture)
    assert error.value.code == code
    assert error.value.field == field


def test_diagnostics_never_echo_arbitrary_inputs(contract, tmp_path, capsys, monkeypatch):
    sentinel = "LEAK_api_key_sk-EXAMPLE"
    message = tmp_path / f"{sentinel}.txt"
    message.write_text(f"not an identity {sentinel}\n\nTFW-Agent-Session: {sentinel}\n", encoding="utf-8")
    monkeypatch.setenv("TFW_FIXTURE_SECRET", sentinel)
    result = ci.main(["validate-message", "--message-file", str(message)])
    output = capsys.readouterr()
    assert result == 2
    assert sentinel not in output.out + output.err
    assert "Traceback" not in output.err
    assert "Correct form: [codex/TFW-49/phase-a/executor] describe the result" in output.err


def test_current_repository_exact_anchor_range_is_valid(contract):
    schema, state = contract
    result = ci.audit_range(schema, state, ROOT)
    assert result["anchor"] == state["activation"]["last_pre_policy_commit"]
    assert result["target"] == git(ROOT, "rev-parse", "HEAD")
    assert result["commit_count"] >= 3
    assert result["actor_authentication"] is False
    assert result["contract_version"] == "1.1.0"


def test_range_excludes_anchor_and_reports_every_invalid_descendant(contract, tmp_path):
    schema, state = contract
    repo = init_repo(tmp_path)
    anchor = commit(repo, "[master]: legacy anchor", "anchor.txt")
    valid = commit(repo, "[codex/TFW-49/phase-a/executor] valid result", "valid.txt")
    invalid1 = commit(repo, "missing identity one", "invalid1.txt")
    invalid2 = commit(repo, "[codex/TFW-49/phase--a/executor] invalid two", "invalid2.txt")
    with pytest.raises(ci.ContractError) as error:
        ci.audit_range(schema, project_state(state, anchor), repo)
    assert error.value.code == ci.Codes.RANGE_VIOLATION
    assert error.value.violations == (
        (invalid1, ci.Codes.SUBJECT_FORMAT),
        (invalid2, ci.Codes.WORK),
    )
    assert anchor not in dict(error.value.violations)
    assert valid not in dict(error.value.violations)


def test_merge_dag_descendants_are_unique_and_complete(contract, tmp_path):
    schema, state = contract
    repo = init_repo(tmp_path)
    anchor = commit(repo, "legacy anchor", "anchor.txt")
    git(repo, "branch", "side", anchor)
    commit(repo, "[codex/TFW-49/phase-a/executor] main result", "main.txt")
    git(repo, "checkout", "-q", "side")
    commit(repo, "[cursor/TFW-49/phase-a/reviewer] side result", "side.txt")
    git(repo, "checkout", "-q", "master")
    git(repo, "merge", "--no-ff", "-q", "-m", "[codex/TFW-49/phase-a/executor] merge result", "side")
    result = ci.audit_range(schema, project_state(state, anchor), repo)
    assert result["commit_count"] == 3
    assert len(result["commits"]) == len(set(result["commits"]))


def test_unborn_root_and_nonancestor_ranges_fail_or_close_explicitly(contract, tmp_path):
    schema, state = contract
    unborn = init_repo(tmp_path, "unborn")
    with pytest.raises(ci.ContractError) as error:
        ci.audit_range(schema, state, unborn)
    assert error.value.code == ci.Codes.RANGE_NO_TARGET
    repo = init_repo(tmp_path, "topology")
    root = commit(repo, "legacy root", "root.txt")
    assert ci.audit_range(schema, project_state(state, root), repo)["commit_count"] == 0
    anchor = commit(repo, "[codex/TFW-49/phase-a/executor] policy point", "anchor.txt")
    git(repo, "checkout", "-q", "-b", "other", root)
    target = commit(repo, "[codex/TFW-49/phase-a/executor] other line", "other.txt")
    with pytest.raises(ci.ContractError) as error:
        ci.audit_range(schema, project_state(state, anchor), repo, target)
    assert error.value.code == ci.Codes.RANGE_ANCESTRY


def test_state_template_is_clean_root_inclusive_and_current_state_stays_exclusive(
    contract,
):
    schema, state = contract
    template = json.loads(STATE_TEMPLATE.read_text(encoding="utf-8"))
    ci.validate_state(schema, template)
    assert template["activation"]["last_pre_policy_commit"] is None
    assert template["activation"]["range_semantics"] == "root-inclusive"
    assert template["activation"]["pre_anchor_history"] == "not-applicable"
    assert state["activation"]["range_semantics"] == "exclusive-anchor"
    assert state["activation"]["last_pre_policy_commit"] == (
        "f1106186417e84cdb38e797f7af66a60885bad76"
    )
    for owner in (template, state):
        assert "installed" not in owner["hook_runtime"]
        assert owner["hook_runtime"] == {
            "required_version": schema["runtime"]["required_version"],
            "source": schema["runtime"]["source"],
        }
    assert "f1106186417e84cdb38e797f7af66a60885bad76" not in (
        STATE_TEMPLATE.read_text(encoding="utf-8")
    )


@pytest.mark.parametrize(
    ("mode", "anchor", "history", "field"),
    [
        ("exclusive-anchor", None, "excluded", "activation.last_pre_policy_commit"),
        ("root-inclusive", "0" * 40, "not-applicable", "activation.last_pre_policy_commit"),
        ("exclusive-anchor", "0" * 40, "not-applicable", "activation.pre_anchor_history"),
        ("root-inclusive", None, "excluded", "activation.pre_anchor_history"),
    ],
)
def test_activation_mode_anchor_and_history_pairings_fail_closed(
    contract, mode, anchor, history, field
):
    schema, state = contract
    fixture = copy.deepcopy(state)
    fixture["activation"].update(
        {
            "range_semantics": mode,
            "last_pre_policy_commit": anchor,
            "pre_anchor_history": history,
        }
    )
    with pytest.raises(ci.ContractError) as error:
        ci.validate_state(schema, fixture)
    assert error.value.code == ci.Codes.STATE_SHAPE
    assert error.value.field == field


def test_root_inclusive_audit_includes_target_roots_and_multi_root_merge(
    contract, tmp_path
):
    schema, state = contract
    repo = init_repo(tmp_path, "root-inclusive")
    root_one = commit(
        repo, "[codex/TFW-49/phase-c/executor] create first root", "one.txt"
    )
    git(repo, "checkout", "--orphan", "other-root")
    git(repo, "rm", "-q", "-rf", ".")
    root_two = commit(
        repo, "[codex/TFW-49/phase-c/executor] create second root", "two.txt"
    )
    git(repo, "checkout", "-q", "master")
    git(
        repo,
        "merge",
        "--allow-unrelated-histories",
        "--no-ff",
        "-q",
        "-m",
        "[codex/TFW-49/phase-c/executor] merge both roots",
        "other-root",
    )
    target = git(repo, "rev-parse", "HEAD")
    result = ci.audit_range(schema, root_state(state), repo)
    assert result["anchor"] is None
    assert result["target"] == target
    assert result["commit_count"] == 3
    assert set(result["commits"]) == {root_one, root_two, target}
    assert result["actor_authentication"] is False


def test_root_inclusive_unborn_and_explicit_missing_target_fail_without_fallback(
    contract, tmp_path
):
    schema, state = contract
    repo = init_repo(tmp_path, "root-unborn")
    with pytest.raises(ci.ContractError) as error:
        ci.audit_range(schema, root_state(state), repo)
    assert error.value.code == ci.Codes.RANGE_NO_TARGET
    commit(repo, "[codex/TFW-49/phase-c/executor] create root", "root.txt")
    with pytest.raises(ci.ContractError) as error:
        ci.audit_range(schema, root_state(state), repo, "missing-target")
    assert error.value.code == ci.Codes.RANGE_TARGET


def test_shallow_history_fails_closed(contract, tmp_path):
    schema, state = contract
    source = init_repo(tmp_path, "source")
    anchor = commit(source, "legacy anchor", "anchor.txt")
    commit(source, "[codex/TFW-49/phase-a/executor] valid result", "valid.txt")
    clone = tmp_path / "shallow"
    subprocess.run(["git", "clone", "-q", "--depth", "1", source.resolve().as_uri(), str(clone)], check=True)
    with pytest.raises(ci.ContractError) as error:
        ci.audit_range(schema, project_state(state, anchor), clone)
    assert error.value.code == ci.Codes.RANGE_SHALLOW


def test_cli_uses_fixture_paths_and_schema_owned_truth_boundary(contract, tmp_path, capsys):
    schema, state = contract
    schema_path, state_path = tmp_path / "schema.json", tmp_path / "state.json"
    schema_path.write_text(json.dumps(schema), encoding="utf-8")
    state_path.write_text(json.dumps(state), encoding="utf-8")
    assert ci.main(["describe", "--schema", str(schema_path), "--state", str(state_path)]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["example"] == schema["grammar"]["identity_template"].format(
        **schema["diagnostic_example"]
    )
    assert payload["truth_boundary"] == schema["truth_boundary"]


def test_documented_examples_trailers_and_owner_links_are_schema_backed(contract):
    schema, _ = contract
    conventions = (ROOT / ".tfw" / "conventions.md").read_text(encoding="utf-8")
    glossary = (ROOT / ".tfw" / "glossary.md").read_text(encoding="utf-8")
    example = schema["grammar"]["identity_template"].format(**schema["diagnostic_example"])
    assert conventions.count(example) == 1
    assert ci.parse_subject(schema, example).fields["task"] == schema["diagnostic_example"]["task"]
    for name in schema["trailers"].values():
        assert name in conventions
    for owner in ("commit_identity.schema.json", "commit_identity_state.json", "scripts/commit_identity.py"):
        assert owner in conventions and owner in glossary
    assert "### Commit Identity and Attribution" in conventions
    assert "(conventions.md#commit-identity-and-attribution)" in glossary
    for unlisted in ("antigravity", "claude-code", "cursor", "researcher", "reviewer"):
        assert f"`{unlisted}`" not in conventions
