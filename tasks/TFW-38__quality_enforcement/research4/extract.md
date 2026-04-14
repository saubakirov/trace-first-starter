# Extract — Iteration 4
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: Design citation and diagram creation mandates.

## Thread A: Knowledge Citation Mandate

### E1: Citation Format Design

The coordinator currently writes HL with D-numbers for **intra-task** decisions (D4, D16, D-A1.1). The gap is **cross-task** knowledge from KNOWLEDGE.md.

**Proposed citation format:** Same as existing D-number pattern, but with KNOWLEDGE.md source marker:

```markdown
## 4. Context
...
Relevant project knowledge:
- K:arch.workers — "No Celery. asyncio workers in-process" (KNOWLEDGE.md §1.3)
- K:pitfall.timezone — "Yandex Cloud PG default = Europe/Moscow" (KNOWLEDGE.md §3.1)
```

**But this requires KNOWLEDGE.md to have stable section numbering.** Alternative: reference by topic file:

```markdown
- knowledge/engineering.md: "No Celery mandate"
- knowledge/operations.md: "timezone pitfall — Yandex Cloud PG"
```

**Simpler:** Just require the coordinator to mention which KNOWLEDGE.md items apply. No rigid format — the trace itself is proof of reading.

### E2: Coordinator Citation Mandate — Placement in plan.md

**Where to add:**
- plan.md Step 3 ("Research & Understand") already says "read relevant code, existing HL files, knowledge items."
- Add after Step 3.3: **"Check KNOWLEDGE.md — list applicable architecture decisions, known pitfalls, and existing patterns. Reference them in HL §4 (Context) with source markers."**

**HL template change:**
- HL §4 currently: "Summarize existing code/architecture context."
- Update: add sub-prompt "Relevant KNOWLEDGE.md items: list applicable decisions with references. If no KNOWLEDGE.md exists or nothing applies, write 'No applicable knowledge items.'"

This forces an explicit acknowledgment — either citations or conscious N/A.

### E3: Executor and Researcher Citation

**Executor:** In ONB, the executor identifies inconsistencies. If KNOWLEDGE.md documents "no Redis dependency" and TS Step 5 introduces Redis — the executor should catch this. Currently handoff.md says "Inconsistencies between HL/TS and actual code" — doesn't mention KNOWLEDGE.md.

**Fix:** Add to handoff.md Phase 1, step 2 bullet: "Inconsistencies between HL/TS and **KNOWLEDGE.md/actual code**"

**Researcher:** Already loads KNOWLEDGE.md in Step 1. The gap is in synthesis — RES should note when findings confirm or contradict existing knowledge. But this is naturally addressed by the Fact Candidates section (which compares results against known facts).

**Verdict:** Primary mandate is on the coordinator (most impact). Executor gets a minor addition. Researcher doesn't need changes.

## Thread B: Diagram Creation Mandate

### E4: Why HL §3.1 Succeeds

plan.md Step 4.3: "Fill §3.1 (visualization) — create ASCII visualization of To-Be **(mandatory).** Add mermaid if flow is complex."

The key word is **"mandatory"** + explicit step number. The agent knows: "I cannot skip Step 4.3."

### E5: Fix for RF §8 — Handoff.md Phase 3

Current handoff.md Phase 3 (lines 72-79) lists 6 bullet items for RF content. None mention §8 Diagrams.

**Fix:** Add explicit bullet to Phase 3:

```markdown
- **Diagrams** — architecture, data flow, sequence diagrams for the work done.
  If no diagrams are relevant, write "No diagrams." in §8. Do NOT leave §8 empty.
```

This mirrors the RF template §8's own text — but now it's in the WORKFLOW, not just the template. Per iter 1 root cause: the workflow is what agents follow, not the template header.

### E6: Fix for RES Findings Map — research/base.md Step 6

Current research/base.md Step 6 lists:
1. RES file
2. HL Update Recommendations  
3. Fact Candidates
4. Iteration Status block
5. Conclusion

**Missing:** Findings Map. The template has it (RES.md §Findings Map), but the workflow doesn't list it.

**Fix:** Add to Step 6 list:

```
5. **Findings Map** — visual diagram showing relationships between key findings, decisions, 
   and hypotheses. Use ASCII, mermaid, or structured table. 
   This is the diagram that docs.md will index in KNOWLEDGE.md §2.
```

### E7: Full Diagram Enforcement Chain (Complete)

After fixes:

```
WHO creates       MANDATE             WHERE stored   WHO collects   WHERE indexed
────────────────────────────────────────────────────────────────────────────────
Coordinator →  plan.md §4.3          → HL §3.1     → docs.md    → KNOWLEDGE.md §2
               "mandatory"

Executor    →  handoff.md Phase 3    → RF §8       → docs.md    → KNOWLEDGE.md §2  
               "If no diagrams,                       
               write 'No diagrams'"            

Researcher  →  research/base.md §6   → RES         → docs.md    → KNOWLEDGE.md §2
               "Findings Map —                        
               visual diagram"                              
```

Every link in the chain now has an explicit mandate. Creation → Storage → Collection → Indexing.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Citation mandate: coordinator in plan.md Step 3 + HL §4. Executor in handoff.md Phase 1 (minor) (E2, E3) | Challenge |
| Diagram mandate: handoff.md Phase 3 for RF §8, research/base.md Step 6 for Findings Map (E5, E6) | Challenge |
| Complete chain: create → store → collect → index (E7) | None |

**Sufficiency:**
- [x] External source used? (iter 1 root cause model: workflow-template disconnect)
- [x] Briefing gap closed?

Stage complete: YES
→ Close Extract, proceed to Challenge.
