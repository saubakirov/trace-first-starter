# RES — TFW-38: Quality Enforcement

> **Date**: 2026-04-14
> **Author**: Researcher
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-38](HL-TFW-38__quality_enforcement.md)
> **Mode**: Pipeline

---

## Research Context

Empirical audit of TFW agent behavior across 4 active projects (helpdesk, auto-schedule, atamat, steps-framework) to validate that executors skip RF §6-8, reviewers rubber-stamp, researchers omit Findings Maps, and diagrams are abandoned. Goal: collect evidence to support or refute HL hypotheses before writing TS.

## Briefing

Pipeline research for TFW-38. Focus areas: (1) empirical skip rates for RF §6-8 across real projects, (2) actual reviewer audit behavior from REVIEW files, (3) RES Findings Map presence rates, (4) external research on LLM instruction-following patterns. Mode: focused (1 OODA loop per stage).

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | **Explicit §6-8 enumeration in handoff.md is the correct fix** | 96-100% skip rate empirically validated across 80+ RF files. Template presence is necessary but not sufficient. Only positive examples (HD PhaseG/H) correlate with user attention, not workflow instructions. Apple RLCF research confirms checklist decomposition beats implicit compliance. |
| D2 | **Reviewer audit step is needed but should include a triage gate** | Reviewers currently trust RF claims. Only TFW-19 has an explicit "Independent Verification" section. TFW-36 reviewer self-assessed: "I trusted executor's self-reported fix instead of verifying independently." But analytical/docs tasks would make file-level audit wasteful. Triage: code task → spot-check; docs task → verify existence. |
| D3 | **Diagram collection should INDEX, not COPY** | Zero diagrams collected in any project currently. Copying creates stale repositories. Better: add references to KNOWLEDGE.md §2 ("Architecture diagram → RF Phase G §8"). Diagrams stay in RF trace with full context. |
| D4 | **9 mandatory items in handoff Phase 3 is within the empirically validated constraint budget** | Apple RLCF research shows agents struggle with >10 constraints. Going from 6 to 9 stays under threshold. Each new item has "If empty, write 'No X'" fallback — zero content burden. |
| D5 | **Review workflow may benefit from research-like staged structure (Read → Verify → Challenge → Synthesize)** | User observation: the research flow's power comes from forced cognitive mode transitions. Current review is single-pass. Structured stages would make audit behavior reliable, not personality-dependent. Beyond TFW-38 Phase A scope — recommended as iteration 2 thread. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Which projects have the most RF/RES/REVIEW files? | ✅ Answered | Helpdesk (newest), atamat (most, older TFW), auto-schedule (few recent), steps-framework (most with current TFW) |
| Q2 | Are there positive examples of §6-8 being filled? | ✅ Answered | Only HD PhaseG/H (2026-04-14) — correlates with user quality discussion, not workflow. TFW-36 PhaseA also has all sections. |
| Q3 | Has diagram collection been attempted before? | ✅ Answered | No — never attempted in any form. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Adding explicit §6-8 enumeration to handoff.md Phase 3 will stop executors from skipping them | open | 🟢 supported | 96-100% skip rate with current workflow. Only filled when user explicitly focused on quality. Template alone insufficient. Apple RLCF confirms checklist decomposition works. 9 items < 10 constraint threshold. |
| H2 | An audit verification step in review.md will change reviewer behavior from "trust" to "verify" | open | 🟢 supported | TFW-36 reviewer admitted trust-chain failure. Only TFW-19 has independent verification. 2026 industry consensus: multi-gate review with deterministic verification for objective checks. Triage gate handles analytical task overhead. User proposes deeper restructure (staged review like research flow) — iteration 2 thread. |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | Phase B D6: change "storage location strategy" to "indexing strategy" — diagrams should be indexed in KNOWLEDGE.md, not copied to docs/diagrams/ | D3, Challenge C5 |
| 2 | Add H3: "Structured review stages (Read → Verify → Challenge → Synthesize) will produce more reliable reviews than a single-pass audit step" | D5, user observation |
| 3 | Consider adding Phase C: "Review Workflow Restructure" for the staged review concept, if iteration 2 confirms value | D5 |
| 4 | Risk R2 mitigation confirmed valid — triage gate for trivial/analytical tasks is the right approach | D2, Challenge C2 |

## Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Before writing:** review the conversation history. The human's messages are the primary source.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| F1 | process | RF §6-8 skip rate is 96-100% across 80+ RF files in 4 active projects. The template contains the sections with detailed instructions, but agents don't fill them because the handoff workflow doesn't enumerate them. Template ≠ enforcement. | Gather G1, cross-project grep | High |
| F2 | process | The only RF files with §6-8 filled (HD PhaseG, PhaseH, TFW-36 PhaseA) were produced in sessions where the user was actively discussing quality enforcement. The correlation is user attention, not workflow instruction. | Gather G1, positive example analysis | High |
| F3 | philosophy | User: review should be structured like the research flow — with explicit stages, cognitive mode transitions, and traces. The research flow forces the agent through gather → extract → challenge modes. Review is currently single-pass read-and-write. Structured stages would make audit behavior reliable, not personality-dependent. | User, 2026-04-14 | High |
| F4 | convention | TFW-19 REVIEW is the only REVIEW in the steps-framework project with an explicit "§3. Independent Verification" section. TFW-31 (scheduler) REVIEW has line-by-line DoD verification. Both emerged organically, proving the capability exists but is not reliably triggered. | Extract E4, Challenge C6 | High |
| F5 | process | RES Findings Map presence is 80% in helpdesk (newer project, post-TFW-32 template) vs 15% in steps-framework (older tasks predate the section). The presence correlates with template version at task creation time, not with workflow enforcement. | Gather G2 | Medium |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | philosophy | The user observes that review should follow the same structural pattern as research: forced cognitive mode transitions via explicit stages. This is a deeper insight than "add an audit step" — it suggests that ANY TFW workflow that requires quality judgment (research, review) should use the stage pattern, while workflows that are procedural (handoff, docs) can remain step-based. The implication: there are two classes of TFW workflows — investigative (staged) and procedural (linear). | User, 2026-04-14 | ★★★ |

## Findings Map

```
PROBLEM CHAIN (confirmed empirically)
══════════════════════════════════════

handoff.md Phase 3          review.md Step 1           research/base.md Step 6
lists 6 items               says "read RF"             lists 4 synthesis items
  ↓                           ↓                           ↓
§6-8 NOT listed             no audit instruction       Findings Map NOT listed
  ↓                           ↓                           ↓
96-100% skip rate            trust-chain failures       ~50% skip (newer projects)
across 80+ RFs              (TFW-36 self-assessment)    0% in older projects

        ↓                            ↓                          ↓
    ┌───┴───┐                   ┌────┴────┐                 ┌───┴───┐
    │  H1   │                   │   H2    │                 │  H1   │
    │CONFIRM│                   │ CONFIRM │                 │CONFIRM│
    └───────┘                   └─────────┘                 └───────┘

ROOT CAUSE (unified)
════════════════════
Template has section + instructions
        BUT
Workflow doesn't enumerate it
        =
Agent skips it (workflow wins over template)

EXTERNAL VALIDATION
═══════════════════
Apple RLCF: checklist decomposition > implicit compliance
2026 consensus: multi-gate review with deterministic verification
Constraint budget: <10 items per checklist (we're at 9)

NEW DIRECTION (user, iteration 2 candidate)
═══════════════════════════════════════════
Review → staged flow (Read → Verify → Challenge → Synthesize)
  ↓
Parallels research flow (Briefing → Gather → Extract → Challenge → RES)
  ↓
Two classes of TFW workflows: investigative (staged) vs procedural (linear)
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 3 (max)
- **Hypotheses tested:** H1 (🟢 supported), H2 (🟢 supported)
- **Hypotheses deferred:** None
- **Gaps discovered:** User proposed staged review structure (D5, SS1) — not in original HL
- **Superseded decisions:** None

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | Staged review workflow (Read → Verify → Challenge → Synthesize) | Could replace the "add Step 1.5 audit" approach with a structurally deeper solution. Parallels research flow design. User-initiated direction. | Analyze: does review benefit from cognitive mode transitions the same way research does? What would review stage files look like? Would this exceed the 1200-word budget? |
| 2 | Two classes of TFW workflows: investigative vs procedural | If confirmed, this is a framework-level design principle that affects future workflow design. | Map all 10 TFW workflows into investigative vs procedural. Do the investigative ones all need staged structure? |
| 3 | Diagram indexing vs copying in docs.md | D3 recommends indexing. Need to design the actual KNOWLEDGE.md §2 format for diagram references. | Concrete format proposal for KNOWLEDGE.md diagram index entries. |

### Recommendation
- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS
- [x] **MORE NEEDED** — Iteration 2 should explore the staged review concept (Thread #1). This is a user-directed structural change that could modify Phase A scope from "add audit step" to "restructure review as staged flow." The mechanical fixes (§6-8 enumeration, Findings Map mandate) are ready for TS. The review restructure needs one more iteration.

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Research iteration 1 validated both HL hypotheses with strong empirical evidence: 80+ RF files show 96-100% §6-8 skip rates, proving template-alone enforcement fails. External research (Apple RLCF, 2026 multi-gate review patterns) confirms that explicit checklist enumeration and deterministic verification gates are industry best practice. The iteration's most valuable discovery is the user's observation (D5/SS1) that review should be structured like the research flow — with staged cognitive modes rather than a single-pass audit step. This opens a potentially deeper redesign that warrants exploration in iteration 2 before writing the TS for Phase A.

---

*RES — TFW-38: Quality Enforcement | 2026-04-14*
