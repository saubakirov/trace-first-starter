# Daily Task — 20261114-120711_daily-task-faster: faster and simpler Daily Task skill

## 1. Source and attribution

- Requester and acceptance authority: Vladimir Korzhov (git user `Vladimir Korzhov`), in this
  Claude Code VS Code session; upstream merge authority stays with the repository owner
  (`saubakirov`), who, by the requester's account, agreed to accept the MR.
- Worker: Claude Code 2.1.302 session `b9270daa-2608-437c-b607-350500e4178b`, model
  `claude-opus-5-5`, branch `daily-task-faster` (from upstream `master`, TFW 3.10.0 at `f06beceb`).
- Observed before the first product write: `2026-11-14T12:07:11+05:00`.
- Request (excerpt, translated): «Speed up and simplify the TFW Daily Task skill so a daily task is
  faster, cheaper in tokens and clearer to a model and a human … MR 1 without new scripts.»
  Measured by the requester's audit (2026-11-14): ~45 KB mandatory reading before work; five
  cumulative economics revisions in one record, each covering the previous ones.
- Related: none in `daily/` (search by `daily-task`, `economics`, `Daily` in recent records found
  no record changing the Daily skill itself).

## 2. Goal, Value and Boundaries

Goal: the Daily skill reads in one pass — when to use it, a short numbered path, stop conditions —
and pulls only the economics lines it needs from a small reference instead of the whole
economics README.

Value: less reading before every Daily run and fewer economics revisions per record, with every
existing gate kept.

Boundaries: change only `.tfw/extensions/daily-task/` (SKILL.md, new `references/economics.md`,
`templates/task.md`, `installation.md`, both entries), the two installed wrappers, and — in a
separate commit — the Daily cadence lines of `.tfw/economics/README.md`. No scripts, no Codex or
Antigravity profiles, no PR #5 branch. Commits after the requester's «ok»; push only on request
with `git push -u origin daily-task-faster`.

Completion oracle: every gate of the old SKILL.md maps to the new text; installation map lists the
new reference; wrappers are byte-equal to their sources; an independent subagent review of old vs
new text finds no lost gate; mandatory pre-work reading is measured.

## 3. Context before action

Inspected: `CLAUDE.md`, `.tfw/extensions/daily-task/{SKILL.md,installation.md,templates/task.md,entries/*}`,
`.claude/skills/tfw-daily-task/SKILL.md`, `.agents/skills/tfw-daily-task/`, `.tfw/economics/README.md`
(Daily, commands and price sections), `.tfw/economics/claude-code.md`, helper argument parser,
`C:\projects\transcard-migration\daily\2026\20261106-092446_conciseness-audit\task.md` (economics part).
North Star fit: less ceremony per purpose, same evidence and authority.
No active formal task owns these files.

## 4. Result, decisions and check

Products (two commits): `.tfw/extensions/daily-task/{SKILL.md,references/economics.md,templates/task.md,installation.md,entries/*/SKILL.md}`,
`.claude/skills/tfw-daily-task/SKILL.md`, `.agents/skills/tfw-daily-task/SKILL.md`, `docs/scripts/gen_docs.py`,
`.tfw/CHANGELOG.md`; commit 2 adds the cadence change in `.tfw/economics/README.md`, `.tfw/conventions.md`,
`.tfw/README.md`, `.tfw/workflows/economics.md`, `.claude/commands/tfw-economics.md`.

Decisions (2026-11-14):
- Cadence (commit 2), requester's choice A: capture at close, interruption and handover only. The
  review's gap (a result awaiting acceptance when nobody returns) is covered by a later capture from
  the preserved session journal by whoever returns to or closes the record.
- `references/economics.md` is 4.1 KB, over the 1–2 KB target: the three exact commands and the ID
  format rules the helper enforces take most of it; quote details point to the README.
- Record size guidance ("about one screen plus links") added to SKILL.md and the template after the
  A/B test showed records did not shrink.

