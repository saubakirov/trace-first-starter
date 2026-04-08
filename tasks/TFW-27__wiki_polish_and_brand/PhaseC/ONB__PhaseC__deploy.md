# ONB — TFW-27 / Phase C: Deploy to GitHub Pages

> **Date**: 2026-04-08
> **Author**: Executor
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL__PhaseC__deploy.md](HL__PhaseC__deploy.md)
> **TS**: [TS__PhaseC__deploy.md](TS__PhaseC__deploy.md)

---

## 1. Understanding

Phase C deploys the TFW documentation site to GitHub Pages using GitHub Actions. On every push to `main`, a CI workflow builds docs via `mkdocs build` and deploys the result to the `gh-pages` environment. TFW-28 (Deploy docs) has been absorbed into this phase. The task also requires filling `site_url` and `repo_url` in `docs/mkdocs.yml`.

## 2. Entry Points

| File | Current State |
|------|--------------|
| `.github/workflows/docs.yml` | **Already exists** — 46 lines, functionally identical to TS spec |
| `docs/mkdocs.yml` | `site_url: ""`, `repo_url: ""` — need to be filled |
| `docs/requirements.txt` | Complete, 7 packages |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | `.github/workflows/docs.yml` already exists and is functionally identical to what the TS specifies. The only difference: the existing file uses `cancel-in-progress: true` while the TS has `false`, and the TS uses `python -m mkdocs build` vs `mkdocs build`. Should I: (a) leave the existing file as-is, (b) overwrite with the TS version exactly, or (c) keep the existing file and just apply the two minor TS differences? | **(a) Leave as-is.** Existing file is production-ready. Both Rec 1 and Rec 2 are correct — `cancel-in-progress: true` is better, `mkdocs build` is more conventional. No changes needed. |
| 2 | Step 3 says "In GitHub repo → Settings → Pages → Source: GitHub Actions." This is a manual step in the GitHub UI. Has this already been done? If not, shall I proceed with all other steps and leave this as a manual verification item for you? | **Already done.** GitHub Pages enabled with custom domain `tfw.saubakirov.kz`. Use `site_url: "https://tfw.saubakirov.kz/"` in mkdocs.yml (not the default `github.io` URL). |

## 4. Recommendations (suggestions, not blocking)

1. The existing `docs.yml` uses `cancel-in-progress: true` which is arguably better for docs deploys — cancelling a stale build when a newer push arrives saves CI minutes. The TS specifies `false`. I recommend keeping `true`.
2. `mkdocs build --config-file docs/mkdocs.yml` (existing) vs `python -m mkdocs build -f docs/mkdocs.yml` (TS) — both are equivalent. The existing form is more conventional. I recommend keeping the existing form.
3. In summary: the existing `docs.yml` is already production-ready. The real work in this phase is filling `site_url`/`repo_url` in mkdocs.yml and the manual GitHub Pages enablement.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **`site_dir` mismatch**: `docs/mkdocs.yml` has `site_dir: ../site` (relative to `docs/`), meaning the build output goes to `<repo>/site/`. The workflow uploads from `path: site/` — this matches. No issue.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS says "Create GitHub Actions workflow" (Step 1)** — but `.github/workflows/docs.yml` already exists with nearly identical content. This was likely written before the previous conversation created the file.

---

*ONB — TFW-27 / Phase C: Deploy to GitHub Pages | 2026-04-08*
