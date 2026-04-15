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
Formal reviewer report after reviewing RF: 4-stage process (Map → Verify → Judge → Decide) with stage files as evidence, verdict (APPROVE/REVISE/REJECT), tech debt triage. Synthesized from `review/map.md`, `review/verify.md`, `review/judge.md`. → conventions.md §3

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
Human-sourced domain knowledge captured with deep analytical synthesis. Appears in three contexts with qualifiers: HL §11 "Strategic Insights (Planning)", RF §7 "Strategic Insights (Execution)", RES "Strategic Insights (Research)". The agent's cognitive mode: capture the insight, then ADD implications — what does it mean for the project? High-value signals: user corrections, emotional statements, vision framing, alternative selection. Contrast with Fact Candidate (pure reporting, no interpretation).

### Value Flow
Visual section in HL template (§3.2). Visualizes HOW value gets created — the process from user pain through pipeline steps to value delivered. Cognitive mode: strategic/value-oriented (INPUT→PROCESSING→OUTCOME). Distinct from §3.1 Result Visualization (outcome preview). → conventions.md §3 Visual Sections

### Findings Map
Visual section in RES template. Visualizes research findings: root cause analysis, hypothesis trees, priority matrices, relationship maps between discoveries. Cognitive mode: analytical/research. → conventions.md §3 Visual Sections

### Per-template Naming
Design principle: when a section's cognitive mode differs across templates, use a different section name per template. When the mode is the same — use a unified name. Applied to: visual sections (per-template: Value Flow, Diagrams, Findings Map) vs knowledge capture sections (unified: Fact Candidates, Strategic Insights). Decision criterion: "Does the cognitive mode CHANGE between templates?" → conventions.md §3 Visual Sections

## Task Naming

Format: `{PREFIX}-{N}__{short-title}`. Full naming rules and file conventions → conventions.md §4

## Status Flow

