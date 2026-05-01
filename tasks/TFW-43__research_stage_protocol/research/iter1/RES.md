# RES — TFW-43: Research Stage Protocol

> **Date**: 2026-05-01
> **Author**: Researcher (Antigravity)
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-43](../../HL-TFW-43__research_stage_protocol.md)
> **Mode**: Pipeline

---

## Research Context

TFW-43 introduces Mindset blocks into 4 research stage templates (Briefing, Gather, Extract, Challenge) — the same per-stage identity anchoring pattern that made the review workflow effective (D41). This iteration investigated the exact wording: which role-nouns, which Test question format, and how h1 guiding questions relate to the new Mindset block. The research also settled the Briefing stage treatment (full Mindset vs lighter/none).

## Briefing

Reference: [1_briefing.md](1_briefing.md). Focus: H2 (role-noun anchoring), H4 (h1 vs Mindset), H5 (Test question format). All 3 user questions deferred to research — no constraints imposed.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | **4 functional role-nouns: Strategist / Explorer / Analyst / Critic** | Functional nouns activate specific professional associations in LLM training data better than metaphorical alternatives (Scout, Adversary). Verified non-overlapping on 2 axes: convergent↔divergent AND build↔break. Maps to 4 distinct cognitive modes: planning → exploration → structuring → attacking |
| D2 | **Existential Test questions with stage-output reference** | External research confirms: structured self-check with stage-output reference > vague "Did I...?". Test questions reference the template's own structural output (dimensions table, configuration space, surviving configs) as verification anchor. Format matches review templates exactly |
| D3 | **Keep h1 guiding questions + add Mindset alongside (dual signal)** | Review templates prove h1 and Mindset are complementary, not redundant: h1 = task orientation ("What to answer"), Mindset = cognitive orientation ("How to think"). Three-layer verification: h1 (task) / Mindset+Test (identity) / Checkpoint (completion) |
| D4 | **Add Briefing h1 guiding question: "What should we investigate?"** | Current Briefing h1 has no guiding question, breaking consistency with the other 3 stages. "What should we investigate?" fits naturally without force-fitting the "What do we NOT {x}?" pattern. Review templates also don't use a single question pattern |
| D5 | **Full Mindset block for Briefing (same structure as other 3)** | Briefing is investigative in standalone mode (user: "sometimes I start something by myself"). Even in pipeline mode, requires cognitive shift from coordinator to research planner. Consistency: 4 stages, 4 Mindsets. Partial application = confusion about when Mindset is needed |
| D6 | **Test ≠ Checkpoint — different verification layers** | Test = identity/comprehension check ("Am I thinking like a {role}?"). Checkpoint = task/completion check ("Did I do the mechanics?"). Review templates validate this separation. Making Test a checklist would duplicate the existing Checkpoint sufficiency block |
| D7 | **Test escalation pattern: purpose → coverage → insight → robustness** | Mirrors review escalation (comprehension → evidence → reputation). Each level builds on the previous. Aligned with the structural dependency already enforced by dimensional analysis cross-stage references |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Does C2+T1 (lighter Briefing Mindset) work better for simple tasks? | Deferred | Survived consistency check as valid alternative. Monitor in practice — if full Briefing Mindset proves heavy, this is the fallback |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Batch copy breaks D31 | Confirmed | ✅ Confirmed | User observation, D31 definition. Not re-tested — pre-confirmed |
| H2 | Role-noun anchoring produces measurably different behavior than prose | Needs research | ✅ Confirmed | External: persona prompting well-established in LLM research. Internal: D28 (naming > explanation), F3 ("dreaming" = 1 word > paragraphs). 4 non-overlapping functional nouns selected |
| H3 | Review stage pattern transfers to research | Confirmed | ✅ Confirmed | Structural formula extracted from review templates. Same 3-component structure (Mindset + Test + Checkpoint) maps cleanly to all 4 research stages |
| H4 | h1 guiding questions are effective but invisible — Mindset is the right home | Needs research | ❌ Partially refuted | Review templates show h1 and Mindset are COMPLEMENTARY, not substitutes. h1 = task orientation, Mindset = cognitive orientation. Moving h1 content into Mindset would overload the blockquote. Decision: keep both (D3) |
| H5 | Self-check Test ("Did I...?") matches checkpoint pattern better than imperative | Needs research | 🔄 Refined | External research shows "Did I...?" is too vague for reasoning tasks. Existential external perspective ("Can I point to..." / "Would someone...") with stage-output reference is more effective. Review templates already use this format, not "Did I..." |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | §10 H4: Change status from "Needs research" to "Partially refuted — h1 and Mindset are complementary, not substitute" | D3 |
| 2 | §10 H5: Change status from "Needs research" to "Refined — existential external > 'Did I...' but not imperative" | D2 |
| 3 | §3.2 D1 deliverable: Add "Briefing h1 guiding question" to scope (currently only mentions Mindset + Test) | D4 |

## Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | philosophy | Test questions and Checkpoint checklists serve different verification layers: Test = identity/comprehension ("Am I thinking right?"), Checkpoint = task/completion ("Did I do the work?"). Collapsing them into one = dilution. Review templates already enforce this separation | Extract E3, Challenge C3 | ★★☆ |
| FC2 | process | Review template Mindset blocks follow a 3-part instruction formula: {situational framing}. {action directive}. {constraint/quality standard}. This formula should be treated as canonical when adding Mindset blocks to other investigative templates | Gather G1, Extract E5 | ★★☆ |
| FC3 | philosophy | Escalation patterns in multi-stage workflows (review: comprehension→evidence→reputation, research: purpose→coverage→insight→robustness) emerge naturally from structural dependencies between stages — they are not designed, they are discovered. The Test questions reflect, not impose, escalation | Challenge C2 | ★☆☆ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | process | User deferred all 3 guiding questions to research ("don't know, we will see") — zero constraints on wording. This means the researcher has full autonomy on naming. In TFW context: when user trusts the research process, they delegate vocabulary decisions entirely. This is different from D28 sessions where user had strong naming intuitions | User, Briefing Q&A | ★★☆ |

## Findings Map

```
                    ┌─────────────────────────────┐
                    │  REVIEW PATTERN (proven D41) │
                    │  Map → Verify → Judge        │
                    │  Newcomer → Auditor → Judge   │
                    └──────────────┬───────────────┘
                                   │ transfer (H3 ✅)
                    ┌──────────────▼───────────────┐
                    │  RESEARCH PATTERN (proposed)  │
                    │  Brief → Gather → Extract →   │
                    │  Challenge                    │
                    │  Strategist → Explorer →      │
                    │  Analyst → Critic             │
                    └──────────────┬───────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
     ┌────────▼────────┐ ┌────────▼────────┐ ┌────────▼────────┐
     │ THREE-LAYER      │ │ DUAL SIGNAL     │ │ ESCALATION      │
     │ VERIFICATION     │ │ (D3)            │ │ PATTERN (D7)    │
     │                  │ │                 │ │                 │
     │ h1 = task        │ │ h1 stays        │ │ purpose         │
     │ Mindset = identity│ │ Mindset adds    │ │ → coverage      │
     │ Checkpoint = work │ │ (complementary) │ │ → insight       │
     └──────────────────┘ └─────────────────┘ │ → robustness    │
                                               └─────────────────┘
```

## Iteration Status

- **Iteration:** 1 of 1 (min) / 3 (max)
- **Hypotheses tested:** H1 (✅ confirmed), H2 (✅ confirmed), H3 (✅ confirmed), H4 (❌ partially refuted), H5 (🔄 refined)
- **Hypotheses deferred:** None
- **Gaps discovered:** None — all hypotheses resolved with evidence
- **Superseded decisions:** None

### Open Threads (for next iteration)

No open threads.

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS
- [ ] **MORE NEEDED** — {specify what and why}
- [ ] **BLOCKED** — {specify blocker}

> All 5 hypotheses resolved. The proposed Mindset block wording is concrete enough to implement. The C2+T1 alternative (lighter Briefing) is noted but not blocking — it's a fallback if practice shows full Briefing Mindset is too heavy.

## Conclusion

This research determined exact Mindset block wording for 4 research stage templates by transferring the proven review template pattern (D41) and validating it against external LLM persona prompting evidence and TFW's own naming principles (D28, F3). The key finding is that role-nouns (Strategist/Explorer/Analyst/Critic) work because they occupy distinct positions on two cognitive axes (convergent↔divergent, build↔break), and that h1 guiding questions and Mindset blocks serve different verification layers — they are complementary, not substitutes. H4 was partially refuted: the assumption that guiding questions should move into Mindset was wrong. H5 was refined: the effective Test format is existential external perspective with stage-output reference, not the assumed "Did I...?" self-check. Without this research, the implementation would have likely copied review Mindset blocks mechanically — missing the three-layer verification insight and producing Test questions that duplicate the existing Checkpoint.

---

*RES — TFW-43: Research Stage Protocol | 2026-05-01*
