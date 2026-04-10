# Philosophy Improvement Spec — .tfw/README.md

> **Target file**: `.tfw/README.md` (134 lines, 7483 bytes — post-TFW-27 strip, D35)
> **Source decisions**: D5 (RES1), D9 (RES1)
> **Source insights**: S9 (team tool), S11 (communication gaps), S2 ("higher level")
> **See also**: [positioning_spec.md](positioning_spec.md), [audience_personas.md](audience_personas.md)

---

## Summary

`.tfw/README.md` is TFW's philosophy paper — the "thesis" document that explains the *why* behind the methodology. Post-TFW-27 (D35), it was stripped to 134 lines of pure philosophy: no reference tables, no lifecycle diagrams, no technical details. The philosophy is strong. The gap is narrow: it frames the problem and solution for an individual developer ("You open a new session"), when TFW's positioning is team-centric ("Teams that can't afford to lose context").

This spec proposes targeted additions and rewrites — not a restructure. The philosophy paper's voice and quality should be preserved.

---

## Section-by-section Analysis

### 1. "The Problem: Knowledge Evaporates" (lines 7-27)

**Current state:**
- Strong writing. Clear problem statement.
- Individual-focused framing: "You open a new session. The context is gone. You re-explain everything from scratch."
- Symptoms list is developer-focused: "threads branch," "model resets," "context windows truncate"

**Direction:**
- ADD team dimension early — after the individual framing, extend to team: "Now multiply this by a team. Your colleague opens a new session — and the context you built yesterday is invisible to them. Decisions made in one conversation don't propagate to the next person. Knowledge lives in people's heads."
- ADD one symptom bullet for team knowledge loss: "Team members re-learn context that was established in previous sessions by other people"
- KEEP the individual framing as the entry hook — it's relatable and strong. The team extension deepens it.
- KEEP "The common fixes don't work" — these are universally true for both individual and team scenarios

**Proposed addition** (after line 12, "This is not a minor annoyance..."):
```
Scale this to a team and the problem becomes structural. Your colleague opens 
a new session — and the context you built yesterday is invisible. A product 
manager's strategic decision doesn't reach the developer implementing it. 
An analyst's finding doesn't reach the team member who needs it. Knowledge 
lives in people's heads, in Slack threads, in meeting notes that nobody re-reads.
```

**Source**: S9 (team tool), S11 ("any growing business suffers from communication gaps")

---

### 2. "The Thesis: Traces Over Code" (lines 32-52)

**Current state:**
- Core thesis is clean and well-articulated
- Table (Traditional vs Trace-First) is strong — 4 rows, clear contrast
- Final paragraph frames TFW as "AI-First philosophy" with a correct but narrow scope: "the human's job shifts from *writing* code to *managing* the context"

**Direction:**
- ADD explicit team value after the table: "Traces are the team's shared memory. When any team member — human or AI — reads the HL, TS, and RF chain, they understand not just what exists, but why it exists, what was considered, and what was rejected."
- ADD "generates vs stores" positioning: "Unlike knowledge tools that require someone to write and maintain documentation, TFW generates knowledge as a byproduct of the methodology itself."
- ADD one row to the table:

| Traditional | Trace-First |
|:--|:--|
| Team knowledge lives in Slack threads and meetings | Team knowledge lives in structured traces that any member can read |

- KEEP "AI-First philosophy" framing — it's accurate and aligns with the methodology's actual mechanism

**Source**: D5 ("generates vs stores"), S9 ("team tool, AI agents are team members"), FC3 ("one repo for all roles")

---

### 3. "How TFW Works" (lines 55-65)

**Current state:**
- Good description: "A task moves through a deterministic lifecycle..."
- Lists the lifecycle stages correctly
- "domain-agnostic" and "tool-agnostic" framing is present and correct

**Direction:**
- ADD team/role breadth statement: "The same ritual works whether you're a product manager, data analyst, or engineer. The lifecycle adapts to the domain — not the other way around."
- ADD the universal qualifier: "TFW is for teams and individuals who can't afford to lose context."
- KEEP the lifecycle description — it's concise and accurate

**Proposed addition** (after line 63, "...or a plain chat window."):
```
The same ritual works whether you're a product manager planning strategy, 
a data analyst building iterative research, or an engineer implementing 
architecture. TFW is for teams and individuals who can't afford to lose context.
```

**Source**: D9 (audience hierarchy), S1 ("value OS for any domain")

---

### 4. "Values and Principles" (lines 69-102)

