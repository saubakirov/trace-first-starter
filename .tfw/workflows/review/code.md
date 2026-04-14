# Review Mode: code

## Verify Actions
1. Open at least `min_verify_ratio` (default: 42%) of files from RF §1 (What Was Done) → verify changes exist and match description. On any discrepancy → escalate to 100%
2. Check RF §4 (Verification) → re-run at least 1 build/test command if possible
3. Cross-reference RF §3 (Acceptance Criteria) checkmarks against TS DoD
4. If "Tests pass" claimed → check test file exists and covers stated scenarios

## Mode-Specific Checklist Items
| # | Check | Description |
|---|-------|-------------|
| 7 | Code quality | Conventions, naming, type hints |
| 8 | Test coverage | Tests written and passing per TS |
| 9 | Security | No secrets exposed, guards in place |
| 10 | Breaking changes | API compat, backward compat, migrations |
