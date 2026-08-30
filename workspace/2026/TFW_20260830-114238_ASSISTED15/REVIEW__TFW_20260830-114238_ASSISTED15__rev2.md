# REVIEW — TFW_20260830-114238_ASSISTED15 / Repeat Review 2: Neutral Assisted 1.5 Product and Maintenance Bridge

> **Date**: 2026-08-30
> **Author**: saubakirov via Codex Reviewer
> **Verdict**: 🔄 REVISE
> **RF**: [RF — TFW_20260830-114238_ASSISTED15](RF__TFW_20260830-114238_ASSISTED15.md)
> **TS**: [TS — TFW_20260830-114238_ASSISTED15](TS__TFW_20260830-114238_ASSISTED15.md)
> **Historical review**: [First-pass REVISE](REVIEW__TFW_20260830-114238_ASSISTED15.md)
> **Stage files**: `review/rev2/map.md`, `review/rev2/verify.md`, `review/rev2/judge.md`
> This is a full repeat review after corrections `b37f7a3`, `964abd2`, `85d4e76`. The first review and its D1–D8 evidence remain immutable history.

---

## 1. Map

The corrected result remains a standalone Russian-authoritative Assisted 1.5 within the frozen 35-path `editions/` boundary. It combines five lifecycle roles, local identity, neutral reusable templates, public-only release history, and an asymmetric bridge: verified public stock moves forward under a closed baseline, while downstream learning returns only as a privacy-safe review candidate. The real mixed field tree remains read-only P6 evidence rather than public payload.

The same Executor corrected all eight first-pass findings without adding a product path. This same independent Reviewer then repeated Map, Verify and Judge over the complete current product and evidence package, not only the correction diff.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| 1 | Frozen/product boundary and commit attribution | ✅ | 35/35 product paths: 25 added, 7 modified, 3 deleted; 3,649 changed lines; all 17 Assisted commits have zero forbidden-path hits. Concurrent external root/TFW-60 changes were separated by the dual audit. |
| 2 | Historical correction package D1–D8 | ✅ | Exact manifest regeneration, manifest-carrying next source, Windows junction rejection, identity chain/ACL, reverse provenance/confinement, seven role cases, documented identity command and clean renders all independently rerun and closed. |
| 3 | Complete product/evidence/citation census | ⚠️ | 35/35 product paths and 47/47 evidence attachments were inspected; 39 evidence files fully support their bounded claim, 8 are partial/overclaiming, 0 are missing. All 20 HL/ONB citation applications resolve and match semantics. |
| 4 | Fresh release, maintenance, identity and template validation | ❌ | Stock commands pass, but independent hostile checks find D9: the target-keyed “project” lock lives under each unique operation directory, and D10: registry read precedes first locality re-probe. The green matrix is incomplete against AC-3/8/11/12. |
| 5 | Rendered result and semantic neutrality/privacy | ✅ | All 16 PDF page PNGs and four browser full captures were opened; glyphs, tokens, tables and layouts are readable with no local URL/seam/byte mismatch. All 35 product paths are generic; no Innoforce knowledge/person/brand/private history/path payload is shipped. |
| 6 | EV E4 lifecycle dependency | ✅ | Live tree is exactly one Phase Coordinator → same completed Executor → same independent Reviewer; Coordinator-only reporting and the seven deterministic role records are established. E4 closes. |
| 7 | EV E12 directions, field source and publication | ⚠️ | Both direction mechanics, 29-row H: pre/post equality under both documented sort orders, and no publication are proven. E12 cannot close as a whole because AC-12 depends on AC-3/AC-11 and D9 leaves cross-operation locking unproved. |

Raw verification: [review/rev2/verify.md](review/rev2/verify.md).

### Repeat-review findings

| ID | Severity | Exact finding | Required acceptance evidence |
|---|---|---|---|
| D9 | Critical | `editions/maintenance/assisted_maintenance.py:644-647` derives a stable key but puts the lock in the unique `operation/` directory. A same-target second operation used a different lock path and returned `verified` while the first lock was held. | Use a stable private pinned target-keyed lock independent of operation directory, acquired before baseline/staging/mutation. An independent real two-process same-target fixture must prove distinct operation directories contend and the losing operation performs zero product writes. |
| D10 | High | `editions/02-assisted/.agents/skills/tfw-identity/scripts/tfw_identity.py:495-500` and `:761-764` read the registry before the first full-chain locality re-probe. Instrumented order is `read_registry→reprobe`. | Re-probe full chain plus owner/private ACL before any registry/lock existence, type or byte access; remove the redundant dispatcher pre-read and keep reads under validated locking where applicable. An independent substitution-before-first-read fixture must prove zero substituted-registry read and zero persistent write. |

