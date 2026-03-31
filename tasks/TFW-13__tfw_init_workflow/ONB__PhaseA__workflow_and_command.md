# ONB — TFW-13 / Phase A: Init Workflow + Slash Command

> **Дата**: 2026-03-30
> **Автор**: Executor (AI)
> **Статус**: 🟠 ONB — Ожидает ответов
> **Parent HL**: [HL-TFW-13](HL-TFW-13__tfw_init_workflow.md)
> **TS**: [TS Phase A](TS__PhaseA__workflow_and_command.md)

---

## 1. Understanding (как понял задачу)

Создать `tfw-init` — AI-first workflow для инициализации TFW в любом проекте. Phase A включает: (1) workflow `.tfw/workflows/init.md` с 5 фазами (Discover, Interview+Mini-Setup, Knowledge, Full Setup, Verify), role lock Coordinator, tutorial mode; (2) slash-команды для Claude Code и Antigravity; (3) обновление CLAUDE.md и шаблона; (4) замена старого init.md указателем. 3 новых файла, 3 модификации.

## 2. Entry Points (откуда начинать)

| Файл | Роль |
|------|------|
| `.tfw/workflows/init.md` | CREATE — основной workflow (Step 1) |
| `.claude/commands/tfw-init.md` | CREATE — thin wrapper slash command (Step 2) |
| `.agent/workflows/tfw-init.md` | CREATE — Antigravity copy (Step 3) |
| `CLAUDE.md` | MODIFY — добавить строку в таблицу (Step 4) |
| `.tfw/adapters/claude-code/CLAUDE.md.template` | MODIFY — добавить строку в шаблон (Step 5) |
| `.tfw/init.md` | MODIFY — заменить содержимое указателем (Step 6) |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | **Antigravity pattern:** TS Step 3 говорит: `.agent/workflows/tfw-init.md` = копия `.claude/commands/tfw-init.md` + YAML frontmatter. Но ВСЕ существующие `.agent/workflows/` файлы — это полные копии `.tfw/workflows/` файлов (с тем же YAML frontmatter). Например, `.agent/workflows/tfw-handoff.md` = 5444 байт (полный workflow), а `.claude/commands/tfw-handoff.md` = 1436 байт (thin wrapper). Какой паттерн использовать? **Рекомендую:** следовать существующему паттерну — `.agent/workflows/tfw-init.md` = копия `.tfw/workflows/init.md`. | **Согласен.** Следовать существующему паттерну: `.agent/workflows/tfw-init.md` = полная копия `.tfw/workflows/init.md`. TS Step 3 ошибочен — executor прав. |

## 4. Recommendations (suggestions, not blocking)

1. Содержимое workflow из TS Step 1 — ~182 строки (с frontmatter). Это близко к лимиту 200 строк из DoF. При реализации буду следить за длиной, но проблем не ожидаю — текущий контент укладывается.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Naming overlap: `.tfw/init.md` (pointer) и `.tfw/workflows/init.md` (workflow) — оба файла будут существовать. TS это осознаёт (Risk §6), но пользователи могут путать. Pointer в init.md явно ссылается на workflow, так что риск минимален.

## 6. Inconsistencies with Code (spec vs reality)

1. **Antigravity pattern** (описано в Q1 выше) — TS говорит "копия Claude Code команды", реальность — "копия полного workflow".

---

*ONB — TFW-13 / Phase A: Init Workflow + Slash Command | 2026-03-30*
