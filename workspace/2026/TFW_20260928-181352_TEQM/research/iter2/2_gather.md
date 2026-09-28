# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260928-181352_TEQM](../../HL-TFW_20260928-181352_TEQM.md)
> Goal: Identify what this exact Claude Code session exposes about its own tokens/time/money and how `economics.md` could collect it.

## Dimensions

| Dimension | Alt A | Alt B | Alt C |
|-----------|-------|-------|-------|
| D1: Numeric source mechanism | This session's own `ccd_session_mgmt.get_usage`/`get_session` (internal harness tools) | Claude Code CLI `--output-format json` (iter1, external process) | Claude Code OTel exporter (`claude_code.token.usage` / `.cost.usage` / `.active_time.total`, public docs, requires enabled telemetry) |
| D2: What the number represents | Live context-window occupancy (a gauge that can shrink on compaction) | A per-invocation cumulative total (input+output+cache, fixed once the process exits) | A per-request counter, incremented once per API request, exported continuously |
| D3: Money meaning | Account-level quota percentage against a rolling window (5-hour / weekly), no dollar figure, no per-token price | Per-invocation `total_cost_usd` at `costBasis: list` (a computed list-price estimate, not a bill) | Per-request `claude_code.cost.usage` metric in USD (documented, requires OTel) |
| D4: Child/parallel coverage | `list_sessions(linked:true)` shows sibling sessions this session started, each with its own `get_usage` — but only while that child is still running | Not applicable — a CLI invocation has no children of its own | OTel span attributes (`agent.name`, `mcp_server.name`, …) tag which sub-unit a request belongs to, if instrumented |

## Findings

### G1: This session's own exposed fields (`get_usage` / `get_session`, sampled twice)

First sample (17:55:17 activity):
```
plan.windows: 5-hour=87% (resets 4m), Weekly·all-models=50% (resets 4d 8h), Weekly·Fable=8%
plan.extraUsage: enabled=false
context.tokensUsed=134,884 / contextWindow=1,000,000 (13%), autoCompactsAtPercent=97
context.categories: Messages 54,537 / System tools 44,385 / MCP tools 16,568 / System prompt 10,786 / Skills 6,102 / Memory files 2,506
session: id=local_802eab5b-1770-4551-b59a-aefd367bb975, title="TEQM research iteration 2", model=claude-sonnet-5, effort=high,
         permissionMode=bypassPermissions, createdAt=2026-09-28T17:53:46.553Z, lastActivityAt=2026-09-28T17:55:17.680Z
```

Second sample (17:57:50 activity, after Briefing + two external lookups + this pair of calls):
```
plan.windows: 5-hour=88% (resets 2m), Weekly·all-models=50%, Weekly·Fable=8%
context.tokensUsed=147,756 (15%) — +12,872 tokens over the ~153s between samples
context.categories: Messages 64,359 (+9,822) / System tools 46,351 (+1,966) / MCP tools 17,652 (+1,084) / System prompt/Skills/Memory files unchanged
session: same id/model/effort/mode; lastActivityAt=2026-09-28T17:57:50.580Z
```

The numbers move in response to real work between two samples: this is a live, queryable gauge, not a static placeholder. Model identity (`claude-sonnet-5`), effort (`high`) and permission mode (`bypassPermissions`) are exposed and match this environment's own system-reminder. No field named `cost`, `price`, `input_tokens`, `output_tokens`, `cache_tokens` or `thinking_tokens` exists anywhere in either tool's output.

### G2: Public documentation for the adjacent CLI/OTel surface

[Claude Code monitoring — OTel](https://code.claude.com/docs/en/monitoring-usage) documents, for the CLI when `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA` is enabled: a `claude_code.token.usage` counter split by `input`/`output`/`cacheRead`/`cacheCreation`, tagged with `model`, `query_source`, `speed`, `effort`, `agent.name`, `mcp_server.name`, etc.; a `claude_code.cost.usage` counter in USD with the same tags; and a `claude_code.active_time.total` counter in seconds split into `"user"` (keyboard) and `"cli"` (tool execution + generation) — the latter is close to the HL's "agent execution time" definition. With enhanced tracing, span-level `llm_request` events additionally carry `duration_ms` and per-request token counts. None of this is exposed inside this Desktop/Code-tab session; it requires the separate CLI process with telemetry env vars set, matching iter1's finding that CLI evidence does not establish Desktop evidence (and, this iteration finds, the reverse holds too).

A web search on Desktop-app usage limits (queried 2026-09-28) turned up only user-facing explainer articles and a GitHub issue (`anthropics/claude-code#90708`, "Desktop app: bring back the context-usage indicator") confirming the context-percentage indicator is a UI feature with a history of being added/removed, not a stable documented API; and issue `#52467` describing a Desktop-specific extra-usage bug, i.e., the Desktop app's usage/quota surface is known (by its own bug tracker) to diverge from the CLI's on the same account. No official page documents the `ccd_session_mgmt` tool surface used here — it appears to be internal to this Claude Code app/agent harness, not the public product.

### G3: Context-window size discrepancy

General Claude Code usage articles found via search describe a 200K-token context window across paid plans (500K on some Enterprise models). This session's own `get_usage` reports `contextWindow: 1,000,000`. The two do not reconcile from documentation alone — either the cited articles are stale relative to the current Sonnet 5 / Team-plan configuration, or this session's context allowance is a plan/model-specific exception. Preserved as an open, sourced discrepancy rather than resolved by inference.

### G4: Sibling/child session visibility (documented, not exercised)

Per the `list_sessions` tool's own description: passing `linked: true` restricts the listing to "your own family" — sessions this session started, the session that started this one, and their own linked sessions — each row carrying its own `model`/`permissionMode` (the latter "reported only for sessions this session started"). `get_usage`/`get_session` accept an explicit `session_id` for any such sibling, but `context` reports `"unavailable"` for "an idle, starting or archived session" — i.e., a child's numeric snapshot must be pulled while it is still running, or it may become unrecoverable. This iteration did not spawn a child (no `Agent` call was made), so this dimension is documented from the tool schema, not independently observed this session — flagged accordingly, not asserted as tested.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| This session exposes context-window occupancy + account quota + session/model/effort identity; no token-direction split, no thinking counter, no dollar cost. | Whether `contextWindow: 1,000,000` reflects a documented plan/model allowance or an undocumented exception. |
| Two live samples show the gauge moving in real time with real work (+12,872 tokens / ~153s). | Whether this delta is a faithful proxy for actual API-billed tokens consumed in that interval, or merely context-window growth (see Challenge). |
| OTel/CLI path (iter1 + public docs) has a genuinely richer, documented schema (token-type split, USD cost, active-time split) unavailable from inside this Desktop session. | Whether that OTel path can be attached to a *Desktop* app session at all, or only to a separate CLI process (iter1 already left Claude Desktop's own event route unverified). |
| Child/sibling session visibility is schema-documented via `list_sessions`. | Not exercised this iteration; a live parent/child join remains unobserved for the Claude family, same gap iter1 flagged for AGY/Codex. |

**Sufficiency:**
- [x] External source used? (Claude Code OTel monitoring doc; Desktop usage-limit web search incl. two GitHub issues)
- [x] Briefing gap closed? (Guiding Questions 1–2 answered by G1/G3; Q3 partially answered by G4, flagged as documented-not-observed)
- [x] Dimensions identified?

Stage complete: YES
→ User decision: none required — iteration mandate authorizes continuous execution (see Briefing, User Direction).
