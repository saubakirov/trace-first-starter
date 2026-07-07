# HL — TFW-44: Coordinator Quality Gates

> **Date**: 2026-05-04
> **Author**: Coordinator (Antigravity)
> **Status**: 📝 HL_DRAFT — Awaiting review

---

## 1. Vision

The HL→TS handoff now has structural guarantees: every user insight translates to a verifiable TS element, every critical requirement gets its own AC, and every constraint specifies a floor alongside its ceiling. The framework gains three universal gates that work across all domains — code, analytics, documentation, education — without domain-specific assumptions baked into the core.

**Impact:** Coordinators produce TS files that executors cannot misinterpret by omission. Insight loss at the HL→TS boundary drops from systematic to exceptional.

> "I said it once during planning, and it actually showed up in the result."

## 2. Current State (As-Is)

### Problem Origin

An Antigravity Knowledge Item (`coordinator_quality_gates.md`) was created from the KAZNU-21 Phase B post-mortem. It documents 5 loss patterns (LP1–LP5) and proposes 5 gates (A–E). This KI currently:
- Lives in the Antigravity knowledge base — invisible to TFW framework users on other tools
- Mixes universal insights (applicable to any TFW project) with domain-specific advice (pedagogical context, content budgets for lectures)
- Silently influences Antigravity sessions on this project without explicit framework backing

### Current HL §11 → Executor Path

| Step | Mechanism | Structural? |
|------|-----------|-------------|
| 1. User says something during planning | Coordinator captures in HL §11 | ✅ Template + plan.md Step 4 |
| 2. HL §7 Principles → TS §3 | Principles Check table | ✅ Structural enforcement |
| 3. HL §7.2 Citations → ONB §7 | Knowledge Citations cascade | ✅ Cascade with verification |
| 4. HL §11 Insights → TS AC | **No mechanism** | ❌ Gap |
| 5. Executor reads HL during ONB | Reads full HL (handoff.md Step 5) | ⚠️ Reads, but no confirmation |

**Gap:** §11 insights are captured but have no structural path to TS. They exist in a «dead zone» — recorded but not enforced.

### What the KI Contains (5 gates)

| Gate | Description | Universal? |
|------|-------------|-----------|
| A — Insight→AC traceability | Every HL §11 insight maps to a TS element | ✅ Yes |
| B — 1 Requirement = 1 AC | Explicit user requirement = separate AC, not list item | ✅ Yes |
| C — Content Budget | Pre-plan file splits for prose tasks | ⚠️ Partially — universal concept, educational calibration |
| D — Pedagogical Context | Audience, narrative, emotional outcome | ❌ Domain-specific |
| E — Floor AND Ceiling | Every DoF ceiling needs a floor | ✅ Yes |

## 3. Target State (To-Be)

### What changes:

1. **Framework (TFW)** gains 3 universal gates in `plan.md` (coordinator self-check before TS submission):
   - Gate A: Insight→AC traceability (HL §11 → TS)
   - Gate B: 1 explicit requirement = 1 AC (LLM anti-pattern)
   - Gate E: Floor AND Ceiling in DoF

2. **KI cleanup** — `coordinator_quality_gates.md` in Antigravity KI gets trimmed:
   - Gate C: marked as domain-specific (or generalized to "content scope budget" — needs research)
   - Gate D: marked as educational domain-specific
   - Universal gates A/B/E: referenced as "formalized in TFW conventions/plan.md"

### 3.1 Result Visualization

**Before (As-Is):**
```
plan.md footer:
  "Read conventions.md §14 (Anti-patterns). Did I violate any?
   Especially: TS without approved HL? Modified files outside scope?
   Skipped RESEARCH without presenting pros/cons? HL without §3.1, §10, or §11?
   Did I hand off to Researcher properly?"
```

