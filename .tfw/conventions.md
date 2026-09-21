# TFW Conventions

## 1) Purpose

TFW turns work (analytics, documents, code, research) into a reproducible process:
- context is captured,
- decisions are traced,
- results are repeatable,
- any agent can continue the project in a new session.

## 2) Required Artifacts (project root)

- `README.md` — human explanation: why/what/how, with direct routes to the method, verified knowledge, releases, and selected traces. It carries no live task table and is not edited by a lifecycle transition.
- `AGENTS.md` — AI agent behavior rules for the project.
- `KNOWLEDGE.md` _(optional)_ — project knowledge index: architecture, decisions, legacy. Template: `.tfw/templates/KNOWLEDGE.md`.
- `RELEASE.md` _(optional)_ — project release strategy and context. Template: `.tfw/templates/RELEASE.md`.
- `.tfw/README.md` — TFW philosophy, lifecycle, values.
- `.tfw/conventions.md` — project conventions (this file).
- `.tfw/glossary.md` — project glossary.
- `.tfw/templates/HL.md` — canonical HL template.
- `.tfw/templates/TS.md` — canonical TS template.
- `.tfw/templates/RF.md` — canonical RF template.
- `.tfw/templates/ONB.md` — canonical Onboarding Report template.
- `.tfw/templates/RES.md` — canonical Research Report template.
- `.tfw/templates/status.md` — canonical task state carrier.
- `.tfw/templates/journal/event.md` — canonical journal event.
- `.tfw/templates/team/profile.md` — canonical participant profile.
- `.tfw/templates/REVIEW.md` — canonical Review template.
- `.tfw/workflows/init.md` — canonical initialization workflow.
- `.tfw/workflows/plan.md` — canonical planning workflow.
- `.tfw/workflows/research/base.md` — canonical research workflow (entry point).
- `.tfw/workflows/handoff.md` — canonical execution workflow.
- `.tfw/workflows/review.md` — canonical review workflow.
- `.tfw/workflows/docs.md` — canonical knowledge update workflow.
- `.tfw/workflows/release.md` — canonical release workflow.
- `.tfw/workflows/update.md` — canonical upstream update workflow.
- `.tfw/workflows/config.md` — interactive config change workflow.
- `.tfw/templates/update_receipt.md` — immutable record for one update attempt.
- `.tfw/VERSION` — current framework version (semver, single line).
- `.tfw/CHANGELOG.md` — version history (Keep a Changelog format).
- `.tfw/project_config.yaml` — project configuration (stack, checks, task containers, scope, research, review, and content settings).
- `.tfw/compilable_contract.md` — build-time compilation specification (Source Manifest, Reference Format, Output Structure).
- `.tfw/migrations/{major}.md` — migration guide per major version. A major release without one is incomplete.

## 3) Artifact Types (canonical)

> See also: [glossary.md](glossary.md) for terminology, [README.md](README.md) for philosophy.

### HL (High Level)
Context/frame. Not a task — a "map of meaning".
Format: strictly follows `.tfw/templates/HL.md`.

#### HL Contract

An approved HL is a contract, not a draft. Approval is the moment it freezes.

| HL section | State after owner approval |
|------------|---------------------------|
| §1 Vision · §3 Target State (incl. §3.1, §3.2) · §4 Phases · §5 DoD · §6 DoF · §7 Principles (incl. §7.1) | 🔒 FROZEN |
| §2 Current State · §7.2 Knowledge Citations · §8 Dependencies · §9 Risks · §10 RESEARCH Case · §11 Strategic Insights | 🟢 FREE |
| §12 Amendment Log | 🟢 APPEND-ONLY |

1. **The contract state is artifact state.** The HL header carries a `Contract` field with two values: `📝 DRAFT — not yet approved` and `🔒 FROZEN — approved by {owner} YYYY-MM-DD`. Task status tracks the pipeline; the `Contract` field tracks the artifact. They are not interchangeable.
2. **Free sections stay free.** Research and the coordinator update §2, §7.2, §8, §9, §10 and §11 directly, with no proposal and no verdict. Risk registers, hypothesis statuses and dependency statuses are required to move.
3. **A frozen section may not be edited.** The only channel is §12 Amendment Log: propose, resolve and record the rule-8 verdict, then apply. This includes the coordinator that authored the HL.
4. **§12 is append-only.** Rows are never deleted, rewritten or renumbered. A refused proposal stays visible as an attempt — that visibility is the point.
5. **The frozen unit is the declarative claim, not the section text.** Frozen at claim level: the phase set and each phase's declared outcome, §3's to-be claims, each §5 and §6 item, each §7 principle, and §1. Rewording a claim without changing it is not an amendment; changing what it commits to is.

For Coordination Selection, an immutable delegation mandate is the frozen claim. `EXTEND` widens
its scope, role coverage, reach or amendment authority; `SUPERSEDE` replaces its holder. A profile,
binding, title or shared principal supplies attribution only and never supplies a mandate or
amendment authority. Owner-direct activation needs no invented agent principal or delegation.

6. **Deliverable lists inside an already-approved phase are free** — specifying *how* a phase meets its declared outcome is refinement. **Tripwire:** if the change cannot be accepted under §5 and §6 *as they stand at the moment of classification*, it is an amendment. Two tables decide it; no judgement call is required.
7. **Non-substantive edits are not amendments** — typos, broken links, formatting, renumbering of free-section rows.
8. **A verdict is a distinct, resolved act.** Chat/workflow input is evidence, never a verdict. The
governing task/phase `status.md.owner` must be a declared human and is the root/fallback ruler. An
owner-approved committed HL may give one directly addressable Coordinator unit an immutable,
bounded delegation mandate and amendment grant. A principal is optional stable attribution; it
grants nothing. Several units may share one principal, but that never merges nodes or lets a child
consume another unit's grant. Amendment authority exists only in the exact immutable mandate cited
by the task routing spine.

For claimed delegation, each task/phase-local `dispatch` body and refs preserve actual source,
destination and parent units, governing role/scope/channel, and the originating proposer as
`{principal, unit}` or explicit `none`; `writer` is attribution, not an edge. Only a Coordinator unit
on one unambiguous human-rooted path may create a child. Before work refuse an Executor source,
unknown/repeated/competing node or parent, ancestor/task-Coordinator target, cycle, foreign scope,
missing address, missing root authorization, or non-human/unresolved termination. Forwarding,
transcription, restart, continuation, or a new writer never changes proposal origin.

For ordinary `EXTEND`/`SUPERSEDE`, a root Coordinator may rule only a genuinely subordinate-origin,
non-reserved proposal inside its exact immutable amendment grant and mandate. A child never inherits
that grant. A root-unit-origin, owner-reserved, missing/ambiguous-origin, out-of-grant or
out-of-mandate proposal routes to the human owner and remains `PROPOSED` until ruled. Before signing,
validate unit chain, origin, grant, mandate, reservation and signer. Profile role, `accountable_to`,
binding, title, provider, `writer`, or `on_behalf_of` supplies none of them. Owner-direct work without
a valid delegated claim routes to the owner.
9. **An owner-initiated frozen change is an amendment too** — one §12 row records the owner as `Proposer` and their real explicit decision. An agent's `on_behalf_of`, human binding or `accountable_to` cannot create this direct-human exception. The log's value is the record, not the gate.
10. **A restrictive change applies on filing.** Narrowing — adding a DoF item, tightening scope, dropping a deliverable — is logged with `Type` = `RESTRICT` and verdict `✅ APPLIED — no owner verdict required`. Restrictive-free is prohibited: the classifier benefits from the label, so the log costs nothing and removes the incentive.
11. **`Type` states relation to the baseline, never disposition.** `EXTEND` adds and the original stays in force; `SUPERSEDE` replaces; `RESTRICT` narrows. Disposition belongs in `Verdict`.
12. **A proposal without evidence, cost and a considered alternative is not a proposal.** The burden sits on the proposer, which is what keeps declining cheap.

**Contract Baseline** — a frozen contract that cannot be diffed is not frozen.

13. **The approved HL is committed before the first research iteration.** An uncommitted baseline makes "frozen" permanently unverifiable.
14. **The baseline reference is a reserved `freeze` scope word** in the commit subject, per the `[agent/task/scope/role]` grammar in §4: `[claude-code/PROJ-7/freeze/coordinator] freeze approved hl`. It applies to the **first** freeze and to every re-freeze after an approved amendment.
15. **Recovery form:** `git log --format="%h %s"`, filtered on `^\S+ \[[^]]*/{TASK-ID}/freeze/`. Filter the subject, never the message; do not start the pattern with `/` because some shells rewrite it as a path.
16. **No header field can name its own commit** — a commit's SHA cannot appear in its own content. The baseline lives in the commit subject, not in the file, and needs no separate registry.

**Delegated authority**

17. **A delegated mandate is a ceiling, never a source of new permission.** It bounds what an agent may do; it does not create what an agent may do.
18. **No agent may widen its own grant.** Authority that can justify its own extension is not authority, it is a loop.
19. **Delegation is never valid authority to accept a scope or budget overrun.** "I was delegated this decision" does not convert an overrun into a compliant result.

**Phase HL**

20. **A Phase HL is derivation-only.** It may restate master content and add execution context — files, sequencing, phase-local risks.
21. **A Phase HL may not carry its own §1, §5, §6 or §7.** Vision, acceptance criteria, failure conditions and principles exist once, in the master HL. A Phase HL that authors them is a second, unapproved contract.

History: D63 and TFW-53.

### Project North Star

The layer above every task HL: what the product is for, and what it must never become. Together with the
contract baseline it is the reference set of the Purpose Check (`templates/review/judge.md` row 2a),
and it is PV priority 0 (`glossary.md`).

1. **Locus: designated section(s) of a README.** More than one location is permitted — a project whose
   product is its own method may designate sections of both its root README and its philosophy paper.
2. **A task HL may never be nominated.** Nominating one promotes a task contract to project authority with
   no gate at the promotion point, and imports contract drift one level up. Supporting that locus properly
   would need a project-level freeze mechanism, which TFW does not define.
3. **Payload: purpose, principles and non-goals.** Non-goals are not optional. The failure mode this layer
   exists to catch is *excess*, not opposition, and a purpose statement alone cannot detect excess.
4. **Admission criteria.** A clause belongs here if it states what the product *is for* or *must never
   become*. If a single task's implementation choice could satisfy or violate it, it is a principle
   (HL §7), not a north-star clause. This is a criterion, not a size cap — a list carrying implementation
   detail satisfies a citation requirement forever while blocking nothing.
5. **Optional, with a declared fallback:** project north star → master HL §1 at the contract baseline. A
   review is never blocked on a missing north star.
6. **PV priority 0 and priority 1 may name the same file.** They are distinguished by what the section says
   — *what we are building* versus *how we build* — never by which file holds it. Where the product is the
   methodology, one file legitimately carries both.
7. **Citation namespace:** `NS{n}` for north-star clauses; HL §7 keeps `P{n}`; a project principle registry
   uses `PP{n}` (see `compilable_contract.md` §2).

