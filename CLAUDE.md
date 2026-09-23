# TFW — Claude Code Adapter

<!-- TFW:CLAUDE:START -->
## TFW (Trace-First Workflow)

This project follows Trace-First Workflow. The tool-agnostic core lives in `.tfw/`.
Version: see `.tfw/VERSION`.

### Command Routing

Root instructions are already active; do not reload them. For `/tfw-*`, open the matching
`.claude/commands/tfw-*.md` copy and its canonical workflow completely. The workflow's Read
Contract selects task state, addressed shared ranges, templates, and knowledge inputs.
At new-task Plan entry, after identifying the request and active platform and completing the
workflow's task-control and shared-rule reads, read exactly
`.tfw/adapters/claude-code/coordinator.md` for the owner-facing startup card and initial mode choice.
At Plan Step 5 validate that choice and current capability; re-read this selected profile only
when the active surface or relevant capability materially changes. GATEWAY uses the same profile
at its corresponding new-work selection gate. Do not preload other profiles or the tooling
manifest, and do not load this profile for every role command. A missing or ambiguous selected
pointer refuses a provider-specific offer and is reported without guessing.

### Activation and routing

At new-task entry, report `provision · addressed send · wait/readback · title/readback` from the
mechanisms exposed in the current Claude Code session, classifying each as `native`,
`owner-assisted`, or `unavailable`. Starting one session does not provision distinct addressable TFW
role units. Without an exposed distinct-unit creator and exact recipient send, provision and
addressed send are owner-assisted; resume/agent or title options count as native only when the
current surface also exposes their exact readback. Never borrow Codex or receipt capabilities.

A slash command activates work only when its exact `/tfw-*` skill, task/phase and owner-direct,
delegated or continuation source resolve. The command-only first message names the command and
task/phase; native origin and task files supply the source. A session, role prompt, briefing, wait result or
title is not activation. Read and validate the complete task routing spine before material work;
report every status change to `coordinator_route` under native-gates reporting. Under
`tfw-gates-only`, role units communicate
materially only with their own Coordinator, never peers, owner or GATEWAY. Record actual producer
session/address, parent route, activation/dispatch source and immutable authority in role artifacts.
Never open or resume another TFW role session, or inspect raw provider-wide state, session logs or
unrelated task/chat history, to read its chat, reasoning, tool output, terminal or unreturned work.
Monitor only through addressed TFW messages and exposed event/status/wait mechanisms. After an
unchanged signal, back off; never poll on a short fixed timer or narrate unchanged state. A suspected
stall permits one addressed status request, then is reported as unavailable or blocked. Under
`tfw-gates-only`, do not harvest or relay another unit's unreturned reasoning, suspicions, prose or
preferred solution.
Iterative dialogue requires an exact immutable two-peer grant independent of GATEWAY selection.
Only an explicit human `owner-transfer` choice disables inter-agent sends; manual chat creation
alone does not. A new role's first message is only `/tfw-* <task[/phase]>`.

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
