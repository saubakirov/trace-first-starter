# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-53](../../HL-TFW-53__hl_contract_and_goal_defence.md)
> Goal: An approved HL becomes a frozen strategic contract that research may only amend through a logged, evidenced, owner-ruled channel.

**OODA loops run:** 3 of 3. L1 — configuration space. L2 — escalation modelling per configuration. L3 — the granularity/scope separation and its consequences.

---

## Configuration Space

Cross-product of Gather's eight dimensions. The full space is 4⁸; per the template's >30 rule, C1 is the
design exactly as the frozen HL §3 describes it, and every further row differs from C1 in ≥1 dimension.
No evaluation here — elimination happens in Challenge.

| Config | D1 Scope | D2 Granularity | D3 State | D4 Classify | D5 Batching | D6 Asymmetry | D7 Phase HL | D8 REJECT |
|--------|----------|----------------|----------|-------------|-------------|--------------|-------------|-----------|
| **C1 As-approved** | A all six | A whole section | B header+§12 | A researcher | B per iteration | A symmetric | *(unspecified)* | A independent |
| **C2 Narrow set** | B outcome set §1§5§6§7 | A whole section | B header+§12 | A researcher | B per iteration | A symmetric | C derived-only | B redefine (a) |
| **C3 Claim-level** | A all six | **B declarative claims** | C +baseline ref | A researcher | B per iteration | A symmetric | C derived-only | B redefine (a) |
| **C4 Claim-level + asymmetric** | A all six | B declarative claims | C +baseline ref | C two-key | B per iteration | **C restrictive-logged** | C derived-only | B redefine (a) |
| **C5 Item-level** | A all six | C numbered items | C +baseline ref | A researcher | B per iteration | C restrictive-logged | C derived-only | B redefine (a) |
| **C6 Goals-only** | C §1+§3 | A whole section | B header+§12 | B coordinator | B per iteration | A symmetric | B abolished | A independent |
| **C7 Acceptance-only** | D §5+§6 | C numbered items | B header+§12 | A researcher | B per iteration | A symmetric | B abolished | A independent |
| **C8 Structural lock** | A all six | A whole section | **D filesystem marker** | A researcher | B per iteration | A symmetric | A inherit | A independent |
| **C9 Deferred gate** | A all six | B declarative claims | C +baseline ref | A researcher | **C at pre-TS gate** | C restrictive-logged | C derived-only | B redefine (a) |
| **C10 Passive log** | A all six | B declarative claims | C +baseline ref | A researcher | **D no push; owner reads §12** | C restrictive-logged | C derived-only | B redefine (a) |
| **C11 Rule-table** | A all six | B declarative claims | C +baseline ref | **D mechanical rule table** | B per iteration | C restrictive-logged | C derived-only | B redefine (a) |
| **C12 Impact-classed** | A all six | B declarative claims | C +baseline ref | C two-key | B per iteration | **D impact-classed** | C derived-only | C amendment before re-entry |
| **C13 No phase HL** | A all six | B declarative claims | C +baseline ref | A researcher | B per iteration | C restrictive-logged | **B abolished** | B redefine (a) |
| **C14 Phase contract** | A all six | B declarative claims | C +baseline ref | A researcher | B per iteration | C restrictive-logged | **D own approval gate** | B redefine (a) |

---

## Findings

### E1 — The frozen/free axis is not the axis that controls cost. Granularity is.

G1 measured escalation load against **D1 (which sections)**. Modelling the same 213 rows against
**D2 (what unit inside a section)** separates two variables the HL treats as one.

Modelled escalation load per configuration. C1 is an exact count from G1; the rest are projections applied
row-by-row to the same corpus and are marked as such.

