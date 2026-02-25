# Trace-First Workflow (TFW) v3 — Canonical Starter

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
| `TASK.md` | Scope, DoD, risks |
| `STEPS.md` | Progress journal (Summary lines) |
| `TECH_DEBT.md` | Tech debt registry |

### .tfw/ (TFW core — tool-agnostic)

| Path | Contents |
|------|----------|
| [`.tfw/README.md`](.tfw/README.md) | Philosophy, thesis, lifecycle, anti-patterns, evolution |
| [`.tfw/conventions.md`](.tfw/conventions.md) | Formal rules, statuses, naming, scope budgets |
| [`.tfw/glossary.md`](.tfw/glossary.md) | Terminology |
| [`.tfw/templates/`](.tfw/templates/) | Canonical templates (HL, TS, RF, ONB, REVIEW) |
| [`.tfw/workflows/`](.tfw/workflows/) | Process workflows (plan, handoff, resume) |
| [`.tfw/adapters/`](.tfw/adapters/) | Tool adapter templates |
| [`.tfw/init.md`](.tfw/init.md) | Setup instructions |
| [`.tfw/PROJECT_CONFIG.yaml`](.tfw/PROJECT_CONFIG.yaml) | Project parameters |

---

## Tool Adapters

TFW v3 works with any development tool. Templates in `.tfw/adapters/`:

| Tool | Adapter | Project entry point |
|------|---------|---------------------|
| Claude Code | `.tfw/adapters/claude-code/` | `CLAUDE.md` (project root) |
| Cursor | `.tfw/adapters/cursor/` | `.cursor/rules/tfw.mdc` |
| Antigravity | `.tfw/adapters/antigravity/` | `.agent/rules/tfw.md` |
| Plain chat | — | Read `.tfw/README.md` directly |

Setup details in [`.tfw/init.md`](.tfw/init.md).

---

## Key Concepts

- **Task lifecycle**: `⬜ TODO → 🔵 HL → 🟡 TS → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE` — [details](.tfw/README.md#task-lifecycle)
- **Execution modes**: CL (Chat Loop, default) / AG (Autonomous) — [details](.tfw/README.md#execution-modes)
- **Scope budgets**: ≤7 files, ≤600 LOC per phase — [details](.tfw/README.md#scope-budgets)
- **Conduct**: no sycophancy, no placeholders, summary discipline — [full rules](.tfw/conventions.md)
- **Current version**: v3 (2026) — [evolution history](.tfw/README.md#evolution)

---

## Links

- **Repository**: [github.com/saubakirov/trace-first-starter](https://github.com/saubakirov/trace-first-starter)
- **Author**: [saubakirov.kz](https://saubakirov.kz)
- **License**: [MIT](LICENSE)

---

## Task Board

| ID | Task | Status | HL | TS | ONB | RF | REV |
|----|------|--------|----|----| --- |----| --- |
| TFW-1 | Formalize success criteria | ✅ DONE | — | ✅ | — | ✅ | — |
| TFW-2 | Upgrade to TFW v3 | ✅ DONE | — | ✅ | — | ✅ | — |
| TFW-3 | Root README public-readiness | 🟢 RF | ✅ | ✅ | — | ✅ | |

> Statuses: ⬜ TODO → 🔵 HL → 🟡 TS → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE | ❌ BLOCKED
