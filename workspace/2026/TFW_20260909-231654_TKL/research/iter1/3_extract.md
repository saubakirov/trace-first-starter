# Extract — What do we NOT see?

> **Mindset:** Analyst; compare complete configurations and expose displaced work.
> Parent: [TKL HL](../../HL-TFW_20260909-231654_TKL.md)
> Goal: usable, qualified knowledge with preserved sources and proportionate handover.
> Date: 2026-09-13 · Writer: robert · Role: Researcher · Mode: focused
> Inputs: [Briefing](1_briefing.md), [Gather](2_gather.md), selected current templates and PV Index at `3f4e59418c521dd22908662028351258288b89fb`.

## Configuration Space

The full space is represented in factored form: `D1 × D2 × D3 × D4 × D5 × D6 × D7 × D8`, each with Gather's A/B/C alternatives, or `3^8 = 6,561` tuples before consistency checks. The following representative complete configurations expose material architectural choices; they are not a claim to have individually evaluated every tuple. Each row differs on at least one axis. Shared safeguards and function accounting below complete the carrier choices.

| Config | D1 Capture timing | D2 Source ownership | D3 Qualification carrier | D4 Publication scheduling | D5 Retrieval | D6 Correction and conflict | D7 Integration | D8 Migration |
|---|---|---|---|---|---|---|---|---|
| C1 Existing sections and curated topics | B handovers | A role artifacts | A topic tables | B material disposition at close | A central map | A current record/source history | A existing closer | A compatible legacy inputs |
| C2 Task summary and curated topics | B handovers | B Coordinator task file | A topic tables | A qualify all before close | A central map | A current record/source history | A existing closer | B bounded conversion |
| C3 Existing sources and project records | B handovers | A role artifacts | B separate records | B material disposition at close | B entry/search/relations | B explicit replacement | A existing closer | A compatible legacy inputs |
| C4 Separate contributor sources and project records | B handovers | C contributor files | B separate records | B material disposition at close | C optional view/fallback | B explicit replacement | A existing closer | B bounded conversion |
| C5 Qualified task-local sources | B handovers | C contributor files | C task-local qualification refs | B material disposition at close | C optional view/fallback | B explicit replacement | A existing closer | A compatible legacy inputs |
| C6 Continuous capture with scheduled publication | C continuous | C contributor files | B separate records | C curator batch | C optional view/fallback | B explicit replacement | A existing closer | A compatible legacy inputs |

Unlisted variants include final-close-only capture, unresolved-only retention, a separate closing worker, and wholesale reset. They remain visible in the factored space; Challenge checks their conflicts with the frozen requirements. D6-C is also a necessary fallback for an unresolved real contradiction in any design, not permission to omit a correction route. Optional indexing is an overlay on C3 as well as C4; no design may require it.

## Findings

### E1. The smallest complete handover reuses role artifacts but covers context loss

The common contract under comparison is: at a producing-role transfer or material checkpoint, preserve the available material claim, its grounds, uncertainty, scope and actual producer; return the exact source address. A final RF/RES/REVIEW section is sufficient when it exists before the handover. A role that stops before its final artifact needs a small owned checkpoint in its existing task/stage trace. One extra file is justified only when no existing permitted carrier can safely receive that contribution. This conditional combination is not the all-new-file C4 or the one-task-summary C2.

The closer obtains the contributing-unit set from the selected task's actual dispatches/handoffs and available direct context, then checks the returned sources. No separate maintained contributor inventory is necessary. Unknown participation is an honest limit; the closer cannot verify unseen chats or prevent all unrecorded work. Required source absence is distinct from an examined “no material new knowledge” statement. Repeating an earlier source uses a reference, not a duplicate summary.

Concrete outcomes before close:

| Outcome | What must be inspectable | Consequence |
|---|---|---|
| Material contribution captured | Claim, source, producing unit and scope; classification/disposition | Qualify current reusable claims, or record why preservation without endorsement is the complete disposition |
| No new material contribution | Scope/context examined and why prior sources suffice or nothing relevant arose | Legitimate absence; no filler fact/file quota |
| Available context incomplete | Missing participant/range and its effect on the accepted result | Material missing handover blocks this close; route to its existing owner, never relabel as N/A |
| Observation retained but not accepted | Source, uncertainty and reason it is not current project knowledge | No fabricated promotion; no promise of a background worker |
| Contradictory material | Both claims, shared applicability and authorized resolver | Block the affected decision/close if its truth is necessary; unrelated work proceeds |

