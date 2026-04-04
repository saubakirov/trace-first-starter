# RES — TFW-24: Researcher Role & RES State Machine

> **Date**: 2026-04-04
> **Author**: Researcher
> **Status**: 🔬 RES — In progress
> **Parent HL**: [HL-TFW-24](HL-TFW-24__res_state_machine.md)
> **Mode**: Pipeline / Focused

---

## Research Context
TFW-24 proposes splitting Researcher from Coordinator into a standalone role with its own Role Lock, and adding a State Table to the RES file for crash-resilient resumability. This research investigates: (1) whether the role split is a clean relabeling or requires new workflow logic, (2) whether a markdown State Table is a format agents can reliably parse after crash recovery, (3) how Step 0 (Resume Protocol) should work, and (4) whether the word budget (≤600) is achievable.

## Briefing

### Research Plan
1. **Gather** — Study how other multi-agent frameworks handle role-based crash recovery and state persistence. Find examples of state tables in markdown that AI agents parse reliably. Look at MCP state patterns.
2. **Extract** — Analyze current base.md, conventions.md §15, and glossary.md for exact changes needed. Word count current base.md. Map "Coordinator (Research Mode)" references across .tfw/. Identify what's truly new vs relabeling.
3. **Challenge** — Test edge cases: crash mid-gate, two active stages, pipeline handback ambiguity. Verify word budget feasibility. Stress-test State Table format options.

### Scope Intent
- **In scope:** State Table format, Step 0 wording, Role Lock table changes, word budget feasibility, pipeline handoff/handback protocol
- **Out of scope:** Changes to other roles (Executor, Reviewer), new workflow files beyond base.md modifications, OODA loop changes

### Guiding Questions
1. What worries you most — the State Table format (agents parsing it wrong) or the role separation (pipeline confusion at handoff/handback)?
2. Should the Researcher role be allowed to update HL §10 hypotheses directly, or must that go through Coordinator?
3. Is there any scenario where Coordinator should still be able to conduct research (emergency/inline) or is the split absolute?

### Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | State Table in RES file is sufficient for crash recovery (no external state file needed) | confirmed (user) | 🟢 accepted | User confirmed |
| H2 | Researcher role maps 1:1 to existing "Coordinator (Research Mode)" — no new workflow logic needed, just role relabeling + state machine | open | 🟡 partial | Role relabeling = yes. But subfolder architecture (D1) = new workflow logic. Not pure relabeling. |
| H3 | State Table format that agents reliably parse exists within 10 lines | open | ⚫ superseded | Replaced by D1: file existence = state. No table to parse. |
| H4 | Word budget (≤600) is achievable with Step 0 + state rules added | open | 🟢 confirmed | 518 + ~70 = ~588 words. Within budget. |

→ User direction:
- Priority = reliability (crashes, pauses, switches). Format secondary.
- Researcher writes RES only. Recommends HL updates → Coordinator applies. Strict separation.
- Absolute role split. Coordinator light research ≠ Researcher structured investigation. No overlap.
- **Reframing (user):** State Table is a detail, not the goal. Goal = structural enforcement. File existence = state machine. Research subfolder with stage files, mandatory consolidation to final RES.
- **HL template gap (user):** Goal and Value sections lost during English standardization. §1 Vision drifted to code-oriented. Need explicit Goal/Value structure.

## Decisions
| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Research subfolder (`research/`) with stage files replaces State Table in RES header | File existence = enforcement. Agent can't skip stages — no Gather file means plan isn't done. No parsing needed. Filesystem IS the state machine. User insight: "дело не в формате, дело в структурности процесса" |
| D2 | Final RES = synthesis document, not concatenation. Structure differs from stage files | External: "Synthesis creates new understanding. Aggregation just lists summaries." Different structure = impossible to copy-paste. RES has: Decisions, Hypotheses, HL Recommendations, Fact Candidates, Conclusion |
| D3 | Researcher role = absolute split from Coordinator. No "Research Mode" overlay | User: "строго". Coordinator does light prep (may suffice → skip research). When not sufficient → Researcher role. No overlap. Same pattern as TFW-8 (Reviewer split) |
| D4 | Goal & Value explicit fields in HL template §1 | Research quality depends on clear goals. F8: "HL-level thinking = values, processes, outcomes". Without structured Goal/Value, Researcher has no north star. In scope for TFW-24 |
| D5 | Stage file naming: `briefing.md`, `gather.md`, `extract.md`, `challenge.md` in `research/` subfolder | D28 applied. `briefing` (not `plan`) avoids conflict with `.tfw/workflows/plan.md`. Simple, descriptive, namespace-isolated by folder |

