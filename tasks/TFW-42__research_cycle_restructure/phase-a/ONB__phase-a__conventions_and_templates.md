# ONB — TFW-42 / Phase A: Conventions & Templates

> **Date**: 2026-04-30
> **Author**: Executor (Antigravity)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-42](../HL-TFW-42__research_cycle_restructure.md)
> **TS**: [TS Phase A](TS__phase-a__conventions_and_templates.md)

---

## 1. Understanding
Phase A rewrites conventions.md §4 to establish the new research folder structure (unified `research/iterN/`, numbered stage files, kebab-case phase folders), enriches the iterations.yaml schema with optional `agent` and `sources` fields, renames the 4 stage file templates with numeric prefixes, updates the RES template header, and adds an agent selection guidance subsection. This is a pure conventions + templates phase — no workflow or glossary changes.

## 2. Entry Points
| File | Purpose |
|------|---------|
| `.tfw/conventions.md` (lines 107-191) | §4 Task Numbering — filename table, Research subfolder, Multi-iteration research, Multi-phase folder structure |
| `.tfw/templates/research/briefing.md` | Stage template → rename to `1_briefing.md` |
| `.tfw/templates/research/gather.md` | Stage template → rename to `2_gather.md` |
| `.tfw/templates/research/extract.md` | Stage template → rename to `3_extract.md` |
| `.tfw/templates/research/challenge.md` | Stage template → rename to `4_challenge.md` |
| `.tfw/templates/RES.md` (line 15) | Briefing path reference → update to new convention |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | conventions.md §4 lines 131-133 currently describe stage files as `briefing.md`, `gather.md`, `extract.md`, `challenge.md` and reference templates by old names. After rewrite, the Review subfolder section (line 148-150) has a parallel reference: `research/gather.md`. Should I update the Review subfolder's parallel reference from `research/gather.md` to `research/iterN/2_gather.md`, or leave it as-is since review structure is out of scope? | **Yes, update it.** The Review subfolder section has a parenthetical `(research/gather.md, etc.)` that illustrates the parallel — update to numbered names for consistency. The review structure itself isn't changing, only the illustrative reference to research stage files. |
| 2 | The TS says stage file renames should use `git mv`. On Windows with this tooling, I can create new files and delete old ones (content-preserving). Shall I proceed with create-new + delete-old, or do you want `git mv` via command? | **Create-new + delete-old is fine.** Content is identical, git will detect the rename automatically. No need for explicit `git mv`. |

## 4. Recommendations (suggestions, not blocking)
1. **Agent guidance subsection placement:** TS §6 says "place after the iterations.yaml block, before Review subfolder (line 148)." I recommend placing it as a new `### Agent selection guidance` sub-section under the `### Research subfolder` heading, after the iterations.yaml block and its explanatory paragraph (line 172), and before `### Review subfolder` (line 148). This keeps all research-related content grouped.

2. **RES.md Briefing reference:** Line 15 currently says `{Copied from or reference to research/briefing.md.}`. I will update this to `{Copied from or reference to 1_briefing.md in iteration folder.}` as TS §6 suggests — keeping it generic since the RES.md now lives inside `research/iterN/` alongside its stage files.

## 5. Risks Found (edge cases, potential issues not in TS)
1. **Cross-references outside §4:** conventions.md §14 (line 386) references `TS §5 must contain acceptance criteria (WHAT), not code or steps (HOW)` — no research paths. §3 line 51 references `research/` subfolder and `templates/research/` by old names (`briefing.md`, `gather.md`, etc.). These are in §3, not §4. Should be noted as observation but technically out of TS scope (TS says "Grep entire file for PhaseA, research2, research3" in Phase Risks, but only changes §4).

2. **compilable_contract.md (line 56, 78):** References `PhaseA/` in resolution rules. Out of scope per TS, but will break on convention change. Observation for Phase B/C.

## 6. Inconsistencies with Code (spec vs reality)
1. **TS §6 line numbers are approximate.** TS says "§4 currently spans lines 107-191" — confirmed accurate. TS says "iterations.yaml code block is at lines 152-170" — confirmed accurate. TS says "agent guidance: place before Review subfolder (line 148)" — but Review subfolder is at line 148 which is BEFORE the iterations.yaml block (line 152). The intended placement is after the iterations.yaml block (after line 172), before §5 Task Statuses (line 193). The Review subfolder section is actually at lines 148-150. I will use the logical intent: after iterations.yaml, before Review subfolder — which means after line 172, before line 148. **Wait** — re-reading the file: Review subfolder is at line 148, iterations.yaml block starts at line 152. This means the TS description of "after iterations.yaml, before Review subfolder" is physically impossible given current line order. The actual order is: Research subfolder (131) → Multi-iteration (135) → Review subfolder (148) → iterations.yaml (152) → Multi-phase (174). **I will restructure §4 to achieve the logical grouping the HL intended: all research content (subfolder + iterations + agent guidance) together, then review, then multi-phase.** **Coordinator: Correct. My TS line references were wrong — the current order is indeed Research → Review → iterations.yaml → Multi-phase, which is illogical. Your restructuring to group all research content together is the right call. The intended logical order: Research subfolder → Multi-iteration → iterations.yaml schema → Agent guidance → Review subfolder → Multi-phase. Proceed with this restructuring.**

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | KC1: philosophy.md F4 — Structural enforcement beats format enforcement | ✅ | Applied — numbered filenames are structural (sort order enforced by filesystem), not format (documented but unenforced) | |
| 2 | KC2: philosophy.md F24 — Instructions produce compliance, heuristics produce competence | ✅ | Applied — `1_briefing.md` is self-documenting heuristic vs "read briefing first" instruction | |
| 3 | KC3: convention.md F19 — Naming consistency is a design principle | ✅ | Applied — phase-a kebab-case aligns with D48, stage files get uniform `N_name.md` pattern | |
| 4 | KC4: KNOWLEDGE.md D48 — Naming normalization | ✅ | Applied — extending lowercase convention to folder names (PhaseA → phase-a) | |
| 5 | KC5: KNOWLEDGE.md D38 — Multi-iteration research | ✅ | Applied — refactoring D38 structure (same principles, better organization) | |
| 6 | KC6: process.md F14 — Without YAML control files, agents fast-run | ✅ | Applied — enriching iterations.yaml with agent/sources fields | |
| 7 | KC7: convention.md F15 — Multi-phase uses PhaseX/ subfolders | ✅ | Applied — changing PhaseX → phase-x in conventions | |

> No NEW items found beyond coordinator's citations.

---

*ONB — TFW-42 / Phase A: Conventions & Templates | 2026-04-30*
