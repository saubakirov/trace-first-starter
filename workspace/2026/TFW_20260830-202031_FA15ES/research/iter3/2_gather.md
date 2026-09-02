# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> Goal: Restore the field-proven Assisted 1.6 behavior as a neutral standalone edition through bounded, fully classified edits.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D _(if any)_ |
|-----------|-------|-------|-------|-----------------|
| D1 — path disposition | preserve at the same path | relocate/adapt to the public path | exclude/delete | retain a current-only public path |
| D2 — source-text treatment | byte-exact | bounded source-line edit | replace a contiguous block | whole-file replacement |
| D3 — field provenance | retain literally | retain as explicitly historical | sanitize organization-specific locator/fact while keeping the milestone | omit the milestone |
| D4 — public neutralization | remove only direct names/logo | also neutralize identifying examples | also replace field palette | replace the whole template |
| D5 — old/new container references | current public path only | historical source path only | explicit old-source → new-target mapping | global token replacement |

## Findings

### G1: The comparison boundary is exactly 35 paths

The immutable field root contains **28 files / 297,522 bytes**. The current public package contains **26 files**: 23 paths overlap the source, two source-private classes account for five source-only paths (four private knowledge records and one company logo), and exactly three paths exist only in the current package (one neutral SVG mark and two theme layers). Two JSON maintenance records and the two repository-level Editions routing documents complete the contract boundary:

| Set | Count | Boundary consequence |
|---|---:|---|
| field Assisted 1.6 source files | 28 | every row requires a disposition |
| current-only paths below `editions/02-assisted/` | 3 | retain the neutral mark; test the two themes against the no-extra-layer rule |
| current `editions/maintenance/` files | 2 | test against the no-static-maintenance-machinery decision |
| Editions routing documents | 2 | revise version and asymmetric-maintenance truth |
| **total disposition rows** | **35** | no category summary may replace a row |

The 23 shared relative paths have zero byte-exact matches. That fact is not evidence for 23 rewrites: the current public tree is the rejected reconstruction, while the field tree is the preservation baseline.

### G2: Privacy is a path/content boundary, not a reason to discard algorithms

The four source files below `knowledge/records/` are private organizational records. They are identified in the final ledger by path, broad category, and exclusion reason only; their record bodies, claims, people, and quoted wording are not copied into research. The populated organization/project defaults in `PROJECT.md`, organization claims in `knowledge/INDEX.md`, company identity in templates, and the logo asset are separate private/branding surfaces inside otherwise useful files.

NIST's Privacy Framework treats data minimization and limiting identification as privacy-risk controls. Applied here, the smallest sufficient public disclosure is: identify the excluded file/category, retain no record body, and keep a generic empty knowledge-navigation contract. This supports selective hunk removal rather than either verbatim publication or wholesale deletion of the surrounding Assisted behavior. Source: [NIST Privacy Framework Core](https://www.nist.gov/system/files/documents/2021/05/05/NIST-Privacy-Framework-V1.0-Core-PDF.pdf).

### G3: A count needs a reproducible hunk definition

The line ledger uses the immutable field 1.6 file and line numbers. A **planned source hunk** is a maximal contiguous source-line range whose content will change. Unchanged source lines split hunks; additions are anchored to the adjacent source range. A hunk may carry more than one allowed DoD 3 classification, and class totals therefore overlap while the unique-hunk total does not. Whole-file exclusion, path relocation, current-only retention/deletion, and repository-only edits are path dispositions, not changed source hunks.

This matches a future `git diff --unified=0 --inter-hunk-context=0` audit: Git documents that `--unified=<n>` controls context and `--inter-hunk-context` controls fusion of nearby hunks. Implementation must compare its realized source-derived target against this semantic ledger and explain any boundary shift caused by the concrete replacement text. Source: [Git `diff` documentation](https://git-scm.com/docs/git-diff.html).

### G4: Historical `work/` and `people/` are the only non-mechanical terminology case

Active public instructions must use `workspace/` and `team/`. Historical sections cannot be changed by global token replacement without falsifying the 1.0–1.6 lineage. The alternatives are: keep an old token only when it identifies a legacy input; rewrite an active target to the new container; or state an explicit old-source → new-target mapping. This is the only discovered ambiguity with potential to change the hunk map. It is resolvable inside the approved contract and does not require a frozen-section amendment.

### G5: Substantial surfaces are measurable before editing

The source carries five complete behavioral skills plus metadata, four root behavioral/reference documents, a complete 1.0–1.6 changelog, a migration guide, participant and knowledge navigation, and five practical output files including a 393-line presentation and the artifact-only A4 builder. The preservation test is not file presence alone: the hunk ledger must leave all unlisted source ranges unchanged and the later implementation must render/run the practical artifacts.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Exact 35-path scope, private path classes, zero-context hunk definition, and historical-container ambiguity are bounded | Build the 35-row disposition ledger and enumerate every planned source hunk with tags |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified? _(skip if <3 independent factors — use comparison matrix in Findings instead)_

Stage complete: YES
→ User decision: preauthorized focused continuation to Extract
