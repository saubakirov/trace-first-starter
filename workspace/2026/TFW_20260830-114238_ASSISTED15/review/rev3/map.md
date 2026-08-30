# Map — "What was done?" (revision 3)
> **Mindset:** Experienced newcomer. Understand the terminal corrected result before judging it.
> **Test:** "Can I explain the complete current result without relying on either prior verdict or the Executor's self-test?"
> RF: [RF — TFW_20260830-114238_ASSISTED15](../../RF__TFW_20260830-114238_ASSISTED15.md)
> TS: [TS — TFW_20260830-114238_ASSISTED15](../../TS__TFW_20260830-114238_ASSISTED15.md)
> Historical verdicts: [first pass — REVISE](../../REVIEW__TFW_20260830-114238_ASSISTED15.md); [revision 2 — REVISE](../../REVIEW__TFW_20260830-114238_ASSISTED15__rev2.md)

## Understanding

The complete terminal result remains a Russian-authoritative, standalone Assisted 1.5 confined to the frozen 35-product-path boundary under `editions/`: 25 additions, seven modifications and three stock-hook deletions. It combines five manual lifecycle role skills, a fail-closed local identity mechanism, neutral offline templates, public-only release history, and an asymmetric maintenance bridge. Verified public stock may update a clean downstream Assisted core while protected downstream content is preserved; downstream learning may return only as a confined privacy-safe candidate requiring independent review. The real P6 Innoforce tree is evidence input only and must remain read-only.

The first review's D1–D8 were independently closed in revision 2. Revision 2 then found two additional defects in the maintenance boundary: D9, where the claimed project lock was scoped by a unique operation directory and therefore could not serialize two operations for the same target, and D10, where identity code could inspect/read persistent registry state before its first operation-time full-chain and private owner/ACL reprobe.

The same Executor's terminal correction changes six existing approved product files in `afef18a` without adding product paths. The declared D9 design now derives a stable private target-keyed lock outside the operation directory, acquires it before operation-directory creation, baseline capture, staging or target mutation, makes same-target operations share one key, and leaves different targets independent. The declared D10 design now re-probes the full pinned namespace chain plus private owner/ACL before any registry/lock exists, type or read access, performs registry reads under a validated live lock, and fails namespace substitution before the first read with zero substituted reads and zero persistent writes.

Evidence/RF commit `640fad5` refreshes 14 task-local files for those corrections. Terminal attestation commit `1aa6e97` updates exactly five task-local evidence/RF files so the claimed dual audit includes that follow-up itself. The current RF reports 4,035 product lines, manifest SHA-256 `f09603aaa60af68fe8e21cc3d14215f6a7bf64486e09dd2e966d779a793c66ea`, unchanged policy SHA-256 `2caf8bba83ac4018f4cde1d38964cb91645bb1637d6a9f866fed97a083d64b07`, two clean V1–V12 evidence runs and 47 current evidence attachments. These are mapped claims, not review conclusions.

## TS ↔ RF Alignment

| TS requirement | Terminal RF claim | Aligned? |
|----------------|-------------------|----------|
| AC-1 — release boundary, standalone package, truthful version and 35-path/4,800-line ceiling | RF §§1, 3, 4 claims one uninitialized `1.5`, exactly 35 product paths, 4,035 product lines and a 21-commit task-attributed zero-forbidden audit despite concurrent external work | claimed |
| AC-2 — portable acyclic manifest/policy and exact hook retirement | RF §§2–4 claims exact regenerated payload equality, hostile omitted/extra/self/nonregular rejection, separate manifest authority and exact three-hook retirement | claimed |
| AC-3 — forward preflight, stable project serialization, race stop and honest partial/recovery history | RF §§2–4 claims a private stable target-keyed lock acquired before operation state, complete destination baseline and staging; same-target contention; pinned source/target/operation/stage chains; zero-write hostile rejection; immutable partial and linked recovery | claimed |
| AC-4 — complete five-skill lifecycle and reusable independent roles | RF §§1–5 claims complete manual contracts, a deterministic seven-scenario role matrix, one Coordinator, the same Executor across corrections and this same independent Reviewer across full reruns | claimed |
| AC-5 — installed-state and customization preservation | RF §§2–4 claims protected project/work/people/knowledge/template/overlay/unknown/`.codex`/Full bytes and next-source readiness | claimed |
| AC-6 — reverse privacy, asymmetric authority and P6 field treatment | RF §§2–4 claims closed terminal+journal provenance, outside-root confinement, byte-identical secret-different candidates, no public mutation and field-source read-only treatment | claimed |
| AC-7 — identity semantics and zero-write fallback | RF §§2–4 claims clean documented command execution, cardinality/surname/collision coverage, Assisted-only state and zero-write unsafe fallback | claimed |
| AC-8 — operation-time locality and race defense | RF §§2–4 claims a full created-chain pin, Windows owner/ACL proof before persistent access, validated live-lock reads, permissive-ACL/substitution/reparse rejection and zero-read/zero-write first-access failure | claimed |
| AC-9 — useful neutral offline templates | RF §§1–4 claims complete worked templates, restricted TI1, header-free blocked-network output and 20 replacement visual inspections | claimed |
| AC-10 — public neutrality and product-wide agreement | RF §§2–4 claims cross-file path/version/lifecycle/identity/template agreement and zero organization/person/path/brand/private-history residue | claimed |
| AC-11 — complete deterministic V1–V12 matrix | RF §§3–5 claims two clean V1–V12, identity and template runs, deterministic evidence summaries, task schema checks, real contention and hostile correction cases | claimed |
| AC-12 — both maintenance directions, source immutability and no publication | RF §§2–5 claims maintainable P2 forward, confined candidate-only reverse, equal P6 field pre/post rows and digests under both aggregate orders, and no push/tag; terminal Reviewer acceptance remains deferred | claimed |

