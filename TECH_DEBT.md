# Tech Debt Registry

| # | Source | Severity | File(s) | Description | Status |
|---|--------|----------|---------|-------------|--------|
| TD-12 | TFW-8/A RF obs. | Low | `.tfw/templates/REVIEW.md` | Template uses `{coordinator}` as author placeholder; should be `{reviewer}` | ⬜ Backlog |
| TD-33 | TFW-14 RES obs. | Low | `.tfw/workflows/handoff.md`, adapters | `tfw-handoff` misnaming — no handoff status/document exists. Consider renaming to `tfw-execute`. Low priority, high blast radius | Open |
| TD-35 | TFW-14 RF obs. #2 | Low | `.tfw/glossary.md` L60 | RESEARCH entry doesn't mention pros/cons format or default recommendation | Open |
| TD-36 | TFW-14 RF obs. #3 | Low | `.tfw/glossary.md` L66 | Pass definition uses old model, doesn't mention "sufficient for HL finalization" | Open |
| TD-37 | TFW-14 RF obs. #4 | Low | `.tfw/conventions.md` L50 | RES artifact description doesn't mention Briefing or Closure sections | Open |
| TD-40 | TFW-15 RF obs. #3 | Low | `.tfw/conventions.md` L222 | Role Lock table handoff.md Forbidden column incomplete — should list forbidden artifacts | ⬜ Backlog |
| TD-45 | TFW-18 RF obs. #1 | Low | `.tfw/conventions.md` | §10.1 and §10.2 subsection numbering breaks the flat numbering scheme (§1-§15). Future renumbering pass needed | ⬜ Backlog |
| TD-46 | TFW-18 RF obs. #2 | Low | `.tfw/workflows/init.md` | Phase 5 verify checklist references old step numbers after .user_preferences.md insertion shifted 5→6, 6→7 | ⬜ Backlog |
| TD-49 | TFW-21 RF obs. #2 | Low | `.tfw/workflows/handoff.md` | Anti-patterns section partially overlaps conventions.md §14 | ⬜ Backlog |
| TD-50 | TFW-19 RF obs. #1 | Low | `.tfw/conventions.md` | §2 Required Artifacts doesn't list config.md — only original 10 listed, but §8 now has 11 workflows | ⬜ Backlog |
| TD-51 | TFW-19 RF obs. #2 | Low | `.tfw/PROJECT_CONFIG.yaml` | `tfw.workflows` section missing `config: .tfw/workflows/config.md` — needs adding for consistency | ⬜ Backlog |
| TD-52 | TFW-18-B RF obs. #1 | Low | `.tfw/README.md` L77 | §Project Structure tree lists old workflow set — doesn't include knowledge/config | ⬜ Backlog |
| TD-53 | TFW-18-B RF obs. #2 | Low | `.tfw/workflows/review.md` L79 | review.md Step 4 FC reminder still uses old «project knowledge» framing — not yet reframed to «strategic knowledge» | ⬜ Backlog |
| TD-57 | TFW-23/B RF obs. #1 | Med | `.tfw/workflows/config.md` L19,29 | Edit mode prompts in Russian — inconsistent with English-first convention | ⬜ Backlog |
| TD-59 | TFW-23 REVIEW FC#1 | High | `.tfw/workflows/` | No crash-recovery gate mechanism — after session crash, WAIT gates are lost. Need "Gate Recovery" protocol | ⬜ Backlog |
| TD-60 | TFW-24 RF obs. #1 | Low | `.tfw/conventions.md` L129 | §10.1, §10.2, §10 numbered out of order — inherited from previous tasks | ⬜ Backlog |
| TD-61 | TFW-24 RF obs. #2 | Low | `.tfw/glossary.md` L66 | RESEARCH entry says "Optional — user can skip with confirmation" — duplicates plan.md Step 6 logic | ⬜ Backlog |
| TD-62 | TFW-24 REVIEW | Med | `.tfw/conventions.md` L292-303 | Hard Stop Rule only covers Coordinator→Executor and Executor→Reviewer. Missing: Researcher→Coordinator transition | ⬜ Backlog |
| TD-63 | TFW-25 RF obs. #1 | Med | `KNOWLEDGE.md` L39-75 | §1 Architecture Decisions table (D1-D33) = 34 rows with long rationale text. Main driver of KNOWLEDGE.md exceeding 120-line target. Consider compression or active/archived split | ⬜ Backlog |

> Added by REVIEW files during task lifecycle. See `.tfw/workflows/docs.md`.
