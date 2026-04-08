# ONB — TFW-29: Consistency Audit

> **Date**: 2026-04-08
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-29](HL-TFW-29__consistency_audit.md)
> **TS**: [TS TFW-29](TS__TFW-29__consistency_audit.md)

---

## 1. Understanding

Remove redundancy between conventions.md, glossary.md, and .tfw/README.md. Fix inconsistencies in AGENTS.md, adapter files, and conventions.md numbering. Extract the Compilable Contract (§16) from conventions.md into its own file. The goal: agents load less duplicate content, no contradictions between files, all references resolve.

## 2. Entry Points

| File | Role in task |
|------|-------------|
| `.tfw/conventions.md` (426 lines) | Extract §16, fix §10 numbering |
| `.tfw/glossary.md` (191 lines) | Compress duplicated definitions → 1-liners + refs |
| `.tfw/README.md` (144 lines) | Anti-patterns block → ref to §14 |
| `AGENTS.md` (35 lines) | Workflow list 5 → 11 |
| `.agent/rules/agents.md` (34 lines) | Sync with AGENTS.md, fix handoff→REVIEW error |
| `.agent/rules/tfw.md` (28 lines) | Fix refs to non-existent `.agent/rules/conventions.md` |
| `.tfw/workflows/resume.md` (96 lines) | Add Context Loading section (if missing) |
| `.tfw/workflows/docs.md` (68 lines) | Add Prerequisites section (if missing) |
| `docs/scripts/gen_docs.py` (692 lines) | Verify Source Manifest after §16 extraction |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | **gen_docs.py Source Manifest**: After extracting §16 to `.tfw/compilable_contract.md`, should I add it as a new entry in gen_docs.py's `STATIC_SOURCES` (e.g., mapping to `reference/compilable-contract.md`)? The TS doesn't mention gen_docs.py updates, but the TS §6 Risks row 1 says "Verify compilable_contract.md path is correct for gen_docs.py. Update Source Manifest if needed." The conventions.md §16.1 Source Manifest table currently doesn't list it either. I believe it should be added to both. | **Yes.** Add `compilable_contract.md` to gen_docs.py `STATIC_SOURCES` mapping to `reference/compilable-contract.md`. Also update the Source Manifest table inside `compilable_contract.md` to list itself. You're right — without this the file becomes invisible in the docs site. |
| 2 | **AGENTS.md review.md missing from TS Step 4**: The TS Step 4 lists 11 workflows but omits `review.md` from the bullet list (lists plan, research, handoff, review, resume, docs, knowledge, init, config, release, update — wait, actually it has 11 including review). Confirmed: the TS list is correct at 11. No question needed. WITHDRAWN. | — |

## 4. Recommendations (suggestions, not blocking)

1. **conventions.md §16 stub should include a brief "what this is" line for agents**. The TS stub is 3 lines. I recommend adding a 1-sentence abstract so agents who see it during context loading know what the Compilable Contract is without following the link: "Defines the Source Manifest, Reference Format, and Output Structure for build-time compilation of TFW artifacts into documentation."
   > ✅ **Accepted.** Add the 1-sentence abstract to the stub.
2. **§11 "Design Rules (from P10-P13)" heading**: HL §2.3 item 5 flags that "references P10-P13 which are from KNOWLEDGE.md, not conventions.md itself." The TS doesn't explicitly address this. I recommend renaming the heading to "Design Rules" (dropping "from P10-P13") since those P-numbers were already moved/removed in TFW-25 and are confusing for new readers.
   > ✅ **Accepted.** Rename to "Design Rules" — the P-numbers are stale.
3. **resume.md already has Context Loading (implicit)**: resume.md Step 1 says "User specifies task folder path" and Step 2 says "Read Master HL." It has its own loading sequence embedded in the steps. Adding a separate "Context Loading" section as TS Step 7 suggests could be redundant with the existing workflow steps. I recommend a lighter touch: add a 1-line note referencing conventions.md §10 at the start, not a full section.
   > ✅ **Accepted.** Lighter touch: add 1-line ref to §10 at start, don't create a full section.
4. **docs.md has "Trigger Modes" but no Prerequisites**: Confirmed missing. The TS recommendation to add a "Prerequisites" section is appropriate.
   > ✅ **Confirmed.**

## 5. Risks Found (edge cases, potential issues not in TS)

1. **gen_docs.py hardcoded Source Manifest**: gen_docs.py line 22 maps `.tfw/conventions.md` → `reference/conventions.md`. After §16 extraction, the conventions page will be shorter but the mapping still works. However, `.tfw/compilable_contract.md` has NO entry in `STATIC_SOURCES` or `GLOB_SOURCES`. It will be invisible in the docs site unless added. This is the same risk as Q1.
   > ✅ **Addressed in Q1.** Add to STATIC_SOURCES.
2. **gen_docs.py docstring and comments reference `§16`**: Line 6 says `Contract: .tfw/conventions.md §16 (Compilable Contract)`. After extraction, this should say `.tfw/compilable_contract.md` or `conventions.md §16 → compilable_contract.md`. Not a breaking issue, but a stale comment.
   > ✅ **Fix it.** Update the docstring to point to `compilable_contract.md`.
3. **conventions.md §16.1 Source Manifest table self-reference**: The Source Manifest (currently §16.1, row 4) lists `.tfw/conventions.md` → `reference/conventions.md`. After extraction, the Source Manifest lives in `compilable_contract.md`, but gen_docs.py's `STATIC_SOURCES` is the actual runtime truth. The table in `compilable_contract.md` should be updated to include itself.
   > ✅ **Yes, add self-reference row** to Source Manifest table in compilable_contract.md.
4. **KNOWLEDGE.md references to "§16 in conventions.md"**: Lines 19, 39, 80, 108 in KNOWLEDGE.md reference `conventions.md §16`. After extraction, these become slightly misleading (§16 still exists as a stub, but the full content is elsewhere). This is out of scope per TS but worth noting for next tfw-docs.
   > ⬜ **Out of scope.** Record for next tfw-docs. §16 stub still exists so the refs aren't broken, just less precise.
5. **Glossary terms "Compilable Contract", "Reference Format", "Source Manifest"**: TS Step 3 says "Keep as 1-liners with ref to compilable_contract.md." Currently they ref `conventions.md §16`. The ref target needs to change to `compilable_contract.md`.
   > ✅ **Yes, update ref targets** to `compilable_contract.md`.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS Step 7 says "If Context Loading is genuinely missing" for resume.md** — resume.md does NOT have an explicit "Context Loading" section heading, but its Phase 1 steps ARE a context loading sequence (read Master HL, extract vision, phases, principles, strategic insights). The TS instruction is correct that there's no labeled section, but the functionality exists.
   > ✅ **Acknowledged.** Per Rec #3: add 1-line §10 ref, don't create a full section.
2. **TS Step 3 lists "Concept Taxonomy" as a meta-only term to remove** — glossary.md §Concept Taxonomy (lines 56-64) is a table mapping Document Type, Template, Workflow, Adapter Command, Status. This was introduced in D20 (TFW-15) as a formal disambiguation of 5 key concepts. While no workflow explicitly references it, it serves the "vocabulary" function of the glossary. Removing it is TS-directed, but I flag it as borderline — it has genuine definitional value.
   > 🟡 **Keep it.** Good catch — Concept Taxonomy is actually useful disambiguation (Document Type vs Template vs Workflow vs Adapter). It's only 8 lines. Keep in glossary.

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). Build script resolves to hyperlinks.

---

*ONB — TFW-29: Consistency Audit | 2026-04-08*
