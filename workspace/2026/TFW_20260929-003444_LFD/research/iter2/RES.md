# RES — TFW_20260929-003444_LFD: Lightweight Framework Delivery

> **Date:** 2026-09-29
> **Author:** Claude Code Researcher (in-session agent `lfd-researcher`)
> **Status:** 🔬 RES — Complete, iteration 2 of 2 minimum / 3 maximum
> **Parent HL:** [HL-TFW_20260929-003444_LFD.md](../../HL-TFW_20260929-003444_LFD.md)
> **Mode:** Pipeline / focused (Coordinator ruling)
> **Producer unit:** `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher`, continued by name; this in-session agent cannot read its own name back
> **Parent Coordinator:** `claude-code:session:local_e821cd09-6696-482b-bd88-ca93dba929a2`
> **Activation / dispatch source:** delegated; continuation [dispatch ded6](../../journal/20260929-030426__dispatch__ded6.md) @ `526da86d2a1bc65bd2ca6b405ea00245da690493`; synthesis continuation [gate answer 7138](../../journal/20260929-034232__gate_answer__7138.md) @ `d7e68aa8c2adbf8c8631a8ff93bec831a7d8e7f1`
> **Coordination authority:** `HL-TFW_20260929-003444_LFD.md @ c4044d2efc78e2e422849b27bccc4e0d9da2688e`; `baseline` · `native-gates` · `tfw-gates-only`
> **Originating proposer:** `{principal: none, unit: claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher}` for A3; no other proposal

---

## Research Context

Iteration 2 had three jobs:
- test H2, where update time goes, from existing evidence only;
- walk `update.md` for steps that cost time without protecting receiver state, the pin or owner
  decisions;
- settle how exposed staging is.

**Evidence used:**
- the 17 distinct update receipts in the receivers on this machine, read only and anonymized;
- read-only `git log` counts in those receivers;
- iteration 1's download timings;
- one light GitHub run each of S2 and of S3 with a tag;
- scratch receivers against the local server.

No trial update ran, and no receiver changed.

## Briefing

[1_briefing.md](1_briefing.md). Coordinator gates:
- [8f5a](../../journal/20260929-031130__gate_answer__8f5a.md) approved a bounded H2 and the history count.
- [41f0](../../journal/20260929-033020__gate_answer__41f0.md) extended the history count to three more staging
  names.
- [0e63](../../journal/20260929-033641__gate_answer__0e63.md) asked that B1 and B2 be weighed with and without
  update authority.
- [7138](../../journal/20260929-034232__gate_answer__7138.md) set this synthesis's two separations: the
  owner-dependent staging options apart from the recommendation, and the three kinds of time share
  apart.

Stages: [Gather](2_gather.md), [Extract](3_extract.md), [Challenge](4_challenge.md).

## Decisions

