# EV — TFW_20260907-133942_PTTC / Phase A: Proportionate repository verification

> **Date**: 2026-09-08
> **Author**: robert, Executor `01a081fd-96cb-7862-9c15-33d803c1aade`
> **Task**: TFW_20260907-133942_PTTC / Phase A
> **TS**: [approved Phase A TS](../TS__phase-a__proportionate_repository_verification.md)

## Environment

| Field | Value |
|---|---|
| OS | Windows 11, 10.0.26200, AMD64 |
| Language / Runtime | Python 3.13.5; regular observations 02–06/08: isolated pytest 8.4.2; controlled pair 01/07: same global pytest 9.0.2 |
| Build dependencies | MkDocs 1.6.1, mkdocs-material 9.7.6, PyYAML 6.0.3 throughout |
| Database | N/A |
| Deploy target | N/A; local repository and disposable roots only |
| CI / Pipeline | Local; no CI, push, publication or landing performed by Executor |
| Producer / parent | Executor `01a081fd-96cb-7862-9c15-33d803c1aade`; Coordinator `01a08196-9e95-7ef3-8a4f-a5d6b4a424a9`; root LEAD `01a07050-9d35-7080-a5f6-afd14334e68d`; owner saubakirov |
| Repository / scratch | Branch `codex/pttc-phase-a-exec`, `C:/Users/c0rpa/.codex/worktrees/b9b5/steps-framework`; disposable `E:/TEMP/pttc-phase-a-b9b5/` |

Global pytest 9.0.2 is outside `tools/requirements.txt`'s `>=8,<9` range. After the baseline observation, the Coordinator directed retaining that environment for the controlled pair and using isolated supported pytest 8.4.2 for the ordinary gates. The pair is local comparative evidence, not supported-environment acceptance. The global environment was unchanged. Exact commands, versions, environment hash, manifests and failed attempts are in [the ledger](phase-a-verification.txt) and the raw archive.

## Evidence

