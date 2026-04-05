# Extract — "What do we NOT see?"
> Parent: [HL-TFW-26](../HL-TFW-26__documentation_site.md)
> Goal: Compile TFW project artifacts into a publishable documentation site — deterministic, scriptable, no agent involvement.

## Findings

### E1: Compilable Contract — Artifact Structure Audit

Audited all 10 source artifacts. Each analyzed for: structure consistency, heading format, cross-references, frontmatter needs, transformation complexity.

| Source | Heading format | Cross-refs | Frontmatter needed? | Transformation |
|--------|---------------|------------|---------------------|----------------|
| `README.md` | `# Title` + `## Sections` | Relative links to `.tfw/`, `tasks/` | Yes: title, nav_order | **Moderate** — landing page extraction (drop Task Board for docs?) |
| `KNOWLEDGE.md` | `## 0-4` numbered sections | Links to `tasks/` RF files | Yes: title, nav_order | **Split** — §0-3 → separate pages. §4 → index only |
| `knowledge/*.md` | `# Knowledge: {Category}` + table | Links to RF/REVIEW sources | Yes: title, category | **Minimal** — add frontmatter, copy |
| `TECH_DEBT.md` | `# Tech Debt Registry` + table | Source column references tasks | Yes: title | **Minimal** — add frontmatter, copy |
| `.tfw/README.md` | `# TFW` + long-form narrative | Internal refs to conventions, glossary | Yes: title, nav_order | **Moderate** — extract sections to concept pages |
| `.tfw/conventions.md` | `## 1-15` numbered sections | Refs to glossary, templates, workflows | Yes: title | **Minimal** — add frontmatter, copy (or split large sections) |
| `.tfw/glossary.md` | `# TFW Glossary` + `### Terms` | Refs to conventions | Yes: title | **Minimal** — add frontmatter, copy |
| `.tfw/CHANGELOG.md` | Keep a Changelog format | Refs to tasks | Yes: title | **Minimal** — add frontmatter, copy |
| `.tfw/init.md` | `# Getting Started` pointer | Refs to workflow | Yes: title | **Minimal** — getting-started page |
| `RELEASE.md` | `# Release Strategy` | Refs to CHANGELOG | Yes: title | **Minimal** — add frontmatter, copy |

**Key insight**: Most artifacts need only frontmatter injection + copy. Only 3 need real transformation:
1. `KNOWLEDGE.md` — split by section (§0-§3 are different page types)
2. `.tfw/README.md` — long (353 lines) — could be split into concepts pages OR served as single page
3. `README.md` — landing page extraction (Task Board is not public docs content)

### E2: Compilable Contract — Formal Specification

The **compilable contract** is the strict structure each artifact type MUST have for deterministic compilation:

```yaml
# Compilable Contract v1 — what Layer 2 (utility) expects

artifacts:
  knowledge_topic:
    location: knowledge/{category}.md
    must_have:
      - "# Knowledge: {Category}" as H1
      - blockquote with "Topic file for" and "See KNOWLEDGE.md"
      - table with columns: #, Fact, Verified, Source(s), Added
    frontmatter_inject:
      title: "Knowledge: {Category}"
      section: knowledge

  knowledge_index:
    location: KNOWLEDGE.md
    must_have:
      - "# KNOWLEDGE.md" as H1
      - "## 0. Philosophy" section
      - "## 1. Architecture Map" section
      - "## 3. Legacy" section
      - "## 4. Project Facts" section (index table)
    compiler_action: split by ## sections → separate pages

  tech_debt:
    location: TECH_DEBT.md
    must_have:
      - "# Tech Debt Registry" as H1
      - table with columns: #, Source, Severity, File(s), Description, Status
    frontmatter_inject:
      title: "Tech Debt"
      section: reference

  changelog:
    location: .tfw/CHANGELOG.md
    must_have:
      - "# TFW Changelog" as H1
      - Keep a Changelog format ([x.y.z] — date)
    frontmatter_inject:
      title: "Changelog"
      section: reference

  conventions:
    location: .tfw/conventions.md
    must_have:
      - "# TFW Conventions" as H1
      - "## N)" numbered sections
    frontmatter_inject:
      title: "Conventions"
      section: reference

  glossary:
    location: .tfw/glossary.md
    must_have:
      - "# TFW Glossary" as H1
      - "### Term" format for entries
    frontmatter_inject:
      title: "Glossary"
      section: reference

  philosophy:
    location: .tfw/README.md
    must_have:
      - "# Trace-First Workflow (TFW)" as H1
      - "## Values and Principles" section
      - "## How It Works" section
    compiler_action: serve as single page OR split by ##
    frontmatter_inject:
      title: "Philosophy & Design"
      section: concepts

  landing:
    location: README.md
    must_have:
      - "# " as H1 (project title)
      - "## Quick Start" section
      - "## What's Inside" section
    compiler_action: extract non-Task-Board content for index page
    frontmatter_inject:
      title: "Home"
```

### E3: Source→Output Mapping — Revised from HL

Based on Gather and Extract findings, the HL §3.1 mapping needs revision:

