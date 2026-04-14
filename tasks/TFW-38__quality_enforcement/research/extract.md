# Extract — "What do we NOT see?"
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: Structural analysis — why workflows cause skipping, what patterns enforce completion.

## Findings

### E1: Template-Workflow Disconnect — The Root Cause

The RF template (`.tfw/templates/RF.md`) has 8 sections: §1-5 (core) + §6 Fact Candidates + §7 Strategic Insights + §8 Diagrams.

The handoff workflow (`handoff.md` Phase 3, line 73) lists 6 mandatory items:
```
- What was done
- Test results
- Known limitations or tech debt
- Deviations from TS
- Screenshots / logs
- Observations
```

**§6, §7, §8 are NOT in this list.** There's a "Fact Candidates" mention in the informational blockquote below (lines 81-87), but it's framed as a suggestion ("As you work, capture strategic knowledge..."), not as a mandatory section enumeration.

**The disconnect mechanism:**
1. Agent reads handoff.md Phase 3 → sees the 6-item mandatory list
2. Agent opens RF template → sees §1-8
3. Agent fills §1-5 from the mandatory list → "Observations" maps to §5
4. Agent stops. §6-8 have no corresponding mandatory item in the workflow.
5. The template's §6-8 sections with their blockquote instructions are invisible to the agent's task execution context — the agent has already decided "what to do" from the workflow and is using the template only for "how to format."

**This is the exact pattern from HL S1:** "Agents treat workflows as WHAT to do, templates as HOW to format. When they disagree, workflow wins."

### E2: Word Count Budget Analysis

| Workflow | Current words | Budget (1200 max) | Headroom |
|----------|---------------|--------------------| ---------|
| handoff.md | **825** | 1200 | **375 words** |
| review.md | **816** | 1200 | **384 words** |
| research/base.md | **748** | 1200 | **452 words** |
| docs.md | **443** | 1200 | **757 words** |

All four target workflows are well within budget. The HL risk R1 (word count exceeds 1200) is LOW probability — there's ample headroom for enforcement additions.

**Estimated word cost of proposed changes:**
- handoff.md Phase 3 §6-8 enumeration: ~30 words
- review.md Step 1.5 audit section: ~80-100 words
- review.md checklist item #10: ~10 words
- research/base.md Findings Map mention: ~10 words
- docs.md diagram collection section: ~60-80 words
- conventions.md §14 new anti-patterns: ~30-40 words

**Total: ~220-270 words across 4 files.** Well within budget.

### E3: Positive Example Analysis — What Made HD PhaseG/H Fill §6-8?

Two recent HD RFs (PhaseG = 2026-04-14, PhaseH = 2026-04-14) are the only RFs with all three sections filled. Analysis:

**HD-4 PhaseH RF** (the best example):
- §6: 5 fact candidates with Category/Candidate/Source/Confidence columns
- §7: 3 strategic insights with Insight/Implication columns
- §8: 1 mermaid sequence diagram (auth flow)
- This RF was produced by an agent that had a conversation where the user explicitly cared about §6-8 quality (this is the same session where TFW-38 was conceived)

**HD-3 PhaseG RF**:
- §8 Fact Candidates: 5 entries (renamed from §6 → §8 — likely template confusion)
- No §7 Strategic Insights section
- No diagrams section

**Conclusion:** The positive examples correlate with user attention to quality, not with workflow instructions. The agent filled §6-8 because the user was actively discussing quality enforcement, not because handoff.md told it to.

### E4: REVIEW Template vs Workflow Gap

**REVIEW template** has 9-item checklist (#1-9). Item #9 is "Observations collected."

**Missing from both template and workflow:**
- No item for "RF §6-8 completeness check"
- No instruction to verify RF claims independently
- review.md Step 1 says "Read RF thoroughly" and "Examine changed files" — but "examine" is passive, not adversarial

**Existing reviewer behavior** (from Gather G3):
- TFW-36 REVIEW self-assessed: "I trusted executor's self-reported fix instead of verifying independently"
- TFW-19 REVIEW: only one with explicit "§3. Independent Verification" section
- HD-3 Full REVIEW: flags "not verified independently" for coverage claim — honest but not structural

**The fix:** Add item #10 to checklist ("RF completeness: §6-8 present or explicitly N/A") + add audit step to workflow.

### E5: research/base.md Step 6 Gap

Step 6 Synthesis (lines 83-93) lists what to include:
```
3. HL Update Recommendations (table)
4. Fact Candidates — review conversation history first
5. Iteration Status block (mandatory) — see RES template
6. Conclusion (1 paragraph)
```

**Missing:** Findings Map. It's in the RES template (lines 73-82) but not mentioned in Step 6.

**Template section is there, workflow instruction is not.** Same disconnect pattern as RF §6-8.

### E6: docs.md Diagram Collection Opportunity

docs.md has 6-item checklist:
```
1. Architecture changed?
2. New decision?
3. Something deprecated?
4. New tech debt?
5. New principle/convention?
6. Fact Candidates present?
```

**Missing:** "Diagrams/process docs to collect?" — no mechanism to extract mermaid diagrams or architecture visuals from RF §8 or RES Findings Map into persistent project documentation.

docs.md is at 443 words (757 headroom) — adding a diagram collection step fits easily.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Template-workflow disconnect is the exact mechanism | None |
| Word budgets have 375-757 word headroom each | None |
| Positive examples are user-attention-driven, not workflow-driven | None |
| REVIEW template missing §6-8 completeness check | None |
| research/base.md Step 6 misses Findings Map | None |
| docs.md has no diagram collection | None |

**Sufficiency:**
- [x] External source used? (Confirmed by RLCF/TICK research in Gather)
- [x] Briefing gap closed? (All structural gaps identified and quantified)

Stage complete: YES
→ User decision: ___
