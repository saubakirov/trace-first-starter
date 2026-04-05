# HL — TFW-26: Documentation as Output

> **Date**: 2026-04-05
> **Author**: Coordinator
> **Status**: ✅ DONE — FC ✅, Phase A ✅, Phase B ✅. Closed as MVP. Remaining work spawned to TFW-27, TFW-28

---

## 1. Vision

TFW produces structured knowledge **by design**. The workflow — HL, RES, RF, REVIEW, tfw-knowledge, tfw-docs — already generates structured .md files with decisions, facts, links, task history. This corpus of artifacts is inherently queryable: any AI agent pointed at the project folder can answer questions about architecture, processes, and decisions — without vectorization, elasticsearch, or special indexing. The artifacts ARE the knowledge base.

Documentation, web UI, and AI-queryable endpoints are **side effects** of this structured knowledge, not the primary goal. Because TFW enforces structure and traceability in artifacts, compiling them into any output format — web docs, MCP endpoints, portable bundles — is a mechanical step, done by deterministic utilities (not agents).

The system operates in two layers:
1. **Layer 1 (Agent, intelligent):** Maintains artifact quality — structure, links, cross-references, naming conventions. Produces raw documentation through existing workflows (tfw-docs, tfw-knowledge). Ensures artifacts conform to the **compilable contract**.
2. **Layer 2 (Utilities, deterministic, plural):** Multiple independent consumers read the same artifacts via the compilable contract:
   - **2a:** Static docs site (MkDocs → GitHub/GitLab Pages)
   - **2b:** MCP-servable knowledge (AI agents query artifacts — future)
   - **2c:** Portable knowledge bundle (zip/archive — future)

**Impact:** Projects that follow TFW discipline get three things for free: (1) a knowledge base that any AI agent can query by reading files, (2) a publishable documentation site compiled from those files, (3) traceable decision history with links to original artifacts. The starter repo (tfw.saubakirov.kz) becomes the first consumer.

> "We never wrote docs. The TFW workflow produced structured knowledge — decisions, facts, architecture. The docs site was just a side effect. And any new AI agent we onboard can answer questions about the project by reading the same files."

## 2. Current State (As-Is)

### Two-layer architecture (already partially exists)

**Layer 1 — Agent quality maintenance (EXISTS):**
```
tfw-knowledge ──→ knowledge/ topic files (verified facts)
tfw-docs      ──→ KNOWLEDGE.md (architecture, decisions, legacy)
                   TECH_DEBT.md (debt registry)
```

**Layer 2 — Compilation to publishable docs (MISSING):**
```
KNOWLEDGE.md ──→ ???
knowledge/   ──→ ???
CHANGELOG    ──→ ???
                  ↓
           No "compile to docs" step.
```

### What already exists (structured, compilable)

| Source | Content | Format | Compilable? | Transformation |
|--------|---------|--------|-------------|----------------|
| `README.md` | Project description, task board | Markdown tables | ✅ | **Moderate** — extract non-Task-Board content |
| `KNOWLEDGE.md` | Architecture, decisions, legacy, facts index | Structured sections | ✅ | **Split** — §0-§3 → separate pages |
| `knowledge/*.md` | Verified facts (19 facts, 4 topics) | Uniform table format | ✅ | **Minimal** — frontmatter + copy |
| `TECH_DEBT.md` | Tech debt registry | Structured tables | ✅ | **Minimal** — frontmatter + copy |
| `.tfw/CHANGELOG.md` | Version history | Keep a Changelog | ✅ | **Minimal** — frontmatter + copy |
| `.tfw/README.md` | Philosophy, values, lifecycle | Long-form narrative | ✅ | **Moderate** — single page or split by sections |
| `.tfw/conventions.md` | Rules, standards | Structured sections | ✅ | **Minimal** — frontmatter + copy |
| `.tfw/glossary.md` | Terminology | Definition list | ✅ | **Minimal** — frontmatter + copy |
| `.tfw/init.md` | Getting started pointer | Short reference | ✅ | **Minimal** — getting-started page |
| `RELEASE.md` | Release strategy | Structured sections | ✅ | **Minimal** — frontmatter + copy |

