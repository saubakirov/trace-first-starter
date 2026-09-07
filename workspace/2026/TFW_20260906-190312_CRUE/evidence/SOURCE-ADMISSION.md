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
