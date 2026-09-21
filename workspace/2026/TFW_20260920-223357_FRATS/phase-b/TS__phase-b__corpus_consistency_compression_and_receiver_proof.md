# TS — TFW_20260920-223357_FRATS / Phase B: Corpus Consistency, Compression and Receiver Proof

> **Date**: 2026-09-21
> **Author**: Codex (Coordinator), acting as `saubakirov`
> **Status**: 🟡 DRAFT — exact TS and denominator await owner approval
> **Master HL**: [Framework Refactoring and Agent-Team Simplification](../HL-TFW_20260920-223357_FRATS.md)
> **Phase HL**: [Phase B derivation](HL__phase-b__corpus_consistency_compression_and_receiver_proof.md)
> **Baseline**: accepted Phase A Candidate `1a9209530d7a939db1270e2f91dcef40a9f449e6`

---

## 1. Objective

Reduce the active TFW instruction corpus to the smallest justified, internally consistent form that
still preserves all accepted behavior. The result must be measurable, source-derived, exact across
canonical and provider surfaces, compatible with historical artifacts, and demonstrably useful to
four real receiver projects without changing them.

## 2. Scope

### In scope

- Historical RCFR replay and a current, reproducible reader-exposure/unique-corpus successor with an
  explicit comparison bridge.
- A complete in-scope instruction census: normative owner, actual reader, delivery sites, duplicate,
  contradiction, stale instruction, readerless bound and exact disposition.
- Semantics-first subtraction across the 47-path VALUE selector.
- One filename issuance grammar across artifact type, topology, revision and append behavior, with
  historical compatibility reads.
- Exact canonical/copy/managed-block parity for all surviving manifest commands and adapters.
- Update/init/config consistency for preservation, installation and migration behavior.
- Existing assurance checks and exact Baseline→Candidate accounting.
- Read-only replay in Helpdesk, SenseLab/KazNPU AI Lab, AFD and RYC.
- A sourced D75 correction package routed through `/tfw-docs` during closing.

### Out of scope

- Receiver mutation or release effects of any kind.
- New execution/coordination architecture, provider reliability trials or deferred `FRATS-D01` work.
- Historical artifact renaming or normalization.
- A percentage/word target, synthetic edits to meet a number, or restoration of the retired large
  audit file without an independently justified maintained reader.
- New permanent tests solely to satisfy this task.
- Executor edits to `KNOWLEDGE.md`.

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1–P6 | Accepted Phase A autonomy, routing, activation and role boundaries | AC-3, AC-4, AC-5 | Six-edge replay shows no change to activation, authority, return or dialogue behavior. |
| P7 | One truth, one owner, one reader path | AC-2, AC-4 | Every surviving instruction has one normative owner and named reader/delivery path. |
| P8 | Subtraction without semantic loss | AC-1, AC-3, AC-8 | Counts report the result; six-edge behavior selects what may leave. |
| P9 | Structural enforcement | AC-2, AC-3, AC-5 | Filename, copy and refusal mismatches are machine- or trace-visible. |
| P10 | Native evidence before provider claims | AC-5 | Adapter claims stop at copy/native-entry behavior; Phase A P3/P4 limits remain limits. |
| P11 | Independent review remains independent | AC-9 | Separate Reviewer evaluates Candidate, evidence and any D75 follow-up. |
| P12 | Receivers are evidence, not fixtures to rewrite | AC-6 | Four epoch-bound read-only snapshots; mutation is a failure. |
| P13 | No receiver runtime tax | AC-1, AC-4, AC-6 | File-based successor and current adapters only; no service or restored giant oracle. |

## 4. Affected Files and Value-Bearing Accounting

