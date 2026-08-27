# Map — TFW-60 / Phase A review revision 4

> **Mindset:** Map. Establish the contract, supported operating model, and review surface
> before judging the result.

## Review identity

- Reviewer: `saubakirov`, via Codex
- RF: `RF__phase-a__task_state_and_coordination.md`, revision 3
- TS: `TS__phase-a__task_state_and_coordination.md`, revision 5
- Implementation snapshot claimed and independently resolved: `afd24f5`
- Report commit at review start: `26f0df4`
- Historical verdicts are inputs, not files to replace: first review, revision 2, and revision 3

## Owner-directed boundary

This is a **quality-only** review. By explicit owner direction:

- file counts, line counts, diff size, scope-budget ratios, and census volume are excluded
  from the verdict;
- the prior formal budget approval remains settled and is not re-litigated;
- deliberately writing records in a retired grammar, deliberately corrupting profiles, or
  otherwise trying to defeat the rules is not part of the operating model being judged;
- ordinary supported TFW workflows, ordinary configuration, migration, compatibility,
  validation, reproducibility, and accidental errors named by the TS remain in scope.

No volume assertion can make this review pass or fail.

## Contract map

The master purpose remains task locality: different tasks must advance without a common edit,
and another participant must be able to discover the task's live state from filesystem traces.
The Phase HL narrows that purpose to task-local status, immutable journal events, participant
attribution, migration, and a derived non-authoritative index. TS revision 5 adds the bounded
third-pass corrections in AC-14.

The quality-critical third-pass obligations are:

| Obligation | Accepted behavior |
|---|---|
| Participant accountability | Production validation refuses a current event when `team/` is absent or empty, rejects undeclared actors, and requires `on_behalf_of` to resolve to a declared human |
| Legacy compatibility | Immutable pre-2.0.0 actorless records remain readable; the current published grammar is actor-bearing |
| Production-path coverage | Tests drive both `collect` and `--validate`, rather than proving only an injected helper path |
| Canonical naming | `{ID}` means the complete clock-and-slug identifier; canonical event examples include the actor |
| Evidence reproducibility | RF and EV name a resolved implementation commit and provide rerunnable commands against it |

## Previous finding disposition

| Revision 3 item | Revision 4 mapping |
|---|---|
| Identity validation failed open and discarded profile type | Closed in production paths: the empty/missing-team, undeclared-actor, agent-accountability, and declared-human cases are exercised and behave as specified |
| Canonical naming had two meanings | Closed: current instructions and templates use the whole identifier and actor-bearing event grammar; the regression guard covers the shipped surface |
| RF/EV mixed changing snapshots | Closed: the evidence is pinned to `afd24f5`, which resolves independently and is distinct from the later report commit |

## Quality surface inspected

The inspection covered the current HL/TS/RF/EV chain; implementation at the pinned snapshot;
the state, journal, profile, migration, and index paths; shipped workflow/template surfaces;
tests for both direct rules and production entry points; the release-facing documentation
hierarchy; adapter parity; current repository state; and every prior review item.

The exploratory possibility of hand-constructing a current record with the retired actorless
filename, or hand-corrupting a profile specifically to evade its declaration, is not promoted
to a finding. It is outside the owner-directed non-adversarial operating model and is not how
the current workflows instruct a record to be written.

## Contract and citation integrity

The master HL, Phase HL, TS, RF, EV, and ONB references resolve. The citation-bearing surfaces
did not change in the third corrective pass. Revision 3's disclosed historical ONB relevance
discrepancy remains exactly that: preserved historical understanding, explicitly routed in RF
observation 12, and not a defect introduced or concealed by this result.

Stage complete: YES
