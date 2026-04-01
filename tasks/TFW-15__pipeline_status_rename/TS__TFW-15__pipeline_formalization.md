# TS — TFW-15: Pipeline Formalization

> **Дата**: 2026-04-01
> **Автор**: Coordinator (AI)
> **Статус**: 🟡 TS_DRAFT — Ожидает апрува
> **Parent HL**: [HL-TFW-15](HL-TFW-15__pipeline_status_rename.md)

---

## 1. Цель

Переименовать pipeline статусы с `🔵 HL` / `🟡 TS` на `📝 HL_DRAFT` / `🟡 TS_DRAFT`, добавить формальный status registry в PROJECT_CONFIG.yaml, обновить all pipeline strings и status tables in 9 live files. Перенумеровать Phase 3.5 → Phase 4.

## 2. Scope

### In Scope
- Pipeline string replacement (old → new) in all `.tfw/` live files and root README.md
- Status registry (`tfw.statuses`) in PROJECT_CONFIG.yaml
- Concept Taxonomy definitions in glossary.md
- Phase 3.5 → Phase 4 renumber + step numbering fix in plan.md
- HL.md and TS.md template status labels
- REJECT verdict → branching point in conventions.md

### Out of Scope
- Archived tasks (`tasks/TFW-{1..14}/`) — historical, no changes
- CHANGELOG.md — historical `Phase 3.5` references preserved
- Adapter files (`.claude/`, `.agent/`) — reference workflows, not statuses
- Document Status lifecycle (DRAFT/APPROVED in headers) — deferred
- Templates: ONB, RF, REVIEW, RES — no pipeline strings

## 3. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Add `tfw.statuses` registry with `role` field |
| `.tfw/conventions.md` | MODIFY | §5: pipeline, status table, skip path, REJECT branching |
| `.tfw/glossary.md` | MODIFY | Status Flow diagram, status count, Concept Taxonomy |
| `.tfw/README.md` | MODIFY | Task Lifecycle pipeline diagram + "8-status" reference |
| `.tfw/workflows/plan.md` | MODIFY | Phase 3.5 → 4, step renumber, `🔵 HL` refs, Status Transitions |
| `.tfw/workflows/research.md` | MODIFY | Status Transitions section (L278-281) |
| `README.md` (root) | MODIFY | Key Concepts pipeline + task board legend |
| `.tfw/templates/HL.md` | MODIFY | Status: `🔵 HL` → `📝 HL_DRAFT` |
| `.tfw/templates/TS.md` | MODIFY | Status: `🟡 TS` → `🟡 TS_DRAFT` |

**Бюджет:** 0 новых файлов, 9 модификаций. Лимиты — см. `tfw.scope_budgets` в `.tfw/PROJECT_CONFIG.yaml`.

## 4. Детальные шаги

### Step 1: PROJECT_CONFIG.yaml — Status Registry

Add `tfw.statuses` block after `tfw.research`:

```yaml
  statuses:
    - id: TODO
      emoji: "⬜"
      description: "Task registered, work not started"
    - id: HL_DRAFT
      emoji: "📝"
      description: "HL being drafted or discussed"
      role: coordinator
    - id: RES
      emoji: "🔬"
      description: "Research in progress (optional)"
      role: coordinator
    - id: TS_DRAFT
      emoji: "🟡"
      description: "TS written, awaiting approval"
      role: coordinator
    - id: ONB
      emoji: "🟠"
      description: "Executor onboarding"
      role: executor
    - id: RF
      emoji: "🟢"
      description: "Execution complete, RF written"
      role: executor
    - id: REV
      emoji: "🔍"
      description: "Review in progress"
      role: reviewer
    - id: DONE
      emoji: "✅"
      description: "Task closed"
    - id: BLOCKED
      emoji: "❌"
      description: "Blocked by dependency"
```

### Step 2: conventions.md — Pipeline + Status Table + REJECT

**§5 pipeline diagram (L97-105)**:
```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
                          (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)
```

**Status table (L107-117)** — replace:

| Status | Meaning |
|--------|---------|
| ⬜ TODO | Task planned, HL not started |
| 📝 HL_DRAFT | HL being drafted, awaiting review/approval |
| 🔬 RES | Research in progress (optional — user can skip to TS_DRAFT) |
| 🟡 TS_DRAFT | TS written, awaiting approval for execution |
| 🟠 ONB | Onboarding: executor studying the task |
| 🟢 RF | Execution complete, RF written |
| 🔍 REV | Review: reviewer checking RF |
| ✅ DONE | Task closed, traces updated |
| ❌ BLOCKED | Blocked by dependency |

