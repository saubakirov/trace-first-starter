# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md)
> Goal: Make concurrent human and agent work in a synchronized TFW workspace conflict-resistant by moving normal lifecycle state and coordination to stable task-local, single-writer surfaces while retaining discoverability and Git provenance.

## Consistency Check

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|-------------|-------------|-------------|-------------|------------------|
| D2. Derived-index condition | absent, stale or malformed | D4. Reader behaviour | trust index | a missing/contradictory/discontinuous projection cannot establish task authority |
| D3. Task-control shape | recognized legacy or malformed control | D4. Reader behaviour | best-effort act from inferred artifacts | lossless migration forbids guessed lifecycle, owner, value or terminal facts |
| D5. Usability evidence | FA, UH or UI instrumentation | D5. Usability evidence | claim NH | one evidence class cannot be relabelled as a participant observation |
| D7. YAML acceptance | full YAML extensions | D3. Task-control shape | closed strict control | anchors, aliases, tags, directives and merge features add meanings outside the validator-owned subset |
| D8. Recovery authority | timestamp/latest writer | D9. Journal/snapshot visibility | divergent branch | time does not prove authority or a valid event chain after offline reconnect |
| D9. Journal/snapshot visibility | snapshot ahead | D4. Reader behaviour | act | snapshot claims history that is absent or malformed, so transition/release must stop |
| D10. Journal segmentation | count-only or manual | H3 bounded retained journal | byte-bounded cold start/storage | count does not bound multi-byte records; manual boundaries are not a deterministic finite policy |
| D11. Landing trace order | pure commit-only | frozen DoD-3 handoff trace | no pre-landing handoff | a material role-to-landing handoff disappears from the task-local coordinator record |
| D11. Landing trace order | post-commit event | one atomic task landing | no second task write | the actual SHA exists only after the result commit, so mirroring it requires a later write/commit |
| D12. Git profile | guarded G-A | D13. Git scope gate | caller-derived/unpinned paths | a wrong worktree can be self-consistent relative to the wrong invocation |
| D12. Git profile | G-C per-peer Git exchange | frozen ordinary-file sync floor | no second exchange authority | importing peer Git states creates an authority/transport not required by C1-R2 |
| D13. Git scope gate | whole index/worktree | frozen one-task provenance | exact task/phase commit | unrelated staged or working paths cannot be distinguished reliably |
| D14. Migration action | move/normalize legacy folders | frozen stable paths | preserve historical references | a move changes active/history-bearing paths and introduces sync rename risk |
| D14. Migration action | exclude malformed/nonstandard input | frozen lossless migration | account for every row/directory | omission is silent deletion from project discovery even when bytes remain |
| D15. Edition boundary | separate task meanings | observed shared lifecycle/owner/event needs | carrier/profile divergence only | no observed legacy fact requires `active`, `blocked`, ownership epoch or event order to mean something different by edition |

### Surviving configurations

| Survivor | Extract configurations retained | Revised invariant | Recovery behaviour |
|----------|---------------------------------|-------------------|--------------------|
| **C1-R2 control/catalogue family** | T1-B, T1-C, T1-D, T1-E | nine-field strict shared core; state-dependent conditional fields; closed profile fields; derived timestamps outside authority; router + persisted disposable index | valid controls act; absent/stale/malformed view scans/rebuilds; legacy/malformed controls remain visible and non-actionable |
| **C1-R2 compatibility view** | T1-F | every input is accounted; a standard control exists only when core facts have verified sources | `legacy-unresolved`/`malformed` stops workflows for that task without moving or rewriting it |
| **C1-R2 journal/recovery** | T2-A, T2-B, T2-C, T2-D | event-first/snapshot-second; one owner/epoch; identical duplicate only; finite combined count+encoded-byte segmentation | journal ahead may be completed/compensated; snapshot ahead/divergence/malformed stop; authorized recovery increments epoch; old branch quarantined |
| **L3 + G-B baseline** | T3-C | pre-landing handoff manifest plus exact literal allowlist; one landing owner; one result commit; reachable unique matching commit is derived completion | no commit = retryable not-landed; one valid match = landed; zero/invalid/duplicate matches stop or remain not-landed without task write |
| **L3 + guarded G-A optional Full** | T3-E | G-B gates plus separately pinned canonical Git-dir/worktree/index, branch/ref, remote and tested capability/version profile | any pin/capability/scope mismatch stops before commit; local profile repair does not change task authority |
| **Sync-only peer under G-B** | narrowed T3-G | a non-Git participant can resume the last durable task state but cannot assert Git completion or release | reports `landing_requested; Git completion unknown`; Git-aware landing owner/release performs L3 verification |

