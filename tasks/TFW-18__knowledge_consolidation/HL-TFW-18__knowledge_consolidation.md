# HL — TFW-18: Knowledge Consolidation

> **Дата**: 2026-04-03
> **Автор**: Coordinator (AI)
> **Статус**: 📝 HL_DRAFT — Updated after RESEARCH (RES-TFW-18)

---

## 1. Видение

Знания проекта сейчас теряются между чатами. Агенты выполняют задачи, в ходе работы узнают о проекте новые факты — архитектурные ограничения, внешние зависимости, бизнес-контекст, поведение инфраструктуры — но нигде их не фиксируют. RF записывает Observations (tech debt), но не записывает **что агент узнал о проекте**. Знания остаются в чате и пропадают.

**Три проблемы:**

1. **Нет механизма сбора** — ни один шаблон (RF, REVIEW, RES) не требует записывать факты о проекте
2. **Нет процесса консолидации** — tfw-docs работает с architecture decisions и tech debt, но не с фактами из чатов (предпочтения, контекст среды, бизнес-ограничения, забытые требования)
3. **Нет принудительного напоминания** — пользователь может месяцами не запускать tfw-docs, знания накапливаются в артефактах, но не попадают в KNOWLEDGE.md

> **Вдохновение:** Claude Code «dream» — 4-фазный процесс (Orient → Gather → Consolidate → Prune). TFW адаптирует эту идею: сбор через артефакты (не чаты), консолидация через `/tfw-knowledge`, mandatory gate каждые N задач.
>
> **Validated by RESEARCH (RES-TFW-18):** Design aligns with Zettelkasten (fleeting→permanent notes), LangMem (hot-path + background consolidation), Claude Code (topic files + index). See [RES](RES__TFW-18__knowledge_consolidation.md) for full analysis.

## 2. Текущее состояние (As-Is)

### Fact collection

| Артефакт | Что записывается | Что теряется |
|----------|-----------------|--------------|
| RF §5 Observations | Tech debt (code smells, missing tests) | Факты о проекте: бизнес-контекст, инфра, пользователи, среда |
| REVIEW §3 Tech Debt | Observations → triage | Факты из REVIEW сессии (reviewer видит вещи, которых executor не видел) |
| RES (full doc) | Decisions, open questions | Факты о домене, обнаруженные при исследовании |
| ONB §6 Inconsistencies | Code vs spec | Факты о расхождениях code/spec/reality |

### Knowledge consolidation (tfw-docs)

| Аспект | Состояние |
|--------|-----------|
| Trigger | After REVIEW or manual |
| Input | RF observations + architecture changes |
| Process | 5-item checklist (arch? decision? deprecated? debt? principle?) |
| Output | KNOWLEDGE.md sections 0-4 + TECH_DEBT.md |
| Missing | No fact collection. No contradiction check. No pruning. No mandatory schedule |

### User preferences

| Аспект | Состояние |
|--------|-----------|
| File | Не существует |
| Content | Язык, тон, стиль, привычки — нигде не записаны |
| Scope | Cross-project (одна персона, разные проекты) |

### Mandatory gate

| Аспект | Состояние |
|--------|-----------|
| Current | Нет. tfw-docs запускается когда пользователь вспомнит |
| Pipeline | `⬜ TODO → 📝 HL_DRAFT → ...` — ничего до TODO |

## 3. Целевое состояние (To-Be)

### 3.1 Fact Candidates — сбор в каждом артефакте

Каждый агент на финальной стадии пишет раздел **«Fact Candidates»** — вещи, которые он узнал о проекте, продукте, среде, которые могут быть полезны будущим агентам.

| Артефакт | Кто пишет | Когда |
|----------|-----------|-------|
| RF §6 Fact Candidates | Executor | При написании RF |
| REVIEW §5 Fact Candidates | Reviewer | При написании REVIEW |
| RES → Closure | Researcher | При закрытии RES |

**Формат:**

```markdown
## Fact Candidates

> Candidates are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.
> Record only if the next agent would make a DIFFERENT DECISION knowing this fact.
>
> Anti-patterns: "project uses git", "code is in Python", "tests exist"

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | environment | Production DB is on shared instance, not dedicated | User said in chat | High |
| 2 | process | Client expects weekly reports every Monday | Implied from TS constraints | Medium |
| 3 | convention | Team prefers explicit error messages over generic ones | Observed in code review | High |
```

**Категории** (domain-agnostic, TFW applies to any field):

