# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> Goal: Restore the field-proven Assisted 1.6 behavior as a neutral standalone edition through bounded, fully classified edits.

## Configuration Space

| Config | D1 — path disposition | D2 — source-text treatment | D3 — field provenance | D4 — public neutralization | D5 — old/new container references |
|--------|-----------------------|----------------------------|-----------------------|----------------------------|------------------------------------|
| C1 | preserve at same path | byte-exact | retain literally | direct names/logo only | historical source path only |
| C2 | preserve at same path | bounded source-line edit | retain as explicitly historical | identifying examples too | explicit old-source → new-target mapping |
| C3 | relocate/adapt | bounded source-line edit | retain as explicitly historical | identifying examples too | explicit old-source → new-target mapping |
| C4 | relocate/adapt | replace contiguous block | sanitize locator/fact, keep milestone | company palette too | explicit old-source → new-target mapping |
| C5 | exclude/delete | whole-file replacement | omit milestone | replace whole template | global token replacement |
| C6 | retain current-only | byte-exact | not applicable | direct names/logo only | current public path only |
| C7 | exclude/delete | not applicable | sanitize locator/fact, keep milestone | direct names/logo only | current public path only |
| C8 | preserve at same path | bounded source-line edit | sanitize locator/fact, keep milestone | company palette too | current public path only |

The selected ledger is deliberately mixed rather than one configuration for all paths: C1 for six exact files, C2/C3/C4/C8 for bounded adaptations, C5/C7 for private or rejected paths, and C6 for the neutral public mark. This combination was not explicit in the Briefing because the palette and historical-container cases only became visible after line inspection.

## Findings

### E1: Complete 35-path disposition ledger

`SHA` is the immutable field-source SHA-256 prefix for non-private source rows; full hashes were computed in the read-only inspection and are recoverable by re-running it. Private-record rows intentionally expose only file identity, category, and exclusion reason. No private record body or per-record metadata was copied into this artifact.

