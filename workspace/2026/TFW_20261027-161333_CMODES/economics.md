# Economics — TFW_20261027-161333_CMODES

Prepared-result checkpoint: 2026-10-28T08:03:17.710017+00:00. Product Candidate `c6dd3155d5f4e42d2ef1d1ff3bdc4c5b1db8e5ee` has independent final APPROVE at `698e2c8bf1fbc3ab768b1cfdfb80f87e9a73da1a`; lifecycle is KNW pending actual owner acceptance. This is the reconciled preparation-cycle basis, not a completed-task lifetime total or release.

## Result and decision

The approved work makes three coordination modes explicit for one or multiple phases, preserves one owner-facing Coordinator, independent file-context roles, real phase state and lean model/effort judgment. Final delivery has 38 VALUE files, 826 additions + 374 deletions = 1,200 touched LOC; two material defects were repaired and independently checked. Accepted ECFIX is already in Baseline and its four files are unchanged.

Sources: [status](status.md), [HL](HL-TFW_20261027-161333_CMODES.md), [RF](RF__TFW_20261027-161333_CMODES.md), [final REVIEW](REVIEW__TFW_20261027-161333_CMODES.md). Primary area: coordination. Keywords: coordination modes, native subagents, phase routing, independent review, file context. These are task-associated resources, not separately allocated feature costs.

## Received and selected resources

Expected physical units: **8**; received: **8**; measured in selected bounds: **8**. Missing/failure-only/omitted units: **0/0/0**. 25 distinct received JSONL files reconcile to 9 selected files and 16 numeric rows. 16 verified covered predecessors remain preserved and are excluded from totals. There is no conflicting overlap, inclusive-parent duplication or reconciliation diagnostic.

**131,209,136 tokens** = 2,892,433 fresh input + 127,572,480 cached input + 744,223 output. Input total 130,464,913 includes cache; 235,554 reasoning tokens are already a subset of output. Cached input is 97.78% of input. These are native consumption facts, not a subscription bill or proof of efficiency.

| Producer / actual unit | Observed model and effort | Fresh input | Cached input | Output | Total tokens |
|---|---|---:|---:|---:|---:|
| Coordinator; `codex:thread:local:01a17d06-be29-7a31-afe4-bbd67c5cc3b7` | gpt-6-astra/max | 1,106,834 | 68,670,592 | 417,019 | 70,194,445 |
| Researcher; `codex:thread:local:01a17db6-0f53-7603-878a-adaa590010e4` | gpt-6-astra/high | 512,933 | 21,702,400 | 119,288 | 22,334,621 |
| Product Executor; `codex:thread:local:01a180dd-4622-7b02-adaa-7ec70b9ae50a` | gpt-6.1-sol/high | 286,181 | 16,369,792 | 80,815 | 16,736,788 |
| Product Reviewer; `codex:thread:local:01a1813d-7849-7890-8d76-609ba0c80190` | gpt-6-astra/high | 387,440 | 9,438,976 | 59,569 | 9,885,985 |
| Failed probe and accountability return; `01a180f4-c4fb-7302-ace6-36bd0302526b` | gpt-6.1-sol/medium | 63,870 | 810,112 | 3,309 | 877,291 |
| Native phase A/B Executor; `01a180fb-2d66-7ae2-ac3f-58c0c118a7a3` | gpt-6.1-sol/high | 258,224 | 4,886,528 | 30,080 | 5,174,832 |
| Native phase A Reviewer; `01a18105-fcd4-7d20-9eb9-40ff4c9b7755` | gpt-6.1-sol/high | 150,727 | 3,428,480 | 17,080 | 3,596,287 |
| Native phase B Reviewer; `01a18120-f269-70c1-a5e8-3cd77a52c667` | gpt-6.1-sol/high | 126,224 | 2,265,600 | 17,063 | 2,408,887 |

## Exact selected source basis

Every source is `codex.rollout` with the exact source ID below. Hashes address returned numeric bytes, not another role's private transcript. Root sources remain phase-null; the reused native Executor has two proven disjoint phase bounds. All earlier versions remain in their original role folders.

