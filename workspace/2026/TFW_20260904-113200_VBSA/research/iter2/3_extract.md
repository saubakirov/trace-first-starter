# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260904-113200_VBSA](../../HL-TFW_20260904-113200_VBSA.md)
> Goal: Turn the non-code replay and governance attacks into explicit enforceable configurations without treating any Iteration 1 proposal as approved.

## Configuration Space

The full cross-product of Gather's ten dimensions is mechanically large. These configurations retain every combination that produces a distinct authority, measurement, or compatibility outcome and is not contradictory on its face.

| Config | D1 — non-code metric applicability | D2 — file-count meaning | D3/D10 — classification unit and mixed role | D4/D5 — authority and timing | D6 — cross-phase allocation | D7 — hard-bound basis | D8/D9 — compatibility and carrier |
|---|---|---|---|---|---|---|---|
| X1 — historical whole-hard | Files + LOC everywhere | Absolute hard ceiling | Whole repository diff | Owner waiver after crossing | Count shared path in every phase | Configured threshold alone | Reinterpret all tasks; freehand role totals |
| X2 — literal Iteration 1 hybrid | File count universal; LOC applicable | Absolute configured soft trigger | Whole path VALUE on ambiguity | Coordinator inside six conditions, before work | Phase-attributable path delta | Named harm | Same-key forward change; TS→RF→EV→REVIEW |
| X3 — planned-membership hybrid | File count universal; LOC applicable | Planned-versus-actual membership plus configured soft trigger | Whole measured path on inseparable mixed change | Coordinator prospective; Owner for new accepted output | Separate phase candidates or one path owner | Six-part materiality test | TS approval epoch; existing chain |
| X4 — disclosure only | File count universal; LOC applicable | Cardinality disclosure, never trigger | Whole path | No threshold authority | Separate phase candidate | Explicit hard bounds only | Forward change; existing chain |
| X5 — delivery-specific only | Delivery-specific measures | No universal file signal | Accepted-output component | Coordinator prospective | Component allocation | Named harm | Forward change; existing chain |
| X6 — no numeric control | No numeric signal | None | Accepted-output mapping | Coordinator/Reviewer judge coherence | One path owner | Nonnumeric DoF only | Forward change; existing chain |
| X7 — universal file-hard | Logical files only | Hard file ceiling | Whole path | Owner every crossing | Count shared path once | File count itself | Forward change; existing chain |
| X8 — sub-file accounting | Files + LOC | Configured soft trigger | Semantic hunk/line selector | Coordinator prospective | Hunk allocation | Named harm | Forward change; new maintained selector record |
| X9 — retroactive adjudication | File count universal; LOC applicable | Soft trigger | Whole path | Reviewer/Coordinator after implementation | Reviewer reconstructs | Named harm after act | Same-key change; RF→REVIEW only |
| X10 — project-preserved hard default | Files + applicable LOC | Hard for old projects, soft for new | Whole path | Owner/Coordinator selected by project | Phase candidate | Configured threshold | Same keys, semantics inferred from install history |
| X11 — explicit-mode compatibility | Files + applicable LOC | Hard or soft | Whole path | Named authority | Phase candidate | Named harm for hard | Add `mode` key; existing chain |
| X12 — zero-tolerance overlay | Files + applicable LOC | Soft configured trigger | Whole measured path | Coordinator prospective except frozen/external boundary | Separate phase candidates | Zero-write/exact-path hard constraint plus soft size triggers | TS approval epoch; existing chain |

X3 and X12 were not proposed in the Briefing. X3 separates two useful file signals—selector membership drift and absolute configured cardinality—and makes the former mandatory even below the configured number. X12 recognizes that a phase can simultaneously have soft delivery-size triggers and a hard zero-write/exact-path authority boundary; “hard” is a property of a named constraint, not of the entire scope-budget subsystem.

## Findings

### E1 — The cross-domain measurement contract has two layers

The TFW-27/A replay separates a universally reproducible layer from delivery-specific interpretation:

```text
Layer 1 — identity/cardinality
  fixed baseline + fixed candidate
  ∩ phase-attributable selector
  ∩ VALUE paths
  = logical changed/new/modified VALUE paths

Layer 2 — applicable magnitude
  text paths      → additions, deletions, touched LOC
  binary/non-text → LOC = N/A
  domain evidence → quality/significant-characteristic checks, not a universal metric registry
```

Logical VALUE-file count is therefore useful universally for file-backed TFW work in exactly two senses:

1. it confirms which accepted artifacts the phase changed; and
2. it reveals plan-to-actual membership drift, including binary artifacts for which LOC is unavailable.