| Category | Scope | Examples |
|----------|-------|----------|
| `environment` | Where the work lives | servers, tools, platforms, classrooms, labs, hosting |
| `process` | How work gets done | schedules, approvals, reporting cadence, grading rules |
| `stakeholder` | Who is involved | clients, students, reviewers, partners, regulators |
| `constraint` | What limits exist | budgets, deadlines, legal, compliance, technical limits |
| `convention` | Agreed standards | naming, style, format, language, tone |
| `domain` | Subject matter | business rules, scientific models, curriculum, regulations |
| `context` | Background knowledge | history, prior decisions, external factors, market conditions |
| `risk` | Known dangers | fragile dependencies, single points of failure, assumptions |

> Categories are open — agents can use custom categories when none fit. The list above is guidance, not exhaustive.

### 3.2 User Preferences — отдельный файл под .gitignore

```
project-root/
├── .user_preferences.md    # ← gitignored, personal
```

**Содержимое:** язык общения, тон, стиль работы, привычки, timezone, предпочтения инструментов. Записывается один раз, обновляется агентом если замечает изменения.

### 3.3 `/tfw-knowledge` — отдельный workflow (Dream-like consolidation)

> **RESEARCH decision R5:** Separate workflow, NOT tfw-docs extension. Different trigger (periodic vs per-task), different duration (10-20 min vs 2 min), different scope (batch vs single).

Новый workflow `/tfw-knowledge` с 4 фазами:

```
Phase 1: Orient — прочитать KNOWLEDGE.md + knowledge/ topic files, понять текущее состояние знаний
Phase 2: Gather — собрать Fact Candidates из всех RF/REVIEW/RES с момента последней консолидации
Phase 3: Consolidate — сверить, дедуплицировать, разрешить противоречия, записать в topic files
Phase 4: Prune — удалить устаревшее, пометить непроверенное, обновить индекс в KNOWLEDGE.md §5
```

**Capabilities:**
- **Fact verification** — если факт повторяется в ≥2 артефактах → автоматически «verified». Если один раз → «unverified», агент спрашивает пользователя
- **Contradiction detection** — если два факта противоречат → агент поднимает вопрос
- **Staleness** — факты без источника или с источником > N задач назад помечаются для проверки
- **Marker** — проверенные артефакты маркируются `fact-candidates: processed YYYY-MM-DD`
- **Statistics** — обновляет stats в `knowledge_state.yaml` (total, verified, unverified, rejected)

**tfw-docs остаётся как есть** — quick per-task pass (sections 0-4 KNOWLEDGE.md). Получает п.6 в checklist: "Fact Candidates present? They will be processed during next `/tfw-knowledge`."

### 3.4 Knowledge Gate — отдельный lifecycle

Knowledge Gate живёт **отдельно от основного pipeline**. Не новый статус для задач, а отдельная сессия с собственным трекингом.

**Трекинг: `.tfw/knowledge_state.yaml`**

```yaml
# State — updated by /tfw-knowledge. Config → see tfw.knowledge in PROJECT_CONFIG.yaml
knowledge:
  last_consolidation_seq: 15    # seq of last task when consolidation ran
  last_consolidation_date: 2026-04-03
  stats:
    total_facts: 23
    verified: 18
    unverified: 5
    rejected: 2
    candidates_processed: 47
    sources_scanned: 12
```

> **RESEARCH decision R7:** No `pending_candidates` — seq-based check sufficient.

**Lifecycle (2 статуса, своя сессия):**

```
🔍 SCAN → ✅ CONSOLIDATED
```

- `🔍 SCAN` — агент сканирует все артефакты с момента `last_consolidation_seq`, собирает Fact Candidates
- `✅ CONSOLIDATED` — пользователь подтвердил, topic files обновлены, `last_consolidation_seq` сдвинут

**Правила:**
- Coordinator проверяет в **Phase 0 plan.md**: `(current_seq - last_consolidation_seq) >= interval`
- Gate mode configurable: `tfw.knowledge.gate_mode: hard` (default) / `soft` / `off`
- `hard` → hard stop: "Knowledge consolidation overdue. Run `/tfw-knowledge` before proceeding." Skip requires justification
- `soft` → reminder only, user decides
- Consolidation = отдельная сессия (`/tfw-knowledge`), 5-10 минут
- Основной pipeline **не трогается**: никаких новых статусов, никаких pipeline diagram changes

**В plan.md:** Phase 0: Knowledge Gate Check (перед Phase 1).