| # | Basis | Source/current path | Bytes / SHA | Disposition | Resulting path | Reason |
|---:|---|---|---|---|---|---|
| 1 | source | `.agents/skills/tfw-handoff/agents/openai.yaml` | 378 / `0516336e97d6` | preserve byte-exact | same | generic metadata |
| 2 | source | `.agents/skills/tfw-handoff/SKILL.md` | 11,114 / `ee4c703bee29` | bounded adapt | same | `work/` → `workspace/`; algorithm otherwise unchanged |
| 3 | source | `.agents/skills/tfw-identity/agents/openai.yaml` | 547 / `cd2acda1961b` | preserve byte-exact | same | generic prompt-only metadata |
| 4 | source | `.agents/skills/tfw-identity/SKILL.md` | 18,464 / `5e0723a44333` | bounded adapt | same | `team/`, provider-neutral sync wording, isolated canonical binding path |
| 5 | source | `.agents/skills/tfw-plan/agents/openai.yaml` | 330 / `9d1f968f1eae` | preserve byte-exact | same | generic metadata |
| 6 | source | `.agents/skills/tfw-plan/SKILL.md` | 12,994 / `b5e0b78448ca` | bounded adapt | same | `work/` → `workspace/`; algorithm otherwise unchanged |
| 7 | source | `.agents/skills/tfw-review/agents/openai.yaml` | 344 / `a7db8ffe61ad` | preserve byte-exact | same | generic metadata |
| 8 | source | `.agents/skills/tfw-review/SKILL.md` | 10,643 / `c56e0089282a` | bounded adapt | same | `work/` → `workspace/`; algorithm otherwise unchanged |
| 9 | source | `.agents/skills/tfw-update/agents/openai.yaml` | 454 / `f17f189f8fac` | preserve byte-exact | same | generic metadata |
| 10 | source | `.agents/skills/tfw-update/SKILL.md` | 22,251 / `416a768c20f9` | bounded adapt | same | containers, private-record migration claims, and binding coexistence |
| 11 | source | `AGENTS.md` | 31,319 / `79cd1e6bac0b` | bounded adapt | same | private context, containers, provider neutrality, binding coexistence |
| 12 | source | `CHANGELOG.md` | 43,630 / `a1aa3b04fa8c` | bounded adapt | same | retain releases 1.0–1.6; sanitize field overlay and correct public maintenance/path truth |
| 13 | source | `knowledge/INDEX.md` | 3,701 / `2b143d09efb3` | bounded adapt | same | retain navigation/risk rules; replace private populated index with empty generic state |
| 14 | source | `knowledge/records/как_мы_работаем.md` | withheld | exclude whole file | none | private mixed organizational/procedural record; category only, no body copied |
| 15 | source | `knowledge/records/кто_мы.md` | withheld | exclude whole file | none | private organizational identity record; category only |
| 16 | source | `knowledge/records/цели_и_ценности.md` | withheld | exclude whole file | none | private goals/values record; category only |
| 17 | source | `knowledge/records/чем_занимаемся.md` | withheld | exclude whole file | none | private business/activity record; category only |
| 18 | source | `MIGRATION.md` | 21,271 / `1bf711f1280b` | bounded adapt | same | functional maps retained; private targets, current paths, source names and binding path corrected |
| 19 | source | `people/README.md` | 6,283 / `10ec126927ec` | relocate + bounded adapt | `team/README.md` | approved common container; independent Assisted schema retained |
| 20 | source | `PROJECT.md` | 9,124 / `d1d8eb93ce61` | bounded adapt | same | visibly uninitialized neutral card; private defaults/constraints removed |
| 21 | source | `README.md` | 19,824 / `090d419abdfa` | bounded adapt | same | containers, private references, provider-neutral source/sync, binding coexistence |
| 22 | source | `VERSION` | 4 / `e5cd57eee963` | preserve byte-exact | same | exact public target version `1.6` |
| 23 | source | `шаблоны/assets/logo.png` | 14,004 / `f95b3bc78fd4` | exclude whole file | none | company logo/brand asset |
| 24 | source | `шаблоны/build_a4.py` | 7,298 / `ab18472ca1aa` | bounded adapt | same | neutral name/palette/asset only; artifact-builder algorithm retained |
| 25 | source | `шаблоны/документ_A4.md` | 5,270 / `b3638c2f3289` | bounded adapt | same | company header/footer neutralization |
| 26 | source | `шаблоны/заметка.md` | 3,293 / `ad5228af1466` | bounded adapt | same | identifying place/institution examples neutralized; worked example retained |
| 27 | source | `шаблоны/план_работы.md` | 7,790 / `03820291852c` | bounded adapt | same | `work/` → `workspace/`; full planning template retained |
| 28 | source | `шаблоны/презентация.html` | 25,557 / `fb4012fe3733` | bounded adapt | same | company name/logo/palette and fixed identifying examples neutralized; full deck retained |
| 29 | assisted-only | `editions/02-assisted/шаблоны/assets/tfw-mark.svg` | 270 / `1ed6d9081546` | retain byte-exact | same | one passive neutral replacement asset with a unique job |
| 30 | assisted-only | `editions/02-assisted/шаблоны/overlay/theme.css` | 182 / `69cc5a26887d` | delete | none | rejected extra theme layer; source templates already contain their complete styling |
| 31 | assisted-only | `editions/02-assisted/шаблоны/theme.css` | 185 / `6072dca48147` | delete | none | rejected extra theme abstraction; no unique job |
| 32 | maintenance | `editions/maintenance/maintenance-policy.json` | 1,840 / `f044ec7925f6` | delete | none | rejected static authority/protocol; conflicts with dynamic manifest + human gate |
| 33 | maintenance | `editions/maintenance/release-manifest.json` | 4,168 / `57ef3be53f72` | delete | none | stale 1.5 manifest and same-package origin claim; dynamic observed manifest replaces it |
| 34 | repository route | `editions/README.md` | current | bounded revise | same | Assisted 1.6 selection, copyability, relative links, capability truth |
| 35 | repository route | `editions/ASSISTED_MAINTENANCE.md` | current | bounded revise | same | asymmetric provider-neutral human-gated route; no JSON/runtime claim |

The resulting `editions/02-assisted/` tree has **24 shipped files**: 23 non-private source responsibilities (including the `people/README.md` relocation) plus the retained neutral mark. The four private records, source logo, two theme layers, and two maintenance JSON files are absent. The two repository routing documents remain outside the copied package.

### E2: Exact planned source-hunk ledger

