# EV — TFW_20260902-111644_CRATM / Phase B: Named principals

> **Date**: 2026-09-06
> **Author**: Codex (Executor, acting as `saubakirov`)
> **Task**: TFW_20260902-111644_CRATM
> **TS**: [TS Phase B](../TS__phase-b__named_principals.md)

---

## Environment

| Field | Value |
|---|---|
| OS | Microsoft Windows 11 Pro 10.0.26200 build 26200 |
| Language / Runtime | Python 3.13.5; PyYAML 6.0.3; Git 2.42.0.windows.1; pytest 9.0.2; MkDocs 1.6.1 |
| Database | N/A — Markdown/Git protocol change has no database surface |
| Deploy target | N/A — repository-local framework documentation |
| CI / Pipeline | Local detached Git worktree and local configured checks |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | The profile contract keeps the original four required human keys, makes both role fields optional for both profile types, accepts a non-empty description or exact `not_applicable`, and defines omission as unknown/not supplied. The unchanged real `team/saubakirov.md` parsed with exactly `handle`, `name`, `since`, and `type`; its Baseline→Candidate diff is empty. Contract fixtures for a four-key human, omitted roles, and `not_applicable` all passed. Roles are explicitly non-authenticating and non-authoritative. | Candidate Markdown; Python/PyYAML fixture gate | VERIFIED | [Profile template](../../../../../.tfw/templates/team/profile.md); fixture matrix and commands below: 17/17 PASS; real-profile parse PASS |
| E2 | AC-2 | An agent requires `accountable_to` resolving directly to a human plus exact YAML Boolean `true` or `false`; provider/model/process/session/workflow-role identity is forbidden. Ruler and worker examples carry separate stable handles and opposite grants; changing a grant requires a new profile. Optional non-empty mentality is descriptive only. Valid ruler, worker, and mentality fixtures passed; missing-human, agent-to-agent, quoted-`"true"`, `yes`, and `sometimes` fixtures were rejected. No workflow, adapter, skill, or `AGENTS.md` consumes any new profile field, so Phase C routing and permission behavior were not introduced. | Candidate Markdown; Python/PyYAML and ripgrep | VERIFIED | [Canonical principal contract](../../../../../.tfw/conventions.md#declared-participants-and-principals); [profile examples](../../../../../.tfw/templates/team/profile.md); `rg` consumer search below returned no matches |
| E3 | AC-3 | Current events may use optional `writer` for a declared human or valid agent while `on_behalf_of` remains human, `via` remains tool text, and the filename token remains uniqueness only. Human-writer and agent-writer fixtures passed; a writer guessed from `via` was rejected; legacy `actor` input passed unchanged. All 28 Baseline journal files containing `actor:` exist at Candidate with identical blobs. `gen_index.py` and both relevant test files are byte-identical. Governing-source search found no blocking reporter/validator invocation: only two explicit report-only comments. Baseline and Candidate `--check tasks` each returned the same one foreign RDP summary-length problem and the same informational stateless-phase count; delta is empty. | Immutable Git refs; Python/PyYAML; ripgrep; report-only diagnostic | VERIFIED | [Event template](../../../../../.tfw/templates/journal/event.md); actor/reporter hashes and diagnostic output below |
| E4 | AC-4 | The one-job binding selects either a declared human or valid agent by one absolute project-root mapping and contains no authority, mentality, fallback, default, liveness, device, or provider data. An external Windows-path agent binding fixture passed and a top-level `authority` key was rejected. One-profile silent resolution, multi-profile binding, and one-question invalid/shared/copied handling remain canonical. Neither documented real binding path existed before or after the fixture; the fixture remained in memory and created no file. | Candidate Markdown; in-memory Python/PyYAML fixture; real filesystem existence checks | VERIFIED | [Binding template](../../../../../.tfw/templates/bindings.yaml); fixture matrix and external-state checks below |
| E5 | AC-5 | Candidate contains exactly four modified VALUE paths; the complete Baseline→Candidate set adds only authorized Phase B TRACE. No code, config, test, workflow, adapter, other phase/task, existing profile/event, or external state changed. Phase A commit/worktree/staging/landing and D79 Session identity ranges have identical SHA-256 hashes at both refs. Exact word counts are: `conventions.md` 10,547→10,854 (+307), `profile.md` 380→371 (-9), `event.md` 339→353 (+14), and `bindings.yaml` 452→465 (+13); every template remains below 1,200 words. The conventions growth is the minimum shared contract: a template-only form would leave event and binding checkpoints without canonical principal semantics. The first full suite exposed four retained-context compatibility regressions (attention reduction, two journal semantics checks, and `/tfw-init` cap); the wording was compressed within the approved four paths before Candidate. Final checks: 630 tests collected; 629 passed, 1 skipped in 319.54 s; project check passed; `git diff --check` passed; MkDocs built successfully in 112.70 s with existing historical-reference and third-party advisory warnings only. | Immutable refs and full local suite | VERIFIED | Candidate `0ee39046b760d6d3e8d837c2377e49c1c95668bd`; commands/results below |
| E-accounting | AC-6 | Dependency Baseline is `a048b2db5f44f5d748f22f3a0133f4ecf0acd9c4`; approved planning content is `b1cb7b0374703d87f76d9c8de67bbef264cddcc5`; owner approval is recorded by descendant `1e2631bff51b3b62673808d5de57f812883d814b`; both precede Candidate. Candidate `0ee39046b760d6d3e8d837c2377e49c1c95668bd` was committed 2026-09-06T10:17:51+05:00 as the first tested Executor VALUE commit, after ONB and before EV/RF/REVIEW/RF state. Literal membership, all `M`/VALUE: `.tfw/conventions.md` 41+13 (shared principal/event/binding contract), `.tfw/templates/bindings.yaml` 18+16 (principal selection), `.tfw/templates/journal/event.md` 14+11 (writer/legacy composition), `.tfw/templates/team/profile.md` 70+32 (human/agent schema). Totals: 4 logical text files; 143 additions + 72 deletions = 215 touched LOC; binary/non-text N/A. Phase attribution is wholly Phase B; `INVALID` does not apply. Trigger disposition: **keep one phase**, because 4<50, 215<5,000, and the four owners form one usable identity path. Actual membership equals the immutable 4-file plan and 215 is below the immutable 240-LOC denominator and owner ceilings 8 files/480 LOC; no zero grew, HC-B1 did not move, and no new ruling was needed. Exact NUL-safe commands below exited 0 and returned four `M` records plus the stated numstat. | Git 2.42.0 in the real detached worktree | VERIFIED | Governing [TS §4](../TS__phase-b__named_principals.md#4-affected-files-and-value-bearing-accounting); exact replay below |

`E-accounting` reproduces the approved TS selector. It does not define one, move Candidate, ratchet the
denominator, or supply late authority.

### Fixture inputs and results

The exact shell form was an in-memory PowerShell here-string passed to PyYAML with
`$validator | python -`; no fixture file or external binding was written. The validator enforced the
documented key sets, handle pattern, human-only direct accountability, lexical unquoted Boolean,
declared writer, and single top-level `bindings` map. These were the complete YAML inputs (the compact
mapping notation is YAML-equivalent to the multi-line strings supplied):

| Fixture | Exact input | Expected / observed |
|---|---|---|
| unchanged four-key human | `{handle: alice, name: Alice, type: human, since: 2026-09-06}` | accept / PASS |
| roles omitted | `{handle: worker, name: Worker, type: agent, since: 2026-09-06, accountable_to: alice, may_rule_amendments: false}` | accept / PASS |
| exact not-applicable | `{handle: ruler, name: Ruler, type: agent, since: 2026-09-06, organization_role: not_applicable, accountable_to: alice, may_rule_amendments: true}` | accept / PASS |
| ruler | `{handle: ruler, name: Ruler, type: agent, since: 2026-09-06, accountable_to: alice, may_rule_amendments: true}` | accept / PASS |
| worker | `{handle: worker, name: Worker, type: agent, since: 2026-09-06, accountable_to: alice, may_rule_amendments: false}` | accept / PASS |
| descriptive mentality | worker input plus `mentality: critical opponent` | accept / PASS |
| missing human | agent input with `accountable_to: missing` | reject / PASS |
| agent-to-agent | agent input with `accountable_to: ruler` | reject / PASS |
| quoted grant | agent input with `may_rule_amendments: "true"` | reject / PASS |
| YAML synonym grant | agent input with `may_rule_amendments: yes` | reject / PASS |
| arbitrary grant | agent input with `may_rule_amendments: sometimes` | reject / PASS |
| human writer | `{on_behalf_of: alice, writer: alice, via: codex}` | accept / PASS |
| agent writer | `{on_behalf_of: alice, writer: worker, via: codex}` | accept / PASS |
| writer inferred from tool | `{on_behalf_of: alice, writer: codex, via: codex}` | reject / PASS |
| legacy actor | `{on_behalf_of: alice, actor: robot-v1, via: codex}` | accept unchanged / PASS |
| external-path binding | `{bindings: {'C:\\work\\project': worker}}` | accept / PASS |
| authority-bearing binding | `{bindings: {'/work/project': worker}, authority: true}` | reject / PASS |

Output ended with `RESULT 17/17 passed`. Separately:

```text
PASS unchanged team/saubakirov.md four-key human: ['handle', 'name', 'since', 'type']
baseline_candidate_blob_unchanged_exit=0
windows=C:\Users\c0rpa\AppData\Local\tfw\bindings.yaml exists=False
posix=C:\Users\c0rpa\.tfw\bindings.yaml exists=False
```

### Compatibility, corpus, and boundary results

```text
principal-field consumer search:
  rg -n 'organization_role|project_role|accountable_to|may_rule_amendments|mentality' \
    .tfw/workflows .tfw/adapters .agents/skills AGENTS.md
  exit 1; no matches

governing reporter/validator search:
  .tfw/project_config.yaml:136: report-only comment; nothing gates on it
  .tfw/templates/project_config.yaml:146: no verify key; report-only comment
  no workflow, adapter, skill, or command receiver match

unchanged excluded blobs (Baseline = Candidate):
  .tfw/scripts/gen_index.py              1c86c69ba879e2a91ab2bb7ceae7d6892fbaee64
  .tfw/scripts/test_gen_index.py         bd658230a0f1909252d980ffcec59154529812ba
  docs/scripts/test_runtime_context.py   321dd03be899d18a92432bf6259b6ea9241dd977

legacy actor corpus:
  git grep -Il 'actor:' <Baseline> -- ':**/journal/*.md'
  actor_files=28 mismatches=0

report-only baseline and Candidate (both exit 1):
  workspace/2026/TFW_20260902-112841_RDP/journal/
    20260902-181437__amendment_escalated__531a.md:
    summary is 123 code points, ceiling is 120
  1 problem(s) across 63 tasks
  17 phase directories under 6 task(s) carry no state file; informational, exit unaffected
  diagnostic delta: none

preserved ranges (Baseline = Candidate SHA-256):
  D79 Session identity: a7d9d69c3bccb389b57f9e583fd6542a5bbe4235b766e0ecd693044d4aa6cd06
  Phase A commit/worktree/staging/landing:
    ea39c941d17fd5f3100fb81b41e136a0c1101275cb1f0a40d367693f5579cb80
```

The complete Baseline→Candidate path list is the four VALUE paths plus
`phase-b/{HL,TS,ONB,status,journal/*}` TRACE. Candidate's own commit contains only the four VALUE paths.
Added routing-related words occur only in the prohibitions “creates no route” and “no route or
permission”; manual diff inspection found no recipient algorithm, team mode, Role Assignment,
autonomous-from semantics, or provider profile.

### Test and accounting replay

```text
python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only
  630 tests collected; exit 0

python -m pytest .tfw/scripts/ docs/scripts/ -q
  629 passed, 1 skipped in 319.54s; exit 0

python .tfw/scripts/gen_index.py --check project
  project is consistent with the release it declares; exit 0

python -m mkdocs build --config-file docs/mkdocs.yml
  documentation built in 112.70s; exit 0

git diff --check <Baseline> <Candidate> -- <four literal VALUE paths>
  exit 0
```

Exact accounting replay:

```powershell
$valuePaths = @(
  '.tfw/conventions.md',
  '.tfw/templates/team/profile.md',
  '.tfw/templates/journal/event.md',
  '.tfw/templates/bindings.yaml'
)
$baselineSha = 'a048b2db5f44f5d748f22f3a0133f4ecf0acd9c4'
$candidateSha = '0ee39046b760d6d3e8d837c2377e49c1c95668bd'
if ($candidateSha -notmatch '^[0-9a-f]{40}$') { throw 'Candidate must be the full immutable Executor SHA' }
git diff --name-status --find-renames=50% -z $baselineSha $candidateSha -- $valuePaths
git diff --numstat --find-renames=50% -z $baselineSha $candidateSha -- $valuePaths
```

Both commands exited 0. Rendering NUL as `<NUL>` produced:

```text
M<NUL>.tfw/conventions.md<NUL>
M<NUL>.tfw/templates/bindings.yaml<NUL>
M<NUL>.tfw/templates/journal/event.md<NUL>
M<NUL>.tfw/templates/team/profile.md<NUL>

41  13  .tfw/conventions.md<NUL>
18  16  .tfw/templates/bindings.yaml<NUL>
14  11  .tfw/templates/journal/event.md<NUL>
70  32  .tfw/templates/team/profile.md<NUL>
TOTAL files=4 additions=143 deletions=72 touched=215
```

`git merge-base --is-ancestor` returned 0 for planning→approval and approval→Candidate. Candidate's
parent is ONB-state TRACE commit `1cbe84957db5a59b4fb3ec53497887b8552b94df`; no EV, RF, REVIEW, or
RF-state path is in Candidate.

## Verdict

Evidence verdict: 6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

---

*EV — TFW_20260902-111644_CRATM / Phase B: Named principals | 2026-09-06*
