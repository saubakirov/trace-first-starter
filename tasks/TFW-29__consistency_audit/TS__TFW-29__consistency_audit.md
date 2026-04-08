# TS — TFW-29: Consistency Audit

> **Date**: 2026-04-08
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-29](HL-TFW-29__consistency_audit.md)
> **RES**: [RES-TFW-29](RES__TFW-29__consistency_audit.md)

---

## 1. Objective
Remove redundancy between conventions.md, glossary.md, and workflows. Fix inconsistencies in adapter files and AGENTS.md. Extract build-time content (§16) from conventions.md. Result: agents load less, understand more, no contradictions.

## 2. Scope

### In Scope
- Extract conventions.md §16 (Compilable Contract) to separate file
- Compress glossary.md: duplicated definitions → 1-liners with refs, remove meta-only terms
- Fix conventions.md §10 numbering
- Fix AGENTS.md incomplete workflow list
- Fix `.agent/rules/agents.md` and `.agent/rules/tfw.md` inconsistencies
- Replace .tfw/README.md anti-patterns block with ref to §14
- Add minimal Context Loading to resume.md and docs.md (if confirmed missing on re-read)

### Out of Scope
- Restructuring conventions.md sections (§1-§3, §7-§8 stay as-is — they serve as onboarding reference)
- Template file changes
- Any workflow logic changes (only loading/reference fixes)
- CHANGELOG update (separate step after execution)

## 3. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/conventions.md` | MODIFY | Extract §16 → stub ref; fix §10 numbering |
| `.tfw/compilable_contract.md` | CREATE | §16 content moved here |
| `.tfw/glossary.md` | MODIFY | Compress: dedup defs → 1-liners, remove meta terms |
| `.tfw/README.md` | MODIFY | Anti-patterns block → ref to conventions §14 |
| `AGENTS.md` | MODIFY | Workflow list 5 → 11 |
| `.agent/rules/agents.md` | MODIFY | Sync with AGENTS.md, fix handoff→REVIEW error |
| `.agent/rules/tfw.md` | MODIFY | Remove refs to non-existent files |
| `.tfw/workflows/resume.md` | MODIFY | Add Context Loading section (if missing — verify first) |
| `.tfw/workflows/docs.md` | MODIFY | Add Prerequisites section (if missing — verify first) |

**Budget:** 1 new file, 8 modifications. Max 14 files, max 8 new, max 1200 LOC.

## 4. Detailed Steps

### Step 1: Extract §16 Compilable Contract
1. Read conventions.md — locate §16 and all sub-sections (§16.1-§16.4)
2. Create `.tfw/compilable_contract.md` with the full content
3. Replace §16 block in conventions.md with:
   ```markdown
   ## 16) Compilable Contract

   > Build-time specification for deterministic compilation of TFW artifacts.
   > Full contract: [compilable_contract.md](compilable_contract.md)
   ```
4. Verify: grep workflows for any `§16` references → should be 0

### Step 2: Fix conventions.md §10 numbering
Current order: §10.1 Fact Categories → §10.2 Knowledge Infrastructure → §10 Context Loading.

Fix: reorder to §10 Context Loading → §10.1 Fact Categories → §10.2 Knowledge Infrastructure.

Move the §10 block (lines ~233-238) BEFORE §10.1 (lines ~207-221).

### Step 3: Compress glossary.md
For each duplicated term (artifact types, status flow, CL/AG, task naming):
- Replace full definition with 1-liner + ref

Example — current HL entry (~4 lines):
```markdown
### HL (High Level)
Context, research, background, requirements. Not a task — a "map of meaning". 
Format: strictly follows `.tfw/templates/HL.md`. Contains: Vision, As-Is, To-Be, 
Phases, DoD, DoF, Principles, Dependencies, Risks.
```

Compressed (~1 line):
```markdown
### HL (High Level)
Context/frame artifact for a task — the "map of meaning". → conventions.md §3
```

Remove these meta-only terms entirely:
- Concept Taxonomy (never referenced by any workflow)
- Workflow (canonical) — self-referential
- `.tfw/ Directory` — meta
- Execution Engine, Progress Reporting — config-level, never used
- tfw-init, tfw-release, tfw-update workflow descriptions — workflows are self-describing

