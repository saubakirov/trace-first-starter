# Extract — What do we not see?

> Mindset: Analyst. Make the whole, change consequences and comparison procedure inspectable.
> Parent: [HL](../../HL-TFW_20261021-150657_UTW.md)
> Goal: responsible people can explain the work and its change consequences, and inspect its contribution to purpose.
> Producer: codex:thread:local:01a15ead-17fe-77d0-ab5c-42f6122cc8d3
> Recipient: codex:thread:local:01a15de4-49bd-7101-98c7-3be0e89f3288

Date: 2026-10-21 (+05:00). Iteration 2 of 2; focused, one pass. Authority: journal/20261021-195144__gate_answer__81af.md @ 8d850ef9c808c8a61b57877fb66b8ffd99760bfa; received at 16071bb145dfaa48f182ba770b004cf5a8e12ba1. Complete routing remains RES / delegated / native-gates / tfw-gates-only / baseline, owner saubakirov, same unit and Coordinator; original mandate is HL section 4.1 @ 30c07f6d690482c8fdfeeecba29999089a3bcd87. Current status and iteration selection were reread; Extract is the first missing stage. No task controls change.

This record contains research examples and a proposed later procedure, not implementation, an approved trial or observed human performance. Local sources resolve at the received epoch above. Gather @ 17d60d7a95c070c69a535abd797ff9c3105cf999 supplies the full source-to-claim map.

## Configuration Space

The full unranked space is the Cartesian product of Gather's five three-valued dimensions: 3^5 = 243 combinations. Codes A/B/C refer exactly to Gather's alternatives, in its order. Formally every tuple `(o,g,a,r,p)` with each member in `{A,B,C}` is included; there is no hidden filtering or efficacy ranking. The following named slices make the combinations relevant to the cases visible without printing 243 rows. They are configurations for comparison, not decisions that all must be implemented.

| Config | Orientation and consequential relationships | Source and answer-ground presentation | Assistance exposure in the later comparison | Material refresh method | Production responsibility within existing ownership |
|---|---|---|---|---|---|
| S1 | A: linked account | A: inline sources | A: material, no live help | A: affected path | A: producer drafts |
| S2 | B: relation table | B: claim/source table | A: material, no live help | A: affected path | C: producer verifies generated draft |
| S3 | C: additional view | B: claim/source table | A: material, no live help | A: affected path | C: producer verifies generated draft |
| S4 | B: relation table | C: evaluator rationale | C: supported then separate unaided observation | B: reconstruct bounded whole | B: Coordinator assembles supplied sources |
| S5 | C: additional view | C: evaluator rationale | B: disclosed live help | C: extraction proposes relations | C: producer verifies generated draft |

S4 exposes a combination not concretely specified in Briefing: Coordinator assembly plus a whole reconstruction and separately grounded rationale, with supported and unaided observations kept distinct. It is not preferred yet. Every configuration still requires checkable source grounds; changing their presentation does not remove independent checking. An extraction tool proposes links but cannot accept their meaning. A producer retains responsibility for its claims even when another role assembles the whole.

For a controlled C1*/C2* comparison, hold the other four choices fixed: S2 versus S3 illustrates this. Do not compare S1 and S5 and attribute the difference to visualization alone. Optional C3* live assistance is a separate condition. C4* extraction is conditional infrastructure, not a prerequisite for either case.

## Findings

### E1 — Reader-facing TFW whole/change account (adequate C1*)

**Constructed case: a service team is preparing an updated response guide.** The approved purpose is to help the responsible operator give a correct next step when a request falls outside the ordinary service conditions. The guide and its supporting check were prepared using the service policy then in force. Before acceptance, the authoritative policy changes which requests need escalation. These scenario facts are invented for research; the workflow rules below are real. No customer, policy change or successful result is claimed to exist.

**Your responsibility:** decide whether the guide can be accepted now and explain what needs to happen next. You are not asked to memorize record names.

| Whole | Why the connection matters | What the policy change does |
|---|---|---|
| Approved purpose → promised behavior: operators can choose the correct next step | A polished guide is useful only if its advice serves that purpose | The purpose stays the same; the escalation advice may no longer meet it |
| Current policy → guide's decision rule → operator action | The rule depends on what the authoritative policy actually says | Inspect the affected rule and scenarios; do not infer the new answer merely from the existence of a new version |
| Applicable check → claim that the guide gives correct advice | A check supports the version and assumptions it actually examined | Earlier evidence remains evidence about its old conditions; it may no longer support the changed rule |
| Producer's return → independent judgment → acceptance decision | Writing the guide and judging whether its material claims are established are different responsibilities | The producer repairs affected content/proof within authority; the independent reviewer judges the affected result |
| Accepted result → qualified reusable knowledge | Future work needs the claim's source, scope and acceptance, not just a copied conclusion | Technical guidance and human-sourced business context follow their respective qualification paths; acceptance is not blanket publication |

