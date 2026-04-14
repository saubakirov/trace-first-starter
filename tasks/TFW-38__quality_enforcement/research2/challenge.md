# Challenge — "What do we NOT expect?"
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: Stress-test staged review design, mode system, naming, and practical viability.

## Findings

### C1: Counter — "Stages within one file are just renamed sections, not real cognitive transitions"

**Argument:** Research stages work because each stage produces a separate file that the agent commits to before moving on. If review stages are just sections in one file, the agent might fill them all at once without the cognitive mode shift.

**Test:** Look at how the handoff.md ONB step works — it's a single file with distinct sections (Blocking Questions, Recommendations, Risks, Inconsistencies), and agents DO fill each section with different cognitive modes. The ONB file is proof that sections within one file CAN enforce cognitive transitions IF the workflow explicitly describes the mindset for each.

**Additional evidence:** The TFW-36 REVIEW has self-assessment (§2.4 "Reviewer Self-Assessment") — a cognitive transition that happened within a single REVIEW file. The agent shifted from "judge" to "self-reflect" within one document.

**Verdict: PARTIALLY VALID.** The risk is real but mitigated by:
1. The workflow describing each stage's mindset explicitly (like research stages do)
2. The Verify stage requiring ACTION (open file, run command) that physically forces a different mode
3. The REVIEW template having clear section boundaries

**Mitigation:** The review.md workflow Step 2 (Verify) MUST contain a concrete action list, not just a description. E.g., "Open 2-3 files from RF §1, verify changes exist. If RF claims tests pass — check test file."

### C2: Counter — "3 modes is overengineered. Most tasks are code tasks."

**Test:** Count task types across projects.

Evidence from existing REVIEW files:
- Helpdesk: 10 REVIEWs → 8 code tasks, 1 doc (Phase0), 1 scaffold (PhaseB) = 80% code
- Steps-framework: 15+ REVIEWs → ~6 code, ~5 content/positioning, ~4 analytical = ~40% code
- Auto-schedule: 3+ REVIEWs → all code = 100% code

**Helpdesk** is code-heavy. **Steps-framework** is mixed (methodology project = lots of content/analytical). **Scheduler** is all code.

**Conclusion:** TFW is used for code-heavy AND content-heavy projects. If modes didn't exist, non-code projects would have 4 N/A items per review (the HD Phase0 pattern). Three modes is justified.

**But — does the reviewer need to explicitly select a mode?** Or can it be automatic?

The mode is determinable from the task: if TS has "file paths" and "LOC budget" → standard. If TS is about writing deliverables → content. If TS produces specs/analysis → analytical.

**Simplification:** Mode could be a suggestion in the workflow, not a hard gate. "Default: standard. If task has no code changes → content or analytical." Same pattern as research mode.

**Verdict: 3 modes is JUSTIFIED.** Steps-framework alone proves 60% non-code tasks exist. Auto-detection is a nice-to-have but manual selection (like research) is simpler and reliable.

### C3: Counter — "The Verify stage doubles the review time"

**Test:** What does Verify actually cost?

For a code task:
- Open 2-3 files → check changes exist → ~2 minutes agent time
- Re-run one test → ~1 minute (if possible)
- Cross-reference AC checkmarks → ~2 minutes
Total: ~5 minutes. Current review time for HD PhaseF: ~15-20 minutes. Verify adds ~25% overhead.

For a docs task:
- Check deliverable files exist → ~30 seconds
- Check structure matches spec → ~1 minute
Total: ~1.5 minutes. Minimal overhead.

**The TFW-36 incident proves the cost of NOT verifying:** A fabricated citation traversed 4 roles and 8 documents. The review took ~20 minutes and missed it. Adding 5 minutes of verification would have caught it.

**Verdict: JUSTIFIED.** 25% overhead for code reviews, minimal for docs. The cost of NOT verifying (missed bugs, fabricated citations) is dramatically higher.

### C4: Mode Naming Analysis

**Current proposal:** `standard`, `content`, `analytical`

**Problems with these names:**
- "standard" implies "normal/default" — biases toward always using it
- "content" is vague — could mean UI content, documentation, writing
- "analytical" could be confused with data analysis tasks

**Alternative naming options:**

| Option | Code tasks | Writing tasks | Spec/research tasks |
|--------|-----------|---------------|---------------------|
| A (current) | standard | content | analytical |
| B (by output) | implementation | deliverable | specification |
| C (by action) | build | compose | analyze |
| D (by what's reviewed) | code | prose | artifacts |

**Analysis:**
- Option B: "implementation / deliverable / specification" — clear, but "deliverable" is too generic
- Option C: "build / compose / analyze" — verb-based, active, distinct
- Option D: "code / prose / artifacts" — short, memorable, but "artifacts" collides with TFW artifact terminology

**The user said:** "code/business/education/design something else" — suggesting domain-based naming. But this creates infinite modes (one per domain). The mode should describe WHAT IS BEING REVIEWED (the output type), not WHICH DOMAIN it belongs to.

**Recommendation:** Keep it simple. The mode describes the primary output type:
- **code** — implementation with tests (verify: run/check tests)
- **prose** — written deliverables (verify: check sources, structure)
- **spec** — analytical specifications, research output (verify: check sources, citations)

Three short, memorable names. The mode configures the Assess checklist items, not the domain.

**Verdict: Rename to `code`, `prose`, `spec`.** Shorter, more precise, less biased than "standard."

### C5: Does REVIEW Template Need New Sections?

Current REVIEW template has: §1 Checklist, §2 Verdict, §3 Tech Debt, §4 Traces, §5 Fact Candidates.

Staged review would restructure to:
- §1 Comprehend (brief summary of what was reviewed)
- §2 Verify (evidence table — what was checked, what was found)
- §3 Assess (domain-aware checklist)
- §4 Verdict (from current §2)
- §5 Tech Debt (from current §3)
- §6 Traces (from current §4)
- §7 Fact Candidates (from current §5)

This is a template restructure, not just a workflow change. The template and workflow must change together (this was the ROOT CAUSE from iteration 1 — they must match).

**Word cost of template change:** ~20 additional words for §1 Comprehend header + §2 Verify table template. Other sections just renumber.

### C6: Edge Case — What If Verify Finds a Problem?

Current flow: if reviewer finds an issue, they write "❌" in checklist and REVISE verdict.

With staged review: if Verify finds a discrepancy (e.g., RF claims "tests pass" but test file doesn't exist), what happens?

**Answer:** The same — reviewer proceeds through Assess and Synthesize, documents the discrepancy as evidence, and renders REVISE verdict in §4. The stages don't gate each other (unlike research stages). They're cognitive phases, not approval gates.

**This is a key difference from research:** Research stages have checkpoints with WAIT gates. Review stages DON'T — they flow sequentially within one agent session. The mindset transitions, but execution doesn't pause.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Sections-as-stages work IF workflow enforces mindset (C1) | None |
| 3 modes justified by task type distribution (C2) | None |
| Verify adds ~25% overhead, justified by error prevention (C3) | None |
| Mode naming: code / prose / spec (C4) | None |
| REVIEW template needs restructure to match (C5) | **Implementation detail for TS** |
| Stages don't gate — they flow sequentially, unlike research (C6) | **Key design distinction** |

**Sufficiency:**
- [x] External source used? (ISO model applied in Gather, constraint budget from iter 1)
- [x] Briefing gap closed? (All open threads resolved)

Stage complete: YES
→ User decision: ___
