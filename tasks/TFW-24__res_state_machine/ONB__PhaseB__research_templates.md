# ONB — TFW-24 / Phase B: Research Stage Templates

> **Date**: 2026-04-04
> **Author**: Executor
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-24](HL-TFW-24__res_state_machine.md)
> **TS**: [TS Phase B](TS__PhaseB__research_templates.md)

---

## 1. Understanding

Create 4 canonical templates for research stage files (`briefing.md`, `gather.md`, `extract.md`, `challenge.md`) in `.tfw/templates/research/`. Update `base.md` Steps 3/4/5 to reference templates. Update `conventions.md` §4 to replace inline format with template reference. Sync adapter.

## 2. Entry Points

| File | Key Lines/Sections |
|------|--------------------|
| `.tfw/workflows/research/base.md` | L30-32 (Step 3), L34-36 (Step 4), L43-45 (Step 5) |
| `.tfw/conventions.md` | L98-116 (Research subfolder — inline format to replace) |
| `.agent/workflows/tfw-research.md` | Full copy of base.md |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions | — |

## 4. Recommendations (suggestions, not blocking)

1. **conventions.md currently has a richer inline format (L102-116) than Phase A left.** It includes `Stage file format` with a code block and `Briefing file format` line. The TS §Step 6 says to replace inline format with templates reference. This is clean — the templates will be the canonical source.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **base.md word count.** Current: 600 words (exactly at limit). TS estimates "same word count (~12 words → ~12 words)" for each change. Need to verify after edits.

## 6. Inconsistencies with Code (spec vs reality)

1. **conventions.md §4 (L102-116) has more inline content than the TS expected.** TS Step 6 says "Replace inline stage file format block" — the actual block is 18 lines (L102-116), not just the one-line convention from Phase A. This is fine — replacing all of it with the template reference is cleaner.

---

*ONB — TFW-24 / Phase B: Research Stage Templates | 2026-04-04*
