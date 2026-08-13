# RF — TFW-56: Remove the Review Mode Axis

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-56](HL-TFW-56__review_mode_removal.md) — 🔒 FROZEN, re-frozen 2026-08-13 after A1–A5, A7
> **TS**: [TS TFW-56](TS__TFW-56__review_mode_removal.md)
> **ONB**: [ONB TFW-56](ONB__TFW-56__review_mode_removal.md) — one blocking question, answered `1.1.0`
> **Evidence**: [EV TFW-56](evidence/EV__TFW-56__review_mode_removal.md) — 9/16 VERIFIED, 0 DEFERRED, 0 BLOCKED, 7 N/A

---

## 1. What Was Done

### New Files

| File | Description |
|------|------------|
| `tasks/TFW-56__review_mode_removal/evidence/EV__TFW-56__review_mode_removal.md` | Mandatory evidence artifact — 16 rows, the recorded grep gate, both config excerpts, the six-adapter parity check, the S1-vs-U7 dry-run, and the diffstat anomaly |

**Zero framework files created**, as DoF and AC-12 require.

### Deleted Files

| File | Lines |
|------|------|
| `.tfw/workflows/review/code.md` | 15 |
| `.tfw/workflows/review/docs.md` | 12 |
| `.tfw/workflows/review/spec.md` | 12 |

The folder itself is gone, not emptied (DoF-7). ⚠️ These three deletions were committed by a
concurrent session — see §2 decision 7 and §6 observation 1.

### Modified Files

| File | Changes |
|------|---------|
| `.tfw/workflows/review.md` | Step 1 (mode selection + 🛑 WAIT) removed; the mode-file load removed from Verify and replaced with a statement that every `verify.md` action is unconditional and depth is set by `min_verify_ratio`; Steps 2-8 renumbered 1-7, so Step 0 is Session Naming for the first time |
| `.tfw/templates/review/judge.md` | `Mode:` field and Mode-Specific Checklist section removed; universal checklist 7 → **10** rows; U2 split into two separately answered clauses, (a) mapping integrity and (b) **design soundness** (4.5%); **S1 evidence sufficiency** (16.1%), **S2 backward compatibility** (8.5%), **S4 safety** (4.0%) added, each carrying its measured rate; status vocabulary `✅/❌/⚪`; a rows-7-vs-8 contrast note; two new Checkpoint items |
| `.tfw/templates/review/verify.md` | `Mode:` field removed; new **Claim & Source Checks** section carrying the three orphaned `docs`/`spec` verify actions as unconditional, with a table and a Checkpoint item |
| `.tfw/templates/review/map.md` | `Mode:` field removed |
| `.tfw/templates/REVIEW.md` | `Review Mode` header field and the mode-specific placeholder comment removed; §3 Judge table realigned to ten rows matching `judge.md` one-for-one and in order; `⚪` added to the status vocabulary |
| `.tfw/project_config.yaml` | `tfw.review.default_mode` removed; `tfw.version` `1.0.0` → `1.1.0` |
| `.tfw/templates/project_config.yaml` | `tfw.review.default_mode` removed |
| `.tfw/workflows/config.md` | `review.default_mode` propagation row removed |
| `.tfw/conventions.md` | §14 anti-pattern added: a review checklist row added without an evidenced firing rate |
| `.tfw/glossary.md` | Reviewer heading → "coordinator under the reviewer Role Lock"; entry describes one universal 10-row checklist with explicit `⚪ N/A` instead of a "mode-aware checklist (6 universal + mode-specific)"; Principles Check pointer `review.md` Step 4 → Step 3 |
| `.tfw/VERSION` | `1.0.0` → `1.1.0` |
| `.tfw/CHANGELOG.md` | New `## [1.1.0] — 2026-08-13` entry. `### Removed` names `tfw.review.default_mode` by name with upgrade instructions |
| `.claude/commands/tfw-review.md` · `.agent/workflows/tfw-review.md` | Re-synced from `.tfw/workflows/review.md` |
| `.claude/commands/tfw-config.md` · `.agent/workflows/tfw-config.md` | Re-synced from `.tfw/workflows/config.md` |
| `.tfw/adapters/codex/skills/tfw-review/SKILL.md` · `.agents/skills/tfw-review/SKILL.md` | The "review-mode WAIT gate" instruction replaced with the four stage self-check gates that actually remain |
| `TECH_DEBT.md` | TD-106 closed with the reason recorded |
| `README.md` | Task Board: TFW-56 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF, ONB link added |

