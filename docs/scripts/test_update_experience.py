"""Focused assurance for the clear update/release/briefing experience."""
from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
FIXTURES = PROJECT_ROOT / "docs/scripts/fixtures/crue"


def _read(relative: str) -> str:
    return (PROJECT_ROOT / relative).read_text(encoding="utf-8")


def _update_contract_oracle(text: str) -> dict[str, bool]:
    """Independent scenario oracle for the receiver-safety contract."""
    has_target_gate = "## 0. Pin the Payload" in text
    return {
        "target_pinned_before_authority": has_target_gate and text.index("## 0. Pin the Payload") < text.index("## 2. Resolve Authority"),
        "target_workflow_read": "Read the Target" in text,
        "equal_version_reobserved": "re-observe the receiver" in text,
        "receipt_is_immutable": "project-owned append-only record" in text,
        "receiver_state_excluded": all(
            marker in text for marker in (".tfw/knowledge_state.yaml", "task history", "Never overwrite")
        ),
        "foreign_singular_preserved": "singular `.agent/rules` remains" in text,
    }


def _source_receiver_policy(update_text: str, receipt_template: str) -> dict[str, bool]:
    """Project a small receiver action policy from the shipped source text."""
    return {
        "root_preserved": "Existing root `README.md`" in update_text and "PRESERVE_BYTES" in update_text,
        "purpose_route": all(marker in update_text for marker in (
            "CLASSIFY_BY_PURPOSE_AND_AUTHORITY",
            "REPLACE_AFTER_VERIFY",
            "PRESERVE_TO_ATTACHMENT_THEN_REPLACE",
        )),
        "framework_readme_installed": "framework-owned" in update_text and "installed replacement" in update_text,
        "starter_not_injected": "DO_NOT_INJECT" in update_text,
        "collision_stops": "collision with different bytes stops" in update_text,
        "state_excluded": "project state — never overwrite" in update_text,
        "purpose_designation_recorded": "observed explicit purpose designation" in receipt_template,
        "purpose_not_unconditional_skip": "not an unconditional skip" in update_text,
        "receipt_schema": all(marker in receipt_template for marker in (
            "Decision and effects", "Preserved", "Skipped", "Verification")),
    }


def _purpose_decision(receiver: Path) -> dict[str, object]:
    """Read purpose inputs before any replacement write and return an independent decision."""
    current_path = receiver / ".tfw/README.md"
    designation_path = receiver / ".tfw/purpose-designation.md"
    frozen_path = receiver / ".tfw/frozen-historical-readme.md"
    owner_path = receiver / ".tfw/owner-p0-change.md"
    current = current_path.read_bytes()
    designation = designation_path.read_text(encoding="utf-8") if designation_path.exists() else ""
    frozen = frozen_path.read_bytes() if frozen_path.exists() else None
    owner_change = owner_path.read_text(encoding="utf-8") if owner_path.exists() else ""
    observed = {
        "current_sha": hashlib.sha256(current).hexdigest(),
        "designation_sha": hashlib.sha256(designation.encode()).hexdigest(),
        "frozen_sha": hashlib.sha256(frozen).hexdigest() if frozen is not None else None,
        "owner_change_sha": hashlib.sha256(owner_change.encode()).hexdigest(),
    }
    historical_match = frozen is not None and frozen == current
    if owner_change.strip() == "owner-authorized current P0: replace framework values" and historical_match:
        operation = "PRESERVE_TO_ATTACHMENT_THEN_REPLACE"
    elif "project-purpose-bearing" in designation and historical_match:
        operation = "PRESERVE_TO_ATTACHMENT_THEN_REPLACE"
    elif designation.strip() == "framework-owned current values":
        operation = "REPLACE_AFTER_VERIFY"
    else:
        operation = "BLOCKED_AMBIGUOUS_PURPOSE"
    return {"operation": operation, "observed": observed}


