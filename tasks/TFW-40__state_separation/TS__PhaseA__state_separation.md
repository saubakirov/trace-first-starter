# TS — TFW-40 / Phase A: State Separation & Templates

> **Date**: 2026-04-15
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-40](HL-TFW-40__state_separation.md)

---

## 1. Objective
Establish the state/framework boundary in `.tfw/`. Create templates for state files, update init.md and update.md to use them, and add file classification to conventions.md. Fix the root cause of the knowledge gate contamination bug.

## 2. Scope

### In Scope
- Create `.tfw/templates/knowledge_state.yaml` (clean template)
- Create `.tfw/templates/project_config.yaml` (annotated template)
- Update `init.md` — template-based state/config creation
- Update `update.md` — state exclusion list + config merge rules + new ⚫ STATE category
- Update `conventions.md` — add §10.3 File Classification
- Reset `.tfw/knowledge_state.yaml` in upstream to zeros (keep stats accurate for TFW project since it uses the template concept)

### Out of Scope
- Rename `PROJECT_CONFIG.yaml` → `project_config.yaml` (Phase B)
- Rename `TOPIC_FILE.md` → `topic_file.md` (Phase B)
- Reference updates (Phase B)

## 3. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/templates/knowledge_state.yaml` | CREATE | Clean state template (all zeros) |
| `.tfw/templates/project_config.yaml` | CREATE | Annotated config template with PROJECT/FRAMEWORK markers |
| `.tfw/workflows/init.md` | MODIFY | Phase 2: create state from template, config from template |
| `.tfw/workflows/update.md` | MODIFY | Add ⚫ STATE category, config merge rules |
| `.tfw/conventions.md` | MODIFY | Add §10.3 File Classification in .tfw/ |

**Budget:** 2 new files, 3 modifications. Within defaults: max 14 files, max 8 new, max 1200 LOC.

## 4. Detailed Steps

### Step 1: Create knowledge_state.yaml template

Create `.tfw/templates/knowledge_state.yaml`:

```yaml
# Knowledge consolidation state — updated by /tfw-knowledge
# Configuration (interval, gate_mode, limits) → see tfw.knowledge in PROJECT_CONFIG.yaml
knowledge:
  last_consolidation_seq: 0
  last_consolidation_date: null
  stats:
    total_facts: 0
    verified: 0
    unverified: 0
    rejected: 0
    candidates_processed: 0
    sources_scanned: 0
```

### Step 2: Create project_config.yaml template

Create `.tfw/templates/project_config.yaml` — copy of current `PROJECT_CONFIG.yaml` with:
- `project.*` fields set to placeholder values (`my-project`, `user/my-project`, `main`)
- `tfw.task_prefix` set to `PROJ`
- `tfw.initial_seq` set to `1`
- `tfw.content_language` set to `en`
- `build.*` set to echo placeholders
- Remove `stack` section entirely (project-specific, not in template)
- Add inline annotations: `# ← PROJECT: set during init` and `# ← FRAMEWORK: updated by tfw-update`
- Keep all `tfw.scope_budgets`, `tfw.templates`, `tfw.workflows`, `tfw.research`, `tfw.review`, `tfw.knowledge`, `tfw.statuses` as framework defaults

### Step 3: Update init.md

In Phase 2 (Mini-Setup), after interview, change step 1 from "Fill `.tfw/PROJECT_CONFIG.yaml`" to:

```markdown
1. Copy `.tfw/templates/project_config.yaml` → `.tfw/PROJECT_CONFIG.yaml`
   Fill with discovered + interview data (project.*, tfw.task_prefix, initial_seq, content_language, build.*)
2. Copy `.tfw/templates/knowledge_state.yaml` → `.tfw/knowledge_state.yaml`
   (no modifications needed — clean state)
3. Create `tasks/` directory
...
```

Add anti-pattern:
```
- Agent copies knowledge_state.yaml directly from upstream instead of from template
```

### Step 4: Update update.md

In Step 3 (Categorize Changes), add a new category BEFORE the existing three:

```markdown
| Category | Symbol | Meaning | Action |
|----------|--------|---------|--------|
| State | ⚫ | Project runtime state — never part of framework | **NEVER overwrite.** Skip entirely |
| Safe | 🟢 | New file, or file not customized by project | Copy from upstream |
| Merge | 🟡 | File exists and may have project-specific changes | Manual review + merge |
| Breaking | 🔴 | File removed, renamed, or structurally changed | Follow CHANGELOG |

### Files that are project state (⚫ — NEVER overwrite):
- `.tfw/knowledge_state.yaml` — project knowledge consolidation tracking
- `knowledge/` — project-specific verified facts (NOT from upstream)
- `KNOWLEDGE.md` — project knowledge index (NOT from upstream)
- `TECH_DEBT.md` — project tech debt (NOT from upstream)

### Files requiring merge (🟡):
- `.tfw/PROJECT_CONFIG.yaml` — project has custom values
  **Project sections** (preserve): `project.*`, `tfw.task_prefix`, `tfw.initial_seq`, 
  `tfw.content_language`, `build.*`, `stack.*`, `tfw.user_preferences`
  **Framework sections** (update): `tfw.version`, `tfw.templates`, `tfw.workflows`,
  `tfw.statuses`, `tfw.scope_budgets`, `tfw.research`, `tfw.review`, `tfw.knowledge`
```

### Step 5: Update conventions.md

Add §10.3 after §10.2 (Knowledge Infrastructure):

```markdown
## 10.3) File Classification in `.tfw/`

`.tfw/` contains three categories of files with different lifecycle rules:

| Category | Files | Init | Update | Owner |
|----------|-------|------|--------|-------|
| **Framework** | workflows/, templates/, conventions.md, glossary.md, README.md, CHANGELOG.md, VERSION, compilable_contract.md, quickstart.md, adapters/ | Copy from upstream | Overwrite/merge from upstream | Upstream repo |
| **State** | knowledge_state.yaml | Create from template | **NEVER** overwrite | Project (tfw-knowledge) |
| **Config** | PROJECT_CONFIG.yaml | Create from template → fill project values | Merge: framework sections update, project sections preserve | Project + upstream |

**Templates** for state and config files: `.tfw/templates/knowledge_state.yaml`, `.tfw/templates/project_config.yaml`.

**Rule:** `init.md` and `update.md` MUST respect these categories. State files are NEVER sourced from upstream — only from templates.
```

## 5. Acceptance Criteria

- [ ] `.tfw/templates/knowledge_state.yaml` exists with all zeros
- [ ] `.tfw/templates/project_config.yaml` exists with placeholder project values and PROJECT/FRAMEWORK annotations
- [ ] `init.md` Phase 2 references templates for state and config creation
- [ ] `init.md` has anti-pattern about direct upstream copy
- [ ] `update.md` Step 3 has ⚫ STATE category with exclusion list
- [ ] `update.md` Step 3 has explicit merge rules for PROJECT_CONFIG (project vs framework sections)
- [ ] `conventions.md` §10.3 documents the 3-category classification
- [ ] A new project initialized via init.md would get knowledge_state with seq=0

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Template drifts from actual PROJECT_CONFIG structure | Template created from current CONFIG; future changes must update both (add to config.md anti-patterns) |

---

*TS — TFW-40 / Phase A: State Separation & Templates | 2026-04-15*
