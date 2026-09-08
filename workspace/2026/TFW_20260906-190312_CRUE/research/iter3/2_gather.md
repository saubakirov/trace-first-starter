# Gather — CRUE Iteration 3: What do we not know?
> **Mindset:** Explorer under Deep mode. Widen the configuration space, but do not spend a third loop when the source, dimensions, hypothesis tests, and counterevidence are already sufficient for Extract.
> **Test:** Can I name every decision dimension, its alternatives, the current 3.0.0 fact, and what evidence would distinguish the alternatives?
> **Parent:** [HL — TFW_20260906-190312_CRUE](../../HL-TFW_20260906-190312_CRUE.md)
> **Goal:** TFW releases and updates should give receiving owners a coherent, safe, understandable improvement and a truthful continuation without requiring them to learn framework internals.
> **Mode:** Pipeline · Deep
> **Operational source:** `8fd8e40b734e9c439bb84721ef8bee441b9fcdd7`; no publication or upstream-availability claim

## Dimensions

No alternative below is selected at Gather. Extract must assemble complete configurations and Challenge must try to falsify them.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1 · Generic/project release boundary | Generic workflow owns fixed TFW/Git/SemVer mechanics; project file supplies details | Generic workflow owns domain-neutral gates; optional project `RELEASE.md` owns concrete mechanics | Project `RELEASE.md` owns the whole route with no common release workflow | A new universal release manifest/engine owns both policy and mechanics |
| D2 · Durable update continuity | Re-observe only; no new durable attempt record | One immutable attempt receipt plus referenced preservation evidence | Reuse a task-local status/journal or other existing trace | Add a mutable installation/update state registry |
| D3 · Legacy `.tfw/README.md` transition | Keep legacy bytes at the live path and withhold the new methodology | Preserve exact bytes in a content-addressed project-owned attachment, then install the framework document | Merge legacy project text into the new framework document in place | Relocate project purpose to an existing project-owned document and record a reference |
| D4 · Incidental concurrent traces | Separate producer-attributed trace landing commits | Deliberately co-commit inspected stable TRACE paths with an authorized commit | Ignore every path classified TRACE | Block whenever any foreign task path or commit is present |
| D5 · Agent rule/read placement | Workflow-local just-in-time rules with named shared headings | Shared canonical rule plus thin pointers from affected workflows | Duplicate complete local rules in every consumer | Generate and consume a separate rule graph/registry |
| D6 · Update decision unit | File/copy action | Semantic effect | Connected effect group | Whole update attempt |
| D7 · Final owner account | Changelog-derived capability/change categories only | Actual outcome plus applicable benefit, limitation/preservation, and next action from observed evidence | Full technical checklist | Free-form summary without a fixed evidence relation |
| D8 · Adapter-root transition | Keep singular tracked installation and change the manifest | Move the framework-owned installation to declared plural roots | Support old/new/both roots indefinitely | Add a new provider command mode while moving roots |
| D9 · Evidence strength | Source consistency only | Source plus synthetic receiver scenarios | Native agent trajectory plus end state | Native evidence plus bounded owner-comprehension observation |

## Findings

### G1 — Epoch and source admission separate product fact from planning history

The current Researcher branch contains the accepted CRUE traces, but its operational surface is byte-equivalent to `8fd8e40b734e9c439bb84721ef8bee441b9fcdd7`. That commit is a completed local 3.0.0 source supplied by the Coordinator; neither a tag nor publication is inferred. Iterations 1–2 remain evidence about released 2.2.0 at `8e68ab37d300122ff110500ad58f354f76b6210f`. The [revision-2 TS](../../TS-TFW_20260906-190312_CRUE.md) is a proposal to compare, not evidence that its files or behavior exist.

A 15-file release/update census found that only eight selected files changed from 2.2.0 to 3.0.0: `.tfw/README.md`, `conventions.md`, `glossary.md`, `migrations/2.0.0.md`, `quickstart.md`, `templates/HL.md`, `workflows/init.md`, and `workflows/update.md`. The generic release workflow, root and template `RELEASE.md`, briefing template, adapter manifest, and Antigravity adapter README did not change in that selected set. Therefore old findings cannot be copied wholesale, but the unchanged release/briefing/adapter contradictions remain live candidates until disproved.

