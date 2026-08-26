# TS — TFW-55 / Phase B.2: Restore and Localize the Project README

> **Date**: 2026-08-26
> **Author**: Coordinator
> **Status**: ✅ APPROVED — owner 2026-08-26
> **Parent HL**: [HL-TFW-55](../HL-TFW-55__canonization_program.md)
> **Phase HL**: [Phase B.2 HL](HL__phase-b2__project_readme_localization.md)
> **Contract baseline**: `5dee93d` — Amendment A6 supersedes the compact-doorway contract
> **Production baseline**: public prefix of `b924926:README.md`; live Task Board tail from the Executor start commit

---

## 1. Objective

Restore the practical project-guide function of the root README from exact pre-Phase-B baseline `b924926`, apply only minimal factual and Philosophy-of-Trace alignment, and create complete natural Russian and Kazakh localizations of that restored README. Preserve the current English Task Board and the superseded Phase B trace. The result must help a newcomer understand the project, choose an Edition, install or initialize it, start with an exact command, inspect repository structure and workflow, and reach philosophy, mechanics, and history without turning the README into a paraphrase of `.tfw/README.md`.

## 2. Scope

### In Scope

- replace only the current English public prefix before `## Task Board` with the ledgered, minimally updated `b924926` practical README;
- preserve the live Task Board tail from the Phase B.2 execution baseline, allowing only normal TFW-55 row transitions;
- replace `README.ru.md` and `README.kk.md` with natural full-function localizations of the restored English project README, without Task Boards;
- add/retain a visible three-language switch and English semantic-source notice;
- verify current Editions, Quick Start, commands, file structure, adapters, lifecycle, updating, links, attribution, and license facts;
- correct unsupported philosophy/authority claims only where the baseline conflicts with the reviewed North Star;
- create new Phase B.2 ONB, EV, RU/KK language reports, and RF; preserve all old Phase B artifacts unchanged;
- make the prior contract failure explicit and leave D66 correction to post-APPROVE `/tfw-docs`.

### Out of Scope

- any modification to `.tfw/README.md`, framework mechanics, conventions, glossary, workflows, templates, Editions content, adapters, runtime, config, docs site, or visual assets;
- a translation or rewrite of the Project North Star essay;
- BoK, book, guide, course, certification, marketing, launch, or user research;
- rollback of Task Board state, TFW-60, TFW-54, research files, or other parallel work;
- deletion or rewriting of the superseded Phase B ONB/RF/EV/LANG_REVIEW/REVIEW chain;
- a new word ceiling, compression ratio, or preferred word band.

## 3. Principles Check

| # | Principle (master HL §7) | Enforced by | Gate |
|---|---|---|---|
| P1 | One North Star, several depths | AC-2, AC-3 | README performs practical work and links to the essay for philosophical depth |
| P2 | Philosophy before machinery | AC-3 | Opening preserves the continuity problem and correct functional definition before repository mechanics |
| P3 | Human purpose remains human | AC-3, AC-5, AC-6 | Authority wording is mapped in EN/RU/KK and critics check drift |
| P4 | Trace, not transcript | AC-3 | Unsupported transcript/determinism/automatic-memory claims are removed or qualified |
| P5 | Self-awareness must be operational | AC-3, AC-4 | Any self-aware-project wording remains tied to inspectable project capabilities |
| P6 | Function before compression | AC-1, AC-2 | Keep-by-default ledger and newcomer walkthrough; no word target may remove a function |
| P7 | Provenance before polish | AC-1, AC-7, AC-9 | Exact baseline/hash, update reasons, critic reports, and old-chain supersession remain visible |
| P8 | Experience reveals the system | AC-2, AC-4 | Audience, Editions, Quick Start, structure, and workflow remain problem-led and actionable |
| P9 | Refutation before canonicalization | AC-7, AC-9 | Critics search for missing functions and the formal Reviewer checks against owner rejection, not old APPROVE |

## 4. Affected Files

