# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260907-133942_PTTC](../../HL-TFW_20260907-133942_PTTC.md)
> Goal: Identify the simplest complete and coherent verification design by removing accidental test coupling and duplicated obligations while preserving meaningful defect detection and honest completion.

## Consistency Check

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|-------------|-------------|-------------|-------------|-----------------|
| D1: contract being protected | Historical acceptance or release package | D3: evidence source | Live repository corpus as the sole historical oracle | A moving current tree cannot establish an immutable historical byte claim; the CRUE repair demonstrates the legitimate successor would be rejected. |
| D1: contract being protected | Current semantic invariant | D3: evidence source | Immutable Git baseline/release ref as the sole current oracle | A historical ref can preserve lineage but cannot by itself establish that the current successor still satisfies the live contract. |
| D1: contract being protected | Generated HTML/link behavior | D2: execution dependency | Pure no-build test module with no generated artifact | Without generated output or an equivalent bounded renderer contract, the test cannot establish the output behavior it claims to protect. |
| D1: contract being protected | Live-corpus health diagnostic | D4: disposition | KEEP as a mandatory product/release gate | Corpus health is an optional diagnostic boundary here; making it a release oracle turns a retained historical indeterminate input into a false product failure. |
| D1: contract being protected | Structural/copy/parity invariant | D4: disposition | REMOVE with no surviving equivalent check | Removing the only parity or mutant check loses the concrete boundary even if the source files remain present. |

### Surviving configurations

| Config | D1 | D2 | D3 | D4 | Notes |
|--------|----|----|----|----|-------|
| C2 | Current semantic invariant | Explicit integration fixture for HTML-output tests | Current working tree | REWORK | Retain output-facing protection while narrowing the fixture boundary. |
| C3 | Current semantic invariant | Pure no-build test module | Current working tree | MOVE | Suitable for repository/state predicates whose evidence is not `site/`. |
| C4 | Current semantic invariant | Direct bounded helper or subprocess check | Synthetic `tmp_path` fixture and mutants | REWORK | Useful when a small adverse input is the protected consequence, not live corpus cleanliness. |
| C7 | Historical acceptance or release package | Pure no-build test module | Immutable Git baseline/release ref | REWORK | Historical claims remain pinned, but current successor state is checked separately. |
| C8 | Structural/copy/parity invariant | Pure no-build test module | Current working tree | KEEP | Candidate for exact-copy and current surface checks that need no renderer. |
| C9 | Structural/copy/parity invariant | Direct bounded helper or subprocess check | Synthetic `tmp_path` fixture and mutants | REWORK | Candidate for package replay, stale-term and controlled doctor semantics. |
| C10 | Live-corpus health diagnostic | Module-wide autouse MkDocs build | Live repository corpus | REMOVE | Remove the gate; retain doctor behavior through controlled fixtures. |
| C11 | Live-corpus health diagnostic | Pure no-build test module | Live repository corpus | MOVE | If retained, keep it explicitly optional/non-gating and separate from product acceptance. |
| C13 | Historical acceptance or release package | Direct bounded helper or subprocess check | Current working tree | KEEP | Only when the predicate is actually a current metadata contract, as in CRUE's `_current_release_metadata`. |
| C16 | Historical acceptance or release package | Pure no-build test module | Synthetic `tmp_path` fixture and mutants | KEEP | Package replay can prove a bounded transformation without a site build. |

### Unexpected survivors

- **C10:** Removing a live-corpus gate survives because it removes an acceptance condition that protects no current product output, while the six controlled doctor tests preserve diagnostic correctness.
- **C9:** A structural guard plus a small mutant fixture survives without either a whole-site build or a live corpus; its protection is the rejected adverse input, not the amount of machinery around it.
- **C11:** An optional pure diagnostic can survive as disclosed information, but it is incompatible with treating “zero findings” as a universal release oracle.

## Findings

### C1: Duplicate definitions — distinguish superseded contracts from lost current protection

