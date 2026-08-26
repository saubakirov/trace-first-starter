# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md)
> Goal: Make concurrent human and agent work in a synchronized TFW workspace conflict-resistant by moving normal lifecycle state and coordination to stable task-local, single-writer surfaces while retaining discoverability and Git provenance.

## Dimensions

No alternative is selected in Gather. C2–C5, G-C and service/database designs appear only where new evidence tests a named survivor invariant; their appearance below does not reopen them.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1. Portfolio entry | permanent root router + persisted derived index | permanent router + on-demand view | task-folder scan from a fixed glob | external/service catalogue |
| D2. Derived-index condition | normal and digest-matched | absent | structurally valid but stale | malformed or partially written |
| D3. Task-control shape | strict valid `status.yaml` | recognized legacy without control | malformed or unsupported control | service/database record |
| D4. Reader behaviour | trust index | re-read task authority before acting | ignore/quarantine index and scan controls | best-effort inference from artifacts |
| D5. Usability evidence | fresh-agent runtime | researcher usability heuristic | genuinely observed non-technical-human runtime | UI or file-browser instrumentation without a human participant |
| D6. Status field admission | required shared-kernel field | conditionally required field | edition/profile extension | derived or omitted field |
| D7. YAML acceptance | full YAML 1.2 | strict application subset | frontmatter/Markdown grammar | JSON/database schema |
| D8. Recovery authority | current state owner | predeclared recovery authority with epoch increment | timestamp/latest-writer selection | lock/lease/transaction service |
| D9. Journal/snapshot visibility | aligned | journal ahead | snapshot ahead | divergent or malformed branch |
| D10. Journal segmentation | count ceiling | encoded-byte ceiling | combined first-hit ceiling | time/phase/manual boundary |
| D11. Landing trace order | post-commit `landed` event | commit-only landing evidence | pre-landing handoff/manifest plus commit | second commit containing landing event |
| D12. Git profile | G-B one landing machine | guarded G-A external administration | per-peer Git/worktree G-C | no Git landing |
| D13. Git scope gate | literal declared allowlist | task-directory pathspec | whole worktree/index | manifest digest plus exact allowlist |
| D14. Migration action | preserve path and import verified facts | move/normalize legacy folder | exclude malformed/nonstandard task | create new task and retain predecessor reference |
| D15. Edition boundary | shared semantic kernel + artifact profiles | shared serialization and semantics | deterministic adapters over distinct carriers | separate Full and Assisted task models |

## Findings

### G1. Evidence taxonomy and claim boundary

This iteration uses seven non-interchangeable evidence classes.

| Label | Meaning in this trace | Available in Gather? |
|-------|-----------------------|----------------------|
| **FA** | fresh Codex agent given only a fixture entry path; read-only runtime observation | yes, four index conditions across three fresh agents |
| **UH** | researcher judgment that a route is visible or understandable; no participant observation | yes |
| **NH** | genuinely observed non-technical-human behaviour | **no** |
| **DF** | deterministic local fixture exercising an explicitly encoded rule | yes |
| **RR** | read-only observation of this repository or a temporary Git runtime | yes |
| **PS** | current primary specification, vendor contract or upstream repository source | yes |
| **PR** | actual synchronized-provider runtime, including offline/reconnect/conflict-copy behaviour | **no** |

DF can show that a proposed parser or recovery rule is deterministic under its own model; it cannot show that a provider will expose files in that order. PS can establish documented failure semantics; it cannot establish that the current machine reproduced them. FA can establish an AI cold-start route; it cannot stand in for NH.

### G2. Reproduction environment, commands and immutable result summaries

The unique fixture root is outside all tracked project paths:

```text
E:\TEMP\tfw60_iter2_e48d40f17410468387a67a8ca02120cc
```

Runtime versions were Python 3.13.5, PyYAML 6.0.3 and Git 2.42.0.windows.1. The harness and result hashes are:

