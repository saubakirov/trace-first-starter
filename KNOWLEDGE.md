# KNOWLEDGE.md — Trace-First Starter Knowledge Index

> Central index of project architecture, decisions, and evolution.
> **Principle**: Index, don't duplicate — link to RF/HL files, don't copy their contents.

---

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
| P10 | Knowledge by design — TFW produces a navigable knowledge graph as byproduct of its workflow. AI-queryability first, web UI second. See `compilable_contract.md` | TFW-26 HL §7.1, §11 S1/S2/S6 |

---

## 1. Architecture Map

### Framework Structure

| Component | Description | Key Files |
|-----------|-------------|-----------|
| TFW Core | Tool-agnostic framework spec | `.tfw/README.md`, `.tfw/conventions.md`, `.tfw/glossary.md` |
| Templates | Canonical artifact templates | `.tfw/templates/` (HL, TS, RES, RF, ONB, REVIEW, KNOWLEDGE, RELEASE, `research/` stage templates) |
| Workflows | Task lifecycle workflows | `.tfw/workflows/` (init, plan, research/, handoff, review, resume, docs, release, update, knowledge, config) |
| Adapters | Tool-specific bridges | `.tfw/adapters/` (claude-code, cursor, antigravity) |
| Init | AI-first initialization workflow + manual pointer | `.tfw/workflows/init.md`, `.tfw/init.md` (pointer) |
| Config | Centralized project parameters (budgets, templates, workflows, research limits, knowledge limits) | `.tfw/PROJECT_CONFIG.yaml` |
| Knowledge | Fact collection + consolidation infrastructure | `knowledge/`, `.tfw/knowledge_state.yaml`, `.tfw/workflows/knowledge.md` |
| Versioning | Framework version tracking and changelog | `.tfw/VERSION`, `.tfw/CHANGELOG.md` |
| Release | Release strategy and process | `RELEASE.md` (optional), `.tfw/workflows/release.md` |
| Claude Code Adapter | Slash commands + entry point for Claude Code | `CLAUDE.md`, `.claude/commands/`, `.tfw/adapters/claude-code/` |
| Documentation Pipeline | Compilable contract + build-time compilation to navigable docs. 681 LOC, 68 tests, 10 resolvers, literate-nav, strict mode | `compilable_contract.md`, `docs/scripts/gen_docs.py`, `docs/mkdocs.yml`, `.github/workflows/docs.yml` |
| Brand Identity | Two-color discipline (charcoal + teal), Inter/JetBrains Mono, TFW monogram logo | `docs/brand/identity.md`, `docs/img/tfw-logo.png` |
| Deploy | GitHub Pages at `tfw.saubakirov.kz`, auto-deploy on push to master | `.github/workflows/docs.yml` |

### Architecture Decisions

