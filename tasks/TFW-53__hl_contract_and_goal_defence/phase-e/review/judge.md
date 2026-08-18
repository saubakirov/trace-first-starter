# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | Frozen DoD-34/35/36 at baseline `11cd340` are all satisfied. AC-1 → V1–V4, V6: the status is present and correct in all five carriers, terminal, drawn as a side node, with the BLOCKED boundary and the three-way collision stated at both ends. AC-2 → V1: §13's third sentence and §14's 39th bullet, additions only, naming no task and no repository. AC-3 → V6: both rows at 298/299 between TFW-47 and TFW-50, TFW-48 marked assigned, TFW-49 byte-identical to `5b17786`. AC-4 → V7/V8, C1–C3. AC-5 → command 6, exactly 2 files. AC-6 → V5, one hunk. **Qualification:** AC-1's *gate* also required the EV census to classify every hit; the product passes, the census does not (row 8) |
| 2 | **(a) Purpose Check** · **(b) Design soundness** | ✅ | **(a)** Aligned — citation and harm in one field below. **(b)** Sound on three counts. The status is a **side node**, not a branch under `❌ REJECT`: TFW-48 was rejected out of `🟡 TS_DRAFT` having never reached a review, so drawing it under the review verdict would make a review outcome read as a route to a terminal state and break Phase A's branch (a) rule — baseline P3 (structural enforcement) and P9 (naming creates behavior). The **three-way collision** is closed at both ends without editing `templates/HL.md`, respecting §7.1 section ownership, at the cost of exactly one clause in the glossary article. The change is **additive-only** — `git diff` shows 6 insertions and 0 deletions in `conventions.md`, which is what makes "nothing else in the vocabulary changed" provable rather than asserted |
| 3 | Tech debt documented | ✅ | RF §6 carries three observations, each with a file, a line range, a type and a stated reason for leaving it. None is filler: obs. 1 is a diagram defect whose repair would require a decision the TS forbids; obs. 2 names a shipped file class missing from `conventions.md` §3; obs. 3 is a table-header/row arity mismatch that truncates the newest rows in a strict renderer. Two are promoted to new debt (row 5) |
| 4 | Style & standards | ✅ | Budget: **2 product files created, 6 modified**, against 15 new / 30 modified — the smallest phase in the task, as the TS predicted. Each carrier's existing form was matched rather than one form imported into all five (ASCII node, table row, YAML entry, prose sentence, legend clause). Commit subject `[claude-code/TFW-53/phase-e/executor] ship the REJECTED status, the trace rule, two post-mortems` follows the TFW-50 grammar. `README.md` was left unstaged exactly as TS §9 and ONB Q2 (b) directed, and the foreign TFW-55 line was named in the RF rather than committed |
| 5 | Observations collected | ✅ | Quality filter applied. Obs. **2** (`POSTMORTEM` is a shipped file class `conventions.md` §3 does not name) → **promote**: the next rejected task invents a second name for the same thing. Obs. **3** (board header declares 8 columns, rows carry 7/8/9) → **promote**: a header-trusting renderer truncates the newest rows, and the two rows this phase added are among them. Obs. **1** (the loose `❌ BLOCKED` edge) → **not new debt**: TD-175 already measures the same question from the other end and the owner asked for it to be recorded there |
| 6 | RF completeness (§7-9) | ✅ | §7 and §8 both declare **none** and state why, applying the Human-Only Test explicitly and naming TD-174 as the contradiction they are resolving against. This is the correct shape — Phase D was sent back for filling §7 from the Scope line, and this RF states which side of the contradiction it applies rather than leaving the reviewer to guess. §8 additionally flags, at the coordinator's request, that recreating the two folders gives a future whole-tree operation a live directory to restore into — an honest statement that the deliverable slightly enlarges the surface of the failure it describes. §9 carries three diagrams that earn their place: a before/after of the one carrier whose shape changed, the three-token disambiguation, and the failure mechanism |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | 27 rows, every AC-1–AC-6 Evidence field covered, environment header complete, valid statuses, one honestly-declared DEFERRED with its blocker named rather than omitted. Existence only — this does not certify the claims |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? | ❌ | **26 of 27 rows establish their claims.** **E1 does not** (D1). It reports `grep -rn "REJECTED" .tfw/ README.md` → **10 hits** and classifies them; the command returns **12**. The two missing hits are `README.md`:298 and :299 — the phase's own board rows, both task-status carriers. The correct split is **task status 9 · amendment verdict 3 · review verdict 0**, not 7/3/0, and the *"Reconciling 7 against 10"* paragraph is wrong as written. The same root cause makes RF §1's *"the legend sits at line 307 as measured at the time of writing"* a pre-edit number — it was 309 then and is 310 now, while the row numbers in the same ledger are post-edit. Proof: `git show 8d9432b^:README.md` has the legend at 307 and **zero** `REJECTED` hits, so the census ran after the legend edit and before the row insertions |
| 9 | Backward compatibility | ✅ | Consumers checked. `docs/scripts/gen_docs.py`:324–341 parses board rows by regex with no hardcoded status set — two new rows and a new status pass through; 68 tests confirm. `templates/project_config.yaml` was updated alongside the live config, so a project initialised from the template is born with the status instead of acquiring it by `/tfw-update` — the failure mode a config-only change would have created. No section number, template anchor or document heading was renamed. §14's new bullet is appended, so no existing entry's position is cited by index. The `❌` glyph is now shared by `BLOCKED` and `REJECTED`; no consumer keys on the emoji alone, and the ambiguity a shared glyph could create is exactly what the boundary sentence in every carrier exists to answer |
| 10 | Safety | ✅ | Markdown and YAML text only. No credentials, no destructive or irreversible operation, no shell or runtime shipped. The one act with a lasting footprint — recreating `tasks/TFW-48__*/` and `tasks/TFW-49__*/` — is bounded to one file each (verified at 2), disclosed in RF §8 with its own risk statement, and mitigated by the §14 anti-pattern the same phase ships. `bc6779e` and every historical commit are untouched |