It is not a universal measure of internal magnitude, effort, review load, risk, or value. The absolute configured number remains a soft prompt to consider decomposition; the stronger universal signal is a mismatch between the planned selector and actual VALUE membership. TFW-27/A would have raised that mismatch at 7 versus 6 even though it stayed below the old absolute ceiling of 14.

This result preserves A3 and narrows A1: every applicable configured number may be a soft trigger, but file count's evidence-backed universal job is cardinality/disclosure. A hard or sufficient interpretation still needs a task-local reason.

### E2 — Four classes survive the replay, but classification and attribution are separate

The four semantic classes classify purpose; a phase selector assigns a change to an accounting subject. These are distinct operations:

```text
changed path
   |
   +-- which accepted task/phase change owns this delta?  → attribution
   |
   +-- what role does it play in that accepted result?    → VALUE / ASSURANCE / TRACE / DERIVED
```

TFW-27's combined commit proves why the distinction is necessary. Phase B's `gen_docs.py` is VALUE for Phase B, not ASSURANCE or TRACE for Phase A; it is simply outside Phase A's attributed selector. `docs/mkdocs.yml` carries both phases' VALUE in one path and one commit, so exact per-phase LOC is not recoverable. The forward contract can still use existing carriers if it requires one of these before implementation:

- separate immutable phase candidates for shared-path edits;
- assign the whole changed path to one named phase and make the other depend on that delivered change; or
- declare the metric INVALID for per-phase enforcement and use conservative whole-path counting only for disclosure.

No new class is created for “other phase.” It would confuse attribution with semantic purpose.

Mixed-role handling also needs a bounded form of A4. If a baseline→candidate diff for one path contains inseparable VALUE and excluded-role edits, the whole changed path and its candidate diff count as VALUE. Later excluded-only edits do not advance the fixed candidate. A narrower sub-file exclusion is allowed only when the TS provides a reproducible selector; freehand line subtraction is prohibited. This conservatism can overcount within the fixed candidate, but it cannot create RCFR's post-candidate self-invalidation.

### E3 — Minimal enforceable trigger-disposition chain

The chain uses only existing sections and one accounting AC. Its irreducible statements are:

#### 1. TS §4 + one TS §5 acceptance criterion — prescribe and rule prospectively

The Coordinator records:

```text
Subject:       task/phase VALUE surface
Baseline:      immutable ref before implementation
Candidate rule: immutable commit/tree containing the last VALUE change submitted
Selector:      declared phase-attributable paths/path sets with Class and AC/outcome reason
Measures:      logical changed/new/modified VALUE files; additions/deletions/touched text LOC where applicable
Triggers:      configured values and planned result
Hard constraint: none, or {harm, subject/selector, metric+threshold, pre-write action, change authority}
Ruling:        within / split / accept trigger / escalate to owner, with cause, cost, assurance implication, split alternative, decider and decision-before-work reference
```

The existing Affected Files table gains the semantic class and reason; the existing Budget line becomes the accounting block. One existing AC says that the final candidate and result must use this contract, every selector/class change must be recorded, and no newly discovered VALUE work may begin after a trigger or hard-bound crossing until the named authority records the ruling in the live TS. The AC's `Evidence:` field instructs the EV replay.

If no crossing exists, the ruling is simply `within`; no extra table or artifact is created. If implementation discovery changes membership or predicts a crossing, the Coordinator amends the live governing TS before the added work. The TS remains the sole prospective authority carrier.

#### 2. RF §1 — observe once

The Executor binds the immutable Candidate, publishes the result from the unchanged contract, lists planned-versus-actual VALUE membership/class differences, and cites the TS ruling that predates any added work. RF does not invent a selector, threshold, alternative total, or permission. Missing prospective authority is reported as a deviation; it is not repaired in prose.

#### 3. EV generic row — demonstrate

One evidence row for the accounting AC runs the exact TS method against Baseline/Candidate/Selector, records the output inline or as an attachment, checks the TS decision reference against the first added VALUE work, and uses the existing EV vocabulary:

- `VERIFIED` when refs, membership, arithmetic and prospective ruling agree;
- `BLOCKED` when a ref/selector/ruling is missing, mutable, mismatched or late;
- `N/A` only for an inapplicable metric such as binary LOC, never for the accounting AC as a whole.

`DEFERRED` is not a compliant terminal status for a hard constraint or triggered scope decision because the work has already reached evidence collection.

#### 4. review/verify.md + REVIEW §2/§4 — independently replay and adjudicate

The Reviewer reruns the exact TS method, verifies every actual VALUE path against the accepted outcome/AC, checks the decision-before-work ordering, and records any mismatch as a discrepancy. REVIEW reports the verified result in §2 and uses its existing verdict in §4:

- `APPROVE` when the same calculation and a valid prospective ruling hold;
- `REVISE` with the accounting AC/frozen-claim basis when repair stays within the approved result;
- `REJECT` to the Owner when the change introduced a new accepted deliverable, altered a frozen architecture/interface/authority/boundary, or made the contract unfit for purpose.

The Reviewer never supplies the missing ruling. REVIEW §5's debt dispositions are unrelated and need no change.

Removing any link breaks a distinct property: without TS there is no prospective authority; without RF there is no bound candidate/actual discovery record; without EV there is no execution evidence; without REVIEW there is no independent adjudication. ONB can carry the question that caused a TS amendment, but is not a fifth accounting authority.

### E4 — Coordinator authority is a decision tree, not a six-box waiver

The adversarial cases yield this prospective decision tree:

```text
newly discovered change before implementation
        |
        +-- separately usable/independently accepted output, new AC,
        |   relaxed DoF, changed phase boundary, or changed frozen target?
        |          yes → OWNER amendment / new task or phase
        |
        +-- new or changed public interface, persisted-data model,
        |   security/trust/authority boundary, or cross-phase ownership?
        |          yes → if frozen claim changes: OWNER amendment
        |                otherwise: COORDINATOR TS revision before work,
        |                with affected stakeholders/phase dependencies named
        |
        +-- necessary implementation constituent of an existing accepted result,
        |   same contract and architecture boundaries, class/selector recorded?
        |          yes → COORDINATOR may disposition soft trigger before work
        |
        +-- unresolved or already implemented?
                   unresolved → whole-path VALUE / stop for decision
                   already implemented → deviation; never retroactive approval
```

This refines A2 in two ways:

1. “unchanged outcome” is insufficient by itself; the rule must also test frozen target-state claims and public interface, persisted-data, security/trust, authority and cross-phase ownership boundaries; and
2. the ruling must be demonstrably prospective. The existing “except for recording discovery evidence” allowance permits inspection, not implementation of the discovered surface.

NIST SP 800-53 CM-3 supplies a strong external countermodel to retroactive acceptance: configuration-controlled changes are proposed, justified, reviewed and dispositioned by the appropriate authority, and enhanced control inhibits change until approval is received: <https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-53.pdf>. TFW need not import NIST machinery; the ordering principle is the relevant evidence.

### E5 — Smallest materiality rule for task-local hard constraints

A proposed hard constraint is admitted only when all six questions have concrete answers:

| # | Admission question | Required answer |
|---|---|---|
| M1 | What consequence does crossing cause? | Named damage to purpose, safety/security, compatibility, external acceptance, irreversible state, authority, or trace integrity—not “large” or “hard to review.” |
| M2 | What approved object or risk does it protect? | Frozen claim, TS AC/DoF, external rule, or explicitly accepted containment boundary. |
| M3 | Does the metric directly observe that harm's boundary? | Applicable metric and selector; no LOC for binary value, no file count for an internal page/row limit. |
| M4 | Can it be evaluated before the damaging act? | Exact pre-write check or bounded operation; otherwise it is a review criterion, not a hard stop. |
| M5 | Why is a soft trigger, split alternative, evidence or later review insufficient? | Named irreversibility, external rejection, uncontrolled blast radius, or authority breach. |
| M6 | Who may change or waive it? | Named Coordinator, Owner, or external authority, consistent with the frozen contract; Executor and Reviewer never self-authorize. |

Material examples:

- **Exact read-only corpus boundary:** zero writes to AFD, Helpdesk and historical tasks protects immutable evidence and authority. Path selector and pre-write control directly observe it; only the Owner can expand the research scope.
- **AFD incident corrective containment:** exact allowed product/test paths protect a named security/incident blast radius. The path set is material; LOC may remain a secondary soft signal unless the consequence is directly tied to it.
- **External submission file cap:** a recipient rejects a package with more than the permitted attachments. Logical VALUE-file count directly represents the external rule; the external/Owner authority controls relaxation.
- **Irreversible migration boundary:** no changes outside named schemas/data partitions before rollback evidence. This is hard because review after destructive migration is too late, though its domain metric belongs in the AC rather than a universal registry.

Counterexamples:

- configured 50 files or 5,000 LOC with only “keep work small” as rationale;
- reviewer preference or schedule discomfort that can be handled by staged review;
- a binary document/presentation LOC ceiling;
- a cap on test, evidence, RF, REVIEW, journal or research volume;
- a threshold first evaluated after implementation;
- a local hard bound copied from another task without its harm, selector and authority.

The admission test prevents “named harm” from becoming boilerplate: failure of any M1–M6 makes the number soft or inapplicable.

