# Challenge — "What do we NOT expect?"

> **Mindset:** Critic. Every surviving configuration needs evidence; every elimination needs a reason.
> **Test:** "Would my surviving configuration hold if a different researcher attacked it?"
> **Parent:** [HL-TFW_20260906-190312_CRUE](../../HL-TFW_20260906-190312_CRUE.md)
> **Goal:** Make TFW releases and updates clear, safe and useful without requiring owners to learn framework internals.
> **Operational source:** `8fd8e40b734e9c439bb84721ef8bee441b9fcdd7`; no publication or upstream-availability claim

## Consistency Check

All 36 pairs of the original Gather D1–D9 dimensions were considered. The compact notation below records the compatibility condition for every pair; a condition is not a claim that the current source already meets it.

| Dimension | Pairs checked | Challenge result |
|---|---|---|
| D1 · generic/project release boundary | D2–D9 | Compatible with receipt, preservation, trace, semantic-effect, owner-account, adapter and evidence choices only when the generic workflow owns domain-neutral gates and the optional project contract owns concrete inputs/effects. A generic TFW/Git/SemVer algorithm is incompatible with no-release, document and non-Git projects. |
| D2 · durable update continuity | D3–D9 | Receipt history can reference preservation and report outcomes, but never supplies current state, task authority, Git provenance, adapter parity or comprehension. Mandatory task reuse is incompatible with the current taskless update Role Lock/read path. |
| D3 · legacy README transition | D4–D9 | Preservation can coexist with trace selection, semantic groups, briefing, adapter moves and evidence. It is incompatible with removing all purpose readers: a historical HL's unchanged relative link can otherwise resolve the replaced live file. |
| D4 · incidental concurrent traces | D5–D9 | Deliberate sibling TRACE co-commit is compatible only with aligned conventions/handoff/review/release readers, semantic effect filtering, truthful owner/release accounts and exact-path evidence. Blanket TRACE inclusion/exemption and own-producer landing for every TRACE path both fail frozen A3. |
| D5 · agent rule/read placement | D6–D9 | One canonical algorithm plus conditional shared headings and exact full copies is compatible. A second update guide or registry needs a unique reader/job and conflict rule; none was found. |
| D6 · update decision unit | D7–D9 | Semantic effects may form connected atomic groups and then project to owner/evidence/adapter results. Per-file approval and whole-attempt classification both hide mixed authority/effects. |
| D7 · final owner account | D8–D9 | Outcome/benefit/limit/next action can report adapter state, but message emission is not owner receipt or comprehension. Technical checklist and free-form optimism are incompatible with the fixed information contract. |
| D8 · adapter-root transition | D9 | Plural canonical installation plus bounded singular legacy support is compatible with source/synthetic/native evidence. It does not prove provider behavior or authorize cleanup of foreign singular neighbors. |
| D9 · evidence strength | — | Evidence layers compose only as separately labeled observations; source consistency, native invocation and owner comprehension do not substitute for each other. |

### Incompatible pairs found in the Extract configurations

| Configuration | Dimension A / alternative | Dimension B / alternative | Why incompatible |
|---|---|---|---|
| C0 | D2 re-observe only | D3 exact transition | After an untracked/custom legacy README is overwritten, current observation and Git cannot reconstruct the prior bytes. Stopping on every such receiver does not deliver the approved routine transition. |
| C0 | D4 separate-only landing | D6 semantic-effect decision | Frozen DoD 13 requires deliberate selection of a stable sibling TRACE-only path; producer difference alone cannot replace effect classification. |
| C1 | D2 task-local status/journal | D5 current update route | Current `update.md` forbids task planning/execution/review artifacts and has no task prerequisite/read. Making every update a full task creates a new lifecycle/authority prerequisite. |
| C1 | D4 same-producer-only inclusion | D7 truthful owner/task account | It rejects the required sibling TRACE case; treating a co-commit as task completion would instead make the account false. |
| C2 | D5 target workflow plus version-independent guide | D2 current observation/continuity | Both carriers would govern ownership, recovery and old-version applicability, but no precedence/conflict rule or unique guide-only case is specified. The guide can become stale current authority. |
| C2 | D7 CRUE release-note deliverable | D1 project release intake | The task file and later changelog/release synthesis can describe the same effects; the TS gives no exact future `/tfw-release` read edge or disagreement rule. |
| C3 as first extracted | D3 preserved attachment | D5 no HL/judge change | A future HL can cite the attachment, but an old frozen HL continues to name `.tfw/README.md`; opening that relative link against the live tree silently changes its meaning. |
| C3 as first extracted | D7 no CRUE release-note file | D1 current release read contract | Removing the file without adding an exact root-`RELEASE.md` intake leaves the future release owner unable to select the accepted RF/REVIEW evidence under read-contract order 5. |
| C4 | D2 mutable current-state registry | D5 generated registry/engine | The engine makes a second current authority beside receiver observation/config and contradicts the approved receipt-as-history/no-registry boundary. |
| C4 | D1 universal release engine | D6 project-defined semantic effects | Parameterizing one engine does not give it authority to choose the meaning, version or external effects of every project release. |

