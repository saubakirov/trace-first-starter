# ONB — TFW-55 / Phase B: Multilingual Public Entry

> **Date**: 2026-08-26
> **Author**: Codex Executor
> **Status**: 🟠 ONB — complete; no blocking questions
> **Parent HL**: [HL-TFW-55](../HL-TFW-55__canonization_program.md)
> **Phase HL**: [Phase B derivation](HL__phase-b__multilingual_public_entry.md)
> **TS**: [TS Phase B](TS__phase-b__multilingual_public_entry.md)
> **Execution baseline**: `6ec4d6f763a3007e4b887cda80817bb8f8c7538b`

---

## 1. Understanding

Replace only the English onboarding content before `## Task Board` in root `README.md`, then create independent Russian and Kazakh doorways beside it. English remains the semantic source and the only operational Task Board. All three doorways must preserve the same six semantic invariants, proportional Editions, usable first actions, language switching, license/repository links, and routes to understand, use, or audit TFW, while each stays at or below 800 raw-Markdown words. Russian and Kazakh must read as naturally authored target-language prose rather than mirrored translations. The phase also creates separate final language reports, EV, RF, and narrow attributed commits; it does not create a BoK or modify the reviewed Project North Star or framework mechanics.

The owner-approved master amendments, reviewed Phase A result, approved Phase B derivation, and approved TS resolve source authority, scope, terminology, language topology, board boundary, and size rules. No new contract decision is required.

## 2. Entry Points

- Production targets: [`README.md`](../../../README.md), root `README.ru.md`, and root `README.kk.md`.
- Semantic source: reviewed [Project North Star](../../../.tfw/README.md), including the TFW definition, proportional realizations, and `NS1`–`NS3`.
- Approved contracts: [master HL](../HL-TFW-55__canonization_program.md), [Phase B HL](HL__phase-b__multilingual_public_entry.md), and [Phase B TS](TS__phase-b__multilingual_public_entry.md).
- Precedent/result bounds: [Phase A RF](../phase-a/RF__phase-a__canonical_foundation_essay.md) and [Phase A REVIEW](../phase-a/REVIEW__phase-a__canonical_foundation_essay.md).
- Usage facts: [Editions](../../../editions/README.md), [Quick Start](../../../.tfw/quickstart.md), edition roots, and [MIT License](../../../LICENSE).
- Evidence targets: `evidence/EV__phase-b__multilingual_public_entry.md`, `evidence/LANG_REVIEW__phase-b__ru.md`, and `evidence/LANG_REVIEW__phase-b__kk.md`.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The approved sources answer all implementation-significant questions, and the delegation explicitly authorizes execution after source-based resolution.

## 4. Recommendations (suggestions, not blocking)

1. Draft the English doorway first as the frozen semantic packet, then compose Russian and Kazakh independently from semantic units rather than sentence-by-sentence translation.
2. Keep Quick Start compact but executable by offering copy/follow paths for new, existing, and configured projects; link to full instructions rather than reproducing them.
3. Use the same destination paths and code identifiers across languages, while allowing headings, paragraph order, and explanatory rhythm to differ naturally.
4. Treat the 550–700-word band as drafting guidance only. Required meaning and usability take priority up to the hard 800-word ceiling.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Russian has abundant owner-source phrasing, while Kazakh does not; superficially fluent Kazakh can still carry English or Russian syntax and therefore needs the stricter triangulated back-translation required by AC-9.
2. A language reviewer can review a stale draft after production changes. The final report must name the reviewed commit/blob and be regenerated or explicitly rechecked after every material localization edit.
3. Markdown links can resolve as files while still routing a localized reader into untranslated operational content. The audit route must state that the English Task Board/corpus is authoritative rather than implying a localized operational state.
4. Current edition-specific README files are Russian-language historical products even though the top-level Editions guide is English. Doorway claims must use the current top-level guide and capability limits rather than inferring polished multilingual edition UX.
5. The Task Board is long but wholly outside the English onboarding metric. Any counting script that scans the whole file would create false pressure to remove required doorway meaning.

## 6. Inconsistencies with Code (spec vs reality)

