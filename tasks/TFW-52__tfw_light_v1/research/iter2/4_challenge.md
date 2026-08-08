# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. The configurations are attacked below; every survivor is conditional on evidence, and every elimination names its reason.
> **Test:** "Would the surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-52](../../HL-TFW-52__tfw_light_v1.md)
> Goal: Determine the smallest reliable Assisted mechanisms for discipline, collaboration, identity, and durable memory while preserving Light's simplicity and the approved edition boundary.

## Challenge method and evidence lanes

Challenge ran three DEEP-mode passes without modifying the approved HL, its plan, any adapter/product/control file, or a real synchronized folder:

1. **Contract attack:** recheck current official Codex behavior for hook trust, callback concurrency, instruction lifetime/root discovery, Stop re-entry, Windows commands, working directory, and scheduled-task availability.
2. **State-machine attack:** run in-memory cases for corrupt/future clocks, dirty/incomplete state, scheduled/start overlap, two consolidators, corrupt receipts, conflict copies, index recovery, copied/shared-device bindings, automation attribution, and task activation.
3. **Pairwise elimination:** compare C0/C1/C2 under the same attacks, preserve C3 only as the external ceiling, then remove mechanisms whose complexity did not carry a necessary invariant.

The four evidence lanes remain distinct:

- **Documented platform support:** current official Codex/Google documentation.
- **Observed local behavior:** read-only host/repository observations from this iteration.
- **Unavailable or unproven:** callbacks, sync ordering, identity, or guarantees not exercised here.
- **Proposed adapter/research behavior:** the survivor below; it is neither current Codex behavior nor an owner decision.

