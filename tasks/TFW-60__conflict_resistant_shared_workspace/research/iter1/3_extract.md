# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md)
> Goal: Make concurrent human and agent work in a synchronized TFW workspace conflict-resistant by moving normal lifecycle state and coordination to stable task-local, single-writer surfaces while retaining discoverability and Git provenance.

## Configuration Space

All configurations obey the frozen Phase-A boundary: task-local authority, stable task directory, one normal state/journal writer, ordinary files, no database/service, and non-authoritative project views. The two tables are one configuration space split for readability; their headers preserve Gather's D1-D14 dimensions.

### Control, ownership and discovery dimensions

| Config | D1. Catalogue persistence | D2. Catalogue authority | D3. Status carrier | D4. Human view | D5. Transition write | D9. Ownership | D10. Edition compatibility | D14. Cold-start entry |
|--------|---------------------------|-------------------------|--------------------|----------------|----------------------|---------------|----------------------------|-----------------------|
| **C1 — structured split** | permanent root router + generated catalogue | task-local control | strict `status.yaml` | generated catalogue plus deliberately simple YAML | update one scalar snapshot | task steward owns control and journal | same schema and serialization | README names fixed glob and optional query command |
| **C2 — human split** | permanent root router + generated catalogue | task-local control | bounded `STATUS.md` frontmatter | the control file itself plus catalogue | update frontmatter snapshot | task steward owns control and journal | same semantic/schema contract; Markdown serialization | README → catalogue → fixed `STATUS.md` |
| **C3 — structural markers** | permanent root router; catalogue generated per read | task-local marker set | one status marker in a fixed `state/` directory | generated catalogue; marker name visible in file browser | create new marker, then remove old marker | task steward owns marker set and events | shared semantics, edition-specific rendering allowed | README → stable task folder → `state/` |
| **C4 — event-derived** | permanent root router + generated live catalogue | task-local journal; snapshot is projection | status inferred from last valid transition | generated `STATUS.md`/catalogue | append one transition event | task steward owns journal; generator owns projections | same event/state semantics; projection may differ | README names journal scan/query; projection is convenience |
| **C5 — combined bounded document** | permanent root router + generated catalogue | one task-local control document | bounded `STATUS.md` frontmatter | the same document | rewrite snapshot and append one event in one file | task steward owns whole document | same schema and Markdown serialization | README → fixed `STATUS.md`; no command required |

### Journal, transport and freshness dimensions

| Config | D6. Journal storage | D7. Journal breadth | D8. Journal retention | D11. Git topology | D12. Parallel isolation | D13. Catalogue freshness |
|--------|---------------------|---------------------|-----------------------|-------------------|-------------------------|--------------------------|
| **C1** | strict Markdown event records separate from YAML | material coordination only | numbered append-only segments retained with task | synced work files; local Git metadata; declared landing owner | disjoint task paths; role-owned same-task artifacts | rebuild per read; cached view carries source revision/time |
| **C2** | JSONL separate from `STATUS.md` | same closed coordination grammar | numbered immutable segments retained; head referenced by status | each Git-capable participant may have a local external Git directory/index; one landing owner per commit | disjoint task paths | explicit refresh; stale cache visibly labelled |
| **C3** | one immutable file per coordination event | same closed grammar | retain event files; terminal view derives outcome only | sync-only peers plus one local landing repository | different tasks use different folders; one writer for marker set | scan marker/event files on demand |
| **C4** | segmented JSONL is both history and state source | same closed grammar | sealed segments + active head; all retained | local Git metadata; task-scoped landing | journal single writer; other roles own artifacts | event-triggered or per-read projection; stale projection never resumes work |
| **C5** | event section in the status document | same closed grammar | hard document budget; task split or explicit exception before overflow | sync-only peers plus one landing owner | whole control file is one writer; role outputs disjoint | catalogue rebuild per read |

Configurations not present in the Briefing include C1's strict YAML plus a human-readable reference journal, C3's immutable-per-event form, and C4's file-only event-derived state. They are not selections; Challenge must attack their failure behavior.

### Structural trade-offs carried to Challenge

| Config | What it makes cheap | What it makes expensive or ambiguous |
|--------|---------------------|--------------------------------------|
| C1 | deterministic current-state parsing; snapshot remains small; journal is readable | non-technical editing of YAML; two-file event/snapshot ordering; generated human view matters more |
| C2 | direct human inspection; frontmatter can remain deterministic | Markdown body-growth pressure; JSONL journal is opaque without a view; frontmatter/body disagreement must be impossible or detected |
| C3 | visually structural status; event writers never rewrite an old event | marker create/delete is not one stable carrier path; offline sync can expose zero or two markers; many small files |
| C4 | one append operation is the state transition; corrections are explicit compensating events | resume requires a parser and last-valid-event rule; projection absence/staleness is user-visible; long-history scan and recovery |
| C5 | one file answers human cold start; no cross-file event/snapshot lag | snapshot rewrite and journal append touch the same file; one conflicted copy affects both; segmentation complicates the fixed entry path |

