# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260904-113200_VBSA](../../HL-TFW_20260904-113200_VBSA.md)
> Goal: Turn the corpus observations into explicit configurations, a non-overlapping classification rule, and a smallest-carrier measurement contract without selecting the winner yet.

## Configuration Space

The eight Gather dimensions would produce thousands of mechanical combinations. The table keeps the distinct non-obviously-contradictory configurations that change a real decision; Challenge will eliminate inconsistent rows.

| Config | D1 — governed subject | D2 — control strength | D3 — growth authority | D4 — classification carrier | D5 — reference pair | D6 — metric model | D7 — assurance treatment | D8 — shared/generated treatment |
|--------|-----------------------|-----------------------|-----------------------|-----------------------------|---------------------|-------------------|---------------------------|----------------------------------|
| C1 — current whole-hard | Whole repository diff | Universal hard ceiling | Owner rules every crossing | Convention-only inference | Baseline → Reviewer `HEAD` | Four current metrics universally | Count assurance as delivery | Count every touched path |
| C2 — value-hard owner | Declared `VALUE` surface | Universal hard ceiling | Owner rules every crossing | TS class column | Fixed baseline → pre-RF implementation candidate | Four current metrics universally | Excluded from delivery; existing gates | Phase-attributable delta; accepted output precedence |
| C3 — value-hard delegated | Declared `VALUE` surface | Universal hard ceiling | Coordinator inside unchanged outcome | TS class column | Fixed baseline → pre-RF implementation candidate | Four current metrics universally | Excluded from delivery; existing gates | Phase-attributable delta; accepted output precedence |
| C4 — value-soft | Declared `VALUE` surface | Soft decomposition trigger | Coordinator inside unchanged outcome | TS class column + semantic rule | Fixed baseline → latest `VALUE` candidate | Delivery-appropriate metrics | Existing relevance/risk/review gates | Phase delta; accepted output precedence |
| C5 — hybrid trigger + explicit hard bound | Declared `VALUE` surface | Configured soft trigger; phase-specific hard bound only when named | Coordinator inside unchanged outcome; owner for outcome expansion | Existing TS §4 table/contract block | Fixed baseline → latest `VALUE` candidate | Delivery-appropriate metrics plus exact path boundary when useful | Existing relevance/risk/review gates | Phase delta; accepted output precedence |
| C6 — criterion-sliced | Acceptance-criterion slices | Phase-specific hard bound | Coordinator inside unchanged outcome | AC-linked TS path sets | One fixed reference pair per phase | File surface + criterion evidence | Assurance travels with its AC but has no size budget | Shared change attributed to the AC that requires it |
| C7 — value-nonnumeric | Declared `VALUE` surface | No numerical size control | Coordinator inside unchanged outcome | TS pathspec/semantic declaration | Fixed baseline → latest `VALUE` candidate | Cohesion, independence, reviewability, reversibility | Existing relevance/risk/review gates | Accepted output precedence |
| C8 — flow-control hybrid | Acceptance-criterion slices | Soft trigger | Executor adapts within TS; Reviewer judges | Explicit workflow policy | Baseline → increment candidates | WIP, age, SLE, outcome/evidence | Assurance remains in the work item | One coherent increment at a time |
| C9 — dual hard budgets | Declared `VALUE` surface + assurance workload | Universal hard ceilings for both | Owner rules every crossing | TS class column | Fixed baseline → pre-RF candidate | VALUE file/LOC + assurance file/LOC | Second assurance-size budget | Phase-attributable delta |
| C10 — manifest hard | Declared `VALUE` surface | Universal hard ceiling | Owner rules every crossing | Standalone manifest/registry | Manifest baseline/candidate | Four current metrics | Excluded from delivery; existing gates | Manifest enumerates generated/shared paths |
| C11 — review-defined soft | Declared `VALUE` surface | Soft trigger | Reviewer constructs/rules | Convention-only inference | Baseline → Reviewer `HEAD` | Reviewer-selected applicable metric | Reviewer excludes assurance | Reviewer interprets shared/generated paths |
| C12 — executor self-managed | Declared `VALUE` surface | Phase-specific hard bound | Executor adapts within TS | TS pathspec | Fixed baseline → Executor candidate | Delivery-appropriate metrics | Existing gates | Phase-attributable delta |
| C13 — mechanical split | Declared `VALUE` surface | Universal hard ceiling | No override; split mechanically | TS class column | Fixed baseline → pre-RF candidate | Four current metrics | Existing gates | Phase-attributable delta |
| C14 — file-only hard | Declared `VALUE` surface | Universal hard ceiling | Owner or Coordinator by outcome boundary | TS class column | Fixed baseline → pre-RF candidate | Logical file count only | Existing gates | Rename = one logical file; binary accepted outputs count |

