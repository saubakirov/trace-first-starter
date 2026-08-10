# Briefing — "What should we investigate?"

> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-53](../../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN, baseline re-frozen after A1–A5 (`d9a4c57`)
> Goal: An approved HL is a contract, and the reviewer is its defender — review asks "is this what we set out to do?" against a north star that sits above the task.
> Predecessor: [`research/iter1/RES.md`](../iter1/RES.md) — decisions D1–D14 constrain this iteration.
> **Mode:** Pipeline · deep (`loops_per_stage: 3`, counter-evidence required) · autonomous run, gates disabled by owner directive
> (*«tfw-53 автономно без вопросов deep mode iter 2»*)

---

## Predecessor Context (iteration 1)

Iteration 1 priced the freeze and redesigned its granularity. What it hands to this iteration:

| Constraint from iter1 | Effect on iteration 2 |
|---|---|
| **D2/D4** — the frozen unit is the *declarative claim*, not the section text | The goal check measures against declarative claims, not against section prose. A wording delta is not a goal failure by construction |
| **D5/D6** — contract baseline = header + §12 + a reserved `[agent/TFW-NN/freeze/coordinator]` commit | The goal check's reference set is *retrievable*: `git log --grep='/freeze/'` gives the reviewer the exact approved text |
| **D10** — Phase HL becomes derivation-only (A1 approved) | The goal check must **exclude** the phase HL from its reference set. TFW-48 proves why: master P7 did not survive into the phase HL its reviewers checked against |
| **D11** — `❌ REJECT` branch (a) redefined as *file an amendment* (A5 approved) | Any new verdict class must compose with the amendment protocol, not around it |
| **D8/D9** — `Type` column, `APPLIED — restrictive` (A2 approved) | Precedent that a verdict vocabulary carries consequences, and that the type must be visible at ruling time rather than reconstructed from prose |
| **Open thread 3** — salami residual, unresolved | Carried here as (f3): does a `git diff` against the freeze baseline at the pre-TS gate cost anything? |

Also inherited: **SS1** — the owner's interruption budget is spent on *frequency*, not on *authority*. A goal check that fires
often is not a cheap check; the design's success metric is signal-per-fire.

## Research Plan

### Gather — "What do we NOT know?"
- Measure the review surface directly: how much purpose vocabulary exists in `review.md`, the three stage templates and
  the three mode files today. Word-level, not impressionistic.
- Resolve H12 mechanically: which file does PV Index priority 1 ("README Values") actually resolve to, in TFW and in a
  second real TFW project (AFD). Compare the two READMEs byte-for-byte where they overlap.
- Measure H13: the reviewer-relevant fraction of AFD's 509-line north-star anchor, by section and line count.
- Recover the negative-control corpus: the TFW-48/49 phase REVIEWs at `721ca15`, their verdicts, and the master HL text
  they should have been measured against (`9e19a4f` for TFW-49).
- Decompose the problem into independent Dimensions — anchor locus, payload, obligation, forcing-function form,
  verdict class, materiality mechanism, reference set. Each must carry ≥3 alternatives with none marked preferred.
- External: standards-grade vocabulary for the "built the right thing" axis, and evidence on what makes a review gate
  degrade into a rubber stamp.

### Extract — "What do we NOT see?"
- Build the Configuration Space across those dimensions; keep every combination that is not obviously contradictory.
- Cross-reference AFD's three concurrent `P{n}` namespaces against the owner's own directive to test DoD-24's premise.
- Model what each configuration costs a *small* project — the H12 adoption-tax question stated as a number, not a worry.
- Locate the retention failures: rules this framework already wrote and already lost (D46's "not rubber stamp",
  TFW-48's DoD-11/P7). If the pattern is retention rather than invention, the design target changes.

### Challenge — "What do we NOT expect?"
- Pairwise consistency across the dimensions; eliminate the incompatible combinations and name why.
- **The replay (HL DoD-26).** Run the drafted check against six TFW-48/49 phase REVIEWs (seven verdicts) and against
  three TFW reviews that were genuinely sound. Required outcome: ≥1 non-approve on the former, 0 on the latter.
- The hardest negative control (f2): TFW-48's approved master **already carried** DoD-11 and P7 goal defence and lost
  both. Would the drafted check have fired *given that the master already demanded it*? A check that would not fire here
  is not a check.
- Attack the verdict vocabulary: does each candidate term survive translation out of software, and does it collide with
  a term the framework already uses?
- Counter-evidence duty (deep mode): actively look for the reading under which the north star is unnecessary, the
  forcing function is ceremony, and the check should not ship.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H11 | The forcing function — the reviewer must quote the north-star clause the work serves — is what separates a live check from a rubber stamp. Without it the honest answer is "aligned" ~145 times out of 149 and the check decays within a few tasks | open |
| H12 | The project north star is the **root `README.md`**, and no new file is needed. Corollary: PV Index priority 1 "README Values" resolves to `.tfw/README.md` — methodology values identical in every project — not to project purpose. If so, priority 1 is misnamed in every TFW project | open — owner's instinct, needs verification |
| H13 | A one-page north-star payload is sufficient for review purposes; AFD's 509-line anchor is ~41 reviewer-relevant lines, so the framework must not mandate the larger form | open |

Not re-litigated (settled upstream, per `iterations.yaml`): H2, H7, H8, H9, H10.
Resolved in iteration 1 and treated as constraints, not questions: H1, H3, H6.

## Scope Intent

- **In scope:** the north-star anchor (locus, payload, obligation); the substantive goal check in Judge and its three
  mandatory clauses; the verdict vocabulary for a goal failure and its finding; the reference set the check reads;
  the `P{n}` namespace guard; the DoD-26 replay validation; the salami residual (f3) as a cost question only.
- **Out of scope:** anything in Phase A/B enforcement mechanics already decided by iteration 1; the AT execution mode
  (TFW-54, DoF-4); a TS→HL traceability gate (owner ruled out, DoF-6); Phase E trace restoration (needs no research);
  re-opening H8's "not a fifth stage" ruling — the owner's ruling on form is a dependency, not a research question.
- **Explicitly not written by this role:** HL, TS, code. Findings that touch frozen sections leave here as Amendment
  Proposals, per the mechanism this task is building and which its own HL header applies.

## Guiding Questions

> Owner directed an autonomous run. These are recorded, answered from evidence where possible, and routed to the
> coordinator in RES § Open Questions where they need a verdict.

1. If PV priority 1 is misnamed in every TFW project (H12 corollary), is correcting it inside TFW-53's scope, or is it a
   separate defect that this task merely discovered?
2. Must a project have a north star before it can run a review — or does the check degrade gracefully to the master HL
   §1 when no anchor is designated?
3. Does a goal failure deserve a verdict name distinct from `❌ REJECT`, given that the board must distinguish "built
   wrong" from "built the wrong thing" — and given that A5 already redefined REJECT's branch (a)?

## User Direction

- Run autonomously, deep mode, no interactive gates (owner, 2026-08-08). All four 🛑 WAIT gates are executed as
  self-checkpoints and recorded in the stage files.
- Iteration 1's five amendment proposals were ruled on before this iteration started — all five APPROVED, applied, and
  re-frozen. This iteration therefore runs against an amended contract, and the amendment protocol has now been
  exercised once end-to-end on the task that invents it.
- Owner instinct on record (S26): *«по идее сам ридми должен быть им»* and *«у нас тут есть два readme… кто из них
  является north-star?»* — H12 exists because the owner asked this question, and it is the highest-value item here.

---
Stage complete: YES
