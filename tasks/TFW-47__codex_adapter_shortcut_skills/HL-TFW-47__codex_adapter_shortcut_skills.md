# HL — TFW-47: Evidence Enforcement & Codex Adapter

> **Date**: 2026-07-17
> **Author**: Coordinator (Antigravity)
> **Status**: ✅ HL_APPROVED — Research complete, proceeding to TS
> **Revision**: 3 (updated with iter1+iter2 research findings)

---

## 1. Vision

TFW enforces physical evidence as a non-optional output of every task. Every completed task has an `evidence/` folder with a structured template file capturing real verification results — commands run, outputs observed, environments used. This closes the gap where evidence was conceptually defined (D52) but never physically materialized (0 of 38 tasks created the folder).

Simultaneously, Codex becomes a first-class TFW adapter with dedicated shortcut skills (`tfw-plan`, `tfw-review`, etc.), matching the adapter parity already achieved for Claude Code and Antigravity.

**Impact:** Reviewers can audit physical artifacts instead of trusting inline RF claims. Codex users get the same obvious workflow affordances as users of other tools.

> "Я хочу открыть папку задачи и увидеть `evidence/` с реальными результатами проверки — не читать RF и верить на слово."

## 2. Current State (As-Is)

### Evidence

D52 (TFW-46) introduced the evidence concept — three-role pipeline, status vocabulary, §5 in RF. But D16 made `evidence/` folder explicitly **optional** ("only when binary artifacts exist"). Result:

| Metric | Value |
|--------|-------|
| Tasks with `evidence/` folder | **0 / 38** |
| Templates requiring folder creation | **0** |
| Workflows with "create evidence/" step | **0** |
| D16 status | Optional — text evidence goes inline in RF |

Evidence exists as inline RF text: "line count = 84 ✅", "SHA-256 confirms ✅". No physical artifacts, no reproducible proof.

### Codex Adapter

| Tool | Current adapter pattern | Status |
|------|-------------------------|--------|
| Claude Code | `CLAUDE.md` + `.claude/commands/` | ✅ First-class |
| Cursor | `.cursor/rules/tfw.mdc` | ✅ First-class |
| Antigravity | `.agent/rules/tfw.md` + `.agent/workflows/` | ✅ First-class |
| Codex | Not defined | ❌ Missing |

Codex reads `AGENTS.md` natively but has no dedicated shortcut skills. User reported: `/tfw-plan` not visible as a separate Codex skill.

### Existing constraints

| Constraint | Source | Implication |
|------------|--------|-------------|
| `.tfw/workflows/*.md` = source of truth | convention F5 | Codex skills must be thin routers |
| Tool adapters are framework-owned | conventions §10.3 | Codex adapter → `.tfw/adapters/codex/` |
| Adapter sync in config/update workflows | workflows config.md, update.md | Must add Codex to both |
| Evidence pipeline = 3 roles | conventions §3 | Changes affect TS, RF, handoff, review templates |
| 32 KiB Codex instruction cap | Codex docs | Cannot load conventions.md (27 KB) into instruction chain |

## 3. Target State (To-Be)

### 3.1 Result Visualization

Six months after this ships:

```
Любая завершённая задача:
  tasks/TFW-50__feature_x/
    HL-TFW-50__feature_x.md
    TS__TFW-50__feature_x.md
    ONB__TFW-50__feature_x.md
    RF__TFW-50__feature_x.md
    evidence/                          ← ВСЕГДА создаётся
      EV__TFW-50__feature_x.md         ← Environment header + per-AC table + Verdict
      screenshot_deploy.png             ← бинарные артефакты (если есть)
      api_response.json                 ← дополнительные файлы (если есть)
    review/
      ...

Codex skill list ($tfw-* — native invocation):
  $tfw-plan       → reads .tfw/workflows/plan.md
  $tfw-research   → reads .tfw/workflows/research/base.md
  $tfw-handoff    → reads .tfw/workflows/handoff.md
  $tfw-review     → reads .tfw/workflows/review.md
  $tfw-resume     → reads .tfw/workflows/resume.md
  ...

Installed at: .agents/skills/tfw-*/SKILL.md (2026 cross-platform standard)
Source:       .tfw/adapters/codex/skills/tfw-*/SKILL.md
```