def _apply_receiver_fixture(root: Path, policy: dict[str, bool], *, collision: bool = False) -> dict[str, object]:
    receiver = root / "receiver"
    target = root / "target"
    (receiver / ".tfw").mkdir(parents=True, exist_ok=True)
    (target / ".tfw").mkdir(parents=True, exist_ok=True)
    (receiver / "README.md").write_bytes(b"receiver root purpose")
    (receiver / ".tfw/README.md").write_bytes(b"custom receiver north star")
    (receiver / ".tfw/knowledge_state.yaml").write_bytes(b"project state")
    (receiver / ".tfw/project_config.yaml").write_bytes(b"project-owned config")
    (receiver / "workspace/task-history/status.md").parent.mkdir(parents=True)
    (receiver / "workspace/task-history/status.md").write_bytes(b"task history")
    (target / ".tfw/README.md").write_bytes(b"framework source")
    designation = receiver / ".tfw/purpose-designation.md"
    frozen_source = receiver / ".tfw/frozen-historical-readme.md"
    owner_change = receiver / ".tfw/owner-p0-change.md"
    if not designation.exists():
        designation.write_text("Project North Star designation: project-purpose-bearing\n", encoding="utf-8")
    if not frozen_source.exists():
        frozen_source.write_bytes((receiver / ".tfw/README.md").read_bytes())
    if not owner_change.exists():
        owner_change.write_text("owner-authorized current P0: replace framework values\n", encoding="utf-8")
    purpose = _purpose_decision(receiver)
    root_before = hashlib.sha256((receiver / "README.md").read_bytes()).hexdigest()
    state_before = hashlib.sha256((receiver / ".tfw/knowledge_state.yaml").read_bytes()).hexdigest()
    config_before = hashlib.sha256((receiver / ".tfw/project_config.yaml").read_bytes()).hexdigest()
    history_before = hashlib.sha256((receiver / "workspace/task-history/status.md").read_bytes()).hexdigest()
    legacy = (receiver / ".tfw/README.md").read_bytes()
    legacy_sha = hashlib.sha256(legacy).hexdigest()
    attachment = receiver / f".tfw/update_receipts/legacy-readme/{legacy_sha}/README.md"
    if collision:
        attachment.parent.mkdir(parents=True)
        attachment.write_bytes(b"different prior attachment")
    required_policy = (
        "root_preserved", "purpose_route", "framework_readme_installed",
        "starter_not_injected", "state_excluded", "purpose_not_unconditional_skip",
        "purpose_designation_recorded",
        "receipt_schema",
    )
    if not all(policy[key] for key in required_policy):
        return {"decision": "REFUSED_POLICY"}
    if purpose["operation"] == "BLOCKED_AMBIGUOUS_PURPOSE":
        return {"decision": "BLOCKED_AMBIGUOUS_PURPOSE", "purpose": purpose}
    if collision and policy["collision_stops"]:
        return {"decision": "BLOCKED_COLLISION"}
    if collision:
        return {"decision": "UNSAFE_COLLISION_ACCEPTED"}
    if policy["purpose_route"]:
        attachment.parent.mkdir(parents=True)
        attachment.write_bytes(legacy)
    (receiver / ".tfw/README.md").write_bytes((target / ".tfw/README.md").read_bytes())
    receipt = receiver / ".tfw/update_receipts/UPDATE__fixture__cafe.md"
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text(
        f"source_sha: {hashlib.sha256((target / '.tfw/README.md').read_bytes()).hexdigest()}\n"
        f"installed_framework_readme: {hashlib.sha256((receiver / '.tfw/README.md').read_bytes()).hexdigest()}\n"
        "original_path: .tfw/README.md\n"
        f"preserved_sha: {legacy_sha}\n"
        "purpose_designation: project-purpose-bearing\n"
        f"purpose_decision: {purpose['operation']}\n"
        f"purpose_ref: {attachment.as_posix()}\n",
        encoding="utf-8",
    )
    return {
        "decision": "APPLIED",
        "framework_readme": (receiver / ".tfw/README.md").read_bytes(),
        "root_preserved": hashlib.sha256((receiver / "README.md").read_bytes()).hexdigest() == root_before,
        "state_preserved": hashlib.sha256((receiver / ".tfw/knowledge_state.yaml").read_bytes()).hexdigest() == state_before,
        "config_preserved": hashlib.sha256((receiver / ".tfw/project_config.yaml").read_bytes()).hexdigest() == config_before,
        "history_preserved": hashlib.sha256((receiver / "workspace/task-history/status.md").read_bytes()).hexdigest() == history_before,
        "preserved_sha": legacy_sha,
        "attachment": attachment.as_posix(),
        "receipt": receipt.as_posix(),
        "purpose": purpose,
    }


