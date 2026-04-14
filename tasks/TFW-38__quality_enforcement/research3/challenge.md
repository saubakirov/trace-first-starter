# Challenge — Iteration 3
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: Stress-test naming choices and TS over-spec conclusion.

## C1: "Map" as Stage 1 — Ambiguity Risk

**Problem:** "Map" has multiple meanings in tech:
- `map()` function (programming)
- "map" as cartography
- "map" as "build a mental model"

**Test:** In context, does it cause confusion?

Workflow would say: "**Step 1: Map** — Read RF, TS, HL. Build a mental model of what was done."

In this context, "map" clearly means "orient yourself." It's used as a verb ("map the territory"), not a data structure. The workflow text disambiguates.

**Comparison with rejected alternatives:**
- "Read" — too passive. Doesn't trigger "build understanding," triggers "scan text."
- "Orient" — from OODA. But alone, it's unclear ("orient what? orient where?"). OODA context isn't present in review.
- "Scan" — too shallow. Implies quick glance, not deep understanding.

**Verdict: "Map" holds.** The workflow context eliminates ambiguity. 1 syllable, active, memorable.

## C2: "Judge" — Risk of Negative Connotation?

**Concern:** "Judge" could feel punitive. A reviewer might think they're supposed to find fault, not evaluate quality objectively.

**Test:** What does "judge" trigger in the legal metaphor?
- A judge reviews evidence (Stage 2: Verify provided the evidence)
- A judge applies law/standards (Stage 3: checklist = the law)
- A judge decides verdict (Stage 4: Decide follows Judge)

The negative connotation ("don't judge me") is casual English. In a structured workflow, "judge" = "apply standards to evidence." This is exactly what the checklist does.

**Alternative "Evaluate":** 4 syllables, academic, vague. "Judge" is sharper.

**Verdict: "Judge" holds.** The legal metaphor chain (Map evidence → Verify claims → Judge quality → Decide verdict) is coherent.

## C3: "Decide" vs "Close" vs "Conclude" for Stage 4

**What happens in Stage 4:**
1. Write verdict (APPROVE / REVISE / REJECT)
2. Triage tech debt
3. Capture fact candidates
4. Update traces

This is more than just a "decision." It's decision + capture + cleanup.

| Name | Covers decision | Covers capture | Covers cleanup | Syllables |
|------|----------------|----------------|----------------|-----------|
| Decide | ✅ | ❌ implies just the call | ❌ | 2 |
| Close | ⚠️ implies finality | ⚠️ | ✅ | 1 |
| Conclude | ✅ | ⚠️ | ✅ | 2 |
| Deliver | ❌ wrong metaphor | ❌ | ❌ | 3 |

**"Decide" is strong enough.** The stage description says "Decide and capture." The verb covers the primary action (verdict). The rest (tech debt, facts, traces) are mechanical steps that don't need their own stage name — they're substeps of the decision.

**Verdict: "Decide" holds.** Primary action = verdict. Substeps don't need separate naming.

## C4: Mode Names — "docs" Collision Risk

**Concern:** Many projects have a `docs/` folder. Will `docs` mode collide with the folder meaning?

**Context:** Mode appears in:
- `PROJECT_CONFIG.yaml`: `tfw.review.default_mode: docs`
- Workflow text: "Select mode: code / docs / spec"
- Mode file path: `.tfw/workflows/review/docs.md`

**None of these contexts** reference the project's `docs/` folder. The mode name exists purely in TFW config and workflow space. No collision.

**Verdict: "docs" holds.** No practical namespace collision.

## C5: The Full Naming Chain — Does It Sound Right Together?

Complete review flow:

```
Reviewer selects mode: { code | docs | spec }
                ↓
Step 1: MAP    — "Read RF, TS, HL. Build mental model."
Step 2: VERIFY — "Open files. Spot-check claims."
Step 3: JUDGE  — "Apply checklist. Evaluate quality."
Step 4: DECIDE — "Write verdict. Capture tech debt and facts."
```

Reading the stages as a sentence: "Map the work, Verify the claims, Judge the quality, Decide the verdict."

**Does it flow?** Yes — short, active, escalating. Each stage has clear intent. No stage name needs explanation.

**Compare:** "Comprehend, Verify, Assess, Synthesize" — academic, 3-4 syllables, needs explanation.

**Verdict: The chain works.** Naming Creates Behavior: Map|Verify|Judge|Decide triggers the right cognitive mode at each stage.

## C6: TS Over-Spec — Is This Actually Just "Coordinator Can't Let Go"?

**Counter-hypothesis:** Maybe the coordinator writes full code because the TS template doesn't explicitly STOP them. The template says "code examples if relevant" — there's no constraint like "maximum 3 code snippets" or "code examples must be ≤30 LOC."

**Test:** Does the coordinator write full code for ALL tasks or only complex ones?

Evidence:
- HD PhaseF Steps 3-5 (analytics service): method signatures + formula, NOT full code
- Atamat PhaseF2 Step 3 (RouteStrip): pseudocode structure, NOT full code
- HD PhaseD Steps 1-5 (schemas, SLA, repository, service): FULL code

**Pattern:** When the domain is well-known to the coordinator (SLA algorithm from sla-engine.md, schemas from api-contracts.md), the coordinator writes full code. When it's UI/visual (RouteStrip), the coordinator writes structure. When it's a standard pattern (analytics repo), the coordinator writes signatures.

**Insight:** The coordinator writes L4 when they know the answer and wants to ensure correctness. This isn't pathological — it's risk-averse behavior for complex/critical code. The problem is only when L4 is applied to boilerplate.

**Verdict: Over-specification is a TENDENCY, not a mandate.** TS already varies between L2-L4 naturally. The issue is that there's no explicit guidance on WHEN to use which level. Adding a recommendation to the TS template conventions would solve this — but it's a separate task, not TFW-38.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| "Map" holds — workflow context eliminates ambiguity (C1) | None |
| "Judge" holds — legal metaphor is coherent (C2) | None |
| "Decide" holds — primary action is verdict (C3) | None |
| "docs" holds — no namespace collision (C4) | None |
| Full chain flows: Map → Verify → Judge → Decide (C5) | None |
| TS over-spec is tendency, not mandate. Separate task (C6) | Fact candidate for RES |

**Sufficiency:**
- [x] External source used? (TFW "Naming Creates Behavior" value as validation criterion)
- [x] Briefing gap closed? (All naming validated, TS finding scoped)

Stage complete: YES
→ User decision: ___
