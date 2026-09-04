---
name: tfw-docs
description: Command /tfw-docs updates Trace-First Workflow project documentation after review. Use for /tfw-docs or updates to KNOWLEDGE.md sections 1-3 from RF/REVIEW results.
---

# /tfw-docs

This repository skill implements the `/tfw-docs` command.

## Contract

- Treat literal `/tfw-docs` input as a command. Also accept `tfw-docs` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Enforce the Coordinator role lock: permit only the documentation and named convention ranges owned by the workflow; forbid code, implementation, debt, topic-file, and `KNOWLEDGE.md` §4 changes.
- Read `.tfw/workflows/docs.md` completely and follow its Read Contract. Root instructions are already active; do not independently preload common files.
- Follow its triage, approval, traceability, and stop gates.

If Fact Candidates remain, direct the user to `/tfw-knowledge`.
