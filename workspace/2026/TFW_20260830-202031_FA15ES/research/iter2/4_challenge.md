# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> Goal: Assisted 1.6 remains a faithful independent TFW realization while Full and Assisted coexist on one device and publishers choose update sources without provider-specific product machinery.

## Consistency Check

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1: Physical binding layout | One combined Full/Assisted YAML | D1: Physical binding layout | Independent schemas and writers | Full permits one path → handle key kind; Assisted requires UUID → mode/participant records and a different reservation protocol. |
| D1: Physical binding layout | Separate files under one parent | D2: Legacy Assisted handling | Permanent dual read | Two Assisted files can disagree and require cross-location reservation; neither remains the sole authority. |
| D2: Legacy Assisted handling | Automatic copy/merge | D3: Unresolved local state | Fail-closed semantics | A stale, invalid, locked, or unavailable legacy registry cannot authorize durable writes into the new authority. |
| D1: Physical binding layout | One physical common parent | D4: Host placement | Independent platform-native roots | On macOS/Linux Full is fixed at `~/.tfw` while field Assisted is elsewhere, so both cannot be true simultaneously. |
| D4: Host placement | Project/shared/sync root | D3: Unresolved local state | Persistent binding | Machine-local attribution would be shared or synchronized; the field contract explicitly rejects that placement. |
| D5: Source representation | Mutable `latest` or branch head | D6: Exact-byte evidence | `VERSION` only | The locator and version can remain the same while package bytes change. |
| D5: Source representation | Provider folder/tree | D7: Recheck model | Locator metadata only | Folder membership and child bytes can change without the top-level locator changing. |
| D6: Exact-byte evidence | Same-channel digest | D8: Origin assurance | Cryptographic publisher authentication | A substituted package can carry a matching substituted digest; no independently trusted signer or expected value exists. |
| D7: Recheck model | Snapshot once | D5: Source representation | Mutable folder/link | Post-plan source or target changes remain undetected before the write. |
| D8: Origin assurance | Signature/attestation | D8: Origin assurance | No configured trusted root/verified subject | A signature can prove only possession of some key; the client has not established whose key it should trust. |
| D9: Documentation ownership | Publisher shelf inside installable `README.md` | D9: Documentation ownership | Shelf survives overlay update | `README.md` is replaceable service content, so a downstream provider choice can be erased by the very update it locates. |

### Surviving configurations

| Config | D1: Physical binding layout | D2: Legacy handling | D3: Unresolved state | D4: Host placement | D5–D9 source family | Notes |
|--------|-----------------------------|---------------------|----------------------|--------------------|----------------------|-------|
| S1 | B2 separate child file | Preserve/ignore; re-onboard once | Ask; session-only if unsafe | Full family root | U1 versioned archive | Baseline provider-neutral archive flow. |
| S2 | B2 separate child file | Preserve/ignore; re-onboard once | Ask; session-only if unsafe | Full family root | U2 provider/Drive folder | Survives only with safe closed copy, full dynamic manifest, and full source re-read. |
| S3 | B2 separate child file | Preserve/ignore; re-onboard once | Ask; session-only if unsafe | Full family root | U3 Drive blob/revision | Provider object/checksum evidence is conditional; manifest remains mandatory. |
| S4 | B2 separate child file | Preserve/ignore; re-onboard once | Ask; session-only if unsafe | Full family root | U4 GitHub immutable asset | Strongest available provider case, but not required and not present in the current repository. |
| S5 | B2 separate child file | Preserve/ignore; re-onboard once | Ask; session-only if unsafe | Full family root | U5 GitHub exact-commit archive | Valid for the human-gated scope when described as computed snapshot integrity, not immutable release authentication. |
| S6 | B2 separate child file | Preserve/ignore; re-onboard once | Ask; session-only if unsafe | Full family root | U6 local folder/archive | Valid with resolved path, closed copy, manifest, and re-read; the path itself is not an immutable object. |