> **RESEARCH finding (E1):** 7/10 artifacts need only frontmatter + copy. Only 3 need real transformation (KNOWLEDGE.md split, README.md extraction, .tfw/README.md optional split).

### Specific problems

| Problem | Evidence |
|---------|----------|
| Knowledge exists but isn't publishable | 33 architecture decisions in KNOWLEDGE.md — invisible to anyone outside the repo |
| No compilation step in the pipeline | tfw-docs stops at KNOWLEDGE.md update |
| Each project reinvents docs | No standard way to get docs from TFW artifacts |
| Starter repo serves raw README | tfw.saubakirov.kz — Task Board dominates, no navigation, broken code-block rendering |
| Traceability is inconsistent | knowledge/ facts have Source column → tasks/RF. But KNOWLEDGE.md §0 Principles have only "Source" text — no clickable link. Some links by-design, some accidental |
| No "compilable contract" | Agents produce structured artifacts, but no explicit specification of what structure the compiler expects. Structure emerged organically, not by specification |
| Coordinator has no fact capture mechanism | HL has no Fact Candidates section. Strategic insights from planning sessions survive only if tfw-knowledge happens to be called in the same chat session |
| Dead links in compiled output | knowledge/ facts reference `tasks/RF-...` — these links work on GitHub but become dead in docs site output |

## 3. Target State (To-Be)

### Two-layer architecture (complete)

**Layer 1 — Agent quality maintenance (enhanced):**
```
tfw-knowledge ──→ knowledge/ topic files (verified facts)
tfw-docs      ──→ KNOWLEDGE.md (architecture, decisions, legacy)
                   TECH_DEBT.md (debt registry)
                   ↓
          Agents ensure artifacts conform to
          the COMPILABLE CONTRACT:
          • Headings match expected patterns
          • Links are not broken
          • Names follow conventions
          • Table formats are consistent
          • Cross-references are valid
```

**Layer 2 — Deterministic compilation (NEW):**
```
docs/scripts/gen_docs.py (runs at build time via mkdocs-gen-files):
  reads artifacts from project root, .tfw/, knowledge/
  adds frontmatter, splits KNOWLEDGE.md by sections
  generates virtual pages in MkDocs build

  Output (site/ — CI/CD artifact, NOT in git):
    ├── index.md                    ← from README.md or curated docs/index.md
    ├── getting-started.md          ← from .tfw/init.md
    ├── concepts/philosophy.md      ← from .tfw/README.md
    ├── architecture/principles.md  ← from KNOWLEDGE.md §0
    ├── architecture/decisions.md   ← from KNOWLEDGE.md §1
    ├── architecture/legacy.md      ← from KNOWLEDGE.md §3
    ├── knowledge/*.md              ← from knowledge/*.md (copy + frontmatter)
    ├── reference/conventions.md    ← from .tfw/conventions.md
    ├── reference/glossary.md       ← from .tfw/glossary.md
    ├── reference/changelog.md      ← from .tfw/CHANGELOG.md
    └── reference/tech-debt.md      ← from TECH_DEBT.md
```

**Key architectural decisions (from RESEARCH):**
- **No compiled output in git** (D2) — `site/` is a CI/CD artifact, deployed via GitHub Actions
- **Compilable contract is the primary deliverable** (D3) — more important than tool choice
- **Utility warns on contract violations** (D5) — deterministic string checks, not silent failures
- **Current artifact structure is already sufficient** (D6) — only the formal contract spec is missing

### What changes

| Aspect | As-Is | To-Be |
|--------|-------|-------|
| Documentation output | None | `site/` folder, deployed via CI/CD (NOT in git) |
| `docs/` folder | Doesn't exist | Project-specific docs workspace: configs, scripts, curated pages |
| Compilable contract | Implicit (emerged organically) | Explicit specification in conventions or docs/ |
| Layer 1 (agent) | Maintains KNOWLEDGE.md, knowledge/ | Same + ensures artifacts conform to compilable contract |
| Layer 2 (compiler) | Doesn't exist | MkDocs + gen-files script (~100 LOC) |
| Trigger | N/A | CI/CD (GitHub Actions / GitLab CI), local `mkdocs serve` |
| Hosting target | N/A | GitHub Pages / GitLab Pages |
| Platform support | N/A | Same mkdocs.yml, different CI wrapper per platform |

