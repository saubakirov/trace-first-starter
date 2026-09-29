# Trials — TFW_20260929-003444_LFD

Scratch trial record for [EV](EV__TFW_20260929-003444_LFD.md). Every trial ran on 2026-09-29 on the
owner's Windows machine, in the Executor's scratch area outside every real receiver. Paths are shown
by role: `<scratch>`, `<local mirror>`. Nothing in a real receiver, a remote or GitHub changed.

## Method

- **Verbatim extraction.** A scratch harness (not committed) read the indented command block under
  the label `Fetch a tag from the receiver root:` or `An untagged commit:` straight from the given
  `update.md`, replaced only `<tag>`, `<upstream>` and `<SHA>`, and ran each line from a fresh
  receiver root (`git init` plus one commit). It then followed the prose: record the full SHA,
  `.tfw/VERSION` and the tag's `git ls-remote <upstream> refs/tags/<tag>` line; copy the clone's
  `.tfw` to `.tfw/.upstream/.tfw`; for every path of `git ls-tree -r <SHA> -- .tfw` compare
  `git hash-object --no-filters .tfw/.upstream/<path>` (path as an argument) with the listed blob
  id; delete the clone; repeat the `ls-remote` line; run `git ls-files -- .tfw/.upstream`.
  Git Bash copies with `cp -r`, PowerShell with `Copy-Item -Recurse`; deletion with `rm -rf` or
  `Remove-Item -Recurse -Force`. The install harness did the same for `quickstart.md`.
- **Texts.** Candidate `0b755dcada76fe0f22bf285a77b40f812c365c45`: `update.md` blob
  `c630386ef8f161e73af03cb81068f8219facaba6`, `quickstart.md` blob
  `ace33e4e7a665a00b2ba7c52e5a06945d6c78e90`. Earlier runs T1–T7 used the pre-commit text
  `cb25cc2ab91b8121eec41b52b06eff961461daa7`, whose Step 0 (lines 41–64) is byte-identical to the
  Candidate's; only a Step 4 line wrap differs.
- **Sizes.** `size-pack` from `git count-objects -vH` includes pack indexes, so it slightly
  overstates the transfer.
- **Local mirror.** A bare depth-1 copy of `v3.7.1`, later also of the Candidate, with
  `uploadpack.allowFilter` true; set to false for T4 only. It stands in for the upstream where a
  trial must not or cannot use GitHub.

## Step 0, tag route, GitHub `v3.7.1` (AC-1 gate, AC-2)

| # | Environment | Text | Fetch window | `size-pack` | Raw-byte check | Staging copy | Clone deleted | Recheck | Pre-seal |
|---|---|---|---:|---:|---|---:|---|---|---|
| T1b | Git Bash, Git 2.42.0.windows.1 | Candidate | 6.06 s | 679.57 KiB | 95/95 | 95 files | yes | unchanged | 0 entries |
| T2b | Windows PowerShell 5.1.26100, Git 2.42.0.windows.1 | Candidate | 5.07 s | 679.57 KiB | 95/95 | 95 files | yes | unchanged | 0 entries |
| T3b | WSL Ubuntu, Git 2.43.0 | Candidate | 4.42 s | 679.57 KiB | 95/95 | 95 files | yes | unchanged | 0 entries |
| T1 | Git Bash | pre-commit | 6.14 s | 679.57 KiB | 95/95 | 95 files | yes | unchanged | 0 entries |
| T2 | PowerShell 5.1 | pre-commit | 5.19 s | 679.57 KiB | 95/95 | 95 files | yes | unchanged | 0 entries |
| T3 | WSL Ubuntu | pre-commit | 4.62 s | 679.57 KiB | 95/95 | 95 files | yes | unchanged | 0 entries |

Pin observed in each: `clone --branch v3.7.1` gave full SHA `1e3e00e9b7bf0c706cdc12094eadeb4103fc6bbb`,
`.tfw/VERSION` `3.7.1`, and the line `e39a0371d887cc209bf77eb1a94948f75345d956 refs/tags/v3.7.1`. No
command reads the source's `HEAD`. The raw-byte loop took 15.8 s in Git Bash, 6.7 s in PowerShell and
0.4 s in WSL (one `hash-object` process per file).

