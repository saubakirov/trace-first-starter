# RES — TFW_20260929-003444_LFD: Lightweight Framework Delivery

> **Date:** 2026-09-29
> **Author:** Claude Code Researcher (in-session agent `lfd-researcher`)
> **Status:** 🔬 RES — Complete, iteration 1 of 2 minimum / 3 maximum
> **Parent HL:** [HL-TFW_20260929-003444_LFD.md](../../HL-TFW_20260929-003444_LFD.md)
> **Mode:** Pipeline / deep (Coordinator ruling)
> **Producer unit:** `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher`, as recorded by the dispatch; this in-session agent cannot read its own name back
> **Parent Coordinator:** `claude-code:session:local_e821cd09-6696-482b-bd88-ca93dba929a2`
> **Activation / dispatch source:** delegated; [dispatch](../../journal/20260929-005309__dispatch__c29b.md) @ `8ebea35e23e559eff58d195b7d338b35429e9c70`; synthesis continuation [gate answer 32ef](../../journal/20260929-023243__gate_answer__32ef.md) @ `e3ae21fb3e796c2ca324f2a277fa38c788108feb`
> **Coordination authority:** `HL-TFW_20260929-003444_LFD.md @ c4044d2efc78e2e422849b27bccc4e0d9da2688e`; `baseline` · `native-gates` · `tfw-gates-only`
> **Originating proposer:** `{principal: none, unit: claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher}` for A1 and A2; no other proposal

---

## Research Context

Iteration 1 tested H1, H3 and H4 on the owner's Windows machine: Git 2.42.0 in Git Bash and in Windows
PowerShell 5.1, and Git 2.43.0 in WSL Ubuntu. The target was tag `v3.7.1` (commit
`1e3e00e9b7bf0c706cdc12094eadeb4103fc6bbb`), fetched from GitHub and from this repository served
read-only over `file://`, always into scratch directories. The questions were:
- which exact, Git-only way of fetching and installing only the framework keeps every file byte-equal
  and the pin guarantees intact in each shell;
- how that method shows its own failure;
- how a version line stays short and never blocks;
- what install and release archives need.

After the Extract deviation E10, every trial that could fetch beyond its named paths ran only against
the local server. H2 (where update time goes) belongs to iteration 2.

## Briefing

[1_briefing.md](1_briefing.md) holds the plan, hypotheses, scope and hygiene. Coordinator gates:
- [f52c](../../journal/20260929-010420__gate_answer__f52c.md) approved the Briefing, the Codex sandbox
  and WSL trials within limits, and one heavy GitHub run.
- [89ea](../../journal/20260929-015144__gate_answer__89ea.md) moved Gather to Extract.
- [2493](../../journal/20260929-020513__gate_answer__2493.md) accepted E10 as a disclosed breach and
  bound later trials to the local server.
- [32ef](../../journal/20260929-023243__gate_answer__32ef.md) set the form of A1, the flagged decision
  and the X7 correction below.

## Decisions