**Budget:** 20 modified + 3 deleted + 1 new evidence artifact. Project limits 30 files / 15 new /
3000 LOC / 30 modified — within budget on every axis; net LOC negative (−39).

## 2. Key Decisions

1. **`VERSION` → `1.1.0`, and `project_config.yaml`'s `tfw.version` with it.** The bump was the ONB's
   one blocking question; the owner chose `1.1.0` (backward-compatible removal) over the `2.0.0` that
   `RELEASE.md` §3's *"required file removed"* clause implies. `tfw.version` was bumped alongside
   because `git log -p` shows it moving in lockstep with `.tfw/VERSION` on every release since 0.8.5 —
   leaving it at `1.0.0` would have desynced two fields that have never disagreed. This is the one
   change in the task not itemised in TS §4, and it is inside a file TS §4 already lists as MODIFY.

2. **S1 is worded against U7, not merely differently from it.** AC-2 and DoF make the naming the
   deliverable. Row 7 asks *does the evidence exist*; row 8 asks *does it establish the claim*, and the
   row spells out the failure shapes: a passing test that tests the wrong thing, a self-declared gate
   marked green while unmet, a citation that does not support its sentence, a screenshot of a page that
   was never under test. A note under the table states that answering them the same way means one of
   them was not asked, and that `✅` on 7 with `❌` on 8 is the normal shape of a real finding. The
   Checkpoint requires them answered separately. The dry-run in EV §E3 is the test of whether this
   worked, and it did — different answers, different reasoning.

3. **U2 was split into two clauses rather than rewritten as one.** S3 *design soundness* is clause (b),
   a separately quotable sentence carrying its own 4.5%. TFW-53 Phase C (frozen DoD-20) replaces the
   *mapping-integrity* check in this same row — so making the two clauses separable means Phase C can
   replace clause (a) and leave S3 standing. A single fused sentence would have taken S3 out with it,
   silently. TS §6 said "sharpen U2, do not restructure it"; this is the smallest structure that
   survives the next task. See §6 observation 2.

4. **All three orphaned verify actions were migrated, none declined.** AC-4 permitted a written
   decline. They were not declined because they are the Verify-stage half of the same convergence S1 is
   the Judge-stage half of: declining them would have left the highest-firing check in TFW review with
   a Judge row and no Verify action feeding it. Destination: a new **Claim & Source Checks** section in
   `verify.md` plus a Checkpoint item — the file's established structural-enforcement site, where the
   `code` build/test action already lives unconditionally (F4, F24: structural over exhortation).

5. **`REVIEW.md` §3's missing seventh row was repaired.** It carried 6 rows against `judge.md`'s 7 —
   the Evidence completeness row added in 0.8.8 never reached it. AC-5 requires row-for-row alignment,
   so this closes as a consequence rather than as a bonus fix. Recorded because the row count moves 6 →
   10 rather than 7 → 10, and that difference should not read as scope creep.

6. **`conventions.md` §11 L466 (*"Mode files loaded at Step 2, not at start"*) was left alone.** Its
   phrasing is inherited from D42 and so reads as being about review modes, but it is also — and after
   this task exclusively — true of research: `research/{focused,deep}.md` exist and are selected at
   `research/base.md` Step 2. Editing it would have been a third change to `conventions.md` that AC-8
   does not ask for, on a sentence that remains true. Reported in §6 rather than silently changed.

7. **The three deletions were committed by another session, and no attempt was made to repair it.** A
   concurrent TFW-53 Phase B session committed `fbdf443` at 17:44 and swept up this task's
   already-staged `git rm`. The outcome is correct — the folder is gone from the working tree and from
   `HEAD` — but the deletion is attributed to another task. Rewriting `fbdf443` is not an executor's
   call: it is another session's commit and may already be published. Everything after that point was
   staged by explicit path, never `git add -A`. Full detail in EV §E9 and §6 observation 1.

