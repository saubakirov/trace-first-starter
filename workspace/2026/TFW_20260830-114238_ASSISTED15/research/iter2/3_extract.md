# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260830-114238_ASSISTED15](../../HL-TFW_20260830-114238_ASSISTED15.md)
> Predecessor: [Iteration 2 Gather](2_gather.md)
> Goal: Select one implementation-ready configuration for all five iteration threads, reject unsafe or needlessly expansive alternatives, and leave only adversarial verification work for Challenge.

## Configuration Space

The full Cartesian product is much larger than 30 rows. These configurations preserve at least one non-default alternative and expose the meaningful cross-dimension interactions. Evaluation follows in Findings.

| Config | D1: locality authority | D2: locality result | D3: path identity | D4: release serialization | D5: maintenance-policy selector | D6: operation-report visibility | D7: template customization | D8: asset/font delivery | D9: role orchestration | D10: retry/interruption | D11: public history authority | D12: privacy evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X1 | OS roots only | proven/unsafe/unknown | portable NFC + casefold | stored JCS | exact paths only | private + derived public | CSS variable overlay | system fonts + neutral local asset | unified runtime adapter + manual | same-session follow-up; optional interrupt | public Assisted only | scan + schema + semantic review |
| X2 | OS roots + declared custom root | proven/unsafe/unknown | portable NFC + casefold | stored JCS | exact + prefix, specificity ordered | private + derived public | CSS variable overlay | system fonts + neutral/custom local asset | unified runtime adapter + manual | same-session follow-up; optional interrupt | public Assisted only | scan + schema + semantic review |
| X3 | operator declaration only | proven/unsafe/unknown | exact UTF-8 | pretty JSON | ordered first-match prefix | one private report | stock-hash in-place | local/remote mixed | external session manager | replacement sessions | public + generic provenance | marker scan only |
| X4 | runtime volume/mount only | local/nonlocal | platform-native | line tuples | expanded exact table | counts-only | immutable stock + copies | vendored fonts/assets | Responses adapter only | interrupt then follow-up | tags only | schema suppression |
| X5 | OS roots + declared custom root | proven/unsafe/unknown | portable NFC + casefold | stored JCS | exact + prefix, first-match | private + derived public | JSON compiled theme | system fonts + embedded asset | Codex task adapter only | wait then same-session follow-up | public Assisted only | scan + schema + semantic review |
| X6 | session-only | unsupported | portable NFC + casefold | repository tree object | exact paths only | public redacted only | CSS variable overlay | system fonts + neutral local asset | manual protocol only | user-routed same sessions | public Assisted only | semantic review |
| X7 | OS roots + declared custom root | proven/unsafe/unknown | portable NFC + casefold | stored JCS | exact + prefix, specificity ordered | private + derived public | stock-hash in-place | system fonts + neutral local asset | unified runtime adapter + manual | same-session follow-up; optional interrupt | public + generic provenance | scan + schema + semantic review |
| X8 | OS roots + declared custom root | proven/unsafe/unknown | portable NFC + casefold | stored JCS | expanded exact table | private + derived public | CSS variable overlay | system fonts + neutral/custom local asset | unified runtime adapter + manual | create replacement on lost handle | copied downstream history | source not inspected |

## Findings

### E1 — OODA Loop 1: `X2` locality with a bounded operational proof model

