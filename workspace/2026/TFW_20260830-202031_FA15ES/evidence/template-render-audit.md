# Template render audit — TFW_20260830-202031_FA15ES

> Date: 2026-09-02
> Product commit: `626d77b5c3261dff493d15c7ce5862b9e036d10e`
> Render source: external standalone fixture `E:\TEMP\tfw-fa15es-final-626d77b-qa`

## Render procedure

1. Executed the standalone copy's `шаблоны/build_a4.py` against its complete `документ_A4.md`; the builder returned `pages: 4`.
2. Served only the external fixture on `127.0.0.1` and opened both generated A4 HTML and the standalone presentation in the in-app browser.
3. Inspected the visible DOM, every page/slide in full-page screenshots, computed layout dimensions, image natural dimensions, and console warnings/errors.
4. Calculated WCAG relative luminance for every foreground/background pair used by the changed neutral palette. Gradient cases use the worst contrast across all declared stops; translucent foregrounds/backgrounds are composited before calculation.

PNG was selected as the representative render format permitted by the TS's `PDF/PNG` evidence requirement. The generated HTML remains print-configured for the documented browser “Save as PDF” path.

## Completeness and asset checks

| Artifact | Structural observation | Asset observation | Console | Result |
|---|---|---|---|---|
| A4 document | 4/4 `.page` containers; 0 descendant clipping offenders; document width equals viewport content width | 1/1 `assets/tfw-mark.svg`, natural size 96×96 | 0 warnings/errors | PASS |
| presentation | 4/4 `.slide` containers; each 960×540 with `scrollWidth=clientWidth` and `scrollHeight=clientHeight` | 4/4 passive marks, each natural size 96×96 | 0 warnings/errors | PASS |

Visual inspection found no truncated title, body, table, list, note, code fragment, footer, or slide content. The A4 output preserves the complete worked title/instructions, three content sections, two tables, callout, and footer. The presentation preserves title, comparison, table, and editing-guidance slides. The note and work-plan Markdown retain their complete worked structures by the immutable-source diff audit.

The only retained mark is the exact 270-byte `tfw-mark.svg`. No raster company logo, field palette, overlay, or theme CSS is required.

## Contrast calculations

Ordinary text threshold: **4.5:1**. Large bold text threshold: **3.0:1**.

| Rendered pair / worst case | Ratio | Threshold | Result |
|---|---:|---:|---|
| A4 muted metadata `#52606D` / white | 6.46:1 | 4.5:1 | PASS |
| A4 blue heading `#334E68` / white | 8.64:1 | 4.5:1 | PASS |
| A4 primary heading `#243B53` / white | 11.50:1 | 4.5:1 | PASS |
| A4 body `#1F2933` / white | 14.76:1 | 4.5:1 | PASS |
| A4 body / translucent neutral quote | 12.76:1 | 4.5:1 | PASS |
| A4 body / `#F0F4F8` | 13.35:1 | 4.5:1 | PASS |
| A4 table text `#111111` / `#D9E2EC` | 14.42:1 | 4.5:1 | PASS |
| presentation muted `#555555` / white | 7.46:1 | 4.5:1 | PASS |
| presentation heading `#243B53` / white | 11.50:1 | 4.5:1 | PASS |
| white act label / `#243B53` or `#334E68` | 8.64:1 | 4.5:1 | PASS |
| light-box heading / worst neutral tint | 9.81:1 | 4.5:1 | PASS |
| light-box body / worst neutral tint | 10.77:1 | 4.5:1 | PASS |
| table/quote text `#111111` / `#D9E2EC` | 14.42:1 | 4.5:1 | PASS |
| title-slide 85%-white ordinary text / worst gradient stop | 4.94:1 | 4.5:1 | PASS |
| pause-slide 78%-white ordinary text / worst gradient stop | 6.01:1 | 4.5:1 | PASS |
| pause-slide white body / green tint | 6.61:1 | 4.5:1 | PASS |
| pause-slide white body / red tint | 7.71:1 | 4.5:1 | PASS |
| pause-slide white code / neutral tint | 5.87:1 | 4.5:1 | PASS |
| pause-slide green 19px bold heading / green tint | 4.36:1 | 3.0:1 | PASS |
| pause-slide red 19px bold heading / red tint | 3.76:1 | 3.0:1 | PASS |

The small slide indices are ancillary positional markers rather than ordinary content: `#A8A8B4` on white is 2.35:1 and 55%-white on the dark gradient is at least 3.87:1. They retain exact field styling outside the neutralization hunks and are classified under the WCAG 1.4.3 incidental-text exception. All semantic headings, prose, list items, table cells, callouts, instructions, and code fragments satisfy their applicable threshold.

Reproduce calculations:

```powershell
python workspace/2026/TFW_20260830-202031_FA15ES/evidence/attachments/contrast_audit.py
```

Expected terminal line: `CONTENT_CONTRAST=PASS`.

## Render attachments

| File | Bytes | SHA-256 | Coverage |
|---|---:|---|---|
| [a4-full.png](renders/a4-full.png) | 234,505 | `daf2918364d02ed10f3d33d8972816156e13e2f5905be9fdd966d53b45e4b875` | all 4 A4 page containers |
| [presentation-full.png](renders/presentation-full.png) | 216,939 | `e63dcc9c01642c9ef0a2a955026a243a4a5dca6122a4b790158859ccaeadb02d` | all 4 slides |

Render verdict: **PASS**.
