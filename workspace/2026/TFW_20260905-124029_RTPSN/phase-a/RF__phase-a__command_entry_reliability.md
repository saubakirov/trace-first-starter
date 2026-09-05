# RF — TFW_20260905-124029_RTPSN / Phase A: Command Entry Reliability

> **Date**: 2026-09-05
> **Author**: saubakirov (Executor, via Codex)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW_20260905-124029_RTPSN](../HL-TFW_20260905-124029_RTPSN.md)
> **TS**: [TS Phase A](TS__phase-a__command_entry_reliability.md)

---

## 1. What Was Done

Phase A added one universal command-entry contract and a six-level evidence ladder to the
framework and adapter documentation. It also added an explicit, non-default evaluation
harness with disposable Git fixtures, fixed arm/fixture scheduling, independent event/diff
graders, budget enforcement, redaction, retained invalid attempts, confidence intervals,
independent summary recomputation, and offline mutant coverage.

The approved live matrix started with the exact 54-run denominator and limits. The Coordinator
stopped further live calls when the first two valid runs used 162,311 reported tokens, whose
exact linear projection for 54 was 4,382,397 tokens against the approved 750,000 ceiling.
Seven runs completed before the stop reached the running process, reporting 702,852 tokens;
one interrupted eighth attempt emitted no completed telemetry. The denominator was not
reduced or substituted. AC-3 is `BLOCKED`, H4 remains inconclusive, and the terminal production
result is `BASELINE RETAINED`. No production skill was edited.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `8866090960cb403e5254bf017bb2423b8171b0f2` |
| Baseline / Candidate | `7bc0f30736ff1456c5d9dd74286a4e3a94c63361` / `0636bc80da74ed686a01bdbe514c6a9921997d52` |
| VALUE membership | `M .tfw/conventions.md` — universal six-step entry sequence/evidence ladder; `M .tfw/adapters/README.md` — four-adapter contract and declared/tracked/installed/clean/live distinction; `M .tfw/adapters/codex/README.md` — thin-baseline and explicit live-evaluation boundary. All are Phase-A VALUE. |
| Arithmetic | 81 additions + 0 deletions = 81 touched text LOC; 3 logical files; binary/non-text N/A |
| Membership deviations | None. The approved prospective baseline-retained branch contains only the three unconditional VALUE files; the conditional 22 production skill paths are correctly absent. |
| Trigger disposition | Cause: AC-3 blocked under the approved ceiling. Cost: 3 VALUE files/81 touched LOC. Assurance: 2 created + 2 modified test/harness files and TRACE evidence. Split: none required. Authority: owner-approved TS. Terminal verdict: `BASELINE RETAINED`. Both configured prompts remain below threshold (3<50 files; 81<5,000 LOC). |
| Authority and timing | Immutable denominator 25 VALUE files / 800 LOC was approved prospectively at `8866090960cb403e5254bf017bb2423b8171b0f2` and never ratcheted. Actual 3/81 is below the Coordinator multiplier boundary of 50 files/1,600 LOC. Approval precedes ONB, implementation, Candidate, tests, and evidence. |
| Reproduction | Unchanged TS §4 NUL-safe `git diff --name-status --find-renames=50% -z` and `git diff --numstat --find-renames=50% -z` from full Baseline to full Candidate over the approved selector; exact command/output is in `evidence/command-entry-counts.txt`. |

This reports the approved contract; it does not create a selector, move Candidate, ratchet the
denominator, or supply late authority.

### New Files

