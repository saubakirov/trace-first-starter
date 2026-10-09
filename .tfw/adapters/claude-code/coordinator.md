# Claude Code Coordinator profile

Selected by `CLAUDE.md` at new-task entry and Plan Step 5 or a changed capability gate. Read this one profile, not every provider profile or the tooling manifest. Canonical TFW rules govern authority, role locks, gates and acceptance; this file gives the Claude route and its evidence limits.

## Startup card values on Claude Code

At new-task entry, render one shared startup card from mechanisms actually exposed in this
Claude surface.
Offer the visible full-chat route: the Coordinator creates each separate Coordinator, Researcher,
Executor and independent Reviewer chat itself where a route in Self-created role chats below works;
otherwise the owner may need to click-create each chat, with native addressed gates where current
tools support them. For a really small one-phase task, also
offer the single-phase agent mode below.
Owner-only or bounded delegated activation with `tfw-gates-only` dialogue and native-gates
reporting is the initial operating choice;
owner-transfer requires explicit selection. One-phase work has one task Coordinator and distinct
worker roles. Long work keeps that task Coordinator for strategy, owner decisions and ready-phase
launch while each ready phase has a separate bounded Coordinator, with owner creation clicks when
required. Roles return vertically to their own Coordinator; phase-level results return to the task
Coordinator. Outside the single-phase agent mode below, no subagent substitutes for a visible, directly addressable TFW role unit.

Show role-specific visible titles when the surface can set and read them. Use task-only grouping
when supported; report an unavailable mechanism or required owner action. Do not assume a Codex
Section exists here. On Claude Desktop, use the owner-selected local
checkout, serialize mutation and hold the Executor while an independent Reviewer examines a fixed
reachable Candidate; do not invent a path. The Coordinator selects model and effort separately at
each launch from actual available choices and records rationale outside the first message; report
unobserved effective settings as unknown. Every new role begins with exactly
`/tfw-* <task[/phase]>` after the ID/phase is known, with no briefing or startup card appended.
Name owner clicks, HL/TS and reserved verdicts still owed. Close only after durable vertical
returns, independent acceptance, selected docs/knowledge/changelog effects and safe chat/archive
and checkout disposition. Archive is not disk cleanup.

## Visible full-chat route

At each ready role gate, request the owner click if full-chat creation is owner-assisted. The nonempty initial prompt is exactly `/tfw-* <task[/phase]>`; do not create an empty waiting pool or attach a briefing. A pool is conditional only on a surface that actually permits command-only later activation. A creation receipt or first normal gate may supply transport readiness/address without a compulsory second handshake. Existing chats can use exact addressed sends when exposed; manual creation alone does not select fully manual reporting. Active Researcher, Executor and Reviewer still return native vertical gates to their own Coordinator unless the owner explicitly selected `owner-transfer`. This route cannot claim unattended completion while future owner clicks or reserved decisions remain.

Use one owner-selected local checkout/worktree for visible full chats on Claude Desktop. Serialize repository mutation with one active owner and exact-path commits; preserve foreign work. Hold Executor mutation while the independent Reviewer examines a fixed reachable Candidate. Sequence conflicting phase work in that same checkout. Do not silently move the chain to provider-created isolated trees with a stale base. Archive is recoverable conversation disposition, not disk cleanup; preserve its restoration dependencies or expose the remaining disposal decision.

## Self-created role chats

A task or phase Coordinator that is a watched session may create a full role chat itself at that
role's ready gate, never earlier, through one of the routes below. Each route creates the chat with
the Launch selection applied, makes it visible to the owner, then activates it with a cross-session
message carrying exactly `/tfw-<command> <task[/phase]>` and nothing else; this command-only later
activation is what permits the created chat (Visible full-chat route). The role's reply is its first
return; if it shows that the canonical workflow did not load, stop this launch. Record the address
and title in the dispatch. Later sends and returns use the same messages. Never read a role's chat,
terminal, pane or `.jsonl` log, and resume a role session only to present it. Report `provision`,
`addressed send`, `wait/readback` and `title/readback` from what the first launch shows, never from
a version or platform. A failed step stops only the affected launch: name the cause and use the
owner-click route for it. Corrections go to the existing Executor by message; the Reviewer is always
a newly created unit.

