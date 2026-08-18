# TS — TFW-53 / Phase E: Rejected-Task Trace Restoration

> **Date**: 2026-08-18
> **Author**: Coordinator (Claude Code)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN
> **Covers**: frozen DoD 34–36
> **Predecessors read** (Pre-TS gate): [RF Phase D](../phase-d/RF__phase-d__glossary_adapters_version.md), [REVIEW Phase D](../phase-d/REVIEW__phase-d__glossary_adapters_version.md) — ✅ APPROVE, second pass. Phase E is independent of A–D; Phase D is read only for file-level collision, and it touched `conventions.md`, `glossary.md` and `project_config.yaml` in lines this phase does not use

---

## 1. Objective

TFW can record that a task succeeded, that it is waiting, or that it is in flight. It has **no way to record that a task failed.** The status set ends `✅ DONE` with `❌ BLOCKED` on the side, and blocked means waiting. Anyone closing a failed task must lie (`✅ DONE`), pretend (`❌ BLOCKED`), or delete the folder.

This phase ships the missing state and the rule that protects it: a terminal `❌ REJECTED`, a trace-discipline rule that reverting a *result* never reverts its *trace*, and an anti-pattern for the whole-tree restore that silently erases a failure status from the board.

Then it applies that machinery once. TFW-48 and TFW-49 return to the Task Board with one post-mortem file each — the first users of the new status, and the debt this project owes its own most expensive lesson.

## 2. Scope

### In Scope

**The rule — five files, every project on TFW gets it:**
- `❌ REJECTED` as a terminal status in `conventions.md` §5, `project_config.yaml`, `glossary.md` and the README legend
- `conventions.md` §13 — reverting a result does not revert its trace; a rejected task's folder and board row are never deleted
- `conventions.md` §14 — the whole-tree-restore anti-pattern

**The application — two files plus two board rows:**
- One post-mortem per rejected task, `tasks/TFW-48__*/` and `tasks/TFW-49__*/`
- Both board rows restored with `❌ REJECTED`

### Out of Scope

- **The 75 artifact files stay in git history and do not return to the working tree.** HL DoF-16 makes re-adding them a failure condition: this phase restores *visibility*, not content. Anything beyond one post-mortem per task is out of scope by name
- Rewriting `bc6779e` or any historical commit — the restore was performed under owner instruction and its trace is part of the record
- `❌ BLOCKED`'s meaning, or any other status
- Any part of the AT execution mode (HL DoF-4)

## 3. Principles Check

| # | Principle (HL §7) | Enforced by | Gate |
|---|-------------------|-------------|------|
| P17 | A failed trace is the most valuable trace — reverting a result must never revert its evidence | AC-2, AC-3 | The rule exists in §13, and the two rows are back on the board |
| P3 | Structural enforcement over guidelines | AC-1 | The status is a real state in four carriers, not advice to be careful |
| P9 | Naming creates behavior | AC-1 | `REJECTED` and `BLOCKED` are given a stated boundary, so agents cannot use them interchangeably |
| P8 | Tool-agnostic by behavior | AC-1 | The status lands in the framework's own carriers; no vendor mechanism |
| P1, P2, P4–P7, P10–P16 | contract mechanics, purpose defence, portability | N/A | Discharged in Phases A–D. This phase adds no contract or review mechanism |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/conventions.md` | MODIFY | §5 status set and diagram · §13 trace rule · §14 anti-pattern |
| `.tfw/project_config.yaml` | MODIFY | One `tfw.statuses` entry after `BLOCKED` |
| `.tfw/templates/project_config.yaml` | MODIFY | The same entry — a new project must be born with the status, not inherit it by upgrade |
| `.tfw/glossary.md` | MODIFY | `## Status Flow` — the diagram, the "9 statuses" count, and the REJECTED/BLOCKED boundary |
| `README.md` | MODIFY | Legend line 307 · two board rows between TFW-47 and TFW-50 |
| `tasks/TFW-48__value_first_methodology_rebaseline/POSTMORTEM__TFW-48.md` | CREATE | One page |
| `tasks/TFW-49__agent_commit_identity_and_attribution/POSTMORTEM__TFW-49.md` | CREATE | One page |
| `phase-e/evidence/EV__phase-e__rejected_trace_restoration.md` | CREATE | Structured evidence _(trace, not product — see the budget note)_ |

