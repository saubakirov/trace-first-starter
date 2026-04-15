# Tech Debt Registry

| # | Source | Severity | File(s) | Description | Status |
|---|--------|----------|---------|-------------|--------|
| TD-33 | TFW-14 RES obs. | Low | `.tfw/workflows/handoff.md`, adapters | `tfw-handoff` misnaming — no handoff status/document exists. Consider renaming to `tfw-execute`. Low priority, high blast radius | ✅ Closed (cost/benefit: no agent confusion, high blast radius, low value) |
| TD-45 | TFW-18 RF obs. #1 | Low | `.tfw/conventions.md` | §10.1 and §10.2 subsection numbering breaks the flat numbering scheme (§1-§15). Future renumbering pass needed | ⬜ Backlog |
| TD-59 | TFW-23 REVIEW FC#1 | High | `.tfw/workflows/` | No crash-recovery gate mechanism — after session crash, WAIT gates are lost. Need "Gate Recovery" protocol | ✅ Closed (file-based state machine pattern in research D31 + review D41 covers critical paths) |
| TD-63 | TFW-25 RF obs. #1 | Med | `KNOWLEDGE.md` L39-75 | §1 Architecture Decisions table (D1-D46) = 46 rows with long rationale text. Main driver of KNOWLEDGE.md exceeding 120-line target. Consider compression or active/archived split | ⬜ Backlog |
| TD-73 | TFW-26/B RF obs. #6 | Med | `docs/requirements.txt` | MkDocs 2.0 will break mkdocs-gen-files plugin. Pin or monitor | ⬜ Monitor |
| TD-79 | TFW-27/B RF obs. #1 | Med | `docs/scripts/gen_docs.py` | gen_docs.py at 692 LOC — exceeds 600 LOC threshold. `resolve_references()` (200+ LOC) extraction candidate → `resolvers.py` | ⬜ Backlog |
| TD-80 | TFW-27/B RF obs. #2 | Med | `docs/scripts/gen_docs.py` | Artifact resolver doesn't search PhaseX subfolders for `RF TFW-26`. Many "Unresolved reference" info messages. Needs thorough fix | ⬜ Backlog (important) |
| TD-81 | TFW-27/B RF obs. #3 | Med | `docs/scripts/gen_docs.py`, `README.md` | `_generate_tasks_index()` Task Board parser is fragile — regex-based parsing of README.md tables | ⬜ Backlog |
| TD-82 | TFW-27/B REVIEW | Low | `docs/mkdocs.yml` | `attr_list` and `md_in_html` extensions added for README logo — may be removable if README format changes | ⬜ Backlog |
| TD-88 | TFW-32/A REVIEW obs. #1 | Low | `KNOWLEDGE.md` L37 | §1 Architecture Map says "Updated via `tfw-docs` workflow" — correct, but "optional" annotation could be clarified after docs/knowledge separation | ⬜ Backlog |
| TD-90 | TFW-32/C RF obs. #2 | Low | `.tfw/workflows/plan.md` | plan.md grew from 108 to ~150 lines after TFW-32/C + TFW-38/B. Still within workflow word limit but approaching threshold. Monitor growth | ⬜ Monitor |
| TD-91 | TFW-32/D RF obs. #1 | Low | `README.md` L31-36 | "Who This Is For" bullets lack inline links to specific TFW features — reader can't explore further | ⬜ Backlog |
| TD-99 | TFW-38 Phase B redesign | Med | `KNOWLEDGE.md`, templates, workflows, glossary, conventions | KNOWLEDGE.md naming: "knowledge" = ambiguous (file vs concept vs folder). Consider renaming root file to DOCS.md or PROJECT_INDEX.md to distinguish from `knowledge/` folder. High blast radius (20+ references). Requires dedicated task | ⬜ Backlog |
| TD-102 | TFW-40/A RF obs. #1 | Low | `.tfw/workflows/init.md` | Phase 2 step 1 (create config from template) and Phase 4 step 6 ("Update PROJECT_CONFIG.yaml — finalize all values") overlap after Phase A changes. Phase 4 step 6 should be clarified to "update framework-section values if needed" | ⬜ Backlog |
| TD-103 | TFW-40/B RF obs. #3 | Low | `.tfw/project_config.yaml` | Live config file has different comment formatting than template (shorter comment). Pre-existing discrepancy, not introduced by Phase B rename | ⬜ Backlog |
| TD-104 | TFW-40 HL §11 S4 | Med | TFW-16 (backlog) | tfw-doctor (TFW-16) = self-diagnosis of TFW meta-state. User use case: «помочь перепроверять самого себя и починить мета информацию». Concrete trigger: verify knowledge_state.yaml values match project reality after tfw-update | ⬜ Backlog (linked to TFW-16) |

> Added by REVIEW files during task lifecycle. See `.tfw/workflows/docs.md`.
> Closed items purged 2026-04-15 (41 items removed: TD-12..TD-101 with ✅ status).
