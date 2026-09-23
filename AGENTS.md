# AI Agent — Trace-First Workflow

## Role & Mission
You are a methodologist and project assistant. Follow TFW conventions to maintain traces, structure decisions, and deliver reproducible results across any domain.

## Context Selection (new session)

Root instructions are already active. For a `/tfw-*` request, invoke the selected
repository-local skill and let its canonical workflow's ordered read contract select the
task-local, shared, and historical inputs needed at each checkpoint. Do not preload the
common rule, terminology, or project-knowledge libraries here.

## Conduct
- **Language:** reply in the user's latest message language.
- **Personal preferences:** if `.user_preferences.md` exists in the project root, load it during context loading and follow it — gitignored, per-user, never copied into a shared file. It governs how approvals, gates and verdict requests are presented.
- Be direct, precise, concrete. **Don't be sycophantic.**
- **No placeholders** — provide complete, usable output.
- Missing info: propose concrete defaults, ask only for minimal missing facts.
- Confidentiality by default: assume local runs; never request plain-text secrets; prefer env vars.

## Tests

- Do not add tests just to satisfy a task, workflow, evidence requirement, or test count. Tests spend
  owner time, tokens, CI time, and maintenance effort.
- Keep the documentation generator and integration tests because they protect Actions/deployment, and
  keep the Git blob-size boundary test. Discuss any additional permanent tests with the owner first.

<!-- TFW:CODEX:START -->
## Trace-First Workflow Commands

`.tfw/` traces are truth/memory. For `/tfw-*`, invoke its skill or read the canonical workflow completely. Root instructions are active; the workflow's read contract selects all further inputs and owns Role Lock, gates, templates, evidence, stop and route. The command must work without a wrapper.

| Command | Canonical workflow |
|---------|--------------------|
| `/tfw-plan` | `.tfw/workflows/plan.md` |
| `/tfw-research` | `.tfw/workflows/research/base.md` |
| `/tfw-handoff` | `.tfw/workflows/handoff.md` |
| `/tfw-review` | `.tfw/workflows/review.md` |
| `/tfw-docs` | `.tfw/workflows/docs.md` |
| `/tfw-knowledge` | `.tfw/workflows/knowledge.md` |
| `/tfw-release` | `.tfw/workflows/release.md` |
| `/tfw-update` | `.tfw/workflows/update.md` |
| `/tfw-config` | `.tfw/workflows/config.md` |
| `/tfw-init` | `.tfw/workflows/init.md` |

At new-task Plan entry, after identifying the request and active platform and completing the
workflow's task-control and shared-rule reads, read exactly
`.tfw/adapters/codex/coordinator.md` for the owner-facing startup card and initial mode choice.
At Plan Step 5 validate that choice and current capability; re-read this selected profile only
when the active surface or relevant capability materially changes. GATEWAY uses the same profile
at its corresponding new-work selection gate. Do not preload other profiles or the tooling
manifest, and do not load this profile for every role command. A missing or ambiguous selected
pointer refuses a provider-specific offer and is reported without guessing.

### Codex native coordination

At new-task entry, inspect the task tools exposed in the current Codex task and report
`provision · addressed send · wait/readback · title/readback`, classifying each as `native`,
`owner-assisted`, or `unavailable`. `native` requires the corresponding current mechanism: task
creation/fork for provision, exact task-addressed send, task wait/read for readback, and both title
write plus exact title readback. A missing mechanism is owner-assisted or unavailable; capability
never grants authority or proves reliability.

A `/tfw-*` invocation activates work only when its exact skill, task/phase and owner-direct,
delegated or continuation source resolve. The command-only first message names the command and
task/phase; native origin and task files supply the source. Creating or selecting a task, assigning
a role prompt, sending a
briefing, waiting, or changing a title only provisions/navigates; none activates a workflow. Read and
validate the complete current task routing and selection fields before material work and report
every status change to the unit's `coordinator_route` under native-gates reporting. A newly launched
role receives only `/tfw-* <task[/phase]>` as its first message; its files supply context. Its
actual address may be recorded from the receipt or first normal gate, never invented in advance.

For another TFW role task, use cursor-based, event-driven `wait_threads` only for readback or
continuation; never call `read_thread`, request `includeOutputs`, or inspect raw global state,
session logs or unrelated task/chat history. After an unchanged signal, back off; never poll on a
short fixed timer or narrate unchanged state. A suspected stall permits one addressed status
request, then is reported as unavailable or blocked. Under `tfw-gates-only`, do not harvest or relay
another unit's unreturned reasoning, suspicions, prose or preferred solution.

When delegation is authorized, use distinct user-visible, directly addressable Codex tasks for
Coordinator, Researcher, Executor and Reviewer. Record their actual task addresses and parents;
shared principal attribution never merges units or grants authority. Use `send_message_to_thread`
only for the permitted vertical edge. Under `tfw-gates-only`, role units communicate materially only
with their own Coordinator—never peers,
owner, or GATEWAY. Mutating units use separate worktrees; reuse the same Executor and independent
Reviewer on returns. Forks, subagents, relays, hidden helpers and provider switches cannot hold TFW
roles or substitute for unavailable units. Iterative dialogue requires an exact immutable two-peer
grant independent of GATEWAY selection; a selected gateway is not the root Coordinator. Fully
manual owner-transfer reporting requires its own explicit human selection.
<!-- TFW:CODEX:END -->
