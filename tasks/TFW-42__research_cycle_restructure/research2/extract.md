# Extract — "What do we NOT see?" (Iteration 2)
> Parent: [HL-TFW-42](../../HL-TFW-42__research_cycle_restructure.md)
> Goal: Map agent capabilities for research subtasks and formalize how TFW guides coordinators in agent selection.

## Configuration Space

From 3 dimensions × 3 alternatives = 27 theoretical. Reduced to 9 meaningful after removing contradictions.

| Config | D1: Guidance specificity | D2: Guidance location | D3: Decision model |
|--------|-------------------------|----------------------|-------------------|
| C1 | Generic archetypes | Comment in template | Human decides, no rec |
| C2 | Generic archetypes | Table in conventions | Human decides, decision table |
| C3 | Generic archetypes | Prompt in plan.md | Human decides, decision table |
| C4 | Capability-based | Comment in template | Human decides, no rec |
| C5 | Capability-based | Table in conventions | Human decides, decision table |
| C6 | Capability-based | Prompt in plan.md | Human decides, decision table |
| C7 | Tool-specific | Table in conventions | Human decides, decision table |
| C8 | Tool-specific | Comment in template | Framework suggests |
| C9 | Capability-based | Table in conventions + comment in template | Human decides, decision table |

## Findings

### E1: Why C9 (hybrid) emerges as strongest

C9 combines the best of two locations:
1. **Table in conventions.md** — capability categories table (tool-agnostic). Coordinator can reference when planning.
2. **Comment in iterations.yaml template** — brief nudge at the decision point. Just enough to trigger "should I consider multi-agent?"

This mirrors the Pattern A approach (D24): enforcement-critical values inline, detail via reference.

The table in conventions.md would look like:

```markdown
### Agent selection guidance

When planning multi-iteration research, consider whether different iterations
would benefit from different tools based on their primary research activity:

| Research activity | Key capability | Example tools |
|-------------------|---------------|---------------|
| Web research, competitive analysis | Web search, large context | IDE agents with web search |
| Code audit, dependency analysis | File traversal, shell commands | Terminal/CLI agents |
| Infrastructure reconnaissance | MCP integration, interactive sessions | Agents with MCP support |
| Architecture synthesis | Large context window (500K+) | Agents with extended context |
| Data analysis | Database MCP servers | Agents with data source access |

> The `agent` field in `iterations.yaml` records which tool was used (optional).
> Coordinator decides — this table is guidance, not prescription.
```

**Key design decisions in this table:**
- **No tool names** — says "IDE agents with web search" not "Antigravity"
- **"Example tools" column left generic** — project-specific mapping lives in KNOWLEDGE.md
- **5 rows, not 8** — collapsed the 8 subtask types from Gather G2 into 5 research activities (merged overlapping types)
- **Footer clarifies** — guidance, not prescription

### E2: The template comment design

In `.tfw/templates/research/iterations.yaml` (or conventions.md §4 schema example):

```yaml
iterations:
  - number: 1
    focus: >
      What this iteration investigates.
    hypotheses: [H1, H2]
    status: pending
    res_file: RES.md
    # agent: tool-name    # optional — which tool/agent runs this iteration
    # sources: [external, codebase]  # optional — expected research source types
```

The comment is minimal — just field name + one-word description. The conventions.md table provides detail for those who want it.

### E3: plan.md Step 6b integration

Current plan.md Step 6b creates iterations.yaml. The change is minimal:

Add one sentence after the existing instruction:
> "For multi-iteration research, consider whether different iterations would benefit from different tools. See conventions.md §4 Agent selection guidance."

This is a reference, not a mandate. Coordinator can skip it for single-agent tasks.

### E4: Project-level tool mapping (KNOWLEDGE.md or project_config.yaml)

For projects that USE multi-agent, the project-specific tool mapping lives in KNOWLEDGE.md:

```markdown
### Agent capabilities (project-specific)

| Tool | Strengths for research | Used in |
|------|----------------------|---------|
| Antigravity | Web search, MCP (Google Sheets, ClickHouse), ~1M context, image generation | TFW-42 iter 1-2, AFD-2 iter 1,4,6,7,8 |
| Claude Code | Terminal-native, MCP, shell commands, codebase reasoning | AFD-2 iter 5 |
| Codex CLI | Async background tasks, sandboxed code audit, autonomous | AFD-2 iter 2,3 |
```

This is NOT in `.tfw/` — it's project-specific knowledge that accumulates through usage. The `tfw-knowledge` workflow would capture it naturally from Fact Candidates.

### E5: The "framework suggests" model — why it fails

C8 proposes framework-level suggestions (e.g., "iteration focus contains 'code audit' → suggest Codex").

**Why this fails:**
1. **Keyword matching is brittle** — "code audit" vs "codebase analysis" vs "dependency review" all mean similar things
2. **Tool landscape changes** — Codex CLI may gain web search tomorrow; suggestion logic becomes wrong
3. **TFW is a methodology, not a runtime** — it produces markdown files, not running code
4. **Breaks TFW's philosophy** — TFW trusts coordinators to make decisions, provides tools for traceability

**Verdict:** Framework suggests = over-engineering. Human decides with guidance table = correct.

### E6: Concrete deliverable — what changes in TFW

Summary of all changes needed for agent guidance formalization:

| File | Change | Size |
|------|--------|------|
| conventions.md §4 | Add "Agent selection guidance" subsection with 5-row capability table | ~15 lines |
| conventions.md §4 iterations.yaml schema | Add `agent` and `sources` comments to schema example | ~2 lines |
| plan.md Step 6b | Add one sentence referencing conventions.md agent guidance | ~1 line |
| templates (iterations.yaml example) | Include `agent` and `sources` as commented-out optional fields | ~2 lines |

**Total impact:** ~20 lines across 3 files. Minimal, non-breaking, tool-agnostic.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C9 (hybrid: conventions table + template comment) = winner | None |
| Concrete table designed (5 rows, tool-agnostic) | None |
| Template comment designed (minimal, commented-out fields) | None |
| plan.md change = 1 sentence reference | None |
| "Framework suggests" model rejected (E5) | None |

**Sufficiency:**
- [x] External source used? (Cross-referenced with Gather G1 capability data)
- [x] Briefing gap closed? (Formalization fully designed: where, what, how)
- [x] Configuration Space built from Gather dimensions? (9 configs, C9 hybrid winner)

**Deep mode criteria:**
- [x] Hypothesis tested? (Agent guidance formalized via two-tier approach)
- [x] Counter-evidence sought? (E5: framework suggests model tested and rejected)

**Metacognitive check:** NEW — the concrete guidance table design (5 rows, tool-agnostic, "Example tools" column). This is actionable output, not just analysis. Also discovered that the total TFW change is ~20 lines — significantly smaller than expected.

Stage complete: YES
→ User decision: proceed (autonomous mode)
