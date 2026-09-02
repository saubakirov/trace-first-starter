# RES — TFW_20260830-202031_FA15ES: Independent Bindings Coexistence and Provider-Neutral Assisted Update Sources — Iteration 2

> **Date**: 2026-09-02
> **Author**: saubakirov via Codex Researcher
> **Status**: 🔬 RES — Iteration 2 complete
> **Parent HL**: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> **Mode**: Pipeline / Focused

---

## Research Context

This iteration challenged iteration 1 decisions D1–D7 against the four open threads accepted by the Coordinator: exact binding/re-onboarding states, Windows and POSIX placement, Drive/GitHub/local acquisition and recheck behavior, the origin-authentication boundary, and durable documentation ownership. All fixtures were synthetic/in-memory or read-only. No product, HL, TS, task-state, or iteration-control file was changed.

## Briefing

The predecessor decisions, four open threads, focused plan, scope, and three guiding questions are recorded in [1_briefing.md](1_briefing.md). Gather decomposed nine dimensions and executed the binding/path fixture; Extract built binding and source configuration families plus live provider manifests; Challenge performed pairwise elimination, repeated external reads, injected same-version substitution, and ran the documentation deletion test.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Confirm H2a with B2: Full remains at `%LOCALAPPDATA%\tfw\bindings.yaml` on Windows and `~/.tfw/bindings.yaml` on POSIX; Assisted alone owns `%LOCALAPPDATA%\tfw\assisted\bindings.yml` or `~/.tfw/assisted/bindings.yml`. | The eight-state in-memory fixture resolved the real Windows known folder and asserted zero Full/legacy reads or writes. Combined schema, a new root that moves Full, and two platform-native physical roots each violate a frozen constraint (G1–G3, E1, C1). |
| D2 | Preserve and ignore the old `tfw-assisted` file. A missing canonical-new entry triggers the existing human gate once and creates only the current project's new `fixed` or `ask` entry; malformed/locked/unsafe new state remains untouched and yields session-only attribution. | Missing, valid, `ask`, disagreement, malformed, foreign-lock, shared-device, and autonomous cases all retained one Assisted authority with no merge, delete, profile conversion, other-project enumeration, or Full access (G2, C1). |
| D3 | Treat `~/.tfw/assisted` on macOS/Linux as an explicit TFW family-root exception, not as platform-preferred state placement. Retain every field safety check and session-only fallback. | XDG prefers `$XDG_STATE_HOME` and Apple prefers `~/Library/Application Support`; Full is already fixed at `~/.tfw`. A home path can still be shared/redirected, so only rejection of unsafe/shared/symlinked/unreservable state makes the placement honest (G3, E1, C1). |
| D4 | Define one capability-based acquisition contract for Drive, GitHub, local, and other forms: safe closed tree; human-confirmed publisher/locator; actual access form; `VERSION`/migration eligibility; strongest stable object identity available; available provider/out-of-band evidence; mandatory computed archive digest when applicable; mandatory normalized path/size/SHA-256 manifest; and full post-Gate recheck before writes. | The Drive-mounted folder, GitHub exact-commit zipball, and local folder all produced repeatable dynamic manifests despite different provider metadata. Provider-neutrality means conditional evidence fields, not pretending all providers expose the same schema (G4–G6, E2–E3, C2). |
| D5 | Write only from the approved, rechecked closed tree. Re-resolve/re-read the provider source, closed tree, target baselines, and protected paths after approval; any difference or unavailable required recheck returns to Compare and requires a new Gate. | The third Drive-field read and repeated GitHub ref were unchanged, while a same-version synthetic byte substitution changed the dynamic manifest despite identical version/structural markers. This closes the mutable-folder/link and time-of-check gap without a provider watcher (C2). |
| D6 | Accept human-confirmed origin plus computed integrity (A0+A1) as the honest minimum for the approved explicit human-gated scope; consume stronger provider, independent-digest, or attestation evidence when available, but never imply publisher authentication. | Both substituted fixtures validate against their own same-channel manifest. NIST hash semantics detect change after a digest exists; authenticated update designs require independently trusted keys/metadata. Signed trust-root governance is a separate future threat model, not an unsigned JSON job (E4, C3). |
| D7 | Put provider-specific shelf authority outside the replaceable installable package. For this repository, `editions/ASSISTED_MAINTENANCE.md` owns the public shelf and asymmetric promotion route; each downstream producer owns its separate human-readable publisher guide. Keep generic input forms in Assisted `README.md`, normative acquisition/recheck in `/tfw-update`, and version/protected migration in `MIGRATION.md` plus `CHANGELOG.md`. | A packaged publisher URL can be overwritten by the update it locates. The deletion test left one unique job per existing locus, and `/tfw-update` already asks once when no source is supplied (E5, C4). |
| D8 | Delete `maintenance/release-manifest.json` and `maintenance-policy.json` during implementation and add no replacement manifest/schema/registry. | Dynamic manifests did the accounting job across all fixtures; version/migration files, publisher docs, the updater, and optional external evidence cover every other surviving job. Same-package JSON cannot authenticate its own publisher (E6, C4). |
| D9 | Research is sufficient for TS planning. The current repository's GitHub Releases count is zero, so implementation/release work must select and materialize an actual public shelf without claiming a nonexistent release asset, digest, immutability, or attestation. | Both hypotheses survived all in-scope challenges. The remaining items are specification, implementation, and release truthfulness—not unresolved design research (C4–C5). |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Is moving Assisted on macOS/Linux from platform-preferred application-state roots into Full's `~/.tfw` parent acceptable? | Closed | Yes, as a documented family-root exception with the existing shared/sync/link/reservation checks and session-only fallback. It costs one-time re-onboarding and platform convention, not project/profile/task continuity. |
| Q2 | Can Drive, GitHub, and local forms expose enough exact-object/digest/recheck evidence without provider-specific core instructions? | Closed | Yes. Exact-object/provider digest evidence is capability-dependent; the mandatory common denominator is a safe closed tree, computed manifest, disclosure of unavailable signals, and full recheck. |
| Q3 | Is human-confirmed source plus computed integrity the accepted origin boundary? | Closed for FA15ES | Yes for this explicit human-gated scope, with exact non-authentication wording. Independently trusted digests or verified attestations may strengthen a run; a configured signing trust root belongs to a separate security contract. |
| Q4 | Which public shelf should this repository publish Assisted 1.6 from? | Implementation/release input | The publisher may choose Drive, GitHub exact-commit/archive or a future release asset, local, or another accessible representation. The current GitHub repository has no Releases, so no release-asset claim is presently valid. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H2a | One backward-compatible machine-local bindings facility can serve Full and Assisted concurrently while keeping their files or namespaces, project keys, profile schemas, and write protocols independent and leaving Full product files unchanged. | conditionally supported — iteration 1 selected B2 pending fixture and POSIX validation | 🟢 supported | D1–D3; Gather G1–G3; Extract E1; Challenge C1. Eight states, concrete Windows resolution, and explicit POSIX analysis preserve independent authorities and fail closed. |
| H4 | A provider-neutral source contract can let each Assisted producer select its own release location while the prompt-only `/tfw-update`, version, changelog, and migration maps keep updates explicit and human-gated; research must determine whether a separate manifest or schema has a unique necessary job. | supported in design — provider fixtures and origin boundary pending | 🟢 supported | D4–D8; Gather G4–G7; Extract E2–E6; Challenge C2–C4. Drive/GitHub/local cases share closed-tree manifest/recheck semantics; no static schema has a unique job. |