### 3.2 Value Flow

```
USER PAIN                           USER PAIN
"evidence/ не создаётся"            "Codex не видит /tfw-plan"
        |                                   |
        v                                   v
PHASE A: Evidence Enforcement       PHASE B-C: Codex Adapter
  conventions.md §3, §4              .tfw/adapters/codex/
  templates: TS, RF, evidence/        skills/tfw-*/SKILL.md
  handoff.md Step 11                  AGENTS.md.template
        |                                   |
        v                                   v
PHASE D: Framework Integration (оба потока сходятся)
  README, glossary, init, update, config workflows
        |
        v
PHASE E: Release
  VERSION bump, CHANGELOG
```

## 4. Phases

### Phase Dependencies

```mermaid
graph LR
  A["Phase A: Evidence enforcement ✅"] --> B["Phase B: Codex adapter + integration"]
  B --> C["Phase C: Release packaging"]
```

| Phase | Depends on | Shared files | Can run in parallel with |
|-------|------------|--------------|--------------------------|
| B | A | conventions.md, glossary.md, README | — |
| C | B | VERSION, CHANGELOG | — |

### Phase A: Evidence enforcement 🔴

> **Requires:** Independent
>
> **Context for coordinator:**
> 1. conventions.md §3 (Evidence Sections) — current pipeline definition
> 2. conventions.md §4 (Task Numbering) — folder structure, `evidence/` absent
> 3. conventions.md §14 (Anti-patterns) — 5 evidence anti-patterns
> 4. TFW-46 research/iter2/RES.md D16 — the decision that made `evidence/` optional
> 5. Previous analysis: `analysis_evidence_gap.md` from conversation d2fb1e99
> 6. glossary.md — Evidence Terms section
>
> **Key decisions:**
> - D16 (revoke): `evidence/` was optional → now mandatory
> - D52 (extend): evidence layer gets physical folder requirement
>
> **Deliverables:**
> 1. Create `.tfw/templates/evidence/` with structured evidence template file (name and structure — research deliverable; must align with TFW values: trace-first, honest, structured, reproducible).
> 2. Update conventions.md §4 — add `evidence/` as mandatory subfolder in task structure (single-phase and multi-phase).
> 3. Update conventions.md §3 — remove optional language, add folder creation requirement.
> 4. Update `.tfw/templates/TS.md` — add `## Evidence Artifacts` section listing expected evidence files.
> 5. Update `.tfw/templates/RF.md` §5 — artifact column references `evidence/` path.
> 6. Update `.tfw/workflows/handoff.md` Step 11 — add explicit step: "Create `evidence/` folder, populate with template, fill with real results."
> 7. Update KNOWLEDGE.md — revoke D16 optional status, extend D52.

### Phase B: Codex adapter + framework integration 🔴