| Config | Escalating rows / 213 | Iterations that escalate / 36 | Mean proposals per escalating iteration |
|--------|----------------------|-------------------------------|------------------------------------------|
| **C1 As-approved** | 162 — 76% *(counted)* | 35 — 97% *(counted)* | 4.6 |
| **C2 Narrow set** (§1§5§6§7 whole-section) | ~26 — 12% *(projected)* | ~19 — 53% | ~1.4 |
| **C3 Claim-level** (all six, declarative only) | ~66 — 31% *(projected)* | ~26 — 72% | ~2.5 |
| **C4 Claim-level + restrictive-logged** | ~56 — 26% *(projected)* | ~24 — 67% | ~2.3 |
| **C5 Item-level** | ~95 — 45% *(projected)* | ~31 — 86% | ~3.1 |
| **C7 Acceptance-only** (§5§6) | ~15 — 7% *(projected)* | ~15 — 42% | ~1.0 |

Projection method: each of the 213 rows was re-tested against the configuration's protected unit. For
C3/C4 a row escalates if it changes the phase *set* or a phase's declared outcome, a §3 to-be claim, a §5/§6
item, a §7 principle, or §1 — and applies freely if it only specifies a deliverable list inside an approved
phase. C4 additionally releases the ~15% restrictive rows from G2 into `APPLIED — restrictive`.

**The gap between C1 (4.6) and C2 (1.4) is entirely a definitional choice, and it is not the choice the HL
argued about.** HL §3's frozen/free table debates *sections*; the cost driver is *what counts as a change to
a section*. Two configurations with an identical frozen section list differ by a factor of 3.3 in owner
interruption.

### E2 — The combination nobody proposed: C3/C4 need no amendment to ship

This is the Extract test's answer, and it is not a compromise between the alternatives — it is orthogonal
to them.

Every response to G1's number that was visible in the Briefing involves shrinking the frozen set, which
means **amending HL §3** — a frozen section — on the first research iteration of the task that invented the
amendment protocol. That is not fatal (it would be an honest first exercise of the mechanism), but it is
expensive: it reopens the owner's central decision and it weakens the demonstration.

C3 and C4 do not require it. HL §3's table freezes *sections*; it never defines what constitutes a change to
one. That definition is explicitly delegated downward — **HL §4 Phase A deliverable 3: "`conventions.md` §3 —
HL Contract definition: what freezes, when, what append-only means for §12."** "What freezes" is inside
approved Phase A scope. Defining the frozen unit as *declarative claims* rather than *whole section text*
therefore lands as a Phase A design decision, not as an amendment.

Consequences:
- HL §3's frozen list stays exactly as approved. Zero amendments from iteration 1 on the freeze question.
- DoF-2 ("freezing so broad that routine research output triggers escalations") is answered by construction
  rather than by shrinking the promise.
- The owner's approval keeps its meaning: all six sections are still frozen. What changed is that "we will
  add `mkdocs-literate-nav` to `requirements.txt`" stops counting as a contract change, which no reading of
  §1 Vision ever claimed it was.

### E3 — DoD as the tripwire: a free-granularity rule needs a bound, and one already exists

C3/C4's obvious hole: if deliverable lists inside a phase are free, a phase can absorb an entire new
capability one deliverable at a time — TFW-48's Phase A behaviour, relocated. The bound must be mechanical,
not judgemental.

**Proposed rule (Phase A design decision, not an amendment):** *a change to a deliverable list is a
refinement only if it requires no change to §5 DoD or §6 DoF. If the deliverable cannot be accepted under
the existing acceptance criteria, it is an amendment.*

This is testable against the corpus, and it holds:

| Corpus case | Deliverable change | DoD row in the same RES? | Rule's verdict | Correct? |
|---|---|---|---|---|
| TFW-22 #1 — replace Phase C's `research.md` enrichment with a `research/` directory architecture | large | **yes** — #9 "Update DoD to include: research/ directory, YAML mode config…" | escalate | yes — this *is* a contract change |
| TFW-38 iter4 #1–#4 — four "Add Phase A scope: …" rows | moderate | **no** | apply freely | yes — enrichment serving an already-approved DoD |
| TFW-25 U3 — "Phase A step 1: include 'Honesty Over Convincingness' rewrite" | small | **yes** — U4/U5 change DoD counts | escalate | yes — the count *is* the acceptance criterion |
| TFW-47 iter2 #1–#5 — Phase B/C deliverables: replace "verify" with "document" | wording | no | apply freely | yes — the deliverable was already approved; research only learned it was already true |
| TFW-27 #2 — "Phase B scope: 4 features, ~120 LOC" | large | **yes** — #3 "Phase B DoD update" | escalate | yes |