| File | Action | Description |
|---|---|---|
| `README.md` | MODIFY | Restore/minimally align the practical English public prefix; preserve current Task Board tail |
| `README.ru.md` | MODIFY | Replace short doorway with natural Russian localization of the practical README; no board |
| `README.kk.md` | MODIFY | Replace short doorway with natural Kazakh localization of the practical README; no board |
| `phase-b/ONB__phase-b2__project_readme_localization.md` | CREATE | Corrective Executor onboarding, baseline/tail capture, scope, and risks |
| `phase-b/evidence/EV__phase-b2__project_readme_localization.md` | CREATE | Per-AC results, ledger, functional/localization matrices, navigation and board checks |
| `phase-b/evidence/LANG_REVIEW__phase-b2__ru.md` | CREATE | Russian draft and exact-final critic reports plus dispositions |
| `phase-b/evidence/LANG_REVIEW__phase-b2__kk.md` | CREATE | Kazakh draft and exact-final critic reports plus dispositions |
| `phase-b/RF__phase-b2__project_readme_localization.md` | CREATE | Corrective result, verification, provenance, limitations, and supersession record |

**Budget:** 8 execution-stage files total; 5 new, 3 modified. Estimated ≤1,800 changed lines, within configured limits of 30 files, 15 new files, 3,000 LOC, and 30 modified files. Old Phase B artifacts are read-only and do not enter the diff.

## 5. Acceptance Criteria

### AC-1: Exact baseline and disposition ledger govern restoration

The English practical content starts from the public prefix of `b924926:README.md`, not from the rejected 523-word result.

- [ ] Executor reproduces the baseline prefix at 1,485 whitespace-delimited words and SHA-256 `d14f9b89b174a59f8cd3177dfd111147ec2efdfcb3254fd3790788896b11638d`.
- [ ] EV contains a section-level keep/update/add/remove ledger covering every baseline heading and the unsupported claim class.
- [ ] Every practical baseline section is retained unless EV names a concrete functional reason for an equivalent consolidation or removal.
- [ ] Every changed English claim is mapped to one of: factual correction, authority correction, stale navigation, current Edition/command/path fact, or minimal philosophy alignment.
- [ ] Current Task Board tail is captured from the Executor start commit and is never sourced from `b924926`.

Gate: Baseline hash/word reproduction; heading-to-ledger completeness; prefix diff classified line by line or block by block; separate current-tail hash.

Evidence: N/A — the baseline and transformations are directly inspectable Git/document facts.

### AC-2: English README performs the practical project-guide job [depends: AC-1]

The restored English README helps a newcomer understand and use this repository without opening the essay first.

- [ ] It explains what TFW and this repository are, the continuity problem they address, and who benefits.
- [ ] It preserves recognizable guidance for product leaders, analysts/researchers, engineers, and non-code work.
- [ ] It lets the reader choose Light, Assisted, or Full by work shape/risk and follow current links.
- [ ] It provides usable, copyable starts for a new project, an existing project, and an already configured project.
- [ ] It shows exact workflow commands, repository/root structure, `.tfw/` structure, adapters, key concepts/lifecycle, updating, and public links.
- [ ] It routes separately to philosophy, mechanics, documentation/help, history/evidence, repository, author, and license.
- [ ] No acceptance check depends on a word ceiling or compression target; descriptive counts are recorded only for provenance.

Gate: Cold newcomer walkthrough answering the seven Phase HL questions with exact README locations and click/action sequences; baseline functional-block matrix has no unjustified gap.

Evidence: N/A — repository navigation and instructions are directly inspectable; no population-level comprehension claim is made.

### AC-3: Philosophy alignment is minimal and correct [depends: AC-1]

The README agrees with the reviewed North Star without retelling it.

- [ ] TFW is described as a methodology for joint human–AI work, grounded in the Philosophy of Trace.
- [ ] Human purpose, legitimate authority, judgment, acceptance, accountability, and stop responsibility remain explicit; agents perform bounded work.
- [ ] Trace is selected durable continuity, not raw chat, hidden reasoning, guaranteed reproduction, automatic truth, or self-maintaining documentation.
- [ ] Unsupported baseline claims such as automatic capture, replacement of documentation, decisions documenting themselves, or independent agent authority are removed or bounded.
- [ ] The README links to `.tfw/README.md` for the full argument and does not reproduce the essay's principle/non-goal exposition.
- [ ] Any “self-aware product/project” wording is tied to inspectable capabilities, not anthropomorphism.

