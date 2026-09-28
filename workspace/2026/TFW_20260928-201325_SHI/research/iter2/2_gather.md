# Gather — First durable writes and carrierless operations

> **Mindset:** Explorer; inventory alternatives before selecting a design.
> **Mode:** deep; two OODA passes, active counter-evidence and independent contract/copy checks.
> **Parent:** [HL](../../HL-TFW_20260928-201325_SHI.md), frozen authority `f0a8aebbb11686f16081f29b86b96a9d8aa172cf`.
> **Goal:** Find exact provenance coverage gaps and supported entitlement evidence before proposing the minimum change set and later trial.
> **Producer unit:** `codex:thread:local:01a0e909-5023-7ca0-b006-72b639f258c8`.
> **Parent / return route:** `codex:thread:local:01a0e88a-41cb-75b0-b36f-0e8491af8dc2`.
> **Activation:** same-unit continuation, `journal/20260928-224203__dispatch__b7e2.md @ e419f2eed7360202c0a472d53fe8cf741a19cc70`; subsequent Coordinator acceptance of Briefing `3fd3f704200db4e2a05af40e9c01a9f80615f8dd` authorizes Gather only.
> **Selection:** baseline; native-gates; tfw-gates-only; no phase or implementation activation.

## Dimensions

Alternatives are investigative configurations, not recommendations or approved changes.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| Durable carrier | Existing lawful event or owned artifact | Dedicated local launch/operation receipt | Git commit message | Supported preserved external evidence |
| Coverage boundary | Task-bound Full work only | All material Full operations including taskless maintenance | Every invocation including read-only verification | Selected shared-host operations only |
| Context reference granularity | Complete inline context in every output | One exact source plus bounded references from outputs | Per-unit mutable current context | Context only in final result |
| Entry and continuation observation | Explicit per-launch declaration | Reuse unchanged declaration after checking current context | Infer human from OS/provider account | Verified identity supplied by an external system |
| Current-plan evidence | Supported current Billing/workspace surface | Actual applicable contract/seat evidence | Cached login claim | Catalogue availability only |
| Trial isolation | Separate OS users and access boundaries | Separate sessions under one UID | Containers with specifically bounded credentials/mounts | Separate physical machines |

## Findings

### G1 — Ten Full commands do not share one existing writable carrier

Source epoch for framework files below: `e419f2eed7360202c0a472d53fe8cf741a19cc70`; the later Briefing commit changes research only. Read the named workflow's Read Contract, Role Lock and operation checkpoint, then cross-check actual output forms/closed schema. The table describes current contracts; no new write permission is inferred.

