# RF — TFW-53 / Phase E: Rejected-Task Trace Restoration

> **Date**: 2026-08-18
> **Author**: Executor (Claude Code)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN, approved 2026-08-08
> **TS**: [TS Phase E](TS__phase-e__rejected_trace_restoration.md) — amended 2026-08-18 after ONB
> **ONB**: [ONB Phase E](ONB__phase-e__rejected_trace_restoration.md) — answered 2026-08-18, three blockers cleared
> **Covers**: frozen DoD 34–36
> **REVIEW**: [REVIEW Phase E](REVIEW__phase-e__rejected_trace_restoration.md) — 🔄 REVISE, one finding in
> the evidence record. **Corrected 2026-08-18**, five items, all inside the approved TS; see the correction
> note below
>
> ✅ **`README.md` has landed.** The board rows, the legend and this task's own row are committed in
> `8d9432b`. During execution the file was held by a concurrent TFW-55 session, so per TS §9 and the ONB
> Q2 answer (b) this phase's commit deliberately left it unstaged and the coordinator landed it. §1 carries
> the line-by-line ledger of whose line is whose. Note for the record: `8d9432b`'s subject is
> `[claude-code/TFW-58/proposal/coordinator] propose the revise protocol` and does not name TFW-53 —
> recorded as TD-178 by the review, and a procedural gap rather than a defect in this phase's work.

> **Correction note — 2026-08-18, after REVIEW Phase E.** The verdict was 🔄 REVISE on one finding: two
> numbers in the evidence record did not reproduce. Both came from one cause — the `REJECTED` census and
> the README legend line number were taken from a tree that already carried the edited legend but **not
> yet** the two board rows, so a mid-execution snapshot was recorded as the final state.
>
> | # | Where | Was | Is |
> |---|-------|-----|-----|
> | 1–2 | EV — E1, the hit-classification table, the reconciliation paragraph | 10 hits · split 7 / 3 / 0 | **12 hits** · split **9 / 3 / 0**, with `README.md`:298 and :299 added as the two missing task-status carriers, and every command re-executed with its output quoted |
> | 3 | RF §4 — the census row | 10 hits · 7 / 3 / 0 | **12 hits** · **9 / 3 / 0** |
> | 4 | RF §1 — the README line ledger | legend at **307**, a pre-edit number sitting beside two post-edit ones | legend at **310**, all three numbers from the same tree state, with the reason it moved |
> | 5 | RF header · §3 AC-3 | ⚠️ held by another session | discharged — landed in `8d9432b`, box checked |
> | +6 | EV — E27 and the verdict line | DEFERRED · 26/27 | **VERIFIED · 27/27** — not one of the review's five items, corrected because leaving it would contradict item 5 in the same phase's other file |
>
> **No product file was touched by this pass.** `.tfw/`, both post-mortems and `README.md`'s rows and
> legend were verified clean at 100% coverage and are unchanged. The one README edit in this pass is board
> bookkeeping: the TFW-53 status cell moves `🔄 REVISE (E)` → `🟢 RF (E)` for re-review. **`README.md` is
> committed this time** — the concurrent TFW-55 session's changes landed in `8d9432b`, so the file is no
> longer held and the only pending line was this phase's own status cell.

---

## 1. What Was Done

### New Files

| File | Description |
|------|-------------|
| `tasks/TFW-48__value_first_methodology_rebaseline/POSTMORTEM__TFW-48.md` | One page, 544 words. Five sections; status **assigned** now, not restored |
| `tasks/TFW-49__agent_commit_identity_and_attribution/POSTMORTEM__TFW-49.md` | One page, 727 words. Same five sections in the same order; board status **restored** |
| `phase-e/evidence/EV__phase-e__rejected_trace_restoration.md` | 27 evidence rows, plus the classification of all ten `REJECTED` hits _(trace, not product)_ |

**2 files created against the 75 that remain in git history** (AC-5). Nothing from `721ca15` re-entered
the working tree.

### Modified Files

