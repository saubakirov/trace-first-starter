# HL — TFW-27 / Phase A: Brand Identity & Logo

> **Date**: 2026-04-08
> **Author**: Coordinator
> **Status**: ✅ Approved
> **Parent HL**: [HL-TFW-27](../HL-TFW-27__wiki_polish_and_brand.md)

---

## 1. Vision

TFW's documentation site and GitHub repository currently look like a generic MkDocs project. There's no visual identity — no logo, no palette, no typography, no brand voice expressed visually. A visitor sees the default indigo Material theme and a utilitarian README. Nothing signals that this is a coherent methodology product with a clear philosophy.

Phase A establishes TFW's brand identity from the ground up: a monogram logo (TFW as a single continuous workflow path with checkpoint nodes), a disciplined color palette (charcoal + calm teal), professional typography, and a brand guidelines document. It also rewrites the README hero section with a vision statement that communicates TFW's core value proposition — structured self-knowledge for products.

**Impact:** After Phase A, TFW has a distinctive, recognizable visual identity that expresses its philosophy: precise, methodical, engineering-grade. The README opens with a compelling vision statement instead of a bare heading. The docs site looks like a professional product, not a side project.

> "I opened the repo and immediately understood what TFW is about. The logo, the colors, the opening text — it all said the same thing: this is a serious, thoughtful methodology. It felt like something I could trust with my project's memory."

## 2. Current State (As-Is)

| Aspect | Current State |
|--------|---------------|
| Logo | None |
| Color palette | MkDocs Material default (indigo) |
| Typography | Browser defaults |
| Brand voice | Exists in `.tfw/README.md` — "Traces Over Code" — but not visually expressed |
| Favicon | None |
| README hero | Utilitarian heading + one-line quote. No vision statement, no value proposition |
| Brand guidelines | None |

## 3. Target State (To-Be)

