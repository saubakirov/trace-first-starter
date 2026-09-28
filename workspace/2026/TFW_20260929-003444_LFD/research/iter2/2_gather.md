# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260929-003444_LFD](../../HL-TFW_20260929-003444_LFD.md)
> Goal: Installing or updating TFW moves only the framework, about one megabyte, by one written method, and a newer release shows in one line when new work starts; the owner decides whether and when to update.
> Producer unit: `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher` · mode focused · single pass
> Continuation source: [gate answer 8f5a](../../journal/20260929-031130__gate_answer__8f5a.md) in `9ba6fe0d867dcb07b2e8ddc3c1d6cab58980bce9`

Sources in this stage:
- **Receipts.** The update receipts of the receivers on this machine, read only. Receivers appear as R
  numbers: R1 and R2 as in HL §2, R3–R8 by the date of their first receipt. The mapping to real folders
  exists only in the session scratch area.
- **Receiver history.** The approved read-only `git log --all --oneline -- .tfw/.upstream` in each
  receiver, reported as counts.
- **GitHub.** One light run each of S2 and of S3 with a tag, in Windows PowerShell 5.1, each rehearsed
  first on the local server. The clones were deleted after checking.

Nothing in any receiver, remote or GitHub changed.

## Dimensions

No alternative is recommended here; Extract and Challenge decide.

| Dimension | Alt A | Alt B | Alt C | Alt D _(if any)_ |
|-----------|-------|-------|-------|-----------------|
| D1 Evidence for the time split | clock values in receipts | iteration 1's download times and a link-speed model | counts of repeated steps and receipt size | a timed trial update (excluded) |
| D2 Where a step comes from | `update.md` | a pinned migration guide | a template field | agent habit |
| D3 What a step protects | receiver state | the pin and provenance | an owner decision | nothing observed |
| D4 Change form | keep | narrow its trigger or scope | merge with another step | remove |
| D5 How often the payload is verified | once after the fetch and once after the copy | at several points (observed: 3) | only at the end | — |
| D6 Project checks | all configured checks after applying | only checks whose inputs include changed paths | before and after | reported as not applicable when only instruction text changed |
| D7 Receipt form | the template as it is | a shorter template | references instead of copied evidence | today's practice (4–7× the template) |
| D8 Staging exposure control | order only: delete the clone right after the copy | a local exclude line in `info/exclude` | an ignore line written by init, or by a migration | a check before cleanup that staging is untracked |

## Findings

### G1 — What `update.md` mandates, step by step

