# ONB — TFW-48 / Phase B: Planning, Comparative Research, and Learning Routing

> **Date**: 2026-07-29
> **Author**: Executor (Codex)
> **Status**: 🟠 ONB — Awaiting Coordinator approval
> **Parent HL**: [Phase B HL](HL__phase-b__planning_research_learning.md)
> **Master HL**: [HL-TFW-48](../HL-TFW-48__value_first_methodology_rebaseline.md)
> **TS**: [TS Phase B](TS__phase-b__planning_research_learning.md)

---

## 1. Understanding

Phase B makes the planning and research consumer chain enforce the value-first Method
Kernel delivered and approved in Phase A. The work must connect purpose, applicable
Project Values, decision-changing uncertainty, human insights, comparative procedure
fit, evidence-based closure, and selected learning dispositions across exactly twelve
existing framework files. It must retire unsupported activity counts from workflow
authority without changing their config values, preserve one complete filesystem-traced
Briefing → Gather → Extract → Challenge → RES procedure, and keep H4 explicitly
unresolved with no strategy architecture or comparison execution.

## 2. Entry Points

| Area | Files | Role in Phase B |
|------|-------|-----------------|
| Semantic and operational owners | `.tfw/glossary.md`, `.tfw/conventions.md` | Own the Comparative Decision Procedure, research intensity, stop conditions, learning receipt contract, numeric dispositions, and Phase B transition boundary |
| Planning consumer | `.tfw/workflows/plan.md` | Frames purpose/uncertainty, traces Strategic Insights, checks procedure fit, and authorizes triggered iterations and TS |
| Research algorithm and intensity | `.tfw/workflows/research/base.md`, `.tfw/workflows/research/focused.md`, `.tfw/workflows/research/deep.md` | Consume the named comparative procedure, qualitative intensity, claim-based stage closure, and learning-selection gate |
| Planning/research synthesis templates | `.tfw/templates/HL.md`, `.tfw/templates/RES.md` | Carry insight implication/disposition and research learning routing without adding a new top-level capture surface |
| Stage templates | `.tfw/templates/research/1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md` | Preserve cross-stage natural dependency, procedure-fit evidence, qualitative sufficiency, and compact stage Learning Receipts |
| Read-only controls and verification | `.tfw/project_config.yaml`, `docs/scripts/test_gen_docs.py`, `docs/scripts/test_integration.py` | Confirm unchanged config and run the required generated-documentation checks |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking specification question was found. All 12 files exist, Phase A is approved, the Phase B TS is explicitly approved, and its scope/authority boundaries resolve against the current consumers. Explicit Coordinator approval of this ONB remains the execution gate. | _Coordinator approval required before implementation_ |

## 4. Recommendations (suggestions, not blocking)

1. Implement the consumer chain in dependency order: semantic owners first,
   planning/research workflows second, then output-shape templates. Verify AC-1 before
   beginning its dependent ACs.
2. Keep the Learning Receipt definition in conventions and use compact, structurally
   equivalent receipt shapes in stage templates. This avoids four competing
   definitions while preserving point-of-use observability.
3. Treat count retirement as an authority change, not a value migration: remove
   completion claims from consumers, retain the unchanged keys in config, and record
   every former count in the Phase B numeric disposition ledger.
4. Preserve current paths, stage filenames, `iterations.yaml` shape, and the canonical
   `## Fact Candidates` heading so later Phase D/E/F work has a stable migration seam.
5. Pair source scans with rendered-page inspection. TD-125/126 make repository-wide
   strict output noisy, so the evidence record should identify affected pages and links
   directly in addition to the required 68-test suite.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Structural floor regression:** removing `min_iterations`, loop, and count authority
   could be misread as permission to skip a stage. The complete filesystem trace and
   Coordinator closure authority must remain complete local gates.
2. **Implicit strategy selection:** a procedure-fit mismatch must return the unresolved
   information need to the Coordinator/user. Suggesting a replacement method in the
   same gate would violate the H4 boundary.
3. **Definition drift across templates:** four local receipt tables can silently diverge
   unless their fields point to the conventions owner and automated scans compare them.
4. **Transitional config ambiguity:** `min_iterations`, `max_passes`, and
   `loops_per_stage` remain visible in config after consumer authority changes. The
   conventions ledger and workflow wording must call this state transitional or
   unconsumed without implying deletion.
5. **Exact modified-file ceiling:** the TS uses all 12 allowed modified framework
   files. Any additional framework change—even an attractive cleanup—would exceed
   approved scope and must be reported rather than implemented.
6. **Legacy strict-build noise:** TD-125's 94 historical warnings and TD-126's broken
   philosophy hero can obscure unrelated documentation signals. Required tests and
   affected-link evidence must remain the Phase B gate.
7. **Phase D compatibility:** narrowing Fact Candidate entry without changing
   `/tfw-knowledge` can create temporary semantic tension. Phase B must state the
   downstream consumer is transitional rather than claim promotion closure is complete.

