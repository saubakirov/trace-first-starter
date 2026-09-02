# Compilable Contract

> TFW artifacts are structured by design. This contract defines what structure utilities expect
> for deterministic compilation into documentation sites, MCP endpoints, or other output formats.
> Agents maintain structure (Layer 1). Utilities consume this contract (Layer 2).

## 1) Source Manifest

All `.md` files below are compilable. The utility walks these paths:

| # | Source Path | Output Path | Behavior |
|---|------------|-------------|----------|
| 1 | `README.md` | `index.md` | Full copy. If `docs/index.md` exists, use it as override |
| 2 | `.tfw/README.md` | `concepts/philosophy.md` | Copy + frontmatter |
| 3 | `.tfw/quickstart.md` | `getting-started.md` | Copy + frontmatter |
| 4 | `.tfw/conventions.md` | `reference/conventions.md` | Copy + frontmatter |
| 5 | `.tfw/glossary.md` | `reference/glossary.md` | Copy + frontmatter |
| 6 | `.tfw/CHANGELOG.md` | `reference/changelog.md` | Copy + frontmatter |
| 7 | `KNOWLEDGE.md` | `knowledge-index.md` | Copy + frontmatter (whole file, no split) |
| 8 | `knowledge/*.md` | `knowledge/{filename}.md` | Copy each + frontmatter |
| 9 | `RELEASE.md` | `reference/release.md` | Copy + frontmatter. Optional — skip if absent |
| 10 | `{container}/**/*.md` for each `tfw.task_containers` entry | `tasks/{same relative path}` | Copy + frontmatter. Preserve folder structure. Containers are configuration; the output prefix stays `tasks/` |
| 11 | `.tfw/workflows/**/*.md` | `reference/workflows/{path}` | Copy + frontmatter |
| 12 | `.tfw/templates/**/*.md` | `reference/templates/{path}` | Copy + frontmatter |
| 13 | `.tfw/compilable_contract.md` | `reference/compilable-contract.md` | Copy + frontmatter |

> **Principle:** task containers preserve their folder structure in output so that all relative links
> between artifacts (HL→TS, RF→HL, REVIEW→RF) work without rewriting.

File existence rules:

| Source | Required? | On Missing |
|--------|-----------|------------|
| `README.md` | Required | ERROR |
| `.tfw/README.md`, `conventions.md`, `glossary.md`, `CHANGELOG.md`, `quickstart.md` | Required | ERROR |
| `KNOWLEDGE.md` | Optional | WARNING, skip page |
| `knowledge/` | Optional | WARNING, skip section |
| `RELEASE.md` | Optional | Skip silently |
| task containers | Optional | Skip silently |
| `docs/index.md` | Optional | Falls back to README.md |

## 2) Reference Format

Agents write **text references** to other artifacts. A build-time resolver converts these into
hyperlinks. Agents do NOT write full markdown links for cross-artifact references (saves tokens,
reduces errors).

Standard reference patterns:

| Pattern | Example | Resolves to |
|---------|---------|-------------|
| `{TYPE} {ID}` | `RF TFW_20260829-010832_CRSW` | `{container}/**/{ID}*/RF__*.md` (glob, every container) |
| `{TYPE} {ID} §{section}` | `RF TFW_20260829-010832_CRSW §6` | Same file, anchor to section |
| `{TYPE} {ID}/{PHASE}` | `RF TFW_20260829-010832_CRSW/A` | `{container}/**/{ID}*/phase-a/RF__phase-a*.md` |
| `HL-{ID}` | `HL-TFW_20260829-010832_CRSW` | `{container}/**/{ID}*/HL-{ID}*.md` |
| `D{N}` | `D24` | KNOWLEDGE.md §1 Architecture Decisions row |
| `P{N}` | `P7` | HL §7 Principles row (task-local) |
| `PP{N}` | `PP2` | Project principle registry row — `KNOWLEDGE.md` §0 where a project keeps one. Reserved: no resolution in a project without §0 |
| `NS{N}` | `NS3` | Project North Star clause — the designated README section(s), conventions.md §3 |
| `F{N}` in knowledge context | `F4` | knowledge/{category}.md row |
| `TD-{N}` | `TD-59` | `tasks/DEBT-SNAPSHOT.md` row — the retired registry, sealed at 2.1.0. It carries no manifest row of its own: the task-container glob (row 10) already compiles it, exactly as it does `tasks/BOARD-SNAPSHOT.md`. One source, one output page |
| `S{N}` | `S9` | HL §11 Strategic Insights row (task-local) |

Where references appear:
- `KNOWLEDGE.md` §1 Source column, §2 Key Artifact column, §3 Source column
- `knowledge/*.md` Source(s) column
- `RF.md` §2 Key Decisions (rationale text), §7 FC Source column
- `REVIEW.md` §5 Tech Debt Source column, §7 FC Source column
- `RES.md` Decisions Rationale column, HL Recommendations Source column, FC Source column
- Any inline mention in artifact prose

Resolution rules:
- Resolver reads `tfw.task_containers` and searches every container, with and without year nesting. It recognizes each identifier whole in exactly three named forms: current `PREFIX_YYYYMMDD-HHMMSS_ABBR`, `2.0.0-dirty` `YYYYMMDD-HHMMSS__slug`, and legacy `PREFIX-N`; `tfw.task_prefix` supplies `PREFIX`
- Glob-based: `{TYPE} {ID}` → find `{container}/**/{ID}*/{TYPE}__*.md` across every configured container
- If glob returns multiple matches → use first alphabetically, emit WARNING
- If glob returns zero matches → leave as text, emit WARNING
- Phase references: `RF {ID}/A` → search in `{ID}*/phase-a/` first, then task root
- `D{N}`, `P{N}`, `F{N}`, `PP{N}`, `NS{N}`, `TD-{N}` → anchor links within the appropriate index page
- Resolver runs as a post-processing step on generated pages (regex scan + replacement)

## 3) Frontmatter Convention

Every output page gets YAML frontmatter:

```yaml
---
title: "{from first # heading or filename}"
source: "{relative path to source file}"
---
```

## 4) Output Navigation Structure

```
Home                              <- README.md (full, with the route to the index)
Getting Started                   <- .tfw/quickstart.md
Concepts/
  Philosophy                      <- .tfw/README.md
Architecture/
  Knowledge Index                 <- KNOWLEDGE.md (whole file)
  Knowledge/
    {topic files}                 <- knowledge/*.md
Reference/
  Conventions                     <- .tfw/conventions.md
  Glossary                        <- .tfw/glossary.md
  Compilable Contract             <- .tfw/compilable_contract.md
  Changelog                       <- .tfw/CHANGELOG.md
  Release                         <- RELEASE.md
  Workflows/                      <- .tfw/workflows/**/*.md
  Templates/                      <- .tfw/templates/**/*.md
Tasks/
  {task folders with all artifacts} <- every task container (preserved structure)
```
