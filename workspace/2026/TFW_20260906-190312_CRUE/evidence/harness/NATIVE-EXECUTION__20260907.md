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

## Bounded launcher-containment harness

The smallest safe container route was built from the locally available `python:3.13-slim` image with
`--pull=false --network none`; no host or original-project path was mounted at runtime. Harness image:
`sha256:ab96f92ce8e1fa156d07a7e75da2073a9a67d6956ea8d72a5392b16e84f10a24`.

Exact runtime command:

```text
docker run --rm --network none --read-only --user 65532:65532 --cap-drop ALL --security-opt no-new-privileges --pids-limit 64 --tmpfs /run/tfw:rw,noexec,nosuid,nodev tfw-crue-native-harness:20260907
```

Independent `docker inspect` of the created container recorded:

```text
User=65532:65532 Readonly=true Network=none CapDrop=["ALL"] SecurityOpt=["no-new-privileges"] Binds=null Mounts=[] Tmpfs={"/run/tfw":"rw,noexec,nosuid,nodev"}
```

The in-container sidecar used only the Unix socket `/run/tfw/provider-connect.sock` and checked exact
provider/host/port tuples before any connect decision. Raw result:

```json
{"cap_eff": "0000000000000000", "gid": 65532, "results": [{"decision": "ALLOW", "host": "api.anthropic.com", "port": 443, "provider": "claude"}, {"decision": "DENY", "host": "api.openai.com", "port": 443, "provider": "claude"}, {"decision": "ALLOW", "host": "api.openai.com", "port": 443, "provider": "codex"}, {"decision": "DENY", "host": "api.openai.com", "port": 80, "provider": "codex"}], "rootfs_write_blocked": true, "uid": 65532, "unix_socket": "/run/tfw/provider-connect.sock"}
```

This proves the sidecar policy and container controls, not native provider inheritance: the actual
Windows Claude/Codex launchers are not inside this container and no host executable, auth store,
original project or provider socket was mounted into it. Docker reports the daemon security profile as
`unconfined`; the harness therefore does not claim a complete kernel-level native boundary.

## Native restricted-access checks

Claude's supported restriction surface was verified with `--bare`, `--strict-mcp-config` pointing to
the task-local empty `empty-mcp.json`, `--no-chrome`, `--disable-slash-commands`, `--tools ""`,
`--no-session-persistence`, and a task-harness `--add-dir`. It returned the no-auth result with
`session_id=a0ffdbed-6313-4246-adb9-234808a249e8`, `uuid=0e7dbec2-bdf4-4f52-a3e6-fdf082e96774`,
`duration_api_ms=0`, and `Not logged in · Please run /login`. No MCP/plugin/web/Chrome tool ran.

Codex's corrected restricted command used a task-local `CODEX_HOME` (not the user config),
`--ignore-user-config --ignore-rules --ephemeral --sandbox read-only`,
`-c 'web_search="disabled"'`, and disabled `plugins`, `plugin_sharing`, `remote_plugin`,
`browser_use`, `browser_use_external`, `browser_use_full_cdp_access`, `computer_use`, `multi_agent`,
`in_app_browser`, `in_app_chat`, `in_app_local_automation`, `tool_call_mcp_elicitation`,
`skill_mcp_dependency_install`, and `unbounded_connection_retries`. No plugin warm-up request appeared
in the corrected run. It returned a native thread `01a07d1a-e685-75d1-9e99-5ebd15056bd1` and repeated
`401 Unauthorized`/missing bearer responses from `wss://api.openai.com/v1/responses`; the PowerShell
shell-snapshot warning remained. The earlier `web_search_request` deprecation message was a config
correction, not a provider result. The task-local rollout directory was moved out of the worktree after
capture; no user/global settings were copied or changed.

