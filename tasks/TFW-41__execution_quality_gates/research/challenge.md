# Challenge — "What do we NOT expect?"
> Parent: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> Goal: Structural gates at every TFW handoff point — prevent failures, not just detect them.

## Findings

### C1: When Does Requirements-First TS FAIL? (H1 Stress Test)

**Scenario 1: Novel implementation with no known pattern.**
Requirements say "WHAT" but the executor has never done anything similar. Without guidance (P1-V4 config), the executor makes bad architectural choices. Example: "Implement permissions cache with TTL" — executor builds Redis-backed solution when in-memory dict suffices (violating HL §7 P4 "No new abstractions").

**Verdict:** Requirements-first WITHOUT guidance fails for novel domains. The `§5. Technical Guidance` section (renamed from `§4. Detailed Steps`) is NOT "code" — it's context, patterns, constraints. The template must distinguish:
- §4 = Acceptance Criteria (WHAT, verifiable, gates)
- §5 = Technical Guidance (HOW context, patterns, NOT code — executor decides implementation)

**Scenario 2: CSS/visual tasks without visual spec.**
Requirements say "all hardcoded colors → CSS vars" but without a reference (concept.html), the executor doesn't know WHICH colors to use. Acceptance criteria `grep '#[0-9a-fA-F]{6}' = 0 matches` is necessary but insufficient — executor could replace with ugly vars that technically pass.

**Verdict:** Visual tasks need concept.html (F23) or screenshot reference IN ADDITION TO AC. The TS template should allow optional visual reference links in §5 for frontend-heavy phases.

**Scenario 3: Small/trivial tasks (<3 requirements).**
For tasks like "delete junk file + run linter" — full requirements-first TS is overhead. HD-18/D had 5 deliverables but each was 1-line mechanical change. A full AC+gate per item adds process without catching anything.

**Verdict:** Scope budget already handles this (F14: <50 LOC cosmetic fixes bypass TFW). No template change needed — the existing gate (`Hotfix-сессии обходят TFW gates`) covers trivial cases.

---

### C2: Execution Loops — The >3 Threshold (H3 Stress Test)

**Question:** Is >3 requirements the right threshold for mandatory Execution Loops?

**Test against evidence:**

| Case | # Requirements | Loops would have helped? |
|------|---------------|--------------------------|
| HD-16/C | 24 AC items | YES — per_page caught at R3, not at review |
| HD-18/C | 5 AC items | MAYBE — all passed anyway (requirements-first was sufficient) |
| HD-18/D | 6 AC items | NO — all mechanical, linear was fine |
| HD-9/A | 8 test items | YES — T7 resume was discovered during ONB, not at review |

**Pattern:** The threshold isn't about COUNT but about DEPENDENCY. HD-18/D had 6 items but they were independent (each file = separate fix). HD-16/C had items where R3 (per_page) depended on R1 (backend schema). HD-9/A had items where T7 (resume) depended on B1 (elapsed fix).

**Revised threshold:** Execution Loops are mandatory when **any requirement has a cross-file or cross-component dependency**. The executor must verify R_n gates before starting R_{n+1} when they share state. For independent requirements, linear execution is fine.

**Practical test:** At TS write time, coordinator marks each AC as `[independent]` or `[depends: AC-X]`. Dependent chains = mandatory loops. Independent items = linear.

---

### C3: Zwicky Box — Are 5 Enforcement Rules Sufficient? (H4 Stress Test)

**Testing each rule against HD-19 failure:**

| Rule | Would it have prevented HD-19 failure? | Over-constraining? |
|------|----------------------------------------|-------------------|
| R1: ≥3 values per parameter | ✅ YES — forces researcher to think beyond binary | No — 3 is minimum for genuine alternatives |
| R2: CCA pairwise table | ✅ YES — would have revealed D2×D3 dependency | Potentially — at 8 params × 4 values = 28 pairwise checks. Manageable? |
| R3: No "recommended" before CCA | ✅ YES — prevents confirmation bias | No — purely procedural |
| R4: ≥2 surviving configs | ✅ YES — prevents single-option validation | No — if only 1 survives CCA, that's genuine signal |
| R5: ≥1 non-obvious config | ⚠️ HARD TO ENFORCE — what is "non-obvious"? | YES — subjective. Reviewer can't verify "non-obvious" |

**R4 revision:** Change to "≥2 surviving configs OR explicit statement that CCA eliminated all but one, with the elimination log."