## Step 0, untagged route and failure cases

| # | Case | Environment | Result |
|---|---|---|---|
| T5 | untagged by full SHA `1e3e00e9…`, GitHub | Git Bash | 5 commands exit 0; 622.81 KiB; 4.92 s; 95/95; clone deleted; pre-seal 0 |
| T6 | the same | PowerShell 5.1 | 622.81 KiB; 4.04 s; 95/95; `-c core.attributesFile=` accepted on `checkout` |
| T4 | host without filter support: `<local mirror>` with `uploadpack.allowFilter` false | Git Bash | clone exit 0 with one line `warning: filtering not recognized by server, ignoring`; `size-pack` 114.51 MiB, above the 2 MiB line, so the text's disclosure applies; payload still 95/95 |
| T12 | fallback forms as the Candidate words them (`--no-checkout` clone; untagged `fetch` without filter; `checkout <SHA> -- .tfw`) | Git Bash, `<local mirror>` | both 114.51 MiB (disclosed by the size rule); the clone holds only `.git` and `.tfw`; 95/95. The trigger itself, Git rejecting an option, cannot occur on Git 2.42/2.43 |
| T7 | hostile line endings: global `core.autocrlf=true` and a user attributes file `* text eol=crlf` (`core.longpaths` kept) | Git Bash, `<local mirror>` | control clone without the flags: 95 of 95 files contain CR; tag route per text 95/95 raw-equal; untagged route per text 95/95 |
| T7-lp | the same config without `core.longpaths`, receiver root of 112 characters | Git Bash | `sparse-checkout set .tfw` exit 128, `Filename too long`, on `.tfw/update_receipts/knowledge-lifecycle/<64 hex>/before/.tfw`; 17 of 95 files not written and flagged by the byte check. Loud, not silent. Only the upstream's own `update_receipts/` reach 138 characters (the rest of `.tfw/` ≤ 55), so a Windows receiver root above about 98 characters needs Git's `core.longpaths` |

Codex probe (ONB §4 item 1) run once in Windows PowerShell 5.1: 679.57 KiB, 95 files, 0 mismatches,
12 s, folder removed. Not run inside a Codex session.

## Install (AC-4)

| # | Environment | Tag chosen | Fetch | Installed `.tfw/` | `editions/` |
|---|---|---|---|---|---|
| T8 | Git Bash | `v3.7.1` from 45 exact of 50 tags (5 suffixed ignored) | 5.50 s, 774.34 KiB | 88 files = tag's `.tfw/` minus `project_config.yaml`, `knowledge_state.yaml`, `update_receipts/`; 88/88 raw-equal | 30/30 raw-equal |
| T9 | PowerShell 5.1 | `v3.7.1` | 5.06 s, 774.34 KiB | 88 files, 88/88 raw-equal | 30/30 raw-equal; 6 of 6 Cyrillic-named files present by name |

The copy followed `quickstart.md`'s existing exclusions from a temporary directory outside the project.

## Release archive (AC-5)

`git archive --format=zip 0b755dca` (attributes from the tree, as GitHub archives): 525,788 bytes;
`tar.gz` 422,842 bytes. 130 files of the tree's 4,079: `.tfw/` 93 (no `project_config.yaml`,
`knowledge_state.yaml` or `update_receipts/`), `editions/` 30, `README.md`, `README.ru.md`,
`README.kk.md`, `LICENSE`, `tools/migrations/2.0.0/` (3). The set equals the allow-list computed from
`git ls-tree` with unquoted paths; 130/130 members byte-equal to their tree blobs; `.gitattributes`
absent. Before commit, `git archive --worktree-attributes` of the Baseline gave 523,485 bytes, 130 files.

## Version line (AC-6), Claude Code shell tool with a 5,000 ms limit