Full status diagram, transitions, and review verdicts → conventions.md §5

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE
```

9 statuses: TODO, HL_DRAFT, RES, TS_DRAFT, ONB, RF, REV, KNW, DONE (+ BLOCKED). RES and KNW are optional.

### KNW (Knowledge Capture)
Post-review status indicating docs and knowledge workflows have been applied. Triggered after REVIEW ✅ APPROVE. Markers in REVIEW §4: `tfw-docs: Applied/N/A`, `tfw-knowledge: Applied/N/A`. Both markers set → status transitions to ✅ DONE. For trivial tasks, reviewer pre-marks both as N/A during review. → conventions.md §5

## Concept Taxonomy

| Concept | Definition | Where it lives |
|---------|------------|----------------|
| **Document Type** | Type of artifact: HL, RES, TS, ONB, RF, REVIEW | glossary.md (Artifact Types) |
| **Template** | Canonical format for a document type | `.tfw/templates/` |
| **Workflow** | Tool-agnostic process description (plan, research, handoff...) | `.tfw/workflows/` |
| **Adapter Command** | Tool-specific invocation of a workflow (slash-command, skill) | `.claude/commands/`, `.agent/workflows/` |
| **Status** | Process status of a task on the board | `project_config.yaml` `tfw.statuses` |

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
Reads RF and TS (for DoD verification). Creates review stage files (map.md, verify.md, judge.md) then synthesizes into REVIEW file with mode-aware checklist (6 universal + mode-specific items). Triages executor Observations → TECH_DEBT.md. Cannot: write code, write ONB, write RF, modify HL/TS.

## RESEARCH
Stage between HL and TS in the pipeline. Structured investigation: gathering information, extracting hidden knowledge, critical analysis. Produces recommendations in pros/cons format for coordinator decision. Can also run standalone via `/tfw-research`. Produces a RES artifact.

## Stage (Research)
One thematic block within RESEARCH: Gather, Extract, or Challenge. Each stage ends with a checkpoint. Stages form a checklist — the agent must cover all three, but the order is flexible.

## Pass (Research)
A full round-trip across all three RESEARCH stages. Each stage runs an OODA loop with a sufficiency verdict at the end. Minimum 1 pass required. Additional passes cover stages that need deeper investigation (recommended max: 3 passes).

## Iteration (Research)
One full round of `/tfw-research` within a multi-iteration task. Each iteration has its own subfolder (`researchN/`), its own RES file (`RES__iterN__*.md`), and a mandatory Iteration Status block. Iteration 1 = standard research. Iteration 2+ = builds on predecessor findings, addresses open threads and gaps. Minimum iterations configurable via `tfw.research.min_iterations` in project_config.yaml (default: 2). → conventions.md §4 Research subfolder

## iterations.yaml
Control file at task root for multi-iteration research. Created by coordinator in `plan.md` Step 6b. Contains: `task_id`, `title`, `min_iterations`, `max_iterations`, and an `iterations` array tracking each iteration's number, focus, hypotheses, status, and RES file path. Coordinator owns this file — researchers read it, coordinator updates it. → conventions.md §4 Research subfolder

## min_iterations
Configurable hard floor for research iterations. Default: 2 (from `tfw.research.min_iterations` in project_config.yaml). Coordinator gate in `plan.md` Step 6c blocks TS until this many iterations complete. Coordinator can override per task in `iterations.yaml`. Rationale: researchers optimize for speed, structural enforcement ensures minimum depth. → plan.md Step 6c

## Read-only AG
A mode within RESEARCH where the agent autonomously reads project files and web sources but writes only to the RES artifact. No code changes, no other file modifications.

## Phase
A bounded unit of work within a multi-phase task. Each phase has its own HL → TS → ONB → RF → REVIEW cycle. Named with letters (A, B, C) or numbers. Subject to scope budgets (→ conventions.md §6).

## Multi-phase Handoff
Convention for tasks with 3+ phases: master HL §4 includes a Context block per phase (Requires, Shared files, Key decisions, Deliverables) enabling independent coordinators to write Phase HL without reading all research. → `templates/HL.md` §4, `plan.md` Step 7.

## Scope Budget
Limits per phase calibrated for AI executor agents. Exceeding limits degrades quality. When exceeded — split the phase. Values → `tfw.scope_budgets` in project_config.yaml.

## Topic File
Per-category knowledge file in the `knowledge/` folder. Contains verified facts in a structured table. Template: `.tfw/templates/topic_file.md`. Updated by `/tfw-knowledge` consolidation.

## Knowledge Gate
Periodic consolidation checkpoint in Phase 0 of `plan.md`. Mode configurable: `hard` (stop + justification), `soft` (reminder only), `off` (skip). → `tfw.knowledge.gate_mode` in project_config.yaml.

## Consolidation
4-phase process for converting Fact Candidates into verified project knowledge: Orient → Gather → Consolidate → Prune. Executed via `/tfw-knowledge` workflow.

## Project Values (PV)
The complete set of accumulated project context that MUST inform decisions. When someone says "check values", "check against experience", or "verify alignment" — scan the PV Index. Project Values include beliefs, validated principles, architecture decisions, agreed standards, and known anti-patterns. Not just moral values — everything that has VALUE for making decisions.

### PV Index (scan order)

| Priority | Source | What it contains |
|----------|--------|-----------------|
| 1 | README Values | Core beliefs (e.g., Traces Over Code, Structural Enforcement) |
| 2 | `knowledge/philosophy.md` | Validated principles and design rationale |
| 3 | `KNOWLEDGE.md` §1 | Architecture Decisions (D-records) |
| 4 | `conventions.md` §3, §11, §14 | Naming rules, Design rules, Anti-patterns |
| 5 | `knowledge/convention.md` | Agreed standards and patterns |
| 6 | `knowledge/process.md` | Process facts and workflow patterns |
| 7 | Other `knowledge/*.md` | Domain, constraint, stakeholder, environment facts |

**Who scans PV:**
- **Coordinator** — full scan during planning. Output: HL §7.2 Knowledge Citations table.
- **Reviewer** — full scan during verification. Output: verify.md Knowledge Citations Verified section.
- **Executor** — reads coordinator's citations from HL §7.2. Output: ONB §7 confirming read + any new items found.
- **Researcher** — reads HL §7.2 citations. Cross-references in RES Fact Candidates.

## Config Sync Registry
A table in `config.md` workflow mapping `project_config.yaml` keys to their inline display locations. AI agent reads the registry to find where values appear, compares with YAML, and proposes updates.

## Tool Adapter
A tool-specific entry point (CLAUDE.md, .cursor/rules, .agent/workflows/) that references `.tfw/` as the single source of truth. → conventions.md §9

## Task Board
Markdown table in `README.md` — single source of truth for task statuses. Updated by every TFW workflow.

## project_config.yaml
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