| Canonical source | Current entry/read rule | First or material durable surface | Coverage consequence |
|---|---|---|---|
| `.tfw/workflows/plan.md` | Task control and Session identity; new owner-direct work has no prior task | First status/event and HL; later TS, selected Coordinator rulings/selection events | Resolve declaration before first task write; phase derivation and a later TS-producing invocation cannot inherit the author's machine as current host. |
| `.tfw/workflows/research/base.md` | Task/HL/iterations, Session identity and activation | `research/iterN/1_briefing.md`; subsequent stages; RES | Briefing has producer/activation slots; later stage templates do not. Final RES alone cannot identify an earlier material stage at its gate. |
| `.tfw/workflows/handoff.md` | Approved TS, exact Executor source and routing before ONB | ONB, implementation/evidence, RF; numbered returns | ONB and RF already preserve units/dispatch. A context-changing continuation needs a new bounded source even if no new onboarding file is created. |
| `.tfw/workflows/review.md` | Bootstrap resolves identity/independence before Map | `review/map.md`, then verify/judge, finally REVIEW | Final REVIEW producer header is too late to cover Map's first durable write. Stage-owned context is possible without allowing Reviewer to edit another role's artifact. |
| `.tfw/workflows/docs.md` | Actual Coordinator; task-bound or owner-direct manual batch | Selected documentation ranges, warranted technical record, current REVIEW effect reference | Manual batch creates no task/principal; architecture-only work need not produce a new knowledge record. No universal task journal exists. |
| `.tfw/workflows/knowledge.md` | Actual Coordinator; selected sources; task-owned or project-wide owner-direct | Warranted human record or selected owning qualification/closing reference | Existing record has source/producer/qualifier distinctions. Reuse, retain-only and justified-none do not warrant a new knowledge record merely to carry a launch. |
| `.tfw/workflows/release.md` | Full/Daily selected authority plus project-owned `RELEASE.md` | Only project-defined release output and metadata | The project contract chooses outputs. No universal Git, version/changelog/tag or extra Full artifact can be assumed; Daily remains outside this research's change scope. |
| `.tfw/workflows/init.md` | Exact owner-direct source; full-init versus attach/repair first | Full-init setup files, first status/event, RES/RF; repair modifies selected adapters only | Full-init writes before its task exists. Attach/repair skips init-task creation and Session identity checkpoint; report does not establish a standard durable receipt. |
| `.tfw/workflows/update.md` | Exact owner-direct source, immutable target; task route only when bound | Applied migration plus `.tfw/update_receipts/UPDATE__<stamp>__<four-hex>.md` | Existing immutable project-owned receipt is a suitable candidate surface, but it is sealed after verification. Do not pretend a future receipt existed before the first write. |
| `.tfw/workflows/config.md` | Selected project config/registry ranges; project-wide operation creates no task identity | Edit changes config/registered ranges/copies; Verify writes nothing | Task artifacts are forbidden. Adding launch data to project_config would confuse operation history with configuration; a new receipt would require explicit contract and wrapper changes. |

**Counterexample to the strongest reuse claim:** a taskless Config edit has no lawful task journal or owned task artifact. A Docs batch can change reference text without producing a knowledge record. A role's permission to report is not evidence that the report is preserved locally and immutably. Therefore “reuse existing task artifacts for all Full operations with no additional fallback” is not established.

**Counterexample to the simplest universal fallback:** Release explicitly declines a framework-wide Git prerequisite. Knowledge records accept an exact preserved source when Git is unavailable. Commit attribution is useful in this repository but cannot alone carry the portable rule across all consuming projects. Creating an artificial Full task for every maintenance action conflicts with the explicit taskless routes.

### G2 — Existing semantics can be reused, but timing and schemas matter

Cross-checked sources: `.tfw/templates/journal/event.md`, `.tfw/templates/status.md`, `.tfw/templates/{HL,TS,ONB,RF,RES,REVIEW}.md`, research/review stage templates, `.tfw/templates/knowledge/record.md`, `.tfw/templates/update_receipt.md`, and selected `Session identity`, `Commit Attribution`, `Current knowledge use`, `Knowledge handover` ranges in `.tfw/conventions.md`.

- Event frontmatter has a closed kind set and established attribution. Dispatch unit edges belong in its body/refs; a launch is not automatically a transition or dispatch. `refs` must resolve inside the owning task/phase, so a shared external receipt cannot simply be inserted there as an absolute path or escaping traversal.
- Live status describes task state/routing, not a mutable per-human/per-host roster. New provenance does not warrant duplicating status or changing its seven-field coordination selection.
- HL/TS author, accountable owner, declared launcher, native working unit, exact mandate, execution host and source/qualifier are different subjects. A record copied to another host retains its original producer; the copy operation must not rewrite that history.
- Research Briefing and ONB have useful first-artifact slots; Review's Map lacks the corresponding producer header. Existing RES/RF/REVIEW lineage is useful for references, not proof of all prior launches.
- Update's receipt already states authority, source, receiver and effects. Knowledge's record already distinguishes original source from current producer and qualifier. Extending those semantics is a candidate; inserting generic identity logs into accepted knowledge is not automatically justified.
- `Knowledge handover` permits a minimal fallback only under an owning task when no suitable return source exists. That rule does not currently authorize taskless launch receipts or a second global index.

