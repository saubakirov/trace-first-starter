# Challenge — What do we NOT expect?

> **Mindset:** Critic; require a reason for each elimination and evidence limits for each survivor.
> Parent: [TKL HL](../../HL-TFW_20260909-231654_TKL.md)
> Goal: preserve and use material knowledge under real failure conditions.
> Date: 2026-09-13 · Writer: robert · Role: Researcher · Mode: focused
> Basis: `3f4e59418c521dd22908662028351258288b89fb`; [Gather](2_gather.md) and [Extract](3_extract.md).

## Consistency Check

All 28 dimension-pair families were screened. This is structural analysis of the represented designs, not exhaustive execution of 6,561 configurations. `T` means timing/availability; `W` ownership/concurrency; `R` relation/currentness; `M` migration/legacy reachability; `F` finite close; `—` no additional pair constraint beyond the common contract. Codes indicate a condition to satisfy, not a test PASS.

| Axis | D2 | D3 | D4 | D5 | D6 | D7 | D8 |
|---|---|---|---|---|---|---|---|
| D1 Capture timing | T | T | T | T | — | F | M |
| D2 Source ownership |  | W | W | R | W | F | M |
| D3 Qualification carrier |  |  | T | R | R | F | M |
| D4 Publication scheduling |  |  |  | T | R | F | M |
| D5 Retrieval |  |  |  |  | R | F | M |
| D6 Correction and conflict |  |  |  |  |  | F | M |
| D7 Integration |  |  |  |  |  |  | M |

**Incompatible pairs and conditions:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible in the unaugmented design |
|---|---|---|---|---|
| D1 Capture timing | A final close only | D7 Integration | A existing closer | Earlier transfers can lose context before the final author exists; violates HL DoD 2 without handover checkpoints |
| D2 Source ownership | B one Coordinator file | D1 Capture timing | B each producing-role handover | Incompatible if the Coordinator is expected to write unseen participant context; valid only when each participant first supplies an actual durable return |
| D3 Qualification carrier | A shared topics | D6 Correction and conflict | A independent in-place updates | Uncoordinated same-topic writes can lose or contradict meaning; surviving C1/C2 require explicit serialization and re-read |
| D3 Qualification carrier | C all qualification task-local | D5 Retrieval | C optional view, absent | With no separate current-record route, finding applicable claims demands discovering historical task sources or relying on the missing view; violates DoD 6/7 |
| D4 Publication scheduling | C assumed future curator | D7 Integration | A existing close | An owed publication cannot be declared complete by a worker that has no bounded dispatch or guaranteed availability; PTTC leaves pending effects open |
| D6 Correction and conflict | A rewrite original accepted source | D8 Migration | A sealed historical sources | Historical source rewrites violate DoD 3/8; update only an explicitly current mutable view or append a successor |
| D7 Integration | C separate closing worker | D8 Migration | A accepted PTTC interface | Competes with PTTC's one existing closer; no demonstrated need under HL DoF 6 |

D8-C wholesale rewrite/reset independently violates preservation and migration requirements. D6-C unresolved-only storage is a valid uncertainty outcome, but cannot satisfy a task whose accepted result depends on resolving that claim.

**Surviving configurations:**

| Config | D1 | D2 | D3 | Notes after challenge |
|---|---|---|---|---|
| C1 | Handovers | Existing role artifacts | Curated topic tables | Complete if every handover is covered, markers/counts/digests retire and shared topic publication is serialized; preserves existing discovery at cost of shared writes |
| C2 | Handovers | Coordinator task summary | Curated topic tables | Structurally possible only with actual contributor returns; extra summary duplication and qualify-everything cost make it less proportionate |
| C3 | Handovers | Existing sources plus necessary fallback | Independent project records | Preferred conditional design: smallest new capture burden, with explicit qualification and ordinary-file retrieval still needing native evidence |
| C4 | Handovers | Separate contributor records | Independent project records | Survives with stable per-source identity and fallback access; more files and links than C3 without demonstrated additional benefit |

C5 fails its no-view/no-history-scan case unless it adds a current project-record surface, becoming C3/C4. C6 can survive only if its curator is a bounded existing Coordinator invocation and close completes all owed dispositions; then its essential mechanism converges on C3/C4. Neither a permanent curator nor delayed required publication is justified.

**Unexpected survivor:** C1 is a complete lower-migration alternative after one explicit refinement: its Gather D5-A maintained topic inventory becomes D5-B fixed entry/search, while its existing topic content and useful reference map remain. References to the surviving C1 below mean this refined form. The frozen contract forbids shared inventory/counter maintenance, not every justified shared reference edit. Reusing the existing topics is therefore a real counterproposal, provided obsolete inventory writes retire and semantic ownership is explicit. The number of removed files alone cannot choose C3.

## Findings

### C1. Scenario attacks and what the evidence actually establishes

