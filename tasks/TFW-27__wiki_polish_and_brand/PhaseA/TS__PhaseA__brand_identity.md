# TS — TFW-27 / Phase A: Brand Identity & Logo

> **Date**: 2026-04-08
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL__PhaseA__brand_identity.md](HL__PhaseA__brand_identity.md)

---

## 1. Objective

Establish TFW's visual identity (logo, palette, typography, brand guidelines) and apply it to the docs site theme and README hero section. After this phase, TFW looks like a professional methodology product, not a default MkDocs project.

## 2. Scope

### In Scope
- Brand guidelines document with DNA, character, values, logo usage, palette, typography
- TFW monogram logo (SVG) — two-color (charcoal + teal), continuous line with checkpoint nodes
- Favicon (PNG 32×32) derived from logo
- Custom CSS: Google Font (Inter), color variables, typography refinements
- mkdocs.yml: site_name, site_description, theme palette, font, logo, favicon, custom_dir
- README.md hero section: English vision statement (adapted from user's Russian draft)

### Out of Scope
- gen_docs.py changes (Phase B)
- Link resolution, dynamic nav (Phase B)
- docs/index.md landing page redesign (Phase C)
- Deployment (TFW-28)
- README structure below the hero section (Phase C)

## 3. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `docs/brand/identity.md` | CREATE | Brand guidelines: DNA, character, values, palette hex values, typography spec, logo usage rules |
| `docs/brand/logo.svg` | CREATE | TFW monogram — two-color SVG, viewBox-based |
| `docs/brand/favicon.png` | CREATE | 32×32 PNG favicon derived from logo mark |
| `docs/overrides/stylesheets/extra.css` | CREATE | Inter font import, heading typography, teal accent variables, link styling |
| `docs/mkdocs.yml` | MODIFY | site_name, site_description, theme.palette, theme.font, theme.logo, theme.favicon, custom_dir, extra_css |
| `README.md` | MODIFY | Replace hero section (lines 1-8) with logo + vision statement |

**Budget:** 4 new files, 2 modifications, 6 total. Limits: max 14 files, max 8 new, max 1200 LOC.

## 4. Detailed Steps

### Step 1: Create brand guidelines (`docs/brand/identity.md`)

Write the brand guidelines document containing:

**§1 Brand DNA**
- Essence: TFW = structured self-knowledge for products
- Promise: any project can be resumed without loss of meaning
- Formula: Knowledge → Continuity → Power

**§2 Character**
- Calm, intelligent, disciplined, engineering-grade, slightly doctrinal
- NOT: playful, startup-hype, AI-buddy, flashy

**§3 Values** (6 items from HL §5)

**§4 Logo**
- Monogram description: TFW letters as continuous routed line with checkpoint nodes
- Two-color: charcoal base + teal accent on checkpoints
- Usage contexts: mark-only (docs header, favicon), mark + "TRACE FIRST WORKFLOW" (README, landing)
- Minimum size: 16px for mark, 32px for mark + text
- Clear space: 1× mark height around logo
- DO NOT: rotate, stretch, change colors, add effects

**§5 Color Palette**
- Charcoal: `#1a1a2e` (primary text, logo base)
- White: `#ffffff` (light background)
- Calm teal: `#0d9488` (primary accent, links, checkpoints)
- Teal dark: `#0f766e` (dark mode accent)
- Amber: `#d97706` (secondary, trace markers — sparingly)
- Light surface: `#f8fafc`
- Dark surface: `#1e1e2e`

**§6 Typography**
- Headings & body: Inter (Google Fonts)
- Code: JetBrains Mono (or Roboto Mono fallback)
- Logo text: Inter 600 weight, letter-spacing 0.15em, uppercase

### Step 2: Generate logo SVG (`docs/brand/logo.svg`)

Generate the TFW monogram using the image generation tool:
- Input: reference PNGs from ChatGPT concepts as guidance
- Prompt direction: monogram where T, F, W are formed by a single continuous line with 2-3 dot checkpoints. Charcoal line (#1a1a2e) + teal dots (#0d9488). White background. Minimal, engineering feel
- Output: SVG (or high-quality PNG to be traced to SVG)
- Verify: renders at favicon scale (16-32px), works in dark/light modes

### Step 3: Generate favicon (`docs/brand/favicon.png`)

- Derive from logo mark
- 32×32 PNG
- Must be legible: simplified if needed (just the mark, no text)

### Step 4: Create custom CSS (`docs/overrides/stylesheets/extra.css`)

```css
/* TFW Brand Typography */
:root {
  --md-primary-fg-color: #0d9488;
  --md-accent-fg-color: #0d9488;
}

[data-md-color-scheme="slate"] {
  --md-primary-fg-color: #0f766e;
  --md-accent-fg-color: #14b8a6;
}

/* Heading refinements */
.md-typeset h1,
.md-typeset h2,
.md-typeset h3 {
  font-weight: 600;
  letter-spacing: -0.01em;
}

/* Link hover */
.md-typeset a:hover {
  color: #0f766e;
}
```

Note: exact CSS will be refined during execution based on Material theme variables.

### Step 5: Update mkdocs.yml

Apply the following changes to `docs/mkdocs.yml`:

```yaml
site_name: "Trace-First Workflow"
site_description: "A structured methodology where products preserve knowledge about themselves — purpose, decisions, history, and meaning."

theme:
  name: material
  custom_dir: overrides
  logo: brand/logo.svg
  favicon: brand/favicon.png
  font:
    text: Inter
    code: JetBrains Mono
  features:
    # ... existing features
  palette:
    - scheme: default
      primary: teal
      accent: teal
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: teal
      accent: teal
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

extra_css:
  - overrides/stylesheets/extra.css
```

Material's named `primary: teal` sets header color. Custom CSS fine-tunes specific hex values.

### Step 6: Rewrite README hero section

Replace lines 1-8 of `README.md` with:

```markdown
# Trace-First Workflow

> *Imagine a product that knows more about itself than just its code structure and file layout.*
>
> *It knows its purpose. It knows the value it delivers. It knows which decisions were made during its evolution, why they were made, and what they led to. It knows its history, limitations, weaknesses, and technical debt.*
>
> *Such a product knows not only what it contains, but how, why, and for what purpose each part exists.*
>
> *This is what sets TFW apart. Most approaches work with the technical layer — code, files, dependencies, current state. TFW preserves and structures not just the implementation, but the meaning.*
>
> *A product built on this methodology is better equipped to maintain itself, move toward its goals with precision, and reliably support business growth.*
>
> ***Because knowledge is power.***
```

Keep everything below (Who This Is For, Quick Start, etc.) unchanged.

### Step 7: Verify build

Run `mkdocs build` from `docs/` directory:
- Logo renders in header
- Favicon loads in browser tab
- Inter font renders (headings + body)
- Teal palette applied (not indigo)
- Light/dark mode toggle works
- No build errors

## 5. Acceptance Criteria

- [ ] Logo SVG at `docs/brand/logo.svg` — two-color monogram, renders in docs header
- [ ] Favicon at `docs/brand/favicon.png` — renders in browser tab
- [ ] Color palette applied — teal primary, not indigo
- [ ] Inter font renders in docs (headings + body text)
- [ ] Dark mode toggle works with teal palette
- [ ] `docs/brand/identity.md` contains full brand guidelines (DNA, character, values, palette, typography, logo usage)
- [ ] README.md hero section has English vision statement
- [ ] `mkdocs build` passes without errors

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Generated logo doesn't match monogram concept | Use reference PNGs as generation input, iterate with user |
| Material theme `custom_dir` path resolution | Use documented `overrides/` pattern from Material docs |
| Inter font CDN blocked in some environments | Material can download fonts locally; system fallback = sans-serif |
| Hero text too long for README opening | Cap at ~12 lines, user reviews before final |

---

*TS — TFW-27 / Phase A: Brand Identity & Logo | 2026-04-08*
