# REVIEW — TFW-53 / Phase B: Enforcement in Workflows

> **Date**: 2026-08-13
> **Author**: Reviewer (Claude Code)
> **Verdict**: ✅ **APPROVE** — with four documentary corrections carried to KNW and one open owner decision
> **Verdict history**: first pass 2026-08-13 → 🔄 REVISE on discrepancy D1. Owner waived D1 the same day
> (*«они там напутали коммиты… можно не обращать внимание»*) — the finding stands on substance and is carried
> by TD-144, but no longer counts against this phase. Re-ruled ✅ APPROVE. Both stage-file addenda record the
> change; nothing in the first pass was rewritten.
> **RF**: [RF Phase B](RF__phase-b__enforcement_in_workflows.md)
> **TS**: [TS Phase B](TS__phase-b__enforcement_in_workflows.md)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

Phase A wrote the HL contract into the artifacts; nothing enforced it, and `plan.md` still carried two
instructions telling the coordinator to do what the contract forbids. Phase B replaces both with
classification: Step 6c routes each research recommendation by **target section + `conventions.md` rule 6**
— never by the label the researcher attached — applying free units and transcribing frozen claims into HL
§12 as `PROPOSED`, with one batched escalation per iteration. Step 4 turns approval into a written
`Contract` field plus a freeze commit before the first research iteration. A new **6d** block handles
amendment verdicts wherever they arrive, placed outside the research loop on a measurement: 4 of this
task's own 13 §12 rows entered from an executor ONB or from the owner during execution.
`research/base.md` Step 6 splits one recommendation table into `Refinements` / `Amendment Proposals`.
`plan.md` went 1,206 → 1,195 words by removing 13 measured duplication sites.

Two corrective passes rode along, both disclosed and both classified before the file was touched:
`templates/RES.md`:133 (the third live "update HL", authorised at ONB Q2) and `templates/HL.md` §3.1
(rewritten on owner authorisation mid-execution).

## 2. Verify

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | `plan.md` — Step 4, Step 6c, 6d, 13 removals | ✅ | verify.md V1. All mechanisms present and worded as claimed |
| 2 | `min_iterations` hard gate survived the 6c rewrite | ✅ | verify.md V2 — `diff` of old vs new gate block returns **exactly one** changed line, the one AC-2 required. D38's only statement of the floor is intact |
| 3 | `research/base.md` — class names vs `templates/RES.md` | ✅ | verify.md V3. `Refinements` / `Amendment Proposals` verbatim; free/frozen section sets identical; `wc -w` = 943 |
| 4 | `templates/RES.md` — the ONB Q2 limit ("line 133 and nothing else") | ✅ | verify.md V4 — `git show --stat` reports `2 +-`, one line |
| 5 | `templates/HL.md` §3.1 — frozen DoD-11's four properties survive | ✅ | verify.md V5 — checked clause by clause against HL:581. The 14-word negation is gone by construction, as claimed. 1,894 → 1,823 words |
| 6 | AC-2 gate reproduced | ✅ | `grep -n "[Uu]pdate HL" .tfw/workflows/plan.md` → 0; repo-wide `.tfw/**/*.md` → 0 |
| 7 | AC-5 gate reproduced | ✅ | `grep -niEc` over both workflows → `0`, `0` |
| 8 | AC-6 both endpoints reproduced with one command | ✅ | `wc -w` → 1,195 now; `git show fbdf443~1:… \| wc -w` → 1,206 |
| 9 | Build gate re-run | ✅ | `python -m pytest docs/scripts/ -q` → **68 passed** in 32.86s |
| 10 | Freeze-commit recovery form | ✅ | Returns exactly **6** commits — matches RF Decision 8. `8136306` confirmed absent from it (EV divergence 1 is real) |
| 11 | 30 Knowledge Citations (HL §7.2 + ONB §7) | ✅ | verify.md — 30/30 resolve, **0 hallucinations** |
| 12 | 9 key claims spot-checked against primary sources | ⚠️ 7 hold, **2 false** | verify.md C1-C9. HL:724 confirms the unlogged Q5 edit; `TECH_DEBT.md` confirms the 1,205/1,206 delta; C1 and C2 fail |
| 13 | **Commit file set vs TS §4** | ❌ | verify.md V8 / D1 — `git show --stat fbdf443` lists **six** files, not three |