Gate: Claim-change ledger against `b924926`, invariant inspection against reviewed `.tfw/README.md`, and explicit anti-paraphrase review.

Evidence: N/A — semantic consistency is directly inspectable in versioned text.

### AC-4: Editions, starts, mechanics, and links are current [depends: AC-2]

Practical material is preserved accurately rather than copied blindly from the old README.

- [ ] Light, Assisted, and Full descriptions and destinations match current `editions/README.md`; Assisted makes no unsupported automation guarantee.
- [ ] New/existing/configured project instructions match current Edition and `.tfw/quickstart.md` routes.
- [ ] `/tfw-plan`, `/tfw-handoff`, `/tfw-review`, `/tfw-resume`, and other retained commands remain exact and factually placed.
- [ ] Root file, `.tfw/`, adapter, lifecycle/status, version, update, documentation, repository, author, and license entries resolve and match current sources.
- [ ] External URLs are preserved or intentionally updated with a recorded reason; live availability is not claimed unless checked.

Gate: Source-by-source fact table and automated local target/anchor check; exact command/path comparison; external URL string ledger.

Evidence: N/A — current repository facts and local navigation are deterministic checks.

### AC-5: Russian is a full, natural localization [depends: AC-2, AC-3, AC-4]

`README.ru.md` localizes the practical English README rather than summarizing the essay or shortening the project guide.

- [ ] Functional parity covers every keep/update/add block and all seven newcomer questions.
- [ ] Commands, paths, URLs, Edition names, identifiers, and destinations remain exact.
- [ ] The file declares English as semantic source, links to the canonical essay, and contains no Task Board or operational project state.
- [ ] Russian syntax, paragraphing, terminology, and tone are idiomatic; material calque, mirrored English construction, and translation smell are absent.
- [ ] No new promise, authority, capability, project scope, or philosophical claim appears.
- [ ] Strict UTF-8 passes with no replacement characters or mojibake.

Gate: English↔Russian functional/semantic matrix plus isolated Russian critic and exact-final recheck under AC-7.

Evidence: N/A — language review is a bounded document critique, not human reception evidence.

### AC-6: Kazakh is a full, natural localization [depends: AC-2, AC-3, AC-4]

`README.kk.md` localizes the practical English README rather than summarizing the essay or shortening the project guide.

- [ ] Functional parity covers every keep/update/add block and all seven newcomer questions.
- [ ] Commands, paths, URLs, Edition names, identifiers, and destinations remain exact.
- [ ] The file declares English as semantic source, links to the canonical essay, and contains no Task Board or operational project state.
- [ ] Kazakh syntax, paragraphing, terminology, and tone are idiomatic; material calque, mirrored English/Russian construction, and translation smell are absent.
- [ ] No new promise, authority, capability, project scope, or philosophical claim appears.
- [ ] Strict UTF-8 passes with no replacement characters or mojibake.

Gate: English↔Kazakh functional/semantic matrix, definition back-translation, isolated Kazakh critic, and exact-final recheck under AC-7.

Evidence: N/A — language review is a bounded document critique, not human reception evidence.

### AC-7: Independent language critics close material defects [depends: AC-5, AC-6]

The Executor may not self-certify both full localizations.

- [ ] Separate isolated RU and KK critic tasks receive the exact English production source, target localization, baseline functional ledger, minimal semantic invariants, current fact packet, and fixed materiality rubric.
- [ ] Each critic checks missing practical functions, semantic/factual/authority drift, navigation, commands/paths, naturalness, calque, translation smell, and whether the target reads as a complete project README.
- [ ] RU supplies English back-translation of the definition; KK supplies English and Russian back-translations.
- [ ] Every HIGH finding is corrected and the exact final commit is rechecked; unresolved HIGH must be zero in both reports.
- [ ] Taste-only alternatives are recorded as non-blocking and do not cause an endless loop.
- [ ] New Phase B.2 reports preserve draft/final commits and blobs, all findings, dispositions, and final counts without overwriting the old reports.

