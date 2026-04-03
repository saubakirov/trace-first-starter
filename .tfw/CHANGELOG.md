# TFW Changelog

All notable changes to the Trace-First Workflow framework.
Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.6.1] — 2026-04-03
### Added
- Chat history scan instruction in `handoff.md`, `research.md`, `review.md` — agents MUST review conversation history before writing Fact Candidates. Human messages are the primary source of project knowledge (TFW-18 post-release finding)
### Changed
- All 3 adapter copies synced (`tfw-handoff`, `tfw-research`, `tfw-review`)

## [0.6.0] — 2026-04-03
### Added
- `/tfw-knowledge` workflow — 4-phase consolidation (Orient → Gather → Consolidate → Prune) with role lock, behavior rules, anti-patterns (TFW-18)
- `TOPIC_FILE.md` template — per-category knowledge files in `knowledge/` folder (TFW-18)
- `.tfw/knowledge_state.yaml` — consolidation state tracking (seq, date, stats) (TFW-18)
- `tfw.knowledge` section in `PROJECT_CONFIG.yaml` — 6 configurable parameters: interval, gate_mode, max_index_lines, max_index_facts_lines, max_facts_per_topic, max_topic_files (TFW-18)
- §6 Fact Candidates in `RF.md` template — mandatory section with quality filter and anti-patterns (TFW-18)
- §5 Fact Candidates in `REVIEW.md` template — mandatory section with quality filter (TFW-18)
- Fact Candidates in `RES.md` template Closure section (TFW-18)
- Phase 0: Knowledge Gate Check in `plan.md` — configurable (hard/soft/off) enforcement before Phase 1 (TFW-18)
- 💡 Mindset reminders in `handoff.md`, `research.md`, `review.md` — capture project facts (TFW-18)
- §5 Project Facts compact index in `KNOWLEDGE.md` template — category/count/link table (TFW-18)
- Item 6 in `docs.md` checklist — Fact Candidates marker (TFW-18)
- §10.1 Fact Categories and §10.2 Knowledge Infrastructure in `conventions.md` (TFW-18)
- 4 glossary terms: Fact Candidate, Topic File, Knowledge Gate, Consolidation (TFW-18)
- D22 in `KNOWLEDGE.md` — knowledge consolidation decision (TFW-18)
- `/tfw-knowledge` Antigravity adapter (TFW-18)
- `.user_preferences.md` guidance in `init.md` Step 5 (TFW-18)
### Changed
- All 5 existing adapter copies synced with canonical workflows (TFW-18)

## [0.5.5] — 2026-04-03
### Added
- Coordinator Mindset section in `plan.md` — quality of planning > speed of pipeline, anti-rush guidance, RESEARCH as default (TFW-17)
- Hard Rule #8 in `research.md` — every stage MUST include at least one external action (web search, URL read, docs) (TFW-17)
- Stage-level mindset reminders in `research.md` — 1-line blockquote at the start of Gather, Extract, Challenge (TFW-17)
- Depth self-check in `research.md` checkpoint template — "Did I use external sources, or only project files?" (TFW-17)
- External research bullet in Sufficiency Check — "Did every stage include external research?" (TFW-17)
- D21 in `KNOWLEDGE.md` — dual-lever fix for coordinator rush-bias + research depth (TFW-17)
- P9 in `KNOWLEDGE.md` — Coordinator Mindset principle (TFW-17)
### Changed
- `plan.md` Phase 1 — "Understand the problem" → "Understand the problem deeply" with anti-rush guidance (TFW-17)
- `plan.md` RESEARCH Gate — coordinator must be specific about what RESEARCH could reveal, frame as risk reduction (TFW-17)
- `research.md` Gather stage — "Autonomous search" replaced with "**Search externally**: how is this problem solved elsewhere?" (TFW-17)
- P8 in `KNOWLEDGE.md` — updated to include external tool mandate reference (TFW-17)
- All 4 adapter copies synced — `.agent/workflows/tfw-plan.md`, `.agent/workflows/tfw-research.md`, `.claude/commands/tfw-plan.md`, `.claude/commands/tfw-research.md` (TFW-17)
### Fixed
- TD-34: `research.md` L26 no longer references TS as primary output (confirmed resolved by TFW-14, verified TFW-17)
- Adapter desync: `.agent/workflows/tfw-plan.md` and `.claude/commands/tfw-plan.md` had stale `🔵 HL` statuses, `Phase 3.5` numbering, old pipeline diagram — all fixed via full copy from canonical

