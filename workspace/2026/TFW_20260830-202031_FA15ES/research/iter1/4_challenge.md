# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> Goal: Restore field-proven Assisted 1.6 as an independent TFW realization while preserving isolated Full/Assisted identity semantics and a human-gated update path whose publisher chooses the release source.

## Consistency Check

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1: Device-store topology | Put Assisted under Full's existing local-state parent | D2: Existing Assisted-binding transition | Leave legacy location canonical | The Assisted record cannot remain canonical outside the proposed common parent and simultaneously establish that parent as the facility. |
| D1: Device-store topology | Keep sibling product roots | D2: Existing Assisted-binding transition | Re-onboard/create at new common-parent location | This silently selects a different D1 topology; the pair is internally inconsistent. |
| D1: Device-store topology | One polymorphic file | D2: Existing Assisted-binding transition | Guarded copy or permanent dual read | Assisted entries would enter or compete with Full's strict path→handle file, changing Full and erasing schema/write ownership boundaries. |
| D1: Device-store topology | Configurable common state root | D2: Existing Assisted-binding transition | Any | Full does not read the new setting; without a Full change it cannot be the common facility. |
| D1: Device-store topology | Common Full parent | D2: Existing Assisted-binding transition | Permanent dual read | Two Assisted authorities continue indefinitely and require precedence/divergence policy, contradicting subtraction and fail-closed single-source behavior. |
| D3: Publisher source-selection locus | Structured release-source manifest | D6: Trust and integrity proof | Package-internal hashes only | A manifest distributed and replaceable with the package cannot independently authenticate the publisher/source it names. |
| D4: Published release object | Versioned folder tree | D5: Release identity | Content digest plus version | A folder has no single provider-independent content digest unless another complete-tree manifest is introduced. |
| D4: Published release object | Git commit/tag tree | D5: Release identity | Semantic version plus mutable tag | GitHub documents that tag locking is provided only by immutable releases; an ordinary version-shaped tag may move. |
| D4: Published release object | Provider-native snapshot/export | D6: Trust and integrity proof | Provider checksum only | Drive checksum fields apply to stored binary content, not Google Docs/shortcuts/exports, so this cannot be a universal exact-byte rule. |
| D5: Release identity | Mutable `latest` locator | D6: Trust and integrity proof | Structural checks only | A structurally valid older or substituted package can pass; the locator does not pin an exact intended release. |
| D3: Publisher source-selection locus | Machine/project configuration field | D5: Release identity | Immutable provider object ID | The field becomes provider-specific durable state with migration and privacy duties while the same value can be supplied/confirmed at invocation. No unique job is established. |

### Surviving configurations

| Config | D1: Device-store topology | D2: Binding transition | D3: Source locus | D4/D5/D6 release contract | Notes |
|--------|---------------------------|------------------------|------------------|---------------------------|-------|
| B1U1 | Sibling roots | Legacy remains canonical | Per invocation | Versioned folder + semantic version + structural checks | Technically preserves both 1.6 systems exactly; weak against the strict physical reading of “one facility.” |
| B1U2 | Sibling roots | Legacy remains canonical | Per invocation | Versioned archive + version/digest + provider/computed digest | Strong update contract, but does not improve binding discoverability. |
| B2U1 | Common Full parent, isolated Assisted child | Re-onboard at new path; old state untouched | Per invocation | Versioned folder + computed tree manifest + one human gate | No new source artifact; suitable for synced/local Drive trees when no archive is available. |
| B2U2 | Common Full parent, isolated Assisted child | Re-onboard at new path; old state untouched | Per invocation | Versioned archive + version/digest + provider/computed digest | Smallest full H2a/H4 mechanism; publisher discovery remains manual. |
| B2U3 | Common Full parent, isolated Assisted child | Re-onboard at new path; old state untouched | Publisher documentation + explicit invocation | Exact versioned archive/object ID + provider/computed digest | Adds a durable human-readable publisher route without a machine schema. |
| B2U6 | Common Full parent, isolated Assisted child | Re-onboard at new path; old state untouched | Publisher documentation + explicit invocation | Immutable GitHub release/asset + digest/attestation + computed manifest | Strong public-TFW practice; cannot be required of Drive/other publishers. |
| B3U2 | Common Full parent, isolated Assisted child | Guarded one-time Assisted-only copy | Per invocation | Versioned archive + version/digest + provider/computed digest | Preserves device convenience but adds two-path reservation and migration logic. |
| B3U3 | Common Full parent, isolated Assisted child | Guarded one-time Assisted-only copy | Publisher documentation + explicit invocation | Exact versioned archive/object ID + provider/computed digest | Strongest continuity, highest in-scope prompt complexity. |

