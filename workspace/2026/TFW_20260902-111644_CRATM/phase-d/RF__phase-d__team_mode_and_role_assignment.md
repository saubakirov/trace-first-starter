# RF — TFW_20260902-111644_CRATM / Phase D: Team mode and Role Assignment

> **Date**: 2026-09-06
> **Author**: saubakirov (Codex Executor)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL Phase D](HL__phase-d__team_mode_and_role_assignment.md)
> **TS**: [TS Phase D](TS__phase-d__team_mode_and_role_assignment.md)

---

## 1. What Was Done

Phase D now defines provider-neutral Agent Team mode, a frozen six-column Role Assignment contract, exact boundary and return behavior, four workflow consumer checkpoints, and a bounded Codex native profile. The implementation preserves existing CL/AG authority, Role Locks, approval gates, hard stops, copy parity, and predecessor contracts.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `6a7ede0549dca272c149b0294a972c013d5cb291` (2026-09-06T17:30:57+05:00) |
| Baseline / Candidate | `8e68ab37d300122ff110500ad58f354f76b6210f` / `9edbebcf68872a72a9274765ad053e8d25fa66ac` |
| VALUE membership | `.tfw/conventions.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.tfw/templates/HL.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.tfw/workflows/plan.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.tfw/workflows/handoff.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.tfw/workflows/review.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.tfw/workflows/research/base.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.tfw/adapters/codex/AGENTS.md.template` — MODIFY / VALUE / approved literal Phase D selector member<br>`AGENTS.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.agent/workflows/tfw-plan.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.agent/workflows/tfw-handoff.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.agent/workflows/tfw-review.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.agent/workflows/tfw-research.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.claude/commands/tfw-plan.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.claude/commands/tfw-handoff.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.claude/commands/tfw-review.md` — MODIFY / VALUE / approved literal Phase D selector member<br>`.claude/commands/tfw-research.md` — MODIFY / VALUE / approved literal Phase D selector member |
| Arithmetic | 180 additions + 423 deletions = 603 touched text LOC; 16 logical files; binary/non-text N/A |
| Membership deviations | None. Actual VALUE membership exactly equals the approved literal sixteen-path selector. |
| Trigger disposition | `KEEP_ONE_PHASE`: required contract and assurance fit the approved selector and limits; 16 files and 603 touched LOC require neither split nor escalation. |
| Authority and timing | The owner-approved denominator was immutably fixed at approval as 16 files / 640 touched LOC (420 additions + 220 deletions). Approval commit `6a7ede0549dca272c149b0294a972c013d5cb291` predates ONB and implementation. Actual `16 < 32`, `603 <= 640`, and `603 < 1280`; no growth, multiplier, or planned-zero trigger occurred, so no prospective scope ruling was required. |
| Reproduction | Raw byte output from `git diff --name-only -z <Baseline> <Candidate> -- <literal selector>` and `git diff --numstat -z <Baseline> <Candidate> -- <literal selector>` was independently split on NUL. It reproduced 16 names, 16 numeric rows, identical membership, and `180 + 423 = 603`. |

This reports the approved contract; it does not create a selector, move Candidate, ratchet the denominator, or supply late authority.

### New Files