## Purpose Check — row 2 clause (a)

**Reference set.** Master **HL-TFW-53 at contract baseline `11cd340`**, recovered by `conventions.md` §3
rule 15 (`git log --format="%h %s"` filtered on `^\S+ \[[^]]*/TFW-53/freeze/` — seven freeze commits,
`11cd340` the latest), plus the **Project North Star** in `.tfw/README.md` § The Thesis: Traces Over Code
and the root README. Neither the TS nor a Phase HL was used.

**Citation and harm, one field.** Serves baseline principle **P17** — *"A failed trace is the most valuable
trace — it records what cannot be re-derived. Reverting a result must never revert its evidence"* — and the
north-star thesis that the irreplaceable artifact is *"the trace — the record of intent, decisions,
constraints, and **rejected alternatives** that led to the result"*. Without this phase the framework has no
state that means *failed*, so the next task that fails is closed by lying with `✅ DONE`, misusing
`❌ BLOCKED`, or deleting the folder — and the project's two most expensive failures, 27,103 deletions and
six days, stay invisible on the board that is supposed to be its memory. That is material loss of
irreplaceable knowledge by method rather than by carelessness, not a wording preference.

**Excess and adjacency — no.** The deliverables are exactly baseline §4 Phase E items 1–5. Nothing from the
AT execution mode was pulled forward (DoF-4). No contract or review mechanism was added — the TS says so and
the diff confirms it. The one addition beyond the frozen text, `templates/project_config.yaml`, is strictly
more complete than DoD-34's four carriers rather than different from them, and AC-6's changelog block is a
recorded coordinator scope extension with a stated one-block limit.

**Deferral confession — no.** Every item the RF names a different home for was actually left there:
`templates/HL.md` (Phase A), `conventions.md` §3 (Phase A, obs. 2), the loose `BLOCKED` edge (TD-175), the
`templates/RF.md` §7 contradiction (TD-174), the `VERSION` bump (`/tfw-release`). None was shipped here.

**Materiality.** The harm prevented is the permanent loss of failure evidence — the one class of knowledge
the north star calls irreplaceable. The single revision finding concerns the truth of a count in the
evidence record; it does not make the delivered mechanism beside the point.

**Outcome: ✅ aligned.** Neither the purpose-failure nor the contract-defect outcome applies: the reference
set is internally consistent, and the work is what the owner approved.

