# TFW — Claude Code Adapter

<!-- TFW:CLAUDE:START -->
## TFW (Trace-First Workflow)

This project follows Trace-First Workflow. The tool-agnostic core lives in `.tfw/`.
Version: see `.tfw/VERSION`.

### Command Routing

Root instructions are already active; do not reload them. For `/tfw-*`, open the matching
`.claude/commands/tfw-*.md` copy and its canonical workflow completely. The workflow's Read
Contract selects task state, addressed shared ranges, templates, and knowledge inputs.

### Activation and routing

Before Plan Step 5, report `provision · addressed send · wait/readback · title/readback` from the
mechanisms exposed in the current Claude Code session, classifying each as `native`,
`owner-assisted`, or `unavailable`. Starting one session does not provision distinct addressable TFW
role units. Without an exposed distinct-unit creator and exact recipient send, provision and
addressed send are owner-assisted; resume/agent or title options count as native only when the
current surface also exposes their exact readback. Never borrow Codex or receipt capabilities.

A slash command activates work only when it names the exact `/tfw-*` skill, task/phase and
owner-direct, delegated or continuation source. A session, role prompt, briefing, wait result or
title is not activation. Read and validate the complete task routing spine before material work;
report every status change to `coordinator_route`. Under `tfw-gates-only`, role units communicate
materially only with their own Coordinator, never peers, owner or GATEWAY. Record actual producer
session/address, parent route, activation/dispatch source and immutable authority in role artifacts.
Never open or resume another TFW role session to inspect its chat, reasoning, tool output, terminal or
unreturned work. Silence routes through wait/status or one addressed status request; unavailable
monitoring is disclosed rather than replaced by session inspection.
Iterative dialogue requires a separately addressable GATEWAY session and exact immutable grant.

### Slash Commands

| Command | Workflow | Role | Purpose |
|---------|----------|------|---------|
| `/tfw-plan` | `.tfw/workflows/plan.md` | Coordinator | Research, write HL, freeze the contract, RESEARCH gate, route amendments, write TS |
| `/tfw-research` | `.tfw/workflows/research/base.md` | Researcher | Structured investigation — pipeline or standalone |
| `/tfw-handoff` | `.tfw/workflows/handoff.md` | Executor | ONB, implement, RF |
| `/tfw-review` | `.tfw/workflows/review.md` | Reviewer | Review RF against checklist, Purpose Check against the contract baseline, write REVIEW |
| `/tfw-docs` | `.tfw/workflows/docs.md` | Coordinator | Update KNOWLEDGE.md after REVIEW |
| `/tfw-knowledge` | `.tfw/workflows/knowledge.md` | Coordinator | Consolidate fact candidates into verified project knowledge |
| `/tfw-release` | `.tfw/workflows/release.md` | Coordinator | Version bump, CHANGELOG, tag |
| `/tfw-init` | `.tfw/workflows/init.md` | Coordinator | Initialize TFW in a project — discover, interview, setup |
| `/tfw-update` | `.tfw/workflows/update.md` | Coordinator | Fetch upstream, compare versions, sync adapters |
| `/tfw-config` | `.tfw/workflows/config.md` | Coordinator | Interactive config change, propagate to all inline values |

### Discovery References (not preload)

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
