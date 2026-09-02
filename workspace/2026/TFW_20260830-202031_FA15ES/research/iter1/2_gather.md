# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> Goal: Restore field-proven Assisted 1.6 as an independent TFW realization while preserving isolated Full/Assisted identity semantics and a human-gated update path whose publisher chooses the release source.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: Device-store topology | Keep Full and Assisted sibling product roots | Put Assisted under Full's existing local-state parent | Put both schemas in one polymorphic file | Add a configurable common state root |
| D2: Existing Assisted-binding transition | Leave legacy location canonical | Re-onboard and create only at the new location | Guarded one-time copy to the new location | Permanent precedence-based dual read |
| D3: Publisher source-selection locus | Source supplied per update invocation | Human-readable publisher source in product documentation | Machine/project configuration field | Structured release-source manifest |
| D4: Published release object | Versioned folder tree | One versioned archive file | Git commit/tag tree | Provider-native snapshot/export |
| D5: Release identity | Mutable `latest` locator | Semantic version plus locator | Immutable provider object/release ID | Content digest plus version |
| D6: Trust and integrity proof | Structural package checks only | Provider checksum/digest | Publisher-provided digest outside the package | Cryptographic signature/attestation |

The dimensions are independent enough to expose combinations that the HL did not preselect: a common local parent does not require a combined schema; a Drive folder does not require a Drive-shaped core contract; and a content digest does not by itself identify an authorized publisher.

## Findings

### G1: Full and Assisted bindings have different jobs, keys, schemas, and write protocols

The current Full contract (`.tfw/templates/bindings.yaml`; `.tfw/conventions.md` §4) is deliberately one-job state: an absolute project path maps to a human handle in that project's `team/`. On Windows it is `%LOCALAPPDATA%\tfw\bindings.yaml`; on POSIX it is `~/.tfw/bindings.yaml`. The template explicitly says that a second key kind is a design change. It does not carry a schema version, Assisted `project_id`, `fixed`/`ask`, or Assisted's reservation protocol.

Field Assisted 1.6 (`.agents/skills/tfw-identity/SKILL.md`) instead stores a versioned list keyed by canonical UUID `project_id`; each entry is `fixed + participant` or `ask`; it rejects unknown fields, duplicate projects, unsafe/shared locations, and active foreign reservations, and writes through an exclusive reservation plus strict post-read. It explicitly does not read, import, or modify Full state. Therefore “one facility” cannot mean one mixed mapping file without changing Full's frozen one-key-kind contract and Assisted's validation semantics.

### G2: A shared parent with implementation-owned children is structurally possible, but its cross-platform baseline is constrained by Full

