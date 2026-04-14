# RES — TFW-38: Quality Enforcement (Iteration 4)

> **Date**: 2026-04-14
> **Author**: Researcher
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-38](HL-TFW-38__quality_enforcement.md)
> **Predecessors**: RES iter 1-3
> **Mode**: Pipeline

---

## Research Context

Iteration 4 addresses two user-directed gaps discovered after iter 3: (A) Knowledge citation mandate — coordinator and other roles don't reference KNOWLEDGE.md decisions when planning/executing, losing cross-task knowledge. (B) Diagram creation enforcement — diagrams are collected (D10) but never created because handoff.md and research/base.md don't mandate their creation.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D14 | **Knowledge citation mandate for coordinator in plan.md Step 3 + HL §4** | KNOWLEDGE.md is read in context loading (Step 1) but never cited in output. Coordinator operates in task silo — cross-task decisions, known pitfalls, and architectural patterns from KNOWLEDGE.md are silently ignored. Fix: explicit check step + "Relevant KNOWLEDGE.md items" block in HL §4. Pattern: "If no KNOWLEDGE.md exists or nothing applies, write 'No applicable knowledge items'" — same as RF §8 "No diagrams" pattern. |
| D15 | **Knowledge citation for executor in handoff.md Phase 1** | Executor checks "Inconsistencies between HL/TS and actual code" but not against KNOWLEDGE.md. Missing 4 words: "and KNOWLEDGE.md" in the bullet. Prevents executor from catching spec vs knowledge conflicts (e.g., "no Redis mandate" violated in TS). |
| D16 | **Diagram creation mandate for executor in handoff.md Phase 3** | RF §8 Diagrams is skipped at 96% rate because handoff.md Phase 3 doesn't mention it. Root cause = template-workflow disconnect (same as D1 §6-8 finding). Fix: add explicit bullet to Phase 3 RF checklist. RF template already describes what to do — the workflow just needs to point to it. |
| D17 | **Findings Map mandate for researcher in research/base.md Step 6** | RES template has Findings Map section. research/base.md Step 6 lists 5 synthesis items, Findings Map not among them. Fix: add as synthesis item. For simple iterations, use a minimal format: "Question → Evidence → Decision." |

## Complete Enforcement Chain (All 4 Iterations)

```
                    KNOWLEDGE CITATION                      DIAGRAM CREATION
                    ──────────────────                      ────────────────

PLAN              plan.md Step 3                           plan.md Step 4.3
(Coordinator)     "Check KNOWLEDGE.md,                     "ASCII visualization
                   cite in HL §4"                           mandatory" ← WORKS
                   ← NEW: D14                              

RESEARCH          (reads KNOWLEDGE.md                      research/base.md Step 6
(Researcher)       in Step 1, cites via                    "Findings Map — visual
                   Fact Candidates naturally)               diagram of findings"
                                                           ← NEW: D17

HANDOFF           handoff.md Phase 1                       handoff.md Phase 3
(Executor)        "Inconsistencies with                    "Diagrams — architecture,
                   KNOWLEDGE.md/actual code"                data flow, sequences.
                   ← NEW: D15                               Write 'No diagrams' if N/A"
                                                           ← NEW: D16

REVIEW            review.md Judge stage                    review.md Judge stage
(Reviewer)        Checklist: "Knowledge                    Checklist item #10:
                   alignment checked?"                     "RF completeness (§6-8)"
                   ← EXISTING (covered                     ← D1 (iter 1)
                    by philosophy check)

DOCS              --                                      docs.md checklist
(Knowledge Mgr)                                           "Index diagrams in
                                                           KNOWLEDGE.md §2"
                                                           ← D10 (iter 2)
```

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | Add Phase A scope: plan.md Step 3 knowledge citation + HL template §4 update | D14 |
| 2 | Add Phase A scope: handoff.md Phase 1 KNOWLEDGE.md inconsistency check | D15 |
| 3 | Add Phase A scope: handoff.md Phase 3 diagram mandate | D16 |
| 4 | Add Phase A scope: research/base.md Step 6 Findings Map mandate | D17 |

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| F14 | process | KNOWLEDGE.md is in context loading for 3 workflows (plan, handoff, research) but no workflow requires citing its contents in output artifacts. This creates a "read but don't use" pattern — the agent loads knowledge but doesn't prove it influenced decisions. Cross-task knowledge stays siloed. | G1-G2 | High |
| F15 | process | HL §3.1 diagrams are NOT skipped because plan.md Step 4.3 says "mandatory." RF §8 diagrams ARE skipped at 96% because handoff.md Phase 3 doesn't mention §8. Same root cause as §6-8: explicit workflow mention = execution, implicit template section = skip. This is now confirmed across 3 independent cases: §6-8 (iter 1), §8 Diagrams (iter 4), Findings Map (iter 4). | G4-G5, comparing plan.md §4.3 success vs handoff.md Phase 3 omission | High |
| F16 | philosophy | The "explicit N/A" pattern ("write 'No diagrams' if N/A", "write 'No applicable knowledge items'") transforms a silent skip into a conscious trace. The trace enables reviewer challenge: if RF §8 says "No diagrams" for a phase with a state machine, the reviewer in Judge stage can write ❌. Without the explicit N/A, the reviewer doesn't know if the executor forgot or consciously decided. | C3-C4 | High |

