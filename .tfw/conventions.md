# TFW Conventions

## 1) Purpose

TFW turns work (analytics, documents, code, research) into a reproducible process:
- context is captured,
- decisions are traced,
- results are repeatable,
- any agent can continue the project in a new session.

## 2) Required Artifacts (project root)

- `README.md` — human explanation: why/what/how. Contains Task Board.
- `AGENTS.md` — AI agent behavior rules for the project.
- `TECH_DEBT.md` — accumulated tech debt from reviews (observations → triage → registry).
- `KNOWLEDGE.md` _(optional)_ — project knowledge index: architecture, decisions, legacy. Template: `.tfw/templates/KNOWLEDGE.md`.
- `RELEASE.md` _(optional)_ — project release strategy and context. Template: `.tfw/templates/RELEASE.md`.
- `.tfw/README.md` — TFW philosophy, lifecycle, values.
- `.tfw/conventions.md` — project conventions (this file).
- `.tfw/glossary.md` — project glossary.
- `.tfw/templates/HL.md` — canonical HL template.
- `.tfw/templates/TS.md` — canonical TS template.
- `.tfw/templates/RF.md` — canonical RF template.
- `.tfw/templates/ONB.md` — canonical Onboarding Report template.
- `.tfw/templates/RES.md` — canonical Research Report template.
- `.tfw/templates/REVIEW.md` — canonical Review template.
- `.tfw/workflows/init.md` — canonical initialization workflow.
- `.tfw/workflows/plan.md` — canonical planning workflow.
- `.tfw/workflows/research.md` — canonical research workflow.
- `.tfw/workflows/handoff.md` — canonical execution workflow.
- `.tfw/workflows/review.md` — canonical review workflow.
- `.tfw/workflows/resume.md` — canonical resume workflow.
- `.tfw/workflows/docs.md` — canonical knowledge update workflow.
- `.tfw/workflows/release.md` — canonical release workflow.
- `.tfw/workflows/update.md` — canonical upstream update workflow.
- `.tfw/VERSION` — current framework version (semver, single line).
- `.tfw/CHANGELOG.md` — version history (Keep a Changelog format).
- `.tfw/PROJECT_CONFIG.yaml` — project configuration (stack, build commands, task prefix, execution engine).

## 3) Artifact Types (canonical)

> See also: [glossary.md](glossary.md) for terminology, [README.md](README.md) for philosophy.

### HL (High Level)
Context/frame. Not a task — a "map of meaning".
Format: strictly follows `.tfw/templates/HL.md`.

### RES (Research Report)
Structured investigation artifact. Living document: decisions and questions at the top, stage logs below.
Created between HL and TS (pipeline) or standalone for any research.
Format: strictly follows `.tfw/templates/RES.md`.

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

### Fact Candidates (section in RF, REVIEW, RES)
Raw observations about the project recorded during work. NOT verified facts — they become facts after `/tfw-knowledge` consolidation. Each artifact has a Fact Candidates section with a structured table (Category, Candidate, Source, Confidence). Quality filter: "Would the next agent decide differently knowing this?"

## 4) Task Numbering

ID format is defined in `.tfw/PROJECT_CONFIG.yaml` (field `tfw.task_prefix`).

File naming:

| Artifact | Format | Example |
|----------|--------|---------|
| Master HL | `HL-{PREFIX}-{N}__{title}.md` | `HL-PROJ-3__tfw-setup.md` |
| Single-phase RES | `RES__{PREFIX}-{N}__{title}.md` | `RES__PROJ-3__tfw-setup.md` |
| Single-phase TS | `TS__{PREFIX}-{N}__{title}.md` | `TS__PROJ-3__tfw-setup.md` |
| Single-phase RF | `RF__{PREFIX}-{N}__{title}.md` | `RF__PROJ-3__tfw-setup.md` |
| Single-phase ONB | `ONB__{PREFIX}-{N}__{title}.md` | `ONB__PROJ-3__tfw-setup.md` |
| Single-phase REVIEW | `REVIEW__{PREFIX}-{N}__{title}.md` | `REVIEW__PROJ-3__tfw-setup.md` |
| Phase RES | `RES__Phase{X}__{title}.md` | `RES__PhaseA__conventions.md` |
| Phase TS | `TS__Phase{X}__{title}.md` | `TS__PhaseA__conventions.md` |
| Phase RF | `RF__Phase{X}__{title}.md` | `RF__PhaseA__conventions.md` |
| Phase ONB | `ONB__Phase{X}__{title}.md` | `ONB__PhaseA__conventions.md` |
| Phase REVIEW | `REVIEW__Phase{X}__{title}.md` | `REVIEW__PhaseA__conventions.md` |

