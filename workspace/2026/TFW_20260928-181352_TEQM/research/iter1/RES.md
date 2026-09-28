# RES — TFW_20260928-181352_TEQM: Task Economics and Quality Measurement

> **Date**: 2026-09-28  
> **Author**: Researcher unit  
> **Status**: 🔬 RES — iteration 1 complete  
> **Parent HL**: [HL-TFW_20260928-181352_TEQM.md](../../HL-TFW_20260928-181352_TEQM.md) at `36c100b1d6e246fbdb45ec7a2341bb652ca80b7a`  
> **Mode**: Pipeline / focused  
> **Producer unit**: `codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243`  
> **Parent Coordinator**: `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793`  
> **Activation / dispatch source**: owner-approved HL §4.1; `journal/20260928-221314__dispatch__3fed.md` and `journal/20260928-221909__dispatch__f4ed.md`; command-first `/tfw-research TFW_20260928-181352_TEQM`  
> **Coordination authority**: `HL-TFW_20260928-181352_TEQM.md @ 36c100b1d6e246fbdb45ec7a2341bb652ca80b7a`  
> **Originating proposer**: none

---

## Research Context

The approved first iteration tests whether the locally available Antigravity, Claude Desktop and Codex surfaces can supply task/role-bound token and execution-time observations for the two-product economics pilot, with an explicit money basis. It compares the exact applications with adjacent CLI, SDK and account-quota routes. The owner authorized bounded local checks, then directed use of `agy` CLI instead of GUI for the Antigravity probe and clarified that Claude CLI subscription access was available in Git Bash. The Coordinator ruled the bounded AGY CLI research within the existing HL mandate without an amendment; the three named Desktop surfaces remain separate evidence rows. Sources and probes were observed on 2026-09-28; no unrelated session content was inspected.

## Briefing

[Briefing](1_briefing.md) framed H1 and H4 as the primary iteration-1 hypotheses, specified exact surface/version and task-binding checks, and deferred period aggregation and classification to iteration 2. [Gather](2_gather.md) mapped five independent dimensions: numeric source, TFW binding, time meaning, money meaning and surface coverage. [Extract](3_extract.md) combined them into conditional routes. [Challenge](4_challenge.md) rejected quota-as-task-cost and duplicate counter/time interpretations, and recorded the two completed owner-directed CLI checks.

## Decisions

