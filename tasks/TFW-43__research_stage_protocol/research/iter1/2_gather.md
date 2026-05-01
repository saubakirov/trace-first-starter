# Gather — "What do we NOT know?"
> Parent: [HL-TFW-43](../../HL-TFW-43__research_stage_protocol.md)
> Goal: Determine exact Mindset block wording for 4 research stage templates that produces measurably different cognitive modes in AI agents.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D _(if any)_ |
|-----------|-------|-------|-------|--------------------|
| D1: Role-noun per stage | Functional noun (Explorer/Analyst/Critic/Strategist) | Metaphorical noun (Scout/Synthesizer/Adversary/Architect) | Task-verb noun (Decomposer/Cross-referencer/Eliminator) | Match review pattern (Student/Auditor/Judge → ?) |
| D2: Test question format | Self-check interrogative ("Did I...?") | External perspective ("Would someone...?") | Specific checklist ("Check: N dimensions identified?") | Imperative ("Verify that...") |
| D3: h1 guiding question placement | Keep h1 as-is + add Mindset (dual signal) | Move h1 content into Mindset (Mindset = primary, h1 = stage name only) | Merge: h1 stays as title, Mindset references it ("Answer the h1 question by...") | Replace h1 entirely with role-noun title |
| D4: Briefing stage treatment | Full Mindset block (same structure as other 3) | Lighter Mindset (shorter, procedural framing) | No Mindset (Briefing is coordinator input, not investigative) | |

## Findings

### G1: Review template Mindset pattern — structural analysis

Analyzed 3 review templates (map.md, verify.md, judge.md). The proven pattern:

```
# {Stage Name} — "{Guiding question}"
> **Mindset:** {Role-noun}. {One-sentence instruction}. {Constraint/orientation}.
> **Test:** "{Self-check question as full sentence with quotes}"
```

Key observations:
1. **Role-nouns used:** "Experienced newcomer" (map), "Auditor" (verify), "Judge" (judge)
2. **Test format:** Always a quoted question in "Could I..." / "Would I..." / "If I..." form — external perspective, not "Did I..."
3. **Test specificity:** Each test is existential ("Can I explain...", "Would evidence alone prove...", "Would I stake my reputation...") — not checklist-style
4. **h1 pattern:** Stage name + guiding question in quotes (`# Map — "What was done?"`)
5. **The guiding question is NOT in the Mindset block** — it stays in h1. Mindset and h1 are complementary: h1 = what to answer, Mindset = how to think

This contradicts H4's assumption that "guiding questions should move to Mindset." The review pattern shows they work as dual signals — h1 orients the task, Mindset orients the cognition.

### G2: LLM persona/role assignment research

External research findings on persona prompting:

1. **Persona prompting is well-established:** "You are a {role}" framing measurably shifts LLM behavior. The effect is strongest when the role-noun activates specific domain knowledge and reasoning patterns associated with that role.

2. **Role-noun > prose instruction:** A single well-chosen role-noun ("Auditor") triggers different reasoning than equivalent prose ("carefully check each claim against evidence"). This aligns with TFW D28 (naming > explanation) and process.md F3 ("Claude dreaming = 1 word replacing paragraphs").

3. **Functional nouns > metaphorical:** Nouns with clear professional associations (Auditor, Editor, Critic) produce more consistent behavior than vague metaphors (Guardian, Sentinel). The LLM has more training data associating "Auditor" with specific behaviors than "Guardian."

### G3: Self-check vs imperative format — external evidence

Key finding from research on LLM self-verification:

1. **Imperative instructions are more effective DURING generation** — they set constraints before the agent works
2. **Self-check questions ("Did I...?") are more effective POST-generation** — they trigger review of completed work
3. **Structured checklists outperform vague self-check** — "Did I identify ≥3 dimensions?" > "Did I do this right?"
4. **Critical finding:** For reasoning tasks, vague self-check can DEGRADE performance — model "corrects" right answers into wrong ones. Specific, objective self-check works better.
5. **External feedback improves self-check** — when the model has a structural reference (checklist, previous stage output) to verify against, self-check is reliable

