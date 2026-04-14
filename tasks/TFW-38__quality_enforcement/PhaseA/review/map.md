# Map — "What was done?"
> **Mindset:** Newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF__PhaseA2__review_stage_files.md](../RF__PhaseA2__review_stage_files.md)
> TS: [TS__PhaseA2__review_stage_files.md](../TS__PhaseA2__review_stage_files.md)
> Mode: spec

## Understanding

The executor converted the review process from an inline section-based flow into a file-based trace system. Three new stage templates were created (`map.md`, `verify.md`, `judge.md`) in `.tfw/templates/review/`, each with an identity-based mindset header (Newcomer/Auditor/Judge) and a self-check gate. The `review.md` workflow was rewritten (Steps 0-4) to instruct the reviewer to create a `review/` subfolder, write stage files, and then synthesize them into the REVIEW artifact. The REVIEW.md template was updated to reference stage files, and `conventions.md` §3 gained a new "Review subfolder" entry paralleling the research subfolder convention.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC1: 3 stage templates exist in `.tfw/templates/review/` | RF §1: map.md (905B), verify.md (1341B), judge.md (1602B) created | ✅ |
| AC2: Each template has Mindset as mandatory header field | RF §3: Student/Auditor/Judge + Test Questions in all headers | ✅ |
| AC3: Each template has Checkpoint with self-check gates | RF §3: map (4), verify (4), judge (5) gates | ✅ |
| AC4: verify.md self-check includes KNOWLEDGE.md contradiction check | RF §3: verify self-check item 4 includes KNOWLEDGE.md | ✅ |
| AC5: judge.md self-check includes evidence + KNOWLEDGE.md cross-ref | RF §3: judge self-check items 1, 4, 5 | ✅ |
| AC6: review.md Step 0 has 🛑 WAIT gate | RF §3: review.md line 53-54 | ✅ |
| AC7: Step 0 presents "Switch? [code/docs/spec]" | RF §3: review.md line 53 | ✅ |
| AC8: Steps 1-3 instruct to create review/ folder + stage files | RF §3: review.md lines 56-80 | ✅ |
| AC9: Step 4 synthesizes stage files into REVIEW | RF §3: review.md lines 82-92 | ✅ |
| AC10: REVIEW.md references stage files in header | RF §3: REVIEW.md lines 9-10 | ✅ |
| AC11: conventions.md §3 documents review stage files | RF §3: conventions.md lines 138-140 | ✅ |
| AC12: Stage file structure parallels research stage files | RF §3: Findings → Checkpoint → Self-check | ✅ |
| AC13: review.md has Reviewer Identity statement | RF §3: review.md lines 30-31 | ✅ |
| AC14: review.md has Trust Protocol table (7 rows) | RF §3: review.md lines 33-43 | ✅ |

## Deviations from TS

1. **map.md mindset label**: TS Step 1 specifies "Student" as mindset. Actual template uses "Newcomer." This is a terminology deviation — same cognitive intent, different word.
2. **Adapter file** (`.agent/workflows/tfw-review.md`): RF §1 lists this as modified. Not in TS §3 Affected Files. This is an expected out-of-scope change (adapter sync is standard practice per conventions §9).
3. No other deviations detected. All 14 AC items are claimed as met.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy? (Workflow > Template, Map/Verify/Judge/Decide cognitive stages, Knowledge Gate as hard gate across all roles)
- [x] Read ONB — were blocking questions resolved? (No blocking questions. 5 recommendations approved by coordinator.)

Stage complete: YES
