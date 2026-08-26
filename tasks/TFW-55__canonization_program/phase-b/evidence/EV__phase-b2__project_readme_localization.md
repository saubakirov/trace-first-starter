# EV — TFW-55 / Phase B.2: Project README Restoration and Localization

> **Date**: 2026-08-26
> **Author**: Codex Executor
> **Task**: TFW-55 / Phase B.2
> **TS**: [TS Phase B.2](../TS__phase-b2__project_readme_localization.md)
> **State**: DRAFT REMEDIATION AUDIT — pre-freeze self-gate complete; draft critics dispositioned; exact-final critic rechecks pending

---

## Environment

| Field | Value |
|---|---|
| OS | Microsoft Windows 11 Pro |
| Shell / runtime | Windows PowerShell 5.1.26100.8655; Git CLI |
| Repository state | Detached worktree; start `2a534c70f31807b0f131b7a83e46e249715697e0`; amended contract freeze `5dee93d31fde4ee5ea279880137e83fb50fca296` |
| Verification target | Working-tree draft of `README.md`, `README.ru.md`, and `README.kk.md`; English board compared with exact start commit |
| CI / Pipeline | Local deterministic document and Git checks; no external availability claim |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | Exact historic public prefix reproduced as 1,485 whitespace words and SHA-256 `d14f9b89b174a59f8cd3177dfd111147ec2efdfcb3254fd3790788896b11638d`; every baseline heading has a ledger disposition | Git object `b924926:README.md`, normalized LF | VERIFIED | §1–2 |
| E2 | AC-2 | All baseline practical sections, three audiences, three start states, mechanics, structure, update path, and public routes remain; seven-question cold walkthrough has an action path in EN/RU/KK | Working-tree draft | VERIFIED | §3–4 |
| E3 | AC-3 | Definition and authority boundary match the reviewed semantic source; unsupported automation/documentation/agent-authority claims are replaced; no NS1/NS2/NS3 exposition or second essay appears | `.tfw/README.md` blob `71a4d725cff7d0d7508403589195e9f87a0fc49a` | VERIFIED | §2, §5 |
| E4 | AC-4 | Edition facts, starts, all 11 commands, root/core paths, adapters, lifecycle, version/update, local targets, and preserved external URL strings match current sources | Repository at execution draft | VERIFIED | §5–7 |
| E5 | AC-5 | Russian draft covers every functional block, preserves exact identifiers/destinations, declares English authority, excludes the live board, and passes strict UTF-8 | Working-tree draft | VERIFIED | §3, §6, §8; independent critic pending under E7 |
| E6 | AC-6 | Kazakh draft covers every functional block, preserves exact identifiers/destinations, declares English authority, excludes the live board, and passes strict UTF-8 | Working-tree draft | VERIFIED | §3, §6, §8; independent critic pending under E7 |
| E7 | AC-7 | Two isolated critics inspected exact freeze `ff26598`; RU reported H0/M6/L4, KK H1/M8/L3; every finding is dispositioned and the KK HIGH is corrected; exact-final rechecks remain | Frozen draft plus bounded remediation candidate | DEFERRED | `LANG_REVIEW__phase-b2__ru.md`, `LANG_REVIEW__phase-b2__kk.md` |
| E8 | AC-8 | Visible three-language switch; exactly one English board and zero localized boards; non-TFW-55 tail identity; TFW-60 identity; strict UTF-8; public-prefix local-link checks; `.tfw/README.md` blob | Start vs working tree | VERIFIED | §6, §8–9 |
| E9 | AC-9 | Corrective chain identifies historic production baseline, amended contract, owner rejection, and stale D66 closure route; execution scope contains only the approved files | Start vs working tree | VERIFIED | §10; final critic lineage and RF pending |

## 1. Reconstruction Baselines