Rejected/stopped work retains available knowledge at its actual stop/handover; it does not receive a fake RF, successful DONE or invented retrospective account. A crash before any checkpoint can still lose material; the observable protection is a missing return at the next controlled transfer/close, not losslessness.

### E2. Qualification needs an accountable decision, not a popularity count

C1/C2 retain the current Coordinator-owned knowledge operation and topics. They can remove a global gate and source markers, but publication continues to edit shared topic rows. C3/C4 keep the same authorized operation while changing its output shape. C5 stores both source and later qualification near tasks, requiring a cross-task current-claim discovery mechanism. C6 separates capture availability from publication, but needs a concrete finite scheduling owner; “a curator eventually runs” is not a completion mechanism.

Candidate semantics should distinguish a human preference/decision, externally verifiable claim, observation, technical reference and governing instruction. Human statements have authority only within their actual owner/mandate scope; technical claims need their applicable source/evidence route. Preserve current docs-versus-knowledge purposes even if a common record form is used. A provenance trail does not make a claim true: [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) models derivation and responsible agents so readers can assess provenance. TFW's acceptance authority is supplied by its own contracts, not by adopting an ontology.

For C3/C4, a project record contains one independently qualified claim or coherent decision: an independently allocated identity, plain title/searchable scope, statement and rationale, source addresses and versions, producer, qualifier/authority, applicability and uncertainty, plus explicit relations to replaced/duplicate/contradictory records. This is a proposed semantic minimum, not an approved schema. Confidence, source independence and authorized acceptance must not collapse into a green icon. No new globally sequential F/D counter is allocated; existing F/D references remain valid.

Qualification occurs during a bounded invocation already owned by the relevant Coordinator: at handover if another task needs the claim now, and before close for that task's required final effects. All material contributions receive a completed disposition. “Retain as uncertain evidence” may be a final, grounded decision; “publish later, owner unspecified” is an unresolved obligation and cannot pass the current PTTC close. This avoids using the word “deferred” to quietly change PTTC's rule. A real open obligation uses its existing authority route and blocks only its protected action.

### E3. Source identity, semantic conflict and replay need separate treatment

C3/C4 allocate a durable record identity from the producing task/unit and its preserved local claim key, before the first publication attempt. A retry reuses that identity and re-reads actual output. Same identity/equal semantic content means already applied; same identity/divergent content means stop and reconcile. Two independent sources may express the same claim under different identities: retain provenance and qualify a duplicate/equivalence relation rather than deleting one or blind-incrementing totals. A content hash can detect identical bytes, but cannot decide semantic equivalence or permission.

Before promotion and before consuming a claim, inspect relevant project records, their applicability and all references to their identities, including later supersession or conflict relations. A later correction names its predecessor from a new record so sealed task sources require no marker edit. “Newest timestamp wins” is rejected as authority. Concurrent corrections to one predecessor remain competing branches until an authorized resolution names both. Independent task writes can therefore survive while their incompatibility remains visible.

This offers bounded file-based convergence only over an explicitly observed integrated revision. It cannot certify absence of unseen sibling branches. The existing landing owner must refresh changed overlapping knowledge claims after integration; affected independent acceptance follows PTTC. Distinct filenames remove shared inventory contention, not semantic reconciliation. Same-task shared source ownership is similarly separate: C2's single writer prevents direct append collision but becomes a bottleneck and cannot reconstruct an absent contributor.

On interruption, source capture survives independently. A finished qualification record with a missing closing reference is recoverable by matching its preserved identity/source and acceptance; add only the missing current control. A half-written or divergent record is not accepted. If actual effects or authority changed, use the existing affected review/correction route. No periodic queue, global processed count or source mutation is required.

### E4. Account for every current central function before removing a carrier

This table is the C3/C4 replacement contract to test, not an authorized rewrite. C1/C2 retain the first five current carriers and remove only the gate/state/marker burden; C5 must supply equivalent retrieval without scanning sealed tasks.

