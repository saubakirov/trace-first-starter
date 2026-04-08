# ONB — TFW-27 / Phase A: Brand Identity & Logo

> **Date**: 2026-04-08
> **Author**: Executor
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL__PhaseA__brand_identity.md](HL__PhaseA__brand_identity.md)
> **TS**: [TS__PhaseA__brand_identity.md](TS__PhaseA__brand_identity.md)

---

## 1. Understanding

Phase A establishes TFW's visual identity: a monogram logo (TFW as continuous routed line with checkpoint nodes), charcoal + calm teal palette, Inter/JetBrains Mono typography, a brand guidelines document at `docs/brand/identity.md`, and applying all of this to mkdocs.yml + custom CSS. Additionally, the README.md hero section gets rewritten with an English vision statement. The goal is to transform TFW's docs site from a generic default-indigo MkDocs project into a professional, recognizable methodology product.

## 2. Entry Points

| File | Current State | Action |
|------|--------------|--------|
| `docs/mkdocs.yml` | 65 lines, default indigo palette, `site_name: "My Project Docs"`, no logo/favicon/font/custom_dir | MODIFY — full theme config |
| `README.md` | 141 lines, utilitarian hero (lines 1-7) | MODIFY — replace hero section |
| `docs/brand/identity.md` | Does not exist | CREATE — brand guidelines |
| `docs/brand/logo.svg` | Does not exist | CREATE — monogram logo |
| `docs/brand/favicon.png` | Does not exist | CREATE — 32×32 favicon |
| `docs/overrides/stylesheets/extra.css` | Does not exist | CREATE — custom CSS |
| Reference images | `tasks/TFW-27.../2026-04-08_13-26.png` (concept 1), `2026-04-08_13-28.png` (concept 3 "TFW Monogram") | Input for logo generation |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | **Logo format: SVG vs PNG.** The image generation tool outputs raster images (PNG), not vector SVG. TS Step 2 specifies "SVG (or high-quality PNG to be traced to SVG)". Should I: (a) generate a high-quality PNG and use it directly as the logo (Material theme accepts PNG), or (b) generate a PNG and manually hand-craft an SVG monogram based on the concept? Option (b) gives a true vector, but the monogram is complex enough that an SVG hand-trace would be approximate. | **(a) PNG is fine.** Use a high-quality PNG directly. Material renders PNG logos perfectly. A vector version can be a future deliverable. Name the file `logo.png` (not `.svg`) and update mkdocs.yml config accordingly. |
| 2 | **Which reference concept to follow?** Image 1 (`13-26.png`) shows a cleaner monogram with lighter strokes. Image 2 (`13-28.png`, "Концепция 3 — TFW MONOGRAM") shows a bolder, more stylized version with thicker strokes and circuit-board feel. Which direction is preferred for the logo generation prompt? | **Concept 2 (13-28.png)** — the bolder monogram with thicker strokes. It reads better at small sizes and has more character. Use it as primary input to the generation tool. |
| 3 | **README hero replacement range.** TS says "Replace lines 1-8 of README.md". The current README lines 1-7 are: `# Trace-First Workflow (TFW) — Canonical Starter` + blank + `> *"The thought process..."*` + blank + paragraph + blank + `For the full philosophy...`. Line 8 is `---`. Should the replacement include the `---` (line 9) or stop before it? The TS hero text doesn't end with `---`. I'll assume: replace lines 1-7 with the new hero, keep `---` at line 8 as section separator. Correct? | **Correct.** Replace lines 1-7 (everything above the first `---`). Keep the `---` separator. The new hero text should NOT include a trailing `---` — the existing one stays. |

## 4. Recommendations (suggestions, not blocking)

1. **Use PNG for logo + favicon directly.** MkDocs Material renders both PNG and SVG logos. Since the image generation tool produces PNG, using a high-quality PNG (~512px or larger) avoids a lossy SVG tracing step. The brand guidelines can note that a vector version is a future deliverable.

2. **Add `site_url` and `repo_url` to mkdocs.yml.** The TS scope covers `site_name` and `site_description`, but the current mkdocs.yml has empty `site_url` and `repo_url`. Setting `repo_url: "https://github.com/saubakirov/trace-first-starter"` would add the GitHub corner link in the docs header — free value. This is technically outside TS scope, so I'll note it but skip unless approved.

3. **Logo text treatment.** The reference images show "TRACE FIRST" in dark + "WORKFLOW" in teal below the monogram. The TS specifies Inter 600 weight, letter-spacing 0.15em, uppercase for logo text. For the docs site header, Material supports only a small logo image (no text next to it in the header). The full mark + text would go in README.md only. The docs header gets the mark-only version (per HL §3.1 Context A).

## 5. Risks Found (edge cases, potential issues not in TS)

1. **`custom_dir: overrides` path resolution.** MkDocs Material `custom_dir` is relative to `mkdocs.yml`. Since `mkdocs.yml` is at `docs/mkdocs.yml` and `docs_dir: .` means docs root = `docs/`, the overrides directory needs to be at `docs/overrides/`. This matches the TS path `docs/overrides/stylesheets/extra.css`. Verified — no issue, just confirming the path chain.

2. **`extra_css` path resolution.** In mkdocs.yml, `extra_css` paths are relative to `docs_dir` (which is `.`, meaning `docs/`). So `extra_css: [overrides/stylesheets/extra.css]` should resolve correctly to `docs/overrides/stylesheets/extra.css`. Verified.

3. **Brand assets path in Material theme.** `theme.logo` and `theme.favicon` paths are relative to `docs_dir`. So `logo: brand/logo.svg` → `docs/brand/logo.svg`. If we use PNG instead, path becomes `brand/logo.png`. Need to match file extension to config.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS Step 5 says `docs/mkdocs.yml`** — correctly pointing to the actual file path. No inconsistency.

2. **TS §3 Affected Files says `docs/mkdocs.yml`** — refers to MODIFY action. Current `mkdocs.yml` has `docs_dir: .` (line 4) and `site_dir: ../site` (line 5), meaning the build output goes to `site/` at project root. These are not being changed by TS (correct — out of scope).

3. **TS Step 6 says "Replace lines 1-8"** but README has content on lines 1-7 with line 8 being blank and line 9 being `---`. Minor mismatch — the intent is clear (replace the hero section above the first `---`).

---

*ONB — TFW-27 / Phase A: Brand Identity & Logo | 2026-04-08*
