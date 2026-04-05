# TS — TFW-26: Coordinator Fact Capture & Session Discipline

> **Date**: 2026-04-05
> **Author**: Lead Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-26](../HL-TFW-26__documentation_site.md) §11 S9, S10, S12

---

## 1. Objective

Formalize the Coordinator's responsibility to capture strategic insights from planning sessions. Currently, all roles except Coordinator have explicit fact capture mechanisms (RF §6, REVIEW §5, RES §FC). The Coordinator's main artifact (HL) has no Fact Candidates section. Strategic insights — user emotions, corrections, vision statements — survive only if tfw-knowledge happens to run in the same chat session.

This TS adds: (1) a Strategic Insights section to the HL template, (2) a mandatory step in plan.md for fact capture, and (3) guidance on recognizing high-value signals in user communication.

**This is a mini-task — no separate phase. Executes as part of TFW-26, deployable immediately.**

## 2. Scope

### In Scope
- Add Strategic Insights / Fact Candidates section to HL template
- Add fact capture step to plan.md (Step 4 or new step)
- Add fact capture guidance to resume.md (existing coordinators picking up work)
- Add glossary term: "Strategic Insight"

### Out of Scope
- Other template changes (RF, REVIEW, RES — already have FC sections)
- Knowledge consolidation workflow changes (tfw-knowledge handles FC processing)
- Any code or script changes

## 3. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/conventions.md` | MODIFY | Add `philosophy` to §10.1 Fact Categories |
| `.tfw/templates/HL.md` | MODIFY | Add §11 Strategic Session Insights template section |
| `.tfw/workflows/plan.md` | MODIFY | Add fact capture step after Step 4 (Write HL) |
| `.tfw/workflows/resume.md` | MODIFY | Add fact capture reminder in context loading |
| `.tfw/glossary.md` | MODIFY | Add "Strategic Insight" term |

**Budget:** 0 new files, 5 modifications. Within defaults: max 7 files, max 600 LOC.

## 4. Detailed Steps

### Step 1: Add `philosophy` to conventions.md §10.1 Fact Categories

In `.tfw/conventions.md` §10.1 table, add `philosophy` row:

```diff
 | `risk` | Known dangers | knowledge silos, fragile dependencies |
+| `philosophy` | Values, principles, vision | design rationale, methodology beliefs, north star decisions, "why we do it this way" |
```

> This category was missing despite being the most-used in practice (5/13 insights in TFW-26 = philosophy).

### Step 2: Add §11 to HL template

In `.tfw/templates/HL.md`, after §10 RESEARCH Case, add:

```markdown
## 11. Strategic Session Insights

> Coordinator captures strategic insights from planning sessions here.
> These transfer to RES/RF as Fact Candidates via tfw-knowledge.
>
> **High-value signals to watch for:**
> - User corrects direction or reframes the problem
> - User expresses emotion (frustration, excitement, urgency)
> - User shares domain knowledge not in any artifact
> - User makes strategic decisions between alternatives
> - User reveals business context, stakeholder priorities, or constraints
>
> **Human-Only Test:** Would this insight be unknown without the user saying it?
> **Categories:** Use conventions.md §10.1 Fact Categories.

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | {insight} | {category — see §10.1} | User, {context} |
```

### Step 3: Add fact capture step to plan.md

In `.tfw/workflows/plan.md`, after Step 4 (Write HL), before the GATE, add:

```markdown
### Step 4b: Capture Strategic Insights

During Steps 3-4, the user shares strategic insights — domain knowledge, corrections,
emotions, vision. These are the MOST VALUABLE facts in the project (see knowledge/process.md F2).

**Mandatory behavior:**
1. DURING conversation: note any user statement that passes the Human-Only Test
2. AFTER writing HL: review the full conversation history for missed insights
3. Write all captured insights to HL §11 (Strategic Session Insights table)
4. Each insight must have: Category (conventions.md §10.1), Source (who said it, when)

> ⚠️ Do NOT defer this to tfw-knowledge. The coordinator may be the ONLY agent
> in this chat session. If insights aren't captured in HL §11, they are lost.
```

### Step 4: Add fact capture reminder to resume.md

In `.tfw/workflows/resume.md`, in the context loading or orient phase, add a note:

```markdown
> **Fact capture reminder:** If resuming a Coordinator session, review the conversation
> history for strategic insights that may not have been captured in HL §11.
> The previous coordinator may have missed user emotions, corrections, or vision statements.
```

### Step 5: Add glossary term

In `.tfw/glossary.md`, add:

```markdown
### Strategic Insight
A fact or decision captured during a Coordinator planning session (HL §11). Represents domain knowledge, stakeholder priorities, business context, or architectural vision that only the human stakeholder can provide. Strategic Insights are the primary input for knowledge consolidation. High-value signals: user corrections, emotional statements, vision framing, alternative selection. Categories per conventions.md §10.1. Transfers to Fact Candidates via tfw-knowledge.
```

## 5. Acceptance Criteria

- [ ] conventions.md §10.1 has `philosophy` category in Fact Categories table
- [ ] HL template has §11 Strategic Session Insights with table, signals, and §10.1 reference
- [ ] plan.md has Step 4b with mandatory fact capture behavior
- [ ] resume.md has fact capture reminder for coordinator context loading
- [ ] glossary.md has "Strategic Insight" definition
- [ ] No hardcoded category lists — all templates reference §10.1
- [ ] No existing template sections are broken by the additions

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Coordinators ignore §11 because it's "optional" | Step 4b in plan.md makes it mandatory. Self-check in plan.md footer should reference it |
| §11 produces low-quality facts (too many, too trivial) | Human-Only Test and high-value signals guidance filter noise |
| Overlong HL if coordinator captures too many insights | Table format is compact. Real-world example (TFW-26 HL) has 13 insights = ~15 lines |

---

*TS — TFW-26: Coordinator Fact Capture & Session Discipline | 2026-04-05*
