---
name: tfw-init
description: Initialize Trace-First Workflow in a new or existing project. Use when the user invokes /tfw-init, tfw-init, or $tfw-init, or asks for first-time TFW setup, project discovery, adapter installation, or creation of the initial TFW task.
---

# TFW Init

Use this skill as the Codex-native equivalent of `/tfw-init`.

## Contract

- Treat `/tfw-init`, `tfw-init`, and `$tfw-init` as aliases when the text reaches Codex.
- If `.tfw/` exists, read `.tfw/workflows/init.md` completely; it is the canonical workflow. If `.tfw/` is missing, do not invent framework files—obtain the framework source or explain the missing prerequisite.
- Load available `AGENTS.md`, README files, project documentation, repository structure, and existing TFW state before changing files.
- Enforce the Coordinator role lock: permit TFW setup/config, adapters, and the init task's RES/RF traces required by the workflow; forbid HL, TS, and code unrelated to TFW setup.
- Use `.tfw/templates/*` whenever the workflow creates an artifact or state file.
- Detect an already-configured project and do not rerun full initialization without user direction.
- Follow interview, research, verification, and stop gates exactly as the workflow requires.

Report created or updated files and project-specific assumptions requiring confirmation.
