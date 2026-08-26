# RF — TFW-60 / Phase A: Task State & Coordination

> **Date**: 2026-08-26
> **Author**: Claude Code (Executor), acting for `saubakirov`
> **Status**: 🟢 RF — corrective pass complete
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md) · [HL — Phase A](HL__phase-a__task_state_and_coordination.md)
> **TS**: [TS — Phase A](TS__phase-a__task_state_and_coordination.md) — **revision 4, approved**
> **REVIEW**: [rev 2](REVIEW__phase-a__task_state_and_coordination__rev2.md) — 🔄 REVISE, 7 items · [first pass](REVIEW__phase-a__task_state_and_coordination.md) — ❌ REJECT, 15 findings
> **Revision 2** — 2026-08-27. Second corrective pass, closing AC-13. Every contested figure regenerated and persisted in [`evidence/measurement_log.txt`](evidence/measurement_log.txt)
> **ONB**: [ONB — Phase A](ONB__phase-a__task_state_and_coordination.md) — 12 questions, all answered
> **Baseline for every measurement**: `80d6a16`
> **Supersedes**: the first-pass RF (retained at `b606303`). This is a corrective pass, not a re-run.

---

## 1. What Was Done

The rejected pass had the right shape and three defects that made it unreleasable: an
identifier that promised a uniqueness its grammar could not deliver, an event filename that
lost one of two concurrent writes, and a build gate that pushed every task transition back
into the shared file this phase exists to remove. Underneath those sat a quieter failure —
the board snapshot shipped empty, and the review certified it.

This pass fixes all fifteen findings, executes the two criteria the owner added after the
review, and closes every countable claim on a printed count.

### The four that mattered most

**The destroyed trace, restored.** `tasks/BOARD-SNAPSHOT.md` shipped reading
`Rows captured | 0` against a 61-row board and contained `TFW-` zero times. Eight
identifiers — **TFW-16, TFW-20, TFW-28, TFW-33, TFW-34, TFW-35, TFW-37, TFW-39** — were
board-only rows whose *only* carrier was that snapshot, so emptying it erased them entirely.

*Root cause.* After the board was removed from `README.md`, the migration was re-run to
regenerate the snapshot. `parse_board()` read the live README, found no table, returned zero
rows, wrote an empty snapshot over the correct one — and **reported success**.

*Fix, structural rather than a re-run.* The board source is now an explicit argument
(`--board-rev`), and a run yielding zero rows is **refused** with the remedy printed. The
snapshot is regenerated from `b094943`, the last commit that held the board, and verified by
count against `git show b094943:README.md`: **61 = 61**. All 61 identifiers are now named
individually in the accounting, with `Unaccounted: 0`.

**The identifier (F1).** The identifier is now the **whole directory name**,
`YYYYMMDD-HHMMSS__slug`; a bare timestamp is refused by the resolver as ambiguous. Two
mutually offline participants reaching the same second no longer collide, because the slug
tells them apart. Reaching the same second *and* the same slug means they created the same
task — surfaced, not prevented. The create-or-retry algorithm, its bound and its visible
failure now live in `plan.md`: the shipped workflow, not a harness.

**The event filename (F3).** `<YYYYMMDD-HHMMSS>__<kind>__<actor>.md`. The actor is in the
name because it is the only field separating two concurrent writers: `on_behalf_of` names the
same accountable person for both, and `via` names the same provider for two sessions of one
tool. One actor writing twice in a second takes the next actual second — never a counter,
because a counter is the shared state this model removes.

**The shared-write regression (F15).** The rejected pass shipped a test asserting the
committed index always matches the generator, and made it the `build.verify` command. That
one assertion undid the phase: advancing any task failed the gate until somebody rewrote
`workspace/00-INDEX.md`. The test is gone, replaced by two asserting the opposite, and
`build.verify` is now `gen_index.py --validate`, which reads each task's own state and is
unaffected by whether the aggregate is current.

### New Files — 30

