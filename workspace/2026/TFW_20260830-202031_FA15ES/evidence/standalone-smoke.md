# Standalone smoke — TFW_20260830-202031_FA15ES

> Date: 2026-09-02
> Executor task: `Executor | TFW_20260830-202031_FA15ES`
> Executor branch: `codex/tfw-fa15es-executor`
> Product commit: `626d77b5c3261dff493d15c7ce5862b9e036d10e`
> External fixture: `E:\TEMP\tfw-fa15es-final-626d77b-qa`

## Environment

| Field | Value |
|---|---|
| OS | Microsoft Windows 11 Pro 10.0.26200 (build 26200) |
| Shell | Windows PowerShell 5.1.26100.9278 |
| Python | 3.13.5 |
| Git | 2.42.0.windows.1 |
| Network/provider dependency | none; all fixtures local and synthetic |

## Copy and package census

Only `editions/02-assisted/` was copied to `standalone-assisted-1.6/` under the external fixture root. The copied tree contains exactly **24 files / 260,872 bytes**:

- 5 prompt-only skills, each with `SKILL.md` and `agents/openai.yaml` — 10 files;
- root contracts `AGENTS.md`, `CHANGELOG.md`, `MIGRATION.md`, `PROJECT.md`, `README.md`, `VERSION` — 6 files;
- `knowledge/INDEX.md` and `team/README.md` — 2 files;
- four practical template inputs, the artifact-only `build_a4.py`, and passive `assets/tfw-mark.svg` — 6 files.

Absent by census: `workspace/`, human/automation profiles, `project_id`, machine-local bindings/locks, private records, raster logo, maintenance JSON, overlay/theme CSS, lifecycle hooks, bytecode, temp/conflict copies, reparse points, and any executable besides the artifact-only A4 builder.

## Uninitialized scenario

| Check | Observation | Result |
|---|---|---|
| package state | `PROJECT.md` visibly uninitialized | PASS |
| participant state | `team/` contains only `README.md`; 0 profiles | PASS |
| task state | `workspace/` absent | PASS |
| knowledge state | generic empty `knowledge/INDEX.md` | PASS |
| version | exact `VERSION=1.6` | PASS |
| external dependency | no read of repository root, Full edition, `.tfw/`, or field source | PASS |

## Prompt/file lifecycle scenarios

Static prompt-contract checks and isolated synthetic files exercised:

- new and existing participant selection;
- missing/ambiguous identity and surname-collision human gates;
- current participant, task owner, and AI role as separate concepts;
- plan → handoff → independent review → human acceptance lifecycle;
- autonomous handoff/review owner inheritance without local participant guessing;
- fail-closed handling for invalid project/profile/binding state;
- stable active `workspace/` and `team/` paths with old container names only as migration inputs.

No shipped helper/runtime was invoked for those lifecycle behaviors; they remain prompt/file contracts.

## Initialized and protected-state scenario

The copied service set was placed beside synthetic initialized `workspace/`, `team/`, and `knowledge/` state. Pre/post manifests for all protected paths were byte-identical. Existing project identity and participant data stayed downstream and were not copied back into the clean starter.

## Artifact smoke

- `build_a4.py` executed from the external standalone copy and returned `pages: 4`.
- The generated HTML contained four page containers.
- The presentation contained four complete slide containers.
- All relative template assets resolved after copying the passive mark into the generated HTML's relative `assets/` location.
- Detailed visual and contrast results are in `template-render-audit.md`.

## Result and retention

Standalone verdict: **PASS**. The structured result is [fixture-results.json](attachments/fixture-results.json).

The final fixture root is retained until independent review. It is disposable after human acceptance; no product or task trace depends on its continued existence.