## Open Questions
| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Stage file template: how much structure? Full OODA checkpoint fields or minimal (Findings + Checkpoint)? | resolved | Minimal with Goal reference. Quality > bureaucracy. Agent reads HL Goal in stage file header = alignment anchor |
| Q2 | Crash mid-stage: how to detect incomplete file? | resolved | Accept partial file (C1 Option 3). Agent reads content, assesses completeness. Simplicity over mechanism |
|---|----------|--------|--------|

---

## Stage: Gather — "What do we NOT know?"

### G1: External — Multi-agent crash recovery patterns (3 web searches)

**LangGraph** (industry leader for stateful agents): Uses "checkpointers" — saves graph state snapshot after every node. Stores in "threads" by `thread_id`. Crash → resume from last checkpoint. Supports time-travel debugging and human-in-the-loop pause/resume.

**CrewAI**: `@persist` decorator + SQLite. UUID per flow instance. Task replay on failure, but developer must trigger manually.

**AutoGen**: Manual `save_state()`/`load_state()`. No native checkpoint infra. Developer builds their own.

**Key insight**: Industry convergence → checkpoint after every meaningful step. LangGraph does it automatically (infrastructure-level). TFW can't do automatic — we don't control the runtime. But we CAN mandate "update state table before every WAIT" (agent-level enforcement).

### G2: External — File-based state persistence for AI agents

Pattern validated externally: `STATE.md` or `TASKS.md` in filesystem = human-readable, Git-trackable, zero-infrastructure checkpoint.

**Read-Decide-Act-Update cycle** (from external source): Agent reads `STATE.md` at startup → evaluates current state → acts → atomically updates file. Matches TFW's "read-before-write" (HL §7 P2).

**Recommended format** (external): Standard markdown (lists, checkboxes `[ ]`, YAML frontmatter). LLMs are "highly proficient at parsing these formats." Avoid JSON/Protobuf.

**Key insight**: Markdown tables with simple status markers (✅/🔄/⬜) are the optimal format for LLM agents. External sources confirm checkbox `[ ]` syntax is well-parsed. Our State Table approach is validated.

### G3: Internal — Current base.md word count

**base.md = 518 words** (measured). Budget = 600 words. Headroom = 82 words. Step 0 (Resume Protocol) + state table rules need to fit in ~80 words.

### G4: Internal — "Coordinator (Research Mode)" references

Only **1 reference** in `.tfw/` that says "Coordinator (Research Mode)":
- `base.md` L7: `🔒 ROLE LOCK: COORDINATOR (Research Mode)`

Other references use "Research Mode:" as mode file titles (focused.md, deep.md) — these stay.

Additional changes needed:
- `conventions.md` L181: Workflow table, research/base.md → role = Coordinator
- `conventions.md` L279: Role Lock table, research/base.md → Coordinator
- `glossary.md` L97-102: Coordinator role definition includes "Conducts RESEARCH and writes RES files"
- `plan.md` L71: "Start `/tfw-research`" → implicit handoff to same role (Coordinator). Needs to say "Researcher"

### G5: Internal — TFW-8 precedent (Reviewer role split)

TFW-8 established the exact pattern:
1. **Problem**: Executor + Reviewer merged → self-review
2. **Solution**: New role (Reviewer = "coordinator in review mode"), separate workflow, Role Lock, Hard Stop
3. **Key design**: "Not a fundamentally new identity — it's the coordinator with a locked scope"
4. **Pattern**: Extract from parent workflow → standalone workflow → Role Lock → Hard Stop → adapter sync

