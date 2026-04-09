# HL — TFW-31: Quick Start — Agent-First Rewrite

**Status:** 📝 HL_DRAFT (v3 — post-RESEARCH, redesigned)
**Author:** Coordinator
**Date:** 2026-04-09

---

## §1 Problem

### Bootstrap paradox (chicken-and-egg)
init.md is an execution workflow that assumes the agent already understands TFW (roles, artifacts, lifecycle). But at first contact, the agent knows nothing. Cramming "what is TFW" into init.md mixes learning with execution — two fundamentally different activities.

### No learning step
There is no file that tells a fresh agent: "clone this repo, read these files in this order, now you understand TFW." The agent goes straight from "nothing" to "execute init workflow" with no onboarding.

### Quick Start prompts aren't self-contained
A user copies a prompt from README into Claude Code. The prompt must contain everything the agent needs: repo URL, what to read, what to do. Current prompts assume the agent already has context.

### init.md doesn't explain what it creates
Phase 2 asks "what task prefix?" without explaining what a prefix is. Mini-Setup creates a "Task Board" without showing what it looks like. A first-time user (and agent) is lost.

---

## §2 Goal

1. Create `.tfw/quickstart.md` — a strict reading list for agents (learning step, ~20 lines)
2. Rewrite README Quick Start — 3 self-contained prompt blocks
3. Enrich init.md Tutorial Mode with mini-examples (prefix, task board)
4. Remove Phase 0 Bootstrap from init.md (added in v1, wrong approach)
5. Update gen_docs.py — quickstart.md becomes "Getting Started" in docs

---

## §3 Visualization

### §3.1 User journey (to-be)

```
Human reads README
    │
    ├── Copies prompt into agent
    │
    Agent receives:
    ├── 1. Clone repo URL
    ├── 2. Read .tfw/quickstart.md        ← NEW FILE (learning)
    │       │
    │       ├── Read .tfw/README.md       (philosophy)
    │       ├── Read .tfw/glossary.md     (terms)
    │       ├── Read .tfw/conventions.md  (rules)
    │       └── "Now run init.md"
    │
    └── 3. Execute .tfw/workflows/init.md  (execution, existing)
```

### §3.2 quickstart.md structure (~20 lines)

```
# Quick Start — For AI Agents

## Step 1: Get TFW files
Clone https://github.com/saubakirov/trace-first-starter
(or: .tfw/ is already in your project)

## Step 2: Learn TFW (read in this order)
1. .tfw/README.md — philosophy, why traces matter
2. .tfw/glossary.md — what terms like HL, TS, RF mean
3. .tfw/conventions.md — formal rules, naming, statuses

## Step 3: Tell the human
Recommend reading .tfw/README.md (5 min, philosophy only)

## Step 4: Initialize
Run .tfw/workflows/init.md — it guides you through project setup
```

### §3.3 README Quick Start (to-be)

```
## Quick Start

> Read the [philosophy](.tfw/README.md) first — 5 minutes.
> Everything else is handled by your AI agent.

### New project
    <self-contained prompt with repo URL + quickstart.md reference>

### Existing project
    <self-contained prompt with .tfw/ copy + quickstart.md reference>

### Already set up
    <prompt with AGENTS.md + plan.md>
```

---

## §4 Scope

| Metric | Value |
|--------|-------|
| Files modified | 3 (`README.md`, `.tfw/workflows/init.md`, `docs/scripts/gen_docs.py`) |
| New files | 1 (`.tfw/quickstart.md`) |
| Lines changed | ~80 |

---

## §10 RESEARCH Justification

RESEARCH completed. Findings:
- Bootstrap paradox: init.md assumes context that doesn't exist
- OMO pattern doesn't translate (methodology ≠ software)
- Solution: separate learning (quickstart.md) from execution (init.md)
- gen_docs.py maps `.tfw/init.md` → "Getting Started" — needs update

---

## §11 Strategic Session Insights

| # | Insight | Category | Source |
|---|---------|----------|--------|
| 1 | "Два в одном получаем проблему курицы и яйца" — learning and execution must be separate files | Architecture | User |
| 2 | User's real pattern: "TFW здесь, сделай инит" — agent needs full .tfw/ access + reading order | UX | User example |
| 3 | "Человек и агент ничего не знают" — design for zero prior knowledge | UX | User |
| 4 | init.md needs mini-examples in Tutorial Mode (prefix, task board) | Onboarding | User |
| 5 | quickstart.md goes in `.tfw/` (framework core, not project artifact), lowercase | Naming | Coordinator analysis |
