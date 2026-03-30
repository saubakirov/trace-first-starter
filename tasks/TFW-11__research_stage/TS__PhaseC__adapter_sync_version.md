# TS — TFW-11 / Phase C: Full Adapter Sync + Claude Code Restore + Version 0.5.0

> **Date**: 2026-03-30
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS — waiting for approval
> **Parent HL**: [HL-TFW-11](HL-TFW-11__research_stage.md)

---

## 1. Goal

1. Restore Claude Code adapter (CLAUDE.md, slash commands, adapter README) lost during merge
2. Create new slash commands for all post-TFW-6 workflows (research, review, release, update)
3. Update all existing slash commands and adapters for v0.5 (RESEARCH + reviewer role)
4. Resolve TD-5..TD-9 (adapter/init desyncs from Phase B)
5. Bump version 0.4.2 → 0.5.0, write CHANGELOG

## 2. Scope

### Group A: Restore from backup-research (7 files)

| # | File | Action | Source |
|---|------|--------|--------|
| 1 | `CLAUDE.md` | **RESTORE** from backup → update v0.5 | backup-research |
| 2 | `.claude/commands/tfw-plan.md` | **RESTORE** → add RESEARCH gate reference | backup-research |
| 3 | `.claude/commands/tfw-handoff.md` | **RESTORE** → fix: remove Phase 4 review (now in review.md) | backup-research |
| 4 | `.claude/commands/tfw-resume.md` | **RESTORE** as-is | backup-research |
| 5 | `.claude/commands/tfw-docs.md` | **RESTORE** as-is | backup-research |
| 6 | `.claude/commands/tfw-task.md` | **RESTORE** → add RESEARCH gate mention | backup-research |
| 7 | `.tfw/adapters/claude-code/README.md` | **RESTORE** → add research/review/release/update to table | backup-research |

### Group B: New slash commands (4 files)

| # | File | Action |
|---|------|--------|
| 8 | `.claude/commands/tfw-research.md` | **NEW** — structured investigation, Role Lock COORDINATOR |
| 9 | `.claude/commands/tfw-review.md` | **NEW** — review RF against checklist, Role Lock REVIEWER |
| 10 | `.claude/commands/tfw-release.md` | **NEW** — version bump + CHANGELOG, Role Lock COORDINATOR |
| 11 | `.claude/commands/tfw-update.md` | **NEW** — fetch upstream + compare, Role Lock COORDINATOR |

### Group C: Adapter templates + rules (4 files)

| # | File | Change |
|---|------|--------|
| 12 | `.tfw/adapters/claude-code/CLAUDE.md.template` | Expand: slash command table, RES, research, review, v0.5 |
| 13 | `.tfw/adapters/cursor/tfw.mdc.template` | Templates list +RES, workflows +research/review/release/update, v0.5 |
| 14 | `.tfw/adapters/antigravity/tfw-rules.md.template` | Templates +RES, v0.5 |
| 15 | `.agent/rules/tfw.md` | `TFW v3` → `TFW 0.5`, templates +RES |

### Group D: Antigravity workflow sync (3 files)

| # | File | Change |
|---|------|--------|
| 16 | `.agent/workflows/tfw-plan.md` | Re-copy from `.tfw/workflows/plan.md` (TD-5) |
| 17 | `.agent/workflows/tfw-research.md` | **NEW** — copy from `.tfw/workflows/research.md` |
| 18 | `.agent/workflows/tfw-handoff.md` | Re-copy (has pre-reviewer content) |

### Group E: init.md + README tree (2 files)

| # | File | Change |
|---|------|--------|
| 19 | `.tfw/init.md` | Add `res:` template (TD-6), add `research.md` copy (TD-7) |
| 20 | `.tfw/README.md` | Tree: templates +RES (TD-8), workflows +research (TD-9) |

### Group F: Version + cleanup (3 files)

| # | File | Change |
|---|------|--------|
| 21 | `.tfw/VERSION` | `0.4.2` → `0.5.0` |
| 22 | `.tfw/PROJECT_CONFIG.yaml` | `tfw.version: "0.5.0"` |
| 23 | `.tfw/CHANGELOG.md` | `[0.5.0]` entry |
| 24 | `TECH_DEBT.md` | TD-5..TD-9 → ✅ Resolved |

### Scope Budget

**Budget:** 11 new files, 13 modifications = 24 total.

