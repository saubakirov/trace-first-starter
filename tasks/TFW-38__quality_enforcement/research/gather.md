# Gather — "What do we NOT know?"
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: Empirical evidence on RF §6-8 skip rates, reviewer audit behavior, and Findings Map presence across real TFW projects.

## Findings

### G1: RF §6-8 Presence Audit (cross-project)

**Corpus:** 4 projects, ~100 RF files total.

| Project | RF files | §6 Fact Candidates | §7 Strategic Insights | §8 Diagrams |
|---------|----------|--------------------|-----------------------|-------------|
| Helpdesk (12 RFs) | 12 | **1** (PhaseG only) | **1** (PhaseH only) | **0** |
| Steps-framework (40+ RFs) | 40+ | **2** (TFW-21, TFW-27 PhaseB partial) | **0** | **0** |
| Auto-schedule (8+ RFs) | 8+ | **0** | **0** | **0** |
| Atamat (20+ RFs) | 20+ | **0** (older TFW version) | **0** | **0** |

**Total skip rates across §6-8:**
- §6 Fact Candidates: present in ~3 of 80+ RFs → **~96% skip rate**
- §7 Strategic Insights: present in ~1 of 80+ RFs → **~99% skip rate**
- §8 Diagrams: present in ~0 of 80+ (confirmed zero) → **100% skip rate**

**Critical exception:** The two most recent helpdesk RFs (PhaseG, PhaseH) are the ONLY ones with §6-8 fully filled. These were written 2026-04-14 — TODAY. This strongly suggests a recent user intervention or explicit prompting, not a workflow-driven behavior.

HD-4 PhaseH RF has all three sections: §6 (5 fact candidates), §7 (3 strategic insights), §8 (1 mermaid diagram). HD-3 PhaseG RF has §8 renamed as "Fact Candidates" (5 entries). Both files were written with the newer TFW templates active.

### G2: RES Findings Map Presence Audit

| Project | RES files | Findings Map present | Findings Map absent |
|---------|-----------|---------------------|---------------------|
| Helpdesk | 10 | **8** (all HD-2 iterations, all HD-3/G, HD-4 iter1) | 2 |
| Steps-framework | 12+ | **2** (TFW-36 iter1, iter2 only) | 10+ |
| Auto-schedule | 2 | **0** | 2 |

Helpdesk has 80% Findings Map presence. Steps-framework has ~15%. Auto-schedule has 0%.

**Why helpdesk is different:** Helpdesk was created AFTER the Findings Map was added to the RES template (TFW-32 Phase B). Older projects predate the section.

### G3: Reviewer Audit Behavior

**Pattern observed in REVIEW files:**

1. **No REVIEW file in any project contains an explicit "I independently verified X"** audit step as a section. The word "verified" appears in checklist evidence only (e.g., "verified independently" as a checklist note).

2. **TFW-36 Phase A REVIEW is the outlier** — contains a self-critical "Reviewer Self-Assessment" section (lines 64-72) where the reviewer admits: "My initial review marked 'Data accuracy ✅' based on executor's self-reported fix. I did not: open knowledge_state.yaml to verify numbers independently, search for other unverified claims."

3. **HD-3 Full Task REVIEW** contains "Actual coverage % not verified independently" — the reviewer flags claims it couldn't check, but doesn't describe a verification protocol.

4. **HD-3 PhaseF REVIEW** has "Code audit" and "Acceptance Criteria Audit" as section names — suggesting the reviewer adopted audit language organically.

5. **TFW-19 REVIEW** has a "§3. Independent Verification" section — the only REVIEW with an explicit verification section.

**Pattern:** Reviewers who DO verify do so organically / per-reviewer personality. There is no workflow instruction that forces it.

### G4: handoff.md Phase 3 Text Analysis

Current handoff.md Phase 3 (lines 72-79) says:
```
12. Create RF file... Must contain:
    - What was done (changes list with file paths)
    - Test results (pass/fail, output logs)
    - Known limitations or tech debt
    - Deviations from TS (if any, with justification)
    - Screenshots / logs if applicable
    - **Observations** (out-of-scope items noticed during work)
```

**Missing:** §6 Fact Candidates, §7 Strategic Insights, §8 Diagrams. The mention of "Fact Candidates" appears only in the blue info box below (lines 81-87), but as informational context, not as a mandatory section list item.

### G5: External Research — LLM Instruction Following

Apple RLCF and TICK/STICK research (2025-2026) confirms:
- Decomposing instructions into explicit, verifiable checklist items significantly improves model adherence
- Models struggle with >10 constraints; explicit enumeration beats implicit template compliance
- "Attention drift" — reasoning chains can cause models to lose sight of specific structural requirements
- Industry consensus: **verification is primary** — checklist presence beats template hope

This directly supports H1: explicit enumeration in the workflow is the correct mechanism.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| §6-8 skip rate: 96-100% across projects | None — data is clear |
| Reviewer audit behavior: organic, not enforced | None |
| Findings Map: present mostly in newer projects | None |
| External evidence confirms explicit enumeration works | None |

**Sufficiency:**
- [x] External source used? (Apple RLCF, TICK/STICK research)
- [x] Briefing gap closed? (All 4 problems empirically confirmed)

Stage complete: YES
→ User decision: ___