The 3.0.0 source removed the ordinary Full runtime/index dependency from init/update and corrected the obsolete writer instruction in live instructions. A targeted search found the retired sentence only as quoted history in `.tfw/CHANGELOG.md` and `.tfw/migrations/3.0.0.md`, not as a live rule. D82/no-runtime and the writer repair are baseline facts to preserve, not CRUE work to recreate.

### G2 — Preliminary source-delta map: done, partial, unmet, and TS-only

| Responsibility | 3.0.0 observation | Relation to earlier RES | Revision-2 TS proposal | Gather status |
|---|---|---|---|---|
| No shipped runtime/index for ordinary Full | Init/update perform semantic checks without `.tfw/scripts/`; quickstart routes directly to task traces | Supersedes old helper/test paths under D82 | Preserve this boundary in AC-1/AC-7 | **Done in source; regression constraint only** |
| Retired writer wording | No live-instruction hit; only changelog/migration quotation | Discharges one reproduced 2.2.0 defect | Do not duplicate CRATM repair | **Done in source; regression constraint only** |
| Routine update questions/approval | [Update](../../../../../.tfw/workflows/update.md) still requires exactly three questions and one checkbox per file, then exact checklist approval | Iter1/iter2 concern still applies | Replace with consequence/authority-based decisions | **Unmet** |
| Repeat/interruption recovery | Update stops immediately when installed and target versions match; provenance/version are written before final checks, message, and cleanup; no current attempt carrier exists | Iter1 D4–D6 and iter2 D7 remain applicable as design evidence | New receipt template, re-observation, state-specific recovery | **Unmet; proposed carrier unproved** |
| Framework methodology versus legacy purpose | Update/init preserve existing `.tfw/README.md` byte-for-byte, so an existing receiver does not receive the new framework-owned methodology | Earlier research left the transition mechanism open | Content-addressed `legacy-readme/<sha256>/README.md` attachment plus evidence-bound purpose reads | **Required outcome unmet; mechanism TS-only** |
| Owner-facing completion account | [Briefing](../../../../../.tfw/templates/briefing.md) permits only four changelog-derived blocks and forbids outcome/verification/open information | Iter1 D9 and iter2 D3 remain applicable | Outcome/benefit/limitation/next-action projection from actual evidence | **Unmet** |
| A3 worktree/exact-path/TRACE boundary | Conventions already isolate worktree indexes, preserve unrelated dirt, require exact paths, keep producer-attributed landing history, classify by purpose not location, and prevent excluded-only writes from moving Candidate | New current-source fact beyond both 2.2.0 RES outputs | Explicit deliberate TRACE co-commit and aligned handoff/update/review/release readers | **Substantially present; co-commit/provenance edge unresolved** |
| A4 optional/project-defined release | D10 makes `tfw-release` canonical and `RELEASE.md` project context; D12 makes the file optional; the template permits project-specific release forms and even no version scheme | Not tested against current 3.0.0 by earlier RES | Domain-neutral common workflow/template plus concrete root `RELEASE.md` and thin routers | **Principle exists; current workflow contradicts it** |
| Generic release execution | [Release workflow](../../../../../.tfw/workflows/release.md) unconditionally reads `.tfw/VERSION`, `tfw.version`, `.tfw/CHANGELOG.md`, Git tags/DONE tasks, chooses SemVer, and writes TFW version/changelog | Unchanged in selected 2.2.0→3.0.0 census | Remove project-specific assumptions from the generic route | **Unmet** |
| Self-hosting concrete release policy | Root [RELEASE.md](../../../../../RELEASE.md) already owns TFW payload, SemVer, migrations, checks, commit/tag/push order | Existing D10 project-context carrier | Revise for complete isolated composition and A3 semantics | **Carrier exists; adequacy unresolved** |
| Antigravity declared versus tracked roots | Manifest and adapter README declare plural `.agents/rules` and `.agents/workflows`; the exact TFW rule and 11 workflow files are still tracked under singular `.agent`, while `.agents` contains Codex skills | One reproduced 2.2.0 mismatch remains | Twelve singular→plural logical renames, five with content changes | **Unmet source parity** |
| New durable/update release artifacts | No `update_receipt` vocabulary, `.tfw/templates/update_receipt.md`, `.tfw/migrations/update-experience.md`, `.tfw/update_receipts/`, or CRUE deliverable release note exists in 3.0.0 | Earlier RES proposed a receipt but did not implement it | Three new tracked VALUE files plus future project-owned receipt/attachment instances | **TS-only entities** |

The TS VALUE table contains 38 logical rows against 3.0.0: 23 existing non-rename files proposed for modification, three absent files proposed for creation, and 12 singular Antigravity sources proposed for rename to absent plural destinations. This is a measured inventory of the proposal, not evidence that all 38 are necessary or that a smaller count would behave better.

### G3 — A3 is not a blank-slate mechanism

Current [conventions](../../../../../.tfw/conventions.md) already provide four distinct jobs:

1. Worktrees isolate working files and indexes but are explicitly not locks or merge policy.
2. Exact-path staging preserves unrelated dirt and stops on inseparable foreign hunks.
3. Cross-session landing gives a deliverable its own commit whose subject recovers the producer; an exact Candidate remains reachable.
4. Semantic value classification says location/name never decide, TRACE does not spend the delivery budget, exclusions waive no gate, and excluded-only writes do not move Candidate.

Current handoff and review workflows consume these rules, and current update Step 0 already says dirty unrelated task files do not matter. Root `RELEASE.md` requires all **in-scope** tasks to be DONE or excluded, not every repository task. These facts support the first half of H5: most of the harmless-trace/worktree boundary can be restored or clarified in existing carriers rather than introduced as a new subsystem.

Counterevidence prevents a premature H5 verdict. A3's proposed permission to co-commit a sibling trace can conflict with the existing rule that a cross-session deliverable gets its own producer-attributed commit. One commit subject names one task/scope/role; a mixed-producer commit can make path history less recoverable even if every path was inspected. Extract must compare separate landing, same-producer co-commit, and true incidental co-commit rather than treating all TRACE paths as equivalent.

External Git documentation independently bounds the worktree claim: linked worktrees have separate `HEAD` and index but share the repository, refs, and by default repository configuration. Worktrees reduce index/working-tree contention; they do not prove release composition, serialize writers, or make shared refs/private configuration harmless. This supports the current D77 wording and counters any design that treats a release worktree as end-to-end isolation.

### G4 — A4 exposes restoration work, not evidence for a new release engine

The current generic release route and its project template disagree at the authority boundary:

- [`.tfw/templates/RELEASE.md`](../../../../../.tfw/templates/RELEASE.md) is explicitly optional, accepts applications, documents, pipelines, and `None` as a version approach, and delegates project-specific actions to the project.
- The canonical [release workflow](../../../../../.tfw/workflows/release.md) nevertheless requires the template, `.tfw/VERSION`, `tfw.version`, `.tfw/CHANGELOG.md`, Git tags, task DONE state, and SemVer, then updates the installed TFW version/config as though every project release were a framework release.
- Root [RELEASE.md](../../../../../RELEASE.md) already contains this repository's concrete TFW payload, SemVer, migration, tests, commit, tag, and push mechanics.

This directly tests H5. D10/D12 already supply the architectural terms “canonical generic workflow”, “project context”, and “optional”. A smaller complete candidate might restore that separation in existing carriers rather than add a universal release mechanism. Counterevidence is that a common route must still define permission, readiness, truthful completion, and a bounded missing-contract response; removing all common release guidance would merely hide those jobs in every project file.

The two Codex release skill changes and installed copy in the TS are thin-router/copy consequences, not independent release authorities. They may still be necessary synchronization constituents if the canonical entry contract changes, but they cannot justify the design by file count.

