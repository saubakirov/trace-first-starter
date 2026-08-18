# PROPOSAL — TFW-59: North Star Lifecycle — who designates it, where it lives, who asks

> **Date**: 2026-08-18
> **Author**: Coordinator (Claude Code)
> **Status**: 📋 PROPOSAL — not chartered, no HL
> **Origin**: owner observation 2026-08-18, after closing TFW-53
> **Sequenced after**: TFW-55 amendment A2 (the *designation* for this repository) — this proposal is the *mechanism*, and the two are different problems

---

## 1. The observation

TFW-53 Phase C shipped the **Project North Star** as a concept and gave it everything except a life.
It has a definition, seven rules, a glossary article, a PV priority, a template field and a place in the
reviewer's reference set — and no answer to *who writes it, when, where it is recorded once, and who
notices it is missing.*

The owner's words, 2026-08-18: *«непонятно куда что когда писать. и кто-то должен спросить, но
координатор не спрашивает — его вообще не парит, что его нет»*.

## 2. Measured, not asserted

| # | Measurement | Command / source | Result |
|---|-------------|------------------|--------|
| 1 | Does any workflow tell a coordinator to establish a north star? | `grep -i "north star" .tfw/workflows/plan.md` | **0** |
| 2 | Does initialization ask a new project for one? | `grep -i "north star" .tfw/workflows/init.md` | **0** |
| 3 | Is there a project-level carrier? | `grep -i north .tfw/project_config.yaml .tfw/templates/project_config.yaml` | **0** — no key |
| 4 | What is the only carrier? | `templates/HL.md`:18 | A **per-task** header field, retyped by every HL, with nothing checking that two HLs name the same locus |
| 5 | Does anything detect its absence? | `review.md`, `judge.md` | The fallback is correct and silent. `⚪ N/A` is permitted, a review is *never* blocked — by design (rule 5) — so absence produces **no signal at all** |
| 6 | Did the gap actually bite? | `HL-TFW-54`:12, :485, :518 | The coordinator recorded `N/A — no project north star designated` **three times**, ruled it *not a blocker*, and routed the designation to TFW-55 |
| 7 | Did the receiving contract accept it? | `grep -i "north star" HL-TFW-55…md` | **One hit**, the header phrase *"North-star role"* — a metaphor for that task's foundational role, **not** the `conventions.md` §3 concept. TFW-55's frozen DoD says nothing about a designation |
| 8 | Does the content exist? | `grep -i "non-goal" README.md .tfw/README.md` | **0**. Rule 3 makes non-goals mandatory; this repository has none |

**The shape of the defect.** Nothing misbehaved. The coordinator noticed, wrote the field honestly,
applied the correct fallback and routed the work — and the routing landed on a contract that never
accepted it, because no rule says who may accept it. **A responsibility that belongs to no role is
discharged by everyone writing `N/A` and moving on.** Rule 5's *"a review is never blocked on a missing
north star"* is right for review and, without a counterpart elsewhere, it means the absence is never
raised by anyone at any point in the lifecycle.

## 3. Why it matters, in one sentence each

- **The fallback is not equivalent.** §1 Vision at the contract baseline states what a *task* is for. It
  catches a result that contradicts the goal; it cannot catch **excess**, and rule 3 says excess is what
  this layer exists to catch.
- **Excess is TFW-54's first failure mode.** A coordinator releasing a team of delegate sessions is the
  case where excess is cheapest to produce and slowest to notice.
- **Per-HL retyping drifts.** The one carrier is a free-text field in every HL. Two tasks naming different
  sections is undetectable today, and that is the same defect class as the pre-TFW-53 HL: a claim with no
  single place it lives.

## 4. Design sketch — recorded, not decided

Four questions the task would answer. The sketch is a starting point, not a ruling.

| Question | Sketch |
|----------|--------|
| **Where is it recorded once?** | A project-level carrier so the locus is declared one time and every HL cites it rather than restating it. Candidate: a `tfw.north_star` key listing sections, propagated through `workflows/config.md`'s Config Sync Registry like every other parameter. The HL field then becomes a citation, not a source |
| **Who writes it, and when?** | `init.md` asks at initialization — it already interviews for project context, and this is the one question that establishes what the product is for. For an existing project without one, `/tfw-config` or a `/tfw-plan` step raises it **once**, not per task |
| **Who notices it is missing?** | Not the reviewer — rule 5 is deliberate and should stand. A coordinator-side prompt is the natural home: the role that writes the HL header field is the role that should be made to ask rather than to type `N/A`. Open question: a hard gate reproduces the interruption the owner refuses (`stakeholder.md` F6), so this is probably a one-time ask with a recorded declination |
| **How does a task hand designation work to another task?** | The TFW-54 → TFW-55 routing failed silently because a frozen contract cannot receive scope by being named from outside. The general rule is small: work routed into a frozen contract enters through that contract's §12, or it has not been routed |

## 5. Scope boundary

**In:** the lifecycle — carrier, authoring moment, the asking role, cross-task routing into a frozen contract.

**Out:** writing *this* repository's north star and its non-goals. That is content, it belongs to the task
that owns both README surfaces, and it is filed as **TFW-55 amendment A2**, awaiting the owner's verdict.
Shipping the mechanism and the content together would repeat the coupling that TFW-53 deliberately split
across its own phases.

**Also out:** changing rule 5. A review is never blocked on a missing north star, and that stays.

## 6. Cost of not doing it

Every project on TFW — including this one — runs its Purpose Check on a reference set that answers *what
was this task for* and never *what is this product for*. The check still fires and still cites, so the
gap is invisible in exactly the way `philosophy.md` **F39** describes: a citation that resolves is not a
citation that is relevant. The precedent is not hypothetical — `process.md` **F30** records that this
project wrote down the coordinator-drift failure in April 2026, built no enforcement site, and paid
27,103 deleted lines for it.

---

*PROPOSAL — TFW-59: North Star Lifecycle | 2026-08-18*
