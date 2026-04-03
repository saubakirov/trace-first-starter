# Trace-First Workflow (TFW) — Canonical Starter

> *"The thought process and the instructions are more valuable than the immediate result."*

Most work with AI happens in dialogue — and then the chat ends. Tomorrow you re-explain the project from scratch. Context evaporates across sessions, models, and teams. TFW solves this: a single ritual that captures intent, structures decisions, and makes any project resumable by any agent or human.

For the full philosophy, thesis, and design rationale → [`.tfw/README.md`](.tfw/README.md)

---

## Who This Is For

TFW is domain-agnostic. It works for:

- **Software engineering** — architecture decisions, codebase development, debugging sessions
- **Data and analytics** — ETL pipelines, SQL analysis, reporting with human-in-the-loop
- **Writing and publishing** — blog posts, reports, contracts, academic papers
- **Education** — course development, assignment creation, research projects
- **Product management** — specs, roadmaps, decision logs

If your work involves AI-assisted iteration and you need continuity across sessions — TFW is for you.

---

## Quick Start

### New project

1. Fork or clone this repository
2. Follow [`.tfw/init.md`](.tfw/init.md) to configure your project
3. Choose your tool adapter (Claude Code, Cursor, Antigravity, or plain chat)
4. Start with [`.tfw/workflows/plan.md`](.tfw/workflows/plan.md) to create your first task

### Mid-conversation

Already deep in a chat and realize it's time to get structured?

1. Paste this repo link: `https://github.com/saubakirov/trace-first-starter`
2. The agent reads README → AGENTS, harvests your existing context, and bootstraps TFW files
3. Review the drafts, pick a mode, continue — now with traces

---

## What's Inside

### Root Files (your project)

| File | Purpose |
|------|---------|
| `README.md` | Project guide + Task Board |
| `AGENTS.md` | AI agent role and behavior |
| `KNOWLEDGE.md` | Architecture, decisions, legacy index |
| `TECH_DEBT.md` | Tech debt registry |
| `RELEASE.md` | Release strategy and context (optional) |

### .tfw/ (TFW core — tool-agnostic)

| Path | Contents |
|------|----------|
| [`.tfw/README.md`](.tfw/README.md) | Philosophy, thesis, lifecycle, anti-patterns, evolution |
| [`.tfw/conventions.md`](.tfw/conventions.md) | Formal rules, statuses, naming, scope budgets |
| [`.tfw/glossary.md`](.tfw/glossary.md) | Terminology |
| [`.tfw/templates/`](.tfw/templates/) | Canonical templates (HL, TS, RF, ONB, REVIEW) |
| [`.tfw/workflows/`](.tfw/workflows/) | Process workflows (plan, handoff, resume, release, update) |
| [`.tfw/adapters/`](.tfw/adapters/) | Tool adapter templates |
| [`.tfw/init.md`](.tfw/init.md) | Setup instructions |
| [`.tfw/PROJECT_CONFIG.yaml`](.tfw/PROJECT_CONFIG.yaml) | Project parameters |
| [`.tfw/VERSION`](.tfw/VERSION) | Current framework version (semver) |
| [`.tfw/CHANGELOG.md`](.tfw/CHANGELOG.md) | Version history |

---

## Tool Adapters

TFW works with any development tool. Templates in `.tfw/adapters/`:

| Tool | Adapter | Project entry point |
|------|---------|---------------------|
| Claude Code | `.tfw/adapters/claude-code/` | `CLAUDE.md` (project root) |
| Cursor | `.tfw/adapters/cursor/` | `.cursor/rules/tfw.mdc` |
| Antigravity | `.tfw/adapters/antigravity/` | `.agent/rules/tfw.md` |
| Plain chat | — | Read `.tfw/README.md` directly |

Setup details in [`.tfw/init.md`](.tfw/init.md).

---

## Key Concepts

