# Verify — “Are the claims true?”

> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **Review target:** `9d65d4eeabd7737c25ae64587a91306d84c41821`
> **Execution baseline:** `6ec4d6f`
> **Min verify ratio:** 0.42
> **RF files claimed:** 8
> **Files required:** ⌈8 × 0.42⌉ = 4
> **Files verified:** 8/8 (100%; the complete execution scope)

## Verification Log

### V1: `README.md`

- **RF claim:** only the public onboarding above `## Task Board` was replaced, apart from the normal TFW-55 row transition.
- **Actual:** the pre-board surface is a 523-word English doorway with the language switch, semantic definition, human/agent authority boundary, three Editions, three start cases, three routes, `NS1`–`NS3`, attribution, and no forbidden guarantee. The board begins at the single `## Task Board` heading. After removing only the TFW-55 row and normalizing line endings, the baseline and final board tails are byte-equal and have SHA-256 `a8c544a50cc3d098f3890bc6b8d6e26bb9d5a05c333a9eb64672d7aa44b4ecb6`.
- **Match:** ✅

### V2: `README.ru.md`

- **RF claim:** a natural 528-word Russian doorway, derived from English meaning, with no Task Board and final HIGH severity zero.
- **Actual:** all required semantic and authority units are present, the source hierarchy is explicit, local routes resolve, commands and stable identifiers are preserved, and no board content is copied. Independent reading found idiomatic Russian overall. Phrases such as “О смысловом источнике” and “следуйте соответствующей миграции” admit smoother editorial alternatives, but neither changes meaning nor creates serious calque/translation smell. The final file is the exact language-critic recheck blob `5fde98450e6f248dfb695ef7f403f066f98f6cf3`.
- **Match:** ✅

### V3: `README.kk.md`

- **RF claim:** a natural 526-word Kazakh doorway, derived from English meaning, with no Task Board and final HIGH severity zero.
- **Actual:** all required semantic and authority units are present, the source hierarchy is explicit, local routes resolve, commands and stable identifiers are preserved, and no board content is copied. Independent reading found the doorway understandable and natural at the material threshold. “қайталанатын жұмысқа немесе қатысушысы аз жұмыста” and two already recorded LOW alternatives can be polished, but they do not distort the contract or rise to serious translation smell. The final file is the exact language-critic recheck blob `b4c2ca57de9d9d87a4d0f56b0dfaa402d2f8a76a`.
- **Match:** ✅

### V4: `phase-b/ONB__phase-b__multilingual_public_entry.md`

- **RF claim:** records scope, exact baseline, required source loading, language-review plan, questions, and constraints.
- **Actual:** it freezes the eight-file execution scope and read-only areas, uses the approved TS, records no blocking question, distinguishes the missing Iteration 2 trace from Phase B work, and carries the 17-source knowledge ledger.
- **Match:** ✅

### V5: `phase-b/RF__phase-b__multilingual_public_entry.md`

- **RF claim:** reports the implementation, decisions, AC results, evidence, observations, provenance, and residual limitations.
- **Actual:** file inventory and commit lineage match Git; reported counts, blobs, board-tail hash, language severity closure, and scope are reproducible. §§7–9 are present and appropriately state that execution produced no human-only fact candidate, strategic insight, or useful diagram.
- **Match:** ✅

### V6: `phase-b/evidence/EV__phase-b__multilingual_public_entry.md`

- **RF claim:** provides per-AC document gates, semantic/terminology matrices, navigation, budgets, lineage, board integrity, and subtraction evidence.
- **Actual:** every AC is mapped; deterministic values reproduce from Git objects. The artifact correctly distinguishes repository-local document verification from unavailable live/human reception evidence.
- **Match:** ✅

### V7: `phase-b/evidence/LANG_REVIEW__phase-b__ru.md`

