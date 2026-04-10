# Positioning Spec — TFW README Improvement

> **Source decisions**: D5 (RES1), D9 (RES1)
> **Source insights**: S1-S17 (HL §11)
> **Source research**: G2 (gather.md), VLM-3 RES3 D19-D20
> **See also**: [audience_personas.md](audience_personas.md), [translation_table.md](translation_table.md)

---

## Section A — Value Proposition

### The Paragraph

> Trace-First Workflow is a team knowledge methodology that generates institutional memory as a byproduct of working. Every task — whether code, analytics, writing, or business process — moves through a structured lifecycle that captures not just results, but intent, decisions, constraints, and rejected alternatives. Where tools like Confluence and Notion require someone to manually write and maintain documentation, TFW produces it automatically: the traces left by working *are* the documentation. AI agents are team members in this framework, not individual assistants — they read the same traces, follow the same lifecycle, and contribute to the same knowledge base. Over 10, 50, or 100 tasks, a TFW project compounds knowledge that makes every next decision better, every onboarding faster, and every context switch lossless.

### Decomposition

| Element | In the paragraph | Source |
|---------|-----------------|--------|
| **Pain** | *(implied)* Growing teams/projects lose knowledge when decisions don't propagate | D5, S11 |
| **Mechanism** | "generates institutional memory as a byproduct of working" | D5 |
| **Differentiator** | "Where Confluence/Notion require someone to manually write... TFW produces it automatically" | D5, FC7 (RES1) |
| **Team frame** | "AI agents are team members, not individual assistants" | S9, FC3 (RES1) |
| **Domain breadth** | "code, analytics, writing, or business process" | S1 |
| **Compounding** | "Over 10, 50, 100 tasks... compounds knowledge" | S7 (Knowledge Pipeline = killer feature) |

---

## Section B — README.md Improvement Spec

### Section-by-section Analysis

#### 1. Opening Quote Block

**Current** (lines 1-20):
```
> "The thinking is the product. Everything else is output."
> [5-paragraph block about "a product that knows more about itself"]
```

**Direction:**
- KEEP the opening quote — strong, memorable, already serves as tagline (D35)
- ADD a subtitle line after the quote: establish the team methodology frame immediately
- SHARPEN the 5-paragraph block: currently reads as philosophy. Should read as *hook* — problem → promise → proof in 3 sentences max
- The current block is excellent writing but too long for a README opening. Move the full version to `.tfw/README.md` and keep a compressed version here

**Proposed structure:**
```
> "The thinking is the product. Everything else is output."

# Trace-First Workflow

**A team knowledge methodology where every task generates institutional memory — 
not as an afterthought, but as a byproduct of working.**

[2-3 sentence hook: pain + mechanism + result]
```

**Source**: S9 (team tool), D5 (generates vs stores), S2 ("not only programmers, but higher level")

---

#### 2. "Who This Is For" Section

**Current** (lines 27-38):
```
TFW is not about code. It's about making decisions visible and knowledge permanent.
- Business and operations — ...
- Product management — ...
- Software engineering — ...
- Data and analytics — ...
- Writing and publishing — ...
- Education — ...

If your work involves AI-assisted iteration... TFW is for you.
```

**Direction:**
- RESTRUCTURE from flat list to 3-tier hierarchy matching [audience_personas.md](audience_personas.md)
- LEAD with product leaders (Tier 1), not "Business and operations"
- ADD qualifying questions per tier — these are sharper than generic descriptions
- REPLACE generic closing line with universal qualifier: "Teams and individuals who can't afford to lose context"
- REMOVE domain-only bullets (Writing, Education) — fold into domain breadth statement

