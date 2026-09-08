# Gather — "What do we NOT know?"
> **Mindset:** Explorer. Widen before narrowing; treat every transfer from software engineering as a hypothesis about agent behavior.
> **Test:** "Can I name every dimension and its alternatives without confusing a prompt with executable enforcement?"
> Parent: [HL-TFW_20260906-190312_CRUE](../../HL-TFW_20260906-190312_CRUE.md)
> Goal: TFW releases reach existing projects as coherent, safe, and understandable improvements that agents can apply from shipped instructions while owners retain project purpose and consequential choices.

## Evidence boundary

- **Primary-source observations** below are claims made or results reported by the linked standards bodies, papers, and model developers.
- **Transfer hypotheses** are this Researcher's interpretations for an agent reading release/update prompts. They are not observed TFW behavior and remain open through Extract and Challenge.
- **Observed TFW behavior in this pass:** none. Gather deliberately did not inspect the released update procedure; the approved HL supplied purpose and safety bounds, while applicability to `v2.2.0` / `8e68ab37d300122ff110500ad58f354f76b6210f` is deferred until independent configurations exist.

## Dimensions

Each row is an independent decision factor. Alternatives are deliberately unranked.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1 · Authority representation | Flat prose with contextual interpretation | Ordered source/role hierarchy | Fixed invariants plus delegated defaults | Conflict cases with an explicit resolution rubric |
| D2 · Ambiguity and decision boundary | Ask all configuration questions before action | Ask when evidence is incomplete | Degrade to a narrower safe service | Act inside a declared envelope; stop on material unresolved consequence |
| D3 · Instruction shape | One narrative procedure | Typed blocks: purpose/invariant/rule/default/example | Stage cards with entry/exit evidence | Compact state table plus linked detail |
| D4 · Update and recovery semantics | Linear best effort | Prepare/apply/verify/report | Evidence-qualified replay of intended-idempotent actions | Checkpoints with semantic compensation and explicit resume |
| D5 · Evidence binding | Agent self-report | Claim-to-source citation | Pre/post observation plus named check | Independent or representative behavioral assessment |
| D6 · Owner-facing interaction | Full technical checklist | End-only summary | Progressive disclosure with exceptions first | Consequence card at each material choice plus final outcome |
| D7 · Benefit and limitation account | Changelog inventory | Claimed release capability | Applicable benefit plus receiver evidence | Benefit/cost/limit/next-action case |
| D8 · Behavioral evaluation | Text/lint conformance | One-model happy path | Adversarial scenario and context-position variants | Representative agents plus owner-comprehension task |

## Findings

### G1 · Authority is a behavior to elicit and test, not a heading that executes

