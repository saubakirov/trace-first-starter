# TS — TFW-55 / Phase B: Multilingual Public Entry

> **Date**: 2026-08-26
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — approved by the owner 2026-08-26; ready for `/tfw-handoff`
> **Parent HL**: [HL-TFW-55](../HL-TFW-55__canonization_program.md)
> **Phase HL**: [Phase B derivation](HL__phase-b__multilingual_public_entry.md)
> **Phase A source**: [RF](../phase-a/RF__phase-a__canonical_foundation_essay.md) · [REVIEW](../phase-a/REVIEW__phase-a__canonical_foundation_essay.md) · [Project North Star](../../../.tfw/README.md)
> **Master freeze**: `a60bc6d`

---

## 1. Objective

Turn the repository root into a concise multilingual doorway without creating a second philosophy. English `README.md` remains the semantic source and the only Task Board; new `README.ru.md` and `README.kk.md` provide natural Russian and Kazakh localizations rather than literal translations. Each version must explain enough to understand TFW, choose an Edition, begin work, and find authoritative meaning/history in no more than 800 public-onboarding words.

## 2. Scope

### In Scope

- Replace the 1,485-word English public section above `## Task Board` with a ≤800-word doorway derived from the reviewed Project North Star.
- Create root-level Russian and Kazakh localizations, each independently composed in natural target-language prose, ≤800 words, and without Task Boards.
- Make the same working `English · Русский · Қазақша` switch the first visible block in all three files.
- Preserve one definition, proportional Editions selection, compact Quick Start, license/repository links, and understand/use/audit navigation in every language.
- Make `NS1`, `NS2`, and `NS3` directly discoverable from the English root and semantically represented in both localizations.
- Remove duplicated philosophy, comparison, audience-card, FAQ, lifecycle, inventory, adapter, and update prose when authoritative linked material already owns it.
- Run separate Russian and Kazakh naturalness/calque critiques and preserve their complete structured reports as dedicated evidence files, with the parity matrix, word/link checks, and subtraction ledger in EV/RF.

### Out of Scope

- Any edit to `.tfw/README.md`, Project North Star semantics, conventions, glossary, workflows, templates, Editions behavior/content, adapters, configuration, or runtime.
- A full Russian/Kazakh translation of the Project North Star, specification, Task Board, task traces, or knowledge base.
- BoK creation, book/guide/course content, university packaging, market/legal research, visual rebrand, documentation-site redesign, or launch work.
- Proof of human comprehension, learning, adoption, or localization reception outside the bounded language critiques.

## 3. Principles Check

| # | Principle from master HL §7 | Enforced by | Gate |
|---|---|---|---|
| P1 | One North Star, several depths | AC-1, AC-4, AC-7 | Doorways link to North Star/mechanics/corpus and do not restate them as competing authority |
| P2 | Philosophy before machinery | AC-1–AC-3 | Problem and definition precede Editions and Quick Start in every language |
| P3 | Human purpose remains human | AC-4 | Six semantic invariants preserve authority/accountability boundaries |
| P4 | Trace, not transcript | AC-4 | Localization matrix rejects chat/archive/determinism drift |
| P5 | Self-awareness must be operational | AC-4 | Doorways omit the term or preserve its bounded capability; no anthropomorphic shorthand |
| P6 | Subtract before adding | AC-8 | Fixed word ceilings, combined ceiling, and content disposition ledger |
| P7 | Provenance before polish | AC-4, AC-9 | English source declaration, parity matrix, language reports, and claim dispositions |
| P8 | Experience reveals the system | AC-6 | Editions are proportional and solve visible work/risk needs, not a maturity badge |
| P9 | Refutation before canonicalization | AC-4, AC-9 | Language reviewers actively search for missing/extra promises and source drift |

## 4. Affected Files