The immutable Candidate is `8c72c4c25aa7dde461cfee23b11f90db5f09e220`. Collection/full execution observed final working bytes at `62cb3f58a56c2dc8e69fd5f67366264f10725c6d`; Candidate was then committed in canonical handoff order. E8 records the crossing rather than claiming that its SHA existed before execution. Each archive reference below resolves inside `phase-a-raw.zip/logs/`.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | All 15 original output predicates and the shared module build remain. The new source/Git/temp-tree family has no build-backed import or output read. Absent-output evidence is 121 unaffected passes from 02 plus all 3 corrected dependent tests in 03; the 3 original failures and exact correction are retained. Stale-output 04 passes all 124 selected cases, starts zero MkDocs processes and leaves all 1,778 site files byte-identical. The actual full run also covers the final sources. Only live R10/R14 paths changed; their retained ledger selection passes. | pytest 8.4.2; isolated pure root based at committed ONB plus four working VALUE files; final source bytes match Candidate | VERIFIED | `dependency-map.json`, `dependency-dispositions.md`, `02-*`, `03-*`, `04-*`, `06-full-suite.*`; [ledger](phase-a-verification.txt) |
| E2 | AC-2 | Seven statically shadowed bodies, two thin aliases and two orphan helpers are removed. Every removed body has a surviving effective predicate or alias target in the complete mapping. Controlled doctor, adapter parity, package replay and negative cases remain observed in 04/06. Board regression guard follows its own filename for self-exclusion and now inspects the old integration filename; its meaningful source population is preserved. | Static baseline/Candidate identity plus pytest 8.4.2 | VERIFIED | `dependency-dispositions.md` maps all 156 baseline function bodies; `dependency-map.json` records body hashes and dependencies for 150 current functions/helpers; `04-pure-stale.*`, `06-full-suite.*` |
| E3 | AC-3, executable claims | Historical pre/post-K2 row identities stay pinned to their real immutable epochs. Current selected decision/artifact cardinality, lineage and required immutable sources are checked without full-row equality. Wording and the labeled synthetic successor pass; missing/duplicate rows, incompatible phase, fabricated/wrong references fail their controlled checks. The unchanged live KNOWLEDGE.md is included with zero builds in the pure runs. | pytest 8.4.2; actual and disposable knowledge inputs | VERIFIED | `03-corrected-absent.*`, `04-pure-stale.*`, `06-full-suite.*`; `knowledge-variants.preparation.json`, `knowledge-negative-inputs.json` and exact inputs; [variants](phase-a-input-variants.md) |
| E4 | AC-3, semantic claims | Independent source-grounded acceptance of the exact wording and synthetic successor, and rejection of the principal/unit authority distortion, remains for the assigned Reviewer. The executable structural helper does not establish material meaning, attribution or successor legitimacy. AC4's hypothetical D84 reading does not substitute for this review. | Existing native Reviewer `01a081fd-9b5b-7061-9c98-7528ed698b07` | DEFERRED | Exact positive/distortion inputs and four immutable authority-source attachments in [variants](phase-a-input-variants.md); formal `/tfw-review` is the next role-owned stage |
| E5 | AC-4 | Candidate README supplies six change→risk selections, broad/output triggers, claim-specific reuse and preserved configured gates. Both existing native holders independently applied identical guide blob `2fdf930de8d974d47961b7fbd0708afe51520dd5` to one case batch before unblinding: retain unaffected fixture evidence; do not accept changed knowledge from old bytes; reject reuse for an unsupported changed oracle. Reviewer challenged unproven output membership in A and chose a broader source selection in B. This is a bounded observed choice, not universal reliability. | Direct native tasks, no case mutation or test execution | VERIFIED | `ac4-raw-batch.txt`, `ac4-executor-response.txt`, `ac4-reviewer-response.txt`; Reviewer turn `01a08212-563b-73f1-9658-715b35aafce7`; [variants](phase-a-input-variants.md) |
| E6 | AC-5, local comparison | Exact scanner test/helper/constants and fixture data are unchanged. Both isolated roots use all 1,968 identical non-VALUE baseline source files; candidate side overlays only exact four Candidate blobs. Absent site on both sides, same interpreter/versions/env/arguments apart from moved node and temporary root. Process time 148.519336900 s → 0.989396900 s, a 147.529940000 s reduction; MkDocs starts 1 → 0. One local pair, with observer overhead and pytest 9 limitation; no universal speedup or changed-knowledge timing claim. | Same global pytest 9.0.2 on Windows/Python 3.13.5 | VERIFIED | `01-baseline.*`, `07-candidate-pair.*`, `07-composition.preparation.json`, `paired-subject-identities.json` |
| E7 | AC-1/5, coherence and output protection | Configured collection finds 549 tests; full suite has 548 passed/1 existing conditional skip. Full output build succeeds. Starting from 1,791 valid stale files, a disposable KNOWLEDGE frontmatter prefix causes a successful fresh build followed by the unchanged leak test detecting exactly one of 1,726 pages. No assertion was changed; disposable generator is restored byte-exactly after raw capture. | pytest 8.4.2; actual full-suite working source and isolated Candidate adverse root | VERIFIED | `05-collection.*`, `06-full-suite.*`, `08-adverse-output.*`, normal/adverse HTML, `08-restoration.preparation.json`; [ledger](phase-a-verification.txt) |
| E8 | AC-5, Candidate applicability | At commit crossing all 1,984 observed source files and membership match; four VALUE blobs match; parent is linear; MERGE_HEAD stays absent; merge graph and selected historical Phase E candidate/parents are unchanged. Literal HEAD is not asserted in this branch without MERGE_HEAD; other actual-root Git assertions use immutable inputs. Later reporting traces are outside this tested manifest and do not receive blanket full-suite acceptance. | Same actual worktree/runtime before and after commit | VERIFIED | `06-full-suite.inputs.json`, `pre-candidate-working-blobs.json`, `candidate-crossing.preparation.json` |
| E9 | AC-5, independent review and landing | Independent Candidate/accounting/applicability judgment and any later root landing crossing have not occurred. Return goes to the existing Coordinator for the existing Reviewer; no second full suite is justified by default. Publication is separately reserved. | Native Reviewer and root, subsequent authorized stages | DEFERRED | This RF/EV packet and reachable Candidate; no Reviewer verdict or landed/published state is asserted |
| E-accounting | AC-5 / TS §4 | Approval `49ddad02f97dfb46919bdd19292902b9082d696f`, exact approved TS producer `af52ef3ab6891031db8c411932879d76cfc1e6e6`, blob `b7ef498c4d911cf6fb4f8c810aef24913480f68d`; Baseline `099d37d21ddfada2ca72c576055f0a26029c7205`, Candidate `8c72c4c25aa7dde461cfee23b11f90db5f09e220`. Exact VALUE membership: MODIFY `docs/scripts/test_integration.py` (output boundary/transfer), CREATE `docs/scripts/test_repository_contracts.py` (accepted pure assurance product), MODIFY `docs/scripts/test_runtime_context.py` (R10/R14 target repairs), MODIFY `tools/README.md` (accepted maintainer route). All attributed to this Phase A Executor; no unresolved attribution or member deviation. 4 logical files; 2,922 additions + 2,937 deletions = 5,859 touched text LOC, no detected rename; binary/non-text N/A. Immutable denominator remains 4 files/6,400 LOC; multiplier triggers 8 files/12,800 LOC are not reached. Actual exceeds the 5,000-LOC soft prompt already prospectively approved at the owner TS epoch, before work: coherent move avoids a broken boundary/duplicate setup and retains broad/independent assurance. No line subtraction or late authority. Exact reproduction: both NUL-safe argv shown below, unchanged from approved method. | Repository Git, actual immutable commits | VERIFIED | `accounting-name-status.nul`, `accounting-numstat.nul`, `accounting.preparation.json`; exact commands below |

