# RES — TFW_20260928-181352_TEQM: Task economics capture and accounting contract

> **Date:** 2026-09-28
> **Author:** Codex Researcher
> **Status:** 🔬 RES — Complete, iteration 4 of 4
> **Parent HL:** [HL-TFW_20260928-181352_TEQM.md](../../HL-TFW_20260928-181352_TEQM.md), A1 re-freeze `7db1148c057300e06f639696544913d3d067031e`
> **Mode:** Pipeline / focused
> **Producer unit:** `codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243`
> **Parent Coordinator:** `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793`
> **Activation / dispatch source:** owner-approved HL §4.1/A1; `journal/20260928-230648__dispatch__8c6a.md @ c9a8ea1df7c0e364d3ed1e1a2a7de465442898eb`; synthesis gate `journal/20260928-232942__gate_answer__4d2f.md @ e1ae77ecb9a99a298cd605c8c55bd1863122eb9f`
> **Coordination authority:** HL A1 re-freeze above; `tfw-gates-only` / `native-gates`
> **Originating proposer:** `{principal: saubakirov, unit: human owner in the Coordinator chat}` for A1; no new Researcher proposal

---

## Research Context

The owner wants a two-product period comparison and the full resource cost of a completed task, with task-bound tokens, agent execution time, money basis and product terms. This final iteration reconciles three accepted, differently scoped platform returns, tests a prospective CLI stream and one close-time classifier, and defines an exact-once task record. It provides a route to a constrained TS while preserving the gap between session-level observations and a complete multi-role pilot. The owner also asked the Antigravity and Claude agents to check neighboring-session visibility; no resulting update was an accepted input at this synthesis gate.

## Briefing

[Iteration-4 Briefing](1_briefing.md) set three questions: which exact capture route is supported; how one `economics.md` can preserve period and lifetime totals without duplicate events; and whether one bounded classifier produces supported terms with measured overhead. [Gather](2_gather.md) separated numeric source, unit binding, counter meaning, time meaning, money basis and product evidence. [Extract](3_extract.md) proposed nine configurations and a single-file ledger. [Challenge](4_challenge.md) tested the most concrete CLI route, classification, disputed attribution, period boundaries, field semantics and pricing. The Challenge correction to Extract E2 is authoritative for this recommendation.

## Decisions

| # | Decision | Rationale |
|---|---|---|
| D1 | Recommend a **prospective, task-owned AGY CLI launch/stream** as the smallest first-path candidate, with explicit role dispatch, native conversation/step keys, wrapper start/end, final cumulative reconciliation and a launched-unit coverage ledger. Make proof of role/child coverage, time basis and event-time semantics an early TS gate. | A fresh AGY 1.2.12 session emitted one usage-bearing step and matching cumulative result. This proves bounded session capture, not full HL DoD-1. [Challenge C1/C5](4_challenge.md). |
| D2 | Identify each raw consumption event by source namespace, immutable provider conversation/request/step identity and counter scope **before** assigning task/phase/role or decoder interpretation. Keep attribution and semantic claims separate and versioned. | The same native event with two role/decoder claims would be counted twice under Extract E2's proposed role-bearing key. A missing stable native ID makes an additive row ambiguous, not hash-recoverable. [Challenge C3](4_challenge.md). |
| D3 | In one `economics.md`, keep source observations, raw counters, semantic claims, intervals, money views, coverage and classifier evidence; derive phase/root and period/lifetime displays from unique leaves. Store ongoing provisional observations before close. | Final cumulative totals cannot be added to steps or split across periods without dated leaves or validated boundary deltas. Root totals reference phase leaves once and add root-only work. [Extract E1/E2](3_extract.md); [Challenge C3](4_challenge.md). |
| D4 | Keep agent execution intervals, provider model/API durations and task calendar elapsed as distinct measures. Count measured failed attempts and classifier work once even when no valid classification is returned. | Two overlapping role intervals can sum to 17 role-minutes over a 12-minute calendar union. AGY reported `SUCCESS` and token use while `structured_output` was absent after a denied command. [Challenge C1/C3](4_challenge.md). |
| D5 | A Claude Code CLI invocation is a measured classifier fallback; retain `list` cost as an estimate. Treat IDE Antigravity encoded fields and documented but unattached Desktop/OTel events as surface-specific research candidates, not a proven whole-task route. | The bounded Claude case gave four relevant synthetic terms and a primary area, but real-task correction and total setup overhead remain unmeasured. IDE field labels, exact price mapping and native Desktop attachment remain unverified. [Gather G1–G4](2_gather.md); [Challenge C2/C4/C5](4_challenge.md). |

