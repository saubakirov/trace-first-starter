# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260907-133942_PTTC](../../HL-TFW_20260907-133942_PTTC.md)
> Goal: Identify the simplest complete and coherent verification design by removing accidental test coupling and duplicated obligations while preserving meaningful defect detection and honest completion.

## Configuration Space

The four Gather dimensions yield 4^4 = 256 nominal combinations. The following representative rows preserve every alternative and include the non-obvious combinations that change the predicate itself independently of its execution boundary. C10 and C11, in particular, were not proposed as a single configuration in the Briefing: they pair a pure no-build route with a predicate-level rework rather than assuming that moving a check is sufficient.

| Config | D1: contract being protected | D2: execution dependency | D3: evidence source | D4: disposition |
|--------|------------------------------|-------------------------|--------------------|----------------|
| C1 | Current semantic invariant | Module-wide autouse MkDocs build | Current working tree | KEEP |
| C2 | Current semantic invariant | Explicit integration fixture for HTML-output tests | Current working tree | REWORK |
| C3 | Current semantic invariant | Pure no-build test module | Current working tree | MOVE |
| C4 | Current semantic invariant | Direct bounded helper or subprocess check | Synthetic `tmp_path` fixture and mutants | REWORK |
| C5 | Historical acceptance or release package | Module-wide autouse MkDocs build | Immutable Git baseline/release ref | KEEP |
| C6 | Historical acceptance or release package | Explicit integration fixture for HTML-output tests | Immutable Git baseline/release ref | MOVE |
| C7 | Historical acceptance or release package | Pure no-build test module | Immutable Git baseline/release ref | REWORK |
| C8 | Structural/copy/parity invariant | Pure no-build test module | Current working tree | KEEP |
| C9 | Structural/copy/parity invariant | Direct bounded helper or subprocess check | Synthetic `tmp_path` fixture and mutants | REWORK |
| C10 | Live-corpus health diagnostic | Module-wide autouse MkDocs build | Live repository corpus | REMOVE |
| C11 | Live-corpus health diagnostic | Pure no-build test module | Live repository corpus | MOVE |
| C12 | Current semantic invariant | Pure no-build test module | Immutable Git baseline/release ref | REWORK |
| C13 | Historical acceptance or release package | Direct bounded helper or subprocess check | Current working tree | KEEP |
| C14 | Structural/copy/parity invariant | Explicit integration fixture for HTML-output tests | Current working tree | MOVE |
| C15 | Live-corpus health diagnostic | Direct bounded helper or subprocess check | Live repository corpus | REMOVE |
| C16 | Historical acceptance or release package | Pure no-build test module | Synthetic `tmp_path` fixture and mutants | KEEP |

## Findings

### E1: Fixture placement and predicate necessity are separate decisions