| File | Description |
|------|------------|
| `.tfw/templates/status.md` | Task state carrier. Closed key set of 11, bounded fields, no free-text body, second-resolution stamps |
| `.tfw/templates/journal_event.md` | One event. Actor-bearing filename, closed `kind` vocabulary, three identity fields, measured ceiling |
| `.tfw/templates/team_profile.md` | Participant profile. Humans only in 2.0.0; the `agent` slot stays declared and empty |
| `docs/scripts/gen_index.py` | Index generation, and the **shared resolver** the others import — identifier, sort key, containers, discovery, status schema, journal schema, phase state |
| `docs/scripts/test_gen_index.py` | 73 tests: resolver, discovery, full schema, journal, phase state, determinism, degraded states |
| `docs/scripts/migrate_board.py` | Accounting migration. Explicit board source, zero-row refusal, no repository or date literals |
| `docs/scripts/test_migrate_board.py` | 36 tests, weighted to the negative guarantees and to the empty-board defect |
| `tasks/README.md` | Why a second container exists, with the measured reason for not renaming |
| `tasks/BOARD-SNAPSHOT.md` | All 61 board rows, verbatim |
| `team/README.md`, `team/saubakirov.md` | The participant model and the one profile that ships |
| `workspace/00-INDEX.md` | The generated portfolio view, now carrying phase rows |
| 11 × `{task}/status.md` | Live state for the 11 non-terminal legacy tasks |
| `{TFW-60}/phase-a/status.md` | **AC-12** — the one phase state file the whole corpus needs |
| 6 × `{TFW-60}/journal/*.md` | This phase's own events, each from a shown clock read |

### Modified Files — 47

| Group | Files | Changes |
|------|---:|---------|
| Canonical rules | 4 | §4 rewritten: container list, whole-name identifier, the collision rule stated operationally, event grammar, three identity fields, phase state. §5 gains `PHASES` |
| Configuration | 2 | `task_containers`, identifier grammar, `id_max_retries`, journal ceiling, `PHASES`, real `build.*`, version `2.0.0` |
| Lifecycle workflows | 8 | Task state instead of the board; the creation algorithm; a *Who Is Acting* block in all six that write durably |
| Templates | 13 | `{ID}` placeholders; second precision; `PHASES` |
| Adapter originals | 10 | Same rules at source; all 38 propagated copies resynced |
| Documentation generator | 3 | Board parser gone; container- and year-aware resolution; 10 resolution tests folded into `test_gen_docs.py` |
| Release surface | 4 | `2.0.0`, CHANGELOG, Quick Start, README route |
| Root entry points | 3 | Context loading and the release checklist |

### Census against the ruling — the tripwire fired, and is raised

| | Configured | Ruled (S42 / S44) | **Delivered** | Δ |
|---|---:|---:|---:|---:|
| Modified files | 30 | 45 | **47** | +2 |
| New files | 15 | 23 | **30** | +7 |
| **Files total** | 30 | 68 | **77** | **+9** |

**TS §7:** *"The census exceeding roughly 75 files total … without returning to the
coordinator."* It does. Every file of the excess is named in
[`evidence/census.md`](evidence/census.md) §1, and none of it is scope creep:

| The +9 | Why |
|---|---|
| 6 journal events | The phase ships a journal as a named deliverable and its own task had none |
| 1 `phase-a/status.md` | **AC-12 requires it.** Measured: the only one the whole corpus needs |
| 1 `.tfw/quickstart.md` | AC-10 requires Quick Start to describe the shipped model; §4 omitted the file |
| 1 `test_gen_docs.py` | F13 demanded docs-resolution coverage. Folded into the **existing** test file rather than adding a fifth script, so the declared create list keeps its shape |

**Not trimmed to reach 68.** Meeting the number would mean deleting TFW-60's own journal,
dropping the phase state AC-12 mandates, or leaving Quick Start describing a removed
mechanism. S44 forbids meeting the count by delivering less. **The numbers above are what a
revised ruling would be given against.**

### Second corrective pass — what review revision 2 returned, and what closed it

The verdict moved `REJECT → REVISE`: the purpose failure is closed, migration is lossless,
and contradicted evidence fell from 12-of-44 to 5-of-59. AC-13 carried what remained.

