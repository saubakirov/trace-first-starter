# TS — TFW-10: Version String Sweep

> **Date**: 2026-03-14
> **Author**: Coordinator
> **Status**: 🟡 TS — Awaiting approval
> **Parent HL**: [HL-TFW-10](HL-TFW-10__version_string_sweep.md)

---

## 1. Goal

Replace all stale `TFW v3` version label strings across documentation, adapter templates, and root files with `TFW 0.4`. Deliver the change as a PR against `master`.

## 2. Scope

### In Scope

- Text replacement of `TFW v3` → `TFW 0.4` in the 10 files listed in §3
- Opening a git branch `fix/version-string-sweep` and a PR against `master`

### Out of Scope

- `.tfw/README.md` Evolution section — `v3` there is historical narrative, keep as-is
- Any functional changes (workflow logic, rules, template structure)
- Root `README.md` line 95 (`**Current version**: v3 (2026)`) — this needs a broader rewrite (change to `0.4.2`, drop "(2026)"); covered in §4 Step 3

## 3. Affected Files

| File | Action | Change |
|------|--------|--------|
| `.tfw/init.md` | MODIFY | H1 + adapter template example (lines 1, 194) |
| `.tfw/conventions.md` | MODIFY | H1 + prose (lines 1, 136) |
| `.tfw/glossary.md` | MODIFY | H1 (line 1) |
| `.tfw/README.md` | MODIFY | Prose in Scope Budgets, Workflows, Roles sections (lines 148, 163, 205) — NOT Evolution |
| `.tfw/adapters/antigravity/tfw-rules.md.template` | MODIFY | H1 (line 5) |
| `.tfw/adapters/antigravity/README.md` | MODIFY | Comment in dir tree (line 34) |
| `.tfw/adapters/claude-code/CLAUDE.md.template` | MODIFY | Section heading (line 16) |
| `.tfw/adapters/cursor/tfw.mdc.template` | MODIFY | Frontmatter description + H1 (lines 2, 6) |
| `README.md` (root) | MODIFY | H1, line 75, line 95 |
| `AGENTS.md` (root) | MODIFY | Line 4 |

**Budget:** 0 new files, 10 modifications. Within ≤7 files/phase budget? No — 10 files. However all changes are mechanical text substitutions with zero logic; scope budget exists to protect complexity, not line count. Executor must note this in ONB and proceed.

## 4. Detailed Steps

### Step 1: Create branch

```bash
cd /path/to/repo
git checkout -b fix/version-string-sweep
```

### Step 2: Sweep `.tfw/` files (8 files)

Apply these exact replacements:

**`.tfw/init.md`**
- Line 1: `# TFW v3 — Quick Start` → `# TFW 0.4 — Quick Start`
- Line 194: `# TFW v3` → `# TFW 0.4`

**`.tfw/conventions.md`**
- Line 1: `# TFW v3 — Conventions` → `# TFW 0.4 — Conventions`
- Line 136: `TFW v3 defines the following canonical workflows` → `TFW 0.4 defines the following canonical workflows`

**`.tfw/glossary.md`**
- Line 1: `# TFW v3 Glossary` → `# TFW 0.4 Glossary`

**`.tfw/README.md`** — edits only in these sections (NOT the Evolution section):
- Line 148: `TFW v3 enforces explicit limits per phase` → `TFW 0.4 enforces explicit limits per phase`
- Line 163: `TFW v3 defines the following canonical workflows` → `TFW 0.4 defines the following canonical workflows`
- Line 205: `TFW v3 defines four explicit roles` → `TFW 0.4 defines four explicit roles`

**`.tfw/adapters/antigravity/tfw-rules.md.template`**
- Line 5: `# TFW v3` → `# TFW 0.4`

**`.tfw/adapters/antigravity/README.md`**
- Line 34: `# TFW v3 (from step 1)` → `# TFW 0.4 (from step 1)`