| # | Decision | Rationale |
|---|---|---|
| D1 | Byte identity is proven by raw bytes only: `git hash-object --no-filters` of each file against its blob id from `git ls-tree` of the pinned commit. A filtered hash or `git status` proves nothing. | A filtered hash reported 0 differences on 95 files rewritten to CRLF ([G1](2_gather.md)). |
| D2 | The fetch is a blobless, depth-1, sparse clone of the one pinned object, and Git writes the files. No `git archive` step, no tool beyond Git. | 670,042 B and 4.8–8.2 s from GitHub in 2 lazy batches. 95/95 byte-equal in Git Bash and PowerShell 5.1 (G2), and in WSL with the install set (G7). The archive route with `--worktree-attributes` is light but makes one round trip per file: 156 s in Git Bash and 92 s in WSL, against 41 s for the whole 114 MiB (G2). Without the flag, one archive in any partial clone, sparse or not, pulls the whole tree (G1, [E10](3_extract.md)). PowerShell 5.1 byte pipes and `tar` traps affect only archives (G4). |
| D3 | The clone carries `-c core.autocrlf=false -c core.attributesFile=`; `core.eol=lf` is an optional guard. | The Git for Windows installer default rewrote every file to CRLF (G3; 88/88 again in [X7](4_challenge.md)). A user attributes file with `eol=crlf` beat both `autocrlf=false` and `core.eol=lf`. An empty `core.attributesFile` neutralised it in 3 of 3 runs (X6). `core.eol=lf` matters only if the upstream tree ever gains a `text` rule without `eol` (inferred from X6's `text=auto` case). |
| D4 | Staging keeps today's path. Clone into `.tfw/.upstream/.clone`, copy its `.tfw` to `.tfw/.upstream/.tfw`, check the copy against the clone's tree, then delete the clone. | Staging is shared by two texts: the installed one stages, the pinned target reads. `update.md` Read Contract row 4 and Step 4 name paths under `.tfw/.upstream/`, and so do the immutable `2.0.0` and `3.1.0` guides (X1). The first update to a new version still stages by the old text, so an outside clone (C1) would force every later target to handle both locations (inferred from the Read Contract). C1 is eliminated. A clone left at `.tfw/.upstream/` became a gitlink under `git add -A` (E4). S1 staging held 95/95 in both Windows shells, with no OS temp path and no gitlink (X1). |
| D5 | A size check follows the clone: `git -C <clone> count-objects -vH`. A full download is disclosed. | On a host without filter support the clone exits 0 and prints one warning, while its config and pack markers still say "partial". Only the stored size (114.43 MiB against 262.50 KiB) and the missing-object count tell the truth (X2). The same figure is DoD 1's measured transfer. It includes pack indexes (622 KiB = 613,019 B pack + 24,740 B index, observed), so it slightly overstates. |
| D6 | One disclosed fallback: if Git rejects an option, repeat the clone without the filter and sparse options and report the measured size. A host without filters needs no extra step. | Old Git fails loudly (exit 129, E2). The filter-less case already gave 95/95 byte-equal (X2). Keeping R1's archive route as a second, light fallback would add a second method with extraction traps (principles 2 and 5). |
| D7 | An authorized untagged commit uses S3: `init`, clone config, remote, promisor and filter config, sparse set, `fetch --depth 1 --filter=blob:none origin <SHA>`, `checkout FETCH_HEAD`. The same sequence accepts a tag, which could make it the only sequence (Open Thread 3). | `clone --branch` takes no SHA, and `clone --revision` needs Git 2.49 (E5). S3 gave 95/95 for a tag and for a SHA locally; `FETCH_HEAD` is the tag object for a tag (X3). A commit that is not a ref tip works over protocol v2 and fails loudly on v0 (X3). C12 and C13 leave the fetch or the tag choice to improvisation (principle 2). |
| D8 | Version line. The upstream (`installed_from: "self"`) makes no call and shows no offer. A receiver runs one `git ls-remote --tags --refs <tfw.upstream>` under a stated limit of about 5 s set on the agent's command tool. It keeps only exact `vX.Y.Z` tags, compares them numerically with `.tfw/VERSION`, and counts newer releases from the same list. Any failure shows "unknown" with its reason. | Normal cost 0.9–2.0 s and 2,938 B (G6). Dropped packets cost 21 s on Windows and 131 s on Linux. Released Git has no connect limit, `http.lowSpeed*` does not bound the connection, and in PowerShell a `timeout` prefix runs Windows `timeout.exe` (G6, E7). Five pre-release tags sort above their release under `-v:refname` (G6). With 0 GitHub Releases, a host API always says none (E7). About 5 s meets DoD 6's "within a few seconds", with 2.5× headroom over the slowest normal run (1.97 s). |
| D9 | Release archive: R3, the allow-list plus the three lines that keep `tools/migrations/2.0.0/`. | ZIP 590,839 B, 132 files, and `.tfw/` whole in every archive (E8). R2 drops the bundle that the `2.0.0`, `3.0.0`, `3.1.0` and `3.2.0` guides say to take from the release (G7, G8). R3 holds from the first release that carries it; tags up to `v3.7.1` stay 178.9 MiB (E6). |
| D10 | Install uses the same clone with `.tfw` and `editions`, then copies the chosen edition without the project state that `quickstart.md` already lists. | Install reads nothing else from the source (G7). 766,242 B, 95/95 and 30/30 byte-equal in three environments, Cyrillic names intact in PowerShell (G7, G4). DoD 4's target is 88 `.tfw/` files at `v3.7.1` (E8). |
| D11 | The migration bundle matters only for archives and for any one-time "fetch light" note for receivers below 2.0.0, not for the new Step 0. | Step 0 always runs from the installed `update.md` ("Until a target is pinned, this installed workflow is the only update contract"), and a receiver running the new text is already past 2.0.0. Inferred from the text, not tested. |
| D12 | The Codex sandbox is reported unobserved. | `codex sandbox` requires a `[permissions]` profile. Supplying one would change Codex configuration, which the gate excluded, and would test a policy of my choosing (G5). |

### Corrections stated at synthesis

1. **X7, a correction of Gather and Extract (requested by the Coordinator).**
   - **What happened.** During Gather's control trials one run set exact non-cone patterns from Git Bash
     with `sparse-checkout set --no-cone /.tfw/`. Its trace (2026-09-29 01:17:51 +05:00) shows that Git
     received `C:/Program Files/Git/.tfw/`: Git Bash converts an argument that begins with `/` into a
     Windows path. Such a pattern matches nothing in the repository, and Challenge reproduced the empty
     result (X7).
   - **How it shaped both stages.** The run was never written into Gather or Extract as a finding, but
     its conclusion shaped both. Every sparse configuration they mapped was either cone mode, which always
     adds the top-level files, or the unanchored `--no-cone .tfw`, which also pulled six files under
     `workspace/…/.tfw/` (E2). An exact `.tfw/` without upstream state appeared only as an archive variant
     (R5).
   - **What is right.** Patterns that do not begin with `/` work: `.tfw/**` is anchored because it
     contains a slash. The exact set (S2) checked out 88/88 framework files byte-equal in Git Bash and
     PowerShell 5.1 (X7). `conventions.md` HL Contract rule 15 already warns that some shells rewrite a
     pattern that begins with `/`.
   - **What X7 got wrong.** X7 puts "did not populate" in quotation marks, as if Gather and Extract said
     it. Neither committed file does; they carried the consequence, not the claim.
2. **X1 left one observation out.** In the scratch receiver, `git add -A` created no gitlink, as X1 says,
   but it did stage the 95 copied files under `.tfw/.upstream/.tfw/`. Today's `git archive` staging has
   the same exposure, because receivers do not ignore `.tfw/.upstream/` (E4).
3. **X4 overstated that R5 brings no benefit.** DoD 5 asks that an archive contain "only framework
   material". Whether the upstream's own state inside `.tfw/` counts as framework material is the flagged
   owner decision below, and R5's lines are one answer to it.
4. **X8's top-level share** is 82,247 B measured directly (`clone --sparse` 246,632 B minus
   `--no-checkout` 164,385 B), not ≈88,000.
