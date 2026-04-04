# HL — TFW-22: Coordinator & Research Enrichment

> **Дата**: 2026-04-04
> **Автор**: Coordinator (AI)
> **Статус**: 📝 HL_DRAFT — Updated after RESEARCH
> **RES**: [RES-TFW-22](RES__TFW-22__coordinator_research_enrichment.md)

---

## 1. Видение

Четыре связанных проблемы мешают координатору и ресерчеру работать на уровне, сопоставимом с качеством TS→executor цикла:

**A. HL без визуализации результата.**
Координатор описывает что и зачем, но не показывает *как это выглядит когда сделано*. Нет ascii-схем, mermaid, before→after таблиц. Исполнитель и юзер не видят «финальную картинку».

**B. RESEARCH-gate без структурного обоснования.**
Координатор формально показывает pros/cons, но не формулирует *слепые зоны, гипотезы, риски незнания*. RESEARCH должен быть всегда рекомендован с аргументами, а skip предложен как опция.

**C. Research workflow без структурированных алгоритмов мышления.**
SequentialThinking (hypothesis, revision, branching) и ClearThought (OODA, scientific method, mental models, metacognition) предлагают алгоритмы, которых в TFW research нет. Берём алгоритмы, не MCP зависимости. **RESEARCH выявил:** монолитный research.md → модульная архитектура research/{base,focused,deep}.md с OODA inner loop, Sufficiency Verdict, Trust Protocol. Validated by code analysis (6 algorithms) + industry best practices (modular instruction stack).

**D. Workflows = info dump, а не алгоритм (гипотеза).**
Executor идеально следует шагам TS — потому что TS = чёткий алгоритм с numbered steps. Workflows (plan.md, research.md) — наоборот: смесь алгоритма, справочных правил, дублирования conventions.md и inline таблиц. Агент теряет фокус в потоке информации. **Это наблюдение, а не доказанный факт** — требуется проверить в RESEARCH, что ref-pattern не ломает compliance.

> **Гипотеза:** Workflow = чёткий алгоритм (шаги → гейты → ветвления), а справочная информация (правила, ограничения, форматы) живёт в conventions.md/glossary.md/templates — workflow ссылается, не дублирует. **Требует валидации в RESEARCH** (H4).

## 2. Текущее состояние (As-Is)

### Дублирование в workflows

| Дублируемый блок | Файлы | Каноническое место | ~Строк |
|---|---|---|---|
| Anti-patterns | 7 workflow файлов | `conventions.md` §14 | ~10 per file |
| Role Lock rules | plan, handoff, review | `conventions.md` §15 | ~3 per file |
| Context Loading (полный список) | handoff, review | `conventions.md` §10 | ~10 per file |
| Scope Budget table | plan.md | `conventions.md` §6 | 8 строк |
| Status Transitions (full diagram) | plan, research | `conventions.md` §5 | 10 строк |
| Prerequisites (6 items) | plan.md | `conventions.md` §10 | 7 строк |

**Итого:** ~80-100 строк дублирования только в plan.md и research.md.

### Word counts (текущие)

| Workflow | Words | Limit (P10) | Budget |
|----------|-------|-------------|--------|
| plan.md | 1213 | 1200 | ⚠️ already over |
| research.md | 1165 | 1200 | 35 слов |
| handoff.md | 912 | 1200 | 288 |
| review.md | 750 | 1200 | 450 |
| resume.md | 552 | 1200 | 648 |

plan.md уже **над** лимитом. research.md в 35 словах от него. Добавление нового контента без рефакторинга = нарушение P10.

### HL Template (`.tfw/templates/HL.md`)

| Секция | Проблема |
|--------|----------|
| §3 To-Be | Текстовое описание, нет визуализации |
| — | Нет секции Research Justification |

### Внешние алгоритмы (изученные)

**SequentialThinking MCP** — пошаговое мышление с revision, branching, hypothesis testing.
**ClearThought MCP** — 38 операций: OODA loop, scientific method, mental models, collaborative reasoning, metacognitive monitoring.

| Концепция | Аналог в TFW | Что взять |
|-----------|-------------|-----------|
| Hypothesis testing | Challenge (частично) | Формализовать гипотезы в Briefing |
| OODA Orient | Нет | Фиксация текущего понимания перед Gather |
| Revision | Нет | Пересмотр выводов из предыдущих стейджей |
| Mental Models (inversion) | Нет | «Что если наш подход НЕПРАВИЛЬНЫЙ?» |
| Metacognitive Monitoring | Depth self-check | Расширить: «подтверждал что знал или нашёл новое?» |
| Multi-perspective | Нет | Рассмотреть с позиции executor/user/reviewer |

