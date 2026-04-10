# Extract — Iteration 3: "What do we NOT see?"
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Predecessors: RES1 (D1-D9), RES2 (D10-D14), [Gather](gather.md)
> Goal: Decision matrices для нейминга, design многоэтапного ресерча.

## E1: Единая философия нейминга

Из Gather G1 выявлена иерархия зрелости информации. Но TFW — не про зрелость данных. TFW — про **ценность и знание**. Поэтому философия нейминга должна идти от TFW, а не от KM-индустрии.

**Предлагаемая философия: «Кто видит, что видит, зачем записывает»**

```
                     ЗАЧЕМ записываем
                    ┌─────────────────────────────────────┐
                    │ Чтобы следующий агент/человек        │
                    │ принял ЛУЧШЕЕ решение               │
                    └─────────────────────────────────────┘
                              ↑
              ┌───────────────┼───────────────┐
              │               │               │
        КТО видит       КТО видит        КТО видит
        = Агент          = Агент          = Человек
        ЧТО видит       ЧТО видит        ЧТО видит
        = Tech debt     = Project facts  = Domain knowledge
              │               │               │
           §5 ←─── название ──→ §6 ←── название ──→ §7/§11
       Observations     [?????????]     [?????????????]
       (уже работает)   (нужен нейминг) (нужен нейминг)
```

**Три принципа для выбора названия:**

| # | Принцип | Тест |
|---|---------|------|
| P1 | **Название = промпт** (D28 + Claude Code Dreaming) | Новый агент без контекста, прочитав ТОЛЬКО название секции, начнёт писать нужный тип информации? |
| P2 | **Название = коммуникация** (user: «люди будут эти термины употреблять») | Бизнес-юзер скажет это слово в разговоре? «Мы нашли Strategic Signal» vs «У нас есть Fact Candidate»? |
| P3 | **Название = фильтр** (иерархия: не всё подряд, а конкретный тип) | Название ИСКЛЮЧАЕТ неподходящий контент? Или приглашает писать всё? |

## E2: Decision Matrix — секция §7/§11 (человеческие знания)

**Что эта секция ДОЛЖНА ловить:**
- Бизнес-контекст, недоступный из проекта
- Мотивы и приоритеты стейкхолдеров
- Доменное знание (отрасль, клиенты, рынок)
- Коррекции курса от человека
- Эмоции и preferences (процесс, инструменты)
- Forward-looking сигналы (тренды, риски)

**Human-Only Test:** Если агент мог бы узнать это из кода/файлов — это НЕ туда.

| # | Название | P1 Промпт (0-3) | P2 Коммуникация (0-3) | P3 Фильтр (0-3) | Cross-domain? | Итого |
|---|---------|:-:|:-:|:-:|:-:|:-:|
| A | Strategic Insights | 3 — «стратегические инсайты» = ищи бизнес-контекст, мотивы, последствия | 2 — бизнес-юзеры используют. Но «стратегический» = не всякий инсайт | 2 — фильтрует технику. Но пропускает эмоции и preferences | Да (бизнес, education, research) | **7** |
| B | Strategic Signals | 2 — «стратегические сигналы» = что-то начинается. Но сигнал ЧЕГО? | 2 — необычное сочетание. Люди не говорят «стратегический сигнал» повседневно | 2 — фильтрует технику. Но «signal» = ранний индикатор, а нам нужны и confirmed facts | Да | **6** |
| C | Stakeholder Intelligence | 2 — «разведка от стейкхолдеров» = точно. Но intimidating | 1 — никто в обычном разговоре не скажет «stakeholder intelligence» | 3 — сильнейший фильтр: только от стейкхолдеров, только high-value | Нет (enterprise only) | **6** |
| D | Discoveries | 2 — «открытия» = ищи новое. Но не направляет ЧТО именно | 3 — естественное слово, люди скажут «мы обнаружили что...» | 1 — слабый фильтр, «discovery» = всё что угодно новое | Да | **6** |
| E | Key Learnings | 2 — «ключевые уроки» = ретроспективно, что узнали | 3 — все знают этот термин из retrospectives | 2 — фильтрует пока ты НЕ рефлексируешь. Но не ловит forward-looking | Да | **7** |
| F | Domain Signals | 3 — «доменные сигналы» = ищи предметное знание | 1 — «domain» = IT-жаргон, бизнес-юзер не использует | 3 — точный фильтр: только domain knowledge, не tech | Частично | **7** |
| G | Field Notes | 1 — «полевые заметки» = записывай ВСЁ от первоисточника | 2 — понятно, но этнографический контекст далёк от IT | 1 — нулевой фильтр, «field notes» = всё подряд | Да | **4** |

