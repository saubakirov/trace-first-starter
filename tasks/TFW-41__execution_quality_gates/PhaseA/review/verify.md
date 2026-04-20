# Review Stage 2: Verify — TFW-41 / Phase A

> **Mode**: docs
> **Min verify ratio**: 0.42 → ⌈3 × 0.42⌉ = 2 files minimum. Verified all 3 (escalated to 100% proactively given scope size).

---

## File Existence Check

| File (claimed) | Exists | Path confirmed |
|----------------|--------|----------------|
| `.tfw/templates/TS.md` | ✅ | Opened, 84 lines |
| `.tfw/templates/HL.md` | ✅ | Opened, 198 lines |
| `.tfw/conventions.md` | ✅ | Opened, 430 lines |

---

## Verification Log

### TS.md — Full verification against all 6 AC items

| AC | Claim | Verified | Evidence |
|----|-------|----------|---------|
| AC-1: §4 AC replaces §4 Detailed Steps | `§4 Detailed Steps` gone; `Acceptance Criteria` present | ✅ | `TS.md` L39: `## 5. Acceptance Criteria` (shifted to §5); L21 has no "Detailed Steps" anywhere in file. DoF gate 1 met. |
| AC-1: AC-N pattern present | `### AC-1:` pattern | ✅ | L45: `### AC-1: {title}`, L51: `### AC-2: {title}  [depends: AC-1]` |
| AC-1: Gate line per AC | Gate present | ✅ | L49: `Gate: {How to verify...}`, L54: `Gate: {How to verify}` |
| AC-1: Instruction text says WHAT not HOW | Present | ✅ | L41: `Describe WHAT the result should achieve, not HOW to implement it.` |
| AC-1: No code blocks in AC section | Verified | ✅ | `## 5. Acceptance Criteria` section (L39–L54): prose + checklist items only. No fenced code blocks. DoF gate 2 met. |
| AC-2: `[depends: AC-1]` example present | Present | ✅ | L51: `### AC-2: {title}  [depends: AC-1]` |
| AC-2: Template instruction explains dependency | Present | ✅ | L43: `Executor verifies dependent ACs in order — a dependent AC cannot pass before its prerequisite.` |
| AC-3 (→ §6 Technical Guidance): heading present | Present | ✅ | L56: `## 6. Technical Guidance` |
| AC-3: Instruction says "Reference material, not instructions. Executor MAY deviate" | Present | ✅ | L58: `> Reference material, not instructions. Executor MAY deviate with justification in RF.` |
| AC-4 (→ §7 DoF): heading present | Present | ✅ | L61: `## 7. Definition of Failure` |
| AC-4: Rejection condition format | Present | ✅ | L63: `- ❌ {Condition that causes RF rejection — hard reject, not a warning}` |
| AC-5: Principles Check table present | Present | ✅ | L21: `## 3. Principles Check`; L26-L29: table with #, Principle, Enforced by, Gate columns. DoF gate 3 met. |
| AC-5: Instruction — each principle MUST have at least one AC | Present | ✅ | L23: `Each principle MUST have at least one AC enforcing it.` |
| AC-5: Instruction — N/A with reason | Present | ✅ | L24: `If a principle has no applicable AC — mark as "N/A" with reason.` |
| AC-6: Cross-Phase Modifications section | Present | ✅ | L71: `## 9. Cross-Phase Modifications (multi-phase only)` |
| AC-6: Instruction — omit for single-phase | Present | ✅ | L73: `Include only for multi-phase tasks. Omit section entirely for single-phase tasks.` |
| AC-6: Table shows file, other phases, coordination note | Present | ✅ | L75-L77: table with File, Also modified in, Coordination note |

**TS.md verdict: All AC items verified against actual file content. No discrepancies.**

---

### HL.md — Verification for AC-7

