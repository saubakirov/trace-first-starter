# TS — TFW-32 / Phase B: Naming & Templates

> **Date**: 2026-04-10
> **Author**: AI (Coordinator)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> **Phase HL**: [HL Phase B](HL__PhaseB__naming_and_templates.md)

---

## 1. Objective

Sharpen §6 "Fact Candidates" and §7/§11 "Strategic Insights" instructions in all applicable templates, add per-template visual sections (HL = "Value Flow", RF = "Diagrams", RES = "Findings Map"), enhance HL §3.1 with Working Backwards framing, and document everything in conventions.md and glossary.md. After this phase, every template triggers the empirically correct LLM cognitive mode for each section.

## 2. Scope

### In Scope
- Sharpen §6 "Fact Candidates" instructions in RF, RES, REVIEW templates
- Rename HL §11 "Strategic Session Insights" → "Strategic Insights (Planning)" + tighten instructions
- Add §7 "Strategic Insights (Execution)" to RF template
- Add "Strategic Insights (Research)" to RES template
- Add §3.2 "Value Flow" to HL template
- Enhance HL §3.1 "Result Visualization" with Working Backwards framing
- Add "Diagrams" section to RF template
- Add "Findings Map" section to RES template
- Add Visual Sections cross-reference table to conventions.md
- Add new terms to glossary.md
- Update conventions.md §3 "Fact Candidates" definition

### Out of Scope
- Renaming §6 or §7/§11 (empirically optimal — D15, D16)
- Adding visual section to REVIEW template (checklist, not result)
- Adding §6 to HL template (planning artifact, not execution)
- Workflow changes (Phase A scope)
- KNOWLEDGE.md changes (Phase A scope)
- README changes (Phase D scope)

## 3. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/templates/HL.md` | MODIFY | §11 rename + tighten, add §3.2 Value Flow, enhance §3.1 Working Backwards |
| `.tfw/templates/RF.md` | MODIFY | Add §7 Strategic Insights (Execution), add Diagrams section, sharpen §6 |
| `.tfw/templates/RES.md` | MODIFY | Add Strategic Insights (Research), add Findings Map section, sharpen Fact Candidates |
| `.tfw/templates/REVIEW.md` | MODIFY | Sharpen §5 Fact Candidates instructions |
| `.tfw/conventions.md` | MODIFY | Add Visual Sections cross-reference table, update §3 Fact Candidates definition |
| `.tfw/glossary.md` | MODIFY | Add Value Flow, Findings Map terms. Update Strategic Insight definition |

**Budget:** 0 new files, 6 modifications. Within limits: max 14 files, max 12 modified, max 1200 LOC.

## 4. Detailed Steps

### Step 1: Enhance HL §3.1 — Working Backwards framing

In `.tfw/templates/HL.md`, replace §3.1 instructions.

**Before (lines 24-32):**
```markdown
### 3.1 Result Visualization

> Show the outcome as if it's already achieved. Choose the format that fits:
> - **Diagrams** (architecture, flow, structure) — ASCII, mermaid, or hand-drawn
> - **Before → After tables** — state comparison
> - **Outlines / mockups** — document structure, UI sketches, report layout
> - **Sample output** — example paragraph, data snippet, formula result
>
> Goal: executor and user must see the "finished picture" before work begins.
```

**After:**
```markdown
### 3.1 Result Visualization

> **Working Backwards:** Show the outcome as if it's already achieved. Imagine it's done —
> what does the user see? What changed? Write from the perspective of "6 months after launch."
>
> Choose the format that fits:
> - **Before → After tables** — state comparison with real data
> - **Outlines / mockups** — document structure, UI sketches, report layout
> - **Sample output** — example paragraph, data snippet, formula result
> - **Narrative** — timeline of a user's day after the change ships
>
> This is NOT a process diagram or architecture flow — those belong in §3.2 Value Flow.
> Goal: executor and user must see the "finished picture" before work begins.
```

### Step 2: Add §3.2 Value Flow to HL template

In `.tfw/templates/HL.md`, insert after §3.1 (after line 32), before §4 Phases:

```markdown
### 3.2 Value Flow

> Visualize HOW value gets created — the machine, not the outcome.
> Show the flow from user pain → pipeline steps → value delivered.
>
> Formats:
> - **ASCII flow** — `INPUT → PROCESSING → OUTCOME` with value labels
> - **Mermaid diagram** — for complex multi-path flows
> - **Value stream table** — columns: Step, Input, Transformation, Value Created
>
> This is NOT the outcome preview (§3.1) — this is the process that creates the outcome.
```

### Step 3: Rename HL §11 and tighten instructions

In `.tfw/templates/HL.md`, replace §11.

