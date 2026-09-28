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
| C12 | Claude Code CLI terminal JSON | Fresh CLI `session_id` recorded at task-owned launch | CLI `duration_ms`; API duration separate | CLI `total_cost_usd` and per-model `costUSD`, reported with `costBasis: list` | Claude Code CLI 2.1.283 in Git Bash | One completed local capture observed; separate from Desktop Code/Cowork/Chat. |
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

[Anthropic's Claude Code monitoring reference](https://code.claude.com/docs/en/monitoring-usage) documents per-API-request input/output/cache tokens, estimated `cost_usd`, `duration_ms`, `session.id`, `query_source` and effort. `query_source` includes main, compaction and subagent work; a session-wide request sum could include multiple sources while a parent aggregate may already represent them. `duration_ms` measures the API request, not the whole agent's tool/wait cycle. Its `session.id` can change on `/clear`, and resumed `event.sequence` may repeat, so a TFW join needs explicit launch lineage and timestamps. No live Desktop Code exporter record was obtained. The first isolated PowerShell CLI prompt returned `Not logged in · Please run /login` with zero usage. After the owner's Git Bash clarification, a Git Bash probe found that this failure depended on the CLI invocation; the completed result is detailed in C7. No login was attempted.

### C3. Antigravity hook identity survives; numeric join does not

The [official Antigravity 2.0 hooks schema](https://www.antigravity.google/docs/hooks/) names `conversationId`, `modelName`, `PreInvocation`, `PostInvocation` and `Stop`, but the documented `PostInvocation` input has no usage count. [Google's SDK announcement](https://antigravity.google/blog/introducing-google-antigravity-sdk) says SDK `usage_metadata` has per-turn and cumulative prompt/candidate/cache/thinking counters; those SDK fields do not establish the 2.0 Desktop export. The adjacent `agy` CLI diagnostic timed out with `num_turns: 0` and all-zero usage, so it cannot be used to prove zero-cost work or success. C2 requires a supported Desktop numeric export with the same conversation ID, which remains unidentified.

### C4. Fresh Desktop attempt and exact access result

The `computer-use` API listed the running 2.16.0 Antigravity window, Claude Desktop 2.9939.2 window and Codex Desktop window. `sky.launch_app({app: 'Google.Antigravity'})` created a second window from the separate `D:\AI\Antigravity` installation, not a new 2.16.0 window. Launching the exact 2.16.0 executable through the API left the targetable-window list unchanged. Launching the Claude Desktop app ID likewise left only its existing window. An attempted state capture of the newly launched older Antigravity window produced inconsistent visual/accessibility targeting; it was discarded and no visible session material was used as evidence. Existing windows were not inspected further or used for prompts because they may contain unrelated work. Thus the attempted operation and observed result are specific: this control path did not yield a reliably isolated fresh session on either exact installed Desktop surface. No task-owned Desktop turn with nonzero numeric output was captured. No persistent app/account setting was changed.

### C5. Owner-directed `agy` CLI capture — observed, with a changed surface boundary

The owner directly instructed this Researcher task to “use agy cli instead GUI” after Extract. GUI attempts stopped. In a fresh temporary directory, the exact command `agy -p 'Reply with exactly: TEQM probe.' --output-format json --print-timeout 90s` using installed `agy 1.2.8` exited `0` and returned `status: SUCCESS`, `num_turns: 1`, `duration_seconds: 9.0384367`, `conversation_id: db5a20bc-3c44-4166-8014-2be057d30e75`, `input_tokens: 18136`, `output_tokens: 98`, `thinking_tokens: 94`, `cache_read_tokens: 0`, `total_tokens: 18234`. The response text itself was not retained in the stage record. A separate `agy -p /model` read returned current default `gemini-3.8-flash-high`; the completed run did not pin `--model`, so that later read is contextual rather than proof of the exact run model. No persistent setting, authentication or other session was touched.

The [official Antigravity CLI headless reference](https://antigravity.google/docs/cli/headless/) says a terminal JSON result reports cumulative session usage and duration; streaming mode has per-step usage and a final result. The observed arithmetic is `18136 + 98 = 18234`. Neither that equality nor the cited page establishes whether `thinking_tokens: 94` is included in output or total. Preserve every raw category and the provider-reported total; do not add thinking to a derived consumption or money total without a documented rule. This is a real, completed, nonzero numeric capture for one fresh CLI session. It is not evidence for Antigravity 2.16.0 GUI, for child-session inclusion, for a tariff charge, or for arbitrary task/role attribution. The recorded CLI `conversation_id` can be joined to a task-owned launch record in a later pilot; that join must be tested rather than assumed. The Coordinator ruled the bounded CLI probe in scope without a frozen-HL amendment (gate `582d51d115403ae8b1a843d468338b4663cd5c75`); the exact surfaces remain distinct.

### C6. Time, money and coverage counterexamples

- Two parallel role intervals 10:00–12:00 and 11:00–13:00 sum to four role-hours while the calendar union is three hours. Both can be true; neither is agent idle time. Tool durations inside those intervals are not an extra addend.
- A price-by-token estimate cannot be produced from a quota percentage, a model name alone, or Antigravity's all-zero timed-out CLI record. [Claude Code's cost documentation](https://code.claude.com/docs/en/costs) distinguishes local usage estimates from actual billing; a subscribed Desktop user may have no marginal provider charge for a given turn.
- A period view needs observations whose consumption occurred in that period. A completed task that spans periods still needs its entire lifetime for task cost. A monthly subscription allocation requires an eligible pool beyond the two pilot products if the same account serves other use.

### C7. Owner-confirmed Git Bash Claude CLI — completed, with invocation sensitivity

The owner reported that Claude CLI was authenticated through the subscription inside Git Bash, correcting the earlier PowerShell-based availability inference. In a fresh temporary directory, `bash.exe -lic 'type -a claude; claude auth status --json'` resolved a user-local `claude` executable and reported `loggedIn: true`, `authMethod: claude.ai`, `subscriptionType: team`; identity fields are omitted. The installed CLI reported Claude Code `2.1.283`. The first Git Bash attempt kept `--bare`: `claude -p 'Reply with exactly: TEQM probe.' --bare --no-session-persistence --output-format json --max-turns 1`. It exited `1`, with `terminal_reason: api_error`, `Not logged in · Please run /login`, zero usage and zero cost. Thus `auth status` alone did not prove this command would complete.

An otherwise identical fresh-directory Git Bash invocation **without `--bare`** exited `0` and returned one completed turn, `duration_ms: 2810`, `input_tokens: 2`, `cache_creation_input_tokens: 9155`, `cache_read_input_tokens: 16123`, `output_tokens: 9`, `thinking_tokens: 0`, `total_cost_usd: 0.0766526`, and per-model `claude-opus-5-5` `costUSD: 0.0766526`, `costBasis: list`. `session_id` was present and its exact value is omitted from this report. The output was the requested probe phrase. No session persistence or login change was requested. The result demonstrates a nonzero local Claude **CLI** token/time/list-cost record, not a Claude Desktop Code exporter, subscription charge, or complete task/child accounting. The contrast is operationally material: collector setup should test its actual launch flags and preserve failed attempts separately from completed usage.

## Checkpoint

| Found | Remaining |
|---|---|
| C7 has an exact existing TFW thread key and a documented token-update event; local CLI schema confirms separate `total` and `last` fields. | Demonstrate supported attachment to the *working Desktop thread* and capture a completed numeric update plus turn interval; verify child-thread inclusion and effective model. |
| C5 has documented per-request tokens, estimate, duration, session identity and subagent source in Claude Code. | Obtain a fresh authenticated Desktop Code session with process-scoped OTel export, then test a child request and agent execution interval without persistent shared config. |
| Antigravity 2.0 hooks provide identity but no documented usage payload. | Find and observe a supported 2.0 Desktop numeric source joined by `conversationId`, or mark that surface partial. |
| Owner-directed Antigravity CLI returned one completed session with token categories, duration and `conversation_id`. | Verify explicit model pinning, role launch join, retries/child use and cumulative-versus-per-step behavior; settle whether CLI is an owner-approved substitute for the HL's exact Desktop boundary. |
| Owner-confirmed Git Bash Claude CLI returned one completed session with model, token categories, duration and list-cost estimate when `--bare` was omitted. | Verify task/role launch join, child coverage, cost semantics and any separate Desktop Code export; do not infer a subscription charge from `costBasis: list`. |
| Fresh-window attempts and adjacent CLI failures are recorded precisely. | A controlled new Desktop session or a supported task-owned event interface is still needed; no global or unrelated-session scrape is authorized. |

**Challenge decision:** C11 and C12 are demonstrated local capture routes for one Antigravity CLI and one Claude Code CLI session respectively, following the owner's direct steering and clarification. Both expose nonzero tokens and duration; C12 also reports a per-model list-cost estimate. Neither satisfies full task/role or child coverage or proves the exact Desktop-surface claim. The Coordinator already ruled bounded CLI research within scope without an HL amendment. C7 (Codex Desktop App Server thread events) remains the next candidate for exact Desktop capture, and C5 (Claude Desktop Code OTel) remains a conditional exact-surface route. C1/C9 retain partial timing; C2 remains conditional on a 2.0 GUI numeric export. H1 has narrow CLI evidence but remains open for the full three-surface/task-role requirement. H4 remains open because the AGY CLI returned no charge or tariff basis and Claude CLI's `costBasis: list` is not a subscription charge. Iteration 2 should test C11/C12 joins and counter/child behavior, then continue the exact Desktop checks required by the approved HL.

**Sufficiency:**
- [x] External primary sources used in this stage.
- [x] Briefing decision gap closed for iteration 1: one first candidate, one fallback, exact failed attempts and next checks are named without claiming success.
- [x] All ten dimension pairs checked; material incompatibilities and surviving configurations listed.

**Material handover:** Producer Researcher; recipient exact parent Coordinator. Source/epoch: linked official pages fetched 2026-09-28; installed Codex CLI 0.152.1 generated schema, app-launch attempts, Antigravity CLI 1.2.8 and Git Bash Claude Code CLI 2.1.283 probes on that date. Inspected scope: task-owned dispatch IDs, public schemas, fresh-window metadata, generated type declarations and fresh CLI sessions; no unrelated transcript or content used. Material: `agy` CLI produced one completed nonzero token/time record; Claude CLI produced a completed nonzero token/time/list-cost record only without `--bare`. No exact Desktop route did. Uncertainty: CLI task/role and child binding, AGY exact run model and thinking semantics, Claude list estimate versus actual subscription charge, and Desktop event attachment. Continuation: Coordinator prepares iteration 2 to validate the demonstrated CLI routes plus remaining exact Desktop coverage or prerequisites; the bounded CLI research itself needs no HL amendment per its scope ruling.

Stage complete: YES
→ User decision: Close Challenge and permit synthesis, or request one specific correction.