5. **X9's example limit** of about 10 s is too loose for DoD 6; D8 uses about 5 s.

## Open Questions

| # | Question | Status | Answer |
|---|---|---|---|
| Q1 | Cone mode (S1) or exact patterns (S2)? | Owner, A1 | Both presented without a pick (gate answer 32ef). |
| Q2 | Does §1's "however large that repository grows" still hold? | Owner, A2 | For file content, yes; the directory structure still travels and grows. |
| Q3 | Should the upstream's own state keep shipping inside `.tfw/`? | Owner, flagged outside this task | Facts below; no recommendation. |
| Q4 | Does "any release" in §3 claim 3 include past tags? | Interpretation for the TS | Read here as releases from the first one carrying R3; past tags are immutable (E6). No amendment proposed. |
| Q5 | Does a real host without filter support (Bitbucket Cloud) behave like the local plain server? | Unobserved | Local emulation only (X2); a community answer says Bitbucket Cloud serves no filters (E6). |
| Q6 | Codex sandbox; command time limits in tools other than Claude Code | Unobserved | G5; Claude Code's shell tool takes a time limit (E7). |
| Q7 | Git 2.25–2.41, macOS, a machine without Windows long-path support | Unobserved | Only Git 2.42 and 2.43 ran; long paths could not be reproduced here (X5). |
| Q8 | S2, and S3 with a tag, against GitHub | Unobserved (local-only binding) | S2: 489,768 B locally. S3 with a SHA took 15.2 s once on GitHub, against 4.8–8.2 s for S1's clone (E5, G2). |
| Q9 | GitHub's own archive with R3 | Unobserved until the owner's push | Local archives only (G8). |
| Q10 | Where does update time go (H2)? | Iteration 2 | Input: 41 s for the old download, against 5–8 s light (G10). |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|---|---|---|---|
| H1 | One Git method is light and byte-identical in Git Bash, PowerShell and the Codex sandbox | open | ✅ supported with conditions for the sparse clone; ❌ for the archive variant as primary; Codex sandbox unobserved | S1: 0.64 MiB, 95/95 in Git Bash, PowerShell 5.1 and WSL (G2, G7). S2: 0.47 MiB, 88/88 locally (X7). Conditions: D3's clone settings and D5's size check. The false case is partly true: line endings convert by default (G3, X6). Clone settings fix that, not the archive link, which is no light fallback for tags up to `v3.7.1` and cannot be checked per file (E3, E6). |
| H2 | Download is a minority of update time | open | ⏸ deferred to iteration 2 | G10 input only. |
| H3 | The latest-release check costs about a second and fails fast | open — partly observed | ⚠️ cost confirmed; false case observed | 0.9–2.0 s and 2,938 B; unknown host ≤0.27 s; blackholed 21 s / 131 s. Git has no connect limit, so the rule states a limit on the agent's tool (G6, E7, D8). |
| H4 | Install needs only `.tfw/` and `editions/` | open | ✅ confirmed; update exception | Install reads nothing else (G7). Receivers below 2.0.0 need `tools/migrations/2.0.0/`, which R3 keeps (G7, G8, D11). |

