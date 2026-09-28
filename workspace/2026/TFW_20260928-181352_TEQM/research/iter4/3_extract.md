# Extract — "What do we NOT see?"
> **Mindset:** Analyst. Combine Gather's dimensions without granting a route its missing join or semantics.
> **Task / producer:** `TFW_20260928-181352_TEQM`, iteration 4; Researcher `codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243`.
> **Parent Coordinator / return:** `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793`; `tfw-gates-only` / `native-gates`.
> **Authority / selection:** A1 HL freeze `7db1148c057300e06f639696544913d3d067031e`; Gather advance `2c4efce30dc0f0681b9152f144cb3727c20a6cde`; focused mode.
> **Evidence epoch:** accepted iteration-1–3 returns and official product documentation checked 2026-09-28; configuration rows are designs to challenge, not observed full integrations.

## Configuration Space

The headers preserve Gather's six dimension names. The table lists distinct, internally possible combinations rather than the full Cartesian product; a source may support only a partial report.

| Config | D1. Numeric source and surface | D2. TFW unit binding | D3. Counter meaning | D4. Time meaning | D5. Money basis | D6. Product-area evidence |
|---|---|---|---|---|---|---|
| C1 | AGY CLI terminal JSON | Explicit task/role dispatch to one fresh CLI conversation | Cumulative *final* session result | Task-owned invocation start/end, with CLI duration separately | Unknown until effective model/category/rate | Purpose/result + controlled vocabulary and correction |
| C2 | AGY CLI `stream-json` step updates plus final result | Explicit dispatch plus stream `conversation_id`; `subagent_info` child IDs if emitted | Per-step event usage, final cumulative result as reconciliation only | Wrapper event receipt/begin/end; provider step duration separately | Dated tariff only if category/model basis is proved | Purpose/result + task changes/revisions + vocabulary |
| C3 | Antigravity IDE internal SQLite `gen_metadata` | IDE conversation ID joined to role dispatch; reported parent link separately checked | Per-row encoded fields with version-specific descriptor/inclusion rule | Reported model latency plus separately evidenced tool/role intervals | Unknown or later dated tariff | Purpose/result + task changes/revisions |
| C4 | Claude Code CLI final JSON | Explicit task/role launch and CLI session ID | Completed session counters and per-model breakdown | CLI invocation wall time; API time separate where exposed | CLI list-cost estimate, not subscription charge | Purpose/result + controlled vocabulary |
| C5 | Claude Code OTel request/active-time events | Session ID + task launch + agent/parent attributes | Per-request additive tokens with source partition | `active_time.total` `type=cli` versus request durations | Estimated OTel cost; billing separate | Purpose/result + task changes/revisions |
| C6 | Codex Desktop App Server turn/token events | Exact TFW thread and turn IDs from task routing | `last` or validated cumulative delta, subject to live semantics | Turn lifecycle interval, separately labeled from tool time | Dated tariff if effective model/categories/rate | Purpose/result + task changes/revisions |
| C7 | Claude Code-tab own `get_usage`/`get_session` | Existing own session ID joined to task role | Compactable context occupancy, not consumed tokens | Sample timestamps or task calendar elapsed | Unknown; account quota is not money | Purpose/result + human correction |
| C8 | TFW task-owned dispatch/close timestamps alone | Exact task/phase/role from local routing | No provider token count | Wrapper or calendar interval, precisely labeled | Unknown | Purpose/result + controlled vocabulary |
| C9 | Task-local provisional observation ledger joining several source rows by exact event key | Explicit role dispatch plus provider session/child lineage | Store leaf events or one final cumulative snapshot per source, never both as addends | Separate agent execution intervals, model/API spans and task elapsed | Parallel *labeled* estimate, allocation or unknown views | One close-time classifier and correctable primary area |

**New combination surfaced by Extract:** C2 pairs AGY's documented per-step stream with task-owned receipt timestamps and uses its final cumulative result only as a checksum. Briefing considered CLI session capture but not this period-boundary/event-reconciliation combination. The [official headless reference](https://antigravity.google/docs/cli/headless/) documents `step_update` usage, final cumulative `usage`, `--json-schema`, explicit `--model` and `subagent_info` child conversation IDs. It does not state whether child tokens are included in parent totals, so C2 cannot infer that inclusion.

## Findings

### E1. One `economics.md` needs source rows before totals

