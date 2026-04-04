# Briefing
> Parent: [HL-TFW-25](../HL-TFW-25__values_consolidation.md)
> Goal: Consolidate TFW's 14 principles and 33 decisions into a clean hierarchy — README Values (beliefs), KNOWLEDGE §0 (design rules), conventions (implementation patterns) — eliminating duplication and pruning self-evident knowledge/ facts.

## Research Plan

### Gather
- Search externally: how do mature AI/dev frameworks (LangChain, CrewAI, Cursor rules, Anthropic's prompt engineering docs) structure their principles/values sections?
- Count items, tiers, and placement patterns in 3-5 external frameworks
- Compare: narrative vs. list vs. table formats for values

### Extract
- Full cross-reference: each P1-P14 and each knowledge/ fact — is it already expressed in conventions.md, workflows, or templates?
- Classify self-evident facts (the code IS the documentation) vs. strategic facts (only humans know this)
- Produce exact lists: what to remove, what to promote, what to compress

### Challenge
- Stress-test the 3-tier taxonomy (values / design principles / implementation rules) — is it the right split?
- Check if 8-value cap is too few or too many by comparing with external examples
- Test whether pruning any knowledge/ fact would actually cause information loss

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | P10-P13 are implementation rules, not principles — they belong in conventions.md | open |
| H2 | ≥5 knowledge/ facts are now self-evident from code and can be safely removed | open |
| H3 | README Values section should stay under 8 items to maintain narrative impact | open |

## Scope Intent
- **In scope:** README §Values structure, KNOWLEDGE.md §0/§3/§4 pruning, knowledge/ topic file audit, external framework comparison
- **Out of scope:** rewriting conventions.md content, adapter sync, template changes, any code changes

## Guiding Questions
1. Are there any knowledge/ facts that you consider strategically important despite being derivable from code? (I'll assume "no" unless you flag specific ones.)
2. Do you want the README Values section to remain pure narrative (paragraph per value), or would a table format be acceptable?
3. Is there a principle you feel is missing from the current P1-P14 that should be added during consolidation?

## User Direction
1. **Philosophy facts = keep.** Implementation-specific facts in convention/process/constraint = prunable if self-evident from code.
2. **Narrative format stays.** README Values = heading + paragraph per value (P3: narrative > DRY).
3. **No missing principles** to add during consolidation.

---
Stage complete: YES
