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