| File | Description |
|---|---|
| `docs/scripts/command_entry_eval.py` | Explicit dry-run/run/summary/finalize-stop harness; live calls are never a default test action. |
| `docs/scripts/test_command_entry_eval.py` | Fake-runner, arm, grader, budget, redaction, cleanup, statistics, decision, and STOP-finalization tests. |
| `phase-a/ONB__phase-a__command_entry_reliability.md` | Executor onboarding, authority, scope, and prerequisite gate. |
| `phase-a/journal/20260905-180503__handoff__2718.md` | TS_DRAFT-to-ONB execution transition. |
| `phase-a/evidence/EV__phase-a__command_entry_reliability.md` | Structured AC and accounting verdict. |
| `phase-a/evidence/command-entry-topology.txt` | Exact 11×4 census, revision comparison, evidence ladder, and incident classification. |
| `phase-a/evidence/command-entry-trials.jsonl` | Seven completed redacted raw live attempts plus explicit STOP record. |
| `phase-a/evidence/command-entry-summary.json` | Independent rates, intervals, usage, limitations, AC-3 status, and production decision. |
| `phase-a/evidence/command-entry-counts.txt` | Per-command/design context estimates and exact VALUE/Candidate accounting. |
| `phase-a/evidence/test-output.txt` | Environment, schedule, hashes, live-stop math, tests, consistency, parity, and cleanup results. |
| `phase-a/RF__phase-a__command_entry_reliability.md` | This cumulative Executor result. |

### Modified Files

| File | Changes |
|---|---|
| `.tfw/conventions.md` | Owns the universal six-step command-entry sequence and R0–R5 evidence ladder without duplicating a workflow algorithm. |
| `.tfw/adapters/README.md` | Documents the shared adapter entry contract and separates declared, tracked, installed, clean, and live evidence. |
| `.tfw/adapters/codex/README.md` | Documents the thin baseline and bounded static/live evaluation claims. |
| `docs/scripts/test_runtime_context.py` | Adds source-derived all-command entry projection and independent route/load/role/order/stop/parity/generated-evidence mutants. |
| `docs/scripts/test_integration.py` | Adds exact 11×4 manifest, current receiver, clean-receiver, thin/full-copy, and mutation gates. |
| `phase-a/status.md` | Entered ONB after onboarding; transitions to RF with this result. |

### Execution Deviations and Residual Risks

- The approved 54-valid-run matrix did not complete. This is a declared terminal `BLOCKED`
  result under AC-3, not a denominator change or scope deviation.
- Stop delivery overlapped a live invocation: seven valid runs completed although the decision
  basis used the first two. The eighth interrupted attempt has no invented usage value.
- All completed attempts cover only the Coordinator new-task fixture. Executor, Reviewer,
  Researcher, resume, and ambiguity fixtures have no Phase-A controlled behavioral sample.
- The CLI JSON stream exposed agent messages but no observable command-execution events for
  the attempted skill/workflow reads. Invocation/load/order graders therefore failed closed;
  model self-report was not accepted as evidence.
- Partial rates and intervals do not establish comparative effect. H4 remains inconclusive;
  baseline retention is a safe default, not architectural superiority.
- Cursor, declared plural Antigravity, and non-Codex live hosts remain unobserved. Clean-receiver
  success is reported only as structural evidence.
- Phase-B naming/session behavior, CRATM orchestration, canonical workflows, manifest routes,
  and all 22 production skill source/install paths remain untouched.

## 2. Key Decisions

1. Retain the current thin proxy as production because AC-3 is blocked and the predeclared
   comparison rule cannot be applied; make no superiority claim.
2. Preserve the six evidence levels as non-substitutable: source presence, receiver parity,
   invocation, complete load, later conformance, and controlled comparative effect.
3. Ship only the three unconditional documentation VALUE changes and four ASSURANCE changes.
   Do not activate the conditional 22-skill branch.
4. Preserve all seven completed attempts, exact telemetry, stop basis, projection, and the
   unreported interrupted attempt instead of rewriting history to the first two runs.
5. Keep full-copy/direct production migration outside this TS. Any future production change
   requires a new approved specification and a feasible evidence design.

## 3. Acceptance Criteria

- [x] AC-1 — exact 11×4 census, revision/context comparison, causal boundary, evidence ladder,
  and live/absent-host limits are reproducible.
