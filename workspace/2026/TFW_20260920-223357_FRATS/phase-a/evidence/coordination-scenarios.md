# Phase A Coordination Scenarios

> Date: 2026-09-21
> Baseline: `c80c0dd5e79a6e996fdc68a89ad01b26887c638e`
> Candidate: `1a9209530d7a939db1270e2f91dcef40a9f449e6`
> Governing TS: `TS__phase-a__explicit_coordination_gateway_and_session_identity.md` at `ad6042dad73aa04b9bbe9f13880c5a944e7e4f05`
> Executor unit: `codex:thread:local:01a0c3a2-c742-7962-a981-369effb5ac83`
> Parent Coordinator: `codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf`

## 1. Status schema fixtures

The fixtures called `tools.tfw_state.validate_status`, `validate_new_status`, and
`validate_new_event` in memory; they did not write repository fixtures.

| Case | Input distinction | Reader verdict | Current-writer verdict |
|---|---|---|---|
| Complete current | all five fields; owner gateway; gates-only; owner-only; local TS plus full approval SHA | PASS | PASS |
| Complete legacy | all five fields absent | PASS as legacy | REFUSE: five current fields missing |
| Partial | only `coordinator_route` present | REFUSE: partial spine | REFUSE |
| Empty | empty `coordinator_route` | REFUSE | REFUSE |
| Invalid enum | `dialogue: chatty` | REFUSE | REFUSE |
| Unresolved authority | authority epoch `latest` instead of a full immutable Git epoch | REFUSE | REFUSE |
| Iterative without gateway | `dialogue: iterative` with `owner:saubakirov` | REFUSE | REFUSE |
| Terminal history | terminal carrier with outcome and no routing spine | PASS as immutable legacy | no rewrite; cannot activate |

The active Phase A carrier was migrated only after Candidate. Commit `9e9513a` added the complete
spine to `phase-a/status.md` while lifecycle remained `ONB`; no same-state event was invented.
`validate_new_status` returned PASS.

## 2. Activation and lineage scenarios

| Scenario | Required facts | Result / refusal point | Durable source |
|---|---|---|---|
| Owner-direct | exact `/tfw-handoff`, FRATS phase-a, explicit owner source, current spine | ACCEPT; autonomous Role-Locked work | user invocation, status, ONB provenance |
| Delegated dispatch | exact skill/task/phase plus direct Coordinator dispatch and immutable mandate | ACCEPT only after all facts resolve | status + dispatch event + role artifact |
| Continuation | same unit, prior activation ref, named authoritative gate, unchanged spine | ACCEPT | prior role artifact/event + current status |
| Prompt only | “You are Executor” without exact skill/source | REFUSE before material read/write | refusal returned to Coordinator |
| Briefing-biased | copied solution or long briefing without exact skill/source | REFUSE before material work | refusal returned to Coordinator |
| Wrong unit | foreign role/address/parent/scope | REFUSE before material work | status + dispatch mismatch |
| Missing skill | task and role named, `/tfw-*` absent | REFUSE before material work | activation checkpoint |
| Unavailable holder | requested continuation cannot address the same unit | REFUSE; no relay/provider substitute | existing lineage + refusal |
| GATEWAY self-plan | gateway tries to run `/tfw-plan` itself | REFUSE; it may activate a separate Coordinator only under exact delegated authority | routing spine + immutable grant |

Provisioning, selecting a task, setting a title, role prompts, briefings, and wait results are
explicitly non-activating in the canonical contract and all nine changed workflows.

## 3. Gates-only edge matrix

