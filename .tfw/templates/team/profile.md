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
One optional principal may attribute several distinct units without merging their addresses,
parents, work, authority, or proposal origins.

| Key | Bound | Human | Agent |
|---|---|---|---|
| `handle` | `[a-z0-9][a-z0-9-]*`; matches filename | required | required |
| `name` | non-empty; ≤80 code points | required | required |
| `type` | `human` or `agent` | required | required |
| `since` | `YYYY-MM-DD` | required | required |
| `organization_role` | description or `not_applicable` | optional | optional |
| `project_role` | description or `not_applicable` | optional | optional |
| `accountable_to` | existing human handle | forbidden | required |
| `may_rule_amendments` | legacy Boolean `true` or `false` | forbidden | optional; read-only |
| `mentality` | non-empty guidance | forbidden | optional |

The original four keys remain a valid human profile. Optional roles must be non-empty;
omitted means unknown/not supplied, while exact `not_applicable` means known not to apply.
Roles are context, never authentication, permission, task scope, or workflow role.

An agent is valid only when `accountable_to` resolves to `type: human`. A historical
`may_rule_amendments` Boolean remains readable but is never issued and grants no route, activation
or amendment authority. Current authority comes only from the exact immutable object named by the
task routing spine. `mentality` guides style only and cannot alter permissions or a Role Lock.

Compatible four-key human:

```yaml
---
handle: saubakirov
name: Sanzhar Aubakirov
type: human
since: 2025-09-08
---
```

Current agent principal:

```yaml
---
handle: method-ruler
name: Method Ruler
type: agent
since: 2026-09-05
organization_role: not_applicable
project_role: phase coordinator
accountable_to: saubakirov
mentality: critical opponent
---
```

New agent profiles omit `may_rule_amendments`. Create a profile before a binding or current `writer` names it. Every event still carries
human `on_behalf_of`. Full writer, tool, token, and binding semantics: `conventions.md` §4.
-->
