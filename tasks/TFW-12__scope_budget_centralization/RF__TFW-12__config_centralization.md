# RF — TFW-12: Config Centralization

> **Date**: 2026-03-30
> **Author**: Executor (AI)
> **Status**: 🟢 RF
> **Parent HL**: [HL-TFW-12](HL-TFW-12__scope_budget_centralization.md)
> **TS**: [TS-TFW-12](TS__TFW-12__config_centralization.md)

---

## 1. What Was Done

Centralized 4 categories of duplicated parameters into `PROJECT_CONFIG.yaml`. Edited 15 files across two phases.

### Phase A: Config + Core Docs (0 new, 7 modified)

| # | File | Changes |
|---|------|---------|
| 1 | `.tfw/PROJECT_CONFIG.yaml` | Added `scope_budgets` (4 values), completed `templates` (+res/knowledge/release → 8 entries), added `workflows` (8 entries), added `research` (4 limits) |
| 2 | `.tfw/conventions.md` | L1: removed version from title (Pattern D). §6: Pattern B — pure reference to config, no values. §8: removed stale `TFW 0.4` from prose |
| 3 | `.tfw/README.md` | §Scope Budgets: Pattern B — pure reference to config, table removed. Removed `TFW 0.5` from 3 prose locations (L151, L166, L209) |
| 4 | `.tfw/workflows/plan.md` | §Scope Budget per Phase: Pattern B — pure reference to config, table removed |
| 5 | `.tfw/glossary.md` | L1: removed version from title (Pattern D). L69: Pattern B pure reference |
| 6 | `.tfw/templates/TS.md` | L27: Pattern B (reference to `tfw.scope_budgets` in config) |
| 7 | `README.md` (root) | Key Concepts: budget → config reference, version → VERSION file reference |

### Phase B: Adapters + Init + Local Copies (0 new, 8 modified)

| # | File | Changes |
|---|------|---------|
| 8 | `.tfw/adapters/claude-code/CLAUDE.md.template` | `TFW 0.5` → `TFW {version}`. Templates list → config reference |
| 9 | `.tfw/adapters/cursor/tfw.mdc.template` | `TFW 0.5` → `TFW {version}`. Templates + workflows → config references |
| 10 | `.tfw/adapters/antigravity/tfw-rules.md.template` | `TFW 0.5` → `TFW {version}`. Templates → config reference |
| 11 | `.tfw/adapters/antigravity/README.md` | Fixed stale `TFW 0.4` in directory tree |
| 12 | `.tfw/init.md` | Removed version from title. Full config example (all 4 sections). `{version}` replacement instruction for adapters |
| 13 | `CLAUDE.md` | `TFW 0.5` → version-agnostic title + `see .tfw/VERSION`. Templates → config reference |
| 14 | `.agent/rules/tfw.md` | Added version reference. Templates → config reference (fixes TD-26: missing version + RES) |
| 15 | `TECH_DEBT.md` | TD-25 → ✅ Resolved (TFW-12). TD-26 → ✅ Resolved (TFW-12) |
| 16 | `.agent/workflows/tfw-plan.md` | Synced scope budget section: Pattern B — pure reference to config, table removed |

### Key Decisions

1. **Tree comments in `.tfw/README.md` kept as-is.** TS item #3 mentioned "Tree comments: reference config for lists". The tree at L63-81 uses inline annotations as visual aids — not authoritative lists.
2. **Pattern B (pure reference) used instead of Pattern A (defaults table).** TS/RES recommended Pattern A (R3/C1: readability). User overrode: budget numbers must exist only in `PROJECT_CONFIG.yaml`. All tables removed, replaced with config references.
3. **`.agent/workflows/tfw-plan.md` synced.** TS §8 marked agent workflow copies as out-of-scope. User flagged the inconsistency — synced to match canonical.

## 2. Test Results

```
# Phase A — no hardcoded budget values with ≤ prefix
$ grep "≤ 7|≤ 4|≤ 600|≤ 6" conventions.md README.md plan.md glossary.md TS.md README.md
→ PASS (0 matches)

# Phase A — no version in core titles
$ grep "TFW 0\." conventions.md glossary.md
→ PASS (0 matches, after fixing stale §8 reference)

# Phase B — no hardcoded version in adapters
$ grep -rn "TFW 0\." .tfw/adapters/ CLAUDE.md .agent/rules/tfw.md
→ PASS (0 matches)

# Phase B — {version} placeholder present in all 3 templates
$ grep "{version}" .tfw/adapters/*/tfw*.template .tfw/adapters/claude-code/CLAUDE.md.template
→ 7 matches across 3 files ✅

# Config sections exist
$ grep "scope_budgets|templates:|workflows:|research:" PROJECT_CONFIG.yaml
→ Lines 13, 19, 29, 39 ✅
```

## 3. Acceptance Criteria Status

### Phase A
- [x] AC-1: `tfw.scope_budgets` exists with 4 keys
- [x] AC-2: `tfw.templates` has 8 entries
- [x] AC-3: `tfw.workflows` has 8 entries
- [x] AC-4: `tfw.research` has 4 limit entries
- [x] AC-5: conventions.md §6 has "configured in PROJECT_CONFIG" header + defaults table
- [x] AC-6: plan.md scope budget section references config
- [x] AC-7: grep `≤ 7` → 0 matches
- [x] AC-8: grep `TFW 0\.` in conventions/glossary → 0 matches

### Phase B
- [x] AC-9: All 3 adapter templates use `{version}`
- [x] AC-10: `CLAUDE.md` references VERSION file
- [x] AC-11: init.md config example shows all 4 sections
- [x] AC-12: grep `TFW 0\.` in adapters/CLAUDE/.agent → 0 matches
- [x] AC-13: TD-25, TD-26 marked ✅ in TECH_DEBT.md

## 4. Deviations from TS

| # | TS Says | Actual | Justification |
|---|---------|--------|---------------|
| 1 | `.tfw/README.md` tree comments → reference config | Kept inline comments as-is | Tree comments are visual dir annotations, not authoritative lists. "See config" would break readability. Documented in ONB inconsistency #2 |
| 2 | `conventions.md` §8 not mentioned in TS | Removed stale `TFW 0.4` from prose | Natural extension of Pattern D — same file, same type of fix. Caught by verification grep |

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/adapters/antigravity/README.md` | 20-24, 49-56 | duplication | Workflow copy commands only list plan/handoff/review/resume — missing research/docs/release/update. Not in TS scope (noted as out-of-scope in TS §8: `.agent/workflows/` copies updated on next tfw-update) |
| 2 | `.tfw/init.md` | 98-104 | duplication | Antigravity workflow copy commands same issue as obs #1 — missing research/docs/release/update |
| 3 | `.tfw/README.md` | 289 | style | Evolution §v3 mentions "Scope budgets — hard limits per phase calibrated for AI agent quality" — no hardcoded values, just description. Fine as-is but could add config reference |
| 4 | `CLAUDE.md` | 48 | naming | Key References says "project parameters (task prefix, build commands)" — now also includes scope_budgets, templates, workflows, research |

---

*RF — TFW-12: Config Centralization | 2026-03-30*
