# ONB — TFW-38 / Phase A: Review Restructure + Full Enforcement Chain

> **Date**: 2026-04-14
> **Author**: Executor
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> **TS**: [TS Phase A](TS__PhaseA__review_restructure.md)

---

## 1. Understanding

Restructure the TFW review workflow from a single-pass read-and-checklist model into a 4-stage cognitive flow (Map → Verify → Judge → Decide) with 3 output-type review modes (code/docs/spec). Simultaneously close the enforcement chain: make handoff.md explicitly enumerate RF §6-8, make research/base.md explicitly require Findings Map, make plan.md cite KNOWLEDGE.md items, and add corresponding anti-patterns to conventions.md. 10 files touched (3 new, 7 modified).

## 2. Entry Points

| File | Role |
|------|------|
| `.tfw/workflows/review.md` (119 lines) | Main restructure target — Steps 1-5 → 4-stage flow + Step 0 mode selection |
| `.tfw/templates/REVIEW.md` (80 lines) | Template restructure — §1-§5 → §1-§7 matching stages |
| `.tfw/workflows/review/` | New directory — 3 mode files (code.md, docs.md, spec.md) |
| `.tfw/workflows/handoff.md` (142 lines) | Phase 1 line 36 + Phase 3 line 73 modifications |
| `.tfw/workflows/research/base.md` (128 lines) | Step 6 line 90-93 — add Findings Map |
| `.tfw/workflows/plan.md` (140 lines) | Step 3 line 31-37 — add knowledge citation |
| `.tfw/conventions.md` (383 lines) | §14 lines ~327-343 — 4 new anti-patterns |
| `.tfw/PROJECT_CONFIG.yaml` (110 lines) | Add `tfw.review` section |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. TS is well-specified with exact content for each step. | — |

## 4. Recommendations (suggestions, not blocking)

1. **review.md word count monitoring.** TS Step 1 specifies substantial content for Steps 0-4. Current review.md is 119 lines (~850 words). The restructure adds Step 0 (mode selection) and Step 2 (Verify). I'll keep stage descriptions tight (matching TS examples) and rely on mode files for differential content to stay under 1200 words. Will report final word count in RF.

2. **REVIEW template §3 Judge — mode-specific row placeholder.** TS Step 2 shows `{mode-specific items from mode file}` as a table row. I recommend keeping this as a clear instruction comment (`<!-- Add mode-specific items from mode file below -->`) rather than a pseudo-table-row, since it's not a real data row. This makes the template cleaner for agent consumption.

3. **Step numbering in review.md.** Current Steps 1-7 will become Steps 0-7 (adding Step 0: Mode Selection, then Steps 1-4 as the 4 stages, Steps 5-7 as post-verdict). The TS references old Steps 5-7 as "keep largely unchanged." I'll renumber them to fit the new sequence: old Step 3 (Tech Debt) → new Step 5, old Step 6 (Update Traces) → new Step 6, old Step 7 (Knowledge Capture) → new Step 7.

4. **handoff.md Phase 3 step number.** Current Phase 3 starts at step 12 (line 73). TS says "replace the current bullet list" at this step. I'll preserve the step number 12 for continuity.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **conventions.md §14 line range.** TS Step 6 says "§14" but conventions.md has no explicit "§14" heading — the anti-patterns section is `## 14) Anti-patterns (prohibited)` at line 327. The new items need to be inserted before the Role Lock Protocol section (§15) starting at line 345. Risk is low — clear section boundary exists.

2. **plan.md Step 3 sub-step numbering.** Current Step 3 has items numbered 1-4 (Identify context, Understand problem, Study references, Ask questions). TS says "add sub-step after 'Study references'" and numbers it "4." This would collide with the existing item 4 ("Ask clarifying questions"). I'll insert the knowledge citation as new item 4 and renumber "Ask clarifying questions" to 5.

3. **research/base.md Step 6 renumbering.** TS says to add Findings Map as item 5 after line 91, then renumber old 5→6 and old 6→7. Current items 5 and 6 are "Iteration Status block" and "Conclusion." This is straightforward but needs careful renumbering.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS Step 1 references "current Steps 1-5" in review.md.** Actual current steps are: Step 1 (Read and Understand), Step 2 (Review Checklist), Step 3 (Tech Debt Collection), Step 4 (Write REVIEW File), Step 5 (Verdict), Step 6 (Update Traces), Step 7 (Knowledge Capture). TS correctly maps Steps 1-5 → Steps 0-4 but references "old Step 5" for verdict — actually the old verdict is Step 5. No actual inconsistency, just noting for clarity.

2. **TS Step 4 says "line 73" for Phase 3 and "line 36" for Phase 1.** Verified: line 73 = `12. **Create RF file**` ✅; line 36 = `   - Inconsistencies between HL/TS and actual code` ✅. Both match.

3. **REVIEW template current §5 (Fact Candidates) content.** TS Step 2 says new §7 "Same as current §5." Verified: current §5 has the full Fact Candidates section with cognitive mode instructions, Human-Only Test, categories, and source format references. Will preserve all of this in new §7.

> **Cross-references**: HL-TFW-38 §4 Phase A, D1, D8, D9, D11, D12, D14-D17.

---

*ONB — TFW-38 / Phase A: Review Restructure + Full Enforcement Chain | 2026-04-14*