| File | Action | Description |
|---|---|---|
| `README.md` | MODIFY | English doorway above the existing Task Board; Task Board remains English-only |
| `README.ru.md` | CREATE | Derived Russian public doorway; no Task Board |
| `README.kk.md` | CREATE | Derived Kazakh public doorway; no Task Board |
| `phase-b/evidence/EV__phase-b__multilingual_public_entry.md` | CREATE | Per-AC evidence, parity/terminology matrices, language critiques, word/link/board/subtraction checks |
| `phase-b/evidence/LANG_REVIEW__phase-b__ru.md` | CREATE | Separate final Russian naturalness, calque, independence, and semantic-equivalence report |
| `phase-b/evidence/LANG_REVIEW__phase-b__kk.md` | CREATE | Separate final Kazakh naturalness, calque, independence, and semantic-equivalence report |

**Budget:** 6 delivery/evidence files; 5 new; 1 production modification; estimated ≤900 changed lines. The mandatory ONB and RF add two normal phase traces, for 8 execution-stage files total (7 new, 1 modified). Within configured limits: 30 files, 15 new files, 3,000 LOC, 30 modified files.

## 5. Acceptance Criteria

### AC-1: English doorway replaces duplicate exposition

English `README.md` becomes a small entry point to the reviewed North Star rather than a second essay.

- [ ] The public section begins with the language switch/source notice, existing brand identity, a concrete continuity problem, and one functional TFW definition before machinery.
- [ ] The definition preserves Philosophy of Trace → TFW methodology → proportional realizations and the human/agent authority boundary.
- [ ] Direct links expose `NS1 — Purpose`, `NS2 — Principles`, and `NS3 — Non-goals` in `.tfw/README.md`.
- [ ] Detailed audience cards, FAQ, comparisons, lifecycle/status explanation, file inventories, adapter tables, and update walkthrough are removed or represented only by authoritative links.
- [ ] No deterministic, automatically self-documenting, same-artifact, raw-chat-memory, agent-authority, or component-novelty claim remains.

Gate: Manual semantic/role inspection plus required old-content disposition ledger in EV.

Evidence: N/A — this is a repository-local document transformation with no live-environment behavior claim.

### AC-2: Russian doorway is a natural, usable localization [depends: AC-1]

`README.ru.md` communicates the English doorway naturally in Russian without becoming an independent source of TFW meaning or sounding like English syntax rendered word for word.

- [ ] It carries every required semantic, Editions, Quick Start, navigation, source, repository, and license unit from the English doorway.
- [ ] It declares that English `README.md` and the English Project North Star are the semantic source.
- [ ] TFW, Trace-First Workflow, Edition names, commands, anchors, and paths remain unchanged; localized concepts follow the terminology contract.
- [ ] It introduces no new promise, authority rule, capability, product scope, or interpretation.
- [ ] Its paragraph order and phrasing are chosen for Russian clarity; it contains no material calque, mechanical mirroring, or translation smell and may reuse natural Russian formulations derived from `.tfw/README.md` semantics.
- [ ] It contains no Task Board, task-status table, or translated operational project state.
- [ ] It is valid UTF-8 with no replacement characters or mojibake.

Gate: Semantic-unit parity matrix plus fresh isolated Russian critique under AC-9.

Evidence: N/A — language quality is captured by bounded document critique in EV, not a live user study.

### AC-3: Kazakh doorway is a natural, usable localization [depends: AC-1]

`README.kk.md` communicates the English doorway naturally in Kazakh without literal-calque drift or independent authority.

- [ ] It carries every required semantic, Editions, Quick Start, navigation, source, repository, and license unit from the English doorway.
- [ ] It declares that English `README.md` and the English Project North Star are the semantic source.
- [ ] TFW, Trace-First Workflow, Edition names, commands, anchors, and paths remain unchanged; localized concepts follow the terminology contract.
- [ ] It introduces no new promise, authority rule, capability, product scope, or interpretation.
- [ ] Its paragraph order and phrasing are chosen for Kazakh clarity; it contains no material calque, mechanical mirroring, or translation smell and may reuse natural Kazakh formulations derived from `.tfw/README.md` semantics.
- [ ] It contains no Task Board, task-status table, or translated operational project state.
- [ ] It is valid UTF-8 with no replacement characters or mojibake.

Gate: Semantic-unit parity matrix, terminology/back-translation inspection, and fresh isolated Kazakh critique under AC-9.

Evidence: N/A — language quality is captured by bounded document critique in EV, not a live user study.

### AC-4: Semantic parity and authority remain explicit [depends: AC-1, AC-2, AC-3]

