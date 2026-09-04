---
description: TFW Config — verify or change config and every registered inline copy
---

# TFW Config — Config Sync Workflow

> **Role:** Coordinator
> **Output:** verified or approved config/range updates and affected adapter copies

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: `project_config.yaml`, registered workflow/convention ranges, and affected adapter
> copies. Forbidden: code and task artifacts.

## Read Contract

Root instructions are already active. Read this workflow completely, then read in order.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | `.tfw/project_config.yaml` | current source values | project config |
| 2 | this workflow's `Config Sync Registry` | the one set of inline targets | canonical workflow |
| 3 | only each registered target file and unique `Section Header` range | compare or update inline copies | registered source range |
| 4 | `.tfw/adapters/manifest.yaml` only when a changed range has adapter copies | affected copy/check destinations | tooling metadata |

Full conventions/glossary/workflows, unregistered ranges, task artifacts, and unrelated adapters are
not inputs. A missing or duplicate heading/row/target, unresolved source, or incomplete adapter map
is a hard stop.

## Edit Mode

1. Ask what config key and value should change.
2. Resolve its config value and every registry row. Values with no inline copy remain config-only.
3. Present one batch preview with old/new values and exact files/headings.
4. Wait for approval, then update config and every resolved row atomically.
5. Sync only affected installed adapters through `Adapter Sync`; verify and report all results.

## Verify Mode

For `/tfw-config verify`, resolve all config values and every registry target, then report each exact
match/mismatch. Write nothing. A mismatch is reported, never silently repaired.

## Config Sync Registry

### scope_budgets

| Config Key | Target File | Section Header | Row Label |
|---|---|---|---|
| `scope_budgets.max_files_per_phase` | `.tfw/conventions.md` | Scope Budgets (per Phase) | Files per phase |
| `scope_budgets.max_new_files` | `.tfw/conventions.md` | Scope Budgets (per Phase) | New files per phase |
| `scope_budgets.max_loc` | `.tfw/conventions.md` | Scope Budgets (per Phase) | LOC per phase |
| `scope_budgets.max_modified_files` | `.tfw/conventions.md` | Scope Budgets (per Phase) | Modified files |

### research

| Config Key | Target File | Section Header | Row Label |
|---|---|---|---|
| `research.max_web_queries_per_stage` | `.tfw/workflows/research/base.md` | Limits | Web queries per stage |
| `research.max_files_per_stage` | `.tfw/workflows/research/base.md` | Limits | Project files read per stage |
| `research.max_questions_per_turn` | `.tfw/workflows/research/base.md` | Limits | Questions to user per turn |
| `research.max_passes` | `.tfw/workflows/research/base.md` | Limits | Max passes |
| `research.modes.focused.loops_per_stage` | `.tfw/workflows/research/focused.md` | Stage Behavior | OODA loops per stage |
| `research.modes.deep.loops_per_stage` | `.tfw/workflows/research/deep.md` | Stage Behavior | OODA loops per stage |

`research.default_mode` has no inline copy; the research workflow reads it directly from config.

### knowledge

No inline copies. Knowledge workflows read `tfw.knowledge` directly from project config.

### review

| Config Key | Target File | Section Header | Row Label |
|---|---|---|---|
| `review.min_verify_ratio` | `.tfw/workflows/review.md` | Step 2: Verify | Min verify ratio |

### content_language

| Config Key | Target File | Section Header | Row Label |
|---|---|---|---|
| `content_language` | `.tfw/conventions.md` | Quality Standard (no compromises) | Content Language |

## Adapter Sync

Expand the manifest's exact command records and select only installed adapters affected by this
change. For `copy`, require source-byte equality. For `managed_block`, replace only the single
declared marker range; report and preserve an unmarked file. Reject missing/extra commands, wrong
roles, unresolved targets, duplicate blocks, drift, or a second-run diff. Preserve unrelated text.
The manifest is copy/check metadata, never runtime authority.

## Anti-patterns

- changing config or an inline copy alone;
- reading or editing an unregistered range;
- applying Edit Mode without approval;
- claiming adapter sync without exact verification.
