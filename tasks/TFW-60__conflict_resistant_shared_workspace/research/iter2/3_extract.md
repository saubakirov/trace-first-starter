# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md)
> Goal: Make concurrent human and agent work in a synchronized TFW workspace conflict-resistant by moving normal lifecycle state and coordination to stable task-local, single-writer surfaces while retaining discoverability and Git provenance.

## Configuration Space

The 15 Gather dimensions produce too many Cartesian combinations to render usefully. The matrices below retain coherent combinations where at least one dimension differs from the C1-R baseline. They do not select or eliminate configurations; evaluation follows in Findings and final elimination remains for Challenge.

### T1 — catalogue, control and reader combinations

| Config | D1. Portfolio entry | D2. Derived-index condition | D3. Task-control shape | D4. Reader behaviour | D5. Usability evidence | D6. Status field admission | D7. YAML acceptance |
|--------|---------------------|-----------------------------|------------------------|----------------------|------------------------|----------------------------|---------------------|
| T1-A | permanent router + persisted derived index | normal | strict valid control | re-read task authority | FA + DF | all 20 fields required | strict application subset |
| T1-B | permanent router + persisted derived index | normal | strict valid control | re-read task authority | FA + DF | shared core + conditional/profile/derived fields | strict application subset |
| T1-C | permanent router + persisted derived index | absent | strict valid plus recognized legacy | scan controls and report legacy | FA + DF | shared core + conditional/profile/derived fields | strict application subset |
| T1-D | permanent router + persisted derived index | stale | strict valid control | compare then re-read authority | FA + DF | shared core + conditional/profile/derived fields | strict application subset |
| T1-E | permanent router + persisted derived index | malformed | valid/legacy/malformed mix | quarantine view and scan controls | FA + DF | shared core + conditional/profile/derived fields | strict application subset |
| T1-F | permanent router + persisted derived index | normal | recognized legacy without control | display verified facts and unknowns | UH + RR | no fabricated standard control | compatibility resolver over existing artifacts |
| T1-G | permanent router + on-demand view | absent by design | standardized task artifacts | derive from artifact graph | PS | derived state | no YAML control |
| T1-H | external/service catalogue | normal service view | database record | trust transactional authority | PS | service schema | database constraints |

T1-B is a combination not present in iteration 1: it retains C1-R's strict control and persisted view while shrinking the authoritative status surface rather than making all 20 candidate fields mandatory.

### T2 — recovery and rollover combinations

| Config | D8. Recovery authority | D9. Journal/snapshot visibility | D10. Journal segmentation |
|--------|------------------------|----------------------------------|---------------------------|
| T2-A | current state owner | aligned | combined first-hit count + encoded bytes |
| T2-B | current state owner | journal ahead at current epoch | combined first-hit count + encoded bytes |
| T2-C | predeclared recovery authority with incremented epoch | stale old-owner branch | combined first-hit count + encoded bytes |
| T2-D | predeclared recovery authority | same-epoch divergence | combined first-hit count + encoded bytes |
| T2-E | timestamp/latest-writer selection | divergent valid-looking branches | count-only ceiling |
| T2-F | lock/lease service | aligned transactional record | database retention policy |
| T2-G | current state owner | aligned | time/phase/manual segmentation |

### T3 — landing, Git and migration combinations

| Config | D11. Landing trace order | D12. Git profile | D13. Git scope gate | D14. Migration action | D15. Edition boundary |
|--------|--------------------------|------------------|----------------------|-----------------------|-----------------------|
| T3-A | post-commit `landed` task event | G-B | literal exact allowlist | preserve path/import verified facts | shared semantic kernel + profiles |
| T3-B | commit-only landing evidence | G-B | literal exact allowlist | preserve path/import verified facts | shared semantic kernel + profiles |
| T3-C | pre-landing handoff/manifest plus commit | G-B | manifest digest + literal exact allowlist | preserve path/import verified facts | shared semantic kernel + profiles |
| T3-D | second commit containing landing event | G-B | literal exact allowlist per commit | preserve path/import verified facts | shared semantic kernel + profiles |
| T3-E | pre-landing handoff/manifest plus commit | guarded G-A with pinned local paths | manifest digest + literal exact allowlist | preserve path/import verified facts | shared semantic kernel + profiles |
| T3-F | commit-only landing evidence | per-peer G-C | task-directory pathspec | move/normalize legacy folder | separate edition models |
| T3-G | no Git completion | no-Git Assisted profile | profile artifact boundary | preserve legacy path | shared semantic kernel + profiles |

