# Briefing — "What should we investigate?" (Iteration 2)
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260922-123250_CMTR](../../HL-TFW_20260922-123250_CMTR.md)
> Goal: enable the coordinator to recommend or autonomously select platform-native models and thinking effort per launch to preserve quality without burning tokens or quotas
> Producer unit: `antigravity:thread:local:24003cc7-799f-4352-9c51-bc150687d097`
> Parent Coordinator: `antigravity:thread:local:3d06f6f4-0f5b-415d-aff2-f70c8f1acdcc`
> Activation / dispatch source: owner-direct: saubakirov via `/tfw-research cmtr iter 2`
> Coordination authority: `HL-TFW_20260922-123250_CMTR.md @ e688188c5124a0ce123feb647e69bde211a78374`
> Originating proposer: `none`

## Predecessor Context (from Iteration 1)

Итерация 1 зафиксировала базовые решения [research/iter1/RES.md](../iter1/RES.md):
- **D1:** 3 уровня сложности (Procedural, Standard, Critical).
- **D2:** Дуальный запуск сессий (UI-подсказка человеку по умолчанию + автономный API-запуск для платформ с task creation).
- **D3:** Интеграция в существующий контракт координации без отдельных файлов `models.yaml`.
- **D4:** Ненавязчивая самокалибровка координатора (Up-Shift / Down-Shift).
- **D5:** Двухуровневая нотация рекомендации (класс мощности + примеры моделей).

Открытые нити и фокус итерации 2: состязательное тестирование правила 3 уровней на 3 контрастных сценариях TFW и выверка точных минимальных диффов расширения ядра фреймворка.

## Research Plan

### Gather
- Отобрать и детально рассмотреть 3 контрастных исторических сценария TFW:
  1. *Процедурный сценарий:* TFW-55 Phase B.2 (локализация README, механическое обновление таблиц, перенос проверенных текстов).
  2. *Стандартный инженерный сценарий:* TFW-26 Phase A/B (разработка генератора документации `gen_docs.py` по четко специфицированному TS с AC).
  3. *Критический состязательный сценарий:* TFW_20260921-180000_RVAG (состязательное ревью, разоблачение ложных возвратов, защита ценностей проекта).
- Исследовать точные места размещения изменений в `.tfw/workflows/plan.md`, `.tfw/conventions.md §7`, `.tfw/templates/HL.md`, `.tfw/templates/TS.md`.
- Зафиксировать платформенное ограничение межсессионных сообщений в Antigravity (доставка в очередь `undelivered` до следующей инвокации) для корректного отражения в конвенциях.

### Extract
- Смоделировать отработку правила 3 уровней на каждом из 3 контрастных сценариев (расчет экономии квот, времени отклика и оценка защиты от потери качества).
- Разработать буквальные тексты расширений для ядра:
  - Формулировка для `plan.md` (Шаг 5: Coordination Selection Gate).
  - Формулировка для `conventions.md §7` (Coordination).
  - Поля для шаблона `HL.md` (§4.1 Coordination Selection).
  - Поле в шапке шаблона `TS.md`.

### Challenge
- Подвергнуть предлагаемые формулировки атаке на избыточность (принцип Сент-Экзюпери, F43, F45): удаление любого слова, не несущего смысловой нагрузки.
- Проверить, не вызывают ли новые поля конфликтов с правилом Role Lock (не начинает ли исполнитель или ревьювер пересматривать назначенную модель).
- Проверить сохранение детерминизма тестов репозитория (`pytest`).

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status (post-iter1) |
|---|-----------|-----------|-------------------------|
| H1 | Разделение задач всего на 3 класса (Procedural, Standard, Critical/Adversarial) покрывает 95% потребностей без необходимости сложного математического скоринга. | open | 🟢 confirmed (проверяется контрастными сценариями) |
| H2 | При наличии четкого поля в шаблоне `TS.md` координатор естественно формулирует точную рекомендацию по модели без раздувания инструкций. | open | 🟡 testing (формируются точные формулировки поля) |
| H3 | Координатор способен надежно диагностировать собственную слабость (нехватку контекста/thinking) по признакам ветвления дерева решений и предупреждать человека. | open | 🟢 confirmed |

## Scope Intent
- **In scope:** Контрастные исторические сценарии TFW; точные тексты расширений `plan.md`, `conventions.md §7`, `HL.md`, `TS.md`; отражение механизма доставки очередей в Antigravity; финализация рекомендаций для фазы реализации (Фаза A).
- **Out of scope:** Написание исполнительного кода фазы A (Role Lock: Researcher); изменение утвержденного замороженного контракта HL.

## Guiding Questions
1. Подтверждают ли 3 контрастных сценария TFW надежность и экономическую оправданность правила 3 уровней?
2. Являются ли подготовленные формулировки расширений минимально достаточными по принципу Сент-Экзюпери?
3. Достаточно ли данных для завершения исследовательского цикла задачи CMTR и перехода к TS (Фаза A)?

---
Stage complete: YES
