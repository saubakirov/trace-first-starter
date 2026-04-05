# TS — TFW-26 / Phase A: Compilable Contract + Infrastructure

> **Date**: 2026-04-05
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-26](../HL-TFW-26__documentation_site.md)

---

## 1. Objective

Define the **compilable contract** — a formal specification of what structure TFW artifacts MUST have for deterministic compilation into a navigable knowledge graph. This includes:
- Source manifest (what files are compiled)
- Reference format (how agents cite sources — text references that a script resolves into hyperlinks)
- Output structure (how the docs site is organized)
- Template/workflow amendments (where current artifacts need tighter conventions for the contract to work)

After this phase, every agent and every utility knows: what goes in, what comes out, and how references connect.

## 2. Scope

### In Scope
- Write §16 Compilable Contract in `.tfw/conventions.md` (source manifest, reference format, resolution rules, output structure)
- Audit and amend templates where Source/reference columns need standardized format
- Create `docs/mkdocs.yml` with MkDocs Material configuration
- Create `docs/scripts/gen_docs.py` skeleton (imports, manifest, function signatures, reference resolver pattern)
- Create `docs/requirements.txt`
- Create `.github/workflows/docs.yml` for GitHub Actions deployment
- Update `.gitignore` with `site/`

### Out of Scope
- gen_docs.py implementation logic (Phase B)
- Curated docs/index.md landing page (Phase C)
- GitLab CI/CD wrapper (Phase C)
- MCP server implementation (future task)
- Coordinator fact capture in HL template (future task, ref S9)

## 3. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/conventions.md` | MODIFY | Add §16: Compilable Contract |
| `.tfw/templates/KNOWLEDGE.md` | MODIFY | Source column: standardize reference format |
| `.tfw/templates/TOPIC_FILE.md` | MODIFY | Source column: add reference format note |
| `.tfw/templates/RF.md` | MODIFY | FC Source + Observations: reference format note |
| `.tfw/templates/REVIEW.md` | MODIFY | FC Source + Tech Debt: reference format note |
| `.tfw/templates/RES.md` | MODIFY | FC Source + HL Recommendations: reference format note |
| `.tfw/glossary.md` | MODIFY | Add: Compilable Contract, Reference Format, Source Manifest terms |
| `docs/mkdocs.yml` | CREATE | MkDocs + Material config |
| `docs/scripts/gen_docs.py` | CREATE | Skeleton with manifest, resolver pattern, function signatures |
| `docs/requirements.txt` | CREATE | Python dependencies |
| `.github/workflows/docs.yml` | CREATE | GitHub Actions build + deploy |
| `.gitignore` | MODIFY | Add `site/` |

**Budget:** 4 new files, 8 modifications = 12 total. Defaults: max 14 files, max 8 new, max 1200 LOC.

## 4. Detailed Steps

### Step 1: Define §16 Compilable Contract in conventions.md

Add after §15 (Role Lock Protocol).

#### §16.1 Source Manifest

All `.md` files in the project are compilable. The utility walks these paths:

| # | Source Path | Output Path | Behavior |
|---|------------|-------------|----------|
| 1 | `README.md` | `index.md` | Full copy. If `docs/index.md` exists, use it as override |
| 2 | `.tfw/README.md` | `concepts/philosophy.md` | Copy + frontmatter |
| 3 | `.tfw/init.md` | `getting-started.md` | Copy + frontmatter |
| 4 | `.tfw/conventions.md` | `reference/conventions.md` | Copy + frontmatter |
| 5 | `.tfw/glossary.md` | `reference/glossary.md` | Copy + frontmatter |
| 6 | `.tfw/CHANGELOG.md` | `reference/changelog.md` | Copy + frontmatter |
| 7 | `KNOWLEDGE.md` | `knowledge-index.md` | Copy + frontmatter (whole file, no split) |
| 8 | `knowledge/*.md` | `knowledge/{filename}.md` | Copy each + frontmatter |
| 9 | `TECH_DEBT.md` | `reference/tech-debt.md` | Copy + frontmatter |
| 10 | `RELEASE.md` | `reference/release.md` | Copy + frontmatter. Optional — skip if absent |
| 11 | `tasks/**/*.md` | `tasks/{same relative path}` | Copy + frontmatter. Preserve folder structure |
| 12 | `.tfw/workflows/**/*.md` | `reference/workflows/{path}` | Copy + frontmatter |
| 13 | `.tfw/templates/**/*.md` | `reference/templates/{path}` | Copy + frontmatter |

