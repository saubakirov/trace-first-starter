# Gather — What do we not know about three-mode coordination?

> Mindset: Explorer. Map independent choices and falsifiable limits before choosing.
> Parent: [approved HL](../../HL-TFW_20261027-161333_CMODES.md).
> Goal: One portable meaning for manual, visible-agent and single-Coordinator subagent work across any phase count.
> Producer: `/root/cmodes_research`, source thread `01a17db6-0f53-7603-878a-adaa590010e4`; recipient `/root`, the exact Coordinator in status.
> Authority: HL freeze `28af8624b5a42f5078e6303ca844dabd1fbbcab6`; baseline/native-gates/tfw-gates-only; dispatch and source binding in [Briefing](1_briefing.md). Originating proposer: none.
> Epoch: repository `c852d40c63b9c1d601d55fcd0552d03a47e157b0`, own prior trace `b10be0ada27dd66679c610e6072fdad89283efe4`; official documentation fetched 2026-10-27. Focused, one OODA pass.

## Dimensions

The three owner-facing modes and multi-phase eligibility are frozen requirements, not alternatives to reject. These are implementation choices within that requirement; combinations need compatibility checks in Extract/Challenge.

| Dimension | Alternative A | Alternative B | Alternative C |
|---|---|---|---|
| D1: representation of a phase governed by the task's same physical Coordinator | Same native recipient in task and phase; phase upstream names the human, with parent-task provenance validated separately | Same native recipient; explicit task-owned phase relation distinguishes scope aggregation from an inter-unit send | Same native recipient and existing coordinator-prefixed parent pointer; reinterpret equal-address parent traversal as local scope aggregation rather than a send |
| D2: current mode carrier | Mode only in the verified existing baseline/selection event; status keeps its existing selection pointer | Explicit mode field in task/phase status, checked against the verified selection source | Mode inferred from launch/dispatch shape and actual native units, while selection remains narrative |
| D3: recovery when a worker cannot continue | Same-unit native continuation when exact identity and required state are preserved | Explicit replacement at a safe checkpoint from durable files with old/new lineage and still-valid authority | Keep the selected mode pending and request the precise owner-assisted recovery; no automatic substitution |

No configuration is recommended at this stage. D1 alternatives trade field count, route meaning and reader simplicity. D2 alternatives trade machine-readable current choice against duplicated state or inference. D3 options may coexist as an ordered recovery policy; they must not be confused with an authority grant.

## Findings

### G1 — Native capability is per operation and version