**R5 revision:** Replace with "document which configuration(s) you did NOT initially expect to survive CCA." This is verifiable — the researcher can state their pre-CCA expectation and compare.

**R2 concern at scale:** At 8 parameters with 4 values each, there are C(8,2)=28 parameter pairs, each needing up to 4×4=16 pairwise checks. That's 448 checks. Impractical.

**Fix:** CCA should be done at PARAMETER level (8 parameters → 28 pairs), not VALUE level. Question: "Are parameters P_i and P_j independent?" If not: "Which P_i values are inconsistent with which P_j values?" This reduces to 28 questions with selective deep-dives.

---

### C4: Pre-TS Gate — Overhead vs Value (H2 Edge Case)

**Scenario: Phase A (first phase, no RF N-1 to read).**
Pre-TS Gate says "read RF N-1 before writing TS." Phase A has no RF N-1. What does the coordinator read?

**Answer:** Phase A reads HL (already required) + RESEARCH artifact (if exists). Pre-TS Gate is N/A for Phase A — the gate applies only to Phase N where N > 1. This is already handled by the "Requires: Phase {N-1} ✅" field in the HL.

**Scenario: Multi-phase with parallel phases (B and C independent of each other, both depend on A).**
Coordinator writes TS-B and TS-C after RF-A. Both should read RF-A. No issue — Pre-TS Gate applies to the LATEST completed RF in the dependency chain, not to a linear N-1.

**Fix:** Pre-TS Gate wording: "Read the RF of the most recent completed phase in this task's dependency chain."

---

### C5: Template Enforcement — The Backward Compatibility Risk

**Current TS template has `§4. Detailed Steps`.** Changing it to `§4. Acceptance Criteria` + `§5. Technical Guidance` will break:

1. All existing tasks in all projects that reference "TS §4 Detailed Steps" in their ONB/REVIEW
2. Training data for coordinators who learned the current template
3. REVIEW workflow that says "check TS §5 Acceptance Criteria" → would need renumbering

**Mitigation:** This is a versioned change (TFW v3 → v4?). The TS template change should be accompanied by:
- VERSION bump
- Migration note in CHANGELOG
- Old §4→§5 numbering preserved in meaning (guidance section moves to §5)
- Existing projects don't need to update — only new TS files use the new template

---

### C6: When Enforcement Rules Become the Problem

**Risk:** The 5 Zwicky enforcement rules (E4-C in extract) could become bureaucratic overhead for research tasks where the solution space is genuinely simple (1-2 parameters, 2 values each).

**Test:** For a research question like "Should we use Redis or in-memory cache for permissions?" — Zwicky Box with 1 parameter and 2 values produces a 1×2 table. CCA is trivial. The rules mandate ≥3 values, forcing the researcher to invent a third option just to pass the gate.

**Fix:** Zwicky Box should be mandatory only when the research question has **≥3 independent parameters**. For 1-2 parameter decisions, a simple comparison table (pros/cons) is sufficient. The workflow should specify: "If ≥3 parameters → Morphological Box. If 1-2 parameters → comparison matrix."

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H1 FAILS when executor has no domain context → §5 Technical Guidance needed (but NOT code) | — |
| H3 threshold: not count-based but dependency-based. Loops mandatory for dependent AC chains | — |
| H4 R5 "non-obvious" is unverifiable → replace with "unexpected survivor" check | — |
| H4 CCA at scale: parameter-level, not value-level | — |
| Pre-TS Gate: N/A for Phase A, uses dependency chain not linear N-1 | — |
| Backward compatibility: version bump, no migration for existing projects | — |
| Zwicky Box: mandatory only for ≥3 parameters, comparison matrix for 1-2 | — |

**Sufficiency:**
- [x] External source used? (N/A for Challenge — this stage uses internal evidence to stress-test)
- [x] Briefing gap closed? All hypotheses stress-tested, edge cases mapped, thresholds refined

**Deep mode criteria:**
- [x] Counter-evidence actively sought? Yes: Requirements-first failure modes (C1), loop threshold revision (C2), Zwicky rule over-constraining (C3, C6)
- [x] Hypotheses revised based on challenge? H3 revised (count → dependency), H4 rules revised (R4, R5, scope threshold)

Stage complete: YES
→ Recommend: proceed to Synthesis. All hypotheses have verdicts. Challenge refined thresholds and fixed over-constraining rules. Ready to write final RES artifact.
