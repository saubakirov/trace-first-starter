<p align="center">
  <a href="README.md">English</a> ·
  <a href="README.ru.md">Русский</a> ·
  <a href="README.kk.md">Қазақша</a>
</p>

<p align="center">
  <img src="docs/brand/logo.png" alt="TFW" width="200">
</p>

<h1 align="center">Trace-First Workflow</h1>

<p align="center"><i>"The thinking is the product. Everything else is output."</i></p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
  <a href=".tfw/VERSION"><img src="https://img.shields.io/github/v/tag/saubakirov/trace-first-starter?label=version&color=blue" alt="Version"></a>
</p>

> **Semantic source:** this English project guide and the English [Project North Star](.tfw/README.md) define the public meaning of TFW. [Russian](README.ru.md) and [Kazakh](README.kk.md) are full localizations of this guide.

> *Imagine a product that knows more about itself than just its output —*
> *its purpose, its decisions, its rejected alternatives, its evidence, and its debt.*

Most projects cannot explain themselves. Their reasoning lives in expired chats, in someone's head, or in meetings nobody recorded. A new teammate or a new AI session sees the output but not the goal, constraints, evidence, or safe next step.

Trace-First Workflow (TFW) makes that work inspectable and continuable. **TFW is a methodology for joint human–AI work, grounded in the Philosophy of Trace.** Humans retain purpose, legitimate authority, judgment, acceptance, accountability, and responsibility to stop; agents perform bounded work. A **Trace** is selected durable context—not a raw transcript or hidden reasoning—that preserves decisions, results or current state, evidence, limits, and continuation.

This repository is the complete TFW starter: choose an Edition, place it in a project, and use its files and workflows to leave enough reliable context for the next authorized person or agent. TFW does not promise automatic truth, identical reproduction, self-maintaining documentation, or independent agent authority.

For the full philosophical argument, read the **[Project North Star](.tfw/README.md)**. This README stays a practical project guide.

---

## Editions

TFW Editions provide different amounts of discipline for different kinds of work. They are not ranks of personal maturity: the same person can use Light for one analysis, Assisted for a recurring process, and Full for a costly long-running project.

| Edition | Choose it when | What you get | Start here |
|---|---|---|---|
| **Light** | Work is one-off, educational, or exploratory; one person is responsible; a missed manual update is tolerable | Four short files for the goal, task list, task trace, and durable project memory | [`editions/01-light/`](editions/01-light/) |
| **Assisted** | Work repeats, two or three participants need separate ownership, or missed trace/status updates recur | Light discipline plus Codex-supported structure and quiet checks; the documented manual order remains the proven fallback | [`editions/02-assisted/`](editions/02-assisted/) |
| **Full** | Work is long-running, cross-functional, regulated, or expensive to get wrong; formal research, evidence, review, and knowledge gates are needed | The complete `HL → RES → TS → ONB → RF → REVIEW` lifecycle | [`.tfw/`](.tfw/) |

Choose the smallest Edition that matches the work. Copy the **contents** of its directory into the project root; do not work inside a nested `editions/01-light/` or `editions/02-assisted/` directory. See the [Edition selection and migration guide](editions/README.md).

---

## Who TFW Is For

**Teams and individuals who cannot afford to lose the reasons behind their work.** TFW is domain-agnostic: its practical discipline applies to software, analytics, research, writing, education, design, and business operations.

<table><tr><td>

#### 🎯 Product leaders carrying decisions across teams

Strategy discussed in one session may not reach the person implementing it. When participants change, the rationale and rejected options disappear. TFW leaves inspectable decisions, authority, evidence, and next steps so another authorized participant can continue without inventing the missing context.

</td></tr><tr><td>

#### 🔬 Analysts and researchers building knowledge iteratively

Earlier analysis is hard to discover, research iterations lose their assumptions, and a final report rarely exposes the choices that shaped it. TFW keeps each iteration and its findings, tested hypotheses, limits, and decisions available for later verification and consolidation.

</td></tr><tr><td>

#### ⚙️ Product-minded engineers preserving architecture context

Code records what exists, not necessarily why it was built that way. TFW keeps architecture decisions, constraints, rejected alternatives, evidence, and technical debt near the implementation so a new developer can inspect the reasoning before changing it.

</td></tr></table>

---

## Quick Start

Start by choosing an Edition. If you are unsure, give the agent the [Edition guide](editions/README.md) and describe the work, participants, duration, and cost of a missed update. The agent should recommend the smallest suitable Edition; the human decides.

### New project — start from scratch

Copy this prompt into an agent that can read and edit files:

    I want to start a new project with Trace-First Workflow (TFW).
    Clone https://github.com/saubakirov/trace-first-starter to a temporary directory.
    Read editions/README.md, recommend the smallest Edition for my work, and explain the choice.
    After I choose, copy the contents of that Edition into my project root and follow its README.
    If I choose Full, copy .tfw/ and follow .tfw/quickstart.md step by step.
    My project is about: <describe the project, participants, duration, and risk>

### Existing project — add TFW without losing state

    I want to add Trace-First Workflow (TFW) to this existing project.
    First inspect the repository and identify files or traces that must be preserved.
    Clone https://github.com/saubakirov/trace-first-starter to a temporary directory.
    Read editions/README.md and recommend the smallest suitable Edition.
    Do not overwrite project state. Use the selected Edition's migration path;
    for Full, copy .tfw/ into the project root and follow .tfw/quickstart.md.
    My project is about: <describe the project, participants, duration, and risk>

For **Light → Assisted**, follow [`editions/02-assisted/MIGRATION.md`](editions/02-assisted/MIGRATION.md) and preserve the Light goal, tasks, traces, results, and memory. Move to Full when the work needs the complete formal lifecycle.

### Already configured — start working

    Read AGENTS.md and the active Edition instructions for project context.
    Give me the current state and the next safe action.
    For a new Full TFW task, start with: /tfw-plan
    Task: <describe the result you need>

In Full TFW, use `/tfw-plan` to create or revise a task plan, `/tfw-handoff` to execute an approved TS, `/tfw-review` to independently verify completed work, and `/tfw-resume` to continue interrupted work. Other repository workflows use `/tfw-research`, `/tfw-docs`, `/tfw-knowledge`, `/tfw-release`, `/tfw-update`, `/tfw-config`, and `/tfw-init`.

**Codex users:** the same `/tfw-*` commands are implemented by repository-local skills, with root `AGENTS.md` as fallback routing; no Codex-specific wrapper is required. Installation and repair instructions are in [`.tfw/adapters/codex/`](.tfw/adapters/codex/README.md).

### FAQ

**Do I need to read every framework file?**
No. A human can begin with this guide, choose an Edition, and let the agent follow the edition instructions. Reading the [Project North Star](.tfw/README.md) is recommended when you want the full purpose and philosophical boundary. Mechanics are in [`.tfw/conventions.md`](.tfw/conventions.md).

**Which AI tools work with TFW?**
Any tool that can read project files can follow the method. Adapter templates exist for Claude Code, Cursor, Antigravity, and Codex. Plain chat can work when you explicitly provide the relevant files and ask it to follow them.

**Can I use TFW for non-code work?**
Yes. TFW structures decisions and continuity, not programming alone. Light grew from a live non-code educational use case, and the same principles apply to research, analytics, writing, teaching, design, and operations.

