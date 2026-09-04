# RF — TFW_20260902-175227_RCFR / Phase C: Closure, Secondary Paths, and Whole-System Proof

> **Date**: 2026-09-04
> **Author**: saubakirov (via Codex)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [Phase C HL](HL__phase-c__closure_secondary_paths_and_whole_system_proof.md)
> **TS**: [TS Phase C](TS__phase-c__closure_secondary_paths_and_whole_system_proof.md)
> **Candidate commit**: `1429fe70cd77f0a9b0ff24c17b15bfe7bcc6ec86`

---

## 1. What Was Done

### New Files

| File | Description |
|------|-------------|
| `evidence/EV__phase-c__closure_secondary_paths_and_whole_system_proof.md` | Structured AC-1…AC-8 evidence and 8/8 verdict. |
| `evidence/runtime-context-whole-system.txt` | Full immutable-baseline/candidate edge, word, trajectory, and corpus audit. |
| `evidence/semantic-and-lifecycle-whole-system.txt` | Baseline/candidate source-derived records, full lifecycle routes, and rejected output-changing mutants. |
| `evidence/stale-duplicate-ledger.txt` | Current-source census, deletion dispositions, surviving-duplicate purposes, and adverse mutations. |
| `evidence/clean-receiver-secondary-routes.txt` | Four-vendor 11-command install, idempotence, repair, role, and preservation replay. |
| `evidence/verification-whole-system.txt` | Targeted/full tests, project/task diagnostics, final counts, scope, and exclusion transcript. |

### Modified Files

| File | Changes |
|------|---------|
| `.tfw/workflows/resume.md` | Replaced filename/glob discovery with ordered task/phase state, journal, lineage, REVIEW/RF, and user-decision reads. |
| `.tfw/workflows/docs.md` | Limited reads/writes to selected state/verdict, KNOWLEDGE §§1–3, and a relevance-selected convention heading while preserving triage/approval/markers. |
| `.tfw/workflows/release.md` | Added a complete ordered contract over RELEASE ranges, VERSION/config, `[Unreleased]`, DONE scope, referenced artifacts, and explicit external-effect authority. |
| `.tfw/workflows/update.md` | Made the pinned target workflow authoritative after pinning and bounded changelog/migration, owner, state-preservation, adapter, verify, briefing, and cleanup gates. |
| `.tfw/workflows/config.md` | Made config plus one registry authoritative, repaired all range addresses, and retained edit approval, verify-only reporting, adapter sync, and hard refusals. |
| `.tfw/workflows/init.md` | Routed full init versus attach/repair before discovery and retained progressive discovery, interview, templates, research, setup, adapter, verification, RF, and close gates. |
| `.claude/commands/tfw-resume.md` | Synchronized canonical Resume bytes. |
| `.claude/commands/tfw-docs.md` | Synchronized canonical Docs bytes. |
| `.claude/commands/tfw-release.md` | Synchronized canonical Release bytes. |
| `.claude/commands/tfw-update.md` | Synchronized canonical Update bytes. |
| `.claude/commands/tfw-config.md` | Synchronized canonical Config bytes. |
| `.claude/commands/tfw-init.md` | Synchronized canonical Init bytes. |
| `.agent/workflows/tfw-resume.md` | Synchronized retained singular Antigravity Resume bytes. |
| `.agent/workflows/tfw-docs.md` | Synchronized retained singular Antigravity Docs bytes. |
| `.agent/workflows/tfw-release.md` | Synchronized retained singular Antigravity Release bytes. |
| `.agent/workflows/tfw-update.md` | Synchronized retained singular Antigravity Update bytes. |
| `.agent/workflows/tfw-config.md` | Synchronized retained singular Antigravity Config bytes. |
| `.agent/workflows/tfw-init.md` | Synchronized retained singular Antigravity Init bytes. |
| `.tfw/adapters/codex/skills/tfw-resume/SKILL.md` | Reduced the Codex source skill to role/refusal checks and one canonical dispatch. |
| `.tfw/adapters/codex/skills/tfw-docs/SKILL.md` | Reduced the Codex source skill to role/refusal checks and one canonical dispatch. |
| `.tfw/adapters/codex/skills/tfw-knowledge/SKILL.md` | Removed independent common preloads while preserving Coordinator and two-WAIT refusal behavior. |
| `.tfw/adapters/codex/skills/tfw-release/SKILL.md` | Reduced the Codex source skill to role/refusal checks and one canonical dispatch. |
| `.tfw/adapters/codex/skills/tfw-update/SKILL.md` | Reduced the Codex source skill to role/refusal checks and one canonical dispatch. |
| `.tfw/adapters/codex/skills/tfw-config/SKILL.md` | Reduced the Codex source skill to role/refusal checks and one canonical dispatch. |
| `.tfw/adapters/codex/skills/tfw-init/SKILL.md` | Reduced the Codex source skill to role/refusal checks and one canonical dispatch. |
| `.agents/skills/tfw-resume/SKILL.md` | Synchronized the installed Codex Resume skill. |
| `.agents/skills/tfw-docs/SKILL.md` | Synchronized the installed Codex Docs skill. |
| `.agents/skills/tfw-knowledge/SKILL.md` | Synchronized the installed Codex Knowledge skill. |
| `.agents/skills/tfw-release/SKILL.md` | Synchronized the installed Codex Release skill. |
| `.agents/skills/tfw-update/SKILL.md` | Synchronized the installed Codex Update skill. |
| `.agents/skills/tfw-config/SKILL.md` | Synchronized the installed Codex Config skill. |
| `.agents/skills/tfw-init/SKILL.md` | Synchronized the installed Codex Init skill. |
| `.tfw/templates/status.md` | Consolidated the complete closed state form, task/phase authority sentence, quoted prose, lifecycle/terminal/UNDECLARED/timestamp rules, bounds, readers, and valid example before writes. |
| `.tfw/templates/journal/event.md` | Consolidated current event identity, closed kinds, accountability/provenance, paired transitions, refs/summary, legacy actor, correction, phase-local, and no-invented-event rules before writes. |
| `.tfw/conventions.md` | Removed duplicated form detail while retaining lifecycle authority, task/phase location, attribution, immutability, and template routing. |
| `.tfw/glossary.md` | Replaced duplicated lifecycle prose with term routes and corrected Revision to the rung-specific governing lineage. |
| `.tfw/adapters/manifest.yaml` | Deleted two phase-local comments with no runtime/tooling reader; the 4×11 mapping is unchanged. |
| `.tfw/scripts/gen_index.py` | Added a strict current-event pre-write validator separate from tolerant historical event reading. |
| `.tfw/scripts/test_gen_index.py` | Added valid and adverse pre-write coverage for summary, human, kind, time, transition, stamp, and token constraints. |
| `docs/scripts/test_runtime_context.py` | Extended the existing audit/oracle to all secondary/lifecycle/revision paths, immutable Phase C baselines, dynamic/transitive edges, corpus math, semantic records, mutants, registry and census gates. |
| `docs/scripts/test_integration.py` | Extended exact role/route/copy and clean-receiver coverage to all seven secondary commands and current project-owned Update exclusions. |

