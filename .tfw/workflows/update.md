---
description: TFW Update — upgrade the installed framework from a pinned upstream payload
---

# TFW Update — Framework Upgrade Workflow

> **Role:** Coordinator
> **Source:** `tfw.upstream` in `.tfw/project_config.yaml`

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: approved framework/config/adapter updates. Forbidden: project implementation,
> task planning/execution/review artifacts, and writes before the owner gate.

## Read Contract

Root instructions are already active. Until Step 0 pins a target, this installed workflow is the
only update algorithm. After pinning, read the target's workflow and follow it from Step 1.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | `.tfw/project_config.yaml` → `tfw.upstream`, `tfw.version`, `tfw.installed_from`, project-owned keys; `.tfw/VERSION` | source, installed version/provenance, and state to preserve | installed config/version |
| 2 | operator-named tag or explicitly authorized commit and its `.tfw/VERSION` | pin one immutable payload | owner/Git object |
| 3 | pinned `.tfw/.upstream/.tfw/workflows/update.md` | target algorithm from Step 1 onward | pinned target |
| 4 | only intervening `.tfw/.upstream/.tfw/CHANGELOG.md` version ranges and the crossed major `.tfw/.upstream/.tfw/migrations/{major}.md` | required deltas and migration | pinned target history |
| 5 | `.tfw/adapters/manifest.yaml` at adapter sync; `.tfw/templates/briefing.md` at briefing | copy/check topology and output form | tooling metadata/template |

Full changelog history, live source `HEAD`, unpinned target files, full common libraries, and project
state bodies are not inputs. A missing pin, target workflow, intervening range, or major migration is
a hard stop.

## 0. Pin the Payload

Resolve `tfw.upstream` to a local Git checkout. The operator names a tag, or explicitly authorizes
an untagged commit. Resolve that object, read VERSION from it, and require tag `v{VERSION}` when a
tag was chosen. A local source must be clean under `.tfw/`; dirty unrelated task files do not
matter. Record target ref, commit, version, and source path.

Materialize exactly that object with `git archive` into `.tfw/.upstream/`; never copy a live working
tree. Re-read the object before adapter sync and stop if it moved. In CL mode present commands rather
than claiming they ran.

## 1. Compare and Route

Follow the pinned target workflow now. If installed and target versions match, stop. Otherwise read
only intervening changelog version ranges. If a major boundary is crossed, run its pinned migration
before continuing; absence blocks the update.

## 2. Owner Gate

Before the first project write ask exactly three questions in one message; read-only work may
continue while awaiting answers:

1. Who is acting (`team/{handle}.md` and event `on_behalf_of`), never inferred?
2. What is `tfw.task_containers` for future creation/resolution?
3. What are the current `build.*` verification commands?

Record the answers. Create `team/` and one human profile only if absent and approved; several
profiles require a per-machine binding.

## 3. Classify and Preview

Compare each local framework file with the installed provenance baseline and pinned target:

- project state — never overwrite: `.tfw/knowledge_state.yaml`, `knowledge/`, `KNOWLEDGE.md`, and
  any project debt record;
- release-identical/provenance drift — replace from target;
- customization — merge the measured local delta into target;
- removed/structurally changed — follow only the intervening changelog/migration.

Merge `.tfw/project_config.yaml` key by key: preserve project-owned `build.*`, scope budgets, task
containers, and owner answers; update framework-owned keys; remove retired keys named by the target.
Produce one checkbox per file, including every Changed/Removed and template-structure item. Wait for
approval of the exact checklist.

## 4. Apply Without State Loss

Copy the approved pinned payload while explicitly skipping and reporting project config/state;
merge config separately. A copy that does not report both skips where both files exist fails. After
each item verify the customization that must survive, then tick it.

## 5. Adapter and Vocabulary Gate

For installed or owner-selected adapters only:

1. Validate the manifest's four adapters, exact 11 commands, sources, targets, roles, and strategies.
2. Apply exact-byte copies or one marker-bounded managed block. Preserve unmarked roots, unrelated
   commands/rules, and adjacent project text.
3. Reject missing/extra commands, wrong roles, unresolved paths, duplicate blocks, drift, or a
   second-run diff.
4. Build an allowlist for every retired term named by the intervening ranges; retirement/history
   text may contain it, live instructions may not. Require zero unexplained hits in payload and
   installed adapters.

## 6. Provenance, Verify, Brief, Clean

Set `tfw.version` and `tfw.installed_from` to `{upstream}@{verified-tag}`; never persist a
machine-local path. Run `python .tfw/scripts/gen_index.py --check project`, adapter parity,
retired-vocabulary, literal `/tfw-*`, customization, and every configured build command.

At the final message, render `.tfw/templates/briefing.md` in `content_language` from only the
intervening Added/Changed/Fixed/Removed bullets; an absent category means nothing in this release.
Record delivery in the checklist. Then remove `.tfw/.upstream/` and optional temporary source only
when safe. Report any retained cleanup path; never hide it.
