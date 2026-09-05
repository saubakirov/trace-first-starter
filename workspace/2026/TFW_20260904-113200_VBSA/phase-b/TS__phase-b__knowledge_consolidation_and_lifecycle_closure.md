# TS — TFW_20260904-113200_VBSA / Phase B: Knowledge consolidation and lifecycle closure

> **Date**: 2026-09-05
> **Author**: Codex (Coordinator)
> **Status**: ✅ APPROVED — saubakirov, 2026-09-05
> **Parent HL**: [HL-TFW_20260904-113200_VBSA](../HL-TFW_20260904-113200_VBSA.md) — `🔒 FROZEN`, including approved/applied A11 at `ac0b12374892b8ad69f2cdeb4b16a4f93d7c1893`
> **Phase HL**: [HL__phase-b__knowledge_consolidation_and_lifecycle_closure](HL__phase-b__knowledge_consolidation_and_lifecycle_closure.md) — derivation-only
> **Accounting Baseline**: `9221dbb659a6b631dca3540b6be38d2a95208858`

> **Approval record**: Owner `saubakirov` approved this complete bounded plan through the latest explicit verdict, recorded at `2026-09-05T11:40:22+05:00` and relayed by Main Coordinator task `01a06b11-b421-74f3-a8da-6008f88ab38e`: «просмотрел, мне всё нравится… переходи к следующей фазе… до конца автономно». The verdict applies only to the scope and boundary below.
> **Immutable owner-approved denominator**: `1` logical touched VALUE file and `5` touched text LOC (`4` additions + `1` deletion). It never ratchets.

---

## 1. Objective

Publish the final approved Phase A value-bearing accounting result into the single root `KNOWLEDGE.md`, then leave no VALUE work for the post-review knowledge gate. The accepted document must update the current configuration description, add D76, add the Phase A key-artifact/result row, and mark the former four-key whole-diff budget as legacy/deprecated while preserving every historical trace and closing Phase B, Phase A, and the root task only through canonical lifecycle transitions.

## 2. Scope

### In Scope

- Modify exactly one existing VALUE path: root `KNOWLEDGE.md`.
- Replace exactly the current one-line §1 `Config` row and add exactly one one-line row to §1, §2, and §3.
- Ground every statement in Phase A RF, final REVIEW, EV, approved master HL, and the accepted Phase A refs.
- Create/update only required task-local Phase B, Phase A, and root lifecycle, handoff, evidence, review, marker, and journal traces.
- Fix and independently replay a tested Phase B Candidate before EV/RF/REVIEW; keep `KNOWLEDGE.md` unchanged after Candidate unless a new Candidate and full review round are produced.

### Out of Scope

- Any second VALUE path; any §4, `knowledge/*.md`, topic-index, conventions, glossary, workflow, template, config, adapter, code, test, generated mirror, release, migration-file, or documentation-site change.
- Any modification of the Phase A Candidate, Candidate membership, approved Phase A artifacts other than post-review TRACE markers/state, historical task artifacts, Git history, `master`, or remotes; no push.
- Rewriting, deleting, renumbering, or normalizing prior master-HL amendments or Phase A traces.
- New facts or Fact Candidates: this phase combines already approved explicit sources and creates no `tfw-knowledge` topic content.
- A lifecycle exception, retrospective approval, second reviewer/executor session in the first round, fork, agent copy, or research session.

## 3. Principles Check

