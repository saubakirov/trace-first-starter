# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 73 authored product files (45 modified + 28 new), excluding propagated copies and task traces
> Files to verify initially: ⌈73 × 0.42⌉ = 31
> Escalation: the first evidence discrepancy triggered 100% verification. All 103 paths changed from baseline `80d6a16` through `HEAD` were inspected by full diff, content read, or byte-copy comparison.

## Verification Log

| # | Surface | Files checked | RF claim | Actual | Match |
|---|---------|---------------|----------|--------|-------|
| V1 | Canonical rules, configuration, release | 8 | The core declares task-local state, both identifier grammars, and release `2.0.0` consistently | Core direction is present, but the release contains false collision claims; `.tfw/templates/project_config.yaml` still says `version: "0.8.4"` | ❌ |
| V2 | Canonical templates | 17 | Templates use `{ID}` and describe the new carriers without legacy residue | New carrier templates exist. `REVIEW.md` still requires `initial_seq`; the journal filename collides for equal second + equal kind; the project-config template has the old version | ❌ |
| V3 | Canonical workflows | 7 | Every lifecycle workflow uses the shipped model | `plan.md` creates a clock ID but immediately reads removed `tfw.initial_seq`; `init.md` still teaches `{PREFIX}-1` in seven live places and contains orphaned `RND-2/RND-3` table rows; `handoff.md` retains the legacy EV filename; `resume.md` retains `{PREFIX}-{N}` | ❌ |
| V4 | Adapter originals | 10 | Adapter originals describe the new context model | The Codex entry-point change is present. It loads `status.md` but omits the selected task's `journal/`; propagated workflow defects remain because adapters route to those canonical workflows | ⚠️ partial |
| V5 | Installed adapter copies | 24 | Installed copies are synchronized from their canonical sources | The 14 changed Antigravity/Claude workflow copies and 8 changed Codex skills checked against their sources are byte-identical where declared. The copies faithfully propagate the canonical defects | ✅ copy integrity / ❌ semantics |
| V6 | Documentation scripts and tests | 6 | One resolver supports both grammars and every configured container; tests cover the release | `gen_index.py` finds both layouts, but `gen_docs.py` still matches only `{task_prefix}-N`, globs only `tasks/`, and groups `tasks/2026/<task>` under `2026`. Tests exercise the legacy corpus and miss the new layout | ❌ |
| V7 | Migrated task corpus and task traces | 23 | Eleven live states ship; every authority resolves; accounting is exact and reproducible | Only 10 state files are tracked. TFW-36's state is ignored by `*`. TFW-54's committed state points to an untracked HL. Current accounting was regenerated after board removal and no longer contains the claimed 61/53 reconciliation | ❌ |
| V8 | Root entry points | 4 | README/AGENTS/CLAUDE/RELEASE route to task state and no longer depend on the board | Board removal and route are present. The root entry points are broadly aligned; this does not repair the contradictory canonical init/update/review instructions | ⚠️ partial |
| V9 | Team profiles | 3 executor paths | Human and agent principals have declared attribution | `saubakirov` and `claude-code` profiles are valid. No lifecycle workflow actually performs the binding resolution before its first durable write | ⚠️ partial |
| V10 | Portfolio index | 1 | Deterministic, derived, 11 sources, current | It is deterministic for identical working-tree inputs. Its committed 11-source result depends on ignored TFW-36 state and an untracked TFW-54 HL; a clean checkout has different inputs. A legitimate task-local transition makes the mandatory `test_committed_index_is_current` fail until the shared index is rewritten | ❌ |
| V11 | RF and evidence traces | 6 | Evidence is internally consistent and supports 43 VERIFIED claims | All files exist, but the migration artifact was overwritten, the ceiling population conflicts across four locations, and several fixtures test weaker cases than their claims | ❌ |
| V12 | Reviewer identity exception | 1 reviewer-added path | N/A — not executor output | `team/codex.md` was added during review on the owner's explicit instruction so the reviewer can write an honest journal actor. It is excluded from executor-surface judgment | ⚪ N/A |

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest docs/scripts/ -q` | `129 passed, 1 skipped in 34.50s` |
| 2 | `python docs/scripts/gen_index.py --check` | `index up to date: workspace/00-INDEX.md` for the current dirty working tree |
| 3 | `python -m pytest docs/scripts/ -q --collect-only` | 130 tests collected |
| 4 | `git diff --name-status 80d6a16..HEAD` + grouped full-diff audit | 103 changed paths: 79 non-installed-copy paths + 24 installed adapter paths; all inspected after escalation |
| 5 | SHA-256 comparison of canonical workflows/Codex skill originals against installed copies | All checked declared copies were byte-identical |
| 6 | `rg` sweep for `{PREFIX}`, `initial_seq`, `Task Board`, and hardcoded `tasks/` across workflows/templates/adapters/scripts | Live residue found in `init.md`, `plan.md`, `update.md`, `handoff.md`, `resume.md`, `REVIEW.md`, and all propagated copies; hardcoded task paths found in `gen_docs.py` and `migrate_board.py` |
| 7 | Targeted temp-tree probe of `gen_docs.resolve_references("RF 20260826-120000")` | Output remained plain text although the clock-ID RF existed under `workspace/2026/…` |
| 8 | Targeted malformed-state probe of `gen_index.read_status()` | A state missing `goal`, `value`, `created`, and `updated` was accepted without `_error` |
| 9 | Targeted task-index grouping probe | `tasks/2026/20260826-120000__demo/status.md` groups under key `2026`, not the task ID |
| 10 | `git ls-files 'tasks/*/status.md'` + ignored check | 10 tracked states; `tasks/TFW-36…/status.md` is ignored by the task's `*` rule |
| 11 | `git cat-file -e HEAD:<authority>` for every migrated status | All committed authorities exist except TFW-54; that status resolves only because the current worktree contains an unrelated untracked HL |
| 12 | `git log --oneline -- evidence/migration_accounting.md` and historical blob read | Correct 61/53 accounting existed at `b094943`; commit `c00c4bc` overwrote it with a post-removal 0/53 result |
| 13 | Current `git diff --name-status 80d6a16..HEAD -- tasks/` | 23 additions, not the 14 additions stated in E23's alleged current-HEAD output |
| 14 | Current commit-subject recount | 283 subjects name a task, not the fixed 278 in E30/RF; TFW-37 remains the single historically named identifier without a directory |
| 15 | After the review's normal `RF → REV` task-local transition: `gen_index.py --check` and `pytest …::test_committed_index_is_current` | Both exit 1: the shared index is stale and the build test fails until that aggregate is rewritten |

Passing tests establish that the tested cases still pass. They do not establish the missing same-second/same-kind, mutually-offline, clean-checkout, full-status-schema, or year-nested documentation cases.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “Two participants who create a task while offline from each other cannot produce two directories carrying the same ID” | Master HL DoD 18; TS AC-2; RF §3 | Identifier grammar `YYYYMMDD-HHMMSS`; fixture uses `12:00:00` and `12:00:01` | ❌ — equal wall-clock seconds produce the same ID while neither participant can observe the other |
| C2 | “Two participants appending concurrently produce two files and no contended write” | TS AC-3; RF §3; EV E8 | Journal grammar `YYYYMMDD-HHMMSS__{kind}.md`; fixture uses `dispatch` and `handoff` | ❌ — equal second + equal kind produces one pathname |
| C3 | “Both grammars are readable by every consumer” | TS AC-2; RF §3/§1; EV E7 | `gen_index.parse_identifier`; `gen_docs.resolve_references` | ❌ — only `gen_index` is shown; the docs resolver rejects clock IDs and hardcodes legacy paths |
| C4 | “61 rows + 53 directories … 53 matched, 8 board-only” | EV E22; RF §3 | Current `evidence/migration_accounting.md` and its Git history | ❌ — the current artifact says 0 rows/53 directories; the supporting historical blob was overwritten |
| C5 | “Every authority resolves to a file that exists” | EV E25 | Migrated status files against the committed `HEAD` tree | ❌ — TFW-54 points to an untracked HL and is broken in a clean checkout |
| C6 | “The ceiling population is 272 + 63 = 335; 3 exceed” | RF/EV/template/changelog | `ceiling_measurement.txt` | ❌ — the attachment measures 280 + 63 = 343 and later says “3 of 335” internally |
| C7 | “Quick Start, canonical rules, glossary, templates and adapter originals carry no residue” | EV E42; RF §3 | Repository-wide residue sweep | ❌ — multiple live instructions still allocate/use `initial_seq` or `{PREFIX}-1`; template version remains 0.8.4 |
| C8 | “The committed index has 11 task state sources” | `workspace/00-INDEX.md`; RF §1 | Git-tracked states and ignored files | ❌ — only 10 states ship; the eleventh is ignored and absent from a clone |
| C9 | “Project-level views … [are not] edited by every workflow transition” and “Different tasks synchronize without a common edit” | Master HL §3.1/§3.2 | `test_committed_index_is_current` after the review transition | ❌ — the normal local transition makes the build red until `workspace/00-INDEX.md` is rewritten, reintroducing one shared edit for every task |

## Discrepancies Found

1. **F1 — AC-2 is internally unsatisfiable as written.** A seconds-only timestamp cannot guarantee uniqueness between mutually offline creators. The TS simultaneously fixes the grammar and requires a property that the grammar cannot provide. The fixture avoids the collision by assigning different seconds and therefore does not test the requirement.
2. **F2 — The shipped creation workflows do not implement their claimed collision protocol.** `plan.md` and `init.md` say to take the clock; neither defines identifier-level existence checks, bounded retry, backwards-clock behavior, or fail-visible output. The non-shipped fixture cannot substitute for the released workflow.
3. **F3 — AC-3's journal filename is not concurrency-safe.** `YYYYMMDD-HHMMSS__{kind}.md` collides when two writers use the same kind in the same second. E8 only demonstrates different kinds.
4. **F4 — Participant resolution is demonstrated only in a non-shipped harness.** The lifecycle workflows do not resolve the acting profile before their first durable write. During this review, multiple profiles and no binding did not provide a valid Codex handle until the owner explicitly authorized adding one.
5. **F5 — AC-4's “no private preferences in the shared tree” condition conflicts with this repository's existing `.user_preferences.md`.** Git ignore does not make a file synchronization-ignore. The fixture's empty temp tree does not establish the repository condition.
6. **F6 — The status reader does not enforce the declared closed schema.** It omits required `goal`, `value`, `created`, `updated`, lifecycle vocabulary/conditional keys, terminal `outcome`, date/type validation, and directory-ID consistency. Malformed live state can become authoritative instead of unresolved.
7. **F7 — `gen_docs.py` is not migrated to the new model.** Artifact, phase, HL, and bare-ID resolvers hardcode `tasks/` and the legacy prefix grammar. Its tasks index treats the creation year as the task folder. Green integration tests contain no year-nested clock-ID fixture.
8. **F8 — Clean-checkout migration completeness fails.** Ten states are tracked, not eleven; TFW-36 is ignored, while TFW-54's authority was selected from an unrelated untracked file and is absent at `HEAD`.
9. **F9 — The required migration accounting evidence was overwritten.** The current artifact no longer supports E21/E22 and the migration is not re-runnable after the board is removed. The script also hardcodes `tasks/BOARD-SNAPSHOT.md`, the index link, the TFW-60 title, and `--today 2026-08-26`.
10. **F10 — The release surface contains live legacy residue.** `init.md`, `plan.md`, `update.md`, `handoff.md`, `resume.md`, `templates/REVIEW.md`, their propagated copies, and the `0.8.4` template version contradict the `2.0.0` release claim.
11. **F11 — AC-7 contradicts AC-1 inside the TS.** AC-1 mandates `<container>/<YYYY>/<id>__<slug>/`; AC-7 says new and legacy tasks are at the same depth below root. Both cannot hold without changing one clause.
12. **F12 — Evidence counts are stale or inconsistent.** E23 reports 14 task additions where current HEAD has 23; E30 reports 278 task-naming subjects where the current recount has 283; the journal population is 343 in the attachment and 335 elsewhere.
13. **F13 — The green suite has coverage gaps aligned with the failures.** There are no tests for mutually offline same-second creation, same-kind journal append, full status schema, clean-checkout migration output, clock-ID docs resolution, or year-nested docs grouping.
14. **F14 — Safety process failure recurred.** Broad staging temporarily committed unrelated TFW-54/TFW-55 work. It was repaired without deleting the working-tree files, but this is a second concrete instance of existing TD-144.
15. **F15 — The build gate makes the derived index a shared transition hot spot.** Immediately after the reviewer changed only TFW-60's `status.md`, `gen_index.py --check` and `test_committed_index_is_current` failed. Keeping the required suite green therefore requires every task transition to rewrite `workspace/00-INDEX.md`, directly contradicting master HL §3.1 (“without being edited by every workflow transition”) and §3.2 (“Different tasks synchronize without a common edit”).

Any one discrepancy requires full verification; all 103 changed paths were consequently checked.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | fixture AC-1 path stability | ✅ | ✅ — supports the fixture path claim |
| E2 | fixture AC-1 year stability | ✅ | ✅ |
| E3 | fixture + container unit test | ✅ | ❌ — only proves `gen_index` configuration; hardcoded `tasks/` remains elsewhere |
| E4 | fixture empty-container creation | ✅ | ⚠️ — proves no counter in that harness, not offline uniqueness or shipped workflow behavior |
| E5 | fixture visible collision | ✅ | ⚠️ — proves a collision visible in one tree, not mutually offline collision |
| E6 | fixture bounded retry | ✅ | ⚠️ — algorithm exists only in the non-shipped fixture transcript |
| E7 | `test_parse_identifier` | ✅ | ❌ — proves one parser, not every consumer |
| E8 | fixture concurrent append | ✅ | ❌ — different kinds produce different names; same-kind contention is untested |
| E9 | fixture over-ceiling refusal | ✅ | ⚠️ — no released workflow implements the refusal gate |
| E10 | fixture correction event | ✅ | ✅ |
| E11 | ceiling attachment | ✅ | ❌ — 280/63/343 in the attachment versus 272/63/335 in the claim; attachment is internally inconsistent |
| E12 | identity fixture | ✅ | ❌ — no shipped lifecycle workflow invokes this resolution; the live review exposed the gap |
| E13 | identity fixture | ✅ | ❌ — the real project tree contains `.user_preferences.md` |
| E14 | identity fixture | ✅ | ⚠️ — design rule is documented, but no consumer is implemented |
| E15 | agent profile fixture/repository | ✅ | ✅ — `claude-code` has its own profile |
| E16 | explicit deferral | ✅ | ✅ — the DEFERRED status is honest and bounded |
| E17 | deterministic index tests | ✅ | ✅ — identical inputs produce identical bytes |
| E18 | current index header | ✅ | ⚠️ — true for the dirty tree, not for clean `HEAD` inputs |
| E19 | unresolved section | ✅ | ✅ — unresolved legacy directories are visible |
| E20 | four-condition fixture | ✅ | ⚠️ — malformed coverage omits most required schema rules |
| E21 | migration accounting | ✅ | ❌ — current artifact no longer records the pre-write run |
| E22 | migration reconciliation | ✅ | ❌ — current artifact says 0 rows/53 directory-only |
| E23 | inline task diff | ⚠️ inline only | ❌ — current baseline-to-HEAD result is 23 additions, not 14 |
| E24 | migration negative tests | ✅ | ✅ — temp-tree non-overwrite behavior is established |
| E25 | migration tests + repository | ✅ | ❌ — TFW-54 authority is absent from committed HEAD |
| E26 | status files + test | ✅ | ✅ — the two legacy values are carried verbatim |
| E27 | board snapshot | ✅ | ✅ — 61 rows are retained in the snapshot |
| E28 | inline link recount | ⚠️ inline only | ⚠️ — no persistent checker/output; new year-nested docs layout is not exercised |
| E29 | inline placeholder relation | ⚠️ inline only | ⚠️ — plausible for five placeholders, but does not establish all relative links |
| E30 | inline commit-subject recount | ⚠️ inline only | ❌ — current count is 283, illustrating the fixed-count drift the TS warned about |
| E31 | `tasks/README.md` | ✅ | ✅ |
| E32 | board sweep | ✅ | ✅ — remaining “Task Board” mentions in the scoped sweep are historical/migration context |
| E33 | integration test + code | ✅ | ✅ — the board parser was removed |
| E34 | reintroduction test | ✅ | ✅ |
| E35 | rewritten integration tests | ✅ | ✅ |
| E36 | pytest/MkDocs integration | ✅ | ✅ — build passes for the current corpus |
| E37 | file-only lifecycle fixture | ✅ | ✅ — no runtime is required for the fixture |
| E38 | absent-index fixture | ✅ | ✅ |
| E39 | changed executable surface | ✅ | ✅ — no daemon/database/lock service was added |
| E40 | VERSION + live config | ✅ | ✅ for those two files; template-version contradiction is recorded under F10 |
| E41 | CHANGELOG | ✅ | ✅ for presence, breaking-change statement, and one-list migration form |
| E42 | residue sweep | ✅ | ❌ — live legacy instructions and version residue remain |
| E43 | board-parser code/test | ✅ | ✅ — the mechanism behind TD-81/TD-177 is removed, though registry closure waits |
| E44 | full test suite | ✅ | ⚠️ — command result reproduced, but the suite does not cover the failed guarantees |

Evidence audit summary: **22 match, 10 partial, 12 contradicted, 0 missing**. E16 remains correctly DEFERRED; “artifact exists” is not the same as “claim established.”

## Knowledge Citations Verified

All 29 coordinator citations in master HL §7.2 and all five ONB-added items were resolved and checked. Priority 0 and 1 were checked separately against the current North Star texts.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL/ONB #1 | PV 0 — `README.md` opening + § How It Works | ✅ | ✅ | ✅ — durable state/journal resume | ❌ — ONB note discusses approval headers, not resumability |
| 2 | HL/ONB #2 | PV 0 — `.tfw/README.md` thesis/success criteria | ✅ | ✅ | ✅ — durable checkpoint and bounded delegation | ❌ — ONB note discusses the file-budget ruling, not the cited purpose |
| 3 | HL/ONB #3–5 | PV 1 — structural enforcement, one authority, portability | ✅ | ✅ | ✅ | ✅ — tests/authority boundary/file-only carrier are relevant |
| 4 | HL/ONB #6–10 | PV 2 — F4/F11/F27/F34/F38 | ✅ | ✅ | ✅ | ✅, with #9 correctly N/A for execution |
| 5 | HL/ONB #11 | PV 3 — D31/D50 locality | ✅ | ✅ | ✅ | ✅ |
| 6 | HL/ONB #12 | PV 3 — D37 exclusive knowledge territories | ✅ | ✅ | ✅ | ❌ — the ONB application note is the FROZEN-status ruling and does not apply D37 |
| 7 | HL/ONB #13–17 | PV 3/4 — D43/D55/D59/D65; conventions §§3–5/13/14 | ✅ | ✅ | ✅ | ✅ |
| 8 | HL/ONB #18–21 | PV 5–7 — F22, F7/F30, risk F1, constraint F1/F3 | ✅ | ✅ | ✅ | ✅, with provider/Git item #20 correctly N/A after A3 |
| 9 | HL/ONB #22–29 | RES sources and comparative inputs | ✅ | ✅ | ✅ | ✅ for applied/N/A routing after A3 |
| 10 | ONB N1–N5 | D66, D3–D5, README live prose, RELEASE checklist, Assisted edition | ✅ | ✅ | ✅ | ✅ — each names a concrete migration or compatibility risk |

Totals: **34 citations, 34 resolved, 31 semantically relevant applications, 3 irrelevant applications, 0 hallucinated**. The three irrelevant applications are an independent D43 cascade failure and were included in the 100% escalation.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈73 × 0.42⌉ files and recorded findings? Full escalation covered all 103 changed paths.
- [x] Ran at least 1 build/test command?
- [x] Claim & Source Checks filled — key claims traced to primary artifacts and current Git state?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 34, resolved: 34, semantically verified: 31, irrelevant: 3, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 44, matched: 22, partial: 10, contradicted: 12, missing: 0

Stage complete: YES