## 3. Целевое состояние (To-Be)

### 3.1 Визуализация результата

**Workflow как алгоритм (после рефакторинга plan.md):**

```
┌─────────────────────────────────────────────────┐
│              plan.md (~850-950 words)            │
│                                                 │
│  Header: Role Lock + Mindset (compact)          │
│                                                 │
│  Step 1: Load context                           │
│    → Step: read conventions.md §10, verify loaded│
│                                                 │
│  Step 2: Knowledge Gate                         │
│    → ref: conventions.md §10.2                  │
│                                                 │
│  Step 3: Research & Understand                  │
│    IF questions → ask (max 3-5), WAIT           │
│                                                 │
│  Step 4: Write HL                               │
│    → ref: templates/HL.md                       │
│    → MUST: fill §3.1 (visualization)            │
│    → MUST: fill §10 (hypotheses + blind spots)  │
│    → update task board                          │
│                                                 │
│  Step 5: Hypothesis Iteration                   │
│    → present §10 hypotheses to user             │
│    → user answers / confirms / rejects each     │
│    → WAIT for user                              │
│    IF all hypotheses closed → RESEARCH optional  │
│    IF open hypotheses remain → Step 6            │
│                                                 │
│  GATE: User approves HL                         │
│                                                 │
│  Step 6: RESEARCH decision                      │
│    → recommend research with §10 arguments      │
│    → offer skip as option                       │
│    → WAIT for user                              │
│    IF yes → /tfw-research                       │
│    IF skip → user confirms                      │
│                                                 │
│  Step 7: Write TS                               │
│    → ref: templates/TS.md                       │
│    → Step: read conventions.md §6 budget table  │
│    → Step: calculate if phase fits limits        │
│    IF exceeds → split or document override       │
│    IF large → multi-phase split                 │
│                                                 │
│  GATE: User approves TS                         │
│                                                 │
│  STOP: "Start /tfw-handoff"                     │
│                                                 │
│  Footer: role-specific anti-patterns (3 lines)  │
│    → ref: conventions.md §14-15 for full list   │
└─────────────────────────────────────────────────┘
```

**Research = модульная архитектура (confirmed by RESEARCH):**

```
.tfw/workflows/research/
├── base.md    (~500-600 words) ← Entry point + Core Algorithm
├── focused.md (~150-200 words) ← Scoped mode
└── deep.md    (~200-250 words) ← Hypothesis-driven mode

Sum: base + focused = 650-800 words < current 1165 ✅
Sum: base + deep    = 700-850 words < current 1165 ✅
```

**base.md — Core Algorithm:**

```
┌─────────────────────────────────────────────────┐
│  base.md — CORE RESEARCH ALGORITHM              │
│                                                 │
│  🔒 Role Lock: Coordinator (research mode)      │
│  Mindset: Critical thinking partner             │
│                                                 │
│  Step 1: Load context                           │
│    → Step: read conventions.md §10              │
│                                                 │
│  Step 2: Select mode                            │
│    → read PROJECT_CONFIG.yaml default_mode      │
│    → present to user, confirm                   │
│    → load research/{mode}.md                    │
│    → 🛑 WAIT                                    │
│                                                 │
│  Step 3: Create RES file                        │
│                                                 │
│  Step 4: Briefing Protocol                      │
│    → Research Plan + Hypotheses from HL §10     │
│    → 🛑 WAIT                                    │
│                                                 │
│  Step 5: Run stages (Gather/Extract/Challenge)  │
│    ┌─── FOR EACH STAGE ───────────────┐         │
│    │  OODA STAGE LOOP:                │         │
│    │  OBSERVE → ORIENT → DECIDE → ACT│         │
│    │  loops_per_stage from YAML       │         │
│    │                                  │         │
│    │  DECIDE = Sufficiency Verdict:   │         │
│    │  ☐ External source used?         │         │
│    │  ☐ Briefing gap closed?          │         │
│    │  + mode-specific criteria        │         │
│    │  ALL met → STAGE CHECKPOINT      │         │
│    │  NOT met + loops left → OBSERVE  │         │
│    │  NOT met + no loops → report     │         │
│    │                                  │         │
│    │  STAGE CHECKPOINT:               │         │
│    │  → present findings + questions  │         │
│    │  → 🛑 WAIT for user             │         │
│    └──────────────────────────────────┘         │
│                                                 │
│  Step 6: Final Checkpoint + Sufficiency Check   │
│  Step 7: Closure (HL recs + Fact Candidates)    │
│                                                 │
│  Trust Protocol:                                │
│  Business/domain → trust as-is                  │
│  Tech/algorithm → verify externally             │
│  Numbers/claims → verify empirically            │
│                                                 │
│  Footer: Rules (compact) + ref conventions §14  │
└─────────────────────────────────────────────────┘
```