These checks exclude unrelated MCP/connectors, hosted web/browser, plugin, remote-control and agent-
spawn surfaces at the launcher configuration level, but they still do not prove the exact-provider
sidecar is used by the native provider process. AC-8 remains blocked; no `SOURCE-ADMISSION.md` is
created, the field manifest remains NOT FROZEN, and zero field slots are consumed.

## Real HTTP CONNECT/native return — 2026-09-08

The bounded return used a network-enabled sidecar and a network-none subject connected only by a
Docker-managed volume carrying two Unix sockets. No host path, original-project mount or credential
store was mounted into either container. The subject ran as UID/GID `65532:65532`, read-only rootfs,
`CapDrop=["ALL"]`, `no-new-privileges`, `pids-limit=128`, and `network=none`; the sidecar used the
same non-root/read-only/cap-drop controls with Docker bridge networking.

The final image digest was `sha256:02246d09d4b7a6185148c9d37b7005975a5e68d6ba6ba4da1afaba37dcf8c594`.
It contained Claude 2.1.143, Codex 0.152.1-linux-x64, Git, `rg`, the Codex code-mode host, and a
sanitized Git copy of Candidate `d6d26003972f7b18fe10d492960d0cbac9f0a3e8`.

The sidecar accepted only provider-specific HTTP CONNECT to port 443 and forwarded bytes
bidirectionally without TLS interception or body logging. Codex used the observed OAuth host
`chatgpt.com` and returned native `PREFLIGHT_ONLY` through the route. A direct non-allowlisted
`api.openai.com:443` CONNECT through the Codex relay returned `HTTP/1.1 403 Forbidden`.

Claude opened native tunnels to `api.anthropic.com:443` and the sidecar denied
`http-intake.logs.us5.datadoghq.com:443`, but no final Claude response arrived within 90 seconds.
Redacted debug metadata recorded `JSON Parse error: Unrecognized token '/'`, Datadog HTTP 403 and
telemetry timeouts. The later neutral probe supersedes a terminal-blocker reading: local auth status was
logged-in, the route was reachable, and the parser/session path remains unresolved. No provider result
was captured and no credential bytes are recorded. Both earlier bounded `docker exec timeout` invocations returned process exit
code `1` rather than timeout status `124`; the classification is therefore a fatal CLI/session path
after startup within the 60/90-second bounds, not a deadline-only observation.

The Codex call was deliberately connection-only and read-only. It proves native provider response and
transport containment for the bounded check, not an admitted updater campaign. No
`SOURCE-ADMISSION.md`, frozen slot, owner-comprehension request, aggregate field report or post-field
correction exists. Field manifest remains NOT FROZEN and field slots remain `0`.

## Runtime-home corrected Claude probe — 2026-09-08

The image/subject metadata was inspected before the retry: image `sha256:02246d09d4b7...`, subject
UID/GID `65532:65532`, `network=none`, read-only rootfs, all capabilities dropped,
`no-new-privileges`, and no host/original mounts. The subject had no HOME/TMPDIR values in its base
environment. Under the existing `/run/tfw` tmpfs, the same UID successfully created harmless files in
`/run/tfw/runtime-home`, `/run/tfw/runtime-tmp` and `/run/tfw/claude-tmp`; these are the only runtime
home/temp paths supplied to the retry.

Exactly one fresh normal-OAuth probe used the same empty cwd and provider argv as the corrected vector
launcher, with fresh paths:
`/run/tfw/neutral-empty/debug-runtime-home-20260908.log`,
`/run/tfw/neutral-empty/claude-runtime-home.stdout`,
`/run/tfw/neutral-empty/claude-runtime-home.stderr`, and the structured receipt beside them. The
launcher receipt recorded child exit `0`, `timed_out=false`, stdout `1203` bytes, stderr `0` bytes,
and stdout SHA-256 `4a877120e9481c31677909c56de2526cc082aafa19b8e0fc9dc8b23b6259c7cf`.

