# Extract — Iteration 2
> Parent: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> Goal: Embed Zwicky heuristics into existing research stages naturally.

## Findings

### E1: Proposed Template Modifications — Before/After

#### gather.md — BEFORE (current)

```markdown
# Gather — "What do we NOT know?"

## Findings

### {G1: source/topic title}
{content}
```

#### gather.md — AFTER (proposed)

```markdown
# Gather — "What do we NOT know?"

## Dimensions
> For each research question, identify independent decision dimensions.
> A dimension = a factor where changing it changes the solution,
> regardless of what other factors do.
> List ≥3 alternatives per dimension. Do NOT mark any as "recommended."

### {D1: dimension name}
| Alt | Description | Source |
|-----|-------------|--------|
| A   | {option}    | {where found} |
| B   | {option}    | {where found} |
| C   | {option}    | {where found} |

## Findings
### {G1: source/topic title}
{content — evidence, data, external research}
```

**What changed:**
- Added `## Dimensions` section BEFORE Findings
- Explicit instruction: "independent decision dimensions" + "≥3 alternatives" + "Do NOT mark recommended"
- Table format forces structured enumeration (no prose-hiding)
- `Source` column anchors each alternative to evidence (prevents invented options)

**Why it works:** The researcher's natural impulse is to report findings. By putting Dimensions FIRST, the template forces the researcher to decompose the problem BEFORE collecting evidence. The evidence then populates the alternatives instead of the other way around.

---

#### extract.md — BEFORE (current)

```markdown
# Extract — "What do we NOT see?"

## Findings

### {E1: analysis title}
{content — patterns, comparisons, internal file analysis}
```

#### extract.md — AFTER (proposed)

```markdown
# Extract — "What do we NOT see?"

## Configuration Space
> Using the dimensions from Gather, build the full cross-reference.
> Each row = one viable configuration (one alternative per dimension).
> Do NOT evaluate yet — list all combinations that are not obviously contradictory.

| Config | D1 | D2 | D3 | ... | Notes |
|--------|----|----|----|----|-------|
| C1     | A  | A  | B  |    | {why this combination} |
| C2     | A  | B  | A  |    | {why this combination} |
| ...    |    |    |    |    | |

> If total combinations > 30: list only configurations where at least one dimension
> differs from the "default" (first-listed) alternative.

## Findings
### {E1: analysis title}
{content — patterns, comparisons, deeper analysis}
```

**What changed:**
- Added `## Configuration Space` section BEFORE Findings
- References Gather's Dimensions explicitly ("Using the dimensions from Gather")
- Table format with one column per dimension
- "Do NOT evaluate yet" prevents premature recommendation
- Overflow rule (>30): forces diversity by requiring at least one non-default alternative

**Why it works:** The researcher can't build the Configuration Space without having done the Gather Dimensions step. The table makes "all Alt 1" visually obvious as a degenerate case. The "do NOT evaluate" instruction separates construction from judgment.

---

#### challenge.md — BEFORE (current)

```markdown
# Challenge — "What do we NOT expect?"

## Findings

### {C1: edge case / stress test title}
{content — what could go wrong, alternatives, counter-evidence}
```

#### challenge.md — AFTER (proposed)

```markdown
# Challenge — "What do we NOT expect?"

## Consistency Check
> Take each pair of dimensions from Extract's Configuration Space.
> For each pair, ask: "Can D_i-Alt_X coexist with D_j-Alt_Y?"
> Mark incompatible pairs. Remove configurations containing them.

| D_i | D_j | Incompatible pair | Why |
|-----|-----|-------------------|-----|
| D1  | D3  | D1-A × D3-C      | {reason} |

**Surviving configurations:** {list from Configuration Space after elimination}
**Unexpected survivors:** {configurations you did NOT expect to survive}

## Findings
### {C1: edge case / stress test title}
{content — stress tests, counter-evidence, edge cases}
```

**What changed:**
- Added `## Consistency Check` section BEFORE Findings
- References Extract's Configuration Space explicitly
- Pairwise table format forces systematic elimination (not hand-waving)
- "Unexpected survivors" — replaces iter 1's "non-obvious configuration" with a verifiable check
- Regular Findings section preserved for non-dimensional analysis

**Why it works:** Challenge's identity is "stress test" — CCA is exactly that, applied to the configuration space. The researcher eliminates combinations by finding inconsistencies, which IS the challenge mindset. No separate exercise needed.

---

### E2: Workflow Changes — tfw-research.md (base.md)

#### Current Step 5 text:
```
## Step 5: Run Stages (Gather → Extract → Challenge)
Cover all three. Order flexible.
```

#### Proposed addition after "Cover all three":
```
**Dimensional analysis** threads through all three stages:
- **Gather** decomposes the problem into independent dimensions with alternatives
- **Extract** constructs the configuration space from Gather's dimensions
- **Challenge** eliminates inconsistent combinations via pairwise consistency check
If the research question has <3 independent dimensions, use a comparison matrix
(pros/cons table) instead of the full dimensional pipeline.
```

