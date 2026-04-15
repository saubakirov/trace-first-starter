# ONB — TFW-40 / Phase B: Naming Normalization

> **Date**: 2026-04-15
> **Author**: Executor
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-40](HL-TFW-40__state_separation.md)
> **TS**: [TS Phase B](TS__PhaseB__naming_normalization.md)

---

## 1. Understanding
Rename `PROJECT_CONFIG.yaml` → `project_config.yaml` and `TOPIC_FILE.md` → `topic_file.md` across all `.tfw/` files. Add a naming convention rule to conventions.md. Update CHANGELOG with migration notes. Version bump to 0.8.4. Mechanical find-replace across ~22 files.

## 2. Entry Points
- `.tfw/PROJECT_CONFIG.yaml` — file to rename
- `.tfw/templates/TOPIC_FILE.md` — file to rename
- `.tfw/conventions.md` — add naming rule, update refs
- `.tfw/glossary.md` — update refs
- `.tfw/workflows/` — update refs in 9 workflow files
- `.tfw/templates/REVIEW.md`, `.tfw/templates/review/verify.md` — update refs
- `.tfw/compilable_contract.md` — update refs
- `.tfw/knowledge_state.yaml`, `.tfw/templates/knowledge_state.yaml` — update comment refs
- `.tfw/CHANGELOG.md`, `.tfw/VERSION` — version bump
- `.tfw/adapters/` — 4 adapter templates + README
- `README.md` — 2 refs (file index table + key concepts table)
- `KNOWLEDGE.md` — refs in §1 Architecture Map

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | TS §3 lists scope as `.tfw/` only, but `README.md` has 2 direct refs (`[.tfw/PROJECT_CONFIG.yaml](.tfw/PROJECT_CONFIG.yaml)` on L159 and `[PROJECT_CONFIG](.tfw/PROJECT_CONFIG.yaml)` on L193) and `KNOWLEDGE.md` has refs in §1. Should I update these root-level files too, or leave them for a separate pass? Leaving them broken would violate HL DoD §9 ("Zero references to PROJECT_CONFIG.yaml in .tfw/" excludes root, but DoD §7 says "All YAML files follow lower_case convention" and the links would 404). | Обновить всё — README.md, KNOWLEDGE.md, и gen_docs.py + test. Битые ссылки = баг, а не tech debt. TS scope расширяю: «19+ files in .tfw/» = "+". DoD §9 расширяю: «grep -r PROJECT_CONFIG .tfw/ README.md KNOWLEDGE.md docs/». По gen_docs.py из §5.1 — тоже включить, docs build не должен ломаться. Исторические тексты (TFW-12 description, TD-102 в TECH_DEBT) — не трогать, это описание прошлого. `git mv` — да, используй вместо Rename-Item. |

## 4. Recommendations (suggestions, not blocking)
1. **Include `README.md` and `KNOWLEDGE.md` in scope** — they have direct path references that will break after rename. TS says "19+ files in `.tfw/`" but grep shows root files too. The "+" accounts for this.
2. **CHANGELOG entry should include Phase A items** — the TS provides a combined v0.8.4 entry covering both phases. Per conventions, this is correct since they ship together. Phase A RF diagram already shows `project_config.yaml` as target path in init.
3. **Config template self-reference** — `.tfw/templates/project_config.yaml` L11 has `version: "0.8.3"` — should bump to `"0.8.4"` per TS Step 5.
4. **Task board description for TFW-12** (L244) says "Centralize config params in PROJECT_CONFIG" — this is historical text in a completed task row. I'd leave it as-is since it describes what the task *was*, not a live reference.

## 5. Risks Found (edge cases, potential issues not in TS)
1. **`docs/scripts/gen_docs.py` has 3 hardcoded refs** (L165 docstring, L166 path construction, L530 conditional check) and `test_gen_docs.py` has 1 (L242 fixture). These are **code files** outside TS §2 scope. The docs build will break after rename unless updated. Recommend including `gen_docs.py` + test in scope or flagging as immediate follow-up.
2. **`.github/workflows/docs.yml`** — verified clean, no refs.
3. **git history** — rename via `Rename-Item` won't preserve git history. Consider `git mv` instead for clean rename tracking.

## 6. Inconsistencies with Code (spec vs reality)
1. **TS §3 lists `.tfw/adapters/README.md`** — it references `PROJECT_CONFIG.yaml` 3 times (L13, L32, L37). Confirmed present.
2. **TS lists `.tfw/templates/project_config.yaml` for MODIFY** — the Phase A RF already created this file. Its L11 has `version: "0.8.3"` which TS Step 5 says to bump. But it also has no self-reference comment to `PROJECT_CONFIG.yaml` — the marker `# ← FRAMEWORK` doesn't reference the filename. So "update self-reference comment if any" → N/A.
3. **TECH_DEBT.md L18** has `PROJECT_CONFIG.yaml` text in TD-102 description — this is historical observation text, not a reference. Leave as-is.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | K1: D22 — knowledge_state.yaml as state tracker | ✅ | Applied — template comment ref updates from `PROJECT_CONFIG.yaml` to `project_config.yaml` | Both live and template files have this comment |
| 2 | K2: D24 — Pattern A (inline defaults + config key) | ✅ | N/A — Phase B is rename-only, no new inline values | |
| 3 | K3: D36 — Agent-first onboarding: quickstart.md + init.md | ✅ | Applied — init.md refs will be updated | |
| 4 | K4: conventions.md §10.2 — Knowledge Infrastructure | ✅ | Applied — `TOPIC_FILE.md` ref in §10.2 → `topic_file.md` | |
| 5 | K5: conventions.md §9 — Tool Adapter Pattern | ✅ | Applied — adapter templates have `PROJECT_CONFIG.yaml` refs to update | |
| 6 | K6: knowledge/convention.md — Naming conventions | ✅ | Applied — the new naming rule in conventions.md codifies this | |
| 7 | K7: D11 — tfw-update 🟢🟡🔴 categorization | ✅ | N/A — Phase A already added ⚫ STATE category | |

---

*ONB — TFW-40 / Phase B: Naming Normalization | 2026-04-15*
