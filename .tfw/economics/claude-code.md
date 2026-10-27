# Claude Code source procedure

Use this from the common [economics contract](README.md) at Daily/Full binding and
capture. It covers observed Code-tab/CLI JSONL, not ordinary Claude Desktop chat.

## Bind before collection

1. Record `claude --version` and this invocation's session ID, transcript location
   and task-start boundary from runtime metadata or its exact launch receipt.
   Existing hook metadata can expose `session_id`/`transcript_path`; child completion
   metadata distinguishes `agent_id`/`agent_transcript_path`. No new hook is required.
2. Resolve the process's configured root (`CLAUDE_CONFIG_DIR` when set, otherwise
   the runtime user's `.claude`); `claude auth status --json` reports config/projects
   directories on observed CLI 2.1.289 without reading credentials. Under `projects/`,
   find only the exact bound `<sessionId>.jsonl` filename, then verify its IDs.
   Do not infer the project-directory encoding or select the newest journal.
3. A child/background unit writes `<sessionId>/subagents/agent-<agentId>.jsonl`.
   Its lines repeat the parent sessionId; bind `--source-id <sessionId>/<agentId>`
   and the actual child unit. The parent's own source ID is `<sessionId>`.
   A parent's journal or inherited session ID alone is not the child's source.
4. Bind zero-based physical lines `[start,end)` at the task boundary. Continuations
   of this same task can use a verified covering successor. Reused/copied/forked
   sessions need native provenance separating inherited work and a verified bound;
   neither a new filename nor a title proves new consumption. In an observed 2.1.289
   fork, inherited message IDs persisted while sessionId was rewritten to the new ID;
   the exact parent/fork receipt and new response boundary excluded those old messages. The current reader
   refuses mixed session IDs even before `start` and response blocks spanning that
   boundary. Preserve that refusal and last-good data when attribution is ambiguous;
   do not filter away foreign IDs or prescribe empty chats as a universal fix.

## Capture and return

Run common `collect` flags with `--provider claude.code-jsonl`, the exact file,
source ID and observed version, task/unit identity, offset and proven line bounds.
Use a new output path and increasing revision each time; `--predecessor` names the
previous immutable file for a covering successor. Validate the bytes and return
hash, revision, bounds and cutoff at the common Daily/Full checkpoint. Keep earlier
files; overlapping snapshots are never added.

Each assistant message ID is one response. Repeated blocks keep maximum output
after input/cache consistency checks. Fresh input, cache read, five-minute and
one-hour writes remain separate; thinking is already inside output. Changed input
categories refuse collection. Native agent duration is unavailable, not a
five-minute-gap estimate. API error/synthetic messages are not measured inference;
an error-only bound refuses with that cause, preserving any valid prior capture.

One observed 2.1.281â€“2.1.284 parent shared no message ID with its separate children;
verify actual inclusion for the selected invocation, then use the common
`--includes-source` rule where necessary. This is not universal provider behavior.

## A bounded unsuccessful search

Record actual surface/version, runtime root checked, native identity evidence,
exact filename/child locator attempted and the observed absence, denial or format
error. Missing identity, denied source access and failed authentication are different
conditions. No unrelated conversation scan or credential read is needed. Follow
common finite outcomes: actual failure receipt for a known attempted bound, or
attributable pre-extraction gap for the exact missing fact. Available collection
remains owed; nonmeasurement does not satisfy a required native experiment.