> **Rule:** ALL artifact filenames MUST include the task ID (`{PREFIX}-{N}`) or Phase identifier. A filename without either is an error.

Task folder: `tasks/{PREFIX}-{N}__{title}/`

### Multi-phase folder structure

For multi-phase tasks, master artifacts (HL, RES) stay at task root. Each phase gets a subfolder:

```
tasks/PROJ-5__query_redesign/
  HL-PROJ-5__query_redesign.md        ← Master HL
  RES__PROJ-5__query_redesign.md      ← Master RES (if any)
  PhaseA/
    TS__PhaseA__data_model.md
    ONB__PhaseA__data_model.md
    RF__PhaseA__data_model.md
    REVIEW__PhaseA__data_model.md
  PhaseB/
    TS__PhaseB__api_layer.md
    ...
```

## 5) Task Statuses

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
                                                                              │
                                                                    ┌─────────┴─────────┐
                                                                    🔄 REVISE          ❌ REJECT
                                                                 (back to dev)    (user decides)
                    (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)        ↓
                                                           ❌ BLOCKED
```

| Status | Meaning |
|--------|---------|
| ⬜ TODO | Task planned, HL not started |
| 📝 HL_DRAFT | HL being drafted, awaiting review/approval |
| 🔬 RES | Research in progress (optional — user can skip to TS_DRAFT) |
| 🟡 TS_DRAFT | TS written, awaiting approval for execution |
| 🟠 ONB | Onboarding: executor studying the task |
| 🟢 RF | Execution complete, RF written |
| 🔍 REV | Review: reviewer checking RF |
| ✅ DONE | Task closed, traces updated |
| ❌ BLOCKED | Blocked by dependency |

Task Board format — ID column must be a relative link to the task folder:
```
| [PROJ-1](tasks/PROJ-1__title/) | Description | Status | ... |
```

Review verdicts:
- ✅ **APPROVE** — all ok → ✅ DONE, update all traces
- 🔄 **REVISE** — specific issues → back to execution (same task)
- ❌ **REJECT** → 🛑 User decides: (a) 📝 HL_DRAFT (rework HL), (b) 🔬 RES (new research), (c) 🟡 TS_DRAFT (rewrite TS)

## 6) Scope Budgets (per Phase)

> Configured in `.tfw/PROJECT_CONFIG.yaml` (`tfw.scope_budgets`).
> Values below are defaults. Override in PROJECT_CONFIG for your project.

| Parameter | Default | Rationale | Config key |
|-----------|---------|-----------|------------|
| Files per phase | 14 | Agent maintains full context of changed files | `max_files_per_phase` |
| New files per phase | 8 | Limits blast radius of new abstractions | `max_new_files` |
| LOC per phase | 1200 | Keeps changes reviewable in one pass | `max_loc` |
| Modified files | 12 | Prevents scattered, hard-to-review diffs | `max_modified_files` |

## 7) Execution Modes

### CL (Chat Loop) — default
- AI proposes steps, human approves/executes.
- AI does NOT execute external actions without approval.

### AG (Autonomous) — explicit request only
- AI works independently within approved TS scope.
- Makes incremental commits.
- Stops when encountering issues not covered by TS.

## 8) Workflows

TFW defines the following canonical workflows in `.tfw/workflows/`:

| Workflow | Role | Purpose |
|----------|------|---------|
| [init.md](workflows/init.md) | Coordinator | Discover project → interview → knowledge → setup → verify |
| [plan.md](workflows/plan.md) | Coordinator | Research → HL → RESEARCH gate → scope decision → TS |
| [research.md](workflows/research.md) | Coordinator | Structured investigation → RES artifact (pipeline or standalone) |
| [handoff.md](workflows/handoff.md) | Executor | Context load → ONB → execute → RF |
| [review.md](workflows/review.md) | Reviewer | Read RF → checklist → verdict → tech debt → traces |
| [resume.md](workflows/resume.md) | Coordinator | Locate task → status matrix → decide next phase |
| [docs.md](workflows/docs.md) | Coordinator | Update KNOWLEDGE.md and TECH_DEBT.md after task completion |
| [knowledge.md](workflows/knowledge.md) | Coordinator | Consolidate fact candidates into verified project knowledge (Orient → Gather → Consolidate → Prune) |
| [release.md](workflows/release.md) | Coordinator | Read RELEASE.md → scope release → version bump → CHANGELOG → tag |
| [update.md](workflows/update.md) | Coordinator | Fetch upstream → compare versions → categorize changes → update checklist → re-sync adapters |
| [config.md](workflows/config.md) | Coordinator | Interactive config change → propagate to all inline values |

## 9) Tool Adapter Pattern

`.tfw/` is the tool-agnostic core — one copy per project. Each development tool reads its own entry point, which references `.tfw/`:

```
CLAUDE.md ──→ "Read .tfw/README.md, follow .tfw/conventions.md"
.cursor/rules ──→ "Read .tfw/README.md, follow .tfw/conventions.md"
```

Adapters are chosen at project init. See `.tfw/init.md` for setup.

## 10.1) Fact Categories

> Universal categories for Fact Candidates. Open list — agents can use custom categories when none fit.

| Category | Scope | Examples |
|----------|-------|----------|
| `environment` | Where the work lives | servers, tools, platforms, classrooms, labs, hosting |
| `process` | How work gets done | schedules, approvals, reporting cadence, grading rules |
| `stakeholder` | Who is involved | clients, students, reviewers, partners, regulators |
| `constraint` | What limits exist | budgets, deadlines, legal, compliance, technical limits |
| `convention` | Agreed standards | naming, style, format, language, tone |
| `domain` | Subject matter | business rules, scientific models, curriculum, regulations |
| `context` | Background knowledge | history, prior decisions, external factors, market conditions |
| `risk` | Known dangers | fragile dependencies, single points of failure, assumptions |

## 10.2) Knowledge Infrastructure

| File | Purpose |
|------|---------|
| `knowledge/` | Project root folder for topic files (per-category verified facts) |
| `knowledge/{category}.md` | Topic file — verified facts for a category. Template: `.tfw/templates/TOPIC_FILE.md` |
| `.tfw/knowledge_state.yaml` | Consolidation tracking: last seq, date, statistics |
| `.tfw/workflows/knowledge.md` | 4-phase consolidation workflow (Orient → Gather → Consolidate → Prune) |
| `tfw.knowledge` in PROJECT_CONFIG | Configurable limits: interval, gate_mode, max_index_lines, max_facts_per_topic, max_topic_files |

## 10) Context Loading Order (new session, strict)

1. `AGENTS.md`
2. `.tfw/conventions.md`, `.tfw/glossary.md`
3. `KNOWLEDGE.md` (if exists)
4. Relevant HL/TS/RF for the current task

## 11) Quality Standard (no compromises)

- No placeholders.
- Results must be usable without manual edits.
- If a result is wrong — fix the prompt/context and retry until quality is met.
- Tasks are atomic and human-verifiable.

## 12) Safety and Execution Honesty

- In CL mode, never claim something was "run" or "tested" outside the session.
- Never request secrets in plain text. Use environment variables.

## 13) Trace Discipline

Every task produces an **RF file** with results, decisions, and observations. The **Task Board** in README.md tracks all task statuses. Together, these form the project's memory across sessions.

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
- Coordinator writes ONB, RF, or implements code → **Role Lock violation**
- Executor writes HL, TS, or changes scope → **Role Lock violation**
- Executor writes REVIEW file → **Role Lock violation**

## 15) Role Lock Protocol

Each workflow declares a **🔒 ROLE LOCK** at the top. The agent MUST refuse any action outside the locked role.

| Workflow | Role Lock | Permitted Artifacts | Forbidden Artifacts |
|----------|-----------|---------------------|---------------------|
| `init.md` | Coordinator | RES, RF, project config files | HL, TS, code |
| `plan.md` | Coordinator | HL, TS | ONB, RF, RES, REVIEW, code |
| `research.md` | Coordinator | RES | HL, TS, ONB, RF, REVIEW, code |
| `handoff.md` | Executor | ONB, RF | HL, TS, RES, REVIEW, code |
| `review.md` | Reviewer | REVIEW | ONB, RF, HL, TS, code |
| `resume.md` | Coordinator | Status matrix, Phase HL, Phase TS | ONB, RF, RES, REVIEW, code |
| `docs.md` | Coordinator | KNOWLEDGE.md, TECH_DEBT.md | code |
| `release.md` | Coordinator | VERSION, CHANGELOG.md | code |
| `update.md` | Coordinator | `.tfw/` files, adapter copies | code |
| `config.md` | Coordinator | PROJECT_CONFIG.yaml, workflow files, convention files, adapter copies | code |

### Hard Stop Rule

When a Coordinator reaches the end of planning (TS approved), the correct action is:
1. Inform the user that planning is complete
2. Instruct: "Start `/tfw-handoff` to begin execution"
3. **Do NOT continue into execution**

When an Executor finishes RF, the correct action is:
1. Inform the user that execution is complete
2. Instruct: "Start `/tfw-review` to review the results"
3. **Do NOT write a REVIEW file**
