# Extract — Iteration 2: candidate configurations and exact contracts

> **Mindset:** Analyst. Make the complete configuration visible before judging it.
> Parent: [HL-TFW_20260913-151442_RWNR](../../HL-TFW_20260913-151442_RWNR.md)
> Goal: decide whether Resume can be retired without loss of lifecycle safety, trace integrity, or a discoverable recovery path.

## Configuration Space

| Config | D1: return inspection | D2: close/recovery | D3: stale handling | D4: history | D5: accounting | D6: Plan size |
|---|---|---|---|---|---|---|
| C1 | Keep Resume | Resume exposes direct contract | Existing 11-command sync | Split oracle | Reproducible counter as diagnostic | Separate future Plan reduction |
| C2 | Pure Plan pre-route gate | Plan names direct contract and stops | Versioned owned-only removal | Split oracle | Amend baseline to one counter; count moved text | Same-change Plan cap ≤1,200 |
| C3 | Pure Plan pre-route gate | Plan names direct contract and stops | Manifest omission only | Split oracle | Reproducible counter | Permit Plan growth below combined baseline |
| C4 | Guards repeated in every lifecycle workflow | Each workflow recognizes close/recovery | Versioned owned-only removal | Split oracle | Reproducible counter | Keep current Plan size |
| C5 | Pure Plan pre-route gate | Plan executes close/recovery | Versioned owned-only removal | Split oracle | Reproducible counter | Same-change Plan cap ≤1,200 |
| C6 | Permanent Resume tombstone redirects to Plan | Direct conventions contract | Versioned removal except tombstone | Whole-file equality for all 182 | Preserve 2,685 unexplained | Keep current Plan size |
| C7 | Pure Plan pre-route gate | Plan names direct contract and stops | Versioned owned-only removal | Split oracle | Reproducible counter including all source additions | Net-negative Plan, with an explicit noncompliance disposition rather than an immediate cap |

C7 is the combination not proposed in Briefing: it separates the combined-surface proof from immediate Plan cap compliance. It remains analytically distinct so Challenge can decide whether an explicit disposition is enough or whether the cap must be an acceptance condition.

## Findings

### E1: exact C2 Plan pre-route contract

C2 adds one section at the start of `.tfw/workflows/plan.md`, after its Read Contract and session-identity resolution but before the Knowledge Gate. The section is an inspector/router, not another lifecycle stage.

#### Pre-route algorithm

1. If the request contains no existing task/phase reference, return `NEW` and continue today's task-inception path. If it contains an exact reference, resolve it through the deduplicated active-plus-historical union from `tfw.task_containers` and optional `tfw.historical_containers`; ordinary discovery remains active-only.
2. Zero exact matches is `NOT_FOUND`; more than one distinct resolved path is `COLLISION`. Report and stop. A historical-only match is `HISTORICAL_ONLY`: read only its cited original state/artifacts when present, state that continuation needs separate authority, and stop without matrix, repair, or mutation.
3. For one active task, read its `status.md`, journal and governing lineage. If the task is `PHASES` and a phase is selected, read that phase's own state/journal and evaluate the phase. If no phase is selected, read every current phase state/journal, render the six-column matrix already defined by Resume, ask which phase to work on, and stop.
4. Resolve session identity only after the exact live task/phase resolves. The evaluator may read and render; it may not write status, journal, HL, TS, REVIEW, close records, or code. It returns a classification and exact route, then stops unless the result is `CONTINUE_PLAN`.
5. If the user's selected intent is close or carrier repair, or the state evidence identifies `KNW` or an APPROVE/carrier mismatch, emit the exact non-command route in E2 and stop. Never execute that contract inside Plan.
6. Apply this state table. An indicated route is output, not invocation.

