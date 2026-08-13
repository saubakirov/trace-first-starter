# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-56](../../HL-TFW-56__review_mode_removal.md)
> Goal: Review stops asking which kind of review this is — the `code / docs / spec` axis is deleted and the two checks inside it that ever carried signal are promoted into the universal checklist.

> **Iteration:** 1 of 1 (coordinator override of `min_iterations: 2`, owner-approved 2026-08-13 — see `research/iterations.yaml`)
> **Mode:** focused (`loops_per_stage: 1`, verify user tech claims, no counter-evidence requirement)

---

## Pre-Briefing Reconnaissance

Three facts were established before writing this plan, because each one decides whether a planned
stage is feasible at all. They are recorded here as *inputs to the plan*, not as findings.

| # | Check | Result | Consequence for the plan |
|---|---|---|---|
| 1 | Does the external corpus named in HL §10 exist and carry the mechanism? | `ai-first-devices` (AFD) — **150** REVIEW files, **139** carrying a `Review Mode` header, `.tfw/workflows/review/{code,docs,spec}.md` present, `tfw.review.default_mode: code` | H3 is measurable this iteration. Sample is **7.7×** the local one (139 vs 18) |
| 2 | Are the review templates actually "byte-identical" (HL §10 claim)? | `.tfw/templates/review/judge.md` — **byte-identical** to this repo's. But AFD runs TFW **0.9.0** vs this repo's **1.0.0** | The mode mechanism replicates; the *surrounding* workflow may not. Version drift must be measured, not assumed — the claim is trusted only for `judge.md` until Gather checks the rest |
| 3 | Is a third, non-AFD corpus available? | `helpdesk` — **71** REVIEW files, **55** carrying `Review Mode`, TFW **0.8.7**, same `default_mode: code` | A second replication is available cheaply. Whether to spend it is Guiding Question 3 |

**Combined mode-carrying corpus available: 139 (AFD) + 55 (helpdesk) + 18 (local) = 212 reviews**, against
the 18 the HL currently reasons from.

---

## Research Plan

### Stage 2 — Gather: decompose, then measure

The problem is not one question, it is six decision factors that have been arguing with each other
inside a single "should we delete it?" framing. Gather's first job is to separate them.

- **Decompose into dimensions before collecting anything.** Candidate independent dimensions:
  **(A) Row substance** — does a mode row express a check the universal set does not?
  **(B) Firing rate** — has that row ever produced a non-✅ in a real review?
  **(C) Priming** — does the *label* change reviewer behaviour beyond the rows it loads?
  **(D) Consumer coupling** — what else reads the key or the header, and what breaks on removal?
  **(E) Extension-point role** — is a mode file where a project puts its own checks?
  **(F) Corpus generality** — does the answer hold outside markdown-only framework work?
  Six ≥ 3, so Extract gets a real Configuration Space rather than a comparison matrix.
- **Measure AFD (H3).** For all 139 mode-carrying REVIEWs: mode distribution, every mode-specific
  row's status (✅ / ⚠️ / ❌ / N/A), and **every instance where a mode row drove a REVISE or REJECT
  verdict**. The last one is the decisive number — the HL's local finding is 0 blocks in 18 reviews.
- **Measure version drift, don't assume parity.** AFD is 0.9.0. Diff `review.md`, the three mode
  files and `templates/review/*` against this repo before treating AFD's numbers as replication.
  A different mechanism measured is not a replication.
- **Audit consumers (H4, H5).** `grep` `default_mode` / `Review Mode` / `workflows/review/` across
  `.tfw/`, adapters, entry points, `editions/`, any docs build, and both external projects. Then
  read `update.md`'s CONFIG-merge rules specifically for the **removed-key** case — the one failure
  mode that hits users rather than this repository.
- **Check whether anyone extended a mode file (H5).** Diff AFD's and helpdesk's three mode files
  against this repo's. A local edit is direct evidence of the extension-point role; three identical
  copies are evidence against it.

### Stage 3 — Extract: cross-reference into a configuration space