| # | Decision | Rationale |
|---|---|---|
| D1 | H2 gets a bounded answer. "Download is a minority" is supported on this connection. "The repeated steps dominate" is not established. | The measured, computed and unmeasured shares are kept apart in the H2 section below ([Extract E1](3_extract.md)). |
| D2 | The update's duration lives in the procedure: the apply window and time that no receipt accounts for. The download is not where it goes. | The old 114 MiB download is ≤ 5% of R1's timed 3.7.1 update; a light fetch is under 1% ([Gather G3](2_gather.md)). |
| D3 | Three removals survive with no loss of protection. (a) Drop "or second-run diff", provided blocks are counted by the template's exact markers. (b) Verify the payload twice: at the fetch and after the copy. (c) Reword the receipt's evidence line so each result names its command and result, or an evidence path. | Second runs: 0 diff in 5 receipts. Payload re-hashes: 0 drift in 3 passes. Each is implied by a check that stays ([Challenge C1, C4, C5](4_challenge.md)). They exceed §3 claim 5's condition, so they go through A3. |
| D4 | Kept: project checks after the update, revalidation before preserved writes, migration obligations, re-observation at equal version, the one mandated pin recheck, and the final message. | Each caught a recorded condition, answers a recorded failure, or costs little against DoF 5 (Gather G5; Challenge C3). |
| D5 | Staging exposure, recommended without any new authority: U2. Keep the clone-then-delete order, and before sealing confirm `git ls-files -- .tfw/.upstream` is empty; disclose any entry. About 15 words, read-only. U1, order alone, is the minimal alternative. | 0 commits for four staging names in 20 repositories. A concurrent session appears twice; one cleanup was blocked (Gather G7; Extract E3; Challenge C6). |
| D6 | B2, a permanent exclude line, and U3, a direct clone at `.tfw/.upstream/`, are owner-dependent options, kept apart below. | Update authority does not cover a standing local setting outside `.tfw/` (Challenge C6). |
| D7 | Eliminated: B1, a temporary exclude line; narrowing project checks by judgment; P2 with a saved list. | PowerShell 5.1's usual removal rewrites the whole exclude file with CRLF. Narrowing checks meets DoF 5. A saved list's encoding depends on the shell (Challenge C4, C6). |
| D8 | S3 with a tag costs no time. The TS may use one sequence for tags and SHAs (≈ 70 words), or the clone form plus S3 for untagged commits (≈ 50). S3 passes `-c core.attributesFile=` on its `checkout`. | GitHub, one run each: S3 3.96 s and S2 3.94 s, against S1's 4.8–5.0 s. PowerShell 5.1 drops the empty argument in `git config … ""` (Gather G8; Extract E5). |
| D9 | A release's step removals shorten the very first update to it. Its light fetch helps only from the update after that. | After pinning, Steps 1–4 follow the pinned `update.md`. Two receipts state they "followed [it] from Step 1" (Extract E1; Challenge C7). |
| D10 | S2 is now observed on GitHub: 487,615 B (0.47 MiB), 88/88 byte-equal. | This completes iteration 1's A1 comparison, which lacked it (Gather G8). |

## H2 — where update time goes, in three separate kinds

| Kind | Values | Source |
|---|---|---|
| **Measured** | Old 114 MiB download ≈ 41 s on this connection; light fetch: S1 4.8–8.2 s, S2 3.94 s, S3 with a tag 3.96 s. R1's 3.7.1 update: 14.5 min from its first network command to the seal — pin and fetch ≈ 1 min, apply ≈ 10, project checks ≈ 2, cleanup and seal ≈ 1. R6's update: 24.7 min from start to seal. Six more apply windows: 2.5–13 min. Project checks where timed: 37 s to ≈ 2 min. One before-run: 12.11 s. | iteration 1 G2; Gather G3, G8; receipt clocks |
| **Computed or inferred** | *Computed:* the old download is ≤ 5% of R1's 3.7.1 update; a light fetch is under 1%. This joins iteration 1's download time with R1's timeline, both on the same connection. *Inferred from bytes, not observed:* the old download would be ≈ 10% of an update at 10 Mbit/s and ≈ 37% at 2 Mbit/s. It would outweigh the rest only below ≈ 1.2 Mbit/s, or ≈ 0.7 Mbit/s against R6's 24.7 min. | Gather G3 |
| **Unmeasured** | The time of each repeated step: payload re-hash, second sync, tag re-lists. Also reading, receipt writing, owner-answer waits, and everything before an update's first network command. | no receipt keeps clocks per step |

**Verdict on H2.** Its first claim holds on this connection. Its second claim, that the procedure's
*repeated* steps dominate, is not established. It is therefore also not established that §3 claim 5's
condition for bounded removals is met.

## Open Questions

| # | Question | Status | Answer |
|---|---|---|---|
| Q1 | May bounded removals rest on redundancy with no protection lost, rather than on shown dominance? | Owner, A3 | Proposed below. |
| Q2 | Should each receiver get a permanent `.tfw/.upstream/` exclude line, enabling U3? | Owner, outside update authority | Options below; not recommended. |
| Q3 | What does each repeated step cost in time? | For the Executor's trial update (DoD 7) | Unmeasured here. |
| Q4 | Does the download share hold on slower links? | Inferred | Every timed update ran on one connection. |
| Q5 | Do receivers' own ignore files cover staging? | Not inspected (outside the approvals) | One receipt says its receiver ignores `.tfw/.upstream/`. |
| Q6 | Why did S3 by SHA take 15.2 s once in iteration 1? | Unexplained | Single runs; the tag form took 3.96 s. |
| Q7 | One receipt stored its Russian text as `?`. | Flagged; outside this task | A lossy write of an immutable record (Gather G9). |
| Q8 | How do other shells remove a line from an exclude file? | Unobserved | Only Git Bash (byte-preserving) and PowerShell 5.1 (rewrites) were tried. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|---|---|---|---|
| H1 | One Git method is light and byte-identical | ✅ supported with conditions (iteration 1) | unchanged; S2 and S3 with a tag now observed on GitHub | S2 0.47 MiB, 88/88; S3 0.58 MiB, 95/95 (Gather G8) |
| H2 | Download is a minority and the repeated steps dominate | open — iteration 2 | ⚖️ bounded: first claim supported on this connection; second not established | the H2 section above |
| H3 | The latest-release check is short and fails fast | ⚠️ (iteration 1) | unchanged | — |
| H4 | Install needs only `.tfw/` and `editions/` | ✅ (iteration 1) | unchanged | — |