| # | Master HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Name the governed object before measuring it | AC-1 / AC-4 | Literal `KNOWLEDGE.md` selector and four exact row effects |
| P2 | Semantic role over location | AC-1 | `KNOWLEDGE.md` is VALUE because it is the accepted output; all TFW files remain TRACE |
| P3 | One measurement, one reference pair | AC-4 | Baseline `9221dbb...`, one tested Candidate, and two NUL-safe Git commands |
| P4 | Trace integrity without trace taxation | AC-4 / AC-5 | Phase/root state and evidence remain mandatory but outside the selector |
| P5 | Assurance is not product scope | AC-4 | Read-only checks and review add no maintained ASSURANCE VALUE path |
| P6 | Structural enforcement | AC-1–AC-5 | Exact Git membership/arithmetic plus source and lifecycle replay |
| P7 | Domain-agnostic by construction | AC-2 | D76 states semantic accepted-output rules, not a code-only case |
| P8 | No shadow total | AC-4 | No numerical budget for TRACE/ASSURANCE/DERIVED |
| P9 | History is evidence | AC-2 / AC-3 | Phase A refs and former four-key semantics are cited, never rewritten |
| P10 | Saint-Exupéry Principle | AC-1 / AC-3 | Four one-line edits in the one existing authority; no second carrier |
| P11 | Decomposition signals, not size verdicts | AC-2 / AC-4 | 50/5,000 are soft prompts with a keep-one-phase disposition |
| P12 | Bounded growth authority | AC-4 | Immutable 1/5 denominator; owner at ≥2 files, ≥10 LOC, or any protected/membership change |

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `KNOWLEDGE.md` | MODIFY | `VALUE` | The accepted Phase B product: one current Config row, D76, one Phase A key-artifact/result row, and one legacy/deprecation row |
| `workspace/2026/TFW_20260904-113200_VBSA/HL-TFW_20260904-113200_VBSA.md` | MODIFY | `TRACE` | Approved A11 and re-freeze record; already committed before TS execution |
| `workspace/2026/TFW_20260904-113200_VBSA/phase-b/**` | CREATE / MODIFY | `TRACE` | Phase plan, local state/journal, ONB, RF, EV, review stages, REVIEW, markers, and close |
| `workspace/2026/TFW_20260904-113200_VBSA/phase-a/status.md`, `workspace/2026/TFW_20260904-113200_VBSA/phase-a/journal/**`, `workspace/2026/TFW_20260904-113200_VBSA/phase-a/REVIEW__phase-a__value_bearing_budget_contract_and_adoption.md` | MODIFY / CREATE | `TRACE` | Apply post-review docs/knowledge markers and legal `KNW → DONE` closure without moving Phase A Candidate |
| `workspace/2026/TFW_20260904-113200_VBSA/status.md`, `workspace/2026/TFW_20260904-113200_VBSA/journal/**` | MODIFY / CREATE | `TRACE` | Root `PHASES → DONE` closure only after both phases are terminal |

No narrower selector, mixed-role path, maintained ASSURANCE path, or accepted DERIVED output is planned. `KNOWLEDGE.md` is wholly VALUE for the fixed Baseline→Candidate diff; freehand line subtraction is prohibited.

### Prospective accounting contract

| Fact | Approved Phase B value |
|---|---|
| Subject / exact VALUE selector | Only changed path `KNOWLEDGE.md`; literal `$valuePaths = @('KNOWLEDGE.md')` |
| Baseline / selector source | Immutable Phase A APPROVE commit `9221dbb659a6b631dca3540b6be38d2a95208858`; this TS at its owner-approval commit resolved through phase state/journal and Git |
| Candidate rule | First tested Executor commit containing the complete `KNOWLEDGE.md` result, before EV/RF/REVIEW/final transition; excluded-only later writes do not move it; later VALUE requires a new Candidate and recomputation |
| Logical VALUE files | Planned `1`; one existing modified file; rename = one but no rename is planned |
| Touched text LOC | Planned `4` additions + `1` deletion = `5`; one Config-row replacement plus three added table rows; numeric numstat fields; binary/non-text = per-file N/A |
| Triggers / disposition | Project prompts are `50` logical VALUE files and `5,000` touched text LOC. **Keep one phase**: 1/5 crosses neither; all four statements form one coherent authority, splitting one file adds ceremony and permits a contradictory intermediate state. Cause: legal Phase A knowledge closure; cost: one file/five LOC plus required TRACE; assurance: exact source/Git/review replay; authority: owner-approved A11 and this TS; terminal pre-work verdict: keep Phase B whole |
| Multiplier / authority | `2`; immutable denominator `1/5`; owner before work at `≥2` logical VALUE files or `≥10` touched text LOC, from applicable planned zero, for any other VALUE membership, or for any protected-boundary change. Coordinator may prospectively rule only necessary same-result wording growth within the same one-file/four-row contract and strictly below 10 LOC |
| Approval epoch / failure | Exact owner verdict in the header and `journal/20260905-114022__dispatch__c3e4.md`; missing/mutable/mismatched/late = `BLOCKED`; metric-only N/A; unresolved phase attribution = `INVALID`; `DEFERRED` is non-terminal |

```powershell
$valuePaths = @('KNOWLEDGE.md')
git diff --name-status --find-renames=50% -z 9221dbb659a6b631dca3540b6be38d2a95208858 <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z 9221dbb659a6b631dca3540b6be38d2a95208858 <CANDIDATE_SHA> -- $valuePaths
```

### Prospective scope rulings

