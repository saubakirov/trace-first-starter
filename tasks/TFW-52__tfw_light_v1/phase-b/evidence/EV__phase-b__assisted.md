# EV — TFW-52 / Phase B: Assisted

> **Date**: 2026-08-13
> **Author**: Codex (Executor)
> **Task**: TFW-52
> **TS**: [TS Phase B](../TS__phase-b__assisted.md)
> **Owner disposition**: Product accepted as successful on 2026-08-13 with the Codex lifecycle-hook limitation recorded, not waived as verified.

---

## Environment

| Field | Value |
|-------|-------|
| OS | Microsoft Windows 11 x64 |
| Codex | Desktop package `26.803.5235.0`; CLI/app-server `0.147.0-alpha.6.5` during the final lifecycle smoke |
| Deploy target | Standalone non-Git Assisted roots outside `steps-framework` |
| CI / Pipeline | Local structural assertions, handler fixtures, fresh-root smoke, Git diff checks |
| Product commits | `8557a32` (starter), `ac4c3a4` (standalone initialization and task intake) |
| Evidence retention | Raw external run roots and rollout files were no longer present at RF closure; exact observed outcomes below are reconstructed from the session trace. |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | The complete nine-file starter was copied to fresh non-Git roots without manual service-file edits. The user layer is Russian and standalone; `README.md` names the limits and is 531/700 words, `AGENTS.md` is 1038/1100. The owner subsequently exercised the starter and accepted the product direction after the standalone-init correction. | Repository plus fresh-root checks | VERIFIED | [`README.md`](../../../../editions/02-assisted/README.md), [`AGENTS.md`](../../../../editions/02-assisted/AGENTS.md), commits `8557a32`, `ac4c3a4` |
| E2 | AC-2 | Definitions for `SessionStart`, `PreCompact`, and `Stop`, cross-platform dispatch, one handler per platform, root discovery, idempotent checkpoint and one-shot Stop logic passed deterministic handler checks. Real trusted Codex Desktop sessions nevertheless produced no durable `HookStarted`/`HookCompleted`, handler-state log, or `additionalContext`. The updated runtime reproduced the same failure. Lifecycle execution is therefore not verified. | Codex Desktop `26.803.5235.0`, CLI `0.147.0-alpha.6.5`; earlier negative baseline `0.146.0-alpha.9.2` | BLOCKED | [`hooks.json`](../../../../editions/02-assisted/.codex/hooks.json), [`tfw-hook.ps1`](../../../../editions/02-assisted/.codex/hooks/tfw-hook.ps1), [`tfw-hook.sh`](../../../../editions/02-assisted/.codex/hooks/tfw-hook.sh); session IDs `019fe4cd-3e12-7380-adda-0852d46b0530`, `019fe5ab-b22b-7501-b2b0-a68cb09ae933` |
| E3 | AC-3 | The final contract requires orientation, trace-before-result, owner, AI role, desired result, criteria, status and backward plan; it explicitly forbids stopping at “task created”. Real automated Stop mismatch evidence was unavailable and the replacement manual run was not completed. | Static contract and deterministic handler only | DEFERRED | [`AGENTS.md`](../../../../editions/02-assisted/AGENTS.md) §§ «Ориентация в каждой задаче», «Перед первой долговечной записью» |
| E4 | AC-4 | The contract and owner’s basic use confirm ordinary reading is separated from durable work; an infrastructure-invalid P1 run left the root unchanged and gave the visible manual-fallback phrase. The full three-question live lane and `SessionStart active_task=none` proof were not completed. | One incomplete interactive session; static contract | DEFERRED | [`AGENTS.md`](../../../../editions/02-assisted/AGENTS.md) § «При старте»; session `019fe5bf-3e38-7342-a12e-28d24a14f72d` |
| E5 | AC-5 | Four local root fixtures passed: project root, nested cwd, absent marker refusal and competing-root refusal; no Git dependency is present. A fresh standalone root with the final `PROJECT.md` was also found from a nested directory and created neither `work/` nor `knowledge/inbox/`. | Local PowerShell handler fixtures; non-Git temporary root | VERIFIED | [`tfw-hook.ps1`](../../../../editions/02-assisted/.codex/hooks/tfw-hook.ps1), [`PROJECT.md`](../../../../editions/02-assisted/PROJECT.md) |
| E6 | AC-6 | The candidate/records/index topology and no-automatic-consolidation language are present. A completed live AC-8 candidate set was not collected. | Static product inspection | DEFERRED | [`knowledge/INDEX.md`](../../../../editions/02-assisted/knowledge/INDEX.md), [`AGENTS.md`](../../../../editions/02-assisted/AGENTS.md) § «Память и риск» |
| E7 | AC-7 | Deterministic secret-pattern handling passed local handler fixtures; the agent contract holds semantic categories and asks once before shared memory. The full two-run live risk lane and Stop publication check were not completed. | Local handler fixture plus static contract | DEFERRED | [`tfw-hook.ps1`](../../../../editions/02-assisted/.codex/hooks/tfw-hook.ps1), [`AGENTS.md`](../../../../editions/02-assisted/AGENTS.md) § «Память и риск» |
| E8 | AC-8 | The Light/Assisted prompts, inputs, order and metrics were planned and frozen, but the comparison was not executed after the lifecycle blocker and later owner-directed product corrections. No claim of measured difference is made. | Not run | DEFERRED | [`ONB`](../ONB__phase-b__assisted.md) § «Expected Evidence Plan» |
| E9 | AC-9 | `MIGRATION.md` specifies preservation, mapping, hashes and duplicate-contract refusal. The full live migration and byte comparison were not executed. | Static product inspection | DEFERRED | [`MIGRATION.md`](../../../../editions/02-assisted/MIGRATION.md) |
| E10 | AC-10 | Per-task writer ownership, separate profiles and automation identity are implemented in the contract. The two-session shared-root run was not executed. | Static product inspection | DEFERRED | [`people/README.md`](../../../../editions/02-assisted/people/README.md), [`AGENTS.md`](../../../../editions/02-assisted/AGENTS.md) |
| E11 | AC-11 | The exact visible fallback phrase and executable manual order are documented; the incomplete interactive session emitted the phrase and continued safely without writes when tools were unavailable. This verifies visible manual mode, not hook execution. | Repository plus session `019fe5bf-3e38-7342-a12e-28d24a14f72d` | VERIFIED | [`README.md`](../../../../editions/02-assisted/README.md) § «Если автоматические проверки недоступны», [`AGENTS.md`](../../../../editions/02-assisted/AGENTS.md) |

