# Challenge — "What do we NOT expect?"

> **Mindset:** Critic
> **Parent:** [3_extract.md](3_extract.md)
> **Goal:** eliminate internally inconsistent controls, stress-test the surviving configurations, and state what the evidence does not support.

## Consistency Check

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| Governed subject | Whole repository diff | Budget invariant | TRACE and ASSURANCE activity must not change delivery-budget status | A whole-diff numerator necessarily grows when later trace or assurance artifacts are added, reproducing RCFR's self-reference. |
| Candidate reference | Reviewer-time `HEAD` | Reproducibility | Fixed implementation candidate | A moving endpoint cannot reproduce the execution decision after later trace commits. |
| Metric | Universal LOC | Artifact domain | Binary, visual, configuration-only, and non-code work | LOC is undefined or misleading for material parts of the supported domain. |
| Control set | Second hard assurance ceiling | Frozen boundary | No second hard trace/assurance budget | A second ceiling recreates the dual-budget design excluded by the frozen HL and makes evidence creation compete with delivery. |
| Carrier | New scope manifest | Subtraction-first constraint | No new entity without a unique job and reader | Existing HL, TS, RF, EV, and REVIEW sections already have the necessary writers and readers. |
| Selector authority | Reviewer reconstructs the included set | Measurement contract | One selector shared from planning through review | A reviewer-defined selector permits the verdict to change the governed subject after execution. |
| Override authority | Executor expands its own grant | Human authority | An agent cannot widen its own authorization | Self-approval turns a ceiling into an unaudited estimate. |
| Enforcement point | Threshold evaluated only after implementation | Hard control | Stop-before-write behavior | A post-act number cannot function as an ex ante hard stop. |
| Classification rule | Directory-wide exclusion | Task-local value | Accepted-deliverable precedence | A generated or test directory can contain the requested product, while an ordinary source directory can contain incidental work. |
| Derived-output rule | Blanket DERIVED exclusion | Acceptance rule | Explicitly accepted generated output is VALUE | Provenance cannot override the task's accepted result. |
| Coordinator authority | May approve any growth | Frozen outcome | Authority only inside unchanged Goal, Value, accepted deliverables, AC, DoF, and phase boundaries | Growth that changes an approved outcome is an HL amendment, not implementation refinement. |
| Rename treatment | Delete plus add as two unrelated files | Logical path accounting | One renamed artifact | Double counting distorts both file and workload signals. |

### Surviving configurations

| Config | D1: governed subject | D2: control strength | D3: authority | Notes |
|---|---|---|---|---|
| C4 | VALUE only | Configured numbers are soft decomposition/disclosure triggers | Coordinator records disposition; Owner retains outcome expansion | Consistent across the three replays and across non-code artifacts, but supplies no hard protection where a task actually requires one. |
| C5 | VALUE only | Soft defaults plus a reason-bound, phase-specific hard constraint when warranted | Coordinator may accept implementation growth only inside the unchanged frozen outcome; Owner approves outcome or boundary expansion | Strongest survivor. It separates an early warning from an explicitly justified hard safety boundary without adding a carrier or key. |
| C6 | Criterion- or path-sliced VALUE | Explicit hard constraint for a named risk | Authority named in the TS; Reviewer verifies the same selector | Useful specialization of C5 for security fixes, migrations, incident containment, or an exact-path change such as AFD A1.2.2. |
| C7 | VALUE only | Nonnumeric coherence and necessity review | Coordinator and Reviewer | Consistent and works where LOC is N/A, but loses the early quantitative signal exposed by BIAI. It is a fallback, not a complete replacement. |
| C8 | Review work, not delivery value | WIP/SLE or reviewability control | Process owner/Coordinator | Useful for flow and review load, but it answers a different question and must not masquerade as the delivery budget. |
| C14-soft | VALUE files | File-count soft trigger | Coordinator records disposition | A broadly applicable weak signal; too coarse to be a universal hard gate. |

### Unexpected survivors

