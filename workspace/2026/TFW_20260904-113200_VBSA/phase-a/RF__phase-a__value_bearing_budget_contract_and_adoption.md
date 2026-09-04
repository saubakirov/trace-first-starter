# RF — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption

> **Date**: 2026-09-04
> **Author**: saubakirov via codex
> **Status**: 🟢 RF — Complete
> **Parent HL**: [Phase A HL](HL__phase-a__value_bearing_budget_contract_and_adoption.md)
> **TS**: [TS Phase A](TS__phase-a__value_bearing_budget_contract_and_adoption.md)

---

## 1. What Was Done

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | 36e50e4a362d474550f26e58defe56132b5417be |
| Baseline / Candidate | f5a96af07dcdc4230ecf31100bd155a3dca09604 / 6dce719338fece2601c1e1ce770273a1bb87c441 |
| VALUE membership | The exact 29 approved rows below; every actual action is M, class is VALUE, and reason is unchanged |
| Arithmetic | 634 additions + 318 deletions = 952 touched text LOC; 29 logical VALUE files; no binary/non-text N/A |
| Membership deviations | None; selector_equals_membership=true |
| Trigger disposition | Keep one phase: neither 50-file nor 5,000-LOC soft prompt is crossed; splitting the coupled canon/templates/copies/migration would risk contradictory behavior |
| Authority and timing | Immutable plan remains 29/1,100; actual 29/952 is below it and below 2× boundaries 58/2,200. No prospective growth ruling was needed. Owner approval is commit 36e50e4; dispatch is phase journal 20260904-211326. Tests passed before Candidate; EV/RF follow Candidate |
| Reproduction | Exact approved NUL-safe name-status and numstat commands are in the EV accounting section |

| Path | Action | Class | Approved semantic reason / actual result |
|---|---|---|---|
| .tfw/README.md | M | VALUE | Local accepted North Star gains the quotation at the ruled NS2 position |
| .tfw/conventions.md | M | VALUE | Canonical classification, accounting, authority, applicability, and M1–M6 contract |
| .tfw/glossary.md | M | VALUE | Stable router replaces the stale four-limit definition |
| .tfw/project_config.yaml | M | VALUE | Live project uses the exact three approved keys |
| .tfw/workflows/plan.md | M | VALUE | VALUE-only TS gate, soft triggers, bounded authority, and universal judgment |
| .tfw/workflows/handoff.md | M | VALUE | Prospective stop, tested Candidate fixation, and RF/EV binding |
| .tfw/workflows/review.md | M | VALUE | Independent replay, timing/authority judgment, and failure semantics |
| .tfw/workflows/config.md | M | VALUE | Three-key registry and deterministic legacy mapping |
| .tfw/workflows/update.md | M | VALUE | Atomic value preservation, approval epoch, and receiver North-Star preservation |
| .tfw/workflows/init.md | M | VALUE | Three-key setup and no foreign North-Star quotation injection |
| .tfw/templates/TS.md | M | VALUE | Prospective selector, denominator, triggers, M1–M6, rulings, and exact method |
| .tfw/templates/RF.md | M | VALUE | Actual approval/Candidate/membership/arithmetic/deviation/authority binding |
| .tfw/templates/REVIEW.md | M | VALUE | Independent accounting result and discrepancy/verdict carrier |
| .tfw/templates/evidence/EV.md | M | VALUE | Exactly one dedicated accounting row with reproduction and timing |
| .tfw/templates/project_config.yaml | M | VALUE | Exact 50/5000/2 starter defaults and project-owned annotation |
| .tfw/CHANGELOG.md | M | VALUE | Version-agnostic Unreleased behavior, mapping, compatibility, and user action |
| RELEASE.md | M | VALUE | Release-number ownership and selected-major migration gate |
| .agent/workflows/tfw-plan.md | M | VALUE | Exact canonical plan copy |
| .agent/workflows/tfw-handoff.md | M | VALUE | Exact canonical handoff copy |
| .agent/workflows/tfw-review.md | M | VALUE | Exact canonical review copy |
| .agent/workflows/tfw-config.md | M | VALUE | Exact canonical config copy |
| .agent/workflows/tfw-update.md | M | VALUE | Exact canonical update copy |
| .agent/workflows/tfw-init.md | M | VALUE | Exact canonical init copy |
| .claude/commands/tfw-plan.md | M | VALUE | Exact canonical plan copy |
| .claude/commands/tfw-handoff.md | M | VALUE | Exact canonical handoff copy |
| .claude/commands/tfw-review.md | M | VALUE | Exact canonical review copy |
| .claude/commands/tfw-config.md | M | VALUE | Exact canonical config copy |
| .claude/commands/tfw-update.md | M | VALUE | Exact canonical update copy |
| .claude/commands/tfw-init.md | M | VALUE | Exact canonical init copy |

Candidate contains two additional approved ASSURANCE paths:
docs/scripts/test_runtime_context.py and docs/scripts/test_integration.py. Candidate contains no TRACE,
DERIVED, added VALUE, or protected HC-1 path. The Baseline-to-Candidate TRACE set is limited to the exact
current-task selectors approved by the TS.

