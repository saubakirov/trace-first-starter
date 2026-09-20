# Gather — "What do we NOT know?"
> **Mindset:** Explorer. Map unknown territory; treat every explanation as a question until a source and epoch support it.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260920-223357_FRATS](../../HL-TFW_20260920-223357_FRATS.md)
> Goal: Refactor TFW from field evidence so its artifacts remain behaviorally complete while routine coordination moves from repeated dialogue to concise durable traces.
> Observation boundary: local files and Git state inspected read-only on 2026-09-20 (`Asia/Qyzylorda`); receiver state is reported per snapshot, not treated as stable across the stage.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: receiver state at observation | clean after committed update | clean but installed release is behind | dirty only in project/task-owned paths | concurrent uncommitted framework update |
| D2: receipt-to-current relation | receipt claim corroborated now | receipt condition resolved later | receipt condition still visible | newer/current state lacks a settled committed receipt |
| D3: measurement continuity | exact historical replay | historical replay plus explicit current bridge | successor measure with no equality claim | comparison unavailable because source/selector is missing |
| D4: runtime context charge | whole file | addressed heading/range | dynamic task-local input recorded but not fixed-charged | deliberate repeated read |
| D5: rule/delivery relationship | sole canonical owner | exact installed copy | managed block projection | foreign/customized content preserved outside framework ownership |
| D6: artifact filename state | current single-phase `TYPE__{ID}` | current phase `TYPE__phase-*` | current `__revN` sibling or cumulative append | historical non-current grammar retained for readability |
| D7: rule-compliance cause | checkpoint placement/timing | conflicting or incompletely loaded instructions | native capability/readback limit | raw instruction length/attention pressure |
| D8: principal-resolution context | human owner session | selected-LEAD root session | shared device or several human principals | non-AT operational session with no named agent principal |

## Findings

### G1: Receiver state is epoch-sensitive and receipts are not current-state registries

The first Git snapshot preceded RYC receipt `UPDATE__20260920-231630__93b9` (`recorded_at` 23:16:30
+05:00). A second RYC snapshot was taken at 23:18:09 +05:00 after that receipt appeared.

| Receiver | First observed Git state | Installed/config state read | Latest receipt read at that point | Current interpretation |
|---|---|---|---|---|
| Steps Framework | `0178fc9`, `master`, three untracked entries: two unrelated owner/task paths plus this `research/iter1/` | 3.4.1 | self/upstream | Research writes are isolated to the approved iteration directory; unrelated untracked paths were not touched. |
| Helpdesk | `f53ed5d`, `beta`, clean | 3.4.1; active `[workspace]`, historical `[tasks]` | `UPDATE__20260920-215723__5a96` | The receipt's 32 uncommitted update paths describe its sealing epoch, not the current tree: the present receiver is clean. The receipt still preserves real update-process evidence, including concurrent HEAD movement, exact-path exclusion repair, project-owned stale Resume mentions, a retained singular file and non-implicated red checks. |
| SenseLab / KazNPU AI Lab | `443eece`, `master`, 27 dirty paths, all observed under sticker design/daily assets rather than `.tfw` | 3.1.0; `[workspace, tasks]`; echo lint/test placeholders | `UPDATE__20260908-182421__9557` | The receiver is behind 3.4.1. Its receipt proves placeholder checks verified nothing and that a prior adapter pass had missed stale Antigravity copies, but the present 27-path dirt is a separate project-content observation. |
| AFD | `c615a907`, `beta`, three dirty task paths (`AFD-51` modified; `AFD-46` HL/research untracked) | 3.3.0; active `[workspace]`, historical `[tasks]`; real Gradle checks | `UPDATE__20260914-050848__9c2b` | The receipt-era task dirt remains visible by path. The receipt's six failing tests, lint finding and retained project-owned singular workflow remain historical claims until separately rerun; this stage does not relabel them as current. |
| RYC | First snapshot: `c5b49a9`, `master`, one untracked `.tfw/.upstream-source/`; second snapshot: same HEAD with 52 uncommitted paths (46 `.tfw`, five adapter paths, one `KNOWLEDGE.md`) | Worktree config became 3.4.1; active `[tasks]`; echo lint/test placeholders | Initially only `UPDATE__20260910-154500__3a2f` (3.2.0); during Gather, `UPDATE__20260920-231630__93b9` (3.4.1) appeared | The receiver changed during inspection. The new receipt records a completed 3.4.1 application, but the second snapshot shows the result still uncommitted. Both epochs are retained; they must not be merged into a claim of a stable clean receiver. |

