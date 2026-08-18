# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42 (`project_config.yaml` → `tfw.review.min_verify_ratio`)
> RF files claimed: **9** (6 modified, 3 created — the EV file included)
> Files to verify: ⌈9 × 0.42⌉ = **4** · **escalated to 9 of 9 (100%)** on the discrepancy in D1

## Verification Log

### V1: `.tfw/conventions.md`
- **RF claim:** §5 gains one side node in the ASCII diagram and one table row after `❌ BLOCKED`; §13 gains the trace rule as a third sentence; §14 gains one appended bullet (38 → 39). `git diff --numstat` → 6 insertions, 0 deletions.
- **Actual:** `git show 1e24e35 -- .tfw/conventions.md` — three hunks, **six `+` lines, zero `-` lines**. Diagram side node at :327, table row at :342, §13 third sentence at :506, §14 bullet at :548. `awk '/^## 14\) Anti-patterns/,/^### 14.1/' | grep -c "^- "` → **39**. The REVISE/REJECT branch, the loose `❌ BLOCKED` edge, and every other phase's §14 entry are untouched — provable from the zero deleted lines.
- **Match:** ✅

### V2: `.tfw/project_config.yaml`
- **RF claim:** one `tfw.statuses` entry after `BLOCKED`; `tfw.version` untouched.
- **Actual:** three added lines at :108–110, `id: REJECTED` / `emoji: "❌"` / `description: "Closed unsuccessfully, terminal, trace retained"`, immediately after `BLOCKED`. PyYAML: **11 statuses**, last two `['BLOCKED','REJECTED']`, emoji `0x274c`, `role` key absent. `version: "1.2.0"` at :7 shows no diff.
- **Match:** ✅

### V3: `.tfw/templates/project_config.yaml`
- **RF claim:** the same entry, so a new project is born with the status.
- **Actual:** identical three lines at :112–114. PyYAML: **11 statuses**, same order, same emoji, no `role` key. Byte-equal payload to V2.
- **Match:** ✅

### V4: `.tfw/glossary.md`
- **RF claim:** `## Status Flow` count sentence replaced with the ONB R6 wording plus the three-way boundary; `### Amendment Log` gains one appended clause and nothing else in that article.
- **Actual:** two hunks, each `-1 / +1`. :130 replaces *"9 statuses: … (+ BLOCKED). RES and KNW are optional."* with the approved wording, then adds the three-token sentence. :57 appends exactly one clause to the existing article — *"Its ❌ REJECTED verdict refuses a proposal, not a task — the terminal task status of the same name is conventions.md §5."* — with the rest of the sentence chain intact and the trailing `→ conventions.md §3 rule 4` pointer preserved. The one-line pipeline diagram at :127 is unchanged, as RF §2 decision 6 states.
- **Match:** ✅

### V5: `.tfw/CHANGELOG.md`
- **RF claim:** `[Unreleased]` — *"Nothing pending."* replaced by one `### Added` block. One hunk, 4 insertions, 1 deletion. `[1.2.0]` untouched.
- **Actual:** exactly one hunk at `@@ -5,7 +5,10 @@`; `-Nothing pending.` and four `+` lines (`### Added` plus three bullets naming the status, the §13 rule and the §14 anti-pattern, each tagged `(TFW-53/E)`). `git diff … | grep "1\.2\.0"` returns only the unchanged context line `## [1.2.0] — 2026-08-14`. `.tfw/VERSION` = `1.2.0`, no diff.
- **Match:** ✅

### V6: `README.md`
- **RF claim:** two board rows at 298 and 299, legend extended, TFW-53's own row advanced; **unstaged and held by another session** — the coordinator lands it.
- **Actual:** the file is now **clean in the working tree**; the rows landed in commit `8d9432b`. Row 298 = TFW-48 `❌ REJECTED` with the status-assigned note and a post-mortem link; row 299 = TFW-49 `❌ REJECTED — complete product-fit failure; superseded by TFW-50`. Both sit between TFW-47 (297) and TFW-50 (300). The legend is at **310**, carrying `❌ BLOCKED (waiting) | ❌ REJECTED (closed unsuccessfully, trace kept)`. The TFW-53 row reads `📚 KNW (A, B, C, D) · 🟢 RF (E)` with D and E links added. The TFW-55 row moved to `🟡 TS_DRAFT (A)` — the foreign line the RF ledger names as not its own.
- **Match:** ⚠️ partial — content correct, **line number in the RF's own ledger wrong** (see D1b). The unstaged caveat is now historical: AC-3's ⚠️ resolves.

