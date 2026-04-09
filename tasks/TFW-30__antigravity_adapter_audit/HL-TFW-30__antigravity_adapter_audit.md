# HL — TFW-30: Antigravity Adapter Audit

> **Date**: 2026-04-09
> **Author**: Coordinator (Antigravity session)
> **Status**: 📝 HL_DRAFT — Awaiting review

---

## 1. Vision
The Antigravity adapter is fully aligned with TFW: workflows compose cleanly, Skills provide progressive disclosure for templates/context, and Planning Mode is either harmonized or explicitly controlled — no silent conflicts. The adapter is the reference implementation, not an afterthought.

**Impact:** Agents in Antigravity follow TFW protocols without wasted tokens, hidden artifacts, or broken context loading. Users get predictable behavior across all TFW tools.

> "I run `/tfw-plan` in Antigravity and the agent does exactly what it does in Claude Code — same quality, same traces, no surprises."

## 2. Current State (As-Is)

### Adapter structure
```
.agent/
├── rules/
│   ├── agents.md        (AGENTS.md duplicate — always-on)
│   └── tfw.md           (always-on, context loading pointer)
└── workflows/
    ├── tfw-plan.md      (FULL COPY of .tfw/workflows/plan.md)
    ├── tfw-handoff.md   (FULL COPY)
    ├── tfw-research.md  (FULL COPY)
    ├── tfw-review.md    (FULL COPY)
    ├── tfw-resume.md    (FULL COPY)
    ├── tfw-docs.md      (FULL COPY)
    ├── tfw-knowledge.md (FULL COPY)
    ├── tfw-config.md    (FULL COPY)
    ├── tfw-release.md   (FULL COPY)
    ├── tfw-update.md    (FULL COPY)
    ├── tfw-init.md      (FULL COPY)
    └── tfw-task.md      (meta-workflow)
```

### Quantified problems

| Problem | Evidence | Impact |
|---------|----------|--------|
| **12 full-copy workflows** | `.agent/workflows/` = copies of `.tfw/workflows/` | Drift guaranteed on any update. Adapter README still says `cp research.md` (wrong path since TFW-22) |
| **Skills = unused** | No `.agent/skills/` folder exists | Zero progressive disclosure — all context loaded always-on via rules |
| **Planning Mode conflict** | Antigravity system prompt enforces `implementation_plan.md` → `task.md` → `walkthrough.md` | TFW has HL/TS/RF. Empirical data: 105 conversations, 54 planning artifacts created. **0 artifacts in TFW-specific sessions** (c22231b1, 530041c1, b54e04b8). TFW rules suppress Planning Mode silently |
| **No GEMINI.md** | Only `AGENTS.md` + `tfw.md` in `.agent/rules/` | Miss the highest-priority rule slot that Antigravity provides |
| **No turbo annotations** | None of the 12 workflows use `// turbo` | Safe read-only steps (context loading, file reading) require manual approval |
| **No workflow composition** | Workflows don't use `Call /other-workflow` | `tfw-task.md` mentions it conceptually but doesn't use proper syntax |

### Planning Mode — empirical analysis

```
Total conversations:           105
Planning artifacts found:       54   (impl_plan: 12, task: 32, walkthrough: 10)
Artifact rate:                  51%

TFW-specific sessions checked:  3    (consistency audit conversations)
Planning artifacts in TFW:      0    (0%)

Current session (TFW active):   0 artifacts created
```

**Inversion: what would happen WITHOUT TFW rules?**
→ Antigravity would create `implementation_plan.md` for complex tasks, `task.md` for tracking, `walkthrough.md` for summaries. This is a **useful built-in capability** that TFW rules silently suppress.

### Inversion Analysis: Where TFW *Hurts* in Antigravity