The official [Python language reference on function definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions) states that a `def` statement is executable and binds the function name in the current namespace to a function object. The [execution model's naming and binding section](https://docs.python.org/3/reference/executionmodel.html#binding-of-names) lists function definitions as name-binding operations. Therefore repeated module-level definitions make the later body the object bound to the name used by a collector; this conclusion is from language semantics, not a pytest run.

The early Phase D bodies are not automatically missing current tests. The source itself marks the transition at lines 2173-2175 as replacing the historical selector/protection projection with the revision-2 epoch semantics without erasing its history. The later bodies provide the revised coverage:

- The first `test_phase_d_literal_value_assurance_and_trace_boundary_is_complete` (2117-2125) checks the original baseline-to-candidate value and trace boundary. The later same-name definition (2305-2321) checks the baseline value set plus the approval-epoch changed set and ancestry. The later check is the applicable revised contract; reviving the first as a second test would reintroduce the superseded baseline-only assertion.
- The first `test_phase_d_workflow_copies_and_codex_managed_receiver_are_exact` (2128-2140) checks the old baseline/current receiver relation. The later definition (2336-2354) checks candidate Git copies, current adapter parity, and approved-to-candidate managed-block movement. The latter matches the revision-2 epoch boundary and is surviving coverage.
- The first `test_phase_d_added_product_lines_do_not_leak_provider_names_or_apis` (2159-2170) is an old baseline-to-current scan. The applicable later predicate is `test_phase_d_added_product_provider_terms_are_confined_to_adapter_and_named_exception` (2434-2450), which adds the revision-epoch comparison and named exceptions. The same old name is reintroduced only as a wrapper at 2735-2736; the exact 2159/2735 repeated name is real, but the 2434 function has a different, current name.
- The first `test_phase_d_claude_release_config_history_and_prior_phases_are_byte_exact` (2143-2156) is a historical full-tree byte check. The later same-name wrapper (2488-2489) calls the revised `test_phase_d_approval_epoch_protects_history_inputs_and_cumulative_prefixes`; the wrapper preserves a historical selector label, not the old body. The repository search found only these definitions and no in-repository command/workflow/doc selector.

Challenge result: classify the early bodies as dead/superseded assertions, not KEEP candidates to resurrect. Classify the later uniquely named predicates as KEEP for their revised protected consequences. The no-consumer wrapper is a REMOVE/REWORK candidate only with the bounded caveat that external consumers were not searched; “not found in this repository” is not proof of global selector absence. No current protection was shown to disappear solely because the old bodies are overwritten, but the naming collision remains a maintainability and future-loss hazard.

### C2: Knowledge row locks — retain the decision, not an accidental permanent snapshot

Three cases separate the protection levels:

1. **Harmless rewording:** changing the explanatory prose of the D83 row to clarify the same selected-LEAD/unit rule, or adding a valid source citation while preserving decision ID, task/phase identity, and the approved consequence, would make `test_phase_e_knowledge_keeps_exact_rtbo_and_final_cratm_decisions` fail because it compares the complete row from an immutable ref. This is a structural false rejection inferred directly from the predicate; it is not claimed as an observed incident.
2. **Legitimate successor:** the committed CRUE repair `a767b17072733dc856d4c73fa6a72277e1538ba5` accepts a successor release through current metadata while historical 3.0.0 bytes remain checked at `8fd8e40b734e9c439bb84721ef8bee441b9fcdd7`. Within the knowledge lineage itself, D84 is a later approved decision that is absent from pre-K2 records and present in the post-K2/current record. A future additive decision must not be rejected merely because the currently known decision set was treated as a universal “latest” snapshot.
3. **Real contradiction/loss:** relabeling the D83 Agent Team decision as D82, deleting D84's writer-attribution decision, swapping the B–D/B–E task label, or replacing the cited immutable commit with an invented address would misstate authority and historical provenance. The existing mutants in lines 2708-2721 represent these concrete failure classes. The narrower current-lineage check at 2398-2412 also protects the D82/D83 distinction and rejects the obsolete Agent Team wording.

The minimum defensible meaning is therefore bounded, not universal: protect one row per explicitly retained decision ID, its governing task/phase identity, required immutable source references, and the known superseded/current distinction; allow later additive decisions and approved explanatory edits unless they alter that protected meaning. The exact semantic field set requires a later owner/Coordinator design decision; this audit does not invent a generic knowledge validator. Initial disposition: REWORK the full-row lock, KEEP the narrow lineage/contradiction protection, and preserve the complete historical rows as knowledge rather than treating them as current byte oracles.

### C3: Regex and retired-string guards — identify the residual consequence

Removing `test_no_board_shaped_regex_survives_in_the_generators` loses one specific cheap defense: detection of a likely literal reintroduction of the retired Task Board parser in any generator script. The simpler existing checks cover related but not identical surfaces: `test_generators_do_not_read_the_root_readme_for_task_state` inspects the task-landing function for the current state source, and generated-output tests catch some resulting page failures. A helper elsewhere could still parse the root README without matching the exact regex and without immediately changing a visible output. The regex guard therefore has a residual architectural consequence, but its predicate is syntactic and should not be presented as proof of actual behavior. Candidate disposition: KEEP only as a narrowly named defense-in-depth check, or REWORK it toward the actual forbidden dependency if a simpler source-derived assertion can cover all generator entrypoints.

The retired-wording registry has a different, direct consequence: a receiving reader can act on contradictory live instructions. `test_no_normative_file_states_a_retired_rule` and `test_no_adapter_file_states_a_retired_rule` cover different shipped surfaces, so deleting one loses coverage even though both use the same registry. Their small “actually fires” tests protect against a vacuous empty/nonmatching registry; they are not behavior claims about agents. The simplest adequate design keeps those consequence checks and their non-vacuity probes, moves them out of the MkDocs fixture, and reviews registry entries individually for obsolete scope. No evidence supports deleting the registry merely because it uses string matching.

### C4: Harmful subtraction and retained protection

The following attack cases survive the challenge:

| Subtraction | Harmful consequence | Surviving protection / decision |
|---|---|---|
| Remove the module build from all integration tests | Generated HTML can stop resolving links, rendering frontmatter, or producing required pages while pure checks stay green | KEEP explicit build only for site-output predicates; MOVE pure checks |
| Remove the whole D82/D83/D84 knowledge contract | Authority, phase lineage, or writer-attribution decisions can be duplicated, relabeled, or lost without a current check | KEEP bounded uniqueness/source/lineage protection; REWORK away from full-row prose lock |
| Remove all regex/retired-string checks as “just strings” | A retired parser dependency or contradictory receiver instruction can return without a direct failure | KEEP the retired-wording consequence checks; retain or replace the regex only if an equivalent dependency guard is evidenced |
| Restore every early duplicate Phase D body under a new name | Superseded baseline/epoch assumptions re-enter and reject legitimate post-revision composition | Do not restore old bodies; retain later revised predicates with unique names and investigate the wrapper separately |
| Keep the live-corpus doctor-clean test as a release gate | Historical malformed records block valid current work and conflate diagnostic health with product acceptance | REMOVE global gate; KEEP controlled doctor fixtures and explicit optional diagnostics |

## Checkpoint

| Found | Remaining |
|---|---|
| Challenge distinguishes dead superseded duplicate bodies from current revised coverage; the true same-name wrapper has no bounded in-repo consumer evidence but external use remains unknown. Full knowledge row equality is too broad; bounded lineage/provenance protection remains necessary. Retired-wording scans protect live instructions; the board regex has a narrower residual architectural role and cannot claim behavior proof. | Exact TS-level semantic fields for knowledge lineage and the final regex disposition remain for Coordinator/Plan. No runtime confirmation or cost measurement is authorized or needed for this iteration's bounded necessity conclusion. |

**Sufficiency:**
- [x] External source used? — official Python language reference and pytest fixture documentation, linked above and in Gather/Extract.
- [x] Briefing gap closed? — harmful subtraction, legitimate successor, real contradiction/loss, supersession, residual protections, and simpler dispositions are explicit.
- [x] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: YES
→ User decision: Proceed to RES synthesis; do not run tests, builds, selectors, or probes.