- [x] AC-2 — explicit safe harness, fixed arms/fixtures, event/diff graders, budgets, redaction,
  independent summary, fake runner, and mutants are implemented and tested.
- [ ] AC-3 — `BLOCKED`: 7/54 valid runs completed; the approved denominator is infeasible under
  the approved 750,000-token ceiling on the observed model/effort/host.
- [x] AC-4 — exactly one safe terminal production result is recorded: `BASELINE RETAINED`;
  comparative selection was not applied and production skill edits are unauthorized.
- [x] AC-5 — one universal pre-action contract is documented/tested without a second algorithm,
  manifest runtime authority, generated evidence input, or protected Phase-B/workflow changes.
- [x] AC-6 — exact topology, per-command context, clean receiver, parity, targeted/full test,
  project consistency, immutable Candidate, scope, and NUL-safe accounting gates pass.
- [x] AC-7 — EV and all raw/supporting evidence resolve locally with bounded claims; H3 remains
  refuted and H4 remains inconclusive.

## 4. Verification

- Lint (`python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`): 613 tests collected in 0.22s; exit 0.
- Tests (`python -m pytest .tfw/scripts/ docs/scripts/ -q`): 612 passed, 1 skipped in 296.01s; exit 0.
- Targeted Candidate tests: 282 passed; exit 0.
- Harness unit tests: 31 passed in 43.96s; exit 0.
- Project structure: `python .tfw/scripts/gen_index.py --check project` reports the project consistent with release 2.1.0; exit 0.
- Global task-state census: `python .tfw/scripts/gen_index.py --check tasks` reports no RTPSN error but exits 1 for one pre-existing RDP journal summary of 123 code points against the 120-point ceiling; not modified in this phase.
- Harness dry-run: exact 54-entry schedule, six fixtures, three arms, three repetitions, max strengthened delta 15; no model call or residue.
- Independent summary/check: exit 0; `ac3_status=BLOCKED`; `valid_runs=7/54`; `reported_total_tokens=702852`; `terminal_result=BASELINE RETAINED`; skill edits unauthorized.
- Receiver parity: 11/11 Codex source/install pairs, 11/11 Claude workflow copies, and 11/11 undeclared singular Antigravity compatibility copies exact; declared Cursor and plural Antigravity absent as recorded.
- Evidence audit: 6/6 required artifacts resolve; summary JSON and 9 JSONL records parse; 44 topology rows; 7 AC rows plus exactly one accounting row; runtime generated-input census clean; protected Candidate diff empty.
- Temporary cleanup: no `tfw-command-entry-*` fixture residue remains under the system temp directory.

## 5. Evidence

See [EV file](evidence/EV__phase-a__command_entry_reliability.md) for evidence details.

Evidence verdict: 7/8 VERIFIED, 0 DEFERRED, 1 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | `workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md` | 9 | style | Pre-existing event summary is 123 code points against the 120-point schema ceiling, so the global task-state census exits 1. RTPSN is not implicated; the foreign immutable event was not modified. |

## 7. Fact Candidates

> fact-candidates: processed 2026-09-05

| # | Category | Candidate | Source | Confidence |
|---|---|---|---|---|
| 1 | Evaluation budget governance | For this phase, the token ceiling is a pre-act guardrail: once exact projection from completed valid runs proves the approved denominator infeasible, live calls stop and raw partial evidence is preserved rather than spending toward the ceiling. | Coordinator strategic STOP during Phase-A execution, 2026-09-05 | High |

## 8. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---|---|---|
| S1 | An evaluation ceiling is not a consumption target. A future comparative study should obtain a separately approved feasible denominator after bounded pilot telemetry, or use a lower-cost observable trace design, before starting the full matrix. | Experiment design / cost control | User, strategic STOP during Phase-A execution, 2026-09-05 |

## 9. Diagrams

No diagrams.

---

*RF — TFW_20260905-124029_RTPSN / Phase A: Command Entry Reliability | 2026-09-05*