## [0.5.4] — 2026-04-01
### Added
- `tfw.statuses` registry in `PROJECT_CONFIG.yaml` — 9 status entries with `role` field (TFW-15)
- Concept Taxonomy in `glossary.md` — 5 formal definitions: Document Type, Template, Workflow, Adapter Command, Status (TFW-15)
- REJECT branching in `conventions.md` — user decides: HL_DRAFT / RES / TS_DRAFT (TFW-15)
- D20 in `KNOWLEDGE.md` — pipeline status decoupling decision (TFW-15)
### Changed
- **BREAKING:** Pipeline statuses renamed: `🔵 HL` → `📝 HL_DRAFT`, `🟡 TS` → `🟡 TS_DRAFT` across all `.tfw/` files (TFW-15)
- **BREAKING:** HL template status label: `🔵 HL — Ожидает ревью` → `📝 HL_DRAFT — Ожидает ревью` (TFW-15)
- **BREAKING:** TS template status label: `🟡 TS — Ожидает апрува` → `🟡 TS_DRAFT — Ожидает апрува` (TFW-15)
- `plan.md` — Phase 3.5 → Phase 4 (RESEARCH Gate), Phase 4 → Phase 5 (Decide Scope & Write TS), step numbering gap fixed (TFW-15)
- `research.md` — Status Transitions section updated to HL_DRAFT/TS_DRAFT (TFW-15)
- `conventions.md` — status table, pipeline diagram, REJECT verdict updated (TFW-15)
- `glossary.md` — Status Flow diagram updated (TFW-15)
- `.tfw/README.md` — Task Lifecycle pipeline diagram and REJECT wording updated (TFW-15)
### Deprecated
- `🔵 HL` and `🟡 TS` status names — replaced by `📝 HL_DRAFT` and `🟡 TS_DRAFT`
- `Phase 3.5` numbering in plan.md — replaced by clean Phase 4/5 numbering

## [0.5.3] — 2026-04-01
### Added
- Briefing Protocol in `research.md` — mandatory entry with research plan, scope intent, guiding questions before stages (TFW-14)
- Closure Protocol in `research.md` — mandatory exit with HL update recommendations after sufficiency check (TFW-14)
- Briefing and Closure sections in `RES.md` template — structural anchors for agent behavior (TFW-14)
- 3 new Hard Rules in `research.md` — briefing mandatory, closure mandatory, sufficiency check with specifics (TFW-14)
- 4 new Anti-patterns — skip-briefing, rush-bias, silent closure, skip-bias (TFW-14)
- HL update gate in `plan.md` Phase 3.5 — coordinator reads RES → updates HL → user confirms → TS (TFW-14)
- D19 in `KNOWLEDGE.md` — HL update = mandatory RESEARCH output (TFW-14)
### Changed
- Checkpoint in `research.md` — extended with Stage Handoff (plan for next stage + question) (TFW-14)
- Final Checkpoint — Complexity Check replaced by Sufficiency Check ("sufficient for HL finalization?") (TFW-14)
- Turn-based rhythm — questions limit changed from "per stage" to "per turn" (≤3) across research.md, Limits table, Hard Rules, Anti-patterns (TFW-14)
- `plan.md` Phase 3.5 — skip-bias fix: pros/cons format, default=recommend research, user decides (TFW-14)
- Both adapters (`.claude/commands/tfw-research.md`, `.agent/workflows/tfw-research.md`) — synced with Briefing→Stages→Closure structure (TFW-14)
- Research Mindset L26 — reworded from "details needed for TS" to "refines the HL" (TFW-14 REVISE)
### Fixed
- TD-34: `research.md` L26 referenced TS as primary output after Closure Protocol addition — now references HL

