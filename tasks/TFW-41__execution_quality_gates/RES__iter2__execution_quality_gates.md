# RES — TFW-41 Iteration 2: Embedded Dimensional Analysis

> **Date**: 2026-04-20
> **Author**: Researcher (AI)
> **Status**: ✅ RES_DONE — Iteration 2 complete
> **Parent HL**: [HL-TFW-41](HL-TFW-41__execution_quality_gates.md)
> **Predecessor**: [RES iter1](RES__TFW-41__execution_quality_gates.md)
> **Mode**: Pipeline / Deep

---

## Research Context

Iteration 1 proposed mandatory Zwicky Box in Extract (DR4) with 5 enforcement rules (DR5). User observed: HD-19's Zwicky Box was "simulation" — all Alt 1 selected, no CCA, no discovery. Instruction "do Zwicky Box" produces compliance, not analysis. Hypothesis: distribute GMA steps across existing Gather→Extract→Challenge stages so morphological analysis emerges naturally from the stage sequence.

## Briefing

See [research2/briefing.md](research2/briefing.md). H5 — user-injected.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| DR7 | **Supersedes DR4/DR5.** Replace "mandatory Zwicky Box in Extract" with embedded dimensional analysis across all 3 stage templates. | HD-19 failure: instruction-based approach produces simulation. Embedded approach creates cross-stage dependency (Extract needs Gather dimensions → can't simulate). |
| DR8 | **Gather template: add `## Dimensions` section.** Each dimension = independent decision factor, ≥3 alternatives in table format, no "recommended" marking. Placed BEFORE `## Findings`. | GMA Step 1 (Decompose) maps naturally to Gather's "What do we NOT know?" Decomposing the decision space IS identifying unknowns. |
| DR9 | **Extract template: add `## Configuration Space` section.** Cross-reference table using Gather's dimensions. One column per dimension, one row per viable combination. Instruction: "Do NOT evaluate yet." | GMA Step 3 (Construct Field) maps naturally to Extract's "What do we NOT see?" The full configuration space IS what you don't see until you enumerate it. |
| DR10 | **Challenge template: add `## Consistency Check` section.** Pairwise incompatibility table for dimension pairs. Output: surviving configurations + unexpected survivors. | GMA Step 4 (CCA) maps naturally to Challenge's "What do we NOT expect?" Finding incompatible pairs IS discovering unexpected constraints. |
| DR11 | **Native terminology, not GMA terminology.** Templates use: Dimension, Alternative, Configuration Space, Consistency Check, Surviving Configuration. Glossary references Zwicky as origin. | Simulation risk: "doing Zwicky" → method compliance. "Finding dimensions" → problem analysis. Native terms remove the compliance trap. |
| DR12 | **Graceful degradation: <3 dimensions → comparison matrix.** One instruction in workflow Step 5: "If <3 independent dimensions, use comparison matrix instead of full dimensional pipeline." Gather still lists alternatives; Extract/Challenge use pros/cons instead of Config Space/CCA. | Challenge C5: single-dimension research shouldn't require full pipeline. The template sections become optional via this one workflow instruction. |
| DR13 | **Workflow Step 5: add 4-line dimensional analysis description.** No methodology names. Describes the flow: Gather decomposes, Extract builds configuration space, Challenge eliminates inconsistencies. | Base workflow needs the connecting thread. Without it, researchers might not see the cross-stage dependency. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| 1 | Should Gather checkpoint include "Dimensions identified?" gate? | Resolved | YES — add to checkpoint sufficiency: `- [ ] Dimensions identified? (if ≥3 decision factors exist)` |
| 2 | Should Extract's Config Space have overflow protection? | Resolved | YES — "If >30 combinations, list only configs where ≥1 dimension differs from first-listed alternative." |

## Hypotheses

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H5 | Zwicky steps can be distributed across existing stages naturally, producing genuine analysis instead of simulation | open (user-injected) | ✅ SUPPORTED | GMA maps 1:1 to stages (Gather E1). HD-19 retrospective shows proposed templates would have prevented "all Alt 1" pattern (Extract E4). Cross-stage dependency creates natural enforcement (Challenge C2). Stage character preserved (Challenge C4). |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | Replace DR4/DR5 with DR7-DR13 in §3 Proposed Solutions | This RES |
| 2 | Add H5 to HL §10 Hypotheses with ✅ SUPPORTED | This RES |
| 3 | §2 Problems: add "Instruction-based Zwicky produces simulation, not analysis" as observed problem | Gather G2, User observation |

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC4 | process | **Instructions produce compliance, heuristics produce analysis.** "MUST do Zwicky Box" → researcher fills box to comply. Template questions that guide thinking → researcher naturally decomposes. The mechanism: instructions target the output (a completed box), heuristics target the process (the thinking that fills it). Same distinction as Requirements-first TS (H1): requirements target behavior, code targets form. | HD-19 failure + User observation + iter 2 analysis | ★★★ |
| FC5 | process | **Cross-stage dependencies are a natural enforcement mechanism.** When Extract's Config Space requires Gather's Dimensions, the researcher can't skip Gather decomposition without Extract failing. This is stronger than a checkpoint gate because it's structural (the artifact can't be created) not procedural (a reviewer must check). | Challenge C2 | ★★☆ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS4 | process | **User directly identified simulation vs analysis problem: "я вижу больше симуляцию... просто таблица ради таблица где выбрано все из первого столбца."** This is a fundamental insight about AI agent behavior: agents optimize for output completion (filled template) not for cognitive value (genuine discovery). Template design must make completion impossible without genuine analysis. The cross-stage dependency mechanism achieves this. | User, 2026-04-20 | ★★★ |
| SS5 | conventions | **User values natural flow over named methodology: "чтобы было более естественно."** The framework should absorb external methodologies into its own vocabulary. Zwicky's concepts are valuable; Zwicky's name in templates is not. This is consistent with TFW's approach to other borrowed concepts (OODA loops are never called "Boyd's cycle" in templates). | User, 2026-04-20 | ★★★ |

## Findings Map

```
ITERATION 1                              ITERATION 2
┌─ DR4: "Must do Zwicky Box" ──────┐     ┌─ DR7: Embedded Dimensional Analysis ──────────┐
│                                   │     │                                                 │
│  Single section in Extract        │     │  GATHER          EXTRACT         CHALLENGE      │
│  5 enforcement rules              │     │  ## Dimensions → ## Config     → ## Consistency │
│  Instruction-based                │     │     Space           Check                       │
│                                   │     │                                                 │
│  Result: simulation risk HIGH     │     │  Cross-stage dependency = natural enforcement   │
│  Evidence: HD-19                  │     │  Result: simulation risk LOW                    │
└───────────────────────────────────┘     └─────────────────────────────────────────────────┘
              │                                         │
              │              SUPERSEDED                 │
              └─────────────────────────────────────────┘

GMA STEP MAPPING (verified):
┌──────────────────────────────────────────────────────────────────┐
│  GMA Step 1: Decompose    →  GATHER  ## Dimensions               │
│  GMA Step 2: Enumerate    →  GATHER  ## Dimensions (Alt table)   │
│  GMA Step 3: Construct    →  EXTRACT ## Configuration Space      │
│  GMA Step 4: CCA          →  CHALLENGE ## Consistency Check      │
│  GMA Step 5: Iterate      →  OODA loop (already built-in)       │
│  GMA Step 6: Synthesize   →  RES (already built-in)             │
└──────────────────────────────────────────────────────────────────┘

TERMINOLOGY MAPPING:
  GMA "parameter"        →  TFW "dimension"
  GMA "value"            →  TFW "alternative"
  GMA "morphological field" →  TFW "configuration space"
  GMA "CCA"              →  TFW "consistency check"
  GMA "consistent config" →  TFW "surviving configuration"
```

## Concrete Deliverables (for TS)

### Files to Modify

| # | File | What changes |
|---|------|-------------|
| 1 | `.tfw/templates/research/gather.md` | Add `## Dimensions` section with table format |
| 2 | `.tfw/templates/research/extract.md` | Add `## Configuration Space` section with cross-reference table |
| 3 | `.tfw/templates/research/challenge.md` | Add `## Consistency Check` section with pairwise table |
| 4 | `.tfw/workflows/research/base.md` (= `.agent/workflows/tfw-research.md`) | Add 4-line dimensional analysis description in Step 5 |
| 5 | `.tfw/glossary.md` | Add 5 terms: Dimension, Alternative, Configuration Space, Consistency Check, Surviving Configuration |
| 6 | `.tfw/conventions.md` | Add dimensional analysis origin note referencing Zwicky |

### Exact Wording — Summary

**Gather `## Dimensions` instruction:**
> For each research question, identify independent decision dimensions.
> A dimension = a factor where changing it changes the solution, regardless of what other factors do.
> List ≥3 alternatives per dimension. Do NOT mark any as "recommended."

**Extract `## Configuration Space` instruction:**
> Using the dimensions from Gather, build the full cross-reference.
> Each row = one viable configuration (one alternative per dimension).
> Do NOT evaluate yet — list all combinations that are not obviously contradictory.

**Challenge `## Consistency Check` instruction:**
> Take each pair of dimensions from Extract's Configuration Space.
> For each pair, ask: "Can D_i-Alt_X coexist with D_j-Alt_Y?"
> Mark incompatible pairs. Remove configurations containing them.

**Workflow Step 5 addition:**
> **Dimensional analysis** threads through all three stages:
> - **Gather** decomposes the problem into independent dimensions with alternatives
> - **Extract** constructs the configuration space from Gather's dimensions
> - **Challenge** eliminates inconsistent combinations via pairwise consistency check
> If the research question has <3 independent dimensions, use a comparison matrix instead.

## Iteration Status

- **Iteration:** 2 of 2 (min) / 4 (max)
- **Hypotheses tested:** H5 (✅ supported)
- **Hypotheses deferred:** None
- **Gaps discovered:** None
- **Superseded decisions:** DR4, DR5 superseded by DR7-DR13

### Open Threads (for next iteration)

No open threads. Both iterations complete. Ready for plan.

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS

Both iterations converge: iter 1 established WHAT gates to add (requirements-first TS, Pre-TS gate, execution loops, principle mapping). Iter 2 established HOW to integrate Zwicky (embedded dimensional analysis across stages, native terminology, cross-stage dependency as enforcement).

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 2 validated H5: GMA methodology maps 1:1 to existing Gather→Extract→Challenge stages. The key mechanism is **cross-stage dependency** — Extract's Configuration Space requires Gather's Dimensions, making it structurally impossible to simulate analysis without doing the decomposition work. This supersedes iteration 1's instruction-based approach (DR4/DR5 "must do Zwicky Box") which produced the HD-19 simulation problem. The deliverables are 6 file modifications with exact wording designed in TFW-native terminology (Dimension, Alternative, Configuration Space, Consistency Check, Surviving Configuration). The terminology references Zwicky in glossary/conventions but never in researcher-facing templates — preventing the "methodology compliance" trap where the researcher optimizes for filling a named framework instead of analyzing the problem.

---

*RES — TFW-41 Iteration 2: Embedded Dimensional Analysis | 2026-04-20*