| File | SHA-256 |
|------|---------|
| `harness.py` | `BE36C6B1E6217A1F728705A7C1001E6AA6EB73ECA29683A408EB5396E4AA48DE` |
| `t1/t1_results.json` | `785F1671CC3651EE85422D6FD4AF5F29041EE7344E1112B089930B937CBD0CDF` |
| `t2/t2_results.json` | `FC31B38B4681A2E3765C246FCBAE8283EC9B095A38E6DF715758A35F3E8BF092` |
| `t3/t3_results.json` | `7DBAFEBA78602F9113CC8E4C9D52515398DFBE2FE088B970E871BE41158B996A` |
| `legacy_census.json` | `59E886851FD98C68836EEBA443592A0BBEDC0C515FA9FB304BB5FFB74FCC1D32` |

Commands, run from the repository root:

```powershell
python "E:\TEMP\tfw60_iter2_e48d40f17410468387a67a8ca02120cc\harness.py" build-t1
python "E:\TEMP\tfw60_iter2_e48d40f17410468387a67a8ca02120cc\harness.py" run-t1
python "E:\TEMP\tfw60_iter2_e48d40f17410468387a67a8ca02120cc\harness.py" run-t2
python "E:\TEMP\tfw60_iter2_e48d40f17410468387a67a8ca02120cc\harness.py" census
python "E:\TEMP\tfw60_iter2_e48d40f17410468387a67a8ca02120cc\harness.py" run-t3
```

All five commands exited 0. The T1 builder reported exactly 100 task directories. The read-only census made no repository change. `git status --short` after fixture execution showed only the already allowed untracked `research/iter2/` directory.

### G3. T1 deterministic 100-task corpus and four catalogue conditions

The corpus contains 80 valid controls, 10 legacy shapes and 10 malformed controls. The valid set uses all five lifecycle values and includes task `TFW-042`, whose value is “Restore failed checkouts without losing decision traces” and whose authoritative lifecycle is `blocked`. Legacy cases include HL-only, proposal-without-HL, Assisted-style TRACE-only, rejected post-mortem, TS/RF without HL, empty, research-only, uppercase phase, README-only and non-contract `status.json` shapes.

The malformed set independently exercises duplicate mapping keys, unsupported schema version, terminal-without-reference, anchors/aliases, custom tags, unknown lifecycle, task/folder ID mismatch, missing journal head event, YAML syntax failure and a divergent duplicate event ID. The strict reader classified all 100 exactly as constructed: 80 valid, 10 legacy, 10 malformed. Regenerating the index twice produced identical content and SHA-256 `d818e00e52903f1f78d8032c12dd6a0fd155e3b5e95f43f1ddc7a1506cd49f8b`.

| Index condition | Deterministic result | Authority effect | Discovery effect |
|-----------------|----------------------|------------------|------------------|
| normal | 100 unique IDs; source count and digest valid; regeneration matched | task control and index agreed for `TFW-042` | derived view supplied portfolio route |
| absent | index missing; fallback scan still returned 80/10/10 | no state loss | portfolio ranking degraded; task scan required |
| stale | index said `active`; task control said `blocked`; re-read detected mismatch | task control won | stale view could misroute a reader that failed to re-read |
| malformed | non-numeric source count, broken digest and truncated table | view supplied no usable state | scanner could recover controls; the view itself was not partially trusted |

This DF result confirms only that C1-R's encoded authority rule survives these fixtures. It does not prove that every generator, Markdown renderer or sync client will preserve the same bytes.

### G4. Fresh-agent cold start versus file-browser and human evidence

Three context-free Codex agents were given only entry paths and told not to generate, edit or consult prior TFW-60 context.

| Condition | FA route and observed result | Timing caveat |
|-----------|------------------------------|---------------|
| normal | `README.md` → `tasks/INDEX.md` → `TFW-042/status.yaml`; returned ID, `blocked`, owner, next action/ref and authority correctly | 7.67 s wall clock |
| absent | scenario README → enumerate task folders/fixed controls → search 90 controls → open `TFW-042/status.yaml`; also reported 10 control-less legacy and 10 malformed folders | 68.307 s included the requested anomaly audit, so it is not directly comparable to normal |
| stale | scenario README → stale index → re-read task control; reported the `active`/`blocked` contradiction and selected `blocked` | 160 ms summed command time; about 1.1 s tool wall time |
| malformed | scenario README → malformed index → read-only fixed-control search → task control; reported invalid metadata and incomplete table | 224 ms summed command time; about 1.7 s tool wall time |