### RES (Research Report)
Structured investigation artifact. Produced via Briefing → Gather → Extract → Challenge stages in `research/` subfolder.
RES file = synthesis (Decisions, Hypotheses, HL Recommendations, Conclusion). Stage files = raw investigation.
Created between HL and TS (pipeline) or standalone for any research.
Format: strictly follows `.tfw/templates/RES.md`.

### TS (Task Spec)
Task definition. Always self-contained: inputs/outputs/constraints/DoD.
Format: strictly follows `.tfw/templates/TS.md`.

### RF (Result File)
Results/facts/data/final text. RF has priority as source of truth.
Contains mandatory Observations table (structured, typed).
Format: strictly follows `.tfw/templates/RF.md`.

### ONB (Onboarding Report)
Structured executor report before starting: understanding, questions, risks, inconsistencies.
The Executor owns the question, blocking reason and operational effect in the ONB. The authority
answers by appending a task-local `gate_answer` event; the ONB cites that event and is not edited by
another role.
Format: strictly follows `.tfw/templates/ONB.md`.

### REVIEW (Review Report)
Formal independent Reviewer report after reviewing RF: checklist, verdict, and a disposition on every debt item it captured.
Format: strictly follows `.tfw/templates/REVIEW.md`.

### Fact Candidates (section in RF, REVIEW, RES)
Raw observations about the project recorded during work. Cognitive mode: pure reporting — record factual without interpretation. NOT verified facts — they become facts after `/tfw-knowledge` consolidation. Each artifact has a Fact Candidates section with a structured table (Category, Candidate, Source, Confidence). Quality filter: "Would the next agent decide differently knowing this?"

### Visual Sections (per-template)

> **Decision criterion:** "Does the cognitive mode CHANGE between templates?" If yes → per-template naming. If no → unified.
> Visual sections trigger different cognitive modes per template context (empirically validated: RES3 D22, RES4 Exp1+Exp2).

| Template | Section | Cognitive Mode | What it produces |
|----------|---------|---------------|-----------------|
| HL | §3.1 Result Visualization | Narrative / Outcome | Outcome preview — Working Backwards style ("imagine it's done") |
| HL | §3.2 Value Flow | Strategic / Value-oriented | Value streams, INPUT→PROCESSING→OUTCOME, transformation tables |
| RF | §9 Diagrams | Technical / Engineering | Architecture, ERD, sequence diagrams, component diagrams |
| RES | Findings Map | Analytical / Research | Root cause analysis, hypothesis trees, priority matrices |
| REVIEW | — | — | No visual section (checklist artifact, not result) |

### Knowledge Capture Sections (unified naming)

| Section | Name | Templates | Cognitive Mode |
|---------|------|-----------|---------------|
| §7 | Fact Candidates | RF, RES, REVIEW | Pure reporting: record without interpretation |
| §8/§11 | Strategic Insights + qualifier | HL (Planning), RF (Execution), RES (Research) | Deep analytical synthesis: capture + add implications |

### Knowledge Input Sections (unified naming)

| Section | Name | Templates | Cognitive Mode |
|---------|------|-----------|----------------|
| §7.2 | Knowledge Citations | HL | Input tracing: cite the exact PV clause/item read, link it, and state its concrete application |
| §7 | Knowledge Citations | ONB | Input tracing: confirm the exact HL §7.2 items read and how each applies; add new relevant items |
| _(section)_ | Knowledge Citations Verified | review/verify.md | Verification: check link resolution, item existence, semantic match, and relevance to the asserted application |

> **Unified naming rationale (D43/D28/D39):** cognitive mode is the same across all three — "report what you read and how it applies." Same mode = same name. Scan scope differs by role: Coordinator + Reviewer do full PV scan, Executor references coordinator's citations. See glossary.md → Project Values (PV).
>
> **Semantic integrity:** a citation that resolves to a real file or anchor but names an absent, irrelevant,
> or semantically different item is a discrepancy, not a verified citation. Priorities 0 and 1 must be
> recorded and checked as distinct meaning even when one README contains both.

### Evidence Sections (per-template)

> Evidence = real-world verification of completed work in its intended environment.
> Separate from Verification (RF §4 — synthetic tool output: lint, test, build).
> Status vocabulary: VERIFIED / DEFERRED / BLOCKED / N/A.
> Role pipeline: Coordinator designs (TS) → Executor collects (EV file) → Reviewer audits (REVIEW).
>
> **Mandatory folder:** Every task directory MUST contain an `evidence/` subfolder with a structured EV file.
> The EV file captures environment metadata, per-AC verification results, and a verdict summary.
> RF §5 is a pointer to the EV file — not a duplicate of the evidence table.
> Template: `.tfw/templates/evidence/EV.md`.

| Template | Section | Cognitive Mode | What it produces |
|----------|---------|---------------|------------------|
| TS | Evidence field (in §5 AC items) | Prescriptive / Planning | What to verify in real environment, suggested tools |
| EV file | `evidence/EV__{...}.md` | Observational / Verification | Environment header, per-AC evidence table, verdict, attachments |
| RF | §5 Evidence (pointer) | Summary / Reference | One-line pointer to EV file + verdict summary |
| review/verify.md | Evidence Verification | Audit / Trust-but-verify | Artifact existence checks, claim-vs-reality |
| review/judge.md | Check #7 Evidence completeness | Judicial / Completeness | All TS Evidence fields covered in EV file? |

## 4) Task Identity and Location

### Where tasks live

`tfw.task_containers` in `.tfw/project_config.yaml` is the ordered **active** path list.
Create tasks in its first entry; ordinary discovery searches active paths only.
New Full projects use `[workspace]` without a container-choice question. Existing single/custom
choices remain valid, including `[tasks]` and `[tasks, workspace]`.

Existing projects may retain history through optional `tfw.historical_containers`: a list of
repository-relative directory paths, absent for new projects. Exact citations, initialized-project
detection and documentation use the ordered active-plus-historical **reference union**, deduplicating
the same resolved path without rewriting active choices. Invalid historical paths or conflicting
whole identifiers are errors; never choose an ambiguous task by container order.

Historical containers do not participate in creation or ordinary current-work selection.
Opening history is read-only; continuation requires a separate explicit authorized act. A container
disposition never declares a task DONE/REJECTED, creates a status, or rewrites its original evidence.

```
{container}/{YYYY}/{id}__{slug}/
```

The year is the year the task was **created**, and it never changes. A task opened in December
and closed the following March stays in the earlier folder. Recomputing it would move a
directory, and moving a directory breaks every reference into it.

**No lifecycle state is expressed by moving a directory.** Not `TODO`, not `DONE`, not
`REJECTED`. A path is created once and outlives every state the task passes through. Status
lives in the task's own `status.md`; a folder move would ask a sync engine to relocate a
directory other participants may be writing inside, and would invalidate references that
already resolve.

The temporary exact `[workspace, tasks]` arrangement may retire empty or established historical-only
secondary storage through [the 3.3.0 migration](migrations/3.3.0.md). Preserve live/unclear work and
recorded keep-active decisions; list position, age and missing status are not historical disposition.
The guide reconciles affected state before narrowing active config. All three identifier grammars
and original paths remain readable; no task is moved, renamed, copied or relabeled.

### Identifier

```
PREFIX_YYYYMMDD-HHMMSS_ABBR  the whole directory name IS the identifier
```

`PREFIX` is `tfw.task_prefix`; `ABBR` is the **acronym of the approved full title** — the
initials of its significant words, uppercase alphanumeric: *Conflict Resistant Shared Workspace*
→ `CRSW`; *Assisted 1.5 core and synchronization* → `ASSISTED15`, digits being alphanumeric.
Neither field may contain `_`, so the single underscores are unambiguous separators. The timestamp is read from the system clock after the abbreviation is
approved; it is never composed or adjusted. Every reference, commit subject and index row
carries the full identifier.

**No participant reads a project-wide maximum to learn which identifier is free.** There is no
counter, registry or allocation step. Creation performs only one exact-path existence check.

The coordinator proposes the full title and its initials **together, in one exchange**, and
the owner approves both before a directory is created; the HL header carries them side by side
as **Title** and **Abbreviation**. *Never derived silently* means two things: never invented
apart from the title — `UPD` for a task with no title behind it is the anti-pattern, an opaque
code a person cannot read back — and never created without the owner's approval. A title is
what makes the approval a decision rather than a formality.

If the full identifier already exists at creation, creation refuses and asks for a different
owner-approved abbreviation. It never recomputes the timestamp, adds a suffix or silently
retries: any of those would invent a different identifier from the one the exchange approved.
When offline work later exposes two directories that normalize to one identifier, validation
stops and names both paths.

**A bare timestamp is not an identifier.** Two participants can reach the same second, so a bare
`YYYYMMDD-HHMMSS` cannot name exactly one task and no consumer accepts one as if it did.

Two historical grammars remain readable forever and are never renamed or issued again:

- legacy `PREFIX-N`, optionally carried by a directory as `PREFIX-N__slug`, normalizes to
  `PREFIX-N`;
- `2.0.0-dirty` `YYYYMMDD-HHMMSS__slug` keeps its whole directory name as the identifier.

### Task control files

| File | What it is |
|------|------------|
| `{task}/status.md` | **The only authority for that task's live state and routing spine.** Closed key set, complete one-line prose fields, no free-text body. Template: `.tfw/templates/status.md` |
| `{task}/journal/{YYYYMMDD-HHMMSS}__{kind}__{token}.md` | One event, immutable once written. The filename **is** the event identifier — nothing allocates it. Template: `.tfw/templates/journal/event.md` |
| `{task}/{phase}/journal/…` | A phase carries its own journal, exactly as it carries its own `status.md`. Same grammar, same rules |
| `team/{handle}.md` | One participant. Declared attribution, never authentication. Template: `.tfw/templates/team/profile.md` |

Before any state/event write, open its template and validate the complete proposed carrier, not
only the changed field: closed schema, lifecycle/outcome relation, permitted transition pair,
clock/token, declared principal and accountable human, actual authority, and every reference.
Resolve status authority from that status file and event refs from their owning task/phase directory;
enforce the template's containment rules and open the actual targets. For a cited immutable object,
verify the object and the claimed artifact at that epoch. A plausible path or SHA is not evidence.
Refuse a missing, escaping, contradictory or unverifiable reference before writing.

Read the clock and draw the event token. Write status before its actual transition event; validate
both proposed carriers before either write. Events are append-only: a correction cites the erroneous
event and describes the actual act using an existing truthful kind, never a same-state or invented
transition. If no kind fits, do not invent an event; record the explanation in the existing owning
artifact. Compatibility `actor` and erroneous history remain readable, never rewritten. Recover an
interrupted pair through `Closing and record recovery`. History: D68, TFW-54, TFW-60.

### Declared participants and principals

A **principal** is a stable project-local `team/{handle}.md` identity backed by a valid human or
agent profile. Provider, model, executable, process, session, folder, hostname, account identity,
and workflow role never define one. Do not create a profile per run or agent session.

A **working unit** is a directly addressable operational node with its own workflow role, actual
address, parent, bounded scope, direct channel and activation or dispatch trace. It is not a
participant or principal and gets no `team/` profile. Optional shared attribution never collapses
unit parentage, work, authority or proposal origin.