### Unexpected survivors

- **B2U1:** a plain synced Drive folder remains viable without a static manifest because the updater can materialize one tree, compute a complete pre-gate manifest, and verify package/migration invariants. It has weaker origin/integrity evidence than an archive but need not be prohibited.
- **B1U2:** unchanged sibling binding roots coexist safely at the technical level; only the owner's intended meaning of “one facility” eliminates it, not a collision or schema defect.
- **B3U6:** an Assisted-only guarded location transition can coexist with GitHub attestation without coupling identity and update mechanisms; the two concerns are genuinely independent.

## Findings

### C1: Binding stress test favors re-onboarding over migration or dual authority

| Case | B2 outcome | Result |
|------|------------|--------|
| Full and Assisted both installed | Full opens only `tfw/bindings.yaml`; Assisted opens only `tfw/assisted/bindings.yml` under the same parent | No shared schema, record, lock, or writer |
| Same directory used by both implementations | Full key remains absolute path; Assisted key remains canonical `project_id` | No translation or collision; different declared participants remain visible rather than normalized |
| Same human has different handles/roles | Each implementation resolves only its own profile schema | No cross-profile import or impersonation |
| Shared device | Assisted stores `ask`; Full follows its own missing/binding rule | Independent human gates remain intact |
| Only one implementation present | The absent sibling file is never required or parsed | Standalone behavior preserved |
| Legacy Assisted file exists, new file absent | Preserve legacy bytes; ask the existing one concise human question; create only the current project entry at the new canonical path after normal reservation/post-read | Functional continuity with one bounded prompt; no local migration authority is invented |
| Both legacy and new files exist | New release reads only the new canonical file; legacy remains rollback evidence, not fallback authority | No precedence or silent merge |
| Canonical file invalid/locked/unsafe | Existing Assisted fail-closed/session-only behavior applies | No overwrite or guessed participant |
| Autonomous handoff/review | Field 1.6 already skips human binding and inherits the trace owner | Location change does not block autonomous roles |
| Old and new Assisted releases used alternately | Each version may retain a different local selection | Residual operational risk; no shared corruption, but documentation must tell users not to treat the legacy file as synchronized state |

B3 initially looked more backward-compatible, but it must reserve and reason about two locations, copy a multi-project file whose other projects may be unavailable for semantic validation, and define what happens after an older release writes the legacy file. B2 repeats the exact precedent already used in the field 1.4→1.5 namespace transition: machine-local selection is recreated after a human gate rather than migrated. It changes convenience once, not identity, profiles, project IDs, owners, or shared state.

**Decision C-D1:** recommend B2 provisionally. H2a is supported as a design: one device-local TFW parent, unchanged Full file, an Assisted-owned child and schema, no cross-reader, and one-time re-onboarding. Iteration 2 must fixture-test Windows and examine whether the POSIX move from platform-preferred state roots to Full's `~/.tfw` parent is an acceptable portability tradeoff.

### C2: Mutable provider locators cannot serve as release identity