### 3.5 KNOWLEDGE.md + `knowledge/` — index + topic files

> **RESEARCH decision R4:** Claude Code uses topic files to offload detail from MEMORY.md index. TFW adopts: KNOWLEDGE.md §5 = compact index, `knowledge/` = detail.

**Структура:**
```
project-root/
├── KNOWLEDGE.md              # index (≤200 строк, configurable)
├── knowledge/                # topic files (project-specific facts)
│   ├── environment.md
│   ├── stakeholders.md
│   └── domain.md
├── .tfw/
│   └── knowledge_state.yaml  # state + statistics (infrastructure)
```

**KNOWLEDGE.md §5 (compact index):**
```markdown
## 5. Project Facts

> Index of project knowledge. Details in `knowledge/` topic files.

| Category | Count | Topic File |
|----------|-------|------------|
| environment | 7 facts | [→](knowledge/environment.md) |
| stakeholder | 4 facts | [→](knowledge/stakeholders.md) |
| domain | 12 facts | [→](knowledge/domain.md) |
```

**Topic file format (`knowledge/environment.md`):**
```markdown
# Knowledge: Environment

| # | Fact | Verified | Source(s) | Added |
|---|------|----------|-----------|-------|
| F1 | Production DB on shared PostgreSQL 16 | ✅ 2x | RF TFW-8, RF TFW-12 | 2026-03-15 |
| F2 | Service lives in Docker Swarm, not K8s | ✅ confirmed | RF SLC-3, RF SLC-7 | 2026-03-20 |
```

**Configurable limits (PROJECT_CONFIG.yaml):**

| Parameter | Default | Config key |
|-----------|---------|------------|
| KNOWLEDGE.md max lines | 200 | `tfw.knowledge.max_index_lines` |
| §5 index max lines | 30 | `tfw.knowledge.max_index_facts_lines` |
| Topic file max facts | 50 | `tfw.knowledge.max_facts_per_topic` |
| Topic files max count | 8 (soft) | `tfw.knowledge.max_topic_files` |
| Consolidation interval | 5 | `tfw.knowledge.interval` |
| Gate mode | hard | `tfw.knowledge.gate_mode` |

## 4. Фазы

### Phase A: Fact Candidates — templates + collection mechanism 🔴
- Добавить §6 Fact Candidates в RF.md template (mandatory)
- Добавить §5 Fact Candidates в REVIEW.md template (mandatory)
- Добавить Fact Candidates в RES.md Closure section (mandatory)
- Добавить quality filter в template: "Would the next agent decide differently?"
- Добавить mindset reminders в handoff.md, research.md, review.md
- Создать `.user_preferences.md` template + `.gitignore` entry в init.md
- Обновить conventions.md (Fact Candidates definition, categories)
- Обновить glossary.md (new terms)

### Phase B: `/tfw-knowledge` workflow + knowledge infrastructure 🔴
- Создать `.tfw/workflows/knowledge.md` — 4-phase process (Orient → Gather → Consolidate → Prune)
- Создать `knowledge/` папку с template topic file
- Добавить §5 Project Facts (compact index) в KNOWLEDGE.md template
- Создать `.tfw/knowledge_state.yaml`
- Добавить `tfw.knowledge` section в PROJECT_CONFIG.yaml (limits + gate_mode)
- Обновить tfw-docs checklist (п.6: Fact Candidates marker)
- Обновить conventions.md (новые файлы: knowledge.md workflow, knowledge_state.yaml, knowledge/ folder)
- Обновить glossary.md (Knowledge Gate, Consolidation, Topic File)
- Обновить adapters (Antigravity + Claude Code)

### Phase C: Knowledge Gate — plan.md integration 🟡
- Добавить Phase 0: Knowledge Gate Check в plan.md
- Обновить plan.md adapters (Antigravity + Claude Code)

### Future TODOs (к записи в Task Board)
- `tfw-config` — пропагация yaml config changes во все workflows/adapters
- `tfw-user-tune` — personal preferences pipeline (.user_preferences.md lifecycle)

## 5. Definition of Done (DoD)

