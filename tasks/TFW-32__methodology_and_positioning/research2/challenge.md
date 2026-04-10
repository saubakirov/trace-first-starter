# Challenge — Iteration 2: "What do we NOT expect?"
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Predecessor: [Gather2](gather.md), [Extract2](extract.md)
> Goal: Stress-test all designs from Extract against failure modes.

## Findings

### C1: Challenge E1 — Is "Strategic Insights" actually better than "Knowledge Candidates"? Or am I rationalizing?

**Adversary position:** "Strategic Insights" survived because it's the STATUS QUO. Confirmation bias: user likes it → researcher found evidence to support it → external research conveniently confirmed. Classic mirror-and-elevate (sycophancy pattern from VLM-3 RES3).

**Honest test — run the SAME scenario through each name:**

Scenario: User says during HL discussion: «У нас сезонность — зимой продажи падают на 40%, летом пик. Это влияет на всё планирование.»

| Name | Agent internal question | Capture? | Why |
|------|------------------------|----------|-----|
| Knowledge Candidates | "Is this knowledge?" → Yes, it's knowledge about the business | ✅ Captures | But ALSO captures "project uses PostgreSQL" (too broad) |
| Strategic Insights | "Is this strategic?" → Seasonality... is it strategy? It's a FACT about the business. Is a fact strategic? | ⚠️ Hesitation | Agent might classify as "domain fact" not "strategic insight" |
| Strategic Signals | "Is this a signal?" → Yes, 40% drop is a strong signal that shapes decisions | ✅ Captures | "Signal" = anything that should change how we act |
| Domain Intelligence | "Is this domain intel?" → Yes, business seasonality = domain | ✅ Captures | But misses emotional/process signals |

**Second scenario:** User says: «Я попробовал запустить три ресерча подряд и мне понравилось.»

| Name | Agent internal question | Capture? |
|------|------------------------|----------|
| Knowledge Candidates | "Is this knowledge?" → Yes? Maybe? It's a preference... | ⚠️ Unclear |
| Strategic Insights | "Is this strategic?" → Process preference = not strategy | ❌ Likely skips |
| Strategic Signals | "Is this a signal?" → User expressing satisfaction + process insight = signal | ✅ Captures |
| Domain Intelligence | "Is this domain intel?" → No, it's process | ❌ Skips |

**Third scenario:** User says: «Меня бесит что агент вечно торопится закончить.»

| Name | Agent internal question | Capture? |
|------|------------------------|----------|
| Knowledge Candidates | "Knowledge?" → Frustration isn't knowledge | ❌ Skips |
| Strategic Insights | "Strategic?" → Frustration = emotional, not strategic | ❌ Skips |
| Strategic Signals | "Signal?" → Strong emotional signal about system design requirement | ✅ Captures |
| Domain Intelligence | "Domain?" → No | ❌ Skips |

**Result table:**

| Name | Scenario 1 (business fact) | Scenario 2 (process preference) | Scenario 3 (emotion) | Precision | Recall |
|------|---------------------------|--------------------------------|----------------------|-----------|--------|
| Knowledge Candidates | ✅ | ⚠️ | ❌ | Low (captures noise) | Medium |
| Strategic Insights | ⚠️ | ❌ | ❌ | High (but too narrow) | Low |
| **Strategic Signals** | ✅ | ✅ | ✅ | High (signal = filter) | High |
| Domain Intelligence | ✅ | ❌ | ❌ | Medium | Low |

**Verdict:** "Strategic Signals" wins the scenario test. "Strategic Insights" DOES have the gap I found — it misses process preferences and emotional signals. "Knowledge Candidates" is too broad. "Strategic Signals" captures all high-value human input because "signal" = "anything that should change how we act."

**But — one more test.** "Strategic Signals" in the template instruction block. How does it read?

```
## Strategic Signals
> Watch for: corrections, emotions, domain knowledge, strategic decisions, business context.
> Human-Only Test: Would this be unknown without the user saying it?
```

vs current:
```
## Strategic Session Insights
> Watch for: corrections, emotions, domain knowledge, strategic decisions, business context.
```

