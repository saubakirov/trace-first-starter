# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260904-113200_VBSA](../../HL-TFW_20260904-113200_VBSA.md)
> Goal: Reconstruct what the existing numbers actually measure, then keep open every viable control and authority model until the evidence can eliminate them.

## Dimensions

Each dimension is independent: choosing a value in one row does not settle the others.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1 — governed subject | Whole repository diff | Declared `VALUE` surface | Acceptance-criterion slices | Review/assurance workload surface |
| D2 — control strength | Universal hard ceiling | Soft decomposition trigger | Phase-specific hard bound | No numerical size control |
| D3 — growth authority | Owner rules every threshold crossing | Coordinator may rule inside unchanged frozen outcome | Executor adapts within TS and Reviewer judges | No override; split mechanically |
| D4 — classification carrier | Class column in existing TS Affected Files | TS pathspec/selector plus semantic rule | Convention-only inference at review time | Standalone manifest/registry |
| D5 — reference pair | Mutable working tree | Fixed baseline and pre-RF implementation candidate | Baseline and latest `VALUE` commit named in RF | Baseline and Reviewer `HEAD` |
| D6 — metric model | Four current metrics for every delivery | Delivery-appropriate metric chosen in TS | File/path surface only | Nonnumeric cohesion, risk, and reviewability tests |
| D7 — assurance treatment | Count ordinary assurance as delivery | Exclude from delivery budget but keep all assurance gates | Maintain a second assurance-size budget | Control assurance by evidence relevance, risk, and review sufficiency |
| D8 — shared/generated treatment | Count every touched path | Count only the phase-attributable delta | Count one logical unit per accepted output | Classify by whether the output itself is accepted value |

## Findings

### G1 — The current framework has numbers but no common accounting contract

The active carriers answer different questions:

- `.tfw/conventions.md` §6 supplies four default ceilings and rationales, but defines no included set, baseline, candidate, rename rule, binary treatment, or reproduction method.
- `.tfw/workflows/plan.md` Step 7 asks the Coordinator to count files, new files, and estimated LOC. It does not say whether tests, evidence, task traces, generated outputs, or later corrections belong to the estimate.
- `.tfw/templates/TS.md` §4 has `File`, `Action`, and `Description`, followed by one aggregate Budget line. It can already host classification and the planned calculation, but does not yet do so.
- `.tfw/templates/RF.md` §1 lists new and modified files without a baseline/candidate pair or a budget subset. `.tfw/templates/evidence/EV.md` has generic evidence rows; `.tfw/templates/review/verify.md` compares RF claims to actual files but does not bind the Reviewer to the Coordinator's selector.

This is not four independent defects. One absent subject and reference contract lets each role construct a different set.

### G2 — RCFR reproduces self-invalidating whole-tree accounting

Read-only sources: RCFR Phase A RF, EV, TS revisions 6–8, REVIEW revisions 2–4, and their stage traces under `workspace/2026/TFW_20260902-175227_RCFR/phase-a/`.

The fixed implementation baseline was `2728dae78d55f6cb7daa39c82874ad5b43621f8a`. The phase eventually distinguished an implementation/test/evidence subset from the whole tree, but kept both as limits:

| Observation point | Whole-tree result | Existing scoped result | Consequence |
|---|---:|---:|---|
| Revision-3 implementation return | 57 paths / 4,463 touched LOC | 41 implementation/test/evidence paths; the same 4,463 total was still whole-tree at this point | The ceiling moved to 4,600 |
| Fixed candidate `09ba070` | 69 paths / 5,517 touched LOC | 41 paths / 3,795 touched LOC | A stale EV line said 68 / 5,505 and caused an evidence-only return |
| REVIEW revision 4 post-trace state `61e1fd8` | 78 paths / 6,065 touched LOC | Accepted implementation/test/evidence content unchanged | The whole-tree ceiling moved again, to 7,000 |

The research replay used one provisional semantic selector against the same Git baseline:

```text
git diff --numstat 2728dae <candidate>
VALUE     = non-task delivery paths, excluding ordinary test files and live knowledge state
ASSURANCE = test files
TRACE     = the task's phase-local TFW/evidence/review paths
DERIVED   = .tfw/knowledge_state.yaml live generated state
```

