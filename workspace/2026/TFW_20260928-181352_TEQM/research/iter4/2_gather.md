# Gather — "What do we NOT know?"
> **Mindset:** Explorer. Keep source, unit join, semantics and valuation as independent choices.
> **Task / producer:** `TFW_20260928-181352_TEQM`, iteration 4; Researcher `codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243`.
> **Parent Coordinator / return:** `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793`; `tfw-gates-only` / `native-gates`.
> **Authority / selection:** A1 HL freeze `7db1148c057300e06f639696544913d3d067031e`; continuation `c9a8ea1df7c0e364d3ed1e1a2a7de465442898eb`; Briefing approval `ee21a6f1933a8affd49f31dce2007bdab565f91e`; focused mode.
> **Evidence epoch:** accepted iteration-1–3 artifacts at the Coordinator's cited revisions and official documentation checked 2026-09-28. The source returns are evidence *about* their own sessions; this Researcher did not access their private live sessions or transcripts.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1. Numeric source and surface | Native task-owned event/terminal JSON with documented fields | Native app's internal local storage with version-specific decoding | Session context-occupancy or account-quota gauge | Task-owned timing/identity record with no provider numeric source |
| D2. TFW unit binding | Explicit task/phase/role dispatch to a newly launched session ID | Existing native thread/session ID reconciled to task routing and lineage | Provider parent/child conversation link plus independently captured TFW role | Workspace, account or calendar coincidence without a unique join |
| D3. Counter meaning | Additive per-request/per-turn consumption event | Cumulative session total or validated delta | Compactable context occupancy gauge | Undocumented encoded field with observed arithmetic only |
| D4. Time meaning | Model/API request duration | Whole agent execution interval, with non-overlapping tool/model/wait classification | Task calendar elapsed time | Account period or quota-reset window |
| D5. Money basis | Observed provider charge | Dated model/token tariff or provider list-cost estimate | Allocated subscription cost over a declared eligible pool | Unknown or quota-only |
| D6. Product-area evidence | Task purpose/result and close record | Task-owned change and revision evidence | Controlled product vocabulary and human correction | File path or generic model labels alone |

These alternatives are intentionally unselected. The same report may carry more than one *labeled* observation, but it may not silently substitute one meaning or add two valuations of the same consumption.

## Findings

### G1. Accepted returns are three different observation scopes

| Source/epoch | Directly returned observation | Claim still needing evidence or qualification |
|---|---|---|
| Iteration 1, AGY CLI 1.2.8 and Claude Code CLI 2.1.283, 2026-09-28 | One completed AGY terminal JSON record with `conversation_id`, token categories and cumulative session duration; one completed Git Bash Claude CLI result without `--bare` with session/model/token categories, duration and `costBasis: list`. | The result IDs were not proved to cover every TFW role/child/retry. CLI records do not become Antigravity or Claude Desktop records. AGY thinking/cache inclusion and exact run model were not settled. [Iter1 RES](../iter1/RES.md). |
| Iteration 2, Claude Code-tab own session, 2026-09-28 | Two `get_usage`/`get_session` samples preserved one session/model ID and context occupancy `134,884 → 147,756`; queried tools returned no input/output/cache/thinking consumption or dollar field. | The difference `12,872` is context growth, not a demonstrated token-consumption count or agent-time rate. No child was run. Its claimed absence applies to these queried tools, not every possible Desktop exporter. [Iter2 Gather](../iter2/2_gather.md); [RES](../iter2/RES.md). |
| Iteration 3, Antigravity IDE 2.17.0 own session, 2026-09-28 | The producer reported 69 `gen_metadata` rows in its own per-conversation SQLite file, with encoded fields, numeric examples and an equality `f3 = f9 + f10` on those rows; it reported a model-duration sum `236.92 s`. | Arithmetic does not name the fields or establish billable categories, exact agent time, child coverage, portable schema or read-only collection cost. A reported parent link in `conversation_summaries.db` remains to be demonstrated with a bounded role join. The `2.16.0`/`2.17.0` and CLI `1.2.8`/`1.2.12` values are observations at different epochs, not conflicting measurements of one binary. [Iter3 Gather](../iter3/2_gather.md); [Challenge](../iter3/4_challenge.md); [RES](../iter3/RES.md). |

The Coordinator accepted iterations 2–3 as research inputs with these qualifications in HL §10, not as approval of their implementation choices. Iteration 3's local `file:` customization citation is an artifact-local source, not an independently verified public descriptor for its protobuf labels; this Gather does not reread that private file or another unit's SQLite/transcript.

### G2. Primary documentation establishes narrower boundaries