## Open Questions

| # | Question | Status | Answer |
|---|---|---|---|
| Q1 | Does the chosen launched-unit denominator include each role, retry and child exactly once? | Open; first TS proof gate | One task-owned AGY session was observed. Child inclusion and full task routing have not been demonstrated. Parent and child aggregates must be reconciled before additive publication. |
| Q2 | Can selected-period consumption be assigned to dated provider leaves while a task spans periods? | Open for a real pilot | Synthetic leaves support the rule; a final-only cumulative result cannot supply an observed split. |
| Q3 | Which native Antigravity fields correspond to billable categories, and which model/rate applies to this subscription? | Open | The IDE producer's 69-row arithmetic is version-specific. Gemini API documentation and tariff do not identify those private fields or prove an actual charge. |
| Q4 | Do actual completed tasks yield useful 3–5 terms with acceptable correction and operating cost? | Open | One synthetic Claude invocation succeeded; AGY's structured attempt consumed tokens without output. Owner threshold and real-task samples are absent. |
| Q5 | Can Codex Desktop or Claude Code-tab expose complete own-task usage on their exact surfaces? | Open | Codex App Server and Claude OTel document possible events, but no live attachment was observed here; Code-tab `get_usage` was a context-occupancy gauge. Any later neighboring-session report needs separate Coordinator acceptance and scope qualification. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|---|---|---|---|
| H1 | At least one exact surface exposes task/role-bound tokens and execution intervals with sufficient coverage. | Proposed | 🟡 Partial | AGY/Claude CLI session captures and a wrapper interval are feasible; no complete multi-role/child denominator or whole-agent interval was demonstrated. Native IDE/Desktop claims remain qualified. |
| H2 | Task-local numeric observations support period and lifetime totals across parallel roles and ongoing work. | Proposed | 🟡 Logical contract tested; real capture open | Native-key-first dedup, cumulative-delta and overlapping-time examples work conditionally. No real cross-period multi-role data set was captured. |
| H3 | One close-time call yields 3–5 useful terms and a primary area at acceptable correction/operating cost. | Proposed | 🟡 Synthetic feasibility only | Claude CLI produced four grounded terms in 2.799 s provider duration and 4.697 s wrapper time, with $0.0235464 list estimate for that successful call. Preliminary attempts and AGY failed-call overhead prevent a total-trial cost conclusion. |
| H4 | A useful money view has known model/token categories and a declared price or payment basis. | Proposed | 🟡 Estimate basis available; charge unknown | Claude list estimate is labeled; official Gemini 3.8 Flash API rates are dated candidates, not verified Antigravity billing. Subscription allocation pool and actual charges are unknown. |

## HL Update Recommendations

The Researcher classifies these suggestions; the Coordinator applies free-section refinements or routes frozen-section proposals. No frozen outcome, DoD or phase alteration is recommended from incomplete capture evidence.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|---|---|
| R1 | §2 | Add the iteration-4 own-session AGY 1.2.12 stream and Claude CLI classifier observations, explicitly distinguishing successful token capture from failed structured classification and list estimate from billed expense. | [Challenge C1/C2](4_challenge.md) |
| R2 | §7.2 | Cite the final iter4 RES and its stage evidence; retain the exact-surface primary documentation for AGY cumulative usage, Claude cost/OTel, Codex App Server and Gemini thinking/pricing. | [Gather G2](2_gather.md); [Challenge C4](4_challenge.md) |
| R3 | §8–§9 | Make the selected prospective path's role/child denominator, native event IDs, period timestamps, interval definition and counter inclusion an explicit prerequisite/risk. Flag the conflicting IDE field labels and exact-model tariff mismatch. | [Challenge C3–C5](4_challenge.md) |
| R4 | §10 | Record H1–H4 as partial with the distinctions in the table above. Describe native-key-first dedup, source-event versus assignment claims, failed-attempt overhead and one supported-path TS proof gate; no full DoD-1 claim. | [Extract E1–E4](3_extract.md); [Challenge C1–C5](4_challenge.md) |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

**No amendment proposals.** The existing frozen contract permits a supported first pilot path and visibly partial fields; the current gap is proof of that path, not a justified change to the owner-approved target.

## Fact Candidates

**No fact candidates.** The owner's CLI steering and request for neighboring-session checks are task directions, not a new human-only project fact to consolidate. Technical findings and source versions remain in this RES.

## Strategic Insights (Research)