**Топ-3: A (Strategic Insights = 7), E (Key Learnings = 7), F (Domain Signals = 7)**

Три лидера с равным счётом но разными ПРОФИЛЯМИ:
- **A — Strategic Insights**: сильный промпт, средний коммуникативно, средний фильтр. *Profile: analyst/PM*
- **E — Key Learnings**: средний промпт, сильная коммуникация, средний фильтр. *Profile: everybody*
- **F — Domain Signals**: сильный промпт, слабая коммуникация, сильный фильтр. *Profile: researcher/engineer*

**Мой анализ:** Оба сильных промптовых варианта (A, F) проигрывают в коммуникации. «Key Learnings» (E) коммуникативно сильнее, но слабый промпт — ретроспективный фокус, не ловит forward-looking.

**Возможный hybrid:** «Strategic Learnings»? Нет — не natural language.

**Я замечаю:** «Strategic Insights» уже РАБОТАЕТ в HL §11 и набрал 7 баллов. RES2 предложил менять на «Strategic Signals» (6 баллов). Это downgrade. Исходное название было лучше.

Вопрос: а нужно ли вообще менять §11?

| Сценарий | Strategic Insights ловит? |
|----------|:------------------------:|
| User: «18% клиентов = 80% выручки (Парето)» | ✅ — бизнес-инсайт |
| User: «Мне не нравится формат, хочу по-другому» | ⚠️ — preference, «стратегический»? |
| User: 😤 «Это меня бесит, агент отказывается работать» | ⚠️ — эмоция, не «стратегическое» |
| User: «В отрасли сейчас тренд на X» | ✅ — доменный инсайт |
| User: «Мы раньше пробовали Y и не сработало» | ✅ — исторический инсайт |

Проблема: preferences и эмоции выпадают. Но Human-Only Test их ловит: «Агент не знал бы без человека? → записывай». Значит проблема не в названии, а в INSTRUCTIONS.

**Рекомендация E2:** Оставить **«Strategic Insights»** для §11/§7. Усилить instructions: «Strategic = anything that changes how the team should act. Includes: domain knowledge, stakeholder priorities, emotional signals, process preferences.»

## E3: Decision Matrix — секция §6 (агентские наблюдения)

**Что эта секция ДОЛЖНА ловить:**
- Паттерны проекта (не code-level, а project-level)
- Conventions замеченные в проекте
- Constraints обнаруженные агентом
- Domain facts обнаруживаемые из данных (не от человека)
- Process наблюдения

**Agent-Can-Discover Test:** Если это можно узнать из кода, данных, файлов → сюда.
**Difference from §5 Observations:** §5 = tech debt, code quality. §6 = project knowledge, не баги.

| # | Название | P1 (0-3) | P2 (0-3) | P3 (0-3) | Cross-domain? | Итого |
|---|---------|:-:|:-:|:-:|:-:|:-:|
| a | Fact Candidates | 2 | 2 | 1 | Да | **5** |
| b | Project Patterns | 3 | 2 | 3 | Да | **8** |
| c | Operational Findings | 2 | 1 | 2 | Нет | **5** |
| d | Project Observations | 2 | 2 | 2 | Да | **6** |
| e | Fact Candidates (tighter) | 2 | 2 | 2 | Да | **6** |

**Явный лидер: b (Project Patterns = 8).** Но — теряет одноразовые факты.

Проблема серьёзная: «pattern» = повторяющееся. А если агент обнаружил одноразовый факт? «Проект использует PostgreSQL 16» — это не паттерн, это constraint. «Клиентская база — 50 городов» — не паттерн, это domain fact.

**Альтернативный подход:** а что если §6 НЕ НУЖНА как отдельная секция?

Текущий путь Fact Candidates: RF §6 → /tfw-knowledge → knowledge/ topic files.
Но «knowledge» = verified facts. А §6 = UNverified candidates.

Вопрос: может проблема не в названии §6, а в том что §6 пытается быть catch-all для двух разных вещей?

| В §6 сейчас попадает | Правильный дом |
|----------------------|---------------|
| Agent-observed project conventions | → §5 Observations (тип `convention`) |
| Agent-observed domain facts from data | → §6 (если Human-Only Test fails — agent CAN discover) |
| Human-shared domain knowledge | → §7 Strategic Insights (Human-Only Test passes) |

