# Gather — Iteration 3: "What do we NOT know?"
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Predecessors: RES1 (D1-D9), RES2 (D10-D14)
> Goal: Варианты нейминга (факты + визуализация), формализация multi-iteration.

## Findings

### G1: Нейминг секций — позиция в информационной иерархии

Внешний ресерч подтверждает чёткую иерархию зрелости информации:

```
Data → Observations → Findings → Signals → Insights
(сырое)  (что видим)   (паттерны)  (ранние   (почему и 
                                   тренды)    что делать)
```

| Уровень | Определение | Вопрос | TFW-аналог |
|---------|-------------|--------|------------|
| Data | Необработанные логи, метрики | «Что записано?» | Код, логи, conversation history |
| Observations | Конкретные факты, замеченные поведения | «Что происходит?» | RF §5 Observations (уже есть) |
| Findings | Паттерны и тренды в агрегированных данных | «Что показывают данные?» | — (не формализовано) |
| Signals | Ранние индикаторы изменений, ещё не паттерн | «Что может начинаться?» | — (RES2 предложил) |
| Insights | Глубокое понимание «почему» + action | «Почему это важно и что делать?» | HL §11 (частично) |

**Ключевое наблюдение:** TFW имеет «Observations» (нижний уровень — агент видит) и «Strategic Session Insights» (верхний уровень — человек знает). Между ними — пробел. «Fact Candidates» пытается закрыть ВСЁ среднее. Отсюда и вагность.

### G2: Naming-as-prompting — название = промпт

Ресерч подтверждает мета-принцип пользователя:
- Section headers = **cognitive frames** для LLM. Конкретное название запускает конкретный режим мышления
- «Описательные метки» (Primary Objective) >>> «общие» (Overview, Details)
- Consistent formatting + описательные headers = stable model behavior
- «Framing effect»: LLM чувствителен к тому КАК информация представлена, даже при идентичной семантике

**Прямое подтверждение D28 (Naming Creates Behavior):** НЕ интуиция, а подтверждённый исследованиями факт. Название секции = micro-prompt.

### G3: Comparison table — секция §6/§7 (что агент наблюдает + что человек знает)

Текущее в TFW: §6 «Fact Candidates» (смесь), HL §11 «Strategic Session Insights».
RES1 предложил: «Doc Candidates + Knowledge Candidates» → отменено RES2.
RES2 предложил: §6 «Fact Candidates» (keep) + §7 «Strategic Signals» (new).

**COMPARISON TABLE — секция ЧЕЛОВЕЧЕСКИХ знаний (§11/§7 equivalents):**

| # | Название | Фрейминг (что оно говорит агенту) | ЗА | ПРОТИВ |
|---|---------|-----------------------------------|-----|--------|
| A | **Strategic Insights** (текущее HL §11) | «Ищи бизнес-контекст, мотивы, стратегию» | Точное. Работает в HL. Люди понимают. «Insight» = индустриальный стандарт для top-level understanding | «Strategic» сужает до бизнес-стратегии. Эмоция юзера, предпочтение процесса — не «стратегические» |
| B | **Strategic Signals** (RES2 D10) | «Ищи всё что должно изменить наши действия» | «Signal» = шире чем insight, ловит ранние индикаторы. Покрывает все 3 сценария из RES2 (бизнес-факт, процесс, эмоция) | «Signal» абстрактно. Без контекста новый агент не поймёт — сигнал ЧЕГО? Требует learning curve |
| C | **Stakeholder Intelligence** | «Ищи высокоценную информацию от стейкхолдеров для принятия решений» | «Intelligence» = формальный, серьёзный, высокий статус. Говорит: это НЕ наблюдения, это стратегическая разведка | Звучит военным/корпоративным. Может отпугнуть не-инженеров. «Intelligence» = intimidating |
| D | **Discoveries** | «Ищи новое — то, чего раньше не знали» | Позитивный, exploratory, forward-looking. Естественный для R&D, research | Слишком неформальный для operations. Не говорит ЧТО искать — только что это должно быть «новое» |
| E | **Key Learnings** | «Запиши главные уроки из разговора» | Индустриальный стандарт (PMI, retrospectives). Все знают | Ретроспективный фокус (что БЫЛО). Не ловит forward-looking сигналы. «Learning» ≠ «то что ещё не стало фактом» |
| F | **Domain Signals** | «Ищи доменные знания от человека — то, чего нет в проекте» | Точно отвечает на Human-Only Test. «Domain» = предметная область, «Signal» = нечто важное | «Domain» может быть непонятно бизнес-юзеру. Менее интуитивно чем «Strategic» |
| G | **Field Notes** | «Записывай всё важное от первоисточника (человека)» | Этнографический термин. Точно описывает ПРОЦЕСС: ты в поле, записываешь от наблюдателя. Cross-domain понятно | НЕ говорит ЗАЧЕМ записывать. Может спровоцировать «dump everything». Новый термин для TFW |

