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
response. No field slot was admitted; manifest remains NOT FROZEN with zero slots and no
`SOURCE-ADMISSION.md`.

The full local suite is `540 passed, 1 skipped in 554.60s`; AC-3 and AC-11 targeted assurance remains
`11 passed`. EV and RF are ready for the same independent Reviewer. The Executor does not write REVIEW.
