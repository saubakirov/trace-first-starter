# TS — TFW_20260921-220500_AGSK / Phase A: Adapter Migration and Workspace Cleanup

> **Current filename**: `TS__phase-a__adapter_migration_and_cleanup.md`
> **Date**: 2026-09-22
> **Author**: Antigravity Coordinator
> **Status**: 🟢 TS_APPROVED — Approved by saubakirov 2026-09-22
> **Parent HL**: [HL-TFW_20260921-220500_AGSK](../HL-TFW_20260921-220500_AGSK.md)

---

## 1. Objective

Перевести адаптер среды Google Antigravity с устаревшей модели рабочих процессов (`workflows`) на стандарт навыков (`skills`), полностью удалить устаревшие каталоги `.agent/` и `.agents/workflows/` из репозитория Steps Framework, актуализировать инструментальный манифест и шаблоны правил Antigravity без повреждения тестового набора и смежных адаптеров.

---

## 2. Scope

### In Scope

- Полное удаление файла `.agent/rules/agents.md` и каталога `.agent/`.
- Полное удаление 10 файлов рабочих процессов `.agents/workflows/tfw-*.md` и каталога `.agents/workflows/`.
- Модификация `.tfw/adapters/manifest.yaml`: перенаправление команд Antigravity на целевой каталог навыков `.agents/skills/tfw-{command}/SKILL.md`.
- Модификация шаблона правила `.tfw/adapters/antigravity/tfw-rules.md.template` и рабочего правила проекта `.agents/rules/tfw.md`: устранение ссылок на `.agents/workflows/`, указание вызова нативных навыков `/tfw-*`.
- Модификация `.tfw/adapters/antigravity/README.md`: документирование правил в `.agents/rules/` и навыков в `.agents/skills/`.
- Верификация прохождения полного набора автоматических тестов (`pytest tools/tests/ docs/scripts/ -q`).

### Out of Scope

- Изменение канонических рабочих процессов фреймворка `.tfw/workflows/*.md` (0 изменений).
- Изменение общих шаблонов артефактов `.tfw/templates/*.md` (0 изменений).
- Изменение адаптеров Claude Code, Cursor и Codex (0 изменений).
- Создание руководства миграции для внешних проектов `.tfw/migrations/3.5.0.md` (вынесено в Фазу B).
- Актуализация сводной документации `README.md`, `KNOWLEDGE.md`, `CHANGELOG.md` (вынесено в Фазу B).

---

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Single Source of Truth (Манифест как единственный источник путей) | AC-3, AC-4, AC-5 | Сверка путей установки между `manifest.yaml`, правилами и README адаптера. |
| P2 | Нулевой технический долг (Полная ликвидация устаревших каталогов) | AC-1, AC-2 | Проверка отсутствия каталогов `.agent/` и `.agents/workflows/` в файловой системе. |
| P3 | Безопасность внешних потребителей (Изоляция изменений) | AC-3, AC-6 | Канонические процессы и тесты репозитория остаются зелёными. |
| P4 | Отсутствие сикофанства и плейсхолдеров | AC-4, AC-5 | Все тексты правил и документации полностью готовы к продуктовому использованию. |

---

## 4. Affected Files and Value-Bearing Accounting

