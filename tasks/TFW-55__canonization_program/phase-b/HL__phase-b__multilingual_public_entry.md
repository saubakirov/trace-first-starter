# HL — TFW-55 / Phase B: Multilingual Public Entry

> **Date**: 2026-08-26
> **Author**: Coordinator
> **Status**: ✅ APPROVED — owner 2026-08-26; ready for `/tfw-handoff`
> **Parent HL**: [HL-TFW-55](../HL-TFW-55__canonization_program.md)
> **Phase A source**: [RF](../phase-a/RF__phase-a__canonical_foundation_essay.md) · [REVIEW](../phase-a/REVIEW__phase-a__canonical_foundation_essay.md) · [Project North Star](../../../.tfw/README.md)
> **Master freeze**: `a60bc6d` — owner-approved Amendments A2–A5
> **Authority**: derivation-only; the master HL owns Vision, Target State, Phases, DoD, DoF, and Principles

---

## Context

Phase A established the English Project North Star in `.tfw/README.md` and passed independent review. Phase B now replaces the 1,485-word English landing section with a doorway of at most 800 words and creates Russian and Kazakh derived doorways beside it.

```text
                         ENGLISH SEMANTIC SOURCE
              .tfw/README.md + public part of README.md
                                  │
                       semantic derivation only
                    ┌─────────────┴─────────────┐
                    ▼                           ▼
              README.ru.md                 README.kk.md
             Russian doorway              Kazakh doorway

README.md alone continues below with the only operational Task Board.
```

This phase is not translation of the 1,548-word essay into two languages. All three root files perform the same smaller job: make TFW understandable enough to choose a path, begin using it, or inspect its evidence. Russian and Kazakh are independent localizations: they preserve the English semantic contract but may use different paragraph order, sentence structure, examples of emphasis, and natural formulations. Literal translation, English-syntax calques, and mirrored prose are defects rather than signs of fidelity.

## Verified Starting Point

| Surface | Current measured state | Phase B consequence |
|---|---:|---|
| English root public section | 1,485 whitespace-delimited words; 246 lines | Reduce to ≤800 words; remove duplicated philosophy, FAQ, inventories, adapter reference, and lifecycle detail |
| `.tfw/README.md` | 1,548 words; REVIEW APPROVE; `NS1`–`NS3` stable | Semantic and North Star source; Phase B must not modify it |
| Combined English explanation | 3,033 words | Reduce to ≤2,600; the 800-word root ceiling makes the final maximum 2,348 |
| `README.ru.md` | absent | Create one derived Russian doorway, ≤800 words, no Task Board |
| `README.kk.md` | absent | Create one derived Kazakh doorway, ≤800 words, no Task Board |
| Root Task Board | one English operational board beginning at `## Task Board` | Preserve as the only board; normal TFW-55 status-row transitions are the sole allowed Phase B changes inside it |

## Result the Owner Will Review

### Three files, one doorway contract

```text
┌─────────────────────────────────────────────────────────────────┐
│ [English] · [Русский] · [Қазақша]                              │
│ logo · Trace-First Workflow · existing brand line              │
├─────────────────────────────────────────────────────────────────┤
│ THE PROBLEM + ONE DEFINITION                                    │
│ delegated intellectual work loses purpose and continuity        │
│ TFW = methodology grounded in the Philosophy of Trace           │
├─────────────────────────────────────────────────────────────────┤
│ CHOOSE PROPORTIONALLY                                           │
│ Light · Assisted · Full                                         │
├─────────────────────────────────────────────────────────────────┤
│ START                                                           │
│ new project · existing project · already using TFW              │
├─────────────────────────────────────────────────────────────────┤
│ THREE ROUTES                                                    │
│ understand → North Star                                         │
│ use → Quick Start / Editions                                    │
│ audit → Task Board / traces / knowledge                         │
├─────────────────────────────────────────────────────────────────┤
│ repository · license · semantic-source notice                    │
└─────────────────────────────────────────────────────────────────┘

README.md only:
┌─────────────────────────────────────────────────────────────────┐
│ ## Task Board — unchanged except TFW-55 workflow status row      │
└─────────────────────────────────────────────────────────────────┘
```

### Content budget

Word count is a ceiling, not a target. The preferred drafting band is 550–700 words per doorway, leaving room for natural Russian and Kazakh phrasing while staying below 800; it must not force removal of meaning needed by the doorway contract. For English, the count ends immediately before `## Task Board`: the heading and the entire Task Board section are excluded and may not be used as a reason to shorten the onboarding prose.

| Content block | Purpose | Indicative share |
|---|---|---:|
| Header + language/source notice | Discovery and authority | 30–60 words |
| Problem + definition | Immediate understanding | 100–150 |
| Editions | Choose proportional implementation | 80–120 |
| Quick Start | Take the first usable action | 180–260 |
| Understand / use / audit paths | Navigation without duplication | 70–110 |
| Repository / license / attribution | Essential public links | 30–60 |

### Semantic invariants across languages

Every version must carry the same meaning, although sentence order and idiom may differ:

