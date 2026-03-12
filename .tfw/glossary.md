# TFW v3 Glossary

## Execution Modes

### CL (Chat Loop Mode)
Default mode. AI proposes steps, user approves/executes. AI does NOT run external commands without approval. Used for: task planning, code review, architecture decisions, any work touching external systems.

### AG (Autonomous Mode)
AI works independently within the file system. Only for pre-approved scope (e.g., executing an approved TS). Must fail safely if context is missing.

## Artifact Types

> Canonical rules → [conventions.md](conventions.md). Philosophy → [README.md](README.md).

### HL (High Level)
Context, research, background, requirements. Not a task — a "map of meaning". Format: strictly follows `.tfw/templates/HL.md`. Contains: Vision, As-Is, To-Be, Phases, DoD, DoF, Principles, Dependencies, Risks.

### TS (Task Spec)
Task definition for a single phase. Self-contained: scope, steps, acceptance criteria. Format: strictly follows `.tfw/templates/TS.md`. Includes scope budget check.

### RF (Result File)
Results, decisions, artifacts, data. RF has priority as source of truth. Contains mandatory Observations table (structured, typed). Format: strictly follows `.tfw/templates/RF.md`.

### ONB (Onboarding Report)
Structured executor report before starting work. Contains: understanding, blocking questions, recommendations, risks, inconsistencies. Coordinator/human answers directly in the file. Format: strictly follows `.tfw/templates/ONB.md`.

### REVIEW (Review Report)
Formal coordinator report after reviewing RF. Contains: 9-point checklist, verdict (APPROVE/REVISE/REJECT), tech debt collection from observations. Format: strictly follows `.tfw/templates/REVIEW.md`.

### TECH_DEBT.md
Accumulated tech debt registry. Fed by: executor Observations in RF → coordinator triage in REVIEW → append to TECH_DEBT.md. Tracks: source phase, severity, file, description, action.

### KNOWLEDGE.md
Project knowledge index (optional). Central map of architecture, decisions, legacy, and principles. Updated via `tfw-docs` workflow after each REVIEW. Principle: index, don't duplicate — links to RF/HL files, never copies. Template: `.tfw/templates/KNOWLEDGE.md`.

## Task Naming
Format: `{PREFIX}-{N}__{short-title}`
- `{PREFIX}` — project prefix from `.tfw/PROJECT_CONFIG.yaml` (e.g., `PROJ`)
- `{N}` — sequential task number
- Files inside: `HL-{PREFIX}-{N}__*.md`, `TS__Phase{X}__*.md`, `RF__Phase{X}__*.md`, `ONB__Phase{X}__*.md`, `REVIEW__Phase{X}__*.md`

## Status Flow

```
⬜ TODO → 🔵 HL → 🟡 TS → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
                                                              │
                                                    ┌─────────┴─────────┐
                                                    🔄 REVISE          ❌ REJECT
                                                 (back to dev)    (new HL/TS)
                     ↓
                ❌ BLOCKED
```

7 statuses: TODO, HL, TS, ONB, RF, REV, DONE (+ BLOCKED).

## Phase
A bounded unit of work within a multi-phase task. Each phase has its own HL → TS → ONB → RF → REVIEW cycle. Named with letters (A, B, C) or numbers. Subject to scope budgets (≤7 files, ≤600 LOC, ≤4 new files per phase).

## Scope Budget
Limits per phase calibrated for AI executor agents. Exceeding limits degrades quality. When exceeded — split the phase.

## Workflow (canonical)
A tool-agnostic process description in `.tfw/workflows/`. Defines **what** to do, not **how**. Canonical workflows in `.tfw/workflows/`: plan (HL→TS), handoff (ONB→execute→RF), review (RF→checklist→REVIEW), resume (status matrix→next phase). Each tool maps workflows to its own format (skills, commands, rules).

## `.tfw/` Directory
Tool-agnostic TFW core. Contains: README.md (philosophy), conventions.md, glossary.md, templates/, workflows/, PROJECT_CONFIG.yaml. One copy per project, referenced by tool-specific adapters.

## Tool Adapter
A tool-specific entry point (CLAUDE.md, .cursor/rules, .agent/workflows/) that references `.tfw/` as the single source of truth. Adapters translate canonical workflows into tool-native format.

## Roles

### User (Human)
- Approves HL and TS before execution
- Provides secrets (tokens, API keys) via env vars
- Reviews RF outputs
- Final authority on task closure

### Coordinator (AI)
- Writes HL and TS
- Manages Task Board in README
- Hands off to executor for implementation
- Hands off to reviewer for review

### Executor (AI)
- Reads approved TS
- Writes ONB before starting
- Implements code/changes
- Makes incremental commits
- Writes RF documenting results
- Reports observations (tech debt, issues)

### Reviewer (AI — coordinator in review mode)
- Reads RF and TS (for DoD verification)
- Writes REVIEW file with 9-point checklist
- Triages executor Observations → TECH_DEBT.md
- Updates Task Board status
- Cannot: write code, write ONB, write RF, modify HL/TS

## Execution Engine
The tool or process that executes TS steps. Defined in `.tfw/PROJECT_CONFIG.yaml` under `coding.engine`. Examples: IDE-native, CLI agent, hybrid. Each project configures its own engine.

## Progress Reporting
Mechanism for monitoring long-running tasks. Implementation is tool-specific (heartbeat, polling, webhooks). Configured per-project.

## Task Board
Markdown table in `README.md` — single source of truth for task statuses. Updated by every TFW workflow/skill. Includes columns for all artifact types (HL, TS, ONB, RF, REV).

## PROJECT_CONFIG.yaml
Per-project configuration file in `.tfw/`. Defines: stack, build commands, task prefix, execution engine, template paths. Used by workflows and tools to parametrize behavior.

## VERSION
Single-line file in `.tfw/` containing the current framework version in semver format (MAJOR.MINOR.PATCH). Machine-readable. Updated by `tfw-release` workflow.

## CHANGELOG.md
Structured version history in `.tfw/`. Follows Keep a Changelog format. Each version entry lists Added, Changed, Deprecated, Removed, Fixed items. Updated by `tfw-release` workflow.

## RELEASE.md
Optional project-level artifact defining release strategy (audience, triggers, version scheme, checklist). Template: `.tfw/templates/RELEASE.md`. Referenced by `tfw-release` workflow for project-specific context. Analogous to KNOWLEDGE.md — optional, but valuable for projects with versioned outputs.

## tfw-release (Workflow)
Canonical release workflow for cutting a new version. Reads RELEASE.md for project context, scopes changes, bumps version, updates CHANGELOG. Lives in `.tfw/workflows/release.md`.

## tfw-update (Workflow)
Canonical update workflow for upgrading a project's `.tfw/` from upstream starter. Reads `tfw.upstream` from `PROJECT_CONFIG.yaml` for source resolution, clones upstream into `.tfw/.upstream/` staging directory, compares versions, categorizes changes (🟢 safe / 🟡 merge / 🔴 breaking), generates update checklist, re-syncs adapter copies. Lives in `.tfw/workflows/update.md`.

---

## Project-Specific Terms

> Remove or replace this section when forking to a new project.

*Add project-specific terminology here.*
