---
name: tfw-knowledge
description: Command /tfw-knowledge consolidates Trace-First Workflow Fact Candidates into verified project knowledge. Use for /tfw-knowledge, selected handovers, human-knowledge qualification, independent records or currentness.
---

# /tfw-knowledge

This repository skill implements the `/tfw-knowledge` command.

## Contract

- Treat literal `/tfw-knowledge` input as a command. Also accept `tfw-knowledge` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Enforce the Coordinator role lock: permit selected human-knowledge records and current owning effect references; forbid code, technical decisions, source/marker/state writes and maintained inventories.
- Read `.tfw/workflows/knowledge.md` completely and follow its Read Contract. Root instructions are already active; do not independently preload common files.
- Treat every Fact Candidate as unverified until the workflow verifies it; never invent facts or resolve contradictions without the user.
- Follow source/intent/authority and incoming-relation checks, every required decision and hard-stop gate; existing explicit authority can satisfy a settled decision.

Report promoted, rejected, deferred, and unchanged facts with their sources.