C5 is the configuration not present in the Briefing: configured numbers cease to be universal vetoes but survive as default signals; a Coordinator can promote a risk-specific phase bound to a hard stop with an explicit reason. It combines the useful BIAI visibility behavior with AFD's exact incident boundary without preserving RCFR's self-taxing whole-tree ceiling.

## Findings

### E1 — A precedence decision tree makes the four classes non-overlapping

Classify the changed artifact's role in this approved delivery, in this order:

1. **Explicitly accepted output?** `VALUE`, regardless of type, path, extension, or how it was produced. This catches test products, final PDFs, generated sites, prompts, datasets, and adapter copies when those are promised results.
2. **Necessary constituent of the accepted result?** `VALUE`. “Internal,” “infrastructure,” or “supporting” does not demote production code, a required lockfile, a schema, or an installed runtime copy.
3. **Task-local TFW state, lifecycle, research, handoff, evidence, result, or review record?** `TRACE`. A real deliverable stored in the task folder already exited at step 1, so location cannot suppress value.
4. **Created only to test, verify, inspect, or demonstrate another accepted result?** `ASSURANCE`. If the suite itself is accepted, step 1 made it `VALUE`.
5. **Mechanically reproducible and not independently accepted?** `DERIVED`. If the rendered/generated output is accepted, step 1 made it `VALUE`.
6. **Still ambiguous?** Treat it as `VALUE` until the Coordinator records a narrower class with an acceptance-criterion rationale. Ambiguity must not become a hiding channel.

The class is attached to the approved purpose, not permanently to a filename. The same PDF can be `DERIVED` as a visual-QA rendering in one phase and `VALUE` as the recipient's requested publication in another.

### E2 — Cross-domain classification matrix

| Changed surface | Default | Override/edge | Budget treatment |
|---|---|---|---|
| Product code, workflow, prompt, document source, presentation source, dataset | `VALUE` when required for the accepted result | A temporary analysis input may be `ASSURANCE` | Logical files and applicable text metric |
| Durable internal production infrastructure, schema, lockfile, active adapter | `VALUE` | None merely because it is internal or generated | Counts as accepted-result support |
| Ordinary unit/integration/e2e tests and fixtures | `ASSURANCE` | `VALUE` when the approved delivery is the evaluator, suite, harness, or conformance product | No delivery-size charge; all quality gates remain |
| HL, TS, ONB, RF, REVIEW, RES, status, journal, stage files, EV, raw evidence/logs | `TRACE` | A domain deliverable that merely resembles or lives beside a TFW artifact is `VALUE` by precedence | Never spends delivery budget |
| Final PDF/PPTX/image/site/build accepted by recipient | `VALUE` | None because generation is mechanical | File count; LOC explicitly N/A where not meaningful |
| Disposable render, cache, compiled object, generated preview | `DERIVED` | `VALUE` if independently accepted | Excluded by default |
| Generated active adapter copy required as shipped behavior | `VALUE` | A transient install/check copy is `DERIVED` | Accepted-output precedence |
| Rename of a `VALUE` artifact | `VALUE` | Content change may also have text LOC | One logical changed file, not automatic create + delete |
| Deletion from the accepted surface | `VALUE` | Whole-file deletion may reduce complexity rather than increase review cost | One logical changed file; deleted lines reported, not confused with output size |
| Binary deliverable | `VALUE` | Raw evidence binary remains `TRACE` | File count applies; LOC = N/A, never zero |
| Shared file changed by this phase | Class follows purpose | Unchanged inherited content is not re-counted | Only fixed baseline→candidate delta attributable to the phase |

