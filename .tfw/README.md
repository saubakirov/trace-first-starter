# Trace-First Workflow (TFW)

> *"The thought process and the instructions are more valuable than the immediate result."*

---

## The Problem: Knowledge Evaporates

Most work with AI happens in dialogue. You explain the project. You negotiate constraints. You make trade-offs. The AI produces something useful. And then the chat ends.

Tomorrow you open a new session. The context is gone. You re-explain everything from scratch. The model doesn't remember your architecture, your naming conventions, why you chose one technology over another, which algorithm fit the constraints, or the three approaches you already rejected. You start over.

This is not a minor annoyance — it is the fundamental bottleneck of AI-assisted work.

**The symptoms are everywhere:**
- Threads branch and drift. There is no single source of truth.
- You keep answering "what is this project again?" in every new chat.
- Model resets and forced new sessions wipe working memory.
- Context windows silently truncate key decisions.
- Deliverables ship without the "why" — making them hard to maintain or evolve.
- Agents waste tokens re-reading long, unstructured histories.

**The common fixes don't work:**
- **One giant prompt** becomes brittle, expensive, and stale within days.
- **Pinned notes** without a ritual decay into uncurated scrapbooks nobody reads.
- **Chat exports** are linear blobs — impossible to search, impossible to use for onboarding a new agent.

What's needed is not a better tool. It's a better **discipline**.

---

## The Thesis: Traces Over Code

Trace-First Workflow is built on a simple observation:

**The most valuable artifact of any AI session is not the code or the document it produces. It is the trace — the record of intent, decisions, constraints, and rejected alternatives that led to the result.**

Code can be regenerated. A well-structured prompt with the right context will produce the same output again and again. But the *reasoning* behind the prompt — why you asked for this, what you tried before, what constraints you imposed — that is the irreplaceable knowledge that makes future work possible.

TFW inverts the traditional priority:

| Traditional | Trace-First |
|:--|:--|
| Code is the artifact; docs are an afterthought | Traces are the artifact; code is a reproducible output |
| Context lives in the developer's head | Context lives in files that any agent or human can read |
| Onboarding = "read the codebase" | Onboarding = read AGENTS → STEPS → TASK |
| New chat = start from zero | New chat = load traces, resume from last checkpoint |

This is closely related to the **AI-First** philosophy: if AI is going to produce most of the code, then the architecture, the processes, and the knowledge must be organized for the AI, not just for the human developer. The human's job shifts from *writing* code to *managing* the context that the AI needs to produce correct code.

TFW is the methodology for that management.

---

## How It Works

TFW is a ritual with a predictable structure and one unbreakable rule.

### Project Structure

Every project — whether it's a codebase, a report, a data analysis, or a contract — follows the same layout:

```
project-root/
├── README.md          # Human guide: why/what/how + Task Board
├── AGENTS.md          # AI role, behavior, operating modes
├── TASK.md            # Scope, boundaries, DoD, risks
├── STEPS.md           # Chronological log of Summary lines
├── TECH_DEBT.md       # Accumulated tech debt from reviews
├── .tfw/              # TFW core (tool-agnostic)
│   ├── README.md      # TFW philosophy and ritual (this file)
│   ├── conventions.md # Formal rules and standards
│   ├── glossary.md    # Terminology
│   ├── templates/     # HL, TS, RF, ONB, REVIEW templates
│   ├── workflows/     # Canonical workflows (plan, handoff, resume)
│   ├── adapters/      # Tool adapter templates (Claude Code, Cursor, Antigravity)
│   └── PROJECT_CONFIG.yaml
└── tasks/             # Task artifacts organized by ID
```

The `.tfw/` directory is the heart of v3. It is **tool-agnostic** — the same `.tfw/` works whether you use Claude Code, Cursor, Antigravity, or a plain chat window. Each development tool reads its own entry point (e.g., `CLAUDE.md`, `.cursor/rules`), which simply references `.tfw/` as the single source of truth.

### The Context Loading Order

An AI agent entering a new session reads files in this exact sequence:

```
AGENTS.md → STEPS.md → TASK.md → .tfw/conventions.md → relevant task files
```

Role context first. Then progress history. Then scope. Then rules. This order gives the agent the minimum necessary knowledge to become productive — fast and token-efficient.

### The One Rule: Summary Discipline

Every significant AI reply ends with exactly one Summary line. No exceptions.

```
[2026-02-25] Summary: Stage=Implementation | Iteration=4 | Goal=Refactor auth module | Task=Extract JWT logic | Status=Done
```

This line is appended to `STEPS.md`. Over time, STEPS becomes the project's memory — a searchable, chronological record of everything that happened. When you start a new chat, the new agent reads STEPS and knows where you left off.

The Summary is not optional. It is not a nicety. It is the mechanism that makes continuity across sessions possible.

---

## Artifact Types

TFW classifies every file by its role in the knowledge lifecycle using a prefix system:

| Prefix | Name | Purpose |
|:--|:--|:--|
| **HL** | High Level | Context, vision, research, requirements. Not a task — a "map of meaning" |
| **TS** | Task Spec | Concrete task definition: scope, steps, acceptance criteria. Self-contained |
| **ONB** | Onboarding Report | Executor's analysis before starting: questions, risks, inconsistencies |
| **RF** | Result File | What was done, decisions, test results, mandatory observations |
| **REVIEW** | Review Report | Coordinator's review: checklist, verdict, tech debt collection |

This prefix system makes any project directory **self-describing**. Any agent — or human — can scan a folder and immediately understand what each file is and how to use it.

---

## Task Lifecycle

Every task in TFW follows a deterministic lifecycle with seven statuses:

```
⬜ TODO → 🔵 HL → 🟡 TS → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
```

The lifecycle enforces quality gates:

1. **Plan** — Write an HL (vision, phases, acceptance criteria). Get it approved before proceeding.
2. **Specify** — Write a TS (concrete steps, scope budget). Get it approved.
3. **Onboard** — The executor reads the TS, writes an ONB report with questions and risks *before touching any code*. Questions are answered. Only then does work begin.
4. **Execute** — Develop within the approved TS scope. Stay within scope budgets.
5. **Deliver** — Write an RF documenting what was done, decisions made, and mandatory observations (tech debt, issues noticed).
6. **Review** — The coordinator reviews the RF against a checklist. Three possible verdicts:
   - **✅ APPROVE** — all checks pass, close the task.
   - **🔄 REVISE** — specific items to fix, iterate.
   - **❌ REJECT** — fundamental issues, rethink from HL/TS.
7. **Close** — Update all traces, aggregate tech debt.

This is not ceremony for its own sake. Each gate exists because skipping it has caused real problems: executors coding before understanding the task, deliverables shipping without observations, tech debt accumulating silently without anyone triaging it.

---

## Scope Budgets

One of the hardest-earned lessons: AI agents degrade in quality when tasks are too large. TFW v3 enforces explicit limits per phase:

| Parameter | Budget | Why |
|:--|:--|:--|
| Files per phase | ≤ 7 | Agent maintains full mental model |
| New files | ≤ 4 | Each new file needs consistent patterns |
| New code (LOC) | ≤ 600 | Beyond this, repetition and shortcuts appear |
| Modified files | ≤ 6 | Each modification requires reading + understanding |

If a phase exceeds these budgets — split it. Smaller phases with clear boundaries produce better results than large phases where the agent loses track of constraints.

---

## Canonical Workflows

TFW v3 defines three canonical workflows that describe **what** to do at each stage. They are tool-agnostic — the same process works in any environment:

| Workflow | Role | What it does |
|:--|:--|:--|
| **plan** | Coordinator | Research → write HL → review → scope decision → write TS |
| **handoff** | Executor + Coordinator | Context load → ONB → execute → RF → REVIEW |
| **resume** | Coordinator | Locate task → phase status matrix → decide next phase |

Each development tool maps these workflows to its own format:
- **Claude Code**: instructions in `CLAUDE.md`
- **Cursor**: `.cursor/rules`
- **Antigravity**: `.agent/workflows/`
- **Plain chat**: follow the workflow file directly

The workflows live in `.tfw/workflows/` — one source of truth. Tool adapters reference them, never duplicate.

---

## Execution Modes

### Chat Loop (CL) — the default

The AI and the human take turns. The AI proposes steps; the human approves and executes them. The AI **never** runs external operations in CL mode — it generates exact instructions (SQL queries, shell commands, API calls) and waits for the human to run them and report back.

This is a safety constraint, not a limitation.

### Autonomous (AG) — by explicit request

When the user explicitly requests autonomous execution, or when agent tooling is available, the AI works independently within the approved TS scope. It makes incremental commits and stops when encountering issues not covered by the specification.

AG mode requires all necessary context to exist in files. If something is missing, the agent fails safely and asks.

**The rule:** default is always CL. The user must explicitly switch to AG.

---

## Roles

TFW v3 defines three explicit roles:

| Role | Responsibility |
|:--|:--|
| **Human (User)** | Approves HL and TS. Provides secrets via env vars. Reviews outputs. Final authority on task closure. |
| **Coordinator (AI)** | Writes HL and TS. Reviews executor's RF. Writes REVIEW files. Manages the Task Board. Triages observations to TECH_DEBT.md. |
| **Executor (AI)** | Reads approved TS. Writes ONB before starting. Implements changes. Writes RF with mandatory observations. Reports tech debt. |

In small projects, one AI agent fills both Coordinator and Executor roles. In larger projects, these can be separate agents — or a human can take the Coordinator role while the AI executes.

---

## Values and Principles

### Candor Over Flattery

AI agents trained on human feedback develop a habit of agreeing with users and praising their ideas. This is dangerous in engineering work. TFW agents are explicitly instructed: **Don't be sycophantic.** Be direct, precise, concrete. Flag risks. Disagree when the evidence supports it.

### Completeness Over Speed

When asked to implement, provide complete, usable output. **No placeholders.** No `// TODO: implement this`. If you can't produce a complete solution, say what's missing — don't fill the gap with a stub.

### Determinism and Safety

