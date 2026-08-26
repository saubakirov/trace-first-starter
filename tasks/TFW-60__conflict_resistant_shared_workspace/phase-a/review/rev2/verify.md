# Verify — "Are the claims true?" (revision 2)
> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **Test:** "If I removed the RF, would the implementation and evidence prove the result?"
> Min verify ratio: 0.42
> RF product census: 77 files; initial minimum: `ceil(77 × 0.42) = 33`
> Escalation: discrepancies triggered 100% coverage of all 119 baseline-to-HEAD paths.

## Verification Log

| # | Surface | Verification | Actual result | Match |
|---|---|---|---|---|
| V1 | Canonical rules and TS R3 | Read full current rules and the approved TS; compared identifier, journal, identity, phase, and release clauses | The intended model is coherent and purpose-aligned | ✅ |
| V2 | Corrective delta | Inspected all 29 paths changed after approved TS R3 (`c5e447a..HEAD`) | Corrective code and evidence are present; discrepancies F-R2-1 through F-R2-7 remain | ❌ |
| V3 | Full implementation surface | Revalidated all 119 paths from `80d6a16..HEAD` by direct diff/read, schema/build tests, Git accounting, or exact-copy hashing | 119 paths accounted: 76 modified, 43 added | ✅ coverage / ❌ result |
| V4 | Test and validation gates | Ran full pytest, state validation, index freshness, targeted negative probes, and `git diff --check` | `190 passed, 1 skipped`; 53 tasks validate; index initially current; targeted probes expose two untested contract failures; one trailing-space error | ❌ overall |
| V5 | Workflow adapters | SHA-256 compared all 22 Claude/Antigravity workflow copies and all 11 installed Codex skills with their declared sources | Every declared copy is byte-identical | ✅ copy integrity |
| V6 | Identifier contract | Compared TS AC-2, resolver, plan algorithm, both config files, templates, and tests | Resolver/workflow use whole-name IDs; both `id_format` values still specify only `{YYYYMMDD}-{HHMMSS}` | ❌ |
| V7 | Journal behavior | Read validator/helper/tests and ran same-actor/provider probes | Two actors are separated, but same-actor retry fabricates later seconds and can move backward at midnight; a matching `actor: claude` passes validation | ❌ |
| V8 | Session identity | Inspected all Who Is Acting blocks and propagated copies | The POSIX path is valid; six canonical Windows paths contain TAB/BS control bytes and twelve installed copies reproduce them | ❌ |
| V9 | Migration and corpus | Recounted snapshot/status/accounting and exercised the test suite | 61 snapshot rows, 53 task directories, 8 board-only, 0 unaccounted, 11 task statuses + one phase status | ✅ core result |
| V10 | RF/EV/evidence | Audited all 59 evidence rows and every attachment against current commands/files | 46 verified, 5 partial, 5 contradicted, 1 deferred, 2 N/A | ❌ |
| V11 | Knowledge citations | Re-read PV priorities 0–4 fully and 5–7 by relevance; checked all master HL §7.2 and ONB §7 applications | 34 resolve and exist; 31 applications relevant, ONB rows 1, 2, and 12 remain irrelevant | ❌ |
| V12 | Purpose regression | Reproduced local validation/current-index behavior and inspected current build config/tests | `--validate` is the build gate and stale index is non-blocking; no transition is forced to rewrite the aggregate | ✅ corrected |
| V13 | Git safety | Inspected commits and current dirty tree | Corrective commits did not consume current TFW-54/55/TECH_DEBT changes; explicit-path staging procedure itself has no persistent proof | ✅ outcome / ⚠️ claim |

## Commands Executed