| File | Changes |
|------|---------|
| `.tfw/conventions.md` | **§5** — one side node in the ASCII diagram, one table row after `❌ BLOCKED`. **§13** — the trace rule as a third sentence. **§14** — one appended bullet (38 → 39). `git diff --numstat` → **6 insertions, 0 deletions**: additions only, in the three sections Phase E owns |
| `.tfw/project_config.yaml` | One `tfw.statuses` entry after `BLOCKED`. `tfw.version` untouched |
| `.tfw/templates/project_config.yaml` | The same entry, so a new project is born with the status instead of acquiring it by upgrade |
| `.tfw/glossary.md` | `## Status Flow` — the count sentence replaced with the ONB R6 wording plus the three-way boundary. `### Amendment Log` — **one appended clause, nothing else in that article** |
| `.tfw/CHANGELOG.md` | `[Unreleased]` — *"Nothing pending."* replaced by one `### Added` block (AC-6). One hunk. `[1.2.0]` and `VERSION` untouched |
| `README.md` | Two board rows, the legend, this task's own row. Left unstaged during execution because the file was concurrently held; **landed by the coordinator in `8d9432b`.** See the line ledger below |

### `README.md` line ledger — whose line is whose

All line numbers below are measured in the **committed tree** at `8d9432b`, so every number in this table
comes from one state. _(Corrected 2026-08-18 — the legend was first reported at 307, a pre-edit number
standing beside two post-edit ones. REVIEW finding D1b.)_

| Line | Content | Author |
|------|---------|--------|
| 298 | TFW-48 board row, `❌ REJECTED`, status assigned | **this phase** |
| 299 | TFW-49 board row, `❌ REJECTED`, status restored byte-identical from `5b17786` | **this phase** |
| 310 | The legend, extended with `❌ BLOCKED (waiting) \| ❌ REJECTED (closed unsuccessfully, trace kept)` | **this phase** |
| TFW-53 row | Status `📚 KNW (A, B, C, D) · 🟢 RF (E)`, plus E's links in the TS, ONB and RF columns | **this phase** (routine handoff work, ONB R4) |
| TFW-55 row | `🔬 RES — 2/2 complete; A1 verdict pending` → `🟡 TS_DRAFT (A)`, plus the phase-A TS link | **not mine** — the concurrent TFW-55 session |
| TFW-58 row | A new proposal row, added above the legend by `8d9432b` | **not mine** — the coordinator, in the same commit that landed the board |

**Why the legend reads 310 and not 309.** Three lines were inserted above it, not two: this phase's two
board rows, and the TFW-58 proposal row the coordinator added in the same commit. Only two of the three
displaced lines belong to this phase. Before the insertion the legend was at 307 with **zero** `REJECTED`
occurrences in the file — `git show 8d9432b^:README.md`.

### The seven sites, quoted

**`.tfw/conventions.md` §5 — the diagram gains a side node; the REVISE/REJECT branch is not touched:**

```
                    (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)        ↓
                                                           ❌ BLOCKED

  from any status ──→ ❌ REJECTED     terminal · no edge leads out · the trace is kept
```

**`.tfw/conventions.md` §5 — one table row after `❌ BLOCKED`:**

> | ❌ REJECTED | Task closed unsuccessfully and permanently. Distinct from ❌ BLOCKED, which is
> waiting and resumes when the dependency clears. Terminal: no status follows it, and the task folder
> and its board row are never deleted. This is a task status — not the review verdict ❌ REJECT, and
> not the HL §12 amendment verdict ❌ REJECTED; neither of those is terminal |

**`.tfw/project_config.yaml` and `.tfw/templates/project_config.yaml`:**

```yaml
    - id: REJECTED
      emoji: "❌"
      description: "Closed unsuccessfully, terminal, trace retained"
```

**`.tfw/glossary.md` `## Status Flow`:**

> 9 pipeline statuses: TODO, HL_DRAFT, RES, TS_DRAFT, ONB, RF, REV, KNW, DONE. RES and KNW are
> optional. Two statuses sit outside the pipeline: ❌ BLOCKED — waiting, the task resumes when the
> dependency clears; ❌ REJECTED — closed unsuccessfully, terminal, the trace is kept. `❌ REJECTED`
> here is a **task status** — not the review verdict `❌ REJECT`, and not the HL §12 amendment verdict
> `❌ REJECTED`; neither of those is terminal.

**`.tfw/glossary.md` `### Amendment Log` — one clause appended, nothing else in the article:**

> Its ❌ REJECTED verdict refuses a proposal, not a task — the terminal task status of the same name is
> conventions.md §5.

