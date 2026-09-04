---
name: tfw-knowledge
description: Command /tfw-knowledge consolidates Trace-First Workflow Fact Candidates into verified project knowledge. Use for /tfw-knowledge, the knowledge gate, fact promotion, topic files, or knowledge_state.yaml maintenance.
---

# /tfw-knowledge

This repository skill implements the `/tfw-knowledge` command.

## Contract

- Treat literal `/tfw-knowledge` input as a command. Also accept `tfw-knowledge` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Enforce the Coordinator role lock: permit `knowledge/`, `KNOWLEDGE.md` §4, knowledge state, and processed markers; forbid code and substantive edits to source artifacts.
- Read `.tfw/workflows/knowledge.md` completely and follow its Read Contract. Root instructions are already active; do not independently preload common files.
- Treat every Fact Candidate as unverified until the workflow verifies it; never invent facts or resolve contradictions without the user.
- Follow every transaction, WAIT, and hard-stop gate.

Report promoted, rejected, deferred, and unchanged facts with their sources.
