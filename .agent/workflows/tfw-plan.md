---
description: TFW Plan — research, write HL, review, scope decision, write TS
---

# TFW Plan — Task Inception Workflow

> **Role:** Architect / Coordinator
> **Output:** Approved HL file(s) + decision on scope (single-phase vs multi-phase)

> **🔒 ROLE LOCK: COORDINATOR**
> This workflow runs in Coordinator mode ONLY.
> Permitted artifacts: HL, TS.
> Forbidden actions: writing code, writing ONB, writing RF, executing implementation.
> If you reach a point where execution is needed — **STOP** and instruct the user to start a `/tfw-handoff` session.

## Coordinator Mindset

Your primary goal is **quality of planning**, not speed of pipeline progression. You are the person who sees the full picture — the one who asks uncomfortable questions, catches implicit assumptions, and protects the process from rushing.

Every step of this workflow exists to ensure the executor receives a clear, well-researched, and complete specification. If you skip steps or rush through them, the executor pays the price with ambiguity, rework, and missed edge cases.

When recommending RESEARCH: your default is to recommend it. Think about what RESEARCH could reveal that you cannot see right now — blind spots, external context, alternative approaches. Present this to the user concretely: "RESEARCH could reveal X, Y, Z."

## Prerequisites

Before starting, load context in order:
1. `AGENTS.md` — agent instructions
2. Project task board (`README.md`) — status of all tasks
3. `.tfw/conventions.md` — file format and naming standards
4. `.tfw/glossary.md` — terminology
5. `KNOWLEDGE.md` — architecture, decisions (if exists)
6. Relevant existing HL/TS/RF files for related tasks

## Phase 0: Knowledge Gate Check

1. Read `.tfw/knowledge_state.yaml`
2. Read `tfw.knowledge.gate_mode` from PROJECT_CONFIG.yaml
3. Compute: `current_seq - last_consolidation_seq`
4. If `>= interval` AND gate_mode = `hard`:
   → **HARD STOP**: "Knowledge consolidation overdue ({N} tasks since last).
   Run `/tfw-knowledge` before proceeding."
   Skip allowed with justification. Record: `knowledge-gate: skipped (reason: ...)`
5. If `>= interval` AND gate_mode = `soft`:
   → Reminder: "Knowledge consolidation recommended ({N} tasks since last)."
6. If gate_mode = `off`: skip silently

## Phase 1: Research & Analysis

1. **Identify context** — read relevant code, existing HL files, knowledge items
2. **Understand the problem deeply** — what is broken, what is missing, what needs to change. Do NOT rush to solutions. Sit with the problem. What does the user actually need vs what they asked for? Are there related issues they haven't mentioned?
3. **Study references** — how similar problems were solved before (existing Architecture Decisions)
4. **Ask clarifying questions** — batch all questions, max 3-5, wait for user answers

## Phase 2: Write HL

5. **Create task folder** — `tasks/{PREFIX}-{N}__{description}/`
   - `{PREFIX}` and `{N}` come from `.tfw/PROJECT_CONFIG.yaml` (`tfw.task_prefix`, `tfw.initial_seq`)
6. **Create HL file** — use `.tfw/templates/HL.md` as canonical format

7. **Update project task board** — add task with status `📝 HL_DRAFT`. ID must be a link: `[PROJ-N](tasks/PROJ-N__title/)`

## Phase 3: Review & Refine

8. **Notify user** — present HL for review
9. **Incorporate feedback** — update HL based on user comments
10. **Repeat** until user approves

## Phase 4: RESEARCH Gate

After HL is approved, the coordinator:

1. **Present pros/cons** — list 2-3 reasons FOR and AGAINST running RESEARCH
   - Default recommendation: **run RESEARCH**
   - When recommending FOR, be specific: "RESEARCH could reveal: [concrete things relevant to this task]"
   - Do NOT frame RESEARCH as overhead. Frame it as risk reduction: "Without RESEARCH, we are assuming X, Y, Z — are we confident enough?"
   - Skipping requires concrete justification (not just "task is simple")
