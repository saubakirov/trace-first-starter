# REVIEW — TFW-53 / Phase E: Rejected-Task Trace Restoration

> **Date**: 2026-08-18
> **Author**: Reviewer (Claude Code)
> **Verdict**: ✅ **APPROVE** — second pass, 2026-08-18. First pass was 🔄 REVISE on one finding; all five items corrected in `5d0f86c`, re-verified, and one non-material residue disclosed
> **RF**: [RF Phase E](RF__phase-e__rejected_trace_restoration.md)
> **TS**: [TS Phase E](TS__phase-e__rejected_trace_restoration.md) — amended 2026-08-18 after ONB
> **Contract baseline**: `11cd340`, recovered by `conventions.md` §3 rule 15 · covers frozen DoD 34–36
> **Stage files**: [`review/map.md`](review/map.md) · [`review/verify.md`](review/verify.md) · [`review/judge.md`](review/judge.md)
> **Passes**: 1st 🔄 REVISE · 2nd ✅ APPROVE
> **Verification depth**: 9 of 9 claimed files (100%) — escalated from the required ⌈9 × 0.42⌉ = 4 on the discrepancy in §2 D1
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

TFW's status set could say a task succeeded, was in flight, or was waiting — and nothing could say it had
failed. Phase E ships the missing state (`❌ REJECTED`, terminal, in five carriers), the rule that protects
it (`conventions.md` §13 — reverting a *result* never reverts its *trace*), and the warning that names how
the loss happened (§14 — a whole-tree restore silently reverts the board past a failure status). Then it
applies the machinery once: two post-mortem files and two restored board rows for TFW-48 and TFW-49.

Three decisions shape the result. `❌ REJECTED` is drawn as a **side node reachable from any status**, not
as a branch under the review verdict `❌ REJECT` — TFW-48 was rejected out of `🟡 TS_DRAFT` having never
reached a review, which settles it by counterexample from this phase's own corpus. The `REJECT*` collision
is **three-way** (task status · review verdict · HL §12 amendment verdict) and is closed at both ends
*without* editing `templates/HL.md`, which belongs to Phase A. And TFW-49's owner verdict is quoted
**whole** rather than elided, because the middle of the block is where the owner listed what was actually
rejected.