Sources: each receiver's `.tfw/project_config.yaml` (RYC's tracked spelling is
`.tfw/PROJECT_CONFIG.yaml`), the named receipts, and direct `git rev-parse`, branch and
`status --short` observations. No receiver file was changed by this Researcher.

### G2: The receiver histories already separate at least four failure/limit classes

1. **Concurrent-tree risk:** Helpdesk's receipt records HEAD moving during the update while the
   measured path overlap stayed empty; RYC visibly changed during this Gather stage.
2. **Ownership/customization boundary:** Helpdesk retained project-owned unmarked Resume mentions
   and an unowned singular file; AFD retained a project-owned singular workflow; KazNPU preserved a
   customized historical README through an attachment.
3. **Verification quality:** KazNPU and RYC configured echo commands that executed but proved
   nothing; Helpdesk reported real lint/test failures outside the update payload; AFD configured
   substantive Gradle checks but its receipt deferred existing failures.
4. **Payload/application mechanics:** Helpdesk's first comparison accidentally used a basename
   exclusion that masked a second `project_config.yaml`, then corrected it with exact-path
   exclusions. KazNPU's receipt records that the prior 3.0.0 pass missed one installed adapter.

These are dimensions, not yet a universal cause. In particular, payload copying itself cannot be
excluded merely because ownership, concurrency and verification problems are also present.

### G3: RCFR's accepted numbers are recoverable, but the live executable denominator is gone

RCFR Phase C's final RF and evidence record:

- canonical trajectory `310,485 → 112,206` words (`63.9%` lower);
- unique active `.tfw` corpus `66,436 → 32,088` words (`51.7%` lower);
- command: `python -X utf8 docs/scripts/test_runtime_context.py --audit`;
- baseline/candidate graph measurement charged full files, named ranges and deliberate rereads,
  while dynamic task-local inputs remained visible but uncharged as fixed payload.

The historical script's `active_runtime_corpus_words` selected every charged `.tfw/` source/range
reachable from `RUNTIME_VARIANTS`, counted a whole file once when `*` was required, and otherwise
removed addressed ranges contained inside larger selected ranges. That is more specific than a
filesystem-wide word count.

The audit script was deleted in commit `c10169b` on 2026-09-14 (`6,885` deleted lines, “Simplify
docs build and remove costly test oracles”). Its source remains recoverable from Git, but the current
3.4.1 surface has ten commands rather than RCFR's eleven because Resume was retired, and the
knowledge lifecycle/read contracts have since changed. Exact historical replay and current
measurement therefore require two outputs: reproduce the immutable RCFR result at its accepted
candidate, then define and justify the current bridge. Running a convenient whole-tree count would
not be the same denominator.

One trace inconsistency also needs extraction: current `KNOWLEDGE.md` D75 says trajectory
`310,485 → 112,536` (`63.8%`) while its cited final RF/evidence say `112,206` (`63.9%`); the same row
agrees on `32,088`. No incoming successor/correction reference to D75 was found in `knowledge/`.

### G4: Canonical ownership and delivery are distinct dimensions

Current `.tfw/adapters/manifest.yaml` names ten commands and four adapter families. Codex commands
copy command-specific skills whose job is dispatch; Claude Code, Cursor and Antigravity copy the
canonical workflows directly. Persistent instructions use either a managed block or an exact copy.
Consequently, “duplicate text” can mean an intentional installed projection, a managed root block,
an obsolete stale copy, or an unowned project file. A useful census must classify the relationship
before calling it removable.