Every profile requires `handle`, `name`, `type`, and `since`; the existing four-key human form stays
valid. Optional `organization_role` and `project_role` accept a non-empty description or exact
`not_applicable` for both profile types. Omitted means unknown or not supplied, not that a role is
absent. These roles are descriptive context only: they never authenticate, grant permission, supply
task scope, or change a workflow Role Lock.

A `type: agent` principal additionally requires `accountable_to`, naming an existing `type: human`
profile. Historical profiles may also carry `may_rule_amendments` as a YAML Boolean; it remains
readable but is never issued and grants nothing. Human profiles do not carry those keys. Optional
agent `mentality` is non-empty descriptive guidance and grants nothing. Current routing and
amendment authority come only from the governing status and cited immutable authority object.

A current event may carry optional `writer`, naming a declared human or valid agent principal. It is
never derived from `via`, an OS/account identity, hostname, model, session, folder, or filename token.
`on_behalf_of` still names the human accountable for the act, `via` is non-empty free-form tool text,
and the opaque filename token supplies uniqueness only. Existing `actor` is historical input:
accept it exactly as already written, but never require it, issue it, validate it under the current
principal rules, remove it, or rewrite it.

### Which handle a machine acts as

Ordinary owner-launched work does not require, infer or invent an agent principal. Resolve a stable
principal only when an immutable delegation mandate or an explicit attribution requirement needs
one. A profile never activates a workflow or supplies authority.

When stable attribution is required, select it from a **binding held on the participant's own
machine**, never in this tree: `~/.tfw/bindings.yaml` on POSIX,
`%LOCALAPPDATA%\tfw\bindings.yaml` on Windows. Template: `.tfw/templates/bindings.yaml`.

```yaml
bindings:
  /abs/path/to/project: principal-handle
```

One project-root mapping may select a declared human or valid agent principal. The file contains
nothing else: no authority, mentality, fallback, default, liveness, device identifier, provider
data, or second key kind. It selects attribution and grants nothing.

If stable attribution is required and the binding is absent, ambiguous or invalid, ask exactly one
short question before the first durable write, once per session. If several humans exist and the
owner-source itself is ambiguous, the same one-question rule selects the human source. Otherwise do
not ask an identity question.

Never infer identity from an OS username, hostname, folder, or account display. The binding selects
which principal the session acts as; it does not prove who is present or what they may do. History:
D68, TFW-54 and TFW-60.

### Workflow activation and routing

A command activates material work only when the request names the exact `/tfw-*` skill, selected
task/phase when task-bound, and owner-direct, delegated, or continuation source. A created or selected
unit, role prompt, briefing, wait result, title, source artifact, trigger, or implicit latest session
does not activate a workflow.

For task-bound work, read its own `status.md` and journal before derived or shared inputs. Validate
the lifecycle/role gate, bounded scope, actual unit/address/parent, and all five routing fields. Total
absence is legacy-readable but cannot activate current work; partial, stale, foreign, unverifiable or
mismatched routing is a pre-work refusal. Owner-direct activation needs no agent principal. Delegated
activation additionally requires the cited immutable mandate and direct Coordinator dispatch; apply
`Which handle a machine acts as` only when stable attribution is explicitly required.

Under `tfw-gates-only`, a role unit sends every material status, question, gate and durable return
only to its own `coordinator_route`; it never sends them to a peer, owner, foreign Coordinator or
GATEWAY. That Coordinator alone uses `owner_gateway`. `iterative` additionally requires its exact
immutable grant and a separately addressable GATEWAY, which performs no workflow role. An authority
answer is valid only as the owning authority's task-local `gate_answer`; no role edits another role's
artifact to answer itself.

Role artifacts preserve the actual producer unit, parent Coordinator, activation/dispatch source,
`coordination_authority`, and originating proposer `{principal, unit}` or explicit `none`. Recheck the
spine on continuation. Provisioning, navigation, attribution and forwarding grant no authority.

### Session identity

Navigation-only; non-authoritative.

```text
SP:=U+0020;DOT:=U+00B7;BASE:=WORK+SP+DOT+SP+TASK[+SP+DOT+SP+PHASE]
GATEWAY_BASE:=GATEWAY+SP+DOT+SP+[HANDLE+SP+DOT+SP]+TASK[+SP+DOT+SP+PHASE]
WORK:=PLAN|RESEARCH|EXEC|REVIEW|RESUME|DOCS|INIT
```

**TASK:** approved root-unique abbreviation;else=full-ID;historical:=full-ID;preserve(`TFW-##`).

**PHASE:** uppercase(sole-governing-`phase-{token}`);else=omit(absent/conflict/ambiguity/iteration).

**GATEWAY:** emit `GATEWAY_BASE` only when `dialogue: iterative` and the current actual unit address
equals the `gateway:{native}` address in `owner_gateway`. The gateway is separate from the root
Coordinator and cannot execute a role workflow. Include `{handle}` only when stable attribution was
explicitly selected. Every role unit emits ordinary `BASE`; historical `LEAD` titles remain readable
but are never issued.

**Handle:** display the selected stable profile handle only. Never use mutable `name`, title,
OS/account/provider, human binding or chat. Navigation grants no identity, authority, mandate,
dispatch edge, role permission or amendment right; a generic bound or attribution is insufficient.

**Collision:** RENDERED:=BASE|GATEWAY_BASE; duplicate(RENDERED)+exposed(stable-key) →
suffix(SP+DOT+SP+`@<shortest-unique-leading-prefix>`); exact-readback-only for either RENDERED.



**Failure:** either RENDERED unavailable/failed/altered-readback/no-key →
report-once(title,reason); continue-unclaimed.

**Forbidden:** guessed-fields/title-pipe/hyphen/emoji/alternate-separator/ordinal.

**Sources:** authoritative-state/lineage; never chat/index/folder/memory.



### Artifact file naming

| Artifact | Format | Example |
|----------|--------|---------|
| Master HL | `HL-{ID}.md` | `HL-TFW_20260829-172110_ABT.md` |
| Phase HL | `HL__phase-{x}__{phase_slug}.md` | `HL__phase-a__data_model.md` |
| Single-phase TS / ONB / RF / REVIEW | `{TYPE}__{ID}.md` | `TS__TFW_20260829-172110_ABT.md` |
| Single-phase EV | `evidence/EV__{ID}.md` | `evidence/EV__TFW_20260829-172110_ABT.md` |
| Phase TS / ONB / RF / REVIEW | `{TYPE}__phase-{x}__{phase_slug}.md` | `TS__phase-a__data_model.md` |
| Phase EV | `evidence/EV__phase-{x}__{phase_slug}.md` | `evidence/EV__phase-a__data_model.md` |
| Research synthesis | `research/iter{N}/RES.md` | `research/iter2/RES.md` |
| Single-phase TS revision | `TS__{ID}__rev{N}.md` | `TS__TFW_20260829-172110_ABT__rev2.md` |
| Single-phase REVIEW revision | `REVIEW__{ID}__rev{N}.md` | `REVIEW__TFW_20260829-172110_ABT__rev2.md` |
| Phase TS revision | `TS__phase-{x}__{phase_slug}__rev{N}.md` | `TS__phase-a__data_model__rev2.md` |
| Phase REVIEW revision | `REVIEW__phase-{x}__{phase_slug}__rev{N}.md` | `REVIEW__phase-a__data_model__rev2.md` |

At a current write gate, first select task topology, then artifact type, then revision behavior. `{ID}`
is the exact task identifier. `{x}` is the selected `phase-{x}` directory token. `{phase_slug}` is
derived once from the selected phase `status.md.title`: remove an exact leading `Phase {X}:`, apply
Unicode NFKC case-folding, replace each non-alphanumeric run with `_`, and trim `_`; an empty result
is invalid. A current producer emits the one matching row and refuses any other new name. Research
stage files use their fixed names inside `research/iter{N}/`; their owning path supplies identity.

**`{ID}` is the task's whole identifier**, and it means the same thing everywhere: in a path,
in a filename, in a reference and in `status.md`. For a current-grammar task that is
`TFW_20260829-172110_ABT` and for a clock task `20260826-143000__query_redesign` — **no title is
appended** to either. The identifier is the whole name; a filename is `HL-{ID}.md` exactly, and
`HL-TFW_20260829-172110_ABT__approved_fixture.md` is a name this contract rejects, just as a
clock task's doubled slug is. The title lives in `status.md` and the HL header, where a person
reads it; the abbreviation inside the identifier is what makes the filename readable without it.

A legacy task keeps `{PREFIX}-{N}`, where the identifier does *not* carry a slug, so its
historical filenames have the form `RES__TFW-60__conflict_resistant_shared_workspace.md`.
Those files are never renamed; the two-part form is history, not a second rule.

Historical clock-task and legacy artifact names remain discoverable exactly as stored. They are
read inputs only: examples, citations, or existing filenames never authorize a new historical-form
artifact. Current issuance always uses the table above.

#### The revision suffix, and what it generates

`__rev{N}` is the only admitted suffix and identifies a repair round ordered after 🔄 REVISE (§5).
The unsuffixed artifact is revision 1 and is never renamed. Revisions are immutable siblings:
each new governing artifact names its predecessor and governing source, and consumers choose the
highest valid lineage. Cumulative records append rather than overwrite.

| Artifact | Form | Why |
|---|---|---|
| **TS** | **sibling** | Exactly one order is in force, and the highest ordinal is it |
| **REVIEW** | **sibling** | Exactly one verdict is live, and the highest ordinal is it |
| **RF** | **appended** — one new numbered subsection per round, in every section the round touches | The result record is cumulative and earlier results remain openable |
| **ONB** | **appended, never a sibling** | Each entry extends the executor's recorded understanding; one ONB file per task |
| **EV** | **appended** — a round's rows beside the earlier round's | Earlier verification remains part of the cumulative evidence |

**A live revision is amended in place and says so in its header; a superseded one is never touched.** The
never-edited rule protects history, not the order currently in force — an order that cannot absorb a
correction is an order nobody can raise a question against.

History: D72 and RDP.

> **Rule:** every current primary artifact at a task/phase root includes the task ID or phase
> identifier. Fixed-name stage artifacts such as `research/iterN/RES.md` and `review/map.md` are
> identified by their owning task/phase path and are not competing primary-artifact grammars.

### Discovery

Task-local carriers are the discovery source. Resolve an exact cited whole identifier through
the reference union; ordinary current-work discovery uses only `tfw.task_containers`. Accept the
current and two historical grammars above. A
workflow acting on a task reads that task's `status.md` directly; a phase reads its own
carrier. Never select by prefix, timestamp fragment, title, or a generated summary.

Enumerating the corpus is optional. When an explicitly requested read-only projection does
so, it must report malformed, duplicate, missing, stateless, and unreadable inputs rather
than infer or drop them. Such output is disposable, non-authoritative, and never a lifecycle
or build gate. A human may approve a rename; readers never normalize one. Generated docs may
create one hidden landing per recognized task solely to keep direct links resolvable, but no
public task catalogue or default current-status page follows from that infrastructure.