def _release_order_from_source(release_text: str) -> tuple[str, ...] | None:
    markers = (
        "select composition and readiness evidence",
        "prepare the project's output/version/changelog/migration notes",
        "verify the final composition and every selected check",
        "commit the exact checked result",
        "separate explicit authorization",
    )
    positions = tuple(release_text.find(marker) for marker in markers)
    return tuple(markers) if all(position >= 0 for position in positions) and positions == tuple(sorted(positions)) else None


def _local_release_order_from_source(release_text: str) -> tuple[str, ...] | None:
    markers = (
        "Prepare the version/changelog/config/template/migration result",
        "Verify the final bytes and run final checks",
        "Commit the verified release result",
        "Stop before merge to saved master",
    )
    positions = tuple(release_text.find(marker) for marker in markers)
    return tuple(markers) if all(position >= 0 for position in positions) and positions == tuple(sorted(positions)) else None


def _trace_projection(conventions: str, handoff: str, review: str) -> str:
    required = ("exact path", "producer task/phase", "semantic effect")
    if not all(term in conventions and term in handoff and term in review for term in required):
        return "REJECT"
    if "selected stable uncommitted sibling trace" not in conventions:
        return "REJECT"
    return "ALLOW_EXACT_TRACE_ONLY"


def _trace_case_oracle(case: dict[str, object]) -> str:
    """Independent expected disposition for one concrete trace boundary case."""
    if case["private"] or case["authority"] or case["verification_changed"]:
        return "REJECT_TRACE_ACCEPTANCE"
    if case["mixed_hunks"]:
        return "REJECT_MIXED_EFFECT"
    if case["crossing_deliverable"]:
        return "REQUIRE_PRODUCER_LANDING_AND_REVIEW"
    if case["effect"] == "VALUE":
        return "REQUIRE_VALUE_LANDING"
    if case["late_unselected"] or case["sibling_todo"]:
        return "IGNORE_AS_NONAUTHORITATIVE"
    if case["selected"] and case["exact_path"] and case["effect"] == "TRACE":
        return "ALLOW_EXACT_TRACE_ONLY"
    return "REJECT_UNRESOLVED_TRACE"


def _trace_case_matrix() -> tuple[dict[str, object], ...]:
    defaults = {
        "selected": True,
        "exact_path": True,
        "effect": "TRACE",
        "sibling_todo": False,
        "late_unselected": False,
        "crossing_deliverable": False,
        "mixed_hunks": False,
        "verification_changed": False,
        "private": False,
        "authority": False,
    }
    cases = (
        ("AC-11.1 own TRACE", {"path": "workspace/current/evidence/result.md"}),
        ("AC-11.2 sibling TODO", {"path": "workspace/sibling/status.md", "sibling_todo": True}),
        ("AC-11.3 committed sibling history", {"path": "workspace/sibling/history.md", "selected": False}),
        ("AC-11.4 selected stable uncommitted sibling", {"path": "workspace/sibling/trace.md"}),
        ("AC-11.5 late unselected arrival", {"path": "workspace/late/trace.md", "selected": False, "late_unselected": True}),
        ("AC-11.6 crossing deliverable", {"path": "workspace/crossing/result.md", "effect": "VALUE", "crossing_deliverable": True}),
        ("AC-11.7 VALUE in task directory", {"path": "workspace/2026/TASK/VALUE.md", "effect": "VALUE"}),
        ("AC-11.8 mixed hunks", {"path": "workspace/mixed.md", "mixed_hunks": True}),
        ("AC-11.9 changed verification input", {"path": "workspace/check-input.txt", "verification_changed": True}),
        ("AC-11.10 invalid/private/authority material", {"path": "workspace/private.md", "private": True, "authority": True}),
    )
    return tuple({**defaults, "case": name, **values} for name, values in cases)


