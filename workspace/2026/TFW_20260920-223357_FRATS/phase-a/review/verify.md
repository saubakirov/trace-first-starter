# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: `0.42`
> RF files claimed: `47 VALUE` (`48` Candidate paths including one ASSURANCE file)
> Files to verify: `⌈47 × 0.42⌉ = 20`; actual: `47/47 VALUE` plus the ASSURANCE file

## Verification Log

An initial evidence-index gap around the exact-path commit boundary triggered 100% verification.
Every Baseline→Candidate VALUE blob was then opened and checked; the raw producer task record was
also inspected to resolve the staging claim.

| # | File(s) opened | RF claim and actual result | Match |
|---|---|---|---|
| V1 | `.tfw/conventions.md`; `.tfw/glossary.md` | The convention file now owns the current coordination vocabulary, five-field routing spine, exact activation, vertical gates, separate GATEWAY and native-evidence boundaries. The glossary routes current terms there and marks CL/AG/AT/LEAD labels as historical. A case-sensitive delivery-set census found no unexplained current issuer. | ✅ |
| V2 | `.tfw/templates/status.md`; `.tfw/templates/journal/event.md`; `tools/tfw_state.py` | Current status writes require the routing fields as an all-or-none set; tolerant legacy reads remain possible. `gate_answer` has mandatory references and current validators reject partial/empty/invalid/unresolved carriers and invalid authority references. | ✅ |
| V3 | `.tfw/templates/HL.md`; `.tfw/templates/bindings.yaml`; `.tfw/templates/team/profile.md` | Owner-direct and delegated selection is explicit; stable principal attribution does not itself grant authority, routing, amendment rights or a live roster. | ✅ |
| V4 | `.tfw/templates/research/1_briefing.md`; `.tfw/templates/RES.md`; `.tfw/templates/ONB.md`; `.tfw/templates/RF.md`; `.tfw/templates/REVIEW.md` | Role artifacts identify the actual producer, parent Coordinator, activation/dispatch source and coordination authority; writer-owned artifacts retain their role boundaries. | ✅ |
| V5 | `.tfw/adapters/codex/AGENTS.md.template`; `AGENTS.md`; `.tfw/adapters/claude-code/CLAUDE.md.template`; `CLAUDE.md`; `.tfw/adapters/antigravity/tfw-rules.md.template`; `.agents/rules/tfw.md`; `.tfw/adapters/cursor/tfw.mdc.template` | Persistent entry surfaces implement bounded activation/routing instructions without making provider capability a project-wide fact. Codex and Claude managed blocks match their templates; the Antigravity persistent projection is byte-identical to its template. | ✅ |
| V6 | `.tfw/workflows/plan.md`; `.tfw/workflows/research/base.md`; `.tfw/workflows/handoff.md`; `.tfw/workflows/review.md`; `.tfw/workflows/docs.md`; `.tfw/workflows/knowledge.md`; `.tfw/workflows/release.md`; `.tfw/workflows/init.md`; `.tfw/workflows/update.md` | The nine canonical workflows consume current routing state, distinguish activation from provisioning/navigation, enforce vertical role returns and retain each workflow's separate external-effect boundary. | ✅ |
| V7 | `.claude/commands/tfw-plan.md`; `.agents/workflows/tfw-plan.md`; `.claude/commands/tfw-research.md`; `.agents/workflows/tfw-research.md`; `.claude/commands/tfw-handoff.md`; `.agents/workflows/tfw-handoff.md`; `.claude/commands/tfw-review.md`; `.agents/workflows/tfw-review.md` | Each copy is byte-identical to its canonical workflow. | ✅ |
| V8 | `.claude/commands/tfw-docs.md`; `.agents/workflows/tfw-docs.md`; `.claude/commands/tfw-knowledge.md`; `.agents/workflows/tfw-knowledge.md`; `.claude/commands/tfw-release.md`; `.agents/workflows/tfw-release.md`; `.claude/commands/tfw-init.md`; `.agents/workflows/tfw-init.md`; `.claude/commands/tfw-update.md`; `.agents/workflows/tfw-update.md` | Each copy is byte-identical to its canonical workflow. Across V7–V8, all 18 generated copies pass. | ✅ |
| V9 | `docs/scripts/command_entry_eval.py` (ASSURANCE) | Existing evaluator fixtures now supply the current routing spine and explicit activation language; the configured suite passes without adding a permanent test. | ✅ |

