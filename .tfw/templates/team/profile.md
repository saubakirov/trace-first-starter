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
one file per participant, humans and agents alike. That is why it is team/ and not
people/. It is the whole answer to "who is `saubakirov` in this journal event".

| Key    | Bound                                  | Read by |
|--------|----------------------------------------|---------|
| handle | `[a-z0-9][a-z0-9-]*`, matches filename | status.md owner, journal actor, index |
| name   | <= 80 code points                      | index, journal rendering |
| type   | `human` or `agent`                     | index, attribution |
| since  | YYYY-MM-DD                             | index |

Create this file BEFORE the first durable write of a session — before any status.md
change, any journal event, any commit. Every event carries an `actor` and an
`on_behalf_of`, and both name a handle declared here. `on_behalf_of` is always a human.

The full rules — how a session resolves which handle is acting, the three identity
fields and what each answers, why identity is never inferred from an OS username, and
why the per-machine binding lives outside the project tree — are in `conventions.md` §4.
They are not repeated here: a second copy of a rule is a second thing to keep true.
-->
