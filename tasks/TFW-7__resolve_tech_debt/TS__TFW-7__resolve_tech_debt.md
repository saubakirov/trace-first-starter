# TS — TFW-7: Resolve All Open Tech Debt

> **Date**: 2026-03-12
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS — Awaiting approval
> **Parent HL**: [HL-TFW-7](HL-TFW-7__resolve_tech_debt.md)

---

## 1. Goal

Resolve all 5 open `⬜ Backlog` tech debt items via targeted text edits. After execution, zero backlog items remain in `TECH_DEBT.md`.

## 2. Scope

### In Scope

- TD-2: Add cross-reference notes between overlapping `.tfw/` files
- TD-3: Reclassify as `Accepted — ONB always required` (no file changes)
- TD-4: Add `docs` workflow to `.tfw/README.md` §Canonical Workflows
- TD-7: Reclassify as `Accepted — by design` (adapters reference `.tfw/workflows/` directly)
- TD-8: Add `docs.md` row to `conventions.md` §8 Workflows table
- TD-9: Remove hardcoded workflow count from `.tfw/README.md` L161 (future-proof)

### Out of Scope

- File restructuring or rewriting
- Any code changes
- New template creation

## 3. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/conventions.md` | MODIFY | Add `docs.md` to §8 table (TD-8); add cross-ref note to overlap areas (TD-2) |
| `.tfw/README.md` | MODIFY | Add `docs` row to §Canonical Workflows (TD-4); fix "five" → "six" (TD-9); add cross-ref note (TD-2) |
| `.tfw/glossary.md` | MODIFY | Add cross-ref note to Workflow definition (TD-2) |
| `TECH_DEBT.md` | MODIFY | Update statuses for all 5 items |

**Budget:** 0 new files, 3 modifications. ≤7 files ✅, ≤4 new ✅, ≤600 LOC ✅.

## 4. Detailed Steps

### Step 1: Fix TD-8 + TD-4 + TD-9 (workflow listing consistency)

**TD-8** — In `.tfw/conventions.md` §8, add `docs.md` row to the Workflows table:

```markdown
| [docs.md](workflows/docs.md) | Coordinator | Update KNOWLEDGE.md and TECH_DEBT.md after task completion |
```

**TD-4** — In `.tfw/README.md` §Canonical Workflows, add `docs` row after the `resume` row:

```markdown
| **docs** | Coordinator | After REVIEW → update KNOWLEDGE.md and TECH_DEBT.md |
```

**TD-9** — In `.tfw/README.md` L161, remove the hardcoded count:

```diff
-TFW v3 defines five canonical workflows
+TFW v3 defines the following canonical workflows
```

### Step 2: Fix TD-3 (accept as-is)

No file changes. TD-3 is accepted — ONB is always required, lightweight mode could undermine the protocol.

### Step 3: Fix TD-2 (cross-references)

Add a brief cross-reference note at the bottom of the overlapping sections in each file:

- `.tfw/conventions.md` — top of §3: `> See also: [.tfw/glossary.md](glossary.md) for terminology, [.tfw/README.md](README.md) for philosophy.`
- `.tfw/README.md` — after §Artifact Types: `> Formal naming rules and lifecycle → [conventions.md](conventions.md). Full definitions → [glossary.md](glossary.md).`
- `.tfw/glossary.md` — after §Artifact Types header: `> Canonical rules → [conventions.md](../conventions.md). Philosophy → [README.md](../README.md).`

### Step 4: Fix TD-7 (accept by design)

No file changes needed. Update status in `TECH_DEBT.md` to `Accepted — by design`.

### Step 5: Update TECH_DEBT.md

Update all 5 items:
- TD-2: `Accepted — cross-refs added`
- TD-3: `Accepted — ONB always required`
- TD-4: `✅ Resolved (TFW-7)`
- TD-7: `Accepted — by design`
- TD-8: `✅ Resolved (TFW-7)`
- TD-9: `✅ Resolved (TFW-7)`

## 5. Acceptance Criteria

- [ ] `conventions.md` §8 Workflows table has 6 rows (plan, handoff, resume, docs, release, update)
- [ ] `.tfw/README.md` §Canonical Workflows has all rows and no hardcoded count
- [ ] TD-3 marked as Accepted in TECH_DEBT.md
- [ ] Cross-reference notes added to conventions, README, glossary
- [ ] All TECH_DEBT.md items resolved or accepted — no `⬜ Backlog` remaining
- [ ] No new inconsistencies introduced

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Edits break markdown table formatting | Verify table renders correctly after each edit |

---

*TS — TFW-7: Resolve All Open Tech Debt | 2026-03-12*