Safe metadata extracted from the JSON response was: `type=result`, `subtype=success`, `is_error=false`,
`stop_reason=end_turn`, `terminal_reason=completed`, `num_turns=1`, `duration_api_ms=1473`,
`api_error_status=null`; the returned text was 47 characters with SHA-256
`0d1352695fc2e54e0bd7ca125fc90614d9e24fc670e2665d86db5dd9f863872b`. The response body, headers and
credentials were not read into evidence or emitted. The sidecar observed allowlisted
`api.anthropic.com:443` tunnels and the existing telemetry deny. This is a successful native
connection-only provider preflight, not an admitted updater or field campaign; field slots remain `0`.

<!-- A malformed earlier append is retained below only as an inert historical editing artifact.
\n+## Real HTTP CONNECT/native return — 2026-09-08
\n+The bounded return used a separate network-enabled sidecar and a network-none subject connected only
by a Docker-managed volume carrying two Unix sockets. No host path, original-project mount or
credential store was mounted into either container. The subject ran as UID/GID `65532:65532`,
read-only rootfs, `CapDrop=["ALL"]`, `no-new-privileges`, `pids-limit=128`, and `network=none`; the
sidecar used the same non-root/read-only/cap-drop controls with Docker bridge networking. The volume
was initialized by a disposable root init container only to set its owner; the provider subject itself
never ran as root.
\n+The final image was built from cached `python:3.13-slim` with `--pull=false`, official Linux binaries,
Git and bundled local runtime helpers. Image digest:
`sha256:02246d09d4b7a6185148c9d37b7005975a5e68d6ba6ba4da1afaba37dcf8c594`.
\n+| Component | Observed identity |
|---|---|
| Claude | 2.1.143; source binary SHA-256 `f75fdc3ff9d9cd494b86192f9e349b5c5c6d3970ed4d5cd5c7b330c5a2b1dcc4` |
| Codex | 0.152.1-linux-x64; source binary SHA-256 `b82018241214a4a7c6b97b198585192d1dbc3aab1ddcdc640f04d8dee8c606f9` |
| Candidate source | sanitized Git copy of Candidate `d6d26003972f7b18fe10d492960d0cbac9f0a3e8`, local copy commit `f4e47e3e7383dcf367026a0f087e11d2093593aa` |
\n+The sidecar accepts only HTTP CONNECT to port 443 on the provider-specific Unix socket, then forwards
the upstream socket bidirectionally without TLS interception, body logging or content inspection. The
observed Codex OAuth host was `chatgpt.com`; Claude used `api.anthropic.com`. A native Codex request
returned the following provider response through the route:
\n+```json
{"type":"item.completed","item":{"id":"item_0","type":"agent_message","text":"PREFLIGHT_ONLY"}}
{"type":"turn.completed","usage":{"input_tokens":10140,"cached_input_tokens":2560,"cache_write_input_tokens":0,"output_tokens":8,"reasoning_output_tokens":0}}
```
\n+The subject also issued a direct non-allowlisted CONNECT to `api.openai.com:443` through the Codex
relay and received:
\n+```text
HTTP/1.1 403 Forbidden
Content-Length: 0
```
\n+The same sidecar observed native Claude TLS tunnels to `api.anthropic.com:443` and denied the native
telemetry host `http-intake.logs.us5.datadoghq.com:443`. Claude did not produce a final response within
the bounded 90-second attempts. Redacted debug metadata recorded `JSON Parse error: Unrecognized token
'/'`, followed by Datadog flush HTTP 403 and telemetry export timeouts. This is classified as a Claude
unresolved parser/session path rather than terminal auth/capability evidence; no provider result or
credential bytes are recorded.
\n+The subject had local `AGENTS.md`, `CLAUDE.md`, `.tfw/**`, a Git worktree and the Candidate source, and
the Codex code-mode host plus `git`/`rg` runtime dependencies were present. The successful Codex call
was deliberately connection-only and read-only. It therefore proves native provider response and
transport containment for the bounded check, but does not constitute an admitted updater campaign:
no `SOURCE-ADMISSION.md`, frozen slot, owner-comprehension request, aggregate field report or
post-field correction exists. Field manifest remains NOT FROZEN and field slots remain `0`. -->