**Primary-source observations.** OpenAI's 2026 instruction-hierarchy work explicitly orders trusted instruction sources and reports stronger conflict handling after targeted training. The same report names three failure boundaries: complicated instructions can look like hierarchy failures, LLM judges are fallible, and reward shortcuts can cause useless behavior such as over-refusal. Its evaluation uses simple, objectively gradable constraints before testing held-out and adversarial cases ([OpenAI, “Improving instruction hierarchy in frontier LLMs”](https://openai.com/index/instruction-hierarchy-challenge/)). Anthropic's Constitutional AI experiment combines a written list of principles with model-generated critique/revision and subsequent supervised and reinforcement learning; its reported behavior is therefore evidence for a principle-and-critique mechanism, not evidence that placing principles in an inference-time prompt is sufficient ([Bai et al., 2022](https://arxiv.org/abs/2212.08073)).

**Transfer hypothesis.** An update instruction can make authority more legible by naming (a) non-negotiable project-preservation invariants, (b) evidence the agent may interpret, (c) decisions already authorized, and (d) the exact condition that returns a choice to the owner. A short conflict rubric and contrastive cases may cue better behavior than repeated prohibitions.

**Boundary and counterevidence.** This remains prompt-level guidance. It cannot import model training, guarantee that every provider follows the same hierarchy, or make an ambiguous materiality judgment objective. Anthropic demonstrated that sufficiently many in-context examples could override safety-trained behavior across multiple model families; mitigation reduced but did not establish universal immunity ([Anthropic, “Many-shot jailbreaking”](https://www.anthropic.com/research/many-shot-jailbreaking)). Thus “more examples” can strengthen the wrong local pattern, and an authority block still needs adverse behavioral tests.

**Later check.** Give a fresh agent conflicting project evidence, a lower-trust instruction embedded in a read file, and a tempting completion shortcut. Observe whether it preserves the higher-authority invariant, cites the conflict, and stops only the affected action without over-refusing harmless work.

### G2 · A project update is an uncertain human-AI interaction, not only a file operation

**Primary-source observations.** Amershi et al. derived 18 specific, observable human-AI interaction guidelines and validated them through multiple rounds including 49 practitioners examining 20 products. Relevant mechanisms include showing capability and limits, presenting contextually relevant information, supporting correction and recovery, narrowing service when uncertain about user goals, explaining behavior, updating cautiously, conveying consequences, and notifying about changed capabilities ([Amershi et al., CHI 2019](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf)). The paper also reports limits: some guidelines were hard to observe in one session, the set may not cover every interface or high-risk domain, and apparently compatible guidelines can trade off.

**Transfer hypothesis.** The owner's interface should not be the execution trace. A compact project-level message can expose the applicable benefit, actual outcome, material exception, consequence of any requested choice, and next action, while citations keep technical detail inspectable. Correction and refusal are normal interaction outcomes, not embarrassing error branches.

**Boundary and counterevidence.** The study concerns AI-infused products broadly, not repository-updating text agents. A fluent explanation may still be false; progressive disclosure may hide a consequential change; and “ask less” may become unauthorized action. Comprehensibility therefore needs a task-based check—can the owner correctly state what changed, what remains unresolved, and what to do next?—rather than a readability judgment alone.

**Later check.** Compare full-checklist, final-summary, progressive-disclosure, and consequence-card interactions on the same scenarios. Score factual accuracy, material omission, unnecessary owner questions, and whether the owner can identify the actual next action from the visible message.

### G3 · Retry and recovery need semantic evidence; “idempotent” is not a prompt adjective

**Primary-source observations.** HTTP semantics distinguish safe methods from unsafe ones so a user agent can constrain automation and make users aware of unsafe actions. An idempotent method has the same intended effect when repeated, which permits automatic retry after uncertain communication failure; non-idempotent requests should not be retried unless semantics or observed state justify it. The standard explicitly notes that ancillary effects can still differ and gives revision inspection/recovery as an example ([RFC 9110 §§9.2.1–9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#name-common-method-properties)). Garcia-Molina and Salem's original Saga model decomposes long-lived work into transactions with compensating transactions after partial execution. Compensation is semantic repair, not necessarily restoration of the exact earlier state because other work may have occurred meanwhile ([Garcia-Molina & Salem, 1987](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf)).

**Transfer hypothesis.** Agent instructions can distinguish read-only discovery, intended-repeatable application, consequential non-repeatable actions, and semantic compensation. Before replay, the agent re-observes target state and proves whether the intended effect is already present. A checkpoint records what was observed and applied so another session resumes from evidence rather than rerunning prose from the top.

**Boundary and counterevidence.** Repository and project changes do not automatically inherit HTTP or database guarantees. A prompt cannot make an action atomic, and “rollback” may erase legitimate concurrent history. Some project decisions have no safe compensation. The analogy is useful only if each action's evidence, duplicate effect, and recovery boundary are stated; otherwise transaction vocabulary supplies false confidence.

**Later check.** Interrupt after each candidate state-changing step, vary whether the effect happened before interruption, and ask a fresh agent to resume. A safe design neither duplicates non-repeatable effects nor silently rewinds unrelated project history, and it reports when compensation is not authorized.

### G4 · Evidence must match the deployment context and the user claim

**Primary-source observations.** NIST's Generative AI Profile calls for empirically validated capability claims, verification of sources and citations, assessments by independent or context-representative actors, and performance or assurance criteria demonstrated under conditions similar to deployment. It warns that current pre-deployment tests may be unsystematic or mismatched to use, that prompt-engineering tests need not establish reliability, and that benchmark-to-real-world gaps are exacerbated by prompt sensitivity and heterogeneous contexts ([NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)). The AI RMF Core treats governance, context mapping, measurement, and management as iterative—not a checklist or necessarily ordered procedure—and requires explicit human-AI roles, system limits, oversight, benefits, costs, and context ([NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)).

**Transfer hypothesis.** Update assurance needs separate claim/evidence pairs: source payload coherence, applicability to this receiver, actual state change, project checks, agent behavior, and owner understanding. One green check cannot promote itself into all six claims. The user-facing message cites only evidence applicable to that project and labels the rest as unverified or irrelevant.

**Boundary and counterevidence.** NIST provides risk-management outcomes, not a ready-made prompt architecture; wholesale transplantation would create ceremony. Independent evaluation can also repeat the same blind spot, and an LLM judge is not automatically independent or correct. Evidence selection must remain proportional to the claim and consequence.

**Later check.** Seed cases where source integrity passes but receiver compatibility fails, where file application succeeds but project checks fail, and where a polished summary contradicts the trace. Verify that no candidate collapses these outcomes into “update complete.”

### G5 · Prompt topology is part of the experiment, but compactness alone is not reliability

**Primary-source observations.** Liu et al. found that long-context model performance changed significantly with the position of relevant information, often favoring the beginning or end and degrading when evidence sat in the middle—even for explicitly long-context models ([Liu et al., TACL 2024](https://aclanthology.org/2024.tacl-1.9/)). Anthropic's many-shot result supplies a different counterexample: repeated demonstrations can increasingly steer behavior, including toward an unwanted policy. Together these findings oppose both “the model can read it somewhere” and “examples are always safer than rules.”

**Transfer hypothesis.** Operational instructions should expose the immediate purpose, invariant, current state, allowed action, stop condition, and required evidence near the decision point, with detail linked rather than indiscriminately repeated. Important behavior should be tested under reordered, distractor-heavy, and partially conflicting context—not only with the canonical file order.

**Boundary and counterevidence.** Position effects were measured on retrieval and question-answering tasks, not this update workflow; they do not prove that putting every rule first solves reasoning. Over-compression can remove rationale needed to transfer a rule to a novel case. The design variable is accessible decision context, not token count by itself.

**Later check.** Hold semantics constant while varying placement, duplication, distractors, and example order. A promising instruction retains preservation, escalation, and reporting behavior across variants without becoming a wall of repeated warnings.

## OODA record and stage decisions

| Pass | Observe | Orient | Decide / Act |
|---|---|---|---|
| 1 | Instruction hierarchy, Constitutional AI, and HAI guidance | Explicit authority and observable interaction rules are plausible mechanisms, but source results include training and UI layers absent from a Markdown workflow | **GD1:** keep authority/conflict handling and owner interaction as separate dimensions; do not claim prompt enforcement |
| 2 | Many-shot jailbreaking and long-context position sensitivity | More context, examples, and prose can amplify a wrong pattern or bury the right one | **GD2:** evaluate instruction topology under adversarial reorder/distractors; reject document completeness as behavioral proof |
| 3 | HTTP semantics, Sagas, and NIST deployment-oriented TEVV | Recovery and assurance analogies add useful distinctions only when tied to observed state, semantic limits, and claim-specific evidence | **GD3:** compare replay/compensation models without calling the update atomic; **GD4:** separate source, receiver, project, behavior, and comprehension claims |

**H4 status after Gather:** still open, but testable. External mechanisms yield a configuration space broader than incremental wording repair. No combination has yet shown that it is simpler and complete; Extract must compose alternatives before the released baseline is consulted.

**Metacognitive check:** new information changed the initial framing. The strongest candidate is not “a clearer long prompt”; training evidence does not transfer automatically to inference-time files, more demonstrations can undermine higher-level intent, compensation is not exact rollback, and user-understanding rules can be unobservable in a single session. These limits make behavioral falsification and claim-specific evidence first-class dimensions.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Eight independent dimensions with at least three alternatives each | Compose coherent configurations rather than select row-by-row favorites |
| Five mechanism families grounded in primary sources | Produce short competing instruction/interaction specimens |
| Counterevidence against hierarchy-as-enforcement, long-context completeness, universal HAI guidance, atomic recovery, and benchmark sufficiency | Test configurations against authority, interruption, customization, refusal, and misleading-success cases |
| Four explicit Gather decisions and a falsifiable partial test of H4 | Only after independent designs exist, inspect the released TFW 2.2.0 behavior and determine applicability/cost |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] H4 tested at this stage without premature acceptance?
- [x] Counter-evidence actively sought?
- [x] At least two stage decisions recorded?
- [x] Metacognitive check completed?

Stage complete: YES
→ User decision: Pending Main Coordinator; Researcher recommends closing Gather and proceeding to Extract.
