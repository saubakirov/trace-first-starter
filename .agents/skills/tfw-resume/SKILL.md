---
name: tfw-resume
description: Command /tfw-resume locates and resumes a Trace-First Workflow task from filesystem traces and its own task state. Use for /tfw-resume, a phase status matrix, interrupted work, or selection of the next TFW stage.
---

# /tfw-resume

This repository skill implements the `/tfw-resume` command.

## Contract

- Treat literal `/tfw-resume` input as a command. Also accept `tfw-resume` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Enforce the Coordinator role lock: permit selected closing/control records and separately attributed REVIEW closing entries, status analysis and Phase HL/TS at the planning gate; forbid ONB, RF, RES, REVIEW creation/proposals, and code changes.
- Read `.tfw/workflows/resume.md` completely and follow its Read Contract. Root instructions are already active; do not independently preload common files.
- Follow its task-local authority and selected close/recovery route; retain the decision gate for unselected planning.

Report the selected closing/recovery effect or unresolved gap and stop; for unselected work, report
the status matrix and name the exact next command after the user chooses a phase.
