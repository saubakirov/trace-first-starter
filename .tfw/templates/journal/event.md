---
time: YYYY-MM-DDTHH:MM:SS+ZZ:ZZ
kind: transition
on_behalf_of: handle
via: claude
from: TS_DRAFT
to: ONB
refs:
  - ONB__phase-a__title.md
summary: one line, at most 120 code points
---

<!--
CANONICAL TEMPLATE — copy into a task's journal/ as
    <YYYYMMDD-HHMMSS>__<kind>__<token>.md

A phase directory carries its own journal/ on this same grammar, exactly as it carries its
own status.md. Every consumer reads every journal a task holds.

THE FILENAME IS THE EVENT IDENTIFIER. Nobody allocates it and nothing counts events. Take
the clock, draw a token, write the file.

THE TOKEN HAS EXACTLY ONE JOB: two writes in one second cannot share a name. Four hex
characters. It is NOT an identity — it names nobody, needs no profile, and is checked
against nothing, because uniqueness is the whole of what it does. If it ever acquires a
second job, it is the wrong mechanism.

    20260827-100100__handoff__9f2c.md
    20260827-100100__handoff__a41b.md     same second, same kind, two events, no collision

IF THAT EXACT NAME IS TAKEN, draw another token. Not a counter — a counter is the shared
state this model exists to remove. And not the next second: the clock is read ONCE and the
reading is used exactly as it was read, never incremented, rounded or composed. An
arithmetic successor once wrapped 23:59:59 to 00:00:00 while keeping yesterday's date and
shipped an event claiming to precede the one it followed.

WHY THE TOKEN AND NOT A NAME. This component used to be the actor handle, and that handle
was carrying two unrelated jobs: say who wrote this, and make the name unique. They
contradict each other — a distinct writer needs a distinct value, a declared handle needs a
profile in team/ — so two external projects created a profile per agent session, and one
later deleted those profiles and left its gate red permanently. Events are immutable;
profiles are not. The operators followed the design and the design contradicted itself.

TWO IDENTITY FIELDS, and they answer two different questions:

| Field          | Answers                | Value |
|----------------|------------------------|-------|
| `on_behalf_of` | who is accountable     | ALWAYS a human handle, declared in team/ |
| `via`          | what produced it       | free-form, non-empty provider or tool text — `claude-code`, `codex`. Absent for a hand edit |

AN EVENT WITHOUT `on_behalf_of` IS INVALID AND IS REFUSED. There is no such thing as a
record nobody answers for.

A WRITER IS NOT NAMED YET. There is no third field, and that is deliberate rather than
missing. Naming a writer needs a principal that delegates and answers to someone, and TFW
does not have one until TFW-54. `via` is descriptive provenance, not a registry value and not
a writer — two sessions of one tool are two writers. A session is not a person. Inventing a per-session profile to satisfy a
validator is the failure this removed. team/ holds people.

AN `actor` ALREADY WRITTEN IS TOLERATED, NEVER REQUIRED, NEVER REWRITTEN. Every event
written before 2.0.0-dirty.3 carries it. A reader treats it as a pre-2.0.0-dirty.3 record:
no error, no comparison against team/, no dangling handle. Do not add the field to a new
event, and do not remove it from an old one.

| Key            | Bound                                        | Required |
|----------------|----------------------------------------------|----------|
| time           | ISO 8601 with offset, read from the clock    | always   |
| kind           | one value from the table below               | always   |
| on_behalf_of   | a human team/ handle                         | always   |
| via            | non-empty free-form provider/tool text       | when a tool produced the record |
| from / to      | a lifecycle id                               | both, or neither |
| refs           | at least one path, relative to the task dir  | always   |
| summary        | <= 120 code points, one line                 | optional, at most one |
| actor          | anything already written                     | never — see above |

CLOSED VOCABULARY for `kind` — no other value is valid:
| kind                | Records |
|---------------------|---------|
| created             | the task came into existence |
| dispatch            | work was handed to a named participant |
| handoff             | a role boundary was crossed: plan to execution, execution to review |
| transition          | lifecycle changed, blockage and resumption included |
| ownership_changed   | the owner field in status.md changed |
| amendment_escalated | a frozen-section change was filed for an owner verdict |
| consolidation       | RESERVED — Phases B and C, not valid yet |

SOME ARTIFACTS LEGITIMATELY HAVE NO EVENT, and that is how the vocabulary stays closed. An
artifact no `kind` covers is filed without one, and no kind is invented for it. The worked
example is an inbound advisory record — a field report from another project: it escalates
nothing and requests no verdict, and `amendment_escalated` would misreport it as awaiting a
ruling.

THE TIMESTAMP IS READ FROM THE SYSTEM CLOCK AT THE MOMENT OF WRITING. Never composed,
guessed, rounded or typed. Invented times cluster on round seconds and sometimes fall after
the events they claim to precede.

IMMUTABLE ONCE WRITTEN. A written event is never edited and never deleted. A correction is a
new event that references the one it corrects. A rule introduced later may describe older
entries but never rewrite them — which is exactly why the actor field is tolerated rather
than cleaned up.

THE 120 CODE POINT CEILING is measured, not chosen. Population: the 272 commit summaries in
this repository that name a task, and the 63 state-change summaries in existing REVIEW
verdicts. Median 38 and 9; p95 combined 83; p99 combined 110. 120 sits just above p99, so 3
of 335 real entries exceed it — and all three are multi-fact summaries that belong in an
artifact rather than in a log line. The ceiling is checkable by eye: one and a half terminal
lines.

CONTENT OVER THE CEILING MOVES INTO AN ARTIFACT and the event keeps a reference to it. This
is the single control that stops the journal becoming the next README.

An event body never copies HL, RES, TS, RF, REVIEW, evidence or chat text. It references
them. The journal records that something happened and where the detail lives; the detail
lives in the artifact that owns it.
-->
