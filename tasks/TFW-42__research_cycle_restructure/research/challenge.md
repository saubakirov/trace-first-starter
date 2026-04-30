# Challenge — "What do we NOT expect?"
> Parent: [HL-TFW-42](../../HL-TFW-42__research_cycle_restructure.md)
> Goal: Determine how TFW should present multi-agent research orchestration to users via iterations.yaml.

## Consistency Check

Take each pair of dimensions and ask: "Can Alternative X coexist with Alternative Y?"

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1: Agent spec | No agent field | D3: Guidance | Active suggestion | Cannot actively suggest agent assignment if there's no field to assign to |
| D1: Agent spec | No agent field | D3: Guidance | Prompt-in-template | Cannot prompt about a field that doesn't exist |
| D1: Agent spec | Enum from registry | D3: Guidance | Document-only | Registry requires framework-level support, can't be document-only |
| D1: Agent spec | Structured profile | D2: Dependency | None (sequential) | Complex agent profiles without dependency tracking is mismatched complexity |
| D2: Dependency | DAG | D3: Guidance | Document-only | DAG dependencies are too complex to be documentation-only — need workflow enforcement |

**Surviving configurations** (from Extract's Configuration Space, after removing rows containing incompatible pairs):

| Config | D1: Agent spec | D2: Dependency | D3: Guidance | Notes |
|--------|---------------|----------------|-------------|-------|
| C1 | Free-text name | Linear chain | Document-only | Minimal viable. Agent field exists, docs explain it, deps are simple |
| C2 | Free-text name | Linear chain | Prompt-in-template | **Best balance.** Template includes agent field with guidance comment. Linear deps. Low overhead |
| C3 | Free-text name | Linear chain | Active suggestion | More prescriptive than C2. plan.md actively asks coordinator to assign agents |
| C9 | No agent field | Implicit | Document-only | Status quo for single-agent projects. Valid but ignores multi-agent |
| C10 | Free-text name | None (sequential) | Prompt-in-template | Like C2 but no `depends_on`. Simpler, but loses future flexibility |
| C11 | Free-text name | Implicit | Prompt-in-template | Like C10 but without explicit dependency field. Relies on sequential reading |

**Unexpected survivors:**
- **C10 (Free-text + None + Prompt-in-template):** Survived despite having no `depends_on` field. This is unexpected because HL-TFW-42 proposes `depends_on`. But empirically (AFD-2), dependencies were always linear-sequential. If iterations are always numbered and each reads the predecessor, `depends_on` adds no information. The iteration NUMBER is the dependency.

## Findings

### C1: Stress-testing C2 (front-runner) against edge cases

**Edge case 1: Single-agent project (most common case)**
- C2 behavior: iterations.yaml template has `agent:` field with comment `# optional — tool/agent for this iteration`. Single-agent user ignores it or writes the same name everywhere.
- Risk: Noise. Mitigation: field is optional, comment says so. Acceptable.

**Edge case 2: 3+ agents on one task**
- C2 behavior: Each iteration gets `agent: <name>`. Linear `depends_on` chain. 
- Risk: What if iter 3 depends on both iter 1 AND iter 2 (not just iter 2)? Linear chain can't express this.
- Analysis: In AFD-2's 8 iterations, this never happened. Each iteration consumed the PREVIOUS iteration's RES, not arbitrary earlier ones. The research workflow already handles multi-predecessor context through the Iteration Status block's "Open Threads" — which lists ALL unresolved threads, not just from the immediate predecessor.
- Verdict: Linear is sufficient. If DAG ever needed, it's a future evolution, not a v1 requirement.

**Edge case 3: Agent becomes unavailable mid-task**
- C2 behavior: Coordinator updates iterations.yaml, changes `agent` for remaining iterations.
- Risk: None — iterations.yaml is a living document, coordinator owns it.
- Verdict: No issue.

**Edge case 4: New agent/tool appears after iterations.yaml written**
- C2 behavior: Free-text name means any string is valid. No registry to update.
- Risk: None — this is exactly why free-text beats enum.
- Verdict: No issue. Advantage over C7/C8 (enum-based).

### C2: Stress-testing the `depends_on` field (proposed in HL-TFW-42)

**The case FOR `depends_on`:**
- Explicit sequencing visible in YAML
- Future-proofing for non-linear research patterns
- Aligns with TS `[depends: AC-X]` pattern (D49)

**The case AGAINST `depends_on`:**
- AFD-2 empirical: ALL dependencies were linear. `depends_on: [1]` for iter 2, `depends_on: [2]` for iter 3, etc. This is just restating the iteration number.
- Research workflow already enforces sequential reading: Step 0 says "read predecessor RES files for context"
- Adding `depends_on` to every iteration is pure noise for the common case
- YAGNI principle: no evidence this will be needed

**Counter-argument to YAGNI:** The `[depends: AC-X]` pattern in TS (D49) was introduced specifically for non-linear execution. Should iterations match this pattern for consistency?
- Response: No. AC items within a single TS are fine-grained (10-20 items, complex dependencies). Research iterations are coarse-grained (2-8 items, sequential). Different granularity = different dependency model is appropriate.

**Verdict: Drop `depends_on` for v1.** The iteration number IS the dependency. research/base.md Step 0 already reads predecessors. If DAG research ever becomes real, add `depends_on` as an optional field in a future TFW version.

### C3: Testing H1 — iterations.yaml `agent` field vs separate mechanism

**H1: "Multi-agent orchestration needs `agent` field in iterations.yaml, not a separate mechanism"**

**Evidence FOR H1 (agent field in iterations.yaml):**
1. CrewAI parallel: `agent:` field on task YAML is the industry standard for YAML-based frameworks
2. AFD-2 empirical: agent assignment was per-iteration, which maps directly to a field on the iteration entry
3. Locality principle (HL §7 P1): agent assignment near iteration focus/hypotheses = related data co-located
4. No new files needed: extends existing YAML, not a new mechanism
5. Optional: single-agent projects ignore it

**Evidence AGAINST H1 (separate mechanism):**
1. Separation of concerns: agent capabilities are metadata about tools, not about the task
2. A separate `.tfw/agents.yaml` could define available agents with strengths
3. Other frameworks (MetaGPT, CrewAI) DO define agents separately

**Critical analysis:**
The "separate mechanism" argument fails for TFW because:
- TFW agents are EXTERNAL TOOLS, not LLM instances. Their capabilities are known to the human, not to the framework.
- A `.tfw/agents.yaml` defining "Antigravity is good at web research" would be: (a) always stale, (b) specific to one user's setup, (c) adding framework maintenance for no enforcement value.
- The coordinator (human) already knows which tool to use. The `agent` field is for TRACEABILITY, not for DISPATCH.

**H1 verdict: CONFIRMED.** The `agent` field in iterations.yaml is sufficient. No separate mechanism needed.

### C4: Final schema recommendation

Based on surviving configurations (C2 winner) and field analysis (Extract E4-E6):

**Proposed iterations.yaml enrichment:**

```yaml
iterations:
  - number: 1
    focus: >
      Multi-line description of what this iteration investigates.
      This serves as both summary and brief.
    hypotheses: [H1, H2]
    status: pending          # pending | in_progress | complete
    res_file: RES.md         # now inside research/iter1/
    agent: antigravity       # optional — tool/agent for this iteration
    sources: [external, codebase]  # optional — expected research sources
```

**Fields dropped from HL-TFW-42 proposal:**
- `brief` — redundant with `focus` (which already supports multiline YAML)
- `notes` — catch-all with no clear purpose
- `depends_on` — iteration number IS the dependency; no DAG evidence

**Fields kept:**
- `agent` — free-text, optional. For traceability, not dispatch.
- `sources` — list, optional. Planning hint for researcher about expected source types.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C2 (free-text + linear + prompt-in-template) is the winning configuration | None |
| H1 confirmed: agent field in iterations.yaml, no separate mechanism | None |
| 3 fields dropped (brief, notes, depends_on) — schema simplified | None |
| 4 edge cases tested, all passed | None |

**Sufficiency:**
- [x] External source used? (CrewAI task-agent binding pattern as validation)
- [x] Briefing gap closed? (H1 fully tested with evidence for and against)
- [x] Pairwise incompatibility checked? (5 incompatible pairs, 6 surviving configs)

**Deep mode criteria:**
- [x] Hypothesis tested? (H1 CONFIRMED with structured evidence)
- [x] Counter-evidence sought? (depends_on YAGNI, separate mechanism failure analysis, single-agent overhead)

**Metacognitive check:** I discovered something NEW — the `depends_on` field is unnecessary because iteration numbers are inherently sequential AND the research workflow already enforces predecessor reading. This is a genuine simplification, not just confirmation bias. The distinction between "traceability" and "dispatch" for the agent field is also a new framing not present in the HL.

Stage complete: YES
→ User decision: proceed (autonomous mode)
