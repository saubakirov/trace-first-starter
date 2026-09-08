---
name: tfw-release
description: Command /tfw-release routes a project-defined release effect under Trace-First Workflow. Use for /tfw-release, release scoping, versioning, changelog entries, tag planning, or release verification.
---

# /tfw-release

This repository skill implements the `/tfw-release` command.

## Contract

- Treat literal `/tfw-release` input as a command. Also accept `tfw-release` and matching natural-language requests.
- Confirm the repository contains `.tfw/`; read `RELEASE.md` only when the project provides it.
- Resolve the selected project release effect and its authority; do not invent a universal versioning or publication policy.
- Enforce the Coordinator role lock: permit only the selected release artifacts and explicit project steps; forbid unrelated code changes.
- Read `.tfw/workflows/release.md` completely and follow its Read Contract. Root instructions are already active; do not independently preload common files.
- Do not tag, push, publish, or deploy unless both the workflow and user authorization permit it.
- Preserve the selected release tree as an isolated complete effect and follow every verification and hard-stop gate.

Report the resolved version, changelog changes, verification results, and blocked gates.