T3-C/T3-E expose the second new combination: the task journal records pre-landing intent and exact provenance, while a reachable commit matched by digest supplies the completed landing fact. It requires neither a post-commit task edit nor a task file that predicts its own commit hash.

## Findings

### E1. Extracted Phase-A configuration C1-R2

Cross-referencing the three matrices yields a revised configuration to carry into Challenge:

```text
PERMANENT ENTRY / DISPOSABLE PROJECTION
README router → persisted tasks/INDEX.md
                      │ select, then re-read
                      ▼
TASK-LOCAL AUTHORITY                    TASK-LOCAL JOURNAL
strict status.yaml                     numbered immutable JSONL segments
9-field shared core                    closed event vocabulary
state-dependent conditionals           one normal writer + owner_epoch
profile fields only when needed        event-first / snapshot-second
derived timestamps stay out            combined count + byte rollover
                      │ ordinary independent-file propagation
                      ▼
FILE-SYNC TRANSPORT FLOOR
no order, lock, transaction or authority claim
                      │
                      ▼
GIT LANDING
G-B baseline / guarded pinned-path G-A optional Full
pre-landing handoff manifest + exact literal allowlist
one commit contains results + producer attribution
reachable matching commit = derived landing completion
                      │
                      ▼
COMPATIBILITY RESOLVER
preserve every legacy path; import only verified facts;
unresolved/malformed tasks stay visible and non-actionable
```

C1-R2 preserves iteration-1 responsibility separation while revising four details:

1. the status schema has a nine-field shared required core rather than 20 universally required fields;
2. `landed` moves from the task event grammar to a derived Git completion fact paired with a pre-landing handoff;
3. rollover is structurally count-plus-encoded-bytes with unresolved configurable values;
4. guarded G-A compares Git observations with separately pinned local expectations and a supported-version/capability gate.

No Gather counter-evidence defeats the C1-R invariant that ordinary synchronized files need one task-local authority, explicit recovery and a disposable projection. Spec Kit/OpenSpec depend on standardized artifacts; GSD Pi depends on a local transactional database; neither solves this heterogeneous, unordered file-sync case without changing the frozen Phase-A boundary. C2–C5 and G-C therefore remain closed pending Challenge rather than reopening by familiarity.

### E2. Smallest shared required status core

The admission test is strict: a field remains universally required only when every supported edition has a shared reader and a creation/change trigger that cannot be supplied safely by a conditional, profile or derived source.

#### Required shared core — present in every valid standard control

| Field | Shared reader | Trigger/reason |
|-------|---------------|----------------|
| `schema_version` | validator/migrator | creation and every parse; unknown versions stop |
| `task_id` | catalogue, resolver, Git scope gate | creation; immutable; must match resolved task identity |
| `goal_summary` | human/agent portfolio reader | creation or approved goal amendment; bounded discovery text |
| `value_summary` | human/agent prioritizer | creation or approved value amendment; bounded outcome text |
| `lifecycle` | resume, release, catalogue | every material lifecycle transition |
| `state_owner` | write guard/recovery reader | creation or authorized ownership change |
| `owner_epoch` | reconciler/write guard | creation at 1; increment only through authorized ownership change |
| `last_event_id` | reconciliation and cold-start reader | every journal event reflected by the snapshot |
| `journal_head` | bounded-history loader | creation and segment rollover |

The shared core is nine fields. `state_owner` remains on terminal records as provenance even though terminal state is immutable in normal operation. `journal_head` remains explicit because directory ordering and legacy segment names are not safe authority.