Full ships no executable, dependency, collector, portfolio cache, or freshness duty. Rules
required for ordinary lifecycle work are complete in workflows and templates and must remain
usable without Python or PyYAML. The upstream repository may keep optional maintainer tools
outside `.tfw/`; they are not copied by init/update and hold no authority over receiver state.
History: D69, D73, D75, D76, and the applicable migration RF.

### A major release ships a migration guide

Version-addressed guides live at `.tfw/migrations/{version}.md`; `update.md` follows every applicable
guide named by the pinned changelog, including minor/patch and equal-version recovery obligations.
Crossing a major also requires its `{major}.0.0.md` guide. **A major release without one is incomplete.** Prose inside a CHANGELOG that
documents the framework repository's *own* migration is a record, not a procedure: it names
that repository's paths, counts and decisions, and a receiving project cannot follow it.

The guide is written for a project that is not this one, and it states its ordering
constraints where a reader is about to violate them rather than in a summary.

### Commit Attribution

Every AI-authored commit MUST use `[agent/task/scope/role] summary`: set `agent` to the lowercase AI product name from explicit context, `task` to the canonical TFW task ID (`project` only when none exists), `scope` to the established lowercase work-slice slug or a lowercase hyphenated form of its explicit label, and `role` to the lowercase canonical TFW workflow owner from §15/Role Lock; keep `summary` short and imperative, commit locally, and push only after explicit user approval.

Example: `[codex/TFW-50/task/coordinator] define minimal commit attribution`

### Worktrees for concurrent mutation

A delegated run that may mutate the repository uses its own Git worktree; its coordinator creates
the tree before dispatch. A read-only run may share the current checkout because it contends for no
writes and creates no landing obligation.

| Property | Rule |
|---|---|
| Location | Outside the project tree, per machine: `~/.tfw/worktrees/{TASK-ID}__{phase}/` on POSIX; `%LOCALAPPDATA%\tfw\worktrees\{TASK-ID}__{phase}\` on Windows. A provider-created or other foreign worktree stays where it is and is read, never renamed into this layout |
| Name | `{TASK-ID}__{phase}`, extensible to `{TASK-ID}__{phase}__{principal}` once the principal exists. An established name is never changed because existing references must keep resolving |
| Landing | Only after the run's role artifact exists and review has run. This lifecycle point selects no branch, merge, or other transport strategy |
| Removal | The coordinator removes the tree only after landing and verification, including reachability of the exact TS-fixed Candidate when one exists |
| Dead run | Read its tree and land its commits before removal. Session death never authorizes deletion |

A worktree isolates files and the Git index. It is not a lock, does not serialize writers, and does
not define a merge strategy; one mutation owner controls each worktree.

### Exact-path staging

Before every commit, read the complete `git status` and the staged name set with
`git diff --cached --name-only`. Stage only explicit full pathspecs. `git add -A`, `git add .`, and
`git commit -a` are forbidden for shared-tree work; `git commit --only -- <paths>` prevents an
already-staged sibling path from riding along. Preserve unrelated dirty work without normalizing or
repairing it. If a selected path contains an inseparable foreign hunk, STOP and report the overlap.

### Trace boundary and selected siblings

A task-local trace is selected by an exact path and a governing artifact, not by a broad directory
scan. A selected stable uncommitted sibling trace may be used only when the governing TS or RF names its
exact path, the producer task/phase, parent/child relationship, and the semantic effect it supplies.
The receiver records the path and commit or working-tree state in EV/RF; it never treats a sibling's
`DONE` state as a prerequisite. Incidental traces remain append-only evidence and do not become new
VALUE scope, new authority, or a second copy of the result.

### Release and update records

`RELEASE.md` is optional project-owned release context. The release workflow is a router: when the
project has no release contract, it records that no release action is due; it does not invent a
universal versioning or publication policy. An update receipt is an immutable attempt record, not a
state registry. It records the pinned source, authority, semantic decisions, applied/skipped/refused
effects, preservation references, verification, and next action. It never stores credentials or
replaces the receiver's own task state.

### Landing a deliverable across sessions

When one session lands a deliverable produced by another, the deliverable gets its own commit. The
subject names the producer's task and phase; `role` names the acting landing role. TD-178 is the
measured wrong/right case:

```text
wrong  [agent/TFW-58/proposal/coordinator] propose the revise protocol
       └─ also carries TFW-53 phase E board rows
right  [agent/TFW-53/phase-e/coordinator] land the board rows
```

The right form lets `git log -- <changed-path>` recover the producing task. When the producer's TS
fixes a Candidate, that exact commit remains reachable after landing and before worktree removal;
recreating equivalent bytes under only a new SHA is not equivalent evidence.

### Research subfolder

Research artifacts live in a single `research/` container at task root. Each iteration gets its own numbered subfolder:

```
{task}/research/
  iterations.yaml              ← control file
  iter1/
    1_briefing.md              ← numbered stage files
    2_gather.md
    3_extract.md
    4_challenge.md
    RES.md                     ← synthesis co-located with stages
  iter2/
    1_briefing.md
    2_gather.md
    3_extract.md
    4_challenge.md
    RES.md
```

File existence = stage completion. Stage file format: see `.tfw/templates/research/` (`1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md`).

#### Multi-iteration research

When research spans multiple iterations, each iteration gets its own subfolder and RES:

| Iteration | Stage files folder | RES file |
|-----------|-------------------|----------|
| 1 | `research/iter1/` | `research/iter1/RES.md` |
| 2 | `research/iter2/` | `research/iter2/RES.md` |
| N | `research/iterN/` | `research/iterN/RES.md` |

**Trace rule:** Iteration folders accumulate — never delete or overwrite previous iteration's files. Each `research/iterN/` folder is a trace. Deleting them = deleting reasoning.

**Control file:** `research/iterations.yaml` tracks iteration state. Created by coordinator in `plan.md` Step 6 before launching research. Format:

```yaml
task_id: PROJ-N
title: research focus description
min_iterations: 2       # from tfw.research.min_iterations or coordinator override
max_iterations: 5       # soft ceiling
iterations:
  - number: 1
    focus: "initial investigation of H1-H3"
    hypotheses: [H1, H2, H3]
    status: complete     # pending | in_progress | complete
    res_file: research/iter1/RES.md
    # agent: antigravity           # optional — which tool/agent ran this iteration
    # sources: [external, codebase] # optional — what sources were consulted
  - number: 2
    focus: "deepen findings from iter 1, test H4"
    hypotheses: [H4]
    status: pending
    res_file: research/iter2/RES.md
```

The `agent` field records which tool or agent conducted the iteration — for traceability, not dispatch. The `sources` field records what source categories were consulted. Both fields are optional; simple single-agent tasks can omit them.

Coordinator updates `research/iterations.yaml` after each iteration (marks status, adds next iteration if needed). Researcher reads it at start to understand predecessor context and assigned hypotheses.


### Review subfolder

Review stage files (`review/map.md`, `review/verify.md`, `review/judge.md`) — intermediate review traces written during the review process. Created in task phase directory. Parallels research stage files (`research/iterN/1_briefing.md`, etc.). The REVIEW artifact synthesizes these files. Stage file format: see `.tfw/templates/review/` (map.md, verify.md, judge.md).

### Evidence subfolder

Every task directory (or phase directory for multi-phase tasks) MUST contain an `evidence/` subfolder. The subfolder always contains at least one structured EV file (`EV__{ID}.md` or `EV__phase-{x}__{title}.md`). Additional binary artifacts (screenshots, API responses, logs) go into the same `evidence/` folder and are indexed in the EV file's Attachments section. Template: `.tfw/templates/evidence/EV.md`.

### Multi-phase folder structure

For multi-phase tasks, master artifacts (HL, RES) stay at task root. Each phase gets a subfolder:

```
{container}/2026/20260826-143000__query_redesign/
  status.md                           ← Live state — the authority for this task
  journal/                            ← One immutable file per event
    20260826-143000__created__saubakirov.md
    20260901-091500__handoff__saubakirov.md
  HL-20260826-143000__query_redesign.md   ← Master HL
  research/                           ← Master research (if any)
  phase-a/
    HL__phase-a__data_model.md
    TS__phase-a__data_model.md
    ONB__phase-a__data_model.md
    RF__phase-a__data_model.md
    REVIEW__phase-a__data_model.md
    evidence/                         ← Mandatory evidence folder
      EV__phase-a__data_model.md      ← Structured evidence file
  phase-b/
    HL__phase-b__api_layer.md
    ...
```

## 5) Task Statuses

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE
   multi-phase:  ⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🧩 PHASES → 📚 KNW → ✅ DONE   (each phase runs the full flow in its own status.md)
                                                                              │
                                                                    ┌─────────┴─────────┐
                                                                    🔄 REVISE          ❌ REJECT
                                                                (routed by rung)  (user decides)
                    (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)        ↓
                                                           ❌ BLOCKED

  from any status ──→ ❌ REJECTED     terminal · no edge leads out · the trace is kept
```

| Status | Meaning |
|--------|---------|
| ⬜ TODO | Task planned, HL not started |
| 📝 HL_DRAFT | HL being drafted, awaiting review/approval |
| 🔬 RES | Research in progress (optional — user can skip to TS_DRAFT) |
| 🧩 PHASES | The task is multi-phase and its phases are running. **A task-level rollup of phase state is prohibited** — each phase carries its own `status.md`, and a summary would be a second fact that must agree with them |
| 🟡 TS_DRAFT | TS written, awaiting approval for execution |
| 🟠 ONB | Onboarding: executor studying the task |
| 🟢 RF | Execution complete, RF written |
| 🔍 REV | Review: reviewer checking RF |
| 📚 KNW | Coordinator completes applicable capture and final-effect acceptance under Closing and record recovery |
| ✅ DONE | Final accepted effects and complete control records checked; task closed |
| ❌ BLOCKED | Blocked by dependency |
| ❌ REJECTED | Task closed unsuccessfully and permanently. Distinct from ❌ BLOCKED, which is waiting and resumes when the dependency clears. Terminal: no status follows it, and the task folder and its board row are never deleted. This is a task status — not the review verdict ❌ REJECT, and not the HL §12 amendment verdict ❌ REJECTED; neither of those is terminal |

Status lives only in the task's own `status.md`. Its lifecycle is one of the ids above or
`UNDECLARED` carrying the source value verbatim (→ glossary.md).

Current statuses also carry the complete five-field routing spine:

- `coordinator_route`: one quoted, non-empty native address for the unit that receives every
  workflow status change, question, gate and durable return;
- `owner_gateway`: either `owner:{human-handle}` or `gateway:{native-address}`;
- `dialogue`: `tfw-gates-only` or `iterative`;
- `activation`: `owner-only` or `delegated:{immutable-mandate-ref}`;
- `coordination_authority`: one quoted exact local authority reference plus immutable epoch.

All five fields are present or absent together. Total absence is legacy-readable but cannot activate
new work. A partial spine is invalid. Current writers emit and strictly validate all five. An
authorized active task may migrate once without a same-state event because no lifecycle transition
occurred; the authority and exact source are recorded in the new fields.

**`UNDECLARED`: migration never normalizes; an accountable owner may resolve.**

| Act | Permitted |
|---|---|
| A tool rewriting `UNDECLARED` to a declared value | **Never.** It has no basis for the choice, and the rewrite is silent |
| The task's owner setting the correct value and recording a `transition` event with `from: UNDECLARED` | **Yes.** The accountable decision and its trace are explicit |