### E6 — Exact forward-compatibility contract

No new configuration key can preserve two simultaneous project-wide meanings. The smallest honest compatibility contract is approval-epoch based:

> **Forward applicability.** Beginning with the TFW version that introduces value-bearing scope accounting, the values under `tfw.scope_budgets` are default soft decomposition and disclosure triggers for each TS approved under that version. They are calculated only over the applicable declared VALUE surface. The change does not amend, relax, or reinterpret an already approved TS, an explicit task- or phase-local hard constraint, or any historical measurement. Existing projects retain their configured numeric values. A governing TS makes a constraint hard only by naming its protected harm, subject and selector, applicable metric and threshold, pre-write enforcement action, and authority permitted to change it.

Exact `CHANGELOG` `Changed` bullet:

> **Scope-budget defaults become forward-only VALUE triggers.** The existing `tfw.scope_budgets` keys and each project's configured numbers remain unchanged. A TS approved under this release treats them as soft decomposition/disclosure triggers over applicable VALUE measures, not automatic failure limits. Any TS approved earlier and every historical result keep the semantics they recorded. A new TS may make a bound hard only by stating the protected harm, selector, metric, pre-write action and change authority. No task history is rewritten and no replacement key is added.

Exact update-briefing rendering for “What you now do differently”:

> For a TS you approve after this update, treat your existing scope-budget numbers as prompts to disclose and decide VALUE-surface growth. Keep every already approved TS and historical result under the meaning it recorded; state any new hard bound explicitly with the harm it protects and who may change it.

This wording makes the behavioral change visible and bounded. SemVer's public-contract rule and prohibition on modifying released contents support explicit versioned communication rather than retroactive edits: <https://semver.org/>. Whether the release requires a major version is outside the Researcher role and belongs to `/tfw-release`; the research records that enforcement semantics are public behavior and must not be described as a mere wording fix.

### E7 — Hypothesis and proposal effects before Challenge

| Item | Extract effect |
|---|---|
| H1 / D1–D4 | Supported for TFW-27/A, including three binary VALUE paths with LOC = N/A. Classification needs separate phase attribution; mixed paths are conservative at the fixed candidate. |
| H2 / D8 | Supported: tests/build/evidence stay mandatory but outside value size. In TFW-27, test paths remain ASSURANCE and ignored site output remains DERIVED. |
| H3 / D9–D10 | Supported with a condition: existing carriers suffice only when phase ownership/candidate discipline makes shared-path allocation reproducible. |
| H4 / A1–A2 | A universal hard default remains refuted. A1 narrows toward dual soft signals; A2 needs architecture/interface boundaries and prospective timing. |
| H5 | Strengthened: the binary replay produces a stable value result and exposes a real missing path rather than hiding it. |
| A4 | Survives only as whole-path conservatism for the fixed measured diff; it must explicitly bar freehand sub-file exclusion and must not advance Candidate for later excluded-only edits. |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| A two-layer cross-domain metric: universal identity/cardinality plus applicable magnitude. | Challenge whether configured absolute file triggers add value beyond planned-membership drift. |
| A complete existing-carrier chain with exact responsibility and failure state at TS, RF, EV and REVIEW. | Remove each statement in turn and test for ceremonial or retroactive behavior. |
| A prospective authority decision tree that distinguishes internal constituents, durable architecture/interfaces, new outputs and already-executed work. | Run the five adversarial cases pairwise and see whether A2 should be replaced rather than extended. |
| An M1–M6 hard-bound admission test with four material examples and six counterexamples. | Attack each example for metric indirectness and authority ambiguity. |
| Exact forward applicability, CHANGELOG and update-briefing text using existing carriers and keys. | Test an in-flight old TS, a new TS in an upgraded project, and a project with customized numeric values. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?
- [x] At least one hypothesis tested? H1–H5 and A1/A2/A4 were all affected.
- [x] Counterevidence sought? Mixed commit attribution, binary file-size spread, NIST pre-approval ordering, and same-key semantic ambiguity challenge the provisional design.

**Metacognitive check:** New structure emerged: “file count” divides into planned membership drift and absolute cardinality; classification divides from phase attribution; and soft scope triggers can coexist with hard zero-write/exact-path authority constraints without making all scope budgets hard.

**Decisions recorded at Extract:** use the approval-epoch compatibility contract; place prospective trigger ruling in TS; preserve the four classes but add an explicit phase-attribution requirement; challenge A2/A4 in narrowed form rather than carry their original wording forward.

Stage complete: YES
→ User decision: Advance under the owner's fixed Iteration 2 assignment; Challenge will eliminate inconsistent configurations and proposals.