TFW-24 follows identical structure: Coordinator + Researcher merged → role confusion → split.

Difference: TFW-8's Reviewer was extracted FROM handoff.md (Phase 4 removed). TFW-24's Researcher already HAS its own workflow (base.md). The change is Role Lock relabeling + State Table addition, not workflow extraction.

### Checkpoint: Gather
| Found | Remaining |
|-------|-----------|
| Crash recovery = checkpoint after every step (LangGraph pattern) | — |
| File-based state = markdown table with simple status markers (validated) | — |
| base.md = 518 words, 82 words headroom | — |
| Only 1 "Coordinator (Research Mode)" ref in workflows | — |
| 4 additional files need role label change (conventions, glossary, plan) | — |
| TFW-8 precedent: identical split pattern, but TFW-24 = relabeling not extraction | — |

**Sufficiency Verdict:**
- [x] External source used? (3 web searches, multiple sources)
- [x] Briefing gap closed? (Gather plan: "how other frameworks handle crash recovery" — answered)

**Agent assessment:** Gather is sufficient. We have external validation for file-based state, format choice, and the checkpoint-after-every-step pattern.
**Depth check:** Used web search (3 queries), read 8 project files. External + internal covered.
**Recommendation:** Close stage, proceed to Extract.
Stage complete: YES
→ User decision: ___

## Stage: Extract — "What do we NOT see?"

### E1: Research subfolder architecture — what changes

**Current flow (base.md):** Agent creates 1 RES file, updates it throughout, checkpoints are sections within the same file.

**Proposed flow:** Agent creates `research/` subfolder with stage files. Final consolidation produces RES.

```
tasks/{PREFIX}-{N}__{title}/
  HL-{PREFIX}-{N}__{title}.md
  research/                        ← NEW subdirectory
    plan.md                        ← briefing, hypotheses, scope, user direction
    gather.md                      ← stage output + checkpoint
    extract.md                     ← stage output + checkpoint
    challenge.md                   ← stage output + checkpoint
  RES__{PREFIX}-{N}__{title}.md    ← final consolidated report (mandatory)
```

**State machine = filesystem:**
- No `research/` folder → research not started
- `plan.md` exists → briefing done
- `gather.md` exists → gather complete
- `extract.md` exists → extract complete  
- `challenge.md` exists → challenge complete
- `RES__*.md` exists → research consolidated

**Agent resume algorithm (Step 0):**
1. Check: does `research/` exist? If no → start fresh
2. Check: which stage files exist? → resume from first missing
3. Check: does `RES__*.md` exist? If yes → research done, proceed to Closure

This is ~30 words in base.md. Compare to the State Table approach (~50-60 words). Actually simpler.

### E2: What happens to the RES template

Current `templates/RES.md` (160 lines) is a monolith — briefing, all 3 stages, final checkpoint, closure all in one file. With the subfolder approach:

**Option A:** Keep RES template as-is for the FINAL consolidated file. Stage files get their own mini-templates.
- Pro: RES remains the canonical artifact. Stage files are working documents.
- Con: Need 2+ new templates (stage file, plan file).

**Option B:** Split RES template into parts: `templates/RES_PLAN.md`, `templates/RES_STAGE.md`, `templates/RES.md` (consolidation only).
- Pro: Each file has clear template. Progressive Disclosure.
- Con: Template proliferation.

**Option C (hybrid):** Keep one RES template that includes ALL stage structures, but the workflow creates stage files by extracting the relevant section. Final RES = consolidation of stage files back into the full template.
- Pro: Single source of truth for format. Agent knows what final RES should look like.
- Con: More complex workflow instructions.

**Recommendation:** Option A. RES template = final report format. Stage files are lightweight (just content + checkpoint). Plan file = briefing + hypotheses.

### E3: HL template — Goal and Value gap

Checked TFW-4 (early HL): "Цель — привести стартер в состояние..." — Goal is embedded in prose. No structured field.

