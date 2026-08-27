# Verify — "Are the claims true?" (revision 3)
> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **Test:** "If I removed the RF, would the implementation and evidence prove the result?"
> Min verify ratio: 0.42
> RF product census: 77 files; initial minimum: `ceil(77 × 0.42) = 33`
> Coverage: revision 2 verified the complete then-current surface; this review inspected 30/30 second-corrective-iteration paths. Discrepancies therefore triggered 100% coverage of the current iteration.

## Verification Log

| # | Surface | Verification | Actual result | Match |
|---|---|---|---|---|
| V1 | Contract and current specification | Recovered master baseline `c1782b3`; read current Phase HL and approved TS R4 | Purpose and accepted 77-file budget are clear; no frozen-contract change is needed | ✅ |
| V2 | Second corrective delta | Inspected all 30 paths in `86bc963^..32d5974`, including code, tests, evidence, status, event, configs, canonical workflows, and exact copies | All requested edits exist; three material discrepancy classes remain | ❌ result / ✅ coverage |
| V3 | Full tests | Ran `python -m pytest docs/scripts/ -q` | `206 passed, 1 skipped in 166.99s` | ✅ |
| V4 | State and index gates | Ran `gen_index.py --validate` and `--check` before the review transition | 53 tasks validate; index was current and remains non-authoritative | ✅ |
| V5 | Adapter integrity | SHA-256 compared all workflow copies and Codex skills to their declared sources | 22/22 workflow copies and 11/11 Codex skills match; zero drift | ✅ |
| V6 | Clock retry | Read helper/tests and reproduced controlled readings | Every candidate comes from `clock()`; stalled clock is bounded; midnight advances the date | ✅ |
| V7 | Actor validation | Ran matching provider, missing-team, and agent-accountability probes | Providers are refused, but the integrated caller passes `None` for an empty `team/`, accepting `ghost`; the name-only set cannot enforce human `on_behalf_of` | ❌ |
| V8 | Identifier declaration | Checked both config files, resolver, plan, init, conventions, templates, and docs tests | Config and resolver agree on the whole ID; canonical init/artifact instructions still give `{ID}` bare-stamp semantics or duplicate `{title}` | ❌ |
| V9 | Windows binding path | Scanned canonical workflows and exact copies; ran class scanner on its real population | Literal path is present in 7 canonical workflows and 14 copies; 0 control bytes in 921 scanned files | ✅ behavior / ❌ stored count |
| V10 | Journal trace | Parsed all task journal files with the current declared handle | 11 events; five current actor-bearing events validate and six pre-2.0 events are reported as immutable legacy | ✅ |
| V11 | Migration and status | Rechecked snapshot/accounting/status/index results and prior verified implementation | 61 identifiers accounted, 0 unaccounted, 11 task states plus one phase state; current phase is RF before verdict | ✅ |
| V12 | RF/EV/evidence | Audited every EV row and all seven attachments against current commands and Git | 50 verified, 4 partial, 2 contradicted, 1 deferred, 2 N/A; final artifacts still contain old incompatible output | ❌ |
| V13 | Git and scope | Checked current status, commit subjects, per-commit paths, and `git diff --check` | Corrective executor commits are scoped; unrelated dirty TFW-54/55/TECH_DEBT work is untouched; diff check is clean | ✅ |
| V14 | Purpose regression | Re-ran local validation/freshness behavior and read build configuration | A task transition is not forced to rewrite the shared index; the original purpose failure stays closed | ✅ |

## Commands Executed

| # | Command | Result |
|---|---|---|
| 1 | `python -m pytest docs/scripts/ -q` | `206 passed, 1 skipped in 166.99s` |
| 2 | `python docs/scripts/gen_index.py --validate` | `53 tasks validate against the closed schema` |
| 3 | `python docs/scripts/gen_index.py --check` | `index up to date: workspace/00-INDEX.md` before this transition |
| 4 | `git diff --name-only 86bc963^..32d5974` | 30 distinct second-corrective-iteration paths |
| 5 | `git diff --name-status 80d6a16..HEAD` | 129 paths: 77 modified, 52 added |
| 6 | SHA-256 source/copy comparison | 22 workflow copies and 11 Codex skills, zero mismatch |
| 7 | `git diff --check 80d6a16..HEAD` | no output |
| 8 | Integrated empty-`team/` actor probe | production caller value is `None`; a matching `actor: ghost` event returns no validation problem |
| 9 | Agent-accountability probe | `on_behalf_of: worker-one` passes when the only known datum is the handle name; profile type is unavailable |
| 10 | Current control-character scanner population | 921 files scanned, 0 hits; stored RF/control artifact says 116 |
| 11 | `git log --format='%s' 86bc963` filtered for `TFW-N` | 294 task-naming subjects at the evidence's recorded HEAD, not 292; current HEAD has 295 |
| 12 | Unfiltered Task Board sweep | 19 historical/mechanical/guard-test hits, matching the regenerated log |
| 13 | Both `id_format` declarations | `{YYYYMMDD}-{HHMMSS}__{slug}` in live and template config |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|---|
| C1 | Every event candidate is a fresh clock reading | RF §1; EV E11 | `gen_index.event_filename`, controllable-clock tests | ✅ |
| C2 | A provider cannot be an actor and an actor resolves to `team/` | RF §1; EV E13 | validator, production callers, targeted probes | ❌ Provider rule holds; declared-handle rule fails open when the handle set is empty and human accountability is not type-checked |
| C3 | The whole directory name is the identifier everywhere | TS AC-2; RF §1/§3 | configs, `conventions.md`, `init.md`, templates, docs tests | ❌ Configs are fixed, but canonical artifact/init instructions remain internally contradictory |
| C4 | Evidence was regenerated from final commands | RF header/§4; EV header/E16/E35/E47/E48 | current Git, test output, attachments | ❌ Several persisted figures and shown commands are mutually incompatible or predate the final commit |
| C5 | The Windows path is literal and no control character remains | RF §1; EV E19 | seven canonical workflows, fourteen copies, integration scanner | ✅ Behavior holds; the stored population count does not |
| C6 | The corrective RF has a current actual-clock handoff | RF §1; measurement log | `journal/20260827-043340__handoff__saubakirov.md` | ✅ |
| C7 | The result serves task locality and resumability | master baseline §3.2; NS1; build/index behavior | local status validation and non-blocking derived index | ✅ |