The same rule governs rejected directory names (→ Discovery): tooling reports; a person may
resolve; the resolution leaves a record.

### A phase carries its own state

A phase owns its `status.md` and `journal/`; create both only with the phase. The task-level
`lifecycle` never summarizes phase state. The task file describes only this arc:

```
TODO → HL_DRAFT → RES → 🧩 PHASES → KNW → DONE
```

While `PHASES` stands, read each phase's state. Every phase consumer reads that local state and
journal before acting. A transition is two ordered acts: write the authoritative task/phase
`status.md`, then append its journal event. History: D68 and TFW-60.

Review verdicts:
- ✅ **APPROVE** — independent verdict → 📚 KNW; return to Coordinator for `Closing and record recovery`
- 🔄 **REVISE** — specific cited issues → the Reviewer proposes and stops; the Coordinator rules
  once, then follows **The 🔄 REVISE route** below. The verdict alone never moves lifecycle
- ❌ **REJECT** → 🛑 User decides: (a) 📝 HL_DRAFT (rework HL), (b) 🔬 RES (new research), (c) 🟡 TS_DRAFT (rewrite TS)

> Branch (a) does not thaw a 🔒 FROZEN HL. It reopens free sections; frozen claims still use
> the §12 amendment channel in §3.

### Closing and record recovery

The existing authorized **Coordinator** owns closing a selected task or phase. Use this contract
directly; Plan's selected-return route exposes it and stops. No new task, bootstrap, phase matrix or phase-choice
question is required for an already selected close. This route grants no missing mandate or scope.
Read that task/phase's state and journal, its governing authority and live REVIEW, then the referenced
RF/evidence and actual capture or landing effects needed for the claim.

**Close after checked final effects.** The independent APPROVE is an input, not a terminal write:

1. Inspect actual contributor/dispatch/return lineage through `Knowledge handover`; read each
   material source and completed disposition. Missing producers, unavailable acceptance-critical
   context and owed publication/resolution keep this selected close nonterminal. An empty file,
   unchecked marker or another producer's return cannot cover a missing contribution. Unrelated
   historical changes and justified non-obligations create no global queue.
   Rule REVIEW §5 dispositions once under existing authority. Complete applicable `/tfw-docs` and
   `/tfw-knowledge` through their existing owners and gates. Both Applied/N/A markers must describe
   actual effects; Deferred and pending dispositions keep the task open.
2. Identify which accepted outputs or claims those effects changed. Reuse evidence only where its
   relevant inputs/output, oracle or authority, and environment assumptions still apply. An enclosing
   SHA, unrelated TODO, or record repair alone invalidates no unaffected claim. A changed dependency
   or insufficient evidence requires the affected check; a file's TRACE/ASSURANCE label proves nothing.
3. The separate Reviewer independently assesses changed final claims and their evidence. The
   Coordinator cannot independently accept its own material output. Record a bounded follow-up in
   existing evidence/REVIEW sections; its recording alone starts no full stage restart, formal
   revision, repeated capture or new knowledge candidate. A real cited defect still follows
   `The 🔄 REVISE route` with the same holders; missing authority or uncertain acceptance stops close.
4. Confirm the required final effects, including actual landing when selected, and validate complete
   status/event carriers through `Task control files`. Only then write DONE with its actual outcome
   and append the real transition. Report reviewed, landed and published distinctly; no external
   effect is authorized by closing.

Record the material grounds once in REVIEW §6: actual capture effects, final accepted output identity,
applicable evidence and independent judgment, dispositions and any remaining effect. N/A needs its
reason. No new closing artifact, registry or mandatory executable is introduced; receiving projects
use their own checks. If a material failure blocks KNW, record that actual BLOCKED dependency and
route the cited condition. After the existing ruler supplies an executable bound, return from BLOCKED
to the rung table's required state; never fabricate a direct KNW-to-ONB edge or an acceptance.

**Repair only the record.** A missing outcome, malformed current carrier or interrupted status/event
pair is administrative only when the accepted result, oracle, authority and relevant dependencies
are reconstructably unchanged. Check the actual outputs, prior acceptance and lineage first. Repair
the current carrier, preserve original event bytes and reference the error in the existing record.
Append only a truthful current act, with the current clock; do not invent the missing past event or
timestamp, repeat a completed transition, or infer execution from an intended state. If status was
written and the event was not, reconstruct what actually occurred before recording the present recovery.

Immediately before a repair, compare the affected current fields with preserved old/intended
values and their actual source/authority. A third value refuses the affected write; preserve it
and unrelated later work, naming the exact conflict and authoritative next action. Never roll back
a whole file/map/tree. A missing past event is not a reason to invent a timestamp or transition.
Validate the repaired carrier and its references, then **stop**. Repair alone creates no product work,
TS revision, Candidate, formal review round, Fact Candidate or knowledge/capture cycle. Unknown or
fabricated SHA/acceptance, changed authority, material output change or uncertain lineage cannot use
this branch. Preserve the honest nonterminal state or report the contradictory terminal carrier and
route the exact gap; never silently normalize it. REJECTED stays terminal and only the accountable
owner may resolve UNDECLARED. A genuine new defect uses its existing authority route, not record repair.

#### The 🔄 REVISE route

A rung belongs to an item; the highest required authority controls a mixed round. The table is the
single routing authority. `live REVIEW` means the existing REVIEW while it remains the current
verdict artifact; recording a Coordinator ruling there is acceptance control, not a new
implementation order.

| Case | Fix boundary | Recipient after Reviewer | Coordinator ruling site | Governing execution artifact | Lifecycle after REVIEW → after Executor acceptance | Exact hard stop |
|---|---|---|---|---|---|---|
| Rung 1 only | inside the approved TS | Coordinator for one ruling act, then the same Executor | ruled bound appended to the live REVIEW; no TS sibling | existing approved TS is the implementation order; ruled live REVIEW bounds the return | `RF → ONB` only when the Executor accepts | Reviewer → Coordinator; Coordinator → `/tfw-handoff`; Executor → `/tfw-review` |
| Any rung 2 | the TS | Coordinator, then the same Executor | one TS revision for the whole round | highest approved TS revision | `TS_DRAFT → ONB` when the Executor accepts | Reviewer → Coordinator; Coordinator → `/tfw-handoff`; Executor → `/tfw-review` |
| Rung 3 | a frozen HL claim | Coordinator, then `HL Contract` rule-8 ruler | HL §12 proposal plus `amendment_escalated` event and resolved ruler's terminal verdict | none until that verdict leaves an executable bound | unchanged; Executor is not dispatchable | Reviewer → Coordinator → resolved ruler; **STOP until terminal verdict** |
| Mixed rung 1 + 2 | approved implementation plus TS change | Coordinator, then the same Executor | one TS revision containing the complete ruled round | highest approved TS revision | `TS_DRAFT → ONB` when the Executor accepts | Reviewer → Coordinator; Coordinator → `/tfw-handoff`; Executor → `/tfw-review` |

A REVISE item names the failed TS acceptance criterion or frozen HL claim, its owner, and an
observable completion condition. The Reviewer proposes and stops. The Coordinator rules every
proposal once: a rung-1-only round is closed in the live REVIEW; any rung-2 item produces one TS
sibling for the whole executable round; rung 3 uses rule 8 and forbids Executor dispatch until its
valid terminal verdict leaves an executable bound. The Executor appends ONB, RF, and EV
round content, and the Reviewer verifies the return. No cited condition means no round: approve
with the remainder disposed, or transition to `BLOCKED` and return to the task owner because no
basis can be stated. An `unassigned` owner is a hard stop. A fresh role holder resolves lineage
from state/artifact references. History: D72 and RDP.

## 6) Scope Budgets (per Phase)

> Configured in `.tfw/project_config.yaml` (`tfw.scope_budgets`).
> Values below are project-owned defaults. `/tfw-config` changes them and their registered inline
> copies together; `/tfw-update` preserves them.

### Semantic value-bearing classification

Budget the accepted **value-bearing surface**; classify paths by purpose:

| Class | Default meaning | Spends the delivery budget? |
|---|---|---:|
| `VALUE` | Accepted output or its necessary constituent | Yes |
| `ASSURANCE` | Ordinary tests/checks/fixtures | No; yes only when assurance is the accepted product |
| `TRACE` | Lifecycle, decision, review, evidence, and log records | Never |
| `DERIVED` | Reproducible output not independently accepted | No; yes when that output is accepted |

| Examples | Class |
|---|---|
| code; shipped prompts; accepted documents; accepted presentations; accepted data; accepted generated final outputs | `VALUE` |
| ordinary tests | `ASSURANCE` |
| conformance-as-product; task-folder deliverables; TFW-looking product sources | `VALUE` |

| Ambiguity rule | Requirement |
|---|---|
| Precedence | Accepted/necessary; whole fixed Baseline→Candidate diff if roles inseparable |
| Narrower selector | Deterministic, replayable, and declared before work |
| Line subtraction | No freehand line subtraction |

Location/name never decide. Phase attribution is separate: shared work uses
distinct immutable phase Candidates, assigns the whole delta to one phase with a dependency, or reports
exact phase enforcement as `INVALID`. Never double count. Exclusion waives no gate and creates no shadow budget.

### Value-bearing accounting contract

Approved TS fixes subject, Baseline, Candidate rule, class/reason selector, measures, plan, triggers,
M1–M6, and rulings. Candidate is the first tested immutable Executor VALUE+ASSURANCE commit before
EV/RF/REVIEW/final transition.
Excluded-only writes do not move it; later VALUE requires replacement and recomputation.

RF binds result/deviations/decision; one EV row reproduces it; REVIEW reruns without supplying authority
or totals. Missing/mutable/mismatched/late is `BLOCKED`; metric-only inapplicability is `N/A`;
`DEFERRED` is not terminal.

The universal measures are exactly these two:

| Measure | Default | Config key | Definition |
|---|---:|---|---|
| Logical touched `VALUE` files | 50 | `decomposition_trigger_files` | Changed selector members; one rename is one |
| Touched text LOC | 5000 | `decomposition_trigger_loc` | Numeric additions + deletions; binary/non-text is per-file `N/A` |

Use immutable SHAs and TS literal VALUE paths:

```powershell
git diff --name-status --find-renames=50% -z <BASELINE_SHA> <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z <BASELINE_SHA> <CANDIDATE_SHA> -- $valuePaths
```

CREATE, MODIFY, DELETE, and rename are actions, not measures.

### Decomposition, constraints, and change authority

| Parameter | Default | Config key | Definition |
|---|---:|---|---|
| Owner escalation multiplier | 2 | `owner_escalation_multiplier` | Delegated boundary against each immutable planned measure |

Triggers are soft prompts, never quality vetoes; record cause, cost, assurance, split, authority, terminal
verdict, and pre-work ref. Compare forecasts/Candidate with the immutable owner plan; no ruling ratchets it.
Owner rules before work at/above multiplier or from planned zero. Below it, Coordinator may add only a
necessary constituent while Goal, Value, outputs, AC, DoF, phase/ownership, architecture/target,
interfaces, data, security, trust, and authority stay fixed. Completed work is only a deviation. Apply
Saint-Exupéry only without damaging purpose, value, correctness, architecture, modularity,
inspectability, or continuation.

A hard constraint is valid only when its approved TS records all M1–M6 facts before work:

| Fact | Required content |
|---|---|
| M1 — consequence | Material harm prevented |
| M2 — protected object/risk | Exact boundary |
| M3 — direct measure + selector | Reproducible check |
| M4 — pre-act enforcement | Check before action |
| M5 — softer control insufficiency | Why disclosure/review cannot prevent harm |
| M6 — change authority | Prospective decision role |

Apply by release/TS approval epoch; never reinterpret history. Migration preserves
`max_files_per_phase`→`decomposition_trigger_files` and `max_loc`→`decomposition_trigger_loc`,
retires the other old keys, and adds multiplier `2`.

## 7) Coordination

Provisioning creates or selects a callable unit. Activation authorizes one exact workflow run.
Continuation resumes the same unit inside the same immutable authority and routing spine. None of
these acts implies another. A profile, binding, title, role prompt, briefing, status token, provider
session, provisioned task or wait result never activates work.

A **TFW gate** is a named workflow checkpoint whose question, status or correction affects whether
the current role may continue. A **durable return** is the role-owned artifact plus task-local status
or event reference that lets its own Coordinator reconstruct the result without transcript or hidden
runtime state. Workflow autonomy is the unit's ability to complete authorized in-scope actions after
valid activation; it is independent of dialogue policy.

Every activation supplies the exact `/tfw-*` skill, task and phase, and one lineage source:

- **owner-direct:** an accountable human starts the role workflow; no agent principal is invented;
- **delegated:** an actual Coordinator dispatch cites the immutable delegation mandate;
- **continuation:** the same unit cites its prior activation and still-current routing spine.

The activation payload contains only those facts and an exact continuation reference when resuming.
Copied solution text, a long briefing, “wait”, or “you are the role” may provide context but never
substitutes for the skill or activation source. Dispatch preserves actual source, destination,
parent, role/scope, native address/channel, governing status/authority and originating proposer.

Before material work the unit reads the governing `status.md`, validates the complete routing spine,
exact lifecycle gate, skill, role, task/phase and lineage, and records producer provenance in its role
artifact. A mismatch, partial or legacy-only status, foreign dispatch, role prompt without activation,
implicit latest-session lookup, relay, hidden helper or ambiguous address is a pre-work refusal.
Apply the session title at the earliest valid state checkpoint, read it back where supported, report
failure once and never treat the title as authority. A GATEWAY may provision or activate a separate
Coordinator only when `activation` cites the exact delegated authority; it never invokes
`/tfw-plan` as its own workflow.

`dialogue: tfw-gates-only` creates only vertical edges: every role unit sends status changes,
questions, gates and durable returns to its own `coordinator_route`; the Coordinator alone uses
`owner_gateway`. Peer-role, role-to-owner and role-to-gateway material communication is prohibited.

**Transcript isolation.** Another active unit's transcript, reasoning, tool output, terminal and
unreturned working tree are not coordination or evidence surfaces. No role reads, tails, resumes,
searches or reconstructs them to monitor progress, validate trust, review work, recover context or
pre-solve that unit's task. Use only addressed TFW status/gate messages, provider status/wait signals
and durable returns. A suspected stall permits one addressed status request; no response or missing
return is reported as unavailable or blocked, never repaired by transcript inspection. After a
durable return, only the named artifacts and commits become inputs at their stated evidence level.

`dialogue: iterative` is valid only when an owner-approved immutable authority names exactly two peer
units, their purpose, boundary, consolidator, durable output and stop condition, and names a separate
directly addressable `GATEWAY` unit. A missing or over-broad grant refuses. The gateway is not the
root Coordinator, cannot execute a role workflow, receives no raw worker traffic, joins no peer
dialogue and cannot rewrite authority. A Reviewer for the result cannot be either peer or consolidator.

An authority answer is an immutable task-local `gate_answer` event. It cites the governing status,
the blocked role artifact and the exact HL or TS authority; its body identifies the answer source,
authority epoch and operational effect. The blocked role never writes its own answer or treats chat,
a title, a profile or hidden state as amendment authority.
An answer that changes scope, acceptance, architecture, authority or an owner reservation is invalid
as `gate_answer` and routes to a TS revision or HL §12. Missing, stale, foreign, unverifiable or
contradictory refs keep the role blocked.

All current role artifacts record: actual producer unit address, parent Coordinator route,
activation or dispatch source, governing authority reference and originating proposer when present.
Shared principal attribution never merges units or changes authority.

A role consumes prior artifacts only at their stated evidence level and does not pre-solve another
Role Lock. Distrust alone creates no repeat-work duty: repetition cites either an explicit independent
workflow check or a concrete contradiction/evidence gap. Record a discrepancy once in the detecting
role's artifact and return it through that unit's own Coordinator without peer debate.

### Provider-native evidence

Coordination capability is admitted per provider and native surface, never by analogy or by combining
partial receipts:

1. **P0 documentation:** identify the native address, send, readback, wait and title mechanisms.
2. **P1 one operation:** demonstrate one bounded addressed operation and exact readback.
3. **P2 readback:** reconstruct source, destination, role, task/phase and immutable authority.
4. **P3 checkpoint series:** demonstrate activation, status/gate return, continuation and terminal
   return without a relay or prohibited edge.
5. **P4 end-to-end trial:** one native TFW trial proves all required edges, isolation, role ownership,
   correction continuity and terminal reconstruction together.

Missing a stage, translated documentation, provider switching, separate demonstrations or a partial
receipt does not admit the provider. Resource limits may bound use but never prove reliability.

Historical `CL`, `AG`, `AT`, `LEAD`, `Autonomous from` and `G1`–`G8` records remain readable at their
original epochs but are not current controls and are never newly issued.

## 8) Workflows

TFW defines the following canonical workflows in `.tfw/workflows/`:

| Workflow | Role | Purpose |
|----------|------|---------|
| [init.md](workflows/init.md) | Coordinator | Discover project → interview → knowledge → setup → verify |
| [plan.md](workflows/plan.md) | Coordinator | Research → HL → RESEARCH gate → scope decision → TS |
| [research/base.md](workflows/research/base.md) | Researcher | Structured investigation → RES artifact (pipeline or standalone) |
| [handoff.md](workflows/handoff.md) | Executor | Context load → ONB → execute → RF |
| [review.md](workflows/review.md) | Reviewer | Read RF → checklist → verdict → debt disposed → traces |
| [docs.md](workflows/docs.md) | Coordinator | Update KNOWLEDGE.md after task completion |
| [knowledge.md](workflows/knowledge.md) | Coordinator | Consolidate fact candidates into verified project knowledge (Orient → Gather → Consolidate → Prune) |
| [release.md](workflows/release.md) | Coordinator | Read RELEASE.md → scope release → version bump → CHANGELOG → tag |
| [update.md](workflows/update.md) | Coordinator | Fetch upstream → compare versions → categorize changes → update checklist → re-sync adapters |
| [config.md](workflows/config.md) | Coordinator | Interactive config change → propagate to all inline values |

## 9) Tool Adapter Pattern

`.tfw/` is the tool-agnostic core — one copy per project. Each development tool reads its own entry point, which references `.tfw/`:

```
CLAUDE.md ──→ "Read .tfw/README.md, follow .tfw/conventions.md"
.cursor/rules ──→ "Read .tfw/README.md, follow .tfw/conventions.md"
.agents/rules/tfw.md ──→ Antigravity persistent project rule
.agents/workflows/tfw-{command}.md ──→ Antigravity `/tfw-*` command routing
AGENTS.md + .agents/skills/tfw-*/SKILL.md ──→ Codex `/tfw-*` command routing
```

Adapters are chosen at project init. See `.tfw/quickstart.md` for setup.

**An adapter installs whole copies or marker-bounded blocks, and nothing of a third kind.** A
whole copy — a command, a workflow, a rule file, a skill — is verified by `cmp` against its
source. Where TFW content is merged into a **project-owned** file — the `TFW:CLAUDE` block in
`CLAUDE.md`, the `TFW:CODEX` block in `AGENTS.md` — the managed text sits between
`<!-- TFW:{NAME}:START -->` and `<!-- TFW:{NAME}:END -->` and is verified on that region alone.
One rule governs every such block, in every adapter:

| The target file… | The sync… |
|---|---|
| carries the markers | replaces the text between them and touches nothing outside |
| does not exist | is created from the template, block included |
| exists **without** markers | is **reported and left untouched** — the operator inserts the block once, and every later sync is mechanical |

Appending a block to a file that already carries an unmarked, hand-written TFW section produces
two sections that disagree; no adapter guesses where the content "probably is". Exactly one
managed block per file. `update.md` Step 4 names which row is a copy and which is a block.

For Codex, `/tfw-*` is the primary human-facing command contract. Root `AGENTS.md`
provides always-on recognition and fallback routing; repository-local skills provide
discoverability and progressive workflow loading. Skills are implementation, not a
separate wrapper users must learn. Adapter source lives in `.tfw/adapters/codex/` and
installed copies live in `.agents/skills/tfw-*/`.

### Command entry and evidence boundary

Every `/tfw-*` entry follows one satisfiable pre-action sequence, regardless of adapter
layout:

1. Discover the command receiver at the adapter's declared route.
2. Reach the command's one canonical workflow; a dispatching receiver reads it completely,
   while a full-copy receiver begins with its byte-identical content.
3. Bind that workflow's declared Role Lock before any task reasoning, question, decision,
   tool call, or durable write.
4. Execute the workflow's Read Contract in its listed order without an adapter-owned preload
   or reordering.
5. Obey the workflow's gates and stops; the receiver supplies no alternative algorithm.
6. At the canonical stop, name the next workflow only by its `/tfw-*` route.

The canonical workflow alone owns task effects, branching, templates, gates, and stops. A
receiver may copy or dispatch it but cannot summarize those decisions into a second
algorithm. The manifest remains tooling-only copy/check metadata and is never runtime role
authority.

Claims about this sequence use six non-substitutable evidence levels:

| Level | Claim proved | Required observation |
|---|---|---|
| R0 — source presence | an instruction exists at its named source | source inspection at a named revision |
| R1 — receiver parity | the runtime-facing copy equals its source | byte comparison or resolved identical content |
| R2 — invocation | the runtime selected the command receiver | tool/event trace for that invocation |
| R3 — complete load | the canonical workflow content entered the run | completed full-read trace, or invoked exact full-copy content |
| R4 — later conformance | later effects followed the applicable role, order, gate, and stop | observed events plus the complete artifact diff |
| R5 — controlled comparative effect | one entry design changes adherence relative to another | predeclared repeated trials and an uncertainty interval |

A higher level is never inferred from a lower one: presence or clean-receiver parity does not
prove invocation, load, later conformance, or comparative effect. Declaration, tracked-copy
presence, installed state, clean-receiver reproduction, and live-host observation are also
reported separately.

## 10) Context Selection

The applicable root instructions are already active. For a TFW command, read its canonical
workflow completely; that workflow alone owns the ordered read contract for its checkpoints.

1. Read the selected task or phase `status.md` and `journal/` before derived, shared, or
   historical material.
2. Read only the task artifacts, shared-rule ranges, templates, and PV/knowledge items named
   by the current checkpoint. A triggered task fact may add a read; it never becomes permanent
   common preload.
3. Address a shared range by unique heading. A missing or duplicate addressed heading is a
   hard stop: report the file and heading rather than guessing a range.
4. Classify every full-file or repeated edge by checkpoint purpose and authority. An
   unclassified full `conventions.md`, `glossary.md`, or `KNOWLEDGE.md` edge is prohibited.
5. Generated manifests and read audits report the contract; they are never authority and no
   role reads them as an instruction source.

Skills and adapter roots dispatch commands and enforce only what must hold before a workflow
can be opened. They do not restate the workflow's algorithm or independently preload shared
files.

## 10.1) Fact Categories

> Universal categories for Fact Candidates. Open list — agents can use custom categories when none fit.

| Category | Scope | Examples |
|----------|-------|----------|
| `environment` | Where the work lives | servers, tools, platforms, classrooms, labs, hosting |
| `process` | How work gets done, business processes | schedules, approvals, reporting cadence, grading cycles |
| `stakeholder` | Who needs what | priorities, pain points, expectations, quotes, key decisions |
| `constraint` | What limits exist | contractual obligations, regulatory deadlines, resource caps, technical limits |
| `convention` | Agreed standards | naming, style, format, language, tone |
| `domain` | Subject matter knowledge | revenue patterns, client segments, market metrics, business rules, curriculum |
| `context` | Background that shapes decisions | market conditions, competitive landscape, regulatory changes, prior decisions |
| `risk` | Known dangers | client concentration, market dependency, knowledge silos, fragile dependencies |
| `philosophy` | Values, principles, vision | design rationale, methodology beliefs, north star decisions, "why we do it this way" |

## 10.2) Knowledge Infrastructure

| File | Purpose |
|------|---------|
| `KNOWLEDGE.md` | Stable entry, architecture/reference map and preserved legacy/source routes; no maintained inventory/counts |
| `knowledge/{category}.md` | Retained legacy topic meaning and source identities; no forced conversion or later marker rewrite |
| `knowledge/records/` | Independently addressable qualified human knowledge and technical/reference decisions; one record form |
| Existing role/stage sections | First capture surface, owned by the actual producing role at its checkpoint/return |
| `.tfw/templates/knowledge/handover.md` | Minimal task-local fallback only when existing sources cannot carry a real return |
| `.tfw/workflows/knowledge.md`, `.tfw/workflows/docs.md` | Existing human-knowledge and technical/reference qualification owners, respectively |
| Existing `.tfw/knowledge_state.yaml` and processed markers | Preserved inert historical evidence; no current gate, inventory, reset or new state scaffold |

### Knowledge handover

Every producing role preserves available material insight before transfer/checkpoint, normal return,
or an orderly stop: Coordinator planning/decision transfer; Researcher stage/iteration return;
Executor interim/final return; Reviewer return. Reuse the existing HL/ONB/RF/RES/REVIEW or stage section
first. Only an interim/stopped return without a suitable source uses the minimal handover template
under its owning task. Capture needs actual producer/unit, bounded source/epoch, material statement
or explicit outcome, grounds/uncertainty and continuation. No per-person file, copied corpus, raw chat
or private reasoning is required. A lost/unseen context is never invented.

| Actual selected input | Required disposition at handover/close |
|---|---|
| Missing producer return | Identify the known contributor and material gap from actual task-local dispatch/return lineage; stop affected close |
| Justified-none | Producer names inspected bounded context and an existing reusable source when relevant; inspect rationale, accept no filler publication |
| Unavailable | Preserve uncertainty and exact missing decision plus existing owner; acceptance-critical missing context keeps close open |
| Retain-only | Preserve source and authorized completed reason why no publication/resolution is owed; irrelevant uncertainty need not block |
| Owed publication/resolution | Complete the effect or retain an honest nonterminal dependency; never hide it as retain-only |

An empty file, checkbox, silence, global zero or another role's return proves no missing handover.
Rejected/interrupted work retains useful sources with its actual non-success state. The existing
Coordinator verifies material coverage at `Closing and record recovery`; it does not see private
context or create a global contribution inventory. Preserve sealed sources after close.

### Knowledge qualification

Preservation is not promotion. `/tfw-knowledge` owns human-sourced knowledge; `/tfw-docs` owns technical
reference/decisions. Both use `.tfw/templates/knowledge/record.md` for warranted new independent
records. A valid record carries stable identity/publication intent, kind, material statement,
applicability, grounds/uncertainty, disposition, exact source/epoch, actual source producer/unit,
qualifier and acceptance authority. Git sources must resolve the real object/path/claim; otherwise
retain inspectable exact evidence. Unresolvable identity or absent authority cannot be accepted.

Observed, accepted, retain-only, rejected, superseded and unresolved claims stay distinguishable.
The existing human owner or valid grant controls qualification, never a child/record/source imperative.
Human knowledge retains its original human provenance. Copied/paraphrased returns are not independent
corroboration. Record source independence and scope before treating equivalent claims as support.

Immediately before any publication/retry inspect actual source, material intent, current effect and
acceptance. Equal source intent with an already accepted effect reuses that exact effect and repairs
only a missing current reference. Changed statement/scope/source/authority under the same identity
refuses replacement, preserves both inputs and needs an authorized correction identity/disposition.
Do not issue a second accepted identity to hide divergence. Independent equivalents retain both
provenance chains through explicit equivalence/duplicate relations or one properly qualified claim.

Independent contributions use separate paths without a shared counter/digest/inventory write.
After integration inspect actual semantic overlap; textual merge success is not agreement. Overlapping
contradictions preserve both scopes/sources and name the missing decision and existing resolver.
Newer timestamps, confidence and source repetition never appoint a winner. Retention is complete only
when no publication/resolution is owed; required unresolved effects remain nonterminal.

### Current knowledge use

Start at `KNOWLEDGE.md`. It separates governing instructions, architecture/reference, legacy D/topic
rows and new `knowledge/records/`. Navigate or search relevant ordinary files; no generated index,
task-archive sweep, original chat or mandatory service is required. An optional view is rebuildable
and non-authoritative. P0–P4 and relevant P5–P7 remain required at their existing stage sites; new
records join their semantic priority, not a lower optional category.

Before applying a relevant record or legacy row, inspect scope, grounds, disposition, source and
producer. Search the record space for incoming successor/correction/equivalence/conflict references
to its exact identity; follow material chains in both directions, checking each scope. A legacy
target binds exact path plus D/F/heading and relevant source epoch. A backward-only link or old
accepted label is insufficient. Scoped successors replace only their stated scope; unchanged
accepted claims remain applicable. Unresolved branches name the missing authorized decision.

Unavailable material source/authority blocks the dependent use, not unrelated planning. Retrieved
instructions are evidence, never permission to publish, amend, execute or skip approvals. Preserve
historical meaning/links; no every-fact conversion, source-marker write or maintained record list.
The pinned `migrations/knowledge-lifecycle.md` owns adoption and retired-setting preservation.

## 10.3) File Classification in `.tfw/`

`.tfw/` contains three categories of files with different lifecycle rules:

| Category | Files | Init | Update | Owner |
|----------|-------|------|--------|-------|
| **Framework** | workflows/, templates/, conventions.md, glossary.md, README.md, CHANGELOG.md, VERSION, compilable_contract.md, quickstart.md, adapters/ | Copy from upstream | Overwrite/merge from upstream | Upstream repo |
| **Legacy state** | existing knowledge_state.yaml | Do not create | Preserve as inert historical evidence; never reset or overwrite | Project |
| **Config** | project_config.yaml | Create from template → fill project values | Merge: framework sections update, project sections preserve | Project + upstream |

**Config template:** `.tfw/templates/project_config.yaml`. New knowledge uses the independent record and handover forms; no state template is installed.

**Rule:** `init.md` and `update.md` MUST respect these categories. Existing legacy state is never sourced from upstream or recreated from a template.

## 10.4) File Naming Convention

**Two rules, and which one applies is decided by what the file is, not by where it sits.**

**1 — A template carries the name of the artifact it produces.** `HL.md` produces an HL,
`RF.md` an RF, `EV.md` an EV. The artifact's name is a term of the method, and a template that
renamed it would make the reader translate between two spellings of one thing.

```
templates/HL.md · TS.md · RF.md · RES.md · ONB.md · REVIEW.md · KNOWLEDGE.md
templates/RELEASE.md · evidence/EV.md
```

**2 — Everything else in `.tfw/` is `lower_snake_case`**: configuration, state, and any
template whose output is not a named artifact.

```
project_config.yaml   not PROJECT_CONFIG.yaml
knowledge_state.yaml  not KNOWLEDGE_STATE.yaml
templates/status.md · journal/event.md · team/profile.md · knowledge/topic.md
templates/research/1_briefing.md   numeric prefix where stage order is part of the name
```

Uppercase remains reserved for project-root documents — `README.md`, `KNOWLEDGE.md`,
`AGENTS.md` — and for `.tfw/` framework docs, `CHANGELOG.md` and `VERSION`.

**A template producing into a directory lives in a directory of that name**, mirroring its
output: `templates/journal/event.md` → `{task}/journal/<name>.md`. An underscore standing in
for a directory separator — a `journal_event` shape rather than `journal/event` — is what
this rule replaced.

> **Why this is stated as two rules rather than one.** Until `2.0.0-dirty.3` §10.4 said every
> Markdown template follows `lower_snake_case`, and **nine of its own twenty subjects
> contradicted it** — every artifact template did. Its single illustration was
> a `topic_file` template a move had already deleted, so the one example it offered named a
> file the payload no longer shipped. Swapping that example for a surviving filename was the
> available small fix and it was refused: it would have left a rule wrong about nine of the
> files it governs, and a rule nobody follows teaches the reader to distrust the ones that
> are true. What was wrong was the rule.

## 11) Quality Standard (no compromises)

- No placeholders.
- Results must be usable without manual edits.
- If a result is wrong — fix the prompt/context and retry until quality is met.
- Tasks are atomic and human-verifiable.
- **Content Language:** Template structure (headings, labels, field names) is always English.
  Artifact content is filled in the language specified by `tfw.content_language` in project_config.yaml.
  Default: `en`. Agent MUST check this value before writing artifacts.

### Design Rules

- **Token density:** workflow instructions ≤1400 words. A ceiling is not a target or permission to
  remove meaning; templates own format and workflows reference templates.
- **Workflow vocabulary:** Phase = task unit; Step = ordered workflow action; Stage = cognitive
  subprocedure; Gate = pass/stop, routing or authority boundary.
- **Inline enforcement**: enforcement-critical values MUST be inline (Pattern A: defaults + config key). Pure refs (Pattern B) = broken
- **DNA/Library**: Role Lock + Mindset = always inline. Reference data = via ref-inside-step. Step self-contained, ref adds precision
- **Progressive Disclosure**: agent loads only what it needs now. Mode files loaded at Step 2, not at start
- **A command written into a workflow must survive its adapter.** No `$0`–`$9` and no `$ARGUMENTS` in any
  shell or `awk` snippet a role runs: adapters may substitute them before the role reads the command.
  Use named variables or literal examples and exercise the command once from the project root before
  shipping it. History: TLD and RDP