**After (To-Be):**
```
plan.md Step 7 — Pre-TS submission self-check:
  ☐ Gate A (Insight Traceability): For each HL §11 insight — is there a TS element?
  ☐ Gate B (Requirement Isolation): Each explicit user requirement = own AC, not list item
  ☐ Gate E (DoF Completeness): Every ceiling constraint has a floor
  → Full anti-pattern list: conventions.md §14
```

**conventions.md §14 additions:**
```
- Coordinator bundles multiple user requirements in one AC → LLM executor drops tail items
- Coordinator sets DoF ceiling without floor → executor chooses minimum (e.g., 0%)
- Coordinator captures insight in HL §11 but doesn't trace to any TS element → insight dies
```

### 3.2 Value Flow

```
User insight during planning
  → HL §11 (Strategic Insights) — CAPTURED
    → plan.md Gate A — TRACED to TS element (new)
      → TS §5 AC / §6 Guidance / §7 DoF — ENFORCEABLE
        → Executor reads in ONB — APPLIED
          → RF — VERIFIED
```

## 4. Phases

Single-phase task.

### Phase A: Universal Gates 🔴

- Add 3 coordinator self-check gates to `plan.md` Step 7 (pre-TS submission)
- Add 3 anti-patterns to `conventions.md` §14
- Clean up Antigravity KI: mark domain-specific gates, update summary
- Update glossary with relevant terms (if needed)

## 5. Definition of Done (DoD)

- ✅ 1. `plan.md` Step 7 contains explicit self-check for Insight→AC traceability (Gate A)
- ✅ 2. `plan.md` Step 7 contains explicit self-check for 1 req = 1 AC (Gate B)
- ✅ 3. `plan.md` Step 7 contains explicit self-check for Floor+Ceiling in DoF (Gate E)
- ✅ 4. `conventions.md` §14 contains 3 new anti-patterns matching gates A, B, E
- ✅ 5. KI `coordinator_quality_gates.md` updated: domain-specific gates marked, universal gates cross-referenced to TFW framework

## 6. Definition of Failure (DoF)

- ❌ 1. Gates are domain-specific (mention "pedagogical", "lecture", "educational" in universal framework text)
- ❌ 2. Gates reference the KI as source of truth instead of being self-contained in TFW files
- ❌ 3. plan.md word count increases by >100 words (token budget — D23)
- ❌ 4. Gates are phrased as explanations instead of actionable checklist items

**On failure:** Rewrite gates as domain-agnostic, self-contained checklist items.

## 7. Principles

1. **Domain-agnostic by default** — F13: gates must work for code, analytics, documentation, education without mentioning any specific domain
2. **Token density** — D23: plan.md is already at attention budget limit. Gates = checklist, not prose
3. **Naming creates behavior** — F3: gate names should trigger the right coordinator check without explanation
4. **Structural enforcement > guidelines** — F4: gates are checklist items in a numbered step, not advisory text

### 7.2 Knowledge Citations

| # | Source | Item | How it applies |
|---|--------|------|----------------|
| 1 | KNOWLEDGE.md §1 | D23 — Workflow compression | plan.md budget: gates must be concise checklist items, not prose blocks |
| 2 | KNOWLEDGE.md §1 | D24 — Pattern A (inline + config key) | Gates live inline in plan.md, not behind indirection |
| 3 | KNOWLEDGE.md §1 | D49 — Requirements-first TS | AC structure already exists; gates enforce quality of AC creation |
| 4 | philosophy.md | F3 — Naming creates behavior | Gate naming = micro-prompts for coordinator |
| 5 | philosophy.md | F4 — Structural enforcement > format | Checklist gates vs advisory prose |
| 6 | philosophy.md | F13 — Domain-agnostic | No domain-specific language in universal gates |
| 7 | philosophy.md | F24 — Instructions produce compliance, heuristics produce competence | Gates should be heuristics ("scan §11"), not instructions ("for each insight, create...") |
| 8 | process.md | F4 — AI agents follow numbered steps + gates perfectly | Embedding gates as numbered checklist items = high compliance |
| 9 | process.md | F7 — Cross-session context loss | §11 insight loss = instance of this systemic problem |
| 10 | conventions.md §14 | Anti-patterns list | Adding 3 new anti-patterns to existing list |
| 11 | conventions.md §3 | HL §11 Strategic Insights definition | Source section for Gate A |

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| No external dependencies | ✅ |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| plan.md bloat beyond attention budget | Medium | High | Strict word limit (D23): checklist format only |
| Gates feel redundant with existing anti-patterns | Low | Medium | Review §14 for overlap before adding |
| KI cleanup affects active KazNU sessions | Low | Low | Mark educational gates, don't delete — sessions keep working |

