# HL — TFW-29: Consistency Audit — Glossary, Conventions, Workflows

> **Date**: 2026-04-08
> **Author**: Coordinator (AI)
> **Status**: 📝 HL_DRAFT — Awaiting review

---

## 1. Vision
The three core reference files (conventions.md, glossary.md, .tfw/README.md) and 11 workflows that read them are free from redundancy, contradiction, and dead weight. An agent loading context spends minimum tokens on maximum signal.

**Impact:** Faster context loading, fewer misalignment bugs between workflows, lower token cost per session, cleaner onboarding for new users and new AI tools.

> "I read conventions + glossary once and I know everything I need. Nothing is repeated, nothing is missing."

## 2. Current State (As-Is)

### 2.1 Size inventory

| File | Lines | Bytes | Words (approx) |
|------|-------|-------|-----------------|
| conventions.md | 426 | 21 406 | ~3 200 |
| glossary.md | 191 | 12 776 | ~1 950 |
| .tfw/README.md | 144 | 7 992 | ~1 350 |
| **Total reference core** | **761** | **42 174** | **~6 500** |

### 2.2 Redundancy map (found during research)

| Content block | Where it appears | Type |
|---------------|-----------------|------|
| **Artifact definitions** (HL, TS, RF, ONB, REVIEW, RES) | conventions.md §3, glossary.md §Artifact Types | **Full duplication**, glossary adds 1-2 sentences per item |
| **Status flow diagram** | conventions.md §5, glossary.md §Status Flow | **Near-identical** ASCII diagram + table |
| **Execution modes CL/AG** | conventions.md §7, glossary.md §Execution Modes, AGENTS.md, .agent/rules/agents.md, .agent/rules/tfw.md | **5x duplication** across layers |
| **Anti-patterns list** | conventions.md §14, .tfw/README.md §Anti-patterns, handoff.md §Anti-patterns, plan.md footer | **4x duplication**, each instance slightly different subset |
| **Role Lock table** | conventions.md §15, every workflow header | **Duplication by design** (inline enforcement), but conventions table is 11 rows that add no value beyond what workflows say at point-of-use |
| **Context Loading Order** | conventions.md §10, AGENTS.md, .agent/rules/agents.md, .agent/rules/tfw.md, handoff.md, review.md, plan.md, research/base.md | **8x presence**, 3 versions: slim (AGENTS.md), full (handoff/review), reference-only (plan: "Read §10") |
| **Fact Categories table** | conventions.md §10.1 | Single-source ✅ — workflows correctly reference |
| **Scope Budgets table** | conventions.md §6 | Single-source ✅ — config.md registry handles sync |
| **Task naming/numbering** | conventions.md §4, glossary.md §Task Naming | **Duplication**, glossary is subset of conventions |
| **Compilable Contract** (§16) | conventions.md §16 (3 subsections, ~100 lines) | Standalone concern, never referenced by any workflow at runtime |
| **KNOWLEDGE.md / TECH_DEBT.md / RELEASE.md descriptions** | conventions.md §2, glossary.md | **Duplication** |
| **Workflow summary table** | conventions.md §8 | Useful, no redundancy issue |
| **Tool Adapter pattern** | conventions.md §9, glossary.md §Tool Adapter, §.tfw Directory | **Duplication** |
| **Reference Format** (§16.2) | conventions.md §16.2, glossary.md §Reference Format, §Source Manifest | **Triple source** |
| **Research-specific terms** (Pass, Stage, Read-only AG) | glossary.md | Unique to glossary ✅ |
| **Knowledge infrastructure** (Topic File, Knowledge Gate, Consolidation, Config Sync Registry) | glossary.md | Unique to glossary ✅ |

### 2.3 Inconsistencies found

