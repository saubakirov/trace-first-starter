# RES — TFW_20260921-180000_RVAG: Reviewer Value-Assurance Gate

> **Current filename**: fixed `research/iter2/RES.md` under the selected task; no task-root `RES__*` is issued.

> **Date**: 2026-09-22
> **Author**: Codex Researcher
> **Status**: 🔬 RES — Iteration 2 complete
> **Parent HL**: [HL-TFW_20260921-180000_RVAG](../../HL-TFW_20260921-180000_RVAG.md)
> **Mode**: Pipeline — focused
> **Producer unit**: `codex:thread:local:01a0c7dd-94bf-78b2-82ba-b14da2e7778a`
> **Parent Coordinator**: `codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5`
> **Activation / dispatch source**: Direct delegated activation from the Parent Coordinator source `codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5` for `/tfw-research TFW_20260921-180000_RVAG iteration 2`, focused mode, under `HL-TFW_20260921-180000_RVAG.md@db61ecac1a7f0743036f84a5d5075ca727b5364c`.
> **Coordination authority**: `HL-TFW_20260921-180000_RVAG.md @ db61ecac1a7f0743036f84a5d5075ca727b5364c`
> **Originating proposer**: `none` — the research focus derives from approved HL §10, `research/iterations.yaml`, and predecessor RES open threads.

---

## Research Context

Iteration 2 attacked iteration 1's preferred one-verdict architecture rather than extending it by
default. It tested C4+ marginal decision power, mixed-round per-item routing, safety/security and
human-authority boundaries, sole-versus-redundant evidence identity, test/check admission,
new-carrier necessity and terminal-message failure behavior. It inspected only the accepted durable
AGSK landing, separated its Antigravity transport and `3.5.0` ownership from RVAG payload semantics,
and established the minimal post-AGSK implementation and later release surfaces.

## Briefing

