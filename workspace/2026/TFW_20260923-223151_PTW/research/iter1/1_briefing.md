# Briefing — What should we investigate?

> **Mindset:** Strategist. Frame the decision before comparing implementations.
> **Parent:** [HL-TFW_20260923-223151_PTW](../../HL-TFW_20260923-223151_PTW.md)
> **Goal:** Design a portable, one-worker route that delivers a bounded result in one run and leaves the smallest adequate, inspectable TFW Trace.
> **Producer unit:** `codex:thread:local:01a0d505-d0b4-76f2-ad95-58f1bf9cfe2e`
> **Parent Coordinator:** `codex:thread:local:01a0cf4d-9254-7633-9ba9-393b0eb8e802`
> **Activation / dispatch source:** Command-only `/tfw-research TFW_20260923-223151_PTW`; Coordinator dispatch `journal/20260925-010738__dispatch__ef88.md` at source commit `87f91aaae5bc6bea4616802119a6e55ccd101da3`, incorporated unchanged as local commit `aea074e`.
> **Coordination authority:** `HL-TFW_20260923-223151_PTW.md @ 64278fdfcbfc0f6a59fa069aef45265abd03b0c5`; approved frozen HL baseline `515b837`.
> **Originating proposer:** `none`; owner `saubakirov` requested the focused inquiry, as recorded in the HL and transition event.
> **Mode:** `focused`, selected by the owner as a quick, light inquiry and confirmed by the Coordinator on 2026-09-25. One pass per stage; one authorized iteration in `research/iterations.yaml`.

## Research Plan

### Gather — establish the comparison dimensions

- Inspect the North Star, approved HL, current Full scope rules and actual SenseLab/Helpdesk Daily records at their stated source epochs; separate observed practice from design claims.
- Inspect the repository's adapter manifest, init/update rules and template paths; identify what is actually installed, updated or overridden.
- Find authoritative external guidance for source-of-truth placement, durable references and project-local skill/package distribution; use it to challenge assumptions, not to grant TFW authority.
- Define dimensions for Goal/Value/North Star fit, trace completeness, one-shot context and write cost, future lookup, update isolation and migration risk.

### Extract — map viable configurations

- Compare dated independent `daily/YYYY/id/task.md`, subject/object-adjacent records, and selected Trace inside an existing commit/PR/document without a new folder, including one non-code case.
- Compare the proposed one-file record with SenseLab's working `task.md`/`brief.md`/`messages.md` split using actual continuation needs rather than file count.
- Compare optional Daily packaging and receiver update paths with a Full-command manifest entry, shared `.tfw/templates/`, and skill-bundled resources.
- Test names and identifiers against cadence/risk cues, stable links, timestamp collisions, multiple workers and retrieval of related work.

### Challenge — try to falsify the leading choice

- Seek a credible no-new-folder case that preserves human source, Goal/Value, decisions, result, verification and continuation across sessions.
- Seek an object- or subject-adjacent case where shared navigation wins despite mutable object ownership, confidential content or cross-object work.
- Probe the recommended package boundary for drift, overwritten local forms, update omissions and accidental changes to Full's fixed role commands.
- Return a decision matrix and explicit blind spots, including at least one alternative or failure mode missing from the current HL, with a falsifiable reason for the recommendation.

## Hypotheses (from HL §10)

| # | Hypothesis | HL status |
|---|---|---|
| H1 | Value comes from selected, connected Trace rather than daily cadence or a fixed file set. | Supported conceptually; naming cue still open. |
| H7 | Mandatory subject folders or a shared journal are needed to retrieve recurring Daily work. | Plausibly false; bounded search and exact links require testing. |
| H11 | One `task.md` costs less than SenseLab's three-file split in every project. | Open; compare continuation and context cost. |
| H12 | A separate dated Daily folder is the smallest adequate Trace for every bounded request. | Open; seek a no-folder counterexample. |
| H13 | `.tfw/extensions/daily-task/` isolates the Daily template from Full and local forms. | Open; test actual install/update and overrides. |
| H14 | `tfw-daily-task`, dated `daily/` folder and `task.md` cue the right behavior at team scale. | Open; test cadence, stable identity and lookup costs. |

## Scope Intent

- **In scope:** One focused architecture recommendation for name, Trace location/form and optional package boundary; evidence from field records, current repository mechanics and bounded external sources; free-section refinements and separately evidenced frozen-section amendment proposals.
- **Out of scope:** Implementing the skill or installer, editing HL/TS/code, migrating SenseLab or Helpdesk records, creating a medium route, or relaxing formal Full role/review requirements.

## Guiding Questions

1. What is the smallest durable Trace location that works for both code and non-code bounded work, and when does a separate folder earn its cost?
2. Which name, identifier and relation rule best preserve one-shot speed and later retrieval without teaching a different TFW method?
3. Which optional packaging and template boundary survives init/update and local overrides without changing the ten Full role commands?

## User Direction

The owner requested a quick, light single iteration focused on folder/file names, placement, alternatives and blind spots. The Coordinator confirmed `focused` and the pending iteration's H1/H7/H11–H14 scope through the native addressed return. The owner also fixed one-shot behavior for clear bounded Daily requests, no universal `daily/README.md`, no existing-record migration, and no silent shared-template effect. These are constraints to test within, not open decisions to reverse in this iteration.

---
Stage complete: YES