Classification tags are the six DoD 3 reasons: `P` private-context removal; `N` neutral branding/example/provider cleanup; `C` approved container terminology migration; `R` edition-relative path correction; `M` version/maintenance truth; `B` machine-local binding coexistence. Ranges refer to immutable field-source lines. Comma-separated tags on one range are intentionally overlapping classifications, not extra hunks.

| Source file | Hunks | Planned immutable-source ranges and classifications |
|---|---:|---|
| `.agents/skills/tfw-plan/SKILL.md` | 2 | `21 [C]`; `29 [C]` |
| `.agents/skills/tfw-handoff/SKILL.md` | 2 | `12 [C]`; `30–31 [C]` |
| `.agents/skills/tfw-review/SKILL.md` | 2 | `12 [C]`; `31–32 [C]` |
| `.agents/skills/tfw-update/SKILL.md` | 10 | `3 [C]`; `18 [C]`; `43 [C]`; `45 [C]`; `53 [P,C,M]`; `57 [P,M]`; `64 [C]`; `67–68 [P,M,B]`; `73–74 [C,P,M]`; `81–83 [C,P,M]` |
| `.agents/skills/tfw-identity/SKILL.md` | 6 | `23 [C]`; `46–47 [C]`; `59 [N]`; `63 [B]`; `67–69 [B]`; `85 [B]` |
| `AGENTS.md` | 13 | `20 [P,N]`; `41 [C]`; `49 [B]`; `62 [C]`; `81 [C,M]`; `86 [C]`; `118–119 [C]`; `121 [C]`; `129 [C]`; `145 [N]`; `148–149 [C,N]`; `159 [C]`; `164 [C]` |
| `CHANGELOG.md` | 28 | `3 [N,P]`; `9 [M]`; `16 [N,M]`; `27–28 [C,P,M]`; `32 [C,P,M]`; `36 [N,P,M]`; `46–47 [C,M]`; `49 [N,M]`; `62–63 [C,N]`; `67–70 [B,N,C]`; `77 [C]`; `81–83 [C,B,P,M]`; `111 [N]`; `116 [N]`; `119–121 [C,P,M]`; `126 [N]`; `128 [C]`; `131–132 [C,P,M]`; `153 [C,N,M]`; `174 [P,M]`; `182–186 [C,P,M]`; `196 [N]`; `222 [M]`; `224 [C]`; `228 [N]`; `234 [P,N,M]`; `236 [N]`; `242 [C,M]` |
| `knowledge/INDEX.md` | 2 | `5 [P,N]`; `9–18 [P]` |
| `MIGRATION.md` | 20 | `7 [C]`; `13 [N]`; `18 [C,P,M]`; `20–22 [P,C,B,M]`; `30 [C,P,M]`; `34 [P,N,M]`; `40 [C]`; `46 [N]`; `51–52 [C]`; `54 [B]`; `63–64 [P,M,B]`; `77 [N]`; `79 [C]`; `85 [N]`; `87 [C]`; `89 [C]`; `118–119 [P,M,C]`; `135–136 [C]`; `138 [C]`; `151 [C]` |
| `people/README.md` → `team/README.md` | 4 | `3 [C]`; `7 [C]`; `25 [C]`; `39 [B]` |
| `PROJECT.md` | 9 | `12 [P,N]`; `18 [P,N]`; `20 [N]`; `28–35 [P]`; `45 [P,N]`; `49 [N]`; `56 [C]`; `58 [B]`; `64–70 [P]` |
| `README.md` | 10 | `5 [C]`; `16–18 [C,P]`; `31 [B,N]`; `37 [C]`; `45 [C]`; `56 [N]`; `83 [C]`; `93 [N,M]`; `96 [C,P,M]`; `102 [C]` |
| `шаблоны/build_a4.py` | 4 | `2 [N]`; `12–13 [N]`; `30 [N]`; `135 [N]` |
| `шаблоны/документ_A4.md` | 2 | `2 [N]`; `94 [N]` |
| `шаблоны/заметка.md` | 3 | `1 [N]`; `25 [N]`; `43 [N]` |
| `шаблоны/план_работы.md` | 2 | `3 [C]`; `78 [C]` |
| `шаблоны/презентация.html` | 17 | `6 [N]`; `9 [N]`; `12 [N]`; `30 [N]`; `35–44 [N]`; `114 [N]`; `153 [N]`; `226 [N]`; `264–265 [N]`; `279–280 [N]`; `289 [N]`; `294 [N]`; `296 [N]`; `302 [N]`; `337 [N]`; `362 [N]`; `380–381 [N]` |
| **Total** | **136** | **205 source lines in planned changed ranges** |

