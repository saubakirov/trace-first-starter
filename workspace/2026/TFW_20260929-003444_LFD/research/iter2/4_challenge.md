# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260929-003444_LFD](../../HL-TFW_20260929-003444_LFD.md)
> Goal: Installing or updating TFW moves only the framework, about one megabyte, by one written method, and a newer release shows in one line when new work starts; the owner decides whether and when to update.
> Producer unit: `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher` · mode focused · single pass
> Continuation source: [gate answer 0e63](../../journal/20260929-033641__gate_answer__0e63.md) in `1e9553d9722470a090de94138276829a003e8e52`

New evidence in this stage:
- **Scratch receivers** (fresh repositories in scratch, local server only, no real receiver):
  - a clone made directly at `.tfw/.upstream/` with an exclude line, in Git Bash;
  - the exclude line's append and removal in Windows PowerShell 5.1;
  - one redirection test.
- **Two documentation sources.**

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D8 staging | no exclude | staging layout | clone directly at `.tfw/.upstream/` (C2) | `git add -A` records a gitlink (iteration 1 E4; E3 test) |
| D8 staging | B1, a line removed at cleanup | shell | Windows PowerShell 5.1 | the usual removal rewrites the whole exclude file with CRLF, so it is not byte-preserving (C6) |
| D8 staging | B2, a permanent line | authority | update authority alone | a standing local setting outside `.tfw/`, beyond "diagnostic staging" (C6) |
| D5 verification | P2, end state against the pinned tree | D8 staging | clone deleted right after the copy | the pinned blob list must outlive the clone: either a saved file, whose encoding depends on the shell, or a kept clone (C4) |
| D6 project checks | narrowed to "not affected" by judgment | DoF 5 | — | a judgment can skip a check that protects the receiver, to save 37 s to about 2 min (C3) |
| Second adapter sync | removed | block counting | any marker other than the template's exact pair | a mis-written marker would count as one block and be duplicated at the next update (C1) |
| S3 `init` form | `git config core.attributesFile ""` | shell | PowerShell 5.1 | the empty argument is dropped (Gather G8) |
| Any removal | — | pinned guides | their obligations | the guides are immutable and cannot be waived (Extract E6) |

**Surviving configurations:**

| Config | D5 verification | D6 project checks | D7 receipt | D8 staging | Second sync | Notes |
|--------|-----------------|-------------------|------------|------------|-------------|-------|
| U1 (P1 + A) | once at the fetch (in the clone), once after the copy (installed against staging) | after only, as the text says | evidence line reworded: command and result, or an evidence path | clone in `.tfw/.upstream/.clone`, deleted after the copy check | removed | needs no authority question; the payload copy is exposed during the apply |
| U2 (U1 + D) | as U1 | as U1 | as U1 | as U1, plus a check before sealing that `git ls-files -- .tfw/.upstream` is empty | removed | detects staged staging before the receipt is sealed; ≈ 15 words |
| U3 **N** (C2 + B2 + P2) | the fetch check, then installed files against the kept clone's own tree | as U1 | as U1 | the clone *is* `.tfw/.upstream/`, with a permanent exclude line | removed | no copy step, no clone-deletion ordering, no shell-specific copy command; the line needs an owner decision |

Eliminated:
- **B1** (a temporary line) in any configuration that must run in PowerShell 5.1.
- **P2 with a saved list.**
- **Narrowing project checks by judgment.**

**Unexpected survivors:**
- **U3.** Iteration 1 set C2 aside only because `git add -A` records the nested clone. A permanent exclude
  line removes that reason. It also removes the copy step, the "delete the clone right after the copy"
  ordering and the shell-specific copy command (`cp -r` against `Copy-Item`). And it lets the end-state
  check use the clone's own tree until cleanup. The whole cost is one line outside `.tfw/`, which only
  the owner can approve.
- **Dropping the second sync.** It survives even though a real failure class sits behind it,
  because the text's own "one marker-bounded block" already catches that class (C1).

## Findings

### C1 — Removing the second adapter sync

- **What only a second run can catch.** Suppose the sync writes a marker that its own detection does not
  recognize. The first run then leaves one block, a count by a loose pattern passes, and the next run
  appends a second block.
- **That class has happened.** The CHANGELOG records a related one: "Appending to a file that already
  carries an unmarked hand-written TFW section produced two sections that disagreed."
- **The next update would still refuse it.** `update.md` rejects "duplicate blocks", so the failure is
  delayed by one update, not silent.
- **Condition for removal.** The block count uses the template's exact begin and end markers. The text
  already says "one marker-bounded block" and "Reject … duplicate blocks, drift".
