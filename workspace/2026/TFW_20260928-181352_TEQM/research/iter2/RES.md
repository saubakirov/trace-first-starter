# RES — TFW_20260928-181352_TEQM: Task Economics and Quality Measurement

> **Current filename**: `research/iter2/RES.md` under this task.

> **Date**: 2026-09-28
> **Author**: Researcher unit (this Claude Code session)
> **Status**: 🔬 RES — iteration 2 complete
> **Parent HL**: [HL-TFW_20260928-181352_TEQM.md](../../HL-TFW_20260928-181352_TEQM.md) at `36c100b1d6e246fbdb45ec7a2341bb652ca80b7a`
> **Mode**: Pipeline / focused
> **Producer unit**: `claude-code:session:local_802eab5b-1770-4551-b59a-aefd367bb975` (this session; native session ID read back via `mcp__ccd_session_mgmt__get_session`)
> **Parent Coordinator**: `codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793` (per `status.md.coordinator_route`)
> **Activation / dispatch source**: Owner-direct `/tfw-research TFW_20260928-181352_TEQM` entered inside this Claude Code session on 2026-09-28, selecting the Coordinator-prepared pending iteration 2 row in `research/iterations.yaml` (agent: `claude`), per that row's own authorized parallel-launch text and HL §4.1's approved research mandate. No agent principal is invented.
> **Coordination authority**: `HL-TFW_20260928-181352_TEQM.md @ 36c100b1d6e246fbdb45ec7a2341bb652ca80b7a`
> **Originating proposer**: none

---

## Research Context

Iteration 2 is this task's Claude self-inspection leg, running independently of and in parallel with iteration 3 (Antigravity, out of scope here and not inspected). Per `research/iterations.yaml` row 2 and the owner's direct command this turn, the task was to identify this exact Claude Code session's surface/mode/version and inspect only this session's own accessible numeric metadata — session/model identity, input/output/cache/thinking tokens, duration, money basis — demonstrate at least one small safe observation, and state exactly what this session exposes and how `economics.md` could collect it, in one focused pass with no intermediate waits. The owner's chat command reinforced that directive explicitly for this turn. Sources and probes were the owner's own subscribed Claude Code Desktop/Code-tab session (this one), two live samples of its own usage-management tools, and public Claude Code CLI/OTel documentation; no unrelated session, transcript or account setting was inspected or changed.

## Briefing

[Briefing](1_briefing.md) framed H1 and H4 as the primary hypotheses for this exact surface, planned a Gather across this session's own fields plus public CLI/OTel documentation, and set Guiding Questions on token/money availability and child coverage. [Gather](2_gather.md) captured two live `get_usage`/`get_session` samples and the adjacent documentation. [Extract](3_extract.md) mapped each HL numeric need onto what this surface does and does not expose, and located this iteration's result relative to iter1's provisional Desktop row. [Challenge](4_challenge.md) stress-tested the context-occupancy-as-total and quota-as-money assumptions and settled on three surviving, explicitly bounded configurations.

## Decisions

