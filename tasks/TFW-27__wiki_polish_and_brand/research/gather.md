# Gather — "What do we NOT know?"
> Parent: [HL-TFW-27](../HL-TFW-27__wiki_polish_and_brand.md)
> Goal: Transform raw documentation output into a polished, branded, navigable knowledge product.

## Findings

### G1: OSS Methodology Landing Page Patterns

Analyzed 4 projects: Conventional Commits, Keep a Changelog, SemVer, OpenClaw.

**Key pattern:** TFW is a hybrid (methodology + tool). Methodology projects lead with spec/FAQ. Product projects lead with quick start. TFW needs both.

**Proposed landing structure:** logo → tagline ("Traces Over Code") → value proposition → core values (3 cards) → quick start (3 steps) → what's inside (link map) → badges → task board (README only).

### G2: Dynamic Navigation (MkDocs)

**Problem (TD-71):** Knowledge topics hardcoded in mkdocs.yml. New topic = manual edit.

**Solution:** `mkdocs-literate-nav` plugin + `mkdocs_gen_files.Nav()` API. gen_docs.py generates SUMMARY.md programmatically:
- Static sections (Home, Getting Started, Concepts, Reference) — hardcoded per §16.4
- Dynamic sections (Knowledge Topics, Tasks, Workflows, Templates) — filesystem scan
- Hardcoded `nav:` removed from mkdocs.yml

~20-30 LOC addition to gen_docs.py. Same plugin ecosystem (gen-files author = literate-nav author).

### G3: Link Quality — TWO distinct problems

**Problem A — 404 links:** Existing markdown links `[text](path)` that break after compilation because source→output paths differ. ~31 instances in `.tfw/` sibling links and README→`.tfw/` links. Fix: path rewriter using Source Manifest mapping.

**Problem B — Missing links (Wikipedia-style):** Plain text mentions of known entities that SHOULD be clickable links but aren't. Examples:
- `D24` mentioned as text → should link to KNOWLEDGE.md decisions table
- `TFW-18` mentioned without artifact type prefix → should link to task folder
- `P7` mentioned → should link to KNOWLEDGE.md principles
- `F4` mentioned → should link to knowledge topic file
- `.tfw/workflows/plan.md` in prose → should link to compiled page

gen_docs.py has 6 resolvers (of 9 defined in §16.2). Missing: P{N}, F{N}, S{N}. Also missing: bare task IDs without type prefix, file paths without backticks.

**Goal:** Maximum link density — like Wikipedia, every mention of a known entity becomes a clickable link on the compiled site. Build-time only (raw markdown stays as text references per §16.2 convention).

### G4: Artifact Graph — Decision: NOT needed

**User decision after discussion:** No separate graph.yaml file. Reasons:
1. TFW's markdown files (KNOWLEDGE.md, reference patterns) already encode the relationship graph
2. Compiled docs with Wikipedia-linking = navigable graph for humans
3. AI agents can navigate TFW's markdown directly — TFW is designed for this
4. Don't create unnecessary entities (TFW principle)

**Implementation:** gen_docs.py builds an in-memory entity index at build time by scanning KNOWLEDGE.md, TECH_DEBT.md, tasks/. Uses it for Wikipedia-style link resolution. No file on disk.

### G5: Graph/Schema Standards

No existing standard fits (JSON-LD, RDF, CITATION.cff all wrong scope). Moot — graph.yaml deferred. In-memory entity index in gen_docs.py needs no schema standard.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Landing page: hybrid methodology+tool pattern | None |
| Dynamic nav: literate-nav + gen_docs.py Nav() | None |
| Link quality: 2 problems (404 paths + missing Wikipedia links) | Need to map ALL entity types for resolver in Extract |
| Graph: not needed (in-memory index only) | None |

**Sufficiency:**
- [x] External source used? (CC, KaC, SemVer, OpenClaw, literate-nav docs)
- [x] Briefing gap closed? (all gather topics resolved with user direction)

Stage complete: YES