| # | Approved/source claim | Repository state | Disposition |
|---|---|---|---|
| 1 | Master HL §7.2 and the Task Board link to `research/iter2/RES.md`; Phase A REVIEW says the citation resolved | `tasks/TFW-55__canonization_program/research/iter2/RES.md` is absent at execution baseline `6ec4d6f` | Non-blocking for Phase B because reviewed `.tfw/README.md`, Phase A RF/REVIEW, and the approved Phase B contracts are the controlling source packet. Do not recreate or repair research traces under Executor scope; report as an observation. |
| 2 | Phase B source measurements say 1,485 English onboarding words and 1,548 North Star words | Reproduced exactly with the TS raw-Markdown `\S+` convention: 1,485 + 1,548 = 3,033 | Consistent; use these as the before counts. |
| 3 | TS requires `.tfw/README.md` blob `71a4d725...` to remain unchanged | Baseline blob is `71a4d725cff7d0d7508403589195e9f87a0fc49a` | Consistent; verify again before RF. |

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|---|---|---|
| 1 | [`README.md`](../../../README.md) — landing, Editions, Quick Start, Task Board | ✅ | Applied | Replace only content before the hard board boundary; preserve the board except the TFW-55 workflow row. |
| 2 | [`.tfw/README.md`](../../../.tfw/README.md) — reviewed Project North Star | ✅ | Applied | Semantic source for the definition, Trace, human authority, proportional realizations, and `NS1`–`NS3`; read-only in Phase B. |
| 3 | [KNOWLEDGE.md](../../../KNOWLEDGE.md) — D2, D35, D40, D52–D60 | ✅ | Applied | Preserve surface separation, domain breadth, evidence honesty, proportional Editions, and capability-claim limits. |
| 4 | [knowledge/philosophy.md](../../../knowledge/philosophy.md) — F3, F6, F8, F10–F16, F21–F25, F32–F33 | ✅ | Applied | Keep public language critical, domain-neutral, continuation-oriented, and free of filler or untested capability claims. |
| 5 | [`.tfw/conventions.md`](../../../.tfw/conventions.md) — §§3, 11, 14 | ✅ | Applied | Enforce North Star roles, scope budgets, no placeholders, trace discipline, evidence honesty, and Executor role lock. |
| 6 | [knowledge/convention.md](../../../knowledge/convention.md) — F7, F9, F17–F19 | ✅ | Applied | Retain stable brand/code names but optimize the doorway for newcomer-readable target-language prose. |
| 7 | [knowledge/process.md](../../../knowledge/process.md) — F2, F11, F16, F22, F25, F27 | ✅ | Applied | Prefer observed workflow facts and source-backed capability limits; do not manufacture a localization registry or extra ceremony. |
| 8 | [knowledge/constraint.md](../../../knowledge/constraint.md) — F2, F3, F6–F7 | ✅ | Applied | Keep the public files concise, avoid template-driven filler, and verify the non-code document result proportionally. |
| 9 | [knowledge/domain.md](../../../knowledge/domain.md) — F1–F3 | ✅ | Applied | Lead through the pain of lost continuity and introduce shared terminology through use rather than a definition dump. |
| 10 | [knowledge/stakeholder.md](../../../knowledge/stakeholder.md) — F1, F4 | ✅ | Applied | Put human value and a low-friction entry before detailed mechanics. |
| 11 | [TFW-32 Phase D RF](../../TFW-32__methodology_and_positioning/PhaseD/RF__PhaseD__positioning_and_messaging.md) | ✅ | Applied critically | Preserve business-first clarity while removing the old audience cards, comparison matrix, and unsupported self-maintenance language. |
| 12 | [TFW-51/52](../../TFW-52__tfw_light_v1/HL-TFW-52__tfw_light_v1.md) — simplification and Editions | ✅ | Applied | Describe Editions by work/risk, keep Light low-friction, and state Assisted limits without promising hooks or superiority. |
| 13 | [TFW-55 RES Iteration 1](../research/iter1/RES.md) | ✅ | Applied | Preserve corpus/essay/spec authority separation and the framework-only overclaim control. |
| 14 | `TFW-55 RES Iteration 2` | ⚠️ unavailable | Applied through reviewed successor sources | The cited file is absent at `6ec4d6f`; its approved consequences are already frozen into the master HL, reviewed North Star, Phase A RF/REVIEW, and Phase B TS. |
| 15 | Owner mini-essay 0.8 corpus | N/A to direct Phase B loading | Applied through Phase A | Phase B derives from the reviewed English result, not directly from the private narrative corpus. Natural Russian formulations may follow the approved Project North Star. |
| 16 | Owner architecture note | N/A to direct Phase B loading | Applied through Phase A | The approved methodology architecture is already expressed in `.tfw/README.md` and the frozen contract. |
| 17 | Owner BoK v0.1 working map | N/A to direct Phase B loading | N/A | Phase B must not create or derive authority from the unapproved BoK draft. |

No new PV item is needed to execute Phase B. The missing Iteration 2 repository trace is an out-of-scope observation, not new project knowledge.

---

*ONB — TFW-55 / Phase B: Multilingual Public Entry | 2026-08-26*