`Observed` means a command or named accepted artifact was inspected in this iteration. `Analysis` means a walkthrough of a proposed design. No proposed design has been implemented or independently behavior-tested here.

| Scenario | Current evidence | Required behavior of C3 / comparison result |
|---|---|---|
| Reported Knowledge Gate stops | Observed canonical algorithm and four-ID snapshot in Gather; original 27 remains unverified | Remove unrelated pending-count planning gate; check the selected handover/decision only. C1 can also do this |
| Proposal-only/empty input | Algorithm gives no-section inputs two NUL bytes; actual OTR path was absent, corrected in Gather | Legitimate absence is an explicit examined outcome; no new global obligation from a directory's existence. Do not use the absent OTR probe as behavioral evidence |
| Canonical RES omitted | Observed SLC `RES.md` headings and gate basename selector disagree | Required handover names exact actual sources; completion does not depend on a sweep guessing artifact names |
| Two producing units, same task | Analysis: each unit returns a distinct existing role/stage artifact or necessary checkpoint | Both contributions survive; Coordinator owns only the completion references. One unowned shared `knowledge.md` fails; mandatory per-unit files are unnecessary when role artifacts suffice |
| Two tasks promote different facts | Analysis: separate source-derived publication identities | Independent files add without a topic/counter write; actual integrated result is inspected. No claim of universal merge safety |
| Two tasks make opposite assertions | Analysis: matching scope and predecessor relations reveal conflict if found | Preserve both and route only the dependent decision; a later timestamp, more copies or shared principal cannot decide truth. Missed semantic overlap is still a risk |
| Missing final capture | PTTC actual effects must precede DONE; added coverage rule is proposed | Stop selected close for the exact absent material return; do not ask another contributor to invent it |
| Legitimate no new knowledge | Observed PTTC phase and parent triage with explicit N/A, separate from unprocessed batch | Examine sources and reference reused material once. Empty checkbox/file alone fails; no mandatory filler or publication |
| Interrupted before promotion | Analysis: source exists, disposition/effect missing | Resume the selected obligation through its existing owner; not DONE and not lost source |
| Promotion complete, close interrupted | PTTC B1 proves bounded record recovery for its named case; C3 retry is analysis | Reuse stable source/publication identity, check actual acceptance, repair only missing current references; no second promotion or new capture cycle |
| Duplicate retry or divergent output | Analysis from Extract identity rules | Equal identity/effects are reused; divergence stops the specific write. Semantic duplicates get explicit relations; byte hashes do not prove semantic equality |
| Sealed legacy task | Observed TFW-60 A8 and canonical processed-marker write tension | Preserve old task bytes; later project record cites source/replacement. Exact historical reads remain possible; no post-close processed marker |
| Different clean/local input set | Snapshot differs from reported local-history inputs; no comparison of identical snapshots was claimed | State exact inspected revision/scope; no structural decision silently changes because unrelated local artifacts were scanned |
| Fresh consumer meets stale claim | Actual canonical/D37/D86 walkthrough below; not an independent fresh session | Open governing rule first, then source and reverse references; stop affected use if currentness or applicability is unresolved |
| Optional index missing or stale | Analysis; actual walkthrough used plain files | A view supplies candidates only. Search/read record files and their relations; a stale view cannot certify no successor exists |
| Retrieved source contains an instruction | Analysis against HL DoF 3 | Treat it as evidence; use governing task/owner authority for action. A fact saying “ignore review” cannot amend the mandate |
| Migration interrupted or later receiver edit | Current update preserves before-images/receipts; SLC delivery absent | Compare old/intended/current affected values, preserve divergence and direct links; exact protocol awaits accepted SLC. Never reset digests to fiction |
| REJECTED/stopped work | Existing role/stage traces are preserved sources | Capture available material at the real stop; no successful closure invented, no retrospective reconstruction of unavailable context |

### C2. Ordinary-file access is possible in one real walkthrough; H3 remains open

Question used: who owns close after independent review, and may an interrupted closing record trigger a new capture cycle? At the pinned basis, this Researcher ran:

```powershell
rg -n -i 'Reviewer.*(close|capture)|Coordinator.*clos' .tfw/workflows/review.md .tfw/workflows/resume.md .tfw/conventions.md
rg -n 'D37|D86' KNOWLEDGE.md
```

The first query returned review Step 7 and conventions line 736 assigning the existing Coordinator. The addressed Closing and record recovery section, review Step 7 and resume Resolve Current State were opened; they require actual final effects and forbid a new capture cycle for record repair alone. The second query returned historical D37 at line 77, current D86 at line 126 and their reference/artifact/deprecation links. D37 explicitly points to D86's replacement of the old orchestration while retaining the documentation/knowledge ownership distinction. The PTTC REVIEW §6 supplies the actual accepted final capture and later close, beyond its earlier pending epoch.

