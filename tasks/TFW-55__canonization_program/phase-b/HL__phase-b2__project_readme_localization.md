# HL — TFW-55 / Phase B.2: Restore and Localize the Project README

> **Date**: 2026-08-26
> **Author**: Coordinator
> **Status**: ✅ APPROVED — owner 2026-08-26; ready for `/tfw-handoff`
> **Parent HL**: [HL-TFW-55](../HL-TFW-55__canonization_program.md)
> **Master freeze**: `5dee93d` — owner-approved Amendment A6
> **Phase A source**: [RF](../phase-a/RF__phase-a__canonical_foundation_essay.md) · [REVIEW](../phase-a/REVIEW__phase-a__canonical_foundation_essay.md) · [Project North Star](../../../.tfw/README.md)
> **Superseded Phase B trace**: [RF](RF__phase-b__multilingual_public_entry.md) · [REVIEW](REVIEW__phase-b__multilingual_public_entry.md) — technically approved against the wrong document function, then rejected by the owner
> **Authority**: derivation-only; the master HL owns Vision, Target State, Phases, DoD, DoF, and Principles

---

## Context

The first Phase B implementation reduced the project README to 523 words and made the localized files equally short. It satisfied the then-approved doorway contract, but the owner rejected the result: the root README stopped being a practical guide to this repository and became a paraphrased second version of `.tfw/README.md`. The essay and the project README have different jobs.

Phase B.2 therefore restarts from the exact English public prefix at commit `b924926`, not from the rejected 523-word text. It restores the project-guide function first, applies only minimal philosophical and factual corrections, then localizes that practical README naturally into Russian and Kazakh. The current Task Board tail is preserved from the Phase B.2 execution baseline; it is never restored from `b924926`.

```text
                         TWO DIFFERENT DOCUMENT JOBS

  README.md / README.ru.md / README.kk.md        .tfw/README.md
  ───────────────────────────────────────        ──────────────
  What is this repository?                       Why does TFW exist?
  Who is it for?                                 Philosophy of Trace
  Which Edition should I choose?                 purpose / principles / non-goals
  How do I install or initialize it?             human–agent boundary
  Which command starts work?                     canonical explanatory essay
  What files and workflows exist?
  Where are mechanics, history, and help?

  practical project guide                        philosophical depth
             │                                            ▲
             └────────────── links, does not paraphrase ───┘
```

## Verified Starting Point

| Surface | Verified state | Phase B.2 consequence |
|---|---|---|
| `b924926:README.md` public prefix | 1,485 whitespace-delimited words; SHA-256 `d14f9b89b174a59f8cd3177dfd111147ec2efdfcb3254fd3790788896b11638d` | Exact functional baseline for English restoration and the RU/KK localization scope |
| Current `README.md` | Rejected 523-word public prefix followed by the live Task Board | Replace only the prefix; retain the current board tail and parallel task state |
| `.tfw/README.md` | 1,548-word reviewed Project North Star; blob `71a4d725cff7d0d7508403589195e9f87a0fc49a` | Read-only philosophy/authority source; do not turn the project README into its summary |
| `README.ru.md` / `README.kk.md` | Short localizations of the rejected doorway | Replace with natural localizations of the restored practical README; no Task Boards |
| Original Phase B RF/REVIEW | REVIEW APPROVE followed by explicit owner rejection | Preserve unchanged as superseded history; new RF/REVIEW must explain the mismatch |
| Knowledge Gate | task sequence 60 − consolidation 58 = 2; hard interval 5 | Passed; `/tfw-knowledge` is not due |

The public prefix at `b924926` is byte-identical to the prefix at `6ec4d6f`; the earlier commit is used because it is the exact pre-Phase-B reviewed baseline named by parent coordination.

## Keep / Update / Add / Remove Ledger

Practical content is kept by default. A section may disappear only if the executor records a concrete functional reason and the formal Reviewer agrees that a newcomer loses no capability.

| Baseline block | Disposition | Allowed change | Required result |
|---|---|---|---|
| Logo, title, tagline, badges | **KEEP** + **ADD** | Add the visible language switch and a short semantic-source notice | Brand and language discovery remain immediate |
| Opening pain/promise and Project North Star link | **KEEP** + **UPDATE** | Correct the category to methodology grounded in the Philosophy of Trace; qualify automatic/self-documenting claims; keep the practical promise | A newcomer understands the continuity problem without receiving a second essay |
| `## Editions` | **KEEP** + **UPDATE** | Align Light/Assisted/Full descriptions and links with current Edition facts | Reader can choose an Edition by work and risk |
| `## Who TFW Is For` and three audience cards | **KEEP** | Natural wording changes only; remove unsupported absolutes, not the audience guidance | Product leaders, analysts/researchers, and engineers can recognize their use case |
| `## Quick Start` and three project states | **KEEP** + **UPDATE** | Preserve copyable starts; align initialization/migration path and exact commands with current sources | New, existing, and configured projects each have an actionable first step |
| `### FAQ` | **KEEP** + **UPDATE** | Correct stale tool/capability facts and overclaims; keep practical questions | Common adoption questions remain answered in the README |
| `## How It Works` | **KEEP** + **UPDATE** | Keep the explanatory table; replace deterministic, automatic-documentation, or independent-agent-authority wording | The workflow model is useful and consistent with the North Star |
| `## What's Inside` | **KEEP** + **UPDATE** | Verify current root and `.tfw/` paths; update descriptions minimally | Reader understands repository structure without opening every file |
| `## Tool Adapters` | **KEEP** + **UPDATE** | Verify current adapters and entry points | Tool setup remains discoverable |
| `## Key Concepts` | **KEEP** + **UPDATE** | Keep lifecycle/modes/budgets/conduct/version routes current | Reader can orient in the working method |
| `## Updating TFW` | **KEEP** + **UPDATE** | Preserve `/tfw-update` guidance and current links | Existing users know how to update safely |
| `## Links` | **KEEP** | Verify destinations; retain repository, docs, help, author, and license routes | Public resources remain discoverable |
| Unsupported phrases such as “traces replace documentation”, “automatically captures”, “decisions document themselves”, or unbounded “AI agents are team members” | **REMOVE OR REPLACE CLAIM**, not section | Use bounded, factual wording tied to selected traces and human authority | Minimal philosophy alignment without deleting practical content |
| `## Task Board` and everything below it | **KEEP FROM CURRENT EXECUTION BASELINE** | Only the normal TFW-55 row may change for workflow status | No TFW-60 or parallel task state is rolled back |

