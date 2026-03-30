# TFW 0.5 — Claude Code Adapter

## TFW (Trace-First Workflow)

This project follows Trace-First Workflow 0.5. The tool-agnostic core lives in `.tfw/`.

### Context Loading (new session, strict order)

1. `AGENTS.md` — AI role and mission
2. `.tfw/conventions.md` — formal rules, naming, scope budgets
3. `.tfw/glossary.md` — terminology
4. `KNOWLEDGE.md` (if exists) — architecture, decisions
5. Project Task Board (`README.md`) — status of all tasks
6. Relevant HL/TS/RF files for the current task

### Slash Commands

| Command | Workflow | Role | Purpose |
|---------|----------|------|---------|
| `/tfw-plan` | `.tfw/workflows/plan.md` | Coordinator | Research, write HL, RESEARCH gate, scope decision, write TS |
| `/tfw-research` | `.tfw/workflows/research.md` | Coordinator | Structured investigation — pipeline or standalone |
| `/tfw-handoff` | `.tfw/workflows/handoff.md` | Executor | ONB, implement, RF |
| `/tfw-review` | `.tfw/workflows/review.md` | Reviewer | Review RF against checklist, write REVIEW |
| `/tfw-resume` | `.tfw/workflows/resume.md` | Coordinator | Status matrix for multi-phase task, decide next phase |
| `/tfw-docs` | `.tfw/workflows/docs.md` | Coordinator | Update KNOWLEDGE.md and TECH_DEBT.md after REVIEW |
| `/tfw-task` | Meta-workflow | Coordinator | Full lifecycle: plan + handoff with hard stop between them |
| `/tfw-release` | `.tfw/workflows/release.md` | Coordinator | Version bump, CHANGELOG, tag |
| `/tfw-update` | `.tfw/workflows/update.md` | Coordinator | Fetch upstream, compare versions, sync adapters |

### Conduct

- **No sycophancy**: Be direct, precise, concrete. Flag risks. Disagree when evidence supports it.
- **No placeholders**: Provide complete, usable output. If incomplete, state what is missing.
- **Language**: Reply in the user's latest message language.
- **Safety**: Secrets via env vars only. Never claim something was "run" outside the session.

### Execution Modes

- **CL (Chat Loop)** — default. AI proposes, user approves/executes.
- **AG (Autonomous)** — explicit request only. AI works within approved TS scope.

### Key References

- `.tfw/README.md` — philosophy, thesis, lifecycle
- `.tfw/conventions.md` — all formal rules
- `.tfw/templates/` — canonical artifact templates (HL, TS, RF, ONB, RES, REVIEW, KNOWLEDGE)
- `.tfw/CHANGELOG.md` — version history
- `.tfw/PROJECT_CONFIG.yaml` — project parameters (task prefix, build commands)