```
┌─────────────────────────────────┐     ┌──────────────────────────────┐
│  TFW PROJECT (source)           │     │  MkDocs site (output)        │
│                                 │     │  built by mkdocs-gen-files   │
│                                 │     │                              │
│  README.md ─────────────────────┼────→│  index.md                    │
│  .tfw/README.md ────────────────┼────→│  concepts/philosophy.md      │
│  .tfw/init.md ──────────────────┼────→│  getting-started.md          │
│  KNOWLEDGE.md §0 ───────────────┼────→│  architecture/principles.md  │
│  KNOWLEDGE.md §1 ───────────────┼────→│  architecture/decisions.md   │
│  KNOWLEDGE.md §3 ───────────────┼────→│  architecture/legacy.md      │
│  knowledge/*.md ────────────────┼────→│  knowledge/*.md  (copy+fm)   │
│  TECH_DEBT.md ──────────────────┼────→│  reference/tech-debt.md      │
│  .tfw/conventions.md ───────────┼────→│  reference/conventions.md    │
│  .tfw/glossary.md ──────────────┼────→│  reference/glossary.md       │
│  .tfw/CHANGELOG.md ─────────────┼────→│  reference/changelog.md      │
│                                 │     │                              │
│  mkdocs.yml ← ← ← ← ← ← ← ← │     │  (MkDocs config — NEW file)  │
│  scripts/gen_docs.py ← ← ← ← ←│     │  (gen-files script — NEW)    │
└─────────────────────────────────┘     └──────────────────────────────┘
```

**Changes from HL:**
- No `docs/` folder committed to git
- `mkdocs.yml` + `scripts/gen_docs.py` added at project root
- Output is `site/` (MkDocs default), deployed via CI/CD
- `concepts/adapters.md` dropped (too specific for generic docs)

### E4: `mkdocs-gen-files` Script Complexity Estimate

The gen-files script needs to:
1. Read ~10 source files from various locations
2. For 7 of them: add YAML frontmatter + copy content
3. For 2 of them: split by `## ` headings into separate pages
4. For 1 (README.md): extract specific sections (remove Task Board)
5. Generate `nav` structure (or use `mkdocs-literate-nav`)

**Estimated LOC**: ~80-120 lines Python.

This is close to H3's "<100 LOC" hypothesis. The script is simple because:
- No content transformation (just split + frontmatter inject)
- No link rewriting (relative links still work within MkDocs)
- No parsing beyond `## ` heading detection

**BUT**: link rewriting IS needed for cross-references between artifacts. Example: `knowledge/convention.md` references `RF TFW-18 §6` — this link points to `tasks/` which is NOT in the docs output. These become dead links. Two options:
1. Accept dead links in docs (they work in the repo, not in the site)
2. Strip task references from docs output (lossy but clean)
3. Include task artifacts in docs (scope explosion)

**Recommendation**: Option 1 — accept dead links. The docs site is a compiled view. Source links to `tasks/` work in the repo context (GitHub), not in the docs context. This is a known, documented limitation.

### E5: New Files Required in TFW Project

For a TFW project to get docs, it needs:

| File | Purpose | Size |
|------|---------|------|
| `mkdocs.yml` | MkDocs configuration — theme, plugins, nav | ~30 lines |
| `scripts/gen_docs.py` | `mkdocs-gen-files` script — reads artifacts, writes docs | ~80-120 lines |
| `.github/workflows/docs.yml` | GitHub Actions deploy workflow | ~20 lines |
| `.gitlab-ci.yml` section | GitLab Pages job (if needed) | ~10 lines |
| `requirements-docs.txt` | Python deps for docs build | ~5 lines |

**Total new files**: 3-4 (not all projects need both GH+GL CI).

### E6: MkDocs Configuration Sketch

```yaml
site_name: "Project Docs"  # From PROJECT_CONFIG project.name
site_url: "https://tfw.saubakirov.kz"
theme:
  name: material
  features:
    - navigation.sections
    - navigation.expand
    - search.suggest
    - content.code.copy
plugins:
  - search
  - gen-files:
      scripts:
        - scripts/gen_docs.py
  - literate-nav:
      nav_file: SUMMARY.md
nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - Concepts:
    - Philosophy & Design: concepts/philosophy.md
  - Architecture:
    - Principles: architecture/principles.md
    - Decisions: architecture/decisions.md
    - Legacy: architecture/legacy.md
  - Knowledge:
    - knowledge/*.md  # Auto-expanded
  - Reference:
    - Conventions: reference/conventions.md
    - Glossary: reference/glossary.md
    - Tech Debt: reference/tech-debt.md
    - Changelog: reference/changelog.md
```

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Compilable contract defined — 8 artifact types with strict structure requirements | Need to validate: does the current artifact structure actually match the contract? (audited: YES, it does) |
| Most artifacts need minimal transformation (frontmatter + copy) | Only KNOWLEDGE.md and README.md need splitting/extraction |
| gen-files script ~80-120 LOC — close to H3 hypothesis | Need to challenge: is link rewriting really not needed? |
| New files in project: 3-4 (mkdocs.yml, gen_docs.py, CI workflow, requirements) | Acceptable scope — not invasive |
| Dead links from task references are a known limitation | Decision needed: accept vs strip vs include tasks |

**Sufficiency:**
- [x] External source used? (No additional external needed — this stage was internal artifact audit)
- [x] Briefing gap closed? (Compilable contract defined, source mapping revised)

**Deep mode:**
- [x] Hypothesis tested? (H1: partially confirmed — copy + frontmatter for 7/10 artifacts. H3: ~100 LOC plausible. H6: current structure IS sufficient)
- [x] Counter-evidence sought? (Link rewriting identified as gap. Dead links = known limitation)

**Metacognitive check:** I confirmed H6 (structure is already sufficient) through direct audit. This is confirmation, not new discovery. But the dead links issue IS new — it's a real gap that the HL §6 DoF doesn't mention. The contract specification in E2 is the most valuable output — it makes the implicit structure explicit.

Stage complete: YES
→ User decision: ___