## Findings

### E1. Minimal logical task-state contract

The contract is logical before it is YAML, Markdown, markers or JSONL. Every field below has a named consumer; fields without one are excluded.

| Field | Required rule | Normal writer | Named consumer |
|-------|---------------|---------------|----------------|
| `schema_version` | closed version identifier | task creator, then immutable | validator/migration |
| `task_id` | stable ID; must match task-folder identity | task creator, then immutable | catalogue, commit attribution, links |
| `goal_summary` | one discovery sentence, bounded; not a second HL contract | task steward | human/agent catalogue |
| `value_summary` | one outcome/value sentence, bounded | task steward | human/agent prioritization |
| `goal_ref` | task-relative or repo-relative canonical source, when one exists | task steward | reader needing full scope |
| `lifecycle` | common closed value: `new`, `active`, `waiting`, `blocked`, `terminal` | task steward | resume, catalogue, workflow routing |
| `workflow_stage` | shared stage vocabulary or declared edition extension | task steward | Full workflow routing; optional Assisted detail |
| `status_since` | RFC 3339 timestamp of current lifecycle/stage | task steward | stale-work and resume display |
| `waiting_on` | null or bounded kind + reference; required for `waiting`/`blocked` | task steward | human/agent next-step discovery |
| `next_action` | bounded imperative, not a plan narrative | task steward | cold-start resume |
| `next_ref` | canonical artifact/gate path or anchor | task steward | resume without copied content |
| `terminal_outcome` | null except terminal; `done` or `rejected` in the shared kernel | task steward after the controlling verdict | catalogue and release |
| `terminal_ref` | required with terminal outcome; points to REVIEW, owner ruling, post-mortem or other authority | task steward | human outcome inspection |
| `state_owner` | persistent person/agent identity that alone changes control/journal | task creator; reassignment itself is journaled by current owner | write-boundary enforcement |
| `ownership_profile` | versioned edition profile defining file-pattern → role | task creator/coordinator | same-task collision prevention |
| `roles` | current identities for Coordinator/Researcher/Executor/Reviewer or Assisted owner | task steward | dispatch and file ownership |
| `last_event_id` | ID of the event reflected in the snapshot | task steward | two-file reconciliation and resume |
| `journal_head` | current segment/path, if segmented | task steward | bounded history loading |
| `updated_at` | time snapshot was last written | task steward | cache/view freshness |

Not admitted: free-form notes, detailed criteria, findings, test evidence, debt, knowledge, chat transcripts, copied review verdicts, or a manually maintained list of which standard artifacts exist. Those already have HL/RES/TS/ONB/RF/REVIEW/evidence homes or can be discovered from stable paths.

`goal_summary` and `value_summary` own catalogue wording only. They point to the HL when it exists and cannot amend its frozen contract. This satisfies discovery without turning the control carrier into a shadow HL.

### E2. Shared lifecycle semantics versus edition representation

One coarse lifecycle plus an optional stage separates universal task meaning from Full's detailed process.

| Shared semantic state | Full mapping | Assisted mapping | Representation that may vary |
|-----------------------|--------------|------------------|------------------------------|
| `new` | TODO/proposal/inception before active workflow | `work/new` | YAML enum, Markdown frontmatter, or marker |
| `active` + `research` | RES work | — | Full exposes the stage; Assisted may omit unused stages |
| `active` + `specification` | HL/TS planning work | — | stage detail may be edition-specific but cannot redefine lifecycle |
| `active` + `execution` | ONB/execution/RF work | `doing` | same task meaning, different workflow artifacts |
| `active` + `review` | review/knowledge gate in progress | `review` | review artifacts and gates differ |
| `waiting` | approval gate, coordinator answer, frozen policy | owner/human answer required | `waiting_on.kind` can carry `approval`, `owner`, `policy` |
| `blocked` | dependency/capability prevents progress | `blocked` | must name a resolvable cause/ref; not a decorative enum |
| `terminal` + `done` | DONE | `done` | terminal outcome/reference common |
| `terminal` + `rejected` | REJECTED trace preserved | rejected/cancelled task if supported | Assisted must preserve trace rather than delete/move away |