## HL Update Recommendations

> **The researcher classifies. The researcher never applies.** The Coordinator owns all HL changes and `research/iterations.yaml` updates.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 Current State | Replace the provisional B2 wording with the confirmed exact Windows/POSIX paths, eight-state re-onboarding behavior, legacy-preserve/ignore rule, and explicit statement that “backward-compatible” preserves product identity/behavior with one bounded local re-prompt rather than preserving the old on-disk path. | D1–D3; G1–G3; E1; C1 |
| R2 | §8 Dependencies | Mark the binding coexistence research dependency complete. Add a release-stage dependency to select/materialize the actual public Assisted shelf and ensure publisher documentation names only capabilities that exist; the current GitHub repository has zero Releases. | D9; E2; C4–C5 |
| R3 | §9 Risks | Add (a) `~/.tfw` may be shared/redirected on POSIX and must fail to session-only when locality/reservation is unproved; (b) a self-consistent substituted package passes same-channel hashes, so A0+A1 is integrity/change evidence, not origin authentication; and (c) a provider shelf claim can be false before the publisher creates the object. | D3, D6, D9; C1, C3–C4 |
| R4 | §10 RESEARCH Case | Mark H2a `supported — B2 fixture and Windows/POSIX challenge complete`; mark H4 `supported — capability-based acquisition, A0+A1 boundary, documentation loci, and Drive/GitHub/local fixtures complete`; close the four iteration-1 threads. | Hypotheses table; D1–D9; C5 |
| R5 | §11 Strategic Insights | Refine S7 with the assurance ladder and durable documentation boundary: mandatory dynamic evidence is provider-neutral, exact-object/provider signals are conditional, publisher-specific shelves live outside replaceable service content, and authenticated origin requires independently trusted evidence rather than a same-package manifest. | D4–D7; E3–E5; C2–C4 |

