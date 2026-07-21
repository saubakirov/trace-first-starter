---
name: tfw-knowledge
description: Consolidate Trace-First Workflow Fact Candidates into verified project knowledge. Use when the user invokes /tfw-knowledge, tfw-knowledge, or $tfw-knowledge, or asks to run the knowledge gate, promote facts, update knowledge topic files, or maintain knowledge_state.yaml.
---

# TFW Knowledge

Use this skill as the Codex-native equivalent of `/tfw-knowledge`.

## Contract

- Treat `/tfw-knowledge`, `tfw-knowledge`, and `$tfw-knowledge` as aliases when the text reaches Codex.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/project_config.yaml`, `.tfw/knowledge_state.yaml`, `KNOWLEDGE.md`, all `knowledge/` topic files, the Task Board, and candidate-bearing artifacts in that order.
- Read `.tfw/workflows/knowledge.md` completely before consolidation; it is the canonical workflow.
- Enforce the Coordinator role lock: permit `knowledge/`, KNOWLEDGE.md §4, knowledge state, and processed markers; forbid code and substantive edits to source artifacts.
- Treat every Fact Candidate as unverified until the workflow verifies it. Never invent facts or resolve contradictions without the user.
- Follow every WAIT gate and stop exactly where the workflow requires.

Report promoted, rejected, deferred, and unchanged facts with their sources.