## 10. RESEARCH Case

### Blind Spots

- Whether Gate C ("content budget") is genuinely educational-only or has a universal generalization (e.g., "scope budget for non-code deliverables")
- Whether the executor actually reads HL §11 in practice — anecdotal evidence from KazNU, no systematic data
- Whether adding a §11 confirmation step to ONB (like §7 for Citations) would be better than / complementary to Gate A

### Hypotheses

| # | Hypothesis | Status |
|---|----------|--------|
| H1 | Executor ignores HL §11 in practice because ONB has no §11 confirmation section — adding Gate A at coordinator level is necessary but not sufficient | open |
| H2 | Gate C generalizes beyond education: any task producing non-code deliverables needs a "deliverable scope budget" (file count/size estimate) in TS §4 | open |
| H3 | Gate B (1 req = 1 AC) is already implied by TS template's per-AC format — but coordinators bypass it by cramming multiple requirements into one AC's bullet list | open |

> **Filter:** Each hypothesis: "If proven false, would our approach change?"
> - H1 false → Gate A alone is sufficient, no ONB change needed → approach simplifies
> - H2 false → Gate C stays educational, no framework change → scope reduces
> - H3 false → Gate B is unnecessary → removes one gate

### Risks of Not Researching

- We add gates that duplicate existing enforcement (waste)
- We miss the ONB gap and think Gate A alone fixes the problem (insufficient)
- We over-generalize Gate C and add complexity that only matters for educational projects (bloat)

### Proposed RESEARCH Focus

1. **Gather**: Trace HL §11 through actual TFW tasks (TFW-38, TFW-41, TFW-43) — did executor use insights? Were they in TS?
2. **Extract**: Compare coordinator TS quality across tasks — pattern of bundled ACs? Missing floors?
3. **Challenge**: Test whether Gate A at coordinator level is sufficient or if executor-side confirmation (ONB §11) is also needed

### Why Not Just...?

- Why not just add all 5 KI gates to the framework? — Gates C/D are domain-specific. Adding them makes the framework assume all projects do educational content.
- Why not just fix the KI and skip framework changes? — KI is tool-specific (Antigravity only). Framework changes benefit all TFW users across all tools.
- Why not add an §11 section to ONB template instead? — Could be complementary, but the root cause is coordinator not converting insights to AC. ONB §11 would catch it downstream but not prevent it.

## 11. Strategic Insights (Planning)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | User suspects Antigravity KI silently improves TFW coordinator behavior — the framework works better than its files specify because KI injects extra checks. This means TFW on other tools (Claude Code, Cursor) would produce worse results. Universal gates formalize what KI does implicitly | philosophy | User, initial request |
| S2 | User's instinct: "executor should see insights anyway" — suggests the current HL reading step feels like it should be enough. The real question is whether reading = applying. Historical evidence (KAZNU-21) says no | process | User, Q1/Q2 response |
| S3 | User explicitly rejected educational gates for the framework: "это не так важно" for TFW core. Clear signal that domain-specific knowledge should stay in project-level KNOWLEDGE.md, not in framework files or cross-project KI | philosophy | User, response to Q3 |

---

*HL — TFW-44: Coordinator Quality Gates | 2026-05-04*