The HL §3 contract permits one Markdown file with a machine-readable block and readable report. A candidate structured block has these groups; every absent value is explicitly `unknown`, `unavailable` or `inapplicable`, never numeric zero by default.

| Group | Minimum fields and source | Why retained |
|---|---|---|
| `identity` | task ID; phase ID or root; product ID; effective TFW version/mode; status/result and revision source | A report is about one governed unit and its outcome, not an account period. |
| `observations[]` | unique observation key; source surface/version and source ref; capture time; provider thread/session/turn/step/request ID; parent ID where observed; exact role unit and dispatch ref; effective model if observed | Supports deduplication, provenance, role binding and version-sensitive interpretation. A path or account identity alone is insufficient. |
| `raw_usage` + `semantics` | provider's raw token fields and reported total; whether each is request, step, session cumulative or gauge; documented/observed/unknown inclusion rule; cache/thinking categories | Prevents rewriting an unexplained field into a billable category. Retains the raw record for later correction. |
| `intervals[]` | start/end or duration, clock/source, interval type (`agent_execution`, `model_request`, `tool`, `task_elapsed`), coverage, overlap/nesting rule | Allows role-time sums and calendar elapsed to remain different quantities. |
| `money[]` | figure if any, currency, `observed_charge` / `tariff_estimate` / `subscription_allocation` / `unknown`, exact model, rate source and effective date or allocation pool/policy, covered observation IDs | Prevents list estimates from becoming invoices or being added to subscription allocations for the same consumption. [Claude cost guidance](https://code.claude.com/docs/en/costs) calls its local token-based dollar figure an estimate. |
| `coverage` | expected launched units/sessions, included observation keys, missing/ambiguous children, capture start/end, known resets and partial reason | A parent total is meaningful only against its actual denominator. |
| `classification` | controlled vocabulary revision, 3–5 supported keywords, primary area or `shared`/`unclassified`, evidence refs, correction, classifier invocation observation key | Tags are search facets; exactly one area receives additive task cost. Classifier overhead is included once. |

The readable portion can display period/lifetime figures, role/phase drill-down, source-strength labels and a concise limitations line derived from these rows. Root `economics.md` references phase-owned observation keys and adds root-only coordination/classifier observations; phase files retain their own leaf keys. A report total is a projection over unique leaf keys, not phase totals plus the same leaves. A provisional task-local ledger (including a provisional `economics.md` variant) is a possible way to retain ongoing-period observations before terminal finalization; the exact storage/update mechanics remain for the TS and must not create a second competing report authority.

### E2. Exact-once aggregation and period attribution require event grain

The rollup key must include source surface/version, native event identity and its owning role/dispatch. For a **per-request or per-step** source, count each completed leaf once; for a **cumulative session** source, use a validated successive delta or one final snapshot for the same interval. Do not add AGY `step_update` usage to its cumulative `result`, or Codex `total` snapshots to each other. A child's event is included only if a verified inclusion rule says it is not already inside the parent counter; otherwise show an unresolved overlap. Claude's [OTel reference](https://code.claude.com/docs/en/monitoring-usage) expressly says its subagent `total_tokens` field is the *final request footprint*, not the run total; it cannot be added as a child-run total.

Period spending selects dated leaf consumption. A session-final-only result that spans two selected periods cannot honestly split its tokens by date; assigning the whole result to its close period would be a policy, not observed period consumption. Per-step/request timestamps, a validated boundary snapshot, or a visibly partial period row are required. Task lifetime then sums the same unique leaves across all periods, including ongoing or unsuccessful work. An illustrative Challenge case will use one task with 100 tokens before a boundary and 150 after: lifetime 250, period rows 100 and 150 only if both leaf times are observed. With only a final 250, both period figures remain unallocated/partial.

For time, two parallel role intervals 10:00–10:10 and 10:05–10:12 yield **17 role-minutes** but **12 calendar minutes** of their union. A model request or tool span inside either role interval is detail, not another addend. A noninteractive, task-owned CLI invocation can supply a *defined wrapper execution interval* if its start/end, permission waits and terminal state are recorded; the provider's model/API duration remains a different field. This bounded interpretation is a candidate for C1/C2/C4, not a claim that every Desktop turn exposes agent execution time.

### E3. Classifier output is another measured role/helper observation

A single close-time classification call could take only the task's purpose, result, task-owned changes/revisions and a small controlled product vocabulary. It would return a primary area or `shared`/`unclassified`, and 3–5 terms tied to supplied evidence. [AGY headless `--json-schema`](https://antigravity.google/docs/cli/headless/) documents a structured terminal result with the enforced schema, usage, duration and `conversation_id`; this is a candidate for a bounded trial under the owner's CLI steering. Schema validity alone cannot prove that terms describe the product feature correctly. A manual correction changes labels and primary area without multiplying captured resource cost or retroactively changing raw usage. The classifier's own session/turn, tokens, time and any qualified estimate must appear once in `observations[]`.

No owner threshold for acceptable classifier operating cost or correction rate is in the accepted returns. Challenge can measure one case and report the exact observed burden; it cannot declare global H3 success from one compliant JSON object. The existing HL product-vocabulary citations provide permitted context without opening another role's private transcript.

### E4. Route prerequisites remain different by exact surface

| Route | Present evidence | Missing before a full pilot claim |
|---|---|---|
| AGY CLI C1/C2 | Iter1 completed nonzero session result; public `stream-json`/child-ID/schema contract. | One task-owned launch/stream with explicit effective model, role and any child IDs; test final versus step reconciliation, agent interval and period timestamp policy. |
| Antigravity IDE C3 | Iter3 own-session encoded rows and arithmetic; public hooks expose conversation ID. | Independently grounded field labels, version portability, read-only collector scope, task/child join, tool/agent interval and applicable price. WAL's general reader property is insufficient alone. |
| Claude CLI C4 / OTel C5 | Iter1 completed CLI record; official OTel token/cost/active-time fields. | Role/child coverage and process-scoped capture, with actual launch flags; no proof of attachment to iter2's Code-tab session. |
| Codex Desktop C6 | App Server event documentation and adjacent generated CLI schema; exact task thread route. | Supported live event access to this Desktop thread and validation of `total`/`last`, child threads, model and turn/agent interval. |
| Claude Code-tab C7 / TFW-only C8 | Exact own-session identity or task-owned lifecycle time. | No consumed-token or dollar amount follows from occupancy/quota/timestamps alone; report remains explicitly partial. |

## Checkpoint

| Found | Remaining |
|---|---|
| Nine configurations cross Gather's exact six dimensions; C2 adds the new per-step/period reconciliation combination. | Challenge a bounded AGY stream and classifier run if access is available; test child/role joins or retain exact unknowns. |
| One-file contract separates raw observations, semantics, intervals, money, coverage, classification and derived display. | Test event keys, cumulative resets, parent/child inclusion and phase/root references against concrete cases. |
| Session-final totals alone cannot allocate a cross-period task; context occupancy cannot substitute for consumed tokens. | Verify per-step timestamp/coverage and price applicability before choosing a first supported path. |

**Extract decision:** Challenge will attack C2 as the most concrete prospective CLI path, C3 as a higher-granularity but internal-schema path, and C6 as the conditional exact Codex Desktop path. C4/C5 remain Claude alternatives; C7/C8 are labeled partial. It will test H2 arithmetic and one bounded H3 classifier case, and may return a prerequisite rather than claim DoD-1 if role/time evidence remains incomplete. The Coordinator's Gather gate limits the first pilot to one demonstrated supported path; it does not require all three implementations.

**Sufficiency:**
- [x] External primary sources used in this stage (linked Antigravity CLI structured/stream reference, Anthropic cost/OTel reference and OpenAI App Server documentation checked 2026-09-28).
- [x] Briefing gap closed for Extract: a concrete single-file record, multi-period/role algebra, classifier overhead and route prerequisites are articulated for Challenge.
- [x] Configuration Space uses all six Gather dimension names; C2 makes a previously unproposed combination visible.

**Material handover:** Producer Researcher; recipient exact parent Coordinator. Source/epoch: accepted iteration-1–3 returns, current HL/gates and linked official pages checked 2026-09-28. Inspected scope: public docs and selected task artifacts only; no another-unit live session or transcript. Material: a report needs leaf observation identity and semantics before totals; AGY's documented stream could potentially provide period grain and child IDs, while its terminal result is cumulative; one classifier invocation is itself chargeable/observable work. Uncertainty: live stream behavior on this installation, child inclusion, effective model/rate, internal IDE field labels and native Codex Desktop access. Continuation: Challenge performs one bounded disconfirmation pass and reports unsupported prerequisites rather than filling gaps from adjacency.

Stage complete: YES
→ User decision: Close Extract and permit Challenge, or request one specific correction.