**Unexpected survivors:**

- **S2 / Drive folder:** a folder with no exposed object ID or provider digest still satisfies the approved prompt-only contract because the updater can freeze a closed local copy, compute the whole tree, re-read the live source before writing, and disclose that origin is human-confirmed rather than authenticated.
- **S5 / GitHub exact-commit generated archive:** the actual repository has no Releases, yet an archive pinned to a commit can still be normalized and rechecked. It must not be called a release asset or attested immutable release.

## Findings

### C1: Binding attacks leave one canonical Assisted authority and no destructive transition

The strongest stale-state attack is “legacy says Alice, new says Bob.” B2 selects Bob because the new file is the only Assisted authority; it never reads legacy, so disagreement cannot create an implicit merge. The strongest availability attack is “new file says Alice but its foreign lock prevents a safe read.” B2 returns no stored participant, asks once, and performs no durable write. The malformed-new case likewise cannot be repaired after a human answer; attribution stays session-only. A shared device creates or retains `ask`, while autonomous handoff/review touches neither registry.

The one-time re-onboarding promise must be described narrowly: after a missing canonical-new entry, the ordinary human gate may create only the current project's `fixed` or `ask` entry. It does not copy profiles, enumerate legacy projects, rename identifiers, touch the Full file, or delete old state. Existing project/profile/task identity remains unchanged. This is backward-compatible product behavior with one bounded loss of local convenience, not on-disk binding compatibility.

The POSIX attack is a shared or redirected home directory. `~/.tfw` is not automatically machine-local merely because it is conventional Full state. The unchanged field guards—reject shared/synchronized roots, unsafe links, non-regular/unreadable state, and unprovable exclusive reservation—are part of B2 on macOS/Linux; failure yields session-only behavior. With that condition, the family-root exception changes convention, not safety.

### C2: Recheck catches drift, but writes must come from the approved closed tree

Challenge repeated both live external reads after Extract:

- The Drive-mounted field source still had 28 files and manifest `6d76545790f6f899612dc3af80bb291e40569d4f7fa300d701fec0f3111ad214`.
- GitHub `v2.0.0` still resolved to commit `5a72b2bd420922d640d4c7f7ed0bf4507e9285af`.

A synthetic same-version substitution then kept `VERSION=1.6` and the same project structural markers while changing only `README.md`. The expected manifest was `8232f1193bac89a580c3cbc378dd6ccd6689a68c2a84bcc204441faf37d99699`; the substituted manifest was `1ad7d8fa3f97e2f0f480d1b73e30ea4eff972f346edf264776aae0071d878497`. Dynamic recheck detected the change even though version and structure did not.

The residual time-of-check/time-of-use rule is therefore:

1. acquire into a new safe closed tree outside the target;
2. normalize and compute archive/tree evidence before the plan and Gate;
3. after approval, re-resolve/re-read the provider source, the closed tree, target baselines, and protected paths;
4. on any difference or inaccessible required recheck, return to Compare and obtain a new Gate;
5. write only from the same rechecked closed tree, never from the live folder/link.

This rule is provider-neutral and keeps the field updater's one-Gate behavior. For Drive revisions, an exact-revision claim is invalid if the revision cannot be retrieved; Google notes that purgeable revisions can disappear unless retained. For GitHub, official verification distinguishes uploaded immutable release assets from generated source archives. Sources: [Drive revision management](https://developers.google.com/workspace/drive/api/guides/manage-revisions), [GitHub release integrity verification](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/verify-release-integrity).

### C3: A self-consistent malicious package defeats same-channel digests from the start

