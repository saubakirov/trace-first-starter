# ONB — TFW-41 / Phase D: Glossary and Adapter Sync

> **Date**: 2026-04-20
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> **TS**: [TS__PhaseD__glossary_and_adapters](TS__PhaseD__glossary_and_adapters.md)

---

## 1. Understanding

Phase D is the closing phase of TFW-41. The task has two independent deliverables: (1) add 14 new terms to `glossary.md` covering the concepts introduced in Phases A (TS structure gates), B (workflow gates), and C (dimensional analysis), and (2) sync 4 Antigravity adapter files in `.agent/workflows/` to match their updated source workflows in `.tfw/workflows/`. Both deliverables are pure text modifications — no code, no compilation. AC-2 depends on AC-1 (adapters reference glossary terms, so glossary must be written first per the `[depends]` annotation).

## 2. Entry Points

| File | Role | Current state |
|------|------|---------------|
| `.tfw/glossary.md` | Target — add 14 terms | 197 lines, ends at Project-Specific Terms section |
| `.agent/workflows/tfw-handoff.md` | Adapter to sync | 148 lines — pre-Phase B (missing Step 0, Execution Loops, Pre-RF Gate, ONB answer protocol) |
| `.agent/workflows/tfw-plan.md` | Adapter to sync | 146 lines — pre-Phase B (missing Step 0, Pre-TS Gate) |
| `.agent/workflows/tfw-review.md` | Adapter to sync | 145 lines — pre-Phase B (old step numbering: Step 0 = Select Mode vs Step 1 in source; missing HL §7 Principles check in Judge) |
| `.agent/workflows/tfw-research.md` | Adapter to sync | 129 lines — pre-Phase C (missing dimensional analysis thread in Step 5) |
| `.tfw/workflows/handoff.md` | Source truth | 161 lines — Phase B version |
| `.tfw/workflows/plan.md` | Source truth | 153 lines — Phase B version |
| `.tfw/workflows/review.md` | Source truth | 153 lines — Phase B version |
| `.tfw/workflows/research/base.md` | Source truth | 131 lines — Phase C version |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | TS §6 says adapters are "exact copies" of source workflows. The only observed difference between source and adapter is the frontmatter (`---` YAML block with `description:` field). Both source and adapters have identical frontmatter. Should the sync preserve the existing frontmatter unchanged (i.e., copy content verbatim including frontmatter), or strip/replace it? | _{coordinator fills in}_ |

## 4. Recommendations (suggestions, not blocking)

1. **Glossary section placement:** TS §6 suggests two new sections: `## Execution Gates` and `## Research — Dimensional Analysis`. This is clean and scannable. I will follow this recommendation unless directed otherwise.
2. **Adapter sync method:** The cleanest approach for AC-2 is to overwrite each adapter file with the exact source content (preserving frontmatter). This guarantees zero diff rather than a manual merge that could miss something.
3. **Glossary definition for "Alternative":** The TS AC-1 list includes `Dimension`, `Configuration Space`, `Consistency Check`, and `Surviving Configuration` — but does NOT list `Alternative` as one of the 14 required terms. The HL §4 Phase D Deliverables list does include "Alternative". I will add it as an unprompted bonus only if there are no concerns — alternatively, I flag it here as a recommendation. **If the reviewer counts 14 strictly**, omit Alternative; if 15 is acceptable, include it for completeness.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **"Alternative" term gap:** HL §4 Phase D Deliverables lists "Alternative" (14th item in the deliverables list), but TS AC-1 lists only 14 terms and does NOT include "Alternative" in the explicit checklist. The TS checklist is the contract. I will follow the TS checklist (14 terms, no "Alternative") and note this discrepancy here. The reviewer may flag it as a gap.
2. **Adapter line count drift:** TS §6 references Phase B RF line counts (handoff: 161, plan: 153, review: 153) and Phase C RF (research/base: 132 lines). The source files I read today are 161, 153, 153, 131 lines respectively — close but research/base.md is 131, not 132. This is within normal (a trailing newline difference). The sync will copy the actual current state, which is authoritative.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS §6 "exact copy" claim vs adapter state:** The current adapter files are definitively NOT exact copies of their sources — they are pre-Phase B/C versions. This is expected (Phase D exists to fix this), but confirms the magnitude: all 4 adapters need full replacement.
2. **`tfw-review.md` step numbering:** The adapter has "Step 0: Select Review Mode" while the source has "Step 1: Select Review Mode" (with a new "Step 0: Name This Session" prepended in Phase B). The sync will correct this automatically via full replacement.
3. **AC-1 count vs HL deliverables:** HL §4 lists "Alternative" in the glossary deliverables list, but TS AC-1 does not include it in the 14-term checklist. TS is the contract. Treated as out-of-scope.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | conventions.md §14 — Anti-patterns list | ✅ | Applied — confirmed no executor role-lock violations in this phase (glossary + adapter copy = permitted executor work) | |
| 2 | conventions.md §3 — TS definition | ✅ | Applied — reinforces that TS is the contract; TS AC-1 (14 terms) overrides HL deliverables list discrepancy on "Alternative" | |
| 3 | glossary.md — Scope Budget | ✅ | N/A — Phase D is 0 new files, 5 modifications, well within budget | |
| 4 | README.md Values — "The thinking is the product" | ✅ | Applied — glossary definitions describe the thinking concepts (WHAT), not implementation (HOW), per P2 principle | |

**Additional PV items found:**

| # | Source | Item | Relevance |
|---|--------|------|-----------|
| 5 | conventions.md §14.1 | Terminology origin note — GMA/Zwicky terms MUST NOT appear in researcher-facing files | Critical constraint for glossary definitions of dimensional analysis terms: definitions must use TFW native terms only |

---

*ONB — TFW-41 / Phase D: Glossary and Adapter Sync | 2026-04-20*
