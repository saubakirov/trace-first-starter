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
| TD-27 | TFW-12 RF obs. #1 | Low | `.tfw/adapters/antigravity/README.md` L20-24, 49-56 | Workflow copy commands only list plan/handoff/review/resume — missing research/docs/release/update | ✅ Resolved (consistency fix 2026-03-31) |
| TD-28 | TFW-12 RF obs. #2 | Low | `.tfw/init.md` L98-104 | Antigravity workflow copy commands incomplete — same missing workflows as TD-27 | Obsolete — init.md replaced by workflow (TFW-13) |
| TD-29 | TFW-13/B RF obs. #1 | Med | `.tfw/conventions.md` L26-30 | §2 Required Artifacts missing review.md, docs.md, release.md, update.md workflows + VERSION, CHANGELOG | ✅ Resolved (consistency fix 2026-03-31) |
| TD-30 | TFW-13/B RF obs. #2 | Med | `.tfw/conventions.md` L141-152 | §8 Workflows table missing research.md | ✅ Resolved (consistency fix 2026-03-31) |
| TD-31 | TFW-13/B RF obs. #3 | Med | `.tfw/conventions.md` L210-217 | §15 Role Lock table missing docs.md, release.md, update.md | ✅ Resolved (consistency fix 2026-03-31) |
| TD-32 | TFW-13/B RF obs. #4 | Low | `.tfw/adapters/antigravity/README.md` | Copy/sync missing research, docs, release, update workflows (overlaps TD-27) | ✅ Resolved (consistency fix 2026-03-31) |
| TD-33 | TFW-14 RES obs. | Low | `.tfw/workflows/handoff.md`, adapters | `tfw-handoff` misnaming — no handoff status/document exists. Consider renaming to `tfw-execute`. Low priority, high blast radius | Open |
| TD-34 | TFW-14 RF obs. #1 | Med | `.tfw/workflows/research.md` L26 | "gives birth to the details needed for TS" — still references TS as primary output after Closure Protocol addition. Should reference HL | ✅ Resolved (text removed, confirmed TFW-17 REVIEW) |
| TD-35 | TFW-14 RF obs. #2 | Low | `.tfw/glossary.md` L60 | RESEARCH entry doesn't mention pros/cons format or default recommendation | Open |
| TD-36 | TFW-14 RF obs. #3 | Low | `.tfw/glossary.md` L66 | Pass definition uses old model, doesn't mention "sufficient for HL finalization" | Open |
| TD-37 | TFW-14 RF obs. #4 | Low | `.tfw/conventions.md` L50 | RES artifact description doesn't mention Briefing or Closure sections | Open |
| TD-38 | TFW-15 RF obs. #1 | Low | `.tfw/glossary.md` L60 | RESEARCH entry says "between HL and TS" — document type names, correct as-is | Accepted |
| TD-39 | TFW-15 RF obs. #2 | Low | `.tfw/README.md` L133-134 | Step list uses "Write an HL" / "Write a TS" — document type names, correct as-is | Accepted |
| TD-40 | TFW-15 RF obs. #3 | Low | `.tfw/conventions.md` L222 | Role Lock table handoff.md Forbidden column incomplete — should list forbidden artifacts | ⬜ Backlog |
| TD-41 | TFW-15 RF obs. #4 | Low | `.tfw/workflows/plan.md` L155 | Anti-pattern uses document type names — correct as-is | Accepted |
| TD-42 | TFW-17 RF obs. #1 | Low | `.agent/workflows/tfw-plan.md` | Adapter copies inherit YAML frontmatter `description` from canonical — correct, not a bug | Accepted |
| TD-43 | TFW-17 RF obs. #2 | Low | `README.md` L127 | Task board TS column shows `✅` while TS file header says `🟡 TS_DRAFT` — consistent pattern (board = approval) | Accepted |
| TD-44 | TFW-17 RF obs. #3 | Low | `TECH_DEBT.md` | Executor incorrectly attributed TD-34 resolution to TFW-17. Actual resolution was TFW-14 | Accepted — corrected in TFW-17 REVIEW |
| TD-45 | TFW-18 RF obs. #1 | Low | `.tfw/conventions.md` | §10.1 and §10.2 subsection numbering breaks the flat numbering scheme (§1-§15). Future renumbering pass needed | ⬜ Backlog |
| TD-46 | TFW-18 RF obs. #2 | Low | `.tfw/workflows/init.md` | Phase 5 verify checklist references old step numbers after .user_preferences.md insertion shifted 5→6, 6→7 | ⬜ Backlog |
| TD-47 | TFW-18 RF obs. #3 | Low | `KNOWLEDGE.md` | Live KNOWLEDGE.md missing §5 Project Facts — template has it, project file doesn't yet | ✅ Resolved (first `/tfw-knowledge` run 2026-04-03) |
| TD-48 | TFW-21 RF obs. #1 | Low | `.tfw/workflows/plan.md` | Naming Rules table (L64-75) duplicates conventions.md §4 — ~100 words recoverable | ✅ Resolved (TFW-19 — content already removed) |
| TD-49 | TFW-21 RF obs. #2 | Low | `.tfw/workflows/handoff.md` | Anti-patterns section partially overlaps conventions.md §14 | ⬜ Backlog |
| TD-50 | TFW-19 RF obs. #1 | Low | `.tfw/conventions.md` | §2 Required Artifacts doesn't list config.md — only original 10 listed, but §8 now has 11 workflows | ⬜ Backlog |
| TD-51 | TFW-19 RF obs. #2 | Low | `.tfw/PROJECT_CONFIG.yaml` | `tfw.workflows` section missing `config: .tfw/workflows/config.md` — needs adding for consistency | ⬜ Backlog |
| TD-52 | TFW-18-B RF obs. #1 | Low | `.tfw/README.md` L77 | §Project Structure tree lists old workflow set — doesn't include knowledge/config (table in §Canonical Workflows was updated) | ⬜ Backlog |
| TD-53 | TFW-18-B RF obs. #2 | Low | `.tfw/workflows/review.md` L79 | review.md Step 4 FC reminder still uses old «project knowledge» framing — not yet reframed to «strategic knowledge» | ⬜ Backlog |
| TD-54 | TFW-22 RF obs. #1 | Med | `conventions.md` L29, 181, 276 | 3 stale references to `research.md` instead of `research/base.md` or `research/` directory. Context loading list, workflows table, Role Lock table. | ✅ Resolved (TFW-22 REVIEW) |
| TD-55 | TFW-22 RF obs. #2 | Low | `conventions.md` L277 | Role Lock table for `handoff.md` lists `code` in Forbidden Artifacts. But `handoff.md` explicitly allows executor to write code (line 64). Contradiction. | ✅ Resolved (TFW-22 REVIEW) |
| TD-56 | TFW-23/A RF obs. #1 | Low | `.tfw/CHANGELOG.md` L17 | Historical entry has `Визуализация результата` in Russian — historical record, not active template | Accepted |
| TD-57 | TFW-23/B RF obs. #1 | Med | `.tfw/workflows/config.md` L19,29 | Edit mode prompts in Russian ("Что хотите изменить…", "Применить?") — inconsistent with English-first convention | ⬜ Backlog |
| TD-58 | TFW-23/A RF obs. #2 | Low | `tasks/*` | Existing filled artifacts use RU headings — expected, historical | Accepted |
| TD-59 | TFW-23 REVIEW FC#1 | High | `.tfw/workflows/` | No crash-recovery gate mechanism — after session crash, WAIT gates are lost. Need "Gate Recovery" protocol | ⬜ Backlog |
| TD-60 | TFW-24 RF obs. #1 | Low | `.tfw/conventions.md` L129 | §10.1, §10.2, §10 numbered out of order — inherited from previous tasks | ⬜ Backlog |
| TD-61 | TFW-24 RF obs. #2 | Low | `.tfw/glossary.md` L66 | RESEARCH entry says "Optional — user can skip with confirmation" — duplicates plan.md Step 6 logic | ⬜ Backlog |
| TD-62 | TFW-24 REVIEW | Med | `.tfw/conventions.md` L292-303 | Hard Stop Rule only covers Coordinator→Executor and Executor→Reviewer. Missing: Researcher→Coordinator transition | ⬜ Backlog |

> Added by REVIEW files during task lifecycle. See `.tfw/workflows/docs.md`.
