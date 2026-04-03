# ONB — TFW-18 / Phase B: Knowledge Quality

> **Дата**: 2026-04-03
> **Автор**: Executor (AI)
> **Статус**: 🟠 ONB — Ожидает ответов
> **Parent HL**: [HL Phase B](HL__PhaseB__knowledge_quality.md)
> **TS**: [TS Phase B](TS__PhaseB__knowledge_quality.md)

---

## 1. Understanding (как понял задачу)

Reframe Fact Candidates guidance in 3 templates (RF, REVIEW, RES) and 2 workflows (research, handoff) from "technical gotchas" framing to "strategic knowledge" framing. Expand category examples in conventions.md to include business-oriented examples. Sharpen gather guidance in knowledge.md. Add Knowledge consolidation to `.tfw/README.md` §v3 and workflows table. Sync 3 adapter files. Total: 8 file modifications, 0 new files, ~120 words added.

## 2. Entry Points (откуда начинать)

| File | Current state | TS Step |
|------|--------------|---------|
| `.tfw/templates/RF.md` L51-56 | «project knowledge — decisions, corrections, context, domain facts. Extract what would change the next agent's behavior» | Step 1 |
| `.tfw/templates/REVIEW.md` L53-58 | Same old framing | Step 2 |
| `.tfw/templates/RES.md` L116-121 | Old framing + «THIS project» filter | Step 3 |
| `.tfw/workflows/research.md` L110 | «project knowledge — decisions, corrections, context, domain facts. Extract what would change the next agent's behavior» | Step 4 |
| `.tfw/workflows/handoff.md` L81-87 | «environment, constraints, stakeholders, conventions» + old framing | Step 5 |
| `.tfw/conventions.md` L206-215 | Generic category examples | Step 6 |
| `.tfw/workflows/knowledge.md` L32-34 | «decisions, corrections, context, domain facts» | Step 7 |
| `.tfw/README.md` L283, L161-170 | No knowledge/config in v3 list or workflow table | Step 8 |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. TS provides exact replacement text for all 8 files. | — |

## 4. Recommendations (suggestions, not blocking)

1. **Step 9 adapter sync scope**: TS says copy to `.agent/workflows/` for research, handoff, knowledge. The `.agent/workflows/tfw-handoff.md` file is already a copy of `.tfw/workflows/handoff.md` (verified in Phase A RF). I'll use `cp` to overwrite after modifications, matching Phase A convention.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Line number drift**: TS specifies exact line numbers (e.g., L51-56, L110, L32-34) from the time TS was written. I verified all line numbers match current file state — no drift detected.
2. **README.md workflows table structure**: TS Step 8b says "Add to workflows table (L161-170)" — the table runs L161-170 with the last entry being `update`. Adding 2 rows will push content down. No risk, just noting.

## 6. Inconsistencies with Code (spec vs reality)

1. No inconsistencies found. All files match TS expectations.

---

*ONB — TFW-18 / Phase B: Knowledge Quality | 2026-04-03*
