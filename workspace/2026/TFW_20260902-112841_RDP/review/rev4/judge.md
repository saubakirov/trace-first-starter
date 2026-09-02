# Judge — "Is the quality sufficient?" — round 4

> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof.
> Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md) — 13 commands, 100% file verification, two discrepancies **D1**
> and **D2**, zero citation discrepancies

## Universal Checklist

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD met? | ✅ | **All four ordered items delivered and independently verified** — `verify.md` V1–V4. Item 1's repair reproduced by importing both expressions and probing nine names (4 characters, not the 3 the order claimed); its hardest gate — *the third assertion shown failing against the old regex* — re-proven here, not taken on report. Items 2 and 3 are one line each, both correct, and `KNOWLEDGE.md` is 1 insertion / 1 deletion with §2's history untouched as ordered. Item 4's record checked bullet against bullet: all three requirements present, and it does not claim the event was repaired. **AC-11 bullet 1 re-run: 322 passed, 1 skipped, exit 0.** AC-11 bullet 2 is **withdrawn by the owner's ruling**, named as withdrawn in TS revision 4 §1, and correctly not claimed. All nine of TS §7's failure conditions hold: ten forbidden paths byte-identical against `859dc74`, four targets in four files, no fifth item worked, zero new entities |
| 2 | **(a) Purpose Check** · **(b) Design soundness** | ✅ (a) · ✅ (b) | **(a)** filled in full below — **✅ Aligned**. **(b)** sound against HL §7. Principle 7 (*a rule with no enforcement site is decoration*) is the item this round exists to satisfy and the only one that could have been faked: round 3 shipped two assertions that **could not fail** against the defect they guarded, which is enforcement in shape and advice in fact. Round 4's third assertion is the first in that file that can fail, and it was *demonstrated* failing before being believed. Principle 6 (*subtraction is the proof*) holds — zero new entities, four one-line-class edits. Principle 1 (*the test is a named consequence*) is met in the observations, which name consequences rather than severities |
| 3 | **Debt disposed** | ⚪ **N/A at this stage — by design, not by omission** | Reason stated: dispositions are **ruled by the coordinator**, once, at the close of review (`conventions.md` §15, `review.md` Step 6). This file is the reviewer's. REVIEW revision 4 §5 therefore carries **eight rows, every one `pending — coordinator` with an explicit `*Proposed:*`** in the shipped grammar — a named consequence or its named absence, never a bare priority, and each `not material` stating *not owed* or *owed and forbidden to pay* **with the barring clause cited**. Each proposal names an artifact that **exists today**: this task's own phase directory, or `workspace/2026/TFW_20260902-222456_RTBO/` (`status.md` present, `lifecycle: TODO`, scope explicitly covering the un-gating aftermath). No row says *"→ backlog"*. **Round 3's seven rows are all ruled and none is `pending`** — verified in REVIEW revision 3 §5, three `paid`, four `not material`, with row 1's three successive rulings preserved unedited |
| 4 | Style & standards | ✅ | Commit subjects follow `conventions.md` Commit Attribution: `[claude-code/TFW_20260902-112841_RDP/rf/executor] …` on all three of the round's commits. The revision grammar this task itself shipped is obeyed exactly — the RF and ONB **appended** as `.4` subsections, rounds 1–3 never overwritten, the TS a **sibling** at the highest ordinal, the EV appended. `git status` shows only a neighbouring session's ` M .gitignore`, in no commit of this round: the shared-tree discipline was claimed and is evidenced |
| 5 | Observations collected | ✅ | Five rows in §6.4, and **the filter is working rather than padding**. Row 1 is the round's own unmet gate, raised against its author's interest. Row 2 named a corpus drift caused by a neighbouring session at 22:24 — since resolved by that session's own commit `9f08960`, which is the drift the row predicted, arriving within the hour. Rows 3, 4 and 5 are each verified true at their exact locators (`verify.md` command 12 confirms row 5 precisely: the removed `verify` **was** the template's one working command, annotated *"A real command, not a placeholder"*). The RF also names what it deliberately did **not** observe — re-observing REVIEW rev3 §5 row 2 would reopen a disposed item by the back door. That restraint is correct |
| 6 | RF completeness (§7-9) | ✅ | Present **and** of quality. §7.4 — four fact candidates, three High one Med; F17 (*a test that proves a detector fires must be shown failing against the defect it guards*) is PV 1 with a method attached and is the round's most transferable output; F20 records that the owner may change the question rather than the answer and tells the next executor to read the whole order for the seam. §8.4 — execution insights, not restatement. §9.4 — two structural diagrams: the escape path through the old lookahead, and a before/after of what moved with the gate and what did not. **Both are structure, which is the only kind that earns its place here** |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | E25–E28 all exist as rows in the EV file with raw output in `evidence/round4.md`, statuses drawn from the fixed four-status vocabulary, and every TS Evidence field covered: the nine probes, the before/after of the changed expression, the grep before and after, the project-wide search with each hit classified, the suite figure and the `git grep` output. The round-4 header names the reference revision for every byte-identity claim, which is what makes those claims checkable at all |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? | ❌ | **The green signal is real and one figure behind it is not.** What the evidence genuinely establishes is better than the corpus norm: E25 does not merely compare two regexes, it **runs the new assertion under the old expression and shows it failing** — the difference between *the expressions differ* and *the test can fail*, and precisely the gap that let this defect through round 3. E26 reports its gate **unmet** rather than green. Three figures are corrected against the executor's own interest. **What it does not establish is the shipped sentence's own denominator:** `.tfw/CHANGELOG.md` asserts *"the only event over the ceiling among the **116** in this corpus that carry a summary"*, and the corpus held **117** summary-bearing events at `1a9059b` — the commit that ships that bullet — 118 at HEAD, 114 at dispatch. **116 is the count at no revision in this round.** `evidence/round4.md` records the measurement as `$ python  # over every journal event in workspace/ and tasks/` — a comment, not a command — so the number cannot be re-derived by the next reader. → **D1**, ordered as REVIEW revision 4 §4 item 1 |
| 9 | Backward compatibility | ✅ | Consumers enumerated and each one checked. `docs/scripts/test_integration.py` is repository tooling — the payload is `.tfw/`, so **no receiving project holds this file**, and the tightening breaks nothing on the canonical surface (0 offenders before, 0 after: the mandated form `TS__{ID}__rev{N}.md` is still admitted, verified directly). `glossary.md` and `KNOWLEDGE.md` are prose locators; the de-numbered forms name titles that exist. The one change with a real receiver is item 4's, and it is the reason the item exists: `build.verify`'s removal from a **PROJECT** section that `update.md` preserves means nobody's key is rewritten for them, so the CHANGELOG entry is the only possible messenger — and it carries an explicit *"remove it"* plus the distinction that a `build.verify` naming something of the receiver's own should be kept. Nothing is adapter-installed, so no `cmp` was owed, and the RF says so rather than silently skipping it |
| 10 | Safety | ✅ | No secret, credential, destructive or irreversible operation. The one irreversible act available in this round — editing an immutable journal event — was **forbidden** and did not happen: the event is byte-identical against `859dc74`, verified. Nothing was force-pushed, nothing rewritten; three commits, each with an explicit path list |

