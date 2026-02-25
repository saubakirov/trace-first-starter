# TFW v3 — Conventions

## 1) Purpose

TFW turns work (analytics, documents, code, research) into a reproducible process:
- context is captured,
- decisions are traced,
- results are repeatable,
- any agent can continue the project in a new session.

## 2) Required Artifacts (project root)

- `README.md` — human explanation: why/what/how. Contains Task Board.
- `AGENTS.md` — AI agent behavior rules for the project.
- `TASK.md` — boundaries, DoD, risks, constraints.
- `STEPS.md` — iteration log (short Summary lines).
- `TECH_DEBT.md` — accumulated tech debt from reviews (observations → triage → registry).
- `.tfw/README.md` — TFW philosophy, lifecycle, values.
- `.tfw/conventions.md` — project conventions (this file).
- `.tfw/glossary.md` — project glossary.
- `.tfw/templates/HL.md` — canonical HL template.
- `.tfw/templates/TS.md` — canonical TS template.
- `.tfw/templates/RF.md` — canonical RF template.
- `.tfw/templates/ONB.md` — canonical Onboarding Report template.
- `.tfw/templates/REVIEW.md` — canonical Review template.
- `.tfw/workflows/plan.md` — canonical planning workflow.
- `.tfw/workflows/handoff.md` — canonical execution workflow.
- `.tfw/workflows/resume.md` — canonical resume workflow.
- `.tfw/PROJECT_CONFIG.yaml` — project configuration (stack, build commands, task prefix, execution engine).

## 3) Artifact Types (canonical)

### HL (High Level)
Context/frame. Not a task — a "map of meaning".
Format: strictly follows `.tfw/templates/HL.md`.

### TS (Task Spec)
Task definition. Always self-contained: inputs/outputs/constraints/DoD.
Format: strictly follows `.tfw/templates/TS.md`.

### RF (Result File)
Results/facts/data/final text. RF has priority as source of truth.
Contains mandatory Observations table (structured, typed).
Format: strictly follows `.tfw/templates/RF.md`.

### ONB (Onboarding Report)
Structured executor report before starting: understanding, questions, risks, inconsistencies.
Coordinator/human answers directly in the file (Q&A format).
Format: strictly follows `.tfw/templates/ONB.md`.

### REVIEW (Review Report)
Formal coordinator report after reviewing RF: checklist, verdict, tech debt.
Format: strictly follows `.tfw/templates/REVIEW.md`.

## 4) Task Numbering

ID format is defined in `.tfw/PROJECT_CONFIG.yaml` (field `tfw.task_prefix`).

File naming:

| Artifact | Format | Example |
|----------|--------|---------|
| Master HL | `HL-{PREFIX}-{N}__{title}.md` | `HL-PROJ-3__tfw-setup.md` |
| Phase TS | `TS__Phase{X}__{title}.md` | `TS__PhaseA__conventions.md` |
| Phase RF | `RF__Phase{X}__{title}.md` | `RF__PhaseA__conventions.md` |
| Phase ONB | `ONB__Phase{X}__{title}.md` | `ONB__PhaseA__conventions.md` |
| Phase REVIEW | `REVIEW__Phase{X}__{title}.md` | `REVIEW__PhaseA__conventions.md` |

Task folder: `tasks/{PREFIX}-{N}__{title}/`

## 5) Task Statuses

```
⬜ TODO → 🔵 HL → 🟡 TS → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
                                                              │
                                                    ┌─────────┴─────────┐
                                                    🔄 REVISE          ❌ REJECT
                                                 (back to dev)    (new HL/TS)
                     ↓
                ❌ BLOCKED
```

| Status | Meaning |
|--------|---------|
| ⬜ TODO | Task planned, HL not started |
| 🔵 HL | HL written, awaiting review/approval |
| 🟡 TS | TS written, awaiting approval for execution |
| 🟠 ONB | Onboarding: executor studying the task, asking questions, awaiting answers |
| 🟢 RF | Execution complete, RF written |
| 🔍 REV | Review: coordinator checking RF against checklist |
| ✅ DONE | Task closed, traces updated |
| ❌ BLOCKED | Blocked by dependency |

Review verdicts:
- ✅ **APPROVE** — all ok → ✅ DONE, update all traces
- 🔄 **REVISE** — specific issues → back to execution (same task)
- ❌ **REJECT** — fundamental problems → new task with HL/TS

## 6) Scope Budgets (per Phase)

> Calibrated for AI executor agents. Exceeding limits — split the phase.

| Parameter | Budget | Rationale |
|-----------|--------|-----------|
| Files per phase | ≤ 7 | Agent maintains full mental model |
| NEW files | ≤ 4 | Each new file needs consistent patterns |
| New code (LOC) | ≤ 600 | Beyond this, repetition and shortcuts appear |
| Modified files | ≤ 6 | Each modify requires reading + understanding |

## 7) Execution Modes

### CL (Chat Loop) — default
- AI proposes steps, human approves/executes.
- AI does NOT execute external actions without approval.

### AG (Autonomous) — explicit request only
- AI works independently within approved TS scope.
- Makes incremental commits.
- Stops when encountering issues not covered by TS.

## 8) Workflows

TFW v3 defines three canonical workflows in `.tfw/workflows/`:

| Workflow | Role | Purpose |
|----------|------|---------|
| [plan.md](workflows/plan.md) | Coordinator | Research → HL → review → scope decision → TS |
| [handoff.md](workflows/handoff.md) | Executor + Coordinator | Context load → ONB → execute → RF → REVIEW |
| [resume.md](workflows/resume.md) | Coordinator | Locate task → status matrix → decide next phase |

## 9) Tool Adapter Pattern

`.tfw/` is the tool-agnostic core — one copy per project. Each development tool reads its own entry point, which references `.tfw/`:

```
CLAUDE.md ──→ "Read .tfw/README.md, follow .tfw/conventions.md"
.cursor/rules ──→ "Read .tfw/README.md, follow .tfw/conventions.md"
```

Adapters are chosen at project init. See `.tfw/init.md` for setup.

## 10) Context Loading Order (new session, strict)

1. `AGENTS.md`
2. `STEPS.md`
3. `TASK.md`
4. `.tfw/conventions.md`, `.tfw/glossary.md`
5. Relevant HL/TS/RF for the current task

## 11) Quality Standard (no compromises)

- No placeholders.
- Results must be usable without manual edits.
- If a result is wrong — fix the prompt/context and retry until quality is met.
- Tasks are atomic and human-verifiable.

## 12) Safety and Execution Honesty

- In CL mode, never claim something was "run" or "tested" outside the session.
- Never request secrets in plain text. Use environment variables.

## 13) Summary Line (mandatory in every significant reply)

```
**Summary**: Stage={stage} | Task={description} | Status={status}
```

## 14) Anti-patterns (prohibited)

- Executor starts coding before all blocking questions resolved
- Executor skips reading HL and goes straight to code
- Coordinator skips review and closes without REVIEW file
- RF file doesn't mention test results or observations
- TS is written without an approved HL
- Executor modifies Master HL without coordinator approval
- Executor makes architectural decisions not in HL
- Executor modifies files outside TS scope (even "obvious fixes")
- Executor does "bonus fixes" without documenting in RF deviations
- Executor writes RF before build/lint passes
- Executor sees tech debt / dead code but doesn't report in Observations
- Coordinator ignores executor Observations — must triage to TECH_DEBT.md