The whole change is **additive**: `git diff` on `conventions.md` shows 6 insertions and 0 deletions, which
is what makes "nothing else in the status vocabulary moved" provable rather than asserted.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | `conventions.md` — §5 diagram node, §5 table row, §13 sentence, §14 bullet | ✅ | `+6 / −0`. §14 bullet count reproduced at **39** (was 38). Zero deletions proves the REVISE/REJECT branch, the loose `BLOCKED` edge and every other phase's §14 entry are untouched |
| 2 | `project_config.yaml` + `templates/project_config.yaml` | ✅ | PyYAML on both: **11 statuses**, order ends `['BLOCKED','REJECTED']`, emoji `0x274c`, no spurious `role` key. `tfw.version` unchanged |
| 3 | `glossary.md` — count sentence + Amendment Log clause | ✅ | Two `−1/+1` hunks. `:130` carries the owner-approved wording; `:57` gains exactly one clause and nothing else in the article. The one-line pipeline diagram at `:127` deliberately unchanged |
| 4 | `CHANGELOG.md` — `[Unreleased]` block | ✅ | One hunk, `+4 / −1`. `[1.2.0]` appears only as unchanged context; `.tfw/VERSION` = 1.2.0, no diff |
| 5 | `README.md` — two rows, legend, own row | ✅ content | Rows at **298 / 299**, between TFW-47 (297) and TFW-50 (300). Legend at **310**. Since committed by `8d9432b` — **AC-3's ⚠️ resolves** |
| 6 | `POSTMORTEM__TFW-48.md` | ✅ | 544 words · five headings in order · status stated as **assigned**, with `🟡 TS (D)` at `5b17786`:294 cited as the last live status · `grep -c "TFW-55"` → 0 |
| 7 | `POSTMORTEM__TFW-49.md` | ✅ | 727 words · identical heading sequence · the seven-line verdict compared line-by-line against `ad0696e` → **identical**, unelided · `9e19a4f` described as a research-approval commit with the "not a contract baseline" reason stated |
| 8 | Both owner verdicts, against their commits | ✅ | The `bc6779e` paragraph is word-for-word in both files (`git log -1 --format=%B`). The `ad0696e` block matches HL lines 10–17 including inline code and the en-dash in *"Phases A–C"*. **Compared, not eyeballed** |
| 9 | Six git references re-executed | ✅ | `721ca15` → **75** files · `bc6779e` → **149 files changed, 798 insertions(+), 27103 deletions(-)** · `5b17786`:294–295 → both status cells verbatim · `ad0696e` · `9e19a4f` |
| 10 | AC-5 file-count gate | ✅ | `find tasks/TFW-48__* tasks/TFW-49__* -type f \| wc -l` → **2**. Nothing from `721ca15` re-entered the tree |
| 11 | Link resolution | ✅ | **7 of 7** — 3 in the post-mortems, 4 in the board rows |
| 12 | Regression gate | ✅ | `python -m pytest docs/scripts/ -q` → **68 passed** in 48.16s, matching the RF and the Phase D baseline |
| 13 | **`REJECTED` site census** | ❌ **D1a** | Re-executed → **12 hits**, not the 10 the RF and EV report. Missing: `README.md`:298 and :299 — the phase's own board rows. Correct split: **task status 9 · amendment verdict 3 · review verdict 0** |
| 14 | **README legend line number in the RF ledger** | ❌ **D1b** | *"line 307 as measured at the time of writing"* is a **pre-edit** number. `git show 8d9432b^:README.md` → legend at 307 with **zero** `REJECTED` hits. With the phase's own two rows inserted above it, the legend was at **309** then and is **310** now — while 298/299 in the same ledger are post-edit numbers |
| 15 | Board-row commit attribution | ⚠️ **D2**, not the executor's | `README.md` was correctly left unstaged (TS §9, ONB Q2 (b)) and disclosed. The coordinator landed it in `8d9432b`, whose subject is `[claude-code/TFW-58/proposal/coordinator] propose the revise protocol` and whose body never mentions TFW-53. → tech debt, not a finding against this RF |

> Raw verification log with all 15 commands, 9 file records, 7 claim/source checks and the 27-row evidence
> audit: [`review/verify.md`](review/verify.md). **Nothing was unverifiable** — every claim in this phase is
> about file content, git history or a status vocabulary, and all three are directly observable.

**The single root cause behind D1a and D1b:** the census and the legend line number were taken from a
`README.md` that already carried the edited legend but **not yet** the two board rows. Nine `.tfw/` hits
plus that one README hit is exactly the reported 10. A mid-execution snapshot was recorded as the final
state.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ✅ | Frozen DoD-34/35/36 all satisfied; AC-1 → §2 rows 1–3 and 5, AC-2 → row 1, AC-3 → row 5, AC-4 → rows 6–9, AC-5 → row 10, AC-6 → row 4. **Qualification:** AC-1's *gate* also required the EV census to classify every hit — the product passes, the census does not (row 8) |
| 2 | Purpose Check + design soundness | ✅ | **(a)** Aligned — full citation-and-harm field below. **(b)** Sound: the side node keeps a review verdict from reading as a route to a terminal state; the three-way collision is closed without touching Phase A's `templates/HL.md`; and the change is additive-only, which is what makes the "nothing else moved" claim provable |
| 3 | Tech debt documented | ✅ | RF §6 carries three observations, each with file, line range, type and a stated reason for leaving it. None is filler; two are promoted below |
| 4 | Style & standards | ✅ | **2 product files created, 6 modified** against 15 / 30 — the smallest phase in the task, as the TS predicted. Each carrier's own form was matched instead of one form imported into all five. Commit grammar follows TFW-50. `README.md` left unstaged as directed, foreign line named |
| 5 | Observations collected | ✅ | Filter applied: obs. 2 and 3 promoted to new debt; obs. 1 folded into the existing TD-175, which measures the same question from the other end |
| 6 | RF completeness (§7-9) | ✅ | §7 and §8 both declare **none**, apply the Human-Only Test explicitly, and name TD-174 as the contradiction they resolve against — the exact defect Phase D was sent back for, avoided by stating which reading is used. §9's three diagrams earn their place |
| 7 | Evidence completeness — does it exist? | ✅ | 27 rows, every AC Evidence field covered, valid statuses, environment header complete, one DEFERRED with its blocker named rather than omitted |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | **26 of 27 rows establish their claims. E1 does not.** It reports 10 hits and classifies them; the command returns 12, and the two it misses are the board rows AC-3 exists to create. The *"Reconciling 7 against 10"* paragraph is wrong as written (§2 D1a), and RF §1's legend line number has the same root cause (§2 D1b) |
| 9 | Backward compatibility | ✅ | `docs/scripts/gen_docs.py`:324–341 parses board rows by regex with no hardcoded status set — 68 tests confirm. Updating `templates/project_config.yaml` alongside the live config means a newly-initialised project is *born* with the status rather than acquiring it by `/tfw-update`. No section number, anchor or heading renamed; the §14 bullet is appended, so no entry's index moves |
| 10 | Safety | ✅ | Markdown and YAML text only; no credentials, no destructive or irreversible operation, no runtime. The one lasting footprint — recreating the two task folders — is bounded to one file each (verified at 2) and disclosed in RF §8 with its own risk statement. No historical commit rewritten |

