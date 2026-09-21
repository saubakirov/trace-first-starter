# Verify — formal review round 2

> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims
> against reality.
> **Test:** If the RF disappeared, would the evidence alone prove the work was done?
> **Min verify ratio:** 0.42
> **RF files claimed:** 47 VALUE paths
> **Files initially required:** ceil(47 × 0.42) = 20
> **Escalation:** 100% after the evidence discrepancy; all 47 VALUE paths were checked.

## Verification Log

The approved literal selector resolves to 47 existing Candidate paths. Independent NUL-safe
accounting reproduces 46 modified paths and one zero-diff path, 1,675 additions plus 2,982 deletions,
4,657 touched text LOC and net −1,307; there is no binary or rename row. Paths outside the selector in
the Baseline→Candidate range are Phase A/B governing and TRACE history rather than extra product
implementation. Generated command copies were checked by Git blob identity.

| # | VALUE path | Actual at Candidate `93186cea…` | Match |
|---:|---|---|---|
| 1 | `.tfw/conventions.md` | Exact ≤1,400 Design Rules text and the prospectively ruled transcript-isolation constituent are present. | ✅ |
| 2 | `.tfw/glossary.md` | Exact Phase/Step/Stage/Gate owner text is present; Purpose Check link resolves. | ✅ |
| 3 | `.tfw/README.md` | Exists and is byte-identical to Baseline; the selector's sole zero-diff path. | ✅ |
| 4 | `.tfw/templates/HL.md` | Current filename and bounded handover guidance remain correct. | ✅ |
| 5 | `.tfw/templates/TS.md` | Single/phase/revision issuance guidance remains correct. | ✅ |
| 6 | `.tfw/templates/RES.md` | Fixed `research/iter{N}/RES.md` issuance remains correct. | ✅ |
| 7 | `.tfw/templates/ONB.md` | Single/phase issuance and handover guidance remain correct. | ✅ |
| 8 | `.tfw/templates/RF.md` | Filename/append and handover guidance remain correct. | ✅ |
| 9 | `.tfw/templates/REVIEW.md` | Filename/revision and handover guidance remain correct. | ✅ |
| 10 | `.tfw/templates/evidence/EV.md` | Evidence filename/append guidance remains correct. | ✅ |
| 11 | `.tfw/workflows/plan.md` | Exact AC-10 mindset and nine-step blocks occur in their two targeted regions; `Coordination`, preserved routing/state semantics and the gate-answered dispatch paragraph are present; 1,370 words. | ✅ |
| 12 | `.tfw/workflows/research/base.md` | Ordered actions use Step; true OODA/Stage terminology is retained; 1,014 words. | ✅ |
| 13 | `.tfw/workflows/handoff.md` | Ordered actions use Step and required recovery/evidence/accounting semantics remain; 937 words. | ✅ |
| 14 | `.tfw/workflows/review.md` | Ordered actions use Step; independence, escalation and return behavior remain; 1,005 words. | ✅ |
| 15 | `.tfw/workflows/docs.md` | Ordered actions use Step; shared routing remains linked; 739 words. | ✅ |
| 16 | `.tfw/workflows/knowledge.md` | Ordered actions use Step; qualification/currentness behavior remains; 1,042 words. | ✅ |
| 17 | `.tfw/workflows/release.md` | Ordered actions use Step; project-defined effect boundary remains; 726 words. | ✅ |
| 18 | `.tfw/workflows/update.md` | Ordered actions use Step; migration/adapter repair semantics remain; 1,003 words. | ✅ |
| 19 | `.tfw/workflows/config.md` | Edit/Verify Mode remains a real mode rather than an ordered Phase; 749 words. | ✅ |
| 20 | `.tfw/workflows/init.md` | Ordered actions use Step; conditional adapter repair remains; 1,209 words. | ✅ |
| 21 | `.tfw/adapters/codex/AGENTS.md.template` | Four capabilities are disclosed against current native mechanisms; bounded cursor wait is allowed and `read_thread`/`includeOutputs` monitoring is refused. | ✅ |
| 22 | `AGENTS.md` | Managed Codex block equals its source; foreign root content remains outside it. | ✅ |
| 23 | `.tfw/adapters/claude-code/CLAUDE.md.template` | Four capabilities stop at exposed/owner-assisted mechanisms; opening/resuming another role session is refused. | ✅ |
| 24 | `CLAUDE.md` | Managed Claude block equals its source; foreign content remains preserved. | ✅ |
| 25 | `.tfw/adapters/antigravity/tfw-rules.md.template` | Provider-local capability boundary and session isolation are explicit. | ✅ |
| 26 | `.agents/rules/tfw.md` | Git-blob-identical to the Antigravity source. | ✅ |
| 27 | `.tfw/adapters/cursor/tfw.mdc.template` | Future-target source makes owner-assisted/unavailable mechanics and session isolation explicit; no installed target is claimed. | ✅ |
| 28 | `.claude/commands/tfw-plan.md` | Blob-identical to canonical Plan. | ✅ |
| 29 | `.agents/workflows/tfw-plan.md` | Blob-identical to canonical Plan. | ✅ |
| 30 | `.claude/commands/tfw-research.md` | Blob-identical to canonical Research. | ✅ |
| 31 | `.agents/workflows/tfw-research.md` | Blob-identical to canonical Research. | ✅ |
| 32 | `.claude/commands/tfw-handoff.md` | Blob-identical to canonical Handoff. | ✅ |
| 33 | `.agents/workflows/tfw-handoff.md` | Blob-identical to canonical Handoff. | ✅ |
| 34 | `.claude/commands/tfw-review.md` | Blob-identical to canonical Review. | ✅ |
| 35 | `.agents/workflows/tfw-review.md` | Blob-identical to canonical Review. | ✅ |
| 36 | `.claude/commands/tfw-docs.md` | Blob-identical to canonical Docs. | ✅ |
| 37 | `.agents/workflows/tfw-docs.md` | Blob-identical to canonical Docs. | ✅ |
| 38 | `.claude/commands/tfw-knowledge.md` | Blob-identical to canonical Knowledge. | ✅ |
| 39 | `.agents/workflows/tfw-knowledge.md` | Blob-identical to canonical Knowledge. | ✅ |
| 40 | `.claude/commands/tfw-release.md` | Blob-identical to canonical Release. | ✅ |
| 41 | `.agents/workflows/tfw-release.md` | Blob-identical to canonical Release. | ✅ |
| 42 | `.claude/commands/tfw-update.md` | Blob-identical to canonical Update. | ✅ |
| 43 | `.agents/workflows/tfw-update.md` | Blob-identical to canonical Update. | ✅ |
| 44 | `.claude/commands/tfw-config.md` | Blob-identical to canonical Config. | ✅ |
| 45 | `.agents/workflows/tfw-config.md` | Blob-identical to canonical Config. | ✅ |
| 46 | `.claude/commands/tfw-init.md` | Blob-identical to canonical Init. | ✅ |
| 47 | `.agents/workflows/tfw-init.md` | Blob-identical to canonical Init. | ✅ |