| File | Description |
|---|---|
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/ONB__phase-d__team_mode_and_role_assignment.md` | Executor onboarding, authority binding, scope, risks, and unblocked execution decision |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/journal/20260906-180030__transition__ef60.md` | Immutable `TS_DRAFT` to `ONB` transition |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/evidence/EV__phase-d__team_mode_and_role_assignment.md` | Per-AC evidence record and final evidence verdict |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/evidence/phase-d-accounting.json` | Selector, per-path accounting, NUL-safe replay, lineage, thresholds, and counts |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/evidence/phase-d-byte-parity.json` | Workflow receiver and managed-block SHA-256 parity |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/evidence/phase-d-census.json` | Classified live-source occurrence and provider-leak census |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/evidence/phase-d-context.json` | Corpus, route, central-range, and workflow-local measurements |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/evidence/phase-d-mutants.json` | Forty-five independent output-changing mutant results |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/evidence/phase-d-native-profile.json` | Native task/worktree/direct-route field trace and evidence limitation |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/evidence/phase-d-protected.json` | Protected Baseline blob, Phase E absence, and root outside-block checks |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/evidence/phase-d-scenarios.json` | Extracted records, fixtures, and seventeen expected/actual scenarios |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/evidence/phase-d-test-output.txt` | Raw relevant command, exit, suite, MkDocs, and diff-check results |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/RF__phase-d__team_mode_and_role_assignment.md` | Executor result report bound to the immutable Candidate |

### Modified Files

| File | Changes |
|---|---|
| `.tfw/conventions.md` | Added exact AT declaration, row activation, duties, seven returns, degradation, lifecycle-boundary, dispatch, and native-profile admission rules. |
| `.tfw/templates/HL.md` | Added the frozen six-column Role Assignment section and its approval/activation constraints. |
| `.tfw/workflows/plan.md` | Added Role Assignment declaration/validation and approved-row dispatch checkpoint. |
| `.tfw/workflows/handoff.md` | Added Executor row resolution, direct reporting, and same-role continuation checkpoint. |
| `.tfw/workflows/review.md` | Added Reviewer row resolution, direct verdict/proposal reporting, and same-role continuation checkpoint. |
| `.tfw/workflows/research/base.md` | Added Researcher row resolution, direct WAIT/RES reporting, and same-role continuation checkpoint. |
| `.tfw/adapters/codex/AGENTS.md.template` | Replaced the managed block with the bounded Codex-native Agent Team profile. |
| `AGENTS.md` | Synchronized the Codex managed block while preserving every byte outside its markers. |
| `.agent/workflows/tfw-plan.md` | Synchronized the canonical Plan workflow. |
| `.agent/workflows/tfw-handoff.md` | Synchronized the canonical Handoff workflow. |
| `.agent/workflows/tfw-review.md` | Synchronized the canonical Review workflow. |
| `.agent/workflows/tfw-research.md` | Synchronized the canonical Research workflow. |
| `.claude/commands/tfw-plan.md` | Synchronized the canonical Plan workflow without changing the Claude adapter profile. |
| `.claude/commands/tfw-handoff.md` | Synchronized the canonical Handoff workflow without changing the Claude adapter profile. |
| `.claude/commands/tfw-review.md` | Synchronized the canonical Review workflow without changing the Claude adapter profile. |
| `.claude/commands/tfw-research.md` | Synchronized the canonical Research workflow without changing the Claude adapter profile. |
| `docs/scripts/test_runtime_context.py` | Added source-derived Phase D contract, scenario, mutation, accounting, census, and context assurance. |
| `docs/scripts/test_integration.py` | Added copy parity, managed-block preservation, provider-boundary, protected-path, and integration checks. |
| `workspace/2026/TFW_20260902-111644_CRATM/phase-d/status.md` | Advanced the approved phase from `TS_DRAFT` to `ONB`; final RF transition follows this report. |

## 2. Key Decisions

1. Kept canonical authority provider-neutral: AT entry and row activation are separate, and no profile, title, identity field, binding, or provider operation grants authority.
2. Confined Codex operation names and native mechanics to the adapter managed block; canonical workflows consume the neutral contract and all eight receiver copies remain byte-identical.
3. Preserved the approved sixteen-file VALUE selector and immutable `16/640` comparison denominator. Actual implementation is smaller at `16/603`, so no retrospective denominator change or prospective scope ruling is needed.
4. Fixed Candidate before EV/RF at `9edbebcf68872a72a9274765ad053e8d25fa66ac`; later commits contain TRACE evidence only and do not move Candidate.
5. Implementation deviations: none in scope or membership. An initial pre-Candidate full-suite run exposed nine legacy-anchor regressions; the prior source-derived anchors were restored without weakening expectations, then the complete suite passed before Candidate was fixed.

## 3. Acceptance Criteria

- [x] AC-1 — Exact AT entry, duties, seven returns, degradation, and eight-step neutral admission gate are implemented and source-derived tests pass.
- [x] AC-2 — Role Assignment and frozen-row autonomy are unambiguous across same-unit lifecycle, gate, amendment, and refusal cases.
- [x] AC-3 — Dispatch plus Plan, Handoff, Research, and Review are real consumers with direct same-role returns and preserved Role Locks.
- [x] AC-4 — The Codex profile is native, bounded, directly routed, independently addressable, provider-local, and explicitly makes no G8 reliability claim.
- [x] AC-5 — Consumers, copies, protected predecessors, provider boundaries, real MkDocs build, and the complete configured suite remain coherent.
- [x] AC-6 — Baseline/Candidate timing, VALUE membership, arithmetic, caps, ancestry, and exact NUL-safe replay are reproducible from immutable objects.

## 4. Verification

- Lint (`git diff --check`): PASS; exit 0 with no output.
- Targeted tests (`python -m pytest docs/scripts/test_runtime_context.py -q -k phase_d`): PASS; 5 passed, 179 deselected in 3.84s.
- Tests (`python -m pytest .tfw/scripts/ docs/scripts/ -q`): PASS; 655 passed, 1 skipped in 341.96s. The integration fixture executed the real `python -m mkdocs build --config-file docs/mkdocs.yml` build.

## 5. Evidence

See [EV file](evidence/EV__phase-d__team_mode_and_role_assignment.md) for evidence details.

Evidence verdict: 7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | `.tfw/scripts/gen_index.py` | 746 | todo | The current event reader's closed `EVENT_KEYS` omits template-valid `writer`; consequently `python .tfw/scripts/gen_index.py --check tasks` reports `unknown keys: writer` for existing Phase B–D events, including the new template-conforming RF transition. Runtime changes are outside the approved Phase D selector and explicitly prohibited by the TS. |
| 2 | `workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md` | 9 | style | The pre-existing 123-code-point summary exceeds the current 120-code-point event ceiling, which is the other actionable failure reported by `--check tasks`; the immutable historical event was not rewritten. |

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

---

*RF — TFW_20260902-111644_CRATM / Phase D: Team mode and Role Assignment | 2026-09-06*
