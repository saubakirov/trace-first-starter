# Gather — "What do we NOT know?"
> **Mindset:** Explorer. Map the independent choices before selecting a capture route.
> **Task / producer:** `TFW_20260928-181352_TEQM`, iteration 1; Researcher `codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243`.
> **Parent Coordinator / return:** `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793`; `tfw-gates-only`, `native-gates`.
> **Authority / selection:** approved HL §4.1 at `36c100b1d6e246fbdb45ec7a2341bb652ca80b7a`; focused mode answer `7e1b376bdd2791f4bc571168a02fa3579528a069`; Briefing approval `94dff95c72dc95327c0b11e1cc149bd8315a8cc6`.
> **Evidence epoch:** primary documentation fetched 2026-09-28; local probes on this host 2026-09-28. Documentation is a capability description, not a verified capture in the running desktop application.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1. Source of a numeric observation | Desktop-owned turn/event stream | Supported lifecycle hook payload | Session-owned export or response JSON | Account quota or administrative aggregate |
| D2. Binding to a TFW unit | Explicit task/phase/role key at session creation | Stable conversation/thread ID joined to a task-owned dispatch record | Workspace or repository path inference | No reliable binding |
| D3. Time meaning | Model/API duration | Whole turn execution interval | Tool interval | Task calendar elapsed time or account period |
| D4. Money meaning | Observed provider charge | Dated tariff estimate from token categories | Allocated subscription expense | Credit/quota state or unknown |
| D5. Surface coverage | Desktop Chat | Desktop agent/Code/Cowork mode | Separate CLI | SDK/API or organization analytics |

No alternative is selected at Gather. D5 prevents a CLI, SDK or sibling mode from silently filling a Desktop evidence row.

## Findings

### G1. Local surface and version inventory — observed

Read-only PowerShell commands: `Get-AppxPackage` filtered by application name, uninstall-registry metadata, `Get-Process` filtered by process name/path, `Get-Command`, and `--version` on the four discovered commands. Scope was executable/package metadata only; no other session content, application logs or account settings were opened.

| Named surface | Local installation/process observation | Adjacent command, separately identified |
|---|---|---|
| Antigravity | Running `Antigravity.exe` under the user Programs installation, product version `2.16.0.0`; uninstall entry `Antigravity 2.16.0`. A second user install entry reports `1.23.2`, but no current process was observed from that entry. | `agy.exe` `1.2.8`; `antigravity.cmd --version` reports `1.107.0` and a build hash. These do not establish the running 2.16.0 application's capture behavior. |
| Claude Desktop | Windows app package and running `claude.exe` at `Claude_2.9939.2.0_x64__pzs8sxrjxfjjc`; product version `2.9939.2`. A separate running Claude Code binary path reported `2.1.281`, but that on-disk path was absent at the probe checkpoint. | `claude.exe` resolved by the shell reports `2.1.278 (Claude Code)`. Its auth state and output are not the Desktop Chat or Cowork state. |
| Codex Desktop | Windows app package `OpenAI.Codex_26.924.2738.0_x64__2p2nqsd0c76g0`. | `codex.exe` reports `codex-cli 0.152.1`; its standalone sessions are separate evidence from this Desktop task. |

### G2. Antigravity 2.0 hooks — documented; local numeric capture unverified