| # | Decision | Rationale | Source |
|---|----------|-----------|--------|
| D1 | v2→v3 migration: `.tfw/` as standalone core | Tool-agnostic, forkable, no coupling to specific AI tool | RF TFW-2 |
| D2 | Content distribution: root README = landing, `.tfw/README.md` = paper | Separation of concerns — GitHub visitors vs framework users | RF TFW-3 |
| D3 | Remove STEPS.md | Replaced by RF files + Task Board. Modern tools (KI, conversation logs) handle continuity | HL-TFW-4 §2.1 |
| D4 | Remove TASK.md | Scope/DoD lives in TS files, backlog in Task Board | HL-TFW-4 |
| D5 | Replace Summary Discipline with Trace Discipline | RF + Task Board = project memory. No separate log needed | HL-TFW-4 §3.1 |
| D6 | YAML frontmatter in `.tfw/workflows/` | Antigravity requires `description` field for slash-command registration | TFW-4 Phase A |
| D7 | KNOWLEDGE.md = optional artifact | Greenfield = overhead, brownfield = must-have | RF TFW-5 |
| D8 | tfw-docs triage gate | Minor tasks skip knowledge update (1-second decision: N/A) | HL-TFW-5 §3.2 |
| D9 | Semver (MAJOR.MINOR.PATCH) for TFW versioning | Industry standard, easy to communicate breaking vs compatible changes | TFW-6 HL §3 |
| D10 | `tfw-release` as canonical workflow, `RELEASE.md` as project context | Separation: general process in workflow, specific context in per-project file | TFW-6 HL §3, discussion |
| D11 | `tfw-update` with 🟢🟡🔴 change categorization | Prevents overwriting project customizations during framework upgrades | TFW-6 HL §3 |
| D12 | `RELEASE.md` optional (like `KNOWLEDGE.md`) | Avoids file inflation for projects that don't release | TFW-6 discussion |
| D13 | Separate review from handoff — Reviewer role with `🔒 ROLE LOCK` | Executor models self-review when review is embedded in handoff; structural fix via separate workflow + role | TFW-8 HL §2.3, §3 |
| D14 | RESEARCH as optional pipeline gate (🔬 RES) between HL and TS | HL→TS gap loses questions, alternatives, blind spots. RES artifact preserves investigation. Optional skip-path for trivial tasks | TFW-11 HL §1-§3 |
| D15 | Claude Code slash commands as thin adapters — role lock + workflow reference, no logic duplication | Each command sets role, loads context, points to canonical `.tfw/workflows/` file. Single source of truth | TFW-11/C RF §2 Key Decision #2 |
| D16 | Centralize scope budgets, template/workflow lists, and version to `PROJECT_CONFIG.yaml` | Drift proven across TFW-5/8/9/11 — each new template/workflow caused multi-file desyncs. Single YAML source eliminates this class of tech debt | TFW-12 RES §Gather, HL §1 |
| D17 | ~~Pattern B (pure reference) over Pattern A~~ **Superseded by D24** | ~~Budget values exist ONLY in config~~ → Pattern B broke agent enforcement. Reverted to Pattern A. See D24 | TFW-12 RF §Key Decisions #2, **superseded by TFW-19** |
| D18 | `tfw-init` as AI-first workflow replacing manual init.md | Agent discovers, interviews, researches, sets up — human init.md was inverted (90% mechanical, 10% valuable) | TFW-13 HL §2-§3 |
| D19 | HL update = mandatory output of RESEARCH; Briefing + Closure protocols | Research exists to refine HL, not to jump to TS. Closure writes HL recommendations; coordinator applies. Skip-bias fix: pros/cons format, user decides | TFW-14 HL §7, RES §Closure |
| D20 | Decouple pipeline statuses from document types: `🔵 HL`→`📝 HL_DRAFT`, `🟡 TS`→`🟡 TS_DRAFT`. Centralized status registry in PROJECT_CONFIG.yaml with `role` field. Concept Taxonomy (5 concepts). REJECT = user branching point | Same status count (8), self-documenting `_DRAFT` suffix for AI agents. Implicit approval = transition to next status. Registry = single source of truth for automation | TFW-15 HL §2, RES (Variant D) |
| D21 | Coordinator Mindset section in plan.md + Hard Rule #8 (external tool mandate) in research.md + stage-level mindset reminders + depth self-check in checkpoints | Root cause: plan.md framed coordination as pipeline (HL→TS→handoff), not as quality gate. Agents exhibited skip-bias, rush-bias, and internal-only research. Fix: dual-lever — mindset at coordinator level + enforcement at research stage level | TFW-17 HL §1, §7 |
| D22 | Knowledge consolidation: Fact Candidates in all artifacts (RF/REVIEW/RES), `/tfw-knowledge` 4-phase workflow (Orient→Gather→Consolidate→Prune), topic files in `knowledge/`, configurable Knowledge Gate in plan.md Phase 0. Settings = PROJECT_CONFIG, state = knowledge_state.yaml | 21 RF files analyzed — zero project facts recorded. Knowledge drift proven: facts lost between tasks (RES-12 R3, RF-11A). Design validated against Zettelkasten, LangMem, Claude Code Dream | TFW-18 HL §3, RES R1-R12 |
| D23 | Workflow compression: research.md 2397→1145 words (-52%). Remove inline templates (checkpoint/sufficiency formats) → reference templates/RES.md. Remove duplicate anti-patterns (3 blocks → 1 MUST/NEVER). Remove Example Flow (template + rules = sufficient calibration). Preserve: Mindset, stage reminders, Briefing, Closure, Hard Rules | Agents on new projects skipped research stages — workflow too long for attention budget. External research confirmed: "principles > procedures", "templates > examples", "don’t repeat standard behavior" | TFW-21 HL, RES (external best practices) |
| D24 | Restore Pattern A (inline defaults + config key) for enforcement-critical values. Supersedes D17. Config Sync Registry in `/tfw-config` workflow maps YAML keys → file locations. Interactive edit/verify modes. No scripts — AI agent is the sync engine | Pattern B (D17) broke agent enforcement of scope budgets — agents stopped reading indirection. RESEARCH-12 warned (R3/C1); user override proved costly. research.md Limits table (already Pattern A) = working proof. External research: inline = only enforcement for AI prompts | TFW-19 HL §3, RES R1-R7 |
| D25 | Research modular architecture: monolithic research.md → `research/{base,focused,deep}.md`. base.md = core algorithm (~500 words), mode files = settings (~100-170 words). Sum < monolith (650-800 vs 1165). YAML-configurable: `tfw.research.default_mode`, `modes.{focused,deep}` | Monolithic file exceeded attention budget. Tiered modes prevent overhead for simple tasks. Progressive Disclosure = agent loads only needed mode. Validated by word count analysis + industry best practices (modular instruction stack) | TFW-22 RES D2, D6, D9, D12 |
| D26 | OODA Stage Loop in research: each stage runs Observe→Orient→Decide→Act, up to `loops_per_stage` (YAML hard limit). Decide = Sufficiency Verdict (2-level: generic + mode-specific criteria). Checkpoint criteria = SOFT (report, not block). Exceeded limit → force exit + report | One-pass research = surface-level. Hard loop limit prevents stall. Soft criteria prevent blocking on unachievable conditions. ClearThought OODA + Ulysses Protocol hybrid | TFW-22 RES D7, D8, D11, Challenge #3 |
| D27 | Trust Protocol: 4-tier trust levels for user input. Business/domain = trust. Tech approach = verify externally. Numbers/claims = verify empirically. "I tried this" = trust outcome, verify reason | User answers on tech = unverified hypotheses. Agent must cross-check externally, not accept at face value. Prevents confirmation bias | TFW-22 RES D3, HL §7 |
| D28 | Naming > Explanation: right terminology creates right associations in AI agents. Small prompt + precise terms > long prompt with explanations. Adopted terms: OODA, Sufficiency Verdict, Trust Protocol, Progressive Disclosure. Claude "dreaming" pattern = proof | User observation: Claude Code used 1 word ("dreaming") to trigger complex memory consolidation behavior where paragraphs of explanation failed | TFW-22 RES D4, user insight |
| D29 | English-only templates + `tfw.content_language` config. Template structure (headings, labels, field names) = always English. Artifact content filled in language from `tfw.content_language` (default: `en`). D28 applied to all 32 heading terms. §3.1 rewritten domain-agnostic (not code-specific) | Templates = code, code = English. Industry standard for AI prompt frameworks. Mixed RU/EN wasted ~1000 tokens/cycle and confused agents | TFW-23 RES D1-D7, HL §7 |
| D30 | Researcher = 4th standalone role (after Coordinator, Executor, Reviewer). Extracted from Coordinator following TFW-8 pattern. Own Role Lock (`🔒 RESEARCHER`), own permitted/forbidden artifacts. Coordinator plans → hands off → Researcher investigates → hands back | One role + two functions = role confusion. TFW-23 crash: 6/6 gates violated. After crash recovery, "Coordinator" skipped stages and wrote HL/TS directly. Same root cause as TFW-8 (Reviewer extraction) | TFW-24 RES D3, HL §1 |
| D31 | Filesystem-as-state-machine: `research/` subfolder with stage files (`briefing.md`, `gather.md`, `extract.md`, `challenge.md`). File existence = stage completion. Step 0 (Resume Protocol): check filesystem → resume from first missing file. No chat history dependency | State Table in RES file = fragile (partial writes, format compliance). File existence = deterministic, zero-parsing, crash-resilient. External validation: artifact-based validation pattern | TFW-24 RES D1, Challenge C5 |
| D32 | RES = synthesis document (not stage aggregation). Stage sections removed from RES template — those live in `research/` subfolder. RES structure (Decisions, Hypotheses, HL Recommendations, Fact Candidates, Conclusion) intentionally different from stage files to prevent copy-paste | Mechanical aggregation = no insight. Different structure forces synthesized thinking. Researcher must re-process findings through analytical lens | TFW-24 RES D2, HL §7 P3 |
| D33 | HL §1 Vision: Amazon Working Backwards elements. Narrative ("write as if done") + Impact field + stakeholder-perspective Quote (press release pattern). §10 "Why Not Just...?" section (internal FAQ pattern). §2/§5 domain-agnostic | Press release forces user/stakeholder thinking. "Why Not Just" forces alternatives before research. Domain-agnostic instructions prevent code-only bias | TFW-24 TS Step 5, session discussion |
| D34 | Compilable Contract (`compilable_contract.md`): Source Manifest (14 entries), Reference Format (9 patterns), Resolution Rules, Frontmatter Convention, Output Nav Structure. Agents write text references (`RF TFW-18`), build-time script resolves to hyperlinks. `.tfw/` = what (contract), `docs/` = how (scripts). 445 LOC gen_docs.py, 42 tests | Primary output = navigable knowledge graph. Agents reference, scripts resolve — no tokens wasted on markdown links. Contract isolates tool choice (MkDocs swappable). tasks/ mandatory in output (user: "excludes = destroys traceability") | TFW-26 HL §7, RES D1-D9, Phase A/B RF |
| D35 | TFW-27 brand identity + wiki polish + deploy: two-color discipline (charcoal #1a1a2e + teal #0d9488), tagline "The thinking is the product", business-first README, `.tfw/README.md` stripped to pure philosophy paper (353→138 LOC), gen_docs.py link rewriter + bare ID resolver + table anchors + literate-nav (681 LOC, 68 tests), GitHub Pages deploy at `tfw.saubakirov.kz`. TFW-28 absorbed | Brand = protocol-grade, not startup-grade. README positions for business/ops first. `.tfw/README.md` = thesis only, no duplicated reference. Deploy = one-push CI. Closes TD-69..74, TD-77, TD-78 | TFW-27 HL, Phase A/B/C RF |

---

## 2. Key Artifacts

| Task | Title | Key Artifact | Why Important |
|------|-------|-------------|---------------|
| TFW-2 | Upgrade to TFW v3 | RF TFW-2 | Foundation: v2→v3 migration decisions |
| TFW-3 | README public-readiness | RF TFW-3 | Content distribution matrix (root vs .tfw/) |
| TFW-4 | Framework cleanup | HL-TFW-4 | Audit findings, redundancy analysis, meta-project awareness |
| TFW-5 | KNOWLEDGE + tfw-docs | HL-TFW-5 | Knowledge feedback loop design |
| TFW-6 | Versioning + update | HL-TFW-6 | Version scheme, release/update workflow design, RELEASE.md pattern |
| TFW-8 | Reviewer role + /tfw-review | HL-TFW-8 | Role separation, self-review fix, review workflow extraction |
| TFW-11 | RESEARCH stage + Claude Code restore | HL-TFW-11 | Optional RESEARCH gate, RES artifact, 8-status pipeline, Claude Code adapter with 9 slash commands |
| TFW-12 | Config centralization | RES TFW-12 | Single source of truth for 4 param categories. First task to use full RESEARCH stage |
| TFW-13 | tfw-init workflow | HL-TFW-13 | Init as AI-first workflow, {PREFIX}-1 pattern, /tfw-research in init |
| TFW-14 | Research interaction model | HL-TFW-14 | Briefing + Closure protocols, turn-based rhythm, Sufficiency Check, skip-bias fix, HL update gate |
| TFW-15 | Pipeline formalization | HL-TFW-15 | Status registry (`tfw.statuses`), Concept Taxonomy, HL_DRAFT/TS_DRAFT rename, REJECT branching, Phase 3.5→4 renumber |
| TFW-17 | Research depth + coordinator quality | HL-TFW-17 | Coordinator Mindset, Hard Rule #8 (external tools), stage-level reminders, depth self-check. Fixes skip-bias, rush-bias, internal-only research |
| TFW-18 | Knowledge consolidation | HL-TFW-18 | Fact Candidates in artifacts, `/tfw-knowledge` 4-phase workflow, `knowledge/` topic files, Knowledge Gate (Phase 0), configurable limits. First RESEARCH with 3 external models (Zettelkasten, LangMem, Claude Code Dream) |
| TFW-19 | Config propagation | HL-TFW-19 | Pattern A restored. Config Sync Registry (16 entries). `/tfw-config` interactive workflow (edit + verify). Enforcement hook in plan.md Phase 5. D17 superseded by D24 |
| TFW-21 | Research workflow compression | HL-TFW-21 | research.md 2397→1145 words (-52%). Template-owns-format pattern. Inline checkpoint/sufficiency moved to templates/RES.md. External best practice validation |
| TFW-22 | Coordinator & Research enrichment | HL-TFW-22 | research.md → research/{base,focused,deep}.md. OODA Stage Loop, Trust Protocol, Sufficiency Verdict, Progressive Disclosure. HL +§3.1 (visualization), +§10 (hypotheses). plan.md algorithm refactor (1213→795 words). 12 RES decisions, 6 ClearThought algorithms mapped |
| TFW-23 | Templates English standardization | HL-TFW-23 | 5 templates translated RU→EN (32 terms via D28). §3.1 rewritten domain-agnostic. `tfw.content_language: en` config added. Config Sync Registry entry. Init workflow updated |
| TFW-24 | Researcher role & RES state machine | HL-TFW-24 | 4th role (Researcher). Subfolder state machine (`research/` stage files). Resume Protocol (Step 0). RES → synthesis format. HL Vision/Impact/Quote (Working Backwards). 4 stage templates. 2 phases (A: role+workflow, B: templates) |
| TFW-25 | Values & Principles consolidation | HL-TFW-25 | README Values 5→8 items (Traces Over Code, Honesty Over Convincingness, Structural Enforcement, Naming Creates Behavior). KNOWLEDGE §0 pruned 14→7 principles. §3 Legacy pruned 35→13. §4 Tech Stack removed. knowledge/ 29→18 facts. P10-P13 → conventions §11 Design Rules |
| TFW-26 | Documentation as Output | HL-TFW-26 | Compilable Contract. gen_docs.py (445 LOC, 42 tests). MkDocs + Material + gen-files. 6 reference resolvers. Structured tasks index. D34. Coordinator fact capture (§11 in HL template, plan.md Step 4b). Closed as MVP → spawned TFW-27 (wiki polish), TFW-28 (deploy) |
| TFW-27 | Wiki polish & brand & deploy | HL-TFW-27 | 3 phases: A (brand identity — logo, palette, typography, tagline, README hero), B (link resolution — 4 gen_docs.py features, 681 LOC, 68 tests, literate-nav, strict mode fix), C (GitHub Pages deploy at tfw.saubakirov.kz). `.tfw/README.md` stripped to pure philosophy paper. TFW-28 absorbed. D35. Closes TD-69..74, TD-77, TD-78 |

---

## 3. Legacy & Deprecation

| Item | Status | When | Replacement | Source |
|------|--------|------|-------------|--------|
| Monolithic `research.md` (1165 words) | Replaced | 2026-04-04 | `research/{base,focused,deep}.md` — modular architecture with YAML-configurable modes | TFW-22 D25 |
| Inline bloat in plan.md (prerequisites, scope budget table, status transitions, anti-patterns) | Removed | 2026-04-04 | Ref-inside-step pattern (D25/P12). plan.md 1213→795 words (-34%) | TFW-22 |
| plan.md info-dump format | Replaced | 2026-04-04 | Algorithm-first format: numbered steps + GATE/WAIT + refs. DNA/Library split (P12) | TFW-22 |
| HL template without visualization or hypothesis sections | Replaced | 2026-04-04 | §3.1 Result Visualization (ascii mandatory), §10 RESEARCH Case (hypotheses + blind spots) | TFW-22 |
| Mixed RU/EN headings in HL, TS, RF, ONB, REVIEW templates | Replaced | 2026-04-04 | All 5 templates → pure English. 32 terms translated per D28. `tfw.content_language` config for content filling | TFW-23 |
| §3.1 instructional block (engineering-focused: ASCII/Mermaid only) | Replaced | 2026-04-04 | Domain-agnostic Variant A: diagrams, tables, outlines/mockups, sample output | TFW-23 D7 |
| Coordinator conducts own research ("Research Mode") | Replaced | 2026-04-04 | Researcher = standalone 4th role with `🔒 ROLE LOCK: RESEARCHER`. Coordinator hands off via `/tfw-research` | TFW-24 D30 |
| State Table in RES file for tracking research progress | Replaced | 2026-04-04 | Filesystem state machine: `research/` subfolder, file existence = gate | TFW-24 D31 |
| RES template with Gather/Extract/Challenge stage sections | Replaced | 2026-04-04 | RES = synthesis format (Decisions, Hypotheses, HL Recommendations, Conclusion). Stages → `research/` subfolder files | TFW-24 D32 |
| HL §1 "Vision" with generic instructions | Replaced | 2026-04-04 | Vision narrative ("write as if done") + Impact field + stakeholder Quote + "Why Not Just...?" (Working Backwards) | TFW-24 D33 |
| Inline stage file format in conventions.md §4 | Replaced | 2026-04-04 | Stage templates in `.tfw/templates/research/` (briefing, gather, extract, challenge) | TFW-24 Phase B |
| P4/P6/P10-P14 in KNOWLEDGE §0 | Moved/Removed | 2026-04-04 | P14 → README Values (Structural Enforcement). P10-P13 → conventions.md §11 Design Rules. P4/P6 = obvious from code | TFW-25 |
| `.tfw/README.md` technical reference sections (353 LOC) | Stripped | 2026-04-08 | Pure philosophy paper (138 LOC). Removed: project structure tree, artifact types table, lifecycle, scope budgets, workflows table, execution modes, roles, Getting Started, Who This Is For. All → `conventions.md` / `glossary.md` refs | TFW-27 D35 |
| `.tfw/README.md` §Evolution (v1/v2/v3 history) | Replaced | 2026-04-08 | Link to `CHANGELOG.md`. Version history not philosophy | TFW-27 |
| TFW-28 (Deploy docs) as standalone task | Absorbed | 2026-04-08 | Merged into TFW-27/C. Deploy = one phase, not a separate task | TFW-27 D35 |

---

## 4. Project Facts

> Index of verified project knowledge. Details in `knowledge/` topic files.
> Updated by `/tfw-knowledge` consolidation.

| Category | Count | Topic File |
|----------|-------|------------|
| philosophy | 11 facts | [→](knowledge/philosophy.md) |
| convention | 9 facts | [→](knowledge/convention.md) |
| process | 8 facts | [→](knowledge/process.md) |
| constraint | 4 facts | [→](knowledge/constraint.md) |
| environment | 2 facts | [→](knowledge/environment.md) |
| stakeholder | 1 fact | [→](knowledge/stakeholder.md) |

---

> **Maintenance**: This file is updated via the `tfw-docs` workflow after each REVIEW.
> See `.tfw/workflows/docs.md` for the update process.
