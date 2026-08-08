# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-52](../../HL-TFW-52__tfw_light_v1.md)
> Goal: Determine the smallest reliable Assisted mechanisms for discipline, collaboration, identity, and durable memory while preserving Light's simplicity and the approved edition boundary.

## Evidence Method

Gather ran three DEEP-mode OODA passes without modifying the approved HL, control files, adapters, product files, or any real synchronized folder.

1. **Official-contract pass:** current OpenAI/ChatGPT Codex documentation was used for `AGENTS.md`, hooks, scheduled tasks, memories, skills/customization, and Windows-specific hook configuration. Current Google Drive Help was used only for the bounded synchronized-folder failure model.
2. **Local-observation pass:** read-only inspection recorded the installed Windows desktop package, trust/config state, hook/memory presence, current repository guidance, and the nested TFW-51 root path. No Codex child session was launched because that could create session state outside the five permitted iteration files.
3. **Disposable-model pass:** PowerShell data structures simulated candidate allocation, semantic duplicates, two offline lease claimants, conflict-copy names, interruption, idempotent recovery, and index rebuild entirely in memory. No fixture files and no real Drive data were created.

The OpenAI documentation helper was not run because it writes a temporary manual cache outside `research/iter2/`, which the owner lock forbids. The official documentation pages below were fetched directly instead.

## Official Primary Sources