All removed prose/algorithm blocks and their surviving authority, executable test, and durable
history are enumerated in `evidence/stale-duplicate-ledger.txt`. No runtime file was added.

## 2. Key Decisions

1. Kept skills as thin role-aware routers and made each canonical workflow the sole owner of ordered reads and command algorithm, so all vendors share one runtime authority.
2. Resolved the immutable baseline with legacy and current parsers before applying candidate contracts; candidate declarations therefore cannot erase baseline full-file, repeated, transitive, or dynamic edges.
3. Added strict `validate_new_event` pre-write enforcement separately from tolerant `validate_event`, preserving historical readability while preventing new invalid immutable events.
4. Kept complete form/schema once in status/event templates and left only distinct location, transition, and attribution enforcement in conventions.
5. Recorded evidence in a separate implementation candidate commit so this RF can name an exact immutable commit without referring circularly to its own trace commit.

## 3. Acceptance Criteria

- [x] AC-1 — reproduced five primary entry totals and the 9,873 carrier anchor; emitted complete graphs and rejected omissions, duplicate/missing headings, unclassified full reads, and injected preloads.
- [x] AC-2 — preserved all seven secondary command algorithms, gates, effects, and role boundaries through thin skill dispatch and workflow-owned ordered contracts.
- [x] AC-3 — preserved complete status/event schema and compatibility while enforcing every immutable current-event bound before installation.
- [x] AC-4 — produced zero unexplained stale/readerless/competing current instructions and recorded every deletion and deliberate duplicate disposition.
- [x] AC-5 — proved exact canonical/copy/skill parity and four-vendor 11-command clean install, no-op rerun, repair, and preservation behavior.
- [x] AC-6 — extended the independent source-derived oracle through secondary commands, lifecycle closure, REVISE return, and adapter routes, with output-changing rejected mutants.
- [x] AC-7 — every changed secondary/lifecycle path is at least 30% lower, primary paths do not regress, canonical trajectory is 63.9% lower, and unique active runtime corpus is 51.7% lower.
- [x] AC-8 — configured collection/full suite, project/task diagnostics, diff, scope, and exclusions pass with only the ruled immutable RDP event.

