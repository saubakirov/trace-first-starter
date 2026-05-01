# Challenge — "What do we NOT expect?"
> Parent: [HL-TFW-43](../../HL-TFW-43__research_stage_protocol.md)
> Goal: Determine exact Mindset block wording for 4 research stage templates that produces measurably different cognitive modes in AI agents.

## Consistency Check

Take each pair of dimensions from Gather and ask: "Can Alternative X coexist with Alternative Y?"

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|--------------------|
| D1: Role-noun | Critic | D2: Test format | Imperative ("Verify that...") | Critic = evaluative identity; imperative = directive. Identity-based role contradicts command-style verification — critic judges, doesn't follow orders |
| D1: Role-noun | Strategist | D4: Briefing | No Mindset (C3) | Can't assign a role-noun to a stage that has no Mindset block — self-contradictory |
| D2: Test format | Structured checklist ("Did I ≥3...?") | D3: h1 placement | Move h1 into Mindset (T3) | If h1 content moves into Mindset AND Test is a checklist, the Mindset blockquote becomes 3+ lines of mixed concern: role + instruction + content from h1 + checklist Test. Overloaded |
| D3: h1 placement | Replace h1 with role-noun (Alt D) | D2: Test format | Existential external | If h1 loses the guiding question, the existential Test loses its anchor — Test questions reference stage purpose, which was carried by h1 |

**Surviving configurations** (from Extract's Configuration Space, after removing rows containing incompatible pairs):

| Config | Role-noun (D1) | Test format (D2) | h1 treatment (D3) | Briefing (D4) | Notes |
|--------|---------------|------------------|-------------------|---------------|-------|
| C1+T1 | Functional (Strategist/Explorer/Analyst/Critic) | Existential external | Keep as-is (dual signal) | Full Mindset | **Primary candidate** — exact review mirror |
| C1+T2 | Functional | Structured checklist | Keep as-is | Full Mindset | Valid but Test redundant with Checkpoint |
| C2+T1 | Functional (lighter Briefing) | Existential external | Keep as-is | Lighter Mindset | Valid — Briefing differentiated |

**Unexpected survivors** (configurations that survived but were not initially favored — worth highlighting):
- **C2+T1**: Lighter Briefing Mindset survived all consistency checks. It's not incompatible — just less consistent. Worth considering if full Briefing Mindset proves too heavy in practice. Trade-off: consistency vs. acknowledging Briefing's different nature (more procedural input than investigative output).

## Findings

### C1: Stress-test — do role-nouns overlap in cognitive connotation?

**Explorer vs Analyst:** Clear distinction. Explorer = divergent (widen the search). Analyst = convergent (structure what was found). Opposite cognitive modes — no overlap.

**Analyst vs Critic:** Potential overlap zone. Both involve judgment. But:
- Analyst judges STRUCTURE (are dimensions cross-referenced? are combinations complete?)
- Critic judges VALIDITY (can combinations coexist? does evidence support survivors?)
- Analyst builds. Critic breaks. Different verbs, different cognitive frames.

**Strategist vs Explorer:** Potential confusion. Both "plan." But:
- Strategist plans WHAT to investigate (scope, hypotheses, questions)
- Explorer EXECUTES the investigation plan (finds sources, decomposes dimensions)
- Strategist = before action. Explorer = during action. Temporal distinction is clean.

**Verdict:** No overlaps that would cause agent confusion. The 4 nouns occupy distinct positions on two axes:
- **Convergent ↔ Divergent:** Strategist (convergent/planning) → Explorer (divergent/searching) → Analyst (convergent/structuring) → Critic (divergent/attacking)
- **Build ↔ Break:** Strategist (build plan) → Explorer (build raw data) → Analyst (build structure) → Critic (break structure)

### C2: Stress-test — does the escalation break if stages run out of order?

The workflow says "Order flexible" for Gather/Extract/Challenge. But the Test escalation (coverage → insight → robustness) assumes sequential build-up. What happens if someone runs Challenge before Extract?

**Analysis:** The dimensional analysis thread already enforces order structurally:
- Extract REFERENCES Gather's Dimensions table (column headers = dimension names from Gather)
- Challenge REFERENCES Extract's Configuration Space (surviving configs = subset of Extract's table)

