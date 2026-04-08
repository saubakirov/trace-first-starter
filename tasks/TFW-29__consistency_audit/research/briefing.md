# Briefing
> Parent: [HL-TFW-29](../HL-TFW-29__consistency_audit.md)
> Goal: Reference files (conventions.md, glossary.md) and 11 workflows are free from redundancy, contradiction, and dead weight — agents load minimum tokens for maximum signal.

## Research Plan

**Gather:**
- Read every workflow's Context Loading / Step 1 section verbatim — extract exactly which files and §-sections each workflow loads
- Read every inline §-reference in every workflow step (not just headers — grep for `§`, `conventions`, `glossary`)
- Read adapter entry points (AGENTS.md, .agent/rules/agents.md, .agent/rules/tfw.md) for what they trigger
- Search external: best practices for AI prompt framework documentation — DRY vs self-contained tradeoffs
- Catalog all anti-pattern blocks across all files (handoff, README, conventions)

**Extract:**
- Build Section Usage Matrix: rows = conventions.md §1-§16, columns = 11 workflows + adapters. Cell = reads/references/ignores/duplicates
- Build Glossary Dependency Map: each glossary term → which workflow(s) need it, where else it exists
- Identify Common Spine (shared loading) vs Divergence Points (per-workflow-specific reads)
- Quantify: how many tokens does the current redundancy cost per session?

**Challenge:**
- Test H2: is the common loading spine real, or do workflows actually diverge significantly?
- Test H4: remove glossary from the mental model for handoff workflow — what term is missing?
- Counter-argument: maybe glossary duplication is USEFUL (self-contained context per role)
- Risk-check: which specific compressions in HL §2.4 could break a workflow?

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | Compilable Contract (§16) is never read by any workflow at runtime — can be safely extracted | confirmed |
| H2 | All workflows follow the same 4-step context loading pattern but then diverge — divergence points reveal which convention sections are actually needed per role | open |
| H3 | Anti-patterns in .tfw/README.md, handoff.md add unique items not in conventions.md §14 | confirmed |
| H4 | Glossary is loaded by every workflow via context loading, but only Research workflows actually need glossary-unique terms (Stage, Pass, OODA); other workflows could skip it entirely | open |

## Scope Intent
- **In scope:** Reading flow tracing for all 11 workflows + 3 adapters. §-reference mapping for conventions.md and glossary.md. Anti-pattern block comparison. External research on DRY documentation patterns for AI agents.
- **Out of scope:** Actually making edits. .tfw/README.md internal content (already stripped in TFW-27). Template files (they reference conventions but aren't loaded at session start). gen_docs.py / compilable contract internals (confirmed independent by H1).

## Guiding Questions
1. For H4 specifically: do you see any non-Research workflow where a glossary-unique term matters at runtime? (I'll verify either way, but your intuition helps scope.)
2. The HL proposes compressing glossary to ~80 lines. Is there a hard floor — a minimum glossary size you'd consider acceptable even if all terms could technically be refs?
3. Anti-patterns: should the authoritative list in conventions §14 be strictly executor-focused, or should it include coordinator/reviewer anti-patterns too (currently mixed)?

## User Direction
1. **H4 — glossary terms:** User says "check yourself" — will verify empirically by tracing all workflows.
2. **Glossary floor:** "maybe 80 too small" — user unsure. Research should determine empirically how many lines glossary actually needs. No hard floor imposed.
3. **Anti-patterns scope:** User leans toward separated by role but uncertain. Research should evaluate whether role-separated anti-patterns or a unified list works better.

---
Stage complete: YES