| Candidate | `VALUE` | `ASSURANCE` | `DERIVED` | `TRACE` | Whole |
|---|---:|---:|---:|---:|---:|
| `09ba070` | **32 / 2,329** | 3 / 1,032 | 1 / 69 | 33 / 2,087 | 69 / 5,517 |
| `4e75ba4` | **32 / 2,329** | 3 / 1,032 | 1 / 69 | 38 / 2,383 | 74 / 5,813 |
| `61e1fd8` | **32 / 2,329** | 3 / 1,032 | 1 / 69 | 42 / 2,635 | 78 / 6,065 |

Format is `paths / touched text LOC`. The `VALUE` result is invariant across all three candidate states while the whole result changes by 9 paths and 548 LOC. The later changes are the RF/EV/TS/review/status/journal material required to report and judge the earlier work. This directly supports a fixed semantic subject and refutes Reviewer `HEAD` as the candidate.

### G3 — BIAI is not a false overrun after reclassification

Read-only active snapshot: `D:\projects\research\helpdesk\workspace\2026\HD_20260903-160919_BIAI\phase-a`, pinned to implementation commit `025ba55`. The phase status still reads `ONB`; its current artifacts are evidence, not final history.

The evidence record reports 23 new files, 19 modified files, and 7,710 added code LOC against a 4,200 LOC limit. New-file composition is explicit: 2,774 product LOC and 2,714 test LOC. The TS says the owner removed LOC as a stop gate for this phase while leaving both 42-file gates active. `SESSIONS.md` records the owner's reason: value and quality outrank the number, and any later config change depends on whether the growth delivered real architectural benefit rather than spaghetti.

Replaying `git show --numstat --format='' 025ba55` and classifying the 59 changed paths by accepted purpose gives:

| Class | Paths | Additions | Deletions | Touched text LOC | Notes |
|---|---:|---:|---:|---:|---|
| `VALUE` | **33** | **4,495** | **154** | **4,649** | Production code, UI, localization, dependency lock, and requested project changelog |
| `ASSURANCE` | 10 | 3,251 | 25 | 3,276 | API/unit/frontend test files |
| `TRACE` | 16 | 937 | 2 | 939 plus 6 binaries | ONB, RF, EV, evidence outputs/screenshots, journals, status |

Therefore a value-bearing rule removes 26 non-value paths and at least 4,215 touched text LOC from the delivery calculation, but the remaining value surface still exceeds 4,200 by 449 touched LOC (or 295 additions if the project retains its additions-only convention). H5 cannot honestly say the proposed rule makes BIAI fit. It converts an undifferentiated 7,710-LOC alarm into a smaller genuine value-growth decision.

The hard LOC ceiling did produce one useful effect: the overrun was detected, decomposed, and shown to the owner before completion. It did not determine the decision. The owner explicitly chose against it, while the file ceilings continued to operate.

### G4 — AFD A1.2 shows the useful case for a fixed, phase-specific bound

Read-only completed evidence: `D:\projects\research\ai-first-devices\tasks\AFD-38__mqtt_broker_security_and_hygiene\phase-a12`, corrective A1.2.2.

The Coordinator authorized exactly nine product/test paths and at most 900 touched LOC. RF named the isolated ONB baseline `ac85ad5e`, implementation candidate `0cd9d597`, and later merge separately. EV excluded foreign merge ancestry and planning/evidence traces from the manual arithmetic. REVIEW independently reproduced 9 paths and 593 additions + 53 deletions = 646 touched LOC.

The semantic replay of `git diff --numstat ac85ad5e 0cd9d597` is:

| Class | Paths | Touched LOC |
|---|---:|---:|
| `VALUE` — four production paths | **4** | **327** |
| `ASSURANCE` — five test paths | 5 | 319 |
| Whole authorized corrective | 9 | 646 |

This case supplies two counterweights to RCFR. First, an exact named implementation candidate prevents later evidence or merge ancestry from moving the figure. Second, the nine-path bound helped preserve an incident corrective boundary. But it does not prove the universal configured limits are necessary: the effective control was a phase-specific path manifest plus explicit forbidden expansions, and it mixed tests with production because the local purpose was implementation containment rather than delivered-value size.

### G5 — External practice supports smallness, but not universal hard LOC ceilings

