# RES — TFW_20260907-133942_PTTC: Proportionate Testing and Task Closure

> **Date**: 2026-09-08
> **Author**: robert (Researcher)
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW_20260907-133942_PTTC](../../HL-TFW_20260907-133942_PTTC.md)
> **Mode**: Pipeline — focused

---

## Research Context

This first main-chain iteration investigates the causes behind CRATM and CRUE verification cost and closure friction: implicit fixture/process dependencies, historical oracles applied to evolving current claims, evidence applicability, and post-capture ownership. The research is bounded to H1–H3 and the combined design against H4; it does not duplicate the independent test-family audit. The work was performed by Researcher `robert`, unit `01a07f61-b614-79e2-b93d-61f6411adc23`, parent root Coordinator `01a07050-9d35-7080-a5f6-afd14334e68d`, owner `saubakirov`, under A1 / HL §4.1 and lifecycle `RES`. Dispatch lineage is `baf3 → 15d2 → 108a → 90e3 → 20d6 → d97f`; the originating proposer is `{principal: robert, unit: 01a07050-9d35-7080-a5f6-afd14334e68d}` for the mandate/scope and `{principal: robert, unit: 01a07f61-b614-79e2-b93d-61f6411adc23}` for the Briefing and subsequent stage findings. All returns used the direct native parent channel. No runtime experiment, test/build run, product edit, or behavioral proof was performed.

## Briefing

The complete framing is preserved in [`1_briefing.md`](1_briefing.md). It accepted focused mode, kept the independent audit separate, and set the scope to the CRATM/CRUE causal timeline, actual fixture/process dependencies, evidence applicability, finite post-capture ownership, H1–H3 and the combined design against H4. The Briefing plan was:

- Gather the source-backed timeline and actual dependency edges.
- Extract the oracle, evidence-carrier and closure dimensions.
- Challenge real sufficient constructions and select a simplest provisional design.

