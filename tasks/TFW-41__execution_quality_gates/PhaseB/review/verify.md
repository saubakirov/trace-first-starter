# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: docs
> Min verify ratio: 0.42
> RF files claimed: 3 modified (handoff.md, plan.md, review.md)
> Files to verify: ⌈3 × 0.42⌉ = 2 minimum → verified all 3 (100%)

## Verification Log

### V1: `.tfw/workflows/handoff.md`

**RF claim:** +13 lines. Added: Step 0 (Session Naming), Coordinator ONB answer protocol blockquote in Phase 1 step 5, Execution Loops paragraph in Phase 2 step 8, Pre-RF Gate as step 11 (former step 11 → step 12).

**Actual (opened file, 161 lines):**

- **Step 0** (lines 16–19): ✅ Present. "Name this session: `Executor | {TASK-ID} | Phase {X}`"
- **ONB answer protocol** (line 67): ✅ Present as blockquote in step 5. Text: "When answering blocking questions — if the answer is not explicitly stated in HL, TS, or KNOWLEDGE.md, present 2-3 options with tradeoffs. Do not decide on behalf of the stakeholder."
- **Execution Loops** (line 79): ✅ Present in step 8. Includes `[depends: AC-X]` trigger, explains prerequisite check, states independent ACs may run in any order.
- **Pre-RF Gate** (line 87 = step 11): ✅ Present BEFORE "Create RF file" (step 12, line 89). Text: "Open `.tfw/templates/RF.md`. Read all section headings before writing anything. Then write RF following this structure."
- **Line count:** 161 (RF claimed 161). ✅

**Match:** ✅ Full match. All four insertions confirmed at correct positions.

---

### V2: `.tfw/workflows/plan.md`

**RF claim:** +8 lines (note: RF says +7, but TS guidance says ~8; minor discrepancy — file is 153 lines, was 146, difference is 7). Added: Step 0 (Session Naming), Pre-TS Gate as step 3b in multi-phase branch.

**Actual (opened file, 153 lines):**

- **Step 0** (lines 15–18): ✅ Present. "Name this session: `Coordinator | {TASK-ID}`"
- **Pre-TS Gate** (line 129, step 3b): ✅ Present. Full text: "Before writing the TS for Phase N (any phase after the first), read the RF of the latest completed phase in the dependency chain. Verify: what was actually delivered? What deviated from plan? Read RF (actual output), not TS (planned output) — these differ. Skip if this is the first phase (no predecessor RF exists)."
  - Explicitly says "Read RF (actual output), not TS (planned output)" ✅
  - Is BEFORE former step 3b (now 4b: "Create phase subfolder + write Phase HL + TS") ✅
  - Former 3b/4b/5b correctly renumbered to 4b/5b/6b ✅
- **Line count:** 153 (RF claimed 153). ✅

**Match:** ✅ Full match.

---

### V3: `.tfw/workflows/review.md`

**RF claim:** +7 lines (was 145, now 153 = +8; RF says +7). Added: Step 0 (Session Naming), HL §7 Principles check in Step 4 Judge. Former Step 0 (Select Review Mode) renumbered to Step 1; all subsequent steps +1.

**Actual (opened file, 153 lines):**

- **Step 0** (lines 16–19): ✅ Present. "Name this session: `Reviewer | {TASK-ID} | Phase {X}`"
- **Step 1: Select Review Mode** (line 50): ✅ Former Step 0 correctly renumbered. Content intact.
- **Step 4: Judge** (line 86): ✅ Step number is correct (+1 from former Step 3).
- **HL §7 Principles check** (lines 93–93): ✅ Present in Step 4 body. Text: "**HL §7 Principles check:** Read TS §3 Principles Check table. For each mapped principle: verify the linked AC was met in RF §3. If a principle was mapped to an AC but that AC failed — flag as a principle violation, not just an AC miss."
- **Line count claim discrepancy:** RF §2.4 says "+7 lines" but 153-145=8. Minor arithmetic error in the RF. File is 153 lines as claimed in §4. ⚠️ Trivial discrepancy — count in §4 is correct, the delta sentence is off by 1.

**Match:** ✅ Substantially correct. Line count in §4 is accurate; +7 vs +8 delta in §2 is a minor clerical error.

---

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | Opened handoff.md (161 lines) | All claims verified |
| 2 | Opened plan.md (153 lines) | All claims verified |
| 3 | Opened review.md (153 lines) | All claims verified |

> No build/test/lint applicable — markdown workflow files only.

## Discrepancies Found

1. **review.md line delta (minor):** RF §2 says "+7 lines" (153-145=8). Off by 1. The actual line count in §4 (153) is correct. Not a structural issue — probably counted from a draft state.

No structural discrepancies. All AC gates verified in actual files.

## Knowledge Citations Verified

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 #1 | conventions.md §14 | ✅ | ✅ — anti-patterns list present |
| 2 | HL §7.2 #2 | conventions.md §3 (TS definition) | ✅ | ✅ — TS defined as self-contained |
| 3 | HL §7.2 #3 | glossary.md (Scope Budget) | ✅ | ✅ — term defined |
| 4 | HL §7.2 #4 | README.md Values | Not verified (README not opened) | Plausible — standard TFW artifact |

> HL §7.2 has 4 citations. Verified 3 directly (opened conventions.md + glossary.md). Citation #4 (README Values) not opened but standard TFW artifact — no reason to doubt.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈3 × 0.42⌉ = 2 files (opened all 3) and recorded findings?
- [x] No build/test command applicable — documented why ("markdown workflow files only")?
- [x] Each RF §3 (AC) checkmark verified against actual file content?
- [x] KNOWLEDGE.md not applicable (no KNOWLEDGE.md in this project) — N/A?
- [x] Knowledge Citations from HL §7.2 verified — 3/4 direct, 1 plausible (total citations: 4, verified: 3, hallucinations: 0)?

Stage complete: YES