## Differentiated neutral Claude probe — 2026-09-08

One differentiated neutral probe was run in the same subject/user with normal OAuth (no `--bare`) from
cwd `/run/tfw/neutral-empty`. The configuration-path environment variable names were
`CLAUDE_CONFIG_DIR`, `HTTPS_PROXY`, `HTTP_PROXY`, `ALL_PROXY` and `NO_PROXY` (values are intentionally
omitted). The exact provider argv after `docker exec` was:

```text
timeout 60 /usr/local/bin/claude --debug-file /run/tfw/neutral-empty/debug.log --setting-sources user
  --strict-mcp-config --mcp-config=/opt/tfw/empty-mcp.json --no-chrome --disable-slash-commands
  --tools "" --no-session-persistence --output-format json -p PREFLIGHT
```

The credential JSON parsed successfully. The separate `claude auth status` launcher was
`docker exec <subject> /usr/local/bin/claude auth status`; PowerShell captured combined stdout/stderr
in an in-memory variable, retained only booleans and the exit code, and printed no provider/account
content. It returned exit `0`, with logged-in/authenticated true and expired/invalid/unauthorized/login
markers false.

For the corrected neutral provider command, stdout and stderr were captured by the invoking
`functions.exec_command` result (no file redirection); the retained result was empty and the wrapper
reported terminal exit `0` after polling session `50908`. Claude's own debug destination was
`/run/tfw/neutral-empty/debug.log`. That file also
contains the preceding malformed inline-JSON setup attempt, so its lines cannot be attributed by order
alone. The first setup form used the variadic `--mcp-config` argument with an inline JSON value, which
was logged as a malformed path before the corrected file form. Claude documents this option as accepting
JSON files or strings; therefore `Unrecognized token '/'` is compatible with a caught string-to-file
fallback and does not prove startup failed. A separate non-provider PowerShell transport audit passed
`--tools ""` to a Python argv echo and observed `['-c', '--tools']`: the empty argument was dropped.
Therefore the Claude invocation does not prove that an empty tools element was received; because
`--tools` is variadic, following flags may have been consumed or shifted. The retained empty-output
wrapper result is consequently inconclusive about CLI completion or tool disabling. The sidecar observed
Anthropic CONNECT attempts and the same telemetry deny. The Claude cause remains unresolved despite
valid local auth status and reachable route; it is not terminal invalid-auth evidence. No updater or
field slot was started.

## Corrected argv-vector Claude probe — 2026-09-08

The one authorized corrected probe used the committed in-subject Python launcher
`harness/claude_probe_launcher.py`. It constructed a Python list and invoked `subprocess.Popen` directly,
with no shell. The receipt recorded the actual empty element after `--tools`:

```json
{"argv":["/usr/local/bin/claude","--debug-file","/run/tfw/neutral-empty/debug-corrected-20260908.log","--setting-sources","user","--strict-mcp-config","--mcp-config=/opt/tfw/empty-mcp.json","--no-chrome","--disable-slash-commands","--tools","","--no-session-persistence","--output-format","json","-p","PREFLIGHT"],"child_exit_code":0,"cwd":"/run/tfw/neutral-empty","debug_path":"/run/tfw/neutral-empty/debug-corrected-20260908.log","stderr_bytes":0,"stderr_path":"/run/tfw/neutral-empty/claude-corrected.stderr","stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_bytes":0,"stdout_path":"/run/tfw/neutral-empty/claude-corrected.stdout","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","timed_out":false,"timeout_seconds":45}
```