### Desktop route

For a Coordinator that is a Desktop Code session (observed 2026-10-07 on Windows: CLI
2.1.287, Desktop 2.19675.0). Desktop shows a CLI session only after it is presented, and
opens it in the permission mode of its last recorded turn.

1. **Create.** Generate a UUID and run
   `claude -p "Permission mode record. No task action; reply: ok." --session-id <uuid> -n "<Session identity title>" --model <model> --effort <effort> --permission-mode <mode>`.
   This fixed, task-free turn records the launch settings; it is not a dispatch, briefing or
   activation. Auto comes only from this flag or user/policy settings, never project settings; a
   model without auto (observed: Haiku 4.5) silently records the default mode.
2. **Present.** Run `claude --desktop --resume <uuid>` once in a real terminal; it accepts no other
   flags and refuses captured output. Windows:
   `Start-Process -FilePath claude -ArgumentList '--desktop','--resume','<uuid>'`; macOS:
   `script -q /dev/null claude --desktop --resume <uuid>`. Where the CLI refuses `--desktop`
   (documented for macOS and x64 Windows only), name the owner action: open a new Desktop Code session
   in the same folder, type `/resume` and pick that title. Read the title and settings back where the
   surface shows them; a mismatch is an owner action.
3. **Activate and exchange** through Desktop cross-session messages. An approval card the surface
   shows, for example for a model or effort change before reuse, is an owner action.

### Remote Control route

For a Coordinator on a Linux or macOS machine whose account has Remote Control, for example a session
of `claude remote-control`; the owner follows each chat at claude.ai/code, in the Claude app or in
Desktop. One probe observed 2026-10-08 on Xubuntu with `systemd`-managed `claude remote-control`
sessions; needs `tmux`.

1. **Create.** Run
   `tmux -L <slug> new-session -d -s <slug> "claude --remote-control '<Session identity title>' -n <slug> --model <model> --effort <effort> --permission-mode <mode>"`,
   where `<slug>` is an ASCII form of the title and `-L` gives the unit its own tmux server. When the
   Coordinator itself runs under a service manager, start that server outside the Coordinator's unit
   (systemd: prefix `systemd-run --user --scope`) so stopping the Coordinator does not end the role.
   No turn is sent; the chat appears in the owner's Remote Control session list once connected.
   Confirm `<slug>` through `ListAgents` before sending (it may list the unit as `interactive` with
   its tmux pane) and record the ref it shows: names that follow session titles can change, refs do
   not.
2. **Activate and exchange** with `SendMessage` to `<slug>` and `notify_when_idle`. The role returns
   its gates by `SendMessage` to the reply address of the message it received; an idle notice only
   wakes the Coordinator and is not a gate. Never attach to, capture or read the tmux pane.
3. **Close.** After durable returns and the last correction, end the unit with
   `tmux -L <slug> kill-server`; its transcript stays resumable.

## Single-phase agent mode

For a really small one-phase task, such as a small fix or debt item, the owner may choose this mode
instead of full role chats. Offer it only where the current surface can start an agent with exactly
`/tfw-* <task>` and receive its return. The task Coordinator stays the owner's only conversation and
launches each needed role (Researcher, Executor, independent Reviewer) as a distinct agent. Each
agent reads its context from task files, owns its artifact and returns only its TFW gates to the
Coordinator, which does none of their work. The Reviewer is a new agent, never the continued
Executor, and examines a fixed Candidate. This saves owner clicks, not Coordinator context. If the
task outgrows one phase or an agent cannot load its workflow or a required tool, stop that
delegation, name the limit and offer full role chats; never switch modes silently.

## One-phase and successor limits

A one-phase task needs no extra phase Coordinator, but Researcher, Executor and Reviewer still need
distinct full role chats, or distinct agents in the single-phase agent mode, and independent judgment. If a needed chat must be created by the owner,
name that pending action and do not promise unattended completion. A successor task Coordinator
requires a safe checkpoint, exact address and dispatch, reconstruction from current task files,
acknowledgement, then an authorized route switch; the old route remains effective meanwhile.