| Resolved state/evidence | Pre-route result | Exact output/next owner | Pre-route mutation |
|---|---|---|---|
| no existing reference | `NEW` | continue current Plan inception | none |
| exact reference absent | `NOT_FOUND` | report exact reference and active/history roots; stop | none |
| whole-ID collision | `COLLISION` | report every resolved path; stop | none |
| historical-only | `HISTORICAL_ONLY` | report read-only history; separate continuation authority required; stop | none |
| missing/malformed status, journal, lineage, duplicate YAML, contradictory selected scope | `INVALID_CARRIER` | name defect; `Coordinator control: Closing and record recovery` only if administrative repair is reconstructable, otherwise accountable owner; stop | none |
| `TODO` | `CONTINUE_PLAN` | Plan's existing understand/HL path | none before existing Plan gates |
| `HL_DRAFT` | `CONTINUE_PLAN` | Plan's existing HL approval/research decision path | none before existing Plan gates |
| `RES` | `ROUTE_RESEARCH` | `/tfw-research` | none |
| task `PHASES`, no phase | `WAIT_PHASE` | phase matrix plus “Which phase should we work on?”; stop | none |
| task `PHASES`, exact phase selected | `EVALUATE_PHASE` | apply this table to phase-local lifecycle | none |
| selected phase itself says `PHASES` | `INVALID_CARRIER` | report prohibited nested rollup; stop | none |
| `TS_DRAFT`, TS/approval lineage incomplete | `CONTINUE_PLAN` | Plan TS/approval gate | none before existing Plan gates |
| `TS_DRAFT`, exact TS approval valid | `ROUTE_EXECUTION` | `/tfw-handoff` | none |
| `ONB` | `ROUTE_EXECUTION` | `/tfw-handoff` using governing TS/return lineage | none |
| `RF` | `ROUTE_REVIEW` | `/tfw-review` | none |
| `REV`, REVIEW absent/incomplete | `ROUTE_REVIEW` | `/tfw-review` | none |
| `REV`, valid REVISE | `CONTINUE_PLAN_REVISE` | Plan Step 8 and shared rung table; Coordinator rules once | none before that existing ruling gate |
| `REV`, valid REJECT | `WAIT_OWNER` | owner chooses HL, research, or TS return; stop | none |
| `REV`, valid APPROVE but status/event did not reach `KNW` | `ROUTE_RECORD_RECOVERY` | exact E2 direct route; stop | none |
| `KNW` | `ROUTE_CLOSE` | exact E2 direct route; stop | none |
| `BLOCKED` | `WAIT_DEPENDENCY` | name recorded dependency/ruler and its recorded return route; never infer clearance | none |
| `DONE` | `TERMINAL` | report final outcome and stop | none |
| `REJECTED` | `TERMINAL` | report unsuccessful terminal state and stop | none |
| `UNDECLARED` | `WAIT_OWNER` | accountable owner resolves verbatim value with transition trace | none |
| any other value | `UNDECLARED` | preserve source value verbatim; accountable owner route; stop | none |

The implementation-level invariant is: for every result except `NEW`/`CONTINUE_PLAN`/`CONTINUE_PLAN_REVISE`, repository path set and bytes before and after pre-route evaluation are identical. For those three results, the evaluator itself still has identical before/after bytes; only the already-existing subsequent Plan gate may later authorize a write. Matrix rendering and questions are outputs, never state transitions.

### E2: exact non-command close/recovery route

The route text is fixed so a user can copy it without learning another command:

> **Coordinator control:** use `.tfw/conventions.md` → `Closing and record recovery` directly for the exact selected task/phase; do not perform Plan work. Read its state/journal, governing authority and live REVIEW first. Stop on missing authority or non-reconstructable lineage.

It has three entry chains, all ending at the same unique heading:

```text
Reviewer APPROVE → writes KNW transition → returns reviewed identity/limits
                 → existing Coordinator → Closing and record recovery

/tfw-plan exact returning reference → pure state inspection → KNW or recoverable carrier gap
                                    → prints Coordinator-control text and stops
                                    → selected natural-language request → direct heading

user already knows/selects close or repair → same Coordinator-control text → direct heading
```