8. **The mandated grep gate was run verbatim and supplemented, not corrected.** One of its four
   alternatives (`review/{code`) could never match — the real string was always `review/{mode}` — so a
   quarter of the acceptance test was itself the anti-pattern this task adds to §14. The AC was not
   modified (that would be a scope change); the command ran as written with its exit status recorded,
   and a wider case-insensitive sweep is recorded beside it as separate evidence.

## 3. Acceptance Criteria

- [x] **AC-1: The selection is absent from the framework.** `.tfw/workflows/review/` does not exist
      (`ls` fails, EV §E1). `review.md` has no mode step, no WAIT gate, no mode-file load. Steps are
      contiguous 0-7 with Step 0 = Session Naming. Every internal step reference resolves — three were
      stale *before* this task and are correct after it with no edit; one (`glossary.md` → Judge)
      needed the edit and got it.
- [x] **AC-2: The universal Judge checklist is the corrected ten rows.** No `Mode:` field, no
      Mode-Specific section (`grep -c "Mode"` → 0). Ten rows. U2 sharpened to cover design soundness.
      S1, S2, S4 added. *Content quality* absent. Each promoted row carries its measured rate inside
      the row. Explicit-N/A is structural at three sites. **The dry-run produced different answers on
      rows 7 and 8** (EV §E3) — AC-2's own pass condition.
- [x] **AC-3: Every removed check has a recorded home.** All eight rows accounted for in the table
      below; each stated destination checked against the shipped file.
- [x] **AC-4: The three orphaned verify actions have a home.** All three present in `verify.md` as
      unconditional actions; none declined. All four `code` actions still mandated. `map.md` and
      `verify.md` carry no `Mode:` field. Accounting for all eight distinct actions below.
- [x] **AC-5: The REVIEW template matches the new checklist.** No header field, no placeholder. §3
      matches `judge.md` 10/10 in the same order (EV §E4).
- [x] **AC-6: The config key is gone and its sibling is untouched.** `default_mode` absent from both
      files. `min_verify_ratio: 0.42` present in both with its comment byte-identical and its
      behavioural home in `review.md` Step 2 unchanged (EV §E5).
- [x] **AC-7: The propagation table is correct.** One `review` row remains; its `Step 2: Verify`
      pointer resolves to `review.md:60` — stale before the renumbering, correct after it (EV §E6).
- [x] **AC-8: Conventions and glossary carry no mode vocabulary.**
      `grep -rn "review mode" .tfw/ --exclude=CHANGELOG.md` → 0 matches _(corrected 2026-08-13 per the
      review finding — TD-146: this line had dropped the `--exclude` flag the command was actually run
      with; EV §E6 carried the correct form. Without the flag it returns 2 hits, both in the new 1.1.0
      entry describing the removal, in the one file DoD-15 forbids rewriting)_. The Review subfolder
      entry needed no change — it never carried mode vocabulary,
      verified by reading. §14 anti-pattern added, worded to satisfy both HL DoD-9's and TS AC-8's
      formulations.
- [x] **AC-9: Adapter parity.** All six copies clean of mode vocabulary; five `diff` runs empty; the
      Codex skill no longer names a WAIT gate that does not exist (EV §E6).
- [x] **AC-10: Version and changelog.** `VERSION` = `1.1.0`. The entry records the deletion, the
      corrected promotion set with rates, and D42's revocation. `### Removed` names
      `tfw.review.default_mode` explicitly, with instructions for an upgrading project.
- [x] **AC-11: TD-106 closed** with the reason: the anomaly was deleted, not annotated.
- [x] **AC-12: The sweep is complete and history is intact.** Grep gate returns zero matches, recorded
      with its output and exit status (EV §E7). 41 files under `tasks/` still carry `Review Mode`,
      including the dry-run subject. No past CHANGELOG entry edited. 3 deletions, no framework file
      created. ⚠️ **Qualified:** the diffstat is split across two commits because the deletions were
      swept into `fbdf443` — the substance is verified, the attribution is not clean (EV §E9).

