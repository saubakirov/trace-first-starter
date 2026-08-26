# EV — TFW-55 / Phase B: Multilingual public entry

> **Date**: 2026-08-26
> **Author**: Codex (Executor)
> **Task**: TFW-55
> **TS**: [TS Phase B](../TS__phase-b__multilingual_public_entry.md)
> **Verified production commit**: `caee273c690ef5b2da34a41635f9c7de78736881`
> **Approved baseline**: `6ec4d6f763a3007e4b887cda80817bb8f8c7538b`

---

## Environment

| Field | Value |
|---|---|
| OS | Microsoft Windows NT `10.0.26200.0` |
| Shell | Windows PowerShell `5.1.26100.8655` |
| Git | `2.42.0.windows.1` |
| Runtime | Repository-local Markdown and PowerShell checks; no application runtime |
| Deploy target | N/A — repository-local documentation change |
| CI / Pipeline | Local deterministic verification |

The configured `lint`, `test`, and `verify` entries only echo `configure your ... command`; they ran successfully but are placeholders, not substantive gates. The Phase B Markdown-specific gates below are the actual verification.

## Evidence

All TS evidence classifications are N/A because Phase B makes no live-environment behavior or user-study claim. Each row still records the deterministic document gate and its result.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | English section is a compact doorway with problem, definition, source routing, removed-detail disposition, and no forbidden claim | Git tree + manual semantic inspection | N/A | [`README.md`](../../../../README.md); [subtraction ledger](#subtraction-ledger-and-old-claim-dispositions) |
| E2 | AC-2 | Russian semantic units, naturalness, authority, UTF-8, no board/state, and zero unresolved HIGH | Independent RU task + local checks | N/A | [`README.ru.md`](../../../../README.ru.md); [RU report](LANG_REVIEW__phase-b__ru.md) |
| E3 | AC-3 | Kazakh semantic units, naturalness, terminology/back-translation, UTF-8, no board/state, and zero unresolved HIGH | Independent KK task + local checks | N/A | [`README.kk.md`](../../../../README.kk.md); [KK report](LANG_REVIEW__phase-b__kk.md) |
| E4 | AC-4 | Six invariants and authority boundary map across all three languages with zero missing/extra/contradictory units | Three-column inspection | N/A | [Invariant matrix](#semantic-invariant-and-authority-matrix) |
| E5 | AC-5 | First-block language switch, all local targets, `NS1`–`NS3`, Task Board anchor, paths, URLs, and commands | PowerShell link/anchor scan | N/A | [Link results](#language-switch-link-anchor-and-command-results) |
| E6 | AC-6 | Edition routes and claims match current guide; new/existing/configured actions and exact Full commands are usable | Cold navigation inspection | N/A | [Edition/Quick Start check](#editions-and-quick-start-fact-check) |
| E7 | AC-7 | Understand/use/audit click paths plus public repository/author/license and source status | Three-language walkthrough | N/A | [Route walkthrough](#three-route-walkthrough) |
| E8 | AC-8 | Raw word budgets, English-only board, byte-identical non-TFW-55 board tail, and subtraction accounting | Baseline/final Git objects | N/A | [Counts](#raw-markdown-word-counts); [board check](#task-board-integrity) |
| E9 | AC-9 | Separate frozen-draft critiques, closure commit, exact-final rechecks, back-translations, and `unresolved HIGH=0` | Two isolated Codex tasks | N/A | [Critique registry](#independent-language-critique-registry) |
| E10 | AC-10 | Scope, provenance, reviewed North Star blob, no forbidden subsystem/artifact, and trace consistency | Git path/blob checks | N/A | [Provenance and scope](#provenance-scope-and-consistency) |

## Semantic invariant and authority matrix

| Required invariant | English `README.md` | Russian `README.ru.md` | Kazakh `README.kk.md` | Result |
|---|---|---|---|---|
| 1. TFW is a human–AI methodology grounded in Philosophy of Trace | `Work that can continue`: functional definition | `Чтобы работу можно было продолжить`: `методология ... основанная на Философии Следа` | `Жұмыс жалғасын табуы үшін`: `Із философиясына негізделген ... әдіснама` | PASS |
| 2. Purpose, legitimate authority, judgment, acceptance, accountability, and stop responsibility remain human | Definition names every item and human responsibility to stop | Definition keeps all items with `право и обязанность остановить` | Definition keeps all items with `тоқтату құқығы мен міндеті` | PASS |
| 3. Agents are bounded; selected durable Trace preserves continuity | Definition: bounded work; selected durable Trace holds context, decisions, result/state, continuation | Definition: agents stay in boundaries; a durably kept selected `След (Trace)` carries all continuity fields | Definition: agent stays inside its boundary; selected durable `Із (Trace)` carries all continuity fields | PASS |
| 4. Editions are proportional, selected by work/risk, not prestige | `Choose the smallest Edition that fits`; explicitly not maturity ranks | `Выберите редакцию под задачу`; not maturity levels; smallest sufficient choice | `Жұмысқа сай редакцияны таңдаңыз`; not maturity stages; smallest sufficient choice | PASS |
| 5. North Star owns stable meaning; mechanics and history live elsewhere | Closing authority paragraph separates North Star, specification, and corpus | Closing paragraph separates Project North Star, specification, corpus, and Task Board statuses | Closing paragraph separates Project North Star, specification, corpus, and Task Board statuses | PASS |
| 6. Domain/vendor independence; no deterministic, automatic-truth, self-documenting, or participation-created authority promise | Explicit boundary paragraph | Explicit domain/supplier/platform boundary and four non-goals | Explicit any-domain/vendor boundary and four non-goals | PASS |

`Self-aware project` is omitted in all three short doorways, as AC-4 allows. No doorway represents Trace as a transcript, hidden reasoning, automatic truth, or deterministic reproduction. English is declared the semantic source; both localizations explicitly yield on conflict and do not create a second canon, BoK, or governance surface.

## Terminology matrix

| Concept | English | Russian | Kazakh | Verification |
|---|---|---|---|---|
| Brand | `Trace-First Workflow (TFW)` | unchanged | unchanged | PASS |
| Foundation | `Philosophy of Trace` | `Философия Следа` | `Із философиясы` | PASS |
| Core record | `Trace` | `След (Trace)` on first use | `Із (Trace)` on first use | PASS |
| Product anchor | `Project North Star`; `NS1`–`NS3` | product name and IDs unchanged | product name and IDs unchanged | PASS |
| Editions | Light / Assisted / Full | names and paths unchanged; explanation localized | names and paths unchanged; explanation localized | PASS |
| Commands and paths | `/tfw-*`, repository paths | unchanged | unchanged | PASS |
| Human authority | purpose/legitimate authority/judgment/acceptance/accountability/stop responsibility | natural functional equivalent; final English back-translation matches | natural functional equivalent; final EN/RU back-translations triangulate | PASS |

## Independent language critique registry

| Language | Critic task | Draft commit / blob | Final commit / blob | Initial HIGH | Final HIGH | Report |
|---|---|---|---|---:|---:|---|
| Russian | `01a03d51-1f84-79a3-a60d-79047fe60306` | `437f7a9b...` / `063f717d...` | `caee273c...` / `5fde9845...` | 4 | 0 | [LANG_REVIEW RU](LANG_REVIEW__phase-b__ru.md) |
| Kazakh | `01a03d51-2480-7ef1-a4d9-f9ad203793f8` | `437f7a9b...` / `614e610a...` | `caee273c...` / `b4c2ca57...` | 2 | 0 | [LANG_REVIEW KK](LANG_REVIEW__phase-b__kk.md) |

Both tasks received the same bounded authority packet plus only the English doorway, their target localization, and the fixed rubric. They did not receive a preferred verdict, edit production, or issue a TFW REVIEW. The exact final blobs were rechecked through `git show`; both worktrees remained clean.

Disposition summary:

- RU H1–H4 closed human/agent/stop authority, Editions logic and calques, domain/vendor/non-goal narrowing, and Task Board authority overclaim.
- KK H1–H2 closed stop/bounded-agent/continuation language and Edition/capability drift.
- Materially useful MEDIUM findings improved opening prose, Trace language, Quick Start safety, domain breadth, and authority routing.
- Remaining stylistic alternatives are explicitly non-blocking in the reports; no taste-only revision cycle was started.
- Final back-translations preserve the functional definition and expose no hidden semantic expansion.

Final severity: **Russian unresolved HIGH=0; Kazakh unresolved HIGH=0**.

## Raw Markdown word counts

Counting convention: strict UTF-8 text; whitespace-delimited non-empty Markdown tokens. For English, the input stops immediately before `## Task Board`; the heading and the entire board tail are excluded. Russian and Kazakh count their whole files.

| Surface | Baseline | Final | Net | Limit / orientation | Result |
|---|---:|---:|---:|---|---|
| English public doorway | 1,485 | 523 | -962 | hard ceiling 800; preferred 550–700 | PASS |
| Russian doorway | absent | 528 | +528 | hard ceiling 800; preferred 550–700 | PASS |
| Kazakh doorway | absent | 526 | +526 | hard ceiling 800; preferred 550–700 | PASS |
| Reviewed `.tfw/README.md` | 1,548 | 1,548 | 0 | read-only source | PASS |
| English public + `.tfw/README.md` | 3,033 | 2,071 | -962 | hard ceiling 2,600 | PASS |

The preferred range is a drafting orientation, not a quota. EN is 27, RU 22, and KK 24 words below 550. All semantic, navigation, Edition, and three-case Quick Start units are present. The two independent critics specifically confirmed that adding words merely to reach 550 would repeat North Star, Editions, or Quick Start content. Retaining 523/528/526 avoids filler and preserves quality; no meaning was cut because the Task Board is long.

## Language switch, link, anchor, and command results

| Check | English | Russian | Kazakh |
|---|---:|---:|---:|
| Strict UTF-8 / replacement or mojibake count | PASS / 0 | PASS / 0 | PASS / 0 |
| Language switch is first visible block | PASS | PASS | PASS |
| Public links total / unique | 28 / 24 | 25 / 21 | 25 / 21 |
| Broken repository-local targets | 0 | 0 | 0 |
| `NS1`, `NS2`, `NS3` anchors | PASS | PASS | PASS |
| Task Board/history route | `#task-board` PASS | `README.md#task-board` PASS | `README.md#task-board` PASS |
| Light / Assisted / Full targets | PASS | PASS | PASS |
| `/tfw-plan`, `/tfw-handoff`, `/tfw-review` occurrences | 1 / 1 / 1 | 1 / 1 / 1 | 1 / 1 / 1 |
| Repository and MIT license routes | PASS | PASS | PASS |

The public scan covers all links created or retained in the onboarding surfaces, including logo and local directories. External repository/documentation/author URL strings are retained consistently; live HTTP availability was not claimed or tested.

## Editions and Quick Start fact check

| Unit | Checked fact | Result |
|---|---|---|
| Light | Resolves to `editions/01-light/`; manual Trace maintenance is acceptable | PASS |
| Assisted | Resolves to `editions/02-assisted/`; recurring/few-participant use, clearer responsibility/support, manual fallback; no durable automatic-dispatch claim | PASS |
| Full | Resolves to `.tfw/`; research/evidence/review/knowledge gates for higher-cost work | PASS |
| New project | Choose Edition, copy directory contents to project root, follow its README; Full points to Quick Start | PASS |
| Existing project | Preserve current files/Traces, inspect before structural change, choose migration/initialization route | PASS |
| Configured project | Read `AGENTS.md` and active Edition instructions, then use exact Full command sequence when applicable | PASS |

## Three-route walkthrough

| Language | Understand | Use | Audit | Result |
|---|---|---|---|---|
| English | `README.md` → `.tfw/README.md#ns1` / `#ns2` / `#ns3` | `README.md` → `editions/README.md` → `.tfw/quickstart.md` / `.tfw/conventions.md` | `README.md#task-board` → `tasks/` / `KNOWLEDGE.md` | PASS |
| Russian | `README.ru.md` → `.tfw/README.md#ns1` / `#ns2` / `#ns3` | `README.ru.md` → `editions/README.md` → `.tfw/quickstart.md` / `.tfw/conventions.md` | `README.ru.md` → English `README.md#task-board` → `tasks/` / `KNOWLEDGE.md` | PASS |
| Kazakh | `README.kk.md` → `.tfw/README.md#ns1` / `#ns2` / `#ns3` | `README.kk.md` → `editions/README.md` → `.tfw/quickstart.md` / `.tfw/conventions.md` | `README.kk.md` → English `README.md#task-board` → `tasks/` / `KNOWLEDGE.md` | PASS |

Repository, documentation, author, and MIT license remain directly discoverable. English explicitly designates the root doorway plus English Project North Star surface; RU/KK identify themselves as derived, independently written doorways.

## Task Board integrity

| Check | Result |
|---|---|
| `## Task Board` headings | English 1; Russian 0; Kazakh 0 — PASS |
| Localized task rows | Russian 0; Kazakh 0 — PASS |
| Approved baseline | `6ec4d6f763a3007e4b887cda80817bb8f8c7538b` |
| Comparison rule | Normalize line endings for comparison; compare from `## Task Board` through EOF after excluding only the complete TFW-55 row |
| Baseline tail SHA-256 | `a8c544a50cc3d098f3890bc6b8d6e26bb9d5a05c333a9eb64672d7aa44b4ecb6` |
| Final tail SHA-256 | `a8c544a50cc3d098f3890bc6b8d6e26bb9d5a05c333a9eb64672d7aa44b4ecb6` |
| Verdict | PASS — every non-TFW-55 board line is byte-identical after normalized line-ending comparison |

The missing TFW-55 Iteration 2 link target is a non-blocking baseline/shared-checkout observation. Per coordinator clarification, it is a pre-existing uncommitted research trace outside Phase B; the existing Task Board link and research artifacts were not changed or added. This known link is below the public onboarding boundary and does not affect the AC-5 public-direction scan or any word count.

## Subtraction ledger and old-claim dispositions

| Class | Baseline treatment | Final treatment | Disposition |
|---|---|---|---|
| Detailed audience cards | Three persona cards and explanatory copy | Removed | Authoritative meaning is role-agnostic; no replacement needed |
| FAQ and comparisons | Inline FAQ/comparison exposition | Removed | Concise non-goals and North Star links replace duplicate explanation |
| Lifecycle / status / How It Works | Detailed mechanics in root | Removed from doorway | Linked to `.tfw/conventions.md` and corpus |
| Root and `.tfw/` file inventories | Long inventories | Removed | Linked to Editions, Quick Start, `.tfw/`, and repository corpus |
| Tool adapter table | Detailed adapter list | Removed | Current mechanics remain in Full specification/conventions |
| Key Concepts glossary | Root-level glossary copy | Removed | Definition retained; detailed meaning linked to Project North Star |
| Update walkthrough | Root update instructions | Removed | Out of the public doorway; authoritative workflow remains elsewhere |
| Brand identity | Logo, name, brand line, badges/links | Retained compactly in English; logo/name/brand line localized | PASS |
| Continuity problem and TFW definition | Fragmented across old exposition | Retained and rewritten as one leading functional block | PASS |
| Editions and Quick Start | Retained but compressed | Linked and localized with factual next actions | PASS |
| Public navigation | Scattered links | Reorganized into understand/use/audit routes | PASS |
| Semantic authority notice | Not explicit in all languages | Added to all three; RU/KK yield to English | Funded inside compressed doorway |
| Language switch and RU/KK doorways | Absent | Added | Required Phase B localization scope; each independently bounded |

The English rewrite removes 962 words while adding the language/source notice inside the 523-word final surface. RU and KK are separate bounded doorway files, not duplications inside the English source. Across the three root onboarding surfaces, the final total is 1,577 words versus the old single-language 1,485 (+92) while access expands from one to three languages; the English semantic-source surface itself drops by 962 words. Task Board length is excluded and did not fund or force any content decision.

Old claim disposition:

| Old or risky claim class | Final disposition |
|---|---|
| Deterministic or identical reproduction | Explicitly disclaimed in all languages |
| Automatic truth | Explicitly disclaimed in all languages |
| Automatically self-maintaining documentation | Explicitly disclaimed in all languages |
| Same artifacts/lifecycle for every Edition | Removed; Editions are proportional realizations |
| Raw chat as durable memory | Removed; Trace is selected durable continuity |
| Agent authority merely from participation | Explicitly disclaimed; authority/accountability remains human/institutional |
| Component novelty / proprietary standard | Not claimed |
| Universal pedagogy, measured superiority, or adoption outcome | Not claimed |
| Durable automatic Assisted hook dispatch | Not claimed; manual fallback is stated |

## Provenance, scope, and consistency

| Check | Result |
|---|---|
| Reviewed `.tfw/README.md` blob | `71a4d725cff7d0d7508403589195e9f87a0fc49a` — PASS |
| Production files changed | Only `README.md`, `README.ru.md`, `README.kk.md` — PASS |
| Trace files added | Phase B ONB, this EV, two LANG_REVIEW reports, and RF only — in scope |
| Forbidden additions | No BoK, translation subsystem, glossary/specification edit, public roadmap, canon manifest, visual asset, or research artifact |
| Markdown whitespace/errors | `git diff --check` PASS |
| Placeholder scan | PASS at evidence gate; final EV/RF consistency scan repeats before commit |
| Scope budget | 8 modified/created files at planned completion; 7 new; far below 30 files / 15 new / 3,000 LOC |

Execution chain before RF:

- `328e6b4` — executor ONB and normal TFW-55 board transition;
- `437f7a9` — frozen multilingual draft used by both initial critics;
- `caee273` — localization finding closure used by both final rechecks.

## Verdict

Evidence verdict: **0/10 VERIFIED, 0 DEFERRED, 0 BLOCKED, 10 N/A**

All ten repository-local document gates pass. The N/A classification follows the approved TS evidence declarations and does not mean the gates were skipped.

---

*EV — TFW-55 / Phase B: Multilingual public entry | 2026-08-26*
