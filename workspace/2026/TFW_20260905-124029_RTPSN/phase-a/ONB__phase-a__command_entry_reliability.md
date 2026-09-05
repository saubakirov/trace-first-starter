# ONB — TFW_20260905-124029_RTPSN / Phase A: Command Entry Reliability

> **Date**: 2026-09-05
> **Author**: Codex (Executor) · on behalf of `saubakirov`
> **Status**: 🟠 ONB — AG authorized; no blockers
> **Parent HL**: [Phase A derivation](HL__phase-a__command_entry_reliability.md)
> **Master HL**: [Role, Task, and Phase Session Naming](../HL-TFW_20260905-124029_RTPSN.md)
> **TS**: [Phase A command entry reliability](TS__phase-a__command_entry_reliability.md)
> **Approval**: `8866090960cb403e5254bf017bb2423b8171b0f2`

---

## 1. Understanding

Phase A must add a safe, explicit Codex CLI evaluation harness and complete the fixed 54-valid-run comparison of current, strengthened, and direct entry arms before applying the approved production decision rule. The work must also make the universal entry sequence and six-level claim boundary inspectable across all 11 commands and four manifest adapters, while retaining one canonical workflow and one Role Lock per command. The current thin proxy is the least-regret production default; strengthened wording may ship only if every AC-4 threshold and AC-5/AC-6 gate passes, while a direct/full-copy material win stops production selection for a new TS.

## 2. Entry Points

- `.tfw/adapters/manifest.yaml` — tooling-only authority for the exact 11 commands, four adapter routes, roles, sources, and targets.
- `.tfw/conventions.md` heading `Tool Adapter Pattern` — approved VALUE owner of the universal pre-action sequence and evidence ladder.
- `.tfw/adapters/README.md` and `.tfw/adapters/codex/README.md` — approved VALUE documentation surfaces for adapter and Codex-specific claim boundaries.
- `.tfw/adapters/codex/skills/tfw-*/SKILL.md` plus `.agents/skills/tfw-*/SKILL.md` — 11 byte-exact source/installed pairs; conditional VALUE only after the AC-4 decision.
- `docs/scripts/test_runtime_context.py` — existing `SourceTree`, unique-heading, read-graph, semantic-mutant, Role-Lock, and NUL-safe accounting helpers.
- `docs/scripts/test_integration.py` — existing manifest, clean-receiver, installed-copy parity, role, and plural-Antigravity checks.
- `docs/scripts/command_entry_eval.py` and `docs/scripts/test_command_entry_eval.py` — approved new ASSURANCE harness and offline test surfaces.
- `workspace/2026/TFW_20260905-124029_RTPSN/phase-a/evidence/` — TRACE-only raw runs, independent summary, topology, counts, test output, and EV.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The owner-approved TS fixes the matrix, arms, model/effort, 54-valid-run denominator, decision rule, scope denominator, ceilings, and production authority. The explicit AG grant authorizes execution when the ONB has no blockers.

## 4. Recommendations (suggestions, not blocking)

1. Reuse the manifest and the existing `SourceTree`/receiver helpers as the only topology inputs; independently constructed fixture expectations and mutants will prevent the harness from grading against its own generated prose.
2. Keep raw CLI events append-only in JSONL and perform the production decision in a separate `summary --check` path so every numeric and terminal claim can be recomputed without another model call.
3. Treat CLI schema/telemetry absence as a metric-local `N/A`, but fail a run as infrastructure-invalid when required observable event or Git-diff evidence is missing; retain every invalid attempt without changing the 54-valid-run denominator.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Codex CLI option names or JSONL event schemas may differ from the planned interface. The harness must probe version/help, retain raw output, redact credential-bearing fields, and fail closed before counting a run valid.
2. Fixture cleanup on Windows can fail when a subprocess retains a handle. Temporary roots must be resolved and checked as outside the repository before cleanup, and residue must be reported rather than deleted broadly.
3. Token ceilings cannot be enforced prospectively if the CLI omits usage until run completion. The harness must refuse the next call once reported cumulative usage reaches the ceiling and preserve the exact limitation; it must not invent per-run usage.
4. The repository is checked out at a detached approval commit. Commits remain valid, but every commit must use full status plus `git commit --only` with explicit Phase-A paths so no shared-index content is captured.

