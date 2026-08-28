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

**Each slash command is a full copy of its canonical workflow**, placed where Claude Code
expects to find it. `.claude/commands/tfw-plan.md` is byte-identical to
`.tfw/workflows/plan.md`, and the same holds for every row in the mapping below.

Copies **are** the model here, not a shortcut around one. Owner ruling, 2026-08-28: a tool
that reads a directory of commands gets the whole instruction in that directory, and a copy
that is re-synced in the same commit as its source cannot drift unnoticed. Two things make
that true rather than hopeful:

- `update.md` **Step 6** re-copies them, and it lists this adapter explicitly — it did not
  until `2.0.0-dirty.3`, and the omission reached two external projects out of two: the
  listed adapter stayed current and the unlisted one rotted into instructions contradicting
  the payload.
- A test fails if any copy differs from its source, and another fails if the adapter layer
  carries vocabulary a release retired.

> This paragraph read *"Commands never duplicate workflow content — they reference it"* until
> `2.0.0-dirty.3`, beside twelve byte-identical copies that had duplicated it since the
> adapter existed. A rule nobody follows teaches the reader to distrust the ones that are
> true, so the rule was corrected to the practice rather than the practice to the rule.

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