### Amendment Proposals — frozen sections, owner verdict required

No amendment proposals. The confirmed design instantiates the already approved frozen claims: independent bindings under one facility, unchanged Full files, prompt-only human-gated updates, producer-selected sources, and subtraction of redundant machinery.

## Fact Candidates

No new fact candidates. The Coordinator's acceptance, iteration state, scope, and authorized checkpoint continuation are already recorded in task artifacts or are workflow direction, not new human-only project knowledge.

## Strategic Insights (Research)

No strategic insights. No new human domain correction or selection occurred during this delegated iteration; the Researcher challenged the Coordinator-approved direction with project, provider, platform, and security evidence.

## Findings Map

```text
H2a — confirmed B2 facility

machine-local TFW family root
├── bindings.yaml                    Full only; unchanged
│   └── absolute project path → Full handle
└── assisted/bindings.yml            Assisted only
    └── project UUID → fixed(participant) | ask
         ├── missing → one human gate → new current-project entry
         ├── invalid/foreign lock/unsafe root → session-only, no repair
         ├── shared device → ask
         └── autonomous role → no local access

legacy tfw-assisted/bindings.yml → preserved, never read/merged/deleted
Windows root → LocalAppData
POSIX root  → ~/.tfw family exception + prove local/safe or fall back

H4 — confirmed capability contract

publisher-owned human guide outside replaceable package
        │ supplies/confirms exact versioned source
        ▼
Drive folder/blob ─┐
GitHub commit/asset ├─▶ safe closed tree ─▶ dynamic manifest ─▶ plan + Gate
local folder/archive┘          │                    │                 │
                              ├─ optional object/digest evidence     │
                              └─ VERSION + migration authority       │
                                                                       ▼
                         re-read provider + closed tree + target/protected
                                       │
                         changed/unavailable? ─ yes ─▶ Compare + new Gate
                                       │ no
                                       ▼
                             write only from closed tree

Assurance boundary: A0 human locator + A1 computed integrity required;
A2/A3 consumed when present; A4 trusted signing is a separate contract.

Rejected: combined/dual bindings · mutable-latest + VERSION only ·
same-channel origin claim · packaged provider locator · static JSON schema.
```

## Iteration Status

- **Iteration:** 2 of 2 (min) / 5 (max)
- **Hypotheses tested:** H2a (supported), H4 (supported)
- **Hypotheses deferred:** None
- **Gaps discovered:** No in-scope research gaps. Implementation/release must select and materialize the actual public shelf and verify the documented binding/source scenarios; signed origin authentication remains an explicitly separate future threat model.
- **Superseded decisions:** Iteration 2 D9 supersedes iteration 1 D8's `MORE NEEDED` conclusion because all four requested fixture threads are now closed. No design decision D1–D7 from iteration 1 was revoked; D1–D8 here confirm and sharpen them.

### Open Threads (for next iteration)

No open threads.

### Recommendation

- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [ ] **MORE NEEDED** — no in-scope research gap
- [ ] **BLOCKED** — no blocker

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 2 converted both iteration-1 designs into challenged contracts. B2 survived eight local-state cases and explicit Windows/macOS/Linux analysis: Full and Assisted share a physical family root but never a schema, authority, lock, migration, or writer, and unsafe POSIX state falls back to session-only behavior. Drive-mounted, GitHub exact-commit, and local inputs all converged on one closed-tree/dynamic-manifest/recheck algorithm while retaining honest provider-specific evidence grades. The same-version substitution fixture established the critical boundary: computed hashes detect drift after observation but do not authenticate the initial publisher. Publisher-specific shelf authority therefore stays in publisher-owned documentation outside replaceable service content, while Assisted docs remain generic and prompt-only; the static JSON pair has no unique job. The self-critique is bounded: no real binding store was written and no authenticated Drive object was fetched, by design of the synthetic/read-only mandate; those are TS verification cases, not unresolved research choices. The recommendation is `SUFFICIENT`.

---

*RES — TFW_20260830-202031_FA15ES: Independent Bindings Coexistence and Provider-Neutral Assisted Update Sources — Iteration 2 | 2026-09-02*
