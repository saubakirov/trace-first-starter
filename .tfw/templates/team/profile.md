---
handle: handle
name: Display Name
type: human
since: YYYY-MM-DD
---

**Participant profile.** Declared attribution, not authentication. It grants and verifies
nothing.

<!--
CANONICAL TEMPLATE — copy into team/ as {handle}.md, one file per participant.

A principal is a stable project-local handle backed by a valid human or agent profile. It is
never a provider, model, executable, process, session, workflow role, or directly addressable
working unit. Never create one per run, session, Coordinator, Researcher, Executor, or Reviewer.
One selected LEAD principal may attribute several distinct units without merging their addresses,
parents, work, or proposal origins.

| Key | Bound | Human | Agent |
|---|---|---|---|
| `handle` | `[a-z0-9][a-z0-9-]*`; matches filename | required | required |
| `name` | non-empty; ≤80 code points | required | required |
| `type` | `human` or `agent` | required | required |
| `since` | `YYYY-MM-DD` | required | required |
| `organization_role` | description or `not_applicable` | optional | optional |
| `project_role` | description or `not_applicable` | optional | optional |
| `accountable_to` | existing human handle | forbidden | required |
| `may_rule_amendments` | Boolean `true` or `false` | forbidden | required |
| `mentality` | non-empty guidance | forbidden | optional |

The original four keys remain a valid human profile. Optional roles must be non-empty;
omitted means unknown/not supplied, while exact `not_applicable` means known not to apply.
Roles are context, never authentication, permission, task scope, or workflow role.

An agent is valid only when `accountable_to` resolves to `type: human` and the grant is a YAML
Boolean. The grant has exactly two levels but creates no route or permission. A `true` grant is
eligible only for the owner-selected LEAD's root Coordinator unit inside its approved mandate;
children sharing principal attribution never inherit it. Never redefine an existing principal's
grant; a change requires a new handle/profile. `mentality` guides style only and cannot imply
authority, alter permissions, or change a Role Lock.

Compatible four-key human:

```yaml
---
handle: saubakirov
name: Sanzhar Aubakirov
type: human
since: 2025-09-08
---
```

Agent principal that may rule amendments:

```yaml
---
handle: method-ruler
name: Method Ruler
type: agent
since: 2026-09-05
organization_role: not_applicable
project_role: phase coordinator
accountable_to: saubakirov
may_rule_amendments: true
mentality: critical opponent
---
```

Create a profile before a binding or current `writer` names it. Every event still carries
human `on_behalf_of`. Full writer, tool, token, and binding semantics: `conventions.md` §4.
-->
