# Phase A Provider-Native Ledger

> Date: 2026-09-21
> Probe: resolve Phase A state; invoke exact `/tfw-handoff`; apply/read back title when exposed;
> attempt one allowed vertical gate return; bound one prohibited direct edge without sending material work.
> Candidate: `1a9209530d7a939db1270e2f91dcef40a9f449e6`

Each provider is classified from its own native surface. Missing capability is a limit, not evidence
borrowed from another provider. No reliability percentage or cross-provider conclusion is made.

## Codex

| Fact | Observation |
|---|---|
| Product / version | Codex Desktop native task tools; CLI `codex-cli 0.152.1` |
| Native surface | user-visible local Codex tasks and task-addressed title/list/read/send/readback operations |
| Actual unit | Executor `codex:thread:local:01a0c3a2-c742-7962-a981-369effb5ac83` |
| Parent | Coordinator `codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf` |
| Title operation | `EXEC · FRATS · A` applied at onboarding |
| Readback | native task listing returned the exact Executor id, title, `active` state, project cwd, and separate `PLAN · FRATS` Coordinator id |
| Allowed edge | two direct status returns to the Coordinator; native send receipt returned that exact destination id |
| Prohibited edge | worker→peer/owner/GATEWAY was predeclared REFUSE and not sent |

P0 **PASS**: native title, list, read, addressed send and wait mechanisms are documented by the
available tool surface. P1 **PASS**: bounded title/addressed-send operations completed. P2 **PASS**:
native readback reconstructs source/destination/title/task and the local status supplies authority.
P3 **PARTIAL**: activation, title/readback and vertical status return were observed; a full correction,
continuation and terminal series was not manufactured for this probe. P4 **NOT DEMONSTRATED**: Phase A
is not a completed end-to-end multi-role reliability trial.

## Claude Code

| Fact | Observation |
|---|---|
| Product / version | Claude Code `2.1.273` |
| Native documentation | `claude --help` exposes `--name`, `--session-id`, `--resume`, `--bg`, `agents --json`, read-only tool selection and print-mode JSON |
| Attempt | exact `/tfw-handoff` owner-direct Phase A probe, named `EXEC · FRATS · A · PROBE`, tools limited to Read/Glob/Grep, no permission prompts, USD 0.25 ceiling |
| Native result | exit 1 before inference; JSON returned session id `ca47c93f-db3f-423d-8598-a7b406c6ccd6`, zero tokens/cost, and expired OAuth authentication |
| Readback | `claude agents --all --json --cwd ...` returned `[]`; no persisted address or title was observable |
| Prohibited edge | no peer/owner/GATEWAY send was attempted |

P0 **PASS** for documented native session/title/resume/background/readback mechanisms. P1 **FAILED AT
AUTHENTICATION**: the bounded operation did not reach model execution. P2 **NOT DEMONSTRATED**: the
failed print session was not present in agent readback. P3 **NOT DEMONSTRATED** and P4 **NOT
DEMONSTRATED**. Unsupported claims: title application, exact route send, checkpoint series and
end-to-end reliability. The authentication failure is preserved as the bounded native result.

## Antigravity

| Fact | Observation |
|---|---|
| Product / version | Antigravity `1.107.0`, build `15487b3041e65228cae24980a3f796c905ef582c`, x64 |
| Native documentation | `antigravity chat --help` exposes `ask`, `edit`, and `agent` modes plus new/reused window selection; it exposes no CLI session id, title, addressed send, wait, or chat readback |
| Attempt | `chat --mode ask --new-window` with the exact `/tfw-handoff` Phase A read-only probe; CLI exit 0 |
| Native operation readback | `antigravity -s` showed running Antigravity window processes and the exact chat argv |
| Conversation readback | unavailable: the CLI printed no unit/address/result and the local computer-use surface exposed no native app inventory; its launch API was unavailable |
| Prohibited edge | no peer/owner/GATEWAY send was attempted |

P0 **PASS WITH LIMITS** for the documented chat/window launch surface. P1 **PASS ONLY AS WINDOW
LAUNCH**; no claim is made that the model completed the prompt. P2 **NOT DEMONSTRATED** because no
native unit address, title or conversation readback was exposed. P3 **NOT DEMONSTRATED** and P4 **NOT
DEMONSTRATED**. Unsupported claims: exact activation receipt, title application/readback, vertical
send, continuation, terminal return and end-to-end reliability.

## Contradiction check

No observed native result contradicted the A3 carrier/routing model. Claude and Antigravity lacked
evidence needed for higher stages; those absences remain explicit limits and are not relabelled as
proof. Codex evidence is bounded to this live phase and does not establish a reliability rate.
