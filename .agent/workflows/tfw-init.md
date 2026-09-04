---
description: TFW Init — initialize TFW or attach/repair one adapter
---

# TFW Init — Project Initialization

> **Role:** Coordinator
> **Output:** configured TFW project and first task, or one repaired adapter

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: TFW setup/config/adapters and the init task's RES/RF. Forbidden: HL, TS, and unrelated
> code.

## Read Contract

Root instructions are already active. Read this workflow completely, then select inputs in order.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | filesystem presence of `.tfw/`, `.tfw/project_config.yaml` → `tfw.task_containers`, and task `status.md`/`journal/` when configured | choose full init versus attach/repair before broad discovery | filesystem/config/task-local |
| 2 | `.tfw/adapters/manifest.yaml` and only the selected adapter sources/targets on attach/repair | exact repair mapping and preservation | tooling metadata/receiver |
| 3 | root README, `<existing receiver North-Star existence and bytes>`, project docs, structure, build config, and people/process material only after full init is selected | progressive discovery and byte-preservation without loading starter purpose | project sources/receiver |
| 4 | `.tfw/templates/project_config.yaml`, `.tfw/templates/knowledge_state.yaml`, `.tfw/templates/team/profile.md`, `.tfw/templates/status.md`, and `.tfw/templates/journal/event.md`, each only before its write | setup forms and pre-write bounds | templates |
| 5 | `.tfw/conventions.md` heading `Identifier` before first-task creation | identifier composition and collision refusal | shared rule |
| 6 | selected research workflow/templates, `.tfw/templates/KNOWLEDGE.md`, and `.tfw/templates/RF.md` only at their phase gates | research, knowledge, and result forms | workflows/templates |

Full common libraries, unselected adapters, and broad project discovery before routing are not
inputs. Missing/duplicate addresses, unresolved manifest rows, or ambiguous adapter selection are
hard stops.

## 0. Route Before Discovery

- **Full init:** `.tfw/` is newly supplied and no configured container holds TFW traces. Continue.
- **Attach/repair:** configured state and traces exist. Preserve all state and skip interview,
  discovery, research, config creation, and init-task creation. Select the adapter explicitly when
  it cannot be inferred; apply its persistent row and all 11 command rows. Verify bytes/blocks,
  roles, paths, idempotence, literal routing, and preservation, report, then stop.

Never reset an existing project or guess its adapter.

## 1. Discover and Interview

Ask whether tutorial explanations are wanted. For full init only, inspect purpose, docs, structure,
process, people, conventions, build/tests, and dependencies; present findings for correction.

Ask at most three questions per message until these are approved: task prefix; completion checks;
AI adapter(s); content language; greenfield/brownfield constraints; first task's full title and its
uppercase alphanumeric acronym. Never invent the acronym apart from an approved title.

## 2. Mini-Setup

Resolve the acting human before writing. Then:

1. Create project config and clean knowledge state from their templates; fill discovered/approved
   project keys. New configuration uses only `decomposition_trigger_files: 50`,
   `decomposition_trigger_loc: 5000`, and `owner_escalation_multiplier: 2` under
   `tfw.scope_budgets`. Add no identifier counter.
2. Create `team/` with one approved human profile; never create it empty or create an agent-session
   profile.
3. Create `tfw.task_containers[0]` and the root README route to its derived `00-INDEX.md`.
   Preserve every existing root or `.tfw/README.md` North Star byte-for-byte. If a project North Star is
   absent, create project-specific approved wording from discovery; never copy or inject the starter
   repository's local Saint-Exupéry quotation.
4. Read the clock once and create `{container}/{YYYY}/{PREFIX}_{stamp}_{ABBR}`. If that exact path
   exists, stop for a different owner-approved abbreviation; do not retry the time or add a suffix.
5. From the status/event templates create lifecycle `RES` state and one `created` event whose
   timestamped name uses a drawn four-hex token, human `on_behalf_of`, tool `via`, and valid refs.
6. Run `python .tfw/scripts/gen_index.py --check project`; it writes nothing.

## 3. Research Gate

Announce and run `/tfw-research` inside the init task. Preserve its formal stages and RES artifact;
focus on architecture, decisions, dependencies, domain terms, debt, and conventions. Wait wherever
the research workflow waits. Use the completed findings in setup.

## 4. Full Setup

1. Merge the managed TFW block into root `AGENTS.md`; never overwrite project-owned text.
2. Create `KNOWLEDGE.md` from its template and approved research findings.
3. For every owner-selected adapter, expand the manifest's persistent row and exact 11 command
   records. `{workflow}` is each command's canonical source and `{command}` its key. Preserve
   unrelated and unmarked receiver content; reject missing/extra routes, wrong role, unresolved
   source/target, duplicate block, drift, or second-run diff.
4. Offer `.user_preferences.md`, add it to `.gitignore` when accepted, and never commit it.
5. Finalize project config and set the init task lifecycle to `RF` with the required event.

## 5. Verify, RF, and Close

Verify core/config/root files, configured container and task state, RES, knowledge choice, selected
adapter roots, exact 11 routes/roles/bytes, idempotence, literal `/tfw-*`, VERSION/config agreement,
project check, and every configured build command.

Write RF from its template with findings, decisions, files, and observed verification. After its
review/knowledge gates complete, close the init task with lifecycle `DONE`, a bounded `outcome`, and
a valid transition event; regenerate the portfolio index only as a separate deliberate act. Stop
with `/tfw-plan` as the next normal command.

## Anti-patterns

- full init over configured state;
- guessed interview values, adapter, identity, time, or acronym;
- project-state reset or root-file overwrite;
- file-existence-only adapter verification;
- RF/DONE without research, review, evidence, and required closure effects.
