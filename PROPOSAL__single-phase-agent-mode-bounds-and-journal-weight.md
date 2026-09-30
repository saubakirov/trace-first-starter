# PROPOSAL — Single-phase agent mode: observable bounds, and journal weight in round-based work

> **Status:** OPEN — filed 2026-09-30 by the Helpdesk CAB task Coordinator at the owner's request.
> **Origin:** Helpdesk task `HD_20260929-162835_CAB` (TFW 3.8.0, Claude Code desktop, single-phase agent
> mode). Trace: [`../helpdesk/workspace/2026/HD_20260929-162835_CAB/`](../helpdesk/workspace/2026/HD_20260929-162835_CAB/)
> on the **local** `beta` line of that repository (closing commit `63523779`; the trace is not on the
> remote `beta`, see Helpdesk `KR-20260930-635237-06`). Retro items outside these two proposals were
> filed as Helpdesk knowledge records `KR-20260930-635237-01…09` and are not proposed here.
> Per `.tfw/conventions.md` rule 12, each proposal below carries evidence, cost and a considered alternative.

## Measured task

| Measure | Value | Where measured |
|---|---|---|
| Mode | single-phase agent mode: one Coordinator session, Researcher / Executor / Reviewer as distinct agents started with `/tfw-* <task>` | `journal/*coordination_selected*`, dispatch events |
| Owner remark rounds on beta | 18 (each: fix → targeted tests → packaging push → CI → owner/user check) | RF round table, `gate_answer__4053` |
| Calendar | 108 965 s (~30.3 h) | `economics.md` |
| Volume | 139 VALUE files / 8 473 LOC vs denominator 48 / 5 500; ×2 bound crossed at round 11, measured at round 18 | HL §12 A7, REVIEW F9 |
| Tokens / API-reference cost | 1 101 447 431 tokens; $438.59 | `economics.md` |
| Journal events | 33: 21 `dispatch`, 5 `transition`, 3 `gate_answer`, 1 each `created`, `coordination_selected`, `handoff`, `amendment_escalated` | `journal/` |
| Outcome | independent APPROVE on a fixed Candidate; owner and user acceptance on beta; released to production as v2.1.0 the same day | REVIEW, CHANGELOG |

The Coordinator's conversation was compacted by the surface at least once during the task.

## Proposal 1 — bound the single-phase agent mode by observables, not by the word "small"

**Current text** (`.tfw/adapters/claude-code/coordinator.md`, § Single-phase agent mode): "For a really
small one-phase task, such as a small fix or debt item, the owner may choose this mode … This saves
owner clicks, not Coordinator context. If the task outgrows one phase or an agent cannot load its
workflow or a required tool, stop that delegation, name the limit and offer full role chats".

**Evidence.** CAB was not small by any reading of the sentence and the mode held: roles stayed
distinct, the Reviewer was a new agent on a fixed Candidate, returns were vertical, acceptance was
independent. What failed was not the mode but two controls that are independent of it: the per-round
volume measurement (Helpdesk `KR-…-01`) and the economics revision chain (`KR-…-02`). The named exit
conditions ("outgrows one phase", "cannot load workflow/tool") never fired; the real pressures were
Coordinator context (compaction), agent name resolution across a date change (`KR-…-08`) and the
owner's wish to relay 18 rounds through one conversation — which is exactly what the mode is for.

**Proposed change.** Keep the mode as an owner choice; replace "really small" with stop conditions
the Coordinator can observe and must report at the next gate:
1. the Coordinator's conversation was compacted, or the surface stopped resolving an agent by name
   (record the id; if the id also fails, the mode has ended);
2. N owner rounds without a full gate run (N set by the project, Helpdesk would set 6) — each such
   checkpoint requires the volume line of `KR-…-01`;
3. a second phase, or a second Executor, becomes necessary.
State explicitly that the mode is bounded by Coordinator context, not by task size, and that address
by id is the norm in it. This turns "small" from a judgement into a report.

**Cost.** One profile paragraph and one line in the startup card. No workflow change.

**Alternative considered.** Keep "really small" and route CAB-size work to full role chats. Rejected by
the measured case: the owner chose the mode precisely to avoid creating and relaying through three
chats over 18 rounds; the full-chat route would have moved every round through owner clicks.

## Proposal 2 — journal weight in round-based work: let one `dispatch` cover a bounded batch of rounds

**Current rule** (`.tfw/conventions.md`, delegation and dispatch): each task/phase-local `dispatch`
event preserves actual source, destination, governing authority and mandate; events are immutable
files, one per event.

**Evidence.** 21 of 33 CAB events are `dispatch`, one per owner remark batch. Their bodies repeat the
same shape — source: owner message; destination: the same Executor id; governing: the same TS and HL
epochs; mandate: the same A3 delegation — and differ only in the remark text and the round number.
The per-round record already exists elsewhere and is richer: the RF round table carries Candidate SHA,
packaging SHA, pipeline id, image tag, what changed and what was verified, and the packaging commit
carries the timestamp. In an 18-round day the dispatch ceremony was a visible share of Coordinator
time and context, which Proposal 1 identifies as the binding constraint of the mode.

**Proposed change.** Allow a `dispatch` event to cover a **bounded batch of rounds** when source
kind, destination, governing epochs and mandate are unchanged: the event names the round range and
the RF table as the per-round carrier; any change in destination, mandate or governing epoch opens a
new event. Keep one event per round as the default outside declared round modes (a `gate_answer`
that declares the round mode, like CAB's `4053`, is the switch).

**Cost.** Per-round timestamps leave the journal (they remain in the RF row and the packaging commit);
a reader reconstructing one round reads RF plus git instead of one event. The immutability rule is
unchanged: a batch event is still written once, after the batch, at its observation epoch.

**Alternatives considered.** (a) A lighter `round` event kind with only `refs` and `summary` — adds a
kind and still costs one file per round. (b) Keep as is — the trace was excellent and nothing was
lost; the cost is real but bounded, so this proposal is a convenience, not a correction. The owner
may reasonably choose (b).

## What is not proposed here

- The volume-measurement rule for accelerated rounds (`handoff.md`): filed as Helpdesk `KR-…-01`;
  worth an upstream line, but that is a separate, smaller proposal.
- The economics helper's successor semantics (`unproved successor overlap` on a non-complete
  successor; chained successors conflict): filed as `KR-…-02` with the working recipe.
- The "owner-run evidence" status for EV/REVIEW: filed as `KR-…-03`.

## Requested decision

Owner of `steps-framework`: accept, amend or decline each proposal separately. Acceptance of
Proposal 1 changes only the Claude Code and Antigravity Coordinator profiles; Proposal 2 changes
`conventions.md` and the `journal/event.md` template guidance.
