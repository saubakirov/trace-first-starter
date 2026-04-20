# TS — TFW-41 / Phase B: Workflow Gates

> **Date**: 2026-04-20
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)

---

## 1. Objective

Add structural gates to TFW workflows: Pre-TS Gate (coordinator reads RF before writing TS), Pre-RF Gate (executor opens template before writing), Execution Loops (dependency-based self-check), coordinator ONB answer protocol, reviewer HL §7 principles check, and Session Naming Step 0. These gates prevent the systematic failures observed in HD-16/HD-18 at their source — during execution, not during review.

## 2. Scope

### In Scope
- Modify `handoff.md` — Pre-RF Gate, Execution Loops, coordinator ONB answer protocol
- Modify `plan.md` — Pre-TS Gate
- Modify `review.md` — HL §7 principles verification in Judge phase
- Add Session Naming Step 0 to all 3 workflows

### Out of Scope
- Template changes (Phase A — done)
- Research template changes (Phase C)
- Glossary and adapter sync (Phase D)

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | Gates over guidelines | AC-1, AC-2, AC-3, AC-4, AC-5 | Each AC adds a structural gate, not a textual suggestion |
| P2 | Requirements, not implementation | N/A | Phase B modifies workflows, not TS template |
| P3 | Verify against fact, not plan | AC-2 | Pre-TS Gate: read RF N-1 before writing TS N |
| P4 | Enforce or remove | AC-5 | Judge verifies principles against AC |
| P5 | Executor as engineer, not copier | AC-3 | Execution Loops force self-checking |
| P6 | Domain-agnostic by default | All ACs | No domain-specific terminology in gate descriptions |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/workflows/handoff.md` | MODIFY | Add Pre-RF Gate, Execution Loops, ONB answer protocol, Session Naming |
| `.tfw/workflows/plan.md` | MODIFY | Add Pre-TS Gate, Session Naming |
| `.tfw/workflows/review.md` | MODIFY | Add HL §7 principles check in Judge, Session Naming |

**Budget:** 0 new files, 3 modifications. Defaults: max 14 files, max 8 new, max 1200 LOC.

## 5. Acceptance Criteria

### AC-1: Pre-RF Gate in handoff.md

Before the executor writes RF, they must open the RF template. This prevents writing from memory.

- [ ] handoff.md Phase 3 has explicit step: "Open `.tfw/templates/RF.md`. Read all section headings. Then write RF following this structure."
- [ ] Step is BEFORE "Create RF file" (current step 11)
Gate: Read handoff.md → Pre-RF step exists before RF creation step

### AC-2: Pre-TS Gate in plan.md

Before the coordinator writes TS for Phase N (where N > first phase), they must read the RF of the latest completed phase. Prevents plan≠fact drift.

- [ ] plan.md Step 7 (Write TS) has sub-step for multi-phase: "Read RF of the latest completed phase. Verify: what was actually delivered? What deviated from plan?"
- [ ] Sub-step is BEFORE "Write TS using templates/TS.md"
- [ ] Explicitly says: "Read RF (actual output), not TS (planned output)"
Gate: Read plan.md → Pre-TS sub-step exists in Step 7, references RF not TS

### AC-3: Execution Loops in handoff.md  [depends: AC-1]

When AC items in the TS have `[depends: AC-X]` annotations, the executor must verify each prerequisite AC before proceeding to its dependent.

- [ ] handoff.md Phase 2 has Execution Loops instruction: "If TS §5 contains `[depends: AC-X]` annotations — verify prerequisite AC gate before starting dependent AC"
- [ ] Instruction explains: "If AC-2 depends on AC-1, verify AC-1 gate passes before starting AC-2 implementation"
- [ ] Instruction says: "Independent ACs (no `[depends]`) may be implemented in any order"
Gate: Read handoff.md → Execution Loops instruction exists in Phase 2

### AC-4: Coordinator ONB answer protocol in handoff.md

When the coordinator answers ONB questions and is uncertain, they must present options rather than deciding on behalf of the stakeholder.

- [ ] handoff.md Phase 1 (or between Phase 1 and 2, where coordinator answers) has: "When answering ONB questions — if answer is not in HL/TS/KNOWLEDGE.md, present 2-3 options with tradeoffs. Do not decide on behalf of the stakeholder."
Gate: Read handoff.md → ONB answer protocol exists

### AC-5: HL §7 principles check in review.md Judge phase

Reviewer verifies that HL §7 principles survived into implementation. Each principle should be traceable: Principle → TS AC (via Principles Check table) → RF result.

- [ ] review.md Step 3 (Judge) has checklist item: "HL §7 principles — read TS §3 Principles Check table. For each mapped principle: verify the linked AC was met in RF §3."
- [ ] Instruction says: "If a principle was mapped to AC but AC failed → flag as principle violation, not just AC miss"
Gate: Read review.md → Principles check exists in Judge step

### AC-6: Session Naming Step 0 in all workflows  

Every workflow starts with naming the session. Format: `Role | Task-ID | Phase`.

- [ ] handoff.md has Step 0 before Context Loading: "Name this session: `Executor | {TASK-ID} | Phase {X}`"
- [ ] plan.md has Step 0 before Step 1: "Name this session: `Coordinator | {TASK-ID}`"
- [ ] review.md has Step 0 before Context Loading: "Name this session: `Reviewer | {TASK-ID} | Phase {X}`"
Gate: Read all 3 workflows → each starts with Step 0 naming instruction

## 6. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF.

- **handoff.md** (148 lines): main insertion points are Phase 1 (ONB answer protocol), Phase 2 (Execution Loops), Phase 3 (Pre-RF Gate). Session Naming before Context Loading.
- **plan.md** (146 lines): Pre-TS Gate goes into Step 7 (Write TS), specifically the multi-phase branch (Step 3b, line 124). Session Naming before Step 1.
- **review.md** (145 lines): Principles check goes into Step 3 (Judge, line 81). Session Naming before Context Loading.
- RF Phase A observation: no hardcoded section numbers in workflows — but check for references to "Detailed Steps" or "§4"/"§5 Acceptance Criteria" from old TS template and update if found.
- Keep additions concise — workflows have an informal ~1200 word budget. Estimate: ~50-80 words total per workflow addition.
- Session Naming format uses pipe `|` separator and `{TASK-ID}` placeholder for consistency.
- Coordinator answers ONB questions in an ad-hoc process (between ONB and execution). In handoff.md the gap is between steps 5-6. Consider adding the protocol as a blockquote instruction in step 5 or as a new sub-step.

## 7. Definition of Failure

- ❌ Any gate added as a "suggestion" or "recommendation" instead of a mandatory step → reject RF
- ❌ Pre-TS Gate references reading "TS" instead of "RF" → defeats the purpose (plan≠fact)
- ❌ Execution Loops triggered by AC count instead of `[depends]` annotation → wrong mechanism
- ❌ Session Naming missing from any of the 3 workflows → reject RF

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Workflow word count exceeds budget | Additions are ~50-80 words per workflow. Existing workflows are within budget. |
| New steps disrupt workflow reading flow | Gates are inserted at natural handoff points (before writing, between phases). Not adding new phases. |
| ONB answer protocol scope creep | Protocol is one instruction, not a new workflow section |

## 9. Cross-Phase Modifications (multi-phase only)

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/conventions.md` | Phase A (anti-patterns), Phase C (terminology origin) | Phase B does NOT modify conventions.md — but gates reference anti-patterns added in Phase A |

> **Cross-references**: HL-TFW-41 §4 Phase B, DR2 (Pre-TS Gate), DR3 (Execution Loops), D6 (Pre-RF Gate), D9 (ONB protocol), D10 (Judge principles), D11 (Session Naming). RF Phase A §2 Decision 5 (no hardcoded section numbers in workflows).

---

*TS — TFW-41 / Phase B: Workflow Gates | 2026-04-20*
