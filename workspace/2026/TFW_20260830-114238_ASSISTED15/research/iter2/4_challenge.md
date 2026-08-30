# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260830-114238_ASSISTED15](../../HL-TFW_20260830-114238_ASSISTED15.md)
> Predecessor: [Iteration 2 Extract](3_extract.md)
> Goal: Falsify `X2` against locality, record, partial-write, template, capability-loss, and public-history attacks before admitting it to RES and TS.

## Consistency Check

All 66 dimension pairs were checked. `S` means the selected `X2` alternatives coexist directly; `C` means they coexist only under the condition named in Findings. No selected pair remains unconditionally incompatible after the Challenge refinements.

| Pair | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1: locality authority | — | C | S | S | S | C | S | S | C | C | S | C |
| D2: locality result |  | — | S | S | S | C | S | S | C | C | S | C |
| D3: path identity |  |  | — | C | C | C | C | C | S | S | C | C |
| D4: release serialization |  |  |  | — | C | C | C | S | S | S | C | C |
| D5: policy selector |  |  |  |  | — | C | C | S | S | S | C | C |
| D6: report visibility |  |  |  |  |  | — | S | S | C | C | C | C |
| D7: template customization |  |  |  |  |  |  | — | C | S | S | C | C |
| D8: asset/font delivery |  |  |  |  |  |  |  | — | S | S | S | C |
| D9: role orchestration |  |  |  |  |  |  |  |  | — | C | S | C |
| D10: retry/interruption |  |  |  |  |  |  |  |  |  | — | S | C |
| D11: public history |  |  |  |  |  |  |  |  |  |  | — | C |
| D12: privacy evidence |  |  |  |  |  |  |  |  |  |  |  | — |

**Incompatible alternative pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D1 | operator declaration only | D2 | `proven` persistence | An assertion without mechanical locality, containment, ancestor, permission, and primitive evidence is not proof |
| D1 | session-only | D2 | persistent `proven` binding | Session-only deliberately performs zero persistent writes |
| D2 | cached prior `proven` | D10 | later write after environment change | Locality must be revalidated at every binding operation |
| D3 | exact UTF-8 only | D4 | portable multi-platform release | Exact spelling alone misses normalization/case collisions |
| D3 | platform-native identity | D5 | one cross-platform prefix policy | The same selector can address different path identities on different targets |
| D4 | manifest contains its own hash/list entry | D5 | policy also points to current manifest | The build graph becomes cyclic and cannot have one deterministic fixed point |
| D4 | pretty and canonical byte forms | D11 | one machine version/history authority | Two accepted byte forms allow disagreement in hashes and release evidence |
| D5 | array first-match | D7 | nested `шаблоны/overlay/` rule | Reordering can transfer ownership from overlay to general templates |
| D5 | glob selector | D3 | portable collision profile | Glob/case/separator behavior is not the selected portable identity contract |
| D6 | public-only report | D12 | recovery and semantic privacy evidence | It cannot retain private pre/post paths while also proving they were not published |
| D6 | exact private counts in public report | D12 | non-disclosure | Counts can fingerprint a downstream installation even when names are omitted |
| D7 | unrestricted CSS overlay | D8 | guaranteed offline local rendering | `@import`, escaped `url()`, fonts, and external resources can reintroduce fetches |
| D7 | compiler-only JSON theme | D10 | unchanged static presentation workflow | It requires generating a previously static template surface |
| D8 | remote font/asset | D12 | offline/privacy acceptance | A request itself leaks dependency/context and fails offline operation |
| D9 | create-only autonomy | D10 | same-session corrections | Creation without stable follow-up/target verification encourages duplicates |
| D9 | runtime-specific mandatory adapter | D10 | complete manual fallback | Missing product-specific operations would make the fallback incomplete |
| D10 | automatic replacement session | D9 | one reusable role session | Replacement violates the phase topology and may overlap a lost-but-running role |
| D11 | tags only | D12 | truthful Assisted 1.0 history | No tag points at the public Assisted 1.0 baseline |
| D11 | copied downstream history | D12 | public privacy/authority | It presents private releases and facts as public Assisted history |
| D12 | marker scan only | D7 | semantic template neutrality | Visible layout, examples, metadata, and unique paraphrase can leak without a marker |

