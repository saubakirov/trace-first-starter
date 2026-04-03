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
   - Inconsistencies between HL/TS and actual code
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
6. **Update project task board** — status to `🟠 ONB`

## Phase 2: Execution

7. **Update project task board** — change status to `🟢 RF` (in progress)
8. **Implement** — follow TS step by step:
   - For code changes: write production-ready code, no placeholders
   - For CL tasks: present commands/SQL to user, wait for execution
   - For AG tasks: create artifacts directly
9. **Run tests** — as specified in TS verification section
10. **Build gate** — run build/compile command from TS verification section.
    If build fails → fix BEFORE writing RF. Never write RF with failing build.

## Phase 3: Write RF

12. **Create RF file** — use `.tfw/templates/RF.md` as canonical format. Must contain:
    - What was done (changes list with file paths)
    - Test results (pass/fail, output logs)
    - Known limitations or tech debt
    - Deviations from TS (if any, with justification)
    - Screenshots / logs if applicable
    - **Observations** (out-of-scope items noticed during work)

> 💡 As you work, capture what you learn about the project — environment, constraints,
> stakeholders, conventions — in §6 Fact Candidates. These save the next agent
> from re-learning the same lessons.

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

- Executor starts coding before all blocking questions resolved
- Executor skips reading HL and goes straight to code
- RF file doesn't mention test results
- TS is written without an approved HL
- Phase Agent modifies Master HL without coordinator approval
- Executor makes architectural decisions not in HL
- Executor modifies files outside TS scope (even "obvious fixes" or "while I'm here")
- Executor does "bonus fixes" without documenting in RF deviations table
- Executor writes RF before build/compile passes
- Executor sees tech debt / dead code but doesn't report it in Observations
- Executor writes REVIEW file — **🔒 Role Lock violation**
- Executor continues past Phase 3 — must STOP after RF
- **🔒 Executor MUST NOT write HL, TS, REVIEW, or change scope** — Role Lock violation
