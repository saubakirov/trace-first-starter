# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260929-003444_LFD](../../HL-TFW_20260929-003444_LFD.md)
> Goal: Installing or updating TFW moves only the framework, about one megabyte, by one written method, and a newer release shows in one line when new work starts; the owner decides whether and when to update.
> Producer unit: `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher` · mode deep · OODA loop 1 of 3 (checkpoint met; no extra loop)
> Continuation source: [gate answer](../../journal/20260929-010420__gate_answer__f52c.md) in `40a589444c51f799782cbecc3b590b7390fce09d`

All trials ran on 2026-09-29 against tag `v3.7.1` (annotated tag object `e39a0371…`, commit
`1e3e00e9b7bf0c706cdc12094eadeb4103fc6bbb`), in scratch directories outside the repository, from the
public upstream `https://github.com/saubakirov/trace-first-starter` or from this repository used
read-only as a `file://` server. Reference lists come from `git ls-tree -r v3.7.1` here. Scratch copies
were deleted or stay only in the session scratch area; nothing in a receiver, remote or GitHub changed.

## Dimensions

No alternative is recommended here; Extract and Challenge decide.

| Dimension | Alt A | Alt B | Alt C | Alt D _(if any)_ |
|-----------|-------|-------|-------|-----------------|
| D1 How the payload is obtained | blobless depth-1 clone + `git archive --worktree-attributes` + extraction | blobless depth-1 clone `--sparse` + `sparse-checkout set <paths>` (Git writes the files) | blobless clone without checkout + `--work-tree=<dir> checkout <tag> -- .tfw` | host archive link (tag or commit tarball/zip); or today's full/shallow clone |
| D2 Line-ending control | environment defaults | `-c core.autocrlf=false` given to `clone` (kept in the temp repository) | that plus `core.eol=lf` against attribute-driven conversion | a repository `.gitattributes` text rule for every receiver |
| D3 Byte-identity check | `git hash-object` (filters on) | `git hash-object --no-filters` against `git ls-tree` ids | SHA-256 of bytes against `git cat-file blob` | `git status` in the temp checkout |
| D4 Path set fetched | `.tfw/` (update) | `.tfw/` + `editions/` (install) | plus a path a pinned migration guide names (`tools/migrations/2.0.0/`) | whole tree (today) |
| D5 Where the payload is staged | `.tfw/.upstream/` without `.git` (today) | temp clone outside the receiver, payload read in place | temp clone inside `.tfw/.upstream/` (nested `.git`) | — |
| D6 Version-check command and limit | `git ls-remote --tags --refs` with no limit | same with the agent tool's time limit | same with `http.lowSpeedLimit/Time` | a host API (`/releases`) or no check |
| D7 Which tag counts as newest | top of `--sort=-v:refname` | highest exact `vX.Y.Z` | `versionsort.suffix=-` then top | — |
| D8 Archive-only `.gitattributes` form | none (today) | allow-list: `/* export-ignore`, then `-export-ignore` per framework path | deny-list per development directory | allow-list that also drops `.tfw/` project state |
| D9 How the upstream recognises itself | `tfw.installed_from: "self"` | `tfw.upstream` equals `origin` URL | presence of development folders | — |

## Findings

### G1 — The measuring rig sees both known failures; R1's explanation holds

- **Byte identity.** A local `git archive` of `.tfw` with `-c core.autocrlf=true` wrote CRLF into all
  95 files: 95/95 differ by raw hash and by SHA-256, yet `git hash-object` with filters on reports
  0 differences. **A filter-applying hash cannot prove byte identity on Windows.** The rig therefore
  compares `hash-object --no-filters` and SHA-256 of raw bytes with the tag's blob ids.
- **Positive control, no network** (this repository as `file://` server, filters allowed only for the
  spawned `upload-pack`):