**COMPARISON TABLE — секция АГЕНТСКИХ наблюдений (§6 equivalents):**

| # | Название | Фрейминг | ЗА | ПРОТИВ |
|---|---------|----------|-----|--------|
| a | **Fact Candidates** (текущее) | «Записывай факты-кандидаты для верификации» | Работает 31 таск. Established. Говорит: это НЕ верифицированные факты, это кандидаты | Вагность: «fact» = слишком широко, агент пишет всё подряд. Нет фильтра |
| b | **Project Patterns** | «Замечай повторяющиеся паттерны проекта» | Точный фильтр: только паттерны, не одноразовые факты. Шарпит capture | Теряет одноразовые важные факты (constraint, convention). Паттерн ≠ единичный факт |
| c | **Operational Findings** | «Записывай операционные находки проекта» | «Findings» = паттерны в данных (иерархия G1). «Operational» = про проект, не про domain | «Operational» звучит enterprise/DevOps. Может сбить если проект не software |
| d | **Project Observations** | «Наблюдай за проектом и записывай» | Чёткое. Низкий уровень — правильно. Observations = «что происходит» | Конфликтует с RF §5 «Observations» (уже есть для tech debt). Дубликат имени |
| e | **Fact Candidates** (with tighter instructions) | «Записывай факты-кандидаты…» + усиленный instruction block в шаблоне | Не меняет ничего, только instruction. Backwards compatible. Минимальный риск | Не решает D28 — если название вагное, instructions компенсируют только частично |

### G4: Comparison table — секция визуализации

| # | Название | Фрейминг | ЗА | ПРОТИВ |
|---|---------|----------|-----|--------|
| 1 | **Diagrams** (RES2 D12) | «Нарисуй диаграммы» | Самое простое и универсальное. Все знают. arc42 использует | Code-centric ассоциация. «Diagram» = UML, DB schema. Бизнес-юзер думает «это для разработчиков» |
| 2 | **Visual Models** | «Создай визуальные модели» | Высокий уровень абстракции. «Model» = правила и логика системы | «Model» двусмысленно (ML model? data model?). Тяжеловесно |
| 3 | **Process Maps** | «Нарисуй карту процесса» | Точно для BPM, workflow. Бизнес-юзеры знают «process map» | Сужает до процессов. А если нужна architecture diagram без процесса? |
| 4 | **Blueprints** | «Создай чертёж/план» | Метафорически сильно: «blueprint» = master plan. Cross-domain | Engineering-heavy ассоциация. «Blueprint» = тяжёлый, детальный. Не для vision-level |
| 5 | **Visual Evidence** (Q5 из RES2) | «Покажи визуальные доказательства» | Сильный фрейминг: ДОКАЗАТЕЛЬСТВА, не украшения. Подталкивает к содержательным диаграммам | «Evidence» = юридический/научный тон. Может быть awkward в HL (vision ≠ evidence) |
| 6 | **Value Maps** | «Нарисуй карту ценности» | Value-centric, прямо из TFW философии. Говорит: покажи ГДЕ создаётся ценность | Придуманный термин. Не индустриальный. Нужно обучение. Не покрывает технические диаграммы |
| 7 | **Flows** | «Покажи потоки» | Короткое, интуитивное, cross-domain. «User flow», «data flow», «value flow» — всё ложится | Слишком общее. «Flow» чего? Может быть и text flow. Не подсказывает РИСОВАТЬ |
| 8 | **Visual Overview** | «Покажи визуальный обзор» | Мягкое, инклюзивное. Не пугает бизнес-юзеров. «Overview» = обзор на том уровне, где мы сейчас | «Overview» = поверхностно. Может дать агенту разрешение на shallow diagrams |

### G5: Многоэтапный ресерч — анализ реальной практики

**VLM-3 (4 итерации) — ЧТО ФАКТИЧЕСКИ ПРОИЗОШЛО:**

| Итерация | Папка | Файлы | Кто запустил | Мотивация |
|----------|-------|-------|-------------|-----------|
| 1 | `research/` | briefing, gather, extract, challenge | User | Начальный ресерч по HL гипотезам |
| 2 | `research2/` | briefing, gather, extract, challenge | User (после чтения RES1) | Верификация фактов — RES1 исследовал не тот репо |
| 3 | `research3/` | briefing, gather, extract, challenge | User (после чтения RES2) | Sycophancy check — RES2 «зеркалил» user direction |
| 4 | `research4/` | briefing, gather, extract, challenge | User (после чтения RES3) | Thinking traces — конкретный новый инсайт от RES3 |