> **Requires:** Phase A ✅
>
> **Context for coordinator:** iter2/RES.md (all Codex decisions), AFD project skills as reference, Phase A RF (evidence enforcement now active).
>
> **Key decisions from research:**
> - iter2 D1: `.agents/skills/` canonical path (2026 standard)
> - iter2 D2: 11 handwritten skills, not generated
> - iter2 D3: On-demand loading (32 KiB cap = non-issue)
> - iter2 D4: `$tfw-*` native invocation; `/tfw-*` soft alias
> - iter2 D5: Two-location: `.tfw/adapters/codex/` → `.agents/skills/`
> - iter2 D6: YAML frontmatter + Contract heading convention
> - iter2 D7: tfw-init copies, tfw-update syncs
>
> **Budget override:** 13 new files (11 skills + README + AGENTS template) exceeds max_new=8. Justified: 11 skill files are structurally identical thin routers (~1.2 KB each), single conceptual unit. Splitting artificially inflates phase count.
>
> **Executor: Codex (CL mode)** — the adapter's first user is its own creator. Evidence = Codex running TFW workflows after installing the adapter.
>
> **Deliverables:**
> 1. Create `.tfw/adapters/codex/README.md` — install + fallback instructions.
> 2. Create `.tfw/adapters/codex/AGENTS.md.template` — root routing.
> 3. Create 11 handwritten skill folders: `.tfw/adapters/codex/skills/tfw-*/SKILL.md`.
> 4. Install skills to `.agents/skills/tfw-*/SKILL.md`.
> 5. Add Codex to README Tool Adapters and Quick Start.
> 6. Update `.tfw/adapters/README.md`.
> 7. Update `.tfw/workflows/init.md` — Codex install option.
> 8. Update `.tfw/workflows/update.md` — Codex adapter sync.
> 9. Update glossary.md — Adapter Command includes Codex.
> 10. Evidence: Codex runs a TFW workflow in CL mode using installed adapter.

### Phase C: Release packaging 🟢

> **Requires:** Phase B ✅
>
> **Deliverables:**
> 1. CHANGELOG entry: evidence enforcement + Codex adapter.
> 2. Bump `.tfw/VERSION`.
> 3. Confirm no stale references omit Codex or evidence/.

## 5. Definition of Done (DoD)

**Evidence enforcement:**
- ✅ 1. `evidence/` is listed as mandatory subfolder in conventions.md §4 (single-phase and multi-phase).
- ✅ 2. Evidence template file exists in `.tfw/templates/evidence/` with structured format aligned to TFW values.
- ✅ 3. TS template includes `## Evidence Artifacts` section prescribing expected files.
- ✅ 4. handoff.md Step 11 includes explicit evidence folder creation + population step.
- ✅ 5. D16 optional status is revoked in KNOWLEDGE.md; D52 extended.
- ✅ 6. RF template §5 Artifact column references `evidence/` paths.

**Codex adapter:**
- ✅ 7. Codex appears in public adapter table with clear entry point.
- ✅ 8. `.tfw/adapters/codex/` exists with README, AGENTS template, shortcut skill folders.
- ✅ 9. Dedicated shortcut skills for all canonical workflows (plan, research, handoff, review, resume, docs, knowledge, release, update, config, init).
- ✅ 10. Each skill reads local workflow file, no logic duplication.
- ✅ 11. `tfw-init` installs Codex shortcut skills.
- ✅ 12. `tfw-update` syncs Codex adapter files.
- ✅ 13. Invocation syntax documented truthfully.

## 6. Definition of Failure (DoF)

- ❌ 1. `evidence/` remains optional or "guidance only."
- ❌ 2. Evidence template is a generic dump without structure aligned to TFW values.
- ❌ 3. handoff.md still says "record in RF §5" without mentioning evidence folder.
- ❌ 4. Codex shortcut skills copy full workflow bodies (second source of truth).
- ❌ 5. Documentation claims `/tfw-plan` works in Codex without validation.
- ❌ 6. `tfw-update` overwrites or drops Codex adapter files.
- ❌ 7. 32 KiB cap not addressed — Codex fails to load TFW instructions.

**On failure:** Evidence: revert to D16 optional status + document why enforcement failed. Codex: revert to "generic `tfw` fallback only" until behavior validated.

## 7. Principles

1. **Evidence is mandatory, not optional** — every task produces `evidence/` with at least one structured file. No exceptions, no "inline is enough."
2. **Template reflects values** — evidence template is designed per TFW principles: trace-first, honest, structured, reproducible. Not a generic log dump.
3. **Thin adapters over duplicated workflows** — Codex skills route to `.tfw/workflows/`, not copies.
4. **Visible affordance over hidden inference** — users see `tfw-plan` as a real Codex skill.
5. **Truthful invocation contract** — document what actually works, not what we wish worked.
6. **Portable installation** — support multiple Codex skill directories without hardcoding.
7. **Fallback-first** — if shortcut skills missing, generic routing still works.
8. **Adapter parity** — Codex setup as easy as Claude Code and Antigravity.