- Do not fabricate data or simulate external systems.
- In CL mode, all external actions are performed by the human.
- If context is insufficient, ask — don't guess.
- Never claim something was "run" or "tested" outside the session.
- Never request secrets in plain text. Use environment variables.

### Portability

Everything is Markdown. No vendor lock-in. The files work in Obsidian, VS Code, GitHub, or a plain text editor. The knowledge belongs to you, not to a platform.

### Single Source of Truth

`.tfw/` contains exactly one copy of each convention, template, and workflow. Tool adapters reference it, never duplicate. If you need to change a rule, change it in one place.

---

## Anti-patterns

These behaviors are explicitly prohibited in TFW:

- Executor starts coding before all blocking questions are resolved
- Executor skips reading HL and goes straight to implementation
- Coordinator skips review and closes without a REVIEW file
- RF file doesn't mention test results or observations
- TS is written without an approved HL
- Executor modifies files outside TS scope — even "obvious fixes"
- Executor does "bonus fixes" without documenting them in RF
- Executor writes RF before build or lint passes
- Coordinator ignores executor observations — must triage to TECH_DEBT.md

These exist because every single one has happened and caused real problems.

---

## Evolution

### v1 — The Original Idea (2024)

Established the core insight: **traces are more important than code**. Introduced the four-file structure (AGENTS, README, TASK, STEPS), the Summary discipline, and the concept of converting ad-hoc chats into structured projects.

v1 worked, but had gaps: no formal execution modes, no protocol for handling task files in new chats, no explicit role separation.

### v2 — Safety and Determinism (2025)

Added CL/AG modes, TS protocol, hard safety constraints, human-vs-AI role model, and the HL/TS/RF file prefix system. Made TFW suitable for complex engineering and analytics workflows.

### v3 — Tool-Agnostic Core (2026)

The current version. Key additions:

- **`.tfw/` directory** — tool-agnostic core with conventions, templates, workflows, and config. One copy per project, referenced by any development tool via adapters.
- **ONB and REVIEW** — two new artifact types that enforce understanding before execution and formal review after delivery.
- **7-status lifecycle** — deterministic progression with explicit quality gates.
- **3 canonical workflows** (plan, handoff, resume) — describe *what* to do, not *how*. Each tool maps them to its own format.
- **Scope budgets** — hard limits per phase calibrated for AI agent quality.
- **TECH_DEBT.md pipeline** — observations in RF → triage in REVIEW → registry in TECH_DEBT.md.
- **Tool adapter pattern** — minimal bridge files that let any IDE or agent framework use the same TFW core.
- **Anti-patterns** — an explicit list of prohibited behaviors based on real failure modes.
- **PROJECT_CONFIG.yaml** — parametrized project configuration (stack, build commands, task prefix, execution engine).

The core philosophy is unchanged: traces first, always.

---

## Getting Started

### For Humans

1. Share the link to this repository in any AI chat:
   `https://github.com/saubakirov/trace-first-starter`
2. The agent reads README → AGENTS, harvests context, and produces the initial project files.
3. Review the drafts. Pick a mode: **Discuss**, **Plan**, **Produce**, **Edit**, **Test**, or **Deploy**.
4. Work iteratively. The agent appends a Summary to every reply — copy these to `STEPS.md`.
5. When you switch chats, models, or agents — the next one reads `STEPS.md` and picks up where the previous one left off.

**Mid-conversation switch:** Already deep in a chat and realize it's time to get structured? Paste the repo link. The agent harvests the existing history and bootstraps the TFW files from what you've already discussed.

**New project init:** Copy the `.tfw/` directory into your project root. Choose a tool adapter. Fill in `PROJECT_CONFIG.yaml`. You're ready in under 5 minutes. See [init.md](init.md) for detailed setup instructions.

### For AI Agents

If you are an AI system reading this, follow the compliance protocol in your tool-specific adapter (`CLAUDE.md`, `.cursor/rules`, etc.) or read `.tfw/conventions.md` directly.

---

## Who This Is For

TFW is domain-agnostic. It works for:

- **Software engineering** — architecture decisions, codebase development, debugging sessions.
- **Data and analytics** — ETL pipelines, SQL analysis, reporting with human-in-the-loop execution.
- **Writing and publishing** — blog posts, reports, contracts, academic papers.
- **Education** — course development, assignment creation, research projects.
- **Product management** — specs, roadmaps, decision logs.

If your work involves AI-assisted iteration and you need continuity across sessions — TFW is for you.

---

## Success Criteria

A TFW project is successful when:

1. **End-to-end AI execution** — the AI handles the task without manual editing of results. If the output is wrong, you fix the prompt, not the output.
2. **Prompt-driven workflow** — every decision is traceable back to a specific instruction. Intent matters more than result.
3. **Atomic scope** — tasks are small enough to fit within the AI's reasoning capacity, but connected to a visible roadmap.
4. **Self-verification** — the AI checks its own work to the standard you would demand of yourself.

---

## Canonical Reference

- **Repository:** [github.com/saubakirov/trace-first-starter](https://github.com/saubakirov/trace-first-starter)
- **Author:** [saubakirov.kz](https://saubakirov.kz)