The Gather correction is precise: `@pytest.fixture(scope="module", autouse=True)` invokes one shared fixture instance for the module in a pytest process, not one MkDocs build per test. The [official fixture reference](https://docs.pytest.org/en/stable/reference/reference.html#pytest.fixture) defines module scope and `autouse`; the [official explanation](https://docs.pytest.org/en/stable/explanation/fixtures.html#autouse-fixtures-fixtures-you-don-t-have-to-request) states that an autouse fixture is executed for every test in its scope. Therefore the avoidable cost is a fixed module-level setup dependency inherited by pure tests, not N builds multiplied by the number of test functions.

That placement finding does not answer whether each predicate is useful. Moving a predicate to a no-build module preserves a useless assertion if its only job is to reproduce wording or an obsolete snapshot. Conversely, removing the fixture from an HTML-output predicate would remove real integration protection. The correct unit of simplification is the pair `(predicate, required evidence)`: first establish the consequence, then place the check at the smallest boundary that supplies it.

### E2: Exact knowledge-row locks preserve lineage but overreach when they freeze prose

`test_phase_d_closure_visible_knowledge_uses_approval_epoch_not_product_baseline` (2398-2412) checks that current `KNOWLEDGE.md` contains exactly one D82 and D83 row, preserves the approved D82/D83 distinction, and does not retain the obsolete D82 Agent Team wording. This has a current semantic purpose: it prevents a historical approval row from silently being substituted for the later owner-approved decision.

`test_phase_e_knowledge_keeps_exact_rtbo_and_final_cratm_decisions` (2650-2724) goes further. It reads complete D82/D83/D84 rows from immutable refs, requires byte-for-byte row equality in candidate fixtures, requires phase-label changes to land in the right row, and rejects duplicates, deletions, swaps, and altered commit addresses. The mutants prove that the predicate fires, but they do not prove that every explanatory phrase and citation field is itself a current invariant. A harmless clarification, source-list extension, or wording correction can be rejected even when decision identity, ownership, phase, and cited immutable source remain valid.

The simpler adequate alternative to test in Challenge is a semantic contract over the protected fields: unique decision IDs, the expected current phase/task identity, required immutable source references, and the absence of the known superseded claim. Preserve the full historical rows as knowledge, but do not automatically make their entire prose a live byte oracle. The exact-row test is therefore a REWORK candidate, while the narrower current lineage check is a provisional KEEP candidate. This is a predicate-level distinction, not a request to delete knowledge or weaken authority.

### E3: Regex and retired-string guards have different consequence bars

`test_no_board_shaped_regex_survives_in_the_generators` (195-217) is a static anti-cause guard against reintroducing the retired Task Board parser. It protects an architectural boundary, but its regex only detects one recognizable source spelling. It cannot prove that an equivalent parser written with different syntax is absent. `test_generators_do_not_read_the_root_readme_for_task_state` (220-231) is closer to the behavioral boundary because it requires `tfw_state.read_status` and rejects active README reads in the task-landing function; generated-output checks then cover actual rendering. The board-regex predicate may still be useful as a cheap defense-in-depth guard, but a negative mutant or a passing string assertion is not proof that the guard is the right oracle. Challenge must compare the semantic source check, output check, and syntax guard rather than retaining all three by default.

The retired-wording family has a stronger direct consequence. `test_no_normative_file_states_a_retired_rule` (1348-1377) scans only files a reader acts on; `test_no_adapter_file_states_a_retired_rule` (1387-1413) scans the separately shipped adapter surface. Their shared registry is not an accidental duplicate because the two surfaces can diverge and a receiver may read only the adapter. The comments explicitly distinguish live instruction from historical narration and exclude changelog records. These predicates do not prove agent behavior, but they do protect against shipping contradictory instructions. Their `test_the_retired_rule_check_actually_fires` and `test_the_adapter_retired_term_check_actually_fires` probes establish that the scanners can detect a planted stale term; they do not by themselves establish that every registered term is necessary. Initial disposition: KEEP the consequence checks, MOVE them out of the MkDocs fixture, and challenge individual registry rows for obsolete or duplicated scope.

### E4: Duplicate function names are a real lost-predicate defect, not merely duplicated cost

Bounded `rg` over the module finds multiple same-name definitions with different bodies:

- `test_phase_d_claude_release_config_history_and_prior_phases_are_byte_exact` is defined at 2143-2156 as a full protected-history byte check, then defined again at 2488-2489 as a wrapper around `test_phase_d_approval_epoch_protects_history_inputs_and_cumulative_prefixes`.
- `test_phase_d_literal_value_assurance_and_trace_boundary_is_complete` is defined at 2117-2125 and again at 2305-2321 with different baseline/approval checks.
- `test_phase_d_workflow_copies_and_codex_managed_receiver_are_exact` is defined at 2128-2140 and again at 2336-2354 with different Git/current/receiver comparisons.
- `test_phase_d_added_product_lines_do_not_leak_provider_names_or_apis` is defined at 2159-2170, while a later same-purpose name at 2434-2450 carries a different approval-epoch and named-exception contract; related wrappers call the later predicate.

In Python, the later definition binds the module name used by pytest collection; the earlier body is not an independently collected test under that name. The repository search found no command, workflow, or documentation consumer of the historical wrapper name beyond these two definitions. Thus the evidence does not justify preserving the wrapper as an external compatibility obligation. The protected unique assertions, however, must not be discarded: the simplest adequate disposition is to give materially different predicates unique names, remove only a no-op wrapper if no real selector consumer is found, and then run the appropriate review/test route later. This is a concrete missed-defect risk caused by duplication, not an inference from runtime cost.

### Candidate map

| Candidate predicate | Protected consequence | Wrong rejection or missed defect | Simplest adequate disposition to challenge |
|---|---|---|---|
| Module-wide autouse build | Real generated HTML and link/rendering behavior | Removing it from HTML checks misses generator/build defects; retaining it around pure checks wastes fixed setup | KEEP for output tests; MOVE pure predicates |
| Exact D82/D83/D84 row equality | Decision lineage and historical attribution | Harmless explanatory prose/citation change can be rejected; a pass still does not establish broader knowledge meaning | REWORK to semantic fields plus immutable source refs |
| Board-shaped regex guard | Prevent reintroduction of a retired parser pattern | Equivalent parser syntax can evade the regex; current pass is not behavioral proof | Challenge against source/output predicates; KEEP only if residual consequence is concrete |
| Normative and adapter retired-wording scans | Receiver does not receive contradictory live instructions | Removing one surface scan misses stale instruction in the other; string scan does not prove agent compliance | KEEP consequence checks; MOVE out of build; review registry rows |
| Duplicate same-name Phase D tests | Historical/approval/copy invariants actually execute | Earlier full predicates are overwritten and silently uncollected | REWORK names; remove only no-consumer wrapper |
| Global live-corpus doctor-clean assertion | Whole-corpus cleanliness | Retained historical malformed input blocks valid work without protecting current product output | REMOVE release gate; KEEP controlled doctor semantics |

## Checkpoint

| Found | Remaining |
|---|---|
| Predicate usefulness is independent of fixture placement. Exact knowledge rows can overfreeze prose; regex guards are syntactic rather than behavioral; retired-wording scans protect live instruction surfaces; and duplicate function names can suppress earlier unique predicates. The simplest design separates HTML integration, pure structural checks, immutable historical checks, and optional diagnostics by consequence. | Challenge must test the surviving configurations against concrete harmful-subtraction counterexamples, decide which semantic fields are sufficient for knowledge lineage, and confirm whether any regex/registry guard has a consequence not already covered by a simpler check. No run or expensive probe is authorized. |

**Sufficiency:**
- [x] External source used? — official pytest fixture documentation, linked in E1.
- [x] Briefing gap closed? — predicate-level necessity, counterexamples, KEEP candidates, duplicate suppression, and simpler alternatives are explicit.
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: Proceed to Challenge after Coordinator review; retain the bounded scope and do not run a probe.
