---
description: TFW Handoff — executor onboarding, implementation, RF
---

# TFW Handoff — Task Execution by New Agent

> **Roles:** Coordinator (hands off) → Executor (receives, questions, implements)
> **Input:** Approved HL + TS files
> **Output:** RF file with implementation results

> **🔒 ROLE LOCK: EXECUTOR**
> Permitted artifacts: ONB, RF.
> Forbidden actions: writing HL, writing TS, writing REVIEW, modifying HL, changing scope.
> The executor MUST NOT modify HL or TS. If scope issues are found — write them in ONB and **STOP**.

## Step 0: Name This Session

**Name this session:** `Executor | {TASK-ID} | Phase {X}`
Set this as the session/conversation name before doing anything else.

## Context Loading (Executor)

When starting as executor, load in order:
1. `AGENTS.md` — agent instructions
2. `.tfw/conventions.md` — project conventions
3. `.tfw/glossary.md` — terminology
4. `KNOWLEDGE.md` — architecture, decisions, legacy (if exists)
5. **Master HL** for the task — understand vision, design philosophy, architecture decisions
6. **Phase HL** (if multi-phase) — phase-specific scope and context
7. **TS file** for the task — exact scope, DoD, constraints
8. Related HL/TS/RF files referenced in the task
9. Relevant code files listed in TS

## Phase 1: Executor Onboarding

1. **Read all context** — HL, TS, referenced files, relevant code
2. **Analyze the task** — identify:
   - Questions that need clarification (blocking and non-blocking)
   - Recommendations for improvement
   - Risks and edge cases not covered in TS
   - Read HL §7.2 Knowledge Citations — verify each item, fill ONB §7.
     For each citation: confirm read, state how applied or why N/A.
     Add any NEW PV items you find relevant that coordinator missed.
   - Inconsistencies between HL/TS/KNOWLEDGE.md and actual code
   - Missing information or incomplete specifications
   - Errors, gaps, or oversights in the spec
3. **Write ONB file** — use `.tfw/templates/ONB.md` as canonical format. Structured as:

   ```markdown
   ## Questions (blocking — cannot proceed without answers)
   | # | Question | Answer |
   |---|----------|--------|

   ## Recommendations (suggestions, not blocking)
   1. ...

   ## Risks Found (edge cases, potential issues not in TS)
   1. ...

   ## Inconsistencies with Code (spec vs reality)
   1. ...
   ```

4. **Commit and push ONB** — the onboarding report is a first-class artifact
5. **Wait for user approval** — do NOT proceed until all blocking questions resolved

   > **Coordinator ONB answer protocol:** When answering blocking questions — if the answer is not explicitly stated in HL, TS, or KNOWLEDGE.md, present 2-3 options with tradeoffs. Do not decide on behalf of the stakeholder.

6. **Update project task board** — status to `🟠 ONB`

## Phase 2: Execution

7. **Update project task board** — change status to `🟢 RF` (in progress)
8. **Implement** — follow TS step by step:
   - For code changes: write production-ready code, no placeholders
   - For CL tasks: present commands/SQL to user, wait for execution
   - For AG tasks: create artifacts directly

   **Execution Loops** — if TS acceptance criteria have `[depends: AC-X]` annotations (meaning one AC must be verified before another can start): verify the prerequisite AC gate passes before starting the dependent AC. Example: if AC-2 has `[depends: AC-1]`, verify AC-1 is complete before implementing AC-2. Independent ACs (no `[depends]`) may be implemented in any order.

9. **Run tests** — as specified in TS verification section
10. **Build gate** — run build/compile command from TS verification section.
    If build fails → fix BEFORE writing RF. Never write RF with failing build.

## Phase 3: Write RF

11. **Pre-RF Gate** — open `.tfw/templates/RF.md`. Read all section headings before writing anything. Then write RF following this structure.

12. **Create RF file** — use `.tfw/templates/RF.md` as canonical format. MANDATORY sections:
    - **§1 What Was Done** — changes list with file paths
    - **§2 Key Decisions** — decisions and rationale
    - **§3 Acceptance Criteria** — checkmark each TS DoD item
    - **§4 Verification** — lint/test/verify results
    - **§5 Observations** — out-of-scope items noticed (table format). Quality bar: only issues that would bite the next developer.
    - **§6 Fact Candidates** — review conversation history, extract human-sourced knowledge. If none: "No fact candidates."
    - **§7 Strategic Insights** — capture domain knowledge with implications. If none: "No strategic insights."
    - **§8 Diagrams** — architecture, data flow, component interaction. If none: "No diagrams."
    Never omit §6-8. Empty content is acceptable ("No X."); absent section is not.

> 💡 As you work, capture strategic knowledge about the project — stakeholder priorities,
> domain patterns, business context, external constraints — in §6 Fact Candidates.
> These save the next agent from missing critical context.
>
> **Before writing Fact Candidates, review the conversation history.** The human's
> messages are the primary source — their decisions, priorities, concerns, and domain
> insights. Extract what informs decisions, not implementation details.

### Observations Section (mandatory in RF)

Executors MUST report anything they noticed but did NOT modify:

```markdown
## Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `example.tsx` | 42 | dead-code | Unused import `OldComponent` |
| 2 | `utils.ts` | 15-20 | duplication | Same helper exists in 3 files |
```

**Types:** `dead-code`, `naming`, `todo`, `duplication`, `perf`, `security`, `style`, `missing-test`, `ux`

**Quality bar**: report only issues that would bite the next developer. Don't generate observations just because the section exists.

If nothing found, write: `No observations.`

## 🛑 Executor STOP

> **Your work is done.** Do NOT proceed to review.
> Inform the user: "RF is complete. Start `/tfw-review` to review the results."
> Writing a REVIEW file as executor is a **🔒 Role Lock violation**.

## Multi-Phase Task Flow

For large tasks broken into phases:

```
Coordinator: Master HL (approved)
    │
    ├── Phase A: Coordinator writes HL__PhaseA + TS__PhaseA
    │   └── Executor Agent: reads → ONB → executes → RF__PhaseA
    │   └── After RF, run /tfw-review for review
    │
    ├── Phase B: Coordinator writes HL__PhaseB + TS__PhaseB
    │   └── Executor Agent: reads → ONB → executes → RF__PhaseB
    │   └── After RF, run /tfw-review for review
    │
    └── ... repeat per Phase
```

Each Phase Agent starts with full context loading.
Coordinator maintains the Master HL for continuity.

## Anti-patterns

> Full generic list → conventions.md §14. Role-specific items below:

- Executor continues past Phase 3 — must STOP after RF
- Executor writes REVIEW file — **🔒 Role Lock violation**
- **🔒 Executor MUST NOT write HL, TS, REVIEW, or change scope** — Role Lock violation