Все 15 путей классифицированы как `VALUE` (целевые изменения адаптера и очистка дерева проекта).

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.agent/rules/agents.md` | DELETE | `VALUE` | Удаление устаревшего правила вендора в единственном числе. |
| `.agents/workflows/tfw-plan.md` | DELETE | `VALUE` | Вывод из эксплуатации устаревшего рабочего процесса Antigravity. |
| `.agents/workflows/tfw-research.md` | DELETE | `VALUE` | Вывод из эксплуатации устаревшего рабочего процесса Antigravity. |
| `.agents/workflows/tfw-handoff.md` | DELETE | `VALUE` | Вывод из эксплуатации устаревшего рабочего процесса Antigravity. |
| `.agents/workflows/tfw-review.md` | DELETE | `VALUE` | Вывод из эксплуатации устаревшего рабочего процесса Antigravity. |
| `.agents/workflows/tfw-docs.md` | DELETE | `VALUE` | Вывод из эксплуатации устаревшего рабочего процесса Antigravity. |
| `.agents/workflows/tfw-knowledge.md` | DELETE | `VALUE` | Вывод из эксплуатации устаревшего рабочего процесса Antigravity. |
| `.agents/workflows/tfw-release.md` | DELETE | `VALUE` | Вывод из эксплуатации устаревшего рабочего процесса Antigravity. |
| `.agents/workflows/tfw-update.md` | DELETE | `VALUE` | Вывод из эксплуатации устаревшего рабочего процесса Antigravity. |
| `.agents/workflows/tfw-config.md` | DELETE | `VALUE` | Вывод из эксплуатации устаревшего рабочего процесса Antigravity. |
| `.agents/workflows/tfw-init.md` | DELETE | `VALUE` | Вывод из эксплуатации устаревшего рабочего процесса Antigravity. |
| `.agents/rules/tfw.md` | MODIFY | `VALUE` | Актуализация установленного правила Antigravity под вызов навыков. |
| `.tfw/adapters/manifest.yaml` | MODIFY | `VALUE` | Перенаправление команд `antigravity` на целевой путь `.agents/skills/tfw-{command}/SKILL.md`. |
| `.tfw/adapters/antigravity/README.md` | MODIFY | `VALUE` | Актуализация описания адаптера под навыки и правила `.agents/`. |
| `.tfw/adapters/antigravity/tfw-rules.md.template` | MODIFY | `VALUE` | Синхронизация исходного шаблона правила с продуктовым файлом. |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | 15 literal paths listed above |
| Baseline / selector source | `e3f19b984fc1ba894a91cc6f832b59f2efc308ad` |
| Candidate rule | Первый коммит Исполнителя, содержащий все 15 путей VALUE при зелёных тестах ASSURANCE |
| Logical VALUE files | 15 (11 удалений, 4 модификации) |
| Touched text LOC | Ожидается чистая убыль строк (~1500 удалено, ~40 добавлено/изменено) |
| Multiplier / authority | Неизменяемый утвержденный знаменатель из 15 файлов; отклонение = BLOCKED |
| Approval epoch / failure | Согласование TS владельцем; изменение перечня файлов без поправки запрещено |

```powershell
$valuePaths = @(
  '.agent/rules/agents.md'
  '.agents/workflows/tfw-plan.md'
  '.agents/workflows/tfw-research.md'
  '.agents/workflows/tfw-handoff.md'
  '.agents/workflows/tfw-review.md'
  '.agents/workflows/tfw-docs.md'
  '.agents/workflows/tfw-knowledge.md'
  '.agents/workflows/tfw-release.md'
  '.agents/workflows/tfw-update.md'
  '.agents/workflows/tfw-config.md'
  '.agents/workflows/tfw-init.md'
  '.agents/rules/tfw.md'
  '.tfw/adapters/manifest.yaml'
  '.tfw/adapters/antigravity/README.md'
  '.tfw/adapters/antigravity/tfw-rules.md.template'
)
```

---

## 5. Acceptance Criteria

### AC-1: Полная ликвидация рудиментарного каталога `.agent/`
- [ ] Файл `.agent/rules/agents.md` удален из репозитория.
- [ ] Каталог `.agent/` полностью отсутствует в файловой системе.

Gate: `Test-Path .agent` возвращает `$false`.
Evidence: Проверка отсутствия путей в git status и файловой системе.

### AC-2: Полная ликвидация каталога `.agents/workflows/`
- [ ] Все 10 файлов `tfw-*.md` в `.agents/workflows/` удалены.
- [ ] Каталог `.agents/workflows/` полностью отсутствует в файловой системе.

Gate: `Test-Path .agents/workflows` возвращает `$false`.
Evidence: Проверка отсутствия каталога через git status.

### AC-3: Актуализация инструментального манифеста `.tfw/adapters/manifest.yaml`
- [ ] В секции `antigravity:` поле `commands.target` указывает на `.agents/skills/tfw-{command}/SKILL.md`.
- [ ] В секции `antigravity:` поле `commands.source` указывает на `.tfw/adapters/codex/skills/tfw-{command}/SKILL.md` со стратегией `copy`.
- [ ] Синтаксис YAML валиден.

Gate: Парсинг `manifest.yaml` через Python/PyYAML без ошибок.
Evidence: Сверка структуры манифеста.

### AC-4: Актуализация шаблона правила и рабочего правила Antigravity
- [ ] В `.tfw/adapters/antigravity/tfw-rules.md.template` и `.agents/rules/tfw.md` удалены любые упоминания `.agents/workflows/`.
- [ ] В тексте правила зафиксировано: «Для вызова команд используйте соответствующий локальный навык из `.agents/skills/` либо следуйте Read Contract канонического процесса».
- [ ] Шаблон и рабочий файл побайтово идентичны.

Gate: `git diff --no-index .tfw/adapters/antigravity/tfw-rules.md.template .agents/rules/tfw.md` возвращает нулевой вывод.
Evidence: Побайтовое равенство шаблона и рабочего правила.

### AC-5: Актуализация документации адаптера Antigravity
- [ ] В `.tfw/adapters/antigravity/README.md` описана схема установки правил в `.agents/rules/tfw.md` и команд в `.agents/skills/tfw-{command}/SKILL.md`.
- [ ] Устранены устаревшие формулировки о совместимости с `.agent/`.

Gate: Проверка отсутствия упоминаний `.agent/` и `workflows/` в `README.md` адаптера.
Evidence: Текстовый анализ обновленного документа.

### AC-6: Сохранность тестов репозитория (ASSURANCE)
- [ ] Запуск автоматических тестов репозитория завершается успешно со статусом 0.
- [ ] Все 14 существующих тестов (`test_git_blob_sizes.py`, `test_gen_docs.py`, `test_integration.py`) проходят без замечаний.

Gate: `python -m pytest tools/tests/ docs/scripts/ -q` завершается с кодом 0 (14 passed).
Evidence: Лог выполнения тестов в отчёте об исполнении.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-a__adapter_migration_and_cleanup.md` | Сводный отчёт о проверке каждого критерия приёмки AC-1 — AC-6. |
| `evidence/clean-tree-check.txt` | Подтверждение отсутствия `.agent` и `.agents/workflows`. |

