# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md)
> Goal: Make concurrent human and agent work in a synchronized TFW workspace conflict-resistant by moving normal lifecycle state and coordination to stable task-local, single-writer surfaces while retaining discoverability and Git provenance.

## Dimensions

No alternative is selected in Gather. Service/database alternatives remain as counterfactuals even though Phase A excludes them; they show which guarantees plain file sync cannot provide.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1. Catalogue persistence | manually maintained Task Board | generated on demand | low-churn persistent router plus generated live catalogue | no project catalogue |
| D2. Catalogue authority | catalogue is authority | task-local files are authority; catalogue is disposable | field-split authority | external tracker/database authority |
| D3. Status carrier | marker filenames | strict `status.yaml` | bounded `STATUS.md` | infer from artifacts or parent directory |
| D4. Human view | raw YAML/markers | generated Markdown/CLI view | bounded Markdown with machine-readable frontmatter | separately maintained human note |
| D5. Transition write | one scalar update at a stable path | marker create/delete/rename | whole task-directory move | append transition and derive state |
| D6. Journal storage | Markdown event table | JSONL | immutable event files | database event table |
| D7. Journal breadth | lifecycle only | lifecycle plus handoffs/gates/claims | all agent activity | rolling digest, not event history |
| D8. Journal retention | unbounded | bounded window plus archive | terminal compaction | separate phase/run journals |
| D9. Ownership | coordinator-only control and journal | one owner per field/file | lock-mediated multi-writer | unrestricted merge |
| D10. Edition contract | one shared schema | shared semantics, edition serialization | common kernel plus extensions | separate edition models |
| D11. Git topology | sync working files and `.git` | sync working files; local Git metadata | one landing clone plus sync-only peers | shared workspace without Git |
| D12. Isolation | separate task files in one tree | branches/worktrees | separate project copies | service leases/transactions |
| D13. View freshness | rebuild per read | explicit refresh with revision | event-triggered generation | visibly stale timestamped view |
| D14. Cold-start entry | root README | scan/query command | agent instruction with stable glob | external dashboard |

## Findings

### G1. Evidence boundary and name disambiguation

Evidence is labelled as follows: **S** = current source, test, or shipped template; **D** = current primary-repository documentation, not independently executed; **L** = local repository/history evidence. No third-party system was installed or executed.

