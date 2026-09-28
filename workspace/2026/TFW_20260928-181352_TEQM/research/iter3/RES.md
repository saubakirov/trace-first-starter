# RES — TFW_20260928-181352_TEQM: Task Economics and Quality Measurement

> **Current filename**: `workspace/2026/TFW_20260928-181352_TEQM/research/iter3/RES.md`  
> **Date**: 2026-09-28  
> **Author**: Researcher unit (Antigravity)  
> **Status**: 🔬 RES — iteration 3 complete  
> **Parent HL**: [HL-TFW_20260928-181352_TEQM.md](../../HL-TFW_20260928-181352_TEQM.md) at `36c100b1d6e246fbdb45ec7a2341bb652ca80b7a`  
> **Mode**: Pipeline / focused  
> **Producer unit**: `antigravity:thread:local:b022b050-c6ce-450a-a406-257fbf471601`  
> **Parent Coordinator**: `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793`  
> **Activation / dispatch source**: owner-direct `/tfw-research TEQM` via Antigravity session `b022b050-c6ce-450a-a406-257fbf471601`; HL §4.1; `iterations.yaml` iter 3  
> **Coordination authority**: `HL-TFW_20260928-181352_TEQM.md @ 36c100b1d6e246fbdb45ec7a2341bb652ca80b7a`  
> **Originating proposer**: none  

---

## Research Context

Iteration 3 executes the independent Antigravity self-inspection mandated in `iterations.yaml`. Operating directly within an active Antigravity session, this research inspects the application's actual local runtime, accessible telemetry storage, and event hooks. The investigation resolves open questions left from Iteration 1 regarding Antigravity Desktop versioning, exact token accounting (especially thinking token inclusion and prompt caching), execution interval measurement, and valuation grounding. All findings are derived from direct empirical examination of local application binaries and live SQLite session databases on 2026-09-28.

## Briefing

[Briefing](1_briefing.md) scoped this investigation to Antigravity self-inspection without cross-inspecting pending Claude Desktop iteration 2 or completed Codex iteration 1. [Gather](2_gather.md) identified the host binary (Antigravity IDE 2.17.0, `language_server.exe`), central AppData storage (`conversation_summaries.db`, `<id>.db`, `transcript.jsonl`), and lifecycle hook contracts. [Extract](3_extract.md) decoded the internal binary Protocol Buffer schema in SQLite table `gen_metadata` and mapped configuration options. [Challenge](4_challenge.md) mathematically verified token inclusion identities across 69 live turns, established execution interval semantics, and verified SQLite WAL concurrency safety.

## Decisions

| # | Decision | Rationale |
|---|---|---|
| D1 | Adopt Direct SQLite extraction (C1) as the primary telemetry capture route for Antigravity. | Antigravity writes every model generation directly to `conversations/<id>.db` table `gen_metadata` in SQLite WAL mode. It is accessible to standard read-only Python scripts in <25 ms without agent interruption or process locks. |
| D2 | Treat Candidate Tokens (`f3`) as the authoritative completion total and Thinking Tokens (`f9`) as a diagnostic subcategory. | Direct protobuf decoding proves that across 100% of tested turns, `f3 == f9 + f10` (Candidate = Thinking + Content). Summing thinking to total completion would double-count tokens. |
| D3 | Separate Prompt Tokens into Fresh Input (`f2`) and Cached Input (`f5`). | Protobuf telemetry explicitly isolates fresh prompt tokens (`f2`) from context-cached tokens (`f5`). Accurate economic modeling requires reporting both categories to reflect pricing discounts. |
| D4 | Measure Model Generation Time (`timing_f11`) and Tool Execution Time distinctly from Task Elapsed Time. | In this live session, pure model generation took 3.95 minutes across 69 turns, whereas elapsed session time was ~7.5 minutes. Conflating model time with elapsed time misrepresents agent effort by ~90%. |
| D5 | Label Antigravity financial figures in `economics.md` as `tariff estimate` or `unknown`. | Antigravity IDE storage does not contain a billing charge field. While `agy` CLI exposes an estimated `cost` field on its status line, neither reflects a direct marginal invoice. Actual money must be computed via explicit tariff models. |

### Antigravity Capability Matrix (Observed vs Iteration 1 Baseline)

| Telemetry Dimension | Iteration 1 Report (Preliminary) | Iteration 3 Verified Reality (Empirical) |
|---|---|---|
| Application Identity | Antigravity 2.16.0 (inferred/unverified) | **Antigravity IDE 2.17.0.0** (`Antigravity.exe`), backed by `language_server.exe` (2.17.0) |
| Adjacent CLI Identity | `agy 1.2.8` | **`agy 1.2.12`** (`C:\Users\c0rpa\AppData\Local\agy\bin\agy.exe`) |
| Numeric Storage Source | "Hooks: conversationId only; Desktop numeric unverified" | **`conversations/<id>.db` table `gen_metadata`** stores full per-turn protobuf usage |
| Token Accounting | "Thinking inclusion unknown; input + output = total" | **Proved Identity:** `f3 (candidate) = f9 (thinking) + f10 (content)`; `f2` (fresh input) and `f5` (cached input) are explicitly segregated |
| Time Semantics | "Desktop execution interval unobserved" | **Exact per-turn model duration:** `timing_f11` provides seconds (`t1`) and nanoseconds (`t2`) |
| Capture Overhead | Unknown | **< 25 ms** to read and parse 100 turns from SQLite WAL without locking IDE |
| Money Valuation | Unknown / absent | **Unpriced in storage**; tariff estimate required per rate card |

