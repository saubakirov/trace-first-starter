# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> Goal: Assisted 1.6 remains a faithful independent TFW realization while Full and Assisted coexist on one device and publishers choose update sources without provider-specific product machinery.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D _(if any)_ |
|-----------|-------|-------|-------|-----------------|
| D1: Physical binding layout | One combined Full/Assisted YAML | Separate implementation-owned files under one physical TFW parent | Separate platform-native roots presented as one conceptual facility | New standalone common root requiring both implementations to move |
| D2: Legacy Assisted handling | Automatic copy/merge | Permanent dual read | Preserve and ignore; one-time re-onboarding at canonical new path | Delete after transition |
| D3: Unresolved local state | Fail open to legacy/default | Repair or overwrite the new file | One human question, then session-only with no persistent write | Stop all conversation |
| D4: Host placement | Current Full path is the cross-platform family root | Each OS's preferred application-state root | User-configured root | Project/shared/sync root |
| D5: Source representation | Versioned archive/blob | Provider folder/tree | Local folder/archive | Mutable `latest` link or branch head |
| D6: Exact-byte evidence | Computed dynamic path/size/SHA-256 manifest | Provider object/revision metadata and digest | Independently published expected digest | No byte evidence beyond `VERSION` |
| D7: Recheck model | Re-read only locator metadata | Re-fetch or re-read exact object plus full manifest immediately before Gate | Snapshot once and trust the working copy | Provider-specific runtime watches the source |
| D8: Origin assurance | Human-confirmed publisher/location | Digest obtained with the same package | Digest or attestation from an independent trusted channel | Cryptographic signature/attestation anchored in a configured trust root |
| D9: Documentation ownership | Publisher shelf in public Assisted README; consumer acquisition in `/tfw-update`; version migration in `MIGRATION.md`; cross-product promotion in Editions maintenance guide | All claims duplicated across every guide | Provider configuration schema in the package | Invocation-only oral/interactive knowledge |

## Findings

### G1: The Windows common parent is concrete and leaves Full byte-for-byte untouched

The Full template fixes Windows at `%LOCALAPPDATA%\tfw\bindings.yaml` and permits exactly one absolute-project-path → handle mapping kind. On this host, .NET resolved the known folder to `C:\Users\c0rpa\AppData\Local`; the synthetic B2 resolution was:

| Authority | Resolved path |
|---|---|
| Full, unchanged | `C:\Users\c0rpa\AppData\Local\tfw\bindings.yaml` |
| Assisted, proposed | `C:\Users\c0rpa\AppData\Local\tfw\assisted\bindings.yml` |
| Assisted, field legacy | `C:\Users\c0rpa\AppData\Local\tfw-assisted\bindings.yml` |

