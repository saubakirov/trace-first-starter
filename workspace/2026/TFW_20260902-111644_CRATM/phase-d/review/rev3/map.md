# Map rev3 — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase D](../../RF__phase-d__team_mode_and_role_assignment.md), cumulative Round 3
> TS: [TS Phase D revision 3](../../TS__phase-d__team_mode_and_role_assignment__rev3.md), with revision-2 AC-1–AC-5 retained

## Understanding

Round 3 replaces the earlier Phase D product result with Candidate
`2363c3d315a855fc0bd6c6dbf683e16bfbaf1726` under approval epoch
`b755de9128f2b0442615a4ca8b787761f937bbcd`. It implements owner-approved A7 as one selected stable
LEAD principal whose root Coordinator creates distinct, directly addressable Coordinator,
Researcher, Executor, and Reviewer units; shared principal attribution neither merges units nor
distributes the root's amendment grant.

The round also implements the supplied-versus-additional profile-admission correction from REVIEW
rev2 and adds root-only, handle-bearing session navigation. Only the selected agent principal acting
in the mandate's exact root Coordinator unit may render `LEAD · {handle} · TASK[ · PHASE]` in Plan
or Resume; children and unresolved identities retain ordinary workflow cues. The implementation
changes the approved 21 VALUE paths and two ASSURANCE paths in one Candidate commit, then appends
cumulative EV/RF and RF-state TRACE before the direct Reviewer dispatch.

The actual review chain is operationally human-rooted rather than self-authorized by the product
under review. Acting handle is the sole profile `saubakirov`; Phase D Coordinator unit
`01a07697-f428-7582-ade4-50997a4a6d63` directly dispatched this existing independent Reviewer unit
`01a0770e-ca5c-7182-95ed-64c7ba0b555a`. Proposal origin remains `{principal: saubakirov, unit:
01a07050-9d35-7080-a5f6-afd14334e68d}` as recorded in the dispatch; forwarding did not replace it.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| Rev2 AC-1 — explicit post-HL owner choice, one selected LEAD mandate, seven returns, safe degradation | Round-3 RF/EV say 14 source-derived AT cases preserve the explicit owner choice and return/degradation contract | ✅ claimed |
| Rev2 AC-2 — principal, actual unit, parent, and proposal origin remain distinct; no inherited/self-ruling grant | RF says source-derived authority/unit cases and mutants preserve `{principal, unit}`, parentage, and origin | ✅ claimed |
| Rev2 AC-3 — protected mandate separated from dynamic working-unit instantiation and owner-approved replacement | RF says the HL template has two layers and replacement requires `SUPERSEDE` plus bounded dispatch | ✅ claimed |
| Rev2 AC-4 — four workflows/copies/Codex operations enforce distinct direct units and same-role return | RF says five canonical consumers plus ten accepted copies and the managed receiver are exact, with existing Executor/Reviewer reuse | ✅ claimed |
| Rev2 AC-5 — supplied Codex limited admission plus native all-eight requirement for every additional profile | RF says combined admission returns `ADMIT_SUPPLIED_LIMITED`, rejects incomplete additional profiles, and rejects universal/partial mutants | ✅ claimed |
| Rev3 AC-6 — approved 21-path replacement Candidate, WIP preservation, two epochs, A5, tests/build | RF reports exact 21 VALUE + 2 ASSURANCE Candidate, `459+462=921`, preserved WIP digest, active corpus `33,676/33,749`, full suite/build, and protected history | ✅ claimed |
| Rev3 AC-7 — exact selected root alone renders stable handle-bearing LEAD across Plan/Resume, with inherited collision/readback/fail-soft behavior | RF reports 16 navigation cases and 14 root-navigation mutants; root Plan/Resume qualify and children/invalid sources fail soft | ✅ claimed; collision/readback behavior requires explicit independent verification |

## Deviations from TS

The RF reports no membership or implementation deviation. Actual VALUE is 11 touched LOC below the
approved `21/932` forecast: `459` additions + `462` deletions = `921`, with the same 21-member
selector. The four figures remain separately disclosed: historical `16/640`, rev2 forecast `18/760`,
observed pre-approval WIP `18/866`, rev3 forecast `21/932`, and actual Candidate `21/921`.

The strict-build evidence claim is bounded: the attachment compares the 24 warning tokens and their
tracked-Markdown occurrence counts before Candidate and at Candidate. It does not claim byte-equal or
otherwise equivalent complete build logs.

RTBO/saved-master integration, retired runtime/index restoration, knowledge promotion, Phase E,
release, tag, and push remain outside this review and Candidate.

## Changed Surface and Referenced Predecessors

Candidate itself contains exactly 23 modified paths: the 21 literal VALUE members and the two
ASSURANCE modules. Product Baseline→Candidate contains historical/TRACE paths as expected, but the
accounting selector charges only the approved 21 VALUE files. Governing predecessors are owner A7
freeze `2386bfb0994f6e0a1aed7b734e345cdb2a540ae1`, TS rev2/REVIEW rev2, historical A–C and original-D
epochs, WIP-preservation checkpoint `c1809cd4a9c85c8dbc83e5c31fc6daa797debd29`, rev3 approval, and
the post-Candidate EV/RF/state/dispatch chain.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely, including cumulative Round 3?
- [x] Read governing TS rev3 and retained rev2 AC-1–AC-5, then matched each item to RF claims?
- [x] Read master HL §7 Principles — can I state the design philosophy?
- [x] Read cumulative ONB — were blocking questions resolved?

Stage complete: YES
