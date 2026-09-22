# RES — TFW_20260921-180000_RVAG: Reviewer Value-Assurance Gate

> **Current filename**: fixed `research/iter1/RES.md` under the selected task; no task-root `RES__*` is issued.

> **Date**: 2026-09-22
> **Author**: Codex Researcher
> **Status**: 🔬 RES — Iteration 1 complete
> **Parent HL**: [HL-TFW_20260921-180000_RVAG](../../HL-TFW_20260921-180000_RVAG.md)
> **Mode**: Pipeline — focused
> **Producer unit**: `codex:thread:local:01a0c7ba-6045-7ab0-b261-11cec3ca1af5`
> **Parent Coordinator**: `codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5`
> **Activation / dispatch source**: Direct native dispatch from the Parent Coordinator for Researcher role on `TFW_20260921-180000_RVAG`, iteration 1; exact `/tfw-research RVAG iter 1` activation and stage gates under `HL-TFW_20260921-180000_RVAG.md@db61ecac1a7f0743036f84a5d5075ca727b5364c`.
> **Coordination authority**: `HL-TFW_20260921-180000_RVAG.md @ db61ecac1a7f0743036f84a5d5075ca727b5364c`
> **Originating proposer**: `none` — the research focus derives from approved HL §10 and `research/iterations.yaml`.

---

## Research Context

Iteration 1 reconstructed the MFX review loop, mapped the active Reviewer verdict, verification,
test-admission, TRACE and return rules, and contrasted false returns with material product, purpose,
authority, safety/security and assurance failures. It tested whether one universal materiality
predicate plus class-selected correction routes can preserve rigorous independent review without a
second score, artifact, registry or product-execution loop for record-only defects. The work also
separated RVAG's Reviewer payload/value semantics from AGSK's provider transport; AGSK Phase B was
still unaccepted at `RF`, so its live result was not consumed.

## Briefing

