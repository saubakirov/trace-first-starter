---
time: YYYY-MM-DDTHH:MM:SS+ZZ:ZZ
kind: transition
on_behalf_of: handle
via: codex
from: TS_DRAFT
to: ONB
refs:
  - ONB__phase-a__title.md
summary: "one line, at most 120 code points"
---

<!--
BEFORE WRITING, validate every bound below. Copy to the task or phase `journal/` as
`<YYYYMMDD-HHMMSS>__<kind>__<token>.md`. Read the clock once and reuse that observed second for the
filename and ISO time; draw four hex characters. On an exact-name collision draw again without
changing the time. The filename is the event identity; the token has no other meaning.

| Key | Bound | Required |
|---|---|---|
| `time` | ISO 8601 with offset, read from the clock | always |
| `kind` | one current kind below | always |
| `on_behalf_of` | declared human `team/` handle | always |
| `via` | non-empty free-form provider/tool text | when a tool writes |
| `from` / `to` | declared lifecycle IDs and a permitted pair | both or neither |
| `refs` | non-empty paths relative to the task directory | always |
| `summary` | ≤120 code points, one line | optional, at most one |
| `actor` | any value already present | never issue; legacy read only |

Current kinds are closed: `created`, `dispatch`, `handoff`, `transition`, `ownership_changed`, and
`amendment_escalated`. `consolidation` is reserved and invalid until separately authorized. If no
kind describes an artifact, write no event; never invent a kind.

`on_behalf_of` always names the accountable human. `via` names the producing tool and is neither an
identity nor an enum. A current event without `on_behalf_of` is refused. A legacy `actor` is
tolerated exactly as written, never validated, added, removed, or rewritten.

A transition requires both `from` and `to`; non-transition state pairs and illegal lifecycle edges
are refused before installation. Phase events use the phase-local journal and the same schema.

Events are immutable once written. Correct by appending a new event that references the old one.
The body never copies artifact or chat content; put detail in its owning artifact and cite it through
`refs`. Content over the summary ceiling moves there too.
-->