| What TFW does | What Antigravity expects | Conflict |
|---|---|---|
| Rules load conventions.md, glossary.md at session start | Progressive disclosure: load heavy context only when needed | Token waste on every session, even for simple questions |
| 12 copied workflows in `.agent/workflows/` | Workflows should be self-contained or reference canonical sources | Drift. `tfw-update` must re-copy 12 files — fragile |
| HL/TS/RF written to `tasks/` folder on disk | Planning artifacts written to `brain/<conv-id>/` | Parallel systems. Double bookkeeping if both active |
| Role Lock (Coordinator can't write code) | Planning Mode blocks code during planning | Compatible — actually aligned |
| No skills | Skills = progressive disclosure mechanism | Missed optimization: templates could be skills |

## 3. Target State (To-Be)

### 3.1 Result Visualization

```
BEFORE (current):                      AFTER (target):

.agent/                                .agent/
├── rules/                             ├── rules/
│   ├── agents.md (always-on)          │   ├── agents.md (always-on)
│   └── tfw.md    (always-on)          │   └── tfw.md    (always-on, lighter)
└── workflows/                         ├── skills/
    ├── tfw-plan.md    ← FULL COPY     │   ├── tfw-conventions/
    ├── tfw-handoff.md ← FULL COPY     │   │   └── SKILL.md  (auto: when TFW task)
    ├── tfw-research.md← FULL COPY     │   └── tfw-templates/
    ├── tfw-review.md  ← FULL COPY     │       └── SKILL.md  (auto: when writing HL/TS/RF)
    ├── ...11 more copies...           └── workflows/
    └── tfw-task.md                        ├── tfw-plan.md     ← THIN ADAPTER
                                           ├── tfw-handoff.md  ← THIN ADAPTER
                                           ├── tfw-research.md ← THIN ADAPTER  
                                           ├── tfw-review.md   ← THIN ADAPTER
                                           ├── tfw-resume.md   ← THIN ADAPTER
                                           ├── tfw-docs.md     ← THIN ADAPTER
                                           ├── tfw-knowledge.md← THIN ADAPTER
                                           ├── tfw-config.md   ← THIN ADAPTER
                                           ├── tfw-release.md  ← THIN ADAPTER
                                           ├── tfw-update.md   ← THIN ADAPTER
                                           ├── tfw-init.md     ← THIN ADAPTER
                                           └── tfw-task.md     ← META (uses Call)

Thin adapter pattern (each ~15 lines):
┌──────────────────────────────────┐
│ ---                              │
│ description: TFW Plan — ...      │
│ ---                              │
│ 🔒 ROLE LOCK: COORDINATOR       │
│                                  │
│ // turbo                         │
│ 1. Read `.tfw/workflows/plan.md` │
│ 2. Follow ALL steps exactly      │
│ 3. Read referenced templates     │
│    from `.tfw/templates/`        │
│                                  │
│ Source of truth:                  │
│   `.tfw/workflows/plan.md`       │
└──────────────────────────────────┘

Planning Mode strategy:
┌─────────────────────────────────────────────┐
│ Antigravity Planning Mode vs TFW            │
│                                             │
│ Option A: Suppress (current — silent)       │
│ Option B: Harmonize (map HL→plan, TS→task)  │
│ Option C: Coexist (let both run)            │
│                                             │
│ → Needs RESEARCH to decide                  │
└─────────────────────────────────────────────┘
```

## 4. Phases

### Phase A: Core Adapter Refactor 🔴
- Convert 12 full-copy workflows to thin adapters
- Add `// turbo` annotations to safe read-only steps
- Validate that `/tfw-plan`, `/tfw-handoff` etc. still work correctly
- Update `.tfw/adapters/antigravity/README.md` to reflect new pattern

### Phase B: Skills Integration 🟡
- Create `tfw-conventions` skill (auto-activate on TFW task context)
- Create `tfw-templates` skill (auto-activate when writing HL/TS/RF/ONB/REVIEW)
- Lighten always-on rules (remove heavy context loading)
- Test progressive disclosure: verify skills activate correctly

### Phase C: Planning Mode Strategy 🟡
- RESEARCH: test Planning Mode interaction empirically
- Decide: suppress / harmonize / coexist
- Implement chosen strategy via rules or workflow adjustments
- Document the decision as Architecture Decision

## 5. Definition of Done (DoD)

- ✅ 1. All 12 workflows are thin adapters (≤20 lines each), pointing to `.tfw/workflows/`
- ✅ 2. At least 1 skill created and demonstrably auto-activating
- ✅ 3. Planning Mode interaction documented as Architecture Decision (D36+)
- ✅ 4. `// turbo` on context-loading steps in all workflows
- ✅ 5. `.tfw/adapters/antigravity/` README and templates updated
- ✅ 6. No regression: `/tfw-plan` still produces HL artifact correctly

## 6. Definition of Failure (DoF)

- ❌ 1. Thin adapters don't trigger workflow reading (agent ignores `Read .tfw/workflows/plan.md`)
- ❌ 2. Skills don't auto-activate in practice (description matching fails)
- ❌ 3. Planning Mode creates duplicate/conflicting artifacts alongside TFW artifacts

**On failure:** Revert to full-copy pattern for failed items, document findings as Architecture Decision.

## 7. Principles

1. **Single Source of Truth** — `.tfw/workflows/` is canonical; adapters reference, never copy
2. **Progressive Disclosure** — load context when needed, not everything always-on
3. **Empirical over theoretical** — test each change in live Antigravity session before committing
4. **Graceful degradation** — if a feature doesn't work (Skills, turbo), fall back to known-working pattern

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Thin adapters fail — agent doesn't read referenced file | Medium | High | Test with one workflow first (tfw-plan). If fails → full copy with header-only diff |
| Skills don't match — never auto-activate | Medium | Medium | Use explicit `@mention` fallback + broad description |
| Planning Mode can't be controlled via rules | Low | Medium | Document as known limitation; coexist pattern |
| turbo annotations cause unsafe auto-runs | Low | High | Only annotate read-only steps (view_file, list_dir) |

## 10. RESEARCH Case

### Blind Spots
- Whether Antigravity actually reads files referenced in thin workflow adapters (or ignores indirection)
- Whether Skills auto-activation is reliable enough for heavy-context files like conventions.md
- How Planning Mode artifacts interact with TFW artifacts when both are active
- Whether `Call /other-workflow` actually works for workflow composition

### Hypotheses

| # | Hypothesis | Status |
|---|----------|--------|
| H1 | Thin adapter workflows (15 lines + "Read .tfw/workflows/plan.md") will cause the agent to read and follow the canonical workflow | open |
| H2 | Skills with broad descriptions (e.g., "Use when working on a TFW task") will auto-activate reliably | open |
| H3 | TFW rules suppress Antigravity Planning Mode (implementation_plan/task/walkthrough creation) | **confirmed** — empirical: 0/3 TFW sessions created planning artifacts |
| H4 | `// turbo` annotations on context-loading steps will correctly auto-run read-only commands | open |
| H5 | `Call /other-workflow` syntax works for composing workflows (e.g., tfw-task calls tfw-plan) | open |

### Risks of Not Researching
- We implement thin adapters and they don't work → agents produce empty/confused output
- We add Skills and they never activate → added complexity with zero benefit
- We don't understand Planning Mode interaction → users get confused by hidden artifacts

### Proposed RESEARCH Focus
1. **Gather**: Test thin adapter pattern with 1 workflow (tfw-plan). Does the agent read the referenced file?
2. **Extract**: Create 1 test skill, observe auto-activation behavior
3. **Challenge**: Can Planning Mode be explicitly controlled via rules? What happens when both TFW and Planning Mode are active?

### Why Not Just...?
- Why not keep full copies? — Proven drift problem. `tfw-update` must copy 12 files. Already broken (research.md path).
- Why not skip Skills entirely? — Progressive disclosure = proven pattern (D25). conventions.md is 327 lines loaded on every session — wasteful.
- Why not disable Planning Mode? — It might be useful for non-TFW tasks. Controlling > disabling.

## 11. Strategic Session Insights

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | User suspects TFW rules suppress Planning Mode: "I often see that it doesn't create [planning artifacts], maybe only creates them without TFW" | process | User, direct observation |
| S2 | User preference: control > disable. "I'd rather turn it off if possible, but you're right, we need to take control" | philosophy | User, planning session |
| S3 | User values inversion thinking as analysis tool | convention | User, explicit request |
| S4 | Task is primarily research-focused: "the task was to investigate, just a question of whether we use everything" | stakeholder | User, scope clarification |

---

*HL — TFW-30: Antigravity Adapter Audit | 2026-04-09*
