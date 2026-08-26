# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md)
> Goal: Independently attack the iteration-1 Phase-A architecture so concurrent humans and agents can rely on task-local state, coordination, file sync and Git landing without losing discoverability, provenance or stable traces.
> Predecessor: [Iteration 1 RES](../iter1/RES.md) and [stage traces](../iter1/)

## Research Plan

### Gather — three adversarial evidence loops

- **T1, corpus and discovery:** build a deterministic 100-task mixed valid/legacy/malformed fixture outside tracked project paths; exercise normal, absent, stale and malformed derived indexes; record a fresh-agent cold-start path separately from heuristic reasoning and from genuinely observed non-technical-human evidence.
- **T1, schema and readers:** challenge every proposed `status.yaml` field against a named reader and lifecycle trigger; inspect current primary comparable-system sources for evidence that central or richer state, Markdown, markers or databases solve a failure C1-R cannot, without reopening eliminated families by preference.
- **T2, journal and recovery:** gather deterministic fixtures for `owner_epoch`, ownership recovery, event-first/snapshot-second ordering, identical/divergent duplicate IDs, malformed records, segment rollover, terminal rejected traces and coordinator disappearance; measure the provisional 240-code-point / 100-event / 32-KiB bounds without promoting them to defaults prematurely.
- **T3, Git and migration:** inventory the repository's Full/Assisted legacy and nonstandard task shapes read-only, including proposal-without-HL and malformed board rows; create temporary Git repositories/worktrees for G-B and guarded G-A attacks covering metadata preflight, unrelated peer changes, staged allowlists, single-task commits and producer/landing-owner attribution.
- **Evidence boundary:** distinguish repository/runtime observations, deterministic temporary fixtures, primary-source contracts, usability heuristics, real human observations and actual provider runtime observations. Never let a local fixture claim vendor sync behaviour or a researcher proxy claim human usability.

### Extract — cross-reference what survives

- Cross-reference T1 dimensions: catalogue state (normal/absent/stale/malformed), task shape (valid/legacy/malformed), reader (fresh agent/file-browser human/workflow), authority decision and status-field reader/trigger coverage.
- Cross-reference T2 dimensions: owner epoch, recovery authority, journal/snapshot visibility order, event-ID condition, malformed record, rollover threshold, terminal outcome and coordinator availability; derive deterministic stop/recovery outcomes without timestamp authority.
- Cross-reference T3 dimensions: G-B/G-A profile, Git-dir/worktree/index preflight state, peer-change timing, staged allowlist result, task/phase scope, producing actor, landing owner and journal/commit ordering.
- Separate the shared semantic lifecycle/ownership/event contract from Full- and Assisted-specific artifact, transport and Git profiles; reject any edition split that changes shared meanings without counter-evidence.
- Map every legacy/nonstandard task shape to verified facts, explicit unknowns and compatibility behaviour; do not invent missing HL/status facts or propose path normalization that moves existing tasks.

### Challenge — seek disconfirmation before synthesis

- Attack C1-R with the 100-task mixed corpus across normal, absent, stale and malformed index cases; test whether fresh-agent selection is reproducible and whether the zero-command file-browser route remains merely a heuristic when no real non-technical participant is available.
- Attack journal recovery with all named failure fixtures, multi-byte Unicode and multiple rollovers; compare the provisional bounds by measured encoded sizes/reader costs and preserve real-provider reconnect as an acceptance gap unless actual runtime evidence exists.
- Attack G-B and guarded G-A in temporary repositories/worktrees: wrong/missing `GIT_DIR`, unexpected worktree/index, unrelated peer changes, exact staged-path allowlists, staged-versus-working changes, one-task commit scope and producer/landing-owner provenance.
- Resolve `landed` ordering by comparing a post-commit event, commit-only provenance and a pre-landing handoff/reference design against resume, release, crash recovery, dirty-tree and circular-reference failures.
- Challenge lossless migration and shared-edition semantics against the full read-only legacy census. Reopen C2–C5 or G-C only if new counter-evidence defeats a C1-R/G-A/G-B invariant rather than because another carrier appears more familiar.

## Predecessor Decisions Under Attack

| Decision | Iteration-1 result to validate adversarially |
|----------|---------------------------------------------|
| D1 | H1 was refuted as stated; retain a permanent router plus persisted, rebuildable, derived `tasks/INDEX.md` for zero-command portfolio discovery. |
| D2 | C1-R was the sole surviving Phase-A control configuration: strict `status.yaml`, separate numbered journal segments, derived index, stable paths, one state owner and explicit recovery. |
| D3 | Authority, projection, journal and Git are distinct responsibility layers; file sync is transport and grants none of their authority. |
| D4 | Status is a small validator-owned YAML subset with no duplicate keys, anchors, aliases, custom tags, free-form notes or copied artifact bodies; `owner_epoch` detects stale authority. |
| D5 | The shared lifecycle kernel is `new`, `active`, `waiting`, `blocked`, `terminal`, with `done`/`rejected` terminal outcomes and edition-specific `workflow_stage`. |
| D6 | Full Coordinator or Assisted steward is the sole normal state/journal writer; recovery increments `owner_epoch` through a predeclared authority. |
| D7 | Journal grammar is `created`, `dispatch`, `handoff`, `transition`, `ownership_changed`, `amendment_escalated`, `landed`, plus reserved `consolidation`; block/resume are typed transitions. |
| D8 | Events carry monotonic ID, UTC time, kind, actor, epoch, applicable delta, references, optional related event and one bounded optional summary; corrections append. |
| D9 | Transitions are event-first/snapshot-second; journal-ahead may be recoverable, snapshot-ahead is invalid, and identical duplicate IDs alone are idempotent. |
| D10 | History is segmented and retained, but 240 code points, 100 events and 32 KiB are hypotheses rather than established constants. |
| D11 | Normative file-sync rules assume independent-file propagation only; no cross-file ordering, lock, transaction or provider-specific guarantee. |
| D12 | Migration is compatibility-first: preserve legacy paths and verified facts, report malformed/nonstandard tasks and never normalize by moving active/history-bearing directories. |
| D13 | G-B is the baseline one-landing-owner Git profile; guarded G-A is optional Full; Git administration never synchronizes. |
| D14 | Landing uses literal task paths, an exact staged-name allowlist, a staged-versus-working recheck, one task/phase scope and separate catalogue landing. |
| D15 | C2–C5 and G-C remain eliminated unless new evidence defeats the surviving invariants. |
| D16 | Iteration 1 found no frozen-HL amendment necessary; all recommended mechanisms fit the approved Phase-A contract. |

