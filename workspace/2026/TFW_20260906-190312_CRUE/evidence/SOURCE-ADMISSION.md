# Source admission — TFW_20260906-190312_CRUE / Phase A

> **Admission:** FROZEN 2026-09-08; six slots admitted, zero updater attempts consumed at freeze.
> **Executor:** `01a07c52-d3cb-76b0-820f-f74a5bd54805`; **Coordinator:** `01a07c49-2e00-7523-be31-a273475c3676`.

## Governing authority

- Approved TS: `TS-TFW_20260906-190312_CRUE.md`, revision 3, approval SHA `5dfed7af5c013d469df88254378f4e7da7867c15`.
- Candidate: `d6d26003972f7b18fe10d492960d0cbac9f0a3e8`.
- Baseline: `8fd8e40b734e9c439bb84721ef8bee441b9fcdd7`.
- Field order: Claude before Codex for each project; AFD and helpdesk mandatory, Atamat admitted because its prepared copy is safely sanitised.
- No release, tag, push, publish, deployment, production, original-repository runtime mount, second campaign, new provider or new execution unit is admitted.

## Native boundary and effective containment

The native image is `tfw-crue-native:20260908`, image digest
`sha256:02246d09d4b7a6185148c9d37b7005975a5e68d6ba6ba4da1afaba37dcf8c594`.
Its environment contains no provider credentials, account identifiers, `HOME`, or `TMPDIR` values.
Each field subject will be a fresh container with the following effective controls: `network=none`,
UID/GID `65532:65532`, read-only root filesystem, all Linux capabilities dropped,
`no-new-privileges`, `pids-limit=128`, and a task-owned Docker named volume for the field copy plus
the task-owned proxy volume only. The subject receives no host path, original project path, Docker
socket, production mount, symlink or external remote. `/run/tfw` is a private tmpfs for runtime
home/temp/auth material; the field project is under its dedicated named volume.

The only networked component is the separate sidecar on Docker bridge. Subjects reach it only through
the task-owned Unix-socket volume. The exact routes are:

| Socket | Allowed destination |
|---|---|
| `/run/tfw/proxy/claude.sock` | `api.anthropic.com:443` |
| `/run/tfw/proxy/codex.sock` | `chatgpt.com:443` |

The sidecar forwards HTTP CONNECT bidirectionally without TLS interception or body logging. Its
negative control denied `api.openai.com:443` with HTTP 403. Field reports retain only safe route,
process, event and hash metadata; no credentials, raw HTTP, TLS bodies, account identifiers or secret
response content are admissible.

## Native identity and preflight ledger

The successful native connection-only preflights established provider reachability but did not start
an updater and did not consume a field slot:

- Claude CLI `2.1.143`; observed model `claude-opus-4-7[1m]`; session UUID
  `2095482c-15ef-43f3-9e23-12bb0207b04a`; result UUID `653939b0-f66a-4455-9335-bff4e6ffc876`.
- Codex CLI `0.152.1-linux-x64`; successful preflight thread
  `01a07d48-7b97-72f0-9ff8-b3357833c04c`.

No account identifier or credential is recorded. Prior preflight-only events are preserved as a
no-extra-attempt ledger: Claude bare-auth selection; Codex 401; simple sidecar policy probe; normal
Claude parse path; corrected vector launcher with no result; and the corrected runtime-home Claude
probe. The last returned structured `success`/`end_turn`, child exit `0`, timeout `false`, stdout
1203 bytes and stderr `0`. None launched `/tfw-update`; none is a consumed slot.

## Candidate source and independent receivers

The source bundle is task-owned and independent at `E:\TEMP\tfw-crue-field-20260908\candidate-git`.
It resolves `HEAD` exactly to Candidate `d6d26003972f7b18fe10d492960d0cbac9f0a3e8`; remotes are
removed. Each receiver's `.tfw/.upstream` is a separate local Git copy with the same exact Candidate
resolution and no configured external fetch route. Receiver Git commits are sanitised receiver
identities, not Candidate identities:

| Receiver | Immutable source snapshot | Sanitised receiver commit | Tracked files | Archive SHA-256 |
|---|---|---|---:|---|
| AFD | `c58ed93bf29f0b02533e360defbdaccdb070fb0a` | `b75d4af38d3bff1b731843acc514e50736c31a58` | 4210 | `E7103B18DBF63DAEE5B969AA2BAFBAFE055C5A09E12D6AA0A31FA447546449F4` |
| helpdesk | `40b196e3dd6f262470c1e1f2a14b862ecb986384` | `37e73c515ed658d422eb618294f1e91cd6f77fdb` | 1583 | `BDF8101A8C05F5DBEA73B5CA9870677552AEA6C8BBC86EBE1DFBCB07A6BC4DE4` |
| Atamat | `df40e667f2da3fd5a1b2cfcaa4c36f97e9255804` | `624b16ef93722a44fe49badf8e6d753bd8ef0d9f` | 1772 | `13a14a3bb3abd17df1025ae664cfa7e5e645bd16ce05978a54113687b708dbdb` |

The first two archive strings above are rendered with visual grouping only; the exact machine values
are retained in `FIELD-MANIFEST.md` and the harness ledger. No symlinks were found in the receiver
archives. Receiver copies are sanitized archive-derived copies; dirty state in the original AFD
repository was not copied.

## Excluded inventory

The archive-only sanitization moved removed files recoverably to
`E:\TEMP\tfw-crue-field-removed-20260908\` and did not modify originals. Exclusions are:

- AFD: tracked YC CA PEM, tracked raw secret-keys file, `.claude/settings.json`, and non-TFW
  `ci-status`, `deploy`, `health`, `incident` commands.
- helpdesk: `.claude/settings.json`, `.claude/settings.local.json`, and non-TFW
  `db-status`, `deploy-prod`, `k8s-status`, `load-prod-snapshot` commands.
- Atamat: `.claude/settings.json`, `.claude/settings.local.json`, non-TFW deploy/YC commands, and
  `code/web/.env.local` / `code/web/.env.production`.

Preserved are project `.tfw` configuration, TFW command files, task history, knowledge, profiles,
grants and configured checks, subject to the approved updater and its safe local checks. No private
bindings, provider credentials, hooks, external remotes, production endpoints or symlinks are in the
admitted copies.

## Frozen prompt and copy roots

The exact UTF-8 prompt is the canonical prompt in `FIELD-MANIFEST.md`; its byte length is 1010 and
SHA-256 is `93f1403f274cf0247ddc176e9b0feaca998d06d39338a16430b03a1177552351`. Every slot receives
that same material prompt and the same Candidate/source facts, with only its slot-specific project
root differing. The exact subject roots, created freshly immediately before each launch, are:

```text
/run/tfw/field/afd-claude/project
/run/tfw/field/afd-codex/project
/run/tfw/field/helpdesk-claude/project
/run/tfw/field/helpdesk-codex/project
/run/tfw/field/atamat-claude/project
/run/tfw/field/atamat-codex/project
```

Safe commands are limited to the updater's local workflow, Git/file inspection and checks discoverable
inside the admitted copy. Deployment, database, Kubernetes, cloud, incident, production, external
fetch and host-path commands are forbidden. A child start consumes exactly one slot; no retry is
permitted.

## Frozen matrix

| Order | Slot | Provider | Source snapshot | Status at freeze |
|---:|---|---|---|---|
| 1 | `afd-claude` | Claude | `c58ed93bf29f0b02533e360defbdaccdb070fb0a` | FROZEN, NOT STARTED |
| 2 | `afd-codex` | Codex | `c58ed93bf29f0b02533e360defbdaccdb070fb0a` | FROZEN, NOT STARTED |
| 3 | `helpdesk-claude` | Claude | `40b196e3dd6f262470c1e1f2a14b862ecb986384` | FROZEN, NOT STARTED |
| 4 | `helpdesk-codex` | Codex | `40b196e3dd6f262470c1e1f2a14b862ecb986384` | FROZEN, NOT STARTED |
| 5 | `atamat-claude` | Claude | `df40e667f2da3fd5a1b2cfcaa4c36f97e9255804` | FROZEN, NOT STARTED |
| 6 | `atamat-codex` | Codex | `df40e667f2da3fd5a1b2cfcaa4c36f97e9255804` | FROZEN, NOT STARTED |

This admission freezes inputs only. It does not assert updater success; field reports and post-field
evidence must record actual child outcomes, actions, changed/preserved files, checks, limitations and
next actions.

## Freeze-contract amendment — native identities and stop rules

The pre-launch contract is now complete. Six independent, real no-updater native allocations were
made in fresh subject state after the source-volume repair. The identity allocation prompt explicitly
forbade project inspection, writes and `/tfw-update`; each allocation used a 60-second hard timeout,
read-only model sandbox, empty runtime cwd, no MCP/connectors/browser/plugins/agent-spawn surfaces,
and the same exact-provider sidecar route. These are allocation identities, not claims that the later
updater will succeed.

| Slot | Provider | Native identity | Native outcome | Fixed model/CLI |
|---|---|---|---|---|
| `afd-claude` | Claude | session `fa6b7284-c8dd-4705-927c-ac4079f421b0`; result `c201e2a8-bba9-46ef-a91d-23538e2209bd` | result success, end_turn, exit 0 | Claude 2.1.143; model field not emitted in safe receipt |
| `afd-codex` | Codex | thread `01a07d93-0f03-76d2-8387-98bdca78ca7f` | thread/turn completed, exit 0 | Codex 0.152.1-linux-x64; explicit `--model gpt-5.6-sol` |
| `helpdesk-claude` | Claude | session `ef0c34dd-14d6-4d47-ae09-40b632a63378`; result `da5c2caf-a5bc-4d8e-979a-49f09fcaf210` | result success, end_turn, exit 0 | Claude 2.1.143; model field not emitted in safe receipt |
| `helpdesk-codex` | Codex | thread `01a07d93-eb81-7ac2-a9bb-b37c1e983881` | thread/turn completed, exit 0 | Codex 0.152.1-linux-x64; explicit `--model gpt-5.6-sol` |
| `atamat-claude` | Claude | session `db95c011-51e8-420b-ac3f-60ac831242c2`; result `5bf41dae-c4a6-461d-8d4d-94b41eae1445` | result success, end_turn, exit 0 | Claude 2.1.143; model field not emitted in safe receipt |
| `atamat-codex` | Codex | thread `01a07d95-96f6-7773-bbaf-0b2e7f910bb1` | thread/turn completed, exit 0 | Codex 0.152.1-linux-x64; explicit `--model gpt-5.6-sol` |

The safe-check command set, executed for all six allocation subjects, was: effective UID; private
`HOME=/run/tfw/runtime-home` and `TMPDIR=/run/tfw/runtime-tmp`; harmless writes to both runtime
paths; credential-file JSON-object shape, byte count and SHA-256 only; source `git rev-parse HEAD`;
empty source `git remote -v`; and a write attempt to the read-only source path. All six reported
UID `65532`, Candidate `d6d26003972f7b18fe10d492960d0cbac9f0a3e8`, empty remote, and source-write
exit `1`. Claude `auth status` returned exit `0` with 251 non-secret output bytes and SHA-256
`c56d1df9bd9a686f715d2693c8bd2386c8628ea4b7b615079cb5ed642be6d47e` in all three Claude subjects.
Codex `login status` returned exit `0` with empty output (empty-file SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`) in all three Codex subjects.
Credential values and account identifiers were never printed.

