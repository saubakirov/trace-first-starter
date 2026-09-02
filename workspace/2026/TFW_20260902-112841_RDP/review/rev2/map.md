# Map — "What was done?" · round 2

> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF__TFW_20260902-112841_RDP](../../RF__TFW_20260902-112841_RDP.md) — round 2 is the `.2` subsection of every section it touches
> TS: [TS__TFW_20260902-112841_RDP__rev2](../../TS__TFW_20260902-112841_RDP__rev2.md) — the highest ordinal, and the order
> Round 1's stage files: [`review/map.md`](../map.md), [`review/verify.md`](../verify.md), [`review/judge.md`](../judge.md)
> Contract baseline: `1c7b55e` — the freeze that carries A13 and A14

## Understanding

Round 1 shipped a review protocol whose loop was ended by **a configured budget on TS revisions**, and
wrote the round's order into `REVIEW` §4 — the reviewer's file. The owner then ruled both wrong, in two
amendments: **A13** withdrew the count entirely and replaced it with a **citation bar** (a round may order
only items naming the condition each breaches), and **A14** moved the round's order into a **TS revision**,
the coordinator's own artifact. Round 2 delivers both, plus the five ordered repairs round 1 left open.

Nine items were ordered in `TS__…__rev2.md` §5a. **Four were already satisfied on entry** — three as
round-1 edits orphaned in a shared working tree, one closed by a neighbouring session — and were verified
against the criteria that ordered them rather than redone. Five were worked: the count is out of every one
of the twelve tracked files that carried it, the revision grammar is stated once in `conventions.md` §4
and generates four artifact rules from one line, `conventions.md` §5 draws the round cycle and returns the
work to the coordinator, `plan.md` gains Step 8 to receive it, and a 🔄 REVISE finally has lifecycle states
(🟡 `TS_DRAFT` → 🟠 `ONB`).

**Fifteen files changed outside the task directory. Zero created. Zero configuration keys — the one round 1
spent was given back, so the task's net entity count is zero.** `review.md` Steps 4–6 measure **477 against
the 483 baseline**, three words better than round 1 left them, and the budget was met by **subtraction**:
the withdrawal freed 88 words and the citation bar cost 82.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| **AC-13** — the round's order is a TS revision, a sibling; highest ordinal governs; the revision states round, orderer, prior review, each item's basis, and its approval; `review.md` Step 6 writes no bound; the basis cell is the enforcement site | RF §3.2 AC-13, all five bullets `[x]` | ✅ |
| **AC-14** — after a review no role guesses: six-step chain, each step a write into the role's own artifact or a designated cell | RF §3.2 AC-14 — five of six `[x]`; **bullet 4 left `[ ]`** because it is the reviewer of the round writing `REVIEW__…__rev2.md`, which had not happened | ✅ honest — and **this file closes it** |
| **AC-15** — the revision grammar stated once in §4, generating all four artifacts; live revision amended in place, superseded never touched; RF rule cites its measurement; round cycle drawn once | RF §3.2 AC-15, all seven bullets `[x]` | ✅ |
| **AC-16** — the count withdrawn from every site it reached, gated by `git grep` | RF §3.2 AC-16, all eight bullets `[x]`; **14 hits in 12 files → 0 in 0** | ✅ |
| **Item 7 (AC-12 carried forward)** — the lifecycle tells the truth for the executor's whole leg | RF §3.2 item 7, all six bullets `[x]`; `(develop)` gone, two REVISE states, both `ONB` descriptions rewritten | ✅ |
| **Items 1–5** — verified rather than redone | RF §3.2 — items 1, 2, 4, 5 committed at `fb1fb36`; item 3 closed at `1de76bc` by the RTMW session | ✅ |
| **Revision 1's AC-11**, bullet 1 — *"The build passes: `python -m pytest .tfw/scripts/ docs/scripts/ -q`"*; TS rev2 §3 keeps it as verified | RF §4.2 reports **1 failed, 321 passed, 1 skipped** and routes the failure as a rung-2 finding | ❌ — **the one misalignment, and the executor declared it** |
| **DoF (TS rev2 §7)** — nine conditions | Order in the coordinator's artifact ✅ · one live revision ✅ · zero new entities ✅ · no undesignated write ✅ · bar has its enforcement site ✅ · `max_revision_cycles` gone ✅ · 477/160 ✅ · `.tfw/scripts/` untouched ✅ · round readable from a listing ✅ | ✅ 9/9 |

## Deviations from TS

Three, **all declared in the RF before this review opened**:

1. **`conventions.md` §14 was edited although TS rev2 §4's table does not name it.** RF §2.2 decision 2
   states the authority: §4 says *"Revision 1's file list stands"*, and revision 1's scope names §14
   explicitly. §14 carried the count (*"A revision budget is exhausted and the loop is allowed to
   continue"*), so leaving it would have left the canon announcing a mechanism the same release removed.
   **Sound** — the authority is textual, not a reading of a headline.
2. **`KNOWLEDGE.md` §2's own task row was corrected although AC-16's bullets do not enumerate it.**
   RF §2.2 decision 3: the row asserted this task shipped *"one config key"*, in a release that ships none,
   and AC-16's headline is *every site it reached*. **Sound** — HL §7.1 forbids a false claim about the corpus.
3. **`handoff.md` step 7 was deliberately not obeyed.** Step 7 orders `lifecycle: RF` *before* step 8
   *Implement*; the executor stayed at `ONB` for the whole leg and reported step 7's wording as observation 1
   rather than editing a line the order does not name. **Sound** — obeying it would have written the exact
   falsehood item 7 exists to remove, while shipping the fix for it.

**Not a deviation:** the red test. The file (`docs/scripts/test_integration.py`) is outside the order's
Affected Files, and changing a TS is a Role Lock violation for the executor. The routing is correct; the
*state* it leaves is the finding, and it belongs to the coordinator.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely — including round 1's subsections, to know what was *not* re-argued
- [x] Read TS DoD and matched each item to RF §3 — AC-13, AC-14, AC-15, AC-16, item 7, items 1–5, plus revision 1's surviving AC-11
- [x] Read HL §7 Principles at baseline `1c7b55e` — seven principles; the operative ones here are 6 (subtraction is the proof) and 7 (a rule with no enforcement site is decoration)
- [x] Read ONB — §8.2's five blocking questions, all answered in §8.2a, **three of them correcting the order rather than clarifying it**

Stage complete: **YES**
