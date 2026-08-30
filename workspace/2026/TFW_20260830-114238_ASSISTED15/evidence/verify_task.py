#!/usr/bin/env python3
"""Verify the amended no-code Assisted 1.5 product and current evidence."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True

REPO = Path(__file__).resolve().parents[4]
EVIDENCE = Path(__file__).resolve().parent
TASK = EVIDENCE.parent
PRODUCT = REPO / "editions"
ASSISTED = PRODUCT / "02-assisted"
BASELINE = "f3eb986"
PRODUCT_COMMIT = "e27024bb782e7d95e1ef82c9ff7a80c51e411cf0"


def sha_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load(name: str) -> dict:
    return json.loads((EVIDENCE / name).read_text(encoding="utf-8"))


def run(command: list[str], expected: int = 0) -> str:
    result = subprocess.run(
        command,
        cwd=REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        timeout=120,
    )
    if result.returncode != expected:
        raise AssertionError(f"command failed ({result.returncode}): {command!r}\n{result.stdout}")
    return result.stdout.rstrip()


def check(value: bool, label: str, messages: list[str]) -> None:
    if not value:
        raise AssertionError(label)
    messages.append(f"PASS {label}")


def product_manifest_rows() -> list[dict]:
    payload = [p for p in ASSISTED.rglob("*") if p.is_file()]
    payload += [PRODUCT / "ASSISTED_MAINTENANCE.md", PRODUCT / "README.md", PRODUCT / "maintenance/maintenance-policy.json"]
    return sorted(
        ({"path": p.relative_to(PRODUCT).as_posix(), "sha256": sha_file(p), "size": p.stat().st_size} for p in payload),
        key=lambda item: item["path"],
    )


def main() -> int:
    messages: list[str] = []
    fixtures = load("assisted15-fixture-results.json")
    boundary = load("boundary-summary.json")
    source = load("source-immutability.json")
    render = load("templates/render-summary.json")

    # AC-1: exact release boundary and no-code product.
    check((ASSISTED / "VERSION").read_bytes() == b"1.5\n", "AC1 exact VERSION bytes", messages)
    check(boundary["paths"] == 33 and boundary["new"] == 23 and boundary["modified"] == 7 and boundary["deleted"] == 3, "AC1 exact 33/23/7/3 census", messages)
    check(boundary["changed_loc"] == 1838 <= 2600, "AC1 1838 changed LOC within budget", messages)
    check(boundary["removed_runtime_paths_absent"], "AC1 removed identity and maintenance executables absent", messages)
    check(boundary["product_executables"] == ["editions/02-assisted/шаблоны/build_a4.py"], "AC1 sole product executable is artifact builder", messages)
    check(not boundary["builder_forbidden_tokens"], "AC1 builder contains no TFW mechanics tokens", messages)
    check(not boundary["clean_copy_initial_state"]["profiles"] and not boundary["clean_copy_initial_state"]["work_exists"] and boundary["clean_copy_initial_state"]["project_uninitialized"] and not boundary["clean_copy_initial_state"]["hidden_full_or_light"], "AC1 clean copy is uninitialized and standalone", messages)
    hook_paths = [ASSISTED / ".codex/hooks.json", ASSISTED / ".codex/hooks/tfw-hook.ps1", ASSISTED / ".codex/hooks/tfw-hook.sh"]
    check(not any(path.exists() for path in hook_paths), "AC1 exact retired hook paths absent", messages)

    # AC-2: prompt/file identity scenarios.
    identity = fixtures["identity"]
    check(identity["scenario_count"] == 10 and identity["contract_markers_present"] and identity["all_passed"], "AC2 ten closed identity scenarios pass", messages)
    check(all(item["only_approved_profile_changed"] and item["zero_write_when_negative"] for item in identity["scenarios"]), "AC2 only explicitly approved profile changes", messages)
    scenario_names = {item["name"] for item in identity["scenarios"]}
    check(scenario_names == {"zero-profiles", "one-profile", "multiple-profiles", "cyrillic-surname", "latin-surname", "missing-surname", "collision", "invalid-profile", "explicit-current-selection", "autonomous-no-human-role"}, "AC2 complete scenario name set", messages)

    # AC-3: lifecycle and role boundary.
    roles = fixtures["roles"]
    check(len(roles["cases"]) == 7 and roles["all_closed"], "AC3 seven deterministic role scenarios close with zero duplicates", messages)
    check(roles["actual_lineage"]["same_reviewer_pending_after_compaction"] and roles["actual_lineage"]["child_reports_only_to_coordinator"], "AC3 actual coordinator/executor/reviewer lineage retained", messages)
    skill_root = ASSISTED / ".agents/skills"
    for name in ("tfw-plan", "tfw-handoff", "tfw-review", "tfw-update", "tfw-identity"):
        check((skill_root / name / "SKILL.md").is_file() and (skill_root / name / "agents/openai.yaml").is_file(), f"AC3 skill and metadata pair {name}", messages)

    # AC-4: static manifest and policy.
    recorded = json.loads((PRODUCT / "maintenance/release-manifest.json").read_text(encoding="utf-8"))
    regenerated_one = product_manifest_rows()
    regenerated_two = product_manifest_rows()
    static = fixtures["static_manifest"]
    check(recorded["files"] == regenerated_one == regenerated_two and static["recorded_equal"] and static["two_run_equal"], "AC4 static manifest two-run and recorded equality", messages)
    check(static["row_count"] == 29 and static["self_excluded"] and static["policy_included"] and static["unique_paths"] and not static["invalid_paths"], "AC4 29 unique confined rows, self-excluded and policy-included", messages)
    policy = static["policy"]
    check(policy["release_version"] == "1.5" and policy["retired_known_stock"] == 3 and policy["target_only"] == "preserve" and policy["procedure"] == "agent-led-ordinary-file-operations", "AC4 declarative policy contract", messages)
    check(policy["authorities"] == ["customizable", "downstream", "public"], "AC4 authority classes", messages)

    # AC-5: forward clean/drifted file procedure.
    forward = fixtures["forward"]
    clean = forward["clean"]
    check(clean["result"]["state"] == "verified" and clean["version"] == "1.5" and not clean["unresolved"], "AC5 clean ordinary-file update reaches 1.5", messages)
    check(clean["protected_equal"] and not clean["public_mismatches"] and not clean["unexplained_changes"] and clean["next_source_manifest_equal"], "AC5 protected bytes and next-source authority", messages)
    check(forward["drifted"]["result"]["state"] == "blocked-drift" and forward["drifted"]["zero_update_writes"] and not forward["drifted"]["update_writes_after_detection"], "AC5 drift blocks with zero update writes", messages)

    # AC-6: reverse privacy and field immutability.
    reverse = fixtures["reverse"]
    check(reverse["candidate_root_outside_public"] and reverse["private_markers_absent"] and reverse["public_unchanged"], "AC6 reverse creates privacy-safe candidate without public mutation", messages)
    check(reverse["candidate"]["requires_independent_semantic_privacy_review"], "AC6 independent candidate review required", messages)
    check(source["row_count"] == 29 and source["canonical_pre_digest"] == source["canonical_post_digest"] == "3a1885c65b13388a51ddaa5b1454122876d4f17d268bc49f0f94f6bb2dbee96b", "AC6 field canonical pre/post equality", messages)
    check(source["python_powershell_row_set_equal"] and source["pre_post_rows_equal"] and source["writes"] == 0, "AC6 independent field row readers and zero writes", messages)

    # AC-7: artifact-only builder and retained blocked-network visual proof.
    template = fixtures["templates"]
    check(template["artifact_only_cli"] and all(item["two_run_equal"] and item["equals_retained_render_html"] for item in template["two_run"].values()), "AC7 artifact builder two-run equality and retained-render equality", messages)
    check(not template["retained_outputs_missing"] and not template["retained_output_signature_errors"], "AC7 every retained replacement resolves with correct signature", messages)
    check(template["all_previous_pages_and_captures_visually_inspected"] and render["visual_inspection"]["all_16_pages_inspected"] and render["visual_inspection"]["all_4_full_captures_inspected"], "AC7 all pages and full captures visually inspected", messages)
    check(render["blocked_network"]["valid_pdf_outputs"] and render["replacement_extensions_match_bytes"] and not render["visual_inspection"]["browser_header_or_absolute_local_url"] and not render["visual_inspection"]["stitch_overlap"], "AC7 blocked-network render integrity", messages)

    # AC-8: cross-file closure and neutrality.
    check(not boundary["removed_runtime_references"], "AC8 zero removed-runtime references", messages)
    check(not boundary["private_markers"], "AC8 zero field/private markers in product", messages)
    identity_text = (skill_root / "tfw-identity/SKILL.md").read_text(encoding="utf-8")
    update_text = (skill_root / "tfw-update/SKILL.md").read_text(encoding="utf-8")
    check("Markdown-процедура" in identity_text and "обычной файловой операцией" in identity_text, "AC8 identity wording agrees on prompt/file procedure", messages)
    check("Compare" in update_text and "Classify" in update_text and "Explicit gate" not in update_text and "один явный gate" in update_text and "обычными доступными файловыми средствами" in update_text, "AC8 update wording agrees on agent-led sequence", messages)
    changelog = (ASSISTED / "CHANGELOG.md").read_text(encoding="utf-8")
    check("[1.5] - Unreleased" in changelog and "[1.0]" in changelog and "SemVer" in changelog, "AC8 truthful version/changelog boundary", messages)

    # AC-9: evidence integrity and task schema.
    obsolete = [
        EVIDENCE / "identity-windows.json",
        EVIDENCE / "maintenance/forward-terminal.json",
        EVIDENCE / "maintenance/partial-terminal.json",
        EVIDENCE / "maintenance/recovery-terminal.json",
    ]
    check(all(path.exists() for path in obsolete), "AC9 superseded runtime attachments retained only as historical trace", messages)
    status = (TASK / "status.md").read_text(encoding="utf-8")
    onb = (TASK / "ONB__TFW_20260830-114238_ASSISTED15.md").read_text(encoding="utf-8")
    check("lifecycle: rf" in status.casefold() and "amendment a1 re-onboarding" in onb.casefold(), "AC9 task lifecycle and amendment onboarding trace", messages)
    check((TASK / "TS__TFW_20260830-114238_ASSISTED15.md").is_file() and (TASK / "HL-TFW_20260830-114238_ASSISTED15.md").is_file(), "AC9 frozen HL/TS resolve", messages)

    # AC-10: publication truth and deferred lifecycle leg.
    publication = boundary["publication"]
    check(publication["all_task_commits_zero_forbidden_hits"] and not publication["forbidden_hits"], "AC10 every post-baseline task commit has zero forbidden path hits", messages)
    check(publication["excluded_owner_config_baseline"]["commit"].startswith(BASELINE), "AC10 owner config commit classified as census baseline", messages)
    check(len(publication["external_tags"]) == 2 and all(item["unchanged"] for item in publication["external_tags"]), "AC10 both external local tags unchanged", messages)
    check(all(not item["contains_amended_product_commit"] for item in publication["external_tags"]), "AC10 external tags do not contain amended product checkpoint", messages)
    check(publication["assisted_task_tag_or_push_acts"] == 0 and publication["remote_containment_absent"], "AC10 zero task tag/push acts and no remote containment", messages)

    # Independent live checks, including task-scoped commit/path audit.
    check(run(["git", "diff", "--check", BASELINE, "--", "editions"]) == "", "LIVE product diff check", messages)
    check(run(["git", "rev-parse", PRODUCT_COMMIT]) == PRODUCT_COMMIT, "LIVE product checkpoint resolves", messages)
    check(run([sys.executable, "-B", str(ASSISTED / "шаблоны/build_a4.py"), "--self-test"], expected=2).find("unrecognized arguments: --self-test") >= 0, "LIVE removed builder self-test command rejects", messages)

    rf = (TASK / "RF__TFW_20260830-114238_ASSISTED15.md").read_text(encoding="utf-8")
    ev = (EVIDENCE / "EV__TFW_20260830-114238_ASSISTED15.md").read_text(encoding="utf-8")
    for number in range(1, 11):
        check(f"AC-{number}" in rf and f"AC-{number}" in ev, f"TRACE RF/EV contain AC-{number}", messages)
    check("SUPERSEDED" in rf and "SUPERSEDED" in ev and "DEFERRED" in rf and "DEFERRED" in ev, "TRACE supersession and deferred compaction/review are explicit", messages)
    check(not (EVIDENCE / "history-compaction-attestation.md").exists(), "TRACE compaction attachment correctly pending Coordinator", messages)

    messages.append("AMENDED_NO_CODE_FINAL=PASS")
    (EVIDENCE / "assisted15-verification.log").write_text("\n".join(messages) + "\n", encoding="utf-8", newline="\n")
    print("\n".join(messages))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        (EVIDENCE / "assisted15-verification.log").write_text(f"AMENDED_NO_CODE_FINAL=FAIL\n{type(exc).__name__}: {exc}\n", encoding="utf-8", newline="\n")
        raise