### AC-3 accounting — all eight mode checklist rows

| Mode row | Rate | Disposition | Destination, verified in the shipped file |
|---|---:|---|---|
| `code` Test coverage | 23.4% | **PROMOTED** | `judge.md` row 8 *Evidence sufficiency* — the 141-row `code` instance of the convergence, the piece the HL's original wording would have dropped |
| `spec` Analytical quality | 25.0% | **PROMOTED** | `judge.md` row 8 — "a self-declared gate marked green while unmet" is this row's actual finding, quoted into the row |
| `spec` Source attribution | 22.2% | **PROMOTED** | `judge.md` row 8 — "a citation that does not support the sentence it is attached to" |
| `docs` Source verification | 12.5% | **PROMOTED** | `judge.md` row 8 — same residue; `docs`/`spec` confirmed synonyms (RES D5) |
| `code` Breaking changes | 8.5% | **PROMOTED** | `judge.md` row 9 *Backward compatibility*, de-domained per F13: interface, template section number, document anchor, downstream process, report |
| `code` Security | 4.0% | **PROMOTED** | `judge.md` row 10 *Safety* — the row states it is kept on consequence rather than rate, so a future rate audit does not delete it |
| `code` Code quality | 4.5% | **PROMOTED (folded)** | `judge.md` row 2 clause (b) *Design soundness*, a separately quotable sentence with its own rate. Explicitly *not* row 4: the six hard failures were contract violations, not naming or style |
| `docs` Content quality | 5.9% | **DROPPED — true duplicate** | Universal row 4 *Style & standards* already asks it. The only one of the eight without residue (A1) |

Eight rows: **seven promoted, one dropped as a proven duplicate, none silently disappeared.**

### AC-4 accounting — all eight distinct verify actions

The three mode files carried ten verify-action entries; four are the same ratio action stated three
times. Eight distinct actions:

| # | Action | From | Disposition | Home in the shipped files |
|---|--------|------|-------------|---------------------------|
| 1 | Open/verify at least `min_verify_ratio` of files, escalate to 100% on discrepancy | all 3 modes | **already covered** | `review.md` Step 2 parameter table + worked example; `verify.md` header `Files to verify: ⌈N × ratio⌉` and Checkpoint *"Opened ≥ ⌈N × ratio⌉ files"* |
| 2 | Re-run at least 1 build/test command if possible | `code` | **already covered** | `verify.md` Checkpoint *"Ran at least 1 build/test command (or documented why not)?"* |
| 3 | Cross-reference RF §3 AC checkmarks against TS DoD | `code` | **already covered** | `verify.md` Checkpoint *"Each RF §3 (AC) checkmark verified against actual file?"* + `review.md` Trust Protocol row *"DoD met" → Cross-check each TS AC item against actual files* |
| 4 | If "Tests pass" claimed → check test file exists | `code` | **already covered** | `review.md` Trust Protocol row *"Tests pass" → Re-run test command or check test file exists* |
| 5 | Check document structure matches spec (headings, required sections) | `docs` | **already covered** | Required structure is declared by the TS, so `judge.md` row 1 *DoD met* holds it; `verify.md`'s per-file *RF claim / Actual / Match* log records it; row 4 *Style & standards* holds convention conformance |
| 6 | Spot-check 2-3 key claims/sources for accuracy | `docs` | **PROMOTED** | `verify.md` → **Claim & Source Checks** action 1 + Checkpoint item |
| 7 | Check source citations are traceable to real artifacts | `spec` | **PROMOTED** | `verify.md` → **Claim & Source Checks** action 2 + Checkpoint item |
| 8 | Verify data claims against primary sources where possible | `spec` | **PROMOTED** | `verify.md` → **Claim & Source Checks** action 3 + Checkpoint item |

Three promoted, five already unconditionally mandated, **none declined and none lost.** Actions 1-4
are the four `code` actions AC-4 requires to remain mandated; action 5 is a fourth `docs` action the
HL and TS did not enumerate among the "three orphaned" — accounted for here because DoF-1 covers every
verify action available today, not only the three that were named.