## Result the Owner Will Review

### Functional newcomer walkthrough

After reading any language version, a newcomer must be able to answer and act on all of these:

1. **What is this?** A repository and reference implementation for the TFW methodology, grounded in the Philosophy of Trace.
2. **Is it for me?** The audience/use-case section connects continuity failures to product, research/analysis, engineering, and non-code work.
3. **Which Edition do I use?** Light, Assisted, and Full remain distinguishable by work shape and risk.
4. **How do I begin?** The README gives usable actions for a new project, an existing project, and an already configured project.
5. **Which command starts the workflow?** Exact `/tfw-*` commands and the current lifecycle remain visible and copyable.
6. **What is in the repository?** Root files, `.tfw/`, adapters, concepts, updating, and help links remain explained.
7. **Where is deeper truth?** Philosophy routes to `.tfw/README.md`; mechanics to conventions/workflows; history and evidence to the English Task Board and traces.

### Minimal philosophy alignment

The practical README needs only enough philosophy to avoid contradiction:

- TFW is a methodology for joint human–AI work, grounded in the Philosophy of Trace.
- Humans retain purpose, legitimate authority, judgment, acceptance, accountability, and stop responsibility.
- Agents perform bounded work; selected durable Traces preserve continuity.
- TFW is not automatic truth, deterministic reproduction, self-maintaining documentation, or authority granted by participation.
- The full argument belongs in `.tfw/README.md`; the project README links there instead of retelling it.

### Localization contract

Russian and Kazakh localize the restored practical README, not the rejected doorway and not the essay. They preserve every practical capability and destination while using natural target-language syntax, paragraphing, and idiom. Section topology may change when that improves reading, but the functional ledger must map every English block to a target-language location or a justified equivalent. Commands, paths, URLs, Edition names, identifiers, and anchors remain exact.

Two isolated language critics check the final files. They block only material meaning, factual, authority, navigation, missing-function, serious naturalness, calque, or translation-smell defects. Taste-only alternatives remain non-blocking. Their complete draft and exact-final rechecks are stored in new Phase B.2 language-review reports, separate from the superseded Phase B evidence.

## Deliverables

1. Restore and minimally align only the English public prefix above `## Task Board`; preserve the live board tail except normal TFW-55 row transitions.
2. Replace `README.ru.md` and `README.kk.md` with natural localizations of the restored practical README; neither contains a Task Board.
3. Make the language switch visible near the top of all three files and keep English as the semantic source.
4. Preserve the practical project-guide functions recorded in the ledger, with exact current paths, commands, Edition facts, structure, workflow, updating, and links.
5. Preserve new Phase B.2 ONB, EV, language reports, RF, review-stage files, and REVIEW without changing or deleting the superseded Phase B chain.
6. After REVIEW APPROVE, correct the stale D66/KNOWLEDGE entry created by the rejected implementation through `/tfw-docs`; do not start BoK.

## Explicitly Not in Phase B.2

- rewriting `.tfw/README.md`, translating the essay, or adding a second philosophical exposition to the project README;
- BoK, book, course, guide, certification, launch, marketing campaign, or documentation-site redesign;
- changes to workflows, templates, conventions, glossary, Editions behavior, adapters, runtime, or visual assets;
- rollback of the Task Board, TFW-60 state, TFW-54 files, research artifacts, or any parallel work;
- an arbitrary word ceiling, compression quota, or preferred band;
- claims of measured human comprehension, adoption, or market effect.

## Research Decision

No new `/tfw-research` iteration is needed. The owner directly identified the document-role failure and selected the exact baseline and desired function. Phase A already fixed the philosophy; Phase B.2 is a bounded restoration, factual alignment, and localization problem. Remaining uncertainty is editorial/language quality and is handled by the keep/update/add/remove ledger, deterministic repository checks, two language critics, and a new independent formal Reviewer.

## Phase-Local Risks

| Risk | Control in TS |
|---|---|
| Executor starts from the current 523-word text | Exact `b924926` prefix hash and section-ledger gate |
| Restoration rolls back current Task Board state | Separate prefix/tail reconstruction; current execution-baseline tail hash; only TFW-55 row allowed to change |
| “Minimal philosophy update” grows into a second essay | AC and DoF prohibit paraphrasing `.tfw/README.md`; every update must map to a stale/false claim or authority need |
| Old practical section is deleted as “duplication” | Keep-by-default ledger and functional newcomer walkthrough |
| RU/KK become abbreviated summaries | Full functional-parity matrix against the restored English README plus separate critics |
| Natural localization becomes literal translation | Target-language naturalness, calque, and translation-smell review with exact-final recheck |
| Old APPROVE is silently treated as current acceptance | New RF/REVIEW must cite owner rejection and classify the old chain as superseded |
| Stale D66 survives closure | Mandatory post-APPROVE `/tfw-docs` correction; BoK remains forbidden |

---

*HL — TFW-55 / Phase B.2: Restore and Localize the Project README | 2026-08-26*
