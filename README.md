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
| 🔄 | **Resume from a checkpoint** | A person or agent reads the task's own state file, its journal and the relevant traces, verifies the recorded state, and continues from an explicit handoff instead of relying on a vanished chat |
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
| `README.md` | Practical project guide and the route to the portfolio index |
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

The complete Full lifecycle is visible in each task's state, journal and trace files:

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
| 🧾 History and evidence | [Portfolio index](workspace/00-INDEX.md) · [`tasks/`](tasks/README.md) · [Verified knowledge](KNOWLEDGE.md) · [Changelog](.tfw/CHANGELOG.md) |
| 🤖 Interactive help | [NotebookLM FAQ](https://notebooklm.google.com/notebook/0a4cc544-0c0a-4fb0-b7ae-f075625d0980) |
| 🎓 Visual introduction | [Onboarding slides](https://notebooklm.google.com/notebook/0a4cc544-0c0a-4fb0-b7ae-f075625d0980?artifactId=e274558e-7d56-45ea-b2e7-efc7f6ccdf46) · [Video overview](https://notebooklm.google.com/notebook/0a4cc544-0c0a-4fb0-b7ae-f075625d0980?artifactId=f800b95b-aefb-4447-a9c9-42adb5455e45) |
| 🌐 Documentation | [tfw.saubakirov.kz](https://tfw.saubakirov.kz/) |
| 🔗 Repository | [github.com/saubakirov/trace-first-starter](https://github.com/saubakirov/trace-first-starter) |
| 👤 Author | [saubakirov.kz](https://saubakirov.kz/) |
| ⚖️ License | [MIT](LICENSE) |

---
## Where the work is

Tasks live in their own folders, and each one carries its own state. Nothing here has to be
edited to move a task forward — that is the point.

**[→ Portfolio index](workspace/00-INDEX.md)** — what is in flight, what closed, what is
waiting to be picked up. Rebuilt from task state by `python .tfw/scripts/gen_index.py`; it
is a view, not the record.

| Where | What it holds |
|---|---|
| [`workspace/`](workspace/00-INDEX.md) | tasks created from 2.0.0 on, nested by creation year |
| [`tasks/`](tasks/README.md) | the pre-2.0.0 corpus, paths unchanged and never renamed |
| [`team/`](team/README.md) | who may act — humans and agents, one profile each |
| [`tasks/BOARD-SNAPSHOT.md`](tasks/BOARD-SNAPSHOT.md) | the Task Board as it stood the day it was retired |

Inside a task folder, `status.md` is the only authority for that task's live state and
`journal/` is the record of how it got there — one immutable file per event. The status
vocabulary is in [`.tfw/glossary.md`](.tfw/glossary.md).

> Before 2.0.0 this section was a live table that every lifecycle transition rewrote. Two
> people advancing two unrelated tasks edited the same file and collided over work that had
> nothing to do with each other. Removing it is what TFW-60 was for.