| Item | Result |
|---|---|
| Historic source | Exact public prefix of `b924926:README.md`, stopping before `## Task Board` |
| Historic descriptive count | 1,485 whitespace-delimited words |
| Historic normalized-LF SHA-256 | `d14f9b89b174a59f8cd3177dfd111147ec2efdfcb3254fd3790788896b11638d` |
| Executor start | `2a534c70f31807b0f131b7a83e46e249715697e0` |
| Full live Task Board normalized-LF SHA-256 at start | `4a11135d87a8dbe8583560faab61147dd5c7a0b0d769029cc3aed6e7ff409ccc` |
| Live Task Board excluding the TFW-55 row at start | `02b8e94e0052907a40b129b3a463111017999d81070a933adfde5e4eb7330a37` |
| Same non-TFW-55 tail in current draft | `02b8e94e0052907a40b129b3a463111017999d81070a933adfde5e4eb7330a37` — exact equality |
| TFW-60 row | Exact equality; remains `🔬 RES (Iteration 2)` |
| Contract authority | Master freeze `5dee93d31fde4ee5ea279880137e83fb50fca296`, Amendment A6; approved Phase B.2 HL/TS |
| Reviewed essay integrity | `.tfw/README.md` blob `71a4d725cff7d0d7508403589195e9f87a0fc49a` |

The historical README was read through `git show`; no historical whole-file checkout or restore was performed. Only the current public prefix is replaced. The board tail remains sourced from the exact Executor start commit, with normal TFW-55 workflow transitions as the sole allowed difference.

## 2. Complete Keep / Update / Add / Remove Ledger

| Baseline block or claim class | Draft disposition | Functional result | Change class and source |
|---|---|---|---|
| Hero: logo, title, tagline, badges | **KEEP + ADD** | Brand identity retained; visible `English · Русский · Қазақша` switch and English semantic-source notice added | Stale navigation / authority surface; Phase B.2 HL ledger |
| Opening pain/promise and North Star route | **KEEP + UPDATE** | Continuity problem and practical repository promise retained; one compact definition and direct essay route replace overclaims | Authority correction + minimal philosophy alignment; reviewed `.tfw/README.md` |
| `## Editions` | **KEEP + UPDATE** | Light, Assisted, and Full are selectable by work shape and risk; copy-the-contents rule and migration link are explicit | Current Edition facts; `editions/README.md` |
| `## Who TFW Is For` | **KEEP + UPDATE WORDING** | Product leaders, analysts/researchers, engineers, and non-code users retain recognizable problems and uses | Factual/authority correction: unsupported absolutes removed; function unchanged |
| `## Quick Start` | **KEEP + UPDATE** | Copyable routes remain for new, existing, and configured projects; Edition-first selection and state preservation are explicit | Current Edition/command/path facts; `editions/README.md`, `.tfw/quickstart.md` |
| `### FAQ` | **KEEP + UPDATE** | Reading burden, supported tools, non-code use, knowledge-tool distinction, continuity limit, and visual help remain answered | Factual + authority correction; adapters, Edition history, semantic source |
| `## How It Works` | **KEEP + UPDATE** | Five-row explanatory table remains, now tied to inspectable capabilities, verified continuation, consolidation, human responsibility, and proportional discipline | Authority correction + minimal philosophy alignment; conventions and reviewed essay |
| `## What's Inside` | **KEEP + UPDATE** | Root files and Full `.tfw/` structure remain discoverable; philosophy and mechanics destinations are separated | Current path facts; live repository, conventions, workflows |
| `## Tool Adapters` | **KEEP + UPDATE** | Claude Code, Cursor, Antigravity, Codex, and plain-chat entry behavior remain visible | Current adapter facts; `.tfw/adapters/`, Codex adapter README |
| `## Key Concepts` | **KEEP + UPDATE** | Lifecycle, conditional states, roles, modes, budgets, evidence, trace types, and versioning remain actionable | Current mechanics; `.tfw/conventions.md`, `.tfw/glossary.md`, config |
| `## Updating TFW` | **KEEP + UPDATE** | Exact `/tfw-update` action and current procedure/history links remain | Current command/path fact; `.tfw/workflows/update.md` |
| `## Links` | **KEEP + UPDATE NAVIGATION** | Edition/start, mechanics, philosophy, history/evidence, help, visuals, docs, repository, author, and license routes remain distinct | Stale navigation; current repository paths; external strings preserved |
| “automatically captures” | **REMOVE CLAIM** | Replaced by deliberate selection and versioned traces | Authority correction; trace is selected, not automatic |
| “traces replace documentation” | **REMOVE CLAIM** | Repository guide explains traces alongside documentation/help routes | Minimal philosophy correction; no replacement guarantee |
| “decisions document themselves” | **REMOVE CLAIM** | Humans still select what is authoritative and worth preserving | Authority correction |
| unbounded “AI agents are team members” | **REPLACE CLAIM** | Agents perform bounded roles; humans retain the six explicit responsibilities | Authority correction |
| deterministic resume / identical reproduction | **REPLACE CLAIM** | Next participant inspects and verifies an explicit checkpoint, then exercises judgment | Factual/authority correction |
| anthropomorphic “self-aware product” | **REPLACE CLAIM, KEEP CAPABILITY** | Inspectable purpose/decision/evidence/state/debt capability is explicit | Minimal philosophy alignment |
| `## Task Board` and tail | **KEEP FROM START** | Only TFW-55 normal row changes; every other line remains exact | Reconstruction boundary; start commit comparison |

