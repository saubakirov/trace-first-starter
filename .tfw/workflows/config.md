---
description: TFW Config — interactive config change, propagate to all inline values
---

# TFW Config — Config Sync Workflow

> **Role:** Coordinator
> **Output:** Updated project_config.yaml + all inline value locations + synced adapters
> **Trigger:** Manual (`/tfw-config`) when config values need changing or auditing

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: reading/writing project_config.yaml, workflow files, convention files, adapter copies.
> Forbidden: writing code, modifying HL/TS/ONB/RF/REVIEW files.

## Modes

### Edit Mode (default)

1. **Ask**: "What would you like to change in the configuration?"
2. **User answers** with config key and desired value (e.g., "scope budget max_files до 10")
3. **Read** `.tfw/project_config.yaml` — get current value
4. **Read** Config Sync Registry (below) — find all inline locations
5. **Propose batch update** — list every file + line that will change:
   ```
   Proposed changes (config key: tfw.scope_budgets.max_files_per_phase, 14 → 10):
   - project_config.yaml: 14 → 10
   - .tfw/workflows/plan.md §Scope Budget per Phase: 14 → 10
   - .tfw/conventions.md §6 Scope Budgets: 14 → 10
   "Apply? ({N} files)"
   ```
6. **User approves** → update all files
7. **Sync adapters** — copy modified workflows to adapter folders (see §Adapter Sync)

### Verify Mode

Invoked with: `/tfw-config verify`

1. **Read** `.tfw/project_config.yaml` — all config values
2. **Read** every target in Config Sync Registry — extract current inline values
3. **Compare** — report mismatches or confirm "All values in sync"
4. **Output format**:
   ```
   Config Sync Report:
   ✅ scope_budgets.max_files_per_phase: 14 (config) = 14 (plan.md) = 14 (conventions.md)
   ❌ scope_budgets.max_loc: 1200 (config) ≠ 1000 (plan.md)
   ...
   ```

## Config Sync Registry

> Maps `project_config.yaml` keys to their inline display locations.
> Agent reads this table to find where values appear, compares with YAML, and proposes updates.

### scope_budgets

| Config Key | Target File | Section Header | Row Label |
|------------|------------|----------------|-----------|
| `scope_budgets.max_files_per_phase` | `.tfw/workflows/plan.md` | Scope Budget per Phase | Files per phase |
| `scope_budgets.max_files_per_phase` | `.tfw/conventions.md` | 6) Scope Budgets | Files per phase |
| `scope_budgets.max_new_files` | `.tfw/workflows/plan.md` | Scope Budget per Phase | New files per phase |
| `scope_budgets.max_new_files` | `.tfw/conventions.md` | 6) Scope Budgets | New files per phase |
| `scope_budgets.max_loc` | `.tfw/workflows/plan.md` | Scope Budget per Phase | LOC per phase |
| `scope_budgets.max_loc` | `.tfw/conventions.md` | 6) Scope Budgets | LOC per phase |
| `scope_budgets.max_modified_files` | `.tfw/workflows/plan.md` | Scope Budget per Phase | Modified files |
| `scope_budgets.max_modified_files` | `.tfw/conventions.md` | 6) Scope Budgets | Modified files |

### research

| Config Key | Target File | Section Header | Row Label |
|------------|------------|----------------|-----------|
| `research.max_web_queries_per_stage` | `.tfw/workflows/research/base.md` | Limits | Web queries per stage |
| `research.max_files_per_stage` | `.tfw/workflows/research/base.md` | Limits | Project files read per stage |
| `research.max_questions_per_turn` | `.tfw/workflows/research/base.md` | Limits | Questions to user per turn |
| `research.max_passes` | `.tfw/workflows/research/base.md` | Limits | Max passes |
| `research.default_mode` | `.tfw/workflows/research/base.md` | Step 2: Select Mode | (read in step) |
| `research.modes.focused.loops_per_stage` | `.tfw/workflows/research/focused.md` | Stage Behavior | OODA loops per stage |
| `research.modes.deep.loops_per_stage` | `.tfw/workflows/research/deep.md` | Stage Behavior | OODA loops per stage |

### knowledge

| Config Key | Target File | Section Header | Row Label |
|------------|------------|----------------|-----------|
| `knowledge.interval` | `.tfw/workflows/knowledge.md` | Limits | Consolidation interval |
| `knowledge.gate_mode` | `.tfw/workflows/knowledge.md` | Limits | Gate mode |
| `knowledge.max_facts_per_topic` | `.tfw/workflows/knowledge.md` | Limits | Max facts per topic |
| `knowledge.max_topic_files` | `.tfw/workflows/knowledge.md` | Limits | Max topic files |

### review

| Config Key | Target File | Section Header | Row Label |
|------------|------------|----------------|-----------|
| `review.min_verify_ratio` | `.tfw/workflows/review.md` | Step 2: Verify | Min verify ratio |

### content_language

| Config Key | Target File | Section Header | Row Label |
|------------|------------|----------------|-----------|
| `content_language` | `.tfw/conventions.md` | 11) Quality Standard | Content Language |

## Adapter Sync

Read `.tfw/adapters/manifest.yaml` and select only installed adapters. Expand its exact 11
command rows; `{workflow}` comes from the command record and `{command}` from its key. Sync
only a target whose canonical workflow, command route, role, or config-bearing source changed
in this session.

For `copy`, require exact source bytes. For `managed_block`, compare and replace only the
declared marker-bounded region; an existing unmarked file is reported and left unchanged.
Reject missing/extra commands, `/tfw-research` not owned by Researcher, unresolved paths,
duplicate blocks, drift, and any second-run diff. Preserve unrelated commands, rules, and
project text. The manifest is copy/check metadata, not a runtime authority.

## Anti-patterns

- Modifying inline values without updating project_config.yaml (source of truth)
- Modifying project_config.yaml without updating inline locations
- Skipping adapter sync after workflow modification
- Syncing only a subset of installed adapters selected by the manifest
- Reporting an adapter sync as done without running the drift check
- Adding new inline value locations without updating the Config Sync Registry
