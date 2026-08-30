# TFW — Claude Code Adapter

<!-- TFW:CLAUDE:START -->
## TFW (Trace-First Workflow)

This project follows Trace-First Workflow. The tool-agnostic core lives in `.tfw/`.
Version: see `.tfw/VERSION`.

### Context Loading (new session, strict order)

1. `AGENTS.md` — AI role and mission
2. `.tfw/conventions.md` — formal rules, naming, scope budgets
3. `.tfw/glossary.md` — terminology
4. `KNOWLEDGE.md` (if exists) — architecture, decisions
5. The selected task's `status.md` — its live state, and the only authority for it
6. Relevant HL/TS/RF files for the current task

### Slash Commands

| Command | Workflow | Role | Purpose |
|---------|----------|------|---------|
| `/tfw-plan` | `.tfw/workflows/plan.md` | Coordinator | Research, write HL, freeze the contract, RESEARCH gate, route amendments, write TS |
| `/tfw-research` | `.tfw/workflows/research/base.md` | Coordinator | Structured investigation — pipeline or standalone |
| `/tfw-handoff` | `.tfw/workflows/handoff.md` | Executor | ONB, implement, RF |
| `/tfw-review` | `.tfw/workflows/review.md` | Reviewer | Review RF against checklist, Purpose Check against the contract baseline, write REVIEW |
| `/tfw-resume` | `.tfw/workflows/resume.md` | Coordinator | Status matrix for multi-phase task, decide next phase |
| `/tfw-docs` | `.tfw/workflows/docs.md` | Coordinator | Update KNOWLEDGE.md and TECH_DEBT.md after REVIEW |
| `/tfw-knowledge` | `.tfw/workflows/knowledge.md` | Coordinator | Consolidate fact candidates into verified project knowledge |
| `/tfw-task` | Meta-workflow | Coordinator | Full lifecycle: plan + handoff with hard stop between them |
| `/tfw-release` | `.tfw/workflows/release.md` | Coordinator | Version bump, CHANGELOG, tag |
| `/tfw-init` | `.tfw/workflows/init.md` | Coordinator | Initialize TFW in a project — discover, interview, setup |
| `/tfw-update` | `.tfw/workflows/update.md` | Coordinator | Fetch upstream, compare versions, sync adapters |
| `/tfw-config` | `.tfw/workflows/config.md` | Coordinator | Interactive config change, propagate to all inline values |

### Key References

- `.tfw/README.md` — philosophy, thesis, lifecycle
- `.tfw/conventions.md` — all formal rules
- `.tfw/templates/` — canonical artifact templates (see `tfw.templates` in `.tfw/project_config.yaml`)
- `.tfw/CHANGELOG.md` — version history
- `.tfw/project_config.yaml` — project parameters (task prefix, build commands)
<!-- TFW:CLAUDE:END -->

### Conduct

- **No sycophancy**: Be direct, precise, concrete. Flag risks. Disagree when evidence supports it.
- **No placeholders**: Provide complete, usable output. If incomplete, state what is missing.
- **Language**: Reply in the user's latest message language.
- **Personal preferences**: if `.user_preferences.md` exists in the project root, load it as part of context loading and follow it. It is gitignored and per-user — never copy its content into a shared file (constraint F1). It governs how gates, approvals and verdict requests are presented.
- **Safety**: Secrets via env vars only. Never claim something was "run" outside the session.

### Execution Modes

- **CL (Chat Loop)** — default. AI proposes, user approves/executes.
- **AG (Autonomous)** — explicit request only. AI works within approved TS scope.
