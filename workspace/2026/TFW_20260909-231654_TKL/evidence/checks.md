# Actual check evidence

Final tested Candidate: `27cdb701b91c5b45b9f54b3e98c9ad67635b3e30`. Final full run `13-full` used Python 3.13.5 from
`E:/TEMP/pttc-phase-a-b9b5/venv/Scripts/python.exe`, pytest 8.4.2, PyYAML 6.0.3,
MkDocs 1.6.1 and Material 9.7.6. Windows host and the actual cwd/argv/timestamps are in each receipt.
The default Python/pytest 9 environment was not used for the suite. No receiver runtime is imposed.

**Final result: 636 passed, 1 inherited skip; production MkDocs exit 0.** Collection reports 637.
`13-full` began `2026-09-13T11:03:37.090124+00:00`, finished `11:12:14.816977+00:00`;
wrapper time 517.729644 seconds, pytest 516.88 seconds. All captured source inputs stayed unchanged.
[Exact Candidate binding and NUL-safe accounting](accounting/candidate-27cdb70/accounting.json)
compares each of the 58 VALUE and seven ASSURANCE raw tested inputs through the actual Git filters
to the immutable Candidate. Raw working CRLF and normalized Git objects are separately identified.

| Actual epoch | Exit | Original final stdout line |
|---|---:|---|
| [01-collection](checks/01-collection/receipt.json) | 0 | 590 tests collected in 1.22s |
| [02-affected](checks/02-affected/receipt.json) | 1 | 33 failed, 444 passed in 290.23s (0:04:50) |
| [03-current-contracts](checks/03-current-contracts/receipt.json) | 1 | 1 failed, 32 passed, 319 deselected in 3.91s |
| [04-tkl-gates](checks/04-tkl-gates/receipt.json) | 1 | 1 failed, 32 passed, 476 deselected in 2.71s |
| [05-collection](checks/05-collection/receipt.json) | 0 | 623 tests collected in 0.32s |
| [06-full](checks/06-full/receipt.json) | 1 | 1 failed, 621 passed, 1 skipped in 510.06s (0:08:30) |
| [07-collection](checks/07-collection/receipt.json) | 0 | 623 tests collected in 0.60s |
| [08-full](checks/08-full/receipt.json) | 0 | 622 passed, 1 skipped in 512.49s (0:08:32) |
| [09-remaining-gates](checks/09-remaining-gates/receipt.json) | 0 | 14 passed, 201 deselected in 0.48s |
| [10-collection](checks/10-collection/receipt.json) | 0 | 637 tests collected in 0.26s |
| [11-full](checks/11-full/receipt.json) | 0 | 636 passed, 1 skipped in 509.30s (0:08:29) |
| [12-collection](checks/12-collection/receipt.json) | 0 | 637 tests collected in 0.48s |
| [13-full](checks/13-full/receipt.json) | 0 | 636 passed, 1 skipped in 516.88s (0:08:36) |

Every row resolves to original stdout/stderr, source-before snapshot/archive where captured, and a
receipt. Initial `01-02-source-before-corrections` was observed during run 02 at 10:20:40.956326 UTC,
not as a pre-run or pre-adoption seal. Later source-before epochs record their own actual inputs.
Since run 07 each run also preserves its invoked capture script and start/end HEAD; actual build
streams and receipt are under the run's build directory. The TRACE-only ONB commit during run 06
changes no tested input and is not a concealed source-generation replacement.

## Original failures and corrections

- Run 02: 33 failures / 444 passes exposed old live-API and retired normative expectations after the
  approved behavior changed. Existing historical digest/threshold vectors remain, executed against
  exact immutable Baseline source; current production APIs are not restored to satisfy old tests.
- Run 03: one failure was an accidental broad replacement of the fixture filename with
  `knowledge_legacy_state.yaml`; restored the original `knowledge_state.yaml` name.
- Run 04: one new gate assertion passed an output prefix without the required trailing slash;
  corrected that assertion input. The original failed run remains.
- Run 06: one remaining graph expectation still required a global pending source; projected the
  separately declared current selected-source expectation while retaining the historical oracle.
- Runs 08 and 11 passed their then-current inputs. Later finite case coverage and the final current
  Architecture Map wording justified the subsequent relevant checks/full run. Run 13 is the final
  immutable Candidate input generation; prior passes are not substituted for it.

The sole skip is `tools/tests/test_migrate_board_2_0.py::test_repository_accounting_balances`, whose
existing lines 553–554 skip after BOARD removal and point to BOARD-SNAPSHOT.md. It is inherited,
not an added waiver. Build success coexists with inherited historical/site-only diagnostics in the
raw stderr; it is not a clean whole-corpus-link claim.

## Assurance interpretation limits

The seven modified test homes preserve their historical source epochs while checking the selected
new contract. Runtime-context and update-cut cases are explicit source guards/interpretation models,
not native command-following, observed crashes, actual clean Full init or a first consumer answer.
Actual four-adapter install/repeat checks use the supported installation paths; source parity proves
those copies and routes, not universal behavior. Doctor tests deny obsolete-state/corpus reads and
invoke the retired command as a real subprocess. Resolver/integration tests check exact destinations
and repeated transformation; the resolver implementation itself is unchanged.

Raw checks/navigation/native inputs were committed with per-command `core.autocrlf=false`; every
committed evidence blob equals its original raw file. Their staged whitespace checks reported
exit 2 on preserved raw material (including CRLF and generated HTML), which was intentionally not
normalized or reformatted. Product Candidate's staged whitespace check passed. Those raw-preservation
commits are excluded TRACE and do not change Candidate or test outcomes.
