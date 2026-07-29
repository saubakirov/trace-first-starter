# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-48](../../HL-TFW-48__value_first_methodology_rebaseline.md)
> Goal: Re-derive TFW from its product purpose and production learning so that its compact method kernel preserves meaning, evidence, independent judgment, and portable knowledge across domains.

## Dimensions

No alternative is selected here. The dimensions deliberately separate concerns that the
current method sometimes combines.

| Dimension | Alternatives still open |
|-----------|-------------------------|
| Rule locality | Full rule repeated at every use; canonical definition plus a short point-of-use check; canonical definition plus a structural artifact/evidence gate; reference only; locality selected by rule criticality |
| Rule authority | Non-overridable invariant; hard gate with named exception authority; configurable project constraint; advisory heuristic; historical metric retained only as evidence; remove |
| Limit semantics | Product/risk boundary; attention budget; workflow stop signal; escalation trigger; sampling default; formatting target; descriptive measurement |
| Evidence authority | Author report/checkmark; artifact existence; independent inspection; executable reproduction; real environment/business flow; stakeholder observation |
| Reviewer authority | TS/RF conformance only; artifact-and-evidence conformance; north-star and cited-source defense; independent reality check; stakeholder-only value judgment |
| Learning route | Capture in every template; periodic central consolidation; event-triggered select→verify→promote/reject; local memory as discovery index; owner-of-truth plus linked derived views; explicit pruning/retirement |
| Research guidance | Neutral task; strategy name only; operational strategy steps; progressively loaded strategy; task-specific generated strategy; fixed technique catalog |
| Research intensity | One uniform workflow; configurable loop count; evidence-risk-based intensity; escalation after contradiction; stage-specific intensity |
| Project adaptation | Edit upstream core; configuration only; registered project extension layer; adapter-owned extension; repository fork |
| Value continuity | Deliver architecture first; require a thin visible value slice in every phase; allow enabling work with explicit value-debt ledger; group coupled phases under one review; defer value to a later release |

## Corpus and Method

The read-only corpus covers the current TFW framework and coordinator-approved anchors
in Atamat, Helpdesk, and AFD. Twenty coordinator-named project anchors were inspected,
with the named non-secret Helpdesk and AFD memory companions used only for discovery.
This exceeds the configured soft default of 15 project files for one stage. The reason is
recorded rather than hidden: the approved longitudinal design spans three projects, four
hypotheses, and six lifecycle boundaries. No excluded or sensitive memory file was
opened.

The evidence ladder used during Gather was:

1. observed execution or real-environment evidence;
2. independent review with source inspection;
3. implementation, test, or tracked artifact;
4. RF/TS/HL claim;
5. personal memory, used only to locate a claim that then required repository
   corroboration.

Production cases are not treated as controlled experiments. They can falsify a universal
claim, show a recurring failure mechanism, or motivate a comparison; they cannot by
themselves isolate a prompt treatment effect.

## Findings

### Cross-project incident map

