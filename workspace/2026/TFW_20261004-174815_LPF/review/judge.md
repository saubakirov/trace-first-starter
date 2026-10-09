# Judge — "Is the accepted result fit and sufficiently established?"
> **Mindset:** Judge. Apply the evidence from Verify in `VALUE → ASSURANCE → TRACE` order.
> **Test:** "Would I defend this acceptance decision for the named purpose, harm and authority?"
> Verify findings: [verify.md](verify.md) at `988c9ff2c9bec5633b88a1a80f086170b1afb124`

## Status and Materiality

**Status vocabulary:** `✅` holds · `❌` finding · `⚪ N/A` does not apply with a stated reason.
Every `❌` cites a Verify finding with the complete item contract. A row, criterion, discrepancy,
citation, count or process record never changes the verdict by itself. Blocking requires an affected
accepted claim or authority, concrete harm and material consequence. Safety/security, human
acceptance authority and accepted-result identity are non-waivable subjects.

## 1. VALUE

| Subject | Status | Evidence / finding IDs |
|---|---|---|
| Purpose and approved value | ✅ | Purpose Check below |
| Domain behavior and acceptance criteria | ✅ | V4–V7, V10: AC-1…AC-11 and DoD 1–10 hold on the Candidate; the live effects of AC-4 and AC-6 are DEFERRED by the approved TS to the next Daily turn and the next receiver update |
| Architecture and HL principles | ✅ | P1 one home: V4, V9; P2 observation over attachment: W3 template and this task's EV (V9, Evidence Verification); P3 verify by repeating: every material claim in V1–V10 was re-established without the Executor's working material (DoF 1 not met); P4: V6; P5: one new file (the guide), changed workflows shrink, no code, test, command, registry, root or dependency (V4, V6); P6: guide §4–§5 (V5); P7: this repository cleaned and this task's trace compliant (V6, V9). O2 is a non-material design observation |
| Safety and security | ✅ | V9: no machine path, address, private name or secret in the task folder or the Candidate's added lines; W2.2 states that removal follows no link; install/update surfaces intact — markers 10 → 10, block parity, YAML values and ownership markers unchanged (V4, V6) |
| Human acceptance authority and reserved effects | ✅ | V3: owner approval of TS, 33 / 1,000 and option A at `9216218d`; ruling 1 prospective and inside the change-authority rule; no `VERSION`, tag, push or remote change; final acceptance remains the owner's |

### Purpose Check

Master HL at its Contract Baseline (`efc915a9`) §1: "The evidence folder is a registry of what was
verified, how, and what was seen; a reviewer repeats the check instead of trusting bytes. A comment
exists only where it carries value for the reader of that file … Repositories stop growing from junk,
searches find decisions instead of dumps, and agents spend tokens on meaning." North Star NS1: another
authorized person or agent can "inspect its material grounds and current result … and continue
without rebuilding the original conversation"; NS2.4: "do not archive everything".

Harm at stake: receiving projects accumulate hundreds of megabytes of evidence and Daily leftovers
and comment correspondence that goes stale and costs tokens (HL §2.1, S1, S6); the opposite harm is
that removing bytes destroys inspectability (NS1, NS2.2). The Candidate serves the first without
causing the second: `evidence/` holds observed deciding values with their method and Candidate, and
this review established every material claim by repetition with no working material from another
role.

1. **Excess and adjacency** — The duplicate Coordinator row fix, the two chatter removals (W7) and
   the TS-template row deletion (ruling 1) sit inside files the task changes, are owner-visible in
   the approved TS or the ruling, shrink words and serve C2/C5; nothing the HL excludes is
   delivered. The §1 phrase "TFW's machine-local folder" against the system temporary directory is
   surface tension only: frozen C1 admits "the system temporary directory as research selects", and
   research selected it on trial evidence (V10).
2. **Deferral confession** — The 41 restatements, commit reduction and the release stay with the
   owner-agreed separate task, the HL's exclusions and the owner; nothing assigned elsewhere is
   shipped, and nothing owed here is pushed out (E5/E8 are deferred by the TS to events after
   release).
3. **Materiality** — No observed issue harms the approved value. O2 can cost rework on one machine
   but cannot lose accepted value, because no claim may rest on working material and observations
   enter EV when made.

| Outcome | Status | Required finding and route |
|---|---|---|
| Aligned | ✅ | HL §1 registry/repetition/comment clauses and NS1 inspectability; harm protected: repository bloat and stale correspondence, without loss of material grounds |

## 2. ASSURANCE