#### Conditional shared fields — required only when their predicate holds

| Field | Predicate | Reader/trigger | Invalid combination |
|-------|-----------|----------------|---------------------|
| `goal_ref` | a verified canonical goal/scope source exists | scope reader; creation/amendment/migration | invented HL/proposal path |
| `waiting_on` | lifecycle is `waiting` or `blocked` | owner/resume reader; entry/exit from those states | waiting/blocked with no bounded kind + ref |
| `next_action` | lifecycle is non-terminal | cold-start reader; creation/handoff/transition | non-terminal with no bounded imperative |
| `next_ref` | lifecycle is non-terminal | cold-start reader; same trigger as next action | copied plan detail or a nonexistent reference |
| `terminal_outcome` | lifecycle is `terminal` | release/catalogue; terminal transition | non-terminal value or value outside `done|rejected` |
| `terminal_ref` | lifecycle is `terminal` | release/auditor; terminal transition | terminal assertion without controlling evidence |

For migrated legacy tasks, an absent verified `goal_ref` is allowed and reported; a path is never guessed. A task lacking any *required core fact* does not receive a fabricated valid standard control: the compatibility resolver reports it as unresolved and workflows stop for that task until an authorized owner supplies the fact.

#### Edition/profile fields — closed and validated when the selected profile uses them

| Field | Profile reader | Disposition |
|-------|----------------|-------------|
| `workflow_stage` | Full workflow router or Assisted adapter | remove from shared required core; edition profile defines vocabulary and whether it is present |
| `ownership_profile` | role/file validator | remove from shared required core; project/edition supplies a versioned default, with a task-local override only when history requires a pinned variant |
| `roles` | dispatcher and artifact ownership validator | remove from shared required core; emit only for profiles with concurrent named roles; `state_owner` alone remains shared |

#### Derived fields — removed from authoritative `status.yaml`

| Field | Derivation | Why not authoritative |
|-------|------------|-----------------------|
| `status_since` | time of the journal transition that established current lifecycle/stage | useful for stale-work display, but cannot order branches or authorize recovery |
| `updated_at` | last reflected event time and/or projection generation metadata | snapshot rewrite time is neither lifecycle age nor conflict authority; provider filesystem times are unsuitable |

The derived index may display both values with their derivation label. They cannot participate in branch choice, and removing them reduces snapshot churn.

