# HL — TFW-40: State/Framework Separation & Naming Normalization

> **Date**: 2026-04-15
> **Author**: Coordinator
> **Status**: 📝 HL_DRAFT — Awaiting review

---

## 1. Vision
`.tfw/` directory has clean boundaries: framework code (workflows, templates, conventions) lives separately from project state (knowledge tracking, project-specific config). Any project can run `tfw-init` or `tfw-update` without inheriting upstream's runtime data. File naming is consistent: YAML files follow `lower_case.yaml` convention.

**Impact:** Every downstream project gets clean initialization. No more phantom knowledge gates, no more inherited stats. Update workflow preserves project identity.

> "I ran tfw-update and nothing broke — my project's state stayed mine, and the framework upgraded seamlessly."

## 2. Current State (As-Is)

### File classification — no boundary

| File | Type | Problem |
|------|------|---------|
| `.tfw/knowledge_state.yaml` | Runtime state | Copied from upstream with seq=38, stats=66 facts. Downstream project has seq=6 |
| `.tfw/PROJECT_CONFIG.yaml` | Hybrid (framework defaults + project identity) | Overwritten/merged ad-hoc. No template. No clear marker of which fields are project-specific |

### Naming inconsistency

| Pattern | Files |
|---------|-------|
| `UPPER_CASE.yaml` | `PROJECT_CONFIG.yaml` |
| `lower_case.yaml` | `knowledge_state.yaml` |

No rule in conventions.md governs YAML file casing.

### Init/Update blind spots

- `init.md` Phase 2 says "Fill `.tfw/PROJECT_CONFIG.yaml`" — no mention of knowledge_state.yaml at all
- `update.md` has no state file exclusion list. Step 3 classifies files as 🟢🟡🔴 but doesn't know about state files
- No template exists for knowledge_state.yaml — it's always copied from upstream

## 3. Target State (To-Be)

### 3.1 Result Visualization

**Before (tfw-init):**
```
Clone upstream → copy .tfw/ → knowledge_state has seq=38, 66 facts → gate broken
```

**After (tfw-init):**
```
Clone upstream → copy .tfw/ framework files
                → create .tfw/knowledge_state.yaml FROM template (seq=0, stats=0)
                → create .tfw/project_config.yaml FROM template → fill project values
                → clean state, gate works correctly
```

**Before (tfw-update):**
```
Clone upstream → diff all .tfw/ files → knowledge_state overwritten with upstream data → gate broken
```

**After (tfw-update):**
```
Clone upstream → diff framework files only
              → SKIP state files (knowledge_state.yaml)
              → MERGE config (framework sections update, project sections preserved)
              → project state untouched
```

### 3.2 Value Flow

```
INIT:  upstream repo ──→ copy FRAMEWORK files ──→ create STATE from templates ──→ fill CONFIG via interview
                         (workflows, templates,    (knowledge_state.yaml)           (project_config.yaml)
                          conventions, glossary)

UPDATE: upstream repo ──→ diff FRAMEWORK files ──→ SKIP state files ──→ MERGE config ──→ sync adapters
                          (🟢🟡🔴 categories)     (never overwrite)     (framework     
                                                                         sections only)
```

## 4. Phases

### Phase A: State Separation & Templates 🔴

> **Requires:** Independent
>
> **Context for coordinator:**
> 1. `.tfw/knowledge_state.yaml` — current upstream state (seq=38)
> 2. `.tfw/workflows/init.md` — Phase 2 (Mini-Setup), Phase 4 (Full Setup)
> 3. `.tfw/workflows/update.md` — Step 3 (Categorize), Step 5 (Execute)
> 4. `.tfw/conventions.md` §10.2 (Knowledge Infrastructure)
>
> **Key decisions:** D47 (state file classification), D48 (template-based init)
>
> **Deliverables:**
> 1. `.tfw/templates/knowledge_state.yaml` — clean state template (all zeros)
> 2. `.tfw/templates/project_config.yaml` — clean config template with PROJECT/FRAMEWORK annotations
> 3. Updated `init.md` — template-based creation for state + config
> 4. Updated `update.md` — state file exclusion + config merge rules
> 5. Updated `conventions.md` — §10.3 "File Classification in .tfw/"
> 6. Reset upstream `knowledge_state.yaml` to clean state (framework repo = starter)

### Phase B: Naming Normalization 🟡

> **Requires:** Phase A ✅
>
> **Shared files with Phase A:** conventions.md, glossary.md
>
> **Context for coordinator:**
> 1. All 19 files referencing `PROJECT_CONFIG.yaml` (grep results)
> 2. `.tfw/workflows/config.md` — Config Sync Registry
> 3. Adapter templates in `.tfw/adapters/`
>
> **Deliverables:**
> 1. Rename `PROJECT_CONFIG.yaml` → `project_config.yaml`
> 2. Rename `templates/TOPIC_FILE.md` → `templates/topic_file.md`
> 3. Update all 19+ files referencing old names
> 4. Update Config Sync Registry
> 5. Add naming convention rule to conventions.md
> 6. Migration notes in CHANGELOG.md
> 7. Version bump to 0.8.4

