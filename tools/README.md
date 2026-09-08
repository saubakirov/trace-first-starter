# Upstream maintainer tools

This directory belongs to the upstream repository, not to the copied `.tfw/` Full payload
or `editions/02-assisted/`. Its Python and PyYAML requirement is therefore not a receiver
prerequisite and none of these commands is an ordinary lifecycle or build gate.

- `tfw_state.py` provides side-effect-free semantic readers used by upstream tests and
  diagnostics. Task-local carriers remain authoritative.
- `tfw_doctor.py` is a bounded, read-only diagnostic with exactly `status`, `check tasks`,
  `check project`, and `knowledge-pending`. It never repairs files. Exit `0` is a complete
  clean scoped read, `1` reports determinate structural findings, and `2` reports incomplete
  or indeterminate input. Advice and compatibility notes are exit-neutral.
- `migrations/2.0.0/` is the self-contained recovery bundle for the pre-2.0 board conversion.

Prepare an isolated maintainer environment. The documentation requirements are needed
for checks of generated output:

```bash
python -m venv .venv
python -m pip install -r tools/requirements.txt -r docs/requirements.txt
python -m pytest tools/tests/ docs/scripts/ -q --collect-only
python -m pytest tools/tests/ docs/scripts/ -q
```

## Selecting verification

Start with the change and the claim that could become false. Identify its relevant inputs,
test or other oracle, governing authority and environment; then choose adequate evidence.
Use the following commands from the repository root. A small diff can change a shared
parser, an approval rule or an expected result and therefore require broad verification.

| Change | Risk to inspect | Relevant selection / additional evidence |
|---|---|---|
| Plain text | Broken encoding or references in shipped instructions | `python -m pytest docs/scripts/test_repository_contracts.py -q`; for an isolated encoding claim, select `::test_no_shipped_text_carries_a_control_character` on that module |
| Parser or shared state reader | Different interpretation across callers, malformed input or lost compatibility | `python -m pytest tools/tests/test_tfw_state.py docs/scripts/test_gen_docs.py docs/scripts/test_runtime_context.py -q`; include output checks for changed rendering, task discovery or link behavior |
| Workflow instruction or adapter | Wrong role, authority, route, installed copy or actual permission | `python -m pytest docs/scripts/test_repository_contracts.py docs/scripts/test_runtime_context.py -q`; changed permission also needs a bounded native example and an independently formed challenge under the task's approved plan |
| Documentation or knowledge | Lost row identity, lineage or provenance; material meaning change; broken rendered navigation | Source contracts for source claims; independent reading against cited decisions for meaning and approved successors; `python -m pytest docs/scripts/test_integration.py -q` when the claim includes generated pages, links, navigation or presentation |
| Lifecycle or control-carrier behavior | Invalid transitions, attribution, recovery or closure | State-reader and runtime-context selections above, with relevant controlled cases in `tools/tests/test_tfw_doctor.py`; changed permission or closure behavior requires the task's behavioral evidence, not just matching text |
| Release input, migration or dependency | Mixed versions, broken package replay, receiver update or platform behavior | Release/package predicates in `test_repository_contracts.py`, relevant migration tests in `tools/tests/`, and configured broad checks for shared release/dependency effects; publication remains a separate authorized act |

`test_repository_contracts.py` reads source files, Git objects and temporary trees. It does
not import the output-test module or require `site/` or MkDocs. Its historical assertions
bind historical inputs; its current knowledge checks establish selected identity, lineage
and provenance. They cannot decide arbitrary prose's meaning or grant approval to a
successor. The independent semantic judgment must name the governing decision and reason.

`test_integration.py` checks generated output and always shares one fresh MkDocs build
per module/process. An existing valid `site/` is not evidence for changed inputs. Shared
fixture changes, test movement, changed oracles, parser/discovery/link changes, environment
or dependency changes, and unresolved cross-surface effects require checking the affected
callers and considering the complete suite. Run collection to detect missing selections;
no collected tests is not a passing observation.

Configured lint/build/test gates in `.tfw/project_config.yaml` and the task's governing
workflow/TS remain in force. This guide helps select targeted checks and assess reuse; it
does not waive those gates, authorize a larger experiment or change a workflow permission.
This repository's current lint/test gates are the collection and full-suite commands above.
Receiver projects use their own configured commands and authority; they acquire none of
this upstream corpus, Python, Git-history, pytest or MkDocs obligation.

## Reusing evidence

Record the claim, relevant input identities, oracle/authority, environment assumptions and
exact earlier evidence reference in the existing EV/RF. Inspect the actual dependency and
the result at the crossing; a matching enclosing commit or file count is insufficient.
Record what changed and why the cited result still applies, with independent review when
required by the governing workflow.

An unrelated TODO or trace edit does not expire evidence for unchanged claims. Changing a
relevant input, fixture, expected result or permission invalidates reuse for the affected
claim, even if its earlier run passed. Obtain the affected check or authorized judgment;
retain unrelated evidence that still applies. A new enclosing commit alone does not force
a complete rerun. Missing provenance, uncertain applicability or a required observation
that cannot fit the approved budget is unfinished work: preserve the result and return the
specific gap through the task's responsible Coordinator. Neither elapsed time nor this
guide supplies approval, and no evidence registry or cache is needed.

## Optional inspection

Examples of optional read-only inspection:

```bash
python tools/tfw_doctor.py --root . status
python tools/tfw_doctor.py --root . check tasks --format json
python tools/tfw_doctor.py --root . check project
python tools/tfw_doctor.py --root . knowledge-pending --format json
```

These reports are disposable projections. They do not replace `status.md`, journals, task
artifacts, or the tool-independent Knowledge Gate in `.tfw/workflows/knowledge.md`.