**Observe.** Microsoft explicitly assigns machine-specific application data to `FOLDERID_LocalAppData`; Apple exposes local-volume and iCloud/ubiquitous item signals; XDG describes persistent state but reserves a normative local/non-shared guarantee for the non-persistent runtime directory. A mount or volume signal still cannot enumerate every user-space copier: [Windows machine-specific app data](https://learn.microsoft.com/en-us/windows/apps/develop/windows-app-restore), [Apple `volumeIsLocalKey`](https://developer.apple.com/documentation/foundation/urlresourcekey/volumeislocalkey), [Apple `isUbiquitousItemKey`](https://developer.apple.com/documentation/foundation/urlresourcekey/isubiquitousitemkey), [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/), [Linux proc filesystem](https://www.kernel.org/doc/html/latest/filesystems/proc.html).

**Orient.** `X1` is attractive but cannot produce persistent identity on a Linux home whose mount is local while the XDG contract remains silent about sharing. `X3` trusts a declaration without mechanical evidence. `X6` is universally safe but unnecessarily discards the frozen persistent binding where platform evidence is adequate. The useful combination not explicit in Briefing is hybrid `X2`: documented OS roots where they have machine-local semantics, an explicitly declared root only when the OS default cannot establish those semantics, and session-only fallback for every unresolved predicate.

**Decide.** Select `operational-local-v1`, with `proven` meaning proven against this explicit threat model:

- prevents default placement inside the package, installed project, source tree, declared shared root, known provider root, remote/network mount, or iCloud ubiquitous namespace;
- prevents a visible symbolic-link/junction/reparse ancestor and non-regular store target;
- requires a current-user app directory with no broad write grant and a platform adapter capable of lock, same-directory temporary write, atomic replacement, and operation-time revalidation;
- revalidates before every persistent read/write and drops to session-only if evidence changes;
- does **not** claim to prevent a malicious same-user process, an undeclared synchronizer, or a provider installed after the probe from copying an otherwise local directory.

The platform contract is exact:

| Platform/root | Required positive evidence | Result on full pass | Result on missing evidence |
|---|---|---|---|
| Windows `FOLDERID_LocalAppData/TFW/Assisted` | OS-known root; `DRIVE_FIXED`; outside project/source/declared and registered provider roots; link/reparse-free ancestors; private app directory; safe platform primitive | `proven` | `unknown` |
| macOS `~/Library/Application Support/TFW/Assisted` | application-support root; `volumeIsLocal=true`; `isUbiquitous=false`; same exclusions, ancestor, permissions, and primitive checks | `proven` | `unknown` |
| Linux `XDG_STATE_HOME/tfw-assisted` | state category and local mount are useful but insufficient without explicit non-shared assertion | `proven` only when the explicit root/attestation contract below also passes | `unknown` |
| Explicit custom root on any platform | operator sets a dedicated Assisted root and affirms non-shared/non-synchronized; platform proves local non-remote volume/mount and all mechanical checks | `proven` under declared-root trust boundary | `unknown` |
| Any root with a positive shared/remote/provider/link/permission disqualifier | one or more unsafe predicates | `unsafe` | not applicable |

The implementation-facing decision order is:

```text
1. If candidate is absent: unknown -> session-only.
2. If any positive disqualifier is true: unsafe -> session-only, zero persistent writes.
3. If any required predicate is false, unsupported, stale, or not observed: unknown -> session-only.
4. If the platform row's complete positive set passes: proven -> persistence allowed.
5. Re-run 2–4 at every binding operation; never upgrade unknown from a cached prior result.
```

The explicit-root assertion is admissible only as one named predicate, never as a substitute for mount/volume, root-containment, ancestor, permissions, or safe-primitive evidence. The public diagnostic uses enum/check booleans and omits the real root.

**Act.** Reject `X1` as needlessly non-persistent on otherwise valid Linux/custom installations, reject `X3` as assertion-only, and retain `X6` as the mandatory runtime outcome whenever `X2` cannot prove every predicate.

### E2 — OODA Loop 1: non-circular record binding and deterministic policy precedence

**Observe.** RFC 8785 gives repeatable JSON bytes but explicitly preserves string data without Unicode normalization and requires ecosystem correctness checks before acting. JSON Schema can close structural properties but cannot prove cross-record authority. TUF's separation of target integrity and version-consistent metadata reinforces the need to bind versions and hashes without making one mutable report authoritative: [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html), [JSON Schema 2020-12 core](https://json-schema.org/draft/2020-12/json-schema-core), [TUF metadata](https://theupdateframework.io/docs/metadata/).

Gather's `MP1` contained `to_manifest_sha256` inside a policy file that the manifest itself would hash. That creates a cycle:

```text
manifest bytes -> policy file hash -> policy bytes -> to_manifest_sha256 -> manifest bytes
```

**Orient.** Excluding both manifest and policy would remove the cycle but weaken release binding. Adding a fourth signed descriptor would exceed the selected three-record contract. A line-tuple manifest would still have the same authority cycle. The cycle disappears if the current manifest binds the current policy, while the current policy binds only accepted **prior** release manifests.

**Decide.** Select this exact binding:

1. Store `release-manifest.json` as canonical JCS UTF-8 bytes; validate it against a closed JSON Schema and `portable-nfc-v1` before use.
2. `files[]` includes every public payload file, including `maintenance-policy.json` and the three schemas, but excludes `release-manifest.json` itself.
3. `files[]` is sorted by validated canonical relative path. `payload_tree_sha256 = SHA-256(JCS(files))`.
4. The operation computes `release_manifest_sha256 = SHA-256(raw canonical release-manifest.json bytes)`; Git/review may establish provenance, but the manifest contract claims integrity, not origin authentication.
5. `maintenance-policy.json` contains only `from_manifest_sha256` for accepted prior releases plus `from_version`, `to_version`, and migration/rule data. It has no `to_manifest_sha256` or current-manifest hash.
6. The current release manifest binds the policy file hash. The operation report binds both current manifest hash and policy hash and verifies that manifest version, `VERSION`, policy `to_version`, and latest public changelog entry agree.

The selected release fields are:

```json
{
  "schema_version": 1,
  "record_type": "assisted-release-manifest",
  "edition": "assisted",
  "release_version": "1.5",
  "content_language": "ru",
  "path_profile": "portable-nfc-v1",
  "hash_algorithm": "sha256",
  "interfaces": {"template_theme": 1, "role_adapter": 1},
  "files": [],
  "payload_tree_sha256": "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
}
```

The hash above is a fixed synthetic fixture value rather than a release value; the generated record must contain exactly 64 lowercase hexadecimal characters computed from its real `files` array. The parser/schema/domain-validation pipeline rejects extra fields, duplicate keys, non-integer/non-safe `bytes`, unknown algorithms, unsorted arrays, and any path outside `portable-nfc-v1`.

Policy precedence is selected as **specificity ordered, not first-match semantics**:

- selectors are only `exact` or directory `prefix`; globs are forbidden;
- resolution chooses exact match first, otherwise the longest matching prefix;
- duplicate exact selectors, duplicate prefixes, equal-specificity competing matches, and prefix strings not ending `/` reject the policy;
- the stored `rules[]` array must be sorted by descending selector length, `exact` before `prefix`, then selector value and rule ID for deterministic review;
- reordering the array cannot change the resolver result, but noncanonical order still fails validation;
- a source-manifest path with no rule stops before write; a target-only unclassified path is preserved byte-for-byte and excluded from reverse promotion;
- only the three exact known retired hook paths may use `remove-if-known-stock`; no rule retires the whole `.codex/` prefix;
- a modified stock-customizable path is preserved. The operation continues only when the new release declares its old interface compatible; otherwise the whole operation stops before the first write.

Selected transition fragment:

```json
{
  "from_version": "1.0",
  "to_version": "1.5",
  "from_manifest_sha256": "dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
  "compatible_interfaces": {"template_theme": [1], "role_adapter": [1]}
}
```

The implementation replaces the descriptive hash string with generated lowercase hexadecimal; schemas and fixtures use a fixed synthetic 64-hex value. No release accepts a version label alone as a baseline.

**Act.** Reject pretty JSON plus an implicit canonicalization step as a two-byte-representation trap, reject repository tree objects as a standalone installed-project contract, reject first-match policy semantics as reorder-sensitive, reject globs as platform-ambiguous, and retain expanded exact tables only as a generated diagnostic view rather than policy authority.

### E3 — OODA Loop 2: private report is authoritative evidence; public report is a one-way projection

**Observe.** NIST treats PII protection as context-dependent confidentiality, while OWASP notes that operational records may contain personal, technical, and business-sensitive information and may require exclusion rather than hashing. A stable hash of a private path can still support dictionary matching, so hash substitution is not redaction: [NIST SP 800-122](https://csrc.nist.gov/pubs/sp/800/122/final), [OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).

**Orient.** A single redacted report cannot support recovery; a single detailed report cannot be safely published. Manually writing two reports invites disagreement. `X2` therefore uses one private immutable operation record and a deterministic, schema-closed public projection. Projection is one-way: public data never reconstructs or links to private path/hash material.

**Decide.** Select two visibility schemas under the one operation-report concept.

Private record minimum:

```json
{
  "schema_version": 1,
  "record_type": "assisted-operation-report",
  "visibility": "private",
  "operation_id": "fixture-private-forward-001",
  "direction": "public-to-downstream",
  "source_version": "1.5",
  "target_version_before": "1.0",
  "target_version_after": "1.5",
  "release_manifest_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "maintenance_policy_sha256": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
  "status": "verified",
  "mutation_started": true,
  "baseline_tree_sha256": "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",
  "entries": [],
  "verification": {
    "version_agrees": true,
    "public_core_matches_manifest": true,
    "owned_target_bytes_preserved": true,
    "unexplained_changes": 0
  },
  "recovery": {"required": false, "journal_record_id": null},
  "public_projection_sha256": "dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
}
```

Private `entries[]` may contain destination-relative path, pre/post SHA-256, rule ID, authority, sensitivity, action, and outcome. Absolute roots, usernames, device IDs, and secrets remain unnecessary even privately.

The immutable state machine is:

```text
planned -> gated -> applying -> verified
planned|gated -> aborted                 (zero mutations)
applying -> partial                      (one or more mutations, verification incomplete/failed)
partial -> [new recovery operation]      (original report remains partial)
```

Before `applying`, the private recovery journal and pre-write hashes exist. `verified` requires zero unexplained changes. Failure after the first mutation is always `partial`; later recovery creates a new linked private report rather than editing history.

Public projection algorithm `public-projection-v1`:

1. Validate the complete private report and its referenced current manifest/policy.
2. Copy only closed allowlisted release fields: record/schema version, direction, public source/target versions, status, mutation-started, rule IDs, public verification booleans, aggregate counts, and `recovery.required`.
3. Include a relative path only when policy marks the rule `sensitivity=public` and authority is `public-core`, `stock-customizable`, or exact `retired`; never include downstream/unknown path or any path hash.
4. Aggregate excluded entries by public enums only. Do not emit private rule names, timestamps, roots, IDs, filenames, raw counts judged uniquely identifying, or hashes of omitted values.
5. Sort public arrays canonically, JCS serialize the body without ID, and set `public_report_id = SHA-256(JCS(body_without_id))`.
6. Run the synthetic private-token/hash scan and an independent semantic privacy review before export. Reverse-promotion reports cannot be public until reviewer acceptance.
7. Store `SHA-256(raw public report bytes)` only in the private report. The public report contains no private report ID or reverse link.

For `partial`, the public projection exposes `status=partial` and `recovery.required=true` but no private journal identifier. A counts-only projection is allowed only when semantic review rejects even public path detail; it is not the default evidence level.

**Act.** Reject one private report with ad hoc redaction, reject a public-only report as insufficient for recovery, reject hashing private paths as sanitization, and retain private→public derivation plus independent semantic review as the selected contract.

### E4 — OODA Loop 2: select TI1 with a fixed interface and a stock-customizable overlay

**Observe.** CSS Custom Properties provide a stable override vocabulary with fallback values, and CSS font-family lists can end in generic/system families. Neither mechanism proves pagination, glyph coverage, or privacy; those remain render/review obligations: [CSS Custom Properties](https://www.w3.org/TR/css-variables-1/), [CSS Fonts 4](https://www.w3.org/TR/css-fonts-4/), [CSS Paged Media 3](https://www.w3.org/TR/css-page-3/), [SVG 2 structure](https://www.w3.org/TR/SVG/struct.html).

**Orient.** TI2 creates a clean compiler but changes the current static-presentation workflow and adds a second generation responsibility. TI3 preserves paths but keeps theme and brand mixed inside every customized template. TI1 can preserve the field builder's first three positional arguments, add a versioned interface, and let updates preserve customized visuals independently from template logic.

**Decide.** Select TI1 with these path authorities:

| Path | Authority | Contract |
|---|---|---|
| `шаблоны/theme-interface.json` | public-core | schema/version and fixed overlay path contract |
| `шаблоны/theme.css` | public-core | complete neutral layout and default variable values |
| `шаблоны/overlay/theme.css` | stock-customizable | shipped neutral/empty overrides; downstream colors/fonts only |
| `шаблоны/overlay/mark.svg` | stock-customizable | shipped neutral mark; downstream may replace; update hash-protects |
| `шаблоны/build_a4.py` | public-core | deterministic local builder; first three positional args preserved |
| note, work-plan, A4 source, presentation | stock-customizable | complete neutral Russian examples; modified installed copies preserved |

`theme-interface.json` selected fields:

```json
{
  "schema_version": 1,
  "interface": "assisted-template-theme",
  "interface_version": 1,
  "core_css": "theme.css",
  "overlay_css": "overlay/theme.css",
  "mark": "overlay/mark.svg",
  "network_resources": "forbidden",
  "required_variables": [
    "--tfw-font-sans",
    "--tfw-font-mono",
    "--tfw-text",
    "--tfw-muted",
    "--tfw-accent",
    "--tfw-surface"
  ]
}
```

The builder interface is exact:

```text
python build_a4.py SOURCE OUTPUT TITLE [--theme-css LOCAL_FILE] [--asset LOCAL_FILE]
```

- the original first three positional arguments retain their meaning;
- default core/overlay/mark paths resolve from the template directory, not the caller's current directory;
- explicit overrides must be readable local regular files; URLs, missing files, links escaping the allowed local root, CSS `@import`, and any `http:`/`https:` reference fail nonzero;
- core and overlay CSS plus the selected SVG bytes are embedded into the A4 output, so the generated HTML is self-contained offline;
- presentation source links the same local core/overlay CSS and local mark and has no required network resource;
- stock system-font stacks are used; no pixel-identical promise is made across renderers;
- neutral/default and custom overlay outputs both undergo V9 render and privacy evidence.

A modified overlay or template is preserved. The forward operation may continue only if the target's prior manifest/interface says its theme interface version is accepted by the new builder. If compatibility is absent or unknown, the entire update stops before the first write and reports the incompatible customized path privately.

**Act.** Reject TI2 for this phase as unnecessary generator expansion, reject TI3 as an ownership seam too weak for reverse promotion, reject vendored fonts as additional licensing/package surface, and reject all remote resources. Keep TI2 as a later migration option if a future release intentionally makes all presentation output generated.

### E5 — OODA Loop 3: one abstract role adapter, two autonomous mappings, one complete manual mapping

**Observe.** Official OpenAI Multi-agent currently exposes spawn, message, same-agent follow-up, wait, interrupt, and list operations, but is beta and warns against shared mutable-state contention. The Codex task/thread family provides persistent task creation, follow-up, observation/wait/read, and opaque task handles, but a general verified interrupt is not guaranteed by the same surface. Tool families and availability can change: [OpenAI Multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent), [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model).

**Orient.** Responses-only `X4` cannot implement user-owned Codex task sessions. Task-only `X5` cannot use hosted same-response agents. Manual-only `X6` is portable but fails to exploit an approved capable runtime. The invariant is an abstract capability transaction, not a product name.

**Decide.** Select `role-adapter-v1`:

| Abstract capability | Responses multi-agent mapping | Codex task/thread mapping | Manual-complete mapping |
|---|---|---|---|
| `create_named_role_session` | `spawn_agent` once per role | create one named task/thread per role | owner opens exactly one role session and records its handle |
| `send_followup_same_session` | `followup_task` | send follow-up to stored task/thread ID | owner sends the next prompt to the same recorded session |
| `observe_role_status` | `list_agents` | wait/read task status | coordinator reads the role's trace/report and owner relays status only when needed |
| `wait_for_role_event` | `wait_agent` | wait for task event | coordinator stops; owner resumes after the recorded role finishes |
| `route_report_to_coordinator` | `send_message`/final to parent | task report targeted to phase coordinator or read by it | role writes RF/REVIEW and reports only through the phase coordinator |
| `verify_target_handle` | canonical agent path/status | opaque task ID plus read/status confirmation | owner confirms the recorded role session before sending |
| `interrupt_and_confirm` | `interrupt_agent` then status check | use only if the runtime exposes a verified interrupt; otherwise unsupported | owner explicitly stops the recorded role and confirms idle |

At phase start the coordinator probes the **base set**: create, same-session follow-up, observe, wait, route, and target verification. If any base capability is absent, the phase enters manual-complete **before creating any autonomous worker**. Interrupt is an optional extension: without it, no live reassignment is attempted; the coordinator waits or uses an explicitly confirmed manual stop.

Phase invariants:

1. one phase coordinator, one executor, and one reviewer session; research uses its named researcher role under the same ownership principle;
2. the coordinator alone creates/records/reassigns role handles;
3. executor is the only implementation writer; reviewer starts only from completed RF/evidence and never writes implementation;
4. correction goes to the same executor, then the same reviewer performs a full re-review;
5. lost or ambiguous handle yields `stop-no-duplicate`; replacement requires an explicit coordinator decision and a recorded supersession, never automatic creation;
6. workers report only to their phase coordinator; top-level coordination talks to phase coordinators only;
7. capability loss mid-phase stops further autonomous dispatch. Completed filesystem traces remain authoritative and the coordinator switches the remaining steps to manual-complete without duplicating a running role.

Manual-complete is not "do the review mentally in one chat." It preserves the same artifact and role gates:

```text
coordinator freezes TS -> one recorded executor session implements -> RF/evidence complete
-> one recorded independent reviewer session performs full review -> REVIEW verdict
-> if correction: same executor -> new RF/evidence -> same reviewer full re-review
-> coordinator reports phase result
```

If the runtime has no cross-session message operation, filesystem RF/REVIEW traces are the relay and the owner only sends the coordinator-authored prompt to the already recorded role session. No worker is authorized to bypass its coordinator.

**Act.** Reject partial autonomous mode, replacement-on-retry, unverified task targeting, and delta-only re-review. Retain no-interrupt Codex task sessions as valid autonomous coordination for non-overlapping ordered work; live interruption simply remains disabled.

### E6 — OODA Loop 3: public-only changelog; downstream provenance belongs outside release history

**Observe.** The public repository has an Assisted 1.0 baseline recorded on 2026-08-09 but no tag pointing at that baseline. The repository `v1.0.0` tag predates Assisted. SemVer requires `X.Y.Z`, while the frozen package authority is exact `1.5`: [Git tag](https://git-scm.com/docs/git-tag.html), [Semantic Versioning 2.0.0](https://semver.org/).

**Orient.** A generic downstream-practice sentence can be truthful, but it adds no public change information and makes every future maintainer decide how much provenance is safe. The maintenance contract already explains reviewed downstream candidates generically. Changelog history should have the smallest authority surface: changes actually present in public Assisted.

**Decide.** Select `D11 Alt A`: no downstream provenance sentence in `CHANGELOG.md`. The maintenance guide may state, without organizations or releases, that a downstream deployment can submit a reviewed candidate through reverse promotion. It must not import downstream release history.

Exact public contract:

```text
VERSION contains exactly: 1.5\n

# Assisted changelog

Only changes in the public TFW Assisted package are listed here. `VERSION` is
the machine-readable version authority. Assisted uses MAJOR.MINOR identifiers;
this file does not claim Semantic Versioning compatibility.

## 1.5 — 2026-08-30

- Added the complete neutral plan, handoff, review, identity, and maintenance lifecycle.
- Added classified forward update and reviewed reverse-promotion records with fail-closed fallbacks.
- Added complete offline Russian note, work-plan, A4, and presentation templates with a neutral customizable theme.

## 1.0

- Established the standalone Russian-language Assisted starter.

Repository baseline recorded 2026-08-09; no Assisted 1.0 release tag is asserted.
```

The implementation uses `2026-08-30` only if that is the actual 1.5 public release-record date; otherwise it records the actual date. It does not backdate a tag, infer a release date from private history, or list field-only versions. `VERSION`, manifest `release_version`, policy `to_version`, latest changelog heading, README, PROJECT, skills, migration, and templates must agree with `1.5`; only `VERSION` is machine authority.

**Act.** Reject copied downstream history, tag-generated Assisted 1.0 history, generic provenance inside the changelog, and any SemVer claim. Keep public path-scoped Git history as evidence, not as a runtime dependency.

### E7 — Selected configuration and rejected alternatives

`X2` survives Extract as the single complete target:

| Thread | Selected contract | Mandatory fallback |
|---|---|---|
| Locality | hybrid OS-defined/declared root, full `operational-local-v1` positive predicates | `unsafe` or `unknown` -> zero persistent writes, session-only |
| Records | stored JCS + closed schemas + `portable-nfc-v1`; current manifest binds policy; policy binds prior manifest only | invalid/collision/mismatch -> stop before write; current mixed field -> P6 candidate |
| Policy | exact/prefix resolver with specificity semantics and canonical stored order | source unknown/ambiguous -> stop; target-only unknown -> preserve |
| Reports | immutable private report + deterministic closed public projection + semantic review | public detail unsafe -> counts-only or no export; partial remains partial |
| Templates | TI1 versioned core CSS + stock-customizable overlay/mark; builder preserves positional CLI and embeds offline | modified incompatible interface -> preserve and stop before write |
| Roles | `role-adapter-v1` with Responses, Codex task, and manual-complete mappings | incomplete base capabilities -> manual-complete before worker creation; no interrupt -> wait/manual stop |
| History | public Assisted only; `VERSION=1.5`; no private provenance or SemVer claim | unknown release date remains unknown; no tag claim |
| Privacy | schema suppression + deterministic token/hash scan + independent semantic review | fail -> no public export/promotion |

Rejected configurations:

- `X1`: safe but unnecessarily makes valid attested Linux/custom roots permanently session-only.
- `X3`: over-trusts operator assertion, has reorder-sensitive policy, mixed network assets, one private report, and duplicate role behavior.
- `X4`: volume-only locality and tag-only history overstate evidence; Responses-only orchestration is not runtime neutral.
- `X5`: compiled theme expands workflow, first-match rules remain fragile, and Codex-task-only adapter omits other supported/manual modes.
- `X6`: retained as fallback outcome, not target; it discards available safe persistence and orchestration.
- `X7`: nearly viable but stock-hash-only customization keeps theme/asset ownership mixed, and changelog provenance adds avoidable disclosure decisions.
- `X8`: copied private history, source noninspection, and replacement sessions violate truthfulness, privacy, and role reuse.

### E8 — Counter-evidence carried into Challenge

Selection does not close these attacks:

| Area | Remaining attack |
|---|---|
| Locality | hidden user-space sync inside LocalAppData/Application Support; false custom-root attestation; provider installed after probe; ancestor swap; permission widening; stale lock; platform primitive unavailable |
| Path/manifest | duplicate JSON keys under permissive parser; non-NFC raw string; Unicode/case/reserved collision; unsafe numeric size; manifest file inserted into its own list; policy omitted from manifest; payload modified after gate |
| Policy | equal-specificity collision; prefix boundary confusion; noncanonical rule order; wrong prior-manifest hash; interface-compatibility lie; modified retired hook; unrelated `.codex` loss |
| Reports | public/private count mismatch; private filename/hash/timestamp/thread ID leak; dictionary attack on a redacted hash; content-derived public ID accidentally includes private body; partial rewritten as verified; recovery journal missing |
| Templates | overlay CSS `@import` or external URL; SVG scripts/external refs/metadata/visible brand; missing glyphs; print background omission; long table overflow; customized old overlay incompatible; requested link escapes local root |
| Roles | capability disappears after creation; follow-up sent to wrong handle; lost session recreated; interrupt returns before idle; executor/reviewer overlap; delta-only re-review; worker reports outside coordinator |
| History/privacy | false `2026-08-30` release date; repository tag presented as Assisted; downstream version/date/hash paraphrased; latest changelog differs from `VERSION`; marker-free semantic disclosure |

### E9 — Hypothesis movement and recommendation classification

| Hypothesis | Gather | Extract |
|---|---|---|
| H1 | supported; two trust models open | **supported with exact refinement:** hybrid `operational-local-v1`; positive proof is bounded and revalidated; otherwise session-only |
| H2 | fixture-ready candidates; record/policy choices open | **conditionally supported, implementation-ready:** non-circular manifest/policy binding, specificity resolver, immutable private report/public projection; Challenge must break it before TS |
| H3 | three interfaces open | **supported structurally with TI1 selected:** versioned CSS overlay/local asset and render matrix; empirical render remains implementation evidence |
| H4 | supported for Russian 1.5 | **supported unchanged:** Russian public authority; machine enums neutral; no English mirror |

- **Refinements:** all selected contracts above, including the bounded locality threat model, prior-only policy binding, public projection algorithm, TI1 interface, unified role adapter, and public-only changelog.
- **Amendment proposals:** none. The selected configuration satisfies the frozen lifecycle, privacy, identity, maintenance, template, language, and role-topology claims without changing a phase, acceptance criterion, failure condition, or principle.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Eight cross-dimension configurations; `X2` selected; all six Gather gaps resolved; exact locality, manifest/policy, projection, TI1, role-adapter/manual, and changelog contracts; seven alternatives rejected; three deep OODA loops completed | Challenge the remaining locality, collision, partial-write, privacy, rendering, capability-loss, and history attacks; determine whether `X2` survives unchanged into RES |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?
- [x] Six named gaps resolved?
- [x] Counter-evidence preserved rather than explained away?
- [x] Recommendation classified as refinement versus amendment?

**Deep-mode exit:** three OODA loops completed; configuration `X2` is exact enough to implement and falsify; every rejected configuration has a concrete reason; remaining work is adversarial rather than architectural selection.

**Metacognitive check:** Extract changed the raw candidates materially: it removed the manifest/policy self-reference cycle; replaced array-order semantics with specificity semantics; made public reporting a one-way derived artifact; selected a stock-customizable neutral overlay instead of a compiler; admitted explicit locality assertion only as one mechanically bounded predicate; and removed downstream provenance from the public changelog entirely.

Stage complete: YES
→ Phase Coordinator decision: recommend close Extract and proceed to Challenge
