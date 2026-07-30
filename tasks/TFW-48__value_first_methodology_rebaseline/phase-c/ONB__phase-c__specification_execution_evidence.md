# ONB — TFW-48 / Phase C: Specification, Execution, and Claim-Typed Evidence

> **Date**: 2026-07-30
> **Author**: Codex Executor
> **Status**: 🟠 ONB — Awaiting Coordinator approval
> **Master HL**: [HL-TFW-48](../HL-TFW-48__value_first_methodology_rebaseline.md)
> **Parent HL**: [HL Phase C](HL__phase-c__specification_execution_evidence.md)
> **TS**: [TS Phase C](TS__phase-c__specification_execution_evidence.md)

---

## 1. Understanding

Phase C must turn the approved D55 Method Kernel into one operational claim chain
across specification, execution, evidence, and executor attestation. Requirement Claims
must state intent and authority, an observable claim, its boundary and precision, and
the intended proof. Execution must preserve approved obligations, adapt the procedure
to the work, record material deviations, and gather claim-triggered Proof Records.
RF then attests only to what those records support while leaving independent review
authority untouched. Scope-budget values remain unchanged attention signals rather
than success criteria. Phase A/B semantics, the full filesystem trace floor, the
Coordinator approval gate, and all deferred Phase D/E/F/H4 boundaries remain intact.
No framework implementation has started.

## 2. Entry Points

### 2.1 Approved framework consumers

| # | Consumer | Current reality | Planned Phase C responsibility |
|---|----------|-----------------|--------------------------------|
| 1 | [`.tfw/conventions.md`](../../../.tfw/conventions.md) | Defines generic Proof Records, evidence flow, and scope budgets, but not the complete Requirement Claim → observation → Proof Record → RF Attestation chain or its status consequences. | Own the canonical chain, claim/proof semantics, executor attestation boundary, deviation handling, Value Debt completeness, and attention-signal response. |
| 2 | [`.tfw/glossary.md`](../../../.tfw/glossary.md) | Defines Phase A proof classes and a scope budget that still says exceeding limits degrades quality and requires a split. | Align concise definitions for Requirement Claim, Proof Record, Executor Attestation, evidence status, deviation, and scope-budget attention semantics with conventions. |
| 3 | [`.tfw/workflows/plan.md`](../../../.tfw/workflows/plan.md) | Disposes research insights and checks numeric budgets, but lacks a point-of-use Requirement Claim gate and a complete response set for budget signals. | Require bounded claims and proof intent in TS, and make budget response value/cohesion-led rather than number-led. |
| 4 | [`.tfw/templates/TS.md`](../../../.tfw/templates/TS.md) | ACs contain conditions, a gate, and evidence prose without explicit intent/authority, claim boundary, precision, or proof intent. | Carry the minimal Requirement Claim structure and justified `N/A`/grouping without creating another artifact. |
| 5 | [`.tfw/templates/ONB.md`](../../../.tfw/templates/ONB.md) | Captures understanding, questions, risks, and inconsistencies but has no explicit reality check for identifiers, sources, tests, proof feasibility, and product-cohesion impact. | Make the Executor compare the approved specification with the actual execution surface before approval. |
| 6 | [`.tfw/workflows/handoff.md`](../../../.tfw/workflows/handoff.md) | Duplicates full ONB/RF shapes, defaults toward code/test/build procedure, and does not yet connect claim-triggered proof, material deviation, and attestation status. | Keep local role/gate imperatives while delegating artifact shapes to templates and making execution/proof procedure domain- and claim-sensitive. |
| 7 | [`.tfw/templates/RF.md`](../../../.tfw/templates/RF.md) | Uses binary AC checkmarks and generic lint/test/verify rows without Proof Record references, limitations, debt, deviations, or an explicit attestation authority boundary. | Make RF the Executor Attestation surface with supported status, proof references, limitations, deviations, and unresolved Value Debt. |
| 8 | [`.tfw/templates/evidence/EV.md`](../../../.tfw/templates/evidence/EV.md) | Uses a per-AC evidence table without stable Proof Record IDs or complete claim/boundary/method/provenance/actor/time/debt fields. | Own the claim-typed Proof Record index and complete Value Debt while preserving trace/status compatibility for later review. |

Baseline measurements use one reproducible method: physical lines plus regex `\S+`
tokens on the approved tree.

| Consumer | Lines | `\S+` tokens |
|----------|------:|--------------:|
| `.tfw/conventions.md` | 856 | 7,165 |
| `.tfw/glossary.md` | 326 | 3,644 |
| `.tfw/workflows/plan.md` | 195 | 1,488 |
| `.tfw/templates/TS.md` | 100 | 533 |
| `.tfw/templates/ONB.md` | 49 | 258 |
| `.tfw/workflows/handoff.md` | 172 | 1,261 |
| `.tfw/templates/RF.md` | 114 | 593 |
| `.tfw/templates/evidence/EV.md` | 52 | 267 |

### 2.2 Exact planned write scope

