---
name: tfw-release
description: Prepare and cut a versioned release under the Trace-First Workflow release process. Use when the user invokes /tfw-release, tfw-release, or $tfw-release, or asks for release scoping, a version bump, changelog entry, tag plan, or TFW release verification.
---

# TFW Release

Use this skill as the Codex-native equivalent of `/tfw-release`.

## Contract

- Treat `/tfw-release`, `tfw-release`, and `$tfw-release` as aliases when the text reaches Codex.
- Confirm the repository contains `.tfw/` and `RELEASE.md`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `RELEASE.md`, `.tfw/VERSION`, `.tfw/CHANGELOG.md`, the Task Board, and relevant task artifacts in that order.
- Read `.tfw/workflows/release.md` completely before release work; it is the canonical workflow.
- Enforce the Coordinator/Maintainer role lock: permit version and changelog artifacts plus explicit project release steps; forbid unrelated code changes.
- Do not tag, push, publish, or deploy unless both the workflow and user authorization permit it.
- Follow every pre-release gate and stop exactly where the workflow requires.

Report the resolved version, changelog changes, verification results, and blocked gates.
