---
description: TFW Update — upgrade the installed framework from one immutable, applicable payload
---

# TFW Update — Framework Upgrade Workflow

> **Role:** Coordinator
> **Source:** `tfw.upstream` in `.tfw/project_config.yaml`

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: approved framework/config/adapter updates and the project-owned update receipt.
> Forbidden: project implementation, task planning/execution/review artifacts, new external effects,
> and writes before the applicable authority and source gates resolve.

## Read Contract

Root instructions are already active. Until Step 0 pins a target, this installed workflow is the
only update entry contract. After pinning, the target's `update.md` is the current behavior reader.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | `.tfw/project_config.yaml` → `tfw.upstream`, installed provenance, project-owned keys; `.tfw/VERSION`; receiver `.tfw/README.md` when present | source, installed version, configuration, and receiver purpose | installed config/version/project |
| 2 | operator-named tag or explicitly authorized immutable commit and its `.tfw/VERSION` | one immutable target | owner/Git object |
| 3 | pinned `.tfw/.upstream/.tfw/workflows/update.md` | target algorithm from Step 1 onward | pinned target |
| 4 | only intervening `.tfw/.upstream/.tfw/CHANGELOG.md` ranges and every applicable version-addressed guide named by those ranges (for example `.tfw/.upstream/.tfw/migrations/2.2.0.md`); when a major boundary is crossed, also the applicable `.tfw/.upstream/.tfw/migrations/{major}.0.0.md` guide | applicable obligations and migration | pinned target history |
| 5 | `.tfw/adapters/manifest.yaml` at adapter sync; `.tfw/templates/briefing.md` and `.tfw/templates/update_receipt.md` at their gates | copy topology and output forms | manifest/templates |

Full changelog history, live source `HEAD`, unpinned target files, full common libraries, and project
state bodies are not inputs. A missing target, target workflow, intervening range, or required major
migration is a hard stop.

## 0. Pin the Payload Before Deciding Anything

Resolve `tfw.upstream` to a local Git checkout. The operator names a tag, or explicitly authorizes an
untagged commit. Resolve that object, read `.tfw/VERSION` from that object, and require tag `v{VERSION}`
when a tag was chosen. A local source must be clean under `.tfw/`; unrelated task dirt is not payload
authority. Record target ref, full commit, version, and source path.

Materialize exactly that object with `git archive` into `.tfw/.upstream/`; never copy a live working
tree. Re-read the object before adapter sync and stop if the object moved. A local untagged Candidate
is an experiment input, not a release identity. Version equality is not source identity and never proves
that a previous update completed.

When an authorized untagged Candidate is applied, set `tfw.version` to the target's `.tfw/VERSION`
and set `tfw.installed_from` to the configured upstream plus the verified full Candidate SHA (the
actual source provenance). Record that the ref is an untagged Candidate in the receipt and outcome;
this source provenance is not a release tag, and the update must never invent or claim
`v{VERSION}`.

## 1. Read the Target and Route Applicable History

Read the pinned target's `update.md` before applying any target file. Before application, verify that
the target workflow, manifest, required templates, intervening changelog ranges, and applicable
migration paths resolve coherently from the same pinned object. If installed and target versions
match, re-observe the receiver, verify the target identity, provenance, required checks, receipt/cleanup
state, and final-message state before reporting already-current. A version field or old success receipt
alone never closes an interrupted update.

Read only changelog ranges between the installed and target versions. For every version-addressed guide
named by those intervening ranges, resolve the guide from the same pinned target, verify source coherence,
and follow its obligations before continuing. If a major boundary is crossed, also resolve and verify
the applicable `migrations/{major}.0.0.md` guide. An absent required guide, an unknown/custom installed
version, or a contradiction between the changelog and guide blocks automatic application and produces a
concrete project-specific next action.

## 2. Resolve Authority Without a Fixed Interview

Discover the acting human, configured task containers, project checks, established customizations, and
current grants from applicable project evidence. Never infer identity from Git, OS, folder, provider,
model, stale receipt, or source checkout. A local per-machine binding may select a handle only when the
binding exists outside the tree; several declared profiles with no binding require one short identity
question before the first durable write.