## HL Update Recommendations

The Researcher classifies; the Coordinator applies the refinements and routes the proposal. Nothing here
edits the HL.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|---|---|
| R1 | §2 | "Update duration": replace with the receipt clocks. R1's 3.7.1 update took 14.5 min from its first network command (pin and fetch ≈ 1, apply ≈ 10, checks ≈ 2, seal ≈ 1). R6's took 24.7 min. Apply windows run 2.5–13 min. The receipts are 17 distinct ones in 8 repositories, 548–3,711 words each against the template's 527. | Gather G2, G3, G6 |
| R2 | §2 | "Receivers lag silently": the 24 receivers are Git working trees of 20 distinct repositories; 4 more folders outside Git also hold `.tfw/VERSION`. | Gather G2 |
| R3 | §9 | Staging row: 0 commits for four staging names in 20 repositories; a concurrent session recorded twice; one cleanup blocked; mitigation U2 (D5). First row: add that step removals apply already on that first update (D9). Removals row: the conditions of D3. New row: "update duration is not attributed per step; removals save an unmeasured share", mitigation DoD 7's measured cost in the Executor's trial. New row: "a receipt written in a non-UTF-8 code page loses its text (observed once)", outside this task. | Gather G7, G9; Challenge C6, C7 |
| R4 | §10 | H2 status: "⚖️ bounded (iteration 2): the download is a minority on this connection (measured and computed); the repeated steps' share is unmeasured; the false case appears only below ≈ 0.7–1.2 Mbit/s (inferred)". Critical challenge: confirmed — removing 113 MiB saves ≈ 35 s of a ≈ 14.5-min update here. | the H2 section |
| R5 | §8 | New row: U3 needs an owner decision for a permanent local exclude line in each receiver; U1 and U2 need nothing new. | Challenge C6 |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|---|---|---|---|---|
| A3 | §3 claim 5 | `EXTEND` | Keep "If research shows that the procedure's own repeated steps dominate update time, bounded removal of those steps is in scope". Add a second trigger: a repeated step may also be removed or narrowed when research shows it found nothing across the recorded updates and a check that stays implies it. The same "without weakening preservation …" limit applies. | Receipts: second sync 0 diff in 5; payload re-hash 0 drift in 3 passes; no project check failed because of an update in 17 (Gather G4, G5). Challenge C1, C4 and C5 show each candidate implied by a kept check under stated conditions. H2's second claim is unmeasured, so the frozen trigger cannot be met from existing evidence. | The savings are unmeasured and probably small, so the owner's pain about duration may largely remain. A redundancy argument can miss a hidden role; the stated conditions and HL §9's independent review of each removal mitigate that. DoD 7 still needs each removal's measured cost in the RF. | **Keep claim 5 as it is:** no procedure change in this task (DoD 7's no-change branch); measure per step in the Executor's trial; open a later task if a step dominates. **A third research iteration** with a timed trial update of a scratch receiver copy, to test dominance as the frozen text requires (`max_iterations: 3`); iteration 2's focus excluded trial updates. **Call the removals refinements under principle 5:** rejected. Principle 5 offsets additions and creates no removal scope, and using it would let the classifier benefit from the label. |

§4 deliverable 5 ("Only if research supports it") would read as satisfied under A3 by the same evidence.
Without A3, the U2 staging recommendation (D5) still stands, because it removes no step. Its ≈ 15
read-only words must still meet principle 5 by replacing vaguer text, for example Step 4's "only when
safe".

## Owner-dependent staging options — outside the recommendation

Per gate answer 7138, these are recorded apart from the recommendation (D5), each with the authority it
needs.

| Option | What it does | Evidence | Authority it needs |
|---|---|---|---|
| **B2 — a permanent exclude line** | Appends `.tfw/.upstream/` once to the receiver's `info/exclude`, found with `git rev-parse --git-path info/exclude`, and keeps it. | `git add -A` stages nothing and makes no gitlink; staging survives other sessions' `git stash -u` and `git clean -fd`; one line covers every worktree. The append works from Git Bash and from PowerShell 5.1: Git matches the CRLF line (Extract E3; Challenge C6). | **Not covered by update authority.** It is a standing local setting outside `.tfw/`, and `update.md` Step 2 excludes "new project decisions". It needs an owner decision for each receiver, for example as the preview's one material question, or a TS-level owner approval that updates may append it. |
| **U3 — clone directly at `.tfw/.upstream/`** (with B2) | The clone itself becomes the staging. The payload sits at `.tfw/.upstream/.tfw/`, the path the pinned guides name. The end-state check uses the clone's own tree; cleanup deletes `.tfw/.upstream/`. | 95/95 byte-equal at the staging path; no gitlink; a nested repository even survives `git clean -fdx` without a second `-f`. It removes the copy step, the clone-deletion ordering and the shell-specific copy command (Challenge C6). | **The same as B2.** Without the line, the direct clone becomes a gitlink under `git add -A` (iteration 1 E4), so U3 exists only if B2 is approved. |

B1, a temporary line removed at cleanup, is not offered. Its usual removal in PowerShell 5.1 rewrote the
receiver's whole exclude file with CRLF.

## Fact Candidates

**No fact candidates.** No owner message reached this iteration; the Coordinator's rulings are in the
journal. Every observation here can be reproduced by re-running the recorded commands or reading the same
receipts, so none passes the Human-Only Test.

## Strategic Insights (Research)

**No strategic insights.** The owner took no part in this iteration's briefings.

## Findings Map

```text
WHERE AN UPDATE'S TIME GOES (R1's 3.7.1 update, 14.5 min from its first network command)
  pin + fetch ≈1 min ── the 114 MiB download ≈41 s (measured); light ≈4 s (measured)
  apply ≈10 min ──────── copy, config merge, preservation, adapters, re-hashes, second sync ...
                         per-step shares: UNMEASURED
  project checks ≈2 min  (measured)
  cleanup + seal ≈1 min
  before the first network command: UNRECORDED

WHAT EACH REPEATED STEP CAUGHT (17 receipts)        CHANGE                   AUTHORITY
  second adapter sync     0 diff in 5              drop "or second-run diff"  A3 (owner)
  payload re-hash         0 drift in 3 passes      two passes, not three      A3 (owner)
  receipt evidence line   pasted output            command/result or path     A3 (owner)
  project checks (after)  only pre-existing fails  keep (DoF 5)               —
  revalidation, migration obligations,
  re-observation at equal version                  keep: each caught
                                                   or answers a recorded      —
                                                   failure

STAGING EXPOSURE (0 incidents for 4 names in 20 repositories)
  recommended ─ U2: clone, copy, check, delete + read-only pre-seal `git ls-files`    no new authority
  minimal ───── U1: order only                                                          no new authority
  owner only ── B2: permanent exclude line ──► enables U3: clone IS .tfw/.upstream/,    owner decision
                    no copy step, no shell-specific copy
  eliminated ── B1: temporary line (PowerShell 5.1 removal rewrites the exclude file)

WHEN BENEFITS ARRIVE
  release N+1 ──► first update to it: Steps 1-4 follow the pinned text  → removals apply
                  its Step 0 fetch still follows the installed text      → light fetch waits one update
```

## Iteration Status

- **Iteration:** 2 of 2 minimum / 3 maximum.
- **Hypotheses tested:** H2, bounded. The first claim is supported on this connection; the second is not
  established.
- **Hypotheses deferred:** none. H1, H3 and H4 were settled in iteration 1; S2 and S3 with a tag were
  added to H1 on GitHub.
- **Gaps discovered:**
  - No receipt keeps clocks per step.
  - §3 claim 5's trigger cannot be met from existing evidence (A3).
  - The receivers' own ignore files are not inspected.
  - One receipt lost its text to a lossy encoding.
  - All timed updates ran on one connection.
- **Superseded decisions:**
  - The receipt clocks supersede the Briefing inventory's "one timed receipt", which searched only for
    duration words (Gather G3).
  - Extract's P2 as a general option survives only inside U3.
  - Extract's "narrow the after-run checks" is eliminated (Challenge C3).
  - B1 is eliminated.
  - Iteration 1's D4 layout (clone in `.tfw/.upstream/.clone`, copy, delete) stands for U1 and U2; U3
    would replace it only if the owner approves B2.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|---|---|---|
| 1 | A3 | Without it, no redundancy-based removal is in scope | The Coordinator routes it to the owner; if declined, see thread 3. |
| 2 | B2 and U3 | The only way to remove the copy step and close every staging window | An owner decision; the TS carries U2 otherwise. |
| 3 | Per-step time | DoD 7 needs each removal's measured cost; claim 5's frozen trigger needs dominance | The Executor's trial update times each step. Or, only if the owner declines A3 and still wants removals, a third iteration with a timed scratch trial update. |
| 4 | The receipt encoding loss | Immutable records can lose content | Flagged to the owner; outside this task. |

### Recommendation

- [x] **SUFFICIENT** — proceed to `/tfw-plan`. The research questions are answered as far as existing
  evidence allows. What remains are owner decisions (A1 and A2 from iteration 1; A3; B2/U3; the flagged
  upstream-state question) and the Executor's measurements.
- [ ] **MORE NEEDED** — only if the owner declines A3 but wants removals backed by measured dominance:
  a third iteration with a timed trial update.
- [ ] **BLOCKED**

## Conclusion

Iteration 2 read every update receipt on this machine and found more clock data than planned. The picture
is clear:
- The download is a minority of update time on this connection. The old 114 MiB is about 41 s of an
  update that runs 14.5 minutes from its first network command, so the light fetch alone will not make
  updates feel fast.
- The time sits in the procedure, but receipts do not attribute it to steps. The repeated steps H2
  suspected never found anything, and each is implied by a check that stays.
- The checks that did catch real conditions were the ones that protect receiver state, and those stay.

Staging never entered a receiver's history, under any of the four names agents used. A read-only check
before sealing guards that without new authority. Only a permanent exclude line, which is the owner's to
approve, removes the copy step altogether. Two receipts show that step removals reach receivers one update
before the light fetch does.

The main contract finding is A3. The frozen trigger for removals requires shown dominance, and existing
evidence cannot show it. The owner either extends the trigger to cover redundancy, or keeps the procedure
unchanged in this task.

Self-critique:
- The Briefing's inventory missed the receipt clocks because it searched only for duration words.
- The staging tests ran only in scratch receivers.
- Only two shells were tried for removing an exclude line.
- The GitHub runs were single samples.
- Iteration 1's 15.2 s for S3 by SHA stays unexplained.

### Material handover at this return

- **Producer / recipient:** Researcher `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher`
  to the parent Coordinator `claude-code:session:local_e821cd09-6696-482b-bd88-ca93dba929a2`.
- **Source / epoch:**
  - 17 distinct receipts and the Git history of 24 receiver working trees (20 repositories), as of
    2026-09-29;
  - `v3.7.1` from GitHub (two runs) and from this repository as a local server;
  - Git 2.42.0 in Git Bash and in Windows PowerShell 5.1.
- **Inspected scope:**
  - Stage files 1–4; `status.md`; the journal through gate answer 7138; the HL at `526da86d`.
  - `update.md`, the receipt and briefing templates, and `KNOWLEDGE.md` D11 and D70.
  - CHANGELOG searches; migration-guide word counts; one field-report line.
  - Git documentation for gitignore, git-add, git-rev-parse, git-clean and git-stash.
  - Scratch trials.

  No receiver, remote or GitHub state changed. Receiver names, paths and commit text stay out of these
  files.
- **Material:** D1–D10, the three-kind H2 table, A3, the owner-dependent options and R1–R5.
- **Uncertainty:** Q3–Q8.
- **Continuation:** the Coordinator reviews via `/tfw-plan`, applies R1–R5, transcribes A3 into §12 as
  `PROPOSED` for the owner, and raises B2/U3 as an owner decision.
- **Unresolved owner decisions:** A1, A2, A3, B2/U3, and the flagged upstream-state question.

---

*RES — TFW_20260929-003444_LFD: Lightweight Framework Delivery | 2026-09-29*