- **Coverage matrix (H1, H2):** 8 mode-specific rows × 7 universal rows, each cell
  *duplicate / partial / absent*. This either confirms the HL §3 three-survivor set
  (compatibility · traceability · safety) or corrects it — the HL is currently asserting it.
- **Cross the survivor set against dimension (B).** A row that is *absent* from the universal set
  but has **never fired in 212 reviews** is a candidate DoF-2 violation — promoting it would swap
  one rubber stamp for another. Absence-of-duplicate is not sufficient grounds for promotion.
- **Configuration Space:** the five design options × the six dimensions.
  Options: **delete** · **project-optional** (config-gated axis) · **non-gated descriptor**
  (no file, no key, one free-text line) · **extend** (prompt/design/architecture) · **multi-select**.
  Each cell: does this dimension support, oppose, or not constrain this option?
- **Surface the unexpected combinations.** The HL argues delete-vs-descriptor as a binary. The space
  should show whether any hybrid survives — e.g. delete the axis *and* the key, but keep genre as a
  derived label read from the TS rather than declared by the reviewer.
- **N/A grammar (F21):** for each promoted row, what does an honest N/A look like, and does the
  grammar make N/A a trace rather than a silent skip?

### Stage 4 — Challenge: attack H6 head-on

- **State the counter-argument in its strongest form first.** D28 ("naming creates behaviour") and
  the README value "Naming Creates Behaviour" both predict that removing a name removes a behaviour.
  This task proposes to remove a name. That is TFW's own doctrine pointed at this HL.
- **Find the observable signature of priming, if it exists.** Compare, within the 212-review corpus,
  reviews of comparable artifacts under different modes: does depth, file-open count, verdict
  distribution or Observations volume vary with the label after controlling for artifact type?
  Define the signature *before* looking, so the test can fail.
- **Test the null the other way.** The field already produced a `docs + code` header and an owner
  override — evidence that one label does not classify the work. If reviewers routinely override or
  compound the label, the label is not priming them; they are priming it.
- **Pairwise-eliminate the surviving configurations** from Extract. The output is not "delete wins"
  but *which configurations survive and on what evidence*, plus the trigger that would flip the
  recommendation to the H6 fallback (non-gated descriptor).
- **Name what this iteration cannot settle.** Dimension (F) — non-code, non-software domains — has
  no corpus anywhere available. That gap goes into the Iteration Status block as an open thread, not
  into a conclusion.

---

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | Stage that carries it | What closes it |
|---|-----------|-----------|----------------------|----------------|
| H1 | The eight mode rows contain exactly three checks absent from the universal set — backward compatibility, source traceability, safety — and the other five are synonyms of universal rows or already mandated elsewhere | open | Extract | The 8×7 coverage matrix, cell by cell |
| H2 | No verify action is lost by deleting the mode files: `code`'s two distinctive actions are already unconditional in `verify.md` Checkpoint and the `review.md` Trust Protocol | open | Gather → Extract | Line-by-line read of the three mode files against `verify.md` + Trust Protocol |
| H3 | The finding replicates in AFD: mode-specific rows there also produce ~0 findings across ~149 reviews | open | Gather | Status distribution across 139 mode-carrying REVIEWs + count of mode-driven REVISE/REJECT |
| H4 | No consumer breaks: nothing outside the six identified files reads `default_mode` or the `Review Mode` header, and `update.md`'s CONFIG merge handles a removed framework key without corrupting an existing project's config | open | Gather | Exhaustive grep + read of `update.md` removed-key semantics |
| H5 | No project uses the mode files as an extension point for custom checks; a project needing extra checks can express them in `project_config.yaml` without a mode axis | open | Gather | Diff of mode files across three installs |
| H6 | The axis's value was in its **rows**, not in **priming** the reviewer — so removing the label does not degrade review behaviour. (D28 predicts the opposite; this is the hypothesis most likely to be refuted) | open | **Challenge** | Pre-declared behavioural signature, tested against the corpus. May not close — see Guiding Question 2 |

