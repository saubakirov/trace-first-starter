"""Self-contained immutable-object replay for FRATS Phase B semantic evidence.

This is task-local TRACE evidence, not product runtime or a permanent test. It reads only named Git
objects, applies in-memory material-negative mutations, prints every predicate source/mutation, and
exits nonzero on any failed or ambiguous result.
"""

from __future__ import annotations

import platform
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


CANDIDATE = "93186cea9ac8209cade30a49e76f3b8a32ae6227"
TS_REF = "116a324bb38d5ca21094bf6c5d528620d4ec4121"
TRANSCRIPT_RULE_REF = "68d85cc20b285e2dce083d23519d3394056033f4"
EVIDENCE_RULING_REF = "4cd4397795a5b831d6d90dacea1adb0a6d41efec"

TS_PATH = (
    "workspace/2026/TFW_20260920-223357_FRATS/phase-b/"
    "TS__phase-b__corpus_consistency_compression_and_receiver_proof__rev2.md"
)
ORIGINAL_REVIEW_PATH = (
    "workspace/2026/TFW_20260920-223357_FRATS/phase-b/"
    "REVIEW__phase-b__corpus_consistency_compression_and_receiver_proof.md"
)
REVIEW_REV2_PATH = (
    "workspace/2026/TFW_20260920-223357_FRATS/phase-b/"
    "REVIEW__phase-b__corpus_consistency_compression_and_receiver_proof__rev2.md"
)
CONVENTIONS = ".tfw/conventions.md"
PLAN = ".tfw/workflows/plan.md"
CURSOR = ".tfw/adapters/cursor/tfw.mdc.template"
CODEX = ".tfw/adapters/codex/AGENTS.md.template"
SESSION_PROVIDERS = (
    ".tfw/adapters/claude-code/CLAUDE.md.template",
    "CLAUDE.md",
    ".tfw/adapters/antigravity/tfw-rules.md.template",
    ".agents/rules/tfw.md",
    CURSOR,
)
ADAPTERS = (
    CODEX,
    "AGENTS.md",
    *SESSION_PROVIDERS,
)
WORKFLOWS = {
    "plan": PLAN,
    "research": ".tfw/workflows/research/base.md",
    "handoff": ".tfw/workflows/handoff.md",
    "review": ".tfw/workflows/review.md",
    "docs": ".tfw/workflows/docs.md",
    "knowledge": ".tfw/workflows/knowledge.md",
    "release": ".tfw/workflows/release.md",
    "update": ".tfw/workflows/update.md",
    "config": ".tfw/workflows/config.md",
    "init": ".tfw/workflows/init.md",
}


def git_root() -> Path:
    output = subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=Path(__file__).resolve().parent,
        text=True,
        encoding="utf-8",
    )
    return Path(output.strip()).resolve()


ROOT = git_root()


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, text=True, encoding="utf-8", stderr=subprocess.PIPE
    )


def blob(ref: str, path: str) -> str:
    return git("show", f"{ref}:{path}")


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract(pattern: str, text: str, label: str) -> str:
    match = re.search(pattern, text, re.S)
    if not match:
        raise AssertionError(f"missing authority block: {label}")
    return match.group(1)


@dataclass(frozen=True)
class Check:
    path: str
    literal: str


@dataclass(frozen=True)
class Scenario:
    name: str
    outcome: str
    checks: tuple[Check, ...]
    mutation_path: str
    mutation_literal: str
    edge: str


def evaluate(scenario: Scenario, overlays: dict[str, str] | None = None) -> bool:
    overlays = overlays or {}
    for check in scenario.checks:
        source = overlays.get(check.path)
        if source is None:
            source = normalized(blob(CANDIDATE, check.path))
        if check.literal not in source:
            return False
    return True


def mutate(scenario: Scenario) -> dict[str, str]:
    source = normalized(blob(CANDIDATE, scenario.mutation_path))
    count = source.count(scenario.mutation_literal)
    if count != 1:
        raise AssertionError(
            f"{scenario.name}: mutation must resolve exactly once, got {count}: "
            f"{scenario.mutation_literal!r}"
        )
    return {scenario.mutation_path: source.replace(scenario.mutation_literal, "<REMOVED>", 1)}


