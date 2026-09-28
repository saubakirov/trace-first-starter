# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260928-181352_TEQM](../../HL-TFW_20260928-181352_TEQM.md)
> Goal: Measure tokens, time, quality, and attributable cost for TFW work across roles and product areas.
> Producer unit: `antigravity:thread:local:b022b050-c6ce-450a-a406-257fbf471601`
> Parent Coordinator: `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793`
> Activation / dispatch source: owner-direct `/tfw-research TEQM` via Antigravity session `b022b050-c6ce-450a-a406-257fbf471601`; HL §4.1; `iterations.yaml` iter 3
> Coordination authority: `HL-TFW_20260928-181352_TEQM.md @ 36c100b1d6e246fbdb45ec7a2341bb652ca80b7a`
> Originating proposer: `none`

## Research Plan

### Gather
- Identify exact running Antigravity IDE version (`Antigravity.exe`, `language_server.exe`) and compare with CLI (`agy`).
- Inspect this session's accessible numeric metadata and storage artifacts: SQLite database `C:\Users\c0rpa\.gemini\antigravity\conversations\<conversation-id>.db`, summaries DB, and transcript JSONL.
- Investigate supported lifecycle hooks (`hooks.json`: `PreToolUse`, `PostToolUse`, `PreInvocation`, `PostInvocation`, `Stop`) and payload contracts.

### Extract
- Decode internal protobuf representations in `gen_metadata` and `steps` tables to isolate token categories (prompt, candidate/output, thinking, cache) and timing fields.
- Formulate configuration space for Antigravity session capture (Direct SQLite read, Lifecycle Hooks + SQLite join, Transcript JSONL parse, or Headless CLI execution).
- Compare capture fidelity, overhead, and reliability between Antigravity IDE runtime and `agy` CLI.

### Challenge
- Stress-test counter inclusion arithmetic: verify whether thinking tokens are part of candidate/output tokens or separate, and whether prompt tokens report fresh vs cached tokens.
- Evaluate execution interval and duration semantics (generation latency vs tool execution vs session elapsed time).
- Challenge money attribution: distinguish absence of direct billing charge in Antigravity storage from tariff-based estimation.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | At least one of the exact Antigravity, Claude Desktop or Codex surfaces can expose task/role-bound tokens and execution intervals with sufficient coverage; each platform's availability is assessed separately. | open |
| H4 | A useful money view can be grounded in known model/token categories and a declared price or payment basis. | open |

## Scope Intent
- **In scope:** Antigravity IDE 2.17.0 self-inspection in session `b022b050-c6ce-450a-a406-257fbf471601`; exact token counters (input, cached, output, thinking); generation and session timing; hook payload contracts; comparison with `agy` CLI 1.2.12; capture route for `economics.md`.
- **Out of scope:** Inspecting Claude Desktop (iter 2) or Codex (iter 1/4); persistent modifications to application binaries or user settings; paid billing changes.

## Guiding Questions
1. Does the live Antigravity IDE session record per-turn token usage and timing in accessible local storage?
2. What are the exact counter inclusion rules for thinking tokens and prompt caching in Antigravity?
3. How can a task collector join these records to TFW task, phase, and role lifecycles?

## User Direction
User instruction at launch: `/tfw-research TEQM возьми там свою итерацию на проверку себя здесь, вопросов не задавай доводи ресерч iter 3`. The owner explicitly requested zero interactive questions and directed autonomous completion of iteration 3 through RES.

---
Stage complete: YES
