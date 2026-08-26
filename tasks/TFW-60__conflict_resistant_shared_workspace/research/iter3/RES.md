# RES — TFW-60: Phase A Task State & Coordination — Iteration 3 (Subtraction)

> **Date**: 2026-08-26
> **Author**: Researcher (Claude Opus 5)
> **Status**: 🔬 RES — iteration 3 complete
> **Parent HL**: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md) — 🔒 FROZEN 2026-08-26
> **Mode**: Pipeline · deep (`loops_per_stage: 3`)
> **Predecessors**: [Iteration 1 RES](../iter1/RES.md) · [Iteration 2 RES](../iter2/RES.md) and all their stage traces
> **Object under attack**: [`phase-a/HL__phase-a__task_state_and_coordination.md`](../../phase-a/HL__phase-a__task_state_and_coordination.md) — 585 lines, 📝 DRAFT, uncommitted
> **Stage files**: [1_briefing.md](1_briefing.md) · [2_gather.md](2_gather.md) · [3_extract.md](3_extract.md) · [4_challenge.md](4_challenge.md)

---

## Research Context

Iterations 1 and 2 closed C1-R2 as sufficient, and that verdict stands for everything they examined.
Iteration 3 attacks what they did not: two mechanisms the Phase A draft made mandatory *after* iteration 2
closed — a deterministic local state engine with an agent-only `tfw-status` skill (§11 S24, S27), and a
participant/device identity subsystem with a machine-local TFW home (§11 S28, S29). Measured across all
ten predecessor files, both appear **zero** times.

The default verdict was removal. The iteration gained one evidence source no predecessor had: a shipped
Assisted v1.4 starter running inside a live Google Drive for desktop mount, alongside three earlier
versions of itself — which turns out to be a natural experiment on exactly the question under test,
because the earlier versions shipped the engine and v1.4 withdrew it.

### Evidence boundary

Classes carried forward from iteration 2 unchanged. Nothing heuristic or fixture-based is relabelled.