**Budget:** 5 modified, 2 new product files. Against 30 / 15 / 3000 / 30. The EV file and the RF are **trace, not product**, per the owner's ruling of 2026-08-18 recorded in TS Phase D AC-8; they are listed but do not spend the budget. Smallest phase in the task.

## 5. Acceptance Criteria

### AC-1: `❌ REJECTED` exists as a terminal state, with a stated boundary against `❌ BLOCKED`

- [ ] The status is present in **all four carriers**: `conventions.md` §5 (both the table and the ASCII transition diagram), `project_config.yaml` `tfw.statuses`, `.tfw/templates/project_config.yaml`, `glossary.md` `## Status Flow`, and the README legend line. A status missing from any one of them is a status agents will use inconsistently
- [ ] It is **terminal** — no transition leads out of it. `📚 KNW` and `✅ DONE` are not reachable from it
- [ ] The boundary is stated in one sentence wherever the two appear together: **`❌ BLOCKED` is waiting — the task resumes when the dependency clears. `❌ REJECTED` is closed unsuccessfully — the work stops and the trace is kept.** Frozen DoF-17 makes interchangeable use a failure of this phase, so the distinction must be written, not implied
- [ ] `glossary.md`'s *"9 statuses: … (+ BLOCKED)"* line is updated — it is a count, and a count that no longer counts is worse than no count
- [ ] **Nothing else in the status vocabulary changes.** No existing status is renamed, no transition is redrawn, and `❌ REJECT` the *review verdict* is untouched — it already exists in §5 and routes to an owner decision. The new item is a **task status**, and the RF states the distinction so a reviewer does not read one as the other

Gate: `grep -rn "REJECTED" .tfw/ README.md` → present in all five carriers; read §5's diagram for a terminal node
Evidence: the five sites, quoted

### AC-2: The trace survives the revert, as a rule [depends: AC-1]

`conventions.md` §13 is currently two sentences — every task produces an RF, the board tracks statuses, together they are the project's memory. It says nothing about deletion, which is why nothing was violated when the traces disappeared.

- [ ] §13 states that **reverting a result does not revert its trace**: a rejected task's folder and its board row are never deleted, and a revert that removes the work leaves the record of the work standing
- [ ] §14 carries the anti-pattern: **a whole-tree restore that silently reverts the Task Board past a task's failure status.** Worded from the mechanism, not from the incident — a blob-for-blob restore to an older tree reverts every file to a state that never contained the newer rows, so the loss is a side effect of the method and no one notices
- [ ] Both are added, not rewritten. §13's two existing sentences stay; §14 gains one entry beside the ones Phases A, B, C and TFW-56 added, and none of theirs is edited (HL §7.1 section ownership)
- [ ] The rule is **general**. It does not name TFW-48, TFW-49 or this repository — the framework file must read the same in a project that has never had a failure (F13)

Gate: `git diff .tfw/conventions.md` shows additions only, in §13 and §14
Evidence: N/A — textual

### AC-3: Two rejected tasks are visible on the board again

- [ ] Both rows are restored **between TFW-47 and TFW-50**, where they belong chronologically, each with `❌ REJECTED` and a link to its task folder
- [ ] **TFW-48's status is assigned, not restored, and the RF says so.** Its last live board status at `5b17786` was `🟡 TS (D)` — it was mid-flight when the restore removed it, not rejected. The terminal status rests on the owner's verdict in `bc6779e`: *"TFW-48 and TFW-49 remain in Git history as rejected experiments in delegating methodology redesign and execution to Codex without sufficient human supervision."* TFW-49's row **is** a restoration — `5b17786:README.md`:295 carried `❌ REJECTED — complete product-fit failure`. In the phase whose subject is honest traces, the difference between *put back* and *ruled now* is visible or the phase fails its own thesis
- [ ] The description cell of each row is one line and does not try to carry the post-mortem