| Claim | Verified | Evidence |
|-------|----------|---------|
| `### Phase Dependencies` subsection in §4 | ✅ | L54: `### Phase Dependencies` (under `## 4. Phases`) |
| Mermaid diagram template present | ✅ | L61-L67: fenced mermaid block with graph LR showing A→B, A→C, B→D, C→D |
| Dependency table present | ✅ | L69-L74: table with Phase, Depends on, Shared files, Can run in parallel with |
| Instruction says "For multi-phase tasks" | ✅ | L56: `> For multi-phase tasks: visualize dependencies and shared files.` |
| Instruction says "Omit for single-phase" | ✅ | L57: `> Omit for single-phase tasks.` |
| Line count matches claim (~190) | ✅ | 198 lines — within target range, +22 lines from Phase Dependencies |

**HL.md verdict: AC-7 fully satisfied.**

---

### conventions.md §14 — Verification for AC-8

| Claimed anti-pattern | Present | Line | Format correct (one-line prose) |
|---------------------|---------|------|---------------------------------|
| TS contains ready-made implementation | ✅ | L386 | ✅ one-line, no sub-bullets |
| Coordinator reads own TS instead of RF when planning next phase | ✅ | L387 | ✅ one-line, no sub-bullets |
| Executor writes RF without opening template | ✅ | L388 | ✅ one-line, no sub-bullets |
| Coordinator answers ONB questions without source | ✅ | L389 | ✅ one-line, no sub-bullets |
| Total count | 23 items | L367-L389 | ✅ was 19, now 23 (RF claims +4 = 23 ✅) |
| Appended after existing (not reordered) | ✅ | L386-L389 are the last 4 items | ✅ |

**conventions.md verdict: AC-8 fully satisfied.**

---

### Line Count Claims

| File | RF Claim | Actual | Match |
|------|----------|--------|-------|
| `TS.md` | 84 lines | 84 lines | ✅ |
| `HL.md` | 198 lines | 198 lines | ✅ |
| `conventions.md` §14 | 23 anti-patterns | 23 items (L367-L389) | ✅ |

---

### DoF Gate Checks (from TS §6)

| Gate | Status | Evidence |
|------|--------|---------|
| ❌ TS template still has `§4 Detailed Steps` | PASSED (gate not triggered) | TS.md has no "Detailed Steps" anywhere |
| ❌ TS template contains code examples in §4 AC section | PASSED | §5 AC section is prose + `[ ]` only |
| ❌ Principles Check table absent | PASSED | `## 3. Principles Check` with full table present |
| ❌ Domain-specific terminology in template instructions | PASSED | All instructions use `{curly brace}` placeholders; no "code", "CSS", "API" literals in instruction text |

---

### Section Numbering Deviation (AC-1 note)

RF §2 Key Decision #1 explains: AC-1 was written expecting `## 4. Acceptance Criteria`. After Principles Check was added as `## 3`, AC became `## 5`. The RF acknowledges this deviation explicitly. The **heading text** ("Acceptance Criteria") matches; the **number** does not match AC-1's example code block. Reviewing the TS AC-1 code block:

```
## 4. Acceptance Criteria  ← TS example shows §4
```

But the template has `## 5. Acceptance Criteria`. This is a **documented deviation**, not a silent one. The TS AC-1 criterion list checks heading content ("Acceptance Criteria"), pattern (AC-N), Gate line, WHAT/HOW instruction, no code blocks — all satisfied. The number in the code example is illustrative, not a hard constraint (TS does not say "the number must be 4"). 

**Assessment:** This deviation is acceptable. The TS did not write "section number must be 4" as a verifiable criterion — it wrote the code block as an example of the structure. The executor correctly notes this in Key Decisions and delivers all verifiable criteria.

---

### Knowledge Citations Verified

RF §7 states no strategic insights (no human domain input). RF §6 has 2 fact candidates — source is execution observation and conventions.md scan, both traceable.

---

## Self-Check Gate

- [x] At least ⌈3 × 0.42⌉ = 2 files verified — verified all 3 (100%)
- [x] Document structure checked against TS spec (headings, required sections)
- [x] 2-3 key claims spot-checked — all 8 AC items verified against actual files
- [x] Section numbering deviation assessed against actual TS criterion text (not just example code)
- [x] No judgment made yet — pure evidence gathering

---

*verify.md — TFW-41 / Phase A review | 2026-04-20*