### Configuration dispositions

| Config | Result | Reason |
|---|---|---|
| C0 · re-observe/no carrier | **Eliminated** | Fails unknown/untracked byte recovery and frozen A3. Re-observation remains mandatory inside the survivor. |
| C1 · ordinary-task/Git reuse | **Eliminated** | Can preserve history, but only by imposing a full task where the ordinary update route deliberately has none; it also narrows A3. |
| C2 · full revision-2 TS | **Dominated, not invalid wholesale** | It covers required outcomes, but its separate guide and CRUE release-note file have no surviving unique job after the exact updater/release reader chains below are restored. Their duplicated authority/conflict cost is avoidable. |
| C3-R · repaired compact receipt | **One minimal full survivor** | Restores narrow HL/judge/review purpose readers, quickstart discovery and an exact root release-intake edge; retains receipt, A3 readers and Antigravity compatibility correction; removes only three proposed rows after their reader chains pass. |
| C4 · registry/engine | **Eliminated** | Adds current-state and universal-release authority without a case existing workflow+project contract+receiver observation cannot answer. |

**Unexpected survivor:** C2 remained case-complete under attack despite being larger. Its rejection is Saint-Exupéry dominance, not a quality failure: C3-R performs the same named jobs while removing two duplicate prospective carriers and one unchanged/non-unique reader. If either successor chain below is not implemented exactly, C2's corresponding carrier must be restored rather than silently omitted.

## Findings

### C1 — A historical North Star link demonstrates subject drift, not a universal purpose freeze

The frozen CRUE HL at commit `c387dcf78ed447426f2e8e5469107037d922c397` names `../../../.tfw/README.md#ns1`, `#ns2`, and `#ns3`. The later A5 freeze `3a5a2680b4582594ee2c73f69309b5e7e97180fc` carries the same textual link, but the `.tfw/README.md` blob changed from `f8a611e64bb07fd196ce520703bbc7dddc51429f` to `ca0885f0fba1fb355f5ee0670d0f57b5243d824e`. The observed change is small and does not itself prove purpose harm. It proves that a relative path can retain its spelling while the referenced bytes change.

That mutability is not automatically a defect. Project North Star is current project-owned authority, and TFW defines no universal project-purpose freeze. An owner-authorized purpose edit after a task's HL freeze may legitimately change what current reviewers must protect. CRUE's special hazard is narrower: the update reassigns the same live `.tfw/README.md` path from possible project-purpose authority to framework-owned methodology. An old textual link must not silently make the replacement framework values into project P0.

The current chain is incomplete:

1. `conventions.md` rule 15 finds a freeze commit by commit subject.
2. The Project North Star section says the current North Star plus contract baseline form the Purpose Check reference set, but does not define a project-level freeze.
3. `review.md` and `judge.md` do not say how a reader distinguishes a legitimate current project-purpose change from a path whose subject/ownership was replaced by update.
4. Markdown preserves the link destination URI, not a Git revision. CommonMark defines an inline link in terms of its destination URI; it does not bind `../../../.tfw/README.md` to the commit containing the document ([CommonMark §6.3](https://spec.commonmark.org/0.31.2/#links)).
5. Git provides one historical-evidence operation: `<rev>:<path>` names the blob/tree at that path in the named revision ([Git revisions](https://git-scm.com/docs/gitrevisions)). It cannot recover an untracked README that was absent from the freeze tree and does not decide current project authority.

Future replacement of live `.tfw/README.md` with framework-owned values would therefore make the frozen old link appear to endorse a different subject if a reviewer treats a working-tree click as authoritative. Retargeting old HLs is forbidden, but freezing every P0 reference to its task baseline would create the new project-purpose protocol that current rules deliberately do not define.

**Required narrow repair:**

- `conventions.md` distinguishes three things: the frozen HL's own clauses; historical evidence of what a cited path meant; and the current owner-authorized Project North Star. A path becoming framework-owned never promotes its replacement content to P0 merely because an old HL named that path.
- `workflows/update.md` and `init.md` preserve exact legacy bytes, record the observed prior path/designation and immediately continuing project-owned purpose locus in the immutable receipt, install framework-owned `.tfw/README.md`, and leave existing frozen HLs unchanged.
- For a tracked historical source, `<freeze>:<path>` is evidence of its original bytes. For an untracked source absent from the freeze tree, the exact preserved attachment plus receipt-bound observation of the original designation is the fallback. Absence from Git alone is not a contract defect.
- `templates/review/judge.md` first reads the current, unambiguous owner-authorized Project North Star. When a cited path underwent the defined ownership transition, it follows the relevant immutable mapping and uses Git-baseline bytes or the evidence-bound preserved attachment to test historical meaning; it never treats live framework `.tfw/README.md` as P0 by path inheritance. Ambiguous/conflicting designation routes as a concrete meaning/contract problem to the owner.
- `workflows/review.md` invokes this conditional legacy-resolution path in Judge; this file is already required by A3.
- `templates/HL.md` tells new HL authors to cite the current project-owned purpose locus, including a preserved `legacy-readme/<sha256>/README.md` attachment when it remains authoritative. It explicitly forbids rewriting older frozen HL links. A later owner-authorized North Star change remains current authority under existing project rules; CRUE adds no blanket freeze.

This restores the two purpose-reader paths removed in the first C3. It does not add a registry, require historical edits, make Git tracking mandatory for legacy purpose, or freeze all Project North Star evolution.

### C2 — The selected stable sibling TRACE case fits existing carriers only with aligned local rules

The frozen A3/DoD 13 requirement is `SELECTED_STABLE_UNCOMMITTED_SIBLING_TRACE`: before an otherwise authorized commit, the actor selects and reads another task's stable TODO/HL/journal path; the path has no VALUE, ASSURANCE, authority-changing or private effect; exact-path co-commit preserves its existing task/writer/content provenance; the sibling task does not become DONE.

Current handoff allows the Candidate changed-path set to contain approved VALUE+ASSURANCE plus “already-authorized task-local TRACE.” Current review requires a crossing deliverable to retain its own producer-task/phase commit and reachable Candidate. Neither sentence decides whether a selected sibling TRACE is task-local to the commit or a crossing deliverable.

The case is expressible without a new provenance protocol if the existing carriers use the same five-way boundary:

| Case | Required result |
|---|---|
| Same-producer necessary TRACE | May co-commit when declared and exact-selected; no special sibling rule needed |
| Selected stable uncommitted sibling TRACE | May deliberately co-commit after semantic inspection; record exact path, source task/writer already present in its trace, unchanged content and noncompletion in existing evidence/RF; no separate owner question |
| Already-committed sibling history | Do not recommit; its reachable commit already preserves history |
| Late unselected sibling TRACE | Leave uncommitted; no duty to collect foreign traces, and inseparable content stops the selected commit |
| Crossing accepted deliverable/Candidate | Keep its own producer-task/phase commit, Candidate reachability and reviewed landing |

`conventions.md` owns the definition/effect filter. `handoff.md` owns pre-commit selection/Candidate membership and evidence. `review.md` verifies content, exact selection, absence of VALUE/ASSURANCE/authority/private effects, existing trace attribution, sibling status noncompletion and actual commit. `update.md`, generic `release.md`, root `RELEASE.md`, Claude full copies and the five changed Antigravity workflow copies consume the same boundary where they classify update/release inputs.

Git `commit --only -- <paths>` supports exact path selection while disregarding other staged paths, but Git does not decide TFW semantics or authorship ([Git commit documentation](https://git-scm.com/docs/git-commit)). W3C PROV's distinction among entity, activity and responsible agent is useful counterevidence to inferring sibling completion from the co-commit; it does not require a new TFW schema ([W3C PROV-DM](https://www.w3.org/TR/prov-dm/)).

**Result:** H5 survives architecturally. The exact wording and native behavior remain implementation/test obligations, not measured reliability. If existing trace identifiers cannot preserve adequate authorship in a concrete case, the TS must state the gap/cost and propose a carrier; it may not drop the frozen case.

### C3 — Ordinary update does not need or permit a full-task prerequisite

Current `update.md` lines 10–12 permit approved framework/config/adapter updates and forbid task planning/execution/review artifacts. Its read contract selects installed config/version/README, immutable source, target workflow, applicable changelog/migration, manifest and briefing; it does not select a task `status.md`, journal, TS, RF or REVIEW.

C1 can be made internally coherent only by changing that Role Lock and requiring task inception, scope approval, lifecycle transitions, evidence, RF and review before a routine update. That is a new authority/cost, and it conflicts with the owner's priority that an ordinary configured update work without a full-task prerequisite.

C3-R keeps the update under Coordinator Role Lock and stores one project-owned append-only receipt outside task lifecycle. The receipt is historical observation/recovery evidence; config/current files remain current state. An active task, if present, is preserved rather than adopted. A task is still required when the owner separately asks to change project product work or another outcome—the update request does not smuggle that authority.

`RECEIVER_UPDATE_WITHOUT_ACTIVE_TASK`, `STALE_SUCCESS_RECEIPT_AFTER_MANUAL_EDIT`, and `INTERRUPTION_BEFORE_RECEIPT` all have a route: re-observe; resume only idempotent/detectable effects; preserve any prior immutable receipt; write a new attempt receipt only for what was observed; report the first unmet condition and next action. No task status is fabricated.

### C4 — Removing the version-independent update guide is safe only through the target-reader chain

The removed `.tfw/migrations/update-experience.md` was supposed to carry prospective ownership, receipt, recovery and older-version applicability. The exact successor chain is:

1. The installed `update.md` is authoritative only until it pins a target.
2. It materializes one immutable target and follows the target's `.tfw/workflows/update.md` from Step 1.
3. The target workflow owns all prospective ownership, decision, preservation, receipt, recovery, verification and owner-account behavior.
4. It reads only applicable intervening target changelog ranges and the crossed major versioned migration. Unknown/pre-stable states stop or take an explicitly supported versioned route; they are never guessed.
5. Root `RELEASE.md` already requires every release's updating section to reach every earlier tag still in use and requires versioned migration text when a major boundary is crossed. The repaired root contract retains and sharpens that obligation.

Thus the target updater receives the current algorithm and release-specific deltas without a version-independent second guide. A separate file under `migrations/` would answer the same prospective decisions as `update.md` yet sit outside the current read contract unless another edge were added.

Counterexample `OLDER_SUPPORTED_RECEIVER_NEEDS_GUIDANCE_NEITHER_CURRENT_WORKFLOW_NOR_VERSIONED_MIGRATION_CAN_SELECT` does not survive if—and only if—the five-step chain is an acceptance test. Missing target workflow, intervening range or required major migration is a truthful hard stop. The task does not pre-author a release number or edit 3.0.0 migration history.

**Disposition:** remove the new guide from the proposed selector; merge its current rules into target `update.md` and its release-dependent deltas into the eventual versioned changelog/migration. If later implementation cannot make an older supported state reach those inputs, restore a carrier with a named read edge and conflict rule.

### C5 — Removing CRUE `RELEASE-NOTES.md` requires a discoverable accepted-task intake

The removed task-local deliverable was supposed to tell a future release owner the actual CRUE changes/value, migration and evidence limits. Current generic release order 4 selects DONE task states; order 5 permits only task artifacts referenced by those states or the release checklist. Current root `RELEASE.md` does not yet name RF/REVIEW as its release-note sources. Without a change, removal fails `FUTURE_RELEASE_OWNER_CANNOT_RECOVER_USER_FACING_CRUE_EFFECTS_FROM_ACCEPTED_TRACE`.

C3-R repairs the whole chain inside already-selected authorities:

1. CRUE implementation RF records actual modified files, key decisions, acceptance results, evidence and limitations; REVIEW independently records verified scope and verdict. Task/phase `status.md` carries DONE/outcome only after acceptance.
2. Root `RELEASE.md` adds a self-hosting release-intake rule for each **selected shipping effect**, not every DONE task. Resolve the effect's actual task/phase owner and the governing evidence set that legally exists for its epoch/topology: a single-phase task may have task-root TS/RF/REVIEW/EV, while a multi-phase task may keep them only under the applicable completed phase. Read only the applicable status/outcome, governing specification, accepted report/verdict and linked evidence.
3. Do not require new umbrella TS/RF/REVIEW/EV at task root, retroactively create artifacts for completed 3.0.0 work, or read unrelated DONE/non-VALUE tasks. A valid historical/N/A route remains valid. Missing/inconsistent evidence for one selected shipping effect is that effect's concrete release gap; it is not a global dirty-worktree or unrelated-task closure failure.
4. From that governing set, extract actual user-facing effect, migration/compatibility obligation, evidence limit and unresolved exclusion. The root contract's checklist reference supplies generic release read-contract order 5.
5. Generic `release.md` remains domain-neutral: it reads sources named by the optional project contract and does not impose TFW RF/REVIEW topology on other projects.
6. The future release owner writes the actual versioned changelog/migration under the root contract, remeasures time-sensitive claims at the release candidate, and reports unpublished/prepared/published state truthfully.

This is a real reader edge, not “the information exists somewhere.” It gives the later owner the accepted governing truth for each selected effect rather than a second task-authored release summary that can disagree with it. It also preserves frozen DoD 12: migration, compatibility and release notes travel with the changed behavior when the separately authorized release is prepared; this research does not claim that release already exists.

**Disposition:** remove CRUE `deliverables/RELEASE-NOTES.md` only with the root-`RELEASE.md` intake above as an explicit TS acceptance condition. Otherwise restore the file and its exact future read edge.

### C6 — Quickstart has a receiver-facing discovery job; the common adapter overview does not

The upstream root README presents `/tfw-update`, explains that it preserves project state, and links the exact update workflow and changelog. That README is not framework payload in a receiving project: the receiver's root README is explicitly preserved. Installed root instructions/adapters expose the command to agents, but the changed briefing is available only after invocation. Therefore `NEW_OWNER_CANNOT_DISCOVER_ROUTINE_UPDATE_ROUTE` survives for an owner following the shipped `.tfw/README.md → .tfw/quickstart.md` practical path.

The survivor restores a narrow `.tfw/quickstart.md` modification: name the ordinary update/continuation entry, state that the target workflow discovers established facts and preserves project-owned state, and link the canonical workflow for details. It carries no algorithm, question list or completion claim. This is an architectural reachability result, not evidence that an owner noticed or understood it.

The common adapter overview already declares plural `.agents/rules` and `.agents/workflows`, the manifest as the tooling-only map, and declared/tracked/installed/live evidence levels. Its falsifier is also not reproduced. The physical twelve-path move plus manifest parity supplies the source fix.

Therefore `.tfw/quickstart.md` is retained for a narrow discovery change; `.tfw/adapters/README.md` remains unchanged.

### C7 — Antigravity-specific compatibility wording must change

The Antigravity README says singular `.agent/*` is “obsolete.” Current Google documentation says Antigravity defaults to plural `.agents/rules` but retains backward support for singular `.agent/rules` ([Google Antigravity Rules](https://antigravity.google/docs/rules-workflows)). “Legacy-supported” is not “canonical for new installation,” but it is also not “unsupported and safe to clean.”

The survivor therefore keeps a narrow `.tfw/adapters/antigravity/README.md` modification: plural targets are canonical for TFW install/repair; singular vendor paths may remain supported legacy/foreign neighbors; move only the twelve manifest-selected TFW files; never delete unrelated singular content. This makes no claim about native execution and adds no provider mode.

### C8 — Generic release, optional project contract and self-hosting mechanics remain three jobs

The generic workflow must identify requested output/audience, read an optional project contract, separate prepare/integrate/publish effects, apply project-declared readiness, obtain missing consequential authority, and report the actual state. It must not require `.tfw/VERSION`, Git, SemVer, changelog or task DONE unless the project contract names them. Missing `RELEASE.md` is a valid no-release/missing-contract route to `/tfw-plan`, not a generic failure.

The project template must express application/document/data releases, `None` versioning, project-selected inputs/checks/effects and no release. Root `RELEASE.md` retains this repository's payload, SemVer, version/changelog/migration, isolated composition, exact task evidence intake, tests, commit/tag and separately authorized push/publication mechanics.

The two byte-identical Codex routers still need a narrow paired change because they currently describe only a “versioned release” and require `RELEASE.md` before the canonical workflow can diagnose absence. Full Claude and Antigravity workflow copies change with the canonical route. No release engine is needed.

### C9 — Exact final entity dispositions

The full revision-2 TS contains 38 logical VALUE rows. Challenge retains 35 and removes three. The count is an analytical proposed selector, not a measured Candidate result; touched LOC, maintenance cost, reliability and comprehension are unmeasured.

| Original proposed entity or exact group | Final disposition | Reader/job test |
|---|---|---|
| `.tfw/README.md` | **Keep MODIFY** | Framework-owned current methodology; legacy project purpose preserved elsewhere. Removing withholds current values. |
| `.tfw/conventions.md` | **Keep MODIFY** | One shared definition for README ownership/baseline dereference, receipt lifecycle, A3 effect boundary and generic/project release authority. |
| `.tfw/glossary.md` | **Keep narrow MODIFY** | Define PV/receipt/incidental-trace/optional-release terms once; no algorithm. |
| `.tfw/workflows/update.md` | **Keep MODIFY** | Sole target update algorithm and full successor of the removed guide. |
| `.tfw/workflows/init.md` | **Keep MODIFY** | New/attach ownership transition must agree with update. |
| `.tfw/workflows/release.md` | **Keep MODIFY** | Domain-neutral release route; consumes project-named inputs/effects. |
| `.tfw/workflows/handoff.md` | **Keep narrow MODIFY** | Admit selected stable sibling TRACE at exact-path/Candidate gate without task closure. |
| `.tfw/workflows/review.md` | **Keep narrow MODIFY** | Verify A3 five-way boundary and conditional legacy-purpose resolution. |
| `.tfw/templates/briefing.md` | **Keep MODIFY** | State-specific outcome/benefit/limitation/next-action projection. |
| `.tfw/templates/update_receipt.md` | **Keep CREATE** | Minimal immutable attempt observation/recovery record; no current-state authority. |
| `.tfw/templates/HL.md` | **Restore/keep narrow MODIFY** | Future HL cites current preserved purpose locus; historical HL is never retargeted. |
| `.tfw/templates/review/judge.md` | **Restore/keep narrow MODIFY** | Separate current P0 authority from historical Git/attachment evidence when an old path became framework-owned. |
| `.tfw/templates/RELEASE.md` | **Keep MODIFY** | Optional domain-neutral project contract, including no-release/unversioned forms and project input/effect choices. |
| root `RELEASE.md` | **Keep MODIFY** | Concrete TFW release mechanics plus effect-selected, epoch/topology-correct task/phase evidence intake. |
| `.tfw/quickstart.md` | **Restore/keep narrow MODIFY** | Receiving owner practical path must reach ordinary update before invocation; canonical workflow owns all details. |
| `.tfw/adapters/README.md` | **Remove from selector / unchanged** | Current plural topology and evidence-level wording already correct. |
| `.tfw/adapters/antigravity/README.md` | **Keep narrow MODIFY** | Correct “obsolete” into canonical-plural/bounded-legacy wording; forbid foreign-neighbor cleanup inference. |
| `.tfw/migrations/update-experience.md` | **Remove CREATE** | Target `update.md` + applicable versioned changelog/migration are the exact successor chain. |
| CRUE `deliverables/RELEASE-NOTES.md` | **Remove CREATE** | Actual accepted task/phase governing evidence + effect-selected root release intake are the exact successor chain. |
| Claude copies of update/init/release/handoff/review | **Keep five MODIFY** | Exact full copies of changed canonical workflows; no independent authority. |
| canonical + installed Codex `tfw-release/SKILL.md` | **Keep two narrow MODIFY** | Do not pre-impose version/contract existence before canonical diagnosis. |
| `.agent/rules/tfw.md → .agents/rules/tfw.md` | **Keep RENAME** | Match declared/current plural rule target; leave foreign singular neighbors. |
| eleven `.agent/workflows/tfw-*.md → .agents/workflows/tfw-*.md` | **Keep eleven RENAMEs; five also MODIFY** | Match declared plural targets; update/init/release/handoff/review copies follow changed canon. |

### C10 — Exact proposed path/action list for C3-R

| # | Exact path | Action | Required result |
|---:|---|---|---|
| 1 | `.tfw/README.md` | MODIFY | Framework ownership/current methodology; no project-purpose loss |
| 2 | `.tfw/conventions.md` | MODIFY | Shared ownership, receipt, baseline-purpose, A3 and release boundaries |
| 3 | `.tfw/glossary.md` | MODIFY | Precise non-duplicated terms only |
| 4 | `.tfw/workflows/update.md` | MODIFY | Complete taskless target update/recovery/communication algorithm |
| 5 | `.tfw/workflows/init.md` | MODIFY | Coherent new/attach README ownership transition |
| 6 | `.tfw/workflows/release.md` | MODIFY | Domain-neutral optional-project release route |
| 7 | `.tfw/workflows/handoff.md` | MODIFY | A3 selected sibling TRACE pre-commit/Candidate rule |
| 8 | `.tfw/workflows/review.md` | MODIFY | A3 verification and conditional legacy-purpose resolution |
| 9 | `.tfw/templates/briefing.md` | MODIFY | Outcome/benefit/limit/next action by observed state |
| 10 | `.tfw/templates/update_receipt.md` | CREATE | Immutable attempt record and attachment reference shape |
| 11 | `.tfw/templates/HL.md` | MODIFY | Future preserved-purpose citation; no historical retarget |
| 12 | `.tfw/templates/review/judge.md` | MODIFY | Current-authority versus legacy-path evidence resolution |
| 13 | `.tfw/templates/RELEASE.md` | MODIFY | Optional project-owned output/input/readiness/effect contract |
| 14 | `RELEASE.md` | MODIFY | Concrete TFW mechanics and selected-effect task/phase evidence intake |
| 15 | `.tfw/quickstart.md` | MODIFY | Receiver-facing ordinary update/continuation discovery; canonical link, no duplicate algorithm |
| 16 | `.tfw/adapters/antigravity/README.md` | MODIFY | Plural canonical, singular legacy-supported, foreign-safe wording |
| 17 | `.claude/commands/tfw-update.md` | MODIFY | Exact canonical full copy |
| 18 | `.claude/commands/tfw-init.md` | MODIFY | Exact canonical full copy |
| 19 | `.claude/commands/tfw-release.md` | MODIFY | Exact canonical full copy |
| 20 | `.claude/commands/tfw-handoff.md` | MODIFY | Exact canonical full copy |
| 21 | `.claude/commands/tfw-review.md` | MODIFY | Exact canonical full copy |
| 22 | `.tfw/adapters/codex/skills/tfw-release/SKILL.md` | MODIFY | Thin optional/unversioned/no-contract router |
| 23 | `.agents/skills/tfw-release/SKILL.md` | MODIFY | Exact installed thin router |
| 24 | `.agent/rules/tfw.md → .agents/rules/tfw.md` | RENAME | Declared plural rule target |
| 25 | `.agent/workflows/tfw-config.md → .agents/workflows/tfw-config.md` | RENAME | Declared plural workflow target |
| 26 | `.agent/workflows/tfw-docs.md → .agents/workflows/tfw-docs.md` | RENAME | Declared plural workflow target |
| 27 | `.agent/workflows/tfw-handoff.md → .agents/workflows/tfw-handoff.md` | RENAME/MODIFY | Plural target plus changed full copy |
| 28 | `.agent/workflows/tfw-init.md → .agents/workflows/tfw-init.md` | RENAME/MODIFY | Plural target plus changed full copy |
| 29 | `.agent/workflows/tfw-knowledge.md → .agents/workflows/tfw-knowledge.md` | RENAME | Declared plural workflow target |
| 30 | `.agent/workflows/tfw-plan.md → .agents/workflows/tfw-plan.md` | RENAME | Declared plural workflow target |
| 31 | `.agent/workflows/tfw-release.md → .agents/workflows/tfw-release.md` | RENAME/MODIFY | Plural target plus changed full copy |
| 32 | `.agent/workflows/tfw-research.md → .agents/workflows/tfw-research.md` | RENAME | Declared plural workflow target |
| 33 | `.agent/workflows/tfw-resume.md → .agents/workflows/tfw-resume.md` | RENAME | Declared plural workflow target |
| 34 | `.agent/workflows/tfw-review.md → .agents/workflows/tfw-review.md` | RENAME/MODIFY | Plural target plus changed full copy |
| 35 | `.agent/workflows/tfw-update.md → .agents/workflows/tfw-update.md` | RENAME/MODIFY | Plural target plus changed full copy |

Excluded from this proposed selector: `.tfw/adapters/README.md`, `.tfw/migrations/update-experience.md`, and `workspace/2026/TFW_20260906-190312_CRUE/deliverables/RELEASE-NOTES.md`. Challenge authorizes no implementation; `/tfw-plan` owns any TS revision and exact acceptance.

### C11 — Hypotheses after attack

| Hypothesis | Challenge result | Evidence limit / remaining obligation |
|---|---|---|
| H5 | **SUPPORTED architecturally.** Existing carriers can express A3's five cases and A4's generic/project split without a registry/engine. | Exact text and source-derived/native scenarios must still prove behavior; failure preserves an explicit proposal/cost, never narrows A3. |
| H6 | **SUPPORTED with one carrier type.** Receipt history plus distinct content-addressed attachments and current re-observation survives C0/C1/C4 counterexamples. | Native interruption/repeat behavior is unobserved; receipt must never become current state. |
| H7 | **SUPPORTED only as authority-path simplification.** The guide and CRUE release-note file are removable through exact successor chains; HL/judge, quickstart and Antigravity readers were restored where removal failed. | No maintenance, reliability, execution-cost or owner-comprehension improvement was measured. Later bounded evidence must qualify those claims. |

### C12 — External evidence and active counterevidence

| Primary source | Challenge use | Transfer limit |
|---|---|---|
| [Git revisions](https://git-scm.com/docs/gitrevisions) | `<rev>:<path>` gives exact historical bytes for a tracked path at a freeze | Cannot recover an untracked source and does not define current Project North Star authority |
| [CommonMark §6.3](https://spec.commonmark.org/0.31.2/#links) | A Markdown link carries a destination URI, not a repository revision | Renderer navigation behavior varies; this does not itself prescribe Git |
| [Git commit](https://git-scm.com/docs/git-commit) | Exact pathspec/`--only` isolates selected paths from unrelated staged content | Does not decide TRACE effects, authorship, privacy or task completion |
| [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) | Separates entity/activity/agent, opposing inference that co-commit equals sibling completion | Does not require a TFW provenance schema or file |
| [Google Antigravity Rules](https://antigravity.google/docs/rules-workflows) | Current plural default plus explicit singular-rule backward support | Does not prove TFW native command execution or every singular workflow behavior |

No web search query was needed in Challenge; five exact primary pages were opened or reopened and their relevant Git/CommonMark/W3C/Google sections were inspected. This satisfies stage external research without surveying for quota. No external source is treated as TFW instruction authority.

### C13 — Material unknowns that remain

No architectural unknown requires iteration 4. Three behavioral facts remain deliberately unclaimed and belong to the already planned implementation/evidence gates:

1. Whether a fresh native agent distinguishes current owner-authorized purpose from historical Git/attachment evidence and refuses to inherit P0 into the replacement framework README.
2. Whether existing task/writer/path traces are sufficient for a reviewer to attribute every selected sibling TRACE case without a new carrier.
3. Whether an owner understands the final state-specific briefing; message emission alone cannot establish this.

If item 2 fails in a concrete source-derived scenario, the implementation returns to `/tfw-plan` with the exact failing case and carrier/change cost. No new field campaign, provider unit or automatic research iteration is authorized.

## Challenge Decisions

| # | Decision | Basis |
|---|---|---|
| CD1 | Select C3-R as the single minimal full survivor: 35 analytical logical VALUE rows / 47 literal source-destination paths, with 22 MODIFY + 1 CREATE + 12 RENAME (five content-changing). | It passes every required case after restoring failed reader removals; three removed rows have complete successor chains. |
| CD2 | Restore `.tfw/templates/HL.md` and `.tfw/templates/review/judge.md`; never retarget historical HLs, but do not freeze all P0 content. Use Git-at-freeze for tracked historical evidence and receipt-bound preserved bytes for untracked legacy purpose; current owner-authorized North Star remains authority. | Actual CRUE freezes demonstrate same-spelling/different-bytes; Git supplies only one evidence route, while the approved transition explicitly includes untracked legacy content. |
| CD3 | Keep the frozen selected-stable sibling TRACE case and align conventions/handoff/review/update/release plus copies; add no provenance protocol unless tests expose a concrete attribution gap. | Existing semantic/evidence carriers can state and verify the five-way boundary. |
| CD4 | Reject full-task reuse for ordinary update; retain one project-owned receipt type plus current-state re-observation. | Current update Role Lock/read contract is deliberately taskless; task lifecycle is a different authority/outcome. |
| CD5 | Remove the version-independent guide only through target update → applicable changelog/versioned migration; remove CRUE release notes only through selected effect → actual epoch/topology-correct task/phase evidence → root release intake → future changelog/migration. | These are exact reader chains with hard-stop counterexamples, not assumed discoverability or a new root-artifact ceremony. |
| CD6 | Keep Antigravity-specific compatibility repair, remove common adapter overview change, and move exactly the twelve selected TFW paths. | Vendor docs distinguish plural default from singular backward support; foreign cleanup remains forbidden. |
| CD7 | Treat path count as an analytical selector proposal only. | No Candidate diff, LOC, cost, reliability, maintenance or comprehension measurement occurred. |

## OODA Record

| Loop | Observe | Orient | Decide | Act |
|---|---|---|---|---|
| 1 | Replayed all 36 dimension pairs and attacked C0–C4 with frozen A3/A4, current Role Locks and exact reader contracts. The CRUE freeze history showed one HL link with two `.tfw/README.md` blobs. | C0/C1/C4 fail required authority/recovery cases; first-draft C3 fails purpose and release-handoff reads; C2 remains complete but duplicates carriers. | Repair C3 rather than defend 32: restore HL/judge readers and exact root release intake; retain C2 until successor paths are proven. | Wrote Consistency Check and C1–C5 with observed blob IDs, hard-stop cases and exact reader chains. |
| 2 | Checked target-update routing, root/global release contracts, RF/REVIEW/status inputs, receiver-facing command discovery, adapter claims and primary Git/CommonMark/W3C/Google sources. | Guide/release-note/common-adapter changes have no unique job after explicit successor edges; quickstart and Antigravity-specific wording still do. | Select 35-row C3-R, dispose all 38 original rows, preserve three behavioral unknowns and forbid measured-benefit claims. | Wrote C6–C13, exact proposed list, hypothesis results and seven decisions. |

## Checkpoint

| Found | Remaining |
|---|---|
| One minimal full survivor, C3-R, with exact 35-row / 47-literal-path proposed action list and all 38 original entity dispositions | `/tfw-plan` must decide/revise the TS; Researcher may not mutate it |
| A replaced legacy North Star path must resolve through current project authority plus historical Git/attachment evidence; old HLs are never retargeted and P0 is not universally frozen | Implementation/native review must verify tracked, untracked, later-owner-change and ambiguous-designation cases |
| A3's selected stable sibling TRACE case fits existing carriers as a five-way semantic boundary | Source-derived and native scenarios must test attribution, exact selection and sibling noncompletion; failure preserves an explicit gap/cost |
| Ordinary update remains taskless; receipt is immutable history and current receiver observation remains authoritative | Interruption/repeat scenarios remain implementation evidence, not Challenge observations |
| Removed guide and release-note jobs have exact updater and future-release successor chains | TS acceptance must name those chains; missing edge restores the removed carrier |
| Three removals: common adapter overview, update-experience guide, CRUE release-note file | No further removal is supported by this stage |
| Three behavioral unknowns remain qualified; no iteration 4 or new campaign is needed/authorized | Later bounded evidence may revise implementation wording, not frozen scope |

**Sufficiency:**

- [x] External source used? Exact Git, CommonMark, W3C and Google primary sources were inspected with transfer limits.
- [x] Briefing gap closed? Yes. Minimality was tested against no-carrier, full-task, full-TS and registry alternatives, and every removal has a complete reader chain/counterexample.
- [x] Pairwise incompatibility checked? All 36 D1–D9 pairs were audited; incompatible selections and conditions are recorded.
- [x] Surviving configurations listed? C3-R is the single minimal full survivor; C2 is explicitly dominated rather than falsely called invalid.
- [x] At least one HL §10 hypothesis tested? H5–H7 have Challenge results and evidence limits.
- [x] Counterevidence sought? Historical blob drift, task Role Lock, selected sibling trace, stale receipt, missing release intake, and vendor legacy support all forced retained/changed dispositions.
- [x] Deep exit criteria met? Seven decisions, all three hypotheses, two OODA loops, external research, every-entity disposition, exact proposed selector and metacognitive limits are complete.

**Metacognitive check:** The challenge increased the leading selector from 32 to 35 because three attempted reader removals failed. That is evidence against optimizing the count. The three remaining removals are supported by exact successor reads, not by shorter prose preference. No field behavior, reliability, maintenance effort, LOC or owner comprehension was observed.

**Recommendation:** Close Challenge and proceed to RES synthesis after direct-parent acceptance. Synthesis should recommend C3-R, carry the 35-row / 47-literal-path list and three behavioral unknowns, and route the TS change to `/tfw-plan`; it must not implement, release, start iteration 4 or claim measured convenience.

Stage complete: YES
→ User decision: pending — direct parent Robert, unit `01a0766c-8096-7a83-af60-f70c248290bc`
