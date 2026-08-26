---
time: YYYY-MM-DDTHH:MM:SS+ZZ:ZZ
kind: transition
actor: handle
from: TS_DRAFT
to: ONB
refs:
  - ONB__phase-a__title.md
summary: one line, at most 120 code points
---

<!--
CANONICAL TEMPLATE — copy into a task's journal/ as YYYYMMDD-HHMMSS__{kind}.md.

THE FILENAME IS THE EVENT IDENTIFIER. Nobody allocates it and nothing counts events.
Take the clock, write the file. Two participants appending at the same moment create two
different files, so a concurrent append cannot contend for a byte range.

IMMUTABLE ONCE WRITTEN. A written event is never edited and never deleted. A correction
is a new event that references the one it corrects.

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

| Key     | Bound                                        | Required |
|---------|----------------------------------------------|----------|
| time    | ISO 8601 with offset                         | always   |
| kind    | one value from the table above               | always   |
| actor   | a team/ handle                               | always   |
| from/to | a lifecycle id, or omitted when none changed | iff the event changed state |
| refs    | at least one path, relative to the task dir  | always   |
| summary | <= 120 code points, one line                 | optional, at most one |

THE 120 CODE POINT CEILING is measured, not chosen. Population: the 272 commit summaries
in this repository that name a task, and the 63 state-change summaries in existing REVIEW
verdicts. Median 38 and 9; p95 combined 83; p99 combined 110. 120 sits just above p99, so
3 of 335 real entries exceed it — and all three are multi-fact summaries that belong in an
artifact rather than in a log line. The ceiling is checkable by eye: one and a half
terminal lines.

CONTENT OVER THE CEILING MOVES INTO AN ARTIFACT and the event keeps a reference to it.
This is the single control that stops the journal becoming the next README.

An event body never copies HL, RES, TS, RF, REVIEW, evidence or chat text. It references
them. The journal records that something happened and where the detail lives; the detail
lives in the artifact that owns it.
-->