The stage used the current official [Codex manual](https://developers.openai.com/codex/codex-manual.md), with targeted confirmation from the current [hooks](https://learn.chatgpt.com/docs/hooks), [scheduled tasks](https://learn.chatgpt.com/docs/automations?surface=app), and [`AGENTS.md` discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md) pages. The manual/page contracts still say that changed non-managed hooks are skipped until their new hash is trusted, matching command hooks launch concurrently, commands run from the session `cwd`, `AGENTS.md` is assembled once per run, and local-file schedules need the computer and desktop app running. Official [Google Drive recovery guidance](https://support.google.com/drive/answer/2565956?co=GENIE.Platform%3DDesktop&hl=en) remains counter-evidence to treating synchronized-folder publication as a transaction: failed sync can require retry or recovery from retained copies.

The OpenAI manual helper and Docs MCP installation were not used because both would create configuration/cache state outside the five owner-permitted iteration files. The official manual/pages were read directly in memory instead.

## Consistency Check

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D1 Root/instruction authority | Git/current-directory discovery only | D17 Platform implementation | Non-Git synchronized folder opened below/alongside intended root | Official discovery may stop at `cwd`; Git-only resolution cannot establish the intended standalone Assisted authority. |
| D1 Root/instruction authority | Missing/wrong Assisted marker | D2 Enforcement surface | Hook mutates durable state anyway | The handler cannot prove project authority and could modify the wrong project; it must fail closed. |
| D2 Enforcement surface | Non-managed changed/untrusted hooks | D3/D4/D5 | Claims of automatic start/checkpoint/Stop enforcement | Current Codex skips the changed definitions, so automatic enforcement is absent until review/trust. |
| D2 Enforcement surface | Multiple matching command hooks | D4/D5 | Concurrent mutable trace repair | Matching commands can launch concurrently; read-modify-write repair can race. Validation, unique append, or model continuation is safer than hook-side mutable repair. |
| D2 Enforcement surface | Command hooks | D15 Task activation | Reliable semantic prompt classifier | Only command handlers execute; deterministic code cannot reliably infer every substantive task from natural language and tool variety. |
| D3 Session-start context | `SessionStart` | D15 Task activation | Every start creates a task | Session lifecycle is not durable-work intent; this produces false tasks for reading, orientation, and non-work conversation. |
| D3 Root instructions | Once-per-run `AGENTS.md` chain | D2 Enforcement surface | Mid-session policy update is immediately authoritative | A stale already-running session does not rebuild its instruction chain merely because the file changed. |
| D4 Checkpoint trigger | `PreCompact` only | D5 Completion | Reliable trace continuity | A missing/skipped callback or already-missing task state defeats it; the trace must be maintained continuously and the event treated as a backstop. |
| D5 Completion gate | Stop continuation | D5 Completion gate | Unbounded repeat until valid | Stop exposes the re-entry flag; blocking repeatedly can loop. The minimal policy permits at most one continuation per turn, then records/reports unresolved state. |
| D6 Weekly execution | Desktop local schedule | H2 calendar freshness | Codex desktop closed | Official guidance requires the desktop app running when local files are needed. |
| D6 Weekly execution | Web schedule | D17 local synchronized folder | Direct local-folder maintenance | Hosted execution cannot directly reach the local folder without another storage/runtime layer. |
| D6 Weekly execution | Schedule + start trigger | D9/D10 | Mutable single-run state | Simultaneous triggers can overlap; both must invoke the same unique-run/idempotent protocol or one trigger must be removed. |
| D7 Staleness signal | Timestamp only | H2 freshness | Future/corrupt/missing clock state treated as fresh | Clock corruption can suppress work indefinitely; invalid/future timestamps must conservatively mean due and cannot override dirty/incomplete/index evidence. |
| D9 Consolidator coordination | Shared expiring lease | H3 one-consolidator guarantee | Strict offline mutual exclusion | Both offline clients can see no lease and acquire it; a shared-folder lease cannot be the safety authority. |
| D9 Consolidator coordination | Two possible runs | D10 Record publication | Mutable in-place only | A crash, late sync, or conflict copy can hide/overwrite the only result and leave no reconciliation evidence. |
| D10 Record publication | Immutable/versioned accepted records | D11 Index publication | Full rebuild | Compatible and preferred: primary evidence survives derived-view loss. |
| D11 Index publication | Active pointer as authority | H3 recovery | Conflicted/corrupt pointer | The pointer can split or corrupt; only accepted records/receipts may be authoritative, with the index/pointer treated as disposable. |
| D12 Identity selection | Device-local binding | D14 Authorship provenance | Authentication/non-repudiation | A copied/shared-device preference can select a profile but cannot verify the physical actor. |
| D12 Identity selection | Participant binding | D14 Authorship provenance | Automated consolidation attributed to bound participant | Automation is a separate actor type; borrowing the local participant silently fabricates authorship. |
| D15 Task activation | Every/substantive-looking prompt | Non-work policy | No false tasks | Natural-language advice and ordinary conversation can sound substantive without requesting a durable outcome. |
| D16 Risk handling | Promotion-time gate only | D8 append-only shared candidate | Secrets/sensitive data protection | The candidate may already have synchronized before consolidation; risk filtering must occur before shared candidate creation as well as before promotion. |
| D17 Platform implementation | POSIX/Git-relative command only | Windows/non-Git target | Cross-platform support | `cwd`, command name, quoting, runtime, path, case, and reserved-name behavior differ; official Windows override support does not make a POSIX handler portable. |
| Local Codex memories | Generated personal state | Shared-memory authority | Deterministic collaboration/rebuild | Local generated memory is not synchronized primary evidence or a deterministic recovery source. |

### Pairwise attacks on C0/C1/C2

| Attack | C0 vs C1 | C0 vs C2 | C1 vs C2 | Pairwise ruling |
|---|---|---|---|---|
| Untrusted/changed hooks | C0 avoids hook trust but has no mechanical gate; C1 silently loses its automation unless absence is surfaced | C2 loses still more behavior when hooks/schedule are unavailable; C0 remains manually usable | Both depend on trusted hooks; C2 has more skipped surfaces | Keep C0 as explicit degraded fallback; automatic Assisted claims require a trusted-installation precondition. |
| Stale session/`AGENTS.md` | Both can retain old rules; C1's already-fired start hook does not refresh a stale run | C2's wider events do not rebuild the instruction chain | Neither solves mid-run authority changes | Require a new session/retrust after contract changes; no configuration earns an unconditional stale-session guarantee. |
| Wrong/absent root marker | C0 can operate in the wrong discovered root; C1 can fail closed on a marker | C2 has the same marker advantage over C0 | C1 and C2 tie | Import marker validation into the survivor; keep topology selection out of scope. |
| Duplicate/missing callbacks | C0 has no callback duplication but can miss every lifecycle action; idempotent C1 validation tolerates duplicates | C2 hook-side repair/publication has the larger race surface | C1's smaller read-only/append-only hook contract is safer | Use hooks for context/validation/unique receipts, not concurrent mutable repair; continuous trace is primary. |
| Stop continuation loop | C0 cannot loop but can end inconsistent; C1 can repair once and must then stop looping | Same C0/C2 tradeoff | C1 and C2 both need the same one-continuation rule | Retain Stop, bound it to one continuation, and report unresolved state after re-entry. |
| False/missed task activation | C0's explicit command avoids false tasks but misses unannounced durable work; C1's durable-boundary rule reduces both but is model-mediated | C2 can guard known write paths, yet unknown durable tools still escape until Stop | C2 improves known-path coverage but cannot close the semantic/tool-surface gap | Retain `active_task = none`, model-driven activation, and explicit fallback; do not claim complete semantic enforcement. A narrow known-path guard is optional only after coverage tests. |
| Clock/state corruption | C0 time-only catch-up can be falsely fresh; C1 hybrid state survives more cases | C2's broader hybrid also survives, but scheduling does not help corrupt state | C1 can import C2's incomplete/index predicates without schedule | Keep hybrid conservative staleness; remove default desktop scheduling. |
| Schedule/start overlap | C0/C1 catch-up-only avoid the second trigger | C2 needs unique-run reconciliation for its own duplicate trigger | C1 is simpler unless wall-clock execution is an explicit requirement | Default to catch-up-only; use C3-class external scheduling only for a separately approved calendar SLA. |
| Offline dual consolidators | C0/C1 guardian/manual evidence is too weak for divergent runs | C2's immutable manifests/receipts/reconciliation survives structurally | C2 recovery evidence is necessary even if its schedule/lease is removed | Import C2's recovery core into a smaller C1-shaped configuration. |
| Lease and pointer failures | C0 has neither; C1's advisory lease adds no safety; C2's pointer adds another conflictable view | C2 recovers only because receipts/records, not because lease/pointer | C1 full rebuild is simpler than C2 pointer; both can omit lease | Remove shared lease and authoritative pointer from the minimum. |
| Copied/shared-device identity | C0 asks per durable task and is safer; C1 binding is quieter on private devices | C2 adds run/device provenance but still cannot authenticate | C1/C2 bindings need private-device/mismatch rules; neither proves identity | Make binding optional/private-device-only; ask once on shared/mismatched/stale state. |
| Automation attribution | C0 manual guardian attribution can still conflate initiator/author; C1 needs actor separation | C2's run provenance makes separation clearer | Import C2's automation actor/run receipt into the survivor | Record `actor_type = automation`; never borrow bound participant identity. |
| Privacy/risk failure | C0 allowlist is safer but less quiet; C1/C2 category gates may already have written a risky candidate | C2's immutable append-only design makes late redaction impossible | Neither C1 nor C2 survives with promotion-only gating | Add capture-time gating; secrets never enter shared candidates, and sensitive/high-stakes material is held/redacted/pointered before sync. |
| Windows/non-Git | C0 portable text is usable but root-weak; C1 needs per-OS commands and marker | C2 adds more runtime/platform assumptions | C1's smaller handler set is easier to make cross-platform | One state contract plus explicit Windows/POSIX entrypoints; no Git-only locator. |

### Surviving configurations

No Extract configuration survives unchanged.

| Config | Root/lifecycle | Freshness | Shared memory | Identity/risk | Status |
|---|---|---|---|---|---|
| **S1 / C1-R — minimal recovery-assisted** | Marker-aware `AGENTS.md`; trusted `SessionStart`, `PreCompact`, and one-shot `Stop` validation; continuously maintained trace; explicit start/close fallback | Catch-up only at start/first shared-memory consumption; conservative hybrid predicate | Unique immutable candidates; designated guardian; no shared lease; unique run manifests and immutable receipts; deterministic identical-run reconciliation; explicit divergent conflict; immutable accepted records; full rebuildable index | Single profile auto; optional private-device binding for multiple profiles; one question on new/shared/stale/mismatch; automation actor; capture- and promotion-time risk gate | **Primary research survivor, conditional and unapproved** |
| **S0 / C0-F — manual degraded fallback** | Current instructions plus explicit start/checkpoint/close skill | Explicit catch-up before shared-memory use | Same immutable candidate/receipt/rebuild format as S1, run manually | Ask once per durable task when multiple profiles; same risk gates | **Operational fallback only; does not satisfy automatic-enforcement claims** |

**C2 as a bundle is eliminated**: its default desktop schedule, broad hook set, shared lease, and active-pointer publication add failure modes without supplying strict calendar execution, semantic classification, mutual exclusion, or knowledge authority. Its immutable run evidence, split-brain detection, automation provenance, and reconciliation are retained inside S1.

**C3 is not a survivor in the Assisted space.** It remains the external ceiling for wall-clock execution while Codex is closed, genuine distributed locking/fencing, and authenticated/signed authorship. Those guarantees require operational infrastructure beyond the smallest local Assisted configuration.

**Unexpected survivor:** C0 survives as S0 only as an explicit degradation path. It is useful because untrusted/unsupported hooks do not have to make the project unusable, but the UI/trace must say “manual safeguards active” rather than claiming automatic enforcement.

## Findings

### C-F1 — Hook failure attacks narrow H1 from “reliable lifecycle” to conditional validation

| Scenario | Attack result | S1 response | Residual limit |
|---|---|---|---|
| Hook definition installed but not trusted | Current Codex skips it | Installation/review is an explicit precondition; known absence selects S0 and surfaces one setup status | If neither current instructions nor hooks run, the system cannot announce its own absence. |
| Previously trusted hook changes | New hash requires review and is skipped | Contract version changes require re-review and a new session | Existing session may still hold old guidance. |
| `AGENTS.md` changed during a run | Instruction chain remains stale | Start/close fallback reads current project state; material Assisted changes require restarting | No current mechanism forces a running model to rediscover `AGENTS.md`. |
| Wrong or absent marker | `cwd`/Git discovery can identify a different authority | Every handler walks ancestors for an explicit marker and validates project ID/version; absent/ambiguous marker fails closed before durable work | Marker scheme is proposed and locally unexecuted. |
| Duplicate event/multiple matching hooks | Commands can launch concurrently | Handlers are idempotent validators or append unique receipts; they do not race to rewrite the trace/index | Other independently installed hooks can still affect behavior. |
| Missing `PreCompact` callback | No last-moment checkpoint | Trace is updated continuously; PreCompact only validates/appends a snapshot of already-durable state | If the model failed to persist state earlier, the hook cannot recreate semantic intent. |
| Stop finds inconsistent active task | Continuation can repair | Block at most once, using the Stop re-entry flag; the agent aligns state and retries | A second failure is reported/recorded unresolved rather than looped. |
| Stop with no active task | An unconditional gate could create noise | Exit silently; `active_task = none` is valid | None for the no-task invariant. |

The official documentation supports the event and failure surfaces, not the proposed S1 semantics. Local observation still shows no installed repository/global hooks, so actual callback ordering, trust prompts, compaction, and Stop continuation remain untested on this host.

H1 therefore does not survive as an unconditional statement. The event trio is still the smallest plausible lifecycle set, but only if:

- installation/trust/root/version preconditions are explicit;
- the model maintains the trace continuously;
- hooks validate inspectable state instead of claiming semantic understanding;
- PreCompact is a backstop, not the only checkpoint;
- Stop is one-shot and idempotent;
- non-work sessions may remain task-free.

### C-F2 — Task-activation attacks expose one unresolved enforcement gap

The in-memory task-boundary model tested five cases:

| Case | Pre-write guard | Stop detects omission | Trace-first result |
|---|---:|---:|---|
| Ordinary explanation | no block | no | valid no-task |
| Substantive-sounding advice with no durable outcome | no block | no | valid no-task |
| Known result path write without active task | block | yes | trace-first preserved if that tool/path is covered |
| Unknown durable tool/side effect without active task | no block | yes | **trace-first missed; Stop is late** |
| Known write with active task | no block | no | valid active task |

This is counter-evidence to claiming that start/compact/Stop alone “reliably” activate and maintain every task. A broad prompt classifier creates false positives; a tool/path guard has finite surface coverage; Stop detects some omissions only after durable work.

S1 keeps the smallest honest behavior:

1. session/project start initializes context and `active_task = none`;
2. the model transitions to an active task before intended durable work;
3. an explicit start command is the ambiguity/manual fallback;
4. a narrowly scoped pre-write guard may protect known result/shared-state paths only after executed coverage tests;
5. Stop validates final consistency but is never advertised as proof that tracing preceded every side effect.

Whether the target Assisted surfaces can cover all durable writes remains unresolved and belongs in implementation evidence, not an HL assertion of platform fact.

### C-F3 — H2 survives only as catch-up-before-consumption

The in-memory staleness predicate treated six states as follows:

| State | Result |
|---|---|
| Fresh timestamp, no inputs/incomplete run/index mismatch | no run |
| Fresh timestamp with unreceipted candidates | run |
| Corrupt timestamp | run conservatively |
| Timestamp materially in the future | clock anomaly + run conservatively |
| Fresh timestamp with incomplete run | run |
| Fresh timestamp with accepted-record/index digest mismatch | run |

The surviving predicate is:

```text
needs_run = interval_due_or_clock_invalid
         OR unreceipted_candidate_ids_exist
         OR incomplete_or_invalid_run_receipt_exists
         OR index_digest_mismatches_accepted_records
```

Missing/corrupt state means due, never fresh. `last_attempt_at` cannot clear the predicate; only a valid completion/reconciliation result can update success state.

Pairwise attack removes the default desktop schedule:

- C1 catch-up-only has one trigger and one observable promise: before first shared-memory consumption after reopening, catch up or state that memory is stale.
- C2's desktop schedule cannot run against local files while the app is closed, so it does not supply the disputed calendar-time guarantee. It adds schedule/start overlap while still needing catch-up.
- If an owner later requires wall-clock freshness, C3-class external scheduling must invoke the same unique-run protocol and recover missed runs after sleep/offline periods. That is a different operational requirement, not a quiet default.

Routine catch-up asks no question. Conflicting/sensitive material is held and, only when necessary, presented as one compact batch. Automation uses its own run identity rather than triggering a participant identity prompt.

### C-F4 — H3 survives after removing the lease and authoritative pointer

The Challenge fixture exercised recovery, not real Drive behavior:

| Attack | Observed in-memory result | Surviving rule |
|---|---|---|
| Two offline lease claimants | Both claimed; strict exclusion was false | No shared lease in S1's safety core. A designated guardian reduces routine overlap only. |
| Two runs, same input and normalized output | Output digests matched; classified duplicate-equivalent | Preserve both receipts and reconcile to one semantic accepted result with all provenance. |
| Two runs, same input and divergent output | Output digests differed; classified explicit conflict | No last-writer winner; preserve both proposals/sources and require deterministic rule or one human resolution. |
| Started manifest without completion | Not accepted; classified incomplete/rerun | Retain candidates and staging; rerun/reconcile idempotently. |
| Completion with wrong digest | Not accepted; classified invalid digest | Hold corrupt receipt/output; never advance accounted/accepted state. |
| Completion without started manifest | Not accepted; classified orphan | Require a valid run chain; preserve physical evidence for review. |
| Five physical candidate-like files including conflict copies | Strict filenames found 2; payload/schema scan recovered 3 unique candidate IDs and held 1 invalid file | Scan every candidate-area file by schema/payload identity; filename is only a locator. |
| Corrupt index pointer | Pointer digest failed; two accepted records rebuilt two entries | Index/pointer is disposable; accepted records and immutable receipts are authority. |

The smallest recovery protocol is therefore:

1. Writers create immutable candidates with unique payload IDs; no shared counter.
2. One designated guardian normally initiates consolidation; no lease is needed for safety.
3. Every run has a unique immutable started manifest containing input IDs/digest.
4. Proposed outputs remain namespaced/immutable until a valid completion receipt exists.
5. Identical overlapping completed runs reconcile automatically by normalized input/output digests while preserving both run receipts.
6. Divergent overlap becomes an explicit conflict; no output silently overwrites the other.
7. Accepted records are immutable/versioned with source IDs and supersession/conflict state.
8. `INDEX.md` is a derived full rebuild with an accepted-record digest; a missing/corrupt/conflicted copy is rebuilt, not repaired incrementally.
9. Candidates are not deleted merely because a run started/completed; pruning, if ever allowed, requires separate accounted-for evidence and remains outside this minimum.

A late-arriving offline run can surface after an apparently clean reconciliation. The next catch-up must rescan manifests/receipts and may supersede the derived index or reopen a conflict. This yields eventual detection/recovery, not instantaneous cross-device consistency or a proof that knowledge loss is impossible.

### C-F5 — H4 survives for declared attribution after copied/shared-device attacks

The identity fixture used two stable profiles, a renamed display value, local device IDs, a shared-device flag, and an automation actor:

| Case | Result |
|---|---|
| Non-work unknown user | no actor, no question |
| Valid binding on the same private device | auto-selected stable profile; current renamed display resolved correctly |
| Binding copied to a different device ID | binding invalid; one question at first durable transition |
| Binding on a declared shared device | binding not reused; one question at first durable transition |
| Binding to deleted profile | stale; one question |
| Automated consolidation with participant binding present | `actor = automation`; no participant question |

S1 narrows device binding to a convenience for a private device. The local record contains only stable project ID, stable profile ID, non-secret local device-instance ID, and minimal binding metadata. It remains outside the synchronized folder. A new/mismatched/shared device asks once when attribution becomes necessary; reading/non-work never asks.

Copying both a binding and its non-secret device ID can still impersonate the declaration. A shared machine can also be used by someone else after a valid selection. Therefore S1 records declared provenance—profile ID, display snapshot, task/source/time, automation/run ID—not authentication or non-repudiation. C3 remains the ceiling for account verification/signing.

Automation provenance has two distinct roles:

- `actor_type = automation` and run/device receipt identify the executor;
- an optional guardian/initiator profile identifies operational responsibility only when explicitly known.

Neither field silently assigns candidate authorship to the locally bound participant.

### C-F6 — Append-only memory makes capture-time privacy gating mandatory

Promotion-only risk review fails: once a secret or sensitive fact is written to an append-only shared candidate, later consolidation cannot make the synchronized copies cease to exist. This is a new Challenge finding and applies to C0/C1/C2.

| Category | Before shared candidate creation | During consolidation/publication |
|---|---|---|
| Routine project fact/decision/preference | May create a sourced candidate quietly | May consolidate quietly when provenance/confidence rules pass |
| Ambiguous/contradictory | Candidate may preserve competing claims without choosing | Publish unresolved/conflict state; batch one question only if needed |
| Health/medical, minors, personal/sensitive data | Hold locally, redact, or create a safe pointer; explicit opt-in before shared identifiable content | Never infer consent from candidate presence; require appropriate confirmation |
| Legal dispute/high-stakes finance/safety | Preserve as sourced unresolved material, not an established fact | Human-confirmed status before promotion or decision reliance |
| Password/token/key/secret | Never write the value or a reversible/guessable derivative to candidate/trace/index | Record only safe remediation metadata; warn and advise secure storage/rotation as appropriate |
| Ordinary non-work conversation | No task, candidate, identity, or shared memory | Nothing to consolidate |

Command hooks can catch structural and some secret-pattern cases, but semantic false positives/negatives remain. “Hold, do not guess” is the surviving default for uncertain risk categories. Automatic shared capture/promotion of sensitive or high-stakes content should be deferred.

### C-F7 — Wrong-root, Windows, and non-Git attacks require fail-closed portability

- Official `AGENTS.md` discovery does not provide an Assisted-specific root guarantee. A non-Git project may load only the current directory; a nested source inside this repository inherits root guidance and is not evidence of standalone behavior.
- Each S1 handler must start from `cwd`, walk ancestors for exactly one expected Assisted marker, validate stable project ID/schema/contract version, and fail closed on none/ambiguity/mismatch before durable work.
- A stale session does not reread changed guidance. Updating the marker/contract requires a new run and hook re-review when definitions changed.
- One state-machine contract can be portable, but commands cannot be assumed portable. Windows needs a reviewed Windows command/runtime; POSIX needs its own entrypoint. The handler must not depend only on `git rev-parse`, `python3`, POSIX quoting, case-sensitive names, or slash conventions.
- Payload IDs/digests, not filenames, carry identity. Normalize Unicode/text encoding, line endings, timestamps, relative logical paths, and casing policy before hashing; reject unsafe/reserved physical names per platform.
- Local rename/replace behavior is not evidence of sync atomicity. S1 relies on immutable unique paths, receipts, validation, and rebuild.
- Light → Assisted and wrong-root remain bounded validation fixtures. No C1-R element selects X1/X2/X3, changes the edition source topology, or authorizes migration/product edits.

### C-F8 — C3 remains only the external guarantee ceiling

Only external infrastructure can materially change three attacked boundaries:

- an OS/service scheduler can run while the Codex desktop app is closed, provided the machine/runtime/storage remain available;
- a real lock/fencing service can serialize consolidators more strongly than a shared Drive lease;
- an account/cryptographic identity system can authenticate/sign provenance rather than record a declaration.

These are useful claim boundaries, not reasons to include C3 in Assisted v1. They add credentials, deployment, availability, recovery, administration, and cross-platform operations that are not justified by the 2–3-person local synchronized-folder target. Research recommends deferring them unless an owner separately approves calendar-time SLA, strict serialization, or authenticated authorship as requirements.

### C-F9 — Smallest surviving Assisted recommendation

**Research recommendation S1 / C1-R: lifecycle-checked, catch-up-only, recovery-based Assisted.** It contains only mechanisms that carried an attacked invariant:

1. **Authority:** short `AGENTS.md` rules plus explicit Assisted marker/project ID; fail closed on wrong/absent/ambiguous root.
2. **Lifecycle:** trusted `SessionStart`, `PreCompact`, and `Stop`; handlers inject/validate inspectable state and append unique evidence rather than racing mutable repairs. Trace maintenance is continuous; Stop continues at most once. Explicit start/close remains the manual fallback.
3. **Task/no-task:** `active_task = none` is valid; create a task only before intended durable work; no task/identity/candidate for reading or non-work. Known-path guards may be evaluated, but complete semantic/tool coverage is not claimed.
4. **Freshness:** lazy catch-up before first shared-memory consumption, using time + dirty inputs + incomplete/invalid receipts + index digest. No calendar-time promise.
5. **Candidates:** immutable unique payload IDs with stable declared author provenance and capture-time risk gating.
6. **Consolidation:** designated guardian, no shared lease; unique run manifests, immutable started/completed/reconciled receipts, automatic identical-run reconciliation, explicit divergent conflict.
7. **Knowledge authority:** immutable/versioned accepted records and source mappings; full rebuildable `INDEX.md`; no authoritative pointer or incremental-only index.
8. **Identity:** single valid profile auto; multiple profiles use an optional private-device binding or one short question at the first attribution-required action; shared/copied/stale binding asks; no shared `CURRENT_USER`; automation is its own actor.
9. **Risk:** secrets excluded before candidate creation; sensitive/high-stakes material held/redacted/sourced and confirmed before shared promotion.
10. **Portability:** common state schemas/invariants with explicit Windows and POSIX command entrypoints; non-Git root resolution; no cross-device atomicity claim.

S0/C0-F uses the same durable data/identity/risk format through explicit skills when hooks are unavailable, but it must be labeled degraded/manual rather than equivalent automatic enforcement.

### C-F10 — Mechanisms to remove or defer from the minimum

| Mechanism | Disposition | Evidence-based reason |
|---|---|---|
| Desktop scheduled consolidation | **Remove from default** | Cannot run on local files with the app closed; catch-up remains necessary and avoids a second trigger. |
| Shared expiring Drive lease | **Remove from safety core/default** | Offline dual claimants defeat exclusion; guardian + immutable recovery evidence is simpler and honest. It may be reconsidered only as a measured collision-reduction optimization. |
| Versioned active-index pointer as authority | **Remove** | Pointer can conflict/corrupt; full rebuild from accepted records is adequate at Assisted scale. |
| Incremental-only index edits | **Remove** | Harder to recover/verify than full rebuild for a small record set. |
| Broad prompt/tool hook set as semantic task classifier | **Defer** | Command handlers cannot reliably classify intent; unknown durable surfaces still escape. A targeted known-path guard needs executed coverage evidence. |
| Hook-side concurrent mutable trace/index repair | **Remove** | Matching hooks can run concurrently; validation, unique receipts, and agent continuation are safer. |
| `SessionEnd` as completion authority | **Remove** | Advisory/delayed and cannot steer; Stop/explicit close carries the gate. |
| Transcript parsing as primary state | **Remove** | Exposed transcript paths are not a stable hook interface; task truth must be in explicit files. |
| Local Codex memories as shared authority | **Remove** | Local generated convenience state is not synchronized/rebuildable evidence. |
| Shared `CURRENT_USER` | **Remove** | Cross-device race and silent misattribution; stable profiles plus local selection are sufficient. |
| Automatic shared capture/promotion of sensitive/high-stakes content | **Defer** | Promotion-time review is too late for append-only synchronized candidates; semantic classification remains fallible. |
| External OS scheduler/service, distributed lock/fencing, authenticated signing | **Defer as C3** | Needed only for calendar SLA, strict serialization, or authenticated authorship; exceeds minimal local Assisted. |

## Research verdicts, not owner decisions

These are Challenge-stage research verdicts for later RES synthesis. They do not modify or reinterpret the approved HL.

| Hypothesis | Research verdict after Challenge | Bounded survivor | Remaining proof gap |
|---|---|---|---|
| **H1** | **Literal reliability challenged; conditional lifecycle support survives** | S1 uses the documented event trio as validation/backstop with continuous trace, fail-closed root, explicit fallback, and bounded Stop | No local hook execution; stale/missing hooks cannot self-enforce; semantic task activation/tool coverage remains incomplete |
| **H2** | **Next-start form supported; calendar-time similarity challenged** | S1 catch-up barrier plus conservative hybrid staleness | Closed-app delay is unbounded; only external C3 can change it, and sleep/offline still require recovery |
| **H3** | **Literal prevention/one-consolidator claim challenged; recoverability design survives** | Unique immutable candidates + guardian + immutable run receipts/reconciliation + immutable records + full rebuild | No real Drive test; late sync, corrupted primary records, and human conflict resolution remain operational risks |
| **H4** | **Declared attribution UX supported; authentication interpretation challenged** | Stable IDs, single auto, private-device binding/one question, automation actor, provenance | Copied credentials/preferences and shared devices can misdeclare; authenticated authorship requires C3 |

**Owner decisions made in this stage:** none. The owner-approved master HL and plan remain unchanged. If RES recommends wording changes, it will present the exact proposed text separately for owner approval and will apply nothing.

## Challenge Decisions (research-process only)

| # | Decision | Rationale |
|---|---|---|
| **C-D1** | Eliminate C0, C1, and C2 as unchanged primary configurations; carry S1/C1-R as the sole primary research survivor and S0/C0-F only as degraded fallback. | C0 lacks automatic enforcement/recovery evidence, C1 lacks split-brain recovery, and C2 adds schedule/lease/pointer/broad-hook complexity without gaining their claimed guarantees. |
| **C-D2** | Remove desktop scheduling, shared lease, and authoritative index pointer from the default minimum. | Catch-up covers next-start freshness; lease does not exclude; index is safely derived/rebuildable. |
| **C-D3** | Retain `SessionStart`, `PreCompact`, and `Stop`, but restrict them to idempotent context/validation/unique evidence; continuous trace and one-shot continuation carry lifecycle safety. | Concurrent/untrusted/missing callbacks make mutable hook-side repair and single-event dependence unsafe. |
| **C-D4** | Preserve C2's immutable run manifests/receipts, split-brain detection, reconciliation, and automation provenance inside S1. | These controls, unlike the lease, recovered the dual-run/interruption/corruption model. |
| **C-D5** | Add capture-time risk gating as a viability invariant before shared candidate creation. | Append-only synchronization makes promotion-only screening irreversibly late for secrets/sensitive material. |
| **C-D6** | Keep semantic task activation and authentication as explicit boundaries, not platform guarantees. | Unknown durable tool paths can evade pre-write checks; local profile selection cannot verify a person. |
| **C-D7** | Defer C3 mechanisms unless an owner approves distinct calendar-SLA, strict-locking, or authenticated-authorship requirements. | External operations are materially more complex than Assisted v1 and solve different requirements. |
| **C-D8** | Reserve exact HL wording recommendations for RES; apply none. | The coordinator explicitly required Challenge findings to remain research verdicts, and the owner lock makes HL immutable. |

## Counter-evidence retained for RES

- Current official contracts describe the event surfaces but not S1's proposed project semantics.
- This host has trusted project configuration but no installed hooks; H1 is not locally executed.
- A stale running session can retain old `AGENTS.md`; no in-scope mechanism forces rediscovery.
- Unknown durable tools can make Stop detection late, so universal trace-first activation is unresolved.
- Desktop scheduling cannot satisfy closed-app calendar freshness for local files.
- Offline dual lease claimants both proceed; no shared-folder lease is strict exclusion.
- Real Drive ordering, late-arriving runs, and cross-device atomicity were not tested.
- Conflict reconciliation can preserve evidence but cannot automatically decide genuinely divergent meaning.
- Device binding supports a declaration, not proof of physical actor; copied/shared devices remain an attribution risk.
- Capture-time semantic risk classification can still miss sensitive/high-stakes material; the safest uncertain action is to hold, not share.
- Windows/non-Git command/root behavior is designed but not executed; Light preservation remains only a bounded future fixture.

## Checkpoint

| Found | Remaining for RES synthesis |
|---|---|
| Pairwise attacks eliminated C0/C1/C2 as unchanged primary bundles and produced one smaller composite survivor, S1/C1-R. | Synthesize evidence without copy-paste; map each HL statement to Confirmed, Challenged, or Unresolved. |
| C0 remains only a transparent degraded/manual fallback; C3 remains only the external ceiling. | State the operational boundary so fallback/ceiling are not mistaken for approved product editions/topology. |
| Schedule, shared lease, authoritative pointer, incremental-only index, broad semantic hooks, concurrent hook repair, shared `CURRENT_USER`, and shared Codex memory authority are removable/deferred. | Convert only material HL contradictions into exact proposed owner-approved wording in RES; apply none. |
| Lifecycle hooks survive as conditional validators/backstops, not semantic task or stale-session guarantees. | Preserve the four evidence lanes and local-execution gap in final verdicts. |
| Catch-up-only plus conservative hybrid state is the smallest freshness mechanism. | State next-start versus calendar-time freshness explicitly. |
| Recovery requires immutable candidates, unique runs/receipts, reconciliation, immutable accepted records, and full rebuild—not a lease. | Bound the claim to recoverability and retain real-provider testing as unresolved. |
| Identity UX survives for declared attribution; automation and privacy rules are explicit. | Separate attribution from authentication in final recommendations. |
| Append-only memory requires capture-time as well as promotion-time risk gating. | Surface this NEW finding and its effect on any automatic-memory wording. |

**Sufficiency:**
- [x] External source used? — current official Codex manual/pages and official Google Drive recovery guidance were rechecked.
- [x] Briefing gap closed? — the queued lifecycle, freshness, recovery, identity, risk, privacy, Windows/non-Git, and non-work attacks were applied.
- [x] Pairwise incompatibility checked? — D1–D17 incompatibilities and C0/C1/C2 pairwise rulings are recorded.
- [x] Surviving configurations listed? — S1/C1-R primary research survivor, S0/C0-F degraded fallback, C3 external ceiling.
- [x] Hypotheses tested? — all H1–H4 have post-Challenge research verdicts and proof gaps.
- [x] Counter-evidence sought? — trust/staleness/coverage/sync/authentication/privacy failures materially narrowed all four hypotheses.
- [x] At least two research decisions? — C-D1 through C-D8.

**Metacognitive check:** NEW findings were produced. First, the smallest viable Assisted configuration is not C1 or C2: it is C1's small lifecycle/catch-up shell plus C2's recovery evidence, after deleting schedule, lease, and pointer authority. Second, append-only safety moves the risk gate earlier than Gather/Extract emphasized—before shared candidate creation, because promotion-time review cannot retract synchronized sensitive content. Third, unknown durable tool paths prove that Stop can detect but cannot retroactively guarantee trace-first activation.

**Blocking questions:** None.

**Recommendation:** Close Challenge and authorize RES synthesis. RES should distinguish Confirmed HL, Challenged HL, Unresolved, and Recommended owner-approved changes; provide any exact proposed wording separately; and modify nothing outside `research/iter2/RES.md`.

---
Stage complete: YES
Coordinator record: Challenge accepted on 2026-08-08; RES synthesis authorized.
