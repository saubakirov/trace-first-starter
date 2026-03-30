# TFW Release — Version Bump + Changelog

You are now running the **TFW Release** workflow.

## Role Lock

**🔒 COORDINATOR** — you manage versioning artifacts only. You MUST NOT write code, ONB, RF, or REVIEW.

## Instructions

1. Load context in this order:
   - `AGENTS.md`
   - `.tfw/conventions.md`
   - `RELEASE.md` (if exists) — project release strategy
   - `.tfw/CHANGELOG.md` — existing version history
   - `.tfw/VERSION` — current version

2. Read and follow the canonical workflow: `.tfw/workflows/release.md`

3. Execute the release process:
   - Scope changes since last release
   - Determine version bump (MAJOR/MINOR/PATCH)
   - Update `.tfw/VERSION`
   - Update `.tfw/CHANGELOG.md`
   - Update `PROJECT_CONFIG.yaml` version field

## User input

$ARGUMENTS
