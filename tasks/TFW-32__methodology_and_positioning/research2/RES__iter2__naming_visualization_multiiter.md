# RES — TFW-32 Iteration 2: Naming, Visualization, Multi-Iteration

> **Date**: 2026-04-10
> **Author**: AI (Researcher)
> **Status**: 🔬 RES — Complete (Iteration 2)
> **Parent HL**: [HL-TFW-32](HL-TFW-32__methodology_and_positioning.md)
> **Mode**: Pipeline (deep)
> **Predecessor**: [RES Iteration 1](RES__TFW-32__methodology_and_positioning.md)

---

## Research Context

Iteration 2 addresses 4 gaps from RES1: (1) naming precision — "Knowledge Candidates" proposed in RES1 D2 may be too vague (D28 violation), (2) visualization/diagrams section — deferred without investigation in RES1, (3) business process representation — not covered in RES1 despite HL S15, (4) multi-iteration research enforcement — designed in RES1 D4 but untested and possibly under-structured.

## Briefing

See [research2/briefing.md](research2/briefing.md). Key user direction:
- "Strategic Insight" has good behavioral vector. "Knowledge" is too broad
- Visualization = separate chapter in each RESULT artifact (RES, RF)
- Business processes = two levels: HL = value vision, RF = technical detail  
- Multi-iteration needs MORE structure than RES1 proposed, not less. Without YAML/statuses → fast-run

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D10 | **Rename "Strategic Session Insights" → "Strategic Signals" across all templates.** Add the section to RES and RF templates (currently only HL §11 has it) | Scenario testing: "Strategic Insights" misses non-strategic human signals (process preferences, emotions — scored 1/3 captures). "Strategic Signals" captures all 3 scenarios (business facts, process preferences, emotions) because "Signal" = "anything that should change how we act." "Knowledge Candidates" scored worst (triggers generic retrieval mode in LLMs). D28 confirmed: name precision → agent capture precision |
| D11 | **Keep "Fact Candidates" (§6) with sharpened scope: agent-observable project patterns.** Do NOT rename to "Doc Candidates" or "Knowledge Candidates" | RES1 D2 (rename to Doc/Knowledge Candidates) overrode a working name based on workflow routing, not capture behavior. §6 Fact Candidates works for its purpose: agent-observed operational patterns about the project. The REAL gap was missing §7 Strategic Signals in RES/RF — not wrong naming of §6. Keep §6, add §7 |
| D12 | **Add "Diagrams" section to RF and RES templates.** Expand HL §3.1 instructions. Per-template instruction block controls framing. Section is optional with explicit "No visual representation required" escape | arc42/C4 confirm: diagrams at each abstraction level with level-appropriate content. One section name ("Diagrams") across all artifacts. Instructions differ per template: HL = value delivery flow, RF = technical process detail, RES = research findings visualization. Name is a navigation anchor — instructions carry behavioral load |
| D13 | **Two-level business process representation.** HL = Value Delivery Flow (user → steps → value). RF = Technical Process Detail (APIs, DBs, sequences). Both live in the Diagrams section | BPMN + VSM confirm two-level pattern. Cross-domain validation: works for code, analytics, education, and research projects. HL shows WHERE value is delivered (executor orientation). RF shows HOW value was delivered (reproduction orientation) |
| D14 | **Multi-iteration enforcement: iterations.yaml + researcher exit protocol + coordinator hard gate in plan.md.** min_iterations = hard floor. Researcher MUST output "Iteration N of M" status block. Coordinator CANNOT proceed to TS while iterations remain uncovered | User direction: "without YAML, agents will fast-run." 4 failure scenarios tested — all handled. Key: gate is in COORDINATOR pipeline (plan.md), not in researcher. Researcher can try to fast-run but coordinator blocks. iterations.yaml = tracking + structural enforcement, not authority |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q5 | "Diagrams" as section name — is it the best option? Alternatives: "Visual Evidence" (stronger framing but awkward in HL), "Schemas" (bilingual but DB-ambiguous) | Open | Recommend "Diagrams" (simplest, universal). Per-template instructions do the real framing. But user may prefer something else — iteration 3 topic |
| Q6 | Should §6 "Fact Candidates" be renamed to something sharper ("Project Patterns", "Operational Observations")? | Open | Currently works. Sharpening is nice-to-have, not blocking. Keep for now, revisit if agents misclassify |
| Q7 | Where exactly in plan.md does the coordinator iteration gate go? Step 6? New Step 6b? | Open | Design exists but insertion point TBD. Coordinator decides |

## Hypotheses

| # | Hypothesis | RES1 Status | RES2 Status | Evidence |
|---|-----------|-------------|-------------|----------|
| H5b | "Knowledge Candidates" is too vague — loses D28 behavioral focus | NEW | ✅ CONFIRMED | LLM naming research: "Knowledge" triggers retrieval mode (broad, generic). "Strategic" triggers synthesis mode (focused, analytical). Scenario test: Knowledge Candidates scored 3/10 on D28, Strategic Signals scored 8/10 |
| H5 (RES1) | FC and SI are TWO different concepts | ✅ CONFIRMED (RES1) | ✅ CONFIRMED + EXTENDED | RES1 proved they're different. RES2 proves the fix: don't rename — EXTEND Strategic Signals section to RES/RF templates. RES1's FC1-FC5 were misclassified Strategic Signals because RES had no SI section |
| H6 | TFW needs a standard visualization/diagrams section | ⏸️ DEFERRED | ✅ CONFIRMED | arc42: diagrams at every level. C4: hierarchical. Per-template instructions solve the "different content" problem. Section optional with escape hatch |
| H6b | Business processes need explicit representation in TFW | NEW | ✅ CONFIRMED | Two-level design validated across 4 domains. HL = where value delivered. RF = how value delivered. Natural fit in Diagrams section |
| H7b | Multi-iteration needs structural enforcement (iterations.yaml) | NEW (revised from RES1 H7) | ✅ CONFIRMED | 4 failure scenarios tested. User: "without YAML → fast-run." Coordinator gate = key enforcement. min_iterations = hard floor |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | §3 Target State: Replace "Doc Candidates + Knowledge Candidates" naming with "keep Strategic Signals + Fact Candidates (sharpened)" | D10, D11 — supersedes RES1 D2 |
| 2 | §4 Phase A: Add "extend Strategic Signals section to RES and RF templates" | D10 |
| 3 | §4 Phase A: Add "add Diagrams section to RF and RES templates, expand HL §3.1" | D12 |
| 4 | §4 Phase A: Add "two-level business process representation in Diagrams section instructions" | D13 |
| 5 | §4 Phase A: Add iterations.yaml format + researcher exit protocol + coordinator gate | D14 |
| 6 | §10 Hypotheses: Update H5, H6, H7 statuses per table above | All |
| 7 | §11 Strategic Session Insights: Rename to "Strategic Signals" | D10 |

