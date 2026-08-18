# PROPOSAL — TFW-58: What Happens After a REVISE

> **Date**: 2026-08-13
> **Author**: Coordinator (Claude Code)
> **Status**: ⬜ TODO — proposal only. No HL, no TS. Entry point: `/tfw-plan`.
> **Sequenced after**: [TFW-53](../TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md) Phase C — see *Why not now* below
> **Splits with**: [TFW-54](../TFW-54__agent_team_mode/PROPOSAL__TFW-54__agent_team_mode.md) — agent freshness on a revision round belongs there

---

## Origin

Owner, 2026-08-13, describing the loop as actually practised:

> *«После ревью есть замечания, и по логике их надо сначала отправить координатору… потом дополнить TS следующим revision, потом исполнителю сказать иди доделай… С другой стороны, я часто просто отдавал ревайз исполнителю, и он сам закрывал — исключая координатора из цикла. Мне проще второй вариант, меньше чатов, быстрее добить. Но при этом я понимаю, что правильно через координатора.»*

> *«В кодексе это иногда превращается в бесконечно долгий цикл ревайзов туда-сюда, и расширяется базовый HL, и они по-немногу плывут и выходят за рамки задачи.»*

> *«Вроде бы мы это отплытие как раз и починили тут в TFW-53, но мне кажется при полной автономии ещё чего-то не хватает.»*

The owner is right on both counts. TFW-53 closes the drift channel above the TS and leaves the one below it open — and the shortcut they feel guilty about is not a violation, because there is no rule to violate.

## The canon gap, measured

| Where | What it says | What it does not say |
|-------|-------------|---------------------|
| `conventions.md:348` | `🔄 REVISE — specific issues → back to execution (same task)` | back to whom, through whom, with what artifact |
| `resume.md:52` | *"flag it as needing re-execution"* | a flag, not a process |
| `templates/REVIEW.md:48` | `### If REVISE — items to fix:` | what the executor does with the list |
| `handoff.md` | Phase 1 Onboarding, as if arriving fresh | **no entry point for "I am returning after a REVISE"** |
| all of `.tfw/` | — | the word `revision` appears **zero times** |

The arrow exists on the lifecycle diagram and nothing implements it. Every project therefore invents its own loop, and two incompatible inventions are already running in this ecosystem.

## Practice: two patterns, neither written down

```
TFW-38 — a second full phase           AFD — revisions inside one artifact
──────────────────────────────         ─────────────────────────────────────
PhaseA  → TS ONB RF REVIEW             149 REVIEW files
PhaseA2 → TS ONB RF REVIEW             13 carry rev1..rev4   (8.7%)
                                       deepest observed loop: 4 rounds
= new work, clean trace,               arc recorded in one file:
  heavy ceremony                       "wrong APPROVE (rev1) → REVISE
                                        → rev2/rev3 fixes → APPROVE"
```

AFD also carries 18 numbered sub-phases (`phase-a0..a3`, `b0..b7`, `c1..c3`, `d1..d3`). Eight sub-phases of a single Phase B is a proliferation signal worth measuring: how many were planned splits, and how many were revision rounds wearing a phase name?

## What TFW-53 closes, and what it leaves open

| Drift channel | Status after TFW-53 |
|---|---|
| Research rewrites the goals | ✅ frozen contract + amendment log |
| Coordinator absorbs findings silently | ✅ classify, never update |
| Reviewer approves work that misses the point | ✅ Purpose Check (Phase C) |
| Reviewer blocks on wording | ✅ materiality bar — a block must rest on material impact |
| **A REVISE loop grows the TS** | ❌ open — the TS traceability gate was ruled out of scope by the owner |
| **A REVISE loop has no termination** | ❌ open — nothing counts rounds |
| **Who is in the loop after a REVISE** | ❌ open — the canon is silent |

TFW-49 drifted through the contract. This is the same failure one level down, through the spec.

## Design sketch — the ladder already exists

The question *"coordinator in the loop or not?"* is malformed. It conflates **who decides what gets fixed** with **who does the fixing**. Separate them and the answer falls out of a mechanism TFW-53 already shipped and the owner already ruled on:

```
reviewer files a REVISE finding
      │
      ├─ satisfiable inside the approved TS?
      │     YES → executor fixes, reviewer re-checks.  COORDINATOR NOT NEEDED
      │            (the owner's shortcut — legitimate, and the majority case)
      │
      │     NO  → the TS must change
      │            → COORDINATOR, because only the coordinator may change a TS.
      │              An executor doing it is a Role Lock violation
      │
      └─ cannot be satisfied without touching a frozen section?
             → OWNER, through the amendment protocol
```

Same shape as refinement / amendment / verdict. Not an invention — the transfer of a ruled mechanism onto a second surface.

**The same tripwire answers the owner's second question.** Revision in place versus a new phase is not a matter of taste:

| | Test | Artifact |
|---|---|---|
| **Revision** | repair of what was already specified — needs no TS change | `rev2` of the RF and the REVIEW; one trace, no new TS |
| **New work** | cannot be accepted under the existing TS | a new phase or a follow-up task, with its own TS |

If it needs a TS change, it is not a revision — it is new work wearing a revision's name.

The consequence the owner is looking for: with this rule, *"расширяется базовый HL"* stops being reachable from inside a revision loop. More work can only be ordered through the coordinator; the goals can only move through the owner.

## Open — needs research, not a decision

1. **Loop termination.** Nothing counts rounds; AFD reached four. Research has `max_passes` and `loops_per_stage`, review has no equivalent. What is the number, and what happens when it is hit — escalate to the owner, or force an APPROVE carrying tech debt?
2. **Re-entry in `handoff.md`.** An executor returning on rev2 today re-runs a full onboarding or improvises. What must a returning executor read, and what may it skip?
3. **Sub-phase proliferation.** Were AFD's eight Phase-B splits planned, or revision rounds renamed? The answer decides whether "new phase" is a healthy outlet or a leak.
4. **Does the loop shrink after TFW-53 Phase C?** The materiality bar removes wording-only blocks — the documented AFD-48/B failure mode. The revise rate before and after is the number that sizes this entire task.

## Deferred to TFW-54 — agent freshness

Owner's intuition: *«существующие агенты склонны дрейфовать и переписываться друг с другом бесконечно, отдавая туда-сюда правки»*. Genuinely unresolved; the evidence pulls both ways.

| Fresh agent on rev2 | Same agent on rev2 |
|---|---|
| AFD-38: the same reviewer approved, then retracted only under owner pressure | A fresh reviewer has not seen rev1's reasoning and re-litigates settled points — the ping-pong gets worse |
| TFW-53 iter2 self-critique: *"hindsight is uncontrolled"* when the same agent re-judges its own work | AFD-48: the second pass found a real defect, but the first failed on **materiality**, not on staleness |

This is agent topology, it needs measurement, and TFW-54 already carries hypotheses about it. Recorded there, not here.

## Why not now, and why not inside TFW-53

Three reasons, in order of weight:

1. **Phase C changes the size of the problem before it can be measured.** The materiality bar removes the class of REVISE that produces the longest loops. Designing a protocol for a loop whose frequency is about to change means measuring the wrong thing.
2. **TFW-53 is five phases and thirteen amendments deep, with Phase B unfinished.** Adding a sixth surface now is the drift the task exists to prevent. The owner's own recorded preference: *«Разделять большие вопросы на отдельные задачи»*.
3. **It needs the research iteration 1 proved works** — a corpus count against AFD's 13 revision arcs and 18 sub-phases, answering how many required a TS change and how many were repairs in place.

**Cost of never doing it:** under full autonomy a loop with no rule and no limit is TFW-49 repeated from below. There the drift ran through the contract; here it runs through the spec.

## Prerequisite

Do not open before TFW-53 Phase C ships and a handful of reviews have run under the Purpose Check. The first deliverable of the research is the before/after revise rate — without it the task is designed against a number that no longer holds.

---

*PROPOSAL — TFW-58: What Happens After a REVISE | 2026-08-13*
