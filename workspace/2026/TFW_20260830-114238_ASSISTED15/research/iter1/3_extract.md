# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260830-114238_ASSISTED15](../../HL-TFW_20260830-114238_ASSISTED15.md)
> Goal: Deliver a standalone, organizationally neutral Assisted 1.5 whose lifecycle, identity, update discipline, and practical templates are derived from the read-only Innoforce field lineage and maintained through an explicit public-core/private-overlay boundary.

## Configuration Space

Gather's D1 is path-scoped rather than package-global: every viable release needs public-core, stock-customizable, downstream-only, and retired/quarantine classes at the same time. The full space is therefore factorized instead of pretending that one D1 alternative can describe the whole tree.

The following combinations are structurally contradictory and are not enumerated: symmetric blind mirroring (D2-B), version-only baseline proof (D3-A), whole-directory installed-project replacement (D4-A), a package/shared identity store (D5-A), independently maintained bilingual copies in this Russian-baseline phase (D7-C), mandatory task APIs without fallback (D8-C), and a literal field changelog presented as public release history (D9-A).

### Package and maintenance policies

| Policy | D1: Path authority | D2: Direction model | D3: Baseline proof | D4: Mutation primitive | D6: Template ownership | D9: Release-history authority |
|---|---|---|---|---|---|---|
| P1 | all four classes, per path | public → downstream only | per-file SHA-256 manifest | hash-gated per-file replacement | stock-hash protected customization | public Assisted history only |
| P2 | all four classes, per path | asymmetric forward + reviewed reverse | per-file SHA-256 manifest with accepted prior stock hashes | hash-gated forward; manual candidate promotion | neutral semantic stock + downstream brand overlay | public history + separately labelled field provenance |
| P3 | all four classes, per path | asymmetric forward + reviewed reverse | retained three-way base snapshot | three-way text merge; manual binary handling | neutral semantic stock + downstream brand overlay | public history + separately labelled field provenance |
| P4 | all four classes, per path | asymmetric forward + reviewed reverse | signed/tagged release manifest | hash-gated forward; manual candidate promotion | neutral semantic stock + downstream brand overlay | public history + separately labelled field provenance |
| P5 | all four classes, per path | generate public and field from a third tree | signed/tagged release manifest | regenerate clean outputs; never mutate installations directly | neutral semantic stock + generated overlay | history generated from repository tags |
| P6 | all four classes, per path | asymmetric forward + reviewed reverse | per-file SHA-256 manifest | manual reconstruction/new-file-only | stock-hash protected customization | public history + separately labelled field provenance |

### Runtime and user-layer policies

| Runtime | D5: Persistent participant state | D7: User-facing language authority | D8: Orchestration capability |
|---|---|---|---|
| R1 | explicitly proven non-shared path; session-only on unknown/unsafe | Russian source of truth | capability-detected autonomous mode + manual fallback |
| R2 | session-only state | Russian source of truth | manual lifecycle only |
| R3 | explicitly proven non-shared path; session-only on unknown/unsafe | Russian source of truth | manual lifecycle only |
| R4 | explicitly proven non-shared path; session-only on unknown/unsafe | language-neutral mechanism + source-linked localized overlays | capability-detected autonomous mode + manual fallback |

All 24 non-obviously-contradictory configurations are the explicit cross-product `P1..P6 × R1..R4`. This factorization preserves every Gather dimension while avoiding a repetitive 24-row, nine-column table. A combination not proposed in the Briefing is `P4 × R2`: signed release integrity with session-only identity and manual lifecycle. It shows that package provenance, identity persistence, and automation availability are independent controls.

## Findings

### E1 — OODA Loop 1: separate integrity evidence from mutation authority

