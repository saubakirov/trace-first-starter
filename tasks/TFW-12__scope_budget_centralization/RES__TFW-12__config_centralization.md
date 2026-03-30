# RES — TFW-12: Config Centralization (Scope Budgets + Version String)

> **Date**: 2026-03-30
> **Author**: Coordinator (AI)
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-12](HL-TFW-12__scope_budget_centralization.md)
> **Mode**: Pipeline

---

## Research Context

TFW-12 proposes centralizing duplicated parameters to avoid updating the same values in 10+ files on every change. RESEARCH found 6 categories of duplication, confirmed 4 for centralization, designed the YAML structure, and challenged the approach for edge cases.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| R1 | All 4 categories (budgets, version, templates, workflows) go to YAML | User confirmed — single source of truth |
| R2 | Status pipeline and research limits stay as-is | Too visual / too local to centralize |
| R3 | `conventions.md` §6 is the canonical description of scope budgets — keeps rationale, references config for values | Readability > pure DRY. "See config" alone loses context |
| R4 | Version removed from core file titles, `{version}` in adapter templates | Titles drift on every bump. Adapter templates resolve on init/update |
| R5 | `tfw-update` adapter refresh (Step 7) already handles version propagation | No new mechanism needed — just use `{version}` placeholder |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Template/workflow lists — YAML or directory scan? | ✅ | YAML (user) |
| Q2 | Scope budgets in docs — pointer only or values + pointer? | ✅ | Values + pointer (R3: readability) |

---

## Stage: Gather — "What do we NOT know?" ✅

### Full Inventory: Duplicated Parameters

| # | Parameter Category | Copies | Drifted? | Action |
|---|-------------------|--------|----------|--------|
| 1 | Scope budgets (≤7, ≤4, ≤600, ≤6) | 6 | No | → YAML |
| 2 | Version strings (`TFW 0.X`) | ~17 | YES (TD-25) | → Remove from titles |
| 3 | Template lists (`HL, TS, RES, RF...`) | 6+ | YES | → YAML list |
| 4 | Workflow lists (`plan, research, handoff...`) | 5 | YES | → YAML list |
| 5 | Status pipeline | 8 | No | Leave |
| 6 | Research limits | 2 | No | Leave |

→ User decision: **Closed.** All 4 categories, YAML approach.

---

## Stage: Extract — "What do we NOT see?" ✅

**E1**: PROJECT_CONFIG templates section already incomplete (missing RES, KNOWLEDGE, RELEASE)
**E2**: research.md references non-existent `research:` config section
**E3**: Two consumption patterns: path lookup (agents) + rendered list (docs)
**E4**: Full YAML structure designed with 4 sections
**E5**: Docs pattern: show defaults + reference config
**E6**: Version removed from core titles, placeholder in adapters

→ User decision: **Closed.**

---

## Stage: Challenge — "What do we NOT expect?"

### Challenge C1: "VALUES + POINTER" is better than "POINTER ONLY"

The HL proposed replacing `≤ 7` with "see PROJECT_CONFIG.yaml". But conventions.md §6 currently has a beautiful table with rationale:

```markdown
| Files per phase | ≤ 7 | Agent maintains full mental model |
```

Replacing `≤ 7` with `see config` destroys readability. Better approach:

```markdown
> Scope budgets are configured in `.tfw/PROJECT_CONFIG.yaml` (`tfw.scope_budgets`).
> Values below are defaults. Override in PROJECT_CONFIG for your project.

| Parameter | Default | Rationale |
|-----------|---------|-----------|
| Files per phase | 7 | Agent maintains full mental model |
```

This keeps the table readable, makes clear that config is the source, and the word "Default" signals customizability.

**Key insight**: conventions.md is the **canonical definition** (semantics + rationale). PROJECT_CONFIG.yaml is the **operational override** (numbers only). They serve different purposes.

### Challenge C2: What about `tfw-update` and adapter refresh?

I initially flagged (G5) that adapter copies don't refresh on update. But actually, `update.md` Step 7 already has an "Adapter Refresh" section that re-syncs from `.tfw/adapters/`. This means:

1. Template says `# TFW {version}` 
2. `init.md` tells user to replace `{version}` with value from PROJECT_CONFIG
3. `tfw-update` re-copies template → version gets updated

**This already works.** The only missing piece: init.md instructions need to mention `{version}` replacement. This is within scope.

### Challenge C3: TS.md template has hardcoded budgets in RUSSIAN

`TS.md` L27: `**Бюджет:** {N} новых файлов, {M} модификаций. ≤7 файлов, ≤4 новых, ≤600 LOC.`

