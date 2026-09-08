# Briefing — "How should an AI agent make a project update clear, safe, and useful?"
> **Mindset:** Strategist. Plan the investigation before proposing a design.
> **Test:** "Can I explain why this is uncertain and what evidence would change the approach?"
> Parent: [HL-TFW_20260906-190312_CRUE](../../HL-TFW_20260906-190312_CRUE.md)
> Goal: TFW releases reach existing projects as coherent, safe, and understandable improvements that agents can apply from shipped instructions while owners retain project purpose and consequential choices.

## Research Plan

### Gather

- Start with primary external sources on instruction-following agents, prompt/instruction hierarchy, uncertainty, human oversight, and evaluation; identify mechanisms rather than generic prompt-writing advice.
- Reframe update reliability through alternative engineering mental models—such as protocol design, safety cases, transaction/recovery semantics, and progressive disclosure—without assuming that any analogy transfers to a probabilistic reader.
- Collect counterevidence about instruction brittleness, context dependence, automation bias, and the gap between apparent compliance and user understanding.
- Define candidate dimensions for later comparison: authority handling, evidence acquisition, ambiguity response, update/recovery state, owner-facing information, and behavioral verification.

### Extract

- Derive at least three coherent prompt-native configurations from the external mechanisms before inspecting the current TFW update procedure for applicability.
- For every strong idea, map engineering principle → agent/prompt adaptation → user benefit → analogy boundary or counterexample → observable check.
- Compare the configurations by their treatment of ownership, uncertainty, consequential decisions, interrupted/repeated updates, and truthful continuation.
- Write short competing instruction and owner-interaction specimens that expose behavioral differences without implementing product changes.

### Challenge

- Stress the configurations with conflicting context, missing evidence, stale prior choices, customized project material, partial application, refusal, and source defects.
- Seek primary counterevidence and construct cases where concise guidance hides authority changes or detailed guidance overwhelms the owner.
- Only after independent alternatives exist, inspect the released `v2.2.0` / `8e68ab37d300122ff110500ad58f354f76b6210f` behavior to test fit, divergence, and migration cost without importing newer-master behavior.
- Decide H4 explicitly: identify a simpler complete survivor, or document why no alternative improves the baseline enough to justify change.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|---|---|
| H4 | An independent prompt-native reframing can yield a simpler complete approach than incremental repair of the existing procedure. If no alternative survives challenge, retain that negative result rather than manufacture novelty. | needs-research |

## Scope Intent

- **In scope:** Primary-source mechanisms for reliable agent instructions and human oversight; alternative mental models; prompt-native release/update interactions; authority, ownership, evidence, uncertainty, recovery, user benefit, and behavioral evaluation; applicability checks against the released TFW 2.2.0 baseline.
- **Out of scope:** Reviewing or reading `iter1`; starting from the Coordinator's defect/fix list; treating H1–H3 as the required architecture; a new installer, runtime, package manager, or script system; implementing fixes; modifying the frozen HL, shared task state, iteration registry, field reports, framework files, or product code; claims beyond observed evidence.

## Guiding Questions

1. What minimum instruction structure helps an agent distinguish evidence, authority, uncertainty, and allowed action without pretending the prompt executes deterministically?
2. Which alternative model gives the owner a truthful project-level account of benefit, consequence, limitation, and next action with the least necessary attention?
3. What behavioral evidence would falsify each candidate rather than merely show one agent producing a plausible-looking answer?

## User Direction

- Owner-approved independent pass `research/iter2/` investigates H4 from first principles; it is not a continuation or review of `iter1`.
- Task-local §10 exception assigns iteration 2 with no predecessor. No `iter1` briefing, stages, RES, worktree, or discussion may be read before this RES is complete.
- The Main Coordinator selected `deep` mode because architectural uncertainty and counterexamples are material; no repeated mode question is required.
- Routine checkpoints are decided by the Main Coordinator in task `01a0766c-8096-7a83-af60-f70c248290bc`; new strategic owner decisions remain unresolved.
- Operational instructions are prompts read by reasoning AI agents, not executable code or a human manual. Engineering practices must be adapted and bounded accordingly.

---
Stage complete: YES
