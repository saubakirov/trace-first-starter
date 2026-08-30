# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260830-114238_ASSISTED15](../../HL-TFW_20260830-114238_ASSISTED15.md)
> Goal: Deliver a standalone, organizationally neutral Assisted 1.5 whose lifecycle, identity, update discipline, and practical templates are derived from the read-only Innoforce field lineage and maintained through an explicit public-core/private-overlay boundary.

## Consistency Check

All 36 dimension pairs were checked. `S` means the selected alternatives are independent and can coexist; `C` means they coexist only with an explicit condition listed below. No selected pair is unconditionally incompatible after the refinements in this stage.

| Pair | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 |
|---|---|---|---|---|---|---|---|---|---|
| D1: Path authority | — | C | C | C | S | C | S | S | C |
| D2: Direction model |  | — | C | C | S | C | S | C | C |
| D3: Baseline proof |  |  | — | C | S | C | S | S | C |
| D4: Mutation primitive |  |  |  | — | S | C | S | C | C |
| D5: Participant state |  |  |  |  | — | S | S | C | S |
| D6: Template ownership |  |  |  |  |  | — | C | S | C |
| D7: Language authority |  |  |  |  |  |  | — | S | C |
| D8: Orchestration |  |  |  |  |  |  |  | — | S |
| D9: Release history |  |  |  |  |  |  |  |  | — |

**Incompatible alternative pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D1 | downstream-only path | D2 | public → downstream mutation of that path | Public has no authority to mutate downstream state |
| D1 | stock-customizable path | D4 | unconditional whole-directory replacement | Customization would be silently overwritten |
| D1 | retired/quarantine path | D4 | unconditional replacement | Retirement cannot coexist with reinstalling the payload |
| D1 | public-core history path | D9 | literal field history | The same public path would have two release authorities |
| D2 | symmetric mirror | D6 | downstream brand overlay | A mirror necessarily imports or deletes one side's owned material |
| D2 | reviewed reverse promotion | D4 | automatic reverse application | Review cannot occur after the public mutation it is meant to authorize |
| D2 | public-only forward | D9 | claim of completed reverse provenance | History would assert a direction the mechanism does not support |
| D3 | version label only | D4 | hash-gated replacement | There is no stock-content fact against which to gate |
| D3 | unbound per-file hashes | D2 | multi-file release update | Files from different releases can form a valid-hash but inconsistent view |
| D4 | three-way text merge | D6 | binary asset | The primitive has no meaningful binary merge semantics |
| D4 | whole-directory replacement | D6 | stock-customizable or overlay | It erases the ownership boundary |
| D5 | package/shared persistent state | D1 | public package or downstream shared state | It copies current-participant state into a shared authority domain |
| D5 | conventional per-user path without locality proof | D8 | silent autonomous persistence | Automation would turn an uncertain path into an unreviewed cross-device claim |
| D6 | independently maintained localized templates | D7 | one authoritative language without source linkage | Both copies would claim authority and drift silently |
| D8 | mandatory task operations | D2 | portable manual fallback | A mandatory unavailable API makes the fallback false |
| D9 | history generated only from tags | D3 | this untagged 1.5 release baseline | The owner forbids tag creation in this task, so tags cannot be the current authority |

**Surviving configurations:**

| Config | D1/D2 | D3/D4 | D5/D8 | D6/D7/D9 | Notes |
|---|---|---|---|---|---|
| `P2 × R1` | classified paths; asymmetric directions | release-bound hashes; gated forward and reviewed reverse | proven-local or session-only; capability-gated auto/manual | neutral stock + overlay; Russian; separated provenance | Survives as the complete target, with all obligations below |
| `P2 × R2` | same maintenance boundary | same release-bound gating | session-only; manual | same product authorities | Survives as mandatory portable fallback |
| `P6 × R1` | classified paths; asymmetric directions | hashes; manual reconstruction/new-only | proven-local or session-only; capability-gated coordination | stock protected; Russian; separated provenance | Survives and is required for today's mixed field files |
| `P4 × R1` | same as P2 | authenticated release metadata plus P2 operations | same as R1 | same as P2 | Survives only as later hardening with rollback/consistent-snapshot rules |

