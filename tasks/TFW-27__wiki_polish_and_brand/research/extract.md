# Extract — "What do we NOT see?"
> Parent: [HL-TFW-27](../HL-TFW-27__wiki_polish_and_brand.md)
> Goal: Wikipedia-style link resolution in compiled docs.

## Findings

### E1: Полная карта сущностей — что резолвить, что нет

gen_docs.py имеет 6 работающих резолверов. После анализа с пользователем — итоговая карта:

| Сущность | Паттерн | gen_docs.py | Действие |
|----------|---------|------------|----------|
| Artifact ref | `RF TFW-18` | ✅ Работает | — |
| Phase ref | `RF TFW-18/A` | ✅ Работает | — |
| HL-dash | `HL-TFW-19` | ✅ Работает | — |
| TD | `TD-59` | ✅ Работает | — |
| Decision | `D24` | ✅ Работает | — |
| Backtick path | `` `.tfw/conventions.md` `` | ✅ Работает | — |
| **Bare task ID** | `TFW-18` | ❌ | Добавить, запускать ПОСЛЕДНИМ |
| **Principle P{N}** | `P7` | ❌ | НЕ резолвить (double semantics). Только HTML-якоря |
| **Fact F{N}** | `F4` | ❌ | НЕ резолвить standalone (нумерация не глобальная) |
| **Strategic S{N}** | `S9` | ❌ | НЕ резолвить (task-local) |
| **File path no backticks** | plain text path | ❌ | НЕ делать (false positives) |

### E2: Направление ссылок — только forward

Пользователь уточнил: ссылки работают только в одном направлении.

- Source-колонки в таблицах KNOWLEDGE.md содержат `TFW-5 HL §7` → это ДОЛЖНА быть ссылка на задачу (forward). Покрывается bare task ID resolver.
- Обратная ссылка (из задачи на принцип) НЕ нужна — автор сам ставит если хочет.

### E3: F{N} — нумерация NOT глобальная

4 файла `knowledge/*.md` используют независимую нумерацию: F1 в process.md ≠ F1 в philosophy.md. Standalone `F4` неоднозначен. Резолвер F{N} невозможен без контекста файла.

Пользователь: если кто-то ссылается на факт, он укажет файл (`process.md F1`). Резолвится path файла через backtick resolver. Внутри файла F1 получает HTML-якорь для deep linking.

### E4: HTML-якоря на нумерованных таблицах

Нужны якоря на каждой строке нумерованных таблиц:
- KNOWLEDGE.md §0: `<a id="p1"></a>`, `<a id="p7"></a>` → `/knowledge-index/#p7`
- KNOWLEDGE.md §1: `<a id="d1"></a>`, `<a id="d24"></a>` → `/knowledge-index/#d24`
- TECH_DEBT.md: `<a id="td-72"></a>` → `/reference/tech-debt/#td-72`
- knowledge/*.md: `<a id="f1"></a>` → `/knowledge/process/#f1`

gen_docs.py добавляет при обработке ~30 LOC (regex по первому столбцу таблицы).

### E5: Markdown link rewriter — Source Manifest как маппинг

STATIC_SOURCES (строки 18-28 gen_docs.py) = готовая таблица source→output:
```
.tfw/conventions.md → reference/conventions.md
.tfw/glossary.md    → reference/glossary.md  
.tfw/README.md      → concepts/philosophy.md
README.md           → index.md
```

Алгоритм: для каждого `[text](target)` → resolve target relative to source dir → lookup в STATIC_SOURCES → rewrite. ~50 LOC.

Stage complete: YES