## Commands Executed

| # | Command / independent check | Result |
|---:|---|---|
| 1 | Parse the TS-approved literal `$valuePaths`; inspect every Candidate blob; NUL-safe Baseline→Candidate `name-status`/`numstat` | PASS — 47/47 exist; 46 modified + 1 zero-diff; 1,675 + 2,982 = 4,657; net −1,307; text only; no rename. |
| 2 | Compare all Baseline→Candidate paths with selector membership and implementation chronology | PASS — VALUE changes are selector-only; other paths are governing/TRACE history; necessary-constituent ruling `68d85cc…` predates its eight VALUE writes. |
| 3 | `git diff --check 1a920953… 93186cea…` | PASS — no output. |
| 4 | Candidate detached worktree: `python -m pytest tools/tests/ docs/scripts/ -q` | PASS — 14 passed in 4.06s. |
| 5 | Candidate detached worktree: `python docs/scripts/command_entry_eval.py dry-run --repetitions 3` | PASS — `errors=[]`, valid, denominator 54. |
| 6 | `len(re.findall(r"\S+", text))` for ten canonical workflows | PASS — Plan 1,370; Research 1,014; Handoff 937; Review 1,005; Docs 739; Knowledge 1,042; Release 726; Update 1,003; Config 749; Init 1,209. |
| 7 | Manifest-derived Git blob comparison for ten canonical workflows and 20 Claude/Antigravity projections | PASS — 20/20 exact. |
| 8 | Candidate managed-block/full-copy SHA-256 comparison | PASS — Codex `dbe0c1…`, Claude `4d412a…`, Antigravity `dc42c…`; each installed surface equals its source. Cursor has no installed target. |
| 9 | Active-heading search plus relative-link resolution in changed VALUE Markdown | PASS — no operational `Phase N`, `Plan gates`, `## N.` or `Step N:` headings; 93 relative-style references found, nine intentional template placeholders excluded, 84/84 real links resolve. |
| 10 | Immutable historical audit module `25d0e89…` over the unchanged successor selector | PASS — historical 310,485→112,206 / 66,436→32,088; Phase B 114,221→110,512 / 37,818→33,220; per-command values reproduce. |
| 11 | Exact TS/ruling/Candidate text comparison and provider-source inspection | PASS for source state — both targeted AC-10 fragments, both AC-11 blocks and transcript rule are exact; dispatch retained; all seven provider surfaces carry the required mapping. |
| 12 | Current read-only receiver snapshots versus the recorded final epoch | BOUNDED PASS — KazNPU, AFD and RYC match their recorded tuples; Helpdesk is a later clean epoch, which neither verifies nor contradicts the recorded equal start/end tuple. |
| 13 | Audit `rung2-semantic-replay.txt` and search the task/repository for its named predicates or harness | DISCREPANCY — the file says an executed `python -` replay produced `EXACT OUTPUT`, but contains no reproduction command or executable predicate definitions; no corresponding source exists elsewhere. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---:|---|---|---|---|
| C1 | Historical and Phase B metric pairs | RF Return Round 2; EV E1-R2 | Immutable deleted audit module plus exact Baseline/Candidate Git blobs | ✅ — all totals reproduce and the two series remain separate. |
| C2 | 46 modified + 1 zero-diff; 4,657 touched LOC; no selector escape | RF accounting; EV E-accounting-R2 | Approved literal selector and exact Git objects | ✅ — membership and arithmetic reproduce. |
| C3 | Exact owner text, vocabulary, safe ceiling and provider disclosures | RF/EV E10-R2–E12-R2 | TS approval `116a324…`, ruling `68d85cc…`, Candidate blobs | ✅ for actual source state; the claimed rung-2 execution record is incomplete as described below. |
| C4 | D75 must change 112,536/−63.8% to 112,206/−63.9% | RF correction package | `KNOWLEDGE.md` D75, terminal RCFR RF/EV/REVIEW and immutable historical replay | ✅ — exact later `/tfw-docs` route remains required; `KNOWLEDGE.md` is untouched. |

