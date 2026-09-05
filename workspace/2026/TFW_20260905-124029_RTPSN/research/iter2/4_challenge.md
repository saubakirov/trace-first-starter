# Challenge — «Что ломает кандидатов?»
> **Mindset:** Critic. Конфигурации проверены на несовместимости и edge cases.
> **Test:** каждый оставшийся вариант имеет источник, ограничение и fallback.
> Parent: [HL-TFW_20260905-124029_RTPSN](../../HL-TFW_20260905-124029_RTPSN.md)
> Goal: выбрать grammar, которая остаётся детерминированной при resume, legacy ID, коллизиях и ограниченных host capabilities.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|-------------|-------------|-------------|-------------|------------------|
| D2. Task cue | любой task cue | D10. Область workflow | project-wide без single task | Title создаёт ложную task binding |
| D5. Phase cue | `Phase A` / `Ph.A` / bare `A` | D7. Момент разрешения | pre-read при неразрешённой фазе | Phase взята из запроса, а не из authoritative state |
| D6. Иерархия | `LEAD` | D7. Момент разрешения | pre-read без CRATM/delegation binding | Label создаёт видимость невыданного полномочия |
| D8. Collision fallback | полный task ID | exact semantic collision внутри одной task | same work/task/phase остаются одинаковыми |
| D8. Collision fallback | invented ordinal | D7. Момент разрешения | state-derived only | У ordinal нет canonical source, он меняется при archive/reorder |
| D9. Возможности host | rename unavailable | D9 procedure | обязательный readback success | Невозможная гарантия для host adapter |
| D10. Область workflow | docs batch / init attach-repair | D2. Task cue | один выбранный task | В этих режимах единого task context нет |
| D1. Первый cue | только emoji | G6 label constraint | human-language function label | Пиктограмма не задаёт однозначного текстового имени функции |

**Surviving configurations:**

| Config | D1 | D2 | D3 | Notes |
|--------|----|----|----|-------|
| C4 | workflow function | abbreviation | work→task→phase | Основная semantic configuration |
| C5 | workflow function | abbreviation | task→work→phase | Технически непротиворечива; отличается scan priority |
| C6 | workflow function | abbreviation | work→task→phase | ASCII transport fallback |
| C9 | hierarchy | abbreviation | hierarchy→task→phase | Только при уже существующем lead binding |
| C10 | workflow function | abbreviation | work→task | Корректна при отсутствующей/неоднозначной фазе |
| C11 | workflow function | abbreviation | work→task→phase | Условно task-bound docs mode |
| C12 | workflow function | legacy `TFW-##` | work→task→phase | Legacy compatibility без новой аббревиатуры |
| C13 | workflow function | full/derived ID | work→task→phase | New-task/init только после ID creation |
| C14 | workflow function | abbreviation | work→task→phase | Exact collision разрешается только существующим semantic discriminator |
| C15 | workflow function | abbreviation | work→task→phase | Rename без readback даёт unverified, не failed |
| C16 | workflow function | abbreviation | work→task→phase | Host failure reported once; основной workflow продолжается |
| C17 | — | — | — | Project-wide workflow не переименовывает task-bound session |

**Unexpected survivors:**

- `C6`: ASCII pipe остаётся полноценным transport fallback; длина равна middle-dot форме, а current corpus подтверждает его приём host.
- `C12`: `REVIEW · TFW-37 · A` совместим с той же grammar без миграции legacy ID.
- `C10`: отсутствие phase segment является положительным результатом разрешения, а не неполным title.

## Findings

### C1. Formal role и exact skill проигрывают functional cue

`Coordinator` не различает plan, resume и lead coordination; это уже проявилось
в четырёх одинаковых sidebar titles. `tfw-plan` различает workflow, но добавляет
четыре символа к `PLAN` и смешивает CLI spelling с пользовательским label.
Функциональные слова `PLAN`, `RESEARCH`, `EXEC`, `REVIEW`, `RESUME`, `DOCS`,
`INIT` короче, читаемы без emoji и дают взаимно однозначное отображение на
task-bound workflow surface. Поэтому C1–C3 и C8 исключаются из canonical form.

Это structural verdict, а не измерение скорости человека: эксперимент на время
и число ошибок не проводился. Следовательно, сильная часть H1 — «work function
лучше различает workflow» — поддержана; сравнительное «быстрее и точнее» пока
не доказано непосредственно.

### C2. Work-first и task-first равны по длине, но не по функции

`PLAN · CRATM · A` и `CRATM · PLAN · A` занимают по 16 code points. Task-first
удобен для группировки по task, но TFW tasks уже находятся внутри project/task
контекста, а главная неоднозначность текущего корпуса находится в work role.
Work-first сохраняет различающий functional cue в начале и создаёт одинаковый
prefix для поиска одной функции. W3C связывает ясные, concise и consistent
labels с предсказуемостью и поиском; это поддерживает единый work-first prefix,
но не заменяет UI-тест truncation.