- **RF claim:** full independent Russian draft/final critique chain with initial HIGH 4 → final HIGH 0.
- **Actual:** the report names critic task `01a03d51-1f84-79a3-a60d-79047fe60306`, exact draft/final commits and blobs, H1–H4 plus lower-severity findings, dispositions, back-translation, and final recheck. The critic thread and Git objects corroborate the chain; no finding was hidden by relabeling.
- **Match:** ✅

### V8: `phase-b/evidence/LANG_REVIEW__phase-b__kk.md`

- **RF claim:** full independent Kazakh draft/final critique chain with initial HIGH 2 → final HIGH 0.
- **Actual:** the report names critic task `01a03d51-2480-7ef1-a4d9-f9ad203793f8`, exact draft/final commits and blobs, H1–H2 plus lower-severity findings, dispositions, two back-translations, and final recheck. The critic thread and Git objects corroborate the chain; no finding was hidden by relabeling.
- **Match:** ✅

## Commands Executed

| # | Command / check | Result |
|---|---|---|
| 1 | `git diff --check 6ec4d6f 9d65d4e` | ✅ no whitespace errors |
| 2 | Configured build/test/lint commands from `.tfw/project_config.yaml` | ✅ all three execute; they are explicit configuration placeholders, so they establish no product behavior |
| 3 | Git-object word-count script, splitting English before the first `## Task Board` | ✅ old EN 1,485; final EN/RU/KK 523/528/526; `.tfw/README.md` 1,548; combined English 2,071 |
| 4 | Local Markdown target and anchor scan at the target commit | ✅ EN/RU/KK: 23/22/22 local targets checked, zero broken; `NS1`–`NS3` and `task-board` anchors resolve |
| 5 | Strict UTF-8 decode and mojibake scan over all four public surfaces | ✅ strict decode passes; zero suspicious sequences |
| 6 | Language lineage via `git rev-parse <commit>:<path>` and `git diff --exit-code caee273..9d65d4e -- README.ru.md README.kk.md` | ✅ draft RU/KK `063f…`/`614e…`; final `5fde…`/`b4c2…`; final critic targets unchanged in RF commit |
| 7 | `git rev-parse 9d65d4e:.tfw/README.md` | ✅ `71a4d725cff7d0d7508403589195e9f87a0fc49a` |
| 8 | Normalized non-TFW-55 board-tail comparison and SHA-256 | ✅ baseline equals final; both `a8c544a50cc3d098f3890bc6b8d6e26bb9d5a05c333a9eb64672d7aa44b4ecb6` |
| 9 | `git diff --name-status 6ec4d6f..9d65d4e` plus `--numstat` | ✅ exactly 8 execution-stage files; 854 insertions, 217 deletions, 1,071 changed-line operations; within 30 files / 15 new / 3,000 LOC |
| 10 | Frozen-surface diff for master HL, Phase B HL/TS, `.tfw/README.md`, and `research/**` | ✅ empty |
| 11 | Placeholder and forbidden-scope scan | ✅ no delivery placeholders; only pre-existing Task Board TODO statuses outside the onboarding; no BoK, research, spec/glossary, visual, registry, or roadmap change |

The RF's `≤900` figure originated as a TS planning estimate, not a configured acceptance budget. Actual churn is 1,071 line operations and remains below the approved configured 3,000-LOC ceiling; the RF does not misreport the actual value.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Primary source | Holds? |
|---|---|---|---|---|
| C1 | The three doorway counts and combined-English ceiling | RF §§2–4; EV AC-8 | blobs at `9d65d4e`, counted independently with the English board excluded | ✅ 523/528/526; 2,071 < 2,600 |
| C2 | `.tfw/README.md` stayed at the reviewed canonical essay blob | RF §§2, 3, 5 | Git object at `9d65d4e` and Phase A REVIEW | ✅ exact blob `71a4…`; 1,548 words |
| C3 | Edition descriptions and manual fallback are factual | all three doorways; EV AC-6 | `editions/README.md`, `editions/01-light/README.md`, `editions/02-assisted/README.md`, `.tfw/quickstart.md` | ✅ Light/Assisted/Full routing and Assisted manual fallback match their owners |
| C4 | Draft/final language review lineage and HIGH closure | RF §§1–3; both language reports | Git objects at `437f7a9`, `caee273`, `9d65d4e`; critic task records | ✅ RU 4→0 and KK 2→0; final blobs unchanged after recheck |