**Mode files (focused.md / deep.md):**

```
┌───────────────────────┐  ┌───────────────────────┐
│  focused.md           │  │  deep.md              │
│  "Scan→Assess→Report" │  │  "Hypothesize→Test→   │
│                       │  │   Revise→Test"        │
│  loops_per_stage: 1   │  │  loops_per_stage: 3   │
│  verify_tech: true    │  │  verify_tech: true    │
│  counter_evidence: no │  │  counter_evidence: yes│
│  criteria: 2 generic  │  │  criteria: 2+2 = 4    │
│  metacognitive: no    │  │  metacognitive: yes   │
└───────────────────────┘  └───────────────────────┘
```

**HL template с новыми секциями:**

```
HL Template (после)
├── §1  Видение
├── §2  As-Is
├── §3  To-Be
├── §3.1 Визуализация результата  ← NEW
│   (ascii обязательно, mermaid для сложных flows,
│    generate images для UI/UX)
├── §4  Фазы
├── §5  DoD
├── §6  DoF
├── §7  Принципы
├── §8  Зависимости
├── §9  Риски
└── §10 Гипотезы и обоснование RESEARCH  ← NEW
    ├── Гипотезы (таблица: ID, гипотеза, статус)
    │   статусы: open / confirmed-by-user / refuted-by-user / needs-research
    ├── Слепые зоны
    ├── Риски незнания
    └── Предлагаемый фокус RESEARCH
```

**Итерация гипотез (Step 5 в plan.md):**

```
Coordinator формирует §10 → представляет юзеру:

  For each hypothesis:
    USER: "Знаю ответ" → confirmed/refuted, записать в таблицу
    USER: "Не уверен"  → needs-research
    USER: "Это не гипотеза, а очевидность" → удалить

  AFTER iteration:
    IF all hypotheses confirmed/refuted by user
      → RESEARCH can be skipped (user offers)
      → coordinator may still recommend if blind spots remain
    IF any hypothesis = needs-research
      → RESEARCH recommended
```

**Защита от фейковых гипотез:**
Каждая гипотеза проходит фильтр: «Если эта гипотеза окажется ложной — изменится ли наш подход?» Если нет — это не гипотеза, а background fact. Юзер = второй фильтр: может отклонить очевидные или бесполезные гипотезы.

### Гипотеза «Workflow = Algorithm» (H4)

Наблюдение: executor следует шагам TS идеально. Workflows — нет. Предположение: дело в формате (алгоритм vs info dump). **Требует проверки в RESEARCH.**

| Характеристика | Сейчас | Целевое (confirmed by RESEARCH) |
|----------------|--------|---------------------|
| Формат | Prose + embedded tables + inline rules | Numbered steps + gates + references |
| Справочные блоки | Inline (Anti-patterns, Context Loading, Status Transitions) | Ref inside algorithmic step (D1): «Step N: Read X → evaluate → act» |
| Role Lock + Mindset | Повторяется, но inconsistently | ALWAYS inline = DNA layer (D10) |
| Reference data | Inline | Library = ref (scope budgets, anti-patterns, transitions) |
| Длина | 1165-1213 words | 850-950 words target (plan.md), 500-600 (base.md) |
| Фокус агента | Теряется в справочном тексте | Держится на numbered steps |

**Предполагаемое правило** (если H4 подтвердится): workflow содержит ТОЛЬКО:
1. **Header** — Role Lock (1 blockquote) + Mindset (2-3 предложения)
2. **Algorithm** — numbered steps с IF/THEN ветвлениями и GATE/WAIT точками
3. **References** — `→ ref:` ссылки на conventions/glossary/templates для деталей
4. **Footer** — role-specific anti-patterns (3-5 строк, только уникальные для этого workflow). Полный список → ref conventions.md §14

