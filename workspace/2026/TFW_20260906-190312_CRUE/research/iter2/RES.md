# RES — TFW_20260906-190312_CRUE: Clear Release and Update Experience — Independent prompt-native reframing

> **Date**: 2026-09-06
> **Author**: Codex, iter2 Researcher, on behalf of saubakirov
> **Status**: 🔬 RES — Iteration 2 complete
> **Parent HL**: [HL-TFW_20260906-190312_CRUE](../../HL-TFW_20260906-190312_CRUE.md)
> **Mode**: Pipeline

---

## Research Context

This independent pass tested H4 from first principles: how to design the release/update contract when the operational reader is an AI agent interpreting language, context, evidence, uncertainty, and authority, while the beneficiary is a person continuing work on their own project. It did not read iteration 1 or begin from the Coordinator's fix list. External mechanisms were gathered first, four prompt-native configurations were compared on the same scenarios, and only then were they challenged against immutable TFW 2.2.0 source `8e68ab37d300122ff110500ad58f354f76b6210f`. The result is a design-level candidate, not an implemented or behaviorally verified solution.

## Briefing

The full intake, dimension model, falsifiers, and independence boundary are in [1_briefing.md](1_briefing.md). The pass treated prompt structure as an interpretive specification rather than executable enforcement; separated source, project, agent, receiver, and comprehension evidence; and admitted a negative H4 result if no simpler complete alternative survived.

## Sources