### Purpose Check — the citation and the harm

**Reference set:** master HL-TFW-53 at contract baseline **`11cd340`**, plus the Project North Star in
`.tfw/README.md` § The Thesis. Neither the TS nor a Phase HL was used.

Serves baseline principle **P17** — *"A failed trace is the most valuable trace — it records what cannot be
re-derived. Reverting a result must never revert its evidence"* — and the north-star thesis that the
irreplaceable artifact is *"the trace — the record of intent, decisions, constraints, and **rejected
alternatives** that led to the result."* Without this phase the framework has no state meaning *failed*, so
the next failure is closed by lying with `✅ DONE`, misusing `❌ BLOCKED`, or deleting the folder — and this
project's two most expensive failures, 27,103 deletions and six days, stay invisible on the board that is
supposed to be its memory. **The harm is permanent loss of irreplaceable knowledge by method rather than by
carelessness** — material, not a wording preference.

Excess and adjacency: **no** — the deliverables are exactly baseline §4 Phase E items 1–5; no AT-mode work
(DoF-4), no contract or review mechanism. Deferral confession: **no** — `templates/HL.md`, `conventions.md`
§3, the loose `BLOCKED` edge, the `templates/RF.md` §7 contradiction and the `VERSION` bump were each named
and each actually left where they belong. Neither the purpose-failure nor the contract-defect outcome
applies: the reference set is internally consistent and the work is what the owner approved.

### Frozen DoF — all clear

Baseline **DoF-4** (no AT mode), **DoF-16** (no artifact files re-added — `find` → 2), **DoF-17** (the
`BLOCKED` boundary is stated in all five carriers): none tripped. All eleven phase-level DoF items in TS §7
checked individually in [`review/judge.md`](review/judge.md); none tripped.

## 4. Verdict

**🔄 REVISE**

**The product is complete and correct; the evidence record is not.** Every carrier of the new status was
opened and verified. Both owner verdicts were compared against their commits rather than read. All six git
references re-execute to the values claimed. The file-count gate that DoF-16 rests on returns 2. The test
suite returns 68. Frozen DoD-34, DoD-35 and DoD-36 are all satisfied, the Purpose Check is aligned against
the `11cd340` baseline, and no Definition-of-Failure item at either level is tripped.

One claim does not reproduce, and it is the one the TS singled out as the reviewer's reconciliation. AC-1's
gate reads: *"The EV file classifies every hit by which of the three meanings it carries, so the arithmetic
is on the page instead of left to the reviewer."* The arithmetic on the page is short by two, and the two it
omits are `README.md`:298 and :299 — the board rows this phase exists to restore. A reader trusting the
classification would conclude the rows are not carriers of the new status. The same mid-execution snapshot
put a pre-edit line number in the RF's own ledger next to two post-edit ones.

This is not a wording objection and it is not new scope. It is a count that does not reproduce, in the
permanent evidence file, in the phase whose entire subject is honest records — and it is the same defect
class Phase D was returned for on its first pass (E17, a hunk count that did not reproduce). Approving it
would set the precedent that a designated reconciliation may be wrong as long as the product is right.

