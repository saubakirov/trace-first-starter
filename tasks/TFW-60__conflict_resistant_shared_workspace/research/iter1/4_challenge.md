# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md)
> Goal: Make concurrent human and agent work in a synchronized TFW workspace conflict-resistant by moving normal lifecycle state and coordination to stable task-local, single-writer surfaces while retaining discoverability and Git provenance.

## Consistency Check

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1 catalogue | generated only and absent between requests | D14 human cold start | zero-command discovery across 100 tasks | A person cannot rank 100 opaque folders without either a persisted view or a hidden generation step. |
| D2 authority | root catalogue carries live truth | D12 isolation | different tasks change disjoint files | Every transition again writes the same root file, reproducing TD-177 and the Phase-A conflict. |
| D3 status | lifecycle-named marker created/deleted per transition | D5 transition | one stable carrier path | A transition necessarily creates one path and removes another; offline sync can expose zero or two markers. |
| D3 status | event-derived only | D14 human cold start | ordinary browsing, no parser | The latest valid event cannot be selected safely after malformed or duplicate records by looking at files. |
| D3 status | Markdown frontmatter plus authored body | D2 authority | one live representation | Either the body duplicates the frontmatter or it is knowingly stale; both are worse than a single strict snapshot. |
| D6 journal | status rewrite and append-only history in one file | D8 retention | sealed immutable segments | The fixed entry file must be rewritten for status and split for growth, so it cannot also be append-only and bounded. |
| D6 journal | JSON objects accepted with duplicate names | D5 deterministic transition | portable validation | RFC 8259 says duplicate object names have unpredictable receiver behaviour; a reader may silently keep different values. |
| D9 ownership | reassignment without a generation/epoch | D12 offline work | old device later reconnects | The old owner cannot distinguish its once-valid authority from the new owner's authority. |
| D10 edition | Assisted lifecycle encoded by moving the task folder | D12 sync | stable references and independent file propagation | The move changes every path and is not an atomic state update across providers. |
| D11 Git | synchronized `.git`, gitfile or index | D12 isolation | independent participant staging | Git administrative locks, indexes and machine-local pointers become shared mutable state. |
| D11 Git | broad staging (`add .`, glob, `commit -a`) | D12 isolation | one-task landing after peer sync | Newly arrived peer changes match the broad scope and can be attributed to the wrong task, as TD-178 demonstrates. |
| D8 retention | delete or summarize sealed history at a size threshold | terminal lifecycle | rejected trace remains inspectable | A bounded active read does not justify erasing the rejection, handoff or amendment trail. |