The approved [Briefing](1_briefing.md) carried iteration-1 D1–D9 and all six open threads into three
focused stages. Gather mapped eight independent dimensions and five mixed-round cases. Extract built
nine representative configurations, formalized a per-item contract plus one aggregate verdict, fixed
the compact payload and derived a twelve-file semantic denominator. Challenge attacked every
survivor, including the Coordinator-requested wrong-route/stale-ref/duplicate/retry protocol case.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Select C1 as the surviving architecture: ordered `VALUE → ASSURANCE → TRACE` reasoning, classified per-item findings and one terminal verdict. | C1 passes mixed product/record, assurance-only, safety/security, human-authority, identity and non-code attacks without a second acceptance surface. |
| D2 | Make the finding—not the artifact or whole round—the unit of classification and payment. Each item records subject, claim/authority, fact+oracle, harm, material consequence, owner, completion condition, route and Candidate effect. | These fields make the Coordinator-required subject/consequence/owner/route executable and prevent discrepancy existence from becoming a return reason. |
| D3 | Let the highest required authority control sequence and the next authorized act, never recast every lower item. | A mixed round may need one ruler or one TS revision while record-only and assurance-only items retain their own routes and unchanged VALUE is not dragged into product execution. |
| D4 | Bind evidence applicability to `{accepted subject, revision/Candidate, relevant environment, oracle/authority, dependency state}`. | A false sole carrier is a material ASSURANCE gap; the same carrier is record-only when independent proof already establishes the same claim for the same tuple. |
| D5 | Replace `min_verify_ratio` and “any discrepancy → 100%” with a recorded claim/risk/dependency/environment/oracle selection and explicit limits. | Population ratios and blanket escalation do not identify the acceptance decision; risk-selected checks do, while safety/authority boundaries remain mandatory. |
| D6 | Admit a permanent guard only when it names protected behavior/invariant, failure consequence and relevant counterfactual detection; classify diagnostics, positive controls and governance assertions separately. | This rejects test-count gaming without deleting useful existing-contract tests that can demonstrate detection through a mutant, fault, fixture or equivalent negative control. |
| D7 | Fix one provider-neutral logical envelope: `REVIEW · <reviewer-unit> · <task-or-phase> · <verdict> · <review-artifact@ref>`, after durable REVIEW and authorized status/journal effect, to exact `coordinator_route`. | The message is a terse continuation signal, not narrative, evidence, authority or external-effect permission. |
| D8 | Make the envelope semantically idempotent by its exact tuple. Preflight route and immutable artifact/ref; duplicates are the same signal; only a provider-confirmed non-applied failure may use one provider-specific identical retry; ambiguous delivery is neither claimed nor blindly retried. | The contract must not invent exactly-once transport, second verdicts or duplicate lifecycle actions. RFC 9110 and provider delivery documentation corroborate the retry/acknowledgment boundary. |
| D9 | Preserve the accepted AGSK transport files unchanged. | AGSK already proves Antigravity UUID extraction, native addressed send and vertical role routing. The compact plain-text payload is compatible; no adapter, manifest, skill, migration-3.5.0 or release-history gap was found. |
| D10 | Fix the RVAG implementation Candidate at twelve existing files: canonical Review workflow; map/verify/judge and REVIEW templates; conventions; both config copies; Config workflow; glossary; and Claude full-copy Review/Config commands. | Every included file carries a live semantic or propagation obligation; all excluded adapter/Executor/root files already route to the canonical owner or satisfy the needed invariant. |
| D11 | Keep `3.5.1` preparation as a later post-acceptance release effect. | VERSION, config-version fields, CHANGELOG and a new `3.5.1` migration guide are release-owned; tag/push/publish/deploy/notify remain separately reserved. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Can C4+ change a safe authorized decision unavailable to one classified verdict plus visible observations? | Closed — no | If the record issue changes no conclusion/action it is a visible observation or finite record repair; if it does, it is material TRACE/ASSURANCE and changes the terminal verdict. |
| Q2 | How should mixed rounds avoid dragging unchanged VALUE onto the highest rung? | Closed | Classify and route each item first. Highest authority controls sequence/next act only; each item retains owner, completion, route and `candidate_effect`. |
| Q3 | What remains after accepted AGSK? | Closed for RVAG scope | Canonical Reviewer payload, ordering, semantic idempotence and the twelve-file semantic denominator remain. AGSK transport and `3.5.0` history stay untouched. |
| Q4 | Can other providers be credited with the same automatic return? | Closed by boundary | No. Codex and accepted AGSK/Antigravity are evidenced. Every other provider remains native, owner-assisted or unavailable based only on its own current mechanism and receipt semantics. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | One universal materiality predicate on every return is sufficient; a second verdict axis is unnecessary. | iteration-1 support; C4+ pending | 🟢 supported | [Extract E2–E3](3_extract.md#e2-one-aggregate-verdict-follows-item-classification-without-flattening-the-items); [Challenge C1/C5](4_challenge.md#c1-mixed-product-defect-plus-record-typo-does-not-drag-unchanged-items-upward). |
| H2 | Risk- and claim-selected verification can replace `min_verify_ratio` without increasing false approvals. | iteration-1 support with safety floor | 🟢 supported with explicit safety/authority floor | [Extract E5](3_extract.md#e5-verification-is-a-selection-argument-not-a-population-ratio); [Challenge C2/C3/C9](4_challenge.md#c2-assurance-only-failure-preserves-independently-established-value). |
| H3 | TRACE defects can be divided deterministically by whether they change authority, accepted-result identity, material proof or an authorized next action, while preserving FRATS transcript isolation and reproducibility. | iteration-1 support | 🟢 supported | [Extract E1/E4](3_extract.md#e1-a-finding-is-the-unit-of-classification-consequence-and-payment); [Challenge C4/C7](4_challenge.md#c4-sole-versus-redundant-false-evidence-changes-class-not-by-filename). |
| H4 | Test admission based on protected behavior, consequence and counterfactual detection removes test-count gaming without discarding valuable characterization tests. | iteration-1 support | 🟢 supported | [Extract E6](3_extract.md#e6-test-admission-needs-an-item-level-detection-argument); [Challenge C9](4_challenge.md#c9-ratio-removal-does-not-imply-weak-or-arbitrary-verification). |
| H5 | MFX is an instance of a recurring framework failure rather than an exceptional task-specific misuse. | iteration-1 support | 🟢 supported | Predecessor MFX evidence plus [Gather G3–G4](2_gather.md#g3-the-active-review-still-has-the-two-iteration-1-false-return-triggers); accepted AGSK Phase A approved the correct result despite a non-material RF arithmetic defect. |
| H6 | The necessary correction can subtract active rules and configuration rather than introduce a new artifact, registry or score. | iteration-1 support | 🟢 supported | [Extract E8](3_extract.md#e8-minimal-post-agsk-implementation-denominator-is-twelve-existing-files); [Challenge C6/C8](4_challenge.md#c6-new-carrier-and-non-code-attacks-remain-expressible-in-existing-files). |
| H7 | A detailed durable REVIEW plus one fixed compact addressed envelope is sufficient for reliable Coordinator continuation; AGSK may supply provider transport, while RVAG supplies the Reviewer-specific payload and value semantics without narrative duplication. | partial; accepted AGSK now available | 🟢 supported within evidenced provider bounds | [Extract E7](3_extract.md#e7-the-compact-terminal-payload-is-fixed-transport-remains-provider-owned); [Challenge C7](4_challenge.md#c7-payload-protocol-attack-requires-semantic-idempotence-not-a-second-verdict). |

## HL Update Recommendations

> **The researcher classifies, never applies or rules.** Refinements below target free sections only.
> Iteration 2 supports the frozen RVAG target as written—including one terminal envelope as one
> logical message identity—and proposes no change to §1 or §3–§7.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 Current State | Add the post-AGSK finding: Antigravity addressed transport is accepted and landed, while canonical Review still carries `min_verify_ratio`, blanket discrepancy escalation and mixed-round recasting that RVAG must replace. | Gather G2–G3 |
| R2 | §7.2 Knowledge Citations | Add bounded external corroboration: NIST SP 800-53A for risk-tailored depth, SLSA source/provenance only for result/revision identity, GitHub Checks/SARIF only as existence examples for aggregate signal plus item detail, and RFC 9110/provider delivery docs only for semantic-idempotence/retry boundaries. Import no external control set or transport guarantee. | Gather G5; Extract E5/E10; Challenge C7 |
| R3 | §8 Dependencies | Mark both configured research iterations complete; close the AGSK sequencing dependency through accepted `v3.5.0` commit `16cbb8f845511c68b55cfa3e57c12e32116253a2`; preserve AGSK transport files and separate later `3.5.1` preparation. | Gather G2; Extract E7–E9; Challenge C8 |
| R4 | §9 Risks | Add terminal-signal risks: wrong route, stale/unresolved REVIEW ref, duplicate delivery, retry after confirmed failure and ambiguous delivery. Mitigate with route/ref preflight, exact logical tuple, duplicate-no-op semantics, provider-specific bounded identical retry only after confirmed non-application, and no exactly-once claim by analogy. | Challenge C7 |
| R5 | §10 RESEARCH Case | Close H1–H7 as supported within evidenced provider bounds; record C1 as survivor, C3 only as reasoning order, and eliminate C4+, ratio/escalation, scores/registries, new carriers and adapter payload duplication. | Challenge Consistency Check/C10 |
| R6 | §10 RESEARCH Case | Record the exact twelve-file post-AGSK semantic denominator and the separate release-owned paths/effect; no Antigravity transport, thin Review skill, manifest, Handoff or root coordination edit is justified. | Extract E8–E9; Challenge C8 |
| R7 | §11 Strategic Insights | Add that mixed rounds require two independent operations: per-item semantic route first, aggregate authority sequence second. “Highest rung controls the round” may order the next act but may not reclassify lower items or move unchanged VALUE. | Extract E1–E3; Challenge C1–C2 |
| R8 | §11 Strategic Insights | Add that exactly-one return is a logical envelope identity, not a universal exactly-once transport claim; a byte-identical bounded retry is provider-specific and never a second verdict or effect. | Extract E7; Challenge C7 |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

**No amendment proposals.** The frozen target already requires ordered VALUE/ASSURANCE/TRACE
judgment, material consequences, protected authority/safety, one durable REVIEW and one compact
terminal envelope. Iteration 2 resolves implementation semantics without changing those claims.

## Fact Candidates

No fact candidates. Conversation review found no new human-only project fact; the Coordinator's
gates clarified the approved research attack and payload boundary, while every material project fact
was independently discoverable in the frozen contract, accepted artifacts, repository or provider
evidence.

## Strategic Insights (Research)

No strategic insights. The Coordinator supplied workflow direction within the approved iteration,
not new human-only domain knowledge or a strategic correction to the project purpose.

## Findings Map

```text
accepted result + frozen purpose + exact authority
                         │
                         ▼
             map material claims and risks
                         │
                         ▼
       verify subject · revision · environment
              oracle/authority · dependencies
                         │
                         ▼
               classify EACH finding
          ┌──────────────┼──────────────┐
          │              │              │
        VALUE        ASSURANCE        TRACE
          │              │              │
    wrong purpose/   material claim   changes authority,
    behavior/safety  unestablished?    identity, proof,
          │              │             safety or action?
          └───────┬──────┴──────┬──────┘
                  │             │
           material item     non-material TRACE
                  │             │
       claim · fact/oracle       └─ finite record repair/
       harm · consequence           observation
       owner · completion              Candidate preserved
       route · Candidate effect
                  │
                  ▼
      highest authority orders the next act
      (never reclassifies the other items)
                  │
                  ▼
          one terminal REVIEW verdict
                  │
      durable REVIEW + status/journal first
                  │
                  ▼
 REVIEW · unit · task/phase · verdict · artifact@ref
       exact coordinator_route · one logical tuple
       duplicate=no new act · retry only if provider
       confirms non-application · ambiguity unclaimed
```

## Iteration Status

- **Iteration:** 2 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (supported), H2 (supported with safety/authority floor), H3 (supported), H4 (supported), H5 (supported), H6 (supported), H7 (supported within evidenced provider bounds)
- **Hypotheses deferred:** None. Other-provider automatic return remains outside the claim, not a deferred RVAG assumption.
- **Gaps discovered:** No research gap. Exact TS selector syntax, acceptance criteria, evidence plan and implementation authority are Coordinator planning work; they do not require another research iteration.
- **Superseded decisions:** D1/D3/D8 supersede iteration-1 D8 by eliminating C4+ as a stored alternative while retaining C3's reasoning order; D7–D10 supersede iteration-1 D9 by closing H7 against accepted AGSK and fixing the payload/protocol/denominator.

### Open Threads (for next iteration)

No open threads.

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [ ] **MORE NEEDED** — no additional research iteration is justified
- [ ] **BLOCKED** — no research blocker remains

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 2 tried to break iteration 1 and instead narrowed it. One ordered
VALUE→ASSURANCE→TRACE judgment is sufficient when every finding carries a material consequence,
owner, completion route and explicit Candidate effect; the highest authority controls sequence but
never turns lower items into product work. C4+, scores, ratios, blanket escalation, new carriers and
adapter payload duplication add no safe decision. Accepted AGSK closes Antigravity transport, leaving
one exact canonical envelope and twelve existing semantic/propagation files for RVAG; `3.5.1`
preparation remains a later release effect. What would have been missed without iteration 2 is the
mixed-round separation between authority ordering and semantic routing, the sole-versus-redundant
evidence classification, and the need for semantic idempotence without claiming exactly-once
delivery. Self-critique: the transport attack is necessarily bounded to the exposed Codex mechanism
and accepted AGSK evidence; no claim is made for unevidenced providers.

### Material handover at this return

**Producer and unit:** Codex Researcher,
`codex:thread:local:01a0c7dd-94bf-78b2-82ba-b14da2e7778a`, returning materially only to
`codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5` under `tfw-gates-only`.

**Bounded source/epoch:** RVAG Contract Baseline
`db61ecac1a7f0743036f84a5d5075ca727b5364c`; inspected framework HEAD
`5815317f8906f5a46bef9fa5f5cb397ff29f1b32`; task status/journal/HL/iteration contract; predecessor
iteration-1 RES and its open threads; current canonical Review/templates/config/conventions/glossary,
thin/full-copy adapter topology and project release contract; accepted AGSK task/phase statuses,
independent REVIEWs, closure `7cb2991`, Candidates `68dd9ce`/`bde7334`, accepted landed messaging
files and tagged `v3.5.0` commit `16cbb8f845511c68b55cfa3e57c12e32116253a2`; primary NASA,
NIST, SLSA, IETF, OASIS, GitHub and provider delivery sources cited in stage files. No live peer
transcript, unaccepted AGSK draft/RF reasoning or private role context was used.

**Material result:** H1–H7 are supported within evidenced provider bounds. C1 is the survivor;
per-item findings precede one aggregate verdict, claim/risk/oracle selection replaces file ratios,
detection power replaces test presence/count, and semantic idempotence bounds the compact addressed
return. The exact RVAG implementation denominator is twelve existing files; accepted AGSK transport
is preserved; later `3.5.1` preparation is separate. No frozen amendment or new carrier is justified.

**Uncertainty and continuation:** Unevidenced providers receive no native/exactly-once claim. The
Coordinator should run `/tfw-plan`, apply or reject the free-section refinements, translate D1–D11
into the TS and exact evidence plan, and preserve the post-acceptance release boundary. No Fact
Candidate, knowledge publication, owner ruling or further research iteration is owed from this unit.

---

*RES — TFW_20260921-180000_RVAG: Reviewer Value-Assurance Gate | 2026-09-22*
