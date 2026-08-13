# AC-8 Evidence — Classification Exercise

> **Date**: 2026-08-13 · **Author**: Executor (Claude Code)
> **Subject**: five discriminating recommendation rows from [`research/iter1/RES.md`](../../research/iter1/RES.md),
> classified using only the text shipped in `.tfw/conventions.md` §3 → HL Contract.

---

## Read the limit before reading the score

The RES iter1 classifications were produced by the same researcher who authored the granularity
rule this exercise applies, and that RES says so in its own self-critique: *"row-by-row
re-classifications by the same researcher who wrote the classification rule — internally
consistent, not independently verified."* I also knew each row's RES assignment before classifying it.

**Therefore agreement demonstrates that the shipped text is *readable* — that a reader can reach the
intended classification from the rule alone — and demonstrates nothing about whether the
classification is *correct*.** The score below is 5/5 and it should not be read as validation of the
rule. The finding worth carrying forward is §Finding, not the score.

Rows were selected to discriminate, not to pass: two D4-tripwire cases where the naive reading of
rule 6 diverges from the RES assignment, one inverse case where the naive reading says "amendment"
and the RES says none is needed, and two controls.

## Shipped rule text under test

Quoted verbatim from `.tfw/conventions.md` §3 → HL Contract:

> 2. **Free sections stay free.** Research and the coordinator update §2, §7.2, §8, §9, §10 and §11
>    directly, with no proposal and no verdict. Risk registers, hypothesis statuses and dependency
>    statuses are required to move.
>
> 5. **The frozen unit is the declarative claim, not the section text.** Frozen at claim level: the
>    phase set and each phase's declared outcome, §3's to-be claims, each §5 and §6 item, each §7
>    principle, and §1. Rewording a claim without changing it is not an amendment; changing what it
>    commits to is.
>
> 6. **Deliverable lists inside an already-approved phase are free** — specifying *how* a phase meets
>    its declared outcome is refinement. **Tripwire:** if the change cannot be accepted under §5 and
>    §6 *as they stand at the moment of classification*, it is an amendment. Two tables decide it; no
>    judgement call is required.
>
> 7. **Non-substantive edits are not amendments** — typos, broken links, formatting, renumbering of
>    free-section rows.

## The exercise

| # | Row (RES iter1) | Target | Naive reading | Rule applied | My classification | RES assignment | Match |
|---|-----------------|--------|---------------|--------------|-------------------|----------------|-------|
| 1 | **A1** — add a Phase A deliverable: `conventions.md` §3 defines the Phase HL as derivation-only, plus a §14 anti-pattern | §4 Phase A | *Refinement* — it adds an item to a deliverable list inside a phase already approved (rule 6 first clause) | Rule 6 tripwire. At classification time DoD-8 enumerated six anti-patterns, none about the Phase HL, and no §5 item covered a Phase HL rule at all. The deliverable would produce work that no acceptance criterion could accept | **Amendment** | Amendment Proposal A1 | ✅ |
| 2 | **A2** — §12 gains a `Type` column | §12 grammar + §4 Phase A deliverable 1 | *Refinement* — a column is a specification detail of an already-approved deliverable | Rule 6 tripwire. DoD-2 enumerates the column grammar as a §5 item. A new column changes that item, so the change cannot be accepted under §5 as it stands | **Amendment** | Amendment Proposal A2 | ✅ |
| 3 | **Coordinator note 1** — the granularity definition (D2/D4) and the non-substantive carve-out (D13) land in Phase A deliverable 3 | `conventions.md` §3 content, under §4 Phase A deliverable 3 | *Amendment* — it decides what freezes, which sounds like a §3 to-be claim | Rule 5: no claim moves — the phase set is unchanged, Phase A's declared outcome is unchanged, no §3 claim, §5 item, §6 item, §7 principle or §1 statement changes. Rule 6: it specifies *how* deliverable 3 meets its outcome. Tripwire clears — DoD-4 (*"conventions.md defines the HL Contract: the six frozen sections, the moment of freezing, and the append-only nature of §12"*) accepts it without modification | **Refinement — no amendment** | "Coordinator notes — inside approved scope, no amendment needed" | ✅ |
| 4 | **A3** — add a DoD item: an approved amendment is followed by a re-freeze commit | §5 DoD | *Amendment* | Rule 5, directly: each §5 item is frozen at claim level, and adding one changes the acceptance contract. The tripwire is not reached | **Amendment** | Amendment Proposal A3 | ✅ |
| 5 | **R2** — raise the Phase HL risk from Medium/Medium to High/High and restate it | §9 Risks | *Refinement* | Rule 2: §9 is free and risk registers are *required* to move | **Refinement** | Refinement R2 | ✅ |

**Score: 5/5** — and per the limit stated above, that number carries less information than row 3 and
the finding below.

## Finding — the tripwire is time-dependent, and the shipped text now says so

Rows 1 and 2 are only classifiable against the state of §5 **at the moment of classification**.
Re-running row 1 against today's contract inverts it: DoD-8 now carries the Phase HL anti-pattern
and DoD-9 states the derivation-only rule, both landed by A1 itself, so the same deliverable would
now clear the tripwire and read as a refinement. That is correct behaviour — an approved amendment
is supposed to widen what the contract accepts — but a rule that omitted the timing would let a
classifier reach opposite answers from the same evidence and defend both.

The draft under test read *"cannot be accepted under the existing §5 and §6"*. `existing` was doing
the work implicitly. During this exercise the clause was tightened to *"under §5 and §6 as they
stand at the moment of classification"* — six words, recorded here as a change the exercise caused
rather than one the TS specified.

## What was not tested

- Whether the RES's own assignments are correct. Nothing in this repository can establish that; the
  owner ruled on all five proposals and approved all five, which measures the proposals, not the
  classifier.
- Rule 7 (non-substantive carve-out). No corpus row exercises it — the RES tables contain no typo or
  broken-link rows, because such changes never reach a recommendation table in the first place.
  This is a coverage gap of the corpus, not of the rule.

---

*AC-8 Evidence — Classification Exercise | TFW-53 / Phase A | 2026-08-13*