No practical section was removed or consolidated away. The final descriptive counts are reported for provenance only; no size target governed editing.

## 3. Functional Parity Matrix

| Practical function | English | Russian | Kazakh | Result |
|---|---|---|---|---|
| Hero, opening, definition, essay route | Top/opening | Top/opening | Top/opening | Full parity |
| Edition choice and destinations | `Editions` | `Редакции` | `Редакциялар` | Light/Assisted/Full facts and paths exact |
| Product-leader use case | First audience card | `Руководителям продукта…` | `Өнім жетекшілері…` | Preserved |
| Research/analysis use case | Second audience card | `Аналитикам и исследователям…` | `Талдаушылар мен зерттеушілер…` | Preserved |
| Engineering use case | Third audience card | `Инженерам…` | `Инженерлер…` | Preserved |
| Non-code capability | Audience opening + FAQ | Audience opening + FAQ | Audience opening + FAQ | Preserved without adding scope |
| New-project start | `New project` prompt | `Новый проект` prompt | `Жаңа жоба` prompt | Copyable; exact URL/paths |
| Existing-project start | `Existing project` prompt | `Существующий проект` prompt | `Қолданыстағы жоба` prompt | Copyable; preserve-first route |
| Configured-project start | `Already configured` | `TFW уже настроен` | `TFW бапталған` | Exact `/tfw-plan` first action |
| Full command surface | Quick Start command paragraph | Same section | Same section | Same 11-command set |
| FAQ functions | Six questions | Six natural questions | Six natural questions | Full functional parity |
| How-work model | Five-row table | Five-row table | Five-row table | Full semantic parity |
| Root and `.tfw/` structure | `What's Inside` | `Что находится…` | `Репозиторийде не бар` | Exact files/paths |
| Adapters | `Tool Adapters` | `Адаптеры инструментов` | `Құрал адаптерлері` | Exact tools/entry paths |
| Lifecycle and concepts | `Key Concepts` | `Основные понятия` | `Негізгі ұғымдар` | Tokens and identifiers exact |
| Update path | `Updating TFW` | `Обновление TFW` | `TFW жаңарту` | Exact `/tfw-update` and links |
| Public routes | `Links` | `Ссылки` | `Сілтемелер` | All 35 public targets; intended board-anchor localization only |
| Live operational board | English only | Absent | Absent | Contract satisfied |

## 4. Cold Newcomer Walkthrough

