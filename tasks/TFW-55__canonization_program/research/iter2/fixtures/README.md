# TFW-55 Iteration 2 — Frozen Extract fixtures

Status: **FROZEN FOR COORDINATOR REVIEW — NO CRITIQUE RUNS EXECUTED**

This directory freezes the matched source packets and evaluation procedure prepared during Extract. It is research instrumentation, not evidence and not an implementation artifact.

- `frozen_design.json` is the normative machine-readable fixture. Packet strings, cases, expected-under-fixture answers, rubric, blind labels, seed, and run order are exact.
- `SHA256SUMS` freezes the design bytes after Extract. Any later packet change invalidates the hash and requires returning to the Extract gate.
- Challenge may instantiate fresh isolated Codex tasks only after the coordinator closes Extract. Each task receives exactly one blind variant assembled by the declared rule; it receives no answer key, configuration name, project history, or founder intent.
- Raw prompts, assembled packet, output, runtime/model metadata, and score must be preserved in Challenge. No run may be discarded or rerun selectively.
- The answer key tests consistent application of the provisional rule. It is not evidence that the rule or category is true.
- Synthetic non-code cases test coherence/generalizability only. They are not evidence of real adoption.

External source versions are declared inside the design. The key category counter-control is the November 2020 Scrum Guide: Scrum calls itself a lightweight framework, requires its core composition, and says a partial implementation is not Scrum. A usable boundary therefore does not by itself establish a methodology or discipline.
