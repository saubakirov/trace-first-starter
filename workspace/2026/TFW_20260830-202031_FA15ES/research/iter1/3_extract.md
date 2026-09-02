# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> Goal: Restore field-proven Assisted 1.6 as an independent TFW realization while preserving isolated Full/Assisted identity semantics and a human-gated update path whose publisher chooses the release source.

## Configuration Space

The six Gather dimensions separate into two orthogonal subspaces. H2a chooses D1–D2; H4 chooses D3–D6. Every binding family below can compose with every update family, so the explicit cross-product is 4 × 7 = 28 configurations rather than an arbitrary sample of the original 4,096 raw combinations.

### Binding families (D1 × D2)

| Family | D1: Device-store topology | D2: Existing Assisted-binding transition |
|--------|---------------------------|------------------------------------------|
| B1 | Keep Full and Assisted sibling product roots | Leave legacy location canonical |
| B2 | Put Assisted under Full's existing local-state parent | Re-onboard and create only at the new location |
| B3 | Put Assisted under Full's existing local-state parent | Guarded one-time copy to the new location |
| B4 | Put Assisted under Full's existing local-state parent | Permanent precedence-based dual read |

Two raw D1 alternatives are obviously contradictory before evaluation: one polymorphic file requires Full to accept a second key/schema, and a configurable common root does not affect Full unless Full is changed. Both violate the frozen Editions-only/no-Full-change boundary, so they do not enter the configuration space.

### Update families (D3 × D4 × D5 × D6)

| Family | D3: Publisher source-selection locus | D4: Published release object | D5: Release identity | D6: Trust and integrity proof |
|--------|----------------------------------------|------------------------------|----------------------|---------------------------------|
| U1 | Source supplied per update invocation | Versioned folder tree | Semantic version plus locator | Structural package checks only |
| U2 | Source supplied per update invocation | One versioned archive file | Content digest plus version | Provider checksum/digest when exposed; otherwise computed manifest |
| U3 | Human-readable publisher source in product documentation | One versioned archive file | Immutable provider object/release ID | Provider checksum/digest plus computed manifest |
| U4 | Machine/project configuration field | One versioned archive file | Content digest plus version | Publisher-provided digest outside the package |
| U5 | Structured release-source manifest | Versioned folder tree | Mutable `latest` locator | Structural checks plus package-internal hashes |
| U6 | Human-readable publisher source in product documentation | Git commit/tag tree or attached archive | Immutable provider release ID | Signature/attestation plus computed manifest |
| U7 | Source supplied per update invocation | Provider-native snapshot/export | Immutable provider object ID | Provider checksum plus computed manifest |

### Explicit composite space

| Binding \ Update | U1 | U2 | U3 | U4 | U5 | U6 | U7 |
|------------------|----|----|----|----|----|----|----|
| B1 | B1U1 | B1U2 | B1U3 | B1U4 | B1U5 | B1U6 | B1U7 |
| B2 | B2U1 | B2U2 | B2U3 | B2U4 | B2U5 | B2U6 | B2U7 |
| B3 | B3U1 | B3U2 | B3U3 | B3U4 | B3U5 | B3U6 | B3U7 |
| B4 | B4U1 | B4U2 | B4U3 | B4U4 | B4U5 | B4U6 | B4U7 |

The initially unproposed combinations are visible here. In particular, B2U2 yields one TFW-local parent and provider-neutral exact archives without a source schema; B1U3 preserves both existing binding locations while still giving publishers explicit sources; B3U6 pairs guarded local-state adoption with GitHub's strongest release integrity option without making that option mandatory for Drive publishers.

## Findings

### E1: The smallest “one facility” interpretation that does not change Full is a parent/child ownership boundary

The concrete B2/B3/B4 target is:

| Platform | Existing Full path (unchanged) | Proposed Assisted canonical path | Existing Assisted 1.6 path |
|----------|--------------------------------|----------------------------------|----------------------------|
| Windows | `%LOCALAPPDATA%\tfw\bindings.yaml` | `%LOCALAPPDATA%\tfw\assisted\bindings.yml` | `%LOCALAPPDATA%\tfw-assisted\bindings.yml` |
| macOS | `~/.tfw/bindings.yaml` | `~/.tfw/assisted/bindings.yml` | `~/Library/Application Support/tfw-assisted/bindings.yml` |
| Linux/Unix | `~/.tfw/bindings.yaml` | `~/.tfw/assisted/bindings.yml` | `${XDG_STATE_HOME:-~/.local/state}/tfw-assisted/bindings.yml` |

`tfw/` is the device-local TFW family facility only because Full already owns that location. Full continues to open exactly `bindings.yaml`; Assisted opens exactly `assisted/bindings.yml`, keeps `schema_version: 1`, `project_id`, `fixed`/`ask`, its own reservation, and never enumerates or parses the sibling Full file. This is namespace coexistence, not shared technical authority.