**Before (lines 106-122):**
```markdown
## 11. Strategic Session Insights

> **Human-Only Test:** Would this insight be unknown without the user saying it?
> Watch for: corrections, emotions, domain knowledge, strategic decisions, business context.
> Categories: conventions.md §10.1.
>
> **High-value signals to watch for:**
> - User corrects direction or reframes the problem
> - User expresses emotion (frustration, excitement, urgency)
> - User shares domain knowledge not in any artifact
> - User makes strategic decisions between alternatives
> - User reveals business context, stakeholder priorities, or constraints

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | {insight} | {category — see §10.1} | User, {context} |
```

**After:**
```markdown
## 11. Strategic Insights (Planning)

> **Cognitive mode:** Deep analytical synthesis. Capture human-sourced domain knowledge,
> then ADD implications — what does this insight mean for the project's direction?
>
> **Human-Only Test:** Would this insight be unknown without the user saying it?
> If an agent can discover it by reading code — it's NOT a strategic insight, it's a Fact Candidate (§6).
>
> **High-value signals to watch for:**
> - User corrects direction or reframes the problem
> - User expresses emotion (frustration, excitement, urgency)
> - User shares domain knowledge not in any artifact
> - User makes strategic decisions between alternatives
> - User reveals business context, stakeholder priorities, or constraints
>
> **Categories:** conventions.md §10.1.

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | {insight} | {category — see §10.1} | User, {context} |
```

### Step 4: Sharpen RF §6 and add §7 + Diagrams section

In `.tfw/templates/RF.md`, make three changes:

**4a.** Sharpen §6 Fact Candidates instructions. Replace the instruction block (lines 52-61):

**Before:**
```markdown
> **Before writing Fact Candidates, review the conversation history.** The human's
> messages are the primary source of strategic knowledge — domain insights, stakeholder
> priorities, business context, and constraints that shape decisions.
>
> Good: "18% clients = 80% revenue (Pareto)", "stakeholder: find problem clients first"
> NOT fact candidates: "project uses git", "code is in Python", implementation details (→ §5 Observations → tfw-docs)
>
> **Human-Only Test**: would this fact be unknown without the human saying it?
> If an agent can discover it by reading code or running commands — it's not a fact candidate.
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.
```

**After:**
```markdown
> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Scope:** Agent-observed project patterns discovered during execution.
> Good: "18% clients = 80% revenue (Pareto)", "stakeholder: find problem clients first"
> NOT fact candidates: "project uses git", implementation details (→ §5 Observations → tfw-docs),
> or agent-generated analysis (→ §7 Strategic Insights).
>
> **Human-Only Test**: would this fact be unknown without the human saying it?
> If an agent can discover it by reading code or running commands — it's not a fact candidate.
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.
>
> **Before writing:** review the conversation history. The human's messages are the primary source.
```

**4b.** Add §7 "Strategic Insights (Execution)" after §6 (after line 69). Insert before the footer `---`:

```markdown
## 7. Strategic Insights (Execution)

> **Cognitive mode:** Deep analytical synthesis. Capture human-sourced domain knowledge
> observed during execution, then ADD implications — what does this insight mean for the project?
>
> **Human-Only Test:** Would this insight be unknown without the user saying it?
> If an agent can discover it by reading code — it's NOT a strategic insight, it's a Fact Candidate (§6).
>
> **When to fill:** Only when the human provides domain knowledge, corrections, or strategic
> context DURING execution. If no human interaction occurred — write "No strategic insights."
>
> **Categories:** conventions.md §10.1.

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | {insight} | {category — see §10.1} | User, {context} |

> **Source format**: Use reference patterns (e.g., `RF TFW-18`, `D24`). See compilable_contract.md §2.
```

**4c.** Add "Diagrams" section after §7 (before footer `---`):

```markdown
## 8. Diagrams

> **Cognitive mode:** Technical engineering documentation.
> Visualize architecture, data flow, component interaction, or sequence diagrams
> for the work completed in this phase.
>
> Formats: ASCII, mermaid, or structured tables.
> Focus: HOW the system is built — components, layers, protocols, data flow.
>
> If no diagrams are relevant — write "No diagrams."
```

### Step 5: Add Strategic Insights (Research) and Findings Map to RES template

In `.tfw/templates/RES.md`, make three changes:

**5a.** Sharpen Fact Candidates section. Replace instruction block (lines 38-46):

**Before:**
```markdown
> **Before writing Fact Candidates, review the conversation history.** The human's
> messages are the primary source of strategic knowledge — domain insights, stakeholder
> priorities, business context, and constraints that shape decisions.
>
> Record strategic facts about THIS project — not findings about alternatives,
> not implementation details (those belong in tfw-docs).
>
> **Human-Only Test**: would this fact be unknown without the human saying it?
> If an agent can discover it by reading code or running commands — it's not a fact candidate.
```