Sources: [W3C Consistent Identification](https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification),
[W3C Headings and Labels](https://www.w3.org/WAI/WCAG21/Understanding/headings-and-labels).

### C3. Bare phase приемлем только как третий позиционный slot

`Phase A` самодостаточно читается, но добавляет шесть символов; `Ph.A` экономит
часть длины, одновременно вводя новую сокращённую лексику. Bare `A` однозначен
лишь после двух обязательных slots и внутри зафиксированной grammar. Поэтому
phase render должен быть точным canonical phase ID без слова `Phase`:
`PLAN · CRATM · A`, `EXEC · AFD-50 · A3-Q-R`. Если фаза отсутствует или выбор
неоднозначен, допустима только форма без третьего сегмента (`RESUME · CRATM`),
а не placeholder и не догадка.

Research iteration (`I2`) не является phase и не занимает phase slot. Она
остаётся в research artifacts/status, если governing task state явно не объявил
её canonical phase.

### C4. Middle dot устойчив как текст, но не даёт host-гарантии

Локальная проверка строки `PLAN · CRATM · A` показала неизменность во всех
четырёх .NET normalization forms (NFC, NFD, NFKC, NFKD); U+00B7 классифицируется
как punctuation, а не emoji. Unicode Normalization Forms гарантирует стабильность
нормализованных строк между версиями стандарта. Это снимает риск canonical
normalization drift, но не доказывает, что каждый host одинаково отображает,
обрезает или индексирует middle dot.

Canonical separator может быть ` SPACE U+00B7 SPACE`; если rename/readback
показывает, что host не сохранил его, transport fallback — ` SPACE | SPACE`.
ASCII hyphen отклонён: он визуально смешивается с дефисами внутри `TFW-37` и
phase IDs. Emoji отклонён из-за presentation variability и лишнего UTF-16 unit.

Sources: [Unicode Normalization Forms](https://www.unicode.org/reports/tr15/),
[Unicode Emoji presentation](https://www.unicode.org/reports/tr51/tr51-7.html).

### C5. Adversarial placement cases

| Case | Риск раннего rename | Surviving placement |
|------|---------------------|---------------------|
| `/tfw-plan`, новая task | ID ещё не существует | сразу после создания canonical ID |
| `/tfw-plan`, существующая task | слова запроса могут расходиться со state | после Read Contract task/phase resolution, до планирования |
| `/tfw-handoff` | pre-read instruction доверяет request label | после Read Contract Item 1, до ONB |
| `/tfw-review` | pre-read instruction доверяет request label | после Read Contract Item 1, до Map |
| `/tfw-research` | standalone mode может создать task; iteration не phase | после task/iteration resolution, до Briefing/stage work |
| `/tfw-resume` | может быть несколько candidate tasks/phases | после выбора одной task; phase только если однозначна |
| `/tfw-docs` | batch mode охватывает несколько tasks | после single-task Select/Triage; skip в batch |
| `/tfw-init` | attach/repair не создаёт task | только full-init, после создания init-task ID |
| project-wide workflows | task cue был бы ложным | rename rule не применяется |

Общий invariant: переименование выполняется в первой точке, где workflow уже
авторитетно разрешил все включаемые slots, и до первой substantive action.

### C6. Два collision fallback и hard edge

1. **Task abbreviation collision.** Если одна abbreviation соответствует двум
   доступным canonical task IDs, только конфликтующая task использует полный ID.
2. **Exact rendered-title collision.** Сначала используется уже существующий
   semantic discriminator: authoritative phase или `LEAD` binding. Если BASE
   всё ещё совпадает и host предоставляет stable thread key, возможен
   navigation-only suffix ` · @<short-stable-key>`. Он не является ролью,
   фазой или полномочием. Если stable key/rename недоступны, collision один раз
   сообщается, основной workflow продолжается, ordinal не выдумывается.

Второй fallback добавляет исключительный четвёртый transport segment к
трёхслотовой frozen grammar. Поэтому его нельзя скрыто внести как HL Refinement:
он должен быть отдельным Amendment Proposal для решения координатором.

### C7. Проверка new/resumed и host surface остаётся acceptance work

Current desktop доказывает rename/readback как capability, а Codex changelog —
`/rename` в современном CLI. Однако в Iteration 2 не создавалась новая session и
не переименовывалась resumed session: это прямо запрещено мандатом. Поэтому
DoD B7 должен проверяться при реализации на поддерживаемом host: один new-task
и один resumed-task title должны быть видимы/read back. Для unsupported host
допустим только одноразовый fail-soft report.

Source: [ChatGPT & Codex changelog](https://learn.chatgpt.com/docs/changelog).

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Functional work-first grammar пережила edge cases | Human timing/error comparison H1 не выполнен |
| Middle dot normalization стабилен; ASCII pipe годится как fallback | Pixel truncation и search indexing конкретных hosts не измерены |
| Bare phase безопасен только после authoritative resolution | Implementation должна показать new и resumed title |
| Placement rule выведен для всех 11 workflows | Остальные host adapters остаются unknown, не assumed |
| Два типа collisions имеют разные fallback | `@stable-key` требует явного решения по Amendment Proposal |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: YES
→ User decision: перейти к Synthesis и зафиксировать recommendations, verdicts и evidence limits согласно явному мандату.