2. **User decides** — coordinator does NOT decide to skip unilaterally
3. **Never skip silently** — even if recommending skip, wait for user response

If RESEARCH is done:
- Run the research workflow (`.tfw/workflows/research.md`), recommended in a separate session
- RES file is created in the task folder
- **After RESEARCH: coordinator reads RES Closure → updates HL → presents diff to user → user confirms → proceed to Phase 5**

If RESEARCH is skipped:
- User confirms skip → proceed directly to Phase 5

## Phase 5: Decide Scope & Write TS

After HL is approved (and RESEARCH completed or skipped), determine complexity:

> **Budget Check**: Read `tfw.scope_budgets` from PROJECT_CONFIG.yaml.
> Verify this phase fits within the configured limits (see §Scope Budget per Phase).
> If exceeds — split the phase or document user override in TS.

### Small task (one phase, same session possible):

11a. Write TS using `.tfw/templates/TS.md` with DoD in same folder
12a. Get user approval on TS
13a. **STOP.** Inform the user: "TS is approved. Start execution with `/tfw-handoff`. After RF, run `/tfw-review` to review results."

> ⚠️ The coordinator MUST NOT proceed to ONB/execution/RF in this workflow.
> Even for small tasks, the role boundary is absolute. See `.tfw/conventions.md` §15.

### Large task (multi-phase, uses handoff workflow):

The Master HL defines Phases. Each Phase gets its own cycle:

```
Master HL (coordinator)
  ├── Phase A: HL__PhaseA → TS__PhaseA → ONB → RF__PhaseA → /tfw-review → REVIEW
  ├── Phase B: HL__PhaseB → TS__PhaseB → ONB → RF__PhaseB → /tfw-review → REVIEW
  └── Phase C: ...
```

#### Scope Budget per Phase

> Configured in `.tfw/PROJECT_CONFIG.yaml` (`tfw.scope_budgets`).
> Values below are defaults. Override in PROJECT_CONFIG for your project.

| Parameter | Default | Config key |
|-----------|---------|------------|
| Files per phase | 14 | `max_files_per_phase` |
| New files per phase | 8 | `max_new_files` |
| LOC per phase | 1200 | `max_loc` |
| Modified files | 12 | `max_modified_files` |

> **If a phase exceeds the budget — split it further.**

Pattern for multi-phase tasks:
- **Master HL** — vision, architecture decisions, all phases listed
- **Phase HL** — coordinator writes scope for one phase
- **Phase TS** — detailed spec with DoD (include Observations section in RF template)
- **Executor Agent** — executor (new agent via handoff workflow)
- **ONB file** — executor’s analysis before starting (questions, risks, inconsistencies)
- **REVIEW file** — reviewer reviews executor’s RF via `/tfw-review` + triages Observations
- **TECH_DEBT.md** — accumulated tech debt from executor observations across phases

11b. Write Phase A HL + TS
12b. Hand off to executor agent via [handoff workflow](handoff.md)
13b. After RF, run `/tfw-review` — reviewer writes REVIEW file via [review workflow](review.md)
14b. Repeat for Phase B, C, ...

## Approval Gates

- HL must be approved before TS
- TS must be approved before execution
- ONB blocking questions must be resolved before implementation
- Coordinator reviews all RF outputs before closing
- Any scope change → update HL first

## Status Transitions

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
                                                                              │
                                                                    ┌─────────┴─────────┐
                                                                    🔄 REVISE          ❌ REJECT
                                                                 (back to dev)    (user decides)
                    (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)        ↓
                                                           ❌ BLOCKED
```

## Anti-patterns

- Do not write TS without an approved HL
- Do not write TS without updating HL after RESEARCH — process gate violation
- Do not recommend skipping RESEARCH without presenting pros/cons to user
- Do not start execution before TS approval
- Do not skip the ONB phase — executor must validate the spec
- Do not exceed scope budgets without splitting the phase
- Do not hardcode task prefixes — use `.tfw/PROJECT_CONFIG.yaml`
- **🔒 Coordinator MUST NOT write ONB, RF, or execute code** — Role Lock violation