An ordinary configured update does not require a fixed three-question interview or one approval per
file. Ask one material question only when evidence cannot settle project meaning, a consequential choice,
or an external effect. State the project consequence, missing evidence, recommendation, and tradeoff in
ordinary language. An updater cannot select a receiving LEAD or turn a normal update into AT.
## 3. Observe, Classify, and Preview Semantic Effects

Before any target write, compare the installed payload with the pinned target and classify semantic
groups. The update request authorizes coherent framework-owned changes and explicitly prescribed
compatible migrations; it does not authorize new project decisions or external effects.

project state — never overwrite: `.tfw/knowledge_state.yaml`, `knowledge/`, `KNOWLEDGE.md`, and task
history. Follow the pinned target workflow now; a missing pin or required guide is a hard stop.
Read only intervening changelog version ranges and their applicable version-addressed guides before
applying the pinned payload.

### Receiver North-Star operation

| Receiver state | Operation |
|---|---|
| Existing root `README.md` | `PRESERVE_BYTES` |
| Current receiver `.tfw/README.md` | `CLASSIFY_BY_PURPOSE_AND_AUTHORITY` |
| Framework-owned current `.tfw/README.md` | `REPLACE_AFTER_VERIFY` |
| Customized/project-purpose/frozen-citation `.tfw/README.md` | `PRESERVE_TO_ATTACHMENT_THEN_REPLACE` |
| Absent project North Star | `LEAVE_ABSENT` |
| Starter quotation | `DO_NOT_INJECT` |

The root `README.md` remains project-owned and is never replaced by this route. For the current
`.tfw/README.md`, read the installed purpose/authority designation and applicable frozen-citation
meaning before choosing the operation. Framework-owned current values may be replaced only after the
pinned target bytes, source coherence, and purpose are verified. Customized, project-purpose-bearing,
or frozen-citation meaning must be preserved byte-identically at the content-addressed destination
before replacement; framework readers and citations then resolve that destination for historical
meaning without making it the current framework document. If approved evidence cannot resolve purpose,
stop for one material meaning question or a concrete project-specific next action.

Never overwrite `.tfw/knowledge_state.yaml`, `knowledge/`, `KNOWLEDGE.md`, task history, profiles,
grants, or configured project checks as payload. Merge `.tfw/project_config.yaml` key by key: preserve
project-owned `build.*`, scope budgets, task containers, and owner answers; update framework-owned keys;
remove only retired keys named by the target.

For a customized, unknown-origin, or explicitly project-purpose-bearing legacy `.tfw/README.md`, preserve
the exact bytes at `.tfw/update_receipts/legacy-readme/<full-sha256>/README.md` before replacement. An
identical attachment is reused; a collision with different bytes stops. The attachment is historical
evidence, not a current-state registry and not a new Project North Star.

### Decision record

For every non-mechanical decision, record: observed fact; applicable authority; whether that authority
still applies; semantic effect; permitted action; resolving evidence. Collision alone is not an owner
question when the approved preservation rule settles it. A conflict or ambiguous purpose is a material
question, not an invitation to guess.

Preview connected semantic groups, exclusions, project-owned preservation, applicable migration, planned
checks, unresolved material choices, and the exact target identity. Do not demand a per-file approval
when the update authority already settles the operation.

## 4. Apply Without State Loss

After authority and preview gates resolve, copy the approved pinned payload as connected semantic groups
while explicitly skipping and reporting project config/state, receipts, preservation attachments, and
unrelated project content. A receiver purpose file that belongs to the approved framework refresh is
handled by the North-Star classification above; it is not an unconditional skip. Merge config separately.
A copy must report the applicable exclusions by name—project config merge, knowledge/state/task history,
receipts, preservation attachments, and unrelated project content—and must report the purpose operation
when the receiver file exists; otherwise its own receipt fails.

Connected semantic groups stop together when a dependency fails. Diagnostic staging or preservation
preparation is a disclosed write; it is not target application. Destructive cleanup occurs only after
verified preservation and installed replacement. Never erase post-update project work or task history.

Re-entry always observes the present receiver before applying, repairing, refusing, or reporting. A
partial application, provenance write, past receipt, or equal version does not make final checks,
cleanup, receipt, or owner communication complete.

### Project-owned scope-budget migration

When an older receiver still carries the retired scope-budget keys, apply this prospective mapping
atomically during the approved config merge:

| Old key | New key | Treatment |
|---|---|---|
| `max_files_per_phase` | `decomposition_trigger_files` | preserve the configured number |
| `max_loc` | `decomposition_trigger_loc` | preserve the configured number |
| `max_new_files` | — | retire; do not reinterpret |
| `max_modified_files` | — | retire; do not reinterpret |
| — | `owner_escalation_multiplier` | add default `2` |

Historical TS/results retain their approval-epoch semantics; a mixed old/new block is a hard stop.

## 5. Define the Immutable Attempt Receipt

Do not seal the receipt before adapter/application checks, final verification, cleanup resolution, and
the final message outcome. Reserve one project-owned append-only record and write it at the end of Step
8, so an interrupted run can honestly record that delivery or cleanup did not complete:

`.tfw/update_receipts/UPDATE__YYYYMMDD-HHMMSS__<four-hex>.md`

Use the template `.tfw/templates/update_receipt.md`. The record contains actual run identity, immutable
source locator/full SHA, installed provenance, semantic groups and authority, applied/skipped/refused
effects, preservation references, check subjects/results, unresolved material items, cleanup outcome,
and the next action. It contains no copied secrets or hidden reasoning. If a name collides, redraw only
the opaque token; never overwrite an existing record. A receipt is history and recovery evidence, not a
current-state lock or proof that a person read the final message.

## 6. Adapter and Vocabulary Gate

For installed or owner-selected adapters:

1. Validate the manifest's four adapters, exact 11 commands, sources, targets, roles, and strategies.
2. Apply exact-byte copies or one marker-bounded managed block. Preserve unmarked roots, foreign rules,
   unrelated commands, and adjacent project text.
3. For Antigravity, new self-install targets plural `.agents`; singular `.agent/rules` remains a
   documented backward-compatible rule location. Do not infer legacy workflow discovery from rule support
   and do not delete a foreign or unowned singular file.
4. Reject missing/extra commands, wrong roles, unresolved paths, duplicate blocks, drift, or a second-run
   diff. Build an allowlist for retired terms named by intervening ranges; history may contain them, live
   instructions may not.

## 7. Verify the Receiver and Source Separately

Verify directly and report every failure:

- target ref, full SHA, version, and tag agreement;
- config/state/purpose preservation and approved config merge;
- source coherence and required workflow/template/migration paths;
- adapter parity and foreign-neighbor preservation;
- selected project checks, with pre-existing failures, missing dependencies, unavailable checks, and
  placeholder commands labeled honestly;
- receipt, cleanup, recovery/re-entry state, and the exact final message inputs;
- no removed runtime/index/PyYAML prerequisite, no retired prose-limit key, and no unexplained retired
  normative wording.

Maintainer tests are assurance, not receiver-project verification. Run configured commands only after
the target and receiver subjects are explicit. A green source suite cannot establish native agent
behavior, effective isolation, or owner comprehension.

## 8. Render the Outcome and Clean Up

Open `.tfw/templates/briefing.md` only at this gate. Lead with actual completion or noncompletion, then
relevant verified benefit, preservation/material change or limitation, next useful action, and one
optional detail reference. Translate benefits into the owner's language—what the change lets them do,
not what the procedure calls it; if an agent technique matters, keep it as supporting detail after the
owner-facing result. Keep changelog-supported benefits distinguishable from run-supported facts.
Empty changelog categories may say nothing changed; they do not suppress an observed failure or required
next step. The message never claims that a person read or understood it.

Write the receipt last, including whether the final message was delivered and whether cleanup completed.
Remove `.tfw/.upstream/` and temporary source only when safe; report any retained cleanup path. An
ordinary update may modify the current receiving repository within its resolved authority, but never
updates an unrelated repository, application production service, or external destination beyond the
requested update scope. Provider/source
authentication is a separate safety concern: use only the minimum authority needed for the selected
source and record any unavailable containment honestly.

## Safety boundary

Native provider/source authentication may be used when minimally necessary and authorized for the
resolved update/source. Production credentials, private per-user bindings/preferences, unrelated
secrets, and token material in tracked evidence or messages are forbidden. Prompt restrictions, executable
presence, echo checks, and post-run hashes alone do not prove effective filesystem/network containment.
