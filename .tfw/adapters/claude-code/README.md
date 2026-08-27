# Claude Code Adapter — Setup Guide

## Structure

```
project-root/
├── CLAUDE.md                          # Auto-loaded by Claude Code (from template)
└── .claude/
    └── commands/
        ├── tfw-plan.md                # /tfw-plan — task inception
        ├── tfw-research.md            # /tfw-research — structured investigation
        ├── tfw-handoff.md             # /tfw-handoff — execution
        ├── tfw-review.md              # /tfw-review — RF review
        ├── tfw-resume.md              # /tfw-resume — multi-phase status
        ├── tfw-docs.md                # /tfw-docs — knowledge update
        ├── tfw-task.md                # /tfw-task — full lifecycle meta-workflow
        ├── tfw-release.md             # /tfw-release — version bump
        └── tfw-update.md              # /tfw-update — fetch upstream + sync
```

## Setup

1. Copy `CLAUDE.md.template` to your project root as `CLAUDE.md`
2. Fill in `{project_name}`, `{stack}`, `{owner}`, and code standards
3. Copy the command templates from this repo's `.claude/commands/` into your project's `.claude/commands/`
4. No further configuration needed — Claude Code auto-discovers `CLAUDE.md` and `.claude/commands/`

## Design Principle

Each slash command is a thin adapter that:
1. Sets the **role lock** (Coordinator, Executor, or Reviewer)
2. Instructs the agent to **load context** in the correct order
3. Points to the **canonical workflow** in `.tfw/workflows/`
4. Passes through `$ARGUMENTS` from the user

The canonical workflows in `.tfw/workflows/` are the single source of truth. Commands never duplicate workflow content — they reference it.

## Command Mapping

| Slash Command | Canonical Workflow | Role | Antigravity Equivalent |
|---------------|-------------------|------|----------------------|
| `/tfw-plan` | `.tfw/workflows/plan.md` | Coordinator | `/tfw-plan` |
| `/tfw-research` | `.tfw/workflows/research/base.md` | Coordinator | `/tfw-research` |
| `/tfw-handoff` | `.tfw/workflows/handoff.md` | Executor | `/tfw-handoff` |
| `/tfw-review` | `.tfw/workflows/review.md` | Reviewer | `/tfw-review` |
| `/tfw-resume` | `.tfw/workflows/resume.md` | Coordinator | `/tfw-resume` |
| `/tfw-docs` | `.tfw/workflows/docs.md` | Coordinator | `/tfw-docs` |
| `/tfw-task` | `plan.md` + `handoff.md` | Coordinator | `/tfw-task` |
| `/tfw-release` | `.tfw/workflows/release.md` | Coordinator | `/tfw-release` |
| `/tfw-update` | `.tfw/workflows/update.md` | Coordinator | `/tfw-update` |
