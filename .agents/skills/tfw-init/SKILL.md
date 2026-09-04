---
name: tfw-init
description: Command /tfw-init initializes Trace-First Workflow or attaches and repairs TFW tooling in an existing project. Use for /tfw-init, first-time setup, project discovery, adapter installation, or Codex adapter repair.
---

# /tfw-init

This repository skill implements the `/tfw-init` command.

## Contract

- Treat literal `/tfw-init` input as a command. Also accept `tfw-init` and matching natural-language requests.
- If `.tfw/` exists, read `.tfw/workflows/init.md` completely; if it is missing, obtain the framework source or explain the missing prerequisite instead of inventing files.
- Enforce the Coordinator role lock: permit TFW setup/config, adapters, and the init task's RES/RF traces required by the workflow; forbid HL, TS, and code unrelated to TFW setup.
- Follow the workflow's Read Contract. Root instructions are already active; do not independently preload common files.
- Detect full init versus attach/repair before broad discovery, use templates at their gates, preserve configured state, and follow every interview, research, verification, close, and hard-stop gate.

Report created or updated files and project-specific assumptions requiring confirmation.