The fix is bounded, mechanical, and entirely inside the approved TS: correct two numbers, add two rows to a
table, re-run one command. **No HL change, no TS change, no product change.** Routes back to the
**executor**.

### Items to fix

| # | Where | What | Verification |
|---|-------|------|--------------|
| 1 | `EV__phase-e__rejected_trace_restoration.md` — E1 and the § *"The ten `REJECTED` hits, classified"* | Change the count from **10** to **12**. Add the two missing rows: `README.md`:298 (task status — TFW-48 board row) and `README.md`:299 (task status — TFW-49 board row), both `new (AC-3)`. Correct `README.md`'s legend line number from 307 to its actual value. Retitle the section for the real count | `grep -rn "REJECTED" .tfw/ README.md \| wc -l` → 12, and the table has 12 rows |
| 2 | `EV__…md` — the *"Reconciling 7 against 10"* paragraph | Rewrite as 7 against 12. The three uncounted hits it already names stay; add the two board rows as the fourth reason — the TS gate counted five carriers as five hits, and `README.md` carries the status three times, not once. Final split: **task status 9 · amendment verdict 3 · review verdict 0** | The stated split sums to 12 and matches the table |
| 3 | `RF__…md` §4 verification table, row *"`REJECTED` site census"* | Same correction: 12 hits — 9 task status, 3 amendment verdict, 0 new review verdict | Row matches the EV table |
| 4 | `RF__…md` §1 README line ledger | Correct the legend line number and state it as measured **after** the phase's own row insertions, so all three numbers in the ledger are from the same tree state | `grep -n "^> Statuses:" README.md` matches the ledger |
| 5 | `RF__…md` header and §3 AC-3 | The ⚠️ is discharged: `README.md` landed in commit `8d9432b`. Replace the "held by another session" warning with the commit that carries the rows, and check the AC-3 box | `git log --oneline -- README.md \| head -1` |

> Nothing else in the RF or the EV needs to change. Do not touch `.tfw/`, the post-mortems, `README.md` or
> any product file — all of them verified clean at 100% coverage.

## 4.1 Second pass — 2026-08-18

**Corrective commit:** `5d0f86c` `[claude-code/TFW-53/phase-e/executor] correct the census to 12, fix the
legend line, discharge the deferral`. Coordinator alongside: `27a7bee` (TS — no delta, with the reason
stated) and `86f159f` (HL §11 S40).

### The five items, re-verified against the files

| # | Required | Delivered | ✓ |
|---|----------|-----------|---|
| 1 | EV E1 + hit table: 10 → 12, add `README.md`:298/:299, fix the legend line, retitle | Section is now *"The twelve `REJECTED` hits, classified"*, **12 rows**, hits 7–8 are the board rows marked `new (AC-3)` and *"missing from the first count"*, legend row reads `:310` | ✅ |
| 2 | Reconciliation rewritten as 7 → 12, split 9 / 3 / 0 | *"Reconciling 7 against 12"*, **four** uncounted reasons — the new one being *"`README.md` carries the status three times, not once"*. Split re-counted by me from the table itself: **9 / 3 / 0** | ✅ |
| 3 | RF §4 census row | **12 hits — 9 / 3 / 0**, plus a per-file breakdown that sums to 12, citing finding D1a | ✅ |
| 4 | RF §1 ledger from one tree state | *"All line numbers below are measured in the committed tree at `8d9432b`"*; legend **310**; TFW-58's row added and marked **not mine**; a paragraph explaining that **three** lines were inserted above the legend, only two of them this phase's | ✅ — answers more than was asked |
| 5 | RF header + AC-3: discharge the ⚠️ | *"✅ `README.md` has landed"* naming `8d9432b`; AC-3's last box checked with the confirming command; the TD-178 attribution gap noted on the same line | ✅ |
| +6 | *Not a review item* — E27 and the EV verdict | E27 → **VERIFIED** carrying **both** states rather than overwriting the first; verdict **27/27**; RF §5 matches. Reason stated: leaving it DEFERRED while the RF reports the rows committed would contradict item 5 inside the same phase | ✅ — correct, and self-justified |