Current template §1:
```
## 1. Vision
What we want and WHY. Business value. Brand context.
```

Problems:
1. "What we want and WHY" = instruction, not structure. Agent writes prose, doesn't separate Goal from Value.
2. §2 says "Current code, bugs, metrics, architecture" — code-specific
3. §5 says "tests, code, data, deploy, monitoring" — software-specific
4. D29 (TFW-23) made §3.1 domain-agnostic but didn't touch §1, §2, §5

**This is a separate task** (TFW-25?). Recording as HL Update Recommendation for now.

Proposed fix sketch:
```
## 1. Goal & Value
**Goal:** {what we are achieving} — one sentence
**Value:** {why it matters} — what changes if we succeed vs don't
> One key quote that captures the essence.
```

### E4: Role changes — exact diff

**conventions.md §8 (Workflows table):**
- L181: `research/base.md | Coordinator` → `research/base.md | Researcher`

**conventions.md §15 (Role Lock table):**
- L279: `research/base.md | Coordinator | RES` → `research/base.md | Researcher | RES`

**glossary.md §Roles:**
- L97-102: Remove "Conducts RESEARCH and writes RES files" from Coordinator
- Add new ### Researcher (AI) section
- L112: Reviewer is "coordinator in review mode" — Researcher follows same pattern: "dedicated research agent"

**plan.md §Step 6:**
- L71: "Start `/tfw-research`" → add: "Hand off to Researcher. **STOP.**"
- Need Hard Stop Rule for Coordinator→Researcher (like Coordinator→Executor already has)

**base.md L7:**
- `🔒 ROLE LOCK: COORDINATOR (Research Mode)` → `🔒 ROLE LOCK: RESEARCHER`

**PROJECT_CONFIG.yaml §statuses:**
- L73-76: RES status `role: coordinator` → `role: researcher`

### E5: Word budget — reassessment

With the subfolder approach, base.md changes are:
- Remove: nothing from existing content
- Add: Step 0 (resume protocol, ~30 words) + subfolder creation instruction in Step 3 (~20 words) + consolidation instruction in Step 7 (~20 words)
- Change: Role Lock line (same word count)

**518 + 70 = ~588 words. Within 600 budget.** H4 = confirmed feasible.

### E6: External validation — structural enforcement

