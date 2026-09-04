---
name: tfw-plan
description: Command /tfw-plan plans a Trace-First Workflow task and creates or revises HL/TS artifacts. Use for /tfw-plan, TFW task inception, scope planning, or phase specifications.
---

# /tfw-plan

This repository skill implements the `/tfw-plan` command.

## Contract

- Treat literal `/tfw-plan` input as a command. Also accept `tfw-plan` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Enforce the Coordinator role lock: permit HL and TS; forbid ONB, RF, RES, REVIEW, and code.
- Read `.tfw/workflows/plan.md` completely and follow its Read Contract and gates. Root instructions
  are already active; do not independently preload `AGENTS.md` or any full common library.
- Open `.tfw/templates/HL.md` and `.tfw/templates/TS.md` only at their workflow gates.
- Stop when the workflow routes to research, handoff, execution, or review.

When the workflow routes onward, name the exact next command, such as `/tfw-research` or `/tfw-handoff`.
