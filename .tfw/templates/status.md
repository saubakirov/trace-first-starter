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
CANONICAL TEMPLATE — copy into a task directory as status.md and fill every key.

Format: YAML front matter, then the one fixed sentence above. Nothing else.
The file has no free-text body. Explanation belongs in the HL; events belong in journal/.

QUOTE EVERY PROSE VALUE. title, goal, value, outcome and lifecycle_verbatim are sentences,
and a sentence is where a colon shows up. A colon FOLLOWED BY A SPACE ends a YAML plain
scalar, so this is not a long title, it is a syntax error:

    title: Phase AA: portable delivery          <- INVALID, the file will not parse

Quoted, it is a string, and any punctuation inside it is just text:

    title: "Phase AA: portable delivery"        <- valid

The example above therefore quotes them. The six keys that are never prose — id, lifecycle,
owner, authority, created, updated — do not need it. Measured cost of getting
this wrong: five hand-written files in a row, all unparseable, on the first project to
hand-author this carrier. `gen_index.py --check tasks` now names the offending key.

A COMPLETE, VALID EXAMPLE — copy this rather than the skeleton if you are writing by hand:

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

    **Task state.** This file is the only authority for this task's live state. The portfolio index is derived from it and never outranks it.

A PHASE FILE — `{task}/phase-x/status.md` — uses the SAME keys and a DIFFERENT fixed
sentence, so a reader can tell the two apart without opening the directory:

    **Task state.** This file is the only authority for this phase's live state. The task-level `status.md` never summarizes it.

Which one to use: in the task directory, the task sentence above the comment; in a `phase-*`
directory, the phase sentence. `id` carries the TASK's identifier in both; `authority` points
at the phase's own TS or HL. A phase file is written by hand when its directory is created,
and never by migration -- the board never held per-phase state, so `--check tasks` names a
phase directory that has none.

CLOSED KEY SET — no key may be added without a convention change, and no key may be
present without a named reader. A field nothing reads does not belong here.

| Key                  | Bound                                   | Required        | Read by |
|----------------------|-----------------------------------------|-----------------|---------|
| id                   | the task's own directory name, or a legacy `[A-Z]+-\d+` | always | index, resume, docs generator |
| title                | <= 80 code points                       | always          | index |
| goal                 | <= 160 code points, one line            | always          | index |
| value                | <= 160 code points, one line            | always          | index |
| lifecycle            | one declared status id, or UNDECLARED   | always          | index, resume, release |
| lifecycle_verbatim   | <= 80 code points                       | iff UNDECLARED  | index, migration diagnostics |
| owner                | a team/ handle, or `unassigned`         | always          | index, resume |
| authority            | path relative to this file              | always          | index, resume |
| outcome              | <= 160 code points, one line            | iff terminal    | index, release |
| created              | YYYYMMDD-HHMMSS                         | always          | index |
| updated              | YYYYMMDD-HHMMSS                         | always          | index freshness |

lifecycle takes one of the ids in project_config.yaml `tfw.statuses`:
TODO · HL_DRAFT · RES · PHASES · TS_DRAFT · ONB · RF · REV · KNW · DONE · BLOCKED · REJECTED

PHASES belongs to a multi-phase task and means its phases are running. It NEVER summarizes
what they are doing: each phase directory carries its own status.md on this same schema, and
a task-level rollup would be a second fact that has to agree with them — the two-file
synchronization problem this carrier exists to avoid.

TIME IS RECORDED TO THE SECOND, in the same grammar as the identifier. A day-resolution
stamp says almost nothing on a corpus that takes several transitions a day: at day
resolution `created` and `updated` are routinely identical and `updated` stops answering the
question it exists for. The value is READ from the system clock, never composed or typed.

`unrecorded` is the honest value when a source never carried the fact. A day-only legacy
source migrates to that day with a DECLARED zero time — `20260819-000000` means "this day,
time unknown", and must never be read as second-accurate history.

Terminal ids are DONE and REJECTED. A terminal task carries `outcome` and keeps its
directory and its path forever.

UNDECLARED is not a lifecycle a person selects. Migration writes it when a legacy source
carried a value outside the vocabulary, and puts that value verbatim in
lifecycle_verbatim. A consumer treats UNDECLARED as non-actionable and reports it.

MIGRATION NEVER NORMALIZES IT. AN ACCOUNTABLE OWNER MAY RESOLVE IT — by setting the correct
value and recording a `transition` event carrying `from: UNDECLARED`. Two different acts: a
tool has no basis for the choice, a person does, and the event is what makes the resolution
a trace rather than a silent rewrite. Full rule and the two-act table: conventions.md §5.
Read as an absolute prohibition, this strands tasks at a value every consumer treats as
non-actionable — or gets them fixed with no record, which is worse.

WHAT DOES NOT GO HERE
- the last event id, the journal head, or any pointer duplicating a journal fact: two
  files that must agree is the synchronization problem that previously required an engine
- history of any kind: a state change is an event, and events are files in journal/
- prose: if a fact needs a paragraph, it is HL content and this file links to it
-->