| # | Decision | Rationale |
|---|---|---|
| D1 | Use AGY CLI C11 as the first *observed local session-capture candidate*; test an explicit task/role launch join before calling it task capture. | `agy 1.2.8` returned one completed JSON result with a conversation key, nonzero token categories and duration. The [official CLI reference](https://antigravity.google/docs/cli/headless/) describes cumulative result usage. Exact model, child coverage and pricing were not established. |
| D2 | Keep Claude Code CLI C12 as a second observed adjacent candidate; keep Claude Desktop Code OTel C5 and Codex Desktop App Server C7 as exact-Desktop candidates, unverified locally. | Git Bash CLI 2.1.283 returned a completed token/time/list-cost record only when `--bare` was omitted. [Claude Code monitoring](https://code.claude.com/docs/en/monitoring-usage) and [Codex App Server](https://learn.chatgpt.com/docs/app-server) document richer event routes, but no live Desktop exporter/attachment was observed. |
| D3 | Report Desktop coverage per product and mode; do not promote CLI, SDK, hook identity or account quota into a Desktop numeric claim. | [Antigravity hooks](https://www.antigravity.google/docs/hooks/) document `conversationId` and model but no usage field in the cited `PostInvocation` payload. [Claude's plugin guide](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) distinguishes Chat from Code/Cowork hooks. This task's Codex `get_usage_limits` was account-level. |
| D4 | Preserve raw counters, their source total and their semantics; do not sum snapshots or infer thinking-token inclusion from arithmetic. | Codex generated CLI schema has separate cumulative `total` and `last`; AGY's `input + output = total` does not prove whether its separately reported thinking count is included. Parent/child inclusion is unknown on both observed CLI routes. |
| D5 | Label money and time by basis: Claude CLI list-cost estimate, AGY money unknown; session duration, API duration, turn interval and task elapsed time stay distinct. | Claude CLI reported `costBasis: list`, not a subscription charge. [Claude cost guidance](https://code.claude.com/docs/en/costs) distinguishes estimates and billing. Tool/API intervals may overlap a turn; quota percentage cannot price a task. |

### Three-platform capability matrix

| Named Desktop surface | Task/session identity and numeric capture | Execution time and money | Child/retry coverage | Evidence and limit |
|---|---|---|---|---|
| Antigravity 2.16.0 | 2.0 hook schema documents `conversationId` and model; cited `PostInvocation` payload has no tokens. One separate `agy 1.2.8` CLI run observed `conversation_id`, input 18,136, output 98, thinking 94, cache read 0 and reported total 18,234. | CLI `duration_seconds: 9.0384367`; no charge field, exact run model not pinned. Desktop execution interval unobserved. | Unknown; CLI cumulative result may encompass steps, but child inclusion not demonstrated. | Desktop: documented identity / numeric unverified. CLI: one completed local observation. The CLI does not prove Desktop behavior. [Hooks](https://www.antigravity.google/docs/hooks/); [CLI](https://antigravity.google/docs/cli/headless/). |
| Claude Desktop 2.9939.2 | Chat, Cowork and Code modes differ. Code OTel documents request/session fields, but no Desktop event was captured. Separate Git Bash Claude Code CLI 2.1.283 returned a `session_id`, input 2, cache creation 9,155, cache read 16,123, output 9 and model `claude-opus-5-5`. | CLI `duration_ms: 2810`, `total_cost_usd: 0.0766526`, per-model `costBasis: list`; neither an observed subscription charge nor Desktop agent time. | OTel documents `query_source` for child/compaction; live CLI parent/child behavior untested. | Desktop: documented conditional route / numeric unverified. CLI: one completed local observation without `--bare`; the same command with `--bare` failed. [Monitoring](https://code.claude.com/docs/en/monitoring-usage); [plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude). |
| Codex Desktop 26.924.2738 | App Server documents `thread/tokenUsage/updated`; generated schema from separate `codex-cli 0.152.1` identifies thread/turn IDs and `total`/`last` token breakdowns. This task's quota tool had no thread counter. | App Server turn lifecycle and optional OTel `turn.e2e_duration_ms` are documented. No live Desktop turn-token event or task money record was captured. | Child-thread inclusion and whether current Desktop task can be observed through App Server remain unverified. | Exact Desktop event attachment unverified; CLI schema is adjacent evidence. [App Server](https://learn.chatgpt.com/docs/app-server); [OTel](https://learn.chatgpt.com/docs/config-file/config-advanced#turn-and-tool-activity). |

The AGY equality `18,136 + 98 = 18,234` is an observation only. Whether thinking 94 is contained in output or total is unknown. Neither AGY nor Claude CLI result has yet been joined to a TFW task/phase/role launch ledger, so neither satisfies full H1.

## Open Questions

| # | Question | Status | Answer |
|---|---|---|---|
| Q1 | Can a task-owned AGY/Claude CLI launch reliably bind every parent, child, retry and resumed session to one TFW role? | Open | A conversation/session key was observed in one fresh run each; multi-session coverage was not tested. |
| Q2 | What do AGY thinking, cumulative result and streaming step counters include? | Open | Preserve raw fields; official CLI page and one result do not settle thinking or child inclusion. |
| Q3 | Can the working Codex Desktop thread emit/read supported token updates and turn intervals through App Server? | Open | Documented event and CLI schema exist; attachment to this Desktop task was not observed. |
| Q4 | Can a fresh Claude Desktop Code/Cowork session export request counters without changing shared configuration? | Open | OTel is documented for Code; only separate Git Bash CLI was captured. |
| Q5 | What actual charge, dated tariff or subscription allocation can accompany these observations? | Open | Claude CLI produced a list-cost estimate; AGY produced no money field. Subscription payment and eligible pool were not inspected. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|---|---|---|---|
| H1 | An exact named surface exposes sufficiently complete task/role tokens and execution intervals; assess each platform separately. | Proposed | 🟡 Narrow adjacent support; full claim open | Two completed CLI sessions have numeric counters and durations, but no complete role/child join or exact Desktop numeric observation. |
| H2 | Task-local records support period and full-task totals across parallel roles, revisions and ongoing work. | Proposed | ⚪ Deferred to iteration 2 | Counter/overlap failure cases identified; no multi-role or cross-period sample assembled. |
| H3 | One close-time invocation assigns useful product terms and a primary area at acceptable cost. | Proposed | ⚪ Deferred to iteration 2 | No classification trial in this capability iteration. |
| H4 | Money view is grounded in known model/token categories and a declared price/payment basis. | Proposed | 🟡 Partial estimate; full claim open | Claude CLI per-model `costBasis: list` and estimate observed; AGY price absent and subscription charge/eligible coverage unknown. |

## HL Update Recommendations

The Researcher classifies these for the Coordinator; no HL text or frozen claim is changed here.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|---|---|
| R1 | §2 | Add dated local versions and the exact Desktop-versus-CLI distinction; replace the blanket “no live capture” statement with two adjacent CLI captures while retaining “no demonstrated task/role-bound Desktop route.” | Gather G1; Challenge C5/C7. |
| R2 | §7.2 | Cite Antigravity 2.0 hooks/CLI, Claude Code monitoring/costs and Codex App Server/schema evidence with their surface limits. | Gather–Challenge primary-source checks. |
| R3 | §8–§9 | Mark isolated CLI capture as observed but complete task join, child coverage, exact Desktop access and actual/subscription money as open; add invocation-flag and counter-inclusion risks. | Challenge C1–C7. |
| R4 | §10 | Replace the pending three-platform preview with the matrix above, carry H1/H4 as partially tested, and focus iteration 2 on role binding, counters, cross-period aggregation, classifier cost and the `economics.md` record contract. | This RES, Decisions and Open Questions. |
| R5 | §11 | Record the owner's task-specific AGY CLI steering and Git Bash Claude CLI clarification without treating adjacent CLI results as Desktop proof or a universal project preference. | Owner messages during iteration 1; Challenge C5/C7. |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

No amendment proposals. The Coordinator's scope ruling `journal/20260928-224307__gate_answer__fb52.md @ 582d51d115403ae8b1a843d468338b4663cd5c75` permits the bounded AGY CLI probe under the approved mandate; the frozen three-platform comparison and pilot contract are unchanged. CLI substitution as an implementation guarantee was not established.

## Fact Candidates

The conversation history and approved HL §11 were reviewed. These are new human-sourced, task-specific statements, not verified project-wide rules.

| # | Category | Candidate | Source | Confidence |
|---|---|---|---|---|
| FC1 | process | For this research probe, the owner directed use of `agy` CLI instead of the Antigravity GUI. | User, direct Researcher message, 2026-09-28 (“use agy cli instead GUI”). | High |
| FC2 | stakeholder | The owner said Claude CLI had subscription access inside Git Bash and asked for that environment to be tried. | Owner clarification relayed to this Researcher by the Coordinator, 2026-09-28. | High for the statement; access was independently probed. |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|---|---|---|---|
| SS1 | process | The owner wants local CLI evidence when the GUI route is impractical in this research. A collector should identify its actual launch surface and flags and show CLI coverage explicitly; the instruction does not by itself make CLI data interchangeable with Desktop data. | User, direct AGY steering, 2026-09-28. | ★★★ |
| SS2 | stakeholder | The owner's Git Bash correction exposed an environment-dependent access assumption: the earlier `Not logged in` result did not settle Claude CLI availability. The successful no-`--bare` probe supports a targeted authenticated path, while the failed `--bare` probe shows the actual invocation must be verified. | Owner clarification relayed by Coordinator, 2026-09-28; Challenge C7. | ★★★ |

## Findings Map

```text
Named Desktop surfaces (the HL comparison denominator)
├─ Antigravity 2.16.0 ─ hooks: conversation identity; Desktop numeric data unverified
│  └─ adjacent AGY CLI 1.2.8 ─ observed session tokens + duration; price/model/child join open
├─ Claude Desktop 2.9939.2 ─ Code OTel documented; Desktop export unverified
│  └─ adjacent Claude Code CLI 2.1.283 ─ observed tokens + duration + list-cost estimate
└─ Codex Desktop 26.924.2738 ─ App Server event documented; live attachment unverified
   └─ adjacent Codex CLI 0.152.1 ─ generated token schema, no owned event capture

For a task economics figure: numeric event → exact session/role join → counter rule
                           → time meaning → price/payment basis → coverage label.
Account quota has no exact session join; a CLI observation does not fill a Desktop row.
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 2 (max).
- **Hypotheses tested:** H1 partially supported by two adjacent CLI captures but open for exact surfaces/full role coverage; H4 partially supported by a Claude list estimate but open for actual/subscription money.
- **Hypotheses deferred:** H2 needs multi-role, cross-period and revision evidence; H3 needs a bounded classifier trial on representative permitted material.
- **Gaps discovered:** exact Desktop numeric access on all three surfaces; TFW task/role and child join; AGY thinking and cumulative/step inclusion; effective AGY run model and price; Claude CLI list estimate versus charge; Codex `total`/`last` event semantics; a task-bound execution interval.
- **Superseded decisions:** Extract's C7-first *candidate* was superseded as first *observed local session capture* by owner-directed AGY C11 and Git Bash Claude C12. C7 remains a conditional exact-Desktop candidate. Gather's inference that Claude CLI could not authenticate was corrected by the completed Git Bash invocation without `--bare`.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|---|---|---|
| 1 | CLI launch identity, child/retry coverage and counter inclusion | One-session records cannot yet become whole-task or role totals. | Run bounded task-owned parent/child or retry cases where permitted; pin model, retain IDs and reconcile cumulative versus step/request records. |
| 2 | Exact Desktop event access | The HL requires a three-platform capability comparison and a credible first implementation path. | Check supported Codex App Server attachment, Claude Desktop Code export and Antigravity numeric source; record precise unavailable prerequisites. |
| 3 | Money and time basis | List estimates, subscriptions, API time and agent time answer different questions. | Define price epoch/payment pool and interval semantics; keep missing values explicit. |
| 4 | `economics.md` contract, period/lifetime totals and classification | H2/H3 and the single-file artifact are untested. | Exercise representative task/phase and two-project examples with overlap, ongoing work and one bounded classification; measure overhead. |

### Recommendation

- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS.
- [x] **MORE NEEDED** — execute the approved second iteration to test task/role joins, counter and time semantics, period/full-task aggregation, classification overhead and the `economics.md` contract before a TS claims supported coverage.
- [ ] **BLOCKED** — no research continuation is possible.

The Coordinator decides continuation; this Researcher does not change `research/iterations.yaml` or launch iteration 2.

## Conclusion

Iteration 1 produced a versioned three-platform capability map and two completed local CLI observations that a documentation-only review would have missed. The Claude Git Bash result corrected an overly broad authentication inference; the AGY result corrected the earlier timed-out zero record. Both are valuable prospective capture candidates, but neither proves full TFW role/child coverage or numeric access in the named Desktop applications. Counter inclusion, effective model/pricing and execution-time meaning remain unresolved, so the honest return is a second focused iteration rather than an implementation claim.

### Material handover at this return

Producer: Researcher `codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243`; recipient: exact parent Coordinator `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793` under `tfw-gates-only` / `native-gates`. Source/epoch: owner-approved HL freeze, four stage traces, linked official sources fetched 2026-09-28, installed-application inventory, generated local Codex CLI schema and bounded AGY/Claude CLI probes on 2026-09-28. Inspected scope: public documentation, executable/package metadata, task-owned tool schema/quota shape and fresh isolated CLI sessions; no unrelated conversation, transcript, account secret or persistent setting was inspected or changed. Material: exact Desktop capability remains unverified; AGY CLI supplied a completed token/time record and Claude CLI supplied a completed token/time/list-cost record without `--bare`. Uncertainty: full task/role/child attribution, counter inclusion, AGY model/price, subscription charge, Desktop attachment and H2/H3. Continuation: Coordinator integrates this return, closes iteration-1 control and dispatches the approved iteration 2 if its gates allow; any TS or HL application remains on the Coordinator/owner route.

---

*RES — TFW_20260928-181352_TEQM: Task Economics and Quality Measurement | 2026-09-28*
