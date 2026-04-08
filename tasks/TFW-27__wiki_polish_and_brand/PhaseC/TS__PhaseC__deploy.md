# TS — TFW-27 / Phase C: Deploy to GitHub Pages

> **Date**: 2026-04-08
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL__PhaseC__deploy.md](HL__PhaseC__deploy.md)

---

## 1. Objective

Deploy TFW documentation to GitHub Pages using GitHub Actions. Auto-deploy on push to main.

## 2. Scope

### In Scope
- `.github/workflows/docs.yml` — GitHub Actions workflow
- `docs/mkdocs.yml` — fill `site_url`, `repo_url`

### Out of Scope
- Custom domain (future)
- SEO meta tags (future — depends on live URL)
- Analytics

## 3. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.github/workflows/docs.yml` | NEW | GitHub Actions workflow for MkDocs deploy |
| `docs/mkdocs.yml` | MODIFY | Set `site_url` and `repo_url` |

## 4. Detailed Steps

### Step 1: Create GitHub Actions workflow

`.github/workflows/docs.yml`:

```yaml
name: Deploy Docs

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
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install -r docs/requirements.txt

      - name: Build docs
        run: python -m mkdocs build -f docs/mkdocs.yml

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: site/

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### Step 2: Update mkdocs.yml

```yaml
site_url: "https://saubakirov.github.io/trace-first-starter/"
repo_url: "https://github.com/saubakirov/trace-first-starter"
```

### Step 3: Enable GitHub Pages

In GitHub repo → Settings → Pages → Source: GitHub Actions.

### Step 4: Push and verify

1. Commit both files
2. Push to main
3. Check Actions tab — workflow runs
4. Visit site URL — docs render correctly

## 5. Acceptance Criteria

- [ ] `.github/workflows/docs.yml` exists
- [ ] `site_url` and `repo_url` are set in mkdocs.yml
- [ ] GitHub Actions workflow runs successfully on push
- [ ] Site is accessible at GitHub Pages URL
- [ ] Logo, navigation, links work on live site

---

*TS — TFW-27 / Phase C: Deploy to GitHub Pages | 2026-04-08*
