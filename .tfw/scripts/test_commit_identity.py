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
    assert state["hook_runtime"]["installed"] is False
    assert state["claims"]["actor_authentication"] is False


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
    assert imported <= {"argparse", "dataclasses", "json", "pathlib", "re", "subprocess", "sys", "typing"}
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
    assert ci.parse_subject(schema, subject, structural=True).fields == fields


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


@pytest.mark.parametrize("mutation", ["version", "anchor", "registry", "hook", "auth"])
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
        fixture["hook_runtime"]["installed"] = True
        code = ci.Codes.STATE_SHAPE
    else:
        fixture["claims"]["actor_authentication"] = True
        code = ci.Codes.STATE_SHAPE
    with pytest.raises(ci.ContractError) as error:
        ci.validate_state(schema, fixture)
    assert error.value.code == code


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
    assert error.value.code == ci.Codes.RANGE_ANCHOR
    repo = init_repo(tmp_path, "topology")
    root = commit(repo, "legacy root", "root.txt")
    assert ci.audit_range(schema, project_state(state, root), repo)["commit_count"] == 0
    anchor = commit(repo, "[codex/TFW-49/phase-a/executor] policy point", "anchor.txt")
    git(repo, "checkout", "-q", "-b", "other", root)
    target = commit(repo, "[codex/TFW-49/phase-a/executor] other line", "other.txt")
    with pytest.raises(ci.ContractError) as error:
        ci.audit_range(schema, project_state(state, anchor), repo, target)
    assert error.value.code == ci.Codes.RANGE_ANCESTRY


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
