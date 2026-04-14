# HL — TFW-38: Quality Enforcement — Staged Review, Handoff Enforcement, Diagram Collection

> **Date**: 2026-04-14
> **Author**: Coordinator
> **Status**: 📝 HL_DRAFT — Updated with RESEARCH (4 iterations)

---

## 1. Vision

TFW workflow agents consistently produce complete artifacts — including diagrams, fact candidates, and strategic insights — and reviewers perform genuine quality audits via a structured 4-stage review process (Map → Verify → Judge → Decide) with domain-aware modes. Diagrams produced during tasks are indexed in KNOWLEDGE.md as living project documentation.

**Impact:** Every RF contains §6-8 because the workflow enforces it. Every REVIEW follows a staged flow with independent verification. Every diagram is indexed and discoverable.

> "The reviewer caught three claims in the RF that didn't match the actual code. The Judge stage forced them to evaluate quality against HL philosophy, not just check boxes."

## 2. Current State (As-Is)

### Observed problems (empirically validated — 4 research iterations across 4+ projects, 80+ RF files):

| # | Problem | Root Cause | Evidence |
|---|---------|------------|----------|
| P1 | Executor skips RF §6-8 (96-100% skip rate) | `handoff.md` Phase 3 doesn't enumerate §6-8 by name | RES1 F1: grep across 80+ RFs |
| P2 | Reviewer trusts RF claims without verification | `review.md` has no audit mandate, no spot-check instruction | RES1 F4: only TFW-19 has independent verification |
| P3 | Researcher skips Findings Map (~50% in newer, 0% in older projects) | `research/base.md` Step 6 omits Findings Map from enumeration | RES1 F5 |
| P4 | Diagrams abandoned after task closes | `docs.md` has no diagram collection mechanism | RES1 Q3: never attempted |
| P5 | REVIEW checklist is 44% code-specific — generates N/A noise on non-code tasks | Single checklist for all task types | RES2 F9: 4 of 9 items are N/A on docs/spec tasks |
| P6 | KNOWLEDGE.md read in 3 workflows but NEVER cited in output | No citation mandate in plan.md/handoff.md — cross-task knowledge stays siloed | RES4 F14: "read but don't use" pattern |

### Root cause (unified — RES1 D1):

Agents follow workflow step instructions literally. Template has the section → but workflow doesn't enumerate it → agent skips it. **Workflow wins over template in agent attention.**

## 3. Target State (To-Be)

### 3.1 Result Visualization

**Before → After:**

| Artifact | Before | After |
|----------|--------|-------|
| RF §6-8 | Skipped 96-100% | Always present — handoff.md explicitly requires each |
| REVIEW | Single-pass read → trust → checklist | 4-stage flow: Map → Verify → Judge → Decide |
| REVIEW checklist | 9 items, 44% code-only | Mode-aware: 6 universal + 2-4 mode-specific |
| RES Findings Map | Skipped ~50% | Always present — research/base.md explicitly requires |
| Diagrams lifecycle | Created → abandoned | Indexed in KNOWLEDGE.md §2 by docs.md |

**Sample 4-stage REVIEW flow:**
```
┌──────┐    ┌────────┐    ┌───────┐    ┌────────┐
│ MAP  │ →  │ VERIFY │ →  │ JUDGE │ →  │ DECIDE │
│"What │    │"Are    │    │"Is the│    │"What's │
│ was  │    │ claims │    │ quality│    │ the    │
│ done"│    │ true?" │    │ good?" │    │verdict"│
└──────┘    └────────┘    └───────┘    └────────┘
 Read RF     Open files    Checklist    Verdict +
 +TS+HL      Spot-check    (mode:       Tech Debt +
 Build       Re-run test   code/docs/   Fact Cands
 mental      Check AC      spec)        Traces
 model       evidence
```

### 3.2 Value Flow

```
EXECUTOR                REVIEWER                         DOCS
   │                       │                               │
handoff.md              review.md                       docs.md
Phase 3:                4-stage flow:                   Checklist #7:
§1-8 explicit           Map→Verify→Judge→Decide         Diagram index
   │                    + mode selection (code/docs/spec)    │
   ▼                       ▼                               ▼
RF with                 REVIEW with                    KNOWLEDGE.md §2
all sections            evidence-based verdict         Diagram Index
```

## 4. Phases

### Phase A: Review Restructure + Full Enforcement Chain 🔴

