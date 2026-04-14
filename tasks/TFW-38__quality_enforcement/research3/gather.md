# Gather — Iteration 3
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: (A) TS over-specification audit, (B) Naming matrix for all review terms.

## Thread A: TS Over-Specification Audit

### G1: TS Template vs Real TS Content

**TS template (`.tfw/templates/TS.md`)** defines §4 as:
```
## 4. Detailed Steps
### Step 1: {title}
{What to do, with code examples if relevant}
```

The template says "with code examples **if relevant**" — which is permissive, not prescriptive. It doesn't say "write the complete implementation."

### G2: HD PhaseD TS — 1036 lines, 41KB

**Content classification:**

| Section | Lines | Content Type |
|---------|-------|-------------|
| §1 Objective | 3 | Requirement (WHAT) |
| §2 Scope | 25 | Requirement |
| §3 Affected Files | 16 | Design direction |
| §4 Step 1 Common Schemas | 27 | **FULL IMPLEMENTATION** — complete Python classes |
| §4 Step 2 Ticket Schemas | 121 | **FULL IMPLEMENTATION** — every field, every type hint, every docstring |
| §4 Step 3 SLA Engine | 194 | **FULL IMPLEMENTATION** — complete class with all methods, algorithms, edge cases |
| §4 Step 4 Ticket Repository | 134 | **FULL IMPLEMENTATION** — every CRUD method, advisory lock, pagination |
| §4 Step 5 Ticket Service | 260 | **FULL IMPLEMENTATION** — complete business logic, state machine, SLA integration |
| §4 Steps 6-8 API Routes | 100 | **FULL IMPLEMENTATION** — partial with Python snippets |
| §4 Steps 9-10 Tests | 20 | Requirement (what to test) |
| §5 AC | 34 | Requirement |

**Total code in TS:** ~736 lines of Python out of 1036 total. **71% of the TS is ready-to-paste code.**

### G3: HD PhaseF TS — 356 lines, 14KB

**Content classification:**

| Section | Lines | Content Type |
|---------|-------|-------------|
| §1 Objective | 3 | Requirement |
| §2 Inputs | 12 | Context |
| §3 Steps 1-2 Mat views + schemas | 95 | **CODE** — DDL specs, complete Pydantic schemas |
| §3 Steps 3-4 Analytics Repo + Service | 38 | **Mixed** — method signatures + formulas, not full code |
| §3 Step 5 Report Service | 8 | Requirement (method list) |
| §3 Step 6 Workers | 70 | **FULL CODE** — complete asyncio workers with SQL |
| §3 Steps 7-10 Routes + Tests | 70 | Requirement (endpoint table, test list) |
| AC | 35 | Requirement |

**Code ratio:** ~200 lines of code / 356 total = **56%**. Still more code than spec, but closer to "design direction with examples."

### G4: Atamat TFW-16 PhaseH TS — 546 lines, 19KB

**Content classification:**

| Section | Lines | Content Type |
|---------|-------|-------------|
| §0-1 Scope + Manifest | 38 | Requirement/Design |
| Step 1 geocode_place | 86 | **FULL CODE** — complete Python function |
| Step 2 find_route | 102 | **FULL CODE** — complete Python function |
| Step 3 Agentic Loop integration | 90 | **MIXED** — code snippets at specific line numbers |
| Step 4 Prompt instructions | 22 | **FULL CODE** — exact XML block |
| Step 5 Widget frontend | 118 | **MIXED** — TypeScript types + pseudocode + CSS |
| AC + Verification | 50 | Requirement |

**Code ratio:** ~300 / 546 = **55%**.

### G5: Atamat TFW-16 PhaseF2 TS — 512 lines, 16KB

**Content classification:**

| Section | Lines | Content Type |
|---------|-------|-------------|
| §0-1 Scope + Manifest | 30 | Requirement/Design |
| Step 1-2 isLoading + thinking | 72 | **FULL CODE** — TSX, TypeScript |
| Step 3 RouteStrip | 80 | **PSEUDOCODE** — structure + state logic, not exact code |
| Step 4-5 Integration + CSS | 152 | **FULL CSS CODE** |
| AC + Verification | 60 | Requirement |

**Code ratio:** ~250 / 512 = **49%**.

### G6: TS Over-Specification Summary

| TS | Total lines | Code lines | Code % | Type |
|----|-------------|-----------|--------|------|
| HD PhaseD | 1036 | ~736 | 71% | FULL IMPLEMENTATION |
| HD PhaseF | 356 | ~200 | 56% | MIXED (formulas + code) |
| Atamat PhaseH | 546 | ~300 | 55% | FULL IMPLEMENTATION (tools) |
| Atamat PhaseF2 | 512 | ~250 | 49% | MIXED (pseudo + CSS) |
| **Average** | ~612 | ~371 | **58%** | **More code than spec** |

**Conclusion:** On average, 58% of TS content is ready-to-paste code. HD PhaseD is the extreme case at 71% — the coordinator essentially wrote the entire implementation. The executor's job in such cases is to copy-paste from TS, adjust for runtime issues, and fill in gaps.

**Token cost:** HD PhaseD TS = 41KB. At ~4 chars/token, that's ~10,250 tokens. If 71% is code the executor would have written anyway, ~7,300 tokens were "double-spent" (coordinator writes it, executor reads it and types it).

## Thread B: Naming Matrix

### G7: TFW Naming Principles (from .tfw/README.md §Values)

Key value: **"Naming Creates Behavior"** (line 104-106):
> "Right terminology triggers right associations in AI agents. A small prompt with precise terms is more effective than a long prompt with explanations. TFW adopted OODA, Sufficiency Verdict, Trust Protocol, Progressive Disclosure — each term replaced paragraphs of instructions. If you have to explain what a step does, the step is named wrong."

