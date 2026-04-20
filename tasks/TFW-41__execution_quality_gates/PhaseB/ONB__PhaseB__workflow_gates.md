# ONB — TFW-41 / Phase B: Workflow Gates

> **Date**: 2026-04-20
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> **TS**: [TS__PhaseB__workflow_gates](TS__PhaseB__workflow_gates.md)

---

## 1. Understanding

Phase B adds 6 structural gates to 3 TFW workflow files: `handoff.md` (Pre-RF Gate + Execution Loops + ONB answer protocol + Session Naming), `plan.md` (Pre-TS Gate + Session Naming), and `review.md` (HL §7 principles check in Judge + Session Naming). No new files. All changes are insertions into existing workflow prose — no restructuring of phases. Phase A (templates + conventions) is complete and approved.

## 2. Entry Points

| File | Current lines | Insertion points |
|------|--------------|-----------------|
| `.tfw/workflows/handoff.md` | 148 | Before Context Loading (Step 0), Phase 1 step 5 (ONB answer protocol), Phase 2 step 8 (Execution Loops), before Phase 3 step 11 (Pre-RF Gate) |
| `.tfw/workflows/plan.md` | 146 | Before Step 1 (Step 0 naming), Step 7 §3b multi-phase branch (Pre-TS Gate) |
| `.tfw/workflows/review.md` | 145 | Before Context Loading (Step 0), Step 3 Judge (HL §7 principles check) |
| `.tfw/templates/RF.md` | 106 | Read-only reference — Pre-RF Gate instructs executor to open this file |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. All ACs are unambiguous and complete. | — |

## 4. Recommendations (suggestions, not blocking)

1. **AC-2 placement in plan.md**: The TS §6 Technical Guidance says "Pre-TS Gate goes into Step 7, specifically the multi-phase branch (Step 3b, line 124)." However, reading plan.md, the Pre-TS Gate applies equally to single-phase tasks that follow a previous phase (e.g., a task with multiple iterations of research where the coordinator re-enters Step 7 after review). Consider whether the gate should be universal to Step 7 or limited to `3b`. I will implement it at `3b` (multi-phase) as specified — this is the correct interpretation per AC-2's explicit scope: "where N > first phase." Single-phase tasks don't have a previous phase RF to read. No change to spec needed.

2. **AC-4 placement**: The TS guidance says "between steps 5-6 as a blockquote instruction in step 5 or as a new sub-step." Step 5 in handoff.md says "Wait for user approval." The coordinator answer protocol is a coordinator-side action that happens during this wait. A blockquote inside step 5 is natural and keeps the executor workflow uninterrupted — I will use this approach.

3. **AC-6 Session Naming wording**: `review.md` doesn't always apply to a "Phase" (single-phase tasks also get reviewed). The TS AC-6 says `Reviewer | {TASK-ID} | Phase {X}`. Consider `Phase {X}` optional for single-phase tasks. I will implement per spec — the `{X}` placeholder is obvious and flexible; a reviewer can use "Phase A" or omit if single-phase. No deviation needed.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Word budget**: The informal ~1200-word budget per workflow (conventions.md §11). Current sizes: `handoff.md` ~780 words, `plan.md` ~1020 words, `review.md` ~870 words. Phase B adds ~50-80 words per workflow per TS estimate. `plan.md` is closest to budget at ~1020 words — 80-word addition brings it to ~1100, within budget. Low risk.

2. **AC-3 Execution Loops — minimal footprint**: The `[depends]` mechanism was added to the TS template in Phase A. However, `handoff.md` currently contains no reference to `[depends]`. The Execution Loops instruction must be self-contained enough for executors who haven't memorized the new TS template. I will include a brief definition of what `[depends: AC-X]` means in the instruction itself.

3. **Step numbering in handoff.md**: Adding Step 0 shifts no existing step numbers (it's prepended). But the Pre-RF Gate is a new step between step 10 (Build gate) and step 11 (Create RF file). This makes the former step 11 become step 12. Since handoff.md references steps by name, not only by number (e.g., "current step 11" in TS §5 AC-1), this is safe — but I will verify no other section cross-references step numbers.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS §6 line count for review.md**: "review.md (145 lines)" — verified ✅ (145 lines confirmed).
2. **TS §6 line count for handoff.md**: "handoff.md (148 lines)" — verified ✅.
3. **TS §6 line count for plan.md**: "plan.md (146 lines)" — verified ✅.
4. **No `§4 Detailed Steps` or `§5 Acceptance Criteria` references found in any workflow** — confirmed per Phase A RF §5 Observation 2 and my own scan. Phase B additions are clean.
5. **AC-1 gate wording**: TS says step must be "BEFORE 'Create RF file' (current step 11)." After adding Step 0, the former step 11 becomes step 12. The AC gate says "before RF creation step" — not "before step 11" — so it's satisfied regardless of renumbering. ✅

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | conventions.md §14 — Anti-patterns list | ✅ | Applied — Phase A added 4 new anti-patterns including "executor writes RF without opening template" (AC-1 origin) and "coordinator answers ONB questions without source" (AC-4 origin). Phase B gates enforce these at the workflow level. | |
| 2 | conventions.md §3 — TS definition | ✅ | N/A to Phase B — Phase A already addressed TS structure. Phase B modifies workflows, not TS template. | |
| 3 | glossary.md — Scope Budget | ✅ | Applied — word budget risk assessed in §5 Risks. All 3 workflows remain within budget. | |
| 4 | README.md Values — "The thinking is the product" | ✅ | Applied — Execution Loops (AC-3) and Pre-TS Gate (AC-2) both enforce thinking: executor verifies gates, coordinator reads actual output. | |

> **NEW PV item found**: RF Phase A §2 Decision 5 (Phase B coordinator note) — "scan for '§4 Detailed Steps', '§4', '§5 Acceptance Criteria' references in workflows." Executed: none found. This note is now resolved.

---

*ONB — TFW-41 / Phase B: Workflow Gates | 2026-04-20*