Gate: read the board between TFW-47 and TFW-50; `git show 5b17786:README.md | sed -n '294,296p'` for the comparison
Evidence: the two rows, and the pre-restore rows they are compared against

### AC-4: One post-mortem per task, and it is one page [depends: AC-3]

Each file carries exactly five things, in this order:

- [ ] **What the task attempted** — two or three sentences, from its approved HL
- [ ] **The owner's verdict, verbatim and quoted.** For TFW-49, from the HL header at `ad0696e`: *"TFW-49 solved a small prompt-design need with an unnecessary software subsystem… Phases A–C remain immutable failure evidence; they are not the desired architecture."* For both, the restore commit's sentence quoted above. A paraphrase inside quotation marks is the defect this task corrected in Phase C — quote to the end of the sentence or do not quote
- [ ] **The failure mechanism**, stated as a mechanism rather than a story: blanket delegation granted at approval time → research produces a scope-expanding signal → the same coordinator amends the approved HL to absorb it → phase TSs derive from the amended HL → reviewers verify RF against those TSs → **nothing in the chain ever compares the result to what the owner approved.** This is the sentence TFW-53 exists to answer, and it belongs where a reader will find it without opening this task
- [ ] **The git references needed to recover the full artifacts** — all 75 files live at `721ca15`, recoverable with `git show 721ca15:<path>`; TFW-49's approved contract baseline is `9e19a4f`; the removal is `bc6779e` (149 files, 27,103 deletions); the pre-restore board rows are at `5b17786:README.md`:294-295. Every reference is checked to resolve before it is written
- [ ] **What replaced it** — TFW-49 → [TFW-50](../TFW-50__minimal_agent_commit_attribution/) (one readable subject rule, no runtime). TFW-48 → **name the successor or state plainly that there is none**; do not invent one
- [ ] **Length: one page.** These are signposts into git history, not restored artifacts. A post-mortem that grows into a narrative is DoF-16 arriving by a different door
- [ ] Both files carry the same section order, so the two read as one form rather than two essays

Gate: every git reference in both files is executed and resolves; `wc -w` per file
Evidence: the resolved references, with output

### AC-5: Nothing was restored that should have stayed in git

- [ ] `tasks/TFW-48__*/` and `tasks/TFW-49__*/` contain **exactly one file each**. No `phase-*/`, no `research/`, no HL, no RF
- [ ] `git status` shows no artifact file from `721ca15` re-entering the working tree
- [ ] The RF states the count explicitly: 2 files created against 75 that remain in history

