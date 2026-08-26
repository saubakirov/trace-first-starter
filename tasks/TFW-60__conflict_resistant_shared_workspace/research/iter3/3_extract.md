# Extract — "What do we NOT see?"

> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md)
> Goal: several humans and agents advance different tasks in one synchronized folder without editing
> the same project-root registries first.
> Loops run: 3 of 3 (deep)

---

## Configuration Space

Seven dimensions from Gather. Only coherent combinations are listed; contradictory ones are dropped here
and the pairwise reasons are recorded in Challenge.

| Config | D-I enforcement | D-II event ID | D-III journal carrier | D-IV duplication | D-V participant | D-VI machine-local | D-VII Git |
|---|---|---|---|---|---|---|---|
| **P0** Draft as written | A engine | A counter | A appended segments | A snapshot duplicates | B profiles + binding + device ID | A full TFW home | B G-B |
| **P1** Field model transplanted | D structural gate | B timestamp | C section in the control file | C one file | D profiles + one question | D nothing outside | D no Git in the tree |
| **P2** Grammar-first subtraction | C skill + D gate | B timestamp | **B one file per event** | B no duplication | C profiles + binding, no device ID | B one per-project file | B G-B |
| **P3** Validator-only | B advisory validator | B timestamp | B one file per event | B no duplication | C | B | B |
| **P4** No journal | D structural gate | D none | D role artifacts are the record | B no duplication | D one question | C Git paths only | B |
| **P5** Engine, no identity subsystem | A engine | A counter | A segments | A | D one question | C Git paths only | B |
| **P6** Identity subsystem, no engine | C skill | B timestamp | B one file per event | B | B + device ID | A full home | B |
| **P7** H6 floor | D structural gate | D none | D role artifacts are the record | B | D | D | unchanged |

**Combination nobody proposed: P2.** Iterations 1-2 never had D-III alternative B on the table. Their
journal dimension ran *combined-with-status* (C5, eliminated) versus *separate appended file* (survivor).
"One file per event" was never a row. It is the alternative that makes the append-prefix invariant, the
sealed-segment digest chain, the rollover policy and the whole recovery matrix have no subject.

---

## Findings

### E1 — The six responsibilities the draft assigns to executable code, one by one

Phase A draft lines 208-216. The test each row must pass: **does this responsibility still exist if the
carrier grammar changes?**

