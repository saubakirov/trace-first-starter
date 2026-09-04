---
name: tfw-release
description: Command /tfw-release prepares and cuts a versioned release under Trace-First Workflow. Use for /tfw-release, release scoping, version bumps, changelog entries, tag planning, or release verification.
---

# /tfw-release

This repository skill implements the `/tfw-release` command.

## Contract

- Treat literal `/tfw-release` input as a command. Also accept `tfw-release` and matching natural-language requests.
- Confirm the repository contains `.tfw/` and `RELEASE.md`.
- Enforce the Coordinator/Maintainer role lock: permit version and changelog artifacts plus explicit project release steps; forbid unrelated code changes.
- Read `.tfw/workflows/release.md` completely and follow its Read Contract. Root instructions are already active; do not independently preload common files.
- Do not tag, push, publish, or deploy unless both the workflow and user authorization permit it.
- Follow every pre-release, verification, and hard-stop gate.

Report the resolved version, changelog changes, verification results, and blocked gates.
