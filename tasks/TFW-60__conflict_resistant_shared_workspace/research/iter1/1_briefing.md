# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md)
> Goal: Make concurrent human and agent work in a synchronized TFW workspace conflict-resistant by moving normal lifecycle state and coordination to stable task-local, single-writer surfaces while retaining discoverability and Git provenance.

## Research Plan

### Gather

- Build the Phase A read/write/ownership map across the Task Board, lifecycle workflows, adapters, documentation compiler, task artifacts and Git staging surfaces; reconstruct TD-81, TD-144, TD-175, TD-177 and TD-178 from their original traces.
- Locate and inspect available AFD evidence read-only, without guessing its path or modifying that project; determine what its README constraint actually enforces and what remains only textual guidance.
- Compare current primary repositories and documentation for GSD / Get Shit Done, BMAD, Hermes and at least three other active spec-driven or agent-workflow systems. Disambiguate similarly named projects and separate shipped repository behavior from documentation claims.
- Establish primary-source semantics for Google Drive, OneDrive, Dropbox and plain synchronized folders: independent-file edits, same-file conflicts, offline reconnect, directory moves and treatment of `.git`.
- Decompose candidate decision factors: catalogue materialization, cold-start discovery, status representation, journal grammar/retention, ownership, edition contract, synchronization guarantees and Git topology.

### Extract

- Cross-reference the Gather dimensions into a configuration space spanning persistent/generated/hybrid catalogue, marker/YAML/bounded-Markdown status, journal formats, single-writer boundaries, shared/edition-specific state contracts and local/shared Git metadata.
- Trace each configuration through cold-start agent discovery and non-technical human browsing, including which facts have an authoritative source and which project views are derived.
- Derive a minimal read/write/ownership contract and journal event grammar from concrete consumers, refusing fields or events without a named reader or lifecycle trigger.
- Separate common task-state semantics from transport- and edition-specific operating rules; identify configurations compatible with ordinary file sync and explicit-path Git commits.

### Challenge

- Seek counter-evidence against all four hypotheses, including evidence that a persistent board is indispensable, YAML/markers are unusable for non-technical humans, strict journals still duplicate artifacts, or editions need incompatible state models.
- Stress surviving configurations against 100-task discovery, long-running journals, missing/stale generated views, offline concurrent state changes, same-file conflict copies, coordinator disappearance, task rejection and directory-move synchronization.
- Test failure containment for different-task and same-task concurrency, including contradictory markers, malformed status data, duplicate journal events and one shared Git index.
- Classify conclusions as Phase A refinements or amendment proposals against the frozen HL, with evidence, cost and a considered alternative for every proposed amendment.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | A persistent Task Board is not required: a standard on-demand command can assemble task ID, goal, value, live status and terminal outcome from task-local sources without degrading cold-start agent planning or human discovery. | needs-research |
| H2 | A tiny machine-readable task-local status carrier — marker files or a strictly bounded YAML schema — is safer than a mutable Markdown status page and remains understandable to non-technical users through normal file browsing. | needs-research |
| H3 | A separate coordinator-owned append-only journal with a closed event vocabulary, artifact references and a size/retention rule preserves cross-session management context without duplicating HL/RES/RF/REVIEW or becoming a new writing surface. | needs-research |
| H4 | Assisted and Full can share one task-local state/journal contract while differing only in collaboration transport and Git requirements; separate task models per edition are unnecessary. | needs-research |

## Scope Intent

- **In scope:** Phase A only — task catalogue and cold-start discovery; live task status; coordinator journal; internal read/write/ownership topology; TD-81, TD-144, TD-175, TD-177 and TD-178; discoverable local AFD evidence; current primary-source comparison of GSD, BMAD, Hermes and at least three additional systems; Google Drive, OneDrive, Dropbox and plain file-sync semantics; `.git` locality and landing topology; one shared Assisted/Full state contract versus edition-specific models.
- **Out of scope:** Phase B debt storage and aggregation; Phase C knowledge staging and consolidation; implementation, migration, adapter edits or framework/code changes; HL, `iterations.yaml`, README, TS, ONB, RF or REVIEW edits; iteration 2; vendor API integration; modifications to any AFD project.

## Guiding Questions

1. What is the smallest authoritative task-local state plus project discovery arrangement that survives cold start for agents and ordinary browsing for non-technical humans without making every transition a shared-file edit?
2. What closed journal grammar, reference rules and retention boundary preserve coordinator continuity while excluding information already owned by HL, RES, TS, ONB, RF or REVIEW?
3. Which semantics can be identical across Assisted and Full, and which must remain edition- or transport-specific because file sync and Git provide materially different guarantees?

## User Direction

- Owner authorized an autonomous research cycle through Codex tasks and does not want stage-by-stage substantive questions; workflow gates still require a report and STOP for Coordinator continuation.
- Coordinator approved `deep` mode for iteration 1: up to three OODA loops per stage, technical claims cross-checked twice and counter-evidence required.
- Iteration 1 is restricted to Phase A and H1–H4. Debt and knowledge architecture are explicitly excluded.
- Only `research/iter1/` stage files and `research/iter1/RES.md` may be written. The frozen master HL and coordinator-owned `research/iterations.yaml` remain read-only.

---
Stage complete: YES