| # | Finding | What was wrong | What closed it |
|---|---|---|---|
| 1 | `event_filename` composed a second | It took a stamp as a parameter and produced successors by **arithmetic** — a number somebody allocated, which its own docstring forbade. At `23:59:59` it wrapped the time while keeping *yesterday's* date, producing an event claiming to precede the one it follows | Every candidate is now a **fresh reading of the clock**, with a wait between readings because only time passing makes the next one differ. Bounded; on exhaustion it fails visibly. A controllable clock records what it was asked for, so a test can prove the returned stamp was read and not computed |
| 2 | A provider could be an actor | The test only proved a *mismatch* between filename and body was caught. `actor: claude` stated consistently in both places passed — the likelier mistake, because it looks tidy | A provider family is refused wherever it appears, and an actor must additionally resolve to a declared `team/` handle. Legacy events keep their bytes: the rule postdates them |
| 3 | `id_format` contradicted AC-2 | Both configs read `{YYYYMMDD}-{HHMMSS}` — the bare stamp the resolver refuses as ambiguous | Both now read `{YYYYMMDD}-{HHMMSS}__{slug}`, and the comment says why the timestamp alone is not an identifier |
| 4 | The Windows binding path was corrupt | The backslash-t and backslash-b in the Windows path were interpreted as escapes and written as a **TAB** and a **BACKSPACE**, in 6 canonical files and 12 adapter copies. Every agent was sent to a path that cannot exist | The literal `%LOCALAPPDATA%\\tfw\\bindings.yaml` restored in all six, both adapter sets re-copied, and 0 control characters remain in 116 shipped text files |
| 5 | Evidence figures were stale or wrong | Five contradicted, five partial | Every one regenerated from a command and persisted in `measurement_log.txt` |
| 6 | No current handoff event | The live trace did not identify which RF went to review | A `handoff` event written from a clock read, with the read shown either side of the call. The first-pass event is preserved unchanged |
| 7 | *(coordinator)* Test the class, not the string | A regression test on one path leaves the next Windows path free to break identically | One assertion: **no shipped text carries a control character** outside tab, newline and CR. Binaries excluded by extension |
| 8 | *(coordinator)* Prove the gate can fail | `grep -P` aborts here with a locale error and **exits without output** — indistinguishable from a clean scan. The coordinator's own first scan came back empty for this reason | The gate is Python, not a shell pipeline, and its first act is to fail on a deliberately corrupted fixture. `control_char_gate.txt` shows the failure before the pass |

**Item 7 vindicated itself immediately.** While writing this RF's own evidence I reintroduced
the exact defect into the EV — two BACKSPACE bytes, from the same escape trap. The class scan
caught it. Worth recording: the scan did **not** flag the accompanying TAB, because a tab is
legal in text, which is precisely why the literal-path assertion is kept *alongside* the class
check rather than replaced by it. Neither alone is sufficient.

**Declined, per the coordinator.** Review item 7 asked for an ONB revision fixing three
citation applications. 34 of 34 citations resolve and 31 of 34 applications are sound; the ONB
records what the executor understood at onboarding, and amending a past understanding to read
better edits a trace for appearance. Recorded here instead — see Observation 12.

## 2. Key Decisions

1. **The identifier is the whole directory name.** Revision 2 made it the timestamp and then
   demanded offline uniqueness of it — two clauses that could not both hold. Including the
   slug makes the promise satisfiable and reframes the residual case honestly.

2. **A bare timestamp is rejected, not tolerated.** `parse_identifier("20260826-143000")`
   returns `None` on purpose. A value that can name two tasks must not be accepted as if it
   named one, and the resolver enforces that once for every consumer.

3. **The actor is in the event filename, and the fallback is the clock, not a counter.** A
   counter would reintroduce shared state into the one place this phase made contention-free.

4. **Legacy events are described, never rewritten.** Six events predate the grammar. The
   journal is immutable, so the validator recognises the old shape and reports it as legacy —
   the same treatment legacy task identifiers get. The withdrawal of the agent profiles is a
   **new** `ownership_changed` event; three prior events keep their bytes.

