# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> Goal: Assisted 1.6 remains a faithful independent TFW realization while Full and Assisted coexist on one device and publishers choose update sources without provider-specific product machinery.

## Configuration Space

The raw Cartesian product of Gather's nine dimensions exceeds 30 combinations and mixes two independent subsystems. The space is therefore represented as coherent binding and source families; any binding row can pair with any source row. `B3` and `U5` were not proposed in the Briefing and make the hidden alternatives visible.

### Binding families

| Config | D1: Physical binding layout | D2: Legacy Assisted handling | D3: Unresolved local state | D4: Host placement |
|--------|-----------------------------|--------------------------------|------------------------------------|--------------------|
| B1 | One combined Full/Assisted YAML | Automatic copy/merge | Repair or overwrite | Current Full path |
| B2 | Separate files under one physical TFW parent | Preserve and ignore; one-time re-onboarding | One question, then session-only when persistence is unsafe | Current Full path is family root |
| B3 | Separate platform-native roots presented as one conceptual facility | Preserve and ignore; one-time re-onboarding | One question, then session-only when persistence is unsafe | Each OS's preferred application-state root |
| B4 | New standalone common root requiring both systems to move | Automatic copy/merge | One question, then session-only when persistence is unsafe | User-configured root |
| B5 | Separate files under one physical TFW parent | Permanent dual read | One question, then session-only when persistence is unsafe | Current Full path is family root |
| B6 | Separate files under one physical TFW parent | Delete after transition | Stop all conversation | Current Full path is family root |

### Update-source families

| Config | D5: Source representation | D6: Exact-byte evidence | D7: Recheck model | D8: Origin assurance | D9: Documentation ownership |
|--------|---------------------------|-------------------------|-------------------|----------------------|-----------------------------|
| U1 | Versioned archive/blob | Computed archive digest plus dynamic tree manifest | Re-fetch/re-read exact object and recompute before Gate | Human-confirmed publisher/location | Publisher shelf outside installable package; generic updater and migration docs inside |
| U2 | Provider folder/tree | Computed dynamic tree manifest | Re-read folder membership and every file before Gate | Human-confirmed publisher/location | Same split as U1 |
| U3 | Drive archive/blob | File/revision metadata, provider checksum when available, plus dynamic tree manifest | Re-fetch named file/revision and recompute before Gate | Human confirmation; optional independent digest | Same split as U1 |
| U4 | GitHub immutable release asset | Release/asset IDs, provider digest, dynamic tree manifest, attestation | Verify immutable release/asset again before Gate | Provider attestation or configured trust root | Same split as U1 |
| U5 | GitHub generated archive pinned to commit SHA | Exact commit plus computed archive digest and dynamic tree manifest | Resolve/fetch the same commit and recompute before Gate | Human-confirmed repository; no release-asset attestation | Same split as U1 |
| U6 | Local folder/archive | Resolved path plus computed archive/tree digest and dynamic manifest | Re-read the same path and recompute before Gate | Human-confirmed local provenance | Same split as U1 |
| U7 | Mutable `latest` link or branch head | `VERSION` only | Re-read locator metadata only | Human confirmation | Invocation-only knowledge |
| U8 | Versioned archive with same-package digest | Same-channel digest | Snapshot once and trust working copy | Same-channel checksum | All claims duplicated across every guide |
| U9 | Provider folder/tree | Provider metadata only | Provider-specific watcher/runtime | Provider account identity | Provider configuration schema in package |

## Findings

### E1: B2 is the only physical-common-parent family compatible with the frozen constraints

The eight-state fixture eliminates B1 because Full's one-key-kind file cannot contain Assisted UUID/mode records; it eliminates B4 because Full cannot move; B5 because two Assisted paths become simultaneous authorities; and B6 because deleting legacy state and stopping non-personalized conversation exceed the field contract. B3 is mechanically safe and more platform-conventional, but it has no one discoverable physical facility: on macOS and Linux the Full and Assisted registries stay in unrelated roots. B2 alone satisfies the owner-approved common facility as a concrete namespace while leaving Full unchanged.

B2's compatibility boundary is exact:

- Full continues to read/write only `<family-root>/bindings.yaml` using absolute project path → Full handle.
- Assisted reads/writes only `<family-root>/assisted/bindings.yml` using `schema_version: 1` and UUID → `fixed(participant)`/`ask`.
- Assisted never probes, imports, modifies, or locks the Full file; Full receives no product edit.
- The old `tfw-assisted` file is retained as inert local history and is never read as a fallback.
- A missing new entry triggers the existing human gate once; invalid or locked state is never repaired in place and falls back to session-only attribution.
- macOS/Linux documentation must explicitly identify `~/.tfw` as the TFW family-root exception and keep all field safety checks; no path alone proves the home directory is machine-local.

