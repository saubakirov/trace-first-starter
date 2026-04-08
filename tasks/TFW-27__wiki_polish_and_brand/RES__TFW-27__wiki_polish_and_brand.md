# RES — TFW-27: Wiki Polish & Brand Identity

> **Date**: 2026-04-05
> **Author**: Researcher
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-27](HL-TFW-27__wiki_polish_and_brand.md)
> **Mode**: Pipeline (focused)

---

## Research Context

TFW-27 transforms the raw documentation site (TFW-26 output) into a polished, branded knowledge product. The HL proposed an artifact graph manifest as the backbone. Research investigated: (1) whether the graph is needed, (2) how to implement Wikipedia-style linking, (3) MkDocs dynamic navigation, (4) OSS landing page patterns.

## Briefing

→ [research/briefing.md](research/briefing.md)

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| R1 | **No artifact graph file.** TFW's markdown structure (KNOWLEDGE.md, reference patterns) already IS the navigable graph. Compiled docs with Wikipedia-linking = navigable graph for humans. AI reads markdown directly — TFW by design is AI-queryable | User: "плодить лишние сущности не надо." All 5 current TDs solvable without graph. TFW principle: don't create unnecessary entities. Graph .yaml = derived artifact that can stale |
| R2 | **Wikipedia-style linking via in-memory entity index.** gen_docs.py builds lookup at build time by scanning KNOWLEDGE.md, TECH_DEBT.md, tasks/. Resolves text mentions to clickable links. No file on disk | Entity index is ephemeral (build-time only), deterministic, no maintenance burden. Source Manifest + filesystem scan = sufficient input |
| R3 | **P{N} auto-resolution rejected.** P{N} has double semantics: KNOWLEDGE.md §0 globals vs HL §7 task-locals. `P1` = "Traces over code" globally but "handoff combines executor" in HL-TFW-8. Auto-resolution = guaranteed false positives. Instead: HTML anchors on KNOWLEDGE.md §0 rows for deep linking (`#p7`) | Scanned tasks/: P1 appears in 5+ different HLs with different meanings. Whitelist doesn't help — same number, different entity |
| R4 | **File paths without backticks — not resolved.** Only backtick-wrapped paths (`` `.tfw/conventions.md` ``) get resolved. Plain text `.tfw/conventions.md` risks matching URLs, code blocks, link targets | False positive examples found in README.md, task artifacts. Backtick = author signal "this is a path" |
| R5 | **Adopt `mkdocs-literate-nav` for dynamic navigation.** gen_docs.py generates SUMMARY.md via `mkdocs_gen_files.Nav()`. Static sections from §16.4 (hardcoded in code), dynamic sections (Knowledge, Tasks, Workflows) from filesystem scan. Hardcoded `nav:` deleted from mkdocs.yml | literate-nav designed to integrate with gen-files (same author). Zero conflicts with Material features (search, SEO, navigation.sections). Solves TD-71, TD-70, TD-69 |
| R6 | **Landing page = hybrid methodology + tool pattern.** Structure: logo → tagline → values (3 cards) → quick start (3 steps) → what's inside → badges. Based on analysis of 4 OSS projects (Conventional Commits, Keep a Changelog, SemVer, OpenClaw) | Methodology projects lead with "what + why." Product projects lead with quick start. TFW is both — neither pure pattern applies |

## Scope: gen_docs.py Enhancements

| # | Feature | LOC | What it fixes |
|---|---------|-----|---------------|
| 1 | Bare task ID resolver (`TFW-18` → task HL link) | ~15 | Missing task links in KNOWLEDGE.md Source columns |
| 2 | Markdown link rewriter (fix `[text](relative.md)` after source→output mapping) | ~50 | TD-72: ~31 broken links in `.tfw/` sibling refs + README→`.tfw/` |
| 3 | HTML anchors on table rows (P{N}, D{N}, TD-{N}, F{N}) | ~30 | Deep linking: `/knowledge-index/#p7`, `#d24`, `/reference/tech-debt/#td-72` |
| 4 | literate-nav integration (SUMMARY.md generation) | ~25 | TD-71, TD-70, TD-69: dynamic nav from filesystem |
| | **Total** | **~120** | |

