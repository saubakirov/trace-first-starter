# PROPOSAL — TFW-57: Artifact Growth Control

> **Date**: 2026-08-13
> **Author**: Coordinator (Claude Code)
> **Status**: ⬜ TODO — proposal only. No HL, no TS. Entry point: `/tfw-plan`.
> **Origin**: owner observation during TFW-53 Phase A review, plus REVIEW TFW-53/A third pass TD-140–TD-143

---

## The observation

> *«Мне кажется, вот такие циклы туда-сюда — ревью, фикс, ревью, фикс — приводят к таким проблемам часто.»* — owner, 2026-08-13

Every corrective cycle appends a defence against the last failure and nobody re-reads the whole. A finding says a line is wrong; the fix adds a clause. The materiality bar decides *whether* to fix. Nothing decides *how much text a fix may add*. Over a few cycles the artifact stops carrying its rule and starts carrying its own scar tissue.

The instance that triggered this: `conventions.md` rule 15 grew **30 → 162 words** across three review passes — MSYS after the first, anchoring plus a documented limit after the second — against a 37-word median for the 21 rules around it. It was then repaired not by compression but by replacing the mechanism, which removed the need for 132 of those words entirely.

The same shape is visible across the whole repository, and it is not confined to framework files.

## Measured

Word counts, this repository, from the first commit that contains each file:

| File | 2026-07-21 | now | Change | Has a numeric budget? |
|------|-----------:|----:|-------:|----------------------|
| `README.md` | 2,778 | 3,152 | +13% (2.9× since 2025-09) | ✗ none |
| `TECH_DEBT.md` | 1,463 | 3,562 | **+144%** | ✗ none |
| `KNOWLEDGE.md` | 5,797 | 6,960 | +20% | ⚠️ lines only, and breached |
| `.tfw/conventions.md` | 3,817 | 5,200 | +36% | ✗ none |
| `.tfw/templates/HL.md` | 1,073 | 1,888 | **+76% in one phase** | ✗ F22 "minimalism", no number |
| `.tfw/glossary.md` | 2,908 | 2,967 | +2% | ✗ none |
| `.tfw/workflows/plan.md` | 1,205 | 1,205 | 0% | ✓ F2: 700–900 working, 1,200 hard |

**Two honest caveats, stated before anyone builds on this.**

1. **`plan.md`'s flat line is not evidence that the budget held it.** It was edited three times in the window — TFW-48/B and TFW-48/C both grew it — and returned to 1,205 by the *wholesale revert* of those tasks, not by a budget stopping anyone. As a control case it is confounded. Whether a number would have held it is untested.
2. **`glossary.md` grew 2% with no budget at all**, which is a counter-example to the simple story. Something else is holding it — most likely that a glossary article has an obvious natural size and a new term is an obvious new row, so growth is additive rather than accretive.

What survives both caveats is narrower and still worth acting on: **the artifacts that grew most are the ones with no number, and the one artifact that has a number is over it.**

## The sharper finding: a number without a checkpoint decays

`KNOWLEDGE.md` is configured with `tfw.knowledge.max_index_lines: 200`. It is **202 lines today**. The limit is breached, nothing reported it, and no workflow reads the value.

This reframes the task. The naive fix — give templates, conventions and task artifacts a word budget — reproduces the failure it is trying to cure, because a budget nobody checks is a comment. The mechanism has to be a *checkpoint*, and the number is only its parameter.

Related evidence from the same review pass:

- **TD-141** — the attention budget is numeric for workflows only. Templates have F22 "minimalism" with no number; `conventions.md` has none; task artifacts (TS, RF, ONB, REVIEW) have none. The three classes that grew are exactly the three with no number.
- **TD-142** — Phase A's own artifacts are simultaneously the largest in the repository: TS 4,107 against a 1,277 median across 64 tasks; RF 5,112 against 773; ONB 4,483 against 712. The causes are named as structural rather than stylistic — for instance, a TS has no change log, so a corrective pass appends where it should replace.
- **TD-140** — the HL template's two largest additions restate material that already exists elsewhere: §3.1 states Working Backwards twice, §12 restates `conventions.md` §3.

## Why the root documents belong in scope

The owner named `README.md`, `TECH_DEBT.md` and `KNOWLEDGE.md` specifically, and the numbers support it. Each has a different growth mechanism, which is why one rule will not cover all three:

| Document | Mechanism | What is missing |
|----------|-----------|-----------------|
| `README.md` | Every task that ships something user-visible adds a section; nothing ever consolidates. 2.9× since the first commit | No owner for length; no trigger to re-read the whole |
| `TECH_DEBT.md` | Append-only by design and correct to be so — but 55 open rows, +144% in three weeks. A purge happened once (2026-04-15, 41 items) as a one-off decision | A consolidation trigger. The ritual exists and has fired exactly once |
| `KNOWLEDGE.md` | Grows as decisions accumulate, which is the point. Has a configured line limit that nothing reads | A checkpoint that reads the limit already configured |

`TECH_DEBT.md` deserves care: unbounded growth there is partly *healthy*, because a debt register that stays small is usually a register nobody writes to. The question is not size but **whether every row is still true and still worth carrying** — closure and consolidation, not compression.

## Candidate scope

Sketch only. The shape is a decision for `/tfw-plan`.

1. **A checkpoint, not a cap.** Something reads the configured numbers and reports; where it lives (a workflow step, a gate, the knowledge consolidation cycle) is the central design question.
2. **Numbers for the three classes that have none** — templates, `conventions.md`, task artifacts — set from measured medians rather than invented.
3. **A correction rule.** A corrective pass may not grow the artifact it corrects: the rule stays the rule, the reasoning moves to knowledge. This is the direct answer to the owner's observation and the cheapest single item here.
4. **A change log for TS**, so a corrective pass replaces instead of appending (TD-142's named cause).
5. **A consolidation trigger for `TECH_DEBT.md`**, on the pattern the knowledge gate already uses — interval plus a mode.
6. **Duplication as a first-class finding.** §3.1 and §12 grew mostly by restating content that exists elsewhere; a growth rule that does not name duplication will be satisfied by shorter duplicates.

## Open questions

| # | Question |
|---|----------|
| 1 | Checkpoint or gate — does exceeding a budget block, warn, or only appear in a report? The knowledge gate's `hard / soft / off` mode is the obvious precedent |
| 2 | Where does the checkpoint live so it is not itself skippable? A rule that only fires when someone remembers to look is the defect being fixed |
| 3 | Are word counts the right measure for `TECH_DEBT.md`, or is open-row count and row age the honest metric? |
| 4 | Is D24's Pattern A — enforcement-critical values must be inline, restated rather than referenced — in tension with a duplication rule? It is deliberate duplication and it has a reason. The boundary needs stating, not assuming |
| 5 | Does the correction rule apply to *traces* (RF, REVIEW, ONB) at all? A trace that grows because the work was genuinely complicated is not a defect |

## Not in TFW-53

TD-141 and TD-142 are missing mechanisms, not defects in Phase A's work. Building them inside TFW-53 would be the scope inflation that task exists to prevent — and the amendment protocol would have to log it, which is how it was caught. TD-140 stays with TFW-53 Phase D, where a consistency pass is already scheduled and where merging §3.1's two blocks is in scope.

---

*PROPOSAL — TFW-57: Artifact Growth Control | 2026-08-13*