| Source | Contribution and limit |
|---|---|
| [OpenAI, “Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions”](https://openai.com/index/instruction-hierarchy-challenge/) | Supports explicit authority ordering and adversarial conflict cases; does not prove a TFW prompt will follow them reliably. |
| [OpenAI, “Inside our approach to the Model Spec”](https://openai.com/index/our-approach-to-the-model-spec/) | Supports compact boundaries, defaults, rubrics, contrastive examples, and scenario evaluation; explicitly treats the specification as an interface, not an implementation. |
| [Bai et al., “Constitutional AI”](https://arxiv.org/abs/2212.08073) | Shows principles and feedback can shape model behavior; it is a training-method result, not evidence that Markdown alone enforces TFW behavior. |
| [Anthropic, “Many-shot jailbreaking”](https://www.anthropic.com/research/many-shot-jailbreaking) | Counterevidence to “more examples is safer”: long example contexts can amplify an unwanted pattern. |
| [Anthropic, “Demystifying evals for AI agents”](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Supports grading trajectory and outcome separately, multiple trials, isolated state, and calibrated graders. |
| [Liu et al., “Lost in the Middle”](https://aclanthology.org/2024.tacl-1.9/) | Supports the risk that important instructions become less usable by position in long context; it does not identify an optimal TFW prompt layout. |
| [RFC 9110, §§9.2.1–9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#name-common-method-properties) and [Garcia-Molina & Salem, “Sagas”](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf) | Supply bounded analogies for observed-state retry, idempotence, and semantic compensation; neither implies atomic rollback for project updates. |
| [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) and [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Support claim-scoped evidence, deployment-like evaluation, and explicit measurement limits. |
| [Amershi et al., “Guidelines for Human-AI Interaction”](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf) and [Reicherts et al., CHI 2025](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/03/AI-Help-Me-Think-CHI-2025.pdf) | Support consequence-aware communication and correction while challenging the assumption that explanation alone improves calibrated reliance or comprehension. |
| [Dhanorkar, Passi & Vorvoreanu, FAccT 2026](https://arxiv.org/abs/2606.05391) | Provides qualitative counterevidence that more pre-configuration and review necessarily yield effective oversight; the small, mostly single-company sample is not evidence about TFW owners. |
| TFW 2.2.0 at `8e68ab37d300122ff110500ad58f354f76b6210f`: [update workflow](../../../../../.tfw/workflows/update.md), [briefing template](../../../../../.tfw/templates/briefing.md), [migration 2.2.0](../../../../../.tfw/migrations/2.2.0.md), [release workflow](../../../../../.tfw/workflows/release.md), [adapter manifest](../../../../../.tfw/adapters/manifest.yaml), and targeted [repository test](../../../../../.tfw/scripts/test_gen_index.py) | Immutable baseline used only in Challenge. Local links show the current checkout path; all reported baseline observations were obtained from the named Git object with `git show`, `git grep`, or `git ls-tree`. |

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Retain C1, the Constitutional Interpreter, only as a specification layer. | A small set of invariants, defaults, a materiality rubric, and scarce contrastive examples gives the agent an authority vocabulary, but written principles are neither enforcement nor a complete update mechanism. |
| D2 | Reject C2, the Evidence-Gated Protocol, as a standalone controlling architecture. | The released workflow already has ordered stages. A second protocol/state machine would duplicate them and can recreate checklist ritual. Explicit entry/exit conditions, source-before-project ordering, re-observation before replay, and trajectory-plus-outcome evidence remain necessary inside the existing workflow. Narrative prose is not inherently incompatible with recovery; the failure arises when conditions and recovery state are not named and retrievable. |
| D3 | Reject C3, the Outcome-Backward Case, as a standalone controlling architecture; retain its final projection. | User-visible claims cannot safely define the technical workload because they may omit invisible integrity work. After the mandatory integrity envelope, `benefit / actual outcome / material limitation / next action` is a useful owner interface. |
| D4 | Revise C4 into C4-R and make one semantic effect its unit. | A file or shell action can combine differently owned effects. Effects may share a decision only when authority source, project owner, reversibility, proof, and outcome meaning all match; otherwise they split. |
| D5 | Treat C4-R as a short decision grammar, not a mandatory six-field printout and not a request to expose hidden chain-of-thought. | The contract needs inspectable bases, authorized actions, and evidence, persisted when material. Routine internal application of the grammar need not appear in the owner message or as one record per file. |
| D6 | Attach owner questions to unresolved semantic authority or consequence, not to file collision or technical discovery. | Established framework policy, project evidence, and an approved meaning-preserving migration can settle an effect. Ask only for competing authorities, ambiguous designation, irreversible loss, or genuinely new project behavior. |
| D7 | Use claim-specific references to authoritative sources and observed results; do not add a mutable claim or state registry. | Source truth, receiver state, project checks, agent trajectory, and owner comprehension are distinct. One authoritative task-local update trace can connect material evidence, but its exact existing carrier and archive boundary remain a planning/TS dependency. |
| D8 | Give H4 only a limited positive verdict. | C1 + C4-R + a mandatory integrity envelope + C3's output projection is conceptually simpler than incremental defect-led architecture or a second state machine. No comparative run measured reading cost, reliability, implementation size, or comprehension. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Which existing task-local trace is the single authoritative carrier for immutable source, preserved decisions, material effects, proofs, unresolved items, and continuation, and when is it archived? | Open — TS dependency | TFW 2.2.0 refers to an update checklist but does not name a canonical durable location or form. Planning must select the carrier without creating a duplicate project-state registry. |
| Q2 | What exact prospective transition preserves legacy project-specific `.tfw/README.md` material and its meaning while installing the framework-owned methodology document? | Open — TS dependency | The approved HL settles the ownership policy but intentionally leaves the transition mechanism to the task. It must distinguish relocation/preservation from ambiguous or competing project-purpose authority. |
| Q3 | What behavioral fixtures, agent/harness combinations, graders, and thresholds are sufficient to support claims about materiality decisions, interruption recovery, unsupported completion, and owner comprehension? | Open — TS and evaluation dependency | Static text checks can verify carrier consistency, not agent or user behavior. The design must predeclare representative cases, isolate state, inspect trajectory and outcome, and qualify the observed environment. |
| Q4 | How will adapter authority, retired vocabulary, payload integrity, repository checks, and receiver-project checks be reconciled into one mandatory integrity envelope? | Open — TS dependency | The baseline exposes contradictions between declared topology, shipped paths, live wording, and starter-specific tests. They must be resolved coherently rather than treated as equivalent evidence. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H4 | An independent prompt-native reframing can yield a simpler complete approach than incremental repair of the existing procedure. If no alternative survives challenge, retain that negative result rather than manufacture novelty. | needs-research | 🟡 Provisionally supported at design level; not empirically verified | [Extract configuration comparison](3_extract.md#configuration-space), [Challenge survivor ledger](4_challenge.md#c6--survivor-and-rejection-ledger), and [limited verdict](4_challenge.md#c7--limited-h4-verdict). Simplicity is an analytical hypothesis about control structure, not a measured gain. |

## HL Update Recommendations

> **The researcher classifies, never applies or rules.** Each recommendation names its HL section.
> Refinements target free sections (§2, §7.2, §8–§11); Amendment Proposals target frozen sections
> (§1, §3–§7). The Coordinator transcribes the latter into §12 as `PROPOSED`, preserving origin, then
> routes by `conventions.md` → `HL Contract` rule 8. Frozen claims wait for a valid terminal verdict.
> Use §3's declarative-claim granularity and §15 Role Lock. Empty class: **No refinements.** /
> **No amendment proposals.**

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 | Add the immutable 2.2.0 findings that the strong existing pin/classify/preserve/verify structure coexists with an unconditional three-question gate, per-file approval surface, briefing/migration contradiction, manifest/installed-root mismatch, live retired wording, starter-specific repository test, and no named durable update-record carrier. Keep observations scoped to the release object, not current master. | Codex, iter2 Researcher · [Challenge C1](4_challenge.md#c1--released-220-already-contains-useful-mechanisms-but-they-do-not-form-a-coherent-agentuser-contract) |
| R2 | §7.2 | Add the primary-source basis and its limits: instruction hierarchy and Model Spec for authority/rubrics; agent evals, NIST, and long-context evidence for scoped behavioral proof; RFC/Sagas for bounded recovery analogies; HAI and oversight studies for communication/attention counterevidence. Do not cite any as proof of TFW behavior. | Codex, iter2 Researcher · [Gather findings](2_gather.md#findings) and [Challenge C5](4_challenge.md#c5--external-evaluation-attack-a-plausible-walkthrough-is-not-a-behavioral-result) |
| R3 | §8 | Make three design dependencies explicit before implementation: one authoritative existing task-local update-trace carrier with archive boundary; a meaning-preserving legacy `.tfw/README.md` transition; and bounded behavioral proof across declared agent/harness scenarios. Also retain adapter and receiver-verification reconciliation inside the integrity dependency. | Codex, iter2 Researcher · [Challenge C4](4_challenge.md#c4--c4-must-split-semantic-effects-before-it-can-group-actions) and [C5](4_challenge.md#c5--external-evaluation-attack-a-plausible-walkthrough-is-not-a-behavioral-result) |
| R4 | §9 | Add risks that a compact grammar becomes uninspectable hidden reasoning, a grouped file action hides a differently owned semantic effect, final-message design omits invisible integrity work, and a second protocol duplicates existing stages. Clarify that narrative prose itself is compatible with checkpoints/recovery when its entry, exit, observation, and recovery conditions are explicit and retrievable. | Codex, iter2 Researcher · [Challenge consistency check](4_challenge.md#consistency-check), [C3](4_challenge.md#c3--c3-may-shape-communication-but-cannot-choose-the-integrity-work), and [C4](4_challenge.md#c4--c4-must-split-semantic-effects-before-it-can-group-actions) |
| R5 | §10 | Record H4 as **provisionally supported at design level; not empirically verified**. Describe the candidate as C1 specification layer + C4-R semantic-effect decision grammar + mandatory integrity envelope + downstream C3 projection. Preserve the falsifier: if planning cannot define the legacy transition, trace carrier, and behavioral evidence, the honest result is “no verified simpler alternative.” | Codex, iter2 Researcher · [Challenge C7](4_challenge.md#c7--limited-h4-verdict) |
| R6 | §11 | Add four research-derived implications: the minimal control unit is a semantic effect, not a file/action; owner attention follows unresolved authority/consequence rather than topology; owner communication is a downstream evidence projection rather than a scope authority; and conceptual simplicity cannot be claimed as behavioral or maintenance improvement without measurement. | Codex, iter2 Researcher · [Challenge C2–C7](4_challenge.md#findings) |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

**No amendment proposals.** The surviving design is compatible with the frozen vision, boundaries, phase, DoD/DoF, and principles. This pass proposes no change to an approved claim.

## Fact Candidates

**No fact candidates.** No human supplied new project facts during this independent pass. All project observations were discoverable from the approved HL, repository sources, or commands and therefore fail the Human-Only Test.

## Strategic Insights (Research)

**No strategic insights.** The pass received no new human briefing beyond the already recorded HL; its novel conclusions are researcher-derived and are routed as §11 refinement R6 rather than misclassified as human-sourced knowledge.

## Findings Map

```text
Primary evidence + counterevidence
              │
              ├── C1: invariants / defaults / rubric / scarce examples
              │          └── survives as specification, not enforcement
              │
              ├── C2: second evidence state machine
              │          └── rejected standalone
              │              retain named entry/exit evidence in existing workflow
              │
              ├── C3: outcome-backward scope
              │          └── rejected standalone
              │              retain BENEFIT / OUTCOME / LIMITATION / NEXT after proof
              │
              └── C4 → C4-R: one semantic effect
                         OBSERVED → AUTHORIZED → EFFECT → ACTION → PROOF → MESSAGE
                                      │
                                      ├── split on authority / owner / reversibility /
                                      │   proof / outcome meaning
                                      └── persist inspectable material results only

Surviving candidate
  C1 specification + C4-R decision grammar + mandatory integrity envelope
                                                │
                                                ├── one existing task-local trace
                                                └── C3 owner-facing projection

Required proof loop
  isolated receiver fixtures → multiple agent/harness trials
  → trajectory checks + end-state checks → qualified behavior/comprehension claims
```

## Iteration Status

- **Iteration:** 2 of 2 (min) / 5 (max)
- **Hypotheses tested:** H4 (provisionally supported at design level; not empirically verified)
- **Hypotheses deferred:** None for this assigned pass; behavioral confirmation is a later TS/evaluation dependency, not an unperformed claim of this analytical iteration
- **Gaps discovered:** no canonical durable update-record carrier in released 2.2.0; exact legacy methodology/purpose transition not selected; adapter authority and verification categories conflict; no fresh agent or owner-comprehension measurement
- **Superseded decisions:** D2 supersedes Extract's C2 standalone candidate; D3 supersedes Extract's C3 standalone candidate; D4 supersedes Extract's action-grouped C4; D6 corrects the early assumption that an ownership collision automatically requires an owner question

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | Comparative behavioral evidence for C1 + C4-R | Logical consistency cannot establish reliable agent behavior, safe replay, or lower owner burden. | Prefer TS-scoped isolated fixtures and declared agent/harness trials over another conceptual research pass. |
| 2 | Owner comprehension of the output projection | A fluent positive explanation can increase overreliance or hide an incomplete mental model. | Define a small comprehension task for benefit, actual completion, limitation, and next action; report only observed results. |
| 3 | Carrier and legacy transition design | Without these, the candidate cannot recover durably or protect project-purpose meaning. | Resolve during `/tfw-plan`/TS using the existing trace system and prospective ownership policy; do not add a second registry. |

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [ ] **MORE NEEDED** — not recommended; the remaining gaps are explicit planning/TS and behavioral-evaluation dependencies
- [ ] **BLOCKED** — no blocker

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Independent research found a coherent prompt-native alternative at the design level: retain a compact authority specification, make one semantic effect the unit of a local `OBSERVED → AUTHORIZED → EFFECT → ACTION → PROOF → MESSAGE` grammar, keep source/migration/ownership/adapter/verification/recovery work inside a mandatory integrity envelope, and render the owner-facing benefit/outcome/limitation/next account only from its evidence. It rejected a second duplicating state machine and rejected user-facing claims as technical scope authority, while preserving explicit entry/exit conditions within the existing workflow. The pass also corrected two attractive simplifications: narrative prose can support recovery when conditions are named and retrievable, and file collision alone does not create an owner decision. What this research adds is a common control model linking authority, recovery, proof, and communication without a new registry. Its main limitation is decisive: no fresh agent run, owner-comprehension study, or comparative cost measurement was performed, so H4 remains provisional and no improvement magnitude, deterministic compliance, smaller diff, or fewer-files result may be claimed.

---

*RES — TFW_20260906-190312_CRUE: Clear Release and Update Experience — Independent prompt-native reframing | 2026-09-06*
