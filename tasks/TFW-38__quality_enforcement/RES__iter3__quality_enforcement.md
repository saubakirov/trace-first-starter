# RES — TFW-38: Quality Enforcement (Iteration 3)

> **Date**: 2026-04-14
> **Author**: Researcher
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-38](HL-TFW-38__quality_enforcement.md)
> **Predecessors**: [RES iter 1](RES__TFW-38__quality_enforcement.md), [RES iter 2](RES__iter2__quality_enforcement.md)
> **Mode**: Pipeline

---

## Research Context

Iteration 3 addressed two user-directed threads: (A) TS over-specification audit — are coordinators writing implementation instead of requirements? (B) Complete naming refinement for review stages, modes, and all downstream references.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D11 | **Review stage names: Map → Verify → Judge → Decide** | "Naming Creates Behavior" (TFW value): if you must explain it, it's named wrong. User rejected "comprehend" (unclear) and "assess" (vague, prefers "judge" — more intentional). All names are 1-2 syllables, active verbs from established disciplines (navigation, engineering, legal, management). Chain reads as sentence: "Map the work, Verify the claims, Judge the quality, Decide the verdict." |
| D12 | **Review mode names: code / docs / spec** | User rejected "prose" (meaningless). Modes describe output type (noun), not domain. All 1 syllable. "docs" replaces "prose" for writing/documentation tasks — clear, short, no namespace collision with project `docs/` folders. |
| D13 | **TS over-specification is a tendency, not a systemic defect. Out of TFW-38 scope.** | 4 TS sampled: 49-71% code. Coordinators write full code for complex/critical logic (SLA algorithms, security), signatures for standard patterns, pseudocode for UI. This varies naturally. The issue is missing guidance on WHEN to use which level (L1-L4). Recommend separate task for TS template conventions. |

## Hypothesis Status (Cumulative)

| # | Hypothesis | Status | Iteration |
|---|-----------|--------|-----------|
| H1 | Explicit §6-8 enumeration stops skipping | 🟢 confirmed | 1 |
| H2 | Audit step changes reviewer behavior | 🟢 superseded by H3 | 1 |
| H3 | Domain-specific review stages produce more reliable reviews | 🟢 confirmed | 2 |
| H4 | "Naming Creates Behavior" applied to review stages eliminates comprehension friction | 🟢 confirmed | 3 (user test: "comprehend" fails, "map" passes) |

## Final Naming Inventory

### Review Stages

| Stage | Name | REVIEW Section | Cognitive Mode | Verbs Chain |
|-------|------|----------------|----------------|-------------|
| 1 | **Map** | §1 Map | "Do I understand what was done?" | Map the work |
| 2 | **Verify** | §2 Verify | "Are the claims true?" | Verify the claims |
| 3 | **Judge** | §3 Judge | "Is the quality sufficient?" | Judge the quality |
| 4 | **Decide** | §4 Decide | "What's the verdict?" | Decide the verdict |

### Review Modes

| Mode | Tasks | Checklist Items | Verify Actions |
|------|-------|----------------|----------------|
| **code** | Implementation | 10 items (6 universal + 4 domain) | Spot-check 2-3 files, check tests |
| **docs** | Writing, docs, design | 8 items (6 universal + 2 domain) | Verify deliverable existence, check structure |
| **spec** | Analytical, research | 8 items (6 universal + 2 domain) | Verify deliverables, check source citations |

### File Paths

| Entity | Path |
|--------|------|
| Review workflow | `.tfw/workflows/review.md` |
| Code mode file | `.tfw/workflows/review/code.md` |
| Docs mode file | `.tfw/workflows/review/docs.md` |
| Spec mode file | `.tfw/workflows/review/spec.md` |
| REVIEW template | `.tfw/templates/REVIEW.md` |
| Config key | `tfw.review.default_mode` |

### Cross-Reference: Review vs Research Naming

