# REVIEW — TFW_20260902-111644_CRATM / Phase C: Authority routing

> **Date**: 2026-09-06
> **Author**: Codex (Reviewer; acting as `saubakirov`)
> **Verdict**: 🔄 REVISE
> **RF**: [RF Phase C](RF__phase-c__authority_routing.md), state tip `f36c426b9d70695e3cd2639d87885aac3af5170b`
> **TS**: [TS Phase C](TS__phase-c__authority_routing.md), approved at `1f1173d968e9b74a5e06e3e2070ae604c2844ca5`
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`

---

## 1. Map

The Candidate replaces universal owner-only amendment routing with a human-rooted, child-only
authority resolver, preserves the originating proposer, chooses the nearest eligible non-proposer
ruler, and retains named human-only exceptions. The change spans six canonical contract/workflow/
template owners, six exact tracked copies, and two assurance modules; Git independently confirms the
declared 12 VALUE + 2 ASSURANCE boundary and immutable Candidate lineage.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| V-authority | Rule 8 and every current owner-only consumer | BLOCKED | Two live §14 anti-patterns retain owner-signing language and EV classifies them `live; narrowed`, outside AC-4's permitted classes; current rule 8 also omits the prior guarantee required by the frozen master. |
| V-ordinary-CL | Rule 8, Plan 6d, and assurance coverage | BLOCKED | Rule 8 routes no-delegation CL directly to the owner; Plan 6d has no such branch, requires delegation facts, and STOPs when they are absent. The `ordinary_cl` helper short-circuits before reading Plan. |
| V-accounting | Independent value-bearing replay | BLOCKED | Approval `1f1173...`; Baseline `fb08c120...`; Candidate `b2a963...`; literal 12 VALUE members; 89 additions + 90 deletions = 179 touched text LOC; binary N/A; immutable 12/320 denominator; below triggers; ancestry and zero later VALUE verified. Exact Candidate membership/subject are visible, but the required contemporaneous full-status, cached-name, exact pathspec, and `git commit --only` evidence is absent. |
| V-assurance | Validator, targeted tests, full suite, build, structure, copy parity | VERIFIED with stated limits | 503-line program executes; 38/38 helper payloads and 10/10 mutants hold; targeted 7/7; configured 635 passed + 1 skipped of 636; MkDocs and structure exit 0; all six copies match. Those signals do not exercise the Plan ordinary-CL text or validate AC-4's census classes. |
| V-evidence-hash | Recorded validator output and SHA-256 | BLOCKED | The 3,788-line content matches after stripping stdout's terminal LF. Raw stdout SHA is `260d571f...`; claimed `1a0445cb...` is the fenced payload without that LF, so “byte-for-byte output” is not exact. |
| V-citations | HL §7.2 and ONB §7, PV 0–7 | VERIFIED | 20/20 references resolve through explicit anchors/real files; 20/20 items exist, match their claimed meanings, and are relevant. No hallucinated or irrelevant citation. |

Raw log: [review/verify.md](review/verify.md). Verification was escalated from the configured
`ceil(14 × 0.42) = 6` minimum to all 14 Candidate files after the first discrepancy. The broad
repository-root pytest command is not configured and collides with generated `site/scripts` module
names; the exact configured suite was rerun successfully. Inherited MkDocs unresolved-reference
warnings do not name Phase C.

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD / all TS AC | ❌ | AC-1, AC-4, AC-5's dependency on AC-4, AC-6, frozen Phase C deliverable 3, and master DoD 10 are not fully met. |
| 2 | Purpose and design | ❌ | Purpose is aligned: baseline HL §1 requires every proposal to terminate at a human and be ruled by the nearest named principal, protecting NS1's human-governed continuity from unauthorized frozen-contract change. Design delivery fails because live owner-only text competes with the resolver and Plan rejects the required ordinary-CL path. |
| 3 | Debt disposed by consequence | ✅ | All five findings are proposed as `pending — coordinator` against this existing Phase C, each with a named consequence and observable completion condition. |
| 4 | Style and standards | ❌ | Copy parity, naming, Candidate subject, and membership hold; canonical old→new legibility and contemporaneous exact-path evidence do not. |
| 5 | Observations collected | ✅ | RF observation 1 is a real authority issue; review confirmed it and found the adjacent anti-pattern plus the Plan consumer gap. |
| 6 | RF §7–§9 complete | ✅ | Fact Candidates, Strategic Insights, and Diagrams sections are present and explicitly empty. |
| 7 | Evidence exists | ❌ | EV contains the main source/payload/test/count/lineage evidence, but no contemporaneous status/cached-name/exact-path commit transcript. |
| 8 | Evidence is sufficient | ❌ | Passing helper tests establish their model, not the contradictory Plan consumer or AC-4 classification; raw stdout hash wording is also inexact. |
| 9 | Backward compatibility | ❌ | Ordinary CL is promised a direct-owner route but Plan 6d requires absent delegation facts and STOPs; both accepted Plan copies preserve the break. |
| 10 | Safety | ✅ | No secrets, credentials, destructive/external act, runtime authority, provider permission, Phase D/E surface, push, or master mutation occurred. |

Purpose is **aligned**, and the master baseline/North Star are internally coherent. These are
correctable delivery/evidence failures against the approved order, not a purpose failure or contract
defect, so `❌ REJECT` is not warranted.

## 4. Verdict

**🔄 REVISE**

The immutable boundary, arithmetic, ancestry, copy parity, validator content, configured suite, build,
and knowledge citations are independently verified. Approval is blocked because the shipped
enforcement surface does not consistently implement ordinary CL or the owner-to-ruler change, the
canonical rule omits a frozen disclosure requirement, and AC-6 evidence is incomplete. Five items
are proposals to the Coordinator; the proposed round is rung 1-only because every correction is
inside the existing approved TS. Only the Coordinator may rule that classification and bound.

### Proposals to coordinator

1. Replace or explicitly route the two live §14 owner-only anti-pattern sentences so a fresh census
   puts every current occurrence into AC-4's permitted classes and no current enforcement site can be
   read as requiring the owner to sign — **basis:** TS AC-4 and DoF “Any current owner-only enforcement
   consumer survives unclassified”; frozen master DoD 9–11.
2. Amend Candidate rule 8 to state both the current resolved-ruler guarantee and the prior “only the
   owner rules” guarantee it replaces, with the old→new weakening legible in the canonical rule —
   **basis:** frozen master Phase C deliverable 3 and DoD 10; TS AC-5 frozen-boundary contract.
3. Add an explicit ordinary-CL/no-delegation branch to Plan 6d before delegated-chain validation and
   extend assurance to parse/test that actual consumer plus a contradiction mutant — **basis:** TS
   AC-1 ordinary-CL backward compatibility and AC-4 one-authority consumer cascade.
4. On the required replacement Candidate created by items 1–3, preserve real pre-commit full status,
   cached-name list, exact full-path pathspec, and `git commit --only` output contemporaneously in EV;
   then recompute Candidate membership, accounting, ancestry, and no-later-VALUE proof — **basis:** TS
   AC-6, HC-C1, and Technical Guidance. Do not reconstruct the old shell history.
5. Re-record the validator digest against a named byte representation: either hash exact stdout
   including its terminal LF or explicitly label the existing digest as fenced content without that
   LF; remove the unsupported byte-for-byte equivalence and rerun the extraction — **basis:** TS AC-5
   execution honesty and AC-6 reproducible evidence.

Observable completion is a replacement Candidate/EV/RF return in which the current-source census,
actual Plan ordinary-CL consumer test, old→new rule-8 text, contemporaneous staging transcript,
literal 12-path accounting, digest representation, targeted/full suite, copy parity, and
Candidate→tip immutability all agree.

## 5. Tech Debt Collected and Disposed

| # | Source | Severity | File | Description | Disposition |
|---|---|---|---|---|---|
| 1 | RF §6 observation 1; Verify discrepancy 1 | High | `.tfw/conventions.md` | Live anti-patterns say `logged owner verdict` / `owner rules`, leaving current enforcement language outside AC-4's allowed census classes; omission preserves contradictory signing authority. | **pending — coordinator** — rule the Phase C correction; unresolved, the frozen-amendment channel has two competing readers and Phase C cannot close. |
| 2 | Verify discrepancy 2 | High | `.tfw/conventions.md` | Rule 8 omits the old owner-only guarantee that the frozen master requires it to replace explicitly; omission hides the material authority weakening from canonical readers. | **pending — coordinator** — rule the Phase C correction; unresolved, frozen master deliverable 3/DoD 10 remain unmet and Phase C cannot close. |
| 3 | Verify discrepancy 3 | High | `.tfw/workflows/plan.md` and two tracked copies | Plan 6d has no no-delegation branch and makes separate root/child-chain facts unconditional; omission blocks ordinary CL despite rule 8. | **pending — coordinator** — rule the Phase C correction/test bound; unresolved, existing CL consumers can STOP incorrectly and Phase C cannot close. |
| 4 | Verify discrepancy 4 | Medium | `evidence/EV__phase-c__authority_routing.md` | No contemporaneous Candidate full-status/cached-name/exact pathspec/`commit --only` transcript exists; omission weakens inspectability of the pre-act HC-C1 gate. | **pending — coordinator** — rule capture on the legitimate replacement Candidate or a non-fabrication disposition; unresolved, AC-6 evidence remains incomplete and Phase C cannot close. |
| 5 | Verify discrepancy 5 | Medium | `evidence/EV__phase-c__authority_routing.md` | Claimed digest is for fenced content without the terminal LF, while actual stdout has it; omission makes the byte boundary and “byte-for-byte” claim false. | **pending — coordinator** — rule an exact representation and rerun in Phase C; unresolved, the validator evidence cannot support its stated byte-level claim and Phase C cannot close. |

No disposition is ruled by the Reviewer. All five proposals remain pending for one Coordinator ruling.

### Coordinator ruling — return round 1

All five proposals are **accepted as proposed — rung 1**. Each correction is already required by
the approved TS: items 1 and 3 close AC-4's live-consumer cascade and AC-1's ordinary-CL branch;
item 2 closes the frozen Phase C deliverable 3 / master DoD 10 through AC-5; items 4 and 5 close
AC-6 and AC-5 execution-honesty evidence. None changes the frozen purpose, authority model, literal
selector, immutable 12 VALUE / 320 touched-LOC denominator, HC-C1/C2, or Phase C scope. The existing
approved TS remains the implementation order; no TS sibling or frozen-HL amendment is authorized,
and lifecycle remains `RF` until the same Executor accepts this bound and records `RF → ONB`.

| Item | Coordinator ruling | Closed return bound / observable completion |
|---|---|---|
| 1 | **✅ ACCEPTED — rung 1** | Replace the two live §14 owner-signing formulations with wording that enforces a valid rule-8 verdict/application and preserves only named human exceptions. Re-run the current-source census; every owner-only occurrence must be classified as replaced amendment route, preserved human exception, historical changelog/knowledge, or unrelated budget/approval rule, with no competing universal owner-signing reader. |
| 2 | **✅ ACCEPTED — rung 1** | In canonical rule 8, state explicitly that the prior guarantee was “only the owner rules” and that the current guarantee routes ordinary delegated amendments to the nearest eligible non-proposer, otherwise the governing owner. Keep the weakening legible without changing its already-approved semantics or exceptions. |
| 3 | **✅ ACCEPTED — rung 1** | Put an explicit ordinary-CL/no-delegation branch before delegated-prefix validation in Plan 6d, then synchronize its two accepted copies. Assurance must parse and exercise the actual Plan consumer, prove direct owner routing without invented delegation facts, and reject an output-changing contradiction mutant; helper-only and substring-only coverage is insufficient. |
| 4 | **✅ ACCEPTED — rung 1** | Any VALUE correction creates a replacement Candidate under the unchanged Baseline and literal selector. Before that commit, capture the complete status, cached-name list, exact full-path pathspec, and actual `git commit --only` command/output contemporaneously; append the untouched capture to EV after the commit. Recompute exact 12-path membership, additions/deletions/touched LOC, ancestry, subject/producer attribution, and Candidate→tip no-later-VALUE proof. Do not reconstruct the first Candidate's shell history. |
| 5 | **✅ ACCEPTED — rung 1** | Hash exact validator stdout including its terminal LF, name that byte representation, record the full digest, and remove the unsupported equivalence to the fenced block. Re-run extraction and prove recorded stdout/digest parity; if the fenced representation is also reported, label its different newline boundary and digest explicitly. |

The return may modify only the already-approved VALUE/ASSURANCE members and append the existing
ONB/RF/EV round traces. Caps remain unchanged; all route/corpus and copy-parity gates rerun. The same
Executor must produce the replacement immutable Candidate and cumulative evidence, then stop at
`/tfw-review`; the same Reviewer verifies the returned lineage. The five historical `pending —
coordinator` cells above are proposals preserved as written and are superseded by these one-time
terminal rulings; no pending disposition remains in this round.

## 6. Traces Updated

- [x] Phase lifecycle intentionally remains `RF`; `🔄 REVISE` alone authorizes no status change or transition event.
- [x] HL status is unchanged; Phase C is not complete and §5 has five pending Coordinator rows.
- [x] Stale project files checked — configured tests, MkDocs, structure, Git lineage, and exact Candidate boundary were inspected.
- [x] tfw-docs: N/A — REVISE does not enter KNW.
- [x] tfw-knowledge: N/A — no RF or REVIEW Fact Candidates.

## 7. Fact Candidates

No fact candidates.

---

*REVIEW — TFW_20260902-111644_CRATM / Phase C: Authority routing | 2026-09-06*