Keep Compilable Contract / Reference Format / Source Manifest as 1-liners with ref to compilable_contract.md.

### Step 4: Fix AGENTS.md
Replace §Workflows section with complete list of all 11 workflows:
```markdown
## Workflows
Follow `.tfw/workflows/`:
- `plan.md` — task inception (HL → research → TS)
- `research/base.md` — structured investigation (RES artifact)
- `handoff.md` — execution (ONB → develop → RF)
- `review.md` — task review (RF → checklist → REVIEW)
- `resume.md` — continue interrupted work (status matrix → next phase)
- `docs.md` — knowledge update after REVIEW (KNOWLEDGE.md, TECH_DEBT.md)
- `knowledge.md` — consolidate fact candidates into verified knowledge
- `init.md` — initialize TFW in a new project
- `config.md` — interactive config change, propagate to inline values
- `release.md` — cut a versioned release
- `update.md` — upgrade .tfw/ from upstream starter
```

### Step 5: Fix adapter files
**`.agent/rules/agents.md`:**
- Sync workflow list with AGENTS.md (Step 4 result)
- Fix line 30: remove "→ REVIEW" from handoff description

**`.agent/rules/tfw.md`:**
- Replace context loading references to non-existent `.agent/rules/conventions.md` and `.agent/rules/glossary.md` with direct `.tfw/conventions.md` and `.tfw/glossary.md`

### Step 6: README.md anti-patterns
In `.tfw/README.md`, replace the full anti-patterns list (~9 items) with:
```markdown
## Anti-patterns

> Full list → [conventions.md §14](conventions.md#14-anti-patterns-prohibited)

These exist because every single one has happened and caused real problems.
```

### Step 7: Verify resume.md and docs.md Context Loading
Re-read both files. If Context Loading is genuinely missing:
- **resume.md:** Add after the Role Lock block:
  ```markdown
  ## Context Loading
  1. Read conventions.md §10 — verify core context loaded
  2. User specifies task folder path
  ```
- **docs.md:** Add Prerequisites if missing:
  ```markdown
  ## Prerequisites
  1. Read `KNOWLEDGE.md` — current state before updating
  2. Read `TECH_DEBT.md` — current entries
  ```

### Step 8: Final verification
1. `grep -r "§16" .tfw/workflows/` — confirm 0 references to §16 from workflows
2. `grep -r "§10" .tfw/workflows/` — confirm §10 references still resolve
3. `diff .agent/workflows/tfw-plan.md .tfw/workflows/plan.md` — adapters in sync
4. Count lines: conventions.md, glossary.md — verify reduction
5. Read through each modified file for coherence

## 5. Acceptance Criteria

- [ ] conventions.md §16 block replaced with 3-line stub referencing compilable_contract.md
- [ ] `.tfw/compilable_contract.md` exists with full §16 content
- [ ] conventions.md §10 numbering is sequential (§10 → §10.1 → §10.2)
- [ ] glossary.md has no duplicated full definitions — only 1-liners + refs for shared terms
- [ ] glossary.md meta-only terms removed (Concept Taxonomy, Workflow canonical, .tfw/ Directory, Execution Engine, Progress Reporting, tfw-init/release/update descriptions)
- [ ] AGENTS.md lists all 11 workflows
- [ ] `.agent/rules/agents.md` synced with AGENTS.md, no "handoff→REVIEW" error
- [ ] `.agent/rules/tfw.md` references `.tfw/conventions.md` directly (not non-existent agent/rules copies)
- [ ] `.tfw/README.md` anti-patterns = ref to §14 (not full list)
- [ ] No workflow `§`-reference is broken by changes (grep verification)

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| §16 extraction breaks compilable contract docs build | Verify compilable_contract.md path is correct for gen_docs.py. Update Source Manifest if needed |
| Glossary compression removes a term an agent actually needs | Verify each removal against G4 workflow usage table. When in doubt, keep as 1-liner |
| §10 renumbering breaks workflow refs | All refs use `§10` not `§10.3` — moving §10 before §10.1 preserves all references |

---

*TS — TFW-29: Consistency Audit | 2026-04-08*
