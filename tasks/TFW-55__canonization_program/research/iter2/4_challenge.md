# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-55](../../HL-TFW-55__canonization_program.md)
> Goal: Attack the fourteen Extract configurations and frozen matched fixtures under uniform falsification, while keeping evidence viability separate from frozen-HL compatibility.

## Authorized frozen instrumentation

- Coordinator verdict: `close stage — v2 authorized for Challenge`.
- Normative design: `fixtures/frozen_design.v2.json`.
- Required SHA-256 rechecked before the first run: `d7fdb413af669abdf92cb3c055f7a966db3d4daec58d2ac15c36e679805f0f7a` — **MATCH**.
- All three `SHA256SUMS.v2` entries — **MATCH**.
- v1 remains `rejected-before-run / no evidence`; v1 critic/scorer runs = `0/0`.
- v2 pre-run run artifacts = `0`.
- Frozen v2, `README_V2.md`, `SHA256SUMS.v2`, and `V1_REJECTED.md` will not be edited during Challenge.

### Controlled run metadata

| Role | Model | Reasoning | Isolation/runtime | Rule |
|---|---|---|---|---|
| Critic | `gpt-5.6-sol` | `low` | one collaboration subagent with `fork_turns=none` per opaque variant; unique agent id/task name recorded per run | No tools, project/thread history, mapping, answer key, founder intent, or cross-variant context |
| Scorer | `gpt-5.6-sol` | `low` | separate collaboration subagent with `fork_turns=none` per raw output; unique agent id/task name recorded per score | Receives only opaque packet/output, programmatic checks, neutral `EXPECTED`, rubric and scorer schema |

The collaboration runtime guarantees a fresh prompt context with `fork_turns=none` and identical declared model/reasoning settings. If a spawn cannot retain those settings or an agent uses tools/outside context despite the packet rule, the affected family is invalidated and returns to Extract; no result will be imitated locally.

## Consistency Check

The first category attempt remains invalid instrumentation and contributes no evidence. The separately gated v4 restart completed validly with no reuse. Category-scoped dispositions below use only v4; Challenge still cannot issue whole-iteration dispositions because ablation and later families are unauthorized and unrun.

## Findings

### C1 — Category family invalidated; no mapping reveal or inference

The five category critics completed pass 1 in frozen opaque order. Exact packets and raw outputs were preserved. Opaque scoring completed for the first three labels. The fourth scorer received an abbreviated packet/rubric/schema rather than the exact frozen scorer input. This violates the v2 isolated-scoring assembly and invalidates the **whole category family**; it is not a malformed model result or a replication trigger.

Consequences applied literally:

- no selective scorer repair, pass 2, mapping reveal, comparison, or category inference;
- the fifth critic's output is preserved, but its scorer was never started;
- ablation and every later family were not started;
- all completed category traces are instrumentation/audit records only;
- no C1/C3/C4/C9/C10 or H2 disposition is drawn.

Trace: [category invalidation](challenge_runs/category/INVALIDATION.md) and [pass-1 checksums](challenge_runs/category/pass1/SHA256SUMS).

