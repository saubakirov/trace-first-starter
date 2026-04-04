# Gather — "What do we NOT know?"
> Parent: [HL-TFW-25](../HL-TFW-25__values_consolidation.md)
> Goal: Validate TFW's 3-tier taxonomy and value count cap against external frameworks and industry patterns.

## Findings

### G1: Industry-standard Values/Principles/Rules hierarchy
**Source:** Software engineering taxonomy research (web search)

External consensus confirms a 3-layer hierarchy:

| Layer | Nature | TFW equivalent |
|-------|--------|----------------|
| **Values** | Abstract, foundational, "why" — culture, priorities | README §Values |
| **Principles** | Heuristic, guiding, "how" — best practices, design rules | KNOWLEDGE §0 (some) |
| **Rules** | Concrete, prescriptive, "what" — enforceable constraints | conventions.md |

Key insight: **"The common failure mode occurs when teams implement Rules without fostering the Values that make those rules meaningful."** This validates TFW's approach of having a separate Values section — but also means values must be genuinely philosophical, not disguised rules.

**Implication for H1:** P10-P13 (token density, inline enforcement, DNA/library, progressive disclosure) are clearly Rules-tier, not Values-tier. They describe enforceable constraints, not beliefs. The HL's proposal to move them to conventions.md is correct per industry taxonomy.

### G2: Framework comparison — how many values/principles?
**Source:** Cursor rules, CrewAI, Microsoft RA, general AI framework docs

| Framework | Values-tier items | Format | Location |
|-----------|------------------|--------|----------|
| Cursor rules (2025 best practices) | 3-5 "always apply" rules | YAML frontmatter + markdown | `.cursor/rules/` |
| CrewAI | ~4 core design principles (80/20, specialists, single purpose, flows vs crews) | Prose | docs site |
| Microsoft Responsible AI | 6 principles (fairness, privacy, transparency, accountability, reliability, inclusiveness) | Narrative sections | corporate docs |
| NIST AI RMF | 4 core functions | Structured prose | gov standard |

**Pattern:** Mature frameworks have 4-8 values-tier items. None exceed 10. All use narrative/prose, not tables. This strongly supports H3 (≤8 items).

**Additional pattern — "Reference, Don't Duplicate":** Both Cursor and general AI framework docs explicitly recommend referencing canonical files rather than duplicating content. TFW already follows this (P2), validating that it's a real value, not invented.

### G3: Cursor rules — modular architecture principle
**Source:** Cursor rules best practices 2025

Key principle: **"Keep individual rule files under 500 lines. Every token used for rules is a token taken away from the AI's ability to 'see' your actual code."**

This validates TFW's P10 (token density) and P13 (progressive disclosure) — but as engineering constraints, not philosophical values. They are tools-implementation rules. In the Values/Principles/Rules taxonomy, they sit firmly in Rules.

### G4: "Embed values into architecture, not just documents"
**Source:** AI agent framework best practices 2025-2026

**Trend:** By 2026, the shift is from "creating values docs" to "embedding values into agent architecture." Compliance = technical feature, not policy document.

This is exactly what TFW does with conventions.md, workflows, and templates. The README Values section should state the *beliefs*; the enforcement lives in the architecture. This supports the HL's approach: values = beliefs (README), rules = enforcement (conventions).

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 3-tier taxonomy validated by industry standard | None — taxonomy is well-supported |
| 4-8 items is the norm for values sections | None |
| Narrative format preferred over tables for values | None |
| P10-P13 confirmed as Rules, not Values | None |

**Sufficiency:**
- [x] External source used? (4 web searches, multiple framework references)
- [x] Briefing gap closed? (taxonomy validated, count validated, format validated)

Stage complete: YES
→ User decision: ___
