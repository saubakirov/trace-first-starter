# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260830-114238_ASSISTED15](../../HL-TFW_20260830-114238_ASSISTED15.md)
> Predecessor: [Iteration 1 RES](../iter1/RES.md)
> Goal: Turn the surviving Assisted 1.5 core/overlay design into exact, adversarially testable locality, maintenance-record, template, orchestration, and public-history candidates without reopening the frozen product contract.

## Dimensions

Each alternative is still open until Extract and Challenge. A capability or platform signal is not treated as stronger evidence than its primary source supports.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: locality authority | OS-defined app-state root | explicit operator-declared local root | runtime-detected local volume/mount | session-only, no persistent root |
| D2: locality result | `proven` under a stated threat model | `unsafe` by positive disqualifier | `unknown` on incomplete evidence | platform unsupported |
| D3: path identity | exact UTF-8 path | NFC-normalized path | portable NFC + casefold collision key | platform-native identity |
| D4: release serialization | stored JCS JSON | pretty JSON canonicalized only for hashing | line-oriented tuple manifest | repository tree object |
| D5: maintenance-policy selector | exact path only | exact + prefix, ordered | expanded per-release path table | glob patterns |
| D6: operation-report visibility | one private detailed report | one public redacted report | private evidence + derived public report | counts-only report |
| D7: template customization | stock-hash protected in-place files | CSS variable overlay | JSON theme compiled into output | immutable stock plus copied downstream templates |
| D8: asset/font delivery | system-font stack + neutral local asset | vendored local fonts/assets | optional explicit local asset override | remote web resources |
| D9: role orchestration | Responses multi-agent adapter | Codex task/thread adapter | external session manager | complete manual protocol |
| D10: retry/interruption | follow up in the same role session | interrupt then same-session follow-up | wait for completion then follow up | create a replacement role session |
| D11: public history authority | public Assisted repository history only | public history plus generic provenance note | release tags only | copied downstream release history |
| D12: privacy evidence | deterministic marker/field scan | schema-level suppression | semantic independent review | source never inspected |

## Findings

### G1 — OODA Loop 1: locality is a decision table, not a folder-name heuristic

**Observe.** The official platform evidence supports different claims:

