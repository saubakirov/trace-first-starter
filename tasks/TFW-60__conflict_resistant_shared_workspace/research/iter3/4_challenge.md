# Challenge — "What do we NOT expect?"

> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md)
> Goal: several humans and agents advance different tasks in one synchronized folder without editing
> the same project-root registries first.
> Loops run: 3 of 3 (deep)

---

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D-II event ID | A monotonic counter | D-I enforcement | C skill only / D structural gate | Read-max-then-increment needs a serialised allocator. Under file sync, two offline writers both read the same max and both write `E0008`. Only a shared serialised implementation *reduces* this, and even it cannot prevent it across disconnected machines. A counter therefore drags an engine in and still does not close the case. |
| D-II event ID | B timestamp | D-I enforcement | A engine | Not contradictory, but the engine's headline justification (S24, "manual ID allocation") evaporates: there is nothing to allocate. The engine survives this pair only on some *other* ground. |
| D-III journal | A appended segments | D-I enforcement | C skill only | An append-only invariant over a growing file cannot be checked by an agent that must first read the whole file and then trust itself to write a strict prefix-plus-one-record. Either the grammar changes or code enforces it. |
| D-III journal | B one file per event | D-I enforcement | A engine | Coexist, but the engine's append-verification, segment-sealing, digest-chain and rollover duties have no subject. Keeping the engine here means keeping a component whose largest job has been deleted. |
| D-IV duplication | A snapshot stores `last_event_id` | D-VII Git | any | Orthogonal to Git, but incompatible with the ordinary-file-sync floor itself: no provider offers a cross-file transaction (iteration 1 D11). Storing a journal fact in the snapshot manufactures a two-file commit on a substrate that has none. This is self-inflicted, not imposed. |
| D-V participant | A shared registry / `CURRENT_USER` | anything | — | A project-root mutable file every session writes: precisely the contention TFW-60 exists to remove. Already excluded by the draft and by the field product. |
| D-V participant | B profiles + binding + `device_instance_id` | D-VI footprint | D nothing outside | A device identity with nowhere to live is not a device identity. |
| D-VI footprint | D nothing outside | D-VII Git | B G-B / C G-A | Absolute worktree, git-dir and index paths are machine facts; a synchronized file cannot hold them. |
| D-VI footprint | D nothing outside | private preferences | — | A gitignored file is still synchronized. `.user_preferences.md` sits in this repository's `.gitignore` and would replicate to every Drive participant. "Private inside a shared root" is a contradiction. |
| D-VII Git | A `.git` inside the sync root | any | — | [Git FAQ](https://git-scm.com/docs/gitfaq): *"It is important not to use a cloud syncing service to sync any portion of a Git repository."* Reinforced by direct observation that Drive writes into dot-directories and cannot exclude nested subfolders. |
| D-VII Git | D no Git in the tree | master HL DoD-9 | — | DoD-9 requires freeze baselines, attribution and release history to keep working. A synchronized tree with no Git relationship at all cannot carry a contract baseline. |
| D-III journal | D no journal | master HL DoD-3 | — | DoD-3 is frozen and requires a task-local coordinator journal. P4 and P7 are therefore not shippable, whatever their other merits. |

**Surviving configurations:**

| Config | D-I | D-II | D-III | D-IV | D-V | D-VI | D-VII | Notes |
|---|---|---|---|---|---|---|---|---|
| **P2** Grammar-first subtraction | C skill + D gate | B timestamp | B one file per event | B no duplication | C profiles + binding | B one per-project machine-local file | B G-B | Survives every pair. Recommended survivor. |
| **P3** Validator-only | B advisory validator | B timestamp | B one file per event | B | C | B | B | Survives. P2 plus one read-time checker. Fallback if the enum-typo residual is judged material. |
| **P0** Draft as written | A | A | A | A | B | A | B | Survives the pairwise test **only** by paying for its own incompatibilities: it needs the engine because it chose a counter, and it needs the transaction because it chose to duplicate. Eliminated on §7.1, budget and precedent — see C7. |
| **P7** H6 floor | D | D | D | B | D | D | unchanged | Violates frozen DoD-3. **Retained as the measurement baseline, not as a candidate.** |
| ~~P1~~ Field model transplanted | — | — | — | — | — | — | — | Eliminated for Full: Assisted reaches single-writer safety by *forbidding* concurrent roles (*"handoff и review не работают одновременно"*), while master HL §2.3 and DoD-2 make same-task parallel roles a first-class case that must be **ownered**, not banned. |
| ~~P4~~ No journal | — | — | — | — | — | — | — | Eliminated: frozen DoD-3. |
| ~~P5~~ Engine, no identity | — | — | — | — | — | — | — | Eliminated: keeps the expensive half and drops the cheap one. |
| ~~P6~~ Identity subsystem, no engine | — | — | — | — | — | — | — | Eliminated: keeps the half that buys least (E5) and drops the half that at least has a coherent story. |

**Unexpected survivor: P3.** The subtraction case is strongest against a *mutation engine* and weakest
against a *read-time validator*. A validator is a different animal: it never writes, so it cannot be the
sole path, it cannot block work when absent, and it has no availability failure mode. P3 concedes the one
residual R1 leaves — an agent typing `lifecycle: activ` — at a fraction of the cost. If the coordinator
wants belt-and-braces, P3 is the honest place to spend, not P0.

---

## Findings

### C1 — The honest hunt: is there a scenario that only executable code closes?

I looked for one, and I did not stop at the first comfortable answer. Nine candidates, each with a verdict.

| # | Scenario | Does only code close it? |
|---|---|---|
| 1 | Two writers append to the same journal file; one append truncates the other | **No.** Dissolved by D-III B. Two writers produce two files. |
| 2 | An agent writes an invalid enum (`lifecycle: activ`) and readers silently mis-handle the task | **No, and not by a mutation engine either.** Closed by a *reader* rule: an unrecognised value fails closed. That is a validator (P3) at most, and a one-line convention at least. |
| 3 | Records drift into heterogeneous shapes so a later tool cannot parse them | **Circular.** The intolerance for variation is created by choosing a machine-parsed carrier. A human-read line tolerates variation by design. |
| 4 | Adapters must produce byte-identical records | **Circular.** The requirement exists because a shared engine exists. It appears in the draft's evidence table and in no frozen DoD item. |
| 5 | SHA-256 of a manifest or an artifact | **No.** `sha256sum` / `Get-FileHash` / `git hash-object` are already present, and the shipped field reviewer skill already instructs the agent to take one. |
| 6 | An agent bypasses the interface and edits the files directly | **No — and the engine does not close it either.** The draft concedes: *"it cannot stop a person with filesystem write access from bypassing the supported command."* Both designs rely on compliance. |
| 7 | **Deterministically rendering 52-60 task folders into one index, reproducibly** | **Yes.** An agent asked to regenerate a 60-row table twice will not produce the same bytes. Code is required. **But** it is a build-time generator in the same class as `docs/scripts/gen_docs.py`, which this repository already ships and which nobody calls a state engine. It writes a derived, disposable file and it is already outside `tfw-status`'s scope by the draft's own boundary. |
| 8 | **Exact 111-to-60 migration accounting with zero guessed facts** | **Yes.** An agent doing 111-item exact accounting by hand will err, and the failure is silent. Code is required. **But** it runs once, against a copy, and is then dead weight. A one-shot migration script is not a shipped runtime. |
| 9 | **Two participants offline both allocate task ID `TFW-61`** | **No — and nothing in the draft addresses it.** See C2. |

**The verdict this produces is not the one H5 asks for.** H5 says *"No executable code is required."* That
is **false as written**: scenarios 7 and 8 require code. What is true, and is the substantive claim, is
that **no deterministic state-transition engine and no mandatory mutation interface are required**. The
code that is genuinely required is two narrowly scoped, non-authoritative pieces — a derived-view
generator and a one-shot migration script — both of a class the repository already ships. Neither owns
task state, neither is on the mutation path, and neither can block work when absent.

### C2 — The counter the draft leaves in place

`.tfw/project_config.yaml`: `id_format: "{prefix}-{seq}"`, `initial_seq: 12`. `plan.md` Step 4.1: *"Create
task folder — `tasks/{PREFIX}-{N}__{description}/` → read `tfw.task_prefix` and `tfw.initial_seq`."* The
next task ID is obtained by scanning the project for the current maximum.

That is **read-max-then-increment across the whole project** — the exact operation S24 objects to for
event IDs, sitting at the task level, at the moment of task creation, which is the highest-value
collision in the system. Two participants working offline in one synchronized folder both create
`TFW-61`, and on reconnect two different task directories claim one identity. No engine in the draft
prevents this, because the draft's engine is scoped to *"task-control creation, event append,
lifecycle/snapshot transition, ownership change, recovery and validation"* — it operates on a task root it
is handed, not on the namespace.

Neither iteration 1 nor iteration 2 raised this: their migration analysis found *"zero duplicate
identities"* in the existing corpus, which is a statement about history, not about concurrency.

The field product solved exactly this, deliberately, and said so: `ID = YYYYMMDD-HHMMSS__slug`, no
counter, collision resolved by taking a new actual timestamp, allocation performed by an atomic
create-if-absent. **A Phase A that builds an event-ID allocator while leaving the task-ID counter
untouched has automated the cheap collision and left the expensive one.** This does not require adopting
the field grammar wholesale — but it does require the TS to say which it does.

### C3 — Attacking P2: does one file per event actually survive?

I attacked the survivor rather than only the incumbent.

| Attack | Result |
|---|---|
| **100-event long task** — the case that produced the rollover requirement | 100 files in `journal/`. No rollover policy, no sealed-segment digest, no encoded-byte ceiling: the bound that matters is *how many the reader opens*, and a reader opens the last N by filename sort without reading the rest. This is strictly better than the segmented file, where a bounded read still requires opening a segment that may hold 100 records. The three unsupported numbers (`100 events`, `32 KiB`, `240 code points`) that iteration 2 could not justify simply stop being needed for count and bytes. A summary-length bound remains sensible and stays a convention. |
| **Two events in the same second** | Real. Mitigated exactly as the field product mitigates task-ID collision: on collision take a new actual timestamp, and use millisecond precision. Note that the withdrawn v1.3 hook already wrote its event log as one file per event named `event-{yyyyMMddTHHmmssfffZ}-{Event}-{safe}.log` — the field implementation of a journal was *already* one-file-per-event with a millisecond stamp. |
| **Ordering under file sync** | Filename sort gives total order without a chain. Providers deliver files independently and out of order; a missing middle event is visible as a gap in an otherwise dense sequence, and — unlike a torn append — it cannot corrupt its neighbours. |
| **Provider conflict copy** | Lands as a *sibling* file with a provider-mangled name. Visible to a human in a file listing, nameable by an agent, and it never overwrites the original. Under D-III A the same event would be a conflicted copy of the whole segment, which is the case iteration 2 had to build a recovery matrix for. |
| **Tamper detection** | Weakened: no digest chain, so a silently deleted event is only detectable as a gap, and a silently rewritten one is not detectable at all. **Honest cost.** Counter: the draft itself already disclaims this — *"It does not make the log tamper-proof against a writer who can replace the entire chain, and Phase A does not claim such security."* A chain that cannot resist the attacker it names is buying detection of *accident*, and accidental single-file rewrite is rarer than accidental torn append, which is what the chain was defending against in the first place. |
| **Git noise** | 52 tasks × tens of events = thousands of tiny blobs over the project's life. Git handles this without difficulty; it does inflate `git log --stat` for a task folder. Acceptable. |
| **Human readability** | Improves. `ls journal/` shows `20260826T162000123Z__handoff.md` — timestamp and kind in the name. A human sees the management history without opening anything, which is precisely the "browse the synchronized folder" case DoF-7 protects. |
| **Does it reopen an eliminated family?** | No. Iteration 1 eliminated C4 (*event-derived state, replay required*) and C5 (*combined snapshot and unbounded history in one conflict domain*). P2 keeps a separate snapshot, so no replay; and the history is not in the snapshot's conflict domain, so C5 does not apply. D-III B is a **new alternative within the surviving family**, not a resurrection. |

P2 survives. Its one real cost is chain-based tamper detection, which the draft already declines to claim.

### C4 — The device registry recreates the contention TFW-60 exists to remove

Treated as a hypothesis, not a premise, per the mandate. A shared mutable device list would be:

- a **project-root file every participant writes**, on every new machine and every rename — DoF-1 and
  DoF-2 in one artifact;
- an **authoritative-looking aggregate** whose value can disagree with reality — DoF-4;
- a **privacy surface**: machine names and usage patterns of every participant in a shared folder,
  against `knowledge/constraint.md` F1 (shared personal state is unsafe);
- a **false-authentication invitation**: a list of known devices reads like an allow-list, and D59 exists
  to keep capability claims apart.

The draft already refuses it, for substantially these reasons. That part of S29 is correct and should
stand. What should not stand is the *"optional derived observed-instance report"*: a project-wide derived
aggregate that must be produced and refreshed, serving diagnostics nobody has asked for, admitted with no
§7.1 answer. Remove it.

And the positive half of S29 — `device_instance_id` — fails its own test. The draft concedes it authorises
nothing, is copied along with the local home, and *"cannot be detected reliably without stronger external
identity"*. It buys automatic detection of one rare case (a binding copied to another machine) that the
field model already handles by asking one short question. One question on an unrecognised device is
cheaper than a UUID, a `device.yaml`, a three-OS path specification and an install/verify lifecycle.

### C5 — Counter-evidence: where the subtraction case is weakest

Stated deliberately, because a subtraction pass that finds only reasons to subtract has not been run
honestly.

1. **Cross-agent reproducibility.** If the owner's real requirement is that Codex, Claude Code, Cursor and
   Antigravity produce *identical control bytes*, only one shared implementation delivers it. Skills
   cannot. This is the strongest argument for the engine, and it is the argument S24 is reaching for with
   "homogeneous". Against it: no frozen DoD item requires byte-identity. DoD-2 requires **one normal
   writer per mutable file** — which is an ownership property, not a byte property — and DoD-11 requires
   filesystem inspection to be sufficient to resume, which tolerates variation. If the owner *does* want
   byte-identity, that is a new requirement and belongs in §12, not in a Phase HL.
2. **The failure this iteration cites is a hook, not an engine.** The v1.4 withdrawal (G5) is about a
   session hook that scanned the whole tree on every event and blew a 30-second budget. An on-demand
   engine touching one task folder would not fail that way. The transfer is valid only for the engine's
   two full-tree duties — index generation and migration accounting — and, notably, those are the two
   duties C1 concedes need code. That is an uncomfortable pairing and I am recording it rather than
   smoothing it: **the parts of the engine that genuinely need code are also the parts the field evidence
   shows are slow on a Drive mount.** The mitigation is that both are explicit, on-demand, and never on
   the path of a normal transition.
3. **Removing the engine does not remove the hard evidence obligations.** NH (non-technical human) and PR
   (real offline fork / reconnect / conflict copies) remain mandatory under §7.1 and DoD-14 regardless of
   architecture. Subtraction reduces the *build*, not the *proof*.
4. **A skill's strictness is real but not structural.** The four field `SKILL.md` files are genuinely
   constraining — name gates, forbidden actions, exact stop points, mandatory reports, *"Отсутствие
   отправленного отчёта не считается завершённым preflight"* — but every one of them is a rule an agent
   must choose to follow. What makes the name gate different is that it is enforced by an *operation with
   an observable result* (rename, then verify the rename), not by memory. That distinction is the design
   lever: prefer rules whose compliance produces an artifact, over rules that merely forbid.
5. **`status.yaml` at six or seven fields still passes.** This iteration does not argue against a strict
   task-local status carrier. Iterations 1-2 earned it. The argument is against the two fields that
   duplicate journal facts, and against the machinery those two fields require.

### C6 — H7's dependency chain, traced explicitly

The mandate asked what falls if the premise falls. The premise does **not** fall — so the trace runs the
other way, and it is more interesting.

```
PREMISE  "a synchronized .git breaks the repository"
   status: CONFIRMED by primary source — Git FAQ, "not… any portion of a Git repository";
           corruption classes named: missing objects, changed or added files, broken refs
   reinforced by: PR observation — Drive writes desktop.ini into 100% of directories,
                  including dot-directories; nested subfolders cannot be excluded (G2, G12)
   ├── "supported root contains no .git directory or gitfile"        → SURVIVES, and the
   │      "or gitfile" clause is well-aimed: this repo has 2 linked worktrees, each of
   │      which keeps a .git FILE in its root
   ├── machine-local Git paths (work_tree / git_dir / index_file)    → SURVIVES
   ├── G-B as a *topology*                                           → SURVIVES
   ├── G-B as a *Git-supported configuration*                        → DOES NOT SURVIVE
   │      the same paragraph: a shared working tree is safe "only… if it will only be
   │      used by a single user across all machines". Multi-participant Drive worktree
   │      is not that. Residual risk is precise: an index whose cached stat data
   │      describes a worktree another machine changed underneath it
   ├── L3 pre-landing manifest + post-staging drift recheck          → SURVIVES, and is
   │      now *better* motivated: it is the control for exactly that residual
   └── G-A optional per-participant pinned external Git              → WEAKENED. More
          participants sharing one worktree with more independent indexes is the
          configuration the source warns about most directly. Keep it optional and
          Full-only, as iteration 2 already ruled, and stop describing it as an
          upgrade
```

Two corrections the Phase A draft needs, neither touching a frozen claim:

- It cites Google's stream/mirror pages for a proposition Google does not state, and does not cite the one
  source that states it directly. Cite the Git FAQ.
- It should stop implying that removing `.git` makes the topology *supported*. The honest formulation:
  removing `.git` removes the object/ref corruption class; the remaining risk is index/worktree staleness,
  and L3 is the control for it.

**And one thing the draft is missing entirely.** `.gitignore` in this repository does not list
`desktop.ini`. On the observed Drive behaviour, a worktree in the sync root gains roughly **1 189**
untracked `desktop.ini` files — one per directory — rewritten en masse on every Drive client version
bump, because the client version is embedded in the file body. That is not a corruption risk; it is a
noise and staging risk directly relevant to L3's *"leaves unrelated peer changes unstaged"* and to the
existing risk F1 about broad staging. A one-line `.gitignore` entry closes it, and no design does.

### C7 — Why P0 is eliminated, stated as four independent grounds

Any one of these would be arguable. Together they are not.

1. **§7.1.** Five components of P0 cannot name a duplicate write they remove, and `status.yaml` at nine
   fields *adds* one (E2). §7.1 is frozen and admits no new artifact that fails this test.
2. **Budget.** 92-111 modified against 30, and 82-143 new against 15 (E3). DoF-12 makes crossing a budget
   without an exact count and an explicit owner ruling a failure condition. Subtraction does not fix this
   alone — 59 % of even the floor is adapter copies — but it moves the phase from ~3.4× to ~1.7×.
3. **Precedent.** TFW-49's owner verdict rejected, by name, *"the schema, state, Python
   validator/router/runtime, Git hooks, range audit, installation lifecycle, and cross-platform
   machinery"*, at a cost of 149 files and 27 103 deletions. P0 proposes two JSON schemas, a
   validator/router/runtime, a checked Git helper, cross-platform machine-local machinery and an
   install/verify lifecycle in `/tfw-init` and `/tfw-config`. `KNOWLEDGE.md` D24 states the standing
   decision: *"No scripts — AI agent is the sync engine."* TFW-54, reached independently, froze DoF-2:
   *"Anything executable ships… TFW-49's cause of death."*
4. **Field withdrawal.** The same owner built the engine, the machine-local home, the binding and a
   machine-local event log — 738 lines across two implementations — shipped them in three versions, and
   removed them in v1.4 because on a real large folder the check exceeded its own timeout and could hang
   without reporting (G5). The replacement shipped is prose plus four skill contracts.

### C8 — What the recommended survivor P2 looks like, concretely

Not a design — a bounded description of what the coordinator would be choosing.

- **Status:** a short task-local control carrying what artifact presence cannot derive — lifecycle,
  terminal outcome, `waiting_on`, owner, plus the goal/value summaries the index needs. Six or seven
  fields. `last_event_id` and `journal_head` are **not** among them.
- **Journal:** `journal/<UTC-ms>__<kind>.md`, one file per event, reference-first, closed vocabulary
  unchanged from iteration 1 D7 as amended by iteration 2 D8. No segments, no sealing, no digest chain,
  no rollover policy, no count/byte ceilings. Head is the last filename.
- **Enforcement:** the lifecycle skills write, as they already do. Single-writer is enforced structurally
  by extending TFW's existing Step-0 session naming into a **verified blocking gate** — the field model's
  mechanism, which TFW half-has already: `plan.md`, `handoff.md` and `review.md` carry *"Name this
  session"* today, but three of thirteen workflows carry it, it is not verified, and nothing blocks on it.
  Making it verified and blocking is a change to text that already exists, not a new mechanism.
- **Index:** `tasks/INDEX.md`, generated by a build-time generator in the `gen_docs.py` class, derived,
  disposable, one publisher. No engine.
- **Identity:** `people/<handle>.md` exactly as the field product ships it, plus **one** machine-local
  file per project holding the bound profile handle, a pointer to private preferences and the three Git
  paths. No `device_instance_id`, no `device.yaml`, no three-OS home tree, no observed-instance report.
- **Git:** unchanged from iteration 2 — G-B baseline, optional Full-only G-A, L3 — with the citation
  corrected to the Git FAQ, the "supported" claim softened, and `desktop.ini` added to `.gitignore`.
- **Migration:** a one-shot script against a copy, with the exact-accounting contract iteration 2 D10
  already specified. Deleted from the framework after it runs, or kept in `docs/scripts/` where one-shot
  tooling already lives.
- **Not shipped:** the deterministic state engine, the `tfw-status` skill and its four adapter copies,
  `.tfw/task_state.md`, `.tfw/workflows/status.md`, both JSON schemas, the full machine-local home,
  `device_instance_id` and the observed-instance report.

Rough delta against P0: **-4 canonical new documents, -4 skill files, -5 to -12 engine files, -3 to -5
templates, -52 to -104 per-task journal segments** where the journal is created lazily, and the largest
single item, **the entire deterministic-engine LOC budget**.

### C9 — What this iteration could not establish

- **NH.** No non-technical participant was observed. Unchanged from iteration 2, still mandatory.
- **PR, the hard half.** Offline fork, reconnect, conflict-copy naming and two-device reconciliation were
  not observed. The Drive mount is real and the provider artifacts are real, but the folder holds no
  active task and no second device is reachable from here.
- **Empirical Git reproduction.** The mandate forbids state-changing Git commands, so no throwaway
  repository could be created inside a Drive folder and observed failing. C6's premise therefore rests on
  primary documentation plus a read-only census, not on a reproduction. This is the correct trade: master
  HL §2.1 risk F1 records that two sessions sharing one index already produced a misattributed commit.
- **Whether every TFW adapter can rename its own session.** C8's blocking name gate depends on it. Codex
  can; TFW's own Step 0 assumes the others can; none of it is verified. This is a TS/evidence item.
- **Populated Assisted corpus.** All four field starters are unused templates with no `work/` directory
  and no participant profiles. The migration obligation *"a populated Assisted corpus must be included
  when available"* is currently unmeetable from any source I can reach.

---

## Checkpoint

| Found | Remaining |
|---|---|
| Nine scenarios tested; only two require code, both non-authoritative and of a class already shipped. H5 is **false as written** and **true in substance** (C1) | — |
| The task-ID counter is an unaddressed project-wide read-max-increment — the same defect S24 objects to, at higher value, left in place by the draft (C2) | Whether the TS adopts a timestamp identity or a reservation rule; either way it must say |
| P2 survives a seven-way attack; its only real loss is chain-based tamper detection, which the draft already disclaims (C3) | — |
| A shared device registry recreates DoF-1/2/4 plus a privacy surface; `device_instance_id` fails its own test (C4) | — |
| Counter-evidence recorded: cross-agent byte-identity is the one requirement only an engine serves, and no frozen DoD asks for it (C5) | If the owner *does* want it, that is a §12 matter |
| H7's premise is confirmed, not refuted; the same source is stricter than the draft's conclusion; L3 gains motivation, G-B loses the word "supported" (C6) | Empirical reproduction impossible here |
| Four independent grounds eliminate P0 (C7) | — |
| `desktop.ini` is absent from `.gitignore`; ≈1 189 untracked files would appear in a Drive-hosted worktree (C6) | — |

**Sufficiency:**
- [x] External source used? — Git FAQ (PS), Google Drive documentation (PS), live Drive mount (PR)
- [x] Briefing gap closed? — all three guiding questions answered with evidence
- [x] Pairwise incompatibility checked? Surviving configurations listed? — 12 pairs, 4 configurations
      eliminated with reasons, P2 recommended, P3 as the unexpected survivor

**Metacognitive check.** The findings that were *not* available before this iteration ran: the field
withdrawal of an already-built engine (G5); the one-file-per-event alternative (D-III B) that no prior
configuration space contained; the task-ID counter (C2); the inversion of H7 — the folklore charge fails
and the source turns out to constrain the draft's own baseline; and the discovery that the budget overrun
is mostly adapter duplication rather than architecture. The place I most had to resist a comfortable
answer was C1: the subtraction case wanted "no code at all", and the evidence does not support it.

Stage complete: YES
→ User decision: coordinator gate — proceed to synthesis