YAML is not accepted merely because it is familiar. The survivor requires a deliberately small YAML 1.2 subset: unique keys, no aliases, anchors, custom tags or implicit application-specific types, and validation before use. The YAML 1.2.2 specification requires mapping keys to be unique and presents mappings as human-facing key/value pairs ([YAML 1.2.2](https://yaml.org/spec/1.2.2/)). JSONL could also be made strict with a duplicate-aware reader, but ordinary JSON interoperability is not enough: duplicate object names yield unpredictable receiver behaviour ([RFC 8259](https://www.rfc-editor.org/rfc/rfc8259)).

### Configuration dispositions

| Config | Verdict after attack | Decisive failure or surviving constraint |
|--------|----------------------|------------------------------------------|
| **C1 — structured split** | **SURVIVES as C1-R** | A strict task-local snapshot and separate reference-first journal isolate current reads from history. It survives only with a persisted-but-derived catalogue cache, owner epochs, fail-closed validation and explicit two-file reconciliation. |
| **C2 — human split** | **ELIMINATED** | A bounded `STATUS.md` either embeds a YAML-like machine schema and adds no safety over C1, or permits prose/body drift. Its JSONL journal also needs a duplicate-aware technical reader while being less directly inspectable than C1's strict Markdown events. |
| **C3 — structural markers** | **ELIMINATED** | Marker create/delete is a multi-path transition; offline reconnect can produce contradictory markers. One immutable file per event also turns a long task into an unbounded small-file directory. |
| **C4 — event-derived** | **ELIMINATED** | Current state depends on replay and error-selection rules. A missing projection defeats zero-command human use, and a malformed last event makes “current” unknowable without a validator. |
| **C5 — combined bounded document** | **ELIMINATED** | Snapshot rewrites and history appends collide in one file; a conflict copy damages both present state and provenance. Segment rollover destroys the claimed fixed one-file entry. |

The C1-R refinement is bounded, not a blend of carriers: `status.yaml` alone is live state authority; numbered journal segments alone are coordination history; `tasks/INDEX.md` is a persisted disposable projection. No manually maintained Task Board or second status prose is introduced.

### Surviving configurations and invariants

| Survivor | Invariant | Recovery behaviour |
|----------|-----------|-------------------|
| **C1-R — strict snapshot + segmented journal + persisted derived index** | Every task has one fixed `status.yaml`; one current `state_owner` at one valid `owner_epoch` writes it and the active journal segment. A transition appends a valid event before advancing `last_event_id`. The root router and persisted index never override the task file. | Invalid status stops resume/release for that task. Journal-ahead status is completed or compensated by the owner; status-ahead journal is invalid. Divergent copies are preserved, compared by epoch and event chain, and reconciled through a new event. The index is regenerated from valid task controls and may be discarded. |
| **G-A — external local Git directory, guarded** | The synchronized root contains no `.git` directory, gitfile, index or lock. Every Git command uses an absolute local `GIT_DIR` and the exact synchronized `GIT_WORK_TREE`; only the declared landing owner commits/pushes. | A preflight mismatch fails closed before staging. The local repository can be repaired or recloned without changing synchronized task authority. No fallback `git init` or parent-repository discovery is allowed. |
| **G-B — one Git-capable landing owner** | Peers use file sync only; exactly one landing machine holds local Git metadata and stages literal task paths. Task artifacts/journal preserve producing-role identity even though the landing owner is the Git committer. | Loss of the local repository is recovered by recloning/reinitializing from durable Git history and reattaching the synchronized worktree after a clean comparison. Work continues through file sync, but landing pauses until the owner and preflight are restored. |

**Unexpected survivor:** G-A remains viable for Full despite its setup burden because Git exposes enough read-only preflight information to make it fail closed. `git rev-parse --absolute-git-dir`, `--show-toplevel`, and `--git-path index` can verify that the administrative paths are local and that the worktree is exact ([git-rev-parse](https://git-scm.com/docs/git-rev-parse)). It is not the default for a non-technical Assisted workspace; G-B is the smaller profile there.

G-C is eliminated. Local clones plus a separate synchronized exchange directory give excellent Git isolation but introduce two authorities and an import protocol. That is a different collaboration product, not the required ordinary shared-workspace topology.

## Findings

### Loop 1 — discovery, carrier and log corruption

#### Required scenarios 1–4

| Scenario | Attack | C1-R behaviour | Result |
|----------|--------|----------------|--------|
| **1. 100-task cold start** | Fresh agent has no chat; non-technical human runs no command. | README permanently states the fixed control glob and links the persisted derived `tasks/INDEX.md`. The agent validates controls and ranks goal/value/state itself. The human reads the index and clicks the fixed task control. The index contains generation time, schema, source count and digest/revision, and an authority warning. | Survives normally. A purely on-demand catalogue does not. |
| **2. Catalogue absent/stale/malformed** | Cache was deleted, stopped refreshing or cannot parse. | Resume/release ignore it and scan controls. Stale metadata is visible and the selected task is re-read. A malformed cache is quarantined/rebuilt, never partially trusted. A human can still browse ID/slug folders and the fixed control, but ranking 100 tasks is degraded; absence is a visible operational incident assigned to the catalogue owner, not an accepted steady state. | Survives without state corruption; zero-command portfolio usability is degraded until deterministic rebuild. |
| **3. Long task crosses a segment limit** | Task exceeds proposed 100 events/32 KiB. | The owner seals the active numbered segment, creates the next stable numbered path with `previous_segment` and `previous_last_event_id`, appends the next event, then advances `journal_head`/`last_event_id`. Sealed segments remain immutable and retained. Cold start reads the snapshot and referenced last event, not all segments. | Survives; proposed numbers are not validated. |
| **4. Ordering inversion, duplicates, malformed records, conflict copies** | Sync exposes event before snapshot or vice versa; duplicate ID differs; last event is malformed; provider creates a copy. | Journal ahead is a recoverable pending transition. Snapshot pointing to a missing/malformed event is invalid and freezes transitions. A repeated ID is idempotent only if the normalized complete record is identical; otherwise both branches are quarantined. Conflict copies remain until the designated owner appends a reconciliation/correction event. | Survives by stopping, never by “latest timestamp wins.” |

The 100-task test changes H1's strongest form. A standard command is enough for an agent but not for a zero-command human. The defensible architecture is a permanent low-churn router plus a **persisted generated cache**, with task-local status as authority. Persisting a generated file does not make it manually maintained or live-authoritative.

Catalogue metadata cannot solve staleness by itself. A digest/revision tells a reader that the view was built from a particular source set; it does not prove that every peer has already received that set. The only safe selection rule is “open the chosen task control before acting.” Vendor documentation continues to support this conservative floor: Google documents unsynced recovery/Lost & Found behaviour, OneDrive documents conflict and resync handling, and Dropbox explicitly creates conflicted copies for simultaneous or offline edits ([Google Drive troubleshooting](https://support.google.com/drive/answer/2565956?hl=en), [OneDrive sync troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/sharepoint/sync/troubleshoot-sync-issues), [Dropbox conflicted copies](https://help.dropbox.com/organize/conflicted-copy)).

#### Numerical bounds remain hypotheses

The Extract values — 240 Unicode code points per summary and segment rollover at 100 events or 32 KiB — are plausible test fixtures, not architectural evidence. The surviving rules are structural:

1. the project schema declares finite event-summary and active-segment limits;
2. the writer checks the encoded record size before append;
3. rollover creates a new segment and never rewrites or deletes a sealed one;
4. status plus the last referenced event remains the bounded cold-start read;
5. full history remains available on demand, including rejected tasks.

The exact defaults require an implementation fixture with short/long Unicode, 100+ events, rendering and parser timing. Challenge therefore rejects the numbers as final constants while retaining the bounded-segment mechanism.

### Field-by-field challenge

Every surviving control field has a named reader and lifecycle trigger. Optional means “explicitly null/absent by schema,” never “guess from prose.”

| Field | Named reader | Lifecycle trigger or reason | Challenge result |
|-------|--------------|-----------------------------|------------------|
| `schema_version` | validator/migrator | creation and every parse | Keep; unknown versions fail closed. |
| `task_id` | catalogue, links, commit scope gate | creation; immutable | Keep; must agree with directory identity/legacy resolver. |
| `goal_summary` | human/agent catalogue | creation or an approved goal amendment | Keep bounded; discovery wording only, never a second HL. |
| `value_summary` | human/agent prioritization | creation or approved value amendment | Keep bounded for the same reason. |
| `goal_ref` | scope reader | creation/amendment; optional for legacy proposals | Keep as reference; never invent a missing HL. |
| `lifecycle` | resume, release, catalogue | every material state transition | Keep closed: `new`, `active`, `waiting`, `blocked`, `terminal`. |
| `workflow_stage` | workflow router | dispatch/handoff/transition | Keep; edition profile declares supported subset. |
| `status_since` | stale-work display | lifecycle/stage change only | Keep; not the same as file-update time. |
| `waiting_on` | resume and owner | entry to `waiting`/`blocked`, cleared on exit | Keep conditionally required with a bounded kind/ref. |
| `next_action` | cold-start reader | every handoff or transition | Keep as one imperative, not a plan. |
| `next_ref` | cold-start reader | same as `next_action` | Keep; prevents copied gate/artifact detail. |
| `terminal_outcome` | release/catalogue | entry to terminal | Keep closed to `done` or `rejected`; null otherwise. |
| `terminal_ref` | release/auditor/human | entry to terminal | Keep required for terminal; points to controlling verdict/ruling. |
| `state_owner` | write guard and handoff | creation or ownership recovery | Keep; identity alone is insufficient offline. |
| **`owner_epoch`** | write guard/reconciler | creation at 1; increment on every ownership change | **Add.** Stale offline writes from an earlier owner become mechanically detectable. |
| `ownership_profile` | role/file validator | creation or versioned migration | Keep as a profile ID; do not copy the whole map into each task. |
| `roles` | dispatcher and artifact ownership check | assignment/handoff | Keep; Assisted may carry only owner/assigned role, Full carries its role set. |
| `last_event_id` | reconciliation and resume | every accepted journal event reflected by snapshot | Keep; snapshot/file timestamp is not an ordering protocol. |
| `journal_head` | bounded history reader | segment rollover | Keep; path must be task-relative and monotonic. |
| `updated_at` | catalogue freshness display | every valid snapshot rewrite | Keep explicit because sync may not preserve useful filesystem times. |

The schema should allow only the narrow mappings/sequences needed for `waiting_on` and `roles`; all frequently changed values remain obvious scalars. Static comments may explain enums, but comments are non-authoritative. A non-technical state owner changes a named scalar and runs/receives validation through the supported adapter; a non-owner does not edit the control merely because it is readable.

### Event-by-event challenge

The original nine event kinds were too broad. Separate `blocked` and `resumed` kinds duplicate lifecycle transitions, while `consolidation` would make a catalogue rebuild write every task journal — the same fan-in in reverse. Coordinator disappearance requires a fact the original grammar lacked.

| Extract event | Named reader | Lifecycle trigger | Challenge disposition |
|---------------|--------------|-------------------|-----------------------|
| `created` | validator, first cold-start audit | task control becomes authoritative | **Keep.** Establishes epoch 1 and initial state. |
| `dispatch` | assigned role, coordinator resume | bounded work is assigned | **Keep.** Reference target scope/artifact; no prompt transcript. |
| `handoff` | coordinator/next role | role returns, pauses or transfers work | **Keep.** Reference produced artifact/gate and one outcome word. |
| `transition` | resume, catalogue generator, release | lifecycle/stage changes, including block and unblock | **Keep.** Carries `from`, `to`, reason kind and controlling ref. |
| `blocked` | resume | entry to blocked | **Eliminate as separate kind.** Use `transition` to `blocked` with cause/ref. |
| `resumed` | resume | exit from waiting/blocked | **Eliminate as separate kind.** Use `transition` related to the prior transition. |
| `amendment_escalated` | Coordinator and HL amendment workflow | frozen change proposed/decided | **Keep.** Reference proposal/amendment; never copy its body. |
| `landed` | release/auditor/provenance reader | declared task paths committed | **Keep with caution.** Reference commit and producing roles; it may be journal-ahead until the next task-state landing and is not proof of release by itself. |
| `consolidation` | catalogue/debt/knowledge workflow | project view rebuilt | **Eliminate from task journal in Phase A.** Catalogue metadata owns its own build trace; debt/knowledge are out of scope. |
| **`ownership_changed`** | write guard and recovery reader | coordinator/state owner changes or is recovered | **Add.** Requires old/new owner, incremented epoch and recovery-authority reference. |

The surviving closed grammar is therefore `created`, `dispatch`, `handoff`, `transition`, `ownership_changed`, `amendment_escalated`, and `landed`. Every record contains `event_id`, `at`, `kind`, `actor`, `owner_epoch`, applicable state delta, at least one reference, optional related event, and an optional bounded one-line summary. A correction is a new referenced event; sealed history is never edited.

### Loop 2 — ownership, terminal state and migration

#### Required scenarios 5–8

| Scenario | Failure mode | Surviving invariant and recovery |
|----------|--------------|----------------------------------|
| **5. Two owners act offline and reconnect** | Both snapshots may have plausible timestamps and the provider may keep both. | Only the branch with a valid `ownership_changed` chain to the highest authorized `owner_epoch` can become current. Old-epoch events are preserved as rejected/quarantined attempts, not replayed. If both wrote the same epoch, stop; the declared recovery authority reviews both artifact refs and appends a new-epoch reconciliation event. Timestamp never decides authority. |
| **6. Parallel role artifacts; coordinator disappears** | Researcher/executor/reviewer can finish disjoint files, but nobody may safely advance control. | Role writers continue only in their profile-owned artifacts and leave handoff refs. A versioned ownership profile names the recovery authority. That authority records the ruling, increments `owner_epoch`, writes `ownership_changed`, then resumes normal transitions. The absent coordinator's old offline writes fail the epoch check. |
| **7. Done and rejected terminal tasks** | Rejected work may vanish; a stale catalogue may show done; reopening can rewrite history. | `terminal_outcome` and `terminal_ref` are mandatory and retained for both outcomes. Release reads task controls, not the catalogue: `done` is eligible subject to normal gates; `rejected` is visible but not releasable. A terminal task is not silently reopened; changed intent creates a successor task or explicit frozen-contract amendment with a new trace. |
| **8a. Assisted folder-move migration** | Moving legacy task directories breaks references and may fork during sync. | Do not normalize paths by moving them. Freeze each existing legacy directory at its current location, add the control there, and let the compatibility resolver scan declared legacy roots. New tasks use the neutral stable root. Parent folder names cease to be status authority. |
| **8b. Full Task Board migration** | Malformed rows, proposals without HL, and nonstandard tasks cannot be losslessly coerced. | Create task-local controls from only verified row/artifact facts; use existing proposal or other canonical file as `goal_ref`; leave optional unknowns explicit. Preserve Task Board history as migration input/cache, never rewrite history to look uniform. Validation reports unindexed/malformed legacy tasks instead of omitting them. |

No distributed file lock is claimed. One-writer ownership reduces expected collision frequency; `owner_epoch`, closed event chains and stop/reconcile rules make accidental violations detectable and recoverable. They do not make two same-file offline edits atomic.

The shared Assisted/Full kernel survives. Both editions need the same task identity, lifecycle/outcome, next action/reference, state ownership/epoch and event meanings. Representation may differ only where a deterministic adapter preserves those meanings; transport and Git profile may differ. Edition-specific artifact sets, ID generation, stage subsets and recovery authorities remain profiles, not separate task models.

### Loop 3 — Git setup, scope and provenance

#### Required scenarios 9–10

| Scenario | Attack | G-A | G-B |
|----------|--------|-----|-----|
| **9. Explicit staging after synced peer changes** | Peer changes arrive between status inspection, staging and commit. | Landing owner syncs/reconciles first, stages only literal declared task paths, compares the cached-name set to an exact allowlist, and verifies no allowed path changed again after staging. Out-of-scope peer changes remain unstaged. | Same landing gate; peers never share the index, so their other task files remain working-tree changes only. |
| **10. `.git`/`GIT_DIR` failure and one-owner provenance** | Environment is unset, external directory missing, a `.git` pointer appears, or one committer hides producing roles. | Wrapper verifies absolute Git dir, exact worktree and local index before every mutating command; any mismatch stops. No automatic init. Commit subject/trailers plus task journal/artifact ownership identify producer, task, phase and landing owner. | Only the landing machine is Git-capable. Loss/mismatch stops landing and is repaired from durable history; producer attribution comes from task artifacts/journal and declared commit trailers, not fabricated Git authorship. |

Official Git behaviour supports the gate but does not supply it automatically:

- `--git-dir`/`GIT_DIR` disables ordinary repository discovery and requires the correct worktree to be specified ([Git manual](https://git-scm.com/docs/git)).
- A linked worktree stores a `.git` file in the worktree pointing into repository administration, and worktree-local versus shared paths differ ([git-worktree](https://git-scm.com/docs/git-worktree.html)). That machine-specific pointer must not synchronize.
- `git add` stages the named file contents at the time it runs; a directory path updates the directory as a whole, and globs expand scope ([git-add](https://git-scm.com/docs/git-add)). Therefore explicit files plus a staged-name allowlist are mandatory, not stylistic advice.

A defensible landing sequence is:

1. verify sync health and the declared landing owner;
2. verify absolute `GIT_DIR`, worktree and index are local/correct, and that no `.git` entry exists in the synchronized root;
3. reconcile the landing branch with durable Git history before staging;
4. stage exact task files with literal pathspec handling and `--` separation;
5. compare `git diff --cached --name-only` to the task/phase allowlist and fail on any extra or missing path;
6. verify staged task files did not change again in the working tree; re-stage or stop if they did;
7. commit one task/phase/role scope with task/role/landing attribution; land catalogue generation separately;
8. append/reference the `landed` event according to the journal protocol without pretending the event is contained in the commit it names.

G-A and G-B solve different usability levels without changing task semantics. G-A gives technical Full participants local inspection/diff capability; G-B gives file-sync-first Assisted participants the smallest Git surface. Both retain one landing owner and the same explicit-path scope gate. A local index removes TD-144's shared-index ambiguity; only the allowlist removes TD-178's own-task attribution failure.

### Deep-mode OODA record

| Loop | Observe/orient | Attack/adapt | Counter-evidence retained |
|------|----------------|--------------|---------------------------|
| 1. Discovery and corruption | Crossed 100-task cold start with missing/malformed views and log ordering | Eliminated C3/C4/C5; reduced C2; strengthened C1 with persisted derived cache and fail-closed chains | Without a cache, human portfolio discovery degrades; two files are never atomic; numeric limits remain unproven. |
| 2. Ownership and lifecycle | Replayed offline dual owners, coordinator loss, terminal rejection and both edition migrations | Added owner epoch/recovery event; eliminated move-based migration and per-task consolidation events | Ownership rules cannot prevent disconnected violations; legacy roots remain nonuniform; recovery needs a predeclared authority. |
| 3. Git landing | Replayed peer sync between stage/commit and broken external Git setup | Eliminated G-C; retained guarded G-A and simpler G-B with one landing owner and exact allowlists | Local indexes do not prevent broad staging; one committer does not itself preserve producer identity; wrappers need implementation evidence. |

### Amendment implications versus free refinements

No frozen-HL amendment is required by the surviving design:

- H1's strongest on-demand-only form fails, but frozen §3.1 and Phase-A deliverable 3 already permit a low-churn **or rebuildable** non-authoritative catalogue. A persisted derived cache is inside that contract.
- Separate `status.yaml` and journal files remain one task-local control substrate under Phase-A deliverable 2; §10 explicitly left journal separation and carrier format open.
- Freezing existing Assisted legacy paths instead of moving them implements the frozen stable-path/lossless-migration requirements.
- Shared semantic state plus edition-specific transport/Git profiles implements, rather than changes, the frozen concurrency shape.

Free refinements for RES/TS are: add `owner_epoch`; replace `blocked`/`resumed` with typed transitions; add `ownership_changed`; remove per-task `consolidation`; define the persisted cache metadata and degraded state; define strict YAML/event validators; parameterize and test numerical bounds; specify migration resolvers; and make Git preflight/allowlist checks executable. If later design insists that “one carrier” means one physical file containing both mutable snapshot and append-only history, that interpretation conflicts with Challenge evidence and should be escalated before TS rather than silently implemented.

### Remaining gaps and research sufficiency

The remaining uncertainties are empirical acceptance work, not missing architecture alternatives:

1. choose numeric summary/segment defaults with a reproducible long-task fixture;
2. test the generated 100-task index and scalar YAML with a genuinely non-technical reader;
3. run reconnect/conflict-copy scenarios in at least one actual synchronized environment and record provider/version;
4. implement duplicate-key, owner-epoch and journal-chain validators and run malformed fixtures;
5. verify migration against every current malformed/legacy/nonstandard task, including TFW-54-style proposals;
6. exercise both guarded G-A failure and G-B landing after peer sync.

Those items belong in Phase-A TS/evidence. Primary vendor and Git contracts already establish that no candidate can rely on cross-file atomicity, distributed locks, synchronized Git administration or implicit staging scope. The iteration can proceed to RES synthesis without widening into debt or knowledge architecture.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1-R is the sole surviving task-control configuration; C2-C5 are eliminated with named failure modes. | RES must turn the Challenge implications into explicit H1-H4 verdicts and recommendations. |
| G-A and G-B survive as edition/topology profiles; G-C is eliminated. | Numerical defaults remain implementation hypotheses, not frozen constants. |
| All ten required scenarios have invariant and recovery behaviour. | Real human/provider/fixture evidence is required in Phase-A implementation acceptance. |
| Every proposed field and event has a named reader/trigger; redundant events were removed and owner recovery added. | Exact file grammar/schema and migration algorithm belong in TS. |
| Frozen sections need no amendment on present evidence; free refinements are enumerated. | Coordinator approval is required before writing RES. |

**Eliminations at this gate:** C2 bounded Markdown/JSONL split; C3 structural markers; C4 event-derived authority; C5 combined status/journal; G-C local-clone exchange.

**Survivors at this gate:** C1-R strict snapshot + segmented journal + persisted derived index; guarded G-A for Git-capable Full use; G-B for one-landing-owner/file-sync-first use.

**Recommendation at this gate:** approve RES synthesis. Challenge found no unresolved architecture branch that requires another Gather/Extract pass.

**Questions for the Coordinator:** none.

**Files written at this gate:** `research/iter1/4_challenge.md` only (plus previously accepted `1_briefing.md`, `2_gather.md`, and `3_extract.md`). `RES.md` has not been written.

**Evidence state:** current primary YAML/JSON/Git specifications and vendor sync documentation were used. External service/database systems remain counterexamples only. Human usability, provider reconnect behaviour in a real shared folder, migration fixtures and numeric limits remain explicitly unverified implementation evidence.

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?
- [x] Three Challenge loops completed and counter-evidence retained (deep mode)?
- [x] Every required adversarial scenario attacked with invariant/recovery behaviour?

Stage complete: YES
→ User decision: WAIT — Coordinator must approve RES synthesis or redirect a Challenge gap.
