# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-53](../../HL-TFW-53__hl_contract_and_goal_defence.md)
> Goal: An approved HL becomes a frozen strategic contract that research may only amend through a logged, evidenced, owner-ruled channel.

**OODA loops run:** 3 of 3 (deep mode).
L1 — corpus census + classification (H1). L2 — Phase HL forensics (H6) + state-mechanism enumeration (H3). L3 — external regimes + counter-evidence sweep.

---

## Dimensions

Eight independent decision factors. Each is a degree of freedom the shipped contract must pick a value for.
No alternative is marked recommended — all stay open until Challenge.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| **D1 Freeze scope** — which sections freeze | All six: §1 §3 §4 §5 §6 §7 (HL as approved) | Outcome set: §1 §5 §6 §7 (goals + acceptance + values; §3/§4 free) | Goals only: §1 §3 | Acceptance only: §5 §6 |
| **D2 Freeze granularity** — what unit inside a frozen section is protected | Whole section text (any diff = amendment) | Declarative claims only — phase set + each phase's declared outcome; deliverable lists inside a phase stay free | Numbered items (a DoD item, a phase, a principle) — add/remove/reword = amendment, renumber = free | Headline sentence per section; body is commentary |
| **D3 Contract state mechanism** | Header field only (`Contract: 🔒 FROZEN`, date) | Header field + append-only §12 Amendment Log (HL §3 proposal) | Header field + §12 + **baseline commit reference** (SHA or annotated tag) | Filesystem marker per D31 — `contract.lock` / frozen HL snapshot file in the task folder |
| **D4 Classification authority** — who names the target section of a finding | Researcher classifies in RES; coordinator applies verbatim | Coordinator classifies at Step 6c; RES stays unclassified | Researcher classifies, coordinator verifies before applying (two-key) | Mechanical rule table in `conventions.md`; both parties read the same map |
| **D5 Escalation batching** | One message per proposal, as found | One batched message per research iteration (HL Principle 4) | One batched message at the pre-TS gate — all iterations at once | Continuous log, no push at all; owner reads §12 when they choose |
| **D6 Freeze asymmetry** — does change direction matter | Symmetric: any edit to a frozen section is an amendment | Restrictive-free: tightening (add DoF, narrow scope, drop a deliverable) applies directly; loosening escalates | Restrictive-logged: tightening is logged in §12 as `APPLIED`, not gated | Impact-classed: escalation triggered by cost/blast-radius, not by direction |
| **D7 Phase HL governance** | Phase HLs inherit the master freeze — same frozen sections, same protocol | Phase HL abolished; the phase's authority is the master §4 entry + the phase TS | Phase HL is derivation-only: it may restate master content, never introduce DoD/DoF/Principles of its own | Phase HL gets its own owner approval gate and its own contract state |
| **D8 REJECT composition** | Independent: `❌ REJECT` and the amendment protocol never interact | REJECT (a) "rework HL" branch is redefined as *file an amendment*, not *edit the HL* | A REJECT on goal grounds requires an amendment before re-entry to any status | New terminal verdict class distinct from REJECT, routed to owner |

---

## Findings

### G1 — H1 corpus census: the frozen set absorbs 76% of historical research output

**Method.** Every `RES*.md` under `tasks/` was scanned for an `HL Update Recommendations` table (36 research
iterations across 27 tasks — a wider corpus than the six tasks the briefing named, deliberately, because a
larger denominator makes the count harder to dismiss). Each row was assigned to the HL section it targets, then
to `FROZEN` or `FREE` per the HL §3 table. Rows naming their section explicitly (`§4 Phase A`, `§10 H5`) were
taken at face value; rows naming a deliverable or scope change were assigned to §3/§4; rows naming a follow-up
task or a parking-lot entry were assigned FREE.

| Metric | Value |
|--------|-------|
| Research iterations with an `HL Update Recommendations` table | 35 of 36 |
| Total recommendation rows | **213** |
| Rows targeting a **frozen** section (§1 §3 §4 §5 §6 §7) | **162 — 76.1%** |
| Rows targeting a **free** section (§2 §7.2 §8 §9 §10 §11) | 51 — 23.9% |
| Iterations that would fire **≥1 amendment escalation** | **35 of 36 — 97%** |
| Mean amendment proposals per iteration | **4.5** |
| Iterations producing zero HL recommendations | 1 (TFW-46 iter2) |