- **Task lifecycle**: `⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE` (RES optional) — [details](.tfw/README.md#task-lifecycle)
- **Execution modes**: CL (Chat Loop, default) / AG (Autonomous) — [details](.tfw/README.md#execution-modes)
- **Scope budgets**: configurable per phase — see `tfw.scope_budgets` in [PROJECT_CONFIG](.tfw/PROJECT_CONFIG.yaml) — [details](.tfw/README.md#scope-budgets)
- **Conduct**: no sycophancy, no placeholders — [full rules](.tfw/conventions.md)
- **Versioning**: semver in `.tfw/VERSION`, changelog in `.tfw/CHANGELOG.md` — [details](.tfw/CHANGELOG.md)
- **Current version**: see [`.tfw/VERSION`](.tfw/VERSION) — [changelog](.tfw/CHANGELOG.md) · [evolution](.tfw/README.md#evolution)

---

## Links

- **Repository**: [github.com/saubakirov/trace-first-starter](https://github.com/saubakirov/trace-first-starter)
- **Author**: [saubakirov.kz](https://saubakirov.kz)
- **License**: [MIT](LICENSE)

---

## Task Board

| ID | Task | Status | HL | TS | ONB | RF | REV |
|----|------|--------|----|----| --- |----| --- |
| [TFW-1](tasks/TFW-1__formalize_success_criteria/) | Formalize success criteria | ✅ DONE | — | ✅ | — | ✅ | — |
| [TFW-2](tasks/TFW-2__upgrade_to_v3/) | Upgrade to TFW v3 | ✅ DONE | — | ✅ | — | ✅ | — |
| [TFW-3](tasks/TFW-3__readme_public_readiness/) | Root README public-readiness | 🟢 RF | ✅ | ✅ | — | ✅ | |
| [TFW-4](tasks/TFW-4__framework_cleanup/) | Framework cleanup | 🟡 TS | ✅ | ✅ | | | |
| [TFW-5](tasks/TFW-5__knowledge_and_tfw_docs/) | KNOWLEDGE.md + tfw-docs workflow | ✅ DONE | ✅ | ✅ | — | ✅ | ✅ |
| [TFW-6](tasks/TFW-6__versioning_and_update/) | Versioning, changelog, tfw-update workflow | ✅ DONE | ✅ | ✅ | [A](tasks/TFW-6__versioning_and_update/ONB__PhaseA__versioning_infra.md) [B](tasks/TFW-6__versioning_and_update/ONB__PhaseB__workflows.md) [C](tasks/TFW-6__versioning_and_update/ONB__PhaseC__documentation.md) | [A](tasks/TFW-6__versioning_and_update/RF__PhaseA__versioning_infra.md) [B](tasks/TFW-6__versioning_and_update/RF__PhaseB__workflows.md) [C](tasks/TFW-6__versioning_and_update/RF__PhaseC__documentation.md) | [A](tasks/TFW-6__versioning_and_update/REVIEW__PhaseA__versioning_infra.md) [B](tasks/TFW-6__versioning_and_update/REVIEW__PhaseB__workflows.md) [C](tasks/TFW-6__versioning_and_update/REVIEW__PhaseC__documentation.md) |
| [TFW-7](tasks/TFW-7__resolve_tech_debt/) | Resolve all open tech debt | ✅ DONE | ✅ | ✅ | [✅](tasks/TFW-7__resolve_tech_debt/ONB__TFW-7__resolve_tech_debt.md) | [✅](tasks/TFW-7__resolve_tech_debt/RF__TFW-7__resolve_tech_debt.md) | [✅](tasks/TFW-7__resolve_tech_debt/REVIEW__TFW-7__resolve_tech_debt.md) |
| [TFW-8](tasks/TFW-8__reviewer_role_and_workflow/) | Reviewer role + /tfw-review workflow | ✅ DONE | [✅](tasks/TFW-8__reviewer_role_and_workflow/HL-TFW-8__reviewer_role_and_workflow.md) | [✅](tasks/TFW-8__reviewer_role_and_workflow/TS__TFW-8__reviewer_role_and_workflow.md) | [✅](tasks/TFW-8__reviewer_role_and_workflow/ONB__TFW-8__reviewer_role_and_workflow.md) | [A](tasks/TFW-8__reviewer_role_and_workflow/RF__PhaseA__core_extraction.md) [B](tasks/TFW-8__reviewer_role_and_workflow/RF__PhaseB__documentation_sync.md) | [A](tasks/TFW-8__reviewer_role_and_workflow/REVIEW__PhaseA__core_extraction.md) [B](tasks/TFW-8__reviewer_role_and_workflow/REVIEW__PhaseB__documentation_sync.md) |
| [TFW-9](tasks/TFW-9__update_source_mechanism/) | Update source mechanism for tfw-update | ✅ DONE | [✅](tasks/TFW-9__update_source_mechanism/HL-TFW-9__update_source_mechanism.md) | [✅](tasks/TFW-9__update_source_mechanism/TS__TFW-9__update_source_mechanism.md) | [✅](tasks/TFW-9__update_source_mechanism/ONB__TFW-9__update_source_mechanism.md) | [✅](tasks/TFW-9__update_source_mechanism/RF__TFW-9__update_source_mechanism.md) | [✅](tasks/TFW-9__update_source_mechanism/REVIEW__TFW-9__update_source_mechanism.md) |
| [TFW-10](tasks/TFW-10__version_string_sweep/) | Replace stale "TFW v3" labels with semver | ✅ DONE | [✅](tasks/TFW-10__version_string_sweep/HL-TFW-10__version_string_sweep.md) | [✅](tasks/TFW-10__version_string_sweep/TS__TFW-10__version_string_sweep.md) | [✅](tasks/TFW-10__version_string_sweep/ONB__TFW-10__version_string_sweep.md) | [✅](tasks/TFW-10__version_string_sweep/RF__TFW-10__version_string_sweep.md) | [✅](tasks/TFW-10__version_string_sweep/REVIEW__TFW-10__version_string_sweep.md) |
| [TFW-11](tasks/TFW-11__research_stage/) | RESEARCH stage in pipeline | ✅ DONE | ✅ | ✅ | ✅ | [A](tasks/TFW-11__research_stage/RF__PhaseA__core_artifact_workflow.md) [B](tasks/TFW-11__research_stage/RF__PhaseB__integration_desyncs.md) [C](tasks/TFW-11__research_stage/RF__PhaseC__adapter_sync_version.md) | [A](tasks/TFW-11__research_stage/REVIEW__PhaseA__core_artifact_workflow.md) [B](tasks/TFW-11__research_stage/REVIEW__PhaseB__integration_desyncs.md) [C](tasks/TFW-11__research_stage/REVIEW__PhaseC__adapter_sync_version.md) |
| [TFW-12](tasks/TFW-12__scope_budget_centralization/) | Centralize config params in PROJECT_CONFIG | ✅ DONE | ✅ | ✅ | ✅ | [✅](tasks/TFW-12__scope_budget_centralization/RF__TFW-12__config_centralization.md) | [✅](tasks/TFW-12__scope_budget_centralization/REVIEW__TFW-12__config_centralization.md) |
| [TFW-13](tasks/TFW-13__tfw_init_workflow/) | tfw-init workflow (replace init.md) | ✅ DONE | ✅ | [A](tasks/TFW-13__tfw_init_workflow/TS__PhaseA__workflow_and_command.md) [B](tasks/TFW-13__tfw_init_workflow/TS__PhaseB__docs_and_cleanup.md) | [A](tasks/TFW-13__tfw_init_workflow/ONB__PhaseA__workflow_and_command.md) [B](tasks/TFW-13__tfw_init_workflow/ONB__PhaseB__docs_and_cleanup.md) | [A](tasks/TFW-13__tfw_init_workflow/RF__PhaseA__workflow_and_command.md) [B](tasks/TFW-13__tfw_init_workflow/RF__PhaseB__docs_and_cleanup.md) | [A](tasks/TFW-13__tfw_init_workflow/REVIEW__PhaseA__workflow_and_command.md) [B](tasks/TFW-13__tfw_init_workflow/REVIEW__PhaseB__docs_and_cleanup.md) |
| [TFW-14](tasks/TFW-14__research_interaction_model/) | Research interaction model (briefing + handoff) | ✅ DONE | [✅](tasks/TFW-14__research_interaction_model/HL-TFW-14__research_interaction_model.md) | [✅](tasks/TFW-14__research_interaction_model/RES__TFW-14__research_interaction_model.md) | [✅](tasks/TFW-14__research_interaction_model/TS__TFW-14__research_interaction_model.md) | [✅](tasks/TFW-14__research_interaction_model/RF__TFW-14__research_interaction_model.md) | [✅](tasks/TFW-14__research_interaction_model/REVIEW__TFW-14__research_interaction_model.md) |
| [TFW-15](tasks/TFW-15__pipeline_status_rename/) | Pipeline rename: separate statuses from documents (HL_DRAFT → RES → TS_DRAFT) | ✅ DONE | [✅](tasks/TFW-15__pipeline_status_rename/HL-TFW-15__pipeline_status_rename.md) | [✅](tasks/TFW-15__pipeline_status_rename/RES__TFW-15__pipeline_status_rename.md) | [✅](tasks/TFW-15__pipeline_status_rename/TS__TFW-15__pipeline_formalization.md) | [✅](tasks/TFW-15__pipeline_status_rename/RF__TFW-15__pipeline_formalization.md) | [✅](tasks/TFW-15__pipeline_status_rename/REVIEW__TFW-15__pipeline_formalization.md) |
| TFW-16 | tfw-doctor: analyze user behavior, chats, KI, tasks — find missed workflows, knowledge gaps, hidden flows | ⬜ TODO | | | | | |
| [TFW-17](tasks/TFW-17__research_depth_and_coordinator_quality/) | Research depth + coordinator quality (skip-bias, external tools, rush-bias) | ✅ DONE | [✅](tasks/TFW-17__research_depth_and_coordinator_quality/HL-TFW-17__research_depth_and_coordinator_quality.md) | [✅](tasks/TFW-17__research_depth_and_coordinator_quality/TS__TFW-17__research_depth_and_coordinator_quality.md) | [✅](tasks/TFW-17__research_depth_and_coordinator_quality/ONB__TFW-17__research_depth_and_coordinator_quality.md) | [✅](tasks/TFW-17__research_depth_and_coordinator_quality/RF__TFW-17__research_depth_and_coordinator_quality.md) | [✅](tasks/TFW-17__research_depth_and_coordinator_quality/REVIEW__TFW-17__research_depth_and_coordinator_quality.md) |
| [TFW-18](tasks/TFW-18__knowledge_consolidation/) | Knowledge consolidation: fact candidates, dream-like docs, mandatory gate | ✅ DONE | [✅](tasks/TFW-18__knowledge_consolidation/HL-TFW-18__knowledge_consolidation.md) | [✅](tasks/TFW-18__knowledge_consolidation/RES__TFW-18__knowledge_consolidation.md) | [✅](tasks/TFW-18__knowledge_consolidation/TS__TFW-18__knowledge_consolidation.md) | [✅](tasks/TFW-18__knowledge_consolidation/ONB__TFW-18__knowledge_consolidation.md) | [✅](tasks/TFW-18__knowledge_consolidation/REVIEW__TFW-18__knowledge_consolidation.md) |
| [TFW-19](tasks/TFW-19__config_propagation/) | tfw-config: propagate PROJECT_CONFIG.yaml changes to workflows/adapters automatically | ✅ DONE | [✅](tasks/TFW-19__config_propagation/HL-TFW-19__config_propagation.md) | [✅](tasks/TFW-19__config_propagation/RES__TFW-19__config_propagation.md) | [✅](tasks/TFW-19__config_propagation/TS__TFW-19__config_propagation.md) | [✅](tasks/TFW-19__config_propagation/ONB__TFW-19__config_propagation.md) | [✅](tasks/TFW-19__config_propagation/REVIEW__TFW-19__config_propagation.md) |
| TFW-20 | tfw-user-tune: personal preferences pipeline (.user_preferences.md lifecycle, gitignored, user-specific) | ⬜ TODO | | | | | |
| [TFW-21](tasks/TFW-21__research_workflow_compression/) | Compress research.md: 2397→1145 words (-52%), deduplicate, remove inline templates | ✅ DONE | [✅](tasks/TFW-21__research_workflow_compression/HL-TFW-21__research_workflow_compression.md) | [✅](tasks/TFW-21__research_workflow_compression/RES__TFW-21__research_workflow_compression.md) | [✅](tasks/TFW-21__research_workflow_compression/TS__TFW-21__research_workflow_compression.md) | [✅](tasks/TFW-21__research_workflow_compression/RF__TFW-21__research_workflow_compression.md) | [✅](tasks/TFW-21__research_workflow_compression/REVIEW__TFW-21__research_workflow_compression.md) |

> Statuses: ⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE | ❌ BLOCKED
