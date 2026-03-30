# TS — TFW-12: Config Centralization

> **Date**: 2026-03-30
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS — waiting for approval
> **Parent HL**: [HL-TFW-12](HL-TFW-12__scope_budget_centralization.md)
> **RES**: [RES-TFW-12](RES__TFW-12__config_centralization.md)

---

## 1. Goal

Centralize 4 categories of duplicated parameters into `PROJECT_CONFIG.yaml` as single source of truth:
- Scope budgets (4 values × 6 files)
- Version strings (~17 places)
- Template list (6+ places, already drifted)
- Workflow list (5 places, already drifted)

## 2. PROJECT_CONFIG.yaml Target State

```yaml
tfw:
  version: "0.5.0"
  upstream: "https://github.com/saubakirov/trace-first-starter"
  task_prefix: TFW
  id_format: "{prefix}-{seq}"
  initial_seq: 12

  scope_budgets:
    max_files_per_phase: 7
    max_new_files: 4
    max_loc: 600
    max_modified_files: 6

  templates:
    hl: .tfw/templates/HL.md
    ts: .tfw/templates/TS.md
    res: .tfw/templates/RES.md
    rf: .tfw/templates/RF.md
    onb: .tfw/templates/ONB.md
    review: .tfw/templates/REVIEW.md
    knowledge: .tfw/templates/KNOWLEDGE.md
    release: .tfw/templates/RELEASE.md

  workflows:
    plan: .tfw/workflows/plan.md
    research: .tfw/workflows/research.md
    handoff: .tfw/workflows/handoff.md
    review: .tfw/workflows/review.md
    resume: .tfw/workflows/resume.md
    docs: .tfw/workflows/docs.md
    release: .tfw/workflows/release.md
    update: .tfw/workflows/update.md

  research:
    max_web_queries_per_stage: 5
    max_files_per_stage: 15
    max_questions_per_stage: 3
    max_passes: 3
```

## 3. Reference Patterns

### Pattern A: "Values + pointer" (conventions.md, plan.md, .tfw/README.md)

Readable table with values marked as defaults, header links to config.

```markdown
> Scope budgets are configured in `.tfw/PROJECT_CONFIG.yaml` (`tfw.scope_budgets`).
> Values below are defaults.

| Parameter | Default | Rationale |
|-----------|---------|-----------|
| Files per phase | 7 | Agent maintains full mental model |
```

### Pattern B: "Pure reference" (TS.md template, glossary.md)

```markdown
Subject to scope budgets (see `tfw.scope_budgets` in `.tfw/PROJECT_CONFIG.yaml`).
```

### Pattern C: "Version placeholder" (adapter templates)

```markdown
# TFW {version}
```

Resolved by `init.md` setup or `tfw-update` adapter refresh.

### Pattern D: "Version removed from titles" (core .tfw/ files)

```markdown
# TFW Conventions       ← was: # TFW 0.4 — Conventions
# TFW Glossary          ← was: # TFW 0.4 Glossary
```

## 4. Scope

### Phase A: Config + Core Docs (0 new, 7 modified)

| # | File | Changes |
|---|------|---------|
| 1 | `.tfw/PROJECT_CONFIG.yaml` | Add `scope_budgets`, complete `templates` (+res/knowledge/release), add `workflows`, add `research` |
| 2 | `.tfw/conventions.md` | §6: Pattern A budgets. L1: remove version from title (Pattern D). Fix workflow table if needed |
| 3 | `.tfw/README.md` | Scope Budgets section: Pattern A. Body: remove `TFW 0.5` from prose. Tree comments: reference config for lists |
| 4 | `.tfw/workflows/plan.md` | §Scope Budget: Pattern A |
| 5 | `.tfw/glossary.md` | L1: remove version (Pattern D). L69: Pattern B for budget values |
| 6 | `.tfw/templates/TS.md` | L27: Pattern B for budget values |
| 7 | `README.md` (root) | Budget reference → "see PROJECT_CONFIG". Version → "see `.tfw/VERSION`" |

**Budget**: 0 new, 7 modified ✅

### Phase B: Adapters + Init + Local Copies (0 new, 8 modified)

| # | File | Changes |
|---|------|---------|
| 8 | `.tfw/adapters/claude-code/CLAUDE.md.template` | `TFW 0.5` → `TFW {version}`. Template/workflow lists → reference config |
| 9 | `.tfw/adapters/cursor/tfw.mdc.template` | `TFW 0.5` → `TFW {version}`. Lists → reference config |
| 10 | `.tfw/adapters/antigravity/tfw-rules.md.template` | `TFW 0.5` → `TFW {version}`. Lists → reference config |
| 11 | `.tfw/adapters/antigravity/README.md` | Fix stale `TFW 0.4` reference |
| 12 | `.tfw/init.md` | Remove version from title. Add `{version}` replacement instruction. Update config example with full structure. Update template/workflow copy commands |
| 13 | `CLAUDE.md` | `TFW 0.5` → value from VERSION. Lists → reference config |
| 14 | `.agent/rules/tfw.md` | Templates +RES. Version reference (TD-26) |
| 15 | `.tfw/workflows/research.md` | Verify L122 `research:` reference is accurate (now config exists) |