### 3.1 Result Visualization

**Source → Output mapping (revised from RESEARCH E3):**

```
┌─────────────────────────────────┐       ┌──────────────────────────────┐
│  TFW PROJECT (source)           │       │  MkDocs site (output)        │
│                                 │       │  built by mkdocs-gen-files   │
│                                 │       │  deployed via CI/CD          │
│  README.md ─────────────────────┼──────→│  index.md                    │
│  .tfw/README.md ────────────────┼──────→│  concepts/philosophy.md      │
│  .tfw/init.md ──────────────────┼──────→│  getting-started.md          │
│  KNOWLEDGE.md §0 ───────────────┼──────→│  architecture/principles.md  │
│  KNOWLEDGE.md §1 ───────────────┼──────→│  architecture/decisions.md   │
│  KNOWLEDGE.md §3 ───────────────┼──────→│  architecture/legacy.md      │
│  knowledge/*.md ────────────────┼──────→│  knowledge/*.md  (copy+fm)   │
│  TECH_DEBT.md ──────────────────┼──────→│  reference/tech-debt.md      │
│  .tfw/conventions.md ───────────┼──────→│  reference/conventions.md    │
│  .tfw/glossary.md ──────────────┼──────→│  reference/glossary.md       │
│  .tfw/CHANGELOG.md ─────────────┼──────→│  reference/changelog.md      │
│                                 │       │                              │
│  docs/index.md (optional) ──────┼──────→│  index.md (curated override) │
│  docs/faq.md (optional) ────────┼──────→│  faq.md                      │
│                                 │       │                              │
│  docs/mkdocs.yml ← project cfg  │       │                              │
│  docs/scripts/gen_docs.py ← ← ←│       │  (gen-files script)          │
└─────────────────────────────────┘       └──────────────────────────────┘
```

**`docs/` folder structure (in git — project-specific workspace):**

```
docs/                              ← project-specific documentation workspace
├── mkdocs.yml                     ← MkDocs config (project name, URL, theme)
├── scripts/
│   └── gen_docs.py                ← compilation script (reads artifacts, writes virtual pages)
├── requirements.txt               ← Python deps (mkdocs, material, gen-files)
├── index.md                       ← (optional) curated landing page override
├── faq.md                         ← (optional) curated FAQ
└── .gitkeep                       ← ensures folder exists even if no curated pages
```

**Separation of concerns:**
- `.tfw/` knows **WHAT** structure to expect (compilable contract)
- `docs/` knows **HOW** to build (scripts, configs, tooling)
- This mirrors: `.tfw/conventions.md` (rules) vs `tasks/` (implementation)

## 4. Phases

### Coordinator Fact Capture (mini-task) ✅ DONE
- Added `philosophy` to conventions.md §10.1 Fact Categories
- Added §11 Strategic Session Insights to HL template
- Added Step 4b (fact capture) to plan.md
- Added fact capture reminder to resume.md
- Added "Strategic Insight" glossary term
- [Artifacts](coordinator_fact_capture/)

### Phase A: Compilable contract + infrastructure ✅ DONE
- Defined compilable contract: §16 in conventions.md (§16.1 Source Manifest, §16.2 Reference Format, §16.3 Frontmatter, §16.4 Output Nav)
- Amended templates: KNOWLEDGE.md, TOPIC_FILE.md, RF.md, REVIEW.md, RES.md — standardized Source columns
- Created docs/ infrastructure: mkdocs.yml, gen_docs.py skeleton, requirements.txt
- Created .github/workflows/docs.yml
- Added glossary terms: Compilable Contract, Reference Format, Source Manifest
- [Artifacts](PhaseA/)

### Phase B: Gen-files script implementation ✅ DONE
- Implemented `docs/scripts/gen_docs.py` (445 LOC — exceeded ~100 LOC estimate, justified by scope expansion below)
- 6 reference resolvers: artifact, phase, HL-dash, TD, D, backtick-path
- Structured tasks index with numeric sorting, status from README task board
- Section index pages for tasks/, knowledge/, workflows/, templates/
- 42 tests (29 unit + 13 integration)
- MkDocs build: exit 0, ~165 pages generated
- [Artifacts](PhaseB/)