## Hypotheses (from HL §10)

| # | Hypothesis | Result | Evidence |
|---|-----------|--------|----------|
| H1 | Artifact graph can be auto-generated from file structure | ⚫ Not needed | TFW markdown IS the graph. In-memory index at build time sufficient. User: "AI сам разберётся в TFW" |
| H2 | Dynamic nav via `mkdocs-literate-nav` | ✅ Confirmed | API (`mkdocs_gen_files.Nav()`) designed for this. Same author as gen-files. Zero Material conflicts |
| H3 | Broken links limited to `.tfw/` internal relative links | 🟡 Partial | Two categories: sibling links (15) + README→.tfw/ (16). Task `../` relative links NOT broken (folder structure preserved). Plus the Wikipedia-linking problem — text mentions without links |
| H4 | OSS methodology projects use consistent landing pattern | 🟡 Partial | Pattern exists (tagline + value prop + FAQ) but varies. Badges = TFW addition (none of 4 projects use them). Quick start only in product projects |
| H5 | Custom YAML schema for graph | ⚫ Not needed | No graph file. Schema design moot |

## HL Update Recommendations

| # | What to change |
|---|---------------|
| 1 | **Remove artifact graph from all phases.** No .yaml file, no graph generation script, no graph validation. Replace with: in-memory entity index in gen_docs.py |
| 2 | **Phase B scope: 4 features.** (1) Bare task ID resolver, (2) markdown link rewriter, (3) HTML table anchors, (4) literate-nav integration. ~120 LOC total |
| 3 | **Phase B DoD update.** "Graph exists" → "All §16.2 resolvers work + table anchors linkable." "Nav from graph" → "Nav auto-generated via literate-nav" |
| 4 | **§7 Principle #2 rewrite.** "Graph drives everything" → "Source Manifest drives link resolution. literate-nav drives navigation. TFW markdown IS the knowledge graph" |
| 5 | **P{N} resolver: HTML anchors only, no auto-resolution.** Double semantics (global vs task-local) makes auto-resolution unreliable |
| 6 | **File paths: backtick-only.** No plain text path resolution. Backtick = author signal |
| 7 | **Add `mkdocs-literate-nav` + `mkdocs-section-index` to docs/requirements.txt** |

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | philosophy | TFW's markdown structure IS the knowledge graph — no separate graph artifact needed. AI navigates markdown directly because TFW is designed for AI-queryability by structure (KNOWLEDGE.md as index, reference patterns, topic files). "Плодить лишние сущности не надо" | User, this research session | High |
| FC2 | constraint | P{N} has irreconcilable double semantics: KNOWLEDGE.md §0 (global principles) vs HL §7 (task-local principles). Same number = different entity. Auto-resolution impossible without context awareness beyond regex | Challenge C1, scan of 5+ HLs with conflicting P1 definitions | High |
| FC3 | philosophy | User expects "Wikipedia-feel" from documentation: every reference to a known entity = clickable link. Direction is always forward (text → target), never backward. Source columns in tables = primary location where task references need resolving | User, this session + RF TFW-26/B FC#3 | High |

## Conclusion

Research dramatically simplified TFW-27. The artifact graph — the HL's central concept — is unnecessary. TFW's existing markdown structure already embodies the knowledge graph; the compiled docs site with Wikipedia-style linking makes it navigable. The practical work is 4 targeted enhancements to gen_docs.py (~120 LOC) plus the landing page and brand identity from Phase A/C. P{N} auto-resolution was rejected on solid evidence (double semantics). The scope shrank from "build a graph engine" to "make existing resolvers complete + add nav automation."

---

*RES — TFW-27: Wiki Polish & Brand Identity | 2026-04-05*