**`README.md` legend:**

> Statuses: ⬜ TODO → … → ✅ DONE | ❌ BLOCKED (waiting) | ❌ REJECTED (closed unsuccessfully, trace kept)

**`.tfw/conventions.md` §13 — appended after the two existing sentences, which are unchanged:**

> Reverting a result does not revert its trace. A rejected task's folder and its board row are never
> deleted: the work may leave the working tree, the record that the work happened stays.

**`.tfw/conventions.md` §14 — one bullet, from the mechanism, naming no task and no repository:**

> - A whole-tree restore reverts the Task Board past a task's failure status — restoring every file to
>   an older tree also restores rows to a state that never contained the newer ones, so the loss happens
>   silently and nobody decides it

## 2. Key Decisions

1. **The three `REJECT` tokens are named, and the distinction is stated where each lives.** `❌ REJECT`
   is a **review verdict** routing to an owner decision with three branches — Phase A owns it and it is
   byte-untouched. `❌ REJECTED` in `templates/HL.md`:246 is an **amendment verdict**: the owner refused
   a proposal. `❌ REJECTED` in `conventions.md` §5 is the **task status** this phase adds, and it is the
   only one of the three that is terminal. The collision is closed at both ends without editing
   `templates/HL.md`: the task-status side names all three, and the `glossary.md` `### Amendment Log`
   article carries one clause pointing back. A reviewer must not read the new status as a change to the
   review verdict — nothing in the REVISE/REJECT branch moved.

2. **The status is drawn as a side node, not as a branch under `❌ REJECT`** (ONB Q3, Option A).
   Rejection is an owner decision available at any point, not a review outcome — TFW-48 was rejected out
   of `🟡 TS_DRAFT` having never reached a review, which settles it by counterexample from this phase's
   own corpus. Drawing it under the REJECT branch would make the review verdict read as a route to a
   terminal state, which this phase's Definition of Failure forbids.

3. **The TFW-49 verdict is quoted whole, not elided** (ONB R1, approved). The middle the TS's ellipsis
   swallowed is where the owner listed *what* was rejected — the schema, the state, the Python
   validator/router/runtime, the git hooks, the range audit, the installation lifecycle, the
   cross-platform machinery. That list is the substance. The block is byte-identical to `ad0696e`,
   verified by `diff`, not by eye. Recorded as the **stricter reading** of AC-4's own rule, not as a
   deviation from it.

4. **`9e19a4f` is described as the commit that recorded the approval of TFW-49's research — not as a
   contract baseline.** It carries no `freeze` scope word because that grammar is a product of TFW-50 and
   of TFW-53, both later. Applying the term to a July commit would be quiet back-dating, in the phase
   whose subject is honest records.

5. **TFW-48's row says its status was assigned, TFW-49's says nothing because it is a literal
   restoration.** TFW-49's status cell is byte-identical to `5b17786:README.md`:295 — verified by
   comparison, not asserted. TFW-48's cell states *"status **assigned** 2026-08-18, not restored (last
   live status was 🟡 TS (D))"*. In a phase about honest traces, *put back* and *ruled now* cannot look
   the same.

6. **`glossary.md`'s one-line pipeline diagram is left alone; only the count sentence carries the new
   status.** The owner-approved reference wording covered the count sentence, and adding the side node to
   the glossary diagram too would be a second material change to a site the owner already read. AC-1's
   requirement is satisfied — the status is inside `## Status Flow`. Naming it because a reviewer
   scanning the glossary *diagram* alone will not see `REJECTED`, and that is a deliberate boundary, not
   an oversight.

7. **The post-mortem link goes in the last board column, following the TFW-51 precedent.** TFW-51's row
   already puts a non-standard document link (`[Owner-confirmed exception]`) in the trailing column. The
   artifact columns are `—` because those artifacts genuinely are not in the working tree, and a link to
   a file that only exists in git history would be a broken link pretending to be a trace.

8. **`CHANGELOG.md` was touched only under AC-6, and only in `[Unreleased]`.** One hunk, four insertions,
   one deletion. `[1.2.0]`'s sentence *"Phase E is independent and not in this release"* stays true of
   1.2.0 permanently. `VERSION` and `tfw.version` are untouched — the bump belongs to `/tfw-release`.

