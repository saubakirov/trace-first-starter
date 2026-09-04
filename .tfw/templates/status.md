---
id: PREFIX_YYYYMMDD-HHMMSS_ABBR
title: "short task name"
goal: "why this task exists, one line"
value: "what shipping it gives the project, one line"
lifecycle: TODO
owner: unassigned
authority: HL-PREFIX_YYYYMMDD-HHMMSS_ABBR.md
created: YYYYMMDD-HHMMSS
updated: YYYYMMDD-HHMMSS
---

**Task state.** This file is the only authority for this task's live state. The portfolio index is derived from it and never outranks it.

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
    created: 20260827-091500
    updated: 20260827-114210
    ---

The key set is closed; readers are named below.

| Key | Bound | Required | Read by |
|---|---|---|---|
| `id` | task directory ID, including readable legacy IDs | always | index, resume, docs |
| `title` | ≤80 code points | always | index |
| `goal` | ≤160 code points, one line | always | index |
| `value` | ≤160 code points, one line | always | index |
| `lifecycle` | declared ID or `UNDECLARED` | always | index, resume, release |
| `lifecycle_verbatim` | ≤80 code points | iff `UNDECLARED` | index, migration diagnostics |
| `owner` | human `team/` handle or `unassigned` | always | index, resume |
| `authority` | path relative to this file | always | index, resume |
| `outcome` | ≤160 code points, one line | iff terminal | index, release |
| `created` | `YYYYMMDD-HHMMSS` or `unrecorded` | always | index |
| `updated` | `YYYYMMDD-HHMMSS` or `unrecorded` | always | index freshness |

Lifecycle IDs are `project_config.yaml` `tfw.statuses`: `TODO`, `HL_DRAFT`, `RES`, `PHASES`,
`TS_DRAFT`, `ONB`, `RF`, `REV`, `KNW`, `DONE`, `BLOCKED`, `REJECTED`. `PHASES` does not summarize
phase state. Terminal `DONE`/`REJECTED` require `outcome`; nonterminal states forbid it.

Migration-only `UNDECLARED` requires the verbatim source value. Tools never normalize it; an
accountable owner resolves it with a paired `transition` event from `UNDECLARED`.

Read second-resolution times from the clock. Use `unrecorded` with no source time and
`YYYYMMDD-000000` for a known legacy date with unknown time.

No history, event pointers, or prose paragraphs. Events live in `journal/`; detail in the authority.
-->
