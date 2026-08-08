# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-53](../../HL-TFW-53__hl_contract_and_goal_defence.md)
> Goal: An approved HL becomes a frozen strategic contract that research may only amend through a logged, evidenced, owner-ruled channel.

**Iteration:** 1 of 2 (min) / 3 (max) · **Mode:** deep (`loops_per_stage: 3`, counter-evidence required)
**Run mode:** autonomous, owner-authorised — `/tfw-research tfw-53 автономно без вопросов deep mode`. Stage WAIT gates are executed as self-checkpoints; no questions are asked mid-run. All questions are surfaced in RES for the coordinator.

---

## Contract Notice

The parent HL is **🔒 FROZEN** (approved 2026-08-08, baseline commit `8136306`).
Frozen: §1, §3, §4, §5, §6, §7. Free: §2, §7.2, §8, §9, §10, §11.

This research classifies its output accordingly. Findings that touch a frozen section are written as
**Amendment Proposals** for HL §12, never as updates. This is the mechanism under investigation applied
to itself — and it is a live test: if the protocol is unusable by the researcher who is designing it,
that is a finding, not a formatting problem.

## Research Plan

**Gather — "What do we NOT know?"**
- Build the full corpus of historical `HL Update Recommendations` rows across every RES in `tasks/` (the HL named six tasks; the corpus is larger and the wider count is strictly better evidence for H1).
- Classify each row against the frozen/free split in HL §3 and produce a number: escalations per iteration.
- Locate every Phase HL that has ever existed in this repository (working tree + git history) and diff it against its master HL (H6).
- Enumerate the mechanism alternatives for contract state (H3) against D31, TFW-50's commit convention, and the git object model.
- External: how mature change-control regimes bound an approved baseline — ADR immutability/supersession, CCB baseline management, repository-level ownership gates.
- Decompose into independent Dimensions. Candidate factors already visible: freeze scope, freeze granularity, state mechanism, classification authority, escalation batching, freeze asymmetry, Phase HL governance, REJECT composition.

**Extract — "What do we NOT see?"**
- Cross-reference the dimensions into a Configuration Space; look for the combination nobody proposed — specifically whether the frozen/free axis is the right axis at all, or whether change *type* and *granularity* carry more of the load than section identity.
- Sub-classify the frozen-targeting corpus by change nature (deliverable precisification / scope addition / goal redefinition / acceptance change / principle change) and by direction (expansive vs restrictive), because the escalation cost of the design depends on that distribution, not on the raw count.

**Challenge — "What do we NOT expect?"**
- Pairwise consistency across dimensions; eliminate incompatible combinations.
- Counter-evidence, deliberately: the corpus was produced under D19, which *ordered* research to rewrite the HL. Would the same findings exist under a freeze? Selection effect must be priced in before the H1 number is trusted.
- Stress the surviving configurations against DoF-2 (escalation spam), DoF-7 (undefined rejected path), DoF-10 (unverifiable baseline), and the documented CCB failure pair (rubber stamp / bottleneck).
- Resolve freeze asymmetry and REJECT composition, the two open design questions in HL §10 Blind Spots.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | In TFW's own history, the large majority of RES `HL Update Recommendations` targeted free sections (§2, §8, §9, §10) rather than frozen ones — so freezing six sections costs few escalations per task | open — one counter-signal (TFW-49 `642c647`); needs the full corpus count |
| H3 | A contract state field in the HL header plus an append-only §12 is sufficient state; no filesystem-level marker (lock file, approved-HL snapshot) is needed despite D31 | open |
| H6 | Phase HLs in multi-phase tasks are a real drift channel: historical Phase HLs introduced deliverables absent from their master HL | open — TFW-48/49 phase HLs believed to show no content drift |

Also in scope from HL §10 Blind Spots (not numbered hypotheses):
- **Freeze asymmetry** — do tightening a DoF and loosening a DoD need the same amendment path?
- **REJECT composition** — how the amendment protocol composes with the existing `❌ REJECT → user branching point` in `conventions.md` §5.

Settled upstream and **not re-litigated**: H2 (confirmed), H7 (confirmed), H8/H9/H10 (settled by AFD recon). H11/H12/H13 belong to iteration 2.

## Scope Intent

- **In scope:** the contract half of TFW-53 — freeze scope, freeze granularity, contract-state mechanism, classification and escalation protocol, Phase HL governance, amendment/REJECT composition. Evidence is this repository's own history.
- **Out of scope:** goal defence in review (north star, Judge check, reviewer identity, verdict vocabulary, replay validation) — that is iteration 2 in full. Phase E trace restoration needs no research. AT delegation mode is TFW-54.
- **Method boundary:** this iteration proposes; it never edits the HL, and it never writes TS.

## Guiding Questions

Autonomous run — no questions asked of the user during this iteration. The three questions this iteration
would otherwise have put to the owner are carried into `RES.md § Open Questions` for the coordinator to route:

1. If freezing all six sections escalates on ~every iteration, is the correct response to shrink the frozen set or to shrink the frozen *unit* inside §3/§4?
2. Should tightening a constraint (adding a DoF, narrowing scope, dropping a deliverable) travel the same amendment path as loosening one?
3. Do Phase HLs inherit the freeze, or should the artifact class stop existing?

## User Direction

Owner instruction for this run, recorded verbatim: *«tfw-53 автономно без вопросов deep mode»* — run iteration 1
autonomously, in deep mode, without interactive gates. Owner also fixed the run architecture in HL §11 S27:
research runs in a separate session with no planning-conversation history, deliberately, because in TFW-49 the same
coordinator that ran the research accepted it.

---
Stage complete: YES