**Verification ratio:** ⌈7 × 0.42⌉ = 3 required. **Escalated to 100% on discrepancy D1** — 10 files opened
(the 7 the RF claims, plus the 3 it does not).

**What could not be verified:** AC-3's *rejected* verdict path. Not a reviewer limitation — the corpus
contains no rejected amendment (13 §12 rows = 12 `✅ APPROVED` + 1 `🚫 WITHDRAWN`). The RF's `DEFERRED` is
the correct status and names the blocker precisely.

### Discrepancies

**D1 — `fbdf443` modified three files outside TS §4, and no artifact of this phase says so.** *(High)*
The commit deletes `.tfw/workflows/review/{code,docs,spec}.md` — 39 lines belonging to concurrent task
TFW-56. TS DoF-4 (*"any file outside the two named in §4 is modified"*) is triggered in letter.
**Substance is unharmed:** those deletions are TFW-56's own approved work, the end state is correct, and
this executor authored no content change to them — a directory-level stage (`git add .tfw/workflows/`,
which reaches `review/*`) is the only mechanism that fits. **The trace is harmed and irreversibly:** asking
git when TFW-56 removed the mode files now returns a commit reading `[claude-code/TFW-53/phase-b/executor]`.
The framework-level debt is already registered as **TD-144 (High)** from TFW-56's side. What is missing is
any acknowledgement in the artifact under review — and RF §8 S1 argues, correctly, that under concurrency
the commit subject becomes the only record of which task a change belongs to. The document making that
argument also asserts in Decision 14 that the discipline was kept.

**D2 — `templates/HL.md` is a fourth modified file and RF §3 still says "three".** *(Medium)*
RF §1's table lists four modified files; RF §3's DoF clearance line reads *"no file modified outside TS §4's
three"*. The `templates/HL.md` pass itself is handled properly — owner-authorised, classified against rule 6
before being touched, disclosed as Decision 13, with the RF stating plainly that adding the TS §4 entry is
the coordinator's act. But the one line a reviewer reads as the DoF self-check is the line that is wrong.

**D3 — an authorised removal was not disclosed, against an explicit ONB condition.** *(Medium)*
The coordinator's ruling on ONB Inconsistency 1: *"Remove it. Authorised, and it is not a budget trim…
**State the reason in the RF so the saving is not counted as compression.**"* The dead reference at
`plan.md`:97 (`conventions.md` §4 "Agent selection guidance", removed by D50) is gone from the file, and
`grep -niE "agent selection|D50|:97"` over the RF **and** the EV returns 0 matches. EV Exhibit B's 13-row
ledger does not itemise it, and its own reconciliation admits an unexplained 2-word gap. So 9 of the 11
words AC-6 attributes to duplication removal came from a correctness fix instead.

**D4 — RF §2 skips Decision 12.** *(Low)* The list runs 1–11, then 13, 14.

> **Owner ruling 2026-08-13 — D1 waived.** *«задача делалась параллельно с 56-й и они там напутали коммиты.
> можно не обращать внимание»*. D1 stands on substance and TD-144 carries it at High from the TFW-56 side;
> it no longer counts against this phase, and DoF-4 is treated as not triggered for the three
> `.tfw/workflows/review/*` deletions. **D2, D3 and D4 stand** — none is a commit artifact.

### 2.1 Substantive findings — second pass

> Found after the first pass, on a re-read of the shipped text against the rules it cites. **None is a
> failure to deliver what the TS required.** Raw derivation: `review/verify.md` addendum F1-F5.

