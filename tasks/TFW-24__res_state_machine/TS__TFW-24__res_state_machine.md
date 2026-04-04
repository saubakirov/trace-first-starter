# TS — TFW-24: Researcher Role & RES State Machine

> **Date**: 2026-04-04
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-24](HL-TFW-24__res_state_machine.md)

---

## 1. Objective

Extract RESEARCHER as a standalone 4th role with its own Role Lock, introduce a research subfolder with stage files as a filesystem-level state machine, and add a Resume Protocol so any agent can continue research from any chat after any crash. Additionally, update HL template §1 to Vision + Impact + Quote format and make §2/§5 domain-agnostic.

## 2. Scope

### In Scope
- Researcher role definition (conventions §8, §15, glossary)
- `research/base.md` → Role Lock relabeling + Step 0 (Resume) + subfolder creation + Synthesis step
- Research subfolder convention (conventions §4)
- Stage file structure (Goal ref + Findings + Checkpoint)
- `plan.md` Step 6 → handoff to Researcher + Hard Stop
- `templates/RES.md` → synthesis format
- `templates/HL.md` → §1 Vision/Impact/Quote + §2/§5 domain-agnostic
- `PROJECT_CONFIG.yaml` → RES status role
- Adapter sync

### Out of Scope
- Changes to Executor or Reviewer roles
- New template files for stage files (stage structure documented in conventions, not a separate template)
- OODA loop changes
- Mode files (focused.md, deep.md) changes

## 3. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/conventions.md` | MODIFY | §4: research subfolder convention. §8: Workflows table role → Researcher. §15: Role Lock table → Researcher row |
| `.tfw/glossary.md` | MODIFY | Remove "Conducts RESEARCH" from Coordinator. Add Researcher role definition |
| `.tfw/workflows/research/base.md` | MODIFY | Role Lock → RESEARCHER. Add Step 0 (Resume Protocol). Step 3 → create research/ subfolder + stage files. Step 7 → Synthesis (consolidate stage files → final RES). Rule: MUST update stage file before WAIT |
| `.tfw/workflows/plan.md` | MODIFY | Step 6 → "Hand off to Researcher. STOP." Add Hard Stop (Coordinator must not conduct research) |
| `.tfw/templates/RES.md` | MODIFY | Reshape to synthesis format: Decisions, Hypotheses, HL Recommendations, FC, Conclusion. Remove stage sections (Gather/Extract/Challenge) — those live in stage files |
| `.tfw/templates/HL.md` | MODIFY | §1 → Vision + Impact + Quote. §2 → domain-agnostic instruction. §5 → domain-agnostic instruction |
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | RES status `role: coordinator` → `role: researcher` |
| `.agent/workflows/tfw-plan.md` | MODIFY | Copy from `.tfw/workflows/plan.md` |
| `.agent/workflows/tfw-research.md` | MODIFY | Copy from `.tfw/workflows/research/base.md` |
| `.claude/commands/tfw-plan.md` | MODIFY | Copy from `.tfw/workflows/plan.md` |

**Budget:** 0 new files, 10 modifications. Limits: max 14 files, max 12 modified. ✅ Within budget.

## 4. Detailed Steps

### Step 1: Researcher role in conventions.md + glossary.md

**conventions.md §8 (Workflows table):**
- Change `research/base.md` row: `Coordinator` → `Researcher`

**conventions.md §15 (Role Lock table):**
- Change `research/base.md` row: `Coordinator` → `Researcher`
- Permitted: `RES, research/ stage files`
- Forbidden: `HL, TS, ONB, RF, REVIEW, code`

**conventions.md §4 (Artifact Naming):**
- Add research subfolder convention:
  > Research stage files stored in `tasks/{ID}/research/`: `briefing.md`, `gather.md`, `extract.md`, `challenge.md`. File existence = stage completion. Final `RES__*.md` = synthesis of all stages.

**glossary.md:**
- Coordinator entry: remove "Conducts RESEARCH and writes RES files"
- Add new entry:
  > **Researcher (AI)** — Dedicated research agent. Writes RES and stage files in `research/` subfolder. Follows OODA loop. Hard Stop: after writing RES, says "Research complete. Continue with `/tfw-plan`."

### Step 2: base.md — Role Lock + Step 0 + subfolder + Synthesis

**Role Lock (L7-8):**
```markdown
> 🔒 **ROLE LOCK: RESEARCHER**
> You write RES and research/ stage files only. You do NOT write HL, TS, ONB, RF, REVIEW, or code.
```

**Step 0: Resume Protocol (insert before current Step 1):**
```markdown
## Step 0: Resume

IF resuming (not fresh start): re-read this workflow + mode file.
Check task folder: `research/` exists? → which stage files exist? → `RES__*` exists?
Resume from first missing stage. If RES exists → research complete.
```

**Step 3 (current) — add subfolder creation:**
After "Create in task directory", add:
> Create `research/` subfolder. Each stage writes its own file: `briefing.md`, `gather.md`, `extract.md`, `challenge.md`. Format: Goal reference (from HL §1) + Findings + Checkpoint (`Stage complete: YES/NO`).

**Step 4 (Briefing) — writes to `research/briefing.md`:**
Update to: "Write Briefing Protocol to `research/briefing.md`."

