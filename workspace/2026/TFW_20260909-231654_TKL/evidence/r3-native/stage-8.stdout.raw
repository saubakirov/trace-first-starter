---
kind: update_receipt
attempt_id: UPDATE__YYYYMMDD-HHMMSS__abcd
recorded_at: YYYY-MM-DDTHH:MM:SSZ
writer: <resolved handle or omit>
---

# Update Receipt — `{attempt_id}`

Immutable record of one update attempt. Append a new receipt for a later attempt; never rewrite an
older receipt. This record is evidence and history, not the receiver's state registry. Do not put
credentials, tokens, private keys, or other secrets here.

## 1. Pinned source and receiver

| Field | Value |
|---|---|
| Receiver root | `<absolute or repository-relative root>` |
| Receiver baseline | `<full SHA or explicit uncommitted state>` |
| Source ref | `<tag/branch/commit/path>` |
| Source full SHA | `<full SHA or N/A for non-Git source>` |
| Source provenance | `<official/package/local provenance>` |
| Target workflow read | `<exact path and revision>` |
| Attempt time | `<actual clock value>` |

## 2. Authority and semantic groups

State who authorized the attempt, which governing task or contract applies, and which connected
semantic groups were considered together. Do not infer authority from the source, version number,
machine identity, or a sibling lifecycle state.

| Question | Answer |
|---|---|
| Acting handle and role | `<answer or unresolved>` |
| Acceptance authority | `<human/owner/contract or unresolved>` |
| Governing task/phase | `<exact ID/path or N/A for an ordinary update>` |
| Groups inspected together | `<list exact groups/paths>` |
| Material questions | `<none, or question → answer/route>` |

## 3. Decision and effects

| Effect | Exact paths/groups | Decision | Reason and authority |
|---|---|---|---|
| Applied | `<paths>` | `<applied>` | `<why>` |
| Preserved | `<paths/legacy sources>` | `<preserved>` | `<why/how referenced>` |
| Skipped | `<paths/groups>` | `<skipped>` | `<why>` |
| Refused | `<paths/groups>` | `<refused>` | `<boundary/authority>` |

For each preserved project-purpose-bearing source, record the observed explicit purpose designation
and the exact preservation reference; a receipt records the observation and does not create current
Project North Star authority.

Record version equality as a re-observation only; equal versions do not prove completion. Preserve
legacy sources by content address or exact historical reference when their identity or purpose still
matters. Do not silently overwrite receiver state or split one semantic group across unrelated edits.

## 4. Verification

| Check | Result | Artifact or command |
|---|---|---|
| Source integrity and provenance | `VERIFIED / DEFERRED / BLOCKED / N/A` | `<ref>` |
| Receiver state/config exclusions | `VERIFIED / DEFERRED / BLOCKED / N/A` | `<ref>` |
| Connected-group consistency | `VERIFIED / DEFERRED / BLOCKED / N/A` | `<ref>` |
| Adapter/runtime surface | `VERIFIED / DEFERRED / BLOCKED / N/A` | `<ref>` |
| Maintainer checks | `VERIFIED / DEFERRED / BLOCKED / N/A` | `<ref>` |
| Receiver proof | `VERIFIED / DEFERRED / BLOCKED / N/A` | `<ref>` |

Explain every non-`VERIFIED` result. Link exact evidence; screenshots or summaries without a resolving
path do not prove the receiver state.

## 5. Cleanup, continuation, and final-message input

- Temporary files/worktrees removed or retained: `<exact paths and reason>`
- Cleanup resolution/disclosure observed before sealing: `<exact outcome or retained path>`
- Unresolved material items: `<none or list>`
- Next authoritative action: `<action and owner>`
- Final message delivery at receipt time: `planned/not-yet-observed`
- Final message inputs: `<render the outcome from this sealed receipt; do not claim future delivery or comprehension>`
- Attachments/evidence: `<exact paths>`