The external counter-control remains unchanged: the official [2020 Scrum Guide](https://scrumguides.org/scrum-guide.html) calls Scrum a lightweight framework while making its elements essential and its framework purposefully incomplete. Even a future valid category pass cannot treat correct boundary application alone as evidence for methodology/discipline.

### C2 — Challenge must return the category family to Extract

The defect came from manually composing a large opaque scorer prompt even though v2 specified exact assembly. A replacement category execution package must be frozen and gated before any rerun. It must restart the complete category family from pass 1; invalidated v2 runs cannot be reused as a first pass or replication.

## Historical invalidation checkpoint

| Found | Remaining |
|-------|-----------|
| v2 pre-run integrity/settings were valid; all five category critics and four scorer attempts are preserved; one scorer-input violation invalidated the family before mapping reveal. | New Extract gate must freeze a mechanically preassembled category scorer-input procedure. Challenge remains stopped before ablation; all requested configuration and H1–H4 dispositions remain pending valid evidence. |

**Sufficiency:**
- [x] External source used? — official Scrum Guide rechecked as the mandatory framework/category counter-control.
- [ ] Briefing gap closed? — blocked by invalid category instrumentation before later families.
- [ ] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: NO
→ User decision: **Challenge execution authorized, then stopped by freeze rule. Return category family to a new Extract gate; no comparative evidence produced.**

### C3 — Authorized v3 stopped at dispatch-verifiability preflight

The coordinator accepted C1/C2, verified the replacement hashes, and authorized a v3 category-only restart. The authorization required a post-dispatch SHA-256 over the actual inline message obtained from orchestration trace. The collaboration spawn interface has no API that returns those dispatched bytes. Hashing the intended file or reconstructing the message would not meet the gate.

No v3 critic was spawned and no experimental output exists. Challenge therefore stopped again before any run and returned only the execution instrumentation to Extract. `TFW55-I2-CATEGORY-FILEREAD-v4` is pending a new gate; it moves exact experimental prompt delivery to a hash-attested local file read while preserving all v2/v3 semantics and scoring constraints.

Historical pre-v4 status: **NO RUN AUTHORIZED; category evidence empty.**

### Authorized category file-read restart

- Coordinator verdict: `close stage — category file-read v4 authorized`.
- v4 design SHA-256 rechecked: `05cb8b5c1dbf4ea3171753a12759e6242838e933fddfc690c28695cdf4e51c63`.
- v4 `SHA256SUMS`: 3/3 match; manifest SHA-256 `474d181be45e2615b0e6e7d55e3f4b78501360a397ee0980cbba0c0a1a2ec1bd`.
- Upstream v2/v3 hashes match; v3 runs remain `0`; v4 pre-run artifacts `0`.
- Authorized scope: complete category restart only. Ablation and later families remain unauthorized.
- Attestation meaning is narrow: it proves the sanctioned reader verified and emitted the named strict-UTF-8 file bytes before the role answered. It does not prove filesystem sandboxing, absence of technical access, or semantic consumption.
- For category v4 only, the later gate superseded the original no-tool delivery assumption with exactly one sanctioned reader invocation and one assigned raw-output write per role. No other access was permitted.

### C4 — Valid category v4 result: shared boundary applies; category advantage not observed

The full trace is [CATEGORY_LEDGER.md](challenge_runs/category_v4/CATEGORY_LEDGER.md); exact run metadata is [run_manifest.json](challenge_runs/category_v4/run_manifest.json). The 52-entry [SHA256SUMS](challenge_runs/category_v4/SHA256SUMS) verifies completely; its SHA-256 is `6eb41da235bef435f5a1d270fbe1b909c7c031e6e39657b63afb887c635abb57`.

| Pass | Q7 | M2 | R5 | K8 | V1 |
|---|---|---|---|---|---|
| 1 | `2/2/2; d0; a3` | `2/2/2; d0; a4` | `2/2/2; d0; a4` | `2/2/2; d0; a3` | `2/2/2; d0; a3` |
| 2 | `2/2/2; d0; a3` | `2/2/2; d0; a3` | `2/2/2; d0; a3` | `2/2/2; d0; a3` | `2/2/2; d0; a3` |

Scores are definition/exclusion/rule-application; `d` is drift and `a` ambiguity. Pass 1's ambiguity difference triggered the mandatory complete second pass. Pass 2 did not confirm it, so it is an unstable observation rather than comparative evidence. No third pass ran.

Mapping was revealed only after both complete passes and all audits: `Q7=C1`, `M2=C4`, `R5=C10`, `K8=C9`, `V1=C3`.

Permitted inference: under one controlled model/reasoning setting, all five packets supported exact immediate application of the same provisional F1–F4 boundary to the seven neutral cases in both probes; no stable category-wording difference was observed.

Forbidden inference: candidate equivalence; a true discipline/methodology/hierarchy category; human comprehension or terminology reception; novelty or adoption; or conversion of a usable boundary into proof of a category above framework. Scrum remains the required counter-control.

| Candidate | Evidence viability | Frozen-HL compatibility | Category-only disposition |
|---|---|---|---|
| C1 | Valid; no stable advantage over C4 | Directly compatible with frozen discipline-first wording | Survives, but discipline receives no comparative support |
| C3 | Valid; no stable advantage over C4 | Primary methodology would require conditional A1 treatment | Survives as evidence-viable amendment candidate, not winner |
| C4 | Valid full-strength low-assumption control | Primary framework conflicts with frozen fundamental-discipline wording; architecture fits | Survives intact; higher-category claims still must beat it |
| C9 | Valid; category result does not test quiet terminology | Category/public-language changes require conditional A1/A2 treatment | Survives; not distinguished from C3 and cannot mature A2 |
| C10 | Valid; hierarchy necessity remains unproved | Partly matches frozen layers but conflicts with one discipline-first primary formulation | Survives as positioning/amendment candidate |

No candidate is eliminated by a confirmed comparative difference. The asymmetrical narrowing is that shared-boundary applicability survives while the extra higher-category claims gain no comparative support over C4.

| Hypothesis | Category-only status | Frozen-HL compatibility |
|---|---|---|
| H1 | Not tested; remains conditionally supported from Iteration 1 | Unchanged |
| H2 | Narrowed: shared composition is immediately applicable in this model setting; no evidence here that discipline/methodology/hierarchy is a better primary category | Remains open; C4 is the low-assumption control and A1 stays conditional |
| H3 | Not tested; remains narrowly supported | Unchanged |
| H4 | Not tested; remains mixed/open | Unchanged |

### Category execution checkpoint

| Passes | Validity | Replication | Mapping | Allowed inference | Prohibited inference |
|---|---|---|---|---|---|
| 2 complete | Valid; 20/20 attestations and 20/20 raw outputs audited, zero schema failures | Triggered by pass-1 ambiguity; not confirmed in pass 2 | Revealed after all runs/scores | Bounded immediate shared-boundary application; no stable wording difference observed | Equivalence, higher-category truth, human/field/novelty/learning claims |

Category checkpoint complete: YES
→ User decision at checkpoint: **Pending category ledger gate. Stop before ablation and return later-family execution instrumentation to Extract only after coordinator direction.**

### C5 — Proportionality stop closes experimental work

The coordinator accepted category v4 as the only valid bounded critique family and terminated all further experimental instrumentation. The owner challenged the duration and opacity of the process; another execution package would cost more than its likely decision value, while model probes could not settle the remaining human reception, pedagogy, adoption, or positioning questions.

| Planned family | Final status | Reason | Evidential effect |
|---|---|---|---|
| Ablation | **NOT RUN — coordinator-terminated** | Logical ablations already expose the fixture's internal consequences; another model application pass has low incremental decision value | Neither supports nor refutes F1–F4 minimality or real-world adoption |
| Authority | **NOT RUN — coordinator-terminated** | Source/logic can specify precedence; model accuracy cannot demonstrate maintenance or external-author use over time | H1 remains conditional; explicit precedence is still required in the rewrite |
| D9 agent route | **NOT RUN — coordinator-terminated** | One-model route accuracy cannot settle human consumption or cross-tool robustness | No D9 alternative is selected; human/cross-tool contract remains future field evidence |
| Terminology | **NOT RUN — coordinator-terminated** | Model-induced ambiguity cannot answer human reception | `self-aware` remains an owner/future-human decision; A2 does not mature |
| Exposition ordering proxy | **NOT RUN — coordinator-terminated** | Linear-order sensitivity cannot choose staged/branched exposition or show learning efficacy | Two-surface subtraction survives; Light → Assisted → Full superiority remains unproved; A3 does not mature |

No missing run is simulated, imputed, or treated as negative evidence.

### Final Challenge disposition

- **Architecture:** corpus preserves history/evidence; essay selects stable current meaning; living specification governs current mechanics. This is conditionally supported. The rewrite must state precedence explicitly; a new canonical surface is not justified.
- **Semantic floor:** F1 human purpose/authority, F2 bounded delegation, F3 selected durable material trace plus result/current state, and F4 authoritative result/continuation form the best-supported positive floor. R1 proportional assurance remains a separate constraint, not a fifth universal artifact.
- **Category:** individual component novelty is refuted by adjacent primary/official sources. Consequential composition remains plausible and immediately applicable in the category probe. A discipline, methodology, or hierarchy above framework is not research-demonstrated. C4 remains the lowest-assumption description; C1/C3/C9/C10 remain positioning choices with additional burden.
- **Teaching/exposition:** teaching observation, proposed mechanism, and demonstrated outcome stay separate. Two-surface subtraction survives; terminology reception, D9 human contract, and Light → Assisted → Full learning superiority are future human/field questions and cannot be canonicalized as proven.
- **HL compatibility:** evidence viability remains separate from frozen-HL compatibility. A1–A3 remain conditional owner decisions or future-test candidates; none is an evidence-mature amendment proposal.

| Hypothesis | Final Challenge status | Reason |
|---|---|---|
| H1 | **Conditionally supported** | Layered selector architecture is coherent and avoids corpus monism; explicit precedence and real outsider use remain untested |
| H2 | **Narrowed / open** | Component novelty is refuted and composition is plausible/applicable, but a category above framework is not demonstrated by sources or the bounded model probe |
| H3 | **Narrowly supported** | Stable conceptual knowledge can be routed separately from rhetoric/pedagogy/outcome claims; no new teaching-efficacy evidence was collected |
| H4 | **Mixed / open** | Two-surface subtraction survives; terminology, D9 human compatibility, and progression superiority remain unproved |

## Final Checkpoint

| Found | Remaining / deliberately deferred |
|---|---|
| Layered self-canon architecture and selected-continuity semantics are sufficient for planning. | Actual rewrite must make precedence explicit. |
| Primary sources refute component novelty and do not supply a universal category taxonomy. | Owner must choose calibrated positioning; human reception/adoption cannot be derived from this research. |
| Category v4 validly found no stable category-wording difference under one model setting. | Human terminology, D9, pedagogy, cross-tool robustness, and real non-code adoption remain future human/field evidence. |
| Proportionality now favors decision and bounded uncertainty over further opaque instrumentation. | No further research iteration is justified solely to simulate those empirical questions. |

**Sufficiency:**
- [x] External source used? — eight primary/official controls remain the external evidence lane.
- [x] Briefing gap closed? — each planned difference is resolved by source/logic, bounded category evidence, or explicit empirical deferral.
- [x] Pairwise incompatibility checked? Survivors listed? — C1/C3/C4/C9/C10 dispositions and frozen-HL compatibility are explicit; none is eliminated by comparative model evidence.

Stage complete: YES
→ User decision: **`close stage` — accept category v4; terminate later experiments for diminishing decision value; synthesize Iteration-2 RES.**