The Test questions reference stage-specific outputs. If Challenge runs before Extract, the Test ("Would my surviving configurations hold...?") has no configurations to reference — it naturally fails.

**Verdict:** Test escalation is ALIGNED with the structural dependency already enforced by dimensional analysis. Not a new constraint — it reflects an existing one. The "Order flexible" note in base.md applies to stages generally, but dimensional analysis stages have a natural order that both structure AND Test questions enforce.

### C3: Stress-test — is Test truly non-redundant with Checkpoint?

**Checkpoint (current, each template):**
```
**Sufficiency:**
- [ ] External source used?
- [ ] Briefing gap closed?
- [ ] Dimensions identified?
```

**Proposed Test (Gather):** "Can I point to the dimensions table and name every degree of freedom without looking at my sources?"

These check DIFFERENT things:
- Checkpoint: "Did I do the mechanics?" (file read, source cited, table filled)
- Test: "Did I UNDERSTAND what I found?" (can I explain it from memory = internalization)

Review validates this: Verify Checkpoint = "Opened ≥ ⌈N × ratio⌉ files?", Verify Test = "If I removed the RF, would the evidence alone prove the work was done?" — mechanics vs meaning.

**Verdict:** Not redundant. Test is an identity/comprehension check, Checkpoint is a task/completion check. Keep both.

### C4: Stress-test — Briefing h1 guiding question options

Extract proposed `"What should we investigate?"` for Briefing h1. Let me stress-test:

| Option | Fits "NOT" pattern? | Natural? | Distinctive? |
|--------|---------------------|----------|-------------|
| "What should we investigate?" | No | Yes | Clear planning framing |
| "What do we NOT ask?" | Yes | Awkward | Forced |
| "Why are we here?" | No | Too philosophical | Vague |
| (no question) | N/A | Current state | Inconsistent with other 3 |

The review templates don't follow a single pattern either ("What was done?" / "Are the claims true?" / "Is the quality sufficient?"). The "NOT" pattern in research is elegant but shouldn't be force-fitted.

**Verdict:** `"What should we investigate?"` — clear, natural, planning-oriented. Doesn't break the rhythm of the other three questions.

### C5: Stress-test — exact Test question wording per stage

Drafting and stress-testing each:

| Stage | Proposed Test | Stress test | Verdict |
|-------|--------------|-------------|---------|
| Briefing | "Can I explain WHY we're investigating this and what would change our approach?" | Does this test planning quality? Yes — if you can't explain WHY, your plan is mechanical. "What would change our approach" tests adaptability awareness | ✅ Keep |
| Gather | "Can I point to the dimensions table and name every degree of freedom without looking at my sources?" | Does this test comprehension? Yes — if you can name dimensions from memory, you internalized the problem space. "Without looking at sources" forces understanding, not regurgitation | ✅ Keep but simplify |
| Extract | "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?" | Does this test analytical insight? Yes — if Extract only confirms what was already planned, no new insight was generated. This is the Extract stage's unique value proposition | ✅ Keep |
| Challenge | "Would my surviving configurations hold if a different researcher attacked them?" | Does this test adversarial robustness? Yes — external perspective forces the critic to consider blind spots. "Different researcher" = role distance from own work | ✅ Keep |

**Simplified Gather Test:** "Can I name every dimension and its alternatives without checking my sources?" — shorter, same meaning.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1+T1 confirmed: no incompatible pairs in the selected combination | — |
| Role-nouns verified non-overlapping on 2 axes (convergent/divergent + build/break) | — |
| Test ≠ Checkpoint: identity/comprehension vs task/completion | — |
| Briefing h1: "What should we investigate?" | — |
| All 4 Test questions drafted and stress-tested | — |
| Escalation aligned with structural dependency — not a new constraint | — |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: YES
→ User decision: ___