5. **`UNDECLARED` and `PHASES` are opposite kinds of vocabulary.** `UNDECLARED` is never
   selectable and lets a migration carry a foreign value without normalizing it. `PHASES` is
   selectable and says only that phases are running — it never summarizes them, because a
   rollup is a second fact that has to agree with the phase files.

6. **Second precision, and an honest zero.** Git knows the exact second a directory first
   appeared, so migrated `created` values are real. Where a source held only a day, the zero
   time is **declared**, and this RF says so rather than implying second-accurate history.

7. **The migration refuses by default and skips only when told.** `--skip-existing` was added
   rather than weakening the no-overwrite guarantee: a live task's state is its own, and a
   migration must not reach back into it.

8. **`--validate` is the build gate, not `--check`.** One reads task-local truth; the other
   asks whether a shared aggregate is current. Only the first can be a gate without
   recreating the bottleneck.

9. **Authority prefers what a clean clone will have.** TFW-54's state pointed at an HL that
   existed on one machine. `find_authority` now ranks by preference **among files Git
   carries**, falling back to the filesystem only when Git cannot answer.

10. **The docs-resolution tests went into the existing test file.** A fifth script file would
    have changed the shape of a group the TS declared. Placement, not trimming — the coverage
    is identical.

## 3. Acceptance Criteria

**AC-1 — container, year nesting, stable paths** — [x] all five. Path set identical across
`TODO → ONB → BLOCKED → RF → DONE → REJECTED`; a December task updated in March stays in
2026; two container values resolve differently.

**AC-2 — identifiers need no project-wide read**
- [x] **R3** — the identifier is the whole directory name; a bare stamp is refused
- [x] every reference, commit subject and index row carries the full identifier
- [x] creation reads no counter and no other task directory
- [x] two mutually offline participants in the same second do not collide
- [x] a genuine collision takes a new actual timestamp, never reuse or overwrite
- [x] the retry is bounded and fails visibly
- [x] both grammars readable through one resolver

**AC-3 — immutable journal with a measured ceiling**
- [x] **R3** — `<stamp>__<kind>__<actor>.md`; same second + same kind + two actors → two files
- [x] **R3** — name taken → next actual second
- [x] **R3** — the timestamp is read from the clock; **every read in this pass is shown in the EV**
- [x] **R3** — three identity fields; an event without `on_behalf_of` is refused
- [x] **R3** — a provider name is never an actor
- [x] closed vocabulary; a correction is a new event; ceiling 120 with the measurement recorded
- [x] no event body copies artifact or chat text

**AC-4 — participants declared in `team/`**
- [x] **R3** — humans only; `claude-code.md` and `codex.md` deleted
- [x] **R3** — the schema still admits `type: agent`; no agent profile ships
- [x] **R3** — a profile authorizes nothing
- [x] **R3** — existing events not rewritten; one `ownership_changed` event appended
- [x] four resolution cases; resolution now inside the shipped workflows (F4)
- [x] no binding or private preferences on the shared tree; identity never inferred from the OS
- [ ] **readability by a non-specialist — DESIGN INTENT, NOT OBSERVED.** TFW-61 owns it (S43)

**AC-5 — derived, never authoritative** — [x] all items, plus the F15 correction: a normal
transition touches one file, the index is then stale, and staleness is visible rather than
forbidden.

**AC-6 — exact accounting, corpus byte-identical**
- [x] dry run against a committed manifest before any write
- [x] **R3** — snapshot row count produced by a command and compared side by side: **61 = 61**
- [x] **R3** — all 61 identifiers resolve and are named; `Unaccounted: 0`
- [x] **R3** — the eight lost identifiers named individually, with where each lands
- [x] zero renames, zero moves, zero byte changes; nothing invented; verbatim values carried
- [x] all 61 rows captured before removal

**AC-7 — references and history keep resolving** — [x] the failure set did not grow; commit
subjects resolve; `TFW-37` was already unresolvable at baseline. Equal-depth clause deleted by
R3, so nothing to execute.

**AC-8 — the board is gone and nothing reads it** — [x] all items; the reintroduction test
fired once and caught a real leftover.

