# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF__phase-b__enforcement_in_workflows.md](../RF__phase-b__enforcement_in_workflows.md)
> TS: [TS__phase-b__enforcement_in_workflows.md](../TS__phase-b__enforcement_in_workflows.md)

## Understanding

Phase A wrote the HL contract into the artifacts and into `conventions.md`; nothing enforced it, and
`plan.md` still carried two instructions — line 106 *"Update HL with research findings"* and line 117
*"update HL → present diff → user confirms"* — telling the coordinator to do exactly what the new rules
forbid. Phase B replaces both with classification: Step 6c now routes each research recommendation by
its **target section plus `conventions.md` rule 6**, applying free units and transcribing frozen claims
into HL §12 as `PROPOSED`, with one batched escalation per iteration. Step 4 turns HL approval into a
written `Contract` field plus a freeze commit before the first research iteration. A new **6d** block
handles amendment verdicts wherever they arrive — deliberately not nested inside the research loop,
because two of this task's own thirteen §12 rows entered from an ONB and two from the owner during
execution. `research/base.md` Step 6 splits one recommendation table into `Refinements` /
`Amendment Proposals`, each row naming its target HL section, plus a `MUST` rule and a Role Lock
restatement. Two corrective passes rode along: `templates/RES.md`:133 (the third live "update HL",
authorised at ONB Q2) and `templates/HL.md` §3.1 (rewritten on owner authorisation mid-execution).

`plan.md` went 1,206 → 1,195 words by removing 13 measured duplication sites — under F2's 1,200 hard
threshold, still outside its 700–900 working range, which the executor reports as a partial failure
rather than resolving.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — approval recorded, not implied; freeze commit before first iteration; reference not restatement | ✅ Step 4 `On approval — freeze the contract`, 3 items, points at `conventions.md` §3 rule 15 | ✅ |
| AC-2 — both "update HL" replaced; classify by target section + rule 6; batched escalation; no self-application | ✅ 0 grep matches; five items present; replay of 22 rows in `routing_replay.md` | ✅ |
| AC-3 — both verdict paths + re-freeze at new baseline + `RESTRICT` on filing + reserved scope word | ✅ new 6d block, three bullets | ✅ |
| AC-4 — researcher classifies into the two Phase A classes, never edits; D19 narrowed not revoked | ✅ Step 6 item 3 + new `MUST` rule | ✅ |
| AC-5 — no platform, shell or vendor in either workflow | ✅ 0 matches before and after | ✅ |
| AC-6 — `plan.md` meets F2 (≤1,200 hard, 700–900 working); removals paired with their duplicate source | ⚠️ **Partial, reported.** 1,195 — hard threshold met, working range not. 13 removals ledgered | ⚠️ declared partial |
| DoF-4 — no file modified outside the three named in TS §4 | RF §3: *"no file modified outside TS §4's three"* | ❌ **contradicted by RF §1's own table and by the commit** — see verify.md D1/D2 |

## Deviations from TS

1. **`templates/RES.md`:133** — one clause, authorised at ONB Q2, added to TS §4 with the limit *"one
   clause on line 133 and nothing else"* **before** the file was touched. Disclosed in RF §1 as a Phase A
   correction. Properly handled.
2. **`templates/HL.md` §3.1** — a fourth file, **not in TS §4**. Owner-authorised mid-execution, classified
   before being touched (RF Decision 13), and the RF states plainly that adding the scope entry is the
   coordinator's act, not the executor's. Disclosed, but the scope entry does not exist yet.
3. **`.tfw/workflows/review/{code,docs,spec}.md`** — three files deleted inside commit `fbdf443`,
   **undisclosed anywhere in the RF or EV**. They belong to concurrent task TFW-56. See verify.md D1.
4. **`plan.md`:97 dead reference removed** — authorised at ONB Inconsistency 1 with an explicit condition
   (*"state the reason in the RF so the saving is not counted as compression"*). No mention in RF or EV.
   See verify.md D3.
5. **6d is a new labelled block**, not named by any AC — sanctioned by the coordinator's ONB Recommendation 1
   ruling, and nothing was renumbered, so external citations (`glossary.md`:178) still resolve.
6. **Line 117 replaced by a gate**, not deleted — RF Decision 4 states this and names it as unrequired by
   any AC. Reasonable: AC-2 demanded the line go, and the algorithm needed something in its position.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy? *(the contract earns the autonomy;
      classify never edit; structural enforcement over guidelines; batch don't interrupt; evidence-cost-alternative;
      narrow D19; token density; tool-agnostic; naming creates behaviour; authority cannot self-extend;
      a remark is not a verdict; a frozen baseline must be diffable)*
- [x] Read ONB — were blocking questions resolved? *(Q1 rewrote AC-6 against frozen DoD-17; Q2 authorised
      `templates/RES.md`:133. Both answered before execution, both traceable in the shipped work.)*

Stage complete: YES