This is the **ultimate filter**: if the user has to ask "what does this mean?" — the name failed.

User feedback:
- "prose мне непонятно вообще" → FAIL
- "comprehend мне тоже непонятно что это вообще" → FAIL
- "между assess и judge мне больше нравится judge, намерение явное" → assess is unclear, judge is direct

### G8: Existing TFW Naming Patterns

| Current Term | What It Triggers | Works? |
|-------------|-----------------|--------|
| Gather | "Collect data" | ✅ Clear, active verb |
| Extract | "Pull out patterns" | ✅ Clear, active verb |
| Challenge | "Test, push back" | ✅ Clear, active verb |
| Briefing | "Preparation, plan" | ✅ Military metaphor, understood |
| Onboarding | "Learning the context" | ✅ Industry standard |
| Handoff | "Passing to someone" | ✅ Clear metaphor |
| Role Lock | "Can't change role" | ✅ Structural, enforcement |
| Verdict | "Final decision" | ✅ Legal metaphor, decisive |

**Pattern:** TFW uses **short, active, metaphorical terms** from established disciplines (military, legal, engineering). The best terms are 1-2 syllables and need no explanation.

### G9: Candidate Matrix — Review Stages

Current proposal tested in iter 2: Comprehend → Verify → Assess → Synthesize

| Candidate | Syllables | Meaning Clear? | User Test | Parallel Discipline | Score |
|-----------|-----------|---------------|-----------|---------------------|-------|
| **Comprehend** | 3 | "Understand deeply" — pretentious | ❌ "непонятно" | Academic | 2/5 |
| **Read** | 1 | "Look at the document" | ✅ Obvious | — | 4/5 but too passive |
| **Scan** | 1 | "Quick look through" | ✅ Clear | Military/medical | 3/5 too shallow |
| **Orient** | 3 | "Get bearings" | ⚠️ Known from OODA, but alone unclear | Military (OODA) | 3/5 |
| **Study** | 2 | "Read carefully" | ✅ Clear | Academic | 3/5 too passive |
| **Map** | 1 | "Build mental map of what was done" | ✅ Metaphorical, active | Navigation | 4/5 |
| **Verify** | 3 | "Check if claims are true" | ✅ Universal | Engineering/audit | 5/5 |
| **Check** | 1 | "Quick inspection" | ✅ Simple | — | 4/5 too casual |
| **Audit** | 2 | "Systematic examination" | ✅ Clear, strong | Financial/engineering | 4/5 |
| **Assess** | 2 | "Evaluate quality" — vague | ⚠️ "между assess и judge" | HR/education | 3/5 |
| **Judge** | 1 | "Make a decision about quality" | ✅ User prefers | Legal | 5/5 |
| **Rate** | 1 | "Assign score" | ⚠️ Too numerical | — | 2/5 |
| **Weigh** | 1 | "Consider pros/cons" | ✅ Metaphorical | Legal | 3/5 |
| **Synthesize** | 4 | "Combine to produce whole" — academic | ⚠️ Long | Academic | 3/5 |
| **Decide** | 2 | "Make the call" | ✅ Clear, active | Management | 4/5 |
| **Close** | 1 | "Finish, wrap up" | ✅ Clear | Project management | 4/5 |

**Top candidates per stage:**

Stage 1 (understand): **Map** (1 syllable, active, metaphorical)
Stage 2 (check evidence): **Verify** (clear, no alternatives)
Stage 3 (quality judgment): **Judge** (user preference, 1 syllable, direct)
Stage 4 (decide + capture): **Decide** (2 syllables, active) or **Close** (1 syllable, clear)

### G10: Candidate Matrix — Review Modes

Current proposal: code, prose, spec

| Candidate | For Code Tasks | For Writing Tasks | For Analytical Tasks |
|-----------|---------------|-------------------|----------------------|
| A: code / prose / spec | ✅ clear | ❌ user rejects "prose" | ⚠️ OK |
| B: code / content / analysis | ✅ | ⚠️ vague | ⚠️ confusable with data analysis tasks |
| C: build / write / analyze | ✅ active | ✅ clear verb | ⚠️ confusable |
| D: code / docs / research | ✅ | ✅ simple | ⚠️ research collides with RES |
| E: implementation / deliverable / specification | ✅ formal | ⚠️ long | ⚠️ long |
| F: dev / text / study | ✅ short | ✅ short | ⚠️ unclear |

**"prose" alternatives for writing tasks:**
- `text` — too generic
- `content` — vague
- `docs` — clear, short, understood
- `write` — active verb, matches TFW pattern
- `creative` — wrong connotation

**Best option:** modes should match the REVIEW template variant name. They'll appear in `PROJECT_CONFIG.yaml` and be referenced in workflow text. Short, memorable.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| TS are 49-71% ready-to-paste code — confirmed over-specification (G2-G6) | Need to determine: is this a PROBLEM or a FEATURE? |
| "Naming Creates Behavior" is the filter — if you must explain it, it's wrong (G7) | — |
| "comprehend" and "prose" fail the user test (G9, G10) | Need final naming decision |
| Top candidates: Map → Verify → Judge → Decide (G9) | Need challenge validation |
| Mode naming unclear — docs/write are top contenders for writing mode (G10) | Need final decision |

**Sufficiency:**
- [x] External source used? (ISO model from iter2, TFW values)
- [x] Briefing gap closed? (Both threads gathered)

Stage complete: YES
→ User decision: ___
