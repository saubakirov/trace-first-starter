# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260913-151442_RWNR](../../HL-TFW_20260913-151442_RWNR.md)
> Goal: Determine whether `/tfw-resume` is a necessary public command and retire it only after every continuity guarantee has a proven surviving route.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D _(if any)_ |
|-----------|-------|-------|-------|-----------------|
| D1: Returning-user entry topology | Keep `/tfw-resume` | Make `/tfw-plan <task>` the only general continuation entry | Require direct lifecycle-specific commands | Rename or wrap resume |
| D2: Multi-phase choice owner | Resume workflow | Plan workflow | Shared canonical phase-selection contract | Direct selection of a named phase before command entry |
| D3: Historical-only safety owner | Resume-local guard | Plan-local guard | Shared exact-selection/discovery contract | Repeated guard in every lifecycle workflow |
| D4: Closing and record-recovery entry | Resume workflow | Plan workflow | Existing Coordinator invokes the shared conventions contract directly | New public recovery entry |
| D5: Retirement propagation | Delete canonical command only | Remove manifest/config/docs and regenerate clean receivers | Versioned migration removes verified owned stale files in existing receivers | Keep tombstones that refuse invocation |
| D6: Assurance level | Source-string assertions | Copy/manifest parity | Executable state-fixture scenarios with before/after hashes | Native adapter invocation trials |
| D7: Retained-surface denominator | Frozen 2,685-word baseline | Generic whitespace count | Bytes and physical lines | Semantically charged instruction words |

## Findings

### G1: Canonical responsibility inventory

The canonical source is `.tfw/workflows/resume.md` (83 physical lines, 5,093 bytes). Its public job is not generic execution: it is a Coordinator entry that selects an exact task, inspects state, exposes phase choice, and optionally reaches the shared close/recovery contract.

| ID | Observable responsibility | Trigger/input | Result or safety stop | Canonical authority and role |
|---|---|---|---|---|
| R1 | Resolve an exact task across the deduplicated active-plus-historical reference union | Explicit task reference or ordinary current selection | Whole-ID collision refuses selection; ordinary discovery stays active-only | `resume.md` Read Contract and §1; Coordinator |
| R2 | Protect historical-only traces | Selected path exists only in a historical container | Read cited original state/artifacts, report historical access, then stop before phase choice, closing, repair, or mutation; later continuation needs separate authority | `resume.md` §1 historical-read branch; Coordinator read-only |
| R3 | Reconstruct current lineage | Selected current `status.md`/journal plus referenced authority | Report governing artifacts and highest valid lineage; indexes, globs, chat, and unrelated RF are non-authoritative | `resume.md` Read Contract and §1; Coordinator |
| R4 | Inspect an unselected multi-phase task | Task lifecycle is `PHASES` and no phase is selected | Read every current phase's local state/journal; missing or malformed state blocks a confident recommendation | `resume.md` §1 plus `conventions.md` → `A phase carries its own state`; Coordinator |
| R5 | Preserve returned review state | Latest completed/returned phase has a live REVIEW | Read the REVIEW, preserve every disposition, and never reopen REVIEW §5 as a backlog | `resume.md` §1; Reviewer remains source of proposals, Coordinator only rules through the shared route |
| R6 | Apply navigation identity without enlarging authority | One task and lineage resolve | Root LEAD may retain its qualified title; children stay ordinary `RESUME`; ambiguous phase is omitted | `resume.md` §1 plus `conventions.md` → `Session identity`; navigation only |
| R7 | Reach selected closing or record recovery without replanning | The close/recovery request and Coordinator mandate are already explicit | Invoke `conventions.md` → `Closing and record recovery`, report the effect/gap, then stop; no matrix or bootstrap | Shared conventions contract; existing authorized Coordinator |
| R8 | Expose one row per declared phase | Current task has phases and no selected next phase | Matrix includes description, authority, lifecycle, REVIEW verdict, and exact next route | `resume.md` §2; Coordinator, read-only |
| R9 | Prevent silent phase ordering | Matrix is complete | Ask which phase to plan and stop; phase order is never assumed | `resume.md` §3; human decision gate |
| R10 | Route, never absorb, lifecycle work | User chooses a phase | Enter `/tfw-plan`; approved TS routes to `/tfw-handoff`; RF routes to `/tfw-review` | `resume.md` §3; Plan/Executor/Reviewer Role Locks remain separate |
| R11 | Resolve acting attribution before any write | A resume branch would write closing/control records | One profile, valid binding, or one question; never infer identity | `resume.md` → `Who Is Acting`; Coordinator |
| R12 | Enforce a narrow Coordinator Role Lock | Every resume invocation | Allows read-only status analysis, phase planning only after selection, and selected closing/control writes; forbids ONB, RF, RES, REVIEW creation/proposals, implementation | `resume.md` header and `conventions.md` §15 |