**Task Board format (L119-122)** — update status example.

**Review verdicts (L124-128)** — REJECT updated:
```
- ❌ REJECT → 🛑 User decides: (a) 📝 HL_DRAFT, (b) 🔬 RES, (c) 🟡 TS_DRAFT
```

**Task Board legend (L128)** — update pipeline string.

### Step 3: glossary.md — Status Flow + Concept Taxonomy

**Status Flow section (L47-57)** — replace pipeline diagram + update "8 statuses" reference:
```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
                          (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)
```

Add **Concept Taxonomy** section after Status Flow: Document Type, Template, Workflow, Adapter Command, Status — definitions per HL §2.4.

### Step 4: .tfw/README.md — Task Lifecycle

**Pipeline diagram (L127-128)** — replace:
```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
              (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)
```

**"8-status lifecycle" text (L124, L280)** — keep "eight statuses" (count unchanged).

**Step list (L133-143)** — update step 1 "Write an HL" references and REJECT verdict wording.

### Step 5: plan.md — Phase Renumber + Status Refs

1. **Step 7 (L60)**: `🔵 HL` → `📝 HL_DRAFT`
2. **Phase 3.5 → Phase 4** (L68): rename header, keep content
3. **Phase 4 → Phase 5** (L86): rename header
4. **Step numbering fix** (L64): step 8 is missing (jumps 7→9). Renumber: 8→Notify, 9→Incorporate, 10→Repeat
5. **Status Transitions diagram (L142-149)**: replace with new pipeline:
```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
                          (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)        ↓
                                                                ❌ BLOCKED
```

### Step 6: research.md — Status Transitions

**L278-281** — replace:
```
Pipeline:   📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → ...
Standalone: ⬜ TODO → 🔬 RES → ✅ DONE (or → new task)
Skip:       📝 HL_DRAFT ··· 🟡 TS_DRAFT (user confirms skip)
```

### Step 7: README.md (root) — Key Concepts + Legend

**Key Concepts (L90)**: replace pipeline string:
```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE
```

**Task Board legend (L128)**: replace:
```
> Statuses: ⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE | ❌ BLOCKED
```

**TFW-15 row (L125)**: update status `🔵 HL` → `📝 HL_DRAFT` (after TS approval this becomes `🟡 TS_DRAFT`).

### Step 8: HL.md template

**L5**: `🔵 HL — Ожидает ревью` → `📝 HL_DRAFT — Ожидает ревью`

### Step 9: TS.md template

**L5**: `🟡 TS — Ожидает апрува` → `🟡 TS_DRAFT — Ожидает апрува`

## 5. Acceptance Criteria

- [ ] 1. Pipeline string `⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE` present in all 7 pipeline locations
- [ ] 2. `tfw.statuses` block in PROJECT_CONFIG.yaml with 9 entries and `role` field
- [ ] 3. conventions.md status table has `📝 HL_DRAFT` and `🟡 TS_DRAFT`
- [ ] 4. conventions.md REJECT = branching user decision point
- [ ] 5. glossary.md has Concept Taxonomy section
- [ ] 6. plan.md: no `Phase 3.5` (header renamed to `Phase 4`), no step gap
- [ ] 7. research.md: Status Transitions use `HL_DRAFT` / `TS_DRAFT`
- [ ] 8. HL.md template: `📝 HL_DRAFT — Ожидает ревью`
- [ ] 9. TS.md template: `🟡 TS_DRAFT — Ожидает апрува`
- [ ] 10. Grep `🔵 HL` in `.tfw/` (excluding CHANGELOG.md) → 0 results
- [ ] 11. Grep `Phase 3.5` in `.tfw/` (excluding CHANGELOG.md) → 0 results
- [ ] 12. No archived files (`tasks/TFW-{1..14}/`) modified

## 6. Риски фазы

| Риск | Mitigation |
|------|------------|
| Пропустить pipeline string location | RES Gather audit: 9 файлов, все locations записаны |
| Step renumber в plan.md сломает references | Адаптеры ссылаются на workflow file, не на step numbers |
| `_DRAFT` suffix непонятен новым агентам | glossary Concept Taxonomy + conventions status table |

---

*TS — TFW-15: Pipeline Formalization | 2026-04-01*
