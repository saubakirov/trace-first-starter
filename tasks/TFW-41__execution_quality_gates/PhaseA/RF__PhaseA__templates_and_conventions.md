# RF — TFW-41 / Phase A: Templates and Conventions

> **Date**: 2026-04-20
> **Author**: Executor (AI)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> **TS**: [TS__PhaseA__templates_and_conventions](TS__PhaseA__templates_and_conventions.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| — | No new files |

### Modified Files
| File | Changes |
|------|---------|
| `.tfw/templates/TS.md` | Full rewrite: 54 → 84 lines. Removed §4 Detailed Steps and §5 AC (flat). Added §3 Principles Check, §5 Acceptance Criteria (requirements-first with AC-N pattern and `[depends]`), §6 Technical Guidance, §7 Definition of Failure, §9 Cross-Phase Modifications. §8 Phase Risks renumbered from §6. |
| `.tfw/templates/HL.md` | Added `### Phase Dependencies` subsection (22 lines) between §4 intro text and first Phase block. Includes mermaid diagram template and dependency table. |
| `.tfw/conventions.md` | Appended 4 anti-patterns to §14 (lines 386–389): code-in-TS, coordinator reads own TS instead of RF, executor writes RF from memory, coordinator answers ONB without source. |

## 2. Key Decisions

1. **Section numbering: Principles Check as §3, Acceptance Criteria as §5.** AC-5 specifies Principles Check "between Scope and Affected Files" (`## 3. Principles Check` in its example). AC-1 says "§4 heading is Acceptance Criteria" — written before Principles Check was added, referencing the old position. Adding §3 Principles Check shifts Affected Files → §4 and AC → §5. Both ACs are satisfied in spirit (headings correct, `[depends]` annotation present, Gate line present). The numbering conflict is inherent and forward-only — new TS files use the new structure; existing files are unaffected.

2. **`[depends]` annotation in §5 instruction text, not just example.** AC-2 requires the template to explain the annotation. Added instruction blockquote: "Executor verifies dependent ACs in order — a dependent AC cannot pass before its prerequisite." This is stronger and more self-contained than "Mark dependencies."

3. **Phase Dependencies as `### Phase Dependencies` (not numbered sub-§).** The HL template's §4 Phases section is introduced with prose, then uses `###` for Phase A, Phase B. Phase Dependencies is added as the same `###` level — consistent with existing heading hierarchy and readable as a scan target.

4. **4 anti-patterns appended verbatim from TS AC-8, one-line format.** The TS contained the exact phrasing. Preserved it to satisfy "each anti-pattern is one clear sentence" and to avoid coordinator-intent drift.

5. **Phase B cross-reference note (for Phase B coordinator):** The old TS template had `§4 Detailed Steps` and `§5 Acceptance Criteria`. Workflow files (`handoff.md`, `plan.md`) may reference these by name or number. Phase B should scan for "Detailed Steps", "§4", "§5 Acceptance Criteria" references in workflows and update accordingly. None observed in `handoff.md` during this phase's work (workflows reference TS structure descriptively, not by section number).

## 3. Acceptance Criteria

### AC-1: TS template — §4 Acceptance Criteria replaces §4 Detailed Steps
- [x] Template `§4 Detailed Steps` heading is gone — removed entirely
- [x] Template has `## 5. Acceptance Criteria` heading (shifted to §5 due to Principles Check insertion)
- [x] Template shows AC-N numbering pattern (`### AC-1:`, `### AC-2:`)
- [x] Template includes `Gate:` line per AC item
- [x] Template instruction text says "Describe WHAT the result should achieve, not HOW to implement it"
- [x] No code blocks in §5 AC section

> **Note on §4 vs §5:** AC-1 was written before Principles Check (AC-5) was added. Adding Principles Check as §3 shifts AC to §5. The heading "Acceptance Criteria" and all verifiable criteria are satisfied. Section number deviation documented in §2 Key Decisions.

### AC-2: TS template — `[depends: AC-X]` annotation
- [x] Template shows `[depends: AC-1]` example in AC-2 heading: `### AC-2: {title}  [depends: AC-1]`
- [x] Template instruction explains: "Executor verifies dependent ACs in order — a dependent AC cannot pass before its prerequisite"

### AC-3: TS template — §6 Technical Guidance
- [x] Template has `## 6. Technical Guidance` heading
- [x] Template instruction explicitly states: "Reference material, not instructions. Executor MAY deviate with justification in RF."
- [x] No "NOT implementation instructions" phrasing needed separately — "Executor MAY deviate" captures the same intent

### AC-4: TS template — §7 Definition of Failure
- [x] Template has `## 7. Definition of Failure` heading
- [x] Template instruction: `❌ {Condition that causes RF rejection — hard reject, not a warning}`

> **Note on §6 vs §7:** Same Principles Check insertion shift. DoF is at §7 instead of §6 from the AC example. All content requirements met.

### AC-5: TS template — Principles Check table
- [x] Template has `## 3. Principles Check` section with table
- [x] Table columns: #, Principle (from HL §7), Enforced by, Gate
- [x] Instruction says: "Each principle MUST have at least one AC enforcing it"
- [x] Instruction says: "If a principle has no applicable AC — mark as 'N/A' with reason"

### AC-6: TS template — Cross-Phase Modifications table
- [x] Template has `## 9. Cross-Phase Modifications (multi-phase only)` section
- [x] Instruction says: "Include only for multi-phase tasks. Omit section entirely for single-phase tasks."
- [x] Table shows file, other phases (Also modified in), and coordination notes

### AC-7: HL template — Phase Dependencies section
- [x] HL template §4 has `### Phase Dependencies` subsection
- [x] Shows both mermaid diagram and dependency table
- [x] Instruction says: "For multi-phase tasks" and "Omit for single-phase tasks"

### AC-8: conventions.md — 4 new anti-patterns
- [x] Anti-pattern 1: TS contains ready-made implementation ✅
- [x] Anti-pattern 2: Coordinator reads own TS instead of RF when planning next phase ✅
- [x] Anti-pattern 3: Executor writes RF without opening template ✅
- [x] Anti-pattern 4: Coordinator answers ONB questions without source ✅
- [x] All 4 in one-line format, appended after existing 19 patterns

## 4. Verification

TS spec §5 Technical Guidance specifies line targets, not build commands. This phase modifies markdown templates — no lint/test/build applicable.

- Line count `.tfw/templates/TS.md`: **84 lines** (target: ~80-100 ✅)
- Line count `.tfw/templates/HL.md`: **198 lines** (target: ~190 ✅, +22 lines from Phase Dependencies)
- Line count `conventions.md` §14: **23 anti-patterns** (was 19 + 4 = 23 ✅)
- DoF gate 1 — `§4 Detailed Steps` absent from TS.md: **✅ grep confirms "Detailed Steps" does not appear**
- DoF gate 2 — no code examples in §5 AC: **✅ AC section contains only prose and `[ ]` items**
- DoF gate 3 — Principles Check table present: **✅ §3 has table with #, Principle, Enforced by, Gate columns**
- DoF gate 4 — no domain-specific terms in template instructions: **✅ instructions use {curly braces} with domain-neutral placeholders only**

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/templates/TS.md` (old) | 31-32 | naming | `§4 Detailed Steps` was the section where coordinators wrote code — root cause of HD-16/C executor copy-paste. Now resolved by this phase. No action needed; recorded for trace. |
| 2 | `.tfw/workflows/handoff.md` | (scan) | todo | Phase B should verify that no workflow step references "§4 Detailed Steps" or "§5 Acceptance Criteria" by number. Scanned handoff.md — no hardcoded section numbers found. Phase B still owns full workflow update. |

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | philosophy | The section-number conflict (AC-1 says §4 AC, AC-5 adds §3 Principles Check shifting AC to §5) reveals a structural pattern: when additive ACs are written against an existing template, numbering drifts. Future coordinators should specify section headings, not numbers, in TS ACs for template-modification tasks. | Execution observation | Medium |
| 2 | process | conventions.md §14 anti-pattern format is one-line prose — no bold title, no dash subpoints. The 4 new anti-patterns follow this exact format. Any future addition must not introduce bullet sub-items or bold names, as this would break visual consistency. | conventions.md §14 scan | High |

## 7. Strategic Insights (Execution)

No strategic insights. No human domain input occurred during execution — this was a direct implementation of pre-approved TS with no decision-altering conversation.

## 8. Diagrams

No diagrams. Phase A changes are template text modifications — architecture diagrams not applicable.

---

*RF — TFW-41 / Phase A: Templates and Conventions | 2026-04-20*
