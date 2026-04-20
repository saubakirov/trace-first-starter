# ONB — TFW-41 / Phase C: Research Templates — Embedded Dimensional Analysis

> **Date**: 2026-04-20
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> **TS**: [TS__PhaseC__research_templates.md](TS__PhaseC__research_templates.md)

---

## 1. Understanding

Phase C embeds dimensional analysis into the three research stage templates (Gather, Extract, Challenge) and the connecting research workflow. The goal is to make morphological decomposition emerge naturally from the stage sequence — researchers fill sections because the cross-stage dependency forces them to, not because a methodology is mandated. A parallel terminology origin note in `conventions.md` traces the native TFW terms (Dimension, Configuration Space, Consistency Check) back to Zwicky's GMA — but this is maintainer-facing only and must never appear in researcher templates. 5 file modifications, 0 new files.

## 2. Entry Points

| File | Current State | Action |
|------|--------------|--------|
| `.tfw/templates/research/gather.md` | 25 lines — Findings + Checkpoint | Add `## Dimensions` before `## Findings` |
| `.tfw/templates/research/extract.md` | 25 lines — Findings + Checkpoint | Add `## Configuration Space` before `## Findings` |
| `.tfw/templates/research/challenge.md` | 25 lines — Findings + Checkpoint | Add `## Consistency Check` before `## Findings` |
| `.tfw/workflows/research/base.md` | 129 lines — Step 5 has OODA loop | Add dimensional analysis paragraph in Step 5 (≤6 lines) |
| `.tfw/conventions.md` | 430 lines — §14 ends at line 390 | Add terminology origin note after §14 anti-patterns |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. | — |

## 4. Recommendations (suggestions, not blocking)

1. **Conventions insertion point:** TS §6 Technical Guidance says "After §14 anti-patterns, before §15 Role Lock (or as subsection of §14 / new §14.1)." I recommend adding it as `## 14.1` (a subsection of §14) rather than a free-floating paragraph between §14 and §15. This keeps the section numbering intact and makes it discoverable to maintainers scanning the §14 block. Will proceed with `## 14.1` unless directed otherwise.

2. **Checkpoint sufficiency item wording (AC-1):** TS says "Dimensions identified? (if ≥3 independent decision factors exist)". The conditional phrasing `(if ≥3 independent decision factors exist)` signals graceful degradation at the checkpoint level. I will render this as a conditional checkbox: `- [ ] Dimensions identified? _(skip if <3 independent factors — use comparison matrix instead)_` — more actionable than the raw AC phrasing.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Overflow protection wording in Extract:** AC-2 specifies "If >30 combinations, list only configs where ≥1 dimension differs from the first-listed alternative." This is a correct pruning heuristic but may confuse researchers who don't know what "first-listed alternative" means in context. Will add a brief inline example in the section instruction to anchor it.

2. **base.md Step 5 token budget:** The existing Step 5 already contains the OODA loop. Adding a dimensional analysis paragraph at the start risks pushing Stage Checkpoint content below context-comfortable depth. Will keep the thread to ≤5 lines and place it at the START of Step 5 as an introductory thread before the OODA heading — not embedded inside the OODA block — to minimize disruption.

## 6. Inconsistencies with Code (spec vs reality)

No inconsistencies found. All 5 target files exist at the paths specified in TS §4. Template sizes match TS §6 Technical Guidance (gather/extract/challenge: 25 lines each; base.md: 129 lines).

## 7. Knowledge Citations

> HL §7.2 has 4 citations. Verified below.

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | `conventions.md §14` — Anti-patterns list | ✅ | N/A (Phase C adds a terminology origin note, not anti-patterns — those were Phase A's scope) | Confirmed §14 ends at line 390. Insertion point confirmed after existing anti-patterns. |
| 2 | `conventions.md §3` — TS definition | ✅ | N/A for Phase C scope | Confirms TS is self-contained. Orthogonal to template modifications. |
| 3 | `glossary.md` — Scope Budget | ✅ | Applied: 5 modifications, 0 new files — well within budget | Budget ceiling: 14 files, 1200 LOC. This phase: ~60 LOC delta. Safe. |
| 4 | `README.md Values` — "The thinking is the product" | ✅ | Applied: Dimensions/Configuration Space/Consistency Check force thinking by decomposition before synthesis | Executor-as-engineer principle — enforced via cross-stage structural dependency |

**New PV items found:**
- HL §7 S6: "Instructions produce compliance, heuristics produce analysis" — directly informs section wording. Sections use guiding questions ("Can X coexist with Y?"), not mandates ("MUST list all combinations"). Applied in all three template sections.
- HL §7 S7: "Cross-stage dependencies are natural enforcement" — the Configuration Space section references Gather's Dimension column headers by design, making it structurally impossible to fill without prior decomposition.

---

*ONB — TFW-41 / Phase C: Research Templates — Embedded Dimensional Analysis | 2026-04-20*