### Eliminated configurations

| Extract configuration | Disposition | Failure |
|-----------------------|-------------|---------|
| T1-A — all 20 fields universally required | eliminate as unnecessary authority surface | five fields have only conditional/profile/derived readers; mandatory presence adds churn without a shared invariant |
| T1-G — on-demand-only view | remains eliminated | FA can scan, but frozen zero-command human portfolio discoverability remains unsupported during absence |
| T1-H / T2-F — service/database authority | remains out/eliminated for Phase A | stronger transactions are real but violate frozen ordinary-file/no-service boundary |
| T2-E — timestamp/latest writer | eliminate | cannot resolve authorized epoch or same-ID divergent payload |
| T2-G — manual/time-only segmentation | eliminate | no deterministic finite count/byte bound and no reproducible rollover |
| T3-A — post-commit task `landed` event | eliminate | immediate task dirt and commit-without-event crash window; no frozen outcome requires the mirrored SHA |
| T3-B — pure commit-only | eliminate in favor of L3 | producer trailers can survive, but no task-local handoff/manifest correlates declared result scope with the commit |
| T3-D — second landing commit | eliminate as dominated | preserves SHA in files only by adding an intermediate incomplete state and second crash/landing boundary |
| T3-F — G-C + path normalization + separate models | remains eliminated | compounds exchange authority, path breakage and semantic drift; no survivor invariant was defeated |

### Unexpected survivors

- **Explicit unresolved migration state:** lossless accounting does not require forcing every input into a valid `status.yaml`. Visibility plus a fail-closed action gate is safer than a syntactically complete record containing guessed facts.
- **Manifest identity across rebase:** L3 can recompute completion after a commit SHA changes, provided exactly one reachable commit still matches the manifest, attribution and paths. The manifest—not a remembered SHA—is the correlation key.
- **Non-Git resume:** filesystem-only readers can determine the last durable task state (`landing_requested`) without asserting a Git fact they cannot observe. This preserves frozen filesystem resume while release stays Git-aware.

## Findings

### C1. Reproducible Challenge fixture and evidence boundary

The canonical final challenge fixture is outside tracked project paths:

```text
E:\TEMP\tfw60_iter2_e48d40f17410468387a67a8ca02120cc\challenge_run2
```

The first run completed but exposed one missing explicit conditional case: absence of optional `goal_ref`. The final run added that attack and supersedes run 1.

```powershell
$env:TFW60_CHALLENGE_RUN='challenge_run2'
python "E:\TEMP\tfw60_iter2_e48d40f17410468387a67a8ca02120cc\challenge.py"
```

Final command exit: 0; elapsed: 19.219 seconds.

| Artifact | SHA-256 |
|----------|---------|
| `challenge.py` | `6AA1F9366B5F21202FD8AD36C8312F6B5FE23E6272FF89F3F55392FABE4562F4` |
| `challenge_run2/challenge_results.json` | `76B818F3DBDECA3326D6BF569DC92FB29DC6610F620ADDE909719E4E97E44C83` |

The suite created only temporary YAML, journal and Git repositories. The live repository census was read-only. The result explicitly records NH and PR as `NOT OBSERVED`; no local result is presented as provider behaviour.

### C2. Nine shared-core fields survive individual removal

Each mutation removed exactly one shared field from an otherwise valid active control. All nine failed the strict validator and the first consumer/recovery invariant is independently identifiable:

| Removed field | First named reader | First invariant lost |
|---------------|--------------------|----------------------|
| `schema_version` | validator/migrator | cannot choose a closed grammar or distinguish an old/partial control |
| `task_id` | catalogue/Git scope gate | cannot correlate control, folder, landing manifest and commit identity |
| `goal_summary` | portfolio reader | cannot answer the frozen project-level goal discovery question |
| `value_summary` | portfolio prioritizer | cannot answer the frozen project-level value discovery question |
| `lifecycle` | resume/release | cannot choose legal conditionals, transition or terminal treatment |
| `state_owner` | write guard | cannot identify the sole normal control/journal writer |
| `owner_epoch` | reconciler | cannot reject a stale former-owner branch after authorized recovery |
| `last_event_id` | snapshot/journal reconciler | cannot prove which event the snapshot reflects or detect snapshot-ahead state |
| `journal_head` | bounded history loader | current event-ID grammar cannot locate the reflected event without scanning unbounded segments |

`journal_head` could be folded into a future structured event locator, but that would preserve the same semantic information rather than demote it. Under the extracted monotonic event-ID grammar it remains required.

No tenth field passed the universal admission test. `goal_ref` may be absent when no source is verified because bounded goal/value summaries still support selection; the test accepted that shape and produced one unambiguous non-terminal cold-start branch.

### C3. Conditional/profile legality yields one cold-start branch

Valid `new`, `active`, `waiting`, `blocked`, terminal-done and terminal-rejected cases were accepted. Full and Assisted profile examples were accepted, and a no-`goal_ref` legacy-compatible case was accepted. Each returned exactly one of:

- non-terminal: `next_action` + `next_ref`, plus `waiting_on` only for waiting/blocked; or
- terminal: `terminal_outcome` + `terminal_ref`, with no next/waiting fields.

The validator rejected every ambiguous or illegal combination tested:

| Attack | Result |
|--------|--------|
| non-terminal missing next action/ref | reject |
| waiting without `waiting_on` | reject |
| terminal without outcome/ref | reject |
| terminal carrying next fields | reject |
| non-terminal carrying terminal fields | reject |
| `roles` without a known ownership profile | reject |
| unknown profile version | reject |

Profile fields therefore cannot silently alter shared lifecycle legality. A profile can refine `workflow_stage` and role/file assignment, but it cannot define a new lifecycle meaning or make an otherwise ambiguous snapshot actionable.

### C4. Strict-YAML application profile fails closed

One valid reduced YAML control was accepted. Every adversarial input was rejected before workflow action:

| Attack class | Cases | Result |
|--------------|-------|--------|
| duplicate/extension semantics | duplicate key, anchor+alias, custom tag, YAML directive, merge key | reject |
| schema drift | unknown field, removed derived field, unknown version | reject |
| malformed reference | absolute Windows path, parent escape, external URL, nonconforming journal path | reject |
| partial visibility/content | empty file, valid YAML with only two fields, truncated quoted scalar | reject |