| Question | EN click/action sequence | RU click/action sequence | KK click/action sequence | Result |
|---|---|---|---|---|
| 1. What is this? | Opening → repository promise → Project North Star link | Opening → repository description → Project North Star | Opening → repository description → Project North Star | Repository, methodology, and Philosophy-of-Trace grounding are explicit |
| 2. Is it for me? | `Who TFW Is For` → select product, research, engineering, or non-code case | `Кому подходит TFW` | `TFW кімге арналған` | Four required use shapes are recognizable |
| 3. Which Edition? | `Editions` table → compare work/risk → click Light, Assisted, Full, or guide | `Редакции` table and same destinations | `Редакциялар` table and same destinations | Human has clear selection responsibility |
| 4. How do I begin? | `Quick Start` → copy new/existing/configured prompt → follow Edition README or Full quickstart | `Быстрый старт` → choose matching project state | `Жылдам бастау` → choose matching project state | Three actionable starts in every language |
| 5. Which command starts work? | Configured prompt → `/tfw-plan`; paragraph explains handoff/review/resume and all other commands | Same identifiers in configured block | Same identifiers in configured block | Exact copyable command surface |
| 6. What is in the repository? | `What's Inside` → root/core → adapters → concepts → update | `Что находится…` and following sections | `Репозиторийде не бар` and following sections | Structure and operating model explained without opening every file |
| 7. Where is deeper truth? | `Links`: philosophy → `.tfw/README.md`; mechanics → conventions/workflows; history/evidence → board/tasks/knowledge/changelog | Same routes; English board linked by `README.md#task-board` | Same routes; English board linked by `README.md#task-board` | Philosophy, mechanics, and corpus remain separate |

## 5. Source-by-Source Fact Table

| README fact surface | Authority checked | Draft result |
|---|---|---|
| TFW definition, selected Trace, human/agent boundary, non-promises | Reviewed `.tfw/README.md` at blob `71a4d725…` plus Phase B.2 AC-3 minimum | One practical definition; six human responsibilities and bounded agents explicit; essay carries full argument |
| Light / Assisted / Full choice, availability, migration | `editions/README.md`; edition directories and Assisted `MIGRATION.md` | Descriptions and destinations match; no unsupported hook/automation guarantee |
| Full acquisition and initialization | `.tfw/quickstart.md` | Clone/copy `.tfw/`, then follow quickstart; existing state preserved before changes |
| Exact commands | Root `AGENTS.md`, canonical `.tfw/workflows/`, registered local skills | All 11 `/tfw-*` commands present identically in EN/RU/KK |
| Roles, modes, lifecycle, evidence, scope | `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/project_config.yaml` | Current identifiers and conditional-state explanation used |
| Root structure | Live repository root | `README.md`, `AGENTS.md`, `KNOWLEDGE.md`, `TECH_DEBT.md`, `RELEASE.md` resolve |
| Full core structure | Live `.tfw/` tree | README, conventions, glossary, templates, workflows, adapters, quickstart, config, version, changelog resolve |
| Adapters and entry points | Live `.tfw/adapters/`; Codex adapter README | Claude Code, Cursor, Antigravity, Codex paths exact; plain chat makes no installed-adapter claim |
| Version/update | `.tfw/VERSION` = `1.3.0`; `.tfw/workflows/update.md`; changelog | Exact version path, `/tfw-update`, process and history routes preserved |
| License | Root `LICENSE` | MIT route exact |
| History/evidence | English board, `tasks/`, `KNOWLEDGE.md`, changelog | Separate routes supplied; localized files carry no operational state |
| External help/docs/repo/author | Exact strings from `b924926` practical README | Preserved without claiming current live availability |

## 6. Commands, Paths, URLs, and Anchors

### Exact command set in every language

`/tfw-config`, `/tfw-docs`, `/tfw-handoff`, `/tfw-init`, `/tfw-knowledge`, `/tfw-plan`, `/tfw-release`, `/tfw-research`, `/tfw-resume`, `/tfw-review`, `/tfw-update`

