# Research Workflow Architecture

> **Proposed in:** TFW-22 (Coordinator & Research Enrichment)
> **Status:** Draft — subject to change during TS phase

---

## File Structure

```
.tfw/
├── PROJECT_CONFIG.yaml
│   └── tfw.research:
│       ├── max_questions_per_turn: 3
│       ├── max_passes: 3
│       ├── max_web_queries_per_stage: 5
│       ├── max_files_per_stage: 15
│       ├── default_mode: focused
│       └── modes:
│           ├── focused:
│           │   ├── loops_per_stage: 1
│           │   └── verify_user_tech_claims: true
│           └── deep:
│               ├── loops_per_stage: 3
│               ├── verify_user_tech_claims: true
│               └── require_counter_evidence: true
│
├── workflows/
│   └── research/
│       ├── base.md          ← Entry point: Role Lock, Mindset,
│       │                       Core Algorithm, Checkpoint Protocol,
│       │                       Closure + mode selection step
│       ├── focused.md       ← Режим: scoped investigation
│       │                       1 OODA loop per stage
│       │                       "Scan → assess → report"
│       └── deep.md          ← Режим: hypothesis-driven
│                               multi-loop per stage
│                               "Hypothesize → test → revise → test"
│
├── templates/
│   ├── HL.md                ← +§3.1 Визуализация результата
│   │                           +§10 Гипотезы и обоснование RESEARCH
│   └── RES.md               ← +Hypotheses table
│                                +Checkpoint Protocol (Sufficiency Verdict)
│
├── conventions.md           ← Ref targets: §5, §6, §10, §14, §15
└── glossary.md              ← +OODA Stage Loop, Checkpoint Gate,
                                 Sufficiency Verdict
```

## Algorithm Flow

```
User вызывает /tfw-research
          │
          ▼
┌─────────────────────────────────────────────────────────┐
│  base.md — CORE ALGORITHM                               │
│                                                         │
│  🔒 Role Lock: Coordinator (research mode)              │
│                                                         │
│  MINDSET: "Critical thinking partner. Find what's       │
│  missing. Healthy critique. Show blind spots."          │
│                                                         │
│  Step 1: Load context                                   │
│    → ref: conventions.md §10                            │
│                                                         │
│  Step 2: Select mode                                    │
│    → read PROJECT_CONFIG.yaml tfw.research.default_mode │
│    → present to user: "Recommend [focused/deep].        │
│      Reason: [specific]. Switch?"                       │
│    → 🛑 WAIT                                            │
│    → load mode file: research/{mode}.md                 │
│                                                         │
│  Step 3: Create RES file                                │
│    → ref: templates/RES.md                              │
│                                                         │
│  Step 4: Briefing Protocol                              │
│    → Research Plan (3-5 bullets)                        │
│    → Hypotheses from HL §10 (if pipeline mode)          │
│    → Scope intent                                       │
│    → Guiding questions (≤3)                             │
│    → 🛑 WAIT                                            │
│                                                         │
│  Step 5: Run stages (Gather → Extract → Challenge)      │
│    ┌─── FOR EACH STAGE ──────────────────────────┐      │
│    │                                              │      │
│    │  ╔═══════════════════════════════════╗       │      │
│    │  ║  OODA STAGE LOOP                  ║       │      │
│    │  ║  (loops_per_stage from YAML)      ║       │      │
│    │  ║                                   ║       │      │
│    │  ║  OBSERVE: search / read / ask     ║       │      │
│    │  ║      │                            ║       │      │
│    │  ║      ▼                            ║       │      │
│    │  ║  ORIENT: interpret against        ║       │      │
│    │  ║    existing understanding.        ║       │      │
│    │  ║    "Confirms or challenges?"      ║       │      │
│    │  ║      │                            ║       │      │
│    │  ║      ▼                            ║       │      │
│    │  ║  DECIDE: Sufficiency Verdict      ║       │      │
│    │  ║    → run checkpoint criteria      ║       │      │
│    │  ║    → ALL criteria met?            ║       │      │
│    │  ║      │         │                  ║       │      │
│    │  ║     YES       NO                  ║       │      │
│    │  ║      │         │                  ║       │      │
│    │  ║      │    loop_count < max?       ║       │      │
│    │  ║      │      │        │            ║       │      │
│    │  ║      │     YES      NO            ║       │      │
│    │  ║      │      │        │            ║       │      │
│    │  ║      │      ▼        ▼            ║       │      │
│    │  ║      │   ACT: update RES,         ║       │      │
│    │  ║      │   formulate questions      ║       │      │
│    │  ║      │      │                     ║       │      │
│    │  ║      │      └───→ OBSERVE (loop)  ║       │      │
│    │  ║      │                            ║       │      │
│    │  ║      ▼                            ║       │      │
│    │  ║  STAGE CHECKPOINT                 ║       │      │
│    │  ║    → present findings to user     ║       │      │
│    │  ║    → questions (≤3)               ║       │      │
│    │  ║    → 🛑 WAIT for user response    ║       │      │
│    │  ╚═══════════════════════════════════╝       │      │
│    │                                              │      │
│    └──────────────────────────────────────────────┘      │
│                                                         │
│  Step 6: Final Checkpoint                               │
│    → Sufficiency Check (overall)                        │
│    → 🛑 WAIT                                            │
│                                                         │
│  Step 7: Closure Protocol                               │
│    → HL Update Recommendations                          │
│    → Fact Candidates                                    │
│    → 🛑 WAIT                                            │
│                                                         │
│  Footer: Rules (compact) + ref: conventions.md §14      │
└─────────────────────────────────────────────────────────┘
```

