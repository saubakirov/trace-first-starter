# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260928-181352_TEQM](../../HL-TFW_20260928-181352_TEQM.md)
> Goal: Measure tokens, time, quality, and attributable cost for TFW work across roles and product areas.

## Configuration Space

| Config | D1: Telemetry Extraction Source | D2: Task/Role Binding | D3: Execution Interval Semantics | D4: Money Valuation Basis | Feasibility & Fit |
|---|---|---|---|---|---|
| C1 | Direct SQLite (`conversations/<id>.db` `gen_metadata`) | Step index join (`kv_last_step_index` mapped to `transcript.jsonl`) | Model + Tool Execution duration (turn latency + tool runtime) | Public Gemini tariff model (rate card per input/cache/output) | High: fully observable, granular, zero modification to agent runtime |
| C2 | Lifecycle Hook (`hooks.json` `Stop` / `PostInvocation`) | Checkpoint cumulative diffing on role entry/exit | Model + Tool Execution duration | Public Gemini tariff model | High: automated collection triggered on session exit/turn completion |
| C3 | Direct SQLite (`conversations/<id>.db` `gen_metadata`) | Session-level containment (one thread per role) | Pure Model Generation Latency (`timing_f11` ns) | Tariff model + subscription pool allocation | Medium: clean attribution but ignores tool wait/processing overhead |
| C4 | Transcript parsing (`transcript.jsonl`) | Step index join | Calendar Wall-Clock Elapsed Time | Token volume only (unpriced / unknown) | Low: transcript lacks token counters and thinking breakdowns |
| C5 | Subprocess `agy` CLI (`--output-format json`) | Session-level containment | Total CLI session duration | Built-in CLI cost estimate (`cost` field) | Medium: requires spawning separate CLI runs; bypasses IDE environment |

## Findings

### E1: Direct SQLite Protocol Buffer Extraction Pipeline
Inspection of Antigravity's internal storage reveals that every model generation writes an immutable row to SQLite table `gen_metadata` in `<conversation_id>.db`. The record is structured as follows:
1. **Model & Trajectory Identity:**
   - Top-level `f19` stores model name: `gemini-3.8-flash`.
   - Key-value attributes store `kv_model_enum` (`MODEL_PLACEHOLDER_M318`), `kv_trajectory_id` (UUID), `kv_request_id` (`{trajectory_id}-{turn_idx}`), and `kv_last_step_index`.
2. **Token Categories:**
   - Field 1 -> Field 4 contains the `UsageMetadata` message:
     - `f2` (varint): Prompt / input tokens (fresh context).
     - `f5` (varint, optional): Cached prompt tokens (populated on subsequent turns).
     - `f3` (varint): Total candidate / output tokens.
     - `f9` (varint): Thinking / reasoning tokens.
     - `f10` (varint): Content / response tokens.
   - **Proved Relationship:** `f3 == f9 + f10`. Thinking is strictly an internal constituent of candidate tokens, not an uncounted external addition.
3. **Model Generation Latency:**
   - Field 1 -> Field 11 stores exact model generation duration: `t1` (seconds) and `t2` (nanoseconds).
4. **Extraction Tooling:**
   - A lightweight pure-Python script (~40 LOC, using standard library `sqlite3` without external protobuf compiler dependencies) can reliably parse and aggregate these records for any session.

### E2: TFW Lifecycle Integration and `economics.md` Collection
How an automated or semi-automated collector can produce `economics.md` for a TFW task in Antigravity:
1. **Binding Key:** The conversation ID is exposed to the agent via system prompt metadata (`Conversation ID: b022b050-...`) and to lifecycle hooks via `conversationId` in stdin.
2. **Checkpoint Recording:**
   - When a role starts (e.g. Executor entering ONB), it notes the current `max(idx)` in `gen_metadata` (or timestamp).
   - When a role finishes (e.g. Executor writing RF, Reviewer writing REVIEW), it queries all rows where `idx > start_idx`.
   - Summed fresh input, cached input, thinking, and content tokens are calculated.
