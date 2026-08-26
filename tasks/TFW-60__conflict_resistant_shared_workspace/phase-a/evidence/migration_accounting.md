# Migration accounting — TFW-60 / Phase A


Produced by `python docs/scripts/migrate_board.py --manifest`. Every board row and
every task directory is accounted for exactly once. Re-runnable: the numbers below
are recomputed from the tree, not transcribed.

## Reconciliation

```
    0 board data rows
   53 task directories
  ----------------------------------------
   53 source occurrences  ->   53 logical identities

        0  matched       row and directory both exist
        0  board-only    a row with no directory
       53  directory-only  a directory with no row
```

Rows in a shape no strict `| [ID](path)` parser matches: **0**. They are reported, not repaired.

## Board-only rows

None.

## Directory-only entries

| ID | Path |
|---|---|
| `TFW-1` | `tasks/TFW-1__formalize_success_criteria` |
| `TFW-2` | `tasks/TFW-2__upgrade_to_v3` |
| `TFW-3` | `tasks/TFW-3__readme_public_readiness` |
| `TFW-4` | `tasks/TFW-4__framework_cleanup` |
| `TFW-5` | `tasks/TFW-5__knowledge_and_tfw_docs` |
| `TFW-6` | `tasks/TFW-6__versioning_and_update` |
| `TFW-7` | `tasks/TFW-7__resolve_tech_debt` |
| `TFW-8` | `tasks/TFW-8__reviewer_role_and_workflow` |
| `TFW-9` | `tasks/TFW-9__update_source_mechanism` |
| `TFW-10` | `tasks/TFW-10__version_string_sweep` |
| `TFW-11` | `tasks/TFW-11__research_stage` |
| `TFW-12` | `tasks/TFW-12__scope_budget_centralization` |
| `TFW-13` | `tasks/TFW-13__tfw_init_workflow` |
| `TFW-14` | `tasks/TFW-14__research_interaction_model` |
| `TFW-15` | `tasks/TFW-15__pipeline_status_rename` |
| `TFW-17` | `tasks/TFW-17__research_depth_and_coordinator_quality` |
| `TFW-18` | `tasks/TFW-18__knowledge_consolidation` |
| `TFW-19` | `tasks/TFW-19__config_propagation` |
| `TFW-21` | `tasks/TFW-21__research_workflow_compression` |
| `TFW-22` | `tasks/TFW-22__coordinator_research_enrichment` |
| `TFW-23` | `tasks/TFW-23__templates_english_standardization` |
| `TFW-24` | `tasks/TFW-24__res_state_machine` |
| `TFW-25` | `tasks/TFW-25__values_consolidation` |
| `TFW-26` | `tasks/TFW-26__documentation_site` |
| `TFW-27` | `tasks/TFW-27__wiki_polish_and_brand` |
| `TFW-29` | `tasks/TFW-29__consistency_audit` |
| `TFW-30` | `tasks/TFW-30__antigravity_adapter_audit` |
| `TFW-31` | `tasks/TFW-31__quick_start_agent_first` |
| `TFW-32` | `tasks/TFW-32__methodology_and_positioning` |
| `TFW-36` | `tasks/TFW-36__content_marketing_blog_series` |
| `TFW-38` | `tasks/TFW-38__quality_enforcement` |
| `TFW-40` | `tasks/TFW-40__state_separation` |
| `TFW-41` | `tasks/TFW-41__execution_quality_gates` |
| `TFW-42` | `tasks/TFW-42__research_cycle_restructure` |
| `TFW-43` | `tasks/TFW-43__research_stage_protocol` |
| `TFW-44` | `tasks/TFW-44__coordinator_quality_gates` |
| `TFW-45` | `tasks/TFW-45__multi_agent_workflows` |
| `TFW-46` | `tasks/TFW-46__evidence_layer` |
| `TFW-47` | `tasks/TFW-47__codex_adapter_shortcut_skills` |
| `TFW-48` | `tasks/TFW-48__value_first_methodology_rebaseline` |
| `TFW-49` | `tasks/TFW-49__agent_commit_identity_and_attribution` |
| `TFW-50` | `tasks/TFW-50__minimal_agent_commit_attribution` |
| `TFW-51` | `tasks/TFW-51__tfw_light_ru` |
| `TFW-52` | `tasks/TFW-52__tfw_light_v1` |
| `TFW-53` | `tasks/TFW-53__hl_contract_and_goal_defence` |
| `TFW-54` | `tasks/TFW-54__agent_team_mode` |
| `TFW-55` | `tasks/TFW-55__canonization_program` |
| `TFW-56` | `tasks/TFW-56__review_mode_removal` |
| `TFW-57` | `tasks/TFW-57__artifact_growth_control` |
| `TFW-58` | `tasks/TFW-58__revise_protocol` |
| `TFW-59` | `tasks/TFW-59__north_star_lifecycle` |
| `TFW-60` | `tasks/TFW-60__conflict_resistant_shared_workspace` |
| `TFW-61` | `tasks/TFW-61__collaboration_transport_modes` |

## Malformed rows

None.

## Task state written

None.

## Guarantees checked

| Guarantee | How |
|---|---|
| Zero renames, zero moves | the script has no rename or move call |
| Zero byte changes to existing artifacts | only paths that do not yet exist are opened for writing; an existing target aborts the run |
| No fact invented | absent facts are written as `unrecorded`; a lifecycle outside the vocabulary becomes `UNDECLARED` plus the verbatim value |
| Every row and directory accounted once | the reconciliation above sums to the source occurrence count |

---

*Migration accounting — TFW-60 / Phase A*
