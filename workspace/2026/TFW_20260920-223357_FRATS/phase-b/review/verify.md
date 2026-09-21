# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> **Min verify ratio:** 0.42
> **RF files claimed:** 47 VALUE paths
> **Files initially required:** ⌈47 × 0.42⌉ = 20
> **Escalation:** 100% after the first evidence discrepancy; all 47 VALUE paths were checked.

## Verification Log

The literal selector resolves to 47 existing Candidate paths. Independent accounting reproduces 39
modified and eight zero-diff paths, 365 additions plus 507 deletions, 872 touched text LOC and net
−142. The implementation range `72d73a5…fd0655c` contains only selector members. The table records
every VALUE path; generated copies were checked by Git blob identity rather than sampled prose.

| # | VALUE path | Actual at Candidate | Match |
|---:|---|---|---|
| 1 | `.tfw/conventions.md` | F1 and F4–F9 repairs/consolidations are present. The unchanged `Design Rules` still requires workflow instructions ≤1200 words, while four Candidate workflows exceed it. | ⚠️ partial |
| 2 | `.tfw/glossary.md` | `Deferral confession` now resolves to Review `Purpose Check`. | ✅ |
| 3 | `.tfw/README.md` | Exists and is byte-identical to Baseline. | ✅ |
| 4 | `.tfw/templates/HL.md` | Exact current filename guidance and compact handover fields are present. | ✅ |
| 5 | `.tfw/templates/TS.md` | Exact single/phase/revision filename guidance is present. | ✅ |
| 6 | `.tfw/templates/RES.md` | Fixed `research/iter{N}/RES.md` issuance and compact handover are present. | ✅ |
| 7 | `.tfw/templates/ONB.md` | Exact single/phase filename guidance and compact handover are present. | ✅ |
| 8 | `.tfw/templates/RF.md` | Exact filename/append guidance and compact handover are present. | ✅ |
| 9 | `.tfw/templates/REVIEW.md` | Exact filename/revision guidance and compact handover are present. | ✅ |
| 10 | `.tfw/templates/evidence/EV.md` | Exact evidence filename/append guidance is present; stale names footer was removed. | ✅ |
| 11 | `.tfw/workflows/plan.md` | Routing/handover prose is consolidated and filename emission is repaired, but the file is 1,433 words against the active ≤1,200 rule. | ❌ |
| 12 | `.tfw/workflows/research/base.md` | Consolidation and fixed RES issuance are present; 1,007 words. | ✅ |
| 13 | `.tfw/workflows/handoff.md` | Consolidation and exact ONB/EV/RF issuance are present, but the file is 2,101 words against the active ≤1,200 rule. | ❌ |
| 14 | `.tfw/workflows/review.md` | Consolidation and exact REVIEW issuance are present, but the file is 2,136 words against the active ≤1,200 rule. | ❌ |
| 15 | `.tfw/workflows/docs.md` | Shared handover route replaces repeated prose; 733 words. | ✅ |
| 16 | `.tfw/workflows/knowledge.md` | Shared handover route replaces repeated prose; 1,038 words. | ✅ |
| 17 | `.tfw/workflows/release.md` | Task-local routing is read first and shared prose is consolidated; 718 words. | ✅ |
| 18 | `.tfw/workflows/update.md` | Task-local routing and conditional adapter read are present, but the file grows from 2,619 to 2,630 words and remains above the active ≤1,200 rule. | ❌ |
| 19 | `.tfw/workflows/config.md` | Explicit activation checkpoint and corrected config description are present; 748 words. | ✅ |
| 20 | `.tfw/workflows/init.md` | Conditional adapter-repair read is present; 1,197 words. | ✅ |
| 21 | `.tfw/adapters/codex/AGENTS.md.template` | Zero-diff; managed block remains required bootstrap/recovery content. | ✅ |
| 22 | `AGENTS.md` | Zero-diff; managed Codex block equals its source and foreign project content remains outside it. | ✅ |
| 23 | `.tfw/adapters/claude-code/CLAUDE.md.template` | Zero-diff; provider-local bootstrap remains bounded. | ✅ |
| 24 | `CLAUDE.md` | Zero-diff; managed Claude block equals its source. | ✅ |
| 25 | `.tfw/adapters/antigravity/tfw-rules.md.template` | Zero-diff. | ✅ |
| 26 | `.agents/rules/tfw.md` | Zero-diff and Git-blob-identical to its Antigravity source. | ✅ |
| 27 | `.tfw/adapters/cursor/tfw.mdc.template` | Zero-diff; no installed Cursor target is claimed. | ✅ |
| 28 | `.claude/commands/tfw-plan.md` | Blob-identical to canonical Plan. | ✅ parity; inherits canonical word-limit finding |
| 29 | `.agents/workflows/tfw-plan.md` | Blob-identical to canonical Plan. | ✅ parity; inherits canonical word-limit finding |
| 30 | `.claude/commands/tfw-research.md` | Blob-identical to canonical Research. | ✅ |
| 31 | `.agents/workflows/tfw-research.md` | Blob-identical to canonical Research. | ✅ |
| 32 | `.claude/commands/tfw-handoff.md` | Blob-identical to canonical Handoff. | ✅ parity; inherits canonical word-limit finding |
| 33 | `.agents/workflows/tfw-handoff.md` | Blob-identical to canonical Handoff. | ✅ parity; inherits canonical word-limit finding |
| 34 | `.claude/commands/tfw-review.md` | Blob-identical to canonical Review. | ✅ parity; inherits canonical word-limit finding |
| 35 | `.agents/workflows/tfw-review.md` | Blob-identical to canonical Review. | ✅ parity; inherits canonical word-limit finding |
| 36 | `.claude/commands/tfw-docs.md` | Blob-identical to canonical Docs. | ✅ |
| 37 | `.agents/workflows/tfw-docs.md` | Blob-identical to canonical Docs. | ✅ |
| 38 | `.claude/commands/tfw-knowledge.md` | Blob-identical to canonical Knowledge. | ✅ |
| 39 | `.agents/workflows/tfw-knowledge.md` | Blob-identical to canonical Knowledge. | ✅ |
| 40 | `.claude/commands/tfw-release.md` | Blob-identical to canonical Release. | ✅ |
| 41 | `.agents/workflows/tfw-release.md` | Blob-identical to canonical Release. | ✅ |
| 42 | `.claude/commands/tfw-update.md` | Blob-identical to canonical Update. | ✅ parity; inherits canonical word-limit finding |
| 43 | `.agents/workflows/tfw-update.md` | Blob-identical to canonical Update. | ✅ parity; inherits canonical word-limit finding |
| 44 | `.claude/commands/tfw-config.md` | Blob-identical to canonical Config. | ✅ |
| 45 | `.agents/workflows/tfw-config.md` | Blob-identical to canonical Config. | ✅ |
| 46 | `.claude/commands/tfw-init.md` | Blob-identical to canonical Init. | ✅ |
| 47 | `.agents/workflows/tfw-init.md` | Blob-identical to canonical Init. | ✅ |