## 12) Safety and Execution Honesty

- Never claim something was "run" or "tested" outside the observed session and recorded evidence.
- Never request secrets in plain text. Use environment variables.
- Evidence requires real-environment observation — deploying, opening, running, or viewing completed work in conditions beyond the build/test toolchain. VERIFIED status requires an artifact reference (file path or inline output).

## 13) Trace Discipline

Every task produces an **RF file** with results, decisions and observations, a **`status.md`** carrying its live state, and a **`journal/`** recording the events that moved it. Together with its task-local artifacts, these form the project's memory across sessions — and because each lives inside its own task, two tasks can advance without their traces colliding.

Debt found in a review is part of that trace and lives in the REVIEW that found it, disposed of before the task closes. There is no project-level debt registry: the one that existed was retired at 2.1.0 and its rows are history in `tasks/DEBT-SNAPSHOT.md`.

Reverting a result does not revert its trace. A rejected task's folder and its board row are never deleted: the work may leave the working tree, the record that the work happened stays.

## 14) Anti-patterns (prohibited)

- Executor codes before blocking questions resolve
- Executor codes without reading HL
- Coordinator closes without review or REVIEW
- RF omits test results or observations
- TS precedes HL approval
- Executor modifies the Master HL
- Executor makes architectural decisions not in HL
- Executor modifies out-of-TS files, including “obvious fixes”
- Executor makes undocumented “bonus fixes”
- Executor writes RF before build/lint passes
- Executor omits material debt/dead code from Observations
- Coordinator leaves a surviving Executor observation unrecorded or undisposed in REVIEW §5
- Coordinator writes ONB/RF or code → **Role Lock violation**
- Executor writes HL/TS or changes scope → **Role Lock violation**
- Executor writes REVIEW → **Role Lock violation**
- Reviewer approves without opening files or spot-checking RF claims against artifacts
- A review checklist row is added without an evidenced firing rate or a stated asymmetric consequence
- Executor omits RF §7-9 (Fact Candidates, Strategic Insights, Diagrams) — sections are mandatory; empty content ("No X.") is valid, absent section is not
- Researcher omits Findings Map in RES — section is mandatory; "No findings map." is valid if genuinely no visualization relevant
- Coordinator reads KNOWLEDGE.md in context loading but never cites relevant items in HL §4 — "read but don't use" pattern breaks cross-task knowledge flow
- TS contains ready-made implementation — TS §5 must contain acceptance criteria (WHAT), not code or steps (HOW); implementation belongs to executor
- Coordinator reads own TS instead of RF when planning next phase — before writing TS for Phase N, read RF of the latest completed phase; plan ≠ fact
- Executor writes RF without opening template — RF template must be opened before writing; writing from memory drifts from required structure
- Coordinator answers ONB questions without source — when uncertain, present options and context, not decisions on behalf of the stakeholder
- Executor marks evidence VERIFIED without artifact reference in `evidence/` folder — assertion without evidence
- Executor marks evidence N/A without justification from TS Evidence field or documented reason
- Executor writes RF §5 Evidence before actually collecting evidence — evidence must be contemporaneous, not reconstructed
- Reviewer approves RF without checking that evidence artifact references resolve to real files or inline output
- Executor marks evidence DEFERRED without naming the specific blocker (missing environment, unavailable device, pending deployment)
- Anyone edits a frozen HL section without a §12 row carrying the valid rule-8 verdict — the silent contract edit the amendment channel exists to replace
- Researcher submits HL recommendations without classifying each row as a refinement or an amendment proposal — one undifferentiated channel is how "risk probability is Medium" and "drop Phase B" arrive together
- Coordinator applies an amendment before its valid rule-8 verdict — the proposal and change become one act, so the ruling follows what it governs
- Research starts on an uncommitted approved HL — the baseline cannot be diffed, so drift becomes documented and permanently unverifiable
- Any role treats a remark inside a research thread, a review or a chat as an amendment verdict — a comment is input, a verdict is a distinct recorded act
- An agent cites its own delegation as authority to accept a scope or budget overrun — a mandate is a ceiling, and authority that extends itself is not authority
- A Phase HL authors its own acceptance criteria, failure conditions, vision or principles — a second, unapproved contract one level below the one that was ruled on
- A reviewer approves work that satisfies the TS but not the approved contract or the north star — the TS is downstream of any drift, so a green review against it can only confirm the drift
- A reviewer asserts alignment without citing the clause it serves — an unciteable claim is indistinguishable from a fabricated one, and a citation that resolves while being irrelevant is the same defect one layer in
- A whole-tree restore reverts task state past a recorded failure
- A workflow acts on a task from the derived index instead of re-reading that task's `status.md`
- A task directory is moved to express status or change its creation-year folder
- An identifier is allocated from a project-wide maximum, counter, or another task directory
- A journal event is edited/deleted instead of corrected by a new referencing event
- A journal event copies artifact or chat bodies instead of referencing them
- A status outside the vocabulary is normalized instead of reported verbatim
- Identity is inferred from an OS username, hostname, folder, or account display
- A per-user file is stored on the shared tree
- A workflow command contains `$0`–`$9` or `$ARGUMENTS`
- A task closes with an undisposed debt item or a disposition naming no existing phase/round and cited condition
- A project-level debt list, per-task debt file, or generated backlog view is introduced
- Work is left unfinished because it can be recorded as debt
- A rung-2 finding is addressed only to the Executor, who cannot amend a TS
- A 🔄 REVISE item names no breached acceptance criterion or frozen claim
- Broad staging mixes sibling work (TD-144; TFW-60 review; verbal rule 0/1)
- An unrelated landing commit hides its producer from path history (TD-178)
- A foreign caller resumes “last,” writing into an undelegated session rather than the returned id
- An agent rules its proposal after transcription, session replacement, or grant change
- Claimed delegation lacks one human-rooted child-only prefix or substitutes accountability
- An Executor initiates, or a phase Coordinator points to an ancestor/task Coordinator

History for these prohibitions: D61, D68, D72, and the named task/snapshot traces.

### 14.1 Terminology Origin (maintainer reference)

The following terms used in research stage templates are TFW-native and intentionally avoid methodology names:

| TFW Term | Meaning | Origin |
|----------|---------|--------|
| Dimension | An independent decision factor (degree of freedom) in the problem | Zwicky's GMA: "parameter" |
| Alternative | One valid value for a Dimension | Zwicky's GMA: "parameter value" |
| Configuration Space | The full cross-product of all Dimension alternatives | Zwicky's GMA: "morphological box" |
| Consistency Check | Pairwise incompatibility analysis eliminating invalid combinations | Zwicky's GMA: "cross-consistency assessment (CCA)" |
| Surviving Configuration | A configuration that passed all pairwise checks | Zwicky's GMA: "compatible solution" |

> **Scope:** This note is for framework maintainers only. The terms "Zwicky", "GMA", "General Morphological Analysis", "morphological box", and "cross-consistency assessment" MUST NOT appear in any researcher-facing template or workflow instruction.

## 15) Role Lock Protocol

Each workflow declares a **🔒 ROLE LOCK** at the top. The agent MUST refuse any action outside the locked role.

**Acceptance authority is named here, not only in the workflow that exercises it.** Deciding whether
new work exists belongs to the Coordinator; a reviewer that ruled it would be deciding the
consequences of its own findings. For rung 1, the Coordinator records an acceptance ruling in the
live REVIEW but authors no implementation order: the approved TS remains governing. The complete
recipient/artifact/state contract is owned by `The 🔄 REVISE route` in §5.

| Workflow | Role Lock | Permitted Artifacts | Forbidden Artifacts |
|----------|-----------|---------------------|---------------------|
| `init.md` | Coordinator | RES, RF, project config files | HL, TS, code |
| `plan.md` | Coordinator | HL, TS, acceptance rulings appended to a live REVIEW | ONB, RF, RES, REVIEW creation/proposals, code |
| `research/base.md` | Researcher | RES, research/ stage files | HL, TS, ONB, RF, REVIEW, code |
| `handoff.md` | Executor | ONB, RF, code | HL, TS, RES, REVIEW |
| `review.md` | Reviewer — **marks and proposes**; the **Coordinator** holds acceptance authority over dispositions and rules them once at the close of review (Step 6) | review stage files (map.md, verify.md, judge.md), REVIEW, proposed dispositions | ONB, RF, HL, TS, code, **disposition rulings** |
| `docs.md` | Coordinator | selected KNOWLEDGE.md reference ranges, technical records, current effect reference | code, human-knowledge promotion, historical source edits |
| `knowledge.md` | Coordinator | selected human-knowledge records and current qualification reference | code, technical decisions, legacy/source/state rewrites |
| `release.md` | Coordinator | VERSION, CHANGELOG.md | code |
| `update.md` | Coordinator | `.tfw/` files, adapter copies | code |
| `config.md` | Coordinator | project_config.yaml, workflow files, convention files, adapter copies | code |

### Hard Stop Rule

When a Coordinator reaches the end of planning (TS approved), the correct action is:
1. Inform the user that planning is complete
2. Instruct: "Start `/tfw-handoff` to begin execution"
3. **Do NOT continue into execution**

When an Executor finishes RF, the correct action is:
1. Inform the user that execution is complete
2. Instruct: "Start `/tfw-review` to review the results"
3. **Do NOT write a REVIEW file**

When a Researcher finishes RES, the correct action is:
1. Inform the user that research is complete
2. Instruct: "Continue with `/tfw-plan` to apply research findings"
3. **Do NOT write HL or TS**

When a Reviewer reaches a verdict, the correct action is to **name the next act** — a decision with
no addressee is not a decision:
1. On ✅ APPROVE — record the independent verdict and authorized KNW transition, then return to the
   Coordinator for `Closing and record recovery`. The Reviewer never runs project qualification or declares DONE;
   it remains available for independent assessment of affected final claims
2. On 🔄 REVISE — state that the items are **proposals**, say how many, and return the work to the
   Coordinator: "Start `/tfw-plan` to rule the round." Do not move lifecycle, rule a bound, or
   dispatch an Executor; the Coordinator applies `The 🔄 REVISE route` in §5
3. On ❌ REJECT — route by §5's three destinations and say **which**: (a) 📝 HL_DRAFT, (b) 🔬 RES, or
   (c) 🟡 TS_DRAFT
4. **Do NOT fix anything yourself** — a reviewer that repairs its own findings has reviewed nothing

When a Coordinator receives work returned by a 🔄 REVISE, the correct action is:
1. Rule all proposals once and apply the exact case in `The 🔄 REVISE route` in §5
2. Name the table's next recipient and governing artifact; dispatch only when that case permits it
3. **Do NOT execute the round yourself** — ruling/ordering is not doing

## 16) Compilable Contract

> Build-time specification for deterministic compilation of TFW artifacts into documentation.
> Defines the Source Manifest, Reference Format, and Output Structure.
> Full contract: [compilable_contract.md](compilable_contract.md)
