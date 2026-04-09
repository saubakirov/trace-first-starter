# Tech Debt Registry

| # | Source | Severity | File(s) | Description | Status |
|---|--------|----------|---------|-------------|--------|
| TD-12 | TFW-8/A RF obs. | Low | `.tfw/templates/REVIEW.md` | Template uses `{coordinator}` as author placeholder; should be `{reviewer}` | ✅ Quick fix |
| TD-33 | TFW-14 RES obs. | Low | `.tfw/workflows/handoff.md`, adapters | `tfw-handoff` misnaming — no handoff status/document exists. Consider renaming to `tfw-execute`. Low priority, high blast radius | Open |
| TD-35 | TFW-14 RF obs. #2 | Low | `.tfw/glossary.md` L60 | RESEARCH entry doesn't mention pros/cons format or default recommendation | Open |
| TD-36 | TFW-14 RF obs. #3 | Low | `.tfw/glossary.md` L66 | Pass definition uses old model, doesn't mention "sufficient for HL finalization" | Open |
| TD-37 | TFW-14 RF obs. #4 | Low | `.tfw/conventions.md` L50 | RES artifact description doesn't mention Briefing or Closure sections | ✅ Quick fix |
| TD-40 | TFW-15 RF obs. #3 | Low | `.tfw/conventions.md` L292 | Role Lock table handoff.md Forbidden column incomplete — should list forbidden artifacts | ✅ Already correct (HL, TS, RES, REVIEW) |
| TD-45 | TFW-18 RF obs. #1 | Low | `.tfw/conventions.md` | §10.1 and §10.2 subsection numbering breaks the flat numbering scheme (§1-§15). Future renumbering pass needed | ⬜ Backlog |
| TD-46 | TFW-18 RF obs. #2 | Low | `.tfw/workflows/init.md` | Phase 5 verify checklist references old step numbers after .user_preferences.md insertion shifted 5→6, 6→7 | ✅ Verified: no step number references in Phase 5 |
| TD-49 | TFW-21 RF obs. #2 | Low | `.tfw/workflows/handoff.md` | Anti-patterns section partially overlaps conventions.md §14 | ✅ Quick fix (ref + role-specific only) |
| TD-50 | TFW-19 RF obs. #1 | Low | `.tfw/conventions.md` | §2 Required Artifacts doesn't list config.md — only original 10 listed, but §8 now has 11 workflows | ✅ Quick fix |
| TD-51 | TFW-19 RF obs. #2 | Low | `.tfw/PROJECT_CONFIG.yaml` | `tfw.workflows` section missing `config: .tfw/workflows/config.md` — needs adding for consistency | ✅ Quick fix |
| TD-52 | TFW-18-B RF obs. #1 | Low | `.tfw/README.md` L77 | §Project Structure tree lists old workflow set — doesn't include knowledge/config | ✅ TFW-27 (.tfw/README.md cleanup) |
| TD-53 | TFW-18-B RF obs. #2 | Low | `.tfw/workflows/review.md` L79 | review.md Step 4 FC reminder still uses old «project knowledge» framing — not yet reframed to «strategic knowledge» | ✅ Quick fix |
| TD-57 | TFW-23/B RF obs. #1 | Med | `.tfw/workflows/config.md` L19,29 | Edit mode prompts in Russian — inconsistent with English-first convention | ✅ Quick fix |
| TD-59 | TFW-23 REVIEW FC#1 | High | `.tfw/workflows/` | No crash-recovery gate mechanism — after session crash, WAIT gates are lost. Need "Gate Recovery" protocol | ⬜ Backlog |
| TD-60 | TFW-24 RF obs. #1 | Low | `.tfw/conventions.md` L129 | §10.1, §10.2, §10 numbered out of order — inherited from previous tasks | ✅ TFW-29 |
| TD-61 | TFW-24 RF obs. #2 | Low | `.tfw/glossary.md` L91 | RESEARCH entry says "Optional — user can skip with confirmation" — duplicates plan.md Step 6 logic | ✅ Quick fix |
| TD-62 | TFW-24 REVIEW | Med | `.tfw/conventions.md` L302-322 | Hard Stop Rule only covers Coordinator→Executor and Executor→Reviewer. Missing: Researcher→Coordinator transition | ✅ Quick fix |
| TD-63 | TFW-25 RF obs. #1 | Med | `KNOWLEDGE.md` L39-75 | §1 Architecture Decisions table (D1-D33) = 34 rows with long rationale text. Main driver of KNOWLEDGE.md exceeding 120-line target. Consider compression or active/archived split | ⬜ Backlog |
| TD-64 | TFW-26 RF obs. #1 | Low | `.tfw/templates/RF.md` L67 | RF §6 category list duplicates conventions.md §10.1 — two places to update when categories change. Monitor, not blocking | ✅ Quick fix (replaced with ref) |
| TD-65 | TFW-26/A RF obs. #1 | Low | `.tfw/templates/KNOWLEDGE.md` | CRLF line endings while all other templates use LF. Inconsistent git diffs | ✅ Verified: LF (git autocrlf) |
| TD-66 | TFW-26/A RF obs. #2 | Med | `KNOWLEDGE.md` | §0 Source column uses backtick paths — predates §16.2 reference format. Migrate during tfw-docs | ✅ Quick fix (D1-D8, §2 all converted) |
| TD-67 | TFW-26/A RF obs. #3 | Med | `knowledge/*.md` | Existing topic files use backtick-path Source format — predates §16.2. Migrate during tfw-knowledge | ✅ Verified: already uses reference format |
| TD-68 | TFW-26/A RF obs. #4 | Low | `README.md` L136 | Task Board TFW-26 row lacks Phase A artifact links | ⬜ Backlog |
| TD-69 | TFW-26/B RF obs. #1 | Low | `docs/mkdocs.yml` | Nav: "Concepts > Philosophy" vs "Knowledge > Topics > Philosophy" — confusing label duplication | ✅ TFW-27/B |
| TD-70 | TFW-26/B RF obs. #2 | Med | `docs/scripts/gen_docs.py` | Tasks sidebar: single flat link, no per-task sidebar browsing | ✅ TFW-27/B |
| TD-71 | TFW-26/B RF obs. #3 | Med | `docs/mkdocs.yml` L44-47 | Knowledge topics hardcoded in nav. New topics require manual edit | ✅ TFW-27/B |
| TD-72 | TFW-26/B RF obs. #4 | High | `.tfw/` sources | Pre-existing relative links break after compilation (different output paths) | ✅ TFW-27/B |
| TD-73 | TFW-26/B RF obs. #6 | Med | `docs/requirements.txt` | MkDocs 2.0 will break mkdocs-gen-files plugin. Pin or monitor | ⬜ Backlog |
| TD-74 | TFW-26/B RF obs. #8 | Med | `docs/scripts/gen_docs.py` | `--strict` mode fails on absolute link INFO messages | ✅ TFW-27/B |
| TD-75 | TFW-26 knowledge session | Med | `.tfw/workflows/knowledge.md` | Strategic Session Insights (§11/§7) quality design: current scan list is minimal fix. Needs: (a) formalized priority tiers for insight sources, (b) explicit guidance on strategic vs technical filtering, (c) consider separate "strategic knowledge" consolidation pass vs standard FC processing | ⬜ Backlog |
| TD-76 | TFW-26 coordinator review | High | templates, workflows, glossary | Terminology proliferation: "Fact Candidates" (RF §6, REVIEW §5, RES), "Strategic Session Insights" (HL §11), "Execution Session Insights" (RF §7) = three names for one concept (potential facts for tfw-knowledge). Violates D28 (Naming Creates Behavior). Need: single canonical term, unified section name across all templates, glossary update. Current state confuses agents — they don't connect §11/§7 to FC pipeline | ⬜ Backlog |
| TD-77 | TFW-27/A RF obs. #1 | Low | `docs/mkdocs.yml` L3-4 | `site_url` and `repo_url` remain empty. Must be set before deployment | ✅ TFW-27/C |
| TD-78 | TFW-27/A RF obs. #2 | Low | `docs/index.md` | Placeholder landing page replaced with README.md | ✅ TFW-27/B |
| TD-79 | TFW-27/B RF obs. #1 | Med | `docs/scripts/gen_docs.py` | gen_docs.py at 692 LOC — exceeds 600 LOC threshold. `resolve_references()` (200+ LOC) extraction candidate → `resolvers.py` | ⬜ Backlog |
| TD-80 | TFW-27/B RF obs. #2 | Low | `docs/scripts/gen_docs.py` | Artifact resolver doesn't search PhaseX subfolders for `RF TFW-26`. Many "Unresolved reference" info messages | ⬜ Backlog |
| TD-81 | TFW-27/B RF obs. #3 | Med | `docs/scripts/gen_docs.py`, `README.md` | `_generate_tasks_index()` Task Board parser is fragile — regex-based parsing of README.md tables | ⬜ Backlog |
| TD-82 | TFW-27/B REVIEW | Low | `docs/mkdocs.yml` | `attr_list` and `md_in_html` extensions added for README logo — may be removable if README format changes | ⬜ Backlog |

| TD-83 | TFW-29 RF obs. #1 | Low | `KNOWLEDGE.md` L19, 39, 80, 108 | References to "conventions.md §16" now imprecise — §16 is a stub, full content in compilable_contract.md | ✅ Quick fix (P10, D34, Architecture Map updated) |
| TD-84 | TFW-29 RF obs. #3 + REVIEW | Med | 7 template files | Templates reference "conventions.md §16.2" or "§16 Reference Format" — should point to `compilable_contract.md §2` | ✅ Quick fix (all 7 files) |
| TD-85 | TFW-29 RF obs. #2 | Low | `.tfw/conventions.md` L198-206 | §9 Tool Adapter Pattern example doesn't mention .agent/rules | ✅ Quick fix |
| TD-86 | TFW-29 REVIEW | Low | `.tfw/glossary.md` L42-48 | Fact Candidate and Strategic Insight placed under Artifact Types heading — should be standalone sections | ✅ Quick fix |

> Added by REVIEW files during task lifecycle. See `.tfw/workflows/docs.md`.