The [official Antigravity hooks reference](https://www.antigravity.google/docs/hooks/) explicitly lists Antigravity 2.0, CLI and standalone IDE as distinct surfaces. For 2.0, workspace `.agents/hooks.json` and global `~/.gemini/config/hooks.json` are documented; `PreInvocation`, `PostInvocation` and `Stop` exist. Common hook input includes `conversationId`, `workspacePaths`, `transcriptPath`, `artifactDirectoryPath` and `modelName`. The documented `PostInvocation` input refers back to `invocationNum` and `initialNumSteps`; no token, charge or duration counter appears in that documented hook input. Transcript paths are described, but unrelated transcripts were not inspected. The [SDK usage example](https://www.antigravity.google/docs/sdk/lifecycle/) exposes `response.usage_metadata.total_token_count` for an SDK agent, a different surface and execution contract. The [CLI `/usage` page](https://www.antigravity.google/docs/cli/commands/usage/) describes a model quota panel; quota is not a turn-cost record.

Bounded adjacent probe: in a fresh temporary directory, `agy -p 'Reply with exactly: TEQM probe.' --output-format json --print-timeout 30s` returned after a timeout notice with a partial JSON record containing `conversation_id`, `duration_seconds: 0`, `num_turns: 0` and all-zero `usage`. Its `status: SUCCESS` text cannot override the timeout or establish completed consumption. No persistent hook configuration was changed and no live Antigravity 2.0 Desktop turn was sent.

### G3. Claude Desktop modes — documented distinctions; local CLI probe blocked

The [official Claude plugin guide](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) says plugins run in Desktop Chat, Cowork and Claude Code, but hooks and subagents run in Cowork and Claude Code, not Chat. The [Claude Code monitoring reference](https://code.claude.com/docs/en/monitoring-usage) documents opt-in OpenTelemetry counters/events for Claude Code, and explicitly discusses launch by the desktop app; it does not thereby prove that this installed Desktop Chat/Cowork/Code mode exports the needed fields under current configuration. The [Claude Code costs guide](https://code.claude.com/docs/en/costs) and [`/cost` reference](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet) describe Code-session estimates; a subscription usage limit is a separate basis. The [Claude usage-limit guide](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) says web, Code and Desktop share a usage limit, so a limit cannot identify one task's consumption.

Before the adjacent CLI probe, `ANTHROPIC_API_KEY` was checked for presence only and was absent; no secret value was read. A fresh, nonpersistent `claude -p ... --bare --no-session-persistence --output-format json --max-turns 1` returned JSON with a session ID, duration and zero token/cost fields, `is_error: true`, and `Not logged in · Please run /login`. The installed Desktop app's subscription therefore did not authenticate this standalone CLI probe. No login or persistent setting change was made. Desktop Chat/Cowork/Code numeric output remains unverified.

### G4. Codex Desktop versus App Server and account quota — documented/observed split

[Official OpenAI documentation for Codex App Server](https://learn.chatgpt.com/docs/app-server) describes `thread/tokenUsage/updated` for an active thread and turn lifecycle events. [Official OpenAI advanced configuration](https://learn.chatgpt.com/docs/config-file/config-advanced#turn-and-tool-activity) describes optional OpenTelemetry `turn.e2e_duration_ms` and `turn.token_usage` categories (`total`, `input`, `cached_input`, `output`, `reasoning_output`). Neither document proves that the currently exposed Codex Desktop task tools return those events or that an observer can subscribe to all existing role threads. No exporter was enabled.

Live task-scoped read-only probe: `mcp__codex_app__get_usage_limits({})` returned top-level keys for `ordinaryUsageAllowed`, `rateLimits`, `rateLimitsByLimitId`, reset credits, account ID and upsell; no thread/turn token or execution-time fields were present. Only the field names were inspected, not account identifiers or other threads. This tool is an account quota signal, not a task observation. The current task's model/effort was requested as `gpt-6-sol`/`high`; an independent effective-model readback has not been observed.

### G5. Source-strength and money boundary

This pass observed installed versions, the Codex quota-tool shape, a timed-out Antigravity CLI response and a blocked Claude Code CLI response. It did not observe a completed nonzero Desktop session counter, a Desktop execution interval or a provider charge on any of the three named surfaces. The official pages establish possible mechanisms and their scope, not live capture. A price-times-token figure would require a dated price basis and exact model/input/output/cache categories; subscription cost needs a separate allocation pool. Neither has been supplied for this pass. H1 and H4 therefore remain open.

## Checkpoint

| Found | Remaining |
|---|---|
| Exact running/installed versions of all three named desktop applications are identified. | Establish the active mode inside each Desktop app and perform a successful session-bound numeric capture where the supported interface permits it. |
| Antigravity 2.0 has documented hook identity/model fields, but its documented invocation payload lacks usage counters. | Determine whether a supported 2.0 event/export exposes usage and time for the same conversation, including child sessions. |
| Claude Desktop separates Chat from Cowork/Code hooks; a standalone CLI is not logged in. | Test a fresh Desktop mode without importing CLI auth assumptions; determine export/event field coverage. |
| Codex App Server and OTel document token/time signals; the exposed task tool returned account quotas only. | Determine whether the working Desktop thread can be observed through a supported task-owned event route, without inspecting unrelated tasks or changing global configuration. |

**Gather decision:** Extract will compare only route configurations that keep exact surface, stable unit identity, counter semantics and money basis separate. No capture route is yet shown to satisfy the pilot's H1 condition.

**Sufficiency:**
- [x] External primary sources used for every named surface.
- [x] Briefing gap closed for this stage: dimensions and exact local surfaces are mapped; capability gaps are explicit rather than silently filled.
- [x] Five independent decision dimensions identified with at least three alternatives each.

**Material handover:** Producer Researcher; recipient exact parent Coordinator. Sources/epoch: linked official pages fetched 2026-09-28 and the bounded local commands above on the same date. Inspected scope: public documentation, executable/package metadata and two isolated adjacent CLI responses, plus this task's quota-tool field names. Material: no completed Desktop numeric observation has yet been demonstrated. Uncertainty: app modes, live counter semantics and child-session coverage. Continuation: Extract maps plausible supported configurations and rejects account quota or adjacent-product substitution.

Stage complete: YES
→ User decision: Close Gather and advance to Extract under the approved focused scope, or request one specific correction.