## 6. Inconsistencies with Code (spec vs reality)

No blocking inconsistency. The approved new harness/test files are absent as expected; the 11 current Codex source skills and their 11 installed copies are byte-identical; the manifest still declares exactly 11 commands and four adapters; and the approved VALUE selector has no baseline-to-approval delta. Cursor and plural Antigravity receivers are absent from this checkout exactly as the TS says and therefore can support only clean-receiver structural evidence, not live-host claims.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|---|---|---|
| 1 | `.tfw/README.md` NS1 | ✅ | Applied | Evidence, state, Candidate, EV, and RF must let the next authorized role reproduce the result without this chat. |
| 2 | `.tfw/README.md` Methodology Values and Success Criteria | ✅ | Applied | Structural tests and immutable raw evidence expose violations; names guide behavior but do not count as compliance; the Candidate must be complete and inspectable. |
| 3 | `knowledge/philosophy.md` F18 | ✅ | N/A for Phase A wording | Phase A measures entry behavior and does not implement the Phase B session-title vocabulary that this naming principle informs. |
| 4 | `knowledge/philosophy.md` F38 and F45 | ✅ | Applied | Reuse existing authorities and test surfaces, add only the approved harness/evidence, and retain the baseline when extra entry prose has no measured value. |
| 5 | `KNOWLEDGE.md` D15 and D54 | ✅ | Applied | Keep Codex skills as thin routers and measure parity as a behavioral promise without treating file-layout similarity as proof of behavior. |
| 6 | `KNOWLEDGE.md` D73–D75 | ✅ | Applied | Preserve workflow-owned selective reads, one manifest, four-adapter/11-route topology, one role per command, and the RCFR context reductions. |
| 7 | `.tfw/conventions.md` Tool Adapter Pattern and Role Lock Protocol | ✅ | Applied | Full copies remain exact; Codex skills dispatch; the canonical workflow binds the role and owns the algorithm before task action. |
| 8 | `knowledge/convention.md` F4 and F19 | ✅ | Applied | Encode the universal boundary as an executable ordered sequence and, only if selected, synchronize one consistent strengthened skeleton across all 11 pairs. |
| 9 | `knowledge/process.md` F3, F4, F7, F27, F30, F43 | ✅ | Applied | Use numbered gates, durable traces, explicit resume/stop fixtures, observable enforcement, and place the absence/limitation rationale where the adapter reader encounters it. |
| 10 | Iteration 1 RES D1–D8 | ✅ | Applied | Preserve CRATM as uncovered path, RTPSN as post-load noncompliance, H3 as refuted, H4 as pre-trial inconclusive, and current thin proxy as least-regret baseline. |
| 11 | Iteration 2 RES D1–D10 | ✅ | N/A for implementation | Phase A preserves but does not implement the selected naming grammar, rename placement, `LEAD`, collision suffix, or separator behavior. |

Additional relevant items from the Phase HL Knowledge Applications were read and applied: `README.md` How It Works; `knowledge/philosophy.md` F4, F24, F32, F43; `knowledge/convention.md` F5; `knowledge/process.md` F37; `knowledge/constraint.md` F2 and F12; and `knowledge/risk.md` F1. Together they require structural gates, one source of truth, method-and-revision-bound measurements, bounded prompt growth, repository-owned obligations, architecture over symptom patches, and explicit-path commit discipline.

## 8. Execution Authority and Scope Check

- Mode: AG, explicitly granted in the approved TS and Coordinator handoff.
- Acting handle: `saubakirov`, the only participant profile in `team/`; `via: codex`.
- Immutable VALUE denominator: 25 logical files / 800 touched text LOC.
- Configured soft prompts: 50 VALUE files / 5,000 touched text LOC; owner escalation at 50 files or 1,600 LOC from the immutable denominator.
- Approved Baseline: `7bc0f30736ff1456c5d9dd74286a4e3a94c63361`.
- Approved TS/authority: `8866090960cb403e5254bf017bb2423b8171b0f2`.
- Current disposition: three unconditional VALUE files; the 22 skill paths remain excluded unless AC-4 selects strengthened. No added VALUE path, protected-boundary change, or growth from planned zero is authorized.

---

*ONB — TFW_20260905-124029_RTPSN / Phase A: Command Entry Reliability | 2026-09-05*