| # | Command | Result |
|---|---|---|
| 1 | `python -m pytest docs/scripts/ -q` | `190 passed, 1 skipped in 190.67s` |
| 2 | `python docs/scripts/gen_index.py --validate` | `53 tasks validate against the closed schema` |
| 3 | `python docs/scripts/gen_index.py --check` | `index up to date: workspace/00-INDEX.md` before this review transition |
| 4 | `git diff --name-status 80d6a16..HEAD` | 119 paths: 76 modified, 43 added |
| 5 | `git diff --name-status c5e447a..HEAD` | 29 corrective-pass paths |
| 6 | SHA-256 source/copy comparison | 22 workflow copies and 11 Codex skills match their sources |
| 7 | Targeted `validate_event` probe with matching filename/body `actor: claude`, `via: claude` | `provider_actor_problems=[]` — provider actor is accepted |
| 8 | Targeted `event_filename` probe with a collision at `20260826-235959` | returns `20260826-000000__transition__saubakirov.md` — composed and chronologically earlier |
| 9 | `git grep LOCALAPPDATA` with control-byte rendering | six canonical and twelve copied paths contain `<TAB>fw<BS>indings.yaml` |
| 10 | `git ls-files 'tasks/*/status.md'` | 12 tracked: 11 task-level plus one phase-level |
| 11 | Snapshot/accounting recount | 61 rows; 53 directories; 8 board-only; `Unaccounted: 0` |
| 12 | Exact E35 command over `80d6a16..HEAD -- tasks/` | 33 additions and 3 modifications, not “additions only” |
| 13 | RF E40-style Task Board sweep | returns eight historical/migration code lines, not the recorded “no output” |
| 14 | `git diff --check 80d6a16..HEAD` | trailing whitespace in `ceiling_measurement.txt:38` |

## Claim and Source Checks

| # | Claim | Primary source | Result |
|---|---|---|---|
| C1 | Same actor takes the next **actual** second; timestamps are never composed | TS AC-3; `gen_index.event_filename`; tests 501–519 | ❌ The helper adds integer seconds and wraps the date at midnight; the tests label the composed values “actual” |
| C2 | A provider name is rejected as an actor | TS AC-3; EV E13; `validate_event` | ❌ The test only proves filename/body mismatch rejection; `actor: claude` with a matching filename is accepted |
| C3 | Configuration carries the whole identifier grammar | TS §4/AC-2; RF configuration row; both config files | ❌ Both files declare `id_format: "{YYYYMMDD}-{HHMMSS}"`, the bare stamp R3 says is not an identifier |
| C4 | Binding resolution is shipped on Windows | TS AC-4; Who Is Acting blocks | ❌ Six canonical blocks contain control characters instead of `%LOCALAPPDATA%\tfw\bindings.yaml` |
| C5 | Ceiling evidence is regenerated and internally consistent | TS AC-11 F12; EV E16; attachment | ❌ Attachment: 280 + 63 = 343, p95 82; EV: 272 + 63 = 335, p95 83; attachment prose also says 335 |
| C6 | The corpus diff shown under E35 is additions only | EV inline E35 | ❌ The shown baseline command returns 3 `M` paths as well as 33 `A` paths |
| C7 | Every corrective commit used explicit path staging and a checked staged set | EV E48 | ⚠️ Commit contents are scoped, but no persisted command output proves the staging procedure |
| C8 | The corrective RF is represented by current journal state | RF new-files row; task journal | ❌ No R3 handoff/transition follows the 23:33 RF. The old 23:20 legacy handoff still says 43/44, while current EV has 59 items |
| C9 | The result preserves task-locality purpose | master baseline §3.1/§3.2; config build gate; tests | ✅ `--validate` reads local truth; `--check` is an explicit freshness query, not a transition gate |

## Discrepancies Found

1. **F-R2-1 — AC-3's “actual clock” guarantee is contradicted by shipped code and tests.**
   `event_filename()` composes `stamp + step`; at midnight it returns `00:00:00` on the old
   date. This is neither a clock read nor chronological. EV E11 and the “every failure” part
   of E47 therefore do not hold.
2. **F-R2-2 — provider names are not rejected as actors.** The named test creates an actor/
   filename mismatch and never tests a matching provider actor. A direct matching probe is
   accepted with no validation problems, contrary to AC-3 and EV E13.