| # | Responsibility (draft's words) | Survives a grammar change? | Analysis |
|---|---|---|---|
| **R1** | "strict status, event, profile and local-binding parsing/validation" | **Mostly no** | The strict-YAML application profile (D5: reject anchors, aliases, merge keys, tags, directives, duplicate keys) is a defence against features **YAML has and the carrier did not need**. A fixed line grammar — `Status: active` — has no anchors to reject. `profile` and `local-binding` parsing exists only because the identity subsystem exists (D-V B / D-VI A); under D-V C/D it disappears with them. **Residual:** an agent can still write `lifecycle: activ`. But that is closed by a *reader* rule — an unrecognised value fails closed — not by a writer engine. A validator ≠ a mutation engine. |
| **R2a** | "event-ID allocation" | **No** | Required only by D-II A. Monotonic `TFW-60-E0007` demands read-max-then-increment, which demands a serialised allocator, which under file sync demands a lock nobody has. D-II B needs nothing: the clock allocates. The field starter states the whole policy in one sentence — *"При коллизии… возьми новый фактический timestamp"* (G3) — and the actual atomicity comes from the filesystem: *"Атомарно создай только отсутствующую папку"*. `mkdir`/`O_EXCL` **is** the allocator, and it is already deterministic, already local, already installed. |
| **R2b** | "canonical JSONL encoding, append verification, segment sealing" | **No** | Append verification ("old bytes must be an exact prefix of the new bytes") exists because D-III A puts many events in one growing file. Under D-III B there are no appends: two writers produce two files, not a torn write. Segment sealing plus a SHA-256 predecessor chain exists to detect rewrite of that same growing file; with one file per event, deletion or alteration is visible by ordinary file listing, and a provider conflict copy lands as a *sibling*, which is exactly the behaviour the recovery matrix wants and could not get. |
| **R2c** | "snapshot update" (`last_event_id`, `journal_head`) | **No** | This is the second half of S24's justification — *"synchronizing two files from memory"* — and it is self-inflicted. `last_event_id` duplicates a journal fact; `journal_head` duplicates a directory fact. Under D-IV B neither is stored: the head is the lexicographically last filename. Remove the duplicate and the cross-file transaction, the event-first/snapshot-second ordering rule, and the entire six-way reconciliation matrix (journal-ahead, snapshot-ahead, duplicate-identical, duplicate-divergent, malformed, stale epoch) lose their subject. Master HL §7.1 requires every new artifact to name **the duplicate write it removes**; `status.yaml` as specified *adds* one. |
| **R3** | "recovery checks and byte-preserving fail-closed diagnostics" | **Largely no** | Downstream of R2. What remains under D-III B / D-IV B: two events with an identical timestamp (rename one — the field starter's own collision rule), and a provider conflict copy (a visible extra file a human can see and an agent can name). Neither needs an engine. |
| **R4** | "deterministic `tasks/INDEX.md` generation" | **Yes — and it is not a state engine** | Rendering N task folders into one view deterministically is a real job that grammar does not dissolve. But the draft itself puts it outside `tfw-status`'s scope, and it is a *generator*, in the same class as `docs/scripts/gen_docs.py`, which already exists and already reads the board. Counter-evidence worth recording: the shipped field product ships **no** index and explicitly forbids one (G3). This is a generator argument, not an engine argument. |
| **R5** | "external-Git preflight, exact-path manifest/staging and landing verification" | **Yes — and the executable already exists** | Real, and independent of carrier grammar. But the executable is **`git`**. Iteration 2's own preflight was `git rev-parse --absolute-git-dir --show-toplevel --git-path index` plus string comparison (`iter2/2_gather.md:233`). SHA-256 for the manifest is `sha256sum` / `Get-FileHash` / `certutil` — and the field reviewer skill already instructs the agent to take one (G3). This justifies a documented command sequence, not a new TFW runtime. |
| **R6** | "migration accounting and validation" | **Yes — and it is a one-shot script** | Real and unavoidable at 111 source occurrences. But it runs **once**, against a copy, and is then dead weight in the framework. A one-shot migration script is not a shipped deterministic state engine, and conflating them is how a permanent runtime gets justified by a temporary need. |

**Score: four of six dissolve or shrink to a reader rule; two survive and are satisfied by tools that
already exist (`git`, a hash utility, a generator in the same class as `gen_docs.py`) plus one throwaway
script.** Not one of the six requires the mutation engine the draft makes mandatory.

### E2 — The §7.1 ledger: what each mechanism absorbs, and what duplicate write it removes

Master HL §7.1 admits no new artifact that cannot answer both columns.

| Mechanism | Existing responsibility it absorbs | Duplicate write it removes | Verdict |
|---|---|---|---|
| Task-local status carrier | Live status from the root board | **Yes** — the per-transition README write. This is the whole point of Phase A | ✅ admitted |
| `status.yaml` **nine fields** | Goal/value/owner from the board row | Partly. But `last_event_id` + `journal_head` **add** two duplicate writes that did not exist | ⚠️ admitted at 6-7 fields, not 9 |
| `journal/` segments | Coordinator dispatch/handoff record that had no home (DoD-3, S5) | **No** duplicate removed; it is new surface. Justified by an owner decision, not by §7.1 | ✅ admitted by owner ruling, size unjustified |
| `tasks/INDEX.md` | The board's portfolio-view half | **Yes** — the board stops being written per transition | ✅ admitted |
| `.tfw/task_state.md` + `.tfw/workflows/status.md` | Rules that would otherwise live in `conventions.md` §5 and the four lifecycle workflows | **No.** Two new canonical documents alongside the ones that already own status | ❌ names nothing it removes |
| Two JSON schemas | Validation that a closed field list in prose already states | **No.** A third statement of the same shape, after `conventions.md` and `task_state.md` | ❌ triplicates the contract |
| Deterministic state engine | Writing that the lifecycle skills already do | **No.** It adds a mandatory dependency and an availability failure mode ("state-changing operations stop") | ❌ names nothing it removes |
| `tfw-status` skill + adapter copies | Routing that the lifecycle skills already perform | **No.** An indirection layer per adapter | ❌ names nothing it removes |
| `people/<handle>.md` | Attribution currently implicit in commit trailers and chat | **No** duplicate removed, but it is one small file per person and it is the field-proven shape | ✅ admitted |
| Machine-local TFW home (full) | `.user_preferences.md`, which exists and is gitignored | **Yes, one real thing** — a gitignored file is still synchronized by the provider, so "private preferences" inside a shared root are not private | ✅ admitted **for the binding + preferences**, not for `device.yaml` |
| `device_instance_id` | nothing | **No.** The draft itself concedes it authorises nothing, is trivially copied with the home, and cannot be reliably detected | ❌ |
| Derived observed-instance report | nothing | **No.** A new project-wide aggregate that must be regenerated | ❌ |

### E3 — The H6 measurement: floor versus draft

**Counting rule** (declared, so the numbers can be re-derived): a file is *modified* if a Phase A change
requires editing its bytes; adapter copies count individually, per master HL §7.1 — *"Adapter propagation
is counted and never hidden behind 'mechanical copy'."*

**The floor.** Smallest change after which a normal lifecycle transition of task X does not write
`README.md`. It has one non-obvious property: *most of the status is already derivable*. The board's
columns 4-8 (`HL | TS | ONB | RF | REV`) record artifact presence, which duplicates both the `Status`
column and the filesystem itself (D31, D50). What is genuinely **not** derivable from artifact presence is
only: `TODO`, `BLOCKED`, `waiting_on`, and the terminal outcome `DONE` vs `REJECTED`. So the floor carrier
is on the order of three fields, not nine.

| Floor — modified | n |
|---|---:|
| `.tfw/`: conventions, glossary, CHANGELOG, VERSION, project_config | 5 |
| Canonical workflows: plan, handoff, review, research/base, init, resume, release | 7 |
| Templates: REVIEW, RELEASE | 2 |
| Root/docs: README.md, RELEASE.md, knowledge/convention.md | 3 |
| Doc generator + tests, duplicated in `docs/` and `site/` | 4 |
| `.claude/commands/` affected | 7 |
| `.agent/workflows/` affected | 7 |
| `.tfw/adapters/codex/skills/` affected | 8 |
| `.agents/skills/` affected | 8 |
| **Total modified** | **51** |
| **New** | 1 carrier template + 52 per-task carriers (or 1 if created lazily on next touch) |

**The draft.**

| Draft — modified | n |
|---|---:|
| `.tfw/` top level (adds compilable_contract, quickstart, README) | 8 |
| Canonical workflows (adds docs, knowledge, config, update — `/tfw-init` and `/tfw-config` gain device/binding/Git attachment) | 11 |
| Templates (TS, RF, ONB, RES, REVIEW, RELEASE, evidence/EV, review/judge, review/verify, project_config) | 6–10 |
| Adapter sources under `.tfw/adapters/` | 19 |
| Installed adapter copies + root `CLAUDE.md`/`AGENTS.md` | 37 |
| Root docs and knowledge topic files | 4–10 |
| Doc generator + tests ×2 trees | 6 |
| `editions/02-assisted/` — stale at v1.0, must ship the model | 0–9 |
| `.gitignore` (`desktop.ini`) | 1 |
| **Total modified** | **92 – 111** |

| Draft — new | n |
|---|---:|
| `.tfw/task_state.md`, `.tfw/workflows/status.md`, 2 JSON schemas | 4 |
| `tfw-status` skill: adapter sources + installed copies | 4 |
| Deterministic engine (entry + status validator + journal + recovery + CLI); the withdrawn hook needed **two** implementations, 361 + 377 lines | 5–12 |
| Catalogue builder, checked Git helper, migration resolver | 3 |
| Templates: status carrier, event, people profile, device/binding/git | 4–6 |
| `tasks/INDEX.md`, `people/README.md`, `people/<handle>.md` | 3 |
| Evidence fixtures the draft's own table demands: schema matrix, adapter-parity fixture, 11-case identity matrix, 100-task corpus generator + manifest, 11-case recovery matrix, Git landing matrix, migration manifest | 7+ |
| **Framework subtotal** | **30 – 39** |
| Per-task migration output: `status.yaml` × 52 (+ first journal segment × 52) | **52 – 104** |
| **Total new** | **82 – 143** |

| Budget | Configured | Floor | Draft |
|---|---:|---:|---:|
| `max_modified_files` | 30 | 51 — **1.7×** | 92–111 — **3.1×–3.7×** |
| `max_new_files` | 15 | 1–53 | 82–143 — **5.5×–9.5×** |
| `max_loc` | 3 000 | low hundreds | see below |

The coordinator's working figures of **≥98 modified and ≥67 new are confirmed as conservative** — both
sit inside my independently derived ranges and toward the low end.

**LOC.** The withdrawn Assisted hook was 738 lines across two implementations for a *strictly smaller* job:
read-only checks, a status census, an actor binding and a secret regex — no mutation, no journal writing,
no schema validation, no Git, no migration. An engine owning validation, allocation, JSONL encoding,
sealing, recovery, index generation, Git preflight and migration accounting, in a form that must run where
`.tfw/` runs, plausibly consumes the entire 3 000-line budget on its own, before a single Markdown edit
and before tests. Draft decision item 3 — *"Python is an acceptable measured fallback, not an assumed
dependency; a zero-install/bundled path is preferred for Assisted"* — is a request for a bundled
cross-platform runtime, which is where the LOC and the packaging lifecycle both come from.

**The finding that changes the picture for H6:** the floor already exceeds the modified budget, and
**30 of its 51 files (59 %) are adapter copies**. Measured amplification is 3 identical bodies per
canonical workflow and 2 per Codex skill (G10). Subtracting the engine and the identity subsystem takes
the phase from ~3.4× to ~1.7× over budget — a large and real saving — but it does **not** bring Phase A
inside the budget, because the duplication is orthogonal to the architecture. Whoever writes the TS must
either obtain an evidenced owner ruling under DoF-12 or reduce the fan-out, and no carrier choice
substitutes for that.

### E4 — What must actually live outside the synchronized folder

| Candidate | Must it be outside? | Grounds |
|---|---|---|
| `.git` directory / gitfile | **Yes** | [Git FAQ](https://git-scm.com/docs/gitfaq) (PS): do not use a cloud syncing service to sync *any portion* of a repository; corruption classes named are missing objects, **changed or added files**, broken refs. Reinforced by PR: Drive writes into dot-directories without hesitation and cannot exclude a nested subfolder (G2, G12). **Not folklore.** |
| Git index | **Yes** | Same source; the index is the piece the FAQ's "in the middle of it being updated" clause is about. |
| Absolute worktree/git-dir/index paths | **Yes** | They are machine facts; a shared file cannot hold them. Already established in iterations 1-2 as the only `machine-local` finding they had. |
| Current-participant binding | **Yes** | Not for a Git reason. A gitignored file is still synchronized: this repository's `.gitignore` lists `.user_preferences.md`, and Drive would replicate it to every participant regardless. "Private" inside a shared root is not private. |
| Private preferences | **Yes** | Same reason. This is the one genuinely new thing the draft found, and it is worth keeping. |
| `device_instance_id` / `device.yaml` | **No** | Nothing forces it out because nothing needs it in. See E5. |
| A shared device registry | **No, and it must not exist** | The draft already refuses it, correctly. See Challenge C4. |

**The finding H7 did not anticipate.** The Git FAQ is *stricter* than the draft, not looser. It says a
shared working tree is safe *"only… if it will only be used by a single user across all machines"*. The
draft's supported G-B baseline is a working tree in a **shared** Drive folder used by **several**
participants. Removing `.git` removes the object/ref corruption class; it does not turn the remainder into
a configuration Git documents as safe. The residual risk it leaves is precise and nameable: **an index
whose cached stat data describes a worktree another machine has changed underneath it.** That is exactly
what the draft's L3 "recheck drift after staging" control addresses — so L3 is well-motivated and should
survive; what should not survive is citing this source as support for calling G-B *supported*.

### E5 — Identity: what the draft's addition buys over the field model

Owner's stated need, S28: *the agent should know at session start which participant is present, retaining
that on the participant's private computer; ambiguity asks explicitly; no shared `CURRENT_USER`.*

The field model (`people/README.md`, one page) delivers exactly that: one profile → silent selection;
several → private-device binding; new/shared/copied/mismatched device → **one** short question before the
first authorship write; `automation:<name>` is a separate identity; reading and ordinary conversation
require no choice; the profile is declared attribution and *"не аутентифицирует человека и не подтверждает
полномочия."*

| Draft addition on top | What it buys | What it costs |
|---|---|---|
| Stable `project_id` resolution | Lets one machine hold several projects' bindings | A shared config key; small |
| `device_instance_id` (generated UUID) | Automatic detection of a binding copied without its device | The draft concedes it authorises nothing, is copied along with the home, and *"cannot be detected reliably"*. The field model reaches the same outcome by asking one question on an unrecognised device — the case is rare and the question is cheap |
| `device.yaml` + `profiles/<p>/preferences.md` + `projects/<id>/{binding,git}.yaml` | Structure | Four file classes, a three-OS path specification, an install/verify lifecycle in `/tfw-init` and `/tfw-config`, and a new failure mode (`sync_only` when the home is missing) |
| Optional derived observed-instance report | Diagnostics | A new project-wide derived aggregate that must be produced and refreshed |

**And it was already built.** The withdrawn v1.3 hook implemented the machine-local home
(`%LOCALAPPDATA%\TFW-Assisted\<sha256-prefix>\`), the binding (`actor.txt`), profile enumeration from
`people/*.md` and single-profile silent selection — then it went away with the hooks, and v1.4 kept the
*policy* in prose while dropping the *machinery*. The field product has already run this experiment.

Trimmed to what is forced: **one machine-local file per project** holding the bound profile handle, a
pointer to private preferences, and the three Git paths. One new file class, no device identity, no
three-OS directory tree, no `device.yaml`.

### E6 — The circularity map

Three of the draft's strongest-sounding justifications are consequences of choices made one line earlier.

```
S24 "agents manually allocating event IDs"
      └── requires an allocator
            └── only because D-II A chose a monotonic counter
                  └── D-II B (timestamp) needs no allocator
                        └── and the field product already ships D-II B

S24 "synchronizing two files from memory"
      └── requires a cross-file transaction
            └── only because D-IV A stores last_event_id in the snapshot
                  └── D-IV B stores no journal fact in the snapshot
                        └── nothing to synchronize, nothing to reconcile

Draft evidence: "byte-identical valid records through every supported thin adapter"
      └── requires one shared implementation
            └── only because the acceptance test was written as byte-identity
                  └── which is achievable only if a shared engine exists
                        └── the requirement and the mechanism justify each other

Draft: "homogeneous records" (S24)
      └── requires low tolerance for variation
            └── only because D-III A chose a machine-parsed carrier
                  └── a human-read Markdown line tolerates variation by design
```

None of this makes the engine wrong. It makes the *stated* justification unable to carry it. If the engine
is to stay, it needs a justification that does not depend on the grammar C1-R2 happened to pick.

### E7 — What the field product proves, and what it does not

| Proves | Does not prove |
|---|---|
| A TFW-shaped lifecycle with plan/handoff/review roles, stable paths, one-writer discipline, status, a work log, identity and knowledge candidates **runs with zero executable components** in a live Drive folder | That it does so under **Full's** same-task multi-role concurrency — Assisted forbids concurrent role writes outright (*"handoff и review не работают одновременно"*) |
| An atomic `mkdir` plus a timestamp is a sufficient ID allocator | That the same works for a monotonic per-task event sequence — it does not, which is the point |
| A name gate enforced through session naming blocks a stage structurally, with no code | That every TFW adapter can rename its own session. TFW already has session naming in `plan.md`, `handoff.md` and `review.md` Step 0 — but only in those three, and it is not a blocking, verified gate anywhere |
| The engine and machine-local home were built, shipped and withdrawn by the same owner in the same environment | That an on-demand mutation engine would fail the same way. It would not, except in its two full-tree-traversal duties |
| A shipped product can deliberately have no task board and no index | That TFW Full can. Iterations 1-2 found real cold-start value in the board (S15, D1, D2), and Assisted's `work/<ID>/` names carry date + slug, which TFW's `tasks/TFW-N__slug/` also do |

---

## Checkpoint

| Found | Remaining |
|---|---|
| Four of the six engine responsibilities dissolve with a change of grammar; the two that survive are served by `git`, a hash utility and a generator that already has a sibling in the repository (E1) | Whether any *other* scenario needs code — Challenge must hunt for it honestly |
| `status.yaml` as specified **adds** a duplicate write rather than removing one, so it fails its own §7.1 test at nine fields and passes at six or seven (E2) | — |
| Floor = 51 modified / 1–53 new. Draft = 92–111 modified / 82–143 new. Budgets are 30 / 15. The coordinator's ≥98 / ≥67 are confirmed as conservative (E3) | Whether per-task migration output counts against `max_new_files` — §7.1 says byte copies are not silently excluded, which suggests yes |
| 59 % of the floor is adapter copies; subtraction takes the phase from ~3.4× to ~1.7× over budget but cannot bring it inside (E3) | A separate decision the TS cannot avoid: reduce fan-out, or get an evidenced owner ruling under DoF-12 |
| The `.git` claim is documented by Git itself, and the same source is stricter than the draft's conclusion — G-B is not a Git-supported configuration either (E4, E8) | Reproduction is impossible here: no state-changing Git command may be run |
| The identity subsystem's only forced element is a machine-local binding + preferences file, and the reason is sync-visibility, not Git (E4, E5) | — |
| Three of the draft's central justifications are circular (E6) | — |

**Sufficiency:**
- [x] External source used? — Git FAQ (PS), Google Drive documentation (PS)
- [x] Briefing gap closed? — all three guiding questions answered at analysis level
- [x] Configuration Space built from Gather dimensions? — eight configurations across seven dimensions,
      including P2, which no prior iteration had

**Metacognitive check.** New, not confirmed: D-III alternative B (one file per event) was never on any
prior iteration's table, and it is the single change that dissolves the largest block of machinery.
Also new: the budget problem is mostly duplication, not architecture — I expected the engine to be the
cause and it is not. Not yet checked: whether one-file-per-event survives the 100-event long-task case
that produced the rollover requirement, and whether it survives a provider that renames on conflict.
Challenge must attack both.

Stage complete: YES
→ User decision: coordinator gate — proceed to Challenge