## Discrepancies Found

1. **F-R3-1 — identity validation is fail-open and loses the profile type.**
   `team_handles()` returns names only, and both production callers use
   `team_handles(root) or None`. With no declared profile, `None` disables membership checks
   and an actor named `ghost` validates. Because the profile type is discarded, an agent
   handle also validates as `on_behalf_of`, contrary to AC-3's “always a human handle.” The
   direct unit tests inject a non-empty set and therefore do not exercise either production
   failure.
2. **F-R3-2 — the full-ID and actor-bearing grammars are not propagated through the canonical
   release surface.** `.tfw/workflows/init.md:126-127` still defines `{ID}` as the bare clock
   and then appends `__tfw_init`; `.tfw/conventions.md:303-309` appends `{title}` to `{ID}` even
   though line 317 says `{ID}` is the whole identifier; the same file's lines 422-423 still
   show actorless event names. An agent following the shipped init/convention path can put a
   bare stamp into `status.md`, double the slug in artifact names, or copy the superseded
   journal grammar. The docs tests happen to use the correct one-slug filenames, exposing the
   contradiction rather than resolving it.
3. **F-R3-3 — AC-13 item 5 and the R4 countability DoF are still open.** Examples:
   EV E35 says `40 A / 4 M`, while its own inline block still says “additions only” and the
   current command is `42 A / 4 M`; EV still labels TS revision 3 and prints the old
   `190 passed` run; RF/control evidence says 116 scanned files while the shipped test scans
   921; the ceiling population says 292 task-naming subjects while the recorded HEAD has 294
   and current HEAD has 295; E48 omits the final executor commit; and `measurement_log.txt`
   declares `HEAD=86bc963` while containing the later 04:33 handoff. The underlying tests are
   green, but the evidence offered as final is not a single reproducible snapshot.
4. **F-R3-4 — three ONB citation applications remain semantically irrelevant.** All sources
   resolve and exist, but ONB §7 rows 1, 2, and 12 apply resumability, task-locality, and D37
   to unrelated approval/status answers. Approved TS R4 deliberately preserves the ONB and
   records the defect in RF observation 12. It is therefore disclosed historical trace rather
   than a concealed implementation claim, but it is not a semantic pass.

## Evidence Verification

| Classification | Evidence items | Reason |
|---|---|---|
| ✅ Verified (50) | E1–E9, E11–E15, E17–E22, E24–E34, E36–E37, E40–E46, E50–E59 | Reproduced by current tests, files, counts, or direct source inspection |
| ⚠️ Partial (4) | E10, E38, E47, E48 | Name separation is not end-to-end declared-actor validation; link evidence masks canonical placeholder inconsistency; “every named failure” omits integrated identity cases; staging log omits the final executor commit and does not persist the staged-set comparison |
| ❌ Contradicted (2) | E16, E35 | The stated population does not reproduce at its recorded HEAD; E35's row, inline output, and current command disagree |
| ⏸ Deferred (1) | E23 | Non-specialist observation belongs to TFW-61 under approved S43 |
| ⚪ N/A (2) | E39, E49 | Equal-depth clause deleted; transport concern transferred to TFW-61 |

All numbered rows and attachments exist, so evidence completeness is ✅. Their final-state
agreement and ability to establish the claims is ❌.

## Knowledge Citations Verified

PV priorities 0–4 were read in full and priorities 5–7 by relevance. Current master HL §7.2
contains 29 citations; ONB adds N1–N5.

| Group | Link resolution | Item existence / meaning | Application relevance |
|---|---|---|---|
| Master HL §7.2 items 1–29 | 29/29 | 29/29 | 29/29 |
| ONB applications of items 1–29 | 29/29 | 29/29 | 26/29; rows 1, 2, 12 are irrelevant |
| ONB N1–N5 | 5/5 | 5/5 | 5/5 |

Distinct references: **34 resolved, 34 exist, 31 ONB applications relevant, 3 historically
irrelevant, 0 hallucinated.** RF observation 12 and TS R4 make the disposition explicit; the
old ONB itself remains immutable.

## Checkpoint

**Self-check:**
- [x] Verification exceeded `ceil(77 × 0.42)` and covered 30/30 current-iteration paths after discrepancies.
- [x] Full test/build gate and independent negative probes executed.
- [x] Every RF AC claim challenged against current implementation or evidence.
- [x] All 59 evidence rows and every attachment audited.
- [x] PV priorities 0–4 read fully and 5–7 by relevance.
- [x] Every HL §7.2 and ONB §7 citation checked for resolution, existence, meaning, and relevance.
- [x] Current Git diff and unrelated working-tree state checked and preserved.

Stage complete: YES
