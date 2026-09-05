# EV — TFW_20260904-113200_VBSA / Phase B: Knowledge consolidation and lifecycle closure

> **Date**: 2026-09-05
> **Author**: Codex (Executor)
> **Task**: TFW_20260904-113200_VBSA
> **TS**: [TS Phase B](../TS__phase-b__knowledge_consolidation_and_lifecycle_closure.md)

---

## Environment

| Field | Value |
|---|---|
| OS | Microsoft Windows 11 Pro 10.0.26200, 64-bit |
| Language / Runtime | Python 3.13.5; Git 2.42.0.windows.1; PowerShell |
| Database | N/A |
| Deploy target | Local detached worktree rooted at `d0a2bfd3db696c3a32647bfc708aa5089ee18463` |
| CI / Pipeline | Local verification |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | Replacement Candidate `27f9d7e319cb32498675b1b44e9ad422cf177c4b` changes the exact VALUE selector once as `M KNOWLEDGE.md`. R2 supersedes the initial four-row arithmetic only: the diff has the required Config/D76/Phase-A/legacy effects plus one authorized D70 replacement, five hunks, `5` additions and `2` deletions. D75 and §4 are identical to Baseline. | Local Git, Baseline `9221dbb659a6b631dca3540b6be38d2a95208858` | VERIFIED | NUL-safe replay and row checks in §3.1; [KNOWLEDGE.md](../../../../../KNOWLEDGE.md) |
| E2 | AC-2 | Config states both soft VALUE prompts and the multiplier ceiling. D76 carries all four semantic classes, immutable Baseline→Candidate selection, both universal measures, excluded-only invariance, prospective bounded Coordinator authority, immutable denominator, and owner escalation. All cited sources resolve and support the row. | Candidate blob plus Phase A RF/REVIEW/EV and canonical config carriers | VERIFIED | Source matrix in §3.2; candidate rows in [KNOWLEDGE.md](../../../../../KNOWLEDGE.md) |
| E3 | AC-3 | The Phase A row reproduces approved TS, Baseline, final Candidate, 29 VALUE files, `663 + 321 = 984`, two ASSURANCE paths, no membership deviation, and final APPROVE. The legacy row names all four former keys, both mappings, both retired sublimits, multiplier `2`, prospective replacement, and historical preservation. | Candidate blob plus immutable Phase A RF/REVIEW/EV | VERIFIED | Source matrix in §3.2; 19/19 links across all checked rows resolve |
| E-accounting | AC-4 | Initial approval/Baseline `9221dbb659a6b631dca3540b6be38d2a95208858`; replacement Candidate `27f9d7e319cb32498675b1b44e9ad422cf177c4b`; selector `KNOWLEDGE.md`, action `M`, class VALUE because it is the accepted Phase B output; attribution Phase B, VALID; `1` logical file; `5` additions + `2` deletions = `7` touched text LOC; binary/non-text N/A count `0`; below `50`/`5,000` triggers and below `2`/`10` owner boundaries. R2 at `c0d3af39b770d024f0a0a9e82c2ea06e8008f360` prospectively authorized at most `9` LOC without ratcheting the immutable owner denominator `1/5`; D70 work and Candidate came later. Baseline→Candidate non-VALUE changes are declared task TRACE only; protected changes are zero. | Local Git, Python, and PowerShell checks | VERIFIED | Exact method and raw results in §3.1; Candidate parent `c0d3af39b770d024f0a0a9e82c2ea06e8008f360`; [R2 event](../journal/20260905-121325__ruling__16a2.md) |
| E5 | AC-5 | Executor acceptance is paired as `TS_DRAFT → ONB`; replacement Candidate precedes this EV, and Candidate→current HEAD has zero VALUE change. `ONB → RF` will be paired with RF filing. Independent `RF → REV → KNW`, marker application, and phase/root closure remain structurally future work forbidden to the Executor role. | Phase-local status/journal and Git lineage | DEFERRED | [status.md](../status.md); [acceptance event](../journal/20260905-115336__handoff__60f0.md); independent `/tfw-review` required |

### 3.1 Accounting, authority, and lineage replay

Approved literal selector and commands:

```powershell
$valuePaths = @('KNOWLEDGE.md')
git diff --name-status --find-renames=50% -z 9221dbb659a6b631dca3540b6be38d2a95208858 27f9d7e319cb32498675b1b44e9ad422cf177c4b -- $valuePaths
git diff --numstat --find-renames=50% -z 9221dbb659a6b631dca3540b6be38d2a95208858 27f9d7e319cb32498675b1b44e9ad422cf177c4b -- $valuePaths
```

Raw output, with NUL bytes rendered as `<NUL>`:

```text
M<NUL>KNOWLEDGE.md<NUL>
5<TAB>2<TAB>KNOWLEDGE.md<NUL>
```

Lineage and timing:

```text
initial_owner_approval=9221dbb659a6b631dca3540b6be38d2a95208858 @ 2026-09-05T00:47:07+05:00
superseded_candidate=1b336e1257a87e6552090f549cfa3381614ec6d2
R1=bf4a5d50bdbdd956db91d6b892915db5b83fb5dd
R2=c0d3af39b770d024f0a0a9e82c2ea06e8008f360
replacement_candidate=27f9d7e319cb32498675b1b44e9ad422cf177c4b @ 2026-09-05T12:23:50+05:00
replacement_parent=c0d3af39b770d024f0a0a9e82c2ea06e8008f360
candidate_own_paths=M KNOWLEDGE.md
candidate_to_EV_VALUE_paths=0
protected_path_changes=0
section4_equal=true
D75_equal=true
binary_or_non_text_VALUE=0
derived_index_changes=0
```

The first Candidate exposed two ceiling failures. R1 was recorded before any proposed D75 edit, and the
Executor stopped after proving that target impossible. R2 superseded only the subtraction target and was
recorded before D70 changed. The final D70 replacement is one necessary same-result constituent, `7 < 10`,
with unchanged membership and protected boundaries. The immutable approval denominator remains `1/5`.

Baseline→replacement Candidate contains one VALUE path plus only the already approved root-HL A11 and
Phase B HL/TS/ONB/status/journal TRACE paths. The replacement Candidate's own diff contains only the
authorized D70 line in `KNOWLEDGE.md`.

### 3.2 Source-to-row matrix

| Candidate row | Source facts replayed | Result |
|---|---|---|
| Config | `.tfw/project_config.yaml` lines 29–31: `50`, `5000`, `2`; template, conventions §6, and config workflow carry the same keys and migration | VERIFIED |
| D76 | Phase A RF §§1–2 and final REVIEW §§17–20 fix the classes, selector, measures, Candidate invariance, and authority boundary; Phase A EV Pass 2 reproduces them | VERIFIED |
| `TFW_20260904-113200_VBSA/A` | Phase A RF §1.2 binds `36e50e4…`, `f5a96af…`, `59c73bf…`, 29 files, `663 + 321 = 984`, two ASSURANCE paths, and no deviation; final REVIEW records APPROVE at `9221dbb…` | VERIFIED |
| Former whole-diff model | Phase A RF, final REVIEW, EV, and master-HL A9 establish the four old keys, two forward mappings, retirement of two redundant sublimits, multiplier `2`, and immutable history | VERIFIED |

All 11 artifact links in the four required rows resolve. No source, Phase A Candidate, historical artifact,
canonical carrier, test, generated mirror, or remote was modified.

### 3.3 R2 D70 retention proof

Read-only simulation before edit measured D70 `429 → 214` words and `/tfw-plan`
`24,935 → 24,720 ≤ 24,730`. Candidate replay returns the same `214` and `24,720` values. D75 is
byte-identical to Baseline. All five original D70 link destinations remain identical and resolve.

| Retained D70 content | Candidate observation | Result |
|---|---|---|
| Bold decision | “An update neither guesses nor decides for the owner.” | VERIFIED |
| Source pin | Operator-named tag; derive `source_head` from `target_ref`; read `VERSION` at that commit; match tag name; never source `HEAD` | VERIFIED |
| Owner gate | Before first durable write, exactly actor/task containers/verification in one AG message; identity is not inferred from Git, OS, or upstream profiles | VERIFIED |
| Briefing | `content_language`; CHANGELOG `Added`/`Changed`/`Fixed`/`Removed`; no free text; template named | VERIFIED |
| Payload boundary | Both project-owned state files excluded; skips printed; exclusion test derived from payload | VERIFIED |
| Update/release route | Target's `update.md` first; every earlier live tag reachable; reversed norms quoted; `Superseded by` marker retained | VERIFIED |
| Status/phase rule | Whole-cell grammar; second declared token or Unicode `So` refuses; `UNDECLARED` remains verbatim/nonterminal with signals; every phase directory named and state hand-authored | VERIFIED |
| Abbreviation | Initials of approved title, proposed and approved with the title, never silently | VERIFIED |
| Rationale and measurement | Live-source pin, inferred choices, overwritten config, misclosed live multiphase task/stateless phases, titleless `UPD`; `So` selected over all `S` from 114 rows because `+`/`→` false refusals teach overrides | VERIFIED |
| Provenance | RF, REVIEW, ONB §3 Q1, HL A6/A7, fourth and fifth field reports remain linked | VERIFIED |

All 19 links across Config, D70, D75, D76, Phase A, and legacy rows resolve.

### 3.4 Verification record

| Check | Result |
|---|---|
| Semantic/accounting validator | PASS: exact membership, five ruled effects, source tokens, D75/§4 equality, 19 resolved links, zero protected paths |
| Exact former ceiling tests | PASS: `2 passed in 25.34s` |
| Full tracked suite: `python -m pytest .tfw/scripts/ docs/scripts/ -q` | PASS: `562 passed, 1 skipped in 250.38s` |
| `/tfw-plan` graph | PASS: `24,720 ≤ 24,730` |
| `git diff --check 9221dbb… 27f9d7e…` | PASS |
| `python .tfw/scripts/gen_index.py --check project` | PASS: framework `2.1.0`, one participant, project consistent with declared release |

## Verdict

Evidence verdict: 4/5 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A

---

*EV — TFW_20260904-113200_VBSA / Phase B: Knowledge consolidation and lifecycle closure | 2026-09-05*
