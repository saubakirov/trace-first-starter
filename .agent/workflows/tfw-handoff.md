# TFW Handoff — Task Execution by New Agent

> **Roles:** Coordinator (hands off) → Executor (receives, questions, implements) → Coordinator (reviews)
> **Input:** Approved HL + TS files
> **Output:** RF file with implementation results + REVIEW file with verdict

> **🔒 ROLE LOCK: EXECUTOR** (Phases 1-3) → **COORDINATOR** (Phase 4: Review)
> Phase 1-3 permitted artifacts: ONB, RF.
> Phase 1-3 forbidden actions: writing HL, writing TS, modifying HL, changing scope.
> Phase 4 permitted: REVIEW file only.
> The executor MUST NOT modify HL or TS. If scope issues are found — write them in ONB and **STOP**.

## Context Loading (Executor)

When starting as executor, load in order:
1. `AGENTS.md` — agent instructions
2. `.tfw/conventions.md` — project conventions
3. `.tfw/glossary.md` — terminology
4. **Master HL** for the task — understand vision, design philosophy, architecture decisions
5. **Phase HL** (if multi-phase) — phase-specific scope and context
6. **TS file** for the task — exact scope, DoD, constraints
7. Related HL/TS/RF files referenced in the task
8. Relevant code files listed in TS

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
11. **Update STEPS.md** — Summary lines for each significant milestone

## Phase 3: Write RF

12. **Create RF file** — use `.tfw/templates/RF.md` as canonical format. Must contain:
    - What was done (changes list with file paths)
    - Test results (pass/fail, output logs)
    - Known limitations or tech debt
    - Deviations from TS (if any, with justification)
    - Screenshots / logs if applicable
    - **Observations** (out-of-scope items noticed during work)

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

## Phase 4: Coordinator Review

The **coordinator** (original architect or user) reviews the RF.

13. **Review checklist:**

| Check | Description |
|-------|-------------|
| **DoD met?** | All items from TS Definition of Done achieved |
| **Code quality** | Follows project conventions, naming, type hints |
| **Test coverage** | Tests written and passing per TS |
| **Philosophy aligned** | Matches design philosophy from HL |
| **Tech debt** | Any shortcuts taken? Documented? |
| **Security** | No secrets exposed, guards in place |
| **Observability** | Logging, trace_id, records preserved |
| **Breaking changes** | API compat, backward compat, migration needed? |
| **Style & standards** | Code style, naming conventions |

14. **Write REVIEW file** — use `.tfw/templates/REVIEW.md` as canonical format

### Tech Debt Collection (coordinator duty)

After review, coordinator MUST:
1. Read executor's `## Observations` section from RF
2. Triage each item (severity: Low/Medium/High)
3. Add to REVIEW file as `## Tech Debt Collected` section
4. Append to project-level `TECH_DEBT.md`

```markdown
## Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | Phase A RF | Low | 3 files | Duplicate helpers | → backlog |
```

15. **Verdict:**
    - **✅ APPROVE** — all checks pass → close, update all traces
    - **🔄 REVISE** — specific items to fix → executor iterates (back to Phase 2)
    - **❌ REJECT** — fundamental issues → back to HL/TS revision

16. **Update project task board** — final status
17. **Update STEPS.md** — completion Summary

## Multi-Phase Task Flow

For large tasks broken into phases:

```
Coordinator: Master HL (approved)
    │
    ├── Phase A: Coordinator writes HL__PhaseA + TS__PhaseA
    │   └── Executor Agent: reads → ONB → executes → RF__PhaseA
    │   └── Coordinator: reviews → REVIEW__PhaseA → ✅/🔄/❌
    │
    ├── Phase B: Coordinator writes HL__PhaseB + TS__PhaseB
    │   └── Executor Agent: reads → ONB → executes → RF__PhaseB
    │   └── Coordinator: reviews → REVIEW__PhaseB → ✅/🔄/❌
    │
    └── ... repeat per Phase
```

Each Phase Agent starts with full context loading.
Coordinator maintains the Master HL for continuity.

## Anti-patterns

- Executor starts coding before all blocking questions resolved
- Executor skips reading HL and goes straight to code
- Coordinator skips review and deploys without REVIEW file
- RF file doesn't mention test results
- TS is written without an approved HL
- Phase Agent modifies Master HL without coordinator approval
- Executor makes architectural decisions not in HL
- Executor modifies files outside TS scope (even "obvious fixes" or "while I'm here")
- Executor does "bonus fixes" without documenting in RF deviations table
- Executor writes RF before build/compile passes
- Executor sees tech debt / dead code but doesn't report it in Observations
- Coordinator ignores executor Observations — must triage and log in TECH_DEBT.md
- **🔒 Executor MUST NOT write HL, TS, or change scope** — Role Lock violation