## HL Update Recommendations

The Researcher classifies; the Coordinator applies the refinements and routes the proposals. Nothing
here edits the HL.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|---|---|
| R1 | §2 | `.tfw/` row: the 95 files are 88 framework files and 7 upstream state files (289,678 B raw, 26%). "≈0.6 MiB as transferred" becomes 0.64 MiB by a cone-mode sparse clone from GitHub. About half of that is not framework files: trees 164,385 B, top-level files 82,247 B, upstream state ≈89 KB. | G2, E8, X8, correction 4 |
| R2 | §2 | "Fetch is unspecified": R1's fix is light (0.57 MiB) but makes one round trip per file, 156 s in Git Bash and 92 s in WSL, longer than the 114 MiB download (41 s). Latest-tag row: unknown host ≤0.27 s, refused 2.3 s, blackholed 21 s (Windows) / 131 s (Linux); Git has no connect limit; `-v:refname` sorts 5 pre-release tags above their release. New row: trees per tag, 53,377 B / 294 (`v2.0.0`) → 164,385 B / 738 (`v3.7.1`). | G2, G6, X8 |
| R3 | §2 | Unknowns: keep only what stays unknown — the Codex sandbox, macOS, Git below 2.42, real hosts without filter support, the update time split, how external users install. | Open Questions |
| R4 | §7.2 | Row 8 (F23) says the light fetch "still excludes" upstream state. After A1, say where: at the copy step (S1, as today) or at the fetch (S2). New row: P4 `conventions.md` HL Contract rule 15 — some shells rewrite a pattern that begins with `/`, so no sparse pattern in the method begins with `/`. | X7, A1 |
| R5 | §8 | Git row: 2.25 for `clone --sparse` and `sparse-checkout`, 2.35 for `--no-cone` (S2 only; secondary sources); only 2.42 and 2.43 observed; below the floor Git fails loudly. Codex row: unobserved (G5). New row: the host serves filters — GitHub yes (observed, capability `filter`), GitLab and Gitea ≥ 1.16 per their docs, Bitbucket Cloud no (community answer). New row: the agent's command tool can bound time — Claude Code yes, Codex unobserved. | E2, E6, E7, X2, G5 |
| R6 | §9 | Line-ending row: probability High, because the installer default rewrites every file; mitigation D1 and D3. Blackhole row: observed 21 s / 131 s; mitigation D8. Partial-support row: mitigation D5 and D6. `.gitattributes` row: no maintainer procedure archives, and R3 keeps the bundle. New rows: (a) receivers do not ignore `.tfw/.upstream/`, so `git add -A` during an update stages the payload copy (95 files), or a gitlink while a clone exists. Mitigation: delete the clone right after the check; iteration 2 weighs a local exclude. (b) Trees travel with every fetch and grow with the repository (A2). (c) Git Bash rewrites a sparse pattern that begins with `/`, so it matches nothing; D1's check catches it. (d) If S2 is chosen, the method rests on a mode Git's documentation calls deprecated. (e) The per-file check: inside a receiver, `git hash-object --stdin-paths` resolved paths from the receiver's top level, and Git Bash does not convert paths sent on stdin. Both failed loudly in the research harness, so the written check passes paths as arguments. | E4, X7, X8, correction 2 |
| R7 | §10 | H1–H4 statuses as in the table above. "Why not just" row 1: 0.47–0.64 MiB per update, 0.73 MiB install. Row 2 (archive link only): no per-file check without trees, 178.9 MiB for tags up to `v3.7.1`, PowerShell 5.1 extraction traps. Proposed focus item 3: staging stays (D4). | Hypotheses |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|---|---|---|---|---|
| A1 | §3 claim 5 · §7 principle 1 | `SUPERSEDE` | Replace "neither transfers nor examines non-framework content" (claim 5) and "never downloads, stages or examines material it will not install" (principle 1) with an exact statement of what travels, in the form the owner chooses. **S1, cone mode:** besides the framework files, the fetch carries the repository's directory structure, its top-level files and the upstream's own state inside `.tfw/` (≈0.32 MiB at `v3.7.1`); it installs none of them and carries no other file content. **S2, exact patterns:** the fetch carries only the framework files it installs, plus the directory structure Git always sends (0.16 MiB at `v3.7.1`). | S1: 670,042 B from GitHub, 95/95 in Git Bash, PowerShell 5.1 and WSL (G2, G7). S2: 489,768 B from the local server, 88/88 in Git Bash and PowerShell 5.1 (X7). No configuration avoids the trees on GitHub; `--filter=tree:0` gave the same 664,278 B (X8). Git's documentation: "non-cone mode is deprecated". Both forms meet DoD 1's measurable part (under 2 MiB, every framework-owned file hash-equal) and DoD 3. | S1: principle 1 stops being absolute; upstream state is staged as today and kept out of the receiver only by the copy exclusions. S2: rests on a deprecated Git mode. `--no-cone` needs Git ≥ 2.35, above the 2.34 that Ubuntu 22.04 ships (general knowledge, not verified), so such receivers take D6's full fallback. It puts four patterns into `update.md`'s 173-word headroom. The installed patterns fix what staging holds for every later target. Not observed on GitHub. | Keep the frozen wording: no Git method meets it literally, because trees always travel. `tree:0`: same bytes. The archive link (C9): no trees, but no per-file check and 178.9 MiB for tags up to `v3.7.1`. R1's archive route: the same trees plus 93 round trips. A framework-only branch or repository: not measured; adds a step to every release, and HL §10 rejects that kind of per-release ceremony. |
| A2 | §1 | `SUPERSEDE` | Keep "instead of the whole development repository and its history" and qualify "however large that repository grows": the repository's file content and history stay out, while its directory structure travels and grows with the number of folders and files (164,385 B at `v3.7.1`). | Trees per tag: 53,377 B (`v2.0.0`, 2026-08-30) → 83,927 (`v3.0.0`) → 102,663 (`v3.3.0`) → 147,685 (`v3.5.0`) → 164,385 B (`v3.7.1`, 2026-09-28) (X8). Every Git light fetch carries them, in S1 and S2 alike. | §1 promises less. At September's average of ≈3.8 KB a day (a linear extrapolation, not a forward measurement), S1 passes 1 MiB in about 3 months and DoD 1's 2 MiB in about a year; S2 does so in about 5 and 14 months. | Keep §1 as written: the measurement contradicts it (principle 7). Leave the tree to the separate hygiene task: a non-goal here, and it would change the numbers, not the mechanism. |

