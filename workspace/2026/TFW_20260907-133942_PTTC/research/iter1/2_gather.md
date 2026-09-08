# Gather — "What do we NOT know?"
> **Mindset:** Explorer. Map the unknowns before narrowing them.
> **Parent:** [HL-TFW_20260907-133942_PTTC](../../HL-TFW_20260907-133942_PTTC.md)
> **Goal:** Reach the simplest complete and coherent verification and closure system while preserving meaningful protection, honest completion and continuation.

## Dimensions

The investigation has four independent decision factors. The alternatives are deliberately left open for Extract and Challenge.

| Dimension | Alt A | Alt B | Alt C | Alt D _(if any)_ |
|-----------|-------|-------|-------|-----------------|
| D1: execution dependency boundary | Module-wide automatic site build | Explicit fixture only for output-dependent tests | No site build for pure text/Git checks | Separate integration invocation outside the pure-check path |
| D2: oracle time and authority | Exact historical snapshot hashes | Current semantic metadata and invariants | Immutable pinned package-commit preimages | Explicit rejection of mixed or corrupt states only |
| D3: evidence applicability | Reuse when relevant inputs, oracle and environment are unchanged | Targeted recheck of affected outputs | Independent Reviewer applicability check | Fresh broad rerun after any relevant change |
| D4: closure and return boundary | Capture markers and dispositions | Capture plus checks of changed accepted outputs | Bounded material-change return to the existing review route | Fresh review/knowledge cycle for every administrative correction |

## Findings

### G1: CRATM and CRUE causal timeline and cost boundary

The planning record separates several events that must not be collapsed into one “slow test” cause:

1. The CRATM Phase E transcript records collection of 529 tests in 0.39 seconds, a targeted Phase E run of 15 passed in 279.97 seconds, a strict MkDocs build with exit 0, and a final configured run of 528 passed and 1 skipped in 768.55 seconds. The planning HL separately records six late-round runs totalling 1962.73 seconds. These are observed command durations, not incident wall time, CPU time, tokens or money. The transcript also preserves an initial 526 passed / 1 skipped / 2 failed run in 721.91 seconds, where both failures were stale assertions requiring live Phase-D traces to equal the pre-K1 object even though approved K1 had appended knowledge markers. Source: [CRATM Phase E completion transcript](../../../TFW_20260902-111644_CRATM/phase-e/evidence/phase-e-completion-tests.txt) and [PTTC HL §2](../../HL-TFW_20260907-133942_PTTC.md).
2. The B–D → B–E incident therefore contains at least two distinct mechanisms: an oracle that rejected a coherent state after a legitimate knowledge transition, and a later repair process that spent repeated verification and coordination effort. The recorded 67 additions and 12 deletions in the final assurance correction show the correction boundary was larger than a one-character edit; they do not by themselves establish that all of the work was avoidable.
3. The attributed CRUE repair commit `a767b17072733dc856d4c73fa6a72277e1538ba5` (tree `06e466315a856ede01044b521d840647163014d4`) reports 549 passed and 1 skipped in 715.86 seconds on an isolated `codex/release-3.1.0` preparation. Its changed-path summary includes `docs/scripts/test_integration.py` and `tools/tests/test_tfw_doctor.py` plus five release/configuration files. It changes current-release verification toward semantic metadata, anchors historical postimages to an immutable release commit, and removes only the global live-corpus zero-findings doctor test while retaining bounded doctor checks. This is an attributed source, not a rerun, saved-master integration or publication receipt. Source: [CRUE RF](../../../TFW_20260906-190312_CRUE/RF-TFW_20260906-190312_CRUE.md), the committed diff at `a767b17072733dc856d4c73fa6a72277e1538ba5`, and the updated PTTC HL §2.

**Gather implication:** H1 has a confirmed structural coupling and a recorded cost boundary, but its material saving remains unquantified. The existing records support causal separation, not a fresh performance claim.

### G2: Fixture and oracle dependencies

