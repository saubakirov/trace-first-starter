# Challenge — "What do we NOT expect?"
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Goal: Fix TFW's pipeline gaps and clarify positioning for non-engineer audience.

## Findings

### C1: Stress-test H1 fix — stripping §1/§2 from tfw-knowledge Phase 4

**Concern:** If tfw-knowledge stops updating §1 Architecture Decisions and §2 Key Artifacts, will data be lost?

**Analysis:**
- tfw-docs checklist item #2: "New decision (D-record)? → KNOWLEDGE.md Architecture Decisions" — ✅ covered
- tfw-docs checklist item #1: "Architecture changed? → KNOWLEDGE.md Architecture Map" — ✅ covered
- tfw-docs runs AFTER every REVIEW (auto trigger). So every significant task will get §1/§2 updates from tfw-docs
- tfw-knowledge runs conditionally (Knowledge Gate or manual). It's NOT guaranteed to run after every task

**Verdict:** No data loss. tfw-docs is the more reliable writer for §1/§2 because it always runs. tfw-knowledge was writing to §1/§2 as a redundant "just in case" — that's exactly what creates "already captured."

**But:** One edge case. If tfw-knowledge runs BEFORE tfw-docs (user starts with `/tfw-knowledge` first), the knowledge workflow would skip §1/§2 entirely, then tfw-docs catches them. This is correct behavior — each does its own job. No gap.

### C2: Challenge "Doc Candidates" + "Knowledge Candidates" naming

User proposed renaming FC/SI → "Doc Candidates" / "Knowledge Candidates" to match workflows.

**Analysis against D28 (Naming Creates Behavior):**

| Name | Agent behavior it triggers |
|------|---------------------------|
| "Fact Candidates" (current) | Agent captures observations about anything — mixed bag |
| "Doc Candidates" | Agent captures things about the project's internal structure → feeds tfw-docs |
| "Knowledge Candidates" | Agent captures things only humans know → feeds tfw-knowledge |

**This is actually a strong improvement.** The name immediately tells the agent WHERE the observation goes. Current "Fact Candidates" is vague — agent doesn't know if what it captured is a documentation update or a knowledge insight. With the split:
- Executor writes Doc Candidates (§6a) — things about architecture, patterns, tech debt
- Executor writes Knowledge Candidates (§6b) — things humans said, stakeholder context, domain rules
- Coordinator writes Knowledge Candidates (§11) — strategic signals from planning sessions

**Counter-argument:** Does this increase cognitive load on the agent? It now must classify each observation as "doc" or "knowledge" at capture time.

**Response:** The classification heuristic is simple: "Can the next agent discover this by reading the codebase? YES → Doc Candidate. NO → Knowledge Candidate." This IS the Human-Only Test already in tfw-knowledge — just applied at capture time instead of consolidation time. Early classification = better signal quality.

**Risk:** Agent classifies wrong. Mitigation: both types go through consolidation workflows that have their own filters. Misclassified doc in knowledge section → tfw-knowledge rejects it (fails Human-Only Test). Misclassified knowledge in doc section → tfw-docs skips it (not actionable for documentation). Self-correcting.

### C3: Challenge KNW status — does it slow down simple tasks?

**Current flow for simple tasks:**
```
... → 🔍 REV (reviewer: "APPROVE, tfw-docs: N/A") → ✅ DONE
```

**Proposed flow:**
```
... → 🔍 REV (reviewer: "APPROVE") → 📚 KNW (tfw-docs: N/A, tfw-knowledge: N/A) → ✅ DONE
```

**Challenge:** For trivial tasks (config change, typo fix), is 📚 KNW just ceremony?

**Analysis:**
- The Triage Gate in tfw-docs already handles this: "Was this a significant task? NO → write `tfw-docs: N/A (minor)`"
- If both markers are N/A, and reviewer already set them during REVIEW, then KNW → DONE is instant (zero work)
- The reviewer can pre-set both markers during their REVIEW: `tfw-docs: N/A (minor)`, `tfw-knowledge: N/A` → status goes directly `🔍 REV → ✅ DONE`

**Revised design:** KNW status is implicit when REVIEW doesn't close both markers. flow:
- Small task: Reviewer writes APPROVE + both N/A markers → status = ✅ DONE (KNW skipped)
- Significant task: Reviewer writes APPROVE + `tfw-docs: pending` → status = 📚 KNW until both resolved

**This means 📚 KNW only appears on Task Board for significant tasks.** Trivial tasks go straight to DONE. No ceremony added.

### C4: Challenge competitive positioning — does anyone else claim "team knowledge tool"?

