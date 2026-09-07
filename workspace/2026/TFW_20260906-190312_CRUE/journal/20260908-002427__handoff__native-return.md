---
time: 2026-09-08T00:24:27+05:00
kind: handoff
writer: robert
on_behalf_of: saubakirov
via: codex
from: ONB
to: RF
refs:
  - ONB__TFW_20260906-190312_CRUE.md
  - RF-TFW_20260906-190312_CRUE.md
  - evidence/EV__TFW_20260906-190312_CRUE.md
  - evidence/harness/NATIVE-EXECUTION__20260907.md
  - evidence/FIELD-MANIFEST.md
  - evidence/LOCAL-VERIFICATION.md
  - status.md
---

The bounded return is complete under the unchanged TS. The real HTTP CONNECT/native preflight used a
network-none non-root subject, a network-enabled exact-provider sidecar, official Claude 2.1.143 and
Codex 0.152.1 binaries, minimum private auth and a sanitized Candidate Git copy. Codex returned native
`PREFLIGHT_ONLY` through `chatgpt.com`; a direct `api.openai.com:443` CONNECT returned 403. Claude
opened `api.anthropic.com` tunnels but ended with a redacted JSON-parse/telemetry blocker and no final
response. **Pre-admission snapshot:** no field slot was admitted; the manifest was then NOT FROZEN with
zero slots and no `SOURCE-ADMISSION.md`. This paragraph is superseded by the current projection correction
below and is retained as a historical handoff fact.

The full local suite is `540 passed, 1 skipped in 554.60s`; AC-3 and AC-11 targeted assurance remains
`11 passed`. EV and RF are ready for the same independent Reviewer. The Executor does not write REVIEW.

## Current projection correction — 2026-09-08

The preceding handoff text is retained as the pre-admission/native-preflight snapshot. The current
field projection is superseded by the frozen source admission and field ledger: six rows were admitted
and consumed exactly once, so the campaign is `CONSUMED=6`; no row was retried and no second campaign is
authorized. Current RF/EV records supersede the old preflight counts: targeted assurance is `13 passed`,
the recorded full suite is `540 passed, 1 skipped`, and native semantic effects, owner comprehension,
independent REVIEW and knowledge closure remain nonterminal. The missing owner response is retained as
a comprehension-evidence limitation under AC-9, not as a new approval gate.