## Findings Map

```
ITERATION 4: ENFORCEMENT GAPS
═══════════════════════════════

                    KNOWLEDGE.md               DIAGRAMS
                    ────────────              ──────────

Current state:      Read in 3 workflows       HL §3.1: ✅ (plan.md mandates)
                    Cited in 0 outputs        RF §8:   ❌ (handoff.md omits)
                    Cross-task knowledge       RES Map: ❌ (research.md omits)
                    stays siloed
                         ↓                         ↓
Root cause:         No citation mandate        Template-workflow disconnect
                    in plan.md/handoff.md      (same root cause as D1)
                         ↓                         ↓
Fix:                D14: plan.md Step 3        D16: handoff.md Phase 3
                    D15: handoff.md Phase 1    D17: research/base.md Step 6
                         ↓                         ↓
Validation:         "No applicable items"      "No diagrams."
                    = explicit N/A trace       = explicit N/A trace
                         ↓                         ↓
Audit:              Reviewer checks HL §4      Reviewer checks RF §8
                    in Judge stage             via item #10 (RF completeness)


CUMULATIVE ROOT CAUSE MODEL (4 iterations)
═══════════════════════════════════════════

Template describes section    BUT    Workflow doesn't mention it
        ↓                                    ↓
Agent reads template               Agent follows workflow steps
(briefly, at creation)             (closely, at runtime)
        ↓                                    ↓
Section exists in file             Step not in agent's action list
        ↓                                    ↓
Section left empty/skipped         96% skip rate confirmed

FIX: Add explicit step to workflow → agent executes → section filled
     Confirmed 4× : D1(§6-8), D14(knowledge), D16(diagrams), D17(map)
```

## Iteration Status

- **Iteration:** 4 of 2 (min) / 3 (max, exceeded by user direction)
- **Hypotheses tested:** H1-H4 (all 🟢), plus H5 implicit (knowledge citation gap exists)
- **Gaps discovered:** None remaining
- **New decisions:** D14-D17

### Open Threads

All resolved. Full research complete.

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS
- [ ] **MORE NEEDED**

## Conclusion

Iteration 4 closed the final two gaps in TFW-38's quality enforcement: knowledge citation and diagram creation. Both share the same root cause confirmed across 4 iterations: template-workflow disconnect. When a template describes a section, but the workflow doesn't explicitly mandate it, agents skip it at ~96%. The fix is consistent: add explicit workflow steps with conscious N/A patterns ("No applicable knowledge items", "No diagrams"). Combined with iterations 1-3, TFW-38 now has 17 decisions across 4 research iterations, covering review restructure (D6-D12), handoff enforcement (D1, D15-D16), research enforcement (D17), planning enforcement (D14), and diagram lifecycle (D10, D16-D17). The research is complete and ready for HL update + TS specification.

---

*RES — TFW-38: Quality Enforcement (Iteration 4) | 2026-04-14*