A1 and A2 share their evidence, and A2 holds whichever form A1 selects. §3 claim 1 and DoD 1 draw the
same boundary with "only the framework(-owned) payload". Their measurable parts hold under both forms,
and the HL's own figures (§3.1: "≈0.6 MiB, 95 files") describe S1's shape. Whether they need the same
wording is the Coordinator's routing question.

**A1 side by side** — for the owner's ruling, not a recommendation:

| | S1 — cone mode | S2 — exact patterns |
|---|---|---|
| Commands for a tag | `git clone -c core.autocrlf=false -c core.attributesFile= --filter=blob:none --sparse --depth 1 --branch <tag> <upstream> .tfw/.upstream/.clone`, then `sparse-checkout set .tfw` | the same clone with `--no-checkout` instead of `--sparse`, then `sparse-checkout set --no-cone '.tfw/**' '!.tfw/update_receipts/**' '!.tfw/project_config.yaml' '!.tfw/knowledge_state.yaml'`, then `checkout` |
| Transferred at `v3.7.1` | 670,042 B from GitHub (observed) | 489,768 B from the local server; GitHub not observed |
| Travels besides the framework files | trees 164,385 B; 10 top-level files 82,247 B; upstream state ≈89 KB | trees 164,385 B |
| Staged in the receiver | all 95 `.tfw/` files, upstream state included (as today); top-level files briefly under `.clone/` | exactly the 88 framework files |
| Byte identity observed | 95/95 in Git Bash and PowerShell 5.1, and in WSL with the install set | 88/88 in Git Bash and PowerShell 5.1; WSL not run |
| Git floor | 2.25; the older non-cone behaviour still gives a correct `.tfw/` (E2) | 2.35 for `--no-cone`; not observed below 2.42 |
| Git's documentation | cone mode is the recommended mode | "non-cone mode is deprecated. Please switch to using cone mode." |
| Later targets | staging holds the target's whole `.tfw/` | staging holds only what the installed patterns name; no shipped step needs an excluded file today (X4) |
| Frozen text touched | claim 5 and principle 1: trees, top-level files, upstream state | claim 5 and principle 1: trees only, if tree objects count as material |