The approved [Briefing](1_briefing.md) scoped three stages: Gather durable MFX and contrasting cases;
Extract the minimum discriminators and post-AGSK surface; Challenge false approval, false return,
test deletion, safety/authority weakening and bureaucratic growth. The Coordinator selected focused
mode and preserved iteration 2 as the separate adversarial pass.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Carry C11/C3+ forward as the iteration-1 preferred architecture: `VALUE → ASSURANCE → TRACE` feeds one terminal verdict, with safety/security explicit. | It classifies MFX, TLD, CRATM, FRATS, wrong-purpose output and the four boundary cases correctly without a second acceptance authority or score. |
| D2 | A blocking finding must name subject/authority, observed fact and oracle, concrete harm, material consequence, and completion route. | A breached citation or criterion alone cannot distinguish an immaterial record error from a failed accepted claim; the five elements do. |
| D3 | Verification depth should follow material claims, risk/criticality, affected behavior/dependencies, actual environment, oracle/authority and evidence gaps. | ISO/NIST sources and local contrasts support claim/risk selection; file population and blanket 100% escalation do not identify the decision that evidence must support. |
| D4 | TRACE blocks only when it changes authority, accepted-result identity, material proof, safety/security provenance, or an authorized next action. | CRATM and wrong-Candidate cases remain blocking; MFX counts, labels and independently superseded citations receive finite record-only handling. |
| D5 | Permanent guards require a protected behavior/invariant, failure consequence, and demonstrated relevant counterfactual detection. | Historical red-before-green remains strong for corrected behavior; targeted mutants, fault injection, external fixtures and similar negative controls preserve useful existing-contract tests. |
| D6 | Correction route is selected by the failed subject, not by artifact path or the existence of a discrepancy. | Product/spec/contract defects keep existing rungs; assurance-only gaps preserve Candidate when VALUE is unchanged; reconstructable record-only defects use finite current-carrier repair. |
| D7 | Use existing REVIEW and stage carriers; add no score, registry, stage, artifact or permanent suite. | Every challenged case can be represented in current findings, verdict, rung and recovery structures. |
| D8 | Keep C4+ as an explicit iteration-2 alternative only. | A separate record-health judgment is logically sound but showed no marginal decision power and risks drift or confusion with human acceptance authority. |
| D9 | Keep H7 partial until the accepted AGSK Phase B result lands and is rebased. | RVAG can define compact Reviewer payload/timing/value semantics now, but cannot infer Antigravity transport or the final overlap from an unaccepted RF. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Can a separate record-health judgment change any safe decision that one classified verdict plus visible observations cannot express? | Open — iteration 2 | No such case was found in iteration 1; C4+ remains the counter-hypothesis. |
| Q2 | How should mixed rounds combine product, assurance-only, authority and record-only findings without letting the highest route drag every item into product execution? | Open — iteration 2 | Route each item by subject, then test whether the current highest-rung mixed-round rule needs a bounded exception for evidence/record-only items. |
| Q3 | What exact terminal-return and adapter surface remains after accepted AGSK Phase B landing? | Blocked on durable dependency | Consume only the independently accepted landing; do not read live transcript or unaccepted RF. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | One universal materiality predicate on every return is sufficient; a second verdict axis is unnecessary. | open | 🟢 supported for iteration 1 | [Challenge C1–C8](4_challenge.md#findings); C11/C3+ pass all cases, while C4+ adds no demonstrated decision power. |
| H2 | Risk- and claim-selected verification can replace `min_verify_ratio` without increasing false approvals. | open | 🟢 supported with explicit safety/security floor | [Gather G3–G4](2_gather.md#g3-contrasting-returns-show-why-trace-and-assurance-cannot-become-non-blocking-by-default); [Extract E4](3_extract.md#e4-verification-depth-follows-claims-and-risk-not-artifact-population); [Challenge C1/C3](4_challenge.md#c1-unsafe-but-functionally-correct-defeats-a-functionality-only-value-test). |
| H3 | TRACE defects can be divided deterministically by whether they change authority, accepted-result identity, material proof, or an authorized next action, while preserving FRATS transcript isolation and reproducibility. | open | 🟢 supported; safety/security provenance made explicit | [Extract E2–E3/E6](3_extract.md#e2-the-case-matrix-yields-a-deterministic-finding-taxonomy); [Challenge C2–C4](4_challenge.md#c2-a-correct-result-cannot-legitimize-an-unauthorized-external-effect). |
| H4 | Test admission based on protected behavior, consequence, and counterfactual detection removes test-count gaming without discarding valuable characterization tests. | open | 🟢 supported | [Gather G4](2_gather.md#g4-external-sources-support-claimriskoracle-selection-but-not-a-new-universal-score); [Extract E5](3_extract.md#e5-assurance-is-a-traceable-relation-not-a-volume-score); [Challenge C6](4_challenge.md#c6-test-deletion-and-metric-substitution-attacks). |
| H5 | MFX is an instance of a recurring framework failure rather than an exceptional task-specific misuse. | open | 🟢 supported | MFX reconstructed in [Gather G2](2_gather.md#g2-mfx-is-a-repeated-false-return-class-not-a-single-careless-review) and matched `knowledge/process.md` F31/F32; TLD/CRATM/FRATS delimit legitimate returns. |
| H6 | The necessary correction can subtract active rules and configuration rather than introduce a new artifact, registry or score. | open | 🟢 supported | [Extract E7](3_extract.md#e7-candidate-minimal-change-surface-uses-existing-carriers); [Challenge C7](4_challenge.md#c7-bureaucratic-growth-attack-leaves-no-need-for-a-new-carrier). |
| H7 | A detailed durable REVIEW plus one fixed compact addressed envelope is sufficient for reliable Coordinator continuation; AGSK may supply provider transport, while RVAG supplies the Reviewer-specific payload and value semantics without narrative duplication. | open | 🟡 partial — semantic sufficiency supported; transport pending | [Extract E7](3_extract.md#e7-candidate-minimal-change-surface-uses-existing-carriers); [Challenge C5/C8](4_challenge.md#c5-human-acceptance-authority-survives-every-configuration); AGSK Phase B remained `RF`. |

## HL Update Recommendations

> **The researcher classifies, never applies or rules.** Refinements below target free sections only.
> The frozen RVAG contract already contains the materiality, safety/security, test-admission,
> record-only and compact-return outcomes supported by iteration 1, so no frozen change is proposed.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 Current State | Add the reproducible MFX measurement method and scope: 35 commits in `1e1dcc6..95085d0`, two foreign UPM commits, therefore 33 MFX commits; 31 task-trace commits; per-commit trace churn +3,986/−250; zero later commits under `code/mcp-plugin/src/` and `k8s/`. | Gather G2 |
| R2 | §2 Current State | State the architectural defect precisely: current Review distinguishes evidence existence/sufficiency but one scalar return and blanket discrepancy escalation do not require a shared material-consequence predicate or a record/evidence-only correction route. | Gather G1; Extract E1/E6 |
| R3 | §7.2 Knowledge Citations | Add external corroboration with bounded scope: ISO/IEC/IEEE 29119-1 for risk-based selection and oracle/test-basis importance; NISTIR 7608 for claim→argument→evidence; NIST SP 800-171A for no required artifact/method count; NASA-STD-8739.8B for intended/unintended behavior and explicit safety/security; SLSA only as an identity-binding example; Papadakis et al. only as evidence against mutation-score substitution. | Gather G4; Extract E4/E5; Challenge C1/C3 |
| R4 | §8 Dependencies | Record that AGSK Phase B remained at `RF` throughout iteration 1; its live result was not consumed. Preserve the accepted-landing/rebase gate before final TS denominator, overlap and provider claims. | Gather G5; Extract E7; Challenge H7 |
| R5 | §9 Risks | Add the boundary risk that “materiality” could be misused to waive safety/security, unauthorized external effects, wrong Candidate/environment identity, or human acceptance authority; require these as explicit material boundaries. | Challenge C1–C5 |
| R6 | §9 Risks | Add the opposite risk: a second record-health judgment may drift from the terminal verdict or be mistaken for another acceptance authority; iteration 2 must prove marginal decision power before adopting C4+. | Challenge unexpected survivor/C7 |
| R7 | §10 RESEARCH Case | Update H1–H6 to “supported for iteration 1, pending iteration-2 adversarial confirmation”; update H7 to “partial — semantic envelope supported, exact provider transport pending accepted AGSK landing.” | Challenge C8; hypothesis table above |
| R8 | §10 RESEARCH Case | Set iteration 2 focus to mixed-round routing, C4+ marginal-power attack, safety/security and human-authority counterexamples, record-vs-assurance ambiguity, and accepted AGSK overlap/provider evidence. | Open Questions Q1–Q3; Iteration Status below |
| R9 | §11 Strategic Insights | Add that the smallest sound change is semantic subtraction: universal material consequence, claim/risk/oracle depth, detection-power admission, and class-selected routes in existing carriers; transport does not repair verdict semantics. | Extract E1/E3–E7; Challenge C7 |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

**No amendment proposals.** Iteration 1 supports the frozen §1, §3–§7 claims as written and found no
evidence, cost, or considered alternative that requires changing them.

## Fact Candidates

No fact candidates. Conversation review found no new human-only project fact; Coordinator gates and
durable artifacts supplied workflow direction and reproducible evidence, not human-only knowledge.

## Strategic Insights (Research)

No strategic insights. No human provided new domain knowledge, correction or strategic context in
this Researcher task; all material synthesis derives from approved artifacts, durable cases and
external sources.

## Findings Map

```text
accepted result + frozen purpose + actual authority
                      │
                      ▼
            classify the reviewed subject
          ┌───────────┼────────────┐
          │           │            │
        VALUE      ASSURANCE      TRACE
          │           │            │
   purpose/domain   material     does it change
   behavior/safety  claim bound   authority · result identity
   or security      to actual     material proof · safety/security
          │          result?       provenance · next action?
          │           │            │
      no / unsafe   no / gap     yes             no
          │           │            │               │
          └──────┬────┘        material       record-only
                 │             TRACE              │
                 ▼               │                ▼
      five-field material finding│       finite current-carrier
      claim · fact/oracle · harm  │       correction/observation
      consequence · route        │       Candidate unchanged
                 │               │
                 └───────┬───────┘
                         ▼
        product / evidence / ruler-specific route
                         │
                         ▼
             one durable REVIEW verdict
                         │
                         ▼
       one compact addressed envelope after recording
       (signal only; no authority or external effect)
```

The map explains why MFX loops: current flow jumps from “record discrepancy” directly to the shared
return route, bypassing both the material-consequence decision and the correction-class branch.

## Iteration Status

- **Iteration:** 1 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (supported, not final), H2 (supported with safety floor), H3 (supported), H4 (supported), H5 (supported), H6 (supported), H7 (partial)
- **Hypotheses deferred:** H7 provider transport/final overlap — accepted AGSK Phase B landing was unavailable; H1 final disposition — C4+ remains an explicit iteration-2 counter-hypothesis
- **Gaps discovered:** mixed rounds may let the highest product/spec rung drag evidence-only or record-only items into execution; no sampled case proves a second record-health judgment adds decision power; exact provider transport and change surface wait for accepted AGSK; provider-native evidence remains provider-specific
- **Superseded decisions:** None. Configuration families were research alternatives, not governing decisions.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | C11/C3+ versus C4+ | A second judgment may expose record health or merely create another drifting acceptance surface. | Construct a case where record state changes a safe authorized decision without changing VALUE/ASSURANCE/material TRACE; eliminate C4+ if none exists. |
| 2 | Mixed material and non-material findings | Current highest-rung routing may over-route record/evidence-only items with a real product defect. | Replay mixed rounds and specify per-item disposition plus one executable round without dragging unchanged VALUE. |
| 3 | Safety/security and human authority | A loose “materiality” rule could become discretion to waive severe but low-frequency harm or accept risk without authority. | Attack with unsafe-but-functional, privacy/security, irreversible effect and owner-reserved acceptance cases. |
| 4 | Evidence identity and citation ambiguity | The same false carrier can be record-only or a material assurance gap depending on independent proof. | Vary Candidate/environment/oracle identity and sole-versus-redundant evidence support. |
| 5 | Accepted AGSK landing and provider return | H7 and exact file denominator cannot close by analogy or from an unaccepted RF. | After independent acceptance/landing, rebase, inspect durable result, remove overlap, and test compact payload versus transport across evidenced providers. |
| 6 | New-carrier counterexample | Iteration 1 found no need for a score, registry, stage or artifact. | Actively search for a domain or mixed case that cannot be represented in existing REVIEW/stage/rung/recovery carriers. |

### Recommendation
- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [x] **MORE NEEDED** — run mandatory iteration 2 to challenge C4+, mixed routes, safety/authority boundaries, evidence identity, and the accepted AGSK overlap
- [ ] **BLOCKED** — no iteration-1 research blocker; only H7's transport branch waits on the declared dependency

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 1 shows that MFX is a structural false-return pattern: one verdict route lacks a universal
material-consequence predicate and sends product, assurance and record correction through the same
loop. Contrasting durable cases prove that rigor must remain strong for wrong purpose/behavior,
safety/security, authority, result identity and material proof. The smallest supported architecture
uses one ordered VALUE→ASSURANCE→TRACE judgment, a five-element blocking finding, claim/risk/oracle
verification, detection-power test admission and class-selected routes in existing carriers. What
would have been missed without research is the evidence-only branch, the same surface defect changing
class based on independent proof, and the fact that transport-only or ratio-only changes do not solve
false returns. Self-critique: focused iteration 1 used a bounded case set and could not inspect an
accepted AGSK landing; iteration 2 must try to break the one-verdict result before planning freezes it.

### Material handover at this return

**Producer and unit:** Codex Researcher,
`codex:thread:local:01a0c7ba-6045-7ab0-b261-11cec3ca1af5`, returning materially only to
`codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5` under `tfw-gates-only`.

**Bounded source/epoch:** RVAG Contract Baseline
`db61ecac1a7f0743036f84a5d5075ca727b5364c`; framework HEAD
`8528730c46f74df5f8e881c658ff5e419bfb92d9`; task status/journal/HL/iteration contract; current Review
workflow/templates/config and canonical status/REVISE/recovery rules; Helpdesk MFX Git range
`1e1dcc6..95085d0` plus REVIEW revisions 1–4; durable TLD, CRATM Phase C and FRATS Phase B reviews;
selected current knowledge relations; external ISO, NIST, NASA, SLSA and ICSE sources cited in stage
files. No live peer transcript, unaccepted AGSK RF or private reasoning was used.

**Material result:** H1–H6 receive iteration-1 support. One explicit safety-aware verdict architecture
can distinguish material VALUE/ASSURANCE/TRACE failures from reconstructable record-only defects;
verification and tests follow claims, risk, oracle and detection power; correction routes preserve
Candidate identity whenever VALUE is unchanged. No frozen HL change or new carrier is justified.

**Uncertainty and continuation:** H1 remains non-final because C4+ survives logically; H7 remains
partial because AGSK Phase B has not been independently accepted and landed. The Coordinator should
open iteration 2 under the existing sequential contract, carrying the six open threads above. No
human-only Fact Candidate or knowledge publication is owed from this iteration.

---

*RES — TFW_20260921-180000_RVAG: Reviewer Value-Assurance Gate | 2026-09-22*
