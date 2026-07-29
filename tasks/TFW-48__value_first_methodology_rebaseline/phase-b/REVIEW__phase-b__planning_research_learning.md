# REVIEW — TFW-48 / Phase B: Planning, Comparative Research, and Learning Routing

> **Date**: 2026-07-29
> **Author**: Reviewer (Codex)
> **Verdict**: 🔄 REVISE
> **Review Mode**: spec
> **RF**: [RF Phase B](RF__phase-b__planning_research_learning.md)
> **TS**: [TS Phase B](TS__phase-b__planning_research_learning.md)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

Phase B updates the twelve approved planning, comparative-research, intensity, and
research-template consumers so they consume the value-first Method Kernel. The intended
result names and bounds the Briefing → Gather → Extract → Challenge → RES procedure,
replaces activity-count closure with supported decision/evidence claims, routes selected
learning through typed receipts, and preserves the H4/T0 non-claim without changing
config values or later-phase consumers.

The framework implementation is commit `4466109` over onboarding baseline `8758529`;
commit `d2f1466` adds final EV/RF lifecycle traces. No implementation artifact was
modified during review.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | Actual implementation diff and approved scope | ✅ | `8758529..4466109` changes exactly 12 approved existing framework consumers plus README; zero new framework files; config and config template unchanged |
| 2 | Full consumer source set | ❌ | Discrepancy escalation produced 12/12 verification; glossary and conventions retain active legacy count/procedure contracts |
| 3 | Nine TS acceptance criteria | ❌ | 5/9 pass; AC-1, AC-3, AC-5, and AC-9 fail |
| 4 | Procedure fit and closure authority | ✅ | Current plan/base/Briefing MISMATCH returns only the unresolved need; fitting work retains the complete Briefing → Gather → Extract → Challenge → RES floor and Coordinator/user closure |
| 5 | Focused/deep intensity and twelve-row numeric ledger | ⚠️ | Qualitative intensity and 12/12 ledger rows pass, including `max_iterations`; legacy glossary/conventions instructions still enforce hard/recommended/required counts and a soft ceiling |
| 6 | Learning Receipts and RES/Phase D boundary | ✅ | 4/4 stage templates contain `## Learning Receipt` and explicit `No selected signal`; `## Fact Candidates`, required relations/actor, and transitional Phase D ownership remain |
| 7 | H4/scope architecture boundary | ✅ | H4 remains unresolved/T0-only; no selector, catalog, registry, runtime strategy choice, strategy extension, prohibited comparison, later-phase implementation, or thirteenth framework consumer |
| 8 | EV dispositions and rendered claims | ❌ | 9/9 rows exist and all eight N/A labels match TS fields, but E1, E3, E5, and E9 do not match independently verified source/rendered semantics |
| 9 | Tests, links, anchors, and rendered layout | ✅ | 68 pytest tests pass; diff hygiene passes; 27/27 HL/ONB citation rows resolve; affected pages/anchors load and no page-level horizontal overflow was observed |
| 10 | RF descriptive measurements | ❌ | Actual after-word total is 17,115, not 17,120; glossary, plan, HL template, and RES template after-counts are high by five words combined |

> Raw verification log: see `review/verify.md`. Verification was not limited; the first
> discrepancy triggered 100% source coverage.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | Four ACs fail and the TS failure condition against equivalent retired-count language is triggered |
| 2 | Philosophy aligned | ❌ | The approved HL contains 12, not 10, principles; all 12 were audited and P2, P4, P5, and P8 fail |
| 3 | Tech debt documented | ✅ | No new out-of-scope debt survives review; in-scope defects remain revision work, while TD-125/126 stay unchanged |
| 4 | Style & standards | ❌ | Public owner surfaces publish competing definitions and closure authority |
| 5 | Observations collected | ✅ | RF no-observation claim was challenged; no qualifying out-of-scope observation exists, and defects were not misclassified as backlog |
| 6 | RF completeness (§7–9 present) | ✅ | No-FC/no-execution-insight dispositions survive the conversation-history and Human-Only Test; diagram is meaningful |
| 7 | Evidence completeness | ❌ | EV coverage is structurally complete, but four rows do not substantively support their AC claims |
| 8 | Analytical quality | ❌ | New contracts are coherent in isolation but not across the complete affected consumer set; RF missed the contradictions |
| 9 | Source attribution | ✅ | All citations, commits, commands, source findings, and rendered observations are traceable |

