# Daily economics — 20260929-104929_claude-subagent-economics

Combined view of the numeric files returned to `economics/`, reconciled and summed by the
landed helper's own `reconcile` and `summarize` (collector `tfw-economics/1.1`, master
`8cd05ecb` or later). A Daily has no `status.md`, which the helper's task report command
requires, so this page is built from the same functions and no status was invented.

## By unit

| Unit | Scope | Range | Cutoff +05:00 | Tokens | Cached input | Output | Priced USD | Unpriced tokens |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Antigravity | its whole conversation at capture (task.md §13) | 0–136, complete | 12:00 | 17,583,859 | 15,433,174 | 109,212 | 3.10 | 0 |
| Claude Code, Daily worker | this Daily's whole session, from 10:32 | 0–1116 | 12:05 | 38,813,129 | 38,015,055 | 270,862 | 16.48 | 1,020,183 |
| Codex diagnostic subagent | created for this Daily (task.md §6) | 0–269 | 12:03 | 1,836,698 | 1,747,968 | 18,092 | 0.00 | 1,836,698 |
| Codex chat, TEQM Coordinator | whole saved chat history since 2026-09-28, TEQM included | 0–5211 | 12:02 | 90,099,337 | 86,493,184 | 521,772 | 125.53 | 0 |

## Totals

| Selection | Tokens | Priced USD | Unpriced tokens |
|---|---:|---:|---:|
| This Daily: Claude, Codex subagent, Antigravity | 58,233,686 | 19.58 | 2,856,881 |
| All returned files, with the whole Codex chat history | 148,333,023 | 145.12 | 2,856,881 |

## Time

Kinds are never added together.

- Antigravity: model generation 764 s
- Claude Code, Daily worker: no native duration in this source
- Codex diagnostic subagent: completed turn 454 s
- Codex chat, TEQM Coordinator: completed turn 22,097 s

## Coverage and limits

- Returned files: 4; measured units: 4; omitted: none; failure-only: none; excluded files: none.
- The Codex chat file covers the chat's whole saved history, including the TEQM task, so it
  is kept out of the Daily total, which is therefore a lower bound. Its Daily share needs a
  capture bounded from the Daily's first call in that chat.
- Antigravity declared its capture complete while its conversation was still active; each
  file is a snapshot, and consumption after its cutoff, this page included, is outside it.
- Antigravity rows carry no proved date, so date filters leave them out; totals keep them.
- USD is the Standard API reference on the 2026-09-29 rate card, not a subscription bill.
  `gpt-6-luna` and `claude-sonnet-5-5` have no rate there, so their tokens stay unpriced.

## Files

- `antigravity-coordinator-20260929-120043.jsonl` — SHA-256 `0bee10d61c5880437146e81216be2aa8fc902b8fa92982309f294f429d16c19e`
- `claude-code-worker-20260929-120546.jsonl` — SHA-256 `5529bd231d811008efb2c4457878272cb5e6d2cc36a278df651db60863df6347`
- `codex-probe-20260929-120342.jsonl` — SHA-256 `1c8cd4a8ef3c98049817e14260cab25611a36915681fa0b46aa76e02a9af7160`
- `codex-parent-20260929-120253.jsonl` — SHA-256 `1f44422395e8f1dc8694872cc4ea3de1c7277454e6eb2d98dbfd3f0adb69946b`