### V7: `tasks/TFW-48__value_first_methodology_rebaseline/POSTMORTEM__TFW-48.md`
- **RF claim:** one page, 544 words, five sections, status **assigned** not restored, `bc6779e` verdict verbatim, successor line *"Nothing replaced it."*
- **Actual:** `wc -w` → **544**. Headings in order: *What the task attempted · The owner's verdict · The failure mechanism · Recovering the full artifacts · What replaced it*. The header states the last live status `🟡 TS (D)` at `5b17786:README.md`:294 and that the terminal status *"was assigned by this phase, not restored"*. The `bc6779e` quotation matches `git log -1 --format=%B bc6779e` word for word, and the second quotation (*"Executed by Codex under explicit user instruction…"*) also matches. Successor line reads exactly as the TS approved. `grep -c "TFW-55"` → **0**.
- **Match:** ✅

### V8: `tasks/TFW-49__agent_commit_identity_and_attribution/POSTMORTEM__TFW-49.md`
- **RF claim:** 727 words, same five sections in the same order, the TFW-49 verdict quoted **whole** and byte-identical to `ad0696e`, `9e19a4f` described as a research-approval commit and explicitly not a contract baseline.
- **Actual:** `wc -w` → **727**. Identical heading sequence to V7. The seven-line verdict block was compared line by line against `git show ad0696e:tasks/TFW-49__…/HL-TFW-49__….md` lines 10–17 — **identical**, including the `[surface/task/work/role] summary` inline code and the en-dash in *"Phases A–C"*. The recovery table row 2 reads *"the commit that recorded the approval of TFW-49's research"* and carries the explicit **"Not a contract baseline"** clause with the reason. Successor is TFW-50 with the rejected subsystem enumerated.
- **Match:** ✅

