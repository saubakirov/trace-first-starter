# REVIEW — TFW_20260902-111644_CRATM / Phase E: Sweep correction and release preparation

> **Date**: 2026-09-07
> **Author**: Phase E Reviewer (Codex)
> **Verdict**: 🔄 REVISE
> **RF**: [RF Phase E](RF__phase-e__sweep_correction_and_release.md)
> **TS**: [TS Phase E](TS__phase-e__completion_and_release_preparation.md)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`

---

## 1. Map

Corrected K1 precedes Candidate II `6c93e813e7a3ccae05b74a85170cca36c2de8856`. Candidate II changes the
exact twelve VALUE paths and two ASSURANCE paths: three canonical writer rules and their six copies,
five glossary routers, one Phase-B anchor, one release-package carrier, and assurance. EV/RF/dispatch
follow as TRACE; K2, lifecycle close, release application, saved landing, tag, push, and publication
remain outside this review.

The RF correctly leaves four Main challenges for independent review. Exact patch bytes and all
pre-release gates reproduce, but the operational package/current-state claims do not.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| V-accounting | Independent value-bearing replay | VERIFIED | Approval `759475fe…` / TS blob `96585e0f…`; Baseline `b0bfcd2…`; Candidate `6c93e81…`; exact 12 VALUE paths / 417+37=454 LOC; exactly 2 ASSURANCE paths; no binary N/A; below 12/900 and 24/1800; Candidate precedes EV/RF; no later VALUE; exact 46-path union floor/forecast 2908/3288≤4000. |
| V-K1 | Corrected Knowledge Gate input | VERIFIED | K1 `e06a84d…` has the ten VALUE paths / 97 LOC, exact F11, nine markers/eight sources, 169/75/94/359/606/231, digest `3ec4fae5…`, unchanged `KNOWLEDGE.md` blob `0325a157…`; detached K1 doctor returns no pending task. Failed `12a3c7b…` is disclosed. |
| V-current | Writer/copy/glossary/anchor/debt result | VERIFIED | Stale canon 3→0; exact sentence once across all nine files; triple hashes exact; words 2051→2024 / 1167→1140 / 2122→2095; five one-owner routers; B9 anchor and strict build pass; prior debt records remain intact. |
| V-package-bytes | Embedded six-file patch, postimages, and protected Candidate | VERIFIED | Package digest `0324ccc8…`; independent apply yields exact six paths / 177+3=180 LOC and all six expected SHA-256 values; Candidate's canonical release diff is empty. |
| V-pre-release | Configured Candidate-II suite | VERIFIED | Independently: 529 collected; 528 passed, 1 skipped; 15 Phase-E passed; strict MkDocs exit 0; diff/parity/census/mutants green. |
| V-successor | Exact Candidate-II-plus-package state | BLOCKED | Targeted current-state guard exits 1 because legitimate `.tfw/migrations/3.0.0.md` exists. Package-created `b0bfcd2…` tree collects only 522 pre-Candidate tests, while package commands run in the caller tree. |
| V-operation | CWD, failure propagation, rollback | BLOCKED | Python/MkDocs have no `$releaseTree` location; a failed native command followed by success yields wrapper exit 0; line 91 removes the patch and documented rollback exits 128. |
| V-semantics | RTBO/provider migration text | BLOCKED | Package says no shared knowledge index though semantic `KNOWLEDGE.md` §4 remains; provider-neutral instructions omit frozen master §3 claim 9/A6 and F11's homogeneous/Codex-first/Claude-gated/fresh-helper limits. |

Raw log: [review/verify.md](review/verify.md). Verification covered all fourteen Candidate-II files
and all RF evidence artifacts. One limitation remains: the exact fourteen-path commit result is proved,
but the claimed contemporaneous `git commit --only` invocation is absent from RF/EV/attachments.

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD / all TS AC | ❌ | AC-1–AC-3 hold; AC-4/AC-5 fail at Verify V-successor/V-operation/V-semantics. |
| 2 | Purpose and design | ❌ | Purpose is aligned with NS1 and frozen master §1; design is unsound because it verifies the wrong tree, masks failure, loses rollback, and rejects the authorized successor. No contract defect or purpose-scope failure. |
| 3 | Debt disposed by consequence | ✅ | Two Phase-D rows retain terminal Coordinator rulings and are now non-material under RTBO; Phase-C items are paid in existing phase-c. New defects are correction findings, not debt. |
| 4 | Style and standards | ❌ | Canon/copy/glossary style holds; migration wording and executable command contract do not. |
| 5 | Observations collected | ✅ | RF/EV preserve all four real challenges without late repair or premature ruling. |
| 6 | RF §7–§9 complete | ✅ | All three sections exist and validly report none. |
| 7 | Evidence exists | ✅ | Six EV rows and every attachment resolve. |
| 8 | Evidence is sufficient | ❌ | Evidence proves pre-release bytes/gates, not executable release-tree verification, rollback, successor compatibility, or migration semantics. |
| 9 | Backward compatibility | ❌ | G-3 creates a guaranteed current-test failure; migration consumers can receive false knowledge/provider guidance. |
| 10 | Safety | ❌ | Rollback input is removed and native-command failure can be masked; no secret/credential issue found. |

Purpose reference: North Star NS1 requires that another authorized participant can inspect the current
result and continue; frozen master §3 claim 9 requires field-proven provider-homogeneous long-lived
chains. This is the right release subject, but the concrete harm is a falsely green, non-recoverable
release that can exceed its admitted provider boundary.

## 4. Verdict

**🔄 REVISE**

Candidate II is correctly bounded and its pre-release implementation/accounting gates are green, but
it cannot satisfy AC-4/AC-5 at the authorized successor. The exact package changes cause the current
suite to fail; the package tests the caller rather than its release tree, can mask native-command
failure, and cannot execute its documented rollback. Its RTBO and provider prose also contradicts
retained semantic knowledge and the frozen A6/F11 admission boundary.

All four proposals are **Rung 1**: the existing approved TS, literal 12 VALUE + 2 ASSURANCE selector,
and immutable denominator remain sufficient. No TS or frozen-HL change is proposed.

### If REVISE — proposals to coordinator

1. **Make assurance successor-compatible without a late G-3 write** — **basis:** TS AC-5 lines 375–380. **Owner after ruling:** the same Phase E Executor. **Observable completion:** the two existing assurance files separately preserve immutable pre-release objects and accept only the exact pre-release or package-defined post-release current bytes; pre/post/corrupt mutants pass, and the unchanged configured suite passes after applying the package.
2. **Make the package execute and roll back in its named tree** — **basis:** TS AC-4 lines 355–369. **Owner after ruling:** the same Phase E Executor. **Observable completion:** a disposable tree based on exact Candidate II (and later the exact post-DONE baseline) retains the six content-preimage checks, runs collection/full pytest and strict MkDocs inside `$releaseTree`, stops/propagates every non-zero exit, reverses to all six preimages with a retained/reconstructed patch, then reapplies to all six exact postimages.
3. **Correct the RTBO migration boundary** — **basis:** TS AC-4 lines 357–361 and frozen master DoD 16/D82. **Owner after ruling:** the same Phase E Executor. **Observable completion:** package prose says the tracked task portfolio cache and numeric line ceiling are retired while semantic `KNOWLEDGE.md` and its §4 fact index remain; a negative check rejects the current false phrase.
4. **Carry the provider admission boundary into release prose** — **basis:** TS AC-4 lines 360–361 and frozen master §3 claim 9/A6. **Owner after ruling:** the same Phase E Executor. **Observable completion:** changelog/migration distinguish provider-neutral methodology from available profiles: long-lived chains are provider-homogeneous, Codex is the first implementation, a complete Claude-only chain is not admitted without the native gate, and cross-provider fresh runs are bounded helpers only.

The Coordinator must rule these four proposals once in this live REVIEW. If accepted, the same
Executor uses the existing approved TS, creates a new Candidate because VALUE and ASSURANCE change,
recomputes package digest/postimages/accounting/full union, captures contemporaneous exact-path staging,
rewrites EV/RF for the round, and returns to this same Reviewer. Lifecycle remains `RF` until the
Executor accepts a ruled Rung-1 round and the route permits `RF → ONB`.

## 5. Tech Debt Collected and Disposed

No new debt is created by this review. The three prior groups have terminal existing dispositions;
the four material items above are REVISE proposals and may not be deferred as debt.

| # | Source | Severity | File | Description | Disposition |
|---|---|---|---|---|---|
| 1 | Phase-D REVIEW §5 item 1; Phase-E EV | Med | `.tfw/scripts/gen_index.py` (retired) | Former shipped generator omitted valid event `writer`. | **not material — owed but forbidden to pay.** Existing Coordinator ruling is terminal; RTBO removed the shipped runtime/portfolio-cache duty, so restoration would breach the accepted no-runtime boundary. |
| 2 | Phase-D REVIEW §5 item 2; Phase-E EV | Low | immutable RDP journal event | Historical 123-character summary exceeded a former 120 ceiling. | **not material — not owed.** Existing Coordinator ruling is terminal; RTBO removed numeric prose validity ceilings and immutable history remains untouched. |
| 3 | Phase-C REVIEW rev2 §5 items 1–5; Phase-E EV | Med | Phase-C authority/routing implementation | Five earlier authority/evidence defects. | **paid — phase-c.** Existing `phase-c/` RF/EV/REVIEW records the consequence-removing repair and current assurance preserves it. |

## 6. Traces Updated

- [x] REVIEW and map/verify/judge written; a phase handoff event returns four Rung-1 proposals to the Coordinator. `🔄 REVISE` authorizes no lifecycle/outcome/status transition.
- [x] Phase HL/status unchanged because Phase E does not complete and §5 has no pending debt row.
- [x] Stale project files checked; no product, assurance, K2, release, saved-checkout, tag, push, or publication write made.
- [x] tfw-docs: N/A — only after independent APPROVE/KNW.
- [x] tfw-knowledge: N/A — REVIEW/RF contain no Fact Candidates, and REVISE remains at `RF`.

## 7. Fact Candidates

> fact-candidates: processed 2026-09-07

No fact candidates. The four findings derive from repository artifacts and reproducible tests, not a
new human-sourced project fact.

---

*REVIEW — TFW_20260902-111644_CRATM / Phase E: Sweep correction and release preparation | 2026-09-07*

## 8. Coordinator ruling — completion return round 1

**Ruled 2026-09-07 by the Phase E Coordinator under Main's A8 technical ruling.** All four
Reviewer proposals are accepted once as material **Rung 1** implementation defects. The proposal
source remains the Phase E Reviewer unit `01a078a4-5ef7-76f0-8a1f-f5e165e3504e`; technical ruler
is `robert`, Main task `01a07050-9d35-7080-a5f6-afd14334e68d`. The existing approved completion
plan `759475fe232fee39f7e25a2aa0f25df2214cde7f`, TS blob
`96585e0f8bd3d49b8d81f17bed96821b76cef1d3`, corrected K1
`e06a84d81594df770d48ae3426a8551677207538`, literal selector and immutable budgets remain
governing. No TS/HL amendment, new authority or additional approval epoch is required.

### Accepted return bound

1. **Successor-compatible assurance.** Preserve the immutable pre-release snapshot checks and add
   exact successor checks without freezing the current tree at the pre-release state. The two
   existing assurance files must exercise the exact pre-release state, legitimate G2 K2/DONE and
   G3 release successors, and corrupt states, so those later gates require no assurance write.
2. **Executable and reversible release package.** Revise the existing package VALUE carrier so it
   verifies the corrected Candidate payload in the named release tree. Keep immutable six-file
   content-preimage checks distinct from the invocation's exact execution baseline; do not embed a
   self-referential commit SHA. Run collection, the full suite and configured strict MkDocs inside
   `$releaseTree`, with explicit native exit checks, correct working directory and fail-fast exit
   propagation. Retain or deterministically reconstruct the patch through a proved
   forward → reverse → reapply cycle; prove all six original preimages and staging are restored,
   then prove all six exact postimages again. Do not mutate canonical release paths in the Executor
   checkout.
3. **Exact RTBO migration boundary.** State that RTBO retires the tracked task-portfolio cache and
   numeric semantic-index line ceiling while retaining semantic `KNOWLEDGE.md` and its §4 fact
   index. Add an effective negative check that rejects the false phrase “no shared knowledge index
   is maintained.”
4. **Exact provider admission boundary.** Distinguish provider-neutral methodology from currently
   admitted execution profiles: long-lived chains are provider-homogeneous; Codex is the first
   implementation; a complete Claude-only chain is not admitted without its native proof gate;
   cross-provider fresh runs are bounded helpers only. This grants no new capability or admission.

### Selector, Candidate and evidence ruling

The same Executor may modify only the existing package VALUE path and the two existing ASSURANCE
paths for this repair. The other eleven Candidate-II VALUE outputs remain byte-identical to
`6c93e813e7a3ccae05b74a85170cca36c2de8856`. Ordinary append-only ONB/EV/RF/review/dispatch TRACE is
allowed; no canonical release, K2/DONE, new product path, runtime, profile, role/session, tag, push or
publication write is authorized.

Candidate II `6c93e813…` remains reachable as the failed first attempt. After this ruling and
contemporaneous exact-path staging evidence, the first fully tested new VALUE+ASSURANCE commit is the
replacement Candidate II and must precede the new EV/RF round. Recompute the whole fixed
`b0bfcd22125d8a34366d7eb885a2fb54234bdc7d` → replacement diff over the same twelve VALUE paths
(immutable 12/900; owner 24/1800), the package digest/postimages, exactly two ASSURANCE paths, and the
whole `957f7be8f5f208b87be12a8cd4d67b24af00cd1e` → replacement 46-path forecast (immutable 46/4000).
Do not measure only the repair hunk, subtract history, ratchet or borrow capacity; any forecast
escalation must precede work.

Rerun every configured full/targeted/strict gate plus the actual corrected release-tree full suite,
forward/reverse/reapply proof, corrupt mutants and current/snapshot checks. Preserve initial failures
transparently. Lifecycle remains `RF` until this same Executor accepts the ruled round and records
`RF → ONB`; after replacement EV/RF, return to this same Reviewer for `/tfw-review`.
