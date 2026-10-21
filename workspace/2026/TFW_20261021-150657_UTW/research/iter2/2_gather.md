# Gather — What do we not know?

> Mindset: Explorer. Bind the two cases before designing their explanatory material.
> Parent: [HL](../../HL-TFW_20261021-150657_UTW.md)
> Goal: preserve a responsibility-relevant whole, material change consequences and inspectable contribution to purpose through ordinary TFW work.
> Producer: codex:thread:local:01a15ead-17fe-77d0-ab5c-42f6122cc8d3
> Recipient: codex:thread:local:01a15de4-49bd-7101-98c7-3be0e89f3288

Date: 2026-10-21 (+05:00). Iteration 2 of 2; focused; one pass. Gather activation is journal/20261021-194352__gate_answer__b5d8.md @ 44bd6c31d5abd67799b3f39f9d0e116ace894fe4, accepting Briefing @ 29da2498551bc5d5ae4c0e102bb4b57ae0b9eeff. Controls were received at 4e1a9cbb48a8d64c504562734f8e5ed4b4e39ab5; all local source references below resolve at that epoch unless stated otherwise. Complete status/iteration selection remains RES / delegated / native-gates / tfw-gates-only / baseline, same owner and routes, frozen HL authority @ 30c07f6d690482c8fdfeeecba29999089a3bcd87. No control file is changed here.

## Dimensions

These are case-design degrees of freedom, not competing truth standards. The independent source and authority requirements apply to every alternative. No option is ranked at Gather; combinations will be bounded in Extract and tested in Challenge. Iteration-1 evidence is retained at its original scope.

| Dimension | Alt A | Alt B | Alt C |
|---|---|---|---|
| Orientation and consequential relationships | One linked whole/change account in the existing carrier | A compact relation table within that account | An additional derived relationship view linked to the same account |
| Source and answer-ground presentation | Citations beside each consequential claim | A compact claim-to-source table | A separately readable, source-bound scenario rationale for the evaluator |
| Assistance exposure in the later comparison | Equal source/material access without live assistance | Equal access with disclosed, recorded live assistance | Separate supported-use and subsequent unaided observations |
| Material refresh method | Author checks the affected decision path | Author reconstructs the bounded whole from current sources | Domain extraction proposes affected relations for author verification |
| Production responsibility within existing ownership | Producing role drafts its own explanation | Producing role supplies sources and a Coordinator assembles the relevant whole | Producing role verifies an agent-generated draft against the same sources |

An adequate C1* can contain a table or small diagram. C2* means an additional representation with a named benefit and maintenance burden. Refresh methods are alternatives for inspecting affected meaning, never permission to discard unaffected evidence or regenerate everything after every edit. Evaluator rationale cannot grant itself authority or prove its correctness by matching the explanation.

## Findings

### G1 — TFW case: purpose, changed dependency, acceptance and reuse

The selected scenario is **constructed**, not a discovered defect or an observed completed task: after initial evidence has been obtained but before acceptance, a dependency relevant to an accepted claim changes. The reader must determine what the change affects, what evidence still applies, who can act and whether the work still serves its purpose. The exact fictional claim and change will be made explicit in Extract; no real task result is invented.

