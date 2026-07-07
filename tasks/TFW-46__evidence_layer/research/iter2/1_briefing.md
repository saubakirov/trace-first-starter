# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-46](../../HL-TFW-46__evidence_layer.md)
> Goal: Close the gap between "RF says done" and "actually works" by designing the Evidence Layer integration into TFW templates and workflows.

## Predecessor Context (Iteration 1)

### Decisions to build on
| # | Decision | Summary |
|---|----------|---------|
| D1 | "Evidence" is the correct term | Validated across 6 disciplines, triggers "show me artifacts" behavior per D28 |
| D2 | 4-status vocabulary: VERIFIED / DEFERRED / BLOCKED / N/A | AFD's 6-status rejected — TFW Evidence ≠ testing system |
| D3 | Proportional scope, not universal or mode-based | Coordinator calibrates evidence depth per AC in TS |
| D4 | Mixed artifact storage: optional `evidence/` subfolder + inline RF | Text evidence inline, binary evidence in folder when needed |
| D5 | Separate §5 Evidence in RF (not merged into §4) | Different cognitive modes: synthetic vs real. Renumbering §5-§8 → §6-§9 |
| D6 | Evidence field in TS §5 AC items, parallel to Gate | Gate = synthetic, Evidence = real. Per-AC integration |
| D7 | Evidence Audit extends REVIEW §2 Verify and §3 Judge | One new Judge check #7: "Evidence completeness" |
| D8 | Per-template naming: Evidence Plan (TS) / Evidence (RF) / Evidence Audit (REVIEW) | Three cognitive modes → three names |

### Open threads from iter1
| # | Thread | Why it matters |
|---|--------|---------------|
| 1 | H2: Can coordinators reliably write Evidence Plans? | If they can't → evidence planning shifts to executor autonomy |
| 2 | H4: Tooling coverage — what % can be automated? | Determines whether "proactive tooling" guidance belongs in TFW or stays project-specific |
| 3 | Anti-self-deception rules for conventions.md §14 | Without enforcement, agents mark VERIFIED without real artifacts |
| 4 | Evidence folder convention | Naming, placement (task-root vs phase-subfolder) |
| 5 | Handoff workflow integration point | Where does evidence collection sit in handoff.md? |

### User-injected directions
- Mode: deep (user-specified)
- Focus: internal synthesis — apply iter1 findings to concrete TFW design

## Research Plan

### Gather
- **G1:** Analyze current handoff.md flow — map every step, identify natural insertion point for evidence collection. Is it between Step 10 (build gate) and Step 11 (Pre-RF Gate)? Or a Phase 2.5 between Execution and RF?
- **G2:** Survey tooling landscape for evidence automation — MCP servers (browser, screenshot, CLI), Playwright/Puppeteer patterns, headless screenshot tools, CLI output capture. What's available out-of-box for agents?
- **G3:** Draft concrete Evidence Plan examples for 3 real tasks (AHA-6, HD-28, TFW-36 blog) — test whether coordinators can reliably write per-AC evidence requirements at TS time
- **G4:** Research anti-self-deception patterns from compliance/audit domains and AFD RUNBOOK — what structural rules prevent "VERIFIED without artifact"?
- **G5:** Analyze RF template renumbering impact — what files reference §5, §6, §7, §8 currently?

### Extract
- **E1:** Build Configuration Space: {Evidence collection placement × Tooling integration level × Anti-deception enforcement mechanism × Folder convention}
- **E2:** Cross-reference H2 (coordinator prediction) evidence plans against actual task complexity — does it scale from trivial (typo fix) to complex (payment system)?
- **E3:** Map tooling findings to TFW guidance level — framework-level vs project-level vs task-level

### Challenge
- **C1:** Stress-test evidence collection placement — does it break the handoff flow's cognitive rhythm?
- **C2:** Counter-evidence for coordinator prediction — what happens when the coordinator gets the evidence plan wrong? What's the fallback?
- **C3:** Challenge tooling coverage claim — what % of evidence TRULY cannot be automated? What does "proactive tooling" actually mean in practice?

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | Iter1 Status |
|---|-----------|-----------|--------------|
| H1 | Evidence can be domain-agnostic with fixed status vocabulary but domain-specific evidence types | open | 🟡 partially tested — domain catalog shows it works across 8 domains |
| H2 | Coordinator can reliably predict what evidence is needed at TS time | open | 🟡 partially tested — Gate/Evidence parallel works in theory |
| H4 | MCP + browser + CLI can cover 70%+ of evidence collection | open | ⏳ deferred from iter1 |
| H5 | Merging §4 + Evidence into one section is better than two separate | open | ❌ refuted in iter1 — separate sections confirmed |

## Scope Intent
- **In scope:** Workflow integration design (handoff, plan, review), anti-self-deception rules, tooling landscape survey, coordinator prediction validation, evidence folder convention, RF renumbering analysis
- **Out of scope:** Actual template implementation (that's TS/handoff work), writing TS, writing any code, modifying any TFW files

## Guiding Questions
1. When the executor finishes code + tests, what is the minimal-friction way to trigger evidence collection without breaking the handoff flow's cognitive momentum?
2. What concrete anti-self-deception rules can we borrow from compliance/audit that translate to AI agent behavior?
3. Is the 70% tooling automation threshold (H4) realistic, or is evidence fundamentally a human-verification activity?

## User Direction

1. **Thread priority:** Equal — all 5 open threads treated with same weight.
2. **Tooling to investigate:** Playwright MCP + DB MCP specifically. Other tools use simple APIs.
3. **H2 test tasks:** Agent decides — will use AHA-6, HD-28, TFW-36 as planned.
4. **Mode:** AG — no more questions, execute autonomously.

---
Stage complete: YES
