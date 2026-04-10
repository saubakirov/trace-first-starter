# HL — TFW-32 / Phase B: Naming & Templates

> **Date**: 2026-04-10
> **Author**: AI (Coordinator)
> **Status**: 📝 HL_DRAFT — Awaiting review
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)

---

## 1. Vision

Section names in TFW templates are empirically validated micro-prompts. §6 "Fact Candidates" triggers pure reporting mode. §7/§11 "Strategic Insights" triggers deep analytical synthesis. Visual sections have per-template names that activate the correct cognitive mode per context: HL = "Value Flow" (strategic), RF = "Diagrams" (technical), RES = "Findings Map" (analytical). §3.1 "Result Visualization" stays as a separate concept — Amazon Working Backwards outcome preview. Every template, glossary, and conventions entry is consistent.

**Impact:** After this phase, (1) every template has sharpened §6/§7 instructions that reliably trigger the correct LLM cognitive mode, (2) agents writing HL produce strategic value visualizations, not confused tech diagrams, (3) RES and RF have visual sections for the first time, (4) conventions.md has a cross-reference table documenting per-template visual section names, (5) glossary reflects all new terms.

> "Section name = strongest single-word prompt. If named right, AI needs fewer instructions."

## 2. Current State (As-Is)

### 2.1 §6 Fact Candidates — instructions need sharpening

| Template | Current §6 state | Problem |
|----------|------------------|---------|
| RF | Has section + good instructions | "Human-Only Test" framing works but scope unclear: agent sometimes records implementation details |
| RES | Has section + minimal instructions | Weaker instructions than RF. Missing "project-level facts" scope clarifier |
| REVIEW | Has section + RF-level instructions | Same as RF — adequate but could be tighter |
| HL | No §6 — correct (HL is planning, not execution) | N/A |

**Research finding (RES3 D16):** Name "Fact Candidates" is empirically optimal. Triggers pure reporting: "record factual without adding interpretation." 5-variant comparison: original outperformed all alternatives. 31 tasks of backwards-compatible usage.

### 2.2 §7/§11 Strategic Insights — inconsistent across templates

| Template | Current state | Problem |
|----------|---------------|---------|
| HL §11 | "Strategic Session Insights" — has instructions | Name inconsistent with §7. Missing qualifier "(Planning)" |
| RF §7 | Section does NOT exist | RF has no Strategic Insights section — executor-observed human knowledge is lost |
| RES | Section does NOT exist in template | RES3/RES4 added it ad-hoc ("Strategic Insights (from conversation)") — not in canonical template |
| REVIEW | No section | REVIEW is checklist/verdict — correct: no Strategic Insights needed |

**Research finding (RES3 D15):** Name "Strategic Insights" is empirically optimal. Triggers deepest analytical mode — model ADDS implications not in input. 7-variant comparison. Supersedes D2 (Doc/Knowledge Candidates) and D10 (Strategic Signals).

**Research finding (RES4 D25):** Keep ONE name + qualifier: "(Planning)" in HL, "(Execution)" in RF, "(Research)" in RES. Qualifiers serve human readability; zero cost.

### 2.3 No visual section in RF or RES

| Template | Current visual | Problem |
|----------|---------------|---------|
| HL | §3.1 "Result Visualization" | Exists, works, but framing could be enhanced with Working Backwards |
| HL | No "Value Flow" section | Strategic value delivery visualization has no canonical place |
| RF | None | Technical diagrams (architecture, flow) have no designated section |
| RES | None | Research findings visualization (root cause, priority matrix) has no designated section |

**Research finding (RES4 D22):** Per-template naming for visual section. Decision criterion: "Does the cognitive mode CHANGE between templates?" Answer: YES.

**Empirical evidence (Experiment 1, Qwen3.5-27B):** 6 names → 6 distinct cognitive modes:
- "Value Flow" → strategic/value-oriented (INPUT→PROCESSING→OUTCOME)
- "Diagrams" → technical/engineering (mermaid, ERD, architecture)
- "Findings Map" → analytical/research (root cause, hypothesis tree, priority matrix)
- "Result Visualization" → narrative/outcome (timeline, testimonials, "imagine done")
- "Visual Overview" → generic/unfocused (weakest — rejected)

**Empirical evidence (Experiment 2):** "Diagrams" in HL = confused output. "Value Flow" in HL = clean strategic output. Context × Name interaction validated.