| # | Decision | Rationale |
|---|---|---|
| D1 | Record this exact surface as **Claude Code Desktop, "Code tab" agent session** (this session), distinct from Claude Chat/Cowork modes iter1 also named; do not generalize this iteration's findings to those other modes. | This session's own tool surface (`ccd_session_mgmt.*`) is what was actually queried; nothing here touches Chat/Cowork. |
| D2 | Use `get_session`'s `sessionId` (`local_802eab5b-1770-4551-b59a-aefd367bb975`) as the session/task-role identity anchor; note it is stable across this whole multi-stage iteration, unlike iter1's per-invocation CLI `session_id`. | Two samples five stages apart returned the same ID; iter1's Git Bash CLI minted a fresh ID per invocation. |
| D3 | Report token exposure on this surface as **context-window occupancy** (`tokensUsed`/`contextWindow`/`percentUsed`, content-type categories), not as input/output/cache/thinking counters; no such counters exist in `get_usage`'s output. | Directly observed field names and values in two samples (Gather G1); cross-checked against the OTel-documented counter names (Gather G2), which do not appear here. |
| D4 | Reject context-occupancy as a lifetime-total proxy after any compaction; accept a same-window, pre-compaction delta (C4') only as a bounded, labeled rate, not a task total. | `autoCompactsAtPercent: 97` is a documented shrink point for the same counter; iter1's D4 already established the general anti-pattern (arithmetic ≠ inclusion proof) for a different platform's counters. |
| D5 | Report money on this surface as **unknown**, not merely "unlabeled" — a quota percentage against an undisclosed pool size and undisclosed plan price cannot be converted into an estimate, unlike iter1's Claude CLI row, which had a `costBasis: list` figure to label. | `get_usage.plan` exposes only percentages and reset times; `extraUsage.enabled: false`; no third-party figure for this exact plan's pool size was found strong enough to cite without manufacturing evidence (DoF-1). |
| D6 | **Addendum, added after the owner's follow-up direction to test parallel/child sessions directly.** Two separate, non-overlapping child-coverage mechanisms exist on this surface, not one: `list_sessions`/`get_usage` (pull, on demand) never see an `Agent`-tool sub-agent at all; the task-notification event fired at a sub-agent's own completion pushes `subagent_tokens`/`tool_uses`/`duration_ms` automatically instead. `economics.md` collection logic must pick the mechanism per child *type*, not assume one uniform child-coverage answer. | One spawned trivial `Agent` sub-agent (task: "what is 2+2?"), `list_sessions({linked:true})` and `list_sessions({include_archived:true})` both blind to it while its own completion notification carried `subagent_tokens: 53901`, `tool_uses: 0`, `duration_ms: 2519` — Gather G5, Challenge C5 (addenda). |

## Open Questions

| # | Question | Status | Answer |
|---|---|---|---|
| Q1 | Does this exact session expose task/role-bound tokens comparable to the CLI's input/output/cache split? | Closed | No — only context-window occupancy by content type, confirmed by two live samples. |
| Q2 | Can this surface ground a dollar money view under the current plan? | Closed | No — quota percentage only; no absolute pool size or price is exposed; `extraUsage` is disabled for this account. |
| Q3 | Can a future collector get child/parallel-role coverage from this surface? | Closed (addendum) | Yes, but through two different mechanisms depending on child type: `Agent`-tool sub-agents are invisible to `list_sessions`/`get_usage` and instead self-report `subagent_tokens`/`tool_uses`/`duration_ms` via their own completion notification (observed: one live probe); a hypothetical separately-started linked CCD session would instead need `list_sessions(linked:true)` + `get_usage` polled before it archives (still schema-documented only, no such session exists in this account to test). |
| Q4 | Does `contextWindow: 1,000,000` reflect a documented plan/model allowance? | Open | Public search only found generic 200K/500K figures for other configurations; this account's actual 1M figure is unreconciled. |
| Q5 | Is there any route to the richer OTel-documented schema (token-type split, USD cost, active-time split) from inside a Desktop Code-tab session? | Open | Documentation ties that schema to a separately configured CLI process with telemetry env vars; no attachment to this Desktop session type was found or attempted. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|---|---|---|---|
| H1 | An exact named surface exposes sufficiently complete task/role tokens and execution intervals; assess each platform separately. | Proposed | 🟡 Claude Desktop (Code-tab) row filled: session/model identity yes, token-direction split no, execution interval no exact counter (wall-clock bounds only) | Two live `get_usage`/`get_session` samples (Gather G1), cross-checked against OTel docs (Gather G2). |
| H4 | Money view is grounded in known model/token categories and a declared price or payment basis. | Proposed | 🔴 For this exact surface: no — quota % only, not convertible to dollars under the current plan | `get_usage.plan` fields (Gather G1); `extraUsage.enabled: false`; Challenge C2. |
| H2 | Task-local records support period and full-task totals across parallel roles, revisions and ongoing work. | Proposed | 🟡 One facet now observed (addendum): `Agent`-tool sub-agent token/duration coverage is real, via its notification event, not merely documented. Full H2 — revisions, cross-period totals, a separately-started linked-session child — remains untested; formal reconciliation stays with iteration 4 per `research/iterations.yaml`. | Gather G4/G5; Challenge C5 (addendum). |
| H3 | One close-time invocation assigns useful product terms and a primary area at acceptable cost. | Proposed | ⚪ Not touched — out of this iteration's focus; deferred to iteration 4. | None this iteration. |

## HL Update Recommendations

The Researcher classifies these for the Coordinator; no HL text or frozen claim is changed here.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|---|---|
| R1 | §10 | Fill the "Claude Desktop — exact mode/version to establish" row of the three-platform preview table with this iteration's result: Code-tab agent session, `claude-sonnet-5`, session/model identity via `get_session`, context-window occupancy (not token-direction) via `get_usage`, no dollar cost, quota % only; explicitly note Chat/Cowork modes remain untested. | This RES, Decisions D1–D5. |
| R2 | §2 | Add the observed context-window-size discrepancy (documented 200K/500K vs this session's observed 1,000,000) as an open, sourced item rather than letting §2's "no complete live capture route" read as fully resolved by this partial capture. | Gather G3. |
| R3 | §7.2 | Cite the [Claude Code monitoring/OTel doc](https://code.claude.com/docs/en/monitoring-usage)'s specific counter names (`claude_code.token.usage`, `.cost.usage`, `.active_time.total`) as the documented richer schema this Desktop surface does not expose, alongside iter1's existing citation of the same page for CLI. | Gather G2. |
| R4 | §9 | Add a risk row: "A live context-window gauge is mistaken for a cumulative token total after compaction," with the proposed response "record the compaction watermark alongside any same-session delta, or bound the claim to a compaction-free window." | Challenge, incompatible pair D2×HL-Artifact-contract. |
| R5 | §10 | Carry H1 as platform-differentiated (CLI: partial estimate available; this Desktop Code-tab surface: identity yes, tokens/cost coarse-or-absent) rather than one shared status, and note H4 now has one negative-with-reason data point (this surface) alongside iter1's one partial-positive (Claude CLI list estimate) — the two must be reconciled per-surface in iteration 4, not averaged. | Hypotheses table above. |
| R6 | §10 | Record, as a cross-cutting note for the eventual `economics.md` contract, that `Agent`-tool sub-agent work (background/parallel delegation within one Claude Code session) is invisible to `list_sessions`/`get_usage` and must instead be captured from its own completion-notification event (`subagent_tokens`/`tool_uses`/`duration_ms`) at the moment it fires, not polled later. | Gather G5, Challenge C5 (addenda) — one observed spawn/completion. |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

No amendment proposals. This iteration stayed within the owner-approved §4.1 mandate (bounded local self-inspection of this exact session's own metadata); no frozen §1/§3–§7 claim is challenged by these findings.

## Fact Candidates

The conversation history for this iteration was reviewed. This is a new human-sourced, task-specific statement, not a verified project-wide rule.

| # | Category | Candidate | Source | Confidence |
|---|---|---|---|---|
| FC1 | process | For this specific iteration 2 turn, the owner explicitly directed no intermediate approval waits and a single pass straight through to a completed RES, reinforcing (in live chat, not only in the pre-written `research/iterations.yaml` row text) that this self-inspection iteration should run without stage-by-stage checkpoints. | User, direct command this turn, 2026-09-28 ("вопросов не задавай доводи ресерч iter 2"). | High |
| FC2 | process | After the first RES pass, the owner directly asked for a live parallel/child-session test specifically ("параллельные сессии можешь проверить рядом и дополнить"), rather than accepting the schema-documented, unexercised child-coverage claim as sufficient. | User, direct follow-up command, 2026-09-28. | High |

## Strategic Insights (Research)

No strategic insights beyond FC1 above — no additional domain knowledge, correction or strategic context was supplied by the owner this iteration beyond the process directive already captured as a Fact Candidate.

## Findings Map

```text
This task's economics data sources, by surface (iteration 2 adds the middle branch)
├─ Antigravity ─ iter1: hooks documented, AGY CLI observed ─ iteration 3: pending (out of scope here)
├─ Claude ─ iter1: adjacent Claude Code CLI observed (tokens+duration+list-cost)
│         └─ iteration 2 (this RES): Claude Code Desktop "Code tab" session (this one)
│              ├─ session/model identity ─ OBSERVED (get_session)
│              ├─ tokens ─ OBSERVED but coarse: context-window occupancy by content-type,
│              │           not input/output/cache/thinking (get_usage)
│              ├─ time ─ wall-clock bounds only (createdAt/lastActivityAt); no exact interval
│              ├─ money ─ quota % only; NOT convertible to a dollar figure on this plan
│              └─ children ─ TWO mechanisms, addendum:
│                   ├─ list_sessions(linked)+get_usage ─ blind to Agent-tool sub-agents (OBSERVED)
│                   └─ completion notification ─ subagent_tokens/tool_uses/duration_ms,
│                        pushed automatically at close (OBSERVED: 53,901 tok / 0 tools / 2,519 ms)
└─ Codex ─ iter1: App Server/CLI schema documented, no live Desktop attachment

Same-surface delta technique (C4'): sample get_usage twice, subtract →
  valid rate PROVIDED no compaction fired between samples (autoCompactsAtPercent watermark
  must be recorded); otherwise void. This is the one new capture idea this iteration adds
  that Briefing did not anticipate.
```

## Iteration Status

- **Iteration:** 2 of 4 (min) / 4 (max), per this task's `research/iterations.yaml` (task-specific ceiling, overriding the project-config default of 2/3).
- **Hypotheses tested:** H1 (Claude Desktop Code-tab row filled — partial: identity yes, token/time granularity coarse); H4 (this surface — negative, with reason: no dollar-convertible basis under the current plan).
- **Hypotheses deferred:** H2 (child-coverage mechanism documented, not exercised — formal test belongs to iteration 4's reconciliation per `research/iterations.yaml` row 4); H3 (not touched, out of this iteration's named focus).
- **Gaps discovered:** whether the OTel-documented richer schema can ever attach to a Desktop Code-tab session (Q5); the unreconciled 200K/500K-vs-1,000,000 context-window figure (Q4); whether the completion-notification event is exactly-once (its own note says a resumed agent may notify again under the same task-id) and whether nested grandchild sub-agents produce one rolled-up notification or several; whether a separately-started linked CCD session (not an `Agent`-tool sub-agent) would actually show up in `list_sessions` in practice — no such session exists in this account to test.
- **Superseded decisions:** None within this iteration. This RES's Decisions and Extract §E2 *refine* — not supersede — iter1's provisional "Desktop: numeric unverified" read, specifically for the Claude Desktop Code-tab agent-session mode; iter1's read for Claude Chat/Cowork modes and for Antigravity/Codex Desktop remains exactly as iter1 left it.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|---|---|---|
| 1 | Reconcile per-surface H1/H4 status (Antigravity from iteration 3, Claude from this iteration, Codex from iteration 1) into one matrix instead of one shared verdict. | The task's own iteration 4 focus depends on having three independently-collected, non-averaged rows to reconcile. | Iteration 4: build the single three-platform matrix cell-by-cell from iterations 1–3's actual returns, not a re-derived summary. |
| 2 | Decide whether "money: unknown" for the Claude Desktop Code-tab surface is acceptable for the pilot, or whether the pilot must pair this surface with the CLI/OTel route (iter1) whenever a dollar figure is required. | Directly determines whether the eventual `economics.md` money field for Claude-surface work is ever populated with more than "unknown." | Iteration 4 / TS: an explicit scope decision, owner-visible, not silently defaulted either way. |
| 3 | Extend the now-observed `Agent`-tool notification mechanism to a *non-trivial* TFW role's worth of sub-agent work (not a one-token probe), and separately test whether a real separately-started linked CCD session shows up in `list_sessions` the way its schema claims. | H2 needs the notification mechanism validated under realistic token volume and tool use before `economics.md` can rely on it, and the linked-CCD-session path is still purely theoretical. | Iteration 4: run one bounded, realistic parent/child pair on this surface; capture the notification's usage block verbatim into the child's own `economics.md`. |
| 4 | Reconcile the 200K/500K-documented vs 1,000,000-observed context-window figure. | Affects how the auto-compact watermark should be interpreted for the same-session delta technique (C4') on other accounts/plans. | Low priority; does not block the current pilot decision, but worth a footnote before generalizing C4' beyond this account. |

### Recommendation

- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS.
- [x] **MORE NEEDED** — this task's own `research/iterations.yaml` fixes a 4-iteration structure with iteration 4 explicitly gated on the Coordinator accepting durable returns from iterations 1, 2 and 3 first. Iteration 3 (Antigravity) is still pending and independent of this one; this Researcher does not alter `research/iterations.yaml` or claim iteration 4's reconciliation work.
- [ ] **BLOCKED** — no research continuation is possible.

The Coordinator decides continuation; this Researcher does not change `research/iterations.yaml` or launch iteration 4.

## Conclusion

Iteration 2 answered its own guiding questions directly from two live samples of this exact session's own usage tools rather than from documentation alone: this Claude Code Desktop Code-tab session exposes stable session/model identity and a live, moving context-window-occupancy gauge, but no input/output/cache/thinking token split, no exact execution-time interval, and no dollar-convertible money figure under the current Team plan — a materially coarser, differently-shaped dataset than iter1's adjacent Claude Code CLI observation, not a missing one. The one technique this iteration adds beyond what Briefing anticipated is the same-session delta (C4'), useful only inside a single compaction-free window and only ever labeled as a rate, never a total. Following the owner's direct follow-up to test parallel sessions, one live spawn-and-observe probe (D6/G5/C5, addenda) closed what was initially left as "plausible by schema, not observed": `list_sessions`/`get_usage` are categorically blind to `Agent`-tool sub-agents, but that sub-agent's own completion notification pushes `subagent_tokens`/`tool_uses`/`duration_ms` automatically — a genuine, precise execution interval, the best one either surface has produced. The self-critique: the probe was deliberately trivial (one token, zero tool calls, 53,901 tokens of pure overhead), so the mechanism is confirmed to exist but not yet validated at realistic TFW-role volume, and a hypothetical separately-started linked CCD session (as opposed to an in-conversation sub-agent) remains entirely untested — both stay open threads for iteration 4 rather than settled claims.

### Material handover at this return

Producer: this Claude Code session, `claude-code:session:local_802eab5b-1770-4551-b59a-aefd367bb975`, acting as Researcher for iteration 2 under owner-direct activation; recipient: the task Coordinator named in `status.md` (`codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793`), which integrates this return per `tfw-gates-only`/`native-gates` alongside iterations 1 and 3. Source/epoch: this session's own `mcp__ccd_session_mgmt__get_usage`/`get_session` outputs sampled twice on 2026-09-28 (17:55 and 17:57 UTC-ish per the tool's own ISO timestamps), one spawned `Agent` sub-agent probe and its completion-notification usage block (added as an addendum after the owner's follow-up chat direction, same date), the [Claude Code monitoring/OTel doc](https://code.claude.com/docs/en/monitoring-usage), a bounded web search on Desktop usage limits, and the governing HL/`iterations.yaml`/iter1 RES already committed. Inspected scope: this session's own metadata, one deliberately trivial sub-agent this session itself spawned, and public documentation only; no other pre-existing session (the 19 unrelated sessions surfaced by the unfiltered `list_sessions` check were seen only as a title/id/path list, never opened) was read, and the iteration-3 (Antigravity) work was not touched; `status.md` and `research/iterations.yaml` were read, not written. Material: this Desktop Code-tab surface's token/time/money exposure is coarser than the CLI's, money is flatly unknown here, and child coverage now has one observed, mechanism-specific answer instead of a documented guess. Uncertainty: notification exactly-once/nesting behavior, realistic-volume validation, the context-window-size discrepancy (Q4), and OTel attachment to this session type (Q5) all remain open. Continuation: the Coordinator closes this iteration's control (original pass plus this addendum), awaits iteration 3's independent return, and only then dispatches iteration 4's Coordinator-gated reconciliation per `research/iterations.yaml`; no TS or HL application is implied by this return.

---

*RES — TFW_20260928-181352_TEQM: Task Economics and Quality Measurement | 2026-09-28*
