# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260830-194027_TLD](../../HL-TFW_20260830-194027_TLD.md)
> Goal: a review records the debt it found in its own task and writes nothing else; the registry becomes history.

> **Mode:** focused — one OODA loop per stage, user tech claims cross-checked once.
> **Run condition:** the owner asked for this pass without gates (*«без вопросов ко мне»*). Every
> 🛑 WAIT in `research/base.md` is answered by the researcher and recorded in the stage checkpoint
> instead of being put to the owner. Nothing else in the workflow is relaxed.
> **Iteration:** 1 of 1 (min) / 2 (max), per `research/iterations.yaml`.

## Research Plan

**Gather — census the receiving projects, not this repository.**
- Enumerate every project on this machine carrying `.tfw/`, and verify HL §2.8's population of 19 rather than inheriting it.
- Record the *form* of each `TECH_DEBT.md`: flat table, sectioned tables, or prose; the column set; the identifier scheme.
- Look for counter-evidence to H1 **first**: a task in any receiving project whose scope came from a registry row rather than from the REVIEW that filed it.
- Read what the receiving projects' configs actually contain — specifically whether `tfw.task_containers`, the key H6's closure depends on, exists at their installed version.
- Read the TFW-60 field reports for what receiving projects did with prose instructions of this shape.

**Extract — build the configuration space of the retirement instruction.**
- Cross the dimensions Gather names: what the prose does to the file, where the sealed file goes, when relative to the 2.0.0 board migration, what happens to rows that are not debt, who decides, what replaces discovery.
- Surface combinations the HL has not considered, especially any that survive the "no per-row triage" constraint of A1.

**Challenge — argue the retirement is wrong, on this evidence.**
- Pairwise-eliminate incompatible alternatives.
- Build the strongest case that the registry is load-bearing somewhere, and see whether the evidence supports it.
- Stress the instruction against the receiving project least like this repository.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | Nothing consumes `TECH_DEBT.md` as a live list; no completed task's trace shows an item picked up **from the registry** rather than from its REVIEW | verify at TS — corpus half unverified |
| H3 | A receiving project can retire its own registry from prose alone, with no row lost | open — risk reduced by A1 |
| H6 | Where a receiver puts its snapshot: the last configured task container | closed 2026-09-01 by the owner — re-examined here only against receiving-project configs, not reopened |

> H2 (citation resolution) is a single-line check inside this repository and belongs to the TS, not
> to a pass whose declared subject is the receiving projects. H4 and H5 were struck by A1 and are
> not revived here.

## Scope Intent

- **In scope:** every project on this machine carrying `.tfw/`; the shape, identifier grammar and live content of their `TECH_DEBT.md`; their installed version and config keys; their task corpora as evidence for or against H1; `.tfw/migrations/2.0.0.md` as the text they will follow; the seven TFW-60 field reports.
- **Out of scope:** this repository's own 121 rows. A1 forbids reading them to score them, and the census below never opens them for triage. Also out: the HL's frozen sections, the TS, and any per-row judgement anywhere.

## Guiding Questions

> The owner asked for no questions this pass. These are the three the researcher answers for
> themself, and the answers are recorded at each checkpoint.

1. Is the population really 19, and does the form of these files admit a single retirement prose?
2. Does H1 survive contact with the receiving projects, or is there a counter-example?
3. What does the retirement or the update path have to account for that HL §2 does not already name?

## User Direction

- 2026-09-01, owner: run this pass without questions. Recorded as the run condition above.
- Standing constraint from A1: the retirement reads no row and judges no row. This briefing inherits it.

---
Stage complete: YES