## 4. Verdict

**🔄 REVISE**

The implementation has the correct Phase B architecture on its newly edited paths:
purpose-led planning, mismatch return-only semantics, full filesystem traces,
qualitative focused/deep intensity, twelve explicit numeric dispositions, typed
Learning Receipts, preserved Fact Candidate compatibility, Phase D transition wording,
and the H4/T0 boundary all independently verify. Scope is also exact: 12 approved
framework consumers, no new framework file, and no config or exact-value change.

It cannot be approved because affected canonical consumers still publish the old
behavior that Phase B was required to retire. The glossary treats Pass and
`min_iterations` as minimum gates, recommends a pass maximum, requires fixed
dimension/alternative counts, and describes stage order as flexible. Conventions still
labels `max_iterations` a soft ceiling. These statements directly conflict with the new
ledger and claim-based closure, fail AC-1/AC-3/AC-5/AC-9, violate four approved
principles, and trigger the TS Definition of Failure against equivalent retired-count
language. Passing tests and readable pages do not neutralize a semantic contradiction
that those pages visibly render.

### Items to fix

1. Reconcile the affected glossary entries for `RESEARCH`, `Stage (Research)`,
   `Pass (Research)`, `Iteration (Research)`, `min_iterations`, `Dimension
   (Research)`, and `Alternative (Research)` with the Phase B canonical procedure,
   fit, natural-dependency, numeric-disposition, and claim-based closure contracts.
   Compatibility metadata may remain, but it must not act as a universal hard floor,
   recommended maximum, configuration prerequisite, or substitute procedure.
2. Reconcile the conventions `iterations.yaml` example with the twelve-row ledger:
   remove the `max_iterations` soft-ceiling authority and make retained min/max fields'
   transitional, non-closure status unambiguous without changing their exact values.
3. Repeat the complete former-count/competing-definition semantic scan and rendered
   glossary/conventions QA. Update EV E1/E3/E5/E9 and RF AC claims only after the
   canonical consumers are mutually consistent.
4. Correct RF after-word counts to glossary 3,478; plan 1,487; HL template 1,164; RES
   template 763; total 17,115, or replace the counting method with an explicit,
   reproducible method and recompute the whole table consistently.

The fixes are confined to the approved Phase B consumers and lifecycle traces, so the
specification does not require rejection or HL/TS redesign.

## 5. Tech Debt Collected

No new tech debt. Review discrepancies D1–D4 are current Phase B acceptance defects or
RF/evidence corrections and must not be deferred to the backlog. Existing TD-125 and
TD-126 remain unchanged and out of scope.

## 6. Traces Updated

- [x] README Task Board — Phase B status set to 🔄 REVISE and REVIEW linked
- [x] REVIEW and `review/map.md`, `review/verify.md`, `review/judge.md` — created
- [x] HL status — unchanged under Reviewer role lock
- [x] project_config.yaml — N/A; no sequence or configuration change
- [x] TECH_DEBT.md — checked; no surviving item to append
- [x] Other project files — affected consumers, protected config surfaces, later-phase boundaries, and lifecycle diff checked for stale information
- [x] tfw-docs: N/A — verdict is REVISE; explicitly not run
- [x] tfw-knowledge: N/A — verdict is REVISE and no qualifying Fact Candidate exists; explicitly not run

## 7. Fact Candidates

No Fact Candidates. The human's value-first goals, proxy-count concerns,
domain-neutrality requirement, learning-loop direction, and H4 skepticism already
exist in approved planning traces. Execution messages only approved or restated those
boundaries. Review findings are repository-verifiable implementation defects, not
human-only project facts.

---

*REVIEW — TFW-48 / Phase B: Planning, Comparative Research, and Learning Routing | 2026-07-29*
