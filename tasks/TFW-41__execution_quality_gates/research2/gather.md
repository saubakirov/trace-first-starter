# Gather — Iteration 2
> Parent: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> Goal: Embed Zwicky heuristics into existing research stages naturally.

## Findings

### G1: GMA Step → TFW Stage Natural Mapping

GMA has 6 steps (from swemorph.com canonical source). TFW research has 3 stages + synthesis. The mapping:

```
GMA Step                          TFW Stage        Natural fit?
─────────────────────────────     ────────────     ────────────
1. Problem Decomposition          GATHER           ✅ Perfect — Gather already asks "what
                                                   do we NOT know?" Decomposing into 
                                                   independent parameters IS identifying
                                                   what you don't know.

2. Enumerate Values               GATHER→EXTRACT   ⚠️ Split — Gather collects raw options,
                                                   Extract structures them into parameters.

3. Construct Morphological Field  EXTRACT          ✅ Perfect — Extract is "what do we NOT
                                                   see?" Building the matrix is exactly
                                                   seeing the full space you didn't see.

4. Cross-Consistency Assessment   CHALLENGE        ✅ Perfect — Challenge is "what do we NOT
                                                   expect?" CCA = finding unexpected
                                                   inconsistencies between pairs.

5. Iterative Refinement           OODA loop        ✅ Already built-in — the OODA loop
                                                   within each stage handles this.

6. Synthesis & Evaluation         RES synthesis     ✅ Already built-in — RES template
                                                   has Decisions and Recommendations.
```

**Key insight:** The mapping is almost 1:1. GMA steps don't need a separate "Zwicky Box section" — they ARE the stage heuristics. The problem in HD-19 was that all 6 steps were crammed into Extract as one "Section C" blob, violating the natural stage roles.

### G2: HD-19 Failure — Wrong Stage Distribution

In HD-19 extract.md, the Zwicky Box section appeared as one monolithic block:
- Parameters defined in-place (should have been in Gather)
- Values listed in-place (should have been in Gather findings)
- "Рекомендуется" annotated before any elimination (should have been in Challenge)
- No CCA at all (should have been Challenge's core job)
- Everything crammed into Extract as a single table

**What should have happened:**
1. **Gather** finds G1: "Working schedule has 3 storage options" → these are **dimensions** with **alternatives**, not "findings" in the narrow sense.
2. **Extract** builds the full cross-reference matrix from Gather dimensions. No recommendations yet.
3. **Challenge** performs CCA: "D1-Alt1 × D2-Alt2 — compatible? Yes/No/Why?" and eliminates pairs.
4. **RES** picks from surviving configurations.

### G3: The "Heuristic" vs "Instruction" Distinction

The iter 1 approach (DR4/DR5) was instruction-based: "MUST do Zwicky Box." The user observed this produces simulation.

A heuristic approach would GUIDE the researcher's thinking at each stage without naming "Zwicky" or "morphological analysis." The researcher naturally decomposes, enumerates, and eliminates because the template QUESTIONS lead there.

**The mechanism:** Each stage template's heading question already implies the right GMA step:
- "What do we NOT know?" → You don't know the full parameter space → Decompose
- "What do we NOT see?" → You don't see all combinations → Enumerate & cross-reference
- "What do we NOT expect?" → You don't expect which combinations are inconsistent → CCA

The templates just need to make these implications EXPLICIT with one-line heuristics, not with procedural instructions.

### G4: Existing Template Gaps — What's Missing

Current templates are maximally open-ended:
- Gather: `{content}` — no guidance on HOW to structure findings
- Extract: `{content — patterns, comparisons, internal file analysis}` — hints at patterns but no requirement to enumerate alternatives
- Challenge: `{content — what could go wrong, alternatives, counter-evidence}` — mentions "alternatives" but doesn't require systematic elimination

**What's needed:** One structural heuristic per stage that nudges toward the GMA step without naming the methodology. The heuristic should feel like natural stage discipline, not like a separate exercise.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| GMA maps 1:1 to Gather→Extract→Challenge | Need to design exact template wording |
| HD-19 failure = wrong stage distribution (all in Extract) | Need to test proposed wording against HD-19 |
| Heuristic > Instruction approach for preventing simulation | Need to compare with iter 1 DR4 approach |

**Sufficiency:**
- [x] External source used? (GMA canonical methodology from swemorph.com)
- [x] Briefing gap closed? (Mapping complete, HD-19 diagnosed)

Stage complete: YES
→ Proceeding to Extract.