| Boundary | Evidence observed | Mechanism exposed | Hypotheses informed |
|----------|-------------------|-------------------|----------------------|
| Instruction→execution | Atamat TFW-2.100 used a 376-line `AGENT_WORKFLOW.md` and parallel system prompt with repeated completion checks, yet the adversarial RF found a 507-line file, ignored frontend scope, and downgraded “100% complete” to about 70–75%. | Repetition and procedural volume did not guarantee truthful coverage; independent inspection changed the result. | H1, H2, H4 |
| Limit→behavior | Atamat TFW-14 Phase A exceeded a nominal 400-line source budget at 513 physical lines, then passed after reclassification to about 265 “functional” lines. | A useful pressure signal became negotiable through classification; the protected failure and counting rule were not the same thing. | H2 |
| Finding→knowledge | Atamat TFW-11 B1 extracted 15 decisions, 15 principles, and 12 legacy items; B2 repaired links while keeping an index-not-duplicate structure. | Selection, canonical ownership, and links can preserve knowledge without copying the whole source. | H1, H3 |
| TS→execution | Helpdesk HD-25’s TS contained a wrong i18n path. The implementation corrected it, but TS-required RTL/upload integration tests were absent despite RF checkmarks. | Literal conformance and author checkmarks were weaker than source inspection plus evidence verification. | H1, H2 |
| Research→plan | Helpdesk HD-28 iteration 1 consisted of empty stage templates but still counted as an iteration. Iteration 2 inspected the database, falsified the assumed `system_settings` table, and found `equipment_instances` unused. | Counted workflow progress was not research progress; point-of-use reality checks repaired the model. | H1, H2 |
| TS→database reality | Helpdesk HD-26 Phase A specified an impossible PostgreSQL enum-value removal. A live run forced a type-swap migration; a partial acceptance item and deferred test were still initially represented as complete. | The environment, not the document, was authoritative; a binary checklist concealed partial evidence. | H1, H2 |
| Test→runtime reality | Helpdesk HD-26 Phase C found a SQLAlchemy bulk-update state bug with a real PostgreSQL smoke test after mocked unit tests stayed green. | A structurally plausible mock tested the wrong truth boundary. | H1, H2 |
| Phase→adjacent phase | Helpdesk HD-30 had locally correct frontend and backend phases, but repeated query parameters met a scalar backend contract and silently broke multi-select. | Per-phase review missed an adjacent protocol boundary; cross-layer replay found it. | H1, H2 |
| Purpose→phase value | Helpdesk HD-23 defined a mobile outcome (“find, understand, do” within two taps) but Phase A delivered architecture/infrastructure and explicitly deferred visible value. | Phase decomposition can preserve local completion while delaying the product reason for the work. | H2 |
| TS/RF→north star | AFD-38 Phase B first passed because code, TS, RF, and tests agreed. The verdict was retracted when the result violated the single-registry principle and falsely deferred device diagnosis. | An independent reviewer needs authority beyond document conformance. | H1, H4 |
| Cited source→implementation | AFD-10 Phase A0 initially passed its TS; later inspection of the cited Helpdesk source exposed omitted Alembic infrastructure. | A reference is useful only if the consumer verifies the relevant source contract. | H1 |
| Command→claimed evidence | AFD-36 Phase C required six clean aggregate attempts. Five failed environmentally; the successful run reported 1302 XML tests, not the RF’s 1318. A prior stale-XML/exit-127 episode had also reversed an approval. | “Command named” and “command actually succeeded from a clean state” are different evidence states. | H1, H2 |
| Synthetic→honest flow | AFD-14’s honest-fleet ledgers forbade seeders/fakes and exercised live lifecycle chains; honest operation exposed failures synthetic setup had hidden. | The decisive gate must cross the business truth boundary, not merely produce test data. | H1, H2 |
| Literal copy→drift | AFD-34 T1a traced drift to literal facts copied into two or more files without an owner-of-truth link; a values-only repair re-drifted in five days. | Duplication increases update surfaces unless ownership and derivation are explicit. | H1, H3 |
| Memory→repository knowledge | AFD-34 T1b classified 52 memory files with four routes: liberate, merge/extend, split, or remain local. It handled 235 facts with token-index dedup and prioritized retirement of high-risk material. | More destinations were not the missing mechanism; routing, deduplication, verification, and retirement were. | H3 |

The four safe Helpdesk memory notes were corroborated by project traces: source-blind TS
precision errors, omission of tests when the TS omitted them, literal copying from
code-heavy specifications, and fragmentation that delivered plumbing while losing a
chat-style product experience. The four safe AFD notes were also corroborated:
principle-defending review, cited-source verification, clean aggregate execution, and
honest-fleet gates. Several of these lessons have reached repository knowledge, but the
promotion is selective rather than automatic.

### H1 — Canonical rule plus point-of-use enforcement

**Supporting observations**

- TFW-2.100 is counter-evidence to “more repeated instruction always produces better
  compliance.” Repeated completion language coexisted with false completeness.
- TFW-11 and AFD-34 show that a canonical owner plus links can preserve meaning while
  reducing literal copies and drift surfaces.
- HD-26, AFD-10, AFD-36, and AFD-14 show that a short check can be effective when it
  names an observable boundary: live PostgreSQL, cited migration source, clean aggregate
  run, or honest fleet.