| # | Where | Mandated action | Trigger | Protects | Observed cost or proxy |
|---|---|---|---|---|---|
| 1 | Read Contract | read every applicable migration guide and changelog range | always | migration obligations | grows with the version gap; the guides total 20,899 words |
| 2 | Step 0 | activation and routing | always | authority | — |
| 3 | Step 0 | pin: operator's tag, `VERSION` equal to the tag, source clean under `.tfw/`, full SHA recorded | always | the pin | one `ls-remote` ≈ 1–2 s |
| 4 | Step 0 | materialize the object into `.tfw/.upstream/` | always | — (transport) | 114 MiB ≈ 41 s before; light ≈ 4–8 s |
| 5 | Step 0 | recheck immutability before adapter sync | always | the pin, if the tag moves | once by the text; 2–3 times in receipts |
| 6 | Step 1 | read the pinned `update.md`; verify workflow, manifest, templates, ranges and guides come from one object | always | the pin; obligations | R1's 3.7.1 update re-hashed the whole payload here |
| 7 | Step 1 | re-observe at equal version; `knowledge-lifecycle.md` "always applies" when present | conditional / always | state: no false completion | a 1,160-word guide re-read and re-checked on every update |
| 8 | Step 1 | discover the accountable human, containers, checks, customizations, grants; at most one material question | always / conditional | owner decisions | owner waits (R6's re-entry was sealed 44 min after its first receipt) |
| 9 | Step 2 | compare installed payload with the target; classify; preview | always | state | — |
| 10 | Step 2 | the never-overwrite list; key-by-key config merge; README classification; Daily gate | always / conditional | state | — |
| 11 | Step 3 | apply by connected group; the guides' preservation with revalidation before each write | always / conditional | state | apply windows of 2.5–13 min (G3) |
| 12 | Step 4 | adapter sync: 4 adapters, 10 commands, profile pointers; reject drift or a second-run diff | always | adapter integrity | a second sync run in 4 receipts, asserted without running in 1 |
| 13 | Step 4 | verify ref, SHA, version, source coherence, preservation, migrations, adapter parity, project checks, recovery, cleanup | always | state; the pin | project checks 37 s to about 2 min where timed |
| 14 | Step 4 | remove `.tfw/.upstream/` when safe | always | no stray paths | blocked once (R8) |
| 15 | Step 4 | seal one receipt from the template | always | the record | 548–3,711 words against the template's 527 |
| 16 | Step 4 | render the final message from the briefing template | always | the owner's report | a 240-word template |

### G2 — The receipt corpus

The 28 roots under the projects root are 24 Git working trees, belonging to 20 distinct repositories, and
4 folders outside Git; the HL's count of 24 matches the working trees. The repositories hold 45 receipt
files but only 17 distinct receipts, in 8 repositories. Words are counted by whitespace. Below, "R1 3.4.0"
means R1's update to 3.4.0.

| R | Update (2026) | Words | Clock values in the receipt | Fetch and staging | Notable |
|---|---|---:|---|---|---|
| R1 | 2.2.0 → 3.1.0 (09-08) | 2,017 | applied "immediately before" the seal | local upstream checkout | second sync run: no diff |
| R1 | 3.1.0 → 3.3.0 (09-13) | 2,767 | apply 13 min; seal 3 min later | local upstream checkout | a concurrent session committed three times during the run; pin read 3 times |
| R1 | 3.3.0 → 3.4.0 (09-14) | 3,158 | pin to seal ≈ 3.6 h; apply 2.5 min; checks 37 s | local upstream checkout | first pass stopped at a revalidation check; tests run before and after |
| R1 | 3.4.0 → 3.4.1 (09-20) | 2,314 | apply to seal 3.3 min | fresh clone from GitHub | a lint and a test suite were already failing, "not implicated" |
| R1 | 3.4.1 → 3.5.1 (09-22) | 3,711 | apply to seal 11 min | bare clone in the session scratch area | a migration obligation found custom files and refused a retirement |
| R1 | 3.5.1 → 3.6.0 (09-23) | 2,174 | apply to seal 4 min | bare clone in scratch | lint and tests after the last edit |
| R1 | 3.6.0 → 3.6.1 (09-24) | 1,077 | seal only | partial clone + archive: 114 MiB | project checks deferred: "instruction text only" |
| R1 | 3.6.1 → 3.7.1 (09-28) | 2,306 | first fetch command to seal 14.5 min; apply ≈ 10 min; checks ≈ 2 min | partial clone + archive: 114 MiB, diagnosed | payload re-hashed 3 times; tag re-listed twice |
| R2 | 0.8.7 → 3.6.1 (09-24) | 900 | attempt window 4 min | shallow clone at the tag into `.tfw/.upstream/`, which this receiver ignores | checks are placeholders |
| R3 | 3.0.0 → 3.1.0 (09-08) | 788 | seal only | local upstream checkout | pin re-read before sync |
| R4 | → 3.2.0 (09-10); → 3.4.1 (09-20) | 548; 641 | seal only | a source folder inside the receiver at `.tfw/.upstream-source/`, beside `.tfw/.upstream/` | checks are placeholders |
| R5 | 2.0.0-dirty.4 → 3.3.0 (09-13) | 1,965 | seal only | fresh clone inside the receiver at `.tfw/.upstream-source/` + archive | pin read 3 times |
| R6 | 2.2.0 → 3.3.0 (09-14), plus a re-entry | 1,619; 929 | start to seal 24.7 min; re-entry sealed 44 min later | clone in scratch + archive | tests failed before the update, "pre-existing"; the re-entry closed a group after an owner answer |
| R7 | 2.0.0-dirty.4 → 3.4.1 (09-17) | 617 | none | `.tfw/.upstream/`, called a "worktree" in the receipt | older receipt form |
| R8 | → 3.7.0 (09-28) | 824 | seal only | checkout at `.tfw/.source/` + archive + a `.tar` | cleanup blocked; staging kept; receipt text stored as `?` (G9) |

### G3 — H2: what the clocks say

- **Download (measured).** On this connection the old 114 MiB download took ≈ 41 s (iteration 1, one run).
  The light forms take 3.9–8.2 s: S1 4.8–8.2 s (iteration 1); S2 and S3 with a tag 3.9–4.0 s (G8).
- **Procedure (measured in receipts).**
  - Apply windows: 13, 2.5, 3.3, 11, 4 and ≈ 10 min (R1) and 4 min (R2).
  - From start to seal: 14.5 min (R1's 3.7.1 update, from its first fetch command) and 24.7 min (R6).
    R1's 3.4.0 update took ≈ 3.6 h from pin to seal. Its receipt records a concurrent session and a wait
    loop, and does not account for the rest.
- **Download share (computed).** The old download is 41 s of 14.5 min (4.7%) and of 24.7 min (2.8%). A
  light fetch is under 1%.
- **Slower links (inferred from bytes, not observed).** Take R1's 3.7.1 procedure without its download
  (≈ 13.8 min). The old 114 MiB download (956 Mbit) is then:
  - ≈ 10% of the update at 10 Mbit/s;
  - ≈ 37% at 2 Mbit/s;
  - more than half only below ≈ 1.2 Mbit/s; against R6's 24.7 min, if all of it were procedure, below
    ≈ 0.7 Mbit/s.

  At 1 Mbit/s the light fetch (≈ 5 Mbit) takes about 5 s.
- **Not measurable from receipts.** How much of the apply window each repeated step takes, how long
  reading takes, and how long the receipt takes to write. No receipt keeps clocks per step, except for
  project checks.

### G4 — Repeated steps: what the text asks for and what agents did

| Repeat | What `update.md` says | Observed | Found anything? |
|---|---|---|---|
| Payload re-hash | Step 1 "verify … come from the same object"; Step 4 "source coherence"; neither says how often | R1 3.7.1: 3 passes (after materialization, before adapter sync, before cleanup) | 0 drift each time |
| Tag re-list / pin re-read | Step 0 "Recheck immutability before adapter sync" (once) | R1 3.7.1: 2 re-lists; R1 3.3.0 and R5: 3 reads | never moved |
| Second adapter sync | Step 4 "reject … drift or second-run diff" | run in 4 receipts; asserted without running in 1 | 0 diff |
| Project checks before and after | Step 4 "project checks"; "Label pre-existing failures" | R1 3.4.0: tests before (12.11 s) and after (22.15 s) | nothing the update caused |
| Knowledge-lifecycle re-observation | Step 1 "always applies"; Step 0 "a prior receipt never proves completion" | R1 3.6.1: guide "byte-unchanged … re-observed only" | its revalidation caught a concurrent write in R1 3.4.0 (G5) |

Only one of these repeats has a recorded reason: CHANGELOG line 487 says equal versions "no longer end an
interrupted update without checking actual source and state". None was found for the second-run diff
(searched: second-run, idempotent, twice, re-run).

### G5 — What the checks caught

- **Real conditions, caught by checks that protect state or the owner's constraint:**
  - revalidation before a preserved write, when a concurrent session changed the same file (R1 3.4.0);
  - a migration obligation, which found custom files and refused a retirement (R1 3.5.1);
  - the owner's fetch-size constraint, which exposed the 114 MiB download (R1 3.7.1);
  - a failed attachment write, disclosed (R1 3.3.0).
- **Only pre-existing problems, found by project checks:** twice. R1 3.4.1 had a test suite that was
  already broken; R6's tests failed before the update.
- **Nothing:** the payload re-hash (3 passes), the tag re-lists, and the second sync run.
- **Placeholders or deferred project checks:** R2, R4 (both receipts), R1 3.6.1 and R8.

No receipt records a project check failing because of the update.

### G6 — Receipt length

- **Sizes.** The template has 527 words: §1 70, §2 91, §3 125, §4 117, §5 65. R1's eight receipts run
  1,077–3,711 words (mean 2,440); the others 548–1,965.
- **Where the words go.** Most sit in §3 (effects, up to 936 words) and §4 (verification, up to 774). In
  R1's 3.3.0 and 3.4.0 receipts §2 also grew, to 693 and 914 words. Verification tables grow from the
  template's 6 rows to 14–15, with commands and results inside the cells.
- **Why.** The template's own fields are short. Its request to "Link exact evidence; screenshots or
  summaries without a resolving path do not prove the receiver state" may be what invites inlined commands
  (inference).
- **Cost.** Writing time is not recorded anywhere.

### G7 — Staging exposure (open thread 2)

- **History.** No commit touching `.tfw/.upstream`, in any ref, in any of the 20 repositories.
- **Staging forms found in the receipts:** six.
  - an archive into `.tfw/.upstream/`;
  - `.tfw/.upstream/` called a "worktree" (R7);
  - a source folder inside the receiver at `.tfw/.upstream-source/`: a fresh clone in R5, not described
    in R4's two receipts;
  - a checkout at `.tfw/.source/` plus a `.tar` (R8);
  - a shallow clone straight into `.tfw/.upstream/`, which that receiver ignores (R2);
  - clones in the session scratch area (R1, R6).

  The other staging names were outside the approved `git log` path and were not checked.
- **Cleanup.** Every receipt that mentions cleanup reports it done, except R8. There, removal "blocked by
  policy" left `.tfw/.source/`, `.tfw/.upstream/` and the `.tar` in the receiver.
- **Concurrency.** A concurrent session in the same working tree is recorded twice (R1 3.3.0 and 3.4.0).
  That is the condition under which another session's `git add -A` would pick staging up.
- **How long each window stays open.**
  - The clone: seconds, until it is deleted after the copy.
  - The payload copy under `.tfw/.upstream/.tfw/`: until Step 4 cleanup, which is the whole apply window
    (2.5–13 min).
  - Blocked cleanup: indefinitely (R8).
- **External sources.**
  - `info/exclude` is per repository, not versioned, not shared with clones, below `.gitignore` in
    precedence, and does not affect tracked files.
  - `git add` never adds ignored files unless forced, and warns when it adds an embedded repository.

### G8 — S2 and S3 with a tag, on GitHub (PowerShell 5.1, one run each)

| Run | Steps | Stored packs | Size checks | Time | Bytes |
|---|---|---:|---|---:|---|
| S2 | clone `--no-checkout`; exact patterns; `checkout` | 487,615 B (0.47 MiB) | 180 KiB after the clone; 499 KiB at the end | 2.21 + 1.73 = 3.94 s | 88/88 |
| S3, tag | `init` and config; `sparse-checkout set .tfw`; fetch by tag; `checkout FETCH_HEAD` | 613,185 B (0.58 MiB) | 180 KiB after the fetch; 623 KiB at the end | 0.30 + 1.89 + 1.77 = 3.96 s | 95/95; `FETCH_HEAD` is the tag object, `HEAD` the pinned commit |

- **Baseline.** S1 took 4.8–5.0 s and 670,042 B in PowerShell (iteration 1). With single runs, S3's tag
  form shows no time penalty on this connection. Iteration 1's 15.2 s for the SHA form, in Git Bash, stays
  unexplained.
- **Local rehearsals** with the same flags gave S2 502.04 KiB, 88/88, and S3 627.38 KiB, 95/95.
- **PowerShell 5.1 drops an empty argument.** `git config core.attributesFile ""` exited 1 and stored
  nothing. Only the non-obvious `'""'` stored the empty value. The one-token form `-c core.attributesFile=`
  works for `clone` and for any single command. So S3's `init` form cannot write the empty value as
  persistent config in plain PowerShell; the S3 run passed it with `-c` on the `checkout`.

### G9 — Other observations

- **R8's receipt was damaged when it was written.** It is stored as plain ASCII with CRLF line endings,
  and its Russian text became `?` (297 runs of three or more). The receipt does not say how it was
  written. A write in a non-UTF-8 code page, such as Windows PowerShell 5.1's `Set-Content` default, would
  produce this (inference).
- **Fetch improvisation continued.** The receipts show six staging forms across 8 repositories, and four
  fetch forms in R1 alone: local checkout, fresh clone, bare clone in scratch, and partial clone with
  archive. This is iteration 1's D2 case again (principle 2).
- **An earlier era said the same.** The first external field report (TFW-60, an early procedure) says the
  file copying "took minutes" and the rest was reconstruction. It is qualitative, from before the current
  workflow.

### External sources

- Git, [gitignore](https://git-scm.com/docs/gitignore): `$GIT_COMMON_DIR/info/exclude` holds patterns
  "specific to a particular repository but which do not need to be shared"; precedence below `.gitignore`;
  tracked files are unaffected.
- Git, [git-add](https://git-scm.com/docs/git-add): "will warn when adding an embedded repository"; "will
  not add ignored files by default".

Web actions: 2 (soft limit 5). Project files read: 7 (`update.md`, the receipt and briefing templates,
`KNOWLEDGE.md` rows D11 and D70, CHANGELOG searches, the migration-guide word counts, one field-report
line). Evidence items, counted separately: 17 receipts and 24 `git log` runs.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Receipts carry more clock data than the Briefing's inventory found: 7 apply windows and 2 start-to-seal spans | no clocks per step; reading and receipt-writing time unmeasured |
| The old download is 3–5% of a timed update on this connection; the light fetch is under 1%; the old download dominates only below ≈ 0.7–1.2 Mbit/s (inferred) | slower links not observed |
| Repeats: payload re-hash (3 passes, 0 drift), a second sync (0 diff), before-and-after checks, tag re-lists | their time cost |
| Checks that caught real conditions protect state or the owner's constraint; project checks found only pre-existing failures | — |
| Receipts run 548–3,711 words against 527; the bulk is in §3 and §4 | why agents inline commands (inferred from the template's wording) |
| Staging never entered history in 20 repositories; R8 kept staging after a blocked cleanup; concurrent sessions recorded twice | other staging names not checked |
| S2 0.47 MiB and S3 with a tag 0.58 MiB, both ≈ 4 s on GitHub, byte-equal | single runs |
| PowerShell 5.1 drops empty arguments, so S3 needs `-c core.attributesFile=` on the command that writes files | — |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed? (H2 evidence gathered within the approved bound; subtraction candidates listed with what they caught; thread 2 evidence; both GitHub runs)
- [x] Dimensions identified?

**Stage decisions.**
1. **H2 rests on receipt clocks as well as on the one timed receipt.** Measured and inferred shares stay
   apart, as the gate answer requires.
2. **Extract maps these removal candidates:** payload re-hashes beyond one pass after the fetch and one
   after the copy; the second sync run; project checks before and after, and on updates that change only
   instruction text; receipt length.
3. **Kept out of the candidates:** revalidation before preserved writes, migration obligations,
   re-observation at equal version and the one mandated pin recheck. Each either caught a recorded
   condition or answers a recorded failure.
4. **Thread 2 has no observed incident.** Extract weighs the three windows: the clone (seconds), the
   payload copy (the apply window) and blocked cleanup (indefinite).

**Metacognitive note.**
- **New:** the receipt clocks, what each kind of check caught, the six staging forms, R8's damaged receipt
  and the PowerShell empty-argument trap.
- **Confirmed:** the download is a minority of update time on this connection, and fetch improvisation
  continues.

**Knowledge handover.**
- **Producer:** as in the header.
- **Source and epoch:** the receivers' receipts and Git history as of 2026-09-29; `v3.7.1` from GitHub
  and the local server; Git 2.42.0 for Windows, PowerShell 5.1.
- **Material:** G1–G9.
- **Uncertainty:** the Remaining column.
- **Continuation:** Extract, after the Coordinator's gate.

Stage complete: YES
→ User decision: ___
