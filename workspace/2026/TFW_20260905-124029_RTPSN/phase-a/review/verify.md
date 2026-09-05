# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 17 unique paths (11 new + 6 modified)
> Files to verify: ⌈17 × 0.42⌉ = 8; actual verification: all 17 claimed paths plus the omitted final transition event (18/18 actual approval-to-RF-head paths)

## Verification Log

### V1: `docs/scripts/command_entry_eval.py`
- **RF claim:** Explicit dry-run/run/summary/finalize-stop harness; live calls are never a default action.
- **Actual:** The no-subcommand path prints help and exits 0; `dry-run` only renders fixtures/schedule; only `run_matrix` reaches `codex exec`. Live argv includes `--ephemeral`, `--ignore-user-config`, `workspace-write`, pinned model/effort, `approval_policy="never"`, JSON output, and fixture `--cd`. Fixture creation and cleanup validate resolved paths outside the repository; raw output is redacted before evidence serialization.
- **Match:** ✅

### V2: `docs/scripts/test_command_entry_eval.py`
- **RF claim:** Offline fake-runner, arm, grader, budget, redaction, cleanup, statistics, decision, and STOP-finalization assurance.
- **Actual:** The file independently constructs command/message traces, covers every named family, rejects role/load/order/route and cleanup mutants, and never invokes the live runner. Independent execution: 31 passed in 44.63s.
- **Match:** ✅

### V3: `phase-a/ONB__phase-a__command_entry_reliability.md`
- **RF claim:** Executor onboarding, authority, scope, and prerequisite gate.
- **Actual:** Resolves approval `8866090960…`, AG authority, acting handle, immutable 25/800 denominator, three unconditional VALUE paths, conditional skill exclusion, and no blockers before implementation.
- **Match:** ✅

### V4: `phase-a/journal/20260905-180503__handoff__2718.md`
- **RF claim:** TS_DRAFT-to-ONB execution transition.
- **Actual:** Immutable event has the claimed transition, actor/via, TS/ONB refs, and matching timestamp/state history.
- **Match:** ✅

### V5: `phase-a/evidence/EV__phase-a__command_entry_reliability.md`
- **RF claim:** Structured AC and accounting verdict, 7/8 VERIFIED and AC-3 BLOCKED.
- **Actual:** Seven AC rows plus exactly one accounting row exist; E1/E2/E4–E7/accounting are VERIFIED and E3 is BLOCKED. Every attachment resolves.
- **Match:** ✅

### V6: `phase-a/evidence/command-entry-topology.txt`
- **RF claim:** Exact 11×4 census, revision comparison, evidence ladder, and incident boundary.
- **Actual:** 44 route rows; 11 commands, four adapters, declared/tracked/installed/clean/live states, immutable Baseline/Candidate, R0–R5 separation, H3 refutation, H4 inconclusive, and untested-host limits are explicit.
- **Match:** ✅

### V7: `phase-a/evidence/command-entry-trials.jsonl`
- **RF claim:** Seven completed raw attempts plus a terminal STOP record; one interrupted attempt has no invented telemetry.
- **Actual:** Nine parseable records: one `run_start`, seven valid attempt objects in the exact schedule prefix, and one `run_end`. Attempt usage sums to 702,852; events, hashes, grader results, CLI boundary, and empty diffs are retained. `run_end.coordinator_stop` records basis 2/162,311, projection 4,382,397, completed 7/702,852, and `unreported_interrupted_attempt=true`.
- **Match:** ✅

### V8: `phase-a/evidence/command-entry-summary.json`
- **RF claim:** Independent partial rates/intervals, usage, limitations, AC-3 BLOCKED, and baseline-retention decision.
- **Actual:** `summary --check` exits 0 and recomputes 7/54, 702,852, zero completed aggregate passes, empty decision comparisons, `production_skill_edits_authorized=false`, and `BASELINE RETAINED`. Partial Wilson/Newcombe intervals are reported without a superiority or causal conclusion.
- **Match:** ✅