The matrix removes the proposed fifth “durable supporting implementation” class: its members are `VALUE` by step 2. More classes would add labels without creating a new decision.

### E3 — The reproducible calculation needs five named parts, not a new artifact

An enforceable measurement instance is:

```text
Subject    = declared VALUE paths/path sets justified by accepted outcomes and ACs
Baseline   = immutable Git commit/tree before phase implementation
Candidate  = immutable Git commit/tree containing the last VALUE change being submitted
Metrics    = logical VALUE files changed/new/modified + touched text LOC where applicable
Method     = the exact Git commands and selector recorded in TS, replayed in RF/EV/REVIEW
```

Metric rules derived from Git's record model:

- use NUL-safe `git diff --name-status -M -z <baseline> <candidate> -- <selector>` for status and rename handling;
- count `A` as new, `M`/`T` as modified, `D` as deleted, and `R` as one logical changed file rather than a new-plus-delete pair;
- define touched text LOC as additions + deletions from NUL-safe `--numstat`; a binary `-`/`-` record is `N/A` for LOC and still participates in file counts;
- do not count unchanged reused shared files; count only their phase-attributable diff;
- a later `TRACE`, `ASSURANCE`, or excluded `DERIVED` commit does not replace Candidate;
- any later `VALUE` edit creates a new Candidate and the same method is rerun.

