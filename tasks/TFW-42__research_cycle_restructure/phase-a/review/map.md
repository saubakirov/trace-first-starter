# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase A](../RF__phase-a__conventions_and_templates.md)
> TS: [TS Phase A](../TS__phase-a__conventions_and_templates.md)
> Mode: docs

## Understanding

The executor rewrote conventions.md §4 to establish a unified `research/iterN/` folder structure, renumbered stage file templates (1_briefing.md → 4_challenge.md), enriched the iterations.yaml schema with optional `agent` and `sources` fields, normalized phase folder naming from PascalCase to kebab-case, added an agent selection guidance subsection with a 5-row capability table, updated the RES template briefing reference, and restructured the §4 section ordering for logical grouping. Two key decisions: (1) section reordering was approved via ONB Q1, (2) RES template path made relative since RES.md now lives alongside stage files.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1: Research folder structure — `research/` single container, `research/iterN/`, `research/iterations.yaml`, co-located RES.md, trace rule | RF §3 AC-1: ✅ all sub-items checked | ✅ |
| AC-2: iterations.yaml schema — `agent` + `sources` optional, `res_file` paths, no `brief`/`notes`/`depends_on`, traceability not dispatch | RF §3 AC-2: ✅ all sub-items checked | ✅ |
| AC-3: Numbered stage files — 4 files renamed, old deleted, conventions lists numbered names | RF §3 AC-3: ✅ all sub-items checked | ✅ |
| AC-4: Phase folder naming — `phase-a/` kebab-case, filename table updated, 0 PhaseA matches | RF §3 AC-4: ✅ all sub-items checked | ✅ |
| AC-5: Schema backward compatibility — 9 original fields preserved, new fields additive | RF §3 AC-5: ✅ all sub-items checked | ✅ |
| AC-6: Agent selection guidance — 5-row capability table, no tool names, "guidance not prescription" | RF §3 AC-6: ✅ all sub-items checked | ✅ |

## Deviations from TS

1. **Section reordering in §4** — RF §2 Key Decision #1: the executor restructured §4's internal ordering (Research → Multi-iteration → iterations.yaml → Agent guidance → Review → Multi-phase) to achieve logical grouping. This was a deviation from TS's assumed line ordering but was explicitly approved by the coordinator in ONB §6. Valid deviation with approval.

2. **Multi-phase tree update** — RF §2 Key Decision #3: replaced `RES__PROJ-5__query_redesign.md ← Master RES (if any)` with `research/ ← Master research (if any)` in the multi-phase example tree. Not explicitly in TS but directly follows from AC-1 (research/ as single container). Logically consistent.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES
