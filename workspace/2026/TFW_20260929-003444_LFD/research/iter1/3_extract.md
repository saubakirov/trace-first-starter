# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260929-003444_LFD](../../HL-TFW_20260929-003444_LFD.md)
> Goal: Installing or updating TFW moves only the framework, about one megabyte, by one written method, and a newer release shows in one line when new work starts; the owner decides whether and when to update.
> Producer unit: `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher` · mode deep · OODA loop 1 of 3 (checkpoint met; no extra loop)
> Continuation source: [gate answer](../../journal/20260929-015144__gate_answer__89ea.md) in `67e2a38f86f87d4e89574e78c87a9e3e6eedd596`

New trials in this stage used the same conditions as Gather: tag `v3.7.1`, scratch directories only.
One deviation is recorded under E10.

## Configuration Space

Dimension names follow Gather (D1–D9). This table lists combinations that are not contradictory. It
does not rank them; the Findings analyse them. **N** marks a combination nobody proposed in the HL or
the Briefing.

### Fetch and install

| Config | D1 How obtained | D2 Line endings | D3 Identity check | D4 Paths | D5 Staging |
|--------|-----------------|-----------------|-------------------|----------|------------|
| C1 **N** | sparse clone | `autocrlf=false` on clone | raw hash against `ls-tree` | `.tfw` | temp clone outside the receiver; payload read in place, no copy |
| C2 | sparse clone | same | same | `.tfw` | clone made at `.tfw/.upstream/` (nested `.git`) |
| C3 **N** | sparse clone, then plain copy | same | same | `.tfw` | temp outside; copy `.tfw` to `.tfw/.upstream/.tfw` (today's layout, no archive) |
| C4 | sparse clone | plus `core.eol=lf` | same | `.tfw` plus a path a pinned guide names (`tools/migrations/2.0.0`) | temp outside |
| C5 **N** | sparse clone, then `archive --worktree-attributes` of local blobs + zip/tar | `autocrlf=false` | same | `.tfw` | `.tfw/.upstream/` |
| C6 | blobless clone + `archive --worktree-attributes` (R1's fix) | same | same | `.tfw` | `.tfw/.upstream/` |
| C7 | blobless clone + `archive` without flag (R1's original) | any | any | `.tfw` | `.tfw/.upstream/` |
| C8 | blobless clone + `--work-tree` pathspec checkout | `autocrlf=false` | raw | `.tfw` | `.tfw/.upstream/` directly |
| C9 | host archive of the commit SHA (zip) | set by the server | file list only; no blob ids without trees | allow-listed archive | `.tfw/.upstream/` |
| C10 | full shallow clone at the tag (disclosed heavy fallback) | `autocrlf=false` | raw | whole tree | temp outside |
| C11 | untagged commit: `init` + filtered `fetch --depth 1 <sha>` + sparse checkout | same | raw | `.tfw` | temp outside |
| C12 **N** | untagged commit: the operator's existing local checkout + `git archive` (today's text) | environment | environment | `.tfw` | `.tfw/.upstream/` |
| I1 | install: sparse clone with `.tfw editions` | `autocrlf=false` | raw | `.tfw` + `editions` | temp outside; copy the chosen edition |
| I2 | install: GitHub "Download ZIP" of a post-change tag | server | none | allow-listed archive | the user's folder |
| I3 | install: README "clone to a temporary directory" (today) | environment | none | whole history | temp |

### Version line

| Config | D6 Command and limit | D7 Newest tag | D9 Upstream |
|--------|---------------------|---------------|-------------|
| V1 **N** | no network call | — | `installed_from: "self"` → no line offer |
| V2 | `ls-remote --tags --refs` once, the agent tool's own time limit | highest exact `vX.Y.Z` | receiver |
| V3 | same, no limit | highest exact `vX.Y.Z` | receiver |
| V4 | same with `http.lowSpeed*` | top of `--sort=-v:refname` | receiver |
| V5 | host API `/releases/latest` | a published Release (0 exist) | receiver |
| V6 | shell `timeout N` prefix | highest exact `vX.Y.Z` | receiver |

### Release archive (§3 claim 3)

| Config | D8 `.gitattributes` form |
|--------|--------------------------|
| R1 | none (today) |
| R2 | allow-list: `/* export-ignore`, then `-export-ignore` for `.tfw`, `editions`, README files, `LICENSE` |
| R3 **N** | R2 plus `/tools -export-ignore`, `/tools/* export-ignore`, `/tools/migrations -export-ignore` |
| R4 | deny-list per development directory |
| R5 | R2 minus `.tfw/` project state (`project_config.yaml`, `knowledge_state.yaml`, `update_receipts/`) |

## Findings

### E1 — Measured matrix: method × shell × line-ending setting

| Config | Git Bash | PowerShell 5.1 | WSL Ubuntu | Installer default `autocrlf=true` | Tools beyond Git |
|---|---|---|---|---|---|
| C1 / C3 | 0.64 MiB, 6.9–8.2 s, 95/95 | 0.64 MiB, 4.8–5.0 s, 95/95; `Copy-Item` staging 95/95 | 0.73 MiB (install set), 4.8–5.2 s | **95 files CRLF unless `-c core.autocrlf=false`** | none (`cp` or `Copy-Item` for C3) |
| C5 | archive 0.2 s, 0 lazy fetches | zip + `Expand-Archive` 95/95 | — | same; the archive applies it too | zip/tar extraction |
| C6 | 0.57 MiB, 158 s, 93 round trips | extraction traps (G4) | 92 s | same | tar or zip |
| C7 | 114.1 MiB, 41 s | — | — | same | tar or zip |
| C8 | 93 round trips, 75 s (local server) | — | — | same | none |
| C11 | 0.58 MiB, 15.2 s, 95/95 (GitHub, by full SHA) | — | — | same | none |
| C10 | ≈114 MiB (the tree's blobs at depth 1) | — | — | same | none |

The first `cp -r` or `Copy-Item -Recurse` copies preserve bytes: 95/95 by raw hash in both shells.
The configuration a first reading of the HL suggests, R1's fix (C6), is the slowest light option.

### E2 — Git feature floor

| Feature | Needed by | Available from | Evidence |
|---|---|---|---|
| `git sparse-checkout` | C1–C5, I1, C11 | 2.25 | Git 2.25.0 release notes; GitHub blog |
| `clone --sparse` | C1–C5, I1 | 2.25 | secondary sources; observed in 2.42 and 2.43 |
| cone default for `sparse-checkout set` | the "root files included" detail | 2.37 | secondary |
| partial clone `--filter=blob:none` on clone | all light configs | about 2.19–2.24, depending on source | secondary |
| `archive --worktree-attributes` | C5, C6 | long-standing | git-archive docs |
| `clone --revision` (clone by SHA) | an easier C11 | 2.49 | **absent in 2.42** (`unknown option`) |

A Git between 2.25 and 2.36 leaves `set .tfw` in non-cone mode. Emulated with `--no-cone .tfw` on the
local server, it still gave `.tfw/` 95/95 byte-equal. It dropped the root files, and the unanchored
pattern also pulled six tiny files under `workspace/…/evidence/…/.tfw/`. Reading the payload only from
`<tmp>/.tfw/` keeps the result right either way. For reference, from general knowledge not verified
here: Ubuntu 22.04 ships Git 2.34, Debian 12 2.39, macOS Command Line Tools about 2.39. **Git below
2.42 and macOS were not observed.** An old Git without `--sparse` or `--filter` fails loudly
(`unknown option`, exit 129); it cannot degrade silently.

### E3 — Fit with the unchanged pin

| `update.md` Step 0 guarantee | C1/C3 (tag) | C6 (tag) | C9 archive link | C11 untagged |
|---|---|---|---|---|
| operator-named tag resolves one object | `clone --branch <tag>` asks the remote for that tag only; 1 tag fetched | same | needs the commit SHA first (`ls-remote`) | the operator gives the SHA; `--branch <sha>` fails (exit 128) |
| `VERSION` equals the tag | `git show HEAD:.tfw/VERSION` → `3.7.1` | same | from extracted files | same as C1 |
| full SHA recorded | `git rev-parse HEAD` | same | known beforehand | given |
| immutability recheck | `git ls-remote <upstream> refs/tags/<tag>` equals `git rev-parse <tag>` | same | a commit-ID archive keeps its contents (GitHub Docs) | the commit is immutable |
| no live `HEAD` read | yes (`clone --branch` with depth) | yes | yes | yes |
| "local source clean under `.tfw/`" | trivially true for a fresh clone; `status --porcelain -- .tfw` empty | no checkout exists | not applicable | yes |
| per-file check against the pinned tree | trees present: `ls-tree` + `hash-object --no-filters` | same | **not possible without trees** | same |

C1/C3 fit every guarantee without changing its meaning. What changes is only where the "local Git
checkout" comes from: a fresh temp clone made for this update, instead of an existing one.

### E4 — Where the payload lives

- Receivers do not ignore `.tfw/.upstream/`. Only the upstream's own `.gitignore` lists it; neither
  `init.md` nor the templates add it. In a scratch receiver, a clone placed at `.tfw/.upstream/` (C2)
  turned `git add -A` into `warning: adding embedded git repository` and a gitlink (mode `160000`).
  **C2 can put a stray path into receiver history** (DoF 1).
- C1 keeps the clone outside the receiver, but it changes path references `update.md` uses: Read
  Contract row 4 `.tfw/.upstream/.tfw/workflows/update.md` and the Step 4 cleanup.
- C3 keeps every existing path reference and adds one copy command, with no archive tool.
- Whether `.tfw/.upstream/` staging is needed at all is iteration 2's subtraction question. C1 is the
  configuration that answers "no".

### E5 — The untagged Candidate route

`update.md` also allows an explicitly authorized untagged commit. `git clone --branch` cannot take a SHA,
and `clone --revision` needs Git 2.49. The Git-only light route (C11) needs seven commands: init,
autocrlf, remote, promisor, filter, sparse set, fetch by SHA, then checkout. Measured on GitHub: 15.2 s,
0.58 MiB, 95/95 byte-equal. C12, a configuration nobody proposed, keeps the untagged case on today's
text: an operator who authorizes a Candidate usually holds a local checkout, where `git archive` costs
nothing. The light fetch would then cover tags only. Challenge tests whether that keeps DoD 3.

### E6 — Fallback chain by failure cause

| Failure | Observed or documented signal | Configs that still work |
|---|---|---|
| Git without `--sparse` (< 2.25) | `unknown option`, exit 129 | C6 (slow, per file), C10 |
| Host without filter support | one warning line `filtering not recognized by server, ignoring`, full download, **exit code to be tested** | C9 (if the host honours `export-ignore`), C10 |
| PowerShell 5.1 byte pipes, `tar` resolution, OEM-name garbling | G4 | C1, C3, C11 (no archive); zip + `Expand-Archive` for C5, C6, C9 |
| No `.gitattributes` in the target tree (every tag up to `v3.7.1`) | archive is 178.9 MiB | C9 is not light for old targets |

Host support for partial clone:

| Host | Support |
|---|---|
| GitHub | yes (observed) |
| GitLab | yes (docs; forum reports of old versions ignoring the filter) |
| Gitea | from 1.16 (Gitea docs) |
| Bitbucket Cloud | **no**; community answer, "not supported" |

The primary method is host-neutral wherever a host serves filters. Elsewhere Git itself falls back to
a full download, which Challenge must make visible.

### E7 — Version-line mechanics

- **V1:** the upstream (`installed_from: "self"`) needs no network call and shows no offer.
- **V2 (receiver):**
  - One `git ls-remote --tags --refs <tfw.upstream>`: 0.9–2.0 s, 2,938 B.
  - Keep only exact `refs/tags/vX.Y.Z`, compare numerically with `.tfw/VERSION`, and count newer
    releases from the same list.
  - A failure or a timeout shows the newest as unknown, with the reason.
- **Why V3, V4 and V6 fail:**
  - V3: without a limit, a blackholed network costs 21 s on Windows and 131 s on Linux.
  - V4: `lowSpeed*` does not bound the connection phase, and the top of `-v:refname` can be a
    suffixed tag.
  - V6: in PowerShell and cmd, `timeout` resolves to Windows `timeout.exe`, a wait command. It
    failed with `Invalid syntax`, exit 1, while Git Bash's coreutils `timeout 5 git --version`
    worked. A shell prefix therefore cannot be the one written method.
- **The limit must come from the agent:** libcurl's default connect limit is 300 s. A 2026-07-23 patch
  proposing `http.connectTimeoutMs` / `GIT_HTTP_CONNECT_TIMEOUT_MS` got review questions from the
  maintainer, not acceptance. No released Git bounds the connection phase, so only the agent's own
  command time limit can. Claude Code's shell tool exposes one; the Codex sandbox stays unobserved.
- **V5:** the repository has 0 published Releases, so the host API would always say "none".

### E8 — Install payload and archive variants

- **Install (I1, DoD 4):** the installed `.tfw/` should equal the tag's `.tfw/` minus
  `project_config.yaml`, `knowledge_state.yaml`, `update_receipts/` (5 files at `v3.7.1`) and
  `.upstream/`. Init then writes a fresh `project_config.yaml` from the template. That is 88
  framework files at `v3.7.1`.
- **Archive variants** (local archives of a scratch commit on top of `v3.7.1`):

| Config | ZIP | Files | `tools/migrations/2.0.0` in tree-attribute archives | `.tfw/` via tree-attribute archive |
|---|---:|---:|---|---:|
| R1 | 178.9 MiB | 3,902 | yes | 95 |
| R2 | 571,807 B (0.55 MiB) | 129 | **no (0 files)** | 95 |
| R3 **N** | 590,839 B (0.56 MiB) | 132 | yes (3 files) | 95 |
| R5 | 473,080 B (0.45 MiB) | 122 | no | **88** (config, state and receipts dropped) |

R3 removes the migration-bundle conflict for +19 KB. R5 gives ZIP users a `.tfw/` already clean of
upstream state. It also means any tree-attribute archive of `.tfw` loses the target's
`project_config.yaml`. Whether an update reads the target's live config (Step 2, "update
framework-owned keys") is not settled by the text. Challenge asks that question.

### E9 — Text cost

`update.md` has 1,227 words by `wc -w`, leaving 173 to the 1,400-word ceiling. The Step 0 sentences
the light fetch replaces ("Resolve `tfw.upstream` to a local Git checkout … materialize exactly that
object with `git archive` into `.tfw/.upstream/`") are about 50 words. The 2-command form is C1. C3 adds
one copy. C6 needs clone, archive and extraction. C11 needs seven. The byte copy
`.claude/commands/tfw-update.md` must follow.

### E10 — Deviation: a second heavy GitHub transfer (not approved)

On 2026-09-29 at about 01:55 (+05:00) I ran `git archive` **without** `--worktree-attributes` inside an
existing GitHub sparse clone, to see whether local blobs change the prefetch. They do not: it made 1
batch fetch of the whole tree, 40.1 s and ≈114 MiB, in a clone that already held every `.tfw` blob.
The gate answer approved exactly one heavy run, and this was a second one, caused by my test design.
The clone was deleted at 01:56:47. Since then, any trial that could fetch lazily beyond its paths runs
only against the local `file://` server.

**The trap it shows:** in any partial clone, sparse or not, one `git archive` without the flag pulls
the whole tree. A written method that keeps an archive step has to carry that flag every time.

### External sources (this stage)

- GitHub blog, [Bring your monorepo down to size with sparse-checkout](https://github.blog/open-source/git/bring-your-monorepo-down-to-size-with-sparse-checkout/): `sparse-checkout` in 2.25; cone mode includes immediate files of parent directories.
- [Highlights from Git 2.25](https://github.blog/open-source/git/highlights-from-git-2-25/) and search summaries (secondary) for `clone --sparse` in 2.25 and the cone default in 2.37.
- Host support: [Gitea clone filters](https://docs.gitea.com/usage/clone-filters); [Atlassian community on Bitbucket Cloud](https://community.atlassian.com/forums/Bitbucket-questions/filtering-not-recognized-by-server-error-when-trying-git-clone/qaq-p/2041185); [GitLab forum](https://forum.gitlab.com/t/partial-clone-does-not-work/38656).
- Git mailing list, [http: add a config to limit the connection time](https://ratatoskr.run/git/2026/07/17309732/t) (2026-07-23): a proposal under review, with libcurl's default 300 s.
- Observed locally: `git archive --remote=https://…` → `operation not supported by protocol` (exit 128, 0.24 s), so it is no option for HTTPS upstreams.

Web actions: 5 (soft limit 5). Project files read: 2 new (the startup-card range and the receiver
`.gitignore` sources); trial outputs are not project files.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1/C3 fit every pin guarantee unchanged, need only Git (plus one copy for C3), and hold 95/95 in three environments | how a host without filters shows itself (exit code, signal) — Challenge |
| C2's nested clone becomes a gitlink under `git add -A` in a receiver | — |
| C6 is light but per file (158 s); C8 likewise; any no-flag archive in a partial clone prefetches the whole tree | — |
| Old Git (2.25–2.36, non-cone) still gives a byte-equal `.tfw/`; below 2.25 fails loudly | Git below 2.42 and macOS unobserved |
| The untagged route costs 7 commands (C11) or stays on today's text (C12) | whether C12 keeps DoD 3 — Challenge |
| V2 is the only version-check shape with bounded time; the limit must come from the agent's tool; `timeout` is not portable; no released Git bounds connect | Codex tool behaviour unobserved |
| R3 keeps the migration bundle in archives for +19 KB; R5 would drop the target config from tree-attribute archives | whether an update reads the target's live `project_config.yaml` — Challenge |
| Deviation E10 recorded | — |

**Stage decisions.**
1. **Taken to Challenge:**
   - C1 and C3 as the primary pair; they differ only in staging.
   - C11 or C12 for untagged Candidates.
   - C10 as the disclosed heavy fallback, and C9 as the host fallback for targets that carry R2 or
     R3.
   - V1 with V2.
   - R2 against R3.
2. **Set aside, with measured reasons:**
   - C2 (gitlink), C7 (114 MiB), C8 (per file with no advantage over C6).
   - V3, V4, V6 (unbounded, ineffective, not portable) and V5 (no Releases).
   - R4 (drifts as directories appear; not measured).

   C6 stays only as the Git-only answer to "Git too old for `--sparse`".
3. **R5 is held** until Challenge settles whether an update reads the target's config.

**Metacognitive check.** New here:
- C8 is as slow as C6.
- A no-flag archive prefetches even in a sparse clone (from E10).
- A nested clone becomes a gitlink in a receiver.
- The untagged route needs seven commands.
- Windows `timeout` is a trap.
- Old Git degrades without harm.
- Bitbucket Cloud does not serve filters.
- R3 exists.

Confirmed only: the pin fit of C1, expected from G9. Not checked: another Git host in practice, older
Git binaries, macOS.

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed? (feature floor, pin fit, version-line mechanics, install payload, archive variants)
- [x] Configuration Space built from Gather dimensions?
- [x] Hypothesis tested? (H1 floor and fallbacks, H3 limit shape, H4 exclusions)
- [x] Counter-evidence sought? (old Git, nested clone, Windows `timeout`, host support, the no-flag archive in a sparse clone)

**Knowledge handover.** Producer as in the header. Source and epoch: `v3.7.1` and this repository at
`67e2a38f`; Git 2.42.0 for Windows and 2.43.0 in WSL; 2026-09-29. Material: E1–E10. Uncertainty: the
Remaining column. Continuation: Challenge after the Coordinator's gate.

Stage complete: YES
→ User decision: ___