### G5 — H6 has a real continuity/purpose problem, but RFC 9110 does not select the carrier

Current update sequencing admits ambiguous interruption states:

- equality of installed/target version exits before current verification;
- version/provenance are written before postconditions, configured builds, owner message, and cleanup;
- the final message is not evidence that it was received or understood;
- no durable attempt record or legacy-preservation carrier exists.

The TS's immutable receipt addresses historical evidence and continuation, while content-addressed README bytes address exact preservation. These are two jobs even if they share a project-owned namespace: an attempt record explains an observed run; a preservation attachment retains bytes and an evidence reference. Combining them into one mutable “current install state” would contradict iter1/iter2 and D82.

[RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) supplies a bounded analogy: automatic retry is safe when intended effects are idempotent or the client can detect whether the original operation was applied; a version-control client can inspect target revisions after partial failure. It also supplies counterevidence to receipt-only recovery: logs may differ even for an idempotent intended effect, and a non-idempotent operation should not be retried merely because a prior record exists. TFW therefore still needs current receiver observation and effect-specific recovery conditions. The RFC does not require a Markdown receipt, choose its directory, or prove agent compliance.

The current Project North Star contract allows designated sections in one or more READMEs and falls back to the master HL when absent. That makes a preserved legacy document a possible citation locus, but it does not decide where its bytes live, who may relocate an existing designation, or how a later reader resolves historical links. Extract must keep “byte preservation”, “current purpose authority”, and “attempt history” as separate comparison dimensions before deciding whether two files/directories are one entity or an overloaded one.

### G6 — Minimum read path is about accessible authority, not raw compression

The current update happy path already uses progressive disclosure: installed config/version/README → immutable source pin → target update workflow → intervening changelog/migration → manifest only at adapter sync → briefing only at final rendering. D73–D75 make those workflow-owned selective reads a current architectural constraint. The TS proposes adding a receipt template, a prospective update-experience migration/guide, and several purpose/release readers. Those additions may make missing authority explicit or may scatter the same decision across more locations; source census alone cannot decide.

