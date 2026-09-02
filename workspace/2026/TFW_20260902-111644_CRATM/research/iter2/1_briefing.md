# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> Goal: a project declares who its participants are, a coordinator runs the task with a team of them in isolated trees under a contract it cannot move.

> **Iteration 2 of a parallel pair, not a successor.** `research/iterations.yaml` rules that the two
> iterations are independent: each tool measures its own side, and iteration 2 does **not** target
> iteration 1's gaps. There is therefore **no predecessor RES to build on** — `research/iter1/RES.md`
> does not exist at the time of this briefing. Iteration 1 (Codex measuring Codex) started
> concurrently in this same working tree at 00:03 on 2026-09-03 and was at its Gather stage while this
> file was written. Its partial findings are deliberately **not read**: the owner assigned the sides by
> capability, and reading a sibling's in-flight notes would contaminate the one thing this pair buys —
> two independent measurements.
>
> **Gates waived by the owner** for this iteration ("no questions to me", 2026-09-03). Every stage file
> is still written before its checkpoint, so the trace is unchanged; what is removed is the wait.

## Research Plan

**Gather — measure, do not reason about, this session's own capabilities**
- Enumerate peer Claude sessions; record count, age, project, and whether one answers a delegation-shaped message. `knowledge/constraint.md` F11 ("peers are Codex-only") is the claim under test.
- Establish whether a Claude participant can be *created* on demand, as distinct from *addressed*: the peer list, the in-process subagent, and the headless `claude -p` session are three different things and must not be reported as one.
- Run the crossing in both directions with real invocations: this session calling Codex, and the command a Codex session would use to call Claude. Record latency, token cost, and every failure verbatim — DoF 10 makes a conclusions-only report a failure of this task.
- Census the worktrees on this machine, including what Codex leaves behind after a run ends.
- Count the journal corpus by identity field, and run the shipped validator against a synthetic event carrying a `writer` key. H9 is decided by that validator, not by the template's prose.
- Decompose into dimensions: delegation channel per vendor, return path, writer-identity carrier, worktree occupancy.

**Extract — cross-reference the dimensions into configurations**
- Build the configuration space over the vendor channels, the return path and the writer carrier; the interesting combinations are the mixed ones nobody proposed in the HL.
- Compare the closed schemas (`status.md`, journal event) against the open one (`team/{handle}.md`) — the migration cost of a new field is a property of the carrier, and the HL treats all three as markup.
- Read the Assisted edition's own participant schema as field evidence, never as authority (S4: a shared noun does not make two schemas one).

**Challenge — attack the survivors**
- Pairwise: which channel cannot coexist with which return path, which writer carrier cannot coexist with the immutable corpus.
- H8 against AFD's real corpus: group every REVIEW file into arcs, count rounds, and check whether the reviewer changed between rounds. If no arc ever changed reviewer, H8 has no control case and must be said so.
- H2 against TFW-45's actual vocabulary rather than its subject: find the colliding word.
- Counter-evidence on the crossing: what the vendors' own documentation says the commands do, in case a measurement here is a local accident.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H4 | Peer Claude sessions are durable enough to hold a delegated workflow; if not, the honest degradation is subagents or sequencing, and it must not be sold as equivalent | open |
| H5 | Claude and Codex can exchange more than exit codes, in at least one direction, without a TFW-side mechanism | open |
| H9 | A writer field can name a principal while legacy `actor` stays readable and the opaque filename token keeps its single job | open |
| H2 | Session-level team mode and stage-level TFW-45 swarm can be defined without vocabulary collision, and Phase A can specify a worktree protocol without deciding TFW-61's transport | open — shared with iteration 1, Challenge stage |
| H7 | Optional `organization_role` and `project_role` add useful structured context without a breaking migration, and a team scope is not a third dimension | open — shared, Challenge stage |
| H8 | On a revision round a fresh participant beats the one that produced the artifact. Testable against AFD's 13 revision arcs | open — shared, Challenge stage |

## Scope Intent

- **In scope:** this session's own measurable capabilities and their cost; both crossing directions; two vendors in one worktree; the journal corpus and the validator that gates it; the three shared hypotheses attacked with data that exists on this machine.
- **Out of scope:** Codex's internal chain reliability and its self-forking (H1 — iteration 1's assignment, by owner ruling); whether a worktree pays for its merge (H3 — same); branch and merge policy (TFW-61); the revise loop itself (TFW-58); any edit to the HL, to `.tfw/`, to `knowledge/`, or to another project. Nothing outside `research/iter2/` is written by this iteration.

## Guiding Questions

1. — none put to the owner; the gates were waived for this iteration and every question below was answered by measurement instead.
2. —
3. —

## User Direction

- Owner, 2026-09-02, in `iterations.yaml`: the two iterations are **parallel and independent**; the default reading of a numbered list does not hold for them.
- Owner, 2026-09-02, HL DoF 10: mechanics or failure — *"the RES files report conclusions without reporting what the tools actually did, including the failures"* is a failure condition of the whole task.
- Owner, 2026-09-03, on invoking this iteration: **"no questions to me"** — the stage gates are answered by the researcher; the stage files are still written in order.

---
Stage complete: YES