All three doorways preserve the same six invariants while allowing natural language-specific structure.

- [ ] EV maps each invariant to exact sections in English, Russian, and Kazakh.
- [ ] Human purpose, legitimate authority, judgment, acceptance, accountability, and stop responsibility remain human/institutional in all versions.
- [ ] Trace remains selected durable continuity, not transcript, hidden reasoning, automatic truth, or deterministic reproduction.
- [ ] If “self-aware project” appears, it is operationally bounded; omission from the short doorway is allowed.
- [ ] English is identified as the semantic source; localizations explicitly yield on conflict.
- [ ] The root documents point to the existing North Star and do not create another canon, BoK, or governance surface.
- [ ] Semantic units are equivalent, but paragraph counts, sentence order, and local phrasing are not required to mirror English.

Gate: Three-column invariant/authority matrix in EV; zero missing units and zero contradictory/extra claims.

Evidence: N/A — parity is directly inspectable in versioned files.

### AC-5: Language switch and local links work everywhere [depends: AC-1, AC-2, AC-3]

A visitor can change language without searching, and every repository-local destination resolves.

- [ ] `English · Русский · Қазақша` is the first visible block in all three files with correct relative targets.
- [ ] All three files link to Project North Star, Editions, Quick Start, Task Board/history route, repository, and license as applicable.
- [ ] Russian and Kazakh audit links lead to the English Task Board/corpus rather than duplicating operational state.
- [ ] Every local file/directory link and every required `#ns1`/`#ns2`/`#ns3` anchor resolves.
- [ ] Commands, paths, URLs, and Markdown link destinations are byte-identical across languages where they represent the same destination.

Gate: Automated local link/anchor/target comparison with results recorded in EV.

Evidence: N/A — link resolution is a reproducible local check.

### AC-6: Editions and Quick Start remain factual and usable

Simplification must not make current use harder to discover or reintroduce unsupported capability claims.

- [ ] Light points to `editions/01-light/`, Assisted to `editions/02-assisted/`, and Full to `.tfw/`/the Full workflow route.
- [ ] Each Edition is explained by work complexity/risk and availability, not prestige or universal maturity.
- [ ] Assisted does not promise durable automatic hook dispatch or measured superiority over Light.
- [ ] Each language gives usable first actions for a new project, an existing project, and an already-configured project, or one equally functional compact sequence.
- [ ] `/tfw-plan` and other exact commands/paths are never translated or altered.

Gate: Check every Edition/path/command against current `editions/README.md`, `.tfw/quickstart.md`, and D57–D60; run a cold navigation inspection from each doorway.

Evidence: N/A — no installation is performed; current documentation facts and navigation are verified locally.

### AC-7: Three navigation routes and public essentials are visible

Every doorway answers where to go next without reproducing the destination.

- [ ] **Understand:** direct Project North Star/definition/purpose route.
- [ ] **Use:** Editions selection and Quick Start route.
- [ ] **Audit:** English Task Board, task traces/knowledge, or equivalent history/evidence route.
- [ ] Repository, author/attribution where retained, version where retained, and MIT license remain discoverable.
- [ ] The English root visibly completes the root + `.tfw/README.md` Project North Star designation; Russian/Kazakh identify themselves as derived doorways.

Gate: Three-route walkthrough for each language in EV, with exact click sequence and destination.

Evidence: N/A — navigation paths are repository-local and directly inspectable.

### AC-8: Budgets, subtraction, and Task Board integrity hold

The new entry is smaller, not a multilingual duplication of the old information architecture.

- [ ] English public content before `## Task Board` is ≤800 whitespace-delimited words; `## Task Board` and the entire section after it are excluded from this metric.
- [ ] Entire `README.ru.md` and `README.kk.md` are each ≤800 whitespace-delimited words.
- [ ] English public content plus `.tfw/README.md` is ≤2,600 words; measured before/final/net counts are recorded.
- [ ] English `README.md` contains exactly one `## Task Board`; Russian and Kazakh contain zero Task Board headings/rows.
- [ ] From the approved Phase B TS baseline, all English Task Board lines except the normal TFW-55 status row remain byte-identical.
- [ ] EV records removed, linked, retained, localized, and newly added content classes; added language/source text is funded by subtraction, while Task Board length has no effect on the onboarding budget or content cuts.

