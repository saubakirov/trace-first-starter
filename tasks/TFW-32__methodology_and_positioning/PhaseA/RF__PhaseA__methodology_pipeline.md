# RF — TFW-32 / Phase A: Methodology Pipeline Fixes

> **Date**: 2026-04-10
> **Author**: AI (Executor)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> **TS**: [TS Phase A](TS__PhaseA__methodology_pipeline.md)

---

## 1. What Was Done

All 7 TS steps executed + 2 post-RF tech debt fixes (user-requested). 11 files modified, 0 new files (excluding ONB/RF artifacts).

### Step 1: Verify §0 → knowledge/philosophy.md mapping
Verified all 8 principles (P1, P2, P3, P5, P7, P8, P9, P10) have canonical homes in knowledge/philosophy.md, conventions.md, plan.md Mindset, or `.tfw/README.md` Values. Mapping confirmed per TS table. No information loss.

### Step 2: Remove KNOWLEDGE.md §0
Removed the entire `## 0. Philosophy & Principles` section (P1-P10 table + heading + separator). File now starts with `## 1. Architecture Map`. §1-§4 numbering preserved — no renumbering cascade.

### Step 3: Update tfw-knowledge workflow
- **Header Output** changed from `KNOWLEDGE.md §1/§2/§4, topic files...` → `knowledge/ topic files, KNOWLEDGE.md §4 (index), knowledge_state.yaml`
- **Phase 4**: Stripped items that wrote to §1 (Architecture Decisions) and §2 (Key Artifacts). Replaced with single item: `Update KNOWLEDGE.md §4 (Project Facts)` + explicit warning: `⚠️ Do NOT write to §1 or §2 — those belong to /tfw-docs`

### Step 4: Update tfw-docs workflow
- **Added Scope section** after Prerequisites: `Writes to: KNOWLEDGE.md §1-§3 + TECH_DEBT.md` / `Does NOT write to: knowledge/ topic files, KNOWLEDGE.md §4`
- **Added Orchestration section** after "After Update": recommends `/tfw-knowledge` when FC exist, marks N/A when they don't

### Step 5: Add `📚 KNW` status (4 files)

| File | Change |
|------|--------|
| `conventions.md` §5 | Pipeline diagram: added `📚 KNW` between REV and DONE. Status table: added KNW row. Verdict: APPROVE → 📚 KNW → ✅ DONE |
| `glossary.md` | Pipeline diagram updated. Status count: 8 → 9. Added `### KNW (Knowledge Capture)` definition |
| `PROJECT_CONFIG.yaml` | Added `KNW` entry (emoji: 📚, role: coordinator) between REV and DONE in `tfw.statuses` |
| `README.md` | Key Concepts pipeline + status legend: both updated with KNW. Both now show `(RES, KNW optional)` |

### Step 6: Add REVIEW markers
Added `- [ ] tfw-knowledge: {Applied / N/A / Deferred to batch}` to `.tfw/templates/REVIEW.md` §4 Traces Updated (line after existing tfw-docs marker).

### Step 7: Update review.md workflow
- **Step 5 Verdict**: Changed `✅ APPROVE → ✅ DONE` to `✅ APPROVE → 📚 KNW, proceed to Step 7`
- **Step 6 Update Traces**: Changed `set final status` → `set status per verdict`. Changed `mark as ✅ DONE` → `mark as 📚 KNW (not ✅ DONE yet)`
- **Added Step 7: Knowledge Capture (KNW)**: Full orchestration — run tfw-docs, conditionally run tfw-knowledge, mark both in REVIEW §4, transition to DONE when both set

## 2. Changes List

| # | File | Lines Changed | Description |
|---|------|---------------|-------------|
| 1 | `KNOWLEDGE.md` | -15 | Removed §0 Philosophy & Principles section |
| 2 | `.tfw/workflows/knowledge.md` | -4/+3 | Stripped §1/§2 writes from Phase 4, updated Output header |
| 3 | `.tfw/workflows/docs.md` | +10, +1/-1 | Added Scope + Orchestration sections. Fixed checklist #5 orphaned §0 ref |
| 4 | `.tfw/conventions.md` | +2/-1 | Added KNW to pipeline diagram, status table, APPROVE verdict |
| 5 | `.tfw/glossary.md` | +4/-2 | Updated pipeline diagram, status count, added KNW definition |
| 6 | `.tfw/PROJECT_CONFIG.yaml` | +4 | Added KNW status entry between REV and DONE |
| 7 | `README.md` | +2/-2 | Updated Key Concepts pipeline + status legend |
| 8 | `.tfw/templates/REVIEW.md` | +1 | Added tfw-knowledge marker in §4 Traces Updated |
| 9 | `.tfw/workflows/review.md` | +12/-3 | Updated Step 5/6, added Step 7 (KNW transition) |
| 10 | `docs/scripts/test_gen_docs.py` | +3/-2 | Fixed `init.md` → `quickstart.md` in 2 tests + added missing `compilable_contract.md` fixture |

