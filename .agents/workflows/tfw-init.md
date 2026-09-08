---
description: TFW Init — initialize TFW or attach/repair one adapter
---

# TFW Init — Project Initialization

> **Role:** Coordinator
> **Output:** configured TFW project and first task, or one repaired adapter

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: TFW setup/config/adapters and the init task's RES/RF. Forbidden: HL, TS, unrelated
> code, project-purpose replacement, and state reset.

## Read Contract

Read this workflow completely, then select inputs in order. Full common libraries and unselected
adapters are not inputs.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | `.tfw/`; `.tfw/project_config.yaml` → `tfw.task_containers`; task `status.md`/`journal/` | route full-init or attach/repair | filesystem/config/task-local |
| 2 | `.tfw/adapters/manifest.yaml` and selected adapter sources/targets | exact repair mapping and preservation | manifest/receiver |
| 3 | full-init only: root README, receiver `.tfw/README.md`, project docs/structure/build/people/process | discovery and purpose preservation | project/receiver |
| 4 | templates for config, knowledge state, profile, status, journal | output forms | templates |
| 5 | `.tfw/conventions.md` → `Identifier`, `Session identity` | identity and naming | shared rule |
| 6 | selected research/knowledge/RF forms at their gates | init research and result | workflows/templates |

Missing or duplicate task containers, unresolved manifest rows, ambiguous adapter selection, or a
purpose collision that evidence cannot settle are hard stops.

## 0. Route Before Discovery

**Detect Full Init vs Adapter Attach/Repair** before reading broad project context.

- **Full init:** `.tfw/` is newly supplied and no configured container holds TFW traces. Continue.
- **Attach/repair:** configured state and traces exist. Preserve all state; skip discovery, research,
  config creation, and init-task creation. Select the adapter explicitly when it cannot be inferred,
  apply its persistent row and all 11 command rows, verify bytes/blocks, roles, paths, idempotence, and
  foreign neighbors, then stop.

Never reset an existing project or guess its adapter. An existing root or `.tfw/README.md` is not a
blank starter surface.

## 1. Discover and Interview

**Interview + Mini-Setup** applies only to full init; attach/repair has no second interview.

For full init, inspect purpose, docs, structure, process, people, conventions, build/tests, dependencies,
release procedure when present, and project language. Ask whether tutorial explanations are wanted. Ask
at most three questions per message until the owner approves task prefix, completion checks, adapter(s),
content language, greenfield/brownfield constraints, and the first task title/acronym. Never invent an
acronym apart from an approved title.

## 2. Mini-Setup

Resolve the acting human before writing. Preserve existing project-owned purpose and state:

### Receiver North-Star operation

| Receiver state | Operation |
|---|---|
| Existing root `README.md` | `PRESERVE_BYTES` |
| Current receiver `.tfw/README.md` | `CLASSIFY_BY_PURPOSE_AND_AUTHORITY` |
| Framework-owned current `.tfw/README.md` | `REPLACE_AFTER_VERIFY` |
| Customized/project-purpose/frozen-citation `.tfw/README.md` | `PRESERVE_TO_ATTACHMENT_THEN_REPLACE` |
| Absent project North Star | `CREATE_FROM_DISCOVERY` |
| Starter quotation | `DO_NOT_INJECT` |

The root `README.md` remains project-owned. For an existing `.tfw/README.md`, resolve the installed
purpose/authority designation before deciding whether current framework values may replace it. Preserve
customized, project-purpose-bearing, or frozen-citation bytes at the content-addressed destination
`.tfw/update_receipts/legacy-readme/<full-sha256>/README.md` before replacement; the receipt records
the observed designation and current readers use that exact path for historical meaning. An unresolved
purpose stops for one material question or a concrete next action rather than silently preserving or
replacing.

1. Create project config and clean knowledge state from templates. New config uses only
   `decomposition_trigger_files: 50`, `decomposition_trigger_loc: 5000`, and
   `owner_escalation_multiplier: 2` under `tfw.scope_budgets`.
2. Create `team/` with one approved human profile; never create an agent-session profile.
3. Create the first configured task container and a direct root README route to method, knowledge,
   releases, and one selected trace. Create no catalogue/cache/status page.
4. Read the clock once and create `{container}/{YYYY}/{PREFIX}_{stamp}_{ABBR}`. Collision stops for a
   different owner-approved abbreviation; do not retry time or add a suffix.

### Project-owned release procedure

If the project has `RELEASE.md`, preserve it and read its established contract. If it has no release
procedure, leave it absent; ordinary initialization does not create a starter release policy. A later
explicit release request receives a bounded planning route for the missing decision.

### Session identity checkpoint

Full-init: after-item4/before-item5. Apply `WORK=INIT` and the created task identifier.
Attach/repair: skip this checkpoint. Navigation is not authority and no identity is inferred from OS, Git,
provider, model, or folder.

5. From the status/event templates, create lifecycle `RES` state and one `created` event using a drawn
   opaque token, human `on_behalf_of`, tool `via`, and valid refs.
6. Verify semantic YAML, task state/event contracts, absent retired runtime/prose keys, no receiver
   Python/PyYAML prerequisite, and project-owned files unchanged.

## 3. Research Gate

Announce and run `/tfw-research` inside the init task. Preserve its stages and RES. Focus on architecture,
decisions, dependencies, domain terms, debt, conventions, and the project's own release procedure when
one exists. Wait wherever the research workflow waits.

## 4. Full Setup

1. Merge the managed TFW block into root `AGENTS.md`; never overwrite project-owned text.
2. Create `KNOWLEDGE.md` from its template and approved research findings.
3. Install selected adapters from the manifest's persistent row and exact 11 command records. Preserve
   unrelated/unmarked content; reject missing/extra routes, duplicate blocks, drift, or second-run diff.
4. Offer `.user_preferences.md`, add it to `.gitignore` when accepted, and never commit it.
5. Finalize project config and set the init task lifecycle to `RF` with the required event.
   The repair route reports, then stop; full init continues to research and closure. For the route
   contract, report, then stop after repair.

## 5. Verify, RF, and Close

Verify core/config/root files, state, RES, knowledge choice, selected adapter roots, exact routes/roles/
bytes, idempotence, literal `/tfw-*` routes, VERSION/config agreement, direct setup postconditions, and
configured build commands. Write RF from its template with findings, decisions, files, and observed
verification. After review/knowledge gates, close with `DONE` and a filled outcome; stop with `/tfw-plan`.

## Anti-patterns

- full init over configured state;
- guessed interview values, adapter, identity, time, or acronym;
- project-state reset, purpose overwrite, or root-file replacement;
- file-existence-only adapter verification;
- RF/DONE without research, review, evidence, and required closure effects.
