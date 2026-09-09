---
time: YYYY-MM-DDTHH:MM:SS+ZZ:ZZ
kind: transition
writer: handle
on_behalf_of: handle
via: codex
from: TS_DRAFT
to: ONB
refs:
  - ONB__phase-a__title.md
summary: "brief one-line summary, normally no more than 120 code points"
---

<!--
BEFORE WRITING, validate every structural rule. Copy to the task or phase `journal/` as
`<YYYYMMDD-HHMMSS>__<kind>__<token>.md`. Read the clock once; reuse that second for filename and ISO
time; draw four hex characters. On collision redraw without changing time. The filename is event
identity; the token means only uniqueness.

| Key | Shape or guidance | Required |
|---|---|---|
| `time` | ISO 8601 with offset, read from the clock | always |
| `kind` | one current kind below | always |
| `writer` | declared human or valid agent principal handle | optional |
| `on_behalf_of` | declared human `team/` handle | always |
| `via` | non-empty free-form provider/tool text | when a tool writes |
| `from` / `to` | declared lifecycle IDs and a permitted pair | both or neither |
| `refs` | non-empty paths relative to the task directory | always |
| `summary` | one line; brief, normally no more than 120 code points (authoring advice, never validity) | optional, at most one |
| `actor` | any value already present | never issue; legacy read only |

Current kinds are closed: `created`, `dispatch`, `handoff`, `transition`, `ownership_changed`,
`amendment_escalated`. `consolidation` is reserved. If no kind fits, write no event; never invent one.

Optional `writer` names a declared principal; never derive it from `via`, OS/account identity,
hostname, model, session, folder, or token. `on_behalf_of` names the accountable human, `via` is
non-empty free-form tool text, and the token supplies uniqueness only. A current event without `on_behalf_of` is refused.
Legacy `actor` is accepted exactly as written, never required, issued,
validated under current principal rules, removed, or rewritten.

For `kind: dispatch`, `writer` remains optional principal attribution and never stands for a unit
edge. The body/summary plus refs must preserve the actual source, destination and parent units,
workflow role and bounded scope, direct address/channel, governing artifacts, and originating
proposer `{principal, unit}` or explicit `none`. Identical writers never merge units; forwarding,
restart or continuation never changes the recorded origin. Add no frontmatter key for these facts.

A transition requires both `from` and `to`; non-transition state pairs and illegal lifecycle edges
are refused. Phase events use the phase-local journal and this schema.

Validate the complete proposed event before writing, including actual authority and referenced
artifacts. Resolve each ref from the owning task/phase directory, not `journal/`; require a nonempty
relative filesystem path contained within that task/phase and open the target. Absolute paths, URIs,
escaping traversal and missing targets are refused. Follow a local authority artifact for ancestor
lineage rather than place an escaping ref here. Verify any cited immutable object's existence and
claimed content; an invented SHA cannot support an act.

For an interrupted or erroneous close, apply `conventions.md` → `Closing and record recovery`.
Preserve the old event bytes. A present correction names the error and actual act with the current
clock and an existing truthful kind; no backdated reconstruction or same-state transition. If no
kind fits, do not invent one. Validate the repaired carrier/references and stop when only the record
changed; material or uncertain acceptance returns through its actual authority.

Events are immutable once written. Correct by appending a new event that references the old one.
The body never copies artifact or chat content; put detail in its owning artifact and cite it through
`refs`. Keep the summary easy to scan without truncating or rejecting a complete source value.
-->