## 3. Acceptance Criteria

**AC-1 — `❌ REJECTED` exists as a terminal state with a stated boundary**

- [x] Present in all **five** carriers: `conventions.md` §5 (table **and** diagram), `project_config.yaml`, `templates/project_config.yaml`, `glossary.md` `## Status Flow`, README legend
- [x] Terminal — the side node has no outbound edge; `📚 KNW` and `✅ DONE` are unreachable from it
- [x] Drawn as a side node reachable from any status, not under `❌ REJECT`; the REVISE/REJECT branch is byte-unchanged (0 deleted lines in the whole file)
- [x] The BLOCKED/REJECTED boundary is stated in one sentence at every site where the two appear together
- [x] The `"9 statuses"` line updated with the ONB R6 wording, verbatim as approved
- [x] The three-way collision stated at both ends — task-status side names all three; `glossary.md` `### Amendment Log` gains exactly one clause and nothing else. `templates/HL.md` untouched
- [x] Nothing else in the status vocabulary changed; no status renamed, no transition redrawn, `❌ REJECT` untouched. The distinction is stated in §2 decision 1

**AC-2 — The trace survives the revert, as a rule**

- [x] §13 states that reverting a result does not revert its trace, and that a rejected task's folder and board row are never deleted
- [x] §14 carries the whole-tree-restore anti-pattern, written from the mechanism
- [x] Both added, not rewritten — §13's two sentences stand; §14 gains one entry (38 → 39) and no other phase's entry is edited
- [x] General: neither passage names TFW-48, TFW-49 or this repository — verified by search over the added lines, 0 matches

**AC-3 — Two rejected tasks are visible on the board again**

- [x] Both rows between TFW-47 and TFW-50, each `❌ REJECTED` with a link to its task folder
- [x] TFW-48's status is assigned, not restored, and both the row and this RF say so; TFW-49's is a byte-identical restoration
- [x] Each description cell is one line and does not carry the post-mortem
- [x] **Committed.** During execution `README.md` was held by a concurrent session and correctly left unstaged (TS §9, ONB Q2 (b)); the coordinator landed it in `8d9432b`. `git log --oneline -1 -- README.md` confirms, and the rows read at 298 / 299 in the committed tree _(⚠️ discharged 2026-08-18, REVIEW item 5)_

**AC-4 — One post-mortem per task, one page**

- [x] What the task attempted, from the approved HL — two or three sentences in each
- [x] The owner's verdict verbatim: TFW-49's seven-line block **whole**, byte-identical to `ad0696e`; the `bc6779e` sentence byte-identical in both files. Both compared by `diff`, not by eye
- [x] The failure mechanism, stated as a mechanism, in the same words in both files
- [x] The git references, every one re-executed at evidence time; `9e19a4f` described accurately
- [x] What replaced it — TFW-49 → TFW-50; TFW-48 → *"Nothing replaced it. No successor task has been chartered."* TFW-55 appears in neither file
- [x] One page: 544 and 727 words
- [x] Identical section order in both — verified by heading sequence comparison

**AC-5 — Nothing was restored that should have stayed in git**

- [x] Exactly one file per folder — `find … | wc -l` → **2**. No `phase-*/`, no `research/`, no HL, no RF
- [x] `git status` shows no artifact file from `721ca15` re-entering the working tree
- [x] **2 files created against 75 that remain in history**

**AC-6 — The changelog stops saying nothing is pending**

- [x] One `### Added` block under `[Unreleased]`, naming the status, the §13 rule and the §14 anti-pattern
- [x] `[1.2.0]` untouched — no diff line matches `1.2.0`
- [x] `VERSION` and `tfw.version` untouched — no diff in either
- [x] Recorded as a coordinator scope extension (TS AC-6, from ONB R3). Limit honoured: one block, nothing else in the file

## 4. Verification

