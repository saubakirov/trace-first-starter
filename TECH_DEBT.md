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

> Added by REVIEW files during task lifecycle. See `.tfw/workflows/docs.md`.
