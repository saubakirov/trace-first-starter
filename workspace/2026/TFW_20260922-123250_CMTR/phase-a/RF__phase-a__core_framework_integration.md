# RF — TFW_20260922-123250_CMTR / Phase A: Core Framework Integration & Coordination Guidance

> **Current filename**: `RF__phase-a__core_framework_integration.md`

> **Date**: 2026-09-22
> **Author**: Executor (Antigravity)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW_20260922-123250_CMTR](../HL-TFW_20260922-123250_CMTR.md)
> **TS**: [TS Phase A](TS__phase-a__core_framework_integration.md)
> **Producer unit**: antigravity:thread:local:59016b7c-b3c7-4452-81d0-4dc65405e6d9
> **Parent Coordinator**: antigravity:thread:local:3d06f6f4-0f5b-415d-aff2-f70c8f1acdcc
> **Activation / dispatch source**: owner-direct: saubakirov via `/tfw-handoff cmtr`
> **Coordination authority**: `../HL-TFW_20260922-123250_CMTR.md @ 9cb04a4cc3c1fc2d3f3fef9e395798d60667ef47`
> **Originating proposer**: none

---

## 1. What Was Done

Integrated the 3-tier cognitive budgeting rule (Procedural / Standard / Critical), mandatory grounded platform inspection, dual launch protocol (GUI owner-assisted + autonomous API), and coordinator self-calibration into four core TFW files. All changes use the verified research texts from `research/iter2/3_extract.md` (E1–E4) with HL Amendment A1 (grounded inspection) integrated.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `b3b4de3baea16f5122abb4db6f2e082867c49cce` |
| Baseline / Candidate | `9cb04a4cc3c1fc2d3f3fef9e395798d60667ef47` / `92c5ee4bb83271adbc8770af93c3c6f3e3be986b` |
| VALUE membership | `.tfw/workflows/plan.md` (MODIFY, VALUE — Step 5 cognitive profiling), `.tfw/conventions.md` (MODIFY, VALUE — §7 Cognitive Budgeting subsection), `.tfw/templates/HL.md` (MODIFY, VALUE — §4.1 Execution profile column), `.tfw/templates/TS.md` (MODIFY, VALUE — Recommended execution profile metadata) |
| Arithmetic | 33 + 3 = 36 touched text LOC; 4 logical files; binary/non-text N/A |
| Membership deviations | none |
| Trigger disposition | 4 files < 50 trigger, 36 LOC < 5000 trigger — no decomposition required |
| Authority and timing | owner-direct saubakirov; multiplier 2×; TS approved at `b3b4de3baea16f5122abb4db6f2e082867c49cce` pre-work |
| Reproduction | `git diff --numstat -z 9cb04a4cc3c1fc2d3f3fef9e395798d60667ef47 92c5ee4bb83271adbc8770af93c3c6f3e3be986b -- .tfw/workflows/plan.md .tfw/conventions.md .tfw/templates/HL.md .tfw/templates/TS.md` |

### New Files

No new files created (zero new files — consistent with Principle P2 / F43, F45).

### Modified Files

| File | Changes |
|---|---|
| `.tfw/workflows/plan.md` | Added 12-line cognitive profiling paragraph to Step 5: 3-tier rule, grounded inspection, dual launch, self-calibration |
| `.tfw/conventions.md` | Added 17-line `### Cognitive Budgeting and Platform-Adaptive Launching` subsection in §7 before `### Provider-native evidence` |
| `.tfw/templates/HL.md` | Added `Execution profile` column to §4.1 Coordination Selection table (header + data row + separator) |
| `.tfw/templates/TS.md` | Added 1-line `Recommended execution profile` metadata in header block |

## 2. Key Decisions

1. **Insertion point in conventions.md**: Placed before `### Provider-native evidence` as specified by AC-2, maintaining the natural reading order: coordination rules → cognitive budgeting → provider evidence.
2. **Text fidelity**: Used the exact verified texts from TS §6 Technical Guidance without modification, matching the research E1–E4 texts with A1 amendment integration.
3. **Template backward compatibility**: Added the column to the HL table rather than creating a new table, preserving the single Coordination Selection table structure for existing tasks.

## 3. Acceptance Criteria

- [x] AC-1: Paragraph integrated in `.tfw/workflows/plan.md` Step 5 with 3-tier rule, grounded inspection, dual launch, self-calibration
- [x] AC-2: `### Cognitive Budgeting and Platform-Adaptive Launching` subsection added in `.tfw/conventions.md §7` before `### Provider-native evidence`
- [x] AC-3: `Execution profile` column added to `.tfw/templates/HL.md` §4.1 table
- [x] AC-4: `Recommended execution profile` metadata line added to `.tfw/templates/TS.md` header
- [x] AC-5: `python -m pytest tools/tests/ docs/scripts/ -q` returns `14 passed`

## 4. Verification

- Lint (`python -m pytest tools/tests/ docs/scripts/ -q --collect-only`): passed (14 items collected)
- Tests (`python -m pytest tools/tests/ docs/scripts/ -q`): 14 passed in 3.63s

## 5. Evidence

See [EV file](evidence/EV__phase-a__core_framework_integration.md) for evidence details.

Evidence verdict: 6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

No observations.

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

### Material handover at this return

- **Producer unit**: Executor `antigravity:thread:local:59016b7c-b3c7-4452-81d0-4dc65405e6d9`
- **Source epoch**: 2026-09-22T13:41:00+05:00
- **Inspected scope**: Four VALUE files at Candidate `92c5ee4`, all 5 TS ACs with gate checks, full pytest suite (14/14 passed), HL §7.2 citations (10 items applied in ONB §7), accounting numstat against Baseline.
- **Materiality**: All 5 ACs VERIFIED. 36 LOC across 4 files, zero new files, zero deviations from TS §4 selector. Tests pass without regressions. Phase A core framework integration complete.
- **Uncertainty**: None.
- **Continuation**: Phase A ready for `/tfw-review`. Phase B (platform adapters and documentation) depends on Phase A acceptance.

---

*RF — TFW_20260922-123250_CMTR / Phase A: Core Framework Integration & Coordination Guidance | 2026-09-22*