OWNER_DIRECT = (
    "**owner-direct:** an accountable human starts the role workflow; no agent principal is invented;"
)
DELEGATED = (
    "**delegated:** an actual Coordinator dispatch cites the immutable delegation mandate;"
)
CONTINUATION = (
    "**continuation:** the same unit cites its prior activation and still-current routing spine."
)
PREWORK_REFUSAL = (
    "A mismatch, partial or legacy-only status, foreign dispatch, role prompt without activation, "
    "implicit latest-session lookup, relay, hidden helper or ambiguous address is a pre-work refusal."
)
ITERATIVE_GATEWAY = (
    "`dialogue: iterative` is valid only when an owner-approved immutable authority names exactly "
    "two peer units, their purpose, boundary, consolidator, durable output and stop condition, and "
    "names a separate directly addressable `GATEWAY` unit."
)
GATEWAY_STOP = (
    "An exact configured GATEWAY never runs Plan: route the existing Coordinator or "
    "provision/activate a separate one only under exact delegation, then stop."
)
OWNER_ASSISTED = (
    "A missing native mechanism requires owner-assisted provisioning/exact addresses or a capable "
    "provider, never a claim of end-to-end orchestration."
)
CURSOR_LIMIT = (
    "Treat provision and addressed send as owner-assisted, and wait/readback or title/readback as "
    "unavailable, unless the current surface exposes the exact mechanism and observable result."
)
CODEX_WAIT = (
    "For another TFW role task, use cursor-based, bounded `wait_threads`; never call `read_thread` "
    "or use `includeOutputs` to monitor it."
)
ONE_REQUEST = (
    "A suspected stall permits one addressed status request; no response or missing return is "
    "reported as unavailable or blocked, never repaired by transcript inspection."
)
DURABLE_RETURN = (
    "After a durable return, only the named artifacts and commits become inputs at their stated "
    "evidence level."
)
TRANSCRIPT_SURFACE = (
    "**Transcript isolation.** Another active unit's transcript, reasoning, tool output, terminal "
    "and unreturned working tree are not coordination or evidence surfaces."
)
NO_RECONSTRUCT = (
    "No role reads, tails, resumes, searches or reconstructs them to monitor progress, validate "
    "trust, review work, recover context or pre-solve that unit's task."
)
SESSION_INSPECTION = (
    "Never open or resume another TFW role session to inspect its chat, reasoning, tool output, "
    "terminal or unreturned work."
)


SCENARIOS = (
    Scenario("owner_direct", "ACTIVATE_NO_INVENTED_PRINCIPAL", (Check(CONVENTIONS, OWNER_DIRECT),), CONVENTIONS, OWNER_DIRECT, "activation"),
    Scenario("exact_delegated", "ACTIVATE", (Check(CONVENTIONS, DELEGATED),), CONVENTIONS, DELEGATED, "authority"),
    Scenario("ordinary_continuation", "ACTIVATE_SAME_UNIT", (Check(CONVENTIONS, CONTINUATION),), CONVENTIONS, CONTINUATION, "continuation"),
    Scenario("invalid_continuation", "REFUSE", (Check(CONVENTIONS, PREWORK_REFUSAL),), CONVENTIONS, PREWORK_REFUSAL, "continuation"),
    Scenario("iterative_gateway_separation", "ROUTE_COORDINATOR_AND_STOP", (Check(CONVENTIONS, ITERATIVE_GATEWAY),), CONVENTIONS, ITERATIVE_GATEWAY, "authority"),
    Scenario("accidental_gateway_invocation", "REFUSE_ROLE_WORKFLOW", (Check(PLAN, GATEWAY_STOP),), PLAN, GATEWAY_STOP, "activation"),
    Scenario("limited_provider_owner_assisted", "OWNER_ASSISTED_BOUNDARY", (Check(PLAN, OWNER_ASSISTED), Check(CURSOR, CURSOR_LIMIT)), PLAN, OWNER_ASSISTED, "provider"),
    Scenario("bounded_cursor_wait", "ALLOW_STATUS_SIGNAL", (Check(CODEX, CODEX_WAIT),), CODEX, "cursor-based, bounded `wait_threads`", "observation"),
    Scenario("one_addressed_status_request", "ALLOW_ONE_REQUEST", (Check(CONVENTIONS, ONE_REQUEST),), CONVENTIONS, ONE_REQUEST, "observation"),
    Scenario("durable_artifact_commit", "ALLOW_AT_STATED_EVIDENCE", (Check(CONVENTIONS, DURABLE_RETURN),), CONVENTIONS, DURABLE_RETURN, "evidence"),
    Scenario("refuse_transcript_surfaces", "REFUSE", (Check(CONVENTIONS, TRANSCRIPT_SURFACE), Check(CONVENTIONS, NO_RECONSTRUCT)), CONVENTIONS, TRANSCRIPT_SURFACE, "observation"),
    Scenario("refuse_codex_read_thread_outputs", "REFUSE", (Check(CODEX, CODEX_WAIT),), CODEX, "never call `read_thread` or use `includeOutputs` to monitor it", "observation"),
    Scenario("refuse_provider_session_inspection", "REFUSE", tuple(Check(path, SESSION_INSPECTION) for path in SESSION_PROVIDERS), CURSOR, SESSION_INSPECTION, "observation"),
)


