# REVIEW — TFW-53 / Phase C: Goal Defence in Review

> **Date**: 2026-08-13
> **Author**: Reviewer (Claude Code)
> **Verdict**: ✅ **APPROVE** — second pass, 2026-08-13. _(First pass: 🔄 REVISE, three items — all three discharged; see §8.)_
> **RF**: [RF Phase C](RF__phase-c__goal_defence_in_review.md)
> **TS**: [TS Phase C](TS__phase-c__goal_defence_in_review.md)
> **Reference set** (Purpose Check): HL-TFW-53 at frozen baseline **`e8ee76e`**, recovered per `conventions.md` §3 rule 15 · north star ruled but not designated → declared fallback (master HL §1 at the baseline) in use
> **Stage files**: [`review/map.md`](review/map.md), [`review/verify.md`](review/verify.md), [`review/judge.md`](review/judge.md)
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

The Judge's row 2(a) asked **mapping integrity** — does every TS §3 Principles Check row resolve to an AC
that was met? — a question structurally unable to detect a principle violated by the mapping itself, and it
had two live statements (`judge.md` row 2, `review.md` Step 3). Both are gone. In their place: a **Purpose
Check** answered against the master HL at its committed frozen baseline plus the Project North Star, with the
TS and any Phase HL named invalid. The enforcement sits in a block **below** the table — one fused field
(quote the clause served *and* name the concrete harm), three tests, an override clause, three outcomes —
which is why the whole mechanism cost `review.md` 111 words and cost clause (b) nothing.

