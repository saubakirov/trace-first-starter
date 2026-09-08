# RES — TFW_20260907-133942_PTTC: Proportionate Testing and Task Closure

> **Date**: 2026-09-08
> **Author**: robert (Researcher)
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW_20260907-133942_PTTC](../../HL-TFW_20260907-133942_PTTC.md)
> **Mode**: Pipeline — focused

---

## Research Context

This sequential iteration challenged the main iteration-1 design against the independently attributed audit: actual test necessity, the current-versus-historical knowledge oracle, board-regex and historical-wrapper obligations, the six HL §3.1 scenarios, a genuine integration failure, a receiver with its own checks, and the smallest affordable future Phase A/B proof program. The main source is RES producer commit 8f1002be14af64aff608b3cdbeba6b048e223e2c from Researcher unit 01a07f61-b614-79e2-b93d-61f6411adc23; the independent audit is exact Git source commit 0ebf0b107cee9589e709746c836b989628230041 from unit 01a07f61-b613-7c10-b9f8-2b076af2a746. This iter2 work was performed by the main Researcher robert, unit 01a07f61-b614-79e2-b93d-61f6411adc23, parent root Coordinator 01a07050-9d35-7080-a5f6-afd14334e68d, owner saubakirov, under A1 / HL §4.1 and lifecycle RES. The mandate and dispatches were Coordinator-issued under the owner-approved mandate, not separate owner-origin rulings. All findings retain producer origin and were returned through the direct native parent channel. No test, build, runtime, behavioral probe, benchmark, source/code edit, implementation, release or publication action was performed.

## Briefing

The framing and scope are preserved in [1_briefing.md](1_briefing.md). The iter2 plan compared the two exact predecessor RES sources, mapped disputed checks and eight source-model scenarios, and defined a future evidence plan. The mode gate was focused, as recorded in dispatch 0fdd; Gather, Extract and Challenge were each completed at their direct Coordinator checkpoint. The briefing correction records that dispatch 425b was Coordinator-issued under A1 / HL §4.1, not a separate owner-origin ruling, and that any future cap is a TS planning proposal rather than measured runtime or timeout-based success.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Treat the two iter1 RES reports as complementary sources with separate producer and unit attribution. | They agree on the main causal boundaries but cover different scopes: the main report includes closure and receiver reasoning; the audit concentrates on test/audit necessity. Neither source replaces the other or changes its origin. |
| D2 | Select a structural family split for the dependency boundary: move only proven pure source/Git/temp-tree tests and helpers; retain a shared module-scoped build for genuine output consumers; keep ambiguous consumers under that shared build until their dependency is resolved. | Explicit fixture opt-in can preserve one module-scoped setup, but a missed HTML consumer or helper may read stale site output and pass. The split encodes an actual dependency boundary and avoids rebuilding per output test; the split itself is not proof that classification is correct. |
| D3 | Use a hybrid knowledge oracle: protect row identity/cardinality, task/phase lineage, required immutable references, current/superseded relation and attribution when material; allow harmless explanatory prose to evolve through an explicit semantic disposition. | Full-row equality overlocks harmless wording and citations, while unrestricted prose loses provenance. Exact literals remain finite regression evidence, not a universal semantic-equivalence proof. The hybrid is a defensible candidate, not the only theoretically coherent solution. |
| D4 | KEEP the board-regex guard narrowly as a pure source guard for preventing reintroduction of the retired root-board parser. | Its protected consequence is distinct from generated-output correctness and agent behavior. Removing it without an adequate replacement would reopen a known architecture; retaining it does not require a site build, registry or runtime claim. |
| D5 | REMOVE obsolete same-name baseline bodies and thin historical wrapper aliases; retain unique revision-2 predicates and all historical Git objects. | Later definitions bind the same names and the wrapper delegates to the current predicate, so the old bodies are not independent current protection. Pytest name selection is a mechanism, not evidence of a declared public compatibility contract. Git history retains the superseded evidence; no external consumer obligation is inferred without a named consumer. |
| D6 | Treat administrative carrier repair and missing terminal outcome as one closure-record integrity obligation with record-only versus material/indeterminate branches. | Both ask whether the closure record truthfully identifies the claim and result. A fake or unverifiable SHA, authority or lineage is not a benign typo. Unchanged carrier repair stops after exact validation; material change gets an affected-output check and one existing return route. |
| D7 | Use one isolated synthetic receiving project with its own owner path and check command to test receiver independence; do not export pytest, MkDocs, the sender's Git corpus or PTTC tooling as receiver requirements. | Sender evidence is applicable only to its named claim/dependency tuple. A synthetic receiver tests the boundary without requiring access to another project or making claims about all receivers. |
| D8 | Route implementation proof through existing EV/RF/status/journal carriers with finite prospective TS bounds and explicit stop/report behavior. | The plan needs same-input/same-environment comparison, absent/stale-output protection, a genuine integration defect, meaningful negative cases, changed-permission behavioral proof, closure branches and receiver evidence. Counts are proposed attempt bounds, not frozen quotas, authority or success after timeout. |
| D9 | Mark the research sufficient for planning, not for implementation, economics, reliability or task completion. | The material design choices are resolved at source-model level; all remaining gaps are named implementation evidence obligations rather than unresolved design questions. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Does the family split preserve all genuine HTML consumers and helpers while removing setup from only pure checks? | Open — implementation evidence | The source model favors the split, but future evidence must enumerate direct/helper consumers, test absent and stale output, and keep ambiguous consumers under the shared build. |
| Q2 | Does the selected dependency design produce a comparable cost/protection improvement? | Open — implementation evidence | Existing durations are mixed historical observations. A same-input, same-environment before/after comparison is still required; two selections alone do not establish a saving. |
| Q3 | Do hybrid knowledge fields distinguish harmless wording, a legitimate owner-approved successor and material authority/provenance distortion? | Open — implementation evidence and owner/Reviewer judgment | The protected boundary is defensible and concrete, but semantic equivalence is not proven by current exact-string mutants. |
| Q4 | Does the board guard retain a distinct consequence, and can obsolete wrappers be removed without a named consumer break? | Bounded implementation risk | The guard has a visible retired-parser consequence. No external wrapper consumer is evidenced in the repository; a named consumer could change the disposition, but this is not an automatic research task or public API promise. |
| Q5 | Does one closure-record integrity route stop correctly for record-only repair and return once for material/indeterminate change? | Open — implementation evidence | The branches and existing owners are identified; late-output, erroneous-terminal-write and affected-output behavior remain unexecuted. |
| Q6 | Does the design preserve meaningful defect detection for changed permissions, a genuine integration failure and a receiver with its own checks? | Open — implementation evidence | Future proof must include one bounded behavior case, one real integration-failure case, one synthetic receiver and meaningful negative cases. No claim is made now. |

