# HL — TFW-12: Config Centralization (Scope Budgets + Version String)

> **Status**: 🔵 HL (draft v2)
> **Author**: Coordinator (AI)
> **Date**: 2026-03-30

---

## 1. Vision

Two types of values are hardcoded across many `.tfw/` files:

1. **Scope budgets** (≤7 files, ≤4 new, ≤600 LOC, ≤6 modified) — in 6 live files
2. **Version strings** (`TFW 0.5`, `0.5.0`) — in ~17 places

Changing either requires manually updating every file. TFW-11/C just demonstrated the pain: version bump from 0.4→0.5 touched 13+ files.

**Goal**: define both in `PROJECT_CONFIG.yaml` as single source of truth. All other files reference the config, not hardcode values. When a project bumps version or adjusts budgets, one YAML edit propagates everywhere.

## 2. As-Is

### Scope Budgets — hardcoded in 6 live files

| File | Occurrences |
|------|------------|
| `.tfw/conventions.md` (§6) | 4 values: ≤7, ≤4, ≤600, ≤6 |
| `.tfw/README.md` (§Scope Budgets) | 4 values (duplicate) |
| `.tfw/workflows/plan.md` (§Scope Budget) | 4 values (duplicate) |
| `.tfw/glossary.md` (Phase def) | 3 values inline |
| `.tfw/templates/TS.md` | 3 values inline |
| `README.md` (root, Key Concepts) | 2 values inline |

### Version Strings — hardcoded in ~17 places

| File | Content |
|------|---------|
| `.tfw/VERSION` | `0.5.0` — **this stays** (machine-readable) |
| `.tfw/PROJECT_CONFIG.yaml` | `tfw.version: "0.5.0"` — **this is the source** |
| `.tfw/conventions.md` L1 | `# TFW 0.4 — Conventions` ← stale |
| `.tfw/glossary.md` L1 | `# TFW 0.4 Glossary` ← stale |
| `.tfw/README.md` L151, L166, L209 | `TFW 0.5 enforces...` |
| `.tfw/init.md` L1, L196 | `# TFW 0.5 — Quick Start` |
| `.tfw/adapters/claude-code/CLAUDE.md.template` L15-16 | `TFW 0.5` |
| `.tfw/adapters/cursor/tfw.mdc.template` L2, L6 | `TFW 0.5` |
| `.tfw/adapters/antigravity/tfw-rules.md.template` L5 | `TFW 0.5` |
| `.tfw/adapters/antigravity/README.md` L34 | `TFW 0.4` ← stale |
| `CLAUDE.md` L1, L5 | `TFW 0.5` |
| `README.md` (root) | `Current version: 0.5.0` |

### Current PROJECT_CONFIG.yaml

```yaml
tfw:
  version: "0.5.0"
  # no scope_budgets section
```

## 3. To-Be

### PROJECT_CONFIG.yaml — single source of truth

```yaml
tfw:
  version: "0.5.0"
  scope_budgets:
    max_files_per_phase: 7
    max_new_files: 4
    max_loc: 600
    max_modified_files: 6
```

### Version strings → reference

**Before** (conventions.md):
```
# TFW 0.4 — Conventions
```

**After**:
```
# TFW Conventions
```

Drop the version from titles entirely. The version is tracked in `PROJECT_CONFIG.yaml` and `VERSION` file. Having it in document titles creates drift (proven by TD-25: conventions/glossary still say 0.4 after bump to 0.5).

**Adapter templates** — use placeholder:
```
# TFW {version}
```
Agent reads version from PROJECT_CONFIG.yaml when instantiating.

**Root README** — reference:
```
- **Current version**: see `.tfw/VERSION` — [changelog](.tfw/CHANGELOG.md)
```

### Scope budgets → reference

Same pattern as HL v1: replace hardcoded values with references to `PROJECT_CONFIG.yaml`.

## 4. Principles

1. **One truth** — numbers and version live ONLY in PROJECT_CONFIG.yaml (+ VERSION file for machine-readable semver)
2. **VERSION file stays** — `tfw-release` workflow reads it, `tfw-update` reads it. It's the machine-readable canonical source, PROJECT_CONFIG mirrors it.
3. **No version in titles** — removes the #1 source of drift. Titles become version-agnostic.
4. **Trace integrity** — historical task artifacts never modified.
5. **Adapter templates use placeholders** — `{version}` resolved on copy by init.md instructions.

## 5. Phases

### Phase A: Config + Scope Budgets

Add `scope_budgets` section to PROJECT_CONFIG.yaml. Update canonical definition in `conventions.md` (§6). De-duplicate from README, plan.md, glossary.md, TS.md template, root README.

**Files**: PROJECT_CONFIG.yaml, conventions.md, .tfw/README.md, plan.md, glossary.md, TS.md template, root README.md
**Budget**: 0 new, 7 modified

### Phase B: Version String Cleanup

Remove hardcoded version from titles in core files. Update adapter templates with `{version}` placeholder. Fix stale 0.4 references (TD-25). Update init.md instructions.

**Files**: conventions.md, glossary.md, .tfw/README.md, init.md, 3 adapter templates, antigravity README, CLAUDE.md, root README
**Budget**: 0 new, ~10 modified (mechanical one-line edits)

## 6. DoD

- [ ] `tfw.scope_budgets` exists in PROJECT_CONFIG.yaml with 4 values
- [ ] grep `≤ 7|≤ 4|≤ 600|≤ 6` in `.tfw/` returns 0 hardcoded values
- [ ] No `TFW 0.X` in document titles (conventions, glossary, README)
- [ ] Adapter templates use `{version}` placeholder
- [ ] init.md instructs user to set version from PROJECT_CONFIG
- [ ] TD-25 resolved (conventions/glossary title fix)
- [ ] No changes to `tasks/` (historical integrity)

## 7. DoF

- Hardcoded budget/version values remain in any live `.tfw/` file
- Historical task artifacts modified
- VERSION file removed or disconnected from PROJECT_CONFIG
- Version appears in document titles

## 8. Risks

| Risk | Mitigation |
|------|------------|
| Titles without version less informative | VERSION file + PROJECT_CONFIG are the canonical sources; titles link to them |
| Agent confusion during template instantiation | init.md documents the `{version}` replacement step |
| Downstream projects miss scope_budgets config | init.md example shows it; tfw-update flags new fields |

---

*HL — TFW-12: Config Centralization (Scope Budgets + Version String) | 2026-03-30*