## Discrepancies Found

1. **AC-3 / AC-10 / AC-12 — the required rung-2 semantic replay is not reproducible or
   traceable at predicate level.** `evidence/rung2-semantic-replay.txt` says an executed `python -`
   replay read named Git objects and then presents 32 named `PASS` outputs. Unlike the retained
   rung-1 evidence, it supplies neither the executed command nor the code that defines
   `scenario_owner_direct`, `scenario_invalid_continuation`, the provider cases or the isolation
   predicates; repository search finds no separate harness. The prose decision table states the
   expected answers but does not show how Candidate text was mapped to those answers or how a
   material-negative mutation was tested. Independent source inspection confirms the final text and
   provider mappings, but cannot authenticate the claimed execution or reconstruct its exact oracle.
   This breaches AC-3's positive/material-negative replay and traceability gate and leaves the replay
   portions of AC-10 and AC-12 unsupported. The minimal repair is evidence-only: preserve the exact
   executable command/harness, immutable refs, environment/version, predicates and output, then
   update EV/RF against that record; no Candidate VALUE change is presently indicated.

The discrepancy triggered full 47-path verification. The ledger's older header and path rows describe
the earlier Candidate epoch, but its explicit Return Round 2/3 section names final Candidate
`93186cea…`, records F16–F19 and states that all paths except `.tfw/README.md` are cumulative changes.
Those append-only historical dispositions therefore remain interpretable and are not treated as a
second finding.

