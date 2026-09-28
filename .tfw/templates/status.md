---
id: PREFIX_YYYYMMDD-HHMMSS_ABBR
title: "short task name"
goal: "why this task exists, one line"
value: "what shipping it gives the project, one line"
lifecycle: TODO
owner: unassigned
authority: HL-PREFIX_YYYYMMDD-HHMMSS_ABBR.md
coordinator_route: "native:coordinator-address"
upstream_route: owner:human-handle
dialogue: tfw-gates-only
activation: owner-only
coordination_authority: "HL-PREFIX_YYYYMMDD-HHMMSS_ABBR.md @ full-immutable-epoch"
reporting: native-gates
selection_ref: baseline
created: YYYYMMDD-HHMMSS
updated: YYYYMMDD-HHMMSS
---

**Task state.** This file is the only authority for this task's live state. Any downstream projection is disposable and never outranks it.

<!--
Copy to `{task}/status.md`; for a phase replace only the fixed sentence:

**Task state.** This file is the only authority for this phase's live state. The task-level `status.md` never summarizes it.

Keep front matter, that sentence, and nothing else. Quote prose keys `title`, `goal`, `value`,
`outcome`, and `lifecycle_verbatim`; unquoted colon-space is invalid YAML.

A COMPLETE, VALID EXAMPLE:

    ---
    id: 20260827-091500__query_redesign
    title: "Query redesign: cut p95 latency"
    goal: "the report page times out for the three largest tenants"
    value: "the largest tenants can open the report at all"
    lifecycle: TS_DRAFT
    owner: saubakirov
    authority: HL-20260827-091500__query_redesign.md
    coordinator_route: "codex:thread:local:01example"
    upstream_route: owner:saubakirov
    dialogue: tfw-gates-only
    activation: owner-only
    coordination_authority: "HL-20260827-091500__query_redesign.md @ 0123456789abcdef0123456789abcdef01234567"
    reporting: native-gates
    selection_ref: baseline
    created: 20260827-091500
    updated: 20260827-114210
    ---

For a new phase, the same seven fields use its own worker recipient and the task Coordinator's
observed address as the upward route. For example, if the governing task status has
`coordinator_route: "codex:thread:local:01task"`, its `phase-a/status.md` may carry
`coordinator_route: "codex:thread:local:01phase"` and
`upstream_route: "coordinator:codex:thread:local:01task"`. The phase must have its own
bounded dispatch; this example grants none. A one-phase task uses the task form and no phase
Coordinator.

The key set is closed. Concision guides, never validates; never truncate.

| Key | Shape | Required | Read by |
|---|---|---|---|
| `id` | task directory ID, including readable legacy IDs | always | resume, docs, selected readers |
| `title` | complete one-line prose | always | humans, docs |
| `goal` | complete one-line prose | always | humans, workflows |
| `value` | complete one-line prose | always | humans, workflows |
| `lifecycle` | declared ID or `UNDECLARED` | always | resume, release |
| `lifecycle_verbatim` | complete source value | iff `UNDECLARED` | migration diagnostics |
| `owner` | human `team/` handle or `unassigned` | always | resume, authority checks |
| `authority` | path relative to this file | always | resume, authority checks |
| `coordinator_route` | quoted non-empty native unit address | current statuses | all workflows |
| `upstream_route` | task: `owner:{human-handle}`; phase: `coordinator:{native-address}` | new statuses | Coordinator only |
| `owner_gateway` | `owner:{human-handle}` or `gateway:{native-address}` | historical carriers only | legacy readers |
| `dialogue` | `tfw-gates-only` or `iterative` | current statuses | all workflows |
| `activation` | `owner-only` or `delegated:{immutable-mandate-ref}` | current statuses | activation checks |
| `coordination_authority` | quoted exact local authority reference plus immutable epoch | current statuses | all workflows |
| `reporting` | `native-gates` or `owner-transfer` | current new writes | role return readers |
| `selection_ref` | `baseline` or exact `coordination_selected` journal path `@` full commit; a phase may cite its governing ancestor task journal | current new writes | authority checks |
| `outcome` | complete one-line prose | iff terminal | release, humans |
| `created` | `YYYYMMDD-HHMMSS` or `unrecorded` | always | selected readers |
| `updated` | `YYYYMMDD-HHMMSS` or `unrecorded` | always | selected readers |

Lifecycle IDs are `project_config.yaml` `tfw.statuses`: `TODO`, `HL_DRAFT`, `RES`, `PHASES`,
`TS_DRAFT`, `ONB`, `RF`, `REV`, `KNW`, `DONE`, `BLOCKED`, `REJECTED`. `PHASES` does not summarize
phase state. Terminal `DONE`/`REJECTED` require `outcome`; nonterminal states forbid it.

Migration-only `UNDECLARED` requires the verbatim source value. Tools never normalize it; an
accountable owner resolves it with a paired `transition` event from `UNDECLARED`.

The four shared coordination fields (`coordinator_route`, `dialogue`, `activation`,
`coordination_authority`) and exactly one upward-route name form a complete spine. New writes use
`upstream_route` plus `reporting` and `selection_ref`; they never emit `owner_gateway`. A task
`upstream_route` names its own human `owner`; a phase names the actual governing task Coordinator's
native address, verified against its parent status, and differs from its local
`coordinator_route`. A missing, double, malformed or wrong-ancestor route refuses. A phase's
worker gates still reach its local `coordinator_route`; the upward route carries only phase-level
returns. Total absence is legacy read-only and cannot activate new work.

An existing complete five-field `owner_gateway` carrier, with or without the selection pair,
remains readable with its actual authority. Do not silently rewrite it or infer a new parent.
Migrate a live carrier only at a safe checkpoint with an observed recipient and verified owner
choice, preserving the original event bytes and authority epoch. `baseline` means the verified
original human choice and frozen ceiling in `coordination_authority`, never a template default.
If that object cannot be verified, only dependent new authority is blocked.

The selection pair is independent of `activation`, `dialogue` and routes. Iterative dialogue
always needs an exact immutable grant naming two peers,
purpose, boundary, consolidator, durable output and stop; the Reviewer is neither peer nor
consolidator. `owner-transfer` requires an explicit human selection and disables inter-agent sends,
not role artifacts or owner-reserved decisions. A pending selection event changes nothing until its
named checkpoint; only an effective selection is reflected here. At adoption inspect the referenced
immutable event and commit, actual human source, old/new values, task/phase/role scope, condition,
reservations and HL ceiling. A phase may cite only its exact governing ancestor task event whose
content explicitly covers that phase; sibling or foreign paths refuse. Journal event refs stay
task-contained. Status remains the only effective selection; do not replay events into parallel
state or consult root live status continuously for phase permission.

Read second-resolution times from the clock. Use `unrecorded` with no source time and
`YYYYMMDD-000000` for a known legacy date with unknown time.

No history, event pointers, or prose paragraphs. Events live in `journal/`; detail in the authority.

Before writing, validate all fields and the fixed body together, even for a one-field repair.
Resolve `authority` from this file to an existing artifact inside the project; inspect the actual
governing lineage and human owner. A terminal outcome describes an actually accepted result,
not an intended effect. Apply `conventions.md` → `Closing and record recovery` before DONE or
repairing a terminal carrier. An unchanged accepted result permits record-only repair and stop;
unknown acceptance or changed output does not. Do not invent a transition to repair a missing field.
-->
