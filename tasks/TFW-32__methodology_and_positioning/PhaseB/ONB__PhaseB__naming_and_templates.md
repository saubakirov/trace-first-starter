# ONB — TFW-32 / Phase B: Naming & Templates

> **Date**: 2026-04-10
> **Author**: AI (Executor)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> **TS**: [TS Phase B](TS__PhaseB__naming_and_templates.md)

---

## 1. Understanding

Phase B sharpens knowledge capture instructions and adds visual sections to TFW templates. The core principle: section names are micro-prompts that trigger specific LLM cognitive modes. §6 "Fact Candidates" and §7/§11 "Strategic Insights" keep their empirically optimal names but get tighter scope and mode instructions. Three new visual sections use per-template names because cognitive modes differ by context: HL = "Value Flow" (strategic), RF = "Diagrams" (technical), RES = "Findings Map" (analytical). HL §3.1 gets Working Backwards framing. All changes are documented in conventions.md and glossary.md in the same phase.

## 2. Entry Points

| File | Role |
|------|------|
| `.tfw/templates/HL.md` | §3.1 enhance, §3.2 add, §11 rename+tighten |
| `.tfw/templates/RF.md` | §6 sharpen, §7 add, §8 Diagrams add |
| `.tfw/templates/RES.md` | Fact Candidates sharpen, Strategic Insights (Research) add, Findings Map add |
| `.tfw/templates/REVIEW.md` | §5 sharpen |
| `.tfw/conventions.md` | Visual Sections table, Knowledge Capture table, §3 FC update |
| `.tfw/glossary.md` | Strategic Insight update, Value Flow, Findings Map, Per-template Naming |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. | — |

All 8 steps are fully specified with exact before/after content. File line references verified against current file state.

## 4. Recommendations (suggestions, not blocking)

1. **TS Step 4b §7 section number**: TS says "Add §7" to RF, but current RF ends at §6 (line 69). The new section fits naturally as §7. However, TS Step 4c says "Add §8 Diagrams" — this means RF will jump from §6 to §8 with §7 in between. This is logical and consistent.

2. **RES template §-numbering**: TS Steps 5b/5c don't assign section numbers to Strategic Insights (Research) or Findings Map in RES — they use heading-only naming. This is intentional: RES is a synthesis document, not a phase-numbered artifact like RF. I'll follow the TS exactly.

3. **TS line references vs actual**: Verified TS line references against current file state:
   - HL.md §11 TS says "lines 106-122" → actual lines 106-121. Minor off-by-one. Content matches exactly. No impact.
   - RF.md §6 TS says "lines 52-61" → actual lines 52-61. ✅ Match.
   - RES.md TS says "lines 38-46" → actual lines 38-46. ✅ Match.
   - REVIEW.md TS says "lines 56-65" → actual lines 56-65. ✅ Match.
   - conventions.md TS says "after line 76" → actual line 75-76 contains the FC definition. ✅ Match.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Section ordering in RF**: Adding §7 and §8 after §6 places them before the footer `---`. The current footer is at line 71. The TS explicitly says "Insert before the footer `---`" — clear and correct.

2. **RES template Conclusion section**: TS says insert Strategic Insights and Findings Map "before Conclusion" (Step 5b: "after line 51, before Conclusion"). Current RES has Conclusion at line 53. Inserting two new sections before it will push Conclusion down. This maintains the template's logical flow: data sections → synthesis sections → Conclusion.

## 6. Inconsistencies with Code (spec vs reality)

1. **HL.md line count for §11**: TS Step 3 says "Before (lines 106-122)" — the actual §11 content spans lines 106-127 (including the cross-references block and footer). The TS "Before" block only shows lines 106-121. The cross-references block (line 123) and footer (lines 125-127) should NOT be touched. This is consistent — the TS replaces only the §11 content, leaving cross-references and footer intact.

> **Cross-references**: TS__PhaseB, HL-TFW-32 §4 Phase B, RES3 D15/D16, RES4 D21/D22/D24/D25/D26.

---

*ONB — TFW-32 / Phase B: Naming & Templates | 2026-04-10*