This narrows iteration 1 D2/D3 but does not supersede them.

### E2: Concrete provider matrix shows one invariant with provider-specific evidence grades

All executions were read-only or in-memory; no archive or fixture was written to disk.

| Source case | Concrete observation | Exact-object evidence available to this access path | Digest evidence | Dynamic manifest | Immediate recheck |
|---|---|---|---|---|---|
| Drive-mounted field folder | `H:\Shared drives\IT\Innoforce AI-First Knowledge\innoforce_starter_v1.6`; 28 files; 0 reparse points | None exposed by the filesystem mount; the path is a mutable locator | Computed per-file SHA-256 only | `6d76545790f6f899612dc3af80bb291e40569d4f7fa300d701fec0f3111ad214` | Second full read: same 28 files and same manifest |
| Drive blob/archive through API | Official API supports `fileId`; blob metadata may expose `version`, `modifiedTime`, and `sha256Checksum`; a retained earlier blob uses `revisionId` | File ID alone is not a byte identity; file + revision is stronger, subject to revision retention | Provider SHA-256 when available, then computed archive and tree digests | Required after safe extraction | Re-fetch the same revision or re-read head metadata/content; inability to retrieve the named revision is a blocker for an exact-revision claim |
| Current GitHub repository releases | Public Releases API returned `Count: 0` | No release ID, asset ID, immutable flag, asset digest, or release attestation exists for this repository today | None | N/A | A release-asset flow cannot be claimed for the current shelf |
| GitHub generated zipball pinned to `v2.0.0` commit | Tag API resolved `5a72b2bd420922d640d4c7f7ed0bf4507e9285af`; two in-memory downloads each had 13,580,705 bytes and 1,128 files | Exact commit SHA; not an uploaded release asset | Both archive reads: `5db6a9124136c5a950c2c3dea6476a79cc8d56d090cfc9ca88d52620922e5022`; provider digest absent | Both normalized trees: `b956987ca1207a80c79247ce6e6c779f9ecdadb2da5b10bb22f80e3a15a38f99` | Archive and manifest were identical on the second fetch; this observation is not a future immutability guarantee |
| Local current Assisted folder | Resolved workspace path; 26 files; 0 reparse points | Resolved path only; path contents are mutable | Computed per-file SHA-256 | `2cfc9a9a18ac6d1f008a09242412389b88b35cde83e0455f38f289b3827a1992` | Second full read: same 26 files and same manifest |

