# Extract — "What do we NOT see?"
> Parent: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> Goal: Structural gates at every TFW handoff point — prevent failures, not just detect them.

## Findings

### E1: Evidence Chain — TS Content Type → Execution Quality (H1)

**Controlled comparison (same project, same coordinator, same executor model):**

| Case | TS type | TS size | AC pass rate | Phase D needed? | Evidence |
|------|---------|---------|-------------|-----------------|----------|
| HD-16/C | Code-in-TS (§4 Detailed Steps) | 50KB / 1280 LOC | 23/24 (96%) | YES — palette, 89 colors | per_page=100 vs 500 |
| HD-18/C | Requirements-first (§4 Acceptance Criteria) | 11KB / 206 LOC | 100% | NO | All grep gates passed |

**Confounding variables controlled:**
- Same TFW version (conventions, templates)
- Same project codebase (Helpdesk)
- Executor model class: AI agent in both cases
- Coordinator: AI + PO involvement in both

**Causal mechanism:** HD-16/C executor had complete code to copy → copied without thinking → didn't verify per_page against backend cap. HD-18/C executor had requirements + grep gates → had to engineer solution → ran gates that would have caught the discrepancy.

**H1 verdict: SUPPORTED.** The evidence chain is strong — requirements-first TS at minimum eliminates the "copy without verifying" failure mode. The 79% size reduction is a secondary benefit (fewer tokens = more attention budget for actual engineering).

**Critical PO evidence:** `process.md F24` — "TS = требования + gates, НЕ код. TS с кодом → исполнитель копирует без мысли → форма есть, содержания нет." Source: PO feedback, 2026-04-19. The coordinator was **explicitly taught** this principle by the PO. Without F24, the coordinator would have continued writing code-in-TS.

**Implication for TFW-41:** Template enforcement is necessary. The coordinator learned F24 only through PO feedback after failure. Without structural enforcement in the TS template, future coordinators (new sessions, new projects) won't have F24 in their knowledge base.

---

### E2: Pre-TS Gate Analysis (H2)

**HD-18 coordinator self-assessment — 3 errors that reached ONB:**

