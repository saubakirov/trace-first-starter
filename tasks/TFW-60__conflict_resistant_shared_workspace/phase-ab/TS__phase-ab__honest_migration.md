# TS — TFW-60 / Phase AB: Honest Migration

> **Date**: 2026-08-29
> **Author**: Claude Code (Coordinator)
> **Status**: ✅ APPROVED — owner, 2026-08-29, at **revision 2**. Execution authorized
> **Revision 2**: after onboarding. Three blocking questions answered; changes carry `R2`. Four of the
> nine inconsistencies were the coordinator's: an incomplete grammar surface, release work assigned
> against §15, a DoF clause forbidding the only realizable tag order, and an adapter line that would have
> broken the Codex router architecture.
> **Phase HL**: [HL Phase AB](HL__phase-ab__honest_migration.md)
> **Master freeze**: `810b1b8` — baseline after amendment A5
> **Origin**: [third field report](../FIELD-REPORT__TFW-60__third_external_update.md), defect groups 1–7
> **Predecessor read through the Pre-TS Gate**: Phase AA RF at revision 2, REVIEW revision 3, and the closure at `9570402` — the phase was closed by owner waiver with blocking item 1 outstanding (TD-199), so the RF does **not** describe the R4 pass. TS AC-15 and REVIEW rev3 §2 are the authoritative account of what that pass built.

---

## 1. Objective

Make the migration tools tell the truth. After this phase a tool either parses an identifier whole or
refuses it, computes every guarantee it prints, and preserves identifier characters in the prose it
carries across.

New tasks take one identifier grammar — project, moment, subject — and every existing form stays
readable forever.

## 2. Scope

**In scope:** identifier parsing in both scripts, the identifier grammar in `conventions.md` and
`plan.md`, the manifest's asserted invariants, markup stripping, the framework/corpus test split,
`update.md`'s source-quiescence and provenance-drift rules, the retired-vocabulary check's wording, and
the two items carried from Phase AA.

**Out of scope:** any rename or move of an existing task directory; `status.md` keys; the journal event
schema; the lifecycle vocabulary; the index format; the `actor` field; the three consumer projects;
Phases B and C; TFW-61.

### Decisions the owner has already settled

| Decision | Ruling |
|---|---|
| Identifier grammar | `{PREFIX}_{YYYYMMDD-HHMMSS}_{ABBR}`, landing **in this phase** — 2026-08-29 |
| `2.0.0` release gate | This phase, with **no fourth external run** — 2026-08-29 |
| Phase AA closure | Closed by waiver; F4 and TD-197 move here — 2026-08-29 |

## 3. Principles Check

| Principle | Where it is verified |
|---|---|
| P1 Pain before mechanism | AC-1 — the pain is a completed task silently marked live on a real corpus |
| P4 Stable paths over status moves | AC-3 — three grammars coexist and nothing is renamed |
| P5 Local truth, derived views | AC-2 — the manifest computes rather than asserts; a derived artifact stops claiming what it did not check |
| P9 No trace deletion during simplification | AC-4 — migrated prose keeps its identifier characters |
| P10 Every phase pays for its release surface | AC-8 — `2.0.0` follows this phase |

## 4. Affected Files

**Measured at onboarding, 2026-08-29.** The table below was the coordinator's estimate; the executor
measured it as §4 required and found ten more grammar carriers, added under R2. Byte-identical adapter
copies are excluded by S32, work artifacts by S46.

