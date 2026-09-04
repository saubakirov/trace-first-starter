---
name: tfw-update
description: Command /tfw-update upgrades and synchronizes local Trace-First Workflow files and adapters while preserving project state. Use for /tfw-update, upstream upgrades, version comparison, migration, or adapter repair.
---

# /tfw-update

This repository skill implements the `/tfw-update` command.

## Contract

- Treat literal `/tfw-update` input as a command. Also accept `tfw-update` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Enforce the Coordinator role lock: permit `.tfw/` framework/config merges and adapter copies; forbid code changes.
- Read `.tfw/workflows/update.md` completely and follow its Read Contract. Root instructions are already active; do not independently preload common files.
- Preserve project state and customizations; follow every pin, classification, adapter, verification, briefing, cleanup, and hard-stop gate.

Report framework version status, copied adapters, preserved state, and manual merge risks.
