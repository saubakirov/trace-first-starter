# RES — TFW-60: Phase A Task State & Coordination — Iteration 1

> **Date**: 2026-08-26
> **Author**: Researcher (Codex)
> **Status**: 🔬 RES — iteration 1 complete
> **Parent HL**: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md) — 🔒 FROZEN 2026-08-26
> **Mode**: Pipeline · deep (`loops_per_stage: 3`)
> **Stage files**: [1_briefing.md](1_briefing.md) · [2_gather.md](2_gather.md) · [3_extract.md](3_extract.md) · [4_challenge.md](4_challenge.md)

---

## Research Context

Phase A must replace the root Task Board as live pipeline authority without replacing a known conflict
with an invisible or technically fragile task model. Iteration 1 mapped every current status reader and
writer, reconstructed TD-81/144/175/177/178, inspected local AFD practice read-only, compared seven
current or historically relevant workflow systems, established the minimum documented behaviour of
ordinary file-sync providers, and attacked five file-only control configurations plus three Git
profiles. Debt and knowledge architecture were deliberately excluded.

The result is narrower than any starting proposal. A manually maintained live README table is not
needed, but an on-demand-only view fails the zero-command human case. Strict YAML is the strongest
status carrier, but its non-technical usability remains an acceptance question rather than a proven
fact. A separate journal survives only as a closed, reference-first, segmented coordinator trace with
explicit recovery. Assisted and Full can share the same semantic task contract while differing in
artifact profiles, transport and Git participation.

## Briefing

See [1_briefing.md](1_briefing.md). The Coordinator approved deep mode and Phase-A-only scope. Later
gates directed the research to retain a low-churn permanent entry/router, build coherent configurations
rather than isolated feature picks, separate status strictness from ownership, and test ten named
failure scenarios before synthesis. All four stage checkpoints were accepted before this RES was
written.

### Evidence boundary

Evidence labels in the stage trace remain important:

- **Local/source evidence:** repository files and Git history were inspected directly. This includes
  the 60-row Task Board, `gen_docs.py` parser, current Full/Assisted carriers, TFW-54's nonstandard task
  shape, and the TD-144/178 commits.
