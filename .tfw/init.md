# TFW v3 — Quick Start

Initialize Trace-First Workflow v3 in a new project.

## Prerequisites

- A project directory (existing or new)
- A development tool: Claude Code, Cursor, Antigravity, or plain chat

## Step 1: Copy `.tfw/`

Copy the entire `.tfw/` directory to your project root:

```bash
cp -r /path/to/tfw-source/.tfw/ /path/to/your-project/.tfw/
```

## Step 2: Configure

Edit `.tfw/PROJECT_CONFIG.yaml`:

```yaml
project:
  name: your-project
  repo: user/your-project
  branch: main

tfw:
  task_prefix: PROJ          # Short prefix for task IDs
  initial_seq: 1
  templates:                  # Keep as-is
    hl: .tfw/templates/HL.md
    ts: .tfw/templates/TS.md
    rf: .tfw/templates/RF.md
    onb: .tfw/templates/ONB.md
    review: .tfw/templates/REVIEW.md

build:
  lint: your-lint-command     # ruff check ., eslint ., flutter analyze
  test: your-test-command     # pytest, npm test, flutter test
  verify: your-verify-cmd    # python -c 'import main', flutter build apk --debug
```

## Step 3: Choose Tool Adapter

### Claude Code

```bash
cp .tfw/adapters/claude-code/CLAUDE.md.template CLAUDE.md
```
Edit `CLAUDE.md`: fill in project name, stack, owner, code standards.

### Cursor

```bash
mkdir -p .cursor/rules
cp .tfw/adapters/cursor/tfw.mdc.template .cursor/rules/tfw.mdc
```

### Antigravity

```bash
mkdir -p .agent/rules .agent/workflows
```

**Rules** — copy and **adapt for your project**:

```bash
# TFW reference rule (use as-is)
cp .tfw/adapters/antigravity/tfw-rules.md.template .agent/rules/tfw.md

# Agent identity — adapt role description, allowed stages, project-specific conduct
cp AGENTS.md .agent/rules/agents.md

# Conventions — adapt naming, stack conventions, lint/test commands for your project
cp .tfw/conventions.md .agent/rules/conventions.md

# Glossary — add project-specific terms
cp .tfw/glossary.md .agent/rules/glossary.md
```

> ⚠️ `conventions.md` and `glossary.md` in `.tfw/` are **starter templates**.
> The copies in `.agent/rules/` are the **project-specific versions** that the agent reads.
> You MUST review and adapt them: naming conventions, stack, build commands, domain terms.

**Workflows** — copy as-is:

```bash
cp .tfw/workflows/plan.md .agent/workflows/tfw-plan.md
cp .tfw/workflows/handoff.md .agent/workflows/tfw-handoff.md
cp .tfw/workflows/resume.md .agent/workflows/tfw-resume.md
cp .tfw/workflows/tfw-task.md .agent/workflows/tfw-task.md
```

See `.tfw/adapters/antigravity/README.md` for details.

### Plain Chat

No adapter needed. Reference `.tfw/README.md` directly in your chat.

## Step 4: Create Root Files

```bash
# AGENTS.md — AI role and mission for your project
# TASK.md — project scope, DoD, risks
# STEPS.md — empty progress journal
# README.md — project description with Task Board:

cat >> README.md << 'EOF'

## Task Board

| ID | Task | Status | HL | TS | ONB | RF | REV |
|----|------|--------|----|----| --- |----| --- |

> Statuses: ⬜ TODO → 🔵 HL → 🟡 TS → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE | ❌ BLOCKED
EOF

# TECH_DEBT.md — empty tech debt registry
mkdir -p tasks/
```

> **⚠️ Do NOT add these files to `.gitignore`:**
> `STEPS.md`, `TECH_DEBT.md`, `TASK.md`, `AGENTS.md`, and the `tasks/` directory
> are **core trace artifacts** and MUST be version-controlled.
> Without them in git, the entire trace history is lost.

## Step 5: Start Working

Follow `.tfw/workflows/plan.md` to create your first task.

## Verification

- [ ] `.tfw/` directory exists with all files
- [ ] `.tfw/PROJECT_CONFIG.yaml` has correct project values
- [ ] Tool adapter is in place (CLAUDE.md / .cursor/rules/ / .agent/)
- [ ] `.agent/rules/conventions.md` adapted for project (naming, stack, build commands)
- [ ] `.agent/rules/glossary.md` adapted for project (domain terms added)
- [ ] Root files exist: README.md, AGENTS.md, TASK.md, STEPS.md
- [ ] `tasks/` directory exists

---

## How to Write a New Adapter

An adapter is a bridge between a development tool and `.tfw/`. Requirements:

1. **Entry point** — the file your tool auto-loads (e.g., CLAUDE.md, .cursor/rules/*.mdc)
2. **References `.tfw/`** — points to conventions, glossary, workflows. Never duplicates them.
3. **Minimal** — ≤35 lines of content. Project-specific sections only.
4. **Contains**:
   - Reference to `.tfw/README.md` (philosophy)
   - Reference to `.tfw/conventions.md` (rules)
   - Context loading order
   - Reference to `.tfw/workflows/` (plan, handoff, resume)
   - Conduct rules (no sycophancy, no placeholders, summary discipline)

### Template structure

```markdown
# TFW v3
Read `.tfw/README.md` for philosophy. Follow `.tfw/conventions.md`.
Workflows: `.tfw/workflows/` (plan, handoff, resume).
Context: AGENTS.md → STEPS.md → TASK.md → .tfw/conventions.md → .tfw/glossary.md
Rules: no sycophancy, no placeholders, summary discipline, user's language.
```

Place adapter template in `.tfw/adapters/{tool-name}/` with a README explaining setup.
