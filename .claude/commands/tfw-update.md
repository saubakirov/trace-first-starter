---
description: TFW Update — upgrade from one immutable applicable payload
---

# TFW Update — Framework Upgrade Workflow

> 🔒 **ROLE LOCK: COORDINATOR.** Apply only authorized framework/config/adapter migrations and one
> project-owned receipt. Never perform project implementation, task lifecycle work, new external
> effects, or writes before source/authority gates resolve.

## Read Contract

Root instructions are active. Until a target is pinned, this installed workflow is the only update
contract; afterward the pinned target's `update.md` governs.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | selected task/phase `status.md`, `journal/`, when task-bound | routing and lineage | task-local |
| 2 | `.tfw/project_config.yaml` → `tfw.upstream`, installed provenance/project keys; `.tfw/VERSION`; receiver `.tfw/README.md` when present | source, version, receiver purpose | installed project/config |
| 3 | operator tag or explicitly authorized immutable commit and its `.tfw/VERSION` | one target | owner/Git object |
| 4 | pinned `.tfw/.upstream/.tfw/workflows/update.md` | target algorithm | pinned target |
| 5 | intervening pinned CHANGELOG ranges and every named/applicable migration; target migration at equal version/unfinished attempt; `{major}.0.0.md` on a major crossing | migration obligations | pinned history/receiver evidence |
| 6 | `.tfw/adapters/manifest.yaml`; briefing and update-receipt templates at their gates | copies and outputs | manifest/templates |

Never read live source HEAD, unpinned target files, full changelog/common libraries or project-state
bodies. Missing/incoherent target workflow, range or required guide stops.

## Step 0 — Activation and pin

Apply root activation/routing before pinning or writing; require exact owner-direct `/tfw-update` and,
when task-bound, the actual Coordinator. Preserve legacy statuses. Add a complete routing spine only
when accountable authority supplies all five exact values; otherwise report the missing decision.

Resolve `tfw.upstream` to a local Git checkout. The operator names a tag or explicitly authorizes an
untagged commit. Resolve the object, read its VERSION, and for a tag require `v{VERSION}`. Local
source must be clean under `.tfw/`. Record locator, full SHA, version and source path; materialize
exactly that object with `git archive` into `.tfw/.upstream/`. Recheck immutability before adapter
sync. Version equality or a prior receipt never proves completion.

For an authorized untagged Candidate, set installed version from target VERSION and
`tfw.installed_from` to configured upstream plus full Candidate SHA; receipt/outcome label it
untagged and never claim a release tag.

## Step 1 — Target history and authority

Read pinned target `update.md` before target writes. Verify workflow, manifest, templates, required
changelog ranges and migrations come from the same object. At equal version, re-observe target
identity, provenance, checks, receipt/cleanup/final-message state; read that version's migration entry
and unfinished/preservation records. If present, `migrations/knowledge-lifecycle.md` always applies.
For 3.3.0, read `migrations/3.3.0.md` before any already-current result. Unknown/custom installed
versions, absent guides or changelog/guide contradictions stop with a concrete next action.

Discover accountable human, task containers, checks, customizations and grants from project
evidence—never Git/OS/path/provider/model/receipt. Stable principal attribution requires an immutable
mandate or provenance need. Ask one short material question only when evidence cannot settle project
meaning, consequential choice or external effect; Update cannot create delegation or iterative
dialogue.

## Step 2 — Observe, classify, and preview

Compare installed payload with target before writes; group connected semantic effects. Update
authority covers coherent framework-owned changes and prescribed compatible migration, not new
project decisions or external effects.

Never overwrite `.tfw/knowledge_state.yaml`, `knowledge/`, `KNOWLEDGE.md`, task history, profiles,
grants, receipts, preservation attachments, root `README.md`, configured project checks or unrelated
content. Merge project config key-by-key: preserve `build.*`, scope budgets, task containers and owner
answers; update framework-owned keys; remove only target-declared retired keys.

Classify current `.tfw/README.md`: replace a verified framework-owned copy; preserve customized,
project-purpose or frozen-citation bytes first at
`.tfw/update_receipts/legacy-readme/<sha256>/README.md`; leave an absent project North Star absent and
never inject starter quotation. Reuse identical attachment; different-byte collision stops. If
purpose remains ambiguous, ask one material question.

For every non-mechanical choice record fact, authority/currentness, semantic effect, permitted action
and resolving evidence. Preview groups, exclusions, preservation, migrations, checks, unresolved
choices and exact target; do not demand per-file approval already supplied by update authority.

## Step 3 — Apply connected groups

Copy approved pinned payload by connected group while reporting exclusions; merge config separately.
Stop a whole group on dependency failure. Diagnostic staging/preservation is a disclosed write.
Destructive cleanup follows verified preservation and replacement only. Re-entry observes current
receiver; partial application, equal version or old receipt never closes checks/cleanup/reporting.

- **Knowledge lifecycle:** pinned guide owns reader/adapter/config/entry group. Preserve old/intended
  before-images, install mixed-compatible readers first, retire only named live keys/instructions,
  preserve historical state/topic/source meaning, and perform no every-fact conversion. Revalidate
  each field; old/intended may continue, a third value refuses. Completed identical repeat verifies
  without another promotion.
- **Active/historical containers:** pinned 3.3.0 guide owns cases/recovery. Preserve exact
  before-image and membership/digest pairs, install compatible readers, revalidate/reconcile, then
  publish config. Finish/refuse before knowledge-lifecycle adoption; never restore a whole digest map.
- **Scope budgets:** atomically map `max_files_per_phase`→`decomposition_trigger_files` and
  `max_loc`→`decomposition_trigger_loc` preserving values; retire `max_new_files` and
  `max_modified_files`; add `owner_escalation_multiplier: 2`. Mixed old/new blocks stop; historical
  task approvals retain their epoch semantics.

## Step 4 — Adapters, verification, receipt, outcome

At adapter sync, if a persistent coordination block changes, read `Workflow activation and routing`;
otherwise it is uncharged. Validate four adapters and ten manifest commands. Apply exact copies or
one marker-bounded block; preserve unmarked/foreign neighbors. Antigravity installs to plural
`.agents`; singular `.agent/rules` remains compatible rule location, never inferred workflow support
or deletion authority. Reject missing/extra commands, wrong roles/paths, duplicate blocks, drift or
second-run diff; allow retired terms only where intervening history names them.

Verify target ref/SHA/version/tag, source coherence, config/state/purpose preservation, migrations,
adapter parity, project checks, recovery/re-entry, cleanup and final-message inputs. Label pre-existing
failures, placeholders, unavailable checks and assurance limits. Source tests do not prove native
agent behavior, isolation or comprehension.

After verification, remove `.tfw/.upstream/`/temporary source only when safe and record retained
paths. Then seal one append-only `.tfw/update_receipts/UPDATE__<stamp>__<four-hex>.md` from the
template, recording source/provenance, groups, authority, effects, preservation, checks, cleanup,
next action and delivery state `planned/not-yet-observed`. Never overwrite or later rewrite it.

Finally open the briefing template and render completion/noncompletion, verified benefit,
preservation/limitation and next action from the sealed receipt. Never claim delivery/comprehension,
modify an unrelated repository/service, expose secrets, or treat prompt/echo/hash checks as proof of
filesystem/network containment.
