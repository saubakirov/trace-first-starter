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
| P8 | RESEARCH ≠ passive checklist — agent MUST ask pointed questions at every stage, contribute own observations before asking, WAIT for user response, and use at least one external tool per stage (web search, URL read, docs). Internal-only analysis = incomplete research. Running stages silently is a protocol violation. See Research Mindset + Hard Rule #8 in `.tfw/workflows/research.md` | TFW-11 HL §7, TFW-14, TFW-17 HL §7 |
| P9 | Coordinator Mindset: quality of planning > speed of pipeline progression — coordinator asks uncomfortable questions, catches implicit assumptions, protects process from rushing. Every workflow step exists to give the executor a clear spec. See Coordinator Mindset in `.tfw/workflows/plan.md` | TFW-17 HL §7.1 |
| P10 | Token density: workflow instructions MUST stay ≤1200 words. Beyond this, agents lose mid-document attention — stages get skipped, rules ignored. Templates own format definitions; workflows reference templates. See D23 | TFW-21 HL §7, RES (external research) |

---

## 1. Architecture Map

### Framework Structure

| Component | Description | Key Files |
|-----------|-------------|-----------|
| TFW Core | Tool-agnostic framework spec | `.tfw/README.md`, `.tfw/conventions.md`, `.tfw/glossary.md` |
| Templates | Canonical artifact templates | `.tfw/templates/` (HL, TS, RES, RF, ONB, REVIEW, KNOWLEDGE, RELEASE) |
| Workflows | Task lifecycle workflows | `.tfw/workflows/` (init, plan, research, handoff, review, resume, docs, release, update, knowledge) |
| Adapters | Tool-specific bridges | `.tfw/adapters/` (claude-code, cursor, antigravity) |
| Init | AI-first initialization workflow + manual pointer | `.tfw/workflows/init.md`, `.tfw/init.md` (pointer) |
| Config | Centralized project parameters (budgets, templates, workflows, research limits, knowledge limits) | `.tfw/PROJECT_CONFIG.yaml` |
| Knowledge | Fact collection + consolidation infrastructure | `knowledge/`, `.tfw/knowledge_state.yaml`, `.tfw/workflows/knowledge.md` |
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
| D19 | HL update = mandatory output of RESEARCH; Briefing + Closure protocols | Research exists to refine HL, not to jump to TS. Closure writes HL recommendations; coordinator applies. Skip-bias fix: pros/cons format, user decides | TFW-14 HL §7, RES §Closure |
| D20 | Decouple pipeline statuses from document types: `🔵 HL`→`📝 HL_DRAFT`, `🟡 TS`→`🟡 TS_DRAFT`. Centralized status registry in PROJECT_CONFIG.yaml with `role` field. Concept Taxonomy (5 concepts). REJECT = user branching point | Same status count (8), self-documenting `_DRAFT` suffix for AI agents. Implicit approval = transition to next status. Registry = single source of truth for automation | TFW-15 HL §2, RES (Variant D) |
| D21 | Coordinator Mindset section in plan.md + Hard Rule #8 (external tool mandate) in research.md + stage-level mindset reminders + depth self-check in checkpoints | Root cause: plan.md framed coordination as pipeline (HL→TS→handoff), not as quality gate. Agents exhibited skip-bias, rush-bias, and internal-only research. Fix: dual-lever — mindset at coordinator level + enforcement at research stage level | TFW-17 HL §1, §7 |
| D22 | Knowledge consolidation: Fact Candidates in all artifacts (RF/REVIEW/RES), `/tfw-knowledge` 4-phase workflow (Orient→Gather→Consolidate→Prune), topic files in `knowledge/`, configurable Knowledge Gate in plan.md Phase 0. Settings = PROJECT_CONFIG, state = knowledge_state.yaml | 21 RF files analyzed — zero project facts recorded. Knowledge drift proven: facts lost between tasks (RES-12 R3, RF-11A). Design validated against Zettelkasten, LangMem, Claude Code Dream | TFW-18 HL §3, RES R1-R12 |
| D23 | Workflow compression: research.md 2397→1145 words (-52%). Remove inline templates (checkpoint/sufficiency formats) → reference templates/RES.md. Remove duplicate anti-patterns (3 blocks → 1 MUST/NEVER). Remove Example Flow (template + rules = sufficient calibration). Preserve: Mindset, stage reminders, Briefing, Closure, Hard Rules | Agents on new projects skipped research stages — workflow too long for attention budget. External research confirmed: "principles > procedures", "templates > examples", "don’t repeat standard behavior" | TFW-21 HL, RES (external best practices) |

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
| TFW-14 | Research interaction model | `tasks/TFW-14.../HL-TFW-14...md` | Briefing + Closure protocols, turn-based rhythm, Sufficiency Check, skip-bias fix, HL update gate |
| TFW-15 | Pipeline formalization | `tasks/TFW-15.../HL-TFW-15...md` | Status registry (`tfw.statuses`), Concept Taxonomy, HL_DRAFT/TS_DRAFT rename, REJECT branching, Phase 3.5→4 renumber |
| TFW-17 | Research depth + coordinator quality | `tasks/TFW-17.../HL-TFW-17...md` | Coordinator Mindset, Hard Rule #8 (external tools), stage-level reminders, depth self-check. Fixes skip-bias, rush-bias, internal-only research |
| TFW-18 | Knowledge consolidation | `tasks/TFW-18.../HL-TFW-18...md` | Fact Candidates in artifacts, `/tfw-knowledge` 4-phase workflow, `knowledge/` topic files, Knowledge Gate (Phase 0), configurable limits. First RESEARCH with 3 external models (Zettelkasten, LangMem, Claude Code Dream) |
| TFW-21 | Research workflow compression | `tasks/TFW-21.../HL-TFW-21...md` | research.md 2397→1145 words (-52%). Template-owns-format pattern. Inline checkpoint/sufficiency moved to templates/RES.md. External best practice validation |

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
| Complexity Check in RESEARCH Final Checkpoint | Replaced | 2026-04-01 | Sufficiency Check ("sufficient for HL finalization?") | TFW-14 D19 |
| `🔵 HL` / `🟡 TS` board statuses | Replaced | 2026-04-01 | `📝 HL_DRAFT` / `🟡 TS_DRAFT` (process statuses ≠ document types) | TFW-15 D20 |
| `Phase 3.5: RESEARCH Gate` in plan.md | Replaced | 2026-04-01 | `Phase 4: RESEARCH Gate` (clean numbering: 1→2→3→4→5) | TFW-15 |
| `Autonomous search: documentation, changelogs...` in Gather stage | Replaced | 2026-04-03 | `**Search externally**: how is this problem solved elsewhere?...` (explicit, directive) | TFW-17 D21 |
| Coordinator without Mindset section | Replaced | 2026-04-03 | Coordinator Mindset section after Role Lock: quality > speed, anti-rush, RESEARCH default | TFW-17 D21 |
| Example Flow in research.md (45 lines) | Removed | 2026-04-03 | Template RES.md + Hard Rules = sufficient calibration | TFW-21 D23 |
| "Good/Bad research" + "Operational" sections in research.md | Removed | 2026-04-03 | Merged into MUST/NEVER rules block | TFW-21 D23 |
| Inline checkpoint/sufficiency templates in research.md | Removed | 2026-04-03 | Format fields moved to `templates/RES.md` (template-owns-format pattern) | TFW-21 D23 |
| Duplicate Anti-patterns block in research.md | Removed | 2026-04-03 | Merged into single Rules section (MUST + NEVER) | TFW-21 D23 |

---

## 4. Tech Stack & Infrastructure

| Layer | Technology | Notes |
|-------|-----------|-------|
| Format | Markdown + YAML | All artifacts are plain text |
| VCS | Git (GitHub) | `saubakirov/trace-first-starter` |
| Tools | Claude Code, Cursor, Antigravity | Adapters in `.tfw/adapters/` |
| License | MIT | |

---

## 5. Project Facts

> Index of verified project knowledge. Details in `knowledge/` topic files.
> Updated by `/tfw-knowledge` consolidation.

| Category | Count | Topic File |
|----------|-------|------------|
| convention | 3 facts | [→](knowledge/convention.md) |
| process | 3 facts | [→](knowledge/process.md) |
| philosophy | 1 fact | [→](knowledge/philosophy.md) |
| constraint | 1 fact | [→](knowledge/constraint.md) |

---

> **Maintenance**: This file is updated via the `tfw-docs` workflow after each REVIEW.
> See `.tfw/workflows/docs.md` for the update process.
