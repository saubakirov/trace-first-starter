# Field manifest — TFW_20260906-190312_CRUE / Phase A

> **Admission:** NOT FROZEN; prepared for Coordinator review; 0 field slots consumed.
> **Candidate:** `d6d26003972f7b18fe10d492960d0cbac9f0a3e8`
> **Baseline:** `8fd8e40b734e9c439bb84721ef8bee441b9fcdd7`
> **Owner authority:** approved TS revision 3, SHA `5dfed7af5c013d469df88254378f4e7da7867c15`

This file records only the bounded campaign inputs that can be prepared without starting a subject.
The Coordinator must append the frozen block after independently checking candidate reachability,
sanitization, copy roots, authentication, effective containment and the no-extra-attempt ledger.

## Required matrix before admission

| Slot | Project/provider | Immutable source snapshot | Observed installed state | Copy root | Status |
|---|---|---|---|---|---|
| `afd-claude` | AFD / Claude | `c58ed93bf29f0b02533e360defbdaccdb070fb0a` | `.tfw/VERSION = 2.1.0` | not created | mandatory, not admitted |
| `afd-codex` | AFD / Codex | `c58ed93bf29f0b02533e360defbdaccdb070fb0a` | `.tfw/VERSION = 2.1.0` | not created | mandatory, not admitted |
| `helpdesk-claude` | helpdesk / Claude | `40b196e3dd6f262470c1e1f2a14b862ecb986384` | `.tfw/VERSION = 2.1.0` | not created | mandatory, not admitted |
| `helpdesk-codex` | helpdesk / Codex | `40b196e3dd6f262470c1e1f2a14b862ecb986384` | `.tfw/VERSION = 2.1.0` | not created | mandatory, not admitted |
| `atamat-claude` | Atamat / Claude | `df40e667f2da3fd5a1b2cfcaa4c36f97e9255804` | `.tfw/VERSION` and `tfw.version = 2.0.0` | not created | conditional, not admitted |
| `atamat-codex` | Atamat / Codex | `df40e667f2da3fd5a1b2cfcaa4c36f97e9255804` | 2.0.0; migration coverage | not created | conditional, not admitted |

Original repository paths are recorded in the approved TS only; this manifest does not access them or
copy their current dirty state. A sanitized manifest must be appended before admission and must name
excluded credentials, private bindings, profiles, remotes, hooks, links and hazardous configuration
without exposing their contents.

## Neutral starting prompt

Each admitted subject receives the same material authority and candidate facts, with no CRUE answers,
walkthrough, expected outcome or earlier subject report:

> In this isolated copy, perform the approved `/tfw-update` from Candidate
> `d6d26003972f7b18fe10d492960d0cbac9f0a3e8` according to the pinned target workflow. Follow the
> copy's established project authority and safety boundary. Do not access an original repository,
> production service, external destination or credentials. After the attempt, return a short field
> report stating what you observed, what you changed or preserved, any question and answer, checks
> actually run, unresolved limitation, and the exact next action. Do not claim success for an
> unverified or stopped result.

The final frozen prompt must include the exact admitted copy root and safe command set, then be hashed
or preserved in the frozen manifest before the first updater start.

## Freeze gates

Before any slot is consumed, the Coordinator must record: native auth result without secrets, actual
model/tool versions and session identities, effective copy-only write and restricted-egress proof,
independent copy metadata and sanitized inventory, one unique copy root per slot, Claude-before-Codex
order per project, and the no-extra-attempt ledger. A preflight is not an updater attempt.

## Return harness gate — 2026-09-07

The Executor built and ran a task-local Docker harness with no host/original-project runtime mounts,
read-only rootfs, non-root UID `65532`, all capabilities dropped, `network=none`, and a Unix-socket
sidecar that returned exact-provider/host/port ALLOW/DENY decisions. Native Claude/Codex launchers were
also run with task-local restrictions excluding MCP/connectors, web/browser, plugins, remote-control and
agent-spawn surfaces. These observations do not prove that the native provider processes inherit the
container controls or use the sidecar socket; Docker's daemon profile is `unconfined`, and no safe
native provider boundary is available.

**Admission result:** NOT FROZEN; zero slots consumed; no sanitized field copies created; no updater or
original-project access authorized. `evidence/SOURCE-ADMISSION.md` is intentionally absent because the
Coordinator-owned admission condition was not met. See `harness/NATIVE-EXECUTION__20260907.md` for
raw harness and launcher observations.

## Real-route return result — 2026-09-08

The follow-up harness satisfied the transport portion of the gate for a bounded preflight: a
network-enabled sidecar accepted only provider-specific HTTP CONNECT over Unix sockets, while a
network-none non-root subject ran official Claude 2.1.143 and Codex 0.152.1 binaries against a
sanitized Candidate Git copy. Codex returned native `PREFLIGHT_ONLY` through observed
`chatgpt.com:443`; a direct `api.openai.com:443` CONNECT received 403. Claude opened
`api.anthropic.com:443` tunnels but produced no final response and logged only redacted JSON-parse,
Datadog and telemetry failures. These are native preflight observations, not field reports.

The gate remains NOT FROZEN: the Claude blocker prevents a two-provider field campaign, and the
Coordinator has not admitted any copy or slot. No `SOURCE-ADMISSION.md` was created. Slots consumed:
`0`; owner-comprehension request: none; aggregate field analysis: none; post-field correction: none.
The exact image, subject flags, observed domains and raw response/403 are in
`harness/NATIVE-EXECUTION__20260907.md`.