**TFW-32 (2 итерации) — ЧТО ФАКТИЧЕСКИ ПРОИЗОШЛО:**

| Итерация | Папка | Файлы | Кто запустил | Мотивация |
|----------|-------|-------|-------------|-----------|
| 1 | `research/` | briefing, gather, extract, challenge | User | Базовый ресерч по 8 гипотезам |
| 2 | `research2/` | briefing, gather, extract, challenge + RES file inside | User | Gaps от RES1 (naming, viz, multi-iter) |

**Паттерны из практики:**

1. **Каждая итерация имела КОНКРЕТНУЮ мотивацию** — не «продолжить», а «проверить/углубить/исправить»
2. **Briefing iteration 2+ ВСЕГДА ссылался на предыдущий RES** — Predecessor link + список проблем
3. **Папки нумеровались `researchN/`** — ad-hoc, не стандартизировано
4. **RES файлы нумеровались по-разному:**
   - VLM-3: `RES__`, `RES2__`, `RES3__`, `RES4__` (на уровне task root)
   - TFW-32: `RES__` (task root) + `RES__iter2__` (внутри research2/)
5. **Coordinator (user) контролировал:**
   - Когда запускать следующую итерацию
   - Фокус итерации (гипотезы, проблемы)
   - Решение «хватит» или «ещё»
6. **Researcher НЕ контролировал:**
   - Сколько итераций будет
   - Будет ли вообще следующая
   - Но RES2 TFW-32 добавил «Iteration Status» блок — полезно

**ЧТО ОТСУТСТВОВАЛО и МЕШАЛО:**

| Проблема | Где видна | Как решалась |
|----------|----------|--------------|
| Нет control file — coordinator помнил state в голове | VLM-3: 4 iteration без файла | Работало потому что один человек. Не масштабируется |
| Нет стандартного exit block от researcher | VLM-3 R1-R3: RES не говорил «вот что осталось» | User сам читал и решал. Отсутствие exit block = researcher «закрыл» без рекомендаций |
| Нет стандартного briefing template для iteration 2+ | TFW-32 R2, VLM-3 R2-R4: каждый briefing ad-hoc | Работало, но каждый раз заново изобретали формат |
| Нет naming convention для папок | `research2/` vs numbered | ad-hoc |
| RES файлы — нет единого места | VLM-3: все на task root. TFW-32: RES2 внутри research2/ | Путаница |

**ЧТО РАБОТАЛО ХОРОШО:**

| Паттерн | Почему работает |
|---------|----------------|
| Каждый researcher = fresh agent = fresh perspective | RES3 VLM-3 поймал sycophancy в RES2 именно потому что был другой агент |
| Predecessor link в briefing | Researcher знает историю, не начинает с нуля |
| User-driven focus для iteration 2+ | Coordinator видит gaps которые researcher не видит |
| RES2 TFW-32 «Iteration Status» block | Структурированный exit: итерация X of Y, что tested, что deferred, recommendation |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Иерархия: Data → Observations → Findings → Signals → Insights. TFW покрывает edges (Observations + Insights), middle (Fact Candidates) = вагное | Decision: какие варианты для обеих секций (§6 + §7) финальные |
| Naming-as-prompting = подтверждённый факт, не интуиция | Apply: критерий для decision matrix |
| 7 вариантов для §7 (человеческие знания), 5 для §6 (агентские наблюдения) | Narrow: decision matrix в Extract |
| 8 вариантов для визуализации | Narrow: decision matrix в Extract |
| Полная картина multi-iteration из двух проектов | Design: flow, файлы, exit protocol, briefing template |

**Sufficiency:**
- [x] External source used? (KM hierarchy, naming-as-prompting research, tacit knowledge terminology, visualization methodology)
- [x] Briefing gap closed? (все 3 направления покрыты вариантами)

**Deep mode criteria:**
- [x] Hypothesis tested? H5c (варианты собраны, D28 confirmed), H6c (варианты собраны), H7c (практика проанализирована)
- [x] Counter-evidence sought? Для каждого варианта есть «ПРОТИВ». Для multi-iteration проверено что НЕ работало

**Metacognitive check:** Обнаружил конкретную вещь — TFW information hierarchy. «Observations» (bottom) и «Insights» (top) УЖЕ правильно названы. «Fact Candidates» = вагное middle. Это не «два типа» (agent vs human), а ТРИ уровня зрелости информации. Это меняет framing решения.

Stage complete: YES
→ User decision: ___