| Research | Review | Structural Parallel |
|----------|--------|---------------------|
| Briefing | Map | Prepare/understand |
| Gather | Verify | Collect evidence |
| Extract | Judge | Apply cognitive framework |
| Challenge | — | (no challenge in review) |
| RES | Decide | Synthesize conclusion |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | Phase A: rename all stage references from Comprehend/Verify/Assess/Synthesize to Map/Verify/Judge/Decide | D11 |
| 2 | Phase A: rename mode "prose" to "docs" | D12 |
| 3 | Add new task recommendation to HL §7 Parking Lot: "TS Template Conventions — L1-L4 specification level guidance" | D13, G2-G6 |
| 4 | HL §10: add H4 (naming validation) | D11 |

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| F10 | convention | Review stages: Map → Verify → Judge → Decide. All 1-2 syllables, active verbs, from navigation/engineering/legal/management disciplines. Validated by TFW "Naming Creates Behavior" principle: "comprehend" failed user test (unclear), "assess" failed user test (too vague), "judge" passed (intentional, direct). | User, 2026-04-14, Challenge C1-C5 | High |
| F11 | convention | Review modes: code / docs / spec. All 1-syllable nouns describing output type. "prose" rejected by user (meaningless). Modes configure the Judge-stage checklist, not the domain. | User, 2026-04-14, G10, C4 | High |
| F12 | process | TS files across helpdesk and atamat contain 49-71% ready-to-paste code (average 58%). Coordinators write full implementation (L4) for complex/critical logic and method signatures (L3) for standard patterns. This is natural risk-averse behavior, not pathological. Missing: explicit guidance on when to use L1-L4 in TS template. | G2-G6, C6, 4 TS sampled | High |
| F13 | philosophy | User: "Проверить что координатор в ТС не ставит задачу слишком детально, так что уже почти выполняет её. Оставляет ли он на креатив исполнителя." TS over-specification suppresses executor creativity and makes ONB trivial. Token double-spend when coordinator writes code without testing and executor copies it. | User, 2026-04-14 | High |

## Strategic Insights

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS2 | process | TS content quality has a specification level spectrum (L1: Goal → L2: Requirement → L3: Design → L4: Implementation). Most TS files are at L4 for complex steps and L2-L3 for simple steps. The missing piece is explicit guidance: templates should recommend which specification level to use based on step complexity. This is a separate methodology improvement, not a quality enforcement fix. | G2-G6, E3-E4, C6 | ★★★ |

## Findings Map

```
ITERATION 3 SCOPE
══════════════════

Thread A: TS Over-Spec                  Thread B: Naming
────────────────────                    ────────────────

4 TS sampled:                           User feedback:
HD PhaseD: 71% code                     ❌ "comprehend" = unclear
HD PhaseF: 56% code                     ❌ "prose" = meaningless
AT PhaseH: 55% code                     ✅ "judge" = intentional
AT PhaseF2: 49% code                    
     ↓                                       ↓
Average: 58% code                       "Naming Creates Behavior"
     ↓                                  filter applied:
Tendency, not defect                         ↓
Complex → L4 (natural)                  Stages: Map → Verify → Judge → Decide
Simple → L2-L3 (natural)               Modes:  code / docs / spec
     ↓                                       ↓
Missing: L1-L4 guidance                All 1-2 syllables
→ Separate task, not TFW-38            All active, need no explanation
                                       ✅ User test passed

CUMULATIVE RESEARCH (3 iterations)
══════════════════════════════════

Iter 1: Template-workflow disconnect → §6-8 skip rate 96-100%
        Fix: explicit enumeration in handoff.md (D1)
        Reviewer trust-chain → audit step needed (D2)

Iter 2: Review should have staged structure (D6)
        3 modes based on output type (D7)
        Stages as REVIEW sections, not files (D8)
        Template must restructure to match (D9)
        Diagrams → index, not copy (D10)

Iter 3: Stages renamed: Map → Verify → Judge → Decide (D11)
        Modes renamed: code → docs → spec (D12)
        TS over-spec = tendency, separate task (D13)
```

## Iteration Status

- **Iteration:** 3 of 2 (min) / 3 (max)
- **Hypotheses tested:** H1 (🟢), H2 (🟢→H3), H3 (🟢), H4 (🟢)
- **Hypotheses deferred:** None
- **Gaps discovered:** TS specification level guidance needed (out of scope)
- **Superseded decisions:** D7 mode "prose" → D12 mode "docs"

### Open Threads

| # | Thread | Status |
|---|--------|--------|
| 1 | Staged review design | ✅ Resolved — D6, D8, D9, D11 |
| 2 | Review modes | ✅ Resolved — D7→D12 |
| 3 | Naming validation | ✅ Resolved — D11, D12, user test |
| 4 | TS over-specification | ✅ Resolved — D13, out of scope, separate task |
| 5 | Diagram indexing | ✅ Resolved — D10 |

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS
- [ ] **MORE NEEDED**

3 iterations completed (at max). All hypotheses tested. All open threads resolved. Naming validated by user. TS over-spec scoped out cleanly. Ready for TS specification.

## Conclusion

Three research iterations produced a comprehensive evidence base for TFW-38 quality enforcement. Iteration 1 empirically confirmed the template-workflow disconnect (96-100% §6-8 skip rate across 80+ files) and the reviewer trust-chain failure. Iteration 2 designed a 4-stage domain-agnostic review flow with 3 output-type modes. Iteration 3 refined naming via the TFW's own "Naming Creates Behavior" principle — final stages Map → Verify → Judge → Decide, modes code / docs / spec — and identified the TS over-specification tendency as a separate improvement track (L1-L4 guidance). The research is ready for HL update and TS specification.

---

*RES — TFW-38: Quality Enforcement (Iteration 3) | 2026-04-14*
