# Extract — "What do we NOT see?"
> **Mindset:** Analyst. Combine Gather's independent dimensions without treating a documented component as a demonstrated route.
> **Task / producer:** `TFW_20260928-181352_TEQM`, iteration 1; Researcher `codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243`.
> **Parent Coordinator / return:** `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793`; `tfw-gates-only`, `native-gates`.
> **Authority / selection:** approved HL §4.1 at `36c100b1d6e246fbdb45ec7a2341bb652ca80b7a`; focused mode; Gather advance `d7a26a7ff19c9e670c707dacffe9fb55ea646dd3`.
> **Evidence epoch:** primary documentation revisited and local UI capability inventoried 2026-09-28. No other task's session content was inspected.

## Configuration Space

The headers reproduce Gather's five decision dimensions. These are combinations to test, not recommendations. “Conditional” means a required field or access path is still unverified.

| Config | D1. Source of a numeric observation | D2. Binding to a TFW unit | D3. Time meaning | D4. Money meaning | D5. Surface coverage |
|---|---|---|---|---|---|
| C1 | Antigravity 2.0 Desktop `PreInvocation`/`PostInvocation`/`Stop` hooks plus task-owned timestamps | `conversationId` joined to an explicit task dispatch | Hook-bounded invocation or loop wall time | Unknown | Antigravity 2.0 Desktop |
| C2 | Antigravity 2.0 hooks for identity plus a supported conversation export if it carries numeric usage (conditional) | `conversationId` join | Hook interval plus export timestamps (conditional) | Dated tariff estimate if model and token categories are present (conditional) | Antigravity 2.0 Desktop |
| C3 | Antigravity SDK response `usage_metadata` | SDK-created conversation ID | Client-wrapped request interval | Dated tariff estimate (conditional) | SDK, adjacent to Desktop |
| C4 | Claude Desktop Chat data export (numeric fields unverified) | Chat ID joined to a task-owned launch | Chat start/end calendar elapsed | Unknown | Claude Desktop Chat |
| C5 | Claude Code OpenTelemetry `api_request` events and token/cost metrics | `session.id` joined to explicit task/role launch; `query_source` partitions main and subagent requests | API-request duration; separate active-time or wrapper interval needed for agent execution | Event `cost_usd` as an estimate, not a subscription charge | Claude Code in Desktop Code mode (launch/export unverified locally) |
| C6 | Claude Desktop Cowork hooks/events (numeric payload unverified) | Cowork session or task ID joined to launch | Task/turn interval to establish | Unknown or separate subscription allocation | Claude Desktop Cowork |
| C7 | Codex App Server `thread/tokenUsage/updated` plus turn events | Exact Desktop thread ID joined to task/role route | Turn start/completion interval | Dated tariff estimate only if model/token categories and applicable price are known | Codex Desktop through App Server (attachment unverified) |
| C8 | Codex OpenTelemetry `turn.token_usage` and `turn.e2e_duration_ms` | Explicit task-specific launch/export labels, if available; default metric tags do not prove task join | Turn end-to-end interval | Dated tariff estimate (conditional) | Codex runtime/possible Desktop route, unverified |
| C9 | Task-owned start/finish observations combined with a later provider numeric export | Explicit task/phase/role ID in the observation | Measured wrapper interval, separately labeled from model/API time | Unknown until provider data joins | Any named Desktop surface with a task-owned turn boundary |
| C10 | Account quota or administrative aggregate | Product period allocation rule, no unique task key | Account-period time | Allocated subscription expense | Account-wide, across surfaces and unrelated use |

C9 makes a combination absent from the Briefing's capture sketch: a task-owned interval can be recorded independently of provider timing while exact token observations arrive later. Its time field would retain the wrapper's actual meaning. C10 is listed so the later challenge can show precisely why an aggregate cannot answer the per-task question without an allocation convention and complete eligible pool.

## Findings

### E1. Local Desktop inspection boundary

The `computer-use` runtime was initialized and its application inventory read without opening any session. It returned one Claude window titled `Claude`, one Codex window titled `ChatGPT`, and one Antigravity process window whose title names an unrelated project (the same returned window appears under two Antigravity app registrations). The approved mandate excludes another session's unreturned content. Therefore no existing window state, screenshot, transcript or chat was opened. A fresh blank window was not verified as selectable; Desktop UI numeric capture remains unobserved. The inventory is a practical access attempt, not evidence that the apps lack usage features.

### E2. Claude Code request-level join is richer than a session total — documented only

