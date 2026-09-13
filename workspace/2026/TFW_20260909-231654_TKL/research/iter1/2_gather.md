# Gather — What do we NOT know?

> **Mindset:** Explorer; map alternatives before narrowing.
> Parent: [TKL HL](../../HL-TFW_20260909-231654_TKL.md)
> Goal: complete, usable knowledge continuity without global bookkeeping.
> Date: 2026-09-13 · Writer: robert · Role: Researcher · Mode: focused
> Authority and exact native lineage: [Briefing](1_briefing.md#authority-and-basis). Inspected repository basis: `3f4e59418c521dd22908662028351258288b89fb`.

## Dimensions

| Dimension | Alt A | Alt B | Alt C |
|---|---|---|---|
| D1 Capture timing | Final task close only | Every producing-role handover, with material interim checkpoint | Continuous note capture plus final synthesis |
| D2 Source ownership | Existing role artifacts and sections | One task file owned by its Coordinator | Independently named contributor/checkpoint files |
| D3 Qualification carrier | Existing shared category tables | Independently addressable project records | Qualification references attached to task-local sources |
| D4 Publication scheduling | Qualify every candidate before close | Complete material handover/disposition at close; qualify when needed | Periodic curator batch |
| D5 Retrieval | Maintained central map and topic inventory | Stable entry instructions plus ordinary file search and relation traversal | Optional generated view with ordinary-file fallback |
| D6 Correction and conflict | Update current record and preserve source/history | Append explicit replacement/resolution references | Keep divergent records unresolved pending authorized ruling |
| D7 Integration | Existing closer with handover evidence | Existing closer with mandatory promotion of everything | Separate knowledge-closing worker |
| D8 Migration | Keep current carriers as compatible legacy inputs | Bounded approved conversion preserving old links | Immediate wholesale rewrite and state reset |

Options are not endorsed in this stage; incompatibilities are evaluated in Extract.

## Findings

### G1. Current responsibility map: capture and qualification are not one operation

Paths below are repository-relative and refer to the inspected basis, not proposed outputs.

| Job | Actual owner and input/output | Gap or consequence for TKL |
|---|---|---|
| Planning capture | Coordinator, `.tfw/workflows/plan.md` Step 4 and HL §11 | End-of-artifact capture; the section does not establish that every contributing participant handed over context |
| Research capture | Researcher, research workflow synthesis, `RES.md` Fact Candidates and Strategic Insights | Final RES is a useful source; interrupted work also has stage files, which the global gate intentionally does not select |
| Execution capture | Executor, `.tfw/workflows/handoff.md` Phase 3 and RF §§7–8; observation/debt uses its distinct route | Existing required sections are reusable; a final RF cannot protect an earlier lost context by itself |
| Independent contribution | Reviewer, review trust protocol and REVIEW §7 | Reviewer writes its own candidates and challenges unjustified absence; PTTC's prohibition on Reviewer “capture” means Coordinator-owned docs/knowledge effects, not a prohibition on Reviewer-authored observations |
| Technical reference capture | Coordinator, `.tfw/workflows/docs.md`; KNOWLEDGE §§1–3 and selected convention range | Map, decisions, artifact navigation and deprecation are distinct from human-only fact consolidation; each function needs a home if the central file changes |
| Qualification | Coordinator, `.tfw/workflows/knowledge.md` Phases 2–3; selected task sections and conversation → approved category changes | Human-only filter; deduplication; contradictions go to the user; source multiplicity/confirmation and approval are separate steps. More copies of one account are not independent grounds |
| Promotion and bookkeeping | Same knowledge owner; source processed markers → topic tables → KNOWLEDGE §4 → post-marker digests/state last | Multiple shared writes, immutable-source tension and retry coupling; the approved disposition ledger exists only as a write plan, not proof that every role contributed |
| Access | Plan Step 3 PV/knowledge citations; handoff ONB §7; research/read contracts; root KNOWLEDGE map and topic links | Required governing context precedes relevant knowledge. A retrieval design must preserve this ordering and require application of relevant sources |
| Close and recovery | Existing Coordinator, `.tfw/conventions.md` → Closing and record recovery; REVIEW §6 is the existing carrier | Actual effects and independent acceptance of changed final claims precede DONE. Deferred/pending dispositions ordinarily keep close open; record repair alone starts no capture cycle |
| Update/init | `.tfw/workflows/update.md`, conventions File Classification; framework template versus receiver state | State/history/knowledge are preserved, not upstream payload. A compatible migration needs explicit guide authority; deleting a state file cannot masquerade as completed consolidation |

The selected cross-cutting read exceeded the soft fifteen-project-file limit: the actual producer, consumer, close and update contracts plus dependency controls were necessary to map the whole lifecycle. This is a bounded iteration investigation, not a proposed routine historical scan.

### G2. The gate is both overinclusive and underinclusive for the desired obligation

The [canonical algorithm](../../../../../.tfw/workflows/knowledge.md#canonical-knowledge-gate-algorithm) selects artifact basenames and named sections, hashes them for every discovered task, and compares the result to `.tfw/knowledge_state.yaml`. Eligibility does not depend on lifecycle, sealing, participant completeness, materiality or a recorded close disposition. Thus changed historical prose can be pending while unrecorded participant knowledge is invisible. A no-section task receives SHA-256 of exactly two NUL bytes; a missing saved entry can make even that task pending.

A further observed selection gap: canonical research files are named `research/iterN/RES.md`, but the gate accepts `RES__*.md`, not `RES.md`. `RF-TFW_20260906-190312_CRUE.md` is also outside its `RF__` selector. SLC has two actual `RES.md` files with candidate sections; the optional source reader selects only its HL. This is not a proposal to rename sealed history or repair a glob as the complete TKL solution. It shows why a content-change counter cannot establish handover completeness.

One read-only diagnostic was run using the existing upstream `tools/tfw_state.py`, Python 3.13.5 and PyYAML 6.0.3, with `python -B -` to avoid bytecode writes. This is optional maintainer corroboration, not execution of a workflow gate or an ordinary receiver requirement. Canonical steps were read independently. The first wrapper run reported pending IDs then failed with `KeyError: 'tfw'` because `read_config` already returns that block; the corrected wrapper semantically loaded the full YAML. No state write occurred in either run. Corrected exit: 0.

```text
knowledge_pending(Path.cwd()) at 3f4e59418c521dd22908662028351258288b89fb:
pending_task_ids:
  TFW_20260906-190312_CRUE
  TFW_20260907-020729_SLC
  TFW_20260907-133942_PTTC
  TFW_20260909-231654_TKL
removed_task_ids: []
problems: []
migration_required: false
knowledge_gate_result('hard', 5, pending): action=continue, delta=4, interval=5
EMPTY_KNOWLEDGE_DIGEST:
  96a296d224f285c67bee93c30f8a309157f0daa35dc5b87e410b78630a09cfc7
SLC selected_paths: [workspace/2026/TFW_20260907-020729_SLC/HL-TFW_20260907-020729_SLC.md]
SLC selected_sections: 1
SLC digest: 178d5d0a29458d8fb819fe293486ba5d246270da12f5818e7eeda237739b5b5e
Direct helper call on absent OTR path: selected_sections=0; digest=EMPTY_KNOWLEDGE_DIGEST
  (not a discovered task and not evidence of a real empty task; see correction below)
KNOWLEDGE_ARTIFACT.fullmatch:
  RES.md=False; RES__example.md=True
  RF-TFW_20260906-190312_CRUE.md=False; RF__example.md=True
```

Reproduce by importing `tfw_state` from `tools`, calling `knowledge_pending(Path.cwd())`, then `selected_knowledge_sections(root, root / task_path)` and inspecting `KNOWLEDGE_ARTIFACT.fullmatch` for the named basenames. This number is a dated clean-worktree observation. The original reported 27 is not reproduced or explained by it. TFW-36's known gitignored inputs can differ in another worktree; the earlier legacy-heading and POSIX-sort mistakes remain reported calculation defects, not new knowledge. No subtraction across these different snapshots establishes a historical cause.

Challenge-stage correction: the attempted OTR empty-task probe used the path mentioned by the HL without first checking existence. A follow-up returned `OTR_discovered=false`, `OTR_prior=null`, `OTR_direct_path_exists=false`; reading its status reported a missing path. The direct helper accepts a nonexistent path and returns no sections. Therefore its empty digest is not an observation of an existing OTR task. The four-ID discovery result remains valid; the no-section-new-task consequence follows the canonical algorithm and the explicit two-NUL calculation, not this absent path. OTR is excluded from the research scope and was not reconstructed or edited.

### G3. PTTC supplies an actual finite interface; SLC supplies a current planning boundary

[PTTC status](../../../TFW_20260907-133942_PTTC/status.md) is DONE. Its [B RF](../../../TFW_20260907-133942_PTTC/phase-b/RF__phase-b__finite_closure_and_recovery.md) identifies Candidate `edf6d8261b12451c3ceb3cb5a9a6244bc3b47d1c`; the [independent REVIEW](../../../TFW_20260907-133942_PTTC/phase-b/REVIEW__phase-b__finite_closure_and_recovery.md) approves those effects and separately records acceptance of final documentation changes. REVIEW §6 later records actual landing and close. Its six native cases in one receiver include B1 record recovery, B2 a real failure/correction and independent acceptance, and B5 selected close despite an unrelated TODO. B6 contains a preserved disagreement; no universal behavior or speedup follows. PTTC intentionally changed only knowledge Phase 4's effect-return route, leaving digest discovery and state ordering intact.

PTTC parent triage explicitly approved knowledge N/A for new publication while leaving the ordinary pending batch unprocessed. [CRUE's closing event](../../../TFW_20260906-190312_CRUE/journal/20260908-082533__transition__2b86.md) separately preserves the owner's earlier explicit knowledge deferral. Both DONE tasks remain pending in G2. Their historical rulings must survive; neither becomes a default permission for future tasks to omit required capture.

[SLC status](../../../TFW_20260907-020729_SLC/status.md) is TS_DRAFT, updated `20260909-145128`. Its ordered journal ends at the same-Coordinator TS return `20260909-150355__dispatch__6993.md`. Its [draft TS](../../../TFW_20260907-020729_SLC/TS__TFW_20260907-020729_SLC.md) proposes active versus historical containers, a bounded digest-removal exception and recoverable update cases; the tree contains no delivered RF/REVIEW. Its stale draft still calls PTTC B unaccepted; that describes its drafting epoch, not current PTTC. TKL may study the intended interfaces but must consume SLC's accepted actual result before final design/shared implementation. No SLC file was changed.

The legacy [TFW-60 HL A8](../../../../../tasks/TFW-60__conflict_resistant_shared_workspace/HL-TFW-60__conflict_resistant_shared_workspace.md) dropped task-local knowledge Phase C and sealed the legacy corpus. It supplies rationale and a preservation boundary, not inherited implementation authority.

### G4. External pattern evidence and its limits

- [Nygard, decision records](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions): small records preserve context, choice and consequences. His mutable superseded status and sequential IDs are not adopted by implication; TFW needs correction links that leave sealed sources untouched.
- [LangChain, memory overview](https://docs.langchain.com/oss/python/concepts/memory): a collection shifts work toward reconciliation and retrieval; immediate versus background capture has different latency and availability costs. This does not establish which TFW handover is sufficient.
- [Microsoft, event sourcing](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing): immutable inputs and rebuildable projections illustrate source/view separation; idempotency and ordering remain explicit responsibilities. A full event platform is neither necessary nor proposed.
- [Git merge documentation](https://git-scm.com/docs/git-merge): merging operates on the heads and merge base; distinct textual changes may merge automatically. Inference for TKL: a clean merge cannot certify that independently authored knowledge claims agree.

Accessed 2026-09-13. These primary sources are pattern evidence; actual TFW behavior comes from named repository sources and bounded observations above.

## Checkpoint

| Found | Remaining |
|---|---|
| Existing role artifacts and existing closer are usable integration sites | Minimum material handover and qualification scheduling |
| Global digest change is neither task closure nor contribution completeness | Complete alternatives and replacement of every central function |
| PTTC accepted; SLC still a draft dependency | SLC's future accepted integration interface |
| Ordinary files preserve sources but do not solve semantic consistency by filename | Conflict and stale-match behavior; independent consumer evidence |

OBSERVE: source contracts, optional diagnostic and primary patterns. ORIENT: distinguish capture, publication and authority. DECIDE: compare full lifecycle configurations, not a gate toggle. ACT: carry D1–D8 into Extract.

**Sufficiency:** External source used: YES. Briefing gap closed for responsibility mapping: YES. Dimensions identified: YES. Recommendation: close Gather; advance under the existing focused dispatch. No additional owner decision requested.

Stage complete: YES