Google documents `files.get(..., alt=media)` and `revisions.get(fileId, revisionId, alt=media)` for blob download; GitHub documents that a Releases listing excludes tags without a release and that uploaded assets can expose `digest`. Sources: [Drive downloads](https://developers.google.com/workspace/drive/api/guides/manage-downloads), [GitHub Releases REST API](https://docs.github.com/en/rest/releases/releases), [GitHub repository archive endpoint](https://docs.github.com/en/rest/repos/contents#download-a-repository-archive-zip).

The provider-neutral rule is not “every provider exposes the same fields.” It is “record the strongest stable source identity the access path exposes, always compute the normalized tree manifest, and label missing assurance rather than invent it.”

### E3: The minimum generic acquisition record has mandatory and conditional fields

| Evidence item | Requirement | Provider-neutral meaning |
|---|---|---|
| Human-confirmed publisher and locator | Mandatory | Declares the current trust boundary; never inferred from folder name or account display |
| Source form and actual access means | Mandatory | Folder, archive, URL, attachment, cloud object, or other whole-package representation; no required connector/runtime |
| Claimed package version and eligible migration map | Mandatory | Read from the closed tree's `VERSION`, `CHANGELOG.md`, and `MIGRATION.md`; never taken from the locator name alone |
| Stable object identity | Conditional but recorded when exposed | Drive file/revision/version; GitHub repository + commit or release + asset; local resolved path is explicitly mutable |
| Provider or independently supplied digest/attestation | Conditional | Compared when available; absence is recorded, not synthesized as provider evidence |
| Computed acquisition digest | Mandatory for an archive/blob | Records the received bytes; does not authenticate their origin |
| Dynamic normalized tree manifest | Mandatory | Sorted relative path + size + SHA-256 after safe normalization; the common evidence for folder and archive forms |
| Pre-Gate recheck result | Mandatory | Re-resolve/re-read the source and target immediately before writes; any locator/object/tree/protected-state difference returns to Compare and requires a new Gate |

This contract uses capabilities rather than provider fields. It supports U1–U6 without putting Drive/GitHub configuration in the product. U7 fails to identify bytes; U8 cannot detect a post-snapshot change and its same-channel checksum adds no origin assurance; U9 violates the prompt-only provider-neutral boundary.

### E4: Integrity and origin form an assurance ladder, not one boolean

| Grade | What is established | What remains unproved |
|---|---|---|
| A0 — locator only | A human chose a location | Which bytes were read; whether they changed |
| A1 — computed digest/manifest | Exact bytes/tree observed at Compare and whether they changed at Recheck | Who published those bytes |
| A2 — provider object metadata/digest | Provider account/object supplied the observed bytes; stronger immutability when explicitly enabled | Publisher identity outside the provider trust/account boundary |
| A3 — independently obtained expected digest | Received bytes match a value from a second trusted channel | Long-term key identity and revocation unless the channel supplies it |
| A4 — verified signature/attestation with trusted root | Cryptographic origin/subject claim under a configured trust root | Compromise or policy errors inside that trust system |

The approved FA15ES contract requires A0 + A1 and consumes A2/A3 when available. It must not claim A4. GitHub immutable releases can expose an attestation path, but this repository currently has no releases; adding and governing a trust root or signature policy would be a separate security contract, not a hidden updater refinement.

### E5: Publisher-specific shelf documentation must live outside the replaceable service set

Gather's candidate `README.md` “Release source” subsection fails the persistence test: the field updater treats `README.md` as replaceable service content, so a downstream publisher's Drive choice could disappear on the next public overlay. The exact locus is instead split by authority:

| Claim | Exact authoritative locus | Why it survives and stays provider-neutral |
|---|---|---|
| Public TFW publisher's release shelf and naming convention | `editions/ASSISTED_MAINTENANCE.md`, a repository-level guide outside copied `02-assisted/` | Public maintainer authority; not replaced inside downstream projects |
| Any downstream producer's Drive/GitHub/other shelf | That producer's human-readable publisher documentation adjacent to/outside the installable package and target | The producer owns and preserves it; the core does not encode its provider or credentials |
| Consumer-visible accepted source forms and “ask once when absent” behavior | `editions/02-assisted/README.md` | Generic onboarding contract only; no shelf URL |
| Normative acquisition, evidence, Gate, recheck, and residual-risk behavior | `editions/02-assisted/.agents/skills/tfw-update/SKILL.md` | One prompt-only algorithm for every access form |
| Whole-package eligibility and exact protected-state transition | `editions/02-assisted/MIGRATION.md`, with release facts/maps retained in `CHANGELOG.md` | Version authority, not source discovery |
| Public → downstream and reviewed downstream → public promotion | `editions/ASSISTED_MAINTENANCE.md` | Repository-level maintainer route; may point to the public shelf without duplicating updater mechanics |

When no publisher document is available, `/tfw-update` keeps the field behavior and asks exactly where the new package is. This is a usable fallback, not a hidden default. No new package file, provider schema, or persistent locator registry is needed.

### E6: The rejected JSON pair still has no unique job after fixture execution

The dynamic manifest performed the byte-accounting job for all three actual access forms. `VERSION`/`CHANGELOG.md`/`MIGRATION.md` performed version and migration authority; human confirmation and optional provider/out-of-band evidence performed the trust job; the updater performed normalization, Gate, and recheck. A same-package static manifest can be useful as publisher metadata but cannot authenticate its own distribution, and it is not necessary to recompute the target/source snapshot. `maintenance-policy.json` duplicates prose authority and provider-independent classification. Neither file is required by any surviving U1–U6 family.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| B2 is the only concrete common-parent layout satisfying Full non-interference; the fixture defines exact one-time re-onboarding, invalid, lock, shared, and autonomous behavior. | Stress-test stale/new substitution and the POSIX family-root exception against safety and wording ambiguity. |
| Drive-mounted, GitHub commit archive, and local folder cases all support a mandatory dynamic manifest/recheck despite different exact-object and digest evidence. | Inject same-version byte substitution and mutable-locator changes; decide whether A0+A1 is an honest sufficient boundary. |
| Publisher shelves must be documented outside the replaceable package service set; current public GitHub repository has tags but zero Releases. | Attempt to delete or merge documentation loci without losing an authority; state any release-publication gap precisely. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: Pre-authorized continuation to Challenge; no contract blocker found.
