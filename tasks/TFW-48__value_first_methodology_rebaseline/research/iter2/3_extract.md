# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-48](../../HL-TFW-48__value_first_methodology_rebaseline.md)
> Briefing: [Iteration 2 Briefing](1_briefing.md)
> Gather: [Iteration 2 Gather](2_gather.md)
> Predecessor: [Iteration 1 RES](../iter1/RES.md)
> Goal: Re-derive TFW from its product purpose and production learning so that a
> proportionate method kernel preserves meaning, evidence, independent judgment, and
> portable knowledge across routine and high-risk work in multiple domains.
> Mode: Pipeline — Deep

## Scope and Authorization

This Extract analyzes the approved six-software/four-non-code sample as evidence about
mechanisms and configurations. It does not estimate prevalence and does not support a
model-era causal claim. The excluded failure, security, migration, incident, and
no-review cases remain available for Challenge.

No H4 output, comparison cell, fresh context, fork, task, or model was created,
dispatched, or executed. The 40-, 112-, and 220-output designs remain unapproved.

## Configuration Space

### Why the space is conditional

The 12 Gather dimensions have four alternatives each, so a blind Cartesian expansion
would contain `4^12 = 16,777,216` rows. Most would be meaningless because:

- D1–D5 describe a **rule or numeric control**, not the whole workflow;
- D6–D7 describe a **learning policy or transaction**;
- D8 describes an independent **project extension record**, which can exist without
  any learning event;
- D9–D10 describe each **value-proof obligation and its packaging**, and multiple
  proof obligations can coexist for one deliverable;
- D11 describes an **H4 evidence claim**; and
- D12 lists **additive cost surfaces**, not mutually exclusive alternatives.

The full usable space is therefore a configuration grammar:

```text
Method configuration M =
  one or more Rule records R(D1, D2, D3, D4?, D5?)
  + Learning policy/transactions L(D6, D7)
  + zero or more Extension records
      E(D8, owner, source-version, precedence, consumers,
        freshness, unsupported/migration behavior)
  + one or more Value-proof records V(D9, D10)
  + optional H4 evidence package T(D11, set(D12))
```

`?` means numeric dimensions apply only when the rule contains an operative number.
An `E` record exists independently of a learning transaction. A `V` record attaches
to one claim obligation, so a method can require local proof for every claimed
deliverable and add seam, stakeholder/live, or value-debt records when those claims
are triggered. This keeps every Gather dimension visible without pretending that,
for example, "researcher time" and "scoring time" are competing resource choices.

### Alternative codes

| Dimension | A | B | C | D |
|-----------|---|---|---|---|
| D1 — Rule consequence | Reversible explanation/reference | Observable lifecycle/navigation error | False evidence/value judgment | Pre-action role, safety, destructive, or irreversible breach |
| D2 — Rule locality | Canonical reference only | Canonical owner + short local cue | Canonical owner + local observable gate | Full local imperative + hard gate |
| D3 — Task exposure | Routine and local | Reversible cross-seam | External-source/stakeholder-facing | High-risk/irreversible |
| D4 — Numeric semantics | Boundary | Escalation trigger | Attention warning/sampling default | Target/descriptive measurement |
| D5 — Numeric owner | Framework invariant | Workflow default | Project calibration | Task-specific override |
| D6 — Learning entry | Every completed artifact | Event-triggered durable/contradictory signal | Coordinator-selected batch | Remain task-local/reject |
| D7 — Learning receipt | None | One-line disposition and reason | Source↔destination backlink | Central lifecycle registry |
| D8 — Project extension form | Inline root instruction | Project config block | Registered/versioned extension | Direct upstream-core fork |
| D9 — Value proof | Local artifact verification | Interface/seam proof | Stakeholder/end-to-end validation | Explicit value debt with due validation |
| D10 — Review packaging | One compact review | Staged logs + synthesis | Risk-triggered expansion | Grouped cross-phase value/seam review |
| D11 — H4 evidence scope | Protocol feasibility only | Small protocol rehearsal | Variance calibration pilot | Inferential matched-strategy trial |
| D12 — H4 resource surface | Codex credits | API-token equivalent | Human scoring/reconciliation | Researcher case construction/analysis |

### Rule/numeric configurations

These rows enumerate coherent rule shapes. They are not ranked here.

