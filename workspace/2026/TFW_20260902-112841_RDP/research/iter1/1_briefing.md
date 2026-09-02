# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260902-112841_RDP](../../HL-TFW_20260902-112841_RDP.md)
> Goal: Every finding a review produces becomes a decision by rule — one criterion, one named decider, one termination.

> **Mode:** `deep` (configured default is `focused`). Reason: H1 and H4 can fail the task outright,
> and HL §10's Challenge focus explicitly demands counter-evidence — *"argue that the criterion is
> unfalsifiable in practice"* — which `focused` does not require. Owner instruction for this run:
> **no questions, no gates.** Stage checkpoints are written; the 🛑 WAIT after each is not taken.

> **Acting handle:** `saubakirov` — one profile in `team/`, used silently per `conventions.md` §4.

## Research Plan

### Gather — measure three corpora that behave differently on the same templates
- Verify the HL's own counts before building on them: REVIEW file totals, repeat-round counts, versions.
- Verdict distribution per corpus (APPROVE / REVISE / REJECT), extracted from §4 of each REVIEW.
- Judge-row mark distribution (✅ / ❌ / ⚪) per corpus, normalised per review — the mechanism behind a
  low REVISE rate, if there is one.
- For every helpdesk REVISE: what was ordered, and what artifact records its closure.
- For every round past two in *any* corpus: what that round actually corrected.
- Candidate dimensions expected: termination trigger, decider for ordered work, disposition vocabulary,
  where the criterion lives, budget granularity.

### Extract — build the configuration space
- Cross-reference the dimensions; make combinations visible that the HL did not propose.
- Score the criterion against all nine TLD rows and compare with how each was actually ruled (H1).
- Classify every round-3+ item as work / specification / record (H2).
- Draft the mechanisms into `review.md` Steps 4–6 and count (H4) — this is answerable only by writing.

### Challenge — attack the survivors
- The strongest case that the criterion admits everything and therefore decides nothing.
- The strongest case that the two-round cap destroys real fixes.
- Pairwise consistency between termination trigger, decider, and disposition vocabulary.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | The criterion discriminates: applied to real findings it produces a materially different split from the eight ad-hoc rulings in §2.4, and at least one of those eight would change | open |
| H2 | Two rounds is the right cap: rounds beyond the second correct wording or specification rather than work | open |
| H4 | The three mechanisms fit under the budget in `review.md` — the excess is prose standing in for terms (F40) | open |
| H5 | The loops invented elsewhere converge on the same ladder the TFW-58 sketch prescribes | open |
| H6 | `helpdesk` avoids the loop for a locatable reason, not by luck — and if that reason is a practice, it is worth more than the cap | open |

**H3 is not assigned to this iteration** — whether the coordinator's single act can be made non-rubber-stamp
without a new entity is answered by reading text that already exists, not by measuring corpora. It belongs
to the TS or to iteration 2.

## Scope Intent

- **In scope:** five corpora (`helpdesk`, `ai-first-devices`, `innoforce-ai-first`, `kaznpu-ai-lab`, this
  repository) read for review behaviour; the four rounds past two in this repository plus every one found
  elsewhere; the nine TLD disposition rows; `review.md` Steps 4–6 and Anti-patterns as a drafting surface.
- **Out of scope:** H3 (rubber-stamp prevention). Any edit to the HL. Any write outside this task directory.
  `KZ-IT-telegram-list` — carries no `.tfw/` and no REVIEW files; excluded after measurement, not assumed.

## Hard Boundaries (inherited from TLD, non-negotiable)

- No file in any tree but this one is created, modified, moved or deleted. Reading a sibling project is
  `find`, `wc`, `grep`, `sed`, `awk` and nothing else.
- `tasks/` is the frozen legacy corpus: cited, never edited. That includes TFW-58.
- `tfw.research.max_files_per_stage` is 15 and the corpora hold 331 REVIEW files. Sampling is deliberate
  and the method is declared in `2_gather.md`.

## Guiding Questions

Owner instruction for this run is **no questions**. The three that would otherwise have been asked are
recorded here so the record shows what was decided without him:

1. Does DoD 10's *"every section this task edits ends no larger than it started"* bind **per section**
   or across the **Steps 4–6 group** whose numbers it names? — Answered by measurement in Extract; the
   two readings give opposite verdicts, and this is raised as an amendment proposal rather than assumed.
2. If a third round is found to correct real work rather than wording, does the cap stand? — Treated as
   the HL's own filter says: H2 false → the cap must be re-derived or dropped. Reported, not decided.
3. Does the debt-search snippet in Step 5 stay? — Its 73 words decide whether the budget is met. Reported
   as a coordinator choice, not made here.

## User Direction

- **2026-09-02, owner, via command arguments:** *"no questions to me"* — run the full iteration without
  gates. Recorded as the reason every 🛑 WAIT in `research/base.md` was written-through rather than taken.
- **2026-09-02, owner, recorded in HL §10:** `helpdesk` was named by the owner as the control case for
  research. That instruction set the priority order used in Gather.

---
Stage complete: YES
