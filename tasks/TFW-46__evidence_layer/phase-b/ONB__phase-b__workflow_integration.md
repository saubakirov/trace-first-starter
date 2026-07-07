# ONB — TFW-46 / Phase B: Workflows + Integration

> **Date**: 2026-07-07
> **Author**: Executor (Antigravity, Claude Opus 4.6)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-46](../HL-TFW-46__evidence_layer.md)
> **TS**: [TS Phase B](TS__phase-b__workflow_integration.md)

---

## 1. Understanding

Phase B integrates the Evidence concept (established in Phase A's conventions + templates) into TFW's three lifecycle workflows. Specifically: (1) handoff.md gets a new Step 11 (Evidence Collection) between build gate and Pre-RF Gate, with step renumbering 11-12 → 12-13; (2) review.md Trust Protocol gets 2 new evidence-specific entries; (3) plan.md Step 7 gets a coordinator reminder to write Evidence fields in TS AC items; (4) RF.md TD-1 fix (stale `§5 Observations` → `§6 Observations`). After this phase, the Evidence lifecycle is active end-to-end across coordinator → executor → reviewer.

## 2. Entry Points

| File | Current state | What changes |
|------|--------------|-------------|
| `.tfw/workflows/handoff.md` | Steps 7-12, Phase A already updated §refs to §6-9 | New Step 11 inserted, Steps 11-12 → 12-13, §5 Evidence added to mandatory RF sections |
| `.tfw/workflows/review.md` | Trust Protocol has 7 entries, Step 3 references verify.md | 2 new Trust Protocol entries for evidence claims, Step 3 evidence reference |
| `.tfw/workflows/plan.md` | Step 7 covers TS writing with budget check | Brief evidence reminder added |
| `.tfw/templates/RF.md` | Line 68: `§5 Observations` (stale) | Fix to `§6 Observations` |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions | — |

No blocking questions. The TS is clear, all 5 ACs have precise scope, and the affected files are well-understood from Phase A context.

## 4. Recommendations (suggestions, not blocking)

1. **AC-1 Step 13 `Never omit §5.` wording**: The TS says to add `Never omit §5.` alongside existing `Never omit §7-9.` (updated from §6-8). Currently handoff.md line 98 reads `Never omit §7-9.` I'll update to `Never omit §5. Never omit §7-9.` to keep them as two separate constraints (Evidence completeness vs Knowledge sections completeness) rather than merging into a range like `§5, §7-9` which could confuse the range semantics.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **handoff.md tip blockquote reference**: Line 101 references `§7 Fact Candidates` in the tip block. After Step renumbering (11→12, 12→13), the tip stays at the same location (after the Create RF step). No content change needed but must verify it doesn't shift during step insertion.
2. **handoff.md Observations Section heading**: The inline example (lines 108-125) references `## Observations (out-of-scope, not modified)` without a §-number. This is an example block, not a cross-ref — no update needed, but worth noting.

## 6. Inconsistencies with Code (spec vs reality)

1. The TS §4 says handoff.md has "Steps 7-12". Actual file has Steps 7 (Update task board), 8 (Implement), 9 (Run tests), 10 (Build gate), 11 (Pre-RF Gate), 12 (Create RF file). Confirmed: 6 numbered steps (7-12) as TS describes. No inconsistency.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | K1: README Values — Honesty Over Convincingness | ✅ | Applied — Step 11 DEFERRED/BLOCKED guidance ensures honest evidence gaps | |
| 2 | K2: README Values — Structural Enforcement | ✅ | Applied — Evidence artifacts as structural proof in Step 11 | |
| 3 | K3: philosophy.md F4 | ✅ | Applied — Evidence folder pattern referenced in Step 11 | |
| 4 | K4: philosophy.md F21 | ✅ | Applied — DEFERRED/N/A statuses in Step 11 follow explicit N/A pattern | |
| 5 | K5: philosophy.md F27 | ✅ | N/A — Phase B is workflow text changes, not artifact file creation | |
| 6 | K6: process.md F14 | ✅ | Applied — Step 11 proportionality clause prevents fast-green | |
| 7 | K7: conventions.md §12 | ✅ | Applied — Step 11 extends "never claim tested" to require evidence artifacts | |
| 8 | K8: conventions.md §14 | ✅ | Applied — Step 11 mirrors anti-pattern: "executor writes RF before evidence collected" | |
| 9 | K9: D41 (TFW-41) | ✅ | Applied — Evidence Plan extends AC gates, Step 11 implements the executor side | |
| 10 | K10: D46 (TFW-38) | ✅ | Applied — Trust Protocol entries (AC-2) extend D46's Trust Protocol for evidence claims | |
| 11 | K11: philosophy.md F13 | ✅ | Applied — Step 11 stays domain-agnostic, no tool names | |

No new PV items found beyond coordinator's K1-K11.

---

*ONB — TFW-46 / Phase B: Workflows + Integration | 2026-07-07*
