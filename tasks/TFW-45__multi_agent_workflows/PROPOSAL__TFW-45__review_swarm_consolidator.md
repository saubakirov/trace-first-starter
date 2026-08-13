# PROPOSAL — TFW-45 addendum: Review as Consolidator + Delegated Auditors

> **Date**: 2026-08-13
> **Author**: Coordinator (Claude Code)
> **Status**: ❄️ Addendum to a FROZEN task. Not a plan. Entry point when TFW-45 thaws: `/tfw-plan`.
> **Target**: [TFW-45](HL-TFW-45__multi_agent_workflows.md) Phase B (Review Swarm) — the HL is **not edited**; this file carries the newer design
> **Sequencing constraint**: [TFW-53](../TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md) Phase C — see § Collision with a frozen contract
> **Sibling**: [TFW-56](../TFW-56__review_mode_removal/HL-TFW-56__review_mode_removal.md) removes the `code/docs/spec` mode axis and frees the term "review mode"

---

## Why this file exists

Owner session 2026-08-13 opened three questions about review at once: are the `code/docs/spec`
modes worth their gate, is the four-stage sequence worth its cost when **one** agent runs all of it,
and should the main agent become a *review consolidator* holding goal and value defence while the
rest runs as subagents with their own system prompts and mentality.

Owner decision the same session: **the mode question ships alone** as [TFW-56](../TFW-56__review_mode_removal/HL-TFW-56__review_mode_removal.md).
The subagent question belongs to TFW-45, which already owns it — so the analysis lands here rather
than evaporating.

> *«хорошо, тогда докидай пропоузал в 45 и свои мысли. здесь оставим только удаление режимов»*

TFW-45's HL was written 2026-06-15 and its review half (Phase B) is three lines long:
*"Review swarm mode integration (likely `review/swarm.md`), `review.md` Step 1 update, system prompt
composition rules for Map/Verify/Judge stage agents."* Everything below is newer than that, and two
items **contradict** it. Nothing here is approved.

## The owner's design

> Main agent = **review consolidator**, carrying goal defence, value defence "and something else".
> The remaining work runs as subagents — sequentially or in parallel, where available — each with a
> concrete system prompt and its own mentality.

This is the same instinct as TFW-45's original review swarm, with one structural addition the
original does not have: the coordinator is no longer just a *synthesizer of stage files*. It holds a
**check of its own** that is not delegable. That changes the decomposition, not just the execution
model.

## Thought 1 — the current stage set is the wrong thing to delegate

TFW-45 §3.1 sketches `map_reviewer` → `verify_reviewer` → `judge_reviewer` + coordinator writes
REVIEW. That is a 1:1 lift of today's stages into subagents. Delegability is not uniform across them:

| Stage | Delegable? | Why |
|---|---|---|
| **Verify** | Best candidate | Mechanical, by far the most token-expensive (see measurement below), output is a table the consolidator can re-check against the files. Fresh context is an advantage: a verifier that never read the RF's *framing* is harder to persuade |
| **Map** | Cheap, yes | Comprehension; output is consumed structurally by later stages |
| **Judge** | Worst candidate | To rule, it needs the whole reference set — and the reference set is precisely the consolidator's asset |
| **Purpose / goal defence** | **No** | See Thought 2 |

Measurement, TFW-53 Phase A review (the most recent complete review in this repo):

| Artifact | Lines | Share |
|---|---|---|
| `review/map.md` | 88 | 26% |
| `review/verify.md` | **179** | **52%** |
| `review/judge.md` | 76 | 22% |
| → `REVIEW__phase-a__*.md` (synthesis of the above) | 198 | — |

So ~540 lines are written to deliver one verdict, and the majority of genuine work sits in one
stage. If delegation is about offloading token-heavy mechanical work onto a fresh context, the
honest design is **not** three symmetrical stage agents. It is a consolidator plus one or more
auditors, with Map folded in or delegated as a cheap prelude.

**This contradicts TFW-45 Phase B as written.** It should be treated as a re-decomposition, not as
"add a swarm mode file to the existing three stages".

## Thought 2 — goal defence cannot be delegated, and the reason is now formal

TFW-53 Phase C fixes the Purpose Check's reference set: **the master HL at its frozen baseline plus
the project north star**, and it declares the TS and any Phase HL *invalid* references (DoD-20). A
subagent handed `TS + RF` therefore **cannot** perform the check — not because it is less capable,
but because it was not given the only admissible reference. Two further properties point the same
way: the check's output is a *verdict*, not a document, and its scope is the whole result rather
than one dimension of it.