## 3. Test Results

- **Build gate**: No build command configured (`echo "configure your verify command"`)
- **gen_docs.py tests**: **68 passed, 0 failed** (after fixing pre-existing test failures — see §8 Deviation #3)
- **Manual verification**: All 11 files reviewed after modification. All acceptance criteria checked below

## 4. Acceptance Criteria Verification

| # | Criterion | Status |
|---|-----------|--------|
| 1 | tfw-knowledge Phase 4 has NO mention of §1 or §2 writes | ✅ Verified — Phase 4 now only writes §4 + has explicit ⚠️ warning |
| 2 | tfw-knowledge header Output mentions only knowledge/, KNOWLEDGE.md §4, knowledge_state.yaml | ✅ Verified |
| 3 | tfw-docs has explicit Scope section with writes/does-not-write | ✅ Verified — Scope section added after Prerequisites |
| 4 | tfw-docs has Orchestration section recommending tfw-knowledge when FC exist | ✅ Verified — Orchestration section added after "After Update" |
| 5 | KNOWLEDGE.md has no §0 section | ✅ Verified — file starts at §1 Architecture Map |
| 6 | All P1-P10 from §0 verified present elsewhere | ✅ Verified — mapping in TS Step 1 confirmed all 8 principles have homes |
| 7 | Pipeline diagram in conventions.md shows 📚 KNW between REV and DONE | ✅ Verified |
| 8 | Pipeline diagram in glossary.md shows KNW + count says "9 statuses" | ✅ Verified |
| 9 | KNW entry exists in PROJECT_CONFIG.yaml tfw.statuses | ✅ Verified — between REV and DONE, role: coordinator |
| 10 | README.md status legend includes KNW | ✅ Verified — both Key Concepts and status legend updated |
| 11 | REVIEW template §4 has tfw-knowledge marker | ✅ Verified — added after existing tfw-docs marker |
| 12 | review.md has Step 7 for KNW transition | ✅ Verified — full orchestration with tfw-docs + tfw-knowledge |

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `KNOWLEDGE.md` | 37 | naming | `KNOWLEDGE.md` description in §1 Architecture Map says "Updated via `tfw-docs` workflow" — correct after this fix, but also mentions "optional" — could be clarified post-rename |

> Observations #1 and #2 from original RF were fixed post-RF (user-requested). See §8 Deviations #3 and #4.

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | tfw-docs and tfw-knowledge had a structural collision: both wrote to KNOWLEDGE.md §1/§2. Root cause was tfw-knowledge Phase 4 encroaching on tfw-docs territory. Fix: exclusive write territories with explicit warnings | HL-TFW-32 §2.1, this RF | High |

## 7. Strategic Insights (Execution)

No strategic insights captured — execution was mechanical (spec-to-implementation, no user interaction during execution).

## 8. Deviations from TS

| # | TS instruction | What I did | Justification |
|---|----------------|------------|---------------|
| 1 | TS doesn't mention updating review.md Step 5 verdict text | Updated Step 5 from `→ ✅ DONE` to `→ 📚 KNW, proceed to Step 7` | Without this change, Step 5 and Step 7 would contradict each other. Agents following Step 5 literally would skip Step 7. ONB Recommendation #1 |
| 2 | TS doesn't mention updating review.md Step 6 text | Updated `set final status` → `set status per verdict` and `mark as ✅ DONE` → `mark as 📚 KNW` | Same as above — Step 6 needed consistency with new KNW flow |
| 3 | Out of TS scope: test_gen_docs.py | Fixed `init.md` → `quickstart.md` in 2 test fixtures + added missing `compilable_contract.md`. 66/68 → 68/68 | User-requested. Pre-existing tech debt from TFW-31 |
| 4 | Out of TS scope: docs.md checklist #5 | Changed `KNOWLEDGE.md \| Philosophy / Rules` → `conventions.md \| Design Rules / relevant section` | User-requested. Orphaned reference caused by §0 removal in Step 2 |

---

*RF — TFW-32 / Phase A: Methodology Pipeline Fixes | 2026-04-10*
