# Tech Debt Registry

| # | Source | Severity | File(s) | Description | Status |
|---|--------|----------|---------|-------------|--------|
| TD-1 | TFW-3 RF obs. | Low | README.md, .tfw/README.md | "Who This Is For" in both — acceptable overlap but monitor for divergence | Accepted |
| TD-2 | TFW-4 HL | Med | `.tfw/` | Content duplication across conventions/README/glossary — Phase B planned | ⬜ TFW-4 Phase B |
| TD-3 | TFW-4 HL | Low | `.tfw/conventions.md` | ONB overhead for small single-phase tasks — Phase C planned | ⬜ TFW-4 Phase C |
| TD-4 | TFW-5 RF obs. | Low | `.tfw/README.md` | Workflows section lists only plan/handoff/resume — should mention docs | ⬜ Backlog |
| TD-5 | TFW-6/A RF obs. | Low | `README.md` | Empty line splitting Root Files table rows | ✅ Resolved (TFW-6/C) |
| TD-6 | TFW-6/A RF obs. | Med | `.tfw/PROJECT_CONFIG.yaml` | Build commands are placeholder `echo` — meta-project has no build | Accepted |
| TD-7 | TFW-6/B RF obs. | Low | `.agent/workflows/` | No Claude Code/Cursor adapter copies for release/update workflows | ⬜ Backlog |
| TD-8 | TFW-6/B RF obs. | Med | `.tfw/conventions.md` §8 | `docs.md` workflow not listed in Workflows table | ⬜ Backlog |
| TD-9 | TFW-6/C RF obs. | Low | `.tfw/README.md` L77 | Project structure lists 6 workflows but §Canonical Workflows says "five" (docs omitted) — related to TD-8 | ⬜ Backlog |

> Added by REVIEW files during task lifecycle. See `.tfw/workflows/docs.md`.