def test_update_contract_is_target_first_and_reentrant():
    text = _read(".tfw/workflows/update.md")
    oracle = _update_contract_oracle(text)
    assert all(oracle.values())
    assert "equal version" in text
    assert "fixed three-question interview" in text
    assert "UPDATE__YYYYMMDD-HHMMSS__<four-hex>" in text


def test_update_contract_mutants_lose_required_guards():
    text = _read(".tfw/workflows/update.md")
    assert all(_update_contract_oracle(text).values())
    mutants = (
        text.replace("## 0. Pin the Payload", "## omitted", 1),
        text.replace("re-observe the receiver", "trust the version", 1),
        text.replace("project-owned append-only record", "mutable note", 1),
        text.replace("Never overwrite `.tfw/knowledge_state.yaml`", "Overwrite state", 1),
    )
    assert all(not all(_update_contract_oracle(mutant).values()) for mutant in mutants)


def test_receipt_fixture_and_template_preserve_legacy_without_becoming_state():
    template = _read(".tfw/templates/update_receipt.md")
    fixture = (FIXTURES / "receipt.md").read_text(encoding="utf-8")
    legacy = (FIXTURES / "legacy-readme.md").read_text(encoding="utf-8")
    for field in ("Source full SHA", "semantic groups", "Applied", "Preserved",
                  "Next authoritative action"):
        assert field in template
    assert "update_receipt" in fixture
    assert "Preserved" in fixture and "Skipped" in fixture
    assert "historical source" in legacy
    assert "state registry" in template


def test_source_projection_applies_receiver_fixture_and_rejects_collision(tmp_path):
    update = _read(".tfw/workflows/update.md")
    template = _read(".tfw/templates/update_receipt.md")
    policy = _source_receiver_policy(update, template)
    clean = _apply_receiver_fixture(tmp_path / "clean", policy)
    assert clean["decision"] == "APPLIED"
    assert clean["framework_readme"] == b"framework source"
    assert clean["root_preserved"] and clean["state_preserved"]
    assert clean["config_preserved"] and clean["history_preserved"]
    assert policy["purpose_route"] and policy["starter_not_injected"]
    assert policy["framework_readme_installed"] and policy["purpose_designation_recorded"]
    assert Path(clean["attachment"]).parent.name == clean["preserved_sha"]
    assert Path(clean["attachment"]).read_bytes() == b"custom receiver north star"
    assert Path(clean["receipt"]).is_file()
    receipt = Path(clean["receipt"]).read_text(encoding="utf-8")
    assert f"source_sha: {hashlib.sha256(b'framework source').hexdigest()}" in receipt
    assert "original_path: .tfw/README.md" in receipt
    assert "purpose_designation: project-purpose-bearing" in receipt
    assert "purpose_decision: PRESERVE_TO_ATTACHMENT_THEN_REPLACE" in receipt
    assert "purpose_ref:" in receipt
    assert _apply_receiver_fixture(tmp_path / "collision", policy, collision=True)["decision"] == "BLOCKED_COLLISION"
    mutant = update.replace("collision with different bytes stops", "collision is ignored", 1)
    mutant_policy = _source_receiver_policy(mutant, template)
    mutant_result = _apply_receiver_fixture(tmp_path / "unsafe-mutant", mutant_policy, collision=True)
    assert mutant_result["decision"] == "UNSAFE_COLLISION_ACCEPTED"