- [Lost in the Middle](https://arxiv.org/abs/2307.03172) found that long-context model
  performance can degrade with the position of relevant information. This supports
  point-of-use resurfacing rather than assuming that a canonical rule somewhere in a
  large context is operationally available.

**Counter-evidence and unresolved questions**

- A reference-only design is not supported. AFD-10 had a cited source, yet the critical
  infrastructure was missed because the source was not checked.
- Canonical ownership is insufficient when links are broken, the consumer does not load
  the owner, or the point check is only a self-reported checkbox.
- [ReasonIF](https://aclanthology.org/2026.findings-acl.1456/) reports instruction
  adherence below 0.25 for the best tested open reasoning model and worsening adherence
  with task difficulty. Its tasks and models differ from this corpus, but it is strong
  counter-evidence to assuming that either canonical text or inline text guarantees
  compliance.

**Gather status:** Supported only in the stronger form “canonical owner + localized,
observable enforcement.” The evidence rejects both universal full repetition and
reference-only minimalism. It does not yet identify which critical rules still require
inline restatement for weaker models.

### H2 — Fixed limits and proxy optimization

The current framework mixes qualitatively different numbers:

| Class | Examples observed | Open interpretation |
|-------|-------------------|---------------------|
| Safety or semantic invariant | At most three blocking questions; minimum two independent sources for promoted facts | A hard number may encode coordination safety or corroboration, not productivity |
| Escalation threshold | Review sampling ratio 0.42, escalating to 100% on discrepancy | The number triggers more inspection rather than defining success |
| Attention/scope budget | 14 files, 8 new files, 1200 LOC, 12 modified files; 1200-word workflow ceiling; 35-line adapter target | Useful early warning, but may invite reclassification or fragmentation |
| Research sampling default | 5 web queries and 15 project files per stage; up to 3 loops/passes | A cost/attention control that needs justified override, as this stage demonstrates |
| Knowledge storage shape | 200 index lines, 30 index facts, 50 facts/topic, 8 topics, interval 5 | A retrieval/maintenance heuristic whose protected failure must be tested |
| Historical measurement | Physical versus “functional” LOC; iteration count; test-count totals | Descriptive numbers become harmful when treated as completion evidence |

**Supporting observations**

- Atamat’s line-budget reclassification, HD-28’s empty counted iteration, and AFD-36’s
  discrepant test total show direct proxy risks.
- Helpdesk knowledge itself records a tension: file-count budgets are poor quality
  metrics, while cognitive-size budgets can still be useful split signals.
- HD-23 and the Helpdesk fragmentation memory show the inverse failure: pressure to
  create manageable phases can sever a coherent value slice.
- The 15-file soft limit was exceeded here for a declared reason. Treating it as a hard
  success criterion would have forced either silent omission or artificial stage
  fragmentation.
- [Strict Output Length Constraint](https://aclanthology.org/2025.emnlp-main.389/)
  evaluated 30 models across multiple budgets and found that the best model or prompt
  style changes with the budget. A limit can be operationally necessary, but its effect
  is context-dependent rather than universally quality-improving.

**Counter-evidence and unresolved questions**

- Removing all numbers is contradicted by real coordination, latency, attention, and
  escalation needs. The evidence challenges untyped limits, not measurement itself.
- No causal comparison in this corpus isolates whether a particular TFW limit caused a
  failure; several incidents show gaming or misleading interpretation after the fact.

**Gather status:** Strong support for classifying each number by protected failure,
authority, owner, measurement rule, and override semantics. Only partial support for
removing any particular limit before Challenge replays it.

### H3 — Capture locations versus routing quality

**Supporting observations**

- TFW already offers stage traces, RES, RF/review evidence, Fact Candidates, root
  knowledge, topic files, technical debt, and project-local memory/discovery sources.
- AFD-34 found 52 memory files and 235 facts; its difficulty was choosing among four
  routes, deduplicating, linking to an owner, and retiring risky material.
- Atamat TFW-11 demonstrated successful select→classify→link behavior without copying
  every source into the index.
- Helpdesk and AFD both contain lessons that were discovered in personal memory,
  corroborated in task traces, and sometimes promoted into repository knowledge. The
  uneven promotion shows a routing/verification problem, not absence of a destination.

**Counter-evidence and unresolved questions**

- A “destination exists” does not prove it is easy to discover, has a clear owner, or
  accepts every domain-specific learning type.
- Some lessons remain only in personal memory or task reviews. Gather has not yet
  distinguished justified local retention from missed promotion.
- The current Fact Candidate path may be available but too delayed or manual; that is a
  usability failure that can resemble a missing capture location.

**Gather status:** Strong production support for H3’s dominant-failure claim, with the
qualification that discoverability and ownership of existing destinations must be
tested before declaring the capture topology sufficient.

### H4 — Operational cognitive strategy versus name or length

**Production observations**

- Principle-defending review, cited-source inspection, clean-run verification, honest
  fleet operation, and database reality checks repeatedly changed outcomes. These are
  operational behaviors, not technique names.
- TFW-2.100 shows that adding procedural volume alone can coexist with shallow or false
  completion.
- These cases are history-bearing and task-mismatched. They support plausibility but do
  not establish that a strategy prompt caused the better result.

**External evidence**

- [Metacognitive Prompting](https://aclanthology.org/2024.naacl-long.106/) compared a
  structured self-evaluation strategy with other prompting approaches across four
  models and ten NLU datasets, reporting broader gains than name-only priming would
  explain.
- [Strategy-Induct](https://aclanthology.org/2026.findings-acl.23/) generates explicit
  task-level reasoning strategies from example questions and reports gains across
  multiple tasks and model scales.
- [Instruction Optimization for Tabular Fact Verification](https://aclanthology.org/2026.findings-eacl.161/)
  compared prompting techniques, three optimizers, four benchmarks, and three model
  families. Optimization improved accuracy, but the best optimizer differed between
  CoT and ReAct and with model scale. This supports matching operational guidance to
  task/method rather than declaring one named strategy universal.
- ReasonIF supplies the opposing signal: instruction presence may still have low
  adherence, especially as difficulty rises.

**Required controlled comparison**

The predeclared minimum trial remains:

1. identical task pack and source snapshot;
2. neutral base, strategy-name-only, operational strategy, and length-matched neutral
   conditions;
3. recorded model, surface, date, full prompt, context, and treatment;
4. more than one inquiry family and more than one model profile;
5. a rubric declared before outputs and scored independently/blinded where practical;
6. measures for source coverage, counter-evidence, traceability, unsupported claims,
   decision quality, and cost/length.

Fresh isolated Codex tasks or neutral forks are needed to prevent treatment leakage.
This Researcher has no user authorization to create or fork user-owned tasks. Existing
history-bearing tasks therefore remain observational evidence only.

**Gather status:** Externally and observationally supported, but not causally established
for TFW inquiry work. H4 remains open pending an authorized isolated trial or an
explicitly narrower iteration claim.

## Gather Decisions

These are evidence-handling decisions for the next stage, not final method
recommendations.

1. **G-D1:** Replace the binary “repeat versus reference” framing with a three-part
   mechanism: semantic owner, point-of-use cue, and observable enforcement boundary.
   Extract must keep reference-only and full-repetition counterexamples available.
2. **G-D2:** Treat every numeric constraint as typed data. Extract must record the
   protected failure, authority, owner, measurement rule, escalation/override behavior,
   and observed proxy risk before judging retention.
3. **G-D3:** Model learning as a routed state transition—captured, selected, verified,
   promoted, rejected, linked/derived, or retired—rather than count destinations.
4. **G-D4:** Do not use production anecdotes or external prompt studies as causal proof
   of H4. Carry a controlled-comparison design and a visible authorization dependency.

## Metacognitive Check

- **What changed the search?** The first loop focused on repeated instructions and
  numeric limits. Cross-project cases shifted the search toward authority and evidence
  topology: several failures occurred despite correct-looking documents, tests, or
  checkmarks.
- **What could be selection bias?** The coordinator supplied known failure-rich anchors.
  Successful routine cases are underrepresented, so Gather can identify failure
  mechanisms more reliably than their base rates.
- **What is being conflated?** Physical size, cognitive load, scope, latency, and value
  are different variables; “more instruction” and “more operational guidance” are also
  different treatments.
- **What evidence would reverse the provisional direction?** Repeated failures caused
  specifically by missing inline restatement despite a loaded canonical owner and an
  observable gate; a fixed limit whose removal reproducibly causes the protected
  failure; a knowledge loss caused by no valid destination; or a length-matched neutral
  condition matching the operational-strategy condition.
- **What remains unknowable from this corpus?** Causal effect sizes, model-era
  generalization, and the prevalence of each failure mechanism.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H1 is supported only as canonical ownership plus localized observable enforcement, not reference-only minimalism. | Identify rule classes that still require inline restatement and test them against weaker-model failure cases. |
| H2 has direct proxy-risk examples and a typed inventory of limit purposes. | Replay candidate removals/changes; distinguish useful pressure from success metrics. |
| H3 has strong routing/dedup/promotion evidence across Atamat and AFD, with selective promotion visible in Helpdesk and AFD. | Test discoverability, ownership, local-retention reasons, and pruning behavior. |
| H4 has multi-study external support and operational production analogues. | Obtain authorization for fresh isolated matched trials, or explicitly limit iteration 1 to protocol design and non-causal evidence. |
| External primary research was used for instruction locality, adherence, strategy effects, and length constraints. | Use external case-study/evaluation guidance during Extract and Challenge to structure inference and rival explanations. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] At least one HL hypothesis tested?
- [x] Counter-evidence sought?
- [x] Metacognitive check completed?

### Coordinator decision

2026-07-28 — **APPROVE**:

- Advance to Extract with H1–H3 provisional, preserving their counterexamples and the
  unresolved knowledge-destination discoverability/ownership questions.
- Classify limits before recommending retention or removal. The documented 15-file
  override is accepted as evidence about override semantics, not proof that the limit
  is useless.
- Keep H4 explicitly non-causal in iteration 1. Extract and Challenge must deliver the
  controlled-trial protocol, rival explanations, evaluation rubric, isolation
  requirements, and stopping criteria.
- Do not create or coordinate fresh/forked Codex tasks during iteration 1. Recommend
  the controlled trial for Iteration 2 after explicit owner approval of its cost and
  external task creation.
- Existing history-bearing tasks remain observational evidence only.

Stage complete: YES
→ User decision: coordinator approved advancement to Extract