“Aligned” means only that the RF addresses each frozen TS criterion. Verify revision 3 must independently re-establish every item from the actual implementation and evidence; it must not inherit D1–D8 closure or accept D9/D10 from assertions.

## Deviations from TS

No frozen-contract amendment, new product path, or boundary expansion is declared. Commit `afef18a` modifies these six existing product paths only:

- `editions/02-assisted/.agents/skills/tfw-identity/SKILL.md`
- `editions/02-assisted/.agents/skills/tfw-identity/scripts/tfw_identity.py`
- `editions/02-assisted/.agents/skills/tfw-update/SKILL.md`
- `editions/ASSISTED_MAINTENANCE.md`
- `editions/maintenance/assisted_maintenance.py`
- `editions/maintenance/release-manifest.json`

The original ONB topology refinements remain the only approved affected-file clarifications: maintainer tooling lives under `editions/maintenance/`, and the neutral mark lives at `editions/02-assisted/шаблоны/assets/tfw-mark.svg`. Neither refinement changes the frozen product count or claim.

EV currently marks E1–E11 verified and E12 deferred for terminal acceptance by this same Reviewer. In revision 3, E4 must still be reopened against the actual one-Coordinator → same-Executor → one-Reviewer lineage and full independent rerun; E12 may close only after both P2/reverse directions, P6 source immutability, semantic privacy and no-publication are independently accepted.

Concurrent external work currently modifies root `.gitignore`, `KNOWLEDGE.md`, `TECH_DEBT.md`, TFW-55 and TFW-60 paths. Those changes are unrelated and must remain untouched. Verify must therefore keep two explicit views: the literal repository-wide baseline difference and the task-attributed 21-commit audit. The latter must prove that every Assisted task commit has zero forbidden product paths while the former truthfully identifies external changes rather than attributing them to this task.

The first-pass and revision-2 maps, verification traces, judgments and formal REVISE artifacts remain immutable history. This pass writes only under `review/rev3/` and, after Judge, a distinct revision-3 formal REVIEW. Root `KNOWLEDGE.md`, `TECH_DEBT.md`, `.tfw/` and root guides remain outside the frozen product boundary.

## Mandatory Verify Focus

- Re-enumerate and inspect all 35 product paths and all 47 current evidence attachments/citations, including actual implementation rather than RF summaries.
- Independently reproduce real two-process same-target contention: identical stable lock key, loser blocked before operation-directory creation and zero target/product writes; prove different-target independence.
- Independently instrument first-access ordering for identity: full-chain and owner/ACL reprobe before any registry/lock exists/type/read; substitution before the first read must yield zero substituted reads and zero persistent writes.
- Reopen D1–D8, V1–V12, manifest/policy hashes, hook retirement, protected-state behavior, semantic neutrality/privacy, deterministic seven-scenario roles and all render/visual artifacts.
- Perform both global and task-attributed audits, verify the claimed 21 Assisted commits, and separate concurrent external paths.
- Recompute P6 pre/post row equality and canonical digests without writing to `H:`; confirm both maintenance directions and absence of publication, push or tag.

## Checkpoint

**Self-check:**
- [x] Read the terminal RF §1–§5 and current EV completely?
- [x] Read all TS acceptance criteria and map each to the terminal RF without treating a claim as proof?
- [x] Read the master HL at frozen Contract Baseline `ee09a8a` and preserve its product boundary and design philosophy?
- [x] Read ONB and confirm its blocking answers precede implementation?
- [x] Read both historical REVISE artifacts and map D1–D10 to the current claimed correction surface?
- [x] Identify the current 47-file evidence attachment set and the unrelated dirty paths that must remain untouched?

Stage complete: YES