The read-only fixture asserted that Full's resolved path still equals the template path and that the Assisted path's parent is exactly `...\tfw\assisted`. Microsoft defines `FOLDERID_LocalAppData` as a per-user known folder with default `%USERPROFILE%\AppData\Local`, which supports the current Windows placement; it does not itself prove that an arbitrary redirected location is private or safe. Source: [Microsoft KNOWNFOLDERID](https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid#folderid_localappdata).

### G2: The eight-state binding fixture closes the missing/new/legacy behavior gap

An in-memory state table exercised eight cases and rejected any row that read or wrote the Full file or read, wrote, merged, or deleted the legacy Assisted file. The assertion completed with `Cases: 8` and `CrossImplementationAccess: 0`.

| Case | Canonical-new behavior | Persistent effect |
|---|---|---|
| New missing; legacy `fixed(alice)` | Ask once; legacy is not consulted | After a validated personal-device answer, create only the current project's new `fixed` entry |
| New valid `fixed(alice)` | Strictly validate and select `alice` | None |
| New valid `ask`; legacy `fixed(alice)` | Ask every new chat | Retain `ask`; no participant is pinned |
| New `fixed(bob)`; legacy `fixed(alice)` | Select `bob` | None; new path is sole Assisted authority |
| New malformed | Ask, but treat persistence as unsafe | Session-only; do not overwrite invalid state |
| Foreign new-file lock | Do not read/return the saved participant | Ask and continue session-only; do not remove lock or write |
| New missing on shared device | Ask | Create only a new `ask` entry after validation |
| Autonomous handoff/review | Skip human onboarding | No local binding reads or writes |

This preserves the field 1.6 semantics: only a fully valid `fixed` selects a participant; `ask`/missing/invalid lead to one natural question; a foreign reservation is unresolved; a shared device stores `ask`; an autonomous role skips local identity; failure to prove a safe write yields session-only attribution. Re-onboarding is therefore not migration: it creates one new canonical entry for the current project only after the same existing human gate.

### G3: POSIX portability is a documented exception, not a safety failure

| Host | Full today | Field Assisted today | B2 canonical Assisted | Portability consequence |
|---|---|---|---|---|
| Windows | `%LOCALAPPDATA%\tfw\bindings.yaml` | `%LOCALAPPDATA%\tfw-assisted\bindings.yml` | `%LOCALAPPDATA%\tfw\assisted\bindings.yml` | Remains inside the OS local application-data facility |
| macOS | `~/.tfw/bindings.yaml` | `~/Library/Application Support/tfw-assisted/bindings.yml` | `~/.tfw/assisted/bindings.yml` | Departs from Apple's preferred Application Support directory to join Full's existing family root |
| Linux/Unix | `~/.tfw/bindings.yaml` | `${XDG_STATE_HOME:-~/.local/state}/tfw-assisted/bindings.yml` | `~/.tfw/assisted/bindings.yml` | Departs from the XDG state base to join Full's existing family root |

The XDG specification says persistent user-specific state belongs under absolute `$XDG_STATE_HOME`, defaulting to `~/.local/state`; Apple assigns app-managed support/state data to an app-specific subdirectory of `~/Library/Application Support`. Sources: [XDG Base Directory Specification 0.8](https://specifications.freedesktop.org/basedir/0.8/), [Apple File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html).

B2 is still portable because its POSIX form uses ordinary home-relative files and exactly the Full location already shipped by this repository. It is less platform-conventional than field Assisted. The product text must name the family-root exception explicitly; it must retain the field checks that reject a shared/synchronized root, symlink/reparse escape, unreadable/non-regular state, and unprovable exclusive reservation. A path convention alone cannot prove machine locality on a network-mounted home, so session-only fallback remains mandatory on every OS.

### G4: Drive supplies useful identity and integrity signals but not a permanent immutable release by default

For a Drive blob, the Files resource can expose an object `id`, `modifiedTime`, `version`, and `sha256Checksum` when available. A Drive object ID is a locator, while bytes can change; folder membership and child content are separate mutable objects. Older blob revisions may be automatically purged unless marked `keepForever`, and only a bounded number can be retained. A Drive folder must therefore be normalized into a closed local tree and described by a dynamic manifest; an archive/blob can additionally record its exact object/revision and provider checksum. Sources: [Drive files resource](https://developers.google.com/workspace/drive/api/reference/rest/v3/files), [Drive revision management](https://developers.google.com/workspace/drive/api/guides/manage-revisions).

### G5: GitHub immutability is a release property, not a consequence of using a release-shaped URL

GitHub documents that an immutable release locks its associated tag and assets and produces a release attestation. It separately warns that integrity verification of a local asset applies to uploaded release assets, not automatically generated source archives. Therefore a normal tag, branch, ordinary release, or generated `zipball`/`tarball` remains a mutable or insufficient exact-object claim unless the publisher documents and the consumer verifies the stronger property. Source: [GitHub immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases), [GitHub release integrity verification](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/verify-release-integrity).

### G6: Same-channel SHA-256 is change evidence, not publisher authentication

The field updater's dynamic `relative path + size + SHA-256` manifests can prove that the source stayed byte-identical between Compare and the pre-Gate recheck and can make a folder equivalent to an archive for update planning. A digest delivered alongside substituted bytes merely describes those substituted bytes. Origin assurance begins only when the expected digest or attestation is obtained through a separately trusted channel or verified against an already configured trust root. H4's approved human-gated scope can honestly retain human source confirmation plus available integrity evidence, but it must label package-origin substitution as residual risk rather than claiming cryptographic authentication.

### G7: Four documentation jobs already have four natural owners

The field Assisted `README.md` already tells consumers that `/tfw-update` accepts a path, archive, URL, cloud link, attachment, or other accessible complete-package representation. The field `/tfw-update` skill already owns normalization, static validation, exact migration-map selection, the human Gate, and recheck. `MIGRATION.md` already owns version-specific source eligibility and protected-state maps. `editions/ASSISTED_MAINTENANCE.md` already owns the public ↔ downstream maintainer route, but currently duplicates the rejected static JSON authority. The minimum locus is therefore:

1. Assisted `README.md`: publisher fills one short “Release source” subsection naming its human-readable shelf and release naming convention; no provider schema.
2. Assisted `/tfw-update`: generic consumer acquisition/evidence contract, including exact-object recording, available digest, dynamic manifest, recheck, and honest authentication boundary.
3. Assisted `MIGRATION.md`: whole-package/version-specific eligibility only; link to the updater for acquisition.
4. Editions maintenance guide: asymmetric public ↔ downstream promotion and repository-specific public shelf; delete JSON authority wording rather than duplicating updater mechanics.

No fifth file has a unique job. `CHANGELOG.md` remains release history/migration-map evidence, not a current source locator.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| The Windows path and eight binding states validate independent authority and one-time re-onboarding; POSIX B2 is safe only as an explicit family-root convention plus existing fail-closed checks. | Cross-reference the dimensions, run concrete Drive/GitHub/local manifest/recheck fixtures, and test same-version substitution and origin claims. |
| Drive, GitHub, and local sources expose different locator/immutability metadata but can all normalize to one closed tree and dynamic manifest. | Determine which exact-object and digest fields are required, conditional, or unavailable for each provider case. |
| The four documentation claims have distinct existing owners; the static JSON pair has no remaining unique job. | Challenge whether any locus can be removed or any claim must rise to a frozen amendment. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?

Stage complete: YES
→ User decision: Pre-authorized continuation to Extract; no contract blocker found.
