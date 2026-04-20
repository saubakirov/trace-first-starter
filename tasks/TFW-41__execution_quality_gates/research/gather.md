# Gather — "What do we NOT know?"
> Parent: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> Goal: Structural gates at every TFW handoff point — prevent failures, not just detect them.

## Findings

### G1: HD-16 Phase C TS — Code-in-TS at Scale (50KB)

**File:** `helpdesk/tasks/HD-16__user_feedback_v12/PhaseC_ux/TS__PhaseC__monitor_columns.md`  
**Size:** 50,145 bytes, 1,280 lines. Contains 13 "Detailed Steps" with complete TypeScript/CSS code blocks.

**Evidence of copy-paste executor behavior:**
- Steps contain complete component implementations (MonitorLane.tsx: 95 lines of JSX, EventFeed.tsx: 140 lines of JSX, MonitorPage.tsx: 350+ lines full rewrite)
- CSS replacements specified line-by-line (13 individual color substitutions with exact before→after)
- Complete inline styles dictated, down to `padding: '4px 6px'` and `fontSize: '0.78rem'`

**Result (from REVIEW):** 23/24 AC met. But: `per_page=100` in code vs TS/RF specification of 500. **The executor copied the code from TS but didn't verify the functional requirement.** The reviewer caught it: "RF claims 500, TS specifies 500, code has 100. Discrepancy."

**Root cause:** The backend enforced `max_per_page=100` — a constraint NOT in the TS. The executor copied code that said `per_page: 500` but the runtime clamped it. No gate checked the actual runtime behavior.

### G2: HD-16 Phase D HL — The Gold Standard (Requirements-first)

**File:** `helpdesk/tasks/HD-16__user_feedback_v12/PhaseD_design/HL__PhaseD__design_system.md`

Phase D HL was written AFTER Phase C's failures. It demonstrates the pattern TFW-41 wants to formalize:

**Structure observed:**
- 8 Deliverables (D1-D8), each with:
  - **Requirement** (1-2 sentences, WHAT not HOW)
  - **Acceptance criteria** (checkbox list, verifiable)
  - **Gate** (concrete verification command: `grep`, screenshot, contrast check)
- §7 Definition of Failure (hard reject conditions with `❌` markers)

**Example (D1):**
```
Gate: grep -rn '#[0-9a-fA-F]{6}' StatusBadge.module.css = 0 matches
```

**Key insight:** Phase D HL organically evolved what TFW-41 proposes. This is empirical validation that the pattern works — it was invented in response to the failure it aims to prevent.

### G3: HD-18 TS Evolution — Coordinator Self-Correcting

**File:** `helpdesk/tasks/HD-18__security_performance_hardening/PhaseC/TS__PhaseC__resource_safety.md`

HD-18 Phase C TS already uses `§4. Acceptance Criteria` instead of the template's `§4. Detailed Steps`. Each AC (AC-C1 through AC-C5) has:
- **Requirements** (WHAT the component must do)
- **Hard gates** (grep commands to verify implementation)
- **Constraints** (what to NOT do)

