# Extract — Shared provenance form, local carriers, separate proof obligations

> **Mindset:** Analyst; compare concrete configurations without selecting a survivor before Challenge.
> **Mode:** deep, two passes.
> **Parent:** [HL](../../HL-TFW_20260928-201325_SHI.md); frozen authority `f0a8aebbb11686f16081f29b86b96a9d8aa172cf`.
> **Goal:** Make the minimum contract/file alternatives and later real trial reviewable.
> **Producer:** `codex:thread:local:01a0e909-5023-7ca0-b006-72b639f258c8`.
> **Coordinator / recipient:** `codex:thread:local:01a0e88a-41cb-75b0-b36f-0e8491af8dc2`.
> **Activation:** unchanged iteration-2 dispatch at `e419f2eed7360202c0a472d53fe8cf741a19cc70`; Coordinator accepted Gather `e8deb74c68e853422dd2dd52ed015dd792ae1957` and directed this Extract.
> **Authority limits:** research only; no source/template edits, entitlement changes, pilot, phase launches or owner questions.

## Configuration Space

This is a covering set of materially different combinations, not the several-thousand-row Cartesian product. It retains the Gather dimension names and includes the no-change control. The configurations remain unselected; coverage limits describe what each proposes to cover, not a verdict.

| Config | Durable carrier | Coverage boundary | Context reference granularity | Entry and continuation observation | Current-plan evidence | Trial isolation |
|---|---|---|---|---|---|---|
| E0 current control | Existing current events/results | Current rules | Current producer/authority fields | Existing bindings/source checks | Unavailable; cached Pro only | Observed separate OS sessions; trial pending |
| E1 existing-only | Existing lawful event or owned artifact | Task-bound Full work | Full first context, later exact reference | Explicit declaration; recheck changes | Current authorized Billing/contract evidence required | Separate OS users/access boundaries |
| E2 hybrid component | Existing owned artifact; local fallback receipt where none is timely/lawful | All material Full operations, including pre-task/taskless | One shared form; full context once, bounded references later | Explicit launch declaration; new context on material change | Same required evidence; currently unavailable | Separate OS users/access boundaries |
| E3 universal receipt | One local receipt per material unit launch/context | Same Full boundary | Receipt links exact governed acts/results | Same explicit declaration/recheck | Same required evidence; currently unavailable | Separate OS users/access boundaries |
| E4 distributed forms | Existing artifacts plus fallback receipt | Same Full boundary | Fields/hooks separately installed into all applicable artifact templates | Same explicit declaration/recheck | Same required evidence; currently unavailable | Separate OS users/access boundaries |
| E5 external source | Supported preserved external evidence | Selected shared-host Full launches | Exact external source from each effect | External declared or verified identity, explicitly distinguished | Actual contract and access evidence | Separately bounded containers/credentials/mounts |
| E6 repo-specific | Commit message plus existing artifacts | Git-consuming task-bound and taskless operations | Commit-scoped context | Explicit declaration/recheck | Actual plan evidence | Separate OS users/access boundaries |

E2's common template component plus fallback is new relative to Briefing's broad “existing versus dedicated” distinction. E1's narrower boundary and E6's Git dependency require explicit comparison with portability and frozen coverage; neither silently redefines the HL. Any isolation transport may change independently of the carrier if equivalent proof is supplied; no inference that a container or separate UID alone passes the trial.

## Findings

### E-A — A launch is an activity context, not another person or host registry