- ✅ 1. RF.md template: §6 Fact Candidates section (mandatory)
- ✅ 2. REVIEW.md template: §5 Fact Candidates section (mandatory)
- ✅ 3. RES.md template: Fact Candidates in Closure (mandatory)
- ✅ 4. Quality filter in template: "Would the next agent decide differently?"
- ✅ 5. Mindset reminders in handoff.md, research.md, review.md
- ✅ 6. `.user_preferences.md` template exists, `.gitignore` guidance in init workflow
- ✅ 7. `.tfw/workflows/knowledge.md` — 4-phase consolidation workflow
- ✅ 8. `knowledge/` folder with topic file template
- ✅ 9. KNOWLEDGE.md template: §5 compact index with links to topic files
- ✅ 10. `.tfw/knowledge_state.yaml` with stats tracking
- ✅ 11. `tfw.knowledge` section in PROJECT_CONFIG.yaml (limits + gate_mode)
- ✅ 12. tfw-docs checklist updated (p.6: Fact Candidates marker)
- ✅ 13. plan.md: Phase 0 Knowledge Gate Check before Phase 1
- ✅ 14. glossary.md: new terms (Fact Candidate, Knowledge Gate, Consolidation, Topic File)
- ✅ 15. All adapters synced (Antigravity + Claude Code)
- ✅ 16. No changes to main pipeline diagrams (separate lifecycle)

## 6. Definition of Failure (DoF)

- ❌ 1. Fact Candidates section = empty «No candidates» в каждом RF (агенты игнорируют)
- ❌ 2. DOCS gate becomes bureaucracy — 10 minutes of user time every 5 tasks с нулевой ценностью
- ❌ 3. tfw-docs consolidation раздувает KNOWLEDGE.md до нечитаемого размера (>300 строк)
- ❌ 4. Агенты записывают trivial facts («project uses git»)

**При провале:**
- DoF-1: Усилить примерами в шаблоне, добавить anti-pattern «No candidates» в review checklist
- DoF-2: Сделать gate soft (recommendation) вместо hard
- DoF-3: Ввести лимит на §5 (≤30 facts) + pruning phase
- DoF-4: Добавить quality criteria в template

## 7. Принципы

1. **Facts ≠ Observations** — Observations = tech debt (code issues). Facts = project knowledge (бизнес, инфра, среда, стейкхолдеры). Два разных типа информации, два разных pipeline'а.
2. **Candidates ≠ Facts** — Agents записывают **кандидатов**. Они становятся фактами только после consolidation (tfw-docs). Один источник = unverified. Два+ = verified.
3. **Dream, not database** — Цель не собрать все факты, а собрать **полезные**. Quality > quantity. Факт полезен если будущий агент принял бы другое решение, зная его.
4. **Gate protects quality** — Knowledge Gate защищает от drift: знания накапливаются в артефактах, но не попадают в KNOWLEDGE.md. Gate = принудительная синхронизация. Отдельный lifecycle — не трогает основной pipeline.
5. **Preferences are personal** — `.user_preferences.md` = gitignored, personal, cross-project applicable. Project facts = shared, committed, project-specific.
6. **Domain-agnostic categories** — TFW работает в образовании, бизнесе, инженерии, дизайне, науке. Категории фактов должны быть универсальными: `environment`, `process`, `stakeholder`, не `infra`, `integration`, `deployment`.
7. **Configurable by design** — Лимиты, gate mode, interval — всё в PROJECT_CONFIG.yaml. Defaults (разумные) + override (под проект).

## 8. Зависимости

| Зависимость | Статус |
|-------------|--------|
| RF.md template | ✅ current |
| REVIEW.md template | ✅ current |
| RES.md template | ✅ current |
| docs.md workflow | ✅ current |
| KNOWLEDGE.md template | ✅ current |
| conventions.md | ✅ current |
| glossary.md | ✅ current |
| plan.md | ✅ current (v0.5.5) |

## 9. Риски

| Риск | Вероятность | Влияние | Mitigation |
|------|-------------|---------|------------|
| Fact Candidates = noise (too many trivial facts) | Высокая | Среднее | Quality examples in template + pruning in consolidation |
| DOCS gate friction | Средняя | Высокое | Make it lightweight (scan → propose → approve, <5 min) |
| KNOWLEDGE.md grows unbounded | Средняя | Среднее | Prune phase + size limit (≤30 facts in §5) |
| Blast radius concerns | ~~Средняя~~ Низкая | ~~Среднее~~ Низкое | Knowledge Gate = separate lifecycle, no pipeline changes. Only plan.md gets Phase 0 check |
| Contradiction resolution = hard | Низкая | Среднее | Agent flags, user resolves — no auto-resolution |

---

*HL — TFW-18: Knowledge Consolidation | 2026-04-03*