| Producer / phase | Source ID | Revision / range | Cutoff UTC | Returned SHA-256 |
|---|---|---|---|---|
| Failed probe and accountability return / phase-a | `01a180f4-c4fb-7302-ace6-36bd0302526b` | r1 / [0,156) | 2026-10-28T06:33:01.043075+00:00 | `99548a482f8eb274eb992d0adb0a7d5005dc76fc4d516545ad8d4c9f9618c636` |
| Native phase A/B Executor / phase-a | `01a180fb-2d66-7ae2-ac3f-58c0c118a7a3` | r1 / [0,212) | 2026-10-28T05:35:06.784094+00:00 | `5276e8b84cb3d796f116476b380b19cbeb948a304aa98821669fb9467dc931a9` |
| Native phase A/B Executor / phase-b | `01a180fb-2d66-7ae2-ac3f-58c0c118a7a3` | r2 / [264,367) | 2026-10-28T06:07:24.853604+00:00 | `0711d65b2772128d5728c3b391543be6c58f13d1f52e97391cd2ab7f85b288fd` |
| Native phase A Reviewer / phase-a | `01a18105-fcd4-7d20-9eb9-40ff4c9b7755` | r1 / [0,242) | 2026-10-28T05:47:30.716852+00:00 | `f0292504a8d335245425dfa2bb9fab7d73749703f7a722656aa3e36e38d17809` |
| Native phase B Reviewer / phase-b | `01a18120-f269-70c1-a5e8-3cd77a52c667` | r1 / [0,185) | 2026-10-28T06:16:57.984766+00:00 | `d6b332fe7d9df81bae0e55d1321511a7b1b8d13e08b0dcb2e21dc466e9957529` |
| Coordinator / task | `01a17d06-be29-7a31-afe4-bbd67c5cc3b7` | r11 / [0,4033) | 2026-10-28T08:03:17.710017+00:00 | `12221e652f787e1ed75822a36aa16f0a7a4cec2ef951a635026f6d24485ffe55` |
| Researcher / task | `01a17db6-0f53-7603-878a-adaa590010e4` | r3 / [0,1240) | 2026-10-27T18:43:44.455744+00:00 | `ec6f19bd95f1a107bc190713e5bb4ee73445e285ee5049bbf261365b1bd50fe3` |
| Product Executor / task | `01a180dd-4622-7b02-adaa-7ec70b9ae50a` | r3 / [0,648) | 2026-10-28T07:31:22.747516+00:00 | `d740973551d8f53ccd301367b4872ec84af31f70f6cfd586619986da5e93dace` |
| Product Reviewer / task | `01a1813d-7849-7890-8d76-609ba0c80190` | r3 / [0,621) | 2026-10-28T07:45:16.030007+00:00 | `4fd05c591e7573b13abccd0ebb9090d398165dbd74e139829b6e46271d97ab9b` |

Selected byte locators:

- `0711d65b2772128d5728c3b391543be6c58f13d1f52e97391cd2ab7f85b288fd`: Git object `31a7997dbae8ec0843afffe465a03eaefa19b889:native-proof/2026/TFW_20261027-161333_CMODES/phase-b/economics/roles/0711d65b2772128d5728c3b391543be6c58f13d1f52e97391cd2ab7f85b288fd.jsonl`.
- `12221e652f787e1ed75822a36aa16f0a7a4cec2ef951a635026f6d24485ffe55`: [economics/roles/12221e652f787e1ed75822a36aa16f0a7a4cec2ef951a635026f6d24485ffe55.jsonl](economics/roles/12221e652f787e1ed75822a36aa16f0a7a4cec2ef951a635026f6d24485ffe55.jsonl).
- `4fd05c591e7573b13abccd0ebb9090d398165dbd74e139829b6e46271d97ab9b`: [economics/roles/4fd05c591e7573b13abccd0ebb9090d398165dbd74e139829b6e46271d97ab9b.jsonl](economics/roles/4fd05c591e7573b13abccd0ebb9090d398165dbd74e139829b6e46271d97ab9b.jsonl).
- `5276e8b84cb3d796f116476b380b19cbeb948a304aa98821669fb9467dc931a9`: Git object `31a7997dbae8ec0843afffe465a03eaefa19b889:native-proof/2026/TFW_20261027-161333_CMODES/phase-a/economics/roles/5276e8b84cb3d796f116476b380b19cbeb948a304aa98821669fb9467dc931a9.jsonl`.
- `99548a482f8eb274eb992d0adb0a7d5005dc76fc4d516545ad8d4c9f9618c636`: Git object `31a7997dbae8ec0843afffe465a03eaefa19b889:native-proof/2026/TFW_20261027-161333_CMODES/phase-a/economics/roles/99548a482f8eb274eb992d0adb0a7d5005dc76fc4d516545ad8d4c9f9618c636.jsonl`.
- `d6b332fe7d9df81bae0e55d1321511a7b1b8d13e08b0dcb2e21dc466e9957529`: Git object `31a7997dbae8ec0843afffe465a03eaefa19b889:native-proof/2026/TFW_20261027-161333_CMODES/phase-b/economics/roles/d6b332fe7d9df81bae0e55d1321511a7b1b8d13e08b0dcb2e21dc466e9957529.jsonl`.
- `d740973551d8f53ccd301367b4872ec84af31f70f6cfd586619986da5e93dace`: [economics/roles/d740973551d8f53ccd301367b4872ec84af31f70f6cfd586619986da5e93dace.jsonl](economics/roles/d740973551d8f53ccd301367b4872ec84af31f70f6cfd586619986da5e93dace.jsonl).
- `ec6f19bd95f1a107bc190713e5bb4ee73445e285ee5049bbf261365b1bd50fe3`: [economics/roles/ec6f19bd95f1a107bc190713e5bb4ee73445e285ee5049bbf261365b1bd50fe3.jsonl](economics/roles/ec6f19bd95f1a107bc190713e5bb4ee73445e285ee5049bbf261365b1bd50fe3.jsonl).
- `f0292504a8d335245425dfa2bb9fab7d73749703f7a722656aa3e36e38d17809`: Git object `31a7997dbae8ec0843afffe465a03eaefa19b889:native-proof/2026/TFW_20261027-161333_CMODES/phase-a/economics/roles/f0292504a8d335245425dfa2bb9fab7d73749703f7a722656aa3e36e38d17809.jsonl`.