---

## 6. Technical Guidance

1. **Редактирование `.tfw/adapters/manifest.yaml`:**
   Секция `antigravity` должна быть приведена к виду:
   ```yaml
     antigravity:
       persistent:
         source: .tfw/adapters/antigravity/tfw-rules.md.template
         target: .agents/rules/tfw.md
         strategy: copy
       commands:
         source: .tfw/adapters/codex/skills/tfw-{command}/SKILL.md
         target: .agents/skills/tfw-{command}/SKILL.md
         strategy: copy
   ```
2. **Удаление каталогов:**
   Использовать стандартные файловые инструменты (или команды `git rm`), гарантируя удаление пустых родительских каталогов `.agent` и `.agents/workflows`.
3. **Редактирование правила `.agents/rules/tfw.md`:**
   Вместо строки:
   `For /tfw-*, open .agents/workflows/tfw-<command>.md, then follow the mapped canonical workflow's Read Contract.`
   Использовать формулировку:
   `For /tfw-*, invoke the matching repository-local skill. The canonical workflow's Read Contract selects all further inputs.`

---

## 7. Definition of Failure

- ❌ 1. Сохранение файла `.agent/rules/agents.md` или каталога `.agent/`.
- ❌ 2. Сохранение любого файла в `.agents/workflows/` или самого каталога.
- ❌ 3. Расхождение между шаблоном `.tfw/adapters/antigravity/tfw-rules.md.template` и установленным правилом `.agents/rules/tfw.md`.
- ❌ 4. Ошибка синтаксиса в `.tfw/adapters/manifest.yaml`.
- ❌ 5. Падение любого из 14 тестов репозитория.
- ❌ 6. Модификация файлов вне согласованного знаменателя из 15 путей.

---

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Удаление `.agents/workflows/` может нарушить скрытые относительные пути | Ripgrep-поиск перед коммитом; запуск полного набора тестов `pytest`. |
| Нарушение побайтового соответствия между шаблоном и установленным правилом | Контрольная проверка через `git diff --no-index`. |

---

## 9. Cross-Phase Modifications (multi-phase only)

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/adapters/manifest.yaml` | Phase B (потенциально) | В Фазе B проверяется только при обновлении документации; в Фазе A вносится продуктовое изменение путей. |

---

*TS — TFW_20260921-220500_AGSK / Phase A: Adapter Migration and Workspace Cleanup | 2026-09-22*