**Surviving configurations:**

| Config | Locality/records | Reports/templates | Roles/history | Notes |
|---|---|---|---|---|
| `X2-refined` | bounded `operational-local-v1`; portable JCS; acyclic policy binding | terminal private report + public projection; restricted TI1 overlay | capability-atomic adapter; public-only history | Complete target after the refinements below |
| `X1-strict` | OS-defined roots only; Linux/custom often `unknown` | same as `X2-refined` | same as `X2-refined` | Survives as a stricter platform behavior, not the universal target |
| `X6` | session-only; non-mutating/manual | same schemas and privacy gates still apply | manual-complete same-role protocol | Mandatory portable fallback |
| `P6 × X2` | same metadata, no direct mutation of current mixed lineage | private candidate, independent neutralization/review | same role adapter/history | Required first bridge for the current field lineage |

**Unexpected survivors:**

- `X1-strict` is not a competing architecture: it is the valid runtime result when an operator declines explicit locality assertion or the platform cannot prove a custom root.
- `X6` still satisfies the product contract because persistence, interruption, and autonomous routing are conveniences. Complete traces, independent review, and session-only identity remain possible.
- A public operation report may legitimately collapse to public-action counts plus a `private_entries_suppressed=true` boolean. Less detail is stronger evidence when exact private counts would identify an installation.

## Findings

### C1 — OODA Loop 1: locality revalidation survives only as a bounded claim

