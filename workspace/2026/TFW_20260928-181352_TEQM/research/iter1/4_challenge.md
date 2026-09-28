# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. A route survives only within the evidence actually obtained.
> **Task / producer:** `TFW_20260928-181352_TEQM`, iteration 1; Researcher `codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243`.
> **Parent Coordinator / return:** `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793`; `tfw-gates-only`, `native-gates`.
> **Authority / selection:** approved HL §4.1 at `36c100b1d6e246fbdb45ec7a2341bb652ca80b7a`; focused mode; Extract advance `fbc42eb377e5cfd623b93601c5c12546b6148b1b`.
> **Evidence epoch:** external primary sources and bounded local diagnostics on 2026-09-28. No unrelated session transcript or content is evidence here.

## Consistency Check

Every pair among Gather's five dimensions (D1–D2, D1–D3, D1–D4, D1–D5, D2–D3, D2–D4, D2–D5, D3–D4, D3–D5, D4–D5) was checked for a contradictory claim. The table records the material incompatibilities; unlisted pairs can coexist if their values retain separate meanings and explicit coverage.

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible as one task-bound measurement |
|---|---|---|---|---|
| D1. Source of a numeric observation | Account quota/aggregate | D2. Binding to a TFW unit | Exact task/role from quota alone | A shared account bucket contains other use and no unique task key; partitioning needs an independent complete allocation ledger. |
| D1. Source of a numeric observation | Antigravity 2.0 hook payload alone | D4. Money meaning | Dated token tariff estimate | The documented `PostInvocation` payload has identity and invocation indexes, not input/output/cache counters; model name alone cannot price a turn. |
| D1. Source of a numeric observation | Desktop Chat export with no numeric fields established | D3. Time meaning | Agent execution interval | A conversation export's existence does not establish begin/end execution events; chat calendar age cannot substitute. |
| D2. Binding to a TFW unit | Workspace/repository path inference | D5. Surface coverage | Parallel roles or shared workspace | Several tasks and roles can use the same directory, so the path cannot uniquely allocate a provider event. |
| D3. Time meaning | Tool interval | D4. Money meaning | Combined task-agent total from additive tool plus enclosing turn time | The tool interval may be inside the turn; summing both duplicates time, regardless of money policy. |
| D4. Money meaning | Provider tariff estimate plus subscription allocation as one total | D5. Surface coverage | The same subscribed consumption | These are different accounting bases for the same use; adding them double-charges the same consumption. |
| D5. Surface coverage | Antigravity SDK or separate CLI | D1. Source of a numeric observation | Claimed as verified Antigravity 2.0 Desktop output | Product adjacency does not establish the app's own event or export. |
| D5. Surface coverage | Claude Desktop Chat | D1. Source of a numeric observation | Claude Code/Cowork plugin hook | [Anthropic's plugin guide](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) says hooks run in Cowork and Code, not Chat. |

**Surviving configurations** (the columns retain Gather's dimension names; “survives” means internally coherent, not implemented or verified):

| Config | D1. Source of a numeric observation | D2. Binding to a TFW unit | D3. Time meaning | D4. Money meaning | D5. Surface coverage | Notes |
|---|---|---|---|---|---|---|
| C1 | Hooks and task-owned timestamps | `conversationId` dispatch join | Hook-bounded wall interval | Unknown | Antigravity 2.0 | Time/identity only; insufficient H1 tokens. |
| C2 | Hooks plus a supported numeric export | `conversationId` join | Hook interval plus export timestamps | Conditional tariff estimate | Antigravity 2.0 | Export and matching numeric key unverified. |
| C3 | SDK `usage_metadata` | SDK session key | Wrapped request interval | Conditional tariff estimate | Antigravity SDK | Coherent adjacent route; cannot satisfy exact Desktop claim. |
| C5 | Claude Code OTel `api_request` | `session.id` and explicit task launch; `query_source` for child partition | Request duration plus separate execution interval | Documented estimated `cost_usd` | Claude Desktop Code mode | Mode launch/export unverified locally. |
| C6 | Cowork hook/event | Task-owned session key | Measured task/turn interval | Unknown | Claude Desktop Cowork | Numeric payload and child coverage unverified. |
| C7 | Codex App Server usage/turn events | Exact thread ID dispatch join | Turn interval | Conditional tariff estimate | Codex Desktop | Stream attachment and live numeric event unverified. |
| C8 | Codex OTel metrics | Explicit launch/export label | Turn end-to-end interval | Conditional tariff estimate | Codex runtime/Desktop | Label and process-scoped export need verification. |
| C9 | Task-owned timestamps plus later provider export | Explicit task/phase/role key | Wrapper interval | Unknown until join | Any exact Desktop mode | Honest partial fallback; cannot alone meet H1. |
| C11 | `agy --output-format json` terminal result | Fresh CLI `conversation_id` recorded with exact TFW task/role at launch | CLI `duration_seconds` for the completed session | Unknown; no observed charge field | Antigravity CLI 1.2.8 | Added after Extract by the owner's direct CLI steering; one completed local capture is observed below. |

C4 and C10 remain possible as descriptive chat-age/account-period reports, but are eliminated as full-task economics capture because they cannot supply both task-bound tokens and agent execution time under current evidence.

**Unexpected survivor:** C9 can preserve task-bound timing without provider timing metadata. Its interval must be labeled as wrapper wall time, and it remains partial until a provider numeric join is demonstrated.

## Findings

### C1. Codex cumulative-counter trap and exact local schema

The [official Codex App Server reference](https://learn.chatgpt.com/docs/app-server) names `thread/tokenUsage/updated` but does not expose its full counter shape on the page. A disposable, read-only schema-generation probe used the installed `codex-cli 0.152.1`: `codex app-server generate-ts --out <temporary directory>`. The generated `ThreadTokenUsageUpdatedNotification` contains `threadId`, `turnId` and `tokenUsage`; `ThreadTokenUsage` contains `total`, `last` and `modelContextWindow`; each `TokenUsageBreakdown` contains total/input/cached-input/cache-write-input/output/reasoning-output token fields. The generated `RawResponseCompletedNotification` is labeled internal-only and must not be treated as the supported integration route. This schema is local CLI evidence for its own version, not a Desktop 26.924.2738 stream observation.

If a cumulative `total` changes from 120 to 150 tokens, adding the two snapshots reports 270 rather than 150. A collector must use a validated delta or an exact final total once; `last` must be checked for its update semantics before it is added across events. A parent aggregate plus child rows must likewise not be summed until child inclusion is known. There is no exposed `mcp__codex_app` thread-token retrieval method in this task's current tool catalog; the observed `get_usage_limits` response is account-level. External-client attachment to the current Desktop thread is therefore the exact missing Codex probe.

### C2. Claude Code telemetry is promising, but model time is not agent time

[Anthropic's Claude Code monitoring reference](https://code.claude.com/docs/en/monitoring-usage) documents per-API-request input/output/cache tokens, estimated `cost_usd`, `duration_ms`, `session.id`, `query_source` and effort. `query_source` includes main, compaction and subagent work; a session-wide request sum could include multiple sources while a parent aggregate may already represent them. `duration_ms` measures the API request, not the whole agent's tool/wait cycle. Its `session.id` can change on `/clear`, and resumed `event.sequence` may repeat, so a TFW join needs explicit launch lineage and timestamps. No live Desktop Code exporter record was obtained. The standalone Claude Code CLI returned `Not logged in · Please run /login` on an isolated prompt; it proves only that this CLI entry point cannot use the Desktop subscription as-is, and no login was attempted.

### C3. Antigravity hook identity survives; numeric join does not

The [official Antigravity 2.0 hooks schema](https://www.antigravity.google/docs/hooks/) names `conversationId`, `modelName`, `PreInvocation`, `PostInvocation` and `Stop`, but the documented `PostInvocation` input has no usage count. [Google's SDK announcement](https://antigravity.google/blog/introducing-google-antigravity-sdk) says SDK `usage_metadata` has per-turn and cumulative prompt/candidate/cache/thinking counters; those SDK fields do not establish the 2.0 Desktop export. The adjacent `agy` CLI diagnostic timed out with `num_turns: 0` and all-zero usage, so it cannot be used to prove zero-cost work or success. C2 requires a supported Desktop numeric export with the same conversation ID, which remains unidentified.

### C4. Fresh Desktop attempt and exact access result

The `computer-use` API listed the running 2.16.0 Antigravity window, Claude Desktop 2.9939.2 window and Codex Desktop window. `sky.launch_app({app: 'Google.Antigravity'})` created a second window from the separate `D:\AI\Antigravity` installation, not a new 2.16.0 window. Launching the exact 2.16.0 executable through the API left the targetable-window list unchanged. Launching the Claude Desktop app ID likewise left only its existing window. An attempted state capture of the newly launched older Antigravity window produced inconsistent visual/accessibility targeting; it was discarded and no visible session material was used as evidence. Existing windows were not inspected further or used for prompts because they may contain unrelated work. Thus the attempted operation and observed result are specific: this control path did not yield a reliably isolated fresh session on either exact installed Desktop surface. No task-owned Desktop turn with nonzero numeric output was captured. No persistent app/account setting was changed.

### C5. Owner-directed `agy` CLI capture — observed, with a changed surface boundary

The owner directly instructed this Researcher task to “use agy cli instead GUI” after Extract. GUI attempts stopped. In a fresh temporary directory, the exact command `agy -p 'Reply with exactly: TEQM probe.' --output-format json --print-timeout 90s` using installed `agy 1.2.8` exited `0` and returned `status: SUCCESS`, `num_turns: 1`, `duration_seconds: 9.0384367`, `conversation_id: db5a20bc-3c44-4166-8014-2be057d30e75`, `input_tokens: 18136`, `output_tokens: 98`, `thinking_tokens: 94`, `cache_read_tokens: 0`, `total_tokens: 18234`. The response text itself was not retained in the stage record. A separate `agy -p /model` read returned current default `gemini-3.8-flash-high`; the completed run did not pin `--model`, so that later read is contextual rather than proof of the exact run model. No persistent setting, authentication or other session was touched.

The [official Antigravity CLI headless reference](https://antigravity.google/docs/cli/headless/) says a terminal JSON result reports cumulative session usage and duration; streaming mode has per-step usage and a final result. Here `18136 + 98 = 18234`, so adding `thinking_tokens: 94` again would double-count a reported subcategory. This is a real, completed, nonzero numeric capture for one fresh CLI session. It is not evidence for Antigravity 2.16.0 GUI, for child-session inclusion, for a tariff charge, or for arbitrary task/role attribution. The recorded CLI `conversation_id` can be joined to a task-owned launch record in a later pilot; that join must be tested rather than assumed. The Coordinator was notified of the owner's changed surface preference so any frozen HL boundary is resolved by its authorized route.

### C6. Time, money and coverage counterexamples

- Two parallel role intervals 10:00–12:00 and 11:00–13:00 sum to four role-hours while the calendar union is three hours. Both can be true; neither is agent idle time. Tool durations inside those intervals are not an extra addend.
- A price-by-token estimate cannot be produced from a quota percentage, a model name alone, or Antigravity's all-zero timed-out CLI record. [Claude Code's cost documentation](https://code.claude.com/docs/en/costs) distinguishes local usage estimates from actual billing; a subscribed Desktop user may have no marginal provider charge for a given turn.
- A period view needs observations whose consumption occurred in that period. A completed task that spans periods still needs its entire lifetime for task cost. A monthly subscription allocation requires an eligible pool beyond the two pilot products if the same account serves other use.

## Checkpoint

| Found | Remaining |
|---|---|
| C7 has an exact existing TFW thread key and a documented token-update event; local CLI schema confirms separate `total` and `last` fields. | Demonstrate supported attachment to the *working Desktop thread* and capture a completed numeric update plus turn interval; verify child-thread inclusion and effective model. |
| C5 has documented per-request tokens, estimate, duration, session identity and subagent source in Claude Code. | Obtain a fresh authenticated Desktop Code session with process-scoped OTel export, then test a child request and agent execution interval without persistent shared config. |
| Antigravity 2.0 hooks provide identity but no documented usage payload. | Find and observe a supported 2.0 Desktop numeric source joined by `conversationId`, or mark that surface partial. |
| Owner-directed Antigravity CLI returned one completed session with token categories, duration and `conversation_id`. | Verify explicit model pinning, role launch join, retries/child use and cumulative-versus-per-step behavior; settle whether CLI is an owner-approved substitute for the HL's exact Desktop boundary. |
| Fresh-window attempts and adjacent CLI failures are recorded precisely. | A controlled new Desktop session or a supported task-owned event interface is still needed; no global or unrelated-session scrape is authorized. |

**Challenge decision:** C11 is now the first *demonstrated local capture route* for a single Antigravity CLI session, following the owner's direct steering. Its supported JSON result exposes nonzero tokens, duration and a conversation key. It does not yet satisfy full task/role coverage or prove the frozen Desktop-surface claim; the Coordinator must resolve the scope effect. C7 (Codex Desktop App Server thread events) is the next candidate for exact Desktop capture, and C5 (Claude Desktop Code OTel) is a conditional fallback. C1/C9 retain explicitly partial timing; C2 remains conditional on a 2.0 GUI numeric export. H1 has narrow CLI evidence but remains open for the full three-surface/task-role requirement. H4 remains unproven because the successful CLI result included no charge or tariff basis. Iteration 2 should test C11's join and counter behavior while the Coordinator resolves its authority, then continue the exact Desktop checks still required by the approved HL.

**Sufficiency:**
- [x] External primary sources used in this stage.
- [x] Briefing decision gap closed for iteration 1: one first candidate, one fallback, exact failed attempts and next checks are named without claiming success.
- [x] All ten dimension pairs checked; material incompatibilities and surviving configurations listed.

**Material handover:** Producer Researcher; recipient exact parent Coordinator. Source/epoch: linked official pages fetched 2026-09-28; installed Codex CLI 0.152.1 generated schema, app-launch attempts and Antigravity CLI 1.2.8 probe on that date. Inspected scope: task-owned dispatch IDs, public schemas, fresh-window metadata, generated type declarations and one new CLI session; no unrelated transcript or content used. Material: `agy` CLI produced one completed, nonzero session token/time record after the owner's direct surface steering; no exact Desktop route did. Uncertainty: CLI task/role and child binding, exact run model/price, Desktop event attachment, and whether owner steering changes frozen HL coverage. Continuation: the Coordinator resolves that scope issue and prepares iteration 2 to validate the demonstrated CLI route plus remaining Desktop coverage or exact prerequisites.

Stage complete: YES
→ User decision: Close Challenge and permit synthesis, or request one specific correction.
