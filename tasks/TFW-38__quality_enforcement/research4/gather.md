# Gather — Iteration 4
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: (A) Knowledge citation gaps, (B) Diagram creation gaps.

## Thread A: Knowledge Citation

### G1: Current KNOWLEDGE.md References in Workflows

| Workflow | Where Referenced | How Referenced | Action Mandate? |
|----------|-----------------|----------------|-----------------|
| **plan.md** Step 1 | "KNOWLEDGE.md read" | Context loading list | ✅ Read — but no citation |
| **plan.md** Step 3 | "read relevant code, existing HL files, knowledge items" | Part of research | ⚠️ "knowledge items" vague |
| **handoff.md** Context Loading | "#4 KNOWLEDGE.md — architecture, decisions, legacy (if exists)" | Context loading list | ✅ Read — but no citation |
| **research/base.md** Step 1 | "KNOWLEDGE.md" in context loading | Part of Step 1 | ✅ Read — but no citation |
| **docs.md** | "Read KNOWLEDGE.md — current state" | First step | ✅ Read — this workflow WRITES to it |
| **knowledge.md** | Core subject of workflow | Throughout | ✅ |

**Gap:** KNOWLEDGE.md is listed as something to READ in context loading. But NO workflow says:
- "Cite relevant decisions (D-numbers) from KNOWLEDGE.md in your output"
- "Reference specific architecture facts when they influence your design"
- "Prove you read KNOWLEDGE.md by including applicable D-numbers"

### G2: Citation Patterns in Real HL/TS Files

Looking at the best HL/TS files from helpdesk:

**HD PhaseD TS §1:** "D-A1.1 (auto-priority), D4 (optimistic lock), D10 (advisory lock), D16 (SLA calendar)" — these are HL decision numbers, NOT KNOWLEDGE.md references.

**HD PhaseF TS §3:** "D18 (pain score formula), D27 (degradation levels)" — same pattern.

**Atamat TFW-16 PhaseH:** "TFW-16 Phase H" markers everywhere, but no KNOWLEDGE.md architecture citations.

**Pattern:** Coordinators cite HL decisions (D-numbers from the same task). They do NOT cite cross-task knowledge (from KNOWLEDGE.md). This means:
- The coordinator operates within the task silo
- Cross-task knowledge (past decisions, architectural patterns, known pitfalls) is NOT being applied even when it exists

**Example:** HD PhaseF uses asyncio workers. KNOWLEDGE.md for steps-framework has no asyncio pattern — but helpdesk KNOWLEDGE.md (if it exists) might have worker patterns. The coordinator didn't cite any cross-task reference.

### G3: Who Should Cite Knowledge?

| Role | When | What to Cite | Value |
|------|------|-------------|-------|
| **Coordinator** (plan.md) | Writing HL §4 (context), TS §6 (constraints) | Architecture decisions, known pitfalls, existing patterns from KNOWLEDGE.md | Prevents reinventing known patterns. Avoids known pitfalls. |
| **Executor** (handoff.md) | Writing ONB (Inconsistencies), RF §6-7 (Fact Candidates) | Relevant KNOWLEDGE.md facts when they confirm/contradict TS | Validates that TS aligns with project knowledge |
| **Researcher** (research/base.md) | Writing RES (Decisions, Fact Candidates) | KNOWLEDGE.md facts that relate to research findings | Avoids rediscovering known facts |
| **Reviewer** (review.md) | Judge stage — checklist | Check if executor considered relevant KNOWLEDGE.md items | Catches knowledge gaps in implementation |

## Thread B: Diagram Creation

### G4: Where Diagrams Should Be Created

| Artifact | Section | Template Says | Workflow Says | Skip Rate |
|----------|---------|---------------|---------------|-----------|
| **RF** | §8 Diagrams | "Visualize architecture, data flow, component interaction... If no diagrams are relevant — write 'No diagrams.'" | **NOTHING** — handoff.md Phase 3 doesn't mention §8 | ~96% (from iter 1) |
| **RES** | Findings Map | "Formats: ASCII, mermaid, or structured tables... for validated findings" | **NOTHING** — research/base.md Step 6 lists 4 synthesis items, Findings Map not among them | ~50% newer, ~85% older |
| **HL** | §3.1 | "mermaid diagram — for complex multi-path flows" | plan.md Step 4.3: "create ASCII visualization of To-Be (mandatory)" | Low — plan.md DOES mandate it |

**Key insight:** HL §3.1 diagrams are NOT skipped because plan.md Step 4.3 **explicitly says "mandatory."** This is the same root cause as §6-8: the workflow must enumerate the section for agents to fill it.

### G5: The Diagram Creation Chain

```
WHO creates → WHERE stored → WHO collects → WHERE indexed
────────────────────────────────────────────────────────
Coordinator → HL §3.1      → docs.md    → KNOWLEDGE.md §2
Executor    → RF §8        → docs.md    → KNOWLEDGE.md §2 ← MISSING: creation mandate
Researcher  → RES Findings → docs.md    → KNOWLEDGE.md §2 ← MISSING: creation mandate
```

The chain breaks at "creation mandate" for executor and researcher. Collection (docs.md) is solved by D10 from iter 2. But you can't collect what was never created.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| KNOWLEDGE.md is read but never cited (G1-G2) | Design citation mandate |
| Coordinator should cite D-numbers from KNOWLEDGE.md in HL/TS (G3) | Where exactly in plan.md |
| Diagram creation fails because handoff.md and research/base.md don't mention it (G4-G5) | Design creation mandate |
| HL §3.1 succeeds BECAUSE plan.md says "mandatory" (G4) | Proof: same fix works |

**Sufficiency:**
- [x] External source used? (Root cause model from iter 1 applied)
- [x] Briefing gap closed? (Both gap analyses complete)

Stage complete: YES
→ Close Gather, proceed to Extract.
