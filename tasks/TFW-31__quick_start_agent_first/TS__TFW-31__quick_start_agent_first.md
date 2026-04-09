# TS — TFW-31: Quick Start — Agent-First Rewrite (v3)

**Status:** 🟡 TS_DRAFT
**HL:** [HL-TFW-31](HL-TFW-31__quick_start_agent_first.md)
**RES:** [RES-TFW-31](RES__TFW-31__quick_start_agent_first.md)
**Author:** Coordinator
**Date:** 2026-04-09

---

## Scope Budget

| Metric | Budget | Actual |
|--------|--------|--------|
| Files modified | 14 | 3 |
| New files | 8 | 1 |
| LOC changed | 1200 | ~100 |

---

## Change 1: [NEW] .tfw/quickstart.md

Create `.tfw/quickstart.md` — a strict reading list for AI agents. No duplication — just file references and order. Domain-agnostic language (work, decisions, tasks — not code).

```markdown
---
description: TFW Quick Start — reading list for AI agents before first initialization
---

# Quick Start — For AI Agents

> You are about to help a user adopt Trace-First Workflow (TFW) — a methodology
> that makes decisions, reasoning, and knowledge permanent across AI sessions.
> It works for any domain: software, analytics, writing, business processes.

## Step 1: Get TFW files

If the `.tfw/` directory is not already in the project, clone the starter:

    git clone https://github.com/saubakirov/trace-first-starter

Then copy the `.tfw/` directory into the user's project root.

## Step 2: Learn TFW

Read these files in order. Do not skip — each builds on the previous:

1. **`.tfw/README.md`** — the philosophy: why traces matter more than output
2. **`.tfw/glossary.md`** — terminology: what HL, TS, RF, Coordinator, Executor mean
3. **`.tfw/conventions.md`** — formal rules: naming, statuses, scope budgets, anti-patterns

After reading, you should understand:
- The task lifecycle (TODO → HL → TS → ONB → RF → REVIEW → DONE)
- The three roles (Coordinator plans, Executor implements, Reviewer reviews)
- That every task produces trace files — the project's permanent memory

## Step 3: Recommend to the human

Tell the user:
"We recommend reading `.tfw/README.md` — it explains the philosophy behind TFW
and takes about 5 minutes. You don't need to read anything else — I'll handle the rest."

## Step 4: Initialize

Now run the initialization workflow:

    Read .tfw/workflows/init.md and follow it.

This will guide you through project discovery, an interview with the user,
and creation of all TFW project files.
```

---

## Change 2: README.md — Rewrite Quick Start section

Replace the entire current Quick Start section (lines 42–87) with the content below. Each prompt block is **self-contained** — works when copy-pasted into any AI agent with zero prior context.

```markdown
## Quick Start

> **For humans:** read the [philosophy](.tfw/README.md) — 5 minutes that explain why TFW works.
> Everything else is handled by your AI agent.

### New project — start from scratch

Copy this into your AI agent (Claude Code, Cursor, or any chat):

    I want to start a new project using Trace-First Workflow (TFW) —
    a methodology that preserves decisions, reasoning, and knowledge across AI sessions.
    Clone https://github.com/saubakirov/trace-first-starter to a temp directory,
    then read .tfw/quickstart.md and follow it step by step.
    My project is about: <describe your project in a few sentences>

### Existing project — add TFW

    I want to add Trace-First Workflow (TFW) to this existing project.
    Clone https://github.com/saubakirov/trace-first-starter to a temp directory,
    copy the .tfw/ directory into my project root, then delete the temp clone.
    Then read .tfw/quickstart.md and follow it step by step.
    My project is about: <describe your project>

### Already set up — start working

    Read AGENTS.md for project context.
    Then read .tfw/workflows/plan.md and follow it to create a new task.
    Task: <describe what you want to do>

### FAQ

**Do I need to read the documentation?**
No. The `.tfw/` files are designed for AI agents. You only need [the philosophy](.tfw/README.md).

**Which AI tools work with TFW?**
Any tool that can read files. Adapters exist for Claude Code, Cursor, and Antigravity — your agent sets them up during init.

**Can I use TFW for non-code work?**
Yes — analytics, writing, education, business processes. TFW is about structuring decisions, not about code.

---
```

---

## Change 3: .tfw/workflows/init.md — Three modifications

### 3a: Remove Phase 0: Bootstrap (lines 16–42)

Delete the entire Phase 0 section added in v1. It was a wrong approach — learning belongs in quickstart.md, not in the execution workflow.

### 3b: Enrich Tutorial Mode with mini-examples

Replace the current Tutorial Mode (after removing Phase 0) with:

```markdown
## Tutorial Mode

At the start, ask the user:
"Is this your first time using TFW? I can explain each step as we go."
If yes — add brief explanations at each phase.
If no — proceed efficiently, skip explanations.

Regardless of tutorial mode, suggest:
"We recommend reading `.tfw/README.md` — it explains the philosophy behind TFW
and takes about 5 minutes. Everything else in the repo is designed for AI agents,
not for you to read line by line."

### Mini-examples for first-time users

Use these when tutorial mode is on:

**Task prefix** — a short code for your project's task IDs:
- `LEE` → tasks are LEE-1, LEE-2, LEE-3...
- `APP` → tasks are APP-1, APP-2, APP-3...

**Task Board** — a table in README.md that tracks all work:

| ID | Task | Status |
|----|------|--------|
| LEE-1 | TFW Init | ✅ DONE |
| LEE-2 | Sales analysis dashboard | 🟡 TS_DRAFT |
| LEE-3 | Client onboarding workflow | ⬜ TODO |
```

### 3c: Verify .claude/commands/ copy (from v1)

The Phase 4 explicit `.claude/commands/` instruction from v1 should remain. Verify it's still present after removing Phase 0.

---

## Change 4: docs/scripts/gen_docs.py — Update source mapping

Change the "Getting Started" source from `init.md` to `quickstart.md`:

```python
# Line 21: change from
(".tfw/init.md", "getting-started.md", True),
# to
(".tfw/quickstart.md", "getting-started.md", True),
```

And add init.md to be published as a workflow reference (it'll be auto-picked up by the workflows glob — verify it's matched by `.tfw/workflows/**/*.md`).

---

## Definition of Done

- [ ] `.tfw/quickstart.md` exists with 4-step reading list
- [ ] quickstart.md language is domain-agnostic (decisions, reasoning, work — not code)
- [ ] quickstart.md includes repo URL, reading order, human recommendation, pointer to init.md
- [ ] README Quick Start has 3 self-contained prompt blocks
- [ ] Each prompt includes "Trace-First Workflow (TFW)" description + repo URL
- [ ] Each prompt has `<placeholder>` for project description
- [ ] FAQ is 3 questions, domain-agnostic
- [ ] init.md Phase 0 removed (was wrong approach)
- [ ] init.md Tutorial Mode has mini-examples (prefix, task board)
- [ ] init.md Phase 4 still has `.claude/commands/` copy instruction
- [ ] gen_docs.py maps quickstart.md → getting-started.md
- [ ] No other sections of README.md modified