Exact-preserve source files have zero hunks: all five `agents/openai.yaml` files and `VERSION`. Whole-file exclusions also have zero source-text hunks because no part of those paths enters the target.

| Classification | Tagged hunks | Interpretation |
|---|---:|---|
| `P` private-context removal | 31 | private facts/defaults/record migration claims are removed or generalized |
| `N` neutral branding/example/provider cleanup | 58 | direct names, logo references, identifying examples, field palette, and vendor-specific wording |
| `C` container migration | 66 | active `people/`→`team/`, `work/`→`workspace/`, plus explicit legacy-source mappings |
| `R` edition-relative path correction | 0 source hunks | applies only to current repository routing documents, not the copied field source |
| `M` version/maintenance truth | 30 | public derivative provenance, functional maps, removal of stale/static authority claims |
| `B` binding coexistence | 13 | canonical child namespace, legacy Assisted non-read/non-migration, Full isolation |

Counts overlap because one contiguous range may solve several allowed concerns. The unique total remains **136**, not the sum of tag counts.

### E3: Preservation is the dominant operation

The 17 adapted source text files contain **2,105 lines**. The ledger places **205 lines (9.7%)** inside planned changed ranges and **1,900 lines (90.3%)** outside them. The six exact source files add another 21 byte-preserved lines. The large behavioral surfaces remain materially intact:

| Surface | Source size | Planned hunk constraint |
|---|---:|---|
| five behavioral skills | 75–147 lines each | only the ranges above may change; all gates, fail-closed rules, reports and lifecycle steps survive |
| `AGENTS.md` | 181 lines | 15 source lines bounded; complete working contract retained |
| `CHANGELOG.md` | 242 lines | all releases 1.0–1.6 and non-private hook/migration evidence retained |
| `MIGRATION.md` | 151 lines | exact historical maps/stop rules retained with public target/path/privacy corrections |
| note | 51 lines | three identifying-example lines change; worked decision example remains |
| work plan | 84 lines | two path lines change; full Gate/DoD/DoF structure remains |
| A4 document | 94 lines | two brand lines change; three-page worked structure remains |
| presentation | 393 lines | 29 brand/palette/example lines bounded; full HTML/CSS deck remains |
| A4 builder | 165 lines | five neutral-style/asset lines bounded; parsing/rendering algorithm remains artifact-only |

### E4: Sanitized provenance is more truthful than either verbatim retention or omission

The 1.0–1.6 headings, dates, functional milestones, migration gates, hook removal history, and non-private stock hook hashes remain. Organization-specific starter names, private-record names/hashes, internal event wording, company asset claims, and vendor-bound sync statements become generic field-overlay/public-derivative wording. Historical old-container paths remain only when they are input facts; active destinations use `team/`/`workspace/` or spell out old-source → new-target.

This follows the human-oriented changelog rule that every version and notable change should remain visible while avoiding irrelevant implementation dumps. Source: [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/). It also avoids claiming a new `1.6` binary-equivalent release: `VERSION` stays owner-frozen at 1.6, while the 1.6 narrative explicitly records the later public neutralization as a classified derivative.

### E5: The only ambiguous hunk cluster is resolved without amendment

The presentation labels its colors and typography as the company's visual style. Therefore the palette sites at source lines `30`, `35–44`, `114`, `153`, `226`, `264–265`, and `279–280` are branding, not generic algorithm. They are included in the 17 presentation hunks and will be replaced with one neutral built-in palette; the CSS/layout/component system remains. Omitting these sites would leave indirect company branding, while deleting or replacing the full 393-line template would violate preservation. The frozen DoD already authorizes neutral branding cleanup, so no amendment proposal is required.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| All 35 paths disposed; 136 source hunks/205 lines exactly ranged and tagged; provenance/container ambiguity resolved; preservation quantified | Attack the ledger for leakage, missing algorithms, false migration claims, and count instability |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: preauthorized focused continuation to Challenge
