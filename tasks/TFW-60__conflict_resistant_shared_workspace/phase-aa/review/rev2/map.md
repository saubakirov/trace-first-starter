# Map — revision 2 — "What was done?"
> **Mindset:** Experienced newcomer. Understand before you judge.
> **Scope of this revision:** the delta since REVIEW `8e83b6d` returned 🔄 REVISE. The first pass
> stands and is not rewritten: [`../map.md`](../map.md) · [`../verify.md`](../verify.md) · [`../judge.md`](../judge.md)
> RF: [RF Phase AA](../../RF__phase-aa__portable_delivery.md) at **revision 2**
> Commits under review: `b44bf7d`, `312dca9`
> **Owner's stated emphasis for this pass:** not file or line counts — *«важнее качество цели ценности»*
> — and a full audit of the template moves: who referenced what, where each thing is taken
> from, and whether any dirt or strangeness survived.

## Understanding

The executor closed the three returned items and then did something the review did not ask
for: it ran the **mechanic** the review's own fact candidate named — *grep the retired
sentence, not the concept* — and found four more sites of the same class. Two of them were in
code this phase had just edited.

`.tfw/templates/status.md` now states the two-act `UNDECLARED` rule and **cites**
`conventions.md` §5 instead of restating its table; the miscount reads *"The six keys."* The
four loose claims are narrowed in place, and in `312dca9` the executor declined to reuse the
reviewer's parser measurement, re-derived its own, and recorded both with their methods —
*"a number from someone else's run is not one they can vouch for."*

The class is now a test rather than an intention: `test_no_normative_file_states_a_retired_rule`
checks a named registry of retired wordings against every payload file that instructs, states
its own reach, and files the part it cannot reach as an observation with a candidate fix.

## TS ↔ RF Alignment — delta only

| Returned item | RF revision 2 claim | Aligned? |
|---|---|---|
| 1 — `templates/status.md` states the retired absolute rule | §10 item 1: replaced with the two-act rule, citing §5; CHANGELOG Canon entry now names all three copies and records that the third was missed | ✅ |
| 2 — *"four keys"* listed six | §10 item 2: *"The six keys"* | ✅ |
| 3 — four claims wider than their evidence | §10 item 3 (a)–(d): pycache caveat at the row; follow counts re-measured at the declared pin (9 and 6); ASCII check's reach stated; both parser measurements recorded | ✅ |
| *(not returned)* — the class behind item 1 | §10 items 4–7: stale `--validate` docstring; `parents[2]` in both test files; the dead `TD-11` citation; and the CHANGELOG paraphrase **deliberately** left with its exemption classified | ✅ exceeds the item |
| *(not returned)* — D3, the two counts | §1: both numbers now stated, with what each counts, and the TS's invalidated prediction pointed at the next phase's budget table | ✅ recorded as the review asked, not "fixed" |

## Deviations from TS — delta

None new. Revision 2 touches four payload files (`templates/status.md`, `CHANGELOG.md`, the
two payload test files) plus one non-payload test file and this phase's own trace artifacts.
Every one was already in the phase's scope.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 and the new §10 completely?
- [x] Matched each returned item to the RF's account of it?
- [x] Read HL §7 Principles — unchanged since the first pass; principle 10 still the phase's spine
- [x] Read ONB — no new questions were raised; the revise round needed none

Stage complete: YES
