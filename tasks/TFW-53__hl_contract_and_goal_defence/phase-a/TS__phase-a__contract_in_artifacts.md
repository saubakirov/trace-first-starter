# TS — TFW-53 / Phase A: Contract in Artifacts

> **Date**: 2026-08-10
> **Author**: Coordinator (Claude Code)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN, baseline `git log --grep='/TFW-53/freeze/'`

---

## 1. Objective

Make the HL contract exist as artifact state. Today an approved HL is indistinguishable from a draft: there is no approved marker, no record of what may not move, and no channel for a change that must not be made silently. This phase gives `templates/HL.md` a contract header, frozen/free marking and an append-only `§12 Amendment Log`; gives `templates/RES.md` a two-class recommendation split so a researcher classifies instead of proposing edits wholesale; and writes the governing rules into `conventions.md` — what freezes, at what granularity, how the baseline is recovered, and what a Phase HL may no longer do. Nothing here changes a workflow. Phase B makes the workflows obey what this phase defines.

## 2. Scope

### In Scope

- `templates/HL.md` — contract header block, frozen/free section marking, `§12 Amendment Log`, and the §3.1 Result Visualization gate (four properties).
- `templates/RES.md` — `HL Update Recommendations` split into `Refinements` and `Amendment Proposals`; removal of the line that instructs the coordinator to apply them.
- `conventions.md` — HL Contract definition (§3), granularity rule, baseline reference, Phase HL constraint, REJECT branch (a) redefinition (§5), and seven anti-patterns (§14).

### Out of Scope

- Any change to `plan.md`, `review.md` or `research/base.md` — Phase B and C own those. A rule defined here that is not yet enforced anywhere is the expected intermediate state.
- The Project North Star, PV Index priority 0/1, and the north-star header field — Phase C. `templates/HL.md` is touched again there; see §9.
- Glossary articles and adapter sync — Phase D.
- The `❌ REJECTED` status row and trace restoration — Phase E, which also edits `conventions.md` §5.
- The salami `git diff` pre-TS check — open thread, decided in Phase B TS or recorded in `TECH_DEBT.md`.

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P2 | Classify, never edit | AC-3 | `templates/RES.md` offers two classes and states the researcher never applies; the "Coordinator applies these" line is gone |
| P3 | Structural enforcement over guidelines | AC-1, AC-2, AC-6 | The contract is artifact state (header + §12) and a git-recoverable baseline, not advice |
| P5 | Evidence, cost, alternative | AC-2 | §12's column grammar makes all three mandatory fields; a row cannot be filled without them |
| P6 | Narrow D19, don't revoke it | AC-3 | RES still produces HL feedback; only the frozen channel changes from write to propose |
| P7 | Token density | AC-8 | Additions are numbered rules and table rows; no prose blocks. `conventions.md` growth measured in AC-8 |
| P9 | Naming creates behavior | AC-1, AC-2 | The shipped words are `Contract`, `FROZEN`, `Amendment`, `EXTEND`/`SUPERSEDE` — not "update recommendation" |
| P10 | Authority cannot self-extend | AC-7 | `conventions.md` states a delegated mandate is a ceiling and may not be cited to accept an overrun |
| P11 | A remark is not a verdict | AC-5 | `conventions.md` states research-thread input is never approval, and an owner-initiated change is itself an amendment |
| P12 | A frozen baseline must be diffable | AC-6 | Commit-before-research rule plus the reserved `freeze` scope word |
| P1 | The contract earns the autonomy | N/A | Task-level claim realised across all phases; no single Phase A artifact enforces it |
| P4 | Batch, don't interrupt | N/A | Escalation behaviour lives in `plan.md` — Phase B |
| P8 | Tool-agnostic by behavior | N/A | Adapter parity is Phase D; nothing here is tool-specific |
| P13–P16 | Purpose check, materiality bar, citation, judge against baseline | N/A | Review-side; Phase C |
| P17 | A failed trace is the most valuable trace | N/A | Phase E |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/templates/HL.md` | MODIFY | Contract header block; frozen/free marking; new `§12 Amendment Log`; §3.1 gate clauses |
| `.tfw/templates/RES.md` | MODIFY | Two-class recommendation split; delete line 32 comment |
| `.tfw/conventions.md` | MODIFY | §3 HL Contract + granularity + baseline + Phase HL rule; §5 REJECT branch (a); §14 seven anti-patterns |

**Budget:** 0 new files, 3 modifications, est. ~180 added lines. Defaults: max 14 files, max 8 new, max 1200 LOC, max 12 modified. Well within all four.

## 5. Acceptance Criteria

### AC-1: The HL declares its own contract state
`templates/HL.md` carries a header block that makes an approved HL structurally distinguishable from a draft, and marks every section as frozen or free.

- [ ] Header block carries a contract state field with at least the states "draft" and "frozen", plus the approval date
- [ ] **Three** states are marked, matching HL §3 exactly: 🔒 FROZEN (§1, §3, §4, §5, §6, §7), 🟢 FREE (§2, §7.2, §8, §9, §10, §11), 🟢 APPEND-ONLY (§12) _(corrected 2026-08-10 — the original two-state wording contradicted its own gate)_
- [ ] A pointer to the amendment channel (§12) is present in the header
- [ ] Each section heading carries its state marker inline (`## 1. Vision 🔒 FROZEN`), so the state is visible at the section and not only in the header. Verified safe for the docs build: `gen_docs.py` derives no anchors from headings