## Frozen Definition of Failure — compliance

| Baseline DoF | Status | Basis |
|---|---|---|
| ❌ 4 — any part of the AT execution mode built here | ✅ not tripped | No delegation mechanism in the diff |
| ❌ 16 — the 75 TFW-48/49 artifact files re-added to the working tree | ✅ not tripped | `find … \| wc -l` → **2**; nothing from `721ca15` re-entered |
| ❌ 17 — `❌ REJECTED` introduced without a boundary against `❌ BLOCKED` | ✅ not tripped | The boundary sentence is present in all five carriers, verified individually |

| Phase DoF (TS §7) | Status | Basis |
|---|---|---|
| Review verdict `❌ REJECT` altered or made to look terminal | ✅ not tripped | 0 deleted lines in `conventions.md`; the REVISE/REJECT branch is byte-identical |
| TFW-48's row claims to be a restoration | ✅ not tripped | Row and post-mortem header both say **assigned**, with the last live status cited |
| A verdict paraphrased inside quotation marks, or a git reference that does not resolve | ✅ not tripped | C1–C3: both verdicts byte-identical to their commits; all six references re-executed |
| §13/§14 text names this repository or these two tasks | ✅ not tripped | Re-searched the added lines, 0 matches |
| Another phase's §14 entry edited | ✅ not tripped | 0 deletions |
| `9e19a4f` described as a contract baseline | ✅ not tripped | Described as a research-approval commit, with the back-dating reason stated |
| `VERSION`, `tfw.version` or `[1.2.0]` touched | ✅ not tripped | No diff in `VERSION`; `1.2.0` appears only as unchanged context |
| `README.md` staged while another session held it, or its foreign line committed unnamed | ✅ not tripped | Left unstaged; the TFW-55 line named in the RF ledger |
| The pre-existing loose `❌ BLOCKED` edge "fixed" | ✅ not tripped | Untouched; recorded as RF §6 obs. 1 |

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D37 — the README Task Board is pipeline memory | Two rejected rows restored to the board, and a rule that a rejected row is never deleted | **No** — the phase repairs a hole in that memory and makes the repair structural |
| 2 | D28 / P9 — naming creates behavior | Three tokens share the `❌ REJECT*` shape; each is named and bounded at every site it appears | **No** — the decision applied rather than contradicted |
| 3 | D61 — evidence completeness and evidence sufficiency are separate checks | EV declares 26/27 VERIFIED | **No implementation contradiction, but the RF claim fails D61's sufficiency discipline once:** E1 exists and does not prove what it is offered to prove (row 8) |
| 4 | `KNOWLEDGE.md`:184 — TFW-50 replaced TFW-49, nothing replaced TFW-48 | Both post-mortems' successor lines | **No** — matched exactly; TFW-55 correctly not named |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every `⚪ N/A` carries a stated reason — no row skipped as a bare ✅? *(no row was answered N/A)*
- [x] Row 2(a): answered against the contract baseline and the north star — never the TS or a Phase HL — with a quoted clause **and** a named harm in one field?
- [x] Rows 7 and 8 answered separately, with different reasoning? *(7 = the 27 rows exist and cover every AC; 8 = one of them does not establish its claim)*
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §7-9 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [x] Fact Candidates from RF reviewed — any that need challenge? *(RF §7 and §8 both declare none and justify it under the Human-Only Test. Correct, and it names TD-174 as the contradiction it resolves against. No challenge)*

Stage complete: YES

---

# Judge — second pass (corrective, 2026-08-18)

> Evidence: [verify.md § second pass](verify.md). Corrective commit `5d0f86c`; coordinator commits
> `27a7bee` (TS: no delta, with the reason) and `86f159f` (HL §11 S40).