The [official OpenAI subagent page](https://learn.chatgpt.com/docs/agent-configuration/subagents) describes separate agent threads, follow-up orchestration and steering in local Codex, inherited permission controls and explicit/configured model selection. It does not establish this project's complete role cycle or guarantee process-restart continuity. Current local tool schemas, rather than general documentation, define the callable transport here.

| Operation | This Codex Desktop surface | Observation and limit |
|---|---|---|
| Provision | `collaboration.spawn_agent` returns a canonical child address; fresh context is `fork_turns: none` | Actual Researcher dispatch exists; no new child was created during Gather. |
| Addressed continuation | `followup_task` starts an idle same child; `send_message` only queues without starting a turn | This child completed an earlier return and received further bounded work under the same address. This proves a local same-session continuation only. |
| Return/readback | Native final result is delivered to parent; `wait_agent` signals mailbox changes | Briefing at an immutable commit was received and explicitly accepted by the parent. No idle-host wake, process restart or exactly-once guarantee was tested. |
| Context separation | Fresh launch requested in dispatch; shared cwd still applies | This child initially lacked the task-specific grant and located it only after an exact reference. That is compatible with fresh context, not an independent information-isolation audit. |
| Mutation isolation | Managed worktree returned an actual separate path; commands must use explicit workdir | Own trace committed there. Worktree isolation does not restrict tool permissions or prove a Reviewer read the fixed Candidate. |
| Capacity | Current tool contract reports four team slots including the root | This is an observed session limit, not a universal Codex constant or a maximum number of task phases. Slot release after terminal worker completion remains untested here. |
| Navigation | Canonical child name/address exists | No independent child title write/readback is exposed. Visible task grouping/title requirements cannot be universal activation prerequisites. |

The [Claude Code subagent documentation](https://code.claude.com/docs/en/sub-agents#resume-subagents) documents resumable general-purpose/custom agents by exact ID, but Explore/Plan are one-shot. Non-fork subagents start fresh; project instructions normally load except for named exceptions. Completed-agent messaging resumes the same ID; resumption by another subagent can change the return recipient. Human-cancelled agents require human resumption. The page documents persistence across restarting the same session, retention limits, and a pre-2.1.304 immediate-resume defect. These are documented behaviors, not locally observed Claude results. A TFW adapter therefore needs version/surface checks and exact Coordinator-origin continuation; neither a generic agent label nor availability of Agent Teams establishes role compatibility.

### G2 — The current phase schema rejects the requested same-unit topology

Read-only inspection of `tools/tfw_state.py:320–335` found two simultaneous conditions: a phase's `upstream_route` must identify the root status's Coordinator, and it must not identify that phase's own `coordinator_route`. Assigning the same Coordinator to root and phase satisfies parent identity but fails the equal-address prohibition at lines 332–333. This is a concrete parser contradiction, not merely wording in an adapter. No code was changed or new permanent test added.

`conventions.md` → `A phase carries its own state` separately requires phase-local status/journal and forbids root lifecycle from summarizing phases. That useful state boundary does not itself require a second physical Coordinator. The representation must preserve it while separating logical phase ownership from a native message edge.

### G3 — Consumer families, not one prohibition

| Current owner / consumer | Observed dependency | Extract consequence |
|---|---|---|
| `conventions.md`, Coordination; `glossary.md`, Phase Coordinator | Distinct holder for each phase; vertical parent structure and no ancestor targets | Decide where same-unit local phase governance ends and inter-unit routing begins. Preserve anti-cycle and authority checks for actual unit edges. |
| `workflows/plan.md`, Steps 1/5/9 | Activates one phase Coordinator per ready phase; phase TS authored by that unit | Add a path where the same task Coordinator derives each ready phase's planning without impersonating workers. |
| `templates/HL.md` §4.1; `templates/status.md` | Frozen selection asks for exact phase units; phase upstream must differ from local recipient | Represent an actual selected topology; keep legacy interpretation and phase scope explicit. |
| `tools/tfw_state.py`, `validate_status` | Hard equal-address rejection plus parent verification | Change grammar and validations coherently; removing the rejection alone would leave message loops and ambiguous selection. |
| Codex profile + `AGENTS.md` + adapter root template | Visible role chats, `wait_threads` and title/readback; explicit subagent ban | Supply native collaboration mechanics without rewriting common meaning or treating a missing title as missing authority. |
| Claude Code profile | Subagents limited to very small one-phase work; visible route otherwise | Remove phase-count eligibility as methodology; retain actual native startup/continuation/permission limits. |
| Antigravity profile | Same one-phase restriction; historic owner reports about native mechanisms | Admit common semantics while keeping unverified current capability explicitly conditional. No live Antigravity claim. |
| Shipped installed entries and glossary; documentation integration | Canonical wording is copied into adapters; definitions and receiving docs can keep obsolete meaning | Derive final delivery set from matched semantics and manifest-owned copy topology during implementation, not a hand-maintained list. |

This is a source-search map, not a frozen implementation file list. Searches covered the relevant adapter/template/workflow trees and named current roots. Bounded body inspection selected the consumers above. `docs/scripts/test_integration.py` contained no literal `upstream_route`, `coordinator_route`, `subagent` or `phase upward` match; that absence does not prove no indirect coverage. `tools/tfw_doctor.py` likewise has no independent literal route logic in the selected search. Existing documentation/integration/blob-size checks remain the validation base; any new permanent tests require the owner's separate discussion.

### G4 — Independence and provenance are separate obligations

An Executor's same native ID can continue corrections, while the Reviewer must be another unit with fresh role context and a fixed reachable Candidate. The Coordinator remains a Coordinator even when all roles are children. Native context separation, filesystem separation, correct authority and independent judgment are four different conditions; none establishes the others.

CMODES can supply task/phase/role, actual parent and child IDs, activation/selection epoch, dispatch and return commit, source binding, and correction/replacement lineage through ordinary existing records. ECFIX owns numeric source discovery, copied-history/overlap interpretation, collector repair and reconciliation. Its accepted interface is not yet supplied. No child sum, cost reduction or whole-cycle measured coverage is claimed.

### G5 — Missing checks with explicit oracles

| Missing proof | Required observation before a success claim |
|---|---|
| Codex interrupt/restart | Interrupt a bounded approved worker and resume the exact returned identity; verify the next artifact and source continuity. Separately restart the host if a restart guarantee is claimed; current same-session continuation cannot stand in for that. |
| Independent fixed-Candidate review | Launch a distinct fresh Reviewer, record Candidate commit and reachable authority, stop conflicting mutation, obtain its own REVIEW, then resume the original Executor for a correction and the original Reviewer for recheck. |
| Multiple phases with one Coordinator | Create two phase-local states under the selected representation; hold phase B until A's required result validates; route both workers to the actual same Coordinator without self-send or second holder. |
| Stale or foreign routing | Reject a wrong parent, foreign/sibling selection event, stale effective epoch and unauthorized replacement; preserve readable historical carriers. |
| Slots and native failure | Demonstrate bounded scheduling or an honest pending action on an observed capacity failure; prove neither phase count nor native completion implies task completion. |
| Claude operation | Exercise command-only startup, durable return and same-ID correction on a named supported Claude Code version/surface; current public docs alone do not complete this proof. |

## Checkpoint

| Found | Remaining |
|---|---|
| Current Codex same-session role return and continuation; documented Claude lifecycle limits | Interrupt/restart, independent Review and full multi-phase proof remain untested. |
| Exact rejecting phase-reader invariant and its prose/template consumers | Compare D1/D2 representations and incompatible combinations in Extract. |
| Existing phase-local state and durable-file ownership remain usable | Settle native delivery vs local scope aggregation and safe switch semantics. |
| ECFIX boundary preserved | Accepted economics interface remains an iteration-2 dependency. |

**Sufficiency:**
- [x] External primary sources used and fetched; one web search, direct opens of official pages.
- [x] Briefing gap closed for Gather: dimensions, consumer causes and precise evidence limits are explicit.
- [x] Independent decision dimensions identified; alternatives remain unranked.

Stage decision: close Gather and compare coherent configurations in Extract; do not expand into native reliability experiments or economics implementation.

Material handover: `/root/cmodes_research` inspected the scoped current consumers at the stated repository epoch and official pages on the observation date. Findings G1–G5 are the material return. Existing PCUX/ATC/GSC/TEQM meanings remain scoped as in Briefing; no successor knowledge or product authority is created. Coordinator may accept this stage under frozen H1/H2. Question: accept the dimensions and missing-proof table as the input for Extract?

Stage complete: YES
→ Coordinator decision: pending; stop before Extract.
