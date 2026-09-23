---
trigger: always_on
---

# TFW

This project follows Trace-First Workflow. Root instructions are already active; do not
reload them. For `/tfw-*`, invoke the matching repository-local skill. The canonical workflow's Read Contract selects all further inputs.
At Plan Step 5, GATEWAY's corresponding capability/selection gate, or a changed capability gate,
read exactly
`.tfw/adapters/antigravity/coordinator.md`; do not preload other profiles or the tooling manifest.
Missing or ambiguous selection is reported without guessing the provider.

Before Plan Step 5, report `provision · addressed send · wait/readback · title/readback` from the
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
with their own Coordinator, never peers, owner or GATEWAY. Record actual producer surface/address,
parent route, activation/dispatch source and immutable authority. Iterative dialogue requires an
exact immutable two-peer grant independent of GATEWAY selection. Manual chat creation alone does
not select `owner-transfer`; a new role's first message is only `/tfw-* <task[/phase]>`.
Never open or resume another TFW role session, or inspect raw provider-wide state, session logs or
unrelated task/chat history, to read its chat, reasoning, tool output, terminal or unreturned work.
Monitor only through addressed TFW messages and exposed event/status/wait mechanisms. After an
unchanged signal, back off; never poll on a short fixed timer or narrate unchanged state. A suspected
stall permits one addressed status request, then is reported as unavailable or blocked. Under
`tfw-gates-only`, do not harvest or relay another unit's unreturned reasoning, suspicions, prose or
preferred solution.

| Commands | Roles |
|---|---|
| `/tfw-plan`, `/tfw-docs`, `/tfw-knowledge`, `/tfw-release`, `/tfw-update`, `/tfw-config`, `/tfw-init` | Coordinator |
| `/tfw-research` | Researcher |
| `/tfw-handoff` | Executor |
| `/tfw-review` | Reviewer |

### Coordination Messaging

Under `tfw-gates-only`, role units communicate vertically with their Coordinator via `send_message`:
- Extract the target UUID from `coordinator_route` (strip `antigravity:thread:local:`).
- Call `send_message(Recipient="<uuid>", Message="...")` to report every gate transition:
  - **Researcher:** report completion of each research iteration and RES artifact delivery.
  - **Executor:** report ONB start, blockers, and RF completion.
  - **Reviewer:** report REV start and REVIEW verdict (APPROVE / REVISE / REJECT).
- Cross-session addressed messaging between active Antigravity threads is fully supported; role units must send formal notifications directly upon completing gate work instead of delegating status delivery to the human owner.

## Rules

- **No sycophancy.** Be direct, precise, concrete.
- **No placeholders.** All code and text must be production-ready.
- **Language.** Reply in the user's latest message language.