| # | Location A | Location B | Issue |
|---|-----------|-----------|-------|
| 1 | AGENTS.md §Workflows (line 30) | Actual workflow list | AGENTS.md lists 5 workflows (plan, handoff, review, resume, docs). Actual = 11 workflows. Missing: research, knowledge, init, config, release, update |
| 2 | .agent/rules/agents.md (line 30) | AGENTS.md (line 29) | agents.md says "handoff.md — execution (ONB → develop → RF → REVIEW)". AGENTS.md says "handoff.md — execution (ONB → develop → RF)". The agents.md version is wrong — handoff does NOT produce REVIEW |
| 3 | .agent/rules/tfw.md (line 19) | Actual project | Refers to `.agent/rules/conventions.md` and `.agent/rules/glossary.md` — these files do not exist |
| 4 | conventions.md §10 | conventions.md numbering | §10 Context Loading is numbered after §10.2. Convention numbering is non-sequential: §10.1, §10.2 come before §10 |
| 5 | conventions.md §11 | conventions.md §6 | §11 Quality Standard references Design Rules P10-P13 — these P-numbers are from KNOWLEDGE.md, not from conventions.md itself. Unclear reference for new users |

### 2.4 What can be cut without loss

| Block | Lines | Proposal | Rationale |
|-------|-------|----------|-----------|
| glossary.md: Artifact Types (full definitions) | ~20 | Replace with 1-line per artifact + "→ conventions.md §3" | Full defs exist in conventions |
| glossary.md: Status Flow (diagram + text) | ~12 | Replace with 1-line + "→ conventions.md §5" | Identical diagram |
| glossary.md: Execution Modes (full defs) | ~5 | Keep as-is (short, useful standalone) | Already compact |
| glossary.md: Task Naming | ~5 | Replace with 1-line + ref | Subset of conventions §4 |
| glossary.md: Reference Format, Source Manifest, Compilable Contract | ~10 | Replace with 1-line + ref | Definitions for build-time concepts |
| glossary.md: TECH_DEBT.md, KNOWLEDGE.md, RELEASE.md entries | ~6 | Keep as-is | Short, unique angle |
| conventions.md: Compilable Contract §16 | ~100 | Move to `.tfw/compilable_contract.md` | Never read by workflows at runtime. Build-time concern only |
| conventions.md: Anti-patterns §14 | ~15 | Keep inline. Remove duplicates from README and handoff | Single authoritative list |
| conventions.md: §10 numbering | — | Renumber: §10 → §10.3 or move §10 before §10.1 | Fix broken numbering |

## 3. Target State (To-Be)

### 3.1 Result Visualization

```
BEFORE (6,500 words across 3 files, heavy overlap):

┌─────────────────────┐   ┌──────────────────┐   ┌───────────────┐
│   conventions.md    │   │   glossary.md    │   │ .tfw/README   │
│   426 lines         │   │   191 lines      │   │ 144 lines     │
│                     │   │                  │   │               │
│ §3 Artifacts ◄──────┼───┤ Artifacts ◄──────┼───┤               │
│ §5 Statuses ◄───────┼───┤ Statuses         │   │               │
│ §7 CL/AG ◄──────────┼───┤ CL/AG            │   │               │
│ §14 Anti-patterns ◄─┼───┼──────────────────┼───┤ Anti-patterns │
│ §10 Context Load ◄──┼───┼──────────────────┼───┼─ 8x copies    │
│ §16 Compilable(100) │   │ Ref Format       │   │               │
└─────────────────────┘   └──────────────────┘   └───────────────┘

AFTER (~5,200 words, no overlap):

┌──────────────────────────┐  ┌───────────────────┐  ┌───────────────┐
│   conventions.md (~330)  │  │  glossary.md (~80) │  │ .tfw/README   │
│                          │  │                    │  │ (unchanged)   │
│ §3 Artifacts (SoT)       │  │ One-liners + refs  │  │               │
│ §5 Statuses (SoT)        │  │ Research terms     │  │ "→ conv §14"  │
│ §7 CL/AG (SoT)           │  │ Knowledge terms    │  │               │
│ §10 Facts + Knowledge    │  │ Concept Taxonomy   │  │               │
│ §11 Quality              │  │ Project-Specific   │  │               │
│ §14 Anti-patterns (SoT)  │  │                    │  │               │
│ §15 Role Lock (SoT)      │  │                    │  │               │
│                          │  │                    │  │               │
│ §16 → compilable.md      │  │                    │  │               │
└──────────────────────────┘  └───────────────────┘  └───────────────┘
                                                      ┌─────────────────────────┐
                                                      │ compilable_contract.md  │
                                                      │ (~100 lines, build-time)│
                                                      └─────────────────────────┘
```

