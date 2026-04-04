# HL — TFW-24: Researcher Role & RES State Machine

> **Date**: 2026-04-04
> **Author**: Coordinator
> **Status**: 📝 HL_DRAFT — Awaiting review

---

## 1. Goal & Value

**Goal:** Split Researcher into a standalone role with dedicated workflow, and enforce research stage completion through filesystem-level state machine (subfolder with stage files).

**Value:** Research becomes crash-resilient, multi-chat resumable, and structurally impossible to skip stages. Role confusion between Coordinator and Researcher is eliminated.

> "File existence = state machine. Agent can't skip stages — no file = not done."

## 2. Current State (As-Is)

| Problem | Evidence | Impact |
|---------|----------|--------|
| Research = "Coordinator in Research Mode" | base.md L7: `ROLE LOCK: COORDINATOR (Research Mode)` | User confused Plan vs Research in TFW-24 inception |
| Gates are decorative | `→ User decision: ___` — 6/6 unfilled in TFW-23 | No enforcement, no state persistence |
| No resume inside research | `/tfw-resume` at pipeline level only | Crash mid-stage = chaos |
| Gate responses lost with chat | Approvals exist only in chat | New chat = no record |
| 3 roles cover 4 functions | Coordinator = planning + research | Same problem TFW-8 solved for Reviewer |

### Historical pattern

```
TFW-8:  Executor + Reviewer merged → self-review → Reviewer role extracted
TFW-24: Coordinator + Researcher merged → role confusion + crash fragility → Researcher role extracted
```

## 3. Target State (To-Be)

4 roles: **Coordinator** (HL, TS), **Researcher** (RES, stage files), **Executor** (ONB, RF, code), **Reviewer** (REVIEW). Research uses subfolder with stage files as filesystem-level state machine.

### 3.1 Result Visualization

**Role separation:**

```
BEFORE (3 roles):                    AFTER (4 roles):
  Coordinator ─┬─ HL, TS              Coordinator ── HL, TS
               └─ RES (mode switch)   Researcher ─── RES, stage files  ← NEW
  Executor ──── ONB, RF, code         Executor ───── ONB, RF, code
  Reviewer ──── REVIEW                Reviewer ───── REVIEW
```

**Research subfolder (filesystem = state machine):**

```
tasks/TFW-24__res_state_machine/
  HL-TFW-24__res_state_machine.md
  research/                           ← state machine
    briefing.md                       ← exists = briefing done
    gather.md                         ← exists = gather done
    extract.md                        ← exists = extract done
    challenge.md                      ← exists = challenge done
  RES__TFW-24__res_state_machine.md   ← exists = synthesis done
```

**Resume algorithm (Step 0 in base.md):**

```
1. research/ exists?  → NO: start fresh
2. Which files exist? → resume from first missing
3. RES exists?        → research complete, proceed to Closure
```

**Pipeline handoff:**

```
Coordinator (plan.md)        Researcher (base.md)         Coordinator (plan.md)
  HL approved                  reads HL                     reads RES Closure
  "Start /tfw-research"       runs stages                  updates HL
  ── STOP ──                   writes RES                   writes TS
                               ── STOP ──
```

## 4. Phases

### Phase A: Researcher Role + Subfolder State Machine 🔴
- Researcher role in conventions.md §15, §8, glossary.md
- `research/base.md` Role Lock → `RESEARCHER`
- Step 0 (Resume Protocol) in base.md
- Research subfolder convention in conventions.md §4
- Stage file structure (lightweight: Goal ref + Findings + Checkpoint)
- Step 7 → Synthesis step (write final RES from stage files)
- `plan.md` Step 6 → explicit handoff to Researcher with Hard Stop
- `templates/RES.md` → synthesis format (Decisions, Hypotheses, HL Recommendations, FC, Conclusion)
- HL template §1 → Goal & Value structured fields
- HL template §2, §5 → domain-agnostic language
- PROJECT_CONFIG.yaml RES status role → researcher
- Adapter sync

## 5. Definition of Done (DoD)

