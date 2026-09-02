# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> Goal: a project declares who its participants are, a coordinator runs the task with a team of them in isolated trees under a contract it cannot move.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1 | peer session by name | D3 | text on stdout | A peer answers into a conversation, not a pipe. There is no stream for the caller to read, and `claude --help` exposes no subcommand that posts into a running session — the peer channel is in-session tooling only |
| D1 | in-process subagent | D5 | one worktree per principal | A subagent has no separate identity and no tree of its own; it runs inside the caller's process and cwd. Isolating it is isolating the caller |
| D2 | `exec resume --last` | any | any | **Measured, not argued:** from a foreign caller, `--last` attached to the owner's interactive thread (2.8 MB, 264 K tokens) and answered out of it. `--include-non-interactive` does not exist in this build. A delegation that can land in the human's own session is not a delegation |
| D2 | file drop | D1 | any autonomous shape | A file drop waits for a human to open a session, which is the one thing §1 promises to remove: *"the owner approves once… and comes back to a finished result"* |
| D3 | journal event only | — | — | The canon forbids an event carrying HL/RES/TS/RF/REVIEW text; the detail must live in the artifact and the event reference it. Excluded by rule, not by preference |
| D4 | reuse free-form `via` | — | — | §7 P5: authority is carried by the name. `via` is declared free-form, is checked by nothing, and has already drifted `claude` → `claude-code` inside one corpus. A grant cannot rest on a field that renames itself |
| D4 | the filename token | — | — | The pre-`2.0.0-dirty.3` design. Two jobs in one component is the failure that removed `actor`; D68 names it |
| D5 | one shared tree | — | — | Three measured index corruptions (TD-144, TD-178, TFW-60/A), and a verbal staging directive measured at 0 successes of 1 |

**Surviving configurations:**

| Config | D1 Claude | D2 Codex | D3 return | D4 writer | D5 worktree | Notes |
|--------|-----------|----------|-----------|-----------|-------------|-------|
| C1 | peer by name | interactive chain | artifact | `writer` key | per principal | The HL as drawn. Survives **only when a Codex participant coordinates** — see C3 below |
| C2 | headless `-p` + id | interactive chain | artifact | `writer` key | per principal | Adds an on-demand Claude delegate the peer list cannot supply |
| C3 | headless `-p` + id | `exec` + `resume <ID>` | artifact | `writer` key | per principal | The only row reachable **from either vendor's coordinator** |
| C4 | headless `-p` + id | `exec` + `resume <ID>` | `-o` file → artifact | `writer` key | per phase | Same, with the machine-readable hop the vendors already supply |
| C5 | peer by name | `codex mcp-server` | stdout | `writer` key | per principal | Survives structurally; declaring it is TFW-61's subject, so it is named and not chosen |
| C6 | subagent | `exec` + `resume <ID>` | artifact | `writer` key | per phase | The degraded shape: a subagent is a stage helper, never a delegate |
| C8 | peer by name | interactive chain | artifact | second principal key | per principal | Identical cost to C1 — both edit `EVENT_KEYS`; the choice is naming, not migration |
| C9 | no delegation | interactive chain | artifact | `writer` key | per phase | The honest degradation. It must never be sold as team mode |

**Unexpected survivors:**

- **C3/C4 — the headless pair.** The HL's §2 frames the peer discovery as the news, and it is the wrong half. A peer cannot be *created*; it must already exist because a human opened it. A headless session **can** be created on demand, is resumable by id from any directory on the machine, and — measured — remembers its own history across process boundaries. The durable delegate is the one the HL never listed.
- **C5 — MCP.** Both CLIs speak it in both directions today. It survives every consistency check and is excluded only by scope discipline, which is a different thing from being wrong.
- **C8 — a second principal key.** Once G7 showed that any new event key costs the same validator edit, "reuse something that exists" stops being the cheap option. Nothing is saved by not naming the field `writer`.

## Findings

### C1: The crossing is asymmetric, so the Channel column is constrained by who coordinates

Measured routes, from each vendor's session outward:

```
      FROM a Claude session                     FROM a Codex session
  ┌──────────────────────────────┐        ┌──────────────────────────────┐
  │ Claude peer   ✅ by name      │        │ Claude peer   ❌ no route     │
  │ Claude fresh  ✅ claude -p    │        │ Claude fresh  ✅ claude -p    │
  │ Codex thread  ❌ no route     │        │ Codex thread  ✅ own chain    │
  │ Codex fresh   ✅ codex exec*  │        │ Codex fresh   ✅ codex exec   │
  └──────────────────────────────┘        └──────────────────────────────┘
       * three config overrides                 (S10: the owner's practice)
```