1. TFW is a methodology for joint human–AI work, grounded in the Philosophy of Trace.
2. People retain purpose, legitimate authority, judgment, acceptance, accountability, and stop responsibility.
3. Agents perform bounded work; selected durable Traces preserve continuity.
4. Light, Assisted, and Full are proportional realizations chosen by work and risk, not prestige.
5. The Project North Star owns stable purpose/principles/non-goals; detailed mechanics and history live elsewhere.
6. TFW is domain-agnostic and vendor-independent; no deterministic, self-documenting, or untested-capability promise returns.

### Terminology contract

| Concept | English source | Russian default | Kazakh default | Rule |
|---|---|---|---|---|
| Brand | Trace-First Workflow (TFW) | Trace-First Workflow (TFW) | Trace-First Workflow (TFW) | Never translate the brand name or acronym |
| Foundation | Philosophy of Trace | Философия Следа | Із философиясы | Use the localized form naturally; English may appear once for disambiguation |
| Core record | Trace | След (Trace) on first use | Із (Trace) on first use | Preserve the capitalized methodological concept; do not translate as chat log |
| Product anchor | Project North Star; `NS1`–`NS3` | Project North Star; `NS1`–`NS3` | Project North Star; `NS1`–`NS3` | Keep the citable product name and IDs stable |
| Editions | Light / Assisted / Full | Light / Assisted / Full | Light / Assisted / Full | Names and paths stay unchanged; explanations are localized |
| Commands and paths | `/tfw-*`, `.tfw/...` | unchanged | unchanged | Code identifiers are never translated |

Language reviewers may improve Russian/Kazakh terms when they preserve these distinctions and record the reason in EV. Localizations may reuse natural formulations, explanatory moves, and short fragments from the approved `.tfw/README.md` when that improves the target language without changing an invariant. Literal back-translation is not required; semantic equivalence and idiomatic clarity are.

## Language Review Contract

The executor obtains two fresh, isolated bilingual critiques before RF:

- one Russian review of `README.ru.md` against the reviewed English source packet;
- one Kazakh review of `README.kk.md` against the same packet.

Each reviewer receives the English doorway, the relevant parts of the approved `.tfw/README.md`, the target localization, the six invariants, terminology table, and a fixed rubric. It reports: invariant coverage, semantic drift, missing/extra promise, command/path corruption, terminology problems, naturalness, English-syntax calques, translation smell, and whether the localization reads as independently authored target-language prose. A high-severity meaning, factual, authority, navigation, or natural-language usability error blocks RF. Stylistic preference without semantic or usability harm is non-blocking and must not create an endless revision cycle.

The complete Russian and Kazakh reports are preserved as separate, reviewable evidence files: `evidence/LANG_REVIEW__phase-b__ru.md` and `evidence/LANG_REVIEW__phase-b__kk.md`. The EV file links them, records dispositions, and confirms that the final localized files—not an earlier draft—were checked.

## Deliverables

1. Replace only the public section above `## Task Board` in English `README.md`; preserve the board except normal TFW-55 status transitions.
2. Create root-level `README.ru.md` and `README.kk.md` as natural, independently composed localizations, each ≤800 words and without a Task Board.
3. Make working `English · Русский · Қазақша` links the first visible block in all three files and declare English as the semantic source.
4. Preserve one concise definition, proportional Editions, usable Quick Start, license/repository links, and explicit understand/use/audit paths in every language.
5. Remove duplicate philosophy, audience cards, FAQ, lifecycle/reference inventories, adapter tables, and update instructions when an authoritative link already exists.
6. Verify word ceilings (with the entire Task Board excluded from the English count), semantic parity, local links, Task Board uniqueness, terminology, and independent Russian/Kazakh naturalness reviews in separate reports plus EV/RF.

## Explicitly Not in Phase B

- any change to `.tfw/README.md`, Project North Star semantics, workflows, templates, Editions behavior, adapters, configuration, or runtime;
- a full translation of the Project North Star essay or operational specification;
- creation or publication of the BoK;
- visual rebrand, new graphics, documentation site redesign, book/course/guide content, marketing campaign, or launch work;
- claims of human comprehension, learning, adoption, or market effect.

## Research Decision

No additional `/tfw-research` iteration is justified. The master research and reviewed Phase A result already determine meaning, authority, exclusions, and source text. Phase B uncertainty is bounded localization/editorial quality, resolved by reproducible parity checks and two language critiques. Real human reception remains a later field question and cannot change the current file architecture.

## Phase-Local Risks

| Risk | Control in TS |
|---|---|
| Localization becomes a second canon | English source notice, invariant matrix, and drift review in both derived files |
| Russian or Kazakh reads as translated English | Independently composed target-language prose plus separate naturalness/calque reports and a high-severity blocker |
| Simplification removes the usable entry | Mandatory Editions, Quick Start, and understand/use/audit routes in every file |
| The Task Board is damaged or duplicated | Board-tail comparison with only the TFW-55 row allowed to change; no board heading/rows in localizations |
| Three files differ structurally | Expected and allowed; semantic units and navigation roles—not paragraph mirroring—are the parity gate |
| Old overclaims survive because they are familiar marketing | Required disposition list against the current 1,485-word source and North Star non-goals |
| Review cycles on taste | Materiality rule: only meaning, authority, factual, navigation, or serious idiom defects block |

---

*HL — TFW-55 / Phase B: Multilingual Public Entry | 2026-08-26*