External research confirms (search #4):
> "Decouple procedure from cognition. Stop asking the agent to remember where it is. Move state outside the agent into an external structure."
> "Artifact-Based Validation: Force each step to output a specific artifact. If the required file does not exist, downstream tasks remain blocked."
> "The Deterministic Sandwich: alternate between Cognitive Atoms (LLM does work) and Deterministic Gates (system verifies output)."

This is exactly what the subfolder approach does. Each stage file IS the artifact-based gate. No file = blocked.

### Checkpoint: Extract
| Found | Remaining |
|-------|-----------|
| Subfolder architecture: 5 files (plan + 3 stages + RES final) | Template approach needs decision (A/B/C recommended: A) |
| Role changes: 6 files need editing (conventions, glossary, plan, base, config, adapters) | — |
| HL template Goal/Value gap: confirmed, separate task | — |
| Word budget: ~588 words feasible (H4 confirmed) | — |
| External: "artifact-based validation" = exact match for subfolder gates | — |
| Resume algorithm: 30 words, 3-step check (folder → files → RES) | — |

**Sufficiency Verdict:**
- [x] External source used? (web search: structural workflow enforcement)
- [x] Briefing gap closed? (Extract plan: "exact changes needed" — mapped all 6 files)

**Agent assessment:** Extract is sufficient. We have the full change map, word budget confirmed, and external validation for artifact-based gates.
**Depth check:** 1 external search + 6 internal file reads. Both axes covered.
**Recommendation:** Close stage, proceed to Challenge.
Stage complete: YES
→ User decision: ___

## Stage: Challenge — "What do we NOT expect?"

### C1: Edge case — crash mid-stage file write

**Scenario:** Agent crashes while writing `gather.md`. File exists but is incomplete.

**Risk:** Resume algorithm sees file → assumes stage done → skips to Extract. Broken.

**Mitigation options:**
- Option 1: Two-step write — agent writes to `_gather.md` (temp), renames to `gather.md` on completion. Resume checks for underscore-prefixed files = "interrupted."
- Option 2: Each stage file MUST end with a `## Checkpoint` section containing `Stage complete: YES`. Resume checks for this line. Missing = incomplete.
- Option 3: Accept the risk. Partial file is better than no file. Agent reads file on resume, sees it's incomplete from content, continues.

**Recommendation:** Option 3. Reason: agents are good at reading content and assessing completeness. Adding temp files or checkpoint parsing adds complexity that the subfolder approach was designed to avoid. The whole point is simplicity. If the agent can read "Stage complete: YES/NO" in the content, it can decide whether to continue or redo. No extra mechanism needed.

### C2: Edge case — pipeline handback ambiguity

**Scenario:** Research done. RES exists. Who resumes the pipeline — Coordinator or Researcher?

**Current plan.md L74:** "After RESEARCH: read RES Closure → update HL → present diff to user → proceed to Step 7."

This is clear: **Coordinator** resumes. Researcher writes RES, recommends HL updates in Closure section. Coordinator reads RES, applies recommendations, continues to TS.

**Hard Stop needed in base.md:** After writing final RES, Researcher MUST stop and say: "Research complete. Start `/tfw-plan` to continue planning." (Parallels: Executor → "/tfw-review", Coordinator → "/tfw-handoff")

**But wait:** Unlike Executor→Reviewer (always different sessions), Coordinator→Researcher might need to be the SAME session if research was inline in planning. The user said no — "строго." Separate invocations. OK.

**Decision:** Researcher writes RES → STOP → user starts `/tfw-plan` → Coordinator reads RES Closure → updates HL → proceeds.

### C3: Consolidation quality — the real risk

External research confirms: "Synthesis creates new understanding. Aggregation just lists summaries." The risk with stage files is that consolidation becomes mechanical copy-paste rather than synthesis.

**The final RES must be a synthesis document**, not a concatenation of gather.md + extract.md + challenge.md. It must:
1. Integrate findings across stages (not per-stage summaries)
2. Identify patterns and contradictions
3. Connect everything back to HL Goal & Value
4. Produce actionable HL Update Recommendations

**How to enforce this in the template:** The final RES template should NOT contain stage sections (Gather/Extract/Challenge). Instead it should have:
- Decisions (synthesized across all stages)
- Open Questions (remaining)
- Hypotheses (final status + evidence)
- HL Update Recommendations
- Fact Candidates
- Conclusion

The stage files are working documents. The RES is the verdict. Different structures = impossible to copy-paste.

**D28 (Naming > Explanation):** Need the right term for this consolidation step. Not "Consolidation" (sounds mechanical). Not "Summary" (sounds reductive). 

Candidate terms:
- **Synthesis** — "combining parts into a whole." Academic, precise. ✅
- **Verdict** — "final judgment." Legal connotation. Too narrow.
- **Distillation** — "extracting the essential." Good for chemistry, weird for research.

**Recommendation:** "Synthesis" for the act, "RES" remains the artifact name. The workflow step = "Step 7: Synthesize → write final RES."

### C4: Goal & Value in HL — scope fit

User says Goal/Value in HL is the same concern as TFW-24: "research не должен уходить в сторону от целей и ценности."

**Challenge:** Is this scope creep or genuinely connected?

**Analysis:** 
- TFW-24 Goal: research that can't skip, rush, or lose state.
- Goal/Value in HL: clear destination for research to anchor against.
- Connection: if HL §1 doesn't state Goal and Value clearly, what does the Researcher optimize for? The plan.md file? The user's chat messages? If the Researcher needs a north star, it's the HL's Goal & Value.

Convention F8: "HL-level thinking = values, processes, outcomes." This IS the same concern.

**But:** Adding Goal/Value to the HL template is a different type of change (template format) than Researcher role + subfolder (workflow + conventions). They're conceptually connected but mechanically separate.

**Recommendation:** Include Goal/Value in TFW-24 as a sub-deliverable. It's 2 lines in the HL template. The change is tiny. The connection is real. Separate task would be overhead for 2 lines.

### C5: Stage file term design

Per D28 — right names create right agent behavior. What should the stage files be called?

Current plan from E1: `plan.md`, `gather.md`, `extract.md`, `challenge.md`

**Challenge:** `plan.md` conflicts with `.tfw/workflows/plan.md`. Agent might confuse research plan with task planning workflow.

**Options:**
- `briefing.md` instead of `plan.md` → matches base.md Step 4 ("Briefing Protocol"). No ambiguity.
- `00_briefing.md`, `01_gather.md`, `02_extract.md`, `03_challenge.md` → numbered = ordered. But ugly and over-engineered.

**Recommendation:** `briefing.md`, `gather.md`, `extract.md`, `challenge.md`. Simple, descriptive, no conflicts. The `research/` folder provides namespace isolation.

Stage file internal structure (lightweight, per D28):
```markdown
# {Stage Name}
> Parent: [HL-{PREFIX}-{N}](../../HL-{PREFIX}-{N}__{title}.md)
> Goal: {from HL §1}

## Findings
{content}

## Checkpoint
Stage complete: YES / NO
```

Minimal. Goal reference forces alignment with HL. Checkpoint = completion marker.

### Checkpoint: Challenge
| Found | Remaining |
|-------|-----------|
| Crash mid-stage: accept partial file, agent reads content (Option 3) | — |
| Pipeline handback: Researcher STOP → user → Coordinator reads RES Closure | — |
| Consolidation = synthesis, NOT copy-paste. RES structure must differ from stage files | — |
| Goal/Value in HL = in scope for TFW-24 (2-line template change, real connection) | — |
| Stage file naming: briefing/gather/extract/challenge. No conflicts | — |
| Term: "Synthesis" for consolidation step | — |

**Sufficiency Verdict:**
- [x] External source used? (web: synthesis vs aggregation patterns)
- [x] Briefing gap closed? (Challenge plan: "edge cases, word budget, format stress test" — covered)

**Agent assessment:** Challenge is sufficient. Found 1 real risk (consolidation becoming copy-paste), resolved by different RES structure. Edge cases have clean answers. Goal/Value confirmed in scope.
**Depth check:** 1 external search + 2 knowledge files + internal analysis. Both axes covered.
**Recommendation:** Close stage, proceed to Final Checkpoint.
Stage complete: YES
→ User decision: ___

---

## Final Checkpoint

| Stage | Status | Key Findings |
|-------|--------|-------------|
| Gather | ✅ done | LangGraph checkpoint pattern validated file-based state. Markdown tables confirmed parseable. base.md = 518 words (82 headroom). TFW-8 = exact structural precedent for role split. Only 1 "Coordinator (Research Mode)" ref in workflows. |
| Extract | ✅ done | Subfolder architecture mapped (briefing + 3 stages + RES). Option A for templates (RES = final synthesis, stage files = lightweight). HL Goal/Value gap confirmed (F8). Role changes: 6 files. Word budget: ~588 feasible. External: "Artifact-Based Validation" = exact match. |
| Challenge | ✅ done | Crash mid-stage: accept partial file (simplicity). Pipeline handback: Researcher STOP → user → Coordinator. Consolidation risk solved: RES structure ≠ stage structure → synthesis, not copy-paste. Goal/Value = in scope. Stage naming: briefing/gather/extract/challenge. Term: "Synthesis." |

### Sufficiency Check
**Question:** Sufficient for HL finalization? Can we confidently define phases, approach, and dependencies?
**Self-check:**
- Are there unclosed Open Questions in RES? → No critical ones. Stage file template detail is a design decision, not a blocker.
- Did all stages produce substantive findings or were any perfunctory? → All three produced decisions with evidence.
- Did every stage include external research, or was it internal-only? → 4 external web searches + 2 knowledge file reads across 3 stages.
- Is the solution proportionate to the problem scale? → Yes. Subfolder approach is more structural than original State Table plan, but the problem (research crash fragility + quality drift) warrants it.
- Are phases, boundaries and dependencies clear enough to finalize HL? → Yes.
**Agent assessment:** Sufficient for HL finalization. Research uncovered a stronger solution (subfolder architecture) than the original plan (State Table), validated externally. The HL needs rewriting to reflect D1 (subfolder replaces State Table) and the added Goal/Value sub-deliverable.
→ User decision: ___

**Verdict:** Sufficient for HL finalization

## Closure

### HL Update Recommendations
| # | What to update | Source |
|---|---------------|--------|
| R1 | **Rewrite §1 Vision → §1 Goal & Value.** Add structured `Goal:` and `Value:` fields. Remove code-specific language ("Business value. Brand context.") → domain-agnostic | C4, D4, F8 |
| R2 | **Rewrite §3 Target State.** Replace State Table visualization with subfolder architecture diagram. State machine = filesystem, not table | D1, E1 |
| R3 | **Update Phase A scope.** Add: subfolder creation in base.md, stage file templates, synthesis step in Step 7, Goal/Value in HL template. Remove: State Table in RES template | D1, D2, D4, E2 |
| R4 | **Update §3.2.** 4 roles stays. But Researcher = dedicated role (not "coordinator in research mode"). Update description | D3, E4 |
| R5 | **Revise DoD.** Add items: stage file templates exist, synthesis step in base.md, HL template §1 updated, briefing.md/gather.md/extract.md/challenge.md naming in conventions. Remove/revise State Table items (4, 5) | D1, D5 |
| R6 | **Add §2 domain-agnostic fixes.** §2 says "Current code, bugs, metrics, architecture" → generalize to "Current state, problems, metrics, structure". §5 says "tests, code, data, deploy, monitoring" → generalize | E3, F8 |
| R7 | **Update H2, H3 in §10.** H2 = partial (role relabeling yes, but new workflow logic). H3 = superseded by D1 (file existence replaces table) | Hypothesis analysis |

### Next Step
→ Update HL with R1-R7 → confirm → TS
→ User decision: ___

### Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | convention | File existence is a stronger enforcement mechanism than in-file state tables for AI agents — filesystem state requires no parsing, no format compliance, no update discipline. "Artifact-Based Validation" pattern (external) | User insight + external research (Gather G2, Challenge C1) | high |
| FC2 | convention | Synthesis ≠ aggregation for research consolidation. Final research artifact must have a DIFFERENT structure from stage working documents to prevent mechanical copy-paste. Term: "Synthesis" | External research (Challenge C3) | high |
| FC3 | convention | HL §1 Vision lacks structured Goal/Value separation. Without explicit Goal and Value fields, research agents have no north star to anchor against. Related to F8: "HL-level thinking = values, processes, outcomes" | User observation + F8 convention | high |

## Conclusion

TFW-24 entered research with a State Table solution (markdown table in RES header for crash recovery). Research revealed that the real problem isn't format — it's structural enforcement. The user's insight ("дело не в формате, дело в структурности процесса") redirected the approach from table-level state to filesystem-level state: a `research/` subfolder with stage files (`briefing.md`, `gather.md`, `extract.md`, `challenge.md`) where file existence IS the state machine. External research validated this as "Artifact-Based Validation" — an industry-recognized pattern for preventing step-skipping in AI workflows. The consolidation risk (copy-paste vs synthesis) was resolved by giving the final RES a different structure from stage files. The HL template's missing Goal/Value structure was identified as a connected concern: research quality depends on clear goals, which must be explicitly stated in HL §1. Self-critique: initial fixation on State Table format (H3) delayed arrival at the stronger solution. The user's reframing was the turning point — research should have questioned the solution earlier, not just the format.

---

*RES — TFW-24: Researcher Role & RES State Machine | 2026-04-04*