- **A numeric signal survives the attack on hard ceilings.** BIAI still crosses the value-only threshold, and empirical review research reports that size is associated with review change while also finding that size is not sufficient by itself. The evidence supports visibility and decomposition pressure, not a universal veto.
- **A hard bound survives only when its protected harm is explicit.** AFD's exact nine-path, 900-LOC boundary was useful because it expressed an incident-containment slice with fixed refs and accepted paths; it does not establish that every phase needs the same hard configured limits.
- **Nonnumeric controls remain necessary.** Coherence, accepted-outcome mapping, and split alternatives are the only meaningful controls for binaries, generated accepted outputs, or work whose effort is not represented by LOC.
- **Flow controls survive outside the delivery budget.** WIP limits and service-level expectations can improve review flow, but combining them with value-surface acceptance would create a second, conceptually different budget.

## Findings

### C1. Whole-diff hard ceilings are eliminated

RCFR is the falsifying case. Its VALUE surface is stable at 32 paths and 2,329 touched lines at the implementation candidate, the post-evidence candidate, and the final reviewed candidate. Whole-diff totals rise from 69 paths/5,517 touched lines to 78 paths/6,065 touched lines solely because trace artifacts continue to accrue. A whole-diff hard gate therefore measures the workflow observing itself, not implementation growth.

### C2. A universal hard ceiling is not supported

The three replays do not justify one cross-domain hard rule:

- RCFR demonstrates a false whole-diff overrun and stale-evidence review churn.
- BIAI demonstrates genuine VALUE growth: 4,649 touched lines (4,495 additions) against the 4,200 configured LOC value. Value classification narrows the signal but does not erase it.
- AFD demonstrates that an exact, phase-specific hard slice can be useful: nine accepted product/test paths and 646 touched lines against a 900-LOC constraint.

External evidence points in the same direction. A controlled experiment found that decomposing changes altered review behavior and reduced false positives, but did not improve every review outcome ([PeerJ/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7924728/)). A large empirical study found change size associated with review evolution while warning that no single factor is sufficient and project factors differ ([Empirical Software Engineering/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9489594/)). These results support small, reviewable slices and a size signal; they do not yield a domain-independent cutoff.

**Hypothesis effect:** H4 is **refuted as stated and narrowed**. Existing configured numbers should be default soft triggers. A hard constraint is valid only when the TS identifies the harm it protects, the applicable metric and selector, the pre-write enforcement point, and the escalation authority.

### C3. Removing all numeric controls is also unsupported

C7 is internally consistent, but BIAI shows why it is insufficient. Without the numeric result, the Coordinator and Reviewer would lose a concrete indication that delivery value grew beyond the planned scale. The appropriate response is not an automatic failure: it is a recorded disposition—split, accept inside the unchanged outcome, or escalate an actual outcome expansion.

### C4. The hybrid control is the strongest survivor

C5 has two layers:

1. The four existing configured values remain universal **signals** over the applicable VALUE measures. Crossing a signal requires a recorded cause, cost, and split alternative.
2. A TS may promote an applicable measure or exact path/criterion slice to a **hard bound** when the task names the protected harm. The same selector and fixed refs flow through RF, EV, and REVIEW.

No new manifest or configuration key is needed. The existing `scope_budgets` carrier can retain its values for compatibility while the conventions and existing templates state the distinction between a default trigger and an explicit task-local hard constraint.

### C5. Bounded Coordinator authority can be precise

The Coordinator may disposition a soft-trigger crossing, or revise an implementation estimate/bound, only if all of these are true:

1. the frozen Goal, Value, accepted deliverables, AC, DoF, and cross-phase boundary remain unchanged;
2. every added VALUE path is necessary for an existing accepted result and is classified with its reason;
3. the measurement is recomputed with the already approved baseline, candidate rule, selector, and metric;
4. the decision is made before work begins on the newly discovered surface, except for recording discovery evidence;
5. the Coordinator records the cause, delivery cost, assurance implication, and credible split alternative; and
6. the Reviewer verifies the same facts independently.

The Owner remains the authority for a changed outcome, new accepted deliverable, new AC, relaxed DoF, or cross-phase expansion. The Executor never approves its own wider grant.

