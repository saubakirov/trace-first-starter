# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260928-181352_TEQM](../../HL-TFW_20260928-181352_TEQM.md)
> Goal: Measure tokens, time, quality, and attributable cost for TFW work across roles and product areas.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1: Telemetry Extraction Source | Direct SQLite read of `<conversation_id>.db` table `gen_metadata` | Lifecycle Hooks (`hooks.json` `PostInvocation` / `Stop`) querying SQLite | Parsing `transcript.jsonl` step event stream | Subprocess invocation of `agy` CLI with `--output-format json` |
| D2: TFW Task/Role Binding | Step index join (`last_step_index` in `gen_metadata` mapped to `transcript.jsonl` tool steps) | Checkpoint cumulative snapshot diffing on role entry/exit (`status.md` transitions) | Session-level containment (one conversation thread per role unit) | External wrapper session manager |
| D3: Execution Interval Semantics | Pure Model Generation Latency (`timing_f11` in `gen_metadata`, nanosecond precision) | Model + Tool Execution duration (calculated from step `created_at` deltas in transcript) | Calendar Wall-Clock Elapsed Time (`last_user_input_time` to final turn completion) | Sum of agent active CPU time across child processes |
| D4: Money Valuation Basis | Public Gemini tariff model (list rates applied to prompt, cached, output tokens) | Fixed subscription pool allocation weighted by model token share | Unrounded CLI status line cost model (`cost` metric from `agy`) | Explicitly unpriced / labeled Unknown with token volume only |

## Findings