The owner-approved initial ruling is the exact 1-file/5-LOC plan above; no growth ruling exists. The four one-line edits are the Saint-Exupéry minimum that preserves purpose, value, correctness, authority, inspectability, and continuation. Before any wording growth, the Executor stops. The Coordinator may approve only necessary same-result growth below 10 LOC with unchanged literal membership and protected boundary, recording cause, cost, assurance effect, split alternative, Saint-Exupéry judgment, authority, verdict, and pre-work ref. A second VALUE file, another membership/section, ≥10 LOC, or protected-boundary movement routes to owner `saubakirov` through the Main Coordinator before work.

#### R1 — context-ceiling-preserving same-file subtraction (2026-09-05)

**Cause:** the first tested Candidate `1b336e1257a87e6552090f549cfa3381614ec6d2` reproduced the approved 1-file/5-LOC result, but the tracked assurance suite reported `560 passed, 1 skipped, 2 failed`; both failures were immutable `/tfw-plan` context-ceiling assertions (`24,935 > 24,730`), and the `+207` contribution was the newly required §1 Config/D76 content. **Cost:** replace the adjacent existing one-line D75 row with a shorter one-line form while preserving its decision, metrics, and authoritative links; the replacement Candidate remains exactly one VALUE path and is expected to measure `5` additions + `2` deletions = `7` touched text LOC. Actual work is authorized only strictly below the owner boundary: one VALUE file and at most `9` touched text LOC. **Assurance effect:** the Executor must rerun the full tracked suite and all AC/accounting/link/protected-boundary checks; both context-ceiling tests must be green before the replacement Candidate. **Split alternative:** a second carrier or phase would duplicate authority and cannot reduce the context graph; changing the ceiling/test/canonical reader is out of scope. **Saint-Exupéry judgment:** same-file subtraction is the smallest change that preserves the accepted result and its executable guard. **Authority:** prospective Coordinator ruling relaying Main Coordinator task `01a06b11-b421-74f3-a8da-6008f88ab38e`, before any D75 edit, recorded in `journal/20260905-121000__ruling__eeb8.md`. **Verdict:** `APPROVE` only for the bounded D75 replacement described here. If D75's decision, metrics, or links cannot be preserved, if the suite remains red, or if actual accounting reaches `10` LOC, a second VALUE path, another section, or a protected-boundary change, stop and route to the owner. The first Candidate is superseded and must not be reviewed; after this ruling the Executor creates one replacement Candidate and performs the complete evidence/RF replay. This R1 supersedes only the TS's exact four-row/`4 + 1 = 5` assertions for the replacement Candidate; the required Config, D76, §2, §3 effects, immutable owner-approved denominator, and every other boundary remain unchanged.

### Task-local hard constraint — HC-1 (M1–M6)

| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| A second VALUE carrier, Phase A rewrite, or extra knowledge section would invalidate the accepted one-file closure or create competing durable authority | Literal VALUE membership `KNOWLEDGE.md`; within it only the existing §1 Config row and new D76/§2/§3 rows; all code, test, workflow, template, conventions, glossary, config, adapters, generated mirrors, §4/topic files, Phase A Candidate, history, `master`, remotes | VALUE membership exactly one M record for `KNOWLEDGE.md`; touched LOC exactly 4+1=5 unless prospectively ruled below 10; zero protected-path changes; diff hunks confined to four table rows | Before every non-TRACE write and Candidate commit, compare intended and actual diff to the literal selector, four-row contract, 1/5 plan, and protected set; stop on first mismatch | Disclosure or review after work cannot prevent Candidate invalidation, authority duplication, or an irreversible history/boundary change; file/LOC prompts alone cannot identify a tiny prohibited edit | Coordinator only for necessary same-result LOC growth strictly below 10 in the same membership/boundary; owner `saubakirov` prospectively through Main Coordinator for any other relaxation, ≥2 files, ≥10 LOC, membership/section change, or protected-boundary change |

**Actions (not budget dimensions):** 1 modified VALUE file; 0 created VALUE files; 0 maintained ASSURANCE files; required TRACE files created/modified under the exact selectors above.

**Immutable owner-approved denominator:** 1 logical touched VALUE file and 5 touched text LOC; never ratchets.

## 5. Acceptance Criteria

### AC-1: One exact VALUE diff

The Phase B Candidate modifies only `KNOWLEDGE.md` as VALUE and has exactly four semantic row effects.
- [ ] The existing §1 `Config` row is replaced once, with no duplicate `Config` row.
- [ ] Exactly one D76 row, one `TFW_20260904-113200_VBSA/A` §2 row, and one four-key legacy §3 row are added.
- [ ] Baseline→Candidate name-status is exactly one `M` record for `KNOWLEDGE.md`; numstat is exactly 4 additions and 1 deletion; no binary N/A.
- [ ] No other `KNOWLEDGE.md` line or section changes; §4 is byte-identical to Baseline.