> **Requires:** Independent
>
> **Context for coordinator:**
> 1. `review.md` — full workflow
> 2. `REVIEW.md` template — full template
> 3. `handoff.md` — Phase 1 (onboarding) + Phase 3 (RF)
> 4. `research/base.md` — Step 6 (synthesis)
> 5. `plan.md` — Step 3 (knowledge citation)
> 6. `conventions.md` §3 Visual Sections + §14 Anti-patterns
> 7. RES D1, D6→D11, D7→D12, D8, D9, D14-D17
>
> **Key decisions:**
> - D1: explicit §6-8 mandate in handoff.md
> - D11: 4-stage review: Map → Verify → Judge → Decide
> - D12: 3 review modes: code / docs / spec
> - ~~D8: stages as REVIEW sections (not separate files)~~ → **superseded by D18**
> - D9: REVIEW template restructures to match stages
> - D14: knowledge citation mandate in plan.md Step 3
> - D15: KNOWLEDGE.md inconsistency check in handoff.md Phase 1
> - D16: diagram creation mandate in handoff.md Phase 3
> - D17: Findings Map mandate in research/base.md Step 6
>
> **Deliverables:**
> 1. `review.md` — restructured with 4 stages + mode selection (Step 0)
> 2. `REVIEW.md` template — new §1-§7 structure matching stages
> 3. `.tfw/workflows/review/code.md` — code-mode checklist + verify actions [NEW]
> 4. `.tfw/workflows/review/docs.md` — docs-mode checklist + verify actions [NEW]
> 5. `.tfw/workflows/review/spec.md` — spec-mode checklist + verify actions [NEW]
> 6. `handoff.md` — Phase 1: add KNOWLEDGE.md to inconsistency check; Phase 3: explicitly enumerate §6-§8
> 7. `research/base.md` — Step 6 explicitly requires Findings Map
> 8. `plan.md` — Step 3: add "Check KNOWLEDGE.md, cite relevant items in HL §4"
> 9. `conventions.md` §14 — new anti-patterns for review trust / section skipping / knowledge non-citation

### Phase A.2: Review Stage Files + Self-Check Gates 🔴

> **Requires:** Phase A ✅
>
> **Key decisions:**
> - D18: review stages as separate files (map.md, verify.md, judge.md) — supersedes D8. Without file fixation stages collapse into single stream of consciousness, same root cause as P1-P3.
>
> **Deliverables:**
> 1. `.tfw/templates/review/map.md` — Map stage template with self-check gate [NEW]
> 2. `.tfw/templates/review/verify.md` — Verify stage template with self-check gate [NEW]
> 3. `.tfw/templates/review/judge.md` — Judge stage template with self-check gate [NEW]
> 4. `review.md` — Steps 1-3 write stage files; Step 4 synthesizes into REVIEW
> 5. `REVIEW.md` template — references stage files; synthesis artifact
> 6. `conventions.md` §3 — review stage files in artifact taxonomy

### Phase B: Knowledge Citation Table 🔴

> **Requires:** Phase A.2 ✅
>
> **Context for coordinator:**
> 1. HL §7 P6 (Knowledge Gate) + S9 (cross-task knowledge as hard gate)
> 2. RES iter 4 D14-D15 (knowledge citation mandate)
> 3. `plan.md` Step 3, `handoff.md` Phase 1, `review/verify.md`, `review/judge.md`
> 4. `conventions.md` §3 Artifact Types
>
> **Key decisions:**
> - D19: Knowledge Citation Table — every role MUST leave a table of WHAT they read from KNOWLEDGE.md/conventions/knowledge/, WHERE it is (link), and HOW it applies. Reviewer verifies links are real (anti-hallucination gate). Silent "I checked" → traceable "I read [D28](link) and applied it to X."
>
> **Deliverables:**
> 1. `HL.md` template — new §4.1 Knowledge Citations table (Coordinator fills during planning)
> 2. `ONB.md` template — new §6.1 Knowledge Cross-Reference table (Executor fills during onboarding)
> 3. `review/verify.md` template — update KNOWLEDGE.md checkpoint to require citation table
> 4. `handoff.md` — Phase 1 instructions: fill citation table in ONB from KNOWLEDGE.md scan
> 5. `plan.md` — Step 3 instructions: fill citation table in HL from KNOWLEDGE.md scan
>
> **Diagram indexing** → moved to TFW-39 (Visual Knowledge System)

## 5. Definition of Done (DoD)

- ✅ 1. `review.md` restructured with 4 stages (Map → Verify → Judge → Decide) + mode selection
- ✅ 2. `REVIEW.md` template restructured to §1-§7 matching stages
- ✅ 3. 3 review mode files created (code.md, docs.md, spec.md) in `.tfw/workflows/review/`
- ✅ 4. `handoff.md` Phase 1 checks KNOWLEDGE.md inconsistencies; Phase 3 explicitly lists §6-§8
- ✅ 5. `research/base.md` Step 6 explicitly requires Findings Map
- ✅ 6. `plan.md` Step 3 requires citing relevant KNOWLEDGE.md items in HL §4
- ✅ 7. `docs.md` has diagram indexing mechanism
- ✅ 8. `conventions.md` §14 has new anti-patterns (review trust, §6-8 skip, knowledge non-citation)
- ✅ 9. `PROJECT_CONFIG.yaml` has `tfw.review.default_mode: code`
- ✅ 10. All changes fit within scope budgets (≤14 files, ≤1200 LOC per phase)