| Source | Destination | Payload | Verdict | Carrier / refusal |
|---|---|---|---|---|
| Role unit | own Coordinator | named gate, status/correction, durable return | ALLOW | role artifact plus status/event ref |
| Own Coordinator | role unit | activation/dispatch or authority event reference | ALLOW | direct dispatch or `gate_answer` |
| Role unit | peer role | any material work | REFUSE | role artifact notes discrepancy once; return upward |
| Role unit | foreign Coordinator | any material work | REFUSE | routing-spine mismatch |
| Role unit | owner | gate/result/question | REFUSE | own Coordinator alone uses `owner_gateway` |
| Role unit | GATEWAY | raw traffic or result | REFUSE | gateway receives no raw worker traffic |
| Reviewer | dialogue peer/consolidator | result-development dialogue | REFUSE | independence boundary |

The live Codex Executor used the allowed vertical edge twice: ONB/ONB-transition status and
Candidate/routing-migration status were sent directly to `PLAN · FRATS`. No prohibited edge was sent.

## 4. Iterative dialogue and GATEWAY

| Grant case | Verdict | Reason |
|---|---|---|
| Exact owner-approved grant naming two peers, purpose, boundary, consolidator, durable output, stop, and separate GATEWAY | ACCEPT within those bounds |
| No grant | REFUSE | gates-only remains authoritative |
| Broad “agents may collaborate” grant | REFUSE | peers/purpose/boundary/output/stop unresolved |
| Reviewer included as peer or consolidator | REFUSE | independence would be lost |
| GATEWAY equals root Coordinator | REFUSE | topology collapses ingress and coordination |
| GATEWAY runs a role workflow or receives raw worker traffic | REFUSE | ingress boundary violated |

Navigation is exactly `GATEWAY · {TASK}` or, only with explicitly selected stable attribution,
`GATEWAY · {handle} · {TASK}`. The title grants nothing.

## 5. Authority-owned gate answers

| Case | Verdict | Reason |
|---|---|---|
| Authority-written event cites `status.md`, blocked ONB, and governing TS | PASS | current `gate_answer` carrier is complete |
| Executor self-answer | REFUSE | blocked role cannot own the authority event |
| Cross-task ref | REFUSE | containment/reference validation fails |
| Stale/contradictory source | REFUSE | current status/epoch does not resolve |
| Missing role or HL/TS ref | REFUSE | `validate_new_event` reports the missing class |
| Answer changes scope, acceptance, architecture, authority, or owner reservation | REFUSE | requires TS revision or HL §12, not `gate_answer` |

The ONB template owns only question, blocking reason, event reference, and operational effect. It no
longer invites a Coordinator or human to edit the Executor-owned file.

## 6. Role / artifact ownership

| Artifact | Producer | Required provenance | Negative case |
|---|---|---|---|
| Briefing, RES | Researcher | actual unit, parent route, activation/dispatch, authority, origin | Coordinator prework or producer mismatch refuses |
| ONB, RF | Executor | actual unit, parent route, activation/dispatch, authority, origin | self-answer or foreign producer refuses |
| REVIEW | independent Reviewer | actual unit, parent route, activation/dispatch, authority, origin | result-development peer role refuses |

Prior artifacts are consumed at their stated evidence level. Distrust alone does not authorize
repetition. A concrete contradiction is recorded once in the detecting role's artifact and returned
to that unit's Coordinator without peer debate.

## 7. Six-edge semantic matrix

| Edge | Positive | Material negative | Outcome |
|---|---|---|---|
| Activation | exact skill/task/phase plus owner-direct source | role prompt or missing skill | start / pre-work refusal |
| Authority | current spine and resolvable immutable epoch | partial, placeholder, stale or foreign authority | accept / blocked |
| Evidence | provider-own receipt with stated limit | translated or composed provider claim | bounded claim / refuse claim |
| Recovery | same unit and named prior gate | implicit latest session or substitute holder | continue / refuse |
| Continuation | same unit, prior activation ref, unchanged spine | wrong unit or changed authority | resume / pre-work refusal |
| Exception | valid `gate_answer` or exact iterative grant | self-answer, hidden amendment, broad dialogue grant | bounded effect / escalate |

All twelve outcomes match the frozen Phase A contract. No receiver project, historical artifact, or
FRATS-D01 control was modified.