**Рекомендация E3:** Оставить **«Fact Candidates»** (вариант e — tighter instructions). Причины:
1. «Fact Candidate» = точный D28-фрейм: «это КАНДИДАТ в факт, не верифицированный факт»
2. «Candidate» = pipeline metaphor — записал → consolidated → verified
3. Проблема вагности решается instructions, не rename
4. 31 таск used this term. Backwards compatible
5. Шарпить instructions: «Project-level facts discoverable by reading code, data, or running commands. NOT tech debt (→ §5). NOT human-only knowledge (→ §7).»

## E4: Decision Matrix — секция визуализации

**Что эта секция ДОЛЖНА содержать:**
- HL: Value delivery flow (user → steps → value). Vision level
- RF: Technical process detail (APIs, DBs, sequences). Result level
- RES: Research findings visualization. Discovery level

**Единое название через все артифакты, разный контент через per-template instructions.**

| # | Название | P1 (0-3) | P2 (0-3) | P3 (0-3) | Работает для HL? | Работает для RF? | Итого |
|---|---------|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | Diagrams | 2 | 3 | 2 | ⚠️ (vision ≠ diagram) | ✅ | **7** |
| 2 | Visual Models | 2 | 1 | 2 | ✅ | ✅ | **5** |
| 3 | Process Maps | 3 | 2 | 3 | ✅ (value flow = process) | ⚠️ (не всё = process) | **8** |
| 4 | Blueprints | 2 | 2 | 2 | ⚠️ (heavy для vision) | ✅ | **6** |
| 5 | Visual Evidence | 3 | 1 | 3 | ❌ (vision ≠ evidence) | ✅ | **7** |
| 6 | Value Maps | 3 | 2 | 2 | ✅ | ❌ (tech detail ≠ value map) | **7** |
| 7 | Flows | 2 | 3 | 1 | ✅ | ⚠️ (не всё = flow) | **6** |
| 8 | Visual Overview | 1 | 2 | 1 | ✅ | ⚠️ (overview ≠ detail) | **4** |

**Два лидера: 3 (Process Maps = 8) и тройка на 7 (1, 5, 6).**

Проблемы:
- **Process Maps (8):** Сильнейший фрейминг для BPM/value delivery. Но в RF может быть architecture diagram, ERD schema — это не «process map»
- **Diagrams (7):** Универсальное, все знают. Но code-centric ассоциация
- **Visual Evidence (7):** Сильный фильтр (ДОКАЗАТЕЛЬСТВА). Но не работает в HL (vision ≠ evidence)
- **Value Maps (7):** TFW-native, value-centric. Но не покрывает tech diagrams в RF

**Я замечаю конфликт:** ни одно название не работает одинаково хорошо для HL (vision) и RF (detail). Это потому что КОНТЕНТ различается, а мы ищем ОДНО название.

**Два пути:**
1. **Umbrella term** — одно нейтральное слово + per-template instructions несут нагрузку
2. **Level-specific terms** — разные названия для HL и RF

User просил «одно четкое название». Значит путь 1.

Для umbrella: нужно слово которое:
- Не code-centric
- Не business-only
- Подсказывает РИСОВАТЬ (не писать текст)
- Cross-domain
- Люди говорят это слово

Из таблицы: **Diagrams** (7) — единственный вариант который коммуникативно сильнейший (P2=3) И работает для RF. Проблема «code-centric» решается instructions.

Но есть вариант которого НЕ было в таблице: **«Visual Map»** (singular concept).

| Тест | Result |
|------|--------|
| HL: «Покажи Visual Map ценности» | ✅ — «map = карта, обзор территории» |
| RF: «Покажи Visual Map реализации» | ✅ — «map = детальная карта» |
| RES: «Покажи Visual Map находок» | ✅ — «map = карта знания» |
| P1 (промпт) | 3 — «visual map» = нарисуй карту, покажи структуру |
| P2 (коммуникация) | 2 — люди говорят «карта», «показать на карте» |
| P3 (фильтр) | 2 — «map» = структурированное, не свободный рисунок |
| Cross-domain | ✅ — карты есть везде |

**Рекомендация E4:** Два финалиста на выбор координатора:

| | **Diagrams** | **Visual Map** |
|---|---|---|
| Сила | Universally understood. Zero learning curve | Value-neutral, cross-domain, «map» = навигация |
| Слабость | Code-centric ассоциация | Новый термин, нужно привыкнуть |
| Instruction load | Больше — нужно explains value-level vs detail-level | Меньше — «map at this level» natural |
| TFW-native? | Нет (industry standard) | Да (fits TFW value philosophy) |

