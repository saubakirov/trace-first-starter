# Instruction Disposition Ledger — FRATS Phase B

> **Baseline**: `1a9209530d7a939db1270e2f91dcef40a9f449e6`
> **Candidate**: `fd0655ce17f2c650d238622c1d6a57ec5dd9a204`
> **Selector**: the approved 47 VALUE paths; one row per path, including zero-diff paths

## Closed findings

Each detected duplicate, contradiction, stale instruction or readerless bound appears once here.

| ID | Kind | Baseline finding | Normative owner / actual reader | Disposition and reason |
|---|---|---|---|---|
| F1 | contradiction | `REVIEW` was called a formal Coordinator report while Role Lock assigns the verdict to an independent Reviewer. | `.tfw/conventions.md` / Review, Plan and Handoff | **repair** — define REVIEW as the independent Reviewer's report. |
| F2 | stale reference | Glossary “Deferral confession” pointed to nonexistent HL Contract rule 22. | `.tfw/glossary.md` / all roles resolving the term | **repair** — point to the Review Purpose Check/independent judgment that owns the rule. |
| F3 | stale description | Config workflow described `project_config.yaml` as an execution engine. | `.tfw/workflows/config.md` / Coordinator at config activation | **repair** — identify it as declarative project configuration and add the actual activation checkpoint. |
| F4 | duplicate routing prose | Full activation/spine rules were repeated in role workflows even though root delivery is already active. | `.tfw/conventions.md` → `Workflow activation and routing` / all workflows | **consolidate** — one canonical shared section; ordinary role workflows retain compact role-local validation, while Update/Init load it conditionally at adapter repair. |
| F5 | duplicate knowledge-return prose | Multiple workflows repeated the entire knowledge handover contract. | `.tfw/conventions.md` → `Knowledge handover` / returning workflow at its handover checkpoint | **consolidate** — shared authority plus compact local required fields and route. |
| F6 | duplicate template prose | Six artifact templates repeated a long material-handover explanation. | `.tfw/conventions.md` → `Knowledge handover` / artifact producer | **consolidate** — templates retain the mandatory handover heading and concise field obligation. |
| F7 | incomplete filename last mile | Plan/Handoff/Review and templates used globs or generic “choose topology” language instead of emitting the single legal filename. | `.tfw/conventions.md` → `Artifact file naming` / Plan, Handoff, Review | **repair** — producers now emit exact master/single/phase/revision/append paths. |
| F8 | ambiguous RES precedent | Top-level `RES__*` history could be mistaken for current iteration issuance. | naming convention / Research and Plan | **repair** — current research output is only `research/iterN/RES.md`; historical root forms remain readable, never issuance precedent. |
| F9 | overbroad readerless bound | “All artifact filenames” appeared to govern fixed-name stage files as if they used primary root grammar. | naming convention / all artifact producers | **repair** — scope the grammar to primary root artifacts and name fixed stage paths separately. |
| F10 | generated-copy duplication | Twenty Claude/Antigravity files necessarily duplicate canonical workflows, but no independent authority or editing right exists. | ten canonical workflows / provider command entries | **preserve as generated delivery** — exact byte parity is the reason; same-phase regeneration prevents drift. |
| F11 | readerless measurement candidate | Restoring the deleted large audit or adding a permanent successor would create maintained code without a production reader. | task evidence / Reviewer only | **remove from product scope** — keep immutable, reproducible evidence; add no runtime/test. |

No other stale wording, competing current filename grammar, copy drift or undispositioned search result
was found in the 47-path selector. Zero-diff paths are explicit preserves, not omissions.

## Path-level source → reader → delivery ledger