> Rows 7 and 8 answered on different questions and reaching different answers, which is the normal shape
> of a real finding: the evidence is all **there** (7), and one figure inside it does not **prove what it
> is offered to prove** (8).

## Purpose Check — row 2 clause (a)

**Reference set used:** master HL at contract baseline `1c7b55e`, verified byte-identical
(`git diff 1c7b55e HEAD` on the HL is empty), **plus** the Project North Star `NS1`–`NS3` at
`.tfw/README.md`. **Not** the TS, and there is no Phase HL.

**Status: ✅ Aligned.**

**The field.** The clause served is **NS1** — *"another authorized person or agent can understand what the
work is for, inspect its material grounds and current result, see where authority remains, and continue"* —
and the concrete harm at stake was the fourth round becoming the thing NS1's second paragraph names,
*"work that increases output while obscuring purpose, authority, inspectability, or continuation"*: a round
that ran because a loop had no floor rather than because a condition could be named. **It did not become
that.** Every one of the four items cites a condition in the coordinator's own order, all four are the
coordinator's own errors, and the round's own bound held — four targets, four files, zero new entities,
ten forbidden paths byte-identical. **Authority is visible at every seam that mattered**: the un-gating
was applied by the coordinator outside Role Lock and the TS records that it was, naming who did what
rather than who was supposed to; AC-11 bullet 2 was withdrawn **by name, by whom, and on what grounds**
rather than quietly dropped; and the round's one unmet gate was handed to the reviewer as overturnable
instead of filtered green.

