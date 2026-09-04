---
name: tfw-resume
description: Command /tfw-resume locates and resumes a Trace-First Workflow task from filesystem traces and its own task state. Use for /tfw-resume, a phase status matrix, interrupted work, or selection of the next TFW stage.
---

# /tfw-resume

This repository skill implements the `/tfw-resume` command.

## Contract

- Treat literal `/tfw-resume` input as a command. Also accept `tfw-resume` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Enforce the Coordinator role lock for resume: permit read-only status analysis plus Phase HL/TS when the workflow reaches planning; forbid ONB, RF, RES, REVIEW, and code changes.
- Read `.tfw/workflows/resume.md` completely and follow its Read Contract. Root instructions are already active; do not independently preload common files.
- Follow its task-local authority, decision gate, and hard stop.

Report the status matrix and name the exact next `/tfw-*` command after the user chooses a phase.