3. **F-R2-3 — the released configuration still declares the rejected bare-stamp grammar.**
   `.tfw/project_config.yaml:19` and `.tfw/templates/project_config.yaml:23` contradict TS
   AC-2, the resolver, and RF §1's configuration claim.
4. **F-R2-4 — the Windows binding location is corrupted.** Six canonical workflows contain
   TAB and backspace bytes where `\tfw\bindings.yaml` should be; twelve exact adapter copies
   propagate the defect. On Windows, the multi-profile branch cannot follow the documented
   location. EV E19 is contradicted and E18 is only fixture-level.
5. **F-R2-5 — AC-11 F12 is still open.** Ceiling population/count/percentile values disagree;
   E35 and E40 do not reproduce their shown outputs; E38 and E48 lack persistent current
   evidence. The evidence layer overstates both content and procedure.
6. **F-R2-6 — the corrective handoff trace is absent.** The only ready-for-review event is
   the immutable first-pass event claiming 43/44. There is no actual-clock event for the
   current 59-item RF, despite RF §1 claiming this phase's six events each came from a shown
   clock read.
7. **F-R2-7 — three semantic citation applications remain wrong.** ONB §7 rows 1, 2, and 12
   resolve and quote real items but apply them to unrelated approval/status rulings. This is
   the same D43 discrepancy recorded by the historical review and was not corrected.

The owner explicitly approved the current file-budget overrun during this review. It is not a
discrepancy and does not appear in the list above.

## Evidence Verification

| Classification | Evidence items | Reason |
|---|---|---|
| ✅ Verified (46) | E1–E10, E12, E14–E15, E17, E20–E22, E24–E34, E36–E37, E41–E46, E50–E59 | Reproduced by current files, commands, tests, counts, or direct source inspection |
| ⚠️ Partial (5) | E18, E35, E38, E40, E48 | Fixture-only identity behavior; over-broad/incorrect diff output; stale first-pass relation; non-reproducing grep output; unpersisted staging procedure |
| ❌ Contradicted (5) | E11, E13, E16, E19, E47 | Synthetic clock retry; provider actor accepted; wrong population numbers; broken Windows paths; suite does not cover every failure correctly |
| ⏸ Deferred (1) | E23 | Non-specialist observation belongs to TFW-61 under approved TS R3 |
| ⚪ N/A (2) | E39, E49 | Equal-depth clause deleted; transport concern transferred to TFW-61 |

All named attachments exist. Completeness is therefore ✅; sufficiency is ❌.

## Knowledge Citations Verified

All 29 master HL §7.2 citations and five ONB-added items resolve and exist. Priority 0 was
checked against the root guide and North Star purpose/principles/non-goals; priority 1 was
checked separately against the methodology values. PV 2–4 were read fully and PV 5–7 by task
relevance.

| Group | Resolution / existence | Semantic application |
|---|---|---|
| Master HL §7.2 items 1–29 | 29/29 | 29/29 relevant in the master HL |
| ONB §7 applications of those items | 29/29 | 26/29 relevant; rows 1, 2, 12 are unrelated to their cited clauses |
| ONB N1–N5 | 5/5 | 5/5 relevant |

Totals for distinct review applications: **34 resolved, 34 exist, 31 relevant, 3 irrelevant,
0 hallucinated**.

## Checkpoint

**Self-check:**
- [x] Initial sample exceeded `ceil(77 × 0.42)` and discrepancies escalated coverage to all 119 paths.
- [x] Full build/test suite and at least one independent negative probe run.
- [x] Every RF AC checkmark challenged against implementation or primary evidence.
- [x] All 59 EV rows and every attachment audited.
- [x] Project Values 0–4 read fully; 5–7 read by relevance.
- [x] Every HL §7.2 and ONB §7 citation checked for resolution, existence, meaning, and relevance.
- [x] Current Git diff and unrelated working-tree changes checked and preserved.

Stage complete: YES