Five for five. The rule reuses a section that is already frozen at item level, adds no new concept, and is
checkable by reading two tables. It also gives the researcher a mechanical classification test, which
matters for D4.

### E4 — §12 needs a change-type column, and ADR practice supplies the vocabulary

The HL §3 example log has columns `# · Date · § · Proposed change · Evidence · Alternatives · Verdict`.
Three distinct operations are being funnelled through one row shape, and they have different consequences
for the baseline (G7):

| Type | What happens to the frozen text | What happens to the baseline | Corpus example |
|------|--------------------------------|------------------------------|----------------|
| `EXTEND` | untouched; a clause is added elsewhere | unchanged — the original still holds in full | TFW-46 R7 "consider adding 'Testing ≠ Evidence'" to §7 |
| `SUPERSEDE` | a named claim is replaced | **re-freeze at a new baseline** | TFW-22 #1 replacing Phase C's architecture |
| `APPLIED — restrictive` | tightened, applied immediately, logged not gated (D6 Alt C) | unchanged; the contract can only have got narrower | TFW-27 #1 removing the artifact graph |

Without the column, an `EXTEND` and a `SUPERSEDE` arrive at the owner looking identical, and the owner
must reconstruct the difference from the prose — which is the CCB rubber-stamp mechanism from G8
(no impact assessment → default approve). One column, three values, zero new sections. F22-compatible.

### E5 — Phase HL: three viable governance forms, and the working tree already votes

Evidence spread across the corpus:

| Observation | Reading |
|---|---|
| TFW-42, TFW-46 ran multi-phase with phase folders and **no phase HL at all** | The artifact is optional in practice; work completes without it |
| TFW-47's phase HLs are verbatim transclusions of master §4 | When constrained, the artifact carries zero information |
| TFW-48's phase HLs are full second contracts | When unconstrained, the artifact carries a whole unapproved contract |
| No `templates/PhaseHL.md` exists; `conventions.md` §3 does not define the type | The class is defined by whatever the last agent wrote |
| `conventions.md` §15 grants `resume.md` (Coordinator) the right to write Phase HL | The authority exists; the constraint does not |

The three survivable forms:
- **D7 Alt B (abolish)** — the phase's authority is master §4 plus the phase TS. Supported by TFW-42/46
  completing without one and by TFW-47's being informationally empty. Cost: a Phase TS for a late phase then
  has no intermediate artifact carrying "what changed since the master was written"; `resume.md` loses a
  permitted output.
- **D7 Alt C (derivation-only)** — a Phase HL may restate master content and add execution context, but may
  not contain §1, §5, §6 or §7 of its own. Directly blocks TFW-48's failure while keeping the artifact.
  Cheapest: one sentence in `conventions.md` §3 plus one §14 anti-pattern.
- **D7 Alt D (own approval gate)** — a second contract with a second owner ruling. Honest, and it doubles the
  approval events per task, which is the interruption budget TFW-53 exists to protect.

Note the coupling to D2: under C3/C4, a derivation-only Phase HL that restates the master's phase outcome and
lists deliverables is *exactly* a free-granularity artifact. The two rules compose without a special case.

### E6 — The reference-point cascade is one level shorter than HL §3 describes

HL §3 states the principle chain as `HL §7 → TS §3 → RF §3 → judge.md row 2`, self-referential because HL §7
is coordinator-authored. G3 adds a link the chain diagram omits:

```
master HL §7 (owner-approved)
   ↓  ← TFW-48: three principles dropped here, no gate, no diff
phase HL §7 (coordinator-authored, unapproved, no template)
   ↓
phase TS §3 Principles Check
   ↓
phase RF §3
   ↓
judge.md row 2 — mapping integrity against the phase's own principle set
```