## Open Questions

| # | Question | Status | Answer |
|---|---|---|---|
| Q1 | Do child subagents share the parent conversation SQLite DB or write to separate databases? | Resolved | Each conversation (parent or subagent) receives a dedicated UUID and corresponding database `conversations/<uuid>.db`. The parent links children via `parent_conversation_id` in `conversation_summaries.db`. |
| Q2 | Are thinking tokens billed as output tokens in Gemini rate cards? | Open | Google Cloud Gemini pricing bills thinking tokens as candidate/output tokens. In Antigravity internal metadata, `f3` already includes `f9`. |
| Q3 | What is the exact public rate card to use for Gemini 3.8 Flash and Gemini 3.1 Pro tariff estimation? | Open | Standard Google Gemini API pricing provides baseline rates ($0.15/M input, $0.0375/M cached input, $0.60/M output for Flash); specific subscription-adjusted tariffs require Coordinator definition in Iteration 4. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|---|---|---|---|
| H1 | An exact named surface exposes sufficiently complete task/role tokens and execution intervals; assess each platform separately. | Proposed | 🟢 Supported for Antigravity | Antigravity IDE 2.17.0 exposes complete per-turn token breakdowns (fresh input, cached input, thinking, content) and nanosecond model latency via SQLite table `gen_metadata`. |
| H4 | Money view is grounded in known model/token categories and a declared price/payment basis. | Proposed | 🟡 Tariff-grounded | Observed token categories allow deterministic tariff estimation, but actual provider billing charges are unobserved in Antigravity storage. |

## HL Update Recommendations

The Researcher classifies these recommendations for the Coordinator; no HL text or frozen section is changed here.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|---|---|
| R1 | §2 | Update Antigravity version to 2.17.0 (IDE) and 1.2.12 (CLI). Replace "Desktop numeric data unverified" with verified local SQLite extraction via `conversations/<id>.db` table `gen_metadata`. | Gather G1/G2; Challenge C1. |
| R2 | §7.2 | Cite Antigravity SQLite schema (`gen_metadata` protobuf fields: `f2` prompt, `f5` cache, `f9` thinking, `f10` content, `f3` candidate total, `timing_f11` latency). | Extract E1; Challenge C1. |
| R3 | §8–§9 | Resolve Antigravity capture feasibility risk. Note that money view for Antigravity is restricted to tariff estimation and subscription allocation because local storage contains no direct billing fields. | Challenge C3. |
| R4 | §10 | Update three-platform matrix with verified Antigravity rows. Incorporate the proven arithmetic rule `Candidate = Thinking + Content` into the accounting specification. | Challenge C1; Matrix above. |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

**No amendment proposals.** Findings confirm the feasibility of the frozen §4 mandate and DoD criteria without requiring any contract modifications or scope shifts.

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|---|---|---|---|
| FC1 | process | The owner directed the Antigravity Researcher to execute iteration 3 autonomously without asking interactive questions: "возьми там свою итерацию на проверку себя здесь, вопросов не задавай доводи ресерч iter 3". | User prompt, 2026-09-28. | High |
| FC2 | environment | Antigravity IDE 2.17.0 stores per-turn model telemetry as binary Protocol Buffers in SQLite table `gen_metadata` at `~/.gemini/antigravity/conversations/<conversation_id>.db`. | Empirical inspection of live session database, 2026-09-28. | High |
| FC3 | environment | In Antigravity's internal telemetry schema, candidate tokens (`f3`) mathematically equal thinking tokens (`f9`) plus content tokens (`f10`) across 100% of observed model turns. | Empirical check of 69 turns in session `b022b050-...`, 2026-09-28. | High |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|---|---|---|---|
| SS1 | domain | Because Antigravity is delivered as a subscription/account-level service rather than pay-per-token API credits, task economics on Antigravity must rely on a standardized tariff model (rate card) applied to observed token categories. Presenting tariff calculations as "billed expenses" would mislead finance stakeholders. | Challenge C3; HL §3 Money Contract. | ★★★ |
| SS2 | process | Reading Antigravity's SQLite database directly on task or role completion is superior to injecting runtime lifecycle hooks (`hooks.json`). Direct reading incurs zero runtime latency during turns, avoids altering project workspace configurations, and provides exact historical turn replay. | Extract E2; Challenge C4. | ★★★ |

## Findings Map