No material research-design question remains after Challenge. Q1–Q6 are execution evidence obligations for TS/implementation, not a reason to launch a generic third research iteration.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | A substantial avoidable part of the pure-check cost comes from implicit full-site setup and repeated processes; separating actual dependencies will materially improve it. | needs-research | 🟡 Source-backed dependency cause and family-split design; cost and protection effect unmeasured | [2_gather.md#G2](2_gather.md#g2-actual-dependency-and-necessity-surface), [3_extract.md#E1](3_extract.md#e1-shared-output-setup-versus-pure-family-separation), [4_challenge.md#C1](4_challenge.md#c1-explicit-opt-in-versus-family-split-under-absent-and-stale-output) |
| H2 | Relevant-input and environment provenance permits useful evidence reuse while a bounded counterexample set still catches meaningful cross-surface defects. | needs-research | 🟡 Hybrid protected-field boundary selected as defensible; reuse effectiveness and semantic counterexample coverage unverified | [2_gather.md#G1](2_gather.md#g1-agreement-and-disagreement-between-the-two-iteration-1-reports), [3_extract.md#E2](3_extract.md#e2-knowledge-oracle-with-protected-meaning-and-flexible-explanation), [4_challenge.md#C2](4_challenge.md#c2-knowledge-oracle--owner-approved-successor-harmless-wording-and-material-distortion) |
| H3 | A finite post-capture check and bounded administrative recovery can preserve all existing authority/knowledge safeguards without forcing fresh review and knowledge cycles on unchanged product claims. | needs-research | 🟡 One closure-record integrity duty with finite branches selected; closure behavior unverified | [3_extract.md#E4](3_extract.md#e4-one-closure-record-integrity-obligation-with-two-materiality-branches), [4_challenge.md#C4](4_challenge.md#c4-closure-record-integration-failure-and-synthetic-receiver) |
| H4 | Removing accidental coupling and consolidating duplicated verification/closure responsibilities can produce a simpler complete design than adding a new selection, caching or control layer, while preserving meaningful defect detection. | needs-research | 🟡 Source-backed planning design selected: family split, hybrid oracle, narrow guard, removal of duplicate bodies/wrappers and bounded receiver; completeness and reliability unverified | [3_extract.md#E3](3_extract.md#e3-board-regex-guard-and-historical-wrapper), [4_challenge.md#C3](4_challenge.md#c3-board-regex-guard-and-obsolete-same-name-bodies), [4_challenge.md#C5](4_challenge.md#c5-minimum-implementation-proof-program-and-affordable-caps) |

## HL Update Recommendations

> **The researcher classifies, never applies or rules.** The following are recommendations only. No HL section was edited in this iteration. Free-section refinements are separate from frozen-section amendment proposals.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 | Record the refined dependency boundary: retain one shared module-scoped setup for proven generated-output consumers; move only proven pure tests/helpers; leave ambiguous consumers under the shared build. State that source classification and cost/protection remain implementation evidence, not results of this research. | [4_challenge.md#C1](4_challenge.md#c1-explicit-opt-in-versus-family-split-under-absent-and-stale-output) |
| R2 | §7.2 | Retain the official pytest fixture and test-selection references as tool-mechanics context, and state that explicit fixture scope, node/name selection and Python binding do not establish semantic equivalence, TFW authority or a public compatibility API. | [2_gather.md#G2](2_gather.md#g2-actual-dependency-and-necessity-surface), [4_challenge.md#C3](4_challenge.md#c3-board-regex-guard-and-obsolete-same-name-bodies) |
| R3 | §8 | Specify the hybrid knowledge dependency tuple and existing carriers: claim-relevant inputs, oracle/authority, environment, exact Git identity and applicable EV/RF/status/journal record; keep receiver evidence task-local and do not create a registry/cache/passport. | [3_extract.md#E2](3_extract.md#e2-knowledge-oracle-with-protected-meaning-and-flexible-explanation), [4_challenge.md#C4](4_challenge.md#c4-closure-record-integration-failure-and-synthetic-receiver) |
| R4 | §9 | Add the concrete risks of stale-output false green after missed explicit fixture use, overbroad full-row knowledge locking, removal of distinct board-parser protection, unverified wrapper consumers and timeout-as-success. | [4_challenge.md#C1](4_challenge.md#c1-explicit-opt-in-versus-family-split-under-absent-and-stale-output), [4_challenge.md#C2](4_challenge.md#c2-knowledge-oracle--owner-approved-successor-harmless-wording-and-material-distortion), [4_challenge.md#C3](4_challenge.md#c3-board-regex-guard-and-obsolete-same-name-bodies) |
| R5 | §10 | Record iter2 as sufficient-for-planning: H1 dependency cause selected but cost unmeasured; H2 hybrid boundary defensible but unverified; H3 closure route specified but unexecuted; H4 source-backed planning design selected but completeness unverified. Name the finite implementation evidence program and state that no generic iter3 follows from prohibited experiments. | [4_challenge.md#C5](4_challenge.md#c5-minimum-implementation-proof-program-and-affordable-caps) |
| R6 | §11 | Add the research implication that simplicity is measured by complete consequence coverage and finite ownership: a smaller diff or faster run is not enough, and a receiver must retain its own acceptance authority. | [1_briefing.md](1_briefing.md), [4_challenge.md#C4](4_challenge.md#c4-closure-record-integration-failure-and-synthetic-receiver) |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

**No amendment proposals.** The iteration changes no frozen vision, target state, phase set, DoD/DoF, role mandate or principle. All recommendations refine how the approved contract can be met; no §12 ruling is requested.

## Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Candidate novelty:** No new human-only Fact Candidates were discovered in iter2. The source observations are either already represented by the predecessor RES or are implementation planning constraints; they are not promoted project knowledge.

**No new human-only Fact Candidates.** Existing source-derived observations remain in the predecessor reports and are referenced by the stage files; iter2 does not create a duplicate candidate set.

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | philosophy | The simplest adequate design is defined by actual protected consequences and finite ownership, not by the smallest diff or fastest nominal command. **Implication:** a family split is justified when it removes a real dependency while retaining shared output protection; ambiguity must remain visible rather than being optimized away. | Coordinator dispatch 63ed, owner-approved HL §1/§7, Briefing iter2 | ★★★ |
| SS2 | process | A prospective cap is a pre-act planning guard, not a consumption target, authority source or success criterion; missing evidence must be preserved and reported. **Implication:** TS must name comparable inputs/environment, evidence fields and stop behavior, and cannot erase required observations to satisfy a command count. | Coordinator dispatch 63ed and iter2 User Direction | ★★★ |
| SS3 | stakeholder | Receiver portability means respecting the receiving project's own checks and authority, not exporting the sender's tools or claiming sender evidence is universal. **Implication:** one isolated synthetic receiver is enough to test the boundary without blocking on access to a real external owner. | Coordinator dispatch 63ed, HL §3.1 receiver case | ★★★ |

## Findings Map

~~~text
Module-wide autouse build
        │
        ├── genuine site/ consumers ──► retain one shared module-scoped setup
        │
        └── pure source/Git consumers ──► move only when proven pure
                                      │
                       omitted/misclassified consumer + stale site/
                                      ▼
                              possible false green
                                      │
                                      ▼
             static direct/helper inventory + absent/stale-output proof

Full-row knowledge snapshot ──► harmless wording falsely rejected
Historical-only current oracle ─► legitimate successor falsely rejected
                                      │
                                      ▼
                    hybrid protected fields + current semantic route

Same-name baseline bodies ──► later binding shadows obsolete definitions
Thin historical wrappers ──► duplicate current predicate / unproven API promise
                                      │
                                      ▼
     remove obsolete bodies/wrappers; retain unique rev2 checks and Git history

Capture-only closure ──► changed output or missing outcome can pass unnoticed
                                      │
                                      ▼
       one closure-record integrity duty: exact repair stop OR
       affected-output check → one material return → finite stop
                                      │
                                      ▼
                         receiver keeps its own check and authority
~~~

This map is a source-backed planning model. It is not a runtime, reliability, performance or defect-detection result.

## Iteration Status

- **Iteration:** 2 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (dependency cause and safer split selected; cost/protection unmeasured), H2 (hybrid oracle selected as defensible; semantic/reuse effectiveness unverified), H3 (closure-record integrity route selected; behavior unverified), H4 (source-backed planning design selected; completeness/reliability unverified)
- **Hypotheses deferred:** None as a design question. The empirical portions of H1–H4 remain explicit implementation evidence obligations.
- **Gaps discovered:** complete direct/helper consumer enumeration; absent/stale-output protection; same-input/same-environment cost comparison; meaningful negative cases; exact hybrid field semantics; changed-permission behavioral proof; genuine integration-failure proof; closure late-output and terminal-record branches; synthetic receiver result; bounded external wrapper-consumer uncertainty.
- **Superseded decisions:** Iter2 supersedes the iter1 provisional explicit-opt-in preference as the planning default under the stale-output counterexample: use family split for proven pure checks, with ambiguous consumers retained under shared build. It does not supersede iter1's current/historical separation, claim-granular evidence applicability or finite closure ownership.

### Open Threads (for next iteration)

No further research iteration is required by this RES. The following are named implementation-evidence threads for TS/execution, not generic research debt:

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | Prove the family boundary | A split can still misclassify an HTML consumer if classification is not checked. | One static direct/helper inventory; one same-input/same-environment output-versus-pure comparison; absent and stale-output cases; ambiguous consumers stay under shared setup. |
| 2 | Prove the protected knowledge boundary | Hybrid fields must preserve authority/lineage while allowing harmless prose evolution. | Three named variants: wording-only, owner-approved successor, material/fake authority or SHA; use existing carriers and owner/Reviewer judgment. |
| 3 | Prove closure and receiver behavior | Source reasoning cannot establish changed-permission behavior, affected-output convergence or receiver independence. | One bounded behavioral permission case, one genuine integration defect, one closure-record integrity scenario with record-only/material branches, and one synthetic receiver with its own check command. |
| 4 | Bound wrapper risk | Git history and current predicates may be enough, but an external selector consumer would be a concrete counterexample. | Keep the question dormant unless a named consumer or receiver obligation appears; do not create a public API or generic third iteration. |

### Recommendation

- [x] **SUFFICIENT** — proceed to /tfw-plan to classify these recommendations and write TS
- [ ] **MORE NEEDED** — no material design question remains; implementation evidence is required after planning
- [ ] **BLOCKED** — no blocker

> ⚠️ Coordinator decides whether to continue or proceed. This Researcher recommends planning, but does not authorize implementation, release, publication or task completion.

## Conclusion

Iteration 2 compared the main and independent iter1 RES sources without merging their attribution, challenged the stale-output failure of explicit fixture opt-in, and selected a source-backed planning design: split only proven pure tests/helpers from genuine output consumers while retaining one shared module-scoped build for the latter; use a defensible hybrid knowledge oracle; KEEP the board-regex guard narrowly; REMOVE obsolete same-name bodies and uncontracted wrapper aliases while retaining unique revision-2 predicates and Git history; combine carrier repair and missing terminal outcome into one finite closure-record integrity duty; and verify receiver independence through one synthetic project with its own check command. The research supplied concrete boundaries that a generic “remove coupling” conclusion would miss, especially the possibility of a false green on stale output, the difference between a thin wrapper and a supported compatibility contract, and the need to preserve required evidence while capping future work. The result is sufficient to write a TS, not evidence of savings, semantic equivalence, native behavior, defect-detection completeness, receiver-wide portability or DONE; those claims remain explicitly assigned to future approved implementation evidence. No material design question warrants iter3 on its own, and no prohibited experiment was run merely to make research appear proven.

---

*RES — TFW_20260907-133942_PTTC: Proportionate Testing and Task Closure | 2026-09-08*