## 4. Verification

- **Lint** (`config.build.lint` = `echo "configure your lint command"`): unconfigured starter
  placeholder — nothing to run. Substituted by the docs pipeline below, per the precedent set and
  approved in EV TFW-53/A.
- **Tests** (`python -m pytest docs/scripts/`): **68 passed** in 33.47s. This is the real build gate —
  `conventions.md`, `glossary.md`, `.tfw/workflows/**` and `.tfw/templates/**` are Source Manifest rows
  4, 5, 12 and 13, so the docs pipeline is the only consumer of every file this task changed. Run
  before the RF was written, per the Step 10 build gate.
- **Verify** (`config.build.verify` = placeholder): not applicable. The task's acceptance test is a
  recorded grep, which is AC-12 and EV §E7.
- **Structural gates**, all recorded in the EV file with their output: folder absence, step
  contiguity, 10-row count, `Mode` count 0 in `judge.md`, both config excerpts, one propagation row,
  `grep -rn "review mode" .tfw/` → 0, six-adapter grep → 0, five parity `diff`s → empty, the verbatim
  grep gate → 0 with exit 1, a wider case-insensitive sweep → 4 hits all in the untouched research
  axis, 41 surviving `Review Mode` headers under `tasks/`.
- `gen_docs.py` carries no reference to review modes, confirming RES D9's consumer audit against the
  shipped state rather than the pre-change state.

## 5. Evidence

> **Cognitive mode:** Observational verification — evidence lives in the EV file, not inline.

See [EV file](evidence/EV__TFW-56__review_mode_removal.md) for evidence details.

Evidence verdict: **9/16 VERIFIED, 0 DEFERRED, 0 BLOCKED, 7 N/A**

The 7 N/A quote the TS's own `Evidence:` fields verbatim. E15 (diffstat) is marked VERIFIED with its
trace anomaly recorded in full rather than softened to DEFERRED — the fact is true and checkable; it
is the attribution that is wrong, and downgrading the status would have hidden exactly what this
layer exists to surface.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `fbdf443` (commit) | — | security | **A concurrent session's commit captured this task's staged deletions.** `[claude-code/TFW-53/phase-b/executor]` committed `.tfw/workflows/review/{code,docs,spec}.md` deletions that belong to TFW-56, because a broad `git add`/`git commit -a` ran while they sat in the shared index. Two sessions were writing the same working tree and index simultaneously. Recovering "when did TFW-56 delete the mode files" from TFW-56's commits now returns nothing. The generalisable rule: an agent sharing a working tree must stage by explicit path, never `git add -A` — and TFW has no convention saying so |
| 2 | `.tfw/templates/review/judge.md` | row 2 | todo | **TFW-53 Phase C will evict S3 unless its TS says otherwise.** Phase C's frozen DoD-20 replaces the *mapping-integrity* check in this row, and its context block names Universal Checklist row 2 as the target. S3 *design soundness* (4.5%, six hard ❌) now lives in clause (b) of that row. Clause (b) was deliberately written as a separately quotable sentence so Phase C *can* replace clause (a) and leave it — but nothing in either task's frozen DoD requires it to. One line in Phase C's TS closes this |
| 3 | `knowledge/process.md` | F19 | todo | F19 states `review.md` is the only workflow with a non-standard Step 0 and that "Select Review Mode = Step 1 by design". Both halves are now historical — the step is deleted and Step 0 is Session Naming. Not in TS §4 scope; belongs to `/tfw-knowledge` |
| 4 | `KNOWLEDGE.md` | L74, L173 | todo | D42 is revoked by this task and its row does not say so; the Legacy table row still describes "6 universal + 2-4 mode-specific items. Mode files in `.tfw/workflows/review/`". Not in TS §4 scope — this is `/tfw-docs` territory at KNW |
| 5 | `RELEASE.md` | §3 | naming | The MAJOR row's *"required file removed"* clause classified this task as MAJOR while the owner correctly judged it MINOR (nothing downstream breaks). As written, deleting any unused framework file forces a major — which discourages deletion, the opposite of what a framework wants. Raised in ONB Q1 and answered by choosing `1.1.0`; the rule itself was left untouched |
| 6 | `.tfw/conventions.md` | 466 | naming | §11 Design Rules: *"Mode files loaded at Step 2, not at start"*. Phrasing inherited from D42 (review), still true of research (`research/base.md` Step 2). Left as-is per §2 decision 6 — but a reader who knows the D42 lineage will read it as a dangling reference |
| 7 | `.tfw/workflows/config.md` | 101-112 | duplication | The Adapter Sync block lists four `cp` commands to `.agent/workflows/` only — it omits `.claude/commands/` entirely and omits `review.md` from both. Four adapter copies exist for the files this task touched, and the workflow that is supposed to keep them synced documents one of them. Pre-existing; I synced all four by hand |
| 8 | `.tfw/templates/review/judge.md` | rows 9-10 | perf | S2 (8.5%) and S4 (4.0%) sit at positions 9 and 10, the tail. HL §7.2 #25 records that LLM judges are order-sensitive and that the tail positions are the weakest ones. The order is HL §3.1's frozen after-diagram and was implemented as specified; the mitigation the HL chose is the structural explicit-N/A grammar, not reordering. Worth measuring once the ten-row checklist has a corpus |