The heading is already self-authorizing only as to role and algorithm: it grants no absent mandate or scope. Close writes are governed by the selected task authority and independent REVIEW; material changes receive separate Reviewer assessment. Record repair is allowed only for unchanged reconstructable results and writes only truthful current control state. Plan never gains those permissions, adapters carry no branching behavior, and no `/tfw-*` alias or hidden workflow is created.

### E3: version-addressed owned-only retirement algorithm

The guide filename is the exact owner-selected G2 release version from the pinned target. G1 does not invent that version. The guide records `resume` as a retired command and enumerates the old source identities applicable to each supported installed version.

#### Preflight classifications

For each old source or receiver path, compare actual bytes to the corresponding old canonical blob reached from installed provenance and the pinned migration history:

| Observation | Class | Effect |
|---|---|---|
| path absent | `ABSENT` | success/no-op |
| bytes exactly equal an applicable old canonical blob | `OWNED_EXACT` | eligible for deletion |
| one valid managed marker pair, old inner block exact, outer bytes arbitrary | `OWNED_BLOCK` | replace only inner block; outer bytes must remain identical |
| different bytes, unknown provenance, duplicate/malformed markers, or unmarked live root | `FOREIGN_OR_DRIFTED` | preserve bytes; refuse the retirement semantic group before writes |
| config key absent | `ABSENT` | success/no-op |
| config key/value exactly `resume: .tfw/workflows/resume.md` | `OWNED_EXACT` | remove key during merge |
| config key has any other value or duplicate | `FOREIGN_OR_DRIFTED` | preserve; refuse group |

The preflight set includes both old canonical payload paths, the four possible adapter command destinations, selected persistent adapter roots, and `.agent/rules/agents.md` when it exists. The singular compatibility root is never deleted wholesale: exactly one valid `TFW:CODEX` block can be updated; absence succeeds; any other form is preserved and refuses a successful retirement claim.

#### Apply and postconditions

1. Pin the target object and version; read its update workflow, changelog range, and version-addressed retirement guide. Verify installed provenance and all expected old blobs.
2. Inventory all selected adapters and every preflight subject. If any required subject is `FOREIGN_OR_DRIFTED`, write nothing in the connected retirement group; report exact path, observed identity, expected identities, and authoritative next action.
3. Install the coherent target payload and roots. Delete only `OWNED_EXACT` retired payload/receiver paths; update only `OWNED_BLOCK`; remove only the exact config key/value. Preserve all foreign neighbors and project-owned config/state/history.
4. Verify the target manifest has exactly these ten commands: `plan`, `research`, `handoff`, `review`, `docs`, `knowledge`, `release`, `update`, `config`, `init`. For each of four adapters, a clean receiver has one valid persistent root and exactly ten unique command destinations, with no Resume source, target, route, alias, or tombstone. Cursor absence before install is a normal empty-receiver case.
5. Verify the source payload and existing receiver contain no owned retired path; all exact-copy and managed-block roots match their source while outer/foreign bytes remain unchanged. Run the live-wording allowlist and relevant receiver checks.
6. Re-enter from the same pinned target. Every old path is `ABSENT`, roots/config equal the intended target, no path is recreated, and the second run has an empty diff. Only then may the update receipt claim retirement complete.

This algorithm extends the existing pinned-guide/update authority; it is not a new installer or runtime dependency.

### E4: split candidate history oracle

The baseline path selector runs once against `a2363fd07253ca92410db149b4301432de79be3b`; candidate classification never reselects paths from candidate text.

- **Task-trace oracle:** regenerate the sorted 179-entry baseline tree manifest by the G4 procedure in Gather and require its SHA-256 to be `ed52c4c26845e90c14a569f867ec2200b18da44374f7df2fd897bf7fb58bef96`. At Candidate, require the same 179 paths, modes and blob IDs. Missing, renamed, mode-changed, or content-changed is failure.
- **Aggregate oracle:** read the three baseline blobs named in Gather as raw bytes and split with line terminators retained. For each candidate aggregate, consume candidate raw line chunks left to right and require every baseline chunk to appear in the same order with exact bytes. Extra candidate chunks may occur anywhere; a missing, reordered, edited, re-encoded, or line-ending-changed baseline chunk fails. Path and mode also remain fixed.
- **Live oracle:** evaluate the 23 live paths separately. Historical mentions are allowed only in the fixed 179+3 set and the new versioned migration/changelog record; live sources/receivers may not expose a Resume command or replacement alias.