The immutable CRUE source input was resolved to repair commit `a767b17072733dc856d4c73fa6a72277e1538ba5`, tree `06e466315a856ede01044b521d840647163014d4`, reported as `549 passed, 1 skipped in 715.86 s` on isolated release preparation. It was inspected as an attributed source, not rerun or treated as saved-master integration/publication proof.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Separate stale historical/current oracle failure, fixture/setup coupling, execution mistakes and closure protocol gaps. | CRATM records show these causes co-occurred but are not interchangeable; one remediation cannot be justified by a combined duration alone. |
| D2 | Treat the module-wide MkDocs fixture as an execution dependency boundary, not a build-per-test claim. | `scope="module", autouse=True` establishes one shared setup per module/process; the pure knowledge/Git predicate does not consume generated HTML. |
| D3 | Preserve exact historical preimages only for claims whose subject is historical identity or package replay; use semantic current predicates for evolving current contracts. | CRATM and the attributed CRUE repair both expose the failure of applying a historical snapshot as the sole current-state oracle. |
| D4 | Make evidence reuse claim-granular: reuse only when relevant inputs, oracle/authority and environment assumptions are unchanged; recheck only affected claims/outputs when a dependency changes. | An enclosing commit or unrelated file change does not automatically invalidate every claim, while unconditional reuse is not defensible. |
| D5 | Use the existing EV/RF evidence structure plus exact Git identity as the smallest sufficient evidence carrier; keep `status.md` and `journal/` as control carriers. | This records the material dependency tuple without creating a universal passport, registry, cache or parallel control system. |
| D6 | Select S1 as the simplest provisional design: dependency-scoped verification, separated current/historical oracles, conditional applicability and one existing bounded material-return route after affected-output checking. | It removes an avoidable cause and duplicated obligation while preserving structural/provenance checks and existing Reviewer/Coordinator/owner boundaries. It is not implementation approval or empirical proof. |
| D7 | Do not infer savings, reliability, receiver portability or complete defect detection from this iteration. | No same-environment trial, behavioral replay, receiving-project test or broad run was authorized or performed. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Which immutable CRUE repair should anchor applicability? | Closed for this iteration | `a767b17072733dc856d4c73fa6a72277e1538ba5`, tree `06e466315a856ede01044b521d840647163014d4`; attributed isolated preparation only. |
| Q2 | Does removing the MkDocs dependency from the pure text/Git path produce a material same-environment saving while retaining protection? | Open — implementation evidence owed | Structural coupling is source-established; setup/body/process/attention cost and before/after saving remain unmeasured. |
| Q3 | Can evidence reuse and invalidation be demonstrated with unchanged and changed relevant dependency tuples? | Open — implementation evidence owed | The rule is architecturally explicit, but no reuse/invalidation trial was run. |
| Q4 | Can a bounded post-capture route distinguish administrative carrier repair from accepted-output/oracle/authority change and stop without a bookkeeping-only cycle? | Open — implementation evidence owed | Existing owners and a stop condition are identified; the late-output/terminal-write replay remains to be performed. |
| Q5 | Does S1 preserve meaningful defect detection in a receiving project with its own checks? | Deferred to sequential iteration 2 | Not authorized in this dispatch; it requires a named bounded case, evidence and cost approved by the Coordinator. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | A substantial avoidable part of the pure-check cost comes from implicit full-site setup and repeated processes; separating actual dependencies will materially improve it. | needs-research | 🟡 Structurally supported; economic effect unverified | [`2_gather.md#G1`](2_gather.md#g1-cratm-and-crue-causal-timeline-and-cost-boundary), [`2_gather.md#G2`](2_gather.md#g2-fixture-and-oracle-dependencies), [`4_challenge.md#C1`](4_challenge.md#c1-h1--challenge-the-cost-cause-not-the-build-itself) |
| H2 | Relevant-input and environment provenance permits useful evidence reuse while a bounded counterexample set still catches meaningful cross-surface defects. | needs-research | 🟡 Conditionally supported architecturally; empirical applicability unverified | [`3_extract.md#E2`](3_extract.md#e2-h2-inputs-oracle-environment-and-the-smallest-existing-carrier), [`4_challenge.md#C2`](4_challenge.md#c2-h2--applicability-is-claim-granular-not-commit-global) |
| H3 | A finite post-capture check and bounded administrative recovery can preserve all existing authority and knowledge safeguards without forcing fresh review and knowledge cycles on unchanged product claims. | needs-research | 🟡 Supported as a bounded route; closure behavior unverified | [`3_extract.md#E3`](3_extract.md#e3-h3-protocol-obligations-execution-mistakes-and-material-return), [`4_challenge.md#C3`](4_challenge.md#c3-h3--bounded-administrative-repair-versus-material-change) |
| H4 | Removing accidental coupling and consolidating duplicated verification and closure responsibilities can produce a simpler complete design than adding a new selection, caching or control layer, while preserving meaningful defect detection. | needs-research | 🟡 Simplest design survives source challenge; empirical completeness unverified | [`3_extract.md#E4`](3_extract.md#e4-h4-interaction-patterns-for-challenge), [`4_challenge.md#C4`](4_challenge.md#c4-h4--simplest-complete-design-and-protected-consequences) |

## HL Update Recommendations

> **The researcher classifies, never applies or rules.** The following are recommendations only. Free-section refinements are separate from frozen-section amendment proposals; no frozen claim is changed by this RES.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 | Preserve the source-backed distinction between one module/process fixture setup and per-test execution, the pure knowledge/Git input boundary, and the unmeasured cost boundary. Keep CRUE repair `a767b170…` explicitly attributed as isolated preparation, not saved-master integration or publication. | [`2_gather.md#G1`](2_gather.md#g1-cratm-and-crue-causal-timeline-and-cost-boundary), [`2_gather.md#G2`](2_gather.md#g2-fixture-and-oracle-dependencies) |
| R2 | §7.2 | Add the official pytest fixture, MkDocs CLI, W3C PROV-DM and Git revision references as applicability context, stating that they confirm tool/provenance semantics but do not supply TFW authority, semantic equivalence or agent-behavior proof. | [`2_gather.md#G2`](2_gather.md#g2-fixture-and-oracle-dependencies), [`3_extract.md#E2`](3_extract.md#e2-h2-inputs-oracle-environment-and-the-smallest-existing-carrier), [`4_challenge.md#C2`](4_challenge.md#c2-h2--applicability-is-claim-granular-not-commit-global) |
| R3 | §8 | Record the existing EV/RF plus exact Git identity as the smallest evidence carrier for materially related checks; state that relevant input, oracle/authority and environment are recorded only to the degree applicable to that claim, with no new registry/cache. | [`3_extract.md#E2`](3_extract.md#e2-h2-inputs-oracle-environment-and-the-smallest-existing-carrier) |
| R4 | §9 | Add risks for exact-string detector sensitivity being mistaken for semantic proof, unmeasured cost/reliability claims, and post-capture output drift being hidden by a marker-only close. | [`3_extract.md#E1`](3_extract.md#e1-protected-predicate-versus-semantic-meaning), [`4_challenge.md#C1`](4_challenge.md#c1-h1--challenge-the-cost-cause-not-the-build-itself), [`4_challenge.md#C3`](4_challenge.md#c3-h3--bounded-administrative-repair-versus-material-change) |
| R5 | §10 | Record the iteration-1 results: H1 structural support only; H2 conditional architectural support; H3 bounded-route support; H4 architectural support for S1 only; and the three material questions reserved for sequential iteration 2. | [`4_challenge.md#C1`](4_challenge.md#c1-h1--challenge-the-cost-cause-not-the-build-itself)–[`4_challenge.md#C4`](4_challenge.md#c4-h4--simplest-complete-design-and-protected-consequences) |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

**No amendment proposals.** S1 is a refinement of how the already-frozen outcomes can be met; no change to HL §§1, 3, 4, 5, 6 or 7 is proposed.

## Fact Candidates

> **Cognitive mode:** Pure reporting. These candidates include source-derived observations requested for assessment; they are not verified project knowledge and contain no recommendation.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | environment | `docs/scripts/test_integration.py` declares `build_site` with module scope and `autouse=True`; its body invokes `python -m mkdocs build --config-file docs/mkdocs.yml`. | [`2_gather.md#G2`](2_gather.md#g2-fixture-and-oracle-dependencies); [`docs/scripts/test_integration.py`](../../../../../docs/scripts/test_integration.py#L20-L37) | ★★★ |
| FC2 | convention | The knowledge predicate extracts one exact row for each selected decision from named Git objects and checks selected state-transition/provenance strings and SHAs. | [`3_extract.md#E1`](3_extract.md#e1-protected-predicate-versus-semantic-meaning); [`docs/scripts/test_integration.py`](../../../../../docs/scripts/test_integration.py#L2650-L2720) | ★★★ |
| FC3 | process | Review Step 7 routes an approved result through `tfw-docs` and, when needed, `tfw-knowledge`; `DONE` follows both markers and no undisposed REVIEW §5 item. | [`2_gather.md#G3`](2_gather.md#g3-diagnostic-gate-and-finite-closure-ownership); [review workflow](../../../../../.tfw/workflows/review.md#step-7-knowledge-capture-knw) | ★★★ |
| FC4 | context | CRUE repair commit `a767b17072733dc856d4c73fa6a72277e1538ba5` changes current-release and doctor-test paths and reports `549 passed, 1 skipped in 715.86 s` on isolated release preparation. | [`2_gather.md#G1`](2_gather.md#g1-cratm-and-crue-causal-timeline-and-cost-boundary); commit inspection; updated HL §2 | ★★★ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | philosophy | The owner makes the Saint-Exupéry principle the center of PTTC: success is a simpler complete and coherent system, not a faster run or a smaller diff by itself. **Implication:** every cost reduction must be tested against preserved protection and continuation. | Owner direction recorded in HL §1 and §7; 2026-09-08 research dispatch | ★★★ |
| SS2 | stakeholder | The owner requires confidence that the failure pattern is not exported to receiving projects and reserves implementation/publication decisions after research. **Implication:** applicability and receiver boundaries must be explicit, and this RES must not turn architectural support into release authority. | Owner-approved HL execution boundary and dispatch lineage `baf3 → d97f` | ★★★ |
| SS3 | process | The owner explicitly bounds agent work to direct parent routing, no unnecessary units and no expensive probes without a prospective question and cost. **Implication:** the research design itself must avoid replacing one machinery loop with a new reporting or measurement loop. | Owner-approved A1 / HL §4.1 and direct research dispatches | ★★★ |

## Findings Map

```text
Historical/current oracle drift ──────┐
                                      ├─► false rejection of coherent successors
Module-wide implicit site setup ─────┤    + repeated process/attention cost
                                      │
Marker-only post-capture close ──────┘
              │
              ▼
      Existing protection is mixed with avoidable coupling
              │
              ▼
S1: dependency-scoped checks
    ├─ pure text/Git path has no MkDocs prerequisite
    ├─ current semantic predicate ≠ immutable historical preimage predicate
    ├─ reuse only for unchanged relevant input/oracle/environment tuple
    └─ capture → affected-output check → one existing material return route
              │
              ▼
      Preserve structural/provenance protection and finite ownership
      while avoiding a new selector/cache/counter/control layer
```

The map is a source-backed causal model, not a measured performance or reliability result.

## Iteration Status

- **Iteration:** 1 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (structural support; cost unverified), H2 (conditional architectural support; reuse unverified), H3 (bounded-route support; closure replay unverified), H4 (S1 architectural support; completeness unverified)
- **Hypotheses deferred:** No hypothesis was silently deferred; the empirical portions of H1–H4 are explicitly open implementation-evidence obligations.
- **Gaps discovered:** same-environment setup/body/process/attention cost; authority-preserving rewording versus material authority change; claim-granular reuse/invalidation trial; changed accepted-output check after capture; late-output plus erroneous terminal-write replay; receiver-own-checks boundary; independent audit comparison.
- **Superseded decisions:** None.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | Bounded same-environment pure-check comparison | Structural coupling is proven, but material saving and preserved detection are not. | Compare the same pure text/Git claim with and without the unrelated site setup, recording only applicable setup/body/process evidence and selected negative cases. |
| 2 | Authority-preserving rewording versus real distortion | Exact-string sensitivity can reject harmless wording while missing the distinction between principal attribution and working-unit identity if the predicate is poorly scoped. | Use representative source-derived cases and independent judgment; classify the consequence before any KEEP/REWORK/MOVE/REMOVE proposal. |
| 3 | Late accepted-output change and administrative terminal-write error | H3 needs evidence that the route checks affected outputs, returns on material change and stops without a bookkeeping-only loop. | Replay the two cases through existing Reviewer/Coordinator carriers; no numeric return quota and no automatic full-suite/MkDocs run. |
| 4 | Compare the independent necessity audit with this main RES | Parallel findings must remain separately attributed before sequential iteration 2 is framed. | Coordinator supplies the immutable audit RES; compare agreements/disagreements against the six HL cases and receiver-own-checks boundary. |

### Recommendation
- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [x] **MORE NEEDED** — authorize a separately bounded sequential iteration 2 for the named empirical/applicability questions above; do not infer completion from this source-backed design
- [ ] **BLOCKED** — no blocker

> ⚠️ Coordinator decides whether to continue or proceed. This Researcher does not authorize iteration 2, implementation, release or publication.

## Conclusion

Iteration 1 traced the CRATM/CRUE causal chain and found a coherent simplest provisional design: scope expensive setup to checks that consume generated output, separate current semantic predicates from immutable historical preimage checks, reuse evidence only for unchanged relevant inputs/oracle/environment assumptions, and route changed accepted outputs through one existing bounded material-return path. The work exposed why a row-level mutant count cannot stand in for semantic proof, why a changed enclosing commit does not invalidate unrelated evidence, and why administrative record repair must not be confused with an authority or accepted-output change. This source-backed structure would have been missed by treating the incidents as one slow suite or by adding a universal selector/cache/control layer. The self-critique is material: no same-environment timing, defect-detection, receiver, native-behavior or closure replay was run, the independent audit was not read or merged, and the design remains architectural support rather than implementation proof; those limits are the reason for the Coordinator-directed MORE NEEDED recommendation and the stop before iteration 2.

---

*RES — TFW_20260907-133942_PTTC: Proportionate Testing and Task Closure | 2026-09-08*