### V9: `phase-a/evidence/command-entry-counts.txt`
- **RF claim:** Exact context and immutable VALUE/Candidate accounting.
- **Actual:** Independent Baseline→Candidate replay yields only the three approved unconditional VALUE files with 24+21+36 additions and zero deletions: 3 logical files, 81 touched text LOC, no binary rows, no conditional skill membership.
- **Match:** ✅

### V10: `phase-a/evidence/test-output.txt`
- **RF claim:** Environment, schedule, hashes, stop math, tests, consistency, parity, and cleanup output.
- **Actual:** Stored outputs match raw evidence and were independently reproduced for default/dry-run, harness, summary, project/tasks checks, targeted tests, full tests, parity, and temp residue.
- **Match:** ✅

### V11: `phase-a/RF__phase-a__command_entry_reliability.md`
- **RF claim:** Cumulative Executor result and scope/evidence summary.
- **Actual:** RF keeps AC-3 unchecked and BLOCKED, does not reduce the denominator, makes no comparative/causal claim, retains baseline, names the immutable Candidate, and reports exact usage/VALUE/test facts. Its new/modified-file tables omit the later final transition journal listed in V18.
- **Match:** ⚠️ partial — one permitted TRACE path omitted from the file inventory; substantive claims hold.

### V12: `.tfw/conventions.md`
- **RF claim:** Universal six-step command-entry sequence and R0–R5 ladder without a second workflow algorithm.
- **Actual:** Baseline→Candidate is 36 additions/0 deletions under `Tool Adapter Pattern`; the canonical workflow remains sole owner of effects/gates/stops and manifest remains tooling-only.
- **Match:** ✅

### V13: `.tfw/adapters/README.md`
- **RF claim:** Four-adapter entry contract and declared/tracked/installed/clean/live distinction.
- **Actual:** Baseline→Candidate is 24 additions/0 deletions and contains exactly those bounded distinctions with no route or manifest edit.
- **Match:** ✅

### V14: `.tfw/adapters/codex/README.md`
- **RF claim:** Thin production baseline and explicit static/live evaluation boundary.
- **Actual:** Baseline→Candidate is 21 additions/0 deletions; live harness is named non-default, higher-level claims require named host/model/effort/revision, and clean receiver is not relabelled live behavior.
- **Match:** ✅

### V15: `docs/scripts/test_runtime_context.py`
- **RF claim:** Source-derived entry projection and route/load/role/order/stop/parity/generated-input mutants.
- **Actual:** Candidate adds 141 lines implementing the projection and independent mutations; the independent targeted suite passes.
- **Match:** ✅

### V16: `docs/scripts/test_integration.py`
- **RF claim:** Exact 11×4 manifest/current/clean receiver and skill-contract parity gates.
- **Actual:** Candidate adds 82 lines checking exact topology, every Codex pair, four clean receivers, and independent boundary mutations; the independent targeted suite passes.
- **Match:** ✅

### V17: `phase-a/status.md`
- **RF claim:** Execution entered ONB and finished at RF.
- **Actual:** Current state is RF and its 18:05/19:18 journal events trace both transitions with matching refs.
- **Match:** ✅