B2 is the least migration machinery: after upgrade, a missing new binding triggers the existing one-question human gate and creates only the current project's new entry; the old file is ignored and preserved. B3 preserves convenience across all existing Assisted projects but requires a two-location reservation/copy protocol and a precise rule for foreign/invalid entries. B4 creates two continuing authorities and therefore needs precedence, divergence, and rollback semantics forever.

### E2: The universal source contract is behavioral, not a provider schema

The existing field updater already defines the following provider-neutral contract:

1. **Locator input:** a human supplies or confirms an accessible path, archive, link, attachment, cloud object, or other representation. If it is a URI, generic URI syntax deliberately permits scheme-independent parsing while deferring scheme-specific semantics ([RFC 3986](https://www.rfc-editor.org/info/rfc3986/)); local paths remain valid opaque inputs rather than being forced into an invented URI scheme.
2. **Closed release object:** acquisition yields exactly one safe temporary file tree; escape paths, duplicate normalized paths, unsafe links/reparse points, special files, partial roots, personalized projects, and candidate-only packages are refused.
3. **Claimed identity:** root markers plus `VERSION` name the release; `CHANGELOG.md` and `MIGRATION.md` provide the exact source-version transition and protected-state authority.
4. **Integrity/completeness evidence:** the agent computes a manifest and SHA-256 evidence over the acquired object. SHA-256 is part of the NIST Secure Hash Standard ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)); a provider digest or independently published digest may be compared when available.
5. **Human authority:** source form, access method, versions, service/protected diffs, migration map, checks, and stop conditions are presented before the one write gate.

None of these steps requires a new checked-in `source.json`. Publisher choice can remain human-readable: public TFW documentation points to its GitHub release/archive; an Innoforce overlay points to its Drive release shelf; a third producer names another source. The updater consumes the concrete locator at invocation and applies the same checks.

### E3: Exact archive is a useful portability boundary, not a mandatory transport

Drive has stable object IDs and optional SHA-256 metadata for stored binary files; GitHub release assets expose version/tag, asset ID, size, digest, and optional immutable-release protection. A single versioned archive lets both expose one object and one digest, while a local path or already-extracted tree remains acceptable after the updater computes its own manifest. Therefore U2/U3 are stronger publisher practices, but U1 remains necessary for offline/local and low-capability environments.

This distinction avoids hard-coding “Google Drive folder” into the product contract. Drive can host a folder of versioned archives; GitHub can host release assets; another publisher can provide a network share or attachment. Acquisition differs; the closed-tree and migration invariants do not.

### E4: A new manifest has a unique job only under a stronger unattended-adversary threat model

The two rejected JSON files are neither needed to select a provider nor sufficient to authenticate one. They restate service paths, release version, baseline, and migration selectors already available from the package and migration documents. A fully secure autonomous repository would require a much larger trust system: The Update Framework specifies signed root, targets, snapshot, and timestamp roles with versions, expiry, hashes, and thresholds ([TUF specification](https://theupdateframework.github.io/specification/v1.0.28/)). That is evidence that “add one unsigned manifest” is not a small substitute for repository trust; it is also far outside the frozen human-gated, prompt-only, subtraction-first scope.

A package-internal file inventory could still have the bounded job of accidental corruption detection for a bare folder. U2/U3 make that separate artifact unnecessary by preferring one archive plus provider/out-of-band digest and always computing an acquired-tree manifest before the gate. U1 can compute and display the manifest dynamically, as field 1.6 already requires.

### E5: Extract decision

Carry B1, B2, and B3 to Challenge; B4 remains only as an explicit complexity comparator. Carry U1, U2, and U3 as the provider-neutral core/practice set; retain U6 as optional stronger GitHub evidence and U5 as the manifest comparator. U4 introduces synced/local configuration state that has no unique job over a one-question locator, and U7 makes provider export semantics part of release identity, so neither needs priority in the challenge set.

## OODA Loop 1

- **Observe:** Cross-referenced six dimensions; checked generic locator and digest standards; compared the two local JSON schemas with the field updater's existing package/migration controls.
- **Orient:** The configuration space reveals that the strongest in-scope solution can use no source manifest and no combined binding file. Provider neutrality and source authenticity are separate from transport convenience.
- **Decide:** Generic sufficiency is met: external primary sources were used, the configuration space contains all 28 non-obviously-contradictory composites, and the Briefing gap is reduced to edge-case selection.
- **Act:** Challenge B1–B4 against binding migration/failure cases and U1/U2/U3/U5/U6 against mutable source, rollback, access, and privacy cases.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| A common parent with an Assisted child preserves Full byte/schema behavior; the existing updater already supplies a five-part provider-neutral behavioral contract; exact archive + digest is a publisher practice, not new product machinery. | Decide between B1/B2/B3; test whether re-onboarding is backward-compatible enough; attack mutable Drive/GitHub locators, rollback, private access, partial packages, and the “unsigned manifest” alternative. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: Proceed under the Coordinator's pre-authorized full-iteration delegation; the Coordinator will decide whether iteration 2 continues or alters the recommendation.
