# RES — TFW_20260830-202031_FA15ES: Exact Assisted 1.6 Disposition, Privacy, Provenance, and Hunk Ledger — Iteration 3

> **Date**: 2026-09-02
> **Author**: saubakirov via Codex Researcher
> **Status**: 🔬 RES — Iteration 3 complete
> **Parent HL**: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> **Mode**: Pipeline / Focused

---

## Research Context

This iteration closed the two remaining pre-TS blind spots after the Coordinator accepted iterations 1–2: an exact disposition for all field/current Editions paths and an exact source-hunk plan that preserves Assisted 1.6 while removing private facts, organization identity, branded examples/assets, stale paths, and false maintenance claims. The field source and all product/control files remained read-only. Only `research/iter3/**` was written, and no private record body or per-record metadata was copied into the traces.

## Briefing

The focused plan, predecessor constraints, hypotheses, scope, and three guiding questions are recorded in [1_briefing.md](1_briefing.md). Gather fixed the 35-path boundary and zero-context hunk definition; Extract produced the complete disposition and 136-hunk ledger; Challenge attacked privacy, preservation, migration, count reproducibility, version/maintenance truth, template usability, and hidden additions.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D10 | Fix the complete implementation boundary at **35 disposition rows**: 28 field-source files, three current-only assisted-package paths, two current maintenance JSON paths, and two repository Editions routing documents. | The three set differences and two routing loci close every product path identified by the frozen contract. The Extract ledger independently recounts to 35 rows (G1, E1, C7). |
| D11 | Ship a **24-file** `editions/02-assisted/` package: retain/adapt the 23 non-private field responsibilities, relocate `people/README.md` to `team/README.md`, retain the current passive SVG, exclude four private records and the company logo, and delete both theme layers. Delete both maintenance JSON files; revise the two routing documents. | Every source/current-only path has one action and resulting path. The outcome restores field capability while eliminating private and rejected machinery (E1, C1, C7). |
| D12 | Define the exact source edit plan as **136 unique zero-context hunks over 205 immutable source lines in 17 adapted files**. Multi-purpose hunks have overlapping tags: `P=31`, `N=58`, `C=66`, `R=0`, `M=30`, `B=13`. Six exact source files and five excluded source files have zero source-text hunks. | This is reproducible with fixed diff settings and avoids inflating a hunk that solves more than one allowed concern. The per-file ranges sum to 136 and the path table sums to 35 (G3, E2, C3). |
| D13 | Treat privacy as whole-file exclusion for the four records and the logo, plus bounded removal/generalization inside otherwise useful files. Public traces identify a private record only by file, broad category, and exclusion reason; public migration rules protect downstream `knowledge/**` without naming private stock records or hashes. | Removing names alone would preserve disclosure risk; deleting surrounding algorithms would violate preservation. NIST privacy/de-identification guidance supports minimization and governed disclosure (G2, E1–E2, C1). |
| D14 | Preserve every 1.0–1.6 changelog heading, date, functional milestone, migration gate, hook-removal history, and non-private hook hash while replacing organization-specific locators/facts with explicit field-overlay/public-derivative wording. Keep `VERSION` byte-exact at `1.6`. | This retains a useful human history without claiming that the neutral public tree is byte-identical to the private field package or that a nonexistent/static publisher shelf is authoritative (E4, C5). |
| D15 | Do not globally replace historical `work/`/`people/`. Keep an old token only when it names a legacy input, and state every active mapping as old source → `workspace/`/`team/`; collision, mixed state, or changed baseline stops before write. | Global replacement would falsify provenance and break migration, while leaving active destinations old would violate approved A2. Explicit directional maps satisfy both constraints (G4, E5, C4). |
| D16 | Classify the source presentation palette as organization branding and neutralize only its enumerated color sites together with direct name/logo/example sites. Retain the full 393-line CSS/HTML system, and require contrast/render checks. The A4 builder changes only five neutral-style/asset lines and remains artifact-only. | Source comments explicitly identify the palette as a company visual system. The bounded option removes indirect branding without recreating the rejected theme abstraction or shortening practical outputs (E2–E5, C2, C6). |
| D17 | Make preservation executable in TS: **1,900 of 2,105 lines (90.3%)** in adapted files are outside the edit ranges and must remain unchanged; exact files require SHA equality; source drift, EOL/format churn, an extra hunk, or an unclassified product path fails review. | “Preserve by default” otherwise remains subjective. The measured envelope protects complete skills, root contracts, migration history, templates, and builder behavior (E3, C2–C3). |
| D18 | Recommend `SUFFICIENT` with no amendment proposal. The only ambiguous families—historic old-container strings and the company palette—are resolved by approved A2 and the frozen neutral-branding class. | All paths, hunks, privacy categories, provenance rules, and preservation checks are now specified. Concrete replacement prose, rendered validation, and realized-diff equality are TS/implementation duties, not open design research (C3–C7). |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q5 | Does every source/current-only Editions path have one final disposition and resulting path? | Closed | Yes: 35 rows, comprising 28 source, three assisted-only, two maintenance, and two routing-document paths. |
| Q6 | What is the exact planned source hunk count and classification? | Closed | 136 unique hunks / 205 source lines / 17 adapted files; overlapping tags `P31`, `N58`, `C66`, `R0`, `M30`, `B13`. |
| Q7 | Which organization references are private versus legitimate provenance? | Closed | Record bodies/facts, populated defaults, organization identity/asset/locators, private record names/hashes in public product prose, and identifying examples are removed/generalized. Version headings, dates, functional milestones, historical container inputs, and non-private hook-removal evidence remain as sanitized provenance. |
| Q8 | Does any hunk require a frozen-section amendment? | Closed | No. The historic-container resolution instantiates approved A2, and palette cleanup is already authorized as neutral branding. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | At least the complete non-private behavioral structure of every field 1.6 Markdown file can be preserved; required edits remain bounded to the DoD 3 classes. | confirmed by owner; exact evidence pending | 🟢 supported | D10–D13, D15–D17; E1–E3; C1–C4, C6–C7. All 28 source paths are disposed, 90.3% of adapted source lines remain outside edits, and every planned hunk has one or more of the six enumerated allowed tags. |
| H3 | The 1.0–1.6 changelog can retain every useful functional and migration milestone while removing private facts and clearly distinguishing overlay provenance. | confirmed by owner; exact evidence pending | 🟢 supported | D14–D15; E4–E5; C1, C4–C5. All release headings and functional maps remain; private facts/locators/hashes are replaced by directional, sanitized provenance. |