**How is TFW different from Confluence or Notion?**
Those tools can store and publish knowledge. TFW organizes the work itself so selected decisions, evidence, limits, and next steps are written into versioned traces as the work progresses. It still requires human judgment about what is authoritative and worth preserving; it does not document everything automatically.

**Does the next agent reproduce the previous agent's mind?**
No. A trace is selected durable context, not a transcript or a claim of identical reproduction. The next authorized participant inspects the recorded state, evidence, and constraints and then exercises judgment.

**Where can I learn visually?**
Use the [interactive FAQ](https://notebooklm.google.com/notebook/0a4cc544-0c0a-4fb0-b7ae-f075625d0980), [onboarding slides](https://notebooklm.google.com/notebook/0a4cc544-0c0a-4fb0-b7ae-f075625d0980?artifactId=e274558e-7d56-45ea-b2e7-efc7f6ccdf46), or [video overview](https://notebooklm.google.com/notebook/0a4cc544-0c0a-4fb0-b7ae-f075625d0980?artifactId=f800b95b-aefb-4447-a9c9-42adb5455e45). These URLs are preserved from the established project guide; this README does not claim that an external service is always available.

---

## How It Works

| | Principle | What it means in practice |
|---|---|---|
| 🧠 | **Inspectable project context** | Purpose, decisions, constraints, rejected alternatives, evidence, current state, and debt can be inspected alongside the output; “self-aware” means these capabilities, not an anthropomorphic project |
| 🔄 | **Resume from a checkpoint** | A person or agent reads the Task Board and relevant traces, verifies the recorded state, and continues from an explicit handoff instead of relying on a vanished chat |
| 📈 | **Knowledge can compound** | Task traces preserve candidates; review and knowledge consolidation promote durable facts rather than treating every note as truth |
| 🤝 | **Humans and agents have different responsibilities** | Humans retain purpose, authority, judgment, acceptance, accountability, and the stop decision; agents perform bounded roles inside the approved contract |
| 🌐 | **Proportional discipline across domains** | Light, Assisted, and Full apply the same forward continuity contract with different artifacts and gates appropriate to the work and risk |

---

## What's Inside

<p align="center">
  <img src="docs/brand/overview.png" alt="TFW overview">
</p>

### Root files in a Full project

| File | Purpose |
|---|---|
| `README.md` | Practical project guide and live Task Board |
| `AGENTS.md` | Agent conduct, project routing, and `/tfw-*` command fallback |
| `KNOWLEDGE.md` | Verified architecture, decisions, and durable project knowledge |
| `TECH_DEBT.md` | Technical-debt registry |
| `RELEASE.md` | Release strategy and context when the project uses releases |

### `.tfw/` — Full TFW core

| Path | Contents |
|---|---|
| [`.tfw/README.md`](.tfw/README.md) | Project North Star: purpose, principles, and non-goals |
| [`.tfw/conventions.md`](.tfw/conventions.md) | Formal mechanics: roles, statuses, naming, evidence, gates, and scope budgets |
| [`.tfw/glossary.md`](.tfw/glossary.md) | Canonical terminology |
| [`.tfw/templates/`](.tfw/templates/) | Canonical templates for task, research, execution, evidence, review, and knowledge traces |
| [`.tfw/workflows/`](.tfw/workflows/) | `plan`, `research`, `handoff`, `review`, `resume`, `docs`, `knowledge`, `release`, `update`, `config`, and `init` workflows |
| [`.tfw/adapters/`](.tfw/adapters/) | Tool-specific routing templates |
| [`.tfw/quickstart.md`](.tfw/quickstart.md) | Initialization reading list and procedure for AI agents |
| [`.tfw/project_config.yaml`](.tfw/project_config.yaml) | Project parameters and scope limits |
| [`.tfw/VERSION`](.tfw/VERSION) | Installed framework version |
| [`.tfw/CHANGELOG.md`](.tfw/CHANGELOG.md) | Framework version history |
| [tfw.saubakirov.kz](https://tfw.saubakirov.kz/) | Documentation site generated from repository artifacts |

Light and Assisted have their own smaller root structures. Their READMEs are authoritative for those Editions.

---

## Tool Adapters

<img src="docs/brand/commands_card.png" alt="TFW commands" width="340">

TFW is tool-agnostic. Adapters translate the same repository-local workflow into a tool's project entry point:

| Tool | Adapter | Project entry point |
|---|---|---|
| Claude Code | `.tfw/adapters/claude-code/` | Root `CLAUDE.md` |
| Cursor | `.tfw/adapters/cursor/` | `.cursor/rules/tfw.mdc` |
| Antigravity | `.tfw/adapters/antigravity/` | `.agent/rules/tfw.md` |
| Codex | `.tfw/adapters/codex/` | Root `AGENTS.md` plus `.agents/skills/tfw-*/SKILL.md` |
| Plain chat | No installed adapter | Provide the relevant repository files explicitly |

Start with [`.tfw/quickstart.md`](.tfw/quickstart.md); adapter-specific instructions live under [`.tfw/adapters/`](.tfw/adapters/).

---

## Key Concepts

The complete Full lifecycle is visible in the Task Board and trace files:

```text
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE
```

`RES` and `KNW` are conditional gates. `❌ REJECTED` preserves a failed attempt and its learning; `❌ BLOCKED` records an impasse without pretending the task is complete.

| Concept | Practical meaning | Reference |
|---|---|---|
| Roles | Coordinator plans, Researcher investigates, Executor implements, Reviewer independently verifies | [glossary](.tfw/glossary.md) |
| Execution modes | CL (Chat Loop) is default; AG (Autonomous) requires explicit authorization | [conventions](.tfw/conventions.md) |
| Scope budgets | File, new-file, line, and modified-file ceilings are configured per project and checked before execution | [project config](.tfw/project_config.yaml) |
| Evidence | A TS says what evidence is needed; the RF reports what was collected; REVIEW audits sufficiency | [conventions](.tfw/conventions.md) |
| Task memory | `HL`, `RES`, `TS`, `ONB`, `RF`, `REVIEW`, and knowledge traces serve different decisions; they are not raw chat logs | [templates](.tfw/templates/) |
| Conduct | Work directly, concretely, and completely; do not flatter, leave placeholders, or request plaintext secrets | [conventions](.tfw/conventions.md) |
| Versioning | The installed semantic version is in `.tfw/VERSION`; changes are recorded in the changelog | [changelog](.tfw/CHANGELOG.md) |

For current mechanics, use [conventions](.tfw/conventions.md) and the relevant [workflow](.tfw/workflows/). For the reasoning behind the methodology, use the [Project North Star](.tfw/README.md).

---

## Updating TFW

Check the installed semantic version in [`.tfw/VERSION`](.tfw/VERSION). To compare and update the Full core while preserving project state, ask the agent:

> `/tfw-update`

The update workflow fetches the configured upstream, compares versions, classifies changes as safe, merge-sensitive, or breaking, and applies the selected changes without treating project-specific state as disposable. Read the exact procedure in [`.tfw/workflows/update.md`](.tfw/workflows/update.md) and the version history in [`.tfw/CHANGELOG.md`](.tfw/CHANGELOG.md).

---

## Links

| Need | Destination |
|---|---|
| 🚀 Choose and start | [Edition guide](editions/README.md) · [Full Quick Start](.tfw/quickstart.md) |
| 🧭 Current mechanics | [Conventions](.tfw/conventions.md) · [Glossary](.tfw/glossary.md) · [Workflows](.tfw/workflows/) |
| 💡 Philosophy | [Project North Star](.tfw/README.md) |
| 🧾 History and evidence | [Task Board](#task-board) · [`tasks/`](tasks/) · [Verified knowledge](KNOWLEDGE.md) · [Changelog](.tfw/CHANGELOG.md) |
| 🤖 Interactive help | [NotebookLM FAQ](https://notebooklm.google.com/notebook/0a4cc544-0c0a-4fb0-b7ae-f075625d0980) |
| 🎓 Visual introduction | [Onboarding slides](https://notebooklm.google.com/notebook/0a4cc544-0c0a-4fb0-b7ae-f075625d0980?artifactId=e274558e-7d56-45ea-b2e7-efc7f6ccdf46) · [Video overview](https://notebooklm.google.com/notebook/0a4cc544-0c0a-4fb0-b7ae-f075625d0980?artifactId=f800b95b-aefb-4447-a9c9-42adb5455e45) |
| 🌐 Documentation | [tfw.saubakirov.kz](https://tfw.saubakirov.kz/) |
| 🔗 Repository | [github.com/saubakirov/trace-first-starter](https://github.com/saubakirov/trace-first-starter) |
| 👤 Author | [saubakirov.kz](https://saubakirov.kz/) |
| ⚖️ License | [MIT](LICENSE) |

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
| TFW-16 | tfw-doctor: self-diagnosis of TFW meta-state — verify knowledge_state.yaml matches project, detect stale refs after update, analyze user behavior, find missed workflows, knowledge gaps | ⬜ TODO | | | | | |
| [TFW-17](tasks/TFW-17__research_depth_and_coordinator_quality/) | Research depth + coordinator quality (skip-bias, external tools, rush-bias) | ✅ DONE | [✅](tasks/TFW-17__research_depth_and_coordinator_quality/HL-TFW-17__research_depth_and_coordinator_quality.md) | [✅](tasks/TFW-17__research_depth_and_coordinator_quality/TS__TFW-17__research_depth_and_coordinator_quality.md) | [✅](tasks/TFW-17__research_depth_and_coordinator_quality/ONB__TFW-17__research_depth_and_coordinator_quality.md) | [✅](tasks/TFW-17__research_depth_and_coordinator_quality/RF__TFW-17__research_depth_and_coordinator_quality.md) | [✅](tasks/TFW-17__research_depth_and_coordinator_quality/REVIEW__TFW-17__research_depth_and_coordinator_quality.md) |
| [TFW-18](tasks/TFW-18__knowledge_consolidation/) | Knowledge consolidation: fact candidates, dream-like docs, mandatory gate | ✅ DONE | [✅](tasks/TFW-18__knowledge_consolidation/HL-TFW-18__knowledge_consolidation.md) [✅](tasks/TFW-18__knowledge_consolidation/HL__PhaseB__knowledge_quality.md) | [✅](tasks/TFW-18__knowledge_consolidation/RES__TFW-18__knowledge_consolidation.md) | [✅](tasks/TFW-18__knowledge_consolidation/TS__TFW-18__knowledge_consolidation.md) [✅](tasks/TFW-18__knowledge_consolidation/TS__PhaseB__knowledge_quality.md) | [✅](tasks/TFW-18__knowledge_consolidation/ONB__TFW-18__knowledge_consolidation.md) [✅](tasks/TFW-18__knowledge_consolidation/ONB__PhaseB__knowledge_quality.md) | [✅](tasks/TFW-18__knowledge_consolidation/REVIEW__TFW-18__knowledge_consolidation.md) [✅](tasks/TFW-18__knowledge_consolidation/REVIEW__PhaseB__knowledge_quality.md) |
| [TFW-19](tasks/TFW-19__config_propagation/) | tfw-config: propagate PROJECT_CONFIG.yaml changes to workflows/adapters automatically | ✅ DONE | [✅](tasks/TFW-19__config_propagation/HL-TFW-19__config_propagation.md) | [✅](tasks/TFW-19__config_propagation/RES__TFW-19__config_propagation.md) | [✅](tasks/TFW-19__config_propagation/TS__TFW-19__config_propagation.md) | [✅](tasks/TFW-19__config_propagation/ONB__TFW-19__config_propagation.md) | [✅](tasks/TFW-19__config_propagation/REVIEW__TFW-19__config_propagation.md) |
| TFW-20 | tfw-user-tune: personal preferences pipeline (.user_preferences.md lifecycle, gitignored, user-specific) | ⬜ TODO | | | | | |
| [TFW-21](tasks/TFW-21__research_workflow_compression/) | Compress research.md: 2397→1145 words (-52%), deduplicate, remove inline templates | ✅ DONE | [✅](tasks/TFW-21__research_workflow_compression/HL-TFW-21__research_workflow_compression.md) | [✅](tasks/TFW-21__research_workflow_compression/RES__TFW-21__research_workflow_compression.md) | [✅](tasks/TFW-21__research_workflow_compression/TS__TFW-21__research_workflow_compression.md) | [✅](tasks/TFW-21__research_workflow_compression/RF__TFW-21__research_workflow_compression.md) | [✅](tasks/TFW-21__research_workflow_compression/REVIEW__TFW-21__research_workflow_compression.md) |
| [TFW-22](tasks/TFW-22__coordinator_research_enrichment/) | Coordinator & Research enrichment: result visualization in HL, research justification, structured thinking algorithms | ✅ DONE | [✅](tasks/TFW-22__coordinator_research_enrichment/HL-TFW-22__coordinator_research_enrichment.md) | [✅](tasks/TFW-22__coordinator_research_enrichment/RES__TFW-22__coordinator_research_enrichment.md) | [✅](tasks/TFW-22__coordinator_research_enrichment/TS__TFW-22__coordinator_research_enrichment.md) | [✅](tasks/TFW-22__coordinator_research_enrichment/ONB__TFW-22__coordinator_research_enrichment.md) | [✅](tasks/TFW-22__coordinator_research_enrichment/REVIEW__TFW-22__coordinator_research_enrichment.md) |
| [TFW-23](tasks/TFW-23__templates_english_standardization/) | Templates English standardization: eliminate mixed RU/EN, pure English templates + content_language config | ✅ DONE | [✅](tasks/TFW-23__templates_english_standardization/HL-TFW-23__templates_english_standardization.md) | [✅](tasks/TFW-23__templates_english_standardization/RES__TFW-23__templates_english_standardization.md) | [✅](tasks/TFW-23__templates_english_standardization/TS__TFW-23__templates_english_standardization.md) | [✅](tasks/TFW-23__templates_english_standardization/ONB__TFW-23__templates_english_standardization.md) | [✅](tasks/TFW-23__templates_english_standardization/REVIEW__TFW-23__templates_english_standardization.md) |
| [TFW-24](tasks/TFW-24__res_state_machine/) | RES State Machine: Researcher role, subfolder state machine, resume protocol, HL Vision/Impact, Working Backwards | ✅ DONE | [✅](tasks/TFW-24__res_state_machine/HL-TFW-24__res_state_machine.md) | [✅](tasks/TFW-24__res_state_machine/RES__TFW-24__res_state_machine.md) | [A](tasks/TFW-24__res_state_machine/TS__TFW-24__res_state_machine.md) [B](tasks/TFW-24__res_state_machine/TS__PhaseB__research_templates.md) | [A](tasks/TFW-24__res_state_machine/ONB__TFW-24__res_state_machine.md) [B](tasks/TFW-24__res_state_machine/ONB__PhaseB__research_templates.md) | [A](tasks/TFW-24__res_state_machine/RF__TFW-24__res_state_machine.md) [B](tasks/TFW-24__res_state_machine/RF__PhaseB__research_templates.md) | [A](tasks/TFW-24__res_state_machine/REVIEW__TFW-24__res_state_machine.md) [B](tasks/TFW-24__res_state_machine/REVIEW__PhaseB__research_templates.md) |
| [TFW-25](tasks/TFW-25__values_consolidation/) | Values & Principles consolidation: enrich README Values, prune KNOWLEDGE.md, clean knowledge/ facts | ✅ DONE | [✅](tasks/TFW-25__values_consolidation/HL-TFW-25__values_consolidation.md) | [✅](tasks/TFW-25__values_consolidation/RES__TFW-25__values_consolidation.md) | [✅](tasks/TFW-25__values_consolidation/TS__TFW-25__values_consolidation.md) | [✅](tasks/TFW-25__values_consolidation/ONB__TFW-25__values_consolidation.md) | [✅](tasks/TFW-25__values_consolidation/RF__TFW-25__values_consolidation.md) | [✅](tasks/TFW-25__values_consolidation/REVIEW__TFW-25__values_consolidation.md) |
| [TFW-26](tasks/TFW-26__documentation_site/) | Documentation as Output: compilable contract, MkDocs gen-files, docs site from TFW artifacts | ✅ DONE | [✅](tasks/TFW-26__documentation_site/HL-TFW-26__documentation_site.md) | [✅](tasks/TFW-26__documentation_site/RES__TFW-26__documentation_site.md) | [FC](tasks/TFW-26__documentation_site/coordinator_fact_capture/TS__TFW-26__coordinator_fact_capture.md) [A](tasks/TFW-26__documentation_site/PhaseA/TS__PhaseA__compilable_contract.md) [B](tasks/TFW-26__documentation_site/PhaseB/TS__PhaseB__gen_docs_implementation.md) | [FC](tasks/TFW-26__documentation_site/coordinator_fact_capture/ONB__TFW-26__coordinator_fact_capture.md) [A](tasks/TFW-26__documentation_site/PhaseA/ONB__PhaseA__compilable_contract.md) [B](tasks/TFW-26__documentation_site/PhaseB/ONB__PhaseB__gen_docs_implementation.md) | [FC](tasks/TFW-26__documentation_site/coordinator_fact_capture/RF__TFW-26__coordinator_fact_capture.md) [A](tasks/TFW-26__documentation_site/PhaseA/RF__PhaseA__compilable_contract.md) [B](tasks/TFW-26__documentation_site/PhaseB/RF__PhaseB__gen_docs_implementation.md) | [FC](tasks/TFW-26__documentation_site/coordinator_fact_capture/REVIEW__TFW-26__coordinator_fact_capture.md) [A](tasks/TFW-26__documentation_site/PhaseA/REVIEW__PhaseA__compilable_contract.md) [B](tasks/TFW-26__documentation_site/PhaseB/REVIEW__PhaseB__gen_docs_implementation.md) |
| [TFW-27](tasks/TFW-27__wiki_polish_and_brand/) | Wiki polish & brand: logo, brand identity, link resolution, landing page, deploy to GitHub Pages | ✅ DONE | [✅](tasks/TFW-27__wiki_polish_and_brand/HL-TFW-27__wiki_polish_and_brand.md) | [A✅](tasks/TFW-27__wiki_polish_and_brand/PhaseA/TS__PhaseA__brand_identity.md) [B✅](tasks/TFW-27__wiki_polish_and_brand/PhaseB/TS__PhaseB__link_resolution.md) [C✅](tasks/TFW-27__wiki_polish_and_brand/PhaseC/TS__PhaseC__deploy.md) | [A✅](tasks/TFW-27__wiki_polish_and_brand/PhaseA/ONB__PhaseA__brand_identity.md) [B✅](tasks/TFW-27__wiki_polish_and_brand/PhaseB/ONB__PhaseB__link_resolution.md) [C✅](tasks/TFW-27__wiki_polish_and_brand/PhaseC/ONB__PhaseC__deploy.md) | [A✅](tasks/TFW-27__wiki_polish_and_brand/PhaseA/RF__PhaseA__brand_identity.md) [B✅](tasks/TFW-27__wiki_polish_and_brand/PhaseB/RF__PhaseB__link_resolution.md) [C✅](tasks/TFW-27__wiki_polish_and_brand/PhaseC/RF__PhaseC__deploy.md) | [A✅](tasks/TFW-27__wiki_polish_and_brand/PhaseA/REVIEW__PhaseA__brand_identity.md) [B✅](tasks/TFW-27__wiki_polish_and_brand/PhaseB/REVIEW__PhaseB__link_resolution.md) [C✅](tasks/TFW-27__wiki_polish_and_brand/PhaseC/REVIEW__PhaseC__deploy.md) |
| ~~TFW-28~~ | ~~Deploy docs~~ — absorbed into TFW-27/C | — | | | | | |
| [TFW-29](tasks/TFW-29__consistency_audit/) | Consistency audit: glossary, conventions, workflows — redundancy, compression, reading flows | ✅ DONE | [✅](tasks/TFW-29__consistency_audit/HL-TFW-29__consistency_audit.md) | [✅](tasks/TFW-29__consistency_audit/RES__TFW-29__consistency_audit.md) | [✅](tasks/TFW-29__consistency_audit/TS__TFW-29__consistency_audit.md) | [✅](tasks/TFW-29__consistency_audit/ONB__TFW-29__consistency_audit.md) | [✅](tasks/TFW-29__consistency_audit/RF__TFW-29__consistency_audit.md) | [✅](tasks/TFW-29__consistency_audit/REVIEW__TFW-29__consistency_audit.md) |
| ~~TFW-30~~ | ~~Antigravity adapter audit~~ — absorbed into TFW-45/C | — | | | | | |
| [TFW-31](tasks/TFW-31__quick_start_agent_first/) | Quick Start agent-first rewrite: quickstart.md, starter prompts, init.md domain-agnostic | ✅ DONE | [✅](tasks/TFW-31__quick_start_agent_first/HL-TFW-31__quick_start_agent_first.md) | [✅](tasks/TFW-31__quick_start_agent_first/TS__TFW-31__quick_start_agent_first.md) | [✅](tasks/TFW-31__quick_start_agent_first/ONB__TFW-31__quick_start_agent_first.md) | [✅](tasks/TFW-31__quick_start_agent_first/RF__TFW-31__quick_start_agent_first.md) | [✅](tasks/TFW-31__quick_start_agent_first/REVIEW__TFW-31__quick_start_agent_first.md) |
| [TFW-32](tasks/TFW-32__methodology_and_positioning/) | Methodology refinement & product positioning: docs/knowledge fix, KNW status, terminology, multi-iter research, audience personas | ✅ DONE | [✅](tasks/TFW-32__methodology_and_positioning/HL-TFW-32__methodology_and_positioning.md) | [A](tasks/TFW-32__methodology_and_positioning/PhaseA/TS__PhaseA__methodology_pipeline.md) [B](tasks/TFW-32__methodology_and_positioning/PhaseB/TS__PhaseB__naming_and_templates.md) [C](tasks/TFW-32__methodology_and_positioning/PhaseC/TS__PhaseC__multi_iteration_research.md) [D](tasks/TFW-32__methodology_and_positioning/PhaseD/TS__PhaseD__positioning_and_messaging.md) | [A](tasks/TFW-32__methodology_and_positioning/PhaseA/ONB__PhaseA__methodology_pipeline.md) [B](tasks/TFW-32__methodology_and_positioning/PhaseB/ONB__PhaseB__naming_and_templates.md) [C](tasks/TFW-32__methodology_and_positioning/PhaseC/ONB__PhaseC__multi_iteration_research.md) [D](tasks/TFW-32__methodology_and_positioning/PhaseD/ONB__PhaseD__positioning_and_messaging.md) | [A](tasks/TFW-32__methodology_and_positioning/PhaseA/RF__PhaseA__methodology_pipeline.md) [B](tasks/TFW-32__methodology_and_positioning/PhaseB/RF__PhaseB__naming_and_templates.md) [C](tasks/TFW-32__methodology_and_positioning/PhaseC/RF__PhaseC__multi_iteration_research.md) [D](tasks/TFW-32__methodology_and_positioning/PhaseD/RF__PhaseD__positioning_and_messaging.md) | [A](tasks/TFW-32__methodology_and_positioning/PhaseA/REVIEW__PhaseA__methodology_pipeline.md) [B](tasks/TFW-32__methodology_and_positioning/PhaseB/REVIEW__PhaseB__naming_and_templates.md) [C](tasks/TFW-32__methodology_and_positioning/PhaseC/REVIEW__PhaseC__multi_iteration_research.md) [D](tasks/TFW-32__methodology_and_positioning/PhaseD/REVIEW__PhaseD__positioning_and_messaging.md) |
| TFW-33 | Thinking traces as first-class TFW artifacts (capture AI `<think>` blocks as project knowledge) | ⬜ TODO | | | | | |
| TFW-34 | Knowledge pipeline automation: plugin-based fact capture, handoff manifest (task_state.yaml) | ⬜ TODO | | | | | |
| TFW-35 | Analytical review template: lighter checklist for non-code phases (positioning, specs, documentation) | ⬜ TODO | | | | | |
| [TFW-36](tasks/TFW-36__content_marketing_blog_series/) | Content marketing blog series: 7 Medium posts targeting different audiences via SEO, problem-first with real cases | 📚 KNW (A) | [📝](tasks/TFW-36__content_marketing_blog_series/HL-TFW-36__content_marketing_blog_series.md) | [🔬](tasks/TFW-36__content_marketing_blog_series/RES__TFW-36__content_marketing_blog_series.md) | [🟡](tasks/TFW-36__content_marketing_blog_series/PhaseA/TS__PhaseA__content_strategy_and_post3.md) | [🟠](tasks/TFW-36__content_marketing_blog_series/PhaseA/ONB__PhaseA__content_strategy_and_post3.md) | [🔍](tasks/TFW-36__content_marketing_blog_series/PhaseA/REVIEW__PhaseA__content_strategy_and_post3.md) |
| ~~TFW-37~~ | ~~Source Audit gate~~ — absorbed into TFW-38 (4-stage review + Trust Protocol + docs mode source verification) | — | | | | | |
| [TFW-38](tasks/TFW-38__quality_enforcement/) | Quality enforcement: staged review (Map→Verify→Judge→Decide), handoff §6-8 mandate, knowledge citation table | ✅ DONE | [✅](tasks/TFW-38__quality_enforcement/HL-TFW-38__quality_enforcement.md) | [✅](tasks/TFW-38__quality_enforcement/RES__TFW-38__quality_enforcement.md) | [A✅](tasks/TFW-38__quality_enforcement/PhaseA/TS__PhaseA__review_restructure.md) [A.2✅](tasks/TFW-38__quality_enforcement/PhaseA/TS__PhaseA2__review_stage_files.md) [B✅](tasks/TFW-38__quality_enforcement/PhaseB/TS__PhaseB__knowledge_citation_table.md) | [A🟠](tasks/TFW-38__quality_enforcement/PhaseA/ONB__PhaseA__review_restructure.md) [A.2🟠](tasks/TFW-38__quality_enforcement/PhaseA/ONB__PhaseA2__review_stage_files.md) [B🟠](tasks/TFW-38__quality_enforcement/PhaseB/ONB__PhaseB__knowledge_citation_table.md) | [A🟢](tasks/TFW-38__quality_enforcement/PhaseA/RF__PhaseA__review_restructure.md) [A.2🟢](tasks/TFW-38__quality_enforcement/PhaseA/RF__PhaseA2__review_stage_files.md) [B🟢](tasks/TFW-38__quality_enforcement/PhaseB/RF__PhaseB__knowledge_citation_table.md) | [A✅](tasks/TFW-38__quality_enforcement/PhaseA/REVIEW__PhaseA__review_restructure.md) [A.2✅](tasks/TFW-38__quality_enforcement/PhaseA/REVIEW__PhaseA2__review_stage_files.md) [B✅](tasks/TFW-38__quality_enforcement/PhaseB/REVIEW__PhaseB__knowledge_citation_table.md) |
| TFW-39 | Visual Knowledge System: process/architecture diagram registry with naming convention, mandatory creation criteria, staleness tracking, domain index. Born from TFW-38 Phase B redesign | ⬜ TODO | | | | | |
| [TFW-40](tasks/TFW-40__state_separation/) | State/framework separation: knowledge_state.yaml contamination fix, project_config template, naming normalization | ✅ DONE | [✅](tasks/TFW-40__state_separation/HL-TFW-40__state_separation.md) | | [A](tasks/TFW-40__state_separation/TS__PhaseA__state_separation.md) [B](tasks/TFW-40__state_separation/TS__PhaseB__naming_normalization.md) | [A](tasks/TFW-40__state_separation/ONB__PhaseA__state_separation.md) [B](tasks/TFW-40__state_separation/ONB__PhaseB__naming_normalization.md) | [A](tasks/TFW-40__state_separation/RF__PhaseA__state_separation.md) [B](tasks/TFW-40__state_separation/RF__PhaseB__naming_normalization.md) | [A](tasks/TFW-40__state_separation/REVIEW__PhaseA__state_separation.md) [B](tasks/TFW-40__state_separation/REVIEW__PhaseB__naming_normalization.md) |
| [TFW-41](tasks/TFW-41__execution_quality_gates/) | Execution quality gates: Requirements-first TS, Execution Loops, Pre-TS/Pre-RF gates, principles enforcement, embedded dimensional analysis | ✅ DONE | [✅](tasks/TFW-41__execution_quality_gates/HL-TFW-41__execution_quality_gates.md) | [1](tasks/TFW-41__execution_quality_gates/RES__TFW-41__execution_quality_gates.md) [2](tasks/TFW-41__execution_quality_gates/RES__iter2__execution_quality_gates.md) | [A🟡](tasks/TFW-41__execution_quality_gates/PhaseA/TS__PhaseA__templates_and_conventions.md) [B🟡](tasks/TFW-41__execution_quality_gates/PhaseB/TS__PhaseB__workflow_gates.md) [C🟡](tasks/TFW-41__execution_quality_gates/PhaseC/TS__PhaseC__research_templates.md) [D🟡](tasks/TFW-41__execution_quality_gates/PhaseD/TS__PhaseD__glossary_and_adapters.md) | [A🟠](tasks/TFW-41__execution_quality_gates/PhaseA/ONB__PhaseA__templates_and_conventions.md) [B🟠](tasks/TFW-41__execution_quality_gates/PhaseB/ONB__PhaseB__workflow_gates.md) [C🟠](tasks/TFW-41__execution_quality_gates/PhaseC/ONB__PhaseC__research_templates.md) [D🟠](tasks/TFW-41__execution_quality_gates/PhaseD/ONB__PhaseD__glossary_and_adapters.md) | [A🟢](tasks/TFW-41__execution_quality_gates/PhaseA/RF__PhaseA__templates_and_conventions.md) [B🟢](tasks/TFW-41__execution_quality_gates/PhaseB/RF__PhaseB__workflow_gates.md) [C🟢](tasks/TFW-41__execution_quality_gates/PhaseC/RF__PhaseC__research_templates.md) [D🟢](tasks/TFW-41__execution_quality_gates/PhaseD/RF__PhaseD__glossary_and_adapters.md) | [A✅](tasks/TFW-41__execution_quality_gates/PhaseA/REVIEW__PhaseA__templates_and_conventions.md) [B✅](tasks/TFW-41__execution_quality_gates/PhaseB/REVIEW__PhaseB__workflow_gates.md) [C✅](tasks/TFW-41__execution_quality_gates/PhaseC/REVIEW__PhaseC__research_templates.md) [D✅](tasks/TFW-41__execution_quality_gates/PhaseD/REVIEW__PhaseD__glossary_and_adapters.md) |
| [TFW-42](tasks/TFW-42__research_cycle_restructure/) | Research cycle restructure: unified research/ container, numbered stages, kebab-case phases, iterations.yaml enrichment, multi-agent support | ✅ DONE | [✅](tasks/TFW-42__research_cycle_restructure/HL-TFW-42__research_cycle_restructure.md) | [1](tasks/TFW-42__research_cycle_restructure/research/RES__TFW-42__research_cycle_restructure.md) [2](tasks/TFW-42__research_cycle_restructure/research2/RES__iter2__agent_guidance.md) | [A🟡](tasks/TFW-42__research_cycle_restructure/phase-a/TS__phase-a__conventions_and_templates.md) [B🟡](tasks/TFW-42__research_cycle_restructure/phase-b/TS__phase-b__workflow_updates.md) [C🟡](tasks/TFW-42__research_cycle_restructure/phase-c/TS__phase-c__glossary_and_adapters.md) | [A🟠](tasks/TFW-42__research_cycle_restructure/phase-a/ONB__phase-a__conventions_and_templates.md) [B🟠](tasks/TFW-42__research_cycle_restructure/phase-b/ONB__phase-b__workflow_updates.md) [C🟠](tasks/TFW-42__research_cycle_restructure/phase-c/ONB__phase-c__glossary_and_adapters.md) | [A🟢](tasks/TFW-42__research_cycle_restructure/phase-a/RF__phase-a__conventions_and_templates.md) [B🟢](tasks/TFW-42__research_cycle_restructure/phase-b/RF__phase-b__workflow_updates.md) [C🟢](tasks/TFW-42__research_cycle_restructure/phase-c/RF__phase-c__glossary_and_adapters.md) | [A✅](tasks/TFW-42__research_cycle_restructure/phase-a/REVIEW__phase-a__conventions_and_templates.md) [B✅](tasks/TFW-42__research_cycle_restructure/phase-b/REVIEW__phase-b__workflow_updates.md) [C✅](tasks/TFW-42__research_cycle_restructure/phase-c/REVIEW__phase-c__glossary_and_adapters.md) |
| [TFW-43](tasks/TFW-43__research_stage_protocol/) | Research stage protocol: copy-on-enter, per-stage mindset blocks, STOP gates between stages | ✅ DONE | [✅](tasks/TFW-43__research_stage_protocol/HL-TFW-43__research_stage_protocol.md) | [1](tasks/TFW-43__research_stage_protocol/research/iter1/RES.md) | [🟡](tasks/TFW-43__research_stage_protocol/TS-TFW-43__research_stage_protocol.md) | [🟠](tasks/TFW-43__research_stage_protocol/ONB-TFW-43__research_stage_protocol.md) | [🟢](tasks/TFW-43__research_stage_protocol/RF-TFW-43__research_stage_protocol.md) | [✅](tasks/TFW-43__research_stage_protocol/REVIEW-TFW-43__research_stage_protocol.md) |
| [TFW-44](tasks/TFW-44__coordinator_quality_gates/) | Coordinator quality gates: insight→AC traceability, 1 req = 1 AC, floor+ceiling DoF, KI cleanup | 📝 HL_DRAFT | [📝](tasks/TFW-44__coordinator_quality_gates/HL-TFW-44__coordinator_quality_gates.md) | | | | | |
| [TFW-45](tasks/TFW-45__multi_agent_workflows/) | Multi-agent investigative workflows: swarm mode for research/review + Antigravity adapter overhaul (absorbs TFW-30). [Review-consolidator addendum](tasks/TFW-45__multi_agent_workflows/PROPOSAL__TFW-45__review_swarm_consolidator.md) — delegation topology, blocked by TFW-53/C | ❄️ FROZEN | [📝](tasks/TFW-45__multi_agent_workflows/HL-TFW-45__multi_agent_workflows.md) | | | | | |
| [TFW-46](tasks/TFW-46__evidence_layer/) | Evidence Layer: live verification evidence as first-class artifact — Evidence Plan (TS), Evidence Collection (RF), Evidence Audit (REVIEW) | ✅ DONE | [✅](tasks/TFW-46__evidence_layer/HL-TFW-46__evidence_layer.md) | [1](tasks/TFW-46__evidence_layer/research/iter1/RES.md) [2](tasks/TFW-46__evidence_layer/research/iter2/RES.md) | [A🟡](tasks/TFW-46__evidence_layer/phase-a/TS__phase-a__evidence_templates.md) [B🟡](tasks/TFW-46__evidence_layer/phase-b/TS__phase-b__workflow_integration.md) [C🟡](tasks/TFW-46__evidence_layer/phase-c/TS__phase-c__glossary_and_version.md) | [A🟠](tasks/TFW-46__evidence_layer/phase-a/ONB__phase-a__evidence_templates.md) [B🟠](tasks/TFW-46__evidence_layer/phase-b/ONB__phase-b__workflow_integration.md) [C🟠](tasks/TFW-46__evidence_layer/phase-c/ONB__phase-c__glossary_and_version.md) | [A🟢](tasks/TFW-46__evidence_layer/phase-a/RF__phase-a__evidence_templates.md) [B🟢](tasks/TFW-46__evidence_layer/phase-b/RF__phase-b__workflow_integration.md) [C🟢](tasks/TFW-46__evidence_layer/phase-c/RF__phase-c__glossary_and_version.md) | [A✅](tasks/TFW-46__evidence_layer/phase-a/REVIEW__phase-a__evidence_templates.md) [B✅](tasks/TFW-46__evidence_layer/phase-b/REVIEW__phase-b__workflow_integration.md) [C✅](tasks/TFW-46__evidence_layer/phase-c/REVIEW__phase-c__glossary_and_version.md) |
| [TFW-47](tasks/TFW-47__codex_adapter_shortcut_skills/) | Evidence enforcement & Codex adapter: mandatory `evidence/` folder + first-class Codex integration with dedicated `tfw-*` skills | ✅ DONE | [✅](tasks/TFW-47__codex_adapter_shortcut_skills/HL-TFW-47__codex_adapter_shortcut_skills.md) | [1](tasks/TFW-47__codex_adapter_shortcut_skills/research/iter1/RES.md) [2](tasks/TFW-47__codex_adapter_shortcut_skills/research/iter2/RES.md) | [A🟡](tasks/TFW-47__codex_adapter_shortcut_skills/phase-a/TS__phase-a__evidence_enforcement.md) [B🟡](tasks/TFW-47__codex_adapter_shortcut_skills/phase-b/TS__phase-b__codex_adapter.md) | [A🟠](tasks/TFW-47__codex_adapter_shortcut_skills/phase-a/ONB__phase-a__evidence_enforcement.md) [B🟠](tasks/TFW-47__codex_adapter_shortcut_skills/phase-b/ONB__phase-b__codex_adapter.md) | [A🟢](tasks/TFW-47__codex_adapter_shortcut_skills/phase-a/RF__phase-a__evidence_enforcement.md) [B🟢](tasks/TFW-47__codex_adapter_shortcut_skills/phase-b/RF__phase-b__codex_adapter.md) | [A✅](tasks/TFW-47__codex_adapter_shortcut_skills/phase-a/REVIEW__phase-a__evidence_enforcement.md) [B✅](tasks/TFW-47__codex_adapter_shortcut_skills/phase-b/REVIEW__phase-b__codex_adapter.md) |
| [TFW-48](tasks/TFW-48__value_first_methodology_rebaseline/) | Value-first methodology rebaseline: refactor TFW from product goals, values, and production learning | ❌ REJECTED — rejected experiment in delegating methodology redesign to Codex without sufficient human supervision; status **assigned** 2026-08-18, not restored (last live status was 🟡 TS (D)) | — | — | — | — | — | [post-mortem](tasks/TFW-48__value_first_methodology_rebaseline/POSTMORTEM__TFW-48.md) |
| [TFW-49](tasks/TFW-49__agent_commit_identity_and_attribution/) | Agent commit identity and attribution: searchable task, phase, role, and agent provenance | ❌ REJECTED — complete product-fit failure; superseded by TFW-50 | — | — | — | — | — | [post-mortem](tasks/TFW-49__agent_commit_identity_and_attribution/POSTMORTEM__TFW-49.md) |
| [TFW-50](tasks/TFW-50__minimal_agent_commit_attribution/) | Minimal agent commit attribution: one readable subject rule, no runtime | ✅ DONE | [✅](tasks/TFW-50__minimal_agent_commit_attribution/HL-TFW-50__minimal_agent_commit_attribution.md) | [✅](tasks/TFW-50__minimal_agent_commit_attribution/TS__TFW-50__minimal_agent_commit_attribution.md) | [✅](tasks/TFW-50__minimal_agent_commit_attribution/ONB__TFW-50__minimal_agent_commit_attribution.md) | [🟢](tasks/TFW-50__minimal_agent_commit_attribution/RF__TFW-50__minimal_agent_commit_attribution.md) | [✅](tasks/TFW-50__minimal_agent_commit_attribution/REVIEW__TFW-50__minimal_agent_commit_attribution.md) |
| [TFW-51](tasks/TFW-51__tfw_light_ru/) | TFW Light RU: four-file domain-agnostic starter for AI workshops and non-code work | ✅ DONE | [✅](tasks/TFW-51__tfw_light_ru/HL-TFW-51__tfw_light_ru.md) | — | — | — | [Owner-confirmed exception](tasks/TFW-51__tfw_light_ru/HL-TFW-51__tfw_light_ru.md#0-retrospective-closure-context) |
| [TFW-52](tasks/TFW-52__tfw_light_v1/) | TFW Editions: three compatible editions for different work complexity and education — manual Light, Codex-assisted discipline, existing Full. Team excluded after research → [TFW-54](tasks/TFW-54__agent_team_mode/) | ✅ DONE ([owner-confirmed closure](tasks/TFW-52__tfw_light_v1/HL-TFW-52__tfw_light_v1.md#0-closure-context); Phase B REVIEW waived, hooks runtime blocked → TD-126) | [✅](tasks/TFW-52__tfw_light_v1/HL-TFW-52__tfw_light_v1.md) | [1](tasks/TFW-52__tfw_light_v1/research/iter1/RES.md) [2](tasks/TFW-52__tfw_light_v1/research/iter2/RES.md) [3](tasks/TFW-52__tfw_light_v1/research/iter3/RES.md) | [A✅](tasks/TFW-52__tfw_light_v1/phase-a/TS__phase-a__product_line_and_light.md) [B✅](tasks/TFW-52__tfw_light_v1/phase-b/TS__phase-b__assisted.md) | [A🟠](tasks/TFW-52__tfw_light_v1/phase-a/ONB__phase-a__product_line_and_light.md) [B🟠](tasks/TFW-52__tfw_light_v1/phase-b/ONB__phase-b__assisted.md) | [A🟢](tasks/TFW-52__tfw_light_v1/phase-a/RF__phase-a__product_line_and_light.md) [B🟢](tasks/TFW-52__tfw_light_v1/phase-b/RF__phase-b__assisted.md) | [A✅](tasks/TFW-52__tfw_light_v1/phase-a/REVIEW__phase-a__product_line_and_light.md) [B — waived by owner](tasks/TFW-52__tfw_light_v1/HL-TFW-52__tfw_light_v1.md#0-closure-context) |
| [TFW-53](tasks/TFW-53__hl_contract_and_goal_defence/) | HL as strategic contract: frozen sections, amendment log, research proposes instead of rewrites + reviewer defends goals/north star + rejected-trace restoration | ✅ DONE | [✅](tasks/TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md) | [1](tasks/TFW-53__hl_contract_and_goal_defence/research/iter1/RES.md) [2](tasks/TFW-53__hl_contract_and_goal_defence/research/iter2/RES.md) | [A🟡](tasks/TFW-53__hl_contract_and_goal_defence/phase-a/TS__phase-a__contract_in_artifacts.md) [B🟡](tasks/TFW-53__hl_contract_and_goal_defence/phase-b/TS__phase-b__enforcement_in_workflows.md) [C🟡](tasks/TFW-53__hl_contract_and_goal_defence/phase-c/TS__phase-c__goal_defence_in_review.md) [D🟡](tasks/TFW-53__hl_contract_and_goal_defence/phase-d/TS__phase-d__glossary_adapters_version.md) [E🟡](tasks/TFW-53__hl_contract_and_goal_defence/phase-e/TS__phase-e__rejected_trace_restoration.md) | [A🟠](tasks/TFW-53__hl_contract_and_goal_defence/phase-a/ONB__phase-a__contract_in_artifacts.md) [B🟠](tasks/TFW-53__hl_contract_and_goal_defence/phase-b/ONB__phase-b__enforcement_in_workflows.md) [C🟠](tasks/TFW-53__hl_contract_and_goal_defence/phase-c/ONB__phase-c__goal_defence_in_review.md) [D🟠](tasks/TFW-53__hl_contract_and_goal_defence/phase-d/ONB__phase-d__glossary_adapters_version.md) [E🟠](tasks/TFW-53__hl_contract_and_goal_defence/phase-e/ONB__phase-e__rejected_trace_restoration.md) | [A🟢](tasks/TFW-53__hl_contract_and_goal_defence/phase-a/RF__phase-a__contract_in_artifacts.md) [B🟢](tasks/TFW-53__hl_contract_and_goal_defence/phase-b/RF__phase-b__enforcement_in_workflows.md) [C🟢](tasks/TFW-53__hl_contract_and_goal_defence/phase-c/RF__phase-c__goal_defence_in_review.md) [D🟢](tasks/TFW-53__hl_contract_and_goal_defence/phase-d/RF__phase-d__glossary_adapters_version.md) [E🟢](tasks/TFW-53__hl_contract_and_goal_defence/phase-e/RF__phase-e__rejected_trace_restoration.md) | [A✅](tasks/TFW-53__hl_contract_and_goal_defence/phase-a/REVIEW__phase-a__contract_in_artifacts.md) [B✅](tasks/TFW-53__hl_contract_and_goal_defence/phase-b/REVIEW__phase-b__enforcement_in_workflows.md) [C✅](tasks/TFW-53__hl_contract_and_goal_defence/phase-c/REVIEW__phase-c__goal_defence_in_review.md) [D✅](tasks/TFW-53__hl_contract_and_goal_defence/phase-d/REVIEW__phase-d__glossary_adapters_version.md) [E✅](tasks/TFW-53__hl_contract_and_goal_defence/phase-e/REVIEW__phase-e__rejected_trace_restoration.md) |
| [TFW-54](tasks/TFW-54__agent_team_mode/) | AT (Agent Team) execution mode: a coordinator runs a team of delegate sessions inside the frozen contract — a frozen per-task role table in the HL, whole-workflow-only delegation, cross-session trace integrity (closes TD-144, TD-178), graceful tool degradation. No runtime, no journal, no new artifact class. [Proposal](tasks/TFW-54__agent_team_mode/PROPOSAL__TFW-54__agent_team_mode.md) | 📝 HL_DRAFT | [📝](tasks/TFW-54__agent_team_mode/HL-TFW-54__agent_team_mode.md) | | | | | |
| [TFW-55](tasks/TFW-55__canonization_program/) | TFW Foundations: establish the Philosophy of Trace → TFW methodology architecture, write the Project North Star essay, then restore and localize the practical project README | 📚 KNW (B.2) — REVIEW APPROVE; coordinator owns post-APPROVE docs closure | [✅](tasks/TFW-55__canonization_program/HL-TFW-55__canonization_program.md) | [1](tasks/TFW-55__canonization_program/research/iter1/RES.md) [2](tasks/TFW-55__canonization_program/research/iter2/RES.md) | [A🟡](tasks/TFW-55__canonization_program/phase-a/TS__phase-a__canonical_foundation_essay.md) [B1 superseded](tasks/TFW-55__canonization_program/phase-b/TS__phase-b__multilingual_public_entry.md) [B.2🟡](tasks/TFW-55__canonization_program/phase-b/TS__phase-b2__project_readme_localization.md) | [A🟠](tasks/TFW-55__canonization_program/phase-a/ONB__phase-a__canonical_foundation_essay.md) [B1 superseded](tasks/TFW-55__canonization_program/phase-b/ONB__phase-b__multilingual_public_entry.md) [B.2🟠](tasks/TFW-55__canonization_program/phase-b/ONB__phase-b2__project_readme_localization.md) | [A🟢](tasks/TFW-55__canonization_program/phase-a/RF__phase-a__canonical_foundation_essay.md) [B1 superseded](tasks/TFW-55__canonization_program/phase-b/RF__phase-b__multilingual_public_entry.md) [B.2🟢](tasks/TFW-55__canonization_program/phase-b/RF__phase-b2__project_readme_localization.md) | [A✅](tasks/TFW-55__canonization_program/phase-a/REVIEW__phase-a__canonical_foundation_essay.md) [B1 superseded by owner rejection](tasks/TFW-55__canonization_program/phase-b/REVIEW__phase-b__multilingual_public_entry.md) [B.2✅](tasks/TFW-55__canonization_program/phase-b/REVIEW__phase-b2__project_readme_localization.md) |
| [TFW-56](tasks/TFW-56__review_mode_removal/) | Remove the review mode **selection** (`code`/`docs`/`spec`): delete the gate, the config key and three mode files; promote the gated checks into the universal Judge checklist — evidence sufficiency, compatibility, safety, design soundness | ✅ DONE | [✅](tasks/TFW-56__review_mode_removal/HL-TFW-56__review_mode_removal.md) | [1](tasks/TFW-56__review_mode_removal/research/iter1/RES.md) | [🟡](tasks/TFW-56__review_mode_removal/TS__TFW-56__review_mode_removal.md) | [🟠](tasks/TFW-56__review_mode_removal/ONB__TFW-56__review_mode_removal.md) | [🟢](tasks/TFW-56__review_mode_removal/RF__TFW-56__review_mode_removal.md) | [✅](tasks/TFW-56__review_mode_removal/REVIEW__TFW-56__review_mode_removal.md) |
| [TFW-57](tasks/TFW-57__artifact_growth_control/) | Artifact growth control: a checkpoint that reads the budgets already configured, numbers for the three classes that have none, and a rule that a corrective pass may not grow the artifact it corrects. Covers README, TECH_DEBT.md and KNOWLEDGE.md. [Proposal](tasks/TFW-57__artifact_growth_control/PROPOSAL__TFW-57__artifact_growth_control.md) | ⬜ TODO | | | | | |
| [TFW-58](tasks/TFW-58__revise_protocol/) | What happens after a REVISE: who is in the loop, revision-in-place vs new phase, loop termination, handoff re-entry. [Proposal](tasks/TFW-58__revise_protocol/PROPOSAL__TFW-58__revise_protocol.md); sequenced after TFW-53 Phase C | ⬜ TODO | | | | | |
| [TFW-59](tasks/TFW-59__north_star_lifecycle/) | North Star lifecycle: who designates it, where it is recorded once, who asks when it is missing, and how work is routed into a frozen contract. TFW-53/C shipped the concept with no life around it — `north star` appears 0 times in `plan.md` and 0 in `init.md`, there is no config key, and the only carrier is a per-HL field. [Proposal](tasks/TFW-59__north_star_lifecycle/PROPOSAL__TFW-59__north_star_lifecycle.md); the designation itself is TFW-55 A2 | ⬜ TODO | | | | | |
| [TFW-60](tasks/TFW-60__conflict_resistant_shared_workspace/) | Conflict-resistant shared workspace: task-local state, coordination, debt and knowledge for concurrent humans and agents using file sync and Git | 🔬 RES — SUFFICIENT (A) | [✅](tasks/TFW-60__conflict_resistant_shared_workspace/HL-TFW-60__conflict_resistant_shared_workspace.md) | [1](tasks/TFW-60__conflict_resistant_shared_workspace/research/iter1/RES.md) [2](tasks/TFW-60__conflict_resistant_shared_workspace/research/iter2/RES.md) | | | | |

> Statuses: ⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE | ❌ BLOCKED (waiting) | ❌ REJECTED (closed unsuccessfully, trace kept)