**Estimated savings:** ~1,300 words (~20%), elimination of all semantic duplication.

## 4. Phases

### Phase A: Audit & Compress 🔴
- Fix conventions.md section numbering (§10/§10.1/§10.2 ordering)
- Compress glossary.md: replace duplicated definitions with 1-liners + refs
- Extract Compilable Contract (§16) to `.tfw/compilable_contract.md`, leave stub ref in conventions
- Fix inconsistencies (§2.3 items 1-5)
- Deduplicate anti-patterns: conventions.md §14 = authoritative, README links to it, handoff stops copying the full list
- Sync adapter files (.agent/rules/)

### Phase B: Verify & Polish 🟡
- Run `/tfw-config verify` to confirm inline values are in sync
- Review all workflow Context Loading sections — ensure they consistently point to conventions, don't redefine
- Update CHANGELOG

## 5. Definition of Done (DoD)

- ✅ 1. No artifact definition appears in full in both conventions.md and glossary.md
- ✅ 2. Status flow diagram exists in exactly 1 place (conventions.md)
- ✅ 3. Anti-patterns canonical list = conventions.md §14 only; other files link to it
- ✅ 4. conventions.md section numbering is sequential and logical
- ✅ 5. .agent/rules/tfw.md does not reference non-existent files
- ✅ 6. AGENTS.md workflow list is complete (all 11 workflows)
- ✅ 7. Compilable Contract lives in its own file
- ✅ 8. glossary.md ≤ 130 lines (down from 191)
- ✅ 9. conventions.md ≤ 350 lines (down from 426)
- ✅ 10. All adapter copies in .agent/ are synced

## 6. Definition of Failure (DoF)

- ❌ 1. Any workflow breaks because it referenced a removed section
- ❌ 2. Content is lost (meaning disappears, not just moved)
- ❌ 3. New contradictions are introduced

**On failure:** Revert changed file, validate each workflow against its §-references.

## 7. Principles

1. **Single Source of Truth** — every concept defined in exactly 1 file. Others link to it.
2. **Glossary = vocabulary, Conventions = rules** — glossary gives meaning (what is X?), conventions give behavior (when/how to use X). No overlap.
3. **Inline enforcement preserved** — Role Lock headers in workflows stay inline per Design Rules. But the conventions table is the authoritative registry.
4. **No signal loss** — every cut must be traceable (moved to X or "already exists in Y").

## 8. Dependencies
| Dependency | Status |
|------------|--------|
| None | — |

## 9. Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Workflow breaks from removed §-reference | Medium | High | grep all `§` references before cutting |
| Users of external tools (Claude, Cursor) have stale adapters | Low | Medium | Update tfw-update workflow if adapter structure changes |

## 10. RESEARCH Case

### Blind Spots
- **Reading flow patterns** — we identified redundancies statically, but haven't mapped the actual agent reading paths: what each workflow loads, in what order, what it actually uses vs what it loads "just in case"
- Are there circular references or dead-end reads (agent loads X which says "read Y" which says "read X")?
- Where is the common pattern vs where do workflows diverge in their context loading?

### Hypotheses

