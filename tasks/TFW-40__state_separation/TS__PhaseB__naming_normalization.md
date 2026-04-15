# TS — TFW-40 / Phase B: Naming Normalization

> **Date**: 2026-04-15
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-40](HL-TFW-40__state_separation.md)

---

## 1. Objective
Normalize file naming in `.tfw/`: rename `PROJECT_CONFIG.yaml` → `project_config.yaml`, rename `TOPIC_FILE.md` → `topic_file.md`, update all references, add naming convention rule, version bump to 0.8.4 with migration notes.

## 2. Scope

### In Scope
- Rename 2 files
- Update all references across 19+ files in `.tfw/`
- Add YAML naming rule to conventions.md
- Update Config Sync Registry in config.md
- Version bump + CHANGELOG migration notes
- Sync adapters

### Out of Scope
- Renaming adapter templates (`CLAUDE.md.template` — produces `CLAUDE.md` which IS uppercase by root file convention)
- Root-level project files (README.md, AGENTS.md — GitHub convention)

## 3. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/PROJECT_CONFIG.yaml` | RENAME → `project_config.yaml` | Core rename |
| `.tfw/templates/TOPIC_FILE.md` | RENAME → `topic_file.md` | Template rename |
| `.tfw/templates/project_config.yaml` | MODIFY | Update self-reference comment if any |
| `.tfw/conventions.md` | MODIFY | Update all refs + add naming rule |
| `.tfw/glossary.md` | MODIFY | Update refs |
| `.tfw/workflows/plan.md` | MODIFY | Update refs |
| `.tfw/workflows/init.md` | MODIFY | Update refs |
| `.tfw/workflows/update.md` | MODIFY | Update refs |
| `.tfw/workflows/config.md` | MODIFY | Update refs + Config Sync Registry |
| `.tfw/workflows/knowledge.md` | MODIFY | Update refs |
| `.tfw/workflows/release.md` | MODIFY | Update refs |
| `.tfw/workflows/review.md` | MODIFY | Update refs (verify.md template) |
| `.tfw/workflows/research/base.md` | MODIFY | Update refs |
| `.tfw/templates/REVIEW.md` | MODIFY | Update refs |
| `.tfw/templates/review/verify.md` | MODIFY | Update refs |
| `.tfw/compilable_contract.md` | MODIFY | Update refs |
| `.tfw/knowledge_state.yaml` | MODIFY | Update comment ref |
| `.tfw/CHANGELOG.md` | MODIFY | Add v0.8.4 entry |
| `.tfw/VERSION` | MODIFY | Bump to 0.8.4 |
| `.tfw/adapters/claude-code/CLAUDE.md.template` | MODIFY | Update refs |
| `.tfw/adapters/cursor/tfw.mdc.template` | MODIFY | Update refs |
| `.tfw/adapters/antigravity/tfw-rules.md.template` | MODIFY | Update refs |
| `.tfw/adapters/README.md` | MODIFY | Update refs if present |

**Budget:** 0 new files, ~22 modifications, 2 renames. LOC per file is minimal (find-replace). Exceeds max_modified_files (12) but changes are mechanical (rename only). Override justified: all changes are search-replace of one string.

## 4. Detailed Steps

### Step 1: Rename files

```powershell
# In .tfw/ directory:
Rename-Item "PROJECT_CONFIG.yaml" "project_config.yaml"
Rename-Item "templates/TOPIC_FILE.md" "templates/topic_file.md"
```

### Step 2: Global find-replace in .tfw/

Search: `PROJECT_CONFIG.yaml` → Replace: `project_config.yaml`
Search: `PROJECT_CONFIG` (standalone references) → Replace: `project_config.yaml` (contextual)
Search: `TOPIC_FILE.md` → Replace: `topic_file.md`

Apply across all files listed in §3.

### Step 3: Add naming convention to conventions.md

Add to §11 (Quality Standard) or new subsection:

```markdown
### File Naming in `.tfw/`

| File type | Casing | Examples |
|-----------|--------|---------|
| Artifact templates | `UPPER_CASE.md` | `HL.md`, `TS.md`, `RF.md`, `ONB.md`, `RES.md`, `REVIEW.md`, `KNOWLEDGE.md`, `RELEASE.md` |
| Significant root docs | `UPPER_CASE.md` | `README.md`, `CHANGELOG.md`, `VERSION` |
| Framework code | `lower_case.md` | `conventions.md`, `glossary.md`, `quickstart.md`, all workflows |
| Config/State YAML | `lower_case.yaml` | `project_config.yaml`, `knowledge_state.yaml` |
| Stage/mode files | `lower_case.md` | `briefing.md`, `gather.md`, `focused.md`, `map.md`, `verify.md` |

**Rule:** Artifact template names match the UPPER_CASE artifact files they generate. Everything else is lower_case.
```

### Step 4: Update CHANGELOG.md

Add v0.8.4 entry:

```markdown
## [0.8.4] — 2026-04-15

### Added
- `.tfw/templates/knowledge_state.yaml` — clean state template for project init (D47)
- `.tfw/templates/project_config.yaml` — annotated config template with PROJECT/FRAMEWORK markers (D48)
- `conventions.md` §10.3 — File Classification (framework / state / config)
- `update.md` ⚫ STATE category — state files are never overwritten by updates
- File naming convention for `.tfw/` (YAML = lower_case)

### Changed
- `PROJECT_CONFIG.yaml` → `project_config.yaml` (naming normalization) ⚠️ BREAKING
- `templates/TOPIC_FILE.md` → `templates/topic_file.md` (naming normalization)
- `init.md` — template-based creation for state and config files
- `update.md` — explicit state file exclusion and config merge rules

### Migration: v0.8.3 → v0.8.4
1. Rename `.tfw/PROJECT_CONFIG.yaml` → `.tfw/project_config.yaml`
2. Rename `.tfw/templates/TOPIC_FILE.md` → `.tfw/templates/topic_file.md` (if present)
3. Review `.tfw/knowledge_state.yaml`:
   - If `last_consolidation_seq` doesn't match your project → reset to your actual last seq
   - If `stats` values look foreign → zero them out
4. Update adapter files that reference `PROJECT_CONFIG.yaml`
```

### Step 5: Version bump

```
.tfw/VERSION: 0.8.3 → 0.8.4
.tfw/project_config.yaml: tfw.version: "0.8.3" → "0.8.4"
```

### Step 6: Sync adapters

Copy modified workflows to adapter directories per conventions.md §9.

## 5. Acceptance Criteria

- [ ] `grep -r "PROJECT_CONFIG" .tfw/` returns 0 results
- [ ] `grep -r "TOPIC_FILE" .tfw/` returns 0 results
- [ ] `.tfw/project_config.yaml` exists and is valid YAML
- [ ] `.tfw/templates/topic_file.md` exists
- [ ] conventions.md has file naming convention table
- [ ] CHANGELOG has v0.8.4 with migration notes
- [ ] VERSION = 0.8.4
- [ ] All adapter templates updated

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Missed reference to old filename | DoD §9: mechanical grep verification |
| Downstream projects confused by rename | CHANGELOG migration notes with exact steps |
| Config Sync Registry entries stale after rename | Step 2 includes config.md update |

---

*TS — TFW-40 / Phase B: Naming Normalization | 2026-04-15*