The set comparison is exact: 11/11 in EN, 11/11 in RU, and 11/11 in KK.

### Public target comparison

- Each language public guide contains 35 unique Markdown/HTML targets.
- EN, RU, and KK target sets are identical except the intentional history route: EN uses the local `#task-board` anchor; RU/KK use `README.md#task-board` because the live board exists only in English.
- Every local target in the three public guides resolves in the working tree.
- English contains exactly one `## Task Board`; RU and KK contain zero such headings and zero board rows.

### External URL string ledger

The same eight established external URL strings occur in EN, RU, and KK: two shields.io badges; the GitHub repository/clone URL; NotebookLM FAQ, slides, and video URLs; documentation site; and author site. No URL was silently replaced. The visual-help FAQ explicitly says that availability is not claimed.

## 7. English Block-Change Classification

| Changed block | Allowed reason |
|---|---|
| Language switch and semantic-source notice | Stale navigation + authority correction |
| Opening paragraphs | Unsupported-claim removal + minimal philosophy alignment |
| Editions table and copy rule | Current Edition/path facts |
| Audience copy | Unsupported absolute removal; practical function retained |
| Three Quick Start paths and command paragraph | Current Edition/command/path facts |
| FAQ answers | Factual and authority correction; established external navigation preserved |
| How It Works rows | Determinism/automation/agent-authority correction |
| Root/core structure tables | Current path and authority facts |
| Adapter table | Current adapter/entry-path facts |
| Lifecycle/concepts table | Current mechanics and navigation |
| Update explanation | Current command/procedure facts |
| Links table | Stale navigation and explicit route separation |

Anti-paraphrase inspection: the README does not reproduce the NS1/NS2/NS3 structure, principle list, non-goal argument, or essay narrative. Philosophy alignment is limited to the opening definition/boundary, corrections where an old practical claim was unsafe, and links back to the essay.

## 8. Localization and Encoding Self-Gate

| Check | RU | KK |
|---|---|---|
| Full ledger mapping | PASS | PASS |
| Seven newcomer questions | PASS | PASS |
| Exact Edition names and identifiers | PASS | PASS |
| Exact 11-command set | PASS | PASS |
| Exact local/external destination parity | PASS | PASS |
| English semantic-source declaration | PASS | PASS |
| No live board or operational state | PASS | PASS |
| Strict UTF-8 decoder | PASS | PASS |
| Replacement-character/common mojibake scan | PASS | PASS |
| Self-check for new promise/authority/capability | PASS | PASS |
| Independent naturalness/calque/translation-smell critic | DRAFT PASS: H0/M6/L4, all fixed | DRAFT BLOCKED: H1/M8/L3, all fixed |
| Required definition back-translation | English supplied and recorded | English + Russian supplied and recorded |
| Exact-final recheck by same critic | PENDING E7 | PENDING E7 |

The Executor does not treat this self-gate as language certification. The frozen drafts must pass separate RU and KK critics, and the same critics must recheck the exact final commit.

### Draft critic lineage and dispositions

| Language | Critic task | Frozen target | Draft findings | Remediation candidate | Disposition |
|---|---|---|---|---|---|
| RU | `/root/ru_critic` | `ff26598`, blob `d9f3c7af7a0cf9708a548ae5be5c410939186599` | HIGH 0, MEDIUM 6, LOW 4 | blob `54c24eff4c5c6a0f13e0f80907ac1c3ba2f48a89` | All 10 fixed; exact-final recheck pending |
| KK | `/root/kk_critic` | `ff26598`, blob `d1d5e80b5ad45d7dc6c4efc8926d9b5bae22b4fe` | HIGH 1, MEDIUM 8, LOW 3 | blob `571884b21e09aef44b4f1a6ae629973e626ab8d8` | All 12 fixed, including KK-H1 authority drift; exact-final recheck pending |