- Microsoft identifies `FOLDERID_LocalAppData` as per-user local application data and separately advises that machine-specific application data belongs there. `GetDriveTypeW` distinguishes fixed from remote volumes, but does not detect a user-space sync client: [Known folders](https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid), [Windows app restore](https://learn.microsoft.com/en-us/windows/apps/develop/windows-app-restore), [`GetDriveTypeW`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getdrivetypew).
- Apple exposes both whether a volume is local and whether an item is ubiquitous/iCloud-backed. A false ubiquitous flag excludes iCloud for that item; it says nothing about every third-party synchronizer: [`volumeIsLocalKey`](https://developer.apple.com/documentation/foundation/urlresourcekey/volumeislocalkey), [`isUbiquitousItemKey`](https://developer.apple.com/documentation/foundation/urlresourcekey/isubiquitousitemkey).
- Linux `/proc/<pid>/mountinfo` exposes mount point, filesystem type, and source. The XDG specification categorizes `XDG_STATE_HOME` as persistent per-user state, but gives an explicit local/non-shared guarantee only to `XDG_RUNTIME_DIR`, which is not a durable identity store: [Linux proc filesystem](https://www.kernel.org/doc/html/latest/filesystems/proc.html), [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/).
- Python's `dir_fd` and `follow_symlinks` support is platform-dependent; its documentation also warns that check-then-open authorization is racy. A single cross-platform Python path check is therefore not equivalent to an operation-time safe handle: [Python `os`](https://docs.python.org/3/library/os.html).

The targeted field identity implementation chooses conventional OS state roots and uses same-directory temporary replacement, but it checks only the final store path for a symbolic link and resolves the path before returning the original spelling. It does not positively establish that every ancestor remains non-link, that the volume is local, or that a user-space provider does not synchronize the location. This is a refinement of iteration 1, not a new frozen contradiction.

**Orient.** The word `proven` must be scoped to an explicit threat model. The strongest mechanically testable model here is: no project/source/shared/provider root; local non-remote volume; no link/reparse ancestor; private app-owned directory; supported operation-time open/replace/lock primitive; and no unresolved probe. It cannot prove that an arbitrary same-user program will never copy the directory.

**Decide.** Carry two locality candidates into Extract instead of conflating them:

1. **Strict detected proof:** all mechanical predicates are positive; any provider coverage gap yields `unknown`.
2. **Declared-root proof:** the same mechanical predicates plus an explicit operator assertion that the root is not synchronized/shared; the assertion and threat-model limitation are recorded.

`unsafe` remains reserved for a positive disqualifier. `unknown` is the correct result for incomplete capability or provider evidence. Both non-proven states require the frozen zero-write session-only fallback.

**Act.** The fixture-ready candidate table is:

| Platform/fixture | Candidate root/evidence | Positive disqualifier | Candidate result |
|---|---|---|---|
| Windows local app data | OS machine-specific root; fixed volume; app-owned directory; no reparse ancestor; provider-root scan complete | none | `proven` under strict documented threat model |
| Windows UNC/remote | any per-user-looking path on `DRIVE_REMOTE` or UNC | remote volume | `unsafe` |
| Windows fixed custom folder | fixed volume, but not OS app-state root and provider status incomplete | none | `unknown` |
| Windows reparse ancestor | otherwise local candidate with junction/reparse ancestor | ancestor can redirect operation | `unsafe` |
| macOS application support | application-support root; `volumeIsLocal=true`; `isUbiquitous=false`; no link ancestor; provider-root scan complete | none | `proven` under strict documented threat model |
| macOS iCloud item | local volume but `isUbiquitous=true` | iCloud-backed item | `unsafe` |
| macOS local volume, unknown provider | `volumeIsLocal=true`, no iCloud evidence, third-party provider coverage incomplete | none | `unknown` |
| Linux default XDG state | persistent state category on a local-looking mount, no non-shared guarantee | none | `unknown` |
| Linux explicit root | local mount, non-network filesystem/source, no link ancestor, private directory, explicit non-shared assertion | none | `proven` only under declared-root model |
| Linux NFS/SMB/FUSE provider | network/shared/provider mount evidence | shared mount/source | `unsafe` |
| Any unsupported probe | candidate path exists but volume, ancestor, ACL, or safe primitive cannot be verified | none | `unknown` |
| Any source/project root | candidate is inside source, installed project, declared shared root, or known provider namespace | shared/source containment | `unsafe` |

Exact locality record candidate:

```json
{
  "schema_version": 1,
  "result": "unknown",
  "model": "strict-detected-v1",
  "candidate_kind": "xdg-state-home",
  "checks": {
    "outside_project": true,
    "outside_source": true,
    "outside_declared_shared_roots": true,
    "volume_local": true,
    "provider_scan_complete": false,
    "link_free_ancestors": true,
    "private_directory": true,
    "safe_primitive_available": true
  },
  "persistence_allowed": false
}
```

The record deliberately contains no absolute path, username, or device identifier. A private diagnostic may carry those details; a public trace may not.

### G2 — OODA Loop 1 counter-evidence: a local disk is not a non-shared guarantee

**Observe.** A fixed/local volume can contain a directory watched by a user-space synchronizer. Conversely, a path outside known provider roots may be copied by an unrecognized client. The OS sources expose useful positive and negative signals, not an exhaustive inventory of all future synchronization software.

**Orient.** Treating `fixed` or `volumeIsLocal=true` as sufficient would turn an implementation heuristic into a product guarantee. Treating every app-data root as forever unsafe would make frozen persistent identity impossible even when the operator and platform provide adequate evidence.

**Decide.** The unresolved choice is not whether to fail closed — frozen H1 already requires that — but whether a declared-root assertion is an admissible part of positive evidence. Extract must state the trust boundary; Challenge must attack both candidates with a hidden user-space sync fixture.

**Act.** Add `local-fixed-but-userspace-synced`, `provider-root-added-after-probe`, `ancestor-swapped-after-check`, and `store-permissions-widened` to the Challenge queue.

### G3 — OODA Loop 2: three exact records, three different authorities

**Observe.** RFC 8785 provides deterministic JSON canonicalization, rejects duplicate object names through the I-JSON constraint, sorts object properties, and preserves array order. It explicitly does not normalize Unicode strings. JSON Schema 2020-12 can validate shape and reject unevaluated properties, but does not assign maintenance authority. TUF separates target hashes/sizes from version-consistent metadata, and SPDX treats file checksums as integrity rather than authenticity: [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html), [JSON Schema 2020-12](https://json-schema.org/draft/2020-12), [TUF metadata](https://theupdateframework.io/docs/metadata/), [SPDX file information](https://spdx.github.io/spdx-spec/v2.2.2/file-information/).

**Orient.** Deterministic bytes, portable path identity, path ownership, release transition authority, and a record of what actually happened are independent. One combined manifest would either change on every operation or mix public release facts with downstream-private evidence.

**Decide.** Carry a JCS/JSON-Schema candidate and two serialization alternatives into Extract. In the JCS candidate, paths must pass a separate `portable-nfc-v1` validator before serialization:

- UTF-8, relative, `/` separators, no empty/`.`/`..` segment, no absolute or drive prefix;
- every string already NFC; the validator rejects rather than silently rewrites;
- no control characters, trailing space/dot, or Windows-reserved segment;
- no symbolic links or other non-regular payload entries;
- exact duplicate and `NFC(path).casefold()` collision both reject the entire release;
- files are sorted by canonical path before JCS; raw file bytes are SHA-256 hashed.

**Act.** The exact release-manifest candidate `RM1` is:

```json
{
  "schema_version": 1,
  "record_type": "assisted-release-manifest",
  "edition": "assisted",
  "release_version": "1.5",
  "content_language": "ru",
  "path_profile": "portable-nfc-v1",
  "hash_algorithm": "sha256",
  "files": [
    {
      "path": "CHANGELOG.md",
      "kind": "file",
      "bytes": 512,
      "sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    },
    {
      "path": "VERSION",
      "kind": "file",
      "bytes": 4,
      "sha256": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    }
  ],
  "payload_tree_sha256": "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
}
```

The hashes above are synthetic fixture values. `files` excludes the manifest itself to avoid a self-hash cycle. `payload_tree_sha256` is `SHA-256(JCS(files))`; the stored manifest is itself canonical JCS and its file hash is supplied by the caller/trusted release record. Extract must compare that design with a detached manifest digest and a line-tuple tree digest.

Exact maintenance-policy candidate `MP1`:

```json
{
  "schema_version": 1,
  "record_type": "assisted-maintenance-policy",
  "edition": "assisted",
  "policy_version": "1",
  "path_profile": "portable-nfc-v1",
  "source_unknown": "stop",
  "target_only_unknown": "preserve",
  "rule_match": "first-match",
  "rules": [
    {
      "id": "downstream-template-overlay",
      "selector": {"type": "prefix", "value": "шаблоны/overlay/"},
      "authority": "downstream-only",
      "sensitivity": "private",
      "forward": "preserve",
      "reverse": "candidate-only",
      "on_modified": "preserve"
    },
    {
      "id": "stock-templates",
      "selector": {"type": "prefix", "value": "шаблоны/"},
      "authority": "stock-customizable",
      "sensitivity": "public",
      "forward": "replace-if-known-stock",
      "reverse": "candidate-only",
      "on_modified": "stop-preserve"
    },
    {
      "id": "public-version",
      "selector": {"type": "exact", "value": "VERSION"},
      "authority": "public-core",
      "sensitivity": "public",
      "forward": "replace-if-known-stock",
      "reverse": "forbid",
      "on_modified": "stop-preserve"
    },
    {
      "id": "project-work",
      "selector": {"type": "prefix", "value": "work/"},
      "authority": "downstream-only",
      "sensitivity": "private",
      "forward": "preserve",
      "reverse": "exclude",
      "on_modified": "preserve"
    },
    {
      "id": "retired-known-hook",
      "selector": {"type": "exact", "value": ".codex/hooks.json"},
      "authority": "retired",
      "sensitivity": "public",
      "forward": "remove-if-known-stock",
      "reverse": "forbid",
      "on_modified": "quarantine-preserve"
    }
  ],
  "transitions": [
    {
      "from_version": "1.0",
      "to_version": "1.5",
      "from_manifest_sha256": "dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
      "to_manifest_sha256": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
    }
  ]
}
```

`MP1` makes precedence observable, but nested prefixes can still be reordered incorrectly. Alternatives retained for Extract are: disjoint rules only; longest-specific-selector independent of array order; or expansion to an exact per-release path table. Globs remain a separate, higher-ambiguity alternative.

Exact public operation-report candidate `OR1`:

```json
{
  "schema_version": 1,
  "record_type": "assisted-operation-report",
  "visibility": "public",
  "operation_id": "fixture-forward-clean-001",
  "direction": "public-to-downstream",
  "source_version": "1.5",
  "target_version_before": "1.0",
  "target_version_after": "1.5",
  "source_manifest_sha256": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
  "status": "verified",
  "mutation_started": true,
  "counts": {
    "planned": 6,
    "replaced": 4,
    "removed_known_stock": 1,
    "preserved": 7,
    "candidate_only": 0,
    "suppressed_private": 3,
    "unexplained": 0
  },
  "rule_ids": ["public-version", "stock-templates", "retired-known-hook"],
  "verification": {
    "version_agrees": true,
    "public_core_matches_manifest": true,
    "owned_target_bytes_preserved": true,
    "unexplained_changes": 0
  },
  "recovery": {
    "required": false,
    "journal_record_id": null
  }
}
```

A private report alternative may include exact destination-relative paths and pre/post hashes. A public report must not include absolute paths, usernames, machine IDs, thread IDs, private filenames, private hashes, or timestamps that disclose downstream activity. If failure occurs after the first mutation, `status=partial`, `recovery.required=true`, and a private recovery journal is mandatory; it can never be rewritten as `verified` without a new verification operation.

### G4 — OODA Loop 2: fixture matrix for schemas and mutation boundaries

**Observe.** Strict schemas can reject malformed data while still accepting a false authority claim. A correct manifest can also describe a source version different from `VERSION`, and a correct policy can reference the wrong manifest. A plan can become stale between baseline check and first write.

**Orient.** Cross-record invariants and operation state are therefore fixture obligations, not schema-field documentation.

**Decide.** Carry these exact fixtures into Extract/Challenge:

| Fixture | Input state | Expected candidate assertion |
|---|---|---|
| `forward-clean-1.0-to-1.5` | known public 1.0 stock plus downstream work/people/knowledge/overlay and unrelated `.codex` | only known stock changes; owned/private/unknown bytes identical; all version claims `1.5`; `verified` |
| `forward-custom-template` | one stock-customizable path differs from every accepted stock hash | whole operation stops before write or preserves and reports an explicit incompatibility; never overwrite |
| `mixed-field-candidate` | generic and downstream semantics share paths | P2 makes no mutation; P6 emits a private candidate for manual neutralization/review |
| `portable-path-collision` | `é.md` versus decomposed equivalent; case-only pair; reserved name; `..`; backslash; symlink | release rejected before comparison or write |
| `mixed-release-records` | manifest says 1.5, policy transition says another target, `VERSION` differs | release rejected as internally inconsistent |
| `policy-overlap` | nested prefix rules reversed or equal-specificity selectors conflict | policy rejected or deterministic result proven independent of unsafe order |
| `baseline-race` | target changes after planning and before first mutation | baseline gate fails; zero writes |
| `partial-write` | injected failure after first mutation | `partial`, success false, recovery journal present, unexplained change nonzero until recovered |
| `reverse-private` | synthetic private organization/person/path/id tokens among otherwise generic improvements | public candidate/report contains no sensitive value or hash; semantic review required |
| `reverse-clean-overlay` | already separated public core improvement plus downstream overlay | candidate-only reverse artifact; independent review; no direct source mutation |

**Act.** The release-manifest, maintenance-policy, and operation-report schemas remain three files. No candidate permits a report to become a release authority or a hash to become a path-ownership decision.

### G5 — Targeted template interface and offline evidence

**Observe.** The read-only field set has six useful surfaces: note, work plan, A4 source, A4 builder, presentation, and asset. Targeted inspection confirms that the builder has a three-positional-argument interface, hardcodes a web-font request, and hardcodes one branded local asset. The public Assisted 1.0 tree contains no equivalent practical template set. No field content was copied.

W3C CSS Fonts defines prioritized family lists and generic fallback families; CSS Custom Properties supports reusable values and `var()` fallbacks. Paged-media behavior and page overflow remain renderer-dependent, while SVG may carry text in `title`, `desc`, or arbitrary metadata. Those facts make a local CSS/asset seam feasible but do not make render output or asset privacy self-proving: [CSS Fonts 4](https://www.w3.org/TR/css-fonts-4/), [CSS Custom Properties](https://www.w3.org/TR/css-variables-1/), [CSS Paged Media 3](https://www.w3.org/TR/css-page-3/), [SVG 2 structure](https://www.w3.org/TR/SVG/struct.html).

**Orient.** Theme values, asset selection, template semantics, and installed-project customization are four ownership surfaces. A web-font-free HTML file can still be unreadable; a metadata-free SVG can still reveal a brand in visible paths; an empty placeholder can pass marker scans while failing usefulness.

**Decide.** Retain three exact interface candidates:

1. **TI1 — CSS overlay:** public `шаблоны/theme.css` defines `--tfw-font-sans`, `--tfw-font-mono`, `--tfw-text`, `--tfw-muted`, `--tfw-accent`, `--tfw-surface`, and a neutral stock mark; shipped `шаблоны/overlay/theme.css` is empty and stock-customizable. The builder preserves its first three positional arguments and adds optional `--theme-css`, `--asset`, and `--offline` flags. Requested overrides must be local relative files; missing overrides fail nonzero.
2. **TI2 — compiled JSON theme:** `theme.json` has exact color/font/asset fields; one builder validates it, embeds CSS and the selected local SVG/data URI, and generates both A4 and presentation outputs. This maximizes single-output offline behavior but changes the static-presentation workflow.
3. **TI3 — stock-hash customization only:** complete neutral templates and asset keep fixed relative paths; projects edit copies in place, and maintenance protects any non-stock hash. This has the smallest interface but no independent brand overlay.

Candidate `TI2` theme document:

```json
{
  "schema_version": 1,
  "name": "neutral",
  "colors": {
    "text": "#20242a",
    "muted": "#5f6875",
    "accent": "#315a7d",
    "surface": "#f4f6f8"
  },
  "font_stack": {
    "sans": ["system-ui", "Segoe UI", "Arial", "sans-serif"],
    "mono": ["ui-monospace", "Cascadia Mono", "Consolas", "monospace"]
  },
  "asset": "assets/tfw-mark.svg",
  "network_resources": "forbidden"
}
```

Exact render fixtures shared by all candidates:

- stock note/work-plan examples are complete generic Russian examples, not placeholders;
- A4 and presentation render with network disabled and contain no `http:`/`https:` dependency;
- long Cyrillic/Latin headings, long unbroken tokens, lists, code, and wide/tall tables are rendered and visually inspected;
- neutral SVG is scanned across all bytes and XML nodes for external references, scripts, organization/person/location tokens, `title`, `desc`, and metadata; visible output is also reviewed;
- valid custom theme/asset renders; a requested missing or external asset fails clearly;
- an installed customized-old-template fixture remains byte-identical across update, and an incompatible builder contract is reported rather than hidden;
- evidence includes command, exit code, output hashes, page/slide count, rendered pages/screenshots, network-request log, and privacy scan.

### G6 — OODA Loop 3: reusable-role capability adapter

**Observe.** Official OpenAI documentation currently describes Responses multi-agent as beta. It exposes `spawn_agent`, `send_message`, `followup_task`, `wait_agent`, `interrupt_agent`, and `list_agents`; the root coordinates and synthesizes. It also warns that subagents are a poor fit when they contend over shared mutable state. The beta schema may change: [OpenAI Multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent). Official model guidance separately recommends explicit autonomy, approval, retry, and stopping boundaries: [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model).

The current Codex desktop task surface and the Responses multi-agent surface are not identical. Create/send/wait/read task operations can support persistent user-owned task sessions; the hosted multi-agent actions support spawn/follow-up/wait/interrupt/list inside one response. Availability of either family in one runtime does not prove availability of the other family or a stable external task handle.

**Orient.** The contract is role/session reuse, single-writer ownership, independent review, and coordinator-only reporting — not a particular tool name. Partial autonomous support is dangerous: creation without stable follow-up encourages duplicate role sessions; observation without interruption cannot safely replace a running assignment; interruption without status confirmation can overlap writers.

**Decide.** Carry this capability vector and fail-closed adapter candidate:

```json
{
  "schema_version": 1,
  "adapter": "runtime-detected",
  "required_for_autonomous": [
    "create_named_role_session",
    "send_followup_same_session",
    "observe_role_status",
    "wait_for_role_event",
    "route_report_to_coordinator"
  ],
  "required_for_live_reassignment": [
    "interrupt_running_role",
    "confirm_interrupted_or_idle"
  ],
  "on_missing_required": "manual-complete",
  "on_lost_handle": "stop-no-duplicate",
  "role_handle_persistence": "phase-session-only"
}
```

State-machine candidate:

```text
PROBE
  ├─ incomplete required set ─> MANUAL_COMPLETE
  └─ complete required set ─> READY
READY ─create once/role─> ROLE_IDLE ─follow-up─> ROLE_RUNNING
ROLE_RUNNING ─event─> ROLE_IDLE | ROLE_NEEDS_COORDINATOR | ROLE_FAILED
ROLE_RUNNING ─owner stop + interrupt+confirm─> ROLE_IDLE
ROLE_RUNNING ─interrupt unavailable─> WAIT_OR_MANUAL_STOP
lost/ambiguous handle ─> STOP_NO_DUPLICATE
```

The phase coordinator stores one opaque handle per phase role and is the only party that creates or reassigns those sessions. The executor is the sole implementation writer. The reviewer receives the completed RF/evidence only after execution, performs a full independent re-review on every correction cycle, and reports only to the phase coordinator. A correction uses follow-up on the same executor and then the same reviewer session; it does not create replacement roles. The top-level coordinator communicates with phase coordinators, not their workers.

**Act.** Exact adapter fixtures:

| Fixture | Capabilities/state | Expected candidate behavior |
|---|---|---|
| `all-capabilities` | create/follow-up/observe/wait/route/interrupt/list | one handle per role; same-session correction and re-review |
| `create-only` | create succeeds; stable follow-up absent | manual-complete mode before any worker creation |
| `no-interrupt` | all base capabilities except interrupt | no live reassignment; wait or explicit manual stop |
| `lost-handle` | role may exist but handle cannot be confirmed | stop; do not create a duplicate automatically |
| `wrong-target` | follow-up target cannot be verified | stop; no fallback send to another session |
| `writer-overlap` | executor still running when correction arrives | interrupt+confirm or wait; never overlap implementation writers |
| `partial-review` | reviewer previously approved before correction | full RF/implementation/evidence re-read required; no delta-only approval |
| `report-escape` | worker tries to report to top-level/user | route/reject to phase coordinator; ownership graph preserved |

### G7 — OODA Loop 3: public 1.0/1.5 history and privacy fixture

**Observe.** The public Assisted tree first appears in two path-scoped repository commits on 2026-08-09 and already declares edition version `1.0`. No tag points directly at either commit. The repository's `v1.0.0` tag predates that Assisted baseline, so it cannot truthfully serve as the Assisted 1.0 release tag. This is a public repository fact, not downstream lineage.

Semantic Versioning requires an `X.Y.Z` form and a declared public API. Frozen `VERSION=1.5` is therefore a valid project version scheme but must not be called SemVer without changing the scheme and contract: [Semantic Versioning 2.0.0](https://semver.org/). Git documents annotated tags as release-oriented objects with their own tagger/date/message; absence of such a tag must not be silently replaced by a commit date called a release date: [Git tag](https://git-scm.com/docs/git-tag.html).

NIST recommends protecting PII from inappropriate disclosure, and OWASP notes that operational records can contain personal, technical, and business-sensitive information and may need exclusion, masking, or sanitization: [NIST SP 800-122](https://csrc.nist.gov/pubs/sp/800/122/final), [OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).

**Orient.** A truthful changelog does not require a tag, but it must distinguish a repository baseline date from a release-tag date. A privacy-safe changelog also cannot copy private version sequences, paths, hashes, identities, customer/project facts, or unique paraphrases merely because visible organization markers were removed.

**Decide.** Retain these history candidates:

1. public Assisted entries only, with `1.0` labelled a repository baseline rather than a tagged release;
2. the same entries plus one generic statement that reviewed downstream practice informed 1.5, with no downstream version/fact detail;
3. tag-generated history, which is not usable for Assisted 1.0 without creating false provenance;
4. copied downstream history, retained only as counter-evidence and expected to fail privacy/truthfulness.

Exact public fixture candidate:

```text
VERSION bytes: "1.5\n"

# Assisted changelog

This file records public TFW Assisted package history only. Version numbers use
the Assisted MAJOR.MINOR scheme; they are not claimed to follow Semantic Versioning.

## 1.5 — 2026-08-30

- Added the complete neutral Assisted lifecycle, identity, maintenance, and practical-template set.
- Added fail-closed update and reviewed reverse-promotion boundaries.

## 1.0 — repository baseline recorded 2026-08-09

- Established the standalone Russian-language Assisted starter.

No release tag is asserted for the 1.0 baseline.
```

The 1.5 date is admissible only if the public 1.5 release record is actually created on that date; otherwise the implementation must use its actual release date. The fixture never lists field-only versions as public releases and does not name the field organization.

Privacy fixture corpus uses synthetic values only:

```text
PRIVATE_ORG_MARKER_X
Person Example
person@example.invalid
C:\Users\Example\SharedProject
/Users/example/CloudProject
11111111-1111-1111-1111-111111111111
downstream-version-1.2
```

Public `VERSION`, changelog, release manifest, maintenance policy, templates/assets, and derived public operation reports must contain none of the synthetic tokens or their hashes. Schema suppression and marker scans are necessary but not sufficient: independent semantic review must also reject unique organization, customer, project, site, people, path, identifier, release-history, asset, or operational-timing facts.

**Act.** Add false-date, false-tag, false-SemVer, downstream-version-as-public, hash-of-private-path, private count/path mismatch, marker-free unique paraphrase, SVG metadata, and version/changelog disagreement attacks to Challenge.

### G8 — OODA Loop 3 counter-evidence and contradictions

| # | Tempting claim | Counter-evidence | Gather consequence |
|---|---|---|---|
| C1 | fixed/local volume proves non-shared identity storage | arbitrary user-space sync can watch a local folder | strict provider coverage or declared-root model; otherwise `unknown` |
| C2 | LocalAppData/Application Support/XDG State are equivalent guarantees | only their category semantics overlap; non-shared guarantees differ | per-platform evidence table, not one path-name rule |
| C3 | final-path `islink` prevents redirection | ancestor junction/symlink and check/use races remain | ancestor and operation-time primitive are separate gates |
| C4 | JCS solves portable paths | RFC 8785 does not normalize strings | validate NFC/collisions before canonical JSON |
| C5 | JSON Schema proves safe authority | a valid record can reference the wrong release or policy | cross-record invariants and baseline gate required |
| C6 | an exit-zero offline build proves a useful template | paged overflow, missing glyphs, hidden metadata, and renderer variance remain | rendered-page evidence and semantic review required |
| C7 | a CSS fallback makes output identical everywhere | generic fonts guarantee a match, not pixel identity | test readability/layout invariants, not pixel equality |
| C8 | task creation proves reusable-role orchestration | follow-up, observation, interruption, and target confirmation may be absent | capability vector is atomic; incomplete means manual mode |
| C9 | interruption means the writer is stopped | interrupt can be unavailable or status can remain ambiguous | require confirmation before reassignment |
| C10 | a public commit date is a release date | the Assisted baseline has no pointing release tag | label repository baseline truthfully; do not invent tag provenance |
| C11 | version `1.5` is SemVer | SemVer requires `X.Y.Z` and a public API | document the actual MAJOR.MINOR scheme |
| C12 | zero private markers proves neutrality | unique paraphrase, hashes, metadata, and counts can still disclose context | combine schema suppression, deterministic scans, and semantic review |

### G9 — Source and field-lineage coverage

| Thread | Repository/field evidence | External primary evidence | Counter-evidence covered |
|---|---|---|---|
| Locality | targeted identity implementation and iteration-1 field ledger | Microsoft, Apple, Linux kernel, XDG, Python | local sync, link ancestor, unsupported probe, TOCTOU |
| Records/fixtures | iteration-1 P2/P6/V1–V12 and public tree | RFC 8785, JSON Schema, TUF, SPDX | Unicode/case collision, mixed records, rule overlap, partial write |
| Templates | six targeted field template path/interfaces; public 1.0 absence | W3C Fonts, Variables, Paged Media, SVG | remote resource, metadata, missing asset, pagination, customized old template |
| Reusable roles | owner session topology and current runtime capability families | official OpenAI Multi-agent and model guidance | partial capabilities, lost handle, duplicate roles, incomplete re-review |
| History/privacy | path-scoped public commit/tag checks; iteration-1 private-lineage classification | SemVer, Git tag, NIST, OWASP | false date/tag/version relation, private hashes/facts, marker-free disclosure |

No broad field reread occurred in this iteration. The field tree remained read-only; only targeted path/interface facts already required by the five iteration threads were used, and no private fact was copied.

### G10 — Hypothesis movement after Gather

| Hypothesis | Entering iteration 2 | Gather movement |
|---|---|---|
| H1 | supported with positive-locality refinement | still supported; `proven` now has two explicit candidate trust models and an exact zero-write record, while final admissibility of operator assertion remains open |
| H2 | conditionally supported as manifest + policy + report; mixed lineage P6 | strengthened to fixture-ready candidates; selection of serialization, rule precedence, self-hash boundary, and public/private report derivation remains open |
| H3 | structurally supported; render evidence pending | strengthened to three exact interface candidates and a render matrix; no empirical implementation evidence yet |
| H4 | Russian authoritative for 1.5 | unchanged and supported; schema enums remain language-neutral, public history/template examples remain Russian |

### G11 — Remaining gaps for Extract

1. Select strict-detected versus declared-root locality proof and state the accepted threat model; decide whether macOS and Windows defaults can be `proven` without an explicit assertion.
2. Select the tree-digest/self-hash boundary and path-policy collision algorithm; select ordered, specificity-based, or expanded maintenance rules.
3. Define derivation between private detailed and public redacted operation reports, including partial-failure journal linkage without sensitive paths.
4. Select TI1/TI2/TI3 and determine whether presentation asset override must be generated, CSS-driven, or only stock-hash customized.
5. Map both Responses multi-agent and Codex task/thread capability families into one role adapter and prove the manual protocol is complete when any base capability is missing.
6. Decide whether the public changelog includes the generic downstream-practice provenance sentence or omits provenance entirely; keep the Assisted 1.0 baseline wording distinct from a release tag.

### G12 — Recommendation classification

- **Refinements:** exact locality result vocabulary and threat-model record; separate portable-path validation from JCS; fixture-ready manifest/policy/report candidates; explicit public/private report profiles; three neutral template interfaces; atomic reusable-role capability vector; truthful public baseline wording and non-SemVer label.
- **Amendment proposals:** none. All findings make implementation and verification stricter inside the frozen DoD/DoF. No target-state claim, phase, acceptance criterion, failure condition, or principle needs to change.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Twelve dimensions; platform locality table; exact locality/manifest/policy/report/theme/adapter/history candidates; ten maintenance/render fixtures; eight adapter fixtures; three OODA loops; official primary-source coverage for all five threads; twelve contradictions | Extract surviving configurations and reject alternatives; fix rule/digest/report/template choices; Challenge them under the queued attacks |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] Hypotheses tested?
- [x] Counter-evidence sought?
- [x] Field lineage used read-only without broad re-reading or private disclosure?

**Deep-mode exit:** three OODA loops completed; all five iteration threads have primary evidence and counter-evidence; fixture/schema candidates are exact enough for Extract comparison; open choices are named rather than hidden.

**Metacognitive check:** New information rather than confirmation: only some platforms can reach detected `proven` without an assertion; the current identity symlink defense is final-path-only; the release manifest needs an explicit self-hash boundary; ordered policy rules create a nested-prefix hazard; the current three-argument builder has no theme seam; Responses multi-agent supplies same-session follow-up/interrupt while other Codex task surfaces may not; and the repository `v1.0.0` tag predates the Assisted 1.0 baseline.

Stage complete: YES
→ Phase Coordinator decision: recommend close Gather and proceed to Extract