Shared across editions: stable identity, goal/value summaries, lifecycle, terminal outcome, state owner, role identities, next action/reference, event grammar, and stable task directory. Edition-specific: ID-generation policy, supported workflow-stage subset, artifact ownership profile, adapter/agent transport, Git participation, and presentation serialization. An edition extension may add fields under its namespace but cannot change shared field meanings.

This is narrower than H4's strongest form. Shared semantics do not require Assisted to ship Full's role artifact set or Git workflow, and they do not require Full to use Assisted's timestamp ID.

### E3. One-writer ownership map

The state owner is a capability, not necessarily a product persona. In Full it is the Coordinator; in Assisted it is the task owner/steward. Reassignment requires the outgoing owner (or explicit recovery rule) to append an ownership event before the new owner writes.

| Surface | Full writer | Assisted writer | Other roles do instead |
|---------|-------------|-----------------|------------------------|
| task control/status | Coordinator | task owner/steward | write role artifact and hand off its reference |
| coordinator journal | Coordinator | task owner/steward | never append directly; request/return through owned trace |
| HL/TS | Coordinator | task owner if the edition uses them | reference, do not rewrite |
| research/RES | Researcher | task owner/assigned researcher | coordinator records only dispatch/handoff reference |
| ONB/RF/evidence | Executor | task owner/assigned executor | journal links outcome, not copied detail |
| REVIEW | Reviewer | task owner/assigned reviewer | journal links verdict and transition |
| generated task catalogue/status projection | deterministic generator or declared catalogue owner | same | nobody hand-edits live values |
| Git index/commit | local Git participant; one landing owner for the commit | optional/edition policy | no broad staging; actor identity remains in artifacts/journal |

This map separates status strictness from locking. YAML does not serialize writers; a file lock does not establish business ownership; a one-writer rule does not make a disconnected second device harmless. Each control addresses a different failure.

### E4. Narrow coordinator journal grammar

The event model is shared even if serialization differs. It records management facts, never role work bodies.

#### Closed event vocabulary

| Kind | Required meaning | Required reference/state data |
|------|------------------|-------------------------------|
| `created` | task identity/control created | control path and initial lifecycle |
| `dispatch` | role/session assigned material work | role, assignee, target artifact/scope ref |
| `handoff` | an assigned role returned, paused, or transferred work | producing artifact/gate ref; outcome word only |
| `transition` | lifecycle or workflow stage changed | `from`, `to`, controlling artifact/ref |
| `blocked` | progress stopped by dependency/capability/decision | block kind + source/ref |
| `resumed` | prior block/wait cleared | prior event ID + clearing ref |
| `amendment_escalated` | frozen HL change proposed or decided | HL amendment/proposal/ref; never copy proposal body |
| `landed` | task-owned paths committed or consolidation landed | commit ID + task/phase scope ref |
| `consolidation` | controlled project view/debt/knowledge boundary ran | output ref + result word; Phase A uses catalogue only |

#### Record fields

| Field | Rule |
|-------|------|
| `event_id` | task-scoped monotonic ID such as `TFW-60-E0007`; never reused |
| `at` | RFC 3339 UTC timestamp |
| `kind` | one vocabulary value above |
| `actor` | declared project identity, not a display-only model label |
| `state_delta` | `from → to` only where applicable; otherwise null |
| `ref` | at least one repo-relative artifact path/anchor or commit ID; `created` references control |
| `related_event` | optional earlier event ID for resume/handoff/correction |
| `summary` | optional single line, proposed ceiling **240 Unicode code points**; must add routing context rather than restate the referenced artifact |

Never journal: prompts, chat messages, tool calls, ordinary reads, intermediate reasoning, full findings, test output, evidence bodies, review observations, debt text, or knowledge facts. A role artifact remains canonical; the journal answers who coordinated what, when, and where the durable result lives.

#### Size and retention proposal to test in Challenge

- Active segment ceiling: **100 events or 32 KiB, whichever comes first**. The numbers are a challenge target derived from GSD v1's under-100-line state discipline and AFD's evidence that advisory prose rules alone do not prevent growth; they are not final verdicts.
- At the ceiling, seal the numbered segment and create the next segment at a new stable name; do not rename, truncate, summarize away or rewrite the sealed segment. The control field `journal_head` selects the active one.
- Keep all sealed segments with the task, including rejected tasks. The project catalogue exposes only current state/terminal outcome and never embeds journal history.
- Cold start reads control + the event named by `last_event_id`; full history is on-demand. Segment retention is historical provenance, not always-load context.
- An event over the summary limit must use a reference. It cannot be split into several pseudo-events merely to evade the limit.

