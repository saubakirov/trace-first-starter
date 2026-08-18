# ONB — TFW-53 / Phase E: Rejected-Task Trace Restoration

> **Date**: 2026-08-18
> **Author**: Executor (Claude Code)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN, approved 2026-08-08
> **TS**: [TS Phase E](TS__phase-e__rejected_trace_restoration.md) — 🟡 TS_DRAFT
> **Covers**: frozen DoD 34–36

---

## 1. Understanding

TFW can say a task succeeded, is in flight, or is waiting. It cannot say a task failed. `❌ BLOCKED`
means waiting, `✅ DONE` means closed successfully, and nothing means closed unsuccessfully — so
whoever closes a failed task has to lie, misuse `BLOCKED`, or delete the folder. This project did the
third thing: restore commit `bc6779e` took the tracked tree back to the v0.9.0 blob-for-blob, and
`README.md` went back to a state that had never contained the TFW-48 and TFW-49 rows. One commit
earlier, `README.md`:295 had carried `❌ REJECTED — complete product-fit failure`. Nobody decided to
erase it. The restore method erased it, which is exactly why a rule beats care here.

Phase E ships three things and then uses them once.

The **state**: `❌ REJECTED` as a terminal task status, in every carrier that describes the status set,
with one sentence separating it from `❌ BLOCKED` — blocked is waiting and resumes, rejected is closed
and keeps its trace. The **rule**: `conventions.md` §13, currently two sentences about RFs and the
board, gains the clause that makes the erasure a violation — reverting a *result* never reverts its
*trace*, and a rejected task's folder and board row are never deleted. The **warning**:
`conventions.md` §14 gains the whole-tree-restore anti-pattern, worded from the mechanism, naming no
task and no repository, so a project that has never failed still reads it as a rule.

Then the application. Two folders come back holding one post-mortem file each — what the task
attempted, the owner's verdict quoted verbatim, the failure mechanism, the git references that recover
the full artifacts, and what replaced it. Two board rows come back as `❌ REJECTED`. The 75 artifact
files stay in git history where they are; restoring them is the phase's first named failure condition.

The point of caution: TFW-48's terminal status is **assigned now, not restored**. Its last live status
was `🟡 TS (D)` — mid-flight, not rejected. Only TFW-49's row is literally a restoration. In the phase
whose subject is honest traces, that difference has to be visible.

## 2. Entry Points

Every number below was measured in this session. Nothing is quoted from the TS unchecked.

| Carrier | Location | State measured today |
|---------|----------|---------------------|
| Status set — diagram + table | `.tfw/conventions.md`:316–345 (§5) | 10 statuses in the table, `❌ BLOCKED` last. ASCII diagram carries the REVISE / REJECT branch and a `↓ ❌ BLOCKED` node. No `REJECTED` |
| Status set — structured | `.tfw/project_config.yaml`:70–107 | 10 entries, `id: BLOCKED` last, shape `id` / `emoji` / `description` / optional `role` |
| Status set — template | `.tfw/templates/project_config.yaml`:74–111 | Identical 10 entries, header comment `# ← FRAMEWORK: updated by tfw-update` |
| Status set — glossary | `.tfw/glossary.md`:122–130 (`## Status Flow`) | One-line diagram plus the sentence `9 statuses: … (+ BLOCKED). RES and KNW are optional.` |
| Status set — board legend | `README.md`:307 | `> Statuses: ⬜ TODO → … → ✅ DONE \| ❌ BLOCKED` |
| Trace rule | `.tfw/conventions.md`:499–501 (§13) | Exactly two sentences. Says nothing about deletion — which is why nothing was violated |
| Anti-patterns | `.tfw/conventions.md`:503–556 (§14) | 38 bullets before the `### 14.1` subsection. Phases A, B, C and TFW-56 own entries here |
| Task Board gap | `README.md`:297 → 298 | TFW-47 is followed directly by TFW-50. Two rows missing |
| Rejected task folders | `tasks/` | `tasks/TFW-48__*` and `tasks/TFW-49__*` do not exist |

Git references from TS AC-4 — all executed, all resolve:

| Reference | Claim | Result |
|-----------|-------|--------|
| `721ca15` | 75 TFW-48/49 artifact files | ✅ `git ls-tree -r --name-only 721ca15 -- tasks/` filtered on the two IDs → **75** |
| `bc6779e` | 149 files, 27,103 deletions | ✅ `149 files changed, 798 insertions(+), 27103 deletions(-)` |
| `bc6779e` message | The owner's verdict sentence | ✅ verbatim: *"TFW-48 and TFW-49 remain in Git history as rejected experiments in delegating methodology redesign and execution to Codex without sufficient human supervision."* |
| `5b17786:README.md`:294–295 | TFW-48 at `🟡 TS (D)`, TFW-49 at `❌ REJECTED` | ✅ line 294 → `🟡 TS (D)`; line 295 → `❌ REJECTED — complete product-fit failure; superseded by TFW-50` |
| `ad0696e` | TFW-49 HL header carries the final owner verdict | ✅ commit `[codex/TFW-50/master/coordinator] reject TFW-49 and draft prompt-first replacement`; the verdict is a seven-line block quote in the HL header |
| `9e19a4f` | TFW-49's approved contract baseline | ⚠️ resolves — `[master]: TFW-49: approve agent commit identity research`, 2026-07-30. See inconsistency 4: it is an approval commit, not a `freeze`-scope commit |
| TFW-48 successor | Named anywhere? | ❌ nothing. A repository-wide search for `TFW-48` returns no task chartered to replace it. `KNOWLEDGE.md`:184 names TFW-50 as TFW-49's replacement only |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | **There are three `REJECT` homonyms in this repository, not two.** TS §6 warns me about the review verdict `❌ REJECT` versus the new task status `❌ REJECTED`. But `❌ REJECTED` **already exists** as a literal token — it is an amendment-log verdict value shipped by Phase A in `.tfw/templates/HL.md`:246, named again at :248. So after this phase `❌ REJECTED` means both *"the owner refused this amendment proposal"* and *"this task is closed unsuccessfully"*, and DoF-17's interchangeable-use failure applies to that pair as much as to `BLOCKED`. Which option — (a), (b) or (c) below? | _{coordinator fills in}_ |
| 2 | **How do I commit `README.md`?** The working copy is dirty with two uncommitted line edits: the TFW-53 row (this task's own C/D closure, not yet committed) **and** the TFW-55 row, changed by the concurrent TFW-55 session from `🔬 RES — 2/2 complete` to `🟡 TS_DRAFT (A)`. `git add README.md` stages all of it, so a Phase E commit would carry another session's in-flight work. TS §9 says *stage by explicit path; if the file is held, leave it unstaged and say so* — the two halves conflict here, because the explicit path **is** the held file. Which option — (a), (b) or (c) below? | _{coordinator fills in}_ |
| 3 | **Where does `❌ REJECTED` attach in the §5 ASCII diagram?** AC-1 needs a reader to see a terminal node; DoF forbids making the review verdict `❌ REJECT` look terminal. Those pull opposite ways, because the natural place to draw a rejection is under the REJECT branch — the one place I must not draw it. Option A or Option B below? | _{coordinator fills in}_ |

### Q1 — options

**(a) State the boundary inside the sections Phase E owns. No other phase's file is touched.** The new
`§5` status row and the `glossary.md` article each carry one clause naming all three tokens:
*"`❌ REJECTED` here is a task status. The review verdict `❌ REJECT` and the amendment verdict
`❌ REJECTED` in HL §12 are different objects, and neither is terminal."*

- Cost: one clause in two files. Zero scope growth.
- Consequence of skipping it: an agent grepping `REJECTED` finds two meanings and no statement that
  they differ — DoF-17's failure mode, arriving through a door the TS did not look at.

**(b) (a) plus one cross-reference line in `.tfw/templates/HL.md` §12.** The amendment verdict list
gains *"— not the `❌ REJECTED` task status (conventions.md §5)"*.

- Cost: **a file outside TS §4, in a section Phase A owns.** Needs an explicit scope extension recorded
  here, or it is a Role Lock violation and a breach of HL §7.1 section ownership.
- Benefit: the collision is stated at both ends, so whichever file an agent opens first, it learns
  there are two.

**(c) Ship (a) and log the other end as tech debt.** A TD row proposes the `templates/HL.md`
cross-reference for a later task.

- Cost: nothing now.
- Consequence: the debt register grows by one row that a two-word edit would have closed.

**My recommendation: (a).** It closes the hazard where this phase has authority to write, costs one
clause, and needs no scope extension. (b) is better text and worse process — it edits Phase A's section
on my own initiative, the exact behaviour HL §7.1 exists to stop. (c) leaves a known naming collision
open for the sake of a rule I could satisfy in the same sentence.

### Q2 — options

**(a) Commit `README.md` with all three line edits, and name the foreign line in the RF.** The Phase E
commit carries a TFW-55 row change it did not author.

- Cost: one commit whose diff misstates who changed what — a provenance defect, in the task about
  honest traces.

**(b) Make the README edits, leave the file unstaged, say so in the RF.** Everything else commits
normally; the coordinator lands the board. This is what TS §9 prescribes for a held file.

- Cost: the phase's own commit does not contain its board rows, so a reviewer reading the commit alone
  sees the rule shipped and the application missing. The RF has to point at the working tree.

**(c) Stage only my own lines.** Possible without an interactive prompt: write the intended README to a
temporary path, stage it through `git hash-object` plus `git update-index --cacheinfo`, then restore the
working copy — the index carries my rows, the working tree keeps the TFW-55 row.

- Cost: an index manipulation that is easy to get wrong and hard for a reviewer to verify. On a file two
  sessions are holding, the failure mode is silent loss of the other session's line.

**My recommendation: (b).** It is what the TS already ruled for this case, and the cost is a pointer in
the RF rather than a contaminated commit or a clever index trick. If you would rather have one
self-contained commit, (a) is acceptable **only** with the RF stating plainly that the TFW-55 row came
from another session — otherwise the commit lies about its own contents, in the phase whose thesis is
that traces must not lie.

### Q3 — options

**Option A — a terminal node to the side, reachable from anywhere.**

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE
                                                                              │
                                                                    ┌─────────┴─────────┐
                                                                    🔄 REVISE          ❌ REJECT
                                                                 (back to dev)    (user decides)
                    (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)        ↓
                                                           ❌ BLOCKED

  from any status ──→ ❌ REJECTED     terminal · no edge leads out · the trace is kept
```

Reads correctly against the facts: TFW-48 was rejected out of `🟡 TS_DRAFT`, TFW-49 after three
completed phases. Rejection is not a review outcome — it is an owner decision available at any point.
Leaves `❌ REJECT` exactly where Phase A put it.

**Option B — a fourth branch under the review verdict.**

```
                                                                    🔄 REVISE          ❌ REJECT
                                                                 (back to dev)    (user decides)
                                                                                         │
                                                                                    ❌ REJECTED
```

Compact, and wrong in a way that matters: it makes the review verdict look like a route to a terminal
state — the fourth item in this phase's own Definition of Failure — and it implies a task can only be
rejected after a review. TFW-48 disproves that.

**My recommendation: Option A.** Option B is listed because it is the shape a reader expects, and
naming why it fails is cheaper than defending the choice later.

## 4. Recommendations (suggestions, not blocking)

1. **Quote TFW-49's verdict whole, not elided.** AC-4 prescribes *"TFW-49 solved a small prompt-design
   need with an unnecessary software subsystem… Phases A–C remain immutable failure evidence; they are
   not the desired architecture."* Both fragments are verbatim and both end at a sentence boundary, so
   the `…` is honest. But the same AC says *"quote to the end of the sentence or do not quote"*, and the
   elided middle is where the owner listed **what was rejected** — the schema, the state, the Python
   validator and router, the git hooks, the range audit, the installation lifecycle. That list is the
   substance of the verdict. The full block quote is seven lines and fits the one-page budget. I intend
   to quote it whole and record the deviation in the RF.

2. **TFW-48's successor: state "none", and do not reach for TFW-55.** No task is chartered to replace it
   — verified across the repository. TFW-55 (TFW Foundations) works adjacent ground, philosophy and
   identity, and its own HL cites TFW-48/49 as a **negative** boundary, evidence of an over-engineering
   path. Naming it a successor would be the invention AC-4 forbids. Proposed line: *"Nothing replaced
   it. No successor task has been chartered."*

3. **`CHANGELOG.md` becomes factually wrong the moment this phase lands, and I am not the role that
   fixes it.** `[Unreleased]` reads *"Nothing pending."*, and the `1.2.0` entry states *"Phase E
   (rejected-task trace restoration) is independent and not in this release."* After Phase E there is
   something pending, and a project running `/tfw-update` receives a new task status with no changelog
   line announcing it. `VERSION` and `CHANGELOG.md` are `release.md` artifacts under a Coordinator role
   lock, and neither file is in TS §4. Recommend the coordinator carry this into `/tfw-release`. I will
   not touch either file.

4. **The board needs a fourth edit the TS did not list.** TS §4 names the legend line and the two new
   rows. Handoff steps 6 and 7 also require the TFW-53 row itself to move — `📚 KNW (A, B, C, D)` →
   `· 🟠 ONB (E)` → `· 🟢 RF (E)`, plus E's links in the TS, ONB and RF columns, matching what A–D
   already carry. Flagging it so a reviewer counting README edits against TS §4 does not read the
   fourth one as drift.

5. **`POSTMORTEM` is not a canonical artifact type, and I cannot make it one.** `conventions.md` §4
   requires every artifact filename to carry the task ID or a phase identifier, and
   `POSTMORTEM__TFW-48.md` satisfies that. But §3's artifact-type list — HL, RES, TS, RF, ONB, REVIEW —
   does not include it, and §3 belongs to Phase A under HL §7.1. So the phase ships a file class the
   conventions do not name. Recommend a coordinator decision: define the type in a later task, or accept
   it as a deliberately ad-hoc signpost file. Either way it goes into RF §6.

6. **Proposed replacement for the glossary count sentence**, so the wording is ruled on rather than left
   to me:

   > BEFORE — `.tfw/glossary.md`:130
   >
   > `9 statuses: TODO, HL_DRAFT, RES, TS_DRAFT, ONB, RF, REV, KNW, DONE (+ BLOCKED). RES and KNW are optional.`
   >
   > AFTER
   >
   > `9 pipeline statuses: TODO, HL_DRAFT, RES, TS_DRAFT, ONB, RF, REV, KNW, DONE. RES and KNW are optional. Two statuses sit outside the pipeline: ❌ BLOCKED — waiting, the task resumes when the dependency clears; ❌ REJECTED — closed unsuccessfully, terminal, the trace is kept.`

   The count stays 9 because the pipeline is unchanged; the two off-pipeline states are counted
   separately and given their boundary in the same breath.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **AC-1's gate returns more hits than AC-1 expects.** `grep -rn "REJECTED" .tfw/ README.md` will
   return the five new sites **plus** the two pre-existing `templates/HL.md` amendment-verdict lines —
   seven, not five. A reviewer running the gate literally sees a count mismatch and has to work out
   which hits are which. Mitigation: the EV file lists every hit with its classification, so the
   arithmetic is on the page instead of left to the reviewer.

2. **Every git reference has to resolve at review time, not only at write time.** Six commits are quoted
   across two post-mortems. All are reachable today; a future history rewrite would silently break both
   files. Mitigation: AC-4's gate is re-run during evidence collection and the raw output goes into the
   EV file, so the check is dated rather than asserted.

3. **One page is a tight budget for five required sections plus six git references.** The pull toward
   narrative is the DoF item *"a post-mortem grows past one page and starts re-telling the task"*.
   Mitigation: `wc -w` per file recorded in the EV file, and both files on the same section order so
   neither can quietly grow a sixth section.

4. **TFW-48 has no verdict of its own.** The only ruling naming it is the restore-commit sentence, which
   rules on both tasks jointly. TFW-49 additionally has a seven-line verdict written into its own HL. So
   TFW-48's post-mortem quotes a sentence about two tasks, and a reviewer may find that thin evidence for
   a terminal status. Mitigation: AC-3 already requires the row to say the status was assigned now; the
   post-mortem repeats it in the same words, and the *what it attempted* section cites the approved HL at
   `721ca15` so a reader can reach the original.

5. **Recreating the folder names restores a path that 75 files already match.**
   `tasks/TFW-48__value_first_methodology_rebaseline/` exists again, holding one file. Any future
   whole-tree operation touching that prefix — the very method this phase writes an anti-pattern against
   — now has a live directory to restore into. Low likelihood, and the §14 entry is the mitigation.
   Recorded because the deliverable slightly enlarges the surface of the failure it describes.

6. **`❌` now carries three meanings on one board.** `BLOCKED`, `REJECTED` and the review verdict
   `REJECT` share the glyph, so glyph-scanning a board no longer distinguishes waiting from failed. A
   distinct glyph would fix it, and I am not proposing one: AC-1 fixes the token as `❌ REJECTED` and
   forbids changing any existing status. Recorded as a known cost of the chosen vocabulary.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS §6 says the status is "absent from all four carriers" — the carriers, yes; the token, no.**
   `❌ REJECTED` is already in `.tfw/templates/HL.md`:246 and :248 as an amendment-log verdict. TS §6's
   *"Do not confuse the two REJECTs"* frames a two-way distinction over a three-way collision. This is
   the substance of blocking Q1.

2. **AC-1 says "all four carriers" and then lists five sites.** The prose reads *"present in all four
   carriers"*; the enumeration names `conventions.md` §5, `project_config.yaml`,
   `templates/project_config.yaml`, `glossary.md` and the README legend — five — and the gate line below
   it says *"present in all five carriers"*. TS §4 also lists five files. I am treating the enumeration
   and the gate as authoritative: **five sites**. The word "four" reads as a leftover from before
   `templates/project_config.yaml` was added; it also appears in frozen HL DoD-34, which names four. No
   amendment is needed — DoD-34's four are all inside the five, and shipping the template as well is
   strictly more complete, not different.

3. **`README.md`:307 is correct today and will not stay correct.** The legend is the file's last line and
   two sessions are editing the board, so the RF should report the line number as measured at commit time
   rather than copied from the TS.

4. **`9e19a4f` is an approval commit, not a contract baseline in the §3 sense.** Its subject is
   `[master]: TFW-49: approve agent commit identity research` — a research approval from 2026-07-30. It
   carries no `freeze` scope word, because the `[agent/task/scope/role]` grammar and the reserved `freeze`
   word are products of TFW-50 and of this very task, both later. TS AC-4 calls it *"TFW-49's approved
   contract baseline"*. I will cite it accurately — *the commit that recorded the approval* — rather than
   reproduce a term the commit predates. Calling a July commit a contract baseline, in a phase about
   honest records, is the kind of quiet back-dating this task exists to prevent.

5. **`conventions.md` §5's diagram already has a loose edge.** The `↓` above `❌ BLOCKED` sits under the
   *skip* annotation with no clear source node, so it is unclear what transitions into BLOCKED. It is
   pre-existing, it is inside a section Phase E owns, and repairing it is in no AC. I intend to leave it
   exactly as it is and report it in RF §6 — an uncommissioned §5 tidy-up is a bonus fix, and §14
   prohibits those. Say the word if you want it repaired inside this phase.

## 7. Knowledge Citations

Read all 26 items in HL §7.2. Phase E is the task's smallest and least mechanism-heavy phase, so most
citations were discharged in Phases A–D and are honestly N/A here. The ones that bind this phase say how.

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | `.tfw/README.md` § Structural Enforcement | ✅ | **Applied** | *"The filesystem is the state machine."* The status has to be a real entry in the status set of every carrier, not advice to be careful — and the post-mortem is a **file** in a recreated folder, so the failure is visible by directory listing rather than by memory |
| 2 | `.tfw/README.md` § Naming Creates Behavior | ✅ | **Applied** | The whole of Q1. `REJECTED` carries the association `BLOCKED` cannot — and the same force is why a third token spelled identically is a hazard, not a coincidence |
| 3 | `.tfw/README.md` § Candor Over Flattery | ✅ | **Applied** | Q1, Q2 and inconsistencies 1 and 4 are uncomfortable findings about the TS I was handed. Raising them is the citation being used |
| 4 | `KNOWLEDGE.md` §1 D19 — HL update = mandatory RESEARCH output | ✅ | N/A | Research channel. Phase E runs no research iteration |
| 5 | `KNOWLEDGE.md` §1 D20 — implicit approval = status transition | ✅ | **Applied, obliquely** | D20 is why a status that does not exist cannot be reached. There was no `REJECTED` to transition into, so the failed tasks had nowhere to land — the same root cause as the contract work, one layer down |
| 6 | `KNOWLEDGE.md` §1 D23 — workflow compression, `plan.md` at budget | ✅ | N/A | Phase E touches no workflow file |
| 7 | `KNOWLEDGE.md` §1 D24 — Pattern A, inline defaults over indirection | ✅ | **Applied** | The BLOCKED/REJECTED boundary is written inline at each site, not stated once with four cross-references. It is why AC-1 demands the sentence *wherever the two appear together* |
| 8 | `KNOWLEDGE.md` §1 D31 — filesystem as state machine | ✅ | **Applied** | As 1: the recreated folder holding one file *is* the record |
| 9 | `KNOWLEDGE.md` §1 D49 — gates beat guidelines | ✅ | **Applied** | §13's rule is the guideline; the §14 anti-pattern and the restored board row are what make it checkable |
| 10 | `KNOWLEDGE.md` §1 D54 — adapter parity is a behavioral promise | ✅ | **Applied as a boundary** | The status lands in `.tfw/` and in the config **template**, so a newly initialised project is born with it rather than needing an upgrade. No adapter file carries the status set, so nothing under `.claude/`, `.agents/` or `.agent/` needs re-syncing — checked before writing this |
| 11 | `knowledge/philosophy.md` F4 — structural over format enforcement | ✅ | **Applied** | Same mechanism as 1 and 8 |
| 12 | `knowledge/philosophy.md` F13 — TFW is domain-agnostic | ✅ | **Applied, load-bearing** | AC-2's last bullet and a DoF item both rest on it: §13 and §14 must name no task and no repository. A rule written around one incident does not transfer, and this repository's incident is unusually vivid — which makes the temptation stronger, not weaker |
| 13 | `knowledge/philosophy.md` F21 — explicit N/A | ✅ | **Applied** | RF §7–9 get explicit content or an explicit "No X."; the EV file marks any AC it cannot verify rather than omitting the row |
| 14 | `knowledge/philosophy.md` F22 — template minimalism | ✅ | **Applied as a boundary** | Phase E adds no template section anywhere. `templates/project_config.yaml` gains one status entry in an existing list — data, not structure |
| 15 | `knowledge/philosophy.md` F25 — framework proposes, human decides | ✅ | **Applied** | Every blocking question above carries options with cost and the consequence of declining, and keeps my recommendation separate from the options. No decision taken on the owner's behalf |
| 16 | `knowledge/process.md` F4 — numbered steps and gates work, prose loses agents | ✅ | **Applied** | The §14 entry is one bullet in the established voice, not a paragraph about what happened here |
| 17 | `knowledge/process.md` F6 — coordinator drifts into scope explosion | ✅ | **Applied** | The recorded, unfixed instance of the failure the two post-mortems document. It is also why recommendations 3 and 5 stop at *recommend*: `CHANGELOG.md` and `conventions.md` §3 sit outside this phase's grant, and an executor quietly widening its own scope is the same failure in miniature |
| 18 | `knowledge/process.md` F14 — agents fast-run without structural enforcement | ✅ | **Applied** | *"Agents always want to finish faster."* The 75 files are one `git show` away, and restoring them would look like thoroughness. AC-5's file count is the structure that stops it |
| 19 | `knowledge/process.md` F20 — HL is authoritative on WHAT; the user decides on divergence | ✅ | **Applied** | Inconsistency 2 is exactly an HL/TS divergence — four carriers against five. F20's resolution is *ask*, so it is written here with my reading stated rather than resolved silently |
| 20 | `knowledge/constraint.md` F2 — >1200 words degrades a workflow | ✅ | N/A | No workflow file is touched. The one-page post-mortem budget is a different constraint from a different source (DoF) |
| 21 | `.tfw/conventions.md` §7 — Execution Modes CL/AG | ✅ | N/A | Phase E adds no execution mode. HL DoF-4 puts any part of AT out of bounds |
| 22 | `.tfw/conventions.md` §15 — Role Lock Protocol | ✅ | **Applied, load-bearing** | It is why recommendation 3 stops at a recommendation — `VERSION` and `CHANGELOG.md` are `release.md` artifacts under a Coordinator lock. It is also Q1 option (b)'s real cost, and the reason no REVIEW file will follow this RF |
| 23 | `KNOWLEDGE.md` §1 D55 — minimal commit attribution | ✅ | **Applied** | Commits use `[claude-code/TFW-53/phase-e/executor] …`, matching the A–D pattern in this task's history |
| 24 | `knowledge/process.md` F11 — organic emergence, then formalisation | ✅ | **Applied** | `5b17786:README.md`:295 shows a coordinator hand-writing `❌ REJECTED` into the status column of a framework that offered no such status. Phase E formalises what the board already did once under pressure — the documented pattern, not an invention |
| 25 | `KNOWLEDGE.md` §1 D43 — Knowledge Citations as the anti-hallucination device | ✅ | **Applied, load-bearing** | The same mechanism as AC-4's verbatim-quote rule, for the same reason. It is why recommendation 1 argues for the whole verdict over the elided one, and why every git reference in §2 carries its executed output instead of a claim that it resolves |
| 26 | `KNOWLEDGE.md` §1 D46 — Reviewer Identity, Trust Protocol | ✅ | N/A | Review-side. Named here only because this phase's subject matter is D46's cautionary case: seven REVIEW verdicts, six of them `✅ APPROVE`, on the work the owner then rejected wholesale (`721ca15`) |

**New items the coordinator did not cite, relevant to this phase:**

| # | Source | Item | Why it matters here |
|---|--------|------|--------------------|
| N1 | `KNOWLEDGE.md` §3 Legacy, line 184 | *"TFW-48 methodology rebaseline and TFW-49 commit-attribution implementations — Rejected / history only, 2026-08-04. Their tracked result was reverted to v0.9.0. TFW-50 independently restores only the readable commit-subject outcome…"* | The nearest thing to an existing post-mortem, and the source of record that TFW-50 replaced TFW-49. It also confirms by omission that **nothing** replaced TFW-48 — grounding recommendation 2 in a verified fact rather than in a failed search |
| N2 | `.tfw/conventions.md` §4 — trace rule for research folders | *"Iteration folders accumulate — never delete or overwrite previous iteration's files. Each `research/iterN/` folder is a trace. Deleting them = deleting reasoning."* | §13's new rule already exists in the conventions **as a special case for research folders**. Phase E is generalising a rule the file states narrowly. Worth echoing its phrasing so the two read as one principle rather than two coincidences — which is why it is listed before §13 gets written |
| N3 | `tasks/TFW-45__multi_agent_workflows/PROPOSAL__TFW-45__review_swarm_consolidator.md`:127 | *"TFW-48/49 REVIEWs — seven verdicts, six ✅ APPROVE, on work the owner later rejected wholesale"*, with the recovery path `git show 721ca15:<path>` | An independent citation of the same failure in a live proposal. Confirms the post-mortems point at a mechanism other tasks already reason from, and gives the failure-mechanism section a second source outside TFW-53 |

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2. Build script resolves to hyperlinks.

---

*ONB — TFW-53 / Phase E: Rejected-Task Trace Restoration | 2026-08-18*