A stable Drive `fileId` is not immutable content: Drive records a monotonically increasing file version and a revision history, and older binary revisions can be purged unless marked `keepForever` ([Drive file resource](https://developers.google.com/workspace/drive/api/reference/rest/v3/files), [Drive revision management](https://developers.google.com/workspace/drive/api/guides/manage-revisions)). A Drive folder or file ID can identify the shelf/object, but exact release identity still needs a versioned object/revision plus acquired-byte evidence.

Likewise, GitHub's strongest guarantee is conditional: immutable releases lock tags and assets and generate attestations, but immutability must be enabled for future releases ([GitHub immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases)). Ordinary tags/releases remain acceptable inputs only when the human gate sees the resolved version and computed digest; they must not be described as immutable.

**Decision C-D2:** recommend U3 as publisher guidance with U2/U1 as accepted runtime inputs. Each publisher names a release shelf in human-readable documentation; the invocation supplies or confirms one exact versioned package. Prefer one archive and record its provider/out-of-band digest when available. The core updater still accepts a folder or local tree, computes its own manifest, and applies exactly the same package and migration checks.

### C3: Rollback, substitution, access, and partial-source tests remain fail-closed without a new schema

| Failure case | Required behavior |
|--------------|-------------------|
| `latest` resolves to older/same version | Show actual current→target versions; refuse as an update unless the owner explicitly commissions a rollback with its own scope |
| Same Drive object receives new revision | Re-resolve immediately before the gate/write; compare version/revision/digest when exposed; otherwise rebuild manifest and return to the gate on change |
| Git tag/release asset changes | Treat as mutable unless provider reports immutable; re-resolve/digest before write and stop on change |
| Private link requires authentication | Use an already authorized environment capability if available; never request/store credentials; otherwise request an accessible export/attachment and change nothing |
| Folder/archive is partial or has multiple roots | Fail the existing exact-root/service-set/package-cleanliness checks |
| Archive contains escape path, duplicate normalized path, link/reparse escape, or executable source code | Reject/contain during safe materialization; never execute source code |
| Valid-looking package substituted at trusted locator | Human trust plus provider/out-of-band digest is the current boundary; structural checks alone do not authenticate the publisher, so report this residual risk honestly |
| Reverse field→public flow contains private context | Produce a new candidate outside both trees; independent privacy/semantic review precedes any later public task |

These are already expressible as prose in `/tfw-update`, `MIGRATION.md`, `CHANGELOG.md`, and `ASSISTED_MAINTENANCE.md`. A provider-specific `source.json` would create parsing, migration, and secret-handling surface without closing the trust gap.

### C4: The rejected JSON pair fails both the subtraction test and the stronger-security test

Deleting `release-manifest.json` and `maintenance-policy.json` loses no unique provider-selection behavior: the manifest is regenerated before the gate, while version/migration/protected-state authority already lives in `VERSION`, `CHANGELOG.md`, `MIGRATION.md`, and the updater. Keeping them still would not provide signed publisher trust. A genuinely unattended hostile-mirror design requires trusted keys, signed roles, version/expiry and consistent snapshots—the multi-role machinery described by TUF—not two unsigned package-local JSON documents ([TUF specification](https://theupdateframework.github.io/specification/v1.0.28/)). That stronger model conflicts with the approved human-gated, prompt-only scope and would require a new contract decision.

**Decision C-D3:** no separate manifest or policy schema has a unique necessary job for H4. Preserve dynamic manifests as evidence in each update report; keep publisher location and provider-specific instructions human-readable; keep the release/migration contract in the four existing Assisted carriers.

### C5: Challenge decision and remaining uncertainty

H4 is supported by current contracts plus bounded prose clarification. H2a has a feasible isolated layout but remains conditional until iteration 2 validates the new path and transition fixtures. The first iteration should recommend `MORE NEEDED`, both because the task control requires at least two iterations and because the cross-platform/concurrent-old-release residuals have not been empirically exercised.

## OODA Loop 1

- **Observe:** Attacked each candidate with same-device, legacy-state, shared-device, mutable-source, rollback, private-access, partial-package, and source-substitution cases; checked Drive revisions and GitHub immutability against primary provider documentation.
- **Orient:** Counter-evidence weakens any claim that a stable Drive ID or version-shaped Git tag is immutable. It also weakens B3: preserving a selection by copying state adds more authority/migration surface than asking once again.
- **Decide:** Generic sufficiency is met for iteration 1: external sources were used, incompatible pairs and survivors are explicit, and both Briefing questions now have evidence-backed provisional answers.
- **Act:** Carry B2 and U3/U2/U1 into RES, classify only free-section refinements, record no amendment proposal, and leave fixture validation to the Coordinator-controlled next iteration.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| B2 is the smallest isolated common-parent design; U3 with U2/U1 fallbacks is provider-neutral; mutable names/IDs are not immutable bytes; the two JSON schemas have no unique in-scope job. | Fixture-test the binding transition and POSIX tradeoff; exercise exact Drive/GitHub/local acquisition cases; decide whether origin-authentication risk is accepted or requires a separate stronger-security task. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: YES
→ User decision: Close iteration 1 under the Coordinator's pre-authorized delegation; Coordinator decides iteration 2 and updates `research/iterations.yaml`.