> **Principle:** `tasks/` preserve their folder structure in output so that all relative links between artifacts (HL→TS, RF→HL, REVIEW→RF) work without rewriting.

File existence rules:

| Source | Required? | On Missing |
|--------|-----------|------------|
| `README.md` | Required | ERROR |
| `.tfw/README.md`, `conventions.md`, `glossary.md`, `CHANGELOG.md`, `init.md` | Required | ERROR |
| `KNOWLEDGE.md` | Optional | WARNING, skip page |
| `knowledge/` | Optional | WARNING, skip section |
| `TECH_DEBT.md` | Optional | WARNING, skip page |
| `RELEASE.md` | Optional | Skip silently |
| `tasks/` | Optional | Skip silently |
| `docs/index.md` | Optional | Falls back to README.md |

#### §16.2 Reference Format

Agents write **text references** to other artifacts. A build-time resolver converts these into hyperlinks. Agents do NOT write full markdown links for cross-artifact references (saves tokens, reduces errors).

**Standard reference patterns:**

| Pattern | Example | Resolves to |
|---------|---------|-------------|
| `{TYPE} {PREFIX}-{N}` | `RF TFW-18` | `tasks/TFW-18*/RF__*.md` (glob) |
| `{TYPE} {PREFIX}-{N} §{section}` | `RF TFW-18 §6` | Same file, anchor to section |
| `{TYPE} {PREFIX}-{N}/{PHASE}` | `RF TFW-18/A` | `tasks/TFW-18*/PhaseA/RF__PhaseA*.md` or `tasks/TFW-18*/RF__PhaseA*.md` |
| `HL-{PREFIX}-{N}` | `HL-TFW-19` | `tasks/TFW-19*/HL-TFW-19*.md` |
| `D{N}` | `D24` | KNOWLEDGE.md §1 Architecture Decisions row |
| `P{N}` | `P7` | KNOWLEDGE.md §0 Philosophy row |
| `F{N}` in knowledge context | `F4` | knowledge/{category}.md row |
| `TD-{N}` | `TD-59` | TECH_DEBT.md row |
| `S{N}` | `S9` | HL §11 Strategic Insights row (task-local) |

**Where references appear:**
- `KNOWLEDGE.md` §0 Source column, §1 Source column, §2 Key Artifact column, §3 Source column
- `knowledge/*.md` Source(s) column
- `TECH_DEBT.md` Source column
- `RF.md` §2 Key Decisions (rationale text), §6 FC Source column
- `REVIEW.md` §3 Tech Debt Source column, §5 FC Source column
- `RES.md` Decisions Rationale column, HL Recommendations Source column, FC Source column
- Any inline mention in artifact prose

**Resolution rules:**
- Resolver uses `tfw.task_prefix` from PROJECT_CONFIG.yaml to know the prefix
- Glob-based: `{TYPE} TFW-18` → find `tasks/TFW-18*/{TYPE}__*.md`
- If glob returns multiple matches → use first alphabetically, emit WARNING
- If glob returns zero matches → leave as text, emit WARNING
- Phase references: `RF TFW-18/A` → search in `tasks/TFW-18*/PhaseA/` first, then task root
- `D{N}`, `P{N}`, `F{N}`, `TD-{N}` → anchor links within the appropriate index page
- Resolver runs as a post-processing step on generated pages (regex scan + replacement)

#### §16.3 Frontmatter Convention

Every output page gets YAML frontmatter:

```yaml
---
title: "{from first # heading or filename}"
source: "{relative path to source file}"
---
```

#### §16.4 Output Navigation Structure

```
Home                              ← README.md (full, with Task Board)
Getting Started                   ← .tfw/init.md
Concepts/
  Philosophy                      ← .tfw/README.md
Architecture/
  Knowledge Index                 ← KNOWLEDGE.md (whole file)
  Knowledge/
    {topic files}                 ← knowledge/*.md
Reference/
  Conventions                     ← .tfw/conventions.md
  Glossary                        ← .tfw/glossary.md
  Tech Debt                       ← TECH_DEBT.md
  Changelog                       ← .tfw/CHANGELOG.md
  Release                         ← RELEASE.md
  Workflows/                      ← .tfw/workflows/**/*.md
  Templates/                      ← .tfw/templates/**/*.md
Tasks/
  {task folders with all artifacts} ← tasks/**/*.md (preserved structure)
```

### Step 2: Amend templates — Reference Format

For each template, add a short note to Source column instructions specifying the reference format.

#### KNOWLEDGE.md template (`.tfw/templates/KNOWLEDGE.md`)

Change §0 Source column example from backtick-path to reference format:

```diff
-| P1 | _Describe your first principle_ | `tasks/{ID}/HL-...md` |
+| P1 | _Describe your first principle_ | HL-{PREFIX}-{N} |
```

Change §1 Architecture Decisions Source column:

```diff
-| # | Decision | Rationale | Source RF |
-|---|----------|-----------|-----------
-| D1 | _e.g., Chose PostgreSQL_ | _ACID needed_ | `tasks/{ID}/RF-...md` |
+| # | Decision | Rationale | Source |
+|---|----------|-----------|--------|
+| D1 | _e.g., Chose PostgreSQL_ | _ACID needed_ | RF {PREFIX}-{N} |
```

Change §2 Key Artifacts:

```diff
-| _PROJ-1_ | _Initial setup_ | `tasks/PROJ-1.../RF-...md` | _Foundation decisions_ |
+| _PROJ-1_ | _Initial setup_ | RF {PREFIX}-1 | _Foundation decisions_ |
```

Change §3 Legacy Source column:

```diff
-| _e.g., Old auth module_ | Deprecated | _2026-01_ | _OAuth2 flow_ | `tasks/{ID}/RF-...md` |
+| _e.g., Old auth module_ | Deprecated | _2026-01_ | _OAuth2 flow_ | RF {PREFIX}-{N} |
```

Also fix stale `§5` reference on L4 → `§4`:

```diff
-> See KNOWLEDGE.md §5 for the index.
+> See KNOWLEDGE.md §4 for the index.
```

This is TOPIC_FILE.md L4, not KNOWLEDGE.md.

#### TOPIC_FILE.md template (`.tfw/templates/TOPIC_FILE.md`)

Add reference format note to the table header area:

```diff
+> **Source format**: Use reference patterns (e.g., `RF TFW-18 §6`, `REVIEW TFW-22`).
+> Build-time resolver converts these to hyperlinks. See conventions.md §16.2.
+
 | # | Fact | Verified | Source(s) | Added |
 |---|------|----------|-----------|-------|
```

Fix stale §5 reference:

```diff
-> See KNOWLEDGE.md §5 for the index.
+> See KNOWLEDGE.md §4 for the index.
```

#### RF.md template (`.tfw/templates/RF.md`)

Add reference format note before FC table:

```diff
+> **Source format**: Use reference patterns (e.g., `RF TFW-18`, `D24`). See conventions.md §16.2.
+
 | # | Category | Candidate | Source | Confidence |
```

#### REVIEW.md template (`.tfw/templates/REVIEW.md`)

Add reference format note before FC table and Tech Debt table:

```diff
 ## 3. Tech Debt Collected
+> **Source format**: Use reference patterns (conventions.md §16.2).
 
 | # | Source | Severity | File | Description | Action |
```

```diff
+> **Source format**: Use reference patterns (e.g., `RF TFW-18`, `D24`). See conventions.md §16.2.
+
 | # | Category | Candidate | Source | Confidence |
```

#### RES.md template (`.tfw/templates/RES.md`)

Add reference format note before FC table:

```diff
+> **Source format**: Use reference patterns (e.g., `HL-TFW-19`, `D24`). See conventions.md §16.2.
+
 | # | Category | Candidate | Source | Confidence |
```

### Step 3: Add glossary terms

Add to `glossary.md` before `## Project-Specific Terms`:

```markdown
## Compilable Contract
Formal specification (conventions.md §16) of what structure TFW artifacts must have for deterministic compilation into documentation, MCP endpoints, or other output formats. Defines: source manifest (what files), reference format (how agents cite), resolution rules (how scripts resolve), output structure (where pages go). The contract is the interface between Layer 1 (agents) and Layer 2 (utilities).

## Reference Format
Standard text pattern for cross-artifact citations (conventions.md §16.2). Agents write structured text (e.g., `RF TFW-18 §6`, `D24`) instead of full markdown links. Build-time resolver converts these to hyperlinks. Saves tokens, reduces link-rot, enables multi-target output (web, MCP, archive).

## Source Manifest
Ordered list of project files that compilation utilities read (conventions.md §16.1). Includes: root artifacts, .tfw/ core, knowledge/ facts, tasks/ history. Each entry has a source path, output path, and transformation type.
```