Every path below exists at the baseline. Listed paths form the immutable planned denominator even
when the census proves an individual path already correct and it therefore stays zero-diff. No file
is changed merely to satisfy the count.

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/README.md` | MODIFY | `VALUE` | Consolidate shared semantics and remove duplicate, contradictory, stale or readerless prose. |
| `.tfw/templates/{HL,TS,RES,ONB,RF,REVIEW}.md`, `.tfw/templates/evidence/EV.md` | MODIFY | `VALUE` | Minimal complete forms and one exact new-artifact filename grammar. |
| `.tfw/workflows/{plan,research/base,handoff,review,docs,knowledge,release,update,config,init}.md` | MODIFY | `VALUE` | Algorithmic bounded reads, exact producers/consumers and consistent migration behavior. |
| `.claude/commands/tfw-{command}.md`, `.agents/workflows/tfw-{command}.md` for all ten commands | MODIFY | `VALUE` | Exact manifest-derived copies of canonical workflows. |
| `.tfw/adapters/{codex/AGENTS.md.template,claude-code/CLAUDE.md.template,antigravity/tfw-rules.md.template,cursor/tfw.mdc.template}` plus `AGENTS.md`, `CLAUDE.md`, `.agents/rules/tfw.md` | MODIFY | `VALUE` | Persistent native entry behavior and managed-copy parity without duplicated core semantics. |
| `docs/scripts/command_entry_eval.py`, `docs/scripts/test_integration.py`, `docs/scripts/test_gen_docs.py` | MODIFY | `ASSURANCE` | Existing readers may be updated only where changed production behavior requires it; no new test surface. |
| `tools/tests/test_git_blob_sizes.py` | NONE | `ASSURANCE` | Existing required boundary runs unchanged. |
| Phase-B HL/TS/status/journal, EV/RF/REVIEW and bounded evidence files | CREATE/MODIFY | `TRACE` | Governance, reproducible evidence and independent acceptance; excluded from VALUE denominator. |
| Four receiver repositories and `KNOWLEDGE.md` during execution | NONE | `TRACE` input | Read-only evidence; D75 correction is a later `/tfw-docs` effect, not Executor VALUE. |

### Literal VALUE selector (47 paths)

```powershell
$valuePaths = @(
  '.tfw/conventions.md'
  '.tfw/glossary.md'
  '.tfw/README.md'
  '.tfw/templates/HL.md'
  '.tfw/templates/TS.md'
  '.tfw/templates/RES.md'
  '.tfw/templates/ONB.md'
  '.tfw/templates/RF.md'
  '.tfw/templates/REVIEW.md'
  '.tfw/templates/evidence/EV.md'
  '.tfw/workflows/plan.md'
  '.tfw/workflows/research/base.md'
  '.tfw/workflows/handoff.md'
  '.tfw/workflows/review.md'
  '.tfw/workflows/docs.md'
  '.tfw/workflows/knowledge.md'
  '.tfw/workflows/release.md'
  '.tfw/workflows/update.md'
  '.tfw/workflows/config.md'
  '.tfw/workflows/init.md'
  '.tfw/adapters/codex/AGENTS.md.template'
  'AGENTS.md'
  '.tfw/adapters/claude-code/CLAUDE.md.template'
  'CLAUDE.md'
  '.tfw/adapters/antigravity/tfw-rules.md.template'
  '.agents/rules/tfw.md'
  '.tfw/adapters/cursor/tfw.mdc.template'
  '.claude/commands/tfw-plan.md'
  '.agents/workflows/tfw-plan.md'
  '.claude/commands/tfw-research.md'
  '.agents/workflows/tfw-research.md'
  '.claude/commands/tfw-handoff.md'
  '.agents/workflows/tfw-handoff.md'
  '.claude/commands/tfw-review.md'
  '.agents/workflows/tfw-review.md'
  '.claude/commands/tfw-docs.md'
  '.agents/workflows/tfw-docs.md'
  '.claude/commands/tfw-knowledge.md'
  '.agents/workflows/tfw-knowledge.md'
  '.claude/commands/tfw-release.md'
  '.agents/workflows/tfw-release.md'
  '.claude/commands/tfw-update.md'
  '.agents/workflows/tfw-update.md'
  '.claude/commands/tfw-config.md'
  '.agents/workflows/tfw-config.md'
  '.claude/commands/tfw-init.md'
  '.agents/workflows/tfw-init.md'
)
```

### Scope Contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | Literal 47-path `$valuePaths` array above; whole-file membership, no freehand exclusions. |
| Baseline / selector source | `1a9209530d7a939db1270e2f91dcef40a9f449e6`; this TS at its future owner-approval commit. |
| Candidate rule | First tested Executor commit containing required VALUE and necessary existing ASSURANCE changes, before EV/RF/REVIEW/final transition. TRACE-only later writes do not move it; later VALUE requires a new Candidate and recomputation. |
| Logical VALUE files | 47 planned; rename = one. Already-compliant listed paths may be zero-diff and remain in the immutable denominator. |
| Touched text LOC | 1,200 additions + 3,600 deletions = 4,800 planned; numeric `numstat` fields; binary/non-text = per-file N/A. This is a forecast, not a reduction quota. |
| Triggers / disposition | Config prompts at 50 VALUE files or 5,000 touched text LOC. The 47/4,800 plan remains one phase because canonical ownership, consumers and projections must change coherently. Crossing either prompt requires a prospective cause/cost/assurance/split ruling before added work. |
| Multiplier / authority | Immutable plan 47 files / 4,800 LOC; owner decision required at 94 files or 9,600 LOC, from any planned-zero class, or for a change to Goal, Value, outputs, AC, DoF, phase/ownership, architecture, target, interfaces, data, security, trust or authority. Below both multipliers, the Coordinator may admit only a necessary constituent with those invariants fixed and a pre-work ruling. |
| Approval epoch / failure | Prospective owner approval of this exact TS and denominator; missing/mutable/mismatched/late = BLOCKED; metric-only N/A; unresolved phase attribution = INVALID; DEFERRED is non-terminal. |

```powershell
git diff --name-status --find-renames=50% -z 1a9209530d7a939db1270e2f91dcef40a9f449e6 <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z 1a9209530d7a939db1270e2f91dcef40a9f449e6 <CANDIDATE_SHA> -- $valuePaths
```

### Prospective scope rulings

None. The plan stays below both configured decomposition prompts. Its paths are one coupled
instruction product: canonical rule, role-local consumer, generated provider copies and native
entry surfaces. Splitting them would knowingly create a period in which readers disagree.

No task-local M1–M6 hard constraint is introduced. Read-only receivers, historical preservation and
Role Lock are existing acceptance/authority boundaries.

**Actions (not budget dimensions):** 47 MODIFY-or-zero-diff `VALUE`; up to 3 existing MODIFY
`ASSURANCE`; one unchanged blob-size `ASSURANCE`; no planned VALUE CREATE/DELETE/RENAME.
**Immutable owner-approved denominator:** 47 VALUE files and 4,800 touched text LOC; never ratchets.

## 5. Acceptance Criteria

### AC-1: Reproducible historical and current measurement

- [ ] Reproduce the RCFR trajectory 310,485→112,206 and active corpus 66,436→32,088 from immutable
  commit `25d0e89afe48144c79c11324ff09d300b76dd6e9`, without restoring its deleted audit to the live tree.
- [ ] Define a current ten-command reader-exposure and unique-active-corpus selector from manifest,
  persistent entries and actual read contracts at baseline `1a920953…`; record exact command,
  inclusions, exclusions, deduplication and tool versions.
- [ ] Measure baseline and Candidate with that identical selector and report exact before/after
  values. Keep the historical replay and successor series separate; explain the proven bridge and
  every reason exact comparison is impossible.
- [ ] Any maintained successor code has a named current reader and cost/value justification;
  otherwise the measurement remains bounded evidence rather than a permanent runtime/test.

Gate: Reviewer can rerun both measurement paths from immutable refs and reproduce the reported
numbers or the exact documented environment limit.
Evidence: `evidence/current-corpus-and-exposure.txt`.

### AC-2: Complete instruction and filename census [depends: AC-1]

- [ ] Every active instruction in the VALUE selector has a normative owner, actual reader, delivery
  path and one disposition: preserve, consolidate, remove or repair, with reason.
- [ ] Every detected duplicate, contradiction, stale instruction and readerless bound appears once
  in the ledger; no vague “cleanup” or undispositioned search result remains.
- [ ] New artifacts use exactly one grammar per artifact type and topology, including master,
  single-phase, phase-scoped, revision and append cases. Plan, Handoff, Review and templates agree.
- [ ] Historical filename variants remain readable and untouched but cannot be used as current
  issuance precedent.

Gate: source→reader→delivery matrix plus positive and historical-compatibility filename fixtures.
Evidence: `evidence/instruction-disposition-ledger.md`.

### AC-3: Six-edge semantic preservation [depends: AC-2]

For every removal or consolidation, the ledger maps source, destination, authority, carrier,
recovery and consequence for all applicable edges: activation, authority, evidence, recovery,
continuation and exception.

- [ ] Each edge has at least one positive and one material negative replay against the Phase A
  Candidate, and all outcomes remain equivalent or become strictly less ambiguous.
- [ ] No text is removed because it is long, repeated-looking or expensive before its owner/readers
  and edge consequences are known.
- [ ] Phase A routing spine, owner boundary, activation provenance, gate ownership, independent
  review and provider-limit behavior remain intact.
- [ ] Any non-equivalent outcome stops the related subtraction and is reported, not compensated by
  more prose or an invented mechanism.

Gate: Reviewer can trace every semantic subtraction to the ledger and replay outcomes.
Evidence: `evidence/six-edge-replay.md`.

### AC-4: Maximum justified subtraction and canonical ownership [depends: AC-2, AC-3]

- [ ] Shared provider-neutral rules have one canonical owner; workflows state only algorithmic
  role-local actions, templates only required form/fields, and adapters only native mechanics.
- [ ] Duplicated explanatory prose leaves all secondary surfaces when an exact authoritative link
  and bounded read contract preserve behavior.
- [ ] Every preserved repetition states why local availability, failure recovery or provider entry
  requires it and names its owner.
- [ ] Candidate reports gross additions, deletions and net change but passes or fails on behavioral
  evidence, never on a percentage or word threshold.
- [ ] No new runtime, registry, generic backlog, mandatory artifact or large restored oracle replaces
  prose that was removed.

Gate: disposition ledger closes every census item and the six-edge oracle closes every subtraction.
Evidence: AC-1 through AC-3 evidence plus exact Candidate accounting.

### AC-5: Adapter, command and migration consistency [depends: AC-2, AC-3, AC-4]

- [ ] All ten manifest commands resolve to their canonical workflows; every changed Claude and
  Antigravity command copy is byte-identical to its canonical source.
- [ ] Codex skill routers remain thin source/installed pairs; they change only if a concrete reader
  defect requires a prospective VALUE ruling because they are outside the selector.
- [ ] Codex, Claude and Antigravity managed persistent targets match their sources while preserving
  foreign/project-owned content; Cursor source expresses the same semantics without claiming a
  local installed target.
- [ ] Update, init and config are mutually consistent, idempotent where configured, preserve custom
  content and never defer same-phase synchronization to “later cleanup”.
- [ ] Phase A native evidence remains bounded as recorded; no adapter wording upgrades P0–P4 claims.

Gate: manifest-derived copy checks, managed-block comparison and update/init/config preservation
fixtures all pass from one Candidate.
Evidence: `evidence/adapter-and-suite.txt`.

### AC-6: Four-receiver read-only replay [depends: AC-4, AC-5]

At one recorded verification epoch inspect:

- `D:\projects\research\helpdesk`;
- `D:\projects\research\kaznpu-ai-lab` (SenseLab / KazNPU AI Lab);
- `D:\projects\research\ai-first-devices` (AFD); and
- `D:\projects\research\research-yandex-cloud` (RYC).

- [ ] Record each repository's resolved path, HEAD, branch, worktree state, installed TFW/version or
  latest receipt, and which local customizations constrain interpretation.
- [ ] Replay current versus proposed source behavior without install/update/write; state exactly what
  Phase B fixes, preserves, cannot infer and would require separate owner action.
- [ ] Do not stage, commit, normalize, generate into or otherwise mutate any receiver tree. A receiver
  changing independently during inspection creates a new epoch rather than a merged observation.
- [ ] Receiver-specific facts remain bounded to their project and epoch; no field failure becomes a
  universal provider/methodology claim.

Gate: before/after Git status and immutable snapshots prove no task-caused receiver mutation.
Evidence: `evidence/receiver-replay.md`.

### AC-7: Existing assurance and exact accounting [depends: AC-5, AC-6]

- [ ] Existing configured framework checks pass, including documentation generation/integration and
  Git blob-size boundary. Any unrelated existing failure is bounded with baseline evidence.
- [ ] No new permanent test is added solely for coverage count or evidence theatre; changes to the
  three listed ASSURANCE readers correspond to an actual changed production contract.
- [ ] NUL-safe Baseline→Candidate accounting uses the literal 47-path selector and reports changed,
  zero-diff and any prospective-ruling path separately.
- [ ] No VALUE path outside the selector changes without an authorized prospective ruling; no
  receiver or historical artifact changes.

Gate: exact commands, versions, exits, diffs and limits are captured from the tested Candidate.
Evidence: `evidence/adapter-and-suite.txt` and required EV.

### AC-8: Owner-readable outcome and D75 correction route [depends: AC-1–AC-7]

- [ ] RF shows historical replay, current baseline, Candidate result, gross/net change, practical
  benefit, preserved costs, limitations and remaining owner decisions in one comparable account.
- [ ] RF explains that 112,206 is source-reproduced while current D75 says 112,536, and supplies the
  exact citations and correction text without the Executor editing `KNOWLEDGE.md`.
- [ ] Accepted correction is routed through `/tfw-docs` during closing; any resulting knowledge
  change receives bounded follow-up by the same independent Reviewer before `DONE`.
- [ ] No size claim substitutes for an explanation of reader behavior, and no successor number is
  presented as the historical denominator.

Gate: owner can decide remaining work without reconstructing the task from chats or raw logs.
Evidence: RF plus AC-1/AC-6 evidence and closing trace.

### AC-9: Independent acceptance and terminal lineage [depends: AC-1–AC-8]

- [ ] Executor produces one tested Candidate, EV and RF with exact Baseline→Candidate lineage.
- [ ] A separate `/tfw-review` unit evaluates purpose, every AC, six-edge preservation, receiver
  immutability and measurement comparability without participating in implementation dialogue.
- [ ] Any accepted `/tfw-docs` correction is captured as a later authorized effect and receives the
  same Reviewer's bounded follow-up; otherwise the original verdict remains explicitly conditional.
- [ ] Coordinator records applicable/N/A downstream routes and only then closes Phase B and master
  task. No release, tag, push, publication or deployment is inferred.

Gate: REVIEW is APPROVE, or APPROVE_WITH_ACTIONS with every blocking action closed, and terminal
status/journal references resolve to the accepted commits.
Evidence: required EV, RF, REVIEW and closing journal.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-b__corpus_consistency_compression_and_receiver_proof.md` | Required per-AC environment, evidence and verdict index. |
| `evidence/current-corpus-and-exposure.txt` | Historical replay, successor selector, baseline/Candidate outputs and comparison limits. |
| `evidence/instruction-disposition-ledger.md` | Source/reader/delivery/filename census and one disposition per finding. |
| `evidence/six-edge-replay.md` | Per-subtraction semantic mapping and positive/material-negative outcomes. |
| `evidence/adapter-and-suite.txt` | Manifest/copy/managed-block checks, configured suite and exact accounting. |
| `evidence/receiver-replay.md` | Epoch-bound read-only Helpdesk, SenseLab, AFD and RYC results. |

