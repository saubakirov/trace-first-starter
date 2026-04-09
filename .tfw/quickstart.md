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