**After:**
```markdown
> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Scope:** Agent-observed project patterns discovered during research.
> Record facts about THIS project — not findings about alternatives,
> not implementation details (those belong in tfw-docs).
>
> **Human-Only Test**: would this fact be unknown without the human saying it?
> If an agent can discover it by reading code or running commands — it's not a fact candidate.
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.
>
> **Before writing:** review the conversation history. The human's messages are the primary source.
```

**5b.** Add "Strategic Insights (Research)" section after Fact Candidates (after line 51), before Conclusion:

```markdown
## Strategic Insights (Research)

> **Cognitive mode:** Deep analytical synthesis. Capture human-sourced domain knowledge
> observed during research briefings, then ADD implications — what does this insight
> mean for the project's direction?
>
> **Human-Only Test:** Would this insight be unknown without the user saying it?
> If an agent can discover it by reading code — it's NOT a strategic insight, it's a Fact Candidate.
>
> **When to fill:** Only when the human provides domain knowledge, corrections, or strategic
> context in research briefings. If no human interaction occurred — write "No strategic insights."
>
> **Categories:** conventions.md §10.1.

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | {category} | {insight} | User, {context} | ★★★/★★☆/★☆☆ |
```

**5c.** Add "Findings Map" section after Strategic Insights, before Conclusion:

```markdown
## Findings Map

> **Cognitive mode:** Analytical research visualization.
> Visualize research findings: root cause analysis, hypothesis trees, priority matrices,
> relationship maps between discoveries.
>
> Formats: ASCII, mermaid, or structured tables.
> Focus: WHAT was discovered and WHY — pattern relationships, causal chains, decision trees.
>
> If no visualization is relevant — write "No findings map."
```

### Step 6: Sharpen REVIEW §5 Fact Candidates

In `.tfw/templates/REVIEW.md`, replace §5 instruction block (lines 56-65):

**Before:**
```markdown
> **Before writing Fact Candidates, review the conversation history.** The human's
> messages are the primary source of strategic knowledge — domain insights, stakeholder
> priorities, business context, and constraints that shape decisions.
>
> Good: "18% clients = 80% revenue (Pareto)", "stakeholder: find problem clients first"
> NOT fact candidates: "project uses git", "code is in Python", implementation details (→ §5 Observations → tfw-docs)
>
> **Human-Only Test**: would this fact be unknown without the human saying it?
> If an agent can discover it by reading code or running commands — it's not a fact candidate.
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.
```

**After:**
```markdown
> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Scope:** Reviewer-observed project patterns discovered during the review process.
> Good: "18% clients = 80% revenue (Pareto)", "stakeholder: find problem clients first"
> NOT fact candidates: "project uses git", implementation details (→ Observations → tfw-docs),
> or reviewer analysis/opinions (those belong in §2 Verdict rationale).
>
> **Human-Only Test**: would this fact be unknown without the human saying it?
> If an agent can discover it by reading code or running commands — it's not a fact candidate.
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.
>
> **Before writing:** review the conversation history. The human's messages are the primary source.
```

### Step 7: Add Visual Sections cross-reference to conventions.md

In `.tfw/conventions.md`, add a new subsection after §3 "Fact Candidates" (after line 76), before §4 "Task Numbering":

```markdown
### Visual Sections (per-template)

> **Decision criterion:** "Does the cognitive mode CHANGE between templates?" If yes → per-template naming. If no → unified.
> Visual sections trigger different cognitive modes per template context (empirically validated: RES3 D22, RES4 Exp1+Exp2).

| Template | Section | Cognitive Mode | What it produces |
|----------|---------|---------------|-----------------|
| HL | §3.1 Result Visualization | Narrative / Outcome | Outcome preview — Working Backwards style ("imagine it's done") |
| HL | §3.2 Value Flow | Strategic / Value-oriented | Value streams, INPUT→PROCESSING→OUTCOME, transformation tables |
| RF | §8 Diagrams | Technical / Engineering | Architecture, ERD, sequence diagrams, component diagrams |
| RES | Findings Map | Analytical / Research | Root cause analysis, hypothesis trees, priority matrices |
| REVIEW | — | — | No visual section (checklist artifact, not result) |

### Knowledge Capture Sections (unified naming)

| Section | Name | Templates | Cognitive Mode |
|---------|------|-----------|---------------|
| §6 | Fact Candidates | RF, RES, REVIEW | Pure reporting: record without interpretation |
| §7/§11 | Strategic Insights + qualifier | HL (Planning), RF (Execution), RES (Research) | Deep analytical synthesis: capture + add implications |
```

Also update the Fact Candidates definition in §3 (line 74-75):

**Before:**
```markdown
### Fact Candidates (section in RF, REVIEW, RES)
Raw observations about the project recorded during work. NOT verified facts — they become facts after `/tfw-knowledge` consolidation. Each artifact has a Fact Candidates section with a structured table (Category, Candidate, Source, Confidence). Quality filter: "Would the next agent decide differently knowing this?"
```

