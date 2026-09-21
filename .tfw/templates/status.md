---
id: PREFIX_YYYYMMDD-HHMMSS_ABBR
title: "short task name"
goal: "why this task exists, one line"
value: "what shipping it gives the project, one line"
lifecycle: TODO
owner: unassigned
authority: HL-PREFIX_YYYYMMDD-HHMMSS_ABBR.md
coordinator_route: "native:coordinator-address"
owner_gateway: owner:human-handle
dialogue: tfw-gates-only
activation: owner-only
coordination_authority: "HL-PREFIX_YYYYMMDD-HHMMSS_ABBR.md @ full-immutable-epoch"
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
    owner_gateway: owner:saubakirov
    dialogue: tfw-gates-only
    activation: owner-only
    coordination_authority: "HL-20260827-091500__query_redesign.md @ 0123456789abcdef0123456789abcdef01234567"
    created: 20260827-091500
    updated: 20260827-114210
    ---

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
| `owner_gateway` | `owner:{human-handle}` or `gateway:{native-address}` | current statuses | Coordinator only |
| `dialogue` | `tfw-gates-only` or `iterative` | current statuses | all workflows |
| `activation` | `owner-only` or `delegated:{immutable-mandate-ref}` | current statuses | activation checks |
| `coordination_authority` | quoted exact local authority reference plus immutable epoch | current statuses | all workflows |
| `outcome` | complete one-line prose | iff terminal | release, humans |
| `created` | `YYYYMMDD-HHMMSS` or `unrecorded` | always | selected readers |
| `updated` | `YYYYMMDD-HHMMSS` or `unrecorded` | always | selected readers |

Lifecycle IDs are `project_config.yaml` `tfw.statuses`: `TODO`, `HL_DRAFT`, `RES`, `PHASES`,
`TS_DRAFT`, `ONB`, `RF`, `REV`, `KNW`, `DONE`, `BLOCKED`, `REJECTED`. `PHASES` does not summarize
phase state. Terminal `DONE`/`REJECTED` require `outcome`; nonterminal states forbid it.

Migration-only `UNDECLARED` requires the verbatim source value. Tools never normalize it; an
accountable owner resolves it with a paired `transition` event from `UNDECLARED`.

The five coordination fields are an all-or-none routing spine. Total absence is accepted only when
reading legacy status and cannot activate a current workflow. Partial presence is invalid. Current
writers require all five. `owner_gateway: gateway:{native-address}` and `dialogue: iterative` require
an exact immutable grant in `coordination_authority`; otherwise use `owner:{human-handle}` and
`tfw-gates-only`. An authorized active status may add the complete spine without a same-state event;
the lifecycle did not change.

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
