# Briefing
> Parent: [HL-TFW-26](../HL-TFW-26__documentation_site.md)
> Goal: Enable TFW projects to mechanically compile their structured artifacts into a publishable documentation site — deterministic, scriptable, no agent involvement in compilation.

## Research Plan

### Gather (3-5 bullets)
- Survey SSG landscape: MkDocs (Material), Jekyll (Just-the-Docs), Hugo, Docusaurus, Astro Starlight — evaluate native multi-source compilation, frontmatter injection, plugin systems
- Research ADR/knowledge-as-docs tooling: adr-tools, log4brains, backstage TechDocs — do any compile structured artifacts (not just render md)?
- Investigate GitHub Pages + GitLab Pages compatibility: shared config format? CI/CD requirements vs local-only?
- Study "docs-from-code" and "docs-from-artifacts" patterns in industry: Diátaxis, Divio, Stripe's docs approach
- Evaluate custom lightweight utilities: Python script, bash, or tool-specific config — what's the minimum viable approach?

### Extract (3-5 bullets)
- Audit current TFW artifact structure: map all files, cross-references, link formats, naming conventions
- Attempt manual compilation of KNOWLEDGE.md + knowledge/*.md into a docs structure with the most promising SSG
- Define the "compilable contract": exact structure each artifact type must have for deterministic compilation
- Analyze the source→output mapping from HL §3.1 — validate each mapping is achievable with the chosen tool
- Identify traceability gaps: broken links, inconsistent cross-references, missing backlinks

### Challenge (3-5 bullets)
- Stress-test the two-layer split: is "agent maintains, utility compiles" the right boundary? Or should the utility also validate/lint?
- Challenge H3 (<100 LOC): is this realistic or aspirational? What's the real complexity?
- Counter-evidence for "found tool": is TFW's structure unique enough that no existing SSG fits without heavy customization?
- Test the "progressive enhancement" claim: does README-only → minimal docs actually work, or does it degrade?
- Challenge docs/ at project root: git pollution, .gitignore concerns, build artifact vs source distinction

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | A simple copy + frontmatter injection is sufficient for most artifacts (no content transformation) | open |
| H2 | An existing tool (MkDocs / Jekyll / Hugo) can be configured to read TFW artifact structure directly | open |
| H3 | A lightweight Python/bash script (<100 LOC) can handle the compilation step | open |
| H4 | The same `docs/` output works for both GitHub Pages and GitLab Pages | open |
| H5 | `docs/` at project root (alongside tasks/, knowledge/) is the right location | open |
| H6 | Current TFW artifact structure is already sufficient for compilation — only a formal "compilable contract" is missing, not structural changes | open |
| H7 | The traceability gaps (facts without backlinks, principles without clickable sources) can be fixed by tightening existing workflow rules, not by adding new workflows | open |

## Scope Intent
- **In scope:** SSG evaluation, artifact structure audit, compilable contract definition, GitHub Pages/GitLab Pages compatibility, source→output mapping validation, tooling recommendation
- **Out of scope:** MCP server for queries, full-text search, multi-repo aggregation, CI/CD pipeline implementation (only feasibility), curated landing page content

## Guiding Questions
1. Does the starter repo (tfw.saubakirov.kz) currently use GitHub Pages? If so, what's the current deployment setup — custom domain, which branch/folder serves the site?
2. Is there a strong preference for Python-based tooling (MkDocs) over Ruby (Jekyll) or Go (Hugo) — considering the project's existing tech stack?
3. The HL mentions "platform portable" (GitHub Pages + GitLab Pages). Is GitLab Pages a real requirement or a nice-to-have? Does any TFW consumer project actually use GitLab?

## User Direction
1. **GitHub Pages**: Yes, tfw.saubakirov.kz serves from GitHub Pages, from root of the repo (main branch root). This means `docs/` folder approach would require reconfiguring to serve from `docs/` instead of root, OR the compiled output replaces root-level files.
2. **Tooling**: No preference — Python/Ruby/Go/anything. Must satisfy requirements. Decision is purely technical.
3. **GitLab Pages**: Nice-to-have, not blocking. Innoforce uses GitLab internally, so real use case exists. Design for GitHub Pages first, ensure GitLab compatibility is achievable.

---
Stage complete: YES
