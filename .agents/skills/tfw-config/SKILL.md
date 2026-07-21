---
name: tfw-config
description: Audit or change Trace-First Workflow configuration and propagate values to every registered inline location. Use when the user invokes /tfw-config, tfw-config, or $tfw-config, or asks for config verification, project_config.yaml changes, or Config Sync Registry updates.
---

# TFW Config

Use this skill as the Codex-native equivalent of `/tfw-config`.

## Contract

- Treat `/tfw-config`, `tfw-config`, and `$tfw-config` as aliases when the text reaches Codex.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/project_config.yaml`, and `.tfw/workflows/config.md` in that order.
- Read `.tfw/workflows/config.md` completely before config work; it is the canonical workflow and contains the Config Sync Registry.
- Enforce the Coordinator role lock: permit project_config.yaml, workflow/convention inline values, and adapter copies; forbid code and task-artifact changes.
- In verify mode, compare source values with every registry target. In edit mode, require approval and update every registered location plus affected adapter copies.
- Follow every approval and hard-stop gate exactly as the workflow requires.

Report keys checked or changed, synchronized files, and remaining mismatches.
