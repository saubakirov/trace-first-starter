# EV — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption

> **Date**: 2026-09-04
> **Author**: saubakirov via codex
> **Task**: TFW_20260904-113200_VBSA
> **TS**: [TS Phase A](../TS__phase-a__value_bearing_budget_contract_and_adoption.md)

---

## Environment

| Field | Value |
|---|---|
| OS | Windows; repository-local PowerShell |
| Language / Runtime | Python 3.13; pytest |
| Database | N/A — documentation/runtime contract has no database |
| Deploy target | Local Git worktree |
| CI / Pipeline | Local commands |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | Source-derived four-class contract, semantic precedence fixtures, and classification mutant | pytest, local | VERIFIED | python -m pytest docs/scripts/test_runtime_context.py -q -k vbsa → 20 passed |
| E2 | AC-2 | Baseline/Candidate invariance, NUL-safe rename/binary handling, and three exact phase-attribution routes | pytest, local | VERIFIED | targeted accounting/Candidate/attribution command → 6 passed |
| E3 | AC-3 | Exact three-key configs, forward migration, history preservation, update/init behavior, and release gate | pytest + MkDocs, local | VERIFIED | targeted config/migration/release/update/init command → 9 passed; full suite repeated the final sources |
| E4 | AC-4 | Prospective authority, immutable denominator, local quotation placement, and foreign North-Star byte preservation | pytest + MkDocs, local | VERIFIED | targeted authority/Saint/North-Star command → 4 passed; D75 selective-read regression also passed |
| E5 | AC-5 | Candidate-before-trace workflow plus RF and exactly one EV accounting carrier | pytest, local | VERIFIED | targeted handoff/RF/EV command → 2 passed |
| E6 | AC-6 | Reviewer independently replays and never repairs accounting or supplies late authority | pytest, local | VERIFIED | targeted review command → 1 passed |
| E7 | AC-7 | Complete runtime and integration regression, project structure, adapter parity, YAML, Python syntax, and whitespace | pytest/Git/index, local | VERIFIED | 553 passed, 1 skipped; gen_index --check project exit 0; git diff --check exit 0; 12 copies byte-identical |
| E-accounting | AC-8 | Approval 36e50e4a362d474550f26e58defe56132b5417be; Baseline f5a96af07dcdc4230ecf31100bd155a3dca09604; Candidate edb0017bd0c1d33eafbf99ee2b9c841e2fd91b2f; approved literal selector has 29 paths and actual membership is the same 29 paths, all action M, class VALUE, with each semantic reason bound to its approved TS row; phase attribution VALID to Phase A; 657 additions + 318 deletions = 975 touched text LOC; 29 logical files; no binary/non-text N/A; approved keep-one-phase disposition remains terminal; 29/975 is below 50/5000 and below Owner boundary 58/2200; REVIEW §8 authorized the bounded round before work; required tests preceded Candidate and this EV follows it; exact method is in the Round 1 reproduction below | Git, local | VERIFIED | selector_count=29; changed_logical_files=29; selector_equals_membership=true; phase_attribution=VALID; HC-1 protected changes=0 |

## Accounting reproduction — initial delivery

The literal VALUE selector was extracted from the Class column of the approved TS at
36e50e4a362d474550f26e58defe56132b5417be:

    $valuePaths = @(
      '.tfw/README.md',
      '.tfw/conventions.md',
      '.tfw/glossary.md',
      '.tfw/project_config.yaml',
      '.tfw/workflows/plan.md',
      '.tfw/workflows/handoff.md',
      '.tfw/workflows/review.md',
      '.tfw/workflows/config.md',
      '.tfw/workflows/update.md',
      '.tfw/workflows/init.md',
      '.tfw/templates/TS.md',
      '.tfw/templates/RF.md',
      '.tfw/templates/REVIEW.md',
      '.tfw/templates/evidence/EV.md',
      '.tfw/templates/project_config.yaml',
      '.tfw/CHANGELOG.md',
      'RELEASE.md',
      '.agent/workflows/tfw-plan.md',
      '.agent/workflows/tfw-handoff.md',
      '.agent/workflows/tfw-review.md',
      '.agent/workflows/tfw-config.md',
      '.agent/workflows/tfw-update.md',
      '.agent/workflows/tfw-init.md',
      '.claude/commands/tfw-plan.md',
      '.claude/commands/tfw-handoff.md',
      '.claude/commands/tfw-review.md',
      '.claude/commands/tfw-config.md',
      '.claude/commands/tfw-update.md',
      '.claude/commands/tfw-init.md'
    )
    git diff --name-status --find-renames=50% -z f5a96af07dcdc4230ecf31100bd155a3dca09604 6dce719338fece2601c1e1ce770273a1bb87c441 -- $valuePaths
    git diff --numstat --find-renames=50% -z f5a96af07dcdc4230ecf31100bd155a3dca09604 6dce719338fece2601c1e1ce770273a1bb87c441 -- $valuePaths