The [OpenAI Model Spec](https://model-spec.openai.com/2025-02-12.html) supports explicit authority levels, concrete defaults, and visible bounds when goals conflict. It simultaneously says the public specification is intended behavior and production models did not yet fully reflect it. That is direct counterevidence to treating a well-structured Markdown contract as behavioral proof.

[Liu et al., “Lost in the Middle”](https://aclanthology.org/2024.tacl-1.9/) found that relevant-information position can materially affect long-context retrieval, with performance often worse when needed information is in the middle. The study supports measuring authority accessibility and reader hops, not assuming a long context is used uniformly. Its tasks and evaluated model generations are not TFW update executions; it does not prove that fewer files, fewer words, or placing everything in one file improves this workflow.

Together with NS2.2, F40, F43, and F45, the comparison unit should be one responsibility with a named authority and counterexample. A paragraph replaced by a precise existing term may disappear; a necessary recovery or preservation job cannot be deleted merely to improve a count.

### G7 — Owner communication needs consequence and recovery, but comprehension remains unmeasured

[Amershi et al., “Guidelines for Human-AI Interaction”](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/) validated 18 design guidelines through multiple evaluation rounds, including 49 design practitioners assessing 20 AI-infused products. Relevant guidelines support efficient correction, scope service when goals are uncertain, make behavior explainable, update cautiously, convey consequences, and notify users about changes. This supports a short state-specific owner account and recovery path rather than a technical checklist.

The same source limits the inference: it is a guideline-validation study across AI products, not an observation that a TFW owner understood `outcome / benefit / limitation / next action`. A correct information contract, message emission, and actual comprehension remain different evidence layers. H7 can be tested architecturally here; behavioral and comprehension claims remain for the bounded later evidence already named by the HL/TS.

### G8 — External evidence map and transfer limits

| Primary source | What it supports | Counterevidence / transfer limit |
|---|---|---|
| [OpenAI Model Spec, 2025-02-12](https://model-spec.openai.com/2025-02-12.html) | Explicit instruction authority, concrete defaults, bounds, uncertainty | Intended behavior is not deterministic compliance; the source itself says deployed models did not yet fully reflect the spec |
| [RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) | Idempotent-or-detectable retry and post-failure re-observation | HTTP semantics neither select a TFW receipt nor make project writes transactional |
| [Git `worktree` documentation](https://git-scm.com/docs/git-worktree) | Per-worktree `HEAD`/index and multiple working trees | Repository refs and default config remain shared; a worktree is not a lock, merge policy, or publication proof |
| [Liu et al., TACL 2024](https://aclanthology.org/2024.tacl-1.9/) | Relevant-information placement can impair long-context use | Different tasks/models; does not prove “shorter = better” or a TFW behavior change |
| [Amershi et al., CHI 2019](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/) | Correction, scoped uncertainty, explanation, cautious change, consequences, notification | Guideline validation is not owner-comprehension evidence for this design |

The stage used five web queries, the configured soft maximum, and no external source is treated as TFW implementation authority. It inspected the planned 15-file operational census plus targeted `handoff.md` and `review.md` reads needed to test A3: 17 operational files, two above the soft file limit, with the reason recorded here and no broader architecture scan.

## Comparison Measures for Extract

| Measure | What to record | Why it is not enough alone |
|---|---|---|
| M1 · Required-case completeness | First unmet condition across ordinary/repeat/interrupted update, legacy purpose, harmless/operational trace, no-release, application, non-Git, and self-hosting cases | A paper-complete scenario table does not prove agent behavior |
| M2 · New authoritative entities | Count and name only new sources of current authority; distinguish immutable evidence and deliverables | Fewer files can hide duplicated or overloaded authority |
| M3 · Mandatory agent read hops | Documents/unique heading ranges required on happy, decision, and recovery paths | Hop count ignores salience, length, and model behavior |
| M4 · Authority ambiguity | Places where two carriers can answer the same decision differently or no carrier answers | Zero detected conflicts can reflect an incomplete census |
| M5 · Persistent artifacts per attempt | Required new record/attachment instances and their lifecycle/retention | Artifact count does not price the consequence of missing history |
| M6 · Permission/write surface | Which effects are authorized, separately gated, diagnostic, or forbidden | A smaller write set may withhold required values or evidence |
| M7 · Failure observability and continuation | Whether interruption/refusal/source/receiver/message states have a truthful first unmet condition and next action | Clear prose does not prove correct observation |
| M8 · Evidence level | Declared/source-consistent/synthetic/native/owner-observed | Higher evidence in one layer cannot substitute for another |
| M9 · Change surface | Existing modified paths, new paths, renames, and later measured LOC | Descriptive cost only; not a quality target or behavioral result |

## Gather Decisions

| # | Decision for the next stage | Basis |
|---|---|---|
| GD1 | Treat 3.0.0 source fact, still-applicable 2.2.0 evidence, and revision-2 proposal as three separate columns in every configuration. | Prevents old defects, current fixes, and proposed mechanisms from being silently merged into one baseline. |
| GD2 | Compare one responsibility/authority/counterexample at a time, then assemble complete configurations; do not use a file or line as the semantic unit. | NS2.2, F40/F43/F45, current value classification, and semantic-effect findings all reject mechanical counting. |
| GD3 | Keep A3 as a partial-restoration question and A4 as a demonstrated generic/project contradiction; neither is presumed to require a new subsystem. | Current D77/exact-path/Candidate rules already discharge much of A3, while generic release visibly contradicts D10/D12 and its own template. |
| GD4 | Keep receipt history, legacy-byte preservation, and current purpose authority analytically separate even when an alternative colocates them. | They answer different questions and fail under different counterexamples. |
| GD5 | Use external sources only for bounded mechanism/measurement claims; no source here proves TFW agent reliability, owner comprehension, or the superiority of a shorter prompt. | Every external source supplies an explicit transfer limit or counterexample. |

## Hypothesis Tests at Gather

| Hypothesis | Gather result | Evidence and remaining falsifier |
|---|---|---|
| H5 | **Mixed, advanced to Extract.** Existing optional/project-context terms and current trace/worktree/effect rules discharge substantial A3/A4 structure; the generic release workflow still violates the boundary, and co-commit provenance is unresolved. | G3–G4. A complete restored configuration must survive all release and trace cases without hidden duplication. |
| H6 | **Need established; carrier not selected.** Current source has interruption ambiguity, no receipt, and no migration from legacy README purpose. Re-observation is mandatory; a receipt may help continuity but cannot become current state. | G2/G5 and RFC counterevidence. Extract must test whether one namespace/two record forms is minimal or overloaded and whether an existing carrier can satisfy the same jobs. |
| H7 | **Risk and measures established; benefit unproved.** Current selective reads are valuable, while TS additions can either clarify or scatter authority. | G6–G7. Extract must map exact read hops; Challenge must test missing/hidden decisions. No behavior or comprehension result exists. |

## OODA Record

| Loop | Observe | Orient | Decide | Act |
|---|---|---|---|---|
| 1 | Inspected the pinned 3.0.0 update/release/README/purpose/trace/adapter readers, 2.2.0→3.0.0 selected diff, proposed-carrier absence, TS inventory presence, and singular/plural tree. | Several earlier findings remain, but no-runtime and writer repair are already done; A3 is partly existing architecture; A4 is a live internal contradiction. | Separate epochs and define responsibility/authority/counterexample dimensions before alternatives. | Wrote G1–G5, the preliminary source-delta map, dimensions, and comparison measures. |
| 2 | Checked primary OpenAI, RFC, Git, TACL, and CHI sources for authority, retry, worktree isolation, long-context use, recovery, and consequence communication. | Each mechanism transfers only with a stated limit; none proves prompt compliance or user understanding. | The stage has external evidence, active counterevidence, three hypotheses tested, and a closed Briefing gap. A third loop would add breadth without a named unresolved Gather criterion. | Bounded every external claim, completed decisions/hypothesis statuses, and prepared the Extract questions. |

## Checkpoint

| Found | Remaining |
|---|---|
| Exact current/source/proposal separation and measured 38-row presence census | Assemble and compare complete configurations, not isolated deltas |
| Nine independent decision dimensions with alternatives | Resolve consistency/incompatibility among alternative combinations |
| A3 is partly current D77/exact-path/Candidate behavior; A4 is a demonstrated generic/project release contradiction | Test separate landing versus bounded co-commit and minimal common-release obligations |
| Recovery/purpose jobs are real; proposed receipt/attachment carrier is not yet justified as minimal | Compare no-new-carrier, one-namespace/two-form, existing-trace reuse, and registry alternatives |
| External primary mechanisms plus explicit counterevidence/transfer limits | Challenge surviving configurations against the full counterexample set |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] At least one HL §10 hypothesis tested? H5, H6, and H7 received bounded Gather results.
- [x] Counterevidence sought? Each local/external mechanism carries a failure boundary; both overbuilding and under-specification were tested.
- [x] Deep exit criteria met? Five Gather decisions, all three hypotheses tested, and metacognitive check completed.

**Metacognitive check:** New findings were produced, not only confirmations: 3.0.0 already discharges the runtime/writer defects; A3 overlaps substantially with current rules and creates a specific co-commit/provenance tension; A4 is a direct contradiction between an optional/project-specific template and a TFW-specific generic workflow; the TS introduces exactly three absent tracked entities and 12 root moves rather than a wholly new system. No actual agent reliability, comprehension, or maintenance reduction was observed.

**Recommendation:** Close Gather and proceed to Extract after the direct parent accepts this checkpoint. More Gather is not recommended without a specific missing dimension or source fact.

Stage complete: YES
→ User decision: pending — direct parent Robert, unit `01a0766c-8096-7a83-af60-f70c248290bc`