| Config | D1 — Rule consequence | D2 — Rule locality | D3 — Task exposure | D4 — Numeric semantics | D5 — Numeric owner |
|--------|-----------------------|--------------------|--------------------|------------------------|--------------------|
| R1 | A | A | A | — | — |
| R2 | A | B | B | D | B |
| R3 | B | B | A | C | B |
| R4 | B | C | B | B | C |
| R5 | B | C | C | A | B |
| R6 | C | B | A | C | C |
| R7 | C | C | B | B | C |
| R8 | C | C | C | A | B |
| R9 | D | D | A | — | A |
| R10 | D | D | B | B | A |
| R11 | D | D | C | A | A |
| R12 | D | D | D | A | A |
| R13 | B | C | A | C | D |
| R14 | C | C | C | D | D |

R9 is deliberately non-obvious: a pre-action authority boundary can require a full
local hard gate even when the surrounding task is routine. Risk is a property of the
rule consequence as well as the task.

### Learning configurations

| Config | D6 — Learning entry | D7 — Learning receipt |
|--------|---------------------|-----------------------|
| L1 | D | B |
| L2 | B | B |
| L3 | B | C |
| L4 | B | D |
| L5 | C | C |
| L6 | A | D |

The combinations expose a distinction hidden by "capture all learning": the entry
predicate can remain selective while receipt strength rises from a one-line reason to
a backlink or lifecycle registry.

### Extension configurations

Each row is one independently existing `E` record; a method can have zero or more.

| Config | D8 — Project extension form | Required lifecycle fields |
|--------|-----------------------------|---------------------------|
| E1 | A | Owner, source/version, precedence, consumers, freshness, unsupported/migration behavior |
| E2 | B | Same six fields |
| E3 | C | Same six fields |
| E4 | D | Same six fields plus explicit fork/upstream reconciliation policy |

### Value-proof configurations

| Config | D9 — Value proof | D10 — Review packaging |
|--------|------------------|-------------------------|
| V1 | A | A |
| V2 | A | C |
| V3 | B | A |
| V4 | B | B |
| V5 | B | C |
| V6 | B | D |
| V7 | C | B |
| V8 | C | D |
| V9 | D | A |
| V10 | D | D |

These combinations make proof depth and artifact count independent. Seam proof can be
compact (V3), while local proof can expand when discrepancy or risk appears (V2).
Every claimed deliverable has at least one local-proof record (V1 or V2). Seam and
stakeholder/live records are added when the claim crosses those boundaries; V9/V10
record an explicit owner and due event when triggered proof is honestly deferred.

### H4 evidence configurations

D12 is represented as a set because every executed design would incur more than one
surface.

| Config | D11 — H4 evidence scope | D12 — H4 resource surface | Claim carried by the configuration |
|--------|--------------------------|----------------------------|------------------------------------|
| T0 | A | D only | Desk protocol and owner package; no run |
| T1 | B | A+C+D | Small operability/scoring/cost rehearsal |
| T2 | B | A+B+C+D | Same rehearsal with API-equivalent sensitivity |
| T3 | C | A+C+D | Variance/runtime calibration pilot |
| T4 | C | A+B+C+D | Calibration plus currency sensitivity |
| T5 | D | A+C+D | Inferential matched-strategy trial |
| T6 | D | A+B+C+D | Inferential trial plus currency sensitivity |

T0 is the only currently authorized configuration. T1/T2 correspond to the 40-output
proposal, T3/T4 to the 112-output proposal, and T5/T6 to the illustrative 220-output
design only if its power and multiplicity requirements are first satisfied.

### Cross-subsystem combinations not visible in the Briefing

The following complete configurations use the grammar rather than treating TFW as one
global weight setting. They are not yet survivors.

| Config | Rule set | Learning | Extensions | Value-proof records | H4 |
|--------|----------|----------|------------|---------------------|-----|
| M1 | R1 + R3 + R9 | L2 | none | V1 | T0 |
| M2 | R1 + R4 + R9 | L3 | none | V1 + V3 | T0 |
| M3 | R3 + R7 + R9 | L3 | E3 | V1 + V5 | T0 |
| M4 | R4 + R8 + R11 | L4 | E3 | V1 + V8 | T0 |
| M5 | R3 + R9 + R13 | L3 | E3 | V1 + V6; add V7/V8 or V9/V10 when stakeholder/live proof is triggered or deferred | T0 |
| M6 | R5 + R10 + R12 | L4 | E3 | V2 + V7 | T0 |
| M7 | R3 + R7 + R9 | L3 | E3 | V1 + V5 | T2 |
| M8 | R3 + R7 + R9 | L3 | E3 | V1 + V5 | T4 |
| M9 | R3 + R7 + R9 | L3 | E3 | V1 + V5 | T6 |

