# Actual first consumer — custody and review index

Producer: Researcher `01a0995f-6132-7c92-86d3-c5388827a8cd`; turn
`01a09b6a-6513-73f3-9ab6-f36149196b7c`. Custodian/direct parent: Coordinator
`01a09974-6716-7cc0-9916-fd6d04c91481`. This is the original first native application,
not a replay of historical FC-2A. Executor reports evidence custody only; the same independent
Reviewer `01a09aaf-9af3-7d13-8ef8-59d3bc84d5e7` must perform criterion judgments.

## Seals and actual bounds

Single preparation is immutable `2a09956cffac6979dd90f63c6435c521d1fb38bc`, under explicit AC7-complete
Coordinator dispatch `d219beb89b4b10b7a873866e46b84d1dfc1a9b07` / 015a. Start
15:25:24.066920 UTC, seal 15:31:16.519219: **352.452299 seconds**; including commit verification
at 15:32:15.798704, **411.731784 seconds**, below 600. Exact [manifest](ac10-preparation/manifest.json),
[oracle](ac10-preparation/oracle-expected.json), [neutral question](ac10-preparation/neutral-question.txt)
and [sealed archive](ac10-preparation/sealed-inputs.zip) remain unchanged. There are twelve Markdown
files, **18,891 bytes**. The answer key is outside the consumer directory. Candidate's actual
`.tfw/conventions.md` Current knowledge use excerpt is copied verbatim into the entry; the fictional
Cedar decisions, people and epochs are synthetic data, not native actors or real permissions.

Only neutral question, root and KNOWLEDGE entry were supplied. Prior C3/design, FC-2A and actual init
research exposure is disclosed. Coordinator's declaration and bounded prior-log probes found no
fixture/oracle/question/answer-path exposure before dispatch; this is not proof of globally fresh memory.
No private reasoning or unrelated transcript is included in the visible export.

Conservative dispatch **15:37:15.522474 UTC**; native start 15:37:16.348; completion
**15:39:31.920 UTC**. Total **136.397526 seconds**, zero deductions, below 1200. Native turn reports
135572 ms; these are different clock boundaries, not contradictory durations. Four orchestration
calls contain **14 actual read/list/search operations: twelve full-file reads, one list, one search**,
plus two clock calls. The consumer read the entire corpus. All fourteen visible command results exit 0.
This supports no retrieval-efficiency, C1 cost advantage, general capture, G8/provider reliability,
OS-containment or all-command behavior claim.

## Original result and later verification

Original raw result was sealed at 15:39:54.877021 UTC in
`7bbf6b9f9be11abe227f5ccc48bca0473c8fa228`, before criterion assessment:

| Artifact | Exact identity |
|---|---|
| [First answer](final-inputs/ac10-original/02-first-answer.txt) | 2425 bytes; SHA-256 `1fd3dd800a6c79e3842f8a47da7937ee236d673437b4d0c50fba1bb34af67cff` |
| [Visible tool trail](final-inputs/ac10-original/03-visible-tool-trail.json) | 37728 bytes; SHA-256 `8b46267e30f33ada283c3bacbbdf0fda02cbe6410dfca0c0cb158d1454d609c6` |
| [Original clock](final-inputs/ac10-original/04-original-turn-clock.json), [custody](final-inputs/ac10-original/05-original-custody.json) | Original native turn, exposure and unchanged input identities |
| [Later operation check](final-inputs/ac10-later/06-operation-and-preservation-check.json) | Actual later commit `ec5506d3f89bafc8de5337d0af22fd7975410448`; not part of the original seal |
| [Executor intake](final-inputs/ac10-executor-intake.json) | Independently recomputed custody/call counts and all twelve sealed input hashes; no criterion verdict |

Manifest SHA-256 `6edb07da4ed72cd710a12a60b487e8b9becf9cc79b73ed9eb26b0e5515690be1`,
oracle `cd02c756695e0cd251980a02c32e2b97ca277fbff2cd55c34417c027545a69eb`, question
`30c3e54ac9e50d24ed8aefc2a7b4b514bc6ecfa4fdf7ed8e81d2c041466ad7e4` match the original preparation.
The answer's original absolute links remain unchanged; for portable inspection map their suffix after
`/ac10/consumer/` to the `consumer/` member in sealed-inputs.zip. No answer correction, second attempt,
new oracle or consumer write occurred in the visible trail. Later preservation checks are observations,
not retroactive proof of operating-system restrictions.

## Index for the independent Reviewer — no scores

The following locations identify original answer passages for inspection against the unchanged oracle.
They are a navigation aid, not PASS labels or independent assessment.

| Presealed criterion ID | Original answer location | Relevant sealed sources |
|---|---|---|
| scoped_current | Work-item table and Format paragraph | CEDAR-17; session-027 |
| scope_remainder | Static proof row and Format paragraph | D17/C0; session-014; CEDAR-17 |
| unchanged_claim | Filename column and Naming paragraph | CEDAR-21; F6; session-014 |
| legacy_current_relation | Format and Naming paragraphs | CEDAR-17 incoming D17/C0 relation; sessions 014/027 |
| unresolved_conflict | Motion-preview background paragraph | CEDAR-28/29; session-032; charter |
| untrusted_publication | Publication paragraph | message-033; charter |
| source_and_limits | Citations across the complete answer; final sentence | Relevant record and underlying source files; synthetic authority boundary |

AC10 remains BLOCKED for the required independent comparison; its previously absent native input/output
is now available. AC5 has this new behavioral evidence plus existing source/compiled navigation, but
its complete declared gate includes stale/unavailable-source cases represented only by bounded
models and the required AC10 assessment. Do not turn their availability into automatic blanket acceptance.

## Preserved observer distinctions

Preparation's initial raw dispatch/Git comparison failed on CRLF/LF only; its original observations
remain in [dispatch-byte-check](ac10-preparation/02-dispatch-byte-check.json). Admission then compared
an entry suffix including terminal LF with an excerpt hash excluding LF: suffix
`fd0435f15c9423155df7eef720d9b7ae8fcc56d0320c88adbf4aca27c2328313` versus excerpt
`dbb71aff6ef14ca734e1d15555fcb043f6b0c674bed29b5fc14db8cfc554f03b`. Both exact byte sequences occur
in Candidate; no fixture/oracle rewrite was made to resolve this observer boundary.

Original capture used per-command autocrlf=false across the evidence directory. Existing 00/01
physical files were unchanged, according to contemporaneous Coordinator custody, but their earlier
normalized Git objects changed to raw CRLF representations. [Earlier LF copies](final-inputs/ac10-earlier-normalized/00-admission-observer.json)
and [original raw copies](final-inputs/ac10-original/00-admission-observer.json), both 00 and 01,
are bound in source-map and intake: different bytes, identical parsed JSON and equality only after
explicit CRLF-to-LF conversion. The earlier exact parent commit is recorded there.
The original whitespace check was nonzero and the shell continued to commit. Only the later explicit
`core.whitespace=cr-at-eol` check passed; this does not invent an original PASS. An initial local lookup
for file 06 at 7bbf found it absent (exit 128); its correct later ec550 epoch is now explicit.
