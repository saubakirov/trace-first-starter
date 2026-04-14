# RF — TFW-38 / Phase A.2: Review Stage Files + Self-Check Gates

> **Date**: 2026-04-14
> **Author**: Executor
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> **TS**: [TS Phase A.2](TS__PhaseA2__review_stage_files.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `.tfw/templates/review/map.md` | Map stage template — Experienced newcomer mindset, TS↔RF alignment table, self-check gate (4 items) |
| `.tfw/templates/review/verify.md` | Verify stage template — Auditor mindset, verification log per file, commands table, discrepancy escalation, self-check gate (4 items incl. KNOWLEDGE.md) |
| `.tfw/templates/review/judge.md` | Judge stage template — Judge mindset, universal 6-point checklist, mode-specific slot, KNOWLEDGE.md contradictions table, self-check gate (5 items) |

### Modified Files
| File | Changes |
|------|---------|
| `.tfw/workflows/review.md` | Steps 0-4 rewritten. Role Lock updated (stage files + REVIEW). Added Reviewer Identity (D21), Trust Protocol 7-row table (D27), Step 0 🛑 WAIT gate, Steps 1-3 file-based stages with mindset blockquotes (Experienced newcomer/Auditor/Judge/Decision-maker), Step 4 as synthesis. Steps 5-7 unchanged. Post-review: Step 1 mindset synced to "Experienced newcomer" per user directive. |
| `.tfw/templates/REVIEW.md` | Added `Stage files` reference in header (lines 9-10). §2 Verify now points to `review/verify.md` for raw evidence. |
| `.tfw/conventions.md` | §3: New "Review subfolder" section (lines 138-140). §15: Role Lock table updated — Reviewer row now includes stage files (TD-97 fix). |
| `.tfw/glossary.md` | REVIEW entry updated from stale "9-point checklist" to "4-stage process with stage files" (TD-98 fix). |
| `.agent/workflows/tfw-review.md` | Adapter re-synced from `.tfw/workflows/review.md`. |

## 2. Key Decisions

1. **Role Lock expanded** — "Permitted artifacts: review stage files (map.md, verify.md, judge.md) + REVIEW file." Per ONB §4.1 coordinator approval.
2. **Review subfolder placement** — inserted right after Research subfolder trace rule (line 136) for structural parallelism. Per ONB §4.3 coordinator approval.
3. **REVIEW §2 Verify** — kept summary table + added link to verify.md for raw evidence. Per ONB §4.2 coordinator approval.
4. **Mindset rename** (post-review) — "Student" → "Experienced newcomer" in map.md template and review.md Step 1. User directive: avoids academic connotation while preserving the "understand before judging" cognitive intent.
5. **TD-97 + TD-98 fixes** (post-review) — conventions.md §15 Role Lock table and glossary.md REVIEW entry updated to reflect stage files. Applied immediately per REVIEW triage ("→ quick fix").

## 3. Acceptance Criteria

- [x] 3 stage templates exist in `.tfw/templates/review/` (map.md, verify.md, judge.md)
- [x] Each template has **Mindset** as a mandatory header field (Experienced newcomer / Auditor / Judge) with Test Question
- [x] Each template has a Checkpoint section with self-check gates (checkboxes)
- [x] verify.md self-check includes KNOWLEDGE.md contradiction check
- [x] judge.md self-check includes evidence requirement + KNOWLEDGE.md cross-reference
- [x] `review.md` Step 0 has 🛑 WAIT gate after mode presentation (parallels research Step 2)
- [x] `review.md` Step 0 presents mode with "Switch? [code/docs/spec]" option
- [x] `review.md` Steps 1-3 instruct reviewer to create `review/` folder and write stage files
- [x] `review.md` Step 4 instructs reviewer to synthesize stage files into REVIEW artifact
- [x] `REVIEW.md` template references stage files in header
- [x] `conventions.md` §3 documents review stage files
- [x] Stage file structure parallels research stage file structure (Findings → Checkpoint → Self-check)
- [x] `review.md` has Overall Reviewer Identity statement before Step 0 (D21 pattern)
- [x] `review.md` has Trust Protocol table for RF claim types (D27 pattern, 7 rows)

## 4. Verification

- Lint: N/A (markdown files)
- Tests: N/A (no automated tests)
- Verify: Manual — all 14 acceptance criteria verified + 3 post-review fixes:
  - Templates: 3 files (map.md, verify.md, judge.md) ✅
  - Mindsets: Experienced newcomer / Auditor / Judge + Test Questions ✅
  - Self-check gates: map (4), verify (4 incl. KNOWLEDGE.md), judge (5 incl. evidence+KNOWLEDGE.md) ✅
  - review.md: 🛑 WAIT + "Switch? [code/docs/spec]" ✅
  - review.md: Steps 1-3 create review/ folder + stage files ✅
  - review.md: Step 4 synthesizes into REVIEW ✅
  - REVIEW.md: Stage files reference in header ✅
  - conventions.md §3: Review subfolder section ✅
  - conventions.md §15: Role Lock table includes stage files (TD-97 fix) ✅
  - glossary.md: REVIEW entry updated to 4-stage (TD-98 fix) ✅
  - review.md: Reviewer Identity + Trust Protocol (7 rows) ✅

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/conventions.md` | 88 | style | Visual Sections table has `REVIEW | — | — | No visual section` — this was true before stage files but is now outdated. REVIEW is now a synthesis artifact with stage files as visual traces. Not a critical issue — the table describes template-level visual sections, not stage files. |
| 2 | `.tfw/workflows/review.md` | 12 | naming | Role Lock now lists 4 permitted artifacts (3 stage files + REVIEW). This is the longest permitted artifacts list — other Role Locks (Executor: ONB, RF; Coordinator: HL, TS) have 2. Consistent with scope but notable. |

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | philosophy | Reviewer mindset labels must avoid academic/patronizing connotations. "Student" rejected in favor of "Experienced newcomer" — same cognitive intent (understand before judging), but respects the reviewer's competence | User directive, REVIEW A.2 | High |

## 7. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | Low-severity TD items that fix consistency gaps (stale glossary entries, mismatched tables) should be applied immediately during review, not backlogged. The "→ quick fix" triage action prevents accumulation of drift between canonical workflow files and their documentation mirrors. | convention | REVIEW A.2 TD-97/TD-98 |

## 8. Diagrams

No diagrams.

---

*RF — TFW-38 / Phase A.2: Review Stage Files + Self-Check Gates | 2026-04-14*