### Flagged owner decision — outside this task's recommendation

Per gate answer 32ef, this is recorded for the owner and not recommended.

- **Fact.** `.tfw/` at `v3.7.1` ships 7 files of the upstream's own state: `project_config.yaml`
  (4,177 B), `knowledge_state.yaml` (1,825 B) and 5 files under `update_receipts/` (283,676 B, mostly two
  before-images of 140,878 B and 134,291 B). That is 289,678 B raw, 26% of the folder's 1,102,877 B, and
  about 89 KB of a light fetch.
- **Today.** None of them reaches a receiver's `.tfw/`: `quickstart.md` and the update's copy step leave
  them out (F23, D70).
- **Where the answer touches this task.**
  1. **A1.** S1 transfers and stages them; S2 skips them.
  2. **DoD 5** asks that an archive contain "only framework material". R3 meets that only if these files
     count as part of the shipped framework, as the HL's 95-file figures assume. Otherwise the archive
     also needs R5's exclusion lines. R2 with those lines (R5) measured 473,080 B; R3 with them is not
     measured (≈0.47 MiB, inferred).
  3. **R5's known cost.** An old receiver whose installed text archives the target's `.tfw` would get it
     without these files. The Read Contract's "never read … project-state bodies" means no shipped step
     reads them (X4).
- **Question for the owner:** should the upstream's own state keep shipping inside `.tfw/`?

## Fact Candidates

**No fact candidates.** No owner message reached this iteration; the Coordinator's rulings are in the
journal. Anyone can reproduce every observation here by running the recorded commands, so none passes
the Human-Only Test.

## Strategic Insights (Research)

**No strategic insights.** The owner took no part in this iteration's briefings and supplied no domain
or strategy claim.

## Findings Map

