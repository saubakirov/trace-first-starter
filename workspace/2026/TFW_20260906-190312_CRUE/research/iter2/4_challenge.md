# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. Attack every configuration; retain only mechanisms whose authority, evidence, and user effect remain inspectable.
> **Test:** "Would the survivors hold under a different agent, partial execution, hidden material effects, and a source that contradicts itself?"
> Parent: [HL-TFW_20260906-190312_CRUE](../../HL-TFW_20260906-190312_CRUE.md)
> Goal: TFW releases reach existing projects as coherent, safe, and understandable improvements that agents can apply from shipped instructions while owners retain project purpose and consequential choices.

## Evidence boundary

- **Baseline observations** below come only from Git object `v2.2.0` / `8e68ab37d300122ff110500ad58f354f76b6210f`, read with `git show`, `git grep`, and `git ls-tree`. They do not attribute later master behavior to the release.
- **External observations** are attributed to primary research or the publishing model developer.
- **Walkthrough results** are analytical applications of C1–C4 to declared cases. No fresh agent-run, owner-comprehension study, or comparative performance measurement was performed.
- **Verdicts** are research decisions about design consistency. They do not authorize product changes, settle an HL amendment, or prove the future behavior of any model/provider.

## Consistency Check

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1 · Authority | Flat prose with contextual interpretation | D2 · Ambiguity | Act inside a declared envelope | The envelope has no explicit authority boundary to interpret or audit |
| D1 · Authority | Flat prose with contextual interpretation | D8 · Evaluation | Text/lint conformance | Text presence cannot show which conflicting instruction the agent followed |
| D2 · Ambiguity | Ask all configuration questions before action | D6 · Owner interaction | Consequence cards only at material choices | It spends owner attention before materiality is known and repeats already settled choices |
| D2 · Ambiguity | Act inside a declared envelope | D5 · Evidence | Agent self-report | The agent cannot establish that the envelope applied using its own assertion alone |
| D3 · Instruction shape | One narrative procedure | D4 · Recovery | Checkpoints with semantic compensation | Recovery state and compensation boundary cannot be reliably recovered from an undifferentiated narrative |
| D4 · Recovery | Linear best effort | D5 · Evidence | Pre/post observation plus named check | An interrupted linear run supplies no rule for using those observations to resume safely |
| D4 · Recovery | Semantic compensation | D1 · Authority | Flat prose with contextual interpretation | Compensation may change or erase project meaning; it requires explicit authority/effect classification |
| D5 · Evidence | Agent self-report | D7 · Benefit/limit | Applicable benefit plus receiver evidence | A self-report is not receiver evidence, so the stated benefit cannot be qualified as applied |
| D6 · Owner interaction | End-only summary | D2 · Ambiguity | Stop on material unresolved consequence | A necessary pre-action decision cannot be postponed until the end |
| D7 · Benefit/limit | Changelog inventory | D6 · Owner interaction | Project outcome first | Release possibility and actual receiver outcome are different claims |
| D8 · Evaluation | One-model happy path | D1/D2 behavior | Reliable authority and decision handling | One favorable trajectory cannot support a reliability claim for probabilistic agents |
| D8 · Evaluation | Text/lint conformance | D4/D5 behavior | Safe recovery and truthful evidence | Static text checks neither environment state nor the action trajectory |

### Surviving configurations

| Config | Authority mechanism | Action/recovery mechanism | Owner/evidence mechanism | Notes |
|--------|---------------------|---------------------------|--------------------------|-------|
| C1 · Constitutional Interpreter | Small invariants, defaults, materiality rubric, contrastive boundary examples | Re-observe under the “no unsupported completion” invariant | Consequence question only when evidence cannot settle project meaning | Survives as a specification layer; not a complete update mechanism by itself |
| C4-R · Revised Local Decision Tuple | C1 invariants/defaults bound every tuple | One semantic effect per tuple; re-observe before retry; mandatory integrity envelope remains outside discretionary grouping | Existing authoritative evidence is referenced; material results go to one existing task-local update trace; final message uses outcome claims | Survives as the primary prompt-native configuration, conditional on defining the existing trace carrier and behavioral verification |

### Eliminated as standalone configurations