- The official [Scrum Guide](https://scrumguides.org/scrum-guide.html) fixes the timebox and protects the Sprint Goal, while permitting scope to be clarified and renegotiated with the Product Owner as learning occurs. Developers adapt the plan toward the goal. This is a goal-bound authority model, not a fixed LOC model.
- The official [Kanban Guide](https://kanbanguides.org/the-kanban-guide/) requires explicit control of work in progress and uses a probabilistic Service Level Expectation based on historical cycle time. Exceptions to WIP control are explicit. It controls flow and risk without pricing a work item's delivered value in LOC.
- DORA's [Working in small batches](https://dora.dev/capabilities/working-in-small-batches/) reports that small batches, work visibility, experimentation, and customer feedback predict delivery and organizational performance. It establishes the value of decomposition, not a universal numerical cutoff.
- Google's [Small CLs guidance](https://google.github.io/eng-practices/review/developer/small-cls.html) explicitly says there is no hard-and-fast size rule; conceptual self-containment and reviewer judgment outrank raw line count. It counts full-file deletion differently, treats generated changes as exceptional, and requires related tests even though those tests make the change numerically larger.
- The [Agile Manifesto principles](https://agilemanifesto.org/iso/en/principles.html) pair frequent valuable delivery, simplicity, sustainable pace, technical excellence, and team adaptation. The control is a bundle of value, cadence, and quality properties rather than one size number.

The convergence is specific: small batches are valuable; limits should reveal risk early; scope may adapt inside a protected outcome; and raw LOC is at most a context signal. None of these sources establishes that one cross-domain hard ceiling is the necessary enforcement mechanism.

### G6 — Git can reproduce text arithmetic, but cannot make LOC universal

Official [`git diff` documentation](https://git-scm.com/docs/git-diff) defines `--numstat` as machine-oriented added/deleted-line output, distinguishes preimage and postimage paths for renames under `-z`, and emits `-`/`-` for binary entries. Consequences for a TFW contract:

- text touched LOC can be defined as additions + deletions for selected `VALUE` records;
- binary `VALUE` files can participate in file counts but have no truthful LOC value;
- rename classification must use `--name-status -M -z` (one logical renamed file) rather than pretending a rename is always one create plus one delete;
- a deletion remains a change to accepted value but raw deleted-line volume overstates review or delivery effort in some cases;
- candidate identity and selector are prior semantic decisions; Git only calculates their result.

For documents, presentations, images, datasets, or generated final outputs, file/path count plus delivery-specific evidence is often the only comparable default. A framework-wide alternate metric system would add machinery without making heterogeneous outputs commensurable.

### G7 — The four classes cover the observed fifth-class concern

The HL blind spot asks whether durable supporting implementation needs a fifth class. In all three corpora, supporting infrastructure required for the accepted outcome is `VALUE` even when not user-facing: RCFR scripts and adapter sources, BIAI repository/service/schema code and dependency lock, and AFD's worker and MQTT integration changes. `ASSURANCE` means the artifact's purpose is to test or demonstrate another accepted result; it does not mean “internal.” Explicit accepted-deliverable precedence makes a conformance/test product `VALUE`.

No fifth class is needed in the observed corpus. The remaining risk is gaming: a role could falsely call necessary delivery support `ASSURANCE` or a generated accepted deliverable `DERIVED`. That needs a Reviewer challenge against the accepted outcome and ACs, not more class names.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| RCFR proves whole-tree self-reference: `VALUE` is stable at 32 paths / 2,329 LOC while trace-only growth moves the whole result 69/5,517 → 78/6,065. | Challenge whether the provisional selector can be gamed and whether live generated state is always `DERIVED`. |
| BIAI reclassification removes assurance/trace inflation but leaves a genuine `VALUE` overrun: 33 paths / 4,649 touched LOC. | Decide whether that overrun should hard-stop, softly trigger decomposition, or be Coordinator-rulable inside the frozen outcome. |
| AFD A1.2 validates fixed references and a phase-specific exact-path bound, not a universal configured ceiling. | Separate the value-size question from incident containment and reviewer-load controls. |
| Existing TS/RF/EV/Verify sections can carry the information; the absent piece is a shared contract, not a missing artifact. | Build and eliminate complete configurations; prove the smallest carrier changes. |
| External sources support small batches, explicit policies, and adaptive scope, but none establishes a universal hard LOC rule. | Test the strongest case for retaining hard ceilings before rejecting or narrowing them. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?

Stage complete: YES
→ User decision: Advance under the owner's initial instruction to complete iteration 1; no new scope or owner-only choice was introduced at Gather.