## 7. Fact Candidates

> fact-candidates: processed 2026-08-13 — none admitted to `knowledge/`; the operational ones are carried as TD-144, TD-146, TD-149, TD-150

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | environment | Two agent sessions can hold the same git working tree and index simultaneously in this project, and a broad `git add`/`commit -a` in one will capture the other's staged changes. Observed: `fbdf443` (TFW-53/B) committed TFW-56's staged mode-file deletions three minutes after they were staged. Mitigation that worked: stage by explicit path only | Executor, 2026-08-13 (EV §E9) | ★★★ |
| 2 | process | `.tfw/project_config.yaml`'s `tfw.version` field has tracked `.tfw/VERSION` in lockstep on every release since 0.8.5 — verified by `git log -p -- .tfw/project_config.yaml`. A task that bumps `VERSION` must bump both or leave two fields disagreeing for the first time | Executor, 2026-08-13 | ★★★ |
| 3 | constraint | `RELEASE.md` §3's MAJOR row (*"required file removed"*) classifies any framework-file deletion as breaking. The owner ruled TFW-56 a MINOR (`1.1.0`) on the ground that nothing downstream breaks — so the written rule and the owner's applied standard diverge, and the applied standard is impact-based | User, 2026-08-13 (ONB Q1) | ★★★ |
| 4 | process | The acceptance grep in TS AC-12 contained an alternative (`review/{code`) that matched nothing in the repository before any change was made — the real string was `review/{mode}`. A grep gate authored from memory rather than run once against the pre-change tree can ship a dead alternative and still read as a complete sweep | Executor, 2026-08-13 (EV §E7) | ★★★ |
| 5 | convention | `.tfw/workflows/config.md`'s Adapter Sync block documents `.agent/workflows/` copies only and omits `.claude/commands/` — so the workflow that exists to prevent adapter drift covers half the adapters. All four copies were byte-identical to their sources before this task, so the drift has been prevented by discipline rather than by the documented procedure | Executor, 2026-08-13 | ★★☆ |

## 8. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | The owner chose `1.1.0` over the `2.0.0` that their own `RELEASE.md` §3 prescribes, on the impact test rather than the letter — nothing downstream breaks, so it is not a major. **Implication:** the applied release standard in this project is *observable consumer impact*, not *category of change*, and §3's file-based clause is a proxy that has now visibly failed once. Left unedited by decision, so the next version bump will hit the same fork. A framework whose written rule forces a major for deleting an unused file has an incentive not to delete unused files — which is the opposite of what TFW-56 exists to demonstrate | philosophy | User, 2026-08-13 (ONB Q1) |
| S2 | The owner answered a blocking question with two characters and no argument. **Implication:** the ONB's job was to make the decision cheap, not to be discussed — options with costs stated, a recommendation, and no further ceremony. That is a signal about the shape of blocking questions in this project: one real fork, priced, with the executor's recommendation attached, is answerable in a word. It also raises the cost of a *bad* blocking question, since an owner who answers in one word is not going to relitigate a question that should never have been asked | process | User, 2026-08-13 |
| S3 | The research inverted this task's own empirical premise, and the task shipped anyway — on the design argument (*«что проверять задается рамкой задачи»*, HL §11 S1) with a corrected promotion set bolted on through seven amendments. **Implication:** the amendment channel absorbed a refuted premise without the task dying, which is the first live demonstration that TFW-53's contract mechanism does what it was built for. The executor-visible consequence is concrete: the frozen §3.1 diagram told me exactly which ten rows in which order, so a measurement that arrived *after* the freeze still produced an unambiguous instruction rather than a judgement call | philosophy | HL §12 A1-A7, RES iter1 |