| ID | Source | Material used |
|---|---|---|
| O1 | [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Instruction discovery runs once per Codex run; project scope starts at the project root (typically Git root), walks toward `cwd`, and falls back to the current directory when no project root is found. Nested guidance is concatenated root-to-leaf. |
| O2 | [Hooks](https://learn.chatgpt.com/docs/hooks) | Supported lifecycle events and wire behavior; hook locations and trust; `SessionStart`, `PreCompact`, `PostCompact`, `Stop`, and `SessionEnd`; command-only handlers; Windows override; concurrent hook execution; current release limitations. |
| O3 | [Scheduled tasks](https://learn.chatgpt.com/docs/automations?surface=app) | Local-project schedules need the computer on, desktop app running, and project available; web schedules cannot work directly in a local folder; CLI/IDE do not provide the Scheduled management interface. |
| O4 | [Memories](https://learn.chatgpt.com/docs/customization/memories) | Local Codex memories are off by default, stored under `~/.codex/memories/`, updated asynchronously after eligible idle chats, may skip generation near rate limits, and are generated state rather than a primary control surface. |
| O5 | [Customization overview](https://learn.chatgpt.com/docs/customization/overview) | `AGENTS.md`, memories, skills, MCP, and subagents are complementary surfaces with different scopes; skills package reusable workflows rather than lifecycle guarantees. |
| G1 | [Fix problems in Drive for desktop](https://support.google.com/drive/answer/2565956?co=GENIE.Platform%3DDesktop&hl=en) | Incompatible local/cloud changes can leave a copy rather than update the original; retry and recovery are not equivalent to an atomic merge. |
| G2 | [Stream and mirror files with Drive for desktop](https://support.google.com/drive/answer/13401938?hl=en) | Offline/mirrored files later synchronize, and when differing content already exists Drive can keep both. This supports modeling conflict copies and delayed visibility. |

The current hooks page explicitly warns that linked `main`-branch schemas may lead the installed release; this research treats the page's described release behavior, not repository-main schemas, as the platform contract.

## Dimensions

Each row is an independent decision factor. Alternatives remain open; none is marked recommended in Gather.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| **D1 Root/instruction authority** | Codex-discovered Git/current-directory root | Explicit Assisted root marker found by ancestor walk | User/configured absolute project root | Installed plugin root plus project marker |
| **D2 Enforcement surface** | `AGENTS.md` only | Start/compact/stop hooks | Wider prompt/tool/session hook set | External wrapper/scheduler around Codex |
| **D3 Session-start context** | Static `AGENTS.md` chain | `SessionStart` additional context | Explicit start skill/command | Manual launch prompt |
| **D4 Checkpoint trigger** | `PreCompact` | Periodic/time-based check | Significant tool/file transition | Manual or task-close only |
| **D5 Completion gate** | `Stop` continuation | `SessionEnd` advisory save | Explicit close skill/command | Continuous task-state validation |
| **D6 Weekly execution** | Lazy catch-up on next project start | Desktop scheduled task | External OS scheduler | Web scheduled task with connected storage |
| **D7 Staleness signal** | `last_success_at + interval` | Calendar/ISO-period bucket | Candidate high-water/dirty marker | Time plus unprocessed-input hybrid |
| **D8 Candidate identity** | Random UUID | UTC timestamp + profile + random suffix | Content hash | Shared sequence/counter |
| **D9 Consolidator coordination** | Designated guardian, no lease | Shared expiring lease | Unique run staging plus deterministic reconciliation | External lock/service |
| **D10 Record publication** | Mutable records in place | Write-new then replace | Immutable versioned records with supersession | Per-run immutable snapshot |
| **D11 Index publication** | Incremental edit | Local temp-and-replace | Full rebuild from accepted records | Versioned index snapshots plus active pointer |
| **D12 Identity selection** | Ask every session/task | Single profile auto, otherwise one question | Device-local binding | OS/workspace account mapping |
| **D13 Participant identity key** | Mutable display handle | Stable opaque profile ID | Email/workspace identity | Cryptographic identity |
| **D14 Authorship provenance** | Author handle only | Profile ID + display snapshot + source/task/time | Profile + device/run identity | Signed record/receipt |
| **D15 Task activation** | Every prompt creates a task | Explicit user command only | Semantic prompt heuristic | First durable-result/file transition |
| **D16 Risk handling** | Ask before every promotion | Category-based gate | Allowlist-only promotion | No shared promotion; pointers only |
| **D17 Platform implementation** | One portable runtime | Per-OS commands/scripts | Windows-first implementation | Plugin-packaged runtime abstraction |

## Findings

### G-F1 — H1 platform contracts exist, but their guarantees are narrower than the HL wording

The current official hooks page documents all three lifecycle surfaces named by H1:

- `SessionStart` sources are `startup`, `resume`, `clear`, and `compact`. Plain text or JSON `additionalContext` becomes developer context. After root-session compaction, a `SessionStart` matching `compact` runs before the immediate next model request.
- `PreCompact` runs for `manual` or `auto` compaction. Plain-text stdout is ignored. JSON can stop compaction, but the hook itself must persist any checkpoint; Codex does not create a task checkpoint automatically.
- `Stop` receives `turn_id`, `stop_hook_active`, and `last_assistant_message`. A blocking decision creates a continuation prompt instead of rejecting the turn. The hook must use `stop_hook_active` and idempotent state checks to avoid continuation loops.

Important boundaries:

1. Only `type: command` handlers execute today. `prompt` and `agent` handlers are parsed but skipped. Therefore semantic questions such as “is this a substantive task?” cannot be delegated to an agent hook handler under the current release contract.
2. Project hooks run only from a trusted project `.codex/` layer, and each non-managed command definition must be reviewed/trusted by hash. Changed hooks are skipped pending re-review. “Mandatory” therefore means mandatory after an explicit installation/trust step, not zero-touch on first open.
3. Matching hooks from multiple sources all load and matching command hooks launch concurrently. A project hook cannot assume it is the only hook or prevent another matching hook from starting.
4. Hook commands run with the session `cwd`. The official page recommends Git-root resolution for repo hooks because Codex may start in a subdirectory. That example does not solve a non-Git Drive-style project; Assisted needs another root-authority mechanism or an explicit correct-root requirement.
5. `commandWindows`/`command_windows` is available, asynchronous hooks are not supported, and hard-coded `python3`, POSIX quoting, or `git rev-parse` is not cross-platform/non-Git-safe.
6. `SessionEnd` is advisory. It may run on archive/delete, normal close, or after 30 idle minutes, does not run for subagents, cannot steer Codex, and does not immediately run when merely switching away. It is not a completion gate.
7. Transcript paths are exposed for convenience but are explicitly not a stable hook interface. An Assisted checkpoint should not parse transcript internals as its only source of active-task truth.

The lifecycle events can enforce file/state invariants that a command can inspect. They cannot by themselves understand the user's goal, guarantee that an old already-running session rereads newly changed guidance, or prove that a semantically correct trace was written.

### G-F2 — Evidence lanes for H1 must stay separate

| Mechanism | Documented support | Observed in this local session | Unavailable or not evidenced locally | Candidate Assisted behavior to compare in Extract |
|---|---|---|---|---|
| `AGENTS.md` discovery | Once per run; Git/current root chain; nested overrides | Root `AGENTS.md` content is present in this task's project instructions | No child-session smoke test under alternative roots | Root self-check plus short durable rules |
| `SessionStart` | `startup/resume/clear/compact`, additional context | No user/project `hooks.json` is installed | Event execution and trust UX not exercised | Load project/task/memory summary; check due state |
| `PreCompact` | Before manual/auto compact; command may persist state or stop compaction | No hook installed | Actual compaction callback not exercised | Idempotent active-task checkpoint from files, not transcript schema |
| `PostCompact`/compact start | Post event plus `SessionStart source=compact` | No hook installed | Restoration after real compact not exercised | Re-inject short state after checkpoint |
| `Stop` | Can create continuation prompt; `stop_hook_active` exposed | No hook installed | Loop prevention and file correction not exercised | Compare inspect-only, direct safe repair, and continue-agent policies |
| `SessionEnd` | Advisory, delayed/close/archive cases | No hook installed | Timing not exercised | Optional best-effort receipt only, never sole close gate |
| Skills | Official reusable workflow surface | Repository `tfw-research` skill routed this `/tfw-research` session and gates are being followed | No evidence that an ordinary prompt selects a task skill | Compare explicit close/start skill as fallback, not lifecycle replacement |
| Local memories | Local generated state, off by default, delayed | Memory directory exists but is empty; no memory feature key was found | No generation/use pass executed | Exclude as shared truth; optional personal convenience only |
| Scheduled tasks | Desktop/web scheduled surfaces documented | No task run inspected | Local scheduled execution not exercised | Optional accelerator that invokes the same idempotent consolidator |

### G-F3 — Read-only local observations

| Observation | Result | Interpretation boundary |
|---|---|---|
| Installed desktop package | `OpenAI.Codex` Windows x64 package version `26.727.6591.0` | This is the desktop package version, not a semantic CLI release number. |
| Project trust | Global `config.toml` contains the exact `steps-framework` path with `trust_level = "trusted"` | Project trust exists, but individual hook-definition trust is separate and no project hooks exist. |
| Hook configuration | No global `~/.codex/hooks.json`; no repository `.codex/hooks.json` or `.codex/config.toml` | Current local behavior cannot demonstrate H1 hook execution without forbidden product/config writes. |
| Memory configuration/state | No matching memory feature keys; `~/.codex/memories/` exists with zero entries | This is consistent with the documented default-off behavior, not proof about another device/account. |
| CLI executable | Desktop-bundled `codex.exe` resolves under WindowsApps but execution from this thread's shell returned Access Denied | CLI smoke testing is unavailable from this host context; it does not imply the desktop app itself cannot run Codex. |
| Current skill | Repository-local `tfw-research` skill was selected and enforced | Confirms skill routing in this task, not task-start/completion enforcement for arbitrary prompts. |

### G-F4 — Bounded root-discovery fixture

The existing TFW-51 prototype is stored at `tasks/TFW-51__tfw_light_ru/tfw-light-ru/` inside this repository. A read-only ancestor walk found:

- Git root: `D:\projects\research\steps-framework`
- Guidance on the documented root-to-`cwd` path: root `AGENTS.md` and nested prototype `AGENTS.md`

According to O1, opening that nested source directory in place does not behave like opening a copied standalone starter: the parent repository guidance participates in the instruction chain. In a non-Git standalone copy where Codex finds no other project root, only the current directory is checked. This validates wrong-root/source-versus-runtime as a real bounded scenario without reopening iteration-1 topology selection.

### G-F5 — H2: schedule and catch-up are not equivalent in wall-clock freshness

Official scheduled-task behavior creates four distinct execution states:

| State | Local project schedule | Lazy catch-up | External alternative |
|---|---|---|---|
| Computer on, desktop app running, project available | Supported | Runs at next start/prompt if due | OS scheduler also possible |
| Computer on, desktop app closed | Not supported for local project files | Does not run until next project start | Task Scheduler/cron/launchd must run a separate deterministic local program |
| Computer off/asleep | Does not run | Does not run | No local mechanism runs until wake/boot |
| Web scheduled task | Runs in hosted context | N/A | Cannot directly work in the local project folder; needs uploaded/connected storage |
| CLI or IDE only | No Scheduled management interface | A start hook/explicit command can catch up | External scheduler remains outside Codex |

Consequences:

- A lazy catch-up can provide equivalent freshness **at the boundary of the next successful project start**, if no consumer needs the shared index between the missed deadline and that start and the hook is installed/trusted.
- It cannot provide the same calendar-time freshness. The delay is unbounded while the project remains unopened.
- The smallest quiet interaction is zero questions for a successful routine run, followed by at most one terse status line. Sensitive or conflicting candidates can be held and asked as one compact batch. A question is not needed merely because time elapsed.
- Desktop scheduling and start catch-up must invoke the same idempotent consolidator. Otherwise simultaneous schedule/start runs create two code paths and two failure modes.

Staleness itself has multiple meanings: time overdue, unprocessed input, incomplete prior run, or stale derived index. A time-only flag can say “fresh” while new candidates remain; a candidate-only flag never triggers maintenance when index pruning is due. Extract must combine or explicitly choose among D7 alternatives.

### G-F6 — In-memory H3 fixtures

The successful fixture ran in Windows PowerShell with no filesystem writes.

| Scenario | Fixture result | What it establishes / does not establish |
|---|---|---|
| Three writers, random-suffixed IDs | 3,000 generated, 3,000 distinct, 0 observed collisions | Demonstrates the construction avoids central allocation in this sample; does not mathematically prove zero UUID collisions. |
| Two writers, shared counter | Both read/allocated `C-000042`; 1 collision | A central next-ID file is a hot read-modify-write point. |
| Formatting duplicate | Two differently cased/spaced claims normalized to the same SHA-256 key | Unique candidate files do not remove semantic duplicates; consolidation still needs explicit deduplication and source retention. |
| Two offline lease claimants | Both saw no lease and believed they acquired it | A lease file in an asynchronously synchronized folder cannot guarantee strict mutual exclusion during offline/delayed visibility. |
| Conflict-copy/unexpected filenames | 4 physical files; a strict filename pattern accepted 2, schema parsing recovered 3 unique candidate IDs | Recovery must validate payload identity and deduplicate by candidate ID; filename shape alone can silently omit conflict copies. |
| Interrupted consolidation | 3 candidates, 1 record before crash, 3 deterministic records after rerun, 3 rebuilt index entries, 0 source deletions | Idempotent record IDs plus retained candidates allow recovery in this bounded model. It does not validate actual Drive upload ordering or cross-device atomicity. |

Google's official support material supplies counter-evidence to treating ordinary file updates as transactions: incompatible local/cloud changes can leave copies or move edits to recovery locations. Therefore a synchronized folder must be treated as delayed multi-copy transport, not a lock service or database.

### G-F7 — H3 architecture implications remain alternatives, not a selected design

The phrase “one consolidator” has three different possible meanings:

1. **One designated human/device normally runs it.** This removes routine multi-writer pressure but does not prevent an accidental or offline second run.
2. **One active run is coordinated by a shared lease.** This reduces ordinary overlap when visibility is timely but cannot provide strict exclusion offline.
3. **Multiple runs may occur, but immutable inputs and receipts make split-brain detectable and recoverable.** This accepts duplicate work and requires reconciliation/publish authority.

Knowledge-loss prevention also decomposes:

- **Candidate preservation:** every candidate is immutable, uniquely identified in its payload, and never pruned before a receipt accounts for it.
- **Semantic consolidation:** duplicate/contradictory candidates can map to one or more records while preserving all source IDs and epistemic status.
- **Record publication:** a crash or second consolidator cannot silently overwrite the only accepted durable record.
- **Index recovery:** `INDEX.md` is recreated entirely from accepted records; its absence or conflict is a navigation failure, not knowledge loss.
- **Conflict-copy intake:** unexpected physical filenames and duplicate physical copies are scanned by schema/payload identity, quarantined if invalid, and reported.

The Gather evidence supports recoverability under these conditions. It does not prove that a shared lease prevents two consolidators or that a derived index alone prevents loss.

### G-F8 — H4 identity UX can attribute work, but it cannot authenticate the actor

| Scenario | Minimal behavior target | Remaining ambiguity |
|---|---|---|
| Exactly one valid profile | Auto-select; do not create or consult a current-user binding | The profile still represents declared project identity, not verified OS identity. |
| Multiple profiles, valid local binding | Reuse without a question | Binding must be keyed to stable project identity and stable profile ID, not path/display handle alone. |
| Multiple profiles, no binding/new device | Ask one short choice before recording authorship/ownership | Reading or an ordinary conversation does not need the question. |
| Binding points to missing profile | Treat as stale and ask once | Silent fallback would misattribute work. |
| Participant renamed | Preserve binding if profile has an immutable ID; read the new display handle from the profile | Handle-only bindings break or create false new users. |
| Participant removed/replaced | Invalidate binding and ask once | Historical records keep the old profile/display snapshot. |
| Unknown user reads or asks a non-work question | Do not create a task and do not require identity | If the conversation later creates durable work, identity becomes necessary at that boundary. |
| Unknown user begins durable work | Do not guess; require one choice or leave the contribution explicitly unattributed/pending | “Unknown” is safer than borrowing the last device user. |
| Privacy review | Keep device binding outside the synchronized folder and store only the minimum project-ID → profile-ID relation | Shared provenance still exposes project-level author identity by design. |
| Authorship dispute | Show declared profile, task/source, time, and consolidation receipt | Without account authentication/signature, the files cannot prove who physically used the device. |

This evidence supports H4 as a low-friction **attribution/provenance** mechanism. “Reliably establishes authorship” is too strong if interpreted as authentication or non-repudiation.

### G-F9 — Task activation, owner/status consistency, and non-work conversation

No current hook event means “a substantive task has begun.” Available mechanisms observe prompts, tool calls, lifecycle events, and completion attempts:

- `UserPromptSubmit` exposes prompt text, but only command handlers run; a deterministic semantic classifier will have false positives/negatives.
- Tool hooks can observe commands/file operations, but task intent should exist before the first destructive or result-producing action, and tool coverage/surface names can vary.
- `Stop` is late enough to repair omissions but cannot prove the trace was created before work.
- `AGENTS.md` plus `SessionStart` can direct the model to create a task early, but this remains agent behavior until a later hook checks physical invariants.

The alternatives in D15 therefore stay live. Any design must satisfy both sides of the HL: a meaningful task gets owner/trace/status discipline, while ordinary questions, reading, or project orientation do not create false tasks.

Task-local consistency can be mechanically inspected at Stop without a shared task board:

- exactly one task folder is declared active for the current run or none;
- trace owner equals the stable profile ID used in authored candidates;
- folder status, trace status, result links, and candidate receipts agree;
- another participant's trace is not rewritten without explicit ownership transfer;
- failure to determine identity leaves ownership pending rather than guessed.

Whether the Stop command repairs a safe mismatch directly or returns a continuation prompt remains an Extract/Challenge configuration choice.

### G-F10 — Quiet risk gate categories

| Category | Candidate handling alternatives that remain open | Hard boundary observed from owner/HL |
|---|---|---|
| Routine project fact/decision/format preference | Quiet promotion; quiet candidate retention; confidence threshold | No question merely for routine processing. |
| Ambiguous/contradictory conclusion | Retain as candidate; create conflict record; one batched question | Do not silently choose a contested fact. |
| Health/medical, personal/sensitive data, minors | Redacted pointer; explicit opt-in to shared record; private/local-only retention | Do not silently promote identifiable sensitive content. |
| Legal dispute/high-stakes finance/safety | Source-required record; human-confirmed status; keep as unresolved claim | Do not convert a disputed/high-stakes conclusion into a fact autonomously. |
| Password/token/key/secret | Reject/quarantine metadata; replace with safe-store pointer | Never store the secret in trace/candidate/index; notify about removal/rotation. |
| Ordinary non-work conversation | No task, no candidate, no identity question | Escalate only if the conversation crosses into durable work or shared memory. |

A hook command can apply deterministic secret patterns and structural checks, but medical/legal/personal-context interpretation is semantic. With command-only hooks, the safest platform-supported pattern may be to add developer context and let the model hold/ask, then have Stop verify that no prohibited candidate was published. This remains a configuration, not a Gather recommendation.

### G-F11 — Windows and cross-platform constraints

- Official hooks support `commandWindows`; a single POSIX `command` is not sufficient evidence of Windows support.
- Commands run at session `cwd`; relative `.codex/hooks/...` paths are unsafe when a session starts below the project root.
- Git-root discovery cannot be the only Assisted locator because the target includes non-Git synchronized folders. An ancestor marker, configured path, plugin root, or strict open-root requirement remains necessary.
- `python3`, `python`, and `py -3` availability differs; a bundled/runtime-free PowerShell path is Windows-specific, while shell scripts are not portable. The implementation choice must be explicit.
- Local atomic replace semantics do not establish atomicity across a sync provider. Run staging, completion receipts, and rebuild behavior must tolerate delayed/conflict copies independently of local rename behavior.
- Paths, case sensitivity, reserved names, timestamp formatting, and line endings must be normalized in candidate IDs/receipts. Payload IDs must remain authoritative over filenames.

## Preliminary Hypothesis Tests

These are Gather orientations, not final RES verdicts.

| Hypothesis | Gather orientation | Confirming evidence | Counter-evidence / unresolved proof |
|---|---|---|---|
| **H1** | **Partial support; reliability/sufficiency unproven** | All named lifecycle events are documented; Stop can continue work; compact-start can re-inject context. | Hooks require trust, only command handlers run, no semantic task-start event exists, AGENTS loads once/run, cwd/root can be wrong, local hooks are not installed/tested. |
| **H2** | **Literal equivalence challenged; next-start equivalence plausible** | Start catch-up can process overdue local state before later work without a permanently running app. | Calendar freshness is impossible while app/project remain closed; desktop local schedules need computer/app; web schedules cannot access local folder. |
| **H3** | **Bounded recoverability support; prevention wording too strong** | Unique immutable inputs, deterministic rerun, retained candidates, receipts, and rebuild recovered the in-memory interruption model. | Shared-file lease failed strict offline exclusion; conflict copies and divergent consolidators remain possible; real sync ordering not tested. |
| **H4** | **UX rule supported for attribution; authentication claim challenged** | Single-profile auto and valid local binding remove unnecessary questions; stable profile IDs handle rename. | A local binding is a declaration, not proof of physical actor; stale/deleted bindings and new devices still require one question. |

## Gather Decisions (research-process only)

| # | Decision | Rationale |
|---|---|---|
| **G-D1** | Preserve four evidence lanes in all later artifacts: documented support, observed local behavior, unavailable/unproven behavior, and proposed adapter behavior. | The approved HL currently blends platform and adapter claims; separation prevents an implementation proposal from becoming a claimed Codex guarantee. |
| **G-D2** | Carry strict offline mutual exclusion as **unproven/failed in the shared-file model**; Extract must model both exclusion attempts and split-brain recovery. | Both offline claimants can observe no lease. Calling a lease “one writer” would hide counter-evidence. |
| **G-D3** | Split H2 freshness into calendar-time freshness and next-project-start freshness. | Scheduled and lazy execution are comparable only at the later start boundary, not during the closed interval. |
| **G-D4** | Split H4 into identity selection, shared provenance, and authentication/non-repudiation. | Device-local binding can select a declared profile but cannot prove who physically used the device. |
| **G-D5** | Treat task activation as an independent dimension rather than assuming `SessionStart` creates tasks. | Current hooks expose lifecycle/prompt/tool events, not the semantic start of meaningful work. This is necessary to protect non-work conversations. |
| **G-D6** | Keep root discovery and Light → Assisted preservation bounded to runtime validation fixtures. | The coordinator lock excludes topology redesign; the nested TFW-51 observation is sufficient to keep wrong-root behavior in scope without choosing X1/X2/X3. |

## Counter-Evidence and Simpler Alternatives Retained

- `AGENTS.md` plus one explicit close skill may be sufficient for low-frequency single-user Assisted work; hooks may not justify trust/setup cost in every environment.
- `SessionStart + Stop` without `PreCompact` may be sufficient if traces are updated continuously; conversely `PreCompact` is valuable only when active task state is already explicit in files.
- Catch-up-only is simpler than dual schedule/catch-up when no one consumes the index between sessions.
- Designated guardian plus recovery may be simpler and more honest than pretending a shared lease is a distributed lock.
- Deterministic full index rebuild may be safer than incremental index edits for the small Assisted scale.
- Session-local one-question identity avoids persistent binding/privacy state, at the cost of recurring friction.
- OS account mapping removes a question but can be wrong on shared devices and does not necessarily match a project participant.
- No automatic promotion (pointers/candidates only) minimizes sensitive-data risk but weakens the “quiet memory” value proposition.

## Checkpoint

| Found | Remaining for Extract/Challenge |
|---|---|
| Current Codex officially supports `SessionStart`, `PreCompact`, `PostCompact`, `Stop`, and `SessionEnd`, with precise but limited command-hook semantics. | Choose and cross-reference lifecycle configurations; actual local hook execution is untested because no hooks are installed and product writes are forbidden. |
| Project hooks require project trust and per-definition hash review; only command handlers execute; matching hooks can run concurrently. | Model first-run/trust failure and multiple-hook interactions. |
| AGENTS/root discovery is once per run and root-dependent; nested TFW-51 source inherits parent-repository guidance. | Define bounded wrong-root detection/fail-safe alternatives without selecting product topology. |
| Local scheduled tasks require computer + desktop app + project; web schedules cannot directly use the local folder. | Build H2 state/configuration space and smallest quiet interaction. |
| Memory is local, generated, delayed, and off by default; local state is empty here. | Confirm it remains optional/personal in Challenge; do not use it as shared authority. |
| Unique candidates and deterministic rerun recovered the in-memory interruption; shared counter and offline lease failed. | Build configurations for guardian, lease, staging/receipts, reconciliation, and rebuild; attack dual-consolidator recovery. |
| Single-profile auto and local binding reduce questions, but only establish declared provenance. | Build identity state machine across new/stale/renamed/deleted/unknown cases and privacy/authorship dimensions. |
| No hook directly denotes semantic task start. | Compare prompt, explicit command, first durable transition, and hybrid activation while protecting ordinary conversations. |

**Sufficiency:**
- [x] External source used? — current official OpenAI/ChatGPT Codex pages plus bounded official Google Drive support.
- [x] Briefing gap closed? — Gather now separates platform contracts, local observations, unavailable behavior, and adapter alternatives for H1–H4.
- [x] Dimensions identified? — 17 independent factors with at least three alternatives each.
- [x] Hypothesis tested? — preliminary tests recorded for H1, H2, H3, and H4.
- [x] Counter-evidence sought? — trust friction, command-only hooks, no semantic task-start event, closed-app schedule limits, offline lease split-brain, conflict copies, and attribution/authentication separation.

**Metacognitive check:** NEW findings were produced. The strongest change from the starting frame is not that lifecycle hooks are absent—they are now officially documented—but that their trust model, command-only semantics, concurrent execution, cwd/root dependence, and lack of a semantic task-start event prevent treating the H1 event set as a complete guarantee. H2's “same freshness,” H3's strict single-writer lease, and H4's “authorship” also require narrower definitions.

**Blocking questions:** None.

**Recommendation:** Close Gather and authorize Extract. Extract should construct configurations that preserve the evidence-lane separation, next-start freshness boundary, split-brain recovery, and attribution/authentication distinction.

---
Stage complete: YES
Coordinator record: Gather accepted on 2026-08-08; Extract authorized.