Current GSD separates an append-only `DECISIONS.md` responsibility from rendered `STATE.md`, while Hermes caps a completion-event summary and keeps full run detail elsewhere. Those systems use DB/command enforcement outside this task's candidate set, but their responsibility separation supports the reference-first grammar. Primary context: [`open-gsd/gsd-pi` configuration](https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/configuration.md) and [Hermes Kanban reference](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/kanban.md).

### E5. Two-file ordering and reconciliation

C1/C2 have a snapshot and journal without a cross-file transaction. Their candidate protocol is:

1. The state owner allocates the next event ID and appends the event first.
2. The same owner updates the snapshot and sets `last_event_id` to that ID.
3. Journal ahead of snapshot means a transition may be pending/recoverable; the owner reconciles by applying or compensating it.
4. Snapshot pointing to a missing event is invalid: stop state transitions, wait for sync, and reconcile preserved copies.
5. A retried event ID is idempotent only if its full record is byte-equivalent; otherwise it is a conflict requiring a new correction event.

C4 avoids snapshot authority but pays for log parsing. C5 avoids cross-file lag but puts snapshot rewrites and appends in one conflict domain. Challenge must compare these failures rather than assume one is atomic.

### E6. Cold-start paths

The permanent root entry is an instruction/router, not a manually updated task table.

#### Agent, no prior chat and no command knowledge

1. `AGENTS.md`/README states the authority rule and fixed control glob.
2. Agent scans `tasks/*/<control-name>` or the edition-declared equivalent.
3. It parses ID, goal/value, lifecycle/outcome, owner, next action/ref and freshness.
4. It may open a generated catalogue for ranking, but re-reads the selected task's local authority before resume.
5. Missing/invalid control is reported as an unindexed legacy/malformed task, not silently omitted.

#### Non-technical human using ordinary file browsing

1. Root README's permanent Work/Tasks entry links a generated `tasks/INDEX.md` when present and says it may be stale.
2. The index shows ID, goal, value, lifecycle, coordinator, and terminal outcome with a link to the fixed task control path.
3. If the index is absent/stale, the same entry explains: open `tasks/`, choose a task folder, open the fixed control file. No shell command is required for inspection.
4. Editing is allowed only for the named state owner. Other people add their own artifact or ask the owner; the view itself is never edited.

Every generated catalogue declares: `authority=derived`, generation time, source schema version, source count/digest or repository revision, and rebuild command/path. Resume/release never trusts it over task-local control.

This does not prove YAML or marker usability. Challenge must hand the candidate path to a fresh agent and a non-technical reader without explaining the hidden command.

### E7. File-sync operating rules are carrier-independent

1. A task directory never moves to express lifecycle. Identity and all references keep the same base path.
2. Only the task's `state_owner` writes its control and journal. Different roles write their declared artifact paths.
3. Independent tasks use disjoint task folders; generated project views are not edited during normal transitions.
4. A lifecycle change is not started while the local sync client reports an error or unsynchronized prior state. This is an operating precondition, not a distributed lock.
5. Offline work may continue in role-owned files, but no two devices may intentionally edit the same task control/journal offline. Ownership remains in force when disconnected.
6. Provider-created conflict copies are preserved. The state owner stops transitions, compares both copies and journal cursors, records a compensating event if needed, then removes/archives only after reconciliation.
7. No algorithm assumes ordered visibility of the event and snapshot files. Readers use `last_event_id` rules from E5.
8. Generated views can lag and be replaced at any time; they never repair task state backwards.
9. Directory rename/move, provider API locks, online daemons and SQLite/WAL are not normal transition mechanisms.

These rules follow the vendor floor gathered in Stage 2: independent files propagate, while same-file conflicts, offline forks and move ambiguity are expected. They do not claim cross-device atomicity.

### E8. Git profiles and landing controls

Git is a distinct layer over the synchronized working files.

| Profile | Working files | Git metadata/index | Landing | Visible trade-off |
|---------|---------------|--------------------|---------|-------------------|
| **G-A external local Git directory per participant** | common synced root | each Git-capable participant configures a machine-local `GIT_DIR` and index with the synced root as `GIT_WORK_TREE` | declared owner lands one task/phase commit | separates indexes but requires a wrapper/environment; plain `git` discovery from the folder does not work |
| **G-B one Git landing owner** | common synced root for all | only landing machine has local repository metadata outside sync | peers finish artifacts; landing owner stages explicit task paths and commits | simplest non-technical peer model; Git authorship depends on journal/artifact attribution plus committer rules |
| **G-C local clones plus synced task exchange** | each participant has local clone; selected task files synchronize through a separate shared path/import step | ordinary local `.git` per clone | Git remote/landing branch plus explicit import | strongest Git isolation, but two transports and import reconciliation increase product complexity |