The launcher itself exited `0`; the native child exited `0`, did not time out, and emitted no stdout or
stderr. The debug file recorded the JSON parse diagnostic, then `[STARTUP] Loading MCP configs...`,
policy-limit persistence and Anthropic CONNECT activity; the last redacted operation was a Datadog
telemetry flush HTTP 403. This proves the corrected argv reached startup and the provider route, but no
model reply or provider error was emitted to the separate output files. The structured result is
therefore `NO_PROVIDER_OUTPUT_AFTER_STARTUP`, not invalid-auth evidence and not a field admission.

## Freeze-contract native identity allocation — 2026-09-08

Before any updater start, six fresh task-owned subjects performed a bounded no-updater allocation with
an explicit empty runtime cwd and a 60-second hard timeout. The allocation prompt forbade project
inspection, writes and `/tfw-update`. The receipts retained only non-secret event metadata:

| Slot | Provider | Native identity | Safe outcome |
|---|---|---|---|
| `afd-claude` | Claude 2.1.143 | session `fa6b7284-c8dd-4705-927c-ac4079f421b0`; result `c201e2a8-bba9-46ef-a91d-23538e2209bd` | `result/success/end_turn`, exit 0 |
| `afd-codex` | Codex 0.152.1-linux-x64 | thread `01a07d93-0f03-76d2-8387-98bdca78ca7f` | thread/turn completed, exit 0 |
| `helpdesk-claude` | Claude 2.1.143 | session `ef0c34dd-14d6-4d47-ae09-40b632a63378`; result `da5c2caf-a5bc-4d8e-979a-49f09fcaf210` | `result/success/end_turn`, exit 0 |
| `helpdesk-codex` | Codex 0.152.1-linux-x64 | thread `01a07d93-eb81-7ac2-a9bb-b37c1e983881` | thread/turn completed, exit 0 |
| `atamat-claude` | Claude 2.1.143 | session `db95c011-51e8-420b-ac3f-60ac831242c2`; result `5bf41dae-c4a6-461d-8d4d-94b41eae1445` | `result/success/end_turn`, exit 0 |
| `atamat-codex` | Codex 0.152.1-linux-x64 | thread `01a07d95-96f6-7773-bbaf-0b2e7f910bb1` | thread/turn completed, exit 0 |

Every Codex allocation passed explicit `--model gpt-5.6-sol`; the safe JSONL did not emit a model
field, so the fixed argv is the model authority. No account identifier or credential value is present.

The final local safety check ran with `docker exec -w /run/tfw/runtime-home`, UID `65532`, and private
HOME/TMPDIR. It wrote harmless files only to the two runtime paths, validated credential JSON shape and
size/hash, resolved source `HEAD=d6d26003972f7b18fe10d492960d0cbac9f0a3e8`, observed zero source
remote characters, and received source write exit `1` in all six subjects. Claude `auth status` exit
was `0` in all three Claude subjects; Codex `login status` exit was `0` with empty output in all three
Codex subjects. Credential values and status bodies were not retained.

The complete Candidate source is now a distinct task-owned volume
`tfw-crue-source-20260908`, initialized from bundle SHA-256
`06DA810270384C565C0FDC6070D8F10AAF16D83CEDBECA2EF0D5604CC977AC2E`, and mounted read-only. The
source volume resolves exact d6, has no remote or dirty state, and rejects a write. Receiver volumes
remain independent and writable; the actual field subjects will overlay this source read-only at
`.tfw/.upstream`.

Per-slot stop limits are one provider child, 900 seconds wall-clock maximum, first terminal result,
no continuation/resume/retry, pids limit 128, UID/GID `65532:65532`, read-only rootfs, all capabilities
dropped, `no-new-privileges`, network none and exact provider-specific sidecar socket only. The
allocation setup failures (read-only-rootfs docker copy, stdin injection, auth path, auth ownership,
Codex flag syntax and a PowerShell quoting error) are preserved as preflight history; they launched
no updater. Updater starts remain `0`; all six field rows remain `FROZEN, NOT STARTED`.
