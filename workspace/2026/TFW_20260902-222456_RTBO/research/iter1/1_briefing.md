# Briefing — "Where should portfolio collection and diagnostics live?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> Parent: [HL-TFW_20260902-222456_RTBO](../../HL-TFW_20260902-222456_RTBO.md)
> Goal: TFW keeps task state inspectable without a committed portfolio cache, a hard prose-length gate, or a runtime prerequisite.

## Research Plan

### Gather

- Inventory `gen_index.py` by responsibility, dependency, caller, shipped destination, and observable failure behavior.
- Exercise the current entry points in the upstream repository and clean Full/Assisted payloads, including Python-present/PyYAML-absent conditions.
- Separate the documentation build's current-list projection, primary navigation, trace-page compilation, and citation resolution into independently testable surfaces.
- Classify current findings by protected object, material consequence, compliance timing, and exit-code behavior; use the immutable 123-character event as the required negative case.

### Extract

- Compare optional Full utility, maintainer-only doctor, and split-core ownership across portability, duplication, correctness, receiver burden, and failure isolation.
- Form a configuration space over ownership, runtime, invocation, output, diagnostic severity, and documentation exposure.
- Eliminate combinations that make Full depend on the helper, penetrate Assisted, write shared state, suppress structural corruption, or break cited trace reachability.

### Challenge

- Try to disprove the leading ownership shape through clean-receiver and dependency-path counterexamples.
- Challenge whether a build-time current list or broad primary task navigation produces value beyond citation-only reachability.
- Verify that removing length enforcement quiets the existing 123-character event while malformed state, duplicates, illegal transitions, and missing authority remain observable.
- Identify compatibility obligations that cannot safely be folded into either ordinary Full use or the bounded maintainer diagnostics surface.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H2 | Full can include an optional status collector without making Python or PyYAML a practical prerequisite, provided every workflow has a complete no-helper path and helper absence never changes lifecycle. | needs-research |
| H3 | A CI-generated current task list helps orientation, while placing the entire task corpus in primary site navigation distracts from TFW's philosophy and use; citation-reachable traces are sufficient. | needs-research |
| H4 | Material task/project integrity checks can be separated from advisory authoring guidance so that the known 123 event becomes quiet without reducing detection of malformed state, illegal transitions, duplicates, or missing authority. | needs-research |

## Scope Intent

- **In scope:** Current `gen_index.py` responsibilities and consumers; Full and Assisted delivery boundaries; no-helper behavior; documentation task surfaces; current task/project diagnostics; the immutable 123-character event; the bounded relationship to a future `tfw-doctor`.
- **Out of scope:** Implementing or naming a broad doctor product; modifying HL, TS, code, templates, existing history, or another task; proving that every future agent can enumerate an arbitrarily large corpus; replacing the documentation platform.

## Guiding Questions

1. Which deterministic capabilities have a real receiving-project consumer, and which exist only for upstream maintenance or a retired committed index?
2. Can a shipped optional utility remain absent from all lifecycle paths, and is that boundary clearer or cheaper than a maintainer-only or split-core design?
3. What is the smallest documentation and diagnostic surface that preserves orientation, structural integrity, and citation reachability without creating routine noise?

## User Direction

The owner directed the research team to proceed autonomously through complete research iterations and report goals, values, and recommendations afterward. H1 is already refuted by owner judgment: corpus scale alone does not justify shipped runtime because a capable agent can create a fit-for-environment collector. Unknown answers must remain explicit gaps or proposals rather than being invented to avoid a question.

The configured `focused` mode is used for iteration 1 because the question is bounded to an existing module, its known consumers, and three declared ownership shapes. Checkpoint findings are recorded durably and the owner's prior autonomous-run direction supplies continuation authority between stages; it does not authorize HL amendments or implementation.

---
Stage complete: YES