### 7.1 Quality Contract

For all phases:
- Evidence folder naming and structure decisions made in Phase A are binding for all subsequent phases.
- Codex skill structure decisions made in Phase B/C are binding for Phase D documentation.
- No phase may introduce tool-specific logic into `.tfw/workflows/` or `.tfw/templates/` — these remain tool-agnostic.

### 7.2 Knowledge Citations

| # | Source | Item | How it applies |
|---|--------|------|----------------|
| KC1 | KNOWLEDGE.md D52 | Evidence Layer — 3-role pipeline, status vocabulary | Foundation being extended with mandatory folder |
| KC2 | TFW-46 research D16 | `evidence/` optional — only for binary artifacts | Decision being **revoked** — folder now mandatory |
| KC3 | knowledge/convention.md F5 | `.tfw/workflows/*.md` = source of truth for adapters | Codex skills must be thin routers |
| KC4 | KNOWLEDGE.md D15 | Claude Code slash commands = thin adapters | Codex shortcut skills follow same pattern |
| KC5 | KNOWLEDGE.md D50 | Research cycle restructure — adapter sync as phase | Codex must include docs/workflow sync |
| KC6 | knowledge/process.md F3 | Naming creates behavior in AI agents | Dedicated `tfw-plan` > generic explanation |
| KC7 | knowledge/domain.md F4 | TFW agents are IDE-level systems | Codex = tool adapter, not new role model |
| KC8 | conventions.md §12 | Evidence requires real-environment observation, VERIFIED needs artifact ref | Enforcement closes the gap between rule and practice |
| KC9 | conventions.md §14 | Anti-pattern: VERIFIED without artifact reference | Mandatory folder makes this structurally impossible |

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| Evidence gap analysis (conversation d2fb1e99) | ✅ Complete |
| Codex skill discovery behavior | needs-research |
| Codex invocation syntax | needs-research |
| Codex 32 KiB instruction cap handling | needs-research |
| Evidence template name and structure | needs-research |
| Existing adapter patterns | ✅ Available in `.tfw/adapters/` |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Evidence template too rigid for diverse tasks | Medium | Medium | No tiers — proportionality via row count (trivial=2, complex=11). Research validated on 3 task types |
| Evidence enforcement creates friction for trivial tasks | Medium | Low | Minimum bar = environment header + 1 evidence row. Tested on HD-13 (trivial) |
| 32 KiB Codex cap blocks TFW instruction loading | **Low** | **Low** | **DOWNGRADED** — on-demand loading via skill contract bypasses cap entirely (iter2 D3/D8) |
| Codex UI doesn't show skills as slash commands | Medium | Medium | `$tfw-*` is native; `/tfw-*` is soft alias via description matching (iter2 D4) |
| Shortcut skills drift from workflow list | Medium | Medium | Validate skill list against `tfw.workflows` in project_config.yaml |
| Evidence template naming conflicts with existing artifacts | Low | Low | Research phase proposes name; coordinator approves |

## 10. RESEARCH Case

### Blind Spots

**Evidence:**
- What should the evidence template file be named? (Must align with TFW naming conventions: HL, TS, RF, RES, REVIEW — all uppercase abbreviations)
- What sections should the template contain? (Structured per TFW values, not just a log)
- How does the template handle proportionality? (Trivial task vs complex deployment)

**Codex:**
- Exact skill discovery directories and reload behavior.
- Whether `/tfw-plan` triggers a skill or only natural language.
- Whether `SKILL.md` YAML frontmatter fields affect visibility.
- 32 KiB cap workarounds for heavy TFW docs.
- Generated vs handwritten skill folders.