| Relationship needed in the account | Independent canonical grounds | Consequence for the case |
|---|---|---|
| Governing purpose constrains local success | `.tfw/templates/review/judge.md`, Purpose Check, inspected in iteration 1; `.tfw/workflows/review.md`, Step 3 | Master HL baseline plus North Star are the purpose reference. Passing a local check is insufficient to establish contribution. |
| Approved work determines authorized execution | `.tfw/workflows/handoff.md`, Steps 1–2 | Executor explains governing artifacts in ONB and works within approved TS and boundaries; a missing scope decision returns to the Coordinator. |
| Claim depends on subject, environment, oracle and dependency state | `.tfw/workflows/handoff.md`, Step 2.8; `.tfw/workflows/review.md`, Step 2; prior EV template evidence rules | Changed or uncertain relevant dependencies require affected rechecking. Earlier evidence is preserved with its epoch, not silently relabeled as current. |
| Evidence supports a returned result, then independent judgment | `.tfw/workflows/handoff.md`, Step 3; `.tfw/workflows/review.md`, finding contract and Steps 1–5 | RF binds claims and EV; Reviewer classifies concrete material findings before verdict. An assurance-only gap need not change established Candidate identity. |
| Accepted work can yield reusable technical or human knowledge | `.tfw/workflows/docs.md`, Steps 1–3; `.tfw/workflows/knowledge.md`, Steps 1–4 | Technical/reference effects and human-only claims use different qualification paths. Neither RF nor APPROVE automatically publishes every statement as knowledge. |
| Reuse retains provenance, scope and actual acceptance | Same docs/knowledge sections | A newer source, duplicate paraphrase or source instruction is not acceptance. Changed accepted claims need their affected-result check; final close remains with the closing Coordinator. |

This is a purpose-to-result chain with branches into qualified reuse, not a diagram of messages between roles. The author of the affected result owns its repair; independent Reviewer owns judgment; the Coordinator resolves the next authorized act; the selected Docs/Knowledge authority owns the publication effect. A proposed understanding aid must fit these owners rather than create a second authority.

Known baseline: Purpose Check already asks whether a local result harms the governing purpose. The proposed contribution question must therefore earn its place by making an assumption, expected outcome or defeater inspectable earlier or more clearly. Its mere presence is not an incremental benefit. Valid authorized adaptation and insufficient outcome evidence must remain distinct from purpose failure.

### G2 — Documentation case: selected sources to a build artifact

Read-only inspection covers `docs/scripts/gen_docs.py`, `docs/mkdocs.yml`, `docs/requirements.txt` and `.github/workflows/docs.yml`. The following are source/configuration observations, not execution results.

| Relationship | Actual source grounds | Limit that the eventual explanation must preserve |
|---|---|---|
| Repository files become selected documentation inputs | `STATIC_SOURCES`, `GLOB_SOURCES`, `_source_map`, `validate_sources` | Required static files are checked for existence. This does not establish the truth of their content or the completeness of all desired documentation. |
| Selected Markdown becomes generated page content | `copy_page`, `rewrite_markdown_links`, `add_frontmatter` | Mapped relative Markdown paths are rewritten; fragments are carried through. The function does not inspect target anchors. Unmapped links can remain unchanged. |
| Pages obtain section indexes and navigation | `_section_index`, `_generate_nav`, `main`; `literate-nav` configuration | Navigation is generated from selected mappings/globs. A navigation entry alone proves neither reader orientation nor semantic correctness. |
| Generator participates in site build | `gen-files` script setting in `docs/mkdocs.yml`; `mkdocs_gen_files.open` calls | Generated page names are build inputs, not necessarily committed source files. Do not infer durable repository copies from those calls. |
| Configured build yields the uploaded directory | `site_dir: ../site`; Actions build command and upload path `site/` | This is the configured path. No build, artifact contents or CI success was observed in this research. |
| Deployment follows a separate job | Actions `deploy` needs `build`, GitHub Pages environment and deploy action | A source account of the build does not prove deployment or end-user availability. |

The bounded source question is now concrete: if a mapped source path or heading changes, which selection, rewritten link, fragment and resulting page claims need inspection? A pathname mapping and a heading/anchor relationship are different dependencies. The eventual example must not teach that rewriting a link validates its target anchor. No actual broken link is asserted here.

The project installs dependencies from lower-bound requirements, including MkDocs and mkdocs-gen-files; exact installed versions were not measured. Runtime dependency resolution, successful rendering, published availability and human navigation remain unknown. No package installation, build or deployment was performed.

### G3 — One bounded external check and its applicability limit