Gate: open `.tfw/templates/HL.md`, confirm all five items by reading. Cross-check the section lists against HL-TFW-53 §3's frozen/free table — the two must agree exactly.
Evidence: `N/A — template content; correctness is established by reading, and there is no runtime behaviour to observe.`

### AC-2: `§12 Amendment Log` exists with an enforceable column grammar
The template carries an append-only amendment log whose columns make evidence, cost and a considered alternative impossible to omit.

- [ ] `§12 Amendment Log` section exists with columns: number, date, section, type, **proposer**, proposed change, evidence, cost, alternatives considered, verdict _(proposer added 2026-08-10 per ONB Q1 — DoD-6 requires a logged proposer and had no field for one)_
- [ ] Type values are enumerated. Third value is **`RESTRICT`** if amendment A10 is approved, `APPLIED — restrictive` verbatim if rejected. **Ship this bullet last**; everything else in AC-2 is unblocked
- [ ] A restrictive change (adds a DoF, narrows scope, drops a deliverable) applies **on filing** with the verdict `✅ APPLIED — no owner verdict required`; restrictive-free is prohibited. Rule stated in `conventions.md` §3 beside the granularity rule _(iter1 D8, previously stated in no DoD item — ONB Q2)_
- [ ] The empty-verdict value is `PROPOSED`, with one line of D28 reasoning: it describes the state of the *request*, which is what the log tracks
- [ ] The section carries an explicit-N/A default ("No amendments.") per F21
- [ ] Instruction text states the log is append-only, that a frozen section may not be edited before its verdict, and that a research-thread remark is not a verdict

Gate: open the template; confirm the column set and the three type values; confirm the explicit-N/A line is present.
Evidence: The amended template must be able to carry HL-TFW-53's own §12 unchanged. Diff the shipped column grammar against the nine live rows in HL-TFW-53 §12 and record any field the template cannot hold. This is a real artifact with real rows, not a constructed example.

### AC-3: RES classifies instead of instructing
`templates/RES.md` splits its recommendations into two classes and no longer tells the coordinator to apply them.

- [ ] `HL Update Recommendations` contains two distinct tables: `Refinements` and `Amendment Proposals`
- [ ] Both tables carry a column naming the target HL section
- [ ] The `Amendment Proposals` table carries evidence, cost and alternatives columns, consistent with AC-2's grammar
- [ ] Instruction text states the researcher classifies but never applies, and that amendment proposals go to HL §12 as proposed
- [ ] The comment `<!-- List what should change in HL based on research. Coordinator applies these. -->` is **removed**

Gate: `grep -n "Coordinator applies these" .tfw/templates/RES.md` returns nothing; both tables present on reading.
Evidence: `N/A — template content.`

### AC-4: `conventions.md` defines the HL Contract [depends: AC-1]
The governing definition exists in one place: what freezes, when it freezes, and what append-only means.