## E5: Multi-iteration research — полный дизайн

### Принципы (из практики)

1. **Ресерч = самоведущий.** Каждая итерация ЯВНО оставляет gap list + directions
2. **min_iterations = 2** (hard floor). Одна итерация = confirmation bias risk
3. **Coordinator решает.** Researcher рекомендует, coordinator запускает
4. **Fresh agent = fresh perspective.** Каждая итерация = новая сессия/агент
5. **State = filesystem.** Control file + RES files = всё что нужно для handoff

### File structure

```
tasks/{ID}/
  HL-{ID}.md                              ← Master HL
  research/                                ← Iteration 1
    iterations.yaml                        ← Control file (coordinator creates)
    briefing.md
    gather.md
    extract.md
    challenge.md
  RES__iter1__{focus}.md                   ← Iteration 1 RES (task root)
  RES__iter2__{focus}.md                   ← Iteration 2 RES (task root)
  RES__iter3__{focus}.md                   ← Iteration 3 RES (task root)
  RES__{ID}.md                             ← Final consolidated RES (после всех итераций)
```

**Изменение от практики:** Все RES на task root (как в VLM-3). Stage files — ТОЛЬКО в `research/` (одна папка, not researchN/). Каждая итерация перезаписывает stage files, но RES-файлы накапливаются на task root.

**Почему одна папка `research/`:** Stage files — рабочие артифакты. Ценность = в RES. Хранить 4 копии gather.md нет смысла — RES содержит synthesis. Stage files = scratch, RES = trace.

**Counter-argument:** Потеря деталей из stage files предыдущих итераций. Но: RES содержит все ключевые facts, decisions, evidence. Если детали нужны — RES должен быть лучше, а не stage files дублироваться.

**Альтернатива (safer):** `researchN/` folders как сейчас. Все stage files сохраняются. Больше trace, больше disk, но zero information loss.

### iterations.yaml format

```yaml
# Research Iterations — TFW-32
# Created by: Coordinator
# Updated by: Coordinator after each iteration

task: TFW-32
min_iterations: 2          # Hard floor. Coordinator CANNOT proceed to TS before this
max_iterations: 5          # Soft cap. Beyond this = scope creep signal  
current: 3                 # Updated by coordinator

iterations:
  - id: 1
    status: complete       # complete | in-progress | planned
    focus: "docs-vs-knowledge, pipeline, terminology, positioning"
    hypotheses: [H1, H2, H3, H5, H7, H8]
    res_file: RES__iter1__methodology.md
    key_decisions: [D1, D2, D3, D4, D5, D6, D7, D8, D9]
    gaps_found:
      - "H6 deferred without investigation"
      - "D2 naming not D28-validated"
      - "Multi-iteration designed but untested"
    
  - id: 2
    status: complete
    focus: "naming precision, visualization, business processes, multi-iteration enforcement"
    hypotheses: [H5b, H6, H6b, H7b]
    res_file: RES__iter2__naming_visualization_multiiter.md
    key_decisions: [D10, D11, D12, D13, D14]
    gaps_found:
      - "Q5: visualization section exact name"
      - "Q6: Fact Candidates scope"
      - "Strategic Signals consolidation in /tfw-knowledge"
    
  - id: 3
    status: in-progress
    focus: "naming finals, visualization finals, multi-iteration formalization"
    hypotheses: [H5c, H6c, H7c, H_meta]
    res_file: null           # filled after completion
    key_decisions: []
    gaps_found: []
```

### Researcher exit protocol (mandatory block at RES end)

```markdown
## Iteration Status

- **Iteration:** {N} of {min_iterations} (min) / {max_iterations} (max)
- **Hypotheses tested:** {list}
- **Hypotheses deferred:** {list with reason}
- **Gaps discovered:** {numbered list}
- **New questions from user:** {if any}
- **Superseded decisions:** {list: "D10 supersedes RES1 D2"}

### Open Threads (for next iteration)
| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | {what} | {impact if ignored} | {gather/extract/challenge} |

### Recommendation
- [ ] SUFFICIENT — proceed to /tfw-plan
- [ ] MORE NEEDED — launch iteration {N+1}. Focus: {specific}
- [ ] BLOCKED — need user input on: {specific question}

> ⚠️ Coordinator decides. Researcher recommends but does NOT decide.
> If iteration < min_iterations → coordinator MUST launch next iteration.
```