Gate: Reproducible raw-Markdown word counts, heading/row counts, board-tail comparison excluding only the TFW-55 row, and subtraction ledger in EV.

Evidence: N/A — size and board integrity are deterministic file checks.

### AC-9: Independent language critiques close material defects [depends: AC-2, AC-3, AC-4]

Russian and Kazakh receive separate fresh critiques before RF; the executor may not self-certify both localizations.

- [ ] Each critique receives only its frozen semantic packet, the English doorway, target localization, and fixed rubric—no founder intent or preferred verdict.
- [ ] Each reports invariant coverage, drift, missing/extra promise, authority, terminology, target-language naturalness, English-syntax calques, translation smell, independent-localization quality, command/path integrity, and severity.
- [ ] The Russian reviewer provides an English back-translation of the definition; the Kazakh reviewer provides both English and Russian back-translations of the definition for triangulation.
- [ ] Every high-severity semantic, factual, authority, navigation, or serious-idiom defect is corrected and rechecked before RF.
- [ ] Pure stylistic preference without material meaning/usability impact is recorded as non-blocking and does not trigger repeated revision.
- [ ] `evidence/LANG_REVIEW__phase-b__ru.md` and `evidence/LANG_REVIEW__phase-b__kk.md` preserve the complete final structured reports; EV links them, records executor dispositions, and confirms zero unresolved high-severity defects.

Gate: Validate reviewer isolation packet, required report fields, disposition table, and final severity counts in EV.

Evidence: N/A — these are bounded language/document critiques, not evidence of population-level reception.

### AC-10: Provenance and scope are reviewable

The normal Phase B trace explains the rewrite without creating a public localization registry.

- [ ] EV maps AC-1–AC-10 to exact files/sections and verification results.
- [ ] RF records semantic source, terminology decisions, old-content dispositions, word counts, link results, board integrity, language reports, and unresolved non-blocking risks.
- [ ] No production file outside the three root READMEs is changed.
- [ ] `.tfw/README.md` remains byte-identical to the Phase A reviewed blob `71a4d725cff7d0d7508403589195e9f87a0fc49a`.
- [ ] No BoK, translation subsystem, glossary/specification change, public roadmap, or canon manifest is created.
- [ ] EV and RF contain no placeholders and agree on every count/verdict before handoff to review.

Gate: Path-scope diff, reviewed-blob comparison, placeholder scan, and EV↔RF consistency check.

Evidence: N/A — provenance and scope are established by repository traces and hashes.

### Evidence Artifact

| File | Description |
|---|---|
| `phase-b/evidence/EV__phase-b__multilingual_public_entry.md` | Required structured evidence: per-AC verdicts, invariant/terminology matrices, Russian/Kazakh critique reports and dispositions, word/link/anchor/board checks, navigation routes, and subtraction ledger |
| `phase-b/evidence/LANG_REVIEW__phase-b__ru.md` | Separate Russian naturalness/calque/independence and semantic-equivalence report against the final file |
| `phase-b/evidence/LANG_REVIEW__phase-b__kk.md` | Separate Kazakh naturalness/calque/independence and semantic-equivalence report against the final file |

## 6. Technical Guidance

### Source order

Executor reads only the sources needed for the doorway, in this order:

1. Master HL §§1, 3–7 and Amendments A2–A5.
2. [Phase B HL](HL__phase-b__multilingual_public_entry.md).
3. Reviewed [`.tfw/README.md`](../../../.tfw/README.md), especially the definition, proportional realizations, `NS1`–`NS3`, and authority routing.
4. Phase A RF and REVIEW for evidence limits and non-blocking root-alignment findings.
5. Current `README.md` public section for subtraction and working links.
6. `editions/README.md`, `.tfw/quickstart.md`, `LICENSE`, and current edition paths only to verify usage facts.

### Semantic packet

The fixed semantic packet used for both localizations and language critiques contains:

- the final English doorway;
- the relevant definition, Trace, human-authority, proportional-realization, and `NS1`–`NS3` passages from the approved `.tfw/README.md`, which may supply natural formulations without becoming a second semantic source;
- the six semantic invariants in the Phase HL;
- the terminology contract;
- the required navigation/Quick Start units;
- explicit exclusions: no extra promise, authority, maturity claim, automation claim, or Task Board.

### Implementation guidance

- Rewrite the English public section as a unit; do not preserve its current heading structure merely because it exists.
- Treat the current Task Board marker as a hard boundary. Capture the approved TS-baseline board tail before editing; later comparisons may ignore only the TFW-55 row used for normal status transitions.
- Raw word-count convention: count whitespace-delimited non-empty tokens in Markdown source. English count stops immediately before `## Task Board`, excluding the heading and every Task Board line; Russian/Kazakh count the whole file; `.tfw/README.md` counts the whole file. Never trade away required onboarding meaning because the operational board is long.
- Keep the existing logo and calm protocol-grade identity where they fit inside the budget; do not create or edit visual assets.
- Preserve brand/code identifiers exactly: `Trace-First Workflow`, `TFW`, Light/Assisted/Full, `/tfw-*`, paths, URLs, `NS1`–`NS3`.
- Write and validate all three READMEs as strict UTF-8; fail on replacement characters or common mojibake sequences.
- Localization topology should differ when natural target-language composition benefits. Semantic-unit parity is mandatory; sentence-by-sentence, paragraph-by-paragraph, and syntax mirroring are not.
- Natural formulations and explanatory moves from the approved `.tfw/README.md` are allowed and encouraged when they improve Russian or Kazakh without changing the English public contract.
- Use two fresh isolated Codex tasks or equivalent bounded reviewers for the language critiques. They critique; they do not edit production files or issue the formal TFW REVIEW verdict.
- A language concern blocks only when it materially changes meaning, authority, factual accuracy, navigation, or ordinary comprehension. Record tasteful alternatives without cycling.
- Do not edit a linked source to make a doorway sentence true. Correct the doorway or record a future finding.

## 7. Definition of Failure

- ❌ Any doorway exceeds 800 words or combined English explanatory content exceeds 2,600.
- ❌ Russian/Kazakh adds meaning, authority, promises, capabilities, or operational state absent from English.
- ❌ English loses the Task Board, another file gains a Task Board, or a non-TFW-55 Task Board line changes.
- ❌ Language switch, required local links, `NS1`–`NS3`, Editions paths, commands, or license navigation break.
- ❌ The doorway again claims deterministic reproduction, automatic self-documentation, same artifacts/lifecycle, agent authority/accountability, universal pedagogy, or untested capability.
- ❌ Russian or Kazakh has an unresolved high-severity language/meaning defect, reads as materially calqued/mechanically mirrored English, or lacks its separate final critique report.
- ❌ Quick Start becomes too abstract to give a new, existing, or configured project a usable next action.
- ❌ `.tfw/README.md`, framework mechanics, Editions content, visual identity assets, BoK, book/course/guide, or documentation site changes enter the phase.
- ❌ EV/RF omits a required matrix/report/count/disposition, contains placeholders, or reports inconsistent results.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| English compression becomes generic marketing | Six invariant checks, North Star direct links, and removal/retention ledger |
| Russian source familiarity silently overrides English | Explicit source declaration and three-column parity matrix |
| Kazakh reviewer produces fluent but semantically shifted text | Definition back-translation, terminology probes, and authority/promise rubric |
| Reviewer cycles on stylistic taste | Materiality rule and severity classification; only high-severity defects block |
| Task Board changes during concurrent work | Compare all board lines except the TFW-55 workflow row rather than relying on one whole-file hash |
| Public usage facts go stale during rewrite | Read current Editions/Quick Start immediately before drafting and verify paths/commands in RF |

## 9. Cross-Phase Modifications

| File | Also involved in | Coordination note |
|---|---|---|
| `README.md` | Phase A control trace | Phase A changed only the TFW-55 Task Board row; Phase B owns public prose and must preserve the rest of the board |
| `.tfw/README.md` | Phase A production result | Read-only semantic source in Phase B; reviewed blob must remain unchanged |

---

*TS — TFW-55 / Phase B: Multilingual Public Entry | 2026-08-26*
