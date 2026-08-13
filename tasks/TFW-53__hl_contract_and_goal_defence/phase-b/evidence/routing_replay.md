# AC-2 Routing Replay — `research/iter2/RES.md` through the shipped Step 6c

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Corpus**: [`research/iter2/RES.md`](../../research/iter2/RES.md) § HL Update Recommendations — 15 refinements (R12-R26), 3 amendment proposals (A6-A8), 4 coordinator notes. 22 rows.
> **Instrument**: the shipped text of `.tfw/workflows/plan.md` Step 6c items 3-4 at commit `fbdf443`, and nothing else.

## Method and its limit, stated first

I wrote the step and I am judging it, so the *instrument* is circular. The **corpus is not**: iteration 2
closed on 2026-08-10, three days before Phase A shipped the two classes, by a researcher who hand-rolled
the split from the HL. Its rows were not written to be routable by this step.

Routing used only these four lines:

```
3. Classify every recommendation by its target section and conventions.md §3 rule 6
   — never by the table it arrived in:
   - free section, or a free unit inside a frozen one → apply it
   - frozen claim → transcribe into HL §12 with verdict PROPOSED; the section itself stays untouched
4. Escalate once per iteration — one message carrying every proposal with its evidence, cost
   and considered alternative. A coordinator may not apply a proposal it filed; only an owner
   verdict moves one
```

Rule 6 supplies the tripwire the step points at: *the frozen unit is the declarative claim, not the
section text; a deliverable-list change inside an approved phase is free **unless the change cannot be
accepted under §5 and §6 as they stand at the moment of classification***.

## Result

| Row | Target | Routes as | Matches its label? | Note |
|-----|--------|-----------|--------------------|------|
| R12 | §10 | apply | ✅ | free section |
| R13-R17 | §2 | apply | ✅ | free section, 5 rows |
| R18-R21 | §9 | apply | ✅ | free section, 4 rows |
| R22, R23 | §11 | apply | ✅ | free section |
| R24 | §7.2 | apply | ✅ | free section |
| R25 | §8 | apply | ✅ | free section |
| R26 (1) fallback chain + admission criteria | §4 Phase C deliverable | apply | ✅ | frozen section, free unit; accepted under DoD-19 as it stood |
| R26 (2) PV priority-1 relabel | §4 Phase C deliverable | **§12 as `PROPOSED`** | ❌ **diverges** | see Finding 1 |
| R26 (3) fused citation-and-harm field | §4 Phase C deliverable | apply | ✅ | accepted under DoD-20 as it stood |
| A6 | §5 DoD (new item) | §12 as `PROPOSED` | ✅ | frozen claim |
| A7 | §5 DoD-19/20 | §12 as `PROPOSED` | ✅ | frozen claim |
| A8 | §5 DoD-17 | §12 as `PROPOSED` | ✅ | frozen claim |
| Note 1 — deliverable weighting | §4 Phase C deliverable | apply | ✅ | frozen section, free unit |
| Note 2 — `judge.md` row 2 is the enforcement site | **none** | **cannot route** | — | Finding 2 |
| Note 3 — `review.md`:28 needs one word | **none** | **cannot route** | — | Finding 2 |
| Note 4 — watch the `plan.md`/`review.md` budget | **none** | **cannot route** | — | Finding 2 |

**19 of 22 rows route. 1 routes against its label. 3 cannot route.**

Cross-check against what actually happened: A6, A7 and A8 are HL §12 rows A6, A7 and A8, each opened as a
proposal and ruled `✅ APPROVED — owner, 2026-08-10`. The shipped step reproduces the historical outcome
for all three.

## Finding 1 — the step catches a live unlogged edit to a frozen section

R26 arrived under `Refinements`. Its second item is *"deliverable 1 gains the PV priority-1 relabel"*,
targeting §4 Phase C. §4 is frozen; a deliverable list inside an approved phase is free — so a
label-trusting step applies it, and so does a target-section-only step. **The tripwire is what
discriminates:** at the moment R26 was filed, could the relabel be accepted under §5 as it then stood?

DoD-18 at that moment required priority 0 and said nothing about priority 1. The relabel entered DoD-18
afterwards, and the HL records how — line 594: `_(amended by A8; relabel per Q5)_`. **A8 is a §12 row;
Q5 is not.** Q5 is an owner ruling at HL line 724, dated 2026-08-10: *"✅ travels with TFW-53 — owner,
2026-08-10. Shipping priority 0 beside an uncorrected priority 1 is worse than shipping neither."*

So the relabel could **not** be accepted under §5 as it stood → under the shipped step it routes to §12
as `PROPOSED`, not to the free-unit path.

Stated fairly: **an owner verdict does exist**, so this is not an unapproved edit. What is missing is the
§12 row that `conventions.md` §3 rule 9 requires for an owner-initiated change to a frozen section — the
verdict was given in a Q&A table and the frozen text was changed on the strength of it. That is TFW-48's
failure mode in miniature: the change is documented, but it is not *diffable as an amendment*, so the
question §12 exists to answer ("which frozen claims moved, when, and on whose ruling?") returns an
incomplete answer for this one.

This is the discriminating case AC-2's derivation requirement was added for, and it fires on real history
rather than on a constructed fixture. It is also the only such case in the corpus: the ONB implied the
derivation requirement would change outcomes generally, and on this corpus it changes exactly one row of
22. Its value on the other 21 is that the classification becomes *checkable*, not that it becomes different.

## Finding 2 — three rows target the TS, not the HL, and the two-class model has no channel for them

The researcher's third table, `Coordinator notes — inside approved scope, no amendment needed`, holds four
rows. One (Note 1) is an ordinary free-unit refinement and routes fine. The other three are not HL
recommendations at all:

- Note 2 names `templates/review/judge.md` row 2 as the enforcement site — an instruction about where
  Phase C's TS must land its deliverables.
- Note 3 asks for one word in `review.md`:28 — the same, at line granularity.
- Note 4 says to state the word-budget constraint *"in the Phase C TS so an executor does not route them
  into `review.md` by default"* — explicitly addressed to the TS author.

None names an HL section, because none targets the HL. `templates/RES.md` offers `Refinements` and
`Amendment Proposals`, both defined by their target HL section, so research output aimed at the **TS** has
nowhere to go — and the researcher did what F11 predicts: invented a third table for it.

I did not fold these into `Refinements` to make the replay look clean. Routing them as refinements would
mean "apply it to a free HL section", which is not what any of them asks for.

**Not fixed here.** A third class is a `templates/RES.md` change, and the template is Phase A's; naming it
is Phase D's terminology pass (TS §2). Recorded as an RF observation. The shipped step is not defective
for failing to route them — a step that classifies HL recommendations cannot classify something that is
not one. The gap is in the template's class set, one level up.

## Finding 3 — the escalation the step prescribes matches what the corpus produced

iter2 filed three proposals in one batch and the owner ruled all three on one date. The step's
*"escalate once per iteration — one message carrying every proposal"* describes that exactly. No divergence.

---

*AC-2 Routing Replay — TFW-53 / Phase B | 2026-08-13*