**What changed:** 3 lines that describe the flow WITHOUT naming Zwicky or morphological analysis. The terminology is native to TFW: "dimensions," "configuration space," "consistency check." These map to GMA's "parameters," "morphological field," "CCA" but use language natural to the stage questions.

---

### E3: Glossary Additions

New terms for `.tfw/glossary.md`:

| Term | Definition |
|------|-----------|
| **Dimension** | An independent decision factor in research. Changing it changes the solution regardless of other factors. Identified during Gather. |
| **Alternative** | One possible value for a dimension. Minimum 3 per dimension. Not marked as "recommended" until after Consistency Check. |
| **Configuration Space** | The set of all viable combinations of one alternative per dimension. Built during Extract from Gather's dimensions. |
| **Consistency Check** | Pairwise elimination of incompatible dimension-alternative pairs. Performed during Challenge. Reduces the configuration space to surviving configurations. |
| **Surviving Configuration** | A combination that passed all pairwise consistency checks. Input for RES Decisions. |

---

### E4: Testing Against HD-19 — Would This Have Worked?

**HD-19 research question:** "How should we architect the Settings system?"

**If the proposed templates had been active:**

**Gather** would have produced:
```
## Dimensions

### D1: Working schedule storage
| Alt | Description | Source |
|-----|-------------|--------|
| A   | Tenant-level flag (working_schedule + working_days[]) | Architecture analysis |
| B   | Update sla_configs directly (23:59 hack) | Current codebase |
| C   | Separate tenant_schedule table | Normalized DB design |

### D2: Permission invalidation
| Alt | Description | Source |
|-----|-------------|--------|
| A   | SSE permissions:changed → refetch /auth/me | Existing SSE infrastructure |
| B   | Short TTL (30s) on cache | Simplicity |
| C   | Polling /auth/me/permissions every 60s | Fallback pattern |
| D   | WebSocket per-user | Real-time pattern |

### D3: Frontend permissions store
...
```

**Extract** would have produced Configuration Space:
```
| Config | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 |
|--------|----|----|----|----|----|----|----|----|
| C1     | A  | A  | A  | A  | A  | A  | A  | A  | ← the "all Alt 1" config (would be listed but not special)
| C2     | A  | A  | A  | B  | A  | A  | A  | C  | ← top tabs + force password
| C3     | B  | B  | A  | A  | A  | A  | A  | A  | ← sla_configs direct + short TTL
| ...    |    |    |    |    |    |    |    |    |
```

The "all Alt 1" config would be ONE ROW among many, not the default. The researcher would have to BUILD alternative configs, not just list them.

**Challenge** would have found:
```
## Consistency Check

| D_i | D_j | Incompatible pair | Why |
|-----|-----|-------------------|-----|
| D2  | D3  | D2-C (polling) × D3-B (separate store) | Polling requires centralized state; separate store adds complexity without benefit |
| D2  | D7  | D2-D (WebSocket) × D7-A (single tenant) | WebSocket per-user is overkill for single-tenant MVP |
| D4  | D5  | D4-B (top tabs) × D5-A (visual matrix) | Matrix needs vertical space; top tabs waste it |
```

**Result:** The researcher would have eliminated specific combinations and arrived at surviving configs — not "all Alt 1 recommended."

---

### E5: Comparing Iter 1 (DR4 instruction) vs Iter 2 (embedded heuristics)

| Aspect | Iter 1: DR4 "Mandatory Zwicky Box" | Iter 2: Embedded Dimensions |
|--------|-------------------------------------|----------------------------|
| Template change | Add "must do Zwicky Box in Extract" | Add structural sections to all 3 stage templates |
| Workflow change | Add enforcement rules (5 items) | Add 3-line description in Step 5 |
| Researcher experience | "Now I have to do this extra thing" | "The template sections guide my analysis" |
| Simulation risk | High — researcher fills box to comply | Low — each stage builds on previous stage's output |
| Cross-stage coherence | None — box is self-contained in Extract | High — Gather→Extract→Challenge chain |
| When to skip | "If <3 parameters" (threshold rule) | Same — comparison matrix for <3 dimensions |
| Terminology | "Zwicky Box," "CCA," "morphological" | "Dimensions," "Configuration Space," "Consistency Check" |
| Learning curve | Must know GMA methodology | Natural — template questions guide thinking |

**Verdict:** Iter 2 approach is strictly better. It achieves the same analytical rigor but:
1. Distributes the work naturally across stages (no "blob in Extract")
2. Creates cross-stage dependencies (Extract can't work without Gather dimensions)
3. Uses native terminology (no "Zwicky" in templates)
4. Reduces simulation risk (can't fill Config Space without Gather dimensions)

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Concrete before/after for all 3 templates | Need Challenge stress-test |
| Workflow modification (3 lines) | Need to verify backward compatibility |
| HD-19 retrospective: would have produced different result | Need to check edge cases |
| Glossary terms: 5 new entries | — |

**Sufficiency:**
- [x] External source used? (GMA canonical mapping from Gather)
- [x] Briefing gap closed? (Concrete wording designed, tested against HD-19)

Stage complete: YES
→ Proceeding to Challenge.
