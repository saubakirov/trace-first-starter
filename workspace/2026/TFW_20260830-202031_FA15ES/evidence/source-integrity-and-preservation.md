# Source integrity and preservation — TFW_20260830-202031_FA15ES

> Date: 2026-09-02
> Executor branch: `codex/tfw-fa15es-executor`
> Frozen Coordinator base: `c7300aa184375f9206bf0762df09165b6aa72aed`
> Execution-start commit: `e5e20f5b1070f48740d7d47bdd264ccc66ee524d`
> Product commit: `626d77b5c3261dff493d15c7ce5862b9e036d10e`

## Source boundary and immutability

The field 1.6 source was addressed only through the executor-provided `TFW_FA15ES_SOURCE` environment variable. Its absolute internal locator is intentionally not repeated in evidence. No source path or sibling path was ever passed to a write, move, delete, archive, staging, or commit operation.

| Observation | Files | Bytes | Aggregate SHA-256 / result |
|---|---:|---:|---|
| Frozen research manifest before execution (`research/iter3/3_extract.md`) | 28 | 297,522 | all source hashes computed read-only; private per-record hashes withheld |
| Executor prewrite census | 28 | 297,522 | all 23 non-private size/hash baselines matched; no reparse points |
| Full aggregate during pre-commit verification | 28 | 297,522 | `5c609354c68e8043b121b75ee4ad4a5ced70908462ed3f1ba2c82c03b3195bf2` |
| Full aggregate after product commit | 28 | 297,522 | `5c609354c68e8043b121b75ee4ad4a5ced70908462ed3f1ba2c82c03b3195bf2` |
| Source write targets observed | — | — | **0** |

Evidence limitation: the executor's first local prewrite record stored the complete count/byte census and the 23 non-private hashes, while the private-inclusive aggregate digest was first persisted at pre-commit verification. The frozen research manifest is therefore the pre-implementation authority for the complete 28-file set. Two executor aggregate reads around the final commit are identical, and the source was never a write target.

## Complete 35-disposition census

The row-level ledger is frozen in [ONB §2.1](../ONB__TFW_20260830-202031_FA15ES.md#21-complete-35-disposition-ledger). It was recounted independently after implementation:

| ONB rows | Disposition | Responsibilities | Repository writes |
|---|---|---:|---:|
| 1, 3, 5, 7, 9, 22 | exact source copy | 6 | 6 modified |
| 2, 4, 6, 8, 10–13, 18, 20–21, 24–28 | bounded source adaptation excluding relocation | 16 | 16 modified |
| 14–17, 23 | private/company exclusion | 5 | 0 |
| 19 | `people/README.md` → `team/README.md` relocation plus bounded adaptation | 1 | 1 added + 1 deleted |
| 29 | retain neutral mark byte-for-byte | 1 | 0 |
| 30–33 | delete rejected theme/static-maintenance paths | 4 | 4 deleted |
| 34–35 | repository routing documents | 2 | 2 modified |
| **Total** |  | **35** | **1 added + 24 modified + 5 deleted = 30 changed paths** |

No 31st product path was created. All product changes are under `editions/`; Full, root TFW files, `.tfw/`, other editions, and unrelated task state are unchanged by the product commit.

## Immutable-source diff audit

Comparison method: UTF-8 source text against final target text, zero context and zero inter-hunk context, with the relocation mapped from source `people/README.md` to target `team/README.md`.

| Source responsibility | Hunks | Allowed changed source lines |
|---|---:|---:|
| five lifecycle/identity skill files | 22 | 31 |
| `AGENTS.md` | 13 | 15 |
| `CHANGELOG.md` | 28 | 45 |
| `knowledge/INDEX.md` | 2 | 11 |
| `MIGRATION.md` | 20 | 27 |
| relocated participant contract | 4 | 4 |
| `PROJECT.md` | 9 | 22 |
| package `README.md` | 10 | 12 |
| `шаблоны/build_a4.py` | 4 | 5 |
| three Markdown templates | 7 | 7 |
| `шаблоны/презентация.html` | 17 | 26 |
| **Total: 17 adapted files** | **136** | **205** |

The 17 adapted files contain 2,105 source lines. Exactly 1,900 lines remain outside the allowlist and match source bytes. The source-derived blank line at presentation source line 168 contains inherited trailing spaces; it is outside the allowlist and was deliberately preserved. This is the sole `git diff --check` finding and is not an executor-added hunk.

## Exact-copy and retained-asset hashes

| Path | Bytes | SHA-256 | Source match |
|---|---:|---|---|
| `.agents/skills/tfw-handoff/agents/openai.yaml` | 378 | `0516336e97d63cf315ddbcef5af0394c17a237d289e914f56df94df926ee4fd9` | yes |
| `.agents/skills/tfw-identity/agents/openai.yaml` | 547 | `cd2acda1961bbaf9ba3e598fe8b5361da7c62c1415cb5ea2ff66b562974e9978` | yes |
| `.agents/skills/tfw-plan/agents/openai.yaml` | 330 | `9d1f968f1eaea9f5e12e1cb631357c71d029d3a988804576075ea7fe2ccaa950` | yes |
| `.agents/skills/tfw-review/agents/openai.yaml` | 344 | `a7db8ffe61ad5b002160750a774466d194775cb0fff6aea3a48608168a71e624` | yes |
| `.agents/skills/tfw-update/agents/openai.yaml` | 454 | `f17f189f8facb6859da3971585630c492281014831d116c48fbe17f0ad9741a5` | yes |
| `VERSION` | 4 | `e5cd57eee9635f3612a2a913746f7f794cdb573cc3e16f6b7d8e613f92beac83` | yes |
| `шаблоны/assets/tfw-mark.svg` | 270 | `1ed6d908154678edddf9c1b3ca4c58b9bf813b46b3864d1db0d1be34c9893e11` | retained target baseline |

## Product and budget metrics

| Metric | Before | Final | Delta |
|---|---:|---:|---:|
| Assisted package files | 26 | 24 | -2 |
| Assisted package bytes | 91,299 | 260,872 | +169,573 |
| Bytes across the 30 changed paths | 106,350 | 271,785 | +165,435 |
| Product LOC | — | +1,917 / -853 | 2,770 changed |

The 2,770 changed-line total is below the frozen 5,000 LOC ceiling. The final package contains exactly 24 files, and relative-link verification checked 9 links with 0 broken.

## Reproduction

Run from the repository root with the field source supplied out of band:

```powershell
$env:TFW_FA15ES_SOURCE = '<approved read-only source>'
python workspace/2026/TFW_20260830-202031_FA15ES/evidence/attachments/verify_assisted.py
```

Expected terminal line: `VERDICT=PASS`.
