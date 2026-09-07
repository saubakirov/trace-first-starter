"""Focused assurance for the clear update/release/briefing experience."""
from __future__ import annotations

import hashlib
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
        "purpose_preserved": "Existing `.tfw/README.md`" in update_text and "PRESERVE_BYTES" in update_text,
        "framework_readme_installed": "framework-owned" in update_text and "installed replacement" in update_text,
        "starter_not_injected": "DO_NOT_INJECT" in update_text,
        "collision_stops": "collision with different bytes stops" in update_text,
        "state_excluded": "project state — never overwrite" in update_text,
        "purpose_designation_recorded": "observed explicit purpose designation" in receipt_template,
        "receipt_schema": all(marker in receipt_template for marker in (
            "Decision and effects", "Preserved", "Skipped", "Verification")),
    }


def _apply_receiver_fixture(root: Path, policy: dict[str, bool], *, collision: bool = False) -> dict[str, object]:
    receiver = root / "receiver"
    target = root / "target"
    (receiver / ".tfw").mkdir(parents=True)
    (target / ".tfw").mkdir(parents=True)
    (receiver / "README.md").write_bytes(b"receiver root purpose")
    (receiver / ".tfw/README.md").write_bytes(b"custom receiver north star")
    (receiver / ".tfw/knowledge_state.yaml").write_bytes(b"project state")
    (receiver / ".tfw/project_config.yaml").write_bytes(b"project-owned config")
    (receiver / "workspace/task-history/status.md").parent.mkdir(parents=True)
    (receiver / "workspace/task-history/status.md").write_bytes(b"task history")
    (target / ".tfw/README.md").write_bytes(b"framework source")
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
        "root_preserved", "purpose_preserved", "framework_readme_installed",
        "starter_not_injected", "state_excluded", "purpose_designation_recorded",
        "receipt_schema",
    )
    if not all(policy[key] for key in required_policy):
        return {"decision": "REFUSED_POLICY"}
    if collision and policy["collision_stops"]:
        return {"decision": "BLOCKED_COLLISION"}
    if collision:
        return {"decision": "UNSAFE_COLLISION_ACCEPTED"}
    if policy["purpose_preserved"]:
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


def _trace_projection(conventions: str, handoff: str, review: str) -> str:
    required = ("exact path", "producer task/phase", "semantic effect")
    if not all(term in conventions and term in handoff and term in review for term in required):
        return "REJECT"
    if "selected stable uncommitted sibling trace" not in conventions:
        return "REJECT"
    return "ALLOW_EXACT_TRACE_ONLY"


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
    assert policy["purpose_preserved"] and policy["starter_not_injected"]
    assert policy["framework_readme_installed"] and policy["purpose_designation_recorded"]
    assert Path(clean["attachment"]).parent.name == clean["preserved_sha"]
    assert Path(clean["attachment"]).read_bytes() == b"custom receiver north star"
    assert Path(clean["receipt"]).is_file()
    receipt = Path(clean["receipt"]).read_text(encoding="utf-8")
    assert f"source_sha: {hashlib.sha256(b'framework source').hexdigest()}" in receipt
    assert "original_path: .tfw/README.md" in receipt
    assert "purpose_designation: project-purpose-bearing" in receipt
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
        "For a self-hosting payload",
    )
    assert all(family in release for family in release_families)
    assert "ordinary task completion remains valid" in release
    reordered = release.replace("3. verify the final composition", "3. commit the exact checked result", 1)
    reordered = reordered.replace("4. commit the exact checked result", "4. verify the final composition", 1)
    assert _release_order_from_source(reordered) is None
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
    assert "task `status.md`" in root_release
    assert "production state" in root_release


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
