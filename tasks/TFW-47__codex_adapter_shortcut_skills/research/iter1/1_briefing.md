# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-47](../../HL-TFW-47__codex_adapter_shortcut_skills.md)
> Goal: Every completed task produces a mandatory `evidence/` folder with a structured template file capturing real verification results — closing the gap where evidence was defined but never physically materialized (0/38 tasks).

## Research Plan

**Gather (Explorer):**
- Survey all existing TFW artifact naming conventions (HL, TS, RF, RES, ONB, REVIEW, EV?) — identify naming patterns
- Examine 3-5 completed task folders to catalog what was actually verified and how (inline RF §5 claims)
- Identify candidate dimensions: naming scheme, template structure depth, proportionality mechanism, mandatory vs optional sections
- Look at external evidence/verification template patterns (audit trails, compliance docs, test reports)

**Extract (Analyst):**
- Build configuration space: name options × structure depth × proportionality approach
- Cross-reference each combination against TFW values (trace-first, honest, structured, reproducible)

**Challenge (Critic):**
- Test top candidates against 3 real past tasks (trivial fix, medium refactor, complex multi-phase)
- Check: does the template capture what was verified without creating disproportionate overhead?

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | A single structured evidence template file per task (not per-AC) is sufficient for traceability | open |
| H2 | The evidence template should include environment metadata (OS, tool versions, timestamps) for reproducibility | open |

## Scope Intent
- **In scope:** Evidence template file naming, internal structure, proportionality mechanism, alignment with TFW naming/values. How the template handles trivial vs complex tasks.
- **Out of scope:** Codex adapter mechanics (iteration 2). Workflow integration details (HL Phase A deliverables 2-7, not research scope). How review workflow audits evidence (already defined in D52).

## Guiding Questions
1. Should the evidence file use a 2-letter abbreviation (like HL, TS, RF) or a longer name (like `evidence.md`)? Any preference?
2. Should the template enforce per-AC evidence rows (one row per acceptance criterion) or allow freeform?
3. Is there a minimum evidence bar even for trivial tasks (e.g., "I ran the linter, output was clean")?

## User Direction

1. **Naming:** `EV` abbreviation is accepted. Pattern: `EV__TFW-{N}__{title}.md` — consistent with HL/TS/RF/RES/ONB/REVIEW.
2. **Per-AC vs freeform:** User doesn't know — needs research to decide.
3. **Minimum evidence bar:** Needs empirical research from real TFW projects. User's most active projects: **helpdesk**, **afd**, **tfw** (this repo). Research should examine what was actually verified in completed tasks across these projects.

---
Stage complete: YES
