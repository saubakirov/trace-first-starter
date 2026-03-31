# TS — TFW-13 / Phase B: Adapter Docs + References Cleanup

> **Дата**: 2026-03-30
> **Автор**: Coordinator (AI)
> **Статус**: 🟡 TS — Ожидает апрува
> **Parent HL**: [HL-TFW-13](HL-TFW-13__tfw_init_workflow.md)
> **Research**: [RES__TFW-13](RES__TFW-13__tfw_init_workflow.md)

---

## 1. Цель

Перенести "How to Write a New Adapter" из старого init.md в `.tfw/adapters/README.md`, обновить все ссылки на init.md по проекту, добавить init.md в conventions/glossary/Role Lock, обновить Antigravity README (Phase A Obs #1), обновить root README Quick Start (Phase A Obs #2).

## 2. Scope

### In Scope
- Создать `.tfw/adapters/README.md` с adapter docs из старого init.md
- Обновить `.tfw/conventions.md`: §2 (add init.md workflow), §8 (add init.md to table), §15 (add init.md to Role Lock)
- Обновить `.tfw/glossary.md`: add tfw-init term
- Обновить `.tfw/adapters/antigravity/README.md`: add tfw-init.md to copy instructions
- Обновить `.tfw/PROJECT_CONFIG.yaml`: add init to `tfw.workflows`
- Обновить `KNOWLEDGE.md`: add TFW-13 to key artifacts + D-record

### Out of Scope
- Workflow content changes (done in Phase A)
- Root README Quick Start (minor style, not blocking — defer or do if time permits)

## 3. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/adapters/README.md` | CREATE | "How to Write a New Adapter" (moved from old init.md) |
| `.tfw/conventions.md` | MODIFY | §2: add workflow. §8: add to table. §15: add to Role Lock |
| `.tfw/glossary.md` | MODIFY | Add tfw-init term |
| `.tfw/adapters/antigravity/README.md` | MODIFY | Add tfw-init.md to copy and sync instructions |
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Add `init: .tfw/workflows/init.md` to `tfw.workflows` |
| `KNOWLEDGE.md` | MODIFY | Add TFW-13 key artifact + D18 (init as workflow) |

**Бюджет:** 1 новый файл, 5 модификаций. Лимиты — см. `tfw.scope_budgets` в `.tfw/PROJECT_CONFIG.yaml`.

## 4. Детальные шаги

### Step 1: Создать `.tfw/adapters/README.md`

Перенести секцию "How to Write a New Adapter" из старого init.md (строки 204-231 оригинала, сохранены в git history). Содержание:

```markdown
# TFW Adapters

## Available Adapters

| Tool | Adapter Dir | Entry Point |
|------|------------|-------------|
| Claude Code | `.tfw/adapters/claude-code/` | `CLAUDE.md` |
| Cursor | `.tfw/adapters/cursor/` | `.cursor/rules/tfw.mdc` |
| Antigravity | `.tfw/adapters/antigravity/` | `.agent/rules/tfw.md` |

See each adapter's README for setup instructions.

## How to Write a New Adapter

An adapter is a bridge between a development tool and `.tfw/`. Requirements:

1. **Entry point** — the file your tool auto-loads (e.g., CLAUDE.md, .cursor/rules/*.mdc)
2. **References `.tfw/`** — points to conventions, glossary, workflows. Never duplicates them.
3. **Minimal** — ≤35 lines of content. Project-specific sections only.
4. **Contains**:
   - Reference to `.tfw/README.md` (philosophy)
   - Reference to `.tfw/conventions.md` (rules)
   - Context loading order
   - Reference to `.tfw/workflows/` (all canonical workflows)
   - Conduct rules (no sycophancy, no placeholders)

### Template structure

{markdown}
# TFW {version}
Read `.tfw/README.md` for philosophy. Follow `.tfw/conventions.md`.
Workflows: see `tfw.workflows` in `.tfw/PROJECT_CONFIG.yaml`.
Context: AGENTS.md → .tfw/conventions.md → .tfw/glossary.md
Rules: no sycophancy, no placeholders, user's language.
{/markdown}

Place adapter template in `.tfw/adapters/{tool-name}/` with a README explaining setup.
```

### Step 2: Обновить `.tfw/conventions.md`

1. **§2 Required Artifacts** — добавить:
   ```
   - `.tfw/workflows/init.md` — canonical initialization workflow.
   ```

2. **§8 Workflows** — добавить строку в таблицу:
   ```
   | [init.md](workflows/init.md) | Coordinator | Discover project → interview → knowledge → setup → verify |
   ```

3. **§15 Role Lock Protocol** — добавить строку:
   ```
   | `init.md` | Coordinator | RES, RF, project config files | HL, TS, code |
   ```

### Step 3: Обновить `.tfw/glossary.md`

Добавить термин:

```markdown
## tfw-init (Workflow)
Canonical initialization workflow for bootstrapping TFW in a new project.
AI agent discovers project, interviews user, runs /tfw-research for knowledge
gathering, creates all TFW files, registers itself as {PREFIX}-1 on Task Board.
One-time use. Lives in `.tfw/workflows/init.md`.
```

### Step 4: Обновить `.tfw/adapters/antigravity/README.md`

Добавить `tfw-init.md` в секции "Copy TFW workflows" и "Keeping Workflows in Sync":

```bash
cp .tfw/workflows/init.md .agent/workflows/tfw-init.md
```

Также добавить в tree-пример в секции "Add project-specific rules and workflows".

### Step 5: Обновить `.tfw/PROJECT_CONFIG.yaml`

Добавить в `tfw.workflows`:
```yaml
    init: .tfw/workflows/init.md
```

### Step 6: Обновить `KNOWLEDGE.md`

1. **Architecture Decisions** — добавить:
   ```
   | D18 | `tfw-init` as AI-first workflow replacing manual init.md | Agent discovers, interviews, researches, sets up — human init.md was inverted (90% mechanical, 10% valuable) | TFW-13 HL §2-§3 |
   ```

2. **Key Artifacts** — добавить:
   ```
   | TFW-13 | tfw-init workflow | `tasks/TFW-13.../HL-TFW-13...md` | Init as AI-first workflow, {PREFIX}-1 pattern, /tfw-research in init |
   ```

## 5. Acceptance Criteria

- [ ] `.tfw/adapters/README.md` exists with adapter table + "How to Write" section
- [ ] `conventions.md` §2 lists init.md, §8 has init.md row, §15 has init.md role lock
- [ ] `glossary.md` has tfw-init term
- [ ] Antigravity README lists tfw-init.md in copy + sync instructions
- [ ] `PROJECT_CONFIG.yaml` has `init:` in `tfw.workflows`
- [ ] `KNOWLEDGE.md` has D18 + TFW-13 in key artifacts

## 6. Риски фазы

| Риск | Mitigation |
|------|------------|
| Adapter docs из git history могут отличаться от последней версии | Использовать текст из TS Step 1 (уже адаптирован) |
| conventions.md §15 Role Lock для init нетипичный (RES + RF + config files) | Init уникален — он создаёт проект. Permitted artifacts шире чем у других workflows |

---

*TS — TFW-13 / Phase B: Adapter Docs + References Cleanup | 2026-03-30*