```text
Antigravity IDE 2.17.0 Local Storage & Telemetry Topology
├── conversation_summaries.db
│   └── High-level session metadata (conversation_id, title, step_count, last_modified_time)
│
├── brain/<conversation_id>/.system_generated/logs/transcript.jsonl
│   └── Event sequence: user inputs, tool calls, tool results, thinking blocks, timestamps
│
└── conversations/<conversation_id>.db (SQLite WAL mode)
    ├── steps: Step payloads, permissions, error details
    └── gen_metadata (Binary Protocol Buffer per model turn)
        ├── Model: f19 ('gemini-3.8-flash'), kv_model_enum ('MODEL_PLACEHOLDER_M318')
        ├── Token Accounting (UsageMetadata):
        │   ├── f2: Fresh Input Tokens
        │   ├── f5: Cached Input Tokens (Prompt Caching)
        │   └── f3: Total Candidate Tokens
        │       ├── f9: Thinking / Reasoning Tokens  ──┐
        │       └── f10: Content / Output Tokens    ──┴──> Proved: f3 = f9 + f10
        └── Latency (timing_f11):
            ├── t1: Model Duration (seconds)
            └── t2: Model Duration (nanoseconds)

economics.md Capture Pipeline:
[Task Lifecycle / Close] ──> Read conversations/<id>.db ──> Parse gen_metadata
                         ──> Aggregate (f2, f5, f9, f10, timing) ──> Apply Tariff Rate Card
                         ──> Emit economics.md beside status.md
```

## Iteration Status

- **Iteration:** 3 of 4 (min) / 4 (max).
- **Hypotheses tested:** H1 verified for Antigravity (supported by direct SQLite telemetry); H4 clarified (tariff estimates supported, direct billing charges unobserved).
- **Hypotheses deferred:** H2, H3, and cross-platform multi-agent synthesis deferred to Iteration 4 (Codex reconciliation).
- **Gaps discovered:** Lack of direct billing dollar amounts in Antigravity storage; multi-platform unified rate sheet needed.
- **Superseded decisions:** Superseded Iteration 1 finding that Antigravity Desktop numeric telemetry is "unverified". It is now fully verified, decoded, and proved locally.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|---|---|---|
| 1 | Multi-platform reconciliation (Codex, Claude, Antigravity) | The three platforms differ in storage, token reporting, and money basis. | Iteration 4 (Codex) must reconcile Antigravity SQLite telemetry with Claude CLI/Desktop and Codex App Server findings. |
| 2 | Unified tariff rate sheet | Antigravity and Codex do not output direct billing invoices; they require reference pricing. | Standardize a versioned tariff dictionary in TFW configuration for Gemini, Claude, and OpenAI models. |
| 3 | Multi-role join mechanics | Tasks consist of multiple roles across phases. | Test joining session databases across Coordinator, Researcher, Executor, and Reviewer into root `economics.md`. |

### Recommendation

- [x] **SUFFICIENT** — Antigravity self-inspection is complete. The findings provide an exact, verified telemetry capture route. Recommend the Coordinator incorporate this return, await Claude Desktop Iteration 2, and proceed to Codex Iteration 4 for final reconciliation.
- [ ] **MORE NEEDED**
- [ ] **BLOCKED**

## Conclusion

Iteration 3 achieved a complete, verified breakthrough in understanding Antigravity's internal telemetry. Contrary to initial assumptions that Antigravity Desktop numeric data was unverified or locked behind opaque GUI layers, direct inspection of the active session proved that Antigravity IDE 2.17.0 maintains a comprehensive SQLite database (`conversations/<id>.db`) in WAL mode. Every model turn records nanosecond generation latency and an exact protobuf breakdown of fresh prompt, cached prompt, thinking, and content tokens. Furthermore, empirical analysis resolved the open question regarding thinking tokens, proving that candidate tokens strictly equal thinking tokens plus content tokens. A non-intrusive, read-only Python extraction pipeline can extract these records in <25 ms, providing a rock-solid foundation for `economics.md` on Antigravity without requiring subprocess wrappers or runtime hooks.

### Material handover at this return

Producer: Researcher `antigravity:thread:local:b022b050-c6ce-450a-a406-257fbf471601`; recipient: task Coordinator `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793` under `tfw-gates-only` / `native-gates`. Source/epoch: live Antigravity IDE 2.17.0 installation, active session `b022b050-c6ce-450a-a406-257fbf471601` storage artifacts, `agy` 1.2.12 CLI binary, and official customization documentation on 2026-09-28. Inspected scope: `%USERPROFILE%\.gemini\antigravity\`, `conversations/<id>.db`, `conversation_summaries.db`, `transcript.jsonl`, `hooks.json` specifications, and `Antigravity.exe` VersionInfo; no private user files or unrelated accounts were accessed. Material: complete SQLite protobuf extraction pipeline demonstrated; token arithmetic identity proven (`f3 = f9 + f10`); model generation latency isolated from tool and elapsed duration; tariff estimation identified as the only valid money basis for Antigravity. Uncertainty: parallel Claude Iteration 2 findings and cross-platform rate card standardization. Continuation: Coordinator integrates Iteration 3, awaits or reviews Iteration 2, and dispatches Iteration 4 in Codex for unified reconciliation.

---

*RES — TFW_20260928-181352_TEQM: Task Economics and Quality Measurement | 2026-09-28*