- [Codex App Server](https://learn.chatgpt.com/docs/app-server) documents turn start/completion and `thread/tokenUsage/updated` for an active thread. The separate local `codex-cli 0.152.1` generated schema in iteration 1 distinguishes `total` and `last` token breakdowns. This task's exposed tools currently show only account-level `get_usage_limits` for usage; no thread-token retrieval method appeared in the current callable catalog. A live event from this working Desktop thread is still unobserved.
- [Claude Code monitoring](https://code.claude.com/docs/en/monitoring-usage) documents request tokens, estimated `cost_usd`, request `duration_ms`, session ID and `claude_code.active_time.total` with `type=cli` for processing and `type=user` for human activity. It also documents `agent_id`, `parent_agent_id`, `query_source` and version-gated trace fields. Its subagent `total_tokens` is expressly the *final request footprint*, not whole-run consumption. The accepted Code-tab `get_usage` output is a different, narrower interface; no Desktop OTel attachment was observed. The HL excludes human activity time.
- [Antigravity CLI headless](https://antigravity.google/docs/cli/headless/) explicitly says `usage`, `num_turns` and `duration_seconds` in a result are cumulative over its conversation; streaming step updates coexist with those totals. The page lists `thinking_tokens` but gives no inclusion/billing rule for it. [Antigravity hooks](https://www.antigravity.google/docs/hooks/) document `conversationId` and lifecycle boundaries, with no token field in the cited `PostInvocation` input. Neither page documents the IDE's internal `gen_metadata` field names.
- [SQLite WAL documentation](https://www.sqlite.org/wal.html) supports the general possibility of concurrent readers and a writer. It does not validate the Antigravity producer's decoded schema, prove that all 69 rows were task-relevant, or turn a reported sub-25-ms read into a portable overhead bound.

### G3. Identity and interval evidence is incomplete even where tokens exist

The current TFW `status.md` and dispatch journal identify the task, exact Researcher/Coordinator units and activation. A provider conversation/session/thread ID is separately needed at launch or in a verified role-owned return. Iteration 1 obtained two fresh CLI IDs; iteration 2 obtained a stable Code-tab session ID; iteration 3 reported an IDE conversation ID and possible parent link. None of these alone proves every phase/role/retry observation is included in a root task exactly once. Workspace path, account quota and a later aggregate cannot repair a missing child mapping.

HL §3 requires **agent execution intervals** and separate **task elapsed** time. AGY CLI cumulative `duration_seconds`, Claude CLI `duration_ms`, Claude OTel API duration and Antigravity `timing_f11` model latency are not interchangeable with a complete agent interval. Tool and model spans may overlap or nest; elapsed minus their sum is not observed idle time. Parallel roles can have summed role time greater than task calendar duration. The available returns do not yet demonstrate a whole-role execution interval with a defined begin/end and wait policy.

### G4. Money and product classification remain separate from capture

The observed Claude CLI `costBasis: list` is a list-cost estimate. The accepted Antigravity IDE return has no observed bill field; its proposed general Flash rates were not verified for the reported `gemini-3.8-flash` model or subscription in HL §10. An account quota percentage cannot be back-converted into task tokens or dollars. A tariff needs the exact effective model, category semantics, applicable dated rate and currency. Subscription expense needs an eligible pool that includes other use; it cannot be added to the same usage's tariff estimate as a single bill.

HL §3 already fixes 3–5 product-specific keywords, one primary area or shared/unclassified state, and one close-time model invocation whose overhead belongs in the task. HL §2 cites bounded product README context and business vocabularies; no iteration-1–3 return measured a classifier. Paths alone miss deleted work, investigation and rejected approaches. Gather records three distinct inputs for Extract to combine: purpose/result, task-owned changes/revisions and a controlled vocabulary with correction. H3 remains wholly untested.

## Checkpoint

| Found | Remaining |
|---|---|
| The accepted returns and current primary docs identify numeric sources with different surfaces, units and counter meanings. | Select a first capture route only after evaluating task/role/child join and agent-time completeness; test exact Desktop Codex access if feasible without foreign-session inspection. |
| The Antigravity IDE producer observed encoded per-turn rows and one arithmetic invariant; public docs separately cover CLI totals and hook identity. | Ground or bound encoded field labels, cache/thinking inclusion, version compatibility, read-only scope and monetary model match. |
| Claude Code-tab occupancy and account quota are not consumption or money; Claude CLI/OTel are richer but separate. | Verify any child/role aggregation claim and the applicable launch/export mode. |
| The HL provides a fixed single-file report and classification requirement. | Extract an exact-once observation/report contract, exercise period/lifetime cases and one bounded classifier case. |

**Gather decision:** Extract will construct route configurations from D1–D6 while preserving each source's evidence strength. It will separate raw observations from derived reports and test the missing task/role, time, price and classification joins before Challenge selects a survivor.

**Sufficiency:**
- [x] External primary sources used in this stage (linked OpenAI, Anthropic, Antigravity and SQLite documentation checked 2026-09-28).
- [x] Briefing gap closed for Gather: accepted returns are reconciled by exact scope and six independent decision dimensions; unresolved claims are named.
- [x] Six dimensions have at least three alternatives each; no route is selected here.

**Material handover:** Producer Researcher; recipient exact parent Coordinator. Source/epoch: A1/current task controls, accepted iter1–3 artifacts at dispatch-cited revisions and linked official pages checked 2026-09-28. Inspected scope: return artifacts, current callable-tool names, HL contract and public docs; no other unit's live session, transcript or local database. Material: numeric capture exists at several scopes, but none has yet shown the complete role/child join and agent-time contract; Claude context growth is not consumed tokens; Antigravity field labels need a separate semantic basis. Uncertainty: Desktop Codex event access, Antigravity version portability, effective model/prices and H3 classifier performance. Continuation: Extract combines the six dimensions and identifies exact prerequisites for a bounded first implementation.

Stage complete: YES
→ User decision: Close Gather and permit Extract under the approved focused scope, or request one specific correction.
