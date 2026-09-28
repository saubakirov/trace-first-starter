# Map — TFW_20260928-015408_ATC

> RF: [RF__TFW_20260928-015408_ATC.md](../RF__TFW_20260928-015408_ATC.md) @ `ed23e0c16a0675745a8d7d777ce40387ac85007c`  
> TS: [TS__TFW_20260928-015408_ATC.md](../TS__TFW_20260928-015408_ATC.md) @ `772d5773ba92e5534579cfd0e9152619a4261554`  
> Candidate: `7dfed8bf5350e10f889f66c606a672a52e88f9a3`; Baseline: `84cedfab42ebd5070230bc5c7370d6ac88dd3796`.

## Understanding

The accepted result is an A plus B/V task coordination contract across 23 VALUE paths and one existing ASSURANCE fixture. A single task Coordinator advances a one-phase task; bounded phase Coordinators and a safe successor serve long work while the human retains reserved decisions. The result claims canonical and installed entry parity, a dual-readable status schema, local route probes, fixed accounting and limited receiving evidence; live external activation and idle-parent wake are explicitly unobserved.

## Accepted Claims and Boundaries

| ID | Layer | Accepted claim / authority boundary | Risk or concrete harm | Affected behavior / dependencies | Relevant environment | Oracle / authority | Evidence identity (`subject@revision`, source) | Required? |
|---|---|---|---|---|---|---|---|
| C1 | VALUE | Six-role purpose, value and authority map; no new GATEWAY/LEAD | Duplicate hierarchy or lost human judgment | Canonical coordination, glossary, HL/status templates, profiles | Current project and new-work entry | HL §§1, 3–7, 10; TS AC-1 | 23-path Candidate; RF §1, EV E1 | yes |
| C2 | VALUE | One-phase, sequential, parallel and successor next actions have a responsible actor, route and pending condition | Silent owner babysitting, unbounded context or self-grant | Plan, conventions, status, selected profiles | Current canonical workflow | TS AC-2/DoF; frozen HL purpose | Candidate; RF §3, EV E2/scenario trace | yes |
| C3 | VALUE / ASSURANCE | New root/phase `upstream_route`, valid old `owner_gateway`, exact parent refusal | Misrouted gates or broken active tasks | Status template, `tools/tfw_state.py`, fixture, active task status | Python 3.13.5 and actual old carrier | TS AC-3; approved carrier epoch | Candidate; EV E3/probe | yes |
| C4 | VALUE / TRACE | Role gates return vertically; independent Reviewer and phase returns remain separate | Peer bias, unreturned transcript dependence or lost verdict | Review/Plan workflows, roots, native addressed send | Codex current project; Claude/Antigravity source only | TS AC-4; status `coordinator_route` | Candidate; Executor ONB gate and Reviewer dispatch @ `4bb6ac35d87796cf27292fa3bb5db0a4fb712755` | yes |
| C5 | VALUE / ASSURANCE | Canonical and receiver copies agree, with honest capability limits | Receivers act from stale rules or unsupported wake is claimed | Installed roots, Claude commands, provider profiles, receiving probe | Current checkout and file-backed copied receiver | TS AC-5; byte parity and actual receiving inspection | Candidate; EV E5, `receiving_probe.json` | yes |
| C6 | ASSURANCE / TRACE | Exact 23-path VALUE membership, LOC, tokens, approval order and fixed Candidate | Unreviewable cost, late denominator or false identity | Git history, accounting JSON, TS selector | Immutable Baseline/Candidate blobs | TS §4/AC-6; approved denominator | Baseline/Candidate; EV E-accounting, RF §1 | yes |
| C7 | VALUE / TRACE | Host identity, MCP and release/merge remain outside Candidate and owner authority | Unapproved scope or external effect | Full diff, separate proposal, status/dispatch | Local repo | TS AC-7; HL A1 reservations | Candidate diff; RF §3, EV E7 | yes |
| C8 | TRACE / ASSURANCE | Post-review presentation, final acceptance, release and merge remain Coordinator/owner obligations | Premature DONE or false completion | RF deferred AC-6; REVIEW and task lifecycle | Current task | TS AC-6; status/journal routing | RF §5 and task status @ Reviewer entry | yes |

Mandatory floors: C3/C4/C7 cover safety, security and human authority; C6 covers accepted-result identity. No deployed security boundary is claimed beyond the local workflow and route rules.

## TS ↔ RF Alignment

| TS requirement | RF claim | Claim IDs | Aligned? |
|---|---|---|---|
| AC-1; HL purpose and role model | RF §§1, 3; EV E1 | C1 | partial until independent purpose check |
| AC-2 | RF §§1–3; EV E2 | C2 | partial until scenario trace inspection |
| AC-3 | RF §§1, 3–4; EV E3 | C3 | partial until route probe replay |
| AC-4 | RF §§3–5; EV E4 | C4 | partial: Reviewer return still owed |
| AC-5 | RF §§3–5; EV E5 | C5 | partial: source parity and file-backed probe only; live receiving activation/wake unobserved |
| AC-6 | RF §§1, 3, 5; EV E6/accounting | C6, C8 | partial: owner-facing post-review presentation owed |
| AC-7 | RF §§1, 3; EV E7 | C7 | partial until independent diff scope check |
| DoF: no silent wait, self-grant, extra role, collapsed review, false wake, missing approval | RF limitation and authority claims | C1–C8 | partial until Verify/Judge |

## Verification Selection

| Claim IDs | Planned check or reusable evidence | Why this depth | Known gap or limit |
|---|---|---|---|
| C1, C2, C4 | Inspect all affected canonical/installed role and route changes; trace four cases | Normative cross-file behavior and mandatory authority floor | Text cannot prove provider wake |
| C3 | Inspect parser and template; replay required positive and refusal probes on immutable Candidate | Wrong-parent and legacy breakage are material | Parser cannot authenticate consent |
| C5 | Recheck source/receiver parity; inspect receiving probe inputs and limits; run relevant existing command-entry check | Receiver mismatch can defeat entry | No live external agent activation |
| C6 | Recompute NUL-safe 23-path numstat and tokenizer totals from exact blobs; verify approval and Candidate order | Immutable denominator and result identity are mandatory | File tokens are not runtime context usage |
| C7, C8 | Full changed-path and external-effect scan; inspect owner reservations and deferred presentation route | Mandatory safety, human authority and acceptance floor | Final owner presentation occurs after REVIEW |

## Deviations from TS

RF names no additional VALUE path and one TS-authorized ASSURANCE fixture. AC-6's owner-facing comparison is deferred to the Coordinator after independent review; this is an owed next act, not yet an implementation deviation. Live receiving-agent activation and idle-parent wake are unobserved and must not be treated as verified runtime outcomes.

## Checkpoint

**Self-check:**
- [x] Read RF §§1–5, TS AC/DoF, HL purpose/principles, ONB and referenced research/selection lineage relevant to this result.
- [x] Mapped every material accepted claim and mandatory safety/security, authority and result-identity boundaries.
- [x] Bound each claim to behavior, environment, oracle and exact revision/evidence identity.
- [x] Recorded a replayable verification selection and known gaps.
- [x] Avoided classifying by artifact or discrepancy count.

Stage complete: YES
