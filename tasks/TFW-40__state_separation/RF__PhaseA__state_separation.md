# RF — TFW-40 / Phase A: State Separation & Templates

> **Date**: 2026-04-15
> **Author**: Executor
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-40](HL-TFW-40__state_separation.md)
> **TS**: [TS Phase A](TS__PhaseA__state_separation.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `.tfw/templates/knowledge_state.yaml` | Clean state template (all fields zeroed: seq=0, stats=0). Used by `init.md` for new projects |
| `.tfw/templates/project_config.yaml` | Annotated config template with `# ← PROJECT` / `# ← FRAMEWORK` inline markers. No `stack` section (minimal, per coordinator) |

### Modified Files
| File | Changes |
|------|---------
| `.tfw/workflows/init.md` | Phase 2 Mini-Setup: steps 1-2 now create config and state from templates. Added anti-pattern for direct upstream copy of knowledge_state |
| `.tfw/workflows/update.md` | Step 3: added ⚫ STATE category (never overwrite) with file list. Added explicit merge rules for PROJECT_CONFIG (project sections preserved, framework sections updated) |
| `.tfw/conventions.md` | Added §10.3 File Classification in `.tfw/` — 3-category table (Framework/State/Config) with lifecycle rules |

## 2. Key Decisions

1. **Live `knowledge_state.yaml` not reset** — per coordinator answer, this repo is both starter and live project. Template is clean (seq=0), live file stays at seq=38. Init uses template, not live file.
2. **No `stack` section in config template** — minimal template. Projects needing `stack` add it during init interview. Avoids placeholder clutter.
3. **Template drift anti-pattern placed in `init.md`** — not in `config.md` (which is for value changes, not structure changes). init.md is where template structure matters.

## 3. Acceptance Criteria

- [x] `.tfw/templates/knowledge_state.yaml` exists with all zeros
- [x] `.tfw/templates/project_config.yaml` exists with placeholder project values and PROJECT/FRAMEWORK annotations
- [x] `init.md` Phase 2 references templates for state and config creation
- [x] `init.md` has anti-pattern about direct upstream copy
- [x] `update.md` Step 3 has ⚫ STATE category with exclusion list
- [x] `update.md` Step 3 has explicit merge rules for PROJECT_CONFIG (project vs framework sections)
- [x] `conventions.md` §10.3 documents the 3-category classification
- [x] A new project initialized via init.md would get knowledge_state with seq=0

## 4. Verification

- Template `knowledge_state.yaml`: `last_consolidation_seq: 0` ✅
- Live `knowledge_state.yaml`: `last_consolidation_seq: 38` (preserved) ✅
- `init.md` line 75: references `templates/project_config.yaml` ✅
- `init.md` line 77: references `templates/knowledge_state.yaml` ✅
- `init.md` line 185: anti-pattern about upstream copy ✅
- `update.md` line 58: ⚫ STATE category present ✅
- `update.md` lines 79-82: project/framework section merge rules ✅
- `conventions.md` line 314: §10.3 File Classification present ✅

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/workflows/init.md` | 137 | duplication | Step 6 "Update PROJECT_CONFIG.yaml — finalize all values" partially overlaps with Phase 2 step 1 (create from template + fill). After Phase A changes, Phase 4 step 6 could be more specific: "update framework-section values if needed" |
| 2 | `.tfw/conventions.md` | 309 | naming | §10.2 references `TOPIC_FILE.md` — will be renamed in Phase B to `topic_file.md` |

## 6. Fact Candidates

> fact-candidates: processed 2026-04-15

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | philosophy | User treats template minimalism as a design principle: "Не захламляй шаблон" — templates should contain only what's structurally necessary, projects add domain-specific sections through workflow | User, ONB Q1 answer | High |
| 2 | constraint | The TFW starter repo is simultaneously the upstream template AND a live project with real state (seq=38, 66 facts). This dual identity constrains how state files can be managed — live state must coexist with clean templates | User, ONB Q2 answer + HL §10 "Why Not Just" | High |

## 7. Strategic Insights (Execution)

> strategic-insights: processed 2026-04-15

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | User's answer on stack section reveals a design principle: init interview is the customization mechanism, not template placeholders. Implication: all future template additions should follow the same pattern — templates define structure, interviews inject project-specific sections. This prevents template bloat across TFW versions | philosophy | User, ONB Q1 answer |

## 8. Diagrams

```
.tfw/ File Lifecycle:

INIT (new project):
  upstream/.tfw/templates/project_config.yaml ──COPY──→ .tfw/PROJECT_CONFIG.yaml ──FILL──→ project values
  upstream/.tfw/templates/knowledge_state.yaml ──COPY──→ .tfw/knowledge_state.yaml (clean, seq=0)
  upstream/.tfw/workflows/ ────────────────────COPY──→ .tfw/workflows/
  upstream/.tfw/templates/ ────────────────────COPY──→ .tfw/templates/

UPDATE (existing project):
  upstream/.tfw/workflows/ ──────── 🟢/🟡 ──→ .tfw/workflows/ (overwrite or merge)
  upstream/.tfw/templates/ ──────── 🟢 ────→ .tfw/templates/ (overwrite)
  upstream/.tfw/knowledge_state.yaml ── ⚫ ──→ SKIP (never touch project state)
  upstream PROJECT_CONFIG.yaml ────── 🟡 ────→ MERGE (framework sections only)
```

---

*RF — TFW-40 / Phase A: State Separation & Templates | 2026-04-15*