Three questions must remain separate at Extract: what is declared before action; where the first durable act binds that declaration; and how later artifacts resolve the exact context without copying it everywhere. A later seal can document an earlier observation honestly, but cannot retroactively supply missing authority.

### G3 — Source/copy coverage is measurable, and wrapper Role Locks can constrain the fallback

To answer this research's exact deployment question, inspected `.tfw/adapters/manifest.yaml` solely as a tooling copy map, not as runtime activation/coordination authority. No Coordinator profiles were loaded. Confirmed its mapping by SHA-256 equality of actual source/target bytes for all ten command names: `plan`, `research`, `handoff`, `review`, `docs`, `knowledge`, `release`, `update`, `config`, `init`.

| Source/target family | Observed result | Consequence for a later exact file map |
|---|---|---|
| Canonical workflow → `.claude/commands/tfw-{command}.md` | All ten present and byte-identical | Every changed canonical workflow requires its present Claude command copy to be synchronized. |
| `.tfw/adapters/codex/skills/tfw-{command}/SKILL.md` → `.agents/skills/tfw-{command}/SKILL.md` | All ten present and byte-identical | Wrapper changes require paired source/installed edits; canonical changes alone do not require byte changes in a forwarding wrapper. |
| Canonical workflow → `.cursor/commands/tfw-{command}.md` | All ten targets absent in this checkout | No installed Cursor files to edit here; its selected installation elsewhere still copies the revised canonical workflow. Absence does not prove Cursor behavior. |
| Antigravity manifest command mapping | Reuses Codex skill source and the same `.agents/skills/` targets | No duplicate local command family is needed merely because two adapters name it. |

Read representative `.tfw/adapters/codex/skills/tfw-config/SKILL.md`: it forwards to canonical Config but independently limits writes to config/registered values/adapters and forbids task artifacts. A dedicated receipt proposal must check all affected wrapper permissions instead of asserting that canonical inheritance automatically suffices. That exact minimum is Extract work, not an already selected addition.

### G4 — A supported entitlement check is known; this surface cannot establish the Linux account's current bill