The literal approved selector contains 47 unique VALUE paths. Git independently reports exactly 47
modified VALUE members, no missing or extra member, no rename/create/delete, no binary file, and
`826 + 520 = 1,346` touched text LOC. The Candidate contains exactly those 47 paths plus the declared
ASSURANCE evaluator. No later commit through `51ee2c2274ed1c18b5135188f78540cd2321e14d`
changes a VALUE path.

## Commands Executed

| # | Command / check | Result |
|---|---|---|
| 1 | NUL-safe parse of approved literal VALUE selector against `git diff --name-status --find-renames=50% -z Baseline Candidate` | PASS — 47 unique selector paths, 47 `M` entries, missing `0`, extra `0` |
| 2 | NUL-safe `git diff --numstat -z Baseline Candidate -- $valuePaths` | PASS — 826 additions, 520 deletions, 1,346 touched text LOC, binary `0` |
| 3 | Candidate `git diff-tree` membership | PASS — exactly 48 paths: 47 VALUE plus `docs/scripts/command_entry_eval.py` |
| 4 | VALUE history from approval through final TRACE read | PASS — only Candidate `1a9209530d7a939db1270e2f91dcef40a9f449e6`; later VALUE changes `[]` |
| 5 | `python -m py_compile tools/tfw_state.py docs/scripts/command_entry_eval.py` | PASS — exit 0 |
| 6 | `python -m pytest tools/tests/ docs/scripts/ -q` | PASS — 14 passed in 3.95s |
| 7 | `git diff --check c80c0dd5e79a6e996fdc68a89ad01b26887c638e 1a9209530d7a939db1270e2f91dcef40a9f449e6` | PASS — exit 0 |
| 8 | Independent semantic fixtures for current/legacy status, incomplete/invalid route, unresolved authority, iterative-without-GATEWAY, valid `gate_answer`, and missing/cross-task references | PASS — all twelve required semantic outcomes hold |
| 9 | Canonical/copy byte comparison and managed-block comparison | PASS — 18 workflow copies, Codex and Claude blocks, and Antigravity projection match |
| 10 | Case-sensitive current-term census over the delivery set | PASS — only explicitly historical occurrences plus a false-positive code comment (`AT ALL`) |
| 11 | Resolve every HL §7.2 and ONB §7 citation to file, anchor/item and asserted use | PASS — 20/20 resolve, 20/20 exist, 20/20 match meaning and relevance |
| 12 | Inspect native producer task record around Candidate creation | PASS — complete pre-commit status showed all 48 intended modifications, an empty staged-name set and only the two disclosed unrelated untracked paths; Candidate used `git commit --only` with all 48 explicit pathspecs |
| 13 | Inspect exact-path handling for later evidence/RF and provider TRACE commits | PASS — complete status/cached-name reads and explicit `git commit --only -- <exact paths>` boundaries are present |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|---|
| C1 | “47 MODIFY logical files; 826 + 520 = 1,346 touched text LOC; no binary/rename/deviation” | RF §1; EV `E-accounting` | Primary Git diff at Baseline `c80c0dd…` and Candidate `1a920953…`, using the approved literal selector from TS `ad6042d…` | ✅ |
| C2 | Codex P2/partial P3, Claude P2, and `agy` P2/partial P3; no P4 or reliability rate | RF §2/§4; `provider-native.md` | Native Codex task receipts; Claude session `a42f2c99-9bc2-426a-9726-ab109e52f5c1`; `agy` conversation `9b323e29-99dc-4934-86c3-e930bfca72bc`, including the preserved first contradiction and authorized correction | ✅ |
| C3 | “18 command copies” and “zero unexplained current mode/LEAD issuers” | RF §3/§4; EV E1/E7 | Direct byte comparison against nine canonical workflows plus case-sensitive delivery-set census | ✅ |

Every citation in HL §7.2 and its ONB §7 application resolves to a real repository artifact and
named clause/item. Numeric accounting was checked from primary Git objects, not copied from RF or EV.