**Current decision:** acceptance of the affected advice is not established by the old check alone. First inspect the new policy's relevant clause and the guide's dependent branch. Repair the rule if needed, obtain applicable evidence for affected claims, preserve unaffected evidence with its reasons, then return for independent judgment. If the needed change exceeds approved scope or changes the governing purpose, the Coordinator obtains the missing decision; the producer cannot grant it to itself. The scenario does not specify the policy's new text, so a concrete escalation answer would be invented.

**Purpose assumption:** correct, accessible escalation advice helps the operator take the appropriate next step. **Possible defeater:** the operator cannot find the applicable branch or the advice uses conditions the operator cannot observe. These are questions to investigate, not reported failures. The ordinary Purpose Check already addresses material harm to the approved value; this framing proposes making the causal assumption visible before review, not adding a second verdict.

**Inspect the grounds:** handoff workflow Step 2.8 and review Step 2 govern dependency-sensitive evidence; review Steps 3–5 and Judge Purpose Check govern judgment; docs/knowledge workflows govern qualified reuse. The task's actual approved purpose and current policy would be required source objects in a real pilot. Here their stated fictional facts are the scenario's authority, not repository evidence of a real business requirement.

### E2 — Reader-facing documentation whole/change account (adequate C1*)

**Observed structure, constructed change.** This repository prepares a documentation site from selected project Markdown and generated navigation. The intended reader benefit is finding the project's guidance in a browsable site; that benefit has not been measured here. You maintain the published guidance and need to explain what a source change can affect.

| Whole | Concrete source relationship | What is and is not established |
|---|---|---|
| Project Markdown → selected pages | `STATIC_SOURCES` maps `.tfw/conventions.md` to `reference/conventions.md`; globs include workflows/templates | Selection is visible in code, not proof that every useful page is selected |
| Markdown link → rewritten page link | The rewriter resolves mapped relative `.md` targets and carries a `#fragment` unchanged | Rewriting the path does not check whether that fragment exists |
| Page text → generated content and navigation | `copy_page`, section indexes and `_generate_nav` write through the plugin API; navigation uses `SUMMARY.md` | Intended build inputs are visible; generated bytes have not been inspected in this stage |
| Configured build → site artifact | MkDocs config uses `site_dir: ../site`; Actions runs the build and uploads `site/` | The configured path is known; success and artifact contents are unknown |
| Artifact → deployment → reader use | A separate Pages deployment job depends on build | Neither configuration nor a build claim alone proves live availability or reader understanding |

**Constructed change:** a selected source page links to `.tfw/conventions.md` using the relative path appropriate to that source and the fragment `#example-policy`. The destination heading is changed so its intended fragment becomes `#revised-policy`. Those heading names are fictional and assert no actual repository defect. The source mapping and file paths stay unchanged.

**Consequence:** the rewriter can still produce the mapped page path carrying `#example-policy`. That does not establish a usable jump to the new heading. Inspect and update affected source links as appropriate, establish the actual rendered heading/anchor behavior in the selected environment and check the affected built output. The code does not justify claiming that all links broke, all links work, the build necessarily fails, or deployment has happened. Unaffected source-selection relationships need not be reconstructed solely because this heading changed.

**Inspect the grounds:** `docs/scripts/gen_docs.py` functions `_source_map`, `rewrite_markdown_links`, `copy_page` and `_generate_nav`; `docs/mkdocs.yml`; `.github/workflows/docs.yml`. Exact dependencies and runtime behavior must be bound before a future runtime claim. Gather's current external-manual/MkDocs applicability uncertainty remains open.

### E3 — Additional C2* views with the same facts

The named difficulty is tracing a changed dependency across different carriers without losing which claim it supports. These optional views add placement and visible edges, not new facts. Their content and sources must also remain available in C1*.

```text
TFW: approved purpose ─constrains─> correct operator next step
                                      ^
current policy ─defines─> guide rule ─supports─┘
       │                     │
       └─change may affect───>│<──applicable check supports claim
                             v
                   producer return → independent judgment → acceptance
                                                              │
                                                              v
                                            qualified reuse with source/scope

Docs: selected source → page transformation → generated inputs → build → artifact
          │                  │                                  │        │
          │         mapped path + unchanged fragment            │        v
          │                  ^                                  │  deployment → reader
          └─heading change───┘                                  │
                 requires target inspection, not proven by rewrite or config
```