- **GSD / Get Shit Done:** Taskwarrior/GTD projects and `glittercowboy/get-shit-done` are different projects. `gsd-build/get-shit-done` is now archived (GitHub showed read-only from 2026-06-26); its v1 file implementation remains historical source evidence. `gsd-build/gsd-2` says development moved; the active home observed on 2026-08-26 is [`open-gsd/gsd-pi`](https://github.com/open-gsd/gsd-pi). Current GSD Pi uses authoritative SQLite/WAL plus rendered Markdown, not v1's file authority.
- **BMAD:** [`bmad-code-org/BMAD-METHOD`](https://github.com/bmad-code-org/BMAD-METHOD), not wrappers.
- **Hermes:** [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent), not similarly named packages or mirrors.
- Additional current systems: [`github/spec-kit`](https://github.com/github/spec-kit), [`Fission-AI/OpenSpec`](https://github.com/Fission-AI/OpenSpec), and [`eyaltoledano/claude-task-master`](https://github.com/eyaltoledano/claude-task-master).

### G2. Current TFW read/write/ownership map

| Surface | Current role | Writers found | Readers/consumers found | Ownership/concurrency observation |
|---------|--------------|---------------|-------------------------|-----------------------------------|
| Root `README.md` Task Board | task identity/title, live status, artifact links | Plan sets `HL_DRAFT` (`.tfw/workflows/plan.md:52`); handoff sets `ONB` and later RF (`handoff.md:69` and continuation); review sets verdict/`KNW`/`DONE` (`review.md:116-126`); init creates/transitions it (`init.md:58-106,170,202`); standalone research may register `RES` (`research/base.md:37`) | AGENTS new-session path; all role skills; resume; release; docs generator; people | Independent tasks and successive roles converge on one line-oriented file. The writer changes by stage; there is no persistent single owner. |
| Task folder | stable task identity/group | coordinator/init at creation | all workflows and docs generator | Already isolates task artifacts; Full does not keep live status here. |
| HL / TS | contract and executable specification | Coordinator only | Researcher, Executor, Reviewer | Task-local, role-owned; not an operational log. |
| `research/iterN/*`, `RES.md` | research trace/synthesis | Researcher only | Coordinator/Planner | Iteration-isolated; not live coordination state. |
| ONB | executor briefing and gate questions | Executor; coordinator answers under protocol | Executor/Reviewer | Task-local, but only one stage's dialogue. |
| RF/evidence | execution claims/evidence | Executor | Reviewer/Coordinator | Terminal-stage trace; routine journal duplication would distort purpose. |
| REVIEW | independent verdict | Reviewer | Coordinator/knowledge/docs | Terminal-stage trace; not live status. |
| Generated tasks page | grouped task files plus status copied from README | `docs/scripts/gen_docs.py` | published docs users | `_generate_tasks_index()` regex-parses README's first three columns (`:324-341`); README remains upstream authority. |
| Git index/commit | staging and provenance | every committing role/session | reviewers and later archaeology | Index is shared repository/worktree metadata. It is not protected by task file ownership. |

Current board measurement: **60 task rows**; 40 have 8 cells and 20 have 9, while the header declares 8 columns. The board exposes ID, title-like description, status, and links. It does not consistently expose distinct goal, value, owner, dependency, or last-event fields. An on-demand catalogue cannot recover those absent fields merely by scanning terminal artifacts.

Cold-start dependence is structural:

- `AGENTS.md` requires the Task Board in new-session context.
- Installed TFW role skills put it in their load order.
- `/tfw-resume` combines board state with artifact existence.
- `/tfw-release` reads completed tasks from the board.
- `docs/scripts/gen_docs.py` copies status from it.

Integrity counterexample: README links TFW-54 as though it has an HL, but its task folder currently contains `PROPOSAL__TFW-54__agent_team_mode.md` and no HL. Persistent catalogues can therefore be discoverable but wrong; generated catalogues can also misclassify nonstandard task shapes.

### G3. Reconstruction of TD-81, TD-144, TD-175, TD-177, TD-178

| Debt | Concrete evidence | Exposed dimension |
|------|-------------------|-------------------|
| **TD-81** | `docs/scripts/gen_docs.py:309-366` groups pages, then regex-parses README to copy task name/status. It tolerates row-width drift only because it reads early columns. | Human table grammar is an implicit machine API. |
| **TD-144** | Two sessions shared one working tree and Git index. Commit `fbdf443`, titled for TFW-53/B, captured TFW-56's staged deletion of review mode files; verified with `git show --stat fbdf443`. | Independent working files do not protect a shared index; explicit-path staging is a separate control. |
| **TD-175** | `BLOCKED` had 0 uses across the then-measured 46 rows; actual stopped experiments used `REJECTED`. | A strict enum can be syntactically valid but operationally unused or misnamed. |
| **TD-177** | Header/row widths disagree; current count is 40 eight-cell and 20 nine-cell rows. Regex survives; a strict consumer need not. | Human-readable Markdown alone is not a stable machine protocol. |
| **TD-178** | The coordinator landed TFW-53/E board rows inside `8d9432b`, whose subject names TFW-58 and does not mention TFW-53; verified with `git show --stat 8d9432b`. | Coordinator ownership does not ensure task-specific provenance or commit granularity. |

The debts expose four non-equivalent controls: separate task files, persistent writer ownership, explicit-path staging, and one-task landing commits.

### G4. Current edition divergence

| Edition | Identity/status evidence | Writer model | Stable-path consequence |
|---------|--------------------------|--------------|-------------------------|
| Light | shared `TASKS.md` plus per-task `TRACE.md` | manual | common list remains a same-file surface. |
| Assisted | timestamp/handle/slug ID; task under `work/new|doing|review|done|blocked`; `TRACE.md` repeats `Статус:` | one writer per task/trace; explicitly no shared board/counter/trace | every transition moves the whole task folder **and** edits TRACE (`editions/02-assisted/AGENTS.md:65-77`). |
| Full | framework ID, root Task Board status, task-local role artifacts | writer changes by lifecycle role | task evidence is isolated, but status and Git index remain shared. |

Assisted's folder-move model is shipped local instruction, not inference. Its hooks are documented as unproven for durable orchestration; the supported baseline is manual/file discipline. H4 therefore begins from real differences in identity, state location, transition operation, duplication, and artifacts—not only transport and Git.

### G5. Read-only AFD evidence

Inspected without modification at `C:\Users\c0rpa\.codex\worktrees\10b2\ai-first-devices`:

- Root README retains the live Task Board and cold-start current status (`README.md:55,159`); `tasks/README.md` routes status back to root rather than duplicating it.
- `docs/DOCS_CONTRACT.md:34` separates hand-reviewed `DOCS_MAP` authority from disposable, rebuildable `DOCS_INDEX.jsonl` projection.
- Lifecycle is independent of location because one folder cannot encode independent axes (`:41`); IDs remain stable across path changes (`:55`).
- A concrete bloat fixture warns on a Task Board cell above about 180 words or README above about 1,800 words. AFD-23's cell was measured at 742 words before compression to 60; README moved from 2,889 toward 2,253 (`:93,101-108`).
- The owner made these size signals advisory, not hard gates. Evidence shows measurement detects bloat, not that advice prevents it.
- Evidence stays at its source (`:114`); search is a read-only projection (`:118`); structural checks do not prove arbitrary prose true (`:122`).

AFD supplies local evidence for stable IDs + one semantic owner + disposable view + source references. It also supplies counter-evidence: an always-load persistent board accumulated a 742-word cell before cleanup.

### G6. Primary-system comparison

| System | State/catalogue | History | Concurrency | Evidence level and primary source |
|--------|-----------------|---------|-------------|-----------------------------------|
| **GSD v1, archived** | persistent `.planning/STATE.md` and `ROADMAP.md`; every workflow reads state first | bounded digest of recent decisions, blockers, session continuity; template says under 100 lines, 3-5 recent decisions, active blockers | `STATE.md.lock` with `O_EXCL`, stale detection and read-modify-write | **S:** [`state.cjs`](https://github.com/gsd-build/get-shit-done/blob/main/get-shit-done/bin/lib/state.cjs), [`state.md` template](https://github.com/gsd-build/get-shit-done/blob/main/get-shit-done/templates/state.md), [`roadmap.md`](https://github.com/gsd-build/get-shit-done/blob/main/get-shit-done/templates/roadmap.md). Historical lineage only. |
| **GSD Pi, current** | `.gsd/gsd.db` is runtime authority; Markdown is rendered projection | DB holds milestones/tasks/decisions/summaries | SQLite/WAL, leases and worktrees; explicitly local disk and single-host; `gsd.db*` over network/cloud sync unsupported | **D/current primary:** [`auto-mode`](https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/auto-mode.md), [`parallel orchestration`](https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/parallel-orchestration.md). Non-transferable service counterexample. |
| **BMAD Method** | central `sprint-status.yaml`; strict epic/story/retro vocabularies; status command recommends next story | result detail remains in story/spec artifacts | deterministic generator normalizes legacy states and merges/preserves progress; central YAML is still one file | **S:** [`sprint_plan.py`](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/plan/bmad-sprint-planning/scripts/sprint_plan.py), [`sprint-planning skill`](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/plan/bmad-sprint-planning/SKILL.md). Source present, not run here. |
| **Hermes Agent** | tasks/status/claims/runs in `~/.hermes/kanban.db`; CLI/tools/REST/UI share it | append-only `task_events`; 400-character event summary plus full run metadata | WAL and `BEGIN IMMEDIATE` claims; local process profiles | **S+D:** [`Kanban test`](https://github.com/NousResearch/hermes-agent/blob/main/tests/hermes_cli/test_kanban_core_functionality.py), [`Kanban reference`](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/kanban.md). DB semantics do not transfer to plain sync. |
| **GitHub Spec Kit** | branch feature directory with spec/plan/research/contracts/`tasks.md`; strict task checkboxes and exact paths | checklist progress; no project event journal located | `[P]` only for non-conflicting work; same-file work sequential | **S:** [`tasks command`](https://github.com/github/spec-kit/blob/main/templates/commands/tasks.md), [`tasks template`](https://github.com/github/spec-kit/blob/main/templates/tasks-template.md), [`implement command`](https://github.com/github/spec-kit/blob/main/templates/commands/implement.md). |
| **OpenSpec** | per-change proposal/specs/design/`tasks.md`; CLI reports artifact state | change artifacts are trace; no general journal located | change folders isolate work, but archive moves the whole directory | **D/current primary:** [`workflows.md`](https://github.com/Fission-AI/OpenSpec/blob/main/docs/workflows.md); archive warns but does not block on incomplete tasks. |
| **Claude Task Master** | central structured `tasks.json`; `list`/`next` create on-demand views | task details, not a strict append-only journal | `set-status` mutates central JSON; generated task text files require regeneration | **D/current primary:** [`README-task-master.md`](https://github.com/eyaltoledano/claude-task-master/blob/main/README-task-master.md). |

Observed patterns, not selections:

1. Persistent discoverable state is common; no inspected system reconstructs project meaning solely from terminal artifacts.
2. Strictness exists in YAML/JSON, Markdown/frontmatter, and databases. Parser/writer contracts and ownership matter independently of extension.
3. Central state is normally protected by a lock, database transaction, or serialized CLI—guarantees outside bare cross-device file sync.
4. GSD v1 is direct counter-evidence that human-readable bounded Markdown cannot be strict; its concurrency safety nevertheless depended on source-level locking.
5. Rigorous event history is narrow. Hermes types lifecycle/claim/run events and caps summaries; GSD keeps a digest and references deeper records.
6. Whole-directory moves in OpenSpec and Assisted conflict with TFW-60's frozen stable-path outcome.

### G7. File-sync semantics

| Scenario | Google Drive for desktop | OneDrive/SharePoint | Dropbox | Plain-sync evidence floor |
|----------|--------------------------|---------------------|---------|---------------------------|
| Independent files | new files/folders sync across devices | file-oriented sync | file-oriented sync | Different task files reduce same-file collisions; propagation order is not a transaction. |
| Same-file concurrent/offline edit | incompatible changes can leave an edited copy under original parent/root or Lost & Found | non-Office conflicts keep both versions and append device name; up to five | creates named conflicted copy for simultaneous/offline/open-file edits; manual merge | Conflict copies/last-writer behavior are normal. |
| Offline reconnect | mirror retains local files; stream uses cache; unsynced recovery may use desktop recovery/Lost & Found | local/server copies may require resolution/resync | offline edit explicitly causes conflict copy | No distributed lock or cross-file happens-before survives disconnect. |
| Move/rename | moved/renamed Drive root requires reconnect; move/delete plus local edit may relocate the copy | renaming established synced root can break relationship | shared-folder rename can be member-local; some moves break membership; selective-sync folder conflicts exist | Directory move is not an atomic state transition across clients. |
| Cross-file transaction | none documented | none documented | none documented | Treat related file changes as independently visible and reorderable. |

Primary sources:

- Google: [`Fix problems in Drive for desktop`](https://support.google.com/drive/answer/2565956?hl=en); [`Drive for desktop advanced guide`](https://support.google.com/drive/answer/16631477?hl=en).
- Microsoft: [`Resolve sync issues in OneDrive for work or school`](https://learn.microsoft.com/en-us/troubleshoot/sharepoint/sync/troubleshoot-sync-issues).
- Dropbox: [`What's a conflicted copy?`](https://help.dropbox.com/organize/conflicted-copy); [`Rename or move a shared folder`](https://help.dropbox.com/organize/rename-move-shared-folder); [`selective sync conflict`](https://help.dropbox.com/sync/selective-sync-conflict).

The final column is an architectural inference from primary vendor contracts, not a claim that providers share an algorithm. Reliable distributed locks, compare-and-swap, ordered multi-file propagation, and atomic directory transactions were not documented.

### G8. Git topology evidence

- Linked worktrees share repository data but have per-worktree `HEAD`, `index`, and other state ([`git-worktree`](https://git-scm.com/docs/git-worktree.html)).
- A linked worktree's `.git` file points into the main repository's administrative directory; refs may be shared while index/HEAD are per-worktree ([`gitrepository-layout`](https://git-scm.com/docs/gitrepository-layout)).
- Git's worktree lock protects administrative pruning for temporarily unavailable worktrees; it is not a cloud-sync write lock.

Observed consequences:

1. Syncing `.git` or a worktree `.git` pointer also syncs or invalidates machine-local administrative paths/state; Git documentation does not present cloud-sync replication of `.git` as a collaboration protocol.
2. Local Git metadata separates indexes but does not decide who commits shared working-file changes.
3. TD-144 is an index-sharing failure; TD-178 is a landing/provenance failure. Separate indexes solve only the former.
4. Worktrees provide same-host isolation, not cross-host file-sync transactions. Current GSD Pi reaches the same single-host boundary.

### G9. Deep-mode evidence loops

| Loop | Hypothesis pressure | Counter-evidence found | Revised unknown carried forward |
|------|---------------------|------------------------|----------------------------------|
| 1. Internal + AFD | task-local sources can support a derived view | README uniquely carries live aggregate fields and all cold-start paths read it; AFD still retains a persistent board | Which low-churn entry and task-local fields preserve zero-tool human and agent discovery? |
| 2. Workflow systems | strict YAML/markers and a separate journal might be inherently safer | GSD ships bounded Markdown plus lock; DB systems depend on non-transferable transactions; generated secondary files drift | Which carrier combines parser strictness, human clarity, stable path, and persistent ownership? How narrow must journal events be? |
| 3. Sync + Git | single-writer files plus Git provenance might be sufficient | offline forks, move/edit ambiguity, no multi-file ordering, and TD-178's cross-task landing remain | What exact one-file transition, owner, staging, and landing rules are jointly necessary? |

Provisional evidence pressure only—final verdicts are deferred to Extract/Challenge:

| Hypothesis | Supporting observation | Counter-observation/open gap |
|------------|------------------------|------------------------------|
| H1 | task-local sources plus generated views isolate writers | persistent cold-start sources are universal in the sample; TFW task folders lack some board fields; zero-tool usability untested |
| H2 | BMAD proves strict YAML; current board grammar drifts | GSD proves bounded Markdown can be parsed/locked; marker operations add rename/create-delete behavior |
| H3 | Hermes proves typed, narrow event history; AFD proves source/reference separation | no file-first example proves an unbounded journal; grammar, references and retention remain open |
| H4 | editions share identity/lifecycle/owner/result/resume concepts | Assisted and Full currently differ in ID, path semantics, transition operation and artifact model, not only transport |

## Checkpoint

| Found | Remaining for Extract/Challenge |
|-------|---------------------------------|
| Current TFW read/write/ownership map and all five debt reconstructions | Minimal field-level shared contract and one owner per field. |
| Read-only AFD authority/projection/bloat evidence | Transferable patterns without importing debt or knowledge architecture. |
| Seven-system comparison with current GSD lineage and evidence levels | Coherent configurations and cold-start/human tests. |
| Provider same-file/offline/move semantics | Testable plain-sync invariants without distributed-transaction claims. |
| Git index/worktree evidence separated from task ownership | Local-`.git` landing model, explicit-path staging, and own-task commit rules. |
| Counter-evidence against simple H1-H4 forms | Exact carrier, journal grammar/reference/retention, and edition migration boundary. |

**Evidence state:** internal and AFD observations are local/source-level. GSD v1 lock, BMAD parser, Hermes test, and Spec Kit templates are primary source-level evidence. GSD Pi, OpenSpec, Task Master, and provider semantics are primary repository/vendor documentation not executed here. Debt and knowledge architecture remain excluded.

**Recommendation at this gate:** proceed to Extract. The decision dimensions, external coverage, counter-evidence, and remaining gaps are explicit; another Gather pass would widen product count rather than close a Phase-A variable.

**Questions for the Coordinator:** none. Existing constraints are sufficient. Service/DB alternatives should remain counterexamples, not candidates that widen Phase A.

**Files written at this gate:** `research/iter1/1_briefing.md`; `research/iter1/2_gather.md`.

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] At least one hypothesis tested and counter-evidence sought (deep mode)?
- [x] Three Gather loops completed?

Stage complete: YES
→ User decision: WAIT — Coordinator must approve Extract or redirect the evidence gap.