Checks:
- Commands in `references/economics.md` run on this record: `collect` → `receive` → `report` succeed.
- Mandatory reading before work: 45,382 B → 13,972 B (−69 %) (wrapper, SKILL.md, reference, template).
- Wrappers byte-equal to entry sources (sha256 compared); `pytest tools/tests/ docs/scripts/`: 14 passed.
- Independent subagent review (old vs new text, no conclusions given): 53 skill rules + 9 template
  rules mapped; LOST/WEAKENED items and helper mismatches (version string, null owner, `id`, `last_good`)
  fixed; three contradictions in `conventions.md`, `.tfw/README.md`, `workflows/economics.md` fixed in commit 2.

- A/B test in `transcard-migration` (4 detached worktrees of `main` `20277f2`, headless `claude -p`,
  same task «README section: what blocks Ф1», 2 runs per variant, turn 2 «ок, принято»):

  | | old-1 | old-2 | new-1 | new-2 |
  |---|---|---|---|---|
  | Turn 1 (work) | 81 s, 17 turns | 102 s, 25 | 104 s, 22 | 115 s, 25 |
  | Context per call, turn 1 | 57 k | 55 k | 50.5 k | 53 k |
  | Turn 2 (close) | 11 s, 5 | 9 s, 3 | 56 s, 12 | 43 s, 11 |
  | Economics capture | none | none | 1 revision | 1 revision |
  | Record | 5.9 KB | 6.4 KB | 6.9 KB | 6.4 KB |

  Observed: context per call ~8 % smaller; work time within run-to-run spread, no speed gain shown;
  old runs skipped their required capture, new runs completed it from the reference. A first test
  run was invalid (shell commands denied: headless used PowerShell) and was discarded.

State: accepted for commit by the requester («Добавь строку и переходим к коммиту», 2026-11-14);
merge into upstream is the repository owner's decision.

### Economics

Source: `~/.claude/projects/c--projects-trace-first-starter/b9270daa-2608-437c-b607-350500e4178b.jsonl`,
provider `claude.code-jsonl`, Claude Code 2.1.302; the session starts with this request, boundary line 0.
Money not valued: subscription.

Revision 2 (covers revision 1, do not add): lines `[0, 431)`, `--complete`, cutoff 2026-11-14T07:18:52Z,
sha256 `bdb5392d7b7166e9a7c9e89b836f2363e9af9447ce2d47e55c1d798238a75cee`; model `claude-opus-5-5`, 51 responses:
5,237,500 tokens — cache read 5,087,833, cache write 1 h 112,551, fresh 108, output 37,008 (reasoning 12,097).
Revision 3, final (covers revisions 1–2, do not add): lines `[0, 753)`, `--complete`, cutoff
2026-11-14T07:58:25Z, sha256 `d17eec6668d3295b2eed6d454db30a334cbf6c3b24c18794e1d53dd50fce3e5a`; 98 responses:
13,359,953 tokens — cache read 13,109,526, cache write 1 h 175,036, fresh 226, output 75,165 (reasoning 23,687).
Tail after the cutoff (this line, commits, MR description) uncounted.

Review subagent, own source `b9270daa-2608-437c-b607-350500e4178b/a9cdb772901d13b21`, revision 1: lines `[0, 92)`,
`--complete`, cutoff 2026-11-14T07:57:47Z, sha256 `a8e01a85eed9b0b71c6f3762c7eff95be572719f2152e8c9ccc3a3b562e41128`:
1,273,049 tokens — cache read 1,168,699, cache write 5 min 86,193, fresh 40, output 18,117 (reasoning 6,643).

A/B test sessions (8 headless runs in `C:\projects\worktree\td-*`) are not captured with `collect`;
their CLI JSON reports ~12.3 M cache-read tokens in total (first invalid run 5.4 M, second 6.9 M).

<!-- tfw-economics-record-v1 {"schema_version":1,"id":"20261114-120711_daily-task-faster","project":"trace-first-starter","goal":"Daily Task skill readable in one pass with a small economics reference","value":"Less pre-work reading and fewer economics revisions per Daily record, gates kept","created":"2026-11-14T12:07:11+05:00","owner":"vkorzhov","result_state":"accepted"} -->

## 5. Next or close

Closed for commit 2026-11-14. Next, requester's: push with `git push -u origin daily-task-faster` on request, then the MR.