| Class | What iteration 3 established | What it does not establish |
|---|---|---|
| **PS — primary source** | [Git FAQ](https://git-scm.com/docs/gitfaq) states directly that a cloud syncing service must not sync *any portion* of a Git repository, and that a shared working tree is safe only for a single user across all machines. Google documents stream/mirror selection and folder-level selective sync only | That Git fails in a specific observed instance |
| **PR — provider runtime** | **First PR evidence any iteration has had, and it is narrow.** Two Drive for desktop virtual mounts, clients 129.0.1.0 and 130.0.2.0; a shipped starter on the streamed `H:` mount; `desktop.ini` in **18 of 18** directories including dot-directories, with the client version embedded in the body; no `.git` anywhere; nested subfolders cannot be excluded from sync | Offline fork, reconnect, conflict-copy naming, two-device reconciliation. The folder holds no active task and no second device is reachable |
| **RR — repository/runtime** | Zero-occurrence claim verified by grep; 60 board rows / 52 task directories; adapter amplification measured by `md5sum` at 3 identical bodies per canonical workflow and 2 per Codex skill; `.git` census of 5 444 files / 1 163 directories / 33 MB; TFW-49 post-mortem, D24, D58, TFW-54 DoD-14/DoF-2 | A completed migration; any behaviour of Git versions other than 2.42.0.windows.1 |
| **DF — deterministic fixture** | None built this iteration. Predecessor fixtures are cited, not re-run | — |
| **FA — fresh agent** | None run this iteration | — |
| **UH — usability heuristic** | The field product's zero-index, zero-board discovery route was read, not observed in use | — |
| **NH — non-technical human** | **Not observed. Not available to this iteration.** | Remains a mandatory Phase-A acceptance obligation, exactly as iteration 2 left it |

**Method limits, declared.** The mandate forbids state-changing Git commands, because master HL §2.1
risk F1 records that two sessions sharing one index already produced a misattributed commit. No throwaway
repository could therefore be created inside a Drive folder and observed failing. Every Git finding rests
on primary documentation plus a read-only census. Where a consequence is inferred from a PR observation
rather than observed, it says so and names what would confirm it.

## Briefing

See [1_briefing.md](1_briefing.md). Deep mode, coordinator-set mandate: subtraction is the default
verdict; every finding is measured against the original pain in master HL §§1-2 and S1, not against the
elegance of the mechanism; frozen sections stay frozen; the scope budget `30 / 15 / 30 / 3000` is a
research input. All four stage gates were written before reporting and accepted by the coordinator.

## Decisions

| # | Decision | Rationale |
|---|---|---|
| **D1** | **Recommend P2 — "grammar-first subtraction" — as the Phase A configuration.** Short task-local status control (6-7 fields, no `last_event_id`, no `journal_head`); `journal/<UTC-ms>__<kind>.md`, one file per event; lifecycle skills write; single-writer enforced by a verified blocking session-name gate; `tasks/INDEX.md` produced by a build-time generator; `people/<handle>.md` plus **one** machine-local file per project; Git unchanged from iteration 2 | P2 survived all twelve pairwise consistency checks and a seven-way direct attack. It is a refinement *within* the C1-R2 survivor family, not a resurrection of an eliminated one: a separate snapshot is kept, so no replay (C4 stays dead), and history is not in the snapshot's conflict domain (C5 stays dead). Challenge C3, C8 |
| **D2** | **The deterministic state engine and the `tfw-status` mutation interface are not required and should not ship.** Four of the six responsibilities the draft assigns to executable code dissolve when the carrier grammar changes; the two that survive are served by `git`, an ordinary hash utility, and a generator of the same class as the `gen_docs.py` this repository already ships | Extract E1 tests all six one by one. Master HL §7.1 admits no new artifact that cannot name the duplicate write it removes; five P0 components cannot, and `status.yaml` at nine fields *adds* one. Extract E2, Challenge C7 |
| **D3** | **`last_event_id` and `journal_head` are removed from the status control.** They duplicate journal facts, and that duplication is the sole source of the cross-file transaction, the event-first/snapshot-second ordering rule and the six-way reconciliation matrix | S24's second complaint — *"synchronizing two files from memory"* — is self-inflicted by the schema, not imposed by the pain. Iteration 1 D11 already established that no provider offers a cross-file transaction; storing a journal fact in the snapshot manufactures a two-file commit on a substrate that has none. Extract E1 R2c, E6 |
| **D4** | **Event identifiers are UTC timestamps with millisecond precision; on collision take a new actual timestamp.** No allocator, no monotonic counter, no read-max-then-increment | S24's first complaint — *"manually allocating event IDs"* — exists only because a monotonic counter was chosen. The shipped field product allocates task identifiers exactly this way, and the withdrawn v1.3 hook already wrote its own event log as one file per event named with a millisecond stamp. Gather G3, G5; Challenge C3 |
| **D5** | **Single-writer enforcement is structural, not executable: extend TFW's existing Step-0 session naming into a verified blocking gate.** A stage may not begin until the session carries exactly `Role \| Task-ID \| Phase` and the rename has been verified | This is the field product's mechanism, and TFW half-has it already — `plan.md`, `handoff.md` and `review.md` carry *"Name this session"* today. It is enforced by an operation with an observable result rather than by a rule the agent must remember, and it makes a second concurrent writer visible in the environment's own session list. Gather G4; Challenge C8. Gap: only 3 of 13 workflows carry it, it is never verified, and nothing blocks on it |
| **D6** | **Two pieces of code are genuinely required, and neither is a state engine:** a build-time `tasks/INDEX.md` generator, and a one-shot migration resolver. Both are derived/non-authoritative, both are off the normal-transition path, both fail safe when absent | An agent cannot reproducibly render 60 rows twice, and cannot do 111-item exact accounting without silent error. `docs/scripts/gen_docs.py` already establishes the class. Challenge C1 scenarios 7-8 |
| **D7** | **The identity subsystem reduces to `people/<handle>.md` plus one machine-local file per project** holding the bound profile handle, a pointer to private preferences and the three Git paths. `device_instance_id`, `device.yaml`, the three-OS home tree and the derived observed-instance report are removed | The field model already delivers the owner's stated need in S28. The one genuinely new thing the draft found is that a *gitignored* file is still synchronized — `.user_preferences.md` is in this repository's `.gitignore` and Drive would replicate it to every participant — so private preferences must leave the project. That forces one file, not a home. Extract E5; Challenge C4 |
| **D8** | **No shared device registry, and no derived observed-instance report.** The draft's refusal of the registry is correct and should stand; the report should go with it | A shared mutable device list is DoF-1, DoF-2 and DoF-4 in one artifact, plus a privacy surface against `knowledge/constraint.md` F1 and a false-authentication invitation against D59. The report is a project-wide derived aggregate admitted with no §7.1 answer. Challenge C4 |
| **D9** | **H7's premise is confirmed, not refuted, and the correction runs the other way: the primary source is *stricter* than the draft's conclusion.** Keep "no `.git` directory or gitfile in the sync root"; keep the machine-local Git paths; keep G-B as a topology; stop calling it *supported*; keep G-A optional and Full-only and stop describing it as an upgrade; keep L3, which is now better motivated | The Git FAQ names the corruption classes directly, so the claim is documented, not folklore. The same paragraph says a shared working tree is safe *"only… if it will only be used by a single user across all machines"* — which a multi-participant Drive worktree is not. Removing `.git` removes the object/ref class; the residual is an index whose cached stat data describes a worktree another machine changed underneath it, and L3's post-staging drift recheck is exactly the control for it. Extract E4; Challenge C6 |
| **D10** | **Cite the Git FAQ.** The draft cites Google's stream/mirror pages for a proposition Google does not state, and does not cite the one source that states it directly | Provenance discipline. `.tfw/README.md` NS2-2 and the project's Honesty value both apply. Gather G8 |
| **D11** | **Add `desktop.ini` to `.gitignore`.** On the observed Drive behaviour a worktree in the sync root gains ≈1 189 untracked files — one per directory — rewritten en masse on every Drive client upgrade, because the client version is embedded in the file body | Direct PR observation: 18 of 18 directories carry one, including `.agents/`, `.codex/hooks/` and every nested skill directory. This is a staging-noise and L3-scope risk, not a corruption risk, and no architecture closes it. One line does. Gather G2; Challenge C6 |
| **D12** | **The scope-budget problem is mostly adapter duplication and is orthogonal to the architecture.** Even the *floor* — the smallest change after which a normal transition stops writing root `README.md` — measures 51 modified files against a budget of 30, and 30 of those 51 (59 %) are adapter copies | Measured: `.claude/commands/tfw-X.md` and `.agent/workflows/tfw-X.md` are byte-identical to `.tfw/workflows/X.md` (md5 verified for plan, handoff, review, resume), and all 11 `.agents/skills/*/SKILL.md` are byte-identical to their `.tfw/adapters/codex/` sources. One canonical sentence costs 3 file writes; one touched command concept costs 5. `docs/scripts/` and `site/scripts/` are a second full duplicate pair. Subtraction moves the phase from ~3.4× to ~1.7× over budget; it cannot bring it inside. Extract E3; Gather G10 |
| **D13** | **The highest-value uncontrolled collision in TFW is the task identifier itself, and the draft leaves it in place.** `id_format: "{prefix}-{seq}"` with `plan.md` Step 4.1 reading the project maximum is read-max-then-increment across the whole project — the exact operation S24 objects to for event IDs, at higher stakes, at task creation | Two participants working offline in one synchronized folder both create `TFW-61`; on reconnect two directories claim one identity. The draft's engine is scoped to a task root it is handed, not to the namespace, so it does not close this. Neither predecessor iteration raised it: their migration census found *"zero duplicate identities"*, which is a statement about history, not about concurrency. Challenge C2 |
| **D14** | **One amendment proposal is required** — extend the frozen DoD to cover task-identity allocation under concurrency. Everything else this iteration recommends lands in free sections or in the unapproved Phase A draft | Phase A can satisfy every current DoD item and still produce two `TFW-61` directories after a reconnect. That is a gap in the frozen acceptance set, not a refinement of it. See Amendment Proposals A1 |
| **D15** | **Iteration 3's findings do not reopen C1-R2 and do not contradict iterations 1-2.** D1-D16 of iteration 1 and D1-D14 of iteration 2 stand except where noted: iteration 2 D3 (nine required fields) is narrowed to 6-7 by D3 above, and iteration 2 D7 (numbered segments, count/byte/summary ceilings) is superseded for the count and byte ceilings by D1 above | Both predecessor decisions were reached inside a configuration space that did not contain one-file-per-event. Neither was defended on grounds that survive that alternative. The summary-length bound survives as a convention |
| **D16** | **Research is SUFFICIENT.** The remaining unknowns are acceptance evidence, not research questions | NH, real provider offline/reconnect, adapter session-rename capability and a populated Assisted corpus cannot be manufactured by another local research pass. They were already TS/RF obligations before this iteration and remain so. See Iteration Status |

### Predecessor decision disposition

| Iteration-1/2 decision | Disposition | Iteration-3 result |
|---|---|---|
| iter1 D1, D2, D3 · iter2 D1, D2 | **Confirmed** | Layer separation and the permanent-router + persisted-derived-index hybrid survive. P2 is a refinement inside the C1-R2 family |
| iter2 D3 (nine required `status.yaml` fields) | **Narrowed** | Six or seven. `last_event_id` and `journal_head` duplicate journal facts and are the sole cause of the cross-file transaction (D3) |
| iter1 D7, D8 · iter2 D7 (numbered segments, combined count + byte rollover) | **Superseded in part** | One file per event removes the need for segments, sealing, the digest chain, rollover and the count/byte ceilings. The closed event vocabulary, reference-first records and the summary-length convention survive unchanged (D1) |
| iter1 D9 (event-first / snapshot-second ordering) | **Superseded** | Ordering exists to sequence a two-file write that no longer occurs (D3) |
| iter1 D6 · iter2 D6 (one writer, `owner_epoch`, recovery) | **Confirmed, mechanism changed** | One writer survives and is enforced structurally by the session-name gate rather than by an engine's epoch check (D5). `owner_epoch` survives as a field |
| iter1 D13, D14 · iter2 D8, D9 (G-B, optional G-A, L3, exact-path staging) | **Confirmed, better cited, one word withdrawn** | Keep the topology and L3; cite the Git FAQ; stop calling G-B *supported* (D9, D10) |
| iter1 D12 · iter2 D10 (exact-accounting compatibility migration) | **Confirmed** | And it is one of the two places where code is genuinely required (D6) |
| iter1 D15 · iter2 D12 (eliminated families stay closed) | **Confirmed** | C2-C5, G-C, on-demand-only, timestamp recovery, service/database authority all remain eliminated. D-III B is a new alternative inside the surviving family, not a resurrection (Challenge C3) |
| iter1 D16 · iter2 D14 (no frozen amendment required) | **Revised** | One is now required, for a gap neither iteration examined: task-identity allocation under concurrency (D13, D14) |

## Open Questions

| # | Question | Status | Answer |
|---|---|---|---|
| **Q1** | Does the owner in fact require byte-identical control records across Codex, Claude Code, Cursor and Antigravity? | **Open — decision, not research** | This is the one requirement only a shared implementation serves, and it is what S24's word *"homogeneous"* may be reaching for. No frozen DoD item asks for it: DoD-2 asks for one normal writer per file, which is an ownership property, not a byte property. If the owner does want it, it is a new requirement and belongs in §12 |
| **Q2** | Does the task-identity grammar change to a timestamp, or gain a reservation rule? | **Open for the owner via A1** | Either closes D13. A timestamp matches the field product and needs no coordination; a reservation rule preserves the readable `TFW-N` shape at the cost of a protocol. Renaming 52 existing directories is not on the table — DoD-10 and §7 P4 forbid it — so any change applies to new tasks only |
| **Q3** | Can every supported adapter rename and verify its own session? | **Open for TS evidence** | D5's blocking gate depends on it. Codex demonstrably can. TFW's own Step 0 assumes the others can and never verifies it. If an adapter cannot, that adapter needs a different observable-result gate, not a waiver |
| **Q4** | Does Phase A get an owner budget ruling, a split, or a reduction in adapter fan-out? | **Open — unavoidable, whatever the architecture** | 51 modified at the floor against a budget of 30. DoF-12 makes crossing without an exact count and an explicit evidenced ruling a failure condition. Reducing the fan-out is a framework-structure change that arguably belongs to its own task |
| **Q5** | Is a read-time validator worth its cost (configuration P3)? | **Open — coordinator judgement** | P3 is the unexpected survivor. It concedes the one residual R1 leaves — an agent typing `lifecycle: activ` — without a mutation path, without an availability failure mode and at a fraction of P0's cost. A one-line convention that readers fail closed on unrecognised values is the cheaper alternative |
| **Q6** | What replaces the tamper-detection the digest chain provided? | **Answered, with a stated cost** | Nothing, and the draft already declines to claim it: *"It does not make the log tamper-proof against a writer who can replace the entire chain."* One file per event trades chain-based detection of accidental rewrite for structural impossibility of torn append. Deletion shows as a gap; silent single-file rewrite becomes undetectable. Recorded as a real loss (Challenge C3) |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|---|---|---|---|
| **H5** | No executable code is required. A strict skill invoked by a slash command, plus a carrier grammar that needs no ID allocation, no cross-file transaction and no chain verification, produces homogeneous records without a deterministic state engine | needs-research | ❌ **REFUTED AS STATED · ✅ CONFIRMED IN SUBSTANCE** | *Refuted:* two scenarios require code — reproducibly rendering 60 task folders into one index, and 111-item exact migration accounting. *Confirmed:* no deterministic state engine and no mandatory mutation interface are required. Four of the six responsibilities the draft assigns to code dissolve when the grammar changes (E1); the two that survive are served by `git`, a hash utility and a build-time generator of the class this repository already ships. The two required pieces are derived, off the transition path and fail safe when absent (D6). The engine's stated justification is circular in three places (E6). Corroborating and independent: the same owner built the engine, machine-local home, binding and machine-local event log — 738 lines, two implementations — shipped them in three starter versions and **withdrew them in v1.4** because on a real large folder the check exceeded its own 30-second timeout and could hang without reporting (G5); TFW-49's owner verdict rejects this exact component list (G6); `KNOWLEDGE.md` D24 states *"No scripts — AI agent is the sync engine"*; TFW-54 froze DoF-2 naming *"TFW-49's cause of death"*. Counter-evidence recorded, not suppressed: cross-agent byte-identity is a real requirement only an engine serves, and no frozen DoD asks for it (C5) |
| **H6** | The declared Phase A outcome is reached by removing and reclassifying existing artifacts rather than adding a state engine, `people/` and a machine-local TFW home. The baseline is the smallest repository change that stops two tasks colliding in root `README.md` | needs-research | 🟡 **PARTIALLY CONFIRMED — the subtraction is large and real; the budget still does not close** | Floor measured at **51 modified / 1-53 new**; draft measured at **92-111 modified / 82-143 new**; budgets are 30 / 15 (E3). The coordinator's working figures of ≥98 and ≥67 are confirmed as conservative — both sit inside the derived ranges. Subtraction removes ~41-60 modified and ~75-134 new files and the entire engine LOC budget, moving the phase from ~3.4× to ~1.7× over budget. But **the floor already exceeds the budget**, and 59 % of it is adapter copies: one canonical workflow sentence costs 3 byte-identical file writes, one command concept costs 5, and the doc generator exists twice (D12). The budget problem is duplication, not architecture, and no carrier choice substitutes for a fan-out reduction or an evidenced owner ruling. Also: the pure floor (P7) violates frozen DoD-3, so it is a measuring stick, not a candidate — the shippable minimum is P2 |
| **H7** | The set of things that must live outside the synchronized project folder is smaller than the draft claims, and part of that draft rests on untested folklore — starting with the claim that a synchronized `.git` breaks | needs-research | ❌ **REFUTED FOR GIT · ✅ CONFIRMED FOR IDENTITY · with an inversion** | *Refuted:* the `.git` claim is documented by Git's own FAQ — *"It is important not to use a cloud syncing service to sync any portion of a Git repository… missing objects, changed or added files, broken refs"* — and reinforced by direct PR observation that Drive writes into 100 % of directories including dot-directories and cannot exclude nested subfolders. Not folklore. *The inversion:* the same paragraph is **stricter than the draft's conclusion**. A shared working tree is safe *"only… if it will only be used by a single user across all machines"*, which a multi-participant Drive worktree is not. Removing `.git` removes the object/ref class; it does not make G-B a Git-supported configuration. The residual is index/worktree staleness, and L3's post-staging drift recheck is exactly its control — so L3 gains motivation while the word *supported* must go (D9). *Confirmed for identity:* only two things are genuinely forced out for identity — the current-participant binding and private preferences — and the reason is sync-visibility, not Git: a gitignored file is still synchronized. `device_instance_id`, `device.yaml` and the three-OS home tree are not forced out by anything (E4, D7) |
| **H8** | Session-start participant recognition, private-device binding and multi-person transparency are reached through the existing Assisted `people/<handle>.md` model plus a minimal addition, without a Phase A identity subsystem. Whether a device registry is needed at all is part of the hypothesis | needs-research | ✅ **CONFIRMED** | The shipped field model delivers the owner's stated S28 need exactly: one profile → silent selection; several → private-device binding; new, shared, copied or mismatched device → **one** short question before the first authorship write; `automation:<name>` separate; *"общего файла текущего пользователя в проекте нет"*; and explicitly *"не аутентифицирует человека и не подтверждает полномочия."* The minimal addition is **one** machine-local file per project. `device_instance_id` fails its own test — the draft concedes it authorises nothing, travels with a copied home and *"cannot be detected reliably"* — and buys only automatic detection of a rare case the one-question fallback already handles. The device registry is refused, correctly, and the derived observed-instance report should go with it: it is a project-wide aggregate admitted with no §7.1 answer (E5, C4). Independent corroboration: this subsystem was **already built** in the v1.3 hook — machine-local home at `%LOCALAPPDATA%\TFW-Assisted\<sha256-prefix>\`, `actor.txt` binding, profile enumeration, single-profile silent selection — and withdrawn with it; v1.4 kept the policy in prose and dropped the machinery (G5). Independent again: TFW-54's own draft concluded *"no journal, no new file"* and froze *"Nothing executable is added"* for multi-agent teaming |

## HL Update Recommendations

> The researcher classifies. The researcher never applies.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|---|---|
| **R1** | §10 Hypotheses | Set H5 → `final: refuted as stated, confirmed in substance — no state engine and no mutation interface; two narrow non-authoritative scripts are required`; H6 → `final: partially confirmed — subtraction removes ~41-60 modified and ~75-134 new files, but the floor itself is 51 modified against a budget of 30 and 59 % of it is adapter duplication`; H7 → `final: refuted for Git (documented, not folklore) and inverted — the source is stricter than the draft; confirmed for identity`; H8 → `final: confirmed — people/<handle>.md plus one machine-local file per project` | Iteration 3 Hypotheses table |
| **R2** | §10 Research Result | Add an iteration-3 paragraph: the subtraction pass recommends P2; the engine, `tfw-status`, `.tfw/task_state.md`, `.tfw/workflows/status.md`, both JSON schemas, `device_instance_id`, `device.yaml`, the three-OS TFW home and the observed-instance report are recommended for removal; `status.yaml` narrows to 6-7 fields; the journal becomes one file per event | D1-D8 |
| **R3** | §10 Blind Spots | Add: *"Is the task identifier itself a shared counter, and does Phase A leave the highest-value collision uncontrolled while automating a cheaper one?"* | D13 |
| **R4** | §7.2 Knowledge Citations | Add a row for [Git FAQ](https://git-scm.com/docs/gitfaq) — *a cloud syncing service must not sync any portion of a Git repository; a shared working tree is safe only for a single user across all machines* → applies to: no `.git` in the sync root is documented, and G-B is a topology TFW chooses, not a configuration Git supports. Annotate the existing Google Drive rows as evidence-environment citations that do not state the Git proposition | D9, D10 |
| **R5** | §7.2 Knowledge Citations | Add rows for the in-repo precedent already in PV: `KNOWLEDGE.md` D24 (*"No scripts — AI agent is the sync engine"*), D55/TFW-50 (one Markdown rule, no runtime), D58 (Assisted hooks do not durably dispatch; the proven mode is manual), and the TFW-49 post-mortem owner verdict | G6, G7 |
| **R6** | §9 Risks | Add four risks with controls: (a) **task-ID collision under concurrency** — two offline participants both create `TFW-61`; control = A1 verdict; (b) **`desktop.ini` staging noise** — ≈1 189 untracked files in a Drive-hosted worktree, mass-rewritten on client upgrade; control = one `.gitignore` line; (c) **index/worktree staleness** — an index whose cached stat data describes a worktree another machine changed; control = L3 post-staging drift recheck; (d) **budget overrun is structural** — the floor is 1.7× over `max_modified_files` because of adapter duplication; control = evidenced owner ruling under DoF-12, or a fan-out reduction in its own task | D11, D12, D13, C6 |
| **R7** | §2 Current State | Refresh the measured surfaces: 60 board rows and 52 task directories today; 48 files mention the Task Board outside `tasks/`; adapter amplification measured at 3 byte-identical bodies per canonical workflow and 2 per Codex skill; `docs/scripts/` and `site/scripts/` are a second full duplicate pair; the doc generator's board parser hardcodes the `TFW-\d+` prefix and reads column 3 positionally | G10 |
| **R8** | §8 Dependencies | Record that `editions/02-assisted/` is at v1.0 while the shipped field artifact is v1.4 with four skills and no hooks, and that **no populated Assisted corpus exists anywhere reachable** — all four field starters are unused templates with no `work/` directory and no participant profiles. Any Phase A claim about an Assisted profile is currently written against a stale in-repo model, and the *"populated Assisted corpus when available"* migration obligation is unmeetable today | G11 |
| **R9** | §11 Strategic Insights | Annotate **S24, S27, S28 and S29** with the iteration-3 evidence rather than deleting them — they record owner intent and §12 discipline does not apply to a free section, but overriding recorded owner intent silently would be wrong. **The coordinator must surface the disposition to the owner as an explicit decision even though the amendment channel does not apply here.** Add new rows S30-S33 (below) | D2, D3, D4, D7, D8 |

**Proposed new §11 rows** (free section; the coordinator assigns final numbers):

| # | Insight | Category | Source |
|---|---|---|---|
| S30 | The owner's own product already ran this experiment: the deterministic engine, the machine-local home, the participant binding and a machine-local event log shipped in Assisted 1.0/1.2/1.3 and were withdrawn in 1.4 because on a real large folder the check exceeded its own timeout and could hang without reporting. **Implication:** field evidence about deterministic local machinery over a synchronized tree exists and is negative; it transfers specifically to the two duties that must traverse the whole tree — index generation and migration accounting | environment | [RES 3](RES.md) G5; `innoforce_starter_v1.4/CHANGELOG.md` |
| S31 | Two of the draft's central justifications are produced by the carrier grammar rather than by the pain: a monotonic event counter creates the allocator problem, and storing `last_event_id` in the snapshot creates the cross-file transaction. **Implication:** the mechanism must be justified on grounds that survive a grammar change, or the grammar should change | philosophy | [RES 3](RES.md) E1, E6 |
| S32 | The highest-value uncontrolled collision in TFW is the task identifier itself — `{prefix}-{seq}` is read-max-then-increment across the whole project. **Implication:** Phase A can satisfy every DoD item and still produce two `TFW-61` directories after a reconnect; automating the event counter while leaving the task counter is the wrong order | risk | [RES 3](RES.md) C2, D13 |
| S33 | The scope-budget overrun is duplication, not architecture: one canonical workflow sentence costs three byte-identical file writes and one command concept costs five, so even the minimum Phase A is 1.7× over the modified-files budget. **Implication:** no carrier choice fixes it; it needs an evidenced owner ruling or a fan-out reduction, and the latter probably deserves its own task | constraint | [RES 3](RES.md) E3, D12 |

### Amendment Proposals — frozen sections, owner verdict required

> One proposal. Everything else this iteration recommends lands in a free section or in the unapproved
> Phase A draft, which is not a contract.

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|---|---|---|---|---|
| **A1** | §5 DoD | `EXTEND` | Add a DoD item: *"Task identity is allocated without a project-wide shared counter. Two participants working offline in one synchronized tree cannot create two task directories claiming the same identity; on reconnect, either no collision is possible by construction or the collision is detected and resolved without renaming an existing task path."* | `.tfw/project_config.yaml` `id_format: "{prefix}-{seq}"` and `plan.md` Step 4.1 read the project-wide maximum to allocate the next ID — read-max-then-increment across the whole project, the exact operation S24 objects to for event IDs, at the highest-value moment. The draft's engine is scoped to a task root it is handed, not to the namespace, so it does not close this. The shipped Assisted product removed the counter deliberately: `ID = YYYYMMDD-HHMMSS__slug`, collision resolved by taking a new actual timestamp, allocation performed by an atomic create-if-absent. Neither predecessor iteration raised it — their census found *"zero duplicate identities"*, which describes history, not concurrency ([RES 3](RES.md) C2, D13) | Two options, both real. **(a) Timestamp identity for new tasks:** loses the short readable `TFW-N` and every human habit built on it; 52 existing directories keep their paths, so the project carries two ID grammars permanently. **(b) Reservation rule:** keeps `TFW-N`, adds a protocol step at task creation and does not fully close the offline case. Either way the phase gains scope it does not have today, against a budget already exceeded | **Do nothing** — rejected: the contract would be fully satisfiable while the defect it exists to remove persists at the most visible point in the system, and a duplicate task identity is worse than a duplicate event ID because paths, links and the Task Board all depend on it. **Defer to a later phase** — rejected: Phase B and C both create tasks and would inherit it, and §4 sequences them after A. **Handle it in the Phase A TS without a DoD item** — rejected: a TS cannot add an acceptance obligation the frozen DoD does not carry, and reviewers verify against the contract, not the TS (`conventions.md` §14) |

## Fact Candidates

> Pure reporting. These are not verified facts until `/tfw-knowledge` consolidation.

| # | Category | Candidate | Source | Confidence |
|---|---|---|---|---|
| FC1 | environment | The owner runs two Google Drive for desktop virtual mounts on the working machine (`G:` personal, `H:` `saubakirov@innoforce.kz`), with clients 129.0.1.0 and 130.0.2.0 running simultaneously. TFW field artifacts live on the streamed `H:` mount | [RES 3](RES.md) G2 | ★★★ |
| FC2 | environment | Google Drive for desktop writes a `desktop.ini` into **every** directory of a synchronized tree, including dot-directories, and embeds the client version in the file body — so a client upgrade rewrites one file per directory. Observed at 18 of 18 directories, zero misses | [RES 3](RES.md) G2 | ★★★ |
| FC3 | environment | The shipped Assisted v1.4 starter contains no `.git` directory, and neither do versions 1.0, 1.2 or 1.3. Four TFW skills operate in the folder with no repository present | [RES 3](RES.md) G2 | ★★★ |
| FC4 | process | Assisted v1.0/1.2/1.3 shipped `.codex/hooks.json` plus `tfw-hook.ps1` (361 lines) and `tfw-hook.sh` (377 lines) implementing a machine-local state home, a participant binding, status validation, a status census and a machine-local event log. v1.4 removed all three files. Stated reason: on a real large folder the `Stop` hook exceeded its own 30-second timeout and the check runner could hang without a full report | [RES 3](RES.md) G5; `innoforce_starter_v1.4/CHANGELOG.md` | ★★★ |
| FC5 | convention | The shipped Assisted contract prohibits three things by name: *"Не создавай общий task board, общий счётчик или `CURRENT_USER`"* — no shared task board, no shared counter, no current-user file | [RES 3](RES.md) G3 | ★★★ |
| FC6 | convention | Assisted allocates task identifiers as `YYYYMMDD-HHMMSS__slug` with no counter; on path collision it takes a new actual timestamp and never reuses or overwrites; allocation is performed by an atomic create-if-absent of the task directory | [RES 3](RES.md) G3 | ★★★ |
| FC7 | convention | Assisted enforces single-writer through session naming: a Codex task must be renamed to exactly `plan \| <ID>`, `handoff \| <ID>` or `review \| <ID>` and the rename verified, before reading the result or the sources. If the name cannot be established and verified, the stage is blocked | [RES 3](RES.md) G4 | ★★★ |
| FC8 | convention | Assisted status is one line in `work/<ID>/TRACE.md` (`new\|doing\|review\|done\|blocked`), and the management log is a `## Ход работы` section in the same file. There is no separate status carrier, no journal file, no index and no board. `active_task=none` is explicitly legal | [RES 3](RES.md) G3 | ★★★ |
| FC9 | context | `editions/02-assisted/` in this repository is at edition version 1.0 and still ships the three hook files. The shipped field artifact is v1.4 with four `.agents/skills/` contracts and no hooks | [RES 3](RES.md) G11 | ★★★ |
| FC10 | constraint | No populated Assisted corpus exists in any reachable location. All four field starters are unused templates with no `work/` directory and no `people/<handle>.md` profiles | [RES 3](RES.md) G11 | ★★★ |
| FC11 | convention | `.claude/commands/tfw-X.md` and `.agent/workflows/tfw-X.md` are byte-identical to `.tfw/workflows/X.md` once frontmatter is stripped (md5 verified for plan, handoff, review, resume), and all 11 `.agents/skills/*/SKILL.md` are byte-identical to their `.tfw/adapters/codex/` sources. `docs/scripts/` and `site/scripts/` are a second full duplicate pair | [RES 3](RES.md) G10 | ★★★ |
| FC12 | risk | `.gitignore` does not list `desktop.ini`, and this repository's worktree has 1 189 directories | [RES 3](RES.md) G9 | ★★★ |
| FC13 | context | Session naming is documented in the glossary as *"present in every TFW workflow"*, but it appears in only 3 of 13 canonical workflows (`plan.md`, `handoff.md`, `review.md`), is never verified, and nothing blocks on it | [RES 3](RES.md) G4, C8 | ★★★ |
| FC14 | risk | This repository's `.git` holds 5 444 files across 1 163 directories at 33 MB, with 5 201 loose objects, a 112 846-byte index, two linked worktrees, and `AUTO_MERGE`, `ORIG_HEAD` and a 147-file `lost-found/` present | [RES 3](RES.md) G9 | ★★★ |

## Strategic Insights (Research)

> Human-sourced domain knowledge with implications added.

| # | Category | Insight | Source | Confidence |
|---|---|---|---|---|
| **SS1** | philosophy | The owner ships the same methodology twice — once as this repository's Full edition and once as a Russian-language Assisted starter for non-technical colleagues — and the Assisted line is where the design gets tested against people who will not tolerate ceremony. **Implication:** Assisted is not a reduced Full; it is the honest field trial of every Full mechanism, and when Assisted removes something, that is data about the mechanism, not about the audience | Owner artifacts: four shipped starter versions in a live Drive folder | ★★★ |
| **SS2** | philosophy | The owner's stated position in the mandate is that a good skill suffices, and the instruction was explicit that this is a position to test rather than confirm. Testing it found the position **mostly right and wrong at the edges**: no state engine, but two narrow scripts. **Implication:** the useful boundary is not "code vs no code" but "code that owns state" vs "code that renders or migrates" — the first is authority, the second is a tool | Coordinator mandate; [RES 3](RES.md) C1 | ★★★ |
| **SS3** | process | The owner reversed a prior no-journal ruling (S5) and then, in the same review pass, reached for an engine to make the journal rigorous (S24). **Implication:** the journal requirement is genuine and frozen in DoD-3; the rigour requirement attached itself to a carrier choice. Separating them lets both be satisfied — the journal ships, the engine does not | Master HL §11 S5, S24; [RES 3](RES.md) E6 | ★★☆ |
| **SS4** | constraint | The owner asked whether a list of computers is useful, and answered it correctly in the same insight: only for diagnostics, and only if it never becomes identity or authority (S29). **Implication:** that instinct should be extended one step further — the diagnostic value has not been demanded by any scenario, so the derived observed-instance report should go too | Master HL §11 S29; [RES 3](RES.md) C4 | ★★☆ |

## Findings Map

**Causal chain — where the two contested mechanisms actually come from**

```
             ORIGINAL PAIN (master HL §1-2, S1)
   several humans and agents cannot advance different tasks
   because unrelated work converges on root README / TECH_DEBT / KNOWLEDGE
                              │
                              ▼
        iterations 1-2  →  C1-R2  →  strict status.yaml + separate journal
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
    chose monotonic event ID          chose to store last_event_id
       TFW-60-E0007                      inside the snapshot
              │                               │
              ▼                               ▼
      needs read-max-increment        needs a cross-file transaction
              │                               │
              ▼                               ▼
        needs an allocator            needs event-first/snapshot-second
              │                               │  + a 6-way recovery matrix
              └───────────────┬───────────────┘
                              ▼
                    S24: "a deterministic
                     state-transition engine"
                              │
                              ▼
        engine → tfw-status skill → 4 adapter copies
              → task_state.md → workflows/status.md
              → 2 JSON schemas → packaging → install lifecycle
              → machine-local home → device_instance_id

   ── cut here ──  change the two grammar choices and the chain has no root
```

**Priority matrix — what to remove, and how confident**

| | **Removes a lot** | **Removes a little** |
|---|---|---|
| **High confidence** | Deterministic state engine + `tfw-status` + 4 adapter copies + `task_state.md` + `workflows/status.md` + 2 JSON schemas · journal segments/sealing/digest chain/rollover · `last_event_id` + `journal_head` | `device_instance_id` · `device.yaml` · three-OS home tree · derived observed-instance report |
| **Lower confidence** | Reducing adapter fan-out — large saving, but it is framework structure and probably its own task | A read-time validator (P3) — cheap either way; a one-line reader-fails-closed convention may be enough |

**What survives untouched from iterations 1-2**

`tasks/INDEX.md` as a derived non-authoritative view · permanent README router · stable task paths ·
one normal writer per mutable file · `owner_epoch` as a field · closed event vocabulary · reference-first
events · exact-accounting compatibility migration · G-B baseline · optional Full-only G-A · L3 ·
every elimination (C2-C5, G-C, on-demand-only, timestamp recovery, service/database authority).

## Iteration Status

- **Iteration:** 3 of 2 (min) / 5 (max) — opened above `min_iterations` by coordinator decision
- **Hypotheses tested:** H5 (refuted as stated, confirmed in substance), H6 (partially confirmed),
  H7 (refuted for Git and inverted, confirmed for identity), H8 (confirmed)
- **Hypotheses deferred:** None. H1-H4 were closed by iterations 1-2 and were not reopened
- **Gaps discovered:**
  1. The task identifier is a project-wide shared counter and no frozen DoD item covers it (D13, A1)
  2. The scope budget cannot be met by any architecture — the floor is 51 modified against 30, and 59 %
     of it is adapter duplication (D12)
  3. `desktop.ini` is absent from `.gitignore`; a Drive-hosted worktree gains ≈1 189 untracked files
  4. Session naming is documented as universal and exists in 3 of 13 workflows, unverified and
     non-blocking (FC13)
  5. `editions/02-assisted/` is four versions behind the shipped artifact, and no populated Assisted
     corpus exists anywhere reachable — the migration obligation is currently unmeetable (R8)
- **Superseded decisions:** iteration 2 D3 narrowed by D3 (nine fields → six or seven); iteration 1 D7,
  D8 and iteration 2 D7 superseded in part by D1 (segments, sealing, digest chain, rollover and the
  count/byte ceilings become unnecessary); iteration 1 D9 superseded by D3 (nothing left to order);
  iteration 1 D16 and iteration 2 D14 revised by D14 (one amendment is now required)

### Open Threads (for next iteration)

> These are acceptance and decision threads, not research threads. None of them can be closed by another
> local research pass, which is why the recommendation below is SUFFICIENT.

| # | Thread | Why it matters | Suggested focus |
|---|---|---|---|
| 1 | NH — a genuinely non-technical participant browsing, interpreting and safely changing the control | Unchanged since iteration 1; mandatory under §7.1 and DoD-14. Every carrier decision is provisional until it exists | TS Evidence field; RF/EV must preserve errors and confusion, not only success |
| 2 | PR — real offline fork, reconnect, conflict-copy naming, two-device reconciliation | Iteration 3 supplied the provider *environment* and the provider-written *artifacts*, not the failure behaviour | A second device or a second account on the same Drive folder; record initial and final bytes plus conflict artifacts |
| 3 | Adapter session-rename capability | D5's blocking name gate is the replacement for the engine's ownership enforcement, and it is unverified outside Codex | One fixture per supported adapter; an adapter that cannot rename needs a different observable-result gate, not a waiver |
| 4 | Owner decision on byte-identical cross-agent records (Q1) | The only requirement an engine uniquely serves. If it is real, the whole subtraction case needs re-weighing | Ask directly; if yes, it is a §12 matter, not a Phase HL matter |
| 5 | Owner verdict on A1 and on the budget ruling (Q2, Q4) | Both block a compliant TS: one is a frozen-DoD gap, the other is a DoF-12 condition | Present together — they interact, because closing A1 adds scope to a phase already over budget |
| 6 | Adapter fan-out reduction | The single largest lever on the budget, and independent of TFW-60's subject | Likely its own task; TFW-57 (artifact growth control) is the nearest existing home |

### Recommendation

- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and revise the Phase A HL
- [ ] MORE NEEDED
- [ ] BLOCKED

**Reasoning.** The two mechanisms the iteration was opened to test are now examined, with primary sources,
first-ever provider-runtime observation, in-repository measurement and a field natural experiment in which
the same owner built, shipped and withdrew the very machinery under review. Every remaining unknown is an
acceptance obligation or an owner decision — a non-technical participant, a second synchronized device, an
adapter capability fixture, and two verdicts. None can be manufactured by another local research pass, and
iteration 2 reached the same conclusion about its own residue for the same reason.

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 3 was a subtraction pass against two mechanisms that entered the Phase A draft after research
closed and that no prior iteration had examined. It found that four of the six responsibilities the draft
assigns to executable code exist only because of two grammar choices — a monotonic event counter and a
`last_event_id` stored in the snapshot — and dissolve when those change; that the two remaining ones are
served by `git`, an ordinary hash utility, and a build-time generator of the class this repository already
ships; and that the participant subsystem reduces to the field-proven `people/<handle>.md` model plus one
machine-local file, because the only thing genuinely forced outside a synchronized folder for identity is
the fact that a gitignored file is still synchronized. The strongest evidence was not analytical: the same
owner built this engine and this machine-local home, shipped them in three versions of a starter running
in a real Google Drive folder, and withdrew them because on a real large folder the check exceeded its own
timeout and could hang — replacing them with prose and four skill contracts that are still in service.

What research provided that would otherwise have been missed: the withdrawal itself, which no artifact in
this repository records; the one-file-per-event alternative, which no prior configuration space contained
and which is what makes the largest block of machinery unnecessary; the task-identifier counter, the
highest-value shared counter in TFW, left untouched by a draft that builds an allocator for a cheaper one;
and the measurement that the scope-budget overrun is adapter duplication rather than architecture, so
subtraction improves it by half and cannot fix it.

Self-critique, in three parts. First, H5 as written is false and I have said so: reproducibly rendering
sixty task folders and doing 111-item exact accounting need code, and a subtraction pass that concluded
"no code at all" would have been telling the mandate what it wanted. Second, the strongest field evidence
is a *session hook*, not an on-demand engine, and the failure does not transfer cleanly — it transfers
only to the two duties that must traverse the whole tree, which are precisely the two duties I concede
need code; that pairing is uncomfortable and I have recorded it rather than smoothed it. Third, this
iteration ran no fresh-agent test and built no new deterministic fixture; it leans on primary sources,
one live provider mount, in-repository measurement and predecessor fixtures, and a reader should weigh
its recovery claims accordingly. The one thing the whole subtraction case would not survive is an owner
who genuinely requires byte-identical control records across four agent products — that requirement is
recorded as Q1, unanswered, and it is the honest counterweight to everything above.

---

*RES — TFW-60: Phase A Task State & Coordination — Iteration 3 (Subtraction) | 2026-08-26*