## Verdict

Evidence verdict: 3/11 VERIFIED, 7 DEFERRED, 1 BLOCKED, 0 N/A

Owner disposition: **SUCCESS WITH KNOWN LIMITATION.** The owner accepts the standalone Assisted product and requested closure. AC-2 remains truthfully BLOCKED on the tested Codex runtime; deferred lanes are not silently promoted to verified.

## Trace Notes

| Trace | Observation |
|-------|-------------|
| `019fe4cd-3e12-7380-adda-0852d46b0530` | Trusted clean-root baseline on CLI `0.146.0-alpha.9.2`: no lifecycle dispatch artifacts or additional context. |
| `019fe5ab-b22b-7501-b2b0-a68cb09ae933` | Updated-runtime smoke on CLI `0.147.0-alpha.6.5`: same conclusive absence after one frozen prompt; no retry. |
| `019fe5bf-3e38-7342-a12e-28d24a14f72d` | Downstream run stopped after P1 because a copied diagnostic CLI lacked its sibling code-mode host; product tree remained unchanged. |
| Owner feedback, 2026-08-09 | Basic use showed Assisted needed standalone initialization, project goals/values, AI role/mental model and active problem discovery. Commit `ac4c3a4` implements the correction. |
| Owner acceptance, 2026-08-13 | Owner reports basic operation is satisfactory and directs successful closure with hook caveats. |

---

*EV — TFW-52 / Phase B: Assisted | 2026-08-13*
