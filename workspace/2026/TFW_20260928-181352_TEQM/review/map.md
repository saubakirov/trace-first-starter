# Map — TEQM

> RF: `../RF__TFW_20260928-181352_TEQM.md` at `8bbbcab68115df94c9bef787f436a6410a7cf8cc`
> TS: `../TS__TFW_20260928-181352_TEQM.md` approved at `31cd8e19c165c722412a9f486519fe0d2df50a86`
> Accepted subject: `83227789c5218a01d669acb42903844c5dc21bd9` (VALUE/ASSURANCE Candidate)

## Understanding

The Candidate adds portable role usage records, three bounded native readers, safe receipt/aggregation, reports and Full-workflow return/close instructions. Its value is a truthful, inspectable account of task resources across machines and selected products. RF claims the implementation is complete while the TEQM owner presentation, final report and cleanup remain future Coordinator gates.

## Accepted Claims and Boundaries

| ID | Layer | Accepted claim / authority boundary | Risk or concrete harm | Affected behavior / dependencies | Relevant environment | Oracle / authority | Evidence identity | Required? |
|---|---|---|---|---|---|---|---|---|
| C1 | VALUE/ASSURANCE | Versioned typed records and validator preserve null/zero, identities, revisions and token arithmetic | Fabricated or silently misread costs | Schema, validator, producer records | Python 3.13, JSONL | TS AC-1 | Candidate schema/helper; EV E1 and task checks | yes |
| C2 | VALUE/ASSURANCE | Codex, Claude Code and Antigravity readers capture only authorized numeric sources with truthful counters, dates and duration kinds | Privacy breach or false spend/time | Native selectors, dedup, SQLite snapshot, model/rate mapping | Named local source versions | TS AC-2, TS §4 M1 | Candidate readers; EV E2 and source hashes | yes |
| C3 | VALUE/ASSURANCE | Role returns are portable; duplicate, successor, disjoint and overlapping coverage reconcile once | Double spend or missing remote work presented as complete | Hash receipt, source ranges, parent/child and task/phase rollup | Temporary receiver and actual Executor return | TS AC-3 | Candidate helper; EV E3; Executor JSONL | yes |
| C4 | VALUE/ASSURANCE | Reports/CSV separate lifetime and period, unknown and zero, task and project, roles and models, compatible time and conditional money | Owner makes unsound comparisons | Renderer, rate card, UPM/DARYN samples | Selected task roots and dated rates | TS AC-4 | Candidate helper; EV E4/pilot files | yes |
| C5 | VALUE/TRACE | Full workflow gates preserve role locks, acceptance, finite report/cleanup sequence and receipt | Review or owner gate bypass, recursive close | Conventions, ten workflows and installed copies | Full TFW task paths | TS AC-5; owner mandate | Candidate instructions; EV E5 | yes |
| C6 | VALUE/ASSURANCE | Five-file payload installs coherently and preserves custom receiver files; helper remains optional | Receiver damage or unusable package | Init/update, pinned payload, standard library | Clean/custom local receiver | TS AC-6, TS §4 M2 | Candidate files; EV E6 | yes |
| C7 | TRACE | Exact approved selector and immutable baseline/plan precede Candidate; accepted result is reachable and isolated | Unauthorized scope or wrong result accepted | TS, dispatch, git history/accounting | Review checkout | TS §4, dispatch | Baseline `a669ff6e`, Candidate `83227789`, RF/EV | yes |
| C8 | VALUE/TRACE | Human acceptance authority and North Star purpose remain intact | Unaccepted result or tracking burden | HL contract, review/owner pre-close gates | This task | HL, TS AC-5 | Status/journal and Candidate workflows | yes |

## TS ↔ RF Alignment

| TS requirement | RF claim | Claim IDs | Aligned? |
|---|---|---|---|
| AC-1 | RF §3 complete | C1 | Claimed; verify |
| AC-2 | RF §3 complete | C2 | Claimed; verify |
| AC-3 | RF §3 complete | C3 | Claimed; verify |
| AC-4 | Implementation complete; final TEQM report deferred | C4 | Partial lifecycle, expressly deferred |
| AC-5 | Instructions complete; later gates deferred | C5/C8 | Partial lifecycle, expressly deferred |
| AC-6 | RF §3 complete | C6/C7 | Claimed; verify |
| DoF / safety | No unrelated source mutation or exposure claimed | C2/C6/C8 | Claimed; verify |

## Verification Selection

| Claim IDs | Planned check or reusable evidence | Why this depth | Known gap or limit |
|---|---|---|---|
| C1–C4 | Inspect helper/schema/rates; run task checks and independent numeric/edge probes against saved samples | Core resource numbers and dedup govern owner decisions | Live private source behavior is surface/version bounded |
| C5–C6 | Inspect exact diff and gate placement; compare installed copies; exercise receiver preservation evidence | Authority and data-loss floors | Final task-close effects have not occurred |
| C7 | Re-run literal NUL-safe Baseline→Candidate accounting and inspect history/status | Mandatory accepted-result identity and scope | None known |
| C8 | Check approved HL purpose, journal gates and relevant PV/knowledge citations | Human authority and purpose floor | Owner pre-close acceptance remains future |

## Deviations from TS

RF explicitly defers TEQM final economics/presentation and later DONE/cleanup. These are future Coordinator effects under AC-4/5, not claims of completed Executor work. No other deviation is asserted; verification may identify one.

## Checkpoint

**Self-check:**
- [x] Read RF §§1–5, governing TS AC/DoF, HL purpose/principles, ONB and referenced predecessors.
- [x] Mapped material claims and mandatory safety/security, authority and identity boundaries.
- [x] Bound claims to behavior/dependencies, environment, oracle and exact evidence identity.
- [x] Recorded replayable selection and known limits.
- [x] Avoided classification by file/count alone.

Stage complete: YES