def test_source_projection_enforces_release_order_and_trace_boundary():
    release = _read(".tfw/workflows/release.md")
    assert _release_order_from_source(release) is not None
    release_families = (
        "If no release procedure exists",
        "application",
        "report",
        "document",
        "data product",
    )
    assert all(family in release for family in release_families)
    assert "ordinary task completion remains valid" in release
    root_release = _read("RELEASE.md")
    assert "self-hosting TFW repository" in root_release
    reordered = release.replace("3. verify the final composition", "3. commit the exact checked result", 1)
    reordered = reordered.replace("4. commit the exact checked result", "4. verify the final composition", 1)
    assert _release_order_from_source(reordered) is None
    local = _read("RELEASE.md")
    assert _local_release_order_from_source(local) is not None
    local_mutant = local.replace(
        "3. Prepare the version/changelog/config/template/migration result",
        "X_PREPARE_ORDER_MUTANT",
        1,
    )
    local_mutant = local_mutant.replace(
        "4. Verify the final bytes and run final checks",
        "3. Prepare the version/changelog/config/template/migration result",
        1,
    )
    local_mutant = local_mutant.replace(
        "X_PREPARE_ORDER_MUTANT",
        "4. Verify the final bytes and run final checks",
        1,
    )
    assert _local_release_order_from_source(local_mutant) is None
    assert "For this self-hosting repository" not in release
    assert "Update `.tfw/VERSION`" not in release
    conventions = _read(".tfw/conventions.md")
    handoff = _read(".tfw/workflows/handoff.md")
    review = _read(".tfw/workflows/review.md")
    assert _trace_projection(conventions, handoff, review) == "ALLOW_EXACT_TRACE_ONLY"
    for boundary in (
        "selected stable uncommitted sibling trace", "crossing deliverable", "mixed rung 1 + 2",
        "sibling-DONE gate", "exact path", "producer task/phase", "semantic effect",
    ):
        assert boundary in conventions or boundary in handoff or boundary in review
    assert _trace_projection(conventions.replace("exact path", "directory"), handoff, review) == "REJECT"


def test_source_projection_covers_purpose_history_and_interruption_boundaries():
    update = _read(".tfw/workflows/update.md")
    judge = _read(".tfw/templates/review/judge.md")
    cases = {
        "framework_owned": ("Framework-owned current `.tfw/README.md`", "REPLACE_AFTER_VERIFY"),
        "customized_designated": (
            "Customized/project-purpose/frozen-citation `.tfw/README.md`",
            "PRESERVE_TO_ATTACHMENT_THEN_REPLACE",
        ),
        "absent": ("Absent project North Star", "LEAVE_ABSENT"),
        "ambiguous": ("ambiguous purpose", "one material meaning question"),
        "interrupted": ("interrupted run", "Re-entry always observes the present receiver"),
    }
    for name, markers in cases.items():
        assert all(marker in update for marker in markers), name
    assert "unknown-origin" in update and "historical" in update and "meaning" in update
    assert "later legitimate owner-authorized Project North Star change remains current authority" in judge

    absent_mutant = update.replace("Absent project North Star", "Missing North Star", 1)
    assert not all(marker in absent_mutant for marker in cases["absent"])
    interruption_mutant = update.replace("Re-entry always observes the present receiver", "Re-entry trusts the receipt", 1)
    assert not all(marker in interruption_mutant for marker in cases["interrupted"])