The self-referentiality is therefore worse than diagnosed: the reviewer's principle check in a multi-phase
task can be validating against a principle list that was *authored one level below the owner's approval and
never compared to it*. This is inside iteration 1's remit only as a fact; the consequence for the Phase C
design (which reference set the goal check reads) belongs to iteration 2 and is carried as an open thread.

### E7 — What "committed before research" actually has to mean

DoD-5 requires the approved HL committed before the first research iteration. G4 shows the header cannot name
its own commit. Working through the operational sequence exposes a second requirement nobody has stated:

```
1. owner approves          → coordinator writes header: Contract: 🔒 FROZEN, approved YYYY-MM-DD
2. coordinator commits      → [agent/TFW-NN/freeze/coordinator] freeze approved hl
                              ^^^^^ reserved scope word makes the baseline findable
3. research runs            → RES classifies; frozen-targeting findings become §12 rows
4. owner rules              → approved rows applied
5. coordinator re-commits   → [agent/TFW-NN/freeze/coordinator] re-freeze at amendment A2
```

Step 5 is the part the HL does not specify and DoF-7 half-anticipates. If an approved amendment is applied
without a new freeze commit, the *second* baseline is the one that becomes unverifiable — TFW-48's failure
mode reproduced after the first amendment rather than before the first research iteration. `git log --grep`
on the reserved scope then returns the full freeze history of the contract, in order, with diffs between
consecutive baselines. This is what makes "the baseline is diffable" true across a task's whole life rather
than only at its start.

The reserved scope word is the only new convention required, and D55's `[agent/task/scope/role]` grammar
already has the slot.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Granularity (D2), not scope (D1), controls escalation cost — 4.6 vs 1.4 proposals per iteration with an identical frozen section list | Whether "declarative claim" is expressible without ambiguity by a non-adversarial agent — Challenge |
| **C3/C4 require no amendment**: HL §4 Phase A deliverable 3 already delegates "what freezes" to `conventions.md` | Whether the coordinator would actually read it that way, or treat it as a loophole — Challenge |
| DoD-as-tripwire bounds the free granularity; validated 5/5 against the corpus | Adversarial case: an agent that avoids escalation by *not* proposing the DoD change — Challenge |
| §12 needs a change-type column (`EXTEND` / `SUPERSEDE` / `APPLIED — restrictive`); ADR practice supplies the semantics | — |
| Phase HL: derivation-only (D7 Alt C) composes with C3/C4 without a special case; abolition also viable | Which one the owner prefers — carried to RES Open Questions |
| The principle chain has an extra unapproved link at phase level | Consequence for the Phase C reference set — iteration 2 open thread |
| Re-freeze after an approved amendment is unspecified and is where the baseline is lost the *second* time | — |

**Sufficiency:**
- [x] External source used? — ADR `supersede` vs `amend/extend` semantics imported as §12's change-type vocabulary
- [x] Briefing gap closed? — the "shrink the set or shrink the unit" question from the Briefing now has a modelled answer
- [x] Configuration Space built from Gather dimensions? — 14 configurations across all 8 dimensions
- [x] *(deep)* Hypothesis tested? — H1's consequence re-tested under 6 configurations; H3 resolved into the freeze-commit sequence
- [x] *(deep)* Counter-evidence sought? — E3 is written as the attack on E2 and answered mechanically; the residual adversarial case is handed to Challenge

**Metacognitive check.** E2 is new and was not reachable from the Briefing: the response to a refuted H1 does
not have to be an amendment, because the HL delegated the definition that carries the cost. E1's factor-of-3.3
was not visible before the corpus was re-modelled per configuration. E6 and E7 are new consequences rather
than new data. Unchecked source: no attempt was made to measure how many of the 213 rows the *owner* would
have rejected had they been asked — that number is unknowable from artifacts and is the honest limit of the
G1/E1 estimates.

Stage complete: YES
→ User decision: autonomous run — advancing to Challenge without a gate, per owner instruction.