Normal matrix use creates no artifact and performs no lifecycle transition. The only resume-reachable writes are delegated to the shared close/recovery contract: after independent APPROVE has already entered `KNW`, the authorized Coordinator may write `DONE` plus the real transition event after final effects; a material failure may produce an honest `BLOCKED` dependency; record-only recovery may repair the current carrier and append a truthful present event without altering original event bytes. Review already returns approved work directly to the existing Coordinator for this shared contract (`.tfw/workflows/review.md` Step 7), so closing is not intrinsically dependent on a resume command.

### G2: Callers, receivers, and routes

No canonical workflow calls `/tfw-resume`; a repository search over `.tfw/workflows/` excluding `resume.md` returned no route. Its callers are humans or agents entering through adapter surfaces and current documentation. Its receivers are:

| Surface | Source | Installed or generated receiver | Current state |
|---|---|---|---|
| Canonical algorithm | `.tfw/workflows/resume.md` | Claude `.claude/commands/tfw-resume.md`; Antigravity `.agents/workflows/tfw-resume.md`; Cursor `.cursor/commands/tfw-resume.md` when selected | Current Claude and Antigravity copies are byte-identical; Cursor receiver is absent in this checkout but is generated by the manifest |
| Codex command | `.tfw/adapters/codex/skills/tfw-resume/SKILL.md` | `.agents/skills/tfw-resume/SKILL.md` | Source and installed copy are byte-identical; the thin skill binds the Coordinator Role Lock and fully loads the canonical workflow |
| Always-on command discovery | Four adapter persistent templates | `AGENTS.md`, `CLAUDE.md`, `.agents/rules/tfw.md`, optional Cursor rule | Root files or copies list the route; `.agent/rules/agents.md` is an additional tracked legacy-compatible live root not managed by the current manifest |
| Config discovery | `.tfw/templates/project_config.yaml` | `.tfw/project_config.yaml` | Both register `tfw.workflows.resume` |
| User documentation | Root README source | `README.md`, `README.ru.md`, `README.kk.md` | All three tell users that resume continues interrupted work |

The forward lifecycle is already split: `/tfw-plan` owns known-task planning, research iteration gates, phase topology, TS approval, and REVISE routing; `/tfw-handoff` owns execution; `/tfw-review` owns independent verdict and returns APPROVE to Coordinator closing. Resume presently adds selection and protection around those routes, not another implementation pipeline.

### G3: Live-surface and history census

A path-name-plus-text census at commit `a2363fd` found 205 tracked paths potentially affected by a broad `resume` match after excluding the current RWNR task: 23 live source/config/adapter/receiver/docs/test paths, 3 durable history/knowledge paths, and 179 historical task-trace paths. These are topology counts, never invocation telemetry.

| Classification | Count | Treatment question for later design |
|---|---:|---|
| Canonical/config live | 4 | `resume.md`, conventions workflow/Role Lock rows, live config, and config template must converge on the surviving design |
| Adapter source/manifest live | 7 | Manifest row, four persistent templates, Codex skill source, and Codex adapter documentation must agree |
| Installed/generated live | 7 | Delete command receivers and refresh managed/copy roots; classify the singular `.agent/rules/agents.md` compatibility root explicitly |
| Current docs live | 3 | Replace the obsolete public instruction consistently in EN/RU/KK |
| Maintainer tests live | 2 | Replace command-presence assumptions with absence, behavior-preservation, install, update, and negative scenarios |
| Durable history/knowledge | 3 | Preserve changelog and recorded decisions/facts as truthful historical evidence; current guidance may link to the retirement decision without rewriting the old claim |
| Historical task traces | 179 | Freeze a pre-change path/hash manifest and require byte equality after implementation; do not “clean” old command names |

The broad census deliberately includes filenames and semantic references; an exact `/tfw-resume` text search currently yields hundreds of historical/evidence matches and is therefore unsuitable as a live-removal oracle. The correct oracle is classification plus an allowlist for immutable history.

