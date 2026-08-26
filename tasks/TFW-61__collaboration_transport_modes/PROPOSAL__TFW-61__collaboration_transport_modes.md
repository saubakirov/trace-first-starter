# PROPOSAL — TFW-61: Collaboration Transport Modes — Git or file synchronization, chosen once

> **Date**: 2026-08-26
> **Author**: Coordinator (Claude Code)
> **Status**: 📋 PROPOSAL — not chartered, no HL
> **Origin**: [TFW-60](../TFW-60__conflict_resistant_shared_workspace/HL-TFW-60__conflict_resistant_shared_workspace.md) amendments A2 and A3, owner-approved 2026-08-26
> **Sequenced after**: TFW-60 Phase A. Phase A ships the mode-agnostic core; this task ships the transport around it.

---

## 1. Why this task exists

TFW-60's frozen Vision originally promised both at once: a project folder synchronized through Google
Drive *and* Git as durable provenance, on the same tree, with several participants. Research iteration 3
established from primary sources that this configuration is not supported by Git itself. Amendment A2
replaced simultaneity with a declared project mode; amendment A3 moved every mode-specific rule out of
Phase A.

Those rules now have no owner. This proposal is that owner.

## 2. Measured, not asserted

| # | Measurement | Source | Result |
|---|---|---|---|
| 1 | Does Git permit a cloud-synced repository? | [Git FAQ](https://git-scm.com/docs/gitfaq) | *"It is important **not to use a cloud syncing service to sync any portion of a Git repository**"* — named failures: missing objects, changed or added files, broken refs |
| 2 | Does Git permit a shared working tree? | same | Safe *"only… if it will only be used by **a single user** across all machines"* — which a multi-participant team is not |
| 3 | Does Drive write into dot-directories? | Live folder `innoforce_starter_v1.4`, iteration 3 | `desktop.ini` present in **18 of 18** directories, dot-directories included; a nested subfolder cannot be excluded |
| 4 | Can `.gitignore` keep `.git` out of Drive? | Drive documentation | No. `.gitignore` governs Git, not the sync client |
| 5 | Does the draft's G-B topology survive measurement 2? | TFW-60 Phase A draft, superseded | No. Pinning `.git` outside the tree addresses object corruption and leaves the shared-working-tree prohibition untouched |
| 6 | Was a non-technical participant ever observed? | TFW-60 research iterations 1, 2, 3 | **Never.** Three iterations, zero observations |
| 7 | Was a real sync provider ever exercised for offline fork and reconnect? | same | **Never.** Provider artifacts were observed; offline divergence, conflict-copy naming and reconciliation were not |
| 8 | Does a shipped edition already run in a synchronized folder? | `innoforce_starter_v1.4` | Yes — and its lifecycle hooks were removed in v1.4 because *"on a real large folder Stop did not fit its own timeout"*. Untested transport machinery has already failed here once |

**The shape of the problem.** Git documents the combined configuration as unsupported. So the question is
not *how to make both work on one tree* but *which one a project runs on*, and what each mode owes the
people using it.

## 3. What this task owns

1. **The mode as a declared choice.** A configuration value set at initialization, verified by
   `/tfw-config`, with a defined answer for a project that later wants to switch.
2. **Git mode rules.** Task-owned explicit-path staging, no shared-index ambiguity, retained freeze
   baselines and commit attribution. Closes the remaining part of TD-144 and TD-178.
3. **File-sync mode rules.** Operating and recovery behaviour assuming only ordinary independent-file
   synchronization: conflict copies preserved rather than resolved by timestamp, offline divergence
   reconciled explicitly, no cross-file transaction assumed, no vendor API and no always-on service.
4. **Versioning in file-sync mode.** The provider's per-file version history replaces commit history.
   What that does and does not guarantee must be stated rather than assumed.
5. **The two observations TFW-60 could not make.** A genuinely non-technical participant browsing and
   acting without coaching, and a real provider client exercising offline fork, reconnect, conflict
   artifacts and reconciliation with initial and final bytes recorded.
6. **The publish arrangement, if it survives scrutiny.** A team works in a synchronized folder while one
   person maintains a separate Git clone and lands content into it periodically. This is two folders and
   an explicit step, not a combined mode. It is the plausible answer for a mixed engineer / non-engineer
   team and it has never been tested.

## 4. What it deliberately does not own

- task-local state, journal, participant profiles, index generation, identifier allocation or migration
  of the legacy corpus — all shipped by TFW-60 Phase A and identical in both modes;
- task-local debt and knowledge staging — TFW-60 Phases B and C;
- any requirement for a daemon, database, lock server, vendor API or Git merge driver;
- a third transport.

## 5. The standing risk this task must discharge

TFW-60 amendment A2 records it explicitly: **this repository runs in Git mode, so it never exercises
file-sync mode on itself.** Measurement 8 above is what that looks like when it goes wrong — machinery
shipped into a synchronized folder without being run in one, then withdrawn.

The mitigation is not a fixture. File-sync mode must be exercised on a live project in a real
synchronized folder before it is called released. `innoforce_starter_v1.4` is the candidate environment
and is reachable today.

## 6. Open questions for the HL

- Is the mode a project-level property, or can one project carry a Git repository and a synchronized
  working area with a declared boundary between them?
- What does switching modes mean for an existing corpus, and is switching supported at all?
- In file-sync mode, what replaces the freeze baseline that Git commit subjects currently provide? A
  frozen contract that cannot be diffed is not frozen (`conventions.md` §3 rule 13), and this is the one
  place where dropping Git costs something the journal does not obviously replace.
- Does the publish arrangement in §3.6 belong to this task, or is it a fourth thing?
- Which provider clients and versions are supported, and what happens on the ones that are not?

## 7. Sequencing

| Order | Task | Why |
|---|---|---|
| 1 | TFW-60 Phase A | The core both modes share must exist first |
| 2 | **TFW-61** (this) | Transport rules and the two outstanding observations |
| 3 | TFW-60 Phases B and C | Debt and knowledge locality, unaffected by transport |
| — | TFW-54, TFW-57 | Already sequenced after TFW-60 |

The third open question above is the one that could reshape this proposal: if file-sync mode has no
credible substitute for the contract baseline, then Git may be less optional than A2 assumes, and the
finding belongs in TFW-60 §12 rather than here.