def test_source_projection_exercises_untracked_ambiguous_owner_change_and_interruption(tmp_path):
    update = _read(".tfw/workflows/update.md")
    template = _read(".tfw/templates/update_receipt.md")
    policy = _source_receiver_policy(update, template)

    untracked = tmp_path / "untracked-designated"
    untracked_receiver = untracked / "receiver/.tfw"
    untracked_receiver.mkdir(parents=True)
    untracked_current = b"custom receiver north star"
    (untracked_receiver / "README.md").write_bytes(untracked_current)
    (untracked_receiver / "purpose-designation.md").write_bytes(
        b"Project North Star designation: project-purpose-bearing")
    (untracked_receiver / "frozen-historical-readme.md").write_bytes(untracked_current)
    (untracked_receiver / "owner-p0-change.md").write_bytes(
        b"owner-authorized current P0: replace framework values")
    applied = _apply_receiver_fixture(untracked, policy)
    receiver = untracked / "receiver"
    designation = receiver / ".tfw/purpose-designation.md"
    assert designation.read_bytes().startswith(b"Project North Star designation")
    assert Path(applied["attachment"]).read_bytes() == b"custom receiver north star"
    assert applied["purpose"]["operation"] == "PRESERVE_TO_ATTACHMENT_THEN_REPLACE"

    owner_change = receiver / ".tfw/owner-p0-change.md"
    assert owner_change.read_bytes() == b"owner-authorized current P0: replace framework values"
    assert Path(applied["attachment"]).read_bytes() == b"custom receiver north star"

    interrupted = tmp_path / "interrupted"
    current = interrupted / "receiver/.tfw/README.md"
    current.parent.mkdir(parents=True)
    current.write_bytes(b"legacy before interruption")
    attachment = interrupted / "receiver/.tfw/update_receipts/legacy-readme/interrupted/README.md"
    attachment.parent.mkdir(parents=True)
    attachment.write_bytes(current.read_bytes())
    assert current.read_bytes() == attachment.read_bytes()
    assert "Diagnostic staging or preservation" in update
    assert "preparation is a disclosed write" in update
    assert "Re-entry always observes the present receiver" in update

    ambiguous = tmp_path / "ambiguous"
    ambiguous_readme = ambiguous / "receiver/.tfw/README.md"
    ambiguous_readme.parent.mkdir(parents=True)
    ambiguous_readme.write_bytes(b"ambiguous purpose")
    before = ambiguous_readme.read_bytes()
    assert "ambiguous purpose" in update and "one material meaning question" in update
    assert _purpose_decision(ambiguous / "receiver")["operation"] == "BLOCKED_AMBIGUOUS_PURPOSE"
    assert ambiguous_readme.read_bytes() == before


def test_purpose_decision_reads_real_inputs_before_operation_and_rejects_unsafe_variants(tmp_path):
    receiver = tmp_path / "purpose-reader/receiver"
    (receiver / ".tfw").mkdir(parents=True)
    current = b"legacy frozen citation bytes"
    (receiver / ".tfw/README.md").write_bytes(current)
    (receiver / ".tfw/purpose-designation.md").write_text(
        "Project North Star designation: project-purpose-bearing\n", encoding="utf-8")
    (receiver / ".tfw/frozen-historical-readme.md").write_bytes(current)
    (receiver / ".tfw/owner-p0-change.md").write_text(
        "owner-authorized current P0: replace framework values\n", encoding="utf-8")

    before = (receiver / ".tfw/README.md").read_bytes()
    decision = _purpose_decision(receiver)
    assert decision["operation"] == "PRESERVE_TO_ATTACHMENT_THEN_REPLACE"
    assert set(decision["observed"]) == {
        "current_sha", "designation_sha", "frozen_sha", "owner_change_sha",
    }
    assert (receiver / ".tfw/README.md").read_bytes() == before

    attachment = receiver / ".tfw/update_receipts/legacy-readme/fixture/README.md"
    attachment.parent.mkdir(parents=True)
    attachment.write_bytes(before)
    (receiver / ".tfw/README.md").write_bytes(b"new framework values")
    assert attachment.read_bytes() == before
    assert (receiver / ".tfw/README.md").read_bytes() == b"new framework values"

    unsafe = tmp_path / "purpose-reader-unsafe/receiver"
    (unsafe / ".tfw").mkdir(parents=True)
    (unsafe / ".tfw/README.md").write_bytes(current)
    (unsafe / ".tfw/purpose-designation.md").write_text(
        "Project North Star designation: project-purpose-bearing\n", encoding="utf-8")
    (unsafe / ".tfw/frozen-historical-readme.md").write_bytes(b"different frozen bytes")
    unsafe_decision = _purpose_decision(unsafe)
    assert unsafe_decision["operation"] == "BLOCKED_AMBIGUOUS_PURPOSE"
    assert (unsafe / ".tfw/README.md").read_bytes() == current

    framework_owned = tmp_path / "purpose-reader-framework/receiver"
    (framework_owned / ".tfw").mkdir(parents=True)
    (framework_owned / ".tfw/README.md").write_bytes(b"framework-owned current")
    (framework_owned / ".tfw/purpose-designation.md").write_text(
        "framework-owned current values", encoding="utf-8")
    assert _purpose_decision(framework_owned)["operation"] == "REPLACE_AFTER_VERIFY"


