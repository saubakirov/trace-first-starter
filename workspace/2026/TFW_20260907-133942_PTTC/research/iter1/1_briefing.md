# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260907-133942_PTTC](../../HL-TFW_20260907-133942_PTTC.md)
> Goal: Identify the simplest complete and coherent verification design by removing accidental test coupling and duplicated obligations while preserving meaningful defect detection and honest completion.

## Research Plan

### Gather

- Inventory the bounded test families and fixtures named by the HL, beginning with `docs/scripts/test_integration.py`, `tools/tests/test_tfw_doctor.py`, and their exact callers; record the relevant paths without running tests or builds.
- Classify each assertion by the consequence it protects: current semantic invariant, historical acceptance, structural/tool correctness, release-input boundary, or incidental prose/snapshot lock.
- Trace implicit setup and dependency edges from fixture to test body and from test to live corpus, distinguishing required inputs from inherited work that can be eliminated at its cause.
- Reuse the HL's recorded incident evidence and repository history where it answers cost or behavior questions; mark unmeasured setup, body, process, and review cost explicitly.

### Extract

- For every material candidate, map the exact protected consequence, the legitimate change that could be rejected, and the real defect that could be missed if the mechanism were removed or weakened.
- Separate tautological, duplicated, obsolete, and historical-only assertions from tests that provide independent semantic, structural, or integration protection; retain important KEEP candidates and arguments against removal.
- Compare KEEP / REWORK / MOVE / REMOVE alternatives, preferring elimination of the underlying dependency or consolidation of overlapping responsibilities before proposing selectors, caches, or new control layers.
- Identify the smallest independent evidence that would preserve each surviving protection and the assumptions needed for evidence reuse; flag unknowns that would require a prospective cost decision.

### Challenge

- Construct bounded counterexamples for each proposed subtraction: a plausible legitimate change wrongly rejected and a material defect that the candidate might otherwise detect.
- Challenge the simplest complete design against cross-surface dependencies, historical/current contract drift, implicit expensive setup, and the need for independent judgment; include tests that must remain even when nearby checks are removed.
- Test H4's causal claim: determine whether removing accidental coupling and consolidating duplicated verification is sufficient, or whether any added mechanism has a concrete protective consequence that a simpler alternative cannot provide.
- Produce a finite recommendation with unresolved questions, evidence limits, and an affordable verification route; do not turn this audit into a deletion quota, benchmark campaign, or closure implementation.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | A substantial avoidable part of the pure-check cost comes from implicit full-site setup and repeated processes; separating actual dependencies will materially improve it. | needs-research |
| H2 | Relevant-input and environment provenance permits useful evidence reuse while a bounded counterexample set still catches meaningful cross-surface defects. | needs-research |
| H3 | A finite post-capture check and bounded administrative recovery can preserve all existing authority/knowledge safeguards without forcing fresh review and knowledge cycles on unchanged product claims. | needs-research |
| H4 | Removing accidental coupling and consolidating duplicated verification/closure responsibilities can produce a simpler complete design than adding a new selection, caching or control layer, while preserving meaningful defect detection. | needs-research; primary audit question |

## Scope Intent

- **In scope:** Independent necessity audit of the repository test families and fixtures relevant to H4; exact assertion paths; protected consequences; legitimate changes wrongly rejected; defects potentially missed; implicit expensive dependencies; KEEP / REWORK / MOVE / REMOVE dispositions; counterexamples; and the minimal tests that must remain. Initial conclusions are formed independently of the main Researcher's findings.
- **Out of scope:** Any source or test edit; full or targeted pytest execution; MkDocs build; broad benchmark; CRUE branch or release-policy changes; live-corpus repair; closure implementation; new agents; and any new control, selector, cache, registry, or reporting artifact. Main-investigation outputs are not used as inputs to this independent first iteration.

## Guiding Questions

1. Which candidate checks impose incidental historical, prose, snapshot, or fixture coupling rather than protecting a current consequence, and what exact legitimate change or missed defect demonstrates that distinction?
2. For each candidate, can removing or consolidating the underlying cause preserve protection more simply than adding a selection, caching, or control layer?
3. Which tests must remain, what independent evidence do they provide, and what is the smallest adequate verification route for the final design?

## User Direction

The root Coordinator approved **focused** mode for this bounded H4 audit. The focused single-pass limit reduces process cost but does not waive the approved requirement to identify important retained tests, arguments against harmful removal, and concrete counterexamples. Any expensive probe requires a prospective question and cost report to the Coordinator before execution.

## Agent Team Checkpoint

- **Selected LEAD layer:** principal `robert`; accountable owner `saubakirov`; owner-approved mandate A1 / HL §4.1; autonomous from `RES`; no implementation, publication, new units, or scope expansion.
- **Working-unit layer:** principal attribution `robert`; role `Researcher`; actual unit `01a07f61-b613-7c10-b9f8-2b076af2a746`; parent Coordinator `01a07050-9d35-7080-a5f6-afd14334e68d`; lifecycle `RES`; direct channel is native `send_message_to_thread` / `wait_threads` to the root; host `local`.
- **Governing dispatch lineage:** `journal/20260908-095937__dispatch__06ad.md` → `journal/20260908-100355__dispatch__1708.md` → `journal/20260908-100626__dispatch__31d9.md` (the last read at committed control tip `ecb6a6156a274c579f4daeffd2fd495267ad95d7`).
- **Proposal origins:** scope and unit dispatch originated from `{principal: robert, unit: 01a07050-9d35-7080-a5f6-afd14334e68d}`; this Briefing recommendation originated from `{principal: robert, unit: 01a07f61-b613-7c10-b9f8-2b076af2a746}`. Shared principal attribution does not merge units or grant this Researcher amendment authority.

---
Stage complete: YES