Gate: Critic packet/hash audit, required-field scan, disposition table, exact-final lineage, and `unresolved HIGH=0` in both reports.

Evidence: N/A — critic reports are repository document evidence, not a population-level language study.

### AC-8: Language switch, Task Board, encoding, and scope remain intact [depends: AC-2, AC-5, AC-6]

Restoration changes the public prefix without rolling back project state.

- [ ] `English · Русский · Қазақша` is visible near the top of all three files with correct relative targets.
- [ ] English contains exactly one `## Task Board`; RU and KK contain zero Task Board headings/rows.
- [ ] From the Phase B.2 Executor start commit, every Task Board line except the normal TFW-55 row is byte-identical after execution; TFW-60 and parallel state are preserved.
- [ ] All three files pass strict UTF-8, Markdown/local-link/anchor checks, and command/path destination parity.
- [ ] `.tfw/README.md` remains exact reviewed blob `71a4d725cff7d0d7508403589195e9f87a0fc49a`.
- [ ] Production diff is limited to the three root READMEs; old Phase B traces are unchanged.

Gate: Prefix/tail split checks, board-tail comparison excluding only TFW-55 row, UTF-8/mojibake scan, link/anchor/command checks, blob and path-scope diff.

Evidence: N/A — integrity and scope are deterministic repository checks.

### AC-9: Corrective provenance is explicit and reviewable [depends: AC-1, AC-7, AC-8]

The new trace explains why a technically approved result was still wrong for the owner.

- [ ] ONB, EV, and RF identify `b924926` as production baseline and `5dee93d` as the amended contract baseline.
- [ ] RF names the old Phase B RF/REVIEW and records that REVIEW APPROVE was superseded by owner rejection because it verified the wrong README function.
- [ ] RF includes the complete ledger, descriptive counts, newcomer walkthrough, fact/link checks, critic dispositions, board integrity, scope, and residual limits.
- [ ] EV maps every AC to exact files/sections/commands and agrees with RF; both contain no placeholders.
- [ ] No BoK or unrelated product/process change enters execution.
- [ ] RF flags stale D66/KNOWLEDGE for mandatory post-APPROVE `/tfw-docs`, but does not edit KNOWLEDGE under Executor role.

Gate: Artifact completeness, placeholder scan, EV↔RF consistency, superseded-chain references, scope diff, and post-review docs marker.

Evidence: N/A — provenance is established by Git and TFW artifacts.

### Evidence Artifacts

| File | Description |
|---|---|
| `phase-b/evidence/EV__phase-b2__project_readme_localization.md` | Per-AC verdicts, exact baseline/tail checks, keep/update/add/remove ledger, functional and semantic matrices, newcomer walkthroughs, fact/navigation/scope checks |
| `phase-b/evidence/LANG_REVIEW__phase-b2__ru.md` | Complete Russian draft/final critique chain, dispositions, back-translation, and final severity |
| `phase-b/evidence/LANG_REVIEW__phase-b2__kk.md` | Complete Kazakh draft/final critique chain, dispositions, English/Russian back-translations, and final severity |

## 6. Technical Guidance

### Source order

1. Master HL at freeze `5dee93d`, especially A6, §§1, 3–7.
2. This Phase B.2 HL and TS.
3. `b924926:README.md` public prefix through the line immediately before `## Task Board`.
4. Phase A RF/REVIEW and reviewed `.tfw/README.md` only for minimal definition/authority/non-goal alignment.
5. Current `editions/README.md`, `.tfw/quickstart.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, adapter paths, `LICENSE`, and `.tfw/VERSION` for factual checks.
6. Superseded Phase B RF/REVIEW only to understand the failure and avoid repeating it.

### Reconstruction boundary

- Treat the English file as two regions: **public prefix** and **live Task Board tail**.
- Recover the old prefix from `git show b924926:README.md`; capture the current tail from the Executor start commit.
- Never restore the whole old `README.md`, run a whole-file checkout, or use the old Task Board.
- Compare the final tail to the start commit while excluding only the TFW-55 row used for normal status transitions.
- Word counts stop before `## Task Board` only to keep measurements comparable; they are not pass/fail gates.