**Observe.** Google documents that a user can mirror folders on a local hard drive and that local/cloud divergence may retain both files. A fixed/local volume therefore does not imply absence of synchronization: [Google Drive stream and mirror](https://support.google.com/drive/answer/13401938). Linux `openat2()` can reject symbolic links across all path components and constrain resolution beneath a pinned directory; ordinary `O_NOFOLLOW` covers only the final component. Windows exposes `FILE_FLAG_OPEN_REPARSE_POINT` so an application can inspect a reparse point rather than silently follow it: [Linux `openat2`](https://www.kernel.org/pub/linux/docs/man-pages/book/man-pages-6.15.pdf), [Windows `CreateFile`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilea).

**Attack.** Every E8 locality case was applied:

| Attack | Effect on unrefined claim | `X2-refined` outcome |
|---|---|---|
| Hidden user-space sync under LocalAppData/Application Support | breaks “local means never synchronized” | outside the bounded registered-provider threat model; disclosed residual risk, not upgraded evidence |
| False custom-root assertion | mechanical checks still pass | assertion is a named trust input; false input remains a residual operator risk, never described as detected proof |
| Provider installed after probe | cached result becomes stale | revalidate on every operation; newly registered/provider-root evidence returns unsafe/unknown |
| Ancestor symlink/junction/reparse swap | final-path check can be redirected | platform handle-chain/no-follow resolution is required; unsupported adapter returns `unknown` before write |
| Permission widening | another principal may alter state | recheck directory/store control before every operation; fail session-only on unexpected ACL/mode |
| Stale lock file | deletion-by-age can create two writers | use an OS lock held by a live handle; never infer ownership from pathname/age or delete an unverified foreign lock |
| Native safe primitive absent | check/use race remains | `safe_primitive_available=false` -> `unknown`, session-only, zero persistent writes |

**Orient.** The strongest failure is semantic: `proven` cannot mean “no program will ever copy these bytes.” It means the complete selected evidence set passed under `operational-local-v1`. This limitation must be user-visible in the contract and internal in the decision record.

**Decide.** `X2` survives with these mandatory corrections:

1. Rename no state: keep the enum `proven`, but always record `model=operational-local-v1` and expose its bounded threat model in identity documentation.
2. `provider_scan_complete` means complete for registered and caller-declared provider roots, not all possible software.
3. A platform adapter must operate from a pinned root handle and validate each ancestor/component at operation time. A path-level `resolve()`/`islink()` sequence alone cannot produce `proven`.
4. Persistent binding uses a live OS lock plus same-directory stage/replace and post-read validation. Unsupported locking/reparse semantics force session-only.
5. Unsafe/unknown/failing probes must be tested with write interception: no directory, lock, temporary file, registry, diagnostic containing identity, or fallback cache may be created.

**Act.** Fail the stronger universal-nonsynchronization claim; retain H1's frozen behavior through bounded proof plus zero-write fallback. No HL amendment is needed because the frozen contract already makes uncertain locality session-only.

### C2 — OODA Loop 1: self-cycle prevention passes; authenticity and multi-file atomicity do not appear by magic

**Observe.** RFC 8785 explicitly requires ecosystem correctness checks in addition to canonicalization and rejects acting when those checks fail. Canonical JSON is hashable, not automatically authentic: [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html). JSON Schema closes structure only after a duplicate-key-rejecting parser has produced a valid data model: [JSON Schema 2020-12 core](https://json-schema.org/draft/2020-12/json-schema-core).

**Attack — self-cycle.** The selected build graph was expanded:

```text
schemas + payload + maintenance-policy bytes
  -> per-file hashes
  -> release-manifest files[] and payload_tree_sha256
  -> raw release-manifest SHA-256
  -> operation report
```

There is a topological order because:

- `release-manifest.json` is forbidden inside its own `files[]`;
- `maintenance-policy.json` is required inside `files[]`;
- policy schema forbids `to_manifest_sha256`, current-manifest hash, and current-manifest self-reference;
- policy transitions bind accepted prior manifest hashes only;
- operation reports are generated after and are not release payload authority.

Injecting a current-manifest hash into policy, adding manifest to `files[]`, or omitting policy must fail schema/domain validation. The self-cycle prevention therefore **survives**.

**Attack — every remaining path/manifest/policy case.**

| Attack | Required response |
|---|---|
| Duplicate JSON keys accepted by a permissive parser | parse with duplicate-pair rejection before schema validation; entire release fails |
| Raw non-NFC path or NFC/case/reserved collision | reject; never normalize/rename into a release |
| `bytes` beyond JCS safe integer range | schema maximum `9007199254740991`; actual file size must equal the integer |
| Manifest inserted into own list or policy missing | domain validator rejects fixed manifest path and requires policy/schema/version/changelog/interface entries |
| Payload changes after plan | stage verified source bytes into a local immutable operation area and bind its digest before destination mutation |
| Equal-specificity/duplicate rule | policy invalid; no tie-break by array order |
| Prefix boundary confusion (`work/` versus `workspace/`) | prefix selector must end `/` and match a complete directory segment, not raw arbitrary `startswith` |
| Noncanonical rule order | reject even though resolver semantics are specificity-based; review bytes stay deterministic |
| Wrong prior-manifest hash/version | transition gate fails before first write |
| False interface compatibility declaration | declaration alone is insufficient; statically validate installed overlay grammar/asset and run compatibility render smoke test before write |
| Modified retired hook | never remove; preserve/quarantine and report privately |
| Unrelated `.codex` material | exact retired paths only; before/after byte manifest proves every unrelated path unchanged |

**Orient.** A self-consistent manifest and changed payload can be regenerated together by an untrusted source. `X2` does not include signing/TUF authenticity. Its trust comes from the reviewed repository/source selection and scoped operation. Likewise, local staging freezes the source but cannot make a multi-file destination update transactional against an uncooperative external writer or cloud client.

**Decide.** Keep these residual boundaries explicit:

- release manifest proves integrity/coherence, not origin authentication;
- source bytes are staged and fully verified before write;
- acquire the Assisted project lock and revalidate the entire target baseline immediately before the first mutation;
- recheck each target path before its mutation and all postconditions afterward;
- drift detected before the first mutation yields `aborted` and zero writes; drift/failure after mutation yields `partial`, never success;
- automatic P2 remains limited to clean overlay-separated fixtures/installations. The current mixed field tree stays non-mutating P6.

**Act.** Reject any documentation phrase such as “transactional multi-file sync” or “authenticated release” unless a future phase adds the missing mechanism. The acyclic manifest/policy contract itself survives.

### C3 — OODA Loop 2: immutable partial evidence forces terminal reports and removes private counts

**Observe.** OWASP notes that operational logs can contain personal, technical, and business-sensitive data and recommends exclusion/sanitization plus tamper protection. Hashing a private path is not exclusion and can support a dictionary comparison: [OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html). NIST likewise treats privacy protection as context-dependent rather than a marker-list property: [NIST SP 800-122](https://csrc.nist.gov/pubs/sp/800/122/final).

**Attack.** Two Extract interpretations fail:

1. An exact `suppressed_private` count changes when the private installation changes, so a supposedly public report is not noninterfering.
2. A single “immutable report” cannot transition in place through `planned -> gated -> applying -> partial/verified` without being rewritten.

The full E8 report set produces these requirements:

| Attack | Required response |
|---|---|
| Public/private count mismatch | public-action counts are recomputed from validated private entries; no caller-supplied count accepted |
| Private filename/hash/root/timestamp/thread ID leak | closed public allowlist; schema rejects every non-public field |
| Dictionary attack on redacted hash | no digest of omitted private value appears publicly |
| Public ID computed from private body | ID is SHA-256 of sanitized public body only |
| Exact private count fingerprint | replace with `private_entries_suppressed: true|false`; no exact private count |
| Partial rewritten as verified | terminal report is create-once; recovery creates a new linked private operation |
| Recovery journal missing | journal/staged recovery evidence must be durably persisted and validated before first mutation; otherwise remain prewrite-aborted |

**Orient.** State transitions belong to an append-only private operation journal. The operation report is a terminal snapshot, not the mutable state carrier.

**Decide.** Refine the operation evidence contract:

```text
append-only private journal: planned -> gated -> applying -> terminal event
terminal report created once with exclusive-create: aborted | partial | verified
recovery: new operation/report privately links prior terminal report hash
public projection: generated only from one validated terminal private report
```

Public noninterference fixture:

- create two valid private reports with identical public release/action facts but different private paths, filenames, hashes, IDs, timestamps, and organization tokens;
- their canonical public projection bytes and `public_report_id` must be identical;
- if merely the presence of private entries differs, only the boolean `private_entries_suppressed` may differ;
- semantic reviewer may suppress even public path/action detail or reject export entirely.

Public projections include public-path action counts only. They include no exact downstream/private count and no recovery journal ID. A public `partial` status may state `recovery.required=true` because honesty about an exported operation is more important than hiding failure; the private recovery details remain local.

**Act.** Fail mutable-report and exact-private-count interpretations; retain private→public projection after these refinements. This strengthens V4/V6 without changing the frozen contract.

### C4 — OODA Loop 2: unrestricted TI1 fails; a restricted overlay plus render evidence survives

**Observe.** W3C defines `@import` as loading another stylesheet and CSS URL processing as fetching resources. SVG can load external style/resources and can carry scripts, text, metadata, and references. Paged-media output may overflow or vary by renderer: [CSS Cascading `@import`](https://www.w3.org/TR/css-cascade-3/), [CSS Values URL processing](https://www.w3.org/TR/css-values-4/), [SVG 2 structure](https://www.w3.org/TR/SVG/struct.html), [CSS Paged Media 3](https://www.w3.org/TR/css-page-3/).

**Attack.** An arbitrary `overlay/theme.css` can hide `@import`, escaped `url()`, remote fonts, private text via generated content, or layout rules that make output unreadable. A syntactically valid SVG can contain scripts, event attributes, external references, metadata, visible text, or a branded path. `exit 0` and zero obvious URLs do not prove offline readability.

All E8 template cases resolve as follows:

| Attack | Required response |
|---|---|
| CSS `@import`, `url()`, external font/resource, escape obfuscation | overlay is a strict six-property grammar, not arbitrary CSS; reject backslashes, at-rules, URLs, functions outside the allowed value grammar, and extra selectors/declarations |
| SVG script/external ref/metadata/visible brand | XML allowlist for shape-only SVG; reject script/style/text/title/desc/metadata/foreignObject/use/image/href/event attributes; semantic visual review remains required |
| Missing glyphs/system-font variation | Cyrillic/Latin/code/table render fixtures on supported renderer(s); assert readability, not pixel identity |
| Print background omission | no information or mark may depend on CSS background images/colors; mark is an `<img>`/embedded SVG and content remains legible without backgrounds |
| Long table/page overflow | rendered-page screenshots and overflow checks; exit status alone fails |
| Customized old overlay/interface | preserve bytes; validate interface version plus overlay grammar and render smoke test before core update; incompatible means prewrite stop |
| Requested link escapes local root | open from template root or explicitly approved local root using no-follow/regular-file checks; missing/escape/nonlocal resource fails nonzero |

The selected overlay grammar is now exact:

```text
:root {
  --tfw-font-sans: comma-separated local family names and one generic fallback;
  --tfw-font-mono: comma-separated local family names and one generic fallback;
  --tfw-text: #RRGGBB;
  --tfw-muted: #RRGGBB;
  --tfw-accent: #RRGGBB;
  --tfw-surface: #RRGGBB;
}
```

No other selector, property, at-rule, function, backslash escape, resource URL, or generated content is permitted in a promotable overlay. Downstream projects remain free to maintain arbitrary private customized templates, but those files are preserved and cannot be automatically reverse-promoted or used as public offline evidence.

Builder output embeds validated core CSS, validated overlay variables, and validated local shape-only SVG bytes. Presentation source references only the shipped local files. Render evidence records zero network requests under a blocked network, plus actual pages/screenshots, page/slide count, output hashes, glyph/content checks, and a semantic privacy review.

**Decide.** TI1 **survives with restricted overlay grammar**. The original unrestricted-CSS interpretation fails. TI2 remains unnecessary this phase because TI1 can be statically bounded without replacing the static presentation workflow.

**Act.** Add CSS escape/import, SVG active-content/reference, print-background-disabled, missing-glyph, long-table, and customized-interface fixtures to V9.

### C5 — OODA Loop 3: capability loss cannot be healed by creating another role

**Observe.** Official OpenAI documentation marks Multi-agent beta, says schemas may change, exposes same-agent follow-up/wait/interrupt/list primitives, and warns against agents contending over shared mutable state: [OpenAI Multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent). Capability availability is runtime evidence, not a stable public Assisted promise.

**Attack.** The entire E8 role set was exercised conceptually:

| Attack | Required response |
|---|---|
| Capability disappears after role creation | stop new autonomous dispatch; let confirmed running work finish or manually stop; continue via existing filesystem traces/manual-complete |
| Follow-up target is wrong/ambiguous | verify canonical handle/status immediately before send; no best-match title fallback |
| Lost session is automatically recreated | forbidden; `stop-no-duplicate`; only explicit recorded supersession after confirmed termination can create a successor |
| Interrupt returns before idle | poll/observe until confirmed idle/interrupted; if confirmation unavailable, wait/manual stop |
| Executor/reviewer overlap | reviewer starts only from terminal RF/evidence; implementation writer lock rejects overlap |
| Delta-only re-review | same reviewer reopens complete TS/RF/implementation/evidence and reruns full acceptance |
| Worker reports to top-level/user | report is non-authoritative until present in phase trace and received by phase coordinator; top-level ignores bypass reports |

**Orient.** The base capability probe is necessary but not sufficient for the whole phase. The adapter must revalidate the target and operation before every dispatch. A runtime without general interrupt can still satisfy ordered non-overlapping work; it simply cannot live-reassign a running role.

**Decide.** `role-adapter-v1` survives with four final constraints:

1. capability/target verification occurs at phase start and before every create/follow-up/wait/interrupt;
2. no general interrupt means `wait-or-manual-stop`, not a degraded interrupt guess;
3. capability loss transitions remaining work to manual-complete using existing role/artifact lineage; it never creates an automatic duplicate;
4. if a lost session blocks the only role and termination cannot be proven, the phase stops for coordinator resolution rather than weakening single-writer/session topology.

The same reviewer remains independent because role independence is defined by ownership and full evidence re-evaluation, not by throwing away its session context. Reuse is compatible with full re-review.

**Act.** Retain Codex task sessions without interrupt as valid for the owner's sequential phase flow. Fail any promise that every runtime supports live interruption or recovery from an ambiguous lost session without a stop.

### C6 — OODA Loop 3: public-only changelog survives, but its 1.5 date is a release-time assertion

**Observe.** Git annotated tags have their own tagger/date/message, while the public Assisted baseline has no pointing tag. SemVer requires `X.Y.Z`, which exact `1.5` is not: [Git tag](https://git-scm.com/docs/git-tag.html), [Semantic Versioning 2.0.0](https://semver.org/).

**Attack.** Every E8 history/privacy case was applied:

- hardcoded `2026-08-30` is false if the public 1.5 release record is completed on a later date;
- repository `v1.0.0` cannot be presented as an Assisted 1.0 tag because it predates the Assisted baseline;
- downstream versions/dates/hashes remain private even when paraphrased;
- latest changelog, `VERSION`, manifest, policy, README/PROJECT, skills, migration, and templates can drift independently;
- a marker-free unique operational fact remains a semantic leak.

**Orient.** The changelog can be exact without tags. The 1.0 entry is a repository-baseline statement with a known public commit date, not a tagged-release statement. The 1.5 heading date must be written/verified at actual public release-record creation, not copied blindly from the research fixture.

**Decide.** Public-only history survives unchanged in authority and with one verification refinement:

- `VERSION` exact bytes are `1.5\n` and remain the sole machine authority;
- `CHANGELOG.md` contains only 1.5 and the public 1.0 baseline; no downstream provenance sentence or field release heading;
- 1.0 prose says repository baseline recorded 2026-08-09 and asserts no Assisted 1.0 release tag;
- 1.5 uses the actual public release-record date. If release has not occurred, it remains explicitly unreleased rather than receiving a predicted date;
- the text states MAJOR.MINOR and makes no SemVer claim;
- an automated agreement scan plus independent semantic review verifies all public product claims and artifacts.

No tag is required, created, or inferred. The generic reverse-promotion mechanism belongs in maintenance documentation, not changelog provenance.

**Act.** Fail predicted-date, tag-derived, SemVer, and private-provenance variants. Retain D11 Alt A.

### C7 — Claims that failed and claims that survived

| Claim | Verdict | Required correction/evidence |
|---|---|---|
| A local/fixed OS app-data root is universally nonsynchronized | **failed** | Bounded registered-provider threat model; explicit residual risk; session-only on incomplete evidence |
| Operator assertion alone can make locality `proven` | **failed** | Assertion is only one predicate alongside all mechanical evidence |
| Final-path symlink check/revalidation is race-safe | **failed** | Pinned root and platform handle-chain/no-follow adapter; unsupported -> session-only |
| A self-consistent JCS manifest authenticates its source | **failed** | It proves integrity/coherence only; repository selection/review supplies provenance |
| Current manifest/policy binding is acyclic | **survives** | Manifest excludes itself and includes policy; policy can bind only prior manifest hashes |
| Specificity resolver is order-independent | **survives conditionally** | Duplicate/tie/prefix-boundary invalid; canonical stored order still required |
| Exact private suppression counts are safe publicly | **failed** | Boolean suppression only; public counts cover public entries |
| One immutable report can be updated through all operation states | **failed** | Append-only private journal plus create-once terminal report |
| Private→public projection can be noninterfering | **survives conditionally** | Closed allowlist, no private hashes/counts, paired-report byte-equality fixture, semantic review |
| Arbitrary CSS is a safe offline overlay | **failed** | Strict six-property grammar; local shape-only asset; blocked-network render evidence |
| TI1 remains sufficient without a compiler rewrite | **survives conditionally** | Static validation, embedding, compatibility smoke render, visual/privacy evidence |
| Phase-start capability probe stays valid | **failed** | Re-probe target/operation before every dispatch and stop on loss |
| Interrupt request proves the writer stopped | **failed** | Confirm idle/interrupted or wait/manual stop |
| One executor/reviewer session can be reused | **survives** | No duplicate-on-loss; single writer; full re-review every cycle |
| Research fixture date is automatically the 1.5 release date | **failed** | Use actual release-record date or explicit unreleased state |
| Public-only Assisted changelog is truthful without tags | **survives** | Baseline wording, no SemVer/private history, full version agreement |
| `X2-refined` satisfies the frozen product contract | **survives conditionally** | All V1–V12 obligations below remain mandatory implementation evidence |

### C8 — Final implementation obligations

| ID | Obligation | Passing evidence |
|---|---|---|
| V1 | Portable release paths | duplicate-key-rejecting parser; exact/NFC/casefold/reserved/traversal/regular-file/link tests; fixed required paths; JCS/domain validation |
| V2 | Coherent acyclic transition | generated policy→manifest build graph; self-entry/current-manifest-policy fields rejected; policy required in manifest; prior manifest/version/interface edge agrees with `VERSION` and changelog |
| V3 | Complete preflight and race handling | verified immutable source staging; project lock; full destination baseline immediately before first write; prewrite drift -> zero writes; per-path recheck and postcondition |
| V4 | Partial-failure honesty | failure injected after first mutation; append-only journal existed before write; create-once terminal `partial`; recovery creates new linked report; original never becomes verified |
| V5 | Ownership preservation | work, knowledge, people, identity, profiles, modified templates/overlay, unknown paths, and unrelated `.codex` remain byte-identical; modified retired hook preserved/quarantined |
| V6 | Reverse privacy/report derivation | paired private reports differing only in secret details yield identical public bytes/ID; no private path/hash/count/timestamp/ID; semantic reviewer accepts; current mixed field remains P6 candidate-only |
| V7 | Identity zero-write fallback | every unsafe/unknown/probe/ACL/lock/corrupt/unsupported case produces no persistent directory, lock, temp, registry, diagnostic identity, or selection |
| V8 | Identity operation-time safety | Windows reparse and Unix ancestor/mount swap fixtures; pinned-root safe primitive; live OS lock; revalidation every binding operation; unsupported adapter returns session-only |
| V9 | Template usefulness/offline/privacy | strict overlay grammar attacks; shape-only SVG attacks; blocked-network stock/custom A4 and presentation renders; glyph/long-table/background-disabled checks; pages/screenshots/hashes; semantic privacy review |
| V10 | Version/history truth | exact `VERSION=1.5`; all public claims agree; actual 1.5 date; public 1.0 baseline wording; no Assisted tag dependency, SemVer claim, downstream headings, or private provenance |
| V11 | Reusable-role capability gate | initial/per-dispatch probes; one coordinator/executor/reviewer; same-handle correction; full re-review; no overlap/bypass/duplicate; capability loss and no-interrupt fall back to wait/manual-complete |
| V12 | Both directions | clean overlay-separated P2 forward/reviewed reverse fixtures have before/after records and zero unexplained changes; real mixed field uses non-mutating P6 until clean separation exists |

### C9 — Hypothesis outcomes, residual risks, and sufficiency

| Hypothesis | Challenge outcome |
|---|---|
| H1 | **Survives with a bounded proof model.** Universal non-synchronization fails, but explicit `operational-local-v1` plus zero-write session fallback satisfies the frozen behavior. |
| H2 | **Survives as an acyclic compound contract.** Self-cycle prevention passes; integrity is not authentication; automatic P2 is limited to clean overlay-separated state and current mixed lineage remains P6. |
| H3 | **Survives after restricting TI1.** Arbitrary CSS fails; six-property overlay, shape-only local asset, interface gate, and executed render/privacy evidence are sufficient in principle. |
| H4 | **Survives unchanged.** Russian remains 1.5 authority; public-only history is truthful without a tag or English mirror. |

Residual risks that implementation cannot erase:

1. An undeclared or malicious same-user synchronizer can copy a local state directory after a successful probe. The contract discloses this and revalidates registered evidence; it does not claim hostile same-user confinement.
2. JCS/manifests do not authenticate source origin. This phase relies on reviewed repository/source selection; signing/TUF-style freshness is later hardening.
3. A multi-file update on a shared or cloud-synchronized destination is not a distributed transaction. Clean local fixtures can use P2; current mixed/shared lineage uses P6 and partial states remain explicit.
4. System fonts and renderers vary. Acceptance is readable/useful offline output, not pixel identity.
5. Semantic privacy and usefulness review remains human judgment; deterministic schemas/scans reduce but do not eliminate reviewer error.
6. Runtime task/multi-agent capabilities are beta/changeable; manual-complete remains normative and an ambiguous lost role can block a phase rather than permit duplication.

**Sufficiency recommendation:** iteration 2 is research-complete. `X2-refined`, V1–V12, and the residual-risk statements are precise enough for TS and falsifiable implementation evidence. A third research iteration would repeat implementation work rather than close a frozen-claim gap. After coordinator acceptance, synthesize RES and proceed through the normal plan/handoff/review gates.

- **Refinements:** bounded locality semantics; live OS lock/handle-chain requirement; explicit acyclic build graph; safe-integer/domain validation; immutable source staging; append-only journal + terminal report; boolean private suppression and paired-report noninterference; restricted TI1 grammar/shape-only SVG; per-dispatch capability probe; actual release-date check.
- **Amendment proposals:** none. Failed claims are stronger implementation interpretations that the frozen HL does not require. The frozen lifecycle, identity fallback, classified maintenance directions, template usefulness/privacy, language authority, and reusable-role topology remain satisfiable.

## Checkpoint

| Found | Remaining |
|---|---|
| All 66 dimension pairs checked; 20 incompatible alternative pairs; every E8 attack handled; 10 implementation claims failed and 7 claims survived conditionally or fully; `X2-refined`, X1/X6/P6 fallbacks survive; V1–V12 finalized; six residual risks disclosed; no amendment | Coordinator acceptance, then synthesize iteration-2 RES and commit scoped research traces; implementation/render/platform evidence belongs to handoff/review |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked and survivors listed?
- [x] Every Extract E8 attack handled?
- [x] Counter-evidence changed overstrong claims?
- [x] Final implementation obligations and residual risks explicit?
- [x] Amendment proposals classified?

**Deep-mode exit:** three OODA loops completed; all selected contracts were attacked; public-count, mutable-report, unrestricted-CSS, universal-locality, stable-capability, and predicted-date interpretations failed; the refined compound configuration remains falsifiable and sufficient.

**Metacognitive check:** Challenge did not merely confirm Extract. It removed exact private counts from public reports, moved mutable states into an append-only journal, restricted the CSS overlay to a six-property grammar, narrowed `proven` to a registered-provider threat model, and made capability verification per-dispatch rather than phase-start-only.

Stage complete: YES
→ Phase Coordinator decision: recommend close Challenge, synthesize iteration-2 RES, and do not open iteration 3
