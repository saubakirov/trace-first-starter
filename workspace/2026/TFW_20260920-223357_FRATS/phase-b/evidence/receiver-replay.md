# Receiver Replay — FRATS Phase B

> **Verification epoch**: 2026-09-21T14:06:17.5456556Z to 2026-09-21T14:06:19.3562146Z
> **Mode**: read-only; no install, update, generation, normalization, staging or commit
> **Candidate under comparison**: `fd0655ce17f2c650d238622c1d6a57ec5dd9a204`

The status hash is SHA-256 of `git status --porcelain=v1 --untracked-files=all` records joined by LF
with no final newline. Start and end snapshots matched on resolved path, HEAD, branch, status count
and status hash for every receiver.

| Receiver | HEAD / branch | TFW | Worktree at both boundaries | Local surface/customization | Start=end |
|---|---|---:|---|---|---|
| Helpdesk (`D:/projects/research/helpdesk`) | `53e4d93fb0805eb29947f06c768fee7223d0fcb3` / `beta` | 3.4.1 | clean; 0 paths; `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | managed `AGENTS.md` and `CLAUDE.md`; local `.agent/rules/tfw.md` | yes |
| SenseLab / KazNPU (`D:/projects/research/kaznpu-ai-lab`) | `443eecedb7a52a4914d3518b718918d6def80414` / `master` | 3.1.0 | 173 paths: 4 tracked, 169 untracked; `1e914fb35a118ef7c3e50ac49bc86061e492bf51376cd3c2b9aba562483d88da` | managed `AGENTS.md`/`CLAUDE.md`; no local Antigravity rule | yes |
| AFD (`D:/projects/research/ai-first-devices`) | `c615a9076353e85689150192f45551b4bb4711c2` / `beta` | 3.3.0 | 3 paths: 1 tracked, 2 untracked; `196574d5e93b995ad956ad1b238c377bdda5a2cd46ac2c7cd72f4b98558aa00a` | managed `AGENTS.md`/`CLAUDE.md`; no local Antigravity rule | yes |
| RYC (`D:/projects/research/research-yandex-cloud`) | `93116c4172b3be2b1906c2f725ee1baf5aa0f387` / `master` | 3.4.1 | clean; 0 paths; `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | unmarked, project-owned `AGENTS.md`; no `CLAUDE.md`; local `.agent/rules/tfw.md` | yes |

## Dirty-state bounds

KazNPU's four tracked paths are two faculty-mailing files and two sticker documentation files; its
169 untracked paths are sticker/strategic-vision project outputs. AFD's exact three paths are:

```text
 M tasks/AFD-51__yc_release_and_cross_agent_ops/phase-d/HL__phase-d__prod_metrics_plane.md
?? tasks/AFD-46__operator_identity_and_rbac/HL-AFD-46__operator_identity_and_rbac.md
?? tasks/AFD-46__operator_identity_and_rbac/research/iterations.yaml
```

These are project/task content, not Phase B writes or evidence of adapter failure. RYC's unmarked
`AGENTS.md` is a concrete customization constraint: a future update must preserve it and may not
replace it as a managed block without separate owner authorization.

## Current versus proposed behavior

- Helpdesk and RYC already report 3.4.1. Phase B changes nothing there; the Candidate becomes
  available only after a separately authorized framework release/update.
- KazNPU 3.1.0 and AFD 3.3.0 are older installed epochs. Phase B cannot infer their migration result
  from current project dirt and does not attempt one.
- The Candidate fixes canonical filename issuance, removes contradictory/stale cross-references,
  keeps role workflows on the already-active root delivery, and synchronizes all generated command
  copies in the framework source tree.
- The Candidate preserves managed foreign content, historical filename reads, current adapter
  topology and the existing Codex P2 / Claude P0 evidence ceiling. It does not establish provider
  reliability, receiver upgrade safety for all customizations, or universal behavior from four cases.
- Any install/update, RYC managed-block adoption, cleanup of receiver dirt, or release is a separate
  owner-controlled action outside this Phase B replay.

## Epoch separation

Earlier FRATS research observed KazNPU with 27 dirty paths and RYC with 52 uncommitted update paths.
The present KazNPU 173-path and clean RYC states are a new epoch; they are not silently merged with
the earlier observation. AFD remains at the same HEAD with the same three task paths. All four
receiver facts are bounded to the exact epoch above.

Verdict: read-only replay PASS. No receiver repository was mutated by this task.
