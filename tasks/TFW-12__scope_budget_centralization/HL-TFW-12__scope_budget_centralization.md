# HL — TFW-12: Scope Budget Centralization

> **Status**: 🔵 HL (draft)
> **Author**: Coordinator (AI)
> **Date**: 2026-03-30

---

## 1. Vision

Scope budget values (≤7 files, ≤4 new, ≤600 LOC, ≤6 modified) are currently hardcoded in **6 live `.tfw/` files** and the root README. When a project needs different limits, there is no single place to change them — every file must be manually updated.

**Goal**: define scope budgets once in `.tfw/PROJECT_CONFIG.yaml` and reference them from everywhere else. Changing one YAML field instantly changes the effective limit across the whole framework.

## 2. As-Is

### Hardcoded budget values (live files)

| File | Occurrences | Content |
|------|------------|---------|
| `.tfw/conventions.md` (§6) | 4 values | Full table: ≤7, ≤4, ≤600, ≤6 |
| `.tfw/README.md` (§Scope Budgets) | 4 values | Full table (duplicate of conventions) |
| `.tfw/workflows/plan.md` (§Scope Budget) | 4 values | Full table (duplicate of conventions) |
| `.tfw/glossary.md` (Phase def) | 3 values | Inline: «≤7 files, ≤600 LOC, ≤4 new files» |
| `.tfw/templates/TS.md` | 3 values | Inline: «≤7 файлов, ≤4 новых, ≤600 LOC» |
| `README.md` (Key Concepts) | 2 values | Inline: «≤7 files, ≤600 LOC per phase» |

**Total**: 6 live files × 3-4 values each = ~20 hardcoded values.

### Historical task artifacts (NOT in scope)

8 TS/RF files in `tasks/` contain hardcoded budget values in their Scope Budget sections. These are **frozen historical records** — modifying them would violate trace integrity.

### Current PROJECT_CONFIG.yaml

No `scope_budgets` section exists. The file has: `project`, `tfw`, `build`.

## 3. To-Be

### PROJECT_CONFIG.yaml — single source of truth

```yaml
tfw:
  scope_budgets:
    max_files_per_phase: 7        # Total files touched per phase
    max_new_files: 4              # New files created per phase
    max_loc: 600                  # New lines of code per phase
    max_modified_files: 6         # Existing files modified per phase
```

### All live files — reference, don't duplicate

Each file replaces hardcoded values with a reference to PROJECT_CONFIG.yaml. Pattern:

**Before** (conventions.md):
```
| Files per phase | ≤ 7 | Agent maintains full mental model |
```

**After**:
```
| Files per phase | per `tfw.scope_budgets` in PROJECT_CONFIG.yaml | Agent maintains full mental model |
```

The exact phrasing depends on context:
- **Tables** (conventions, README, plan.md): replace value column with reference
- **Inline** (glossary, root README): replace specific numbers with a reference phrase
- **Templates** (TS.md): replace hardcoded values with `{scope_budgets}` placeholder instruction

## 4. Principles

1. **One truth** — numbers live ONLY in PROJECT_CONFIG.yaml
2. **No silent defaults** — if PROJECT_CONFIG.yaml is missing `scope_budgets`, the agent should fail visibly, not assume defaults
3. **Trace integrity** — historical task artifacts (TS/RF in `tasks/`) are never modified
4. **init.md updated** — the config example in init.md must show `scope_budgets` section

## 5. Phases

### Phase A: Config + Canonical Reference Point

Add `scope_budgets` section to PROJECT_CONFIG.yaml and update the **canonical definition** in `conventions.md` (§6) — the one authoritative location where budgets are defined with rationale. All other files will reference this.

**Files**: PROJECT_CONFIG.yaml, conventions.md, init.md (config example)
**Budget**: 0 new, 3 modified

### Phase B: De-duplicate from Descriptive Files

Remove hardcoded values from files that **duplicate** the conventions table: `.tfw/README.md`, `plan.md`, `glossary.md`, root `README.md`, `TS.md` template.

**Files**: 5 modified
**Budget**: 0 new, 5 modified

## 6. DoD (Definition of Done)

- [ ] `tfw.scope_budgets` section exists in PROJECT_CONFIG.yaml with all 4 values
- [ ] `conventions.md` §6 table references PROJECT_CONFIG.yaml values
- [ ] `.tfw/README.md` scope budgets section references conventions.md / PROJECT_CONFIG.yaml
- [ ] `plan.md` scope budget table references PROJECT_CONFIG.yaml
- [ ] `glossary.md` Phase definition references PROJECT_CONFIG.yaml
- [ ] `TS.md` template uses reference, not hardcoded values
- [ ] `README.md` (root) Key Concepts references PROJECT_CONFIG.yaml
- [ ] `init.md` config example includes `scope_budgets`
- [ ] grep `≤ 7|≤ 4|≤ 600|≤ 6` in `.tfw/` returns 0 hardcoded values in live files
- [ ] No changes to files in `tasks/` (historical integrity)

## 7. DoF (Definition of Failure)

- Hardcoded budget values remain in any live `.tfw/` file
- Historical task artifacts are modified
- No reference path from documents to PROJECT_CONFIG.yaml
- Budget values exist in two or more canonical locations

## 8. Risks

| Risk | Mitigation |
|------|------------|
| Agent confusion — references less readable than inline values | Keep rationale column in tables; reference is just the value |
| Downstream projects miss the new config section | init.md covers it; tfw-update workflow flags new fields |

---

*HL — TFW-12: Scope Budget Centralization | 2026-03-30*
