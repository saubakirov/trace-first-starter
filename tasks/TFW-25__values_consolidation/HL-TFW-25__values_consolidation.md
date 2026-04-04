# HL — TFW-25: Values & Principles Consolidation

> **Date**: 2026-04-04
> **Author**: Coordinator (AI)
> **Status**: 📝 HL_DRAFT — Updated after RESEARCH
> **RES**: [RES-TFW-25](RES__TFW-25__values_consolidation.md)

---

## 1. Vision

TFW accumulated 14 principles and 33 decisions across 24 tasks. They live in 3 separate places (README Values, KNOWLEDGE.md §0, knowledge/ topic files) with heavy duplication and no clear hierarchy. The README Values section — the philosophical face of TFW — is stuck at v1 level with 5 generic entries that don't reflect the framework's real values.

**Impact:** New agents and users read README Values and get a shallow picture. Real principles are buried in KNOWLEDGE.md tables. Knowledge files duplicate what's already self-evident from conventions and workflows.

> "The values section should tell you what TFW believes. Right now it tells you what any framework believes."

## 2. Current State (As-Is)

### Three-layer duplication

| Layer | File | Lines | Role |
|-------|------|-------|------|
| Framework values | `.tfw/README.md` §Values | 26 lines, 5 items | Public philosophy |
| Project principles | `KNOWLEDGE.md` §0 | 17 lines, 14 items (P1-P14) | Internal principle registry |
| Verified facts | `knowledge/*.md` | 57 lines, 29 facts | Knowledge consolidation output |

### Duplication map (6 concepts appear 2-3 times)

| Concept | README Values | KNOWLEDGE P# | knowledge/ fact | conventions/workflows |
|---------|-------------|-------------|----------------|-----------------------|
| Anti-sycophancy | ✅ Candor Over Flattery | P9 (coordinator mindset) | philosophy/F3 | AGENTS.md conduct |
| Ref-inside-step | — | P11, P12 | convention/F5 | plan.md, base.md (inline) |
| Naming > Explanation | — | D28 | process/F5 | — |
| Filesystem = state | — | P14 | convention/F9, philosophy/F4 | conventions §4, base.md |
| Token density | — | P10 | constraint/F2 | base.md limits table |
| 4 roles | — | D30 | process/F9 | conventions §15, glossary |

### P1-P14 classification (not all are "principles")

| Tier | Items | What they really are |
|------|-------|---------------------|
| **Values** (why TFW exists) | P1, P3, P7, P9 | Traces > code, narrative > DRY, role separation, quality > speed |
| **Design principles** (how TFW is built) | P2, P5, P8, P14 | Index don't duplicate, meta-awareness, research ≠ checklist, filesystem = gate |
| **Implementation rules** (how to follow TFW) | P4, P6, P10, P11, P12, P13 | Glossary/conventions split, lightweight docs, token density, inline enforcement, DNA/library, progressive disclosure |

**Problem:** Implementation rules (P10-P13) are recorded as "principles" but they are engineering patterns. They belong in conventions.md, not in a philosophy section.

### KNOWLEDGE.md bloat analysis (179 lines)

| Section | Lines | Redundancy |
|---------|-------|-----------|
| §0 Principles (P1-P14) | 17 | Many are implementation details, not principles |
| §1 Architecture Map | 12 | Duplicates file listing in conventions.md §2 |
| §2 Key Artifacts | 20 | Links to task files — useful index |
| §3 Legacy & Deprecation | 38 | Growing linearly with every task. 50% resolved items |
| §4 Tech Stack | 8 | 4 lines of content |
| §5 Project Facts | 10 | Index to knowledge/ topic files |

§3 Legacy = 38 lines, 17 resolved. Resolved items = historical but take space. §4 Tech Stack = trivially obvious from the repo.

### knowledge/ topic files (29 facts)

Some facts are now self-evident from the code they describe:
- convention/F9 (filesystem state machine) = obvious from conventions.md §4 + base.md Step 0
- convention/F10 (RES = synthesis) = obvious from templates/RES.md structure
- process/F9 (4 roles) = obvious from conventions.md §15
- process/F10 (Resume Protocol) = obvious from base.md Step 0

## 3. Target State (To-Be)

### 3.1 Result Visualization

**Principle hierarchy (after consolidation):**

```
.tfw/README.md §Values and Principles  ← PUBLIC: what TFW believes (5-8 items, narrative)
  │
  ├── Traces Over Code                   (was: P1, exists)
  ├── Candor Over Flattery               (exists, enrich with P9)
  ├── Completeness Over Speed            (exists)
  ├── Structural Enforcement             (NEW: from P14, P8, philosophy/F4)
  ├── Naming Creates Behavior            (NEW: from D28, process/F5)
  ├── Single Source of Truth             (exists)
  ├── Portability                        (exists)
  └── Determinism and Safety             (exists)

KNOWLEDGE.md §0 Principles              ← INTERNAL: battle-tested design rules (compact)
  │
  ├── P1–P3 (philosophy tier) → STAY (compact)
  ├── P4–P6 (implementation) → REMOVE (obvious from conventions.md)
  ├── P7–P9 (roles/quality) → MERGE into README Values / STAY compact
  ├── P10–P13 (engineering patterns) → MOVE to conventions.md or REMOVE
  └── P14 (filesystem state) → MOVE to README Values as "Structural Enforcement"

KNOWLEDGE.md §3 Legacy                  ← PRUNE: remove resolved items
KNOWLEDGE.md §4 Tech Stack              ← REMOVE: obvious from repo

knowledge/ topic files                   ← PRUNE: remove facts now obvious from code
```

