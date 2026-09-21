# RF — TFW_20260920-223357_FRATS / Phase A: Explicit Coordination, GATEWAY and Session Identity

> **Date**: 2026-09-21
> **Author**: saubakirov via Codex Executor
> **Status**: 🟢 RF — Complete
> **Parent HL**: [Master HL](../HL-TFW_20260920-223357_FRATS.md)
> **TS**: [TS Phase A](TS__phase-a__explicit_coordination_gateway_and_session_identity.md)
> **Producer unit**: `codex:thread:local:01a0c3a2-c742-7962-a981-369effb5ac83`
> **Parent Coordinator**: `codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf`
> **Activation / dispatch source**: owner-direct `/tfw-handoff` for FRATS phase-a
> **Coordination authority**: `TS__phase-a__explicit_coordination_gateway_and_session_identity.md @ ad6042dad73aa04b9bbe9f13880c5a944e7e4f05`
> **Originating proposer**: `none — owner-direct activation`

---

## 1. What Was Done

Phase A now has one provider-neutral coordination contract. Current work is autonomous only after an
exact skill/task/phase activation; task state carries the five routing facts; default traffic is
vertical through the unit's own Coordinator; iterative dialogue requires an exact grant and separate
GATEWAY; authority answers are immutable `gate_answer` events; and current role artifacts identify
their actual producer and route. Legacy modes/statuses remain readable without becoming current
authority.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `ad6042dad73aa04b9bbe9f13880c5a944e7e4f05` |
| Baseline / Candidate | `c80c0dd5e79a6e996fdc68a89ad01b26887c638e` / `1a9209530d7a939db1270e2f91dcef40a9f449e6` |
| VALUE membership | all 47 literal TS members below; each `MODIFY`, `VALUE`; no deviation |
| Arithmetic | 826 additions + 520 deletions = 1,346 touched text LOC; 47 logical files; binary/non-text N/A |
| Membership deviations | none; all 47 planned paths changed, no rename/create/delete |
| Trigger disposition | below 50-file and 5,000-LOC prompts; one coordinated schema/reader/copy migration; no split ruling required |
| Authority and timing | immutable denominator 47 / 3,200 and multipliers 94 / 6,400 approved before work; actual stayed below all boundaries |
| Reproduction | approved `git diff --{name-status,numstat} --find-renames=50% -z Baseline Candidate -- $valuePaths`; raw NUL-delimited parse |

| VALUE path | Action | Semantic result |
|---|---|---|
| `.tfw/conventions.md` | MODIFY | canonical coordination, activation, routing, GATEWAY and native-evidence rules |
| `.tfw/glossary.md` | MODIFY | current vocabulary routes to canonical owner; legacy labels historical |
| `.tfw/templates/status.md` | MODIFY | five-field all-or-none routing spine |
| `.tfw/templates/journal/event.md` | MODIFY | authority-owned `gate_answer` contract |
| `.tfw/templates/HL.md` | MODIFY | owner-direct/delegated coordination selection, no live roster |
| `.tfw/templates/bindings.yaml` | MODIFY | conditional stable attribution only |
| `.tfw/templates/team/profile.md` | MODIFY | attribution without current amendment grant issuance |
| `.tfw/templates/research/1_briefing.md` | MODIFY | Researcher producer/route/source/authority provenance |
| `.tfw/templates/RES.md` | MODIFY | Researcher producer/route/source/authority provenance |
| `.tfw/templates/ONB.md` | MODIFY | Executor provenance and writer-owned blocker/event/effect table |
| `.tfw/templates/RF.md` | MODIFY | Executor producer/route/source/authority provenance |
| `.tfw/templates/REVIEW.md` | MODIFY | Reviewer producer/route/source/authority provenance |
| `tools/tfw_state.py` | MODIFY | current/legacy status validation and `gate_answer` validation |
| `.tfw/adapters/codex/AGENTS.md.template` | MODIFY | Codex-native activation and vertical route mechanics |
| `AGENTS.md` | MODIFY | installed Codex managed block and removal of active mode issuance |
| `.tfw/adapters/claude-code/CLAUDE.md.template` | MODIFY | Claude-native activation/routing entry behavior |
| `CLAUDE.md` | MODIFY | installed Claude managed block and removal of active mode issuance |
| `.tfw/adapters/antigravity/tfw-rules.md.template` | MODIFY | Antigravity-native bounded activation/routing behavior |
| `.agents/rules/tfw.md` | MODIFY | exact Antigravity persistent projection |
| `.tfw/adapters/cursor/tfw.mdc.template` | MODIFY | maintained Cursor source with the same semantics |
| `.tfw/workflows/plan.md` | MODIFY | Coordinator activation, current state route and vertical dispatch |
| `.tfw/workflows/research/base.md` | MODIFY | Researcher activation, provenance and vertical returns |
| `.tfw/workflows/handoff.md` | MODIFY | Executor activation, authority answers and autonomous execution |
| `.tfw/workflows/review.md` | MODIFY | independent Reviewer activation and vertical verdict route |
| `.tfw/workflows/docs.md` | MODIFY | task-bound/current route gate and owner-direct batch boundary |
| `.tfw/workflows/knowledge.md` | MODIFY | task-bound/current route gate and owner-direct qualification boundary |
| `.tfw/workflows/release.md` | MODIFY | task-bound route gate and separate external-effect authority |
| `.tfw/workflows/init.md` | MODIFY | owner-direct init activation and first-current-status rule |
| `.tfw/workflows/update.md` | MODIFY | activation gate and authority-only active routing migration |
| `.claude/commands/tfw-plan.md` | MODIFY | exact canonical Plan projection |
| `.agents/workflows/tfw-plan.md` | MODIFY | exact canonical Plan projection |
| `.claude/commands/tfw-research.md` | MODIFY | exact canonical Research projection |
| `.agents/workflows/tfw-research.md` | MODIFY | exact canonical Research projection |
| `.claude/commands/tfw-handoff.md` | MODIFY | exact canonical Handoff projection |
| `.agents/workflows/tfw-handoff.md` | MODIFY | exact canonical Handoff projection |
| `.claude/commands/tfw-review.md` | MODIFY | exact canonical Review projection |
| `.agents/workflows/tfw-review.md` | MODIFY | exact canonical Review projection |
| `.claude/commands/tfw-docs.md` | MODIFY | exact canonical Docs projection |
| `.agents/workflows/tfw-docs.md` | MODIFY | exact canonical Docs projection |
| `.claude/commands/tfw-knowledge.md` | MODIFY | exact canonical Knowledge projection |
| `.agents/workflows/tfw-knowledge.md` | MODIFY | exact canonical Knowledge projection |
| `.claude/commands/tfw-release.md` | MODIFY | exact canonical Release projection |
| `.agents/workflows/tfw-release.md` | MODIFY | exact canonical Release projection |
| `.claude/commands/tfw-init.md` | MODIFY | exact canonical Init projection |
| `.agents/workflows/tfw-init.md` | MODIFY | exact canonical Init projection |
| `.claude/commands/tfw-update.md` | MODIFY | exact canonical Update projection |
| `.agents/workflows/tfw-update.md` | MODIFY | exact canonical Update projection |

The sole ASSURANCE change is `docs/scripts/command_entry_eval.py`: its fixtures now carry the current
routing spine and explicit owner-direct activation language. It is excluded from VALUE accounting.

### New Files

| File | Description |
|---|---|
| `evidence/coordination-scenarios.md` | status, activation, routing, gate-answer, ownership and six-edge cases |
| `evidence/provider-native.md` | independent Codex, Claude and Antigravity P0–P4 ledger |
| `evidence/copy-and-suite.txt` | copy parity, census, suite and exact accounting log |
| `evidence/EV__phase-a__explicit_coordination_gateway_and_session_identity.md` | per-AC evidence index and verdict |

### Modified Files

| File | Changes |
|---|---|
| 47 literal TS VALUE paths | canonical semantics, schemas, role templates, workflows, adapters and exact installed copies listed above |
| `docs/scripts/command_entry_eval.py` | current status fixture and activation prompts |
| `phase-a/status.md` | post-Candidate complete routing spine; lifecycle remained ONB during migration |