**Proposed structure:**
```
## Who TFW Is For

**Teams and individuals who can't afford to lose context.**

### Product leaders scaling decisions across teams
[Pain: decisions don't propagate. Value: traceable. Qualifying question.]

### Analysts and researchers building knowledge iteratively  
[Pain: previous analysis not discoverable. Value: compounds. Qualifying question.]

### Product-minded engineers preserving architecture context
[Pain: "why was this built this way?" Value: traces. Qualifying question.]

TFW works for code, analytics, writing, education, and business processes — 
the same lifecycle, the same artifacts, the same knowledge compounding.
```

**Source**: D9 (3-tier hierarchy), S10 ("product people learn faster"), briefing Q3

---

#### 3. Quick Start Section

**Current** (lines 42-86):
```
> For humans: read the philosophy — 5 minutes...
[3 prompt blocks + FAQ]
```

**Direction:**
- KEEP as-is — this section is strong (post-TFW-31 rewrite, D36)
- ADD one starter prompt variant for team onboarding: "I want to set up TFW for my team of [N] people working on [project]..."
- ADD one FAQ question: "How is TFW different from Confluence/Notion?" → "Confluence stores knowledge someone must write. TFW generates knowledge as you work."
- ADD one FAQ question: "Is TFW only for software engineering?" → "No. TFW is a methodology for structuring decisions..."

**Source**: D5 (generates vs stores), S1 (any domain)

---

#### 4. "How It Works" Section

**Current** (lines 89-98):
```
- Your product becomes self-aware.
- Any agent can resume from any checkpoint.
- Knowledge compounds instead of evaporating.
- One ritual, any domain.
```

**Direction:**
- KEEP structure — 4 bullets is concise and strong
- SHARPEN bullet #3: add "generates vs stores" contrast — "Knowledge compounds instead of evaporating. Unlike documentation tools that require someone to manually write and maintain content, TFW captures knowledge as a byproduct of the work itself."
- CONSIDER adding bullet #5: "AI agents are team members." — "Your AI assistants don't start from zero. They read the same traces your human team reads, follow the same lifecycle, and contribute to the same knowledge base."

**Source**: D5, S9, FC3

---

#### 5. "What's Inside" and "Tool Adapters" Sections

**Current** (lines 101-141):
```
[Two reference tables]
```

**Direction:**
- KEEP as-is. These are reference sections that serve engineers (Tier 3)
- No changes needed — technical users need exact file paths and structures

---

#### 6. "Key Concepts" Section

**Current** (lines 145-153):
```
- Task lifecycle: ... (pipeline with 📚 KNW already shown)
- Execution modes, scope budgets, conduct, versioning
```

**Direction:**
- ALREADY CURRENT post-Phase A — pipeline includes `📚 KNW`
- ADD link to translation table once published: "See business-language equivalents for these terms"

---

#### 7. Links Section

**Current** (lines 156-161):
```
- Repository, Author, License
```

**Direction:**
- ADD "Getting Started" → `.tfw/quickstart.md`
- ADD "Documentation" → `tfw.saubakirov.kz` (docs site already deployed per TFW-27/C)
- ADD "Philosophy" → `.tfw/README.md`

---

#### 8. Missing Sections (Proposed Additions)

**"Why TFW?" section** — Add between opening block and "Who This Is For":
```
## Why TFW?

Growing teams lose knowledge when decisions don't propagate. Context dies with 
chat sessions. New team members re-learn everything from scratch. The "why" behind 
every choice lives in someone's head — until they leave.

TFW fixes this structurally: every task produces traces that capture intent, 
decisions, constraints, and rejected alternatives. Knowledge compounds across 
tasks instead of evaporating between sessions.
```

**Source**: D5, S11, S4

---

## Section C — Competitive Frame

### Positioning Matrix

```
                    GENERATES knowledge          STORES knowledge
                    (byproduct of work)          (requires manual effort)
                    ─────────────────────        ──────────────────────
TFW                 ✅ Traces = byproduct         —
                    of working methodology

Confluence          —                             ✅ Someone must write docs.
                                                  Enforcement-based preservation.

Notion              —                             ✅ Flexible but unstructured.
                                                  Usability-based preservation.

No methodology      —                             ❌ Knowledge lives in heads.
                                                  Evaporates on team changes.
```