## Evidence Verification

| # | RF evidence ref | Artifact exists? | Matches claim? |
|---:|---|---|---|
| E1 | `current-corpus-and-exposure.txt` | ✅ | ✅ — historical and current totals independently reproduce; denominators remain distinct. |
| E2 | `instruction-disposition-ledger.md` | ✅ | ✅ — original findings plus explicit Return Round 1 and Return Round 2/3 sections close the cumulative census and identify the final Candidate. |
| E3 | `six-edge-replay.md`, `rung1-semantic-replay.txt`, `rung2-semantic-replay.txt` | ✅ | ⚠️ partial — rung 1 is executable and exact; rung 2 has expected outputs but omits the command/harness that defines and produces them. |
| E4 | ledger plus exact Candidate accounting | ✅ | ✅ — owner/reader placement, ≤1,400 ceiling and subtraction claims hold; no new runtime/control surface exists. |
| E5 | `adapter-and-suite.txt` | ✅ | ✅ — 20/20 projection parity, source/installed parity and accepted Phase A provider ceilings hold. |
| E6 | `receiver-replay.md` | ✅ | ✅ for its stated final epoch — four start/end tuples are equal and repository-specific conclusions remain bounded. |
| E7 | configured suite and static checks in `adapter-and-suite.txt` | ✅ | ✅ — tests, dry-run, diff, links, headings, words and accounting reproduce. |
| E8 | RF D75 package | ✅ | ✅ — correction values and citations hold; source-owned edit is correctly deferred to closing. |
| E9 | REVIEW, D75 Docs effect/follow-up and terminal close | N/A yet | ✅ as DEFERRED — these are correctly downstream of this independent verdict. |
| E10 | AC-10 exact text/copy evidence | ✅ | ⚠️ partial — source text, word limit, links and copies hold; scenario-replay provenance inherits E3's gap. |
| E11 | AC-11 vocabulary/heading evidence | ✅ | ✅ — exact blocks and repository state independently reproduce. |
| E12 | AC-12 provider-entry evidence | ✅ | ⚠️ partial — all seven surfaces contain the required bounded wording; claimed executable entry/isolation scenarios inherit E3's gap. |
| E-accounting | `adapter-and-suite.txt` final table | ✅ | ✅ — exact refs, selector, statuses and arithmetic reproduce. |

## Knowledge Citations Verified

The master HL §7.2 list and all P0–P3/P5 source artifacts are byte-identical to the prior independent
review epoch; a direct Git comparison returned no changed source path. The master citation list itself
also has no diff. P4 `.tfw/conventions.md` changed and was freshly checked at Candidate. All 20 links
resolve, all named items exist, their meanings match, and their use remains relevant.

