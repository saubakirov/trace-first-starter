# Briefing — Iteration 2
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: Design the staged review structure and resolve remaining open threads from iteration 1.
> Predecessor: [RES iteration 1](../RES__TFW-38__quality_enforcement.md)

## Predecessor Decisions to Build On
- D1: Explicit §6-8 enumeration in handoff.md — CONFIRMED, ready for TS
- D2: Reviewer audit step with triage gate — CONFIRMED, but may be superseded by staged review
- D3: Diagram collection → index, not copy — needs concrete format
- D5: Review should have staged structure — USER CLARIFIED: domain-specific gates (requirements, code quality, security), not literal research flow

## Open Threads from Iteration 1
1. **Staged review workflow** — design domain-specific review stages. User clarified: like industry multi-gate patterns (requirements validation, code quality, security). NOT exact research flow stages.
2. **Two classes of TFW workflows** — investigative (staged) vs procedural (linear). Map all workflows.
3. **Diagram indexing format** — concrete KNOWLEDGE.md §2 format for diagram references.

## User-Injected Direction (post-RES1)
"Better for review: requirements validation, code quality, security — something like this. When I told like research, I mean the flow or idea, but not exact research flow."

## Research Plan

### Gather
- Search: how do production AI code review systems structure multi-gate reviews? What stages/gates are standard?
- Analyze existing TFW REVIEW files — what "natural stages" do good reviewers already follow?
- Check review.md word budget — can staged structure fit in 1200 words?

### Extract
- Design the concrete review stage set for TFW
- Map how the REVIEW template checklist maps to stages
- Define what the reviewer does in each stage (action, not just read)
- Propose diagram index format for KNOWLEDGE.md

### Challenge
- Test: does staged review create stage-file overhead that breaks the review's purpose?
- Test: can the 9-point (now 10-point) checklist be decomposed into stages cleanly?
- Test: does this exceed the 1200-word workflow budget?

## Hypotheses (from HL §10 + iteration 1)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | Explicit §6-8 enumeration stops skipping | 🟢 confirmed (iter 1) |
| H2 | Audit verification step changes reviewer behavior | 🟢 confirmed (iter 1) |
| H3 | Domain-specific review stages (not single-pass) will produce more reliable reviews | open (new, from user direction) |

## Scope Intent
- **In scope:** Review stage design, REVIEW template adjustment, diagram indexing format, workflow classification
- **Out of scope:** Implementing the changes (that's TS/handoff), changing the research workflow, handoff.md changes (already confirmed in iter 1)

## Guiding Questions
1. Should review stages produce intermediate files (like research stage files) or stay within the single REVIEW artifact?
2. Is the staged structure mandatory for ALL reviews, or only code/implementation reviews (with a triage bypass for docs)?

---
Stage complete: NO
