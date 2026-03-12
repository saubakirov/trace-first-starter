# TS — TFW-9: Update Source Mechanism

> **Date**: 2026-03-12
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS — Awaiting approval
> **Parent HL**: [HL-TFW-9](HL-TFW-9__update_source_mechanism.md)

---

## 1. Goal

Add `tfw.upstream` config field and `.tfw/.upstream/` staging directory so that `tfw-update` workflow has a concrete, OS-independent mechanism to fetch upstream files.

## 2. Scope

### In Scope
- Config field for upstream URL
- Fetch step in update workflow
- Gitignore entry for staging dir
- Init and glossary updates

### Out of Scope
- Authentication mechanisms (CL mode — user handles auth)
- Automated update checking (manual trigger only)
- Adapter-specific update logic

## 3. Affected Files (0 NEW + 5 MODIFY)

| File | Action | Description |
|------|--------|-------------|
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Add `tfw.upstream` field |
| `.tfw/workflows/update.md` | MODIFY | Add Step 0: Fetch Upstream |
| `.tfw/init.md` | MODIFY | Mention `tfw.upstream` in config section |
| `.tfw/glossary.md` | MODIFY | Update tfw-update entry |
| `.gitignore` | MODIFY | Add `.tfw/.upstream/` |

## 4. Detailed Steps

### Step 1: Modify `.tfw/PROJECT_CONFIG.yaml`

Add `tfw.upstream` field under `tfw:` section, after `version`:

```yaml
tfw:
  version: "0.4.1"
  upstream: "https://github.com/saubakirov/trace-first-starter"  # Source for tfw-update
  task_prefix: PROJ
```

Comment explains the purpose. Default value = canonical repo.

### Step 2: Modify `.tfw/workflows/update.md`

**2a. Update Prerequisites (lines 13-15):**

Replace:
```
1. Read project's `.tfw/PROJECT_CONFIG.yaml` → `tfw.version` (current installed version)
2. Obtain upstream `.tfw/VERSION` (target version)
3. Obtain upstream `.tfw/CHANGELOG.md`
```

With:
```
1. Read project's `.tfw/PROJECT_CONFIG.yaml` → `tfw.version` (current) and `tfw.upstream` (source URL)
2. Fetch upstream into `.tfw/.upstream/` (see Step 0)
3. Read `.tfw/.upstream/.tfw/VERSION` → target version
4. Read `.tfw/.upstream/.tfw/CHANGELOG.md` → changes since current version
```

**2b. Add Step 0: Fetch Upstream (new section, before Step 1):**

```markdown
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

After update is complete, clean up:
```bash
rm -rf .tfw/.upstream
```
```

**2c. Update all "upstream" references in Steps 1-8:**

Change "upstream `.tfw/VERSION`" → "`.tfw/.upstream/.tfw/VERSION`"
Change "Copy from upstream" → "Copy from `.tfw/.upstream/.tfw/`"
Etc. — every reference to "upstream" files should point to `.tfw/.upstream/.tfw/`.

**2d. Add Step 9: Cleanup (after Step 8: Verify):**

```markdown
## Step 9: Cleanup

Remove the staging directory:
```bash
rm -rf .tfw/.upstream
```

Optional — `.tfw/.upstream/` is gitignored, so leaving it is harmless.
```

### Step 3: Modify `.tfw/init.md`

**3a. Step 2 config section (around line 22-42):**

Add `tfw.upstream` to the example YAML block:

```yaml
tfw:
  upstream: "https://github.com/saubakirov/trace-first-starter"  # Source for tfw-update
  task_prefix: PROJ
  initial_seq: 1
```

**3b. `.gitignore` mention (near Step 4 or Step 5):**

Add note: "Ensure `.tfw/.upstream/` is in your `.gitignore` — this directory is used by `tfw-update` as a staging area."

### Step 4: Modify `.tfw/glossary.md`

Update the tfw-update definition (around line 125) — add mention of source resolution from `tfw.upstream` config field and `.tfw/.upstream/` staging directory.

### Step 5: Modify `.gitignore`

Add line:
```
.tfw/.upstream/
```

## 5. Acceptance Criteria

- [ ] `PROJECT_CONFIG.yaml` has `tfw.upstream` with default GitHub URL
- [ ] `update.md` Step 0 exists with fetch commands (Linux + Windows)
- [ ] `update.md` references point to `.tfw/.upstream/.tfw/` not vague "upstream"
- [ ] `update.md` Step 9 (cleanup) exists
- [ ] `.gitignore` contains `.tfw/.upstream/`
- [ ] `init.md` shows `tfw.upstream` in config example
- [ ] `glossary.md` tfw-update entry mentions source resolution
- [ ] `grep "Obtain upstream" .tfw/workflows/update.md` returns 0 results

## 6. Risks

| Risk | Mitigation |
|------|------------|
| `git clone` fails due to auth | CL mode — user runs command, handles credentials |
| `.tfw/.upstream/` not in gitignore of existing projects | init.md and update.md both mention it; tfw-update can check and warn |

---

*TS — TFW-9: Update Source Mechanism | 2026-03-12*
