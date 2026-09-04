# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260904-113200_VBSA](../../HL-TFW_20260904-113200_VBSA.md)
> Goal: Determine whether TFW can govern the size of accepted delivery with one stable, value-bearing accounting rule without taxing trace or assurance work, and whether a hard numerical ceiling is still the right control.

## Research Plan

### Briefing

- Treat H1–H5 as falsifiable together: classification, assurance exclusion, carrier sufficiency, control choice, and historical replay must form one internally consistent result.
- Use the frozen HL as the contract and `research/iterations.yaml` as the iteration boundary; classify any recommendation to a frozen section as an amendment proposal rather than editing the HL.
- Apply subtraction before addition: first test removing whole-tree totals, redundant counts, and hard-limit mechanics before proposing any new field, selector, manifest, script, or configuration key.

### Gather

- Reconstruct the actual baselines, candidates, counted surfaces, and review disputes in TFW RCFR Phase A; Helpdesk BIAI Phase A; and representative completed AFD evidence, read-only.
- Inventory the current TFW budget carriers and consumers in conventions, planning, TS, RF, EV, review, adapters, and structural tests.
- Decompose the decision into at least three independent dimensions: governed subject, control strength, authority boundary, selector/carrier, metric applicability, and assurance treatment.
- Consult external primary or authoritative sources on work-size controls, change authority, and measurement validity; distinguish evidence about decision quality from mere popularity of a method.

### Extract

- Build a cross-corpus classification matrix for `VALUE`, `ASSURANCE`, `TRACE`, and `DERIVED`, including accepted test products, accepted generated outputs, task-local deliverables, renames, deletions, binaries, and shared files.
- Compare configurations combining hard ceilings, soft decomposition triggers, non-numeric controls, and bounded Coordinator authority inside unchanged approved outcomes.
- Identify the smallest existing carrier set that can preserve one baseline/candidate/classification/method contract across Executor and Reviewer without a standalone manifest or new configuration key.
- Separate delivery-size decisions from assurance sufficiency and review workload so exclusion from one mechanism never removes another gate.

### Challenge

- Try to game every class by hiding necessary product implementation in `ASSURANCE`, `TRACE`, or `DERIVED`, and test whether explicit accepted-delivery precedence closes the loophole.
- Replay candidate rules against RCFR, BIAI, and AFD to test stability, false-overrun removal, and detection of genuine value growth.
- Attack hard ceilings as a mechanism: test decision usefulness, waiver behavior, metric comparability, false precision, and the authority needed for justified growth inside unchanged outcomes.
- Reject configurations that require competing totals, mutable reference pairs, self-invalidating trace counts, unbounded Coordinator discretion, or new machinery without a demonstrated unique reader.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | `VALUE`, `ASSURANCE`, `TRACE`, and `DERIVED`, with semantic precedence for explicitly accepted deliverables, classify the observed TFW, Helpdesk, and AFD cases without contradiction. | needs-research |
| H2 | Ordinary tests can default to excluded `ASSURANCE` without weakening delivery quality because evidence, review, safety, and proportionality gates remain independently binding. | needs-research |
| H3 | Existing TS/RF/EV/review carriers can hold one deterministic selector and fixed baseline/candidate contract; no standalone budget manifest or new configuration key is necessary. | needs-research |
| H4 | Hard upper scope budgets remain the right mechanism for decomposition and drift control; applying them to `VALUE` with delivery-appropriate metrics and bounded Coordinator authority is more effective than replacing hard ceilings with a softer or non-numeric structural control. | needs-research; explicit out-of-the-box challenge required |
| H5 | Replaying the proposed rule against TFW RCFR, Helpdesk BIAI, and completed AFD phases yields one stable classification per corpus and removes the observed false overrun or self-reference without hiding genuine product growth. | needs-research |

## Scope Intent

- **In scope:** Iteration 1 only; H1–H5; current TFW budget rules and role/template consumers; read-only reconstruction of TFW RCFR, Helpdesk BIAI, and representative completed AFD evidence; external authoritative evidence; classification and control alternatives; bounded authority inside unchanged approved outcomes; backward-compatible recommendations.
- **Out of scope:** Any edit to the frozen HL, TS, implementation, canonical framework, historical task, AFD, or Helpdesk; migration or correction of historical counts; iteration 2; a new configuration key, manifest, registry, script, or maintained artifact unless the evidence first disproves all existing-carrier options.

## Guiding Questions

1. Which changed surfaces constituted accepted value in each corpus, and can four semantic classes assign them consistently without relying on paths or extensions?
2. Which control actually changes decisions with the least distortion: hard ceilings, soft triggers, non-numeric structural gates, bounded Coordinator authority, or removal of numerical scope budgets?
3. What is the smallest existing-carrier contract that makes planning, execution, and review reproduce the same result from fixed references while leaving assurance and trace obligations fully binding?

## External Planning Anchors

- The official [Scrum Guide](https://scrumguides.org/scrum-guide.html) separates a protected Goal from scope that can be clarified or renegotiated as learning occurs. This made authority inside an unchanged approved outcome an explicit research dimension rather than an assumed waiver rule.
- Google's [Small CLs guidance](https://google.github.io/eng-practices/review/developer/small-cls.html) treats conceptual cohesion and reviewer judgment as more important than one hard-and-fast size rule. This required the investigation to compare hard ceilings with soft and nonnumeric controls instead of merely repairing the counted subset.

These sources frame questions; they do not predetermine the answer or supply a TFW-specific threshold.

## User Direction

- The owner assigned iteration 1 to investigate all five hypotheses and explicitly required an out-of-the-box challenge of whether hard upper scope budgets should exist at all.
- Compare hard ceilings, soft decomposition triggers, non-numeric controls, and bounded Coordinator authority for implementation growth inside unchanged approved outcomes.
- Reconstruct TFW RCFR, Helpdesk BIAI, and representative completed AFD evidence read-only; never modify those histories or either external project.
- Apply subtraction before addition and do not assume a new manifest or configuration key is necessary.
- Produce the complete iteration trace and English `RES.md`, commit only those iteration artifacts locally with TFW attribution, and do not push.

---
Stage complete: YES
