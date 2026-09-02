# Map — "What was done?" · round 3

> **Mindset:** Experienced newcomer. Understand before you judge.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF__TFW_20260902-112841_RDP](../../RF__TFW_20260902-112841_RDP.md) — round 3 is the `.3` subsection of all nine sections
> TS: [TS__TFW_20260902-112841_RDP__rev3](../../TS__TFW_20260902-112841_RDP__rev3.md) — the highest ordinal, and the order
> Prior stage files: [`review/`](../) (round 1), [`review/rev2/`](../rev2/) (round 2)
> Contract baseline: `1c7b55e` — verified byte-identical to the current HL

## Understanding

Round 3 is the small one. Round 2 delivered both owner amendments; what round 2's review left were four
proposals, and the coordinator ruled all eleven §5 rows in one act and ordered **six items** — the four
proposals plus two it added by overruling two `not material` proposals into `paid`.

Six items, six files plus two adapter copies, ~20 lines:

```
  1  docs/scripts/test_integration.py   DOUBLED_SLUG learns the one suffix §4 mandates
  2  .tfw/workflows/handoff.md          step 7 DELETED; the RF transition moves to the end of Phase 3
  3  .tfw/templates/REVIEW.md           the heading stops inviting an order; the placeholder asks for a basis
  4  .tfw/conventions.md §4             one row: the EV file is classified `appended`
  5  .tfw/CHANGELOG.md                  two dead locators removed; four ⚠️ Changed bullets
  6  .tfw/glossary.md                   `Disposition` says what a `paid` ruling requires
```

**Three items grew by exactly one edit each after the ONB, and no seventh file entered the round.** The
ONB asked three blocking questions and all three were answered *(a)* — de-number the glossary's step
citations inside item 2, write four `⚠️ Changed` bullets on frozen DoD 13, and put two assertions inside
item 1 because an admitted exception with no assertion is how a widening escapes notice.

**The round's headline result: the check item 1 exists to repair now passes.** `DOUBLED_SLUG` went from
12 offenders on the canonical surface to 0, and `handoff.md` got **shorter** — 1 730 → 1 727 — because
step 7 was deleted rather than rewritten.

**The round's headline problem is not the executor's.** The suite is still not green. The remaining
failure is a `summary` of **123 code points** against a 120 ceiling, in a journal event the *coordinator*
wrote at 18:14 — the act that paid REVIEW revision 2 §5 row 10. It landed in `bbdfde8`, the commit that
ordered this round, which is why the order's own stated before figure was already stale when it was
written. The executor measured rather than quoted, found 2 failed instead of 1, and said so.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| **Item 1** — the regex admits *exactly* the mandated suffix and nothing else; other detectors keep firing; two assertions; a comment citing §4 | RF §3.3 item 1 — four bullets `[x]`, **the gate bullet left `[ ]`** | ⚠️ four of five; and the *"exactly … and nothing else"* bullet does not hold as measured — see verify.md D2 |
| **Item 2** — step 7 removed not rewritten; the `RF` transition in Phase 3 once the RF exists; renumbered; file shorter; `glossary.md`'s step citations de-numbered; copies re-synced | RF §3.3 item 2 — all six `[x]` | ⚠️ five of six; the de-numbering covered two citations and **two more survive** — verify.md D3 |
| **Item 3** — heading names proposals; placeholder asks for the breached condition; nothing added | RF §3.3 item 3 — all four `[x]` | ✅ |
| **Item 4** — the EV classified by the generating line, one row | RF §3.3 item 4 — all three `[x]` | ✅ |
| **Item 5** — both locators removed not corrected; substance untouched; no sweep; four `⚠️ Changed` bullets | RF §3.3 item 5 — all five `[x]` | ✅ |
| **Item 6** — one sentence in `Disposition`; in `glossary.md` not §5; nothing else changed | RF §3.3 item 6 — all four `[x]` | ✅ |
| **TS AC-11** (revision 1, held in force by revision 3 §3) — the build passes **and** `--check tasks` stays green | RF §4.3: *"1 failed, 321 passed"* and *"exit 1 on the event above"* | ❌ — **both bullets breached, and the RF says so** |
| **DoF (revision 3 §7)** — ten conditions | RF §3.3 reads them one by one: nine held, the first *"half-failed, and reported as such"* | ⚠️ nine of ten |

## Deviations from TS

**One, and it is a refusal rather than an excursion.** The suite was left red. The cause is in no
revision's Affected Files, and a journal event is immutable once written (`conventions.md` §4), so the
executor enumerated the three available repairs — edit an immutable event, supersede it and leave the
malformed file for the gate to keep reading, or raise `tfw.journal.max_summary_length` to fit a violation
— named each as a **decision rather than a task**, routed it as rung 2 and stopped. `handoff.md`'s own
return section instructs exactly that.

**Not a deviation, and worth naming because it looks like one.** Three items are one edit wider than the
order first wrote them. All three widenings were ordered by the coordinator in the ONB answers and are
recorded in the order's own §4 and §5 with *(ONB Q10/Q11/Q12)* beside each. The executor did not widen
its own scope.

**Nothing was swept.** `review.md` is byte-identical to its state entering the round — `git diff` returns
zero lines, which is the falsifiable form rather than an assurance. `conventions.md` §5 is unchanged at
1 673 words, which item 6's own DoF required.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely, round 3's subsections and the two earlier rounds' for what is closed
- [x] Read the TS and matched each of the six items and revision 1's surviving AC-11 to RF §3.3
- [x] Read HL §7 Principles at baseline `1c7b55e` — the operative ones here are 6 (*subtraction is the proof* — `handoff.md` fell) and 7 (*a rule with no enforcement site is decoration* — item 1's two assertions are that site)
- [x] Read ONB §9 — three blocking questions, all three answered `(a)` in §9.2a before execution began

Stage complete: **YES**