### Independent re-execution

| Command | Result |
|---|---|
| `grep -rn "REJECTED" .tfw/ README.md \| wc -l` | **12** — matches the corrected table row for row *and* line for line |
| `grep -n "^> Statuses:" README.md` | **310** |
| `git diff --stat 1e24e35 HEAD -- .tfw/ tasks/TFW-48__* tasks/TFW-49__*` | **empty** — the *"no product file touched"* claim reproduces |
| `git status --short` on all product paths | **empty** |
| `git show 5d0f86c --stat` | `README.md` 2 lines · RF · EV. No `.tfw/` file, no post-mortem |
| `git show 5d0f86c -- README.md` | Only the `[E🔄]` REVIEW link and the status cell returned `🔄 REVISE (E)` → `🟢 RF (E)` for re-review |

### One residue, disclosed and ruled non-material — D3

`RF__…md`:50, the *New Files* table, still reads *"the classification of all **ten** `REJECTED` hits"*. It
was not among the five items and was not swept.

| Test | Answer |
|------|--------|
| Carries a verification claim? | **No** — a file-description cell. RF §4, RF §1, EV E1, the EV table, the reconciliation and both verdict lines all read 12 and all re-execute |
| Leaves a reader misinformed? | **No** — the sentence points at a file whose own heading is *"The twelve `REJECTED` hits, classified"* |
| Material impact on the value? | **No.** Baseline **DoF-13** and **P14**: a block rests on material impact, never on phrasing. Phase D's second pass set the precedent, approving with three stale arithmetic labels disclosed and ruled non-material |

**To be swept in the closing commit.** The reviewer does not edit the RF (role lock).

### Second-pass judge deltas

| Row | 1st | 2nd | Why it moved |
|---|---|---|---|
| 8 — evidence sufficiency | ❌ | ✅ | The single failing row is closed: 12 re-executed and matched line for line, the split re-counted from the table rather than read off the summary, the legend confirmed at 310, E27's discharge checked against `git log -1 -- README.md` |
| 1 — DoD | ✅ | ✅ | AC-1's gate is now *fully* satisfied — the census classifies every hit, which was the one part outstanding |
| 2 — Purpose Check | ✅ | ✅ | Re-run against `11cd340` and the north star. The corrective pass serves the same clause it corrects: **P17** is about honest records, and this made the phase's own record honest |
| All others | ✅ | ✅ | No product file moved, so nothing under them changed |

## 4.2 Verdict — ✅ APPROVE

The phase delivers what frozen **DoD-34, DoD-35 and DoD-36** ask for, and the record now proves it. Every
carrier of `❌ REJECTED` was opened; both owner verdicts were compared against their commits rather than
read; all six git references re-execute; the DoF-16 file-count gate returns 2; the suite returns 68; and the
one census that did not reproduce now does, row for row and line for line. The Purpose Check is aligned
against baseline `11cd340` and the north star, and no Definition-of-Failure item at either level is tripped.

The corrective pass touched **no product file** — verified independently, not accepted on the RF's word —
and it recorded its corrections as *was → is* rather than replacing the numbers silently. In the phase whose
subject is honest records, that is the right discipline, and it is worth naming as the thing done well.

One numeral survives in a descriptive cell (D3). It is disclosed above, ruled non-material under DoF-13 and
P14, and left for the closing commit. It does not ground a second block.