**The three tests, each answered *no*:**

1. **Excess and adjacency — no.** Nothing arrived that the cited clause does not ask for. The scope
   addition (`KNOWLEDGE.md`) is a **named rung-2 discharge** in TS revision 4 §2, not a drift. DoF 1's
   absolute holds: zero new files, templates, scripts, checks, keys, statuses or verdicts. The one
   temptation — making the gate informational to get green — was correctly identified in TS §2 as a
   script change DoF 1 forbids, and was **not** taken; the gate went instead, on the owner's instruction.
2. **Deferral confession — no.** Nothing the spec names a different home for is shipped here. The
   reverse is the case, twice over: the executor named five out-of-scope findings and touched none of
   them, and explicitly refused to re-observe a **disposed** item because doing so would reopen it by the
   back door. That is the opposite of the failure this test looks for.
3. **Materiality — the one finding is material, and it is not a wording objection.** D1 is not a figure I
   would have phrased differently; it is a corpus count that is **false at the commit that ships it**, in
   a **shipped, untagged** release entry, with **no recoverable command** behind it — and `verify.md`
   command 13 confirms `release.md` contains no step that would re-measure it before the tag. It sits
   inside the one clause of HL §7.1 that governs exactly this: *"Every claim about the corpus carries its
   measurement. A count in this task's artifacts is one that was run, with the command recoverable."*

> **Why a citable finding does not make this a purpose failure.** D1 is a **work defect inside the
> approved contract** — rung 1, in a file this revision's §4 already names, one clause to repair. A purpose
> failure is work that should not exist; this is work that exists correctly with one false number in it.
> The reference set is **internally consistent** and **no frozen claim needs to move**: no amendment is
> proposed, and the tension worth naming — an immutable event against a bound whose only reader runs after
> the write — is a canon rule against a tool, not two baseline clauses, and it is already disposed as
> REVIEW revision 3 §5 row 2 and carried as fact candidate F12. **No contract defect.**

## The handed-over gate — ruled

> Item 2's gate reads *"`grep -n "Step [0-9]" .tfw/glossary.md` returns no `handoff.md` step number."* It
> returns one: line 215, `Session Naming`. The executor declared it unmet, argued it, and marked it
> overturnable. **This is the ruling.**

**The executor is upheld — and on a stronger ground than the three it offered.**

Its three grounds check out (`verify.md` V2): the entry did not drift (the renumbering moved steps 8–13;
Step 0 is at `handoff.md:16` and was never in range); `## Step 0: Name This Session` is a real heading in
`handoff.md` and `review.md`; and the glossary term *is* *"Step 0 convention"*, so the number is the
definiendum rather than a locator into a renumbered list.

But the decisive point is one the executor did not reach. **The condition item 2 enforces is TS revision 3
item 2 bullet 4 — *"a renumbering that leaves them pointing at old numbers is half of one"*.** `handoff.md`
Step 0 does not point at an old number. It points at the current, correct step, by a heading that exists.
The gate's *text* is broader than the condition it was written to enforce, and **a gate is not itself a
condition** — this task's own shipped rule is that a round may order only an item naming a breached
acceptance criterion or frozen HL claim. Reading TS §7's *"a `handoff.md` step number survives anywhere
outside history"* literally enough to reach a correctly-resolving heading would make the failure condition
order a change that **HL §7.1 forbids**: *"Touch nothing you do not have to. A section this task does not
need to change is not improved, reworded or reformatted"* — reinforced by **DoF 8**, *"a section it does
not touch is rewritten."* De-numbering `Session Naming` would rewrite the glossary term and reach `plan.md`
and `review.md`, and `review.md` is under a byte-identity bound. **So the repair is not merely unnecessary;
it is barred.** Leaving it was the only compliant act available, and reporting the gate unmet rather than
filtering it was the right way to leave it.

