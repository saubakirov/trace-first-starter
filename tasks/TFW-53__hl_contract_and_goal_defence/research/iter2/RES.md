# RES — TFW-53: Goal Defence in Review (Iteration 2)

> **Date**: 2026-08-08
> **Author**: Researcher (Claude Code, separate session)
> **Status**: 🔬 RES — Iteration 2 complete
> **Parent HL**: [HL-TFW-53](../../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN, re-frozen after A1–A5 (`d9a4c57`)
> **Predecessor**: [RES iteration 1](../iter1/RES.md) — decisions D1–D14 constrain this iteration
> **Mode**: Pipeline · deep (`loops_per_stage: 3`, counter-evidence required) · autonomous run, no interactive gates

---

## Research Context

Iteration 1 priced the freeze and fixed its granularity. Iteration 2 builds the other half of the task: the defender.
Three hypotheses were open — whether a citation requirement is what keeps a goal check alive (H11), whether the project
north star is the root `README.md` and needs no new artifact (H12), and what the minimum reviewer-relevant payload is
(H13) — alongside an unresolved verdict vocabulary and a mandatory falsifiable acceptance gate (HL DoD-26): the drafted
check must produce at least one non-approve when replayed against the TFW-48/49 phase REVIEWs, and none against three
reviews that were genuinely sound. The corpus is unusually good for this: two projects, 155 review files, one documented
27,103-line failure with every artifact recoverable from git, and one project where the practice already works and has
already misfired once in each direction.

## Briefing

[`1_briefing.md`](1_briefing.md). Stage files: [`2_gather.md`](2_gather.md) · [`3_extract.md`](3_extract.md) ·
[`4_challenge.md`](4_challenge.md).

Run executed autonomously on owner instruction (*«tfw-53 автономно без вопросов deep mode iter 2»*). All four 🛑 WAIT
gates were executed as self-checkpoints; questions that would have been asked are in Open Questions below.

## Decisions

> Continuing iteration 1's numbering (D1–D14).

| # | Decision | Rationale |
|---|----------|-----------|
| **D15** | **The reference set is the master HL at its frozen baseline plus the project north star. The Phase HL and the TS are explicitly invalid references** | Settles open thread f1. A1 makes the Phase HL derivation-only, so it holds nothing approved to measure against; Principle 16 forbids the TS. TFW-48 is the proof: master P7 *"Independent Review Protects the North Star"* was live and approved, and invisible at the point of use because the reviewers read a Phase HL that had dropped it (Challenge C4) |
| **D16** | **The check has three tests — (a) citation, (b) excess/adjacency, (c) deferral confession — and (b) is the discriminating one** | The replay is decisive: citation alone would have **approved** TFW-49 Phase C, because approved DoD-3/DoD-5 make a validator and installable enforcement citable. What blocks it is excess against the phase's declared outcome (*"safely bypass"* → two-hook runtime + private ledger + carrier) plus a named DoF hit. A check shipping (a) without (b) reproduces the failure it exists to prevent (Challenge C2) |
| **D17** | **The forcing function and the materiality bar are one field, not two clauses: quote the clause **and** name the concrete harm** | Fusing them closes the hole neither closes alone. A citation that resolves but is irrelevant passes the forcing function; a harm asserted without a citation passes nothing. One sentence carrying both means a reviewer who cannot name a harm has failed materiality, and one who cannot quote a clause has failed the citation requirement (Extract E4, Challenge C1) |
| **D18** | **No new verdict token. `❌ REJECT` is reused; the name lands on the *finding* — `not fit for purpose` — with mandatory owner routing** | DoD-22 already fixed reuse. A fourth verdict collides with Phase E's concurrent `❌ REJECTED` *status* (two new `❌` tokens in one release = the D17 confusion pattern). Putting the name on the finding is the same move A2 made for §12's `Type` column: the classification is visible at ruling time instead of reconstructed from prose (Extract E5) |
| **D19** | **The check needs a third outcome: *the reference set is internally inconsistent* — routed to the owner as a contract defect, not a work defect** | The most consequential counter-finding of this iteration. TFW-49's approved contract contradicted itself — §1 *"readable without special tooling"* / *"provenance, not decoration"* against DoD-3 *"a versioned structural validator"*, DoD-7 *"repository fixtures"* and DoF-8 making prose-only enforcement a failure. Against a contradictory reference set the same evidence yields a defensible fire and a defensible pass, and the verdict becomes a coin flip wearing citations. Without this outcome the first contradictory HL produces a false REJECT and the check loses credibility on its debut (Challenge C2, C5-iv) |
| **D20** | **North-star locus: a designated section of the root `README.md`. Payload: purpose + principles + **non-goals**** | H12's substance holds — both projects' root READMEs already answer the question (AFD's `## Проблема` / `## Цель`) and neither needs a new file. Non-goals are mandatory because the corpus failure mode is *excess*, not opposition: TFW-49 Phase C did not contradict *"provenance, not decoration"*, it exceeded it. A purpose statement alone cannot catch excess (Gather G2, Extract E3, G13) |
| **D21** | **Anchor obligation: a declared fallback chain — project north star → master HL §1 at the frozen baseline. The absence of a north star never blocks a review** | Keeps DoD-17/18 satisfied (the PV priority and the header field both exist) while making the framework adoptable on upgrade day for every project that has no anchor yet. Also honest about weight: Extract E1 shows the reference-set *rule*, not the anchor artifact, is what would have exposed TFW-49 Phase C — the anchor covers the rarer case where a task's own approved HL is wrong for the product |
| **D22** | **Admission criteria for north-star clauses:** a clause states what the product **is for** or **must never become**. If a single task's implementation choice could satisfy or violate it, it is a principle (HL §7), not a north star | Size caps do not solve the real problem. AFD's anchor mixes *AI-first* with *GPS Kalman filter*; under a citation requirement the reviewer can satisfy the rule forever by quoting the Kalman clause. Applying this test to AFD's 14 principles leaves 4–6 — an independent route to H13's one-page estimate (Gather G3b, Extract E3) |
| **D23** | **Not the nominated-HL locus, unless *nominated-and-frozen*** | Designating a task HL as north star promotes a task contract to project authority with no gate at the promotion point, and imports the drift problem one level up. AFD's anchor grew from 10 to 14 principles after approval with six unlogged `(Added…)` markers and two inline "scope additions" blocks. If the owner wants this locus, it needs a project-level freeze mechanism TFW-53 has not scoped (Extract E2) |
| **D24** | **Citation namespace: `NS{n}` for north-star clauses, `PP{n}` for `KNOWLEDGE.md` §0, `P{n}` unchanged for HL §7** | DoD-24's premise is understated. AFD has three live `P8`s, and the project's own most load-bearing review rule cites the *task-scoped* one while appealing to a "single-registry north-star" that carries no number anywhere. Once every review must produce a principle citation, the collision rate goes from occasional to once per review. `P{n}` stays as-is — renaming it would touch every HL and TS §3 in both projects for no gain (Gather G6, Extract E6) |
| **D25** | **Vocabulary: `Project North Star` · `Purpose Check` · `not fit for purpose` · `deferral confession` · `NS{n}`** | Survivors of a three-way test (de-domaining per F13, collision inside `.tfw/`, behavioural read per D28). `Validation` is rejected as a label despite being the IEEE 1012 standard term — `verify.md` already performs verification in the strict sense, and "validator" was TFW-49's own linter. `Hotfix, not investment` is rejected as software-only. `Not fit for purpose` comes from UK gate-review and contract-law usage and works for a report, a curriculum or a business process (Challenge C6) |
| **D26** | **PV Index: add priority 0 *and* relabel priority 1** to `.tfw/README.md § Values and Principles` — *methodology* values | H12's corollary is confirmed mechanically and is worse than stated: priority 1 does not merely resolve to the wrong file, it resolves to a section that is **byte-identical across projects** (verified by `diff` between TFW and AFD). A "Project Value" source with the same bytes in every project carries zero project information by construction. Leaving the label as-is while adding priority 0 ships a table that invites the exact confusion the owner asked about (Gather G2, Extract E9) |
| **D27** | **The salami check (open thread f3) costs one command and should be a pre-TS gate, decided at Phase A/B TS time** | `git diff $(git log --grep="/TFW-NN/freeze/" -1 --format=%H) -- <HL>` — no new artifact, no new file, output already in the coordinator's native format. It would have fired on TFW-49 (`642c647` is `+167/−117` against the approved baseline) and could not have fired on TFW-48, whose pre-amendment HL was never committed — the hole DoD-5 already closes. Complementary to what is approved, not additive (Extract E8) |
| **D28** | **Recommended configuration: C5** — root-README anchor · purpose + principles + non-goals · fallback chain · quote-plus-harm · REJECT with a named finding and owner routing · two-part materiality · baseline + north star | The only survivor that passes the replay in both directions, needs three modest amendments rather than a redesign, and costs a project with no north star exactly nothing on upgrade day. C10 (tiered verdicts) is the fallback if the owner wants a lighter consequence for repairable purpose failures; C6′ is available if the nominated-HL locus is preferred and the project-freeze mechanism is scoped (Challenge § Surviving configurations) |
| **D29** | **The Reviewer Identity amendment ships but must not be load-bearing** | Strength ordering from the corpus: reference-set rule > forcing function > `judge.md` row > identity text. D46 recorded the identity statement as *"Quality guardian, **not rubber stamp**"*; the shipped text carries only the first half, and `rubber` appears **zero times** in `.tfw/`. Identity text has a measured survival rate of ½ in this repository (Gather G7, Challenge C8) |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q5 | Is correcting PV Index priority 1 inside TFW-53's scope, or a separate defect this task merely discovered? | 🛑 owner/coordinator decision | It is a one-row edit to a table DoD-17 already requires editing, and shipping priority 0 beside an uncorrected priority 1 is worse than shipping neither. Recommended: travel with TFW-53 as a refinement of Phase C deliverable 1. But it is a *discovered* defect present since D44 (2026-04-14) in every TFW project, and the coordinator may prefer it carry its own trace |
| Q6 | Must a project have a north star before it can be reviewed? | ✅ answered | No — D21. The fallback chain (north star → master HL §1 at the frozen baseline) keeps DoD-17/18 satisfied and makes the upgrade free. Blocking review on a missing anchor contradicts F21 and would make the framework un-adoptable the day it ships |
| Q7 | Does a goal-grounds rejection need a verdict name distinct from `❌ REJECT`? | ✅ answered | No — D18. DoD-22 already chose reuse; the distinction the board needs is carried by the *finding* name (`not fit for purpose`) plus mandatory owner routing, which is where A2 put the amendment `Type` for the same reason |
| Q8 | Is an internally contradictory HL in scope for TFW-53? | 🛑 owner decision | Part of TFW-49's rejected scope was a **faithful reading of the DoD the owner approved** (§1 vs DoD-3/5/7 + DoF-8). No downstream role can defend a self-contradictory contract. D19 gives the reviewer an escape hatch; making HLs internally coherent in the first place is a coordinator-side problem in `plan.md` and is **not** proposed here — flagging it would otherwise be scope inflation on the task that exists to prevent it |
| Q9 | Should the nominated-HL locus (AFD's live practice) be supported at all? | 🛑 owner decision | Only as *nominated-and-frozen* (D23). Supporting it unqualified is cheap and reproduces the drift problem one level up; supporting it properly needs a project-level freeze mechanism that is not in this task's file set |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H11 | The forcing function — quoting the north-star clause the work serves — is what separates a live check from a rubber stamp | open | 🟡 **qualified, not confirmed** | Necessary but **not sufficient**, and the replay proves it: citation alone would have approved TFW-49 Phase C, because approved DoD-3/DoD-5 make a validator and installable enforcement genuinely citable. The forcing function's real contribution is *legibility* — an unresolvable or absent citation is mechanically detectable by a later reader, which is D43's exact mechanism and the named remedy in audit practice (ISA 240: relate the matter to the specific circumstances of the entity; PCAOB: a bare sign-off is a documented deficiency). What **discriminates** is the excess/adjacency test. Ship both, and do not let DoD-20's three clauses stand in for D16's three tests (Challenge C2, Extract E4) |
| H12 | The project north star is the root `README.md`; no new file is needed. Corollary: PV priority 1 resolves to `.tfw/README.md` | open | ✅ **confirmed in substance; corollary confirmed and worse than stated** | Corollary: priority 1's own examples (*Traces Over Code*, *Structural Enforcement*) are headings inside `.tfw/README.md § Values and Principles`, and that section is **byte-identical** between TFW and AFD (`diff` → no output). It is structurally incapable of carrying project purpose. Main clause: both root READMEs do answer the north-star question — AFD's under `## Проблема` / `## Цель` — and no framework rule points at them, which is why AFD's agents reach for `HL-AFD-2` instead. So: no new file, **but** a designated section and a header field are required, plus the priority-1 relabel (Gather G2) |
| H13 | A one-page north-star payload is sufficient; AFD's 509-line anchor is mostly irrelevant to a reviewer | open | ✅ **confirmed, with a finding the hypothesis did not anticipate** | Measured: §1 Vision (28 lines) + §7 Principles (17 lines) = **45 of 509 lines, 8.8%**. The unanticipated half: **the anchor itself drifted** — six of §7's fourteen principles carry post-approval `(Added…)` markers and §4 carries two "scope additions" blocks, none logged. A north star that is a task HL is a frozen contract that grew 40% of its principle list after approval. And size is the easy half: the payload needs **admission criteria** (D22), because a list containing implementation detail satisfies a citation requirement forever while blocking nothing (Gather G3) |

Not re-litigated per `iterations.yaml`: H2, H7, H8, H9, H10. Resolved in iteration 1 and treated as constraints: H1, H3, H6.

## HL Update Recommendations

> Classified per the mechanism this task is building. **Refinements** target free sections — the coordinator applies
> them. **Amendment Proposals** target frozen sections — the coordinator may NOT apply them; they go to HL §12 as
> `PROPOSED` and await an owner verdict. This researcher has edited nothing.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R12 | §10 | H11 → 🟡 qualified (necessary, not sufficient — the excess test discriminates); H12 → ✅ confirmed in substance, corollary confirmed and worse (byte-identical section); H13 → ✅ confirmed (45/509 = 8.8%) **plus** the anchor-drift finding | H11/H12/H13 verdicts above |
| R13 | §2 | **Correct the count.** "All seven phase REVIEWs returned ✅ APPROVE" → *seven verdicts across **six** REVIEW files; six of seven final verdicts were APPROVE, and the single 🔄 REVISE at `1ebb680` was overwritten three commits later.* TFW-48 phase-d exists at `721ca15` as HL + TS only and never reached RF or REVIEW | Gather G4 |
| R14 | §2 | Add to the evidence table: **the approved TFW-49 contract was internally contradictory.** §1 (*"readable without special tooling"*, *"provenance, not decoration"*) against DoD-3 (*"a versioned structural validator"*), DoD-7 (*"repository fixtures across four roles and two surfaces"*) and DoF-8 (*"enforcement depends only on agent compliance prose"* = failure). Part of the scope the owner later rejected was a faithful reading of the DoD the owner approved | Challenge C2 |
| R15 | §2 | Add: **the review surface has no vocabulary for purpose.** Measured across `review.md`, three stage templates and three mode files — `purpose` 0, `goal` 0, `intent` 0, `north star` 0, `rubber stamp` 0, `vision` 1 (a context-loading bullet). HL §3's claim is not an interpretation of the text; there is no text | Gather G1 |
| R16 | §2 | Add: **D46 already contained the missing half.** `KNOWLEDGE.md` D46 records the Reviewer Identity as *"Quality guardian, **not rubber stamp**"*; the shipped `review.md:35` carries only *"Quality guardian"*. Second independent instance of the retention pattern, four months older than TFW-48's | Gather G7 |
| R17 | §2 | Add: **AFD's Judge scored ✅ on the AC that contained the violation** — `P8 Owner sees what agent sees → AC-B4 → ✅`, citing the same wire key (`GPS_PUBLISH_EVERY_N`) that the retraction names as the bypass. The mapping-integrity check is not weak, it is structurally inverted: a principle mapped to a passing AC scores ✅ regardless of the AC's content | Gather G5 |
| R18 | §9 | Add risk: **"A designated north star that is a task HL drifts like any other HL."** Probability High, Impact High. AFD's anchor grew 10 → 14 principles post-approval with no log. Mitigation: D20 (root-README locus) or D23 (*nominated-and-frozen* if the HL locus is chosen) | Extract E2, Gather G3 |
| R19 | §9 | Add risk: **"The reference set is internally inconsistent and the check becomes a coin flip."** Probability Medium, Impact High. Mitigation: D19's third outcome — route to the owner as a contract defect | Challenge C2, C5-iv |
| R20 | §9 | Update *"The goal check degenerates into a quality question and approves everything"* — mitigation now carries a **result**, not a plan: the DoD-26 replay returned 3 confident fires + 1 moderate on the rejected corpus and 0 blocks on three sound reviews | Challenge C2, C3 |
| R21 | §9 | Update *"The north-star anchor becomes an adoption tax on small projects"* → Probability **Low**. D21's fallback chain makes the upgrade free for any project without an anchor | D21 |
| R22 | §11 | Add insight: **TFW's own approved contract already drew the line it then crossed.** TFW-49 §1 at `9e19a4f` reads *"This is provenance, not decoration"* — the AFD idiom *decoration vs delivery* is not an import; the reference set needed to block Phase C was owner-approved and retrievable from git the entire time. The reviewers did not lack an anchor, they lacked an instruction to read one | Gather G14 |
| R23 | §11 | Add insight: **a rule stated in an HL cannot defend that HL.** TFW-48's master carried DoD-11 and P7 and lost both — P7 was live, approved and *invisible at the point of use*, because the reviewers' principle table derived from a Phase HL that had dropped it. Goal defence written into a task's own DoD is self-referential in the same way the principle chain is. It must live in the reviewer's template, where no task can drop it | Challenge C4 |
| R24 | §7.2 | Add citations: **D43** (Knowledge Citations as the anti-hallucination device — the forcing function is the same mechanism for the same reason) and **D46** (Reviewer Identity; and the recorded-but-unshipped "not rubber stamp" clause). Both are cited in §4 Phase C's Key Decisions but absent from the citations table | R16, E4 |
| R25 | §8 | Mark *RESEARCH iteration 2* ✅ complete → `research/iter2/RES.md`. Owner ruling on Q1 already recorded; add rows for Q5–Q9 | This RES |
| R26 | §4 Phase C (deliverable text, free under D2/D4) | Three refinements inside the approved phase, none needing a §5/§6 change: (1) deliverable 1 gains the fallback chain and the D22 admission criteria; (2) deliverable 1 gains the PV priority-1 relabel; (3) deliverable 2's clauses are drafted as **one fused field** (quote + harm) rather than two separate ones — all three clauses still ship, per DoD-20 | D17, D21, D22, D26 |

### Amendment Proposals — frozen sections, owner verdict required

> Three proposals, against iteration 1's ~2.3/iteration model and its own warning that *"a second iteration above three
> would be a real signal"*. Three is at the boundary, not above it. Each is an `EXTEND`; none reverses an approved claim.

| # | § | Type | Proposed change | Evidence | Cost | Alternative considered |
|---|---|------|-----------------|----------|------|------------------------|
| **A6** | §5 DoD (new item, Phase C) | `EXTEND` | The Purpose Check has a **third outcome**: *the reference set is internally inconsistent*. It is recorded as a finding, routed to the **owner as a contract defect**, and is not a work defect — the executor is not asked to fix it | TFW-49's approved contract contradicted itself: §1 *"readable without special tooling"* / *"provenance, not decoration"* vs DoD-3 *"a versioned structural validator"*, DoD-7 fixtures, DoF-8 making prose-only enforcement a failure. Against a contradictory reference set the same evidence yields a defensible fire and a defensible pass (Challenge C2, C5-iv) | +1 DoD item; one extra branch in the `judge.md` row and in `review.md` §5 routing | Let the reviewer choose a side — rejected: that is a coin flip wearing citations, and the first contradictory HL would produce a false REJECT and discredit the check on its debut, the AFD-48/B failure mode with higher stakes. Or treat it as REVISE back to the executor — rejected: the executor cannot fix an HL |
| **A7** | §5 DoD-19/DoD-20 | `EXTEND` | The Purpose Check must carry an explicit **excess-and-adjacency test**: *does the result deliver something the cited clause does not ask for, or that a baseline non-goal, DoF item or phase boundary excludes?* DoD-20 currently enumerates three mandatory clauses (override, materiality, forcing function) and none of them is this test | The replay is decisive: **citation alone would have approved TFW-49 Phase C.** Approved DoD-3/DoD-5 make a validator and installable enforcement citable; what blocks it is *"safely bypass"* → two-hook runtime + private ledger + carrier, plus DoF-8's unversioned-`.git/`-state hit. Shipping (a) without (b) reproduces DoF-11 exactly (Challenge C2, D16) | One clause in DoD-19 or DoD-20; one line in the `judge.md` row | Rely on DoD-19's *"serves the north-star purpose… investment or a deferred local workaround"* to imply it — rejected: the replay shows the implication is not read that way. TFW-49's reviewers wrote *"exactly 29 framework paths"* six times; they were policing boundaries and still missed excess, because excess against a *declared outcome* is a different question from scope conformance |
| **A8** | §5 DoD-17 | `EXTEND` | Priority 0 answers *"what we are building, why, **and what we are deliberately not building**"*. DoD-17 currently reads *"what we are building and why"* | The corpus failure mode is **excess, not opposition**. TFW-49 Phase C did not contradict *"provenance, not decoration"* — it exceeded it. TFW-48 Phase A/C did not contradict *"purpose before process"* — they added conceptual layers past it, hitting master DoF-12. A purpose statement alone cannot catch excess; a purpose statement plus non-goals can (Gather G13, Extract E3, Challenge C2) | One clause in DoD-17; one subsection in the north-star payload | Put non-goals in HL §6 DoF instead — rejected: DoF is task-scoped and re-authored per task, which is the self-referential chain the anchor exists to break. Or leave non-goals optional — rejected: it is the element that carries the corpus's actual failure mode, so making it optional makes the check optional in the case that matters |

### Coordinator notes — inside approved scope, no amendment needed

1. **Phase C's deliverable weighting should be re-read.** §4 calls the north-star anchor *"the load-bearing piece; the
   other two are inert without it."* The evidence supports a different ordering: **reference-set rule > forcing function
   > anchor**. At the moment TFW-49 Phase C shipped, the approved Vision, the approved Phase C deliverable and DoF-6 all
   existed and were retrievable at `9e19a4f`; what was missing was the instruction to read them instead of the Phase HL
   and the TS. The anchor still earns its place — it is the only defence against a task whose *own* approved HL is wrong
   for the product — but it is the piece that degrades gracefully, and the reference-set rule is the one that cannot.
   Deliverable weighting inside an approved phase is a refinement under iter1 D2/D4.
2. **`templates/review/judge.md` row 2 is the enforcement site, and it is the only one.** Per Challenge C4, a rule that
   lives in a task's DoD cannot govern that task's reviews. Everything in Phase C that matters must land in the
   *template*, not in `review.md` prose and not in `conventions.md` alone — the same lesson as `templates/RES.md:32`
   from iteration 1, on the other side of the pipeline.
3. **`review.md`'s context-loading list needs one word.** Line 28 says *"**Master HL** for the task"* with no revision.
   The reference-set rule needs it to say *the master HL **at its frozen baseline***, or reviewers will keep reading the
   current file — which in TFW-49's case was the drifted one.
4. **Watch the `plan.md`/`review.md` word budget separately.** DoD-25 caps `review.md` at F2's range. Three of this
   iteration's outputs (reference-set rule, third outcome, excess test) land in `judge.md` — a *template*, not a
   workflow — which is the cheaper surface for the budget. Worth stating in the Phase C TS so an executor does not
   route them into `review.md` by default.

## Fact Candidates

> Human-Only Test applied strictly. Everything in Gather/Extract/Challenge is discoverable by an agent reading files and
> running git — those are research findings, recorded above, not fact candidates.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| — | — | **No new fact candidates.** Iteration 1's FC1 (the owner disables blocking gates when they trust the frame, not when they stop caring) is *reinforced*: the owner ran iteration 2 gateless again, after reading iteration 1's output and after ruling on five amendment proposals. That is confirming evidence for an existing candidate, not a new one | — | — |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS2 | stakeholder | The owner's naive question — *«у нас тут есть два readme… кто из них является north-star?»* — located a defect that had been live in **every TFW project since D44 (2026-04-14)** and that no agent in either project had noticed while scanning PV dozens of times. The owner was right about the substance (the root README does hold the purpose) and right that something was wrong with the index, without being able to name what. **Implication:** the framework's self-audit blind spot is *labels that resolve*. Priority 1 always resolved to a real file with real content, so every scan succeeded and nothing ever failed loudly. The forcing function this task is shipping has the same shape and the same risk — a citation that resolves is not a citation that is relevant (Extract E4), and D22's admission criteria are the only guard against the identical failure recurring one layer up | User, S26 + Gather G2 | ★★★ |
| SS3 | process | The owner approved **5 of 5** amendment proposals from iteration 1 and re-froze the same day. The gate's first live run produced no refusals. **Implication:** the amendment protocol's value in practice was *visibility and batching*, not *rejection* — which is exactly what Principle 4 claims and what SS1 predicted, and it means the design must never be justified by an expected rejection rate. A protocol whose measured refusal rate is 0/5 is either working (the proposals were good because the burden of evidence-cost-alternative filtered them before they were filed) or decaying into the CCB rubber stamp; the two are indistinguishable at n=5, and the discriminator is whether a *rejected* proposal ever appears. Worth watching, not worth acting on yet | Owner verdicts in HL §12, `d9a4c57` | ★★☆ |

## Findings Map

**DoD-26 replay — where the check fires, where it does not, and why that is the point:**

```
REJECTED CORPUS (TFW-48/49 — owner rejected the whole result)
                        (a) cite   (b) excess   (c) confession   outcome
TFW-48/A  method kernel     ✓         ██ DoF-12       ·          🔄/❌  FIRES
TFW-48/B  planning/research ✓          ·  tension     ·          ✅     passes
TFW-48/C  spec/exec/evid    ✓         ██ DoF-12      ░ partial   🔄     FIRES
TFW-49/A  contract+validator✓          ·  arguable    ·          ✅     passes
TFW-49/B  workflow/adapter  ✓         ▓  cue→router   ·          🔄     fires (mod)
TFW-49/C  enforcement migr. ✓         ██ bypass→runtime          ❌     FIRES (strong)
                                      ██ DoF-8 hit   ░ 1ebb680
                                                      ─────────────────
                                                      3 strong + 1 moderate

SOUND CORPUS (tasks the owner kept and built on)
TFW-46/A  evidence templates ✓         ·  disclosed    ·          ✅     no block
TFW-47/B  codex adapter      ✓         ·  positive dev ·          ✅     no block
TFW-50    commit attribution ✓ "without enforcement software"     ✅     no block
                                                      ─────────────────
                                                      0 of 3 blocked

DoD-26 requires: ≥1 non-approve above, 0 below.   → met, with discrimination
(2 of 6 rejected-corpus reviews pass — the check is not a blanket condemnation)
```

**Where each reviewer was looking, and where the answer was:**

```
                       what the reviewer read          what would have blocked it
                       ─────────────────────           ──────────────────────────
TFW-48 phase reviews   phase HL §7  (P7 dropped)  ✗    master §7 P7, approved, live
                       TS §3 mapping              ✗    master DoF-12, approved, live
TFW-49 phase reviews   HL @ 642c647 (drifted)     ✗    HL @ 9e19a4f, approved, in git
                       TS derived from it         ✗    approved Phase C "safely bypass"
                                                       approved DoF-8 ".git/ state"
                       ─────────────────────────────────────────────────────────────
                       every reference was          every anchor existed and was
                       DOWNSTREAM of the drift      RETRIEVABLE the whole time
```

**The four levers, ordered by measured strength:**

```
strongest │ reference-set rule      changes WHAT IS READ      wrong reference is checkable later
          │ forcing fn + harm       changes WHAT IS WRITTEN   unresolvable citation is detectable
          │ judge.md row            changes WHAT IS ASKED     answerable emptily, not omittable
weakest   │ Reviewer Identity       changes WHAT IS FELT      D46 proves identity text is droppable
          └──────────────────────────────────────────────────────────────────────────────────────
            HL §4 calls the anchor "load-bearing"; the evidence puts the reference-set rule first
```

**How a result is routed under the recommended design (C5):**

```
result delivered
  │
  ├─ reference set = master HL @ frozen baseline + project north star   [D15]
  │     (phase HL ✗   TS ✗ — Principle 16, A1)
  │     └─ no north star designated? ── fall back to master HL §1        [D21]
  │
  ├─ (a) quote the clause served + name the concrete harm at stake       [D17]
  │        └─ cannot quote? ────────────────────► not aligned; block cannot be waived
  │
  ├─ (b) excess / adjacency — delivered what the clause did not ask for,
  │        or what a non-goal / DoF / phase boundary excludes?           [D16, A7]
  │
  ├─ (c) deferral confession — spec or result says the right home is
  │        elsewhere, and ships it here anyway                           [E7]
  │
  ├─ reference set self-contradictory? ─────────► finding → OWNER        [D19, A6]
  │                                               contract defect, not work defect
  │
  └─ material impact named? ── no ──────────────► not a block (wording ≠ grounds)
                            └─ yes ────────────► ❌ REJECT
                                                 finding: NOT FIT FOR PURPOSE  [D18, D25]
                                                 routes to OWNER, not executor
                                                 "TS scoped it" / "tests green" ✗ grounds
```

## Iteration Status

- **Iteration:** 2 of 2 (min) / 3 (max) — `min_iterations: 2` is now met
- **Hypotheses tested:** H11 (🟡 qualified — necessary, not sufficient), H12 (✅ confirmed in substance; corollary confirmed and worse than stated), H13 (✅ confirmed, plus an unanticipated anchor-drift finding)
- **Hypotheses deferred:** None. H2, H7, H8, H9, H10 settled upstream; H1, H3, H6 resolved in iteration 1
- **Gaps discovered:** (1) the approved TFW-49 contract was internally contradictory, so part of the rejected scope was a faithful reading of the approved DoD — no downstream role can defend that, and the check needs a third outcome; (2) a designated north star that is a task HL is itself an unfrozen contract, and AFD's has already drifted 10 → 14 principles; (3) the north-star payload needs *admission criteria*, not a size cap — a list containing implementation detail satisfies a citation requirement forever while blocking nothing; (4) `review.md:28` names the master HL with no revision, so the reference-set rule has nothing to bind to until that line changes; (5) D46's "not rubber stamp" clause was recorded in KNOWLEDGE.md and never shipped — a second, older instance of the retention pattern; (6) PV priority 1 resolves to a section that is byte-identical across projects, so the highest-priority Project Value source is structurally incapable of holding project information
- **Superseded decisions:** None. D15–D29 extend iteration 1's D1–D14; no iteration-1 decision is reversed. D28 (recommended configuration C5) is the goal-defence counterpart of iteration 1's D14 (C4), not a replacement for it

### Open Threads (for next iteration)

> `min_iterations` is met and the researcher recommends proceeding. These are threads for **TS time or a contingency
> iteration 3**, not blockers.

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | HL internal coherence (Q8) | TFW-49's §1 and §5 pulled in opposite directions before any drift occurred. D19 gives the reviewer an escape hatch; nothing prevents the next contradictory HL from being written. This is a `plan.md` problem and deliberately **not** proposed here | If the owner wants it: a separate task, sized against how many historical HLs contain a §1/§5 contradiction. Building it inside TFW-53 would be the scope inflation this task exists to prevent |
| 2 | The nominated-HL locus and project-level freezing (Q9, D23) | AFD's live practice, and it works there. Supporting it unqualified reproduces the drift one level up; supporting it properly needs a mechanism outside this file set | Decide at Phase C TS: either exclude the locus explicitly in `conventions.md`, or scope *nominated-and-frozen* as a follow-up |
| 3 | Salami residual — third appearance (D27, iter1 Q3) | Still the one mechanism from HL §11 S3 that survives inside the fix. Now costed: one command at the pre-TS gate, would have fired on TFW-49 | Phase A/B TS: add `git diff` against the freeze baseline to the pre-TS gate, or record the flank in TECH_DEBT explicitly |
| 4 | Whether the check decays in production | The replay proves the check *can* fire on a known-bad corpus. It cannot prove a reviewer will run it honestly on live work, and SS2 says a resolving citation is not a relevant one | After 5–10 live reviews under the new template: count how many Purpose Check rows cite an `NS{n}` clause vs an HL §7 `P{n}`, and how many name a concrete harm. A row that never names a harm is decaying |
| 5 | AFD's remaining 143 reviews were sampled, not enumerated | The "~4 goal-grounded blocks" figure remains prior-recon-sourced. The 149-file verdict distribution (134/26/1) *was* independently recounted here | Low value — the base-rate argument (H8) is already settled and does not change with ±2 |

### Recommendation

- [x] **SUFFICIENT** — proceed. `min_iterations: 2` is met, all three assigned hypotheses are resolved with primary evidence, and HL DoD-26's replay executed in both directions with the required outcome and with discrimination.
- [ ] MORE NEEDED
- [ ] BLOCKED

Sequencing note for the coordinator: A6–A8 are independent of each other and can be ruled on in one batch. Phases A, B
and E do not depend on any of them and can start immediately; **Phase C should not start until A7 is ruled on**, because
it changes what DoD-20 requires the check to carry, and drafting the `judge.md` row twice is the expensive way to find
that out.

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 2 set out to build the defender and found that most of the defence had already been written down and thrown
away. TFW-49's approved Vision says *"provenance, not decoration"* and its approved Phase C says *"safely bypass"*; both
were owner-approved, both were retrievable from git throughout the six days that produced 5,910 lines of Python runtime,
and no reviewer opened them. TFW-48's master carried P7 *"Independent Review Protects the North Star"* as a live frozen
principle, and it was invisible at the point of use because the reviewers' principle table derived from a Phase HL that
had dropped it. `KNOWLEDGE.md` D46 records the Reviewer Identity as *"Quality guardian, not rubber stamp"* and the word
`rubber` appears zero times in `.tfw/`. Three losses, three mechanisms, one conclusion: **a rule stated in an HL cannot
defend that HL, and a rule stated in prose does not survive in this repository.** The design target is retention, and
the only surface that retains is the reviewer's template.

The three hypotheses resolved cleanly and one of them changed the design. H12 holds in substance — the root README does
carry the purpose in both projects, no new file is needed — and its corollary turned out worse than the HL states: PV
priority 1 points at a section that is *byte-identical* between TFW and AFD, so the framework's highest-priority Project
Value source cannot carry project information at all. H13 holds on size (45 of 509 lines) and exposed something the
hypothesis did not ask about: the anchor AFD designated is itself an unfrozen contract that grew 40% of its principle
list after approval. H11 is the one that moved. The forcing function is necessary and it is not what discriminates —
the replay shows that a citation requirement alone would have **approved** TFW-49 Phase C, because the approved DoD
genuinely authorised a validator. What blocks it is excess against the phase's *declared outcome*, which is why A7 asks
for that test to be named rather than implied.

What research provided that the design would have missed: the replay itself, which is the difference between a check
that is argued for and a check that has been shown to fire three times on rejected work and zero times on sound work;
the discovery that citation without an excess test would have reproduced the failure; the third outcome, without which
the first self-contradictory HL turns the check into a coin flip on its debut; and the anchor-drift trap, which would
have shipped invisibly because the obvious cheap locus — nominate an existing HL, as AFD does — quietly promotes a task
contract to project authority with no gate at the promotion point.

Self-critique. The replay is a single researcher re-judging reviews whose outcome I already knew was rejected —
hindsight is uncontrolled, and two of the six fires rest on my reading of *"exceeds the declared outcome"*, which
Challenge C5(i) concedes is a judgement call two competent reviewers could split. The three sound reviews were chosen by
me from a corpus whose sound half is small, so the false-positive control is weaker than the true-positive one. TFW-48's
master could not be read at its true approval point because that HL was never committed pre-amendment — the hole DoD-5
exists to close, met here as a research limit. And the deepest uncertainty is unfalsifiable from artifacts: the check
makes rubber-stamping *legible*, not impossible, and both AFD precedents were caught by the owner reading output rather
than by any mechanism firing on its own. Nothing in either corpus shows a goal check firing unprompted, because no such
check has ever existed to observe.

---

*RES — TFW-53: Goal Defence in Review (Iteration 2) | 2026-08-08*
