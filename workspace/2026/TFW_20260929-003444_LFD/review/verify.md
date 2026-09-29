# Verify — "Do the material claims hold?"
> **Mindset:** Auditor. RF is a declaration, not a fact. Open files, run necessary checks, compare
> accepted claims with reality, and state the limits.
> **Test:** "Would the evidence establish this claim for this subject, revision and environment without RF?"
> Map: [map.md](map.md) at `973006d8`

All runs below took place on 2026-09-29 between 11:30 and 11:55 +05:00 on the owner's Windows 11
machine, in this Reviewer's own scratch area (`<scratch>`, outside the repository and every real
receiver), with Git 2.42.0.windows.1 and Windows PowerShell 5.1.26100.9549. The accepted subject is
Candidate `0b755dcada76fe0f22bf285a77b40f812c365c45`, read from the shared object store; command
blocks were extracted verbatim from `git show 0b755dca:<file>` by label, and only `<tag>`,
`<upstream>`, `<SHA>` and `<temp>` were substituted. No receiver, remote or GitHub state changed;
GitHub was read only (light fetches of 0.6–0.8 MiB and `ls-remote`).

**Hostile environment.** Every Step 0 and install run used a scratch global configuration
(`GIT_CONFIG_GLOBAL`) with `core.autocrlf=true`, `core.attributesFile` pointing to a file containing
`* text eol=crlf`, and `core.longpaths=true`, on top of the Git for Windows system default
`core.autocrlf=true`. `core.longpaths` was needed because the scratch root is 99 characters long; its
absence was tested separately (V8).

## Selection Argument

| Claim IDs | Risk / criticality | Affected behavior / dependencies | Environment | Oracle / authority | Evidence gap / limit | Selected verification and why |
|---|---|---|---|---|---|---|
| C1, C4, C5, C6 | High: the method ships to every receiver | clone, sparse set, size, copy, raw-byte check, deletion, recheck, pre-seal | Git Bash, PowerShell 5.1, GitHub | TS AC-1 gate; DoD 1 | EV runs were the Executor's | TS-required independent re-run in both shells under a hostile line-ending setup (V1, V2) |
| C4 | High on Windows | the two `-c` settings | Git Bash | RES iteration 1 D1, D3 | none shown without the settings in this review | counterfactual control without the settings (V3) |
| C2 | Medium: untagged updates are rare but authorized | promisor registration by URL | both shells, GitHub | TS AC-1 item 4 | deviation from TS §6 | re-run by full SHA and read the written config (V4, V5) |
| C3 | High: DoF 2 | size check, fallback wording | local plain mirror | DoF 2, AC-2 item 3 | real filter-less hosts unobservable | negative control and fallback forms (V6, V7) |
| C16 | Medium | long paths | Git Bash | E10 | E10 partial | run without `core.longpaths` (V8) |
| C1 (next target) | Medium | a tree that carries `.gitattributes` | local mirror of the Candidate | DoD 1 "current payload" | — | untagged route to the Candidate itself (V9) |
| C6 | High: DoF 1 | pre-seal check | scratch receiver | TS AC-7 item 4 | gitlink case not in EV | staged copy and staged gitlink controls (V1, V10) |
| C8 | High: first contact | quickstart Step 1, copy exclusions, Cyrillic names | both shells, GitHub | TS AC-4 gate | README prompts are text | verbatim install runs and three-language reading (V11, V12, V13) |
| C9 | Medium | `export-ignore` allow-list | local Git | TS AC-5 | GitHub archive unobservable before a push | local archive audit, old-method effect (V14) |
| C10 | Medium: DoF 3 | `ls-remote` cost, tag filtering, tool bound | Claude Code shell tool | TS AC-6 | card rendering by a fresh Coordinator | timing, counts, unreachable and offline cases (V15) |
| C5 | High: DoD 3 | `clone --branch` resolution | synthetic local repository | DoD 3, D70 | corner case untested in EV | same-named branch probe (V16) |
| C7 | High: DoF 5 | Step 3–4 hunks, receipt template | text | TS AC-7 | — | whole-diff reading (V17) |
| C11 | Medium | budget, copy, form | Git | TS AC-8 | — | `wc -w`, `cmp`, path lists, command hygiene (V18) |
| C12, C15 | Authority floor | accounting method, Baseline epoch | PowerShell 5.1 | TS §4 | Baseline moved after approval | exact NUL-safe replay against both Baselines (V19) |
| C13 | Identity floor | Candidate reachability and role separation | Git | TS §4 Candidate rule | — | branch, parentage, per-commit file sets (V20) |
| C14 | Safety floor | every committed line | local guard | TS §4 M1, DoF 6 | pattern-based | guard over all 41 task commits plus a positive control (V21) |
| C17, C18 | Low | build gate; economics file | Python 3.13 | project config; economics README | — | extracted-tree test run; helper validation (V22, V23) |

## Verification Log