| Run | Lazy fetches | Stored objects after | Wall time |
|---|---:|---:|---:|
| blobless clone, trees only | — | 164,385 B | 0.2 s |
| + `git archive` **without** flag | **1 batch, every missing blob** | 113,251,114 B (108 MiB) | 13.1 s |
| + `git archive --worktree-attributes` | **93, one per blob** | 583,081 B | 72.0 s, then background `gc` |
| + `--work-tree` pathspec checkout (D1-C) | 93, one per blob | 583,081 B | 75.3 s |
| `--sparse` clone + `sparse-checkout set .tfw` (D1-B) | 2 batches (root files, `.tfw`) | 664,249 B | 2.6 s |

  Git 2.42.0 source agrees: without `--worktree-attributes`, `write_archive_entries` loads the whole
  tree into an index to read attributes, and `object_file_to_archive` passes every file through
  `convert_to_working_tree`, the same line-ending conversion a checkout applies.
- An early control run whose server silently lacked filter support printed one warning line,
  `filtering not recognized by server, ignoring`, and stored a full 120 MB pack. Challenge tests that
  case on purpose.

### G2 — Update candidates against GitHub

| Method | Shell | Transferred (stored packs) | Wall time | Lazy fetches | Files byte-equal |
|---|---|---:|---:|---:|---|
| D1-B `.tfw` | Git Bash | 670,042 B (0.64 MiB) | 8.2 s · 6.9 s | 2 batches | 95/95 · 95/95 |
| D1-B `.tfw` | PowerShell 5.1 | 670,042 B | 5.0 s · 4.8 s | 2 batches | 95/95 · 95/95 |
| D1-A `.tfw` | Git Bash | 594,479 B (0.57 MiB) | 2.1 s clone + **156.2 s** archive | **93** | 95/95 |
| D1-A `.tfw` | WSL Ubuntu | 594,479 B | 1.9 s + **91.7 s** | per blob | 95/95 |
| R1's first method (no flag), **once** | Git Bash | 119,613,804 B (114.1 MiB) | 2.0 s + 39.2 s = **41.2 s** | 1 batch | 95/95 (deleted afterwards) |

Exact D1-B commands, identical in both Windows shells and in WSL:
`git clone -c core.autocrlf=false --filter=blob:none --sparse --depth 1 --branch v3.7.1 <upstream> <tmp>`
then `git -C <tmp> sparse-checkout set .tfw`. The only tool is Git. The adapter byte counter rose by
1.35 and 1.92 MiB for the two Git Bash D1-B runs. Other traffic on the machine counts too, so that is
an upper bound.

**New against R1:** the flag fixes the bytes but not the time. D1-A makes one network round trip per
file, so its duration grows with the number of framework files. On this connection it took longer than
downloading the whole 114 MiB (156 s against 41 s). R1's receipt recorded no download time.

### G3 — Line endings, file kinds and names

- No `.tfw/` or `editions/` blob at `v3.7.1` contains CR or NUL. The 125 files are text (`md`,
  `yaml`, `json`, `template`, extensionless `VERSION`, one `.py`, one `.svg`, one `.html`). There are no
  symbolic links and no executable bits; every mode is `100644`.
- Under the Git for Windows installer default (`core.autocrlf=true`, emulated with `-c`), **D1-B and
  D1-A both rewrite all 95 files to CRLF.** This machine's user config (`input`) hides that. Pinning
  `-c core.autocrlf=false` on the clone gave 95/95 byte-equal in every run above.
- `editions/02-assisted/` holds six files with Cyrillic path names. `.tfw/` names are ASCII. The longest
  path is 138 characters, in `.tfw/update_receipts/`.
- `editions/` at `v3.7.1` has **30 files** (293,360 B). HL §2 says 24.

### G4 — Shell and tool traps around archives (PowerShell 5.1)