## 6. Technical Guidance

- Derive the current metric from the manifest and actual workflow read contracts rather than a
  hand-maintained list; keep the selector itself in evidence so another agent can rerun it.
- Read the deleted historical audit from its immutable Git object or worktree-isolated historical
  checkout. Do not resurrect it in the Candidate.
- Start with the highest-repeat owners: principal/identity selection, full-file purpose reads and
  duplicated form prose. Keep a repetition only when the ledger proves local recovery value.
- Treat filename grammar as producer/consumer behavior, not cosmetic naming. Cover master,
  single-phase, phase-scoped, revised and append flows at Plan/Handoff/Review boundaries.
- Generate installed workflow copies from canonical sources and validate all ten commands; never
  hand-edit a projection into a second implementation.
- Use read-only Git and file inspection in receiver projects. Evidence files live only in this task.
- Keep `KNOWLEDGE.md` out of the Executor Candidate. RF provides the exact D75 source correction;
  the Coordinator invokes the owning documentation workflow only after review.

## 7. Definition of Failure

- ❌ A reduction percentage, word target or file count decides what text leaves.
- ❌ A removed instruction weakens activation, authority, evidence, recovery, continuation or exception behavior.
- ❌ Historical and successor metrics are combined without their different selectors and bridge limits.
- ❌ A census finding lacks one disposition, reason, normative owner or actual reader conclusion.
- ❌ More than one filename grammar remains valid for new issuance, or history is renamed to look consistent.
- ❌ Canonical workflows, installed copies or managed persistent surfaces diverge at Candidate.
- ❌ Same-phase synchronization is deferred to later cleanup.
- ❌ A receiver repository is modified or a moving receiver state is silently merged into one observation.
- ❌ The deleted large audit is restored, or a new permanent test/runtime exists only to prove this task.
- ❌ Executor edits `KNOWLEDGE.md` or silently corrects D75 outside its owning workflow.
- ❌ Phase A provider limits are upgraded, composed or re-tested as a substitute for corpus proof.
- ❌ A VALUE path outside the selector changes without a prospective ruling, or accounting uses a moving baseline.