## 4. Фазы

Три фазы. A — templates (HL + RES), B — plan.md refactor, C — research.md enrichment + refactor.

### Phase A: Templates 🔴
1. **`.tfw/templates/HL.md`** — добавить §3.1 «Визуализация результата», §10 «Обоснование RESEARCH»
2. **`.tfw/templates/RES.md`** — добавить секцию Hypotheses (таблица со статусами)

### Phase B: plan.md → Algorithm Refactor 🔴
1. **`.tfw/workflows/plan.md`** — рефакторинг в формат «шаги → гейты → ссылки»:
   - Replace inline bloat with **ref-inside-step** pattern (D1): NOT «→ ref:» one-liner, but «Step N: Read X → evaluate → act»
   - Role Lock + Mindset = ALWAYS inline (DNA layer, D10)
   - Remove inline Anti-patterns → Step: «Check conventions.md §14. Did I violate any?»
   - Remove inline Status Transitions → ref conventions.md §5
   - Remove inline Prerequisites → Step: «Load context per conventions.md §10»
   - Remove inline Scope Budget → Step: «Read conventions.md §6. Calculate. Split if exceeds»
   - Strengthen RESEARCH Gate: coordinator references §10 HL hypotheses
   - Add step: «Fill §3.1 (visualization) and §10 (hypotheses)»
   - Add Step 5: Hypothesis Iteration with user
   - Target: **~850-950 words** (с 1213). RES confirmed 393 words removable = post-removal 820 + enrichment
2. Adapter sync: `.agent/workflows/tfw-plan.md`, `.claude/commands/tfw-plan.md`

### Phase C: research/ → Modular Architecture + Enrichment 🔴

Replace monolithic `research.md` with directory `research/{base,focused,deep}.md`.
See [proposed architecture](proposed_research_readme.md) for full design.

1. **`.tfw/workflows/research/base.md`** (~500-600 words) — Core Algorithm:
   - Role Lock + Mindset (inline, DNA layer)
   - Step 1: Load context. Step 2: Select mode (read YAML → present → load mode file, Progressive Disclosure D12)
   - Step 3: Create RES. Step 4: Briefing + Hypotheses from HL §10
   - Step 5: Run stages with **OODA Stage Loop** (Observe→Orient→Decide→Act):
     - loops_per_stage = YAML hard limit (D11). Exceeded → force exit + report
     - Sufficiency Verdict: generic criteria (2) + mode-specific criteria (from mode file)
     - Checkpoint criteria = SOFT (report, not block)
   - Step 6: Final Checkpoint. Step 7: Closure
   - **Trust Protocol**: business/domain = trust. Tech = verify externally. Numbers = verify empirically (D3)
   - Footer: compact Rules + ref conventions §14

2. **`.tfw/workflows/research/focused.md`** (~150-200 words):
   - Mindset: «Scan → Assess → Report»
   - 1 OODA loop per stage
   - Checkpoint criteria: 2 generic only
   - Exit: min 1 decision per stage, max 2 turns

3. **`.tfw/workflows/research/deep.md`** (~200-250 words):
   - Mindset: «Hypothesize → Test → Revise → Test»
   - Up to N OODA loops (YAML: loops_per_stage, default: 3)
   - Checkpoint criteria: 2 generic + 2 mode-specific (hypothesis tested + counter-evidence)
   - Metacognitive check: «Did I discover or just confirm?»
   - Exit: min 2 decisions per stage, min 1 hypothesis tested

4. **`.tfw/PROJECT_CONFIG.yaml`** additions:
   ```yaml
   tfw.research:
     default_mode: focused
     modes:
       focused:
         loops_per_stage: 1
         verify_user_tech_claims: true
       deep:
         loops_per_stage: 3
         verify_user_tech_claims: true
         require_counter_evidence: true
   ```

5. Adapter sync: `.agent/workflows/tfw-research.md` → copy of `base.md`
   `.claude/commands/tfw-research.md` → copy of `base.md`
   (mode files NOT adapter-synced — loaded via ref from base.md)

## 5. Definition of Done (DoD)

