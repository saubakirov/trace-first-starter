# Phase HL — TFW_20260905-124029_RTPSN / Phase A: Command Entry Reliability

> **Date**: 2026-09-05
> **Author**: Codex (Coordinator)
> **Status**: 🧩 DERIVED — Phase TS draft
> **Master HL**: [Role, Task, and Phase Session Naming](../HL-TFW_20260905-124029_RTPSN.md)
> **Master Contract**: 🔒 FROZEN — owner verdicts applied at `7bc0f30`; this file adds execution context only
> **Research Basis**: [Iteration 1 RES](../research/iter1/RES.md) · [Iteration 2 RES](../research/iter2/RES.md)

---

## Parent Derivation

This phase implements only master HL §4 Phase A and inherits master DoD A1–A8, DoF 1–5 and 10–12, and §7/§7.1 without changing them. Its required result is an evidence-backed entry contract for all 11 `/tfw-*` commands and four declared adapter classes, with behavioural evidence separated from source, parity, invocation, and load evidence.

Vision, target naming grammar, acceptance, failure conditions, and principles remain solely in the frozen master HL. Phase B remains the only phase allowed to implement session-title grammar, rename placement, phase cues, `LEAD`, collision rendering, or the approved A1 stable-key suffix. The rejected A2 ASCII separator fallback remains rejected.

## Finished Phase View

```text
11 canonical commands × 4 declared adapters
                 |
                 +--> source present -------- structural evidence
                 +--> receiver exact -------- parity evidence
                 +--> command invoked ------- live trace R2
                 +--> workflow loaded ------- live trace R3
                 +--> role/order/gate obeyed  live trace R4
                 +--> one arm beats another - controlled estimate R5
                                                    |
                         +--------------------------+--------------------+
                         |                                               |
              threshold not met                              strengthened proxy wins
                         |                                               |
              current thin proxy stays                  same thin architecture, clearer
              production baseline                       pre-action boundary, 11/11 sync

              full-copy/direct winner --> STOP; new TS required before production use
```

The stakeholder receives a result that says exactly what is known: which command and adapter routes are structurally sound, what the live Codex trials observed, which failures occurred at which boundary, and whether production stayed on the least-regret baseline or adopted the only pre-authorized bounded strengthening. No file topology or successful title is presented as proof of obedience.

## Starting Point

- Iteration 1 refuted H3 as stated. The CRATM incident is an uncovered canonical-workflow path and the RTPSN incident is post-load noncompliance; both traces include the current skill and complete `plan.md` read.
- H4 is inconclusive. No full-copy, current-proxy, strengthened-proxy, or direct design has a measured comparative cross-role adherence advantage.
- The current thin Codex proxy plus canonical workflow is therefore the least-regret operational baseline, not a proven winner.
- Current structural assurance already covers manifest shape, exact source/copy parity, clean receivers, one Role Lock, unique workflow Read Contracts, and semantic mutants. It does not provide live invocation/load/conformance estimates.
- The manifest declares 11 commands and four adapters. In this checkout Codex is installed and live-observed; Claude command copies are present but not live-observed; Cursor and plural Antigravity receivers are absent; singular `.agent/workflows/` copies are compatibility files, not declared Antigravity authority.
- Research measured `/tfw-plan` at 2,291 words/~3,055 estimated tokens for current proxy plus canonical workflow, 2,150/~2,867 for full/direct canonical content, and 2,301/~3,068 for the strengthened specimen. These are word-derived estimates, not runtime telemetry.
- This is the first phase, so the predecessor-RF Pre-TS Gate is not applicable.

## Decision Boundary

Phase A compares three live Codex arms under identical fixtures: current thin proxy, the research-defined strengthened thin proxy, and a schema-valid direct prototype derived in a temporary receiver. Byte-identical full-copy routes remain a distinct structural/maintenance comparison; their runtime canonical body is not counted as an independent Codex behavioural arm.

Production follows this order:

1. Current thin proxy remains the default.
2. The strengthened proxy may replace it only when the predeclared aggregate, confidence, per-role, context-cost, and regression thresholds all pass.
3. A direct or full-copy result is evidence only. This TS does not authorize their production topology, generation, or migration. A material win stops production selection and returns the result for a new Coordinator TS.
4. An inconclusive trial is not a reason to choose a challenger; it records the limit and retains the baseline.