| # | Check | 1st | 2nd | Evidence |
|---|-------|-----|-----|----------|
| 1 | DoD met? | ✅ | ✅ | Unchanged — no product file moved (`git diff 1e24e35 HEAD -- .tfw/ tasks/TFW-48__* tasks/TFW-49__*` is empty). AC-1's gate is now fully satisfied: the census classifies every hit, which was the one part outstanding |
| 2 | Purpose Check + design soundness | ✅ | ✅ | The citation and harm from the first pass stand — nothing in the corrective pass touches what the phase delivers. The pass itself *serves* the same clause: baseline **P17** is about honest records, and the fix makes the phase's own record honest |
| 3 | Tech debt documented | ✅ | ✅ | RF §6's three observations unchanged; TD-176/177 filed from them, TD-178 from the review |
| 4 | Style & standards | ✅ | ✅ | Corrective diff: `README.md` 2 lines, RF, EV. No product file, no `.tfw/` file, no post-mortem. The corrected figures are stated as *was → is* rather than silently replaced — the correct discipline for a permanent record, and the one this phase's own subject demands |
| 5 | Observations collected | ✅ | ✅ | No new observation was introduced by the corrective pass |
| 6 | RF completeness (§7-9) | ✅ | ✅ | §7 and §8 unchanged and still correct under the Human-Only Test; §9's diagrams unaffected |
| 7 | Evidence completeness | ✅ | ✅ | 27 rows; E27 now carries **both** states rather than overwriting the first |
| 8 | Evidence sufficiency | ❌ | ✅ | The single failure is closed. **12 hits** re-executed and matched row for row and line for line against the corrected table; the split **9 / 3 / 0** counted independently from the table rather than read off the summary; the legend at **310** confirmed; the per-file breakdown in RF §4 sums to 12. E27's discharge was checked against `git log -1 -- README.md` → `8d9432b`. **Residue: D3**, one stale numeral in a descriptive cell, ruled non-material below |
| 9 | Backward compatibility | ✅ | ✅ | No product change, so no consumer change. The `[E🔄]` REVIEW link added to the board resolves once this file exists |
| 10 | Safety | ✅ | ✅ | Markdown only; no credential, no destructive operation, no history rewritten |

## Purpose Check — second pass

**Outcome: ✅ aligned, carried and re-run.** Reference set unchanged: master HL-TFW-53 at contract baseline
**`11cd340`** plus the Project North Star in `.tfw/README.md` § The Thesis. The corrective pass serves the
same quoted clauses — baseline **P17**, *"a failed trace is the most valuable trace… reverting a result
must never revert its evidence"*, and the north star's *"rejected alternatives"* — by making the phase's own
evidence record reproduce. It adds no mechanism, ships nothing deferred, and pre-empts no other task. The
harm it prevents is the same one the phase exists to prevent, one layer in: a permanent record whose
arithmetic cannot be re-executed is the shape of the failure TFW-53 was written to answer.

## The materiality ruling on D3

The one surviving numeral (`RF`:50, *"all ten `REJECTED` hits"*) is **not** grounds for a second block.

| Test | Answer |
|------|--------|
| Does it carry a verification claim? | **No.** It is a file-description cell. Every claim-bearing site — RF §4, RF §1, EV E1, the EV table, the reconciliation, both verdict lines — reads 12 and re-executes |
| Does a reader end up misinformed? | **No.** The sentence points at a file whose own heading is *"The twelve `REJECTED` hits, classified"* |
| Material impact on the value? | **No** — baseline **DoF-13** and **P14**: a block rests on material impact, never on phrasing. Precedent: Phase D's second pass approved with three stale arithmetic labels disclosed and ruled non-material |

Disclosed in verify.md D3, to be swept in the closing commit. The reviewer does not edit the RF.

## Contradictions with KNOWLEDGE.md — second pass

| Knowledge item | Result |
|---|---|
| D61 — completeness and sufficiency are separate checks | The first-pass sufficiency failure is closed; the two rows are now answered with different reasoning and different outcomes across the two passes, which is the check working as designed |
| D37 — the board is pipeline memory | The status cell returned `🔄 REVISE (E)` → `🟢 RF (E)` for re-review and the `[E🔄]` link was kept. Both edits are board bookkeeping, correctly disclosed in the RF header |

## Checkpoint — second pass

- [x] Every row re-answered against second-pass evidence, not carried forward by assumption?
- [x] Row 2(a) re-run against the baseline and the north star?
- [x] Rows 7 and 8 still answered separately?
- [x] The one surviving defect explicitly ruled, with the rule cited, rather than quietly dropped?

Stage complete: YES
