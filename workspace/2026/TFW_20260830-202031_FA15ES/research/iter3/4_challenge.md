# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> Goal: Restore the field-proven Assisted 1.6 behavior as a neutral standalone edition through bounded, fully classified edits.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1 — path disposition | preserve at same path | D4 — public neutralization | remove only direct names/logo | the four private records would still ship |
| D2 — source-text treatment | byte-exact | D4 — public neutralization | identifying examples or field palette | those neutralizations necessarily change source bytes |
| D3 — field provenance | retain literally | D4 — public neutralization | remove organization-specific locator/fact | literal field wording contains the context being removed |
| D3 — field provenance | omit milestone | D2 — source-text treatment | bounded source-line edit | omitting releases would destroy the required 1.0–1.6 lineage rather than bound it |
| D5 — old/new container references | global token replacement | D3 — field provenance | retain as explicitly historical | it would falsify historical source paths and executable migration inputs |
| D1 — path disposition | retain current-only | D2 — source-text treatment | byte-exact | valid only for the passive SVG; retaining JSON/themes would preserve rejected machinery |

**Surviving configurations** (from Extract's Configuration Space, after removing rows containing incompatible pairs):

| Config | D1 | D2 | D3 | D4 | D5 | Notes |
|--------|----|----|----|----|----|-------|
| C2 | same path | bounded line edit | explicitly historical | identifying examples | explicit old→new | root docs and migration history |
| C3 | relocate/adapt | bounded line edit | explicitly historical | identifying examples | explicit old→new | `people/README.md` → `team/README.md` |
| C4 | relocate/adapt | contiguous block | sanitized milestone | neutral palette | explicit old→new | private blocks and branded palette only |
| C6 | current-only | byte-exact | n/a | direct identity removed elsewhere | current public | neutral passive SVG only |
| C7 | exclude/delete | n/a | sanitized milestone | direct identity removed | current public | private files, logo, themes, JSON machinery |
| C8 | same path | bounded line edit | sanitized milestone | neutral palette | current public | changelog/templates with source structure retained |

**Unexpected survivors**:
- C4: a palette replacement survives because source text itself labels that palette as the organization's visual identity. The replacement is one bounded set of color sites, not a theme subsystem or template rewrite.
- C6: one current-only asset survives even though current reconstruction is rejected; its passive mark has a unique necessary job and contains neither runtime behavior nor organization identity.

## Findings

### C1: Privacy attack — filenames are enough for the ledger; bodies and per-record metadata are not

The four private records remain whole-file exclusions. The trace identifies each file and a broad category/reason, but publishes neither record body, quoted claim, named person, extracted fact, size, nor digest. Public `knowledge/INDEX.md` keeps the generic navigation/risk algorithm and shows an empty record state. Downstream `/tfw-update` protects unknown/private `knowledge/**` rather than embedding the excluded records' names or hashes in public migration rules.

This is stronger than superficial masking. NIST SP 800-188 warns that de-identification should be governed against disclosure/re-identification risk, not treated as mere token replacement. The safe data-sharing model here is exclusion of the private records plus a generic public contract, with later reverse promotion limited to an independently reviewed generic candidate. Source: [NIST SP 800-188](https://csrc.nist.gov/pubs/sp/800/188/final).

Implementation privacy checks must cover text, paths, comments, image references/metadata, and rendered A4/presentation outputs. They must fail on direct organization identity, the excluded record filenames or historical private-record digests, field source locators, shipped human/project identity, the company logo, or identifying municipality/institution examples. Generic `knowledge/records/` as a future project capability is allowed; the four excluded stock records are not.

### C2: Preservation attack — no critical algorithm depends on an excluded file

The six exact files are generic and contain no private/source/container/binding indicator. Every behavioral skill remains present; the planned changed ranges affect path nouns, privacy claims, provider wording, or the binding location, not the algorithms' gates and failure behavior. The following invariants remain outside or are restated inside classified hunks:

| Surface | Invariant that must survive |
|---|---|
| identity | natural onboarding; ambiguity/collision gate; no guessing/overwrite; profile baseline/post-read; participant/owner/AI-role separation; reservation/atomic write; session-only fallback |
| plan | stable ID creation; exact task title; Gate 0; manual/autonomous choice; no unapproved downstream work |
| handoff | exact task selection; preflight; one active writer; DoD/DoF and knowledge decision; transition only to review |
| review | independent read-only verification; no artifact fix; PASS stays review; FAIL returns doing; final report |
| update | static source read before gate; full classified plan; protected baseline recheck; version-specific migration; no source-code execution; fail on unexplained change |
| templates | full note example; full 84-line plan; three-section A4 document; 393-line slide system; artifact-only Markdown→HTML builder |

Only **205 of 2,105 lines (9.7%)** in adapted source files are inside planned ranges. The remaining **1,900 lines (90.3%)** are a positive preservation obligation, not merely “out of scope.” Whole-file rewrites, formatting passes, translation, terminology cleanup outside the ranges, or reflow are unclassified changes and must fail review.

### C3: Count attack — make 136 reproducible rather than aspirational

The hunk total survives a recount of the Extract table: **136 unique planned source hunks**, covering **205 source lines** across **17 adapted source text files**. Tag counts overlap by design: `P=31`, `N=58`, `C=66`, `R=0`, `M=30`, `B=13`. Six exact source files and five excluded source files contribute zero source-text hunks. The complete path ledger independently recounts to **35 rows**.

The implementation audit must:

1. re-hash the read-only 28-file source tree before and after work and stop on drift;
2. compare each adapted target with its mapped source (`people/README.md` against `team/README.md`) using zero context, no inter-hunk fusion, minimal diff, and disabled indentation heuristic;
3. preserve source encoding and line endings so mechanical churn cannot become an unclassified full-file diff;
4. verify the realized source-side hunk ranges equal the 136-row/range plan; a split/merge caused by concrete replacement wording is a ledger discrepancy, not permission to ignore the count;
5. separately verify exact files by full SHA-256 and excluded/current-only paths by existence and hash checks.

Git's documentation makes hunk fusion configuration-sensitive, which is why the audit parameters are fixed rather than relying on a developer's default diff settings: [Git `diff` context options](https://git-scm.com/docs/diff-context-options.html).

### C4: Migration attack — global renaming would break old installations

Historical `work/` and `people/` strings are not private. They may remain only where an old release or installed source is being identified. Every active destination becomes `workspace/` or `team/`, and the functional maps must say which side is legacy. For protected migration:

- an old source `people/` profile maps one-to-one to `team/` without changing the Assisted profile schema or valid identifier;
- an old source `work/<ID>/` maps one-to-one to `workspace/<ID>/` without changing ID, trace semantics, result, owner, or history;
- an existing target, collision, mixed old/new state, changed baseline, or ambiguous path stops before write;
- downstream knowledge and customization remain protected; no public rule names a private record as stock content;
- the old `tfw-assisted` local registry is preserved but never read, merged, deleted, or used as fallback; the canonical new Assisted child path is used only after the existing one-question gate;
- Full's file, schema, path-key, profiles, and write authority remain untouched.

This resolves the only ambiguous hunk family. A global replacement is rejected; an explicit old-source → new-target map is both honest provenance and functional migration. No amendment is needed because approved amendment A2 already authorizes this exact container transition.

### C5: Version and maintenance attack — `1.6` must not imply a byte-identical field package

`VERSION` remains exact `1.6` as frozen. `CHANGELOG.md` retains every version heading from 1.0 through 1.6 and the useful lifecycle/migration milestones, but the 1.6 narrative must explicitly call the public edition a classified neutral derivative of the field behavior. It must not retain a field full-tree digest, claim an immutable publisher shelf that does not exist, or present the stale 1.5 JSON manifest as source authority.

`editions/ASSISTED_MAINTENANCE.md` becomes the durable asymmetric route established in iterations 1–2: human-confirm publisher/locator, materialize an exact source object, compute a dynamic manifest, recheck immediately before one explicit gate, preserve protected downstream state, and reverse only through a privacy-reviewed generic candidate. The two JSON files are deleted. The copied package's own prompt-only updater keeps functional migration/stop rules without depending on repository-adjacent machinery.

This is compatible with a human-oriented changelog: every release and notable change remains, while internal/private detail is removed rather than replacing the release history with a short reconstruction. The project does not claim Semantic Versioning; its frozen two-part `1.6` identifies the field behavior lineage, while the changelog records the public packaging adaptation.

### C6: Template attack — neutralization must not reduce usability

The field palette sites are replaced in place; the presentation layout, component classes, print behavior, slide examples, and instructions remain. The A4 builder still parses the same Markdown structures and only changes its identity/palette/asset lines. The passive SVG is used by both generated/document templates, and both source and rendered outputs must be checked for absence of the excluded logo.

The new palette is not accepted merely because it is neutral. Rendered ordinary text must meet at least **4.5:1** contrast and large text **3:1**, consistent with WCAG 2.2 SC 1.4.3. Source: [W3C Understanding Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). Offline rendering must remain usable through the existing font fallbacks; no new network/runtime dependency or theme layer may be added.

### C7: Path-ledger attack — no hidden additions remain

The 35 rows close all set differences. Source gives 28 rows; assisted-only gives three; maintenance gives two; repository routing gives two. The final copied package has 24 files. No additional manifest, registry, script, helper, theme, test runtime, logo, or maintenance protocol has a unique authorized job. Tests/fixtures may exist as task evidence during execution but are not shipped as product paths unless the frozen scope is amended.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Privacy, preservation, hunk-count, legacy migration, version/maintenance, template usability, and hidden-addition attacks all have explicit pass/fail checks | None before TS; implementation must realize and re-audit the planned hunks |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: YES
→ User decision: preauthorized focused continuation to Synthesis
