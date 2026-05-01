# HL — TFW-43: Research Stage Protocol

> **Date**: 2026-05-01
> **Author**: Coordinator (Antigravity)
> **Status**: 🟡 TS_DRAFT — Research complete, TS in progress

---

## 1. Vision (Working Backwards)

Research stages now follow the same disciplined protocol as review stages. Each stage is a ritual: copy template → read mindset → adopt cognitive mode → execute → fill → checkpoint → STOP. The researcher can no longer treat stage files as passive output containers — the mindset block forces a cognitive shift before any work begins. File appearance in the iteration folder = stage started; checkpoint completion = stage done. The user sees files appear one by one, tracking real progress.

**Impact:** Research quality improves through forced cognitive transitions. The same pattern that made review stages effective (D41, TFW-38) — per-stage identity anchoring — is applied to research. Copy-on-enter restores D31 (file existence = stage completion) broken by TFW-42's batch-copy approach.

> "Раньше файлы появлялись по одному и я видел как идёт работа. Сейчас все 4 копируются сразу — непонятно что происходит." — User, helpdesk HD-28 observation

## 2. Current State

Research templates (`1_briefing.md`..`4_challenge.md`) have guiding questions in `<h1>` titles but **no Mindset block**. Review templates (map.md, verify.md, judge.md) have explicit `> **Mindset:** {role}. {instruction}. > **Test:** {self-check}` blocks that anchor the cognitive mode — this works.

`base.md` Step 3 copies all 4 templates at once before any stage begins. This creates 4 empty files immediately, breaking:
- **D31** (file existence = stage completion) — Resume Protocol sees all files as "done"
- **Observable progress** — user cannot tell which stage is in progress
- **Cognitive discipline** — agent sees 4 files as a batch job, not 4 distinct modes

## 3. Deliverables

### 3.1 Value Flow

```
BEFORE (current):
  Step 3: mkdir + copy 4 files ──→ [1][2][3][4] all exist
  Step 5: fill 1, fill 2, fill 3, fill 4 (no cognitive shift)
  User sees: 4 files appear instantly, content fills silently

AFTER:
  Step 3: mkdir only
  Step 4: copy 1_briefing → read mindset → fill → STOP
  Step 5: FOR EACH stage:
    copy template → read mindset → adopt mode → OODA → fill → checkpoint → STOP
  User sees: files appear one by one as stages complete
```

### 3.2 Deliverable List

| # | Deliverable | File |
|---|-------------|------|
| D1 | Mindset blocks (Strategist/Explorer/Analyst/Critic) + Test questions in 4 research templates | `templates/research/1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md` |
| D2 | Briefing h1 guiding question: "What should we investigate?" | `templates/research/1_briefing.md` |
| D3 | Copy-on-enter + per-stage STOP in workflow | `workflows/research/base.md` |
| D4 | Adapter sync | `.agent/workflows/tfw-research.md`, `.claude/commands/tfw-research.md` |
| D4 | Version bump + CHANGELOG | `.tfw/VERSION`, `.tfw/CHANGELOG.md`, `.tfw/project_config.yaml` |

## 4. Phases

Single phase. Scope: 4 templates + 1 workflow + 2 adapters + version files = 8 files, ~30 LOC changes.

### Phase Dependencies

None — single phase.

## 5. Definition of Done

- [ ] Each research template has `> **Mindset:**` + `> **Test:**` blockquote (same format as review templates)
- [ ] `base.md` Step 3 creates only the folder — no template copying
- [ ] `base.md` Step 4 copies `1_briefing.md` before writing (copy-on-enter)
- [ ] `base.md` Step 5 explicitly copies each stage template before executing it
- [ ] `base.md` Step 5 has `🛑 STOP` after each stage checkpoint
- [ ] Step 0 Resume Protocol still works: file existence = stage started/complete (not "all files pre-copied")
- [ ] Adapters synced
- [ ] Version bumped to 0.8.7

## 6. Scope Budget

| Limit | Budget | Planned |
|-------|--------|---------|
| Files | ≤7 | 8 (4 templates + 1 workflow + 2 adapters + version = needs budget override) |
| New files | 0 | 0 |
| LOC | ≤600 | ~40 |

Budget override: 8 files vs 7 limit. 4 template files are structurally identical changes (add 2-line blockquote). Treating as justified — splitting would be artificial.

## 7. Principles

### 7.1 Design Principles