**Unexpected survivors:**

- `P2 × R2`: session-only identity and manual lifecycle preserve the entire safety contract; persistence and autonomous tasks are conveniences, not prerequisites for a valid Assisted run.
- `P6 × R1`: although slower, manual reconstruction is not merely an emergency option. It is the only honest initial bridge for field files that currently mix universal behavior and downstream context at one path.

## Findings

### C1 — OODA Loop 1: hostile paths, inconsistent releases, and the real two-direction bridge

**Observe — paths.** A read-only portability scan over the current 9-file public tree and 29-file field 1.5 tree found zero NFC/case-insensitive collisions, zero reparse-point files, and zero Windows-reserved/invalid path components. That is evidence about these two snapshots, not a property of future releases.

Unicode defines canonically equivalent strings that obtain the same binary form only after normalization: [Unicode UAX #15](https://www.unicode.org/reports/tr15/). Windows explicitly says not to assume case sensitivity, reserves names and characters, and rejects trailing spaces/periods: [Microsoft file naming rules](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file). APFS can be case-sensitive or insensitive and preserves original normalization while comparing normalization-insensitively: [Apple APFS FAQ](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/FAQ/FAQ.html).

**Attack.** NFC alone misses `README.md` versus `readme.md` on default Windows; case-folding alone would incorrectly rename distinct files on a case-sensitive target; hashing before rejecting `..`, absolute paths, reserved names, or symlinks can validate a path that escapes the intended root. A check-then-open sequence can also race with an ancestor being replaced. Python's official documentation calls out check/open race hazards and provides descriptor-relative and no-follow operations only where the platform supports them: [Python OS interfaces](https://docs.python.org/3/library/os.html).

**Decide — path contract.** Preserve exact spelling for access and hash, but compute a separate portable collision key using declared NFC plus case-insensitive comparison. Reject rather than rename any collision, absolute path, `.`/`..` segment, NUL/control/reserved component, trailing space/period, path outside the root, symlink/reparse point, or non-regular release entry. Immediately before mutation, re-open/re-resolve the target beneath a pinned root and recheck its baseline. If safe no-follow/root-relative primitives or equivalent platform checks are unavailable, fall back to non-mutating comparison/manual action.

**Observe — release consistency.** Extract's per-file accepted-stock list can still accept a signed or correctly hashed stale release, or mix a manifest from one release with files from another. TUF uses snapshot metadata to bind hashes/versions into a consistent repository view and timestamp metadata to detect stale views: [TUF roles and metadata](https://theupdateframework.io/docs/metadata/). Full TUF is unnecessary for a local gated updater, but the counterexample is decisive.

**Decide — update state machine.** Every operation must pin one source tree digest and one directed transition edge before the gate:

1. `installed VERSION == from_version` and source `VERSION == to_version`.
2. The migration graph explicitly allows `from → to`; downgrade and undeclared same-version correction stop.
3. Manifest, policy, source files, and tree digest all belong to `to_version` and are rehashed immediately before first write.
4. All destination baselines are checked before any write; a changed baseline invalidates the whole plan.
5. The operation journals each per-file result and retained recovery copy. Local per-file replacement is not described as a multi-file transaction.
6. Post-manifest must equal the expected per-class postconditions with zero unexplained changes; partial failure remains explicit and recoverable, never reported as success.

**Attack — current field bridge.** All six paths shared by public 1.0 and field 1.5 differ. Several field root contracts and templates mix universal behavior with downstream wording at the same path. Therefore P2's known-stock automatic forward rule cannot update the current real field tree without either losing downstream context or silently merging it. Marker removal does not solve semantic coupling, and a reverse marker scan cannot prove that a practice is universal.

**Decide — two directions.** P2 may be demonstrated automatically only on clean fixtures whose overlay is already separated. The real read-only field tree initially uses P6 in both directions: generate a non-mutating candidate, semantically reconstruct/neutralize it, independently review it, and then apply it under the destination's own task. `git apply --check` can test patch applicability without applying it, but applicability is not privacy or authority approval: [Git apply](https://git-scm.com/docs/git-apply). Once the downstream distribution adopts a clean overlay boundary, known-stock forward updates may graduate to P2.

**Act.** Add path portability, transition pinning, partial-failure, and both clean-fixture/manual-real-lineage cases to the verification obligations.

### C2 — OODA Loop 2: local identity and neutral templates fail at their convenience boundaries

**Observe — identity.** The field contract already says to use session-only state when machine-local storage cannot be proven. The implementation, however, chooses `%LOCALAPPDATA%`, `~/Library/Application Support`, or `${XDG_STATE_HOME:-~/.local/state}` and only rejects the project, inferred marker roots, declared shared roots, and an existing final-path symlink. It performs no positive volume-locality probe, does not reject every ancestor reparse/symlink after validation, and returns the original path after resolving it for the check.

**Attack.** A cloud client can synchronize an ordinary local volume, so “fixed/local disk” alone still does not prove non-synchronization. A provider can use an unrecognized folder name. An ancestor can change between `resolve()` and lock/temp creation. An existing permissive parent can let another OS user alter attribution state. A failed persistent write can also leak identity if the supposed session fallback creates a directory, lock, temp, or diagnostic containing the participant.

**Decide — identity survivor.** H1 does not survive with the source implementation copied unchanged. It survives at the contract level only if the public script:

- returns `proven | unsafe | unknown` from an explicit locality gate and persists only `proven`;
- combines OS/volume evidence with project/shared/provider-root exclusion and caller-declared shared roots, while treating any uncertainty as no-write;
- checks the full existing ancestor chain for symlink/reparse escape and uses safe operation-time handles where supported;
- checks that an existing store is a regular, privately controlled file and that a foreign lock/corrupt schema never selects a profile;
- implements a real session-only path that performs zero filesystem writes and stores no participant outside active chat context;
- keeps attribution explicitly non-authenticating.

No cross-platform implementation can honestly promise persistent binding everywhere. A platform that lacks reliable probes remains fully usable through R2.

**Observe — templates.** The field A4 builder is standard-library-only and its inline text is escaped, but it hardcodes the company asset and an external Google Fonts URL. The presentation also loads a web font and hardcodes the same asset. The current useful semantics therefore survive static extraction, while offline determinism and neutral output do not.

**Attack.** Removing visible brand text but retaining the asset, asset metadata, remote request, branded alt text, house examples, or color/logo assumption still leaks coupling. Replacing everything with empty placeholders satisfies a marker scan but fails usefulness. A custom template can remain byte-preserved yet become unusable if an updated builder renames its asset contract. Long tables, Cyrillic/Latin mixtures, missing assets, and print pagination can render unreadably even when HTML generation exits zero.

**Decide — template survivor.** H3 survives only under execution evidence, not static confidence. The public set must have complete generic Russian worked examples, a newly produced neutral asset whose metadata is inspected, local font fallbacks with zero required `http(s)` resources, and an optional documented overlay interface. The builder's CLI validates arguments and requested assets. A customized template is byte-preserved on update; if its dependency contract changes, the update reports incompatibility rather than declaring success.

**Act.** Require at least these render fixtures later: stock offline A4; stock offline presentation/print; long Cyrillic/Latin headings and tables; neutral asset metadata scan; valid custom overlay; requested missing asset failure; customized old template preserved across update. Evidence must include execution command, exit status, output hashes, page/slide count, screenshots or rendered pages, and a private-marker scan.

### C3 — OODA Loop 3: truthful history and reusable sessions under missing capabilities

**Observe — version/changelog.** `VERSION=1.5` is frozen, but the previous public package has no machine-readable version file or changelog and only declares 1.0 in prose. The actual date of the original public 1.0 release is not established by the inspected package. The field has its own 1.1–1.5 sequence. No tag will be created in this task.

**Attack.** Backfilling a guessed 1.0 date, presenting field 1.1–1.4 as public releases, calling two-component `1.5` SemVer, or generating history only from absent tags would each make the changelog look precise while being false. Even a private-file hash or path in a public promotion report can leak equality or structure without copying file contents. A brand-marker allowlist can grow until it masks a real leak.

**Decide — history survivor.** `VERSION` is the only machine-readable public version authority. `PROJECT.md`, README, skills, migration, and templates must agree with exact `1.5`; no separate compatibility field may visibly claim edition 1.0. The changelog contains public 1.5 and a clearly labelled historical 1.0 baseline, with an unknown date left unknown rather than invented. A short provenance note says private downstream iterations informed 1.5 but are not public releases; it includes no downstream release-by-release facts, people, paths, hashes, or assets. Reverse operation reports aggregate excluded private classes/counts and keep sensitive path/hash detail only in private evidence.

**Observe — capabilities.** Official OpenAI guidance marks multi-agent as beta and requires explicit autonomy, routing, output, retry, and stop boundaries: [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model). Exact create/title/wait/read/follow-up operations therefore remain runtime evidence, not a universal product promise.

**Attack.** A runtime may create but not re-target a task, wait but not verify identity, rename but not report completion, or lose a task after interruption. Silently creating a replacement breaks the owner's one-session-per-role rule. Reusing one reviewer can also degrade into checking only previously failed points instead of independently rerunning acceptance.

**Decide — orchestration survivor.** Before autonomous mode, one capability transaction must prove: create-or-attach one role session, stable follow-up targeting, status/completion observation, coordinator-directed report delivery, and role identity verification. Exact visible title is used when available; it cannot substitute for the stable handle/report contract. If any operation is absent or fails, do not partially automate: issue the exact manual role transition and stop. If an existing role session is lost, do not silently create a second one for the phase. The same reviewer may be reused, but every re-review reruns the complete DoD/DoF and fresh evidence, not only the prior defect list.

**Act.** Make reusable-role behavior an executable scenario: coordinator creates one executor and one reviewer; FAIL returns to the same executor; corrected RF returns to the same reviewer; writer overlap is rejected; only the coordinator receives child reports; the owner receives one final package.

### C4 — Claims that failed and claims that survived

| Claim | Verdict | Required correction or evidence |
|---|---|---|
| Current path sets are portable, therefore future manifests are safe | **failed** | Validate every source and destination snapshot for NFC/case collisions, reserved names, traversal, and link/reparse escape |
| Per-file hashes alone bind a coherent release | **failed** | Pin source tree digest, transition edge, manifest/policy version, and full preflight before mutation |
| P2 can automatically update today's real field 1.5 | **failed** | Use P6 candidate/manual integration until mixed paths are separated into overlay-owned surfaces |
| Marker scan is sufficient for reverse privacy | **failed** | Default-deny path classes plus semantic review; private paths/hashes stay out of public reports |
| A conventional OS app-data directory proves machine-local state | **failed** | Positive locality gate; unknown/unsafe is zero-write session-only |
| The field builder is already neutral and offline deterministic | **failed** | Remove brand/remote dependencies, add neutral asset and execute render fixtures |
| Signed manifest alone makes an updater fresh and safe | **failed** | Authenticated metadata still needs version/consistent-view/ownership/mutation rules |
| Exact task operations exist everywhere | **failed** | Capability transaction and complete manual fallback |
| Russian is the 1.5 content authority | **survives** | No unsynchronized English mirror; machine enums remain language-neutral |
| One executor and one reviewer can be reused per phase | **survives** | Stable targeting, no replacement-on-loss, full re-review, single writer |
| Exact known-stock hooks can be removed safely | **survives** | Per-file hash; modified hook quarantine/surgical deactivation; unrelated `.codex` preservation |
| `VERSION=1.5` plus separated public/private history is coherent | **survives** | Do not invent public dates, SemVer claim, or field public releases |
| Candidate-only reviewed reverse promotion is safe in principle | **survives** | Applicability, neutrality, authority, and independent review are separate gates |

### C5 — Verification obligations for TS and implementation

| ID | Obligation | Passing evidence |
|---|---|---|
| V1 | Portable release paths | Exact/NFC/case collision, Windows-reserved, traversal, symlink/reparse, regular-file tests on source and fixture targets; current 9/29 snapshots remain clean |
| V2 | Coherent transition | Declared `from → to`, pinned source digest, matching manifest/policy/VERSION, downgrade and mixed-release rejection |
| V3 | Complete preflight and race stop | All baselines checked before first write; changed target/source after plan causes zero further writes |
| V4 | Partial-failure honesty | Inject failure after one staged mutation; journal and recovery copies identify partial state; success is impossible until exact postconditions hold |
| V5 | Ownership preservation | Work, knowledge, people, project identity, profiles, customized template, unrelated `.codex`, overlay, and unknown path stay byte-identical |
| V6 | Reverse privacy/authority | Branded/private/unknown and semantically company-specific fixtures rejected; public candidate has no sensitive path/hash/content and requires independent approval |
| V7 | Identity zero-write fallback | Unsafe/unknown location, remote/sync root, probe error, corrupt registry, foreign lock, and Full namespace yield no persistent Assisted write/selection |
| V8 | Identity path race | Final/ancestor symlink or reparse substitution cannot redirect lock/temp/registry; unsupported safe primitives cause session-only |
| V9 | Template usefulness and neutrality | Offline A4/presentation renders, readable long/table/Cyrillic/Latin fixtures, neutral asset metadata, missing override failure, zero required network/brand/private markers |
| V10 | Version/history truth | `VERSION` exact 1.5; all product references agree; public 1.0 date not invented; field iterations not public release headings; no tag dependency |
| V11 | Reusable-role capability gate | One coordinator/executor/reviewer, same-session retry, full re-review, single writer, coordinator-only child reports, manual fallback on every missing operation |
| V12 | Both directions | Clean-fixture P2 forward and reviewed reverse have before/after manifests and zero unexplained changes; current mixed lineage uses non-mutating P6 evidence only |

### C6 — Hypothesis outcome, remaining gaps, and recommendation

| Hypothesis | Challenge outcome |
|---|---|
| H1 | **Survives at contract level, source implementation fails as-is.** Copying it would weaken locality safety; refined implementation plus R2 preserves the frozen claim. |
| H2 | **Survives only as the compound P2/P6 state machine.** Manifest + diff is necessary but not sufficient; current real lineage starts with P6. |
| H3 | **Survives structurally, not yet empirically.** Neutral/offline execution evidence remains mandatory implementation work. |
| H4 | **Survives.** Russian is the only 1.5 content authority; localization remains a separate source-linked release decision. |

Remaining gaps are implementation-specific rather than research-claim gaps: exact cross-platform locality probes and safe-handle fallbacks; final manifest serialization/path-rule ordering; the neutral asset/theme interface; actual runtime capability combinations; and rendered evidence from the implemented public files.

**Recommendation:** retain `P2 × R1` as target, make `P2 × R2` and `P6 × R1` normative fallbacks, and carry V1–V12 unchanged into TS acceptance. Treat any attempt to automate the current mixed field tree, persist identity on `unknown`, or waive offline render evidence as a failure rather than an optimization.

- **Refinements:** release-bound transition graph; portable collision key plus exact path; operation-time link defense; partial-write journal; P6 mandatory for the current mixed lineage; zero-write identity fallback; private path/hash suppression; no invented 1.0 date; full re-review in the same reviewer session.
- **Amendment proposals:** none. The failed claims were implementation interpretations, not frozen target-state, DoD/DoF, phase, gate, or scope claims.

## Checkpoint

| Found | Remaining |
|---|---|
| All 36 dimension pairs checked; 16 incompatible alternative pairs; 8 implementation claims failed; 5 core claims survived conditionally; V1–V12 define executable obligations; real field bridge correctly narrowed to P6 first | Implement and execute platform, migration, capability, privacy, and render fixtures; no unresolved research question requires changing frozen HL |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?

**Deep-mode exit:** 7 Challenge decisions recorded; H1–H4 attacked; counter-evidence invalidated eight implementation claims; three OODA loops completed.

**Metacognitive check:** The strongest unexpected result was that a safe maintenance bridge does not imply an automatic bridge. Because today's field distribution is mixed at the file-content level, manual reviewed reconstruction is a first-class success path, not a missing feature.

Stage complete: YES
→ Phase Coordinator decision: recommend close Challenge and start iteration 2 rather than synthesize RES yet
