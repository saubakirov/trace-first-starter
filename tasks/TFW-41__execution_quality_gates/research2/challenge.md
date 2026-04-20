# Challenge — Iteration 2
> Parent: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> Goal: Embed Zwicky heuristics into existing research stages naturally.

## Findings

### C1: Does Distributing Zwicky Across Stages Dilute Its Power?

**Risk:** GMA's power comes from seeing the FULL matrix at once. If Gather lists dimensions, Extract builds configs, and Challenge eliminates — does the researcher ever see the full picture?

**Test:** In the HD-19 retrospective (Extract E4), the Config Space table in Extract IS the full matrix. The researcher sees all dimensions as columns and all configs as rows. CCA in Challenge references this same table. The matrix is never fragmented — it's built incrementally but viewed holistically in Extract.

**Verdict:** No dilution. The matrix lives in Extract as `## Configuration Space`. Challenge references it. The distribution is in CONSTRUCTION (across stages), not in VISIBILITY (always in one table).

---

### C2: What If The Researcher Skips Gather Dimensions?

**Risk:** The Gather template has `## Dimensions` as an optional-looking section. The researcher fills `## Findings` and skips Dimensions because they don't see it as mandatory.

**Mitigation options:**

| Option | Effect | Risk |
|--------|--------|------|
| Make Dimensions section mandatory (template instruction) | Researcher fills it mechanically | Same simulation risk as iter 1 |
| Extract template says "Using dimensions from Gather" | Extract fails without Gather input → natural enforcement | Researcher invents dimensions in Extract anyway |
| Checkpoint gate: "Dimensions identified?" | Reviewer catches it | Adds process overhead |

**Best option:** The Extract template's `## Configuration Space` instruction says **"Using the dimensions from Gather"** — this creates a structural dependency. If Gather has no dimensions, the researcher can't fill the Config Space. They'll go back to Gather naturally.

**Additional safeguard:** The Gather template checkpoint should include: `- [ ] Dimensions identified? (≥3 alternatives per dimension, no recommendation)`

---

### C3: Edge Case — Focused Mode (Not Deep Mode)

**Risk:** Focused mode has fewer OODA loops and less rigor. Will the dimensional pipeline work there?

**Test:** Focused mode file says:
- "OODA loops per stage: up to N (default: 2)"
- "Require counter-evidence: no"

The dimensional pipeline doesn't need counter-evidence — it needs structured decomposition. CCA in Challenge IS counter-evidence (finding what doesn't work). Focused mode with 2 loops per stage can still do: Gather(decompose) → Extract(build matrix) → Challenge(eliminate).

**Verdict:** Works in focused mode. The dimensional sections are lightweight — the overhead is structural (add sections), not temporal (more loops).

---

### C4: Does Embedding Change Stage Character?

The stages have clear identities from their heading questions:
- Gather = "What do we NOT know?" → COLLECT
- Extract = "What do we NOT see?" → ANALYZE
- Challenge = "What do we NOT expect?" → STRESS-TEST

**With dimensional sections:**
- Gather = Collect data + DECOMPOSE into dimensions → "What DON'T we know about the decision space?"
- Extract = Analyze patterns + BUILD configuration space → "What combinations DON'T we see?"
- Challenge = Stress-test + ELIMINATE inconsistent pairs → "What incompatibilities DON'T we expect?"

**Verdict:** Stage character is PRESERVED. The dimensional sections are specializations of the existing questions, not foreign additions. Decomposition IS a form of "not knowing" — you don't know the full space until you decompose it. Configuration IS a form of "not seeing" — you don't see all options until you cross-reference. CCA IS a form of "not expecting" — you don't expect which pairs are inconsistent.

---

### C5: When The Research Has <3 Dimensions — Does the Pipeline Degrade Gracefully?

**Scenario:** Research question: "Should we use Redis or in-memory cache?" — 1 dimension, 2-3 values.

**With proposed templates:**
- Gather `## Dimensions`: 1 table with 3 alternatives. Fine — small but structured.
- Extract `## Configuration Space`: 3 rows (one per alternative). The "full matrix" is just a list. Trivial but not wrong.
- Challenge `## Consistency Check`: No pairwise checks possible (only 1 dimension). CCA section says "N/A — single dimension, no cross-consistency needed."

**Fix already in proposal:** "If <3 independent dimensions, use a comparison matrix (pros/cons) instead of full dimensional pipeline." This means the Dimensions section in Gather still works (it's just a list of alternatives), but Extract uses a pros/cons table instead of Configuration Space, and Challenge does a regular stress-test instead of CCA.

**Template wording adjustment:** Add to each section:
- Gather `## Dimensions`: "If the research involves a single decision (≤2 dimensions), list alternatives here. The Configuration Space and Consistency Check sections are optional."
- This one instruction cascades: no Config Space → no CCA → regular analysis flow.

---

### C6: Backward Compatibility — Existing Research Artifacts

**Risk:** Changing templates means new research will have Dimensions/Config Space/Consistency Check sections, but old research won't. Is this a problem?

**No.** Templates are used at creation time. Existing `research/` folders keep their structure. Only new research iterations use new templates. The `## Findings` section is preserved in all templates — old-style research (findings only) is a valid subset of new-style (dimensions + findings).

---

### C7: The Terminology Decision — Why NOT "Zwicky"

**Question:** Why not use the original GMA terminology (parameter, value, morphological field, CCA)?

**Reasons:**
1. **Cognitive load.** "Dimension" and "alternative" are everyday words. "Parameter" and "morphological field" require domain knowledge.
2. **Neutrality.** Naming a methodology creates allegiance. "I'm doing Zwicky" → focus on following the method. "I'm finding dimensions" → focus on the problem.
3. **Extensibility.** "Dimension" maps to GMA's "parameter" but also to decision theory, option pricing, scenario planning. Not locked to one framework.
4. **The user's observation.** "Я вижу больше симуляцию" — the simulation happened because the researcher was trying to "do Zwicky" (methodology compliance) instead of analyzing the problem (genuine discovery). Native terms remove this trap.

**Counter-argument:** Naming the source (Zwicky) in the glossary/conventions helps future researchers understand WHY the pipeline is structured this way.

**Resolution:** Use native terms in templates. Reference Zwicky in conventions/glossary as origin: "Dimensional analysis in TFW research is inspired by Zwicky's General Morphological Analysis (1969). See glossary for term mapping."

## Checkpoint

| Found | Remaining |
|-------|-----------|
| No dilution — matrix lives in Extract, visible holistically | — |
| Cross-stage dependency prevents skipping (Extract needs Gather) | — |
| Works in focused mode (structural, not temporal overhead) | — |
| Stage character preserved — dimensions ARE the stage questions | — |
| <3 dimensions: graceful degradation via single instruction | — |
| Backward compatible — templates used at creation time only | — |
| Terminology: native terms in templates, Zwicky in glossary as origin | — |

**Sufficiency:**
- [x] External source used? (N/A for Challenge — internal stress-test)
- [x] Briefing gap closed? All 3 guiding questions answered

**Answers to guiding questions:**
1. Yes, Gather should explicitly ask for dimensions — but as "independent decision factors" not "parameters."
2. The matrix lives in Extract (Configuration Space). No intermediate artifact needed.
3. CCA belongs in Challenge (Consistency Check). It IS the challenge mindset.

Stage complete: YES
→ Proceeding to Synthesis (RES iter 2).