Windows defines `FOLDERID_LocalAppData` as a per-user known folder at `%LOCALAPPDATA%` ([Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid#folderid_localappdata)). Linux's `$XDG_STATE_HOME` is specifically for per-user state that persists across restarts but is not portable enough for the data home ([XDG Base Directory Specification](https://specifications.freedesktop.org/basedir/0.8/)). Apple recommends app-specific subdirectories under the user's `Library/Application Support` directory ([Apple File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html)). These sources support isolated product subdirectories; they do not support merging unrelated schemas.

No-Full-change is the binding constraint. A physical common parent must be anchored to Full's existing location (`%LOCALAPPDATA%\tfw` on Windows and `~/.tfw` on POSIX), with Assisted owning a child such as `assisted/bindings.yml`. That would move Assisted away from its 1.6 location on every platform and away from the platform-preferred state root on macOS/Linux. Alternatively, “facility” can remain the OS per-user application-state area, with sibling product roots, preserving both current locations but offering no single TFW subdirectory.

### G3: Existing Assisted `/tfw-update` is already transport-neutral at acquisition time

Field 1.6 accepts a path, archive, URL, attachment, cloud object, or another accessible representation, obtains it into a new safe temporary area, refuses authorization bypass, and normalizes it to one closed package tree without executing source code. It then verifies one root, `VERSION`, `CHANGELOG.md`, the service/protected manifests, package cleanliness, and the exact version-specific migration map before one human write gate. `MIGRATION.md` and `CHANGELOG.md` carry the release and migration contract. The updater has no provider API, downloader, or unpacker dependency.

The missing H4 decision is therefore not how to teach the core updater Google Drive versus GitHub. It is how the publisher communicates an authorized source and how an invocation selects one exact release object. Provider-specific access remains an environment capability and may fail with a precise request for another representation.

### G4: Google Drive supplies stable object identity and file checksums, but a folder name is neither unique nor an atomic release digest

Drive file IDs are opaque and stable for the life of the file even when its name changes, while names need not be unique ([Google Drive files overview](https://developers.google.com/workspace/drive/api/guides/about-files)). The `files` resource exposes SHA-256 for stored binary content when available, but not for Google Docs or shortcuts ([Drive `files` resource](https://developers.google.com/workspace/drive/api/reference/rest/v3/files)). Binary content can be fetched by file ID; Google Workspace documents require export instead ([Drive `files.get`](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/get)).

A Drive folder can therefore be a publisher's human-facing release shelf, but a single versioned binary archive inside it has stronger portable identity than the folder tree itself. The core contract can consume the resulting archive/tree without depending on Drive IDs, API fields, or OAuth semantics.

### G5: GitHub releases expose version and asset digests, but immutability is a separate, opt-in property

GitHub's Releases API exposes `tag_name`, release IDs, downloadable assets, asset sizes, SHA-256 `digest`, and an `immutable` property ([GitHub REST Releases](https://docs.github.com/en/rest/releases/releases)). GitHub documents immutable releases as locking the associated tag and assets and creating a release attestation, but the repository or organization must enable that policy for future releases ([GitHub immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases)). A normal release or tag must not be treated as immutable merely because it has a version-shaped name.

GitHub can publish the same single-archive contract as Drive. Provider-native digest or attestation can strengthen evidence, but portability requires the updater to compute and report its own package/tree manifest after acquisition.

### G6: Trust, integrity, completeness, and version compatibility are separate claims

- A human-confirmed source answers “which publisher/location do I trust?” but not whether transfer bytes are complete.
- A digest answers “are these the expected bytes?” only when the expected digest comes from an independently trusted channel or provider metadata; a checksum stored solely inside the same package is self-describing, not publisher authentication.
- `VERSION` plus the package markers answer “what does this package claim to be?”
- `CHANGELOG.md` plus `MIGRATION.md` answer “what exact transition may touch protected state?”
- Pre/post manifests answer “what did this update actually change?”

The current `editions/maintenance/release-manifest.json` and `maintenance-policy.json` combine these jobs into two new schemas, duplicate version/path/migration authority already present in Assisted 1.6, describe repository-relative `02-assisted/` rather than the standalone copied root, and remain unsigned inside the same distribution boundary. They may detect accidental file loss, but they do not independently establish publisher identity.

### G7: Gather decision

Proceed to Extract with all six dimensions. The evidence closes the Briefing's discovery gap: H2a is a namespace/layout and legacy-transition problem, not a shared-schema problem; H4 is an authorized-locator and exact-release-object problem, not a provider adapter problem. No frozen HL claim needs to move to analyze the viable combinations.

## OODA Loop 1

- **Observe:** Compared the Full binding template/workflow, field Assisted 1.6 identity/update/MIGRATION/CHANGELOG contracts, the rejected maintenance JSON pair, and primary OS/Drive/GitHub documentation.
- **Orient:** The local contracts confirm implementation independence; external sources challenge the idea that a folder/tag name alone identifies immutable release bytes.
- **Decide:** Generic sufficiency is met: external sources were used, the discovery gap is closed, and six independent dimensions with at least three alternatives each are recorded.
- **Act:** Carry the dimension names unchanged into Extract and construct only combinations consistent with the frozen no-Full-change/no-runtime boundary.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Independent schemas can coexist only through namespace isolation; provider-neutral acquisition already exists; Drive/GitHub both favor an exact versioned archive object over mutable names/folder trees. | Compare viable combinations; define the smallest universal source contract; choose a backward-compatible Assisted binding transition; stress-test mutability, legacy state, and access failure in later stages. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?

Stage complete: YES
→ User decision: Proceed under the Coordinator's pre-authorized full-iteration delegation; final design remains a Researcher recommendation only.
