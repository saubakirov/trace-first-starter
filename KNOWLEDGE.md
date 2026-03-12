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

---

## 1. Architecture Map

### Framework Structure

| Component | Description | Key Files |
|-----------|-------------|-----------|
| TFW Core | Tool-agnostic framework spec | `.tfw/README.md`, `.tfw/conventions.md`, `.tfw/glossary.md` |
| Templates | Canonical artifact templates | `.tfw/templates/` (HL, TS, RF, ONB, REVIEW, KNOWLEDGE) |
| Workflows | Task lifecycle workflows | `.tfw/workflows/` (plan, handoff, review, resume, docs, release, update) |
| Adapters | Tool-specific bridges | `.tfw/adapters/` (claude-code, cursor, antigravity) |
| Init | Project bootstrap guide | `.tfw/init.md` |
| Versioning | Framework version tracking and changelog | `.tfw/VERSION`, `.tfw/CHANGELOG.md` |
| Release | Release strategy and process | `RELEASE.md` (optional), `.tfw/workflows/release.md` |

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
