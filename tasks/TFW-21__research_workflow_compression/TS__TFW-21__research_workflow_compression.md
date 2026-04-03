# TS — TFW-21: Research Workflow Compression

> **Date**: 2026-04-03
> **Status**: 🟡 TS_DRAFT

---

## Scope

Сжать `.tfw/workflows/research.md` c 2397 слов / 319 строк до ~1200 слов / ~150 строк. Синхронизировать `.agent/workflows/tfw-research.md`. Дополнить `templates/RES.md` checkpoint полями.

## Changes

### Step 1: Дополнить templates/RES.md

**File**: `.tfw/templates/RES.md`

Дополнить каждый Checkpoint (Gather, Extract, Challenge) полями:

```markdown
### Checkpoint: {Stage}
| Found | Remaining |
|-------|-----------|

**Agent assessment:** {one sentence — is this stage sufficient}
**Depth check:** Did I use external sources (web search, docs, URLs), or only project files?
**Recommendation:** close stage / dig deeper into {specific topic}
→ User decision: ___
```

Также добавить в Sufficiency Check строку:
```
- Did every stage include external research, or was it internal-only?
```

### Step 2: Сжать research.md

**File**: `.tfw/workflows/research.md`

Операции (в порядке выполнения):

1. **Research Mindset** (строки 16-26): сжать с 11 строк до ~6 строк. Сохранить tone, "critical thinking partner", "blind spots", "observations before questions". Убрать повторы.

2. **Example Flow** (строки 199-243): **удалить полностью** (45 строк). Template RES.md + Hard Rules = достаточная калибровка.

3. **"What good research looks like"** (строки 259-264): **удалить полностью** (6 строк). Дублирует Hard Rules #1-#3 и Mindset.

4. **"What bad research looks like"** (строки 266-272): **удалить полностью** (7 строк). Дублирует Anti-patterns секцию.

5. **"Operational"** (строки 274-278): **удалить** (5 строк). Повторяет Role Lock + уже сказано выше.

6. **Anti-patterns (второй блок, строки 303-318)**: **слить с Hard Rules** в один блок "Rules". Формат:
   - Hard rules = MUST-список (8 пунктов, компактно)
   - Anti-patterns = NEVER-список (5 ключевых, без дублирования Hard Rules)

7. **Inline Checkpoint format** (строки 131-144): **заменить ссылкой** на templates/RES.md. Одна строка: `Format: see templates/RES.md §Checkpoint`

8. **Inline Final Checkpoint / Sufficiency Check** (строки 146-170): **заменить ссылкой**. Одна строка: `Format: see templates/RES.md §Final Checkpoint`

9. **Closure Protocol** (строки 172-197): сжать — убрать inline quote-block пояснения, оставить numbered steps + constraint "HL is updated ALWAYS after research".

### Step 3: Синхронизировать adapter

**Command**: `cp .tfw/workflows/research.md .agent/workflows/tfw-research.md`

### Step 4: Верификация

```bash
wc -w .tfw/workflows/research.md    # target: ≤ 1300
wc -l .tfw/workflows/research.md    # target: ≤ 160
diff .tfw/workflows/research.md .agent/workflows/tfw-research.md  # target: no diff
```

## Constraints

- **MUST NOT** удалять или перефразировать stage mindset reminders (> Remember: ...)
- **MUST NOT** удалять Briefing Protocol
- **MUST NOT** менять 3-stage structure (Gather, Extract, Challenge)
- **MUST** сохранить все 8 Hard Rules (форма может измениться)
- **MUST** сохранить Research Mindset tone — сжать, не убрать

## DoD

- ✅ 1. research.md ≤ 160 строк
- ✅ 2. research.md ≤ 1300 слов
- ✅ 3. Все 8 Hard Rules сохранены
- ✅ 4. 3 stages + mindset reminders сохранены
- ✅ 5. Briefing + Closure сохранены
- ✅ 6. Нет inline шаблонов
- ✅ 7. `.agent/workflows/tfw-research.md` = копия
- ✅ 8. `wc` верификация
- ✅ 9. templates/RES.md checkpoint дополнен

## Verification

```bash
wc -w .tfw/workflows/research.md
wc -l .tfw/workflows/research.md
diff .tfw/workflows/research.md .agent/workflows/tfw-research.md
```

Ручная проверка: grep по каждому Hard Rule keyword.

---

*TS — TFW-21: Research Workflow Compression | 2026-04-03*