## Commands Executed

| # | Command / check | Result |
|---:|---|---|
| 1 | Parse the approved literal `$valuePaths`; `git cat-file -e`; Baseline→Candidate `--numstat` | PASS — 47/47 exist; 39 changed, 8 zero-diff; 365 + 507 = 872; net −142; no binary row. |
| 2 | Compare implementation range `72d73a5…fd0655c` with selector membership | PASS — 39 paths, all inside the selector; no ASSURANCE or other implementation path. |
| 3 | `git diff --check 1a920953… fd0655ce…` | PASS — no output. |
| 4 | `len(re.findall(r"\S+", text))` for all ten canonical workflows at Baseline and Candidate | FAIL — Candidate Plan 1,433; Handoff 2,101; Review 2,136; Update 2,630, each above `.tfw/conventions.md` `Design Rules` ≤1,200. Research 1,007 and Init 1,197 newly clear the bound. |
| 5 | Manifest-derived Git blob comparison for ten canonical workflows and 20 Claude/Antigravity copies | PASS — 20/20 exact. |
| 6 | Candidate managed-block SHA-256 and Antigravity Git blob comparison | PASS — Codex `ee79…ad`, Claude `eaab…e6`, Antigravity `044608…abe`; source equals target. Cursor source `bd9e…07f`, installed target absent as declared. |
| 7 | Candidate detached worktree: `python -m pytest tools/tests/ docs/scripts/ -q` | PASS — 14 passed in 7.55s. |
| 8 | Candidate detached worktree: same suite with `--collect-only` | PASS — 14 collected. |
| 9 | Candidate detached worktree: `python docs/scripts/command_entry_eval.py dry-run --repetitions 1` | PASS — `errors=[]`, valid, denominator 18. |
| 10 | Detached historical `25d0e89…`: `python docs/scripts/test_runtime_context.py --audit --baseline-ref cf36dd6…` | PASS — trajectory 310,485→112,206 (63.9%); active corpus 66,436→32,088 (51.7%). |
| 11 | Independently execute the immutable historical audit module in memory over Phase B Baseline/Candidate with Resume removed symmetrically | PASS — trajectory 114,221→113,405; active corpus 37,818→37,061; per-command values equal the evidence transcript. |
| 12 | Resolve validator paths and inspect the native Executor record | DISCREPANCY — the replay actually imported `from tools import tfw_state`; `tools/tfw_state.py` exists, `.tfw/scripts/tfw_state.py` does not. |
| 13 | Read-only receiver snapshots after the recorded epoch | BOUNDED — Helpdesk, AFD and RYC still match the recorded tuples; KazNPU is now a later clean epoch at `b91184f…`, so it neither verifies nor contradicts the earlier matched start/end epoch. |
| 14 | Native Executor staging/commit record | PASS — Candidate commits used explicit path lists and `git commit --only`; later TRACE/RF and transition commits used exact path lists; unrelated untracked work remained unstaged. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---:|---|---|---|---|
| C1 | Historical and current metric pairs | RF §1/§2; EV E1 | Fresh immutable historical replay and independent in-memory successor execution | ✅ — all four pairs and per-command totals reproduce. |
| C2 | “39 modified + 8 zero-diff; 365 + 507 = 872; no selector escape” | RF §1/§4; EV `E-accounting` | Git objects at exact Baseline/Candidate and literal approved selector | ✅ — exact membership and arithmetic reproduce. |
| C3 | “Phase A provider evidence remains … Codex P2 and Claude P0” | `adapter-and-suite.txt`; `receiver-replay.md`; RF §4; EV E5 | Accepted Phase A RF and independent APPROVE REVIEW; master HL at Phase B approval | ❌ — accepted Phase A records Codex P2/partial P3, authenticated Claude P2 and Antigravity P2/partial P3. `Claude P0` is the pre-Phase-A research ceiling, not the inherited Phase A result. |
| C4 | D75 must change `112,536/−63.8%` to `112,206/−63.9%` | RF §2/§6 | `KNOWLEDGE.md` D75; terminal RCFR Phase C RF line 185; EV E7; REVIEW rev3; fresh immutable replay | ✅ — the proposed replacement is source-supported and remains correctly routed to later `/tfw-docs`. |

