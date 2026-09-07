# Native execution preflight — TFW_20260906-190312_CRUE / Phase A

> **Status:** native connection checks recorded; field admission remains NOT FROZEN; 0 field slots consumed.
> **Attribution:** Executor `robert`; no updater or field subject was started.
> **Recorded:** 2026-09-07, Asia/Qyzylorda

## Candidate and scope

- Baseline: `8fd8e40b734e9c439bb84721ef8bee441b9fcdd7`
- Replacement Candidate: `d6d26003972f7b18fe10d492960d0cbac9f0a3e8`
- Prior implementation Candidate remains reachable at `146876e279313a6a1a1680b0c7fffa699e30d28e`.
- This record covers bounded native launch attempts only. It does not admit a subject, create a field
  copy, invoke `/tfw-update`, access an original repository, or authorize an external effect.

## Native launch observations

### Claude Code

The first invocation omitted the prompt while using `--print` and returned CLI usage help. It is a
command-shape mistake, not a provider result, and is not counted as an attempt.

The corrected connection-only invocation used the task evidence harness as its only added directory,
`--bare --no-session-persistence --output-format json`, and an inline neutral prompt. The API-key
environment variable was unset; no secret or login action was attempted. The launcher returned JSON:

```text
Not logged in · Please run /login
duration_api_ms: 0
session_id: a599cd58-54e7-4ffd-ad02-9d8468bfcab4
uuid: 4062b9ba-1e7e-42ff-ae89-88337ac4388d
```

This is the expected authentication-selection result for the deliberately bare, API-key-free probe,
not an infrastructure blocker and not evidence of a field trajectory. Normal OAuth authentication
metadata was independently observed by the Coordinator on the Windows/WSL launch surfaces; this
Executor record does not reproduce or expose credentials.

### Codex

The connection-only command was:

```text
codex exec -s read-only --json "Connection-only preflight. Do not read or write project files and do not run an updater. Reply exactly PREFLIGHT_ONLY."
```

Observed result: exit 0, a completed turn with thread
`01a07cdb-43f7-7f02-81c7-ba0ad1bcccf0`, and agent message `PREFLIGHT_ONLY`. The launcher emitted a
PowerShell shell-snapshot unsupported warning. This establishes a bounded read-only connection
response only; it does not prove that the Docker controls below are inherited by the native launcher.

## Containment boundary

The previously recorded Docker probe remains the only effective-control observation: Docker 24.0.6,
Alpine image `sha256:d529dd0c6e5597ac7e4a3e2dea65c3fcc6173f4cae713c409265c1dd9914a11b`, network none,
read-only rootfs, all capabilities dropped, no-new-privileges, and a writeable task harness bind mount.
It observed `CapEff: 0000000000000000`, an empty route table, blocked rootfs writes and allowed harness
writes. Native Claude/Codex inheritance of those controls is not proven, and no allowlisted native
egress boundary is available in this phase.

## Admission disposition

| Item | Result |
|---|---|
| Native Claude connection | Observed; bare/API-key-free auth-selection result only |
| Native Codex connection | Observed; read-only `PREFLIGHT_ONLY` only |
| Native containment inheritance | **UNPROVEN** |
| Native updater run | Not started |
| Sanitized field copies | Not created |
| Field slots | `0` consumed; manifest remains NOT FROZEN |

Therefore AC-8/AC-9 native behavioral evidence remains **BLOCKED/DEFERRED**. The available local
source and synthetic assurance evidence is not upgraded into receiver behavior, provider comparison,
or owner-comprehension evidence by these connection checks.