`Claude peer ❌ from Codex` is evidenced, not assumed: `claude --help` lists nine subcommands
(`agents`, `auth`, `auto-mode`, `doctor`, `install`, `mcp`, `plugin`, `setup-token`, `update`) and
none of them posts a message into a running session. `Codex thread ❌ from Claude` is the same shape
in reverse — the only handle a foreign caller has on an existing Codex thread is `resume`, and
`--last` resolves to the wrong thread.

**Consequence for the frozen §4.1 table:** the `Channel` column's value *"visible thread"* is only
achievable when the coordinator and the delegate are the same vendor. A cross-vendor row must read
*"fresh session"*, and the Role Assignment cannot promise a conversation it has no route to open.
This does not move a frozen claim — the column exists and its values are per-task data — but the
Phase D wording must not present the three channel values as freely combinable with any participant.

### C2: H2 — one word collides, and the real overlap is a deliverable, not a vocabulary

Term counts, both HLs:

| Term | TFW-45 | CRATM | Collision? |
|---|---|---|---|
| `coordinator` | 17 | 48 | **Yes** — TFW-45's coordinator spawns a fresh agent *per stage inside one workflow*; CRATM's Coordinator is a workflow role held *across a task*, with "phase coordinator" one level down |
| `swarm` | 41 | 3 | No — CRATM uses it only to name the boundary |
| `agent` | 86 | — | No — CRATM's unit is `principal` (48), a word TFW-45 never uses |
| `dispatch` | 0 | 19 | No |
| `principal` | 0 | 48 | No |

So H2's vocabulary half holds with one repair: `coordinator` needs a qualifier in the Phase E
glossary — *task coordinator* and *phase coordinator* against TFW-45's *stage coordinator* — and the
two documents must not both use the bare noun.