The [YAML 1.2.2 specification](https://yaml.org/spec/1.2.2/) requires unique mapping keys but deliberately supports anchors, aliases and tags. Rejecting those valid language features is therefore an explicit application-profile boundary, not a claim that the files are “safe because YAML.”

A syntactically valid snapshot whose related files were not yet visible also stopped:

| Visibility case | Result |
|-----------------|--------|
| control, goal, next ref, journal and last event visible | ready |
| journal segment missing | stop partial visibility |
| last event absent from visible journal | stop partial visibility |
| next ref missing | stop partial visibility |

Partial sync is not repaired by accepting a subset. The reader changes no state, preserves visible bytes and retries/reconciles after the missing dependency appears.

### C5. Recovery and rollover invariants survive without numeric defaults

The Gather recovery matrix and Challenge parser attacks jointly preserve these outcomes:

| Condition | Required result |
|-----------|-----------------|
| aligned snapshot/event | accept |
| current-owner/current-epoch journal ahead | recoverable completion or compensation |
| snapshot ahead/missing last event | stop |
| identical duplicate event | idempotent accept |
| divergent duplicate ID | stop/quarantine |
| malformed event/reference | stop |
| authorized ownership recovery | increment epoch, append `ownership_changed`, then resume |
| old epoch reconnect | retain/quarantine; never replay as current |
| same-epoch divergent branch | recovery-authority ruling required; timestamp cannot choose |

The Challenge rollover fixture exercised exact count, exact encoded-byte, multi-byte Unicode and combined first-hit cases. It preserved all event IDs in order. Invalid missing/zero/negative/string limits stopped at configuration validation; an event larger than the byte ceiling and a summary larger than its code-point ceiling stopped instead of creating an infinite empty-segment loop.

The survivor invariant is:

```text
configured_event_ceiling > 0
configured_encoded_byte_ceiling > 0
configured_summary_codepoint_ceiling > 0
roll over before the first next record that would exceed either segment ceiling
reject a single record that cannot fit
```

No numeric default is selected. The mechanism survives; 240 code points, 100 events and 32 KiB remain unsupported candidate inputs.

### C6. L3 survives only with a unique reachable exact match

The normalized pre-landing manifest bound task, phase, handoff event, producer, landing owner, sorted exact paths and content hashes for result/status artifacts. The journal record carried the manifest digest; commit trailers carried the same correlation and attribution.

| Attack | Observed result | Required protocol rule |
|--------|-----------------|------------------------|
| no commit / crash before commit | `NOT_LANDED` | same manifest may be revalidated and retried |
| one valid commit / crash after commit | `LANDED`; evaluator left all task file hashes unchanged | recompute from Git; never mirror completion into status/journal |
| current manifest changed after commit | `NOT_LANDED` | old commit does not satisfy new intent |
| two reachable commits both exactly match | `STOP_AMBIGUOUS_DUPLICATE` | recovery authority/landing owner must select or supersede; never pick newest |
| extra unrelated path | `STOP_INVALID_MATCH` | commit paths must equal allowlist |
| missing declared result | `STOP_INVALID_MATCH` plus artifact-hash mismatch | every declared artifact must be present and bound |
| wrong producer trailer | `STOP_INVALID_MATCH` | producer must equal manifest |
| wrong landing-owner trailer | `STOP_INVALID_MATCH` | landing owner must equal manifest/profile |
| matching commit unreachable from pinned ref | `NOT_LANDED` | unreachable history cannot satisfy release |
| commit rebased to a new SHA with same exact manifest/tree delta | `LANDED` at new reachable SHA | manifest identity survives SHA replacement |
| commit on `landing`, pinned ref still `main` | main `NOT_LANDED`; explicit landing ref `LANDED` | branch/ref changes require explicit local-profile change, not broad `--all` search |
| non-Git resume | `LANDING_REQUESTED_GIT_COMPLETION_UNKNOWN` | report last durable task state only |
| Git-aware release on unique exact match | accept | release records derived `landed@<sha>` in its output/evidence, not task authority |

The valid run created `1227a2cf1d6e629443578954a16538748afa19bf`; pre/post evaluator hashes of journal, result and status were identical. The rebase attack replaced `a69d22c8fb84f1cef6c587faef0c279aa502aa58` with reachable `78a10b6713b8df367051f28d6799b578b17a3e30` and still recomputed completion. The duplicate attack found two exact valid candidates and stopped.

Git's current [`git-log`](https://git-scm.com/docs/git-log) contract defines history as commits reachable from the chosen revision set; [`git-merge-base --is-ancestor`](https://git-scm.com/docs/git-merge-base) supplies an explicit reachability check. Searching `--all` would make abandoned/rebased branches falsely eligible, so release is pinned to one configured landing ref.

### C7. Removing task-journal `landed` is a free refinement, not an amendment

Frozen contract cross-check:

- §4 Phase-A deliverable 2 fixes one task-local carrier for lifecycle, discovery metadata, role/file ownership and an append-only coordinator journal, while leaving exact name/format to research.
- DoD-3 requires journal events for dispatch, handoff, state change, blockage, amendment escalation and consolidation. It does **not** require a `landed` event.
- §3.2 and DoD-9 assign commit/release provenance to Git.
- DoD-11 requires filesystem inspection to identify the last durable task state. L3 preserves `landing_requested` in ordinary task files; Git completion is a separate release/provenance fact.

L3 retains the material pre-landing handoff and producing-role identity, so it does not narrow a frozen journal outcome. Derived completion can be recomputed without modifying the journal/status. Removing the post-commit `landed` kind is therefore a free mechanism refinement for RES/TS, not a §12 amendment.

If a later design removed the pre-landing handoff as well and relied only on an uncorrelated commit, it would need reclassification against frozen DoD-3 and Principles 6–7. That is not the survivor.

### C8. Guarded G-A survives only as a pinned local capability profile

The Challenge created a fresh external Git directory, synchronized worktree and relocated local index. Results:

| Attack | Result |
|--------|--------|
| correct pins/probes | pass |
| `..` aliases canonicalizing to same paths | pass |
| case aliases on this Windows filesystem | pass after platform canonicalization |
| differently relocated index, separately pinned outside sync | pass |
| index inside synchronized root | stop |
| unexpected `.git`/gitfile | stop |
| unsupported Git version | stop |
| missing required capability | stop |
| wrong branch/ref | stop |
| wrong remote | stop |
| missing pin key or malformed pin JSON | stop |
| corrupt/wrong pinned path | stop |

Canonicalization is platform-aware: case folding is valid on this Windows evidence environment and must not be applied on a case-sensitive filesystem. Symlink/junction resolution must use the platform's canonical path API; string lowercasing alone is not a portable gate.

The local profile must be parsed strictly and kept outside sync. It pins Git directory, worktree, index, landing ref/branch, remote and tested version/capability set. A corrupt profile stops; the tool never learns its expected workspace from the same invocation it is checking.

G-A's operational value is narrow: it keeps all administration/index bytes outside a synchronized working root when that topology is necessary. It adds three path pins plus branch/remote/version/capability failure modes. G-B therefore remains the baseline when one landing machine can keep or exclude its normal local Git administration; G-A remains optional Full, not a default promoted by technical novelty.

### C9. Exact-once migration accounting survives without path moves or semantic split

The current repository census produced:

| Measure | Result |
|---------|--------|
| board rows | 60 |
| task directories | 51 |
| source occurrences | 111 |
| logical task IDs | 60 |
| matched board+directory tasks | 51 |
| board-only tasks | TFW-16, 20, 28, 33, 34, 35, 36, 37, 39 |
| directory-only tasks | none |
| duplicate board IDs or task directories | none |
| row widths | 39 eight-cell; 21 nine-cell |
| current standard `status.yaml` controls | 0 |
| proposal without HL | TFW-54, 57, 58, 59 |

All 111 source occurrences were assigned exactly once to one of 60 logical task records. No identity collision requires a directory move. Board-only tasks remain board legacy inputs; migration does not create or move a folder without owner action. Phase spelling variants remain registered paths rather than normalization candidates.

Because no current task has the new standard control, the read-only planner marks all current entries non-actionable until verified facts are migrated; this is a safety result, not a claim that Phase A has already converted them. The synthetic 100-task corpus also accounted exactly once for 80 actionable valid, 10 non-actionable legacy and 10 non-actionable malformed controls.

Visibility and action are separate:

- every row/directory appears in the resolver report/index with raw source provenance;
- only a fully valid standard control is actionable;
- unresolved/malformed entries return stable diagnostic reasons;
- migration never overwrites malformed bytes, rewrites board history or invents HL/value/terminal evidence.

No observed Full class requires a move or different lifecycle meaning. The Assisted source contract also maps without moving, but no populated Assisted task corpus was available. That absence remains acceptance evidence; it is not grounds to invent a separate task model.

### C10. NH and PR do not block research synthesis; they block unverified Phase-A acceptance

Evidence classes remain unchanged:

- **NH:** not observed. FA proves context-free AI discovery; UH establishes a plausible file-browser route; neither verifies a non-technical participant can interpret/edit safely.
- **PR:** not observed. Vendor PS establishes failure classes; DF verifies deterministic local recovery rules; neither reproduces provider reconnect/conflict-copy behaviour.

Research sufficiency asks whether the architecture, alternatives, failure rules and acceptance obligations are determinate. They are. Another paper/fixture iteration cannot manufacture NH or PR, so their absence does not require iteration 3 or block RES synthesis.

They are mandatory Phase-A acceptance evidence:

- PR is explicit in frozen §7.1: file-sync claims require at least one real synchronized-folder observation plus deterministic fixtures. DoD-14 also requires offline edit/reconnect and Git attribution after synchronization. Without PR, Phase A cannot pass RF/REVIEW.
- NH is needed to verify frozen DoD-5 and avoid DoF-7's practical human-undiscoverability failure. The HL does not name a specific participant protocol in §7.1, so requiring an observed non-technical reader is a research-derived TS AC, not a frozen-HL amendment. Without it, H2's human clause and the product outcome remain unproven.

Additional TS acceptance evidence remains: L3 resume/release integration; Git version/platform matrix; full migration against a copy/manifest including populated Assisted inputs; and workload/editor/provider evidence before selecting numeric journal defaults.

### C11. Final H1–H4 pressure and update classification

| Hypothesis | Challenge pressure | Status to carry into RES |
|------------|--------------------|--------------------------|
| **H1** — on-demand-only catalogue without degraded discovery | four FA conditions recovered state, but absent view imposed a scan and NH is absent | **refuted as stated; hybrid confirmed** — permanent router + persisted derived index + authoritative re-read |
| **H2** — tiny task-local carrier is safer and human-understandable | nine-field strict subset rejected every parser/legality attack; no NH | **partially confirmed** — strict reduced YAML confirmed structurally; human clause requires TS acceptance |
| **H3** — separate closed bounded journal preserves continuity | recovery/rollover survived; `landed` removed; finite mechanism retained without fake constants; PR absent | **confirmed at architecture level, acceptance evidence required** |
| **H4** — shared Assisted/Full task semantics | exact accounting found carrier/path differences but no different lifecycle/epoch/event meaning; Assisted runtime absent | **confirmed at semantic-contract level, migration acceptance required** |

#### Amendment proposals — frozen §§1, 3–7

**None.** L3 preserves the frozen journal handoff and Git provenance outcomes. The nine-field core, strict parser, rollover mechanism, G-A pins and unresolved migration state refine how the frozen architecture is achieved without changing its declared outcomes, DoD, DoF or principles.

#### Free refinements — coordinator may apply to §§2, 7.2, 8–11

| Target | Refinement supported by Challenge |
|--------|----------------------------------|
| §2 | update current board split to 39 eight-cell / 21 nine-cell and record exact 111→60 migration accounting |
| §7.2 | cite YAML application-profile boundary and Git reachability/trailer/path contracts |
| §8 | close deterministic architecture research; retain NH, PR, L3 integration, Git matrix and migration runtime as Phase-A dependencies |
| §9 | replace post-commit `landed` risk with L3 duplicate/reachability rules; add G-A pin corruption and explicit unresolved migration risks |
| §10 | record final H1–H4 pressure and classify NH/PR as mandatory TS acceptance rather than inferred research success |
| §11 | add manifest-versus-commit identity, explicit unresolved migration and non-Git-resume/Git-release separation insights |

Detailed field/event schemas, failure codes, migration resolver and L3 commands belong in TS/canonical implementation, not in the frozen HL.

### C12. Deep-mode Challenge loops and metacognitive check

| Loop | Attack focus | Counter-evidence found | Decision |
|------|--------------|------------------------|----------|
| 1 — status/YAML/recovery | remove nine fields; illegal conditional/profile combinations; YAML extensions/partials; finite rollover | `journal_head` could be replaced only by carrying an equivalent event locator; strictness is application-defined, not YAML-defined | **Decision 1:** retain exactly nine shared fields; profile/conditional branches fail closed; keep configurable count+byte mechanism without defaults |
| 2 — L3/Git | every requested landing and G-A failure, including duplicate/rebase/pins | two valid matching commits are possible; `--all`/newest would be unsafe; a rebased exact commit remains identifiable | **Decision 2:** L3 requires exactly one reachable match on a pinned ref; G-A needs canonical local pins; G-B remains baseline |
| 3 — migration/evidence/contract | exact-once live census, synthetic action gate, frozen amendment and Quality Contract | forcing valid controls would invent facts; NH/PR cannot be obtained by more local reasoning | **Decision 3:** explicit unresolved state survives; no amendment; proceed to RES with mandatory NH/PR TS acceptance |

Metacognitive check:

- **NEW:** duplicate *valid* L3 matches are not theoretical; the fixture created two and forced a stop rule.
- **NEW:** rebase tolerance follows from manifest correlation, while branch/ref eligibility must remain pinned.
- **NEW:** exact accounting is 111 source occurrences → 60 logical tasks, with nine board-only and zero directory-only tasks.
- **NEW:** the nine-field core survives removal only under the current event-ID/segment-locator grammar; combining pointer fields would be a representation change, not semantic reduction.
- **CONFIRMED:** C1-R authority/projection separation, event-first recovery, G-B exact scope, stable paths and shared edition semantics.
- **STILL ACCEPTANCE-ONLY:** NH, PR, populated Assisted migration, Git support matrix, L3 workflow integration and numeric defaults.

## Checkpoint

| Found | Remaining for RES/TS acceptance |
|-------|---------------------------------|
| C1-R2 survives all local attacks; eliminated families do not reopen | RES must synthesize decisions without copying stage detail |
| all nine core fields have first-failure readers; conditional/profile branches unambiguous | TS must encode the closed schema and stable diagnostics |
| strict YAML, partial visibility and recovery fail closed | PR must reproduce provider reconnect/conflict artefacts |
| L3 unique-reachable-match protocol survives and recomputes without writes | TS fixture must integrate real resume/release and duplicate/rebase/ref cases |
| combined finite rollover survives; numbers remain unresolved | TS acceptance must select/configure values from workload evidence or preserve explicit project configuration |
| guarded G-A survives pinned canonical checks; G-B is operational baseline | supported Git platform/version/capability matrix required |
| every live source occurrence and synthetic task is accounted exactly once | migration must run on a copy/manifest and include populated Assisted evidence when available |
| no frozen-HL amendment is required | free refinements must remain separate from TS detail in RES |

**Evidence state:** FA, UH, DF, RR and PS are present and bounded. NH and PR are absent. Challenge neither simulates nor upgrades them.

**Recommendation at this gate:** approve RES synthesis. Iteration 2 has sufficient architectural evidence to recommend **SUFFICIENT** research while making NH, PR and the listed integration/runtime items mandatory Phase-A TS acceptance evidence. No iteration 3 is recommended unless the Coordinator intentionally chooses to gather those external acceptance observations during research rather than implementation.

**Questions for the Coordinator:** none. The required attacks produced deterministic dispositions.

**Files written at this gate:** `research/iter2/1_briefing.md`; `research/iter2/2_gather.md`; `research/iter2/3_extract.md`; `research/iter2/4_challenge.md`.

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked and survivors/eliminations listed?
- [x] At least two decisions and one hypothesis tested (deep mode)?
- [x] Counter-evidence actively produced for T1–T3?
- [x] Amendment versus free refinement classified?
- [x] NH/PR evidence boundary preserved?
- [x] Metacognitive NEW-versus-confirmed check completed?

Stage complete: YES
→ User decision: WAIT — Coordinator must approve RES synthesis or redirect a failed invariant.