M5 is the most important newly visible combination: a routine method can use compact,
local artifact proof plus grouped seam proof, event-triggered learning, and an
independently registered extension while retaining a full local role/safety gate.
Stakeholder/live proof is added when the claim triggers it, or represented as explicit
value debt when deferred. "Routine" therefore does not imply that every rule becomes
referential or every control becomes weak. Task exposure may strengthen but never
weaken R9-style pre-action authority boundaries.

## Findings

### E1. The unit of proportionality is the obligation, not the task

The routine cases do not support one workflow-wide light/heavy switch. They support
selecting locality and review packaging separately for each protected failure:

```text
if breach must be prevented before action or is irreversible:
    full local imperative + observable hard gate
elif breach is observable at a lifecycle transition:
    canonical owner + point-of-use observable gate
elif the rule is explanatory and failure is reversible:
    canonical owner/reference + short cue where discovery is uncertain
```

Task exposure can strengthen the selection, but cannot weaken a pre-action authority
boundary. This explains why a routine documentation change can use one compact review
while its role lock remains explicit and local.

**H1 test:** H1 remains conditionally supported. The cases support owned rules plus
local observable gates, not indiscriminate repetition. Counter-evidence is the role
lock: it remains a full local imperative even in routine work. Another counter-case is
HD-7/HD-8, where routine successful work still used staged review traces. Therefore
neither "always compact" nor "always staged" survives.

### E2. Numeric governance is a lifecycle, not a threshold table

An operative number is governable only after six semantic fields are present:

1. type;
2. semantic owner;
3. consumer/enforcement observation;
4. counting rule;
5. breach response; and
6. override authority.

Only then is calibration meaningful. The extracted state machine is:

```text
inventory
  → type
  → trace owner and intended protected failure
  → observe consumer/enforcement
  → classify lifecycle state
  → restore consumer/ownership or retire normativity
  → calibrate only against an explicit loss/benefit function
  → monitor breach and override outcomes
```

#### Restore-owner-or-retire classification

The classification is evidence-based but remains subject to owner confirmation:

| Number/rule | Current evidence class | Reason | Required next fact before calibration |
|-------------|------------------------|--------|---------------------------------------|
| `research.max_passes: 3` | (1) obsolete/dead **or** (2) intended with missing consumer | OODA consumes mode `loops_per_stage`, not this key | Owner must choose whether the key is an alias, independent ceiling, or residue |
| `research.min_iterations: 2` | (3) active consumer with missing registry documentation | Plan/iteration control consumes it; Config Sync Registry omits it | Register owner and every inline derivative |
| `knowledge.max_index_lines: 200` | (2) intended with missing consumer/breach path | Config describes a target; current workflow does not enforce it; mature projects exceed it | Define count, response, override, and navigation outcome—or retire it |
| `knowledge.max_index_facts_lines: 30` | (1) obsolete/dead | Originating index topology/section no longer exists | Confirm retirement and remove derivative references |
| `knowledge.max_facts_per_topic: 50` | (2) intended with incomplete breach path | Workflow checks it but defines no response; AFD is at 54 | Define whether breach means split, warn, explain, or override |
| `knowledge.max_topic_files: 8` | (2) intended with incomplete breach path | Workflow checks it but a ninth topic may be more coherent than forced grouping | Define taxonomy-quality response and override |
| Workflow instruction `≤1200` words | (2) intended with missing breach path **or** (4) descriptive residue | Current HL records canonical workflows above it; word-count method and consequence are absent | Owner must choose an attention target or normative boundary |
| Adapter content `≤35` lines | (1) obsolete/dead **or** (4) descriptive residue | Architecture moved from one thin file to skill directories | Confirm the current unit of maintainability before replacing or retiring it |

No exact replacement is recommended. In particular, exceeding 200 lines, 50 facts, or
8 topics is evidence of non-enforcement and possible construct drift—not proof that a
higher number is optimal.

**H2 test:** H2's mechanism is strongly supported: numeric controls need purpose,
ownership, response, and override semantics. Its stronger form—"current numbers merely
simulate certainty"—is too broad. `min_iterations` and the evidence-existence floor
protect real structural failures even though their exact counts are not universally
calibrated. Challenge must distinguish structural coverage boundaries from tunable
performance thresholds.

### E3. The smallest useful learning receipt is relational

The candidate minimum is:

```text
source signal
  → disposition (promote / defer / reject / task-local)
  → destination or reason
  → responsible actor or due event
```