Six supporting files, two new evidence artifacts, **99 insertions / 8 deletions**, zero new framework files
a project upgrading must create. Three decisions carry the design: the mechanism is a block rather than a
longer row; the third outcome is a *finding* rather than a fourth status glyph (so it cannot collide with
Phase E's `❌ REJECTED`); and the `README.md` board row was left uncommitted because a concurrent TFW-55
session holds the file.

## 2. Verify

> Min verify ratio 0.42 → 4 of 9 files required. **Escalated to 9 of 9 (100%)** on discrepancy D1.
> Raw log: [`review/verify.md`](review/verify.md).

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | All 9 changed files opened and compared against RF §1 | ✅ 8 clean, 1 partial | V1-V9. Every claimed change is present; no undeclared change found |
| 2 | Every AC gate command re-run independently | ✅ reproduces exactly | `mapping integrity` → 0/0 · rows → 10 · `review.md` lines 28/87/102 · `wc -w` 1,065 → **1,176** · `conventions.md` numstat **`27 0`** · recovery-form grep → 2 hits |
| 3 | Test suite re-run | ✅ **68 passed** in 32.81s | Matches the RF's 68 |
| 4 | 22 replay citations traced to the commits the replay names | ⚠️ 20 verbatim, 2 flagged | C1-C22. Every clause, every line count (`3,160`, `1,708`), commit `1ebb680`, and `process.md` F22 all resolve |
| 5 | Replay row 49/A re-read against its own source | ❌ **discrepancy D1** | §1 reads *"readable without special tooling, **while structural validation prevents quiet drift**"* — the clause the row treats as contradicting DoD-3 is the clause that asks for it |
| 6 | ONB §7 knowledge citations | ✅ **32 of 32**, 0 hallucinations | Ten D-records, six philosophy F, seven process F, two constraint F, three `.tfw/README.md` headings at the claimed lines |
| 7 | HL diff from baseline `e8ee76e` to HEAD | ✅ no unlogged frozen edit | Status field, the Step 3/4 stale-pointer correction, the deliverable renumber, one §8 row, S38, the A14 row — all free-section or non-substantive under rules 6/7 |
| 8 | Frozen DoD 18-29 coverage | ✅ 12 of 12 mapped | Including DoD-23, whose AC gap the executor reported and the coordinator closed as AC-12 |
| 9 | RF §5 evidence rows | ⚠️ 11 of 13 establish their claims | E11 and E12 rest on D1. The two divergences the RF *does* disclose (E1, E3) are disclosed well |
| 10 | HL §4 deliverable 2 vs the shipped north-star rule | ⚠️ **D3** | HL says *"the root `README.md`"*, the framework now ships *"section(s) of a README"*. Legitimate under rule 6; the deliverable text was never refined to match → coordinator |
| 11 | Adapter copy this review was invoked through | ⚠️ **D4** | `.claude/commands/tfw-review.md` still instructs the retired check. Canonical `.tfw/workflows/review.md` followed instead. TD-157, Phase D |

**Nothing was unverifiable.** No claim in the RF required an environment this reviewer could not reach.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ✅ | 12 of 12 ACs pass on re-run gates; 12 of 12 frozen DoD items mapped. AC-11 recounts to **4 of 6** after D1 and its `≥1` condition still holds; AC-12's gate is textual and passes independently |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ✅ | **(a) aligned.** Serves §1 Vision's five commitments — *"the contract gains a defender … alignment can no longer be asserted without citing the clause it serves"* — every one now a failing condition in the template filled every review. Harm removed is measured: the retired check scored `✅` on TFW-48/A by mapping onto a Phase HL that authored **its own ten** principles where the master had thirteen, so master P7/P10/P12 were invisible to the row. No excess, no deferral confession. **(b)** sound — the block-not-row choice is what keeps (b) separately answerable and F2 unpaid |
| 3 | Tech debt documented | ✅ | Six observations with file, line, type and destination; five survive the filter |
| 4 | Style & standards | ✅ | D55 commit grammar; HL §4 vocabulary shipped verbatim with no synonym; F13 held (no project name in any template); `P16` deliberately not cited inside `judge.md` because `P{n}` is task-local; F22 held |
| 5 | Observations collected | ✅ | Obs. 1, 2, 3, 5 promoted; obs. 4 rejected as filler (names no defect, predicts a future editor's temptation); obs. 6 is KNW routing, not debt |
| 6 | RF completeness (§7-9 present) | ❌ | All three sections present and mostly strong — §9's three diagrams are the best in this task. **S2's premise fails.** *"The check found its own predecessor's defect while being validated on it"* rests on the 49/A ruling D1 removes; S2 is High confidence and headed for `KNOWLEDGE.md` |
| 7 | Evidence completeness — does it exist? | ✅ | 13 rows, valid statuses, both attachments resolve, D53 folder shape. The two *"N/A — textual"* ACs still carry reproduced commands |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | 11 of 13 establish. **E11 and E12 do not** — replay 49/A rules a contract defect on a half-sentence (D1); its outside confirmation (TFW-50) proves two contracts differed, not that one contradicted itself. Secondary: the 48/A note quotes *"preserves all ten mapped principles"* where the source reads *"preserves Phase HL P1–P10"* (D2) |
| 9 | Backward compatibility | ✅ | The only broken consumer class is the adapter copies, and that window was already open (TD-157, from Phase B's `plan.md` changes) — this phase widens the same window, TS §2 scopes it out, Phase D closes it. No section number, anchor or template section moved; docs pipeline builds clean |
| 10 | Safety | ✅ | No secrets, credentials or destructive operations. The one irreversible act — deleting the mapping-integrity check from both sites — is DoD-20's instruction and DoF-11's requirement. The `README.md` restraint was the safety-relevant call and it was right |

## 4. Verdict

**🔄 REVISE**

Eight of ten Judge rows hold, twelve of twelve acceptance criteria pass on gates this reviewer re-ran, and
the mechanism the phase exists to ship is **correct and well-built**. The Purpose Check is where P3 requires
it — in the template filled every review, not in workflow prose — the fused field makes `✅` cost work, the
materiality bar shipped in the same pass instead of being retrofitted after a false positive, and the block
below the table is a genuinely better answer to TS §8's *"row 2 grows into a paragraph"* risk than discipline
would have been. The Purpose Check run against this work returns **aligned**: it is what we set out to do.

It fails on **evidence sufficiency** (row 8), and the failure is specific. Replay row 49/A rules TFW-49
Phase A a **contract defect** — the third outcome — on the grounds that §1's *"readable without special
tooling"* cannot be jointly satisfied with DoD-3's versioned structural validator. The quoted sentence does
not end where the row ends it. At `9e19a4f:…HL-TFW-49…`:15-17 it reads:

> "The identity remains readable without special tooling, **while structural validation prevents quiet
> drift** between Coordinator, Researcher, Executor, Reviewer, adapters, and repositories."

§1 asks for both properties in one breath. DoD-3's validator is that clause discharged, not its contradiction,
and DoF-8 — which forbids enforcement resting *only* on prose or *only* on unversioned `.git/` state — is
satisfied by any versioned check. No pair of clauses here is jointly unsatisfiable. The row's own outside
confirmation, TFW-50's approved *"one precise Markdown rule … without enforcement software"*, ran under a
**different** HL where no DoF-8 existed; it evidences a change in the owner's preference between two
contracts, not an inconsistency inside one. And the row already concedes the alternative reading is
*"arguable at most … the clause asked for one"* — which lands on `✅ aligned`, exactly where research
iteration 2 put it before amendment A6 existed.

**Why this is REVISE and not APPROVE-with-debt.** Three of the four consequences are contained — AC-11
recounts to 4 of 6 and still passes, AC-12's gate is textual and passes independently, and the replay's other
eight rows are sound with all twenty-two of their citations traced. The two that are not contained both leave
this task's trace: the illustration is **shipped into every install**, where it teaches reviewers that surface
tension is unsatisfiability, three paragraphs below the rule that *a citation that resolves but is irrelevant
fails the row*; and S2 is a High-confidence strategic insight bound for `KNOWLEDGE.md` at KNW, so approving
it writes a false fact into project memory that later work will cite. Both are cheap to fix now and expensive
after Phase D's version bump ships the template.

**Why this is REVISE and not REJECT.** Nothing fundamental is wrong. No HL or TS rework is needed, no
acceptance criterion fails on its gate, no DoF item triggered, and the Purpose Check does not fire. The
design, the scope discipline and the reporting posture are all better than the phase needed them to be — the
executor disclosed both divergences (clause (b)'s three words, AC-3's unclearable gate) in the row, the
verdict block and the RF rather than downgrading them to `DEFERRED`, flagged the frozen DoD-23 coverage gap
instead of implementing around it, and wrote up the TFW-42/A near-miss when smoothing it over would have made
the replay look stronger. That candour is what makes a three-item revision the right instrument.

### If REVISE — items to fix:

1. **Re-score replay row 49/A against the full §1 sentence.** Quote it to its end, state that §1 pairs
   readability with structural validation, and record the outcome the shipped check actually returns
   (`✅ aligned`, or a fire on excess grounds if the 1,708-line delivery is argued that way — but not the
   third outcome). Propagate: `purpose_check_replay.md` §1 and §3, the §0 note about the research divergence,
   the §3 AC-11 condition table, **EV E11 and E12**, RF §3 AC-11 and AC-12 (drop *"Exercised for real: replay
   row 49/A"*), RF §2 decision 6, and RF §5's `13/13`.
2. **Repair the shipped precedent line in `judge.md`.** It currently offers this same reading as the canonical
   illustration of a contract defect. Either substitute a pair of clauses that genuinely cannot be jointly
   satisfied, or reword it so it does not present surface tension as unsatisfiability. This is the item that
   matters beyond this task — it ships. If no genuine example is available in the corpus, saying so and
   describing the *shape* abstractly is better than shipping a weak one.
3. **Correct RF §8 S2, and the 48/A quotation.** S2's premise is gone; what survives is a smaller and still
   real insight — the replay is worth re-running whenever the check changes, and here the re-run *confirmed*
   research's original verdict rather than overturning it. Rewrite it as that, or withdraw it. Separately,
   the 48/A note's *"preserves all ten mapped principles"* is a paraphrase inside quotation marks; the source
   reads *"preserves Phase HL P1–P10"*. Fix the marks — in this phase of all phases, the form is part of the
   deliverable.

**Not required, explicitly:** no re-run of the corpus, no change to the shipped mechanism, no change to any
of the seven framework files other than item 2's one sentence, and no new evidence. AC-11's pass condition
holds at 4 of 6 and the 0-of-3 sound-corpus result is untouched — this is a correction of one reading, not a
re-validation.

### If REJECT — fundamental issues:

None. No HL or TS rework is required.

> **The Purpose Check on this work: ✅ aligned.** Recorded explicitly because the phase's own thesis is that
> the two questions are orthogonal, and this review is the first live demonstration: the work **is** what we
> set out to do, and two of its thirteen evidence rows still do not establish what they claim.

## 5. Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| TD-164 | RF TFW-53/C §6 obs. 1 | **High** | `.tfw/templates/HL.md`:10 | **The baseline recovery command has a fourth copy, in the template every future HL is born from.** Amendment A13 removed the command form from `HL-TFW-53` at all three occurrences and pointed at `conventions.md` §3 rule 15 — applied to the artifact, not to the template. Every new HL is still born carrying a command form rule 15 exists to own in one place, and AC-3's gate cannot pass while it stands. AC-7 forbade this phase to touch the contract block | → Phase D (or whoever next owns `templates/HL.md`) |
| TD-165 | RF TFW-53/C §6 obs. 3 | **Medium** | `.tfw/compilable_contract.md`:81 | **`NS{N}` and `PP{N}` are declared in the §2 pattern table with no resolution behaviour.** The Resolution rules list still reads `D{N}, P{N}, F{N}, TD-{N} → anchor links`. A pattern that resolves nowhere is F4's shape — a rule with no enforcement site — and the build script will silently not link the two namespaces this phase created. AC-9's *"one table, nothing else in that file"* boundary is why it stays | → Phase D, with TD-155 |
| TD-166 | RF TFW-53/C §6 obs. 5 | **Medium** | `.tfw/templates/review/verify.md` | **Verify checks that citations *resolve*; nothing checks that they are *relevant*.** The Purpose Check now demands a relevant citation and the fused harm field is the only guard, inside Judge. SS2 named this exact shape: *a citation that resolves is not a citation that is relevant*. **Promoted from Medium on independent evidence — this review's own D1 is an instance:** a citation that resolves, whose truncation reverses its meaning, passed Verify and had to be caught in Judge | → backlog; candidate for the next `review.md`/`verify.md` pass |
| TD-167 | RF TFW-53/C §6 obs. 2 | Low | `.tfw/compilable_contract.md`:65 | A second stale `KNOWLEDGE.md` §0 reference, six lines below the one AC-9 corrected: *"Where references appear"* still opens with *"`KNOWLEDGE.md` §0 Source column"*, removed by D37 in April | → Phase D, with TD-155 |
| TD-168 | REVIEW TFW-53/C verify.md D3 | Low | `tasks/TFW-53*/HL-TFW-53*.md` §4 Phase C deliverable 2 | **The HL deliverable no longer describes what shipped.** It reads *"Locus: a designated section of the root `README.md`"*; the framework now ships *"designated section(s) of a README"* with more than one location permitted, on the owner's ONB Q2 ruling (S38). Legitimate under `conventions.md` §3 rule 6 — deliverable lists are free and the tripwire clears — but the text was never refined, so the contract now reads narrower than the rule it produced | → coordinator (executor and reviewer are both role-locked out of the HL) |

**Rejected by the quality filter:** RF §6 obs. 4 (*"Step 3 now has two named things a reader must hold
apart"*) — names no defect and predicts a future editor's temptation; nothing breaks if it is never
addressed. RF §6 obs. 6 is not debt but a KNW routing note and is handled in §6 below.

**Already tracked, re-confirmed live rather than re-filed:** TD-157 (adapter copies instruct the retired
review flow — this review session was itself invoked through the stale `.claude/commands/tfw-review.md`,
which still carries *"Quality guardian."* and the deleted `HL §7 Principles check` paragraph; the canonical
workflow was followed instead) · TD-155 (re-routed to Phase D at ONB R4) · TD-134 (`build.lint` is an
unconfigured starter placeholder; the docs pipeline substituted, per the Phase A/B precedent).

## 6. Traces Updated

- [x] README Task Board — status set to **🔄 REVISE (C)**. ⚠️ The row is in the working tree **uncommitted**,
      because a concurrent TFW-55 session holds `README.md` and the owner ruled at ONB §5 risk 5 that the
      board row is theirs to land. This review adds nothing to the index.
- [ ] HL status — **not updated.** Phase C does not complete on a REVISE verdict, and §4 deliverable 2 needs
      the TD-168 refinement, which is the coordinator's to make.
- [x] project_config.yaml — no `initial_seq` change needed
- [x] Other project files — checked; TECH_DEBT.md updated with TD-164 … TD-168
- [x] **tfw-docs: Applied 2026-08-18** — one pass across Phases A–E. `KNOWLEDGE.md` §1 Adapters row (drift check), **D63** contract · **D64** purpose defence · **D65** rejected trace; §2 three artifact rows; §3 six new legacy entries plus the TFW-48/49 row re-pointed at the post-mortems. `TECH_DEBT.md`: TD-176/177/178 added, TD-156 closed, TD-169(a) closed.
- [x] **tfw-knowledge: Applied 2026-08-18** — one pass across Phases A–E. **25 facts** written (105 → 130): philosophy +8, process +5, stakeholder +4, constraint +3, environment +2, convention +2, and a new `knowledge/risk.md` +1. Six candidates rejected, the stalest being the `spec` review-mode preference, which TFW-56 deleted. `fact-candidates: processed` markers set on HL §11 and on all ten RF/REVIEW §7 sections.
  _Original note (blocker cleared at the second pass):_ Deferred, and blocked on revision item 3 — RF §8 S2 must be corrected or withdrawn
      before it enters `KNOWLEDGE.md`. RF §6 obs. 6 (D46's half-shipped identity and the retention finding,
      HL §2 / iter2 G7) belongs in the same batch and is not blocked

## 7. Fact Candidates
> fact-candidates: processed 2026-08-18 (`/tfw-knowledge`, TFW-53 A–E)


> Reviewer-observed, from this review and from the conversation record behind it. The three candidates in
> RF §7 all hold and are not restated here.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | **A replay used as an acceptance test needs its citations re-read at full sentence length, not just resolved.** This phase's replay traced 22 quotations to real commits and 20 were verbatim; the one that failed, failed by ending a sentence early, and its truncation flipped the row's outcome from `aligned` to `contract defect`. The general form: for evidence that is *interpretation of a quotation*, the verification that catches errors is re-reading the source sentence to its end — link-resolution and verbatim-match both pass a truncation | REVIEW TFW-53/C D1; `verify.md` C6 | High |
| 2 | process | **Two independent sessions in one working tree has now shaped three consecutive artifacts of this task, and the discipline still lives nowhere durable.** Phase B swept a sibling's deletions into its commit (TD-144); Phase C's ONB was committed by generating the full diff and applying only its own hunk to the index — a manoeuvre no workflow describes; Phase C's RF and this REVIEW both leave the board row uncommitted on a per-run verbal instruction. Three different answers to one problem, none of them written down. The concrete missing artifact is small: a staging rule in `handoff.md` and `review.md` — stage by explicit path, and what to do when a shared file carries someone else's hunk | RF TFW-53/C §8 S3; RF TFW-53/B S1; TD-144; this review's §6 | High |
| 3 | philosophy | **The framework's self-test is cheap, was not being run, and has now caught two defects at the same seam.** *Can this repository satisfy the rule it is shipping?* caught the PV priority-1 relabel at ONB (the rule was true everywhere except the project that authored it — RF §8 S1). The same question applied to this review caught D1: the phase whose thesis is *alignment must be cited, not asserted* shipped an illustration built on a truncated citation. Both defects sit exactly where "framework" and "project" are assumed distinct | RF TFW-53/C §8 S1; REVIEW TFW-53/C D1-D2; HL §11 S38 | High |

---

## 8. Second Pass — ✅ APPROVE

> **Under review:** `2642e81` (coordinator — HL §2, §9, §12 note, TD-168 closed), `7e5311d` (coordinator —
> TS AC-13 to AC-15, four DoF items), `bd032a5` (executor — `judge.md`, RF, EV, replay).
> **Files opened:** 6 of 6 — the four changed plus the HL and TS. Ratio required 2.
> **Stage detail:** [verify.md](review/verify.md) second-pass section — V10-V16, C23-C28, D1-D6 · [judge.md](review/judge.md) second-pass section.

### 8.1 The three items

| # | First-pass item | Status | What was verified |
|---|-----------------|:---:|-------------------|
| 1 | Re-score replay row 49/A against the full §1 sentence; propagate to eight sites | ✅ **discharged** | §1 quoted to the end of its sentence (verbatim, C23); outcome `✅ aligned`; the excess reading argued and **rejected** against DoD-3 and DoD-7, whose text I traced verbatim (C25); TFW-50's confirmation dropped with the reason; **8 of 8** sites landed — replay §0/§1/§3 diagram/§3 table/§4, EV E11/E12/E14, RF §2 d6/§3/§5/§8/§9. AC-11 recounts to **4 of 6**, condition `≥1` holds, sound corpus untouched at 0 of 3 |
| 2 | Repair the shipped precedent line in `judge.md` | ✅ **discharged, and improved on the ask** | The blockquote no longer offers a case to pattern-match. It states the **bar**: two clauses conflict only if satisfying one *necessarily* violates the other · read each to the end of its sentence · surface tension is not inconsistency · coherent-but-wrong is the purpose question · **no instance has been observed**. No substitute example was hunted for, which was the DoF item easiest to violate. `1,167 → 1,165` words, `review.md` untouched at 1,176 |
| 3 | Correct RF §8 S2, and the 48/A quotation | ✅ **discharged — and the second half was my error** | S2 rewritten with the withdrawal marked inline, so a KNW reader sees what changed; **new S4** added. On the quotation: see §8.2 |

### 8.2 A correction to this review

The first pass claimed *"preserves all ten mapped principles"* was a paraphrase sitting inside quotation
marks. **It is verbatim**, at `REVIEW__phase-a__method_kernel.md`:**51** (§4 Verdict). I compared it against
`phase-a/review/judge.md`:12 — the stage file, a different document — found different wording there, and
called the quotation inaccurate without opening the file it came from. The sentence I offered as the true
source, *"Phase HL P1–P10 all pass through their mapped ACs"*, is line **38** of that same REVIEW file. Both
sentences are real; both support the point (C26, C27).

The executor did not comply. They verified both sources, kept the quotation, added line numbers to each half,
and filed RF §6 obs. 7 recording that TS AC-15's second bullet *"asks for a fix that would have introduced
the defect it was written to remove"*. That is the correct response to a wrong instruction from a reviewer,
and it is the discipline this phase ships: the claim was checked against the source instead of obeyed. The
finding routes to the coordinator, who wrote the AC from my text.

### 8.3 What the corrective pass did better than the ask

Three things, recorded because a review that only reports gaps is not measuring the work.

**The coordinator refused to rewrite A6.** The truncation originated in research iteration 2 and had reached
three HL sections, not only the replay. §2 and §9 are free sections and were corrected; §12 is append-only
and was **appended to** — A6's Evidence cell stands as written, with a correction of record below the table.
A6's verdict stands and the third outcome ships on its structural argument alone; what is withdrawn is the
claim that an instance had been observed. Had the cell been quietly repaired, no later reader could learn
that the amendment was ruled on a belief that did not survive checking. `git diff e8ee76e HEAD` confirms no
frozen §1/§3/§5/§6/§7 edit, and A6's row byte-identical.

**The replay's weakest row became its most informative.** Row 49/A now records that TFW-49 Phase A was
**aligned with its approved contract** while the owner rejected the product — and routes that case to the
north star, because nothing inside row 2(a) could have caught it. That is empirical support for the
deliverable weighting HL §4 declares (*"the only defence against a task whose own approved HL is wrong for
the product"*), which the first pass did not have. The corrected row is worth more than the wrong one was.

**The unexercised branch is a status, not a sentence.** E14 carries the third outcome as `DEFERRED` with the
blocker named, and the absence is stated in three places a later reader will actually reach — `judge.md`'s
own text, HL §9's `Unmeasured` risk row, and the EV row — rather than only in this task's trace.

### 8.4 Judge, second pass

| # | Check | 1st | 2nd |
|---|-------|:---:|:---:|
| 1 | DoD met? | ✅ | ✅ — **15 of 15** ACs on their gates; TS §7's sixteen DoF items clear, count reproduced |
| 2 | Purpose Check + design soundness | ✅ | ✅ — re-run against the changed block; the bar is a better artifact than the example it replaced |
| 6 | RF completeness (§7-9) | ❌ | ✅ — S2's false premise gone, withdrawal marked inline, S4 added, both diagrams corrected |
| 8 | Evidence sufficiency | ❌ | ✅ — E11 recounted, E12 narrowed, E14 added; `13/14 VERIFIED, 1 DEFERRED` is what the evidence supports |
| 3, 4, 5, 7, 9, 10 | tech debt · style · observations · evidence completeness · compatibility · safety | ✅ | ✅ carried — untouched by the pass |

### 8.5 Residual findings — three, all Low, none blocking

| # | Finding | Disposition |
|---|---------|-------------|
| D4 | **`judge.md` is now 1,165 words — the largest artifact of its class in the repository**, 1.7× `REVIEW.md` (679), 2.2× `TS.md` (533), and effectively the weight of `review.md` (1,176), the workflow it serves. It grew **639 → 1,165, +82%**, in this phase. **Not a violation:** frozen DoD-28 *directs* the mechanism into the template because *"a template is not a workflow"*, HL §4 states that choice, and the coordinator installed the no-growth rule the moment it mattered (AC-14, met at −2 words). What is new is the measurement, and it is TD-140's shape one artifact over | → appended to **TD-141** as evidence |
| D5 | EV rows run E1…E12, **E14, E13** — `E14` inserted above `E13` rather than appended, while RF §4 still reads *"EV E1-E13"*. Rows are cited by identifier | → **TD-169**, correct at `/tfw-docs` |
| D6 | The `judge.md` trim that paid for AC-14 is disclosed as *"paid inside the same block"* with no ledger. AC-14 required none, so not a gate miss — but AC-5 required one for `review.md` for exactly this risk. I diffed it: four rhetorical removals, **no mechanism lost** | → **TD-169**, two lines at `/tfw-docs` |

### 8.6 Verdict

**✅ APPROVE.**

All three revision items are discharged, and one of them was discharged by the executor demonstrating the
reviewer was wrong — with both sources cited and the finding filed as an observation. Fifteen of fifteen
acceptance criteria pass on gates re-run in this session; the two Judge rows that failed are repaired against
evidence rather than against assertion; the evidence verdict moved from an overclaimed `13/13` to an accurate
`13/14 VERIFIED, 1 DEFERRED` with the blocker named; and no frozen section moved outside the append-only
channel this task exists to build. The three residual findings are Low, none names a material harm, and all
three are tracked.

The shipped mechanism is the same one the first pass called correct and well-built. What changed is that its
one weak artifact — an illustration built on a citation that resolved and misled — is now the discriminating
test for the outcome it illustrated. **Purpose Check on the corrective pass: ✅ aligned.**

### 8.7 Traces — second pass

- [x] README Task Board — **📚 KNW (A, B, C)**, REVIEW cell `[C✅]`. ⚠️ Still **uncommitted**: the concurrent
      TFW-55 session holds `README.md` and the owner lands the board row.
- [x] TECH_DEBT.md — TD-141 extended with D4's measurement; **TD-169** filed for D5 and D6; TD-168 confirmed
      closed by the coordinator
- [ ] HL status — reads *"Phase C 🔄 REVISE — three narrow corrections in flight"*; now stale on APPROVE.
      → coordinator (role lock)
- [x] **tfw-docs: Applied 2026-08-18.** `KNOWLEDGE.md` §1-§3 updated (D63/D64/D65) plus the TECH_DEBT rows above
- [x] **tfw-knowledge: Applied 2026-08-18.** Six fact candidates — RF §7's three and §7 above's three — plus RF §6
      obs. 6 (D46's half-shipped identity and the retention finding). Phase C reaches ✅ DONE when both are
      marked Applied

---

*REVIEW — TFW-53 / Phase C: Goal Defence in Review | first pass 🔄 REVISE · second pass ✅ APPROVE | 2026-08-13*
