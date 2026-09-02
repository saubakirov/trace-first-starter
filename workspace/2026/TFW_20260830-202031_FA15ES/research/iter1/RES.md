# RES — TFW_20260830-202031_FA15ES: Independent Bindings Coexistence and Provider-Neutral Assisted Update Sources — Iteration 1

> **Date**: 2026-09-02
> **Author**: saubakirov via Codex Researcher
> **Status**: 🔬 RES — Iteration 1 complete
> **Parent HL**: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> **Mode**: Pipeline / Focused

---

## Research Context

This iteration tested only HL hypotheses H2a and H4. It compared the unchanged Full binding contract, field Assisted 1.6 identity/update behavior, the rejected public maintenance JSON pair, and primary platform/provider documentation. The objective was to find the smallest same-device namespace and publisher-selected update-source contract that preserves implementation independence, prompt-only operation, human authority, and the frozen Editions-only boundary.

## Briefing

The approved plan, scope boundaries, and three guiding questions are recorded in [1_briefing.md](1_briefing.md). Gather decomposed six independent dimensions; Extract produced 28 composite binding/update configurations; Challenge stress-tested the surviving families without modifying product files, the HL, TS, or `research/iterations.yaml`.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Full and Assisted must never share one polymorphic binding file. | Full's file has one allowed path→handle key kind; Assisted has a versioned `project_id`/`fixed`/`ask` list and a stronger reservation protocol. Combining them changes Full and erases ownership boundaries (G1, C1). |
| D2 | Provisional H2a layout: keep Full exactly at its current path and place Assisted in an implementation-owned child under the existing Full parent—Windows `%LOCALAPPDATA%\tfw\assisted\bindings.yml`, POSIX `~/.tfw/assisted/bindings.yml`. | This creates one physical TFW device-local parent without Full edits. Full reads only `bindings.yaml`; Assisted reads only `assisted/bindings.yml` and retains `schema_version: 1`, UUID keys, modes, locks, and post-read rules (E1, C1). |
| D3 | Do not migrate, merge, delete, or permanently dual-read the old Assisted binding file. On first use at the new path, repeat the existing one-question human gate and create only the current project entry; preserve the old file untouched and ignored. | A guarded multi-project copy requires two-location locking and semantics for unavailable projects; dual read creates two authorities. One-time re-onboarding changes convenience once but preserves profiles, `project_id`, task owners, and shared state, matching a field-proven namespace-transition precedent (C1). |
| D4 | Treat provider neutrality as an acquisition behavior, not a provider schema. | Field `/tfw-update` already accepts a path, archive, URL, attachment, cloud object, or other accessible representation and normalizes it to one safe closed tree before the human gate (G3, E2). |
| D5 | Each producer should name its release shelf in human-readable publisher documentation; every update invocation supplies or confirms one exact versioned release object. Prefer a single archive plus provider/out-of-band digest, while retaining folder/local-tree input after a computed manifest. | Drive and GitHub differ in access but can publish the same versioned archive. A mutable folder/file/tag name is not exact byte identity; provider-specific retrieval stays outside the core contract (G4–G5, E3, C2). |
| D6 | Keep trust, integrity, version compatibility, migration authority, and actual-change evidence separate. | Human source confirmation establishes the current trust boundary; provider/out-of-band digest strengthens byte integrity; `VERSION` states the claim; `CHANGELOG.md`/`MIGRATION.md` authorize the transition; computed pre/post manifests record actions. No one signal substitutes for the others (G6, C3). |
| D7 | Delete the rejected static `release-manifest.json` and `maintenance-policy.json` in implementation; do not replace them with another checked-in source schema. | They duplicate existing carriers, are repository-relative rather than standalone-root-relative, and are unsigned within the same distribution boundary. They neither select a provider nor authenticate a publisher. Dynamic manifests retain the useful evidence job (E4, C4). |
| D8 | Iteration 1 is insufficient for final closure: H4 is supported in design; H2a remains conditional on fixture and cross-platform validation. | The task requires at least two iterations, and this iteration did not exercise an actual new/legacy binding pair or exact Drive/GitHub/local acquisition fixtures (C5). |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Is moving Assisted on macOS/Linux from platform-preferred application-state roots into Full's pre-existing `~/.tfw` parent an acceptable price for one physical family facility? | Open — iteration 2 | This iteration established the tradeoff but did not validate it against live platform behavior or an owner interpretation of “convenient.” |
| Q2 | Do actual Drive folder/archive and GitHub release-asset flows expose enough stable object/revision/digest evidence to replay the exact pre-gate recheck without provider-specific core instructions? | Open — iteration 2 | Primary APIs support the necessary metadata in principle; no end-to-end retrieval fixture was run. |
| Q3 | Is human-confirmed source plus available digest the accepted origin-authentication boundary, or is a future signed-release threat model required? | Open — Coordinator/owner after iteration 2 | The current scope is explicit, human-gated, and prompt-only. Signed unattended trust would require materially different machinery and a separate contract decision. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H2a | One backward-compatible machine-local bindings facility can serve Full and Assisted concurrently while keeping their files or namespaces, project keys, profile schemas, and write protocols independent and leaving Full product files unchanged. | needs-research | 🟡 conditionally supported | D1–D3; Gather G1–G2; Extract E1; Challenge C1. The B2 layout satisfies the invariants on paper; fixture and POSIX validation remain. |
| H4 | A provider-neutral source contract can let each Assisted producer select its own release location while the prompt-only `/tfw-update`, version, changelog, and migration maps keep updates explicit and human-gated; research must determine whether a separate manifest or schema has a unique necessary job. | needs-research | 🟡 supported in design; case validation pending | D4–D7; Gather G3–G6; Extract E2–E4; Challenge C2–C4. No separate source manifest has a unique in-scope job. |

