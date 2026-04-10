# TS — TFW-32 / Phase A: Methodology Pipeline Fixes

> **Date**: 2026-04-10
> **Author**: AI (Coordinator)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> **Phase HL**: [HL Phase A](HL__PhaseA__methodology_pipeline.md)

---

## 1. Objective

Fix the docs-vs-knowledge workflow collision, add `📚 KNW` status to the task pipeline, remove orphaned KNOWLEDGE.md §0, and add REVIEW markers for docs/knowledge tracking. After this phase, each workflow has exclusive write territory and the pipeline visibly tracks knowledge capture.

## 2. Scope

### In Scope
- Strip §1/§2 writes from tfw-knowledge Phase 4
- Clarify tfw-docs scope (§1-§3 + TECH_DEBT.md, explicit out-of-scope)
- Remove KNOWLEDGE.md §0 content (verified: no information loss)
- Add `📚 KNW` status to conventions.md, PROJECT_CONFIG.yaml, glossary.md
- Add `tfw-docs` and `tfw-knowledge` markers to REVIEW template §4
- Update review.md workflow: KNW transition, markers reference
- Update tfw-docs: orchestration note (recommend tfw-knowledge when FC exist)
- Update pipeline diagrams in conventions.md, glossary.md, README.md

### Out of Scope
- KNOWLEDGE.md rename to DOCS.md (deferred — see HL §3)
- Renumbering §1-§4 (costly, breaks references)
- Template changes for naming (Phase B)
- Multi-iteration research formalization (Phase C)

## 3. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/workflows/knowledge.md` | MODIFY | Strip §1/§2 writes from Phase 4. Update header Output line |
| `.tfw/workflows/docs.md` | MODIFY | Add explicit scope + out-of-scope. Add orchestration note |
| `.tfw/workflows/review.md` | MODIFY | Add Step 6.5: KNW transition. Reference docs/knowledge markers |
| `.tfw/templates/REVIEW.md` | MODIFY | Add tfw-docs and tfw-knowledge markers in §4 Traces Updated |
| `.tfw/conventions.md` | MODIFY | §5: add KNW status to pipeline diagram + status table |
| `.tfw/glossary.md` | MODIFY | Add KNW definition. Update pipeline diagram. Update status count |
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Add KNW status to tfw.statuses list |
| `KNOWLEDGE.md` | MODIFY | Remove §0 content (keep §1-§4 intact) |
| `README.md` | MODIFY | Update status legend line (add KNW) |

**Budget:** 0 new files, 9 modifications. Within limits: max 14 files, max 12 modified, max 1200 LOC.

## 4. Detailed Steps

### Step 1: Verify §0 → knowledge/philosophy.md mapping

Before removing §0, verify each principle has a home:

| §0 Principle | Where it lives |
|-------------|---------------|
| P1 (Traces over code) | knowledge/philosophy.md F6, F8, F10. `.tfw/README.md` Values |
| P2 (Index don't duplicate) | conventions.md principle. TFW-5 HL §7 |
| P3 (Philosophy stays rich) | knowledge/philosophy.md F9 (brand character: doctrinal) |
| P5 (Meta-project awareness) | KNOWLEDGE.md §1 Architecture Map (meta-project entry) |
| P7 (Self-review is not) | conventions.md §15 Role Lock. D13 |
| P8 (Research ≠ passive) | conventions.md §8. D14, D21 |
| P9 (Coordinator quality) | plan.md Mindset. D21 |
| P10 (Knowledge by design) | knowledge/philosophy.md F6, F8 |

**All covered.** Proceed with §0 removal.

### Step 2: Update KNOWLEDGE.md — remove §0

Remove the entire `## 0. Philosophy & Principles` section (lines with P1-P10 table). Keep the horizontal rule. §1-§4 numbering stays unchanged.

**Before:**
```markdown
## 0. Philosophy & Principles
| # | Principle | Source |
...
---
## 1. Architecture Map
```

**After:**
```markdown
## 1. Architecture Map
```

### Step 3: Update tfw-knowledge workflow (knowledge.md)

**3a.** Change header `Output` line:
```
Before: > **Output:** Updated `KNOWLEDGE.md` §1/§2/§4, topic files in `knowledge/`, updated `knowledge_state.yaml`
After:  > **Output:** Updated `knowledge/` topic files, `KNOWLEDGE.md` §4 (index), `knowledge_state.yaml`
```

**3b.** In Phase 4 (Update), strip items 1-2 that write to §1/§2:
```
Before Phase 4:
1. Review existing facts for staleness...
2. Update KNOWLEDGE.md:
   - §1 Architecture Decisions: add new D{N} entries...
   - §2 Key Artifacts: add entry for closed tasks
   - §4 Project Facts: update category counts...
3. Update knowledge_state.yaml...

After Phase 4:
1. Review existing facts for staleness...
2. Update KNOWLEDGE.md §4 (Project Facts): update category counts + links to topic files
   > ⚠️ Do NOT write to §1 or §2 — those belong to `/tfw-docs` (Combination scope)
3. Update knowledge_state.yaml...
```

### Step 4: Update tfw-docs workflow (docs.md)

**4a.** Add scope declaration after Prerequisites:

```markdown
## Scope

**Writes to:** KNOWLEDGE.md §1 (Architecture Map), §2 (Key Artifacts), §3 (Legacy & Deprecation), TECH_DEBT.md
**Does NOT write to:** `knowledge/` topic files, KNOWLEDGE.md §4 (Project Facts index) — those belong to `/tfw-knowledge`
```

**4b.** Add orchestration note after "After Update":

```markdown
## Orchestration

After tfw-docs completes:
- IF Fact Candidates exist in RF, REVIEW, or RES → recommend: "Run `/tfw-knowledge` to consolidate fact candidates"
- IF no Fact Candidates → mark `tfw-knowledge: N/A` in REVIEW
```

### Step 5: Add `📚 KNW` status

**5a.** `conventions.md` §5 — update pipeline diagram:
```
Before: ⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
After:  ⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE
```

Add to status table:
```
| 📚 KNW | Knowledge capture: tfw-docs + tfw-knowledge applied |
```

Update status count in diagram comment if any.

**5b.** `glossary.md` — update pipeline diagram and status count:
```
Before: 8 statuses: TODO, HL_DRAFT, RES, TS_DRAFT, ONB, RF, REV, DONE (+ BLOCKED). RES is optional.
After:  9 statuses: TODO, HL_DRAFT, RES, TS_DRAFT, ONB, RF, REV, KNW, DONE (+ BLOCKED). RES and KNW are optional.
```

Add KNW definition in glossary:
```markdown
### KNW (Knowledge Capture)
Post-review status indicating docs and knowledge workflows have been applied. Triggered after REVIEW ✅ APPROVE. Markers in REVIEW: `tfw-docs: Applied/N/A`, `tfw-knowledge: Applied/N/A`. Both markers set → status transitions to DONE. → conventions.md §5
```

**5c.** `PROJECT_CONFIG.yaml` — add KNW entry to tfw.statuses:
```yaml
    - id: KNW
      emoji: "📚"
      description: "Knowledge capture (tfw-docs + tfw-knowledge)"
      role: coordinator
```
Insert between REV and DONE entries.

**5d.** `README.md` — update status legend:
```
Before: Statuses: ⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE | ❌ BLOCKED
After:  Statuses: ⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE | ❌ BLOCKED
```

Also update `Key Concepts` line:
```
Before: TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE` (RES optional)
After:  TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE` (RES, KNW optional)
```

### Step 6: Add REVIEW markers to template

In `.tfw/templates/REVIEW.md` §4 Traces Updated, add two markers:

```markdown
## 4. Traces Updated

- [ ] README Task Board — status updated
- [ ] HL status — updated if phase completes
- [ ] PROJECT_CONFIG.yaml — initial_seq incremented if needed
- [ ] Other project files — checked for stale info
- [ ] tfw-docs: {Applied — updated Sections X, Y / N/A (minor)}
- [ ] tfw-knowledge: {Applied / N/A / Deferred to batch}
```

**Note:** The `tfw-docs` marker already exists in the current template (line 51). Only `tfw-knowledge` marker needs to be **added**.

### Step 7: Update review.md workflow

After Step 6 "Update Traces", add a new section:

```markdown
## Step 7: Knowledge Capture (KNW)

After ✅ APPROVE verdict:
1. Run `/tfw-docs` — update KNOWLEDGE.md §1-§3 + TECH_DEBT.md
2. If Fact Candidates exist in RF/REVIEW/RES → run `/tfw-knowledge`
3. Mark both in REVIEW §4: `tfw-docs: Applied/N/A` | `tfw-knowledge: Applied/N/A`
4. When both markers are set → update Task Board status to ✅ DONE

For trivial tasks: reviewer pre-marks both as N/A during review.
```

## 5. Acceptance Criteria

- [ ] tfw-knowledge Phase 4 has NO mention of §1 or §2 writes
- [ ] tfw-knowledge header Output mentions only `knowledge/`, `KNOWLEDGE.md §4`, `knowledge_state.yaml`
- [ ] tfw-docs has explicit Scope section with writes/does-not-write
- [ ] tfw-docs has Orchestration section recommending tfw-knowledge when FC exist
- [ ] KNOWLEDGE.md has no §0 section
- [ ] All P1-P10 from §0 verified present elsewhere (mapping in Step 1)
- [ ] Pipeline diagram in conventions.md shows `📚 KNW` between REV and DONE
- [ ] Pipeline diagram in glossary.md shows KNW + count says "9 statuses"
- [ ] KNW entry exists in PROJECT_CONFIG.yaml tfw.statuses (between REV and DONE)
- [ ] README.md status legend includes KNW
- [ ] REVIEW template §4 has `tfw-knowledge` marker
- [ ] review.md has Step 7 for KNW transition

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| §0 removal loses information | Pre-verified mapping (Step 1). All principles live elsewhere |
| KNW status not referenced by any workflow | Step 7 in review.md + Orchestration in docs.md ensure KNW is active |
| Existing REVIEW files missing markers | Backward compatible — markers are new, old reviews unaffected |

> **Cross-references**: RES1 D1, D3, D6, D7, D8. HL-TFW-32 §4 Phase A.

---

*TS — TFW-32 / Phase A: Methodology Pipeline Fixes | 2026-04-10*
