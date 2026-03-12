---
description: TFW Update — upgrade project's .tfw/ from upstream starter
---

# TFW Update — Framework Upgrade Workflow

> **Role:** Coordinator
> **Trigger:** Manually, when a new TFW version is available upstream
> **Source:** Upstream starter repository configured in `tfw.upstream`

## Prerequisites

1. Read project's `.tfw/PROJECT_CONFIG.yaml` → `tfw.version` (current) and `tfw.upstream` (source URL)
2. Fetch upstream into `.tfw/.upstream/` (see Step 0)
3. Read `.tfw/.upstream/.tfw/VERSION` → target version
4. Read `.tfw/.upstream/.tfw/CHANGELOG.md` → changes since current version

## Step 0: Fetch Upstream

Read `tfw.upstream` from `.tfw/PROJECT_CONFIG.yaml` — this is the source repository URL.

Clean any previous staging directory and clone fresh:

**Linux / macOS:**
```bash
rm -rf .tfw/.upstream
git clone --depth 1 {tfw.upstream} .tfw/.upstream
```

**Windows (PowerShell):**
```powershell
if (Test-Path .tfw/.upstream) { Remove-Item -Recurse -Force .tfw/.upstream }
git clone --depth 1 {tfw.upstream} .tfw/.upstream
```

> In CL mode, present the exact command with the resolved URL for the user to run.
> `.tfw/.upstream/` is gitignored — safe to create in the project directory.

## Step 1: Compare Versions

```
Current: {project tfw.version}
Target:  {.tfw/.upstream/.tfw/VERSION}
```

If current == target → already up to date. Stop.

## Step 2: Review CHANGELOG

Read all entries in `.tfw/.upstream/.tfw/CHANGELOG.md` between current and target version. List every change.

## Step 3: Categorize Changes

For each changed file, classify:

| Category | Symbol | Meaning | Action |
|----------|--------|---------|--------|
| Safe | 🟢 | New file, or file not customized by project | Copy from `.tfw/.upstream/.tfw/` directly |
| Merge | 🟡 | File exists and may have project-specific changes | Manual review: diff `.tfw/.upstream/.tfw/` vs local, merge carefully |
| Breaking | 🔴 | File removed, renamed, or structurally changed | Follow migration notes in CHANGELOG |

### Files typically safe to overwrite (🟢):
- `.tfw/VERSION` ← copy from `.tfw/.upstream/.tfw/VERSION`
- `.tfw/CHANGELOG.md` ← copy from `.tfw/.upstream/.tfw/CHANGELOG.md`
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
- [ ] Copy `.tfw/VERSION` from `.tfw/.upstream/.tfw/VERSION`
- [ ] Copy `.tfw/CHANGELOG.md` from `.tfw/.upstream/.tfw/CHANGELOG.md`
- [ ] Copy `.tfw/workflows/{new-workflow}.md` from `.tfw/.upstream/.tfw/workflows/`
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

## Step 9: Cleanup

Remove the staging directory:

**Linux / macOS:**
```bash
rm -rf .tfw/.upstream
```

**Windows (PowerShell):**
```powershell
Remove-Item -Recurse -Force .tfw/.upstream
```

Optional — `.tfw/.upstream/` is gitignored, so leaving it is harmless.