## 9. Diagrams

**The reviewer's path, before and after.**

```
BEFORE                                        AFTER
────────────────────────────────────────      ────────────────────────────────────────
Step 0  name the session                      Step 0  name the session
Step 1  read config default_mode              Step 1  Map        ← work starts here
        guess the mode from task context      Step 2  Verify
        "Review mode: [docs]. Switch?"        Step 3  Judge
        🛑 WAIT for the owner                 Step 4  Decide
        load workflows/review/docs.md         Step 5  Tech Debt
Step 2  Map                                   Step 6  Update Traces
Step 3  Verify (+ mode verify actions)        Step 7  Knowledge Capture
Step 4  Judge  (+ 2-4 gated rows)
…                                             8 steps, contiguous, Step 0 standard
9 steps, one of them a blocking gate          for the first time (TD-106 closed)
        with 0 verdict flips in 203 reviews
```

**Where the eight gated rows went — grouped by residue, not by name.**

```
   GATED (visible to 1 review in 3)                UNIVERSAL (every review)
   ─────────────────────────────────               ────────────────────────────────
   code  Test coverage        23.4% ─┐
   spec  Analytical quality   25.0% ─┤
   spec  Source attribution   22.2% ─┼──────────►  row 8  EVIDENCE SUFFICIENCY  16.1%
   docs  Source verification  12.5% ─┘             "the green signal does not
                                                    establish the claim"
   code  Breaking changes      8.5% ──────────►    row 9  Backward compatibility 8.5%
   code  Security              4.0% ──────────►    row 10 Safety                 4.0%
                                                          (kept on consequence)
   code  Code quality          4.5% ──────────►    row 2(b) Design soundness     4.5%
                                                          ↑ separable clause, so
                                                            TFW-53/C can replace 2(a)
   docs  Content quality       5.9% ─────✂────►    row 4 Style & standards
                                                          already asked it
   ── verify actions ──
   docs  spot-check claims          ─┐
   spec  citations → real artifacts ─┼──────────►  verify.md CLAIM & SOURCE CHECKS
   spec  data → primary sources     ─┘             unconditional + Checkpoint item
   code  ratio · build/test · AC×DoD ·             already unconditional in
         test-file check                           verify.md + Trust Protocol
   docs  structure matches spec     ──────────►    row 1 DoD met (TS declares it)

   7 promoted · 1 dropped as proven duplicate · 0 lost
```

**Row 7 vs row 8 — why two rows and not one.**

```
                  row 7  COMPLETENESS              row 8  SUFFICIENCY
                  "is it there?"                   "does it prove it?"
                        │                                 │
   EV file has 15 rows  ✅                                │
   4-status vocab only  ✅                                │
   attachments resolve  ✅                                │
   N/A quote the TS     ✅                                │
                        │                                 │
                        │        E2 VERIFIED, but RESTRICT untested  ❌
                        │        E13 VERIFIED, conclusion superseded ❌
                        │        E11 4/4, but a property was removed ❌
                        ▼                                 ▼
                       ✅                                ❌
              nothing is missing              three present artifacts prove
                                              less than they are offered for

   Dry-run subject: TFW-53/A (EV §E3). The findings were written by that task's own
   executor, inside the EV file, and no checklist row was asking for them.
```

---

*RF — TFW-56: Remove the Review Mode Axis | 2026-08-13*
