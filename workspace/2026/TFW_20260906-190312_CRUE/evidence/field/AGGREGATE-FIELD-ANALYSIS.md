# Aggregate field analysis — TFW_20260906-190312_CRUE / Phase A

This is the single ordered campaign ledger. Each row consumed exactly one approved slot; no row was
retried, resumed, forked, coached by another slot, or replayed. Allocation identities from the freeze
checkpoint are not used as updater identities. The complete secret-safe native final/action records
are in each linked `REPORT.md`; raw provider output remains inside the private subject runtime.

| Order | Slot | Actual field native identity | Start epoch | Exit | Timeout | Receiver result |
|---:|---|---|---:|---:|---|---|
| 1 | [`afd-claude`](afd-claude/REPORT.md) | session `4f310c1f-0e81-40d4-b215-ad1fd4a972be` | 1788814726.2930703 | 1 | false | STOPPED before update; field auth layout mismatch; receiver clean |
| 2 | [`afd-codex`](afd-codex/REPORT.md) | thread `01a07dab-9585-70e3-a56c-19c8e0667bc6` | 1788814790.039786 | 0 | false | STOPPED before workflow read; `bwrap` unavailable; receiver clean |
| 3 | [`helpdesk-claude`](helpdesk-claude/REPORT.md) | session `53f5733c-2935-4c2b-a0d3-d22b4c77fc79` | 1788814861.8875966 | 0 | false | End-to-end/partial result reported; independently reconciled, 102 status lines |
| 4 | [`helpdesk-codex`](helpdesk-codex/REPORT.md) | thread `01a07db6-c2d3-7f33-a0fc-6c4f60a0d79f` | 1788815518.8463671 | 0 | false | STOPPED before workflow read; `bwrap` unavailable; receiver clean |
| 5 | [`atamat-claude`](atamat-claude/REPORT.md) | session `476b68dc-7d21-4fbf-9b51-fe3860a9f9da` | 1788815599.5637717 | 0 | false | PARTIALLY COMPLETE reported; independently reconciled, 89 status lines |
| 6 | [`atamat-codex`](atamat-codex/REPORT.md) | thread `01a07dc1-0dff-77d1-a197-df3cbc660681` | 1788816193.515642 | 0 | false | STOPPED before workflow read; `bwrap` unavailable; receiver clean |

## Independently reconciled receiver state

- All six copies still resolve `.tfw/.upstream` to Candidate `d6d26003972f7b18fe10d492960d0cbac9f0a3e8`.
- AFD Claude/Codex remain `.tfw/VERSION=2.1.0`, receiver Git clean, no receipts.
- helpdesk Claude is `.tfw/VERSION=3.0.0`, config `tfw.version=3.0.0`, source d6, 102 status lines,
  two receipts, and 11 Claude plus 11 legacy command copies. The self-reported semantic actions and
  checks remain subject to independent Reviewer verification of exact paths/content.
- helpdesk Codex remains `.tfw/VERSION=2.1.0`, Git clean, no receipts.
- Atamat Claude is `.tfw/VERSION=3.0.0`, config `tfw.version=3.0.0`, source d6, 89 status lines,
  two receipts, and 11 Claude plus 11 legacy command copies. `installed_from` has no 40-hex Candidate
  SHA because the Candidate is untagged; this is not a release-success claim.
- Atamat Codex remains `.tfw/VERSION=2.0.0`, Git clean, no receipts.

## Cross-slot findings

The two Codex stops are the same pre-update harness limitation: the receiver-local command sandbox
cannot start because `bwrap` is unavailable. They are not product-update failures and cannot be
reported as successful or failed migrations. AFD Claude is a distinct pre-update auth-layout failure:
its field auth volume exposed the credential at `/run/tfw/auth/.credentials.json` while the frozen
field launcher used `CLAUDE_CONFIG_DIR=/run/tfw/auth/claude`; the provider returned `Not logged in`.
No consumed slot was changed or retried, and this does not establish a Claude product defect.

Claude helpdesk and Atamat produced actual final reports and receiver changes, but the reports are
agent self-reports for semantic claims. Independent state reconciliation confirms version/source/
receipt/status metadata only. Configured project checks were honest non-success outcomes: helpdesk
reported `make lint`/`make test-unit` blocked by missing `ruff`/`pytest`; Atamat reported placeholders
and a removed `build.verify` target as unavailable. The exact project command contract is
[`PROJECT-CHECK-SET__20260908.md`](../harness/PROJECT-CHECK-SET__20260908.md).

AC-8 is not auto-PASS: four rows stopped before updater behavior and two rows need Reviewer-level
verification of semantic effects. AC-9 remains pending one bounded root comprehension request and the
single consolidated correction package. The observed `RELEASE.md` applicability gap was corrected in
final Candidate `4499e8c905eab91fa96c137ac2bc2813153e1fa1`; the causal audit then applied the settled
provenance/briefing corrections and exact-copy sync in final Candidate
`64a963517eca0b0a37aca9f73801eb7fd4366a28`. No field row was rerun.

## AC2/5/6/7/9 factual dispositions

- **AC-2 — routine discovery and questions:** both successful Claude final reports say no material
  question was asked. That is an observed agent report, not independent proof that every owner decision
  was correctly classified. The Atamat text names a project owner/operator; that identity is not an
  independently supplied owner fact and is not promoted here.
- **AC-5 — adapter parity:** independent reconciliation confirms 11 `.claude/commands/tfw-*` and 11
  legacy `.agent/workflows/tfw-*` files in both changed Claude receivers. Full byte parity, plural
  `.agents` adoption and Codex surface behavior remain agent-reported or unverified; Atamat explicitly
  declined plural `.agents` and a Codex marker as owner decisions.
- **AC-6 — outcome communication:** two real Claude final reports and all four stopped-provider final
  reports are preserved in the six linked reports. They contain actual limitations and next actions.
  No bounded owner comprehension answer has been collected yet.
- **AC-7 — local assurance/release contract:** the post-field correction package changed root `RELEASE.md`
  §§5–7, clarified untagged-Candidate provenance in the update workflow, restored owner-language briefing
  guidance, and synchronized the existing update copies. Targeted regression passes `11`; the final full
  suite passes `540` with `1` historical skip; `git diff --check` passes. Receiver project checks remain
  blocked/placeholder as reported by the agents.
- **AC-9 — aggregate evaluation/correction:** this file plus the six exact secret-safe reports is the
  one aggregate package. The RELEASE.md correction is the one ruling-bound correction. A root-level
  comprehension request is pending; it was issued from translated fragments rather than full native
  finals/BRIEFING and therefore is not a comprehension result. Independent Reviewer verdict remains
  required; no auto-PASS is valid.

## Receipt/briefing contradictions

The helpdesk briefing exists at `.tfw/update_receipts/BRIEFING__20260907-210839__ee08.md`, length
6782 bytes, SHA-256 `7fe9964fb215d2e1ac9cba287be74c27dd5babe11e485b061da7855190027d99`; its actual
Russian outcome-led text was read directly and the path/hash are added to that slot report. Atamat's
final text claims a separate briefing path, but independent receiver listing found only its UPDATE
receipt (SHA-256 `ae25d24412d0f54b5f01941f6051c722be9215675db175ae3509b1e066451f4e`). This is a
path/evidence discrepancy, not proof that an owner-facing message was absent; the native final and
receipt delivery state remain Reviewer inputs. Helpdesk's exact `installed_from` SHA and Atamat's
intentionally unadvanced `installed_from` are a reported provenance deviation against the settled
source rule for an applied untagged Candidate; neither receiver is treated as a release identity.
