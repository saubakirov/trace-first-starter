# Gather — Separate carrier effects from semantic obligations

> **Mindset:** Explorer; verify the current dependency rather than repeat the old snapshot.
> Parent: [TKL HL](../../HL-TFW_20260909-231654_TKL.md)
> Goal: identify what C3 changes, what C1 can also do, and which currentness evidence is still missing.
> Date: 2026-09-13 · Writer: robert · Role: Researcher · Focused iteration 2
> Authority: [Briefing](1_briefing.md#authority-and-resolved-inputs).

## Dimensions and comparison matrix

Only two independent choices remain open for this focused iteration: **publication carrier** (refined C1 topics, C3 independent records, mixed legacy/current records) and **currentness access** (curated current entry, ordinary-file relation search, optional derived view with fallback). Capture completeness, truth/authority, sealed history and the existing closer are requirements common to every choice, not optional axes. Use the template's below-three-dimension comparison matrix.

| Design | Capture / ownership | Qualification/currentness | Principal cost and unknown |
|---|---|---|---|
| Refined C1 | Existing role artifacts; shared topics have one publication owner | Update current row with source/version and decision; preserve older source and scoped historical meaning | Same-topic serialization and current-row correction; familiar retrieval. Counts/inventory/digests/processed markers still retire |
| C3 | Same sources; independently owned project records | Append qualified record and explicit relations; readers inspect relevant reverse references | Independent write paths; more relation traversal and stale-branch risk; fresh consumer untested |
| Mixed legacy/current C3 | Preserve historical topics and D rows; new records for subsequent changes | New record names exact old fact/decision identity; current entry explains both sources | Avoid bulk conversion; old facts cannot be treated as current without checking later relations |

## Findings

### G1. Current SLC is accepted outside the old TKL baseline

At merged intake `82d2b3c4485fc4f0bcfb2f80024f43df9b4a0e28`, the worktree copy still says SLC TS_DRAFT. A selected `git log --all -5 --format='%h %s' -- workspace/2026/TFW_20260907-020729_SLC` found later review and close. This disproves a present-tense claim that SLC has no accepted result. No branch was merged and no SLC source was edited.

| Exact Git evidence | Observed meaning |
|---|---|
| Closing commit `c51ee0c0d7891fd165d105f3565e0e54512c1040`, `status.md` | SLC DONE, updated `20260910-132537`; accepted workspace/default and compatible historical access |
| Same commit, `journal/20260910-132537__transition__803f.md` | Actual KNW → DONE after independent C2 approval, terminal dispositions, capture and checked landing |
| Final independent REVIEW producer `99198f133c0047568c1e8411bfae849239b352b1` | Same independent Reviewer accepts corrected C2 and actual final output; original negative epochs remain |
| Replacement Candidate `433d9db62905e16786113af9bfe126a89c21b9a5` | Corrected implementation; supersedes first Candidate `05c6fcdfe6a1c1b4e9615f0390d094ee1b1fb5e8` as delivered subject |
| RF/EV return `52159e4afdf961bc5f4077ef3cc011d98c05e0b1`; final reviewed composition `dd34cacfe88f095a28e67129fdde964e5760da66` | Original RF's pending language is an earlier epoch; later REVIEW/closing carrier supplies completed effects |
| `git branch -a --contains c51ee0c` | Returned `codex/slc-at-root` and `remotes/origin/master`. This is local Git reference evidence, not a fresh remote fetch or publication action |

All paths in this table are under `workspace/2026/TFW_20260907-020729_SLC/` unless stated otherwise. Read with `git show <full-sha>:<path>`; these files are intentionally not copied into the older TKL tree. Both SLC RES inputs were read in full: they already distinguished research support from native delivery. Their receiver-incident reproduction is inherited research evidence, not a fresh TKL rerun.

The actual accepted interface, verified by the diff to `c51ee0c`, is active `tfw.task_containers`, optional `tfw.historical_containers`, and an active-plus-historical reference union for exact reads/init detection/compilation. Ordinary discovery remains active-only; historical resume stops read-only before control repair or continuation. The knowledge workflow first routes an unfinished connected migration to the authorized updater; its normal digest/state-last algorithm remains. `tools/tfw_state.py` adds a small reference-union reader and workspace fallback, with no mandatory receiver helper.

The actual `.tfw/migrations/3.3.0.md` was read completely. It preserves before-images, exact historical membership and affected digest pairs, installs readers before narrowing, reconciles state before final config, supports equal-version re-entry and refuses divergent affected input. It explicitly rejects an atomic switch for arbitrary concurrent readers. TKL must preserve its source-pinned update obligations when retiring future digest bookkeeping; SLC is not a general permission to delete state or reclassify tasks.

Material delivered deviation: C2 corrected the reference resolver to protect complete Markdown link spans from later replacement passes after actual final output exposed malformed links. The final fixed-scope accounting is 24 VALUE files / 668 touched LOC against SLC's unchanged 24/556 plan, not the first RF's 591 LOC. TKL does not inherit these numbers as its budget. Guide/raw-evidence website publication remains outside SLC's accepted site scope; repository source paths stay valid. Current TKL link/navigation changes must consume this corrected resolver rather than the first Candidate.

### G2. Handover and replay checks do not belong to a carrier filename

The existing PTTC Closing and record recovery section and REVIEW §6 were reread. Required actual docs/knowledge effects, terminal dispositions and independent acceptance of material final changes precede DONE. N/A needs a reason; pending/deferred obligations remain open; a record-only repair does not start another capture cycle.

In either C1 or C3, a missing dispatched producer is not a “none” contribution. A justified-none return is sufficient only for its declared inspected context and existing reused sources. Unavailable context describes an actual gap; the closer assesses whether it prevents the required result and must not reconstruct it from another unit's guess. A retained uncertainty can be a completed, authorized disposition only when resolution/publication is not owed for the protected action.

Retry identity must identify the intended publication, not merely equal words. [AWS Builders' Library: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) explains explicit caller request identity and distinguishes duplicate requests from repeated parameters with a different intent. TKL inference: store the stable identity with source and intended disposition, reuse equal completed effects, and refuse same-identity divergence. This is a design analogy, not a cloud dependency. Primary article opened on 2026-09-13.

### G3. What the finite consumer can and cannot establish

One unprimed, separately addressed unit can test whether an explicit ordinary-file entry supports a small current/stale/conflicting decision with source references and authority restraint. It cannot establish a large-corpus recall rate, cross-provider reliability, automated capture, or C3 superiority over C1. Both layouts need semantic acceptance; the native exercise will test C3's risky read path while the carrier/cost comparison remains explicit analysis. The input, expected answers and cost must be fixed before dispatch, and the first sealed answer must remain visible even if it fails.

## Checkpoint

| Found | Remaining |
|---|---|
| Accepted SLC exists with exact final Candidate/review/close and corrected link behavior | Root must reconcile an execution baseline; this Researcher will not merge that dependency into product sources |
| C1 and C3 share all material handover and semantic obligations | Concrete counterexamples and complete function-retention comparison |
| Stable retry identity has a narrow purpose | Independent current/stale consumer observation after payload/oracle seal |

OBSERVE: current worktree plus selected wider Git lineage, actual SLC sources, common closer and primary retry guidance. ORIENT: carrier independence is not truth or freshness. DECIDE: compare two real alternatives and test C3's missing evidence. ACT: prepare Extract with finite exercise inputs and held-out oracle.

External source used: YES. Briefing gap closed for current dependency and factors: YES. Below-three-dimension matrix used: YES. Stage complete: YES.
