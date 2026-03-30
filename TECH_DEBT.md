# Tech Debt Registry

| # | Source | Severity | File(s) | Description | Status |
|---|--------|----------|---------|-------------|--------|
| TD-1 | TFW-3 RF obs. | Low | README.md, .tfw/README.md | "Who This Is For" in both — acceptable overlap but monitor for divergence | Accepted |
| TD-2 | TFW-4 HL | Med | `.tfw/` | Content duplication across conventions/README/glossary — cross-refs added | Accepted — cross-refs added (TFW-7) |
| TD-3 | TFW-4 HL | Low | `.tfw/conventions.md` | ONB overhead for small single-phase tasks — ONB always required | Accepted — ONB always required (TFW-7) |
| TD-4 | TFW-5 RF obs. | Low | `.tfw/README.md` | Workflows section lists only plan/handoff/resume — should mention docs | ✅ Resolved (TFW-7) |
| TD-5 | TFW-6/A RF obs. | Low | `README.md` | Empty line splitting Root Files table rows | ✅ Resolved (TFW-6/C) |
| TD-6 | TFW-6/A RF obs. | Med | `.tfw/PROJECT_CONFIG.yaml` | Build commands are placeholder `echo` — meta-project has no build | Accepted |
| TD-7 | TFW-6/B RF obs. | Low | `.agent/workflows/` | No Claude Code/Cursor adapter copies for release/update workflows | Accepted — by design (TFW-7) |
| TD-8 | TFW-6/B RF obs. | Med | `.tfw/conventions.md` §8 | `docs.md` workflow not listed in Workflows table | ✅ Resolved (TFW-7) |
| TD-9 | TFW-6/C RF obs. | Low | `.tfw/README.md` L77 | Project structure lists 6 workflows but §Canonical Workflows says "five" (docs omitted) — related to TD-8 | ✅ Resolved (TFW-7) |
| TD-10 | TFW-7 RF obs. | Low | `.tfw/glossary.md` L62 | Workflow definition says "Three canonical workflows" — refers to core lifecycle triad (plan, handoff, resume) | ✅ Resolved (TFW-8) |
| TD-11 | TFW-7 RF obs. | Low | `.tfw/README.md` L280 | Evolution §v3 says "3 canonical workflows" — refers to core lifecycle triad | ✅ Resolved (TFW-8) |
| TD-12 | TFW-8/A RF obs. | Low | `.tfw/templates/REVIEW.md` | Template uses `{coordinator}` as author placeholder; should be `{reviewer}` | ⬜ Backlog |
| TD-13 | TFW-8/A RF obs. | Low | `.tfw/workflows/docs.md` | Already references "Coordinator / Reviewer" from prior session — consistent but predates TFW-8 | Accepted — consistent with new role |
| TD-14 | TFW-8/B RF obs. | Low | `.tfw/README.md` L213 | "one AI agent fills both Coordinator and Executor roles" — could mention Reviewer | Accepted — small projects may skip Reviewer |
| TD-15 | TFW-8/B RF obs. | Low | `.tfw/README.md` L250 | Anti-patterns says "Coordinator skips review" — could update to Reviewer | Accepted — meaning is clear in context |
| TD-16 | TFW-8/B RF obs. | Low | `.tfw/CHANGELOG.md` L31 | Historical "3 canonical workflows" in v0.2.0 entry | Accepted — historical record, correct for that version |
| TD-17 | TFW-9 RF obs. | Low | `.tfw/conventions.md` L146 | `update.md` workflow entry could add "fetch upstream" to match new Step 0 | ✅ Resolved |
| TD-18 | TFW-9 RF obs. | Low | `.tfw/README.md` | May still have old description of update workflow | ✅ Resolved |
| TD-19 | TFW-10 RF obs. | Low | `.tfw/adapters/antigravity/tfw-rules.md.template` | Downstream projects that already copied this template will retain `TFW v3` in their `.agent/rules/tfw.md` until they re-copy from the updated template. No automated migration exists. | → backlog; mention in adapter README or next tfw-update release notes |
| TD-20 | TFW-11/B RF obs. #1 | Low | `.agent/workflows/tfw-plan.md:131` | Antigravity adapter copy of plan.md still shows old pipeline (no 🔬 RES) | ✅ Resolved (TFW-11/C) |
| TD-21 | TFW-11/B RF obs. #2 | Low | `.tfw/init.md:30-37` | Step 2 PROJECT_CONFIG.yaml example doesn't include `res` template | ✅ Resolved (TFW-11/C) |
| TD-22 | TFW-11/B RF obs. #3 | Low | `.tfw/init.md:87-93` | Antigravity workflow copy commands missing `research.md` | ✅ Resolved (TFW-11/C) |
| TD-23 | TFW-11/B RF obs. #4 | Low | `.tfw/README.md:73` | Project Structure tree comment missing RES in templates list | ✅ Resolved (TFW-11/C) |
| TD-24 | TFW-11/B RF obs. #5 | Low | `.tfw/README.md:74` | Project Structure tree comment missing research in workflows list | ✅ Resolved (TFW-11/C) |

| TD-25 | TFW-11/C REVIEW obs. | Low | `.tfw/conventions.md` L1, `.tfw/glossary.md` L1 | Title headers still say `TFW 0.4` — should be `0.5` after version bump | ✅ Resolved (TFW-12) |
| TD-26 | TFW-11/C REVIEW AC-10 | Low | `.agent/rules/tfw.md` L5,12 | Missing version identifier and RES in templates list (project-specific copy) | ✅ Resolved (TFW-12) |

| TD-27 | TFW-12 RF obs. #1 | Low | `.tfw/adapters/antigravity/README.md` L20-24, 49-56 | Workflow copy commands only list plan/handoff/review/resume — missing research/docs/release/update | → backlog |
| TD-28 | TFW-12 RF obs. #2 | Low | `.tfw/init.md` L98-104 | Antigravity workflow copy commands incomplete — same missing workflows as TD-27 | → backlog |

> Added by REVIEW files during task lifecycle. See `.tfw/workflows/docs.md`.