The [Claude Code monitoring reference](https://code.claude.com/docs/en/monitoring-usage) describes `api_request` events with `session.id`, model, estimated `cost_usd`, `duration_ms`, input/output/cache token categories, request IDs, `query_source` and effort. It states `session.id` is included in metrics by default, but `/clear` assigns a new ID; resumed sessions can repeat or reorder `event.sequence`, so timestamps matter. The source also describes `query_source` values for main, compaction and subagents, permitting a potential partition only if the actual Desktop Code launch exports those events. The same documentation warns transcript joins are version-specific. A local `claude.exe` CLI probe was unauthenticated; no Desktop Code OTel event has been observed.

### E3. Antigravity identity hook plus numeric source is an unproven join

The [Antigravity 2.0 hooks reference](https://www.antigravity.google/docs/hooks/) supplies `conversationId`, model and hook boundaries but documents no token or cost field in `PostInvocation` input. The [SDK usage example](https://www.antigravity.google/docs/sdk/lifecycle/) supplies `usage_metadata` in an SDK response. Combining these would require proof that a supported 2.0 Desktop export shares the same conversation identity and counter meaning; the SDK alone is not that proof. The CLI timeout with zero values adds no completed-counter evidence.

### E4. Codex thread events and OTel metrics have different joins

The [Codex App Server reference](https://learn.chatgpt.com/docs/app-server) names thread-scoped usage updates and lifecycle events; a current task route already has an exact thread address, which is a plausible join key if the working Desktop thread can be subscribed or read through a supported numeric interface. [OpenAI advanced configuration](https://learn.chatgpt.com/docs/config-file/config-advanced#turn-and-tool-activity) names per-turn token and end-to-end-time metrics, but its default tags (`auth_mode`, `originator`, `session_source`, `model`, `app.version`) do not by themselves demonstrate the exact task/role join. The exposed tool catalog has `get_usage_limits` but no thread-token read method, and its live result is account-level. Attaching an external App Server client to this task remains unverified; enabling persistent OTel configuration is outside this iteration's grant.

### E5. Configuration implications to test in Challenge

- A session ID is necessary but not sufficient for TFW attribution: the task/phase/role association must be recorded when the session is launched, and child sessions need their own identity or an explicit inclusion rule.
- A request duration, turn wall interval, tool duration and calendar task elapsed time are distinct measures. The report cannot sum overlapping request/tool intervals as though they were separate agent labor.
- `cost_usd` in Claude Code telemetry is documented as an estimate. Antigravity credits, Codex quota and shared Claude usage limits are not observed task charges. The pilot needs a separate price epoch or explicit subscription allocation when money is requested.
- A combined route such as C9 can retain partial time coverage while token capture is absent. It must label the report partial, not manufacture a zero token cost.

## Checkpoint

| Found | Remaining |
|---|---|
| Ten route configurations expose distinct identity, time, money and surface joins; C9 is a new cross-source combination. | Challenge which conditional join can be demonstrated on an exact Desktop mode under the current access boundary. |
| Claude Code OTel documents request-level token, estimated-cost, duration and subagent-source fields. | Verify Desktop Code mode launches/exporters and child coverage on a fresh owned session; CLI auth failure cannot answer that. |
| Codex has a plausible exact thread-key join with App Server events, and Antigravity hooks have a documented conversation key. | Verify access to live numeric events/export without global configuration or unrelated transcript reads. |

**Extract decision:** Challenge will stress C5, C7 and C2 as the three surface-specific numeric joins, while using C9 as a partial-coverage fallback and C10 as the aggregate false-positive case. No configuration is selected for implementation yet.

**Sufficiency:**
- [x] External primary sources used in this stage.
- [x] Briefing gap closed for this stage: the full five-dimension configuration space and hidden join assumptions are visible.
- [x] Configuration Space built from Gather's dimension names; ten non-identical combinations listed.

**Material handover:** Producer Researcher; recipient exact parent Coordinator. Source/epoch: linked official pages revisited 2026-09-28, current tool catalog and local app/window inventory the same day. Inspected scope: documented event schemas and window metadata only; no foreign session content. Material: the attractive per-request and per-thread fields still require exact Desktop-mode access and an explicit TFW join. Uncertainty: all three live joins, child coverage and money basis. Continuation: Challenge attempts bounded disconfirmation before selecting a first path or declaring the prerequisite absent.

Stage complete: YES
→ User decision: Close Extract and advance to Challenge, or request one specific correction.