The exact d6 source is a distinct task-owned Docker volume `tfw-crue-source-20260908`, initialized
from a complete bundle SHA-256
`06DA810270384C565C0FDC6070D8F10AAF16D83CEDBECA2EF0D5604CC977AC2E`. In a read-only, non-root
subject it resolves exact d6, has no remote or dirty state, and rejects a write. The field subjects
will mount this source volume read-only at each receiver's `.tfw/.upstream` path; receiver volumes
remain writable and contain only their independent sanitized copy.

Per-slot hard stops are: one provider child only; 900 seconds wall-clock maximum for the updater;
terminate on timeout with no continuation or retry; first terminal provider result ends the slot;
no resume/fork/second campaign; subject UID `65532:65532`, `pids-limit=128`, read-only rootfs,
all capabilities dropped, `no-new-privileges`, network none, private writable runtime/auth volumes,
and exact provider sidecar route only. The field launcher records child exit, timeout, output hashes,
safe provider event metadata and before/after Git status without retaining raw provider text.

The allocation failure ledger is preserved: initial Claude setup timeout; auth-path mismatch; auth
directory ownership failure; Codex comma-delimited-disable parse failure; and the PowerShell quoting
failure in an attempted aggregate local-check command. They started no updater and consumed no field
slot. Current matrix state remains six rows `FROZEN, NOT STARTED`, updater starts `0`.