## 5. Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| TD-176 | RF TFW-53/E §6 obs. 2 | **Med** | `.tfw/conventions.md` §3 | **`POSTMORTEM` is now a shipped file class that §3's artifact-type list does not name.** §3 enumerates HL, RES, TS, RF, ONB and REVIEW and nothing else; §4's filename rule is satisfied (the task ID is present) and frozen HL §4 Phase E deliverable 4 authorises the file, so nothing was smuggled in. What is missing is the type entry. Without it the next rejected task invents a second name for the same thing, and the status this phase shipped acquires an unnamed companion artifact. **Not fixable here** — §3 is Phase A's section under HL §7.1 | ⬜ Backlog → the next task authorised to edit `conventions.md` §3 |
| TD-177 | RF TFW-53/E §6 obs. 3 | **Med** | `README.md`:249 vs 297–299 | **The Task Board header declares 8 columns while its rows carry 7, 8 or 9.** Header: `ID \| Task \| Status \| HL \| TS \| ONB \| RF \| REV`. Every row from TFW-42 onward carries a ninth cell for RES; TFW-50's carries 8; TFW-51's carries 7. Pre-existing and untouched by this phase, but the two rows it added match their neighbours at 9 cells rather than the header — so a renderer that trusts the header truncates the newest rows, including the two restored failure traces. `docs/scripts/gen_docs.py` parses by regex and is unaffected; any stricter consumer is not | ⬜ Backlog → TFW-57 (it already owns README artifact structure) |
| TD-178 | REVIEW TFW-53/E §2 D2 | **Low** | `README.md` · git history | **Phase E's board rows landed under a commit subject naming a different task.** The executor correctly left `README.md` unstaged (TS §9, ONB Q2 (b)) and disclosed the fact. The coordinator then committed the rows inside `8d9432b`, `[claude-code/TFW-58/proposal/coordinator] propose the revise protocol`, whose body never mentions TFW-53. The rows are in history, so AC-3 is satisfied — but `git log -- README.md` shows no TFW-53/E commit for the deliverable of the phase whose subject is honest traces. **The gap is procedural:** TS §9's "the coordinator lands it" does not say *in its own commit* | ⬜ Backlog → the task that specifies cross-session file handoff (candidate: TFW-54, which owns delegation topology) |

**Not promoted.** RF §6 obs. 1 (the §5 diagram's loose `❌ BLOCKED` edge) — **TD-175** already records the
same question from the opposite end (`BLOCKED` at 0 uses across 46 board rows), and the owner asked at the
ONB gate for it to be recorded rather than acted on. Filing a second row would split one decision across
two entries.

## 6. Traces Updated

- [x] README Task Board — TFW-53 row set to `📚 KNW (A, B, C, D, E)`; the REV column carries `[E✅]`
- [x] HL status — Phase E complete; the task now has no phase in flight
- [x] `project_config.yaml` — no `initial_seq` change needed
- [x] Other project files — `TECH_DEBT.md` appended with TD-176, TD-177, TD-178
- **tfw-docs:** ✅ **Applied 2026-08-18** — one pass across Phases A–E: `KNOWLEDGE.md` §1 (Adapters row + **D63**, **D64**, **D65**), §2 (three artifact rows), §3 (six legacy entries + the TFW-48/49 row re-pointed at the post-mortems); `TECH_DEBT.md` TD-176/177/178 added, TD-156 closed, TD-169(a) closed
- **tfw-knowledge:** ✅ **Applied 2026-08-18** — one pass across Phases A–E. **25 facts** written (105 → 130): philosophy +8, process +5, stakeholder +4, constraint +3, environment +2, convention +2, and a new `knowledge/risk.md` +1. Phase E itself contributed none directly — correctly, since its RF §7 and §8 both declared none under the Human-Only Test; its owner ruling had already been captured as HL §11 S39 and is now `stakeholder` F9

> Both have been outstanding since Phase A. TFW-53 closes them once, across all five phases, and only then
> does the board move to `✅ DONE`. The release belongs to the coordinator after that.

## 7. Fact Candidates
> fact-candidates: processed 2026-08-18 (`/tfw-knowledge`, TFW-53 A–E)


**No fact candidates.**

Applying the Human-Only Test, and — like the RF — declaring which side of **TD-174** this uses, since
`templates/REVIEW.md` §7 carries the same self-contradiction the RF names in `templates/RF.md` §7: its Scope
line admits *"reviewer-observed project patterns"* while the Human-Only Test four lines below bars anything
an agent can discover by reading files or running commands. This review applies the **Human-Only Test**, the
stricter reading.

Everything this review learned — the census arithmetic, the commit attribution gap, the board's column
arity — was found by running commands and reading files. It is agent-derived and belongs in §5, where it is
filed. The human input in this session was the review instruction and the file path. The owner's one
substantive contribution to this phase, the vocabulary ruling at the ONB gate, was captured before execution
in HL §11 S39 and TD-175 and is not new here.

---

*REVIEW — TFW-53 / Phase E: Rejected-Task Trace Restoration | 2026-08-18*