| Extraction of a `git archive` | Result |
|---|---|
| `tar` as PowerShell resolves it here: an old third-party GNU tar earlier on PATH | exit 2; a stray `pax_global_header` file; **2 of 95 files missing** (the 138-character paths) |
| Windows built-in `tar.exe` | `.tfw` 95/95 correct; the **6 Cyrillic `editions` names are garbled** as OEM code page text |
| `git archive … \| tar -x -f -` piped in PowerShell 5.1 | `Unrecognized archive format`, 0 files: 5.1 turns a native byte stream into strings (Microsoft Learn; fixed only in PowerShell 7.4+) |
| `--format=zip` + `Expand-Archive` | 95/95 and 30/30 byte-equal, names intact |
| GNU tar 1.34 in Git Bash | 95/95 and 30/30 byte-equal |

D1-B writes no archive and runs no tool beyond Git, so none of these traps apply to it. In PowerShell it
wrote the Cyrillic names correctly: 30/30.

### G5 — Codex sandbox: unobserved

`codex sandbox` (Codex CLI 0.152.1, Windows restricted-token sandbox) requires
`--permission-profile <NAME>` from a `[permissions]` table in the active Codex configuration. The run
stopped with `default_permissions requires a [permissions] table`, and a plain run failed on the
missing argument. Supplying a profile would change Codex configuration or define the policy myself, and
the gate answer excludes both. It would also observe a policy of my choosing, not the one Codex
sessions run under. **Network and fetch behaviour inside the Codex sandbox stay unobserved.** No login,
model call, configuration change or elevation happened. Both runs ended at argument or config
validation.

### G6 — H3: cost and failure of the version check

| Case | Git Bash (2.42.0) | PowerShell 5.1 | WSL Ubuntu (2.43.0) |
|---|---:|---:|---:|
| `git ls-remote --tags --refs <upstream>` | 1.56 · 1.15 · 1.43 s; 50 tags; 2,938 B | 1.39 · 1.31 s | 1.97 · 0.86 · 0.92 s |
| unknown host (`.invalid`) | 0.27 s, exit 128 | 0.26 s, exit 128 | 0.14 s |
| refused connection (dead local proxy) | 2.32 s | — | 0.01 s |
| blackholed address (TEST-NET-1) | **21.3 s** | — | **131.0 s** |
| blackholed + `http.lowSpeedLimit=1`, `lowSpeedTime=5` | 21.2 s | — | 133.1 s |

- Git 2.42's config keys have no connect timeout. `http.lowSpeed*` does not bound the connection
  phase. **Where packets are dropped, only a time limit outside Git keeps the check short.**
- Tags: 50, of which five are `v2.0.0-dirty…` pre-releases. `--sort=-v:refname` puts every
  `v2.0.0-dirty.N` **above** `v2.0.0`, so "take the top line" would count a suffixed tag as newer. The
  top is `v3.7.1` today only because no newer pre-release exists.
- The upstream's own config has `installed_from: "self"` ("this repository IS the upstream"). A
  receiver records `source@tag`. The config template says the same.
- Offline was simulated (unknown host, refused, blackholed), not observed with the network off.

### G7 — H4: what install reads

- The root README's install prompts read `editions/README.md` to choose Assisted or Full, then copy
  `editions/02-assisted/` or `.tfw/`. `quickstart.md` copies only `.tfw/` minus `project_config.yaml`,
  `knowledge_state.yaml`, `update_receipts/`, `.upstream/` and other project state.
- `init.md` creates the receiver's root README route, `AGENTS.md` block, `KNOWLEDGE.md`, config and
  adapters from `.tfw/templates/` and `.tfw/adapters/`. All 8 manifest sources sit under `.tfw/`.
  **Nothing outside `.tfw/` and `editions/` is read from the source.** The README files and `LICENSE`
  matter only for archives.
- The `v3.7.1` tree holds upstream project state inside `.tfw/`: `project_config.yaml`,
  `knowledge_state.yaml` and `update_receipts/knowledge-lifecycle/…`. The quickstart exclusions cover
  them.