**Research finding (RES4 D21):** HL has TWO visual concepts: §3.1 "Result Visualization" = WHAT done looks like (outcome preview). "Value Flow" = HOW value gets created (process visualization). Complementary, zero content overlap.

### 2.4 Glossary and conventions gaps

| Gap | Detail |
|-----|--------|
| glossary.md | Missing: Value Flow, Findings Map, per-template visual naming rule, strategic vs operational capture distinction |
| conventions.md | No cross-reference table for visual section names across templates |
| conventions.md §3 | "Fact Candidates" definition exists but lacks cognitive mode description |

## 3. Target State (To-Be)

### 3.1 Result Visualization

```
BEFORE (naming):
  §6: "Fact Candidates"     → correct name, weak instructions in some templates
  §7: does not exist in RF or RES
  §11: "Strategic Session Insights" → inconsistent name, no qualifier
  Visual: only HL §3.1 "Result Visualization"

AFTER (naming):
  §6: "Fact Candidates"     → sharpened instructions in RF, RES, REVIEW
                               Scope: agent-observed project patterns
                               Mode: "report factual without interpretation"

  §7:  "Strategic Insights (Execution)"  → NEW in RF template
       "Strategic Insights (Research)"   → NEW in RES template

  §11: "Strategic Insights (Planning)"   → renamed from "Strategic Session Insights" in HL

  Visual sections (per-template):
    HL:  "Value Flow"     → NEW §3.2 (strategic value delivery)
    RF:  "Diagrams"       → NEW section (technical process detail)
    RES: "Findings Map"   → NEW section (research findings visualization)

  HL §3.1: "Result Visualization" → enhanced with Working Backwards framing
```

```
DECISION CRITERION:
  "Does the cognitive mode CHANGE between templates?"
    YES → per-template naming (visual section)
    NO  → unified naming (§6 Fact Candidates, §7/§11 Strategic Insights)
```

```
CONVENTIONS.MD CROSS-REFERENCE (new):

  | Template | §6 | §7/§11 | Visual Section |
  |----------|-----|--------|----------------|
  | HL       | —   | §11 Strategic Insights (Planning) | §3.2 Value Flow |
  | RF       | §6 Fact Candidates | §7 Strategic Insights (Execution) | § Diagrams |
  | RES      | § Fact Candidates | § Strategic Insights (Research) | § Findings Map |
  | REVIEW   | §5 Fact Candidates | — | — |
```

## 4. Deliverables

### Template changes

1. **HL template** — rename §11 "Strategic Session Insights" → "Strategic Insights (Planning)". Add §3.2 "Value Flow" with instructions for strategic value delivery visualization. Enhance §3.1 instructions with Working Backwards framing ("Show outcome as if achieved. This is NOT a process diagram")
2. **RF template** — add §7 "Strategic Insights (Execution)" section with instructions + Human-Only Test. Add visual section "Diagrams" for technical process diagrams. Sharpen §6 instructions: add scope clarifier ("agent-observed project patterns, NOT implementation details")
3. **RES template** — add "Strategic Insights (Research)" section with instructions + Human-Only Test. Add "Findings Map" section for research visualization (root cause, priority matrix, hypothesis tree). Sharpen §6 (Fact Candidates) instructions to match RF level
4. **REVIEW template** — sharpen §5 Fact Candidates instructions: explicit scope = "reviewer-observed project patterns during review process." No visual section needed (REVIEW = checklist/verdict, not result artifact)

### Documentation changes

5. **conventions.md** — add cross-cutting "Visual Sections" reference table (template × section name × cognitive mode). Update §3 Fact Candidates definition: add cognitive mode description ("triggers pure reporting: record factual without interpretation")
6. **glossary.md** — add terms: Value Flow, Findings Map, Strategic Insights qualifier explanation. Update Strategic Insight definition to include qualifiers. Add "per-template naming" concept

### What is NOT in scope

- §6 name change (D16: keep "Fact Candidates")
- §7/§11 name change (D15: keep "Strategic Insights")
- REVIEW visual section (REVIEW = checklist, not result)
- HL §6 section (HL is planning, not execution — no Fact Candidates)
- KNOWLEDGE.md changes (Phase A scope)
- Workflow changes (Phase A scope)

## 5. Definition of Done (DoD)

