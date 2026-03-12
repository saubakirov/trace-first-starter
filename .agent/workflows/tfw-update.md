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
