# RES — TFW-25: Values & Principles Consolidation

> **Date**: 2026-04-04
> **Author**: Researcher (AI)
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-25](HL-TFW-25__values_consolidation.md)
> **Mode**: Pipeline

---

## Research Context

TFW accumulated 14 principles (P1-P14), 33 architecture decisions (D1-D33), and 29 knowledge facts across 24 tasks. These live in 3 places (README Values, KNOWLEDGE §0, knowledge/ topic files) with heavy duplication and no clear hierarchy. This research validates the proposed consolidation approach: what taxonomy to use, what to keep, what to prune, and how to restructure README Values as the philosophical face of TFW.

## Briefing

See [research/briefing.md](research/briefing.md). Three hypotheses tested. Focused mode: 1 OODA loop per stage. User direction: philosophy facts = keep, narrative format stays, no missing principles. "Naming Creates Behavior" confirmed as a philosophical belief (linguistic relativity analogy).

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| R1 | 3-tier taxonomy (Values / Design Principles / Rules) is correct | Validated by industry standard (Values = why, Principles = how, Rules = what). Middle tier (KNOWLEDGE §0) earns its existence: 7 items too specific for README, too strategic for conventions |
| R2 | README Values: 8 items (was 5). Add "Traces Over Code", "Structural Enforcement", "Naming Creates Behavior". Rename "Determinism and Safety" → "Honesty Over Convincingness" | External frameworks: 4-8 values is the norm. "Traces Over Code" was in §Thesis but missing from §Values. New values sourced from P14, D28. Rename: current text is rules, not beliefs — rewrite as genuine value statement |
| R3 | KNOWLEDGE §0: 7 items (was 14). Remove P4, P6, P10-P13. Keep P1-P3, P5, P7-P9 (compressed). Promote P14 to README | P4/P6 = obvious from code. P10-P13 = engineering rules (token limits, inline patterns, DNA/library, progressive disclosure) — belong in conventions, not philosophy. P14 = philosophical belief about structural enforcement |
| R4 | knowledge/ facts: 18 facts (was 29). Prune 11 self-evident facts (6 convention, 5 process). Keep all philosophy + constraint | Self-evidence test: "Is this now obvious from the code it describes?" Convention F4/F6/F8-F10/F12 and Process F2/F3/F8-F10 are all demonstrated by the artifacts they describe. Exception: convention/F5 (ref-inside-step) kept — the named pattern has value beyond code (D28) |
| R5 | KNOWLEDGE §3 Legacy: prune 18 of 35 items (all pre-TFW-22, fully resolved) | Historical items from TFW-2 through TFW-15 era. Replacements fully implemented. No active references. Keep TFW-22 through TFW-24 items (recent, may still be referenced) |
| R6 | KNOWLEDGE §4 Tech Stack: remove entirely | 4 lines of trivially obvious content (Markdown, Git, IDE tools, MIT license). Derivable from repo files |
| R7 | "Determinism and Safety" → "Honesty Over Convincingness" — rename, not remove | External research: safety belongs at both value and rule layers. Current README text is 5 implementation rules, not a belief. Rewrite as value: "AI that sounds confident while being wrong > AI that refuses to answer." Rules stay in conventions §12 |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Where do P10-P13 land after removal from §0? | Open | HL proposes conventions.md §X "Design Rules" or integrate into §11. TS should decide exact placement |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | P10-P13 are implementation rules, not principles — they belong in conventions.md | open | ✅ confirmed | Industry taxonomy: all 4 are "Rules" tier (concrete, prescriptive, enforceable). Token limits, inline patterns = engineering constraints |
| H2 | ≥5 knowledge/ facts are now self-evident from code and can be safely removed | open | ✅ confirmed (11) | 11 facts pass self-evidence test. Code/templates/workflows demonstrate them. Info loss risk verified per fact in Challenge |
| H3 | README Values section should stay under 8 items to maintain narrative impact | open | ✅ confirmed (exactly 8) | External benchmarks: Microsoft RA = 6, CrewAI = 4, Cursor = 3-5. No mature framework exceeds 10. 8 = upper bound of healthy range |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| U1 | §3 Target: update value count from 6-8 → exactly 8. Add "Honesty Over Convincingness" (renamed, not removed) | Challenge C1 |
| U2 | §3 Target: knowledge/ fact count from ~20 → 18 (adjusted from 12 prunable to 11) | Challenge C3 |
| U3 | §4 Phase A step 1: include "Honesty Over Convincingness" rewrite alongside other README changes | Challenge C1 |
| U4 | §5 DoD item 1: update range from "6-8 values" → "8 values" | R2 |
| U5 | §5 DoD item 6: update from "≤22 facts" → "18 facts" | R4 |
| U6 | Phase B: add step for P10-P13 placement in conventions.md — needs exact section decision | Q1 |

## Fact Candidates

> Reviewing conversation history — the user's key input was the philosophical grounding for "Naming Creates Behavior" (linguistic relativity / Sapir-Whorf analogy). This is already captured in process/F5. No new strategic facts emerged from this research beyond what's already in the knowledge base.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | philosophy | "Honesty Over Convincingness" framing: AI confidence without correctness is more dangerous than refusal. This is TFW's safety belief — distinct from the implementation rules in conventions §12 | Challenge C1 + external research | High |
| FC2 | convention | Mature AI frameworks universally use 4-8 items for top-level values/principles. None exceed 10. Narrative format (heading + paragraph) preferred over tables for values sections | Gather G2 (Microsoft RA, CrewAI, Cursor, NIST) | High |

## Conclusion

This research validated the HL's core proposal (3-tier taxonomy, pruning strategy) with two significant corrections: (1) "Determinism and Safety" should be renamed and rewritten as a genuine value ("Honesty Over Convincingness"), not removed — external research confirmed safety belongs at the values layer; (2) convention/F5 (ref-inside-step pattern) should be kept because the named pattern has value beyond its code implementation (D28 applies). The industry-standard Values/Principles/Rules hierarchy maps precisely to TFW's README/KNOWLEDGE/conventions structure, giving confidence that the consolidation will produce a well-organized, maintainable framework. Final numbers: 8 README values, 7 KNOWLEDGE §0 principles, 18 knowledge/ facts, 17 Legacy items.

---

*RES — TFW-25: Values & Principles Consolidation | 2026-04-04*
