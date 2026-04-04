# TS — TFW-25: Values & Principles Consolidation

> **Date**: 2026-04-04
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS_DRAFT
> **HL**: [HL-TFW-25](HL-TFW-25__values_consolidation.md)
> **RES**: [RES-TFW-25](RES__TFW-25__values_consolidation.md)

---

## Scope

Phase A only ("Audit & Consolidate"). Phase B deferred.

**Files in scope (7):**
1. `.tfw/README.md` — §Values and Principles rewrite
2. `KNOWLEDGE.md` — §0, §3, §4, §5 changes
3. `knowledge/convention.md` — prune 6 facts
4. `knowledge/process.md` — prune 5 facts
5. `knowledge/philosophy.md` — compress F4 (will be in README values)
6. `.tfw/conventions.md` — absorb P10-P13 content into existing §11 or new subsection
7. README.md task board — status update

**Budget**: 7 files (= max). 0 new files. ~200 LOC net reduction.

---

## Step 1: `.tfw/README.md` §Values and Principles

Replace lines 217-242 with 8 values in narrative format.

### Target content (exact text to write):

```markdown
## Values and Principles

### Traces Over Code

The trace is the product — intent, decisions, constraints, and alternatives matter more than the implementation itself. A codebase without traces is a black box. TFW captures not just *what* was built, but *why*, *what else was considered*, and *what was rejected*.

### Candor Over Flattery

AI agents trained on human feedback develop a habit of agreeing with users and praising their ideas. TFW agents are explicitly instructed: **Don't be sycophantic.** Be direct, precise, concrete. Flag risks. Disagree when evidence supports it. The coordinator's job is to ask uncomfortable questions and catch implicit assumptions — quality of planning matters more than speed of pipeline progression.

### Completeness Over Speed

When asked to implement, provide complete, usable output. **No placeholders.** No `// TODO: implement this`. If you can't produce a complete solution, say what's missing — don't fill the gap with a stub.

### Honesty Over Convincingness

AI agents that sound confident while being wrong are more dangerous than agents that refuse to answer. TFW agents must never fabricate data, claim untested results, or simulate external systems. When context is insufficient, the correct behavior is to ask, not guess. Confidence without correctness is the deadliest failure mode.

### Structural Enforcement

Gates should be structural — file existence, folder structure, required artifacts — not procedural (checkboxes in documents, state tables in headers). If a stage isn't done, the file doesn't exist. No parsing needed, no format compliance required, no update discipline to enforce. The filesystem is the state machine.

### Naming Creates Behavior

Right terminology triggers right associations in AI agents. A small prompt with precise terms is more effective than a long prompt with explanations. TFW adopted OODA, Sufficiency Verdict, Trust Protocol, Progressive Disclosure — each term replaced paragraphs of instructions. If you have to explain what a step does, the step is named wrong.

### Single Source of Truth

`.tfw/` contains exactly one copy of each convention, template, and workflow. Tool adapters reference it, never duplicate. If you need to change a rule, change it in one place.

### Portability

Everything is Markdown. No vendor lock-in. The files work in Obsidian, VS Code, GitHub, or a plain text editor. The knowledge belongs to you, not to a platform.
```

---

## Step 2: `KNOWLEDGE.md` §0 — Prune to 7 principles

Replace lines 8-26 (current 14 P# entries) with 7 entries.

### P# items to REMOVE (6):
- **P4** (Glossary = dictionary) — obvious from file structure
- **P6** (Lightweight docs) — obvious from tfw-docs workflow
- **P10** (Token density ≤1200) — move to conventions.md §11
- **P11** (Enforcement inline) — move to conventions.md §11
- **P12** (DNA/Library split) — move to conventions.md §11
- **P13** (Progressive Disclosure) — architecture IS the principle

### P# item to PROMOTE to README (1):
- **P14** (Filesystem state machine) — becomes "Structural Enforcement" in README

### Surviving §0 (7 items, compressed to 1-liners):

```markdown
## 0. Philosophy & Principles

