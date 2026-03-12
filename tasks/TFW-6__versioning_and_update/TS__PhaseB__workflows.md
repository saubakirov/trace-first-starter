# TS — TFW-6 / Phase B: Workflows

> **Date**: 2026-03-12
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS — Awaiting approval
> **Parent HL**: [HL-TFW-6](HL-TFW-6__versioning_and_update.md)

---

## 1. Goal

Create the two canonical workflows (`tfw-release` and `tfw-update`) and their Antigravity adapter copies. Update conventions and glossary to reflect the new workflows and the optional RELEASE.md artifact. After this phase, any TFW project can run `/tfw-release` and `/tfw-update`.

## 2. Scope

### In Scope
- Create `.tfw/workflows/release.md` — canonical release workflow (general steps)
- Create `.tfw/workflows/update.md` — canonical update workflow for downstream projects
- Create `.agent/workflows/tfw-release.md` — Antigravity adapter copy
- Create `.agent/workflows/tfw-update.md` — Antigravity adapter copy
- Update `.tfw/conventions.md` — §8 Workflows table (add release + update) and §2 Required Artifacts (mention RELEASE.md as optional)
- Update `.tfw/glossary.md` — add version/release/update terms

### Out of Scope
- Documentation updates (KNOWLEDGE.md, .tfw/README.md, root README.md) → Phase C
- Adapter templates for Claude Code and Cursor → future task (note in RF observations)

## 3. Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/workflows/release.md` | CREATE | Canonical release workflow — general steps, references RELEASE.md |
| `.tfw/workflows/update.md` | CREATE | Canonical update workflow — version comparison, change categorization, checklist |
| `.agent/workflows/tfw-release.md` | CREATE | Antigravity adapter — copy of release.md with YAML frontmatter |
| `.agent/workflows/tfw-update.md` | CREATE | Antigravity adapter — copy of update.md with YAML frontmatter |
| `.tfw/conventions.md` | MODIFY | §8 add release + update to Workflows table; §2 add RELEASE.md as optional |
| `.tfw/glossary.md` | MODIFY | Add: VERSION, CHANGELOG, RELEASE.md, tfw-release, tfw-update terms |

**Budget:** 4 new files, 2 modifications. ≤7 files ✅, ≤4 new ✅, ≤600 LOC ✅.

## 4. Detailed Steps

### Step 1: Create `.tfw/workflows/release.md`

```markdown
---
description: TFW Release — cut a versioned release of the project
---

# TFW Release — Version Release Workflow

> **Role:** Coordinator / Maintainer
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
2. Update `tfw.version` in `.tfw/PROJECT_CONFIG.yaml`

## Step 6: Project-Specific Release Steps

Follow `RELEASE.md` §6 for any additional steps (git tag, deploy, publish, notify).

## Step 7: Verify

- `.tfw/VERSION` matches CHANGELOG latest entry
- `tfw.version` in PROJECT_CONFIG.yaml matches VERSION
- CHANGELOG entry has correct date and accurate content
- All pre-release checklist items passed
```

### Step 2: Create `.tfw/workflows/update.md`

```markdown
---
description: TFW Update — upgrade project's .tfw/ from upstream starter
---

# TFW Update — Framework Upgrade Workflow

> **Role:** Coordinator
> **Trigger:** Manually, when a new TFW version is available upstream
> **Source:** Upstream `trace-first-starter` repository or tarball

## Prerequisites

1. Read project's `.tfw/PROJECT_CONFIG.yaml` → `tfw.version` (current installed version)
2. Obtain upstream `.tfw/VERSION` (target version)
3. Obtain upstream `.tfw/CHANGELOG.md`

## Step 1: Compare Versions

```
Current: {project tfw.version}
Target:  {upstream VERSION}
```

If current == target → already up to date. Stop.

## Step 2: Review CHANGELOG

Read all CHANGELOG entries between current and target version. List every change.

## Step 3: Categorize Changes

For each changed file, classify:

| Category | Symbol | Meaning | Action |
|----------|--------|---------|--------|
| Safe | 🟢 | New file, or file not customized by project | Copy from upstream directly |
| Merge | 🟡 | File exists and may have project-specific changes | Manual review: diff upstream vs local, merge carefully |
| Breaking | 🔴 | File removed, renamed, or structurally changed | Follow migration notes in CHANGELOG |

### Files typically safe to overwrite (🟢):
- `.tfw/VERSION`
- `.tfw/CHANGELOG.md`
- New templates in `.tfw/templates/`
- New workflows in `.tfw/workflows/`

### Files requiring merge (🟡):
- `.tfw/conventions.md` — project may have added project-specific conventions
- `.tfw/glossary.md` — project may have added project-specific terms
- `.tfw/PROJECT_CONFIG.yaml` — project has custom values
- `.tfw/init.md` — unlikely to be customized, but check

### Files to check for breaking changes (🔴):
- Any file listed under `### Removed` or `### Changed` in CHANGELOG
- Template structural changes (new required sections, renamed fields)

## Step 4: Generate Update Checklist

Create a concrete checklist of actions:

```markdown
## Update Checklist: v{current} → v{target}

### 🟢 Auto-apply
- [ ] Copy `.tfw/VERSION` from upstream
- [ ] Copy `.tfw/CHANGELOG.md` from upstream
- [ ] Copy `.tfw/workflows/{new-workflow}.md` from upstream
- [ ] Copy `.agent/workflows/tfw-{new-workflow}.md` (adapter)

### 🟡 Manual merge
- [ ] Diff `.tfw/conventions.md` — merge new sections, keep project customizations
- [ ] Diff `.tfw/glossary.md` — add new terms, keep project terms

### 🔴 Breaking changes
- [ ] {Specific migration action from CHANGELOG}
```

## Step 5: Execute Update

Apply changes from the checklist. For each item:
1. Apply the change
2. Verify no project customizations were lost
3. Check the item off

## Step 6: Re-sync Adapters

Update tool-specific adapter copies from `.tfw/`:

| Adapter | Source | Target |
|---------|--------|--------|
| Antigravity workflows | `.tfw/workflows/*.md` | `.agent/workflows/tfw-*.md` |
| Antigravity rules | `.tfw/adapters/antigravity/` | `.agent/rules/` |
| Claude Code | `.tfw/adapters/claude-code/` | `CLAUDE.md` |
| Cursor | `.tfw/adapters/cursor/` | `.cursor/rules/` |

Only re-sync adapters that the project uses.

## Step 7: Update Version Marker

Update `tfw.version` in `.tfw/PROJECT_CONFIG.yaml` to the target version.

## Step 8: Verify

- `tfw.version` in PROJECT_CONFIG.yaml matches `.tfw/VERSION`
- All adapter copies are in sync with `.tfw/workflows/`
- Project-specific customizations preserved in conventions.md and glossary.md
- Build/lint/test still pass (if applicable)
```

### Step 3: Create Antigravity adapter copies

Copy both workflows to `.agent/workflows/` with identical content:
- `.agent/workflows/tfw-release.md` ← `.tfw/workflows/release.md`
- `.agent/workflows/tfw-update.md` ← `.tfw/workflows/update.md`

### Step 4: Update `.tfw/conventions.md`

**A) §8 Workflows table — add two entries:**

| Workflow | Role | Purpose |
|----------|------|---------|
| [release.md](workflows/release.md) | Coordinator | Read RELEASE.md → scope release → version bump → CHANGELOG → tag |
| [update.md](workflows/update.md) | Coordinator | Compare versions → categorize changes → update checklist → re-sync adapters |

**B) §2 Required Artifacts — add RELEASE.md as optional:**

After the `KNOWLEDGE.md` entry:
```markdown
- `RELEASE.md` _(optional)_ — project release strategy and context. Template: `.tfw/templates/RELEASE.md`.
```

### Step 5: Update `.tfw/glossary.md`

Add terms under appropriate sections:

```markdown
### VERSION
Single-line file in `.tfw/` containing the current framework version in semver format (MAJOR.MINOR.PATCH). Machine-readable. Updated by `tfw-release` workflow.

### CHANGELOG.md
Structured version history in `.tfw/`. Follows Keep a Changelog format. Each version entry lists Added, Changed, Deprecated, Removed, Fixed items. Updated by `tfw-release` workflow.

### RELEASE.md
Optional project-level artifact defining release strategy (audience, triggers, version scheme, checklist). Template: `.tfw/templates/RELEASE.md`. Referenced by `tfw-release` workflow for project-specific context. Analogous to KNOWLEDGE.md — optional, but valuable for projects with versioned outputs.

### tfw-release (Workflow)
Canonical release workflow for cutting a new version. Reads RELEASE.md for project context, scopes changes, bumps version, updates CHANGELOG. Lives in `.tfw/workflows/release.md`.

### tfw-update (Workflow)
Canonical update workflow for upgrading a project's `.tfw/` from upstream starter. Compares versions, categorizes changes (🟢 safe / 🟡 merge / 🔴 breaking), generates update checklist, re-syncs adapter copies. Lives in `.tfw/workflows/update.md`.
```

## 5. Acceptance Criteria

- [ ] `.tfw/workflows/release.md` exists with YAML frontmatter and complete release process
- [ ] `.tfw/workflows/update.md` exists with YAML frontmatter and complete update process with 🟢🟡🔴 categorization
- [ ] `.agent/workflows/tfw-release.md` is identical to `.tfw/workflows/release.md`
- [ ] `.agent/workflows/tfw-update.md` is identical to `.tfw/workflows/update.md`
- [ ] `.tfw/conventions.md` §8 includes release + update in Workflows table
- [ ] `.tfw/conventions.md` §2 includes RELEASE.md as optional artifact
- [ ] `.tfw/glossary.md` has entries for VERSION, CHANGELOG.md, RELEASE.md, tfw-release, tfw-update
- [ ] All cross-references in modified files are valid

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Update workflow too complex for simple projects | Keep categorization optional — workflow works even if project skips 🟢🟡🔴 classification |
| Release workflow assumes git | Git steps are in RELEASE.md §6 (project-specific), not in the canonical workflow itself |

---

*TS — TFW-6 / Phase B: Workflows | 2026-03-12*