| Group | Paths | Est. |
|---|---|---:|
| Identifier parsing | `.tfw/scripts/gen_index.py` — `LEGACY_ID`:118, `TASK_DIR`:121, `parse_identifier`:199; `.tfw/scripts/migrate_board.py` imports them at :47 | 2 |
| Manifest guarantees | `.tfw/scripts/migrate_board.py` — the asserted line at :489, the computed block at :604 | — |
| Prose fidelity | `.tfw/scripts/migrate_board.py`:367 — `re.sub(r"[*_\`~]+", "", text)` strips `_` as markup and takes identifier characters with it | — |
| Tests | `.tfw/scripts/test_gen_index.py` (95 tests, 2 repo-state at :858 and :978), `test_migrate_board.py` (39 tests, 1 repo-state at :454) | 2 |
| Grammar in canon | `.tfw/conventions.md`:232–236, :270; `.tfw/workflows/plan.md` — the abbreviation is agreed at planning | 2 |
| Update path | `.tfw/workflows/update.md` — source quiescence, provenance drift, the retired-vocabulary wording, and F4's word ceiling | 1 |
| `via` | `.tfw/conventions.md`:317 and whatever reads it — TD-197 | — |
| Migration guide | `.tfw/migrations/2.0.0.md` — the new grammar and the "commit, or at least stage" wording | 1 |
| Release surface | `.tfw/VERSION`, `.tfw/CHANGELOG.md`, `.tfw/project_config.yaml` | 3 |
| Adapter copies | **R2** — `tfw-plan`, `tfw-update`, `tfw-init` under `.claude/commands/` and `.agent/workflows/`. **`.agents/skills/` is verified byte-identical to its adapter source and otherwise untouched**: a Codex skill is a thin router under D54, and copying a workflow body into it would break the adapter architecture rather than honour the owner's copies ruling | — |

### R2 — ten grammar carriers the coordinator's estimate missed

Onboarding measured the surface, as §4 asked it to. These are in scope:

| Path | Why |
|---|---|
| `.tfw/workflows/init.md` | Creates a project's **first** task and hard-codes the old form. Leaving it out ships a framework whose first task and second task use different grammars |
| `.tfw/templates/project_config.yaml` | New projects copy it; `id_format` still issues the dirty-era form |
| `.tfw/templates/HL.md` | AC-3 requires the approved abbreviation in the HL header and the template has no field for it |
| `.tfw/templates/status.md` | Its `id` and `authority` examples teach the old form |
| `.tfw/glossary.md` | *Task Naming* declares the dirty-era form current |
| `.tfw/compilable_contract.md` | Defines reference patterns for `PREFIX-N` only |
| `docs/scripts/gen_docs.py` | **Functional, not cosmetic**: the resolver accepts only `PREFIX-N`, so a new-grammar task cannot participate in D43's citation cascade. `\b` also treats `_` as a word character, so the boundary strategy cannot take the new pattern unchanged |
| `docs/scripts/test_gen_docs.py` | Regression cover for the above |
| `.claude/commands/tfw-init.md`, `.agent/workflows/tfw-init.md` | Copies of a now-affected canonical workflow |

`KNOWLEDGE.md` D68 and §3 Legacy also declare the old form current. They are **not** the executor's:
D37 reserves them for `/tfw-docs`. Record both in RF Observations.

Census after this addition: **25 physical paths, 19 budget-counted, 0 new files** — inside `30 / 15`.

**Budget.** `30 / 15 / 30 / 3000`. Measured at onboarding: 25 physical, 19 counted, 0 new. **No overrun is
authorized** and the limits do not move.
Phase A's ruling did not extend to AA and does not extend here. Any group appearing or any limit
approached returns to the coordinator before the work proceeds.

## 5. Acceptance Criteria

### AC-1: An identifier is parsed whole or refused

The third report's defect 1. **R2 — onboarding traced it.** The collapse is the unanchored `re.search()`
in `migrate_board.parse_board()`, which reaches an identifier *before* `LEGACY_ID` is consulted — so the
anchored grammar never had the chance to refuse `HD-30b`. Record that in the RF: an unanchored search
reached the identifier ahead of the anchored grammar, and everything downstream trusted the result.

- [ ] the parser recognizes exactly three **named** forms and matches each one whole:

      | Form | Shape | Status |
      |---|---|---|
      | legacy | `PREFIX-N` or `PREFIX-N__slug` | supported forever, never renamed |
      | `2.0.0-dirty` | `YYYYMMDD-HHMMSS__slug` | supported forever, three consumers hold it |
      | current | `PREFIX_YYYYMMDD-HHMMSS_ABBR` | AC-3 |