## 5. Definition of Done (DoD)

- ✅ 1. `tfw-init` creates `knowledge_state.yaml` from template (seq=0)
- ✅ 2. `tfw-init` creates `project_config.yaml` from template
- ✅ 3. `tfw-update` never overwrites `knowledge_state.yaml`
- ✅ 4. `tfw-update` merges `project_config.yaml` (framework only)
- ✅ 5. conventions.md has §10.3 file classification
- ✅ 6. All YAML files follow `lower_case.yaml` convention
- ✅ 7. Zero references to `PROJECT_CONFIG.yaml` (old name) in `.tfw/`
- ✅ 8. CHANGELOG has migration notes for v0.8.3→v0.8.4
- ✅ 9. `grep -r "PROJECT_CONFIG" .tfw/` returns 0 results

## 6. Definition of Failure (DoF)

- ❌ 1. Downstream projects break on update because references to `project_config.yaml` don't match old filename
- ❌ 2. Knowledge gate still shows inherited values after clean init

**On failure:** Revert naming changes (Phase B), keep state separation (Phase A) as standalone fix.

## 7. Principles

1. **State is sacred** — project runtime state must never be overwritten by framework updates
2. **Templates over copies** — state files created from explicit templates, not cloned from upstream
3. **Consistent naming** — one casing rule per file type, no exceptions
4. **Annotations over documentation** — inline `# ← PROJECT` / `# ← FRAMEWORK` markers in config beat external mapping docs

### 7.2 Knowledge Citations

| # | Source | Item | How it applies |
|---|--------|------|----------------|
| K1 | KNOWLEDGE.md §1 D22 | Knowledge consolidation: knowledge_state.yaml as state tracker | Direct — this is the broken file |
| K2 | KNOWLEDGE.md §1 D24 | Pattern A (inline defaults + config key) | Config template should use Pattern A for inline values |
| K3 | KNOWLEDGE.md §1 D36 | Agent-first onboarding: quickstart.md + init.md separation | Init workflow changes must preserve D36 design |
| K4 | conventions.md §10.2 | Knowledge Infrastructure file listing | Must update to reflect new template paths |
| K5 | conventions.md §9 | Tool Adapter Pattern | Adapter re-sync after workflow changes |
| K6 | knowledge/convention.md | Naming conventions | Must add YAML casing rule |
| K7 | KNOWLEDGE.md §1 D11 | tfw-update with 🟢🟡🔴 categorization | Must extend with ⚫ (state, never touch) category |

## 8. Dependencies
| Dependency | Status |
|------------|--------|
| No external dependencies | ✅ |

## 9. Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Rename breaks downstream adapters | Medium | High | Clear migration notes + version bump |
| Missed reference to old filename | Medium | Low | Grep verification in DoD §9 |
| Upstream repo loses own state after reset | Low | Medium | Template coexists with live state; only init copies from template |

## 10. RESEARCH Case

### Blind Spots
- None significant — problem is well-understood, solution is structural

### Hypotheses

| # | Hypothesis | Status |
|---|----------|--------|
| H1 | knowledge_state.yaml is the only state file in .tfw/ | confirmed — audit done |
| H2 | All 19 PROJECT_CONFIG references can be mechanically renamed | confirmed — grep shows all |

### Risks of Not Researching
Low risk. Problem is internal, solution is mechanical. RESEARCH not recommended.

### Why Not Just...?
- Why not just add knowledge_state.yaml to .gitignore in upstream? — It IS needed for TFW's own project. And init.md needs to create it for new projects.
- Why not keep PROJECT_CONFIG.yaml uppercase? — Inconsistent with knowledge_state.yaml. User explicitly asked for normalization. Rule clarity > backward compatibility.

## 11. Strategic Insights (Planning)

> strategic-insights: processed 2026-04-15

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | User identified that init/update contamination is a systemic issue, not just knowledge_state.yaml. PROJECT_CONFIG.yaml had the same problem class | philosophy | User, initial report |
| S2 | User values naming consistency ("у нас то большие буквы, то маленькие. плохо") — this is a design principle, not just aesthetics | convention | User, follow-up |
| S3 | User suggested "template for init" — the template-based approach for state files came from user insight, not framework analysis | process | User, initial report |
| S4 | User recalled TFW-16 (tfw-doctor) — "помочь перепроверять самого себя и починить мета информацию". Concrete use case: verify knowledge_state.yaml values match project reality after update. tfw-doctor = self-diagnosis of TFW meta-state. Link to TFW-16 | process | User, ONB discussion |

---

*HL — TFW-40: State/Framework Separation & Naming Normalization | 2026-04-15*
