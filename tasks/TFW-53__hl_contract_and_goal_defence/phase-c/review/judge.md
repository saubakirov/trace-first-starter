# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

> Every row is asked in every review. There is no genre that exempts a row.
> **Status vocabulary:** `✅` holds · `❌` fails, with a specific finding · `⚪ N/A` does not apply here.

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | All **twelve** ACs pass on their stated gates, every gate command re-run by this reviewer and reproducing exactly (verify.md commands 1-7). All **twelve frozen DoD items 18-29** map to an AC — map.md carries the mapping. Two ACs carry disclosed divergences rather than clean passes and both survive: AC-1's clause (b) changed three words to repair the antecedent the deletion orphaned; AC-3's literal gate has a pre-existing counterexample at `templates/HL.md`:10 that AC-7 forbids this phase to clear. AC-11 recounts to **4 of 6** after D1 and its pass condition (*≥1*) still holds; AC-12's gate is textual and passes independently of D1 |
| 2 | Two clauses, both answered. **(a) Purpose Check** — *is this what we set out to do?* **(b) Design soundness** _(4.5%)_ | ✅ | **(a)** — filled below the table, per the mechanism this phase ships. **(b)** — sound. The design's load-bearing choice is that the mechanism lives in a **block below the row** rather than in the row: it keeps clause (b) separately answerable (P3's enforcement site is the template, and the template is off F2's budget), and it is why 111 words of `review.md` bought a check with a reference set, five failing conditions and three outcomes. The alternative the TS named as a risk — *"row 2 grows into a paragraph"* — was avoided structurally, not by discipline. The third outcome as a **finding** rather than a fourth glyph is the other sound call: a new symbol would have collided with Phase E's `❌ REJECTED` status inside one release |
| 3 | Tech debt documented | ✅ | RF §6 carries six observations with file, line, type and a stated destination each. Five survive the quality filter; obs. 4 does not (see row 5). Two of them (obs. 1, obs. 3) are the kind that would otherwise be found by the next reader and blamed on this phase |
| 4 | Style & standards | ✅ | Commit subject follows the D55 grammar (`[claude-code/TFW-53/phase-c/executor]`). The shipped vocabulary is exactly the HL §4 Phase C list — `Project North Star`, `Purpose Check`, `not fit for purpose`, `deferral confession`, `NS{n}` — with no synonym invented. F13 held: no project name appears in any shipped template, and `P16` is deliberately *not* cited inside `judge.md` because `P{n}` is task-local — the phase fixing a namespace collision declined to commit one, which is the correct call and is written out in RF §2 decision 4. F22 held: no new template section, no row 11 |
| 5 | Observations collected | ✅ | Quality filter applied. **Promoted:** obs. 1 (recovery command's fourth copy, in the template every future HL is born from), obs. 2 and 3 (`compilable_contract.md` — a second stale `KNOWLEDGE.md` §0, and two patterns declared with no resolution behaviour), obs. 5 (`verify.md` checks that citations *resolve*; nothing checks that they are *relevant*, which is the guard the Purpose Check now depends on). **Rejected as filler:** obs. 4 — *"Step 3 now has two named things a reader must hold apart"* names no defect and predicts a future editor's temptation; nothing breaks if it is never addressed. Obs. 6 is not debt but a KNW routing note and is treated as one |
| 6 | RF completeness (§7-9) | ❌ | §7 (3 candidates), §8 (3 insights) and §9 (three diagrams, and they are the strongest §9 in this task — the before/after reviewer view, the third-outcome decision tree and the replay result) are all present and mostly high quality. **The finding is S2's factual basis.** S2 claims *"the check found its own predecessor's defect while being validated on it"* and derives from it that the replay is the check's regression suite. D1 removes the premise: TFW-49's reference set is not internally inconsistent, so the check did not find a defect there, and research iteration 2's original `passes` verdict was right for a second reason it did not know. S2 is marked High confidence and is destined for `KNOWLEDGE.md` at KNW — the row fails so the correction happens before the fact is written, not after |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | All 13 EV rows exist with valid statuses; both attachments resolve; the `evidence/` folder follows D53. Every TS Evidence field is covered — the two ACs whose TS Evidence reads *"N/A — textual"* still carry a reproduced command in the EV row rather than a bare assertion, which exceeds what was asked |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? _(16.1% — the highest-firing check in TFW review)_ | ❌ | Eleven of thirteen rows establish their claims, and the two divergences the EV file *does* disclose (E1, E3) are handled well — named in the row, repeated in the verdict, not downgraded to `DEFERRED` to look tidy. **E11 and E12 do not.** Replay row 49/A rules a contract defect on a half-sentence: §1 reads *"readable without special tooling, **while structural validation prevents quiet drift**"*, so the clause the row treats as contradicting DoD-3's validator is the clause that asks for it (verify.md D1, C6). The row's own supporting argument — TFW-50 as outside confirmation — proves two contracts differed, not that one was self-contradictory. Secondary, same shape: the 48/A note puts *"preserves all ten mapped principles"* in quotation marks where the source reads *"preserves Phase HL P1–P10"* (D2). This is the classic row-7-passes-row-8-fails shape, and the irony is load-bearing: the block three paragraphs above the precedent line rules that *a citation that resolves but is irrelevant fails the row* |
| 9 | Backward compatibility _(8.5%)_ | ✅ | Consumers checked. `judge.md`, `REVIEW.md` and `review.md` have one class of downstream copy — the three adapter surfaces — and `.claude/commands/tfw-review.md` plus `.agent/workflows/tfw-review.md` now instruct a retired check. That window was **already open** (TD-157, opened when Phase B changed `plan.md`); this phase widens the same window rather than creating a new one, TS §2 declares the sync out of scope, and Phase D closes it. No section number moved, no anchor broke, no template section was renumbered, and past REVIEW files keep their own text. The docs pipeline — the only other consumer of these five files — builds clean |
| 10 | Safety _(4.0%)_ | ✅ | No secrets, credentials or destructive operations. The one irreversible act is the deletion of the mapping-integrity check from both live sites, which is DoD-20's instruction and DoF-11's requirement, not a loss. The `README.md` restraint is the safety-relevant judgement call and it was right: a concurrent session holds the file, and the executor staged nothing it did not write |

## Purpose Check — row 2 clause (a)

**Reference set.** Master HL-TFW-53 at frozen baseline **`e8ee76e`**, recovered per `conventions.md` §3
rule 15 (`[claude-code/TFW-53/freeze/coordinator] re-freeze after amendment A13`), plus the Project North
Star. The north star for this repository is ruled but not yet designated in either README (owner, ONB Q2;
HL §11 S38; deliberately deferred per TS §2), so this row runs on the **declared fallback** — master HL §1
at the frozen baseline. Neither the TS nor the Phase HL was used.

**Citation and harm, one field.** Serves §1 Vision — *"And the contract gains a defender. The reviewer stops
being only a quality guardian and becomes the last gate for goals, values and north star. Review asks 'is
this what we set out to do?' against the approved baseline and a project north star that finally sits above
the task — never against a spec that may itself have drifted. Work that is verified, complete and beside the
point becomes a rejectable outcome, and alignment can no longer be asserted without citing the clause it
serves."* Every one of those five commitments is now a **failing condition in the template that is filled
every review**, not prose. The harm it removes is measured, not hypothetical: the check being replaced scored
`✅` on TFW-48/A by mapping master principles onto a Phase HL that had authored **its own ten** in place of
the master's thirteen, so master P7, P10 and P12 were absent from the mapping and structurally invisible to
the row (verify.md C17). A check that cannot see the principles the mapping dropped is the check that
approved six phases of a result later reverted at 27,103 deletions.

**Excess and adjacency — no.** Two candidates tested. (i) `not rubber stamp` restored to the identity: two
words, inside the deliverable AC-4 authorises, closing a documented four-month loss, and explicitly declared
non-load-bearing. (ii) The north-star locus permitting non-root READMEs and more than one location: wider
than frozen §4's *"a designated section of the root `README.md`"*, but owner-ruled at ONB and free under
`conventions.md` §3 rule 6, whose tripwire clears — no §5 or §6 item as it stands is breached. Neither
crosses a baseline non-goal, a DoF item or a phase boundary. Nothing from Phase D or E was pre-empted: no
glossary term articles, no adapter copies, no version bump, no repository north star written.

**Deferral confession — no.** Four items whose home is elsewhere were named and **left**:
`compilable_contract.md`:65 and :81 → Phase D, TD-155 → Phase D, the north-star designation → TFW-55, the
`templates/HL.md` recovery copy → whoever owns that template next. Each is in RF §6 with a destination. The
phase declined the one thing that would have been a confession — implementing frozen DoD-23 without an AC —
and the coordinator closed the gap instead.

**Materiality.** The harm this review names (D1) is material — it ships a defective illustration into every
install and a false fact into project memory — but it is a defect *inside* work that serves the cited clause,
not work that fails to serve it. The block is on evidence sufficiency, not on purpose.

**Outcome: ✅ aligned.** No purpose finding. Recorded explicitly because this phase's own thesis is that the
two questions are orthogonal: the work is what we set out to do **and** two of its evidence rows do not
establish what they claim.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D61 — universal ten-row Judge checklist, measured rates carried inside each promoted row | Purpose Check ships as clause 2(a) with its figure inside the row | **No.** Ten rows kept; the rows 8-10 grammar copied deliberately (RF §2 decision 9) |
| 2 | D46 — Reviewer Identity, recorded as *"Quality guardian, not rubber stamp"* | `not rubber stamp` restored | **No — completed.** D46's row was always the full phrase; only half had shipped. RF §6 obs. 6 routes the retention finding to `/tfw-knowledge` |
| 3 | D43 — citation-with-link as the anti-hallucination device | The fused field adds a harm half | **No — extended.** SS2's gap (*a citation that resolves is not a citation that is relevant*) is what the harm half closes in Judge. RF §6 obs. 5 correctly notes `verify.md` has no counterpart |
| 4 | D37 — `KNOWLEDGE.md` §0 removed | `PP{N}` reserved and unused; no §0 invented | **No.** AC-9 asked for exactly this and the RF says so plainly |
| 5 | D54 — adapter parity is a behavioural promise | Adapter copies left stale | **No, but live-broken** — declared out of scope in TS §2, tracked as TD-157, closed by Phase D. Row 9 |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every `⚪ N/A` carries a stated reason — no row skipped as a bare ✅? — no `⚪` used; all ten rows apply
- [x] Row 2(a): answered against the frozen baseline and the north star — never the TS or a Phase HL — with a quoted clause **and** a named harm in one field? — baseline `e8ee76e` recovered by rule 15; fallback chain in use and named; §1 quoted in full; harm measured against TFW-48/A
- [x] Rows 7 and 8 answered separately, with different reasoning? — 7 asks whether the 13 rows exist (they do); 8 asks whether they prove what they are offered to prove (11 do, 2 do not)
- [x] Referenced verify.md findings in DoD assessment? — D1-D4 and C1-C22 cited by identifier throughout
- [x] Checked RF §7-9 for presence AND quality (not just existence)? — row 6, and the quality check is what fails it
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"? — five items examined, none contradicted
- [x] Fact Candidates from RF reviewed — any that need challenge? — all three hold; FC1 and FC2 are direct owner rulings from ONB Q2, FC3 is the coordinator's own recorded act. None challenged

Stage complete: YES

---

# Judge — second pass (corrective, 2026-08-13)

> **What is re-ruled:** only the two rows that failed — 6 and 8 — plus row 1 for AC-13 to AC-15, and row 2's
> Purpose Check re-run against the changed `judge.md`. Rows 3, 4, 5, 7, 9, 10 were `✅` on the first pass,
> the corrective pass did not touch what they examined, and re-asking them would be ceremony.
> Verify findings: [verify.md](verify.md) — second-pass section, V10-V16, C23-C28, D1-D6.

| # | Check | First pass | Second pass | Evidence |
|---|-------|:---:|:---:|----------|
| 1 | DoD met? | ✅ | ✅ | Now **15 of 15** ACs on their gates. AC-13: §1 quoted to the end of its sentence, `✅ aligned` returned, excess argued and rejected against DoD-3 **and DoD-7** (traced verbatim, C25), TFW-50's confirmation dropped, **8 of 8** propagation sites landed (V14). AC-14: the blockquote states the bar, no substitute example hunted for, `1,167 → 1,165` words, `review.md` untouched at 1,176 (V10, commands 11-12). AC-15: S2 rewritten, S4 added, and the 48/A item resolved by **verifying the source rather than obeying the instruction** (D2). TS §7's sixteen DoF items all clear, count reproduced |
| 2 | Purpose Check + design soundness | ✅ | ✅ | Re-run against the changed block. **(a) aligned** — filled below. **(b)** the design is now *better*, and the improvement is the kind that only a corrective pass produces: the old precedent line gave a reader one case to pattern-match, the new bar gives the discriminating test — *satisfying one clause must necessarily violate the other; read each to the end of its sentence; surface tension is not inconsistency; coherent-but-wrong is the purpose question*. That is precisely the test whose absence produced D1. A gate that teaches the error it was built from is a better gate than one that ships an example |
| 6 | RF completeness (§7-9) | ❌ | ✅ | **The finding is discharged.** S2's false premise is gone and the withdrawal is marked inline rather than quietly overwritten, so a KNW reader sees what changed and why. What replaced it is smaller and verified: two runs of the replay now agree on all nine rows, and the reusable half is that a truncated citation cleared research, an HL and a first-pass evidence file because it *resolved*. **New S4** is the stronger addition — *the corpus contains no self-contradictory contract, and saying so is worth more than an example* — and it generalises to any gate kept on consequence rather than frequency, which `conventions.md` §14 now permits. §9's two affected diagrams are corrected, each carrying its own correction note. §7's three candidates re-checked and unchanged |
| 8 | Evidence sufficiency | ❌ | ✅ | **Both failing rows are repaired and the count is now honest.** E11 carries `4 of 6` with the cause named; E12 is narrowed to the textual gate it actually passes; **E14** is a new row carrying the third outcome as `DEFERRED` with the blocker named — *no such case exists in the nine-review corpus* — on the Phase B precedent for an unexercised branch. Verdict moved from `13/13 VERIFIED` to `13/14 VERIFIED, 1 DEFERRED`, which is what the evidence supports. Six new source checks all hold (C23-C28), including DoD-7's verbatim text behind the new excess rebuttal. **And one of them overturned my own first-pass finding** — D2 was my error; the executor was right that the quotation was verbatim |
| 3, 4, 5, 7, 9, 10 | tech debt · style · observations · evidence completeness · compatibility · safety | ✅ | ✅ carried | Untouched by the corrective pass. One addition to row 3's ledger: RF §6 gains **obs. 7**, which reports a defect in *my own REVIEW* and in the AC written from it, routed to the coordinator. An executor filing an observation against the reviewer, with both line numbers, is the trust protocol working in the direction it is usually not tested in |

## Purpose Check — row 2 clause (a), second pass

**Reference set.** HL-TFW-53 at frozen baseline `e8ee76e`, unchanged — `git diff` confirms no frozen section
moved (V15, command 16). North star still ruled but not designated, so the declared fallback is in use.

**Citation and harm.** Serves §1 Vision — *"Research can no longer edit them; it can only propose an
amendment, with evidence, into a visible Amendment Log, and wait for an explicit owner verdict"* — and the
corrective pass is the clause working under load, on the task's own contract. The truncation originated in
research iteration 2 and had reached the HL. Under the mechanism this task ships, the coordinator corrected
the two **free** sections (§2, §9), appended a correction of record below §12, and **refused to rewrite A6's
row** — because §12 is append-only and a log that edits its own evidence after the fact answers nothing. The
harm avoided is exact and would otherwise have been invisible: had A6's Evidence cell been quietly repaired,
no reader could ever have learned that the amendment was ruled on a belief that did not survive checking,
and the amendment's real ground — the structural argument — would have been indistinguishable from a
retrofit.

**Excess and adjacency — no.** The pass touched four files where the TS authorised four, changed one
blockquote plus the trims AC-14's own bullet directs (*"pay for it inside the same block"*), and reopened
nothing: mechanism, corpus, and AC-1 to AC-12 all untouched, verified. No substitute example was hunted for,
which is the DoF item most easily violated by an executor wanting a clean row.

**Deferral confession — no.** E14 is the opposite of one: the unexercised branch is declared as a status a
reviewer can audit rather than a sentence they must notice.

**Materiality.** The three residual findings (D4, D5, D6) are all Low and none names a material harm — a
measurement of an intended design choice, a row misordering, and a missing two-line ledger.

**Outcome: ✅ aligned.**

## Checkpoint — second pass

- [x] Both failing rows re-ruled against evidence, not against the RF's assertion that they were fixed
- [x] Row 2(a) re-answered against the baseline and the north-star fallback, with a quoted clause and a named harm
- [x] Rows 7 and 8 still answered separately — 7 asks whether E14 exists, 8 asks whether `DEFERRED` is the honest status for it
- [x] Carried-forward rows named explicitly rather than silently re-ticked
- [x] First-pass findings each closed, withdrawn or carried, with the reason stated — D1 closed, **D2 withdrawn as my error**, D3 closed
- [x] New findings recorded rather than smoothed over — D4, D5, D6, all Low

Stage complete: YES