- [ ] anything matching none of the three **whole** is `malformed`: reported, visible, non-actionable,
      and **never** matched by prefix with the remainder discarded
- [ ] a malformed identifier never produces a `status.md`, never enters the index as a classified task,
      and never carries a reason the source did not give
- [ ] **two rows resolving to one identifier is a hard stop before any write**, naming both rows
- [ ] **R2 — the same holds on the directory side.** `TFW-1__a` and `TFW-1__b` normalize to one identifier
      and the current dictionary silently overwrites one. A collision is a hard stop wherever it comes
      from; the rule is about identifiers, not about which side produced them
- [ ] every form that parsed before this change still parses; the three consumer corpora and this one are
      re-run before and after and compared identifier by identifier

Gate: a fixture carrying `HD-30`, `HD-30b`, `TFW-01_single_underscore`, a `2.0.0-dirty` identifier and a
current-grammar one. Each is matched to its named form or reported. The duplicate stops the run.
Evidence: the run output, plus the before/after comparison on four corpora.

### AC-2: The manifest computes every guarantee it prints  [depends: AC-1]

- [ ] `migrate_board.py`:489 asserts *"every task directory is accounted for exactly once"* as prose. It
      is **computed**, under a heading that names each guarantee checked, or it is deleted. Not both left
      standing
- [ ] the invariant now living only in `test_migrate_board.py`:454 — `matched + directory_only ==
      directories` — is evaluated by the manifest itself, at run time, on the corpus in front of it
- [ ] a failing invariant **stops the run** and names which guarantee failed and on which identifiers
- [ ] **R2 — "before any write" includes creating the manifest.** Opening the output file is a write. Every
      invariant and duplicate gate runs before it exists, which is stricter than revision 1 implied
- [ ] the manifest distinguishes *checked and held* from *not checked*; silence is not a pass

Gate: a deliberately unbalanced fixture fails, names the guarantee and writes nothing. The helpdesk board
shape, reproduced, fails before the change and passes after.
Evidence: both runs, and the reproduced shape as a committed fixture.

> This is the phase's centre. A tool that prints a guarantee it never computed is worse than one that
> prints nothing, because the reader stops looking.

### AC-3: One identifier grammar for new tasks  [depends: AC-1]

- [ ] new tasks are created as `{PREFIX}_{YYYYMMDD-HHMMSS}_{ABBR}`, for example
      `TFW_20260829-010832_CRSW`
- [ ] `PREFIX` comes from `tfw.task_prefix`, which already exists; the timestamp is read from the clock,
      never composed; `ABBR` is uppercase alphanumeric
- [ ] **no field may contain `_`**, which is what makes the single `_` an unambiguous separator. State
      this as the reason, not as a rule to memorize
- [ ] `plan.md` **asks the owner to approve the abbreviation** before the folder is created, in the same
      exchange that already establishes the task. It is never derived silently
- [ ] the HL header records the abbreviation beside the full title; `status.md` `title` already carries
      the full name and gains nothing
- [ ] **R2 — collision behaviour, which revision 1 left undefined.** Same second and same approved
      abbreviation must have a defined outcome, and **silent suffixing is forbidden** — it would invent the
      fourth grammar DoF refuses. Two rules, both reusing mechanisms this phase already builds:
      **at creation**, if the whole identifier already exists, refuse and ask for a different abbreviation;
      the timestamp is read from the clock and never re-composed to dodge a collision.
      **At validation**, two directories resolving to one identifier is AC-1's hard stop. Offline peers
      cannot see each other, so this is the rule that actually fires
- [ ] the session-naming step (Phase AA AC-12) uses the new identifier
- [ ] `conventions.md`:232–236 and the migration guide state all three forms and which one is created