| # | Error | Root cause | Would reading RF N-1 have prevented it? |
|---|-------|-----------|----------------------------------------|
| 1 | Wrong function signature (copied from other workers) | Read own TS plan, not actual code | ✅ YES — RF Phase B documents actual signatures |
| 2 | Wrong worker count (didn't count create_task calls) | Assumed count from HL plan | ✅ YES — RF Phase B §2 Key Decisions documents exact count |
| 3 | Referenced already-updated test | Read own TS Phase B, not RF Phase B | ✅ YES — RF Phase B lists which files were modified |

**H2 verdict: STRONGLY SUPPORTED.** All 3 errors have the same root cause: coordinator read own plan (TS N-1) instead of actual output (RF N-1). A Pre-TS Gate requiring `Read RF Phase {N-1} before writing TS Phase {N}` would have prevented all 3.

**Structural analysis:** The current plan.md workflow has no step that says "read RF of previous phase." It says "read HL" and "write TS" — the coordinator naturally reads their own plan because it's the most recent artifact they wrote.

---

### E3: Execution Loops Stress Test (H3)

**Would Execution Loops have caught HD-16/C per_page=100?**

Scenario reconstruction:
1. TS specified: `per_page: 500` in MonitorPage code
2. Executor copied code with `per_page: 500` literal
3. Backend `max_per_page=100` clamped the value
4. No gate checked actual runtime behavior

**If Execution Loops had been active (Gate per Requirement):**

Requirement would have been: "R3: per_page=500 — Monitor fetches all daily tickets"
Gate would have been: "API returns 500 items when 500 exist" or "No truncation warning"

**But:** The gate as written in the TS was a CODE specification (`per_page: 500`), not a BEHAVIORAL requirement. Even with Execution Loops, the executor would have verified "does my code say 500?" → yes → pass. The real gate should have been: "Does the API return the expected count?"

**H3 verdict: CONDITIONALLY SUPPORTED.** Execution Loops catch issues **only when gates test behavior, not code text.** The loop pattern requires Requirements-first TS (H1) to be effective. Without H1, loops verify copy accuracy, not functional correctness.

**Counter-evidence:** HD-18/C succeeded without explicit Execution Loops. The requirements-first pattern with grep gates was sufficient. This suggests Execution Loops add value primarily when:
- >3 requirements (more chances for drift between R_n and R_{n+1})
- Requirements involve runtime behavior, not just code structure
- Requirements have dependencies (R3 depends on R1's API change)

---

### E4: Zwicky Morphological Box — Meta-Test (H4)

#### H4-A: Diagnosing HD-19 Zwicky Box Failure

**HD-19 extract.md Section C — what went wrong:**

| Symptom | Root cause |
|---------|-----------|
| All 8 dimensions selected Alt 1 | No Cross-Consistency Assessment (CCA) performed |
| "Рекомендуется" annotation on first option | Pre-judged before systematic evaluation |
| No elimination of inconsistent combinations | CCA step skipped entirely |
| No new discovery | No parameter interaction analysis |

**The Zwicky Box was decorative.** The researcher already had recommendations from sections A and B, then built the box to confirm them. This is the OPPOSITE of GMA methodology — the box should GENERATE options, CCA should ELIMINATE options, and the result should INFORM (not confirm) the recommendation.

**Root cause:** The research workflow says nothing about HOW to do Extract. The template says `{content — patterns, comparisons, internal file analysis}` — completely open-ended. The researcher optimized for completion, not discovery.

#### H4-B: Applying Zwicky Box to TFW-41's Solution Space (Live Test)

**Step 1: Define parameters** (independent dimensions of the solution)

| # | Parameter | Description |
|---|-----------|-------------|
| P1 | TS content structure | How the TS template organizes what-to-do |
| P2 | Gate verification method | How gates are checked |
| P3 | Coordinator input verification | What the coordinator reads before writing TS |
| P4 | Executor self-check pattern | When/how executor verifies own work |
| P5 | Principle enforcement mechanism | How HL §7 principles survive into implementation |

**Step 2: Enumerate values per parameter**

| P | V1 | V2 | V3 | V4 |
|---|----|----|----|----|
| **P1** | §4 = Detailed Steps (current) | §4 = Requirements + §5 = Guidance | §4 = BDD/Gherkin scenarios | §4 = AC checklist only (no steps, no guidance) |
| **P2** | Manual reviewer check | Grep/CLI commands in TS | Automated test assertion | Screenshot/visual evidence |
| **P3** | Read HL only (current) | Read RF N-1 + HL | Read RF N-1 + HL + diff against TS N-1 | Read RF N-1 only (no HL re-read) |
| **P4** | Linear execution (current) | Gate per Requirement (Execution Loop) | Per-file verification | Post-execution self-review |
| **P5** | Text in HL §7 only (current) | HL §7 → TS AC mapping table | HL §7 → reviewer checklist item | HL §7 → automated gate |

**Step 3: Cross-Consistency Assessment (CCA)**

Pairwise elimination of inconsistent combinations:

| Pair | Inconsistency | Eliminated |
|------|--------------|------------|
| P1-V1 × P4-V2 | Detailed Steps + Execution Loops: loops verify code text, not behavior | ⚠️ weak — loops possible but low value |
| P1-V3 × P2-V2 | BDD scenarios + grep commands: different verification paradigms | ❌ inconsistent |
| P1-V4 × P2-V4 | AC-only + screenshots: no guidance → executor may screenshot wrong thing | ⚠️ weak |
| P2-V4 × P4-V2 | Screenshots + Execution Loops: screenshot per requirement = impractical overhead | ❌ for >5 requirements |
| P3-V4 × P5-V2 | RF-only (no HL) + HL§7 mapping: can't map principles if HL not read | ❌ inconsistent |
| P1-V1 × P5-V2 | Detailed Steps + principle mapping: mapping exists but executor copies code, ignoring mapping | ⚠️ weak — mapping wasted |

**Surviving viable configurations after CCA:**

| Config | P1 | P2 | P3 | P4 | P5 | Notes |
|--------|----|----|----|----|----|----|
| **C1** | V2 (Req+Guidance) | V2 (grep/CLI) | V2 (RF+HL) | V2 (Loops) | V2 (mapping table) | **Full enforcement** — all new mechanisms |
| **C2** | V2 (Req+Guidance) | V2 (grep/CLI) | V2 (RF+HL) | V1 (linear) | V2 (mapping table) | **Moderate** — no loops, requirements-first does heavy lifting |
| **C3** | V2 (Req+Guidance) | V3 (test assertion) | V2 (RF+HL) | V2 (Loops) | V3 (reviewer check) | **Test-heavy** — requires test infra, higher overhead |
| **C4** | V4 (AC only) | V2 (grep/CLI) | V2 (RF+HL) | V2 (Loops) | V2 (mapping) | **Minimal TS** — no guidance at all, executor fully autonomous |

**CCA eliminated:** 6 pairwise inconsistencies → reduced from 1024 (4^5) to 4 viable configurations.

**Observation:** C1 and C2 differ only in P4 (loops vs linear). H3 analysis shows loops are conditionally valuable. C3 requires test automation infrastructure. C4 gives zero guidance — risky for complex tasks.

**Recommendation:** C1 for phases with >3 requirements. C2 for simple phases (≤3 requirements). Both use Requirements+Guidance (P1-V2) and Pre-TS Gate (P3-V2).

#### H4-C: Diagnosing WHY the Box Was Decorative in HD-19

**The researcher's error was NOT in the box itself but in the process:**

1. **No genuine CCA.** The researcher annotated "рекомендуется" on values BEFORE doing pairwise elimination. The recommendation should come AFTER CCA, not before.

2. **Parameters weren't independent.** D2 (permission invalidation) depends on D3 (frontend store) — SSE requires Zustand, not Context. These should have been combined or the dependency made explicit.

3. **No new discovery.** A valid Zwicky Box should produce at least one viable configuration the researcher didn't initially consider. HD-19 produced zero — the "recommended" was already known from sections A and B.

**Fix for TFW research Extract workflow:**

The Zwicky Box step needs algorithmic enforcement:

1. **MUST enumerate ≥3 values per parameter** (prevent binary "yes/no" thinking)
2. **MUST perform CCA pairwise** (table of eliminated pairs with stated inconsistency)
3. **MUST NOT annotate "recommended" before CCA** (prevent confirmation bias)
4. **MUST produce ≥2 surviving configurations** (prevent single-option validation)
5. **MUST identify ≥1 non-obvious configuration** that wasn't in the initial hypothesis

---

### E5: Token Budget Analysis

**Current workflow word counts vs proposed additions:**

| Workflow | Current (words) | Proposed addition | New total | Budget (1200) |
|----------|----------------|-------------------|-----------|---------------|
| handoff.md | ~680 | Pre-RF Gate (~40w) + Execution Loops (~80w) + ONB answer protocol (~30w) | ~830 | ✅ Under |
| plan.md | ~795 | Pre-TS Gate (~50w) | ~845 | ✅ Under |
| review.md | ~600 | HL §7 principles check (~30w) | ~630 | ✅ Under |
| research/base.md | ~500 | Zwicky Box mandate in Extract (~60w) | ~560 | ✅ Under |

**All additions fit within the 1200-word design rule.** No workflow exceeds budget.

---

### E6: TFW Project Self-Evidence

**Does TFW itself exhibit the same problems?**

Checked TFW task artifacts. The TS template (`§4 Detailed Steps`) is the same template used in Helpdesk. TFW tasks (code-focused: TFW-26, TFW-27) also used code-in-TS patterns. The difference: TFW is a methodology project — its "code" is markdown templates and workflows, which are INHERENTLY requirements (they describe what the system should do). So TFW is partially immune to the code-in-TS problem because its code IS requirements.

**But:** TFW research iterations (TFW-22, TFW-24, TFW-32) show the same "first viable option" pattern in Extract stages — no morphological analysis, no systematic parameter enumeration. H4's problem exists in TFW's own research history.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H1 SUPPORTED: Requirements-first TS → better execution quality. Evidence: HD-16/C vs HD-18/C + PO's F24 | — |
| H2 STRONGLY SUPPORTED: Pre-TS Gate prevents plan≠fact drift. All 3 HD-18 errors preventable | — |
| H3 CONDITIONALLY SUPPORTED: Loops valuable for >3 requirements with behavioral gates | Need Challenge to stress-test the >3 threshold |
| H4: Zwicky Box viable BUT needs algorithmic enforcement (5 rules). HD-19 = decorative box. TFW-41 live test produced 4 configs from 1024 | Need Challenge to test if enforcement rules are sufficient |
| Token budgets: all additions fit within 1200-word limit | — |
| PO explicitly taught F24 — coordinator doesn't self-correct | — |

**Sufficiency:**
- [x] External source used? (Zwicky GMA methodology applied with proper CCA)
- [x] Briefing gap closed? (All 4 hypotheses analyzed with evidence)

**Deep mode criteria:**
- [x] Hypothesis tested? All 4 hypotheses tested with evidence and verdict
- [x] Counter-evidence sought? HD-18/C success without loops (→ conditional H3). HD-19 Zwicky failure (→ enforcement rules for H4).

**Metacognitive check:** The Zwicky Box meta-test produced genuine discovery — configuration C4 (AC-only, no guidance) is viable but risky, which I hadn't considered. The CCA also revealed that P1-V1 (current Detailed Steps) + P4-V2 (Execution Loops) is a WEAK combination — loops on code-in-TS verify copy accuracy, not functional correctness. This is a new insight.

Stage complete: YES
→ Recommend: proceed to Challenge. Key questions: (1) Is the >3 requirement threshold for Execution Loops correct? (2) Are the 5 Zwicky enforcement rules sufficient or over-constraining? (3) What's the failure mode of Requirements-first TS — when does it NOT work?