| Aspect | To-Be |
|--------|-------|
| Logo | SVG monogram: letters TFW formed by a single continuous routed line with 2-3 checkpoint nodes. Two-color: dark base + calm teal accent on white. Context-dependent: mark-only in docs header, mark + "TRACE FIRST WORKFLOW" in README |
| Color palette | Base: charcoal (#1a1a2e) / white (#ffffff). Primary accent: calm teal (~#0d9488). Secondary accent: warm amber (trace/history marker, sparingly). Dark mode variants defined |
| Typography | Heading + body: Inter (Google Font). Code: JetBrains Mono or Roboto Mono. Clean, geometric, engineering feel |
| Favicon | Derived from logo mark, 32×32 PNG, recognizable at small size |
| README hero | English vision statement: structured self-knowledge for products. Translated/adapted from brand positioning. Replaces current heading + quote |
| Brand guidelines | `docs/brand/identity.md` — logo usage, palette, typography, voice, character |
| mkdocs.yml | site_name, site_description, theme palette, font, logo, favicon, custom_dir, extra_css |

### 3.1 Result Visualization

**Logo concept (monogram, two-color, white background):**

```
     ┌──●──┐
     │     │
─────┤  F  ├──W──●
     │     │    /
T────┘     └───●

● = checkpoint nodes (teal accent)
— = continuous path line (charcoal)

Context A (docs header):   [TFW mark]
Context B (README):        [TFW mark] + TRACE FIRST WORKFLOW
Context C (favicon):       [TFW mark] simplified at 32px
```

**README hero section (To-Be):**

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  [TFW Logo]                                         │
│                                                     │
│  Trace-First Workflow                               │
│                                                     │
│  Imagine a product that knows more about itself     │
│  than just its code structure and file layout.      │
│                                                     │
│  It knows its purpose...                            │
│  It knows which decisions were made...              │
│  It knows its history, limitations, and debt.       │
│                                                     │
│  TFW preserves not just the implementation,         │
│  but the meaning.                                   │
│                                                     │
│  Because knowledge is power.                        │
│                                                     │
│  ── Quick Start ──                                  │
│  ── What's Inside ──                                │
│  ── Task Board ──                                   │
└─────────────────────────────────────────────────────┘
```

**MkDocs site with brand applied:**

```
┌──────────────────────────────────────────────────────┐
│ [TFW●] Trace-First Workflow      🔍 Search     🌙/☀  │
│ ─── teal accent bar ────────────────────────────────  │
├──────────┬───────────────────────────────────────────┤
│ Nav      │                                           │
│ (Inter)  │   Content area                            │
│          │   Inter font, charcoal text               │
│          │   Teal links                              │
│          │   Code blocks: JetBrains Mono             │
│          │                                           │
└──────────┴───────────────────────────────────────────┘
```

**Color palette:**

```
Base:       ███ #1a1a2e (charcoal)     ███ #ffffff (white)
Accent:     ███ ~#0d9488 (calm teal)   ███ ~#0f766e (teal dark mode)
Secondary:  ███ ~#d97706 (amber)       — used sparingly for "trace" markers
Surface:    ███ #f8fafc (light bg)     ███ #1e1e2e (dark bg)
```

## 4. Deliverables

1. **Brand DNA document** (`docs/brand/identity.md`): logo usage rules, palette with hex values, typography spec, brand character/voice, positioning formula
2. **Logo SVG** (`docs/brand/logo.svg`): monogram mark, two-color, scalable
3. **Favicon** (`docs/brand/favicon.png`): 32×32 derived from logo
4. **Custom CSS** (`docs/overrides/stylesheets/extra.css`): Google Font import, color variables, typography refinements
5. **mkdocs.yml updates**: site_name, site_description, theme config (palette, font, logo, favicon, custom_dir)
6. **README hero text**: English vision statement inserted at top of README.md

## 5. Brand DNA (source material)

### Essence
TFW — a way to make projects meaningful, resumable, and self-aware.

### Core idea
A product should know not just what's in it, but why, how, and what was rejected. The trace is more valuable than the immediate result.

### Brand promise
Any project can be resumed without loss of meaning.

### Brand character
Calm, intelligent, disciplined, strict, engineering-grade, adult, slightly doctrinal. Not a toy, not startup noise — a protocol you can trust with your product's evolution.

### Archetype
Architect × Guardian × Strategist — builds structure, preserves memory, holds direction.

### Positioning
- TFW — structured self-knowledge for products
- TFW — where product memory becomes a system
- Formula: Knowledge → Continuity → Power

### Values (6)
1. **Trace over output** — the decision trail matters more than the deliverable
2. **Meaning over mechanics** — not just how, but why
3. **Continuity over chat** — session ≠ memory boundary
4. **Candor over charm** — precise, not flattering
5. **One truth, many tools** — `.tfw/` as single source, adapters for each tool
6. **Portability over lock-in** — knowledge belongs to the user, not the platform

## 6. Definition of Done (DoD)

- ✅ 1. Logo SVG exists at `docs/brand/logo.svg`, two-color monogram, renders in docs header
- ✅ 2. Favicon renders in browser tab
- ✅ 3. Color palette applied to mkdocs.yml — site no longer uses default indigo
- ✅ 4. Typography uses Inter (not browser defaults)
- ✅ 5. Dark mode toggle works with custom palette
- ✅ 6. Brand guidelines documented in `docs/brand/identity.md` with DNA, palette, typography, logo usage
- ✅ 7. README.md hero section rewritten with English vision statement
- ✅ 8. `mkdocs build` passes without errors
- ✅ 9. Site visually expresses TFW character: precise, methodical, engineering-grade, calm

## 7. Definition of Failure (DoF)

- ❌ 1. Logo looks generic or clip-art — must be distinctive monogram
- ❌ 2. Colors feel like default Material theme (indigo/purple)
- ❌ 3. README hero text reads like documentation, not vision
- ❌ 4. Brand guidelines are just a color list without character/voice/usage rules

## 8. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Generated logo doesn't match monogram concept | Medium | Medium | Iterate with user, use reference PNGs as input to generation |
| Teal palette too close to generic "tech" look | Low | Medium | Use specific hex values, test against competitor sites |
| README hero text too long/preachy | Low | Medium | Keep to ~10 lines, user reviews before merge |
| MkDocs Material custom_dir breaks on upgrade | Low | Medium | Use documented extension points only |

## 9. Principles

1. **Brand = philosophy made visible** — every visual choice must express TFW values (P3 from master HL)
2. **Two-color discipline** — charcoal + teal. Amber sparingly. No gradients, no decorative elements
3. **Context-dependent assets** — logo mark adapts to context (header, README, favicon) but stays recognizable
4. **Insert, don't duplicate** — README hero text goes directly into README.md, not a separate file

## 10. RESEARCH Case

> No separate RESEARCH needed for Phase A. Brand DNA is defined by user input (ChatGPT-assisted brand session). Logo direction is clear (monogram with checkpoints). Color/typography are specific.
> Remaining unknowns are implementation-level (exact hex values, CSS specifics) — those belong in execution, not research.

## 11. Strategic Session Insights

> **Human-Only Test:** Would this insight be unknown without the user saying it?

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | Logo = two-color monogram on white, letters TFW as single continuous routed line with checkpoint nodes. Like a signature, not a pictogram | convention | User, Q1 answer + ChatGPT concept |
| S2 | Text under logo is context-dependent: mark-only in docs header, mark + full name in README | convention | User, Q2 answer |
| S3 | Accent color = calm teal, not electric cyan. "Который более спокойный" — the calmer variant wins | stakeholder | User, Q5 answer |
| S4 | README hero text inspired by Russian vision text: products that know about themselves (purpose, decisions, history, debt, meaning). English only | philosophy | User, hero text draft |
| S5 | Brand character: protocol-grade, not startup-grade. Calm, disciplined, engineering, slightly doctrinal. "Not a toy, not noise" | philosophy | User via ChatGPT brand session |
| S6 | Brand formula: Knowledge → Continuity → Power. TFW = structured self-knowledge for products | philosophy | User via ChatGPT positioning |
| S7 | Tagline = "The thinking is the product. Everything else is output." — chosen over "path > destination" variants (rejected as "samurai cliché"). Expresses that reasoning is the irreplaceable asset | philosophy | User, tagline selection session |
| S8 | Secondary motto = "The trace is the product." — used as inline brand anchor near philosophy link | convention | User, approved from option B |
| S9 | README "Who This Is For" must lead with business/operations, not engineering. "TFW is not about code. It's about making decisions visible and knowledge permanent." Business value > technical value in positioning | stakeholder | User: «бизнес валью важнее. Мы отличаемся тем, что думаем не про технику, а про валью» |

---

*HL — TFW-27 / Phase A: Brand Identity & Logo | 2026-04-08*