| Class | Planned write set | Count |
|-------|-------------------|------:|
| Approved framework consumers | The eight files in §2.1, modified in place | 8 modified, 0 new |
| Executor lifecycle traces | This ONB, Phase C EV, Phase C RF | 3 new |
| Task Board trace | `README.md` TFW-48 row only | 1 modified |
| Total planned Phase C write set | No other files | 12 files: 3 new, 9 modified |

The TS estimates 350–700 changed framework lines. Current configured signals remain
`max_files_per_phase: 14`, `max_new_files: 8`, `max_loc: 1200`, and
`max_modified_files: 12`; neither these exact values nor either config source will
change. They trigger an explicit scope/product-cohesion response and do not prove
success.

Protected from writes are the master/Phase C HL, Phase C TS, all RES and REVIEW
artifacts, Phase A/B history, configuration and its template, exact values,
review/knowledge/lifecycle/adapters/migration/release workflows, `KNOWLEDGE.md`,
`TECH_DEBT.md`, and every Phase D/E/F/H4 consumer. Any discovered thirteenth file is
Observation only.

### 2.3 Approved predecessor facts

Phase A RF plus APPROVE REVIEW establish D55 and the Local/Seam/Live/Value Debt
grammar. Phase B RF plus APPROVE REVIEW establish D56, purpose-led planning,
claim-based research closure, learning compatibility, and the current consumer tree.
Iteration 2 RES supplies claim-triggered proof and proportional packaging. Those facts
are inputs, not Phase C edit targets.

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking specification question was found. The approved HL/TS resolve scope, ownership, dependencies, protected boundaries, and acceptance authority. | N/A. Implementation remains blocked only by the mandatory Coordinator ONB approval gate. |

## 4. Recommendations (suggestions, not blocking)

1. Use stable Proof Record IDs such as `PR-1` in EV and reference those IDs from RF;
   do not introduce a second proof artifact or competing attestation vocabulary.
2. Add a compact Requirement Claim block to each TS AC with intent/authority,
   observable claim, boundary/precision, and proof intent. Allow justified `N/A` and
   grouping so low-risk work stays proportionate.
3. Execute in the TS dependency order: AC-1; AC-2; AC-3/AC-4; AC-5/AC-6; AC-7;
   AC-8; AC-9; AC-10. Verify each owner at its point of consumption.
4. Preserve the existing AC/status/artifact compatibility surfaces in EV/RF while
   adding claim-typed records, limitations, deviations, and Value Debt. This minimizes
   avoidable Phase D migration risk.
5. Use the baseline in §2.1 and one `\S+` token method for final before/after
   measurements; treat the numbers only as scope observations.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Repeating every claim field mechanically could bloat small ACs. Compact fields,
   justified grouping, and explicit `N/A` must remain valid proportionality tools.
2. Reshaping EV/RF could silently break later review consumers. Existing status and
   artifact pointers should remain legible while Phase C adds stronger semantics.
3. Grouped Proof Records can become ambiguous. Every record needs a stable ID,
   resolvable claim, explicit boundary, method, result, and provenance.
4. Removing number-led enforcement can create an unbounded escape hatch. Exceeded
   signals must still require an explicit split, reshape, justify, or Value Debt
   response based on product cohesion and proof feasibility.
5. `DEFERRED` can become filler unless every deferral names the unresolved claim,
   impact, owner, trigger, and closure condition; otherwise the truthful status is
   `BLOCKED`.
6. Compressing duplicated workflow text could weaken Executor role lock, Coordinator
   approval, or STOP semantics. Those local imperatives must remain explicit.
7. Expanded Markdown tables may render poorly. All eight changed consumers need
   rendered QA in addition to source scans.
8. The eight-consumer chain has several term owners. A final owner/consumer and
   negative-definition scan is required to prevent competing meanings.

## 6. Inconsistencies with Code (spec vs reality)

1. `conventions.md` defines generic Proof Records and evidence surfaces, but not the
   complete Requirement Claim → observation → Proof Record → RF Attestation
   relationship, truthful status consequences, or complete Value Debt contract
   required by AC-1/AC-6/AC-7/AC-8.
2. `glossary.md` says exceeding a Scope Budget degrades quality and requires splitting,
   while AC-4 requires those values to be attention signals with an explicit
   value/cohesion-led response rather than automatic success/failure authority.
3. `plan.md` has an insight-disposition gate and a split/override budget branch, but
   no point-of-use claim/boundary/precision/proof gate and no complete set of
   product-cohesion responses required by AC-2/AC-4.
4. `TS.md` has conditions, gates, and evidence prose, but no explicit
   intent/authority, observable claim, boundary, precision classification, or proof
   intent required by AC-2.
5. `ONB.md` asks for generic entry points, questions, risks, and inconsistencies but
   lacks the identifiers/source/test/proof-feasibility/outcome/scope-fragmentation
   reality check required by AC-3.
6. `handoff.md` duplicates full ONB/RF field shapes, assumes a code/test/build default,
   and lacks the material-deviation, claim-triggered proof, and RF-attestation
   relationship required by AC-3/AC-5/AC-6/AC-7.
