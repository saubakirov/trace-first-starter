# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260929-003444_LFD](../../HL-TFW_20260929-003444_LFD.md)
> Goal: Installing or updating TFW moves only the framework, about one megabyte, by one written method, and a newer release shows in one line when new work starts; the owner decides whether and when to update.
> Producer unit: `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher` · mode focused · single pass
> Continuation source: [gate answer 41f0](../../journal/20260929-033020__gate_answer__41f0.md) in `39940afd514147570cd0cc9bb78b1cec325ef504`

New evidence in this stage:
- **History count, extended as approved.** `git log --all --oneline` over `.tfw/.upstream-source`,
  `.tfw/.source` and `.tfw/.upstream.tar` found 0 commits in all 20 repositories. With Gather G7, none of
  the four staging names seen in receipts has ever entered receiver history.
- **One scratch-receiver test.** A fresh `git init` in scratch, with no network and no real receiver.
- **One documentation source.**

## Configuration Space

The columns are Gather's dimensions D5–D8, plus D4's change form applied to the second adapter sync.
**N** marks a combination nobody proposed. Nothing is ranked here; the Findings analyse, Challenge
decides.

| Config | D5 Payload verification | D6 Project checks | D7 Receipt | D8 Staging control | Second adapter sync | Note |
|--------|-------------------------|-------------------|------------|--------------------|---------------------|------|
| P0 | several points (practice) | before and after (practice) | today's practice | cleanup at Step 4 only | run twice | today, as practised |
| P1 | once after the fetch, once after the copy, against staging | after only | the template as it is | order only (clone deleted after the copy check) | removed; direct assertions stay | text almost unchanged |
| P2 **N** | the fetch check, then installed files against the pinned tree's blob list | after only | the template as it is | order only | removed | the end state is checked against the pin, not against staging |
| P3 | as P1 | "not affected" when a check reads no changed path | shorter template wording | order only | removed | adds a judgment call |
| P4 **N** | as P2 | after only | references instead of pasted output | an exclude line written with staging and removed with it | removed | also covers blocked cleanup |
| P5 | as P1 | after only | the template as it is | an ignore line written by init | removed | new receivers only; a project-owned file |
| P6 | only at the end | after only | the template as it is | a check before sealing that staging is untracked | removed | detects, does not prevent |

## Findings

### E1 — H2, the bounded answer

**The most completely timed update: R1's update to 3.7.1.** It runs 14.5 min from its first network
command to the seal:

| Stage of that update | Clock span | Source |
|---|---:|---|
| pin and fetch, including the 114 MiB download | ≈ 1 min (22:06 → ≈22:07) | receipt clocks; the download itself ≈ 41 s by iteration 1's measurement of the same method from this machine |
| apply | ≈ 10 min (≈22:07–22:17) | receipt |
| project checks | ≈ 2 min (22:17:49–22:19:40) | receipt |
| cleanup and seal | ≈ 1 min (→ 22:20:34) | receipt |

R6's update is timed only from start to seal (24.7 min). Six more apply windows run 2.5–13 min
(Gather G3).

**The answer, split along H2's two claims:**
1. **"Download is a minority": supported on this connection.** The old download is ≤ 5% of R1's 3.7.1
   update; a light fetch is under 1%. The false case appears only below ≈ 0.7–1.2 Mbit/s (inferred from
   bytes, not observed).
2. **"The procedure's repeated steps dominate": not established.** The repeats sit inside the apply
   window together with necessary work, and no receipt times them separately. What the evidence shows
   instead is that they found nothing (Gather G4, G5), and that time before the first network command is
   not recorded at all.

**Consequences:**
- The removals below rest on "found nothing and is implied by another check", or on "habit, not mandate",
  not on a measured saving. DoD 7 still requires the RF to give each removal's measured cost; the
  Executor's trial update under DoD 1 is where that cost can be measured.