| # | Principle | Rationale |
|---|-----------|-----------|
| P1 | Copy-on-enter, not copy-all | D31: file existence = stage completion. Batch copy violates this semantic |
| P2 | Mindset-first execution | Review templates proved this: Mindset block → identity anchoring → better cognitive mode adherence. Same pattern, applied to research |
| P3 | STOP between stages | Observable progress for human. Opportunity to steer before next stage. Matches review flow (stage files → synthesis) |
| P4 | Template = instruction + container | Template is not just an output form. It carries the cognitive frame that shapes how the agent fills it |

### 7.2 Knowledge Citations

| # | Source | Item | Relevance |
|---|--------|------|-----------|
| KC1 | knowledge/philosophy.md | F4: Structural enforcement beats format enforcement | Copy-on-enter = structural. Checkpoint markers = format. We choose structural |
| KC2 | knowledge/philosophy.md | F18: Different templates serve different cognitive modes — design principle | Each stage template = different cognitive mode. Mindset block makes this explicit |
| KC3 | knowledge/philosophy.md | F20: TFW has investigative vs procedural workflows. Investigative = forced cognitive transitions via stages | Research is investigative. Forced transitions via mindset blocks = core design |
| KC4 | knowledge/philosophy.md | F24: Instructions → compliance, heuristics → competence. Cross-stage structural dependencies enforce better than mandates | Mindset block = heuristic. Copy-on-enter = structural dependency |
| KC5 | knowledge/process.md | F4: Agents follow numbered steps + gates perfectly but lose focus in prose | Step 5 must be explicit per-stage protocol, not "cover all three" |
| KC6 | KNOWLEDGE.md §1 | D31: Filesystem state machine — file existence = stage completion | Broken by TFW-42 batch copy. This task restores it |
| KC7 | KNOWLEDGE.md §1 | D41: 4-stage review flow — Map→Verify→Judge→Decide with per-stage identity | Source pattern for research stage protocol. Proven effective |
| KC8 | knowledge/stakeholder.md | F2: File naming encodes execution order (UX for methodology artifacts) | File _existence_ encodes completion status — same UX principle extended |

## 8. Out of Scope

- Review templates — already have mindset blocks
- OODA loop mechanics — unchanged
- Dimensional analysis thread — already in Step 5 intro (moves to per-stage copy context)
- Glossary — no new terms
- Conventions — no structural changes

## 9. Risks

| # | Risk | Mitigation |
|---|------|------------|
| R1 | 3 extra STOPs (gather + extract + challenge) = friction for simple tasks | Mode files (focused.md) can override. Base.md defines the disciplined default |
| R2 | Resume Protocol interpretation change — file exists but checkpoint not filled | Acceptable: researcher sees own incomplete work and resumes from checkpoint. Better than 4 empty files |

## 10. RESEARCH Justification

RESEARCH completed (iter1). Key findings: role-nouns confirmed effective, h1/Mindset are complementary (not substitute), Test format refined to existential external. See [RES iter1](research/iter1/RES.md).

| # | Hypothesis | Status | Evidence |
|---|-----------|--------|----------|
| H1 | Batch copy breaks D31 | ✅ Confirmed | User observation: "все 4 копируются сразу" |
| H2 | Role-noun anchoring produces different behavior than prose | ✅ Confirmed | Functional nouns (Strategist/Explorer/Analyst/Critic) non-overlapping on 2 axes: convergent↔divergent, build↔break. D28/F3 evidence |
| H3 | Review stage pattern transfers to research | ✅ Confirmed | 3-component structure (Mindset + Test + Checkpoint) maps cleanly |
| H4 | h1 guiding questions → Mindset block | ❌ Partially refuted | h1 = task orientation, Mindset = cognitive orientation. Complementary, not substitute. Three-layer verification: h1/Mindset/Checkpoint |
| H5 | "Did I...?" Test format | 🔄 Refined | Existential external ("Can I name...", "Would...hold...") with stage-output reference > vague self-check. Matches review templates |

## 11. Strategic Session Insights

| # | Category | Insight | Source |
|---|----------|---------|--------|
| S1 | philosophy | Template dual nature: instruction carrier + output container. Agent treats template as form to fill; the Mindset block forces it to also be an instruction to internalize. «Прям взять шаблон, прочитать майндсет, настроиться, выполнить» | User, TFW-43 planning session |
| S2 | process | Observable progress as stakeholder value. File-by-file appearance = implicit status reporting without any status machinery. Lost when batch-copy introduced | User, TFW-43 planning session (HD-28 production feedback) |
| S3 | philosophy | Pattern portability across TFW workflows: review stage protocol → research stage protocol. When a pattern works in one investigative workflow, it should be tested in all investigative workflows (F20) | Coordinator analysis, TFW-38 → TFW-43 cross-reference |

---

*HL — TFW-43: Research Stage Protocol | 2026-05-01*