## Discrepancies Found

1. **AC-2 / AC-4 — undispositioned active workflow-limit contradictions.** Candidate Plan (1,433),
   Handoff (2,101), Review (2,136) and Update (2,630) violate the active `Design Rules` limit of
   ≤1,200 words. The ledger gives no preserve/consolidate/remove/repair disposition for those four
   contradictions and claims the census closed. Update grows by 11 words. The smallest internally
   consistent corpus and “every detected contradiction once” claims are therefore unproved.
2. **AC-3 — evidence names a nonexistent validator path.** `six-edge-replay.md` says the real
   validator is `.tfw/scripts/tfw_state.py`; that path does not exist. The native producer record
   shows that the actual replay used `tools/tfw_state.py`, so this is a repairable evidence/citation
   defect rather than proof that the event checks did not run. Until corrected, E3 is not fully
   self-resolving and the Reviewer cannot trace the stated oracle solely from the evidence artifact.
3. **AC-5 / inherited Phase A result — stale provider ceiling.** Phase B RF and two evidence files
   say `Codex P2/Claude P0`. Phase A's accepted RF and independent REVIEW instead establish Codex
   P2/partial P3, authenticated Claude P2 and Antigravity P2/partial P3, with no full P3/P4 or
   reliability rate. The Phase B TS requires Phase A evidence to remain bounded *as recorded*.
   EV E5 is therefore incorrectly marked VERIFIED, and RF §4 gives the owner a stale limit.