The [mkdocs-gen-files manual](https://oprypin.github.io/mkdocs-gen-files/) was inspected on 2026-10-21, specifically Usage and Description, to clarify whether generated pages are durable source files. It describes plugin-mode writes as virtual modifications used during the build, while standalone script use can write actual files. That distinction supports keeping source, generated inputs and built output separate in the case.

The current manual now describes ProperDocs, whereas this repository explicitly configures MkDocs. Consequently it is documentation of the current package's presentation, not proof of the exact installed version's behavior or compatibility here. The local configuration and calls establish intended integration; an eventual pilot must bind the actual environment before making a runtime claim. This source-version mismatch is an explicit unknown, not a reason to change the project or expand into migration research.

Iteration-1 C4 and Larkin/Simon evidence remains relevant to boundary/relationship presentation; the retrieval/assistance studies remain relevant to equal facts, access and help conditions. None establishes that these particular examples improve workplace understanding. No new broad literature search was needed.

### G4 — Comparison grounds and missing observations

| Design question | Grounds now available | What Extract must specify, and what remains for actual use |
|---|---|---|
| Can the reader recover the relevant whole? | Purpose-to-acceptance/reuse chain and source-to-build chain above | Initial orientation, reader responsibility and a new change scenario; actual human response is later evidence. |
| Is C2* worth maintaining? | Named cross-source relation difficulty, with adequate C1* allowed | Same facts/access/help in the comparison; count searches, unsupported inferences and explanation failures, not diagram attractiveness alone. |
| Can the answer grounds be checked independently? | Canonical claim/evidence/authority rules and exact generator functions | Source-derived rationale checked separately from the explanation; correct uncertainty accepted. Matching two generated texts is insufficient. |
| Does strategic framing add anything? | Existing Purpose Check already addresses purpose harm | An explicit assumption/defeater contrast against that baseline, including authorized adaptation and unavailable outcomes. |
| Who refreshes what? | Existing producer, Reviewer and Coordinator responsibilities | Affected claim/relation, source epoch, repair owner and reuse disposition for each case; material versus nonmaterial changes. |
| Is the burden proportionate? | Identifiable preparation, use, checking and update actions | Record actual time/help/rework later; no operating-cost estimate is inferred from source inspection or agent token totals. |

## Checkpoint

| Found | Remaining |
|---|---|
| Two bounded cases with source-grounded consequential relationships and existing owners | Concrete whole/change accounts and candidate integration locations in Extract |
| Distinct result acceptance, evidence applicability and knowledge qualification | Independent scenario criteria and baseline/help procedure |
| Generator transformations and configured build boundary, including a false anchor-validation inference | Actual environment/execution unknown; runtime claims require later evidence |
| Existing Purpose Check baseline and semantic refresh boundary | Challenge must test added value, shared errors, missing context and simpler alternatives |

- [x] External source used for a named case-design gap, with current-version limitation preserved.
- [x] Briefing Gather gap closed: sources, relationships, unknowns and comparison dimensions are bound.
- [x] Dimensions identified with at least three alternatives, no ranking.

Focused OODA decision: carry these two source-bound cases into Extract without broadening the source catalogue. Their material uncertainties now concern account adequacy and fair evaluation, not an absence of inspectable source relationships. One pass is sufficient for Gather; no hypothesis is empirically confirmed.

Knowledge handover: this record is the material return; source scope/epoch, producer, recipient, uncertainty and next act are explicit. No new human-only Fact Candidate or Strategic Insight arose in this stage. Prior knowledge dispositions remain at their recorded scope. Own economics revision 1 and its finite cutoff remain unchanged; resumed work is beyond it and will be included in the validated covering successor at iteration-2 RES, not treated as zero.

Stage complete: YES

Required Coordinator decision: accept Gather and authorize Extract for these two bounded cases, or name the material source/dimension gap. Recommendation: accept the checkpoint, without selecting a representation alternative yet. STOP before Extract under the stage gate.