Both synthetic trees validated against their own computed manifest. Thus an attacker who substitutes the complete package before Compare can preserve `VERSION`, structural markers, and a same-package checksum. A1 evidence detects drift relative to the bytes first observed; it does not establish who authored those initial bytes. NIST describes message digests as detecting whether messages changed after the digest was generated. TUF demonstrates what stronger origin/update authentication actually requires: trusted root keys, signed target metadata, version/expiry rules, and snapshot/timestamp roles—not an unsigned manifest beside its payload. Sources: [NIST FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final), [The Update Framework specification](https://theupdateframework.github.io/specification/v1.0.28/).

The exact honest boundary for FA15ES is:

> The human confirms the publisher and source location. The updater records the strongest object/revision/digest evidence available and computes a full normalized-tree manifest. These checks detect changes to the bytes observed during this update; they do not by themselves authenticate the publisher or make a mutable source immutable. If authenticated origin is required, stop and require an independently trusted digest or verified provider attestation/signature. Establishing and governing a signing trust root is outside this Assisted update contract.

This boundary is sufficient for the approved explicit, human-gated, prompt-only scope. It neither forbids stronger provider evidence nor pretends the current repository has it. A future unattended or adversarial-origin threat model requires a separate task and likely a frozen-contract decision because it adds durable trust configuration and verification machinery.

### C4: Documentation deletion test leaves no new schema and no duplicated authority

| Removal attack | Observable failure | Disposition |
|---|---|---|
| Remove generic source forms from Assisted `README.md` | A non-technical user no longer knows that a path, archive, URL, attachment, or cloud object is acceptable | Keep one short generic section; no provider URL |
| Remove acquisition/evidence/recheck rules from `/tfw-update` | Provider cases diverge or silently omit closed-tree/recheck/authentication wording | Keep as the single normative consumer algorithm |
| Remove `MIGRATION.md`/`CHANGELOG.md` transition authority | `VERSION` alone cannot authorize protected-state changes | Keep their existing version/migration jobs; add no locator |
| Remove the public shelf from repository-level maintenance documentation | The public publisher's selected route is no longer visible | Add one exact shelf/naming subsection to `editions/ASSISTED_MAINTENANCE.md` when the publisher has selected and materialized it |
| Put a downstream shelf inside copied/replaced service content | The next overlay can erase the producer's route | Require downstream publisher documentation outside the installable package/target; `/tfw-update` asks once when it is not supplied |
| Keep static `release-manifest.json`/`maintenance-policy.json` | Jobs duplicate dynamic evidence, version maps, and prose classification while remaining same-boundary unsigned data | Delete them; no replacement schema |

The current GitHub repository's read-only Releases API returned zero releases, while tag/archive access exists. Documentation must therefore not claim a GitHub release asset, provider digest, immutability, or attestation until a publisher actually creates and verifies one. This is an implementation truthfulness condition, not a research blocker: the publisher may name Drive, a GitHub exact-commit/archive or future release asset, a local shelf, or another accessible representation.

### C5: Final hypothesis challenge

H2a survives with B2 and the explicit portability/safety wording. H4 survives with U1–U6 and the A0+A1 minimum boundary. No tested failure requires a new manifest schema, provider runtime, Full edit, legacy binding migration, or frozen HL change. The remaining work is specification and implementation: select/materialize the actual public shelf, write the exact generic rules at their identified loci, and verify product fixtures under the future TS.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| B2 survives missing, disagreement, malformed, lock, shared-device, autonomous, Windows, and explicit POSIX attacks without Full or legacy access. | No research gap; implementation must retain the documented fail-closed guards and one-time convenience cost. |
| Closed-tree manifest/recheck detects live and synthetic drift across Drive/GitHub/local forms; same-channel evidence cannot authenticate initial origin. | No in-scope research gap; signed trust remains an explicitly separate threat model. |
| Each documentation locus has one unique job; publisher-specific shelf stays outside the replaceable package, and the JSON pair remains redundant. | Publisher must choose and materialize the actual public shelf during authorized implementation/release work; current GitHub Releases count is zero. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: YES
→ User decision: Pre-authorized synthesis; evidence supports `SUFFICIENT` with no contract blocker.