Per-section breakdown of the 162 frozen-targeting rows:

| Target | Rows | % of all 213 | Character of the traffic |
|--------|------|--------------|--------------------------|
| §4 Phases — deliverable lists inside an already-approved phase | ~78 | ~37% | "Phase A scope: add X", "Phase B deliverables: replace verify with document" |
| §3 Target State (incl. §3.1/§3.2) | ~58 | ~27% | Redefinition of the to-be picture, terminology tables, architecture claims |
| §5 DoD + §6 DoF | ~15 | ~7% | Numbers and thresholds: "6-8 values → exactly 8", "≤130 → ≤110 lines", "5 posts → 7" |
| §7 Principles | ~8 | ~4% | New principle added after research named it |
| §1 Vision | ~3 | ~1.4% | Three rows in the whole corpus |

**Sensitivity.** About 10 rows are genuinely ambiguous (parking-lot entries, "add consistency table reference
to HL", "add new future task"). Assigning every ambiguous row to FREE moves the frozen share from 76.1% to
**71.4%** and does not change any iteration's escalate/don't-escalate outcome. The finding is not an artefact
of classification charity.

**Verdict on H1: refuted, decisively.** The hypothesis predicted that a large majority of rows target free
sections. The measured majority runs the other way by better than 3:1. Under the HL §3 split as approved, a
multi-phase task with `min_iterations: 2` escalates in essentially every iteration, carrying a median of 4–5
proposals per escalation.

**But the number is not evenly distributed, and that is the load-bearing part.** Two thirds of the frozen
traffic (§4 + §3, ~136 of 162 rows) is *specification of an already-approved intent* — the deliverable list
inside a phase whose existence and purpose the owner already approved. Only ~26 rows in the entire corpus
(12%) touch Vision, DoD, DoF or Principles. Freezing at the section level and freezing at the claim level are
therefore quantitatively different designs: the first escalates 4.5 times per iteration, the second roughly
1.4 times per escalating iteration and on ~53% of iterations.

### G2 — Direction of drift: ~85% of frozen-targeting rows widen, ~15% narrow

Rows that *remove* scope are countable and rare: TFW-27 #1 ("Remove artifact graph from all phases"),
TFW-23 #3 ("Remove `content_language` from TFW-23 scope"), TFW-32 iter3 #5 ("REMOVE the rename action item
from Phase A scope"), TFW-47 iter2 #3 ("Remove as open question"), TFW-50 HL3/HL4 (narrow to commit-subject
format only; drop the three-phase implication), TFW-52 iter3 HL-R1 ("Demote the stable-looking Team topology
statement to an experimental candidate"). Roughly 15% of frozen-targeting rows.

The remaining ~85% add a deliverable, add a phase, broaden a DoD number, or replace a target-state claim with
a larger one. This is the quantitative footprint of HL §11 S3 — *«с каждым ресерчем… чуть-чуть раздувается»* —
and it is measurable, not anecdotal. It also identifies exactly which rows a **direction-asymmetric** freeze
(D6 Alt B/C) would let through for free.

### G3 — H6: Phase HLs are not a leak, they are a second unapproved contract

Full census of Phase HL files that have ever existed in this repository:

| Task | Phase HLs | Where |
|------|-----------|-------|
| TFW-47 | phase-a, phase-b | working tree |
| TFW-48 | phase-a, phase-b, phase-c, phase-d | git history only (`721ca15`) |
| TFW-49 | phase-a, phase-b, phase-c | git history only (`721ca15`) |
| TFW-32, TFW-41 | none | the briefing's premise that these have phase folders is incorrect |
| TFW-42, TFW-46 | phase folders exist, **no phase HL** | TS/RF/REVIEW only |

Two distinct species, and the difference is the finding:

**Species 1 — TFW-47, the benign form.** `phase-b/HL__phase-b__codex_adapter.md` is 50 lines: parent link,
the master's Context block, the master's ten deliverables. Diff against master §4 Phase B: **zero introduced
content**. It is a transclusion with a header. Harmless — and also pointless, which matters for D7 Alt B.

**Species 2 — TFW-48, the drift form.** `phase-a/HL__phase-a__method_kernel.md` is a *complete HL*: its own
§1 Vision, §2 As-Is, §3 Target State with §3.1 and §3.2, §4, **§5 DoD with 10 items**, **§6 DoF with 9 items**,
**§7 Principles with 10 items**, §7.1 Quality Contract, §7.2 Knowledge Citations (11 rows), §8, §9 Risks (7 rows),
§10 Hypotheses. None of the master's 19 DoD items, 18 DoF items or 13 principles appear verbatim. Concretely:

| Master TFW-48 | Phase A HL | Effect |
|---|---|---|
| §4 Phase A: 6 deliverables | 7 deliverables; master's item 4 split into three | Scope respecified below the approved grain |
| §5: 19 DoD items (task-wide) | §5: 10 **new** DoD items scoped to the phase | A second acceptance contract nobody approved |
| §6: 18 DoF items | §6: 9 **new** DoF items, incl. #9 "Workflows, templates, adapters, config values, project state, historical traces, or production repositories are modified in this phase" — a constraint absent from the master | New constraints created at phase level |
| §7: 13 principles | §7: 10 principles. Master **P7 "Independent Review Protects the North Star"**, **P10 "Breaking Change With a Bridge"** and **P12 "No Arbitrary Compression Target"** do not survive | Three approved values silently dropped |
| Header: `📝 HL_DRAFT` on master | `✅ HL — Approved scope derived from master HL` | A self-declared approval status the framework does not define |

The dropped P7 is the sharpest single fact in this iteration: TFW-48's master HL already contained
**DoD-11 — "Review can reject work that satisfies TS/RF but violates the product north star"** and
**P7 — "Independent Review Protects the North Star… the last quality authority before project learning and
closure."** TFW-53's Phase C is, in substance, an owner-approved goal that TFW-48 had already approved and
then lost — first from its own Phase A HL, then entirely on revert. The framework did not fail to think of
goal defence; it failed to hold on to it. That is a contract-retention failure, which is exactly the class of
failure this task exists to fix.

**Verdict on H6: confirmed, and worse than stated.** HL §10 records "TFW-48/49 phase HLs showed no content
drift (only marker commits)" — that describes the phase HLs' *commit* history, not their content, and it is
misleading. The channel is not "a phase HL adds a deliverable." It is "a phase HL re-derives the entire
contract, including acceptance criteria and values, with no approval gate and no conformance check."

**Structural cause.** There is no `templates/PhaseHL.md`. `conventions.md` §3 does not define a Phase HL
artifact type. `conventions.md` §15 grants `resume.md` (Coordinator) permission to write "Phase HL + TS" with
no template, no gate and no bound on content. An artifact class with authority and no template is defined by
whatever the last agent wrote — which is exactly what happened.

### G4 — H3: a header field cannot reference its own baseline, and that is not a detail

The contract-state question decomposes into two requirements that the HL treats as one:
**(i) is this HL frozen?** and **(ii) frozen *as what*?** DoD-5 demands the second explicitly — the baseline
must be *diffable*, closing TFW-48's unverifiable-drift mode.

| Mechanism | Answers (i) | Answers (ii) | Cost | Failure mode |
|---|---|---|---|---|
| Header field only | yes | **no** | zero | TFW-52 already invented `✅ HL_APPROVED` unaided; states drift is detectable but not measurable |
| Header field + §12 log | yes | only for changes that were *declared* | zero | An undeclared edit leaves no trace — precisely TFW-49 `642c647` |
| Header + §12 + **baseline commit ref** | yes | yes | one convention | Requires solving the self-reference problem below |
| Filesystem marker (D31) | yes | only if it stores a snapshot | +1 file per task; snapshot duplicates the HL | Two copies of the contract can disagree; F22 template minimalism |

**The self-reference problem.** A commit's SHA cannot appear inside the content of that same commit. So
`Baseline: 8136306` cannot be written into the HL by the same act that freezes it. Three resolutions exist:

1. **Two-commit** — freeze commit, then a second commit writing its SHA into the header. Honest, but the
   header is wrong for exactly one commit, and the second commit is itself an edit to a frozen section.
2. **Annotated tag** — `git tag hl-freeze/TFW-53 <sha>`; the header records the *tag name*, which is knowable
   in advance. One command, no second commit, diffable forever via `git diff hl-freeze/TFW-53 -- <HL path>`.
   Cost: tags are repo-global namespace and must be pushed explicitly; a project without a remote still works.
3. **Commit-subject convention** — no reference in the header at all; the freeze commit is *findable* because
   its subject follows a fixed shape. TFW-50's D55 already ships the vehicle:
   `[agent/task/scope/role] summary`. A reserved scope word makes the baseline recoverable with one command:
   `git log --grep="\[.*/TFW-53/freeze/" --format=%H`. This task's own freeze commit is `8136306
   [claude-code/TFW-53/task/coordinator] freeze approved hl and prepare research` — recoverable today only
   because the summary happens to say "freeze"; under a convention it would be deterministic.

**Verdict on H3: partially confirmed — the "no new file" half holds, the "sufficient" half does not.**
No filesystem marker is needed and D31 does not demand one: D31's principle is *file existence = state*, and
the HL file plus git history already carry the state. But a header field plus §12 alone does not satisfy
DoD-5, because neither names the baseline. The missing piece is a **baseline reference**, and the cheapest
form that survives F22 (template minimalism) and D54 (tool-agnostic) is a reserved commit scope word plus an
optional tag, not a new artifact.

### G5 — Freeze asymmetry: the two directions have different failure modes, and one is already covered

The blind spot asks whether tightening a DoF and loosening a DoD need the same path. The corpus (G2) says
~15% of frozen traffic is tightening. Three arguments cut against symmetric treatment and two cut for it:

*Against symmetry* — (a) DoF-2 is triggered by escalation volume; making the 15% free is a 15% reduction at
zero risk to the stated failure modes, all of which are *widening* failures (§6 DoF-2, DoF-9, and the whole
of §2's evidence). (b) The owner's stated pain is inflation, never contraction. (c) HL §9 records
"Contract makes legitimate mid-task learning feel adversarial" as a risk; the free-tightening path is its
natural mitigation.

*For symmetry* — (d) "Tightening" is not self-evident: dropping a deliverable narrows work but may also
abandon a promised outcome, which is a goal change wearing a scope-reduction costume. TFW-27 #1
("Remove artifact graph from all phases") reads as tightening and is in fact a target-state redesign.
(e) An agent that can classify its own change as restrictive has an incentive gradient, and TFW-49 S13
established that a grant which can justify its own extension is the root cause — a self-served
"this is only a tightening" is the same move in the opposite direction.

Argument (e) is decisive against **Alt B** (restrictive-free) and points at **Alt C** (restrictive-logged):
tightening applies immediately *and* lands in §12 with verdict `APPLIED — restrictive`, so the owner sees it
without being asked to rule on it. Volume drops, visibility does not.

### G6 — REJECT composition: the existing branch already names the amendment path, unlabelled

`conventions.md` §5 today: `❌ REJECT → 🛑 User decides: (a) 📝 HL_DRAFT (rework HL), (b) 🔬 RES (new research),
(c) 🟡 TS_DRAFT (rewrite TS)`. D20 supplies the semantics: "Implicit approval = transition to next status."

Two collisions with the contract:

1. **Branch (a) is an unlogged contract edit.** "Rework HL" after a REJECT reopens frozen sections with no
   proposal, no evidence, no §12 row — the exact act the protocol prohibits everywhere else, permitted here
   because it happens *after* a rejection rather than during research. The fix is a redefinition, not a new
   branch: branch (a) becomes "file an amendment against the frozen sections; owner rules; approved →
   re-freeze at the new baseline."
2. **`❌ REJECT` has no terminal status.** The verdict exists in §5 as a routing decision; the board has no
   `❌ REJECTED` row (Phase E adds it). So a rejected task is indistinguishable from a blocked one — which is
   how TFW-48/49's board rows survived only 
   until a whole-tree restore.

Third, currently unhandled: **who returns the contract to a rulable state after a REJECT?** D20's implicit
approval means transitioning a status *is* the approval. Under a contract, re-entering `📝 HL_DRAFT` must not
silently thaw the frozen sections — otherwise REJECT becomes the universal bypass and every agent that wants
to move a goal learns to route through it.

### G7 — External: ADR immutability is the closest mature analogue, and it separates two operations TFW conflates

Architecture Decision Records are the industry's nearest working equivalent of a frozen contract, and the
practice is settled: *"ADRs are immutable. When circumstances change and a decision is revisited, you don't
edit the old ADR — you write a new one and mark the old one as superseded."* Immutability there means
"no content changes beyond typos or broken links; anything that changes meaning goes in a new ADR."

The transferable part is a distinction TFW does not currently draw:

| ADR operation | Effect on the original | TFW analogue |
|---|---|---|
| **Supersede** | Original status → `superseded`, link forward; original text untouched | An amendment that *replaces* a frozen claim — re-freeze at a new baseline |
| **Amend / extend** | Original **stays `accepted`**; a link is added to the amending record | An amendment that *adds* without contradicting — §12 row, original text intact |

Two lessons land directly. First, the immutable artefact plus a forward pointer is a proven shape, and it
argues for §12 rows carrying an explicit `supersedes`/`extends` type. Second, ADR practice permits typo and
link fixes to an immutable record — a materiality bar at the artefact level. TFW's freeze as drafted has no
such carve-out, so a broken link in §1 is formally an amendment.

Status vocabulary in the field — `proposed / accepted / deprecated / superseded / rejected` — is also a
sanity check on TFW's own set: TFW has no `superseded` for HLs and no `rejected` for tasks (Phase E adds the
latter).

### G8 — External counter-evidence: change control boards fail in exactly the two directions this design must avoid

The change-control literature is not encouraging about approval gates, and it names TFW's two named risks
without knowing about them:

- **Rubber stamp** — *"the board approves everything because declining a change request requires a rationale
  that nobody wrote down. Change requests arrive without impact assessments, so the board has no basis for
  rejection."* This is a direct empirical argument for HL Principle 5 (*evidence, cost, alternative — no
  proposal without all three*): the rationale burden must sit on the **proposer**, or the ruler defaults to
  approve. It is also a warning about §12's `Alternatives considered` column — if it is optional in practice,
  the gate decays.
- **Bottleneck** — *"a clean scope boundary is required, otherwise the board turns into a bottleneck…
  everything goes to the board… If the board owns execution, it will either drown or start rubber-stamping
  changes to clear the queue."* This is DoF-2 stated by an independent field, with a causal mechanism TFW's
  risk register does not carry: **volume converts a gate into a rubber stamp**. At 4.5 proposals per
  iteration (G1), the owner does not become a stricter approver — they become a faster one.

The prescription both sources converge on is scope boundary discipline: govern the small set of decisions
that actually matter, and let the rest through. That is D2 (granularity), not D1 (scope), doing the work.

- **Repository-level enforcement** — GitHub/GitLab branch protection with `CODEOWNERS` enforces
  approval per *path*, and "any user who is not specified… cannot push changes for the specified files."
  Two facts matter for D3: the industry's unit of protection is the **file**, never a section within it —
  so there is no off-the-shelf mechanism for "§1 is frozen and §9 is not" — and the enforcement is external
  to the artefact, which violates D24 (inline defaults) for an agent that never runs a merge request.
  Structural enforcement for TFW therefore has to be *authored* enforcement (template + workflow gate),
  not borrowed platform enforcement.

### G9 — TFW-52 invented the amendment protocol by hand, three weeks early

`TFW-52/research/iter2/RES.md` ships its `HL Update Recommendations` table with a fourth column the RES
template does not have: **Status**, and every one of its nine rows reads `**UNAPPROVED**`. Each row then gets
its own subsection (`### U1 — Replace H1 wording — UNAPPROVED`). `TFW-52/research/iter1/RES.md` opens the same
section with an unprompted disclaimer: *"Recommendations only. A Coordinator decides and applies any HL changes
through `/tfw-plan`; this RES does not modify the parent HL."*

Neither is required by any template, workflow or convention. A researcher facing a genuinely consequential HL
independently invented (a) a proposal status, (b) per-proposal justification blocks, (c) an explicit
non-authority disclaimer. This is `process.md` F11 (organic emergence → formalisation) firing on the exact
mechanism TFW-53 proposes, and it is evidence that the protocol is *usable*, not merely desirable.

It also supplies a field-tested column name. `UNAPPROVED` (state of the world) reads differently from
`PROPOSED` (state of the request); the HL §3 example uses `PROPOSED`. Worth one line in Phase A.

### G10 — The instruction that produces the drift is still in the RES template, unqualified

`templates/RES.md` line 32, immediately under the section heading:
`<!-- List what should change in HL based on research. Coordinator applies these. -->`

"Coordinator applies these" is the instruction the coordinator reads at execution time, and it is the
generative source of the 213 rows counted in G1. HL §10 H2 was closed on the argument that a
`conventions.md` rule loses to the workflow it governs; this comment is the workflow-side twin of that
finding, sitting in the template rather than in `plan.md`. Any Phase A that changes the table structure but
leaves this comment intact ships a contradiction inside a single file.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| **H1 refuted:** 162/213 rows (76%) target frozen sections; 35/36 iterations would escalate; 4.5 proposals/iteration | Whether the right fix is a smaller frozen *set* or a smaller frozen *unit* — Extract |
| Escalation load concentrates in §4 deliverable lists (~37%) and §3 (~27%); §1+§5+§6+§7 together are 12% | Whether a claim-level freeze on §3/§4 is expressible without ambiguity — Challenge |
| **H6 confirmed and understated:** TFW-48 Phase A HL is a full second contract — 10 new DoD, 9 new DoF, 10 principles, three master principles silently dropped | Whether Phase HLs should inherit the freeze or stop existing — Extract/Challenge |
| TFW-48's master HL already contained goal-defence (DoD-11, P7) and lost it at phase level | Nothing — this is evidence, carried to RES |
| **H3 partially confirmed:** no new file needed, but header+§12 cannot satisfy DoD-5; a baseline reference is required and cannot be self-referential | Which of tag / commit-scope convention survives tool-agnosticism — Challenge |
| Asymmetry: tightening is ~15% of traffic; self-classification incentive rules out restrictive-free, points at restrictive-logged | Pairwise interaction with D4 classification authority — Challenge |
| REJECT branch (a) "rework HL" is an unlogged contract edit and a universal bypass | Exact redefinition wording — RES recommendation |
| ADR practice separates *supersede* from *amend/extend* and permits typo-level edits to an immutable record | Whether §12 needs a change-type column — Extract |
| CCB field evidence: volume converts a gate into a rubber stamp; the proposer must carry the rationale burden | Quantified threshold — none exists; Challenge treats it qualitatively |
| TFW-52 iter2 independently invented `UNAPPROVED` proposal statuses and non-authority disclaimers | — |
| `templates/RES.md:32` still instructs "Coordinator applies these" | — |

**Sufficiency:**
- [x] External source used? — ADR immutability/supersession practice; CCB rubber-stamp/bottleneck failure pair; branch-protection/CODEOWNERS path-level granularity limit
- [x] Briefing gap closed? — H1 has a number, H6 has a mechanism, H3 has an enumerated option set with a disqualifying constraint
- [x] Dimensions identified? — 8 independent factors, ≥3 alternatives each
- [x] *(deep)* Hypothesis tested? — H1, H3, H6 all tested against primary evidence
- [x] *(deep)* Counter-evidence sought? — G8 external failure modes; G2 direction split; the D19 selection effect is raised and deferred to Challenge as the strongest attack on G1

**Metacognitive check.** Three findings were genuinely new rather than confirmatory: (a) the escalation load is
concentrated in *specification* traffic, not goal traffic, which reframes the whole design from "which sections"
to "which unit"; (b) TFW-48 already had goal defence in its approved contract and lost it at phase level — the
framework's problem is retention, not invention; (c) the baseline self-reference problem, which quietly refutes
the simple form of H3. Two were confirmatory: the drift direction and the RES template instruction. Sources not
yet consulted: the TFW-48/49 phase REVIEW files (deliberately — they belong to iteration 2's replay), and AFD
(out of scope this iteration).

Stage complete: YES
→ User decision: autonomous run — advancing to Extract without a gate, per owner instruction.