```text
git diff --name-status --find-renames=50% -z 099d37d21ddfada2ca72c576055f0a26029c7205 8c72c4c25aa7dde461cfee23b11f90db5f09e220 -- docs/scripts/test_integration.py docs/scripts/test_repository_contracts.py docs/scripts/test_runtime_context.py tools/README.md
git diff --numstat --find-renames=50% -z 099d37d21ddfada2ca72c576055f0a26029c7205 8c72c4c25aa7dde461cfee23b11f90db5f09e220 -- docs/scripts/test_integration.py docs/scripts/test_repository_contracts.py docs/scripts/test_runtime_context.py tools/README.md

M  docs/scripts/test_integration.py          +3     -2933
A  docs/scripts/test_repository_contracts.py +2858  -0
M  docs/scripts/test_runtime_context.py      +2     -2
M  tools/README.md                          +59    -2
```

### Cost and remaining allowance

Eight actual pytest processes, zero nested pytest processes, three actual MkDocs starts. Child argv classification is attached; `codex --version` reads are not additional agents. The three build durations are already included in pytest process wall time.

Measured pytest process time is **1,006.177771 s**, input capture **31.817493 s**, measured preparation **201.244706 s**. Earlier short preparation has a separately labeled **120 s conservative bound**; later short reads, serialization, packaging, wrapper overhead and closeout have a **180 s conservative bound**. The resulting Executor accounted upper bound is **1,539.239969 s (25.6540 min)**, not a claim that all this time was measured. The Coordinator's separately measured **0.154197 s** read is added only to the common ledger: **1,539.394166 s**, leaving **2,060.605834 s** of the common 3,600 s ceiling at this return. Details and non-overlap are in `budget-summary.json` and the command ledger.

The [prospective correction allocation](../journal/20260908-223446__dispatch__bc81.md) raised this Executor to eight pytest/three builds/50 command minutes without changing the owner ceiling of ten/four/60. Executor has no pytest/build allocation left. One Reviewer targeted process and one common contingency process remain, with one common build; Coordinator routing is required before use. Failed observation 02 is included, with correction 03 limited by actual dependency closure. No repeat was made to improve the time statistic. Native message/review labor, elapsed agent work, tokens and money are unknown. One AC4 batch per holder and the source read are the available effort observations.

## Verdict

Evidence verdict: **8/10 VERIFIED, 2 DEFERRED, 0 BLOCKED, 0 N/A**.

The two deferred rows are explicitly independent Reviewer/root responsibilities; this is an Executor handoff, not completed phase acceptance. No missing semantic or landing evidence is reported as PASS.

## Attachments

| File | Description |
|---|---|
| [phase-a-verification.txt](phase-a-verification.txt) | Execution-order commands, exact identities/outcomes, environment separation, failure/correction, skip, accounting and complete cost ledger |
| [phase-a-input-variants.md](phase-a-input-variants.md) | Exact variant/source references, genuine rendering variation and native case choices with limits |
| [phase-a-raw.zip](phase-a-raw.zip) | 109 members, 2,331,816 bytes; original logs/stdout/stderr/manifests, body/dependency mapping, NUL accounting, exact positive/negative/semantic knowledge inputs, immutable sources, normal/adverse HTML and disposable observation/serialization scripts. Internal SHA256 index verifies every other member. Archive SHA256: `fd878b9b5e136f349afdc56f83a209154a520732ba79c53d722b54fcd68cab0d` |

*EV — TFW_20260907-133942_PTTC / Phase A | 2026-09-08*