**Step 5 (Stages) — each stage writes its own file:**
Update to: "Write each stage to its file: `research/gather.md`, `research/extract.md`, `research/challenge.md`."

**Step 7 (Closure) — rename to Synthesis + Hard Stop:**
```markdown
## Step 7: Synthesis

1. Read all stage files (briefing, gather, extract, challenge)
2. Write final `RES__*.md` using `templates/RES.md` — synthesize, don't copy-paste
3. HL Update Recommendations (table)
4. Fact Candidates — review conversation history first
5. Conclusion (1 paragraph)
6. **STOP.** "Research complete. Continue with `/tfw-plan` to update HL and write TS."
```

**Rules — add:**
- MUST: write stage file before every WAIT gate
- MUST: STOP after writing final RES (never proceed to HL/TS)

### Step 3: plan.md — Researcher handoff

**Step 6 — rewrite handoff:**
```markdown
IF user approves research → "Start `/tfw-research`. Researcher role takes over." **STOP.**
```

Add to footer/self-check:
> Did I hand off to Researcher properly? Did I STOP after recommending research? (Anti-pattern: Coordinator conducting own research)

### Step 4: templates/RES.md — synthesis format

Remove Gather/Extract/Challenge stage sections from RES template. Replace with synthesis structure:

```markdown
## Decisions
| # | Decision | Rationale |

## Open Questions
| # | Question | Status | Answer |

## Hypotheses (from HL §10)
| # | Hypothesis | HL Status | RES Status | Evidence |

## HL Update Recommendations
| # | What to update | Source |

## Fact Candidates
| # | Category | Candidate | Source | Confidence |

## Conclusion
{1 paragraph synthesis}
```

Keep header (Date, Author, Status, Parent HL, Mode) and Research Context. Briefing section stays in RES (copied from `research/briefing.md` or referenced).

### Step 5: templates/HL.md — Vision + domain-agnostic + Working Backwards

**§1 (L9-12):**
```markdown
## 1. Vision
{Strategic narrative: what we want and why — 2-3 sentences. Write as if it's already done.}

**Impact:** {What changes when this is done — for users, team, product}

> Key quote from the stakeholder perspective — what they would say when this ships.
```
Quote instruction changed from generic "key quote" to **stakeholder perspective** (Amazon press release pattern). Forces agent to think: "who benefits? what would they say?"

**§10 — add "Why Not Just...?" section after Blind Spots:**
```markdown
### Why Not Just...?
- Why not {obvious alternative A}? — {reason}
- Why not {obvious alternative B}? — {reason}
```
Amazon internal FAQ pattern. Forces Coordinator to consider alternatives BEFORE research. Structural anti-skip-bias.

**§2 (L14-16):**
```markdown
## 2. Current State (As-Is)
Current state: problems, structure, metrics, constraints.
Tables with REAL data where applicable.
```

**§5 (L42-44):**
```markdown
## 5. Definition of Done (DoD)
Numbered list. Each item starts with ✅.
Must cover all deliverables from §4 Phases.
```

### Step 6: PROJECT_CONFIG.yaml — RES status role

Change RES status entry `role: coordinator` → `role: researcher`.

### Step 7: Adapter sync

```bash
cp .tfw/workflows/plan.md .agent/workflows/tfw-plan.md
cp .tfw/workflows/research/base.md .agent/workflows/tfw-research.md
cp .tfw/workflows/plan.md .claude/commands/tfw-plan.md
```

## 5. Acceptance Criteria

- [ ] `conventions.md` §8 shows Researcher for research/base.md
- [ ] `conventions.md` §15 shows Researcher with correct Permitted/Forbidden
- [ ] `conventions.md` §4 has research subfolder convention
- [ ] `glossary.md` has Researcher entry, Coordinator no longer mentions research
- [ ] `base.md` Role Lock = `RESEARCHER` (not Coordinator)
- [ ] `base.md` has Step 0 (Resume Protocol)
- [ ] `base.md` stages write to individual stage files in `research/`
- [ ] `base.md` Step 7 = Synthesis + Hard Stop
- [ ] `plan.md` Step 6 hands off to Researcher, not self-switches
- [ ] `templates/RES.md` has synthesis structure (no stage sections)
- [ ] `templates/HL.md` §1 = Vision + Impact + stakeholder Quote
- [ ] `templates/HL.md` §10 = has "Why Not Just...?" section
- [ ] `templates/HL.md` §2, §5 = domain-agnostic
- [ ] `PROJECT_CONFIG.yaml` RES role = researcher
- [ ] Zero occurrences of "Coordinator (Research Mode)" in `.tfw/`
- [ ] All 3 adapters synced
- [ ] `base.md` ≤ 600 words

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| base.md exceeds 600 words after additions | Step 0 = ~30 words, subfolder instruction = ~20, Synthesis = ~20. Total ~70 new. 518+70 = ~588 |
| RES template synthesis structure too vague → agents dump stages | Stage sections physically absent from template. Different structure forces different thinking |
| Adapter copy misses files | Explicit `cp` commands in Step 7. 3 files only |

---

*TS — TFW-24: Researcher Role & RES State Machine | 2026-04-04*
