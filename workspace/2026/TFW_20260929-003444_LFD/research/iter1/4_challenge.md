# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260929-003444_LFD](../../HL-TFW_20260929-003444_LFD.md)
> Goal: Installing or updating TFW moves only the framework, about one megabyte, by one written method, and a newer release shows in one line when new work starts; the owner decides whether and when to update.
> Producer unit: `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher` · mode deep · OODA loop 1 of 3 (checkpoint met; no extra loop)
> Continuation source: [gate answer](../../journal/20260929-020513__gate_answer__2493.md) in `dc5d1b4a9ce93c7de8713ac38c50b043b37f3595`

Every trial in this stage ran against the local `file://` server in scratch directories, per the
binding in the gate answer. GitHub was contacted twice, only for `ls-remote` of one tag with a packet
trace; that transfers refs, not objects. Heavy local clones were deleted after measuring.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1 any partial clone | + `git archive` | flag | absent | one batch prefetch of the whole tree, even in a sparse clone (G1, E10) |
| D1 archive routes | tar/pipe | shell | PowerShell 5.1 | byte pipes corrupt; `tar` resolution and OEM names differ (G4) |
| D2 | environment defaults | platform | Git for Windows installer default | all files rewritten to CRLF (G3; 88/88 again in X6) |
| D2 | `autocrlf=false` alone | user attributes | `text=auto` or `eol=crlf` | 95/95 CRLF (X6) |
| D3 | filtered hash or `git status` | platform | Windows | hides CRLF (G1) |
| D4 | `.tfw` only | receiver | pre-2.0 needing `tools/migrations/2.0.0/` | the bundle is missing (G7) |
| D5 | C1: payload read outside `.tfw/.upstream/` | pinned guides | `2.0.0.md`, `3.1.0.md`, `update.md` | they name `.tfw/.upstream/.tfw/…` paths that would not exist (X1) |
| D5 | C2: clone left at `.tfw/.upstream/` | receiver | `git add -A` | gitlink into receiver history (E4) |
| D1 light clone | no size check | host | no filter support (e.g. Bitbucket Cloud) | full download, exit 0 (X2) |
| D1 non-cone patterns | leading `/` | shell | Git Bash | rewritten to `C:/Program Files/Git/.tfw/`, matches nothing (X7) |
| D6 | no limit | network | drops packets | 21 s Windows, 131 s Linux (G6) |
| D6 | `timeout` prefix | shell | PowerShell or cmd | resolves to the wait command (E7) |
| D7 | top of `-v:refname` | tags | suffixed pre-releases | a pre-release sorts above its release (G6) |
| D8 | R2 | pinned guides | "acquire `tools/migrations/2.0.0/` from the release" | absent from the release archive (G8) |
| C9 archive link | per-file check | target | any tag up to `v3.7.1` | no trees for blob ids; 178.9 MiB without `.gitattributes` |

**Surviving configurations:**

| Config | D1 | D2 | D3 | Notes |
|--------|----|----|----|-------|
| **S1** (C3 in staging) | `clone --filter=blob:none --sparse --depth 1 --branch <tag>` into `.tfw/.upstream/.clone`, `sparse-checkout set .tfw`, copy `.tfw` to `.tfw/.upstream/.tfw`, delete `.clone` | clone `-c core.autocrlf=false -c core.attributesFile=` | `count-objects -vH` size check, then raw hash against `ls-tree` | cone mode (the recommended mode); Git ≥ 2.25; keeps every existing path reference |
| **S2** (C15, exact) | `clone --no-checkout …`, `sparse-checkout set --no-cone '.tfw/**' '!.tfw/update_receipts/**' '!.tfw/project_config.yaml' '!.tfw/knowledge_state.yaml'`, `checkout` | same | same | only the 88 installable files and trees; **non-cone mode is deprecated upstream**; `--no-cone` needs Git ≥ 2.35 |
| **S3** (C14, untagged or unified) | `init` + promisor config + sparse set + `fetch --depth 1 --filter=blob:none origin <tag or sha>` + `checkout FETCH_HEAD` | same | same | one sequence for a tag or an authorized SHA; needs protocol v2 for a non-tip SHA |
| **S4** (V1 + V2) | `installed_from: "self"` → no line; else one `ls-remote --tags --refs`, limit set on the agent's command | — | exact `vX.Y.Z`, numeric compare | unknown with reason on failure |
| **S5** (R3) | allow-list plus the migration bundle | — | — | 0.56 MiB zip |
| **F1** (fallback) | the full download a filter-less host forces | same | size check shows it, receipt discloses it | payload still byte-equal |

**Unexpected survivors:**
- S1's clone *inside* `.tfw/.upstream/.clone`. No OS temp path and no shell-specific temp variable
  are needed, so it also suits sandboxes that allow writes only inside the project. The existing
  Step 4 cleanup already removes `.tfw/.upstream/`.
- S2. In Gather and Extract it looked impossible, but the only cause was Git Bash rewriting
  `/.tfw/` (X7).
- S3 as *one* sequence for both tag and SHA. It is shorter than the tag route plus a separate
  untagged route.
- F1. Git performs this fallback by itself; the method only has to measure and disclose it.

## Findings

### X1 — C1 against C3: the staging path carries weight

Pinned text names `.tfw/.upstream/.tfw/…`: `update.md` Read Contract row 4 and Step 4 cleanup, their
byte copy, `migrations/2.0.0.md` (lines 70 and 81: "read `.tfw/.upstream/.tfw/workflows/update.md`",
`[ -f ".tfw/.upstream/$f" ]`), and `migrations/3.1.0.md` (line 93). Those guides are immutable history
("Do not rewrite earlier migration guides"). A payload read in place from an outside clone (C1) would
send a pre-2.0 receiver to paths that no longer exist. **C1 is eliminated for this task.** C3 keeps the
paths.

The in-staging variant (S1) was measured in a scratch receiver:

| Shell | Time (local server) | Stored objects | Result | Receiver effect |
|---|---:|---:|---|---|
| Git Bash (`cp -r`, `rm -rf`) | 1.5 s | 673.91 KiB | 95/95 byte-equal | `git add -A` → 0 gitlinks; receiver `VERSION` untouched |
| PowerShell 5.1 (`Copy-Item -Recurse`, `Remove-Item -Recurse -Force`) | 0.9 s | 673.91 KiB | 95/95 byte-equal | clone folder removed |

While `.clone` exists, the receiver shows `?? .tfw/.upstream/`. Deleting the clone right after the copy
closes the gitlink window.

### X2 — A host without filter support: the signal and the exit code

Tested with a plain local `upload-pack`, which advertises no `filter`:

| Signal | No filter support | Filter supported |
|---|---|---|
| `clone` exit code | **0** | 0 |
| stderr | one line: `warning: filtering not recognized by server, ignoring` (printed even with `-q`) | nothing |
| `remote.origin.promisor` / `partialclonefilter` | `true` / `blob:none` (**misleading**) | same |
| `.promisor` pack marker | present (**misleading**) | present |
| `count-objects -vH` size-pack | **114.43 MiB** | 262.50 KiB |
| objects missing from `HEAD` | **0** | 3,493 |
| resulting `.tfw/` | 95/95 byte-equal | 95/95 |

Configuration and pack markers say "partial" even when the download was full. Only the stderr line,
the stored size and the missing-object count tell the truth. A size check with
`git -C <clone> count-objects -vH` also works as the "measured, not estimated" transfer figure for
DoD 1. A preflight exists: with `GIT_TRACE_PACKET=1`, `ls-remote` shows GitHub's v2 capability
`fetch=shallow wait-for-done filter`, and the plain server lacks `filter`. It needs shell-specific
environment syntax, so it cannot be the one method. The survivor is the post-clone size check with
disclosure (F1).

### X3 — Untagged route under DoD 3

| Candidate | Commands | Pin meaning (tag, SHA, `VERSION`, recheck, no live `HEAD`) | Trap left |
|---|---:|---|---|
| C12: today's local checkout + `git archive` | 0 new | unchanged | "resolve to a local checkout" leaves the fetch to improvisation; the archive flag trap in a partial clone; `autocrlf` |
| C13: clone some tag, then fetch the SHA | 4 | unchanged | **which tag** is an agent choice (improvisation) |
| C14 unified (S3) | 8 | unchanged; `FETCH_HEAD` gives the tag object (`e39a0371…`) for a tag and the commit for a SHA | none observed |

C14 was measured on the local server: 1.4 s for a tag and 1.7 s for a SHA, 617 KB, 95/95 each. A
**non-tip** commit fetched by SHA works over protocol v2 without any server permission. Under protocol
v0 it fails loudly: `Server does not allow request for unadvertised object`, exit 1. On GitHub
(Extract E5, an eight-command variant) the result was 95/95. C12 and C13 are set aside: both leave
room to improvise, which the task exists to remove (Principle 2). All three keep DoD 3's meaning.

### X4 — R2 against R3, and whether an update reads the target's live config

- `update.md` Read Contract: "Never read … project-state bodies". Step 2 "update framework-owned
  keys" names no source. The only config form among the pinned framework files is
  `.tfw/templates/project_config.yaml`. The 3.7.0 guide's "`tfw.version` in `.tfw/project_config.yaml`"
  line is a maintainer release step. **No shipped step requires the target's live
  `project_config.yaml`.** The text does not forbid it by name either, so R5 stays set aside: it gives
  no DoD benefit and carries that ambiguity.