| Check | Command | Result |
|---|---|---|
| Tests | `python -m pytest docs/scripts/` | **68 passed** in 61.85s. Phase D baseline was 68 passed — same count, no new failures |
| YAML parse, both configs | PyYAML on `project_config.yaml` and `templates/project_config.yaml` | Both parsed OK · **11 statuses** each · order ends `['BLOCKED','REJECTED']` · emoji `U+274C` · no spurious `role` key |
| Additions-only, `conventions.md` | `git diff --numstat .tfw/conventions.md` | **6 insertions, 0 deletions** |
| One hunk, `CHANGELOG.md` | `git diff --numstat` + hunk count | **4 insertions, 1 deletion, 1 hunk** |
| `VERSION` / `tfw.version` / `[1.2.0]` untouched | `git diff` per target | No diff, no matching line |
| `templates/HL.md` untouched | `git status --short .tfw/templates/HL.md` | No output |
| `REJECTED` site census ⟳ | `grep -rn "REJECTED" .tfw/ README.md \| wc -l` | **12 hits** — **9** task status, **3** amendment verdict, **0** new review verdict. Per file: `README.md` 3 · `conventions.md` 2 · `glossary.md` 2 · `templates/HL.md` 2 (pre-existing) · `project_config.yaml` 1 · `templates/project_config.yaml` 1 · `CHANGELOG.md` 1. Full classification in the EV file. _(First pass reported 10 and a 7 / 3 / 0 split, taken before the two board rows existed — REVIEW finding D1a)_ |
| §14 bullet count | `grep -c "^- "` over §14 | **39** (was 38) |
| Framework text stays general | search the added §13/§14 lines for task IDs and self-reference | **0 matches** |
| Verdict quotes | `diff` extracted block vs `git show ad0696e:…` and `git log -1 --format=%B bc6779e` | **IDENTICAL** — TFW-49's seven-line block; the restore sentence in both files |
| Post-mortem length | `wc -w` | 544 · 727 |
| Section-order parity | heading sequence comparison | Identical five headings, same order |
| Link resolution | existence check per relative link | **7 of 7** — 3 in the post-mortems, 4 in the board rows |
| Git references | all six re-executed | 75 · `149 files changed, 798 insertions(+), 27103 deletions(-)` · both pre-restore status cells · `ad0696e` · `9e19a4f` |
| File count | `find tasks/TFW-48__* tasks/TFW-49__* -type f \| wc -l` | **2** |

No lint or build command is configured for Markdown in this project; `docs/scripts/` is the only
executable gate, and it passes unchanged.

## 5. Evidence

See [EV file](evidence/EV__phase-e__rejected_trace_restoration.md) for evidence details.

Evidence verdict: **27/27 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**

At first collection this read 26/27 with one DEFERRED — E27, the board rows, which existed and were read
but were not yet committed. The coordinator landed them in `8d9432b`, so the blocker cleared. E27 records
both states rather than overwriting the first, and the EV file carries the correction note for this pass.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/conventions.md` | 324–325 | style | **The §5 diagram has a loose edge that predates this phase.** The `↓` above `❌ BLOCKED` sits under the *skip* annotation with no source node, so the diagram does not say what transitions into `BLOCKED`. Left untouched deliberately: repairing it means **deciding** what transitions into BLOCKED, which is a decision and a bonus fix, not a tidy-up. The coordinator agreed at the ONB gate and asked for a debt row. Related to TD-175, which measures `BLOCKED` at 0 uses across 46 board rows — the two are the same question from opposite ends |
| 2 | `.tfw/conventions.md` | 42–191 (§3) | naming | **`POSTMORTEM` is now a shipped file class that §3's artifact-type list does not name.** §4's filename rule is satisfied (the task ID is present), but §3 enumerates HL, RES, TS, RF, ONB and REVIEW and nothing else. The file itself is authorised by frozen HL §4 Phase E deliverable 4, so nothing was smuggled in; what is missing is the type entry, and §3 is **Phase A's section**. Without it, the next rejected task invents a second name for the same thing |
| 3 | `README.md` | 249 vs 297–299 | style | **The Task Board's header declares 8 columns while its rows carry 7, 8 or 9.** The header is `ID \| Task \| Status \| HL \| TS \| ONB \| RF \| REV`; every row from TFW-42 onward carries a ninth cell for RES, TFW-50's carries 8, TFW-51's carries 7. Pre-existing and untouched — the two new rows match their neighbours at 9 cells rather than the header. A renderer that trusts the header truncates the newest rows |

## 7. Fact Candidates
> fact-candidates: processed 2026-08-18 (`/tfw-knowledge`, TFW-53 A–E)


**No fact candidates.**

The owner's contribution to this phase — the vocabulary challenge at the ONB gate, the ruling to keep
`REJECTED` and close the collision in two clauses — was already captured by the coordinator in HL §11
S39 and TD-175 before execution began. Nothing new from a human reached the executor during execution:
the session's human input was the handoff instruction and the direction to proceed. Recording an
agent-derived observation here would fail the Human-Only Test.

> **Which side of TD-174 this applies.** `templates/RF.md` §7 contradicts itself — its Scope line admits
> *"agent-observed project patterns"* while its Human-Only Test four lines below bars anything an agent
> can discover. TD-174 records that four consecutive reviews approved work on each side. This RF applies
> the **Human-Only Test**, the stricter reading, and says so rather than leaving the reviewer to guess.

## 8. Strategic Insights (Execution)

**No strategic insights.**

Same reasoning as §7 and the same Human-Only Test. No human supplied domain knowledge, correction or
strategic context during execution — the owner's ruling arrived before it, through the coordinator, and
is already recorded in HL §11 S39. The one thing this phase learned that is worth carrying forward is
agent-derived and therefore belongs in §6, where observation 2 records it.

One item is flagged rather than filed, because the coordinator asked for it in the RF verbatim:
**recreating the folder names gives a future whole-tree operation a live directory to restore into, so
the deliverable slightly enlarges the surface of the failure it describes.** `tasks/TFW-48__…/` and
`tasks/TFW-49__…/` now exist again, holding one file each, and 75 files in history match those prefixes.
The §14 anti-pattern is the mitigation, and it is the only one available — the alternative is not
restoring visibility at all.

## 9. Diagrams

**The one carrier whose shape changed — `conventions.md` §5, before and after.**

```
BEFORE — the status set could not express failure

⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE
                                                                              │
                                                                    ┌─────────┴─────────┐
                                                                    🔄 REVISE          ❌ REJECT
                                                                 (back to dev)    (user decides)
                    (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)        ↓
                                                           ❌ BLOCKED

  a failed task had three exits, all of them dishonest:
    ✅ DONE      → a lie
    ❌ BLOCKED   → a pretence; blocked means waiting
    delete it    → what actually happened at bc6779e


AFTER — one honest exit, added and nothing else moved

⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE
                                                                              │
                                                                    ┌─────────┴─────────┐
                                                                    🔄 REVISE          ❌ REJECT   ← untouched:
                                                                 (back to dev)    (user decides)     a review verdict,
                    (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)        ↓                                     not terminal
                                                           ❌ BLOCKED

  from any status ──→ ❌ REJECTED     terminal · no edge leads out · the trace is kept
                          ↑
                    reachable from anywhere, because rejection is an owner decision,
                    not a review outcome — TFW-48 was rejected out of 🟡 TS_DRAFT
```

**The three tokens that share a glyph, and which one is terminal.**

```
❌ REJECT          review verdict     conventions.md §5      → owner decides: (a) HL_DRAFT (b) RES (c) TS_DRAFT
                                                              NOT terminal — three ways out

❌ REJECTED        amendment verdict  templates/HL.md §12    → this proposal was refused; the task continues
                                                              NOT terminal — the work goes on under the
                                                              original contract
                                      ↕ cross-referenced in glossary.md ### Amendment Log

❌ REJECTED        task status        conventions.md §5      → the task is closed unsuccessfully
   ← NEW                                                      TERMINAL — no status follows, and the folder
                                                              and board row are never deleted
```

**What the failure mechanism looked like, since both post-mortems state it and it is the sentence
TFW-53 answers.**

```
  owner approves HL ──┬──→ blanket delegation granted at approval time
                      │
                      ↓
              research produces a scope-expanding signal
                      ↓
       the same coordinator amends the approved HL to absorb it
                      ↓
              phase TSs derive from the amended HL
                      ↓
            reviewers verify each RF against those TSs          ← 7 verdicts, 6 ✅ APPROVE
                      ↓
              ╔═══════════════════════════════════════════╗
              ║  nothing in the chain ever compares the   ║
              ║  result to what the owner approved        ║
              ╚═══════════════════════════════════════════╝
                      ↓
              wholesale rejection · bc6779e · 27,103 deletions
```

---

*RF — TFW-53 / Phase E: Rejected-Task Trace Restoration | 2026-08-18*