**Before → After sizes:**

```
                        BEFORE    AFTER
KNOWLEDGE.md            179 lines  ~115 lines  (-36%)
  §0 Principles         17 lines   ~8 lines    (14 → 7 items)
  §3 Legacy             38 lines   ~20 lines   (35 → 17 items)
  §4 Tech Stack         8 lines    0 lines     (removed)
README.md §Values       26 lines   ~40 lines   (5 → 8 items)
knowledge/ facts        29 facts   18 facts    (-38%)
```

## 4. Phases

### Phase A: Audit & Consolidate 🔴
1. **`.tfw/README.md` §Values** — rewrite to 8 items: add "Traces Over Code", "Structural Enforcement", "Naming Creates Behavior". Rename "Determinism and Safety" → "Honesty Over Convincingness" (rewrite as genuine value, not rule list). Enrich "Candor" with P9 coordinator mindset
2. **`KNOWLEDGE.md` §0** — prune from 14 → 7 items. Remove P4, P6, P10-P13. Promote P14 to README. Compress remaining to 1-liners
3. **`KNOWLEDGE.md` §3** — remove 18 resolved Legacy items (keep 17 recent: TFW-22+)
4. **`KNOWLEDGE.md` §4** — remove entire section
5. **`knowledge/*.md`** — prune 11 self-evident facts (6 convention, 5 process). Keep convention/F5 (named pattern value per D28)

### Phase B: Cross-reference & Apply 🟡
1. **`.tfw/conventions.md`** — absorb P10-P13 content into existing sections or add §X "Design Rules"
2. **`AGENTS.md`** — verify alignment with updated values
3. **Adapters** — sync

## 5. Definition of Done (DoD)

- ✅ 1. README §Values has exactly 8 values including "Traces Over Code", "Structural Enforcement", "Naming Creates Behavior", "Honesty Over Convincingness"
- ✅ 2. KNOWLEDGE.md §0 has exactly 7 principles (no implementation details)
- ✅ 3. KNOWLEDGE.md §3 Legacy: 18 resolved items removed (17 remain)
- ✅ 4. KNOWLEDGE.md §4 Tech Stack: section removed
- ✅ 5. KNOWLEDGE.md total ≤120 lines
- ✅ 6. knowledge/ topic files: 18 facts (11 self-evident ones removed)
- ✅ 7. No principle/value appears in >2 places with full text
- ✅ 8. conventions.md or README absorbs P10-P13 content
- ✅ 9. Cross-references work (no dead refs)

## 6. Definition of Failure (DoF)

- ❌ 1. Values become a list of 15+ items (values ≠ encyclopedia)
- ❌ 2. Pruning removes something that's NOT obvious from other artifacts
- ❌ 3. README Values section becomes longer than Anti-patterns section below it

**On failure:** Restore from git. Values = 8 max. If in doubt, keep in KNOWLEDGE.md rather than promote to README.

## 7. Principles

1. **Values = beliefs, not rules** — README Values answers "what does TFW believe?" not "how does TFW work?"
2. **Promote up, don't duplicate** — if a fact is now obvious from code/conventions, remove from knowledge/ rather than keeping "for completeness"
3. **Compact > comprehensive** — 8 strong values > 15 complete ones

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| TFW-22 (source of P12, P13, D28) | ✅ Done |
| TFW-24 (source of P14, D30-D33) | ✅ Done |
| TFW-18 (knowledge consolidation infrastructure) | ✅ Done |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Pruning removes something valuable | Low | High | Git history. If in doubt, compress rather than delete |
| README Values grows too large | Medium | Medium | Hard cap: 8 values max. "Determinism and Safety" = merge candidate |
| P10-P13 migration creates dead P# refs in task HLs | Low | Low | Historical refs stay valid (source column unchanged) |

## 10. RESEARCH Case

### Blind Spots
- How do other frameworks (LangChain, CrewAI docs, Cursor rules) structure their values/principles sections?
- Is the 3-tier split (values/design/implementation) the right taxonomy, or is 2-tier better?

### Hypotheses

| # | Hypothesis | Status |
|---|----------|--------|
| H1 | P10-P13 are implementation rules, not principles — they belong in conventions.md | ✅ confirmed (RES R3) |
| H2 | ≥5 knowledge/ facts are now self-evident from code and can be safely removed | ✅ confirmed — 11 facts (RES R4) |
| H3 | README Values section should stay under 8 items to maintain narrative impact | ✅ confirmed — exactly 8 (RES R2) |

> **Filter:** Each hypothesis: "If proven false, would our approach change?" 
> H1: Yes — if they are principles, they stay in §0. H2: Yes — if not self-evident, we keep them. H3: Yes — more items might be needed.

### Risks of Not Researching
Task is mostly internal audit — facts are in the codebase. Low risk of unknown unknowns. External research could validate the tier taxonomy.

### Proposed RESEARCH Focus
1. **Gather**: external framework docs — how do they structure principles? 
2. **Extract**: exact list of removable facts from knowledge/
3. **Challenge**: is 3-tier taxonomy correct?

### Why Not Just...?
- Why not just delete everything and rewrite? — Lose provenance. Source links in P# and D# are valuable for tracing decisions
- Why not keep everything as-is? — KNOWLEDGE.md grows ~15 lines/task. At TFW-30 it'll be 200+ lines and unreadable

---

*HL — TFW-25: Values & Principles Consolidation | 2026-04-04*
