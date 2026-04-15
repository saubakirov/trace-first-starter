# ONB — TFW-40 / Phase A: State Separation & Templates

> **Date**: 2026-04-15
> **Author**: Executor
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-40](HL-TFW-40__state_separation.md)
> **TS**: [TS Phase A](TS__PhaseA__state_separation.md)

---

## 1. Understanding

Phase A fixes the root cause of the knowledge gate contamination bug: `.tfw/knowledge_state.yaml` and `.tfw/PROJECT_CONFIG.yaml` are shipped as-is from upstream, leaking runtime state (seq=38, 66 facts) into downstream projects. Fix: create template files for both, update `init.md` to instantiate state from templates (not copies), update `update.md` to classify state files as ⚫ (never overwrite), and document the 3-category classification in `conventions.md §10.3`.

## 2. Entry Points

| File | Role |
|------|------|
| `.tfw/knowledge_state.yaml` | Current contaminated state file (seq=38) |
| `.tfw/PROJECT_CONFIG.yaml` | Current config (hybrid: project identity + framework defaults) |
| `.tfw/workflows/init.md` | Phase 2 Mini-Setup — must create state from templates |
| `.tfw/workflows/update.md` | Step 3 categorization — needs ⚫ STATE category |
| `.tfw/conventions.md` | §10.2 Knowledge Infrastructure — §10.3 to be added after |
| `.tfw/templates/` | Destination for new template files |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | TS Step 2 says "Remove `stack` section entirely" from the template. Current `PROJECT_CONFIG.yaml` in the repo has no `stack` section — the live file never had one. Should I still add a `# stack:` commented placeholder in the template for projects that might need it, or just omit it? | Omit entirely. Template = minimal. Проекты с stack будут добавлять секцию через init.md interview, а не через placeholder. Не захламляй шаблон. |
| 2 | TS says "Reset upstream `knowledge_state.yaml` to zeros." This repo IS the upstream. Should I reset `.tfw/knowledge_state.yaml` to the clean template values (seq=0, all zeros) as part of this phase, losing TFW project's own consolidation history? Or should we keep the live file at seq=38 and only ensure the _template_ is clean? | Оставить seq=38, stats=реальные. Это живой проект, не только стартер. Template чистый — init.md использует template. Live файл не трогать. |

## 4. Recommendations (suggestions, not blocking)

1. **Template registration in PROJECT_CONFIG.yaml `tfw.templates`**: The two new templates (`knowledge_state.yaml`, `project_config.yaml`) are infrastructure, not artifact templates (HL, TS, RF…). I recommend NOT adding them to the `tfw.templates` map — they're a different category (init/update scaffolding, not workflow artifacts). The §10.3 classification table is the right place to document them.

2. **init.md Phase 4 step 6**: Currently says "Update PROJECT_CONFIG.yaml — finalize all values." After Phase A, this should reference the config template flow from Phase 2. No explicit change needed — Phase 2 already creates from template, Phase 4 just updates. Mentioning for completeness.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Template drift risk is underspecified**: TS §6 mentions "future changes must update both" and suggests adding to `config.md` anti-patterns. But `config.md` is the workflow for _changing config values_, not for changing config _structure_. The anti-pattern might fit better in `update.md` or `init.md` anti-patterns (where template structure changes matter). Not blocking — I'll place it in whichever file makes more sense per TS intent.

2. **Merge rules granularity**: TS Step 4 lists explicit "project sections" and "framework sections" for config merge. If a future TFW version adds a new top-level section to PROJECT_CONFIG, the merge rules won't mention it. No fix needed now — the merge rules are guidelines for the agent, not automated scripts.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS says "Copy `.tfw/templates/project_config.yaml` → `.tfw/PROJECT_CONFIG.yaml`"** — note the casing difference (template = `project_config.yaml`, target = `PROJECT_CONFIG.yaml`). This is intentional per scope: Phase B handles the rename. But the init.md instruction will look odd: "copy `project_config.yaml` template → create `PROJECT_CONFIG.yaml`". This is a transitional inconsistency — Phase B resolves it.

2. **TS Step 3 references "Phase 2" of init.md**, but the current init.md calls it "Phase 2: Interview + Mini-Setup" and has a subsection "### Mini-Setup". The step numbering in init.md is `1. Fill .tfw/PROJECT_CONFIG.yaml` / `2. Create tasks/` etc. TS intent maps to init.md Mini-Setup step 1 — will reproduce accurately.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | K1: KNOWLEDGE.md §1 D22 — knowledge_state.yaml as state tracker | ✅ | Applied — this is the file being templated. Template preserves D22 structure (same fields), just zeroed out | |
| 2 | K2: KNOWLEDGE.md §1 D24 — Pattern A (inline defaults + config key) | ✅ | Applied — project_config.yaml template includes inline values (scope budgets, research limits) + config key comments | |
| 3 | K3: KNOWLEDGE.md §1 D36 — Agent-first onboarding: quickstart.md + init.md separation | ✅ | Applied — init.md changes are scoped to Phase 2 Mini-Setup; quickstart.md reading list unchanged | |
| 4 | K4: conventions.md §10.2 — Knowledge Infrastructure file listing | ✅ | Applied — §10.3 extends §10.2 by adding the classification layer; §10.2 listing preserved | |
| 5 | K5: conventions.md §9 — Tool Adapter Pattern | ✅ | N/A for Phase A — no adapter file changes. Phase B will trigger adapter re-sync | |
| 6 | K6: knowledge/convention.md — Naming conventions | ✅ | N/A for Phase A — naming rule is Phase B scope | |
| 7 | K7: KNOWLEDGE.md §1 D11 — tfw-update with 🟢🟡🔴 categorization | ✅ | Applied — adding ⚫ STATE category extends D11 without breaking existing categorization | |

---

*ONB — TFW-40 / Phase A: State Separation & Templates | 2026-04-15*
