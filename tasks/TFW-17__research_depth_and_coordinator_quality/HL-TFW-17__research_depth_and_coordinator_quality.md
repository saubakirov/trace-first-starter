# HL — TFW-17: Research Depth & Coordinator Quality

> **Дата**: 2026-04-03
> **Автор**: Coordinator (AI)
> **Статус**: 📝 HL_DRAFT — Ожидает ревью

---

## 1. Видение

RESEARCH workflow (TFW-11, улучшен в TFW-14) формально содержит правильные инструкции, но агенты системно демонстрируют три паттерна деградации:

1. **Skip-bias** — координатор рекомендует пропустить RESEARCH, хотя по умолчанию он должен рекомендовать его проведение
2. **Internal-only research** — агент изучает только файлы проекта, не использует веб-поиск, не гуглит альтернативные подходы, не изучает как аналогичные задачи решаются в индустрии
3. **Rush-bias** — агент торопится закрыть research, проходит стейджи формально, не мыслит критически, цепляется за изначальный план вместо того чтобы его подвергать сомнению

> **Корневая причина:** проблема не только в research.md. Координатор (plan.md) задаёт «execution mindset» — его цель описана как «HL → TS → handoff» (конвейер), а не как «качественное планирование». Агент воспринимает каждый шаг как задержку на пути к цели, включая RESEARCH.

### Что нужно изменить

Два рычага, работающих в комбинации:

1. **Coordinator mindset в plan.md** — переориентировать с «доведи задачу до TS» на «обеспечь качество планирования»
2. **Research depth в research.md** — усилить требования к использованию инструментов и глубине критического мышления

## 2. Текущее состояние (As-Is)

### Coordinator (plan.md)

| Аспект | Состояние | Проблема |
|--------|-----------|----------|
| Role description | «Architect / Coordinator» | Только заголовок, нет mindset-секции |
| Output description | «Approved HL file(s) + decision on scope» | Фреймит цель как «документ», а не «качество» |
| Phase 1 | «Research & Analysis» → 4 шага → вопросы | Механический чек-лист, нет фокуса на ПОНИМАНИЕ |
| RESEARCH gate | Pros/cons + default=run | Правильно формально, но нет усиления ПОЧЕМУ research важен |
| Handoff tone | «STOP. Start /tfw-handoff» | Корректно по role lock, но подкрепляет «конвейерный» mindset |

### Research (research.md)

| Аспект | Состояние | Проблема |
|--------|-----------|----------|
| Research Mindset | 2 абзаца в начале файла | К моменту стейджей агент «забывает» mindset |
| External tools | L79: «Autonomous search: documentation, changelogs, issues, blog posts» — одна строка | Нет Hard Rule, нет примеров, нет pressure |
| Web search | Упомянут в Limits (max_web_queries_per_stage: 5) | Лимит есть, но нет ОБЯЗАТЕЛЬСТВА использовать хотя бы N запросов |
| Gather stage | «Analyze HL and identify information gaps» | Фокус на HL, а не на внешний мир |
| Critical thinking | Описан в «What good research looks like» | Позитивные примеры, но нет механизма enforcement |
| Stage depth metric | Нет | Агент не знает, когда его исследование поверхностное |

### Adapter desync (tfw-plan.md)

| Строка | Проблема |
|--------|----------|
| L60 | `🔵 HL` вместо `📝 HL_DRAFT` |
| L68 | `Phase 3.5` вместо `Phase 4` |
| L143 | Старый pipeline без HL_DRAFT/TS_DRAFT |

## 3. Целевое состояние (To-Be)

### Coordinator Mindset (plan.md)

| Аспект | Целевое состояние |
|--------|-------------------|
| Role description | «Architect / Coordinator» + **Coordinator Mindset** секция |
| Mindset секция | 4-5 предложений: цель координатора = качество планирования, а не скорость закрытия. Координатор — это тот, кто видит картину целиком, задаёт неудобные вопросы, и защищает процесс от торопливости |
| Phase 1 | Добавить акцент: «understand deeply, не just identify» |
| RESEARCH gate | Усилить default — координатор ДОЛЖЕН объяснить, что именно RESEARCH может раскрыть в этой задаче |

### Research Depth (research.md)

| Аспект | Целевое состояние |
|--------|-------------------|
| External tools | **Hard Rule**: каждый стейдж ДОЛЖЕН включать хотя бы одно внешнее действие (web search, URL read, tool call). Внутренний анализ = необходимо, но недостаточно |
| Gather stage | Расширить: «Analyze HL AND search externally — how is this problem solved elsewhere? What tools/libraries/patterns exist? What are common pitfalls?» |
| Critical thinking | Mindset reminder в начале КАЖДОГО стейджа (1 предложение), не только в шапке файла |
| Depth self-check | В checkpoint добавить: «Did I only read project files, or did I also look outside?» |
| Stage descriptions | Добавить concrete examples of external research per stage |