### Step 4: Create `docs/mkdocs.yml`

```yaml
site_name: "My Project Docs"
site_url: ""
repo_url: ""

theme:
  name: material
  features:
    - navigation.sections
    - navigation.expand
    - navigation.indexes
    - search.suggest
    - search.highlight
    - content.code.copy
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

plugins:
  - search
  - gen-files:
      scripts:
        - scripts/gen_docs.py

nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - Concepts:
      - Philosophy: concepts/philosophy.md
  - Architecture:
      - Knowledge Index: knowledge-index.md
      - Knowledge: knowledge/
  - Reference:
      - Conventions: reference/conventions.md
      - Glossary: reference/glossary.md
      - Tech Debt: reference/tech-debt.md
      - Changelog: reference/changelog.md
      - Release: reference/release.md
      - Workflows: reference/workflows/
      - Templates: reference/templates/
  - Tasks: tasks/

markdown_extensions:
  - tables
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - toc:
      permalink: true
```

> Note: `nav` structure for `tasks/` will be auto-generated by gen_docs.py from Task Board in README.md. This config is a skeleton.

### Step 5: Create `docs/scripts/gen_docs.py`

```python
"""TFW Documentation Generator — mkdocs-gen-files script.

Reads TFW project artifacts and generates virtual MkDocs pages.
Runs at build time via the mkdocs-gen-files plugin.

Contract: .tfw/conventions.md §16 (Compilable Contract)
"""

import re
from pathlib import Path
import mkdocs_gen_files

# --- §16.1 Source Manifest ---

# Static sources: (source_path, output_path, required)
STATIC_SOURCES = [
    ("README.md", "index.md", True),
    (".tfw/README.md", "concepts/philosophy.md", True),
    (".tfw/init.md", "getting-started.md", True),
    (".tfw/conventions.md", "reference/conventions.md", True),
    (".tfw/glossary.md", "reference/glossary.md", True),
    (".tfw/CHANGELOG.md", "reference/changelog.md", True),
    ("KNOWLEDGE.md", "knowledge-index.md", False),
    ("TECH_DEBT.md", "reference/tech-debt.md", False),
    ("RELEASE.md", "reference/release.md", False),
]

# Glob sources: (glob_pattern, output_prefix, required)
GLOB_SOURCES = [
    ("knowledge/*.md", "knowledge/", False),
    ("tasks/**/*.md", "tasks/", False),
    (".tfw/workflows/**/*.md", "reference/workflows/", False),
    (".tfw/templates/**/*.md", "reference/templates/", False),
]

# Curated override
INDEX_OVERRIDE = "docs/index.md"

# --- §16.2 Reference Patterns ---

# Compiled at build time from PROJECT_CONFIG.yaml tfw.task_prefix
TASK_PREFIX = "TFW"  # TODO: Phase B — read from config

REFERENCE_PATTERNS = [
    # {TYPE} {PREFIX}-{N} — e.g., "RF TFW-18", "HL-TFW-19"
    (r'\b(HL|TS|RF|ONB|RES|REVIEW)[- ](' + TASK_PREFIX + r'-\d+)\b', '_resolve_artifact_ref'),
    # {TYPE} {PREFIX}-{N}/{PHASE} — e.g., "RF TFW-18/A"
    (r'\b(HL|TS|RF|ONB|RES|REVIEW)[- ](' + TASK_PREFIX + r'-\d+)/([A-Z])\b', '_resolve_phase_ref'),
    # D{N}, P{N}, TD-{N} — decision/principle/tech-debt references
    (r'\bD(\d+)\b', '_resolve_decision_ref'),
    (r'\bP(\d+)\b', '_resolve_principle_ref'),
    (r'\bTD-(\d+)\b', '_resolve_techdebt_ref'),
]


# --- Transformation Functions ---

def add_frontmatter(content: str, title: str, source: str) -> str:
    """Inject YAML frontmatter (§16.3)."""
    # TODO: Phase B
    pass


def extract_title(content: str, filename: str) -> str:
    """Derive title from first # heading, fallback to filename."""
    # TODO: Phase B
    pass


def copy_with_frontmatter(source_path: str, output_path: str) -> None:
    """Read source, add frontmatter, write virtual page."""
    # TODO: Phase B
    pass


def copy_glob(pattern: str, output_prefix: str) -> None:
    """Glob source files, copy each with frontmatter to output prefix."""
    # TODO: Phase B
    pass


def validate_sources() -> list[str]:
    """Check required sources exist, warn on missing optional (§16.1)."""
    # TODO: Phase B
    pass


# --- §16.2 Reference Resolver ---

def resolve_references(content: str) -> str:
    """Scan content for reference patterns, resolve to hyperlinks.

    Uses glob to find actual file paths for artifact references.
    Leaves unresolvable references as plain text with WARNING.
    """
    # TODO: Phase B — implement pattern matching + glob resolution
    pass


def _resolve_artifact_ref(match: re.Match) -> str:
    """Resolve '{TYPE} {PREFIX}-{N}' to file path."""
    # TODO: Phase B
    pass


def _resolve_phase_ref(match: re.Match) -> str:
    """Resolve '{TYPE} {PREFIX}-{N}/{PHASE}' to file path."""
    # TODO: Phase B
    pass


def _resolve_decision_ref(match: re.Match) -> str:
    """Resolve 'D{N}' to KNOWLEDGE.md anchor."""
    # TODO: Phase B
    pass


def _resolve_principle_ref(match: re.Match) -> str:
    """Resolve 'P{N}' to KNOWLEDGE.md anchor."""
    # TODO: Phase B
    pass


def _resolve_techdebt_ref(match: re.Match) -> str:
    """Resolve 'TD-{N}' to TECH_DEBT.md anchor."""
    # TODO: Phase B
    pass


# --- Main ---

def main():
    """Entry point for mkdocs-gen-files plugin."""
    warnings = validate_sources()
    for w in warnings:
        print(f"WARNING [gen_docs]: {w}")

    # TODO: Phase B
    # 1. Process static sources
    # 2. Process glob sources
    # 3. Apply reference resolver to all generated pages


if __name__ == "__main__":
    main()
```