## Reproduction and limits

Use unchanged `.tfw/economics/tfw_economics.py` `reconcile(paths, expected_units)` over all direct `economics/roles/*.jsonl` here plus exactly five phase-leaf JSONL objects under `native-proof/2026/TFW_20261027-161333_CMODES/phase-*/economics/roles/` at `31a7997dbae8ec0843afffe465a03eaefa19b889`. Obtain each with `git show <commit>:<path>` into system temp, verify its filename SHA-256, then validate/reconcile. Include earlier direct snapshots so covering predecessors verify. Do not include proof-root copied receipts/reports, relabel phase records into the task root, add cumulative snapshots, or sum report totals.

Coordinator r11 receipt `12221e652f787e1ed75822a36aa16f0a7a4cec2ef951a635026f6d24485ffe55` captures its own source after required final role returns, reference effects, independent judgment and relevant integration checks: [0,4033), 16,312,182 bytes, source prefix SHA-256 `d6f55ad8467ce7d5139c86119cb546f6f1f39b6169292e27fb8b2a75c8df39b6`. It verifies and replaces r10 without altering prior bytes. Each producer read only its own native source; Coordinator consumed returned numeric files.

The failed probe includes both refused calls and its later accountability-only reconstruction at the actual cutoff. Earlier missing-return statements remain truthful at their epochs. Executor A/B ranges [0,212) and [264,367) are disjoint; [212,264) is the disclosed unmeasured A sealing tail, not automatically assigned to B. Final role sealing/delivery, this report/record sealing, owner delivery, short exchanges and safe cleanup are a disclosed excluded tail. Later owner decisions, substantive correction or release preparation need a new bound; they are not hidden in it.

Complete selected bytes do not mean complete turn/task duration or zero unobserved usage. Native response streams reconcile to their own counters; older disagreeing token_count streams remain diagnosed in manifests and are never added. Completed-turn durations remain per-source observations in the JSONL, with open/aborted turns unknown; parent waits and child work overlap, so summing them is not project elapsed or human time. Collector operation_seconds is separate. No compatible total elapsed/human-time measure is established.

No current exact-model official price basis was selected for this checkpoint; money remains unavailable. No USD, subscription charge, measured saving, ROI, model superiority or 5–7% error bound is inferred. There is no matched comparison task or counterfactual proving this topology saves resources. The supported action is to retain the reviewed design and take the owner's actual-change decision, then begin separately bounded 3.9.3 preparation.

Managed fixture worktrees are archived and proof bytes are reachable. Main candidate/E/R worktrees remain for owner acceptance/correction. Denied private-temp deletion and the empty archived proof directory have explicit owner-assisted dispositions in REVIEW §6; no successful cleanup is invented. This Coordinator's own report transfer copies remain in its task-temp subtree until that decision and safe disposal.