Owner's instinct — consolidator keeps goal defence — is therefore correct, and it now has a
structural argument rather than a stylistic one.

One honest counter-consideration, worth recording because it cuts the other way: the consolidator is
also the **most context-contaminated** agent in the run — it read everything, including the
executor's own framing. For a *critic* role that contamination is disqualifying. For the purpose
check it is less harmful (the check is anchored to an external, committed baseline, not to
independent judgement) — but "less harmful" is an assumption, not a measurement.

## Thought 3 — the value of staging splits in two, and only one half is proven

| Value | Status | Evidence |
|---|---|---|
| **Evidence trail** — stage files are the record that verification actually happened | **Proven, and independent of who writes them** | D41: single-pass review is trust-based with no trail. `verify.md` carries 52% of stage volume: opened files, executed commands, discrepancies. The artifact survives regardless of agent identity |
| **Genuine cognitive-mode separation** | **Unproven with a single agent** | TFW-45 §2 and S1 — the owner's own argument: one agent carrying the whole history "knows" what the previous stage found and builds on it. Performance, not a mode change |

And the sharpest datum, from TFW-53 research iter2: in AFD, `judge.md` returned **✅ on the very AC
that contained the violation** (`P8 → AC-B4 → ✅`), and the reviewer later retracted his own APPROVE.
Four stages did not catch it. What would have caught it is the reference set. TFW-53 HL §4 Phase C
ranks the levers explicitly: **reference-set rule > forcing function > `judge.md` row > identity
text.** Stage *count* is not on that list.

Implication for TFW-45: the swarm's justification must be stated as *evidence-trail quality* or
*independence of the auditor*, and never as "more stages = better review". The latter is
measurably false in this repository.

## Thought 4 — review can parallelize where research cannot

TFW-45 correctly refused to parallelize research: Extract without Gather Dimensions is garbage (S3).
Review is not the same shape. TFW-45's own table says *"Verify **benefits from** Map's
understanding"* — benefits, not requires. Verify's inputs (RF claims, TS acceptance criteria, the
files themselves) all exist at t0.

So `Map ∥ Verify` is genuinely available. But TFW-45 P1 is *quality over speed*, so parallelism must
be justified by something other than wall-clock — e.g. an auditor that is deliberately **blind** to
Map's narrative. That is a quality argument, and it is testable.

## Thought 5 — H1 was never tested, and the cheap harness now exists

H1 (*a fresh agent with Mindset as system prompt produces genuinely different output than one agent
switching modes mid-conversation*) is the whole justification for TFW-45, and it has never been run.
TFW-45's §10 filter says it plainly: *"H1 false → swarm mode has no quality advantage → entire task
loses primary justification."*

The negative controls did not exist in June 2026 and do now:

| Control | What it is | Where |
|---|---|---|
| TFW-48/49 REVIEWs | Seven verdicts, six ✅ APPROVE, on work the owner later rejected wholesale | `git show 721ca15:<path>` |
| The overwritten REVISE | One genuine 🔄 REVISE (7 of 10 Judge checks FAIL) overwritten three commits later | `1ebb680` |
| AFD-38/phase-b | ✅ APPROVE that the reviewer himself retracted | AFD repo |
| AFD-48/phase-b | The false-positive precedent — a goal-based REVISE demoted after owner challenge | AFD repo |

And TFW-53 **DoD-29 already mandates a replay validation** of the Purpose Check against exactly the
first two. One harness serves both questions. Running TFW-45's H1 on the same corpus costs the
marginal run, not a new experiment.

**Recommendation:** do not ship a swarm mode on design reasoning alone. It is the one hypothesis in
this repository that is both load-bearing and cheap to test, and TFW-53 is already paying for the
stand.

## Collision with a frozen contract — the reason sequencing matters

TFW-53's DoD are **frozen**, and they nail the Purpose Check to one file:

| Frozen item | What it fixes |
|---|---|
| DoD-20 / 21 / 22 / 23 | The substantive Purpose Check, its citation-and-harm field, its excess test and its third outcome live in `templates/review/judge.md` |
| DoD-28 | Justifies that site explicitly: the rules land in `judge.md` *"which is a template and not a workflow"*, keeping `review.md` inside the F2 word budget |
| HL §4 Phase C | *"Enforcement site — `templates/review/judge.md`, and it is the only one"* |

If Judge becomes a **delegated** subagent while goal defence stays with the consolidator, the
enforcement site is wrong: the rule would sit in the prompt of the one agent that must not own it.
Three ways out, in preference order:

| # | Path | Cost |
|---|---|---|
| **ii** | Ship TFW-53 Phase C as frozen, then amend §4/§5 through **§12 Amendment Log** when this work is planned | One logged, evidenced, ruled amendment — and it dogfoods the mechanism TFW-53 exists to build |
| i | Ship C, then rework judge.md silently in this task | Rework in the same file, and no visible record of why the site moved |
| iii | Absorb this work into Phase C | C is already 🔴 and carries 12 DoD items; this is the scope inflation TFW-53 was written to prevent |

Either way: **TFW-53 Phase C lands first.** This work is downstream of it, not parallel to it.

## What TFW-56 changes for this task

[TFW-56](../TFW-56__review_mode_removal/HL-TFW-56__review_mode_removal.md) deletes the
`code/docs/spec` axis. Two consequences here:

1. **Smaller surface.** `review.md` loses a step and its WAIT gate; `judge.md` loses its
   Mode-Specific section; three mode files disappear. A swarm redesign touches less.
2. **The term is freed.** Today "review mode" means `code/docs/spec`. After TFW-56 nothing holds
   the name. If swarm ships as a mode, the word must carry exactly one meaning (D28: one name = one
   behaviour) — and TFW-45 H8 already doubted that "mode file" is even the right abstraction for an
   execution model, as opposed to a parameter set.

## Open questions this addendum adds

| # | Question |
|---|----------|
| Q1 | Is the target *consolidator + N auditors* (a re-decomposition) or *the existing 4 stages, delegated* (TFW-45 Phase B as written)? These are different tasks |
| Q2 | Does Map survive as its own artifact, or fold into Verify's preamble? 26% of stage volume, and its consumer is the next stage rather than the owner |
| Q3 | Where does the Purpose Check live once Judge is delegated — `templates/REVIEW.md`, a new consolidator-owned stage file, or the workflow itself? DoD-28's word-budget argument must be re-answered, not ignored |
| Q4 | Does an auditor deliberately **blind** to Map produce better verification than one primed by it? This is the parallelism question stated as a quality question |
| Q5 | Degradation contract: what exactly does a tool without spawn run? TFW-45 DoD-5 demands zero regression for single-agent users, and that promise now has to cover a re-decomposition, not just a mode switch |
| Q6 | Does the consolidator's context contamination hurt the purpose check? Assumed harmless in Thought 2 — unmeasured |

## Hypotheses added to TFW-45's set

| # | Hypothesis |
|---|-----------|
| H10 | The delegable work is asymmetric: Verify carries the majority of mechanical volume, Judge and the purpose check are not honestly delegable, so a consolidator + auditor topology beats a 1:1 stage-to-subagent lift |
| H11 | A subagent given only `TS + RF` structurally cannot perform the Purpose Check, because TFW-53 DoD-20 makes both invalid references — so goal defence stays with the consolidator by construction, not by preference |
| H12 | `Map ∥ Verify` is safe in review (unlike Gather → Extract in research), and a Map-blind auditor produces *better* verification, not merely faster |
| H13 | The consolidator's full-context contamination is acceptable for the purpose check specifically, because the check is anchored to an external committed baseline rather than to independent judgement |
| H14 | The stage-file evidence trail (D41) retains its full value under delegation — the artifact matters, the author does not |

## Strategic insights carried over

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S9 | Owner separates the two review questions deliberately: mode deletion ships alone and immediately; the subagent re-architecture waits. Small reversible cleanup is not held hostage to a large unproven redesign | process | User, 2026-08-13 |
| S10 | Owner's consolidator formulation places goal and value defence at the top of the review, not inside a stage: *«основному быть агентом ревью-консолидатором с защитой целей ценностей»*. That is an ordering claim — the purpose check outranks the quality checks, rather than sitting beside them | philosophy | User, 2026-08-13 |
| S11 | Owner explicitly does not want subagents forced: *«мы не форсируем использование субагентов»*. So the design must be genuinely optional, and the single-agent path stays a first-class citizen rather than a degraded fallback | constraint | User, 2026-08-13 |
| S12 | Owner's phrasing — *«с конкретными системным промптом и ментальностью»* — keeps the June 2026 premise intact: identity via system prompt, not instruction. The premise is unchanged and still untested (H1) | philosophy | User, 2026-08-13 |

## Prerequisite

Do not start before **TFW-53 Phase C** is complete, and read [TFW-56](../TFW-56__review_mode_removal/HL-TFW-56__review_mode_removal.md)'s
RF first — both change the files this work would touch. Running before either means designing a
swarm around a review flow that is about to change twice.

---

*PROPOSAL — TFW-45 addendum: Review as Consolidator + Delegated Auditors | 2026-08-13*