| # | VALUE path | Normative owner | Actual reader / delivery | Disposition | Reason / finding |
|---:|---|---|---|---|---|
| 1 | `.tfw/conventions.md` | shared methodology canon | all workflows by named range | consolidate/repair | Own F1, F4–F9 once; add exact activation/routing and filename rules. |
| 2 | `.tfw/glossary.md` | terminology canon | all roles | repair | Close F2 without duplicating the Review rule. |
| 3 | `.tfw/README.md` | methodology overview | people and selective workflow reads | preserve, zero-diff | Current North Star/NS rules remain correct; no local duplicate needs removal. |
| 4 | `.tfw/templates/HL.md` | HL form | Plan | consolidate | Keep required handover fields; point to shared F6 owner. |
| 5 | `.tfw/templates/TS.md` | TS form | Plan, Handoff, Review | repair | Emit current filename contract and preserve required accounting form. |
| 6 | `.tfw/templates/RES.md` | RES form | Research | consolidate/repair | Current fixed iteration path; concise F6 handover. |
| 7 | `.tfw/templates/ONB.md` | ONB form | Handoff | consolidate/repair | Current filename and concise F6 handover. |
| 8 | `.tfw/templates/RF.md` | RF form | Handoff, Review | consolidate/repair | Current filename/append behavior and concise F6 handover. |
| 9 | `.tfw/templates/REVIEW.md` | REVIEW form | Review, Plan/Handoff on return | consolidate/repair | Current filename/revision behavior and concise F6 handover. |
| 10 | `.tfw/templates/evidence/EV.md` | evidence form | Handoff, Review | repair | Current evidence filename and append behavior. |
| 11 | `.tfw/workflows/plan.md` | Coordinator algorithm | Coordinator; copied to Claude/Antigravity | consolidate/repair | Compact F4/F5 reads; emit master/single/phase/revision names for F7. |
| 12 | `.tfw/workflows/research/base.md` | Researcher algorithm | Researcher; copied to Claude/Antigravity | consolidate/repair | Remove redundant F5 prose; issue only `research/iterN/RES.md` for F8. |
| 13 | `.tfw/workflows/handoff.md` | Executor algorithm | Executor; copied to Claude/Antigravity | consolidate/repair | Compact F4/F5; exact ONB/EV/RF paths for F7. |
| 14 | `.tfw/workflows/review.md` | Reviewer algorithm | independent Reviewer; copied to Claude/Antigravity | consolidate/repair | Compact F4/F5; exact REVIEW paths/revisions and F1 authority. |
| 15 | `.tfw/workflows/docs.md` | Docs Coordinator algorithm | Coordinator; copied to Claude/Antigravity | consolidate | Replace repeated F5 block with shared heading + local return fields. |
| 16 | `.tfw/workflows/knowledge.md` | Knowledge Coordinator algorithm | Coordinator; copied to Claude/Antigravity | consolidate | Replace repeated F5 block; keep qualification/record actions local. |
| 17 | `.tfw/workflows/release.md` | Release Coordinator algorithm | Coordinator; copied to Claude/Antigravity | consolidate | Task-local state first when task-bound; compact F4/F5 without weakening release gate. |
| 18 | `.tfw/workflows/update.md` | Update Coordinator algorithm | Coordinator; copied to Claude/Antigravity | consolidate/repair | Task-local first; conditional canonical F4 read only at adapter synchronization. |
| 19 | `.tfw/workflows/config.md` | Config Coordinator algorithm | Coordinator; copied to Claude/Antigravity | repair | Close F3 and add explicit activation checkpoint. |
| 20 | `.tfw/workflows/init.md` | Init Coordinator algorithm | Coordinator; copied to Claude/Antigravity | consolidate | Conditional canonical F4 read at adapter installation/repair; preserve discovery behavior. |
| 21 | `.tfw/adapters/codex/AGENTS.md.template` | Codex persistent-entry template | installer → managed `AGENTS.md` block | preserve, zero-diff | Local bootstrap is already minimal and required for recovery; not F4 core duplication. |
| 22 | `AGENTS.md` | project root plus managed Codex block | Codex root context | preserve, zero-diff | Foreign project content and active root dispatch remain unchanged. |
| 23 | `.tfw/adapters/claude-code/CLAUDE.md.template` | Claude persistent-entry template | installer → managed `CLAUDE.md` block | preserve, zero-diff | Provider-local bootstrap/recovery remains necessary. |
| 24 | `CLAUDE.md` | project root plus managed Claude block | Claude root context | preserve, zero-diff | Managed block already equals source; foreign content preserved. |
| 25 | `.tfw/adapters/antigravity/tfw-rules.md.template` | Antigravity persistent entry | installer → `.agents/rules/tfw.md` | preserve, zero-diff | Local rule is the native entry carrier, not an independent authority. |
| 26 | `.agents/rules/tfw.md` | generated Antigravity persistent target | Antigravity | preserve, zero-diff | Exact source copy; local recovery value justifies repetition. |
| 27 | `.tfw/adapters/cursor/tfw.mdc.template` | Cursor persistent-entry source | future Cursor installer/target | preserve, zero-diff | Source expresses the same entry semantics; no installed target is claimed. |
| 28 | `.claude/commands/tfw-plan.md` | generated from Plan | Claude `/tfw-plan` entry | mirror | F10; exact canonical blob. |
| 29 | `.agents/workflows/tfw-plan.md` | generated from Plan | Antigravity `/tfw-plan` entry | mirror | F10; exact canonical blob. |
| 30 | `.claude/commands/tfw-research.md` | generated from Research | Claude `/tfw-research` entry | mirror | F10; exact canonical blob. |
| 31 | `.agents/workflows/tfw-research.md` | generated from Research | Antigravity `/tfw-research` entry | mirror | F10; exact canonical blob. |
| 32 | `.claude/commands/tfw-handoff.md` | generated from Handoff | Claude `/tfw-handoff` entry | mirror | F10; exact canonical blob. |
| 33 | `.agents/workflows/tfw-handoff.md` | generated from Handoff | Antigravity `/tfw-handoff` entry | mirror | F10; exact canonical blob. |
| 34 | `.claude/commands/tfw-review.md` | generated from Review | Claude `/tfw-review` entry | mirror | F10; exact canonical blob. |
| 35 | `.agents/workflows/tfw-review.md` | generated from Review | Antigravity `/tfw-review` entry | mirror | F10; exact canonical blob. |
| 36 | `.claude/commands/tfw-docs.md` | generated from Docs | Claude `/tfw-docs` entry | mirror | F10; exact canonical blob. |
| 37 | `.agents/workflows/tfw-docs.md` | generated from Docs | Antigravity `/tfw-docs` entry | mirror | F10; exact canonical blob. |
| 38 | `.claude/commands/tfw-knowledge.md` | generated from Knowledge | Claude `/tfw-knowledge` entry | mirror | F10; exact canonical blob. |
| 39 | `.agents/workflows/tfw-knowledge.md` | generated from Knowledge | Antigravity `/tfw-knowledge` entry | mirror | F10; exact canonical blob. |
| 40 | `.claude/commands/tfw-release.md` | generated from Release | Claude `/tfw-release` entry | mirror | F10; exact canonical blob. |
| 41 | `.agents/workflows/tfw-release.md` | generated from Release | Antigravity `/tfw-release` entry | mirror | F10; exact canonical blob. |
| 42 | `.claude/commands/tfw-update.md` | generated from Update | Claude `/tfw-update` entry | mirror | F10; exact canonical blob. |
| 43 | `.agents/workflows/tfw-update.md` | generated from Update | Antigravity `/tfw-update` entry | mirror | F10; exact canonical blob. |
| 44 | `.claude/commands/tfw-config.md` | generated from Config | Claude `/tfw-config` entry | mirror | F10; exact canonical blob. |
| 45 | `.agents/workflows/tfw-config.md` | generated from Config | Antigravity `/tfw-config` entry | mirror | F10; exact canonical blob. |
| 46 | `.claude/commands/tfw-init.md` | generated from Init | Claude `/tfw-init` entry | mirror | F10; exact canonical blob. |
| 47 | `.agents/workflows/tfw-init.md` | generated from Init | Antigravity `/tfw-init` entry | mirror | F10; exact canonical blob. |