## Fact Candidates

> (Demonstrating the split: §FC = agent-observed, §SS would be Strategic Signals from conversation)

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC10 | process | LLM category naming triggers specific cognitive modes: "Knowledge" = retrieval (lists facts), "Strategic" = synthesis (identifies implications), "Signal" = detection (filters for decision-relevant items). Name choice is a functional lever, not just semantics | External research (2026-04-10), Gather G1 | ★★☆ |
| FC11 | process | arc42 model places diagrams at EVERY artifact level with level-appropriate content and instructions. Universal section name + per-template instructions = proven pattern in architecture documentation | External research (2026-04-10), Gather G2 | ★★☆ |
| FC12 | process | Multi-iteration research follows "Checkpoint-Resume" pattern: define critical moments, save structured state, resume from last known state. The control file is read at session start — matching TFW's filesystem-as-state-machine design (D31) | External research (2026-04-10), Gather G4 | ★★☆ |

**Strategic Signals (from conversation):**

| # | Category | Signal | Source | Confidence |
|---|----------|--------|--------|------------|
| SS1 | philosophy | "Strategic" as a naming vector gives agents FOCUS on what to search for. "Knowledge" is too broad — agent writes everything. Naming precision = capture precision | User (2026-04-10), briefing Q1 | ★★★ |
| SS2 | process | "Without YAML or statuses, agents will fast-run every time. Agents always want to finish faster." — structural enforcement principle for any iterative AI workflow | User (2026-04-10), briefing H7b correction | ★★★ |
| SS3 | process | Multi-iteration research is a confirmed valuable pattern. User wants it as explicit feature, not accidental capability. Coordinator-driven, structurally enforced, with visibility into iteration state | User (2026-04-10), briefing + HL S17 | ★★★ |
| SS4 | stakeholder | User distinguishes between being agreed with vs being validated through evidence. "Я то согласен, но лишь бы ИИ просто не льстил мне. Надо варианты рассмотреть." — demands adversarial analysis, not confirmation | User (2026-04-10), Extract preparation | ★★★ |

## Conclusion

Iteration 2 addressed 4 gaps from RES1 across 3 stages using external research (LLM naming theory, arc42/C4, BPMN/VSM, checkpoint-resume patterns) and scenario-based testing.

The central finding is that RES1 D2 (rename to "Doc Candidates + Knowledge Candidates") was wrong — it replaced precise names with vague ones. The correct fix is D10: keep "Strategic" framing (D28-validated), sharpen it to "Strategic Signals" (better edge-case coverage than "Insights"), and EXTEND the section to all result artifacts (RES, RF). "Fact Candidates" stays for agent-observed patterns.

Visualization needs a "Diagrams" section in RES and RF templates (HL §3.1 already exists, needs expansion). Business processes fit naturally as two-level content within Diagrams: HL = value delivery flow, RF = technical process detail. Multi-iteration research needs structural enforcement via iterations.yaml + coordinator gate — confirmed through both user experience and 4 failure scenario tests.

Self-critique: The visualization section naming (Q5) is the least resolved decision — "Diagrams" works but better options may exist. The §6 Fact Candidates sharpening (Q6) is deferred but not urgent. The main gap: I didn't investigate how Strategic Signals consolidation differs from Fact Candidates consolidation in /tfw-knowledge — does the workflow need separate processing for each?

## Iteration Status

- **Iteration:** 2 of 2 (min_iterations from user input)
- **Tested:** H5b (naming precision), H6 (visualization), H6b (business processes), H7b (multi-iteration enforcement)
- **Deferred/Remaining:**
  - Q5: Visualization section exact name (recommend iteration 3 if user wants deeper exploration)
  - Q6: §6 "Fact Candidates" scope sharpening (not urgent)
  - Q7: plan.md insertion point for coordinator iteration gate
  - Strategic Signals consolidation path in /tfw-knowledge
- **New hypotheses:** None generated
- **Gaps discovered:**
  - /tfw-knowledge workflow update for Strategic Signals processing
  - Visualization naming (partial)

### Recommendation: SUFFICIENT (with notes)

Core hypotheses resolved. Naming direction clear (D10 supersedes RES1 D2). Visualization, business processes, and multi-iteration all have actionable designs. Remaining open questions (Q5-Q7) are detail-level and can be resolved during TS or execution.

If user wants to explore visualization naming deeper → launch iteration 3 in a new agent.
Otherwise → proceed to `/tfw-plan` to update HL and write TS.

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

---

*RES — TFW-32 Iteration 2: Naming, Visualization, Multi-Iteration | 2026-04-10*