Gate: NUL-safe Git replay from `9221dbb...` against the tested Candidate plus an exact four-hunk/row-key comparison.

Evidence: Full — one EV accounting row records approval ref, Baseline, Candidate, literal membership, 4+1 arithmetic, timing, trigger/authority result, and exact commands.

### AC-2: Current Config and D76 are exact [depends: AC-1]

Section 1 states the accepted prospective model without weakening Phase A.
- [ ] The `Config` row names `decomposition_trigger_files: 50` and `decomposition_trigger_loc: 5000` as soft prompts over VALUE and `owner_escalation_multiplier: 2` as the delegated-authority ceiling; key files resolve.
- [ ] D76 states semantic `VALUE` accounting, the four classes, fixed Baseline→Candidate selector contract, two universal measures, excluded-only Candidate invariance, prospective bounded Coordinator authority, immutable denominator, and owner escalation at/above the multiplier or from planned zero.
- [ ] D76 links to the Phase A RF, final REVIEW, and EV; each link resolves and semantically supports the attached statement.
- [ ] D76 introduces no new key, metric, manifest, registry, ledger, script, lifecycle exception, or alternate authority.

Gate: Semantic comparison against Phase A RF §§1–2, REVIEW §§17–20, EV Pass 2, master HL §§3/5/7, and current config/conventions.

Evidence: Full — independent source-to-row matrix with resolved paths and cited facts.

### AC-3: Phase A result and legacy model are preserved [depends: AC-2]

Sections 2 and 3 make the accepted result and superseded model continuable.
- [ ] The §2 Phase A row identifies approval `9221dbb...`, approved TS `36e50e4...`, Baseline `f5a96af...`, final Candidate `59c73bf...`, 29 VALUE files, 663 additions + 321 deletions = 984 touched text LOC, two ASSURANCE paths, no membership deviation, and final APPROVE.
- [ ] The §3 row names all four former whole-diff keys: `max_files_per_phase`, `max_new_files`, `max_loc`, `max_modified_files`; marks the model deprecated/replaced for prospective work; maps files/LOC to the new decomposition keys; retires the two redundant sublimits; adds multiplier 2; and preserves historical approved semantics.
- [ ] Both rows link to authoritative Phase A artifacts and D76; no source or old artifact is edited.

Gate: Exact fact replay from Phase A RF §§1.2/§4.2, final REVIEW §§17–23, EV E-accounting/Pass 2, and master-HL A9–A11.

Evidence: Full — Reviewer reopens every cited source and rejects any mismatched SHA, total, status, mapping, or semantic claim.

### AC-4: Accounting, authority, and protected boundaries hold [depends: AC-1] [depends: AC-3]

The result obeys the accounting model it records.
- [ ] The approved selector source resolves from the Phase B state/journal and is immutable; Candidate is the first tested Executor VALUE commit and precedes EV/RF/REVIEW.
- [ ] Planned and actual membership are the same one path; 1/5 is below 50/5,000 and below owner boundaries 2/10; keep-one-phase disposition remains justified.
- [ ] Baseline→Candidate changes outside the one VALUE path are only declared current-task TRACE; no ASSURANCE or DERIVED maintained path appears.
- [ ] Every HC-1 protected path has zero changes; Phase A Candidate and Git history remain unchanged; no push occurs.
- [ ] Candidate→review and Candidate→final closure have zero `KNOWLEDGE.md` changes unless a replacement Candidate and full review round exist.

Gate: Full Git lineage, name-status/numstat, protected-selector, `git diff --check`, and project-structure replay before RF and independently in review.

Evidence: Full — EV includes raw refs, arithmetic, timing, selector equality, protected count, and trigger/authority verdict.

### AC-5: Post-review closure has no lifecycle exception [depends: AC-4]

The complete VALUE result exists before review, so closure requires only legal TRACE transitions.
- [ ] Executor acceptance records `TS_DRAFT → ONB`; completion records `ONB → RF`; Reviewer records `RF → REV` and, only on APPROVE, `REV → KNW` with paired phase-local state/journal writes.
- [ ] Phase B REVIEW names `/tfw-docs` Applied because the exact §1–§3 result is already in Candidate, and `/tfw-knowledge` N/A because RF/REVIEW contain no Fact Candidates; applying markers creates no second VALUE diff.
- [ ] After markers, Phase B records `KNW → DONE`; Phase A applies its pending docs marker, keeps knowledge N/A, and records `KNW → DONE`; root records `PHASES → DONE` only after both phase statuses are terminal.
- [ ] Every status transition is permitted, ordered, and paired with an immutable current-form journal event; terminal statuses carry outcomes; no task-level rollup duplicates phase state.