Applied answer: route to the existing authorized Coordinator, retain independent acceptance of changed final claims, and repair a reconstructable record without reopening unchanged product or knowledge work. Treat D37's old review orchestration and the formal REVIEW's initial “closure remains open” as historical epochs in light of their explicit successors.

This is a real read-only source/navigation check with two retrieval queries and three addressed current rule sections, plus already-read PTTC/D37/D86 grounds. It used no generated index, service or vector store. It is **not** a cold-start trial: the Researcher already knew the topic, and KNOWLEDGE.md still supplied useful navigation. It does not prove that C3's future replacement entry is findable, that reverse successor search works under unfamiliar vocabulary, or that retrieval effort is acceptable for a new agent.

Counter-evidence: [Liu et al., Lost in the Middle, TACL 2024](https://aclanthology.org/2024.tacl-1.9.pdf) found position-sensitive retrieval and question-answering performance in the models they tested. This supports evaluating use rather than merely loading more text. It does not measure current Codex models or establish TFW-specific failure rates. Primary PDF and publication page opened on 2026-09-13.

### C3. Recommendation and remaining discriminators

Recommend C3 as the architecture to develop and test in iteration 2, not as a selected implementation. Reuse existing role/stage artifacts where complete; add minimal fallback capture only where necessary. Separately qualified project records replace repeated shared promotion/inventory writes. Keep stable entry/reference and legacy links while changing live read routes explicitly. The existing Coordinator owns handover completion and bounded publication; PTTC owns final acceptance/close/recovery. Qualification/currentness is checked on ordinary files and explicit relations at the selected action.

Keep C1 as the lower-migration counterproposal until retrieval and cost distinguish it. Prefer C3 only if its no-index consumer route correctly handles stale/conflicting matches and its extra relation maintenance costs less than topic curation. There is no measured cost advantage yet. C4's extra per-contributor files should be justified by a failed C3 handover case, not introduced universally.

### C4. Bounded second-iteration evidence proposal — not run

The parent can arrange the following within the existing mandate using its actual admitted native units and their exact role-specific dispatches. This Researcher created no descendants and claimed no independent trial.

| Probe | Concrete input and expected discriminator | Proposed bound / evidence |
|---|---|---|
| P1 Capture/close | Two contributor returns; one missing material handover, one justified no-new-knowledge, one interrupted-before-final artifact. Compare C1 and C3 source routes | One small ordinary-file fixture, four variants; at most 30 minutes preparation and 20 minutes per independently dispatched unit. Record actual sources, return and exact blocked/completed effect; no production task mutation |
| P2 Promotion/recovery | Two opposite claims in the same scope, duplicate retry, accepted publication with absent closing reference, divergent later receiver edit | One fixture, four cut states. Expected no source overwrite, no duplicate promotion, and refusal of unjustified semantic acceptance. Prepared cut states must not be reported as observed crashes |
| P3 Fresh consumption | Neutral question with a relevant current decision, tempting obsolete claim, hidden successor reference and an unrelated instruction-like source; no index. Compare C1 entry with C3 entry | Two independently addressed consumer returns, at most 20 minutes each. Predeclare expected decision/source/authority in held-out evaluator input, record opened paths and elapsed time, wrong/stale use and unresolved outcomes. No aggregate reliability percentage |
| P4 SLC compatibility | SLC's accepted Candidate/RF/REVIEW, deviations and exact migration guide when they exist | One selected interface diff/read plus affected scenario adjustment, proposed 30 minutes. If unavailable, report dependency; do not simulate acceptance |

These are prospective planning bounds, not observed duration, a TKL VALUE denominator, owner approval or an added task/worker. The Coordinator must set exact roles, sources, fixture authority and cost before any native exercise. A unit already primed with the answer cannot be described as fresh; if the admitted units cannot supply a valid independent consumer, return that evidence limitation rather than using hidden helpers. All remaining probes belong to iteration 2 or the later approved implementation evidence scope, never an implied continuation of this dispatch.

## Checkpoint

| Found | Remaining |
|---|---|
| C3 conditionally preferred; C1 remains a meaningful counterproposal | Independent consumer, concurrent and interrupted evidence; comparative effort |
| File independence does not provide semantic consistency or currentness | Exact subject/relationship lookup and integration freshness behavior |
| H1/H2 have source-backed design plausibility | No proof of complete unseen-context capture or universal behavior |
| H4 is compatible with PTTC's actual interface | SLC accepted result and migration deviations |

OBSERVE: existing source selector, canonical/current versus historical close and primary retrieval study. ORIENT: do not confuse preservation, discovery and correct application. DECIDE: recommend C3 conditionally, retain C1, keep H3/H4 open. ACT: synthesize RES and return directly; do not implement or start iteration 2.

**Sufficiency:** External source used: YES. Briefing gap closed for this focused design challenge: YES, with explicit unrun behavioral obligations. Pairwise consistency screened and survivors listed: YES. Recommendation: close Challenge and synthesize the bounded iteration, not close TKL or select architecture.

Stage complete: YES