### E5: one counter, moved-text accounting, and the Plan disposition

Define `W(blob)` as: decode the exact Git blob with strict UTF-8, then count Unicode regular-expression matches of `\S+` without normalizing bytes, Markdown, punctuation, or line endings. This is the repository's existing `_words` algorithm.

The corrected immutable baseline is:

```text
B = W(plan@a2363fd) + W(resume@a2363fd)
  = 2,021 + 716
  = 2,737
```

For a tested immutable Candidate, define:

```text
C = W(candidate plan)
    + Σ W(candidate-side added lines for every other changed surviving instruction source)
```

“Candidate-side added lines” are the non-header `+` lines from a zero-context, no-renames baseline→Candidate diff, joined in path/order and counted with the same `W`. A modified line contributes its entire candidate line; a moved line is a deletion plus an addition and is therefore counted at its destination. Count source-of-truth instructions once; an installed byte-exact copy or marker-bounded projection is excluded only after parity is proved. Tests/evidence and the 179+3 historical set are assurance/trace, not retained instruction surface. The exact inclusion domain is all changed surviving files under `.tfw/workflows/`, `.tfw/conventions.md`, `.tfw/migrations/`, `.tfw/adapters/`, `.tfw/templates/project_config.yaml`, the three public root READMEs, and any new non-generated instruction source introduced by the Candidate. Machine config removals add zero; any added instructional config line is included. A behavior-bearing adapter, redirect, wrapper, or unclassified new instruction path is a structural failure, not a way to escape the sum.

C2 imposes both independent conditions:

1. `W(candidate plan) ≤ 1,200`. The routing table must be funded by rewriting/deduplicating Plan in place and by referencing existing canonical headings/templates. No extracted continuation workflow or helper is permitted.
2. `C < B` with exact operands and path/addition evidence recorded. The 1,200 cap leaves 1,536 words of headroom for all counted non-Plan additions while still requiring strict net subtraction.

The frozen 2,685 value cannot be silently replaced. A classified §12 amendment must change only the numeric/counter clauses to the exact `W`, `B=2,737`, and candidate formula above; purpose, phases, DoF and retirement authority remain unchanged. If the owner rejects that amendment, if Plan exceeds 1,200, if `C ≥ 2,737`, or if any moved instruction is unclassified, C2 fails and C1 keeps Resume.

## Checkpoint

| Found | Remaining |
|---|---|
| C2 has a complete state/no-mutation table and exact gate position. | Execute positive, negative, wait, terminal and mutation-model cases. |
| The direct heading has fixed user-facing route text and a complete Reviewer/Coordinator chain. | Attack fresh-session discoverability and Role Lock leakage. |
| The migration has path classes, all-preflight refusal, four adapter destinations, singular-root treatment, ten-command and repeat postconditions. | Execute ownership/absence/foreign/idempotence model cases. |
| The history selector, task digest and aggregate byte-line oracle are exact. | Re-run generation and deliberate mutants. |
| The counter and Candidate formula are exact; Plan ≤1,200 is the disposition; the 2,737 correction is classified as an amendment. | Run reproducibility/budget mutants and decide H1–H4. |

**Sufficiency:**
- [x] External source used? Every contract is derived from the primary sources and immutable Git objects gathered in stage 2.
- [x] Briefing gap closed? The five gaps now have exact candidate algorithms and fallback conditions.
- [x] Configuration Space built from Gather dimensions? Seven configurations cover all six dimensions and include the previously unproposed C7 split-disposition option.

Stage complete: YES
→ User decision: already fixed by dispatch; challenge C1–C7 with C1 as fallback.