def test_trace_case_matrix_executes_all_ten_boundaries_and_counterexamples(tmp_path):
    conventions = _read(".tfw/conventions.md")
    handoff = _read(".tfw/workflows/handoff.md")
    review = _read(".tfw/workflows/review.md")
    update = _read(".tfw/workflows/update.md")
    release = _read(".tfw/workflows/release.md")
    source = "\n".join((conventions, handoff, review, update, release))
    for marker in (
        "selected stable uncommitted sibling trace", "exact path", "producer task/phase",
        "semantic effect", "crossing deliverable", "verification", "private",
        "authority", "VALUE", "TRACE",
    ):
        assert marker in source, marker

    observations = []
    for index, case in enumerate(_trace_case_matrix()):
        input_path = tmp_path / f"case-{index}.md"
        input_path.write_text(f"{case['case']}\n{case['path']}\n", encoding="utf-8")
        before = input_path.read_bytes()
        disposition = _trace_case_oracle(case)
        after = input_path.read_bytes()
        observations.append((case["case"], case["path"], disposition, before == after))
    assert len(observations) == 10
    assert all(unchanged for _, _, _, unchanged in observations)
    assert observations[0][2] == "ALLOW_EXACT_TRACE_ONLY"
    assert observations[3][2] == "ALLOW_EXACT_TRACE_ONLY"
    assert observations[4][2] == "IGNORE_AS_NONAUTHORITATIVE"
    assert observations[5][2] == "REQUIRE_PRODUCER_LANDING_AND_REVIEW"
    assert all(observations[index][2] != "ALLOW_EXACT_TRACE_ONLY" for index in (1, 2, 5, 6, 7, 8, 9))

    needless_refusal = dict(_trace_case_matrix()[3])
    needless_refusal["sibling_todo"] = True
    assert _trace_case_oracle(needless_refusal) == "IGNORE_AS_NONAUTHORITATIVE"
    safe_without_done = dict(_trace_case_matrix()[3])
    assert _trace_case_oracle(safe_without_done) == "ALLOW_EXACT_TRACE_ONLY"
    missing_exact_path = dict(_trace_case_matrix()[3])
    missing_exact_path["exact_path"] = False
    assert _trace_case_oracle(missing_exact_path) == "REJECT_UNRESOLVED_TRACE"
    unsafe_acceptance = dict(_trace_case_matrix()[7])
    unsafe_acceptance["mixed_hunks"] = False
    unsafe_acceptance["effect"] = "TRACE"
    unsafe_acceptance["selected"] = True
    assert _trace_case_oracle(unsafe_acceptance) == "ALLOW_EXACT_TRACE_ONLY"
    unsafe_acceptance["mixed_hunks"] = True
    assert _trace_case_oracle(unsafe_acceptance) == "REJECT_MIXED_EFFECT"
    unsafe_value = dict(_trace_case_matrix()[6])
    assert _trace_case_oracle(unsafe_value) == "REQUIRE_VALUE_LANDING"