Gate: create a task end to end and confirm the abbreviation was asked for, the path is well formed, and
the index renders the full title.
Evidence: the created task and the exchange that approved its abbreviation.

### AC-4: Migrated prose keeps its identifier characters

- [ ] `migrate_board.py`:367 strips `[*_\`~]` as one character class, so `normalize_text()` became
      `normalizetext()` in a project where that names a real PL/pgSQL function
- [ ] markup is stripped; identifier characters are preserved
- [ ] the snapshot's accounting table and every `status.md` are as faithful as the snapshot's lower half
      already claims to be

Gate: a board cell containing `` `normalize_text()` `` and `working_days` migrates with both intact.
Evidence: before/after on that fixture.

### AC-5: Framework tests and corpus tests are separable

- [ ] the three repository-state tests — `test_gen_index.py`:858, :978 and `test_migrate_board.py`:454 —
      are distinguishable from the 131 that test the framework, by marker or by file
- [ ] a project running `build.test` mid-migration is **not red** for that reason
- [ ] the accounting invariant is exercised by something a receiving project is actually told to run —
      AC-2 makes that the manifest itself, so the test is no longer the only place it lives
- [ ] the migration guide says which command a receiving project runs and when

Gate: the suite on a project with no index yet and a board still present.
Evidence: that run.

### AC-6: The update path states conditions that can hold

- [ ] **source quiescence.** The receiver has a rule; the source does not. A payload taken from a moving
      tree was never in any release — during the third update the source advanced one commit between the
      operator's `git log` and their `git archive`. `update.md` says: pin the source's HEAD before Step 0,
      verify the target tag exists before trusting `VERSION`, and re-check after Step 5
- [ ] **provenance drift.** Ten of twelve `CUSTOMIZED` flags were not customizations — the project was
      installed from a different line. Step 3a says that a small diff whose local wording is *older* than
      the tag is drift and should be overwritten, and to compare against `installed_from` where present
- [ ] **the retired-vocabulary check.** *"Nothing may print"* cannot hold: the payload names the retired
      terms in order to retire them. This wording is the coordinator's, from Phase AA AC-15 item 6.
      Restate it as a reachable condition — zero outside the payload and its copies, or an allowlist
- [ ] `update.md` returns **under 1200 words** (F4, carried from Phase AA). It is at 1380. Prefer removing
      duplication over removing content, as D9 did; if that cannot be done, return to the coordinator
- [ ] *"Commit, or at least stage"* in the migration guide is corrected — the board is read from `HEAD`
      and staging changes nothing

Gate: each bullet closes on the file or a command.
Evidence: the word count, and a source-tag check that fails on a missing tag.

### AC-7: `via` is either checked or declared free-form  [TD-197]

- [ ] `conventions.md`:317 states `via` as an enumeration and nothing validates it. Under Structural
      Enforcement a rule that cannot reveal its own violation is advice
- [ ] **R2 — decided: free-form.** State `via` as non-empty provider or tool text at the point it is
      defined. The reason is onboarding's and is better than "either is acceptable": no canonical provider
      registry exists, so validating the value would confuse **declaration** with **authentication** and
      recreate the boundary D59 draws
- [ ] whichever is chosen is stated where `via` is defined, and TD-197 closes

Gate: the canon and the code agree.
Evidence: the decision recorded in the RF.

### AC-8: The release describes what shipped

> **R2 — this is not the executor's work.** `conventions.md`:675 assigns `release.md` to the Coordinator
> with *"version bump → CHANGELOG → tag"*, all three. Phase AA ruled otherwise and Phase AA was wrong
> against §15; rule 17 says a delegated mandate *"does not create what an agent may do."* Propagating that
> error to look consistent is not a reason. The executor delivers code, tests, fixtures and the RF.

- [ ] **executor:** the seven small items in the third report's §7 are each fixed or filed with a reason;
      none is left unaddressed and unmentioned
