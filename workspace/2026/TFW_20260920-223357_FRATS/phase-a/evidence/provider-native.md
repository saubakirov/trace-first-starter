# Phase A Provider-Native Ledger

> Post-Candidate recheck: 2026-09-21T17:14:20+05:00; owner-authorized continuation, TRACE only.

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

### Authenticated recheck

| Fact | Observation |
|---|---|
| Product / model | Claude Code `2.1.278`; `claude-sonnet-5` |
| Earlier authenticated attempt | session `9f17a3ba-79b0-4f0a-9186-326fa73a7ada` used Opus, exhausted its USD 0.50 ceiling without a final report, and recorded denied disallowed Bash calls; it contributes no P2 result |
| Native operation | exact `/tfw-handoff continuation` for Phase A and Candidate `1a9209530d7a939db1270e2f91dcef40a9f449e6`; requested title `EXEC · FRATS · A · PROBE`; native session `a42f2c99-9bc2-426a-9726-ab109e52f5c1` |
| Result | success in 4 turns; USD 0.2667536; no permission denials, repository writes or external messages |
| Carrier readback | correctly reported task `TFW_20260920-223357_FRATS`, lifecycle `RF`, coordinator route `codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf`, exact coordination authority and owner-direct activation |
| Native limits | model could not observe the wrapper-returned session id, set/read the requested title, or address a return directly to the Codex Coordinator; native `--resume` attempts returned `No deferred tool marker found` |
| Tool deviation | despite the read-only no-Bash instruction, the model disclosed one read-only Bash `find`; it made no write |
| Prohibited edge | no peer, owner or GATEWAY message was sent |

Recheck classification: P0 **PASS**, P1 **PASS**, P2 **PASS**, P3 **NOT DEMONSTRATED** and P4
**NOT DEMONSTRATED**. The original expired-OAuth result remains part of the ledger. The authenticated
bounded operation demonstrated exact carrier/authority readback, but neither an addressed vertical
return nor native continuation/terminal reliability.

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

### `agy` CLI recheck and single corrected readback

| Fact | Observation |
|---|---|
| Product / version | `agy` `1.2.7` |
| Native address | conversation `9b323e29-99dc-4934-86c3-e930bfca72bc` |
| Initial result | `SUCCESS`, but contradicted the carrier: it did not discover the repository skill, omitted lifecycle `RF`, treated the Coordinator as pending and replaced the exact authority with a generic user-global rule |
| Gate and correction | the contradiction was stopped and routed; the owner authorized exactly one corrected readback in the same conversation with explicit skill, status and TS paths; no third attempt was made |
| Corrected result | `SUCCESS`; opened the 22-line skill, 19-line status and 424-line TS; correctly reported skill `tfw-handoff`, task `TFW_20260920-223357_FRATS`, Phase A lifecycle `RF`, the exact coordinator route and coordination authority, and owner-only activation |
| Native limits | title metadata was not exposed; the result returned only to the invoking turn and was not an addressed send to the Codex Coordinator |
| Prohibited edge | named peer, foreign Coordinator, owner and GATEWAY edges and sent none |

Recheck classification: P0 **PASS**, P1 **PASS**, P2 **PASS**, P3 **PARTIAL** and P4 **NOT
DEMONSTRATED**. The same native conversation completed the owner-authorized correction, but did not
demonstrate an addressed vertical Coordinator return or a terminal checkpoint series.

## Contradiction check

The initial `agy` result contradicted the A3 carrier/routing model. The exact mismatch was stopped and
routed, and one owner-authorized correction in the same native conversation resolved the carrier
readback. Claude and `agy` still lack the addressed-return and terminal-series evidence needed for
full P3/P4; those absences are not relabelled as proof. No provider evidence establishes a reliability
rate.