- **The removals reach receivers one update before the light fetch does.** After pinning, the pinned
  target's `update.md` governs Steps 1–4 ("afterward the pinned target's `update.md` governs"). Step 0,
  the fetch, still runs from the installed text. So a release that removes steps shortens the very first
  update to it, while its light fetch helps only from the update after that. (Inferred from the Read
  Contract; HL §9's first risk is the fetch half of this.)

### E2 — The step matrix

| Step | Cost now | Protects | Caught anything? | Change forms | Text effect in `update.md` |
|---|---|---|---|---|---|
| Payload re-hash at several points | unmeasured; 3 passes over 95 files (R1 3.7.1) | staging changed between steps | 0 drift in 3 passes | narrow to P1 (fetch check, then installed against staging) or P2 (installed against the pinned tree) | "source coherence" stays; P2 adds ≈ 20 words |
| Second adapter sync | unmeasured; a second full copy loop | idempotence | 0 diff in 5 receipts (4 runs, 1 assertion without a run) | remove: byte parity, exactly one managed block and unchanged neighbours already imply it; the same sentence already rejects "duplicate blocks, drift" | −3 words ("or second-run diff") |
| Project checks before the update | 12.11 s (R1 3.4.0 tests) | labelling pre-existing failures | failures were labelled pre-existing by reasoning, not by a before-run (R1 3.4.1, R6) | drop the habit; it is not mandated | none |
| Project checks after the update | 37 s to ≈ 2 min | a check that reads framework files failing because of the update | none in 17 receipts; 2 pre-existing | keep; or narrow to "not affected, with the reason" when a check reads no changed path (as R1 3.6.1 did) | narrowing adds ≈ 20 words |
| Receipt length | writing time unrecorded; 548–3,711 words | the record | — | narrow the template's "Link exact evidence …" line, which invites pasted output | template only |
| Tag re-lists and pin re-reads beyond one | ≈ 1–2 s each | a moved tag | never moved | leave as it is (habit; negligible) | none |
| Knowledge-lifecycle re-observation | a 1,160-word guide re-read and re-checked | no false completion | its revalidation caught a concurrent write | keep | — |
| Revalidation before preserved writes | seconds | concurrent change | caught once | keep | — |
| Migration obligations | seconds | customizations | caught once (custom files) | keep | — |
| Re-observation at equal version | seconds | interrupted updates | the rationale at CHANGELOG line 487 | keep | — |
| Fetch (Step 0) | ≈ 41 s → ≈ 4–8 s | — | — | replace (iteration 1) | ≈ 50 words replaced |

### E3 — Staging exposure: windows against controls

**Evidence.**
- 0 commits for any of the four staging names, in 20 repositories.
- A concurrent session in the same tree, recorded twice.
- One cleanup blocked by policy (R8).

**Scratch test** (fresh repositories in scratch; a nested repository at `.tfw/.upstream/.clone` plus a
payload file):
- **No exclude:** `git add -A` warned "adding embedded git repository", staged 1 gitlink and the payload
  file, and `git ls-files -- .tfw/.upstream` listed 2 entries.
- **With `.tfw/.upstream/` in `info/exclude`:** status was empty, `git add -A` staged nothing and printed
  no warning.
- **From a linked worktree:** `git rev-parse --git-path info/exclude` resolved to the repository's shared
  exclude file, so one line covers every worktree. The Git documentation says `--git-path` resolves
  "$GIT_DIR/<path>" and takes relocation variables into account; the worktree behaviour was observed, not
  documented.

| Control | Clone window (seconds) | Payload-copy window (the apply) | Blocked cleanup | Receiver write | Words | Shell dependence |
|---|---|---|---|---|---:|---|
| A. Order only | closed after the copy check | open | open | none | 0 (already D4) | — |
| B1 **N**. Exclude line written before the clone, removed with staging | closed | closed | closed; the line stays with the leftover | one line in `info/exclude`, removed at cleanup | ≈ 20 | the append differs by shell (`echo >>` or `Add-Content`) |
| B2. Exclude line written once and kept | closed | closed | closed | one permanent local line | ≈ 15 | same |
| C. Ignore line written by init | closed | closed | closed | an edit to the project's own `.gitignore`; existing receivers need a migration | init text plus a guide | — |
| D. Check before sealing: `git ls-files -- .tfw/.upstream` is empty | detects | detects | only if it runs | none | ≈ 15 | — |

`info/exclude` is per repository, not versioned and not shared with clones (Gather G7). B1 and B2 are
therefore local and invisible to the project's history. They are still a write outside `.tfw/`, which
the receipt would have to disclose.

### E4 — Combinations nobody proposed

- **P2: check the end state against the pin.** At the fetch, keep the pinned tree's blob list from
  `git ls-tree`. After applying, check every installed framework file against it with
  `hash-object --no-filters`. A staging change between steps then cannot pass unnoticed, which removes the
  only purpose of the intermediate re-hashes. P1 checks the installed files against staging, so it trusts
  whatever staging holds at that moment.
- **B1: the exclude lives exactly as long as staging.** Exposure is closed in every window, and nothing
  persistent remains after a normal cleanup.
- **The timing of benefits (E1).** Step removals shorten the first update to the release that carries
  them; the light fetch shortens only the update after that.

### E5 — Fetch form (iteration 1's open thread 3)

- **Time.** In single runs, S3 with a tag (3.96 s) was no slower than S1 (4.8–5.0 s in PowerShell). Using
  one sequence for tags and SHAs costs no time here.
- **Text.** Two forms are possible, both within the 173-word headroom (word counts approximate):
  - F1: the clone form for tags and S3 for an untagged commit. About 2 command lines plus one sentence,
    ≈ 50 words.
  - F2: S3 for both. About 8 command lines, ≈ 70 words.
- **The PowerShell 5.1 trap.** S3 cannot write an empty `core.attributesFile` with `git config … ""`, so it
  passes `-c core.attributesFile=` on the `checkout` (Gather G8).
- **Pin fit.** S3's tag form gives `FETCH_HEAD` as the tag object and `HEAD` as the commit. The
  immutability recheck compares both with `ls-remote`, as with the clone form.

### E6 — What removals cannot touch

- **The pinned guides are immutable.** Their obligations stay in force for crossings of their versions:
  `knowledge-lifecycle.md` "always applies" when present, and the `3.3.0` guide is read before any
  already-current result. Removals apply only to `update.md`'s own steps and to the templates it names.
- **Sealed receipts are never rewritten.** A shorter template wording affects only new receipts.
- **DoF 5 holds.** Every step that caught something, or that answers a recorded failure, stays in the
  matrix as "keep".

### E7 — Text budget

`update.md` has 1,227 words, 173 below the 1,400 ceiling. Each candidate's effect:

| Candidate | Words |
|---|---:|
| Drop "or second-run diff" | −3 |
| The fetch text | ≈ 50 replaced by ≈ 50–70 |
| P2's end-state check | ≈ +20 |
| A staging control | 0 (A), ≈ +20 (B1), ≈ +15 (B2 or D) |
| Habits (re-hashes, before-runs, re-lists) | 0; they are not in the text |

Every combination in the Configuration Space fits.

### External source

- Git, [git-rev-parse](https://git-scm.com/docs/git-rev-parse): `--git-path` resolves "$GIT_DIR/<path>"
  with relocation variables; `--path-format=absolute` prints absolute paths.

Web actions: 1 (soft limit 5). Project files read: none new beyond Gather's. Evidence items: 24 `git log`
runs over three names and one scratch test.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H2, bounded: the download is a minority on this connection; that repeated steps dominate is not established | per-step times, for the Executor's DoD 1 trial |
| Removals reach receivers one update before the light fetch (Steps 1–4 follow the pinned text) | inferred from the Read Contract, not observed |
| The second sync is implied by assertions the text already requires; before-runs are habit | their time cost |
| P2 checks the end state against the pin, making intermediate re-hashes pointless | its words (≈ 20) against P1's none |
| Staging: no incident for any of four names in 20 repositories; an exclude line closes every window in the scratch test and covers worktrees | receivers' own ignore files not inspected (outside approval) |
| S3 for tags costs no time; F1 ≈ 50 words against F2 ≈ 70 | single runs |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed? (H2 bounded; step matrix with evidence; thread 2 windows and controls; open thread 3 closed)
- [x] Configuration Space built from Gather dimensions?

**Stage decisions.**
1. **H2 is answered in bounded form:** the first claim is supported on this connection; the second is
   unmeasured and is left to the Executor's trial.
2. **Taken to Challenge:**
   - P1 against P2 for payload verification;
   - removing the second sync;
   - dropping the before-run habit;
   - keeping or narrowing the after-run project checks;
   - the receipt template's evidence line;
   - staging controls A, B1, B2 and D. C is noted as init-only and needs a project-file decision.
3. **Set aside:** any change to revalidation, migration obligations, equal-version re-observation, the
   final message or the one mandated pin recheck.

**Metacognitive note.**
- **New:** end-state checking against the pin, the one-update lead that removals have over the light
  fetch, and a single exclude line covering all worktrees.
- **Confirmed:** the repeats found nothing, and nothing staged ever reached history.

**Knowledge handover.**
- **Producer:** as in the header.
- **Source and epoch:** receivers' receipts and Git history as of 2026-09-29; scratch tests on Git 2.42.0
  for Windows.
- **Material:** E1–E7.
- **Uncertainty:** the Remaining column.
- **Continuation:** Challenge, after the Coordinator's gate.

Stage complete: YES
→ User decision: ___