### G4: Clean install and update are different problems

`init.md` Full Setup installs the manifest's persistent row and all exact 11 command rows. The manifest-based clean-receiver tests copy every manifest command into each of four adapter layouts. Removing the resume row and its sources would make a new clean receiver omit the command, provided the exact-set constant and tests change from 11 to the new declared set.

Existing-receiver update is not solved by that omission. `update.md` overlays the pinned `.tfw/` payload, merges config, then validates exact commands and copy/managed-block parity. The test helper `_sync_from_manifest` writes every current command but never deletes a command absent from the new manifest. Therefore a receiver upgraded from the current version would retain stale `.tfw/workflows/resume.md`, configuration, and adapter command targets unless a version-addressed migration names the owned deletion set and verifies ownership before removal. The update must distinguish:

- framework-owned stale canonical/config/adapter sources that the pinned migration may remove;
- generated command copies whose bytes/path establish ownership and may be removed;
- managed root blocks that must be regenerated from the new template while preserving project text;
- unmarked or foreign files that must be reported and left untouched;
- historical task, changelog, migration, knowledge, receipt, and evidence files that must never be scrubbed.

### G5: Existing assurance and uncovered scenarios

A focused run of nine relevant test entrypoints produced `18 passed in 1.83s`. It covers the current historical guard ordering, exact four-adapter/eleven-command manifest, clean receiver creation, secondary-route copy parity, idempotent repair, thin Codex routing, source-derived multi-phase WAIT semantics, closing writes (`status.md` plus transition event), and stale/competing-authority mutants.

Current evidence is strongest at R0/R1 (source presence and receiver parity) plus source-derived semantic simulation. It does not yet execute the post-retirement user scenarios required by the HL:

- `/tfw-plan <multi-phase task>` shows every phase and waits without selecting or mutating;
- historical-only exact selection reads and stops with identical before/after bytes;
- selected close succeeds through the shared Coordinator contract without `/tfw-resume`;
- record-only recovery repairs only reconstructable current carriers, preserves old events, and refuses uncertain lineage;
- wrong-role attempts do not widen Plan or bypass Executor/Reviewer ownership;
- clean install produces no resume source, registration, receiver, or alias;
- update deletes only verified owned stale resume files and does not recreate them on the second run;
- current live surfaces contain no replacement command while the historical allowlist remains byte-identical.

### G6: The 2,685-word baseline is fixed but its counter is not reproducible yet

The frozen HL defines the comparison as Plan 1,995 words plus Resume 690 words = 2,685, and its physical measures match the current sources exactly: Plan 14,416 bytes/220 `wc` lines; Resume 5,093 bytes/84 `wc` lines. A generic whitespace counter on those same bytes returns 2,021 + 716 = 2,737. The 52-word difference does not change the owner-approved baseline, but H4 cannot become a reproducible acceptance test until the exact baseline counting rule is named and applied to both baseline and candidate. Any surviving design must also give Plan's existing >1,200-word violation an architectural disposition; deleting 690 resume words does not authorize pasting them into Plan.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| All 12 observable resume responsibilities are inventoried with triggers, routes, transitions, Role Locks, and stops. | Extract one owner for each responsibility and identify the minimum canonical change point. |
| All current command sources, manifest/config registrations, installed/generated receiver forms, docs, tests, and absent Cursor receiver are classified. | Define the versioned deletion/migration contract for stale existing receivers without touching foreign or historical files. |
| Existing tests were mapped and 18 focused checks passed. | Design executable positive, negative, and no-mutation scenarios at R2–R4 rather than relying on strings/parity. |
| Historical truth is separable as 3 durable history/knowledge files plus 179 task-trace paths. | Freeze an exact pre-implementation hash/path allowlist and decide how current knowledge records the retirement without rewriting old facts. |
| The frozen 2,685 denominator and current physical source sizes were checked. | Recover or define the word-count algorithm so before/after arithmetic is reproducible. |

**Sufficiency:**
- [x] External source used? Primary repository sources, generated receivers, Git path census, and executed maintainer tests.
- [x] Briefing gap closed? The requested responsibility/surface/test inventory is complete enough for configuration mapping.
- [x] Dimensions identified? Seven independent decision factors with at least three alternatives each.

Stage complete: YES
→ User decision: Briefing scope remains unchanged; proceed to Extract and resolve the survivor matrix.
