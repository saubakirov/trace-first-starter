# TS — {PREFIX}-{N} / Phase {X}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {author}
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-{PREFIX}-{N}](path-to-HL)

---

## 1. Objective
{One paragraph: what this phase delivers and why it matters.}

## 2. Scope

### In Scope
- {what will be done}

### Out of Scope
- {what will NOT be done in this phase}

## 3. Principles Check

> Map HL §7 principles to specific AC items. Each principle MUST have at least one AC enforcing it.
> If a principle has no applicable AC — mark as "N/A" with reason.

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | {principle name} | AC-{N} | {how verified} |
| P2 | {principle name} | N/A | {reason not applicable} |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `path/to/file` | CREATE / MODIFY / DELETE | {description} |

**Budget:** {N} new files, {M} modifications. Defaults: max {max_files} files, max {max_new} new, max {max_loc} LOC.

## 5. Acceptance Criteria

> Describe WHAT the result should achieve, not HOW to implement it.
> Each AC must be independently verifiable. Mark dependencies with `[depends: AC-X]`.
> Executor verifies dependent ACs in order — a dependent AC cannot pass before its prerequisite.

### AC-1: {title}
{What the result should achieve — 1-2 sentences.}
- [ ] {Verifiable criterion}
- [ ] {Verifiable criterion}
Gate: {How to verify — a command, query, visual check, or stakeholder confirmation}

### AC-2: {title}  [depends: AC-1]
{What the result should achieve — 1-2 sentences.}
- [ ] {Verifiable criterion}
Gate: {How to verify}

## 6. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF.
- {Relevant context: where things are, what patterns exist, what constraints apply}

## 7. Definition of Failure

- ❌ {Condition that causes RF rejection — hard reject, not a warning}

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| {risk} | {mitigation} |

## 9. Cross-Phase Modifications (multi-phase only)

> Include only for multi-phase tasks. Omit section entirely for single-phase tasks.

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `path/to/file` | Phase {X} | {what to watch for} |

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2. Build script resolves to hyperlinks.

---

*TS — {PREFIX}-{N} / Phase {X}: {Title} | YYYY-MM-DD*