## Positive and compatibility filename fixtures

`phase_slug` is derived from the authoritative phase-status title: Unicode NFKC normalization,
case-folding, each non-alphanumeric run replaced by `_`, then trimming leading/trailing `_`.

| Case | New issuance / behavior | Result |
|---|---|---|
| Master HL | `HL-TFW_20260920-223357_FRATS.md` | unique current form |
| Single-phase TS | `TS__TFW_20260920-223357_FRATS.md` | unique current form |
| Phase TS | `TS__phase-b__corpus_consistency_compression_and_receiver_proof.md` | unique current form |
| Phase EV | `evidence/EV__phase-b__corpus_consistency_compression_and_receiver_proof.md` | unique current form |
| TS revision 2 | `TS__phase-b__corpus_consistency_compression_and_receiver_proof__rev2.md` | new sibling |
| RF later round | `RF__phase-b__corpus_consistency_compression_and_receiver_proof.md` | append to same unsuffixed file |
| Research result | `research/iterN/RES.md` | fixed current path |
| Historical `TS-*`, root `RES__*`, other legacy variants | resolve when explicitly referenced | readable, never new issuance precedent |

Plan, Handoff, Review and all relevant templates now agree on these fixtures. Historical files were
not renamed or normalized.

## Return Round 1 — closed workflow-bound contradictions

Independent REVIEW found four additional active contradictions. These rows extend the F1–F11 census
and supersede the generic path-level dispositions for rows 11, 13, 14 and 18 where more specific.

