# Map — "What was done?" (revision 2)
> **Mindset:** Experienced newcomer. Understand the corrective result before judging it.
> **Test:** "Can I explain what changed since the rejected pass?"
> RF: [RF Phase A](../../RF__phase-a__task_state_and_coordination.md)
> TS: [TS Phase A, revision 3](../../TS__phase-a__task_state_and_coordination.md)
> Historical review: [first REVIEW — REJECT](../../REVIEW__phase-a__task_state_and_coordination.md)

## Understanding

Phase A replaces the root README Task Board as live authority with task-local `status.md`,
immutable event files, participant profiles, and a deterministic but non-authoritative
portfolio index. It migrates the legacy corpus without moving task directories, keeps both
legacy and clock-derived task identifiers readable, rewires lifecycle workflows and adapters,
and publishes the model as TFW `2.0.0`.

The corrective pass follows TS revision 3 at `c5e447a`. It restores the 61-row board snapshot,
makes the whole `YYYYMMDD-HHMMSS__slug` directory name the new identifier, adds actor-bearing
journal filenames, expands status validation and year-nested documentation resolution, gives
phases their own state, and removes the mandatory-current-index build gate that caused the
first result to fail its purpose.

The baseline-to-HEAD surface is 119 paths: 76 modified and 43 added. The RF's product census is
47 modified, 30 new, 77 total; its narrower executor-product accounting is 76 because it
excludes coordinator/reviewer process artifacts. During this re-review the owner explicitly
approved the actual file-budget overrun. The budget tripwire is therefore resolved and is not
a review finding.

## TS ↔ RF Alignment

| TS requirement | RF claim | Mapped result |
|---|---|---|
| AC-1 — configured container, year nesting, stable paths | container-aware resolver and path-stability fixtures | Implemented and independently reproduced |
| AC-2 — whole-name clock identifier, bounded actual-clock retry, both grammars | whole-name parser and creation algorithm in `plan.md` | Mostly implemented; the two config files still declare the bare stamp as `id_format` |
| AC-3 — immutable actor-bearing journal, actual-clock timestamps, identity fields, measured ceiling | same-kind/two-actor tests, `event_filename`, 120-character ceiling | Actor-bearing shape exists; same-actor retry composes timestamps, provider actors pass validation, and measurement claims conflict |
| AC-4 — profiles and session binding before durable writes | one human profile and Who Is Acting blocks | Model exists; Windows binding paths are corrupted in six canonical workflows and their full copies |
| AC-5 — derived index never outranks local state | `--validate` is the build gate; `--check` is informational | Implemented; the first review's purpose failure is corrected |
| AC-6 — exact, byte-preserving migration | 61/53/8/0 accounting and 11 task states | Core migration and snapshot claims reproduce; one RF inline diff claim is not the output of its shown command |
| AC-7 — references and history resolve | both layouts supported; old failure set claimed unchanged | Current tests pass; the claimed baseline relation is not persisted as current evidence |
| AC-8 — board retired and no live consumer parses it | root route, removed docs parser, reintroduction test | Implemented; historical migration reads remain intentional |
| AC-9 — no component required to advance work | ordinary files plus three documentation/migration scripts | Implemented |
| AC-10 — release describes the shipped model | `2.0.0`, changelog, quickstart, adapters | Mostly implemented; configuration still declares the wrong identifier grammar |
| AC-11 — all rejected-pass findings and evidence counts corrected | 15 findings closed; all numbers regenerated | Several old findings are only partially closed and current evidence still contradicts itself |
| AC-12 — second precision and phase-local state | `PHASES`, phase `status.md`, phase rows | Implemented and independently reproduced |

## Previous REJECT — Current Disposition

| Historical finding | Current disposition |
|---|---|
| F1 seconds-only identifier | Corrected in the resolver and workflows; configuration residue remains |
| F2 missing creation retry | Corrected in `plan.md` with bounded rereads of the actual clock |
| F3 event collision | Different actors no longer collide; same-actor retry still composes a fictitious timestamp |
| F4 identity resolution absent from workflows | Added, but five of the six RF-cited Windows paths are unusable; `init.md` is affected too |
| F5 private file-sync binding conflict | Transferred to TFW-61 by approved TS R3 |
| F6 incomplete status schema | Corrected; negative schema tests pass |
| F7 legacy-only docs resolver | Corrected; clock/year/phase fixtures pass |
| F8 incomplete clean-clone states | Corrected: 11 task-level states plus one phase state are tracked |
| F9 overwritten migration accounting | Corrected: explicit board revision and zero-row refusal preserve the 61-row snapshot |
| F10 release residue | Mostly corrected; `id_format` still denotes a bare timestamp |
| F11 contradictory equal-depth clause | Deleted by TS R3 |
| F12 stale/inconsistent evidence | Not closed: the ceiling population and other shown commands remain inconsistent |
| F13 missing tests | Test count and coverage expanded, but the actual-clock and provider-actor tests assert weaker or opposite behavior |
| F14 unsafe broad staging | Current corrective commits preserve the unrelated dirty tree; explicit-path staging is asserted but not evidenced |
| F15 mandatory shared-index rewrite | Corrected; local validation no longer requires the derived index to be current |

## Declared Deviations and Authority

- The RF leaves non-specialist readability explicitly DEFERRED to TFW-61, as TS R3 directs.
- No agent profile ships. Under TS R3 the sole `team/` profile is `saubakirov`; tool provenance
  is recorded separately as `via: codex` or `via: claude`.
- The owner explicitly approved the delivered file-budget overrun during this review. No
  coordinator or TS revision is required for that count.
- The old REJECT, old REVIEW, and `review/{map,verify,judge}.md` remain immutable history.

## Checkpoint

**Self-check:**
- [x] RF §§1–9 read completely.
- [x] TS revision 3 DoD, failure conditions, and all twelve AC groups mapped.
- [x] Master HL contract baseline and Phase HL read.
- [x] ONB decisions and citation applications read.
- [x] Previous REJECT and all historical findings included.

Stage complete: YES
