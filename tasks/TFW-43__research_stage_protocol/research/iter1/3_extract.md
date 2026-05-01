# Extract — "What do we NOT see?"
> Parent: [HL-TFW-43](../../HL-TFW-43__research_stage_protocol.md)
> Goal: Determine exact Mindset block wording for 4 research stage templates that produces measurably different cognitive modes in AI agents.

## Configuration Space

Cross-referencing Gather's 4 dimensions. Since D1 (role-noun) and D4 (briefing treatment) interact most directly, and D2 (test format) × D3 (h1 placement) are largely independent of stage identity, I structure as: first resolve D1×D4 (who is the agent at each stage?), then D2×D3 (how does it self-verify?).

### D1 × D4: Role-noun per stage, including Briefing treatment

| Config | Briefing | Gather | Extract | Challenge | Pattern |
|--------|----------|--------|---------|-----------|---------|
| C1 | Strategist (full Mindset) | Explorer | Analyst | Critic | Functional nouns, all 4 stages equal |
| C2 | Planner (lighter Mindset) | Explorer | Analyst | Critic | Functional nouns, Briefing lighter |
| C3 | No Mindset | Explorer | Analyst | Critic | Skip Briefing — it's procedural input |
| C4 | Strategist (full Mindset) | Scout | Synthesizer | Adversary | Metaphorical nouns |
| C5 | Strategist (full Mindset) | Explorer | Analyst | Stress-tester | Mixed: functional + descriptor |

### D2 × D3: Test format × h1 placement

| Config | Test format | h1 treatment | Pattern |
|--------|-------------|-------------|---------|
| T1 | Existential external ("Can I point to...?") | Keep as-is (dual signal) | Matches review exactly |
| T2 | Structured self-check ("Did I identify ≥3...?") | Keep as-is (dual signal) | Checklist-style, references template structure |
| T3 | Existential external | Move h1 content into Mindset | Mindset becomes primary cognitive anchor |
| T4 | Imperative ("Verify that...") | Keep as-is | Directive, not reflective |
| T5 | Existential external | Merge: h1 references Mindset | Circular dependency |

## Findings

### E1: Review template cross-reference — structural alignment analysis

The review templates established a clear pattern. Let me map it to research:

**Review formula (proven):**
```
# {Name} — "{Question}"
> **Mindset:** {Role}. {Instruction}. {Constraint}.
> **Test:** "{Existential question with external perspective}"
```

**Review instances:**
| Stage | h1 question | Role | Test perspective |
|-------|------------|------|-----------------|
| Map | "What was done?" | Experienced newcomer | "Can I explain..." (comprehension) |
| Verify | "Are the claims true?" | Auditor | "If I removed the RF..." (evidence independence) |
| Judge | "Is the quality sufficient?" | Judge | "Would I stake my reputation..." (accountability) |

**Pattern I notice:** The Test question escalates in stakes: comprehension → evidence → reputation. Each level BUILDS on the previous — you can't judge quality without verified evidence, can't verify without understanding.

**Research parallel:**
| Stage | h1 question (current) | Proposed role | Test escalation |
|-------|----------------------|--------------|-----------------|
| Briefing | (none) | Strategist | "Can I explain WHY we're investigating this?" (purpose) |
| Gather | "What do we NOT know?" | Explorer | "Can I point to dimensions AND external sources?" (coverage) |
| Extract | "What do we NOT see?" | Analyst | "Does my configuration space reveal combinations nobody proposed?" (insight) |
| Challenge | "What do we NOT expect?" | Critic | "Would my surviving configurations hold under adversarial review?" (robustness) |

The escalation: purpose → coverage → insight → robustness. Each builds on the previous, just like review.

### E2: Why C1+T1 is the strongest combination

**C1 (Strategist/Explorer/Analyst/Critic) + T1 (existential external + dual h1):**

Advantages:
1. **Exact structural match to review** — proven pattern, no invention risk
2. **Functional nouns with clear professional associations** — LLM training data contains rich behavioral patterns for Explorer, Analyst, Critic
3. **Strategist for Briefing = full parity** — all 4 stages have Mindset blocks, consistent treatment
4. **h1 dual signal preserved** — the guiding questions ("What do we NOT know?") are already effective per HL §2. Adding Mindset alongside doesn't remove them, it adds cognitive framing ON TOP
5. **Existential Test with stage-output reference** — the Test question points to the template's own structural output (dimensions table, configuration space, surviving configs) as verification anchor