- [ ] §3 defines the HL Contract: the six frozen sections, the moment of freezing (owner approval), and §12 as append-only
- [ ] The definition names the free sections and states that research updates them directly
- [ ] The frozen/free split matches `templates/HL.md` exactly — one source of truth, restated not re-decided

Gate: read `conventions.md` §3; diff the two section lists against `templates/HL.md` and against HL-TFW-53 §3.
Evidence: `N/A — convention text.`

### AC-5: An amendment verdict is a distinct recorded act [depends: AC-4]
The rule that closes the TFW-49 S6 failure mode, in both directions.

- [ ] `conventions.md` states that a verdict on an amendment is a distinct, recorded act
- [ ] It states that input given inside a research thread is never approval
- [ ] It states that an **owner-initiated** change to a frozen section is also an amendment, logged with the owner as proposer and the verdict on the same row

Gate: read `conventions.md`; confirm all three statements present and unambiguous.
Evidence: `N/A — convention text.`

### AC-6: The baseline is diffable [depends: AC-4]
An approved contract that cannot be diffed is not frozen. This closes the TFW-48 failure mode, where drift is documented and permanently unverifiable.

- [ ] `conventions.md` requires the approved HL to be committed **before** the first research iteration
- [ ] It defines the baseline reference as a reserved `freeze` scope word in the commit subject, consistent with D55's `[agent/task/scope/role]` grammar, and states that it applies to the **first** freeze as well as every re-freeze
- [ ] The documented recovery form is **slash-free** — `git log --grep="{TASK-ID}/freeze"`. The `/freeze/` form returns silently empty under Git Bash on Windows because MSYS rewrites the leading slash as a path _(measured; ONB Recommendation 1)_
- [ ] It states that no header field can name its own commit, so the baseline lives in the commit subject and not in the file

Gate: read `conventions.md`; then run the documented recovery command against this repository under **both** Git Bash and PowerShell and confirm both return the TFW-53 freeze commits.
Evidence: Run the documented command in this repository and capture its output. It must return the freeze commits created during TFW-53 planning. This is the mechanism working on live history, not a described intention.

### AC-7: Delegated authority is a ceiling [depends: AC-4]
The clause that prevents TFW-49's self-authorised overruns, landed here so TFW-54 inherits it rather than inventing it.

- [ ] `conventions.md` states that a delegated mandate is a ceiling and never a source of new permission
- [ ] It states that no agent may widen its own grant
- [ ] It states that delegation is never valid authority to accept a scope or budget overrun

Gate: read `conventions.md`; confirm all three statements.
Evidence: `N/A — convention text.`

### AC-8: The granularity rule and the carve-out are stated [depends: AC-4]
The decision that moves escalation from 4.6 to ~2.3 proposals per iteration. Without it the contract is correct and unusable.

- [ ] §3 states that the frozen unit is the **declarative claim**, not the section text
- [ ] It states what is frozen at claim level: the phase set and each phase's declared outcome, §3's to-be claims, §5/§6 items, §7 principles, §1
- [ ] It states that a deliverable-list change inside an already-approved phase is a refinement **unless** it cannot be accepted under the existing §5/§6 — the tripwire
- [ ] It states that non-substantive edits (typos, broken links, formatting) are not amendments
- [ ] `conventions.md` total word count is measured before and after; the delta is reported in the RF

Gate: read §3; then classify five **discriminating** recommendation rows from `research/iter1/RES.md` using only the shipped text — including at least two D4-tripwire cases where the naive reading and the RES classification diverge — and compare against the RES assignment.
Evidence: Record the exercise in the EV file with the shipped rule text quoted and each row's outcome, **and state the circularity limit explicitly**: the RES classifications were produced by the same researcher who wrote the rule, so agreement demonstrates the text is *readable*, not that the rule is *correct*. A 5/5 score presented as validation is worse than a 3/5 presented honestly.

### AC-9: The Phase HL may no longer author a contract [depends: AC-4]
Closes the drift channel one level below the master HL.

- [ ] §3 defines the Phase HL as derivation-only: it may restate master content and add execution context
- [ ] It states the Phase HL may not carry its own §1, §5, §6 or §7
- [ ] §14 carries an anti-pattern for a Phase HL that authors acceptance criteria or principles