**Confluence:**
- Claims: "institutional backbone", structured spaces, Jira integration
- **Gap vs TFW:** Confluence stores documentation but doesn't generate it from work process. There's no lifecycle (HL→TS→RF→REVIEW) that automatically produces knowledge artifacts. Teams must manually write wiki pages. Adoption fails because "tool is so difficult that teams stop documenting."

**Notion:**
- Claims: "connected workspace", flexibility, all-in-one
- **Gap vs TFW:** Notion provides structure but no methodology. No Role Lock (anyone edits anything). No quality gates (REVIEW). No knowledge pipeline. Teams create beautiful databases that gradually go stale because there's no process forcing updates.

**Neither claims "AI agents as team members."** This is TFW's genuine differentiator:
1. AI agents don't just read docs — they PRODUCE the knowledge artifacts (RF, REVIEW, Observations)
2. Knowledge capture is a BYPRODUCT of work, not a separate documentation effort
3. The methodology enforces capture (Role Lock: executor MUST write Observations, reviewer MUST triage to TECH_DEBT)

**TFW's positioning statement:**

> Confluence and Notion store knowledge. TFW generates it. Every task produces observations, decisions, and insights — captured automatically by AI agents following a structured methodology. No separate documentation effort needed. Knowledge is a byproduct of work, not an afterthought.

### C5: Challenge multi-iteration — what if researcher ignores iterations.yaml?

**Scenario:** Researcher reads iterations.yaml but writes a full "final" RES claiming research is complete, ignoring `min_iterations: 3`.

**Mitigations:**
1. **Role Lock already handles this.** Researcher says "Research complete. Continue with `/tfw-plan`." Coordinator reads the RES, checks iterations.yaml, sees iteration 1 of 3 → launches next researcher.
2. **Filesystem state:** Each iteration RES is named `RES__iter{N}__{focus}.md`. Coordinator can see from filenames how many iterations ran.
3. **iterations.yaml is coordinator-owned.** Researcher updates `status: complete` for their iteration but CANNOT modify `min_iterations` or other iteration entries.
4. **Coordinator consolidation** happens after ALL iterations. Coordinator reads all per-iteration RES files and writes HL updates / decisions. No single researcher has authority over the full picture.

**Does this need enforcement in the workflow?** Not in this task. The design is sound — researcher always writes per-iteration RES, coordinator always consolidates. The enforcement is structural (naming convention + coordinator oversight), not rule-based.

### C6: Challenge H8 refinement — is "teams where knowledge loss costs money" too narrow?

**Test:** Who does this EXCLUDE?
- Solo founders → included (AI agents = their team, knowledge loss between sessions)
- Freelancers → included (client context must persist)
- Students/academics → partially excluded (no "money" framing, but "knowledge loss costs time" applies)
- Hobbyists → excluded (acceptable — TFW has real overhead)

**Risk of being too narrow:** Excludes educators (originally in HL target list).

**Revised framing:** "Teams and individuals who work with AI assistants and can't afford to lose context between sessions." Drop "costs money" — replace with "can't afford to lose."

**Final audience hierarchy:**
1. **Primary:** Product leaders, entrepreneurs, PMs managing AI-assisted teams
2. **Core:** Analysts, researchers, educators doing multi-session deep work
3. **Secondary:** Engineers who think beyond code (product-minded technical leads)

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H1 fix validated: no data loss from stripping Phase 4 | — |
| Doc Candidates / Knowledge Candidates naming is D28-aligned and self-correcting | — |
| KNW status: only shows for significant tasks. Trivial → reviewer pre-closes with N/A markers | — |
| TFW vs Confluence/Notion: "stores knowledge" vs "generates knowledge" | — |
| Multi-iteration: structurally sound, coordinator consolidation is the key | — |
| Audience: "can't afford to lose context" > "costs money" | — |

**Sufficiency:**
- [x] External source used? (Confluence/Notion competitive analysis)
- [x] Briefing gap closed? (all designs stress-tested)

**Deep mode criteria:**
- [x] Hypothesis tested? All 6 in-scope hypotheses challenged
- [x] Counter-evidence sought? Sought failure modes for each design: Phase 4 strip (data loss?), naming (cognitive load?), KNW (ceremony?), multi-iteration (researcher ignores?), audience (too narrow?)

**Metacognitive check:** New discovery = KNW status can be invisible for trivial tasks (reviewer pre-closes). Also: the "generates vs stores" competitive positioning is new and sharp. I didn't just confirm — I found a cleaner frame.

Stage complete: YES
→ User decision: ___