This authority model conflicts with the current blanket convention that delegated authority cannot accept a budget overrun. It therefore requires an explicit frozen-HL amendment proposal rather than being smuggled into template wording.

### C6. The measurement contract must fail closed

The following cases produce **INVALID/BLOCKED**, not `under` or `over`:

- the baseline or implementation candidate is absent or mutable;
- RF, EV, and REVIEW use different refs or selectors;
- later VALUE changes exist outside the named candidate;
- a path cannot be classified and the ambiguity is not resolved.

Ambiguous mixed-purpose artifacts are conservatively VALUE as a whole; iteration 1 rejects line-level role classification because its complexity would exceed its decision value. Later TRACE-only or ordinary ASSURANCE-only commits do not move a valid delivery result.

### C7. Edge semantics prevent metric gaming

- Accepted generated output is VALUE; otherwise reproducible generated state is DERIVED.
- Tests are ASSURANCE unless the task explicitly accepts the test asset itself as a deliverable.
- Shared tooling is VALUE only when an accepted outcome requires its changed behavior.
- Renames count as one logical changed artifact; additions and deletions are still reported.
- Binary/non-text VALUE uses file count and the relevant domain measure; LOC is N/A, never zero.
- Deletion is reported separately and must not be credited as negative review effort.
- Unresolved classification defaults to VALUE until the Coordinator supplies an evidence-backed resolution that the Reviewer can verify.

### C8. Subtraction before addition determines the carrier design

The minimal design removes:

- whole-repository totals as the acceptance result;
- duplicate, freehand scope totals in RF and REVIEW;
- universal hard-stop semantics from the four configured defaults; and
- any proposed second trace/assurance budget.

It adds no artifact, manifest, or configuration key. The existing HL, TS, RF, EV, and REVIEW sections carry one measurement contract and one result forward.

### C9. Hypothesis disposition after challenge

| Hypothesis | Disposition | Reason |
|---|---|---|
| H1 | Confirmed with a conservative ambiguity rule | VALUE, ASSURANCE, TRACE, and DERIVED cover all replayed surfaces when accepted-deliverable precedence and unresolved-as-VALUE are explicit. |
| H2 | Confirmed conditionally | Ordinary assurance should not consume the delivery budget, but remains mandatory, in scope, and subject to relevance/proportionality review; an accepted test product is VALUE. |
| H3 | Confirmed | Existing artifacts and readers can carry the contract; a new manifest/key has no unique job. |
| H4 | Refuted as stated; narrowed | Universal hard configured ceilings are not supported. Soft defaults plus explicitly justified phase-local hard bounds are supported. |
| H5 | Partially confirmed | Stable refs and classes remove RCFR's self-reference and reproduce AFD, but BIAI remains a genuine value-growth signal rather than a false overrun. |

## Checkpoint

**Found**

- The configurations that fail because the governed subject, reference, metric, or authority is inconsistent.
- A cross-domain survivor that preserves early warning without treating one number as an automatic quality verdict.
- Exact authority conditions that distinguish implementation refinement from an Owner-level outcome amendment.
- Conservative semantics for ambiguity, accepted generated outputs, tests, shared tooling, renames, deletions, binaries, and later trace growth.
- Amendment pressure against the frozen hard-ceiling and authority claims.

**Remaining**

- Iteration 2 should validate the rubric against at least one completed non-code or binary-heavy task and test whether file-count defaults remain useful rather than ceremonial.
- Iteration 2 should test the proposed Coordinator decision rule against adversarial examples: disguised new deliverables, mixed-role files, and a late-discovered architectural dependency.
- Exact canonical wording and migration impact for redefining existing configured budgets as triggers remain design work; iteration 1 does not edit governance.

**Sufficiency**

- External source used and bounded: **yes**.
- Briefing gap addressed: **yes** — the challenge explicitly attempted to eliminate hard ceilings and also attempted to eliminate numeric controls.
- Pairwise consistency checked: **yes**.

**Stage complete:** **YES**

→ User decision: no decision is required inside the delegated iteration. Proceed to iteration-1 synthesis, preserving the amendment findings for the Coordinator/Owner rather than editing frozen governance.