### V1: C1, C4, C5, C6 — tag route, Git Bash, GitHub `v3.7.1`
- **Accepted claim / authority:** Step 0 run verbatim stages only the pinned payload plus the named remainder, under 2 MiB, every file raw-byte-equal (TS AC-1, DoD 1).
- **Subject tuple:** `update.md` blob `c630386e` at `0b755dca`; Git Bash, Git 2.42.0; GitHub `v3.7.1`; hostile configuration; fresh receiver (`git init` plus one commit, root 105 characters).
- **Action or evidence:** the three extracted lines, then the prose: full SHA by `rev-parse HEAD`, `.tfw/VERSION`, the tag's `ls-remote` line, `cp -r` of the clone's `.tfw` to `.tfw/.upstream/.tfw`, `hash-object --no-filters` per `ls-tree` path, deletion, recheck, `git ls-files -- .tfw/.upstream`; then `git add -A` as a negative control.
- **Observed:** clone 5.35 s, sparse set 3.64 s, `count-objects` 0.12 s, all exit 0; `size-pack: 679.57 KiB`; full SHA `1e3e00e9b7bf0c706cdc12094eadeb4103fc6bbb`, `VERSION` 3.7.1, line `e39a0371d887cc209bf77eb1a94948f75345d956 refs/tags/v3.7.1`; clone top level: `.git`, `.gitignore`, `.tfw` and eight top-level files (the named remainder); the clone's own config carries `core.autocrlf false` and an empty `core.attributesfile`; 95/95 raw-equal, 95 staged files, 0 CR bytes (Python byte count); clone deleted; recheck unchanged; pre-seal 0 entries; after `git add -A`, 95 entries.
- **Limit:** the text names the copy and the deletion as exact operations on exact paths, not as shell commands (AC-1 item 1 says "names exact commands"); any faithful copy is caught by the raw-byte check, and a PowerShell deletion without `-Force` fails loudly on read-only pack files. A receiver outside Git cannot run the pre-seal check (nothing can be staged there).
- **Result:** HOLDS

### V2: C1, C4, C5 — tag route, Windows PowerShell 5.1
- **Accepted claim / authority:** as V1.
- **Subject tuple:** same text; `Invoke-Expression` of each extracted line; `Copy-Item -Recurse`, `Remove-Item -Recurse -Force`; hostile configuration.
- **Observed:** clone 3.31 s, sparse set 1.64 s, exit 0; `size-pack: 679.57 KiB`; same SHA, `VERSION` and tag line; 95/95 raw-equal; 0 files with CR; clone deleted; recheck unchanged; pre-seal 0.
- **Limit:** none beyond V1.
- **Result:** HOLDS

### V3: C4 — counterfactual without the two settings
- **Accepted claim / authority:** `-c core.autocrlf=false -c core.attributesFile=` is what keeps bytes raw.
- **Subject tuple:** V1 with only those two settings removed from each command; same hostile configuration.
- **Observed:** `size-pack: 679.57 KiB`; 0/95 raw-equal; all 95 staged files contain CR (13,681 CR bytes).
- **Limit:** none.
- **Result:** HOLDS — the settings are necessary under the installer default plus a user attributes file, and the raw-byte check detects their absence.

### V4, V5: C2 — untagged route by full SHA, both shells, GitHub
- **Accepted claim / authority:** `init`, sparse set, filtered `fetch --depth 1 <upstream> <SHA>`, `checkout FETCH_HEAD` with the two settings, without `remote add` or promisor configuration (RF decision 2).
- **Subject tuple:** extracted five lines; SHA `1e3e00e9…`; hostile configuration.
- **Observed:** Git Bash: five commands exit 0; `size-pack: 622.81 KiB`; window 5.22 s; Git wrote `remote.https://github.com/saubakirov/trace-first-starter.promisor true` and `…partialclonefilter blob:none` itself; 95/95 raw-equal; 0 CR. PowerShell 5.1: exit 0; 622.81 KiB; 3.86 s; the same promisor keys; 95/95; 0 CR.
- **Limit:** Git 2.42 only (EV E4 adds 2.43 in WSL, not re-run).
- **Result:** HOLDS

### V6: C3 — host without filter support
- **Accepted claim / authority:** a silent full download is exposed by the size check (DoF 2).
- **Subject tuple:** a bare depth-1 mirror of `v3.7.1` built locally from this repository's objects (`file://`, no network; `uploadpack.allowFilter` unset); tag route verbatim.
- **Observed:** clone exit 0 with one line `warning: filtering not recognized by server, ignoring`; the clone's config still says `promisor true` / `partialclonefilter blob:none`; `size-pack: 114.43 MiB`, above the 2 MiB line, so the text's disclosure applies; payload 95/95.
- **Limit:** emulated plain host, not Bitbucket or another real one.
- **Result:** HOLDS — only the size figure tells the truth, and the text requires reading it.

### V7: C3 — fallback forms as worded
- **Accepted claim / authority:** "repeat without `--filter=blob:none`, `--sparse` and `sparse-checkout` (clone `--no-checkout`), writing only `.tfw` by … `checkout <SHA> -- .tfw`".
- **Observed:** clone `--no-checkout` exit 0; `size-pack: 114.43 MiB` (disclosed by the same size rule); checkout exit 0; the clone holds only `.git` and `.tfw` (95 files); 95/95 raw-equal.
- **Limit:** the trigger itself, Git rejecting an option, cannot occur on Git 2.42.
- **Result:** HOLDS

### V8: C16 — long paths without `core.longpaths`
- **Observed:** filter-capable local mirror, receiver root 105 characters: `sparse-checkout set .tfw` exit 254 with `Filename too long` on `.tfw/update_receipts/knowledge-lifecycle/<64 hex>/before/.tfw/…`; `.tfw` not written (`VERSION` empty); raw-byte check 0/95.
- **Limit:** EV E10 reported exit 128 and 17 of 95 files missing at a 112-character root; the detail differs, the loudness does not.
- **Result:** HOLDS — loud, not silent; named as a limit in E10 and RF §6 item 4.

### V9: C1 — the Candidate itself as the next target
- **Observed:** untagged route from a filter-capable local mirror of `lfd/exec`: 667.48 KiB (EV E12: 667.22 KiB); the tree's new `.gitattributes` is checked out at the clone root; 100/100 raw-equal; 0 CR under the hostile configuration.
- **Result:** HOLDS — the new attributes file does not alter checkout bytes.

### V10: C6 — pre-seal check against a staged gitlink
- **Observed:** with a nested repository at `.tfw/.upstream/.clone`, `git add -A` stages mode `160000 … .tfw/.upstream/.clone`; `git ls-files -- .tfw/.upstream` lists that 1 entry.
- **Result:** HOLDS — the check covers both staged staging files (V1: 95) and a gitlink.