## Discrepancies Found

No unresolved discrepancies.

The initial evidence index did not itself expose the complete pre-commit status, staged-name set or
literal Candidate commit command. That evidence gap triggered 100% file verification. The native
producer task record then resolved it: it shows all 48 intended modifications, no staged names, the
two unrelated untracked paths, and `git commit --only` with the complete explicit path list. Current
Git objects independently confirm the resulting membership and preservation boundary.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|---|---|---|
| E1 | `copy-and-suite.txt` current-term census; `.tfw/conventions.md` §7 | ✅ | ✅ — canonical owner and historical-term disposition confirmed |
| E2 | `coordination-scenarios.md` §1; migration `9e9513a` | ✅ | ✅ — strict current carrier, tolerant legacy read and live migration confirmed |
| E3 | `coordination-scenarios.md` §§3–4; Codex ledger | ✅ | ✅ — vertical/default and iterative/GATEWAY boundaries confirmed |
| E4 | `coordination-scenarios.md` §2; ONB and Codex ledger | ✅ | ✅ — activation/provision/continuation and provenance distinctions confirmed |
| E5 | `coordination-scenarios.md` §5 | ✅ | ✅ — `gate_answer` structure and refusal cases confirmed by source and fixtures |
| E6 | `coordination-scenarios.md` §6 | ✅ | ✅ — role ownership and independent-review boundary confirmed |
| E7 | `copy-and-suite.txt` parity, syntax, suite and accounting sections | ✅ | ✅ — reproduced independently; exact-path boundary additionally confirmed from the producer record |
| E8 | `provider-native.md` | ✅ | ✅ — native identities, failures, correction and claim ceilings match raw provider returns |
| E9 | `coordination-scenarios.md` §7; `copy-and-suite.txt` | ✅ | ✅ — Executor-owned checks pass; the formerly deferred independent REVIEW/final-output judgment is supplied by this review |
| E-accounting | `copy-and-suite.txt` NUL-safe accounting | ✅ | ✅ — selector membership, arithmetic, actions and trigger disposition reproduced from Git |

The RF's count remains accurate for its production epoch: 8/9 VERIFIED and E9 DEFERRED pending this
independent role. This review independently closes the deferred portion; it does not retroactively
rewrite the Executor's evidence status.

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|---|---|---|---|---|---|
| 1 | HL §7.2 K1 / ONB §7 #1 | P0 — root `README.md`, preamble and `How It Works` | ✅ | ✅ | ✅ — durable, inspectable continuation and divided responsibilities | ✅ — constrains low-chatter routing |
| 2 | K2 / #2 | P0 — `.tfw/README.md` NS1 | ✅ | ✅ | ✅ — purposeful human-governed continuity | ✅ — authority must remain inspectable |
| 3 | K3 / #3 | P0 — NS2.2, NS2.4, NS2.5, NS2.7 | ✅ | ✅ | ✅ — simple complete form, selected trace, bounded delegation, proportional assurance | ✅ — shapes carrier and evidence size |
| 4 | K4 / #4 | P0 — NS3 | ✅ | ✅ | ✅ — rejects transcripts, authority replacement, bureaucracy and vendor lock | ✅ — excludes provider-bound runtime semantics |
| 5 | K5 / #5 | P1 — Methodology Values | ✅ | ✅ | ✅ — structural enforcement, naming and portability | ✅ — supports exact terms and provider-neutral files |
| 6 | K6 / #6 | P0 — Success Criteria | ✅ | ✅ | ✅ — resume, trace, qualified knowledge and acceptance-ready outcomes | ✅ — preserved by the coordination refactor |
| 7 | K7 / #7 | P2 — philosophy F3/F4/F32/F37/F38/F40/F43/F45 | ✅ | ✅ | ✅ — critical opposition, structural gates, bounded mandates, finite attention, compression and subtraction | ✅ — directly informs topology and refusal design |
| 8 | K8 / #8 | P3 — KNOWLEDGE D23/D28/D31/D59/D73–D75 | ✅ | ✅ | ✅ — compression, naming, filesystem state, capability and selected context | ✅ — defines measured baseline; D75's historical `112,536` conflict is explicitly bounded, not reused as the reproduced count |
| 9 | K9 / #9 | P3 — D79/D81/D83/D84 | ✅ | ✅ | ✅ — session identity, human authority and prior team semantics | ✅ — A3 is correctly treated as successor to D83's active AT/LEAD issuance |
| 10 | K10 / #10 | P3 — D85/D86 | ✅ | ✅ | ✅ — receiver-safe evidence and finite Coordinator closure | ✅ — constrains migration and return behavior |
| 11 | K11 / #11 | P4 — `.tfw/conventions.md` HL Contract, Design Rules, Role Lock, prohibited anti-patterns | ✅ | ✅ | ✅ — frozen intent, dense algorithm, ownership and no cross-role repair | ✅ — governs implementation and this review |
| 12 | K12 / #12 | P5 — convention F1/F5/F19 | ✅ | ✅ | ✅ — canonical parity and naming consistency | ✅ — directly applies to 18 copies and file names |
| 13 | K13 / #13 | P5 — process F3–F5/F27/F30/F35/F37–F40/F43/F45/F47–F49 | ✅ | ✅ | ✅ — precise terms, ordered workflows, file-first/native evidence and reproducible counts | ✅ — directly applies to execution and evidence |
| 14 | K14 / #14 | P5 — constraint F2/F11/F12/F14 | ✅ | ✅ | ✅ — reader load, provider-local topology, file-owned obligations and necessary second coordination act | ✅ — supports bounded provider claims and independent review |
| 15 | K15 / #15 | P5 — environment F5/F6 | ✅ | ✅ | ✅ — provider strengths/topologies differ; prior Claude evidence was not universal | ✅ — requires independent provider ledgers |
| 16 | K16 / #16 | P5 — stakeholder F6–F8/F10–F11/F14–F18 | ✅ | ✅ | ✅ — quiet signals, visible rounds, distinguish sessions and attribution | ✅ — informs task titles and routing without granting authority |
| 17 | K17 / #17 | P5 — risk F1 | ✅ | ✅ | ✅ — shared-tree exact-path isolation | ✅ — governs Candidate and later TRACE commits |
| 18 | K18 / #18 | P5 — `TKL-20260913-01` | ✅ | ✅ | ✅ — qualified role/stage handovers instead of a global inventory | ✅ — scoped successor relation is preserved; D86/D87 remain applicable |
| 19 | K19 / #19 | P6 — iteration-1 RES D1–D10 | ✅ | ✅ | ✅ — receiver chronology, RCFR replay, census and conditional identity | ✅ — supplies empirical inputs to the approved design |
| 20 | K20 / #20 | P6 — iteration-2 RES D11–D21 | ✅ | ✅ | ✅ — traffic/carrier contract, optional principal, evidence ladder and six-edge oracle | ✅ — A3 correctly supersedes the proposed same-writer answer model |

## Checkpoint

**Self-check:**
- [x] Opened ≥ `⌈47 × 0.42⌉ = 20` files and recorded findings? (`47/47` VALUE plus ASSURANCE)
- [x] Independently established evidence applicability and ran necessary affected checks, or named the exact unresolved claim?
- [x] Claim & Source Checks filled — 2–3 key claims spot-checked, every citation traced to a real artifact, data claims checked against a primary source?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: `20`, resolved: `20`, semantically verified: `20`, irrelevant: `0`, hallucinated: `0`
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: `10` including accounting, verified: `10`, missing: `0`

Stage complete: YES

### Selected knowledge evidence

The actual Executor return and raw producer task record were inspected against the exact dispatch
lineage, Candidate and final TRACE read. Claude and `agy` results remain bound to their own native
session/conversation identities; the failed/contradictory earlier attempts are preserved rather than
overwritten. Source epochs and successor boundaries also hold: master A3 supersedes D83's active
AT/LEAD issuance; the iteration-2 authority decision supersedes its earlier same-writer proposal;
`TKL-20260913-01` is a scoped successor rather than a blanket replacement; D86/D87 remain in force.
The known D75 `112,536` historical inconsistency is not promoted into this phase's reproduced
accounting. No newer timestamp, Applied marker, clean tree or Coordinator statement was treated as
independent acceptance.