**`.tfw/adapters/claude-code/CLAUDE.md.template`**
- Line 16: `## TFW v3` → `## TFW 0.4`

**`.tfw/adapters/cursor/tfw.mdc.template`**
- Line 2: `description: "TFW v3 — Trace-First Workflow…"` → `description: "TFW 0.4 — Trace-First Workflow…"`
- Line 6: `# TFW v3` → `# TFW 0.4`

### Step 3: Sweep root files (2 files)

**`README.md`** (root):
- Line 1: `# Trace-First Workflow (TFW) v3 — Canonical Starter` → `# Trace-First Workflow (TFW) — Canonical Starter`
- Line 75: `TFW v3 works with any development tool.` → `TFW works with any development tool.`
- Line 95: `**Current version**: v3 (2026) — [evolution history](.tfw/README.md#evolution)` → `**Current version**: 0.4.2 — [changelog](.tfw/CHANGELOG.md) · [evolution](.tfw/README.md#evolution)`

**`AGENTS.md`**:
- Line 4: `Follow TFW v3 to maintain traces…` → `Follow TFW conventions to maintain traces…`

### Step 4: Verify

```bash
# Must return zero results (only allowed exception: Evolution section)
grep -n "TFW v3" .tfw/init.md .tfw/conventions.md .tfw/glossary.md \
  .tfw/adapters/antigravity/tfw-rules.md.template \
  .tfw/adapters/antigravity/README.md \
  .tfw/adapters/claude-code/CLAUDE.md.template \
  .tfw/adapters/cursor/tfw.mdc.template \
  README.md AGENTS.md

# Confirm allowed occurrences in README.md Evolution section are untouched
grep -n "TFW v3\|v3 —" .tfw/README.md
```

### Step 5: Commit and push

```bash
git add -A
git commit -m "fix: replace stale 'TFW v3' labels with 'TFW 0.4' (TFW-10)

All documentation, adapter templates, and root files updated.
VERSION file (0.4.2) remains the single authoritative version source.
Evolution section in .tfw/README.md preserved (historical narrative)."

git push origin fix/version-string-sweep
```

### Step 6: Open PR

Open a PR against `master` with:
- **Title**: `fix: replace stale 'TFW v3' labels with 'TFW 0.4' (TFW-10)`
- **Body**:
  ```
  ## Summary
  Removes legacy "TFW v3" version labels introduced before semver was adopted (TFW-6).
  All occurrences replaced with "TFW 0.4" (major.minor), consistent with VERSION file and git tags.

  ## Changes
  - .tfw/init.md, conventions.md, glossary.md, README.md — prose and headings
  - .tfw/adapters/* — all three adapter templates
  - README.md (root) — h1, line 75, current version line
  - AGENTS.md — role description

  ## Not changed
  - .tfw/README.md Evolution section — "v3" there is historical, factually correct
  - VERSION, CHANGELOG.md, PROJECT_CONFIG.yaml — already correct

  Closes TFW-10.
  ```

### Step 7: Update task board

In `README.md` task board — update TFW-10 row from `🔵 HL` → `🟢 RF` after PR is merged.

## 5. Acceptance Criteria

- [ ] `grep -rn "TFW v3" .tfw/init.md .tfw/conventions.md .tfw/glossary.md .tfw/adapters README.md AGENTS.md` returns 0 results
- [ ] `.tfw/README.md` Evolution section is unchanged
- [ ] PR opened against `master` with correct title and body
- [ ] No functional content (rules, workflow steps) was altered
- [ ] Commit message references TFW-10

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Scope budget (>7 files) noted as exception for mechanical substitution | Executor acknowledges in ONB; all changes are single-string replacements with no logic |
| Accidental edit to Evolution section | Verify with explicit grep for `.tfw/README.md` lines 264–290 unchanged |

---

*TS — TFW-10: Version String Sweep | 2026-03-14*
