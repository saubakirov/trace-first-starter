# Briefing
> Parent: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> Goal: Add structural gates to every critical TFW handoff point so that failures are prevented, not just detected.

## Research Plan

### Gather
- Mine Helpdesk HD-9 through HD-18 task artifacts (TS, RF, REVIEW, ONB) for concrete evidence of problems #1-9 from HL §2
- Extract TS size/content metrics across HD-16 phases (A-D) — verify the inverse correlation claim (S2)
- Collect examples of coordinator plan≠fact drift from HD-18 artifacts
- Search external sources: "requirements-driven task specifications", "quality gates in agile", "execution loops in engineering workflows"
- Research Zwicky's Morphological Box: original methodology, modern applications, AI/research context applicability

### Extract
- Build parameter matrix: gate type × enforcement point × verification method × token cost
- Apply Zwicky Box to TFW-41's own solution space as a live test of H4
- Compare Requirements-first TS pattern against industry alternatives (BDD/Gherkin, ATDD, Shape Up pitches)
- Evaluate token/word budget impact of proposed gates on existing workflows (handoff.md, plan.md, review.md)

### Challenge
- Stress-test Execution Loops against real HD-16 Phase C: would they have caught per_page=100 vs spec 500?
- Stress-test Pre-TS Gate against HD-18: would reading RF Phase N-1 have prevented the 3 errors?
- Counter-evidence: when do gates ADD overhead without catching errors? (false positive rate)
- Challenge Zwicky Box: is it genuinely useful for AI research or is it overhead that a good researcher does implicitly?

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | Requirements-first TS reduces "Phase D cleanup" phases | open |
| H2 | Pre-TS Gate (read RF N-1) eliminates plan≠fact drift errors | open |
| H3 | Execution Loops catch more issues than linear execution | open |
| H4 | Zwicky's Morphological Box in research Extract/Synthesis improves decision quality by making researchers systematically consider parameter combinations instead of picking first viable option | open |

## Scope Intent
- **In scope:** Evidence from Helpdesk project (HD-9..HD-18). External research on quality gates, requirements-driven specs, Zwicky Box. Token budget analysis for proposed workflow changes. TS template structure analysis.
- **Out of scope:** Implementation of changes (that's execution). Other projects beyond Helpdesk for evidence. Changes to research workflow beyond Extract/Synthesis (per HL §10 note on H4).

## Guiding Questions
1. The Helpdesk project is at `d:\projects\research\helpdesk\` — should I mine ALL task folders (HD-9 through HD-18) or focus on the specific cases cited in the HL (HD-9, HD-16, HD-18)?
2. For H4 (Zwicky Box): is the intent to add it as a mandatory tool in research Extract, or as an optional technique the researcher MAY use?
3. Are there other live projects beyond Helpdesk where you've observed the same 9 problems?

## User Direction
1. **Focus on cited cases only:** HD-9, HD-16, HD-18. Don't mine all HD-9..HD-18.
2. **Zwicky Box = mandatory** tool in research Extract stage (not optional).
3. **TFW project itself** may have evidence of the same problems — check TFW tasks too.

---
Stage complete: YES
