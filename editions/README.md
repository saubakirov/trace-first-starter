# TFW Editions

TFW Editions provide different amounts of discipline for different kinds of work. Copy the **contents** of one edition directory into a project root; do not work inside the edition directory itself.

| Edition | Choose it when | Included discipline | Availability |
|---|---|---|---|
| **Light** | Work is compact, one person is responsible, and visible manual updates are acceptable | Goal, task list, trace and durable memory in four short files | [`01-light/`](01-light/) |
| **Assisted 1.5** | Work repeats, several participants need explicit ownership, or execution and review should be separated | Result-first planning, stable task traces, handoff, independent review, human acceptance, participant identity, safe updates and practical templates | [`02-assisted/`](02-assisted/) |
| **Full** | Work is long-running, regulated or expensive to get wrong | Formal HL → RES → TS → ONB → RF → REVIEW lifecycle with evidence and knowledge gates | [`.tfw/`](../.tfw/) |

Choose the smallest edition whose missing discipline would create an observable risk. Editions are not maturity levels and do not depend on one another at runtime.

## Assisted capability boundary

Assisted 1.5 is a standalone Russian-authoritative starter. Its normal lifecycle is manual: `/tfw-plan` prepares and approves the trace, `/tfw-handoff` executes it, `/tfw-review` performs an independent review, and a human accepts the final result. A runtime may coordinate separate tasks only after it verifies the required operations and the exact target before each dispatch. Missing capability means a complete manual path, not a hidden or degraded hook mode.

Assisted ships no lifecycle hooks. It does not claim automatic startup, checkpoint or finish enforcement. Participant bindings are local declarations, not authentication, and persistent storage is used only when locality can be positively established; otherwise the current session remains usable without a persistent write.

## Moving between editions

- **Start Light:** copy `01-light/` contents into a clean project root and follow its README.
- **Light or an installed Assisted project → Assisted 1.5:** follow [`02-assisted/MIGRATION.md`](02-assisted/MIGRATION.md). Preserve project identity, work, knowledge, profiles and customization.
- **Any edition → Full:** adopt `.tfw/` when the work needs the complete formal lifecycle.

Public Assisted maintenance is asymmetric. The public package may update a clean downstream core through classified, baseline-checked changes. A downstream improvement returns only as a non-mutating generic candidate that receives independent privacy and semantic review before a later public release. See [`ASSISTED_MAINTENANCE.md`](ASSISTED_MAINTENANCE.md).
