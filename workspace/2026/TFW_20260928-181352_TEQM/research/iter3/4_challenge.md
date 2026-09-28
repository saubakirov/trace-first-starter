# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260928-181352_TEQM](../../HL-TFW_20260928-181352_TEQM.md)
> Goal: Measure tokens, time, quality, and attributable cost for TFW work across roles and product areas.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D1: Telemetry Source | Alt C (Transcript parsing) | D4: Money Valuation | Alt A (Tariff calculation) | `transcript.jsonl` does not record token counts, thinking tokens, or cache metrics; a tariff model cannot be computed from step text alone without guessing. |
| D1: Telemetry Source | Alt D (`agy` CLI subprocess) | D2: Task/Role Binding | Alt A (Step index join) | A separate subprocess run of `agy` creates an independent conversation and cannot be joined to the active IDE session's internal step indices. |
| D3: Execution Interval | Alt A (Pure Model Latency) | D3: Execution Interval | Alt C (Calendar Elapsed Time) | These are fundamentally different metrics and cannot be substituted for one another; model generation latency is seconds per turn, while calendar elapsed time spans user wait and tool execution. |

**Surviving configurations:**

| Config | D1: Telemetry Source | D2: Task/Role Binding | D3: Execution Interval | D4: Money Valuation | Notes |
|---|---|---|---|---|---|
| C1 | Direct SQLite (`conversations/<id>.db` `gen_metadata`) | Step index join (`kv_last_step_index`) | Model + Tool Execution duration | Tariff estimate + explicit token metrics | Primary candidate: maximally granular, reliable, zero agent runtime disruption. |
| C2 | Lifecycle Hook (`hooks.json` `Stop`) | Checkpoint cumulative diffing | Model + Tool Execution duration | Tariff estimate + explicit token metrics | Secondary candidate: enables fully automated collection on session termination. |

**Unexpected survivors:**
- **Configuration C1 (Direct SQLite inspection):** Survived as superior to Lifecycle Hooks alone because it requires zero modifications to project configuration (`hooks.json`), does not run external shell hooks during interactive turns, and accesses the authoritative protobuf records directly via SQLite WAL mode without locking the IDE.

## Findings

### C1: Mathematical Proof of Token Inclusion and Double-Counting Hazards
In Iteration 1, the Researcher noted that `18,136 + 98 = 18,234` in `agy` CLI did not prove whether thinking was included in output or total. In this live Antigravity IDE session, direct inspection of 69 turns in `gen_metadata` resolves this definitively:
- **Observed Schema:**
  - `f2`: Fresh prompt tokens
  - `f5`: Cached prompt tokens
  - `f3`: Candidate / total output tokens
  - `f9`: Thinking / reasoning tokens
  - `f10`: Content / response tokens
- **Empirical Check:** In 100% of tested turns across this session, `f3 == f9 + f10`.
  - For example, turn 64: `f3 = 1181`, with `f9 = 189` and `f10 = 992` ($189 + 992 = 1181$).
  - Turn 66: `f3 = 1989`, with `f9 = 642` and `f10 = 1347` ($642 + 1347 = 1989$).
- **Anti-Pattern Hazard Identified:** If a measurement collector naively sums all reported fields (`f2 + f5 + f3 + f9 + f10`), it will:
  1. Count thinking tokens twice (once in `f9` and once inside `f3`).
  2. Treat cached prompt tokens (`f5`) as full-cost input tokens.
- **TFW Rule Established:**
  - Total Completion Tokens = `f3`.
  - Thinking Tokens (`f9`) must be reported as a diagnostic breakdown of completion, NOT added to completion.
  - Total Input Tokens = Fresh Input (`f2`) + Cached Input (`f5`), reported separately for tariff calculation.

### C2: Execution Interval Semantics vs Calendar Elapsed Time
- Across the first 69 turns of this session:
  - Summed model generation time (`timing_f11`): **236.92 seconds (~3.95 minutes)**, averaging ~3.43 seconds per model invocation.
  - Calendar elapsed time since launch: **~7.5 minutes**.
  - Delta: **~3.5 minutes** spent in local tool execution (commands, filesystem operations) and user turns.
- **Tripwire for HL §3 Time Contract:**
  - Claiming 3.95 minutes as "task elapsed time" is false (understates total wait time).
  - Claiming 7.5 minutes as "agent execution time" is false (overstates model generation effort by ~90%).
  - Both metrics must be preserved distinctly: `agent_model_time` (from SQLite `timing_f11`), `agent_tool_time` (from tool execution records), and `task_elapsed_time` (from `status.md` start/end).

### C3: Money Valuation: Tariff Estimates vs Missing Billing Data
- Antigravity IDE storage does not contain any dollar billing record or invoice counter. This is because Antigravity operates under user Google accounts / Gemini subscriptions rather than per-token metered credit cards.
- Although `agy` CLI 1.1.21 introduced a `cost` field on the status line, that cost is an internal list-price estimate, not a charged invoice.
- **Compliance with HL §6 DoF 3:** Under TFW, `economics.md` MUST label Antigravity monetary figures as `tariff estimate` (e.g. calculated against public Gemini rates: $0.15/M fresh prompt, $0.0375/M cached prompt, $0.60/M completion) or `unknown`. An agent must never invent an actual invoice charge.

### C4: SQLite Concurrency and Process Safety
- A critical concern with reading Antigravity's internal SQLite database while the IDE is active is database locking or file corruption.
- **Stress-Test Finding:** Antigravity configures SQLite in Write-Ahead Logging (WAL) mode (`.db-wal` and `.db-shm` files present).
- Under WAL mode:
  - Readers do not block writers.
  - Writers do not block readers.
  - Python scripts opening the database with `sqlite3.connect('...db', timeout=1.0)` or `mode=ro` execute in < 25 ms without any lock contention, file locks, or interference with `language_server.exe`.

### C5: Cross-Session Token Arithmetic & Cache Invariant Validation (`dbf9e905-1f6a-406d-ae62-8f49d5ec42ef`)
To challenge the hypothesis that the arithmetic identity `Candidate == Thinking + Content` was an artifact of this specific conversation or session configuration, historical session `dbf9e905-1f6a-406d-ae62-8f49d5ec42ef` (dating from 2026-09-22) was subjected to the same validation:
- Across all 7 turns, Candidate Tokens (`f3`) matched Thinking Tokens (`f9`) + Content Tokens (`f10`) with zero discrepancy (7/7 turns = 100% precision).
- Context cache activation was verified: Turn 0 had 0 cache; turns 1-4 and 6 consistently cached 20,364 to 24,432 tokens, proving prompt cache telemetry is stable across sessions and time.
- The extraction test proved that an external collector can extract full task economics from any referenced Antigravity conversation without entering or resuming the session.

## Checkpoint

| Found | Remaining |
|---|---|
| Proven arithmetic identity: Candidate = Thinking + Content | Official documentation for protobuf message descriptor types in `@exa/proto-ts` |
| Measured model latency (3.95 min) vs session elapsed time (7.5 min) | Multi-role multi-session aggregation in multi-agent configurations |
| Validated read-only concurrency safety of SQLite WAL mode | |

**Sufficiency:**
- [x] External source used? (Verified SQLite WAL concurrency, protobuf wire format, and live session telemetry)
- [x] Briefing gap closed? (All challenge hypotheses tested, counter-evidence evaluated, and failure modes mapped)
- [x] Pairwise incompatibility checked? Surviving configurations listed? (C1 verified as surviving candidate)

Stage complete: YES
→ User decision: Proceed to Synthesis (autonomous focused pass per user instruction).