## HL Update Recommendations

> **The researcher classifies. The researcher never applies.** The Coordinator owns all HL and iteration-control changes.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 Current State | Replace the preliminary class ledger with the exact outcome: 35 disposition rows; final copied package 24 files; 23 source responsibilities plus one neutral mark; four private records, logo, two themes and two maintenance JSON files absent; routing documents revised. | D10–D11; E1; C7 |
| R2 | §7.2 Knowledge Citations | Add the hunk-count basis (Git zero-context/inter-hunk behavior), privacy minimization/de-identification basis (NIST), human-oriented complete-version changelog basis, and neutral-palette contrast check (W3C). | G2–G3; E4; C1, C3, C6 |
| R3 | §8 Dependencies | Mark “Complete 28-file disposition and hunk-classification evidence” complete with the 35-row/136-hunk/205-line totals. | D10–D12; E1–E2; C3 |
| R4 | §9 Risks | Add explicit review failures for global historical path replacement, source-line/EOL churn that changes hunk boundaries, and neutral palette changes without rendered contrast checks. | D15–D17; C3–C6 |
| R5 | §10 RESEARCH Case | Close both blind spots; mark H1 and H3 supported with exact evidence; correct the H1 prose count from “five” to the **six enumerated DoD 3 classes** without changing those classes. | Hypotheses table; D12–D18 |
| R6 | §11 Strategic Insights | Add that preservation is enforced by a source-side hunk allowlist plus an unchanged-line obligation, while old container tokens are permitted only as legacy inputs in directional migration maps. | D12, D15, D17; E2–E5; C2–C4 |

### Amendment Proposals — frozen sections, owner verdict required

No amendment proposals. The path relocation, privacy removal, binding placement, neutral branding, version target, and maintenance subtraction all instantiate already approved frozen claims or amendments A1–A2.

## Fact Candidates

No new fact candidates. The owner's privacy, preservation, container, version, and visible-task choices are already recorded in the approved HL and amendments; this iteration added agent-observed filesystem and source-line evidence rather than new human-only project knowledge.

## Strategic Insights (Research)

No strategic insights. No new human domain correction or selection occurred during this delegated iteration; the Researcher operationalized the already recorded owner decisions.

## Findings Map

```text
35-path implementation boundary
├── 28 field-source files
│   ├── 6 exact source files ─────────────────────────────── 0 hunks
│   ├── 17 bounded source files ── 2,105 lines
│   │   ├── planned edits ──────── 205 lines / 136 hunks
│   │   └── preservation envelope 1,900 lines / 90.3%
│   └── 5 excluded source files
│       ├── 4 private records (file/category/reason only)
│       └── 1 company logo
├── 3 assisted-only paths
│   ├── neutral SVG ────────────── retain exact
│   └── 2 theme layers ─────────── delete
├── 2 maintenance JSON paths ───── delete
└── 2 repository routing docs ──── revise

final copied package: 24 files

changed-hunk tags (overlap allowed)
P private 31     N neutral 58     C containers 66
R relative 0     M maintenance 30 B bindings 13

historic source work/people ──directional protected map──▶ workspace/team
private field overlay ────────sanitize, keep milestones──▶ public 1.0–1.6 lineage
company template identity ───bounded name/asset/palette──▶ substantial neutral outputs
```

## Iteration Status

- **Iteration:** 3 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (supported), H3 (supported)
- **Hypotheses deferred:** None
- **Gaps discovered:** No in-scope research gap. Concrete replacement wording, realized zero-context hunk equality, privacy scans, migration fixtures, and rendered template/builder checks belong in TS and implementation evidence.
- **Superseded decisions:** D18 extends iteration 2 D9's H2a/H4-scoped sufficiency conclusion to the whole master RESEARCH case by closing H1/H3. It does not revoke iterations 1–2 decisions D1–D8.

### Open Threads (for next iteration)

No open threads.

### Recommendation

- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [ ] **MORE NEEDED** — no in-scope research gap
- [ ] **BLOCKED** — no blocker

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 3 converted the last preservation/privacy concern into a complete implementation contract: 35 path dispositions and 136 classified source hunks over 205 lines, with 90.3% of the adapted source line surface explicitly unchanged. It distinguishes private field overlay from legitimate Assisted provenance, preserves every 1.0–1.6 milestone, maps legacy containers directionally instead of falsifying history, removes rejected JSON/theme machinery, and retains the complete skills and practical templates including the artifact-only builder. The self-critique is precise: 136 is the exact planned source-side count, not a post-implementation observation; concrete replacement text may expose a different diff boundary. That possibility is handled as a hard TS/review equality check—an unexplained split, merge, or extra hunk fails rather than silently changing the ledger. No research ambiguity or frozen amendment remains, so the recommendation is `SUFFICIENT` and the next workflow is `/tfw-plan`.

---

*RES — TFW_20260830-202031_FA15ES: Exact Assisted 1.6 Disposition, Privacy, Provenance, and Hunk Ledger — Iteration 3 | 2026-09-02*