| # | Hypothesis | Status |
|---|----------|--------|
| H1 | Compilable Contract (§16) is never read by any workflow at runtime — can be safely extracted | confirmed (grep shows no workflow reads §16) |
| H2 | All workflows follow the same 4-step context loading pattern (AGENTS → conventions → glossary → KNOWLEDGE) but then diverge — the divergence points reveal which convention sections are actually needed per role | open |
| H3 | Anti-patterns in .tfw/README.md, handoff.md add unique items not in conventions.md §14 | confirmed — handoff adds executor-specific items, README is a subset. Merger needed. |
| H4 | Glossary is loaded by every workflow (via context loading) but only Research workflows actually need glossary-unique terms (Stage, Pass, OODA); other workflows could skip it entirely | open |

### Risks of Not Researching
- Without reading flow diagrams, compression might cut content that a specific workflow path actually needs
- Divergence points between workflows might reveal a deeper structural issue (not just redundancy but inconsistent behavior)

### Proposed RESEARCH Focus

**Deliverable 1: Reading Flow Diagrams**
For each of 6 core workflows (plan, research, handoff, review, resume, knowledge):
- Mermaid sequence diagram or flowchart showing: agent starts → reads file A → reads section X → branches to file B → etc.
- Include: which convention §-sections are actually referenced (not just "read conventions.md" but "reads §6 Scope Budgets, §14 Anti-patterns")
- Include: adapter entry point → .tfw/ canonical → workflow-specific reads
- Mark: 🟢 unique reads, 🟡 shared with other workflows, 🔴 redundant/duplicate reads

**Deliverable 2: Section Usage Matrix**
Table: rows = conventions.md sections (§1-§16), columns = workflows. Cell = how the workflow uses that section (reads / references / ignores / duplicates content from it).
Goal: identify sections that NO workflow reads at runtime → extraction candidates.

**Deliverable 3: Glossary Dependency Map**
For each glossary term: which workflow(s) actually need it? Does the term exist anywhere else (conventions, workflow inline)?
Goal: separate glossary into "universally needed" vs "workflow-specific" vs "redundant with conventions".

**Deliverable 4: Common Spine vs Divergence Report**
Extract the shared loading pattern across all workflows. Document each divergence point with rationale (is it intentional or drift?).

### Gather focus
- Read every workflow's Context Loading section verbatim
- Read every §-reference in every workflow step (not just headers but inline refs like "see §14", "per §6")
- Check adapter entry points (.agent/rules/, AGENTS.md) for what they trigger

### Extract focus
- Build the matrix and diagrams from gathered data
- Identify: (a) dead sections, (b) circular reads, (c) redundant loads, (d) inconsistent patterns

### Challenge focus
- Test H2: is the common spine real or are we projecting a pattern?
- Test H4: remove glossary from mental model for handoff workflow — what breaks? What term is missing?
- Counter-argument: maybe glossary duplication is USEFUL (self-contained context per workflow) — evaluate this

### Why Not Just...?
- Why not just compress without flow mapping? — Risk of breaking a workflow that depends on a specific section we thought was unused
- Why not just merge glossary into conventions? — Glossary has unique terms (Stage, Pass, Knowledge Gate) that don't fit conventions' structure. Need data to decide.

## 11. Strategic Session Insights

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | User specifically concerned about double-reading — agents loading both conventions AND glossary get duplicate content, wasting context window | process | User, initial request |
| S2 | "Возможно конвенции слишком длинные" — conventions.md at 426 lines / 21KB is at the edge of what's useful as a single-read reference | constraint | User, initial request |
| S3 | User suspects information "сбилось, потерялось, запуталось" — the organic growth over 27 tasks has introduced entropy | philosophy | User, initial request |
| S4 | User wants reading flow diagrams (seq diagrams) — visual mapping of what each workflow reads from where. Not just static redundancy but dynamic flow analysis | process | User, mid-planning comment |

---

*HL — TFW-29: Consistency Audit | 2026-04-08*