- **An exception for updates:** the `2.0.0`, `3.0.0`, `3.1.0` and `3.2.0` migration guides and the
  changelog tell a pre-2.0 receiver to "acquire `tools/migrations/2.0.0/`" (3 files, 58 KB) from the
  same pinned release. A `.tfw/`-only fetch leaves it out. Cone mode can add it, but also pulls the
  other five files directly in `tools/`.
- D1-B install set (`sparse-checkout set .tfw editions`): 766,242 B (0.73 MiB). Git Bash 5.4 s,
  PowerShell 5.8 s, WSL 5.2 · 4.8 s. 95/95 and 30/30 byte-equal in all three.

### G8 — §3 claim 3: an archive-only `.gitattributes`, measured locally

Candidate allow-list `/* export-ignore`, then `-export-ignore` for `/.tfw`, `/editions`, the three
README files and `/LICENSE`. It was committed only in a scratch shared clone on top of `v3.7.1`.

- `git archive --format=zip`: **571,807 B (0.55 MiB)**; `tar.gz` 469,640 B. The same tag today
  gives 187,577,223 B (178.9 MiB). Contents: `.tfw/` 95 files, `editions/` 30, `LICENSE`, 3 README
  files; 129 files in all.
- An update-style `git archive <commit> .tfw` still gives 95 files, with or without the flag.
- **`git archive <commit> tools/migrations/2.0.0` gives 0 files when attributes come from the tree**
  (no flag, and GitHub's archive), and 3 files with `--worktree-attributes`. A sparse clone is
  unaffected: export attributes act only on archives.
- `git archive` outside task history appears only in `update.md`, its byte copy
  `.claude/commands/tfw-update.md`, and one changelog entry. Tools and CI (`docs.yml`: checkout, blob
  size check, mkdocs) use no archive. No `.gitattributes`, `export-ignore` or `export-subst` exists
  anywhere outside history.
- GitHub Docs: source archives "are generated by the `git archive` command". Tag archives "may have
  different contents" if the tag moves, while a commit-ID archive keeps the same contents. Community
  reports confirm GitHub honours `export-ignore`. The real GitHub archive stays unobserved until the
  owner pushes.

### G9 — Fit with the unchanged pin (observed in a D1-B clone)

`git rev-parse v3.7.1` gives the tag object (type `tag`); `rev-parse 'v3.7.1^{commit}'` and `HEAD` give
the full commit SHA. `git show HEAD:.tfw/VERSION` reads `3.7.1`. `git status --porcelain -- .tfw` is
empty. `git ls-remote <upstream> refs/tags/v3.7.1 'refs/tags/v3.7.1^{}'` rechecks both ids remotely.
Only the one tag is fetched, and the clone is shallow. Nothing reads live `HEAD` of the source.

### G10 — Input for H2, iteration 2

The old method's download took ≈41 s on this connection (114 MiB, ≈2.8 MiB/s). D1-B takes 5–8 s. This
connection's time only; a slower link scales the 114 MiB part.

### External sources

- GitHub Docs, [Downloading source code archives](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives): generated by `git archive`; tag archives can change, commit archives do not.
- Git, [git-archive](https://git-scm.com/docs/git-archive): attributes come from the archived tree by default; `--worktree-attributes` reads the working tree instead. It says nothing about line-ending conversion.
- Git source [archive.c at v2.42.0](https://github.com/git/git/blob/v2.42.0/archive.c): `convert_to_working_tree` per file; whole-tree `unpack_trees` without the flag.
- Microsoft Learn, [What's New in PowerShell 7.4](https://learn.microsoft.com/en-us/powershell/scripting/whats-new/what-s-new-in-powershell-74) and [about_Redirection](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_redirection): byte-preserving native pipes only from 7.4.
- Git [2.25.0 release notes](https://github.com/git/git/blob/master/Documentation/RelNotes/2.25.0.adoc): dedicated `sparse-checkout` command. The first Git version with `clone --sparse` was not confirmed from notes; observed working in 2.42 and 2.43.
- Secondary: [wgdd.de](https://www.wgdd.de/2019/03/exclude-files-from-being-exported-into.html) on GitHub archives honouring `export-ignore`.

Web actions: 7 against a soft limit of 5 (5 fetched sources, 1 search, and 1 retry after a 404).
Project files: 15, at the soft limit.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| D1-B moves 0.64 MiB (update) / 0.73 MiB (install) in 5–8 s with 2 batch fetches, byte-equal in Git Bash, PowerShell 5.1 and WSL, with Git as the only tool | a Git host without filter support (silent full download seen once); Git older than 2.42; proxies |
| D1-A (R1's fix) is light but makes one round trip per file: 156 s in Git Bash, 92 s in WSL | whether any receiver's Git lacks `--sparse` (floor unconfirmed) |
| Archive output and checkouts follow `core.autocrlf`; the installer default rewrites all 95 files; filtered `hash-object` hides it | an attribute-driven conversion (user attributes file) against `core.autocrlf=false` alone |
| PowerShell 5.1: native pipes corrupt archives; `tar` resolution and name encoding differ; zip + `Expand-Archive` works | none for D1-B; they bind only an archive fallback |
| R1's explanation verified: no-flag archive = one whole-tree prefetch (108 MiB locally, 114.1 MiB from GitHub, 41 s) | — |
| H3: 0.9–2.0 s, 2,938 B; unknown host ≤0.3 s; blackholed 21 s (Windows) / 131 s (Linux); Git has no connect limit | Codex sandbox behaviour; real offline |
| Suffixed tags sort above releases; the upstream carries `installed_from: "self"` | — |
| H4: install reads only `.tfw/` and `editions/`; update needs `tools/migrations/2.0.0/` for pre-2.0 receivers | — |
| Claim 3 candidate: 0.55 MiB zip, 129 files, `.tfw/` unaffected, but the migration bundle vanishes from tree-attribute archives | the GitHub archive itself (needs the owner's push) |
| Codex sandbox: unobserved (needs a configured permission profile) | macOS unobserved |

**Stage decisions.**
1. Byte identity is judged only by raw bytes (`--no-filters` hash and SHA-256), never by a filtered
   hash or `git status`.
2. D1-A and D1-C stay as measured comparators, not eliminated. Extract maps D1-B, D1-A and the archive
   link as the configurations that differ in trade-offs.
3. The Codex sandbox is closed as unobserved for this iteration, with the reason in G5.

**Metacognitive check.** New, not merely confirmed: the per-file round trips of R1's fix;
line-ending conversion inside `git archive` masked by filtered hashes; three PowerShell and tool traps;
no connect limit in Git; the tag sort pitfall; the migration bundle's conflict with claim 3;
`installed_from: "self"`; the editions count. Confirmed: R1's prefetch explanation and H4's path set.
Not checked: macOS, other Git hosts and older Git versions. Challenge covers what the machine allows.

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed? (Gather part: methods, rig, H3, H4, claim 3; Codex sandbox answered as unobserved)
- [x] Dimensions identified?
- [x] Hypothesis tested? (H1, H3, H4)
- [x] Counter-evidence sought? (installer default line endings, PowerShell pipes and tools, blackholed network, no-flag and per-blob fetch, archive attributes on the migration bundle)

**Knowledge handover.** Producer as in the header. Source and epoch: `v3.7.1` from GitHub and from
this repository, Git 2.42.0 for Windows and 2.43.0 in WSL, on 2026-09-29. Inspected: the files named
above plus scratch trials. Material: G1–G10. Uncertainty: the Remaining column. Continuation: Extract
after the Coordinator's gate.

Stage complete: YES
→ User decision: ___