| Subject | Status | Evidence / finding IDs |
|---|---|---|
| Evidence exists | ✅ | EV E1–E13 and E-accounting; RF §4 |
| Evidence applies to accepted subject, Candidate/revision, environment, oracle/authority and dependencies | ✅ | V2: VALUE at HEAD and in the working tree equals the Candidate; same machine and toolchain; Baseline comparisons on identical inputs (V7) |
| Evidence is sufficient for each material claim and risk | ✅ | every material claim independently repeated (V1–V10); limits: AC-4/AC-6 live effects deferred by design; pytest 9.0.2 against the `<9` pin |
| Permanent guards demonstrate relevant counterfactual detection | ⚪ | no permanent guard is added or claimed; G1 labelled control, G2–G4 temporary diagnostics, G5 governance only |

## 3. TRACE

| Subject | Status | Evidence / finding IDs |
|---|---|---|
| Governing authority and independent role lineage | ✅ | complete spine; dispatches 71eb, 2d7e, 34fa, 15bd; distinct Researcher, Executor and Reviewer units; Executor held during review |
| Accepted-result identity and immutable accounting | ✅ | V1, V2: Candidate `0863d299`, 34-path selector, 258 + 411 = 669, 32 ≤ 33, reachable, exact name sets |
| Reproducibility and citation integrity needed for material claims | ✅ | EV commands reproduce (S1–S8); all HL §7.2 and ONB §7 citations resolve and match (Knowledge Citations Verified); O1 is a self-referencing gate, not a leak |
| Authorized continuation, item completion routes and dispositions | ✅ | O1–O4 observations with owners; Coordinator-held closing items listed in Finding Rulings |
| Record-only observations | ✅ | O1, O3, O4 need no product work; O3 completes at Closing step 6 |

## 4. Finding Rulings

| ID | Class | Subject / affected claim or authority | Fact + oracle | Harm and material consequence | Owner / completion | Route / rung | Candidate effect | Disposition |
|---|---|---|---|---|---|---|---|---|
| O1 | TRACE | AC-9 literal leak gate / C12 | the TS's own lines 195, 283, 349 contain the searched word, so the gate cannot return nothing; broadened greps find no leak (V9) | none; the protected object is intact | Coordinator; none required | observation | unchanged | not material |
| O2 | VALUE | W2.2 folder granularity / C1 | `tfw/<task or Daily record ID>/` is one folder for every role of a task on one machine; whole-folder removal by one role can delete another role's retained or in-flight material (verify.md, Candidate Findings O2) | possible rework for another role; no accepted value can be lost (C3; rows written when observed); wording owner-approved (S10) | owner, if a later rule task is wanted; none for this task | observation | unchanged | not material |
| O3 | TRACE | Coordinator's own helper files / C7, Closing step 6 | four `lpf_*.py` helpers in the session scratchpad root, outside the project but not under `tfw/<ID>/` | none; outside the project | Coordinator; removal recorded at close | Closing step 6 | unchanged | not material |
| O4 | TRACE | glossary `Evidence Status Vocabulary` authority / out of scope | cites heading `Evidence Table`, absent from the EV template at Baseline and Candidate | a missing-heading reference; pre-existing | Coordinator for routing; none here | observation | unchanged | not material |

Coordinator-held closing items, not Reviewer findings: the `[Unreleased]` entry's task attribution
(Closing step 4); the F43 ↔ C5 knowledge tension (ONB §7 row 29) together with the D53 contradiction
below for `/tfw-docs` and `/tfw-knowledge`; RF §6 observations 1 and 2.

## 5. Aggregate Verdict

**Verdict:** ✅ APPROVE

**Reason:** VALUE — the Candidate ships the owner-approved W1–W8 verbatim in their places and serves
HL §1 and NS1 without losing inspectability (Purpose Check; V4, V5, V8); the cleanup removed no
program-read line and changed no behavior (V6, V7); safety and owner authority hold (V3, V9).
ASSURANCE — every material claim was repeated independently on the Candidate (V1–V10).
TRACE — identity and accounting replay exactly (V1, V2); O1–O4 are non-material observations that
change neither acceptance nor the next authorized act.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | Accepted claim | Contradiction / effect |
|---|---|---|---|
| K1 | D53 — EV template "with environment header, per-AC evidence table, verdict summary, optional attachments index" | C2: `evidence/` holds only the EV registry; the Attachments section is removed (W2.4, W3) | D53's template description is superseded; the folder and EV stay mandatory as D53 decided. Effect: a successor or replacement entry through the Coordinator's `/tfw-docs` at close; no product change |

## Checkpoint

**Self-check:**
- [x] Judged VALUE, then ASSURANCE, then TRACE, including every mandatory floor?
- [x] Supported every status with Verify evidence and every N/A with a reason?
- [x] Answered Purpose against Contract Baseline + North Star with a relevant clause and concrete harm?
- [x] Kept evidence existence, applicability and sufficiency distinct?
- [x] Gave every verdict-relevant item the complete finding contract, class, route and Candidate effect?
- [x] Let highest authority sequence the next act without reclassifying mixed items?
- [x] Derived exactly one verdict without using checklist, discrepancy, file, test or artifact volume as a quality objective?

Stage complete: YES