**No strategic insights.** No new human-sourced product-domain or project-strategy claim was supplied in this iteration; the latest owner message changed the requested evidence check, whose result is pending qualification.

## Findings Map

```text
Task/role dispatch + provider native ID + raw usage + event time
             │                 │
             │                 └─ same native event? → one raw row;
             │                    conflicting role/decoder claims stay unresolved
             ▼
       coverage and semantics gate
             │
       dated unique consumption leaves ──→ period view
             │                                  │
             └─ all task leaves once ─────────→ lifetime view
                                                │
                      interval type and money basis stay labeled
                      classifier work is another unique observation
```

The gate is causal: a CLI result with numbers but no proven role/child denominator supports a session observation, not a complete task total. A cumulative final result reconciles its leaves; it is not another leaf.

## Iteration Status

- **Iteration:** 4 of 2 minimum / 4 maximum; this Researcher's second personal iteration.
- **Hypotheses tested:** H1 partial, H2 logical contract partial, H3 synthetic feasibility partial, H4 estimate basis partial.
- **Hypotheses deferred:** None unexamined; their unresolved real-pilot claims are named in Open Questions.
- **Gaps discovered:** Native event identity must precede role attribution; full launched-unit/child coverage, cross-period event time, agent interval, IDE field semantics, actual money and real-task classifier value remain unproved.
- **Superseded decisions:** D2 here supersedes [Extract E2](3_extract.md)'s role-bearing dedup key; [Challenge C3](4_challenge.md) demonstrated the duplicate.

### Open Threads (for next iteration)

No further research iteration is authorized under A1. The following are planning/implementation proof obligations, not authorization for another probe:

| # | Thread | Why it matters | Suggested focus |
|---|---|---|---|
| 1 | Chosen path's real role/child denominator and agent interval | Required before a complete task total or DoD-1 claim | In the exact TS, make a bounded prospective capture proof the first acceptance gate. |
| 2 | Period leaves, reset/child inclusion and root/phase reconciliation | Prevents fabricated period splits and duplicate consumption | Define a stable provider key, dated leaf evidence, snapshot policy and explicit unknown state. |
| 3 | Classification quality, total overhead and monetary basis | Synthetic relevance and a list estimate cannot establish operating value or actual cost | Use real bounded task close records, corrections and an owner-selected overhead threshold; keep payment view separate. |
| 4 | Pending Antigravity/Claude neighboring-session reports | May change coverage assessment if valid and task-scoped | Coordinator accepts exact source revision and qualifies surface, scope and privacy boundary before use. |

### Recommendation

- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write a constrained TS whose first proof gate establishes one real supported task/role capture path before claiming the measurement outcome.
- [ ] **MORE NEEDED**
- [ ] **BLOCKED**

This is sufficiency for planning, **not** a finding that HL DoD-1 or the full pilot is met. The Coordinator and owner retain the exact TS, denominator, implementation and acceptance decisions.

## Conclusion

Four iterations now distinguish supported CLI session numbers, a narrow Code-tab context gauge, version-specific IDE metadata and documented but unattached event surfaces. The final probe exposed a numeric AGY success status without valid classification, while a separate Claude CLI call produced four relevant synthetic terms with a list-cost estimate. The accounting design must deduplicate native events before role attribution, reconcile cumulative totals rather than add them, and keep time, period and money semantics explicit in one task-local file. This research supports a constrained prospective TS; it has not demonstrated complete multi-role capture, actual task classification quality or billed cost, and the pending neighboring-session checks were not accepted as evidence here.

### Material handover at this return

**Producer / recipient:** Researcher `codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243` to exact parent Coordinator `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793`. **Source / epoch:** A1 controls and accepted iterations 1–3 at dispatch, iter4 Briefing/Gather/Extract/Challenge and cited official documentation/probes, all inspected 2026-09-28. **Inspected scope:** task controls, accepted research returns, public primary documents, synthetic examples and fresh task-owned CLI sessions; no other unit's live transcript/database or pending native update. **Material:** one-file record and corrected native-key-first exact-once rule; AGY CLI session capture and failed classifier, Claude CLI successful synthetic classifier with its own measured list estimate; precise route and tariff qualifications. **Uncertainty:** real role/child/period coverage, complete agent intervals, internal IDE field labels, actual payment and real-task correction/overhead. **Continuation:** Coordinator closes iteration control and routes the owner decision through `/tfw-plan`; any later native update needs its own accepted input and does not retroactively change this RES. No new iteration, implementation or retry of the denied command follows from this return.

---

*RES — TFW_20260928-181352_TEQM: Task economics capture and accounting contract | 2026-09-28*