**This is not a fifth item.** It goes to REVIEW revision 4 §5 as row 1, `not material — not owed`.

**One thing the executor's argument missed, and it is a separate defect.** Ground (b) — *it is a real
heading* — is true for two of the three workflows that line cites. **`plan.md` has no Step 0**, at HEAD or
at the HL baseline, and says the omission is deliberate at line 84: *"This is step 3 and not step 0
deliberately."* So the entry asserts a universal that one of its own cited files intentionally breaks, and
points a reader at a step that does not exist. **Pre-existing — caused by nothing in this task**, already
propagated into the frozen corpus, and barred from repair here by the same HL §7.1 clause and by TS §7's
*"a fifth item is worked."* → §5 row 2, this review's own finding.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---|---|---|
| 1 | **D52** (PV priority 3) — *"handoff Step 11"* | Repaired to *"handoff `Collect evidence`"* | **None — the contradiction was in D52 and is now gone.** Verified: step 11 is `Pre-RF Gate` and the entry means `Collect evidence`. `glossary.md`'s PV Index row 3 plus *Who scans PV* confirm the stated consequence at its source: coordinators scan priority 3 **in full** before planning |
| 2 | `KNOWLEDGE.md` §2 `TFW-46` row — still cites *"handoff Step 11"* | Deliberately untouched as history | **None.** TS revision 4 §5 item 3 bullet 3 and §7 both require it to stay; repairing it would be editing history. Correctly left |
| 3 | `KNOWLEDGE.md` §2 — no task row for `TFW_20260830-194027_TLD` | RF §6 round-1 row 4, unchanged | **None new.** Already raised and disposed in an earlier round; not reopened here |
| 4 | D53, D55 and the D-records on adapter parity | This round touches nothing adapter-installed | **None.** Verified: no adapter path in either commit, so no parity claim is at risk and no `cmp` was owed |

## Fact Candidates reviewed — any that need challenge?

**F17 (High)** — sound, and the most valuable output of the round: *a test that proves a detector fires
must be shown failing against the defect it guards*, with the procedure attached. Verified by re-running
it. **F19 (Med)** — sound and under-rated at Med; naming the reference revision inside a byte-identity
claim is what let me check that claim in one command instead of re-deriving it. **F20 (High)** — sound,
and correctly framed as domain rather than process.

**F18 (High) — challenged.** Its rule is right: *a shipped artifact must not quote a figure measured over
a live shared corpus*. Its worked example is wrong. It offers *"1 of 116"* as the figure **"the neighbours
cannot move"**, and 116 is exactly a figure the neighbours moved — 114 → 117 → 118 across this round.
The half that is genuinely immovable is **1**, the count over the ceiling, which held at every revision I
measured. **The candidate should carry the corrected example when it reaches `/tfw-knowledge`**, because a
fact whose illustration contradicts its rule teaches the opposite of the rule. Recorded in REVIEW revision
4 §7.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)? — ten rows, each citing `verify.md` findings or a
      command run there
- [x] Every `⚪ N/A` carries a stated reason — no row skipped as a bare ✅? — one `⚪`, row 3, with the
      reason stated: disposition authority is the coordinator's, and the rows are proposals here by rule
- [x] Row 2(a): answered against the contract baseline and the north star — never the TS or a Phase HL —
      with a quoted clause **and** a named harm in one field? — yes, NS1 quoted plus HL §1's baseline,
      baseline verified byte-identical, harm named as the loop-without-a-floor, all three tests answered
- [x] Rows 7 and 8 answered separately, with different reasoning? — ✅ / ❌ respectively; the evidence
      exists in full and one figure inside it does not establish its claim
- [x] Referenced verify.md findings in DoD assessment? — V1–V4 and commands 1–13
- [x] Row 3: every §5 row disposed, each disposition naming something that exists today, each ruling
      naming a consequence or its absence rather than a priority? — eight rows, all `pending — coordinator`
      with proposals in the shipped grammar; targets are this phase directory and `RTBO/`, both existing
- [x] Checked RF §7-9 for presence AND quality? — yes, and F18's example is challenged rather than passed
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"? — four rows, none outstanding
- [x] Fact Candidates from RF reviewed — any that need challenge? — **F18, challenged above**

Stage complete: **YES**