This fits in one line when no destination artifact is created. A backlink becomes
necessary when promotion or deferral creates a durable destination/due event. A
central registry is justified only when lifecycle queries cannot be answered reliably
from source and destination records.

The same relational idea resolves project-extension drift. A registered extension
needs at least:

| Field | Protected failure |
|-------|-------------------|
| Identifier and semantic owner | Project policy becomes anonymous framework behavior |
| Source location and version/range | Consumers load the wrong extension generation |
| Precedence rule | Root, config, adapter, and canonical rules silently conflict |
| Consumer list | A local policy exists but no workflow applies it |
| Source hash/last-sync evidence | A copied derivative silently becomes stale |
| Unsupported/migration behavior | Upgrade skips or corrupts project policy |

This is stronger than "put overrides in config" but narrower than forking upstream
core.

**H3 test:** H3 remains supported with a minimum receipt predicate. Counter-evidence is
the cost of per-item ceremony: AFD-51 and AFD-32 show that a short reason can be enough,
while HD-24 shows that a batch marker without destination or due event is not enough.

### E4. Value proof and review packaging are orthogonal

The cases yield three claim obligations:

| Claim obligation | Trigger | Proof | Packaging choices |
|------------------|---------|-------|-------------------|
| Local artifact | Every claimed deliverable | Inspect/build/source-check the delivered surface | Compact or risk-expanded |
| Interface/seam | Claim crosses component, source, role, package, or phase boundary | Verify both sides and the relation | Compact, staged, or grouped cross-phase |
| Stakeholder/live value | Claim depends on environment, user, owner, or irreversible external result | Validate at earliest honest event | Current review or explicit value debt |

Grouping a seam/value review is permissible only if the due event, owner, evidence
route, and non-claim before validation remain visible. This permits V3/V6/V9 without
equating fewer files with weaker judgment.

K3 can therefore retain its semantic obligations—purpose, authority, evidence,
independent judgment, and learning disposition—without imposing a uniform artifact
package. AFD-32 remains the cost warning; AFD-51 remains the compact counterexample.

### E5. H4 requires three owner decisions, not one pilot label

The owner packages separate claim, outputs, resources, and prerequisites:

| Package | Output formula | Valid claim | Model/credit estimate before 10% rerun reserve | Human estimate | Missing prerequisite |
|---------|----------------|-------------|-----------------------------------------------|----------------|----------------------|
| 40-output rehearsal | `4 cases × 2 profiles × 4 focal conditions + 8 repeats = 40` | Operability, scoring agreement, runtime/token/case-construction estimates only | 60.8–247.5 Codex credits depending on length/cache; API-reference USD 1.62–6.60 | 33.6–64.0 h | Owner authorization and progression criteria |
| 112-output pilot | `12 cases × 2 profiles × 4 focal conditions + 16 repeats = 112` | Variance/reliability calibration and feasibility; not confirmatory H4 without a justified analysis/power plan | 170.1–693.0 credits; API-reference USD 4.54–18.48 | 82.9–156.8 h | Power/precision target, variance basis, multiplicity plan, authorization |
| 220-output illustration | `168 primary + 28 pilot + 24 repeats = 220` | Candidate full matched-strategy trial only if prospective inference requirements are met | 334.1–1,361.3 credits; API-reference USD 8.91–36.30 | 114.8–212.0 h | Final estimand, power simulation, independence, stopping/missingness rules, authorization |

All cost assumptions are dated 2026-07-29 and remain the Gather ranges: 15k–30k input
tokens, 2k–6k output tokens, 0%/50%/80% cache sensitivity, 10% protocol-failure rerun
reserve, two masked scorers at 6–10 minutes/output plus 20% reconciliation, and explicit
researcher construction/analysis time.

