# TS — TFW-19: Config Propagation

> **Дата**: 2026-04-03
> **Автор**: Coordinator (AI)
> **Статус**: 🟡 TS_DRAFT — Ожидает апрува
> **Parent HL**: [HL-TFW-19](HL-TFW-19__config_propagation.md)

---

## 1. Цель

Restore inline config values (Pattern A) in all enforcement-critical workflows, create `/tfw-config` interactive workflow for config sync, and resolve TD-48 (Naming Rules duplication).

## 2. Scope

### In Scope
- Restore inline budget tables in plan.md, conventions.md
- Add inline limits tables in knowledge.md
- Fix TS.md template budget line
- Restore «defaults» wording in research.md
- Add enforcement hook in plan.md Phase 5
- Create config.md workflow (edit + verify modes) with Config Sync Registry
- Create adapter, update conventions.md §8/§15, glossary.md
- Sync all adapters

### Out of Scope
- tfw-update integration (future)
- Pre-commit hooks
- Status, template, workflow list propagation (lookup, not enforcement)

## 3. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/workflows/plan.md` | MODIFY | Restore budget table (compact), add enforcement hook in Phase 5 |
| `.tfw/conventions.md` | MODIFY | Restore budget table (full, with Rationale) in §6 |
| `.tfw/workflows/knowledge.md` | MODIFY | Add §Limits table (compact) |
| `.tfw/templates/TS.md` | MODIFY | Replace L27 with inline defaults |
| `.tfw/workflows/research.md` | MODIFY | Restore «defaults» wording in Limits header |
| `.tfw/workflows/config.md` | CREATE | Interactive config sync workflow + Config Sync Registry |
| `.agent/workflows/tfw-config.md` | CREATE | Antigravity adapter (copy of config.md) |
| `.tfw/conventions.md` | MODIFY | Add config.md to §8, §15 |
| `.tfw/glossary.md` | MODIFY | Add Config Sync Registry term |
| `.agent/workflows/tfw-plan.md` | MODIFY | Adapter sync |
| `.agent/workflows/tfw-research.md` | MODIFY | Adapter sync |

**Бюджет:** 2 новых файла, 9 модификаций. Defaults: max 14 files, max 8 new, max 1200 LOC.

## 4. Детальные шаги

### Step 1: Restore budget table in plan.md

Replace L133-137 «See config» with Pattern A compact table:

```markdown
#### Scope Budget per Phase

> Configured in `.tfw/PROJECT_CONFIG.yaml` (`tfw.scope_budgets`).
> Values below are defaults. Override in PROJECT_CONFIG for your project.

| Parameter | Default | Config key |
|-----------|---------|------------|
| Files per phase | 14 | `max_files_per_phase` |
| New files per phase | 8 | `max_new_files` |
| LOC per phase | 1200 | `max_loc` |
| Modified files | 12 | `max_modified_files` |

> **If a phase exceeds the budget — split it further.**
```

### Step 2: Add enforcement hook in plan.md Phase 5

Before «Write TS», add:

```markdown
> **Budget Check**: Read `tfw.scope_budgets` from PROJECT_CONFIG.yaml.
> Verify this phase fits within the configured limits (see §Scope Budget per Phase).
> If exceeds — split the phase or document user override in TS.
```

### Step 3: Restore budget table in conventions.md §6

Replace L132-135 «See config» with Pattern A full table (with Rationale):

```markdown
## 6) Scope Budgets (per Phase)

> Configured in `.tfw/PROJECT_CONFIG.yaml` (`tfw.scope_budgets`).
> Values below are defaults. Override in PROJECT_CONFIG for your project.

| Parameter | Default | Rationale | Config key |
|-----------|---------|-----------|------------|
| Files per phase | 14 | Agent maintains full context of changed files | `max_files_per_phase` |
| New files per phase | 8 | Limits blast radius of new abstractions | `max_new_files` |
| LOC per phase | 1200 | Keeps changes reviewable in one pass | `max_loc` |
| Modified files | 12 | Prevents scattered, hard-to-review diffs | `max_modified_files` |
```

### Step 4: Add limits table in knowledge.md

Add after Anti-patterns section:

```markdown
## Limits

> Configured in `.tfw/PROJECT_CONFIG.yaml` (`tfw.knowledge`).
> Values below are defaults. Override in PROJECT_CONFIG for your project.

| Parameter | Default | Config key |
|-----------|---------|------------|
| Consolidation interval | 5 tasks | `interval` |
| Gate mode | hard | `gate_mode` |
| Max facts per topic | 50 | `max_facts_per_topic` |
| Max topic files | 8 | `max_topic_files` |
```

### Step 5: Fix TS.md template budget line

Replace L27 with:

```markdown
**Бюджет:** {N} новых файлов, {M} модификаций. Defaults: max {max_files} files, max {max_new} new, max {max_loc} LOC.
```

Coordinator fills in actual values from PROJECT_CONFIG when writing TS.

### Step 6: Restore «defaults» wording in research.md

Replace L142:
```
> Research limits are configured in `.tfw/PROJECT_CONFIG.yaml` (`tfw.research`).
```
With:
```
> Configured in `.tfw/PROJECT_CONFIG.yaml` (`tfw.research`).
> Values below are defaults. Override in PROJECT_CONFIG for your project.
```

### Step 7: Create config.md workflow

Create `.tfw/workflows/config.md` with:

1. **Role Lock**: Coordinator
2. **Two modes**: Edit (interactive) and Verify (audit)
3. **Edit mode UX**:
   - Agent asks: «Что хотите изменить в конфигурации?»
   - User answers with config key and value
   - Agent reads YAML, reads all registry targets, proposes batch update
   - User approves → agent updates files + syncs adapters
4. **Verify mode**: read YAML + all targets, report mismatches
5. **Config Sync Registry**: table mapping config keys → file locations (section header + row label)
6. **Adapter sync step**: after any change, copy modified workflows to adapter folders

Registry must cover:
- `scope_budgets.*` → plan.md, conventions.md
- `research.*` → research.md
- `knowledge.*` → knowledge.md

### Step 8: Update conventions.md §8 + §15

Add `config.md` row to §8 Workflows table:
```
| [config.md](workflows/config.md) | Coordinator | Interactive config change → propagate to all inline values |
```

Add to §15 Role Lock:
```
| `config.md` | Coordinator | PROJECT_CONFIG.yaml, workflow files, convention files, adapter copies | code |
```

### Step 9: Add glossary term

Add after Consolidation term:

```markdown
### Config Sync Registry
A table in `config.md` workflow that maps `PROJECT_CONFIG.yaml` keys to their inline display locations in workflows and conventions. AI agent reads the registry to find where values appear, compares with YAML, and proposes updates. Ensures single source of truth (YAML) with inline visibility (rendered defaults).
```

### Step 10: Sync adapters

Copy modified workflows to `.agent/workflows/`:
- `tfw-plan.md` ← plan.md
- `tfw-research.md` ← research.md
- `tfw-config.md` ← config.md (new)

### Step 11: Resolve TD-48

Mark TD-48 as resolved in TECH_DEBT.md (Naming Rules removed from plan.md in this task).

## 5. Acceptance Criteria

- [ ] plan.md has inline budget table with 4 rows matching PROJECT_CONFIG values
- [ ] plan.md has enforcement hook in Phase 5
- [ ] plan.md does NOT contain Naming Rules table (TD-48)
- [ ] conventions.md §6 has inline budget table with 4 rows + Rationale column
- [ ] conventions.md §4 has multi-phase subfolder structure
- [ ] knowledge.md has §Limits table with 4 rows
- [ ] TS.md template L27 has inline defaults format
- [ ] research.md Limits header says «defaults»
- [ ] config.md workflow exists with edit + verify modes + Config Sync Registry
- [ ] Config Sync Registry covers all 3 config categories (scope_budgets, research, knowledge)
- [ ] conventions.md §8 lists config.md, §15 has config.md Role Lock
- [ ] glossary.md has Config Sync Registry term
- [ ] Antigravity adapter `tfw-config.md` exists
- [ ] All adapters synced (plan, research, config)
- [ ] All inline values match current PROJECT_CONFIG.yaml values

## 6. Verification

```bash
# Verify inline values match config
grep -n "14" .tfw/workflows/plan.md    # max_files_per_phase
grep -n "1200" .tfw/workflows/plan.md  # max_loc
grep -n "50" .tfw/workflows/knowledge.md  # max_facts_per_topic
grep -n "defaults" .tfw/workflows/research.md  # defaults wording

# Verify no Naming Rules in plan.md
grep -c "Naming Rules" .tfw/workflows/plan.md  # should be 0

# Verify config.md exists
ls -la .tfw/workflows/config.md
ls -la .agent/workflows/tfw-config.md

# Verify conventions references
grep "config.md" .tfw/conventions.md  # should appear in §8 and §15
```

## 7. Риски фазы

| Риск | Mitigation |
|------|------------|
| Inline defaults get inconsistent wording across files | Step 6 establishes standard header; use exact copy |
| Config Sync Registry misses an entry | AC #10 requires all 3 categories. Verify with grep |
| Word count increase conflicts with P10 | Tables are ~40-60 words each. Total +200 words across 4 files. Negligible |

---

*TS — TFW-19: Config Propagation | 2026-04-03*