| Case | Scratch receiver | Observed | Line |
|---|---|---|---|
| behind | `.tfw/VERSION` 3.1.0, GitHub upstream | exit 0 in about 4.4 s; 50 tags, 45 exact | installed 3.1.0 · newest 3.7.1 · 11 releases newer · `/tfw-update` now or after this task |
| current | 3.7.1 | exit 0 in 3.94 s | installed 3.7.1 · current · no offer |
| unreachable | upstream at a blackholed address (TEST-NET-1) | the tool returned control at 5 s and moved the process to the background; it ended by itself after 21,048 ms, exit 128 | newest unknown (no answer within 5 s); nothing blocked |
| offline | upstream at an `.invalid` host | exit 128 after 0.35 s, `Could not resolve host` | newest unknown (host not found) |
| upstream itself | this repository, `installed_from: "self"` | no call | no line offer |

No case ran `/tfw-update`. Five further normal calls took 3.17–4.77 s today (research measured
0.9–2.0 s overnight), so on this connection the "about 5 s" limit sits close to the normal cost.

## Trial update through the whole workflow (AC-1 evidence, AC-7, DoD 1, DoD 7)

- **Receiver.** Light-installed from GitHub `v3.7.1` per `quickstart.md` (88 framework files),
  minimal init from the templates (config, `KNOWLEDGE.md`, Claude Code adapter: `CLAUDE.md` block
  and ten command copies), 101 tracked files; then the Candidate's `update.md` installed as its
  update text.
- **Target.** Authorized untagged Candidate `0b755dca` from `<local mirror>`. The fixture's
  `tfw.upstream` pointed at the mirror because the Candidate is unpublished; the config merge
  restored the template's framework-owned value.
- **Why this target.** It is the next update every 3.7.1 receiver makes: this change plus TEQM,
  without the version bump.

| Step | Wall time | Measured parts |
|---|---:|---|
| 0 Pin and fetch | 24.0 s | five commands 2.17 s; `size-pack` 667.22 KiB; copy plus raw-byte check 100/100 in 20.37 s; clone deleted |
| 1 Target history | 28.6 s | pinned `update.md` = installed text; `migrations/3.7.1.md` (installed 3.7.1: verify identity, bytes, unfinished attempts); `knowledge-lifecycle.md` applies with no affected write (no retired keys, no state file, stable entry, no prior receipt) |
| 2 Observe and classify | 55.3 s | 5 new, 13 changed framework files; 7 target state files excluded; Daily group of 5 rows verified package-owned, dormant, byte-equal, no opt-in; config template and manifest unchanged |
| 3 Apply | 32.3 s | copy of 18 files 2.82 s; post-copy raw-byte check against staging 18/18 in 3.41 s; config merge 0.35 s (`tfw.upstream`, `tfw.installed_from` = upstream + full SHA; project keys kept) |
| 4 Adapters to seal | 73.8 s | one adapter sync with validation 3.77 s (9 copies written, 10/10 byte-equal, 1 start and 1 end marker); verification 1.19 s; project checks 0.13 s (template placeholders); cleanup and pre-seal check 0.31 s, 0 entries; receipt 626 words (template 574) written in about 26 s |
| Final message | about 32 s | briefing rendered from the sealed receipt |

From the first network command to the rendered briefing: 5 min 11 s; the transfer itself took
under 1 s of it. Oracle after the update: all 93 installed framework files raw-equal to the
Candidate tree; none of the upstream's own state installed.

Negative control, in a throwaway copy of the receiver before cleanup: `git add -A`, then
`git ls-files -- .tfw/.upstream` listed 100 entries, so the pre-seal check detects staged staging
and the text requires disclosure.

## Cleanup

Scratch receivers, clones and install folders were deleted after measuring; the WSL folders were
removed. The local mirror and the scratch logs stay in the Executor's scratch area until RF is
returned, then are deleted.

---

## Round 2 (TS revision 2): the version line's limit

Round 2 changes one clause of one file: the limit of the version line in `.tfw/conventions.md`, from
about 5 s to about 13 s (HL §12 A5). Candidate `cd4fe89a624897e2d0da2a58e31edb63cce052c7` on branch
`lfd/exec` is one commit after the accepted Candidate `0b755dca`; the difference between them is that one
line. Every trial below ran on 2026-09-29 by the round-2 Executor (`lfd-executor-r2`) in its scratch
area outside every real receiver; paths are shown by role. Nothing in a real receiver, a remote or
GitHub changed. The only remote traffic is `git ls-remote --tags --refs` (about 3 KB, read-only) to the
public upstream and, for the unreachable case, to a documentation-range address that answers nobody.