| ID | Path / baseline finding | Normative owner / readers | Disposition | Candidate result and reason |
|---|---|---|---|---|
| F12 | `.tfw/workflows/plan.md`: 1,433 words exceeded the active ≤1,200 Design Rule | Plan workflow / Coordinator plus Claude and Antigravity projections | **consolidate** | 923 words; retain state routing, activation/authority, knowledge/research gates, exact HL/TS issuance, amendment/REVISE exceptions and Coordinator return. Exact copies regenerated. |
| F13 | `.tfw/workflows/handoff.md`: 2,101 words exceeded the bound | Handoff workflow / Executor plus two projections | **consolidate** | 937 words; retain rung-specific recovery, ONB gate, VALUE/Candidate accounting, evidence/RF, exact state transitions and hard stop. Exact copies regenerated. |
| F14 | `.tfw/workflows/review.md`: 2,136 words exceeded the bound | Review workflow / independent Reviewer plus two projections | **consolidate** | 998 words; retain independent staged verification, immutable accounting, Purpose Check, citation bar, findings/rungs, verdict/KNW and bounded follow-up. `Step 2: Verify` anchor remains valid. Exact copies regenerated. |
| F15 | `.tfw/workflows/update.md`: 2,630 words exceeded the bound | Update workflow / Coordinator plus two projections | **consolidate** | 988 words; retain immutable pin, migration/preservation groups, config/adapter gates, receipt/re-entry/cleanup and safety exceptions. Exact copies regenerated. |

All ten canonical workflows are now ≤1,200 `\S+` words. Each subtraction retains the six-edge
carriers listed in `six-edge-replay.md`; the Candidate replay and material-negative mutations resolve
in `rung1-semantic-replay.txt`. No exception to the Design Rule was invented.

## Return Round 2/3 — owner text, vocabulary, provider entry and transcript isolation

Revision 2 supersedes only the earlier ≤1,200 completion bound with the owner-approved ≤1,400
ceiling and adds exact AC-10–AC-12 semantics. REVIEW §10 then admits one prospective necessary
constituent without changing the selector, denominator, TS, role, route or lifecycle.

| ID | Path / detected finding | Normative owner / readers | Disposition | Final Candidate result and reason |
|---|---|---|---|---|
| F16 | `.tfw/workflows/plan.md`: prior compression reduced the Coordinator to routing mechanics and omitted an executable coordination-selection act. | Plan / Coordinator plus Claude and Antigravity projections | **repair under AC-10** | Install the exact Strategic Architect mindset and nine planning steps, add the `Coordination` read, normalize the state-table route and retain the existing post-approval dispatch paragraph under gate answer `6a43c85d…`. Plan is 1,370 words and both projections are exact. |
| F17 | Active workflow prose collided among Phase, Step, Stage and Gate; the old 1,200 ceiling rejected required meaning. | Glossary and Design Rules / all ten workflows and active references | **repair under AC-11** | Install the exact four-term glossary and ≤1,400 rule, normalize only ordered-action headings and affected anchors/registry entries, preserve true phases/cognitive stages/Config modes, and repair the active Purpose Check anchor. All workflows are ≤1,400 and 84/84 checked relative links resolve. |
| F18 | Provider entry surfaces did not force Plan Step 5's four-capability disclosure and could imply orchestration borrowed from another surface or receipt. | Adapter templates / installed Codex, Claude and Antigravity entry targets; future Cursor target | **repair under AC-12** | All seven source/target paths disclose `provision · addressed send · wait/readback · title/readback` as `native`, `owner-assisted` or `unavailable`, bind claims to exposed mechanisms and preserve managed/full-copy parity. |
| F19 | Vertical gates-only traffic and durable returns left passive observation unnamed, permitting another role's transcript/session/tool output to become hidden coordination state. | `.tfw/conventions.md` `Coordination` / every role; provider mappings / active entry surfaces | **repair under REVIEW §10** | Add the exact canonical transcript-isolation rule once. Codex permits only cursor-based bounded `wait_threads`, never `read_thread`/`includeOutputs` monitoring; Claude, Antigravity and Cursor forbid opening/resuming another role session. All allow wait/status, one addressed request and named artifacts/commits after durable return. |

The final Candidate is `93186cea9ac8209cade30a49e76f3b8a32ae6227`. F16–F19 close every
newly ruled finding without a new workflow, command, artifact, mode, registry, permanent test or
local-only authority. `.tfw/README.md` remains the selector's sole zero-diff path; all other approved
VALUE members are cumulative Phase B changes.
