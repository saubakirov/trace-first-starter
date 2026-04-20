# RES — TFW-41: Execution Quality Gates

> **Date**: 2026-04-20
> **Author**: Researcher (AI)
> **Status**: ✅ RES_DONE — Iteration 1 complete
> **Parent HL**: [HL-TFW-41](HL-TFW-41__execution_quality_gates.md)
> **Mode**: Pipeline

---

## Research Context

TFW v3 pipeline produces correct artifacts but suffers from systematic execution quality failures: code-in-TS creates copy-paste executors, coordinator writes TS from own plan instead of actual RF, and research Extract stages pick the first viable option. This research investigates structural gates to prevent these failures at handoff points rather than catching them at review.

## Briefing

See [research/briefing.md](research/briefing.md). Deep mode, 4 hypotheses, focused on HD-9/HD-16/HD-18 case evidence.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| DR1 | **TS template: §4 → Acceptance Criteria, §5 → Technical Guidance (NOT code).** Replace `§4 Detailed Steps` with verifiable requirements. Guidance section renamed and repurposed: context, patterns, constraints — executor decides implementation. | HD-16/C (50KB code-in-TS → 96% AC, missed per_page) vs HD-18/C (11KB requirements-first → 100% AC). PO F24: «Меня не интересует код в ТС» |
| DR2 | **Pre-TS Gate: coordinator reads RF of latest completed phase in dependency chain before writing next TS.** | HD-18 coordinator self-assessment: 3/3 errors caused by reading own TS instead of RF. All 3 preventable by reading RF. |
| DR3 | **Execution Loops: mandatory when AC items have cross-component dependencies. Independent ACs → linear.** | H3 stress-test: loops add value for dependent chains (HD-16/C per_page depends on backend cap), but overhead for independent items (HD-18/D mechanical fixes). Threshold = dependency, not count. |
| DR4 | **Zwicky Box: mandatory in research Extract for ≥3 parameters. Comparison matrix for 1-2 parameters.** | HD-19 Zwicky = decorative (all Alt 1 selected, no CCA, no discovery). Live TFW-41 test: 4 configs survived from 1024 after CCA. |
| DR5 | **5 Zwicky enforcement rules, revised:** (1) ≥3 values/param, (2) CCA at parameter level, (3) no "recommended" before CCA, (4) ≥2 surviving configs OR elimination log, (5) document unexpected CCA survivors. | Challenge C3: R5 "non-obvious" is unverifiable → replaced with "unexpected survivor." R2 CCA at value-level impractical (448 checks) → parameter-level (28 checks). |
| DR6 | **HL §7 Principles → TS AC mapping table (mandatory).** Each TS must contain a table mapping HL principles to specific AC items that enforce them. | Extract E5: principles survive in text (HL §7) but die before execution. Mapping creates traceability chain: Principle → AC → Gate → RF verification. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| 1 | Should this be a TFW version bump (v3 → v4)? | Open | TS template §4 change is structural. Recommend: minor version (v3.1) — additive, not breaking. |
| 2 | Should Execution Loop dependency marking be coordinator's job or automated? | Open | Recommend coordinator: `[depends: AC-X]` annotation at TS write time. Automation requires parsing AC text — unreliable. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Requirements-first TS reduces "Phase D cleanup" phases | open | ✅ SUPPORTED | HD-16/C (code-in-TS, 50KB) → Phase D needed. HD-18/C (requirements-first, 11KB) → no Phase D. Same project/coordinator/executor. PO F24 confirms. |
| H2 | Pre-TS Gate (read RF N-1) eliminates plan≠fact drift errors | open | ✅ STRONGLY SUPPORTED | HD-18 coordinator self-assessment: 3/3 errors from reading own TS, not RF. All 3 preventable by reading RF N-1. |
| H3 | Execution Loops catch more issues than linear execution | open | ⚠️ CONDITIONALLY SUPPORTED | Loops catch dependent-chain failures (HD-16/C per_page). No value for independent items (HD-18/D). Threshold: dependency, not count. |
| H4 | Zwicky's Morphological Box improves research Extract quality | open | ⚠️ CONDITIONALLY SUPPORTED | HD-19 = decorative box (all Alt 1, no CCA). TFW-41 live test = genuine discovery (4 from 1024). Needs algorithmic enforcement (5 rules) to prevent simulation. |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | H1-H4 status: update from `open` to verdicts | This RES |
| 2 | Add DR1-DR6 decisions to HL §10 or new §11 | This RES |
| 3 | §2 Problems: add Problem #10 "Decorative Zwicky Box" evidence from HD-19 | extract.md E4-A |
| 4 | §3 Proposed Solutions: refine Execution Loops from "always" to "dependency-based" | challenge.md C2 |

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | process | **Coordinator behavior is knowledge-dependent, not template-dependent.** HD-16 coordinator continued writing code-in-TS until PO explicitly injected F24. Without knowledge entry, behavior reverted to default. Template enforcement is necessary because knowledge entries are per-project, but templates are framework-level. | PO feedback HD-16/D, process.md F24 | ★★★ |
| FC2 | process | **TS size inversely correlates with execution quality.** HD-16/C: 50KB → 96% AC. HD-18/C: 11KB → 100% AC. Mechanism: larger TS = more copy-paste surface, less executor thinking. Token budget spent on copying, not engineering. | HD-16/C vs HD-18/C comparison | ★★★ |
| FC3 | process | **Organic evolution validates proposed patterns.** HD-16/D HL independently invented Requirements-first + Gates pattern. HD-18/C TS independently used §4 AC instead of §4 Steps. Both emerged in response to failure — not by design. This means the pattern is discoverable by practitioners, but only after failure. | HD-16/D HL, HD-18/C TS | ★★☆ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | stakeholder | **PO explicitly values requirements over implementation: «Меня не интересует код в ТС. Требования которые нельзя обойти.»** This is a direct instruction to restructure the TS template from code delivery to requirements engineering. The PO sees TS as a specification document, not a code package. | PO, process.md F24, 2026-04-19 | ★★★ |
| SS2 | process | **User observed Zwicky Box simulation and diagnosed it immediately: "я вижу больше симуляцию... просто таблица ради таблица где выбрано все из первого столбца."** This confirms that without algorithmic enforcement, AI researchers optimize for completion (fill the box) rather than discovery (use the box). The workflow must make the CCA step non-skippable. | User, 2026-04-20, this research session | ★★★ |
| SS3 | process | **User treats TFW project as its own test bed: "tfw project itself may be [evidence of same problems]."** Meta-validation: the methodology project should exhibit the problems it aims to solve. TFW research iterations (TFW-22, TFW-24) show the same "first viable option" pattern in Extract stages. Self-referential evidence is the strongest validation for a methodology framework. | User, 2026-04-20 | ★★☆ |