**Current state:**
- 8 values, well-articulated: Traces Over Code, Candor Over Flattery, Completeness Over Speed, Honesty Over Convincingness, Structural Enforcement, Naming Creates Behavior, Single Source of Truth, Portability
- Domain-agnostic already — no code-specific language
- Strong voice: direct, opinionated, concrete

**Direction:**
- NO CHANGES NEEDED. Values are strong, domain-agnostic, and well-written.
- Verified: all 8 values apply equally to product leaders, analysts, and engineers.
- The values section is the strongest part of this document.

---

### 5. "Anti-patterns" (lines 105-110)

**Current state:**
```
> Full list → conventions.md §14
These exist because every single one has happened and caused real problems.
```

**Direction:**
- KEEP as-is. Brief reference to conventions.md is appropriate for a philosophy paper.

---

### 6. "Success Criteria" (lines 112-121)

**Current state:**
```
1. End-to-end AI execution — the AI handles the task without manual editing...
2. Prompt-driven workflow — every decision is traceable...
3. Atomic scope — tasks are small enough...
4. Self-verification — the AI checks its own work...
```

**Direction:**
- REFRAME from engineering-specific to team-centric:
  - Current #1 focuses on "AI handles the task" — this is an implementation detail, not a success criterion for a team methodology
  - Current #4 "self-verification" is engineering-focused

**Proposed rewrite:**
```
A TFW project is successful when:

1. **Any team member can resume from any checkpoint** — a new person (human or AI) 
   reads the Task Board and relevant traces, and picks up where the previous one 
   left off. No re-explanation needed. No context lost.

2. **Every decision is traceable** — for any choice in the project, you can find 
   the reasoning: what prompted it, what alternatives existed, what was rejected 
   and why.

3. **Knowledge compounds over time** — the project accumulates structured knowledge 
   that makes every next decision better, every onboarding faster, and every context 
   switch lossless.

4. **The output requires no manual editing** — if the result is wrong, you fix the 
   prompt and the context, not the output. The traces are complete enough to produce 
   correct results.
```

**Source**: D9 (team framing), S9 ("AI agents are team members"), D5 ("knowledge compounds")

---

### 7. PROPOSED NEW SECTION: "How TFW Compares"

**Position**: After "Success Criteria", before "Version History"

**Rationale**: The philosophy paper explains *what* TFW is and *why* — but never addresses the implicit question: "Why not just use Confluence/Notion?" This section addresses the competitive positioning gap identified in D5 and G2.

**Proposed content:**

```
## How TFW Compares

TFW occupies a different category from most tools people compare it to.

**Knowledge storage tools (Confluence, Notion, wikis)**
These tools protect existing knowledge — through enforcement (Confluence) or 
usability (Notion). But someone must write the documentation. Someone must 
maintain it. And when nobody does, knowledge decays, goes stale, and stops 
being read.

TFW doesn't store knowledge — it generates it. The traces produced by planning, 
researching, executing, and reviewing ARE the documentation. Nobody writes it 
separately. Nobody maintains it separately. The methodology produces it as a 
byproduct of working.

**AI coding assistants (Cursor, Claude Code, Copilot)**
These tools help you write code faster. TFW helps you preserve the context 
that makes code maintainable. They're complementary: TFW works inside these 
tools (via adapters) to add traceability, knowledge capture, and structured 
decision-making to the AI-assisted workflow.

**No methodology (ad-hoc AI chat)**
Knowledge evaporates between sessions. Decisions don't propagate. New team 
members start from zero. The project can't explain itself.

TFW exists because none of these alternatives solve the core problem: 
growing teams lose knowledge when decisions don't propagate.
```

**Source**: D5 (generates vs stores), FC7 (competitive analysis), G2 (Shape Up/DORA pattern: define category, then contrast)

---

## Changes Summary

| Section | Change type | Impact |
|---------|------------|--------|
| The Problem | ADD team dimension paragraph | Medium — extends framing |
| The Thesis | ADD table row + generates vs stores + team memory line | Medium — sharpens positioning |
| How TFW Works | ADD role breadth + universal qualifier | Low — 2 sentences |
| Values and Principles | NO CHANGES | — |
| Anti-patterns | NO CHANGES | — |
| Success Criteria | REWRITE 4 criteria → team-centric framing | High — different emphasis |
| How TFW Compares | NEW SECTION | High — addresses competitive gap |

**Estimated word count change**: +300 words (from ~1100 to ~1400). Within philosophy paper scope.

---

*Philosophy Improvement Spec — .tfw/README.md | 2026-04-10*
*Sources: D5, D9 (RES1), S9, S11 (HL §11), FC7 (gather.md), G2 (positioning patterns)*
