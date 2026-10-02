# Claude Code Coordinator profile

Selected by `CLAUDE.md` at new-task entry and Plan Step 5 or a changed capability gate. Read this one profile, not every provider profile or the tooling manifest. Canonical TFW rules govern authority, role locks, gates and acceptance; this file gives the Claude route and its evidence limits.

## Startup card values on Claude Code

At new-task entry, render one shared startup card from mechanisms actually exposed in this
Claude surface.
Offer the visible full-chat route: on Claude Desktop the Coordinator creates each separate
Coordinator, Researcher, Executor and independent Reviewer chat itself where the probe in Desktop
session provisioning below passes; otherwise the owner may need to click-create each chat, with
native addressed gates where current tools support them. For a really small one-phase task, also
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

## Desktop session provisioning

On Claude Desktop, a task or phase Coordinator that is a watched Desktop Code session may create a
full role chat itself when its own shell reaches a `claude` CLI whose `claude --help` lists
`--desktop` (observed 2026-10-02 on Windows: CLI 2.1.286–2.1.287, Desktop 2.19675.0; untested on
other systems). Run that probe for the startup card and report its result as `provision` and
`title/readback`; never infer it from a version number. An unwatched Coordinator reports addressed
send and wait/readback as unavailable, because Desktop relays cross-session messages only for a
watched sender.

1. **Provision.** Generate a UUID and run, as a background shell command,
   `claude -p "/tfw-<command> <task[/phase]>" --session-id <uuid> -n "<Session identity title>" --model <model> --effort <effort> --permission-mode <mode>`.
   The `-p` prompt is the command-only first message. Launch selection is applied here and in step 3
   only: `--desktop` accepts no other flags. A `-p` turn never waits for a person; a permission the
   mode and allow rules do not cover is denied and the turn continues or ends unattended, so choose
   them to let the role reach its first gate. Auto comes only from this flag or user/policy settings,
   never project settings; a model without auto (observed: Haiku 4.5) silently starts in default mode.
2. **Return and address.** The `-p` output is the unit's first return; if it shows that the canonical
   workflow did not load, stop this launch. The UUID is the unit's address and the `-n` value its
   title; record both in the dispatch.
3. **Record the mode.** Desktop opens a session in the permission mode of its last recorded turn, and
   a slash-command turn records none, so a session whose last turn is the command opens in manual
   (observed: command only, or a plain turn then the command, opens manual; the command then a plain
   turn opens with the requested mode). When the launch mode is not the default, after the first
   return run exactly one plain turn with the same launch flags:
   `claude -p "Permission mode record. No task action; reply: ok." --resume <uuid> --model <model> --effort <effort> --permission-mode <mode>`.
   This fixed text is transport, not a dispatch, continuation or gate; its output is not a return.
4. **Present.** Run `claude --desktop --resume <uuid>` once, detached in a real console, because it
   refuses captured output (Windows: `Start-Process -FilePath claude -ArgumentList
   '--desktop','--resume','<uuid>'`). Read the title and permission mode back from the Desktop
   session; a mode other than the launch mode is an owner action named at the next gate. Presenting a
   unit this Coordinator has just provisioned is the only resume this route uses; it never opens a
   role session to read its work.
5. **Send and wait.** Later addressed sends and returns use Desktop cross-session messages and the
   replies Desktop delivers back. Do not use that surface to read what a session has been doing, and
   never read session `.jsonl` logs. An approval card the surface shows is an owner action; name it
   at the gate.

A failed probe, a refused presentation or a missing first return stops only the affected launch:
name the cause and use the owner-click route for it. Corrections go to the existing Executor by
message; the Reviewer is always a newly provisioned unit.

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