- **C2 Evidence-Gated Protocol:** eliminated as the controlling architecture. The released workflow already has pin, route, gate, classify, apply, adapter/vocabulary, and verify/brief/clean stages. Adding a second explicit state machine raises reading and synchronization cost, can turn observed evidence into ceremonial labels, and does not solve materiality or owner communication. Its re-observation, source-before-project, and trajectory/outcome checks survive as constraints inside C4-R.
- **C3 Outcome-Backward Case:** eliminated as the controlling architecture. Work defined only by four user-visible claims can omit integrity work that the claims do not mention and can reward a persuasive story. Its `benefit / outcome / limitation / next` interface survives strictly downstream of the mandatory integrity envelope.

### Unexpected survivor

- **C4-R:** the smallest configuration survived, but only after losing its most aggressive simplification. A grouped ACTION is allowed solely when every included effect has the same authority source, project owner, reversibility class, proof, and outcome meaning. Any difference splits the group into one tuple per effect. Minimality therefore means a small repeated decision grammar, not fewer distinctions.

## Findings

### C1 · Released 2.2.0 already contains useful mechanisms, but they do not form a coherent agent/user contract

**Baseline observations.** At the immutable release commit, the [update workflow](../../../../../.tfw/workflows/update.md) already pins an operator-named Git object, follows the target's update algorithm, routes migrations, classifies local files against provenance, preserves config/state, gates adapter and vocabulary consistency, verifies receiver commands, and renders a final briefing. This is real structure worth retaining; none of C1–C4 justifies replacing it with a new installer or runtime.

The same snapshot exposes incompatible interaction contracts:

1. Step 2 always asks exactly three owner questions before any project write, including values that may already have authoritative answers in `team/` or project config.
2. Step 3 requires owner approval of an exact per-file checkbox list, so mechanical topology and consequential project meaning share one approval surface.
3. The [briefing template](../../../../../.tfw/templates/briefing.md) permits only four CHANGELOG-derived blocks and no free text, while the [2.2.0 migration](../../../../../.tfw/migrations/2.2.0.md) requires actual receiver setting changes, preserved values, verified outcome, and historical non-rewrite to appear in that briefing.
4. The [adapter manifest](../../../../../.tfw/adapters/manifest.yaml) declares Antigravity targets under plural `.agents/`, while `git ls-tree` at the same commit shows shipped Antigravity-style rules/workflows under singular `.agent/` and Codex skills under `.agents/`. The update's parity instruction does not resolve which installed state is authoritative.
5. `git grep` at the release commit finds the retired sentence “A writer is not named yet” in handoff, research, and review workflows although the update requires zero unexplained retired-term hits.
6. The historical Git blob `8e68ab37d300122ff110500ad58f354f76b6210f:.tfw/scripts/test_gen_index.py` (resolve with `git show`; intentionally absent from the current checkout) contains `test_the_repository_stateless_phases_are_all_informational`, which invokes `PROJECT_ROOT` and asserts six named starter tasks. It is evidence about this repository corpus, not a receiver-project capability gate.

**Analytical inference.** The baseline does not need a parallel procedure. It needs one prompt-native decision contract that tells the agent which existing mechanisms are mandatory integrity work, which facts can be discovered/reused, which effects require owner authority, what evidence controls retry/completion, and what the owner must learn. C4-R can be a reframing of the current algorithm rather than a new execution system.

**Limitation.** These observations prove contradictions and carrier gaps in the released text, not how frequently agents fail or how much a redesign improves behavior.

### C2 · File collision is evidence to classify, not an automatic owner question

The earlier C1–C4 S2 walkthrough was too eager: each version treated project-specific text inside a framework-targeted file as sufficient reason to ask. That confuses location with authority.

**Task authority.** The approved HL settles that current TFW methodology is framework-owned and travels in `.tfw/README.md`; it also requires legacy project-specific additions and actual project-purpose authority to survive. Therefore the agent must not re-ask whether to adopt TFW values. The remaining question is whether preserving existing project meaning is already determined by evidence and the authorized migration mechanism.

**Revised decision rubric.** For each semantic effect, in this order:

