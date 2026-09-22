# ONB — TFW_20260922-123250_CMTR / Phase A: Core Framework Integration & Coordination Guidance

> **Current filename**: `ONB__phase-a__core_framework_integration.md`

> **Date**: 2026-09-22
> **Author**: Executor (Antigravity)
> **Status**: 🟠 ONB
> **Parent HL**: [HL-TFW_20260922-123250_CMTR](../HL-TFW_20260922-123250_CMTR.md)
> **TS**: [TS Phase A](TS__phase-a__core_framework_integration.md)
> **Producer unit**: antigravity:thread:local:59016b7c-b3c7-4452-81d0-4dc65405e6d9
> **Parent Coordinator**: antigravity:thread:local:3d06f6f4-0f5b-415d-aff2-f70c8f1acdcc
> **Activation / dispatch source**: owner-direct: saubakirov via `/tfw-handoff cmtr`
> **Coordination authority**: `../HL-TFW_20260922-123250_CMTR.md @ 9cb04a4cc3c1fc2d3f3fef9e395798d60667ef47`
> **Originating proposer**: none

---

## 1. Understanding

Phase A integrates the 3-tier cognitive budgeting rule, grounded platform model inspection, dual launch protocol, and coordinator self-calibration into four core TFW files: `plan.md` Step 5, `conventions.md §7`, `templates/HL.md §4.1` and `templates/TS.md` header. All edits use verified research texts from `research/iter2/3_extract.md` (E1–E4) with Amendment A1 integration (grounded inspection). The result is zero new files, four point-edit extensions, and full backward compatibility with existing parsers and tests.

## 2. Entry Points

- `.tfw/workflows/plan.md` (line 99–107): Step 5 Coordination Selection Gate — insert cognitive profiling paragraph after current text.
- `.tfw/conventions.md` (line 1049): `### Provider-native evidence` — insert new subsection immediately before it.
- `.tfw/templates/HL.md` (lines 93–95): §4.1 Coordination Selection table — add `Execution profile` column.
- `.tfw/templates/TS.md` (lines 7–9): header metadata block — add `Recommended execution profile` line.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The TS provides verified literal texts (§6 Technical Guidance) and exact insertion points (AC-1 through AC-4). All four target files are accessible and uncommitted changes are clean (only untracked `PROPOSAL__serialized_landing_and_test_boundary.md` and `workspace/2026/TFW_20260909-231654_OTR/` present, both unrelated).

## 4. Recommendations (suggestions, not blocking)

1. The TS §6.2 text for `conventions.md` includes model name examples (Flash, Haiku, 4o-mini, Sonnet, Pro, o3-mini) as illustrative tier anchors. These are abstract tier illustrations, not hardcoded recommendations — consistent with Principle P7 (Grounded Inspection).

## 5. Risks Found (edge cases, potential issues not in TS)

1. The `conventions.md` file is large (1515 lines). Inserting before `### Provider-native evidence` (line 1049) requires precise placement to maintain Markdown heading hierarchy within `## 7) Coordination`.

## 6. Inconsistencies with Code (spec vs reality)

1. No inconsistencies found. All four target files exist at the paths referenced by the TS, and their structure matches the TS's expectations.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | F3 (Critical opponent) | ✅ | Applied: Tier 3 (Critical/Adversarial) prohibits downgrading power on review/inception | Core rule in E2 text |
| 2 | F10 (The thinking is the product) | ✅ | Applied: thinking budget is direct quality lever — reflected in 3-tier justification | Motivates the entire CMTR concept |
| 3 | F18 (Right name per context) | ✅ | Applied: texts use native platform terms (dropdown, reasoning_effort, thinking tokens) | E1/E2 platform-specific guidance |
| 4 | F25 (Framework proposes — human chooses) | ✅ | Applied: dual launch protocol — coordinator gives 2-line guidance, human decides in UI | E2 Dual Launch Protocol |
| 5 | F43 (Architecture quality over fixes) | ✅ | Applied: extending existing Step 5 and §7 instead of creating new files/sections | Zero new files; all point edits |
| 6 | F45 (Subtraction is preferred) | ✅ | Applied: each insertion is one compact paragraph/subsection following Saint-Exupéry | Minimal footprint |
| 7 | D15 (Thin adapters) | ✅ | N/A for Phase A — adapter updates are Phase B scope | |
| 8 | D59 (Capability boundaries) | ✅ | Applied: E2 distinguishes GUI owner-assisted launch from native task API | Dual launch protocol |
| 9 | §7 Coordination (conventions.md) | ✅ | Applied: new subsection placed within existing §7 hierarchy | Insertion before Provider-native evidence |
| 10 | A1 (Grounded inspection amendment) | ✅ | Applied: E1 text integrates mandatory grounded inspection; E2 includes dedicated subsection | Grounded Inspection subsection in E2 |

No additional PV sources missed — HL §7.2 is comprehensive for Phase A scope.

### Material handover at this return

- **Producer unit**: Executor `antigravity:thread:local:59016b7c-b3c7-4452-81d0-4dc65405e6d9`
- **Source epoch**: 2026-09-22T13:37:05+05:00
- **Inspected scope**: Four target VALUE files, TS §6 verified texts (E1–E4), HL §7.2 citations (11 items), git status (clean except unrelated untracked), phase-a/status.md routing spine (complete and valid).
- **Materiality**: No blockers. Verified insertion points for all four AC targets. Texts from research iter2/3_extract.md match TS §6 guidance with A1 amendment integrated.
- **Uncertainty**: None.
- **Continuation**: Proceed to Step 2 (implementation of AC-1 through AC-5).

---

*ONB — TFW_20260922-123250_CMTR / Phase A: Core Framework Integration & Coordination Guidance | 2026-09-22*