NASA's [SWE-093 measurement guidance](https://swehb.nasa.gov/spaces/SWEHBVB/pages/32604581/SWE-093%2B-%2BAnalysis%2Bof%2BMeasurement%2BData) calls LOC one of the most used and misused software metrics, notes the absence of one industry-accepted counting standard, and requires the exact measurement method to accompany analysis. NASA's [software-size guide](https://standards.nasa.gov/sites/default/files/standards/NASA/Baseline/0/nasa-gb-871913.pdf) also notes that LOC varies by language and is unavailable reliably before code exists. These sources independently support method/reference disclosure and reject cross-domain universal LOC comparisons.

The [SPACE framework paper](https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/) establishes that a complex construct cannot be reduced to one activity metric or dimension. Scope size is not developer productivity, so this is an inference rather than direct proof; it still warns against asking LOC to stand simultaneously for delivered value, implementation effort, review load, and risk.

### E4 — Existing carriers have one reader chain

No standalone budget manifest or new configuration key is required.

| Existing carrier | Smallest added responsibility | Reader |
|---|---|---|
| `conventions.md` §6 | Own the semantic classes, precedence, metric definitions, default control semantics, and authority boundary | Coordinator, Executor, Reviewer through their workflow reads |
| `TS.md` §4 | Add `Class` to Affected Files; name baseline, selector/path sets, applicable metrics, exact reproduction method, estimate/trigger, and any explicit hard bound with reason | Executor and Reviewer |
| `RF.md` §1 | Name fixed Candidate, record classification deviations/new discovered paths, publish the one resulting `VALUE` calculation | Reviewer |
| `EV.md` generic row | Re-run the TS method and attach output/status; no dedicated shadow table required | Reviewer |
| `review/verify.md` | Re-run the same TS contract against the RF Candidate; forbid a new selector, reference pair, or metric | REVIEW synthesis |
| Existing adapter manifest/tests | Propagate and compare changed workflow/template copies | Update/config/review gates |

This uses one semantic authority and four lifecycle observations. A manifest would duplicate path membership already required in TS and become stale on implementation discovery; a configuration key would parameterize a new choice where the existing four keys already hold the numerical signal.

### E5 — Control mechanisms protect different harms

| Mechanism | Unique harm it can protect | Observable strength | Structural weakness |
|---|---|---|---|
| Universal hard numeric ceiling | Unbounded phase growth before review | Deterministic stop | Cross-domain metric mismatch; routine owner waivers; false precision; wrong subject can self-invalidate |
| Soft configured trigger | Silent growth and unexamined decomposition | Requires estimate/result and a recorded decision | Can become ignorable if no reader must state a ruling |
| Phase-specific hard bound | Named blast radius, incident boundary, or reviewer capacity | Exact stop tied to this TS | Planning cost and local false precision; must remain changeable when facts invalidate it |
| Nonnumeric structural control | Loss of cohesion, independence, reversibility, or acceptance traceability | Directly tests task shape | Less mechanically comparable; depends on cited judgment |
| WIP/time/SLE control | Too much concurrent or aging work | Flow-based and empirically recalibrated | Does not by itself bound one delivered surface |
| No size control | Ceremony and misleading arithmetic | Maximum subtraction | Loses an early prompt to decompose and disclose growth |

Bounded Coordinator authority is orthogonal. It can pair with a soft trigger or a phase-specific hard bound: the Coordinator may adjust implementation details only while Goal, Value, phase outcome, accepted deliverables, DoD, DoF, and cross-phase boundary remain unchanged. Any expansion of those objects goes to the owner through the existing amendment channel. The authority needs an explicit test because “inside the outcome” cannot be self-declared by the role benefiting from growth.

### E6 — Excluding assurance from delivery size does not exclude it from the change or review

Google's [Small CLs guidance](https://google.github.io/eng-practices/review/developer/small-cls.html) says a small change is conceptually self-contained rather than a simplistic line-count function and also requires related tests. That combination matters: tests stay in the reviewed change even when they should not make the delivered product appear larger.

TFW already has independent controls for assurance:

- each TS acceptance criterion prescribes Evidence;
- Executor runs build/test gates and collects EV evidence;
- Reviewer audits claim/source agreement, evidence completeness and sufficiency, safety, and compatibility;
- Project North Star NS2.6 requires assurance proportional to risk.

An unlimited low-value test pile can therefore be rejected as irrelevant, disproportionate, or review-obscuring without inventing an assurance LOC ceiling. This supports H2 only if every template/workflow states explicitly that “not budget-bearing” is not “out of scope” or “optional.”

### E7 — Preliminary hypothesis effects

| Hypothesis | What Extract reveals before Challenge |
|---|---|
| H1 | Four classes are sufficient only with explicit accepted-output/necessary-constituent precedence and conservative `VALUE` on unresolved ambiguity. |
| H2 | Existing independent assurance gates can carry quality; exclusion must not remove tests from the reviewed change or evidence plan. |
| H3 | Existing carriers form a complete reader chain. A new artifact/key has no unique job yet. |
| H4 | The strongest evidence supports a hybrid, not the hypothesis's universal-hard premise: soft configured triggers plus optional reason-bound phase hard stops and bounded Coordinator authority. |
| H5 | RCFR stabilizes; AFD remains bounded; BIAI remains a smaller genuine overrun. “Removes the observed overrun” is too broad. |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| A six-step precedence rule makes the four classes exhaustive for observed cases and defaults ambiguity to `VALUE`. | Attempt adversarial reclassification and path-selector gaming. |
| C5 combines soft default signals with explicit reason-bound hard stops; it was not present in the Briefing. | Pairwise consistency check against the frozen HL, current authority rules, and corpus outcomes. |
| Five measurement parts fit existing carriers; no new manifest/key has a unique reader. | Test failure/recovery when baseline, candidate, selector, or metric is missing or changes. |
| LOC can be reproducible for text but is not universal; binary LOC must be N/A and delivery-specific metrics cannot become a metric registry. | Decide whether file count alone is an adequate universal signal or only another soft trigger. |
| Bounded Coordinator authority can be stated as an unchanged-outcome test rather than a numeric allowance. | Define the exact stop/escalation boundary without creating self-authorizing delegation. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: Advance under the owner's initial instruction; Challenge must try to break C5 rather than treating its emergence as a recommendation.