- **Primary source inspected, not executed:** current BMAD source, Spec Kit templates, GSD v1 historical
  source, and Hermes tests/docs. No third-party workflow system was installed. Primary references:
  [BMAD sprint parser](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/plan/bmad-sprint-planning/scripts/sprint_plan.py),
  [Spec Kit tasks command](https://github.com/github/spec-kit/blob/main/templates/commands/tasks.md),
  [GSD v1 state source](https://github.com/gsd-build/get-shit-done/blob/main/get-shit-done/bin/lib/state.cjs),
  and [Hermes Kanban tests](https://github.com/NousResearch/hermes-agent/blob/main/tests/hermes_cli/test_kanban_core_functionality.py).
- **Current primary documentation, not runtime proof:** current GSD Pi, OpenSpec, Task Master, and vendor
  sync semantics. GSD Pi and Hermes supply transaction/service counterexamples, not transferable
  guarantees for this file-only design: [GSD Pi parallel orchestration](https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/parallel-orchestration.md),
  [OpenSpec workflows](https://github.com/Fission-AI/OpenSpec/blob/main/docs/workflows.md), and
  [Task Master README](https://github.com/eyaltoledano/claude-task-master/blob/main/README-task-master.md).
- **Normative technical sources:** YAML requires unique mapping keys; JSON duplicate names have
  unpredictable receiver behaviour; Git documents explicit Git/worktree paths and path-scoped staging.
  See [YAML 1.2.2](https://yaml.org/spec/1.2.2/), [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259),
  [Git](https://git-scm.com/docs/git), [git-rev-parse](https://git-scm.com/docs/git-rev-parse), and
  [git-add](https://git-scm.com/docs/git-add).
- **Unverified implementation evidence:** human usability, actual reconnect/conflict-copy behaviour,
  validator fixtures, migration fixtures, numerical journal limits, and Git landing wrappers. These
  become TS acceptance recommendations below; they are not reported as shipped or verified behaviour.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| **D1** | **H1 is refuted as stated, but its architectural goal survives.** A manually maintained persistent live Task Board is unnecessary; an on-demand-only command is also insufficient. Use a permanent low-churn root router plus a persisted, rebuildable, explicitly derived `tasks/INDEX.md` | Agents can scan task controls, but a zero-command human cannot practically rank 100 opaque folders. Persisting a generated projection preserves cold-start value without making transitions edit one shared root authority. Challenge scenarios 1–2 |
| **D2** | **Recommend C1-R as the Phase-A configuration:** fixed strict `status.yaml` authority, separate numbered coordinator journal segments, persisted derived index, stable task paths, one state owner and explicit recovery | It is the only configuration that survived discovery, malformed data, long history, offline conflict, terminal state, migration and landing attacks without requiring a service/database. Challenge configuration dispositions |
| **D3** | Treat the design as four distinct responsibility layers: **authority** (`status.yaml` plus canonical role artifacts), **projection** (README router and derived index), **journal** (management events and references), and **Git** (local administration and controlled landing). File sync transports ordinary work files but grants none of the other layers' authority | The current failures came from conflating these responsibilities: README is both view and state API; a shared index is mistaken for task ownership; Git attribution is mistaken for sync correctness. Gather G2/G3/G7/G8 |
| **D4** | The status schema is deliberately small and validator-owned. Keep the Extract fields with named readers and add `owner_epoch`; prohibit duplicate keys, anchors, aliases, custom tags, free-form notes and copied artifact bodies | TD-177 shows flexible Markdown is not a stable machine contract. YAML's extension alone is not safety; a restricted schema plus fail-closed reader is. `owner_epoch` detects stale offline authority after reassignment without claiming a lock or identity authentication. Challenge field test |
| **D5** | The shared lifecycle kernel is `new`, `active`, `waiting`, `blocked`, and `terminal`, with terminal outcome `done` or `rejected`; `workflow_stage` supplies edition-specific detail | This preserves the real Full and Assisted meanings while avoiding separate edition models. Terminal rejection remains visible and immutable; changed intent creates a successor trace rather than silently reopening history. Extract E2; Challenge scenario 7 |
| **D6** | Use one normal control/journal writer: Full Coordinator or Assisted task steward. Other roles write only profile-owned artifacts and hand off references. Ownership recovery increments `owner_epoch` and records `ownership_changed` against a predeclared recovery authority | File format strictness, locking and business ownership solve different problems. One writer reduces collision; epoch and chain validation detect/recover accidental offline violations. They do not provide distributed mutual exclusion. Challenge scenarios 5–6 |
| **D7** | The journal's closed Phase-A grammar is `created`, `dispatch`, `handoff`, `transition`, `ownership_changed`, `amendment_escalated`, `landed`, and reserved `consolidation`. `blocked`/`resumed` are typed transitions. Catalogue regeneration is projection metadata, not a `consolidation` event in every task | This preserves frozen DoD-3 while avoiding reverse fan-in. `consolidation` is emitted only when a task-local record later crosses an explicit consolidation boundary; reserving the event does not design Phase B/C. Every event has a named reader/trigger and references the canonical artifact instead of copying it. Synthesis narrows Extract E4 and corrects Challenge's over-broad removal of the event kind |
| **D8** | Event records contain task-scoped monotonic ID, UTC time, kind, actor, `owner_epoch`, applicable state delta, at least one reference, optional related event, and one optional bounded summary. Corrections append a new event; sealed history is retained, including rejected tasks | Hermes/GSD support narrow summary/reference responsibilities, but their database/lock guarantees do not transfer. A closed file grammar prevents the journal becoming a second HL/RES/RF/REVIEW. Gather G6; Extract E4; Challenge event test |
| **D9** | Use event-first/snapshot-second transitions. Journal ahead is recoverable; snapshot pointing to a missing or malformed event is invalid. A duplicate event ID is idempotent only when the normalized complete record is identical | File-sync vendors do not document ordered multi-file visibility. “Latest timestamp wins” cannot distinguish stale ownership or divergent valid-looking branches. Extract E5; Challenge scenario 4 |
| **D10** | Segment history structurally and retain all segments, but do not freeze `240 code points`, `100 events`, or `32 KiB` as proven constants | A bounded active read and immutable sealed history solve the architecture problem. The proposed values are fixtures derived from external examples and local bloat evidence, not measured operating limits. Challenge numerical-bound test |
| **D11** | Normative file-sync rules assume only independent-file propagation: stable task directories; disjoint role files; no transition while local sync reports error; conflict copies preserved; no provider API, transaction, lock or ordering claim | Google, OneDrive and Dropbox document conflict/recovery behaviour but no portable cross-file transaction. Provider names belong in evidence environments, not the mechanism. [Google Drive troubleshooting](https://support.google.com/drive/answer/2565956?hl=en), [OneDrive troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/sharepoint/sync/troubleshoot-sync-issues), [Dropbox conflicted copies](https://help.dropbox.com/organize/conflicted-copy) |
| **D12** | Migration is lossless by compatibility, not forced uniformity. Freeze existing Assisted task directories where they are and stop future status moves; scan declared legacy roots. Create Full controls only from verified board/artifact facts; preserve proposals, malformed/nonstandard tasks and historical links | Moving legacy folders would cause the path/sync failure Phase A exists to remove. Guessing missing fields would silently reassign history. Challenge scenario 8 |
| **D13** | **G-B is the baseline Git profile:** one Git-capable landing owner and sync-only peers. **G-A is an optional Full profile:** each technical participant may use guarded machine-local `GIT_DIR`/index for inspection, but the same one-owner landing gate remains. Never synchronize `.git`, a gitfile, index, locks or worktree administration | G-B minimizes non-technical burden. G-A survives only because absolute Git-dir/worktree/index preflight can fail closed. A `--separate-git-dir` gitfile in the synced root is still machine-specific state. Challenge Git profiles |
| **D14** | Every landing stages literal declared task paths, compares the cached-name set to an exact allowlist, verifies staged task paths did not change after staging, and commits one task/phase scope. Catalogue output lands separately | Local indexes solve TD-144 but not TD-178. Git documents that `add` captures named file contents at that moment and that directory/glob pathspecs widen scope. Explicit scope verification is therefore structural, not advisory. Challenge scenarios 9–10 |
| **D15** | Eliminate C2, C3, C4, C5 and G-C rather than blend them into the survivor | C2 either recreates YAML inside Markdown or permits body drift; C3 makes transitions create/delete multiple paths; C4 requires replay to know current state; C5 puts snapshot and unbounded history in one conflict domain; G-C introduces a second exchange/import authority. Challenge dispositions |
| **D16** | No frozen-HL amendment is required. All findings specify how Phase A meets the already-frozen locality, derived-view, stable-path, journal, migration and Git claims | Frozen §3.1 and deliverable 3 explicitly allow low-churn/rebuildable views; §10 left carrier and journal details open. The §5/§6 tripwire is not triggered. The one synthesis correction—retaining reserved `consolidation`—preserves rather than changes frozen DoD-3. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Can a fresh agent select work and a genuinely non-technical human discover and safely change C1-R in a 100-task fixture without being taught a command? | 🟡 open for iteration 2 | Architecture survives analytically; no human usability observation was collected. Test normal, absent, stale and malformed index cases separately. |
| Q2 | What event-summary and segment ceilings are small enough for bounded cold start but large enough to avoid noisy rollover? | 🟡 open for iteration 2 | `240 / 100 / 32 KiB` remain test inputs, not verdicts. Measure encoded Unicode records, 100+ event tasks and renderer/parser behaviour. |
| Q3 | Does `owner_epoch` plus event-first reconciliation produce one deterministic recovery after real offline forks and provider-created conflict copies? | 🟡 open for iteration 2 | Vendor documentation establishes the failure class, not the framework's recovery effectiveness. Capture both branches and the final reconciliation trace in an actual synced folder. |
| Q4 | Should `landed` remain a post-commit journal event, or should task/role provenance live entirely in the commit plus pre-landing handoff to avoid an immediately dirty task journal? | 🟡 open for iteration 2 | Both preserve references; the current event creates a deliberate post-commit lag. Test release/resume consequences before freezing the grammar. |
| Q5 | Which edition should expose G-A, and what exact failure result should users see when local `GIT_DIR`/worktree/index preflight is missing or wrong? | 🟡 open for iteration 2 | G-B is the safe baseline. G-A remains Full-only/optional until setup and recovery are proven usable. |
| Q6 | Can every current Full/Assisted legacy and nonstandard task migrate without guesses, path moves or omissions? | 🟡 open for implementation fixture | The compatibility strategy is defined; a complete corpus fixture must verify TFW-54-style proposals, malformed board rows, rejected tasks and Assisted legacy roots. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| **H1** | A persistent Task Board is not required; a standard on-demand command can assemble task ID, goal, value, live status and terminal outcome without degrading agent or human cold start | needs-research | ❌ **REFUTED AS STATED; HYBRID CONFIRMED** | A manually maintained live board is unnecessary, but on-demand-only fails the zero-command 100-task human case. Permanent router + persisted derived index preserves frozen low-churn/rebuildable contract; task controls remain authority. Gather G2/G5/G6; Challenge scenarios 1–2 |
| **H2** | A tiny machine-readable task-local carrier—markers or strict YAML—is safer than mutable Markdown and remains understandable to non-technical users | needs-research | 🟡 **PARTIALLY CONFIRMED** | Strict reduced YAML survives; markers and bounded Markdown are eliminated. Deterministic parsing is supported by repository drift and language rules. Non-technical discovery is supported through the index, but safe direct editing remains untested. Gather G3/G6; Challenge C1-R/C2/C3 |
| **H3** | A separate coordinator-owned append-only journal with closed events, references and size/retention rules preserves continuity without duplication or unbounded growth | needs-research | 🟡 **SUPPORTED, ACCEPTANCE EVIDENCE REQUIRED** | Separate segmented journal survives with one writer, reference-first records, event-first reconciliation and complete retention. Redundant event kinds were removed, recovery added, and numeric limits remain hypotheses. No live long-task/reconnect fixture yet. Extract E4/E5; Challenge scenarios 3–6 |
| **H4** | Assisted and Full can share one task-local state/journal contract while differing only in transport and Git requirements | needs-research | ✅ **CONFIRMED AT THE SEMANTIC-CONTRACT LEVEL** | Identity form, stage subset, artifact ownership profile, adapter transport and Git participation may vary; lifecycle/outcome, next action/ref, owner/epoch and event meanings remain shared. Separate task models add no value. Gather G4; Extract E2/E3; Challenge scenarios 6–8 |

## Phase-A TS Acceptance Recommendations

These are requirements for the Coordinator to translate into TS acceptance criteria, not a TS or an
implementation plan.

| # | Acceptance recommendation | Required evidence/gate |
|---|---------------------------|------------------------|
| **AR1** | A versioned strict status schema accepts the complete shared contract and rejects duplicate keys, unknown required enums, malformed ownership, illegal terminal combinations, missing event references and unsupported versions before any workflow acts | Reproducible valid/invalid fixture matrix; each invalid case returns a stable fail-closed result and changes no task state |
| **AR2** | A 100-task fixture deterministically generates the persisted derived index, labels authority/freshness/source count and links every valid task while reporting every malformed/legacy task rather than omitting it | Compare generated output across two identical runs; test normal, absent, stale and malformed cache; resume/release must select task-local status over the cache |
| **AR3** | Fresh-reader discovery works for both audiences: a no-chat agent selects a task from the root instructions, and a non-technical human using only ordinary file browsing identifies ID, goal, value, state, owner, terminal outcome and authoritative control without command coaching | Contemporaneous observation record for both readers; human test includes at least one stale-cache task and records errors/confusion rather than only completion |
| **AR4** | Journal/snapshot recovery is deterministic for journal-ahead, snapshot-ahead, duplicate-identical ID, duplicate-divergent ID, malformed event, segment rollover and provider conflict-copy fixtures | Each fixture preserves both inputs, produces one declared recovery result or explicit stop, and never chooses by timestamp alone |
| **AR5** | Long-task behaviour proves a configured finite summary/segment policy without deleting sealed history or loading all history at cold start | Fixture includes 100+ events, multi-byte Unicode, at least two segment rollovers and a rejected terminal task; record encoded sizes and parser/render measurements before choosing defaults |
| **AR6** | Same-task parallel roles write disjoint artifacts; coordinator disappearance prevents unauthorized state transitions and recovery increments the owner epoch against a declared authority | Reproducible role-ownership fixture plus recovery trace; old-owner offline branch is retained/quarantined and cannot become current silently |
| **AR7** | An actual synchronized-folder environment exercises two different tasks, same-file offline conflict/reconnect, independent role files, stale projection and final reconciliation | EV records provider/client/version, initial/final files, conflict artifacts, sync status and journal/control outcome; provider UI alone is insufficient per HL §7.1 |
| **AR8** | Full and Assisted migration retains every historical path and terminal/rejected trace, creates no guessed facts, and discovers legacy/nonstandard tasks including proposals without HL | Corpus manifest before/after, link checks, explicit unknown-field report, and zero unaccounted tasks; existing Assisted folders are not moved merely to normalize layout |
| **AR9** | G-B lands exactly one declared task after unrelated peer changes arrive; G-A additionally fails closed for missing/wrong `GIT_DIR`, worktree, index or unexpected `.git` entry | Capture preflight output, worktree changes, staged-name allowlist, staged-vs-working-tree recheck, commit subject/trailers and final commit file list; no broad staging command |
| **AR10** | The full Phase-A cascade—canonical rules, lifecycle workflows, supported adapters, release/resume, migration, docs compiler and Quick Start—reads task controls rather than live README state and still handles DONE/REJECTED correctly | Exact file/LOC budget census before TS; source/copy drift check; regression fixture for TD-81/175/177 and docs task discovery; Phase A is not releasable with an old-state adapter or compiler |

## HL Update Recommendations

> The recommendations below are classifications only. This Researcher does not edit the frozen HL,
> `iterations.yaml`, README or TS.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| **R1** | §2 | Update the Task Board measurement to 60 rows and record the 40 eight-cell / 20 nine-cell split; add the TD-144 and TD-178 commit reconstructions and the current Full/Assisted ownership/path differences | Gather G2–G4 |
| **R2** | §7.2 | Add primary citations for the YAML unique-key rule, JSON duplicate-name risk, Git explicit Git-dir/worktree/path staging, and vendor conflict-copy floor; keep service/database systems explicitly qualified as counterexamples | RES evidence boundary; Gather G6–G8; Challenge consistency check |
| **R3** | §8 | Mark internal Phase-A topology/debt reconstruction complete; retain real synchronized-folder evidence, exact adapter/budget census, and TFW-54 re-planning as open dependencies | Gather G2/G3; AR7/AR10 |
| **R4** | §9 | Update discoverability risk: on-demand-only materialized as a failure; mitigation is permanent router + persisted derived index + authoritative task re-read. Update status risk: strict YAML survives but human editing remains unverified. Add owner-epoch/recovery, post-commit `landed`, and legacy-resolver risks | D1/D4/D6/D7; Q1/Q3/Q4/Q6 |
| **R5** | §9 | Refine Git risk into two independent failures: shared-index contamination (TD-144) and out-of-scope landing/provenance (TD-178). Mitigate with local administration plus one landing owner **and** exact staged-path allowlists | D13/D14 |
| **R6** | §10 | Mark H1 refuted-as-stated/hybrid-confirmed; H2 partially confirmed; H3 supported pending acceptance evidence; H4 confirmed at semantic-contract level. Replace closed blind spots with the six open questions and preserve debt/knowledge exclusion | Hypothesis table; Open Questions |
| **R7** | §11 | Add the layer insight: authority, projection, journal, file-sync transport and Git landing are separate capabilities. Local Git metadata does not establish task ownership; one writer does not create a distributed lock; a persisted projection does not become authority | D3/D6/D11/D13 |
| **R8** | §11 | Add the migration insight: compatibility can preserve stable paths better than normalization. Existing Assisted directories should become stable legacy roots instead of being moved into a uniform neutral tree | D12 |

### Amendment Proposals — frozen sections, owner verdict required

**No amendment proposals.** C1-R, the hybrid catalogue, shared semantic contract, stable legacy-path
compatibility and guarded Git profiles all satisfy the existing frozen §3–§7 claims. The synthesis
retains `consolidation` as a reserved task-affecting journal event so frozen DoD-3 is not narrowed. If a
later design requires one physical file for snapshot and append-only history, or removes consolidation
from the task trace entirely, that would need fresh classification against the frozen contract.

## Fact Candidates

No new Fact Candidates. The human messages in this iteration authorized scope, mode and gate progression;
those task-specific directions are already preserved in the stage traces and do not pass the
next-agent decision test as independent project facts.

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| **SS1** | stakeholder | The Coordinator explicitly refused to force H1's strongest form and required cold-start paths for both agents and non-technical humans. **Implication:** project visibility is part of correctness, not presentation; a conflict-free design that needs a hidden command still fails the product | Coordinator Extract direction, 2026-08-26 | ★★★ |
| **SS2** | philosophy | The Coordinator required coherent configurations and elimination rather than a feature blend unless evidence demanded a bounded hybrid. **Implication:** C1-R should be specified as a responsibility architecture with explicit authority boundaries, not as a menu of optional carriers that lets projects recreate the original ambiguity | Coordinator Extract/Challenge direction, 2026-08-26 | ★★★ |
| **SS3** | constraint | The Coordinator kept database/service patterns as counterexamples and separated file-sync rules from Git landing. **Implication:** claims must stay at the ordinary-file guarantee floor even when stronger external systems demonstrate attractive locking or transaction behaviour | Coordinator Extract direction, 2026-08-26 | ★★★ |

## Findings Map

```text
                         PROJECT ENTRY / PROJECTION
              README permanent router ──→ tasks/INDEX.md
                    low-churn                 persisted cache
                                                │
                                  never authoritative; may be stale
                                                │ select + re-read
                                                ▼
┌────────────────────────────── STABLE TASK ROOT ──────────────────────────────┐
│                                                                              │
│  AUTHORITY                         JOURNAL                                   │
│  status.yaml                       journal/segment-N                         │
│  ID · goal/value · state           closed management events                 │
│  owner + owner_epoch               references, not copied work              │
│  next/terminal · last_event  ◄──── event-first / snapshot-second ────────┐  │
│       │                                                                  │  │
│       │ named readers                                                   │  │
│       ▼                                                                  │  │
│  resume · release · catalogue       ROLE-OWNED WORK                       │  │
│                                    HL/TS · RES · ONB/RF/EV · REVIEW ──────┘  │
└──────────────────────────────────────────────────────────────────────────────┘
                          │ ordinary independent files
                          ▼
                 FILE-SYNC TRANSPORT FLOOR
       no ordering · no lock · conflict copies · no status moves
                          │
                          ▼
                       GIT LAYER
       local administration + one landing owner + exact path allowlist
       G-B baseline · guarded G-A optional Full · G-C eliminated
```

The causal finding is that conflict resistance comes from **separating responsibility**, not choosing a
single clever format. The projection can disappear without corrupting state; the journal can be long
without becoming cold-start context; file sync can reorder files without granting authority; Git can
land provenance without becoming the synchronization lock.

## Iteration Status

- **Iteration:** 1 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (refuted as stated; hybrid confirmed), H2 (partially confirmed), H3 (supported with acceptance evidence required), H4 (confirmed at semantic-contract level)
- **Hypotheses deferred:** None; all four were tested. Empirical acceptance gaps are carried as iteration-2 threads rather than marked as null results.
- **Gaps discovered:** non-technical direct-edit usability; actual provider reconnect/reconciliation; numerical journal bounds; `landed` event/commit ordering; guarded G-A usability; exhaustive legacy migration.
- **Superseded decisions:** D2 supersedes Extract C1–C5 as unselected candidates; D7 supersedes Extract's nine-kind grammar and corrects Challenge's removal of the frozen `consolidation` event by reserving it for actual task-affecting consolidation only; D13 supersedes G-A/G-B/G-C as unselected profiles.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| **T1** | 100-task cold start and strict-YAML usability | H1's hybrid and H2's human half remain design-supported but not observed. A view that works only for agents violates DoF-7 | Build one reproducible mixed valid/legacy/malformed corpus; run a fresh-agent path and zero-command non-technical browsing/edit task; compare absent/stale/malformed index recovery |
| **T2** | Sync recovery and journal bounds | `owner_epoch`, event-first ordering and segmentation are the critical recovery mechanisms, but vendor documentation does not prove their implementation | Run actual offline dual-owner/conflict-copy and coordinator-loss scenarios; exercise duplicate/malformed/rollover fixtures; choose or reject the provisional numerical defaults from measurements |
| **T3** | Git landing and journal provenance | G-A/G-B survive analytically, while `landed` creates a post-commit trace-order question and TD-178 requires exact landing evidence | Exercise G-B after peer changes and every G-A setup failure; compare `landed` event versus commit-only provenance; verify exact allowlists, producer/landing-owner attribution and recovery |

### Recommendation

- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [x] **MORE NEEDED** — iteration 1 is sufficient for its assigned architectural pass, but `min_iterations: 2` is mandatory and T1–T3 contain material empirical questions before Phase-A TS
- [ ] **BLOCKED** — no blocker

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 1 established a viable Phase-A architecture and eliminated the attractive failure modes that
would otherwise have reached TS: a live root board, an on-demand-only catalogue, status markers,
Markdown control, event-only state, combined status/history, synchronized Git administration, and a
dual-transport exchange model. C1-R separates task authority, derived discovery, coordinator history,
ordinary file transport and Git landing while retaining one shared Assisted/Full semantic contract.
The research also found its own necessary correction: catalogue generation must not fan out into every
task journal, but frozen DoD-3 still requires a consolidation event, so the grammar reserves that event
for actual task-affecting consolidation rather than deleting it. The architecture is sufficiently
bounded to guide iteration 2, not sufficiently evidenced to skip it. The next pass should validate
human discovery, offline recovery, journal bounds and Git landing rather than reopen the eliminated
configuration space.

---

*RES — TFW-60: Phase A Task State & Coordination — Iteration 1 | 2026-08-26*