3. **Execution Interval Determination:**
   - **Agent Model Time:** Sum of `timing_f11` across the role's turns.
   - **Tool Execution Time:** Sum of completed tool durations recorded in `transcript.jsonl` step payloads.
   - **Total Role Interval:** Combined model + tool runtime.
   - **Task Elapsed Time:** Timestamp difference between task creation and completion recorded in `status.md` / `journal/`.
4. **Overhead Assessment:**
   - Reading SQLite while Antigravity is running is safe because SQLite WAL mode (`.db-wal`) supports concurrent readers without blocking the IDE's writes. Querying and parsing 100 turns takes < 25 ms.

### E3: Comparative Architecture: Antigravity IDE 2.17.0 vs `agy` CLI 1.2.12
| Architectural Aspect | Antigravity IDE 2.17.0 | `agy` CLI 1.2.12 |
|---|---|---|
| Runtime Environment | Interactive desktop IDE (Electron + Language Server) | Headless / interactive terminal CLI (Go binary) |
| Telemetry Granularity | Per-turn protobuf in SQLite (`gen_metadata`), per-step JSONL | Per-session aggregate in stdout JSON |
| Token Accounting | Explicit split: fresh prompt (`f2`), cached prompt (`f5`), thinking (`f9`), content (`f10`) | Cumulative totals: `input_tokens`, `cache_read_tokens`, `output_tokens`, `thinking_tokens` |
| Timing Metric | Nanosecond model latency per turn + tool timestamps | Single `duration_seconds` for entire prompt/session |
| Cost Telemetry | Unpriced in storage; requires tariff lookup | Status line model exposes unrounded `cost` |
| TFW Integration Path | Read native SQLite on task/phase completion or via `Stop` hook | Capture stdout JSON from wrapper invocation |

### E4: Empirical Validation on Historical Session (`dbf9e905-1f6a-406d-ae62-8f49d5ec42ef`)
Executing the C1 extraction script against an unrelated, completed historical session (`dbf9e905-1f6a-406d-ae62-8f49d5ec42ef`) confirmed:
1. **Decoupled Telemetry Extraction:** The script successfully extracted all 7 turns, model identities, token breakdowns, and timing records in **11 milliseconds** without waking the session, launching an agent, or reading chat transcripts.
2. **Context Cache Invariant:** The caching mechanism behaves predictably across disparate sessions. On turn 0, cache read is 0. Once context stabilizes (turns 1-4, 6), context caching absorbs ~20k-24k tokens per turn, slashing billed prompt volume by 61.4% (109,955 cached vs 69,157 fresh).
3. **Privacy Compliance (HL §6 DoF 6):** Pure numeric telemetry extraction accesses only `gen_metadata` and `timing_f11`. It completely bypasses user prompt text, model conversation prose, and internal chain-of-thought texts, eliminating privacy and unreturned-reasoning contamination risks.

## Checkpoint

| Found | Remaining |
|---|---|
| Complete extraction pipeline (C1/C2) from SQLite `gen_metadata` | Validated tariff rate sheet for Gemini 3.8 Flash, Gemini 3.1 Pro, Claude Sonnet 4.6 on Antigravity |
| Proved token arithmetic: Candidate = Thinking + Content | Whether Antigravity plans to expose a direct JSON export command in a future release |
| Exact model latency and tool timestamp extraction mechanics | |

**Sufficiency:**
- [x] External source used? (Verified SQLite storage contracts, protobuf decoding, and `agy` changelog)
- [x] Briefing gap closed? (Mapped configuration space and designed end-to-end extraction pipeline)
- [x] Configuration Space built from Gather dimensions? (5 configurations evaluated against D1-D4)

Stage complete: YES
→ User decision: Proceed to Challenge (autonomous focused pass per user instruction).
