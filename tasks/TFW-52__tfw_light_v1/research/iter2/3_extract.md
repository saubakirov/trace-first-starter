# Extract — "What do we NOT see?"
> **Mindset:** Analyst. The raw findings are now combined into bounded configurations; no configuration is an approved product decision.
> **Test:** "Does the configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-52](../../HL-TFW-52__tfw_light_v1.md)
> Goal: Determine the smallest reliable Assisted mechanisms for discipline, collaboration, identity, and durable memory while preserving Light's simplicity and the approved edition boundary.

## Scope and stage evidence

Extract used the accepted Briefing and Gather without changing the approved HL or any product/control file. It ran three analysis passes: assemble coherent configurations, trace their failure/recovery behavior, then seek contradictions and smaller substitutes. The four evidence lanes remain separate throughout:

1. **Documented platform support** — what current official Codex documentation says the platform does.
2. **Observed local behavior** — what this read-only session actually established on this host/repository.
3. **Unavailable or unproven behavior** — what could not be exercised or is not a current platform guarantee.
4. **Proposed adapter/configuration behavior** — research designs to be attacked in Challenge, not current Codex behavior or approved HL.

The stage rechecked the current official [Codex hooks](https://learn.chatgpt.com/docs/hooks), [scheduled tasks](https://learn.chatgpt.com/docs/automations?surface=app), and [`AGENTS.md` discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md) pages on 2026-08-08. They still document the lifecycle events used below, require the desktop app to be running for a local-project scheduled task, and define project instruction discovery from the project root (typically Git) toward `cwd`, with current-directory-only fallback when no project root is found. The stage also retains the bounded failure model from official [Google Drive recovery guidance](https://support.google.com/drive/answer/2565956?co=GENIE.Platform%3DDesktop&hl=en): incompatible edits can produce copies/recovery outcomes rather than an atomic merge.

## Configuration Space

This is a deliberately small set of coherent bundles, not the Cartesian product of all 17 Gather dimensions. A cell such as `B primary + A recovery` layers two non-contradictory alternatives and makes the fallback explicit. The tables are descriptive here; evaluation follows in Findings.

| Config | Name | Configuration intent |
|---|---|---|
| **C0** | Minimal manual contract | Deliberately simpler Assisted floor: instructions and explicit skills, catch-up only, one normal guardian, immutable inputs, full rebuild, no persistent user binding. |
| **C1** | Hooked catch-up baseline | Lifecycle hooks enforce inspectable state; catch-up runs at the next start; a device-local binding removes repeat identity questions. |
| **C2** | Recovery-first Assisted | Hooked lifecycle plus optional desktop schedule, immutable run manifests/receipts, explicit split-brain recovery, and rebuildable published views. |
| **C3** | External-coordination ceiling | External scheduler/lock/identity infrastructure supplies calendar execution, strong serialization, and authenticated provenance; retained as a complexity and claim-boundary comparator. |

### Lifecycle and authority dimensions

| Config | D1 Root/instruction authority | D2 Enforcement surface | D3 Session-start context | D4 Checkpoint trigger | D5 Completion gate |
|---|---|---|---|---|---|
| C0 | A — Codex-discovered Git/current-directory root | A — `AGENTS.md` only | C — explicit start skill/command | D — manual or task-close only | C — explicit close skill/command |
| C1 | B — explicit Assisted root marker found by ancestor walk | B — start/compact/stop hooks | B — `SessionStart` additional context | A — `PreCompact` | A — `Stop` continuation |
| C2 | B — explicit Assisted root marker found by ancestor walk | C — wider prompt/tool/session command-hook set | B — `SessionStart` additional context | C primary + A backstop — significant durable transition plus `PreCompact` | D primary + A gate — continuous task-state validation plus `Stop` continuation |
| C3 | C — configured absolute project root | D — external wrapper/scheduler around Codex | C — explicit start command through wrapper | B — periodic/time-based check | D — continuous state validation outside the model turn |

### Freshness and shared-memory dimensions

| Config | D6 Weekly execution | D7 Staleness signal | D8 Candidate identity | D9 Consolidator coordination | D10 Record publication | D11 Index publication |
|---|---|---|---|---|---|---|
| C0 | A — lazy catch-up on explicit next project start | A — `last_success_at + interval` | A — random UUID | A — designated guardian, no lease | C — immutable versioned records with supersession | C — full rebuild from accepted records |
| C1 | A — lazy catch-up in `SessionStart` | D — time plus unprocessed-input hybrid | B — UTC timestamp + stable profile + random suffix | A + B advisory — designated guardian with best-effort expiring lease | C — immutable versioned records with supersession | C — full rebuild from accepted records |
| C2 | B primary + A recovery — desktop schedule and identical start catch-up | D — time, unprocessed input, interrupted run, and stale-index hybrid | B — UTC timestamp + stable profile + random suffix | A + B advisory + C recovery — guardian, best-effort lease, unique run staging, deterministic reconciliation | C — immutable versioned records with supersession | D view + C generator — versioned snapshots/pointer, always rebuildable from accepted records |
| C3 | C — external OS scheduler | D — time plus unprocessed-input hybrid | A — random UUID | D — external lock/service | C — immutable versioned records with supersession | D — versioned index snapshots plus active pointer |

### Identity, activation, risk, and platform dimensions

| Config | D12 Identity selection | D13 Participant identity key | D14 Authorship provenance | D15 Task activation | D16 Risk handling | D17 Platform implementation |
|---|---|---|---|---|---|---|
| C0 | B — one profile auto; otherwise one question at each durable task | B — stable opaque profile ID | B — profile ID + display snapshot + source/task/time | B — explicit user command only | C — allowlist-only promotion | A — one portable runtime/contract |
| C1 | C — device-local binding after the one/many rule | B — stable opaque profile ID | B — profile ID + display snapshot + source/task/time | D — before first durable-result/file transition | B — category-based gate | B — per-OS commands/scripts |
| C2 | C — device-local binding after the one/many rule | B — stable opaque profile ID | C — profile + local device/run identity + source/task/time | D — before first durable-result/file transition | B — category-based gate | B — per-OS commands behind one state contract |
| C3 | D — OS/workspace account mapping | D — cryptographic/account identity | D — signed record/receipt | B — explicit authenticated work launch | C — allowlist-only promotion | B — per-OS wrapper/service integration |

**Novel combination exposed:** C2 intentionally combines a designated guardian, a non-authoritative best-effort lease, and an authoritative recovery path based on immutable run staging/receipts. Gather listed these D9 alternatives separately; combining them shows that reducing routine collisions and surviving split-brain are complementary controls, not competing claims that a shared-folder lease is a lock.

## Findings

### E1 — The four evidence lanes bound every configuration

| Config | Documented platform support | Observed local behavior | Unavailable or unproven | Proposed adapter/configuration behavior |
|---|---|---|---|---|
| **C0** | Codex discovers `AGENTS.md`; skills can package explicit workflows. | Root project guidance and the repository `tfw-research` skill are active in this session. | Instructions alone do not mechanically prove timely trace creation or close alignment. No arbitrary-task activation test was run. | Require an explicit start/close skill for durable work; run manual catch-up; keep ordinary conversation outside task state. |
| **C1** | `SessionStart`, `PreCompact`, and `Stop` command hooks are documented; Stop may return a continuation prompt. | The project is trusted, but no repository/global hooks are installed; current root/nested instruction paths were observed read-only. | Hook trust UX, event delivery, continuation-loop prevention, non-Git marker discovery, and actual checkpoint restoration were not exercised. | Add a marker-aware start/compact/stop contract; inspect file-state invariants; use Stop to continue only when an active task is inconsistent. |
| **C2** | The wider command-hook events and desktop scheduled tasks are documented, subject to platform/trust/runtime constraints. | Same local evidence as C1; no schedule, hook, or real sync-provider execution was observed. | Closed-app desktop execution, strict shared-folder exclusion, real Drive ordering, atomic cross-device publication, and semantic command-hook classification are not available/proven. | Run the same idempotent consolidator from schedule or start; treat lease as advisory; make manifests, receipts, reconciliation, and rebuild authoritative. |
| **C3** | Codex can be wrapped by external tools, but external locking, calendar execution, account authentication, and signing are not Codex lifecycle guarantees. | No external service, scheduler, signing identity, or managed lock was configured or inspected. | Operational cost, portability, deployment, account recovery, and whether this belongs in Assisted are all unproven. | A separate service serializes consolidation, schedules it while Codex is closed, and authenticates/signed-attributes the actor. |

This lane separation prevents four invalid substitutions:

- a documented event name is not an observed local callback;
- an observed instruction chain is not a lifecycle enforcement guarantee;
- a proposed marker/receipt/binding protocol is not built-in Codex behavior;
- a useful declaration of profile identity is not authentication of a person.

### E2 — H1 lifecycle contract: what each mechanism can actually enforce

| Assisted invariant | Documented Codex surface | Inspectable condition | Boundary / fallback |
|---|---|---|---|
| Correct project context at run start | Root-to-`cwd` `AGENTS.md` discovery; `SessionStart` context | Resolved root marker, project ID, active-task pointer or `none`, due-memory state | `AGENTS.md` is loaded once per run. Marker walk is proposed behavior. Wrong/missing marker must fail closed before durable work, not guess another root. |
| Task context when a real task begins | No semantic task-start event | Active task ID exists before a durable result mutation | C0 requires an explicit command. C1/C2 rely on agent instruction plus deterministic write-boundary checks where available. A session start never creates a task by itself. |
| Pre-compaction continuity | `PreCompact`, followed by compact start/post events | Active trace already contains goal, owner, status, last verified result, and next action | The hook can persist/check state but cannot invent a semantically correct checkpoint. C0 instead relies on continuous/manual trace updates. |
| Completion/status alignment | `Stop` continuation with loop flag | Active trace status, owner, result/evidence links, candidate receipts, and close state agree | `SessionEnd` is advisory, not a gate. Stop repair must be idempotent and apply only to an active task. C0 uses explicit close and cannot force compliance. |
| Shared memory refresh | `SessionStart`; optionally desktop scheduled task | Staleness predicates and completed consolidation receipt validate | The consolidator is proposed. Local schedules need the app running; catch-up is the universal in-Codex fallback. |
| Personal convenience memory | Local Codex memories | None required for shared authority | Memories are generated local state and remain optional; they cannot be the shared source of truth or required recovery path. |

The lifecycle configurations therefore form a real strength gradient:

- **C0** can be sufficient for disciplined low-frequency use, but its guarantee is social/instructional. It is the deliberately simpler counterexample to a claim that three hooks are always necessary.
- **C1** adds enforcement for file-observable invariants at start, compact, and Stop. It cannot deterministically decide whether a prompt is a substantive task.
- **C2** adds more observation points and continuous state checks, but command-only hooks still cannot provide a reliable semantic classifier. Its value is earlier detection and better recovery, not semantic omniscience.
- **C3** can make launch and completion externally explicit, but moves core behavior outside the intended small Assisted runtime.

No configuration can make H1 unconditional from the current evidence. C1/C2 are plausible implementations of the event set, conditional on installation, trust, correct-root resolution, idempotent handlers, and executed fixture evidence.

### E3 — Task activation and non-work behavior are independent of session lifecycle

The proposed durable-work boundary is the earliest point at which the assistant is about to create/change a product result, task trace, shared candidate, ownership/status state, or external side effect for a user goal. Reading, explaining, orientation, casual ideation, and ordinary non-work conversation do not cross it.

| Conversation state | C0 Minimal | C1 Hooked baseline | C2 Recovery-first | C3 External ceiling |
|---|---|---|---|---|
| Open project / resume session | Load instructions only; no task | Resolve marker/context and run due catch-up; `active_task = none` is valid | Same, plus recover incomplete consolidation; no participant identity needed for an automation run | Wrapper opens in conversation or authenticated-work mode; conversation mode has no task |
| Read, explain, answer, orientation | No task, owner, identity question, or candidate | Same | Same | Same |
| User explicitly starts durable work | User invokes start skill and selects identity if needed | Agent creates task before first durable transition; binding may select identity | Same; deterministic write guard may reject known result writes if task/identity state is absent | Authenticated launch declares task and actor |
| Prompt looks substantive but remains advisory | No task until explicit start; risk of under-capture is accepted | No task until a durable boundary is actually intended | Same | Conversation mode remains task-free |
| First durable write is attempted with no task | Instructions require stopping and asking to start | Handler/model establishes task before write; Stop is only a late repair if earlier handling missed | Guard blocks known task/result publication, creates/requests activation, then retries | Wrapper rejects write outside authenticated work mode |
| Stop with no active task | Silent success; no synthetic task | Silent success | Silent success | Silent success |
| Stop with active inconsistent task | Explicit close skill must repair | Stop returns one continuation to align trace/status/owner | Continuous checks should have repaired; Stop is final idempotent gate | External validator rejects incomplete close |

Two consequences are important:

1. `SessionStart` may refresh project memory without creating a user task. A consolidation receipt should identify the automation/run identity, not borrow a participant profile or a shared `CURRENT_USER`.
2. A tool/file transition is only a deterministic proxy for task intent. It can guard known durable paths, but it cannot classify every meaningful conversation or every tool surface. Challenge must attack false positives, missing tool coverage, and read-only commands that happen to write caches.

Task-local alignment should inspect only the declared active task. The minimum invariant set is: one active task or none; stable owner profile or explicit pending owner; trace/status/result links agree; authored candidates reference the same stable profile; another participant's task is never rewritten without an explicit ownership transfer. This keeps the shared Task Board out of the hot path and honors the owner lock against broad topology redesign.

### E4 — H2 requires two different freshness claims

Define two separate service boundaries:

- **Next-start freshness:** before the first shared-memory consumer or durable task after reopening the project, an overdue/dirty/incomplete consolidation has completed successfully or the user is told that memory is stale.
- **Calendar-time freshness:** consolidation has completed by a wall-clock deadline even if nobody starts Codex or opens the project afterward.

They are not synonyms.

| Environment state | C0 explicit catch-up | C1 start-hook catch-up | C2 desktop schedule + start recovery | C3 external OS schedule |
|---|---|---|---|---|
| Computer on; desktop app/project open | Next-start fresh after explicit run | Next-start fresh after automatic pre-use barrier | Best-effort calendar run plus next-start verification | Calendar run can execute independently of Codex |
| Computer on; desktop app closed | No run until next start | No run until next start | Desktop local schedule does not run; next start catches up | Can run if the external runtime, credentials, and local folder are available |
| Computer asleep/off | No run | No run | No run | No local run until wake; scheduler needs missed-run recovery |
| Long unopened interval | Staleness unbounded until explicit start | Calendar staleness unbounded; next-start freshness remains achievable | Schedule helps only during app-running windows; start closes missed gaps | Closest to calendar freshness, but still bounded by machine/runtime availability |
| Simultaneous scheduled and start trigger | N/A | N/A | Both invoke the same idempotent run protocol; overlap becomes detectable split-brain, not a second implementation | External serialization may prevent overlap; receipts remain useful for audit/recovery |

The smallest useful staleness predicate is not time alone:

```text
needs_run = interval_due
         OR unreceipted_candidate_ids_exist
         OR incomplete_run_manifest_exists
         OR active_index_digest != accepted_records_digest
```

The first term supports weekly housekeeping; the other terms catch new inputs, crash recovery, and stale derived state. Clock rollback or missing/corrupt timestamps must not clear the other terms. Success means a valid completion receipt and a verifiable rebuilt view, not merely setting `last_attempt_at`.

The quiet interaction contract is also configuration-independent:

- routine success or nothing due: zero questions; at most one terse status line;
- overdue work at project start: run before first shared-memory consumption, then continue without asking;
- ambiguous, contradictory, sensitive, or high-stakes candidates: retain them and ask at most one compact batch when the answer is needed;
- unavailable/corrupt recovery state: report stale memory once and continue only if the requested work does not require freshness.

Thus H2 is supportable only under the next-start definition. Literal calendar-time similarity is false during a closed interval; C3 is the only configuration that can run while the desktop app is closed, and even it cannot run on a powered-off machine.

### E5 — H3 recovery protocol separates six controls that a “one consolidator” phrase hides

| Control | Purpose | Authority | Failure boundary |
|---|---|---|---|
| **Designated guardian** | One named person/device normally initiates consolidation | Social/operational routing | Does not prevent an accidental, offline, or scheduled second run. |
| **Best-effort lease** | Reduce ordinary overlap when all clients see fresh shared state | Advisory optimization only | Not strict exclusion in a delayed/offline synchronized folder; two holders may both believe they own it. A stale lease can be ignored only by starting a distinct recoverable run, never by overwriting history. |
| **Immutable staging** | Give every run a unique namespace and declared input set | Durable run evidence | An interrupted run may leave partial output; it must not become accepted merely because files exist. |
| **Immutable receipts** | Record started/completed/reconciled states, input IDs/digest, output IDs/digest, actor type, and times | Completion/audit evidence | A missing completion receipt means incomplete. Conflicting receipts trigger comparison; no receipt deletes inputs. |
| **Split-brain detection and reconciliation** | Detect overlapping runs and converge identical results or preserve divergent claims | Deterministic recovery rule | Cannot safely “last writer wins” over semantic differences. Divergence must become an explicit conflict or one batched human decision. |
| **Rebuild** | Recreate navigation/index state from accepted records and supersession metadata | Derived-view recovery | A missing/conflicted pointer or index is an availability issue, not loss of primary candidates/records. |

#### Proposed C2 run state machine

```text
DISCOVER
  -> parse every candidate payload (filename is only a locator)
  -> deduplicate physical copies by candidate_id
  -> create immutable run_id + STARTED manifest(input ids + digest)
  -> stage proposed immutable records/source mappings under run_id
  -> validate risk gates and deterministic record/source digests
  -> write COMPLETED receipt(output ids + digest)
  -> compare overlapping completed/incomplete manifests
       identical semantic outputs -> record duplicate-run reconciliation
       divergent outputs          -> publish conflict state; no silent winner
  -> rebuild versioned index from accepted record/supersession state
  -> validate snapshot digest; update/reconcile advisory active pointer
```

Primary candidates are never removed merely because a run started. A candidate becomes accounted for only through an immutable source mapping in a completed/reconciled receipt. Semantic duplicates retain all candidate IDs. Contradictory claims remain separate or become an explicit conflict record; deduplication must not erase disagreement.

#### Recovery cases across configurations

| Failure case | C0 | C1 | C2 | C3 |
|---|---|---|---|---|
| Concurrent candidate writes | UUIDs avoid shared allocation; guardian later scans all payloads | Timestamp/profile/random IDs; same payload scan | Same, plus per-run manifests prove the scanned set | Same primary-input discipline remains prudent even with service coordination |
| Duplicate semantic candidates | Manual/deterministic normalization; retain both source IDs | Same | Same, with receipt mappings | Service may centralize dedupe but must retain sources |
| Two consolidators | Possible; no exclusion; manual reconciliation | Advisory lease may reduce but cannot prevent; immutable records expose duplicates | Expected failure mode: unique runs, overlap detector, deterministic reconciliation | External lock should serialize, but receipts detect lock/service defects |
| Drive conflict-copy name | Scan schema/payload, not strict filename pattern | Same | Same; invalid payload is held/reported, not silently dropped | Connector/service still must account for conflict copies |
| Interrupted consolidation | Retained candidates permit rerun; manual evidence is weaker | Missing completion receipt triggers rerun and full rebuild | Started manifest plus staged outputs are incomplete until completed/reconciled; rerun is idempotent | Transaction/service may help, but receipt-based recovery remains auditable |
| Stale/false lease owner | Not applicable | New run may proceed after policy TTL, but cannot claim exclusive ownership | New unique run proceeds; overlapping receipts make split-brain visible | External lock defines expiry/fencing, outside the shared folder |
| Corrupt/missing index | Full rebuild | Full rebuild | Validate digest; rebuild versioned snapshot; pointer conflicts are not record conflicts | Rebuild from accepted records |

C0 is the simplest viable shared-memory configuration because it needs no lease or incremental index. Its weakness is human/manual completion evidence, not candidate uniqueness. C2 is the stronger recovery-first configuration because it assumes overlap can happen and makes it detectable/reconcilable. It does **not** strengthen a Drive lease into strict exclusion.

The in-memory Gather fixture supports the structural direction: random-suffixed IDs avoided observed allocation collisions; the shared counter collided; both offline lease claimants believed they acquired the lease; schema parsing recovered more conflict-copy candidates than strict filename matching; and retained inputs plus deterministic IDs recovered an interrupted run. It does not prove real-provider ordering, crash atomicity, or knowledge-loss prevention in production.

### E6 — H4 identity is a low-friction declared-attribution state machine

Identity selection occurs only when a durable action needs ownership/authorship, not at project open or during non-work conversation.

| Profile/binding state | Selection behavior | Shared provenance behavior | Authentication boundary |
|---|---|---|---|
| Zero valid profiles | Block attributed durable publication; offer profile setup or explicit pending/unattributed state | Never borrow a previous/shared identity | No actor is authenticated |
| Exactly one valid profile | Auto-select it; do not create/read a shared current-user file | Record stable profile ID and current display snapshot | Declared project identity only |
| Multiple profiles + valid local binding | Select bound stable profile ID without asking | Record stable ID; resolve current display name from profile | Local binding says “this device normally declares X,” not “X is physically present” |
| Multiple profiles + new device/no binding | Ask one short profile-choice question at first attribution-required transition; optionally store locally | Record selected profile | Answer is a declaration, not credential verification |
| Binding points to deleted/missing profile | Treat as stale; ask once; never silently fall back | Historical records keep the old stable ID/display snapshot | Staleness handling does not authenticate replacement |
| Participant display name changed | Keep binding by stable opaque ID; show new current name while historical snapshots remain | Preserve provenance across rename | Rename does not rotate identity key |
| Unknown user only reads/chats | No question, no task, no authorship | No candidate or owner record | Authentication not needed because no attribution occurs |
| Unknown user attempts durable work | Ask once or hold work explicitly pending/unattributed; never use another person's binding silently | Provenance must expose pending/declared status | Cannot claim verified authorship |

The device-local binding should contain only a stable project identifier → stable profile identifier relation and remain outside the synchronized folder. It must not contain a shared `CURRENT_USER`, secret, sensitive biography, or mutable display handle. Copying that local file to another device would copy a preference, not proof of identity; Challenge must test this privacy/impersonation case.

Minimum shared provenance for C0–C2 is:

- stable declared profile ID;
- display-name snapshot for human readability;
- task ID and source/candidate IDs;
- authored/consolidated timestamps;
- automation versus participant actor type;
- in C2, non-secret local device/run identifier and receipt ID for diagnosing collisions.

This supports traceability and honest authorship attribution at Assisted's friction target. Authentication, non-repudiation, and proof of the physical operator require a stronger account/signature system such as C3 and must not be inferred from C0–C2.

### E7 — Risk gates and quiet weekly behavior are compatible only with “hold, do not guess”

| Category | C0 allowlist behavior | C1/C2 category-gate behavior | Required interaction |
|---|---|---|---|
| Routine project fact, explicit decision, stable format preference | May promote only if explicitly allowlisted; otherwise retain candidate | Quietly consolidate when provenance and confidence rules pass | None on success |
| Ambiguous or contradictory conclusion | Retain candidates; manual close | Create explicit unresolved/conflict state | One compact batch only when resolution matters |
| Health/medical, personal data, minors, sensitive biography | Do not auto-promote to shared record | Redact/pointer/private-only or require explicit opt-in | Ask before shared publication; do not repeat sensitive detail unnecessarily |
| Legal dispute, high-stakes financial/safety conclusion | Keep sourced unresolved claim, not a project fact | Require source and human-confirmed status | Ask before promotion/decision reliance |
| Password, token, private key, secret | Reject shared storage; record only safe remediation metadata | Same, plus deterministic pattern check where possible | Terse warning; advise safe-store/rotation as appropriate |
| Ordinary non-work conversation | No task/candidate/identity | No task/candidate/identity | None |

Command hooks can inspect structure and obvious secret patterns. They cannot reliably understand every medical, legal, financial, or personal context. The model must hold uncertain material, and Stop can validate that prohibited categories were not published—not certify semantic safety by itself.

### E8 — Compatibility and contradiction matrix

| Combination | Result | Reason |
|---|---|---|
| Correct-root instruction loading + non-Git synchronized folder + Git-root-only handler | **Contradictory** | The documented fallback may be only `cwd`; a Git-only resolver cannot establish the intended Assisted authority. |
| `SessionStart` + “every prompt is a task” | **Contradictory to no-task behavior** | A session lifecycle event does not imply durable work and would create noise from ordinary conversation. |
| `PreCompact` + no already-explicit active task state | **Weak/insufficient** | A command hook can checkpoint inspectable files; it cannot reconstruct missing semantic task state reliably. |
| `Stop` + `SessionEnd` as interchangeable completion gates | **Contradictory** | Stop may continue the turn; SessionEnd is advisory and may be delayed. |
| Desktop local schedule + Codex app closed | **Unsupported** | Official scheduled-task guidance requires the app running for local files. |
| Web schedule + direct local synchronized-folder mutation | **Unsupported** | Hosted execution has no direct local project-folder access without another connected storage/runtime layer. |
| Shared expiring lease + strict single consolidator | **Contradicted by fixture/model** | Offline/delayed claimants can both see no lease and proceed. |
| Two possible consolidators + mutable in-place only record/index | **Unsafe** | Conflict copies or overwrite order can hide a result; no immutable evidence defines recovery. |
| Unique candidate filenames + semantic deduplication “solved” | **False equivalence** | Unique physical identity does not detect duplicate meaning or contradictions. |
| Device-local profile binding + authenticated authorship | **False equivalence** | A preference mapping does not verify the physical actor. |
| Local Codex memories + shared project authority | **Incompatible boundary** | Generated local memory is neither synchronized primary evidence nor deterministic recovery state. |
| C2 lifecycle + C2 recovery protocol | **Compatible** | Earlier/duplicate triggers can invoke the same idempotent run and detect overlap through immutable receipts. |
| C0 explicit lifecycle + immutable candidates/full rebuild | **Compatible minimal alternative** | It sacrifices automatic enforcement/scheduling while retaining a small recoverable memory core. |

### E9 — Windows, cross-platform, and bounded root/Light preservation

- C1/C2 require an explicit platform-neutral state contract plus per-OS launch commands. Current hooks support a Windows command override, but the actual commands and runtimes remain untested locally.
- Hook commands run from session `cwd`; handlers must resolve an ancestor marker or fail closed. Relative paths and `git rev-parse` alone are insufficient for a non-Git synchronized folder.
- Local filesystem rename/replace behavior must not be advertised as atomic synchronization. C2's safety comes from immutable evidence and recovery, not a cross-device atomic-rename assumption.
- Candidate/receipt payload IDs are authoritative. Paths, separators, reserved names, casing, line endings, and timestamps require explicit normalization across Windows/macOS/Linux.
- The existing nested TFW-51 prototype remains only a wrong-root/source-versus-runtime validation case: inside this repository it inherits parent guidance; a standalone non-Git copy may not. Nothing in C0–C3 selects X1/X2/X3 or redesigns edition topology.
- Light → Assisted preservation is likewise bounded: a validation fixture should confirm that Light content remains intact while an Assisted marker/state layer is recognized. It cannot be used in this research to choose packaging, migration, or source layout.

### E10 — Configuration comparison and simpler alternatives

| Config | Added moving parts | Principal strength | Principal limitation | Carry into Challenge as |
|---|---|---|---|---|
| **C0 Minimal manual contract** | Explicit start/close skill; manual catch-up; guardian; immutable records; full rebuild | Lowest lifecycle/scheduler/privacy complexity; demonstrates that recovery does not require a lease | Cannot reliably enforce start/checkpoint/close when users skip the workflow; only next-explicit-start freshness | Deliberately simpler counterexample |
| **C1 Hooked catch-up baseline** | Three lifecycle hooks; marker resolver; local binding; receipts; full rebuild | Mechanically checks file-state invariants and achieves quiet next-start freshness | Trust/install dependency; no calendar freshness; semantic activation remains agent-mediated | Smallest automatic Assisted candidate |
| **C2 Recovery-first Assisted** | Wider hooks; optional desktop schedule; run manifests/receipts; split-brain reconciliation; versioned index | Best bounded recovery for 2–3 asynchronous writers without claiming strict exclusion | More state and testing; schedule still cannot run closed; actual Drive behavior untested | Stronger recovery-first candidate |
| **C3 External-coordination ceiling** | External runtime/scheduler/lock, account identity/signing, operations | Calendar execution while Codex is closed and genuine authentication/serialization are possible | Materially exceeds minimal local Assisted complexity; external availability/credentials become dependencies | Ceiling/counterfactual, not a default candidate |

Other simpler alternatives remain live for Challenge:

- C0 with no persistent binding: ask once per durable task when multiple profiles exist.
- C1 without `PreCompact`: maintain trace continuously and rely on Stop; acceptable only if compaction cannot lose unpersisted state.
- C1 with no lease at all: one guardian plus immutable receipts and full rebuild may be clearer than advisory lease complexity.
- C2 without desktop scheduling: start catch-up alone preserves next-start freshness and removes a duplicate trigger.
- Candidate/pointer-only memory: never auto-promote shared records; safest for sensitive projects but delivers less quiet memory value.

### E11 — Extract hypothesis tests

These are stage orientations for Challenge, not final RES verdicts.

| Hypothesis | Extract orientation | Configurations that support the bounded form | Counter-evidence / unresolved proof |
|---|---|---|---|
| **H1** — `SessionStart` + pre-compact + `Stop` reliably load context, maintain trace, and align status quietly | **Conditionally plausible, not yet demonstrated** | C1/C2 map each event to inspectable invariants and protect no-task sessions | Hooks are absent/unexecuted locally; trust/root/handler failures remain; no semantic task-start event; C0 may be sufficient for some Assisted uses |
| **H2** — lazy weekly catch-up gives practically similar freshness to a schedule without Codex remaining running | **Supported only for next-start freshness; challenged for calendar-time freshness** | C1 and C2 start recovery establish an explicit pre-consumption barrier | Nothing runs while closed; delay is unbounded; only C3 can operate closed and it still needs an awake machine/runtime |
| **H3** — unique append-only candidates + one consolidator + derived index prevent knowledge loss for 2–3 Drive-folder participants | **Recovery-first form is plausible; literal prevention/single-writer form remains too strong** | C2 layers guardian, advisory lease, immutable staging/receipts, split-brain reconciliation, and rebuild; C0 is a simpler guardian/rebuild baseline | Lease is not exclusion; real Drive ordering/atomicity not tested; divergent semantic reconciliation and corrupt receipts remain to attack |
| **H4** — one profile auto; multiple profiles bind/ask once; no shared `CURRENT_USER` reliably establishes authorship | **Supported for low-friction declared attribution; challenged for authentication** | C1/C2 stable IDs + local binding + provenance cover new/stale/renamed identity states | New device/unknown actor still asks; copied/shared devices permit false declaration; only C3 adds authenticating infrastructure |

## Extract Decisions (research-process only)

| # | Decision | Rationale |
|---|---|---|
| **E-D1** | Carry C0, C1, and C2 into Challenge; retain C3 only as a ceiling/counterfactual. | This preserves a deliberately simpler option, a small automatic baseline, and a stronger recovery-first option without silently selecting product architecture. |
| **E-D2** | Treat five properties as viability invariants across C0–C2: ordinary conversations create no task; primary candidates are immutable and uniquely identified in payload; a shared lease is never strict exclusion; the index is derived/rebuildable; identity is declared unless separately authenticated. | These properties are supported by evidence/counter-evidence and prevent the most serious category errors. |
| **E-D3** | Test H2 under two named metrics: next-start freshness and calendar-time freshness. | The same word “freshness” otherwise hides the closed-app interval and could falsely confirm H2. |
| **E-D4** | Treat task activation as a state transition before durable work, never as a side effect of `SessionStart`; allow `active_task = none`. | This is necessary for non-work conversations and prevents weekly maintenance from borrowing a participant owner. |
| **E-D5** | In Challenge, attack C2 as a recovery protocol, not as a lock protocol. | Guardian and advisory lease reduce routine overlap; immutable staging/receipts, detection, reconciliation, and rebuild carry safety after overlap occurs. |
| **E-D6** | Treat H4's C0–C2 outcome as attribution/provenance only; reserve “authenticated authorship” for C3-class identity infrastructure. | Device-local binding reduces questions but supplies no credential or non-repudiation proof. |
| **E-D7** | Do not formulate or apply any HL change in Extract. Challenge will determine whether the bounded contradictions require an exact owner-approved wording diff in final RES. | The master HL and plan are immutable in this Researcher session; configurations are research artifacts only. |

## Counter-evidence queued for Challenge

- stale session whose `AGENTS.md` chain predates an Assisted update;
- wrong/nested root, absent marker, untrusted/changed hook, duplicate hook event, missing compaction callback, and Stop continuation loop;
- ordinary question that resembles a task and durable work that begins without a recognized file transition;
- no candidates but interval due; candidates dirty but timestamp fresh; corrupt/missing clock state; simultaneous schedule/start; machine sleep and long absence;
- two offline consolidators with the same/different semantic result; false/stale leases; duplicate completion receipts; partial record publication; conflict-copy filenames; pointer/index conflicts; corrupt accepted record; rebuild after interruption;
- one/many/zero profiles, new/shared/copied device, stale/deleted/renamed profile, privacy leakage, automation receipt attribution, and disputed physical authorship;
- Windows command resolution, paths/case/reserved names, unavailable runtimes, and a standalone non-Git Light → Assisted validation fixture without turning it into topology research.

## Checkpoint

| Found | Remaining for Challenge |
|---|---|
| Four coherent H1–H4 bundles now expose a manual minimum, a hooked baseline, a recovery-first design, and an external ceiling. | Attack each bundle under the queued failure matrix; eliminate unnecessary mechanisms and identify the smallest surviving recommendation. |
| Lifecycle events map to file-observable invariants, while semantic task activation remains a separate state transition. | Test stale/wrong-root, missing/duplicate hook, pre-compact, premature Stop, and false task/no-task scenarios. |
| H2 is formally split into next-start and calendar-time freshness with one hybrid staleness predicate and a quiet interaction contract. | Test clock corruption, sleep/closed-app intervals, simultaneous triggers, failed catch-up, and first-consumer behavior. |
| H3 now distinguishes guardian, advisory lease, immutable staging/receipts, split-brain detection, reconciliation, and rebuild. | Attack divergent two-consolidator outputs and incomplete/corrupt receipts; no real Drive claims may be inferred. |
| H4 now separates low-friction declared attribution from authentication and keeps bindings device-local. | Attack copied/shared devices, unknown actors, stale/renamed/deleted profiles, privacy, and authorship disputes. |
| Root discovery and Light preservation are explicitly bounded validation scenarios. | Validate only those scenarios; do not choose topology or modify the approved HL. |

**Sufficiency:**
- [x] External source used? — current official Codex lifecycle, schedule, and `AGENTS.md` documentation was rechecked in this stage; the official Drive failure boundary remains cited.
- [x] Briefing gap closed? — H1–H4 now have coherent end-to-end configurations rather than disconnected mechanisms.
- [x] Configuration Space built from Gather dimensions? — all D1–D17 appear, including layered non-contradictory alternatives.
- [x] Hypotheses tested? — all four have bounded Extract orientations and explicit counter-evidence.
- [x] Simpler alternative present? — C0 and the reduced alternatives under E10.
- [x] Recovery-first alternative present? — C2, without treating a Drive lease as strict exclusion.
- [x] Four evidence lanes preserved? — E1 and the later contract boundaries keep documented, observed, unproven, and proposed behavior distinct.

**Metacognitive check:** NEW structure was produced. The principal unseen combination is not “a better lease,” but guardian + advisory collision reduction + recovery that assumes two runs can happen. A second important structure is that task activation, consolidation actor identity, and participant attribution are three different state transitions; session start cannot safely stand in for any of them.

**Blocking questions:** None.

**Recommendation:** Close Extract and authorize Challenge. Challenge should attempt to falsify C0–C2, use C3 only to expose which guarantees require external infrastructure, and make no HL or product changes.

---
Stage complete: YES
Coordinator record: Extract accepted on 2026-08-08; Challenge authorized.