### Hypotheses

| # | Hypothesis | Status | Evidence |
|---|------------|--------|----------|
| H1 | A single structured evidence template file per task (not per-AC) is sufficient for traceability | ✅ confirmed | Stress-tested on 3 task types (iter1) |
| H2 | The evidence template should include environment metadata (OS, tool versions, timestamps) for reproducibility | ✅ confirmed | ISO 29119 + AFD-36/A empirical (iter1) |
| H3 | Dedicated Codex skill folders are required for separate visible entries in Codex UI | ✅ confirmed | AGENTS.md routing ≠ skill menu entry (iter2) |
| H4 | `AGENTS.md` routing is sufficient for behavior but insufficient for UI affordance | ✅ confirmed | AFD has both — AGENTS.md for rules, skills for affordance (iter2) |
| H5 | Generated shortcut-skill set is safer than maintaining 11 handwritten folders | ❌ refuted | Template insufficient for 6/11 workflow contracts (iter2) |
| H6 | `$tfw-plan` is the reliable invocation; `/tfw-plan` may only be user convention | ✅ confirmed | `$` = native trigger; `/` = description match alias (iter2) |
| H7 | Codex can load conventions.md on-demand via skill references instead of instruction chain | ✅ confirmed | Skill contract reads at runtime, bypasses 32 KiB cap (iter2) |

### Risks of Not Researching

**Evidence:** Template design without research may produce a format that doesn't fit diverse task types — too rigid or too loose. The template name may conflict with existing TFW naming or feel foreign.

**Codex:** Framework could ship documentation promising Codex experiences the product doesn't provide. 32 KiB cap could silently truncate TFW instructions.

### Proposed RESEARCH Focus

1. **Gather:** (a) Survey TFW artifact naming patterns and propose evidence template name + structure. (b) Inspect Codex skill discovery, reload, invocation syntax.
2. **Extract:** (a) Compare evidence template options: single file vs per-AC, minimal vs comprehensive. (b) Compare Codex adapter options: AGENTS.md only, generic skill, dedicated skills, hybrid.
3. **Challenge:** (a) Test evidence template against 3 real past tasks — does it capture what was actually verified? (b) Can a new Codex user see and use `tfw-plan` after setup?

### Why Not Just...?

- Why not keep `evidence/` optional? — 0/38 tasks created it. Optional = never happens.
- Why not put evidence inline in RF? — Already tried. Result: unauditable text claims.
- Why not name it `verification.md`? — Conflicts with RF §4 Verification (synthetic). Evidence ≠ verification.
- Why not only add Codex to AGENTS.md? — Routes behavior but doesn't create visible shortcut skills.
- Why not copy workflows into Codex skills? — Duplicates source of truth, creates drift.

## 11. Strategic Insights (Planning)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | User wants physical evidence artifacts in the filesystem, not inline RF text. The folder must exist, not be "guidance." This is a deliberate philosophical shift from D16 "optional." | philosophy | User, evidence analysis session (d2fb1e99) |
| S2 | Evidence template file should have a name and structure designed per TFW values — not a generic log dump. User explicitly said "я бы назвал файл иначе и шаблон внутри подготовил по нашим общим принципам целям и ценностям." | stakeholder | User, current session |
| S3 | User wants Codex integration "immediately" at framework level — in `.tfw/adapters/codex/` and init/update, not per-project patches. | stakeholder | User, TFW-47 original session |
| S4 | User noticed `/tfw-plan` "does not invoke" separately after AGENTS.md routing. Docs must distinguish routing text from real skill installation. | process | User, TFW-47 original session |
| S5 | Adapter parity is the product bar: Codex users should get the same obvious workflow affordances as Claude Code and Antigravity users. | philosophy | User request + README adapter positioning |

> fact-candidates: processed 2026-08-05

---

*HL — TFW-47: Evidence Enforcement & Codex Adapter | 2026-07-17*
