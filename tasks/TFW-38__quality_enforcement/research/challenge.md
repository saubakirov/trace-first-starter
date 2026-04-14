# Challenge — "What do we NOT expect?"
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: Stress-test H1/H2, find counter-evidence, identify risks of proposed changes.

## Findings

### C1: Counter-hypothesis — Maybe Agents DO Fill §6-8 When The Template Is Good Enough?

**Test:** If templates alone were sufficient, we'd expect consistent §6-8 presence across projects using the same template version. We'd also expect Findings Map presence to be uniform in RES files.

**Evidence against:**
- RF template has §6-8 with detailed blockquote instructions since TFW-32 (April 2026). Template quality is high — each section has a cognitive mode label, a Human-Only Test, usage guidance, and explicit "If nothing — write 'No X'" instructions.
- Despite this, 96-100% skip rate across 80+ RF files.
- RES template has Findings Map since TFW-32. Helpdesk (80% presence) vs steps-framework (15%) proves the template is not the differentiator — project age and recency of template adoption are.

**Verdict: Counter-hypothesis REJECTED.** Template presence is necessary but not sufficient. The workflow must explicitly enumerate the section.

### C2: Counter-hypothesis — Maybe The Audit Step Creates Unacceptable Overhead For Trivial Tasks?

**Test:** Look at the range of task types that go through review. Are there many trivial tasks where file-level auditing would be wasteful?

**Evidence from real REVIEW files:**
- TFW-32 Phase D REVIEW (positioning/messaging) — reviewer marked `Code quality: ✅`, `Test coverage: N/A`, `Security: N/A`. 4 of 9 checklist items were N/A. The reviewer noted: "Analytical phases produce deliverables that are structurally different from implementation phases — the 9-point checklist's code-centric items all evaluate to N/A."
- TFW-31 (scheduler AI chat) REVIEW — all 9 items substantive, line-by-line DoD verification. ~800 words of evidence.
- TFW-10 (version string sweep) REVIEW — `Test coverage: N/A (no code changed; grep audit substitutes for test suite)`.

**Analysis:** The range is wide — from deep code reviews to N/A-heavy analytical reviews. An audit step that says "open 2-3 files and verify RF claims" would be fine for code tasks but wasteful for docs/analytical tasks.

**Mitigation already in HL:** Risk R2 proposes a triage gate: "Is this a code task? If YES → audit. If docs/config only → skip audit." This is the correct pattern.

**Refined proposal:** The audit step should have a 1-line triage: "Code/implementation task → spot-check files. Analytical/docs task → verify deliverable existence." This prevents overhead while keeping the audit mindset.

**Verdict: PARTIALLY CONFIRMED.** Overhead risk exists for trivial/analytical tasks. Triage gate mitigates it. The HL already anticipates this.

### C3: External Validation — Industry Patterns for AI Reviewer Quality Gates (2025-2026)

**Key findings from web research:**

1. **Multi-stage quality gates are industry standard** — the 2026 consensus is that AI review should be broken into domain-specific gates (requirements validation, code quality, security), not a single monolithic pass. TFW's current 9-point checklist is monolithic. Adding an audit step is a move toward this multi-gate pattern.

2. **"Fix-guided Verification Filter"** — high-trust pipelines in 2026 use deterministic execution (run tests, verify files exist) for objective checks, reserving AI reasoning for subjective checks (architecture consistency). This maps exactly to H2: the reviewer should RE-RUN a build command or VERIFY file existence, not just read RF claims.

3. **Evidence-based trust over "vibe"** — the industry standard requires AI agents to cite evidence for their judgments. TFW's current REVIEW checklist has "Status" and "Notes" columns but doesn't enforce evidence. The TFW-36 REVIEW is the best example — it has line-by-line file citations (`L258-281`, `L72-76`). This behavior emerged organically, not from workflow enforcement.

4. **Immutable audit trails** — the TFW trace model (RF → REVIEW → TECH_DEBT) already provides this. The gap is that the REVIEW step doesn't require independent verification before writing the trail.

**Verdict: H2 SUPPORTED by external evidence.** Adding an audit verification step aligns with 2026 industry best practice. The triage gate for trivial tasks is also industry-aligned ("deterministic for objective, reasoning for subjective").

### C4: Edge Case — What If Adding §6-8 Makes the Handoff List Too Long?

Current handoff Phase 3 mandatory list: 6 items → proposed 9 items.

**Risk:** Apple RLCF research shows agents struggle with >10 constraints. Going from 6 to 9 keeps us under the threshold.

**Risk:** The 3 new items (§6, §7, §8) each have "If empty, write 'No X'" fallbacks. This means the agent MUST include the section header but can legitimately write one line. Zero content burden for tasks where they're not applicable.

**Verdict: LOW RISK.** 9 items is within the empirically validated constraint budget. Fallback lines prevent empty section anxiety.

### C5: Edge Case — Diagram Collection in docs.md Could Become a Maintenance Burden

**Question:** If docs.md collects mermaid diagrams from RF §8 and RES Findings Maps, where do they go? Who maintains them?

**Current state:** Zero diagrams collected anywhere. No `docs/diagrams/` folder exists in any project.

**Risk:** Collected diagrams become stale as architecture evolves. Nobody updates them because they're orphaned from the task context.

**Mitigation options:**
1. **Don't collect — just index.** Instead of copying diagrams to a central location, add references to KNOWLEDGE.md §2 (Key Artifacts): "Architecture diagram → RF Phase G §8, ERD → RF Phase C §8." The diagrams stay in the RF trace where they have full context.
2. **Collect only significant diagrams.** docs.md triage gate already asks "Was this significant?" — diagram collection follows the same gate.

**Verdict: MEDIUM RISK. Option 1 (index, don't copy) is safer** for iteration 1. Avoids creating stale diagram repositories. HL D6 should prefer indexing over copying.

### C6: Positive Pattern — TFW-31 Scheduler REVIEW as Quality Benchmark

The TFW-31 (auto-schedule) REVIEW from 2026-04-05 is an excellent quality example:
- 9/9 checklist with evidence
- Detailed DoD verification table (8 criteria, each with line-number evidence)
- 4 tech debt items triaged with severity and action
- 2 fact candidates with proper categories
- All within the 9-point checklist framework

**Key observation:** This reviewer produced quality WITHOUT an explicit audit step. The quality came from the reviewer model's personality + the detailed DoD in the TS. But this is not reproducible — other REVIEWs from the same project don't reach this level.

**Implication for H2:** The audit step doesn't create new capability — it makes existing capability RELIABLE. The best reviewers already do it; the audit step ensures ALL reviewers do it.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Template-only enforcement is proven insufficient (C1) | None |
| Audit overhead mitigated by triage gate (C2) | None |
| H2 supported by 2026 industry patterns (C3) | None |
| 9-item list is within constraint budget (C4) | None |
| Diagram collection should index, not copy (C5) | **HL update recommendation** |
| Audit step makes quality reliable, not new (C6) | None |

**Sufficiency:**
- [x] External source used? (Apple RLCF constraint limits, 2026 AI review gate patterns)
- [x] Briefing gap closed? (Counter-hypotheses tested, edge cases identified)

Stage complete: YES
→ User decision: ___