**Observe.** SPDX requires a file name/identifier and checksum and explains that a checksum can identify the desired file version, but detecting deliberate corruption depends on authenticating the checksum itself: [SPDX file information](https://spdx.github.io/spdx-spec/v2.2.2/file-information/). The field lineage already demonstrates runtime pre/post manifests and exact stock hashes, but it mixes generated inventory, version-specific migration prose, and path ownership across several files.

**Orient.** One hash table cannot answer all maintenance questions. A release manifest proves package bytes; an ownership policy says what a maintainer may do; a runtime report proves what was observed and changed in one installation. Combining them into an untyped “manifest” would let a correct hash appear to authorize an unsafe overwrite.

**Decide.** Use P2 as the 1.5 baseline and model three separate records:

1. A deterministic **release manifest** for the public package.
2. A versioned **maintenance policy** assigning authority and operations to exact paths or ordered path patterns.
3. A generated **operation report** with installed pre/post manifests, decisions, gates, and unexplained-change count.

P4 is compatible future hardening, not a prerequisite for 1.5. A signature authenticates a manifest but still does not classify a path or authorize a mutation.

**Act.** The minimum machine-readable contract is:

| Scope | Required fields | Rule |
|---|---|---|
| Release header | `schema_version`, `edition`, `release_version`, `hash_algorithm`, `canonicalization`, `tree_digest` | `release_version` must equal root `VERSION`; SHA-256; no absolute source path or participant data |
| Release entry | normalized relative `path`, `kind`, byte `size`, `sha256` | `/` separators, Unicode normalization declared, sorted canonical form; reject absolute/`..`, symlink escape, and case-fold collisions |
| Policy rule | exact path or ordered `pattern`, `authority`, `sensitivity`, `forward`, `reverse`, `postcondition` | exactly one matching authority; ambiguous or missing rule stops |
| Migration baseline | `from_version`, `accepted_stock_sha256`, `to_sha256` or `retire` rule | current downstream hash must match an accepted stock hash before automatic replacement/removal |
| Operation report | source/target release IDs and tree digests, pre/post entry sets, per-path decision, gate identity, verification result, `unexplained_changes` | paths and hashes only; private contents and corporate absolute paths never enter the public artifact |

The canonical tree digest should cover sorted records of `path<TAB>kind<TAB>size<TAB>sha256<LF>`. Unknown installed paths default to downstream-owned preservation plus a stop when they intersect a proposed write. This is safer than default-public authority.

Per-class postconditions are distinct:

| Authority | Forward postcondition | Reverse postcondition |
|---|---|---|
| public core | exact target release hash, unless an explicitly declared compatibility block is customizable | generic candidate only after baseline comparison, privacy scan, review, and new public release |
| stock customizable | replace only known prior stock; otherwise preserve byte-for-byte and report divergence | propose semantic delta; never copy branding/example data automatically |
| downstream-only | unchanged and excluded from package/runtime source manifests | denied |
| retired/quarantine | exact stock removed; modified payload quarantined or surgically deactivated; unrelated neighbors preserved | denied unless independently reconstructed as a new public mechanism |

### E2 — OODA Loop 2: identity, templates, and language are three different overlay problems

**Observe — identity.** The field script correctly separates profiles from binding state, rejects the project and declared shared roots, uses a distinct `tfw-assisted` namespace, locks writes, and performs same-directory atomic replacement. Its default path selection is still stronger than the evidence:

- Apple describes `~/Library/Application Support/<app>` as user-specific application state and notes that Application Support is backed up by default; it does not call the directory device-local: [macOS Library directories](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html), [File System Basics](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html).
- Gather already established that XDG persistent state is user-specific but only XDG runtime state receives an explicit local/not-shared guarantee, and that Windows LocalAppData being per-user is not proof against every redirect or sync configuration.

**Orient — identity.** “Conventional app-data location” and “proven non-shared on this machine” are different predicates. A user confirmation alone can also be wrong. The only contractually safe design is a three-state locality decision: `proven`, `unsafe`, or `unknown`, with no persistent write for the latter two.

**Decide — identity.** Preserve the field implementation's schema, collision, lock, atomicity, and Full/Assisted namespace separation, but replace optimistic path selection with this fail-closed gate:

1. Resolve an OS candidate or explicit override to an absolute canonical path.
2. Reject the project, every declared/detected sync root, symlink escape, non-private existing store, remote/network volume, and a known provider-managed path.
3. Require positive local-volume evidence appropriate to the platform; absence of a reliable probe is `unknown`, not success.
4. Persist only on `proven`; otherwise retain the human's choice in the active chat only, create no registry file, and explain that it will be asked again next session.
5. Treat binding as declared attribution, never authentication. A corrupt/duplicate binding, foreign lock, platform-probe error, or copied Full namespace also falls back without selecting a participant.

This satisfies frozen DoD 5/13 without promising persistent identity on machines where the runtime cannot prove locality. Linux/macOS may therefore be session-only by default in some environments; that is an intended safety outcome, not a degraded hidden write.

**Observe — templates.** Static analysis of the read-only template set found six useful capabilities: note, work plan, A4 source, presentation, deterministic Markdown-to-HTML builder, and an asset. The builder is standard-library-only and escapes text before limited inline formatting, but it hardcodes organization branding, assumes a fixed logo path, and loads web fonts. The A4/presentation sources also contain branded content and style assumptions.

**Orient — templates.** Deleting markers would preserve neither useful examples nor deterministic local rendering. Conversely, copying the style and logo would turn brand overlay into public core. Template semantics, default visual theme, project customization, and company branding need separate ownership.

**Decide — templates.** Use a D6-B/C hybrid:

- Public stock contains complete neutral Russian examples, layout semantics, the builder, and a new non-company asset.
- Brand assets, organization metadata, house colors, and real examples are downstream-only overlays.
- Installed copies of template source are stock-customizable: known old stock hashes may upgrade; a changed file is preserved and reported.
- The builder accepts an optional explicit theme/asset override, has a neutral built-in default, fails clearly on a requested missing asset, and has no required network fetch. Rendering evidence must run offline against both stock and overlay fixtures.

The split-stock-subtree alternative is architecturally clean but would force existing users to change paths and compose overlays immediately. Stock-hash protection plus an optional overlay convention preserves current paths and gives a migration path without overwriting customized templates.

**Observe — language.** GNU gettext treats translation as continuous maintenance: one source template evolves, language catalogs are refreshed, obsolete/new strings are surfaced, and uncertain matches remain for human judgment: [GNU gettext manual](https://www.gnu.org/software/gettext/manual/gettext.html). This is counter-evidence to treating two full hand-maintained documentation trees as equivalent authorities.

**Decide — language.** H4 survives: Russian remains the sole user-facing 1.5 source of truth, while machine-readable manifest enums and invariants remain language-neutral. No English mirror is added in this phase. A later localization may use source-linked overlays carrying `source_version`/baseline and freshness checks; it must be a separate release decision, not an untracked copy.

**Act.** Carry the identity locality gate, stock/custom overlay fixtures, offline rendering, and `content_language=ru` agreement into Challenge acceptance scenarios.

### E3 — OODA Loop 3: version history, reverse promotion, and reusable role sessions

**Observe — version/history.** The field package correctly declares `VERSION=1.5`, yet a project compatibility marker can still read 1.0. The public edition has no `VERSION` or changelog today. Semantic Versioning requires three numeric components and an immutable released version, so the requested two-component `1.5` must not be falsely labelled SemVer: [Semantic Versioning 2.0.0](https://semver.org/). Keep a Changelog recommends a human-curated, reverse-chronological entry for every actual release and an `Unreleased` section, rather than a noisy commit dump: [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).

**Decide — version/history.** `editions/02-assisted/VERSION` is the sole machine-readable product version and is exactly `1.5`. Root contracts and the uninitialized project card say “Assisted 1.5” and do not retain an unexplained 1.0 marker. `CHANGELOG.md` contains actual public Assisted releases (1.5 and the existing public 1.0 baseline) and a separately labelled, non-release provenance note that the intervening field lineage informed 1.5. It copies no private facts and does not present field 1.1–1.4 as public releases. The project explicitly uses an edition `major.minor` scheme, not SemVer.

**Observe — orchestration.** The field plan creates new handoff and review tasks on each failed cycle. The owner instead requires one coordinator, one executor, and one reviewer per phase. Official OpenAI guidance describes multi-agent as beta, tells implementers to define autonomy/approval boundaries, and recommends explicit routing, outputs, retry, and stop conditions: [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model). It does not establish one universal Codex desktop task-control surface.

**Orient — orchestration.** Independence is a separation-of-role property, not a requirement to discard a reviewer's session after every verdict. Reusing one executor thread preserves correction context; reusing one reviewer thread preserves the defect ledger while remaining independent from implementation. Creating fresh tasks on every retry adds coordination state without strengthening writer isolation.

**Decide — reusable roles.** Assisted autonomous mode uses a phase-scoped role pool:

| Role | Cardinality and reuse | Write authority | Reports |
|---|---|---|---|
| plan/coordinator | exactly one for the phase | coordinator trace only while no child writer is active | only final owner package, amendments, or genuine blockers go upward |
| handoff/executor | at most one; all corrections return to the same session | implementation and RF/trace scope while active | preflight/final to coordinator only |
| review/reviewer | at most one; every re-review returns to the same session | review verdict only; never implementation | preflight/PASS/FAIL to coordinator only |

The capability gate must confirm create-or-attach, stable targeting for follow-up, completion/status observation, and verifiable role identity before autonomous mode starts. A runtime handle remains runtime-local rather than becoming shared project identity. If any required operation is absent or becomes unreliable, the coordinator emits exact manual `/tfw-handoff` or `/tfw-review` transitions and stops autonomous claims. Executor and reviewer are never active writers simultaneously.

**Observe — reverse direction.** No field updater implements promotion to public core. A reverse bridge must therefore be proposal-driven:

1. Read trusted public and downstream baselines and compute non-mutating manifests/diffs.
2. Reject downstream-only, private, branded, unknown, or unclassified paths by default.
3. Convert remaining generic deltas into a candidate report/patch with source hashes, rationale, and neutralization notes; never write public core from the comparison step.
4. Independently review and explicitly approve the candidate under the public task contract.
5. Release the public change first, then use the normal forward path to update downstream.

**Act.** Select `P2 × R1` as the complete 1.5 configuration, with `P6` as the reverse-promotion fallback and `R2` as the mandatory manual/session-only degradation path.

### E4 — Surviving and rejected configurations

| Configuration | Status | Reason |
|---|---|---|
| `P2 × R1` | **survives; selected** | Meets both maintenance directions, customization protection, Russian baseline, fail-closed identity, and honest autonomous/manual modes |
| `P2 × R2` | **survives as degraded mode** | Same safe package contract when persistence and task controls are unavailable |
| `P6 × R1` | **survives as reverse fallback** | Slow but safest when a generic field delta cannot be mechanically separated from context |
| `P4 × R1` | **survives as later hardening** | Authenticated manifests can strengthen provenance after key/distribution ownership exists |
| `P1 × any` | rejected as the complete product | Safe forward update but cannot satisfy the reviewed downstream→public bridge |
| `P3 × any` | rejected for automatic 1.5 mutation | Needs a trusted retained base, still conflicts on overlapping text, and does not solve binary/template semantics |
| `P4 × any` as mandatory | rejected for 1.5 | Adds key lifecycle and distribution work; signature does not supply ownership or sanitization decisions |
| `P5 × any` | rejected for this phase | Introduces a third source of truth and generator migration beyond the approved edition update |
| `P6 × any` as the only mode | rejected as primary | Preserves safety but makes routine known-stock forward updates unnecessarily manual |
| `R3` as the only runtime | rejected as primary | Omits field-proven autonomous coordination even when the runtime supports it |
| `R4` in 1.5 | deferred, not rejected globally | Localization is valuable but frozen scope deliberately keeps the Russian baseline separate |

Counter-evidence changed the preferred design in five places: signatures are optional rather than sufficient; three-way merge is not the default; OS app-data paths are candidates rather than proof; split template subtrees are not forced on existing users; and a fresh child task per retry is not equated with independent review.

### E5 — Hypothesis movement and recommendation classification

| Hypothesis | Gather | Extract | Basis |
|---|---|---|---|
| H1 | conditional support | **supported with required refinement** | Universal lifecycle/identity invariants survive if unknown locality has a no-write session fallback and orchestration is capability-gated |
| H2 | narrowed | **supported as a compound contract** | Classified release manifest + maintenance policy + trusted stock baselines + operation report support safe gating; manifest/diff alone never authorizes mutation |
| H3 | partial support | **supported structurally; execution evidence pending** | All six practical capabilities can use neutral stock plus optional downstream overlay; Challenge/implementation must render offline fixtures |
| H4 | open | **supported for 1.5** | Frozen Russian baseline avoids a second authority; primary localization guidance confirms translations require explicit ongoing synchronization |

- **Refinements:** the manifest is three logically separate records; path rules default-deny; identity uses a positive locality state rather than directory-name trust; template ownership combines stock-hash protection with optional overlays; `VERSION` is the only product-version authority; role sessions are reused per phase; reverse promotion is proposal-only.
- **Amendment proposals:** none. These decisions narrow implementation while preserving every frozen vision, phase, DoD/DoF, gate, and scope boundary.

### E6 — Remaining attacks for Challenge

- Attempt case-fold, Unicode-normalization, symlink, unknown-path, modified-stock, missing-file, binary, and concurrent-baseline attacks against the manifest/policy state machine.
- Attempt identity persistence from project, known sync roots, remote volumes, ambiguous OS probes, corrupt registries, foreign locks, and Full namespace; confirm zero-write session fallback.
- Attempt public template output with missing/overridden asset, offline fonts, long tables, Cyrillic/Latin text, and private marker fixtures; require readable neutral render evidence later in implementation.
- Attack changelog neutrality and 1.0→1.5 migration consistency, including whether provenance language leaks a corporate fact or falsely claims a public field release.
- Test the reusable-role contract with missing create/rename/wait/follow-up capability, FAIL→correction→re-review, interrupted coordinator, and simultaneous-writer attempts.
- Demonstrate both directions from clean fixtures with zero unexplained paths; reverse remains candidate-only until public review accepts it.

## Checkpoint

| Found | Remaining |
|---|---|
| Factorized 24-configuration space; selected P2×R1 with explicit fallbacks; minimum release/policy/report schema; safe identity fallback; template ownership/overlay; version/changelog authority; Russian language authority; reusable-role orchestration; reviewed reverse pipeline | Adversarially eliminate hidden failure modes and turn surviving decisions into Challenge acceptance constraints; actual render and platform execution evidence remains implementation work |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

**Deep-mode exit:** 6 Extract decisions recorded; H1–H4 tested; counter-evidence changed five preferred mechanisms; three OODA loops completed.

**Metacognitive check:** The configuration space exposed a new independence result: authenticated release provenance can coexist with session-only identity and manual lifecycle. This prevented package integrity, participant persistence, and orchestration capability from being collapsed into one “advanced mode.”

Stage complete: YES
→ Phase Coordinator decision: recommend close Extract and proceed to Challenge
