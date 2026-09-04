---
description: TFW Release — cut a versioned release of the project
---

# TFW Release — Version Release Workflow

> **Role:** Coordinator / Maintainer
> **Trigger:** manual, when accumulated changes justify a release
> **Prerequisite:** `RELEASE.md`

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: release preparation and only separately authorized external effects. Forbidden:
> implementation, task planning/execution/review artifacts, and implicit tag/push/publish/deploy.

## Read Contract

Root instructions are already active. Read this workflow completely, then read in order. Heading
ranges must resolve once.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | `RELEASE.md` headings `What Is a Release?`, `Version Scheme`, `Release Triggers`, `Pre-Release Checklist`, and `Release Steps` | exact project release contract | project release contract |
| 2 | `.tfw/VERSION` and `.tfw/project_config.yaml` → `tfw.version`, `tfw.task_containers` | installed version and task locations | version/config |
| 3 | `.tfw/CHANGELOG.md` heading `[Unreleased]`, or its evidenced absence | only unreleased material | changelog |
| 4 | Git tags since the current version, then each resolved task/phase `status.md` whose lifecycle is `DONE` in that interval | authoritative completed release scope | Git/task-local state |
| 5 | only task artifacts referenced by the selected DONE states or release checklist | accurate release notes and project steps | governing artifacts |

Unrelated changelog history, derived portfolio state, non-DONE work, full common libraries, and
unreferenced task bodies are not inputs. Missing required contract headings, ambiguous tags, or
malformed state are hard stops.

## Who Is Acting

Resolve the acting handle before the first durable write from `team/` or the valid per-machine
binding; otherwise ask one short question. Never infer it. → `conventions.md`, `Which handle a
machine acts as`.

## 1. Scope and Version

1. List authoritative DONE tasks since the last version tag and classify framework versus project
   changes.
2. Apply `RELEASE.md` Release Triggers. If no trigger fires, stop and record the decision in the
   current RF when applicable.
3. Apply `RELEASE.md` Version Scheme: breaking → MAJOR, feature → MINOR, fix → PATCH. Prefer MINOR
   over PATCH when uncertain; a breaking change is always MAJOR.

## 2. Pre-Release Gate

Run every `RELEASE.md` Pre-Release Checklist item. Any failure stops before changelog/version writes.
Present the resolved scope, bump, checklist, and intended project-specific steps for authorization.

## 3. Write and Verify

1. Under `[Unreleased]`, move only selected bullets into `## [X.Y.Z] — YYYY-MM-DD`, using only
   non-empty Added/Changed/Deprecated/Removed/Fixed categories. If `[Unreleased]` was absent, create
   the empty heading at this write gate before adding the approved entry.
2. Update `.tfw/VERSION` and `tfw.version` together.
3. Follow only the authorized `RELEASE.md` Release Steps.
4. Verify VERSION, config, latest changelog version/date/content, checklist, and configured build.

Tag, push, publish, deploy, and notify are separate external effects: perform each only when the
user explicitly authorizes that effect. Otherwise report the prepared release and stop before it.