Why NOT C3 (skip Briefing Mindset)?
- Briefing IS investigative when standalone (user confirmed: "sometimes I start something by myself")
- Even in pipeline mode, Briefing requires a cognitive shift: stop being a coordinator/executor, become a research planner
- Consistency: 4 stages, 4 Mindsets. Partial application = confusion about when Mindset is needed

Why NOT C4/C5 (metaphorical/mixed nouns)?
- "Scout" = passive observation. "Explorer" = active investigation with agency
- "Synthesizer" = creative generation. "Analyst" = structured decomposition (closer to what Extract actually does)
- "Adversary" = hostile. "Critic" = evaluative with standards (what Challenge actually does)
- "Stress-tester" = descriptor, not identity noun

### E3: Why T1 beats T2 (existential > checklist in Test)

**T1 (existential) vs T2 (structured checklist):**

The Checkpoint section in each template ALREADY contains the structured checklist:
```
**Sufficiency:**
- [ ] External source used?
- [ ] Briefing gap closed?
- [ ] Dimensions identified?
```

If the Test question ALSO contains a checklist ("Did I identify ≥3 dimensions?"), it becomes redundant with Checkpoint. Two places for the same verification = dilution.

The review pattern separates them cleanly:
- **Test** (in Mindset blockquote) = cognitive-level question. "Am I THINKING like a {role}?"
- **Checkpoint** (at stage end) = task-level checklist. "Did I DO the required work?"

Test = identity check. Checkpoint = output check. Different layers, different formats.

### E4: Briefing h1 gap — needs a guiding question

Current state:
- Gather: `# Gather — "What do we NOT know?"`
- Extract: `# Extract — "What do we NOT see?"`
- Challenge: `# Challenge — "What do we NOT expect?"`
- Briefing: `# Briefing` ← **no guiding question**

The three investigative stages follow a "What do we NOT {verb}?" pattern. Briefing breaks it. If Briefing gets a Mindset block, should it also get a guiding question?

Options:
- `# Briefing — "What do we need to know?"` — frames the planning task
- `# Briefing — "What do we NOT ask?"` — fits the "NOT" pattern but is awkward
- `# Briefing` — leave as-is, Briefing is different by nature

I notice the review templates don't force a single pattern either: "What was done?" / "Are the claims true?" / "Is the quality sufficient?" — three different question structures. The "What do we NOT {x}?" pattern in research is a coincidence of good design, not a mandatory format.

**Recommendation:** Add `# Briefing — "What should we investigate?"` — clear, planning-oriented, doesn't force-fit the "NOT" pattern.

### E5: Instruction sentence per Mindset — what goes in it?

Review template instructions are 1-2 sentences with a specific BEHAVIORAL directive:
- Map: "You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension."
- Verify: "The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality."
- Judge: "You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding."

Pattern: {situational framing}. {action directive}. {constraint/quality standard}.

Research equivalent:
- **Briefing:** "You're planning an investigation, not doing it. Frame what matters. Resist solving."
- **Gather:** "You're mapping unknown territory. Widen before you narrow. Every assumption is a question."
- **Extract:** "You have the raw findings. Now build structure. Make combinations visible that nobody proposed."
- **Challenge:** "You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason."

Each instruction follows the review pattern: {what you have/where you are}. {what to do}. {how to do it / what not to do}.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1+T1 is the strongest combination: functional nouns, existential Test, dual h1 signal | Need to stress-test: do any role-nouns overlap? Does "Strategist" feel right for Briefing? |
| Escalation pattern: purpose → coverage → insight → robustness | Need to verify: does escalation break if a stage is done out of order? |
| Template structure: h1=task orientation, Mindset=cognitive orientation, Checkpoint=output verification | Need to challenge: is Test redundant with Checkpoint? |
| Briefing needs h1 guiding question: "What should we investigate?" | Need to stress-test wording |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: ___
