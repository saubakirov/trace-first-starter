# RES — TFW-53: Contract Calibration (Iteration 1)

> **Date**: 2026-08-08
> **Author**: Researcher (Claude Code, separate session)
> **Status**: 🔬 RES — Iteration 1 complete
> **Parent HL**: [HL-TFW-53](../../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN, baseline commit `8136306`
> **Mode**: Pipeline · deep (`loops_per_stage: 3`, counter-evidence required) · autonomous run, no interactive gates

---

## Research Context

TFW-53 proposes to freeze six HL sections on owner approval and route every further change through an
evidenced amendment log. Iteration 1 calibrates that proposal against TFW's own history, which is the only
corpus where the mechanism's cost can be measured rather than guessed: 36 research iterations across 27
tasks, plus the TFW-48/49 failure trees recoverable from git. Three questions were open — how often would a
freeze actually fire (H1), what state mechanism the contract needs (H3), and whether Phase HLs are a second
drift channel (H6) — plus two design questions from HL §10 Blind Spots (freeze asymmetry, REJECT
composition). Nothing here touches goal defence in review; that is iteration 2 in full.

## Briefing

[`1_briefing.md`](1_briefing.md). Stage files: [`2_gather.md`](2_gather.md) · [`3_extract.md`](3_extract.md) ·
[`4_challenge.md`](4_challenge.md).

Run was executed autonomously on owner instruction (*«tfw-53 автономно без вопросов deep mode»*). All four
🛑 WAIT gates were executed as self-checkpoints; the questions that would have been asked are recorded in
Open Questions below for the coordinator to route.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| **D1** | **The frozen section set stays exactly as approved (all six).** No reduction is recommended | Every candidate reduction is refuted by a specific TFW-49 event: release §4 → "Phase C flipped from bypass-the-hook to install-a-runtime" becomes a refinement; release §5/§6 → all 10 DoD and all 10 DoF were replaced silently; release §1/§3 → Vision widened from agent-authored commits to every commit. Challenge § Consistency Check |
| **D2** | **The frozen unit is the declarative claim, not the section text.** Frozen: the phase set and each phase's declared outcome, §3's to-be claims, §5/§6 items, §7 principles, §1. Free: the deliverable list inside an approved phase | This is where the cost lives. Same frozen section list, escalation falls from 4.6 to ~2.3 proposals per iteration (Extract E1). "We will add `mkdocs-literate-nav` to `requirements.txt`" was never a contract change under any reading of §1 |
| **D3** | **D2 requires no amendment.** HL §4 Phase A deliverable 3 already delegates *"what freezes"* to `conventions.md` §3 | The response to a refuted H1 does not have to be a reduction of the owner's approved scope. The definition that carries the cost was delegated downward at approval time (Extract E2) |
| **D4** | **Bound the free granularity with the DoD tripwire:** a deliverable-list change is a refinement only if it needs no §5/§6 change; if it cannot be accepted under the existing criteria, it is an amendment | Mechanical, checkable against two tables, reuses an already-frozen section as the detector, adds no new concept. Validated 5/5 against corpus cases (Extract E3) |
| **D5** | **Contract state = header field + append-only §12 + a baseline reference recoverable from git.** No new file, no snapshot | H3's "no filesystem marker" half holds — D31's principle is *file existence = state*, and a snapshot creates two contracts that can disagree (F22). H3's "sufficient" half fails: neither the header nor §12 names the baseline, so DoD-5's diffability is unmet (Gather G4) |
| **D6** | **The baseline reference is a reserved commit scope word, not a SHA in the header.** `[agent/TFW-NN/freeze/coordinator] …`, recoverable via `git log --grep` | A commit's SHA cannot appear inside its own content, so a self-describing header field is impossible. D55's `[agent/task/scope/role]` grammar already has the slot; a tag is an optional convenience, not a requirement (Gather G4) |
| **D7** | **Re-freeze after every approved amendment** — a new freeze commit at the new baseline | Otherwise the *second* baseline is unverifiable and TFW-48's failure mode reproduces after the first amendment instead of before the first iteration (Extract E7) |
| **D8** | **Freeze asymmetry: restrictive-logged, not restrictive-free.** Tightening (adding a DoF, narrowing scope, dropping a deliverable) applies immediately *and* lands in §12 with verdict `APPLIED — restrictive` | Restrictive-free is unsafe because the classifier benefits from the label — S13's self-extending grant in the opposite direction, and TFW-27 #1 is a corpus case of a target-state redesign that reads as tightening. Logging costs nothing and removes the incentive (Gather G5, Challenge § Consistency Check) |
| **D9** | **§12 gains a `Type` column: `EXTEND` / `SUPERSEDE` / `APPLIED — restrictive`** | ADR practice separates *amend/extend* (original stays accepted, link added) from *supersede* (original replaced) precisely because the consequences differ. Without the column an owner must reconstruct which one they are ruling on — the CCB rubber-stamp mechanism (Extract E4, Gather G7/G8) |
| **D10** | **Phase HLs become derivation-only:** a Phase HL may restate master content and add execution context; it may not carry its own §1, §5, §6 or §7 | H6 confirmed and understated. TFW-48's Phase A HL is a full second contract — 10 new DoD items, 9 new DoF items, 10 principles, with three master principles silently dropped. Abolition (C13) also survives scrutiny and is the owner's call (Gather G3, Extract E5) |
| **D11** | **`❌ REJECT` branch (a) "rework HL" is redefined as *file an amendment*, and re-entry to `📝 HL_DRAFT` does not thaw frozen sections** | Today branch (a) is an unlogged contract edit permitted because it happens after a rejection, and D20's implicit approval means re-entering the status *is* re-approval. Left as-is, REJECT is the universal bypass and agents that want to move a goal learn to route through it (Gather G6) |
| **D12** | **An owner-initiated change is an amendment too** — logged in §12 with the owner as proposer and the verdict on the same row | The protocol as drafted only runs research → owner. Unspecified, the coordinator will apply an owner remark directly — TFW-49's S6 failure with the polarity reversed. The log's value is the record, not the gate; a §12 that omits the owner's own changes cannot answer the question it exists to answer (Challenge C4) |
| **D13** | **Non-substantive edits (typos, broken links, formatting) are not amendments** | ADR practice carves this out explicitly. Without it, a broken link in §1 is formally a contract change, and agents will either file absurd proposals or learn to edit frozen text quietly. The second outcome is worse than the problem (Challenge C7) |
| **D14** | **Recommended configuration: C4** — all six frozen · declarative-claim granularity · header + §12 + git baseline · researcher classifies, coordinator verifies · batched per iteration · restrictive-logged · Phase HL derivation-only · REJECT branch (a) redefined | Lowest escalation load among configurations that keep the full frozen set, and the only survivor that ships without amending the freeze itself. C3 is the simpler fallback if two-key verification proves unnecessary |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Constrain the Phase HL (D10) or abolish the artifact class entirely (C13)? | 🛑 owner decision | Abolition survives scrutiny: TFW-42 and TFW-46 completed multi-phase work without one, TFW-47's constrained form carries zero information beyond master §4, and TFW-48's unconstrained form is where three approved principles were lost. Not recommended over D10 only because removing a permitted output touches `conventions.md` §15 and `resume.md`, outside TFW-53's declared file set |
| Q2 | Is `APPLIED — restrictive` an acceptable amount of ceremony for a change that applies immediately anyway? | 🛑 owner decision | The alternative (restrictive-free, unlogged) is measurably unsafe — see D8. The cost is one §12 row per tightening, ~15% of frozen-targeting traffic |
| Q3 | Does the salami residual (Challenge C2) justify a `git diff`-against-baseline check at the pre-TS gate? | ⬜ deferred | Not resolvable from artifacts. Twelve individually defensible deliverable refinements that sum to a new phase are *not* logged under D2/D4, because only amendments reach §12. This is HL §11 S3's exact mechanism surviving inside the fix |
| Q4 | Would the owner have rejected any of the 162 frozen-targeting historical rows? | ❌ unknowable | The honest limit on this iteration's central number. The 76% measures what research *proposed*, never what an owner *would have refused* |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | The large majority of historical RES `HL Update Recommendations` targeted free sections — so freezing six sections costs few escalations | open | ❌ **refuted** | 162 of 213 rows (76.1%) target frozen sections; 35 of 36 iterations would escalate; mean 4.6 proposals per iteration. Sensitivity: assigning every ambiguous row to FREE gives 71.4% and changes no iteration's outcome. Caveat: the figure is an **upper bound** — `plan.md` Step 6c points research at scope, so some §3/§4 concentration is endogenous (Gather G1, Challenge C1) |
| H3 | A header field plus an append-only §12 is sufficient state; no filesystem-level marker is needed | open | 🟡 **partially confirmed** | "No new file" holds — a snapshot creates two contracts that can disagree, and D31's principle is state-by-existence, which the HL file plus git already provide. "Sufficient" fails — a commit's SHA cannot appear in its own content, so the header cannot name its baseline and DoD-5's diffability is unmet. A reserved commit scope closes it (Gather G4, Extract E7) |
| H6 | Historical Phase HLs introduced deliverables absent from their master HL | open — believed narrow | ✅ **confirmed, and understated** | TFW-48 `phase-a/HL__phase-a__method_kernel.md` is a complete second contract: 10 new DoD items, 9 new DoF items (incl. one constraint absent from the master), 10 principles of which master P7, P10 and P12 do not survive, and a self-declared status `✅ HL — Approved scope derived from master HL`. The HL's note that phase HLs "showed no content drift (only marker commits)" describes their commit history, not their content (Gather G3) |

Not re-litigated per the briefing: H2, H7 (confirmed upstream), H8/H9/H10 (settled by AFD recon).
H11, H12, H13 belong to iteration 2.

## HL Update Recommendations

> Classified per the mechanism this task is building. **Refinements** target free sections — the coordinator
> applies them. **Amendment Proposals** target frozen sections — the coordinator may NOT apply them; they go
> to HL §12 as `PROPOSED` and await an owner verdict. This researcher has edited nothing.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §10 | H1 → ❌ refuted (162/213, 76%, 35/36 iterations, upper bound); H3 → 🟡 partially confirmed (no new file, but baseline reference required); H6 → ✅ confirmed and understated | H1/H3/H6 verdicts above |
| R2 | §9 | Raise "Phase HL files become an unfrozen back door" from Medium/Medium to **High/High** and restate: the channel is not an added deliverable, it is a full re-derivation of the contract including acceptance criteria and values | Gather G3 |
| R3 | §9 | Add risk: **"Escalation volume converts the gate into a rubber stamp."** Probability Medium, Impact High. Mitigation: D2 granularity keeps the load at ~2.3/iteration; Principle 5's evidence-cost-alternative burden sits on the proposer, so declining stays cheap | Challenge C5, external CCB evidence |
| R4 | §9 | Add risk: **"Salami — free deliverable refinements accumulate unlogged."** Probability Medium, Impact Medium. §12 records amendments only; nothing counts the free changes. Candidate mitigation: `git diff` against the baseline at the pre-TS gate | Challenge C2 |
| R5 | §2 | Add to the TFW-48/49 evidence table: **the Phase HL as a second unapproved contract** — TFW-48 Phase A's 10 DoD / 9 DoF / 10 principles, and master P7, P10, P12 not surviving the derivation | Gather G3 |
| R6 | §2 | Add: **TFW-48's approved master HL already contained goal defence** — DoD-11 ("Review can reject work that satisfies TS/RF but violates the product north star") and P7 ("Independent Review Protects the North Star… the last quality authority before project learning and closure"). Both were lost at phase level, then entirely on revert. The framework's failure is retention, not invention | Gather G3 |
| R7 | §2 | Add: `templates/RES.md:32` still carries `<!-- List what should change in HL based on research. Coordinator applies these. -->` — the workflow-side twin of the H2 finding, sitting in the template rather than in `plan.md` | Gather G10 |
| R8 | §11 | Add insight: **TFW-52 iter2 invented the amendment protocol by hand** — an unmandated `Status` column reading `UNAPPROVED` on all nine rows, per-proposal justification subsections, and an unprompted non-authority disclaimer in iter1. `process.md` F11 (organic emergence → formalisation) firing on this exact mechanism | Gather G9 |
| R9 | §11 | Add insight: the owner ran this iteration with **all four blocking gates disabled** on the task that exists to install a gate. Field data on the real interruption budget: the objection is to *being asked*, not to *being bound* | Owner directive, this session |
| R10 | §7.2 | Add citations: **D55** (minimal commit attribution — supplies the baseline-reference vehicle) and **`process.md` F11** (organic emergence → formalisation — justifies formalising TFW-52's hand-rolled protocol) | D6, R8 |
| R11 | §8 | Mark the RESEARCH dependency row's iteration-1 items (amendment frequency, enforcement site, contract state mechanism) ✅ complete; Guard placement and AT portability remain out of iteration 1's scope | This RES |

### Amendment Proposals — frozen sections, owner verdict required

> Five proposals. Above the ~2.3/iteration this research models — expected, because the first iteration of
> the task that invents a mechanism is the worst case for that mechanism. A second iteration above three
> would be a real signal (Challenge C8).

| # | § | Type | Proposed change | Evidence | Cost | Alternative considered |
|---|---|------|-----------------|----------|------|------------------------|
| **A1** | §4 Phase A | `EXTEND` | Add a deliverable: `conventions.md` §3 defines the **Phase HL as derivation-only** — it may restate master content and add execution context, may not carry its own §1/§5/§6/§7 — plus a §14 anti-pattern for a Phase HL that authors acceptance criteria or principles | H6 confirmed: TFW-48 Phase A HL = 10 new DoD, 9 new DoF, 10 principles, three master principles dropped, no template, no gate (G3) | +1 deliverable in Phase A, ~15 lines in `conventions.md`, 0 new files | Abolish the class entirely (C13) — survives scrutiny but touches `conventions.md` §15 and `resume.md`, outside the declared file set. Or leave to a follow-up task — rejected: the freeze then protects the master while the drift relocates one level down, which HL §10 named as the reason to research this at all |
| **A2** | §3 (§12 grammar) + §4 Phase A del. 1 | `EXTEND` | §12 gains a **`Type` column** with values `EXTEND` / `SUPERSEDE` / `APPLIED — restrictive`; the §3 example log is updated to show it | ADR practice separates amend/extend from supersede because the baseline consequence differs; CCB evidence: without an impact assessment the ruler defaults to approve (G7, G8, E4) | One column; §3's illustrative table gains a field | Encode the type in the prose of `Proposed change` — rejected: it is exactly the "reconstruct it from the prose" burden that produces rubber-stamping. Or omit the type — rejected: an `EXTEND` and a `SUPERSEDE` then look identical at the moment of ruling |
| **A3** | §5 DoD | `EXTEND` | Add a DoD item: **an approved amendment is followed by a re-freeze commit at the new baseline.** DoD-5 currently covers only the commit before the first research iteration | The second baseline is otherwise unverifiable — TFW-48's failure mode reproduced after the first amendment rather than before the first iteration (E7) | +1 DoD item; one commit per approved amendment | Rely on DoD-5 alone — rejected: it is explicitly scoped to "before the first research iteration". *(The reserved commit scope word itself is implementation of the existing Phase A deliverable 3 and needs no amendment.)* |
| **A4** | §5 DoD (DoD-6) | `EXTEND` | Extend DoD-6: **an owner-initiated change to a frozen section is also an amendment**, logged in §12 with the owner as proposer and the verdict on the same row | The protocol as drafted runs only research → owner. Unspecified, the coordinator applies an owner remark directly — S6's failure with the polarity reversed. §12 cannot answer "which goals changed and when" if it omits the owner's own changes (Challenge C4) | One clause in DoD-6; one §12 row per owner-initiated change | Treat owner changes as outside the protocol — rejected: it reopens the S6 hole under a different name and empties the log of its stated purpose |
| **A5** | §4 (Phase A or E) + §5 | `EXTEND` | Add a deliverable and a DoD item for **REJECT composition**: `conventions.md` §5 branch (a) "rework HL" is redefined as *file an amendment against the frozen sections*, and re-entry to `📝 HL_DRAFT` explicitly does not thaw them | Branch (a) is today an unlogged contract edit permitted because it follows a rejection; D20's implicit approval makes re-entering the status equivalent to re-approval. REJECT becomes the universal bypass (G6, C7) | +1 deliverable, +1 DoD item; ~8 lines in `conventions.md` §5. Phase assignment is a coordinator call — §7.1 gives §5 to Phase E, but the rule is contract semantics owned by Phase A | Leave REJECT independent — rejected: it is the one documented path that reopens frozen sections with no proposal, no evidence and no log |

### Coordinator notes — inside approved scope, no amendment needed

1. **The granularity definition (D2/D4) and the non-substantive carve-out (D13) belong in Phase A deliverable
   3** (*"conventions.md §3 — HL Contract definition: what freezes, when…"*). "What freezes" was delegated at
   approval time. This is the single highest-leverage decision in the task and it costs zero amendments.
2. **Phase A's TS must include an acceptance criterion for `templates/RES.md:32`.** Delivering the
   Refinements/Amendment-Proposals split while leaving `Coordinator applies these` in place ships DoF-1
   inside the enforcement site itself, and no current DoD item would catch it (Challenge C6).
3. **`UNAPPROVED` vs `PROPOSED`** — TFW-52's field-tested column value describes the state of the world;
   HL §3's example uses `PROPOSED`, which describes the state of the request. Worth one line of D28
   reasoning in Phase A rather than an unexamined default.

## Fact Candidates

> Human-Only Test applied strictly: an agent can discover everything in Gather/Extract/Challenge by reading
> files and running git. Those are research findings, recorded above and in the stage files — not fact
> candidates.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | process | The owner disables blocking gates when they trust the frame, not when they stop caring about the outcome: this iteration was run with all four 🛑 WAIT gates off, on the task whose purpose is to install a gate. The objection is to being asked step-by-step, not to being bound | User, run directive 2026-08-08 | ★★☆ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | stakeholder | The owner's interruption budget is spent on *frequency*, not on *authority*. Running a four-gate workflow gateless while insisting that six HL sections may not move without a personal verdict is one coherent position, not a contradiction — and it is precisely HL Principle 4 ("batch, don't interrupt") stated by behaviour rather than by text. **Implication:** the design's success metric is proposals-per-iteration, not proposals-per-task; C1's 4.6 fails it and C4's ~2.3 passes | User, run directive 2026-08-08 | ★★☆ |

## Findings Map

**Root cause chain — why the reference point is always downstream of the drift:**

```
owner approves master HL  ──────────────── the only owner-ruled artifact
        │
        │  ✗ no gate, no template, no diff        ← H6 confirmed (TFW-48)
        ▼
phase HL §1 §5 §6 §7  (coordinator-authored, unapproved)
        │                                          three master principles dropped here
        ▼
phase TS §3 Principles Check
        │
        ▼
phase RF §3
        │
        ▼
judge.md row 2  — mapping integrity against the phase's own principle set
        │
        ▼
✅ APPROVE  × 7 of 7                               ← H7, already confirmed
```

**Where the 213 historical recommendation rows land, and what each design would gate:**

```
                                 rows    C1 gates?   C4 gates?
§4 deliverable lists   ████████████ 78      yes         no  ← the entire cost difference
§3 to-be claims        ████████     58      yes      yes/no  ← declarative only
§5 §6 acceptance       ██           15      yes        yes
§7 principles          █             8      yes        yes
§1 vision              ▏             3      yes        yes
§2 §8 §9 §10 §11 free  ████████     51      no          no
                                   ────
                                    213    4.6/iter   ~2.3/iter
```

**Decision tree — how a finding is routed under the recommended design (C4):**

```
finding
  ├─ non-substantive (typo, link, formatting)? ──────────────► apply, no log        [D13]
  ├─ targets §2 §7.2 §8 §9 §10 §11? ─────────────────────────► refinement, apply    [HL §3]
  ├─ tightens a frozen claim (adds DoF, narrows scope)? ─────► apply + §12 row
  │                                                             APPLIED — restrictive [D8]
  ├─ changes only a deliverable list inside an approved phase?
  │     └─ needs a §5/§6 change? ── no ──────────────────────► refinement, apply     [D2/D4]
  │                              └─ yes ─────────────────────► amendment             [D4 tripwire]
  └─ changes a phase's set/outcome, a §3 claim, §5, §6, §7, §1
        └────────────────────────────────────────────────────► §12 PROPOSED
                                                               EXTEND | SUPERSEDE   [D9]
                                                               ▼
                                                       owner verdict
                                                       ├─ ✅ apply → re-freeze commit [D7]
                                                       └─ ❌ row stays; original holds
```

**Hypothesis outcomes:**

| | H1 | H3 | H6 |
|---|---|---|---|
| Predicted | few escalations | header + §12 sufficient | narrow channel |
| Measured | 76% / 4.6 per iteration | header cannot name its baseline | full second contract |
| Verdict | ❌ refuted | 🟡 partial | ✅ confirmed, understated |
| Design consequence | granularity, not scope (D2) | git baseline reference (D5/D6) | derivation-only Phase HL (D10) |

## Iteration Status

- **Iteration:** 1 of 2 (min) / 3 (max)
- **Hypotheses tested:** H1 (❌ refuted), H3 (🟡 partially confirmed), H6 (✅ confirmed and understated)
- **Hypotheses deferred:** H11, H12, H13 — iteration 2 by design. H2, H7, H8, H9, H10 settled upstream and not re-litigated
- **Gaps discovered:** (1) no owner-initiated amendment path — S6 with polarity reversed; (2) no re-freeze rule after an approved amendment — the second baseline is where it is lost; (3) `❌ REJECT` branch (a) is an unlogged contract edit and re-entry silently thaws; (4) no non-substantive carve-out, so a broken link is formally an amendment; (5) salami accumulation of free refinements is unlogged and no classification rule closes it; (6) `templates/RES.md:32` can survive Phase A intact and reproduce DoF-1 inside the enforcement site; (7) the principle chain has an extra unapproved link at phase level, which changes which reference set the iteration-2 goal check must read
- **Superseded decisions:** None. D19 is narrowed, not revoked, exactly as HL Principle 6 requires — research still feeds the HL; only the frozen channel changes from write to propose

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | The reference set for the goal check includes an unapproved phase-level link (Extract E6) | If the Judge check reads the *phase* HL's §7, it validates against a principle list authored below the owner's approval — the self-referentiality Phase C exists to break, one level down. TFW-48 is the proof: master P7 "Independent Review Protects the North Star" did not survive into the phase HL that its reviewers then checked against | Iteration 2 must specify the goal check's reference set as **master HL (frozen baseline) + north star**, explicitly excluding phase HL and TS |
| 2 | TFW-48's master HL already carried DoD-11 and P7 goal defence and lost both (Gather G3) | The strongest available evidence that a stated goal without a retention mechanism does nothing — and a warning that Phase C's check can be written correctly and still evaporate | Use it as a negative control in the DoD-23 replay: would the drafted check have fired on TFW-48/49 phase reviews *given that the master already demanded it*? |
| 3 | Salami residual (Challenge C2, Q3) | The one mechanism from HL §11 S3 that survives inside the recommended fix | Cheap to test at Phase A/B TS time: does a `git diff` against the freeze baseline at the pre-TS gate cost anything? |
| 4 | Verdict vocabulary and whether goal rejection needs a name distinct from REJECT | Iteration 2's assigned scope; iteration 1 adds a constraint — D11 redefines REJECT branch (a), so any new verdict class must compose with the amendment protocol, not around it | Coin the terms against D28 with the amendment protocol already fixed |

### Recommendation

- [x] **SUFFICIENT** — proceed. Iteration 1's three hypotheses are resolved with primary evidence, and the design question it was launched to answer (does the freeze cost too much?) has a number and a remedy that needs no amendment.
- [ ] MORE NEEDED
- [ ] BLOCKED

Sequencing note for the coordinator: `min_iterations: 2` is not yet met and iteration 2 (goal defence) is
scoped and ready in `iterations.yaml`. The five amendment proposals above are independent of iteration 2 and
can be ruled on before it starts — doing so is itself the first live exercise of the protocol.

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 1 set out to price the freeze and found the price was being charged for the wrong thing. H1 is
refuted hard — 76% of 213 historical recommendation rows target the frozen set, and 35 of 36 research
iterations would have escalated — but the traffic is not goal traffic. Two thirds of it is specification of
deliverables inside phases the owner had already approved, and only 12% of the entire corpus touches Vision,
DoD, DoF or Principles. The remedy is therefore not to shrink what the owner approved but to define what
counts as changing it, and HL §4 Phase A deliverable 3 already delegated that definition downward — so the
fix that cuts escalation from 4.6 to ~2.3 per iteration ships without a single amendment to the freeze. H6
came back worse than written: TFW-48's Phase A HL is not a leaky deliverable list but a complete second
contract with its own acceptance criteria, and three of the master's approved principles did not survive the
derivation — one of them being the north-star defence that TFW-53's Phase C is now re-inventing. H3 half
holds: no new file is needed, but a header cannot name its own baseline, and the diffability DoD-5 promises
requires a reserved commit scope plus a re-freeze after every approved amendment.

What research provided that the design would have missed: the escalation number and its distribution, without
which C1 would have shipped into the CCB failure band and produced a §12 full of approved drift — worse than
today, because the drift would carry a paper trail asserting it was authorised; the granularity/scope
separation, which is invisible until the corpus is re-modelled per configuration; and three holes that no
amount of careful drafting would have surfaced, because every artifact in this task is written from the
researcher's seat — the owner has no way to propose an amendment, an approved amendment has no re-freeze, and
`❌ REJECT` is a legal bypass around the whole protocol.

Self-critique. The 76% is an upper bound, and Challenge says so: `plan.md` Step 6c aims research at scope, so
part of the §3/§4 concentration is endogenous to the regime being measured, and the number of those 162 rows
an owner would actually have refused is unknowable from artifacts. The C3/C4 projections are row-by-row
re-classifications by the same researcher who wrote the classification rule — internally consistent, not
independently verified. And the salami residual is conceded rather than solved: twelve individually
defensible deliverable refinements that sum to a new phase are precisely HL §11 S3's mechanism, and they
remain unlogged under the design this iteration recommends.

---

*RES — TFW-53: Contract Calibration (Iteration 1) | 2026-08-08*