**On failure:** stop the affected edit, preserve the exact source and evidence, record the failed AC in
the owned artifact and return it through the Phase B Coordinator. Architecture, denominator or
authority changes require prospective approval; they are not repaired through informal dialogue.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| The 4,800-LOC forecast becomes a hidden quota. | Acceptance explicitly ignores achieved size and evaluates dispositions plus six-edge behavior. |
| Forty-seven paths hide unrelated edits. | Literal selector, per-path ledger and exact Candidate accounting with zero-diff reporting. |
| A measurement script becomes a new maintenance burden. | Prefer reproducible task evidence; permanent code requires a named reader and value ruling. |
| Receiver states drift during the run. | Capture Git/receipt epoch at start and end; split later changes into a new observation. |
| D75 remains known-wrong after implementation approval. | Exact RF correction package, `/tfw-docs` closing route and bounded Reviewer follow-up before DONE. |
| Compression makes adapters depend on unavailable shared context. | Adapter entry replay plus preserved local recovery instructions where the ledger proves necessity. |

## 9. Cross-Phase Modifications

| File / concern | Prior owner | Phase-B rule |
|---|---|---|
| Phase A coordination semantics | Phase A Candidate `1a920953…` | May compress representation only; all six behaviors and provider limits remain equivalent. |
| Canonical workflows/templates/adapters | Phase A and current product | One Phase-B Candidate updates owner and projections together. |
| `KNOWLEDGE.md` D75 | `/tfw-docs` / knowledge lifecycle | Read-only to Executor; exact correction routed after review and independently followed up. |
| Receiver installations | Separate project owners | Evidence only; no mutation, upgrade or cleanup in this phase. |

---

*TS — TFW_20260920-223357_FRATS / Phase B: Corpus Consistency, Compression and Receiver Proof | 2026-09-21*
