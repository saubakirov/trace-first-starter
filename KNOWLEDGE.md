# KNOWLEDGE.md — Trace-First Starter Knowledge Index

> Central index of project architecture, decisions, and evolution.
> **Principle**: Index, don't duplicate — link to RF/HL files, don't copy their contents.

---

## 0. Philosophy & Principles

| # | Principle | Source |
|---|-----------|--------|
| P1 | Traces over code — intent, decisions, constraints matter more than implementation | `.tfw/README.md` §Thesis |
| P2 | Index, don't duplicate — link to sources, don't copy | TFW-5 HL §7 |
| P3 | Philosophy stays rich — if DRY conflicts with narrative value, narrative wins | TFW-4 HL §7.1 |
| P4 | Glossary = dictionary, Conventions = rules — same term, different angles, not duplication | TFW-4 discussion |
| P5 | Meta-project awareness — this repo describes TFW AND uses TFW, overlap is by design | TFW-4 HL §7.3 |
| P6 | Lightweight docs — tfw-docs = 5-item checklist, not bureaucracy | TFW-5 HL §7.3 |
| P7 | Self-review is not review — execution and review must be separate role-locked acts | TFW-8 HL §7 |
| P8 | RESEARCH ≠ passive checklist — agent MUST ask pointed questions at every stage, contribute own observations before asking, and WAIT for user response. Running stages silently is a protocol violation. See Research Mindset in `.tfw/workflows/research.md` | TFW-11 HL §7, TFW-11 post-launch fix |

---

## 1. Architecture Map

### Framework Structure

| Component | Description | Key Files |
|-----------|-------------|-----------|
| TFW Core | Tool-agnostic framework spec | `.tfw/README.md`, `.tfw/conventions.md`, `.tfw/glossary.md` |
| Templates | Canonical artifact templates | `.tfw/templates/` (HL, TS, RES, RF, ONB, REVIEW, KNOWLEDGE, RELEASE) |
| Workflows | Task lifecycle workflows | `.tfw/workflows/` (init, plan, research, handoff, review, resume, docs, release, update) |
| Adapters | Tool-specific bridges | `.tfw/adapters/` (claude-code, cursor, antigravity) |
| Init | AI-first initialization workflow + manual pointer | `.tfw/workflows/init.md`, `.tfw/init.md` (pointer) |
| Config | Centralized project parameters (budgets, templates, workflows, research limits) | `.tfw/PROJECT_CONFIG.yaml` |
| Versioning | Framework version tracking and changelog | `.tfw/VERSION`, `.tfw/CHANGELOG.md` |
| Release | Release strategy and process | `RELEASE.md` (optional), `.tfw/workflows/release.md` |
| Claude Code Adapter | Slash commands + entry point for Claude Code | `CLAUDE.md`, `.claude/commands/`, `.tfw/adapters/claude-code/` |

### Architecture Decisions

| # | Decision | Rationale | Source |
|---|----------|-----------|--------|
| D1 | v2→v3 migration: `.tfw/` as standalone core | Tool-agnostic, forkable, no coupling to specific AI tool | `tasks/TFW-2.../RF__TFW-2...md` |
| D2 | Content distribution: root README = landing, `.tfw/README.md` = paper | Separation of concerns — GitHub visitors vs framework users | `tasks/TFW-3.../RF__TFW-3...md` |
| D3 | Remove STEPS.md | Replaced by RF files + Task Board. Modern tools (KI, conversation logs) handle continuity | `tasks/TFW-4.../HL-TFW-4...md` §2.1 |
| D4 | Remove TASK.md | Scope/DoD lives in TS files, backlog in Task Board | `tasks/TFW-4.../HL-TFW-4...md` |
| D5 | Replace Summary Discipline with Trace Discipline | RF + Task Board = project memory. No separate log needed | `tasks/TFW-4.../HL-TFW-4...md` §3.1 |
| D6 | YAML frontmatter in `.tfw/workflows/` | Antigravity requires `description` field for slash-command registration | TFW-4 Phase A |
| D7 | KNOWLEDGE.md = optional artifact | Greenfield = overhead, brownfield = must-have | `tasks/TFW-5.../RF__TFW-5...md` D1 |
| D8 | tfw-docs triage gate | Minor tasks skip knowledge update (1-second decision: N/A) | `tasks/TFW-5.../HL-TFW-5...md` §3.2 |
| D9 | Semver (MAJOR.MINOR.PATCH) for TFW versioning | Industry standard, easy to communicate breaking vs compatible changes | TFW-6 HL §3 |
| D10 | `tfw-release` as canonical workflow, `RELEASE.md` as project context | Separation: general process in workflow, specific context in per-project file | TFW-6 HL §3, discussion |
| D11 | `tfw-update` with 🟢🟡🔴 change categorization | Prevents overwriting project customizations during framework upgrades | TFW-6 HL §3 |
| D12 | `RELEASE.md` optional (like `KNOWLEDGE.md`) | Avoids file inflation for projects that don't release | TFW-6 discussion |
| D13 | Separate review from handoff — Reviewer role with `🔒 ROLE LOCK` | Executor models self-review when review is embedded in handoff; structural fix via separate workflow + role | TFW-8 HL §2.3, §3 |
| D14 | RESEARCH as optional pipeline gate (🔬 RES) between HL and TS | HL→TS gap loses questions, alternatives, blind spots. RES artifact preserves investigation. Optional skip-path for trivial tasks | TFW-11 HL §1-§3 |
| D15 | Claude Code slash commands as thin adapters — role lock + workflow reference, no logic duplication | Each command sets role, loads context, points to canonical `.tfw/workflows/` file. Single source of truth | TFW-11/C RF §2 Key Decision #2 |
| D16 | Centralize scope budgets, template/workflow lists, and version to `PROJECT_CONFIG.yaml` | Drift proven across TFW-5/8/9/11 — each new template/workflow caused multi-file desyncs. Single YAML source eliminates this class of tech debt | TFW-12 RES §Gather, HL §1 |
| D17 | Pattern B (pure reference) over Pattern A (defaults + pointer) for docs | Budget values exist ONLY in config. Docs say "see config". Stricter single source of truth — user override of RES recommendation | TFW-12 RF §Key Decisions #2 |
| D18 | `tfw-init` as AI-first workflow replacing manual init.md | Agent discovers, interviews, researches, sets up — human init.md was inverted (90% mechanical, 10% valuable) | TFW-13 HL §2-§3 |