## HL Update Recommendations

> **The researcher classifies. The researcher never applies.** The Coordinator owns all HL changes and `research/iterations.yaml` updates.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 Current State | Add the provisional coexistence result: a common parent can work only through independently owned sibling/child files; a combined binding schema would violate both implementations. Record B2's exact proposed paths and the one-time re-onboarding rule as research output, not yet final implementation authority. | D1–D3; G1–G2; E1; C1 |
| R2 | §8 Dependencies | Change “Exact Assisted identity-invariant and backward-compatible same-device binding coexistence matrix” from pending to `🟡 design established; Windows/POSIX fixture validation pending in iteration 2`. | D2–D3; C1; Iteration Status gaps |
| R3 | §9 Risks | Add (a) old/new Assisted releases can retain divergent device-local selections after the path transition, and (b) Drive IDs/folders and ordinary Git tags/releases are mutable locators unless exact revision/digest/immutable-release evidence is captured. Mitigate with canonical-new-only reads, legacy preservation, exact version resolution, recheck, and explicit gate. | C1–C3 |
| R4 | §10 RESEARCH Case | Mark H2a `conditionally supported — B2 pending fixture/portability challenge`; mark H4 `supported in design — U3 guidance with U2/U1 inputs, no new manifest, provider fixtures pending`. Carry Q1–Q3 into iteration 2. | Hypotheses table; D8 |
| R5 | §11 Strategic Insights | Add that “one facility” is a namespace/ownership boundary rather than a shared schema, and that provider neutrality belongs in the updater's acquisition contract while publisher choice remains human-readable. A static unsigned manifest is neither provider neutrality nor source authentication. | D1, D4–D7; Findings Map |

### Amendment Proposals — frozen sections, owner verdict required

No amendment proposals. The provisional design fits the existing frozen claims: one facility with isolated schemas, unchanged Full files, prompt-only updates, human gates, provider-selected sources, and no new executable or schema machinery.

## Fact Candidates

No new fact candidates. The delegation introduced no new human-only project fact beyond the owner directions already recorded in HL §§8, 10, and 11.

## Strategic Insights (Research)

No strategic insights. No new human domain correction or selection occurred during this delegated research iteration; the Researcher used only the approved HL direction.

## Findings Map