Gate: read §3 and §14. Then read `git show 721ca15:tasks/TFW-48__*/phase-a/HL__phase-a__method_kernel.md` and confirm the shipped rule would classify it as a violation.
Evidence: Record in the EV file which specific parts of the historical TFW-48 Phase A HL the shipped rule prohibits — its own DoD, DoF and principle list. The rule is validated against the artifact that motivated it, not against a hypothetical.

### AC-10: `❌ REJECT` branch (a) no longer thaws the contract [depends: AC-4]
The one documented path that reopened frozen sections with no proposal, no evidence and no log.

- [ ] `conventions.md` §5 redefines branch (a) "rework HL" as filing an amendment against the frozen sections
- [ ] It states that re-entry to `📝 HL_DRAFT` does not thaw frozen sections
- [ ] The existing three-verdict vocabulary (APPROVE / REVISE / REJECT) is unchanged

Gate: read `conventions.md` §5; confirm the branch text changed and the verdict set did not.
Evidence: `N/A — convention text.`

### AC-11: Working Backwards and visualization become mandatory in §3.1 [depends: AC-1]
Four properties, in short clauses, appended to the existing §3.1 instruction block.

> ⚠️ **Revised 2026-08-10 by amendment A12.** The earlier wording carried a *budget and cut-order*
> property. It is **removed from the contract entirely** — do not implement it, in §3.1 or anywhere
> else. If any draft of this clause already mentions budget, slot, size, count or cut order, delete it.

- [ ] **Working Backwards, explicitly required** — §3.1 is written from the finished state as if it already exists, never as a description of the plan that will produce it
- [ ] **Visual rendering is mandatory, not a format option** — ASCII diagrams, flows, file and folder trees, before/after tables, mockups, sample output. Prose alone does not satisfy §3.1
- [ ] **The value is shown, not only the artifact** — what the result is worth is visible in the same picture
- [ ] **Complete enough to hold at once** — for multi-phase tasks every change carries its phase label and each phase gets one line saying what it is for
- [ ] The clause states that §3.1 is the owner's checkpoint **before** the spend of tokens and time
- [ ] The addition is a clause block, not a rewrite: the existing format options and the §3.2 contrast survive intact

Gate: read `templates/HL.md` §3.1; confirm the four properties and the checkpoint statement are present, the pre-existing instruction text is retained, and **no budget or cut-order language appears anywhere**.
Evidence: Apply the shipped §3.1 rule to HL-TFW-53's own §3.1 and record whether it passes all four properties. This HL now carries a file-level change map, a per-phase purpose map, an end-to-end flow and a six-months-later view, so a pass is expected — a failure would be a finding worth reporting.

### AC-12: The anti-pattern set is complete [depends: AC-4, AC-5, AC-7, AC-9]
`conventions.md` §14 gains the seven anti-patterns this phase's rules imply.

- [ ] Editing a frozen section without a logged owner verdict
- [ ] Submitting recommendations without classification
- [ ] Applying an amendment before its verdict
- [ ] Starting research on an uncommitted HL
- [ ] Treating a research-thread remark as a verdict
- [ ] Citing one's own delegation as authority to accept an overrun
- [ ] A Phase HL that authors its own acceptance criteria or principles

Gate: a **reproducible count of the §14 block specifically** — not a loose file-wide pattern, since `conventions.md` carries bullet lists in nine other sections. Record both counts and the exact command used, so the reviewer can rerun it. Confirm exactly seven additions and no removals.
Evidence: `N/A — convention text.`

### Evidence Artifacts

| File | Description |
|------|-------------|
| `phase-a/evidence/EV__phase-a__contract_in_artifacts.md` | Structured evidence: environment header, per-AC table, verdict _(required)_ |
| `phase-a/evidence/baseline_recovery.txt` | Output of the documented `git log --grep` recovery command (AC-6) |
| `phase-a/evidence/classification_exercise.md` | Five RES iter1 rows classified using only the shipped granularity rule (AC-8) |

## 6. Technical Guidance

> Reference material, not instructions. Deviate with justification in the RF.