## 6. Inconsistencies with Code (spec vs reality)

1. The approved TS removes universal iteration-floor authority, while
   `.tfw/workflows/plan.md` currently requires completed iterations to meet
   `min_iterations` and creates further iterations solely from that count.
2. `.tfw/workflows/research/base.md` currently presents the stage sequence as generic
   research, repeats stages up to `loops_per_stage`, requires external research every
   stage, caps questions, and publishes a five-row count-based limits table.
3. The focused/deep mode files currently define intensity through fixed passes,
   cross-check counts, decisions, turns, loops, and hypotheses instead of qualitative
   evidence and challenge obligations.
4. The stage templates currently prescribe `3-5` plan bullets, `≤3` questions, `≥3`
   dimensions/alternatives, and a `>30` configuration sampling rule; none records a
   Learning Receipt.
5. `.tfw/templates/HL.md` records Strategic Insights without planning implication or
   TS disposition, and `.tfw/templates/RES.md` does not preserve
   destination/backlink/actor for promotion candidates.
6. `.tfw/conventions.md` still labels all workflow/template consumers transitional
   from Phase A, and `.tfw/glossary.md` has no concise definition for Comparative
   Decision Procedure or research intensity.

These are the intended Phase B implementation gaps, not blockers or reasons to expand
scope.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | [Phase A RF](../phase-a/RF__phase-a__method_kernel.md), Key Decisions 1–7 | ✅ | Applied | Preserves the four semantic owners, obligation-level proportionality, typed rule/proof/learning/numeric contracts, and H4 non-claim |
| 2 | [Phase A REVIEW](../phase-a/REVIEW__phase-a__method_kernel.md), APPROVE | ✅ | Applied | Establishes the predecessor as verified implementation: 9/9 AC, 68 tests, unchanged config, and valid owned anchors |
| 3 | [Iteration 2 RES](../research/iter2/RES.md), D15 and D18–D20 | ✅ | Applied | Governs disposition-typed receipts, numeric lifecycle, restore-owner-or-retire status, and T0-only H4 boundary |
| 4 | [KNOWLEDGE.md](../../../KNOWLEDGE.md), D22 | ✅ | Applied | Keeps Fact Candidates as inputs to verification rather than treating capture as knowledge |
| 5 | [KNOWLEDGE.md](../../../KNOWLEDGE.md), D23 | ✅ | Applied | Workflows retain algorithm/gates/references; templates own output shape |
| 6 | [KNOWLEDGE.md](../../../KNOWLEDGE.md), D37 | ✅ | Applied | Phase B does not alter the tfw-docs/tfw-knowledge ownership split or downstream promotion consumer |
| 7 | [KNOWLEDGE.md](../../../KNOWLEDGE.md), D43 | ✅ | Applied | Preserves the Project Values citation cascade instead of adding a duplicate insight/citation artifact |
| 8 | [KNOWLEDGE.md](../../../KNOWLEDGE.md), D49 | ✅ | Applied | Keeps TS requirements-first and preserves cross-stage structural dependency as natural enforcement |
| 9 | [KNOWLEDGE.md](../../../KNOWLEDGE.md), D51 | ✅ | Applied | Preserves copy-on-enter stage traces, stage mindsets/tests, checkpoints, and STOP gates |
| 10 | [KNOWLEDGE.md](../../../KNOWLEDGE.md), D55 | ✅ | Applied | Makes the five protected obligations and typed Phase A objects the governing Phase B authority |
| 11 | [knowledge/philosophy.md](../../../knowledge/philosophy.md), F3/F4/F13/F18/F24–F26 | ✅ | Applied | Requires critical opposition, structural rather than ceremonial gates, domain neutrality, context-specific cognitive prompts, human decision authority, and template duality |
| 12 | [knowledge/process.md](../../../knowledge/process.md), F3–F7/F13–F16/F22–F25 | ✅ | Applied | Guides precise names, algorithmic workflows, file-first traces, insight continuity, triggered iterations, citation/evidence honesty, and rejection of tautological guidance |
| 13 | [TFW-44 HL](../../TFW-44__coordinator_quality_gates/HL-TFW-44__coordinator_quality_gates.md), HL §11 → TS gap | ✅ | Applied | Resolves the live gap through HL implication/disposition and the Pre-TS gate while preserving the historical draft unchanged |
| 14 | **New:** [knowledge/philosophy.md](../../../knowledge/philosophy.md), F21 | ✅ | Applied | Explicit “no selected signal” makes intentional non-entry observable and reviewable without filler Learning Transactions |

All seven unique citation file targets resolve. Every cited D/F item named by the Phase
HL exists in its referenced source.

---

*ONB — TFW-48 / Phase B: Planning, Comparative Research, and Learning Routing | 2026-07-29*