### V18: `phase-a/journal/20260905-191857__transition__7fc0.md`
- **RF claim:** Not listed in RF's new-file inventory.
- **Actual:** RF-head commit creates this permitted TRACE event for ONB→RF; it resolves, matches `phase-a/status.md`, and does not touch Candidate or VALUE.
- **Match:** ⚠️ inventory omission only

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python docs/scripts/command_entry_eval.py` and `… dry-run` | exit 0; default help only; dry-run 54 schedule / 6 fixtures / 3 arms / max delta 15; zero temp residue and no live call |
| 2 | `python -m pytest docs/scripts/test_command_entry_eval.py -q` | 31 passed in 44.63s |
| 3 | `python docs/scripts/command_entry_eval.py summary --input …/command-entry-trials.jsonl --check` | exit 0; BLOCKED, 7/54, 702,852, BASELINE RETAINED, empty comparisons, skill edits unauthorized |
| 4 | `python -m pytest docs/scripts/test_integration.py docs/scripts/test_runtime_context.py docs/scripts/test_command_entry_eval.py -q` | 282 passed in 304.53s |
| 5 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | 612 passed, 1 skipped in 307.17s |
| 6 | `python .tfw/scripts/gen_index.py --check project` | exit 0; project consistent with release 2.1.0 |
| 7 | `python .tfw/scripts/gen_index.py --check tasks` | exit 1 only for the pre-existing RDP 123-code-point summary; RTPSN has no reported problem |
| 8 | Baseline/Candidate `git diff --name-status/--numstat --find-renames=50%` over the literal TS VALUE selector | 3 files; 24+21+36 additions, 0 deletions; 3/81 exact |
| 9 | Git protected-selector and Candidate→RF-head VALUE diffs | empty for workflows, manifest, both skill trees, Phase B, and later VALUE changes |
| 10 | SHA-256 comparison of all `.tfw/adapters/codex/skills/tfw-*` and `.agents/skills/tfw-*` pairs | 11 pairs, 0 mismatches; Baseline→Candidate skill diff empty |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | First two runs = 162,311; projection for 54 = 4,382,397; completed reported usage = 702,852 | RF §1; EV E3; topology; test output | Seven primary attempt `usage` objects plus `run_end.coordinator_stop`; independent arithmetic `162311×27` and seven-row sum | ✅ |
| C2 | Candidate is immutable first implementation commit and later TRACE/RF writes do not move it | RF accounting; EV accounting | Git chain `8866090960… → 33e829e… → 2bb5d62… → 0636bc80… → bc4ddf07… → f16ee242…`; Candidate commit contains only 3 VALUE + 4 ASSURANCE files | ✅ |
| C3 | VALUE = exactly 3 logical files / 81 additions / 0 deletions against immutable 25/800 | RF accounting; EV accounting; counts | Primary Baseline/Candidate Git objects and literal TS selector | ✅ |
| C4 | No statistical superiority or causal result is drawn from the incomplete denominator | RF §§1–3; EV E3/E4; summary decision | Raw 7-run prefix, summary `comparisons={}`, bounded prose, H4 inconclusive | ✅ |
| C5 | Approved reported-token ceiling and time ceiling were not exceeded | RF/EV stop claim; TS AC-3 | Completed reported tokens 702,852 < 750,000. Completed-attempt durations total 280.946s; run-start→STOP-finalization timestamps span 432.887s; both are below 10,800s. Interrupted-attempt actual/billed usage and its isolated duration are unavailable and are not invented. | ✅ with explicit telemetry boundary |

## Discrepancies Found

1. RF's `New Files` / `Modified Files` inventory omits `phase-a/journal/20260905-191857__transition__7fc0.md`, although the RF-head commit creates it. Verification was escalated to 100%. The event is a valid, discoverable TRACE write, matches the state transition, and changes neither Candidate nor VALUE; no TS AC or frozen HL claim requires an exhaustive RF path table, so the omission is non-material to acceptance.

Timing qualification, not a separate discrepancy: `command-entry-summary.json.elapsed_seconds=280.9464342999272` is the sum of completed-attempt durations, while raw timestamps span 432.886864 seconds through STOP finalization. `test-output.txt` labels the former correctly. Neither value approaches the 180-minute ceiling; the unreported interrupted attempt remains an explicit unknown and must not be converted into actual usage telemetry.

> On ANY discrepancy: verification escalated to 100%; all 18 actual approval-to-RF-head paths were checked.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `EV__phase-a__command_entry_reliability.md` | ✅ | ✅ — 7 VERIFIED + 1 BLOCKED rows, exact Candidate/accounting |
| E2 | `command-entry-topology.txt` | ✅ | ✅ — 44 route rows, revision/claim limits and hypothesis boundary |
| E3 | `command-entry-trials.jsonl` | ✅ | ✅ — 9 records, 7 completed attempts, exact STOP and telemetry |
| E4 | `command-entry-summary.json` | ✅ | ✅ — independently recomputes raw prefix and safe terminal decision |
| E5 | `command-entry-counts.txt` | ✅ | ✅ — context method, Candidate scope, and exact 3/81 VALUE replay |
| E6 | `test-output.txt` | ✅ | ✅ — independently reproduced gates; timing correctly qualified as completed-attempt sum |

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL K1 / ONB 1 | P0 `.tfw/README.md` NS1 | ✅ | ✅ | ✅ — durable purpose/authority/result/continuation | ✅ — task evidence enables continuation without chat reconstruction |
| 2 | HL K2 / ONB 2 | P1 Methodology Values + Success Criteria 1–4 | ✅ | ✅ | ✅ — structural enforcement, naming limit, portability, inspectable result | ✅ — tests and bounded claims implement those clauses |
| 3 | HL K3 / ONB 3 | P2 `knowledge/philosophy.md` F18 | ✅ | ✅ | ✅ — context-specific names cue context-specific behavior | ✅ — correctly marked N/A for Phase-A title wording while retained as task context |
| 4 | HL K4 / ONB 4 | P2 F38 + F45 | ✅ | ✅ | ✅ — finite coordination attention and subtraction/artifact budget | ✅ — baseline retention avoids unproved context growth |
| 5 | HL K5 / ONB 5 | P3 `KNOWLEDGE.md` D15 + D54 | ✅ | ✅ | ✅ — thin adapter/router, one source of truth, Codex first-class route | ✅ — current thin Codex topology is preserved and tested |
| 6 | HL K6 / ONB 6 | P3 D73–D75 | ✅ | ✅ | ✅ — workflow-owned selective reads, four-adapter/11-route topology, source-derived proof | ✅ — Candidate adds no preload or second authority |
| 7 | HL K7 / ONB 7 | P4 `conventions.md` Tool Adapter Pattern + Role Lock Protocol | ✅ | ✅ | ✅ — whole copy/router forms and workflow-bound role/effects | ✅ — universal entry sequence stays within those owners |
| 8 | HL K8 / ONB 8 | P5 `knowledge/convention.md` F4 + F19 | ✅ | ✅ | ✅ — ref-inside-step and consistent naming | ✅ — entry is step-shaped and route wording stays consistent |
| 9 | HL K9 / ONB 9 | P6 `knowledge/process.md` F3, F4, F7, F27, F30, F43 | ✅ | ✅ | ✅ — precise cues, gates, durable cross-session trace, enforcement, local rationale | ✅ — fixtures/evidence target the cited operational boundary |
| 10 | HL K10 / ONB 10 | Iteration 1 RES D1–D8 | ✅ | ✅ | ✅ — H3 refuted, H4 inconclusive, thin baseline least-regret | ✅ — Phase-A decision preserves rather than upgrades those findings |
| 11 | HL K11 / ONB 11 | Iteration 2 RES D1–D10 | ✅ | ✅ | ✅ — naming design belongs to Phase B and retains thin entry baseline | ✅ — Candidate leaves all naming/session behavior untouched |
| 12 | Phase HL / ONB additional scan | P0 root `README.md` How It Works; P2 F4/F24/F32/F43; P5 F5; P6 F37; P7 constraint F2/F12 and risk F1 | ✅ | ✅ | ✅ — inspectability, structural gates, one workflow source, revision-bound measures, prompt/repository/index constraints | ✅ — evidence, context accounting, and explicit-path commit boundary match the applications |

All 11 local Markdown links in master HL §7.2 resolve, including `#ns1` and `#methodology-values`. The 22 numbered HL/ONB citation applications and six additional ONB source groups were semantically checked: 28 resolved, 28 semantically verified, 0 irrelevant, 0 hallucinated.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈17 × 0.42⌉ files and recorded findings? (18/18 actual paths)
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Claim & Source Checks filled — key claims checked against primary raw/Git sources and every citation traced?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — no contradiction with D15, D54, D73–D76 or other P3 decisions?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 28 applications/source groups, resolved: 28, semantically verified: 28, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 6, verified: 6, missing: 0

Stage complete: YES