| Current function | Proposed home or explicit retirement | Owner / burden removed |
|---|---|---|
| KNOWLEDGE §1 component map | Keep a concise current reference map at a stable documented entry; preserve its old address during migration | Docs owner updates real architecture changes; no per-fact inventory obligation |
| §1 Architecture Decisions: choice, rationale, source | Separate current decision records plus read-compatible historical D rows | Existing decision/qualification owner; removes shared sequential D-row appends |
| §2 Key Artifacts: important trace entry points | Direct source links from applicable decisions and current reference map; existing useful historical links remain readable | Docs owner maintains genuinely useful navigation, not an inventory of every task |
| §3 Legacy & Deprecation | Current replacement/deprecation statements live with their decision and point to old source; preserve historical rows | No rewrite of sealed rationale or hidden removal of its replacement route |
| §4 topic navigation and counts | Stable instructions identify record locations and ordinary-file search; legacy topic paths remain usable | Retire maintained counts and per-topic inventory; optional views have no freshness duty |
| `knowledge/*.md`: accepted human-sourced meaning, confidence, source, date | Preserve existing topic files/anchors as legacy accepted inputs; promote new qualified records, and relate corrections to exact old facts | Knowledge owner; no bulk recertification or silent confidence upgrade |
| `.tfw/knowledge_state.yaml`: change detection / processed coverage | Replace future need with exact selected-task handover/effect references and stable publication identity | Remove task-digest portfolio and no-section task churn; a source's processing is not inferred from task age |
| State audit date/statistics | Preserve old state under compatible migration evidence; dates on actual decisions/effects remain | Retire live totals as unnecessary bookkeeping; no fabricated “all processed” reset |
| Source `fact-candidates: processed` markers | Later record cites original source, source version and disposition | Removes post-close source edits and post-marker rehash cycle |
| PV P2/P3 and P5–P7 read obligations | Explicit semantic read route to applicable current principles/decisions and relevant domain records, with legacy fallback | Preserve required governing context and independently checked HL citations; no reliance on similarity rank |
| Compiled link resolution and public/documentation references | Compatibility entry/anchors and source links remain until an accepted migration proves replacements | Existing docs/update owners; no “file deleted, links probably recoverable” assumption |
| New-project bootstrap | Clean templates containing method guidance only | Existing init/update owner; never ship this project's accepted memory or old state |

Removing KNOWLEDGE.md as a monolithic qualification/inventory surface is separable from deleting its pathname. A small stable reference entry may remain without a per-record catalogue. Changing the current PV routes, reference compiler or documentation map is real implementation scope; it must be explicitly costed, not hidden as cleanup.

### E5. Migration can preserve meaning without replaying the whole historical backlog

Proposed migration sequence: consume accepted SLC result and source-pinned update guide; classify existing knowledge/reference/state by function and owner; preserve exact before-images and links; install new readers and clean templates; enable new writes only after old accepted meaning is reachable; retire obsolete active bookkeeping with an explicit disposition. Do not label unprocessed historical inputs processed. Keep legacy topic facts and central D rows as directly readable sources until a specific current change requires a new qualified record.

For each prescribed write, re-read the affected current value against preserved old/intended values. Old means apply authorized change; intended means already applied; divergent means stop and preserve later work. This is a proposed application of the existing update preservation/receipt route, pending SLC's actual accepted migration mechanics. No second migration engine or lifecycle is proposed. A partial conversion must remain honest and resumable without demanding a history-wide scan. Fresh projects use clean templates; this upstream repository's memory must never be their payload.

## Checkpoint

| Found | Remaining |
|---|---|
| Six complete carrier/scheduling configurations, plus full factored design space | Pairwise incompatibilities and scenario survival |
| Conditional reuse of existing sources avoids mandatory all-new files | Whether fallback checkpoints give sufficient observable handover |
| Every central function has a retained/replaced/retired job | Fresh-consumer discoverability and stale-match behavior |
| Retry identity and semantic acceptance are separate | Independent concurrent and interrupted trials |

OBSERVE: map/template/PV functions and external provenance model. ORIENT: qualify meaning without moving authority into a file count. DECIDE: carry C1–C6 and explicit common obligations to Challenge. ACT: test failure cases and narrow the recommendation.

**Sufficiency:** External source used: YES, W3C PROV-DM accessed 2026-09-13. Briefing gap closed for complete designs: YES. Configuration space built from Gather dimensions: YES, factored with representative complete rows; exhaustive tuple testing is not claimed.

Stage complete: YES
→ Advance under the recorded autonomous dispatch; no architecture decision taken.