- The migration guides (`2.0.0`, `3.0.0`, `3.1.0`, `3.2.0`, changelog) say to acquire
  `tools/migrations/2.0.0/` "from that same immutable upstream release ref". R2 silently removes it
  from every release archive. **R3 survives** at +19 KB. Git users get the bundle either way with
  `sparse-checkout add tools/migrations/2.0.0` (cone) or an added pattern (S2).

### X5 — Windows long paths: not reproducible here

At 306 characters (base 162 + 138) the sparse checkout wrote 95/95 even with `-c core.longpaths=false`.
This machine has the OS setting `LongPathsEnabled=1`, and the user's global Git config sets
`core.longpaths=true`. Per Microsoft Learn, long paths need both that registry value (not the default)
and a long-path-aware application. **Machines without it are unobserved**, because changing the
setting is a system change. By arithmetic, the risk arises only when the receiver root exceeds about
100 characters: staging = root + 153, in-staging clone = root + 160. The long paths are all
upstream receipts in `.tfw/update_receipts/`, which receivers never install. S2 does not fetch them at
all.

### X6 — A user-level attributes file against `core.autocrlf=false`

Emulated with `core.attributesFile`, and with a default-location `$HOME/.config/git/attributes`:

| User attributes | `autocrlf=false` | + `core.eol=lf` | + `core.attributesFile=` (empty) on the clone |
|---|---|---|---|
| `* text=auto` | **95/95 CRLF** | 0 | — |
| `* text eol=crlf` (default location) | **95/95 CRLF** | **95/95 CRLF** | **0** (3 runs) |

The gitattributes documentation says an explicit `eol` attribute wins over `core.eol`, and the global
file defaults to `$XDG_CONFIG_HOME/git/attributes`. Git for Windows' system attributes file holds only
`diff` rules. `core.attributesFile=` stored by `clone -c` neutralises the user file. `core.eol=lf` in
addition guards a future `text` rule in the upstream's own `.gitattributes`. That is inferred from the
same mechanism with `text=auto`, not tested with a tree-level file. One early harness run printed a
partial listing that three full reruns did not reproduce. The raw-byte check catches any residue
either way.

### X7 — Correction: exact patterns failed in Git Bash only

In Gather and Extract, `sparse-checkout set --no-cone /.tfw/` "did not populate". The cause was Git
Bash: it rewrote the argument, and `.git/info/sparse-checkout` contained `C:/Program Files/Git/.tfw/`.
`conventions.md` already warns that shells rewrite a leading `/`. With patterns that do not start with
`/` (`.tfw/**` is anchored because it contains a slash), the exact set (S2) works:

| S2 | Result |
|---|---|
| Git Bash, local server | 88/88 framework files byte-equal; worktree only `.git` + `.tfw`; stored 489,768 B (trees 164,385 + framework 325,383) |
| PowerShell 5.1, local server | 88/88 byte-equal; the same sparse file |
| finishing step | `checkout`, `checkout HEAD`, `reset --hard`, `read-tree -mu HEAD` all populate |
| without `-c core.autocrlf=false` under the installer default | 88/88 CRLF |

Git's documentation states "non-cone mode is deprecated. Please switch to using cone mode."
`--no-cone` for `set` needs Git ≥ 2.35 (secondary sources; not observed below 2.42).

### X8 — What still travels that is not framework

| Part of a cone-mode (S1) transfer, `v3.7.1` | Stored bytes |
|---|---:|
| trees and the commit (whole repository structure) | 164,385 |
| top-level files that cone mode always includes | ≈88,000 |
| upstream state inside `.tfw/` (`update_receipts/` 285 KB raw, live config, knowledge state: 7 files) | ≈89,000 |
| the 88 installable framework files | ≈325,000 |

**About half of today's 0.64 MiB is not framework.** §3 claim 5 says "neither transfers nor
examines" non-framework content; S1 transfers about 0.17 MiB of file content that it does not install.
S2 removes the files but not the trees. No configuration avoids the trees on GitHub, which serves no
sparse filter. `--filter=tree:0` gave the same 664,278 B, because the lazy fetch of the root tree
returns its whole subtree.

Tree growth: 53,377 B (294 trees, v2.0.0, 2026-08-30) → 164,385 B (738 trees, v3.7.1, 2026-09-28).
At that month's rate the tree part alone would take about a year to push a light fetch past DoD 1's
2 MiB. **§1's "however large that repository grows" holds for file content, not for directory
structure.**

### X9 — Version line under attack

- A default tool timeout does not help. Claude Code's shell default of 120 s is shorter than Linux's
  131 s blackhole, but 21 s on Windows is already a material delay (DoF 3). **The rule must state the
  limit, for example about 10 s**, not rely on defaults.
