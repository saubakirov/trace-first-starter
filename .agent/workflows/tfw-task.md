---
description: Execute TFW task cycle — HL → TS → (hard stop) → ONB → RF with user approval gates
---

# TFW Task — Full Lifecycle (Meta-Workflow)

> **This is a meta-workflow.** It orchestrates `plan` and `handoff` with a mandatory role boundary between them.

## Step 1: Planning (Coordinator)

Run the [plan workflow](.tfw/workflows/plan.md):

1. Load context (AGENTS → STEPS → TASK → conventions)
2. Research & ask clarifying questions
3. Write HL → get user approval
4. Write TS → get user approval

> **🔒 HARD STOP after TS approval.**
> The coordinator MUST NOT proceed to execution in this session.
> Inform the user: "Planning complete. HL and TS are approved. Start `/tfw-handoff` to begin execution."

## Step 2: Execution (Executor)

Run the [handoff workflow](.tfw/workflows/handoff.md) **in a new session or after explicit user confirmation**:

1. Load context (AGENTS → conventions → HL → TS)
2. Write ONB → get user approval on blocking questions
3. Execute → write RF
4. Coordinator reviews → writes REVIEW

## Why the Hard Stop?

Without the hard stop, the AI agent merges Coordinator and Executor roles. This causes:
- TS gets skipped (planner jumps to execution)
- ONB never happens (no cross-check of spec vs reality)
- Scope creep (no formal boundary between "what" and "how")

The hard stop forces a context reset that re-activates the executor's fresh-eyes analysis.
