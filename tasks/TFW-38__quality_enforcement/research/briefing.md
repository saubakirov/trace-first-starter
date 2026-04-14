# Briefing
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: Empirical validation that TFW agents skip RF §6-8, reviewers rubber-stamp, and researchers omit Findings Maps — across real projects.

## Research Plan

### Gather
- Scan RF files from helpdesk, vlm-3, content marketing, and other active TFW projects
- Check which RF sections (§6 Fact Candidates, §7 Strategic Insights, §8 Diagrams) are present vs absent
- Scan REVIEW files — check if reviewers provide evidence or just checkmarks
- Scan RES files — check if Findings Map sections are present

### Extract
- Analyze handoff.md Phase 3 (lines 71-107) — what does it explicitly mention vs what it omits
- Analyze review.md Step 1 — is there any verification/audit instruction?
- Analyze research/base.md Step 6 — does it mention Findings Map?
- Cross-reference: do templates contain sections that workflows don't mention?

### Challenge
- Counter-hypothesis: maybe agents DO fill §6-8 when prompted well — check for positive examples
- Challenge the "workflow > template" claim — search for external evidence on LLM prompt-following behavior
- Check if audit-style review creates overhead that makes it impractical for trivial tasks

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | Adding explicit §6-8 enumeration to handoff.md Phase 3 will stop executors from skipping them | open |
| H2 | An audit verification step in review.md will change reviewer behavior from "trust" to "verify" | open |

## Scope Intent
- **In scope:** Empirical analysis of real TFW artifact quality; current workflow text analysis; external research on LLM instruction-following patterns
- **Out of scope:** Implementation of fixes (that's Phase A/B); CI/linting enforcement (TFW-34 scope); template format changes

## Guiding Questions
1. Which active projects have the most RF/RES/REVIEW files to sample from?
2. Are there any projects where §6-8 ARE consistently filled — and if so, what's different about the prompt or context there?
3. Is the diagram## User Direction

**Q1 answer:** Projects to scan: helpdesk (/d/projects/research/helpdesk), atamat (/d/projects/research/atamat), auto-schedule-prototype (/d/projects/research/auto-schedule-prototype), and steps-framework itself. Helpdesk is newest/most active. Atamat has most tasks but older TFW version. Scheduler has a few recent tasks.

**Q2 answer:** No projects where §6-8 are consistently filled — helpdesk is closest but only in the most recent phases.

**Q3 answer:** No — diagram collection has never been attempted.

**User steering (post-Challenge):** Review should be structured like the research flow — with explicit stages and cognitive mode transitions (Read → Verify → Challenge → Synthesize). This is a deeper insight than "add an audit step."

---
Stage complete: YES