### "Generates vs Stores" Explanation

**Confluence** protects knowledge through enforcement — templates, mandatory fields, approval workflows. Someone must write the documentation. Once written, it decays unless actively maintained. Nobody reads stale docs.

**Notion** protects knowledge through usability — beautiful interface, easy editing, flexible structure. Still requires someone to write and maintain. Knowledge exists only if someone decides to capture it.

**TFW** generates knowledge as a byproduct of working. When you plan a task (HL), the reasoning is captured. When you research (RES), the findings are captured. When you execute (RF), the decisions are captured. When you review (REVIEW), the observations are captured. Nobody has to "write documentation" — the methodology produces it.

**Source**: D5, FC7 (RES1), HL §3.2 Value Flow diagrams

### 8 Unique Features (validated, VLM-3 RES3 D19)

These features were tested against 5 top coding/knowledge tools. The Knowledge Pipeline bundle survived sycophancy demolition (RES3: 2/8 claims survived independently, Knowledge Pipeline was one of them).

| # | Feature | What it means | Why unique |
|---|---------|--------------|-----------|
| 1 | **Knowledge Pipeline** (lifecycle) | Fact candidates → consolidation → verified knowledge → topic files | No tool combines capture + verification + consolidation + domain-agnostic storage. Individual components exist (Copilot Memory, cursor-memory), but the bundle is unique |
| 2 | **Multi-iteration research** | Structured investigation: hypotheses → evidence → decisions across multiple AI sessions | No coding agent formalizes research as a pipeline stage with iteration tracking (iterations.yaml, mandatory exit protocol) |
| 3 | **Role Lock** | Coordinator ≠ Executor ≠ Researcher ≠ Reviewer — structural separation | Tools have "modes" but not enforced role separation with prohibited artifacts per role |
| 4 | **Thinking traces** (future — S6, VLM-3 D20) | Capturing AI reasoning (`<think>` blocks) as first-class project artifacts | Nobody captures thinking for knowledge extraction. Observability tools (LangSmith, Langfuse) log for debugging only |
| 5 | **Domain-agnostic methodology** | Same lifecycle for code, analytics, writing, education, business | All competitors are code-first. TFW is methodology-first, code-optional |
| 6 | **Scope budgets** | Configurable limits per work phase (files, LOC, new files) calibrated for AI agents | No tool provides structural guardrails for AI agent scope per task |
| 7 | **Knowledge Gate** | Periodic consolidation checkpoint: "Have we captured what we learned?" | No tool gates the next task on knowledge capture from the previous one |
| 8 | **Filesystem state machine** | File existence = stage completion. No parsing, no state tables, no format compliance | Unique structural enforcement pattern — most tools use in-memory or database state |

### Competitive Comparison (for FAQ)

**"How is TFW different from Confluence/Notion?"**

Confluence and Notion are knowledge *storage* tools — they hold what someone decides to write. TFW is a knowledge *generation* methodology — it captures decisions, reasoning, and alternatives as a byproduct of working. You don't document your decisions; your decisions document themselves.

**"How is TFW different from Cursor/Claude Code/AI coding assistants?"**

AI coding assistants help you write code faster. TFW helps you preserve the *context* that makes code maintainable. They're complementary: TFW works *inside* these tools (via adapters) to add traceability, knowledge capture, and structured decision-making to the AI-assisted workflow.

**Source**: VLM-3 RES3 D19 (Knowledge Pipeline confirmed unique), D20 (thinking traces novel), FC7 (Confluence/Notion competitive analysis)

---

*Positioning Spec — TFW README Improvement | 2026-04-10*
*Sources: D5, D9 (RES1), S1-S17 (HL §11), G2 (gather.md), VLM-3 RES3 D19-D20*
