# RF — TFW-41 / Phase B: Workflow Gates

> **Date**: 2026-04-20
> **Author**: Executor (AI)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> **TS**: [TS__PhaseB__workflow_gates](TS__PhaseB__workflow_gates.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `tasks/TFW-41__execution_quality_gates/PhaseB/ONB__PhaseB__workflow_gates.md` | Onboarding report (no blocking questions) |
| `tasks/TFW-41__execution_quality_gates/PhaseB/RF__PhaseB__workflow_gates.md` | This file |

### Modified Files
| File | Changes |
|------|---------|
| `.tfw/workflows/handoff.md` | +13 lines. Added: Step 0 (Session Naming), Coordinator ONB answer protocol blockquote in Phase 1 step 5, Execution Loops paragraph in Phase 2 step 8, Pre-RF Gate as step 11 (former step 11 → step 12). |
| `.tfw/workflows/plan.md` | +8 lines. Added: Step 0 (Session Naming), Pre-TS Gate as step 3b in multi-phase branch (former 3b/4b/5b renumbered to 4b/5b/6b). |
| `.tfw/workflows/review.md` | +7 lines. Added: Step 0 (Session Naming), HL §7 Principles check in Step 4 Judge. Former Step 0 (Select Review Mode) renumbered to Step 1; all subsequent steps +1 (now Steps 1–8). |

## 2. Key Decisions

1. **review.md step renumbering.** `review.md` already had a "Step 0: Select Review Mode" before the new Session Naming step was added. Both cannot be Step 0. Renumbered all original steps +1 (Select Review Mode → Step 1, Map → Step 2, etc., through Knowledge Capture → Step 8). This preserves logical order without ambiguity. The TS did not anticipate this collision — resolved using the "make it work structurally, document the deviation" principle.

2. **plan.md step renumbering in 3b branch.** Inserting Pre-TS Gate as new step 3b shifted the former 3b and 4b/5b to 4b and 5b/6b. Renumbered cleanly to avoid the duplicate-label issue encountered in the initial insertion.

3. **Pre-RF Gate uses "open and read headings" language, not "copy template."** The TS AC-1 wording is "Open `.tfw/templates/RF.md`. Read all section headings." This is stronger than "use as canonical format" (which already existed in step 12). The gate enforces the act of reading — not merely referencing the template name from memory.

4. **Execution Loops includes inline definition of `[depends: AC-X]`.** The mechanism was added to the TS template in Phase A, but an executor reading handoff.md without knowing Phase A's changes might not recognize the annotation. The Execution Loops instruction is self-contained: it defines the annotation in parentheses and gives a concrete example. This prevents "compliance by confusion."

5. **Coordinator ONB answer protocol as blockquote inside step 5, not a separate step.** The coordinator's answering behavior is not an executor step — it's a protocol for what happens during the "Wait for user approval" pause. A blockquote attribution makes it visually distinct and role-attributed without disrupting the executor step numbering.

6. **HL §7 Principles check placed inside Step 4 Judge body, not as a sub-step.** The TS specified "checklist item" in Judge. The check is implemented as a paragraph after "Must reference verify.md findings" — same phase, same mindset, no new sub-structure needed. Simpler and more maintainable.

## 3. Acceptance Criteria

### AC-1: Pre-RF Gate in handoff.md
- [x] `handoff.md` Phase 3 has explicit step: "Open `.tfw/templates/RF.md`. Read all section headings before writing anything. Then write RF following this structure."
- [x] Step is BEFORE "Create RF file" (step 11 before step 12)

### AC-2: Pre-TS Gate in plan.md
- [x] `plan.md` Step 7 multi-phase branch (3b) has: "Before writing the TS for Phase N (any phase after the first), read the RF of the latest completed phase in the dependency chain."
- [x] Sub-step is BEFORE "Write Phase HL + TS using templates/TS.md" (new 3b before 4b)
- [x] Explicitly says: "Read RF (actual output), not TS (planned output)"

### AC-3: Execution Loops in handoff.md [depends: AC-1]
- [x] `handoff.md` Phase 2 step 8 has Execution Loops instruction with `[depends: AC-X]` annotation trigger
- [x] Instruction explains: "if AC-2 has `[depends: AC-1]`, verify AC-1 is complete before implementing AC-2"
- [x] Instruction says: "Independent ACs (no `[depends]`) may be implemented in any order"

### AC-4: Coordinator ONB answer protocol in handoff.md
- [x] `handoff.md` Phase 1 step 5 has blockquote: "When answering blocking questions — if the answer is not explicitly stated in HL, TS, or KNOWLEDGE.md, present 2-3 options with tradeoffs. Do not decide on behalf of the stakeholder."

### AC-5: HL §7 principles check in review.md Judge phase
- [x] `review.md` Step 4 (Judge) has: "**HL §7 Principles check:** Read TS §3 Principles Check table. For each mapped principle: verify the linked AC was met in RF §3."
- [x] States: "If a principle was mapped to an AC but that AC failed — flag as a principle violation, not just an AC miss"

### AC-6: Session Naming Step 0 in all workflows
- [x] `handoff.md` Step 0: "Name this session: `Executor | {TASK-ID} | Phase {X}`"
- [x] `plan.md` Step 0: "Name this session: `Coordinator | {TASK-ID}`"
- [x] `review.md` Step 0: "Name this session: `Reviewer | {TASK-ID} | Phase {X}`"

## 4. Verification

TS §6 Technical Guidance specifies line targets and prose verification. No build/lint/test applicable to markdown workflow files.

- `handoff.md`: **161 lines** (was 148, +13 ✅)
- `plan.md`: **153 lines** (was 146, +7 ✅)
- `review.md`: **153 lines** (was 145, +8 ✅)

Word budget check (informal ~1200 words):
- `handoff.md`: ~870 words (was ~780, +~90 words — within budget ✅)
- `plan.md`: ~1080 words (was ~1020, +~60 words — within budget ✅)
- `review.md`: ~930 words (was ~870, +~60 words — within budget ✅)

Gate verification (DoF):
- `handoff.md` Pre-RF Gate: mandatory step, not a suggestion ✅
- `plan.md` Pre-TS Gate: "read RF (actual output), not TS (planned output)" ✅
- Execution Loops: triggered by `[depends]` annotation, not AC count ✅
- Session Naming: present in all 3 workflows ✅

No `§4 Detailed Steps` or `§5 Acceptance Criteria` references found in any workflow (confirmed by scan — consistent with Phase A RF §5 Observation 2).

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/workflows/review.md` | 50 (pre-edit) | naming | `review.md` originally had "Step 0: Select Review Mode" — the only workflow with a pre-existing Step 0. This made Session Naming insertion non-trivial. Future workflows should avoid Step 0 labels unless they are a universal first-step like Session Naming. |
| 2 | `.tfw/workflows/plan.md` | 141–143 | naming | plan.md multi-phase branch used `3b/4b/5b` labeling. Inserting a new 3b caused a duplicate-label issue. The labeling scheme creates fragility: any future insertion in the branch requires renumbering. Consider prose-based labeling (no alphanumeric step IDs) for multi-step branches in future edits. |

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | `review.md` had a pre-existing "Step 0: Select Review Mode" — the only workflow with a non-zero-indexed Step 0. This historical naming created an insertion conflict for Session Naming. Any future executor modifying `review.md` should check for step-number collisions before adding Step 0 content. | Execution observation | High |
| 2 | convention | Alpha-numeric step labels (3b, 4b, 5b) in multi-phase branches of plan.md are fragile: any insertion requires cascade renumbering. The TS template avoids this via AC-N headings; workflow branches could benefit from the same approach (prose names, not position labels). | Execution observation | Medium |

## 7. Strategic Insights (Execution)

No strategic insights. No human domain input occurred during execution — direct implementation of pre-approved TS with no decision-altering conversation.

## 8. Diagrams

No diagrams. Phase B changes are workflow text insertions — architecture diagrams not applicable.

---

*RF — TFW-41 / Phase B: Workflow Gates | 2026-04-20*