The transport half does **not** hold as stated, and the problem is bigger than a word.
[TFW-61's proposal](../../../../tasks/TFW-61__collaboration_transport_modes/PROPOSAL__TFW-61__collaboration_transport_modes.md)
lists as its own deliverable 2: *"Git mode rules. **Task-owned explicit-path staging, no shared-index
ambiguity**, retained freeze…"*. CRATM Phase A deliverable 2 is exact-path staging with `git add -A`,
`git add .` and `commit -a` named and forbidden. **Two live tasks claim the same deliverable.** DoF 11
is not breached — CRATM decides no branch policy and no second transport, and "transport mode" in
TFW-61 means Git versus file synchronization, not a channel between agents — but ownership of the
staging rule has to be recorded somewhere, or the second task to arrive re-authors it.

### C3: H8 — AFD has no control case, and the corpus says something else instead

Every `REVIEW*.md` in AFD grouped into arcs by base name, `__revN` stripped:

| Measure | Value |
|---|---|
| Review arcs | 138 |
| Arcs with more than one round | **7** |
| Arcs in which the reviewer changed between rounds | **0 of 7** |

The HL's H8 says the question is *"testable against AFD's 13 revision arcs"*. It is not: there are 7
multi-round arcs, and in every one the reviewer label on the last round is the same as on the first
(`Codex (Reviewer)` ×4, `Reviewer (Claude Opus 5)`, `Reviewer (Claude Opus 4.8)`, `Reviewer (Codex)`).
**A fresh participant was never tried, so nothing in AFD can say whether it wins.**

What the corpus does contain is the case the hypothesis quotes, and it does not support the reading:
in `AFD-38/phase-b`, the same Claude reviewer issued ✅ APPROVE, then retracted it — *"I first issued
✅ APPROVE. **That was wrong**"* — under owner pressure (*«ты провалил работу как ревьюер»*), and the
same participant then produced the corpus's most thorough review: 100% of RF artifacts verified
against a 42% floor, with on-device evidence for a check it had previously accepted as deferred. The
correction came from the **owner**, not from replacing the participant.

Pairing executor and reviewer by vendor across all 138 arcs:

| Executor | Reviewer | Arcs | Mean rounds | Multi-round |
|---|---|---|---|---|
| claude | claude | 69 | 1.03 | 1 |
| codex | codex | 19 | 1.00 | 0 |
| **claude** | **codex** | **5** | **2.40** | **4** |

Read carefully, because the convenient reading is wrong twice. It does **not** show that cross-vendor
review is better: all five cross-vendor arcs sit inside AFD-48, one unusually hard task, so vendor and
difficulty are confounded and n=5. And it does **not** show that same-vendor review is efficient: 69
same-family arcs closing at 1.03 rounds is a 98% first-pass approval rate, and the one audited
instance of that pattern — AFD-38/phase-b — was wrong on the first pass. The external literature
points the same way: self-preference bias in LLM judges is well documented, ~90% of it attributable to
evaluator uncertainty and largely disappearing under blind evaluation, with *"use a judge from a
different model family than the generator"* the standard mitigation.

**Verdict on H8: not testable here, and it is TFW-58's question.** The one thing this task may take
from it is negative — the Role Assignment must not *forbid* naming a different participant for a
revision round, and it must not promise that doing so helps.

### C4: H7 — the dimensions are free, already field-tested, and scope is not a third one

- **Migration cost: zero, verified.** `team_profiles()` parses front matter with `yaml.safe_load` and
  checks nothing — no key set, no required keys. Every existing four-key profile stays valid because
  nothing was ever validating it. (Contrast the event schema, which is closed and does reject.)
- **The wording exists.** Assisted ships `Роль в компании` / `Роль в проекте` with three absence
  values, and the rule that the two are never merged. Full can match it or diverge knowingly.
- **A team scope is not a third dimension.** Scope is already a column in §4.1's Role Assignment —
  per task, per row, frozen with the row. A profile says what a participant *is* in the project; the
  assignment says what they hold *in this task*. Putting scope in the profile would make it mutable
  state that must agree with a frozen table, which is the two-files-must-agree problem D68 removed.

One divergence to decide rather than discover: Assisted's third type is `automation`, Full's is
`agent`. Two editions, two nouns, one concept.

### C5: What this iteration did not establish, and where it contaminated its own evidence

DoF 10 makes convenience-as-proof a failure of the whole task, and R7 names advocacy as this
research's own risk. Against both:

1. **The Codex failures are an install artifact, not a capability limit.** `codex-cli 0.120.0` from
   npm cannot read the owner's own `config.toml` and cannot use the owner's own model. The owner runs
   Codex successfully through another surface. What is proven is narrow: *the programmatic entry point
   reachable from a Claude session on this machine today needs three overrides.* An upgrade may erase
   all three, and none of this is evidence about Codex as a participant.
2. **n = 2 on the peer channel.** One three-day-old peer answered; one one-hour-old peer had not
   answered when the stage closed. That is enough to refute F11's *"Codex-only"* and nowhere near
   enough to support *"durable enough to hold a delegated workflow"*. What is measured is
   addressability and one successful round trip.
3. **This research corrupted a trace while measuring trace corruption.** The `resume --last` probe
   appended a turn to the owner's own interactive Codex session, which is now permanently in that
   session's rollout file. The HL counts three measured trace-integrity incidents; this is a fourth,
   in a new class — not a shared git index but a shared *session namespace* — and it was caused by
   this iteration, in read-only sandbox mode, by a command that looked like the obvious way to follow
   up a dispatch.
4. **Iteration 1 was not read.** Its Gather was in flight in this same tree while this file was
   written. Everything above is independent of it by construction, which also means nothing here
   corroborates it.
5. **The token figures are floors, not budgets.** One word, cold start, smallest models. A real
   delegation carries a workflow, its conventions and its artifacts; the ~40 K per call is the price
   of opening the door.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Eight configurations survive; three of the survivors were never proposed in the HL | which of C1–C4 Phase D declares is a coordinator decision, not a research one |
| The crossing is asymmetric: no route from Codex to a named Claude peer, none from Claude to a live Codex thread | whether a newer Codex build changes the forward route — untestable without upgrading the owner's machine |
| `coordinator` is the single colliding word with TFW-45; the real overlap with TFW-61 is a duplicated deliverable | who owns the explicit-path staging rule — coordinator's call |
| H8 has 0 control cases in 7 arcs; the quoted case was corrected by the owner, not by a fresh participant | TFW-58's subject; nothing further here |
| H7's two dimensions cost nothing and already exist in Assisted; scope belongs to the assignment, not the profile | `agent` versus `automation` — a Phase B naming decision |
| This iteration produced a fourth trace-integrity incident, in a class the HL does not yet name | — |

**Sufficiency:**
- [x] External source used? — vendor documentation for both CLIs, and the LLM-as-judge self-preference literature for C3
- [x] Briefing gap closed? — H4, H5, H9 answered with measurements; H2, H7, H8 attacked with corpus data
- [x] Pairwise incompatibility checked? Surviving configurations listed? — eight pairs eliminated, eight configurations survive, three flagged as unexpected

Stage complete: YES
→ User decision: gates waived by the owner for this iteration; proceeding to synthesis