**AC-9 — no component required** — [x] a full lifecycle by ordinary file writes; executable
code is exactly three scripts.

**AC-10 — the release describes what shipped** — [x] `2.0.0`; CHANGELOG carries the breaking
change, the migration path and the container as one setting; TD-81/TD-177 retired by code and
test, with the registry edit handed to `/tfw-docs` under D37.

**AC-11 — the rejected pass corrected** — F4 ✅ · F6 ✅ · F7 ✅ · F8 ✅ · F9 ✅ · F10 ✅ ·
F12 ✅ · F13 ✅ · F14 ✅ · F5 transferred to TFW-61 by R3.

**AC-12 — second precision and phase state** — [x] all items. Two phases under two owners
write two files and never touch the task's; the task lifecycle never summarizes them; the
index renders phase rows beneath their task; `PHASES` added and propagated; **migration
created phase state for no legacy task**, confirmed in the census rather than assumed.

**62 of 63 criteria met.** The single open item is AC-4's non-specialist readability, which
the TS itself requires be stated as intent rather than claimed.

## 4. Verification

- **Tests** — `python -m pytest docs/scripts/`: **206 passed, 1 skipped**. Baseline 68; 138
  added. The skip is by design once the board is gone.
- **Verify** — `python docs/scripts/gen_index.py --validate`: **53 tasks validate**.
- **Fixtures** — 43 checks across AC-1, 2, 3, 4, 5, 9 and 12: **43 passed, 0 failed**.
- **Snapshot gate** — 61 = 61 against `git show b094943:README.md`.
- **Accounting** — 61 distinct identifiers, `Unaccounted: 0`. Three counts of the same file
  are all correct and answer different questions: 122 lines contain `TFW-`, 678 occurrences,
  **61 distinct identifiers** — and the third is the one that closes AC-6.
- **Control characters** — 0 in 116 shipped text files, on a gate shown failing first.
- **Corpus integrity** — 40 additions and 4 modifications over `tasks/`; **all four are
  coordinator artifacts of live tasks**, each attributed in `measurement_log.txt` §E35. The
  migration changed no pre-existing artifact. The earlier "additions only" claim was false.
- **Docs build** — the MkDocs build runs inside `test_integration.py` and passes.

Build gate ran before this RF was written, and passed.

## 5. Evidence

See [EV file](evidence/EV__phase-a__task_state_and_coordination.md).

Evidence verdict: **56/59 VERIFIED, 1 DEFERRED, 0 BLOCKED, 2 N/A** — with the ten rows the
review contested regenerated from commands rather than restated.

Every AC in the TS carries `Evidence: N/A`, **and that is not coverage.** Three things are
not claimed anywhere in this phase: non-specialist readability (deferred, blocker named), any
transport behaviour, and any cross-machine concurrency — the evidence is two threads and two
processes on one machine.

## 6. Observations (out-of-scope, not modified)