- ✅ 1. HL template §11 renamed to "Strategic Insights (Planning)" with tightened instructions
- ✅ 2. HL template has §3.2 "Value Flow" section with strategic visualization instructions
- ✅ 3. HL template §3.1 enhanced with Working Backwards framing
- ✅ 4. RF template has §7 "Strategic Insights (Execution)" with Human-Only Test
- ✅ 5. RF template has "Diagrams" visual section
- ✅ 6. RF template §6 has sharpened scope instructions
- ✅ 7. RES template has "Strategic Insights (Research)" section
- ✅ 8. RES template has "Findings Map" visual section
- ✅ 9. RES template §6 (Fact Candidates) has sharpened instructions matching RF level
- ✅ 10. REVIEW template §5 (Fact Candidates) has tightened scope instructions
- ✅ 11. conventions.md has "Visual Sections" cross-reference table
- ✅ 12. glossary.md has Value Flow, Findings Map, and updated Strategic Insight definitions

## 6. Definition of Failure (DoF)

- ❌ 1. §6 or §7/§11 RENAMED (research proved originals are optimal — renaming = regression)
- ❌ 2. Visual section has ONE name across all templates (empirically: causes confused output in wrong context)
- ❌ 3. Templates changed but glossary not updated (agents use old terms)
- ❌ 4. §3.1 and Value Flow merged into one section (they are TWO separate concepts with zero overlap)
- ❌ 5. REVIEW gets visual section (REVIEW = checklist, not result artifact)

**On failure:** Revert template changes. Re-read RES3 D15/D16 and RES4 D21/D22 before retrying.

## 7. Principles

1. **Naming = Prompting (D28)** — section name is the strongest single-word prompt. Empirically validated: correct name triggers correct LLM cognitive mode without additional instructions
2. **Per-template WHERE modes differ** — visual sections have different cognitive modes per template (strategic/technical/analytical). Use per-template names. §6/§7 have the SAME mode across templates. Use unified names
3. **Sharpen, don't rename** — for empirically optimal names (Fact Candidates, Strategic Insights), improve instructions while keeping the name
4. **Two visual concepts in HL** — §3.1 = outcome preview (Working Backwards). §3.2 Value Flow = process visualization. Complementary, not substitutable
5. **Quality Contract compliance** — every template change updates glossary.md and conventions.md in the same phase (from master HL §7.1)

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| TFW-32 Master HL approved | ✅ |
| RES1-RES4 complete | ✅ |
| Phase A complete (pipeline fixes) | 🟠 In progress |
| RES3 D15/D16 (naming validation) | ✅ Empirically validated |
| RES4 D21/D22/D24/D25/D26 (visual + qualifiers) | ✅ Empirically validated |

> Phase A is NOT a blocker for Phase B. Phase B changes templates; Phase A changes workflows. No file overlap.

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Per-template visual names confuse agents | Low | Medium | conventions.md cross-reference table + per-template instructions in each template |
| Adding §7 to RF bloats executor output | Low | Low | Instructions include "if no human interaction during execution, leave empty" |
| Adding §3.2 to HL creates confusion with §3.1 | Medium | Medium | Clear framing: §3.1 = WHAT done looks like, §3.2 = HOW value gets created. Both in instructions |
| Sharpened §6 instructions make agents too restrictive | Low | Medium | Test: verify agent still captures domain facts, not just code observations |

## 10. RESEARCH Case

Research complete at master HL level (4 iterations). Phase B decisions are empirically validated:

| Decision | Status | Source |
|----------|--------|--------|
| D15: Keep "Strategic Insights" | ✅ Empirical (7-variant comparison, Qwen3.5-27B) | RES3 |
| D16: Keep "Fact Candidates" | ✅ Empirical (5-variant comparison, Qwen3.5-27B) | RES3 |
| D21: Two visual concepts in HL | ✅ Empirical (Exp1: zero content overlap) | RES4 |
| D22: Per-template visual naming | ✅ Empirical (Exp1 + Exp2: context × name interaction) | RES4 |
| D24: §6 unified naming | ✅ Analytical (same cognitive mode across templates) | RES4 |
| D25: §7/§11 unified + qualifier | ✅ Analytical (qualifiers for human readability) | RES4 |
| D26: §3.1 Working Backwards framing | ✅ Empirical (Exp1: narrative timeline output) | RES4 |

No additional research needed for Phase B.

---

*HL — TFW-32 / Phase B: Naming & Templates | 2026-04-10*