"Signals" reads naturally. "Signal" implies the agent is a RECEIVER — it detects signals from the human. This matches the SECI Socialization phase (tacit→tacit in conversation, then captured).

**Final assessment:** "Strategic Signals" > "Strategic Insights" > "Knowledge Candidates". But the margin between Signals and Insights is small — both are 10x better than "Knowledge Candidates." If "Signals" feels too technical for non-engineer audience, "Insights" is acceptable fallback.

### C2: Challenge E2 — Does adding Strategic Insights/Signals to RES and RF create template bloat?

**Current RF sections:** 7 sections (§1-§7, where §7 doesn't exist — §6 is last)
**Proposed RF sections:** 8 sections (add §7 Strategic Signals)

**Is this too many?** Check: does every section serve a unique purpose?

| § | Section | Purpose | Overlap? |
|---|---------|---------|----------|
| 1 | What Was Done | File inventory | None |
| 2 | Key Decisions | Design rationale | None |
| 3 | Acceptance Criteria | DoD verification | None |
| 4 | Verification | Build/test results | None |
| 5 | Observations | Agent-observed tech issues (→ TECH_DEBT) | None |
| 6 | Fact Candidates | Project facts (→ /tfw-knowledge) | ⚠️ Overlaps with proposed §7 |
| 7 | Strategic Signals (NEW) | Human-sourced domain knowledge (→ /tfw-knowledge) | ⚠️ Overlaps with §6 |

**Challenge:** If we have BOTH §6 and §7, the agent must classify. Classification = cognitive load = errors.

**Counter-challenge:** The classification heuristic IS the Human-Only Test. §6 = agent can discover from code. §7 = only human knows. This heuristic already exists in the §6 instructions — it's just not enforced by structure.

**But wait — do we even need §6 "Fact Candidates" anymore?**

If §5 Observations captures agent-observed technical facts (→ TECH_DEBT)...
And §7 Strategic Signals captures human-sourced knowledge (→ /tfw-knowledge)...
What does §6 "Fact Candidates" capture that isn't covered?

**Testing: what's in §6 that isn't §5 or proposed §7?**

From RES1 FC list:
- FC1-FC5, FC8: Human-sourced → should be §7 Strategic Signals
- FC6-FC7, FC9: Research-derived findings → these are METHODOLOGY observations about frameworks (SECI, Confluence). Not tech debt (§5), not human-sourced (§7). They're... research conclusions about the external world.

**In RF:** these would be §2 Key Decisions or §1 What Was Done. There's no "external world observations" category in RF because execution is internal.

**In RES:** these are literally the Decisions table. Research findings go to Decisions.

**Conclusion: §6 Fact Candidates might be redundant once §7 exists.**

| Section | What it captures | Flow |
|---------|-----------------|------|
| §5 Observations | Agent-observed internal issues | → TECH_DEBT.md via /tfw-review |
| §7 Strategic Signals | Human-sourced external knowledge | → knowledge/ via /tfw-knowledge |
| §6 Fact Candidates | ??? | → /tfw-knowledge (but what specifically?) |

**Conservative path:** Keep §6, sharpen its scope to "operational patterns about the project" — things that aren't tech debt but ARE agent-observable (e.g., "this project has no tests", "deploy takes 20 minutes", "the team uses RU in commit messages"). Low-cost to keep, low risk.

**Aggressive path:** Remove §6, merge upward. §5 handles internal tech. §7 handles external knowledge. §2 Key Decisions handles research conclusions.

**Recommendation:** Keep §6 but rename to something more precise. Options:
- "Project Patterns" — agent-observable operational patterns
- "Operational Observations" — overlaps with §5 naming
- Just keep "Fact Candidates" with sharpened instructions

This is a coordinator decision. Not critical for THIS research — the IMPORTANT fix is adding §7.

### C3: Challenge E3 — Visualization section: what if ONE name doesn't work?

**Adversary position:** Different artifacts need different framing. Forcing one name = LCD (lowest common denominator).

**Test: Can a SINGLE instruction block per template compensate for a generic name?**

Using "Diagrams" (V1, most generic):

**HL template:**
```
## Diagrams
> Show the target state visually. Choose what fits:
> - Value delivery flow (user → steps → value received)
> - Architecture overview (components, connections)
> - Before → After comparison
> Format: ASCII, mermaid, or hand-drawn sketch.
```

**RF template:**
```
## Diagrams
> Show what was built. Choose what fits:
> - Technical flow (API calls, DB operations, sequences)
> - Data flow (input → transform → output)
> - Deployment topology
> Format: ASCII, mermaid, or plantuml.
```

**RES template:**
```
## Diagrams
> Visualize research findings. Choose what fits:
> - Concept map (relationships between discoveries)
> - Comparison matrix (alternatives evaluated)
> - Process model (if business process was researched)
> Format: ASCII, mermaid, or table.
```

**Does it work?** Each instruction block is specific enough. The SECTION NAME is just an anchor — the instructions do the real work. Similar to how arc42 §5 "Building Block View" contains completely different content at Level 1 vs Level 3, but the section name is the same.

**Counter-test: When would it FAIL?**
- Agent sees "## Diagrams" in HL and thinks "I need to draw something" even when text is sufficient → Solution: add "Optional — include only when visual adds clarity over text" to instructions
- During 📚 KNW consolidation, all "Diagrams" sections are collected → Do they merge cleanly? Mixed levels (vision + detail) in one collection → Need clear labeling in the diagram itself

**Alternative test with "Visual Evidence" (V5):**
- "Evidence" pressures agent to PROVE something visually
- In HL: evidence of what? Nothing is built yet. → Awkward fit
- In RF: evidence of what was built → natural fit
- In RES: evidence of findings → natural fit

**"Diagrams" works better for HL. "Visual Evidence" works better for RF/RES.**

**Resolution:** "Diagrams" is the simplest, most universal, least prescriptive name. The INSTRUCTIONS carry the behavioral load. The name is just a navigation anchor.

But this needs user validation. Marking as PARTIAL — recommend continuing in iteration 3 if user wants more exploration.

### C4: Challenge E4 — What if iterations.yaml becomes stale or contradicts RES?

**Scenario 1:** Researcher writes RES concluding "H6 is not important" but iterations.yaml says H6 is a gap. Who wins?
- **Answer:** Researcher's RES supersedes. iterations.yaml records what the researcher FOUND, including the conclusion that H6 is not important. Coordinator reads both and decides. The YAML is a tracking file, not authority.

**Scenario 2:** Coordinator sets min_iterations: 3 but after iteration 1 all hypotheses are tested. Researcher says SUFFICIENT.
- **Answer:** Coordinator evaluates. If genuinely sufficient → reduce min_iterations and proceed. The YAML is coordinator-owned — coordinator can change it.
- **Risk:** Coordinator under time pressure rubber-stamps SUFFICIENT → same fast-run problem
- **Mitigation:** Coordinator mindset (plan.md) already handles this: "uncomfortable questions, anti-rush." Add: "For multi-iteration research: check iterations.yaml gaps list. If gaps remain, justify why they don't matter before closing."

**Scenario 3:** Researcher ignores iterations.yaml entirely, writes standard RES, says "Research complete."
- **Answer:** Role Lock prevents researcher from proceeding to HL/TS. Coordinator receives RES, checks iterations.yaml, sees iteration 1 of 3 → launches next. Structural enforcement works even if researcher ignores YAML.
- **Key:** The gate is in the COORDINATOR, not the researcher. Researcher can try to fast-run, but coordinator blocks.

**Scenario 4:** No coordinator (user runs everything alone).
- **Answer:** The user IS the coordinator. iterations.yaml serves as their own reminder. The researcher's exit message ("Iteration 1 of 3. Gaps remain. Launch next.") prompts the user to continue.

**All scenarios handled.** The design is sound because:
1. iterations.yaml = tracking, not authority
2. Coordinator = gate keeper (not researcher)
3. Researcher exit message = forcing function for user awareness
4. min_iterations = hard floor but coordinator-modifiable

### C5: Challenge — Does the two-level process representation (E5) actually work in non-code domains?

**Test: TFW used for analytics project (CFO financial analysis)**

HL Value Delivery Flow:
```
Raw 1C Data → Parse → Normalize → Google Sheets → CFO Dashboard → Decision
```
✅ Works — shows where value is delivered (CFO makes decision).

RF Technical Detail:
```
1C Export (XML) → Node.js Parser → Sheets API → formatted cells → pivot formulas
```
✅ Works — shows exact implementation.

**Test: TFW used for education (course design)**

HL Value Delivery Flow:
```
Syllabus Requirements → Topic Selection → Material Creation → Student Assessment → Grade
```
✅ Works — non-technical but still a value flow.

RF Detail:
```
DOCX Template → 7-table structure → AI-generated content → Manual review → Upload to Moodle
```
✅ Works — implementation details.

**Test: TFW used for writing/research (this meta-task)**

HL Value Delivery Flow:
```
Insight/Gap → HL → RES (iteration 1..N) → TS → Execution → REVIEW → Knowledge
```
✅ Works — the TFW pipeline IS the value flow.

RF Detail:
```
HL §10 hypotheses → Gather (web search + file analysis) → Extract (design) → Challenge (stress test) → RES synthesis
```
✅ Works.

**Verdict:** Two-level representation works across all TFW domains (code, analytics, education, research, writing). The abstraction is domain-agnostic.

### C6: Challenge — Is the whole "add Strategic Signals + Diagrams to templates" approach too heavy for simple tasks?

**Current template weight:**
- RF: 74 lines (6 sections)
- HL: 128 lines (11 sections)
- RES: 59 lines (7 sections)

**After changes:**
- RF: ~85 lines (+§7 Strategic Signals, +§Diagrams with instructions)
- HL: ~135 lines (§3.1 already exists → expand instructions)
- RES: ~70 lines (+§Strategic Signals, +§Diagrams)

**Growth:** ~10-15 lines per template. Marginal.

**But:** Every new section is a DECISION POINT for the agent. "Should I write here? Is this relevant?" × N sections = cumulative cognitive load.

**Mitigation:** Same pattern as RF §5 Observations:
> "If nothing found: `No observations.`"

Apply to new sections:
> "If no diagrams needed: `No visual representation required.`"
> "If no strategic signals captured: `No strategic signals in this session.`"

**Verdict:** Acceptable growth. The explicit "nothing found" instruction prevents section anxiety.

## Summary of Challenge Results

| Design | Challenge Result | Status |
|--------|-----------------|--------|
| E1: "Strategic Signals" vs "Strategic Insights" | Signals wins scenario test (3/3 captures vs 1/3). But margin is functional, not catastrophic | ✅ CONFIRMED: Signals > Insights > Knowledge Candidates |
| E2: Add §7 to RF/RES templates | Works. §6 Fact Candidates becomes semi-redundant but keep for safety | ✅ CONFIRMED with note: §6 scope needs sharpening |
| E3: "Diagrams" as universal section name | Works with per-template instructions. Not perfect for HL but acceptable | ⏸️ PARTIAL: recommend iteration 3 for final naming |
| E4: iterations.yaml enforcement | All 4 failure scenarios handled. Coordinator-as-gate-keeper is the key | ✅ CONFIRMED |
| E5: Two-level process representation | Works across 4 domains (code, analytics, education, research) | ✅ CONFIRMED |
| E6: Template bloat risk | ~10-15 lines growth per template. "No X" escape hatch handles empty sections | ✅ ACCEPTABLE |

**Sufficiency:**
- [x] External source used? Scenario-based testing, cross-domain validation
- [x] Briefing gap closed? All 4 hypotheses challenged

**Deep mode criteria:**
- [x] Hypothesis tested? H5b challenged (Signals vs Insights — scenario test, not opinion). H6/H6b challenged (bloat, LCD). H7b challenged (4 failure scenarios)
- [x] Counter-evidence sought? Tested if "Strategic Insights" surviving = confirmation bias (it partially was — Signals is genuinely better in edge cases). Tested if iterations.yaml is over-engineering (it's not — coordinator gate requires it)

**Metacognitive check:** Genuine edge case discovered: "Strategic Insights" DOES miss non-strategic human signals (process preferences, emotions). This wasn't just confirming what I already knew — scenario 2 and 3 exposed a real behavioral gap. The Signals vs Insights distinction is small but meaningful.

Stage complete: YES
→ Ready for Synthesis (RES iteration 2)