## 6. Definition of Failure (DoF)

- ❌ 1. review.md exceeds 1200 words (token density rule)
- ❌ 2. Mode files duplicate universal checklist items
- ❌ 3. Template-workflow disconnect recreated (sections exist in template but workflow doesn't reference them)

**On failure:** Compress. Mode files contain only differential items. Universal items inline in review.md.

## 7. Principles

1. **Workflow > Template** — Enforcement belongs in the workflow. Template = format spec.
2. **Map, Verify, Judge, Decide** — Reviewer follows explicit cognitive stages, not a single-pass read.
3. **Mode, not checklist** — Task type determines which checklist items apply (code/docs/spec).
4. **Index, don't copy** — Diagrams stay in RF/RES traces with full context; KNOWLEDGE.md indexes them.
5. **Naming Creates Behavior** — Stage/mode names must be self-explanatory: 1-2 syllables, active verbs/nouns.
6. **Knowledge Gate** — Every role MUST cross-reference KNOWLEDGE.md before producing output. Not a recommendation — a hard gate. Coordinator cites in HL §4 (D14). Executor checks inconsistencies in ONB (D15). Reviewer verifies contradictions in verify.md and judge.md (A.2). "No applicable knowledge items" = valid trace. Silent omission = process failure.

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| None | ✅ |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| review.md word count exceeds 1200 | Medium | High | Mode files hold differential items; keep main workflow lean |
| 3 new mode files = maintenance burden | Low | Medium | Mode files are small (~200 words each); parallel research modes |
| Reviewer mode selection adds friction | Low | Low | Default mode in PROJECT_CONFIG.yaml; auto-detect from TS context |

## 10. RESEARCH Case

### Hypotheses (RESEARCH complete — 4 iterations)

| # | Hypothesis | Status | Evidence |
|---|----------|--------|----------|
| H1 | Explicit §6-8 enumeration stops skipping | 🟢 confirmed | RES1: 96-100% skip rate, template alone insufficient |
| H2 | Audit step changes reviewer behavior | 🟢 → superseded by H3 | RES1: trust-chain failures confirmed |
| H3 | Structured review stages with modes produce more reliable reviews | 🟢 confirmed | RES2: ISO V&V mapping, mode eliminates N/A friction |
| H4 | "Naming Creates Behavior" — self-explanatory names eliminate comprehension friction | 🟢 confirmed | RES3: user tested — "comprehend"❌, "map"✅, "judge"✅ |
| H5 | Knowledge citation mandate closes the "read but don't use" gap | 🟢 confirmed | RES4: KNOWLEDGE.md in 3 context loads, 0 output citations |

### Parking Lot (out of scope — future tasks)

- **TS Template Conventions** — L1-L4 specification level guidance (RES3 D13). Coordinators write 49-71% code in TS files — missing guidance on when to use which level.

## 11. Strategic Insights (Planning)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | Agents treat workflows as WHAT, templates as HOW. Workflow wins. Enforcement MUST be in workflows. | philosophy | User + empirical evidence |
| S2 | Reviewer needs cognitive mode shift: from "summarize" to "verify." Structured stages enforce this. | philosophy | User, HD project |
| S3 | Diagrams have documentation value beyond task lifecycle. Index, don't copy. | process | User + RES D3/D10 |
| S4 | ONB demonstrates "verify spec vs reality" pattern. Reviewer should apply same to RF claims. | philosophy | User observation |
| S5 | TFW has two classes of workflows: investigative (staged — research, review) and procedural (linear — handoff, docs). Investigative workflows need cognitive mode transitions. | philosophy | RES1 SS1 |
| S6 | Review stages Map→Verify→Judge→Decide parallel research Briefing→Gather→Extract→Challenge but without OODA loops/WAIT gates. | philosophy | RES2 D6-D8 |
| S7 | Mode names describe output type (code/docs/spec), not domain (business/education). Output-type naming is finite and domain-agnostic. | convention | RES2 F8, RES3 D12 |
| S8 | The "explicit N/A" pattern ("No diagrams.", "No applicable knowledge items.") transforms silent skips into conscious traces. The trace enables reviewer challenge: RF §8 says "No diagrams" for a phase with a state machine → reviewer can flag it. Without explicit N/A, reviewer can't distinguish "forgot" from "decided." | philosophy | RES4 F16 |
| S9 | KNOWLEDGE.md cross-reference must be a GATE across all 4 roles, not a soft "check". Coordinator works in task silo without connecting to prior decisions (D14 root cause). Pattern: every role has a mandatory checkpoint where they read KNOWLEDGE.md and either cite relevant items or write "No applicable knowledge items." The gate is complete only when the citation or N/A is written in the output artifact. Coordinator→HL §4, Executor→ONB §6, Reviewer→verify.md checkpoint, Researcher→RES Fact Candidates. | philosophy | RES4 D14-D15, A.2 cross-check |

---

*HL — TFW-38: Quality Enforcement | 2026-04-14*