- [ ] **executor:** the RF states what a project already on `2.0.0-dirty` must know, so the release entry
      can be written from it rather than reconstructed
- [ ] **`/tfw-release`, after review:** version bump, CHANGELOG entry and tag as one act — which is also
      the only order in which all three can be true simultaneously
- [ ] **`/tfw-release`:** the tag is created **and verified to exist**. The third report's operator read
      `VERSION` = `.3` and a CHANGELOG saying *"tagged locally"* while `git tag` disagreed
- [ ] `2.0.0` follows this phase without a fourth external run, per the owner's ruling of 2026-08-29

Gate: read the entry as a receiving project and follow every instruction it gives.
Evidence: the tag exists; the instructions resolve.

## 6. Technical Guidance

- **Trace before fixing AC-1.** The coordinator did not read the code path that collapsed `HD-30b`, and
  says so rather than guessing. `LEGACY_ID` as written should not match it, and both board rows pointed
  into the same directory. Report the mechanism in the RF before changing behaviour.
- **The parser gets stricter, never more permissive.** Three named forms and a dispatcher. The temptation
  will be a fourth catch-all pattern; that is the defect, restated.
- **Do not fix `HD-30b`.** It is the owner's closed sub-item of a closed task. The deliverable is the
  fixture that reproduces its shape.
- **Preserve what three reports praised.** The empty-board refusal, per-identifier accounting, the
  printed resolved root, `--check tasks` catching two operator errors, `--working-tree` being logged.
  Weakening any of them stops the pass.
- **Prose fidelity is a character-class fix, not a rewrite.** `_` is markdown emphasis only between word
  boundaries; inside an identifier it is a character.
- **Evidence is measured at a pinned commit**, never against `HEAD` — the rule Phase A learned over three
  rounds and the third report hit again from the source side.
- **The RF is not optional here.** Phase AA closed without one and it is filed as TD-199. This phase makes
  an architectural change to identifiers; its RF is the declaration the review is conducted against.

## 7. Definition of Failure

- ❌ An identifier matched by prefix with the remainder discarded
- ❌ A guarantee printed that the tool did not compute
- ❌ A form that parsed before this change no longer parses
- ❌ Any existing task directory renamed, moved or rewritten
- ❌ An abbreviation derived without the owner approving it
- ❌ A fourth grammar, or a catch-all pattern that makes a fourth unnecessary by accepting anything
- ❌ **R2** — any instruction to fetch, clone or archive a reference that does not exist. Revision 1 forbade
  naming the version *anywhere* before the tag, which forbids the only realizable order: a tag can point
  only at an object that already exists, so the release files necessarily name their version first. The
  failure is at the **publication boundary** — the third report's operator was told to take a tag that
  `git tag` did not list
- ❌ A check whose stated condition cannot be reached
- ❌ Any budget limit crossed without returning to the coordinator — no overrun is authorized for this phase
- ❌ The model changed: `status.md` keys, the event schema, the lifecycle vocabulary or the index format
- ❌ A check reported as passing that never ran — the pattern this task has now met five times

## 8. Phase Risks

| Risk | Control |
|---|---|
| Stricter parsing breaks a working corpus | Four corpora re-run before and after, compared identifier by identifier |
| The grammar change and the parser fix interfere | They are one change by design; AC-1 lands before AC-3 depends on it |
| The abbreviation becomes noise nobody agreed to | AC-3 makes approval a step in `plan.md`, and the full title stays in `status.md` |
| The phase drifts into a fourth delivery pass | The declared outcome is honesty of the tools; a delivery finding is filed |
| `update.md` grows again while gaining three rules | AC-6 requires it *under* the ceiling with the rules added, by removing duplication |

## 9. Cross-Phase Modifications

None. Phase AB changes how identifiers are parsed and how migration reports; it changes no carrier
Phases B or C extend. The `actor` field stays removed and returns with TFW-54.

---

*TS — TFW-60 / Phase AB: Honest Migration | 2026-08-29*