> ⚠️ Exceeds ≤7 files significantly. Justification:
> - Group A (7 restore): mechanical `git show` + minor edits
> - Group B (4 new): thin slash commands (~30 lines each, role lock + workflow reference, no logic)
> - Group C-F (13 modify): one-line or copy operations
> - Zero new logic — all files are references to canonical workflows
>
> Alternative: split into Phase C (Claude Code) + Phase D (adapters + version). But the user approved combined scope.

## 3. Steps

### Step 1: Restore Claude Code from backup-research

```bash
# Restore as-is, will edit after
git show backup-research:CLAUDE.md > CLAUDE.md
mkdir -p .claude/commands
git show backup-research:.claude/commands/tfw-plan.md > .claude/commands/tfw-plan.md
git show backup-research:.claude/commands/tfw-handoff.md > .claude/commands/tfw-handoff.md
git show backup-research:.claude/commands/tfw-resume.md > .claude/commands/tfw-resume.md
git show backup-research:.claude/commands/tfw-docs.md > .claude/commands/tfw-docs.md
git show backup-research:.claude/commands/tfw-task.md > .claude/commands/tfw-task.md
git show backup-research:.tfw/adapters/claude-code/README.md > .tfw/adapters/claude-code/README.md
```

### Step 2: Update CLAUDE.md for v0.5

- `TFW v3` → `TFW 0.5`
- Slash command table: add `/tfw-research`, `/tfw-review`, `/tfw-release`, `/tfw-update`
- Remove handoff review reference (now in review.md)
- Templates: add RES
- Add `.tfw/CHANGELOG.md` to key references

### Step 3: Update restored slash commands

**tfw-plan.md**: add Phase 3.5 RESEARCH gate reference
**tfw-handoff.md**: remove Phase 4 (review). Add executor STOP block: "Start `/tfw-review`"
**tfw-task.md**: add RESEARCH gate between plan and handoff. Update step 2 for `/tfw-review`
**tfw-resume.md**, **tfw-docs.md**: no changes needed

### Step 4: Create new slash commands

Each follows the pattern: Role Lock → Context Loading → Reference canonical workflow → $ARGUMENTS

**tfw-research.md** — `🔒 COORDINATOR`, ref `.tfw/workflows/research.md`
**tfw-review.md** — `🔒 REVIEWER`, ref `.tfw/workflows/review.md`
**tfw-release.md** — `🔒 COORDINATOR`, ref `.tfw/workflows/release.md`
**tfw-update.md** — `🔒 COORDINATOR`, ref `.tfw/workflows/update.md`

### Step 5: Update CLAUDE.md.template

Expand to full version (from backup), apply v0.5 updates:
- Full context loading order
- Complete slash command table (9 commands)
- RES in templates
- Conduct and execution modes sections

### Step 6: Update adapter README

`.tfw/adapters/claude-code/README.md`:
- Add research, review, release, update to command mapping table
- Update structure diagram with new commands

### Step 7: Adapter templates + rules (Group C)

- Cursor: templates +RES, workflows list complete, v0.5
- Antigravity template: templates +RES, v0.5
- `.agent/rules/tfw.md`: `TFW v3` → `TFW 0.5`, templates +RES

### Step 8: Antigravity workflow sync (Group D)

```bash
cp .tfw/workflows/plan.md .agent/workflows/tfw-plan.md
cp .tfw/workflows/research.md .agent/workflows/tfw-research.md
cp .tfw/workflows/handoff.md .agent/workflows/tfw-handoff.md
```

### Step 9: init.md + README tree (Group E)

- init.md: `res:` в config example, `research.md` в workflow copy commands
- .tfw/README.md: tree comments +RES, +research

### Step 10: Version bump (Group F)

- VERSION: `0.5.0`
- PROJECT_CONFIG: `tfw.version: "0.5.0"`
- CHANGELOG: `[0.5.0]` section
- TECH_DEBT: TD-5..TD-9 → ✅

## 4. CHANGELOG Entry

