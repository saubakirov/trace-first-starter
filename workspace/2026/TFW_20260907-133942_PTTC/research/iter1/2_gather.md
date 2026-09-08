# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260907-133942_PTTC](../../HL-TFW_20260907-133942_PTTC.md)
> Goal: Identify the simplest complete and coherent verification design by removing accidental test coupling and duplicated obligations while preserving meaningful defect detection and honest completion.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D _(if any)_ |
|-----------|-------|-------|-------|-----------------|
| D1: contract being protected | Current semantic invariant | Historical acceptance or release package | Structural/copy/parity invariant | Live-corpus health diagnostic |
| D2: execution dependency | Module-wide autouse MkDocs build | Explicit integration fixture for HTML-output tests | Pure no-build test module | Direct bounded helper or subprocess check |
| D3: evidence source | Current working tree | Immutable Git baseline/release ref | Synthetic `tmp_path` fixture and mutants | Live repository corpus |
| D4: disposition of a mechanism | KEEP | REWORK | MOVE | REMOVE |

## Findings

### G1: The module fixture couples pure checks to a real site build

`docs/scripts/test_integration.py:20-37` defines `build_site` as `@pytest.fixture(scope="module", autouse=True)`. It invokes `python -m mkdocs build --config-file docs/mkdocs.yml` before every test in that module, whether the test reads generated HTML or only reads repository files, Git objects, or temporary trees. This is not an inferred pytest behavior: the official [pytest fixture reference](https://docs.pytest.org/en/stable/reference/reference.html#pytest.fixture) states that `autouse=True` activates a fixture for all tests that can see it and that `scope="module"` shares one fixture instance for the module; the [fixture explanation](https://docs.pytest.org/en/stable/explanation/fixtures.html#autouse-fixtures-fixtures-you-don-t-have-to-request) describes the same scope-wide activation.

The protected consequence is real for output-facing checks such as `test_static_pages_generated` (lines 40-49), `test_knowledge_index_generated` (51-58), `test_task_pages_generated` (60-68), `test_td_refs_resolved_in_output` (141-156), and `test_no_page_renders_its_own_frontmatter_as_body_text` (159-179): they inspect the generated site and need an actual build. Removing the build from those checks would miss a genuine generator/rendering defect.

The same dependency is unnecessary for pure checks. Examples include `test_phase_e_integrated_workflows_have_exact_copy_parity` (2623-2627), `test_phase_e_knowledge_keeps_exact_rtbo_and_final_cratm_decisions` (2650-2724), `test_phase_e_selected_product_and_assurance_files_have_no_conflict_markers` (2727-2732), `test_phase_e_ii_writer_rule_is_bounded_and_copy_identical` (2930-2943), and `test_phase_e_ii_release_destinations_are_protected_and_package_replays` (2975-3009). Their bodies read files, Git objects, or temporary release trees; none reads `site/` or requires HTML generation. A wording-only or control-record change in their inputs can therefore pay for a full site build without changing their claimed evidence.

**Initial disposition:** KEEP the build dependency for HTML-output integration checks; REWORK/MOVE pure checks to an explicit no-build family. The simplest adequate change is to separate the dependency at the test-family boundary, not to add a selector, cache, or universal orchestration layer. Actual setup/body/review durations remain unmeasured because no probe was authorized.

### G2: The committed CRUE repair separates current contracts from historical acceptance

The independent committed source `a767b17072733dc856d4c73fa6a72277e1538ba5` has tree `06e466315a856ede01044b521d840647163014d4`. Its diff provides a concrete counterexample to freezing the current tree at a historical snapshot:

- `_current_release_metadata(root)` now validates the installed version, the newest non-`Unreleased` changelog entry, unique current release heading, nonempty body, referenced migration files, and current migration discoverability. The parametrized `test_current_release_metadata_accepts_successors_and_rejects_mixed_inputs` supplies a successor case plus config drift, template drift, missing entry, duplicate entry, missing guide, and unlinked guide mutants. This keeps current-release protection while accepting a legitimate successor.
- `test_phase_e_preserves_rtbo_phase_d_and_protected_boundaries` no longer calls `_phase_e_ii_release_state(PROJECT_ROOT)`, so a current 3.1.0 composition is not rejected merely because six files differ from the 3.0.0 pre/post hashes.
- `test_phase_e_ii_release_destinations_are_protected_and_package_replays` still checks the immutable historical post-release bytes through `PHASE_E_II_RELEASE_COMMIT = 8fd8e40b734e9c439bb84721ef8bee441b9fcdd7`, and retains package replay and mutant checks. Historical acceptance is preserved at the historical boundary rather than imposed on the live tree.
- The global live-corpus doctor assertion was removed from `tools/tests/test_tfw_doctor.py`, while six controlled checks remain: operation/schema, deterministic read-only behavior, material versus indeterminate exit codes, unmatched/collision inputs, long-prose neutrality versus structural errors, and bounded capability/no full-build dependency. The removed assertion had treated one retained historical indeterminate event as a release-blocking clean-corpus condition, which is a corpus-health diagnostic rather than a current product invariant.

The commit's reported release result (549 passed/1 skipped in 715.86 s) is Coordinator-supplied evidence, not a rerun by this audit. The commit/tree identity is independently read from Git; no tests or builds were executed.

### G3: Existing pure families show what must remain

`docs/scripts/test_gen_docs.py:1-29` explicitly states that its transformation tests run without `mkdocs-gen-files` and mocks that import boundary. The hostile-title parametrization at lines 74-89 protects a real serialization failure mode, not incidental prose. This is a KEEP pattern: pure logic is tested directly and does not inherit a site build.

`tools/tests/test_tfw_doctor.py` retains six controlled tests after the CRUE commit. In particular, lines 116-128 preserve the distinction between material exit code 1 and indeterminate exit code 2; lines 131-146 preserve unmatched/collision handling; and lines 148-155 keep long prose exit-neutral while structural errors remain meaningful. These tests use small temporary fixtures and protect doctor semantics without asserting that the entire historical corpus is clean. They must remain even though the live-corpus gate was removed.

The integration module also contains explicit negative/counterexample tests that should not be deleted for count reduction. `test_no_board_shaped_regex_survives_in_the_generators` (195-210) protects removal of an obsolete implicit Task Board API; `test_the_adapter_retired_term_check_actually_fires` (1429-1441) verifies that a retired-term registry can produce a finding; and `test_phase_e_ii_package_mutants_are_rejected` (3012-3027) rejects malformed release patch markers, wrong version application, and corrupt release state. These are independent defect-detection consequences even when their current placement pays the autouse build cost.

There are also duplicate-looking historical entrypoints. For example, `test_phase_d_claude_release_config_history_and_prior_phases_are_byte_exact` (2487-2489) calls `test_phase_d_approval_epoch_protects_history_inputs_and_cumulative_prefixes` rather than asserting a new condition. The source comment says the old name is retained as a stable pytest entrypoint. This is not enough evidence for REMOVE: an external selector may depend on that name. It is a REWORK candidate only after selector compatibility is established; otherwise KEEP the compatibility entrypoint but avoid treating its repeated assertion as independent protection.

### Candidate map

| Candidate | Protected consequence | Legitimate change wrongly rejected / defect missed | Initial disposition |
|---|---|---|---|
| Module-wide `build_site` fixture | Generated HTML and link/rendering correctness for output-facing tests | A real docs generator or MkDocs integration defect could escape if the build is removed from HTML checks | KEEP for integration family; MOVE pure checks out of its scope |
| Pure Phase E copy, knowledge, writer, and package checks in `test_integration.py` | Exact file parity, immutable decisions, package replay and mutant rejection | Full build adds cost but does not add evidence; removing the assertions would miss parity or package corruption defects | KEEP assertions; MOVE/REWORK execution boundary |
| `_phase_e_ii_release_state(PROJECT_ROOT)` as a live-tree oracle | Historical 3.0.0 package epoch | A coherent later release such as 3.1.0 is rejected as “corrupt or mixed” | REMOVE live coupling; KEEP immutable historical checks |
| Global live-corpus doctor-clean assertion | None beyond a current whole-corpus cleanliness claim | A retained historical malformed event blocks an otherwise valid release | REMOVE global gate; KEEP controlled doctor semantics |
| Six controlled doctor tests | Schema, read-only behavior, semantic exit codes, collision handling, and bounded capability | Removing them could hide a material/indeterminate classification regression or make diagnostics mutate/build | KEEP |
| Historical pytest-name wrapper | Compatibility with selectors using the old test name | Removing it could break an external targeted command despite no new assertion | KEEP provisionally or REWORK after selector evidence; do not count it as independent protection |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| The primary avoidable coupling is the module-wide autouse site build around pure repository/Git/temp-tree checks. Current-vs-historical oracle separation and removal of the whole-corpus doctor gate preserve concrete protections while accepting legitimate current changes. | Exact complete census of every pure test under the integration module, selector compatibility for historical wrappers, and measured setup/body/process/review cost remain open. No expensive probe is authorized. |

**Sufficiency:**
- [x] External source used? — official pytest fixture documentation, linked above.
- [x] Briefing gap closed? — dimensions, candidate dispositions, protected consequences, counterexamples, KEEP cases, and simplest adequate execution boundary are identified.
- [x] Dimensions identified?

Stage complete: YES
→ User decision: Proceed to Extract after Coordinator review; do not run an expensive probe.