The historical RCFR audit made the same distinction for runtime reads: source, heading, purpose,
repeat, ownership, dynamic status and charged status were separate fields. Extract must preserve
those axes instead of reducing the problem to identical bytes or raw word totals.

### G5: Current filename issuance is normative, but the producer form remains incomplete

The current `Artifact file naming` section admits `TS__{ID}.md` and `RF__{ID}.md` for new
single-phase artifacts, parallel phase forms, and `__revN` only for TS/REVIEW repair siblings.
Repository files show current double-underscore examples, while the only observed whole-ID
hyphenated pair is the historical CRUE lineage (`TS-TFW_20260906-190312_CRUE.md` and
`RF-TFW_20260906-190312_CRUE.md`). Current workflow searches found no rule authorizing new
`TS-{ID}` or `RF-{ID}` issuance.

However, the generic TS/RF templates do not state their output filename and their headings assume a
`/ Phase {X}` form even when the same templates are used for single-phase tasks. Plan routes readers
to the naming section, while Handoff gives one explicit TS revision filename. This supports H10's
“incomplete issuance contract plus historical precedent” as a live question, but consumer behavior
still needs mapping before the hypothesis can be confirmed.

### G6: H11 must be narrower than “multiple profiles should not ask”

The repository declares `saubakirov` as a human principal and `robert` as an agent principal. The
machine binding file has no Steps Framework entry. Under the current unconditional rule, several
profiles plus no binding correctly causes one question in each separate session; both the
Coordinator and this Researcher followed that rule. The prompt also protects real cases such as a
shared device and several human principals.

The observed gap is conditional attribution, not Researcher inconsistency: one project-root binding
cannot distinguish an owner-launched non-AT operational session from a future selected-LEAD root
session on the same repository. Optional `writer`, required accountable human, actual `via`,
workflow role, gate recipient, profile attribution, LEAD selection and mandate are separate facts.
Extract must test whether principal resolution can be conditional without weakening the existing
multiple-human/shared-device safety case, including a same-root owner/LEAD counterexample.

### G7: Session compliance evidence is bounded in iteration 1

This Codex surface accepted the exact title `RESEARCH · FRATS` through native title mutation and
returned the same text. That proves one successful local capability instance, not general Codex
reliability and nothing about Claude. The first identity question arose after the title checkpoint,
so the observed H11 case concerns attribution selection, not title capability. Live provider/AT
trials and final interaction architecture remain reserved for iteration 2.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Five receiver snapshots and their receipt/current distinctions are source-bound; RYC explicitly carries two observation epochs. | Extract a normalized receiver chronology and distinguish current, historical, unresolved and concurrently changing claims. |
| RCFR's accepted method and final values are recoverable from immutable artifacts and Git history. | Reproduce the historical result, resolve the D75 `112,536` discrepancy, and define a ten-command current bridge without claiming equality. |
| Canonical ownership, installed projection, managed block and foreign/customized content are separate alternatives. | Build the current rule/reader/copy matrix and identify actual contradictions, staleness and readerless bounds. |
| Current filename rules admit one new single-phase grammar; historical CRUE uses another readable form. | Map every producer, consumer and revision route to determine whether incomplete templates can still cause new issuance ambiguity. |
| The identity prompt has a valid safety purpose; the same-root owner/LEAD distinction is not represented by a project-root binding. | Test conditional resolution against multiple-human, shared-device, owner-launched operational and selected-LEAD cases. |
| One exact Codex title operation succeeded. | Do not generalize; iteration 2 owns native provider/AT challenge. |

**Sufficiency:**
- [x] External source used? — receiver trees, sealed receipts, current Git state and immutable RCFR Git history.
- [x] Briefing gap closed? — the evidence dimensions and alternatives needed for Extract are explicit.
- [x] Dimensions identified? — eight independent factors with at least three alternatives each.

Stage complete: YES
→ User decision: pending Coordinator gate