Arrows mean the labeled informational/processing relationship, never proof of successful execution. The TFW view omits none of the acceptance/publication qualifications in E1. The documentation view retains the separation between source, generated input, artifact and actual reader use. If maintaining these views adds no useful search or reasoning benefit beyond the existing tables, omitting them remains a live outcome for Challenge.

### E4 — Independently grounded scenario criteria

These are draft evaluation criteria, not an answer key validated by this Researcher's authorship. Before a human pilot, an independent Reviewer must derive/check them from the cited source clauses/functions and the fixed scenario facts, separately from the explanatory account. Any disagreement blocks the affected criterion, not explanation access. Preserve source identity and accepted corrections before interpreting results.

| New prompt after orientation | Required reasoning, with acceptable uncertainty | Independent grounds |
|---|---|---|
| TFW: the policy changed only escalation eligibility after initial checks. Can all old evidence be reused, and who must do what? | Identify the dependent rule/check; preserve applicable unaffected evidence; obtain affected proof/repair; distinguish producer, independent judgment and missing authority. Do not invent policy content. | Handoff Step 2.8; review Verify and item routing; fixed scenario facts |
| TFW: instead, only an unrelated policy paragraph was reformatted. Must all work restart? | No blanket restart; inspect relevance and retain evidence whose dependencies still apply. Explain why an unrelated edit has no stated effect. | EV evidence applicability paragraph; review materiality |
| TFW: a team proposes removing every exceptional case to shorten the guide. Does a green check prove value? | Compare against the approved purpose; removing the required help can defeat that purpose. A valid change of purpose requires actual authority. Outcome evidence may still be unavailable. | Judge Purpose Check plus scenario purpose; no claim that shorter is always worse |
| Docs: destination heading changed but mapping did not. What can you conclude without a build? | Path rewriting retains the fragment; actual target resolution/build/deployment are unknown. Identify affected source link and rendered target as checks. | Rewriter's `partition`, unchanged `fragment` suffix, mapping conditions; build config |
| Docs: a source outside the static list and globs is edited. Must its text appear in the generated pages? | Not established by this generator's selection; inspect whether it is included by another relevant path before a whole-site claim. | Static/glob definitions; scope of inspected generator, not an asserted exhaustive site model |

For each material response, record `source-supported`, `partly supported`, `unsupported` or `unavailable`, with the exact claim/reason. Do not collapse these into an employee score. A response naming a real limitation can be correct; a confident unsupported conclusion cannot. Observe the whole account too: what the work is for, how the relevant parts connect, what changed, and where the conclusion stops.

### E5 — Bounded later pilot procedure

Proposed TS choices, not authorization: one responsible TFW participant and one maintainer of the final selected software case; the same person may fill both only if recorded. A small within-person feasibility pilot cannot establish population effectiveness. Final software selection, participant agreement, environment and time budget belong to the owner/TS stage.

1. Fix the selected source epochs, responsibility, scenario facts, explanation variants and independently checked rationale. Bind installed versions and actual output if runtime claims are in scope. Record prior familiarity; show the whole orientation before asking change questions. Explanation is always available on request.
2. Establish B0 using the project's current means: existing artifacts, source search and diagrams already available, with normal assistance explicitly recorded. B0 must be sufficient to attempt the same responsibility, not artificially deprived. Collect response, source path used, uncertainty and elapsed active time.
3. Compare adequate C1* to C2* on matched but different change scenarios with the same facts, available sources and help rules. Counterbalance order across participants when available; for a single participant record order and practice contamination and treat the result as feasibility only. Never reuse a learned answer as evidence of transfer.
4. If live assistance is used, record prompts/help and label the outcome supported performance. Any unaided observation is a separately consented later task with sources/help conditions stated; keep it separate from supported work. Optional C3* conversation is not required to get an explanation. This pilot need not claim durable retention.
5. Record material reasoning from E4 plus omissions, unsupported links, uncertainty, searches, clarification/help, active time and self-reported effort. Confidence is supplemental, never the understanding measure. Let the participant correct an explanation error; preserve the original response and correction separately.
6. Apply one material change and one nonmaterial edit to the approved pilot material. Record preparation, source checking, human review, use and refresh time separately; record what was reused and why. No new permanent test follows merely from doing the pilot.
7. Decide against the baseline: retain an added view only if it addresses the named difficulty without losing material accuracy and its observed burden fits the owner-approved budget. Equal adequate results with additional maintenance support simplifying to C1*. An unclear or contaminated observation remains inconclusive. Thresholds/budget must be approved before interpreting the run; no invented numerical advantage is promised here.

