# Native harness preflight — TFW_20260906-190312_CRUE / Phase A

> **Status:** PREPARED; no field subject started; field slots consumed: 0
> **Attribution:** Executor `robert`; candidate and accounting facts remain Coordinator-controlled.
> **Recorded:** 2026-09-07, Asia/Qyzylorda

## Candidate boundary

- Baseline: `8fd8e40b734e9c439bb84721ef8bee441b9fcdd7`
- Candidate: `146876e279313a6a1a1680b0c7fffa699e30d28e`
- Candidate worktree was clean after the implementation commit.
- No source repository, original project, production service, remote, credential store or native updater was accessed by this preflight.

## Native availability and launch surfaces

Read-only commands and observed results:

| Command | Exit | Observed result |
|---|---:|---|
| `Get-Command docker,claude,codex` | 0 | `docker.exe` 24.0.6; `claude.exe` 2.1.109; `codex.exe` available |
| `docker --version` | 0 | Docker version 24.0.6, build `ed223bc` |
| `claude --version` | 0 | `2.1.109 (Claude Code)` |
| `codex --version` | 0 | `codex-cli 0.152.1` |
| `docker image inspect alpine --format '{{.Id}} {{.RepoTags}}'` | 0 | `sha256:d529dd0c6e5597ac7e4a3e2dea65c3fcc6173f4cae713c409265c1dd9914a11b [alpine:latest]` |

The Claude help surface exposes `--print`, `--bare`, `--add-dir`, `--no-session-persistence` and JSON/stream output formats. The Codex help surface exposes `exec`, `sandbox`, `-s/--sandbox`, JSON output and an explicit dangerous bypass mode. These are capability observations, not an admission decision.

## Effective containment probe

Command:

```text
docker run --rm --network none --read-only --cap-drop ALL --security-opt no-new-privileges --pids-limit 64 --mount type=bind,src=<task evidence>/harness/probe-work,dst=/work alpine:latest sh -c 'set -u; echo id=$(id); grep ^CapEff: /proc/self/status; echo route; cat /proc/net/route; if touch /blocked-root 2>/dev/null; then echo rootfs_write=UNEXPECTED_SUCCESS; else echo rootfs_write=BLOCKED; fi; if touch /work/allowed 2>/dev/null; then echo work_write=ALLOWED; else echo work_write=BLOCKED; fi; echo pids_limit=$(cat /sys/fs/cgroup/pids.max 2>/dev/null || echo unavailable)'
```

Observed output (exit 0):

```text
id=uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
CapEff: 0000000000000000
route
Iface Destination Gateway Flags RefCnt Use Metric Mask MTU Window IRTT
rootfs_write=BLOCKED
work_write=ALLOWED
pids_limit=unavailable
```

The probe establishes the observed container controls for this host. It does not prove that a native
Claude/Codex launcher will inherit them; the effective native copy boundary must be re-proved before
field admission. The temporary `/work/allowed` probe file was removed after the observation.

## Admission disposition

- Native provider authentication status is not inferred from executable presence and is not admitted by this file.
- The prospective lab root remains `C:/Users/c0rpa/AppData/Local/tfw/experiments/TFW_20260906-190312_CRUE`; no copy root was created here.
- No updater command, provider session, source copy, field slot or external network request was started.
- Coordinator must freeze the exact manifest, sanitized copy roots, neutral prompt, native run identities and safe check commands before any subject start.