| # | File | Type | Description |
|---|------|------|-------------|
| 1 | `KNOWLEDGE.md` D66 | `todo` | Calls the README *"the only Task Board"*. False at `2.0.0`. **`/tfw-docs` handoff** — D37 territory |
| 2 | `KNOWLEDGE.md` D65 | `todo` | Records `❌ REJECTED` as living in five carriers, one being the README legend. The legend moved to `glossary.md`; the count is four. **`/tfw-docs` handoff** |
| 3 | `knowledge/convention.md` F22 | `todo` | A verified fact about board updates whose subject no longer exists. **`/tfw-knowledge` handoff** |
| 4 | `TECH_DEBT.md` TD-81, TD-177 | `todo` | Retired by the code change and the reintroduction test; the rows still read open. **`/tfw-docs` handoff** — AC-10 assigns closure there |
| 5 | `editions/02-assisted/AGENTS.md:71` | `security` | A shipped edition changes status by **moving the task folder**, which master HL P4 and DoF 3 prohibit. Not edited: v1.0 against a shipped v1.4. Reviewer raised it as TD-182 |
| 6 | `tasks/TFW-36__…/.gitignore` | `todo` | `*` hides the whole task from Git. Its `status.md` is force-added so eleven ship, but the folder's other contents reach no clone, and the index is reproducible from a working tree and not from a fresh one. TD-183 |
| 7 | `tasks/TFW-45__…/status.md` | `todo` | `❄️ FROZEN` carried verbatim as `UNDECLARED`. Whether `FROZEN` should join the vocabulary is a separate owner ruling. TD-184 |
| 8 | `tasks/TFW-4__…/status.md` | `todo` | `🟡 TS` is the pre-rename label of `TS_DRAFT`; carried verbatim. Someone with the history can set it deliberately — a migration may not |
| 9 | migrated `status.md` files | `todo` | `value: unrecorded` and `owner: unassigned` are honest placeholders, not data. Nothing prompts anyone to fill them |
| 10 | `.tfw/workflows/update.md` | `todo` | Now genuinely changed (the `initial_seq` residue), correcting the first-pass claim that it needed no edit |
| 11 | `docs/scripts/gen_docs.py` | `duplication` | `_glob_sources(root)` re-reads config twice per build. Harmless at this scale |
| 12 | `ONB__phase-a__…md` rows 1, 2, 12 | `todo` | Review rev 2 item 7 found three citation *applications* that do not follow the clauses they cite (resumability, task-locality, D37), though all 34 citations resolve. The coordinator declined an ONB revision: the ONB records what was understood at onboarding, and amending it to read better edits a trace for appearance. Recorded here so the next citation pass has the list |

### Process failures in this task, reported rather than buried

**First pass — broad staging.** `git add -A tasks/` swept ~90 uncommitted files of TFW-55's
research and TFW-54's draft HL into a Phase A commit. Detected during the corpus diff and
backed out in `e2bec00`. The reviewer recorded it as a second instance of TD-144 — inside the
task built to prevent exactly that.

*This pass:* every commit staged by explicit path, with the staged set diffed against the
intended set before committing. TFW-54's and TFW-55's uncommitted work sat untouched in the
working tree from start to finish, as did `TECH_DEBT.md`, which the reviewer had modified.

**First pass — a typed timestamp.** One event shipped stamped `23:20:00`: round seconds,
dated after the review that consumed it. *This pass:* every time value was read from the clock
and the read printed into evidence; the seconds are `47`, `29`, `27`.

## 7. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | `philosophy` | A countable claim closes on a count printed into evidence, never on a sentence. The rejected pass asserted 61 rows were retained while the snapshot held zero, and a full review accepted the sentence | Coordinator message 2026-08-26; TS R3 AC-6 | High |
| 2 | `stakeholder` | The owner treats a budget overrun as a direction, not a caveat: the overrun exists so the scope ships whole, and hitting the number by delivering less inverts the ruling. Coming back is the response to needing more | ONB Q2 (S44), restated 2026-08-26 | High |
| 3 | `philosophy` | A specification clause that cannot be satisfied is a specification defect, not an execution failure. Three R3 changes are the coordinator withdrawing its own contradictory clauses rather than demanding a better attempt | TS revision 3 header | High |
| 4 | `constraint` | A rule that lives only in a test harness is not a shipped rule. The review rejected participant resolution on exactly that basis, even though the behaviour was demonstrably correct | REVIEW F4 | High |
| 5 | `convention` | Time is recorded to the second and read from the clock. A day-resolution stamp on a corpus taking several transitions a day makes `created` and `updated` identical and stops answering its question | TS R3 AC-12 | High |
| 6 | `philosophy` | A provider family is not an actor. Two sessions of one tool are two writers, and accountability always resolves to a human — which is why 2.0.0 ships no agent profile at all | TS R3 AC-4 | High |
| 7 | `risk` | A generated artifact whose input silently disappears fails without any error. The migration reported success while writing an empty snapshot over a correct one | this RF §1 | High |

