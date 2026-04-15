# RF — TFW-40 / Phase B: Naming Normalization

> **Date**: 2026-04-15
> **Author**: Executor
> **Status**: 🟢 RF — Ready for review
> **TS**: [TS Phase B](TS__PhaseB__naming_normalization.md)

## 1. Summary of Work Done

Renamed `PROJECT_CONFIG.yaml` → `project_config.yaml` and `TOPIC_FILE.md` → `topic_file.md` across the entire framework. Updated all references in workflows, templates, adapters, conventions, glossary, compilable contract, root files, and the documentation pipeline. Added §10.4 (YAML File Naming Convention) to conventions.md. Version bumped to 0.8.4 with migration notes.

## 2. Files Modified

| File | What changed |
|------|--------------|
| `.tfw/PROJECT_CONFIG.yaml` | **RENAMED** → `.tfw/project_config.yaml` via `git mv`. Version bumped to 0.8.4 |
| `.tfw/templates/TOPIC_FILE.md` | **RENAMED** → `.tfw/templates/topic_file.md` via `git mv` |
| `.tfw/VERSION` | 0.8.3 → 0.8.4 |
| `.tfw/templates/project_config.yaml` | Version 0.8.3 → 0.8.4 |
| `.tfw/CHANGELOG.md` | Added v0.8.4 entry with Added/Changed/Migration Notes |
| `.tfw/conventions.md` | §10.3 updated (PROJECT_CONFIG → project_config), **§10.4 added** (YAML naming convention), §2/§4/§6/§10.2/§11/§15 refs updated |
| `.tfw/glossary.md` | 8 refs updated (Status, Iteration, min_iterations, Scope Budget, Topic File, Knowledge Gate, Config Sync Registry, PROJECT_CONFIG.yaml heading) |
| `.tfw/compilable_contract.md` | L74 ref updated |
| `.tfw/knowledge_state.yaml` | Comment ref updated |
| `.tfw/templates/knowledge_state.yaml` | Comment ref updated |
| `.tfw/templates/ONB.md` | 2 refs updated (Phase A work) |
| `.tfw/templates/REVIEW.md` | 1 ref updated |
| `.tfw/templates/review/verify.md` | 1 ref updated |
| `.tfw/workflows/init.md` | 5 refs updated |
| `.tfw/workflows/update.md` | 5 refs updated |
| `.tfw/workflows/plan.md` | 4 refs updated |
| `.tfw/workflows/review.md` | 2 refs updated |
| `.tfw/workflows/release.md` | 2 refs updated |
| `.tfw/workflows/knowledge.md` | 3 refs updated (incl. TOPIC_FILE → topic_file) |
| `.tfw/workflows/config.md` | 8 refs updated |
| `.tfw/workflows/research/base.md` | 2 refs updated |
| `.tfw/adapters/antigravity/tfw-rules.md.template` | 2 refs updated |
| `.tfw/adapters/cursor/tfw.mdc.template` | 3 refs updated |
| `.tfw/adapters/claude-code/CLAUDE.md.template` | 2 refs updated |
| `.tfw/adapters/README.md` | 2 refs updated |
| `.agent/rules/tfw.md` | 2 refs updated (live adapter) |
| `.agent/workflows/tfw-*.md` | 8 files re-synced from canonical `.tfw/workflows/` |
| `README.md` | 2 path refs updated (L159, L193) |
| `KNOWLEDGE.md` | §1 Architecture Map Config row updated |
| `docs/scripts/gen_docs.py` | 3 refs updated (L165 docstring, L166 path, L530 conditional) |
| `docs/scripts/test_gen_docs.py` | 1 ref updated (L242 fixture) |

**Total: 28 source files + 8 adapter copies = 36 files touched**

## 3. DoD Status

| # | Acceptance Criterion | Status | Evidence |
|---|---------------------|--------|----------|
| 1 | `grep -r "PROJECT_CONFIG" .tfw/` returns 0 live-reference results | ✅ | Verified — only §10.4 example string "not `PROJECT_CONFIG.yaml`" remains (showing old name, correct) |
| 2 | `grep -r "TOPIC_FILE" .tfw/` returns 0 results | ✅ | Verified — 0 results |
| 3 | `.tfw/project_config.yaml` exists, `.tfw/PROJECT_CONFIG.yaml` does not | ✅ | `git mv` executed |
| 4 | `.tfw/templates/topic_file.md` exists, `.tfw/templates/TOPIC_FILE.md` does not | ✅ | `git mv` executed |
| 5 | §10.4 naming convention added to conventions.md | ✅ | Lines 329-339 |
| 6 | Version = 0.8.4 in VERSION, project_config.yaml, templates/project_config.yaml | ✅ | All three updated |
| 7 | CHANGELOG has v0.8.4 entry with Migration Notes | ✅ | Lines 8-26 |
| 8 | 55/55 gen_docs tests pass | ✅ | `python -m pytest test_gen_docs.py -v` — all pass |
| 9 | Adapter workflows synced | ✅ | 8 files copied, `grep PROJECT_CONFIG .agent/` = 0 results |
| 10 | README.md and KNOWLEDGE.md refs updated | ✅ | No more 404 links |
| 11 | Historical task artifacts NOT modified | ✅ | tasks/ grep shows only historical refs and ONB/TS/HL for TFW-40 |

## 4. Key Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | Used `git mv` instead of `Rename-Item` | Preserves git rename tracking for better `git log --follow` |
| 2 | Extended scope beyond TS to include README.md, KNOWLEDGE.md, gen_docs.py | User answer to ONB Q1: "Обновить всё. Битые ссылки = баг, а не tech debt" |
| 3 | Left CHANGELOG historical entries as-is | They describe what happened at that version — changing them would falsify history |
| 4 | Left TECH_DEBT.md TD-102 text as-is | Historical observation text, per user: "Исторические тексты — не трогать" |
| 5 | Left tasks/ artifact refs as-is | Completed task artifacts are historical records |

## 5. Observations

| # | File | Line | Category | Observation |
|---|------|------|----------|-------------|
| 1 | `.tfw/conventions.md` | 331 | style | §10.4 lists `knowledge_state.yaml` as an example of the naming convention, but this was already lowercase before Phase B. Only `PROJECT_CONFIG.yaml` and `TOPIC_FILE.md` were actually renamed. The convention still holds — it's a documenting-existing-practice + enforcing-new-practice |
| 2 | `KNOWLEDGE.md` | 47-53 | content | D16/D20/D22/D24 Architecture Decisions reference `PROJECT_CONFIG.yaml` by old name. These are historical records of decisions made before the rename. Changing them would require updating the Source column references too, which is risky. Best left as historical |
| 3 | `.tfw/project_config.yaml` | 7 | format | The live config file has different comment formatting than the template (shorter comment). This pre-existed Phase B — not introduced by this change |

> fact-candidates: none (mechanical rename, no strategic insights)
