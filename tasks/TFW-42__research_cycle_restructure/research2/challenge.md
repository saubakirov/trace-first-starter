# Challenge — "What do we NOT expect?" (Iteration 2)
> Parent: [HL-TFW-42](../../HL-TFW-42__research_cycle_restructure.md)
> Goal: Map agent capabilities for research subtasks and formalize how TFW guides coordinators in agent selection.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1: Guidance | Tool-specific | D2: Location | conventions.md | Naming tools in conventions breaks tool-agnosticism (conventions = framework-level, tools = project-level) |
| D1: Guidance | Tool-specific | D3: Decision | No recommendation | If you name tools, you're already recommending — can't be tool-specific AND hands-off |
| D3: Decision | Framework suggests | D2: Location | Comment in template | Comments can't implement suggestion logic — need code or structured prompt |

**Surviving configurations:**

| Config | D1: Specificity | D2: Location | D3: Decision | Notes |
|--------|----------------|-------------|-------------|-------|
| C1 | Generic archetypes | Template comment | Human, no rec | Too minimal — doesn't answer "for what?" |
| C2 | Generic archetypes | Conventions table | Human, decision table | Good but archetypes too vague |
| C5 | Capability-based | Conventions table | Human, decision table | Strong — capabilities are actionable |
| C6 | Capability-based | plan.md prompt | Human, decision table | Too prescriptive for optional feature |
| C9 | Capability-based | **Both** (conventions + template) | Human, decision table | **Best — two-tier guidance** |

**Unexpected survivors:**
- **C5 (capability-based, conventions-only, decision table):** Survived as a simpler alternative to C9. The difference is whether the template includes a comment. C5 = conventions table only, coordinator must know to check it. C9 = conventions table + template hint.

The hint in the template makes C9 strictly better for discoverability without adding complexity. C9 wins.

## Findings

### C1: Stress-test — will the guidance table become stale?

**Risk:** Tool capabilities evolve fast. "Terminal/CLI agents" for code audit may become wrong when Antigravity adds better code traversal.

**Analysis:**
- The table describes RESEARCH ACTIVITIES → KEY CAPABILITIES, not specific tools
- "File traversal, shell commands" will remain the capabilities needed for code audit regardless of which tools offer them
- Tool-to-capability mapping lives in project-level KNOWLEDGE.md, which updates naturally through `tfw-knowledge`

**Verdict:** The conventions table is stable because it maps activities to capabilities (stable), not to tools (volatile). Risk is low.

### C2: Stress-test — single-tool user experience

**Scenario:** A developer uses only Cursor for everything. They see:
- iterations.yaml: `# agent: tool-name  # optional`
- conventions.md: capability table with 5 research activities

**Experience:**
1. They skip the `agent` field (it's commented out)
2. They may read the conventions table once, realize they only have Cursor, and never look again
3. Zero overhead for their workflow

**Verdict:** Optional fields + reference table = zero cost for single-tool users. The design passes the "don't penalize the common case" test.

### C3: Stress-test — new user onboarding

**Scenario:** A developer new to TFW reads `conventions.md §4` to understand research structure.

**Experience:**
1. They see the iterations.yaml schema with `agent` commented out
2. They see the "Agent selection guidance" subsection
3. They learn: "oh, I can use different tools for different iterations"
4. They have a reference table mapping activities to capabilities

**Verdict:** The guidance serves as EDUCATION for new users without being prescriptive. Discovery path is natural: schema → "what's this agent field?" → guidance table.

### C4: Stress-test — tool-agnosticism verification

**Claim:** The conventions table doesn't name specific tools.

**Verification against Extract E1 table:**

| Column | Content | Tool-agnostic? |
|--------|---------|----------------|
| Research activity | "Web research, competitive analysis" | ✅ Generic activity |
| Key capability | "Web search, large context" | ✅ Capability, not tool |
| Example tools | "IDE agents with web search" | ✅ Category, not brand name |

**Edge case:** What if someone reads "IDE agents with web search" and doesn't know which of their tools has web search?
- This is where project-level KNOWLEDGE.md comes in: specific tool mapping is project knowledge, not framework knowledge
- The init workflow (`tfw-init`) could prompt users to document their available tools — but this is out of scope for TFW-42

**Verdict:** Tool-agnosticism preserved. No tool names in `.tfw/` framework files.

### C5: Counter-evidence — is the two-tier approach (conventions + template + project KNOWLEDGE) over-engineered?

**Simpler alternative:** Just add `agent` as optional field, no guidance at all. Let coordinators figure it out.

**Why this fails:**
- User explicitly asked: «как это лучше формализовать, рекомендовать что-то или человек сам выбирает»
- The guidance table is ~15 lines. Not a maintenance burden.
- Without guidance, the `agent` field is just a string with no context — new users won't know why it exists

**Counter to the counter:** The guidance exists but is MINIMAL. 15 lines in conventions + 2 commented lines in template. This is not over-engineering — it's the minimum viable guidance.

### C6: Final design validation — the complete picture

**What a coordinator sees when planning multi-iteration research:**

1. **plan.md Step 6b** (workflow): "For multi-iteration research, consider whether different iterations would benefit from different tools. See conventions.md §4."
2. **conventions.md §4** (reference): 5-row capability table mapping research activities to key capabilities
3. **iterations.yaml template** (decision point): `# agent: tool-name  # optional` as commented-out field
4. **KNOWLEDGE.md** (project-specific): tool-to-capability mapping for this project's available tools

**Flow:**
```
Coordinator reads plan.md Step 6b
  → "consider different tools" (awareness trigger)
  → checks conventions.md §4 if unsure (reference)
  → writes iterations.yaml with agent field if multi-agent (decision)
  → project KNOWLEDGE.md accumulates tool patterns (learning)
```

This is exactly the TFW pattern: workflow triggers → conventions reference → artifact records → knowledge accumulates.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C9 confirmed as winner after 5 stress tests | None |
| Tool-agnosticism verified column-by-column | None |
| Single-tool user = zero overhead | None |
| New user = natural discovery path | None |
| Staleness risk mitigated by capability-based (not tool-based) table | None |

**Sufficiency:**
- [x] External source used? (Validated against tool capability data from Gather)
- [x] Briefing gap closed? (Formalization fully designed and stress-tested)
- [x] Pairwise incompatibility checked? (3 incompatible pairs, 5 survivors)

**Deep mode criteria:**
- [x] Hypothesis tested? (Complete guidance formalization validated)
- [x] Counter-evidence sought? (C5: over-engineering objection, C1: staleness risk)

**Metacognitive check:** The complete coordinator flow (C6) is NEW — it shows how the pieces fit together across workflow → conventions → template → knowledge. This validates that the design is integrated, not fragmented.

Stage complete: YES
→ User decision: proceed (autonomous mode)