Time observations use actual start/stop intervals and interruptions; preparation includes agent drafting plus human verification, not just final reading. Token economics can complement this but cannot stand in for human use/update cost. The later EV can preserve concise scenario/version, conditions, actual response or attributable observation, independent judgment and measurement values; raw recordings need not become a new mandatory framework artifact.

### E6 — Existing integration and refresh owners

| Candidate existing location | Proposed small effect | Producer and refresh responsibility |
|---|---|---|
| HL §2, §3.1 and §3.2; planning workflow at those existing obligations | Use actual context, outcome preview and value flow to identify responsible reader, relevant whole and contribution assumption; do not duplicate mandatory existing visualizations | Coordinator prepares; owner approves governing intent. A frozen-contract change follows amendment authority. |
| ONB §1 Understanding and §2 Entry Points | Source-bound explanation of purpose, relevant relationships and uncertainty; questions remain available without a quiz | Executor verifies its draft against current task/source dependencies on entry and material change |
| RF §2 Key Decisions, §9 Diagrams and Material handover | Carry the useful whole/change explanation and affected source/claim/owner; optional additional view only for a named need | Executor updates affected claims; Coordinator consolidates the bounded return without replacing source ownership |
| EV Evidence and review Verify/Judge | Record actual human-use observations separately from build facts and assumptions; inspect applicability and purpose through existing checks | Producer captures; independent Reviewer checks grounds and judgment. No universal examination gate |
| Selected docs/knowledge records and owning references | Preserve a useful accepted explanation only where reuse is owed; source, scope and refresh responsibility travel with it | Existing authorized Docs/Knowledge owner qualifies; acceptance and closing authority remain unchanged |

For the TFW example, a policy change triggers the guide producer's affected-claim inspection, then proof/judgment as required; a typo unrelated to meaning does not restart the task. For documentation, a heading/link change triggers the maintainer's affected source/target inspection; a source byte change irrelevant to selected output does not establish global invalidity. Unknown dependency relevance is named uncertainty requiring bounded inspection, not automatic passing or universal rebuilding.

Optional domain recipes supply the relations needed in that domain: policy → decision rule → operator action for service guidance; source → transformation → output → reader for documentation. The shared core asks for purpose, relevant whole, consequential dependencies, grounds, limits and refresh ownership. It does not mandate software-specific graphs, terminology or automatic drift scores. These are candidate edits for TS, not changes made to the listed files.

### E7 — External grounding and design inference

The existing [C4 system-context guidance](https://c4model.com/diagrams/system-context) was rechecked on 2026-10-21 for the audience/boundary decision. It emphasizes the system, people and directly related systems at a coarse level for technical and nontechnical audiences. E1/E2 apply the broader presentation idea by starting with responsibility and a bounded whole; this is our design inference, not a claim that C4 validates these TFW accounts. The more detailed tables are needed here to inspect consequential dependencies. Earlier retrieval/assistance evidence remains at its recorded educational/task-specific limits; no new efficacy inference or broad source search is made.

## Checkpoint

| Found | Remaining |
|---|---|
| Actual readable whole/change accounts and optional same-fact relation views | Challenge: shared explanation/key error, missing context, unsupported relation and adequate simpler alternative |
| Concrete source-grounded scenarios and later comparison procedure | Independent checking and actual human use remain future authorized work |
| Existing integration/refresh owners and distinct measurements | Final locations, participant/budget, software case and environment require TS selection |
| Existing purpose baseline and explicit contribution assumption | Challenge must distinguish added value, duplicate procedure, adaptation and uncertainty |

- [x] External source used with its evidentiary limit.
- [x] Briefing Extract gap closed: examples, answer grounds, procedure and existing owners are concrete.
- [x] Configuration space built from the exact Gather dimensions; full product specified and named combinations exposed.

Focused decision: pass these concrete materials to Challenge as candidates, without selecting a winning representation or asserting effectiveness. This is one analytic pass. No implementation, install, build, deployment, human trial or permanent test occurred.

Knowledge handover: sources and epoch, unit, recipient, material examples/proposal, unresolved decisions and authorized next act are explicit. No new human-only Fact Candidate or Strategic Insight arose; agent-proposed contribution assumptions belong to decisions, not RF's human-only Strategic Insights. Prior knowledge dispositions remain scoped. Own economics revision 1 remains unchanged; resumed work beyond its cutoff belongs in the covering successor at iteration-2 RES, not zero or the old delivery tail.

Stage complete: YES

Required Coordinator decision: accept Extract and authorize Challenge, or identify the material account/procedure gap. Recommendation: accept for adversarial checking, without accepting human benefit or implementation. STOP before Challenge.