**Phase A: Templates**
- ✅ 1. `templates/HL.md`: секция §3.1 «Визуализация результата» (ascii mandatory, mermaid для complex flows)
- ✅ 2. `templates/HL.md`: секция §10 «Обоснование RESEARCH» (слепые зоны, гипотезы, риски, фокус)
- ✅ 3. `templates/RES.md`: секция Hypotheses + Sufficiency Verdict checkpoint format

**Phase B: plan.md Refactor**
- ✅ 4. `plan.md`: рефакторинг — ref-inside-step pattern (D1), не pure ref
- ✅ 5. `plan.md`: inline bloat removed → algorithmic steps with refs
- ✅ 6. `plan.md`: Step 4 обязывает заполнить §3.1 и §10 в HL
- ✅ 7. `plan.md`: Step 5 — hypothesis iteration с юзером
- ✅ 8. `plan.md`: RESEARCH Gate ссылается на §10
- ✅ 9. `plan.md` ≤950 words (с 1213; 393 removable = 820 base + enrichment)
- ✅ 10. Role Lock + Mindset = inline (DNA layer, D10)

**Phase C: research/ Directory**
- ✅ 11. `research/base.md` exists with core algorithm (~500-600 words)
- ✅ 12. `research/focused.md` exists with mode-specific settings (~150-200 words)
- ✅ 13. `research/deep.md` exists with mode-specific settings (~200-250 words)
- ✅ 14. OODA Stage Loop implemented in base.md Step 5
- ✅ 15. Sufficiency Verdict: 2-level checkpoint (generic + mode-specific, D8)
- ✅ 16. Checkpoint criteria = SOFT. loops_per_stage = HARD LIMIT (D11)
- ✅ 17. Trust Protocol in base.md (4-tier: trust/verify/empirical, D3)
- ✅ 18. Progressive Disclosure: mode file loaded at Step 2, not start (D12)
- ✅ 19. PROJECT_CONFIG.yaml: tfw.research.default_mode + modes.{focused,deep} settings

**Cross-cutting**
- ✅ 20. Все адаптеры синхронизированы (base.md → 2 adapter copies)
- ✅ 21. Защита от фейковых гипотез: фильтр «изменит ли подход» + юзер
- ✅ 22. IF H4 confirmed: принцип «Workflow = Algorithm» задокументирован в conventions.md

## 6. Definition of Failure (DoF)

- ❌ 1. Word count любого workflow > 1200 (нарушение P10)
- ❌ 2. Ссылки `→ ref:` ведут на несуществующие секции conventions.md
- ❌ 3. Рефакторинг убирает role-lock enforcement из header (это ДОЛЖНО быть inline, не ref)
- ❌ 4. Новые секции в HL template становятся boilerplate
- ❌ 5. Research enrichment = MCP зависимости (берём АЛГОРИТМЫ, не инфраструктуру)

**При провале:** Если refs ломают compliance — вернуть критические правила inline (Role Lock). Если boilerplate — сократить до guided prompts.

## 7. Принципы

1. **Workflow = Algorithm (H4, partially confirmed)** — numbered steps, IF/THEN, GATE/WAIT. Ref = library, steps = inline. **RESEARCH confirmed:** ref works IF inside algorithmic step. Breaks WITHOUT step (D1)
2. **Algorithms, not infrastructure** — берём OODA, Scientific Method, Metacognition из ClearThought/SequentialThinking, не MCP зависимости
3. **Show the finish line** — HL §3.1 визуализация. ASCII mandatory, mermaid для complex flows
4. **Research = structured doubt** — HL §10 гипотезы. Coordinator рекомендует RESEARCH. User может закрыть гипотезы → skip обоснован
5. **Hypotheses have teeth** — фильтр «изменится ли подход если ложная?». User = второй фильтр
6. **DNA / Library split (D10)** — Role Lock + Mindset = ALWAYS inline (DNA layer). Reference data = library (budgets, anti-patterns). Step = self-contained: ref gives precision, not direction
7. **Naming > Explanation (H5)** — правильный термин создаёт правильные ассоциации. «Dreaming» = 1 слово вместо параграфов. Используем: OODA, Sufficiency Verdict, Trust Protocol, Progressive Disclosure
8. **Metacognition** — агент оценивает СВОЁ мышление: «подтверждал что знал или нашёл новое?»
9. **Progressive Disclosure (D12)** — agent gets ONLY what it needs NOW. Mode file loaded at Step 2, not start. Focused agent doesn't see deep rules

## 7.1 Quality Contract