1. **Observe authority:** Is the meaning owned by the framework, a project artifact, an established owner decision, or genuinely unresolved?
2. **Observe consequence:** Does the update merely relocate/preserve established meaning, or does it choose, discard, merge, reprioritize, or reinterpret it?
3. **Check mandate:** Does the approved update design already define a meaning-preserving transition for this observed state?
4. **Act or ask:** If authoritative evidence and the approved transition settle the same meaning, proceed and report preservation. Ask only when competing authorities, ambiguous designation, irreversible loss, or a genuinely new project behavior remains.

**Short contrasting interactions.** Comparative specimens only:

```text
NO OWNER CHOICE
“TFW's current methodology moves into its framework-owned guide. Your existing
project-purpose section remains authoritative at <existing approved location>;
its text and role are preserved. No project decision is changed.”

OWNER CHOICE REQUIRED
“Two current files both declare themselves the project's purpose and prescribe
different priorities. The update cannot preserve both as sole authority.
I recommend <A> because <evidence>; choosing it makes <consequence>.
Alternative <B> keeps <tradeoff>. Which authority should govern?”
```

**Baseline application.** Released 2.2.0 preserves `.tfw/README.md` byte-for-byte and always asks the three technical gate questions. The approved future policy changes README ownership, so it must define the meaning-preserving transition once. After that, a collision with recognizable project additions is a migration case, not recurring owner acceptance. A genuinely ambiguous project-purpose designation remains a material choice.