## Execution Boundary

### Included

- Reproduce the 11-command/four-adapter census and current/pre-RCFR entry/context comparison from immutable revisions.
- Add one reproducible, non-default live-evaluation harness with synthetic task fixtures, raw JSONL capture, independent graders, confidence intervals, usage accounting, and a hard run budget.
- Run 54 isolated Codex trials: six fixtures × three arms × three repetitions, with one pinned model and reasoning effort.
- Grade invocation, complete canonical load, Read Contract order, role/artifact boundary, gate/stop behavior, and final routing separately before producing an aggregate pass.
- Define the universal entry sequence and the six-level evidence ladder in the existing adapter/conventions authorities without adding a runtime preload or competing algorithm.
- If and only if the strengthened arm clears every decision threshold, synchronize the bounded entry-contract wording across the 11 Codex source skills and their 11 installed copies.
- Preserve exact manifest roles/routes, canonical workflows, full-copy parity, and clean-receiver tests.

### Excluded

- Session naming grammar or any Phase B rename behavior.
- A claim that RCFR, proxy thinning, full copies, or any prompt wording caused the two known incidents.
- Production deployment of full-copy or direct-single-authority Codex designs under this TS.
- Changes to canonical workflow algorithms, manifest routes/roles, persistent root preloads, or CRATM roles/orchestration.
- Live-behavior claims for Claude, Cursor, or Antigravity without a live host trace.
- A universal registry, daemon, hook, generated runtime report, or additional always-read file.

## Evaluation Contract

| Dimension | Fixed Phase-A value |
|---|---|
| Live host | local Codex CLI, version and host capability recorded before trials |
| Model / effort | `gpt-5.6-sol` / `medium` for every run |
| Arms | current proxy; strengthened proxy; schema-valid direct prototype |
| Fixtures | Coordinator new; Coordinator resume; Coordinator uncertain path; Researcher stage entry; Executor approved-TS onboarding gate; Reviewer RF-stage entry |
| Repetitions | exactly 3 per fixture/arm; 54 total completed runs |
| Isolation | one temporary Git fixture per run; ephemeral session; ignored user config; workspace-write limited to that fixture |
| Run ceiling | 750,000 total reported input+output tokens and 180 minutes wall time; reaching either before 54 valid runs is `BLOCKED`, never a smaller denominator |
| Aggregate | a run passes only when every applicable boundary grader passes |
| Superiority | challenger ≥10 percentage points over baseline; 95% difference interval excludes zero; no role loses >5 points |
| Deployment | strengthened proxy only, additionally ≤15 added words/~20 estimated tokens per skill route and all structural tests green |
| Missing telemetry | record `N/A` with raw CLI proof; word estimates remain estimates and cannot be relabelled as usage telemetry |

Trial order is deterministic and interleaved by fixture/repetition/arm so time drift is visible rather than silently aligned with one arm. Invalid infrastructure runs are retained with a reason and rerun only until the fixed 54 valid-run denominator is reached or the ceiling blocks the phase.

## Required Sequence

1. Record immutable baseline/current revisions, CLI/model/effort, route census, receiver state, current/pre-RCFR text, and word estimates before editing any runtime entry.
2. Implement and unit-test fixture construction, arm materialization, JSONL capture, graders, interval math, run ceilings, redaction, and summary generation using fake runners first.
3. Extend existing integration/runtime-context tests to reject missing, duplicated, reordered, competing-role, source/copy-drift, and self-validating entry contracts across all 11 commands and four declared adapters.
4. Run the fixed live matrix without modifying production skills.
5. Apply the production decision rule once. Retain baseline on no qualified winner; synchronize only the strengthened proxy on a qualified win; stop for a direct/full-copy production result.
6. Re-run word estimates, targeted tests, full repository tests, task/project checks, source/copy parity, and clean-receiver installation.
7. Write EV/RF from the final immutable Candidate; raw traces remain evidence and never become runtime instruction input.

## File Topology