The external [CONSORT extension for pilot and feasibility
trials](https://doi.org/10.1136/bmj.i5239) independently distinguishes a feasibility
study from a definitive effectiveness test: pilot objectives should determine sample
size and progression criteria, while formal effectiveness hypothesis testing is not
recommended for an underpowered pilot. The analogy does not turn H4 into a clinical
trial; it supports the claim-discipline rule. Accordingly:

- 40 outputs cannot confirm or refute H4;
- 112 outputs cannot be called confirmatory merely because it is larger; and
- 220 outputs cannot be called sufficient until prospective power and multiplicity
  checks justify the intended estimand and inference standard.

**H4 test:** H4 remains unresolved. The configuration space shows a feasible path from
desk protocol (T0) through rehearsal/calibration to an inferential trial, but no result
exists and authorization prohibits producing one. Counter-evidence to "40 is enough
because every cell type appears" is the lack of case-level interval/power support.

### E6. Extract decisions

| ID | Decision | Reason | Challenge implication |
|----|----------|--------|-----------------------|
| X-D1 | Use a conditional configuration grammar with independent learning transactions, zero-or-more extension records, and one-or-more per-claim value-proof records | Dimensions apply to different objects and D12 is additive | Challenge subsystem combinations and cross-subsystem conflicts |
| X-D2 | Make obligation consequence/observability the primary locality selector; task exposure only strengthens it | Routine cases retain hard role gates while varying review packaging | Try to falsify R9/M5 with incident and security counter-cases |
| X-D3 | Route ownerless/unconsumed numbers through restore-owner-or-retire before exact calibration | A number without semantics or a consumer has no observable calibration target | Challenge every provisional lifecycle class and structural-floor exception |
| X-D4 | Separate local proof, seam proof, and due stakeholder validation from review artifact count | Successful compact and staged cases protect different seams | Test whether grouping can hide unresolved value debt |
| X-D5 | Preserve H4 as T0 only until separate owner authorization | Feasibility costing is not effect evidence | Challenge claim boundaries and prerequisite completeness, not model outputs |

## Metacognitive Check

**Did this Extract discover something new, or only confirm Iteration 1?**

It discovered four material refinements:

1. proportionality attaches to individual obligations, not to a whole task;
2. D12 is an additive cost set, so the original 12-axis Cartesian model was malformed;
3. a routine compact workflow can coexist with full local authority/safety gates,
   event-triggered learning, an independently registered extension, mandatory local
   proof, and triggered grouped seam proof (M5); and
4. numeric governance needs a lifecycle classification before calibration, with
   `min_iterations` showing that an orphaned registry entry is not necessarily an
   unconsumed policy.

It also confirmed Iteration 1's learning-receipt and value/seam mechanisms. To avoid
confirmation bias, Challenge must use the preserved failure/security/migration/
incident cases against M5, the provisional numeric classes, and grouped value review.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| A conditional grammar covers all 12 dimensions without a false 16.8-million-row Cartesian table. | Challenge must eliminate inconsistent subsystem and cross-subsystem combinations. |
| M5 decouples routine review packaging, learning, extensions, and per-claim proof while preserving non-negotiable local authority gates. | Test it against failure, incident, security, and migration counter-cases. |
| Eight orphaned/hard-looking values have provisional restore-owner-or-retire classes; no exact value is recommended. | Challenge classifications, structural exceptions, and retirement consequences. |
| Learning receipt and registered-extension minimum fields are explicit. | Test whether this is sufficient without a central registry. |
| Local, seam, and stakeholder/value proof are independent of review file count. | Test grouped review against hidden debt and ownership failure. |
| H4 has T0/T1–T6 claim/resource configurations; only T0 is authorized. | Challenge feasibility assumptions and owner prerequisites without running anything. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?
- [x] At least one HL hypothesis tested?
- [x] Counter-evidence sought?
- [x] Metacognitive check completed?
- [x] Deep exit: at least two Extract decisions?
- [x] Deep exit: at least one hypothesis tested?

**Recommendation:** Close Extract and proceed to Challenge. The configuration space
contains a new non-binary combination (M5), carries all approved numeric and H4
boundaries, and leaves evaluation/elimination to the next stage.

**Questions for Coordinator:**

1. Approve the corrected conditional configuration grammar and M5 as a configuration
   to challenge, rather than treating TFW as one global light/heavy setting.
2. Approve carrying the provisional restore-owner-or-retire classifications into
   Challenge without recommending any exact replacement value.
3. Approve the T0/T1–T6 H4 claim boundaries, with only desk protocol T0 authorized and
   no run/fork/dispatch permission implied.

Stage complete: YES
→ User decision: REVISE A; APPROVE B-C. Coordinator approved the conditional-grammar
  direction after separating learning `L(D6,D7)`, zero-or-more independently governed
  extension records `E(D8, lifecycle fields)`, and one-or-more per-claim value-proof
  records `V(D9,D10)`. M5 now contains mandatory compact local proof plus triggered
  grouped seam proof, event-triggered learning, an independent registered extension,
  and the full local role/safety gate; stakeholder/live proof is added when triggered
  or carried as explicit value debt when deferred. Restore-owner-or-retire classes
  remain provisional falsification objects with no exact replacement values. Only T0
  is authorized; T1-T6 remain claim/cost options with no run, fork, dispatch, fresh
  context, or comparison-model authorization. Extract closes and Challenge may begin
  without another Coordinator WAIT.