Для всех фаз:
- **Inline enforcement:** Role Lock header, Mindset section, GATE/WAIT points — остаются в workflow (не refs)
- **Ref candidates:** Anti-patterns, Context Loading lists, Status Transitions, Scope Budget tables, Prerequisites
- **Format test:** каждый step начинается с номера. Gate — жирным. Wait — 🛑. Ref — `→ ref:` prefix

## 8. Зависимости

| Зависимость | Статус |
|-------------|--------|
| TFW-17 (research depth + coordinator quality) | ✅ DONE |
| TFW-21 (research workflow compression) | ✅ DONE |
| TFW-19 (config propagation) | ✅ DONE |
| `conventions.md` — все ref targets существуют (§5, §6, §10, §14, §15) | ✅ Verified |
| `research.md` word count = 1165 | ✅ |
| `plan.md` word count = 1213 | ⚠️ Already over limit |
| `templates/HL.md` = 71 lines | ✅ |
| `templates/RES.md` = 136 lines | ✅ |

## 9. Риски

| Риск | Вероятность | Влияние | Mitigation |
|------|-------------|---------|------------|
| «Ref indirection» — агент не читает ref | Низкая (mitigated) | Высокое | D1: ref-inside-step, not pure ref. D10: DNA layer inline. RESEARCH validated approach |
| Word target нереалистичен | **Closed** | — | **RESEARCH resolved:** plan.md target = 850-950 (393 removable = 820 base + enrichment) |
| OODA loop stall — агент застревает | Низкая | Среднее | D11: loops_per_stage = HARD LIMIT. Criteria = SOFT (report, not block) |
| Принцип Workflow=Algorithm ломает config.md sync registry | Средняя | Среднее | Обновить sync registry после рефакторинга (scope: в phase B/C) |
| 3 файла вместо 1 = overhead | **Closed** | — | **RESEARCH resolved:** sum < monolith (650-800 vs 1165). Progressive Disclosure bonus |
| Adapter sync для research/ directory | Средняя | Среднее | Only base.md needs adapter sync. Mode files loaded via ref |

## 10. Обоснование RESEARCH

### Слепые зоны
- **«Ref indirection» compliance**: conventions.md §14 (Anti-patterns) = 13 строк. Агент читает их при context loading, но повторная ссылка в workflow — достаточно ли для enforcement? Нет данных.
- **Word budget реальность**: plan.md 1213 → 700 = удалить 513 слов = 42%. Что именно уходит, что остаётся? Нужен построчный анализ.
- **Hypothesis Framing на практике**: работает ли «формулируй гипотезы до research» лучше чем «формулируй вопросы»? Нет evidence.

### Гипотезы

| # | Гипотеза | Статус | RESEARCH verdict |
|---|----------|--------|------------------|
| H1 | Ref-pattern НЕ снижает compliance, потому что conventions.md уже loaded | **partially confirmed** | Ref works IF inside algorithmic step (D1). Pure ref = Pattern B = broken. Ref-inside-step = Pattern A = working |
| H2 | Удаление inline bloat высвободит 300+ слов для enrichment | **confirmed** | 393 words removable from plan.md (32.4%). Post-removal = 820 |
| H3 | Hypothesis Framing улучшит фокус Gather stage | **needs validation** | Not testable in research. Will be validated in first execution |
| H4 | Workflow = algorithm лучше чем info dump | **partially confirmed** | Steps + gates = good. Ref-inside-step = good. Word budget achievable. Full validation after execution |
| H5 | **Naming > Explanation** — правильный термин создаёт правильные ассоциации. Маленький промпт + точные термины > длинный с объяснениями | **open — new** | Claude «dreaming» pattern. To be validated in execution |

### Риски незнания → CLOSED by RESEARCH
RESEARCH addressed all three original risks:
- ✅ Ref compliance → D1 (ref-inside-step), D10 (DNA layer inline)
- ✅ Word target realism → 393 words removable, target 850-950 (not 700)
- ✅ Hypothesis Framing quality → will be validated post-execution (H3)

### RESEARCH выполнен
RES файл: [RES-TFW-22](RES__TFW-22__coordinator_research_enrichment.md). 12 decisions, 7 questions closed, 3 stages complete. Architecture: [proposed_research_readme.md](proposed_research_readme.md).

---

*HL — TFW-22: Coordinator & Research Enrichment | 2026-04-04*