## Mode Files

### focused.md — "Scan → Assess → Report"

**When:** Topic is clear, specific question, need quick answer.

| Setting | Value |
|---------|-------|
| OODA loops per stage | 1 |
| Verify user tech claims | yes (1x) |
| Require counter-evidence | no |
| Max turns per stage | 2 |
| Min decisions per stage | 1 |

**Checkpoint criteria:**
- ☐ External source used?
- ☐ Briefing gap closed?

### deep.md — "Hypothesize → Test → Revise → Test"

**When:** Many unknowns, hypotheses from HL §10, architectural decisions.

| Setting | Value |
|---------|-------|
| OODA loops per stage | up to 3 (YAML) |
| Verify user tech claims | yes (2x) |
| Require counter-evidence | yes |
| Min decisions per stage | 2 |
| Min hypotheses tested | 1 per stage |

**Checkpoint criteria:**
- ☐ External source used?
- ☐ Briefing gap closed?
- ☐ Hypothesis tested?
- ☐ Counter-evidence sought?

**Metacognitive check (deep only):**
"Did I discover something new, or just confirm what I already knew?"

## Checkpoint Protocol (Sufficiency Verdict)

Two-level checkpoint criteria:

### Level 1: Generic (in base.md, always apply)
- ☐ External source used? (not project-files only)
- ☐ Briefing gap closed? (at least 1)

### Level 2: Mode-specific (in mode file, YAML-configurable)
- Focused: none additional
- Deep: hypothesis tested + counter-evidence sought

### Format in RES

```markdown
### Checkpoint: Gather
Sufficiency Verdict:
- [x] External source used: web search for ClearThought docs
- [x] Briefing gap closed: Q1 (word budget) answered
- [ ] Hypothesis tested: H2 still open          ← deep only
- [x] Counter-evidence sought: checked TFW-19   ← deep only
Stage complete: NO → need 1 more loop for H2
```

## Trust Protocol

| Input Type | Trust Level | Agent Behavior |
|-----------|-------------|----------------|
| Business/people/domain | Trust as-is | Ask clarifying questions only |
| Technical approach | Verify externally | Cross-check 1-2x (YAML: verify_user_tech_claims) |
| Performance numbers | Verify empirically | Test, benchmark, or find evidence |
| "I tried this before" | Trust the outcome | Verify the reason (why did it fail?) |

## Adapter Sync

```
.agent/workflows/tfw-research.md  → copy of base.md
.claude/commands/tfw-research.md  → copy of base.md
(mode files do NOT need adapter copies — loaded via ref from base.md)
```