The first discrepancy triggered full 47-path verification as required.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|---|---|---|
| E1 | `current-corpus-and-exposure.txt` | ✅ | ✅ — historical and successor numbers reproduce independently; denominators remain separated. |
| E2 | `instruction-disposition-ledger.md` | ✅ | ❌ — all 47 paths are listed, but four active ≤1,200 workflow violations have no disposition, so the claimed closed census is incomplete. |
| E3 | `six-edge-replay.md` | ✅ | ⚠️ partial — native execution used the real validator, but the artifact cites a nonexistent path. |
| E4 | ledger + `adapter-and-suite.txt` | ✅ | ❌ — canonical ownership/parity holds, but “maximum justified subtraction” and closed contradictions do not hold while four workflows violate the active limit without disposition. |
| E5 | `adapter-and-suite.txt` | ✅ | ❌ — 20/20 copy and persistent parity hold; inherited provider ceiling is stale (`Claude P0` versus accepted Phase A `Claude P2`). |
| E6 | `receiver-replay.md` | ✅ | ✅ for its stated epoch — start/end tuples are internally complete and bounded; current KazNPU is explicitly a later epoch. The file's separate `Claude P0` interpretation is stale and belongs to discrepancy 3. |
| E7 | `adapter-and-suite.txt` | ✅ | ✅ — tests, dry-run, diff and accounting reproduce. |
| E8 | Phase B RF | ✅ | ✅ — metric explanation, D75 replacement/citations and later route hold; `KNOWLEDGE.md` was not edited. |
| E9 | downstream REVIEW/docs/closure | N/A yet | ✅ as DEFERRED — the missing outputs are downstream and named exactly. |
| E-accounting | `adapter-and-suite.txt` | ✅ | ✅ — exact refs, selector, actions and arithmetic reproduce. |

Actual evidence disposition at review time is not the stated `9/10 VERIFIED`: E2, E4 and E5 are
contradicted, E3 is partial, E9 remains deferred, and E1/E6/E7/E8/E-accounting hold. The Executor must
repair and reissue the evidence verdict; the Reviewer does not rewrite Executor-owned EV/RF.

## Knowledge Citations Verified