```text
FETCH one pinned object for update; the same clone plus editions/ for install

git archive route (R1's fix)    host archive link (C9)          sparse clone; Git writes the files
0.57 MiB, 93 round trips:       no trees, no per-file check;    0.47-0.64 MiB in 1-2 batches;
156 s Git Bash, 92 s WSL;       178.9 MiB for tags <= v3.7.1    byte-equal in Git Bash, PS 5.1, WSL
no flag: whole-tree prefetch    fallback only, from R3 on                      │
✗ as the primary                                                               │
where the clone lives ─────────────────────────────────────────────────────────┤
  outside the receiver (C1)     at .tfw/.upstream/ (C2)         in .tfw/.upstream/.clone:
  ✗ the staging path is shared  ✗ nested .git becomes a         copy .tfw, check, delete
    by installed and pinned       gitlink under git add -A      ✓ 95/95 both shells, no gitlink
    text                                                                       │
which files the clone writes ──────────────────────────────────────────────────┤
  S1 cone mode                                    S2 exact patterns
  + top-level files, + upstream state, + trees    framework files + trees only
  0.64 MiB (GitHub) · Git's recommended mode      0.47 MiB (local) · deprecated mode
  Git >= 2.25                                     Git >= 2.35
          └──────────── owner rules A1 (claim 5, principle 1) ────────────┘
          trees travel in both and grow with the repository → A2 (§1)

GUARDS that every surviving form carries
trap (observed)                                       guard
installer default autocrlf=true: every file CRLF      -c core.autocrlf=false on the clone
user attributes file eol=crlf beats both settings     -c core.attributesFile= on the clone
filtered hash and git status hide CRLF                hash-object --no-filters against ls-tree
host without filters: exit 0, markers say partial     count-objects -vH after the clone; disclose
Git Bash turns /.tfw/ into C:/Program Files/Git/...   no pattern begins with /
clone --branch takes no SHA                           init + fetch --depth 1 <SHA> (S3)
Git too old for an option: exit 129                   the clone without filter/sparse, disclosed

VERSION LINE at new-task start
installed_from: "self" ──► no call, no offer
receiver ──► one ls-remote --tags --refs, about 5 s limit on the agent's tool (Git has none)
              ├─ exact vX.Y.Z only (5 pre-release tags sort above their release)
              ├─ newer ──► installed · newest · N newer · /tfw-update now or after this task
              └─ failure or limit ──► "unknown (reason)"; nothing blocks (unbounded: 21 s / 131 s)

RELEASE ARCHIVE
today 178.9 MiB ──► R2 0.55 MiB, drops tools/migrations/2.0.0 ──► R3 0.56 MiB, keeps it
upstream state inside .tfw/ still ships ──► flagged owner decision (R5 lines: 0.45 MiB)
```

Two links in the map are causal. The staging path is fixed by the two texts that share it, not by
preference. And the cone/exact split exists only because X7 found the shell rewrite; before that, cone
mode looked like the only sparse form.

## Iteration Status

- **Iteration:** 1 of 2 minimum / 3 maximum.
- **Hypotheses tested:**
  - H1: supported with conditions; the Codex sandbox was not observed.
  - H3: the cost is confirmed, and the false case was observed for dropped packets.
  - H4: confirmed, with an update exception for receivers below 2.0.0.
- **Hypotheses deferred:** H2, to iteration 2 as planned.
- **Gaps discovered:**
  - Receivers do not ignore `.tfw/.upstream/`.
  - The directory structure travels with every fetch and grows (A2).
  - A host without filter support looks like success (X2).
  - Upstream state ships inside `.tfw/` (flagged).
  - S2, and S3 with a tag, were not observed on GitHub.
  - Unobserved: the Codex sandbox, macOS, Git below 2.42, real hosts without filter support, and
    machines without long-path support.
- **Superseded decisions:**
  - D4 (S1 staging) supersedes Extract's C1/C3 primary pair; [X1](4_challenge.md) eliminated C1.
  - D7 (S3) supersedes Extract's "C11 or C12".
  - D6 (one fallback) supersedes Extract's plan to keep C6 as the Git-only answer to old Git.
  - D8's limit of about 5 s supersedes X9's example of 10 s.
  - R5 moves from "set aside" (X4) into the flagged owner decision (correction 3).
  - Correction 1 replaces the unrecorded Gather conclusion that exact sparse sets do not work.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|---|---|---|
