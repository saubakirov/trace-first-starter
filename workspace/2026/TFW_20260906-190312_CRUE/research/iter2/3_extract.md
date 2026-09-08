# Extract — "What do we NOT see?"
> **Mindset:** Analyst. Build coherent behavioral mechanisms from the dimensions before selecting one.
> **Test:** "Does the configuration space expose a combination not proposed in the Briefing, and do the same cases make its behavior distinguishable?"
> Parent: [HL-TFW_20260906-190312_CRUE](../../HL-TFW_20260906-190312_CRUE.md)
> Goal: TFW releases reach existing projects as coherent, safe, and understandable improvements that agents can apply from shipped instructions while owners retain project purpose and consequential choices.

## Evidence boundary

- **Primary-source observations** are attributed to linked papers, standards, or model developers.
- **Configurations and transfer hypotheses** are this Researcher's constructions. They have not been observed in TFW or shown to improve an update.
- **Observed TFW behavior in this pass:** none. Extract still does not inspect the released update procedure. Configuration-first independence remains intact; baseline applicability belongs to Challenge.

## Configuration Space

The full cross-product of Gather's eight dimensions contains many incoherent and redundant rows. These four configurations keep all eight factors visible while changing the mechanism that controls behavior, not merely the document layout. No row is recommended at Extract.

| Config | D1 · Authority representation | D2 · Ambiguity and decision boundary | D3 · Instruction shape | D4 · Update and recovery semantics | D5 · Evidence binding | D6 · Owner-facing interaction | D7 · Benefit and limitation account | D8 · Behavioral evaluation |
|--------|-------------------------------|--------------------------------------|------------------------|--------------------------------------|-----------------------|-------------------------------|-----------------------------------------|----------------------------|
| C1 · Constitutional Interpreter | Fixed invariants plus delegated defaults | Act inside an envelope; stop on material unresolved consequence | Typed purpose/invariant/rule/default plus few contrastive examples | Prepare/apply/verify/report | Claim-to-source citation | Consequence card at a material choice plus final outcome | Benefit/cost/limit/next-action case | Adversarial scenario and context-position variants |
| C2 · Evidence-Gated Protocol | Ordered source/role hierarchy | Ask when a transition's evidence is incomplete | Stage cards with entry/exit evidence | Checkpoints, evidence-qualified replay, semantic compensation | Pre/post observation plus named check | Progressive disclosure with exceptions first | Applicable benefit plus receiver evidence | Multi-trial trajectory and end-state grading |
| C3 · Outcome-Backward Case | Conflict cases with an explicit resolution rubric | Degrade to a narrower safe service | Compact claim table with linked technical detail | Prepare/apply/verify/report derived backward from reportable claims | Claim-to-source plus receiver-outcome evidence | Project outcome first; choice card only when a claim needs owner authority | Benefit/change/limit/next-action case | Representative agent plus owner-comprehension task |
| C4 · Local Decision Tuple | Fixed invariants plus delegated defaults | Act inside an envelope; stop on material unresolved consequence | A short decision tuple at each consequential boundary | Re-observe before action; evidence-qualified replay; checkpoint only in the existing run record | Pre/post observation plus named check | Progressive disclosure; report only consequential tuples | Applicable benefit plus receiver evidence and explicit unknowns | Adversarial cases across model/context variants plus state check |

**New combination test.** C3 and C4 were not proposed in the Briefing. C3 derives the work backward from truthful owner claims rather than from a forward procedure. C4 treats each consequential boundary as a local observe/authorize/act/prove/message loop and stores durable facts only in an existing run record; it is neither a conventional staged installer nor a claim registry.

## Common scenarios

All four configurations are compared on the same inputs:

- **S1 · Routine repeat:** the project already contains established settings and some target content; no evidence of a new project decision.
- **S2 · Ownership collision:** a file the release treats as framework-owned contains legacy project-purpose material; replacement would change meaning.
- **S3 · Interrupted application:** the prior session ended after a possible write but before verification or final communication.
- **S4 · Source defect:** the pinned release candidate fails its own coherence check before project application.