| Surface | Phase-A purpose | Authority boundary |
|---|---|---|
| `.tfw/conventions.md` Tool Adapter Pattern | universal entry sequence and claim ladder | shared rule, not a second workflow |
| `.tfw/adapters/README.md` | four-adapter contract and evidence limits | tooling documentation; manifest remains copy metadata |
| `.tfw/adapters/codex/README.md` | Codex arm/receiver and smoke-evidence contract | no workflow algorithm |
| `docs/scripts/command_entry_eval.py` | explicit live evaluation tool | invoked only by a human/Executor; never runtime-preloaded |
| `docs/scripts/test_command_entry_eval.py` | deterministic harness/grader assurance | fake runner and mutant coverage; no network test by default |
| existing integration/runtime-context tests | 11×4 topology, role, read, parity, and semantic checks | source-derived expectations, not generated-oracle input |
| 11 Codex skill sources + 11 installed copies | conditional strengthened entry text | modified only after the decision gate; canonical workflows stay authoritative |
| Phase `evidence/` | raw trials, summary, counts, tests, EV | TRACE only; no runtime reader |

## Knowledge Applications

| PV priority | Exact item | Phase-A application |
|---|---|---|
| P0 | `README.md` How It Works: inspectable context, resume from checkpoint, human/agent responsibility | Evidence and state must let another role reproduce the selection without chat or inferred authority. |
| P1 | `.tfw/README.md` Methodology Values: Structural Enforcement, Naming Creates Behavior, Portability; Success Criteria 1–4 | Tests make violations observable; naming cues may guide but never prove compliance; receiver claims remain provider-bounded. |
| P2 | `knowledge/philosophy.md` F4, F24, F32, F43 | Prefer structural gates and self-contained steps; preserve meaning and architecture; do not patch symptoms or mistake wording for causality. |
| P3 | `KNOWLEDGE.md` D15, D54, D73–D75 | Keep thin Codex routers and one canonical selective-read authority as baseline; manifest/copy topology and source-derived semantic tests remain intact. |
| P4 | `conventions.md` Tool Adapter Pattern, Design Rules, Anti-patterns, Role Lock Protocol | No new preload or second algorithm; exact copied receivers, inline role DNA, and Coordinator/Executor boundary remain enforceable. |
| P5 | `knowledge/convention.md` F4, F5, F19 | The entry must be an algorithmic step, workflows remain source of truth, and the 11 skills use one consistent contract form if changed. |
| P6 | `knowledge/process.md` F3, F4, F27, F30, F37, F43 | Precise cues and numbered gates need observable enforcement; measurements name method/revision; absence rationale lives at the confusing entry boundary. |
| P7 | `knowledge/constraint.md` F2, F12; `knowledge/risk.md` F1 | Bound prompt growth, keep obligations in repository files, and commit only explicit phase paths in the shared index. |

## Cross-Phase Handoff

Phase B receives the selected Phase-A entry architecture, exact command/adapter coverage, the live-evidence claim boundary, and a green receiver/test baseline. It may place naming actions only inside canonical workflow checkpoints that Phase A proved reachable; it must not treat Phase-A conformance rates as proof that a session title improves recognition or that any non-Codex host behaves the same way.

## Phase-Local Risks

| Risk | Control |
|---|---|
| 54 live runs consume disproportionate usage | fixed 750,000-token/180-minute ceilings, exact denominator, explicit BLOCKED outcome, no silent sample reduction |
| grader overfits one candidate's phrasing | grade observed reads, writes, gates and routing; fake-runner mutants must change results before live use |
| sandbox prevents or masks forbidden writes | use disposable workspace-write fixtures and inspect complete Git diffs after every run |
| direct prototype accidentally becomes production design | keep it temporary and ineligible; a material win requires a new TS before any receiver edit |
| small sample is overinterpreted | publish proportions and intervals; retain baseline unless every threshold passes |
| generated evidence becomes another authority | no workflow, skill, root rule, or adapter reads the generated files; tests reject such an edge |
| conditional skill synchronization drifts | exact source/installed byte parity and all-command mutant tests gate Candidate creation |
| concurrent work enters the commit | read full status and commit with `git commit --only` over the explicit planning or execution path list |

---

*Phase HL — TFW_20260905-124029_RTPSN / Phase A | 2026-09-05*
