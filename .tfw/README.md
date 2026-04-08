# Trace-First Workflow (TFW)

> *"The thinking is the product. Everything else is output."*

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
| Onboarding = "read the codebase" | Onboarding = read AGENTS → HL → TS → RF |
| New chat = start from zero | New chat = load traces, resume from last checkpoint |

This is closely related to the **AI-First** philosophy: if AI is going to produce most of the code, then the architecture, the processes, and the knowledge must be organized for the AI, not just for the human developer. The human's job shifts from *writing* code to *managing* the context that the AI needs to produce correct code.

TFW is the methodology for that management.

---

## How TFW Works

TFW is a ritual with a predictable structure and one unbreakable rule: **every task produces a trace.**

A task moves through a deterministic lifecycle — Plan → Research → Specify → Onboard → Execute → Deliver → Review → Close. Each stage produces a specific artifact (HL, RES, TS, ONB, RF, REVIEW). The artifacts are files. The files are the project's memory.

When you start a new chat, the new agent reads the Task Board and relevant traces — and knows where the project stands. No re-explanation needed. No context lost. The traces live where the work lives.

The methodology is domain-agnostic. The same ritual works for code, analytics, writing, education, and business processes. It is tool-agnostic — the same `.tfw/` core works in Claude Code, Cursor, Antigravity, or a plain chat window.

> For the full reference — artifact types, naming rules, lifecycle statuses, scope budgets — see [conventions.md](conventions.md) and [glossary.md](glossary.md).

---

## Values and Principles

### Traces Over Code

The trace is the product — intent, decisions, constraints, and alternatives matter more than the implementation itself. A codebase without traces is a black box. TFW captures not just *what* was built, but *why*, *what else was considered*, and *what was rejected*.

### Candor Over Flattery

AI agents trained on human feedback develop a habit of agreeing with users and praising their ideas. TFW agents are explicitly instructed: **Don't be sycophantic.** Be direct, precise, concrete. Flag risks. Disagree when evidence supports it. The coordinator's job is to ask uncomfortable questions and catch implicit assumptions — quality of planning matters more than speed of pipeline progression.

### Completeness Over Speed

When asked to implement, provide complete, usable output. **No placeholders.** No `// TODO: implement this`. If you can't produce a complete solution, say what's missing — don't fill the gap with a stub.

### Honesty Over Convincingness

AI agents that sound confident while being wrong are more dangerous than agents that refuse to answer. TFW agents must never fabricate data, claim untested results, or simulate external systems. When context is insufficient, the correct behavior is to ask, not guess. Confidence without correctness is the deadliest failure mode.

### Structural Enforcement

Gates should be structural — file existence, folder structure, required artifacts — not procedural (checkboxes in documents, state tables in headers). If a stage isn't done, the file doesn't exist. No parsing needed, no format compliance required, no update discipline to enforce. The filesystem is the state machine.

### Naming Creates Behavior

Right terminology triggers right associations in AI agents. A small prompt with precise terms is more effective than a long prompt with explanations. TFW adopted OODA, Sufficiency Verdict, Trust Protocol, Progressive Disclosure — each term replaced paragraphs of instructions. If you have to explain what a step does, the step is named wrong.

### Single Source of Truth

`.tfw/` contains exactly one copy of each convention, template, and workflow. Tool adapters reference it, never duplicate. If you need to change a rule, change it in one place.

### Portability

Everything is Markdown. No vendor lock-in. The files work in Obsidian, VS Code, GitHub, or a plain text editor. The knowledge belongs to you, not to a platform.

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

## Success Criteria

A TFW project is successful when:

1. **End-to-end AI execution** — the AI handles the task without manual editing of results. If the output is wrong, you fix the prompt, not the output.
2. **Prompt-driven workflow** — every decision is traceable back to a specific instruction. Intent matters more than result.
3. **Atomic scope** — tasks are small enough to fit within the AI's reasoning capacity, but connected to a visible roadmap.
4. **Self-verification** — the AI checks its own work to the standard you would demand of yourself.

---

## Version History

For the full evolution of TFW (v1 → v2 → v3) and detailed changelog → [CHANGELOG.md](CHANGELOG.md)

---

## Links

- **Repository:** [github.com/saubakirov/trace-first-starter](https://github.com/saubakirov/trace-first-starter)
- **Author:** [saubakirov.kz](https://saubakirov.kz)
