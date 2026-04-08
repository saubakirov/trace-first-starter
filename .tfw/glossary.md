# TFW Glossary

## Execution Modes

### CL (Chat Loop Mode)
Default mode. AI proposes steps, user approves/executes. AI does NOT run external commands without approval. Used for: task planning, code review, architecture decisions, any work touching external systems.

### AG (Autonomous Mode)
AI works independently within the file system. Only for pre-approved scope (e.g., executing an approved TS). Must fail safely if context is missing.

## Artifact Types

> Full definitions, naming rules, and format requirements → [conventions.md](conventions.md) §3

### HL (High Level)
Context/frame artifact for a task — the "map of meaning". → conventions.md §3

### RES (Research Report)
Structured investigation artifact for the RESEARCH stage. Living document: decisions at top, stage logs below. → conventions.md §3

### TS (Task Spec)
Task definition for a single phase. Self-contained: scope, steps, acceptance criteria. → conventions.md §3

### RF (Result File)
Results, decisions, artifacts. RF has priority as source of truth. Contains mandatory Observations table. → conventions.md §3

### ONB (Onboarding Report)
Structured executor report before starting work: understanding, blocking questions, risks, inconsistencies. → conventions.md §3

### REVIEW (Review Report)
Formal coordinator report after reviewing RF: 9-point checklist, verdict (APPROVE/REVISE/REJECT), tech debt triage. → conventions.md §3

### TECH_DEBT.md
Accumulated tech debt registry. Fed by: executor Observations in RF → coordinator triage in REVIEW → append to TECH_DEBT.md.

### KNOWLEDGE.md
Project knowledge index (optional). Central map of architecture, decisions, legacy, and principles. Updated via `tfw-docs` workflow. Principle: index, don't duplicate.

### RELEASE.md
Optional project-level artifact defining release strategy (audience, triggers, version scheme, checklist). Template: `.tfw/templates/RELEASE.md`.

## Knowledge Terms

### Fact Candidate
Raw observation about the project recorded during work in an artifact's Fact Candidates section. NOT a verified fact — becomes a fact after `/tfw-knowledge` consolidation. Quality filter: "Would the next agent decide differently knowing this?" Categories: → conventions.md §10.1

### Strategic Insight
A fact or decision captured during a Coordinator planning session (HL §11). Represents domain knowledge, stakeholder priorities, business context, or architectural vision that only the human stakeholder can provide. High-value signals: user corrections, emotional statements, vision framing, alternative selection.

## Task Naming

Format: `{PREFIX}-{N}__{short-title}`. Full naming rules and file conventions → conventions.md §4

## Status Flow

Full status diagram, transitions, and review verdicts → conventions.md §5

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
```

8 statuses: TODO, HL_DRAFT, RES, TS_DRAFT, ONB, RF, REV, DONE (+ BLOCKED). RES is optional.

## Concept Taxonomy

| Concept | Definition | Where it lives |
|---------|------------|----------------|
| **Document Type** | Type of artifact: HL, RES, TS, ONB, RF, REVIEW | glossary.md (Artifact Types) |
| **Template** | Canonical format for a document type | `.tfw/templates/` |
| **Workflow** | Tool-agnostic process description (plan, research, handoff...) | `.tfw/workflows/` |
| **Adapter Command** | Tool-specific invocation of a workflow (slash-command, skill) | `.claude/commands/`, `.agent/workflows/` |
| **Status** | Process status of a task on the board | `PROJECT_CONFIG.yaml` `tfw.statuses` |

## Roles

### User (Human)
Approves HL and TS before execution. Provides secrets via env vars. Reviews RF outputs. Final authority on task closure.

### Coordinator (AI)
Writes HL and TS. Manages Task Board. Hands off to researcher, executor, and reviewer.

### Researcher (AI)
Dedicated research agent. Writes RES and stage files in `research/` subfolder. Follows OODA loop per stage. Hard Stop: after writing RES, says "Research complete. Continue with `/tfw-plan`."

### Executor (AI)
Reads approved TS. Writes ONB before starting. Implements changes. Makes incremental commits. Writes RF documenting results. Reports observations (tech debt, issues).

### Reviewer (AI — coordinator in review mode)
Reads RF and TS (for DoD verification). Writes REVIEW file with 9-point checklist. Triages executor Observations → TECH_DEBT.md. Cannot: write code, write ONB, write RF, modify HL/TS.

## RESEARCH
Stage between HL and TS in the pipeline. Structured investigation: gathering information, extracting hidden knowledge, critical analysis. Optional — user can skip with confirmation. Can also run standalone via `/tfw-research`. Produces a RES artifact.

## Stage (Research)
One thematic block within RESEARCH: Gather, Extract, or Challenge. Each stage ends with a checkpoint. Stages form a checklist — the agent must cover all three, but the order is flexible.

## Pass (Research)
A full round-trip across all three RESEARCH stages. Minimum 1 pass required. Additional passes cover stages that need deeper investigation (recommended max: 3 passes).

## Read-only AG
A mode within RESEARCH where the agent autonomously reads project files and web sources but writes only to the RES artifact. No code changes, no other file modifications.

## Phase
A bounded unit of work within a multi-phase task. Each phase has its own HL → TS → ONB → RF → REVIEW cycle. Named with letters (A, B, C) or numbers. Subject to scope budgets (→ conventions.md §6).

## Scope Budget
Limits per phase calibrated for AI executor agents. Exceeding limits degrades quality. When exceeded — split the phase. Values → `tfw.scope_budgets` in PROJECT_CONFIG.yaml.

## Topic File
Per-category knowledge file in the `knowledge/` folder. Contains verified facts in a structured table. Template: `.tfw/templates/TOPIC_FILE.md`. Updated by `/tfw-knowledge` consolidation.

## Knowledge Gate
Periodic consolidation checkpoint in Phase 0 of `plan.md`. Mode configurable: `hard` (stop + justification), `soft` (reminder only), `off` (skip). → `tfw.knowledge.gate_mode` in PROJECT_CONFIG.yaml.

## Consolidation
4-phase process for converting Fact Candidates into verified project knowledge: Orient → Gather → Consolidate → Prune. Executed via `/tfw-knowledge` workflow.

## Config Sync Registry
A table in `config.md` workflow mapping `PROJECT_CONFIG.yaml` keys to their inline display locations. AI agent reads the registry to find where values appear, compares with YAML, and proposes updates.

## Tool Adapter
A tool-specific entry point (CLAUDE.md, .cursor/rules, .agent/workflows/) that references `.tfw/` as the single source of truth. → conventions.md §9

## Task Board
Markdown table in `README.md` — single source of truth for task statuses. Updated by every TFW workflow.

## PROJECT_CONFIG.yaml
Per-project configuration file in `.tfw/`. Defines: stack, build commands, task prefix, execution engine, template paths, scope budgets, knowledge settings.

## VERSION
Single-line file in `.tfw/` containing the current framework version in semver format (MAJOR.MINOR.PATCH).

## CHANGELOG.md
Structured version history in `.tfw/`. Follows Keep a Changelog format.

## Compilable Contract
Build-time specification for deterministic compilation of TFW artifacts. → [compilable_contract.md](compilable_contract.md)

## Reference Format
Standard text patterns for cross-artifact citations (e.g., `RF TFW-18`, `D24`, `TD-59`). Build-time resolver converts to hyperlinks. → [compilable_contract.md](compilable_contract.md) §2

## Source Manifest
Ordered list of project files that compilation utilities read. → [compilable_contract.md](compilable_contract.md) §1

---

## Project-Specific Terms

> Remove or replace this section when forking to a new project.

*Add project-specific terminology here.*