All 20 HL §7.2 links resolve at the Phase B approval epoch, all named items exist, and their stated
meanings are relevant. K20's pre-Phase-A `Claude P0` research fact is real but was later superseded by
accepted Phase A native evidence; applying it as the current inherited ceiling is the discrepancy,
not a hallucinated citation.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---:|---|---|---|---|---|---|
| 1 | K1 / ONB #1 | P0 — root `README.md`, preamble and `How It Works` | ✅ | ✅ | ✅ — inspectable durable continuation and divided responsibility | ✅ |
| 2 | K2 / #2 | P0 — `.tfw/README.md` NS1 | ✅ | ✅ | ✅ — purposeful, human-governed continuity | ✅ |
| 3 | K3 / #3 | P0 — NS2.2/2.4/2.5/2.7 | ✅ | ✅ | ✅ — simplest complete form, selected trace, bounded delegation, proportional assurance | ✅ |
| 4 | K4 / #4 | P0 — NS3 | ✅ | ✅ | ✅ — no transcript, authority substitute, bureaucracy or vendor runtime | ✅ |
| 5 | K5 / #5 | P1 — Methodology Values | ✅ | ✅ | ✅ — structural enforcement, naming and portability | ✅ |
| 6 | K6 / #6 | P0 — Success Criteria | ✅ | ✅ | ✅ — resume, decision trace, qualified knowledge, acceptance-ready outcome | ✅ |
| 7 | K7 / #7 | P2 — philosophy F3/F4/F32/F37/F38/F40/F43/F45 | ✅ | ✅ | ✅ — opposition, gates, bounded mandates, finite attention, compression/subtraction | ✅ |
| 8 | K8 / #8 | P3 — D23/D28/D31/D59/D73–D75 | ✅ | ✅ | ✅ — prior compression, naming, state, capabilities and selected reads; D75 conflict is explicit | ✅ |
| 9 | K9 / #9 | P3 — D79/D81/D83/D84 | ✅ | ✅ | ✅ — navigation-only identity, human authority and historical team semantics | ✅ |
| 10 | K10 / #10 | P3 — D85/D86 | ✅ | ✅ | ✅ — receiver-safe evidence and finite closure | ✅ |
| 11 | K11 / #11 | P4 — HL Contract, Design Rules, Role Lock, anti-patterns | ✅ | ✅ | ✅ — includes the active ≤1,200 workflow rule that exposes discrepancy 1 | ✅ |
| 12 | K12 / #12 | P5 — convention F1/F5/F19 | ✅ | ✅ | ✅ — canonical parity and naming consistency | ✅ |
| 13 | K13 / #13 | P5 — process F3–F5/F27/F30/F35/F37–F40/F43/F45/F47–F49 | ✅ | ✅ | ✅ — exact terms, ordered workflows, file-first evidence, reproducible counts | ✅ |
| 14 | K14 / #14 | P5 — constraint F2/F11/F12/F14 | ✅ | ✅ | ✅ — reader load, provider-local evidence and file-owned obligations | ✅ |
| 15 | K15 / #15 | P5 — environment F5/F6 | ✅ | ✅ | ✅ — provider strengths/topologies differ; no translated universal claim | ✅ |
| 16 | K16 / #16 | P5 — stakeholder F6–F8/F10–F11/F14–F18 | ✅ | ✅ | ✅ — quiet signals, visible rounds, session/unit distinction | ✅ |
| 17 | K17 / #17 | P5 — risk F1 | ✅ | ✅ | ✅ — exact-path shared-tree isolation | ✅ |
| 18 | K18 / #18 | P5 — `TKL-20260913-01` | ✅ | ✅ | ✅ — role/stage handovers and qualified records, no global inventory | ✅ |
| 19 | K19 / #19 | P5 — FRATS iteration-1 RES D1–D10 | ✅ | ✅ | ✅ — epochs, exact historical replay, filename and reader/copy findings | ✅ |
| 20 | K20 / #20 | P5 — FRATS iteration-2 RES D11–D21 | ✅ | ✅ | ✅ — traffic, identity, six-edge oracle and then-current P2/P0 ladder | ✅ with currentness caveat — accepted Phase A later supersedes the Claude ceiling |

## Checkpoint

**Self-check:**
- [x] Opened and recorded all 47/47 VALUE paths after discrepancy escalation?
- [x] Independently established evidence applicability and reran affected checks?
- [x] Claim & Source Checks filled; primary numerical sources and exact Git objects checked?
- [x] Each RF §3 acceptance claim checked against Candidate/evidence?
- [x] `KNOWLEDGE.md` checked; D75 contradiction and authorized correction route documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 20, resolved: 20, semantically verified: 20, irrelevant: 0, hallucinated: 0; one superseded application recorded.
- [x] Evidence artifacts from RF §5 verified?
  - Total: 10, fully holding: 5, contradicted: 3, partial: 1, deferred: 1, missing artifacts: 0.

Stage complete: YES

### Selected knowledge evidence

The actual Executor return, Candidate/staging record, both FRATS research returns, the accepted Phase
A RF/EV/REVIEW, RCFR terminal sources and all twenty selected citations were inspected. The
iteration-2 P2/P0 ladder is a valid pre-Phase-A research epoch, but Phase A's later native evidence
is the applicable successor for Phase B. D75 remains a source-owned publication inconsistency: the
terminal RCFR RF/EV/REVIEW and fresh immutable replay converge on 112,206/32,088, while the accepted
`/tfw-docs` effect has not yet occurred. `TKL-20260913-01` has no later incoming relation that changes
its relevant role/stage-handover rule. Receiver conclusions remain bound to their recorded epoch;
the later KazNPU HEAD is not merged into that evidence.