### G1: Antigravity IDE Runtime & Storage Architecture
- **Host Binary:** The active Antigravity IDE application is `C:\Users\c0rpa\AppData\Local\Programs\antigravity\Antigravity.exe` (FileVersion 2.17.0.0, ProductVersion 2.17.0.0, commit distro `0c7d350c3a9e8639ea238cc996ec4f6dcf1e35cd`, Electron 34/Chromium architecture x64).
- **Backend Service:** Managed by `C:\Users\c0rpa\AppData\Local\Programs\antigravity\resources\bin\language_server.exe` (162 MB native binary) which interfaces with the Gemini model backend and coordinates file/tool operations.
- **AppData Directory:** Centrally stored under `%USERPROFILE%\.gemini\antigravity\` (`C:\Users\c0rpa\.gemini\antigravity\`).
  - `conversation_summaries.db`: Global SQLite database maintaining high-level conversation metadata (`conversation_id`, `title`, `step_count`, `last_modified_time`, `workspace_uris`, `status`, `last_user_input_time`).
  - `conversations/<conversation_id>.db`: Dedicated SQLite database per session storing execution steps, permission requests, and raw turn generation metadata with WAL mode (`.db-wal`).
  - `brain/<conversation_id>/.system_generated/logs/transcript.jsonl`: Append-only JSONL log containing step sequence, created timestamps, user prompts, thinking blocks, and tool calls.

### G2: Accessible Numeric Metadata in Live Session `b022b050-c6ce-450a-a406-257fbf471601`
Direct programmatic inspection of `C:\Users\c0rpa\.gemini\antigravity\conversations\b022b050-c6ce-450a-a406-257fbf471601.db` table `gen_metadata` reveals complete per-turn telemetry stored as binary Protocol Buffers:
- **Model Identity:** Stored as top-level string field 19 (e.g. `gemini-3.8-flash`) and key-value pair `kv_model_enum` (e.g. `MODEL_PLACEHOLDER_M318`).
- **Token Telemetry (Submessage Field 1 -> Field 4):**
  - `f2`: Fresh prompt/input tokens.
  - `f5`: Cached prompt/input tokens (observed starting on turn 2 after initial context caching).
  - `f3`: Candidate/output tokens.
  - `f9`: Thinking tokens (reasoning model tokens).
  - `f10`: Content tokens (model text/tool call output).
  - **Arithmetic Identity:** For 100% of tested turns, `f3 == f9 + f10`. Candidate tokens are the exact sum of thinking tokens and content tokens.
- **Timing Telemetry (Submessage Field 1 -> Field 11):**
  - `t1`: Generation duration in seconds (varint).
  - `t2`: Generation duration fractional nanoseconds (varint).
- **Turn Context:**
  - `kv_last_step_index`: Corresponds to the triggering step index in `steps` and `transcript.jsonl`.
  - `kv_request_id`: Formatted as `{trajectory_id}-{turn_idx}`.
  - `f7`: Internal bot generation identifier (e.g. `bot-6a7fea9d-59c2-4252-a3a0-a0d895bae6f7`).
  - `f8`: Persistent session ID hash (e.g. `-3750763034362895579`).
- **Live Conversation Sample:** Across the first 69 turns of this active session:
  - Fresh input tokens sum: 569,242
  - Output tokens sum: 23,427 (comprising 9,986 thinking tokens + 13,441 content tokens)
  - Total model generation duration: 236.92 seconds (~3.95 minutes).

### G3: Lifecycle Hooks & Integration Points
The Antigravity Customization System ([`hooks.json`](file:///C:/Users/c0rpa/.gemini/antigravity/builtin/skills/agy-customizations/docs/hooks.md)) supports five distinct event hooks:
- Events: `PreToolUse`, `PostToolUse`, `PreInvocation`, `PostInvocation`, `Stop`.
- Execution: Shell commands triggered synchronously during the agent execution loop.
- Payload (`stdin` JSON): Includes `conversationId`, `workspacePaths`, `transcriptPath`, `artifactDirectoryPath`, `modelName`.
- Key Insight: While hook payloads do not include raw token numbers directly, they provide the exact `conversationId`. A hook or post-step script can therefore immediately query `conversations/<conversationId>.db` with zero ambiguity.

### G4: Comparison with Adjacent CLI (`agy` 1.2.12)
- Binary located at `C:\Users\c0rpa\AppData\Local\agy\bin\agy.exe`.
- In headless print mode (`agy --print "<prompt>" --output-format json`), it emits a JSON summary with:
  `conversation_id`, `input_tokens`, `output_tokens`, `thinking_tokens`, `cache_read_tokens`, `total_tokens`, `duration_seconds`.
- Release 1.1.21 added an unrounded estimated `cost` field to the status line model.
- Key differences:
  - Antigravity IDE persists full turn-by-turn history in SQLite with nanosecond timestamps, separate thinking/content breakdown, and explicit cached prompt counters.
  - `agy` CLI provides cumulative session aggregates in JSON stdout. Both share the underlying token accounting model (`thinking` is part of candidate output; cache reads reduce billed input).

## Checkpoint

| Found | Remaining |
|---|---|
| Exact Antigravity IDE version (2.17.0) and backend binary (`language_server.exe`) | Whether child subagents share `<parent_id>.db` or create separate `<child_id>.db` databases |
| Exact SQLite schema and protobuf decoding for per-turn tokens (`f2` fresh input, `f5` cached, `f9` thinking, `f10` content, `f3` output sum) | Exact tariff rate lookup integration for Antigravity-supported models in `economics.md` |
| Exact model generation latency in seconds and nanoseconds (`timing_f11`) | Whether `language_server.exe` exposes an open OTel/gRPC endpoint for streaming metrics |
| Lifecycle hook stdin contracts and `conversationId` binding | |

**Sufficiency:**
- [x] External source used? (Verified Antigravity 2.17.0 binary, `agy` 1.2.12, local SQLite database, and official customization docs)
- [x] Briefing gap closed? (Antigravity IDE self-inspection completed with verified token and timing counters)
- [x] Dimensions identified? (4 dimensions identified: Telemetry Extraction Source, Task/Role Binding, Execution Interval Semantics, Money Valuation Basis)

Stage complete: YES
→ User decision: Proceed to Extract (autonomous focused pass per user instruction).