**F1 — the only half of rule 6 that changes an outcome is not inline.** Step 6c item 3 says *"classify by
target section and rule 6"* and inlines rule 6's **first** half (*deliverable lists inside an approved phase
are free*) while leaving the **second** — the tripwire, *"if the change cannot be accepted under §5 and §6 as
they stand at the moment of classification, it is an amendment"* — as a reference. The replay measures which
half does the work: of 22 real rows, **21 route identically either way; exactly 1 routes differently**, and
that one is a live unlogged edit to a frozen section. `conventions.md` §11 is explicit that
enforcement-critical text must be inline and that a pure reference is broken. **The trade is real:** AC-6
leaves 5 words of headroom, the clause costs ~10, and DoF-2 forbids trimming a mechanism to pay for it. The
executor had no compliant exit and escalated rather than choosing silently. → **owner decision**, TD-159.

> **The mirror image, same budget:** `research/base.md` spent **+74 words** restating class definitions
> `templates/RES.md` already carries in full and the researcher opens anyway — **0 of 22** rows depend on
> that restatement. Across the two files the word budget was allocated inversely to measured value.

**F2 — applying a refinement to a frozen section leaves no record, so the salami pattern stays invisible.**
The free-unit branch reads *"→ apply it"* and requires nothing further. HL §12's own note block states the
risk in the first person — *"three edits to a frozen section under a refinement label is the salami pattern
this task tracks, **and the reviewer should check the classification rather than accept it**"* — and this
reviewer has nothing to check: N successive refinements to §4 produce zero trace. AC-2 and frozen DoD-13
require the application and require no record, so this is a **contract-level gap the working mechanism
exposed**, not an execution defect. → TD-160.

**F3 — the interruption budget is protected on one channel out of four.** Batching governs research output;
6d correctly handles a verdict *arriving* from anywhere; nothing governs **filing** outside the research loop.
Research 8 rows ✅ · executor ONB 2 rows ✗ · owner-during-execution 2 rows ✗ · review 0 rows ✗ — **4 of 13
arrived where no batching rule exists**, and HL §11 S29 records proposals-per-iteration as the design's own
success metric. `handoff.md` and `review.md` sit outside TS §2. → TD-161.

**F4 — the step's paraphrase of rule 6 is broader than rule 6.** *"A free unit inside a frozen one"* against
rule 6's single named unit (a deliverable list inside an approved phase). It saves no reading and widens the
boundary on a first read, in the direction of treating frozen text as free. → TD-162.

**F5 — *"no further measured duplication exists"* has a live counterexample.** `plan.md` Step 2's three
Knowledge Gate modes (`hard` → stop + justification, `soft` → reminder, `off` → skip) are also stated in
`glossary.md`:213, ~50 words. It does not reach the 700-900 range, but it turns the claim AC-6's shortfall
report rests on from a measurement into an assertion. Adjacent defect found in the same check:
`glossary.md`:213 places the gate in *"Phase 0 of `plan.md`"* — `plan.md` has Steps 0-7 and no Phase 0.
→ TD-163.

## 3. Judge

