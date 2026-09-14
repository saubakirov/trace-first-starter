"""Write the authorized first real EV/RF with actual blocking evidence; no acceptance."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[4]
TASK = ROOT / 'workspace/2026/TFW_20260909-231654_TKL'
EVIDENCE = TASK / 'evidence'
ID = 'TFW_20260909-231654_TKL'
CANDIDATE = '27cdb701b91c5b45b9f54b3e98c9ad67635b3e30'
BASE = 'ec91c56007c20cda79f740fec15c85e4af74d17c'
APPROVAL = '2794cbdb40f6c4f3a7d4bce1f8d4eb949d9e6913'
TS_BLOB = 'f69fd4099a21a07ae2d17e6b5108b04ac94f107e'
assert subprocess.check_output(['git', 'rev-parse', 'HEAD:' + (TASK / ('TS__' + ID + '.md')).relative_to(ROOT).as_posix()], cwd=ROOT).decode().strip() == TS_BLOB
accounting = json.loads((EVIDENCE / 'accounting/candidate-27cdb70/accounting.json').read_bytes())
assert accounting['actual']['logical_value_files'] == 58
ts = subprocess.check_output(['git', 'show', TS_BLOB], cwd=ROOT).decode()
values = re.findall(r'^\| `([^`]+)` \| (MODIFY|CREATE|DELETE) \| VALUE \| ([0-9]+) \| ([0-9]+) \| (.*?) \|$', ts, re.M)
assurance = re.findall(r'^\| `([^`]+)` \| MODIFY \| ASSURANCE \| (.*?) \|$', ts, re.M)
assert len(values) == 58 and len(assurance) == 7

ac = [
 ('AC-1', 'VERIFIED', 'Source-derived role routes and actual bounded Coordinator/Executor returns, existing ONB interim return and necessary native fallback; first originals sealed before sibling visibility. Historical/prepared and universal-capture limits remain explicit.', 'handover.md'),
 ('AC-2', 'VERIFIED', 'Actual six first handover/disposition decisions, including real scoped-none return; historical Researcher-A plus prepared missing-B, unavailable/retain-only/owed distinctions and protected close/owner are explicit.', 'handover.md'),
 ('AC-3', 'VERIFIED', 'Actual owner-qualified architecture record and original human decision resolve; observed technical native records retain their own sources, roles and absent acceptance. Source/authority mutants and human/technical ownership checks pass; no implementation acceptance inferred.', 'native/raw/source-inspection.json'),
 ('AC-4', 'BLOCKED', 'Actual independent publication/integration retains all four originals; equal accepted-SLC alias retry and divergent refusal occurred. Temporal overlap is zero (27.461981-second gap): sequential independent writes, not concurrency. Existing Coordinator has returned the gap to LEAD; no new trial or overall PASS.', 'replay-recovery.md'),
 ('AC-5', 'BLOCKED', 'Current-use source/case gates and source/compiled navigation are available; required new AC10 first consumer answer is unperformed and AC4 remains incomplete. No full current-use acceptance claim.', 'navigation.md'),
 ('AC-6', 'BLOCKED', 'Positive native recovery stopped before write: prepared physical directory is not the owning task ID and relative HL authority is absent. All case carriers/events stayed unchanged; negative cases share incomplete physical context. AC4 dependency also remains unsupported; finite model tests do not pay native repair.', 'replay-recovery.md'),
 ('AC-7', 'BLOCKED', 'No actual clean Full init or established adoption/repeat/refusal yet. Q3 omitted original reader/adapter map remains a procedural acceptance defect despite a truthful current reconstruction. Existing staged 0173 route requires initial RF, one Reviewer and real receiver roles; no blanket adoption claim.', 'adoption.md'),
 ('AC-8', 'BLOCKED', 'Final build and exact resolver/integration checks passed; seven actual final HTML destinations and bounded earlier browser observations retained. AC5/AC7 dependencies remain unsupported; later initial EV/RF/control pages were absent from that build. The earlier failed HL click is retained.', 'navigation.md'),
 ('AC-9', 'BLOCKED', 'Source parity, four adapter installations/repeats, selected-source graph and retired no-scan CLI checks pass. A complete actual selected planning-entry result and AC5/AC7-dependent consumer behavior are not established by these models/copies; no universal command-following claim.', 'checks.md'),
 ('AC-10', 'BLOCKED', 'The required new fixture/oracle/question and first read-only consumer attempt have not been prepared or dispatched. Must follow actual AC7 completion and an explicit Coordinator dispatch; historical FC-2A does not substitute.', 'adoption.md'),
 ('AC-11', 'BLOCKED', 'Required final collection/full suite/build and fixed accounting pass; exact per-AC gaps are retained. AC4/6/7/10 and dependent results remain incomplete; one independent Reviewer and final effect judgments are later acts. Initial RF is a real staged return, not delivery acceptance.', 'checks.md'),
]
assert sum(status == 'VERIFIED' for _, status, _, _ in ac) == 3
created_at = datetime.now(timezone.utc).isoformat()
literal_selector = '$valuePaths = @(\n' + ',\n'.join("    '" + row[0] + "'" for row in values) + '\n)'
ev = f'''# EV — {ID} / Phase A: Complete team knowledge lifecycle

> **Date**: 2026-09-13
> **Author**: robert, actual Executor `01a09a0c-c9e2-7d01-af4e-64931af967ed`, for saubakirov
> **Task**: {ID}; sole phase at task root
> **TS**: [Exact approved TS](../TS__{ID}.md), blob `{TS_BLOB}`
> **Epoch**: Initial actual evidence, assembled {created_at}; overall delivery BLOCKED

---

## Environment

| Field | Value |
|---|---|
| OS | Windows 11, 10.0.26200; PowerShell; local timezone +05 |
| Language / Runtime | Python 3.13.5 from E:/TEMP/pttc-phase-a-b9b5/venv/Scripts/python.exe; pytest 8.4.2, PyYAML 6.0.3; MkDocs 1.6.1 / Material 9.7.6 |
| Database | N/A; ordinary Markdown/YAML/Git files |
| Deploy target | N/A; local disposable receivers and local site inspection only |
| CI / Pipeline | Local configured pytest collection/full suite and actual MkDocs subprocess; raw argv/cwd/time/streams retained |

## Evidence

These are Executor evidence statuses for bounded claims, not independent Reviewer acceptance. The
Q2/Q3 ruling `144e3e651382330afba4d7131a562d05e7f515f9` and direct dispatch
`bb3c2803e610bd5fe1cc6eed040b73a6cb2a40aa` explicitly authorize this initial staged BLOCKED RF.
Coordinator's actual Q1 return `99094a4acdf3edcd4d544f76d8ab8e467b8465c7` preserves the two new
gaps and pending authority route; exact original bytes are in
[the returned event](native/raw/99094a4-coordinator-return.md). No enclosing unselected RWNR tip was integrated.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
'''
for i, (criterion, status, claim, artifact) in enumerate(ac, 1):
    ev += f'| E{i} | {criterion} | {claim} | Actual Candidate source/tests and explicitly bounded native/local observations | {status} | [{artifact}]({artifact}) |\n'
ev += f'''| E-accounting | AC-11 accounting only | Approval `{APPROVAL}`; exact TS `{TS_BLOB}`; Baseline `{BASE}` → Candidate `{CANDIDATE}`. All 58 literal whole VALUE paths, +1159/−999 = 2158 touched text LOC, zero binary/rename cases. Full immutable inventory: 58 VALUE, 7 ASSURANCE, 19 TRACE. No membership or planned-zero growth; tools/tfw_state.py +0/−194. Owner's pre-work 58/+1375−1199=2574 denominator and one-phase 50-file prompt disposition remain fixed; 116/5148 return thresholds not reached. Exact NUL-safe commands and path/action/class/reason membership resolve in attachments. | Same repository/Git; actual immutable objects and raw NUL output | VERIFIED | [Accounting JSON](accounting/candidate-27cdb70/accounting.json), [membership](accounting/value-membership.md) |

The exact approved reproduction uses the 58 literal TS VALUE paths, not a new selector:

```powershell
{literal_selector}
git diff --name-status --find-renames=50% -z {BASE} {CANDIDATE} -- $valuePaths
git diff --numstat --find-renames=50% -z {BASE} {CANDIDATE} -- $valuePaths
```

The exact executable argv including every literal path and hashes of both retained `.z` streams are
in accounting.json; filenames were parsed as NUL fields, logical rename grouping reconciled and numeric
fields summed. Membership reasons are the approved TS whole-path effects. No metric is silently zeroed
as binary N/A; there are no binary VALUE files. Authority came before product writes, from the actual
14:14:00+05 owner decision in approval `{APPROVAL}`, not from this report or a clean diff.

Final run 13 yielded **636 passed / 1 inherited skip**, collection 637, MkDocs exit 0. Tested raw inputs
bind to Candidate's normal-filter Git blobs, with raw and normalized identities separately named.
Prior failures and later corrections remain separate observed generations. Exact applicability and
limitations are in [checks](checks.md), [navigation](navigation.md) and [adoption](adoption.md).
Generated output is DERIVED; [all 1,945 observed site paths](inventory/derived-13-observation.json)
are indexed, not published. [Full initial-return inventory](inventory/initial-return-inventory.json)
explains later TRACE exclusions separately from immutable Candidate arithmetic.

## Verdict

Evidence verdict: **4/12 VERIFIED, 0 DEFERRED, 8 BLOCKED, 0 N/A**.

Three AC rows plus the dedicated accounting row are verified within their stated bounds. All eight
other AC rows retain exact blocking conditions; partial positive checks are not blanket PASS. Required
native recovery/concurrency evidence, actual AC7, AC10 and later independent judgment remain open.
No initial artifact is a terminal acceptance or evidence that a missing holder has performed work.

## Attachments

| File | Description |
|---|---|
| [checks.md](checks.md), checks/ | Actual commands, every retained failure/pass generation, snapshots, raw output and final source binding |
| [handover.md](handover.md), native/raw/executor/ and native/raw/coordinator-first/ | Actual distinct-source returns, first seals, scoped-none and first decisions |
| [replay-recovery.md](replay-recovery.md), native/recovery/first-actual/ | Real alias retry, unchanged P, failed positive carrier gate and all preserved negative inputs |
| [q1-receiver.bundle](native/raw/q1-receiver.bundle) | Portable exact receiver commits with immutable Candidate prerequisite; receipt and verify streams alongside |
| [adoption.md](adoption.md), [Q3 current map](adoption/q3-current-observation.json) | Original unchanged before-image, observed generations and unresolved procedural deviation; no completed AC7 |
| [navigation.md](navigation.md), navigation/08-browser/, navigation/11-output/, navigation/13-output/ | Honest browser observations/failures and separate actual generated HTML bytes |
| [Accounting](accounting/candidate-27cdb70/accounting.json), .z streams, [VALUE membership](accounting/value-membership.md) | Exact approved immutable arithmetic, complete Candidate classes and all 58 semantic reasons |
| inventory/ | Full current TRACE/DERIVED scope explanation and observed paths |

---

*EV — {ID} / Phase A: Complete team knowledge lifecycle | 2026-09-13*
'''
# The displayed recipe and stored argv both contain the exact approved selector.

rf = f'''# RF — {ID} / Phase A: Complete team knowledge lifecycle

> **Date**: 2026-09-13
> **Author**: robert, distinct Executor `01a09a0c-c9e2-7d01-af4e-64931af967ed`, for saubakirov
> **Status**: RF — initial report complete; overall delivery/acceptance BLOCKED
> **Parent HL**: [Frozen Team Knowledge Lifecycle](HL-{ID}.md)
> **TS**: [Exact approved Phase A TS](TS__{ID}.md), blob `{TS_BLOB}`

---

## 1. What Was Done

Implemented the approved mixed C3 lifecycle on the complete literal selector: producing-role material
handover, selected qualification, independently addressable records, incoming-relation/current-use
reading, finite close/retry and compatible adoption rules. Existing legacy D/topic/source meaning
remains; the live global pending/digest gate and new-state scaffold are retired. Ten canonical routes,
twenty installed whole copies and four thin routers agree. Nested records enter the existing compiler
without changing SLC's complete-link resolver. The owner architecture record preserves its real
decision and explicitly separates later implementation/release acceptance.

Final local checks passed and Candidate is fixed. Actual Q1 sources, integration and alias retry are
preserved; Q1 temporal overlap did not occur, and positive carrier repair failed its physical identity/
authority preconditions before write. Actual Full init/adoption and the new first consumer answer are
not performed. This is the real initial RF explicitly required by staged ruling 0173, not a complete
delivery or an outer review request. Q3's original before-image omission remains an acceptance defect.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `{APPROVAL}`; exact unchanged TS blob `{TS_BLOB}` |
| Baseline / Candidate | `{BASE}` / `{CANDIDATE}` |
| VALUE membership | All 58 literal whole paths with actual action, class, +/− and approved semantic reason in [membership](evidence/accounting/value-membership.md); no line subtraction or cross-phase allocation |
| Arithmetic | **1159 additions + 999 deletions = 2158 touched text LOC; 58 logical VALUE files**; no rename or binary/non-text case |
| Membership deviations | None; 53 MODIFY, 4 CREATE, 1 DELETE; seven approved ASSURANCE homes changed; immutable full Candidate inventory has 19 TRACE paths |
| Trigger disposition | The 58-file soft prompt was resolved before work by owner's approved one-phase disposition: connected reader/capture/adoption behavior and shipped copies; split considered in exact TS. Actual 2158 LOC remains below 5000 soft prompt. Seven test homes and bounded actual/native evidence supply the declared assurance, with all limitations reported. |
| Authority and timing | Owner 14:14:00+05 pre-work architecture/TS decision at approval above; fixed denominator 58/+1375−1199=2574, multiplier 2 thresholds 116 files OR 5148 LOC. No added VALUE path or planned-zero growth; tools/tfw_state.py is +0/−194. No authority ratchet or late approval. |
| Reproduction | Exact approved NUL-safe name-status/numstat commands, full SHAs and 58-argument vectors in [accounting.json](evidence/accounting/candidate-27cdb70/accounting.json); both original .z outputs retained |

Later evidence/EV/RF/control writes are excluded TRACE and do not move Candidate. Every exclusion is
listed in [initial-return inventory](evidence/inventory/initial-return-inventory.json); configured
site output is separately indexed DERIVED. These records report existing authority and no new scope.

### New Files

| File | Description |
|---|---|
'''
for name, action, pa, pd, reason in values:
    if action == 'CREATE':
        rf += f'| `{name}` | VALUE: {reason} |\n'
rf += f'''| `RF__{ID}.md`, `evidence/EV__{ID}.md` | Actual initial role/evidence reports; no acceptance |
| `evidence/` selected outputs and original self-adoption receipt | TRACE: actual raw checks, source/generation maps, native first returns, accounting and custody; complete literal inventory linked above |

### Modified Files

| File | Changes |
|---|---|
'''
for name, action, pa, pd, reason in values:
    if action == 'MODIFY':
        rf += f'| `{name}` | VALUE: {reason} |\n'
for name, reason in assurance:
    rf += f'| `{name}` | ASSURANCE: {reason} |\n'
rf += f'''| `ONB__{ID}.md` | TRACE: own original onboarding, actual Q2/Q3 return and resolved execution order |
| `status.md` and the new RF transition | TRACE: actual ONB → RF only after complete report/control validation; no terminal outcome |

Deleted VALUE file: `.tfw/templates/knowledge_state.yaml`; it no longer scaffolds obsolete state.
Existing receiver `.tfw/knowledge_state.yaml` remains preserved inert evidence. Earlier planning/
authority TRACE in Candidate belongs to its actual original producers, not this Executor's authorship.

## 2. Key Decisions

1. Kept existing role/stage sources first and added a fallback only for a real checkpoint without a
   suitable source; preserved actual unit/provenance rather than treating shared principal as one role.
2. Used source-bound independent records and explicit incoming relations while retaining legacy meaning.
   Owner-qualified architecture is distinct from observed technical evidence and absent implementation acceptance.
3. Removed only the retired global knowledge API section from optional state tooling; preserved historical
   test vectors against immutable Baseline source. Current source models have separate declared expectations.
4. Preserved raw check/native bytes through per-command Git autocrlf=false. Product remains normal-filter
   Candidate; raw CRLF/generated-output whitespace diagnostics are retained as preservation, not normalized away.
5. Stopped the actual Q1 repair at its failed physical carrier gate. The first failed preparation and
   zero-overlap epoch remain; no fixture repair, extra trial or acceptance was invented. Coordinator's
   formal return is `99094a4acdf3edcd4d544f76d8ab8e467b8465c7`, exact source copied in native/raw.
6. Followed actual 0173/580a order: initial blocked RF before one Reviewer, then real Full init and
   established adoption, then explicit AC7-complete dispatch before the new AC10 fixture/first answer.
   Q3's current reconstruction cannot cure its omitted original reader map; independent Reviewer decides.

## 3. Acceptance Criteria

'''
for criterion, status, claim, artifact in ac:
    rf += f'- [{"x" if status == "VERIFIED" else " "}] **{criterion} — {status}:** {claim}\n'
rf += f'''
The initial report completes the current Executor return, not all TS acceptance. All unsupported
dependent claims remain BLOCKED; no nonterminal requirement is relabelled N/A or silently omitted.

## 4. Verification

- Lint/collection (`python -m pytest tools/tests/ docs/scripts/ -q --collect-only`): final run 12,
  **637 collected, exit 0**, using the supported venv interpreter.
- Tests (`python -m pytest tools/tests/ docs/scripts/ -q`): final run 13, **636 passed / 1 inherited
  skip, exit 0**, 516.88 pytest seconds. The skip is the existing post-BOARD migration accounting case.
- Actual MkDocs subprocess: **exit 0**; original build streams and seven final HTML destinations retained.
- Exact final source binding: all 58 VALUE + seven ASSURANCE states match tested raw input/absence and
  Candidate's real Git filter identities. No product change follows Candidate. Source/adapter/retired
  CLI/model/resolver checks prove their stated subjects; native gaps remain separate.
- Original failures remain: run 02 old expectations (33 failures), run 03 accidental fixture rename,
  run 04 missing trailing-slash test input, run 06 old graph expectation; corrections and subsequent
  source epochs resolve those failures without erasing them. Browser HL click failure and unsupported
  export remain recorded; actual direct observed-HL navigation succeeded. No whole-corpus link claim.

## 5. Evidence

See [EV file](evidence/EV__{ID}.md) for evidence details.

Evidence verdict: **4/12 VERIFIED, 0 DEFERRED, 8 BLOCKED, 0 N/A**.

The EV includes one row per TS AC and exactly one dedicated accounting row. Every VERIFIED row resolves
to actual source/output. Q1 first source/record/return and accepted-P identities, prepared cut defects,
all prior failures and Q3 procedural limits remain inspectable. Final initial EV/RF/control prose was
not in the earlier Candidate build; later material final-output verification and independent judgment
remain with the existing Coordinator and the one Reviewer under PTTC.

## 6. Observations (out-of-scope, not modified)

No observations. Consequential in-scope evidence defects are explicitly recorded under AC4, AC6 and
AC7/Q3 above; they are not hidden as out-of-scope debt or declared paid.

## 7. Fact Candidates

No fact candidates. The available human decisions are the already-recorded owner architecture/cost
and authority boundaries. This execution adds technical measurements and material evidence gaps,
not new human-sourced project knowledge; the scoped-none return does not generalize beyond its seven rows.

## 8. Strategic Insights (Execution)

No strategic insights. No new human-sourced domain context was supplied during this execution return.

## 9. Diagrams

No diagrams. The approved source flow and existing workflow/carrier contracts already describe this
implementation; no new diagram is necessary to assess the observed source and evidence differences.

### Material handover at this return

Actual producer is robert, Executor `01a09a0c-c9e2-7d01-af4e-64931af967ed`, sole direct recipient
Coordinator `01a09974-6716-7cc0-9916-fd6d04c91481`, for owner saubakirov and LEAD
`01a08161-79d3-7472-a01e-8cdc957ee951`. I inspected the exact approved HL/TS/ONB and existing ordered
read context, changed source/test/output generations, actual original own/Coordinator Q1 returns,
real owner architecture decision, accepted SLC dependency and exact Q1/Q2/Q3 rulings. No sibling's
first native source was read before my own original seal. Original source epochs remain unchanged.

Material outcome: tested Candidate and fixed scope arithmetic are ready for inspection; the native
pair was sequential, and my recovery preparation lacked a valid physical task directory and relative
authority target. Positive recovery therefore did not run. Q3 omitted original reader-map facts are
unknown; the dated current observation binds reconstructable identities only. Actual Full init,
adoption/repeat/refusal and the new first consumer answer remain owed. These are technical evidence
and authority dependencies, not new human facts, justified-none for the whole task or paid retention.

Existing Coordinator owns the LEAD ruling on Q1 defects and the already-authorized staged receiver
route. Only after this real initial RF may it create the single independent Reviewer; outer TKL review
does not start yet. Existing Researcher/Coordinator/Reviewer complete actual AC7, then an explicit
Coordinator AC7-complete dispatch permits the separately bounded unseen AC10 preparation/answer.
The same Reviewer later judges supplemented final TKL evidence. I author no RES/REVIEW or new acceptance,
no release/tag/publication, no external receiver edit and no unselected parent merge. This Executor
stops the initial report stage after its direct immutable return. Subsequent bounded evidence work
already has a separate explicit dispatch: LEAD `f70037d94c975fe889eaab9bf17ee18e26608137` / 6f91 permits
one fresh same-holder overlap and one faithful recovery-context completion, preserving the first
epoch. Coordinator routed fresh overlap preparation to this same Executor and owns recovery itself.
Those are future evidence at this initial report, with no presumed success or changed Candidate.

---

*RF — {ID} / Phase A: Complete team knowledge lifecycle | 2026-09-13*
'''
for path, text in [(EVIDENCE / ('EV__' + ID + '.md'), ev), (TASK / ('RF__' + ID + '.md'), rf)]:
    assert not path.exists(), path
    path.write_text(text, encoding='utf-8', newline='\n')
print(json.dumps({'written_at': created_at, 'candidate': CANDIDATE, 'evidence_verdict': {'VERIFIED': 4, 'DEFERRED': 0, 'BLOCKED': 8, 'N/A': 0}, 'rf_bytes': len(rf.encode()), 'ev_bytes': len(ev.encode())}))