- **The source of truth for the frozen/free split is HL-TFW-53 §3.** Do not re-derive it. Both `templates/HL.md` and `conventions.md` restate it; if the three ever disagree, the HL wins and the disagreement is a finding for the RF.
- **A worked example of everything in this phase already exists.** HL-TFW-53's own header, §12 (nine rows, all ruled) and §3.1 were written by hand as a prototype. Read them before writing the template — but treat them as a draft to improve, not a spec to copy. The HL says so explicitly in its own header note.
- **`conventions.md` is near its attention budget.** Every addition should be a numbered rule or a table row. Prose blocks are the failure mode here (F2, D23, `process.md` F4).
- **§14 is edited by four phases.** A owns the seven entries above; B, C and E append their own. Add, never restructure — a renumbering in this phase creates conflicts in three others.
- **`templates/RES.md` line 32** is the exact target of AC-3's deletion. It is the template-side twin of the `plan.md` Step 6c instruction Phase B rewrites; shipping one without the other reproduces the failure through the surviving channel.
- **Naming is a deliverable, not decoration** (D28). The words that must appear are `Contract`, `FROZEN`, `Amendment`, `Amendment Log`, `EXTEND`, `SUPERSEDE`, `RESTRICT`, `Contract Baseline`. _(the third Type value was `APPLIED — restrictive` until amendment A10 renamed it; do not ship the old token)_ Phase D consolidates the glossary; do not invent synonyms here that Phase D then has to reconcile.
- **Evidence proportionality.** Most ACs here are text edits, correctly marked `N/A`. Four are not, and they are the ones where a live artifact or live history can be observed: AC-2, AC-6, AC-8, AC-9, AC-11. Those are where the EV file earns its place.

## 7. Definition of Failure

- ❌ The frozen/free split in `templates/HL.md`, `conventions.md` and HL-TFW-53 §3 do not agree exactly.
- ❌ The contract rules ship as advisory prose without artifact state — the D17/Pattern-B failure, repeated inside the task that exists to prevent it.
- ❌ `templates/RES.md` retains "Coordinator applies these" while shipping the two-class split — DoF-1 delivered inside the enforcement site.
- ❌ The granularity rule is stated so abstractly that the AC-8 classification exercise cannot be completed from the shipped text alone.
- ❌ Any workflow file (`plan.md`, `review.md`, `research/base.md`) is modified in this phase.
- ❌ Any Phase C, D or E deliverable is delivered early "while we are in the file".
- ❌ `conventions.md` §14 is restructured or renumbered rather than appended to.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Rules land in `conventions.md` but the template does not carry the state, leaving the contract advisory | AC-1 and AC-2 are template ACs with their own gates; DoF names the failure explicitly |
| The granularity rule is written to sound right rather than to be applied | AC-8's five-row classification exercise against RES iter1 is a falsifiable gate, not a reading |
| `conventions.md` grows past its attention budget across four phases | AC-8 requires the word-count delta in the RF; B, C and E inherit the same measurement |
| The prototype in HL-TFW-53 is copied verbatim including its rough edges | Technical Guidance names it a draft to improve; AC-11 turns the HL's own §3.1 into a test subject |
| Section-level collisions with Phases B, C, E on `conventions.md` | §9 below; append-only discipline in §14; A sequenced before E on §5 |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/templates/HL.md` | Phase C | C adds the north-star pointer field to the same header block. Leave the block extensible; do not close it with a fixed field list |
| `.tfw/conventions.md` §5 | Phase E | A rewrites REJECT branch (a); E adds the `❌ REJECTED` status row. Different lines. Sequence A before E, or coordinate at E's TS time |
| `.tfw/conventions.md` §14 | Phases B, C, E | Append-only. Each phase adds its own entries; nobody renumbers |
| `.tfw/conventions.md` §3 | Phase C | C adds the Project North Star and PV priority 0/1 correction. A owns the HL Contract subsection; C adds its own |
| `.tfw/glossary.md` | Phase D | Terms shipped as text here are defined as glossary articles there. Use the canonical words listed in §6 so D has nothing to reconcile |

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2. Build script resolves to hyperlinks.

---

*TS — TFW-53 / Phase A: Contract in Artifacts | 2026-08-10*