7. `RF.md` offers binary AC checkmarks and generic command verification without Proof
   Record references, limitations, Value Debt, deviations, or the independent-review
   authority boundary required by AC-7/AC-9.
8. `EV.md` records per-AC evidence without stable Proof Record IDs or complete
   claim/boundary/method/result/provenance/actor/time/debt fields required by
   AC-6/AC-8.

These are the approved Phase C implementation gaps, not contradictions in the HL/TS.
No scope conflict or hidden implementation prerequisite was found.

## 7. Knowledge Citations

All 16 coordinator citations resolve to an existing source and named item on commit
`c9ebb6e` (`16/16`, zero missing). Two additional existing knowledge items clarify
trace presence and template proportionality.

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | [Phase A RF](../phase-a/RF__phase-a__method_kernel.md), Key Decisions 2–7 | ✅ | Applied | Protect D55 obligations, proof grammar, proportionality, and the no-H4 boundary. |
| 2 | [Phase A REVIEW](../phase-a/REVIEW__phase-a__method_kernel.md), APPROVE 9/9 | ✅ | Applied | Treat the Phase A implementation as accepted predecessor state, not a revision target. |
| 3 | [Phase B RF](../phase-b/RF__phase-b__planning_research_learning.md), purpose/closure/numeric ledger | ✅ | Applied | Preserve purpose flow, claim-based closure, learning receipt compatibility, and numeric dispositions. |
| 4 | [Phase B REVIEW](../phase-b/REVIEW__phase-b__planning_research_learning.md), APPROVE 9/9 and 12/12 | ✅ | Applied | Use the approved 12-consumer Phase B tree as the current semantic baseline. |
| 5 | [Iteration 2 RES](../research/iter2/RES.md), D14 and D17–D19 | ✅ | Applied | Make proof claim-triggered and additive, keep packaging proportional, and invent no numeric values. |
| 6 | [Iteration 1 Gather](../research/iter1/2_gather.md), HD-23/25/26/30 and AFD-10/14/36 | ✅ | Applied | Use the cited counter-cases for intent loss, phase fragmentation, source divergence, seam proof, proxy limits, and honest live-proof boundaries. |
| 7 | [KNOWLEDGE.md](../../../KNOWLEDGE.md), D24 | ✅ | Applied | Give each term one canonical owner plus observable point-of-use consumption. |
| 8 | [KNOWLEDGE.md](../../../KNOWLEDGE.md), D49 | ✅ | Applied | Keep TS requirements-first while execution guidance remains domain-adaptable. |
| 9 | [KNOWLEDGE.md](../../../KNOWLEDGE.md), D52–D53 | ✅ | Applied | Preserve the evidence role pipeline and filesystem trace floor while denying presence-as-completion. |
| 10 | [KNOWLEDGE.md](../../../KNOWLEDGE.md), D55–D56 | ✅ | Applied | Preserve the Method Kernel, proof grammar, purpose-led entry, and claim-based research closure. |
| 11 | [knowledge/philosophy.md](../../../knowledge/philosophy.md), F20/F21/F24/F26 | ✅ | Applied | Separate procedural from investigative flow, require explicit `N/A`, favor natural enforcement, and let templates carry output contracts. |
| 12 | [knowledge/philosophy.md](../../../knowledge/philosophy.md), F28/F30/F31 | ✅ | Applied | Plan proactive proof capture, preserve Evidence → Attestation → independent judgment, and keep justified MAY-deviation. |
| 13 | [knowledge/constraint.md](../../../knowledge/constraint.md), F7 | ✅ | Applied | Keep proof domain-agnostic and able to represent visual/observable non-code outcomes. |
| 14 | [knowledge/stakeholder.md](../../../knowledge/stakeholder.md), F3 | ✅ | Applied | Do not let synthetic tests attest to live behavior they did not observe. |
| 15 | [knowledge/process.md](../../../knowledge/process.md), F4/F6/F16/F18/F23/F25 | ✅ | Applied | Use algorithmic gates, bounded scope, verified sources, stable headings, honest mock/live boundaries, and provenance chains. |
| 16 | [knowledge/convention.md](../../../knowledge/convention.md), F4 | ✅ | Applied | Put the required action beside each canonical reference at the consumption point. |
| N1 | [KNOWLEDGE.md](../../../KNOWLEDGE.md), D31 | ✅ | Applied | Newly relevant: file existence proves trace presence/resume state, not semantic completion. |
| N2 | [knowledge/philosophy.md](../../../knowledge/philosophy.md), F22 | ✅ | Applied | Newly relevant: templates should own only essential structure so claim typing does not cause field bloat. |

## Mandatory Approval Gate

Phase 1 is complete. Phase 2 implementation is blocked until the Coordinator replies
with explicit `APPROVE` or `REVISE`. No framework consumer will be modified before
that decision.

---

*ONB — TFW-48 / Phase C: Specification, Execution, and Claim-Typed Evidence | 2026-07-30*