- `installed_from: "self"` could reach a receiver whose config was copied from the upstream (the F23
  contamination class). That receiver would never see the line. S2 never stages the target's config,
  so the update itself cannot cause it; old full-clone installs could. Not measured: receivers were
  not inspected in this iteration.
- Counting "N releases newer" comes from the same one list, so no second call is needed.

### External sources (this stage)

- Git, [gitattributes](https://git-scm.com/docs/gitattributes): precedence of attribute files; explicit `eol` wins; `$XDG_CONFIG_HOME/git/attributes` default; `export-ignore` on files and directories.
- Git, [git-sparse-checkout](https://git-scm.com/docs/git-sparse-checkout): "non-cone mode is deprecated"; cone mode always includes top-level files; quoting of globs.
- Microsoft Learn, [Maximum Path Length Limitation](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation): MAX_PATH 260; `LongPathsEnabled` plus `longPathAware`.
- Secondary search results on `--[no-]cone` availability from 2.35 and the cone default in 2.37 ([Highlights from Git 2.35](https://github.blog/open-source/git/highlights-from-git-2-35/), [actions/checkout #1868](https://github.com/actions/checkout/issues/1868)).

Web actions: 4 (soft limit 5). Project files read: 3 (`migrations/3.7.0.md` range, and the update and
migration grep results).

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1 eliminated: pinned guides need `.tfw/.upstream/.tfw/…`; S1 (clone in staging, copy, delete) holds 95/95 in both Windows shells with no gitlink | — |
| A filter-less host: exit 0, one warning line, misleading config; the size check is the reliable signal | a real non-GitHub host (Bitbucket Cloud) unobserved |
| S3 (C14) serves tag and SHA in one sequence; protocol v0 refuses non-tip SHAs loudly | — |
| R3 survives; no shipped step needs the target's live config; R5 set aside | whether the owner confirms §3 claim 3 at all |
| Long paths not reproducible on this machine | machines without `LongPathsEnabled` |
| `core.autocrlf=false` alone is not enough; `core.attributesFile=` neutralises user files | a tree-level `text` rule (inferred, not tested) |
| S2 is exact (88 files, 0.47 MiB) but uses a deprecated mode and needs Git ≥ 2.35 | Git 2.35–2.41 unobserved |
| About 0.17 MiB of non-framework file content plus 0.16 MiB of trees travel with S1; trees grow with the repository | an owner decision on claim 5 wording or on removing upstream state from `.tfw/` |
| The version-line limit must be stated in the rule | Codex tool behaviour unobserved |

**Stage decisions.**
1. **C1 is eliminated.** S1 (clone inside staging, copy, delete) is the primary Windows-safe
   configuration; it keeps every pinned path.
2. **A post-clone size check with disclosure (F1) is required** in any surviving method. The
   capability preflight is set aside because it is shell-specific.
3. **Untagged: S3 survives; C12 and C13 are set aside** as improvisation.
4. **R3 over R2; R5 set aside.**
5. **Clone configuration:** `core.autocrlf=false` and `core.attributesFile=` are needed;
   `core.eol=lf` is a cheap guard.
6. **S1 against S2 is not a research decision.** S1 uses the recommended mode but transfers about
   0.17 MiB of non-framework files. S2 is exact but relies on a deprecated mode. Which one fits §3
   claim 5 and §7 principle 1 is a contract question for the Coordinator and owner.

**Metacognitive check.** New:
- The Gather and Extract "no-cone does not work" was a Git Bash rewrite, not Git.
- Half of the "framework" transfer is not framework.
- Trees grow with the repository.
- Git's own config and pack markers lie about a failed filter.
- `core.eol=lf` cannot beat an explicit `eol` attribute.
- The staging path is fixed by immutable guides.

Merely confirmed: pin fit, byte identity, R3 sizes. Not checked: a real Bitbucket, Gitea or GitLab host,
Git 2.25–2.41, macOS, the Codex sandbox, machines without long-path support.

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed? (what would make the survivor wrong: silent full download, line endings, long paths, host support, version-check hang, attribute side effects)
- [x] Pairwise incompatibility checked? Surviving configurations listed?
- [x] Hypothesis tested? (H1 survivors and fallback, H3 limit, H4 migration-bundle exception)
- [x] Counter-evidence sought? (every row of the incompatibility table)

**Knowledge handover.** Producer as in the header. Source and epoch: `v3.7.1`; this repository at
`dc5d1b4a`; Git 2.42.0 for Windows; 2026-09-29. Material: X1–X9 and the survivors. Uncertainty: the
Remaining column. Continuation: synthesis (RES) after the Coordinator's gate.

Stage complete: YES
→ User decision: ___