```markdown
## [0.5.0] — 2026-03-30
### Added
- RESEARCH stage — optional structured investigation between HL and TS (TFW-11)
- `RES.md` template — Research Report artifact
- `research.md` workflow — standalone and pipeline research
- Phase 3.5 RESEARCH gate in `plan.md`
- 🔬 RES status — pipeline now 8-status (RES optional)
- `Read-only AG` mode definition in glossary
- RES in Role Lock Protocol (conventions §15)
- Claude Code adapter: `CLAUDE.md`, 9 slash commands in `.claude/commands/`
- Claude Code adapter: `README.md` setup guide
- `/tfw-research` slash command (Claude Code + Antigravity)
- `/tfw-review` slash command (Claude Code)
- `/tfw-release` slash command (Claude Code)
- `/tfw-update` slash command (Claude Code)
### Changed
- Pipeline diagrams updated in all core files (8-status, RES optional)
- Coordinator role updated: conducts RESEARCH, writes RES files
- All 3 adapter templates updated (RES, full workflow/command lists)
- `CLAUDE.md.template` expanded with slash command table and full context loading
- Antigravity adapter copies synced (plan, research, handoff)
- init.md — RES template in config, research.md in workflow copy commands
- .tfw/README.md — project structure tree updated
```

## 5. Acceptance Criteria

### Claude Code (AC-1..AC-6)
- [ ] AC-1: `CLAUDE.md` exists in root, contains `TFW 0.5` and 9-row slash command table
- [ ] AC-2: `.claude/commands/` has 9 files: plan, handoff, resume, docs, task, research, review, release, update
- [ ] AC-3: tfw-handoff.md has no Phase 4 review, has executor STOP block
- [ ] AC-4: tfw-plan.md references RESEARCH gate
- [ ] AC-5: `.tfw/adapters/claude-code/README.md` exists with command mapping table
- [ ] AC-6: `CLAUDE.md.template` has full slash command table

### Antigravity (AC-7..AC-10)
- [ ] AC-7: `diff .tfw/workflows/plan.md .agent/workflows/tfw-plan.md` → empty
- [ ] AC-8: `.agent/workflows/tfw-research.md` matches source
- [ ] AC-9: `diff .tfw/workflows/handoff.md .agent/workflows/tfw-handoff.md` → empty
- [ ] AC-10: `.agent/rules/tfw.md` shows `TFW 0.5` and RES

### Other adapters (AC-11..AC-12)
- [ ] AC-11: Cursor template has RES + full workflow list
- [ ] AC-12: Antigravity template has RES

### Framework (AC-13..AC-17)
- [ ] AC-13: init.md has `res:` template and `research.md` copy command
- [ ] AC-14: .tfw/README.md tree has RES and research
- [ ] AC-15: VERSION = `0.5.0`, PROJECT_CONFIG version = `"0.5.0"`
- [ ] AC-16: CHANGELOG has `[0.5.0]`
- [ ] AC-17: TD-5..TD-9 ✅ in TECH_DEBT.md

### Regression (AC-18..AC-19)
- [ ] AC-18: `grep "TFW v3" .agent/rules/ .tfw/adapters/ CLAUDE.md` → no results
- [ ] AC-19: `grep "Phase 4" .claude/commands/tfw-handoff.md` → no results (review removed)

## 6. Verification Plan

```bash
# Claude Code
test -f CLAUDE.md && echo "CLAUDE.md exists"
ls .claude/commands/ | wc -l  # expect: 9
grep "TFW 0.5" CLAUDE.md
grep "tfw-research" CLAUDE.md
grep -c "STOP" .claude/commands/tfw-handoff.md  # expect: 1

# Antigravity sync
diff .tfw/workflows/plan.md .agent/workflows/tfw-plan.md
diff .tfw/workflows/research.md .agent/workflows/tfw-research.md
diff .tfw/workflows/handoff.md .agent/workflows/tfw-handoff.md
grep "TFW 0.5" .agent/rules/tfw.md

# Other adapters
grep "RES" .tfw/adapters/cursor/tfw.mdc.template
grep "RES" .tfw/adapters/antigravity/tfw-rules.md.template

# Framework
grep "res:" .tfw/init.md
grep "research.md" .tfw/init.md
cat .tfw/VERSION
grep "0.5.0" .tfw/CHANGELOG.md

# Regression
grep "TFW v3" .agent/rules/tfw.md CLAUDE.md .tfw/adapters/*/tfw*.template || echo "PASS"
grep "Phase 4" .claude/commands/tfw-handoff.md || echo "PASS"
```

## 7. Out of Scope

- `.agent/rules/conventions.md`, `.agent/rules/glossary.md` — project-specific copies, already point to updated `.tfw/` originals
- Historical task artifacts in `tasks/` — trace integrity
- KNOWLEDGE.md updates — will run `/tfw-docs` after REVIEW

---

*TS — TFW-11 / Phase C: Full Adapter Sync + Claude Code Restore + Version 0.5.0 | 2026-03-30*