## 4. Verification

- Lint (`python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`): PASS — 492 tests collected.
- Tests (`python -m pytest .tfw/scripts/ docs/scripts/ -q`): PASS — 491 passed, 1 skipped in 308.75s.
- Project consistency (`python .tfw/scripts/gen_index.py --check project`): PASS — project is consistent with release 2.1.0.
- Task diagnostic (`python .tfw/scripts/gen_index.py --check tasks`): expected nonzero — exactly the ruled immutable RDP summary `123>120`; no new problem.
- Scope: PASS — 41 implementation/test files, 4,109 changed LOC, 0 new runtime files, 0 `tasks/`, prior-phase, release, or VERSION changes.
- Candidate: `1429fe70cd77f0a9b0ff24c17b15bfe7bcc6ec86`.

## 5. Evidence

See [EV file](evidence/EV__phase-c__closure_secondary_paths_and_whole_system_proof.md) for evidence details.

Evidence verdict: 8/8 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `../../TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md` | 9 | style | Pre-existing immutable event summary is 123 code points against the current 120 ceiling. Phase C deliberately did not edit it; the owner-ruling exception remains the only task diagnostic problem. |

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

---

*RF — TFW_20260902-175227_RCFR / Phase C: Closure, Secondary Paths, and Whole-System Proof | 2026-09-04*

---

## 10. Return Round 1 — REVIEW `b33d534` / Coordinator ruling `7bded93`

### 10.1 What Was Done

No new runtime file or authority was introduced. The return modified exactly the three ruled
areas:

1. `docs/scripts/test_runtime_context.py` now derives every Phase C semantic field from its own
   baseline/candidate source clause. Independent expected records are comparison-only, are poisoned
   before the anti-feed production check, and reject 11 named output-changing source mutants.
2. `.tfw/scripts/gen_index.py` now applies semantic calendar/offset validation, task-relative ref
   validation, and string/one-line/ceiling summary validation only in `validate_new_event`.
   `.tfw/scripts/test_gen_index.py` covers every ruled adverse class through the actual gate and
   proves that immutable legacy journals remain readable through `read_journal`.
3. Docs and Release now declare only `Coordinator` in their canonical workflows and affected
   copies; the Release canonical/installed Codex skills agree. The source-derived role census
   enumerates the 11 manifest commands, anchors expected roles to `cf36dd6`, reconciles every
   heading/lock/skill/copy, and rejects 8 omission/duplicate/stale/conflict/parity mutants.

The six affected evidence files were append-only supplemented with current raw results. Frozen
HL/TS/REVIEW, thresholds, authority, `tasks/`, prior phases, release/version files, and all other
closed items were not changed.

### 10.2 Key Decisions

1. Kept legacy tolerance in `validate_event`/`read_journal` and placed all newly enforced bounds in
   `validate_new_event`, preserving immutable history while closing the current-write gate.
2. Derived the one-role expectation from the immutable Phase C baseline manifest, then used the
   current manifest only to enumerate the active graph; this detects a coordinated current drift as
   well as contradictions between current surfaces.
3. Preserved expected semantic records as a separate assertion oracle; production owns only
   clause-to-field derivations and never reads `PHASE_C_EXPECTED_RECORDS`.

### 10.3 Ruled Acceptance

- [x] All 66 fields across 11 Phase C semantic cases are independently source-derived; baseline,
  candidate, expected comparison, anti-feed, minimal-input refusal, and 11 mutants pass.
- [x] The current-event pre-write gate rejects 4 impossible time/offset, 4 absolute-ref, 2
  task-escape, and 4 invalid-summary cases; 3 valid relative refs and 2 immutable legacy events
  establish compatibility.
- [x] Docs/Release expose the single baseline-equivalent `Coordinator` boundary; census parity is
  clean over 11 commands, and 8 adverse declaration/copy mutations are rejected.

### 10.4 Verification

- Targeted ruled-item set: 43 passed, 266 deselected in 2.03s.
- Full affected modules: 370 passed in 300.41s.
- Full configured suite: 509 collected; 508 passed, 1 skipped in 284.34s.
- Project consistency: exit 0, release 2.1.0 consistent.
- Task diagnostic: exit 1 with exactly the already ruled immutable RDP summary `123>120`; 17
  stateless phase directories under 6 tasks remain informational.
- Runtime audit: canonical trajectory 310,485 → 112,206 (63.9% lower); unique active `.tfw` corpus
  66,436 → 32,088 (51.7% lower); every frozen per-path threshold passes.
