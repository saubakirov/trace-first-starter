# Judge — "Is the accepted result fit and sufficiently established?"
> **Mindset:** Judge. Apply the evidence from Verify in `VALUE → ASSURANCE → TRACE` order.
> **Test:** "Would I defend this acceptance decision for the named purpose, harm and authority?"
> Verify findings: [verify.md](verify.md) at `de5af646`
> Contract baseline: master HL frozen at `975fed5fac6f2ed2ae47af646907636a67b3dc82` (first freeze `c4044d2e`, re-freezes `49703481` and `975fed5f` with owner-approved §12 A1–A4); Project North Star `.tfw/README.md` NS1–NS3

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
| Domain behavior and acceptance criteria | ✅ | AC-1 V1–V9; AC-2 V6–V8 with named limits; AC-3 V16; AC-4 V11–V13; AC-5 V14; AC-6 V15; AC-7 V17 and V1/V10; AC-8 V18 |
| Architecture and HL principles | ✅ | principle 1 (as amended by A1): the clone holds exactly `.tfw`, the directory structure and the top-level files (V1); 2: one written method, run verbatim from the text in both shells (V1–V5); 3: no script, hook or tool beyond Git (V18); 4: the version line informs and never updates (V15); 5: each Step 0 addition replaces the unspecified "materialize with `git archive`" sentence, three repeats go, and the new rows are the contracted capabilities; 6: Git-only primary, archive link not primary; 7: limits named (V8, O3, O8). Latent corners O1, O2 |
| Safety and security | ✅ | DoF 1: staging never reaches a receiver's index (G3; V1, V10), the upstream state is staged but excluded at copy and dropped from archives (V11, V14); DoF 2: a full download is disclosed (G2; V6, V7); DoF 3: bounded at 5 s, unknown offline (G6; V15); DoF 4: no code (V18); DoF 5: no protecting check removed (V17); DoF 6: no private name or machine path in 42 commits (V21); no secret, remote or GitHub change |
| Human acceptance authority and reserved effects | ✅ | owner rulings A1–A4 and the TS approval precede the work (journal 02ae, 235b); no scope or budget self-extended (V19); the Baseline move is the Coordinator's disclosed act with no threshold crossed (O6); final acceptance, changelog, landing, push, tag and release remain reserved to the owner and Coordinator |

### Purpose Check

**Clause served (HL §1 at `975fed5f`):** "Installing or updating TFW moves the framework and a small,
named remainder — under one megabyte today — instead of the whole development repository and its
history. … The shipped instructions name one way to fetch it, so no agent improvises a download or
rediscovers the same trap in each project … When a newer release exists, the Coordinator says so in
one line when new work starts; the owner decides whether and when to update." North Star: NS1 ("not
the production of more text or more process"), NS2 principles 2, 5 and 7, NS3 (not vendor-bound).

**Harm protected:** every receiver moving about 114 MiB and every new user about 123 MiB (179 MiB by
ZIP) of the framework's own task history; agents improvising the fetch and re-diagnosing the same
blobless-archive trap (R1, twice); receivers lagging silently. Measured on the Candidate: update
679.57 KiB, install 774.34 KiB, ZIP 525,788 bytes — all under one megabyte — with raw-byte identity
in both Windows shells under a hostile line-ending setup; the version line bounded at 5 s and never
updating.

1. **Excess and adjacency** — none. The step removals are admitted by §3 claim 5 as extended by A3;
   the pre-seal check replaces "only when safe"; the README hint is the HL §9 mitigation for the first
   update; nothing touches a non-goal (no hook, script, notification, background check, automatic
   update, history move or Assisted change).
2. **Deferral confession** — none. The changelog entry (TS §2, closing), the `update.md` legacy cleanup
   and the 1,400-word Design Rule (A4, a separate task) and GitHub's archive (owner's push) are left
   where the contract assigns them.
3. **Materiality** — observations O1–O9 leave the approved value intact: O1 needs a same-named branch
   that the canonical upstream does not have; O2 affects only dormant pre-2.0 receivers, loudly; O3 is
   an observation limit; O4–O9 are record or close-time items.

Outcome: **Aligned** ✅. The process added is one card row and one written method; the process removed
is three repeats and an unspecified improvisation. The reference set is consistent in meaning; the
residual wording tension in claim 2 (O4) is surface tension covered by the owner's A1 choice.

## 2. ASSURANCE

| Subject | Status | Evidence / finding IDs |
|---|---|---|
| Evidence exists | ✅ | EV E1–E24 and E-accounting; `evidence/trials.md`; this review's V1–V23 |
| Evidence applies to accepted subject, Candidate/revision, environment, oracle/authority and dependencies | ✅ | EV's Step 0 runs T1b–T3b and every run here used the Candidate's `update.md` blob `c630386e` and `quickstart.md` blob `ace33e4e`; GitHub `v3.7.1` and local mirrors of `v3.7.1` and of the Candidate; Git 2.42 in both Windows shells (2.43 in WSL by EV) |
| Evidence is sufficient for each material claim and risk | ✅ | every TS-required Reviewer re-run done (Step 0 in both shells, three-language reading, accounting); failure cases reproduced (V6–V8); limits named: Codex sandbox and GitHub archive DEFERRED (O8), macOS, Git below 2.42, real filter-less hosts, the card's rendering by a fresh Coordinator (O3), the whole-workflow trial by the Executor only (E12) |
| Permanent guards demonstrate relevant counterfactual detection | ✅ | G1 raw-byte check (V3, V8), G2 size check (V6), G3 pre-seal check (V1, V10) admitted; G4 a setting with demonstrated effect; G5 limited to tag movement (O1); G8 labelled a positive control; G9 a governance scan with a positive control |

