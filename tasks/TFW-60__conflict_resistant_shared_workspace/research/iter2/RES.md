# RES — TFW-60: Phase A Task State & Coordination — Iteration 2

> **Date**: 2026-08-26
> **Author**: Researcher (Codex)
> **Status**: 🔬 RES — iteration 2 complete
> **Parent HL**: [HL-TFW-60](../../HL-TFW-60__conflict_resistant_shared_workspace.md) — 🔒 FROZEN 2026-08-26
> **Mode**: Pipeline · deep (`loops_per_stage: 3`)
> **Predecessor**: [Iteration 1 RES](../iter1/RES.md) and all [iteration 1 stage traces](../iter1/)
> **Stage files**: [1_briefing.md](1_briefing.md) · [2_gather.md](2_gather.md) · [3_extract.md](3_extract.md) · [4_challenge.md](4_challenge.md)

---

## Research Context

Iteration 2 independently attacked the iteration-1 Phase-A architecture rather than widening it by
preference. T1 tested a deterministic 100-task corpus and four catalogue conditions with context-free
agents, minimized the status schema and attacked strict YAML. T2 exercised ownership recovery,
event/snapshot ordering, malformed and duplicate events, rejected retention and journal rollover. T3
tested Git scope and attribution in temporary repositories, resolved the landing-order problem, and
accounted for the repository's current legacy/nonstandard task shapes without changing them. The
result is **C1-R2**, a refinement of C1-R. Debt and knowledge architecture remain out of scope.

### Evidence boundary

| Class | What iteration 2 established | What it does not establish |
|-------|-------------------------------|----------------------------|
| **FA — fresh agent** | Context-free Codex readers recovered authoritative state under normal, absent, stale and malformed index conditions | Non-technical-human comprehension or editing |
| **UH — usability heuristic** | A zero-command README → index → fixed-control file-browser route exists | Observed human behaviour |
| **DF — deterministic fixture** | The proposed validators, recovery rules, rollover and L3 evaluator produce reproducible local outcomes | Actual sync-provider ordering, conflict naming or reconnect behaviour |
| **RR — repository/runtime** | Current repository census and local Git 2.42.0.windows.1 behaviour | All Git versions/platforms or a completed migration |
| **PS — primary source** | Language, Git and vendor contracts define relevant syntax and failure classes | Runtime reproduction of a provider or third-party system |
| **NH — non-technical human** | **Not observed** | Remains mandatory acceptance evidence |
| **PR — provider runtime** | **Not observed** | Remains mandatory acceptance evidence under frozen HL §7.1 |

