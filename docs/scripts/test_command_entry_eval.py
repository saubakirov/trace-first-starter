"""Offline assurance for the explicit command-entry evaluation harness."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pytest

from docs.scripts import command_entry_eval as entry


def _command_event(command: str) -> dict:
    return {
        "type": "item.completed",
        "item": {"type": "command_execution", "command": command, "exit_code": 0},
    }


def _message_event(text: str) -> dict:
    return {"type": "item.completed", "item": {"type": "agent_message", "text": text}}


def _trace(spec: entry.FixtureSpec, arm: str, *, mutation: str | None = None) -> list[dict]:
    command = entry._command_name(spec.command)
    skill = entry._skill_path(command)
    workflow = entry._workflow_path(command)
    commands = [f"Get-Content -Raw -LiteralPath '{skill}'"]
    if arm != "direct":
        commands.append(f"Get-Content -Raw -LiteralPath '{workflow}'")
    for path in spec.required_inputs:
        if path not in {"AGENTS.md", workflow}:
            commands.append(f"Get-Content -Raw -LiteralPath '{path}'")
    if mutation == "no_invocation":
        commands = [value for value in commands if skill not in value]
    if mutation == "no_load":
        commands = [value for value in commands if workflow not in value]
    if mutation == "reordered" and arm != "direct":
        commands[0], commands[1] = commands[1], commands[0]
    events = [_command_event(value) for value in commands]
    message = " ".join(spec.final_patterns)
    if mutation == "wrong_route":
        message = "completed without the required route"
    events.append(_message_event(message))
    events.append({
        "type": "turn.completed",
        "usage": {"input_tokens": 7, "output_tokens": 3},
    })
    return events


def _fake_runner(command, cwd: Path, timeout_seconds: int) -> entry.RunnerResult:
    del timeout_seconds
    prompt = command[-1]
    spec = next(value for value in entry.fixture_specs() if value.prompt == prompt)
    selected = entry._command_name(spec.command)
    skill = (cwd / entry._skill_path(selected)).read_text(encoding="utf-8")
    arm = ("strengthened" if "This skill adds no algorithm." in skill
           else "direct" if entry._strip_frontmatter(skill).startswith("# TFW ")
           or entry._strip_frontmatter(skill).startswith("# TFW Handoff") else "current")
    for relative in spec.required_writes:
        destination = cwd / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text("offline fake-runner output\n", encoding="utf-8")
    stdout = "\n".join(json.dumps(value) for value in _trace(spec, arm)) + "\n"
    return entry.RunnerResult(0, stdout, "", 0.01)


def test_schedule_is_exact_interleaved_six_by_three_by_three():
    planned = entry.schedule(3)
    assert len(planned) == 54
    assert len({item.schedule_id for item in planned}) == 54
    assert [item.arm for item in planned[:3]] == list(entry.ARMS)
    assert [item.repetition for item in planned[:9]] == [1, 1, 1, 2, 2, 2, 3, 3, 3]
    assert {item.fixture for item in planned} == {spec.key for spec in entry.fixture_specs()}


def test_every_fixture_predeclares_one_role_gate_and_boundary():
    specs = entry.fixture_specs()
    assert len(specs) == 6
    assert {spec.role for spec in specs} == {"Coordinator", "Researcher", "Executor", "Reviewer"}
    assert all(spec.required_inputs and spec.forbidden_writes and spec.final_patterns and spec.gate
               for spec in specs)
    assert all(spec.command in {"/tfw-plan", "/tfw-research", "/tfw-handoff", "/tfw-review"}
               for spec in specs)


def test_arm_builders_are_exact_bounded_and_keep_one_canonical_body():
    validation = entry.validate_arm_builders()
    assert validation["valid"] is True
    assert validation["max_strengthened_word_delta"] == 15
    assert set(validation["strengthened_word_deltas"].values()) == {14, 15}
    manifest = entry._manifest()
    for command, row in manifest["commands"].items():
        current = entry.arm_skill(command, "current")
        assert current == (entry.PROJECT_ROOT / entry._source_skill_path(command)).read_text(encoding="utf-8")
        strong = entry.arm_skill(command, "strengthened")
        assert "Before task action" in strong
        assert "before reasoning or tools" in strong
        assert "Read Contract in order" in strong
        assert "This skill adds no algorithm." in strong
        direct = entry.arm_skill(command, "direct")
        canonical = (entry.PROJECT_ROOT / row["workflow"]).read_text(encoding="utf-8")
        assert entry._strip_frontmatter(direct) == entry._strip_frontmatter(canonical)


@pytest.mark.parametrize("arm", entry.ARMS)
def test_fixture_materialization_hashes_every_graded_input_and_cleans(tmp_path, arm):
    spec = entry.fixture_specs()[4]
    root, baseline, hashes = entry.create_fixture(spec, arm, tmp_path)
    assert root.is_relative_to(tmp_path.resolve())
    assert baseline
    assert entry._skill_path("handoff") in hashes
    assert entry._workflow_path("handoff") in hashes
    assert f"workspace/2026/{spec.task_id}/status.md" in hashes
    assert all(len(value) == 64 for value in hashes.values())
    entry.cleanup_fixture(root, tmp_path)
    assert not root.exists()


def test_cleanup_refuses_parent_and_repository_paths(tmp_path):
    with pytest.raises(RuntimeError, match="refusing cleanup"):
        entry.cleanup_fixture(tmp_path, tmp_path)
    with pytest.raises(RuntimeError, match="refusing cleanup"):
        entry.cleanup_fixture(entry.PROJECT_ROOT, entry.PROJECT_ROOT.parent)


@pytest.mark.parametrize("arm", entry.ARMS)
def test_graders_accept_independently_constructed_observed_trace(arm):
    spec = entry.fixture_specs()[1]
    result = entry.grade_run(spec, arm, _trace(spec, arm), ())
    assert result["aggregate_pass"] is True
    assert all(result["graders"].values())


@pytest.mark.parametrize(
    ("mutation", "grader"),
    (
        ("no_invocation", "invocation"),
        ("no_load", "complete_load"),
        ("reordered", "read_contract_order"),
        ("wrong_route", "final_route"),
    ),
)
def test_one_trace_mutant_per_read_and_route_grader_is_rejected(mutation, grader):
    spec = entry.fixture_specs()[1]
    result = entry.grade_run(spec, "current", _trace(spec, "current", mutation=mutation), ())
    assert result["graders"][grader] is False
    assert result["aggregate_pass"] is False


def test_role_gate_and_required_write_mutants_are_rejected():
    spec = entry.fixture_specs()[4]
    allowed = (f"workspace/2026/{spec.task_id}/ONB__{spec.task_id}.md",)
    normal = entry.grade_run(spec, "current", _trace(spec, "current"), allowed)
    assert normal["graders"]["role_artifact_boundary"] is True
    assert normal["graders"]["gate_stop"] is True
    missing = entry.grade_run(spec, "current", _trace(spec, "current"), ())
    assert missing["graders"]["gate_stop"] is False
    forbidden = entry.grade_run(
        spec, "current", _trace(spec, "current"),
        (*allowed, f"workspace/2026/{spec.task_id}/status.md"),
    )
    assert forbidden["graders"]["role_artifact_boundary"] is False


def test_parser_retains_raw_events_usage_and_rejects_unparsed_stdout():
    spec = entry.fixture_specs()[0]
    stdout = "\n".join(json.dumps(value) for value in _trace(spec, "current")) + "\n"
    events, unparsed = entry.parse_events(stdout)
    assert unparsed == []
    assert entry.event_usage(events) == {"input_tokens": 7, "output_tokens": 3, "total_tokens": 10}
    events, unparsed = entry.parse_events(stdout + "not-json\n")
    valid, reason = entry._valid_infrastructure(entry.RunnerResult(0, stdout, "", 1), events, unparsed)
    assert valid is False and reason == "unparsed_stdout"


@pytest.mark.parametrize(
    ("runner", "reason"),
    (
        (entry.RunnerResult(124, "", "", 180, True), "timeout"),
        (entry.RunnerResult(2, "", "error", 1), "codex_exit_2"),
        (entry.RunnerResult(0, "", "", 1), "no_json_events"),
    ),
)
def test_infrastructure_timeout_exit_and_missing_trace_are_invalid(runner, reason):
    valid, actual = entry._valid_infrastructure(runner, [], [])
    assert valid is False and actual == reason


def test_redaction_removes_credential_values_but_not_observable_commands():
    value = {
        "authorization": "Bearer abc.def",
        "message": "api_key=supersecret command=Get-Content",
        "nested": [{"access_token": "token-value"}],
    }
    redacted = entry.redact(value)
    rendered = json.dumps(redacted)
    assert "abc.def" not in rendered and "supersecret" not in rendered and "token-value" not in rendered
    assert "Get-Content" in rendered and rendered.count("<redacted>") == 3


def test_live_command_is_ephemeral_ignores_user_config_and_limits_workspace(tmp_path):
    command = entry.codex_command(tmp_path, "fixed prompt", "gpt-5.6-sol", "medium")
    assert command[:2] == ["codex", "exec"]
    assert "--ephemeral" in command and "--ignore-user-config" in command
    assert command[command.index("--sandbox") + 1] == "workspace-write"
    assert command[command.index("--model") + 1] == "gpt-5.6-sol"
    assert 'model_reasoning_effort="medium"' in command
    assert "--add-dir" not in command and command[-2:] == [str(tmp_path), "fixed prompt"]


def test_fake_runner_executes_one_attempt_without_network_and_captures_diff(tmp_path):
    spec = entry.fixture_specs()[4]
    item = next(item for item in entry.schedule(1) if item.fixture == spec.key and item.arm == "current")
    record = entry.execute_attempt(
        spec, item, 1, "gpt-5.6-sol", "medium", 30, _fake_runner, tmp_path,
    )
    assert record["valid"] is True
    assert record["grading"]["aggregate_pass"] is True
    assert record["usage"]["total_tokens"] == 10
    assert spec.required_writes[0] in record["grading"]["observed"]["changed_paths"]
    assert record["events"] and record["redaction"]["environment_serialized"] is False


def _args(tmp_path, output: Path, **overrides):
    values = {
        "model": "gpt-5.6-sol", "reasoning": "medium", "repetitions": 1,
        "max_runs": 18, "max_tokens": 750_000, "max_minutes": 180,
        "timeout_seconds": 30, "fixture_parent": str(tmp_path / "fixtures"),
        "output": str(output),
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def test_fake_matrix_completes_exact_valid_denominator_and_summary_checks(tmp_path):
    output = tmp_path / "trials.jsonl"
    assert entry.run_matrix(_args(tmp_path, output), _fake_runner) == 0
    records = entry._records(output)
    assert [record["record_type"] for record in records].count("attempt") == 18
    summary = entry.summarize_records(records, check=True)
    assert summary["valid_runs"] == 18 and summary["invalid_attempts"] == 0
    assert all(value["rate"] == 1.0 for value in summary["arms"].values())


def test_token_ceiling_blocks_before_smaller_denominator_can_be_accepted(tmp_path):
    output = tmp_path / "blocked.jsonl"
    assert entry.run_matrix(_args(tmp_path, output, max_tokens=1), _fake_runner) == 2
    records = entry._records(output)
    end = next(record for record in records if record["record_type"] == "run_end")
    assert end["valid_runs"] == 1
    assert end["blocked_reason"] == "token_ceiling_before_54_valid_runs"
    summary = entry.summarize_records(records, check=True)
    assert summary["ac3_status"] == "BLOCKED"
    assert summary["decision"]["terminal_result"] == "BASELINE RETAINED"
    assert summary["decision"]["production_skill_edits_authorized"] is False


def test_invalid_attempt_is_retained_then_same_schedule_item_is_rerun(tmp_path):
    calls = 0

    def flaky(command, cwd, timeout):
        nonlocal calls
        calls += 1
        if calls == 1:
            return entry.RunnerResult(2, "", "infrastructure failure", 0.01)
        return _fake_runner(command, cwd, timeout)

    output = tmp_path / "retried.jsonl"
    assert entry.run_matrix(_args(tmp_path, output), flaky) == 0
    attempts = [record for record in entry._records(output) if record["record_type"] == "attempt"]
    assert len(attempts) == 19
    assert attempts[0]["valid"] is False and attempts[0]["invalid_reason"] == "codex_exit_2"
    assert attempts[1]["schedule_id"] == attempts[0]["schedule_id"]
    assert attempts[1]["attempt"] == 2 and attempts[1]["valid"] is True


def test_finalize_stop_validates_raw_usage_basis_and_preserves_incomplete_denominator(tmp_path):
    output = tmp_path / "partial.jsonl"
    assert entry.run_matrix(_args(tmp_path, output), _fake_runner) == 0
    records = entry._records(output)
    partial = [records[0], *records[1:3]]
    output.write_text("\n".join(json.dumps(record) for record in partial) + "\n", encoding="utf-8")
    args = argparse.Namespace(
        input=str(output), reason="coordinator_stop_test", basis_runs=2, basis_tokens=20,
        unreported_interrupted_attempt=True,
    )
    assert entry.finalize_stop_command(args) == 0
    stopped = entry._records(output)
    end = stopped[-1]
    assert end["coordinator_stop"]["linear_projection_for_approved_denominator"] == 180.0
    assert end["coordinator_stop"]["unreported_interrupted_attempt"] is True
    summary = entry.summarize_records(stopped, check=True)
    assert summary["valid_runs"] == 2 and summary["valid_denominator"] == 18
    assert summary["ac3_status"] == "BLOCKED"


def test_wilson_and_newcombe_are_bounded_and_directional():
    low, high = entry.wilson_interval(9, 18)
    assert 0 < low < 0.5 < high < 1
    forward = entry.newcombe_difference(18, 18, 9, 18)
    reverse = entry.newcombe_difference(9, 18, 18, 18)
    assert forward[0] > 0
    assert reverse[1] < 0
    assert forward == pytest.approx((-reverse[1], -reverse[0]))


def _role_counts(current, strengthened, direct):
    roles = ("Coordinator", "Researcher", "Executor", "Reviewer")
    totals = {"Coordinator": 9, "Researcher": 3, "Executor": 3, "Reviewer": 3}
    return {
        arm: {role: (success[role], totals[role]) for role in roles}
        for arm, success in {
            "current": current, "strengthened": strengthened, "direct": direct,
        }.items()
    }


def test_decision_retains_baseline_for_tie_below_threshold_and_role_loss():
    same = {"Coordinator": 6, "Researcher": 2, "Executor": 2, "Reviewer": 2}
    counts = {"current": (12, 18), "strengthened": (12, 18), "direct": (12, 18)}
    decision = entry.production_decision(counts, _role_counts(same, same, same), 15)
    assert decision["terminal_result"] == "BASELINE RETAINED"
    assert decision["comparisons"]["strengthened"]["behavioural_rule_pass"] is False


def test_decision_selects_strengthened_only_after_every_threshold():
    current = {"Coordinator": 0, "Researcher": 0, "Executor": 0, "Reviewer": 0}
    strong = {"Coordinator": 9, "Researcher": 3, "Executor": 3, "Reviewer": 3}
    direct = {"Coordinator": 0, "Researcher": 0, "Executor": 0, "Reviewer": 0}
    counts = {"current": (0, 18), "strengthened": (18, 18), "direct": (0, 18)}
    decision = entry.production_decision(counts, _role_counts(current, strong, direct), 15)
    assert decision["terminal_result"] == "STRENGTHENED SELECTED"
    assert decision["comparisons"]["strengthened"]["difference_interval_95"][0] > 0
    assert entry.production_decision(counts, _role_counts(current, strong, direct), 16)[
        "terminal_result"] == "BASELINE RETAINED"
    assert entry.production_decision(counts, _role_counts(current, strong, direct), 15, False)[
        "terminal_result"] == "BASELINE RETAINED"


def test_decision_blocks_direct_material_win_before_production_migration():
    current = {"Coordinator": 0, "Researcher": 0, "Executor": 0, "Reviewer": 0}
    direct = {"Coordinator": 9, "Researcher": 3, "Executor": 3, "Reviewer": 3}
    counts = {"current": (0, 18), "strengthened": (0, 18), "direct": (18, 18)}
    decision = entry.production_decision(counts, _role_counts(current, current, direct), 15)
    assert decision["terminal_result"] == "BLOCKED — NEW TS REQUIRED"
    assert "no production migration authority" in decision["reason"]


def test_dry_run_emits_schedule_without_materializing_a_fixture(tmp_path, capsys, monkeypatch):
    before = set(tmp_path.iterdir())
    monkeypatch.setattr(entry.tempfile, "gettempdir", lambda: str(tmp_path))
    args = argparse.Namespace(model="gpt-5.6-sol", reasoning="medium", repetitions=3)
    assert entry.dry_run_command(args) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["valid_denominator"] == 54
    assert len(payload["schedule"]) == 54
    assert set(tmp_path.iterdir()) == before
