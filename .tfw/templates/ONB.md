# ONB — {ID} / Phase {X}: {Title}

> **Current filename**: `ONB__{ID}.md` or `ONB__phase-{x}__{phase_slug}.md`; later rounds append to this file. Derive under `conventions.md` → `Artifact file naming`.

> **Date**: YYYY-MM-DD
> **Author**: {executor}
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-{ID}](path-to-HL)
> **TS**: [TS Phase {X}](path-to-TS)
> **Producer unit**: {actual native Executor address}
> **Parent Coordinator**: {status.md coordinator_route}
> **Activation / dispatch source**: {owner-direct activation or immutable dispatch ref}
> **Coordination authority**: {exact status.md coordination_authority}
> **Originating proposer**: {principal and unit, or `none`}

---

## 1. Understanding
{One-paragraph summary of what needs to be done and why}

## 2. Entry Points
{Key files and code areas relevant to the task}

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Blocking reason | Answer authority / event ref | Operational effect |
|---|---|---|---|---|
| 1 | {question} | {why work cannot proceed} | {task-local `gate_answer` ref or `pending`} | {what becomes permitted, or `none while pending`} |

The Executor owns this table. The answering authority appends `gate_answer`; no Coordinator or human
edits the Executor-owned ONB.

## 4. Recommendations (suggestions, not blocking)
1. {suggestion and rationale}

## 5. Risks Found (edge cases, potential issues not in TS)
1. {risk description}

## 6. Inconsistencies with Code (spec vs reality)
1. {what TS says} vs {what code actually does}

## 7. Knowledge Citations

> Executor: read coordinator's citations in HL §7.2. For each item:
> - Confirm you read it (link + item name)
> - State how you applied it OR why it doesn't apply to your work
> - Add any NEW items you found relevant that coordinator missed

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | {D-number or F-number from HL §7.2} | ✅ | {how applied or why N/A} | |

> For new projects where HL §7.2 says "No applicable knowledge items": write "No applicable knowledge items — confirmed."

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2. Build script resolves to hyperlinks.

### Material handover at this return

Apply `conventions.md` → `Knowledge handover`. Record producer/unit, source/epoch, inspected scope,
material or justified-none, uncertainty, continuation, and any unresolved owner/decision; do not
duplicate or replace the original source.

---

*ONB — {ID} / Phase {X}: {Title} | YYYY-MM-DD*