- ✅ 1. Researcher role defined in `conventions.md` §15 (Role Lock table) and §8 (Workflows table)
- ✅ 2. Researcher role defined in `glossary.md` with Permitted/Forbidden artifacts
- ✅ 3. `research/base.md` Role Lock = `🔒 ROLE LOCK: RESEARCHER`
- ✅ 4. `research/base.md` has Step 0: Resume Protocol (~30 words)
- ✅ 5. `research/base.md` Step 3 → creates `research/` subfolder with stage files
- ✅ 6. `research/base.md` Step 7 → Synthesis step (consolidate stage files → final RES)
- ✅ 7. `conventions.md` §4 → research subfolder convention documented
- ✅ 8. Stage file structure defined: Goal ref + Findings + Checkpoint
- ✅ 9. `plan.md` Step 6 → handoff to Researcher role (not self-switch), Hard Stop
- ✅ 10. `templates/RES.md` → synthesis format (no stage sections, different structure from stage files)
- ✅ 11. `templates/HL.md` §1 → Goal & Value structured fields
- ✅ 12. `templates/HL.md` §2, §5 → domain-agnostic language
- ✅ 13. `PROJECT_CONFIG.yaml` RES status role = `researcher`
- ✅ 14. No references to "Coordinator (Research Mode)" remain in `.tfw/`
- ✅ 15. Adapters synced (`.agent/`, `.claude/`)
- ✅ 16. Word count: base.md ≤ 600 words

## 6. Definition of Failure (DoF)

- ❌ 1. base.md exceeds 600 words → compress Step 0 or move subfolder logic to conventions ref
- ❌ 2. Final RES structure too similar to stage files → copy-paste risk, synthesis fails
- ❌ 3. Role separation creates pipeline ambiguity at handoff → clarify in plan.md

**On failure:** Compress. Ref-inside-step for subfolder details. Reduce stage file structure to bare minimum.

## 7. Principles

1. **One role, one artifact type** — Researcher writes RES + stage files. Coordinator writes HL/TS. No mode switching
2. **Filesystem = state machine** — File existence is enforcement. No parsing, no format compliance, no update discipline. Missing file = stage not done
3. **Synthesis, not aggregation** — Final RES has different structure from stage files. Impossible to copy-paste. Forces integrated thinking
4. **Resume from anywhere** — Step 0: read subfolder → know exact state → continue. Zero dependency on chat history

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| TFW-22 (modular research architecture) | ✅ Done |
| TFW-23 (English templates) | ✅ Done |
| TFW-8 (Reviewer role split precedent) | ✅ Done |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| base.md exceeds 600 words | Medium | Medium | Step 0 = ~30 words. Synthesis instruction = ~20. Total ~70 new |
| Consolidation = copy-paste not synthesis | Medium | High | RES template structure ≠ stage file structure (D2) |
| Role split adds pipeline friction | Low | Medium | Same pattern as TFW-8. Clean handoff/handback |
| Crash mid-stage-file write | Low | Low | Accept partial file. Agent reads content, assesses completeness (C1) |

## 10. RESEARCH Case

### Blind Spots
- ~~How should Step 0 work?~~ → Answered (D1: filesystem check)
- ~~What format for state tracking?~~ → Answered (D1: file existence, not table)

### Hypotheses

| # | Hypothesis | Status |
|---|----------|--------|
| H1 | State in RES file sufficient for crash recovery | ✅ confirmed → evolved to D1: subfolder = state machine |
| H2 | Researcher = pure relabeling of Coordinator Research Mode | 🟡 partial — relabeling yes, but subfolder architecture = new workflow logic |
| H3 | State Table format within 10 lines | ⚫ superseded — file existence replaces table |
| H4 | Word budget ≤600 achievable | ✅ confirmed — 518 + ~70 = ~588 |

### Risks of Not Researching
N/A — research completed.

### Proposed RESEARCH Focus
N/A — research completed. Key findings: D1 (subfolder = state machine), D2 (synthesis ≠ aggregation), D3 (absolute role split), D4 (Goal & Value in HL), D5 (stage file naming).

---

*HL — TFW-24: Researcher Role & RES State Machine | 2026-04-04*