| # | Artifact | Priority + exact citation | Resolves / exists | Meaning and application |
|---:|---|---|---|---|
| 1 | K1 / ONB #1 | P0 — root `README.md`, preamble and `How It Works` | ✅ / ✅ | Durable inspectable continuation and divided responsibility; relevant. |
| 2 | K2 / #2 | P0 — `.tfw/README.md` NS1 | ✅ / ✅ | Purposeful, human-governed continuity; relevant. |
| 3 | K3 / #3 | P0 — NS2.2/2.4/2.5/2.7 | ✅ / ✅ | Simplest complete form, selected trace, bounded delegation and proportional assurance; relevant. |
| 4 | K4 / #4 | P0 — NS3 | ✅ / ✅ | No transcript, authority substitute, bureaucracy or vendor runtime; directly relevant to the new constituent. |
| 5 | K5 / #5 | P1 — Methodology Values | ✅ / ✅ | Structural enforcement, naming and portability; relevant. |
| 6 | K6 / #6 | P0 — Success Criteria | ✅ / ✅ | Resume, decision trace, qualified knowledge and acceptance-ready outcome; relevant. |
| 7 | K7 / #7 | P2 — philosophy F3/F4/F32/F37/F38/F40/F43/F45 | ✅ / ✅ | Opposition, gates, bounded mandates, finite attention and subtraction; relevant. |
| 8 | K8 / #8 | P3 — D23/D28/D31/D59/D73–D75 | ✅ / ✅ | Prior compression, naming, state, capabilities and selected reads; D75 conflict remains explicit. |
| 9 | K9 / #9 | P3 — D79/D81/D83/D84 | ✅ / ✅ | Navigation-only identity, human authority and historical team semantics; relevant. |
| 10 | K10 / #10 | P3 — D85/D86 | ✅ / ✅ | Receiver-safe evidence and finite closure; relevant. |
| 11 | K11 / #11 | P4 — HL Contract, Design Rules, Role Lock, anti-patterns | ✅ / ✅ | Fresh Candidate check confirms ≤1,400, exact-path/role boundaries and transcript isolation. |
| 12 | K12 / #12 | P5 — convention F1/F5/F19 | ✅ / ✅ | Canonical parity and naming consistency; relevant. |
| 13 | K13 / #13 | P5 — process F3–F5/F27/F30/F35/F37–F40/F43/F45/F47–F49 | ✅ / ✅ | Exact terms, ordered workflows, file-first evidence and reproducible counts; relevant. |
| 14 | K14 / #14 | P5 — constraint F2/F11/F12/F14 | ✅ / ✅ | Reader load, provider-local evidence and file-owned obligations; relevant. |
| 15 | K15 / #15 | P5 — environment F5/F6 | ✅ / ✅ | Provider topologies differ and cannot be translated into universal capability; relevant. |
| 16 | K16 / #16 | P5 — stakeholder F6–F8/F10–F11/F14–F18 | ✅ / ✅ | Quiet signals, visible rounds and session/unit distinction; relevant. |
| 17 | K17 / #17 | P5 — risk F1 | ✅ / ✅ | Exact-path shared-tree isolation; relevant. |
| 18 | K18 / #18 | P5 — `TKL-20260913-01` | ✅ / ✅ | Role/stage handovers and qualified records, not global inventory; relevant. |
| 19 | K19 / #19 | P5 — FRATS iteration-1 RES D1–D10 | ✅ / ✅ | Epochs, historical replay, filenames and reader/copy findings; relevant. |
| 20 | K20 / #20 | P5 — FRATS iteration-2 RES D11–D21 | ✅ / ✅ | Traffic, identity and six-edge oracle remain relevant; its pre-Phase-A provider ladder is correctly superseded by accepted Phase A evidence. |

## Checkpoint

**Self-check:**

- [x] Opened and recorded all 47/47 VALUE paths after discrepancy escalation.
- [x] Independently established prior-evidence applicability and reran changed or uncertain checks.
- [x] Claim & Source Checks filled; primary numerical sources and exact Git objects checked.
- [x] Each RF acceptance claim checked against Candidate and evidence.
- [x] `KNOWLEDGE.md` checked; D75 contradiction and authorized correction route remain documented.
- [x] Knowledge citations from HL §7.2 and ONB §7 verified.
  - Total: 20; resolved: 20; semantically verified: 20; irrelevant: 0; hallucinated: 0.
- [x] RF evidence artifacts verified.
  - Total indexed rows: 13; fully holding: 9; partial: 3; deferred: 1; missing files: 0.

Stage complete: **YES**

### Selected knowledge evidence

The selected lineage, immutable source epochs, Candidate commits, Phase A accepted provider evidence,
historical audit module, D75 terminal sources and all twenty knowledge citations were checked without
using another role's transcript, terminal, tool output or unreturned working tree. Unchanged inputs
reuse the prior independent verification; `.tfw/conventions.md`, the seven provider surfaces, revision-2
workflows and final evidence were checked afresh. Receiver conclusions remain bound to the recorded
equal start/end epoch; Helpdesk's later clean HEAD is not merged into that record.
