---
name: tfw-handoff
description: Command /tfw-handoff executes an approved Trace-First Workflow TS and creates ONB, implementation changes, evidence, and RF. Use for /tfw-handoff or implementation of an approved TFW task or phase.
---

# /tfw-handoff

This repository skill implements the `/tfw-handoff` command.

## Contract

- Treat literal `/tfw-handoff` input as a command. Also accept `tfw-handoff` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Enforce the Executor role lock: permit ONB, RF, evidence, and implementation changes within the approved TS; forbid HL, TS, RES, REVIEW, and scope changes.
- Read `.tfw/workflows/handoff.md` completely and follow its checkpoint Read Contract. Root
  instructions are already active; do not independently preload `AGENTS.md` or any full common
  library. On return, let the workflow resolve the highest lineage and prior REVIEW.
- Use `.tfw/templates/ONB.md`, `.tfw/templates/evidence/EV.md`, and `.tfw/templates/RF.md` only at their workflow gates.
- Follow every approval, build, evidence, and Pre-RF gate, then stop after RF.

When RF is complete, direct the user to `/tfw-review`.