| # | Principle | Source |
|---|-----------|--------|
| P1 | Traces over code — intent, decisions, constraints matter more than implementation | `.tfw/README.md` §Values |
| P2 | Index, don't duplicate — link to sources, don't copy | TFW-5 HL §7 |
| P3 | Philosophy stays rich — if DRY conflicts with narrative value, narrative wins | TFW-4 HL §7.1 |
| P5 | Meta-project awareness — this repo describes TFW AND uses TFW, overlap is by design | TFW-4 HL §7.3 |
| P7 | Self-review is not review — execution and review must be separate role-locked acts | TFW-8 HL §7 |
| P8 | Research ≠ passive checklist — external tools, pointed questions, WAIT gates. See `research/base.md` | TFW-11/14/17 |
| P9 | Coordinator quality > speed — uncomfortable questions, implicit assumptions, anti-rush. See `plan.md` Mindset | TFW-17 HL §7.1 |
```

**Note:** P# numbering preserved (P4, P6, P10-P14 become gaps). Historical task HL refs to removed P# remain valid as source links.

---

## Step 3: `KNOWLEDGE.md` §3 — Prune Legacy

Remove 18 resolved items from lines 115-137 (all pre-TFW-22, fully superseded).

Keep lines 138-148 (TFW-22 through TFW-24 items: 11 items).

### Lines to REMOVE:
- L115: STEPS.md → Removed
- L116: TASK.md → Removed
- L117: Summary Discipline → Removed
- L118: AI_ENTRY_POINT.md → Removed
- L119: SUCCESS_CRITERIA.md → Removed
- L120: 00_meta/ directory → Removed
- L121: Review in handoff.md → Removed
- L122: "REVIEW by any role" → Removed
- L123: Inline scope budget values → Removed
- L124: Version strings in titles → Removed
- L125: Hardcoded template/workflow lists → Removed
- L126: Manual init.md → Removed
- L127: Complexity Check → Removed
- L128: Board status emoji rename → Removed
- L129: Phase 3.5 renumber → Removed
- L130: "Autonomous search" in Gather → Removed
- L131: Coordinator without Mindset → Removed
- L132-137: TFW-21/19 era items → Removed

---

## Step 4: `KNOWLEDGE.md` §4 — Remove entirely

Delete lines 152-160 (Tech Stack & Infrastructure section). Trivially obvious from repo.

---

## Step 5: `KNOWLEDGE.md` §5 — Update fact counts

Update the Project Facts index table to reflect new counts after Step 6-7:
- convention: 12 → 6 facts
- process: 10 → 5 facts
- philosophy: 4 → 4 facts (unchanged)
- constraint: 3 → 3 facts (unchanged)

---

## Step 6: `knowledge/convention.md` — Prune 6 facts

Remove:
- **F4** (checkpoint fields in templates) — templates show this
- **F6** (Config Sync Registry scope) — workflow shows this
- **F8** (§3.1 domain-agnostic) — template IS the rule
- **F9** (filesystem state machine) — P14 + conventions §4 + base.md
- **F10** (RES = synthesis) — templates/RES.md structure
- **F12** (stage template structure) — templates exist

Keep: F1, F2, F3, F5, F7, F11 (6 facts)

Renumber F5→F4, F7→F5, F11→F6 for clean sequence.

---

## Step 7: `knowledge/process.md` — Prune 5 facts

Remove:
- **F2** (knowledge ≠ docs) — philosophy/F2 is authoritative version
- **F3** (scan conversation for FCs) — template instruction
- **F8** (crash → gate skipping) — F10 covers fix, problem-only fact = noise
- **F9** (4 roles) — conventions §15
- **F10** (resume protocol) — base.md Step 0

Keep: F1, F4, F5, F6, F7 (5 facts)

Renumber for clean sequence.

---

## Step 8: `.tfw/conventions.md` — Absorb P10-P13

Add subsection to §11 or create §11.1 "Design Rules" with compressed P10-P13 content:

```markdown
### Design Rules (from P10-P13)

- **Token density**: workflow instructions ≤1200 words. Templates own format; workflows reference templates
- **Inline enforcement**: enforcement-critical values MUST be inline (Pattern A: defaults + config key). Pure refs (Pattern B) = broken
- **DNA/Library**: Role Lock + Mindset = always inline. Reference data = via ref-inside-step. Step self-contained, ref adds precision
- **Progressive Disclosure**: agent loads only what it needs now. Mode files loaded at Step 2, not at start
```

**Placement decision:** After reviewing conventions.md structure, insert into existing §11 (Scope Budgets) if it covers "design constraints", OR create a new subsection nearby. Executor decides exact position.

---

## Step 9: README.md task board — Update status

Change TFW-25 status from `📝 HL_DRAFT` to `🟢 RF` after execution complete.

---

## Acceptance Criteria

- [ ] AC-1: `.tfw/README.md` §Values has exactly 8 values: Traces, Candor, Completeness, Honesty, Structural Enforcement, Naming, SSOT, Portability
- [ ] AC-2: `KNOWLEDGE.md` §0 has exactly 7 principles (P1-P3, P5, P7-P9)
- [ ] AC-3: `KNOWLEDGE.md` §3 has ≤17 Legacy items (all TFW-22+)
- [ ] AC-4: `KNOWLEDGE.md` §4 Tech Stack section removed
- [ ] AC-5: `KNOWLEDGE.md` §5 fact counts updated (6/5/4/3)
- [ ] AC-6: `knowledge/convention.md` has exactly 6 facts (renumbered)
- [ ] AC-7: `knowledge/process.md` has exactly 5 facts (renumbered)
- [ ] AC-8: `.tfw/conventions.md` contains P10-P13 content (Design Rules subsection)
- [ ] AC-9: KNOWLEDGE.md total ≤120 lines
- [ ] AC-10: No dead cross-references (grep verify)
- [ ] AC-11: Adapters NOT in scope (Phase B)

---

*TS — TFW-25: Values & Principles Consolidation | 2026-04-04*
