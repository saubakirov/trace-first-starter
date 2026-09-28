# Judge — TEQM Candidate

> Verify findings: [verify.md](verify.md). Accepted result: `83227789c5218a01d669acb42903844c5dc21bd9`.

## 1. VALUE

| Subject | Status | Evidence / finding |
|---|---|---|
| Purpose and approved value | ✅ overall purpose aligned; ❌ delivered behavior | Master HL §1 requires each role's measured resource return and a task report useful across machines. North Star NS1 requires inspectable material grounds; NS2 requires consequential uncertainty visible. F1 silently accepts a contested real-source total; F2 omits phase returns; F3 prevents a report over a valid real return. They harm the owner's ability to compare true task costs. |
| Domain behavior / AC | ❌ | F1 affects TS AC-2/4; F2 violates AC-3/4 and HL DoD-2/6; F3 violates AC-1/4. The 95 task checks pass but omit these real/phase cases. |
| Architecture and HL principles | ❌ | F2 defeats task-local leaf aggregation once and HL P5. F1 defeats HL P4 evidence before precision. Both are correctable inside the approved architecture. |
| Safety/security | ✅ within inspected scope | Native selectors stay bound, SQLite backup is read-only, small numeric returns omit transcript content; no contrary observed fact. |
| Human acceptance authority | ✅ | Approved HL/TS and dispatch precede Candidate; Coordinator retained owner pre-close presentation and did not claim DONE. |

### Purpose Check

At the approved contract baseline, HL §1 says every role returns its own measured JSONL and the Coordinator supplies one account of role/model resources. HL §3 says the task report combines phase consumption and task coordination without double counting. The root `README.md` and North Star NS1/NS2 require an inspectable, purposeful result with material uncertainty visible. The Candidate is directed at that purpose and adds no excluded tracking service or personal activity collection. F1's unqualified smaller total, F2's phase omission and F3's crash on a valid real return materially harm the very account the owner requested. The remedy is bounded correction, not a new purpose or contract ruling.

## 2. ASSURANCE

| Subject | Status | Evidence / finding |
|---|---|---|
| Evidence exists | ✅ | RF, EV, task checks, saved pilots and real role returns resolve. |
| Evidence applicability | ⚠️ partial | Pilot totals apply to selected historical sessions; three native probes apply to exact surface/version. Coordinator return at `e78e0fec` and `5aaf6691` adds a contrary real Codex case for the same Candidate. |
| Sufficiency for material claims | ❌ | F1 proves normal Codex reader's claimed coverage is unestablished; F2 counterexample proves phase/root rollup wrong; F3 actual return crashes the report. |
| Permanent guards | ⚪ N/A | No new permanent guard was added or required. Task-local negative fixtures are bounded assurance controls; the existing suite protects its existing deployment/size boundaries. |

## 3. TRACE

| Subject | Status | Evidence / finding |
|---|---|---|
| Authority and independent lineage | ✅ | Selected status, owner A5/A6, Coordinator dispatch and separate Reviewer address resolve; no title grants mandate. |
| Result identity/accounting | ✅ | Exact NUL-safe 26-path replay: 5 A/21 M, 2,006 + 31 = 2,037 touched text LOC, below 52/5,000 ceiling. Candidate is before RF/EV; later TRACE does not move it. |
| Reproducibility/citations | ✅ with limits | Evidence names revisions, environments and limits; PV P0/P1 and HL §7.2/ONB §7 sources resolve. F1 is a product/source-meaning defect, not a missing citation alone. |
| Continuation | ✅ | Both items have the existing Executor → Coordinator correction route, observable completion and new Candidate requirement. Owner pre-close presentation and final report remain reserved later gates. |
| Record-only observation | ⚪ N/A | No separate non-material record defect found. |

## 4. Finding Rulings

| ID | Class | Subject / accepted claim | Fact + oracle | Harm and material consequence | Owner / observable completion | Route / rung | Candidate effect | Disposition |
|---|---|---|---|---|---|---|---|---|
| F1 | VALUE | Ordinary Codex source collection, TS AC-2/4 | For identical verified prefix, successful collector returns 62,902,737 while independent 460-response sum/final native thread counter is 64,405,038; `codex_rows` ignores that stream | Routine role costs can silently understate or misattribute 1,502,301 tokens on actual work; a manual Coordinator workaround does not make the shipped path truthful | Existing Executor, through Coordinator: establish the two streams' scopes, make normal collection detect/handle/qualify this case, prove the actual bound source and rerun affected report arithmetic | Correct accepted product within TS; same Executor, then this independent Reviewer | New tested VALUE Candidate | pending |
| F2 | VALUE | Task/phase aggregation, TS AC-3/4 and HL DoD-2/6 | Root reader scans only direct `economics/roles`; phase fixture has five tokens but root reports zero | A phased task's full cost and project comparison omit real role work, defeating owner decisions | Existing Executor, through Coordinator: traverse actual phase roots and task-root leaves once, show correct lifetime/period report and no parent duplication or concealed missing units | Correct accepted product within TS; same Executor, then this independent Reviewer | New tested VALUE Candidate | pending |
| F3 | VALUE | Pricing and report generation, TS AC-1/4 | Actual Researcher row validates with zero cache writes and null 5m/1h splits; `price` calls `Decimal(None)`, and three-role report fails | Valid returned work cannot enter the required task report; stale two-role basis remains | Existing Executor, through Coordinator: price zero writes as zero, retain unknown for nonzero unsplit writes, rerun actual three-role report with correct total | Correct accepted product within TS; same Executor, then this independent Reviewer | New tested VALUE Candidate | pending |

## 5. Aggregate Verdict

**Verdict: 🔄 REVISE.** F1, F2 and F3 are material, correctable VALUE defects in the accepted result. The approved task purpose and authority remain sound. Correction returns through the current Coordinator to the same Executor; this Reviewer will assess the replacement Candidate and affected proof. No lifecycle move is authorized by REVISE.

## Contradictions with KNOWLEDGE.md

No applicable contradiction in the governing knowledge. The Candidate behavior conflicts with the accepted task contract; D68/D76/D82/D86 remain applicable as cited.

## Checkpoint

**Self-check:** VALUE → ASSURANCE → TRACE applied; Purpose checked against baseline HL and North Star; evidence existence separated from sufficiency; both items have full routes and Candidate effects; one verdict derived from material harm. Stage complete: YES.