---

## 2. Key Artifacts

| Task | Title | Key Artifact | Why Important |
|------|-------|-------------|---------------|
| TFW-2 | Upgrade to TFW v3 | `tasks/TFW-2.../RF__TFW-2...md` | Foundation: v2→v3 migration decisions |
| TFW-3 | README public-readiness | `tasks/TFW-3.../RF__TFW-3...md` | Content distribution matrix (root vs .tfw/) |
| TFW-4 | Framework cleanup | `tasks/TFW-4.../HL-TFW-4...md` | Audit findings, redundancy analysis, meta-project awareness |
| TFW-5 | KNOWLEDGE + tfw-docs | `tasks/TFW-5.../HL-TFW-5...md` | Knowledge feedback loop design |
| TFW-6 | Versioning + update | `tasks/TFW-6.../HL-TFW-6...md` | Version scheme, release/update workflow design, RELEASE.md pattern |
| TFW-8 | Reviewer role + /tfw-review | `tasks/TFW-8.../HL-TFW-8...md` | Role separation, self-review fix, review workflow extraction |
| TFW-11 | RESEARCH stage + Claude Code restore | `tasks/TFW-11.../HL-TFW-11...md` | Optional RESEARCH gate, RES artifact, 8-status pipeline, Claude Code adapter with 9 slash commands |
| TFW-12 | Config centralization | `tasks/TFW-12.../RES__TFW-12...md` | Single source of truth for 4 param categories. First task to use full RESEARCH stage |
| TFW-13 | tfw-init workflow | `tasks/TFW-13.../HL-TFW-13...md` | Init as AI-first workflow, {PREFIX}-1 pattern, /tfw-research in init |

---

## 3. Legacy & Deprecation

| Item | Status | When | Replacement | Source |
|------|--------|------|-------------|--------|
| `STEPS.md` | Removed | 2026-03-03 | RF files + Task Board | TFW-4 D3 |
| `TASK.md` | Removed | 2026-03-03 | TS files (scope/DoD), Task Board (backlog) | TFW-4 D4 |
| Summary Discipline | Removed | 2026-03-03 | Trace Discipline (RF + Task Board) | TFW-4 D5 |
| `AI_ENTRY_POINT.md` | Removed | 2026-02-25 | `.tfw/README.md` + `.tfw/conventions.md` | TFW-2 |
| `SUCCESS_CRITERIA.md` | Removed | 2026-02-25 | TS DoD sections | TFW-2 |
| `00_meta/` directory | Removed | 2026-02-25 | `.tfw/` directory | TFW-2 |
| Review in `handoff.md` (Phase 4) | Removed | 2026-03-12 | `.tfw/workflows/review.md` (standalone Reviewer workflow) | TFW-8 D13 |
| "REVIEW by any role" (conventions §15) | Removed | 2026-03-12 | REVIEW by Reviewer role only | TFW-8 |
| Inline scope budget values in docs | Removed | 2026-03-30 | `tfw.scope_budgets` in PROJECT_CONFIG.yaml | TFW-12 D16/D17 |
| Version strings in document titles | Removed | 2026-03-30 | `{version}` placeholder in adapter templates, no version in core titles | TFW-12 D16 |
| Hardcoded template/workflow lists in adapters | Removed | 2026-03-30 | `tfw.templates` and `tfw.workflows` in PROJECT_CONFIG.yaml | TFW-12 D16 |
| Manual `init.md` (232 lines) | Replaced | 2026-03-31 | `.tfw/workflows/init.md` (AI workflow) + `.tfw/init.md` (pointer) | TFW-13 D18 |

---

## 4. Tech Stack & Infrastructure

| Layer | Technology | Notes |
|-------|-----------|-------|
| Format | Markdown + YAML | All artifacts are plain text |
| VCS | Git (GitHub) | `saubakirov/trace-first-starter` |
| Tools | Claude Code, Cursor, Antigravity | Adapters in `.tfw/adapters/` |
| License | MIT | |

---

> **Maintenance**: This file is updated via the `tfw-docs` workflow after each REVIEW.
> See `.tfw/workflows/docs.md` for the update process.