The full fixed packets, required back-translations, every initial finding, and every disposition are preserved in the two Phase B.2 `LANG_REVIEW` files. A self-audit also restored the baseline Key Concepts `Conduct` route in all three languages; this adds one bounded mechanics row and is included in the exact-final recheck packet.

## 9. Board and Source Integrity

| Check | Result |
|---|---|
| English prefix/tail split | PASS — exactly one split at `## Task Board` |
| Start tail excluding TFW-55 vs current draft | PASS — exact normalized-LF SHA-256 equality `02b8e94e…` |
| TFW-60 row | PASS — byte-identical, `🔬 RES (Iteration 2)` |
| RU/KK board content | PASS — none |
| `.tfw/README.md` | PASS — unchanged reviewed blob `71a4d725cff7d0d7508403589195e9f87a0fc49a` |
| Historic whole-file restore | PASS — not performed |
| Old B1 traces | PASS — not modified |
| Phase/master contracts and source docs | PASS — not modified |

## 10. Scope, Provenance, and Counts

The execution plan permits 8 total paths: 5 new and 3 modified. The planned final set is exactly the three root READMEs plus the new Phase B.2 ONB, EV, RU/KK language reports, and RF. No Edition, core, adapter, visual, knowledge, BoK, mechanics, research, master/phase plan, old B1 trace, or unrelated file is writable in this phase.

Descriptive counts at the frozen draft and remediation candidate:

| File/region | Whitespace words | Lines |
|---|---:|---:|
| Historical `b924926` public prefix | 1,485 | provenance only |
| English frozen public prefix `ff26598` | 2,129 | 249 before board heading |
| English remediation candidate | 2,149 | 250 before board heading |
| Russian remediation candidate | 2,032 | 240 |
| Kazakh remediation candidate | 2,009 | 240 |

The owner-requested source-expansion provenance classification is explicit:

| English section | Historic → frozen words | Concrete necessity for added material | Candidate effect |
|---|---:|---|---|
| Editions | 77 → 207 | Current three-Edition decision table, current availability/contents, copy-the-contents rule, and migration/selection route from `editions/README.md` | No post-freeze expansion |
| Quick Start including FAQ | 429 → 611 | Edition-first choice; current new/existing/configured actions; state-preserving installation/migration; exact 11-command and Codex routes; bounded corrections to automatic/documentation/reproduction claims | No post-freeze expansion |
| Key Concepts | 96 → 220 | Current conditional lifecycle, roles, modes, budgets, evidence ownership, trace-type separation, and version routes | 220 → 240 solely to restore the baseline Conduct function found missing in self-audit |
| All other blocks combined | Remaining 208-word frozen growth | Human/agent authority correction; current repository/adapters/workflows; retained audience/use cases; explicit mechanics/philosophy/history/help routes; no NS1/NS2/NS3 exposition | Critic remediation changes wording, not function |

Every addition therefore maps to a newcomer capability, current factual correction, authority correction, or retained baseline function. Nothing was added merely to reach or defend a document size; no deletion or compression was performed for a numerical target.

Counts describe the documents and do not determine pass/fail. No ceiling, target band, or compression ratio was used.

The earlier B1 RF and REVIEW remain visible and unchanged. Their APPROVE is superseded by the owner's rejection because they checked compliance with the wrong compact-doorway function. `KNOWLEDGE.md` D66 and its compact-doorway architecture statement are intentionally stale; correction is mandatory only after a new formal APPROVE through `/tfw-docs`, outside Executor authority.

## Pre-Exact-Final Verdict

Evidence verdict: **8 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A**.

The complete functional/source/newcomer/board self-gate passes. Draft critic findings are fully dispositioned. The sole deferred gate is the same two critics' exact-final recheck of the committed remediation, with unresolved HIGH required to equal zero in both languages.

---

*EV — TFW-55 / Phase B.2: Project README Restoration and Localization | 2026-08-26*
