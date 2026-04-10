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

If tutorial mode, suggest:
"We recommend reading `.tfw/README.md` — it explains the philosophy behind TFW
and takes about 5 minutes. Everything else in the repo is designed for AI agents,
not for you to read line by line."

### Mini-examples for first-time users

Use these when tutorial mode is on:

**Task prefix** — a short code for your project's task IDs:
- `RND` → tasks are RND-1, RND-2, RND-3...
- `APP` → tasks are APP-1, APP-2, APP-3...

**Task Board** — a table in README.md that tracks all work:

| ID | Task | Status |
|----|------|--------|
| RND-1 | TFW Init | ✅ DONE |
| RND-2 | Sales analysis dashboard | 🟡 TS_DRAFT |
| RND-3 | Client onboarding workflow | ⬜ TODO |

## Phase 1: Discover

Read the project to understand what exists:
- **Purpose and goals:** What is this project about? What problem does it solve?
- **Existing documentation:** README, notes, specs, decision records
- **Structure:** How is the project organized? Folders, files, naming patterns
- **Processes:** How does work happen today? Tools, workflows, conventions
- **People:** Who is involved? Roles, stakeholders, domain experts
- **For software projects specifically:** stack, build/CI config, dependencies, tests

Present findings to the user:
"I found: {purpose}, {structure}, {processes}. Is this accurate?
Anything I'm missing?"

## Phase 2: Interview + Mini-Setup

### Interview
Ask the user (max 3 questions per batch):

Batch 1 — Identity:
- "What task prefix do you want? (e.g., PROJ, APP, your abbreviation)"
- "How do you verify that work is done correctly?" _(for software: build/test/lint commands; for other domains: review process, checklists, approval flow)_
- "Which AI tool are you using? (Claude Code / Cursor / Antigravity / multiple)"
- "What language should I use for artifact content? (default: English)"

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
   - Claude Code: copy `CLAUDE.md.template` → `CLAUDE.md`, fill in project values.
     Copy each `.tfw/workflows/*.md` → `.claude/commands/tfw-{name}.md` (e.g. `plan.md` → `tfw-plan.md`, etc.)
   - Cursor: copy `tfw.mdc.template` → `.cursor/rules/tfw.mdc`
   - Antigravity: copy `.tfw/adapters/antigravity/rules/` → `.agent/rules/`.
     Copy each `.tfw/workflows/*.md` → `.agent/workflows/tfw-{name}.md` (e.g. `plan.md` → `tfw-plan.md`, etc.)
   These are exact copies — slash commands that the agent discovers automatically.
5. **`.user_preferences.md`** — suggest creating a personal preferences file:
   - Template content:
     ```markdown
     # User Preferences

     > ⚠️ PERSONAL FILE — DO NOT COMMIT TO GIT
     > This file stores individual user preferences for AI agents.
     > It is listed in .gitignore by default.
     > To disable: set `tfw.user_preferences: false` in `.tfw/PROJECT_CONFIG.yaml`

     ## Communication
     - Language: {your language}
     - Tone: {direct / friendly / formal}

     ## Work Style
     - {preferences}
     ```
   - Add `.user_preferences.md` to `.gitignore`
6. **Update PROJECT_CONFIG.yaml** — finalize all values
7. **Update Task Board** — {PREFIX}-1 status to 🟢 RF

[Tutorial: "I'm creating the project files now. AGENTS.md tells AI agents
how to behave in your project. KNOWLEDGE.md captures what I learned about
your architecture. The adapter connects your AI tool to TFW."]

## Phase 5: Verify

Run through checklist (present to user):

- [ ] `.tfw/` directory exists with all core files
- [ ] `.tfw/PROJECT_CONFIG.yaml` has correct project values
- [ ] Tool adapter is in place and configured
- [ ] **Slash commands copied** — verify adapter workflows exist:
  - Antigravity: `.agent/workflows/tfw-plan.md`, `tfw-handoff.md`, `tfw-review.md` (+ others)
  - Claude Code: `.claude/commands/tfw-plan.md`, `tfw-handoff.md`, `tfw-review.md` (+ others)
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
