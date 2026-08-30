---
handle: handle
name: Display Name
type: human
since: YYYY-MM-DD
---

**Participant profile.** Declared attribution, not authentication. This file says who a
handle refers to; it grants nothing and verifies nothing.

<!--
CANONICAL TEMPLATE — copy into team/ as {handle}.md, one file per participant.

WHAT team/ IS, since you are probably standing in a directory that was just created:
one file per PERSON. It is the whole answer to "who is `saubakirov` in this journal event".

WHERE A ROLE GOES. The four keys below are the whole schema, and nobody invents a fifth. A
participant's role and context -- "head of the lab, author of the method" -- are recorded in
`team/README.md`, a file the parser skips and a person reads. `since` is the date the
participant joined the project.

| Key    | Bound                                  | Read by |
|--------|----------------------------------------|---------|
| handle | `[a-z0-9][a-z0-9-]*`, matches filename | status.md owner, journal on_behalf_of, index |
| name   | <= 80 code points                      | index, journal rendering |
| type   | `human` or `agent`                     | index, attribution |
| since  | YYYY-MM-DD                             | index |

Create this file BEFORE the first durable write of a session — before any status.md
change, any journal event, any commit. Every event carries an `on_behalf_of`, and it names a
handle declared here. It is always a human.

`type: agent` IS ADMITTED BY THE SCHEMA AND USABLE BY NOTHING. Naming a writer needs a
principal that delegates and answers to someone, and that is TFW-54; until it lands, team/
holds people and every profile here is a human's. Until then, do NOT create a profile per agent session to get
past a validator — two external projects were forced into exactly that, and one later
deleted those profiles and left its gate red permanently, because events are immutable and
profiles are not. Nothing asks you to name a writer, so nothing needs a profile for one.

The full rules — how a session resolves which handle is acting, the three identity
fields and what each answers, why identity is never inferred from an OS username, and
why the per-machine binding lives outside the project tree — are in `conventions.md` §4.
They are not repeated here: a second copy of a rule is a second thing to keep true.
-->