Historical D1–D8 are closed and must not be reopened as correction scope unless a D9/D10 fix demonstrably regresses them.

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | D9 leaves AC-3/AC-11 unmet; D10 leaves AC-8/AC-11 unmet; AC-12 remains dependent on the failed AC-3/AC-11 property. |
| 2 | Purpose Check + design soundness | ❌ | Purpose is aligned with frozen HL §1 at `ee09a8a` and North Star NS1: the neutral product prevents users remaining on 1.0 or inheriting private practice. Design soundness fails only because D9/D10 do not structurally enforce the promised lock/locality boundaries. No contract defect or amendment exists. |
| 3 | Tech debt documented | ✅ | RF §6 says no observations; D9/D10 are current-scope fixes, not deferred debt. |
| 4 | Style & standards | ✅ | Exact boundary, naming, Russian readability, no placeholders and truthful public history hold. The remaining findings are safety/design, not style. |
| 5 | Observations collected | ✅ | RF reports none; both independent findings remain in acceptance scope. |
| 6 | RF completeness (§7–9 present) | ✅ | Two valid human-sourced Fact Candidates, two useful strategic insights and an accurate authority-flow diagram are present. |
| 7 | Evidence completeness — does it exist? | ✅ | 47/47 attachments exist and every TS evidence class is represented. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | 8/47 attachments overstate complete V3/V8/V11 coverage; none tests D9’s cross-operation contention or D10’s first-access ordering. |
| 9 | Backward compatibility | ✅ | 1.0→1.5 migration, protected state, next-source use, identity command and templates work; D9/D10 are new-mechanism safety gaps rather than observed legacy interface breaks. |
| 10 | Safety | ❌ | Neutrality, reverse confinement, field immutability and no publication hold, but D9 permits simultaneous same-target maintenance and D10 permits identity access before locality/ACL revalidation. |

Full ruling: [review/rev2/judge.md](review/rev2/judge.md).

## 4. Verdict

**🔄 REVISE**

The result is fit for the approved purpose, stays inside the frozen boundary, and closes all eight first-pass findings. It is not acceptance-ready because one Critical and one High safety defect remain in the two mechanisms used to claim conflict-resistant maintenance and operation-time identity locality. The evidence package is complete but not sufficient for AC-3/8/11/12: 39/47 attachments support their bounded claims, while 8 inherit the incomplete race/order matrix.

No HL/TS amendment is needed. The same Executor must make only the two bounded corrections below, and the same Reviewer must independently rerun the entire review contract afterward; next review must include independent concurrency and call-order/substitution tests rather than trusting the Executor’s fixtures.

### Items to fix

1. **D9 — shared same-target project lock.** Within existing product paths, move the target-keyed lock to a stable private pinned location independent of `operation/`; acquire it before baseline, staging and mutation. Add retained real two-process same-target contention plus zero-write-loser evidence. Do not add a product path.
2. **D10 — revalidation before first identity access.** Within existing product paths, perform full-chain and owner/private-ACL re-probe before any registry/lock exists/type/read access, remove the redundant dispatcher pre-read, and use validated locked reads. Add substitution-before-first-read evidence proving zero substituted read and zero persistent write. Do not add a product path.

Correction constraints: H: remains strictly read-only; product changes remain under `editions/`; RF/evidence changes remain task-local; root guides, `.tfw`, `KNOWLEDGE.md`, `TECH_DEBT.md`, Light and unrelated work stay untouched; no push, tag or publication.

## 5. Tech Debt Collected

No tech-debt item is collected. D9/D10 are current-scope acceptance defects and cannot be deferred.

## 6. Traces Updated

- [x] Task `status.md` remains lifecycle `RF` for correction and receives a new RF→RF transition event for this repeat verdict.
- [x] The first-pass REVIEW and `review/{map,verify,judge}.md` remain unchanged; revision 2 uses distinct artifacts.
- [x] HL/TS/ONB/RF/EV and implementation remain unchanged by the Reviewer.
- [x] Unrelated `.gitignore`, TFW-55 and concurrent shared state remain unstaged and unmodified by this review.
- [x] tfw-docs: N/A until APPROVE; the frozen product boundary forbids root guide/`KNOWLEDGE.md` changes during correction.
- [x] tfw-knowledge: N/A until APPROVE; RF candidates remain candidates and no scope-drift consolidation occurs on REVISE.

## 7. Fact Candidates

No new reviewer-observed human-only Fact Candidate was introduced. The two user-sourced RF §7 candidates remain relevant and unchallenged; consolidation waits for eventual approval.

---

*REVIEW — TFW_20260830-114238_ASSISTED15 / Repeat Review 2: Neutral Assisted 1.5 Product and Maintenance Bridge | 2026-08-30*
