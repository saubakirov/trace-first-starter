# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. Evidence from Verify → rule on quality. Every ✅ has proof; every ❌ has a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | `verify.md` F1–F15. AC-1, AC-8 and AC-9 substantially hold. AC-2, AC-3, AC-4, AC-5, AC-6, AC-7 and AC-10 do not: collision guarantees fail, identity is not integrated, state validation is incomplete, migration is not clean-checkout complete, docs consumers reject the new layout, the release retains live residue, and the build gate reintroduces a shared index write. |
| 2 | **(a) Purpose Check** + **(b) Design soundness** | ❌ | **(a) ❌ `not fit for purpose`:** master HL §3.1 says project views answer portfolio questions “without being edited by every workflow transition,” and §3.2 promises “Different tasks synchronize without a common edit.” A normal task-local transition makes `test_committed_index_is_current` fail until the reviewer rewrites the shared `workspace/00-INDEX.md`; unrelated tasks therefore meet again in one required file (`verify.md` F15). **(b) ❌ unsound:** seconds-only offline IDs and same-second/same-kind event paths collide; clean clones lose one state and one authority; docs consumers do not understand the new grammar/layout (`verify.md` F1–F8). |
| 3 | Tech debt documented | ✅ | RF §6 contains eleven concrete observations and a disclosed staging failure. Surviving observations are triaged below; existing TD-81, TD-144 and TD-177 are not duplicated or falsely closed. |
| 4 | Style & standards | ❌ | `verify.md` F10–F11: canonical workflows/templates and propagated copies mix `{ID}` with `{PREFIX}-1`, removed `initial_seq`, an old template version, and contradictory path depths. Init also contains orphaned tutorial table rows. |
| 5 | Observations collected | ✅ | RF §6 is unusually specific: it names stale knowledge, edition divergence, ignored task state, legacy values, harmless duplication, missing data, and the broad-staging incident. Observation 10 is filtered as harmless filler; the rest are routed or explicitly ruled below. |
| 6 | RF completeness (§7–§9) | ✅ | RF §7 has seven human-grounded Fact Candidates; §8 has four strategic insights; §9 renders before/after authority and file ownership. Required sections are present and substantive. |
| 7 | Evidence completeness — does it exist? | ✅ | EV contains 44 numbered items and all four named attachments exist. Nothing is missing; E16 is explicitly and correctly marked DEFERRED. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | `verify.md` evidence audit: 22 match, 10 are partial, 12 are contradicted. Green fixtures use different seconds/different kinds, a dirty working tree, a partial schema reader, and a non-shipped harness. |
| 9 | Backward compatibility | ❌ | `verify.md` F6–F10: `gen_docs.py` remains legacy-only, year-nested tasks group incorrectly, TFW-54's authority is absent from committed HEAD, the eleventh state is ignored, and live init/update/review instructions refer to removed allocation state. |
| 10 | Safety | ❌ | `verify.md` F8/F14: migration output depended on unrelated untracked work, and broad staging temporarily committed TFW-54/TFW-55 files. The executor repaired the index/worktree without deletion, but the release has not structurally prevented the recurring TD-144 failure. |

## Purpose Check — row 2(a)

**`not fit for purpose`.** The result points in the right direction and serves `.tfw/README.md` Success Criterion 1, “An authorized participant can resume from a durable checkpoint,” but the shipped enforcement defeats the specific master-contract value it exists to create: master HL §3.1 says project views answer portfolio questions “without being edited by every workflow transition,” and §3.2 says “Different tasks synchronize without a common edit.” After the normal TFW-60 `RF → REV` transition, the required current-index test fails until the reviewer rewrites the shared portfolio index; concurrent task transitions therefore contend in one common file to keep the build green.

The concrete harm is the original coordination bottleneck returning under a generated filename: task truth is local, but the mandatory green gate is not. This finding routes to the owner. The reference set itself is coherent; the internal TS conflict between AC-1 year nesting and AC-7 equal depth, and the impossible combination inside AC-2, are downstream specification defects requiring coordinator/owner revision before a new execution pass.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF/result claim | Contradiction? |
|---|----------------|-----------------|----------------|
| K1 | D66 — README is the only Task Board | Root board was removed and task state is authoritative | Yes — intentional release change, but D66 remains stale until a later approved docs pass |
| K2 | D65 — REJECTED lives in five carriers including README legend | Legend moved to glossary; RF says count becomes four | Yes — intentional, not yet consolidated |
| K3 | `knowledge/convention.md` F22 — root Task Board update is a process artifact | No live board update exists after this phase | Yes — the historical owner ruling remains true for its event, but its present-tense application is stale |
| K4 | D43 — citations require semantic relevance | ONB §7 rows 1, 2 and 12 resolve but their application notes discuss unrelated rulings | Yes — three semantic application failures, recorded in `verify.md` |
| K5 | D59 — declared attribution is not authentication | Team profiles explicitly preserve this boundary | No |
| K6 | D31/D50 — filesystem state/locality | Task-local state and stable paths follow the locality principle | No |

## Fact Candidate Review

RF §7 candidates 1–7 trace to explicit owner rulings or user statements and pass the Human-Only Test. They are not promoted during a rejected review. Candidate 4 should be interpreted narrowly as the owner-territory ruling for this phase, not a general permission to leave an acceptance gate unmet. No new human-only fact emerged in the review beyond the owner's explicit instruction to add the Codex participant profile; that instruction is recorded as a trace decision, not promoted as project knowledge.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence?
- [x] Every `⚪ N/A` carries a stated reason? No universal row uses N/A.
- [x] Row 2(a) answered against the contract baseline and North Star with a quoted clause and named harm?
- [x] Rows 7 and 8 answered separately?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §7–§9 for presence and quality?
- [x] KNOWLEDGE.md cross-referenced?
- [x] Fact Candidates challenged?

Stage complete: YES