> Ten rows, matching `review/judge.md` one-for-one and in the same order.

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ✅ | **AC-1 – AC-5 fully met and independently reproduced** (§2 rows 1-10). **AC-6 partial and reported:** 1,195 meets F2's ≤1,200 hard threshold and misses the 700-900 working range — but bullet 3 and DoF-2 make reporting the correct outcome, so a declared shortfall is compliance with the criterion's own instruction. **DoF-4's trigger was D1, waived by the owner**; DoF 1, 2, 3, 5 and 6 all clear |
| 2 | Philosophy aligned — mapping integrity + design soundness | ✅ | **(a) 9 of 9 principles hold.** The one row in question, P7 → AC-6, is re-ruled as held: P7 commits to *"everything added is a numbered gate, never a prose block"* and to the budget — every addition is a numbered item, and `plan.md` left the phase **shorter** than it entered, so DoF-3 never came near firing. **(b) Design is sound and unusually well demonstrated:** 6d's placement rests on a count of this task's own §12 rows, and F1 sharpens the compliment — the mechanism's single discriminating case was found *by the mechanism*, on real history, not on a fixture |
| 3 | Tech debt documented | ✅ | RF §6: 7 observations, each with file, lines, type and a stated consequence. Existing debt bounded correctly — TD-134 substitution disclosed, TD-135's trigger verified as not firing, TD-140's remaining half routed to Phase D |
| 4 | Style & standards | ❌ | Template structure, naming and commit grammar all conform. Two defects in the artifact: RF §3 contradicts RF §1 on the file count (D2), and RF §2 skips Decision 12 (D4) |
| 5 | Observations collected | ✅ | All 7 survive the quality filter. Obs. 2 carries its own arithmetic (14 words needed against 5 of headroom); obs. 4 names a live contract-log gap the reviewer independently confirmed at HL:724; obs. 5 names two adapter surfaces that now instruct the opposite of the core |
| 6 | RF completeness (§7-9 present) | ✅ | §7: 3 fact candidates, each sourced to a dated directive. §8: 2 insights with implications drawn, not merely captured. §9: an ASCII before/after of all four instruction sites plus a mermaid graph of verdict entry points annotated with measured counts |
| 7 | Evidence completeness — does it exist? | ✅ | EV file complete: environment header, 8 rows, verdict, 2 exhibits, attachments index. Every TS Evidence field covered; the three `N/A` rows quote the TS's own justification; the one `DEFERRED` names a checkable blocker. All statuses from the fixed vocabulary |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | For AC-1 – AC-5 it does, and better than required — the replay declares its own circularity before its results and still finds a live unlogged frozen-section edit; the history replay reports three divergences against itself. **What the evidence never tested is the file set.** No row, exhibit or command compares the commit's contents against TS §4 — the one check that would have caught D1 — while RF §3 certifies precisely that claim. Second gap: E8's ledger omits the authorised removal (D3) |
| 9 | Backward compatibility | ✅ | Step numbers deliberately stable — `glossary.md`:178 cites `plan.md Step 6c` twice and still resolves; 6d added as a new label; the `min_iterations` gate block byte-identical. `pytest` 68/68 and `mkdocs build` both consume these files. Known consumer lag: the two adapter copies of `plan.md` still carry the old Step 6c — TS §9 assigns that to Phase D, and RF obs. 5 flags the interim contradiction |
| 10 | Safety | ⚪ N/A | The only entry was D1's irreversible misattribution, waived by the owner and carried by TD-144. Reason for N/A, stated rather than assumed: nothing else in this phase touches secrets, credentials or destructive operations — the change set is four markdown files and two new report files |

> **Net: 7 ✅ · 2 ❌ · 1 ⚪.** Both ❌ rows are documentary defects inside the RF (rows 4 and 8), not defects
> in the shipped mechanism. Rows 7 and 8 still land differently — ✅ on existence, ❌ on sufficiency — which is
> the shape the template names as the normal form of a real finding.

## 4. Verdict

**✅ APPROVE**

The mechanism this phase set out to ship is **correct, complete and better evidenced than the TS asked for.**
AC-1 through AC-5 hold under independent reproduction: both "update HL" instructions are gone repo-wide
rather than qualified, 6d's placement outside the research loop rests on a count of this task's own amendment
history rather than on preference, and classification-by-derivation is proven to change a real outcome —
catching a frozen-section edit that carries an owner ruling but no §12 row. AC-6 is reported as partial,
which its own third bullet and DoF-2 make the correct outcome. The `min_iterations` hard gate survived a
rewrite of the step it lives in, byte for byte. 30 of 30 knowledge citations resolve; 0 hallucinations.

The first pass ruled 🔄 REVISE on D1 — three files deleted outside TS §4, sweeping a concurrent session's
staged work into this phase's commit, with the RF certifying the opposite. **The owner waived it** on the
grounds that the two tasks ran in parallel and the commits got tangled. The finding stands on substance and
TD-144 carries it at High severity from the TFW-56 side; on the owner's ruling it no longer counts against
this phase, DoF-4 is not triggered, and the verdict re-rules to ✅ APPROVE.

**What the second pass adds is not a reason to withhold approval.** F1-F5 (§2.1) are the substantive critique
this phase deserves, and each lands somewhere other than on the executor:

| Finding | Where it actually lands |
|---|---|
| F1 — the tripwire, the one half of rule 6 that changes an outcome, is a reference not inline | **Owner decision.** 5 words of headroom against a ~10-word clause, with DoF-2 forbidding the trim that would pay for it. Escalating instead of choosing silently is P5 and F25 behaviour |
| F2 — applying a refinement to a frozen section leaves no record, so the salami pattern HL §12 says it tracks is undetectable | **Contract gap**, exposed by the mechanism working. AC-2 and frozen DoD-13 require the application and require no record |
| F3 — 4 of 13 amendments arrived through channels with no batching discipline | **Contract gap.** `handoff.md` and `review.md` are outside TS §2 |
| F4, F5 — a paraphrase looser than its rule; a "nothing left to remove" claim with a live counterexample | **Text quality**, ~10 and ~50 words |

Judging an executor against obligations its TS does not carry is the mirror image of the drift this task
exists to stop. Principle 16 — *judge against the baseline, never the spec* — cuts both ways: the baseline is
also the ceiling of what may be demanded.

Two ❌ rows survive in §3 and both are documentary: the RF's file count contradicts itself (D2) and an
authorised removal was not disclosed against an explicit ONB condition (D3), which means ~9 of the 11 words
AC-6 attributes to duplication removal came from a correctness fix. Neither touches the shipped mechanism.
They are carried to KNW as corrections rather than held as a gate — the alternative is a re-review cycle for
four lines of text.

### Carried to KNW — four documentary corrections

**Executor** — RF and EV only:

1. **RF §3 — reconcile the file count with RF §1.** The DoF line says *"three"*; the table lists four
   (`plan.md`, `research/base.md`, `templates/RES.md`, `templates/HL.md`). State `templates/HL.md` as an
   owner-authorised fourth file, exactly as Decision 13 already argues.
2. **Disclose the `plan.md`:97 removal** per the coordinator's ONB Inconsistency-1 ruling — the dead
   `conventions.md` §4 "Agent selection guidance" reference (D50), removed as a correctness fix, ~9 words.
   Add it to EV Exhibit B's ledger as a **non-duplication** removal and reconcile the −11.
3. **Soften EV Exhibit B's *"no further measured duplication exists"*** to the claim the evidence supports,
   naming F5's counterexample (Step 2's Knowledge Gate modes, also in `glossary.md`:213).
4. **Fix the RF §2 numbering gap** — Decision 12 is missing; the list runs 1–11, 13, 14.

**Coordinator** — three acts the executor cannot perform:

5. **Add `templates/HL.md` to TS §4** with the limit *"§3.1 only"*, exactly as ONB Q2's authorisation was
   recorded for `templates/RES.md`:133. RF Decision 13 requests this and correctly declines to do it itself.
6. **File the missing §12 row for DoD-18's priority-1 relabel** (RF obs. 4, independently confirmed at
   HL:724): the owner's Q5 ruling exists, rule 9's log entry does not.
7. **Put F1 to the owner as a decision** — insert the tripwire clause and accept ~1,205 words, or leave the
   reference and accept that the step's one discriminating case is decided by text it does not contain.
   Present both costs; do not choose it inside a phase.