**Implication for TFW Test format:**
- Review templates use existential Test questions ("Would I stake my reputation...") — these work because the reviewer has EVIDENCE (verify.md findings) to check against
- Research templates should use Tests that reference the STRUCTURAL output of the stage — e.g., "Can I point to the dimensions table and name every degree of freedom?" (references the template's own structure as verification anchor)

### G4: TFW internal evidence on cognitive framing

From TFW knowledge base:
- **F3 (process.md):** "Naming creates behavior in AI agents more effectively than explanation" — VERIFIED across multiple sources
- **F4 (process.md):** "AI agents follow numbered steps + gates perfectly but lose focus in prose" — VERIFIED
- **F18 (philosophy.md):** "Different templates serve different cognitive modes — this is a DESIGN PRINCIPLE" — confirmed
- **F20 (philosophy.md):** "TFW has investigative vs procedural workflows. Investigative = forced cognitive transitions via stages" — VERIFIED
- **F24 (philosophy.md):** "Instructions → compliance, heuristics → competence. Cross-stage structural dependencies enforce better" — confirmed
- **D28 (KNOWLEDGE.md):** Naming > Explanation — the Claude "dreaming" case: 1 word triggered complex behavior where paragraphs failed
- **D41 (KNOWLEDGE.md):** Review 4-stage flow with per-stage identity — proven effective in production

### G5: Mapping research stages to cognitive modes

Each research stage has a distinct cognitive PURPOSE already defined in conventions and templates:

| Stage | Current h1 | Cognitive Purpose | Required Mental Mode |
|-------|-----------|------------------|---------------------|
| Briefing | (none — h1 is just "Briefing") | Plan the investigation. Frame hypotheses. Set scope. | Strategic/planning — "what do we need to know?" |
| Gather | "What do we NOT know?" | Decompose into dimensions. Collect raw data from external + internal sources | Exploratory/divergent — widen the field, resist premature closure |
| Extract | "What do we NOT see?" | Cross-reference dimensions. Build configuration space. Find hidden combinations | Analytical/synthetic — connect what was found, make invisible visible |
| Challenge | "What do we NOT expect?" | Stress-test configurations. Find incompatibilities. Surface unexpected survivors | Adversarial/critical — attack your own work, find what breaks |

These modes are genuinely distinct — each requires a different cognitive stance. This supports H2: role-nouns should encode these differences.

### G6: Candidate role-nouns per stage

| Stage | Candidate A | Candidate B | Candidate C | Rationale for preferred |
|-------|------------|------------|------------|------------------------|
| Briefing | Strategist | Planner | Navigator | Strategist = planning + priority setting. Planner = too generic. Navigator = metaphorical |
| Gather | Explorer | Scout | Field researcher | Explorer = wide search, resist premature closure. Scout = too passive. Field researcher = too long |
| Extract | Analyst | Synthesizer | Pattern-finder | Analyst = cross-reference and structure. Synthesizer = too creative. Pattern-finder = descriptor, not noun |
| Challenge | Critic | Adversary | Stress-tester | Critic = evaluate with standards. Adversary = too aggressive. Stress-tester = descriptor |

Review uses: Experienced newcomer → Auditor → Judge. Note the progression: comprehension → verification → judgment. Research should follow a parallel progression: planning → exploration → analysis → critique.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Review template structural formula: Role-noun + instruction + Test (external perspective) | Need to validate: does h1 + Mindset dual signal actually work in research context? |
| External evidence: persona prompting works, functional nouns > metaphors | Need to cross-reference: specific Test question wording per stage |
| Self-check research: structured self-check with stage-output reference > vague self-check | Need to validate Briefing treatment — is Strategist the right framing? |
| 4 cognitive modes mapped: Strategic → Exploratory → Analytical → Adversarial | Need consistency check across all combinations |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?

Stage complete: YES
→ User decision: ___