## Findings Map

```
HD-16/C FAILURE                         HD-18/C SUCCESS
┌─ 50KB code-in-TS ─────┐              ┌─ 11KB requirements-first ──┐
│  Executor copies code  │              │  Executor engineers solution│
│  per_page=500 in text  │              │  Grep gates verify behavior │
│  Backend caps to 100   │              │  All 5 AC pass              │
│  Nobody checks runtime │              │  No Phase D needed          │
│  → Phase D cleanup     │              └────────────────────────────┘
└────────────────────────┘                        │
          │                                       │
          ▼                                       ▼
    PO gives F24                          Organic §4 AC pattern
    «Требования, не код»                  already in use
          │                                       │
          └────────── BOTH VALIDATE ──────────────┘
                          │
                    TFW-41 PROPOSAL
                          │
           ┌──────────────┼──────────────┐
           ▼              ▼              ▼
    DR1: TS template   DR2: Pre-TS    DR3: Execution
    §4=AC §5=Guidance  Gate (RF N-1)  Loops (deps)
           │              │              │
           └──────────────┼──────────────┘
                          ▼
                   DR6: HL§7 → AC
                   mapping table
```

```
ZWICKY BOX ANALYSIS
┌─ HD-19 (DECORATIVE) ───────┐    ┌─ TFW-41 (GENUINE) ──────────┐
│  8 params × 4 values       │    │  5 params × 4 values         │
│  All Alt 1 selected        │    │  1024 combinations            │
│  No CCA performed          │    │  CCA: 6 pairs eliminated      │
│  0 new discoveries         │    │  4 configs survived            │
│  = SIMULATION               │    │  1 unexpected survivor (C4)   │
└────────────────────────────┘    │  = GENUINE ANALYSIS            │
                                   └────────────────────────────────┘
         │                                    │
         ▼                                    ▼
   WHY IT FAILED                       5 ENFORCEMENT RULES
   • Pre-judged "recommended"          R1: ≥3 values/param
   • Dependent params                  R2: CCA parameter-level
   • No elimination step               R3: No pre-CCA recommendation
                                        R4: ≥2 survivors OR log
                                        R5: Document unexpected survivors
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 4 (max)
- **Hypotheses tested:** H1 (✅ supported), H2 (✅ strongly supported), H3 (⚠️ conditional), H4 (⚠️ conditional)
- **Hypotheses deferred:** None
- **Gaps discovered:** None critical. Minor: TFW project self-evidence is thin (only noted, not deeply mined)
- **Superseded decisions:** None

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | Execution Loop dependency annotation format | DR3 says "coordinator marks AC as dependent" — what's the exact syntax? | Define in TS template or conventions |
| 2 | Zwicky Box minimum parameter threshold (≥3) | C6 says ≥3 params → box, 1-2 → comparison matrix. Is 3 the right cutoff? | Test against past TFW research tasks |

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS

All 4 hypotheses have verdicts with evidence. 6 decisions ready for HL integration. Challenge refined thresholds and fixed over-constraining rules. Iteration 2 could deepen TFW self-evidence, but the core findings are stable — additional iteration would refine details, not change direction.

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

This research mined 3 Helpdesk task cases (HD-9, HD-16, HD-18) and TFW's own research history to validate 4 hypotheses about execution quality gates. The key finding: **TS content type directly causes execution quality** — code-in-TS produces copy-paste executors (HD-16/C, 50KB, 96% AC) while requirements-first TS produces engineering executors (HD-18/C, 11KB, 100% AC). The causal mechanism is clear: code TS spends executor tokens on copying, requirements TS spends them on thinking.

The Zwicky Box meta-test (H4) produced the most unexpected result: the box itself is a valid analysis tool (reduced 1024 combinations to 4 viable configurations with genuine discovery), but only when algorithmic enforcement prevents the "simulation" failure mode observed in HD-19. Without CCA, the box is decoration.

Self-critique: The evidence base is narrow (1 project, 3 cases). The controlled comparison (HD-16/C vs HD-18/C) is strong because confounding variables are naturally controlled, but generalizability to non-Helpdesk projects is assumed, not proven. TFW project self-evidence was noted but not deeply mined — iteration 2 could strengthen this.

---

*RES — TFW-41: Execution Quality Gates | 2026-04-20*
