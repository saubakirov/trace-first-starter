# TS — TFW-13 / Phase A: Init Workflow + Slash Command

> **Дата**: 2026-03-30
> **Автор**: Coordinator (AI)
> **Статус**: 🟡 TS — Ожидает апрува
> **Parent HL**: [HL-TFW-13](HL-TFW-13__tfw_init_workflow.md)
> **Research**: [RES__TFW-13](RES__TFW-13__tfw_init_workflow.md)

---

## 1. Цель

Создать `tfw-init` — AI-first workflow для инициализации TFW в любом проекте. Workflow заменяет ручной `init.md`. Включает слэш-команду `/tfw-init` для Claude Code и Antigravity. Старый `init.md` заменяется указателем на workflow.

## 2. Scope

### In Scope
- Workflow `.tfw/workflows/init.md` — 5 фаз (Discover, Interview+Mini-Setup, Knowledge, Full Setup, Verify)
- Слэш-команда `/tfw-init` для Claude Code и Antigravity
- Обновление `CLAUDE.md` и `CLAUDE.md.template` (добавить /tfw-init в таблицу)
- Замена старого `.tfw/init.md` указателем на workflow

### Out of Scope
- Перенос "How to Write a New Adapter" в `.tfw/adapters/README.md` — Phase B
- Обновление conventions.md, glossary.md, KNOWLEDGE.md — Phase B
- Обновление PROJECT_CONFIG.yaml (workflows section) — Phase B

## 3. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/workflows/init.md` | CREATE | Init workflow: 5 фаз, role lock, tutorial mode |
| `.claude/commands/tfw-init.md` | CREATE | Claude Code slash command |
| `.agent/workflows/tfw-init.md` | CREATE | Antigravity adapter copy |
| `CLAUDE.md` | MODIFY | Добавить `/tfw-init` в таблицу slash commands |
| `.tfw/adapters/claude-code/CLAUDE.md.template` | MODIFY | Добавить `/tfw-init` в шаблон |
| `.tfw/init.md` | MODIFY | Заменить содержимое указателем на workflow |

**Бюджет:** 3 новых файла, 3 модификации. Лимиты — см. `tfw.scope_budgets` в `.tfw/PROJECT_CONFIG.yaml`.

## 4. Детальные шаги

### Step 1: Создать `.tfw/workflows/init.md`

Workflow с YAML frontmatter. Role Lock: **Coordinator**. Структура:

```markdown
---
description: TFW Init — initialize TFW in a new project, guided by AI agent
---

# TFW Init — Project Initialization

> **Role:** Coordinator
> **Output:** Configured TFW project with {PREFIX}-1 as first task
> **When to use:** Once, when adding TFW to a project for the first time

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: creating project files (CONFIG, AGENTS.md, README Task Board, adapter),
> calling /tfw-research, writing RES/RF for {PREFIX}-1.
> Forbidden: writing code unrelated to TFW setup.

## Tutorial Mode

At the start, ask the user:
"Is this your first time using TFW? I can explain each step as we go."
If yes — add brief explanations at each phase.
If no — proceed efficiently, skip explanations.

## Phase 1: Discover

Read the project to understand what exists:
- Root files: README.md, package.json, pyproject.toml, go.mod, Cargo.toml, etc.
- Directory structure: src/, lib/, tests/, docs/
- Build/CI config: Makefile, Dockerfile, .github/workflows/, CI files
- Existing conventions: .eslintrc, ruff.toml, .editorconfig
- README content: project description, architecture notes

Present findings to the user:
"I found: {stack}, {structure}, {build tools}. Is this accurate?
Anything I'm missing?"

## Phase 2: Interview + Mini-Setup

### Interview
Ask the user (max 3 questions per batch):

Batch 1 — Identity:
- "What task prefix do you want? (e.g., PROJ, APP, your abbreviation)"
- "What are your build/test/lint commands?"
- "Which AI tool are you using? (Claude Code / Cursor / Antigravity / multiple)"

Batch 2 — Context (if needed):
- "Any specific conventions I should know about? (naming, branching, etc.)"
- "Is this a greenfield or brownfield project?"

### Mini-Setup
After interview, create the skeleton:
1. Fill `.tfw/PROJECT_CONFIG.yaml` with discovered + interview data
2. Create `tasks/` directory
3. Create Task Board in README.md (or append if README exists)
4. Register `{PREFIX}-1: TFW Init` as first task with status 🔬 RES
5. Create `tasks/{PREFIX}-1__tfw_init/` folder

[Tutorial: "I've created the Task Board — this is where all tasks live.
{PREFIX}-1 is this initialization itself. You'll see it progress through
statuses as we work."]

## Phase 3: Knowledge

Announce to the user:
"Now I'll run a RESEARCH session to study your project in depth.
This is the /tfw-research workflow — it helps uncover important details
before we finalize the setup."

Run `/tfw-research` formally within {PREFIX}-1:
- Mode: Standalone (the task already exists)
- RES file: `tasks/{PREFIX}-1__tfw_init/RES__{PREFIX}-1__tfw_init.md`
- Focus: architecture, key decisions, dependencies, domain terms,
  tech debt, conventions not covered in interview

After RESEARCH completes, use findings to inform Phase 4.

[Tutorial: "RESEARCH is a stage where I study the project and ask
pointed questions. It produces a RES file — a record of what we found.
You'll use /tfw-research for your own tasks too."]

## Phase 4: Full Setup

Create/update all TFW files using knowledge from Phases 1-3:

1. **AGENTS.md** — role description adapted to project context
2. **KNOWLEDGE.md** — from `.tfw/templates/KNOWLEDGE.md`, filled with
   Phase 3 findings (architecture, decisions, tech stack)
3. **TECH_DEBT.md** — empty or with initial entries if found
4. **Adapter files** — based on user's tool choice:
   - Claude Code: copy CLAUDE.md.template → CLAUDE.md, fill in project values
   - Cursor: copy tfw.mdc.template → .cursor/rules/tfw.mdc
   - Antigravity: copy rules + workflows to .agent/
5. **Update PROJECT_CONFIG.yaml** — finalize all values
6. **Update Task Board** — {PREFIX}-1 status to 🟢 RF

[Tutorial: "I'm creating the project files now. AGENTS.md tells AI agents
how to behave in your project. KNOWLEDGE.md captures what I learned about
your architecture. The adapter connects your AI tool to TFW."]

## Phase 5: Verify

Run through checklist (present to user):

- [ ] `.tfw/` directory exists with all core files
- [ ] `.tfw/PROJECT_CONFIG.yaml` has correct project values
- [ ] Tool adapter is in place and configured
- [ ] Root files exist: README.md (with Task Board), AGENTS.md
- [ ] `tasks/` directory exists with {PREFIX}-1
- [ ] KNOWLEDGE.md created (or consciously skipped for greenfield)
- [ ] {PREFIX}-1 has RES file from RESEARCH
- [ ] `tfw.version` in PROJECT_CONFIG matches `.tfw/VERSION`

Write RF for {PREFIX}-1:
- List all created/modified files
- Key decisions from interview
- RESEARCH findings summary
- Verification results

Close {PREFIX}-1 as ✅ DONE on Task Board.

[Tutorial: "That's it! TFW is set up. Your next step: run /tfw-plan
to create your first real task. The cycle is: plan → research (optional)
→ spec → execute → review. Each step produces trace files so any AI agent
can pick up where you left off."]

## Anti-patterns

- Agent skips Interview and fills CONFIG with guesses
- Agent skips Knowledge phase without asking user
- Agent creates adapter for wrong tool
- Agent doesn't register {PREFIX}-1 on Task Board
- Agent doesn't explain what it's doing (when tutorial mode is on)
- Agent runs full init on a project that already has .tfw/ configured
  (should detect and warn)
```

