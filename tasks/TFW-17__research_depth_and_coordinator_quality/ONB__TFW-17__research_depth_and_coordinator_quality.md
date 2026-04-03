# ONB — TFW-17: Research Depth & Coordinator Quality

> **Дата**: 2026-04-03
> **Автор**: Executor (AI)
> **Статус**: 🟠 ONB — Ожидает ответов
> **Parent HL**: [HL-TFW-17](HL-TFW-17__research_depth_and_coordinator_quality.md)
> **TS**: [TS TFW-17](TS__TFW-17__research_depth_and_coordinator_quality.md)

---

## 1. Understanding (как понял задачу)

Задача двусторонняя: (1) добавить Coordinator Mindset секцию и усилить формулировки в `plan.md`, чтобы координатор ценил качество планирования выше скорости; (2) усилить `research.md` Hard Rule #8 (обязательное использование внешних инструментов), stage-level mindset reminders, depth self-check в checkpoint, и расширить Gather stage. После завершения каноничных файлов — полная копия в 4 адаптера, что автоматически фиксит известные desyncs (статусы, нумерация фаз).

## 2. Entry Points (откуда начинать)

| Файл | Текущие строки | Действие |
|------|------|----------|
| `.tfw/workflows/plan.md` | L10-14 (Role Lock), L28-31 (Phase 1), L70-76 (RESEARCH Gate) | Вставка Mindset, усиление Phase 1 и Gate |
| `.tfw/workflows/research.md` | L77-81 (Gather), L108-133 (Checkpoint), L149-155 (Sufficiency Check), L228-236 (Hard Rules) | Hard Rule #8, reminders, depth check |
| `.agent/workflows/tfw-plan.md` | 163 lines, desynced | Full overwrite |
| `.agent/workflows/tfw-research.md` | 299 lines, partially desynced (statuses) | Full overwrite |
| `.claude/commands/tfw-plan.md` | 163 lines, desynced (identical to .agent) | Full overwrite |
| `.claude/commands/tfw-research.md` | 299 lines, partially desynced | Full overwrite |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | Нет блокирующих вопросов | — |

## 4. Recommendations (suggestions, not blocking)

1. **TS Step 8 specifies "copy"** — both adapter plan files и adapter research files идентичны между собой (Antigravity = Claude Code). Это подтверждено чтением. Копирование каноничного файла решает desync для обоих одновременно.
2. **Line budget**: TS говорит ~15 net new lines для research.md (currently 299). Мой подсчёт добавок: Hard Rule #8 (1 line), 3 stage reminders (6 lines — blockquote + пустые строки), checkpoint depth check (1 line), Sufficiency Check bullet (1 line), Gather expansion (1 line replaced + 1 added) ≈ ~12 net new lines. Укладывается в бюджет.
3. **plan.md Coordinator Mindset**: TS даёт дословный текст (~6 строк). Вставлю точно по TS — после Role Lock, перед Prerequisites.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Phase 1 edit granularity**: TS Step 2 говорит "replace" строку 2 Phase 1. Но фактически меняется только одна подстрока: `Understand the problem` → `Understand the problem deeply` + добавляется предложение. Минимально инвазивное изменение, без риска.
2. **research.md Stage reminders positioning**: TS не указывает точную позицию reminders внутри stage descriptions. Я вставлю их как blockquote сразу после заголовка каждого стейджа (перед bullet list), чтобы агент видел reminder до чтения шагов.

## 6. Inconsistencies with Code (spec vs reality)

1. **HL §2 "Adapter desync" L60/L68/L143** — подтверждено для обоих адаптеров (Antigravity + Claude Code). Оба файла идентичны друг другу и содержат: `🔵 HL` (L60), `Phase 3.5` (L68), `🔵 HL`/`🟡 TS` в pipeline (L143).
2. **HL §2 "Adapter desync tfw-research.md ✅"** — не полностью. Adapter research files используют `🔵 HL`/`🟡 TS` в Status Transitions (L278), тогда как canonical использует `📝 HL_DRAFT`/`🟡 TS_DRAFT`. Desync присутствует, но фиксится автоматически при копировании (Step 8).

---

*ONB — TFW-17: Research Depth & Coordinator Quality | 2026-04-03*