All four FA runs found one unambiguous target. The normal agent also observed mojibake for em dashes in its console rendering; IDs and links remained usable. The absent run demonstrates an important cost difference: authority recovery is possible, but a view outage transfers classification and search work to the reader.

The fixture also supplies a zero-command *route design*: root README links the persisted Markdown index, whose task row can link the fixed control. That remains UH. No non-technical participant opened the fixture in a file browser, interpreted YAML or changed a state. NH is therefore unavailable, and H2's non-technical-human half remains an acceptance gap rather than a simulated result.

### G5. Every proposed status field has a named reader and trigger, but necessity remains uneven

The fixture made all 20 iteration-1 fields structurally required so omission could not silently change meaning. That tests strictness, not field necessity. The field-by-field pressure map is:

| Field | Named reader | Creation/change trigger | Counter-pressure carried to Extract |
|-------|--------------|-------------------------|-------------------------------------|
| `schema_version` | validator/migrator | create; every parse; explicit migration | required for fail-closed evolution; full YAML versioning alone is insufficient |
| `task_id` | catalogue, link resolver, Git scope gate | create; immutable | folder identity duplicates it but legacy/nonstandard paths make the explicit check useful |
| `goal_summary` | portfolio human/agent | create; approved goal amendment | derived systems can read artifact titles, but current proposal/HL shapes are not uniform |
| `value_summary` | portfolio prioritizer | create; approved value amendment | no current artifact naming convention reliably supplies value |
| `goal_ref` | scope reader/migrator | create; amendment; legacy import | TFW-54/57/58/59 require proposal refs; TFW-1/2/48/49 show that HL cannot be assumed |
| `lifecycle` | resume, release, catalogue | every material transition | comparable systems sometimes derive state from artifacts/checklists, so separate authority must justify its recovery value |
| `workflow_stage` | workflow router | dispatch, handoff, phase/gate transition | likely profile-specific; Assisted and Full stage vocabularies differ |
| `status_since` | stale-work view | lifecycle or stage change | informative only; cannot resolve branches or substitute for epoch/event order |
| `waiting_on` | owner and resume reader | enter/leave `waiting` or `blocked` | conditional mapping is necessary only for those states; no free-form dependency narrative |
| `next_action` | cold-start reader | handoff or transition | current active systems often derive “next” from checklists/graphs; explicit value avoids parsing heterogeneous legacy artifacts |
| `next_ref` | cold-start reader | same trigger as next action | prevents copying gate detail; must allow proposal/non-HL refs |
| `terminal_outcome` | release/catalogue | enter terminal | retained rejected fixture shows `done` cannot be the only terminal meaning |
| `terminal_ref` | release/auditor/human | enter terminal | required to distinguish an authoritative rejection from a status assertion |
| `state_owner` | write guard/reconciler | create or ownership change | an identity label is not authentication and does not prevent offline writes |
| `owner_epoch` | reconciler/write guard | create at 1; increment through authorized recovery | fixtures distinguish stale epochs; same-epoch divergence still stops and needs authority |
| `ownership_profile` | role/file validator | create or versioned profile migration | may be project-default/derived, but a per-task version pin prevents rules changing underneath history |
| `roles` | dispatcher/artifact ownership validator | assignment and handoff | strongest minimization candidate: active comparables omit it, and profile-owned artifacts may already carry assignment; Full/Assisted cardinality differs |
| `last_event_id` | reconciliation/resume | every event reflected in snapshot | essential to detect snapshot ahead; a timestamp cannot replace it |
| `journal_head` | bounded-history loader | segment rollover | a numeric naming convention could derive it, but explicit head avoids directory-order inference and supports compatibility |
| `updated_at` | view/cache freshness reader | every valid snapshot rewrite | useful projection metadata; must never act as conflict authority and may be derivable at generation time |

No field is removed in Gather. `roles`, `workflow_stage`, `ownership_profile`, the two timestamps and `journal_head` have the clearest shared-kernel-versus-profile/derived question. Conversely, the fixture directly couples `owner_epoch` and `last_event_id` to deterministic stop/recovery behaviour.