- Frozen scope: 41 implementation/test files, 2,236 insertions + 2,244 deletions = 4,480 changed
  LOC (ceilings 44/5,000), with 0 new runtime, `tasks/`, prior-phase, or release/version files.
- Return implementation/evidence candidate: `587bc417c4a00b8f592d88f7000509bcbbc76b55`
  (17 files, 621 insertions, 92 deletions).

### 10.5 Evidence

See [EV Return Round 1](evidence/EV__phase-c__closure_secondary_paths_and_whole_system_proof.md)
for E9–E11 and the affected raw evidence.

Return evidence verdict: 3/3 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A. Current cumulative evidence
supports AC-1 through AC-8.

### 10.6 Observations (out-of-scope, not modified)

No new observations. The original §6 immutable RDP event remains the sole task diagnostic and its
existing Coordinator ruling remains in force.

### 10.7 Fact Candidates

No fact candidates.

### 10.8 Strategic Insights (Execution)

No strategic insights.

### 10.9 Diagrams

No diagrams.

---

*RF Return Round 1 — TFW_20260902-175227_RCFR / Phase C | 2026-09-04*

---

## 11. Return Round 2 — REVIEW rev2 / Coordinator ruling `dea0b9c`

### 11.1 What Was Done

No new runtime or evidence file was introduced. `.tfw/scripts/gen_index.py` now validates signed
offset components on their original text before `datetime.fromisoformat` can normalize overflowed
minutes, and rejects generic URI-scheme syntax in current-event refs after the existing
root/drive/UNC check. `.tfw/scripts/test_gen_index.py` adds adverse, valid-boundary, pre-install,
and legacy-reader partitions. EV and the validation transcript were append-only supplemented.

Semantic production, role census/parity, runtime thresholds, authority, scope definition, frozen
HL/TS/REVIEW, `tasks/`, prior phases, and release/version files were not modified.

### 11.2 Key Decisions

1. Validate numeric offset hours/minutes before calling Python's semantic parser, because that
   parser normalizes `+05:60` and `+05:99` rather than rejecting their source structure.
2. Use the standard scheme prefix grammar `[A-Za-z][A-Za-z0-9+.-]*:` and retain the earlier
   Windows-drive check first, so both categories are refused with accurate diagnostics.
3. Keep both additions exclusively in `validate_new_event`; immutable historical events continue
   through unchanged `validate_event`/`read_journal` compatibility.

### 11.3 Ruled Acceptance

- [x] `+05:60`, `+05:99`, and `-05:60` are refused before installation; `Z`, `+00:00`, `+05:59`,
  `+14:00`, and `-14:00` remain valid, and the existing over-±14:00 refusal remains intact.
- [x] `https://`, `file://`, `git+ssh://`, and `urn:` refs are refused as URI schemes while the
  three existing normalized task-relative filesystem forms remain valid.
- [x] Three adverse legacy events remain readable without any new pre-write-only diagnostic.

### 11.4 Verification

- Focused actual-gate/legacy set: 30 passed, 162 deselected in 0.29s.
- Full affected module: 192 passed in 3.86s.
- Full configured suite: 521 collected; 520 passed, 1 skipped in 308.75s.
- Direct gate replay: both overflowed-minute examples and three URI schemes return their exact
  refusal; `Z` and `±14:00` return `[]`.
- Project consistency: exit 0. Task diagnostic: exit 1 only for the already ruled immutable RDP
  summary `123>120`; 17 stateless phase directories under 6 tasks remain informational.
- Return implementation scope: 2 files, 68 insertions + 13 deletions = 81 changed LOC.
- Cumulative frozen scope: 41 implementation/test files, 2,291 insertions + 2,244 deletions = 4,535
  changed LOC against ceilings 44/5,000; zero `tasks/`, prior-phase, release/version, or new runtime
  files.
- Implementation/evidence candidate: `25d0e89afe48144c79c11324ff09d300b76dd6e9`
  (4 files, 168 insertions, 13 deletions).

### 11.5 Evidence

See [EV Return Round 2](evidence/EV__phase-c__closure_secondary_paths_and_whole_system_proof.md)
for E12 and the affected raw verification transcript.

Return Round 2 evidence verdict: 1/1 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A. Current cumulative
evidence supports AC-1 through AC-8.

### 11.6 Observations (out-of-scope, not modified)

No new observations. The original §6 immutable RDP event remains the sole task diagnostic and its
existing Coordinator ruling remains in force.

### 11.7 Fact Candidates

No fact candidates.

### 11.8 Strategic Insights (Execution)

No strategic insights.

### 11.9 Diagrams

No diagrams.

---

*RF Return Round 2 — TFW_20260902-175227_RCFR / Phase C | 2026-09-04*