### Step 2: Создать `.claude/commands/tfw-init.md`

```markdown
# TFW Init — Project Initialization

You are now running the **TFW Init** workflow.

## Role Lock

**🔒 COORDINATOR** — you create TFW project files, run RESEARCH,
and guide the user through initialization.

## Critical

This is likely the user's first interaction with TFW.
Ask if they want tutorial mode. Be helpful and explanatory.

## Instructions

1. Read and follow: `.tfw/workflows/init.md`

2. Execute 5 phases:
   - **Discover** — read the project, present findings
   - **Interview + Mini-Setup** — ask questions, create skeleton
   - **Knowledge** — run `/tfw-research` formally
   - **Full Setup** — create all TFW files
   - **Verify** — checklist, write RF, close {PREFIX}-1

## User input

$ARGUMENTS
```

### Step 3: Создать `.agent/workflows/tfw-init.md`

Копия `.claude/commands/tfw-init.md` с YAML frontmatter:
```yaml
---
description: TFW Init — initialize TFW in a new project, guided by AI agent
---
```
Остальное содержимое идентично Step 2.

### Step 4: Обновить `CLAUDE.md`

Добавить строку в таблицу Slash Commands:
```
| `/tfw-init` | `.tfw/workflows/init.md` | Coordinator | Initialize TFW in a project — discover, interview, setup |
```

### Step 5: Обновить `.tfw/adapters/claude-code/CLAUDE.md.template`

Добавить `/tfw-init` в таблицу slash commands шаблона (аналогично Step 4).

### Step 6: Заменить `.tfw/init.md`

Заменить содержимое старого init.md кратким указателем:

```markdown
# TFW — Initialization

> This file is a pointer. The full init process is in the workflow.

## AI-Assisted Init (recommended)

Run `/tfw-init` — the AI agent will guide you through setup interactively.

See `.tfw/workflows/init.md` for the full workflow.

## Manual Init (without AI)

If you're setting up without an AI agent:

1. Copy `.tfw/` to your project
2. Edit `.tfw/PROJECT_CONFIG.yaml` — set project name, task prefix, build commands
3. Choose adapter: see `.tfw/adapters/` for your tool
4. Create root files: AGENTS.md, README.md (with Task Board), TECH_DEBT.md
5. Create `tasks/` directory
6. Start with `/tfw-plan` for your first task
```

## 5. Acceptance Criteria

- [ ] `.tfw/workflows/init.md` exists with 5 phases, role lock, tutorial mode, anti-patterns
- [ ] `.claude/commands/tfw-init.md` exists with role lock and reference to workflow
- [ ] `.agent/workflows/tfw-init.md` exists (Antigravity copy)
- [ ] `CLAUDE.md` contains `/tfw-init` in slash commands table
- [ ] `CLAUDE.md.template` contains `/tfw-init` in slash commands table
- [ ] Old `.tfw/init.md` replaced with pointer (≤30 lines)
- [ ] Workflow references `/tfw-research` formally in Phase 3
- [ ] Workflow creates `{PREFIX}-1` as first task in Phase 2

## 6. Риски фазы

| Риск | Mitigation |
|------|------------|
| Workflow >200 строк | Tutorial text = conditional, keep phases concise |
| Конфликт naming: `.tfw/init.md` (pointer) vs `.tfw/workflows/init.md` (workflow) | Pointer clearly references workflow; different paths |

---

*TS — TFW-13 / Phase A: Init Workflow + Slash Command | 2026-03-30*
