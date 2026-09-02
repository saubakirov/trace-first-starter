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
        ├── tfw-knowledge.md           # /tfw-knowledge — consolidate verified facts
        ├── tfw-release.md             # /tfw-release — version bump
        ├── tfw-update.md              # /tfw-update — fetch upstream + sync
        ├── tfw-config.md              # /tfw-config — config change + adapter sync
        └── tfw-init.md                # /tfw-init — initialize TFW in a project
```

## Setup

1. Copy `CLAUDE.md.template` to your project root as `CLAUDE.md`
2. Fill in `{project_name}`, `{stack}`, `{owner}`, and code standards — everything **outside**
   the managed block below is yours
3. Copy the command templates from this repo's `.claude/commands/` into your project's `.claude/commands/`
4. No further configuration needed — Claude Code auto-discovers `CLAUDE.md` and `.claude/commands/`

## The managed block

`CLAUDE.md.template` carries one TFW-managed block, bounded by

```text
<!-- TFW:CLAUDE:START -->
<!-- TFW:CLAUDE:END -->
```

Inside it: the context-loading order, the `/tfw-*` command table and the key references — the
text a release changes. `update.md` Step 6 verifies and replaces **only the region between the
markers**; `cmp` on that region against the template's is the whole check, so a `CLAUDE.md`
hand-edited in three places above and below the block is still synced mechanically.

The marker rule is stated once, in `.tfw/conventions.md` §9, for every marker-bounded block
in every adapter: markers present → replace the text between them; file absent → create it
from this template; file present **without** markers → **report it and leave it untouched**.
The operator inserts the block once, and from then on every sync is mechanical. Appending a
block to a file that already carries an unmarked hand-written TFW section produces two
sections, which is why a first sync never appends.

The framework's own root `CLAUDE.md` carries this block between the same markers, byte-identical
to the template's, and a test checks it as it checks every other installed copy.

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
| `/tfw-knowledge` | `.tfw/workflows/knowledge.md` | Coordinator | `/tfw-knowledge` |
| `/tfw-release` | `.tfw/workflows/release.md` | Coordinator | `/tfw-release` |
| `/tfw-update` | `.tfw/workflows/update.md` | Coordinator | `/tfw-update` |
| `/tfw-config` | `.tfw/workflows/config.md` | Coordinator | `/tfw-config` |
| `/tfw-init` | `.tfw/workflows/init.md` | Coordinator | `/tfw-init` |
