# TFW Changelog

All notable changes to the Trace-First Workflow framework.
Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [Semantic Versioning](https://semver.org/).

## [Unreleased]

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