### Briefing template for iteration 2+

```markdown
# Briefing — Iteration {N}: {Focus Title}
> Parent: [HL-{ID}](path)
> Predecessor: [RES iter{N-1}](path) — {one-line assessment}
> Mode: {focused/deep}
> Goal: {one sentence}

## Why This Iteration
{What gaps/problems/new insights triggered this iteration. Reference predecessor RES.}

## Open Threads from Iteration {N-1}
{Copy from predecessor RES "Open Threads" table. Mark which ones this iteration covers.}

## New Hypotheses
| # | Hypothesis | Source |
|---|-----------|--------|

## Research Plan
### Gather / Extract / Challenge
{bullets per stage}

## User Direction
{Record steering decisions}

---
Stage complete: YES / NO
```

### Coordinator gate (in plan.md)

After Step 5b (research) returns RES, coordinator checks:

```
IF current_iteration < min_iterations:
  MUST launch next /tfw-research. Cannot proceed to TS.
  
IF current_iteration >= min_iterations:
  READ all RES files + iterations.yaml
  ASSESS: are all HL hypotheses either confirmed, refuted, or explicitly deferred?
  IF yes → proceed to TS
  IF no → launch next iteration OR defer with justification
```

### Flow diagram

```
Coordinator writes HL
    ↓
Coordinator creates iterations.yaml (min=2)
    ↓
┌──────────────────────────────────┐
│  ITERATION LOOP                  │
│                                  │
│  Coordinator launches            │
│  /tfw-research in new agent      │
│       ↓                          │
│  Researcher reads:               │
│  - HL, conventions, glossary     │
│  - iterations.yaml               │
│  - ALL previous RES__iterN__*    │
│       ↓                          │
│  Researcher writes briefing      │
│  (template: iter 2+ if N>1)      │
│       ↓                          │
│  Researcher runs stages          │
│  (gather → extract → challenge)  │
│       ↓                          │
│  Researcher writes RES__iterN__* │
│  with mandatory Iteration Status │
│  + Open Threads table            │
│       ↓                          │
│  STOP. "Iteration N complete."   │
│                                  │
│  Coordinator reads RES           │
│  Updates iterations.yaml         │
│       ↓                          │
│  IF N < min_iterations → LOOP    │
│  IF N >= min AND gaps → LOOP     │
│  IF N >= min AND sufficient → ↓  │
└──────────────────────────────────┘
    ↓
Coordinator writes final RES__{ID}.md
(consolidation of ALL iteration RES files)
    ↓
Coordinator proceeds to TS
```

## Checkpoint

| # | Finding | Decision needed |
|---|---------|----------------|
| E1 | Единая философия: «Кто видит, что видит, зачем» | Coordinator validates |
| E2 | §7/§11: **Strategic Insights** (7 pts) = лучший. RES2 D10 «Strategic Signals» = downgrade (6 pts). Keep original + tighter instructions | Coordinator confirms or chooses alternative |
| E3 | §6: **Fact Candidates** stays. Instructions need sharpening, not rename | Coordinator confirms |
| E4 | Visualization: **Diagrams** vs **Visual Map** — two finalists | Coordinator picks |
| E5 | Multi-iteration: full design с iterations.yaml, exit protocol, briefing template, coordinator gate | Coordinator reviews design |
| E5b | Stage files: one `research/` folder (overwrite) vs `researchN/` (accumulate) | Coordinator picks |

**Sufficiency:**
- [x] External source used? (Gather G1-G5)
- [x] Briefing gap closed? (all 3 topics designed)

**Deep mode criteria:**
- [x] Hypothesis tested? H5c (comparison done, «Strategic Insights» = best), H6c (comparison done, two finalists), H7c (full design)
- [x] Counter-evidence sought? E3: tested «does §6 even need renaming?» → No. E4: tested «does one name work for all?» → Yes with instructions. E5: tested one-folder vs multi-folder

**Metacognitive check:** Я SURPRISED BY OWN FINDING. Шёл менять название — обнаружил что исходное «Strategic Insights» лучше предложенных альтернатив. RES2 D10 (rename to «Strategic Signals») = regression. Это classic pattern: «improve» sometimes = «break what works.» Вопрос к Challenge: правда ли что instructions fix the edge cases, или название ДОЛЖНО покрывать preferences/emotions?

Stage complete: YES
→ User decision: ___