- **Evidence.** 0 diff in 5 receipts (4 runs, 1 assertion without a run). No recorded rationale.
- **Verdict:** survives. Drop "or second-run diff" (−3 words).

### C2 — The before-run habit for project checks

- **The counter-case.** A check that reads changed paths fails after the update. Reasoning cannot then
  show the failure was pre-existing, and a before-run could.
- **Observed practice.** Both pre-existing failures were labelled by reasoning, because neither check read
  a changed path. The before-run cost 12.11 s.
- **The text.** It neither requires nor forbids a before-run, so there is nothing to remove.
- **Verdict:** no text change. Forbidding a cheap, occasionally useful habit would add words for no
  saving (principle 5).

### C3 — Narrowing the after-run project checks

- **The counter-case.** A receiver's lint, documentation build or tests read `.tfw/`, adapter files or the
  config. This was not observed in 17 receipts, but it is plausible, and exactly what the checks exist to
  catch.
- **The trade.** Skipping by judgment saves 37 s to about 2 min and risks DoF 5 ("a verification step that
  protects receiver state is removed for speed").
- **Verdict:** eliminated. The after-run stays as the text says. R1 3.6.1's reasoned deferral remains an
  agent's disclosed choice, not a rule.

### C4 — How often the payload is verified: P1 against P2

- **P1's gap.** A change to staging between the fetch check and the copy would pass, because installed
  equals staging. No such change appears anywhere: 0 drift in 3 passes, and no staging interference in
  17 receipts. The concurrent housekeeping commands that could touch untracked staging (`git stash -u`,
  `git clean -fd`) move or delete it, which fails loudly rather than silently.
- **P2's costs.** P2 needs the pinned blob list after the clone is gone.
  - A saved file depends on the shell. Redirection in this environment's PowerShell wrote UTF-8 with a
    byte-order mark (EF BB BF). Stock Windows PowerShell 5.1 writes UTF-16 by default (general
    knowledge, not observed here).
  - The alternative is to keep the clone, which reopens the gitlink window unless an exclude line exists.
- **Verdict:**
  - P1 survives as the default: two passes instead of today's three, in proportion to a thin, unobserved
    risk (NS2 principle 7).
  - P2 survives only inside U3, where the kept clone makes it free.

### C5 — Rewording the receipt's evidence line

- **The counter-case.** The line exists so a receipt cannot claim a check without resolvable proof
  ("screenshots or summaries without a resolving path do not prove the receiver state").
- **The condition.** A shorter form must keep that property. Asking for "the command and its result, or
  an evidence path, per check; no pasted output" keeps it, and loses nothing that a command line and its
  result would give.
- **R8's lesson.** Its receipt lost its text altogether, and neither form would have saved it.
- **The saving.** Unmeasured: receipts run up to 7× the template's length, and writing time is not
  recorded.
- **Verdict:** survives, with the condition above.

### C6 — Staging controls, with and without update authority

- **What `update.md` grants:**
  - the role lock: "Apply only authorized framework/config/adapter migrations and one project-owned
    receipt";
  - Step 2: authority "covers coherent framework-owned changes and prescribed compatible migration, not
    new project decisions or external effects";
  - Step 3: "Diagnostic staging/preservation is a disclosed write."
- **Observed, in scratch receivers:**
  - **Git Bash, with a clone at `.tfw/.upstream/` and the line in `info/exclude`:** status was empty,
    `git add -A` staged nothing and made no gitlink, and staging survived `git stash -u` and `git clean
    -fd`. The payload at `.tfw/.upstream/.tfw/` was 95/95 byte-equal. Removing the line with
    `grep -v -x -F` restored the file byte for byte.
  - **PowerShell 5.1:** `Add-Content` wrote the line with CRLF, and Git still matched it. The usual
    removal, `Get-Content | Where-Object | Set-Content`, removed the pattern but rewrote all 6 lines with
    CRLF, so the file was no longer byte-equal.
- **Documented:**
  - `git clean` "will refuse to modify untracked nested git repositories … unless a second -f is given",
    and removes ignored files only with `-x`.
  - `git stash -u` stashes untracked files but not ignored ones; only `-a` includes ignored files.

| Control | Under update authority alone | With an owner decision | Verdict |
|---|---|---|---|
| A. Order only | fits: no extra write | — | survives (U1) |
| D. Pre-seal check | fits: read-only | — | survives (U2) |
| B1. Temporary line | fits only if read as part of the disclosed staging write; its removal is not byte-preserving in PowerShell 5.1 | same removal problem | eliminated for one written method |
| B2. Permanent line | does not fit: a standing local setting and a new project decision | fits once approved per receiver | survives only with the owner (U3) |
| C. Ignore line written by init | outside this task's touch set; a project file | a separate decision | set aside |

**The evidence weight.**
- **No incident** for any staging name in 20 repositories.
- **Exposure is a window:** seconds for a clone, the apply for the payload copy, indefinitely after a
  blocked cleanup.
- **The risky condition occurs:** a concurrent session appears twice in the receipts.
- **What B adds beyond `git add -A`:** protection against other sessions' `stash -u` and `clean -fd`.

### C7 — The H2 answer and the one-update lead, attacked

- **One connection only.** Every timed update ran on this machine's connection, so there is no
  independent network evidence. The slower-link shares stay inferred.
- **The one-update lead is observed practice, not only inference.** Two receipts state that the pinned
  target's `update.md` was followed from Step 1: R5 "followed from Step 1 onward" and R3 "followed from
  Step 1". So a release's step removals apply on the first update to it; its light fetch applies from the
  next.
- **What would make the removal list wrong, and whether it was found:**

  | A finding that would break a removal | Found? |
  |---|---|
  | a second sync that caught a duplicate | none |
  | a before-run that proved pre-existence where reasoning could not | none |
  | an after-check that caught an update-caused failure | none, but the check is kept regardless (C3) |
  | a change to staging between steps | none |

### C8 — The bounded list the evidence supports

| # | Change | Words | Protection kept by |
|---|---|---:|---|
| 1 | Drop "or second-run diff" | −3 | "one marker-bounded block" and "duplicate blocks, drift" |
| 2 | Verify the payload twice: at the fetch and after the copy | ≈ 0–5 | the raw-byte check against the pinned tree at the fetch |
| 3 | Reword the receipt's evidence line | ≈ 0 | every result still names its command or evidence path |
| 4 | Staging: order only (U1), plus a pre-seal check (U2), or C2 with an owner-approved exclude line (U3) | 0 / ≈ 15 / ≈ +15 with the copy step removed | Git's ignore rules (U3) or detection before the seal (U2) |

**Kept:**
- project checks after the update;
- revalidation before preserved writes;
- migration obligations;
- re-observation at equal version;
- the one mandated pin recheck;
- the final message.

Each item still needs its measured cost in the RF (DoD 7); the Executor's DoD 1 trial is where that can be
measured.

### External sources

- Git, [git-clean](https://git-scm.com/docs/git-clean): nested repositories need a second `-f`; ignored
  files are removed only with `-x`.
- Git, [git-stash](https://git-scm.com/docs/git-stash): `-u` stashes untracked files; `-a` also ignored
  files.

Web actions: 2 (soft limit 5). Project files read: none new. Evidence items: three scratch tests.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Dropping the second sync survives, provided blocks are counted by the template's exact markers | — |
| Project checks stay; narrowing them by judgment conflicts with DoF 5; the before-run needs no text | — |
| P1 (two passes) is the proportional default; P2 is free only with a kept clone | — |
| The receipt's evidence line can be shortened if every result still names a command or path | writing time unmeasured |
| Staging: A and A+D need no authority; B1 fails byte-preserving removal in PowerShell 5.1; B2 needs the owner; C2 with B2 (U3) removes the copy step | the owner's view on a permanent local exclude line |
| The one-update lead of removals over the light fetch is confirmed by two receipts | — |
| H2 is bounded to one connection | slower links inferred |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed? (each removal attacked with its counter-case; thread 2 settled as three survivors with their authority needs; H2 bounded)
- [x] Pairwise incompatibility checked? Surviving configurations listed?

**Stage decisions.**
1. **The bounded removal list in C8 is what the evidence supports.** Items 1–3 need no authority beyond
   today's.
2. **Eliminated:**
   - narrowing project checks by judgment (DoF 5);
   - B1 as a one-method control (PowerShell 5.1 removal);
   - P2 with a saved list.
3. **U3 goes to RES as an owner-dependent option,** not a recommendation: C2 staging with a permanent
   exclude line.

**Metacognitive note.**
- **New:**
  - C2 becomes viable once the line exists, and removes the copy step.
  - PowerShell 5.1's removal rewrites the exclude file.
  - Excluded staging survives other sessions' `stash -u` and `clean -fd`.
  - Two receipts confirm the one-update lead.
- **Confirmed:** keeping project checks and state-protection checks.

**Knowledge handover.**
- **Producer:** as in the header.
- **Source and epoch:** scratch tests on Git 2.42.0 (Git Bash and Windows PowerShell 5.1) against the local
  server at `v3.7.1`; receivers' receipts as of 2026-09-29.
- **Material:** C1–C8 and the survivors.
- **Uncertainty:** the Remaining column.
- **Continuation:** synthesis (RES), after the Coordinator's gate.

Stage complete: YES
→ User decision: ___