## [0.5.2] — 2026-03-31
### Added
- `init.md` workflow — AI-first project initialization (Discover → Interview → Knowledge → Setup → Verify) (TFW-13)
- `/tfw-init` slash command (Claude Code + Antigravity) (TFW-13)
- `.tfw/adapters/README.md` — adapter index + "How to Write a New Adapter" (moved from old init.md) (TFW-13)
- `docs.md`, `release.md`, `update.md` in conventions §15 Role Lock table (consistency fix)
- `research.md` in conventions §8 Workflows table (consistency fix)
- `VERSION`, `CHANGELOG.md` in conventions §2 Required Artifacts (consistency fix)
### Changed
- `.tfw/init.md` — replaced 232-line manual guide with 20-line pointer to workflow (TFW-13)
- Antigravity README — all 9 workflows in copy/sync instructions (was 5) (consistency fix, TD-27)
- `plan.md` Role Lock — removed REVIEW from permitted artifacts (was inconsistent with §15 table)
- conventions §2 — all 9 workflows now listed (was 5)
- conventions §8 — reordered: init first, added research
### Fixed
- TD-27: Antigravity README missing 4 workflows in copy commands
- TD-29: conventions §2 missing review, docs, release, update workflows + VERSION, CHANGELOG
- TD-30: conventions §8 missing research.md
- TD-31: conventions §15 missing docs, release, update in Role Lock
- TD-32: Antigravity README copy/sync missing research, docs, release, update
- plan.md declared "Permitted: HL, TS, REVIEW" but §15 table said "HL, TS" — fixed to match table

## [0.5.1] — 2026-03-30
### Added
- `tfw.scope_budgets` section in `PROJECT_CONFIG.yaml` — 4 configurable budget values (TFW-12)
- `tfw.workflows` section in `PROJECT_CONFIG.yaml` — 8 workflow entries (TFW-12)
- `tfw.research` section in `PROJECT_CONFIG.yaml` — 4 research limit entries (TFW-12)
- Config component row in `KNOWLEDGE.md` Architecture Map (TFW-12)
### Changed
- `tfw.templates` in `PROJECT_CONFIG.yaml` — completed to 8 entries (+res, +knowledge, +release) (TFW-12)
- Scope budget values removed from docs — pure reference to `tfw.scope_budgets` config (TFW-12, Pattern B)
- Version strings removed from core file titles (conventions.md, glossary.md) — avoids drift on bump (TFW-12)
- Adapter templates use `{version}` placeholder instead of hardcoded version (TFW-12)
- `CLAUDE.md`, `.agent/rules/tfw.md` — version and template/workflow references centralized (TFW-12)
- `init.md` — full config example with all 4 sections, `{version}` replacement instructions (TFW-12)
### Fixed
- `CHANGELOG.md` — restored missing `[0.4.2]` section header
- TD-25: conventions.md/glossary.md title headers fixed (no more stale version)
- TD-26: `.agent/rules/tfw.md` — added version reference and RES template

## [0.5.0] — 2026-03-30
### Added
- RESEARCH stage — optional structured investigation between HL and TS (TFW-11)
- `RES.md` template — Research Report artifact
- `research.md` workflow — standalone and pipeline research
- Phase 3.5 RESEARCH gate in `plan.md`
- 🔬 RES status — pipeline now 8-status (RES optional)
- `Read-only AG` mode definition in glossary
- RES in Role Lock Protocol (conventions §15)
- Claude Code adapter: `CLAUDE.md`, 9 slash commands in `.claude/commands/`
- Claude Code adapter: `README.md` setup guide
- `/tfw-research` slash command (Claude Code + Antigravity)
- `/tfw-review` slash command (Claude Code)
- `/tfw-release` slash command (Claude Code)
- `/tfw-update` slash command (Claude Code)
### Changed
- Pipeline diagrams updated in all core files (8-status, RES optional)
- Coordinator role updated: conducts RESEARCH, writes RES files
- All 3 adapter templates updated (RES, full workflow/command lists)
- `CLAUDE.md.template` expanded with slash command table and full context loading
- Antigravity adapter copies synced (plan, research, handoff)
- init.md — RES template in config, research.md in workflow copy commands
- .tfw/README.md — project structure tree updated

