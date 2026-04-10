# RF — TFW-32 / Phase C: Multi-Iteration Research Formalization

> **Date**: 2026-04-10
> **Author**: AI (Executor)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> **TS**: [TS Phase C](TS__PhaseC__multi_iteration_research.md)

---

## 1. What Was Done

All 7 TS steps executed. 6 files modified, 0 new files created. No deviations from TS.

### Changes by file

| # | File | Change | LOC |
|---|------|--------|-----|
| 1 | `.tfw/PROJECT_CONFIG.yaml` | Added `min_iterations: 2` to `tfw.research` section (L48) | +1 |
| 2 | `.tfw/conventions.md` | §4 Research subfolder: added "Multi-iteration research" subsection with `researchN/` naming table, trace rule, `iterations.yaml` format (YAML block), coordinator lifecycle | +35 |
| 3 | `.tfw/workflows/research/base.md` | Step 0: iteration detection (iterations.yaml + researchN/ count + predecessor RES). Step 3: per-iteration subfolder creation + iter2+ briefing guidance. Step 6: per-iteration RES naming + Iteration Status block requirement + STOP message says "iteration {N}". Limits table: `min_iterations` row | +21 |
| 4 | `.tfw/workflows/plan.md` | Step 6 → 3 sub-steps: 6a (initial decision), 6b (create iterations.yaml), 6c (iteration gate with min_iterations enforcement). Gate logic: `< min` → MUST launch, `≥ min` → coordinator decides | +29 |
| 5 | `.tfw/templates/RES.md` | Iteration Status block inserted before Conclusion. Contains: iteration N/M, hypotheses tested/deferred, gaps, superseded decisions, Open Threads table, Recommendation (SUFFICIENT/MORE NEEDED/BLOCKED) | +25 |
| 6 | `.tfw/glossary.md` | 3 new terms: Iteration (Research), iterations.yaml, min_iterations — with cross-references to conventions.md §4 and plan.md Step 6c | +9 |

**Total LOC changed: ~120 (+additions, -removals). Within budget (max 1200).**

## 2. Acceptance Criteria Verification

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | `tfw.research.min_iterations: 2` in PROJECT_CONFIG.yaml | ✅ | L48 |
| 2 | conventions.md §4 "Multi-iteration research" subsection with researchN/ table, trace rule, iterations.yaml YAML block | ✅ | L125-158 |
| 3 | research/base.md Step 0 detects iterations: checks iterations.yaml, counts researchN/ folders, reads predecessor RES | ✅ | L12-25 |
| 4 | research/base.md Step 3 creates researchN/ for iteration N>1 + iter2+ briefing guidance | ✅ | L39-49 |
| 5 | research/base.md Step 6 names RES files per iteration + requires Iteration Status block | ✅ | L83-93 |
| 6 | research/base.md Limits table has `min_iterations` row (default 2, Hard, config key) | ✅ | L127 |
| 7 | plan.md Step 6 has 3 sub-steps: 6a, 6b, 6c | ✅ | L65-103 |
| 8 | plan.md Step 6c gate logic: `< min` → MUST; `≥ min` → coordinator decides | ✅ | L94-101 |
| 9 | plan.md Step 6c: update HL after each iteration, present diff, user confirms | ✅ | L89-92, L103 |
| 10 | RES template Iteration Status block with all required fields before Conclusion | ✅ | L84-107 (before L109 Conclusion) |
| 11 | glossary.md has "Iteration (Research)", "iterations.yaml", "min_iterations" with cross-refs | ✅ | L112-119 |
| 12 | STOP message in Step 6 says "iteration {N} complete" | ✅ | L93 |

All 12 criteria pass.

## 3. Test Results

- **Build gate**: `echo "configure your verify command"` → pass (stub).
- **Manual verification**: all 6 files reviewed post-edit. Section ordering, cross-references, and content match TS exactly.
- **Backwards compatibility**: verified — if no `iterations.yaml` exists, Step 0 falls back to single-iteration flow. All changes are additive.

## 4. Deviations from TS

None.

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/workflows/plan.md` | 53 | style | Step 4 (Briefing Protocol) at L53 references `research/briefing.md` path — after Step 3 changes, iteration 2+ would use `researchN/briefing.md`. The wording is still technically correct (template reference), but could be clearer for multi-iteration context |
| 2 | `.tfw/workflows/plan.md` | 140 | style | plan.md grew from 108 to 140 lines (+30%). Still within attention budget but approaching the threshold mentioned in conventions.md §11 Design Rules ("workflow instructions ≤1200 words") |
| 3 | `.tfw/conventions.md` | 138 | naming | `iterations.yaml` is documented in §4 "Research subfolder" but not listed in the §4 naming table (L138-157 artifact naming table). The naming table only covers artifact files (HL, TS, RES, etc.), not control files. Consistent with current pattern (PROJECT_CONFIG.yaml also not in naming table) |

## 6. Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | process | research/base.md Step 4 (Briefing Protocol) hardcodes `research/briefing.md` path — does not account for `researchN/` in multi-iteration context. The step works because template copying handles file creation, but the path reference is iteration-unaware | This execution, observation #1 | ★★☆ |

## 7. Strategic Insights (Execution)

No strategic insights. No human domain knowledge was provided during execution — all changes were mechanical TS application.

## 8. Diagrams

```
MULTI-ITERATION RESEARCH FLOW (as implemented):

  plan.md Step 6a              plan.md Step 6b           research/base.md
  ┌─────────────┐             ┌──────────────┐          ┌─────────────────┐
  │ RESEARCH     │──approve──→│ Create        │──STOP──→│ Step 0: Detect  │
  │ decision     │            │ iterations.yaml│         │ iteration from  │
  └──────┬──────┘             └──────────────┘          │ YAML + folders  │
         │skip                                          ├─────────────────┤
         ↓                                              │ Step 3: Create  │
   Step 7 (TS)                                          │ researchN/      │
                                                        ├─────────────────┤
                                                        │ Steps 4-5:     │
                                                        │ Briefing+Stages│
                                                        ├─────────────────┤
                                                        │ Step 6: Write  │
                                                        │ RES + Iteration│
                                                        │ Status block   │
                                                        └───────┬────────┘
                                                                │STOP
                                                                ↓
  plan.md Step 6c              plan.md Step 6c
  ┌─────────────────┐         ┌─────────────────┐
  │ Read RES +      │──< min──→│ MUST launch    │──→ back to base.md
  │ iterations.yaml │         │ next iteration  │
  │ Gate check      │         └─────────────────┘
  │ completed vs    │
  │ min_iterations  │──≥ min──→ coordinator decides → Step 7 (TS)
  └─────────────────┘
```

---

*RF — TFW-32 / Phase C: Multi-Iteration Research Formalization | 2026-04-10*