**External counterevidence.** Interviews with 17 experienced developers found a priori controls, co-planning, monitoring, and post-hoc review, but also “efficient, not perfect” oversight and substantial review difficulty. Participants varied from elaborate pre-configuration to reliance on defaults; instructions did not make behavior certain ([Dhanorkar, Passi & Vorvoreanu, FAccT 2026](https://arxiv.org/abs/2606.05391)). This small, mostly single-company qualitative study is not evidence for TFW users, but it challenges the assumption that more owner gates equal effective oversight. Owner attention should attach to the semantic consequence the agent cannot settle, not to every observable file difference.

### C3 · C3 may shape communication but cannot choose the integrity workload

**Attack.** The C3 instruction “perform only the work needed to make four claims true” is circular. An agent can make a smaller or vaguer claim set, skip an invisible safety operation, then produce a truthful but incomplete message.

**Baseline counterexamples.** Several released requirements are necessary even when absent from the four final claims:

- verifying the immutable source and route before trusting `VERSION`;
- executing all applicable intervening migrations;
- preserving state/config/customization exclusions;
- synchronizing adapter topology and checking second-run drift;
- scanning retired vocabulary across payload and installed adapters;
- separating receiver-project checks from framework/repository checks;
- preserving recovery evidence and cleaning temporary material only when safe.

The manifest/root mismatch, live retired wording, and starter-specific repository test demonstrate why invisible integrity work cannot be inferred backward from a polished final summary.

**Revision.** C3 becomes an output projection after integrity work, never its scope authority:

```text
1. Complete or explicitly fail the mandatory integrity envelope.
2. From its evidence, render BENEFIT / OUTCOME / LIMITATION / NEXT.
3. Never omit an integrity failure because it lacks a friendly user-facing benefit.
4. Keep technical proof inspectable; expose only material consequences in the main message.
```

**External counterevidence.** Human-AI research reports that explanations can have mixed effects and sometimes increase overreliance; realistic decision support involves tensions between actionability and cognitive engagement rather than a universal “more explanation” benefit ([Reicherts et al., CHI 2025](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/03/AI-Help-Me-Think-CHI-2025.pdf)). Therefore the four claims are an information contract to test, not proof that the owner understood or should trust the update.

**Verdict.** C3 standalone is rejected. Its communication projection is retained because it addresses the baseline briefing contradiction without allowing the message to define away technical obligations.

### C4 · C4 must split semantic effects before it can group actions

**Attack.** “One tuple can group settled, meaning-preserving actions” is unsafe if a mechanical-looking file operation contains several semantic effects. A grouped copy could update framework rules, overwrite a project purpose statement, relocate history, and change a default while reporting one benign ACTION.

**Revision to C4-R.** The unit is the semantic effect, not the file and not the shell action:

```text
Split before deciding. Effects may share one tuple only when all five match:
AUTHORITY SOURCE · PROJECT OWNER · REVERSIBILITY · PROOF · OUTCOME MEANING.
If any differs, use separate tuples and expose every material effect.

OBSERVED -> AUTHORIZED -> EFFECT -> ACTION -> PROOF -> MESSAGE
```

Applied to S2, installing current TFW methodology and preserving legacy project purpose are separate effects even if one file edit performs both. The framework-owned effect does not need renewed values acceptance; the project-owned effect follows the approved preservation route or stops if its authority/meaning is unresolved.

Applied to S3, a prior file write does not prove all of its semantic effects. Each effect is re-observed against its proof before replay. “Already applied” is effect-specific.

**Carrier challenge.** Extract assumed an “existing update record.” The 2.2.0 snapshot mentions an update checklist repeatedly but does not name a canonical durable location or form for it. C4-R therefore cannot claim zero carrier design. The simplest sufficient requirement is one authoritative task-local update trace using the project's existing task/trace system, with the location and archive boundary defined once. That is not a second project-state registry; it is the durable result of this update. Selecting the exact carrier belongs to planning, and until selected this is a dependency, not a hidden assumption.

**Cost.** C4-R's instruction kernel is smaller than a second stage machine, but the total coherent change is not small: current workflow, migration, final briefing, adapter authority, verification routing, legacy ownership transition, and behavioral evidence must agree. Reading cost should fall for ordinary cases because settled facts do not become questions or owner-facing checklist rows; this is an inference, not a measurement. Maintenance cost concentrates in one semantic-effect rule, a few contrastive cases, one trace carrier, and scenario tests rather than duplicated claim/state registries.

### C5 · External evaluation attack: a plausible walkthrough is not a behavioral result

**Primary-source observations.** Anthropic distinguishes an agent's trajectory from its actual environment outcome, recommends multiple trials because behavior varies, and warns that graders have different weaknesses. Its guidance explicitly says evaluation concerns model plus harness; exact checks are brittle, model graders need human calibration, and shared state can make trials correlated ([Anthropic, “Demystifying evals for AI agents”](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)). OpenAI similarly presents rubrics and small contrastive examples as interpretive aids, not a mechanical rule or complete implementation, and pairs them with broader scenario suites ([OpenAI, “Inside our approach to the Model Spec”](https://openai.com/index/our-approach-to-the-model-spec/)).

**Implication for survivors.** C1 and C4-R survive logical consistency, not empirical evaluation. A later authorized evaluation must isolate receiver fixtures and inspect both trajectory and outcome across at least:

- established answer present / missing / conflicting;
- legacy purpose clearly relocatable / ambiguously authoritative;
- interruption before write / after write / after verification;
- mixed grouped actions containing one differently owned effect;
- source defect before application and receiver-only failure after application;
- reordered instructions, distracting local prose, and lower-trust prompt injection;
- repeated trials across declared agent/harness combinations;
- owner comprehension of benefit, actual completion, limitation, and next action.

No exact trial count or provider-wide reliability threshold is proposed here; those are experiment-design and budget decisions. A static lint can protect carrier consistency, but it cannot substitute for these behavioral claims.

### C6 · Survivor and rejection ledger

| Config | Challenge verdict | Retained mechanism | Rejected mechanism | Cost / dependency |
|---|---|---|---|---|
| C1 | **SURVIVES AS LAYER** | Invariants, defaults, materiality rubric, few contrastive examples | Treating written principles as enforcement or complete update logic | Low-to-medium read cost; requires scenario evaluation and synchronization with actual algorithm |
| C2 | **REJECT STANDALONE** | Source-before-project, re-observe before replay, trajectory + outcome evidence | A second full state machine and fine-grained gate vocabulary | Highest reading/maintenance pressure; duplicates baseline stages and can recreate checklist ritual |
| C3 | **REJECT STANDALONE; RETAIN OUTPUT PROJECTION** | Benefit / outcome / limitation / next after integrity work | Letting user-visible claims define technical scope | Low owner read cost; medium risk of persuasion/duplication; comprehension needs testing |
| C4-R | **CONDITIONAL SURVIVOR** | One semantic effect per tuple, existing evidence references, effect-specific replay, material result trace | Grouping heterogeneous effects or leaving tuples only in hidden reasoning | Small instruction kernel; depends on one defined task-local carrier, legacy migration semantics, and behavioral proof |

### C7 · Limited H4 verdict

**H4 verdict: PROVISIONALLY SUPPORTED AT DESIGN LEVEL; NOT EMPIRICALLY VERIFIED.** The independent reframing produced a simpler coherent candidate than either incremental defect patching or a second evidence state machine:

1. **C1 specification layer:** a few non-negotiable invariants, established defaults, a consequence/materiality rubric, and scarce contrastive examples.
2. **C4-R local mechanism:** one semantic effect per `OBSERVED → AUTHORIZED → EFFECT → ACTION → PROOF → MESSAGE` tuple; ordinary settled effects can be processed without owner interruption, but heterogeneous effects cannot be hidden in one action.
3. **Mandatory integrity envelope:** immutable source, migration applicability, ownership preservation, adapter/vocabulary coherence, receiver verification, and recovery remain required even when not visible in the user message.
4. **C3 output projection:** `benefit / actual outcome / material limitation / next action` communicates the project result after the integrity envelope, with technical evidence referenced rather than copied into a new registry.

This is simpler in conceptual control structure: one authority layer, one repeated decision grammar, one existing task-local durable result, and one owner-facing projection. It does not imply fewer repository files, a smaller implementation diff, deterministic compliance, or proven owner comprehension. Incremental repairs to the known defects are still required inside the coherent delivery, but they no longer define its architecture.

If planning cannot define (a) a meaning-preserving legacy-purpose transition, (b) one authoritative existing trace carrier, or (c) scenario evidence that weak/different agents split material effects and avoid unsupported completion, the limited H4 support fails and the honest result becomes “no verified simpler alternative.”

## OODA record and decisions

| Pass | Observe | Orient | Decide / Act |
|---|---|---|---|
| 1 | Immutable 2.2.0 workflow, migration, briefing, manifest, and targeted test/source scans | Baseline already has strong stages; contradictions concern authority, carrier agreement, and user outcome rather than absence of procedure | **CD1:** reject C2 as a duplicate controlling architecture; **CD2:** make the integrity envelope non-discretionary |
| 2 | Owner-choice and grouped-action attacks | File/path collisions do not equal new project decisions; a single write can contain differently owned semantic effects | **CD3:** ask only on unresolved meaning/authority; **CD4:** revise C4 to one semantic effect per tuple and split on five attributes |
| 3 | FAccT oversight study, agent-eval practice, Model Spec limits, and HAI reliance counterevidence | More human review and clearer prose do not guarantee effective oversight; logical walkthroughs do not prove agent or user behavior | **CD5:** retain C1 + C4-R conditionally, demote C3 to output projection, and issue only a design-level H4 verdict |

**Metacognitive check:** Challenge overturned two Extract assumptions. First, an ownership collision does not automatically require an owner question; established authority plus a meaning-preserving migration can settle it. Second, the smallest tuple cannot safely group actions by convenience: its unit must be one semantic effect. It also exposed that 2.2.0 has no clearly named durable checklist carrier, so “reuse the existing record” is a planning dependency rather than a fact.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1 survives as a specification layer and C4-R as a conditional primary mechanism | Synthesis must state the carrier and legacy-transition dependencies without inventing their implementation |
| C2 and C3 rejected as standalone architectures; useful evidence/recovery and communication components retained | Coordinator must decide how the findings affect free HL sections and whether any frozen claim needs an amendment proposal |
| Owner-choice rubric distinguishes established meaning from genuinely unresolved authority | Later TS/evaluation must define scenario fixtures and evidence thresholds under separate authorization |
| H4 provisionally supported only at design level | No fresh agent or owner-comprehension evidence exists; no reliability improvement may be claimed |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked and survivors listed?
- [x] H4 tested with a limited verdict?
- [x] Counter-evidence and analogy limits preserved?
- [x] Released behavior read only from `v2.2.0` / `8e68ab37d300122ff110500ad58f354f76b6210f`?
- [x] Walkthrough distinguished from empirical agent behavior?
- [x] At least two stage decisions recorded?
- [x] Metacognitive check completed?

Stage complete: YES
→ User decision: Pending Main Coordinator; Researcher recommends closing Challenge and authorizing RES synthesis.