## 2. Key Decisions

1. Legacy absence is read-compatible, but `validate_new_status` requires all five fields; partial
   routing is invalid and cannot become permanent compatibility.
2. A principal remains optional attribution. Owner-direct activation does not create or infer an
   agent identity; current authority comes from status plus its immutable object.
3. Gates-only is the default topology. Iterative dialogue is a separate exact grant, not a mode label
   or provider capability inference.
4. `gate_answer` stays inside the existing event carrier. Scope/acceptance/architecture/authority
   changes are explicitly rejected and routed to TS revision or HL §12.
5. Provider evidence is recorded independently and honestly: Codex reached bounded P1/P2 and partial
   P3; Claude stopped at expired OAuth; Antigravity exposed only launch/process readback; no provider
   was awarded P4 or a reliability rate.

## 3. Acceptance Criteria

- [x] AC-1: one current vocabulary and zero unexplained current mode/LEAD issuers.
- [x] AC-2: closed routing spine with legacy read/current write distinction and live migration.
- [x] AC-3: vertical gates, exact iterative grant and isolated GATEWAY.
- [x] AC-4: exact skill activation and reconstructable owner-direct/delegated/continuation lineage.
- [x] AC-5: authority-owned `gate_answer` and writer-owned ONB blocker record.
- [x] AC-6: role-owned inputs, producer provenance and no distrust-only peer work.
- [x] AC-7: canonical/copy/managed parity, safe update migration, green configured suite.
- [x] AC-8: independent provider ledger with bounded attempts and explicit P0–P4 limits.
- [x] AC-9 Executor-owned portion: twelve semantic outcomes, suite and exact-path boundary pass; RF is
  complete. Independent `/tfw-review` remains the required next Role-Locked gate.

## 4. Verification

- Syntax: `python -m py_compile tools/tfw_state.py docs/scripts/command_entry_eval.py` — PASS.
- Tests: `python -m pytest tools/tests/ docs/scripts/ -q` — PASS, 14 passed in 3.84s.
- Semantic fixtures: legacy/current/partial/empty/enum/authority/iterative/gate-answer cases — PASS.
- Copy parity: 18 command copies; Codex and Claude managed blocks; Antigravity persistent copy — PASS.
- Diff quality: `git diff --check` — PASS.
- Accounting: 47 logical VALUE files, 1,346 touched text LOC, no binary/rename/deviation — PASS.

## 5. Evidence

See [EV file](evidence/EV__phase-a__explicit_coordination_gateway_and_session_identity.md) for evidence details.

Evidence verdict: 8/9 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A. The deferred portion is only the
subsequent independent REVIEW/final-output judgment required by Role Lock; accounting is VERIFIED.

## 6. Observations (out-of-scope, not modified)

No observations.

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights. The owner's instruction that all status changes return to the Coordinator was
applied as task routing, not promoted as a new project-level fact.

## 9. Diagrams

```text
owner:saubakirov
        ▲
        │ owner_gateway (Coordinator only)
        ▼
PLAN · FRATS
codex:thread:local:01a0bfdb-…
        ▲
        │ TFW gates / status / durable returns only
        ▼
EXEC · FRATS · A
codex:thread:local:01a0c3a2-…

peer / foreign Coordinator / owner / GATEWAY direct material edge → REFUSE
```

### Material handover at this return

Producer: `codex:thread:local:01a0c3a2-c742-7962-a981-369effb5ac83`, parent Coordinator
`codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf`. Inspected context is the approved Phase A
TS at `ad6042dad73aa04b9bbe9f13880c5a944e7e4f05`, Candidate
`1a9209530d7a939db1270e2f91dcef40a9f449e6`, current status, all declared sources, provider-native
attempts and local verification. Material result is the explicit coordination contract and exact
evidence above. Uncertainty is bounded to Claude authentication and Antigravity/Codex P3–P4 limits;
none is represented as reliability proof. Continue with the same task through independent
`/tfw-review`; do not recreate implementation or provider evidence from transcript.

---

*RF — TFW_20260920-223357_FRATS / Phase A: Explicit Coordination, GATEWAY and Session Identity | 2026-09-21*
