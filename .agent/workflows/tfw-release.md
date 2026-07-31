---
description: TFW Release — cut a versioned release of the project
---

# TFW Release — Version Release Workflow

> **Role:** Coordinator. “Maintainer” describes release responsibility but is not a
> separate Commit Identity role.
> **Trigger:** Manually, when accumulated changes justify a new version
> **Prerequisite:** `RELEASE.md` exists with project-specific release context

## Prerequisites

1. Read `RELEASE.md` — understand what a release means for this project
2. Read `.tfw/CHANGELOG.md` — see the last released version
3. Read `.tfw/VERSION` — confirm current version
4. Read Task Board — identify tasks completed since last release

## Step 1: Scope the Release

1. List all tasks completed since the last version tag
2. Categorize changes:
   - **Framework changes** — templates, workflows, conventions, adapters
   - **Project changes** — task artifacts, documentation, internal improvements
3. Decide: do the accumulated changes justify a release? Consult `RELEASE.md` §4 (triggers)

> If NO → stop. Record decision in next RF if applicable.

## Step 2: Determine Version Bump

Consult `RELEASE.md` §3 (version scheme):

| Change type | Bump |
|-------------|------|
| Breaking changes (conventions, template structure, workflow steps changed/removed) | MAJOR |
| New features (new workflows, new templates, new optional artifacts) | MINOR |
| Fixes, clarifications, typos | PATCH |

> When in doubt, prefer MINOR over PATCH. Breaking changes MUST be MAJOR.

## Step 3: Pre-Release Checklist

Run through `RELEASE.md` §5 checklist. All items must pass before proceeding.

## Step 4: Write CHANGELOG Entry

Add a new section to `.tfw/CHANGELOG.md` under `## [Unreleased]`:

```
## [X.Y.Z] — YYYY-MM-DD
### Added
- ...
### Changed
- ...
### Deprecated
- ...
### Removed
- ...
### Fixed
- ...
```

Move items from `[Unreleased]` to the new version section. Only include categories that have entries.

## Step 5: Update Version Files

1. Update `.tfw/VERSION` to the new version
2. Update `tfw.version` in `.tfw/project_config.yaml`

## Step 6: Route the Local Release Commit

Choose an explicit task ID, or use guarded `task:none` only for genuinely non-task
release work with no staged canonical task path. Use the adapter-declared surface and
the registered `coordinator` Role Lock:

```text
python .tfw/scripts/commit_identity_router.py route --workflow release --surface {adapter-surface} --task {TASK-ID|none} --work release --role coordinator --operation ordinary --summary "{concise release result}" --repo . {--non-task only with task:none}
```

Use the returned validated subject for the local release commit. A local commit is
not push, remote-tag, deploy, publish, or notify authority.

## Step 7: Project-Specific Release and Publication Gates

Follow `RELEASE.md` §6 while treating each action separately:

1. Decide whether an authorized local tag is required. Local tag creation does not
   authorize remote tag publication.
2. Before push, remote tag, deploy, publish, or notify, require separate explicit
   human authority for that exact action.
3. If authority is absent, stop after the local result and report the unpublished
   state. For TFW-49, process F26 keeps every remote publication action unavailable
   until all phases close and the user later says `APPROVE PUSH`.

## Step 8: Verify

- `.tfw/VERSION` matches CHANGELOG latest entry
- `tfw.version` in project_config.yaml matches VERSION
- CHANGELOG entry has correct date and accurate content
- All pre-release checklist items passed
- Local commit/tag state and every separately authorized publication action are
  reported distinctly