**Size:** 10,865 bytes (vs HD-16/C's 50,145 bytes = 79% smaller for comparable scope).

**Result (from REVIEW):** "Все TS acceptance criteria выполнены." No Phase D needed.

**Evidence chain:** HD-16/C (50KB code-in-TS → failure → Phase D) → HD-18/C (11KB requirements-first → success). Same coordinator, same project, same executor model. The only variable was TS structure.

### G4: HD-9 ONB — Executor Finds TS Gaps

**File:** `helpdesk/tasks/HD-9__stability_tests_dense_table/PhaseA/ONB__PhaseA__backend_fixes_tests.md`

Executor found 2 blocking questions, 3 recommendations, 5 risks, 6 inconsistencies. All substantive.

**Evidence of Problem #2 (coordinator answers without sources):** Q1 received a concrete answer citing philosophy principles (#7, #12) with LOC threshold (<50 LOC). Q2 received a technical confirmation. Both had sources.

**But Problem #1 (RF drifts from template):** Not directly observable here. Need to check RF structure separately — deferred.

### G5: External — Requirements-Driven Specifications (ATDD/BDD)

**Source:** Industry literature on ATDD, BDD, and "Shift-Left Quality"

Key parallels to TFW-41:
- **"Living Documentation"** = executable specifications that serve as both requirements AND tests → analogous to TS Acceptance Criteria with hard gates
- **Shift-Left Quality** = defining acceptance/behavioral criteria BEFORE writing code → analogous to Requirements-first TS
- **ATDD** = collaborative definition of acceptance tests before coding → TFW-41's Gate concept
- **Requirements ≠ Implementation** = established software engineering principle. TS §4 Detailed Steps conflated both.

### G6: External — Zwicky's Morphological Box (GMA)

**Sources:** swemorph.com, wikipedia, nesslabs.com, GMA + AI research

**Core methodology:**
1. Define parameters (independent dimensions of problem)
2. List values per parameter (all possible options)
3. Construct n-dimensional matrix (the "box")
4. Cross-Consistency Assessment (CCA) — eliminate mutually exclusive combinations
5. Remaining cells = viable solution space

**AI applicability (verified externally):**
- LLM-augmented GMA: LLMs assist in decomposition and generation stages
- Agent architecture design: break complex agent into category variables, map morphospace
- "Totality research" — prevents premature narrowing

**For TFW research Extract:** Forces researcher to:
1. Identify independent parameters (not just pick first viable option)
2. Enumerate values per parameter (prevent blind spots)
3. Systematically eliminate inconsistent combinations (CCA)
4. Present remaining viable configurations to coordinator

**Potential issue:** Overhead for simple decisions. CCA requires pairwise comparison — at 4 params × 3 values = 81 combinations, but CCA reduces to manageable set.

### G7: External — Execution Loops (GenDD / Agentic Workflows)

**Sources:** hatchworks.com, shiplight.ai, medium.com

Industry term: **"Generative Driven Development (GenDD)"** — per-requirement verification embedded in execution loop, not post-hoc testing.

**Pattern:**
1. Define → Plan → Confirm → Execute → Validate (per requirement)
2. Quality gates = mandatory checks at every handoff, not end-of-sprint ceremonies
3. "Self-check pattern" = agent runs specific verification commands before declaring done

**Direct mapping to TFW-41:**
- GenDD's "per-requirement verification" = Execution Loops (Gate per Requirement)
- GenDD's "context packs" = TS §5 Technical Guidance
- GenDD's "fail-fast, converge-fast" = Gate catches error at R_n, not at review

### G8: HD-18 REVIEW — Coordinator Drift Evidence

**File:** `helpdesk/tasks/HD-18__security_performance_hardening/REVIEW__HD-18__PhaseC+D.md`

REVIEW shows 100% AC compliance for both Phase C and D. Reviewer found no plan≠fact drift. **But this is because Phase C already used requirements-first pattern.**

For plan≠fact drift evidence, need to look at HL §10 Hypotheses area, where the HL explicitly states: "Wrong function signature (copied from other workers, not verified), Wrong worker count (didn't count create_task calls), Referenced already-updated test (read own TS, not RF of previous phase)."

These 3 errors are documented in the HL itself, not in a separate artifact — they're from coordinator self-assessment. The coordinator admitted reading own plan instead of RF.

### G9: Helpdesk Knowledge Base — PO Explicitly Taught F24

**File:** `helpdesk/knowledge/process.md` line 36

```
F24: TS = требования + gates, НЕ код. TS с кодом → исполнитель копирует без мысли →
     форма есть, содержания нет.
     Source: PO feedback HD-16/D: «Меня не интересует код в ТС. Требования которые
     нельзя обойти»
```

**Also F25:** "Не дробить видение PO на фазы. Split B→C→D потерял chat-style комменты."
**Also F20:** "TS ОБЯЗАН содержать test requirements." (from HD-15/C post-mortem)

**Implication:** The coordinator did NOT self-correct. The PO explicitly injected F24 after HD-16/D failure. Without this knowledge entry, the coordinator would have continued writing code-in-TS. This proves template enforcement is necessary — knowledge entries are per-project, but template structure is framework-level.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| HD-16/C: 50KB code-in-TS → per_page failure (H1 evidence) | Need to quantify: how much token overhead do gates add? |
| HD-16/D: Gold standard for Requirements-first (organic evolution) | Need to verify H3: would Execution Loops have caught per_page? |
| HD-18/C: Requirements-first TS → 100% success (H1 control case) | H4 untested: Zwicky Box applicability to TFW research |
| HD-18 HL self-assessment: 3 coordinator errors from plan≠fact drift (H2) | H2: need structural analysis — what RF content would have prevented the errors? |
| ATDD/BDD alignment validates Requirements-first pattern | |
| Zwicky Box methodology understood — viable for Extract stage | |
| Execution Loops = established pattern (GenDD) | |

**Sufficiency:**
- [x] External source used? (5 external web searches: ATDD/BDD, Zwicky GMA, GMA+AI, Execution Loops, Quality Gates)
- [x] Briefing gap closed? (All 3 cited Helpdesk tasks analyzed. Zwicky Box methodology researched. Execution Loops validated externally.)

**Deep mode criteria:**
- [x] Hypothesis tested? H1 partially tested (HD-16/C vs HD-18/C evidence chain). H2 evidence gathered. H3/H4 need Extract/Challenge.
- [x] Counter-evidence sought? HD-18/C used requirements-first WITHOUT Execution Loops and still succeeded — counter to H3's necessity claim.

**Metacognitive check:** I discovered something NEW — HD-18/C TS already uses `§4. Acceptance Criteria` instead of `§4. Detailed Steps`. This organic evolution validates H1 but also shows the coordinator was self-correcting without enforcement. The question is: will this self-correction persist without structural enforcement?

Stage complete: YES
→ Recommend: close Gather, proceed to Extract. Key data points collected. Extract should build the Morphological Box and stress-test hypotheses.