## Acceptance Criteria and DoF Verification

| AC | Independent result |
|---|---|
| AC-1 | ✅ English public onboarding is exactly the content before `## Task Board`; it is complete at 523 words, links directly to `NS1`–`NS3`, and contains no prohibited guarantee or authority claim. |
| AC-2 | ✅ Russian is a self-contained, materially natural 528-word localization; meaning, limits, authority, routes, and source precedence are intact; final HIGH=0. |
| AC-3 | ✅ Kazakh is a self-contained, materially natural 526-word localization; meaning, limits, authority, routes, and source precedence are intact; final HIGH=0. |
| AC-4 | ✅ The six invariant groups—problem/continuity, methodology/Trace, human authority, agent boundary, proportional Editions, and source/route hierarchy—are equivalent across languages with no extra authority. |
| AC-5 | ✅ A visible three-language switch is the first content block in all files; local paths, anchors, commands, and stable identifiers resolve and remain exact. |
| AC-6 | ✅ Editions and the three start cases are usable and source-backed; Assisted's manual fallback is explicit. |
| AC-7 | ✅ Each doorway provides distinct understand/use/audit routes and repository, documentation, author, and license attribution. |
| AC-8 | ✅ Per-doorway ceilings and combined-English ceiling pass; 523/528/526 are justified by full coverage and subtraction rather than padded to the 550–700 orientation; the board appears only in English and the non-TFW-55 tail is unchanged. |
| AC-9 | ✅ Independent critic tasks reviewed frozen draft blobs; full reports preserve initial findings, applied dispositions, back-translations, and exact final rechecks with HIGH=0. |
| AC-10 | ✅ Provenance is complete; scope is exactly eight execution files; `.tfw/README.md` and contracts are unchanged; no prohibited Phase B artifact was created. |

All 17 master DoF classes were checked against the Git diff and public files. None occurred: no authority promotion, guarantee, semantic omission, serious calque/translation smell, duplicated board, broken local onboarding link, hidden language finding, stale final recheck, filler, scope creep, spec/BoK/research rewrite, glossary/registry/roadmap/visual, or unrelated task-row edit.

The Russian and Kazakh files intentionally share the doorway's semantic-role order; that is the approved navigation contract, not evidence of sentence mirroring. Their sentence construction, paragraph distribution, explanations, and local connective choices are independently written. Remaining editorial alternatives are taste/fluency polish below the task's materiality threshold and do not warrant filler or another revision loop.

## Discrepancies Found

No material discrepancy between RF claims and the target commit.

Two limitations are recorded without converting them into Phase B findings:

1. `research/iter2/RES.md` is absent both at the clean execution baseline and target commit. The RF accurately records this pre-existing shared-checkout observation, and the executor did not change the link or any research artifact.
2. The frozen master HL also contains a pre-existing unresolved pointer to the absent TFW-54 HL. It is outside the Phase B public doorway, is not part of the RF's “zero broken public local links” claim, and was untouched by the executor. It does not make the approved clauses mutually inconsistent.

Because the review encountered a source-set limitation, verification was escalated to the full 8/8 execution files even though the minimum was 4.

## Evidence Verification

The TS deliberately classifies all ten Evidence fields as `N/A`: the ACs are repository-local document gates rather than test, screenshot, or visual proof requirements. That classification is correct. RF §5 additionally supplies observational artifacts whose existence and contents were independently verified:

| # | RF evidence reference | Artifact exists? | Matches claim? |
|---|---|---|---|
| E1 | `evidence/EV__phase-b__multilingual_public_entry.md` | ✅ | ✅ covers AC-1–AC-10 with reproducible document gates and honest limits |
| E2 | `evidence/LANG_REVIEW__phase-b__ru.md` | ✅ | ✅ complete draft/final RU chain; Git and critic task corroborate it |
| E3 | `evidence/LANG_REVIEW__phase-b__kk.md` | ✅ | ✅ complete draft/final KK chain; Git and critic task corroborate it |

Evidence completeness is therefore 10/10 classifications plus 3/3 referenced artifacts. Its green signal establishes repository-local semantics, navigation, counts, lineage, encoding, attribution, and scope; it does not establish live HTTP availability or human reception, and neither is claimed or required by the TS.

## Knowledge Citations Verified

| # | Artifact / citation | Link resolves? | Item/source exists? | Result |
|---|---|---|---|---|
| 1 | HL/ONB: `README.md` | ✅ | ✅ | applied boundary and routing source |
| 2 | HL/ONB: `.tfw/README.md` | ✅ | ✅ | exact reviewed semantic source |
| 3 | HL/ONB: `KNOWLEDGE.md` D2, D35, D40, D52–D60 | ✅ | ✅ | items read and applicable |
| 4 | HL/ONB: `knowledge/philosophy.md` cited F-items | ✅ | ✅ | items read and applicable |
| 5 | HL/ONB: `.tfw/conventions.md` §§3, 11, 14 | ✅ | ✅ | sections read and applicable |
| 6 | HL/ONB: `knowledge/convention.md` cited F-items | ✅ | ✅ | items read and applicable |
| 7 | HL/ONB: `knowledge/process.md` cited F-items | ✅ | ✅ | items read and applicable |
| 8 | HL/ONB: `knowledge/constraint.md` cited F-items | ✅ | ✅ | items read and applicable |
| 9 | HL/ONB: `knowledge/domain.md` F1–F3 | ✅ | ✅ | items read and applicable |
| 10 | HL/ONB: `knowledge/stakeholder.md` F1, F4 | ✅ | ✅ | items read and applicable |
| 11 | HL/ONB: TFW-32 Phase D | ✅ | ✅ | positioning source exists |
| 12 | HL/ONB: TFW-51/52 through TFW-52 HL | ✅ | ✅ | Editions/simplification source exists |
| 13 | HL/ONB: TFW-55 RES Iteration 1 | ✅ | ✅ | source exists and was applied |
| 14 | HL/ONB: TFW-55 RES Iteration 2 | ❌ pre-existing | ❌ in clean baseline | explicitly disclosed; approved consequences are traceable through frozen successors; no Phase B repair authorized |
| 15 | HL: owner mini-essay 0.8 corpus | ⚪ owner-local path | ✅ | Phase A source; correctly N/A for direct Phase B loading |
| 16 | HL: owner architecture note | ⚪ owner-local path | ✅ | Phase A source; correctly N/A for direct Phase B loading |
| 17 | HL: owner BoK v0.1 working map | ⚪ owner-local path | ✅ | deliberately non-authoritative and N/A to Phase B |

Total citation entries: 17; existing/resolvable sources: 16; one known unavailable baseline trace: 1; hallucinated Phase B citation: 0. No implementation claim contradicts `KNOWLEDGE.md` or its topic files.

## Checkpoint

**Self-check:**

- [x] Opened and recorded 8/8 claimed files (minimum 4).
- [x] Ran configured build/test/lint placeholders and substantive repository-local verification commands.
- [x] Checked four key claims against Git objects and primary repository sources; traced all 17 knowledge entries.
- [x] Verified every RF §3 checkmark against actual files and every TS AC/DoF class.
- [x] Read `KNOWLEDGE.md` and all applicable topic items; found no contradiction.
- [x] Verified RF §5 artifacts and checked that evidence classifications match what the artifacts establish.
- [x] Independently assessed Russian and Kazakh meaning, authority, naturalness, calques, composition, and critique closure.

Stage complete: **YES**