Gate: Status/journal/template validation, Candidate→HEAD VALUE invariance, `python .tfw/scripts/gen_index.py --knowledge-pending --format json`, and project/task checks within their known-baseline limits.

Evidence: Full for Candidate and review route; final post-review TRACE closure is verified by the Coordinator from the terminal state/journal and reported to the Main Coordinator.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-b__knowledge_consolidation_and_lifecycle_closure.md` | Source matrix, exact one-file accounting row, protected-boundary/timing replay, lifecycle evidence, and verdict |

## 6. Technical Guidance

- Preserve the existing one-line Markdown table style so the approved four-row change remains exactly 4 additions + 1 deletion; wording may be concise but must retain every AC fact.
- Use relative artifact links from root `KNOWLEDGE.md` and verify both resolution and semantic relevance.
- Treat `9221dbb...` as Phase B Baseline and `59c73bf...` only as the Phase A result being recorded.
- Retake every SHA, count, and arithmetic result immediately before RF and place raw output in EV; do not type figures from memory.
- Commit only explicit Phase B paths after reading full `git status`; shared worktree state must never be swept into this task.

## 7. Definition of Failure

- ❌ Any second VALUE file, different VALUE membership, §4/topic-file write, or protected-path change occurs without prospective owner approval.
- ❌ Candidate differs from the tested Executor VALUE commit, moves because TRACE is written, or is created after EV/RF/REVIEW.
- ❌ Actual `KNOWLEDGE.md` diff is not exactly one Config replacement plus D76/§2/§3 additions, or does not reproduce 4 additions + 1 deletion without a valid prospective ruling.
- ❌ A Config/D76/result/legacy claim conflicts with Phase A RF, final REVIEW, EV, master HL, or current canonical config/conventions.
- ❌ Phase A Candidate/history is rewritten, master/remote is changed, or any push occurs.
- ❌ A lifecycle state is skipped, summarized at task level, written without its paired journal event, or closed before required review/markers.
- ❌ `/tfw-docs` or `/tfw-knowledge` attempts a second VALUE diff, topic-file/§4 write, convention change, or another carrier.
- ❌ The same session implements and reviews, an extra Executor/Reviewer/Researcher is created in the first round, or a role writes a forbidden artifact.

**On failure:** stop before the out-of-bound act. Report the exact divergence to the Coordinator; route ≥2 VALUE files, ≥10 LOC, any membership/section/protected-boundary change, or canonical-workflow incompatibility to owner `saubakirov` through the Main Coordinator. Do not raise a ceiling, rewrite Phase A, or close by exception.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| A long one-line decision row invites an accidental wrap and LOC drift | Treat one-line table serialization as part of AC-1 and verify exact numstat before Candidate |
| Generic wording loses the authority or Candidate rule | Use the AC-2 source matrix and independent semantic review rather than keyword presence alone |
| Phase A and Phase B refs are conflated | Label Phase B Baseline, Phase A TS approval, Phase A Baseline, Phase A Candidate, and Phase A APPROVE separately |
| Post-review workflow assumes it must write KNOWLEDGE again | The Candidate already contains the docs output; post-review applies/verifies markers only and hard-stops on a second VALUE diff |
| Closing three scopes produces illegal state order | Read each local status before acting and apply phase/root transitions separately with paired events |
| Shared worktree changes are accidentally staged | Use explicit-path commits only and compare staged paths to the phase-owned list before every commit |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `KNOWLEDGE.md` | Phase A REVIEW proposed but did not modify it | Phase B exclusively owns the prospective VALUE edit; Phase A Candidate remains immutable |
| `workspace/2026/TFW_20260904-113200_VBSA/phase-a/status.md` and phase-a journal/REVIEW markers | Phase A | Post-review TRACE closure only; no Phase A implementation or accounting change |
| `workspace/2026/TFW_20260904-113200_VBSA/HL-TFW_20260904-113200_VBSA.md`, root status, and root journal | Task root | A11/re-freeze and final task closure are TRACE; no competing phase-state rollup is permitted |

---

*TS — TFW_20260904-113200_VBSA / Phase B: Knowledge consolidation and lifecycle closure | 2026-09-05*