### Step 6: Create `docs/requirements.txt`

```
mkdocs>=1.6
mkdocs-material>=9.5
mkdocs-gen-files>=0.5
```

### Step 7: Create `.github/workflows/docs.yml`

```yaml
name: Deploy Documentation

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install -r docs/requirements.txt

      - name: Build docs
        run: mkdocs build --config-file docs/mkdocs.yml --strict

      - uses: actions/upload-pages-artifact@v3
        with:
          path: site/

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

### Step 8: Update `.gitignore`

Add `site/` if not present.

## 5. Acceptance Criteria

- [ ] `.tfw/conventions.md` §16 exists with: Source Manifest (13 entries), Reference Format (9 patterns), Resolution Rules, Frontmatter Convention, Output Navigation Structure
- [ ] KNOWLEDGE.md template Source columns use reference format (`RF {PREFIX}-{N}`) instead of backtick paths
- [ ] TOPIC_FILE.md template has reference format note before table
- [ ] RF.md, REVIEW.md, RES.md templates have reference format note before FC tables
- [ ] `glossary.md` has 3 new terms: Compilable Contract, Reference Format, Source Manifest
- [ ] `docs/mkdocs.yml` exists with MkDocs Material config, gen-files plugin, tasks/ in nav
- [ ] `docs/scripts/gen_docs.py` skeleton has: static manifest, glob manifest, reference patterns list, resolver function signatures
- [ ] `docs/requirements.txt` lists 3 dependencies
- [ ] `.github/workflows/docs.yml` exists with build + deploy jobs
- [ ] `.gitignore` includes `site/`
- [ ] All reference patterns in §16.2 are unambiguous — each pattern maps to exactly one resolution rule

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Reference resolver regex has false positives (e.g., `P3` matching prose "P3 protocol") | Resolver only processes content within Source columns and known table formats. Or: use word boundary `\b` + context check. Phase B will tune |
| tasks/ contains 100+ files — nav becomes unwieldy | MkDocs Material collapsible sections. Tasks grouped by folder. Task Board in index provides navigation |
| KNOWLEDGE.md as single page is long (140 lines) | Acceptable — page has TOC with anchors. Split is a future optimization if needed |
| Template changes require adapter sync | Phase A RF will list adapter files to sync. Standard procedure per convention F5 |

---

*TS — TFW-26 / Phase A: Compilable Contract + Infrastructure | 2026-04-05*