## [0.4.2] — 2026-03-12
### Added
- `tfw.upstream` field in `PROJECT_CONFIG.yaml` — configurable source URL for `tfw-update` (TFW-9)
- Step 0 (Fetch Upstream) and Step 9 (Cleanup) in `update.md` — concrete fetch mechanism with cross-platform commands (TFW-9)
- `.tfw/.upstream/` staging directory pattern — OS-independent, gitignored (TFW-9)
### Changed
- `update.md` — all vague "upstream" references replaced with concrete `.tfw/.upstream/.tfw/` paths (TFW-9)
- `conventions.md` §8, `.tfw/README.md` — update workflow description includes "Fetch upstream" step (TD-17, TD-18)
- `init.md` — `tfw.upstream` in config example, `.tfw/.upstream/` gitignore note (TFW-9)
- `glossary.md` — `tfw-update` entry expanded with source resolution details (TFW-9)

## [0.4.1] — 2026-03-12
### Added
- `review.md` workflow — standalone review process with `🔒 ROLE LOCK: REVIEWER` (TFW-8)
- Reviewer role — coordinator in review-locked mode (glossary, conventions) (TFW-8)
- Executor Hard Stop Rule in conventions §15 (TFW-8)
### Changed
- `handoff.md` — removed Phase 4 (review), added executor STOP block (TFW-8)
- `conventions.md` — Role Lock table updated, "any role" for REVIEW removed, review.md row added (TFW-8)
- `glossary.md` — Coordinator role updated (review duties moved to Reviewer) (TFW-8)
- `AGENTS.md` — workflow list updated with review.md (TFW-8)
- `README.md` (`.tfw/`) — workflows table, roles section, evolution updated (TFW-8)
- `plan.md`, `resume.md` — review workflow references added (TFW-8)
- `init.md`, adapter README — review workflow in setup instructions (TFW-8)
### Removed
- Review phase from `handoff.md` — moved to standalone `review.md` (TFW-8)
- "REVIEW files can be written by any role" from conventions §15 (TFW-8)
### Fixed
- `conventions.md` §8 — `docs.md` workflow now listed in Workflows table (TFW-7)
- `.tfw/README.md` — workflow count corrected, docs workflow included (TFW-7)
- Cross-references between conventions, glossary, and README aligned (TFW-7)


## [0.4.0] — 2026-03-12
### Added
- `VERSION` file — machine-readable framework version
- `CHANGELOG.md` — version history (this file)
- `RELEASE.md` template — optional release context artifact
- `tfw-release` workflow — canonical release process
- `tfw-update` workflow — structured upgrade process for downstream projects
### Changed
- `PROJECT_CONFIG.yaml` — added `tfw.version` field
- `init.md` — added version tracking and RELEASE.md guidance

## [0.3.0] — 2026-03-02
### Added
- `KNOWLEDGE.md` template and tfw-docs workflow (TFW-5)
### Changed
- Framework cleanup: removed STEPS.md, TASK.md, Summary Discipline (TFW-4)
- Root README restructured for public readership (TFW-3)

## [0.2.0] — 2026-02-25
### Added
- `.tfw/` directory — tool-agnostic core (conventions, templates, workflows, adapters)
- ONB and REVIEW artifact types
- 7-status lifecycle with quality gates
- 3 canonical workflows (plan, handoff, resume)
- Scope budgets per phase
- TECH_DEBT.md pipeline
- Tool adapter pattern (Claude Code, Cursor, Antigravity)
- PROJECT_CONFIG.yaml
- Anti-patterns list
### Removed
- `AI_ENTRY_POINT.md`, `SUCCESS_CRITERIA.md`, `00_meta/` directory

## [0.1.0] — 2024
### Added
- Core concept: traces are more valuable than code
- 4-file structure (AGENTS, README, TASK, STEPS)
- Summary Discipline
- Chat→project conversion pattern
- CL/AG execution modes (informal)