**Budget**: 0 new, 8 modified (exceeds ≤6 by 2 — all single-line mechanical edits in adapters, justified)

## 5. Steps

### Phase A

1. Edit `PROJECT_CONFIG.yaml` — add all 4 sections per §2
2. Edit `conventions.md` — remove version from title, Pattern A for budgets §6
3. Edit `.tfw/README.md` — remove version from prose, Pattern A for budget section, update tree comments
4. Edit `plan.md` — Pattern A for scope budget table
5. Edit `glossary.md` — remove version from title, Pattern B for inline budgets
6. Edit `TS.md` template — Pattern B for budget line
7. Edit root `README.md` — reference config for budgets, reference VERSION for version
8. Verify: grep for hardcoded budget values and version strings in Phase A files

### Phase B

1. Edit 3 adapter templates — Pattern C for version, reference config for lists
2. Edit antigravity README — fix stale 0.4
3. Edit `init.md` — full config example, `{version}` instructions, update copy commands
4. Edit `CLAUDE.md` — version from VERSION, lists from config
5. Edit `.agent/rules/tfw.md` — fix TD-26
6. Verify `research.md` L122 reference
7. Verify: grep for remaining hardcoded values across all files
8. Resolve TD-25, TD-26 in TECH_DEBT.md

## 6. Acceptance Criteria

### Phase A
- [ ] AC-1: `tfw.scope_budgets` exists in PROJECT_CONFIG with 4 keys
- [ ] AC-2: `tfw.templates` has 8 entries (hl, ts, res, rf, onb, review, knowledge, release)
- [ ] AC-3: `tfw.workflows` has 8 entries (plan, research, handoff, review, resume, docs, release, update)
- [ ] AC-4: `tfw.research` has 4 limit entries
- [ ] AC-5: conventions.md §6 has "configured in PROJECT_CONFIG" header + defaults table
- [ ] AC-6: plan.md scope budget section references config
- [ ] AC-7: `grep "≤ 7" .tfw/conventions.md .tfw/README.md .tfw/workflows/plan.md` → 0 matches (values without ≤ symbol)
- [ ] AC-8: `grep "TFW 0\." .tfw/conventions.md .tfw/glossary.md` → 0 matches (no version in titles)

### Phase B
- [ ] AC-9: All 3 adapter templates use `{version}` not hardcoded version
- [ ] AC-10: `CLAUDE.md` references VERSION file for version
- [ ] AC-11: init.md config example shows all 4 sections (scope_budgets, templates, workflows, research)
- [ ] AC-12: `grep "TFW 0\." .tfw/adapters/ CLAUDE.md .agent/rules/` → 0 matches
- [ ] AC-13: TD-25, TD-26 marked ✅ in TECH_DEBT.md

## 7. Verification

```bash
# Phase A
grep "scope_budgets" .tfw/PROJECT_CONFIG.yaml
grep -c "templates:" .tfw/PROJECT_CONFIG.yaml  # sections exist
grep -c "workflows:" .tfw/PROJECT_CONFIG.yaml

# No hardcoded budget values with ≤ prefix
grep "≤ 7\|≤ 4\|≤ 600\|≤ 6" .tfw/conventions.md .tfw/README.md .tfw/workflows/plan.md .tfw/glossary.md .tfw/templates/TS.md README.md || echo "PASS"

# No version in core titles
grep "TFW 0\." .tfw/conventions.md .tfw/glossary.md || echo "PASS"

# Phase B
grep "{version}" .tfw/adapters/*/tfw*.template .tfw/adapters/claude-code/CLAUDE.md.template
grep "TFW 0\." .tfw/adapters/ CLAUDE.md .agent/rules/tfw.md 2>/dev/null || echo "PASS"
grep "research:" .tfw/PROJECT_CONFIG.yaml
```

## 8. Out of Scope

- Status pipeline diagrams (8 copies — accepted as documentation)
- Research limits in research.md body (L115, L144 — same file, local)
- `.agent/workflows/` copies of plan.md, research.md, handoff.md — these are synced from canonical, will get updated on next tfw-update
- Historical task artifacts
- KNOWLEDGE.md updates — via `/tfw-docs` after REVIEW

---

*TS — TFW-12: Config Centralization | 2026-03-30*
