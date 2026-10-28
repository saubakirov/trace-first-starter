---
trigger: always_on
---

# TFW

This project follows Trace-First Workflow. Root instructions are already active; do not
reload them. For `/tfw-*`, invoke the matching repository-local skill. The canonical workflow's Read Contract selects all further inputs.
At new-task Plan entry, after identifying the request and active platform and completing the
workflow's task-control and shared-rule reads, read exactly
`.tfw/adapters/antigravity/coordinator.md` for the owner-facing startup card and initial mode choice.
At Plan Step 5 validate that choice and current capability; re-read this selected profile only
when the active surface or relevant capability materially changes. The task Coordinator uses the selected profile for new work. Do not preload other profiles or the tooling
manifest, and do not load this profile for every role command. A missing or ambiguous selected
pointer refuses a provider-specific offer and is reported without guessing.
For new work, explicitly select `manual`, `visible-agents` or `subagents`; all admit one or
several phases. One owner-facing Coordinator may own phase-local cycles under governing authority;
distinct bounded phase Coordinators remain available. Apply `conventions.md` → `Coordination modes`
for phase routes, independent context, continuation and actual capability limits. Historical GATEWAY/LEAD carriers remain readable,
but a principal, title or host never supplies a route or mandate.

At new-task entry, report `provision · addressed send · wait/readback · title/readback` from the
mechanisms exposed in the current Antigravity surface, classifying each as `native`,
`owner-assisted`, or `unavailable`. Opening one window or conversation does not provision distinct
addressable TFW role units. Provision, addressed send, wait/readback, or title/readback is native
only when that exact mechanism and its observable result are exposed now; otherwise use the honest
owner-assisted or unavailable boundary. Never borrow another provider's capability or old receipt.

A command activates work only when its exact skill, task/phase and owner-direct,
delegated or continuation source resolve. The command-only first message names the command and
task/phase; native origin and task files supply the source. A workspace, role prompt, briefing, wait result or title is not
activation. Read and validate the complete status routing spine before material work and report every
status change to `coordinator_route`. Under `tfw-gates-only`, role units communicate materially only
with their own Coordinator, never peers, owner. Record actual producer surface/address,
parent route, activation/dispatch source and immutable authority. Iterative dialogue requires an
exact immutable two-peer grant independent of task/phase topology. Manual chat creation alone does
not select `owner-transfer`; a new role's first message is only `/tfw-* <task[/phase]>`.
Before sending on the selected strict edges, apply `.tfw/conventions.md` → `Closed message
catalogue`: persist the owned record and required state/event, send only its permitted form, then
read the referenced record/current authority before the dependent act. Research keeps file-owned stage checkpoints and reference returns; owner–task Coordinator discussion stays substantive. The catalogue also owns the
one-time status fallback, delivery/duplicate handling and unavailable route.

Never open or resume another TFW role session, or inspect raw provider-wide state, session logs or
unrelated task/chat history, to read its chat, reasoning, tool output, terminal or unreturned work.
Monitor only through addressed TFW messages and exposed event/status/wait mechanisms. After an
unchanged signal, back off; never poll on a short fixed timer or narrate unchanged state. A suspected
stall permits one addressed status request, then is reported as unavailable or blocked. Under
`tfw-gates-only`, do not harvest or relay another unit's unreturned reasoning, suspicions, prose or
preferred solution.

| Commands | Roles |
|---|---|
| `/tfw-plan`, `/tfw-docs`, `/tfw-knowledge`, `/tfw-release`, `/tfw-update`, `/tfw-config`, `/tfw-init`, `/tfw-economics` | Coordinator |
| `/tfw-research` | Researcher |
| `/tfw-handoff` | Executor |
| `/tfw-review` | Reviewer |

### Coordination Messaging

Under `tfw-gates-only`, role units communicate vertically with their Coordinator via `send_message`:
- Extract the target UUID from `coordinator_route` (strip `antigravity:thread:local:`).
- When the current surface exposes addressed `send_message`, pass that UUID as `Recipient` and
  the catalogue-selected form as `Message` on its strict edges. Research retains its own required
  stage/RES reporting. Verdicts and findings stay in REVIEW.
- Send the required native notifications after their durable records. A missing mechanism follows
  the catalogue's unavailable route; a template or earlier receipt does not prove live capability.

## Rules

- **No sycophancy.** Be direct, precise, concrete.
- **No placeholders.** All code and text must be production-ready.
- **Language.** Reply in the user's latest message language.
- **Working material and comments.** Keep raw output, logs, exports, screenshots and scratch
  scripts in the system temporary directory under `tfw/<task or record ID>/`, never in the project,
  and remove them when your work ends. A comment exists only when it carries value for its file's
  reader or a program reads it, never as a note to agents, deferred work, history or an excuse
  (`conventions.md` → `Working material`, `Comments`).