**After:**
```markdown
### Fact Candidates (section in RF, REVIEW, RES)
Raw observations about the project recorded during work. Cognitive mode: pure reporting — record factual without interpretation. NOT verified facts — they become facts after `/tfw-knowledge` consolidation. Each artifact has a Fact Candidates section with a structured table (Category, Candidate, Source, Confidence). Quality filter: "Would the next agent decide differently knowing this?"
```

### Step 8: Update glossary.md

In `.tfw/glossary.md`, make three changes:

**8a.** Update "Strategic Insight" definition (line 47-48):

**Before:**
```markdown
### Strategic Insight
A fact or decision captured during a Coordinator planning session (HL §11). Represents domain knowledge, stakeholder priorities, business context, or architectural vision that only the human stakeholder can provide. High-value signals: user corrections, emotional statements, vision framing, alternative selection.
```

**After:**
```markdown
### Strategic Insight
Human-sourced domain knowledge captured with deep analytical synthesis. Appears in three contexts with qualifiers: HL §11 "Strategic Insights (Planning)", RF §7 "Strategic Insights (Execution)", RES "Strategic Insights (Research)". The agent's cognitive mode: capture the insight, then ADD implications — what does it mean for the project? High-value signals: user corrections, emotional statements, vision framing, alternative selection. Contrast with Fact Candidate (pure reporting, no interpretation).
```

**8b.** Add new terms after "Strategic Insight" (after line 48):

```markdown
### Value Flow
Visual section in HL template (§3.2). Visualizes HOW value gets created — the process from user pain through pipeline steps to value delivered. Cognitive mode: strategic/value-oriented (INPUT→PROCESSING→OUTCOME). Distinct from §3.1 Result Visualization (outcome preview). → conventions.md §3 Visual Sections

### Findings Map
Visual section in RES template. Visualizes research findings: root cause analysis, hypothesis trees, priority matrices, relationship maps between discoveries. Cognitive mode: analytical/research. → conventions.md §3 Visual Sections

### Per-template Naming
Design principle: when a section's cognitive mode differs across templates, use a different section name per template. When the mode is the same — use a unified name. Applied to: visual sections (per-template: Value Flow, Diagrams, Findings Map) vs knowledge capture sections (unified: Fact Candidates, Strategic Insights). Decision criterion: "Does the cognitive mode CHANGE between templates?" → conventions.md §3 Visual Sections
```

## 5. Acceptance Criteria

- [ ] HL §11 heading reads "Strategic Insights (Planning)" — not "Strategic Session Insights"
- [ ] HL §11 instructions include "Cognitive mode: Deep analytical synthesis" and cross-reference to §6
- [ ] HL §3.1 instructions include "Working Backwards" framing and "This is NOT a process diagram" note
- [ ] HL has §3.2 "Value Flow" with strategic visualization instructions
- [ ] RF has §7 "Strategic Insights (Execution)" with Human-Only Test and "No strategic insights" fallback
- [ ] RF has §8 "Diagrams" with technical visualization instructions
- [ ] RF §6 instructions include "Cognitive mode: Pure reporting" and explicit out-of-scope list
- [ ] RES has "Strategic Insights (Research)" section with Human-Only Test
- [ ] RES has "Findings Map" section with analytical visualization instructions
- [ ] RES Fact Candidates instructions sharpened to match RF level (cognitive mode + scope + before-writing note)
- [ ] REVIEW §5 instructions include "Cognitive mode: Pure reporting" and reviewer-specific scope
- [ ] conventions.md has "Visual Sections (per-template)" table with all 5 template rows
- [ ] conventions.md has "Knowledge Capture Sections (unified naming)" table
- [ ] conventions.md "Fact Candidates" definition includes "Cognitive mode: pure reporting"
- [ ] glossary.md "Strategic Insight" definition updated with qualifiers and contrast to Fact Candidate
- [ ] glossary.md has "Value Flow", "Findings Map", "Per-template Naming" entries

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Per-template visual names confuse agents | conventions.md cross-reference table (Step 7) + per-template instructions in each template |
| §7 in RF bloats executor output when no human interaction | Instructions include "No strategic insights" fallback (Step 4b) |
| §3.2 Value Flow confused with §3.1 | Both sections have explicit "This is NOT..." cross-reference (Steps 1, 2) |
| Sharpened §6 instructions too restrictive | Instructions keep existing good examples + add "Before writing: review conversation history" (Steps 4a, 5a, 6) |

> **Cross-references**: RES3 D15, D16, D17, D20. RES4 D21, D22, D24, D25, D26. HL-TFW-32 §4 Phase B. HL Phase B §4.

---

*TS — TFW-32 / Phase B: Naming & Templates | 2026-04-10*