In [`docs/scripts/test_integration.py`](../../../../../docs/scripts/test_integration.py#L20-L37), `build_site` is declared as `@pytest.fixture(scope="module", autouse=True)` and runs `python -m mkdocs build --config-file docs/mkdocs.yml` in a subprocess before yielding to the module’s tests. Because the scope is `module`, this is one setup per module/process, not one build per test; all tests in the visible scope inherit that shared setup. The same module contains `test_phase_e_knowledge_keeps_exact_rtbo_and_final_cratm_decisions` (around lines 2650–2720), which reads Git objects and `KNOWLEDGE.md` and mutates only in-memory strings; its assertions do not inspect generated HTML. The fixture nevertheless remains in its visibility scope. The official [pytest fixture API](https://docs.pytest.org/en/latest/reference/reference.html#pytest.fixture) states that module is a supported sharing scope and `autouse=True` activates a fixture for all tests that can see it. The official [MkDocs CLI reference](https://www.mkdocs.org/user-guide/cli/#mkdocs-build) defines `mkdocs build` as the documentation build and documents the default clean site output behavior.

This establishes an avoidable dependency edge: a pure text/Git knowledge assertion is coupled to a whole documentation build by module-level fixture scope. It does not establish the exact incremental cost of that edge, because the recorded command timings combine collection, one module fixture setup, test bodies, subprocess startup and other process work. The current test has structural and provenance protection: it rejects missing or duplicated decision rows, selected text mutations and corrupt historical SHAs. That detector sensitivity does not prove that every changed row changes decision meaning; authority and predicate analysis are still required. Removing the fixture edge must therefore preserve the demonstrated protection while changing only the execution dependency.

The current historical guard is a separate oracle issue. `test_phase_e_preserves_rtbo_phase_d_and_protected_boundaries` calls `_phase_e_ii_release_state(PROJECT_ROOT)` and accepts only exact pre-release or post-release hashes. `_phase_e_ii_release_state` raises on a mixed state. In the attributed CRUE diff, the outer live-tree call is removed and `test_phase_e_ii_release_destinations_are_protected_and_package_replays` instead compares the six postimages against the immutable `PHASE_E_II_RELEASE_COMMIT`. This changes the historical/current boundary without dropping the package replay and corruption checks.

### G3: Diagnostic gate and finite closure ownership

[`tools/tests/test_tfw_doctor.py`](../../../../../tools/tests/test_tfw_doctor.py#L78-L170) retains local, source-derived protection for the doctor interface: stable operations and schema, deterministic read-only output, distinct exit codes for material versus indeterminate findings, unmatched/collision inputs, long prose being exit-neutral, and the bounded capability surface. The removed `test_live_repository_check_tasks_is_clean_and_known_123_event_is_exit_neutral` asserted that the entire live repository returned exit 0 with empty material and indeterminate findings. That assertion converted a disclosed historical corpus condition into a release gate even though an indeterminate result can be an input to a release decision rather than proof of a product defect. The repair removes the global gate, not the doctor behavior or its controlled fixtures.

The existing review route is finite but has an identified post-capture boundary. [`review.md` Step 6–7](../../../../../.tfw/workflows/review.md#step-6-record-verdict-then-route-proposals) routes an approved result to `KNW`, runs `tfw-docs` and, where needed, `tfw-knowledge`, then permits `DONE` only when both markers are set and REVIEW §5 has no undisposed item. PTTC HL §2 records that this route has no explicit check for outputs changed by docs/knowledge. Thus the observed ownership is: Reviewer records and routes the verdict; Coordinator performs the authorized knowledge/documentation transition; task `status.md` carries the terminal state. The unresolved question is which changed accepted outputs need a bounded check before that existing route may close, and which material change must return to review.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| A module-scoped autouse fixture makes the whole MkDocs build an implicit prerequisite for pure knowledge/Git assertions; official pytest and MkDocs references confirm the relevant execution semantics. | No same-environment before/after measurement isolates setup, body, process repetition, attention or monetary/token cost; no new benchmark was run. |
| CRATM’s recorded failures distinguish stale historical/current assertions from implementation and coordination work; CRUE’s immutable repair source replaces the live snapshot gate with semantic current metadata and pins historical postimages, while removing only the global corpus-clean gate. | CRUE’s report has not been independently rerun or integrated into saved master; applicability must remain attributed and bounded to the inspected commit. |
| Review Step 6–7 defines existing Reviewer/Coordinator/status ownership, while PTTC HL §2 identifies the missing changed-output check after capture. | The minimal output set and material-change return condition require Extract and Challenge; no closure redesign is selected here. |
| Four independent dimensions are identified for the next stages. | Alternatives remain open; this Gather does not choose KEEP / REWORK / MOVE / REMOVE. |

**Focused OODA decision:**
- **External source used?** YES — official pytest fixture API and official MkDocs CLI reference, both tied to the concrete fixture question.
- **Briefing gap closed?** YES — the causal timeline, actual dependency edges, attributed CRUE source, evidence boundary and current closure ownership are mapped.
- **Dimensions identified?** YES — four independent factors, each with at least three alternatives.

Stage complete: YES
→ User decision: Awaiting Coordinator checkpoint direction before Extract.