### V11, V12: C8 — install from `quickstart.md`, both shells
- **Subject tuple:** `quickstart.md` blob `ace33e4e` at `0b755dca`; `<tag>` chosen by the text's rule from `ls-remote`; `<temp>` outside any project; copy by the unchanged exclusions (`project_config.yaml`, `knowledge_state.yaml`, `update_receipts/`, `.upstream/`).
- **Observed:** `ls-remote` 1.51 s (Git Bash) and 1.02–1.31 s (PowerShell): 50 tags, 45 exact, highest `v3.7.1`; clone and sparse set exit 0 in both; `size-pack: 774.34 KiB` in both; installed `.tfw/` 88 files, 88/88 raw-equal to the tag tree minus the exclusions; `editions/` 30/30 raw-equal; 0 CR; PowerShell: the 6 Cyrillic-named files under `editions/02-assisted/шаблоны/` present by name and byte-equal.
- **Limit:** the README prompts were not run end to end; their commands are byte-identical to `quickstart.md`'s. The prompts carry no size check or fallback, and for Full they hand over to `quickstart.md`, whose Step 1 may fetch a second time (under 1 MiB).
- **Result:** HOLDS

### V13: C8 — three-language reading
- **Action:** read `README.md`, `README.ru.md`, `README.kk.md` new-project and existing-project prompts and the "Updating TFW" hint against the English meaning.
- **Observed:** the Russian and Kazakh prompts say "fetch only the framework of the latest release into `<temp>`; `<tag>` is the newest `vX.Y.Z` without a suffix in `ls-remote`", carry the identical two commands, and hand the Full copy to `quickstart.md` in `<temp>`; the hints say that a project on 3.7.1 or earlier still has the old fetch text (≈114 MiB) and should ask once for the light fetch, then continue the target's Step 0 from the size check. Kazakh «жұрнақсыз» (without a suffix), «релиз», «фреймворк»; Russian «выпуск», «фреймворк». English "highest" and Russian/Kazakh "newest" coincide for release tags. No divergence in commands, paths, placeholders or conditions.
- **Result:** HOLDS