### G6. Strict YAML evidence and comparable active systems

The [YAML 1.2.2 specification](https://yaml.org/spec/1.2.2/) calls mappings unordered associations with unique keys, but YAML also supports aliases, anchors, tags and directives. Therefore “strict YAML” is an application profile enforced before/while constructing values, not a property obtained from the `.yaml` extension. The fixture rejected duplicate keys and those extension tokens before accepting the closed field set.

Active-system counter-evidence was gathered from current primary repositories:

| System | Current authority/view pattern | Relevant counter-evidence | Transfer boundary |
|--------|--------------------------------|---------------------------|-------------------|
| GitHub Spec Kit | strict Markdown checkbox tasks with exact paths; task progress is updated in `tasks.md` | machine-usable Markdown and same-file serialized work can function without YAML | [`tasks`](https://github.com/github/spec-kit/blob/main/templates/commands/tasks.md) and [`implement`](https://github.com/github/spec-kit/blob/main/templates/commands/implement.md) do not claim offline multi-host file-sync recovery |
| OpenSpec | CLI derives artifact status from an artifact graph and exposes text/JSON views | a separate live status file is not universally necessary | [`CLI`](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md) operates over a standardized change-artifact model unlike this legacy corpus |
| GSD Pi | project-root SQLite/WAL is authority; Markdown is projection; fencing leases coordinate work | central transactional state and leases solve classes C1-R must only detect/reconcile | [`parallel orchestration`](https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/parallel-orchestration.md) explicitly limits the design to local disk/single host, not network or cloud sync; [`architecture`](https://github.com/open-gsd/gsd-pi/blob/main/docs/dev/architecture.md) makes the DB authoritative |
| BMAD Method | deterministic `sprint_plan.py` generates, validates and reports central sprint YAML | central YAML plus one tool is an active alternative; its skill permits a manual “best judgment” fallback when the script fails, unlike C1-R fail-closed parsing | [`sprint planning skill`](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/plan/bmad-sprint-planning/SKILL.md); issue [`#2553`](https://github.com/bmad-code-org/BMAD-METHOD/issues/2553) is a repository report of regenerated status loss, not runtime evidence collected here |
| GSD Pi Git profile | worktrees/branches and task trailers integrate DB state with Git | richer provenance is possible when one local orchestrator owns DB and worktrees | [`Git strategy`](https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/git-strategy.md) inherits the single-host boundary |

These sources challenge the claim that strict YAML is inherently superior or that a persisted index is universally required. None defeats C1-R's named Phase-A invariant: authority must remain task-local, recoverable under unordered plain-file propagation, compatible with heterogeneous legacy artifacts and usable without adding a service. C2–C5 remain comparison rows, not reopened families at Gather.

### G7. T2 deterministic recovery matrix

The T2 fixture encodes event IDs, owner epochs, a snapshot pointer and a closed minimal record check. Its results are:

| Case | DF outcome | Observation |
|------|------------|-------------|
| aligned snapshot/journal | `ACCEPT` | two unique events and exact pointer |
| journal ahead, current owner/epoch | `RECOVERABLE` | one valid pending event identified |
| snapshot points to missing event | `STOP` | snapshot cannot establish its claimed history |
| identical duplicate ID | `ACCEPT` | normalized complete records matched |
| divergent duplicate ID | `STOP` | ID equality did not erase payload divergence |
| malformed event | `STOP` | incomplete fields were not guessed |
| old owner reconnect after epoch 2 | `QUARANTINE` | epoch-1 branch retained but could not become current |
| coordinator disappears; new writer uses same epoch without recovery | `STOP` | identity/timestamp did not authorize the branch |
| predeclared authority changes owner and increments epoch | `ACCEPT` | `ownership_changed` and snapshot aligned |
| terminal rejected | `ACCEPT` | terminal outcome retained `POSTMORTEM.md` reference |

This supports internal determinism for `owner_epoch`, authorized recovery, event-first/snapshot-second, full-record duplicate comparison and rejected retention. It does **not** demonstrate distributed mutual exclusion, identity authentication, actual conflict-copy naming or provider reconnection. Same-epoch divergent valid branches still require a declared recovery ruling; “highest epoch wins” is valid only when the epoch change itself is authorized and chained.

### G8. T2 numerical hypotheses and rollover measurements

The summary test separated code points from encoded bytes:

| Sample | Summary code points | Summary UTF-8 bytes | Complete JSONL record bytes |
|--------|---------------------|--------------------|-----------------------------|
| 60 ASCII | 60 | 60 | 237 |
| 120 Cyrillic | 120 | 240 | 417 |
| 240 emoji | 240 | 960 | 1,137 |
| 241 ASCII | 241 | 241 | 418 |

A 240-code-point ceiling is reproducible as a semantic text bound, but it is not a storage bound. The same allowed length changed complete-record size by nearly 5× between 60 ASCII and 240 emoji; language, references and record overhead matter.

The 235-event mixed-Unicode history was 64,222 bytes. Under the combined first-hit rule:

| Event ceiling | Byte ceiling | Observed segment event counts | First pressure |
|---------------|--------------|-------------------------------|----------------|
| 50 | 16/32/64 KiB | 50, 50, 50, 50, 35 | count |
| 100 | 16 KiB | 60, 60, 60, 55 | bytes |
| 100 | 32 or 64 KiB | 100, 100, 35 | count |
| 200 | 16 KiB | 60, 60, 60, 55 | bytes |
| 200 | 32 KiB | 120, 115 | bytes |
| 200 | 64 KiB | 200, 35 | count |

Local JSONL parsing over 50 repeats measured median/p95 0.3196/0.3537 ms for 100 events (26,992 bytes), 3.2541/4.7608 ms for 1,000 (270,893 bytes), and 40.9655/49.2415 ms for 10,000 (2,718,895 bytes). These are one Python/runtime/machine measurements, not acceptance budgets. Snapshot plus last event was 408 bytes versus 64,222 bytes for the 235-event full history, a 157.41× byte ratio.

The measurements support a *combined* count-and-byte mechanism and bounded cold start. They do not establish 240/100/32 KiB as user-facing defaults. The three numbers remain hypotheses pending expected workload, renderer/editor behaviour and real provider evidence.

### G9. Provider contracts versus provider runtime

Current vendor documentation establishes failure classes only:

- [Google Drive for desktop advanced configuration](https://support.google.com/drive/answer/16631477?hl=en) distinguishes streaming/mirroring and warns that unsynced cache must complete before switching modes; [Drive troubleshooting](https://support.google.com/drive/answer/2565956?hl=en-GB) documents recovery of unsynced files/Lost & Found.
- [Microsoft OneDrive/SharePoint sync troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/sharepoint/sync/troubleshoot-sync-issues) documents non-Office conflicts that retain both versions, append a device name and require manual choice.
- [Dropbox conflicted copies](https://help.dropbox.com/organize/conflicted-copy) documents simultaneous, offline and open-file conflict copies and manual merging.

No synchronized folder, offline device, reconnect, conflict copy or vendor UI was exercised in iteration 2 Gather. PR is unavailable. The portable evidence floor remains independent-file propagation with no assumed cross-file order, lock or transaction. Whether provider-created branches preserve enough bytes/names for the proposed recovery adapter is a TS acceptance gap.

### G10. T3 G-B literal scope and attribution fixture

The temporary Git repository began at `a52404dd9d3c07341017afffbf11e1a7c3d78cb3`. Peer changes then touched TFW-001 and unrelated TFW-002 files. Key commands included:

```powershell
git --literal-pathspecs add -- tasks/TFW-001/file[1].txt tasks/TFW-001/result.txt
git diff --cached --name-only
git diff --name-only -- tasks/TFW-001
git commit -m "[codex/TFW-001/phase-a/landing-owner] land fixture task`n`nTFW-Producer: agent-alpha`nTFW-Landing-Owner: coordinator-beta"
git diff-tree --no-commit-id --name-only -r HEAD
```

Observed RR results:

- Literal staging selected the square-bracket filename and result exactly; the unrelated TFW-002 edit remained unstaged.
- A synchronized edit to the already staged TFW-001 result appeared in the working-versus-index recheck and made the drift gate stop; restaging was explicit.
- Commit `ab543f6026dc9029bff4d3d5c675fe52ece5cf06` contained exactly the two allowed TFW-001 paths. The commit retained separate `TFW-Producer: agent-alpha` and `TFW-Landing-Owner: coordinator-beta` trailers.
- Intentionally staging TFW-002 later was detected as an extra staged name.
- Unrelated working changes survived the one-task commit; a clean *whole worktree* is therefore neither necessary nor expected, while the declared task paths and staged set must be exact.

The official Git contracts support the mechanism: [`git-add`](https://git-scm.com/docs/git-add) documents literal/pathspec controls and `--`; [`git-diff`](https://git-scm.com/docs/git-diff) distinguishes cached/staged comparison. Runtime used Git 2.42; the currently published documentation may describe newer Git, so TS must verify the project's minimum supported version.

### G11. T3 guarded G-A preflight has a pinning requirement

The executable preflight used absolute `--git-dir`, absolute `--work-tree`, `rev-parse --absolute-git-dir --show-toplevel --git-path index`, an index-location check and a synchronized-root `.git` check. Official [`git-rev-parse`](https://git-scm.com/docs/git-rev-parse), [`gitrepository-layout`](https://git-scm.com/docs/gitrepository-layout) and [`git-worktree`](https://git-scm.com/docs/git-worktree) define those probes and show that linked worktrees use a `.git` file pointing to machine-local administration.

| Condition | RR result |
|-----------|-----------|
| correct external Git directory/worktree/index | passed |
| missing Git directory | return 128; failed closed |
| index redirected inside synchronized root | failed closed |
| unexpected `.git` file in synchronized root | failed closed |
| linked worktree | `.git` was a file containing an absolute administrative pointer |
| wrong but internally consistent worktree argument | the generic probe passed relative to the supplied wrong path |

The last row is new counter-evidence against an underspecified G-A preflight: asking Git what worktree corresponds to the caller-supplied `--work-tree` cannot prove that the caller supplied the *configured* synchronized root. The gate must compare results against separately pinned expected `GIT_DIR`, worktree and index paths from local setup; otherwise a wrong target can be self-consistent. This tightens G-A's invariant and failure contract but does not reopen G-C or defeat the optional guarded profile.

### G12. `landed` ordering alternatives expose different gaps

The T3 repository exercised three orders.

| Order | Observed strength | Observed gap |
|-------|-------------------|--------------|
| post-commit `landed` event | event can contain the actual commit hash | task became dirty immediately; a crash can leave the commit without its event; landing the event requires another commit |
| commit-only with producer/landing-owner trailers | landing is atomic in Git and worktree remains no dirtier than unrelated peer changes | file-only resume cannot observe landing without reading Git |
| pre-landing handoff/manifest committed with result | manifest, result and attribution land atomically in commit `7958941ff457786de8208bf8d051d6bc9c09df9f`; manifest digest can be placed in commit trailer | manifest cannot contain its own future commit hash; Git remains landing authority |

A fourth alternative—commit the post-commit event in a second commit—would make history observable in files but necessarily creates an intermediate state and two-commit release scope. Gather does not choose among them. It does show that an event whose semantics assert completed Git landing is structurally post-commit and cannot be in the commit it describes without a circular future-hash problem.

### G13. T3 read-only Full/Assisted legacy census

The current repository, not a synthetic copy, yielded:

| Observation | Count/detail |
|-------------|--------------|
| Full task directories | 51 |
| root task rows | 60 |
| board row widths | 39 rows with 8 cells; 21 with 9 while the header still declares 8 |
| master HL files | 43 |
| task directories without a master HL | TFW-1, TFW-2, TFW-48, TFW-49, TFW-54, TFW-57, TFW-58, TFW-59 |
| proposal without master HL | TFW-54, TFW-57, TFW-58, TFW-59 |
| task controls named `status.yaml` | 0 |
| modern research controls | 10 |
| board task-folder link missing | TFW-36 |
| nonexistent board HL links | TFW-36, TFW-51 anchor, TFW-52 anchor twice, TFW-54 HL |
| phase directory spellings | `PhaseA` 5, `PhaseB` 5, `PhaseC` 3, `PhaseD` 2, `phase-a` 5, `phase-b` 5, `phase-c` 3, `phase-d` 1, `phase-e` 1 |

The board's 8/9-cell split is current malformed-input evidence for any strict table consumer, not a reason to rewrite history. TFW-54 proves that a `HL_DRAFT` row and HL link cannot justify inventing an HL; the existing proposal is the verified scope reference. The same compatibility rule applies to 57–59.

Current Assisted instructions are also counter-evidence to a carrier-only migration assumption. They define status by moving a whole task folder among `work/new|doing|review|done|blocked` **and** updating `TRACE.md`, with one writer per task trace and no shared board. Only `work/new` currently exists in the shipped edition tree, so the other roots are a documented contract, not observed active-task runtime. Migration that moves old folders to a neutral root would break references and create sync rename risk; a compatibility resolver must preserve paths, record verified facts and report unknowns.

### G14. Shared semantics versus edition profiles

The census finds representation differences, not evidence that Full and Assisted need different meanings for identity, lifecycle/outcome, next action/reference, current state owner/epoch or management events.

| Layer | Shared semantic candidate | Full profile evidence | Assisted profile evidence |
|-------|---------------------------|-----------------------|---------------------------|
| identity | stable task ID and immutable history link | `TFW-N` directory/board | timestamp-handle-slug naming |
| lifecycle/outcome | new/active/waiting/blocked/terminal + done/rejected | board/workflow stages and REVIEW | parent folder plus TRACE status; no native rejected kernel located |
| control artifact | one authoritative snapshot meaning | proposed fixed status control | legacy folder+TRACE must be adapted without moving |
| journal meaning | typed management event with artifact refs | Coordinator/role handoffs | task steward/owner handoffs |
| transport | no semantic authority | Full local repository plus collaboration modes | filesystem/manual/Codex-assisted paths |
| Git | landing provenance | G-B baseline, optional guarded G-A | profile may omit direct peer Git and still preserve producer identity in artifacts |

Active GSD Pi supplies a useful artifact-profile counterexample: the same user-visible task semantics can be stored in SQLite and rendered to Markdown, but its single-host DB guarantee is not transferable. The iteration-2 evidence therefore keeps semantic contract, artifact serialization, transport and Git profile as separate dimensions. No new evidence defeats the shared-kernel invariant; exact optional/profile fields remain for Extract.

### G15. Three deep-mode Gather loops and metacognitive check

| Loop | Observe/orient | Counter-evidence | Decision or hypothesis carried forward |
|------|----------------|------------------|-----------------------------------------|
| 1 — T1 catalogue/control | 100-task parser, four index states, four FA routes, current comparable systems | OpenSpec derives state; Spec Kit uses strict Markdown; BMAD centralizes YAML; absent index increases reader work; no NH evidence | **Decision pressure:** retain authority/view separation unless a competitor also meets unordered sync + legacy compatibility. **Hypothesis:** several status fields belong in profiles/derived metadata rather than the shared required core. |
| 2 — T2 recovery/bounds | epoch/order/duplicate/rejection matrix; Unicode, count/byte and parser measurements; vendor contracts | DF encodes the proposed recovery model and cannot prove PR; byte ceiling can fire at 60 or 120 events; code points do not bound bytes | **Decision pressure:** recovery must fail closed and numbers remain configurable hypotheses. **Hypothesis:** combined count+encoded-byte rollover is structurally sound, but 240/100/32 KiB are not evidenced defaults. |
| 3 — T3 Git/migration | G-B allowlist/drift/provenance; G-A preflight; three landing orders; current corpus census | wrong-but-self-consistent worktree passes an unpinned probe; post-commit event dirties; pre-landing manifest cannot know future hash; 21 board rows exceed header width | **Decision pressure:** G-A needs locally pinned expectations; landing provenance must separate intent from completed Git fact. **Hypothesis:** commit + pre-landing handoff may replace a post-commit task-journal `landed` event without weakening file/Git responsibilities. |

Metacognitive check:

- **NEW:** context-free FA evidence now exists for all four index conditions; it confirms recovery/discovery for agents but exposes an absent-index classification burden.
- **NEW:** the provisional summary/count/byte figures now have reproducible measurements; they still do not have workload/provider justification.
- **NEW:** G-A's generic rev-parse probe is insufficient without a separately pinned expected path.
- **NEW:** the ordering fixture makes the future-commit-hash circularity and post-commit dirty state concrete.
- **CONFIRMED, not new:** task authority outranks projections; event-first makes journal-ahead the recoverable direction; exact staged allowlists isolate a task; legacy paths cannot be normalized losslessly.
- **STILL UNKNOWN:** NH and PR, supported-version behaviour for all Git commands, operational frequency/size distribution for real journals, and the minimum shared versus profile field set.

### G16. Hypothesis pressure at the Gather gate

| Hypothesis | Supporting evidence | Counter-evidence/open gap |
|------------|---------------------|---------------------------|
| H1 | all FA readers recovered authoritative task state; normal persisted view shortened the route; stale/malformed views did not corrupt authority | absent view shifts material work to reader; UH is not NH; OpenSpec shows standardized artifacts can support derived-on-read status |
| H2 | strict parser caught ten distinct malformed controls; task-local fixed path enabled deterministic fallback | YAML itself is feature-rich; Spec Kit shows strict Markdown is viable under other concurrency assumptions; no non-technical human read or edited the control |
| H3 | recovery cases, rejected retention and 157× cold/full byte ratio support a narrow referenced journal | the fixture proves its own rules, not provider reconnection; numerical defaults unsupported; `landed` may be the wrong event boundary |
| H4 | census found common lifecycle/ownership needs despite carrier/path differences; no counterexample requires different event meaning | required-field cardinality and workflow stage differ; Assisted runtime population is absent, so migration remains partly source-contract evidence |

## Checkpoint

| Found | Remaining for Extract/Challenge |
|-------|---------------------------------|
| Deterministic 100-task 80/10/10 corpus; normal/absent/stale/malformed view results | Decide field core/profile split and define view-degraded acceptance without claiming NH success |
| Four-condition fresh-agent cold-start evidence | Genuinely observed non-technical-human file-browser/edit evidence remains unavailable |
| Every proposed field mapped to reader, trigger and minimization pressure | Extract which fields are shared required, conditional, profile or derived |
| Executable recovery matrix and reproducible Unicode/rollover/parser measurements | Actual provider offline/reconnect/conflict-copy evidence; numerical default justification |
| G-B scope/drift/provenance fixture and guarded G-A failure matrix | Specify pinned local configuration and supported Git-version gate |
| Concrete landing-order tradeoffs | Challenge whether `landed` stays in the task event grammar or becomes Git fact plus pre-landing handoff |
| Current Full/Assisted read-only legacy census | Map every shape to verified facts/unknowns without path moves; no legacy writes |
| Current primary YAML, Git, vendor and comparable-system sources | No source defeats a named C1-R/G-B invariant; eliminated families remain closed |

**Evidence state:** FA, UH, DF, RR and PS are present. NH and PR are absent. BMAD issue reports are upstream reports, not reproduced runtime. Assisted move/status rules are current shipped source contracts, not observed populated-workspace runtime. Temporary Git results are local runtime, not sync-provider behaviour.

**Recommendation at this gate:** proceed to Extract. T1–T3 have explicit source and fixture coverage, new counter-evidence is isolated, and remaining gaps are evidence-class or synthesis questions rather than an unsearched Phase-A dimension.

**Questions for the Coordinator:** none. Preserve NH and PR as TS acceptance gaps unless the Coordinator can supply real participants/providers within the approved scope; do not simulate them.

**Files written at this gate:** `research/iter2/1_briefing.md`; `research/iter2/2_gather.md`.

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] At least two decisions and one hypothesis pressure recorded (deep mode)?
- [x] Counter-evidence sought for each T1–T3 line?
- [x] Three Gather loops completed?
- [x] Metacognitive NEW-versus-confirmed check completed?

Stage complete: YES
→ User decision: WAIT — Coordinator must approve Extract or redirect the evidence gap.