**Phase B scope expansions (user-driven during live testing):**
- tasks/ included in docs output (user: "Вариант А неприемлим, однозначно надо все собирать")
- KNOWLEDGE.md served as single page with TOC anchors (no split — user decision)
- Backtick-path resolver added (KNOWLEDGE.md uses abbreviated backtick paths exclusively)
- Structured tasks index (user: "сортированы как попало, как для роботов" → numeric sorting)
- Nav restructured: Architecture → Knowledge (user: "Knowledge и Knowledge index как-то странно")

### Spawned Tasks (out of scope — TFW-26 closed as MVP)

| Task | Scope | Tech Debt | Priority |
|------|-------|-----------|----------|
| **TFW-27** | Wiki polish & landing page: fix broken links (TD-72), dynamic nav (TD-71), nav terminology (TD-69), sidebar (TD-70), `--strict` (TD-74), README/index landing, logo, SEO | TD-69..TD-72, TD-74 | High |
| **TFW-28** | Deploy: GitHub Pages to tfw.saubakirov.kz, GitLab CI example, verify responsive design | — | Medium (depends on TFW-27) |
| **Future** | MCP server for Antigravity self-use, multi-repo aggregation, executor session fact capture (RF TFW-26/B obs. #9), KNOWLEDGE.md backtick migration (TD-66, TD-67) | TD-66, TD-67 | Low |

## 5. Definition of Done (DoD)

- ✅ 1. Compilable contract defined: §16 in conventions.md (13 sources, 9 ref patterns, resolution rules)
- ✅ 2. `docs/scripts/gen_docs.py` produces MkDocs site from TFW artifacts (445 LOC, 42 tests)
- ✅ 3. Compilation is deterministic: same input → same output
- → 4. Site deployment — spawned to TFW-28
- ✅ 5. Source mapping documented: every doc page has `source:` in frontmatter
- ✅ 6. Warning-level validation for contract violations
- → 7. Portability (hardcoded topics fix) — spawned to TFW-27
- → 8. GitHub Pages deployment — spawned to TFW-28

## 6. Definition of Failure (DoF)

- ❌ 1. Docs require manually mirroring content from artifacts — **NOT triggered** (gen_docs.py reads source directly)
- ⚠️ 2. The gen-files script exceeds ~150 LOC — **TRIGGERED** (445 LOC). Justified: scope expanded to include tasks/, 6 resolvers, structured indexes. Core logic remains ~150 LOC; ~295 LOC is resolvers + index generation added by user demand
- ❌ 3. Docs output doesn't work with GitHub Pages — **NOT triggered** (build succeeds, pending deployment)
- ⚠️ 4. Adding new knowledge topic requires manual docs update — **Partially triggered** (topics hardcoded in mkdocs.yml nav, TD-71). Gen_docs.py auto-discovers files, but nav needs manual edit. Phase C fix
- ❌ 5. Contract violations fail silently — **NOT triggered** (warnings on missing sources and unresolved refs)

**Revised assessment:** DoF#2 and DoF#4 are amber. Both have clear Phase C fixes. No fundamental architecture change needed. The fallback (curated static docs) is NOT warranted — the system works, it needs polish.

## 7. Principles

1. **Knowledge by design** — TFW produces structured knowledge as a byproduct of its workflow. Artifacts ARE the knowledge base.
2. **AI-queryability first, web UI second** — the primary consumer is the next AI agent that needs to understand the project. Web UI is a side effect.
3. **Two layers, two concerns** — agents maintain quality and structure (Layer 1, intelligent). Utilities compile to outputs (Layer 2, deterministic, plural). Don't mix.
4. **Don't invent, find and configure** — use existing tools (MkDocs + gen-files). Custom code only where no tool fits.
5. **Deterministic compilation with warnings** — Layer 2 walks strict lists, expects strict format. Warns on contract violations. Never fails silently, never uses AI judgment.
6. **Intentional structure, not accidental** — every link, cross-reference, and naming convention must be by-design with the compilable contract.
7. **Contract is the interface** — the compilable contract serves ALL output targets (web docs, MCP, bundles). Tool choice is swappable, contract is stable.
8. **Progressive enhancement** — README.md only = minimal docs site. More artifacts = richer docs.
9. **Platform portable** — same mkdocs.yml for GitHub and GitLab. Only CI/CD wrapper differs.
10. **`.tfw/` = what, `docs/` = how** — TFW core defines the contract (what structure to expect). `docs/` implements compilation (how to build). Scripts and configs are project-specific, not framework meta.
11. **Wikipedia-like feel** — user expectation: everything clickable, navigable, discoverable. Flat file dumps and non-linked references = process failure. (Added post-Phase B, ref E1)

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| tfw-docs workflow exists | ✅ |
| tfw-knowledge workflow exists | ✅ |
| KNOWLEDGE.md with structured sections | ✅ |
| knowledge/ topic files with uniform format | ✅ |
| GitHub Pages on tfw.saubakirov.kz | ✅ |
| Python 3.x available | ✅ |
| MkDocs + Material + gen-files available via pip | ✅ |
| gen_docs.py implementation (Phase B) | ✅ |
| §16 Compilable Contract (Phase A) | ✅ |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| MkDocs 2.0 breaks all plugins including gen-files | Confirmed | High | Pin `mkdocs<2.0`. Monitor Zensical (successor, reads mkdocs.yml). TD-73 |
| MkDocs ecosystem enters maintenance mode (Nov 2025) | Confirmed | Medium | Material maintained until Nov 2026. Compilable contract isolates tool choice. Switching cost low (D8) |
| Artifact format drift — agents don't maintain contract | Medium | High | §16 in conventions.md. Warning-level validation in gen_docs.py |
| Broken relative links after compilation | Confirmed | High | TD-72. Phase C must fix — either link rewriting in gen_docs.py or source migration |
| Knowledge topics hardcoded in nav | Confirmed | Medium | TD-71. Phase C: dynamic nav generation |
| gen_docs.py complexity growth | Medium | Medium | 445 LOC already. Phase C additions (link rewriting, dynamic nav) risk 600+ LOC. Monitor |

## 10. RESEARCH Results

> RESEARCH completed 2026-04-05. Full findings: [RES__TFW-26](RES__TFW-26__documentation_site.md)

### Hypotheses — Final Status

| # | Hypothesis | Status | Evidence |
|---|----------|--------|----------|
| H1 | Copy + frontmatter sufficient for most artifacts | ✅ confirmed | 7/10 need only frontmatter+copy. 3 need splitting/extraction |
| H2 | Existing tool reads TFW structure directly | ⚠️ partial | No SSG reads scattered dirs. MkDocs gen-files solves with build-time scripts |
| H3 | Lightweight script <100 LOC | ❌ refuted | Actual: 445 LOC. Core logic ~150 LOC, rest = resolvers + indexes added by user demand |
| H4 | Same output for GitHub + GitLab Pages | ✅ confirmed | Same mkdocs.yml, different CI wrapper (~20 lines each) |
| H5 | docs/ at project root | ⚠️ revised | docs/ = project-specific workspace (configs, scripts, curated pages). NOT compiled output |
| H6 | Current artifact structure sufficient | ✅ confirmed | Direct audit: heading patterns consistent, tables uniform. Only contract spec missing |
| H7 | Traceability gaps fixable by rule tightening | ⚠️ deferred | Dead links accepted (D9). Traceability improvements = separate task |

### Key Decisions from RESEARCH

| # | Decision |
|---|----------|
| D1 | MkDocs + Material + `mkdocs-gen-files` — gen-files solves multi-source aggregation natively |
| D2 | No compiled output in git — CI/CD builds → deploys |
| D3 | Compilable contract = primary deliverable, more important than tool choice |
| D4 | docs/ = curated-only content + project-specific tooling |
| D5 | Utility warns on contract violations (not silent, not blocking) |
| D6 | Current artifact structure already sufficient |
| D7 | MCP server = separate future task. Contract must not preclude it |
| D8 | MkDocs ecosystem risk accepted. Low switching cost via contract isolation |
| D9 | Dead links from task references accepted and documented |

### Post-RESEARCH User Decisions

| # | Decision | Source |
|---|----------|--------|
| U1 | docs/ contains project-specific tooling: mkdocs.yml, scripts/, curated pages | User, post-RES discussion |
| U2 | Scripts NOT part of .tfw/ meta — they're implementation details | User, post-RES discussion |
| U3 | GitHub Pages index = README.md for now, curated index.md later | User, post-RES discussion |
| U4 | `.tfw/` = what (compilable contract), `docs/` = how (implementation) | User, post-RES discussion |

### Post-Execution User Decisions (Phase A/B)

| # | Decision | Source |
|---|----------|--------|
| U5 | tasks/ mandatory in docs output — excludes destroys knowledge graph traceability | User, Phase A planning. FC3: "Вариант А неприемлим" |
| U6 | KNOWLEDGE.md served as single page with TOC, no split by sections | User, Phase A ONB Q1 |
| U7 | MkDocs docs_dir: `.` (docs/ folder), not `..` (project root) — MkDocs constraint | Executor, Phase A build testing |
| U8 | User expects "Wikipedia-like feel" — everything clickable and navigable | User, Phase B live testing. E1 |
| U9 | Numeric task sorting by ID, not lexicographic | User, Phase B feedback. E3 |
| U10 | Agents reference, scripts resolve — agents write text refs, no full markdown links | User, Phase A planning. FC2 |

## 11. Strategic Session Insights (2026-04-05)

> These insights from the planning session must be captured as Fact Candidates in RES/RF.

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | TFW produces knowledge by-design. The workflow generates structured .md files that ARE the knowledge base. Documentation is a side effect, not a separate activity | philosophy | User, planning session |
| S2 | AI-queryability is the primary value. An AI agent pointed at a TFW project folder can answer questions without vectorization, elasticsearch, or indexing. Tested in KazNU assistant project | philosophy | User, planning session |
| S3 | Web UI / docs site is a side effect of well-structured knowledge, not the goal | philosophy | User, planning session |
| S4 | Agents maintain raw docs quality (structure, links, naming). Compilation is separate and deterministic | process | User, planning session |
| S5 | Current artifact structure emerged partly by accident. Traceability must become intentional everywhere | constraint | User, planning session |
| S6 | TFW's north star: knowledge exchange center. Not just web UI — queryable knowledge base for AI agents | philosophy | User, planning session |
| S7 | Compilation utility = found tool, not invented. Must run locally and via CI/CD. GitHub + GitLab | constraint | User, planning session |
| S8 | docs/ at project root level, alongside tasks/, knowledge/ | convention | User, planning session |
| S9 | Coordinator role has no explicit fact capture step. HL template has no Fact Candidates section | process | User, planning session |
| S10 | Emotional signals from users are the highest-value fact sources. Not enforced in any role's workflow | process | User, planning session |
| S11 | TFW-26 = logical culmination of TFW. Methodology closes the loop: produces the knowledge it's designed to preserve | philosophy | User, planning session |
| S12 | Core research question = what agent behavior produces traceable, interlinked, queryable artifacts. Agent behavior IS the documentation engine | process | User, planning session |
| S13 | `.tfw/` = what (compilable contract), `docs/` = how (scripts, configs, implementation). Scripts are project details, not TFW meta | convention | User, post-RES discussion |
| S14 | Primary output of TFW is a navigable knowledge graph. Graph traces: fact → source RF → decision → HL → user session. Web docs and MCP are consumers of this graph | philosophy | User, Phase A planning. FC1 |
| S15 | Tasks/ excluded from docs = destroyed knowledge graph. Without task artifacts, knowledge/ facts and KNOWLEDGE.md decisions are dead ends with no traceability | philosophy | User, Phase A planning. FC3 |
| S16 | "Нет ощущения вики движка вообще" — user's first reaction to flat file dumps. Tests verify structure, not usability. Live user testing mandatory for output-facing features | philosophy | User, Phase B live testing. E1 |
| S17 | Executor role lacks explicit session fact capture. Coordinator has §11, executor has nothing. Insights from live testing sessions are lost without explicit capture step | process | Executor, Phase B. obs. #9 |

---

*HL — TFW-26: Documentation as Output | 2026-04-05 | Post Phase A/B update*