## Findings

### E1 · C1 Constitutional Interpreter — judgment is driven by a small authority model

**Primary-source observation.** OpenAI describes its Model Spec as several kinds of guidance: a small set of hard boundaries, broader defaults, authority ordering, decision rubrics for gray areas, and a small number of compliant/non-compliant examples near important boundaries. It explicitly says a rubric supports consistent judgment without pretending there is one mechanical rule, and that the Spec is an interface rather than an implementation. It also reports that production behavior can lag, generalize for unintended reasons, and require scenario-based evaluation ([OpenAI, “Inside our approach to the Model Spec,” 2026](https://openai.com/index/our-approach-to-the-model-spec/)).

**Transfer hypothesis.** A release/update prompt can carry a compact “behavioral constitution”: preserve project-owned meaning and history; do not claim unsupported completion; reuse settled choices; expose only consequential unresolved choices. Defaults describe ordinary autonomy, and a materiality rubric resolves the gray boundary. A few contrastive examples show what counts as hidden authority expansion versus technical discovery.

**Short instruction specimen.** This is comparative research text, not product wording:

```text
INVARIANTS
- Preserve project-owned purpose, decisions, state, and history.
- Never report completion without receiver evidence.

DEFAULT
Reuse an established project choice when current evidence identifies it and the
update does not change its meaning.

DECISION RUBRIC
If the effect is reversible, within stated scope, and meaning-preserving, proceed.
If evidence is missing, narrow the action. If project meaning or irreversible
effect is unresolved, stop only that effect and ask with consequence + recommendation.
```

**Behavior on the common scenarios.** In S1, the agent cites the established setting and proceeds without reopening it. In S2, the preservation invariant defeats the replacement default; the agent isolates the affected file and asks a project-consequence question. In S3, the “no unsupported completion” invariant triggers re-observation before any retry. In S4, source failure prevents application and the owner receives a noncompletion statement.

**User benefit.** The agent has a portable judgment vocabulary; the owner sees a question only when project meaning is at stake.

**Carrier and cost.** The carrier can be the existing canonical update instruction plus existing run/update record. Read cost is one compact rule block plus a few boundary examples; maintenance cost is keeping examples consistent with invariants. No new registry is required.

**Boundary/counterexample.** A model may misclassify materiality, overweight an example, or over-refuse. The written constitution is desired behavior, not enforcement. A project-specific fact can still be absent from current context.

**Observable check.** Across S1–S4 with reordered context and an injected lower-trust instruction, grade preservation, question materiality, unsupported-success claims, and over-refusal separately.

### E2 · C2 Evidence-Gated Protocol — observed state controls progress

**Primary-source observation.** Anthropic distinguishes an agent's transcript or trajectory from the final environment state, recommends multiple trials because outputs vary, and combines code-, model-, and human-based graders according to the property being tested. It notes that tool-using agents modify state across turns, errors propagate, exact graders are brittle, model graders need human calibration, and evaluation is of the model plus its harness—not the model alone ([Anthropic, “Demystifying evals for AI agents,” 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)). NIST likewise calls for conditions similar to deployment and warns against benchmark-to-use mismatch ([NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)).

**Transfer hypothesis.** The update becomes an evidence-gated protocol. Each transition names the observation required before entry and the proof required at exit. A later agent resumes by comparing actual state to checkpoint evidence, not by trusting the last prose status. Compensation is semantic and only used where authorized.

**Short instruction specimen.** Comparative only:

```text
DISCOVERED -> PREPARED only with pinned-source proof + receiver inventory.
PREPARED -> APPLIED only with resolved ownership effects + bounded change set.
APPLIED -> VERIFIED only with observed post-state + applicable project checks.
VERIFIED -> REPORTED only when every user-visible claim cites its supporting result.

On resume: inspect state first. Never repeat an uncertain non-repeatable effect.
If a transition lacks evidence, preserve completed evidence and stop at that state.
```

**Behavior on the common scenarios.** In S1, discovery recognizes target effects already present; the agent verifies rather than blindly reapplies. In S2, PREPARED cannot be reached because ownership effect is unresolved, while unrelated discovery remains usable. In S3, the agent reconstructs the highest supported state from the environment and record, then continues or reports partial state. In S4, source proof fails before PREPARED, so project data remains untouched.

**User benefit.** “Complete,” “partial,” and “not applied” correspond to evidenced states, improving resume and failure candor.

**Carrier and cost.** Entry/exit conditions can live as headings in the existing workflow; durable checkpoints can use the existing run/update record. There is no separate state registry, but the record must expose enough evidence to reconstruct the state. Read cost is higher than C1 because every stage has gates; maintenance cost rises when a new release changes an entry or exit condition.

**Boundary/counterexample.** Stage vocabulary can become pseudo-code that the model imitates without checking state. A gate list can reproduce checklist overload, and real project operations may not have safe compensation. Fine-grained states increase synchronization cost across prompt copies.

**Observable check.** Interrupt each scenario before and after every possible write, hide or stale one checkpoint, and run multiple fresh-agent trials. Grade actual end state and trajectory separately; a printed state label earns no credit without its observation.

### E3 · C3 Outcome-Backward Case — truthful owner claims define necessary work

**Primary-source observation.** Human-AI decision-support research reports that explanations do not reliably calibrate reliance and can sometimes increase overreliance. A 2025 mixed-methods study compared direct recommendations with support embedded into a user's own rationale; the mechanisms produced different benefits and tensions, and preferences varied by participant. The authors argue that realistic decision processes cannot be reduced to simple input-output correctness ([Reicherts et al., CHI 2025](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/03/AI-Help-Me-Think-CHI-2025.pdf)). The earlier HAI guidelines emphasize capability limits, contextual information, correction, consequences, and change notification, while acknowledging context and observability limits ([Amershi et al., CHI 2019](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf)).

**Transfer hypothesis.** Design the update backward from four owner-level claims: applicable benefit, actual project change/outcome, material limitation, and next action. For each claim, the agent determines the minimum source and receiver evidence needed. Work not needed to support or refute those claims stays in technical detail; a project choice appears only when a truthful claim cannot be completed without owner authority.

**Short instruction specimen.** Comparative only:

```text
Before changing the project, draft four provisional claims:
1. BENEFIT — what this release can improve here, with release evidence.
2. OUTCOME — what changed or did not change here, with receiver evidence.
3. LIMIT — what remains unverified, partial, refused, or incompatible.
4. NEXT — the smallest useful continuation available now.

Perform only the discovery/application/verification needed to make those claims true.
If a claim depends on a project decision, show the consequence, evidence,
recommendation, and alternative; do not decide it silently.
```

**Behavior on the common scenarios.** In S1, the agent checks applicability and reports only the benefit actually present plus verification, without a mechanical inventory. In S2, it cannot truthfully claim preserved project purpose, so it presents a consequence card before replacement. In S3, OUTCOME remains partial and NEXT identifies safe re-observation/resume rather than declaring success. In S4, OUTCOME says no project application occurred, LIMIT names source incoherence, and NEXT points to a corrected release rather than project repair.

**User benefit.** The owner receives a project-centered account instead of internal topology, while negative outcomes remain useful and actionable.

**Carrier and cost.** The four claims can be fields in the existing final briefing/update record; evidence remains in existing source, diff, and check outputs referenced by that record. This is a reading and synthesis rule, not a new evidence registry. Read cost is low for the owner and medium for the agent; maintenance cost is the risk of duplicating release claims unless benefits are referenced rather than copied.

**Boundary/counterexample.** Backward design may optimize for a persuasive message, omit technically necessary work, or invent evidence to fill a desired narrative. An explanation can increase misplaced trust. Some technical invariants deserve enforcement even when invisible to the four claims.

**Observable check.** Seed unsupported release benefits, successful writes with failed project checks, and a fluent but false summary. Grade every visible claim against evidence, then ask a user to identify benefit, completion status, limitation, and next action without opening the trace.

### E4 · C4 Local Decision Tuple — a minimal hybrid without a new state machine

**Primary-source observation.** RFC 9110 permits retry based on defined semantics and observed conditions rather than on the label alone; it distinguishes safe from unsafe effects and cautions automated retry of non-idempotent requests ([RFC 9110 §§9.2.1–9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#name-common-method-properties)). OpenAI's Model Spec design uses decision rubrics for gray areas while warning that not all important behavior reduces to rules. Anthropic's agent-eval guidance distinguishes trajectory from outcome. These sources jointly suggest a local decision/evidence loop, but none studies this proposed tuple.

**Transfer hypothesis.** At each consequential boundary, the agent resolves one short tuple: `OBSERVED → AUTHORIZED → EFFECT → ACTION → PROOF → MESSAGE`. The tuple is local working structure, not a persistent global ledger. Only material results enter the existing update record. Ordinary mechanical steps can share one tuple; a new owner decision or uncertain replay cannot.

**Short instruction specimen.** Comparative only:

```text
For the next consequential effect, resolve:
OBSERVED: current project/source fact and its location.
AUTHORIZED: prior decision, explicit grant, or unresolved owner choice.
EFFECT: project consequence and reversibility.
ACTION: proceed, narrow, or stop only this effect.
PROOF: post-state/check that would justify the outcome claim.
MESSAGE: owner-visible consequence now, or final benefit/outcome/limit/next.

Persist only material observations/actions/proofs in the existing update record.
```

**Behavior on the common scenarios.** In S1, one tuple groups settled, meaning-preserving actions and verifies their post-state. In S2, AUTHORIZED is unresolved and EFFECT changes project purpose, so only that effect stops with a consequence card. In S3, OBSERVED and PROOF are re-established before deciding whether replay is safe. In S4, source observation prevents any project ACTION and yields a concise failure message.

**User benefit.** The same reasoning shape connects agent autonomy, owner authority, recovery, evidence, and communication without exposing routine tuples to the owner.

**Carrier and cost.** The tuple can appear once in the existing workflow and material instances in the existing update record. It adds no file, registry, or separate lifecycle state. Read cost is the smallest of the four configurations; maintenance cost concentrates in the definitions of “consequential,” “material,” and “proof.”

**Boundary/counterexample.** The tuple may be too abstract for a weak agent, disappear into uninspectable internal reasoning, or vary between steps. Grouping actions can hide one material effect. Without contrastive scenarios and outcome checks, minimality becomes underspecification.

**Observable check.** Run S1–S4 plus mixed mechanical/material actions. Grade whether the agent emits a durable tuple only when needed, preserves every material effect, asks no routine technical question, and ties its final message to observed proof.

### E5 · Same-scenario behavioral comparison

| Config | S1 · Routine repeat | S2 · Ownership collision | S3 · Interrupted application | S4 · Source defect | Mechanism that makes the behavior differ |
|---|---|---|---|---|---|
| C1 | Apply defaults under invariants | Rubric escalates project meaning | Invariant forces re-observation | Invariant blocks unsupported application/completion | Global authority model interprets every case |
| C2 | Reconstruct supported state; verify | Transition evidence is incomplete | Resume from highest evidenced state | Source gate prevents PREPARED | Explicit transitions and evidence gates control progress |
| C3 | Work backward from truthful benefit/outcome | Preservation claim cannot be supported without choice | Outcome/limit/next remain partial | Negative outcome and useful next action are first-class | Owner-visible claims determine the work and question |
| C4 | Resolve one grouped local tuple | Local AUTHORIZED/EFFECT pair stops only the collision | Local observation/proof determine replay | First tuple terminates before project action | Consequential decision loop connects authority, effect, proof, and message |

The configurations can produce similar visible sentences in S4, but for different reasons. This is why evaluation must inspect both trajectory and outcome: identical prose does not establish identical authority or recovery behavior.

### E6 · Carrier and maintenance comparison — claim-specific evidence without a registry

| Config | Canonical instruction carrier | Durable evidence carrier | Agent read cost | Maintenance pressure | New registry? |
|---|---|---|---|---|---|
| C1 | Existing workflow: invariant/default/rubric block plus few cases | Existing update record links observed results | Medium | Rule/example consistency and provider interpretation | No |
| C2 | Existing workflow: stage entry/exit conditions | Existing update record contains checkpoints and proofs | High | Gate proliferation, copied prompt synchronization, state vocabulary | No, if the record remains authoritative |
| C3 | Existing workflow: four provisional claim rules; existing final briefing form | Existing sources, diff/check outputs, and update record references | Medium | Release-claim duplication or persuasive-summary bias | No |
| C4 | Existing workflow: one local decision tuple | Existing update record stores only material tuple results | Low | Ambiguous materiality/proof terms and weak-agent underspecification | No |

**Extraction decision ED1:** claim-specific evidence is a correspondence rule—each claim points to the already authoritative source or observed result—not a separate inventory of claims. A new mutable registry has no demonstrated need in any configuration.

**Extraction decision ED2:** keep all four configurations for Challenge. C1 tests portable judgment, C2 tests explicit progression, C3 tests project-centered truthfulness, and C4 tests whether the same responsibilities fit a smaller local mechanism. Removing one now would erase a distinct failure mode.

**Extraction decision ED3:** use the common S1–S4 cases for behavioral comparison, then add adversarial variants rather than inventing a different favorable scenario for each configuration. Outcome and trajectory are both graded; exact wording is not.

**H4 status after Extract:** open. C4 is a genuinely simpler candidate form and C3 is a genuinely different outcome-backward framing, so H4 is no longer merely speculative. Neither has yet survived baseline applicability, weak-agent, interruption, hidden-authority, or maintenance challenges.

## OODA record

| Pass | Observe | Orient | Decide / Act |
|---|---|---|---|
| 1 | Cross-referenced all eight Gather dimensions | Row-wise “best practices” did not form a behavior mechanism | Constructed C1 authority interpreter, C2 evidence protocol, and C3 outcome-backward case |
| 2 | Model Spec design, agent-eval practice, and HAI reliance evidence | Specs need rubrics and evals; trajectories and end states differ; explanations can increase overreliance | Added C4 local decision tuple and required same-scenario trajectory/outcome checks |
| 3 | Compared carriers and reading/maintenance pressure | Claim-specific evidence can be references in existing artifacts; a new registry would duplicate truth | Recorded ED1–ED3; retained all four without ranking before Challenge |

**Metacognitive check:** Extract discovered two combinations absent from the Briefing. Most importantly, “owner-centered” need not mean adding a communication layer after the procedure: C3 reverses causality by making truthful owner claims define necessary evidence and work. C4 shows a possible simplification below a full staged protocol, but also exposes the risk that compactness merely hides judgment.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Four coherent, behaviorally distinct configurations across all eight dimensions | Test internal consistency and reject combinations that fail safety, authority, recovery, or usability cases |
| Identical S1–S4 comparison with short instruction specimens | Add weak-agent, adversarial-context, concurrent-change, and misleading-success variants |
| Existing-carrier designs for every configuration; no claim registry required | Inspect released TFW 2.2.0 only now and measure applicability/read/maintenance deltas |
| C3 outcome-backward and C4 local tuple are novel relative to Briefing | Determine whether either is actually simpler and complete, or record the negative H4 result |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?
- [x] At least three coherent mechanisms compared on the same scenarios?
- [x] H4 tested without premature acceptance?
- [x] Counter-evidence and analogy limits preserved?
- [x] At least two stage decisions recorded?
- [x] Metacognitive check completed?

Stage complete: YES
→ User decision: Pending Main Coordinator; Researcher recommends closing Extract and proceeding to Challenge.
