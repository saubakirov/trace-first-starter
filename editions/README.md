# TFW Editions

TFW Editions provide different amounts of discipline for different kinds of work. Copy the **contents** of one edition directory into a project root; do not work inside the edition directory itself.

| Edition | Choose it when | Included discipline | Availability |
|---|---|---|---|
| **Light** | Work is compact, one person is responsible, and visible manual updates are acceptable | Goal, task list, trace and durable memory in four short files | [`01-light/`](01-light/) |
| **Assisted 1.6** | Work repeats, several participants need explicit ownership, or execution and review should be separated | Result-first planning, stable task traces, handoff, independent review, human acceptance, participant identity, safe updates and practical templates | [`02-assisted/`](02-assisted/) |
| **Full** | Work is long-running, regulated or expensive to get wrong | Formal HL → RES → TS → ONB → RF → REVIEW lifecycle with evidence and knowledge gates | [`.tfw/`](../.tfw/) |

Choose the smallest edition whose missing discipline would create an observable risk. Editions are not maturity levels and copied editions do not depend on one another.

## Assisted capability boundary

Assisted 1.6 is a standalone Russian-language starter and a neutral derivative of field-proven behavior. Its complete manual lifecycle is `/tfw-plan` → `/tfw-handoff` → `/tfw-review` → human acceptance. Codex may expose execution and review as separate owner-visible tasks; another provider may realize the same role boundary through its own available sessions. Missing task operations leave the documented manual path complete.

Assisted ships no lifecycle, identity, update, maintenance, or synchronization runtime. The only executable is the optional A4 user-artifact builder. Participant choice follows the Markdown profile procedure and is declared attribution, not authentication. Assisted and Full both use the nouns `team/` and `workspace/`, but their schemas, lifecycles, bindings, readers, writers, and authority remain independent.

## Moving between editions

- **Start Light:** copy `01-light/` contents into a clean project root and follow its README.
- **Light or an installed Assisted project → Assisted 1.6:** follow [`02-assisted/MIGRATION.md`](02-assisted/MIGRATION.md). Preserve project identity, task history, knowledge, profiles and customization through its exact old-source → new-target map.
- **Any edition → Full:** adopt `.tfw/` when the work needs the complete formal lifecycle; do not treat matching directory names as schema compatibility.

Public Assisted maintenance is asymmetric, provider-neutral and human-gated. A publisher documents an exact versioned source outside the replaceable package; the updater materializes a safe closed tree, records a dynamic observed manifest and rechecks it before one explicit write gate. A downstream improvement returns only as a non-mutating privacy-clean generic candidate for separate review. This repository does not claim that a GitHub Release or another public shelf already exists. See [`ASSISTED_MAINTENANCE.md`](ASSISTED_MAINTENANCE.md).
