# TFW Glossary

## Execution Modes

### CL (Chat Loop Mode)
Default mode. AI proposes steps, user approves/executes. AI does NOT run external commands without approval. Used for: task planning, code review, architecture decisions, any work touching external systems.

### AG (Autonomous Mode)
AI works independently within the file system. Only for pre-approved scope (e.g., executing an approved TS). Must fail safely if context is missing.

## Artifact Types

> Canonical rules → [conventions.md](conventions.md). Philosophy → [README.md](README.md).

### HL (High Level)
Context, research, background, requirements. Not a task — a "map of meaning". Format: strictly follows `.tfw/templates/HL.md`. Contains: Vision, As-Is, To-Be, Phases, DoD, DoF, Principles, Dependencies, Risks.

### RES (Research Report)
Structured investigation artifact for the RESEARCH stage. Living document: decisions and open questions at the top, stage logs (Gather, Extract, Challenge) below. Created between HL and TS (pipeline mode) or standalone for any research topic. Format: strictly follows `.tfw/templates/RES.md`.

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
- Files inside: `HL-{PREFIX}-{N}__*.md`, `RES__{PREFIX}-{N}__*.md`, `TS__Phase{X}__*.md`, `RF__Phase{X}__*.md`, `ONB__Phase{X}__*.md`, `REVIEW__Phase{X}__*.md`

## Status Flow

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
                          (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)        ↓
                                                          ❌ BLOCKED
```

8 statuses: TODO, HL_DRAFT, RES, TS_DRAFT, ONB, RF, REV, DONE (+ BLOCKED). RES is optional — user can skip directly from HL_DRAFT to TS_DRAFT.

## Concept Taxonomy

| Concept | Definition | Where it lives |
|---------|------------|----------------|
| **Document Type** | Type of artifact: HL, RES, TS, ONB, RF, REVIEW | glossary.md (Artifact Types) |
| **Template** | Canonical format for a document type | `.tfw/templates/` |
| **Workflow** | Tool-agnostic process description (plan, research, handoff...) | `.tfw/workflows/` |
| **Adapter Command** | Tool-specific invocation of a workflow (slash-command, skill) | `.claude/commands/`, `.agent/workflows/` |
| **Status** | Process status of a task on the board | `PROJECT_CONFIG.yaml` `tfw.statuses` |

## RESEARCH
Stage between HL and TS in the pipeline. Structured investigation: gathering information, extracting hidden knowledge, critical analysis. Optional — user can skip with confirmation. Can also run standalone (any topic, any time) via `/tfw-research`. Produces a RES artifact.

## Stage (Research)
One thematic block within RESEARCH: Gather, Extract, or Challenge. Each stage ends with a checkpoint. Stages form a checklist — the agent must cover all three, but the order is flexible.

## Pass (Research)
A full round-trip across all three RESEARCH stages. Minimum 1 pass required. Additional passes cover stages that need deeper investigation (recommended max: 3 passes).

## Phase
A bounded unit of work within a multi-phase task. Each phase has its own HL → TS → ONB → RF → REVIEW cycle. Named with letters (A, B, C) or numbers. Subject to scope budgets (see `tfw.scope_budgets` in `.tfw/PROJECT_CONFIG.yaml`).

## Scope Budget
Limits per phase calibrated for AI executor agents. Exceeding limits degrades quality. When exceeded — split the phase.

## Workflow (canonical)
A tool-agnostic process description in `.tfw/workflows/`. Defines **what** to do, not **how**. Canonical workflows in `.tfw/workflows/`: plan (HL→RES→TS), research (structured investigation), handoff (ONB→execute→RF), review (RF→checklist→REVIEW), resume (status matrix→next phase). Each tool maps workflows to its own format (skills, commands, rules).

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
- Conducts RESEARCH and writes RES files
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

## Read-only AG
A mode within RESEARCH where the agent autonomously reads project files and web sources but writes only to the RES artifact. No code changes, no other file modifications. Formally CL with expanded read permissions.

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

## Fact Candidate
Raw observation about the project recorded during work in an artifact's Fact Candidates section. NOT a verified fact — becomes a fact after `/tfw-knowledge` consolidation. Quality filter: "Would the next agent decide differently knowing this?" Categories: `environment`, `process`, `stakeholder`, `constraint`, `convention`, `domain`, `context`, `risk` (open list).

## Topic File
Per-category knowledge file in the `knowledge/` folder (project root). Contains verified facts in a structured table. Template: `.tfw/templates/TOPIC_FILE.md`. Updated by `/tfw-knowledge` consolidation. Subject to `max_facts_per_topic` limit from `tfw.knowledge` in PROJECT_CONFIG.yaml.

## Knowledge Gate
Periodic consolidation checkpoint in Phase 0 of `plan.md`. Checks `(current_seq - last_consolidation_seq) >= interval`. Mode configurable: `hard` (stop + justification required), `soft` (reminder only), `off` (skip silently). Configured via `tfw.knowledge.gate_mode` in PROJECT_CONFIG.yaml.

## Consolidation
4-phase process for converting Fact Candidates into verified project knowledge: Orient (understand current state) → Gather (scan artifacts since last consolidation) → Consolidate (deduplicate, verify, resolve contradictions, write to topic files) → Prune (remove stale facts, check limits, update index). Executed via `/tfw-knowledge` workflow.

## Config Sync Registry
A table in `config.md` workflow that maps `PROJECT_CONFIG.yaml` keys to their inline display locations in workflows and conventions. AI agent reads the registry to find where values appear, compares with YAML, and proposes updates. Ensures single source of truth (YAML) with inline visibility (rendered defaults).

## RELEASE.md
Optional project-level artifact defining release strategy (audience, triggers, version scheme, checklist). Template: `.tfw/templates/RELEASE.md`. Referenced by `tfw-release` workflow for project-specific context. Analogous to KNOWLEDGE.md — optional, but valuable for projects with versioned outputs.

## tfw-init (Workflow)
Canonical initialization workflow for bootstrapping TFW in a new project. AI agent discovers project, interviews user, runs /tfw-research for knowledge gathering, creates all TFW files, registers itself as {PREFIX}-1 on Task Board. One-time use. Lives in `.tfw/workflows/init.md`.

## tfw-release (Workflow)
Canonical release workflow for cutting a new version. Reads RELEASE.md for project context, scopes changes, bumps version, updates CHANGELOG. Lives in `.tfw/workflows/release.md`.

## tfw-update (Workflow)
Canonical update workflow for upgrading a project's `.tfw/` from upstream starter. Reads `tfw.upstream` from `PROJECT_CONFIG.yaml` for source resolution, clones upstream into `.tfw/.upstream/` staging directory, compares versions, categorizes changes (🟢 safe / 🟡 merge / 🔴 breaking), generates update checklist, re-syncs adapter copies. Lives in `.tfw/workflows/update.md`.

---

## Project-Specific Terms

> Remove or replace this section when forking to a new project.

*Add project-specific terminology here.*