### New Files

No implementation files were created.

### Modified Files

All 29 VALUE and 2 ASSURANCE files in the approved selector were modified; no other implementation path
was touched. EV, this RF, phase status, and the final event are post-Candidate TRACE.

### 1.1 Round 1 return

This append-only round supersedes the initial Candidate only for current review:

| Fact | Round 1 actual |
|---|---|
| Return authority | Live REVIEW §8 at 5ab04d0e666ad38960229013a7ac649e693f3ca8; unchanged TS approval 36e50e4a362d474550f26e58defe56132b5417be |
| Baseline / Candidate | f5a96af07dcdc4230ecf31100bd155a3dca09604 / edb0017bd0c1d33eafbf99ee2b9c841e2fd91b2f |
| VALUE membership | Same exact 29 approved paths; all action M, class VALUE, and approved semantic reasons unchanged |
| Arithmetic | 657 additions + 318 deletions = 975 touched text LOC; 29 logical files; no binary N/A |
| Phase attribution | VALID — the whole delta belongs to Phase A |
| Deviations | None; selector_equals_membership=true |
| Trigger / authority | Keep one phase; 29/975 is below 50/5000 and below 58/2200. Immutable plan remains 29/1,100. Coordinator ruled all three repairs before work |
| Timing | Targeted/full tests passed before Candidate; round EV/RF/status/event follow it |

Candidate's own diff contains exactly 13 approved round paths: canonical conventions, plan/init/update,
their six tracked copies, the EV template, and two ASSURANCE files. No new carrier/path or HC-1 change
occurred.

### 1.2 Pass 2 return

| Fact | Pass 2 actual |
|---|---|
| Return authority | Live REVIEW §16 at baa0b7c8c6938d9131bcf5bb78efd6edfc3653bb; unchanged TS approval 36e50e4a362d474550f26e58defe56132b5417be |
| Baseline / Candidate | f5a96af07dcdc4230ecf31100bd155a3dca09604 / 59c73bf00b386d5221e9989da0df21a71af5c0b1 |
| VALUE membership | Same exact 29 approved paths; all action M, class VALUE, and approved semantic reasons unchanged |
| Arithmetic | 663 additions + 321 deletions = 984 touched text LOC; 29 logical files; no binary N/A |
| Phase attribution | VALID — the whole delta belongs to Phase A |
| Deviations | None; selector_equals_membership=true; protected HC-1 changes=0 |
| Trigger / authority | Keep one phase; 29/984 is below 50/5000 and below 58/2200. Immutable plan remains 29/1,100; §16 ruled R2-D1 before work |
| Timing | All targeted/full tests passed before Candidate; pass-2 EV/RF/status/event follow it |

Candidate's own diff contains four approved VALUE carriers and one approved ASSURANCE test. No new
path, carrier, manifest, ledger, script, migration, or HC-1 change occurred.

## 2. Key Decisions

1. The three configuration keys are decomposition_trigger_files, decomposition_trigger_loc, and
   owner_escalation_multiplier; CREATE/MODIFY/DELETE remain actions rather than measures.
2. D75 remains enforced: plan uses one uniquely addressed planner route, and init checks receiver
   North-Star existence/bytes without loading starter purpose. The runtime regression stays within all
   immutable context ceilings.
3. The changelog remains Unreleased and version-agnostic. Only /tfw-release chooses a version and must
   create the version-named migration guide before VERSION if it selects a major boundary.
4. Template explanations were reduced where canonical workflows/conventions already own semantics. This
   applied the Saint-Exupéry Principle without removing any required field, gate, or authority.

### 2.1 Round 1 return

1. Planner routing now loads three unique canonical conventions sections directly. Exact config ranges
   replace a whole-config read, retaining the immutable D75 ceiling without shadow authority.
2. Init/update expose explicit receiver operations. Tests parse and execute those operations against
   controlled receivers; preservation is behavior-derived rather than asserted in isolation.
3. EV Result cells admit only VERIFIED, DEFERRED, BLOCKED, and N/A. INVALID remains a phase-attribution
   detail and never becomes a fifth evidence status.

### 2.2 Pass 2 return

1. Cross-domain examples, test/conformance treatment, ambiguity precedence, whole-diff fallback,
   selector conditions, freehand prohibition, and the full non-damage boundary now live inside the three
   canonical ranges already loaded by `/tfw-plan`.
2. The assurance projection parses those live ranges and rejects output-changing permission,
   missing-example, and missing-rule mutants independently.
3. D75 was preserved by removing duplicated Step 7 enumeration and unneeded selected config comments;
   all config values and every rule remain available from their authorities.

## 3. Acceptance Criteria

- [x] AC-1 — one semantic VALUE budget subject and four exhaustive classes
- [x] AC-2 — fixed Baseline/Candidate/selector method, NUL safety, and exact phase attribution
- [x] AC-3 — exact three-key configuration and prospective forward migration
- [x] AC-4 — prospective bounded authority and local/universal Saint-Exupéry treatment
- [x] AC-5 — Executor fixes Candidate and RF/one EV row bind the same contract
- [x] AC-6 — Reviewer independently replays and adjudicates without repair
- [x] AC-7 — structural source-derived assurance and exact adapter parity
- [x] AC-8 — Phase A publishes and obeys its immutable accounting

