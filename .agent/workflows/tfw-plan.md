# TFW Plan — Task Inception Workflow

> **Role:** Architect / Coordinator
> **Output:** Approved HL file(s) + decision on scope (single-phase vs multi-phase)

## Prerequisites

Before starting, load context in order:
1. `AGENTS.md` — agent instructions
2. `STEPS.md` — progress log
3. `TASK.md` — backlog and priorities
4. Project task board (`README.md`) — status of all tasks
5. `.tfw/conventions.md` — file format and naming standards
6. `.tfw/glossary.md` — terminology
7. Relevant existing HL/TS/RF files for related tasks

## Phase 1: Research & Analysis

1. **Identify context** — read relevant code, existing HL files, knowledge items
2. **Understand the problem** — what is broken, what is missing, what needs to change
3. **Study references** — how similar problems were solved before (existing Architecture Decisions)
4. **Ask clarifying questions** — batch all questions, max 3-5, wait for user answers

## Phase 2: Write HL

5. **Create task folder** — `tasks/{PREFIX}-{N}__{description}/`
   - `{PREFIX}` and `{N}` come from `PROJECT_CONFIG.yaml` (`tfw.task_prefix`, `tfw.initial_seq`)
6. **Create HL file** — use `.tfw/templates/HL.md` as canonical format

### Naming Rules

> Files ALWAYS include the task number. Without a number — error.

| Artifact | Format | Example |
|----------|--------|---------|
| Master HL | `HL-{PREFIX}-{N}__{title}.md` | `HL-PROJ-5__query_redesign.md` |
| Phase HL | `HL__PhaseA__{title}.md` | `HL__PhaseA__data_collection.md` |
| Phase TS | `TS__PhaseA__{title}.md` | `TS__PhaseA__data_collection.md` |
| Phase ONB | `ONB__PhaseA__{title}.md` | `ONB__PhaseA__data_collection.md` |
| Phase RF | `RF__PhaseA__{title}.md` | `RF__PhaseA__data_collection.md` |
| Phase Review | `REVIEW__PhaseA__{title}.md` | `REVIEW__PhaseA__data_collection.md` |

**Sub-task numbering:** dot-notation from master number.
Master = PROJ-5 → Sub-tasks = PROJ-5.1, PROJ-5.2, ...
Phases = letters (Phase A, B, C) or numbers (Phase 1, 2, 3) — choose one and keep consistent within a task.

7. **Update project task board** — add task with status `🔵 HL`
8. **Update STEPS.md** — add Summary line

## Phase 3: Review & Refine

9. **Notify user** — present HL for review
10. **Incorporate feedback** — update HL based on user comments
11. **Repeat** until user approves

## Phase 4: Decide Scope

After HL is approved, determine complexity:

### Small task (one phase, same agent):

12a. Write TS using `.tfw/templates/TS.md` with DoD in same folder
13a. Get user approval on TS
14a. Execute, write RF

### Large task (multi-phase, uses handoff workflow):

The Master HL defines Phases. Each Phase gets its own cycle:

```
Master HL (coordinator)
  ├── Phase A: HL__PhaseA → TS__PhaseA → ONB → RF__PhaseA → REVIEW
  ├── Phase B: HL__PhaseB → TS__PhaseB → ONB → RF__PhaseB → REVIEW
  └── Phase C: ...
```

#### Scope Budget per Phase

> Calibrated for AI executor agents. Beyond these limits, quality degrades:
> attention to detail drops, patterns become inconsistent, edge cases get missed.

| Parameter | Budget | Rationale |
|-----------|--------|-----------|
| Files per phase | ≤ 7 | Agent maintains full mental model |
| NEW files | ≤ 4 | Each new file needs consistent patterns |
| New code (LOC) | ≤ 600 | Beyond this, repetition and shortcuts appear |
| Modified files | ≤ 6 | Each modify requires reading + understanding |

> **If a phase exceeds the budget — split it further.**

Pattern for multi-phase tasks:
- **Master HL** — vision, architecture decisions, all phases listed
- **Phase HL** — coordinator writes scope for one phase
- **Phase TS** — detailed spec with DoD (include Observations section in RF template)
- **Executor Agent** — executor (new agent via handoff workflow)
- **ONB file** — executor's analysis before starting (questions, risks, inconsistencies)
- **REVIEW file** — coordinator reviews executor's RF + triages Observations
- **TECH_DEBT.md** — accumulated tech debt from executor observations across phases

12b. Write Phase A HL + TS
13b. Hand off to executor agent via [handoff workflow](handoff.md)
14b. Review RF, write REVIEW file
15b. Repeat for Phase B, C, ...

## Approval Gates

- HL must be approved before TS
- TS must be approved before execution
- ONB blocking questions must be resolved before implementation
- Coordinator reviews all RF outputs before closing
- Any scope change → update HL first

## Status Transitions

```
⬜ TODO → 🔵 HL → 🟡 TS → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
                                                              │
                                                    ┌─────────┴─────────┐
                                                    🔄 REVISE          ❌ REJECT
                                                 (back to dev)    (new HL/TS)
                     ↓
                ❌ BLOCKED
```

## Anti-patterns

- Do not write TS without an approved HL
- Do not start execution before TS approval
- Do not skip the ONB phase — executor must validate the spec
- Do not exceed scope budgets without splitting the phase
- Do not hardcode task prefixes — use `PROJECT_CONFIG.yaml`