> **Filter — if false, would the approach change?** (from HL §10, unchanged)
> H1 false → more rows must be promoted; the §3 coverage table is wrong.
> H2 false → verify actions must be migrated into `verify.md`, not just deleted.
> H3 false → the axis works elsewhere; make it project-optional instead of removing it.
> H4 false → migration steps for existing projects, and `update.md` may need a change.
> H5 false → an extension slot is required and the design gains a component.
> H6 false → **do not delete the label.** Fall back to a non-gated descriptor.

---

## Scope Intent

**In scope**
- Empirical base rate of mode-specific rows across the AFD corpus (H3), and the local 18 re-verified
  rather than inherited from the HL.
- Version-drift check between AFD/helpdesk (0.9.0 / 0.8.7) and this repo (1.0.0), limited to the
  review surface — enough to know whether the measurement is a replication.
- Full consumer audit of `tfw.review.default_mode` and the `Review Mode` header, including
  `update.md`'s removed-key CONFIG-merge semantics (H4) and the mode-file-as-extension-point
  question (H5).
- The 8×7 coverage matrix and the survivor set, tested against firing rate, not just against
  duplication (H1, H2).
- H6: whether the label primed the reviewer, and what the fallback trigger is.

**Out of scope**
- Writing HL, TS, or any implementation. Role lock: researcher.
- Editing this repo's `.tfw/` or either external project. Both external corpora are **read-only**.
- The TFW-53 Phase C sequencing decision (HL §8) — that is a coordinator call at TS time, informed
  by this research but not made here.
- The TFW-45 consolidator / subagent re-architecture (owner-split, HL header).
- Rewriting history: existing REVIEW files in any corpus are evidence, never edited.
- Non-software, non-framework domain corpora (analytics, curriculum, business process) — **none
  exists in reach**. This is a named blind spot carried to Iteration Status, not silently dropped.

---

## Guiding Questions

1. **Corpus validity.** AFD runs TFW **0.9.0**, helpdesk **0.8.7**, this repo **1.0.0** — `judge.md`
   is byte-identical across them, but the surrounding review workflow may have moved. Do you want
   the AFD measurement (a) taken at face value as replication, or (b) gated on a drift check of the
   review surface first, with reviews written under a materially different mechanism excluded?
   *(b) costs one extra Gather step and is what I'd recommend — an unqualified 139-review number
   that turns out to measure a different mechanism is worse than no external number.*

2. **How far must H6 go?** Priming cannot be A/B-tested here — no experiment is available, only
   observation of reviews that already happened. I can (a) pre-declare a behavioural signature and
   test it observationally, accepting that a null result is weak evidence, or (b) treat H6 as
   unclosable by observation and go straight to the decision it forces: *is the H6 fallback
   (non-gated descriptor) cheap enough that we adopt it as insurance regardless of the evidence?*
   The HL treats H6 as the hypothesis most likely to be refuted, so this choice decides whether
   iteration 2 is needed.

3. **Second replication.** `helpdesk` offers 55 more mode-carrying reviews for roughly the cost of
   re-running the same extraction. Include it, or is AFD's 139 enough for a focused iteration?

---

## User Direction

**Owner, 2026-08-13 (briefing gate):**

| Q | Answer | Effect on the plan |
|---|--------|--------------------|
| 1 — Corpus validity | **(b)** — gate the AFD measurement on a drift check first | Gather runs the review-surface diff **before** the extraction. Reviews written under a materially different mechanism are excluded or flagged |
| 2 — How far must H6 go | **Researcher's call** | Decided: **(a) + (b) together.** A behavioural signature is pre-declared and tested observationally against the full corpus, *and* Challenge answers the decision H6 forces regardless of the result — because a null from observation is weak evidence and must not be reported as a pass. Rationale recorded in `4_challenge.md` |
| 3 — Second replication | **Include `helpdesk`** (`D:\projects\research\helpdesk`) | Corpus becomes 139 (AFD) + 55 (helpdesk) + 18 (local) = **212** mode-carrying reviews across **three** TFW versions |

**Execution mode:** owner granted autonomous run — *"no questions to me now, auto mode till research end."*
Stages 2-4 run without WAIT gates. The ≤3-questions rule is suspended by owner instruction; open
questions are recorded in the RES Iteration Status block instead of being asked mid-stage.

---
Stage complete: YES