### Adapter sync

| Файл | Изменение |
|------|-----------|
| `.agent/workflows/tfw-plan.md` | Синхронизация со всеми изменениями canonical plan.md |
| `.agent/workflows/tfw-research.md` | Синхронизация со всеми изменениями canonical research.md |

## 4. Фазы

Одна фаза. 6 файлов (2 canonical + 4 адаптера), целостное изменение.

### Phase A: Mindset + Depth 🔴

1. **`.tfw/workflows/plan.md`** — добавить Coordinator Mindset секцию, усилить Phase 1, усилить RESEARCH gate
2. **`.tfw/workflows/research.md`** — Hard Rule про external tools, stage-level mindset reminders, depth self-check в checkpoints, расширить Gather description
3. **`.agent/workflows/tfw-plan.md`** (Antigravity) — полная синхронизация с canonical plan.md
4. **`.agent/workflows/tfw-research.md`** (Antigravity) — полная синхронизация с canonical research.md
5. **`.claude/commands/tfw-plan.md`** (Claude Code) — полная синхронизация с canonical plan.md
6. **`.claude/commands/tfw-research.md`** (Claude Code) — полная синхронизация с canonical research.md

## 5. Definition of Done (DoD)

- [ ] 1. `plan.md`: Coordinator Mindset секция после Role Lock (4-5 предложений)
- [ ] 2. `plan.md`: Phase 1 усилен акцентом на глубокое понимание
- [ ] 3. `plan.md`: RESEARCH gate усилен — координатор описывает ЧТО research может раскрыть
- [ ] 4. `research.md`: Hard Rule #8: external tool usage per stage mandatory
- [ ] 5. `research.md`: Gather stage description расширен (external research)
- [ ] 6. `research.md`: Depth self-check в checkpoint template
- [ ] 7. `research.md`: Stage-level mindset reminders (1 предложение per stage)
- [ ] 8. `.agent/workflows/tfw-plan.md`: полная синхронизация с canonical
- [ ] 9. `.agent/workflows/tfw-research.md`: полная синхронизация с canonical
- [ ] 10. `.claude/commands/tfw-plan.md`: полная синхронизация с canonical
- [ ] 11. `.claude/commands/tfw-research.md`: полная синхронизация с canonical
- [ ] 12. Adapter desync fixes (statuses, phase numbering)

## 6. Definition of Failure (DoF)

- ❌ 1. Workflow раздувается до 400+ строк (research.md уже 299 — budget ~30 строк на добавления)
- ❌ 2. Новые правила становятся формальностью, которую агент проходит механически (как уже случилось с существующими правилами)
- ❌ 3. Coordinator Mindset = ещё один блок текста, который агент пропускает

**При провале:** Переосмыслить формат — возможно, mindset эффективнее встраивать в конкретные шаги, а не выносить в отдельную секцию.

## 7. Принципы

1. **Quality over velocity** — координатор защищает качество планирования. Его метрика = глубина понимания задачи, а не скорость закрытия pipeline
2. **Outside-in research** — внешнее исследование = не опция, а обязательный компонент. Только внутренний анализ = неполное исследование
3. **Reinforcement > declaration** — правила работают когда они вплетены в конкретные шаги, а не вынесены в отдельную «philosophy» секцию которую агент пролистывает
4. **Compact changes** — добавляем ~30 строк, не 150. Усиливаем существующие элементы, не создаём новые

## 8. Зависимости

| Зависимость | Статус |
|-------------|--------|
| `plan.md` (canonical) актуален | ✅ |
| `research.md` (canonical) актуален | ✅ |
| `.agent/workflows/tfw-plan.md` | ⚠️ Desync (L60, L68, L143) |
| `.agent/workflows/tfw-research.md` | ✅ (sync with canonical) |
| TFW-14 (research interaction model) | ✅ DONE |
| TFW-15 (pipeline status rename) | ✅ DONE |
| Open tech debt: TD-34..TD-37 | Косвенно — TD-34 фиксится в этой задаче |

## 9. Риски

| Риск | Вероятность | Влияние | Mitigation |
|------|-------------|---------|------------|
| Агент читает mindset секцию, но «забывает» к стейджу 2 | Высокая | Среднее | Встраивать reminders в конкретные шаги (принцип #3) |
| External tool requirement добавляет friction для простых задач | Средняя | Низкое | Формулировка «at least one external action per stage» — минимальный threshold |
| Coordinator Mindset конфликтует с Role Lock STOP rule | Низкая | Низкое | Mindset говорит «обеспечь качество», Role Lock говорит «не выходи за роль» — не конфликт, а complementary |
| Adapter desync вернётся после следующего обновления | Средняя | Среднее | Адаптеры = полные копии → любое изменение canonical = sync adapters в той же задаче |

---

*HL — TFW-17: Research Depth & Coordinator Quality | 2026-04-03*
