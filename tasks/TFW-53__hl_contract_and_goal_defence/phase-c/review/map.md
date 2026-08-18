# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase C](../RF__phase-c__goal_defence_in_review.md)
> TS: [TS Phase C](../TS__phase-c__goal_defence_in_review.md)
> ONB: [ONB Phase C](../ONB__phase-c__goal_defence_in_review.md) — 3 blocking questions, all answered `(a)`
> Reference set recovered: HL-TFW-53 at frozen baseline `e8ee76e` (`[claude-code/TFW-53/freeze/coordinator] re-freeze after amendment A13`), per `conventions.md` §3 rule 15

## Understanding

The Judge checklist's row 2 clause (a) used to ask **mapping integrity** — does every TS §3 Principles
Check row resolve to an AC that was actually met? That question cannot detect a principle violated by the
mapping itself, and it had two live statements: the `judge.md` row and a paragraph in `review.md` Step 3.
Both are gone. In their place row 2(a) is a **Purpose Check** — *is this what we set out to do?* — answered
against the master HL at its committed frozen baseline plus the Project North Star, with the TS and any
Phase HL named as invalid references. The enforcement mechanism sits in a block **below** the table, not in
the row: one fused field (quote the clause served *and* name the concrete harm), three tests
(excess-and-adjacency, deferral confession, materiality), an override clause ruling out *"the TS scoped it
this way"* and *"tests are green"*, and a three-outcome table.

Around it, six supporting files: `review.md` gains the frozen-baseline reference at line 28, a Reviewer
Identity that names goals/values/north star with block authority, the replacement Step 3 instruction and a
Step 4 routing block; `REVIEW.md` realigns §3 row 2 and surfaces the `not fit for purpose` finding inside
its existing `### If REJECT` block; `glossary.md` PV Index gains priority 0 and relabels priority 1;
`conventions.md` §3 defines the Project North Star in seven rules and §14 gains two review-side
anti-patterns; `templates/HL.md` gains a north-star header field below the contract block;
`compilable_contract.md` stops resolving `P{N}` to the `KNOWLEDGE.md` §0 that D37 removed and reserves
`NS{N}` and `PP{N}`. Two evidence artifacts are new, one of which replays the shipped check against nine
historical reviews.

**Three decisions a newcomer must hold.** (1) The mechanism is a block, not a longer row — so clause (b)
stays quotable and separately answerable, and the whole apparatus costs `review.md`'s word budget nothing.
(2) The third outcome is a *finding*, not a fourth status symbol — the Status column keeps `✅/❌/⚪` so it
cannot collide with Phase E's forthcoming `❌ REJECTED` status. (3) The `README.md` Task Board row was left
uncommitted on the coordinator's explicit instruction, because a concurrent TFW-55 session holds the file.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — Purpose Check replaces clause (a); clause (b) survives; 10 rows; rate + consequence reason; no project name | RF §3: met with one disclosed divergence — clause (b)'s antecedent *"those"* → *"HL §7"*, three words | ✅ (divergence disclosed, not hidden) |
| AC-2 — five properties as failing conditions; dry-run + failing variant | RF §3: all five present; `purpose_check_replay.md` §5 | ✅ |
| AC-3 — reference set stated; TS and Phase HL named invalid; fallback chain; rule-15 pointer, no restated command | RF §3: substantively met; the *gate's* literal form has a pre-existing counterexample at `templates/HL.md`:10 | ⚠️ substantive pass, gate counterexample disclosed |
| AC-4 — line 28, identity, routing, no new verdict token | RF §3: lines 28, 87, 102; verdict set unchanged | ✅ |
| AC-5 — below 1,200 words; no removal to buy headroom; report rather than resolve | RF §3: 1,065 → 1,176; removal column empty | ✅ |
| AC-6 — PV priority 0, priority 1 relabel, admission criteria, locus rules | RF §3: priority 0 added, rows 2-7 byte-identical, `conventions.md` §3 carries all four ruled properties | ✅ |
| AC-7 — HL template north-star field below the contract block, list-valued, fallback, explicit N/A | RF §3: one additive hunk, zero deletions | ✅ |
| AC-8 — `REVIEW.md` §3 row-for-row, finding in the synthesis, no new section | RF §3: ten rows, row 2 realigned, finding inside `### If REJECT` | ✅ |
| AC-9 — `NS{n}` / `PP{n}` / `P{n}`; one table only | RF §3: lines 59-61, `+3 / −1`; `PP{N}` declared and unused, stated as such | ✅ |
| AC-10 — two §14 anti-patterns, additions only | RF §3: `27 0` | ✅ |
| AC-11 — replay, ≥1 non-approve on the rejected corpus, 0 on the sound one, filled field per row | RF §3: 5 of 6 / 0 of 3 | ⚠️ condition met, one row's classification contested — see verify.md D1 |
| AC-12 — third outcome, distinct, routed to the owner, reachable inside `judge.md` | RF §3: outcome table row 3 + one-line precedent; *"exercised for real: replay row 49/A"* | ⚠️ textual gate met; the "exercised" claim rests on the contested row |
| Frozen DoD 18-29 (12 items) | Mapped: 18→AC-6 · 19→AC-7 · 20→AC-1/3/4 · 21→AC-2 · 22→AC-2 · 23→AC-12 · 24→AC-4 · 25→AC-4 · 26→AC-8 · 27→AC-9 · 28→AC-5 · 29→AC-11 | ✅ every frozen item has an AC |

## Deviations from TS

1. **Clause (b) is not byte-identical** — three words, disclosed in RF §2 decision 2, EV E1 and RF §3.
   The antecedent *"those principles"* referred to clause (a)'s TS §3 rows; deleting clause (a) would have
   left a dangling pronoun. Legitimate and correctly surfaced.
2. **`not rubber stamp` restored to the Reviewer Identity** — two words beyond the literal AC-4 text, inside
   the deliverable AC-4 authorises, closing a loss D46 recorded and shipped only half of. Declared in RF §2
   decision 5 with an explicit statement that it is not load-bearing.
3. **`review.md`:85 was added to TS §4 before it was touched** — the coordinator amended the TS on ONB Q1
   rather than letting the executor extend scope silently. Not a deviation in the shipped result; recorded
   because the discipline is what made it not one.
4. **AC-3's gate cannot be cleared by this phase.** The gate says *"confirm no second copy of the recovery
   command exists in `.tfw/`"*; `templates/HL.md`:10 carries one and AC-7's gate forbids modifying that
   block. Reported, not worked around.
5. **TD-155 left open** — its routing note named "the next phase that may edit `conventions.md` §3", which
   is this one, but the fix rewords Phase A's rules 13-15 and both HL §7.1 and TS §9 forbid it. Coordinator
   re-routed it to Phase D at ONB R4.

**Nothing in RF is outside TS scope.** Phase D's deliverables (glossary articles, adapter sync, version
bump) and Phase E's are untouched; no repository north star was written into either README.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely? — and §6-§9
- [x] Read TS DoD and matched each item to RF §3? — 12 ACs plus the frozen DoD 18-29 mapping above
- [x] Read HL §7 Principles — can I state the design philosophy? — read at baseline `e8ee76e`: the contract
      earns the autonomy (P1), structural enforcement over guidelines (P3), purpose is a distinct question
      judged where verdicts are formed (P13), every gate needs a materiality bar (P14), alignment must be
      cited not asserted (P15), judge against the baseline never the spec (P16)
- [x] Read ONB — were blocking questions resolved? — three questions, all answered `(a)`, all four
      coordinator corrections (AC-1, AC-6, AC-7, AC-11) and AC-12 landed in the TS before execution

Stage complete: YES