### V14: C9 — release archive
- **Observed:** `git archive --format=zip 0b755dca` → 525,788 bytes (`tar.gz` 422,842); 130 files, exactly the allow-list computed from the tree (`.tfw` 93 without the upstream's `project_config.yaml`, `knowledge_state.yaml`, `update_receipts/`; `editions` 30; three READMEs; `LICENSE`; `tools/migrations/2.0.0/` 3); 130/130 byte-equal to tree blobs; `.gitattributes` absent. The Baseline's archive is 188,283,035 bytes and 4,075 files. Side effect on the old update method: `git archive 0b755dca .tfw` now yields 93 files instead of 100, omitting only the seven upstream-state files that the receiver copy excludes anyway.
- **Limit:** GitHub's own archive stays unobserved until the owner's separate push (TS-permitted DEFERRED).
- **Result:** HOLDS

### V15: C10 — version line
- **Observed:** rule text at `conventions.md` lines 1094–1101 states every AC-6 element (first row; installed `.tfw/VERSION` against the newest exact `vX.Y.Z` at `tfw.upstream`; suffixed tags never count; one `ls-remote --tags --refs` under about 5 s on the agent's tool, or skip; how many newer and `/tfw-update` now or after; unknown with reason, nothing blocked; `installed_from: "self"` no call; never updates). One call: 1.32 s, 2,938 bytes, 45 exact tags, newest 3.7.1; installed 3.1.0 → 11 newer, 3.7.1 → 0; 5 suffixed tags ignored. Unreachable `192.0.2.1` with the shell tool's 5,000 ms limit: the tool returned control at 5 s and moved the process to the background, where it ended after 21,062 ms with exit 128. Unresolvable `.invalid` host: exit 128 in 0.28 s.
- **Limit:** Claude Code only; the card's rendering by a fresh Coordinator under `plan.md` was observed neither in EV nor here. `plan.md` Read Contract row 2 does not list `.tfw/VERSION`, `tfw.upstream` or `tfw.installed_from`; the rule names them itself.
- **Result:** HOLDS

### V16: C5 — pin semantics of `clone --branch <tag>`
- **Action:** old and new Step 0 compared; synthetic local repository with tag `v1.0.0` on commit A and a branch also named `v1.0.0` on commit B; canonical upstream's branch names read with `ls-remote --heads`.
- **Observed:** every listed guarantee is present in the new text (see the AC-3 comparison below). `git clone --depth 1 --branch v1.0.0` checked out B, the branch; `ls-remote <upstream> refs/tags/v1.0.0` returns only the tag object line, while `'refs/tags/v1.0.0^{}'` returns A; `--branch refs/tags/v1.0.0` is refused. The old text's "Resolve the object" with a revision lookup prefers the tag. The canonical upstream has 1 branch (`master`) and none named like a version tag.
- **Limit:** a corner case; exposure today is nil on the canonical upstream.
- **Result:** HOLDS for the accepted subject; latent corner recorded as observation O1.

| Guarantee | Old Step 0 (Baseline) | New Step 0 (Candidate) | Meaning |
|---|---|---|---|
| operator names the target | "The operator names a tag or explicitly authorizes an untagged commit." | same sentence | unchanged |
| one object | "Resolve the object" in a local checkout | `clone … --depth 1 --branch <tag>` or `fetch --depth 1 <SHA>` | unchanged, except a same-named branch would win (O1) |
| `VERSION` equals the tag | "read its VERSION, and for a tag require `v{VERSION}`" | "the clone's `.tfw/VERSION` (a tag requires `v{VERSION}`)" | unchanged |
| full SHA recorded | "Record locator, full SHA, version and source path" | "Record locator, full SHA, size, the clone's `.tfw/VERSION` … and a tag's … line" | unchanged; "source path" has no object once the clone is deleted |
| immutability recheck | "Recheck immutability before adapter sync." | the tag's `ls-remote` line "rechecked unchanged before adapter sync" | unchanged, now exact |
| no live source `HEAD` | Read Contract | Read Contract unchanged; no command reads `HEAD` | unchanged |
| untagged labelling | paragraph | same paragraph | unchanged |

### V17: C7 — procedure removals and kept checks
- **Observed:** the Candidate touches `update.md` in exactly four hunks: Step 0's fetch paragraph (lines 41–64), Step 3's first sentence ("then check copied files raw-byte-equal to staging (the last payload check)"), Step 4's rejection list ("duplicate blocks or drift", "second-run diff" removed; the "one marker-bounded block" sentence stays), and Step 4's cleanup ("before sealing, `git ls-files -- .tfw/.upstream` must print nothing; disclose any entry", replacing "only when safe"). Revalidation (Step 3 knowledge lifecycle), migration obligations and equal-version re-observation (Step 1), project checks (Step 4 verification list), the TEQM economics sentences, the Daily prewrite gate and the final message are byte-unchanged. The receipt template changes only the provenance cue, the verification column header and the note ("never pasted output"). `conventions.md` §9 still requires exactly one managed block between exact `TFW:{NAME}` markers.
- **Limit:** removal costs come from the Executor's one synthetic trial (E12, E22), not re-run.
- **Result:** HOLDS — each removal is one approved under HL §12 A3; no protecting check was removed.

### V18: C11 — budget and form
- **Observed:** `wc -w` of the Candidate `update.md` 1,492 (Baseline 1,348; A4 ceiling 1,500); `cmp` with `.claude/commands/tfw-update.md` equal, both blob `c630386e`; no `.cursor/` copy exists; parent → Candidate changes exactly 9 paths, the only new file `.gitattributes` (mode 100644); no script, hook or executable; 0 occurrences of `$0`–`$9` or `$ARGUMENTS` in added lines; sparse patterns `.tfw` and `.tfw editions`, none beginning with `/`. `git diff --name-only 49703481 0b755dca` returns 15 paths: the 9 above plus six task records (HL, TS, status and three journal events) from Coordinator commits between the Baseline and the Candidate's parent.
- **Limit:** 8 words of headroom remain under the A4 ceiling.
- **Result:** HOLDS; EV E23's "→ 9 paths" is inaccurate for the cited command (observation O5).

### V19: C12, C15 — accounting replay
- **Observed:** see Accounting Replay below; the TS commands reproduce RF exactly under the governing Baseline.
- **Result:** HOLDS

### V20: C13 — accepted-result identity
- **Observed:** `lfd/exec` contains `0b755dca`; it is the only commit in `a5c90d2b..lfd/exec`, parent `a5c90d2b`, committed 10:56:45; RF/EV at `b9a7ae57` (11:15:39) and the `ONB → RF` status at `98b1a35e` (11:16:14) come after it; trials T1b–T3b ran on its `update.md` blob. Executor commits contain only VALUE, ONB, RF, EV, economics and its own status/journal paths; Coordinator commits contain only HL, TS, status, journal, `research/iterations.yaml` and the received Researcher economics file; Researcher commits contain only research files. Executor mutation has stopped on `lfd/exec` (no later commit); its worktree was not inspected.
- **Result:** HOLDS

### V21: C14 — private names and machine paths
- **Observed:** the repository's local guard (private-name list, machine-path and e-mail patterns), run in manual mode on each of the 41 task commits across `master` and `lfd/exec` and on this review's map commit: no output. Positive control in a scratch repository: the guard flagged a planted Windows user-folder path and a planted Git Bash drive path. Dispatch ade4's pre-review scan agrees.
- **Result:** HOLDS

### V22: C17 — build gate
- **Observed:** Candidate tree extracted with a temporary index into `<scratch>`: `python -m pytest tools/tests/ docs/scripts/ -q --collect-only` → 14 collected; `-q` → 14 passed in 5.10 s (cache plugin disabled to keep the tree clean).
- **Limit:** these tests do not exercise instruction text; labelled a positive control (G8).
- **Result:** HOLDS

### V23: C18 — Executor economics
- **Observed:** `economics/roles/8927ba18….jsonl` SHA-256 equals its name; the helper's `validate` passes; manifest: role `executor`, unit `…/lfd-executor`, label `subagents/agent-a8ccaf657d4cc2e7e.jsonl`, range [0, 961), `complete: false`, cutoff `2026-09-29T06:11:55.748889+00:00`, revision 1; usage total 79,846,677 tokens on `claude-opus-5-5`. The Researcher's failure receipt `da131860….jsonl` also validates.
- **Limit:** reconciliation, including the shared `source_id` noted in RF §6 item 1, is the Coordinator's. During this review another session landed a change to `.tfw/economics/README.md` and the helper on `master` (`59c27b4a`, `8cd05ecb`, Daily task `20260929-104929`): a Claude Code subagent's source ID is now `<sessionId>/<agentId>`, and the collector refuses a session-only ID for a subagent file; the Executor's revision 1 carries the session-only ID, and `validate` still passes it (observation O9). No LFD VALUE path is touched by those commits.
- **Result:** HOLDS

## Commands Executed

| # | Command | Claim IDs | Result |
|---|---|---|---|
| 1 | extracted tag block (3 lines) + prose steps, Git Bash, GitHub `v3.7.1`, hostile config | C1, C4–C6 | exit 0; 679.57 KiB; 95/95; 0 CR; pre-seal 0; control 95 |
| 2 | same in Windows PowerShell 5.1 | C1, C4, C5 | exit 0; 679.57 KiB; 95/95; 0 CR |
| 3 | tag block without the two `-c` settings | C4 | 0/95; 95 files with CR |
| 4 | extracted untagged block (5 lines) by SHA, Git Bash and PowerShell | C2 | exit 0; 622.81 KiB; promisor keys written by Git; 95/95 |
| 5 | `git init --bare` + `fetch --depth 1 file://<this repo> refs/tags/v3.7.1` | C3 | local mirror 114.43 MiB |
| 6 | tag block against the plain mirror | C3 | warning only, exit 0; 114.43 MiB; 95/95 |
| 7 | fallback: clone `--no-checkout`; `count-objects -vH`; `checkout <SHA> -- .tfw` | C3 | 114.43 MiB; only `.git`, `.tfw`; 95/95 |
| 8 | tag block without `core.longpaths`, 105-character root | C16 | sparse set exit 254, `Filename too long`; 0/95 |
| 9 | untagged block to `0b755dca` from a local mirror | C1 | 667.48 KiB; 100/100 |
| 10 | nested repository + `git add -A` + `git ls-files -s -- .tfw/.upstream` | C6 | 1 gitlink entry |
| 11 | extracted quickstart block + copy with exclusions, Git Bash and PowerShell | C8 | 774.34 KiB; 88/88; editions 30/30; 6 Cyrillic names |
| 12 | `git archive --format=zip` / `tar.gz` of `0b755dca` and `49703481`; zip audit | C9 | 525,788 B, 130 files = allow-list, 130/130; Baseline 188,283,035 B |
| 13 | `git archive 0b755dca .tfw` and `49703481 .tfw` listings | C9 | 93 vs 100 files |
| 14 | `git ls-remote --tags --refs <upstream>` timed; counts | C10 | 1.32 s, 2,938 B; 45 exact; 11 newer than 3.1.0 |
| 15 | `ls-remote` to `192.0.2.1` under a 5,000 ms tool limit; to an `.invalid` host | C10 | control back at 5 s, process ended 21,062 ms; 0.28 s exit 128 |
| 16 | synthetic same-named branch/tag clone; `ls-remote` with `^{}`; `--branch refs/tags/…`; `ls-remote --heads <upstream>` | C5 | branch wins; peeled line available; full ref refused; 1 branch upstream |
| 17 | `wc -w`, `cmp`, `git rev-parse <blob>`, `git diff --name-status/--summary/-U0` | C11 | 1,492; equal; 9 / 15 paths; 0 hits |
| 18 | TS §4 PowerShell `--name-status` and `--numstat` `-z` with `$valuePaths`, both Baselines | C12 | 8 files; 122/29/151; 232 from `a0ccb1a3` |
| 19 | `git branch --contains`, `git log a5c90d2b..lfd/exec`, per-commit `git show --name-only` | C13, C15 | 1 Candidate commit; role-clean commits |
| 20 | local guard per task commit; positive control | C14 | 0 hits on 42 commits; control flagged |
| 21 | `pytest … --collect-only`; `pytest … -q` on the extracted tree | C17 | 14 collected; 14 passed |
| 22 | `tfw_economics.py validate`; SHA-256; manifest/usage read | C18 | valid; hash matches; 79,846,677 tokens |

## Claim and Source Checks

| # | Claim / citation | Where | Primary artifact / source | Holds? |
|---|---|---|---|---|
| C1 | update transfers 679.57 KiB instead of about 114 MiB | RF §1 | V1, V2; HL §2 R1 receipts (114 MiB) | ✅ |
| C2 | a filtered fetch by URL registers the promisor itself on Git 2.42/2.43 | RF §2 item 2 | V4, V5 config readback (2.42) | ✅ (2.43 by EV only) |
| C3 | a filter-less host exits 0 with one warning and 114.51 MiB | EV E6 | V6: same warning, 114.43 MiB (pack variance) | ✅ |
| C5 | pin guarantees unchanged in meaning | RF §3 AC-3 | V16 table | ✅ with O1 corner |
| C8 | install 774.34 KiB, 88 files, Cyrillic names intact | RF §1, EV E13–E14 | V11, V12 | ✅ |
| C9 | ZIP 525,788 bytes, 130 files, no `.gitattributes` | RF §1, EV E16 | V14 | ✅ |
| C10 | unreachable returns at 5 s; process ended after ≈21 s | EV E19 | V15: 21,062 ms | ✅ |
| C10 | "normal checks took 3.2–4.8 s today" | RF §6 item 2 | V11, V12, V15: 1.02–1.51 s later the same day | ⚠️ connection-dependent; the 5 s bound held with margin here |
| C11 | 1,492 words; byte copy | RF §3 AC-8 | V18 | ✅ |
| C11 | `git diff --name-only 49703481 0b755dca` → 9 paths | EV E23 | V18: 15 paths | ❌ for the literal command; ✅ for the claim it supports (O5) |
| C12 | 122 + 29 = 151; 232 from `a0ccb1a3` | RF §1, EV E-accounting | V19 | ✅ |
| C18 | 79,846,677 tokens; file validates | RF §5 | V23 | ✅ |
| HL §2 | the Git for Windows installer default rewrites every file | HL §9 | V3 (95 of 95 with CR) | ✅ |
| HL §8 | no host API; Git-only primary method | TS P6 | V1–V7 use only Git | ✅ |

## Guard and Check Admission

| # | Kind | Protected behavior / invariant | Failure consequence | Counterfactual detection | Admission |
|---|---|---|---|---|---|
| G1 | permanent guard | staged payload bytes equal the pinned tree | CRLF-rewritten, stale or missing framework files installed | V3: 0/95 without the settings; V8: 0/95 when long paths abort the checkout | admitted |
| G2 | permanent guard (disclosure) | a full download is never silent | 114 MiB moved while the text claims a light fetch (DoF 2) | V6: 114.43 MiB while the clone's config still claims partial | admitted; it depends on the agent reading one figure against 2 MiB |
| G3 | permanent guard | no staging file or gitlink reaches the receiver's index before sealing | upstream payload or a gitlink committed into a receiver (DoF 1) | V1: 95 entries after `git add -A`; V10: 1 gitlink entry | admitted |
| G4 | protective setting | checkout writes raw bytes regardless of user or system line-ending settings | byte identity lost on default Windows installs | V3 against V1/V2 | admitted as a setting with demonstrated effect, not a check |
| G5 | recheck | the named tag is not moved between pin and adapter sync | a moved tag's object applied | no moved-tag negative control; V16 shows it does not detect a branch-shadowed clone | admitted for tag movement only; the shadow corner is O1 |
| G6 | bound | new-task start is never held by an unreachable upstream | delayed or failed start (DoF 3) | V15: control back at 5 s against a 21 s connect | admitted, on tools that can bound time; others skip by rule |
| G7 | existing guard | a tag's `VERSION` equals its name | wrong release labelled | unchanged text; not re-tested | existing, not re-admitted |
| G8 | positive control | the repository's own tests still pass | unrelated regression | none needed | labelled control; not product assurance for instruction text |
| G9 | governance assertion | no private name or machine path is committed | permanent public leak (DoF 6) | positive control flagged machine paths | admitted as a pattern scan |

## Candidate Findings

No material findings. The following observations keep the full item contract; none changes
acceptance or the next authorized act.

| ID | Class | Subject | Affected claim / authority | Observed fact + oracle | Concrete harm | Material consequence or named absence | Owner | Observable completion | Route / rung | Candidate effect | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| O1 | VALUE (latent) | Step 0 tag route, `clone --branch <tag>` | C5; DoD 3 "operator-named tag resolves to one object"; KNOWLEDGE D70 | V16: Git prefers a same-named branch; the recorded `refs/tags/<tag>` line is the tag object only; no step compares the clone's commit with the peeled tag commit | an upstream or fork carrying a branch named like the tag would have that branch tip installed and recorded as the release | none now: the canonical upstream has one branch (`master`), none version-named; `v{VERSION}` still catches a differing version; the same exposure existed when agents improvised `clone --branch` | Task Coordinator | Step 0 compares `rev-parse HEAD` of the clone with `git ls-remote <upstream> 'refs/tags/<tag>^{}'` (or the tag line itself for a lightweight tag), or the owner accepts the corner | recorded here; Coordinator rules at close; the text needs ≈15 words against 8 of headroom, so the owner-approved separate `update.md` task (gate answer 235b) is the natural carrier once created | unchanged | observation |
| O2 | VALUE (legacy path) | README one-time hint and Step 0 for receivers below 2.0.0 | HL §3 claim 1, principle 2 "no improvisation" | the immutable `migrations/2.0.0.md` note requires `tools/migrations/2.0.0/` "from that same immutable upstream release ref"; the written fetch stages only `.tfw` and deletes the clone before Step 1 reads that guide; RES iteration 1 D11 flagged this for a one-time note; the hint addresses "3.7.1 or earlier" without a pre-2.0 remark | a pre-2.0 receiver's agent must improvise one more small fetch | none: loud (the guide names the bundle and stops without it), limited to dormant 0.x/1.x receivers (13 on the owner's machine, HL §2), and the archive allow-list keeps the bundle from the first release carrying `.gitattributes` | Task Coordinator | a pointer for pre-2.0 targets to add `tools/migrations/2.0.0` to the sparse set, or explicit acceptance | recorded here; Coordinator rules at close | unchanged | observation |
| O3 | ASSURANCE (limit) | version line reach | C10; DoD 6 | V15: the card's rendering by a fresh Coordinator under `plan.md` was not observed; `plan.md` Read Contract row 2 does not list `.tfw/VERSION`, `tfw.upstream`, `tfw.installed_from`, which the rule names itself | a literal reader could omit the row, leaving lag silent | none established: `plan.md` Step 1 renders the card from the rule, and the rule names its inputs | Task Coordinator | the row is seen at the first real new-task start after landing, or a later task adds the inputs to `plan.md` | recorded here; Coordinator rules at close | unchanged | observation |
| O4 | TRACE (contract wording) | frozen HL §3 claim 2 | owner-approved contract | claim 2 says install obtains "only what a new receiver installs"; the owner-approved TS AC-4 uses "the same clone settings", whose cone mode also carries the directory structure, top-level files and upstream state (≈0.32 MiB at `v3.7.1`, per A1); A1 aligned claims 1 and 5, DoD 1, principle 1, §1 and §3.2, not claim 2 | a literal inconsistency inside the frozen contract | none: the owner chose cone mode knowing its remainder (A1) and approved AC-4; DoD 4's measurable part holds | Task Coordinator → owner | the owner acknowledges it at final acceptance, or a §12 row extends A1's wording to claim 2 | HL §12 through the Coordinator only if the owner wants the wording aligned | unchanged | observation |
| O5 | TRACE (evidence text) | EV E23 | C11 evidence | the cited `git diff --name-only 49703481 0b755dca` returns 15 paths, not 9; the extra six are this task's records from Coordinator commits | a re-reader sees a different count | none: the supported claim (no VALUE path outside TS §4; the Candidate commit changes 9 paths) holds | Executor's carrier via the Coordinator | an appended EV note, or accept as is | non-material TRACE; optional current-carrier repair | unchanged | observation |
| O6 | TRACE (authority record) | accounting Baseline | TS §4 approval epoch | the approved Baseline `a0ccb1a3` was moved in place to `49703481` by the Coordinator before launch (TS header, dispatch 489d, ONB §6, RF, EV); gate answer 235b restates it, though the owner's answer there concerned A4 | the approved value and the governing value differ | none: 151 ≤ 160 under the governing Baseline and 232 < 320 under the original, so no owner threshold is crossed either way; the move removes another task's landed lines and matches "this TS at its approval commit" | Task Coordinator | presented to the owner with the result at final acceptance | Coordinator's own record; no review route | unchanged | observation |
| O7 | VALUE (minor) | README prompts | C8 | the prompts carry no size check or fallback; for Full they hand over to `quickstart.md`, whose Step 1 may fetch again | an Assisted install lacks the disclosure (GitHub serves filters); a Full install may fetch twice (< 1 MiB) | none | Task Coordinator | accept, or tighten in a later task | recorded here | unchanged | observation |
| O8 | TRACE (close-time) | EV E9 Codex sandbox, E17 GitHub archive | DoD 2, DoD 5 | both DEFERRED as the TS allows; DoD 2 and DoD 5 accept "reported unavailable with the reason" / "stated as unobserved" | none | none for the verdict | Task Coordinator | at close each is recorded observed or unobserved with its reason | close-time disposition | unchanged | observation |
| O9 | TRACE (economics, outside the Candidate) | Executor economics revision 1 | C18; `.tfw/economics/README.md` as changed on `master` during this review (`59c27b4a`, `8cd05ecb`) | the current text names a Claude Code subagent source `<sessionId>/<agentId>` and says a file captured under a source ID later shown wrong "is not a revision and cannot be superseded: keep it outside economics/roles/ with the reason in the task record, then collect and return the corrected file"; the Executor's file carries the session-only ID | the task's economics report could exclude or mis-key the Executor's contribution | none for the product verdict | Task Coordinator, with the Executor for a corrected capture | reconciliation at close under the current contract | close-time economics reconciliation | unchanged | observation |

## Evidence Verification

| # | RF evidence ref | Subject tuple | Artifact exists? | Establishes the claim? | Limit |
|---|---|---|---|---|---|
| E1 | `update.md` lines 41–64 | Candidate text | ✅ | ✅ | copy and deletion are prose operations (V1 limit) |
| E2–E3 | trials T1b, T2b | Candidate text, both shells, GitHub | ✅ | ✅ reproduced (V1, V2) | — |
| E4 | trials T3b | WSL, Git 2.43 | ✅ | ✅ as Executor evidence | not re-run |
| E5 | trials T5, T6 | untagged, both shells | ✅ | ✅ reproduced (V4, V5) | — |
| E6 | trials T4 | plain local server | ✅ | ✅ reproduced (V6) | emulated host |
| E7 | trials T12 | fallback forms | ✅ | ✅ reproduced (V7) | trigger unproducible |
| E8 | trials T7 | hostile line endings | ✅ | ✅ reproduced (V1–V3) | — |
| E9 | ONB §4 item 1; trials "Codex probe" | Codex sandbox | ✅ | ⚠️ DEFERRED, TS-permitted | owner action pending (O8) |
| E10 | trials T7-lp | long paths | ✅ | ✅ loud; detail differs (V8) | — |
| E11 | RF §3 AC-3 table | text; trials | ✅ | ✅ (V16) | O1 corner |
| E12 | trials "Trial update" | whole workflow, local mirror | ✅ | ✅ as Executor evidence | synthetic receiver; not re-run beyond Step 0 (V9) |
| E13–E14 | trials T8, T9 | install, both shells | ✅ | ✅ reproduced (V11, V12) | — |
| E15 | README line ranges | text | ✅ lines match | ✅ (V13) | prompts text-checked |
| E16 | trials "Release archive" | local archive | ✅ | ✅ reproduced (V14) | — |
| E17 | — | GitHub archive | n/a | ⚠️ DEFERRED, TS-permitted | owner's push (O8) |
| E18 | `conventions.md` lines 1094–1101 | rule text | ✅ | ✅ (V15) | — |
| E19 | trials "Version line" | Claude Code tool | ✅ | ✅ reproduced (V15) | other tools unobserved |
| E20 | diff line refs | text | ✅ | ✅ (V17) | — |
| E21 | trials negative control | scratch receiver | ✅ | ✅ reproduced (V1, V10) | — |
| E22 | trials per-step times | trial update | ✅ | ✅ as Executor evidence | one machine, one run |
| E23 | `wc`, `cmp`, name-only | Git | ✅ | ✅ except the path count (O5) | — |
| E24 | pytest | Candidate tree | ✅ inline | ✅ reproduced (V22) | positive control |
| E-accounting | TS §4 commands | PowerShell 5.1 | ✅ inline | ✅ reproduced (V19) | O6 disclosure |

EV's verdict line (23 VERIFIED, 2 DEFERRED) matches its rows; RF §5 names the same EV and trials files.

## Knowledge Citations Verified

PV scan: P0 NS1–NS3 and P1 `Methodology values` / `Success Criteria` in `.tfw/README.md`; P2
`knowledge/philosophy.md`; P3 `KNOWLEDGE.md` §1; P4 `conventions.md` `HL (High Level)`, `Design
Rules`, `Anti-patterns (prohibited)` — read in full for this subject. P5–P7 by relevance:
`knowledge/environment.md` F3 (Git Bash rewrites a leading `/`) matches the no-leading-slash rule;
`knowledge/convention.md` F2 (mixed line endings in `.tfw/`) is no longer current — no `.tfw` blob at
the Candidate contains CR — and does not affect raw-byte identity. `KNOWLEDGE.md`'s retired-row entry
for "`cp -r` of the payload over `.tfw/`" does not apply: the new copy is clone → staging, and the
receiver copy in Step 3 keeps its declared exclusions. D82 records that the pinned pre-2.0 migration
lives in upstream `tools/` (bears on O2).

| # | Artifact | Priority + exact citation | Resolves? | Item exists? | Meaning matches? | Relevant? |
|---|---|---|---|---|---|---|
| 1 | HL §7.2 #1 | P0 NS1 "not the production of more text or more process" | ✅ `#ns1` | ✅ | ✅ | ✅ one row, one written method |
| 2 | HL §7.2 #2 | P0 NS2 principle 2 (Saint-Exupéry) | ✅ `#ns2` | ✅ | ✅ | ✅ exact text replaces vague; kept checks |
| 3 | HL §7.2 #3 | P0 NS2 principle 7 | ✅ | ✅ | ✅ | ✅ grounds A3 removals |
| 4 | HL §7.2 #4 | P0 NS3 "vendor-bound tool, runtime, model, interface, or memory feature" | ✅ `#ns3` | ✅ | ✅ | ✅ Git-only primary; archive link not primary |
| 5 | HL §7.2 #5 | P1 Methodology values — Structural Enforcement | ✅ `#methodology-values` | ✅ | ✅ | ✅ version row, size and pre-seal checks are observable |
| 6 | HL §7.2 #6 | P1 Methodology values — Portability | ✅ | ✅ | ✅ | ✅ plain Git and files |
| 7 | HL §7.2 #7 | P1 Success Criteria 4 | ✅ `#success-criteria` | ✅ | ✅ | ✅ receivers stop reconstructing the fetch |
| 8 | HL §7.2 #8 | P2 `knowledge/philosophy.md` F23 | ✅ | ✅ line 30 | ✅ state contamination is a class | ✅ upstream state staged but excluded at copy; archives drop it |
| 9 | HL §7.2 #9 | P3 `KNOWLEDGE.md` D70 | ✅ | ✅ | ✅ pin from the operator's tag, never `HEAD` | ✅ with O1 corner |
| 10 | HL §7.2 #10 | P3 `KNOWLEDGE.md` D82 | ✅ | ✅ | ✅ no shipped executable | ✅ method in workflow text |
| 11 | HL §7.2 #11 | P3 `KNOWLEDGE.md` D2 | ✅ | ✅ | ✅ root README landing, `.tfw/README.md` paper | ✅ install change in README Quick Start and quickstart |
| 12 | HL §7.2 #12 | P4 `conventions.md` Design Rules | ✅ | ✅ | ✅ ≤1,400 words; adapter-safe commands exercised from the root | ✅ A4 exception to 1,500 recorded; commands exercised |
| 13 | HL §7.2 #13 | P4 Anti-patterns — Authority and role | ✅ | ✅ | ✅ (stated as the prohibited act) | ✅ V20 role-clean commits |
| 14 | HL §7.2 #14 | P4 `HL Contract` rule 15 | ✅ | ✅ | ✅ leading `/` rewritten by some shells | ✅ no sparse pattern begins with `/` |
| 15 | ONB §7 #15 | P4 §9 Tool Adapter Pattern | ✅ | ✅ | ✅ exact markers, one managed block | ✅ supports dropping the second-run diff |
| 16 | ONB §7 #16 | P4 `Exact-path staging`, `Worktrees for concurrent mutation` | ✅ | ✅ | ✅ | ✅ V20 |
| 17 | ONB §7 #17 | `.tfw/economics/README.md` Claude Code recipe | ✅ | ✅ | ✅ | ✅ V23 |

## Accounting Replay

| Approval / authority | Baseline | Candidate | Literal VALUE membership / actions / classes / reasons | Adds | Deletes | Touched LOC | Binary | Trigger disposition | Exact NUL-safe command | Verdict |
|---|---|---|---|---:|---:|---:|---|---|---|---|
| owner TS approval, gate answer 02ae (8 / 160), freeze `49703481`; TS amended in place at `4d1f5efd` (Baseline) and `975fed5f` (A4), both before or during execution without changing files or denominator | `49703481e1b02ac725428dfd8da19c4d7c954c86` | `0b755dcada76fe0f22bf285a77b40f812c365c45` | `.gitattributes` A 14/0; `.tfw/conventions.md` M 9/0; `.tfw/quickstart.md` M 13/3; `.tfw/templates/update_receipt.md` M 4/4; `.tfw/workflows/update.md` M 31/10; `README.kk.md` M 17/4; `README.md` M 17/4; `README.ru.md` M 17/4 — all VALUE with TS §4 reasons; no renames; single phase | 122 | 29 | 151 | N/A — no binary | 8 / 151 within 8 / 160; owner ceiling 16 / 320 and prompts 50 / 5,000 not reached | `git diff --name-status --find-renames=50% -z 49703481… 0b755dca… -- $valuePaths`; `git diff --numstat --find-renames=50% -z …` (TS §4, PowerShell) | VERIFIED |
| disclosure only: the originally approved Baseline | `a0ccb1a34c0c6321dfa664ddfdd97335e1777019` | same | same 8 paths; TEQM's landed lines included | 186 | 46 | 232 | N/A | above 160, below the 320 owner ceiling | same commands | N/A — not governing (O6) |

The Candidate is the first tested implementation commit, before EV, RF and the `RF` state. Protected
boundaries hold: past migration guides, `plan.md`, `init.md`, coordinator profiles and the Codex
`tfw-update` skill are unchanged.

## Selected Knowledge Evidence

Lineage checked against dispatches c29b, ded6 and d297 (Researcher), 489d (Executor) and ade4 (this
Reviewer). Returns: RES iteration 1 `5776480e` and iteration 2 `9792b639`, both with no Fact
Candidates; the Researcher's economics failure receipt received at `8b66f017`; ONB `1590b5ce`; RF,
EV, trials and Executor economics `b9a7ae57`; transition `98b1a35e`. RF §7 has no Fact Candidates and
RF §8 no Strategic Insights; human-sourced insight remains in HL §11 S1–S6 (owner statements). No
knowledge publication is owed from this review; the qualification decision stays with the
Coordinator's close.

## Checkpoint

**Self-check:**
- [x] Replayed the Map selection and verified all mandatory safety/security, authority and identity floors?
- [x] Established evidence applicability and ran every TS-required or dependency-affected check?
- [x] Recorded explicit limits instead of substituting file, discrepancy, test, commit or artifact counts?
- [x] Classified guards and controls by protected behavior, consequence and counterfactual detection?
- [x] Recorded every candidate finding with the complete item contract and material consequence test?
- [x] Verified RF AC claims, evidence references, citations and immutable accounting against actual artifacts?

Stage complete: YES
