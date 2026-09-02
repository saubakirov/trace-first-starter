# RES — TFW_20260902-111644_CRATM: Claude's own side and the crossings (Iteration 2)

> **Date**: 2026-09-03
> **Author**: Researcher (Claude Code), on behalf of saubakirov
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> **Mode**: Pipeline · focused
> **Iteration**: 2 of 2 (min) / 5 (max) — **parallel and independent of iteration 1**, by owner ruling in `iterations.yaml`
> **Assigned hypotheses**: H4, H5, H9 · shared Challenge work: H2, H7, H8

---

## Research Context

Iteration 2 measures the side of the topology that Claude Code can measure from inside itself, and
every crossing between the two vendors: whether peer Claude sessions are a transport at all, whether a
Claude session and a Codex run can exchange more than an exit code, and whether a writer field can be
added to the journal without disturbing the immutable legacy corpus. It also attacks the three
hypotheses both iterations share — the boundaries against TFW-45, TFW-58 and TFW-61, the two role
dimensions, and whether a fresh participant is better on a revision round. Every claim below comes
from a command run in this session against the working tree at `cdbc493`, or from a corpus counted
here; the failures are reported with the successes because HL DoF 10 makes a conclusions-only report a
failure of the whole task.

## Briefing

See [1_briefing.md](1_briefing.md). No predecessor RES existed: the two iterations are parallel by
owner ruling, and iteration 1 (Codex measuring Codex) was at its Gather stage in this same working
tree while this iteration ran. Its in-flight notes were deliberately not read — reading them would
have destroyed the only thing a parallel pair buys. Gates were waived by the owner for this iteration
("no questions to me", 2026-09-03); the four stage files were still written in order.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | **The durable Claude delegate is a headless resumable session, not a peer.** Peers can be addressed; they cannot be created | Eight peers were listed and one answered a delegation, but nothing in a session can open a peer — a human does that. A `claude -p` run returns a `session_id`, persists as a transcript, and answered from its own history on `--resume` across a process boundary (5 s, $0.0037). The vendor's documentation adds that the id resolves from any directory on the machine |
| D2 | **`knowledge/constraint.md` F11 is false as written and must be re-measured, not rewritten.** Peers are not a Codex-only capability; what is verified is addressability plus one successful round trip | 8 peers listed, twice, twenty minutes apart; `helpdesk-2c` (3 days old, a different project) answered a delegation-shaped message in under a minute with substantive state. n=2 probes: the other peer had not answered when the stage closed |
| D3 | **Both crossing directions work with no TFW-side mechanism, and they are not symmetric.** Codex → Claude is one command; Claude → Codex needs three overrides on this machine | `claude -p` → exit 0, 5.7 s, "PONG". `codex exec` refused three times (config `service_tier: default` unreadable by the CLI; `flex` refused by the API; the config's model `gpt-5.6-sol` too new for the binary) and blocked on stdin once, then ran: exit 0, 16 s, "PONG", 43,466 tokens |
| D4 | **A dispatch is followed up by `resume <SESSION_ID>`, never by `resume --last`** | Measured: `--last` from this caller attached to the owner's own interactive Codex thread (started five minutes before the probes, 2.8 MB transcript, 264 K tokens), answered out of that thread's context, and left the turn permanently in its rollout file. Documented cause: `exec` sessions are excluded from `--last` unless `--include-non-interactive`, a flag absent from this build |
| D5 | **The writer field is a code change, not markup.** `EVENT_KEYS` in `.tfw/scripts/gen_index.py` is closed and an unknown key is a reported problem | Probe against the live validator: a new event carrying `writer: codex-lead` → `['unknown keys: writer']`. Until the key set gains it, every new event carrying a writer fails validation. §3.1's change map lists three templates and no code |
| D6 | **H9's real question is not whether a field can be added but what it is checked against** | `on_behalf_of: codex-lead` is refused in code today (human-only, enforced), so a principal cannot be smuggled through an existing field. `via` is disqualified: declared free-form, it drifted `claude` (26 Aug–29 Aug) → `claude-code` (29 Aug on), one tool with two spellings inside one corpus. And three legacy events already carry a tool name in `actor` — the failure the field was retired for, preserved in place |
| D7 | **H7's migration cost is zero, and a team scope is not a third dimension** | `team_profiles()` parses front matter with `yaml.safe_load` and validates nothing — no key set, no required keys. Adding `organization_role` / `project_role` breaks nothing because nothing checked. Scope already lives in §4.1's Role Assignment, per task and frozen with its row; putting it in a profile would recreate the two-files-must-agree problem D68 removed |
| D8 | **H8 is not testable against AFD, and the case the HL quotes points the other way** | 138 review arcs, 7 with more than one round, and in **0 of 7** did the reviewer change between rounds — no control case exists. In `AFD-38/phase-b` the same reviewer retracted its own wrong ✅ APPROVE under owner pressure and then produced the corpus's most thorough review (100% of RF artifacts verified against a 42% floor). The correction came from the owner, not from a replacement |
| D9 | **The per-call token floor prices delegation granularity before auditability argues it** | One word cost 43,466 tokens through `codex exec` and ~33.7 K cached tokens through `claude -p`. Whole-workflow delegation ≈ 40 K per phase; per-stage ≈ 170 K; a coordinator↔delegate chat, 0.4–1.3 M. S2 prices drift in tokens and owner time |
| D10 | **A fourth trace-integrity failure class exists: a shared session namespace, not a shared git index** | The `--last` probe wrote into a session nobody delegated. The HL counts three occurrences, all git-index; isolation by worktree does not address this one at all, because the namespace being shared is the vendor's session store |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Does a current Codex build remove the three overrides the forward crossing needs? | Open | Untestable here — it would mean upgrading the owner's machine. What is proven is narrow: the entry point reachable from a Claude session **today** needs them |
| Q2 | What is a `writer` value checked against — a `team/` handle (which demands a profile per principal) or free text (which drifts)? | Open | Phase B's decision. Both failure modes are already in this repository's own corpus (D6), so the choice is between two known costs, not between a cost and a clean option |
| Q3 | Who owns the explicit-path staging rule — this task's Phase A, or TFW-61's Git-mode rules? | Open | Coordinator's call. Both documents currently claim it; the second to arrive will re-author it |
| Q4 | Is `agent` or `automation` the project's noun for a non-human participant? | Open | Full's schema admits `type: agent`; the Assisted edition already ships `Тип: automation` with its own identifier form. Two editions, two nouns, one concept |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H4 | Peer Claude sessions are durable enough to hold a delegated workflow; if not, the honest degradation is subagents or sequencing | open | **🟡 partly supported, and the premise is wrong** | Peers persist for days and answer across projects (8 listed, one 3-day-old answered in <1 min). But a peer cannot be **created**, so it cannot be assigned by a Role Assignment written before the work starts. The durable, creatable delegate is the headless resumable session — measured working — and the honest degradation is a subagent, which is a stage helper, not a delegate. `2_gather.md` G1, G2, G3 |
| H5 | Claude and Codex can exchange more than exit codes, in at least one direction, without a TFW-side mechanism | open | **✅ confirmed, both directions, asymmetrically** | Text returned in both directions with no TFW mechanism. Codex → Claude: one command. Claude → Codex: three config overrides plus `</dev/null`. Neither vendor can address the *other's existing session*: `claude --help` exposes no subcommand that posts into a running session, and a foreign caller's only handle on a live Codex thread resolves to the wrong thread. `2_gather.md` G3, G4 · `4_challenge.md` C1 |
| H9 | A writer field can name a principal while legacy `actor` stays readable and the opaque filename token keeps its single job | open | **🟡 supported for the corpus, refuted for the cost** | The legacy side holds exactly as documented: a real pre-rule event with `actor` only validates clean, and 0 of 126 events lack an accountable party. The token is untouched — nothing compares it to any field. What fails is the premise that this is markup: `writer` is refused by the shipped validator's closed key set. `2_gather.md` G6, G7 |
| H2 | Team mode and TFW-45's swarm carry no vocabulary collision; Phase A can specify a worktree protocol without deciding TFW-61's transport | open | **🟡 one collision, and a deliverable overlap the hypothesis does not cover** | `coordinator`: 17 uses in TFW-45 (spawns per stage inside one workflow) against 48 here (a workflow role across a task). Every other term is disjoint — `swarm`, `agent`, `principal`, `dispatch`. TFW-61's proposal claims *"task-owned explicit-path staging"* as its own Git-mode deliverable, which is Phase A deliverable 2 verbatim. DoF 11 is not breached; ownership is unrecorded. `4_challenge.md` C2 |
| H7 | Optional `organization_role` and `project_role` add structured context without a breaking migration, and a team scope is not a third dimension | open | **✅ confirmed on both clauses** | Profiles are validated by nothing, so no migration exists to break. Assisted already ships both dimensions with three absence values and the rule that they are never merged — field evidence, not authority (S4). Scope is per task and already a column in §4.1. `3_extract.md` E6 · `4_challenge.md` C4 |
| H8 | On a revision round a fresh participant beats the one that produced the artifact. Testable against AFD's 13 revision arcs | open | **❌ not testable as stated — no control case exists** | 138 arcs, 7 multi-round, reviewer unchanged in 7 of 7. The quoted case (`AFD-38/phase-b`) was corrected by the owner, not by a fresh participant, and the same participant then produced the most thorough review in the corpus. Same-family pairs close at 1.03 rounds over 69 arcs — a 98% first-pass approval rate, which the self-preference literature reads as a warning rather than efficiency. `4_challenge.md` C3 |

## HL Update Recommendations

> **The researcher classifies. The researcher never applies.** Nothing in the HL was edited by this
> iteration. Refinements target the free sections and are the coordinator's to apply; amendment
> proposals target frozen sections and wait for an owner verdict in §12.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 | In *"A capability fact the project holds is no longer true"*: replace the unverified half with what was measured — 8 peers listed twice twenty minutes apart, six of them 3 days old, three sessions of one tool open in this project at once; one 3-day-old peer in a **different** project answered a delegation-shaped message in under a minute; a peer **cannot be created** from inside a session; a headless `claude -p` session can be created, returns a `session_id`, and answered from its own history on `--resume`. F11's correction is Phase E's, and this is the text it needs | `2_gather.md` G1, G2, G3 |
| R2 | §2 | In *"Isolation already exists on this machine"*: add the census — `~/.codex/worktrees/` holds 15 entries, **3 of them already readably named** (`kz-intake-phase-a`, `-review`, `-smoke`), so a task-shaped name is not something the protocol must win from the vendor; 6 token-named directories hold an **empty** `steps-framework/` shell with no `.git` while `.git/worktrees/` holds one admin entry, so a finished run's measured disposition is litter, not a dangling tree | `2_gather.md` G5 |
| R3 | §2 | Add the corpus counts the identity design rests on: 126 events, **0** without an accountable party, 98 with `on_behalf_of`+`via` only, 22 carrying both, 6 legacy `actor`-only; `actor` names a **tool** in 3 of them (`claude-code` ×2, `codex`); `via` is spelled `claude` before 29 Aug and `claude-code` after, one tool with two spellings and no rule broken | `2_gather.md` G6 |
| R4 | §8 | TFW-61 row: add that its proposal claims *"task-owned explicit-path staging, no shared-index ambiguity"* as its own Git-mode deliverable, which duplicates Phase A deliverable 2 — the boundary is not only vocabulary. TFW-45 row: add that `coordinator` is the single shared word and needs a qualifier in Phase E's glossary | `4_challenge.md` C2 |
| R5 | §9 | R2: add that the merge cost is iteration 1's measurement, while the **disposition** cost is now measured here (litter, not dangling trees). New risk: *a cross-vendor follow-up lands in the human's own session* — `resume --last` did exactly that, in read-only mode, and no worktree prevents it, because the shared namespace is the vendor's session store rather than the git index. Mitigation: dispatch captures the session id and follows up by id, and the protocol says so | `2_gather.md` G4 · `4_challenge.md` C5 |
| R6 | §9 | New risk: *a Role Assignment row promises a channel the vendor pair cannot open.* `Channel: visible thread` is achievable only when coordinator and delegate are the same vendor; there is no route from a Codex session to a named Claude peer, nor from a Claude session to a live Codex thread. Mitigation: Phase D states the constraint where the column is defined | `4_challenge.md` C1 |
| R7 | §10 | Update the hypothesis table with the six statuses above; retire the H8 row's *"testable against AFD's 13 revision arcs"* — measured: 7 multi-round arcs, 0 with a changed reviewer — and record that H8 is TFW-58's question, with the only claim this task may carry being negative (the Role Assignment must neither forbid a different participant on a revision round nor promise that it helps). Close the blind spot *"whether peer Claude sessions are a transport at all"*; open a new one: **what a writer value is checked against** | `4_challenge.md` C3 · D6 |
| R8 | §7.2 | Add a citation row: `editions/02-assisted/team/README.md` ships `Роль в компании` / `Роль в проекте` with three absence values and the rule that the two are never merged — field evidence for Phase B's schema, never authority over it (S4), and the place where Full's `agent` and Assisted's `automation` diverge | `3_extract.md` E6 |

### Amendment Proposals — frozen sections, owner verdict required

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|------|-----------------|----------|------|------------------------|
| A1 | §3.1 | `EXTEND` | Add `.tfw/scripts/gen_index.py` (`EVENT_KEYS`) to the change map under Phase B, so the map names every file the phase must touch | A new event carrying `writer: codex-lead` returns `['unknown keys: writer']` from the live `validate_event`; the map currently lists three templates and no code, and DoD 5 cannot be met without the edit | One more file inside Phase B's scope budget, and its test; the phase stops being template-only | Carry the writer in `via` — rejected: free-form, measured drift, and §7 P5 puts authority in the name. Leave the map silent — rejected: the executor discovers a red gate mid-phase and has to stop to ask |
| A2 | §5 | `EXTEND` | DoD 16: state that extending the closed key set of a validator that already ships is not *"adding something executable"*, and that no new script, hook, daemon, lock or behaviour-selecting config key is thereby permitted | DoD 5 requires `type: agent` to be *"consumed by something… named as a writer"*, which A1 shows requires the edit; DoD 16's word *"added"* reads as forbidding it to the person about to do it | One clause. It makes the NS3 boundary sharper rather than weaker, because it names what is still forbidden | Rely on the reading of "added" — rejected: an executor will file an amendment mid-phase to ask, which is the interruption the mode exists to remove. Drop DoD 16's list — rejected: it is the guard TFW-49 died for the lack of |
| A3 | §4 | `EXTEND` | Phase B deliverable 3: the validator refuses `actor` on a **non-legacy** event, while continuing to tolerate it on every legacy one | Probe row 5: a new event carrying `actor: claude-code` validates clean today, so the template's *"do not add the field to a new event"* has no enforcement site — the thing §7.1 forbids in its own words. The `legacy` flag needed to tell them apart already exists in `validate_event` | One condition and one test. It cannot touch existing events: legacy detection is by the event's own filename shape | Prose only — rejected by §7.1 and `process.md` F30: capture without an enforcement site does not change behaviour. Refuse `actor` everywhere — rejected: it would demand an edit to an immutable event, which is the failure the tolerance exists to prevent |

## Fact Candidates

> Human-sourced only. Everything an agent could discover by reading the tree or running a command was
> routed into the refinements above instead.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | process | **The owner delegates a whole research iteration with every gate waived** — the iteration was invoked as `/tfw-research <task> iter2` with *"no questions to me"*, while the sibling iteration ran concurrently under another vendor in the same working tree. The mode this task designs was exercised on this task's own research before the mode was written | User, 2026-09-03, invoking iteration 2 | ★★★ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | stakeholder | **The owner's waiver arrives per invocation, not per task, and it arrived as one clause of a command.** *"no questions to me"* was appended to the research invocation rather than declared anywhere durable — which is precisely what §3's *"the autonomy boundary is a declared scope, not a moment"* predicts a coordinator will otherwise receive: a verbal grant with no record. **Implication:** the frozen Role Assignment's *"Autonomous from"* column is the place that clause belongs, and the value of this task's own field run is that the grant was given in the failure mode the column removes | User, 2026-09-03 | ★★★ |

## Findings Map

**The crossing, measured — who can reach whom, and at what price**

```
                        ┌──────────────────────────────────────────────┐
                        │  FROM a CLAUDE session (this one)            │
   ┌────────────────┐   │                                              │
   │ Claude peer    │◄──┤ ✅ by name · 8 listed · 1 answered in <1 min │
   │ (human-opened) │   │    ❌ cannot be CREATED                      │
   └────────────────┘   │                                              │
   ┌────────────────┐   │ ✅ claude -p → session_id → --resume          │
   │ Claude fresh   │◄──┤    5.7 s · $0.0040 · ~33.7 K cached          │
   │ (headless)     │   │    ✅ creatable  ✅ durable  ✅ resumable      │
   └────────────────┘   │                                              │
   ┌────────────────┐   │ ✅ codex exec … </dev/null                    │
   │ Codex fresh    │◄──┤    16 s · 43,466 tokens · 3 overrides needed │
   └────────────────┘   │                                              │
   ┌────────────────┐   │ ❌ no route. resume --last → landed in the    │
   │ Codex live     │◄──┤    OWNER'S thread (2.8 MB, 264 K tokens)     │
   │ thread         │   │    and left a turn in it permanently         │
   └────────────────┘   └──────────────────────────────────────────────┘

   FROM a CODEX session:  Claude fresh ✅ (claude -p on PATH)
                          Claude peer  ❌ no CLI subcommand posts into a running session
                          own threads  ✅ its own chain (S10, the owner's practice)
```

**Where a new field costs nothing, and where it costs code**

```
  team/{handle}.md   yaml.safe_load, NO key set, NO required keys ───► organization_role: FREE   (H7 ✅)
  bindings.yaml      outside the tree, read by no shipped script  ───► a principal key:    FREE
  journal event      EVENT_KEYS closed · unknown key = problem    ───► writer:  CODE CHANGE (H9 🟡)
  status.md          STATUS_KEYS closed · unknown key = problem   ───► untouched by this task

  probe results, live validator:
    baseline new event                      → []                        clean
    + writer: codex-lead                    → ['unknown keys: writer']  ✱ A1
    on_behalf_of: codex-lead                → refused, human-only       principals need the new door
    legacy actor-only, real filename        → []                        tolerance holds
    NEW event with actor: claude-code       → []                        ✱ A3 — prohibition has no site
```

**H8 against the AFD corpus — the control group that does not exist**

```
  138 review arcs
   └─ 7 multi-round arcs
       └─ 0 with a different reviewer on the later round      ← nothing to compare
  
  the case H8 quotes (AFD-38/phase-b):
     ✅ APPROVE (wrong)  ──owner pressure──►  🔄 REVISE  ──►  rev2/rev3  ──►  ✅ APPROVE
                                              ▲                              100% verified
                             the corrective force was the OWNER,             (floor: 42%)
                             and the participant never changed

  same-family pairs: 69 arcs, mean 1.03 rounds  = 98% first-pass approval
                     └─ the one instance ever audited was wrong on the first pass
```

## Iteration Status

- **Iteration:** 2 of 2 (min) / 5 (max) — parallel with iteration 1, not sequential
- **Hypotheses tested:** H4 (🟡 partly supported, premise corrected) · H5 (✅ confirmed, asymmetric) · H9 (🟡 corpus yes, cost no) · H2 (🟡 one collision + a deliverable overlap) · H7 (✅ confirmed) · H8 (❌ not testable as stated)
- **Hypotheses deferred:** H1, H3, H6 — iteration 1's assignment by owner ruling; its Gather was in flight in this tree while this RES was written and was deliberately not read
- **Gaps discovered:** the writer field is a validator edit, and §3.1 does not say so (A1) · DoD 16 reads against DoD 5 for the executor who must do it (A2) · a new event may reintroduce `actor` and pass (A3) · a fourth trace-integrity class, the shared session namespace, which no worktree addresses (D10) · the Channel column is constrained by the vendor pair (R6) · TFW-61 and Phase A claim one deliverable (R4)
- **Superseded decisions:** none — this is the first RES in this task

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | Whether a headless `claude -p` delegate can carry a **whole TFW workflow** — not one word, but `/tfw-handoff` for a real phase, with its context loading and its artifacts | D1 makes the headless session the only creatable durable Claude delegate, so Phase D's promise rests on it. One round trip of one word is not evidence that it can hold a workflow | One real delegation of a small, already-approved phase, measured end to end: tokens, wall time, whether the artifacts come back conforming |
| 2 | What a `writer` value is checked against (Q2) | Both available answers have already failed once in this repository: free-form drifted, and a handle-per-session forced two external projects into profile-per-agent | Enumerate the check options against the 126-event corpus and price each; the answer belongs in Phase B's TS, not in a research guess |
| 3 | Whether a current Codex build removes the three overrides (Q1) | If it does, the forward crossing is one command and the cost model changes; if it does not, the Role Assignment's cross-vendor rows carry a setup cost nobody has written down | Re-measure after the owner's own next Codex upgrade — cheap, and it invalidates or confirms D3's second half |
| 4 | The shared session namespace as an isolation subject (D10) | Phase A isolates the git index. Nothing in the HL isolates the vendor's session store, and this iteration corrupted a trace through it while measuring | Decide whether the worktree protocol says anything about session identity per run, or whether this is a §14 anti-pattern and nothing more |

### Recommendation
- [x] **SUFFICIENT** — for this iteration's assigned hypotheses (H4, H5, H9) and for the three shared ones, which are answered as far as data on this machine allows. Proceed to `/tfw-plan` to classify the two recommendation classes above. **This does not make the task's research complete:** `min_iterations: 2` and iteration 1 (H1, H3, H6) is still `pending` in `iterations.yaml` and in flight
- [ ] MORE NEEDED
- [ ] BLOCKED

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 2 measured Claude's own side and both crossings, and three of its four load-bearing results
correct the HL rather than confirm it. Peer sessions are real, durable across days and reachable
across projects — F11 is false as written — but they cannot be created, so the delegate a Role
Assignment can actually name is the headless resumable session the HL never lists, and that is the
capability Phase D's promise rests on. Both crossings work with no TFW mechanism, asymmetrically:
Codex reaches a fresh Claude in one command, Claude reaches a fresh Codex only by overriding the
owner's own configuration three times, and neither can address the other's *existing* session at all.
The writer field composes with the legacy corpus exactly as designed — 126 events, none without an
accountable party, tolerance holding on the real legacy shapes — and is nonetheless not markup: the
shipped validator's key set is closed, which turns one line of a template into a code edit that §3.1
does not currently admit. Of the shared hypotheses, H7 is confirmed and cheaper than assumed, H2 needs
one word qualified and one deliverable's ownership recorded, and H8 has no control case in AFD at all:
seven multi-round arcs, the reviewer unchanged in every one, and the failure the hypothesis quotes was
corrected by the owner rather than by a replacement.

Self-critique, under DoF 10 and R7. The peer channel rests on n=2 probes, one of which never answered.
The Codex failures are an install artifact — a stale npm CLI against a newer config — and prove
something narrow about this machine today rather than anything about Codex as a participant; Q1 says
so and leaves it open rather than resolving it in the mode's favour. The token figures are cold-start
floors for one word, not budgets. And the sharpest finding was produced by the researcher's own
mistake: following up a dispatch with `resume --last` appended a turn to the owner's live Codex thread,
which is a fourth measured trace-integrity incident, in a class no worktree isolates, caused by the
obvious command in read-only mode. That is what this iteration bought that a design discussion would
have missed — not the confirmation that the mode is possible, but four places where the frozen contract
is thinner than it reads.

---

*RES — TFW_20260902-111644_CRATM: Claude's own side and the crossings (Iteration 2) | 2026-09-03*