**Explicitly not required to change:** any shipped mechanism, AC-6's word count, `6d`'s missing
`🚫 WITHDRAWN` path (Decision 7's arithmetic is sound — TD-154), or the §3.1 rewrite, whose
refinement-not-amendment classification this reviewer checked against frozen DoD-11 clause by clause and
confirms.

## 5. Tech Debt Collected

> Observations triaged from RF §6. Obs. 6 is already TD-140's second half and obs. 7 is already TD-107 —
> recorded there, not duplicated. D1's framework-level debt is already TD-144 (High).

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| TD-153 | RF TFW-53/B obs. #1 | Med | `.tfw/templates/RES.md` (§ HL Update Recommendations) | Two classes defined by target **HL** section cannot hold research output aimed at the **TS**. Three of iter2's four "coordinator notes" name no HL section because none targets the HL — the researcher invented an undefined third table for them (F11's emergence pattern). The shipped Step 6c correctly fails to route them; the gap is one level up, in the template's class set | → Phase D terminology pass |
| TD-154 | RF TFW-53/B obs. #2 | Med | `.tfw/workflows/plan.md` 6d | 6d has no `🚫 WITHDRAWN` path, so it cannot describe §12 row A11, and its clause *"only an owner verdict moves one"* conflicts with a proposer withdrawal. ~14 words against 5 of AC-6 headroom; deliberately deferred with the arithmetic stated (RF Decision 7) rather than absorbed silently | → Phase D, or the first phase with artifact-budget headroom (TFW-57) |
| TD-155 | RF TFW-53/B obs. #3 | Med | `.tfw/conventions.md` §3 rules 13-15 | The re-freeze trigger reads *"after an approved amendment"*, but `ffe6c6a` re-froze after a **refinement** to §3.1 — correct practice, unauthorised text. The trigger is arguably *"the frozen text changed"*. Until reworded, correct behaviour is undocumented and incorrect behaviour (skipping a re-freeze after a refinement) is permitted | → next phase that may edit `conventions.md` §3 (not B — out of scope) |
| TD-156 | RF TFW-53/B obs. #4 | Med | `HL-TFW-53…md` §5 DoD-18, §12 | DoD-18's PV priority-1 relabel entered a **frozen** section on owner ruling Q5 (HL:724, 2026-08-10) with no §12 row, which rule 9 requires for an owner-initiated change. The verdict exists; the log entry does not, so §12 returns an incomplete answer to the one question it exists to answer. Found by the shipped step's own replay | → coordinator files the row (REVIEW §4 item 6) |
| TD-157 | RF TFW-53/B obs. #5 | Med | `.claude/commands/tfw-plan.md`, `.agent/workflows/tfw-plan.md` | Both adapter copies still carry the old Step 6c verbatim, including *"Update HL with research findings"*, and both still measure 1,206 words. Until Phase D syncs them, **2 of 3 adapter surfaces instruct the coordinator to do what the core now forbids** — the D54 adapter-parity promise is live-broken, not merely stale | → Phase D (TS §9 already assigns it); tracked here because the window is open now |
| TD-158 | REVIEW TFW-53/B verify.md V5 | Low | `.tfw/templates/HL.md` §3.1 bullet 2 | The rendering list now includes *"a narrative timeline"* in the same bullet that ends *"Prose alone is not a rendering."* The tension is pre-existing — the old block listed `Narrative — timeline of a user's day` as a format option and then said prose was insufficient — but merging the two lists puts both halves in one sentence, where an author reads the permission and skips the constraint | → Phase D terminology pass, alongside TD-140's §12 half |
| TD-159 | REVIEW TFW-53/B §2.1 F1 | **High** | `.tfw/workflows/plan.md` Step 6c item 3 | Rule 6's tripwire — *"if the change cannot be accepted under §5 and §6 as they stand"* — is referenced, not inline, while rule 6's non-discriminating first half **is** inline. The replay measures the split: 21 of 22 rows route identically either way, and the 1 that differs is a live unlogged frozen-section edit. `conventions.md` §11 requires enforcement-critical text inline. Costs ~10 words against 5 of AC-6 headroom, so it cannot be fixed without breaking F2's threshold — the reason it was escalated rather than chosen | ⬜ **Open — owner decision** (REVIEW §4 item 7) |
| TD-160 | REVIEW TFW-53/B §2.1 F2 | **High** | `.tfw/workflows/plan.md` Step 6c item 3; frozen HL DoD-13 | Applying a refinement to a free unit inside a frozen section produces **no record at all** — the branch reads *"→ apply it"* and requires nothing else. HL §12's own note names the salami pattern as tracked and instructs the reviewer to *check* the classification; there is nothing to check, because N successive refinements to §4 leave zero trace. Contract-level gap: AC-2 and frozen DoD-13 require the application and require no log | ⬜ Backlog — needs a §12 amendment or a later-phase deliverable, not an executor fix |
| TD-161 | REVIEW TFW-53/B §2.1 F3 | Med | `.tfw/workflows/handoff.md`, `.tfw/workflows/review.md` | The batching rule that protects the owner's interruption budget governs **research output only**. 6d correctly handles a verdict arriving from anywhere, but nothing governs *filing* outside the research loop: of 13 §12 rows, 8 came from research (disciplined) and **4 from an executor ONB or from the owner during execution (undisciplined)**. HL §11 S29 records proposals-per-iteration as the design's own success metric | ⬜ Backlog — → the phase authorised to edit `handoff.md` / `review.md` |
| TD-162 | REVIEW TFW-53/B §2.1 F4 | Low | `.tfw/workflows/plan.md` Step 6c item 3 | The step's paraphrase *"a free unit inside a frozen one"* is broader than rule 6, whose only named free unit is a deliverable list inside an already-approved phase. It saves no reading (free units are not enumerated in the step) and widens the boundary on a first read — toward treating frozen text as free, the failure mode the task exists to stop | ⬜ Backlog — fold into TD-159's rewrite if that is approved |
| TD-163 | REVIEW TFW-53/B §2.1 F5 | Low | `.tfw/workflows/plan.md` Step 2, `.tfw/glossary.md` L213 | `plan.md` Step 2 states the three Knowledge Gate modes (`hard` stop + justification / `soft` reminder / `off` skip) that `glossary.md`:213 also states — ~50 words, a live counterexample to EV Exhibit B's *"no further measured duplication exists"*. Found in the same check: `glossary.md`:213 places the gate in *"Phase 0 of `plan.md`"*, and `plan.md` has Steps 0-7 with no Phase 0 — the gate is Step 2 | ⬜ Backlog — → Phase D (it owns `glossary.md`) |

## 6. Traces Updated

- [x] README Task Board — status set to `📚 KNW (B) · 📚 KNW (A)`, Phase B REVIEW linked
- [x] HL status — unchanged; the HL header remains 🔒 FROZEN at baseline `e8ee76e`. Phase C is unblocked
- [x] project_config.yaml — `initial_seq` unchanged (no new task created)
- [x] Other project files — TECH_DEBT.md appended (TD-153 – TD-163); no stale info found elsewhere
- [ ] tfw-docs: **Pending** — run `/tfw-docs`. Candidates: D19's narrowing now has an enforcement site;
      D20's implicit-approval root cause is closed in the workflow; TD-159 – TD-163 to register
- [ ] tfw-knowledge: **Pending** — RF §7 FC1-FC3, RF §8 S1-S2 and this REVIEW's §7 FC1-FC2 are live
      candidates. Both markers must be set before the board moves to ✅ DONE

## 7. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | The framework gained a **per-user preferences layer mid-phase** — `.user_preferences.md`, gitignored, wired into `AGENTS.md` and `CLAUDE.md` by commit `d7b02a4` while Phase B was executing. Its own constraint F1 forbids copying its content into any shared framework file, and the `templates/HL.md` §3.1 rewrite is the first test of that boundary: the personal origin stays in the private file, and only the behavioural rule (*"You imagine; the reader must not have to"*) ships to the template. The pattern to record: a personal requirement enters shared text as a **behavioural rule with a falsifiable test**, never as a statement about the reader | User, `.user_preferences.md` 2026-08-13; commit `d7b02a4`; verified against `templates/HL.md` §3.1 | High |
| 2 | risk | **A verbal staging directive did not survive the run it was given for.** The owner instructed both sessions about concurrent execution in one working tree; the TFW-53/B executor recorded it as FC1, reasoned about it in S1, and still swept three of TFW-56's deletions into its own commit. Two independent reviews (this one and TFW-56's) reached the same finding from opposite sides. The measurement, not the anecdote: an instruction that exists only in a session directive has a demonstrated survival rate of 0 out of 1 against a broad `git add`, which is F4's structural-over-exhortation argument reproduced on the git index | User, run directive 2026-08-13; `git show --stat fbdf443`; TFW-56 RF §6 obs. 1; TD-144 | High |

> **Source format**: Use reference patterns (e.g. `RF TFW-18`, `D24`). See compilable_contract.md §2.

---

*REVIEW — TFW-53 / Phase B: Enforcement in Workflows | 2026-08-13*