### 3.1 Round 1 return

- [x] REVIEW finding 1 — canonical planner ranges load; meaning-reversing and missing-route mutants fail
- [x] REVIEW finding 2 — controlled receiver bytes are preserved; overwrite mutant changes output and fails
- [x] REVIEW finding 3 — four Result statuses remain exact; INVALID is accounting detail only

### 3.2 Pass 2 return

- [x] R2-D1 — every named classification example and ambiguity/selector rule is restored
- [x] R2-D1 — Saint-Exupéry protects purpose, value, correctness, architecture, modularity,
  inspectability, and continuation
- [x] R2-D1 — live-source projection changes before freehand, missing-example, and missing-rule rejection
- [x] R2-D1 — pass-1 receiver overwrite and four-status EV contracts remain green
- [x] R2-D1 — planner stays below 24,730 without raising the ceiling or removing another rule

## 4. Verification

- Targeted VBSA semantics: 20 passed
- Targeted accounting/Candidate/attribution: 6 passed
- Targeted config/migration/release/update/init: 9 passed
- Targeted authority/Saint/North-Star: 4 passed
- Targeted handoff/RF/EV: 2 passed
- Targeted review: 1 passed
- Runtime regression after D75 refinement: 149 passed
- Full tests: 553 passed, 1 skipped
- Project index: exit 0, project consistent with declared release
- git diff --check, YAML parse, Python compile, and byte-exact adapter checks: passed

### 4.1 Round 1 return

- Round VBSA/D75 target: 26 passed
- Controlled receiver/North-Star/adapter target: 10 passed
- Runtime suite: 154 passed
- Full suite: 559 passed, 1 skipped
- Planner active context: 24,729 ≤ immutable 24,730
- Project index, Python compile, diff whitespace, and changed-adapter byte parity: passed

### 4.2 Pass 2 return

- Round VBSA/D75 target: 29 passed
- Controlled receiver/North-Star/adapter target: 10 passed
- Runtime suite: 157 passed
- Tracked full suites: 562 passed, 1 skipped (306 docs plus 256 framework, 1 skipped)
- Generated site mirror regression: 306 passed
- Planner active context: 24,728 ≤ immutable 24,730
- Project structure, Python compile, diff whitespace, and changed-adapter byte parity: passed
- Task structure reproduced only the terminally ruled RDP 123/120 defect; it remains untouched
- Diagnostic root-wide pytest discovery was not a suite result because generated `site/scripts` mirrors
  tracked module names; the tracked suites above were run separately

## 5. Evidence

See [EV file](evidence/EV__phase-a__value_bearing_budget_contract_and_adoption.md) for evidence details.

Evidence verdict: 8/8 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

### 5.1 Round 1 return

See [EV file](evidence/EV__phase-a__value_bearing_budget_contract_and_adoption.md), Round 1 Return
Evidence, for adverse-mutant outputs and new Candidate accounting.

Round verdict: 3/3 returned findings VERIFIED; accounting VERIFIED; 0 DEFERRED, 0 BLOCKED, 0 N/A.

### 5.2 Pass 2 return

See [EV file](evidence/EV__phase-a__value_bearing_budget_contract_and_adoption.md), Pass 2 Return
Evidence, for projection/mutant output and the new Candidate accounting.

Pass-2 verdict: R2-D1 VERIFIED; accounting VERIFIED; 0 DEFERRED, 0 BLOCKED, 0 N/A.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md | summary | style | Immutable baseline summary is 123 code points against the current 120 ceiling; gen_index --check tasks reports it. HC-1 forbids repair in this phase |

### 6.1 Round 1 return

No new observations. The existing RDP 123/120 item was reproduced unchanged and follows the Coordinator's
terminal ruling: owed but forbidden to pay in this phase.

### 6.2 Pass 2 return

No new observations. The existing RDP 123/120 item was reproduced unchanged and remains forbidden to
repair in this phase.

## 7. Fact Candidates

No fact candidates.

### 7.1 Round 1 return

No fact candidates.

### 7.2 Pass 2 return

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

### 8.1 Round 1 return

No strategic insights.

### 8.2 Pass 2 return

No strategic insights.

## 9. Diagrams

    Approved TS at approval commit
              |
              v
    Baseline + literal VALUE selector
              |
       tested Candidate
          /         \
         v           v
    one EV row       RF binding
          \         /
              v
      independent /tfw-review

### 9.1 Round 1 return

    REVIEW §8 ruled return
             |
             v
    three bounded carrier repairs
             |
      tests + new Candidate
          /          \
         v            v
    one EV row    appended RF
          \          /
             v
       independent /tfw-review

### 9.2 Pass 2 return

    REVIEW §16: R2-D1
             |
             v
    three canonical live ranges
       /         |          \
      v          v           v
    examples  ambiguity  non-damage boundary
       \         |          /
        source-derived projection
                 |
        tests + Candidate
          /             \
         v               v
    one EV row       appended RF
          \             /
             /tfw-review

---

*RF — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption | 2026-09-04*