### Editorial boundary

- Preserve sections before polishing sentences. The ledger decides document topology; sentence editing cannot silently delete a function.
- Minimal philosophy alignment means replacing false/unsupported claims and adding the correct one-paragraph definition/authority link, not importing `.tfw/README.md` structure or prose.
- Use current linked sources to correct facts. Do not edit those sources to make old README wording true.
- Keep brand identifiers, Edition names, commands, paths, anchors, URLs, lifecycle tokens, and file names exact.
- Localizations may restructure within a section for natural reading but must map every practical function and destination.

### Critic packet

Each critic receives a frozen packet containing the final English README prefix, target localization, the Phase HL ledger and seven newcomer questions, AC-3 semantic minimum, AC-4 fact table, exact command/path/URL set, and severity boundary. Critics do not edit production and do not issue formal TFW REVIEW. After fixes, the same critics recheck the exact final localization commit.

## 7. Definition of Failure

- ❌ English restoration starts from the current 523-word text or another source instead of exact `b924926` public prefix.
- ❌ The final project README is a shortened paraphrase, structural mirror, or second exposition of `.tfw/README.md`.
- ❌ A practical baseline section disappears without a concrete ledgered functional reason and equivalent newcomer capability.
- ❌ A word ceiling, compression ratio, or preferred band is introduced or used to justify deletion.
- ❌ A newcomer cannot choose an Edition, initialize/install, start with an exact command, understand repository structure/workflow, or find philosophy/mechanics/history from the README.
- ❌ RU or KK is an abbreviated summary, loses a practical function/link, adds new meaning/authority/capability, or has unresolved HIGH naturalness/calque/translation-smell findings.
- ❌ Restoration rolls back any Task Board line other than the normal TFW-55 row, changes TFW-60/parallel state, or places a board in RU/KK.
- ❌ Unsupported automatic capture, deterministic reproduction, self-maintaining documentation, independent agent authority, or untested capability survives unqualified.
- ❌ `.tfw/README.md`, framework mechanics, Editions, adapters, assets, BoK, docs site, old Phase B traces, or unrelated files change.
- ❌ RF/EV hide the owner rejection, present the old APPROVE as current acceptance, omit the ledger/critic lineage, or disagree on results.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Current compressed file biases the rewrite | Extract and hash `b924926` prefix before drafting; ledger every old heading |
| Old README facts are copied without review | AC-4 source-by-source fact table and local link/command checks |
| Philosophy correction expands into essay duplication | AC-3 minimal claim set plus explicit anti-paraphrase DoF |
| “Natural localization” becomes partial localization | Functional matrix covers every ledger row and newcomer question |
| Language critics focus only on prose style | Fixed packet requires practical completeness, facts, authority, navigation, and commands before style |
| Parallel Task Board changes are lost | Compare against Executor start commit, not historic `b924926`; exclude only TFW-55 row |
| Old successful-looking traces confuse later agents | New artifacts use `phase-b2`, Board labels old B1 as superseded, RF/REVIEW state owner rejection |
| Corrective work grows into BoK | Explicit scope/DoF and post-APPROVE docs-only correction of D66 |

## 9. Cross-Phase Modifications

| File | Also involved in | Coordination note |
|---|---|---|
| `README.md` | Phase A Task Board trace; superseded Phase B; parallel TFW tasks | Phase B.2 owns only the public prefix and normal TFW-55 row; preserve the live tail from Executor baseline |
| `README.ru.md`, `README.kk.md` | Superseded Phase B production | Replace content; retain old blobs through Git and old RF/REVIEW references |
| `.tfw/README.md` | Phase A approved result | Read-only semantic source; reviewed blob must remain unchanged |
| `KNOWLEDGE.md` D66 | Rejected Phase B docs closure | Executor must not edit; Coordinator corrects only after new REVIEW APPROVE via `/tfw-docs` |

---

*TS — TFW-55 / Phase B.2: Restore and Localize the Project README | 2026-08-26*