## 8. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | The owner added AC-12 **after** the review, reasoning that a change rippling through configuration, every workflow, every template and every adapter should ride a sweep already happening rather than pay for its own later. Implication: the cost of a vocabulary change is dominated by propagation, not by the change itself, so a phase already rewriting the tree is the cheapest moment a project will get — and deferring it is the expensive option, not the safe one | `process` | User, TS R3 AC-12 rationale |
| S2 | The owner refused a task-level rollup of phase state on principle, quoting the carrier's own rule back: two files that must agree is the synchronization problem that previously required an engine. Implication: convenience fields summarizing other files are treated here as design defects however useful they look, and a reviewer should read any derived-and-stored value as a claim needing justification | `philosophy` | User, TS R3 AC-12 |
| S3 | The review's most damaging finding was not a bug but a **test** — an assertion that the shared index is always current, which silently made every task transition a shared write and undid the phase's purpose while the suite stayed green. Implication: a green gate can encode the opposite of the contract, so a Purpose Check must read what the gates *force*, not only what the code does | `process` | Reviewer F15, ruled `not fit for purpose` |
| S4 | The owner's instruction was explicit that this is a corrective pass and **not to start from the RF** — the REVIEW and the R3 clause changes are the input. Implication: after a rejection the previous result artifact is the least reliable document in the folder, because it is the one that asserted the work was done | `process` | User, coordinator message 2026-08-26 |

## 9. Diagrams

**What the identifier is, and why the change mattered**

```text
REVISION 2 — rejected                     REVISION 3 — shipped
────────────────────────                  ────────────────────────
identifier = 20260826-143000              identifier = 20260826-143000__query_redesign
directory  = <identifier>__<slug>         directory  = <identifier>

  Alice (offline)   20260826-143000__auth        20260826-143000__auth
  Bob   (offline)   20260826-143000__cache       20260826-143000__cache
                    ▲                            ▲
                    ONE identifier,              TWO identifiers.
                    two directories.             Nothing to resolve.
                    UNSATISFIABLE.

  Same second AND same slug -> one name -> they created the same task.
  A signal, surfaced. Not a collision to prevent.
```

**How two concurrent writers stopped losing an event**

```text
REVISION 2                                 REVISION 3
<stamp>__<kind>.md                         <stamp>__<kind>__<actor>.md

 14:00:00 handoff (coordinator) ─┐          14:00:00__handoff__saubakirov.md
 14:00:00 handoff (reviewer)   ──┴─► ONE    14:00:00__handoff__reviewer.md
                                   FILE
                             one write      two files. Both survive.
                             silently lost

 The old fixture proved concurrency with two DIFFERENT kinds — which cannot
 collide by construction. It tested the case that was already safe.
```

**The finding that rejected the phase**

```text
BEFORE (rejected)                          AFTER
─────────────────                          ─────
 advance any task                           advance any task
        │                                          │
        ▼                                          ▼
 status.md changes                          status.md changes
        │                                          │
        ▼                                          └── done. One file.
 gen_index --check FAILS
        │                                    the index is now stale — which
        ▼                                    is CORRECT, and visible when
 must rewrite workspace/00-INDEX.md          asked.
        │
        ▼                                    build.verify = --validate,
 ← the shared write, returned                which reads each task's own state.
```

**Where state lives now, phases included**

```text
workspace/00-INDEX.md          derived · rebuilt deliberately · never authoritative
      │
      ▼
workspace/<year>/<stamp>__<slug>/
  ├── status.md          the task's own arc:  TODO → HL_DRAFT → RES → 🧩 PHASES → KNW → DONE
  │                      it NEVER summarizes the phases below
  ├── journal/           <stamp>__<kind>__<actor>.md, immutable once written
  ├── phase-a/status.md  ◄─ owner A writes only this
  ├── phase-b/status.md  ◄─ owner B writes only this
  └── phase-c/status.md

  Two owners advancing two phases touch two files, and neither touches the task's.
```

**The three identity questions, answered separately**

```text
   actor          who performed it      a team/ handle
   on_behalf_of   who is accountable    ALWAYS a human. Refused if absent.
   via            what produced it      claude · codex · gemini

   `via: claude` is not an actor: two Claude sessions are two writers.
   2.0.0 ships no agent profile at all — one accountable participant, the owner.
```

---

*RF — TFW-60 / Phase A: Task State & Coordination | 2026-08-26*