The name-status stream contains 29 M records and no other action. The numstat stream sums to
634 additions and 318 deletions. A separate source-derived parser reproduced the approved selector,
membership equality, arithmetic, trigger result, and authority boundary.

Candidate is the first immutable implementation commit after all required VALUE and ASSURANCE work and
the successful targeted/full tests. Its parent is 3c799770b83b1942a88e2426845f89629772c309.
Candidate contains exactly the 31 approved implementation paths. EV, RF, phase status, and the final
journal event are later TRACE and do not move it.

## Known baseline observation

python .tfw/scripts/gen_index.py --check tasks still reports the immutable historical
workspace/2026/TFW_20260902-112841_RDP journal summary at 123 code points against the 120 ceiling.
This is the approved baseline defect, outside HC-1, and was not modified. Informational legacy phase-state
notes do not affect the command's exit code.

## Verdict

Evidence verdict: 8/8 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## Round 1 Return Evidence

| Finding | Produced behavior | Adverse mutant | Result |
|---|---|---|---|
| Planner canonical route | /tfw-plan graph loads Semantic value-bearing classification, Value-bearing accounting contract, and Decomposition, constraints, and change authority as three unique source ranges; active context is 24,729 against unchanged ceiling 24,730 | Meaning reversal changes the derived contract before rejection; missing route changes the graph before rejection | VERIFIED |
| Receiver North-Star preservation | Init/update operation tables are parsed and executed against controlled tmp_path receivers; root README.md, .tfw/README.md, and historical TS bytes remain exact | PRESERVE_BYTES→OVERWRITE_FROM_STARTER changes both North-Star byte outputs before policy rejection | VERIFIED |
| EV Result vocabulary | Both template Result cells derive exactly VERIFIED / DEFERRED / BLOCKED / N/A; phase-attribution INVALID is present only in accounting detail | Fifth-status mutation changes the parsed Result vocabulary before rejection | VERIFIED |

Commands and results:

- targeted VBSA plus D75 round checks: 26 passed;
- controlled receiver/North-Star/adapter checks: 10 passed;
- complete runtime context suite: 154 passed;
- full framework/docs suite: 559 passed, 1 skipped;
- gen_index --check project, Python compile, git diff --check, and changed-adapter byte parity: passed.

### Round 1 accounting reproduction

The VALUE path array is unchanged from the approved TS and the initial reproduction above. The same
commands were rerun with the new Candidate:

    git diff --name-status --find-renames=50% -z f5a96af07dcdc4230ecf31100bd155a3dca09604 edb0017bd0c1d33eafbf99ee2b9c841e2fd91b2f -- $valuePaths
    git diff --numstat --find-renames=50% -z f5a96af07dcdc4230ecf31100bd155a3dca09604 edb0017bd0c1d33eafbf99ee2b9c841e2fd91b2f -- $valuePaths

The source-derived replay returned 29 M records, selector_equals_membership=true, 657 additions,
318 deletions, 975 touched text LOC, no binary N/A, trigger_crossed=false, and
owner_ceiling_reached=false. Candidate is the first tested Executor VALUE commit for the returned round;
its parent is a1afe36b8396029e22153a224774ea5eb4cd7f6b and its own 13-path diff is contained by the
approved 31-path implementation selector. Round EV/RF/status/journal writes follow Candidate and do not
move it.

Round verdict: 3/3 returned findings VERIFIED; accounting VERIFIED with the single E-accounting row.

---

*EV — TFW_20260904-113200_VBSA / Phase A: Value-bearing budget contract and adoption | 2026-09-04*