Gate: `find tasks/TFW-48__* tasks/TFW-49__* -type f | wc -l` → 2
Evidence: the find output

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-e__rejected_trace_restoration.md` | Environment header, per-AC table, verdict _(required)_ |

## 6. Technical Guidance

> Reference material, not instructions. Deviate with justification in the RF.

**Why the loss happened, since the anti-pattern has to describe the mechanism and not the anecdote.** `bc6779e` was a blob-for-blob restore to the v0.9.0 tree. It reverted `README.md` to a state that never contained the TFW-48/49 rows. Immediately before it, the board did carry `❌ REJECTED — complete product-fit failure` for TFW-49. **The loss of failure status was a side effect of the restore method, not a decision** — which is exactly why a rule is worth more here than care.

**Everything below was verified by the coordinator before this TS was written:** 75 files under `721ca15`; `bc6779e` at 149 files and 27,103 deletions; the pre-restore rows at `5b17786:README.md`:294-295, with TFW-48 at `🟡 TS (D)` and TFW-49 at `❌ REJECTED`; `conventions.md` §13 at two sentences; the status absent from all four carriers; the board running TFW-47 → TFW-50 with the gap where the two rows belong.

**The status set's shape.** `conventions.md` §5 carries an ASCII transition diagram *and* a table, `project_config.yaml` carries a structured list with `id` / `emoji` / `description` / optional `role`, `glossary.md` carries a one-line diagram plus a count sentence, and README carries a single legend line. Four different shapes for one fact — match each carrier's existing form rather than importing one form into all four.

**Section ownership (HL §7.1).** Phase A owns `conventions.md` §3 and its §14 entries; C appended review-side §14 entries; TFW-56 added the checklist-row entry. **E owns §5 and §13 and appends one §14 entry.** Phase A already rewrote §5's REJECT branch (a) — that is the *review verdict*, a different thing from the task status this phase adds, and it must not be disturbed.

**Do not confuse the two REJECTs.** `❌ REJECT` already exists in §5 as a review verdict routing to an owner decision with three branches. `❌ REJECTED` is a terminal task status. They are adjacent, they share a glyph, and conflating them would make the review verdict look terminal — which would break Phase A's branch (a) rule. Name the distinction in the RF.

**Phase E is the last phase of the task.** After its review, TFW-53 goes to `/tfw-docs` and `/tfw-knowledge`, both pending since Phase A.

## 7. Definition of Failure

- ❌ Any TFW-48/49 artifact file beyond one post-mortem per task re-enters the working tree — HL DoF-16, restoring content instead of visibility
- ❌ `❌ REJECTED` ships without a stated boundary against `❌ BLOCKED` — HL DoF-17, agents then use them interchangeably
- ❌ The status is added to some carriers and not others, so a project reading one file disagrees with a project reading another
- ❌ The review verdict `❌ REJECT` is altered, merged with the new status, or made to look terminal
- ❌ TFW-48's row claims to be a restoration when it is a status assigned now
- ❌ A post-mortem paraphrases the owner's verdict inside quotation marks, or carries a git reference that does not resolve
- ❌ A post-mortem grows past one page and starts re-telling the task
- ❌ The §13 rule or the §14 anti-pattern names this repository or these two tasks — a framework rule written around one incident does not transfer (F13)
- ❌ Another phase's `conventions.md` §14 entry is edited (HL §7.1)
- ❌ `bc6779e` or any historical commit is rewritten

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| The post-mortems creep toward restoring the artifacts | AC-5's file count is a hard gate, and DoF names it first. The 75 files are one `git show` away and that is the design |
| `REJECTED` and `REJECT` blur, and Phase A's branch (a) rule breaks | Named in §6 and in DoF; the RF must state the distinction rather than assume the reader sees it |
| The anti-pattern is written as "do not do what happened to us" and does not transfer | AC-2's last bullet: the framework text names no task and no repository |
| TFW-48's assigned status reads as a restoration and quietly falsifies the record | AC-3's second bullet makes the distinction an acceptance criterion, not a footnote |
| The owner's verdict is quoted from memory | AC-4 requires every quotation checked against its commit. Phase C shipped a truncated citation once; the fix was to read to the end of the sentence |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/conventions.md` | A (§3, §5 branch (a), §14), B (§14), C (§3, §14), D (terminology) | E owns §5's status set and §13; appends one §14 entry. Never edit another phase's entry |
| `.tfw/glossary.md` | C (PV Index), D (ten articles, terminology) | E touches `## Status Flow` only |
| `.tfw/project_config.yaml` | D (`tfw.version` → 1.2.0) | E touches `tfw.statuses` only |
| `README.md` | every phase's board row; concurrent TFW-55 session | Stage by explicit path. If the file is held, leave it unstaged and say so — the coordinator lands it |

---

*TS — TFW-53 / Phase E: Rejected-Task Trace Restoration | 2026-08-18*