### Method

- **The rule as written.** A scratch harness (not committed) applies the Candidate's rule text: it reads
  the receiver's `.tfw/VERSION` and `tfw.upstream` (from `.tfw/project_config.yaml`), makes no call when
  `tfw.installed_from` is `"self"`, otherwise makes one `git ls-remote --tags --refs <tfw.upstream>`,
  keeps the exact `vX.Y.Z` tags and prints the row. It enforces no time limit itself.
- **The limit belongs to the tool.** Each check ran as one call of this unit's Claude Code shell tool
  with its `timeout` parameter set to 13,000 ms, the mechanism the rule names. The tool's own message
  is the observation at the limit.
- **Scratch receivers.** `behind` (`.tfw/VERSION` 3.1.0) and `current` (3.7.1) point at the public
  upstream; `blackhole` (3.7.1) points at `https://192.0.2.1/…` (TEST-NET-1); `offline` (3.7.1) at an
  `.invalid` host; `self` carries `installed_from: "self"`.
- **Slow-link stand-in.** A scratch CONNECT proxy on 127.0.0.1 (standard library only, refusing every
  target but `github.com:443`) waits 6.0 s before it opens the tunnel. It is injected through Git's
  environment configuration (`GIT_CONFIG_COUNT`, key `http.proxy`), so the harness and the rule's command
  stay unchanged. It emulates a slow link in front of the real upstream; it is not a real slow network.

### Results

| # | Case | Tool limit | Observed | Row as the rule shows it |
|---|---|---:|---|---|
| R2-1 | behind: 3.1.0 against the public upstream | 13,000 ms | completed, exit 0, 1.28 s; 50 tags, 45 exact | installed 3.1.0 · newest 3.7.1 · 11 releases newer · `/tfw-update` now or after this task |
| R2-2 | current: 3.7.1 | 13,000 ms | completed, 1.11 s | installed 3.7.1 · current · no offer |
| R2-3 | three more ordinary checks (behind), one call | 13,000 ms | 1.31 s, 1.21 s, 1.07 s; the same row | as R2-1 |
| R2-4 | **unreachable**: upstream at a blackholed address | 13,000 ms | the tool returned at its limit with `Command did not complete within its 13s timeout and was moved to the background`; no answer had arrived; the command ended by itself after 21.21 s with `git` exit 128; no process remained | installed 3.7.1 · newest unknown (no answer within about 13 s) · nothing blocked |
| R2-5 | offline control: upstream on an `.invalid` host (not affected by the limit) | 13,000 ms | exit 128 after 0.38 s (round 1: 0.35 s) | newest unknown (host not found) · nothing blocked |
| R2-6 | slow-answer stand-in: 6.0 s in front of the real upstream | 13,000 ms | completed, exit 0, 7.26 s; 50 tags | as R2-1: the real answer is shown |
| R2-7 | the same stand-in under the round-1 limit | 5,000 ms | the tool returned at 5 s with no answer; the command finished by itself, exit 0, 7.29 s after its start, with the same 11-releases-newer answer | would have shown `unknown` although the upstream answered: the case that motivated A5 |

Calibration of the stand-in without a tool limit: 7.34 s, one tunnel. The upstream-itself case makes no
call and is unchanged from round 1; the harness printed its no-call row once as a parse check. No case
ran `/tfw-update`. At the tool's limit the command is not stopped: it runs to its own end and a
completion notice follows, which changes nothing in the row.

### Release archive of the new Candidate (dependency check)

`git archive --format=zip cd4fe89a` (attributes from the tree, as GitHub archives): 525,789 bytes; 130
members equal to the allow-list computed from `git ls-tree`; 130/130 byte-equal to their tree blobs;
`.gitattributes` absent. The same computation for `0b755dca` gives 525,788 bytes and 130/130, so the
one added character is the whole difference.

### Round 2 cleanup

The scratch receivers, the harness, the proxy script with its log, the two archives and the tool's
task output files stay in the Executor's scratch area until this round's RF is committed, then are
deleted by this Executor. The proxy process was stopped after checking that its process ID belonged to
the scratch script; no listener remained on its port and no trial process remained.
