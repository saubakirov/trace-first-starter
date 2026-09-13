# Briefing — Iteration 2: close the retirement proof gaps

> **Mindset:** Strategist. Frame the proof needed before a retirement decision; do not alter the product surface.
> Parent: [HL-TFW_20260913-151442_RWNR](../../HL-TFW_20260913-151442_RWNR.md)
> Predecessor: [Iteration 1 RES](../iter1/RES.md)
> Goal: decide whether Resume can be retired without loss of lifecycle safety, trace integrity, or a discoverable recovery path.

## Research Plan

- **Gather:** recover the exact current state machines, authority chain, install/update ownership rules, historical baseline, and word-count provenance needed to test the five gaps. Treat current files and Git objects as primary evidence.
- **Extract:** specify one bounded candidate architecture: a routing-only Plan preflight, the existing non-command close/recovery route, a version-addressed ownership-checked migration, a two-part history oracle, and one baseline/candidate word counter.
- **Challenge:** execute table-driven and repository-derived checks against H1–H4, including collision and no-mutation states, foreign-file refusal, absent-adapter and idempotence cases, history counts/hashes, and counter reproducibility.
- **Synthesize:** either close all decision gaps and recommend retirement with clause-level North Star mapping, or retain Resume as C1 and state the exact failed condition. Do not convert the result into a TS.

## Hypotheses (from HL §10)

| # | Hypothesis | HL status entering iteration 2 |
|---|---|---|
| H1 | Resume behavior is already covered by Plan/shared lifecycle routes, so Resume has no independent value. | Partly refuted as a literal current-state claim; narrowed to a candidate-state claim conditional on C2. |
| H2 | Resume is unnecessary rather than merely duplicative. | Architecturally plausible; not yet supported by executable candidate-state evidence. |
| H3 | Removing Resume lowers maintenance burden without breaking compatibility. | Blocked by additive-only stale-file handling and an unsplit history oracle. |
| H4 | Resume can be removed while keeping net documentation volume below the frozen baseline. | Blocked by unreproduced baseline counts, moved-text accounting, and Plan's pre-existing size breach. |

## Scope Intent

- **In scope:** exactly the five gaps named by continuing dispatch `1958235` / `journal/20260913-172647__dispatch__93c5.md`; H1–H4; C2 as the leading candidate; C1 (keep Resume) as the mandatory fallback; G1 decision evidence.
- **Out of scope:** edits to control files, HL, TS, workflows, adapters, tests, implementation, TKL/knowledge, review, release, or a third research iteration; creation of a new command, wrapper, hidden continuation helper, or debt registry.

## Guiding Questions

1. Can one early, pure Plan routing gate cover every live, historical, malformed, terminal, phase, return, close, and recovery state while proving that routing itself performs no mutation?
2. Can retirement be installed and updated safely with a versioned ownership check, a ten-command clean-install surface, and separate immutable-task versus append-only-aggregate history proofs?
3. Can one byte-defined word counter measure the immutable baseline and the complete candidate (including moved text), while giving Plan's over-limit state an explicit, enforceable disposition?

## User Direction

The LEAD's continuing dispatch fixes the scope, artifacts, five gaps, and fallback. It authorizes this same Researcher unit to complete focused iteration 2 and return directly after `RES.md`; it grants no control-file or implementation authority. No further user question is required at Briefing.

---
Stage complete: YES
