# Briefing — Iteration 2
> Parent: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> Predecessor: [RES iter1](../RES__TFW-41__execution_quality_gates.md)
> Goal: Embed Zwicky Box heuristics into existing research stages so morphological analysis emerges naturally, not as a bolt-on exercise.

## Predecessor Context

- **DR4:** Zwicky Box mandatory in Extract for ≥3 parameters.
- **DR5:** 5 enforcement rules (≥3 values, CCA, no pre-recommendation, ≥2 survivors, unexpected survivors).
- **Open thread #2:** Zwicky Box minimum parameter threshold — is 3 the right cutoff?
- **H4 CONDITIONALLY SUPPORTED:** Works with enforcement, but HD-19 shows that a standalone "do Zwicky Box" instruction produces simulation.

## New Hypothesis (user-injected)

**H5:** The Zwicky methodology (Decompose → Enumerate → Eliminate → Select) can be distributed across the existing Gather → Extract → Challenge pipeline so that the morphological analysis emerges from the stage sequence itself, without an explicit "build Zwicky Box" instruction. This should be more natural and produce genuine analysis instead of simulation.

## Research Plan

### Gather
- Map original GMA methodology steps to existing TFW research stages
- Analyze HD-19 extract.md failure: which stage SHOULD have done which Zwicky step?
- Search: how do other frameworks embed structured analysis into iterative research without making it feel bureaucratic?

### Extract
- Design the concrete stage modifications: exact wording, exact template changes
- Test the proposed wording against HD-19 scenario: would the new templates have produced different behavior?
- Compare: standalone Zwicky section (iter 1 DR4) vs distributed heuristics (this hypothesis)

### Challenge
- Stress-test: does distributing Zwicky across stages dilute its power?
- Edge case: when the researcher doesn't have ≥3 parameters, does the Gather decomposition step still work?
- Risk: does embedding change the stage character? (Gather = observe, Extract = analyze, Challenge = stress — does Zwicky break these roles?)

## Scope Intent
- **In scope:** Stage template modifications, workflow wording, concrete before/after examples
- **Out of scope:** Changes to non-research workflows (plan.md, handoff.md — those use iter 1 decisions)

## Guiding Questions
1. Should the Gather template explicitly ask for "dimensions" (parameters) as part of finding structure, or is that too prescriptive?
2. Is the Extract stage the right place for enumeration+matrix, or should the matrix live in a new intermediate artifact?
3. Should CCA be a Challenge responsibility (stress-testing combinations) or an Extract responsibility (analytical reduction)?

## User Direction
{Record during briefing discussion}

---
Stage complete: YES (proceeding without wait — user said "Continue")