### V9: `phase-e/evidence/EV__phase-e__rejected_trace_restoration.md`
- **RF claim:** 27 evidence rows plus the classification of all ten `REJECTED` hits. Verdict 26 VERIFIED / 1 DEFERRED.
- **Actual:** 27 rows present, environment header complete, per-AC coverage complete, verdict line matches. **The hit classification is short by two rows** — see D1a.
- **Match:** ⚠️ partial

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest docs/scripts/ -q` | **68 passed** in 48.16s — matches the RF's 68 and the Phase D baseline of 68. No new failures |
| 2 | PyYAML `safe_load` on both `project_config.yaml` files | Both parse. 11 statuses each, order ends `['BLOCKED','REJECTED']`, emoji `0x274c`, no `role` key |
| 3 | `git show 1e24e35 -- .tfw/conventions.md .tfw/glossary.md .tfw/CHANGELOG.md .tfw/project_config.yaml .tfw/templates/project_config.yaml` | conventions `+6/-0`; glossary two `-1/+1` hunks; CHANGELOG one hunk `+4/-1`; both configs `+3/-0` |
| 4 | `awk '/^## 14\) Anti-patterns/,/^### 14.1/' .tfw/conventions.md \| grep -c "^- "` | **39** |
| 5 | `grep -rn "REJECTED" .tfw/ README.md \| wc -l` | **12** — the RF and EV both say 10. **Discrepancy D1a** |
| 6 | `find tasks/TFW-48__* tasks/TFW-49__* -type f \| wc -l` | **2** — both `POSTMORTEM__*.md`. No `phase-*/`, no `research/`, no HL, no RF |
| 7 | `git ls-tree -r --name-only 721ca15 -- tasks/ \| grep -c "TFW-48\|TFW-49"` | **75** |
| 8 | `git show --shortstat bc6779e` | `149 files changed, 798 insertions(+), 27103 deletions(-)` — matches |
| 9 | `git show 5b17786:README.md \| sed -n '294,295p'` | 294 status cell `🟡 TS (D)`; 295 status cell `❌ REJECTED — complete product-fit failure; superseded by TFW-50` — both as claimed |
| 10 | `git log -1 --format="%h %ad %s" ad0696e` / `9e19a4f` | `ad0696e 2026-07-31 [codex/TFW-50/master/coordinator] reject TFW-49 and draft prompt-first replacement` · `9e19a4f 2026-07-30 [master]: TFW-49: approve agent commit identity research` — both resolve, both described accurately |
| 11 | `wc -w` on both post-mortems | 544 · 727 |
| 12 | `grep -n "^## "` on both post-mortems | Identical five-heading sequence, same order |
| 13 | Existence check on all 7 relative links (3 post-mortem, 4 board) | **7 of 7 resolve** |
| 14 | `git log --format="%h %s" \| grep -E "^\S+ \[[^]]*/TFW-53/freeze/"` | 7 freeze commits; latest **`11cd340`** — the contract baseline used for the Purpose Check |
| 15 | `git show 8d9432b^:README.md \| grep -c "REJECTED"` and `grep -n "^> Statuses:"` | **0** hits, legend at line **307** — the reconstruction that proves D1 |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | *"TFW-48 and TFW-49 remain in Git history as rejected experiments in delegating methodology redesign and execution to Codex without sufficient human supervision. They are historical context only and are not current methodology authority."* | Both post-mortems, § The owner's verdict | `git log -1 --format=%B bc6779e`, paragraph 3 — **word-for-word identical** in both files | ✅ |
| C2 | The seven-line TFW-49 final owner verdict, quoted whole | `POSTMORTEM__TFW-49.md` § The owner's verdict | `ad0696e:tasks/TFW-49__…/HL-TFW-49__….md` lines 10–17 — **identical**, no elision, punctuation and inline code preserved | ✅ |
| C3 | *"9e19a4f … Not a contract baseline — it carries no `freeze` scope word"* | `POSTMORTEM__TFW-49.md` recovery table | `git log -1 --format="%h %ad %s" 9e19a4f` → `[master]: TFW-49: approve agent commit identity research`, 2026-07-30. No `freeze` scope word, no `[agent/task/scope/role]` grammar. The description is exact and the TS's DoF on back-dating is honoured | ✅ |
| C4 | *"`grep -rn "REJECTED" .tfw/ README.md` → 10 hits"* | RF §4 verification table; EV §"The ten REJECTED hits, classified" | Re-executed → **12 hits**. `README.md`:298 and :299 are absent from the classification | ❌ **D1a** |
| C5 | *"The legend sits at line 307 as measured at the time of writing"* | RF §1 README line ledger; EV E1 artifact column | Reconstructed: the pre-edit README (`8d9432b^`) carried the legend at 307 with **zero** `REJECTED` hits. Adding the phase's own two rows above it moves it to **309**; it is **310** today after TFW-58's row. 307 is the *pre-edit* number, while 298/299 in the same ledger are *post-edit* numbers | ❌ **D1b** |
| C6 | *"75 files remain in git history"* | RF §1, both post-mortems, EV E14 | `git ls-tree -r --name-only 721ca15 -- tasks/ \| grep -c "TFW-48\|TFW-49"` → **75** | ✅ |
| C7 | *"Phase D baseline was 68 passed"* | RF §4 | Re-ran the suite: **68 passed**. Count matches; no test was added or removed by this phase | ✅ |

## Discrepancies Found

**D1 — the `REJECTED` site census undercounts by two, and the miss is the phase's own board rows.**

Two faces of one root cause: the census and the legend line number were taken from a `README.md` that
already carried the edited legend but **not yet** the two board rows.

| | Claimed | Actual | Where |
|---|---|---|---|
| **D1a** | `grep -rn "REJECTED" .tfw/ README.md` → **10 hits**; classified as *"Task status: 7 sites. Amendment verdict: 3 sites."* | **12 hits**. `README.md`:298 and `README.md`:299 — both **task status** — are missing. Correct split: **task status 9 · amendment verdict 3 · review verdict 0** | RF §4 verification table; EV §"The ten REJECTED hits, classified" and the *"Reconciling 7 against 10"* paragraph |
| **D1b** | *"The legend sits at line 307 as measured at the time of writing"* | 307 is the **pre-edit** line number. With the phase's own two rows inserted above it the legend was at **309** at RF-writing time, and is **310** now. The same ledger reports 298/299 for the rows, which are post-edit numbers | RF §1 README line ledger; EV E1 artifact column |

**Proof.** `git show 8d9432b^:README.md` — the last README state before the rows landed — has the legend
at line 307 and **zero** occurrences of `REJECTED`. So a census returning `README.md`:307 as a hit can only
have been run on a tree where the legend had been edited and the rows had not. Nine `.tfw/` hits plus that
one README hit is exactly the reported 10.

**Why it matters, and why it is not fatal.** No wrong content shipped: all five carriers are present and
correct (V1–V4, V6), and the two board rows are verified independently at E11–E13 and again at V6. The
defect is in the *evidence*, not in the product. But the TS made this census the designated reconciliation
— *"the EV file classifies every hit by which of the three meanings it carries, so the arithmetic is on the
page instead of left to the reviewer (ONB §5 risk 1)"* — and the arithmetic on the page is wrong by exactly
the two rows AC-3 exists to create. A reviewer who trusted the classification would conclude the board rows
were not carriers of the new status. This is the same defect class Phase D was sent back for on its first
pass (E17: a hunk count that did not reproduce).

**D2 — the board rows landed under a commit subject that names a different task.** `README.md` was
correctly left unstaged by the executor (TS §9, ONB Q2 (b)) and correctly disclosed in RF §1. It was then
committed in `8d9432b`, whose subject is `[claude-code/TFW-58/proposal/coordinator] propose the revise
protocol` and whose body does not mention TFW-53 or Phase E. The rows are in history — AC-3 is satisfied —
but `git log --oneline -- README.md` will not show a TFW-53/E commit for the deliverable of a phase whose
subject is honest traces. **Not attributable to the executor**: the coordinator landed it, after the RF was
written. Recorded as tech debt, not as a finding against this RF.

> Escalation: the two discrepancies triggered 100% verification. All 9 claimed files were opened and
> checked. No further discrepancy was found.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | Five carriers present; 10 hits classified | ✅ | ⚠️ — the five carriers are all present and correct at the cited lines, but the hit count is 10 against an actual 12, and `README.md`:307 is a stale line number (**D1**) |
| E2 | §5 side node, terminal, no outbound edge | ✅ | ✅ — `.tfw/conventions.md`:327, no edge leads out, `📚 KNW` / `✅ DONE` unreachable |
| E3 | REVISE/REJECT branch byte-unchanged, `6 0` numstat | ✅ | ✅ — reproduced exactly |
| E4 | Both YAML files parse, 11 statuses, order, emoji, no `role` | ✅ | ✅ — reproduced with PyYAML |
| E5 | Count sentence carries the ONB R6 wording | ✅ | ✅ — `.tfw/glossary.md`:130, matches the TS reference block |
| E6 | Collision stated at both ends; Amendment Log gains one clause only | ✅ | ✅ — `:57` and `:130`; diff is two single-line replacements |
| E7 | `templates/HL.md` untouched | ✅ | ✅ — absent from commit `1e24e35`; both `:246` and `:248` unchanged |
| E8 | §13 gains a third sentence, first two unchanged | ✅ | ✅ — additions only |
| E9 | §14 gains one bullet, 38 → 39 | ✅ | ✅ — count reproduced at 39, zero deletions |
| E10 | Framework text names no task and no repository | ✅ | ✅ — re-searched the added §13/§14 lines, 0 matches |
| E11 | Rows between TFW-47 and TFW-50, one-line description cells | ✅ | ✅ — 297 / **298** / **299** / 300 |
| E12 | Pre-restore comparison at `5b17786`:294–295 | ✅ | ✅ — both status cells reproduce exactly |
| E13 | TFW-49's cell a byte-identical restoration | ✅ | ✅ — compared against `5b17786:README.md`:295 |
| E14 | Six git references re-executed | ✅ | ✅ — 75 · `149 files, 798 insertions, 27103 deletions` · both status cells · `ad0696e` · `9e19a4f` |
| E15 | TFW-49 verdict byte-identical, whole | ✅ | ✅ — line-by-line against `ad0696e` (C2) |
| E16 | `bc6779e` sentence identical in both files | ✅ | ✅ — against `git log -1 --format=%B bc6779e` (C1) |
| E17 | `9e19a4f` described accurately, not as a baseline | ✅ | ✅ (C3) |
| E18 | 544 / 727 words | ✅ | ✅ — `wc -w` reproduced |
| E19 | Identical five-section order | ✅ | ✅ — `grep -n "^## "` reproduced |
| E20 | TFW-55 named in neither file | ✅ | ✅ — `grep -c "TFW-55"` → 0 twice |
| E21 | 7 of 7 links resolve | ✅ | ✅ — existence check reproduced |
| E22 | Exactly 2 files | ✅ | ✅ — `find … \| wc -l` → 2 |
| E23 | Nothing from `721ca15` re-entered the tree | ✅ | ✅ — the two folders hold one file each |
| E24 | CHANGELOG one hunk, `4 1` | ✅ | ✅ — reproduced |
| E25 | `[1.2.0]`, `VERSION`, `tfw.version` untouched | ✅ | ✅ — reproduced |
| E26 | 68 passed | ✅ | ✅ — re-ran, 68 passed |
| E27 | Board rows in the working tree, commit DEFERRED | ✅ | ✅ **and now discharged** — the rows are in `8d9432b`. The blocker was named honestly and has since cleared; see D2 for the residue |

**26 of 27 evidence rows verify cleanly. E1 is ⚠️ partial (D1). E27's DEFERRED status was correct when
written and is now resolved by the coordinator's commit.**

## Knowledge Citations Verified

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 | Not re-cited by this phase — the master HL's Knowledge Citations were verified at the freeze and Phase E adds none | N/A | N/A |
| 2 | RF §7 | `TD-174` — `templates/RF.md` §7 Scope vs Human-Only Test contradiction | ✅ | ✅ — `TECH_DEBT.md`:88, open, Med, backlog |
| 3 | RF §6 obs. 1 | `TD-175` — `❌ BLOCKED` at 0 uses across 46 board rows | ✅ | ✅ — `TECH_DEBT.md`:89, open, Med |
| 4 | RF §7, §8 | HL §11 S39 — the owner's vocabulary ruling | ✅ | ✅ — landed in the HL by `c2d00e9` |

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? *(9 of 9 — 100%, escalated on D1)*
- [x] Ran at least 1 build/test command (or documented why not)? *(`pytest docs/scripts/` → 68 passed; PyYAML parse; 15 commands logged)*
- [x] Claim & Source Checks filled — key claims spot-checked, every citation traced, data claims checked against a primary source? *(7 checks, C1–C7; the two verbatim verdicts compared against their commits, not read by eye)*
- [x] Each RF §3 (AC) checkmark verified against actual file? *(AC-1 through AC-6, every box)*
- [x] KNOWLEDGE.md checked — contradictions with changes documented? *(see judge.md; no contradiction — D37 board-as-memory and the P17 trace principle are both reinforced)*
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified? *(Total 4, verified 4, hallucinations 0)*
- [x] Evidence artifacts from RF §5 verified? *(Total 27, verified 26, partial 1, missing 0)*

Stage complete: YES

---

# Verify — second pass (corrective, 2026-08-18)

> Corrective commit: `5d0f86c` `[claude-code/TFW-53/phase-e/executor] correct the census to 12, fix the
> legend line, discharge the deferral`. Files touched: `README.md` (2 lines), the RF, the EV.
> Coordinator commits alongside it: `27a7bee` (TS note — no TS delta) and `86f159f` (HL §11 S40).

## Items from REVIEW §4, re-verified

| # | Required | State now | Verdict |
|---|----------|-----------|---------|
| 1 | EV E1 and the hit table: 10 → 12, add `README.md`:298 and :299, correct the legend line, retitle | E1 reads **12 hits**; the section is *"The twelve `REJECTED` hits, classified"*; the table has **12 rows**; hits 7 and 8 are the two board rows, both marked `new (AC-3)` and *"missing from the first count"*; the legend row reads `README.md`:310 | ✅ |
| 2 | Rewrite the reconciliation as 7 against 12, final split 9 / 3 / 0 | *"Reconciling 7 against 12"* with **four** uncounted reasons — the second is the new one: *"`README.md` carries the status three times, not once"*. Split counted independently from the table: rows 1–9 task status, rows 10–12 amendment verdict → **9 / 3 / 0** | ✅ |
| 3 | RF §4 census row: 12 hits, 9 / 3 / 0 | Row reads **12 hits — 9 task status, 3 amendment verdict, 0 new review verdict**, with a per-file breakdown (`README.md` 3 · `conventions.md` 2 · `glossary.md` 2 · `templates/HL.md` 2 · `project_config.yaml` 1 · `templates/project_config.yaml` 1 · `CHANGELOG.md` 1 = **12**), and cites finding D1a | ✅ |
| 4 | RF §1 ledger: one tree state for all three numbers | Ledger states *"All line numbers below are measured in the committed tree at `8d9432b`"*; legend row reads **310**; a TFW-58 row is added to the ledger and marked **not mine**; the paragraph *"Why the legend reads 310 and not 309"* explains that **three** lines were inserted, only two of them this phase's | ✅ — and it answers a question the review did not ask |
| 5 | RF header and §3 AC-3: discharge the ⚠️ | Header reads *"✅ `README.md` has landed"* and names `8d9432b`; AC-3's last item is `- [x] **Committed.**` with the confirming command; the TD-178 attribution gap is recorded on the same line | ✅ |
| +6 | *Not a review item* — E27 and the EV verdict line | E27 → **VERIFIED**, carrying **both** states (DEFERRED at collection, discharged since) rather than overwriting the first. EV verdict **27/27**; RF §5 matches. Justified on the page: leaving it DEFERRED while the RF reports the rows as committed would contradict item 5 within the same phase | ✅ — correct call, and the reason is stated rather than assumed |

## Commands Executed — second pass

| # | Command | Result |
|---|---------|--------|
| 1 | `grep -rn "REJECTED" .tfw/ README.md \| wc -l` | **12** — matches the corrected EV table row for row and line for line (`conventions.md` 327/342 · `glossary.md` 57/130 · `project_config.yaml` 108 · `templates/project_config.yaml` 112 · `templates/HL.md` 246/248 · `CHANGELOG.md` 9 · `README.md` 298/299/310) |
| 2 | `grep -n "^> Statuses:" README.md` | **310** — matches the corrected ledger |
| 3 | `git diff --stat 1e24e35 HEAD -- .tfw/ tasks/TFW-48__* tasks/TFW-49__*` | **empty** — no product file changed since the original phase commit |
| 4 | `git status --short .tfw/ tasks/TFW-48__* tasks/TFW-49__* README.md` | **empty** — nothing pending in the working tree |
| 5 | `git show 5d0f86c --stat` | `README.md` 2 lines, the RF, the EV. **No `.tfw/` file, no post-mortem** — the "no product file touched" claim reproduces |
| 6 | `git show 5d0f86c -- README.md` | The only board edits are the `[E🔄]` REVIEW link and the status cell returned from `🔄 REVISE (E)` to `🟢 RF (E)` for re-review. No other row touched |
| 7 | Residual-number sweep: `grep -n "307\|26/27\|\bten\b\|seven hits\|10 hits"` over both files | Every hit sits inside a *was → is* correction note — **except one**. See D3 |

## Discrepancies Found — second pass

**D3 — one stale numeral survives, in a descriptive cell.** `RF__…md`:50, the *New Files* table:

> `phase-e/evidence/EV__…md` | 27 evidence rows, plus the classification of all **ten** `REJECTED` hits

The EV now classifies **twelve**. This cell was not among the five items and the executor did not sweep it.

**Ruled non-material, and disclosed rather than blocked on.** It carries no verification claim: RF §4 (the
verification table), RF §1 (the ledger) and the EV (E1, the table, the reconciliation, the verdict) all
read 12 and all reproduce. A reader following the sentence arrives at a file whose own heading says
*"The twelve `REJECTED` hits"*, so the error self-corrects at the destination. Blocking a second time on
one numeral in a file-description cell is what baseline **DoF-13** and principle **P14** forbid — *"a block
must rest on material impact on the value, never on phrasing"* — and Phase D's second pass set the
precedent by approving with three stale arithmetic labels disclosed and ruled non-material. **To be
corrected in the closing commit**; the reviewer does not edit the RF (role lock).

> No other discrepancy. D1a and D1b are closed. D2 remains an open procedural item, filed as TD-178.

## Checkpoint — second pass

- [x] All five REVIEW items re-verified against the files, not against the correction note?
- [x] The self-declared "no product file touched" claim independently checked? *(commands 3–6)*
- [x] Corrected numbers re-executed rather than read? *(commands 1–2)*
- [x] Swept for residue the executor might have missed? *(command 7 → D3)*

Stage complete: YES
