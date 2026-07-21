---
name: tfw-update
description: Upgrade and synchronize local Trace-First Workflow framework files and adapters while preserving project state. Use when the user invokes /tfw-update, tfw-update, or $tfw-update, or asks for an upstream TFW upgrade, version comparison, migration, or adapter re-sync.
---

# TFW Update

Use this skill as the Codex-native equivalent of `/tfw-update`.

## Contract

- Treat `/tfw-update`, `tfw-update`, and `$tfw-update` as aliases when the text reaches Codex.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/project_config.yaml`, `.tfw/VERSION`, `.tfw/CHANGELOG.md`, and `.tfw/adapters/README.md` in that order.
- Read `.tfw/workflows/update.md` completely before updating; it is the canonical workflow.
- Enforce the Coordinator role lock: permit `.tfw/` framework/config merges and adapter copies; forbid code changes.
- Never overwrite project state such as `.tfw/knowledge_state.yaml`, `knowledge/`, `KNOWLEDGE.md`, or `TECH_DEBT.md`; preserve project customizations during merges.
- Re-sync only adapters used by the project. Scope Codex installation to `.tfw/adapters/codex/skills/tfw-*/` → `.agents/skills/tfw-*/`.
- Follow categorization, cleanup, and verification gates exactly as the workflow requires.

Report framework version status, copied adapters, preserved state, and manual merge risks.