[W3C PROV-DM §§2.1.3, 2.2.1.2 and 5.3.3](https://www.w3.org/TR/2013/REC-prov-dm-20130430/), reread 2026-09-28, distinguishes attribution to an entity from responsibility for an activity and association with a plan. This supports the conceptual separation used here; it does not require adopting PROV syntax, an ontology service or a new TFW runtime. The actual TFW distinctions/authority come from the frozen HL and existing conventions.

For E2/E3/E4, the minimum semantic content under examination is:

| Subject | Record or resolve from an exact existing source | What it must not imply |
|---|---|---|
| Project and work | Inspectable project root/locator at the observation; exact task/phase, or explicit pre-task/taskless operation and bounded effect | A new global project ID or an invented task |
| Original author and accountable owner | Original governing artifact and actual authority source, retained at its epoch | Launcher becomes author/owner by opening the project |
| Declared initiator | The declaration and its actual source; self-declared/weak assurance, or explicit unknown/conflict | Authentication, approval or evidence of physical presence |
| Optional stable principal | Existing valid project profile and explicit attribution source when actually required | One new profile for each run; host/account becoming principal |
| Client device | Observed or declared value with source/assurance; otherwise unknown | IP, OS user, server hostname or XRDP session automatically identifies a person's device |
| Execution host | Owner-selected stable name, source of that designation, and bounded observed attributes/time that relate this run to it | Global uniqueness, hardware attestation or authority from an owner-like name |
| Actual working unit | Native unit address, role and parent/source edge already required by ATC | Pending client handle, title or shared principal substitutes for the actual unit |
| Permission | Exact immutable governing authority and activation/dispatch/selection source applicable to this operation | The provenance record grants a mandate |
| Context epoch | Actual observation/declaration time and source identity; changed context gets a new section/record | Timestamp alone proves trustworthy identity |
| Material acts | Exact output/changed path or bounded artifact section plus revision/evidence identity at its gate | A log of every click/token, or a self-referential future SHA |

This is a semantic list, not ten mandatory duplicated strings on every output. Existing source references can carry author, owner and mandate. A copied artifact keeps original production context; a new copying/continuing unit records its own operation separately. Host migration, changed declared person/principal, unit/authority or material scope creates new context; an unchanged same-unit continuation reuses the verified source. A child role is launched by a Coordinator unit: its source must say so and retain the actual originating human declaration rather than invent a new human click for every agent.

For missing declaration, record unknown and resolve only the authority that depends on the human source. In the later trial, unknown cannot satisfy the required two actual declared initiators. Existing authority checks remain stronger than attribution and can independently stop action.

### E-B — The timely carrier algorithm, including failure paths

E2 would have one proposed shared template, `.tfw/templates/launch_provenance.md`. It would own both a full-context block and a short exact-source reference form. This path does not exist yet. `.tfw/conventions.md` would explicitly permit that common component before/in an artifact's own body while retaining each existing template's section ownership. Without that explicit composition rule, silently adding arbitrary fields contradicts current `Artifact-owned semantic sections`.

1. Resolve current activation and declaration before the first material write. Reuse an applicable explicit source; do not ask the same human again merely because a new tool call ran.
2. Use the first timely, role-owned durable artifact for the full block: Research Briefing, Executor ONB, Reviewer Map, or an existing Coordinator planning/decision artifact. Save that source before dependent material acts. Later artifacts carry the short source reference; acts with no suitable document surface are identified in the owning source's bounded checkpoint section.
3. If no timely rightful artifact exists, use a project-owned fallback at proposed `.tfw/launches/LAUNCH__<actual-stamp>__<opaque-token>.md`. The name is local uniqueness, not a principal, session registry or global allocator. No directory is created for projects that never need a fallback. New-task Plan and full-init need this pre-task case; Config edit, taskless Docs/Knowledge effect, Init repair and constrained release outputs may need it. Update needs an initial source before writes because its existing completion receipt is sealed only after verification.
4. The fallback is owned by the acting Coordinator in these E2 cases. Write only the currently known source/scope before dependent writes, then append bounded observed effects at the normal gate. Preserve previously sealed sections/epochs; do not overwrite old declarations. A stopped attempt records its actual incomplete outcome when an orderly return is possible. A crash leaves the pre-action context, not invented completion. An exact committed source or preserved evidence identifies each sealed checkpoint; never put the future commit SHA inside its own bytes.
5. A later task's first actual owned source refers to the pre-task record; do not rename it, fabricate an earlier task ID, migrate old events or insert an escaping path into journal frontmatter `refs`. A body source locator can resolve the project-local receipt without changing that closed refs schema. The source is not added to live status.
6. Distinguish a read-only advisory invocation from an authority-bearing durable decision. Config Verify keeps its write-nothing behavior; an actual approval/authorization remains in its existing authority-owned carrier. No compulsory receipt is generated for every harmless read.

E3 instead gives each producing role its own receipt permission, even where Briefing/ONB/Map already suffice; the receipt records result paths so a separate new header in every existing artifact is not needed. It still needs exact source linkage in the normal return, unique local paths, immutable checkpoints, preservation and interruption semantics. E4 composes the same information by editing individual output forms rather than one shared component. Challenge must test whether the E2 composition rule is simpler in actual use or merely hides repeated complexity.

### E-C — Exact candidate E2 file map and deletion alternatives

This is a **proposed 37-file implementation envelope: 36 existing files plus one new template**, not an approved TS denominator. It separates semantic sources from exact installed copies; classification/LOC and any development-discovered extra dependency still require Coordinator/owner treatment. No code, tests, host files or task records are changed by this research. Runtime receipt instances are outputs of later real operations, not additional framework templates.

| Exact source file | Purpose/value | Dependency and deletion alternative |
|---|---|---|
| `.tfw/conventions.md` | Own subject/assurance/host rules, shared component composition, change/reuse timing, fallback permissions and project-history preservation | Touch only relevant identity, artifact-section, Role Lock, file-classification ranges plus new uniquely named provenance range. Deleting this requires duplicating semantics across ten workflows. |
| `.tfw/templates/bindings.yaml` | Preserve personal-machine mapping and explicitly bound shared-host use | Comments/usage semantics only; no second key kind. Shared sessions resolve required attribution from their declaration/source instead of guessing from a machine-wide mapping. Removing this clarification leaves the user-facing template contradicting the new shared-host rule. |
| **New** `.tfw/templates/launch_provenance.md` | Own one complete form, reference form and fallback framing | Existing forms compose this one component. Deleting it requires the distributed-form alternative or duplicating field definitions in workflows. |

Each workflow below needs an explicit ordered read of the new shared range/form at its current activation point; Config must expressly admit that selected range rather than illegally reading an unregistered range. Every row has its own placement and lawful writer, so one root instruction cannot replace this table.

| Exact canonical workflow | Exact present copy to synchronize | Local duty / loss if removed |
|---|---|---|
| `.tfw/workflows/plan.md` | `.claude/commands/tfw-plan.md` | Pre-task fallback, later HL/TS/phase/continuation context; missing row loses new-task/phase coverage. |
| `.tfw/workflows/research/base.md` | `.claude/commands/tfw-research.md` | Briefing full source and stage/RES references; missing row loses first-stage and resumed-context coverage. |
| `.tfw/workflows/handoff.md` | `.claude/commands/tfw-handoff.md` | ONB source, implementation/EV/RF checkpoint linkage and changed continuation; missing row loses execution provenance. |
| `.tfw/workflows/review.md` | `.claude/commands/tfw-review.md` | Map source before independent work; subsequent stage/verdict linkage; missing row loses reviewer attribution before REVIEW. |
| `.tfw/workflows/docs.md` | `.claude/commands/tfw-docs.md` | Lawful owned record/effect source or Coordinator fallback for batch/reference-only work; missing row leaves taskless documentation gap. |
| `.tfw/workflows/knowledge.md` | `.claude/commands/tfw-knowledge.md` | Source versus current qualifier retained; fallback only for a material effect without a rightful carrier; missing row conflates origin and current operation. |
| `.tfw/workflows/release.md` | `.claude/commands/tfw-release.md` | Full-side provenance beside project-defined output without forcing Git or changing Daily; missing row loses non-document release effects. |
| `.tfw/workflows/init.md` | `.claude/commands/tfw-init.md` | Pre-task setup and taskless repair sources, preserve receiver launch history; missing row leaves writes before init task uncovered. |
| `.tfw/workflows/update.md` | `.claude/commands/tfw-update.md` | Pre-write source, existing completion receipt reference and preservation exclusion for receiver `.tfw/launches/`; missing row risks losing history on update. |
| `.tfw/workflows/config.md` | `.claude/commands/tfw-config.md` | Limited provenance read/write exception for Edit; Verify stays read-only; missing row leaves an explicit Role Lock/read-contract conflict. |

Seven Coordinator wrappers need the same narrow fallback permission. Their exact installed pairs are:

| Exact source | Exact installed copy | Why existing wording is insufficient |
|---|---|---|
| `.tfw/adapters/codex/skills/tfw-plan/SKILL.md` | `.agents/skills/tfw-plan/SKILL.md` | Permitted HL/TS list does not include a pre-task receipt. |
| `.tfw/adapters/codex/skills/tfw-docs/SKILL.md` | `.agents/skills/tfw-docs/SKILL.md` | Selected records/documentation ranges do not clearly allow a separate launch receipt. |
| `.tfw/adapters/codex/skills/tfw-knowledge/SKILL.md` | `.agents/skills/tfw-knowledge/SKILL.md` | Human records/current effect refs must not be stretched into generic operation history. |
| `.tfw/adapters/codex/skills/tfw-release/SKILL.md` | `.agents/skills/tfw-release/SKILL.md` | Only selected project release artifacts/effects are presently authorized. |
| `.tfw/adapters/codex/skills/tfw-init/SKILL.md` | `.agents/skills/tfw-init/SKILL.md` | Explicitly distinguish receiver history receipt from setup/config and init-task RES/RF. |
| `.tfw/adapters/codex/skills/tfw-update/SKILL.md` | `.agents/skills/tfw-update/SKILL.md` | Make project-owned launch history creation/preservation explicit beside framework/config merges. |
| `.tfw/adapters/codex/skills/tfw-config/SKILL.md` | `.agents/skills/tfw-config/SKILL.md` | Present allowlist is config/registered ranges/adapters, not operation receipts. |

Count: two existing common sources + twenty workflow/copy files + fourteen wrapper/copy files + one new template = 37. Gather proved all ten present command and skill pairs equal before changes. The copy map itself is unchanged. Cursor commands are absent here; a selected receiving installation copies revised workflows through the existing map. Antigravity already shares the installed skill paths, so no duplicate command family is added.

**Concrete alternatives and unchanged files:**

- E3 uses the same two common sources, new template and twenty workflow/copy files, but permits separate receipts in all ten wrapper pairs: **43 files**. It avoids a generic artifact-prefix composition rule but creates a new receipt for each material unit launch/context, including ordinary Researcher/Executor/Reviewer work.
- E4 replaces E2's common-prefix use with explicit hooks in eighteen current forms: `.tfw/templates/HL.md`, `TS.md`, `ONB.md`, `RF.md`, `RES.md`, `REVIEW.md`, `research/1_briefing.md`, `research/2_gather.md`, `research/3_extract.md`, `research/4_challenge.md`, `review/map.md`, `review/verify.md`, `review/judge.md`, `evidence/EV.md`, `knowledge/record.md`, `knowledge/handover.md`, `journal/event.md`, `update_receipt.md`. These paths all share prefix `.tfw/templates/`; each is an existing file. Keeping the reusable field form plus those hooks makes **55 files**, with more hook-maintenance sites but no generic composition exception. A later simplification must explain each omitted first-write/return form.
- E2 leaves those eighteen forms' body schemas unchanged because the single shared component owns the added preamble/reference. It does not add status keys, journal kinds/frontmatter keys, new task IDs, profile keys or binding key kinds.
- No changes proposed to `.tfw/adapters/manifest.yaml`, persistent adapter/root blocks or Coordinator profiles: routing and canonical discovery remain unchanged. Research/Handoff/Review wrappers keep their existing owned-artifact permissions in E2.
- No mandatory host file, host registry, second per-user configuration, runtime, provider API or schema service is proposed. Stable host designation/source is carried directly in the selected launch context and reused when verified unchanged.
- No current `team/` profile, local `.tfw/bindings.yaml`, project config, HL history or existing receipt is rewritten. Migration is forward-only interpretation: old traces retain their actual unknowns; personal bindings remain readable; a shared host never retroactively names an initiator.
- `.tfw/compilable_contract.md` currently compiles templates/workflows and task Markdown but not arbitrary `.tfw/` receiver history. The new template is already covered; launch receipt instances would remain source evidence, like update receipts, and must be referenced by exact source locator rather than promised as compiled site pages. Publishing receipt history would be a separate value/privacy decision; no generator change is included here.
- Release version/changelog and any versioned migration guide are not invented during research. A later release procedure selects them if needed. Phase A must still demonstrate adoption of the forward-only behavior on personal/shared cases; absence of a format conversion is not proof of migration correctness.

### E-D — Later real trial: two people, two projects, one named host

This is a proposed execution design, **not observed evidence**. Person A, Person B, Project A and Project B are role labels to be resolved in the later approved TS; no people, project paths or unit addresses are invented now. Two humans suffice: Person A authors Project A's HL on a personal computer; Person B later launches it on the shared host, while Person A launches Project B there. Author/launcher distinction is observable without requiring a third participant.

| Step and later owner | Actual operation | Oracle / retained non-secret evidence | Stop condition |
|---|---|---|---|
| 1. Coordinator/owner | Select actual permitted product/plan/access route, two people and two bounded real project tasks; approve Phase B scope and effects | Current authorized plan/contract/seat evidence, relevant terms and explicit economic decision; exact accepted TS/mandates | Shared-person individual login, absent required contract or unavailable participants: stop dependent pilot; return economic/scope choice. |
| 2. Person A / project authority | Produce and approve Project A HL on personal computer, publish through the approved project route | Original author/owner, personal-host launch context, exact published artifact revision and approval | Publication or approval is unobserved, or transport lacks authorization. |
| 3. Authorized receiving setup | Pull/copy that exact approved project to named `saubakirov-home-linux-01`; prepare Project B separately | Source/destination revision comparison; actual root paths, OS user/session/access observations, host-name source and current mapping to observed machine | Different or mutable authority source; host-name association unresolved; paths overlap. |
| 4. Each participant | Make their own explicit launch declaration and open distinct actual approved units | Two attributable declarations; weak assurance stated; actual unit/parent/role/mandate, client device observed/declared or unknown | One agent merely simulates both people; title/account/UID substitutes for declaration; unavailable exact unit. |
| 5. Authorized Executor(s) | Run bounded real work concurrently in the two projects | Overlapping observed session/unit activity intervals, distinct workspace/process ownership; project-specific useful output with ordinary required checks | No overlap, shared mutation path/credential context, wrong mandate or failed prerequisite. |
| 6. Authorized access check | Use harmless project-owned canary fixtures and known credential-directory permission metadata to test ordinary-user access boundaries | Own-project positive controls and cross-project denied read/write controls; no secret contents; evidence records identity and actual failure reason | Negative control skipped, shared UID with unconstrained access, broad mount/credential reuse, or denial attributed to wrong cause. |
| 7. One selected continuation | Change one material context or resume without a lifecycle transition, as explicitly authorized | New context/reference where needed; preserved earlier declaration; exact affected output checkpoint | Old context overwritten or assumed current after host/person/authority change. |
| 8. Independent Reviewer | Reconstruct each result from project files and returned evidence without unseen chats | Author, owner, launcher/assurance, device/unknown, named host, native unit, mandate, source/result revision and isolation controls | Any acceptance-critical lineage or isolation claim needs private chat reconstruction. |
| 9. Owner | Inspect actual revised Plan passages and two results; decide acceptance/economic arrangement | Explicit final human acceptance after independent review and economic disclosure | Trace demo is offered as the complete host/plan outcome, or savings are asserted without inputs. |

The access claim is scoped to ordinary project users and the selected setup. RES 1 observed privileged-capable groups; ordinary permissions do not establish isolation from an administrator. Session coexistence alone does not prove two humans, and home-directory metadata alone does not prove project/credential containment. The actual trial must measure the intended boundaries, preserve failed evidence and avoid broad secret reads. No permanent tests are proposed solely to inflate evidence: use bounded temporary controls and keep/remove them by the approved execution plan.

### E-E — Economic comparison has a formula but no evidenced numbers

For the same chosen period and materially comparable workload/capabilities, compare:

`separate total = actual person-A plan cost + actual person-B plan cost + applicable tax/admin costs`

`organizational total = actual committed seats/minimums + actual usage/overages + applicable tax/admin costs`

`API total = measured/estimated authorized workload charges + required client/feature costs + applicable tax/admin costs`

`saving = separate total - selected permitted total` only after those inputs are established. Common-host hardware/energy/admin cost belongs in both sides consistently if claiming total operating savings; sunk versus new expenditure must be stated. One invoice is not one End User account, and a positive subscription saving does not establish equal capability, concurrent capacity, model access or acceptable latency.

Gather's [official Billing evidence](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform) separates ChatGPT and API billing. The organizational candidate and multiple personal subscriptions are distinct economic alternatives; no selected plan, actual seat price, tax, committed term, workload or contract is currently verified for this pilot. **Current result: costs and savings unresolved; no replacement arrangement approved.**

## Deep-mode record and checkpoint

| Pass | Cross-check and counter-evidence | Research decision / new result |
|---|---|---|
| 1 | Gather coverage versus all wrapper permissions; existing `Artifact-owned semantic sections` versus a tempting workflow-only field insertion | Introduce the explicit shared-template component as an alternative; count narrow fallback permission in seven Coordinator wrapper pairs, including pre-task Plan. H2 cannot be closed by workflow prose alone. |
| 2 | Pre-action versus final receipt timing; update preservation rules and compiler source manifest versus an assumed automatically published receipt; real trial claims versus existing session evidence | Separate runtime receipt cost from framework file count, and source inspectability from site export. Keep the pilot and economic evidence as independent unresolved acceptance obligations. H3 still needs no registry in the proposed lookup path, but no live isolation success is inferred. |

**Metacognitive check:** new contributions are the 37/43/55-file concrete alternatives, the explicit composition dependency, pre-task/Update timing, preservation/export boundary and executable later observation sequence. These are design analyses, not evidence that E2 is already the correct minimum. Challenge must attack failure/interruption, omission, copying, principal ambiguity and the maintenance cost of the shared component before selecting a survivor.

**Resource boundary:** bounded excess over the soft file-read budget: selected HL/authority, stage/mode, identity/Role Lock/template-ownership conventions, bindings template, ten wrapper permission ranges, EV/handover forms and compiler manifest. Gather's measured copy checks are reused at the unchanged framework epoch; no unrelated history or other role context was read. An assumed `scripts/` lookup was absent; it supplied no evidence, and no generator-code claim is made.

**Knowledge handover:** source framework epoch remains `e419f2eed7360202c0a472d53fe8cf741a19cc70`; Gather at its full SHA above supplies current findings, selected P0–P7 remain unchanged. No new human Fact Candidate or owner choice arose. Intended recipient is the same Coordinator; implementation and actual entitlement/pilot remain outside this Researcher's authority.

| Found | Remaining |
|---|---|
| Concrete carrier algorithms and exact source/copy/template alternatives | Challenge necessity, burden, failure cases and contract fit; choose a research recommendation |
| Timely pre-task/taskless path and closed-schema compatibility approach | Verify no hidden conflict in composition/Role Locks and preservation |
| Actual pilot sequence, negative controls and independent reconstruction oracle | Later approved execution, actual people/plan/access and results |
| Explicit economic inputs/formula | Actual costs, comparable capability and owner choice |

- [x] External source used; limited conceptual application stated.
- [x] Briefing Extract gap closed to reviewable alternatives and explicit evidence limits.
- [x] Configuration space uses Gather dimensions; new combination exposed.
- [x] Two decisions, H2/H3 analysis and active counter-evidence recorded.

Stage complete: YES
Gate: WAIT — submit exact durable Extract path/SHA; recommend Challenge without implementation or pilot.