| 1 | H2: where update time goes | Claim 5's bounded removals and DoD 7 need measured cost | Time a trial update of a scratch receiver copy step by step under the current rules: download, staging, re-hashes, checks, receipt. |
| 2 | Staging exposure | `git add -A` during an update stages the payload copy, or a gitlink while a clone exists (DoF 1) | In the subtraction challenge, test whether D4's order closes the window or the update needs a local exclude; weigh the answer against principle 5. |
| 3 | S3 with a tag on GitHub | One sequence for tags and SHAs saves text, but S3 with a SHA took 15.2 s once on GitHub, against 4.8–8.2 s for S1's clone | One light run per form (≈0.6 MiB each) under a new gate answer, or the Executor's DoD 2 trials. |
| 4 | Owner rulings on A1, A2 and the flagged decision | The TS's command text depends on A1 | The Coordinator routes them; iteration 2 does not wait for them. |
| 5 | Unobserved environments | Principle 7; DoD 2 | The TS names as unobserved: the Codex sandbox, macOS, Git below 2.42, hosts without filter support, machines without long-path support. |

### Recommendation

- [ ] **SUFFICIENT**
- [x] **MORE NEEDED** — iteration 2 as planned: H2 and the subtraction challenge (`min_iterations: 2`). H1, H3 and H4 are answered as far as this machine and the local-only binding allow. The TS also needs the owner's rulings on A1 and A2.
- [ ] **BLOCKED**

## Conclusion

This iteration measured every candidate way of fetching only the framework of one pinned tag, in both
Windows shells and in WSL, and it found the traps that make the obvious candidates wrong:
- R1's own fix moves few bytes but makes one round trip per file, so on this connection it was slower
  than downloading everything.
- The installer default, and user attribute files, rewrite every file to CRLF, and the usual hash hides
  it.
- A host that ignores the filter reports success.
- Git has no connect limit, so an unbounded version check can take two minutes.

The surviving method is a blobless, depth-1 sparse clone that Git writes into today's staging path. It
runs under two clone settings, with a size check and a raw-byte check. It keeps the pin guarantees
unchanged and moves 0.47–0.64 MiB instead of 114 MiB. Without these trials the TS would probably have
shipped R1's fix or the default line-ending setting.

What remains open is contractual: whether the frozen "only the framework travels" should name the
directory structure and, under cone mode, the top-level files and upstream state. The owner rules on
that through A1 and A2.

Self-critique:
- I made a second heavy GitHub transfer that no gate had approved (E10).
- A failed trial shaped two stages without being written down, and X7 then quoted it as if it had been
  (correction 1).
- S2, and S3 with a tag, were measured only locally.
- The research harness had a path bug inside receiver repositories. It failed loudly and was fixed
  against the known-good and known-CRLF samples before the staging results were recorded.
- X1, X4, X8 and X9 needed the corrections above.

### Material handover at this return

- **Producer / recipient:** Researcher `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher`
  to the parent Coordinator `claude-code:session:local_e821cd09-6696-482b-bd88-ca93dba929a2`.
- **Source / epoch:** tag `v3.7.1` from GitHub and from this repository at `e3ae21fb`; Git 2.42.0 for
  Windows, Git 2.43.0 in WSL, Windows PowerShell 5.1; 2026-09-29.
- **Inspected scope:**
  - Stage files 1–4; `status.md`, `iterations.yaml`, the HL and the four gate answers.
  - `update.md`; the `3.1.0` guide's config rows; the config template; scratch trial traces.
  - `conventions.md` sections: HL Contract, Commit Attribution, Fact Categories, Knowledge handover,
    Current knowledge use, File Classification and Anti-patterns.

  No receiver, remote or GitHub state changed. E10 is the one boundary breach, accepted in gate
  answer 2493.
- **Material:** D1–D12, A1 and A2, the flagged decision, and corrections 1–5.
- **Knowledge used:** D70, D82 (scoped by `TKL-20260913-01` only for the Knowledge Gate), F23 and D2,
  per HL §7.2. No record points at D70, D2 or F23.
- **Uncertainty:** Q4–Q10 and the Open Threads.
- **Continuation:** the Coordinator reviews this iteration via `/tfw-plan`, applies R1–R7, transcribes
  A1 and A2 into §12 as `PROPOSED` for the owner, raises the flagged decision, and decides on
  iteration 2.
- **Unresolved owner decisions:** A1, A2 and the flagged question.

---

*RES — TFW_20260929-003444_LFD: Lightweight Framework Delivery | 2026-09-29*