```text
H2a — one device-local facility
│
├─ Full authority (unchanged)
│  └─ <tfw-parent>/bindings.yaml
│     └─ absolute project path → Full team handle
│
└─ Assisted authority (independent child)
   └─ <tfw-parent>/assisted/bindings.yml
      ├─ schema_version: 1
      ├─ project_id → fixed(participant) | ask
      ├─ Assisted-only reservation + post-read
      └─ old tfw-assisted file preserved, never merged/read as fallback

H4 — provider-neutral release flow

publisher documentation names shelf
        │
        ├─ Google Drive folder ─┐
        ├─ GitHub releases ─────┼─▶ exact versioned package locator
        └─ path/link/archive ───┘            │
                                             ▼
                                  safe temporary closed tree
                                             │
                    ┌────────────────────────┼───────────────────────┐
                    ▼                        ▼                       ▼
              VERSION claim       CHANGELOG/MIGRATION       digest + manifest
                    └────────────────────────┼───────────────────────┘
                                             ▼
                                      one human write gate

Rejected branch: combined binding YAML / dual authority / mutable latest /
unsigned static source manifest / provider-specific runtime.
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 5 (max)
- **Hypotheses tested:** H2a (conditionally supported), H4 (supported in design; provider-case validation pending)
- **Hypotheses deferred:** None; empirical fixture work was deferred, not either hypothesis.
- **Gaps discovered:** POSIX common-parent tradeoff; exact new/legacy Assisted binding fixture; Drive folder/archive and GitHub release-asset retrieval/recheck fixtures; explicit origin-authentication boundary.
- **Superseded decisions:** None.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | B2 binding path and re-onboarding fixture | H2a currently rests on contract analysis, not observed file behavior; legacy preservation and zero Full writes must be demonstrated. | Materialize synthetic Full/new-Assisted/legacy-Assisted files outside the product tree; exercise missing, valid, invalid, locked, shared-device, and both-present states on Windows; inspect POSIX path implications separately. |
| 2 | Drive/GitHub/local source matrix | H4 must prove the same updater invariants survive different access forms without provider-specific core logic. | Exercise a synced Drive-style folder or accessible Drive object, a GitHub release asset/archive, and a local folder/archive; record resolved version/object/digest, safe-tree checks, recheck behavior, and exact blockers. |
| 3 | Mutable locator and origin boundary | Human confirmation plus computed digest detects change but does not authenticate a substituted valid package. | Decide whether explicit residual-risk wording is sufficient for the approved human-gated scope; if not, formulate a separate signed-release amendment/task rather than smuggling trust machinery into FA15ES. |
| 4 | Exact documentation locus | Publisher choice must remain visible after overlay updates without becoming provider configuration schema. | Compare the minimum edits across Assisted `README.md`, `MIGRATION.md`, `/tfw-update`, and `editions/ASSISTED_MAINTENANCE.md`; keep one authority per claim and one publisher-specific human-readable route. |

### Recommendation

- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [x] **MORE NEEDED** — run the Coordinator-approved iteration 2 to challenge B2 and U3/U2/U1 with actual coexistence and Drive/GitHub/local fixtures, then decide the origin-authentication boundary.
- [ ] **BLOCKED** — no blocker

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 1 found that both problems can be solved by boundaries rather than new machinery: isolate Assisted below Full's unchanged device-local parent and re-onboard once instead of migrating or dual-reading state; keep `/tfw-update` transport-neutral, let each publisher document its source shelf, resolve one exact versioned package per invocation, and use available digest plus dynamic manifests before the human gate. The rejected JSON manifest/policy pair adds no unique in-scope authority and still does not authenticate a publisher. The self-critique is material: these are evidence-backed contract conclusions, not observed end-to-end fixtures, and the POSIX placement cost plus source-substitution boundary remain open. Iteration 2 is therefore required before the Coordinator treats either design as TS-ready.

---

*RES — TFW_20260830-202031_FA15ES: Independent Bindings Coexistence and Provider-Neutral Assisted Update Sources — Iteration 1 | 2026-09-02*
