# HL — TFW-27 / Phase C: Deploy to GitHub Pages

> **Date**: 2026-04-08
> **Author**: Coordinator
> **Status**: ✅ Approved
> **Parent HL**: [HL-TFW-27](../HL-TFW-27__wiki_polish_and_brand.md)

---

## 1. Vision

The TFW documentation site is fully built and tested locally but has no public presence. Phase C deploys it to GitHub Pages via a GitHub Actions workflow. After this phase, every push to `main` automatically rebuilds and publishes the docs. TFW-28 (Deploy docs) is absorbed into this phase.

**Impact:** TFW becomes a publicly accessible, auto-deploying documentation site.

## 2. Current State (As-Is)

| Aspect | Current State |
|--------|---------------|
| Docs site | Builds locally with `mkdocs build -f docs/mkdocs.yml`. Not deployed |
| GitHub Pages | Not configured |
| CI/CD | None |
| site_url | Empty string in mkdocs.yml |

## 3. Target State (To-Be)

| Aspect | To-Be |
|--------|-------|
| Docs site | Live at GitHub Pages URL |
| GitHub Pages | Enabled, serves from `gh-pages` branch |
| CI/CD | GitHub Actions workflow: on push to main → build → deploy |
| site_url | Set to actual GitHub Pages URL |

### 3.1 Result Visualization

```
Push to main
    │
    ▼
GitHub Actions (.github/workflows/docs.yml)
    │
    ├── checkout
    ├── setup python
    ├── pip install -r docs/requirements.txt
    ├── mkdocs build -f docs/mkdocs.yml
    └── deploy → gh-pages branch
              │
              ▼
        GitHub Pages serves site
```

## 4. Deliverables

| # | File | Action |
|---|------|--------|
| 1 | `.github/workflows/docs.yml` | NEW — GitHub Actions workflow |
| 2 | `docs/mkdocs.yml` | MODIFY — fill `site_url`, `repo_url` |

## 5. Definition of Done

- ✅ 1. GitHub Actions workflow exists and runs on push to main
- ✅ 2. `site_url` and `repo_url` filled in mkdocs.yml
- ✅ 3. Site is accessible at GitHub Pages URL
- ✅ 4. Docs content renders correctly (logo, nav, links)

## 6. Principles

1. **Standard tooling** — use official `mkdocs gh-deploy` or `actions/deploy-pages` pattern
2. **Zero manual steps** — push to main = site updates automatically

---

*HL — TFW-27 / Phase C: Deploy to GitHub Pages | 2026-04-08*