def test_briefing_and_release_are_outcome_led_and_project_defined():
    briefing = _read(".tfw/templates/briefing.md")
    release = _read(".tfw/workflows/release.md")
    root_release = _read("RELEASE.md")
    for heading in ("## What happened", "## What is useful now", "## What changed or was preserved",
                    "## What remains and what to do next"):
        assert heading in briefing
    assert "No common route requires" in release
    assert "publication" in release
    assert "`.tfw/VERSION`" in root_release
    assert "`.tfw/CHANGELOG.md`" in root_release
    assert ".tfw/migrations/{major}.0.0.md" in root_release
    assert "`status.md`, task journals" in root_release
    assert "production state" in root_release


def test_untagged_candidate_provenance_rejects_old_tag_and_invented_release():
    """Source-derived counterexample: a new payload cannot retain or invent release provenance."""
    update = _read(".tfw/workflows/update.md")
    candidate_sha = "d6d26003972f7b18fe10d492960d0cbac9f0a3e8"
    untagged_rule = (
        "When an authorized untagged Candidate is applied, set `tfw.version` to the target's `.tfw/VERSION`\n"
        "and set `tfw.installed_from` to the configured upstream plus the verified full Candidate SHA (the\n"
        "actual source provenance). Record that the ref is an untagged Candidate in the receipt and outcome;\n"
        "this source provenance is not a release tag, and the update must never invent or claim\n"
        "`v{VERSION}`."
    )

    def provenance_ok(installed_from: str, source_sha: str, source_text: str) -> bool:
        pin_section, separator, _ = source_text.partition("## 1. Read the Target and Route Applicable History")
        return (
            bool(separator)
            and untagged_rule in pin_section
            and installed_from.endswith(f"@{source_sha}")
        )

    assert provenance_ok(f"trace-first-starter@{candidate_sha}", candidate_sha, update)
    assert not provenance_ok("trace-first-starter@v2.0.0", candidate_sha, update)
    assert not provenance_ok("https://github.com/saubakirov/trace-first-starter@v3.0.0", candidate_sha, update)

    stale_rule = "Keep `tfw.installed_from` at the last verified release even when the payload changed."
    mutated_update = update.replace(untagged_rule, stale_rule)
    mutated_update += f"\nHistorical Candidate reference: `{candidate_sha}`.\n"
    assert not provenance_ok("trace-first-starter@v2.0.0", candidate_sha, mutated_update)


def test_owner_language_loss_and_restoration_is_source_derived():
    """Source-derived counterexample: procedural wording cannot replace owner-facing benefit language."""
    baseline = subprocess.check_output(
        ["git", "show", "8fd8e40b734e9c439bb84721ef8bee441b9fcdd7:.tfw/templates/briefing.md"],
        text=True,
    )
    field_candidate = subprocess.check_output(
        ["git", "show", "d6d26003972f7b18fe10d492960d0cbac9f0a3e8:.tfw/templates/briefing.md"],
        text=True,
    )
    final = _read(".tfw/templates/briefing.md")
    assert "what it lets them do" in baseline
    assert "what the procedure calls it" in baseline
    assert "what it lets them do" not in field_candidate
    assert "what the procedure calls it" not in field_candidate
    assert "what the change lets them do" in final
    assert "agent's technique" in final


def test_selected_sibling_trace_has_exact_boundary_language():
    conventions = _read(".tfw/conventions.md")
    handoff = _read(".tfw/workflows/handoff.md")
    review = _read(".tfw/workflows/review.md")
    judge = _read(".tfw/templates/review/judge.md")
    for text in (conventions, handoff, review):
        assert "exact path" in text
        assert "producer task/phase" in text
        assert "sibling" in text and ("DONE" in text or "lifecycle state" in text)
    assert "legacy and historical citations" in judge
    assert "semantic effect" in judge