## 3. TRACE

| Subject | Status | Evidence / finding IDs |
|---|---|---|
| Governing authority and independent role lineage | ✅ | complete spine in `status.md`; dispatches c29b, ded6, d297, 489d, ade4; role-clean commits (V20); this Reviewer independent of Researcher and Executor |
| Accepted-result identity and immutable accounting | ✅ | Candidate `0b755dca`, first tested implementation commit, reachable on `lfd/exec`, no later commit (V20); 8 files, 122 + 29 = 151 against the immutable 8 / 160 (V19); O6 disclosed |
| Reproducibility and citation integrity needed for material claims | ✅ | every EV figure reproduced within pack variance; HL §7.2 and ONB §7 citations resolve and match; O5 (a wrong path count in E23) is non-material |
| Authorized continuation, item completion routes and dispositions | ✅ | APPROVE → `KNW` → Coordinator's close; each observation names owner, completion and route (below) |
| Record-only observations | ✅ | O4, O5, O6, O8, O9 stay in their carriers; no product restart and no Candidate move |

## 4. Finding Rulings

No material finding exists. Each observation is recorded once with its class and proposed
disposition; the Coordinator rules dispositions at close.

| ID | Class | Subject / affected claim or authority | Fact + oracle | Harm and material consequence | Owner / completion | Route / rung | Candidate effect | Disposition |
|---|---|---|---|---|---|---|---|---|
| O1 | VALUE (latent) | Step 0 `clone --branch <tag>`; DoD 3, D70 | a same-named branch wins over the tag; the recorded line is the tag object only (V16) | wrong object under a release label, only if a version-named branch ever exists; none on the canonical upstream today | Task Coordinator; Step 0 compares the clone's commit with the peeled tag, or the owner accepts | observation; carrier: the owner-approved separate `update.md` task (235b), once created | unchanged | proposed: not material now; carry to that task |
| O2 | VALUE (legacy) | pre-2.0 receivers; claim 1, principle 2 | Step 0 stages only `.tfw`; the 2.0.0 guide needs `tools/migrations/2.0.0/` from the same ref; RES iteration 1 D11 | one extra improvised small fetch for dormant 0.x/1.x receivers; loud; not material | Task Coordinator; a one-line pointer or acceptance | observation | unchanged | proposed: not material; optional pointer in the same later task |
| O3 | ASSURANCE (limit) | version line reach; DoD 6 | card rendering by a fresh Coordinator unobserved; `plan.md` row 2 omits the rule's inputs (V15) | lag could stay silent if a reader skips the row; not established | Task Coordinator; observe the row at the first real new-task start after landing | observation | unchanged | proposed: pending that observation at close |
| O4 | TRACE (contract wording) | HL §3 claim 2 | "only what a new receiver installs" vs the owner-approved cone-mode install (A1, AC-4) | wording inconsistency; not material | Task Coordinator → owner; acknowledgement or a §12 row | HL §12 only if the owner wants it | unchanged | proposed: owner acknowledgement at acceptance |
| O5 | TRACE (evidence text) | EV E23 | cited command returns 15 paths, not 9 (V18) | none | Coordinator; optional EV note | optional current-carrier repair | unchanged | proposed: not material |
| O6 | TRACE (authority record) | accounting Baseline | moved in place before launch; no threshold crossed under either Baseline (V19) | none | Task Coordinator; present with the result | Coordinator's own record | unchanged | proposed: presented at acceptance |
| O7 | VALUE (minor) | README prompts | no size check or fallback; possible second fetch for Full (V11) | none material | Task Coordinator | observation | unchanged | proposed: not material |
| O8 | TRACE (close-time) | E9 Codex sandbox, E17 GitHub archive | DEFERRED as the TS allows | none | Task Coordinator; each recorded observed or unobserved at close | close-time disposition | unchanged | pending at close |
| O9 | TRACE (economics) | Executor economics revision 1 | the contract changed during review to `<sessionId>/<agentId>` for subagents; the file carries the session-only ID (V23) | report coverage could mis-key one contribution; not a product matter | Task Coordinator with the Executor | close-time economics reconciliation | unchanged | pending at close |

## 5. Aggregate Verdict

**Verdict:** ✅ APPROVE

**Reason:** VALUE holds: the Candidate serves HL §1 and the North Star, meets AC-1 to AC-8 on
independent re-runs (V1–V18), and triggers no DoF; safety and human authority floors hold (V20, V21,
O6). ASSURANCE holds: every TS-required Reviewer check ran, failure cases were reproduced with
admitted guards (G1–G3), and remaining limits are named (O3, O8). TRACE holds: identity and accounting
replay exactly (V19, V20); the record items O4–O6, O8 and O9 and the latent VALUE corners O1, O2 and
O7 change neither acceptance nor the next authorized act.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | Accepted claim | Contradiction / effect |
|---|---|---|---|
| 1 | D70 "Pin from the operator-named tag … match the tag name—never source `HEAD`" | Step 0 pins with `clone --branch <tag>` | no contradiction for the canonical upstream; the same-named-branch corner (O1) is where the written command could diverge from D70's intent |

No other applicable contradictions: D2, D82, F23 and HL Contract rule 15 are consistent with the
Candidate.

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