Official Git documentation permits an explicit `--git-dir`/`GIT_DIR` with `--work-tree`/`GIT_WORK_TREE` ([`git` manual](https://git-scm.com/docs/git)). `git init --separate-git-dir` instead leaves a text `.git` file in the worktree pointing to the actual repository ([`git-init`](https://git-scm.com/docs/git-init)); inside a cross-machine synced root that pointer itself is machine-specific state. Therefore "keep `.git` local" cannot mean blindly moving `.git` elsewhere while synchronizing its pointer file.

Landing controls shared by G-A/G-B/G-C:

- never synchronize `.git`, a `.git` pointer file, worktree administration, index, locks or reflogs as project content;
- stage literal, explicit task-owned paths; no `git add .`, broad glob, or `commit -a` in the collaboration path;
- before commit, compare `git diff --cached --name-only` to the declared task/phase ownership set and fail on an out-of-scope path;
- one task/phase/role subject per commit; root catalogue consolidation, if any, lands in its own declared commit;
- preserve freeze baselines and existing attribution grammar;
- local indexes address TD-144; scope check + own-task commit address TD-178. Neither substitutes for the other.

No Git profile is selected in Extract. Challenge must test usability, especially G-A's configuration burden and G-B's provenance handoff.

### E9. Deep-mode OODA loops

| Loop | Observe/orient | Configuration revision | Counter-evidence retained |
|------|----------------|------------------------|---------------------------|
| 1. Configurations + field contract | Crossed D1-D14 and mapped existing Full/Assisted states | Reduced shared model to logical fields and coarse lifecycle; produced C1-C5 instead of selecting a syntax | current editions do not share identity or artifacts; generated views can hide malformed legacy tasks |
| 2. Journal + ownership | Applied frozen journal requirements and external bounded-log examples | Closed event vocabulary, reference-first records, segment proposal, and persistent `state_owner` | append-only still grows; split snapshot/log is not atomic; combined file enlarges conflict domain |
| 3. Cold start + sync/Git | Replayed provider offline behavior, TD-144/178, and official Git path controls | Separated permanent router, derived catalogue, file-sync rules, Git profiles and landing checks | external Git directory needs tooling; one landing owner can misattribute; no file format supplies a distributed lock |

Hypothesis verdicts remain deliberately open. C1-C5 and G-A/G-B/G-C are inputs to Challenge, not final recommendations.

## Checkpoint

| Found | Remaining for Challenge |
|-------|-------------------------|
| Five coherent configurations across all Gather dimensions | Eliminate combinations through cold-start, growth, offline, conflict-copy, owner-loss, rejection and landing scenarios. |
| Minimal logical state contract and shared lifecycle mapping | Test whether any field lacks a consumer or any current Full/Assisted state cannot migrate losslessly. |
| Persistent one-writer ownership map | Test coordinator disappearance/reassignment and same-task parallel handoff. |
| Closed reference-first journal grammar with concrete segment proposal | Stress 100-task/long-task growth, two-file ordering, malformed events and duplicate IDs. |
| Explicit agent and non-technical human cold-start paths | Run fresh-reader tests without teaching a hidden command. |
| Carrier-independent file-sync rules | Exercise offline edit/reconnect and provider conflict-copy recovery. |
| Three local-Git profiles plus staging/landing/provenance controls | Test G-A configuration burden, G-B attribution, and actual post-sync commit scope. |

**Alternatives at this gate:** C1 strict YAML split; C2 bounded Markdown + JSONL split; C3 status markers + immutable event files; C4 event-derived JSONL; C5 combined bounded status/journal document. Git profiles G-A/G-B/G-C remain orthogonal.

**Recommendation at this gate:** proceed to Challenge. Extract closed the requested structural gaps; additional synthesis now would prematurely choose among configurations that have not faced the mandatory failure scenarios.

**Questions for the Coordinator:** none. The approved direction is sufficient.

**Files written at this gate:** `research/iter1/3_extract.md` (plus previously accepted `1_briefing.md` and `2_gather.md`).

**Evidence state:** external evidence used in this stage is current official Git documentation plus current primary GSD/Hermes responsibility boundaries; service/database guarantees remain counterexamples only. All design numbers and configurations are proposals awaiting Challenge, not shipped claims or hypothesis verdicts.

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?
- [x] At least one hypothesis tested and counter-evidence sought (deep mode)?
- [x] Three Extract loops completed?

Stage complete: YES
→ User decision: WAIT — Coordinator must approve Challenge or redirect an Extract gap.
