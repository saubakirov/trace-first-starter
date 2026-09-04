---
name: tfw-config
description: Command /tfw-config audits or changes Trace-First Workflow configuration and propagates values to every registered inline location. Use for /tfw-config, config verification, project_config.yaml changes, or Config Sync Registry updates.
---

# /tfw-config

This repository skill implements the `/tfw-config` command.

## Contract

- Treat literal `/tfw-config` input as a command. Also accept `tfw-config` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Enforce the Coordinator role lock: permit `project_config.yaml`, workflow/convention inline values, and adapter copies; forbid code and task-artifact changes.
- Read `.tfw/workflows/config.md` completely and follow its Read Contract. Root instructions are already active; do not independently preload common files.
- Follow every edit approval, registry-completeness, adapter-sync, verification, and hard-stop gate.

Report keys checked or changed, synchronized files, and remaining mismatches.
