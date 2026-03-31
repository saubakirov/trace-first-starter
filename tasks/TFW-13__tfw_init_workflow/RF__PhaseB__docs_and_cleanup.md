# RF — TFW-13 / Phase B: Adapter Docs + References Cleanup

> **Дата**: 2026-03-30
> **Автор**: Executor (AI)
> **Статус**: 🟢 RF — Выполнено
> **Parent HL**: [HL-TFW-13](HL-TFW-13__tfw_init_workflow.md)
> **TS**: [TS Phase B](TS__PhaseB__docs_and_cleanup.md)

---

## 1. Что сделано

### Новые файлы
| Файл | Описание |
|------|----------|
| `.tfw/adapters/README.md` | Adapter index + "How to Write a New Adapter" (перенесено из старого init.md) |

### Изменённые файлы
| Файл | Изменения |
|------|----------|
| `.tfw/conventions.md` | §2: добавлен `init.md` в Required Artifacts. §8: добавлена строка init.md в Workflows table. §15: добавлена строка init.md в Role Lock table |
| `.tfw/glossary.md` | Добавлен термин `tfw-init (Workflow)` |
| `.tfw/adapters/antigravity/README.md` | Добавлен `tfw-init.md` в секции Copy (step 2), tree example (step 3), Keeping in Sync |
| `.tfw/PROJECT_CONFIG.yaml` | Добавлен `init: .tfw/workflows/init.md` в `tfw.workflows` |
| `KNOWLEDGE.md` | Добавлен D18 (tfw-init as AI-first workflow) + TFW-13 в Key Artifacts |

## 2. Ключевые решения

1. **Adapter docs content:** Использован текст из TS Step 1 (адаптированная версия из старого init.md строк 204-231). `{markdown}`/`{/markdown}` pseudo-tags отрендерены как стандартный fenced code block.
2. **Pre-existing gaps:** Обнаружены пробелы в conventions.md и Antigravity README (см. Observations). Добавлен только init.md per TS scope — исправление остальных пробелов out of scope.

## 3. Acceptance Criteria

- [x] `.tfw/adapters/README.md` exists with adapter table + "How to Write" section
- [x] `conventions.md` §2 lists init.md, §8 has init.md row, §15 has init.md role lock
- [x] `glossary.md` has tfw-init term
- [x] Antigravity README lists tfw-init.md in copy + sync instructions
- [x] `PROJECT_CONFIG.yaml` has `init:` in `tfw.workflows`
- [x] `KNOWLEDGE.md` has D18 + TFW-13 in key artifacts

## 4. Верификация

- Lint (`echo "configure your lint command"`): passed (placeholder)
- Tests (`echo "configure your test command"`): passed (placeholder)
- Verify (`echo "configure your verify command"`): passed (placeholder)

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/conventions.md` | 26-30 | todo | §2 Required Artifacts lists only plan, research, handoff, resume workflows. Missing: review.md, docs.md, release.md, update.md (pre-existing gap, not introduced by this task) |
| 2 | `.tfw/conventions.md` | 141-152 | todo | §8 Workflows table missing research.md (pre-existing gap) |
| 3 | `.tfw/conventions.md` | 210-217 | todo | §15 Role Lock table missing docs.md, release.md, update.md (pre-existing gap) |
| 4 | `.tfw/adapters/antigravity/README.md` | 17-27 | todo | Copy/sync sections list only plan, handoff, review, resume, init. Missing: research, docs, release, update workflows (pre-existing gap, init added per scope) |

> **Types:** `dead-code`, `naming`, `todo`, `duplication`, `perf`, `security`, `style`, `missing-test`, `ux`

---

*RF — TFW-13 / Phase B: Adapter Docs + References Cleanup | 2026-03-30*