The strict-YAML profile is an application contract layered over [YAML 1.2.2](https://yaml.org/spec/1.2.2/),
which also supports anchors, aliases and tags that C1-R2 deliberately rejects. Git landing relies on
official path, trailer and reachability contracts: [git-rev-parse](https://git-scm.com/docs/git-rev-parse),
[git-interpret-trailers](https://git-scm.com/docs/git-interpret-trailers),
[git-log](https://git-scm.com/docs/git-log), and
[git-merge-base](https://git-scm.com/docs/git-merge-base). Local Git evidence directly covers only
2.42.0.windows.1; current published documentation may describe newer releases. Google Drive, OneDrive
and Dropbox documentation was used only to identify documented failure classes, never as PR evidence.
Likewise, current Spec Kit, OpenSpec, BMAD and GSD Pi sources are comparisons, not executed guarantees.

## Briefing

See [1_briefing.md](1_briefing.md). The Coordinator approved deep mode and three adversarial evidence
threads, required explicit disconfirmation, and prohibited relabelling FA/UH/DF as NH/PR. Gather,
Extract and Challenge were each completed through three loops and accepted at their WAIT/STOP gates.
The final direction was to synthesize C1-R2, translate survivor invariants into Phase-A TS acceptance
recommendations, classify every HL update and stop after a research-only commit.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| **D1** | **Recommend C1-R2 as the Phase-A architecture.** It combines a permanent hybrid router/index, strict task-local status authority, a segmented reference-first journal, event-first recovery, L3 Git landing, G-B with optional pinned G-A, and a compatibility resolver | The configuration survived all local discovery, schema, recovery, rollover, landing, Git-preflight and migration attacks. No counter-evidence defeated its authority/projection/journal/Git separation |
| **D2** | Keep a permanent low-churn root router and persisted, rebuildable, explicitly derived `tasks/INDEX.md`; every acting reader re-reads the selected task's authority | All four FA readers recovered state, but an absent view shifted substantial classification work to the reader. A derived view may be absent, stale or malformed without changing task truth; on-demand-only still lacks NH evidence for zero-command portfolio discovery |
| **D3** | The universally required `status.yaml` core is exactly nine fields: `schema_version`, `task_id`, `goal_summary`, `value_summary`, `lifecycle`, `state_owner`, `owner_epoch`, `last_event_id`, and `journal_head` | Removing each field broke the first named shared reader or recovery invariant. No tenth field had a universal reader. The schema rejects unknown fields and unsupported versions before action |
| **D4** | Use state-dependent conditionals and closed edition profiles rather than making all metadata universal. Conditionals are `goal_ref`, `waiting_on`, `next_action`, `next_ref`, `terminal_outcome`, `terminal_ref`; profiles may add `workflow_stage`, `ownership_profile`, `roles`; `status_since` and `updated_at` are derived | Valid lifecycle/profile cases produced exactly one cold-start branch. Illegal combinations failed closed. This shrinks authority without letting editions redefine shared lifecycle meaning |
| **D5** | Strict YAML means a validator-owned application subset: unique keys; no anchors, aliases, merge keys, tags or directives; closed fields; bounded shapes; safe relative references; and dependency-visibility checks before action | Duplicate keys, extension features, unknown fields/versions, unsafe references, empty/partial/truncated content and missing referenced files all stopped. The `.yaml` extension itself supplies none of these guarantees |
| **D6** | Keep one normal writer at one `owner_epoch`, event-first/snapshot-second ordering and append-only corrections. Journal-ahead at the current epoch may be completed or compensated; snapshot-ahead, same-epoch divergence, malformed data and divergent duplicate IDs stop; stale epochs are preserved and quarantined | Deterministic fixtures produced one recovery or explicit stop without using timestamps as authority. This is detection/recovery, not a distributed lock, authentication system or provider guarantee |
| **D7** | Keep numbered immutable, reference-first journal segments with finite configured event-count, encoded-byte and summary-code-point ceilings. Retain every sealed segment, including rejected traces; select no default for 240 code points, 100 events or 32 KiB | Count alone does not bound Unicode records and code points do not bound storage. Combined first-hit rollover preserved order and all events; invalid/oversized cases stopped. The fixture supports the mechanism, not those numerical defaults |
| **D8** | Remove task-journal `landed`. Use **L3**: a pre-landing `handoff` records `landing_requested`, a normalized manifest/digest, exact paths, producer and landing owner; one commit contains the handoff plus results and matching trailers; exactly one reachable exact match on the pinned ref is derived landing completion | L3 avoids a future-hash cycle and a post-commit task edit. It recovers a commit after process loss and across rebase, while missing, changed, duplicate, unreachable, wrong-scope or wrong-attribution matches stop or remain not landed. Evaluation does not write status or journal |
| **D9** | Use **G-B** as the baseline: one Git-capable landing owner, sync-only peers, literal exact staged allowlists, task-path drift recheck and one-task/phase commit. Keep **G-A** optional for Full only when a local unsynchronized profile separately pins canonical Git-dir, worktree, index, ref/branch, remote and supported version/capabilities | G-B has the smallest operational surface. G-A adds value only when administration/index bytes must remain external, and otherwise adds path/pin/capability failure modes. A caller-derived probe accepted a wrong self-consistent worktree; pinned expectations close that gap |
| **D10** | Migration is an exact-accounting compatibility resolver, not normalization. Preserve all paths and raw bytes; import only verified facts; keep `legacy-unresolved` and `malformed` entries visible but non-actionable; never create a missing task or invent an HL, value, owner, lifecycle or terminal fact | The live census contains 111 source occurrences—60 board rows plus 51 task directories—resolving to 60 logical task IDs: 51 matched, nine board-only, zero directory-only, zero duplicate identities. No identity collision requires a move or semantic split |
| **D11** | Full and Assisted share identity stability, lifecycle/outcome, next/terminal legality, owner/epoch and event/recovery meanings. Artifact carriers, ID syntax, role cardinality, transport and Git participation are edition profiles | The census found representation differences but no case requiring `active`, `blocked`, terminal outcomes, ownership epoch or event ordering to mean something different. Assisted has no populated migration corpus, so this remains an acceptance obligation rather than runtime proof |
| **D12** | C2–C5, G-C, on-demand-only views, timestamp recovery, manual/time-only rollover, post-commit/two-commit landing and service/database authority remain eliminated for Phase A | New evidence tightened C1-R rather than defeating a survivor invariant. Reopening these families would reintroduce body drift, multi-path transitions, replay-only state, combined conflict domains, a second exchange authority or a forbidden service dependency |
| **D13** | Research is **SUFFICIENT** after iteration 2, with NH, PR, migration runtime, Git support/integration and numerical defaults carried as mandatory TS/RF evidence rather than reported as research proof | The architecture, alternatives, failure rules and acceptance obligations are determinate. Another local research fixture cannot manufacture a real participant, provider runtime or populated Assisted corpus |
| **D14** | No frozen-HL amendment is required | C1-R2 specifies how existing frozen outcomes are met. In particular, DoD-3 requires dispatch, handoff, state change, blockage, amendment escalation and consolidation events—not `landed`; §3.2/DoD-9 assign commit provenance to Git; DoD-11 is satisfied by filesystem-visible `landing_requested` plus a separate Git-aware completion check |

### Predecessor decision disposition

| Iteration-1 decision(s) | Disposition | Iteration-2 result |
|-------------------------|-------------|--------------------|
| D1 | **Confirmed** | H1 remains refuted as stated; the permanent router + persisted derived index hybrid survived four FA catalogue conditions |
| D2 | **Revised** | C1-R becomes C1-R2 with the smaller core, L3, combined rollover and pinned G-A |
| D3, D5, D6, D8, D9, D11 | **Confirmed** | Layer separation, shared lifecycle, owner/epoch recovery, reference-first events, event-first ordering and the ordinary-file sync floor survived |
| D4 | **Revised** | Strict YAML remains, but 20 universal fields are reduced to nine required plus conditional/profile/derived dispositions |
| D7 | **Partly refuted and revised** | The post-commit task event `landed` fails. `consolidation` stays reserved; completed Git landing becomes a derived L3 fact |
| D10 | **Revised** | Segmentation is specifically combined count + encoded bytes with a separate summary code-point guard; its three candidate numbers remain unsupported |
| D12 | **Confirmed and tightened** | Compatibility-first migration may explicitly leave an entry unresolved/non-actionable; exact accounting does not mean forced conversion |
| D13 | **Revised** | G-B remains baseline; G-A now requires separately pinned local paths, ref/remote and a tested version/capability profile |
| D14 | **Revised** | Exact allowlists remain, but the L3 manifest/digest now binds producer, landing owner, artifact hashes, paths and the unique reachable commit |
| D15, D16 | **Confirmed** | Eliminated carrier/Git families stay closed; no frozen amendment is needed |

No iteration-1 D-number is refuted wholesale. The concrete post-commit `landed` subdecision in D7 is the
only predecessor mechanism refuted; the journal responsibility it served is preserved by the
pre-landing handoff.

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| **Q1** | Can a non-technical person discover, interpret and safely change C1-R2 through ordinary browsing? | **Open for TS/RF acceptance, not research** | FA and UH exist; NH does not. The TS must require a genuine participant observation and the RF/EV must preserve errors and confusion, not only success |
| **Q2** | What should the event-summary, event-count and encoded-byte defaults be? | **Unresolved by design** | The combined finite mechanism is supported. `240 / 100 / 32 KiB` are test inputs only; defaults require workload, editor and provider evidence or must remain explicit project configuration |
| **Q3** | Does recovery work after an actual provider offline fork/reconnect? | **Open for TS/RF acceptance** | DF establishes deterministic rules and vendor PS establishes failure classes; PR remains mandatory under frozen §7.1 and DoD-14 |
| **Q4** | How should Git landing and task-journal ordering work? | **Resolved for architecture** | Use L3 pre-landing handoff/manifest plus one exact commit; derive completion from one reachable match without writing task authority |
| **Q5** | Which Git profile is baseline and how does optional G-A fail? | **Resolved for architecture; support matrix open** | G-B baseline; G-A optional Full with strict local pins and stable failure categories. Supported versions/platforms remain acceptance evidence |
| **Q6** | Can all current and Assisted legacy shapes migrate losslessly? | **Resolved as a compatibility contract; runtime evidence open** | Every live Full source is accounted exactly once without moves or guesses. The implementation must run against a copy/manifest and include populated Assisted inputs when available |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| **H1** | A persistent Task Board is not required; an on-demand command can provide the same discovery without degradation | iteration 1 refuted as stated; hybrid confirmed | ❌ **REFUTED AS STATED; HYBRID CONFIRMED** | Four FA conditions recovered authority, but absent view imposed material scan/classification work and NH remains absent. Keep a permanent router + persisted derived index + authoritative re-read |
| **H2** | A tiny machine-readable task-local carrier is safer than mutable Markdown and remains understandable to non-technical users | iteration 1 partially confirmed | 🟡 **PARTIALLY CONFIRMED** | The strict nine-field YAML subset and lifecycle legality survived all structural attacks. Human comprehension/edit safety is not proven and must be accepted through NH evidence |
| **H3** | A separate closed, referenced and bounded journal preserves continuity without duplication or unbounded growth | iteration 1 supported, acceptance evidence required | ✅ **CONFIRMED AT ARCHITECTURE LEVEL; ACCEPTANCE EVIDENCE REQUIRED** | Owner/epoch recovery, event-first ordering, malformed/duplicate handling, rejection retention and combined rollover survived. `landed` was removed. PR, integration and numeric defaults remain acceptance obligations |
| **H4** | Assisted and Full can share one task-state/journal contract while transport and Git differ | iteration 1 confirmed at semantic level | ✅ **CONFIRMED AT SEMANTIC-CONTRACT LEVEL; MIGRATION EVIDENCE REQUIRED** | Exact Full accounting found carrier/path differences but no different lifecycle/epoch/event meaning. Populated Assisted migration runtime remains unavailable |

## Phase-A TS Acceptance Recommendations

These are outcomes and evidence gates for the Coordinator to translate into a TS. They are not a TS or
an implementation prescription.

| # | Acceptance recommendation | Mandatory gate/evidence |
|---|---------------------------|-------------------------|
| **AR1** | Validate exactly the nine-field core, state-dependent conditionals and selected profile fields before any workflow action | Reproducible matrix covers every valid lifecycle, missing core fields, illegal conditional/profile combinations, unknown fields/profile/version and changes no state on rejection |
| **AR2** | Enforce the strict-YAML application profile and dependency visibility | Reject duplicate keys, anchors/aliases, merge keys, tags, directives, unsafe references, empty/partial/truncated files and missing goal/next/journal/event dependencies; preserve bytes and return stable fail-closed diagnostics |
| **AR3** | Build the hybrid catalogue deterministically over a 100-task 80-valid/10-legacy/10-malformed corpus | Two identical builds match; index declares derived authority, source count/digest and freshness; normal/absent/stale/malformed cases re-read authority and never omit legacy/malformed tasks |
| **AR4** | Verify fresh-agent and genuinely non-technical-human discovery separately | FA repeats all four index conditions. NH uses ordinary file browsing with no command coaching, identifies ID/goal/value/lifecycle/owner/outcome/authority, performs one authorized safe edit, and records misunderstandings/errors contemporaneously |
| **AR5** | Make journal/snapshot and owner recovery deterministic | Fixtures cover aligned, journal-ahead, snapshot-ahead, identical/divergent duplicate IDs, malformed records, same-epoch divergence, authorized recovery, old-owner reconnect, coordinator disappearance and terminal rejection; timestamp never decides authority |
| **AR6** | Use finite positive count, encoded-byte and summary-code-point limits while retaining all sealed history | Fixture includes ASCII/Cyrillic/emoji, exact boundary hits, multiple rollovers, oversized single event/summary, 100+ events and rejected history. RF records actual encoded sizes. Any proposed defaults cite workload/editor/provider evidence; `240/100/32 KiB` receive no privileged status |
| **AR7** | Exercise the frozen file-sync scenarios in at least one real supported synchronized-folder environment | PR evidence records provider/client/version, two different tasks, same-task role files, offline same-file fork/reconnect, conflict artefacts, initial/final bytes, sync status and reconciliation. Deterministic fixtures accompany but do not replace it |
| **AR8** | Integrate L3 with resume and release without task-authority writes after commit | Cover no commit, crash before/after, changed manifest, duplicate exact matches, extra/missing paths, wrong producer/landing owner, unreachable/rebased commit and ref change. Non-Git resume reports completion unknown; Git-aware release accepts exactly one reachable exact match and records derived `landed@<sha>` in evidence/output |
| **AR9** | Prove G-B one-task landing after unrelated peer changes | Stage literal exact paths, compare staged names to the manifest, recheck declared paths for working/index drift, retain unrelated changes unstaged, and verify the commit contains exactly one task/phase with separate producer and landing-owner attribution |
| **AR10** | Gate optional G-A with a declared support profile | Test supported Git versions/platforms/capabilities plus canonical path aliases, platform case behaviour, symlink/junction resolution, relocated index, missing/corrupt pins, index-inside-sync, unexpected gitfile, wrong Git-dir/worktree/ref/remote and pin corruption; any failure stops before staging/commit |
| **AR11** | Account for migration inputs exactly once without modifying legacy originals | On an isolated copy/manifest, reconcile 60 board rows + 51 directories = 111 source occurrences → 60 logical tasks; preserve the corrected 39 eight-cell / 21 nine-cell split, nine board-only tasks, proposals without HL, broken links, phase-case variants, terminal/rejected traces and malformed controls |
| **AR12** | Keep unresolved/malformed migration entries visible but non-actionable and test shared edition semantics | Zero unaccounted inputs; zero guessed core facts; zero path moves or legacy overwrites. Include a populated Assisted corpus when available and prove its carrier/path differences map to the shared lifecycle/owner/epoch/event meanings |
| **AR13** | Propagate the Phase-A ownership model through every reader/writer in the releasable slice | Exact pre-TS file/new-file/LOC census; canonical rules, lifecycle workflows, supported adapters, resume/release, Quick Start and docs compiler use task controls/derived views correctly; no stale adapter or live-README authority remains |

The following claim classes must remain explicit in TS Evidence fields and RF/EV results: **NH** for
human usability, **PR** for real sync behaviour, migration runtime for the exact resolver and populated
Assisted inputs, Git runtime for L3/G-B/G-A and the support matrix, and workload/editor/provider evidence
for any numerical defaults. None is research proof in this RES.

## HL Update Recommendations

> These are classifications only. The Researcher does not edit the frozen HL, `iterations.yaml`, README
> or TS.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| **R1** | §2 | Correct the live Task Board census to 39 eight-cell / 21 nine-cell rows and add the exact migration accounting: 60 rows + 51 directories = 111 source occurrences → 60 logical tasks, with 51 matched, nine board-only and no directory-only/duplicate IDs | Gather G13; Challenge C9 |
| **R2** | §7.2 | Add current primary citations for the strict-YAML application boundary and Git path/trailer/reachability contracts. Keep vendor and comparable-system citations qualified as documentation/source evidence, not runtime proof | RES evidence boundary; Extract E2/E6/E7; Challenge C4/C6/C8 |
| **R3** | §8 | Mark iteration-2 architecture research complete. Retain NH, PR, L3 resume/release integration, Git platform/version/capability matrix, copy-based migration including populated Assisted inputs, numerical-default evidence and exact Phase-A budget census as open Phase-A dependencies | D13; AR4/AR7–AR13 |
| **R4** | §9 | Replace the post-commit `landed` risk with L3 unique-reachable-match, duplicate and pinned-ref risks; add G-A pin/canonicalization corruption and explicit unresolved-migration action-gate risks | D8–D10; Challenge C6/C8/C9 |
| **R5** | §10 | Record final H1–H4 verdicts and distinguish architecture confirmation from NH/PR/migration/Git/numerical acceptance obligations. Close `landed` ordering and the universal-field question | Hypotheses; Open Questions |
| **R6** | §11 | Add three insights: manifest identity survives rebase while reachability remains ref-pinned; lossless migration may remain explicitly unresolved; non-Git resume and Git-aware release observe different facts without conflicting authority | D8/D10; Challenge unexpected survivors |

### Amendment Proposals — frozen sections, owner verdict required

**No amendment proposals.** C1-R2 fits the already-frozen task-locality, single-writer, stable-path,
derived-view, journal, migration and Git outcomes. Removing task-journal `landed` is a free refinement:
the frozen journal contract requires a material handoff but never that event name, while Git already owns
commit/release provenance. L3 preserves the pre-landing handoff in ordinary files and derives completion
without a second task write. No declarative claim in §§1 or 3–7 changes, so the §5/§6 amendment tripwire
does not fire.

## Fact Candidates

> fact-candidates: processed 2026-08-30

No new Fact Candidates. The Coordinator messages supplied scope, gates and synthesis requirements for
this task; they do not pass the next-agent decision test as independent project facts.

## Strategic Insights (Research)

No strategic insights. Iteration 2 received workflow and evidence-boundary direction, not new
human-sourced domain knowledge beyond what the frozen HL and iteration-1 trace already preserve.

## Findings Map

```text
PERMANENT DISCOVERY                         TASK-LOCAL TRUTH
README router ──→ persisted tasks/INDEX ──→ status.yaml
                    derived/disposable        9-field shared core
                    may be stale/absent        + conditional/profile legality
                              │                      │
                              └── select, then re-read
                                                     │
                                          event-first / snapshot-second
                                                     │
                                                     ▼
                                      segmented reference-first journal
                                      owner + epoch · retained history
                                                     │
                                           pre-landing handoff/manifest
                                                     │
                                                     ▼
                                      G-B baseline / pinned G-A optional
                                      exact paths · one task · one commit
                                                     │
                                  exactly one reachable exact manifest match
                                                     │
                                                     ▼
                                      derived landed@SHA, no task rewrite

COMPATIBILITY ENVELOPE
111 source occurrences → 60 logical tasks
verified facts become controls · unresolved/malformed stay visible and stop

EVIDENCE CEILING
FA/UH/DF/RR/PS support architecture ──┬── NH must verify human use
                                     └── PR must verify real synchronization
```

The central finding is not a preferred file extension. Conflict resistance comes from maintaining
separate authority, projection, recovery and provenance responsibilities, then making every crossing
explicit and fail-closed.

## Iteration Status

- **Iteration:** 2 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (refuted as stated; hybrid confirmed), H2 (partially confirmed), H3 (confirmed at architecture level with acceptance evidence required), H4 (confirmed at semantic-contract level with migration evidence required)
- **Hypotheses deferred:** None. NH, PR, migration runtime, Git support/integration and numerical defaults are acceptance obligations, not untested architecture hypotheses.
- **Gaps discovered:** NH; PR; populated Assisted migration corpus; L3 workflow integration; supported Git version/platform/capability matrix; evidence-backed numerical defaults.
- **Superseded decisions:** Iteration-2 D3–D4 supersede iteration-1 D4's universal field reading; D7 supersedes D10's undifferentiated rollover proposal; D8 supersedes D7's post-commit `landed` detail and refines D14 landing correlation; D9 supersedes the unpinned G-A form in D13.

### Open Threads (for next iteration)

No open research threads. The remaining items are mandatory Phase-A TS/RF acceptance evidence listed
in AR4 and AR7–AR13; iteration 3 would not be justified unless the Coordinator deliberately moves
those real participant/provider/runtime observations into research.

### Recommendation

- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write the Phase-A TS
- [ ] **MORE NEEDED** — no unresolved Phase-A architecture branch requires another research iteration
- [ ] **BLOCKED** — no blocker

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 2 adversarially validates C1-R while materially narrowing it. C1-R2 preserves the hybrid
router/index, task-local authority, segmented reference-first journal, event-first recovery, stable
paths and shared Assisted/Full semantics; it reduces authority to nine universal fields, replaces the
post-commit `landed` event with L3 manifest-correlated Git completion, makes count-plus-byte rollover
structural without inventing defaults, pins every optional G-A expectation, and permits honest
non-actionable migration states. The self-critique is evidence-class specific: local fixtures and fresh
agents are strong enough to choose the architecture, but they cannot prove human usability or real
provider recovery. Those gaps are therefore hard Phase-A acceptance obligations, not reasons to claim
success or repeat local research. Research is **SUFFICIENT**; continue with `/tfw-plan` and do not start
iteration 3 unless new counter-evidence or an intentional external-evidence research mandate appears.

---

*RES — TFW-60: Phase A Task State & Coordination — Iteration 2 | 2026-08-26*