Strict YAML remains a validator-owned subset: unique keys; no anchors, aliases, custom tags or directives; closed fields; bounded scalar/mapping shapes; fail-closed enum and reference checks. The [YAML 1.2.2 specification](https://yaml.org/spec/1.2.2/) supplies the language contract but not this application profile.

### E3. Shared lifecycle and state-dependent legality

The minimized fields preserve the iteration-1 shared lifecycle kernel:

| Lifecycle | Required conditional state | Prohibited state | Profile examples |
|-----------|----------------------------|------------------|------------------|
| `new` | next action + ref | waiting/terminal fields | Full `HL_DRAFT`; Assisted `new` |
| `active` | next action + ref | waiting/terminal fields | research, planning, execution, review work in progress |
| `waiting` | next action + ref + `waiting_on` | terminal fields | gate verdict, reviewer, owner or landing dependency |
| `blocked` | next action + ref + `waiting_on` | terminal fields | external dependency or declared failure condition |
| `terminal` | outcome `done|rejected` + terminal ref | next/waiting fields | completed or deliberately rejected immutable trace |

`workflow_stage` refines a lifecycle but never changes these meanings. An Assisted `review` directory can map to `waiting` only when the trace actually says it is awaiting review; otherwise the mapping remains unresolved rather than guessing. Terminal work is not reopened; changed intent creates a successor or an approved amendment trace.

### E4. Event vocabulary and field dispositions

The task journal remains management history, not a second artifact body.

| Event kind | Disposition | Trigger and reader |
|------------|-------------|--------------------|
| `created` | keep shared | first event; establishes initial core snapshot |
| `transition` | keep shared | lifecycle change; block/resume are typed deltas, not separate kinds |
| `ownership_changed` | keep shared | authorized recovery or reassignment; increments epoch and names authority ref |
| `amendment_escalated` | keep shared | frozen-contract tripwire; Coordinator/owner reader |
| `handoff` | keep shared, conditionally emitted | artifact/role/landing handoff with refs; all editions may use it |
| `dispatch` | keep allowed, profile-conditioned | Full/multi-role assignment; absent when edition has no dispatch step |
| `consolidation` | retain reserved | emit only for an actual task-affecting consolidation boundary; no catalogue fan-out and no Phase-B/C design here |
| `landed` | remove from task-event grammar | completed landing is a Git fact; task journal records `handoff`/`landing_requested` before commit |

Every event keeps required `event_id`, UTC `at`, `kind`, `actor`, `owner_epoch` and at least one canonical reference. `state_delta` is required for `transition` and `ownership_changed`; `related_event` is required for correction/reconciliation and otherwise optional; one bounded `summary` remains optional. Summary and segment ceilings must be finite configuration values, but Extract does not promote 240 code points, 100 events or 32 KiB to defaults.

Corrections append. Identical duplicate IDs are idempotent only when the normalized complete record matches. Divergent duplicates, malformed records and snapshot-ahead state stop. A current-owner/current-epoch journal-ahead event can be completed or compensated. An old-epoch branch is preserved and quarantined.

### E5. Structural journal bounds without unsupported constants

The gathered measurements support a mechanism, not a numeric default:

```text
seal active segment when
    event_count >= configured_event_ceiling
 OR encoded_segment_bytes + next_record_bytes > configured_byte_ceiling
```

Both ceilings must be finite positive values. The exact encoded UTF-8 JSONL bytes, including newline and record overhead, drive the byte check. At rollover, seal the numbered segment, create the next stable segment with predecessor linkage, append the event, then update `journal_head` and `last_event_id`. Sealed segments are retained for done and rejected tasks.

The optional summary ceiling is also configured in Unicode code points and separately checked against the record-byte ceiling. A code-point bound limits human text length; it does not bound storage. Cold start reads the snapshot and referenced last event, while full history remains on demand.

The 240/100/32-KiB inputs remain unresolved because:

- 240 allowed emoji produced a 1,137-byte event while 60 ASCII produced 237 bytes;
- a 16-KiB ceiling fired around 60 mixed events and 32 KiB around 120 under a 200-event ceiling;
- the parser timings are one Windows/Python runtime and do not describe editors, renderers or providers;
- no real journal workload or provider propagation measurement exists.

Challenge should attack the mechanism and the requirement for finite configuration; it should not manufacture a default from these fixture distributions.

### E6. Guarded G-A becomes a pinned local capability profile

The Gather fixture showed that a generic probe can validate a wrong worktree relative to the wrong value supplied by its caller. Guarded G-A therefore needs local expectations that are not derived from the invocation under test.

The local, unsynchronized G-A profile pins:

- canonical expected Git directory;
- canonical expected synchronized worktree root;
- canonical expected index path outside the synchronized root;
- configured landing branch/ref and remote, if used;
- supported Git versions and required capability probes.

Preflight compares the pinned values with independent observations:

1. `git --version` must be in the declared tested set/range, and capability probes must pass. Gather runtime proves the command set on Git 2.42.0.windows.1 only; it does not prove every later version/platform.
2. `git rev-parse --absolute-git-dir` must equal the pinned Git directory.
3. `git rev-parse --show-toplevel` must equal the pinned worktree.
4. `git rev-parse --git-path index` must equal the pinned index and remain outside the synchronized root.
5. the synchronized root must contain no `.git` directory or gitfile.
6. the task/phase allowlist must be literal and exact; staged names must equal it; every declared path must have no working-versus-index drift immediately before commit.

The official [`git-rev-parse`](https://git-scm.com/docs/git-rev-parse) contract says `--absolute-git-dir` canonicalizes the Git path, `--show-toplevel` reports the worktree root and `--git-path index` honors index relocation. These probes establish observations; only comparison with separately pinned expectations establishes that the intended workspace is targeted.

Stable preflight failure categories are therefore unsupported Git/capability, Git-dir mismatch, worktree mismatch, index mismatch/inside-sync, unexpected `.git`, staged allowlist mismatch and task-path drift. Any failure stops before commit; there is no fallback discovery, parent repository or `git init`.

G-B keeps the same staging, drift, scope and provenance gates but has one landing machine and its normal local Git administration. G-A remains optional Full. No new evidence makes per-peer G-C safe under ordinary file sync.

### E7. Four coherent landing protocols

| Protocol | Atomic results + producer attribution | Actual commit SHA in task file | Post-commit task dirt | Crash after Git commit | File-only resume | Git-aware release |
|----------|---------------------------------------|--------------------------------|-----------------------|------------------------|------------------|-------------------|
| L1. Post-commit `landed` event | results commit contains trailers; event follows | yes | immediate | can leave commit without event | eventually, after second write/sync | can use commit before event but semantics lag |
| L2. Commit only | yes, through commit trailers | no task record | none | commit itself survives | cannot distinguish completed landing from task files | reads commit/trailers directly |
| L3. Pre-landing handoff/manifest + one commit | yes; handoff, results and trailers share commit | no future SHA; manifest digest links both sides | none caused by completion | resume finds reachable matching commit | sees `landing_requested`, not completion | verifies reachable commit, trailers, manifest and exact paths |
| L4. Post-commit event in second commit | first commit results, second records SHA | yes | transient until second commit | intermediate state unavoidable | yes after second commit/sync | must reason about two-commit completeness |

L3 is the leading extracted protocol for Challenge because it makes a coherent distinction:

- **Task truth before landing:** a normalized `handoff` record declares `landing_requested`, task/phase, producer, landing owner, artifact refs and the sorted exact path allowlist. Its digest is computable before Git creates a commit.
- **Git truth after landing:** one commit contains that handoff, the status/journal pointer, task results and producer attribution. Structured trailers include task/phase, producer, landing owner and manifest digest.
- **No circular reference:** the task record never predicts a future commit ID. Git's [`commit-tree`](https://git-scm.com/docs/git-commit-tree) contract creates the commit object from the prepared tree, parents, identities and message and only then emits its object ID.

The temporary repository cross-check on local Git 2.42 parsed these trailers:

```text
TFW-Producer: agent-gamma
TFW-Landing-Owner: coordinator-beta
TFW-Manifest: e436f0ce49ca12592a741e0a3abd69ba1221ceaa14226e261dfcb58688f4942d
```

Commit `7958941ff457786de8208bf8d051d6bc9c09df9f` was an ancestor of `main` and changed exactly `tasks/TFW-003/journal.jsonl` plus `tasks/TFW-003/result.txt`. [`git-interpret-trailers`](https://git-scm.com/docs/git-interpret-trailers) defines machine-readable trailer parsing; the local runtime successfully queried the manifest digest from history and parsed it.

#### Resume and release observation rule for L3

1. Load the authoritative status and referenced pre-landing handoff.
2. Recompute the normalized manifest digest and exact declared allowlist.
3. In the configured landing repository/ref, find a reachable commit with matching task/phase and manifest-digest trailers.
4. Parse producer/landing-owner trailers and compare them with the handoff.
5. Verify the commit's changed paths equal the allowlist and remain within one declared task/phase.
6. Report `landed@<commit>` as a **derived Git observation**. Do not write it back to the task journal merely to mirror Git.

Release is Git-aware and stops if no unique reachable matching commit exists. A sync-only resume can report “landing requested; Git completion unknown” but cannot assert completion. The derived catalogue may display a verified Git completion when generated in a Git-capable environment, labelled as derived. If a crash occurs before commit, no match exists and the manifest can be revalidated/retried; if the commit succeeded before the process crashed, the query recovers it without another task write.

L2 remains a simpler alternative but leaves no task-local landing request/manifest to correlate scope. L1/L4 retain an actual SHA in task files at the cost of an extra visibility/write boundary. Challenge must test L3 against duplicate landing attempts, unreachable/rebased commits, changed manifests and release integration before final disposition.

### E8. Lossless compatibility mapping for every observed class

Migration is a resolver and evidence-preservation operation, not a folder-normalization operation. The resolver classifies every task/row; it creates a standard control only when all required core facts have verified sources. Otherwise the task remains visible as `legacy-unresolved` or `malformed` in the migration report/derived index and workflows fail closed for it.

| Observed legacy/nonstandard class | Verified import sources | Control/mapping rule | Unknown or failure result | Path action |
|-----------------------------------|-------------------------|----------------------|---------------------------|-------------|
| Full task with master HL and consistent board/artifacts | folder ID, HL, exact board row, latest authoritative stage trace | populate ID/goal ref and only summaries/lifecycle/owner confirmed by sources | ambiguous board status or absent owner remains unresolved | preserve directory and every artifact path |
| Full task with no master HL but other canonical artifact (TFW-1/2/48/49) | exact existing TS/RF/REVIEW/trace and board text | choose an existing canonical ref only when its role is verified | never synthesize an HL or infer value/outcome from filename | preserve |
| proposal without HL (TFW-54/57/58/59) | proposal file and literal board row | `goal_ref` points to proposal; proposal remains proposal | no HL link or HL content is invented; incomplete core stays unresolved | preserve |
| board-only/planned row or missing target (including TFW-36) | raw row and literal link target | register as board legacy input | do not create a directory/control from a broken or absent target without owner action | no automatic creation/move |
| 8-cell versus 9-cell board rows under an 8-cell header | raw row bytes, detected row generation/width | parse only fields unambiguous for that row shape; preserve provenance | ambiguous shifted cells are reported, never coerced | preserve README history; no rewrite in migration |
| broken HL link or missing anchor (TFW-36/51/52/54 cases) | literal link plus filesystem result | record link defect and use another existing source only if independently verified | never redirect to a guessed similarly named file/anchor | preserve both source and target paths |
| uppercase/lowercase phase forms (`PhaseA`, `phase-a`, etc.) | exact directory names and contained artifacts | compatibility resolver accepts registered historical form case-sensitively | spelling is not lifecycle/stage evidence | never rename |
| modern `research/iterN/` with `iterations.yaml` | control file, stage traces and RES | import iteration facts exactly; RES existence may support research completion only | do not infer overall task completion or next stage without controlling trace | preserve |
| terminal/rejected history | REVIEW, owner ruling or explicit post-mortem outcome | map `terminal` + `done|rejected` only when controlling source states it; retain ref | board `DONE` alone cannot manufacture terminal evidence | preserve all terminal/rejected files |
| Assisted status-folder + TRACE agree | exact parent folder and TRACE status; edition contract | `new→new`, `doing→active`; `review`, `blocked`, `done` require the additional evidence below | disagreement stops; parent and TRACE are evidence, not two authorities after migration | freeze current task directory; no transition move |
| Assisted `review` | parent/TRACE plus explicit awaiting-review gate/ref | map lifecycle `waiting`, profile stage `review`, waiting ref | if “awaiting” is not verified, leave lifecycle unresolved | preserve |
| Assisted `blocked` | parent/TRACE plus blocker kind/ref | map lifecycle `blocked` and `waiting_on` | missing blocker ref remains unresolved | preserve |
| Assisted `done` | parent/TRACE plus completion/review/owner evidence | map terminal `done` with controlling ref | folder name alone is insufficient for terminal ref | preserve |
| Assisted declared status roots with no populated runtime corpus | shipped AGENTS/README/MIGRATION contract | retain as source-contract mapping rules only | do not claim runtime migration success | no filesystem changes |
| empty, README-only, TRACE-only, HL-only, TS/RF-only or research-only task | exact artifacts present | register known ID/artifact refs; create standard control only after core facts verified | explicit missing-field list; never omit from catalogue | preserve |
| non-contract `status.json` | exact bytes and any documented producer | treat as legacy evidence, not authoritative C1-R control | never rename/convert by extension alone | preserve |
| malformed/unsupported `status.yaml` | exact bytes, parser error and sibling artifacts | quarantine from workflows; report all errors | never partially accept or overwrite during scan | preserve malformed original |

Every mapping records provenance outside the status core in the migration evidence/report. This avoids adding migration notes to live authority. “Zero unaccounted tasks” means every source row and task directory has a disposition; it does not mean every malformed or incomplete task is forced into a valid control.

### E9. Shared semantic contract versus edition profiles

| Concern | Shared semantic contract | Full profile | Assisted profile |
|---------|--------------------------|--------------|------------------|
| identity | stable ID, immutable historical references | `TFW-N` resolver | timestamp-handle-slug resolver |
| lifecycle/outcome | five lifecycle values; done/rejected terminal outcomes | workflow stages and release readers | legacy folder/TRACE adapter; no folder moves after migration |
| control ownership | one state owner at one epoch; declared recovery authority | Coordinator normally owns | task steward normally owns |
| journal | shared event meanings, event-first reconciliation, retained segments | dispatch/multi-role handoffs common | simpler owner/handoff subset |
| artifact ownership | canonical role artifacts stay their own authority | HL/RES/TS/ONB/RF/EV/REVIEW profile | TRACE and edition artifacts profile |
| transport | independent files convey no authority/order | collaboration tools or sync | manual/Codex-assisted files/sync |
| Git | landing proof is separate from lifecycle semantics | G-B baseline, guarded G-A optional | no-Git or landing-owner profile permitted |

The editions do not need identical serialization of profile fields or identical Git participation. They do need identical meanings for identity, lifecycle/outcome, next/terminal condition, owner/epoch and journal recovery. No census fact requires a second task model; the difficult cases are compatibility inputs with unknown facts, not alternative semantics.

### E10. Evidence-class preservation and gaps

| Extracted claim | Evidence class supporting it | Claim ceiling |
|-----------------|------------------------------|---------------|
| FA can recover authoritative state in four index conditions | FA + DF | says nothing about NH or direct editing |
| strict schema/recovery rules are deterministic for fixtures | DF | says nothing about PR visibility/reconnect |
| current corpus contains specified legacy and malformed shapes | RR | does not prove a migration implementation |
| Git 2.42 local trailer/reachability/path checks work | RR + official PS | does not certify all supported versions/platforms |
| provider conflicts/offline recovery are real failure classes | vendor PS | does not establish an observed provider branch or adapter recovery |
| zero-command file-browser route exists structurally | UH | not NH |
| shared semantic contract fits current source contracts | RR + PS analysis | Assisted has no populated runtime migration corpus |

Open acceptance gaps remain:

1. NH: a genuinely non-technical participant must browse, interpret and safely change a control, including stale-view handling.
2. PR: a real supported provider/client pair must exercise offline same-file forks, conflict preservation, reconnect and recovery.
3. Git support: declare and test an actual version/platform matrix; current evidence directly covers Windows Git 2.42.0 plus current official contracts.
4. L3 integration: exercise resume/release against absent, duplicate, unreachable/rebased and mismatched-manifest commits.
5. Migration runtime: apply the resolver to a copy/manifest of every Full and populated Assisted class without touching legacy originals.
6. Numerical policy: collect expected journal distributions and editor/provider measurements before selecting default summary/count/byte values.

### E11. Deep-mode Extract loops and hypothesis pressure

| Loop | Cross-reference | Counter-evidence | Extract decision/hypothesis |
|------|-----------------|------------------|-----------------------------|
| 1 — T1 fields/readers | four index states × three task shapes × reader/evidence class × 20 fields | OpenSpec derives state; Spec Kit uses Markdown; five fields have only profile/derived readers | **Decision 1:** nine required shared fields, six conditional, three profile, two derived. **H2 pressure:** strict task-local YAML remains supported for this sync/legacy problem, but NH remains open. |
| 2 — T2/T3 ordering | event/snapshot order × owner epoch × rollover; four landing orders × two Git profiles | post-commit event dirties; future SHA is circular; generic G-A probe accepts wrong self-consistent path; numbers depend on bytes/workload | **Decision 2:** combined configurable rollover; pinned G-A; extract L3 manifest+commit. **H3 pressure:** journal remains supported but `landed` is reclassified and constants stay unresolved. |
| 3 — migration/editions | 51 task dirs × 60 rows × artifact/path variants × Full/Assisted profiles | current board/schema drift and absent Assisted runtime make uniform conversion lossy | **Decision 3:** compatibility resolver may leave a task unresolved; zero-accounting is not forced normalization. **H4 pressure:** shared meanings survive, profile carriers differ. |

Metacognitive check:

- **NEW in Extract:** the smallest coherent status authority is a nine-field universal core with legality supplied by state-dependent conditional fields; iteration 1's 20-field universal reading was unnecessarily broad.
- **NEW in Extract:** a pre-landing handoff digest acts as a correlation key that survives both pre-commit failure and post-commit process loss; the commit SHA remains a derived Git fact.
- **NEW in Extract:** lossless migration requires permission to leave a task explicitly unresolved. Forcing every input into a valid status would itself invent facts.
- **CONFIRMED:** authority/projection separation, owner epochs, event-first recovery, exact staging and stable legacy paths.
- **NOT CLOSED:** NH, PR, L3 release integration, actual version matrix and numerical defaults.

Hypothesis pressure at this gate:

| Hypothesis | Extract status pressure | Why not final yet |
|------------|-------------------------|------------------|
| H1 | hybrid remains coherent and FA-supported | NH and absent-index usability cost remain open |
| H2 | strict reduced YAML survives with a smaller core | direct non-technical use unobserved; Challenge must attack conditional/profile ambiguity |
| H3 | journal/recovery survives; bounds mechanism refined; `landed` revised | PR and L3 integration absent; constants unresolved |
| H4 | shared semantics survive the complete read-only census | populated Assisted migration runtime absent |

## Checkpoint

| Found | Remaining for Challenge |
|-------|-------------------------|
| C1-R2 with nine-field core, conditional/profile/derived dispositions | Attack whether any demoted field is actually required for safe shared cold start/recovery |
| Event grammar with `landed` moved to Git completion | Attack L3 against duplicate/unreachable/rebased commits and file-only readers |
| Combined count + encoded-byte rollover mechanism | Challenge finite configuration and retain numbers as unresolved |
| Pinned guarded G-A and supported-version/capability gate | Verify failure categories and G-B/G-A edition exposure |
| Lossless mapping for every observed/synthetic legacy class | Attack unresolved-task handling and zero-accounting without legacy writes |
| Shared semantics separated from artifact, transport and Git profiles | Seek a concrete legacy case that requires a different meaning, not merely a carrier |
| FA/UH/DF/RR/PS claims bounded | NH and PR remain explicit acceptance gaps |

**Evidence state:** FA, UH, DF, RR and PS remain distinct and present. NH and PR remain absent. No inference in Extract upgrades an evidence class. Current external cross-checks are the official YAML and Git contracts; Git trailer, reachability and exact-file observations were also reproduced locally on 2.42.0.windows.1.

**Recommendation at this gate:** proceed to Challenge. Attack C1-R2, especially the nine-field minimum, L3 landing observation, unresolved migration state and G-A pinned profile. Do not reopen C2–C5 or G-C unless that attack defeats a named survivor invariant.

**Questions for the Coordinator:** none. The accepted synthesis direction is sufficient for Challenge.

**Files written at this gate:** `research/iter2/1_briefing.md`; `research/iter2/2_gather.md`; `research/iter2/3_extract.md`.

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?
- [x] At least one new combination exposed?
- [x] At least two decisions and one hypothesis tested (deep mode)?
- [x] Counter-evidence retained rather than normalized away?
- [x] Metacognitive NEW-versus-confirmed check completed?

Stage complete: YES
→ User decision: WAIT — Coordinator must approve Challenge or redirect the synthesis.
