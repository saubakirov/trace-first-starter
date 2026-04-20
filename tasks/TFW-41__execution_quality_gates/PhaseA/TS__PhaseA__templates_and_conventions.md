# TS — TFW-41 / Phase A: Templates and Conventions

> **Date**: 2026-04-20
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)

---

## 1. Objective

Rewrite the TS template from procedural (§4 Detailed Steps) to requirements-first (§4 Acceptance Criteria, §5 Technical Guidance, §6 Definition of Failure). Add Principles Check table and `[depends: AC-X]` annotation. Add Phase Dependencies section to HL template. Add 4 anti-patterns to conventions. This phase creates the foundation — all subsequent phases reference these templates.

## 2. Scope

### In Scope
- Rewrite `.tfw/templates/TS.md` — new structure
- Modify `.tfw/templates/HL.md` — add Phase Dependencies section
- Modify `.tfw/conventions.md` §14 — add 4 anti-patterns

### Out of Scope
- Workflow changes (Phase B)
- Research template changes (Phase C)
- Glossary and adapter sync (Phase D)

## 3. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/templates/TS.md` | MODIFY | Rewrite: §4 → AC, §5 → Technical Guidance, add §6 Definition of Failure, add Principles Check, add `[depends]`, add Cross-Phase Modifications |
| `.tfw/templates/HL.md` | MODIFY | Add Phase Dependencies section (mermaid + table) to §4 |
| `.tfw/conventions.md` | MODIFY | Add 4 anti-patterns to §14 |

**Budget:** 0 new files, 3 modifications. Defaults: max 14 files, max 8 new, max 1200 LOC.

## 4. Acceptance Criteria

### AC-1: TS template — §4 Acceptance Criteria replaces §4 Detailed Steps

The current `§4 Detailed Steps` section is replaced with `§4 Acceptance Criteria`. Structure:

```markdown
## 4. Acceptance Criteria

### AC-1: {title}
{What the result should achieve — 1-2 sentences.}
- [ ] {Verifiable criterion}
- [ ] {Verifiable criterion}
Gate: {How to verify — a command, query, visual check, or stakeholder confirmation}
```

- [ ] Template §4 heading is "Acceptance Criteria", not "Detailed Steps"
- [ ] Template shows AC-N numbering pattern
- [ ] Template includes Gate line per AC item
- [ ] Template instruction text says "describe WHAT, not HOW"
- [ ] No code blocks in template §4 (code examples belong in §5)

### AC-2: TS template — `[depends: AC-X]` annotation  [depends: AC-1]

AC items with dependencies on other AC items are explicitly annotated:

```markdown
### AC-3: Report reflects transformed data  [depends: AC-1]
```

- [ ] Template shows `[depends: AC-X]` example in at least one AC item
- [ ] Template instruction explains: "Mark dependencies. Executor verifies dependent ACs in order."

### AC-3: TS template — §5 Technical Guidance replaces implementation details

The current template has no explicit Technical Guidance section. New §5:

```markdown
## 5. Technical Guidance
> Reference material, not instructions. Executor MAY deviate with justification in RF.
- {Relevant context: where things are, what patterns exist, what constraints apply}
```

- [ ] Template §5 heading is "Technical Guidance"
- [ ] Template instruction explicitly states: "NOT implementation instructions. Executor decides HOW."
- [ ] Template instruction states: "Executor MAY deviate with justification in RF."

### AC-4: TS template — §6 Definition of Failure  [depends: AC-1]

New section after Technical Guidance:

```markdown
## 6. Definition of Failure
- ❌ {Condition that causes RF rejection}
```

- [ ] Template §6 heading is "Definition of Failure"
- [ ] Template instruction: "Hard reject conditions — if any of these are true, RF is rejected."

### AC-5: TS template — Principles Check table  [depends: AC-1]

New section between Scope and Affected Files:

```markdown
## 3. Principles Check

> Map HL §7 principles to specific AC items. Each principle MUST have at least one AC enforcing it.
> If a principle has no applicable AC — mark as "N/A" with reason.

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | {principle name} | AC-{N} | {how verified} |
| P2 | {principle name} | N/A | {reason not applicable} |
```

- [ ] Template has "Principles Check" section with table
- [ ] Table columns: #, Principle, Enforced by, Gate
- [ ] Instruction says: "Each principle MUST have at least one AC enforcing it"
- [ ] Instruction says: "If not applicable — mark N/A with reason"

### AC-6: TS template — Cross-Phase Modifications table  [depends: AC-1]

For multi-phase tasks, new section:

```markdown
## 7. Cross-Phase Modifications (multi-phase only)

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `path/to/file` | Phase B | {what to watch for} |
```

- [ ] Template has "Cross-Phase Modifications" section
- [ ] Instruction says: "Include only for multi-phase tasks"
- [ ] Table shows file, other phases, and coordination notes

### AC-7: HL template — Phase Dependencies section

Add to HL template §4 Phases, before the first Phase:

```markdown
### Phase Dependencies

> For multi-phase tasks: visualize dependencies and shared files.

{mermaid graph or ASCII flow}

| Phase | Depends on | Shared files | Can run in parallel with |
|-------|-----------|--------------|-------------------------|
```

- [ ] HL template §4 has "Phase Dependencies" subsection
- [ ] Shows both mermaid/ASCII diagram and table
- [ ] Instruction says: "For multi-phase tasks"

### AC-8: conventions.md — 4 new anti-patterns  

Add to §14:

1. **TS contains ready-made implementation** — TS §4 must contain acceptance criteria, not code/steps. Implementation belongs to executor.
2. **Coordinator reads own TS instead of RF when planning next phase** — Before writing TS for Phase N, read RF of latest completed phase. Plan ≠ fact.
3. **Executor writes RF without opening template** — RF template must be opened before writing. Writing from memory drifts from required structure.
4. **Coordinator answers ONB questions without source** — When uncertain, coordinator must present options, not decide on behalf of stakeholder.

- [ ] All 4 anti-patterns present in conventions.md §14
- [ ] Each anti-pattern is one clear sentence
- [ ] Listed after existing anti-patterns (append, don't reorder)

## 5. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF.

- Current TS template is 54 lines. Target: ~80-100 lines (add structure, keep concise).
- Current HL template is 176 lines. Phase Dependencies adds ~15 lines. Target: ~190 lines.
- Current conventions.md §14 has 19 anti-patterns. Adding 4 → 23. Keep same one-line format.
- Section numbering shift in TS: current §5 (Acceptance Criteria) becomes part of §4. Current §6 (Phase Risks) shifts. Renumber accordingly.
- TS template should have template instruction text in `{curly braces}` following existing convention.
- The TS template's new §4 should NOT reference any specific domain (no code, no CSS, no API). Use domain-neutral examples like the analytics ETL example from HL §3.1.

## 6. Definition of Failure

- ❌ TS template still has `§4 Detailed Steps` heading → reject RF
- ❌ TS template contains code examples in §4 → reject RF (code belongs only in §5 Technical Guidance)
- ❌ Principles Check table is absent from template → reject RF
- ❌ Domain-specific terminology in template instructions (references to "code", "CSS", "API" instead of domain-neutral language) → reject RF

## 7. Phase Risks

| Risk | Mitigation |
|------|------------|
| TS section renumbering breaks cross-references in workflows | Phase B handles workflow updates — note current §-references for Phase B coordinator |
| Template becomes too long / too prescriptive | Budget: ~100 lines max. Instruction text uses `{curly braces}`, not full paragraphs |
| Existing projects using old TS format | Forward-only change — old TS files remain valid, new ones use new template |

> **Cross-references**: HL-TFW-41 §4 Phase A, DR1, DR6, HL §7 Principle 2 (Requirements, not implementation), Principle 6 (Domain-agnostic).

---

*TS — TFW-41 / Phase A: Templates and Conventions | 2026-04-20*