## Open Threads From Iteration 1

| Thread | Required closure or explicit gap |
|--------|----------------------------------|
| T1 — hybrid catalogue and strict YAML | Test a 100-task mixed corpus and four index conditions; supply fresh-agent evidence; distinguish usability heuristics from real non-technical-human observation; challenge every status field with a reader and trigger. |
| T2 — journal and recovery | Test epoch/recovery/order/duplicate/malformed/rollover/rejection/disappearance; evaluate numerical bounds reproducibly; keep real provider behaviour separate from deterministic simulation. |
| T3 — Git landing and migration | Test G-B and guarded G-A failure/scope/provenance cases; settle `landed` ordering; census Full/Assisted legacy and malformed shapes read-only; preserve shared semantics across edition profiles. |

Iteration-1 open questions Q1–Q6 map directly to these threads: human/fresh-agent usability (Q1), numerical limits (Q2), offline/provider recovery evidence (Q3), `landed` ordering (Q4), guarded G-A exposure and failure contract (Q5), and exhaustive compatibility migration (Q6).

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status Entering Iteration 2 |
|---|-----------|--------------------------------|
| H1 | A persistent Task Board is not required: a standard on-demand command can assemble task ID, goal, value, live status and terminal outcome from task-local sources without degrading cold-start agent planning or human discovery. | Iteration 1 refuted it as stated and confirmed a hybrid; iteration 2 attacks the permanent-router + persisted-derived-index replacement. |
| H2 | A tiny machine-readable task-local status carrier — marker files or a strictly bounded YAML schema — is safer than a mutable Markdown status page and remains understandable to non-technical users through normal file browsing. | Iteration 1 partially confirmed strict reduced YAML and eliminated markers/Markdown; direct non-technical editing remains unobserved. |
| H3 | A separate coordinator-owned append-only journal with a closed event vocabulary, artifact references and a size/retention rule preserves cross-session management context without duplicating canonical artifacts or becoming a new writing surface. | Iteration 1 supported it subject to recovery and bounds evidence; iteration 2 attacks both. |
| H4 | Assisted and Full can share one task-local state/journal contract while differing only in collaboration transport and Git requirements; separate task models are unnecessary. | Iteration 1 confirmed shared semantics while allowing edition-specific artifact, transport and Git profiles; iteration 2 audits legacy counter-evidence. |

## Scope Intent

- **In scope:** TFW-60 Phase A iteration 2 only; adversarial validation of C1-R, the hybrid catalogue, strict status schema, coordinator journal and recovery, G-B/guarded G-A Git landing, lossless Full/Assisted migration, and the shared semantic contract; current primary technical sources; deterministic temporary fixtures outside tracked project paths; read-only repository/legacy census; H1–H4 verdicts and classified HL recommendations.
- **Out of scope:** Phase B debt architecture; Phase C knowledge architecture; implementation or TS design; edits to the frozen HL, `research/iterations.yaml`, README, framework, adapters, legacy tasks or any artifact outside `research/iter2/`; iteration 3; destructive operations in external synchronized folders; claiming a deterministic simulation as provider runtime evidence; claiming a researcher simulation as observed non-technical-human evidence.

## Guiding Questions

1. What new evidence, if any, defeats the C1-R authority/projection/journal separation or the permanent-router + persisted-index hybrid strongly enough to reopen an eliminated configuration family?
2. Which journal recovery rules and bounds are reproducibly supported, and which must remain Phase-A TS acceptance gaps because real provider or human evidence is unavailable?
3. Which Git landing/provenance order and compatibility rules survive G-B/G-A fixtures and the complete read-only legacy census without splitting the shared semantic contract by edition?

## User Direction

- Owner authorized the full autonomous research cycle through delegated Codex tasks; the parent task is the Coordinator. The Researcher reports and stops at every TFW gate rather than asking the owner directly.
- Coordinator approved **deep** mode for iteration 2: up to three OODA loops per stage, technical claims cross-checked and explicit counter-evidence required.
- Iteration 2 is independent adversarial validation of iteration 1. C2–C5 and G-C may reopen only if new counter-evidence defeats C1-R, G-B or guarded G-A.
- Required threads are T1 hybrid catalogue/strict YAML, T2 journal/recovery, and T3 Git landing/migration. Phase A only; debt and knowledge architecture remain excluded.
- Only `research/iter2/` stage traces and `research/iter2/RES.md` may be written. Human/provider evidence must be labelled honestly; unavailable real evidence remains a TS acceptance gap.

---
Stage complete: YES