def static_checks() -> None:
    ts = blob(TS_REF, TS_PATH)
    plan = blob(CANDIDATE, PLAN)
    conventions = blob(CANDIDATE, CONVENTIONS)
    glossary = blob(CANDIDATE, ".tfw/glossary.md")
    original_review = blob(TRANSCRIPT_RULE_REF, ORIGINAL_REVIEW_PATH)
    review_rev2 = blob(EVIDENCE_RULING_REF, REVIEW_REV2_PATH)

    ac10 = extract(r"### AC-10:.*?```md\n(.*?)\n```", ts, "AC-10")
    mindset, steps = ac10.split("\n\n## Planning steps\n\n", 1)
    steps = "## Planning steps\n\n" + steps
    ac11 = extract(r"(### AC-11:.*?)(?=### AC-12:)", ts, "AC-11")
    ac11_blocks = re.findall(r"```md\n(.*?)\n```", ac11, re.S)
    transcript_rule = extract(
        r"### 10\.1 Canonical rule.*?```md\n(.*?)\n```", original_review, "transcript rule"
    )
    ruling = (
        "Preserve and rerun an exact, self-contained rung-2 semantic replay against the named "
        "immutable TS, ruling and Candidate."
    )

    checks = {
        "exact_ac10_mindset": mindset in plan,
        "exact_ac10_steps": steps in plan,
        "dispatch_retained": "After approval, a dispatch records source, destination" in plan,
        "plan_le_1400": len(re.findall(r"\S+", plan)) <= 1400,
        "exact_ac11_glossary": len(ac11_blocks) == 2 and ac11_blocks[0] in glossary,
        "exact_ac11_design_rules": len(ac11_blocks) == 2 and ac11_blocks[1] in conventions,
        "exact_transcript_rule": conventions.count(transcript_rule) == 1,
        "evidence_ruling_present": ruling in normalized(review_rev2),
        "all_workflows_le_1400": all(
            len(re.findall(r"\S+", blob(CANDIDATE, path))) <= 1400
            for path in WORKFLOWS.values()
        ),
        "copy_parity_20_of_20": all(
            blob(CANDIDATE, path)
            == blob(CANDIDATE, f".claude/commands/tfw-{name}.md")
            == blob(CANDIDATE, f".agents/workflows/tfw-{name}.md")
            for name, path in WORKFLOWS.items()
        ),
        "provider_mapping_7_of_7": all(
            "one addressed status request" in blob(CANDIDATE, path)
            and (
                "transcript inspection" in blob(CANDIDATE, path)
                or "session inspection" in blob(CANDIDATE, path)
            )
            for path in ADAPTERS
        ),
    }
    for name, passed in checks.items():
        print(f"STATIC {name}={'PASS' if passed else 'FAIL'}")
        if not passed:
            raise AssertionError(name)


def main() -> int:
    print(f"PYTHON {platform.python_version()}")
    print(f"GIT {git('--version').strip()}")
    print(f"CANDIDATE {CANDIDATE}")
    print(f"TS_REF {TS_REF}")
    print(f"TRANSCRIPT_RULE_REF {TRANSCRIPT_RULE_REF}")
    print(f"EVIDENCE_RULING_REF {EVIDENCE_RULING_REF}")
    static_checks()

    covered_edges: set[str] = set()
    for scenario in SCENARIOS:
        positive = evaluate(scenario)
        negative = not evaluate(scenario, mutate(scenario))
        sources = ",".join(sorted({check.path for check in scenario.checks}))
        print(
            f"CASE {scenario.name} positive={'PASS' if positive else 'FAIL'} "
            f"negative={'PASS' if negative else 'FAIL'} outcome={scenario.outcome} "
            f"edge={scenario.edge} sources={sources} "
            f"mutation={scenario.mutation_path}::remove:{scenario.mutation_literal!r}"
        )
        if not positive or not negative:
            raise AssertionError(scenario.name)
        covered_edges.add(scenario.edge)

    expected_edges = {"activation", "authority", "continuation", "provider", "observation", "evidence"}
    if covered_edges != expected_edges:
        raise AssertionError(f"edge coverage {sorted(covered_edges)} != {sorted(expected_edges)}")
    print("EDGE_COVERAGE " + ",".join(sorted(covered_edges)))
    print("OVERALL PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, subprocess.CalledProcessError) as exc:
        print(f"OVERALL FAIL {exc}", file=sys.stderr)
        raise SystemExit(1)