The [official billing instructions](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform), inspected 2026-09-28, identify current ChatGPT Billing settings, role-dependent workspace billing, and separate API billing. The [official authentication documentation](https://learn.chatgpt.com/docs/auth), inspected for this iteration's Briefing, identifies active account/workspace inspection and describes CLI login status as an authentication-method check. These are distinct checks.

The current task runs on the Windows host. Available Codex account usage tools describe the account on this task's host, not the named remote Linux account. Browser control is local; native computer APIs are disabled. The allowed SSH route from RES 1 can observe selected Linux facts, but cached auth claims do not provide a supported current billing/contract surface. No supported remote billing surface has been identified in the exposed tools. This branch is therefore **UNAVAILABLE under current access**, not “no subscription exists.” No billing request failed against the Linux account because none was made; no hidden endpoint, raw app state, login refresh or second user's credentials were used.

Carry forward the earlier non-secret observation only at its original epoch: own cached token claims named `pro`. That is not a current paid entitlement, multi-user permission, purchased seat count or economic saving. A public organizational offer likewise proves neither this project's purchased arrangement nor matching capabilities/costs. The [Terms of Use](https://openai.com/policies/terms-of-use/) and [Services Agreement](https://openai.com/policies/services-agreement/), inspected in RES 1, keep the shared-individual-login route contradicted and distinct End User accounts relevant to the organizational candidate. This stage makes no new legal or price claim and selects no fallback.

**Required later evidence, without requesting it now:** actual applicable product/workspace and subscription or contract, distinct-user allowance/seats, permitted access route, relevant workload/capability limits, and comparable cost inputs. An authorized current surface or accountable non-secret contract evidence must supply them. Additional parsing of the same cached metadata would not close this gap.

### G5 — Trial proof must separate trace, access, identity and economics

RES 1 already supplies version-matched XRDP/session and OS-permission observations. No host command or live trial was run in this stage. Separate OS sessions establish neither two actual humans nor current plan permission; same UID/worktree separation establishes no filesystem boundary. A provenance declaration establishes attribution at its stated assurance, not authentication or authorization. A successful product trial does not establish cost savings.

The exact-carrier inventory adds a requirement for the later trial design: include a material context change or continuation with no lifecycle transition, and reconstruct it from the two projects' actual result sources. A global registry is not yet shown necessary: direct local source references remain a candidate, while cross-project access must be tested separately under the authorized security model. Device `unknown` must remain a valid explicit result, not be replaced by hostname/session metadata. Administrative capability observed in RES 1 prevents claiming protection against host administrators from ordinary home-directory permissions.

## Deep-mode record

| Pass | Observe / orient | Decision / action | Hypothesis and counter-evidence |
|---|---|---|---|
| 1 | Read all ten Full contracts and first/result carrier forms against RES-1 reuse direction | Expand the coverage matrix to taskless maintenance and pre-task setup; keep all carrier alternatives open | H2: event/final-artifact-only coverage fails on Config, Docs batch, Review Map and context-changing continuation. Checked workflow permission and actual form/schema separately. |
| 2 | Inspect actual copy pairs and the Config wrapper; compare supported auth versus Billing documentation and exposed host-specific tools | Require a source/copy/permission map at Extract; terminate current-entitlement investigation at bounded unavailable | H1: cached Pro/catalogue does not establish current permitted arrangement. Independent account/billing guidance contradicts treating auth status as billing proof. H3: no new need for a global registry demonstrated, and no live isolation proof claimed. |

**Metacognitive check:** new information is the exact taskless/pre-task gap, first-stage timing gap, wrapper Role Lock dependency and measured copy topology. Reopening SSH/token inspection would only repeat earlier evidence. The next stage can now compare a truthful existing-carrier design with a narrow fallback, including its real file and runtime-artifact cost.

**Resource boundary:** exceeded the soft fifteen-project-file limit for the explicitly approved all-role/copy audit: ten canonical workflows, selected conventions, output-template headers/ranges, copy manifest and representative wrapper; byte checks covered the twenty present command copies and ten absent Cursor targets. Each group answers coverage, lawful writer, reference timing or deployment; no unrelated task/history or profile library was loaded. Incorrect guessed knowledge-record/journal paths returned missing; corrected to enumerated `knowledge/record.md` and `journal/event.md` before relying on contents. One brace-expanded PowerShell path query failed and was replaced by explicit paths. No missing read was treated as evidence of absent functionality.

## Checkpoint

| Found | Remaining |
|---|---|
| All ten Full routes and taskless/pre-task counterexamples inventoried | Exact minimum owning contract, file/template/copy list and subtraction cost |
| Existing producer/authority semantics and reference/schema limits identified | Select and challenge a fallback without inventing task state or permission |
| Actual installed command parity measured | Inspect only candidate-affected wrapper lines at Extract |
| Supported current billing route distinguished from cached login metadata | Actual entitlement/contract/economic inputs remain unavailable |
| Trace/access/person/economic proof separated | Concrete later two-person/two-project trial sequence and independent oracles |

**Sufficiency:**
- [x] External source used: official Billing, cross-checked with previously inspected official authentication guidance.
- [x] Briefing Gather gap closed to decision-ready evidence or an explicit unavailable boundary.
- [x] Independent dimensions and at least three alternatives each identified; none selected.
- [x] Two research decisions and H1/H2 tests completed; no implementation, account/host mutation or owner question.

**Knowledge handover:** producer/recipient and epochs above; selected P0–P7 authority unchanged from Briefing. Material findings are G1–G4 and trial implications G5; current entitlement, actual people/access trial and final design selection remain open. No new human Fact Candidate arose from Coordinator stage gates. Continue with Extract only after this stage's acceptance; do not turn these research alternatives into approved architecture or expanded writes.

Stage complete: YES
Gate: WAIT — submit exact durable Gather path/SHA to the same Coordinator; recommend Extract.