This is a template — it uses `{N}` placeholders already. The `≤7/≤4/≤600` are just reference values.

Decision: change to `see .tfw/PROJECT_CONFIG.yaml` since this is a template that agents fill in — they'll read actual values from config.

### Challenge C4: glossary.md has inline budget values in prose

`glossary.md` L69: `Subject to scope budgets (≤7 files, ≤600 LOC, ≤4 new files per phase).`

This is prose, not a table. Replace with: `Subject to scope budgets (see .tfw/PROJECT_CONFIG.yaml tfw.scope_budgets).`

### Challenge C5: ALTERNATIVE — should workflows/templates be in a SEPARATE config section?

Current proposal puts everything under `tfw:`. Alternative:

```yaml
tfw:
  version: "0.5.0"
  scope_budgets: {...}
  
artifacts:         # separate section
  templates: {...}
  workflows: {...}
```

Verdict: **keep under `tfw:`** — artifacts ARE part of TFW, not a separate concern. Flatter is simpler.

### Challenge C6: What if a project DOESN'T WANT all 8 workflows?

A small project might use only plan + handoff + resume. If the YAML lists all 8, docs derived from it will show all 8. But this is fine — the list shows what's **available**, not what's required. Same as templates: KNOWLEDGE.md and RELEASE.md are already marked as optional in conventions.md.

### Challenge C7: plan.md scope budget table — duplicate or reference?

`plan.md` L117-120 has exact same table as `conventions.md` §6. 

Options:
- Remove from plan.md, reference conventions.md
- Keep, mark as "defaults from PROJECT_CONFIG"

Decision: **keep** — plan.md is a workflow executed by an agent. Having the table inline is critical for agent performance (avoids extra file read). Mark as "defaults, see PROJECT_CONFIG".

### Checkpoint: Challenge

| Found | Remaining |
|-------|-----------|
| "Values + Pointer" > "Pointer Only" for readability (C1) | — |
| tfw-update adapter refresh already works (C2) | — |
| TS.md template + glossary.md have inline values (C3, C4) | — |
| Flat structure under `tfw:` preferred (C5) | — |
| Full list = available, optional items stay optional (C6) | — |
| plan.md keeps budget table for agent performance (C7) | — |

**Agent assessment:** No show-stoppers found. The approach is sound. Key refinement: conventions.md and plan.md should show values inline ("defaults") + reference config, not just pointers. TS.md template and glossary.md switch to pure references.
**Recommendation:** Close Challenge. Proceed to Final Checkpoint.
→ User decision: ___

---

## Final Checkpoint

| Stage | Status | Key Findings |
|-------|--------|-------------|
| Gather | ✅ | 6 categories identified; 4 go to YAML, 2 stay |
| Extract | ✅ | PROJECT_CONFIG already partially set up (incomplete); designed full YAML structure; two consumption patterns |
| Challenge | ✅ | "Values + pointer" for docs readability; tfw-update already handles adapters; TS.md/glossary use pure references |

### Complexity Check
**Question:** Is the solution proportionate to the problem? What can be removed without losing value?
**Agent assessment:** The scope is proportionate. Each of the 4 categories has proven drift (template list drift in every TFW-5/8/9/11, version drift in TD-25, scope budget drift likely on future adjustments). The YAML additions are ~20 lines. The main work is editing ~12 files to replace hardcoded values with references. Nothing excessive.

If anything could be dropped: research limits (category 6) are already excluded. Status pipeline (category 5) is already excluded. Everything remaining is justified.

→ User decision: ___

**Verdict:** Sufficient for TS / Need another pass

## Conclusion

RESEARCH revealed that the centralization task is broader than initially scoped. Beyond scope budgets and version strings, template and workflow lists are the **#1 source of recurring tech debt** — drifting on every task that adds artifacts or workflows (TFW-5, 8, 9, 11). The key design refinement is "values + pointer" over pure pointers: conventions.md and plan.md keep readable tables with values marked as defaults, while TS.md template and glossary switch to pure config references. The existing `tfw-update` adapter refresh mechanism means version placeholders in templates will propagate automatically. The proposed YAML structure adds ~20 lines to PROJECT_CONFIG.yaml and unifies 4 categories of duplicated parameters into a single source of truth.

Self-critique: I initially focused too narrowly on version strings and missed the broader parameter centralization goal until the user redirected. The Gather stage needed a second pass to be comprehensive.

---

*RES — TFW-12: Config Centralization | 2026-03-30*
