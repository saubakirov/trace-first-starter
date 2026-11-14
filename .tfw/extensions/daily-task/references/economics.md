# Daily economics: the lines a Daily record needs

The full contract is `.tfw/economics/README.md`; read it only for a case this page does not cover.
Provider binding details: `.tfw/economics/claude-code.md`, `antigravity.md`, or the README's Codex recipe.

## 1. Bind at start or resume

Find this worker's own source: Claude Code — the exact `<sessionId>.jsonl` under the runtime
`projects/` folder; Codex — the rollout whose `session_meta.id` is this unit. Never pick the newest
file. Note the start line: 0 when the session starts with this request; when a new session resumes
the record, its own source starts at revision 1 from the line where this record's work begins.
Add the binding block to the record file before the first `receive`; `receive` refuses without it:

```
<!-- tfw-economics-record-v1 {"schema_version":1,"id":"<folder ID>","project":"<project>","goal":"…","value":"…","created":"<offset time>","owner":"<owner ID>","result_state":"prepared"} -->
```

`id` equals the record folder name. IDs (`owner`, `--unit`, `--task`, `--source-id`,
`--source-version`) start with a letter or digit and use only `A-Za-z0-9_.:/-`: no spaces, no `@`.
Numeric receipt needs a resolved owner ID; if the owner is unknown, write `"owner":null`, collect
nothing and record a binding gap (§4). `result_state` follows the record: prepared, checked or accepted.

## 2. Capture, receive, report

```
python .tfw/economics/tfw_economics.py collect --provider claude.code-jsonl \
  --source <journal> --source-id <sessionId> --source-version <version number, e.g. 2.1.302> \
  --project <project> --task <folder ID> --owner <owner ID> --role daily --unit <worker unit> \
  --timezone <+HH:MM> --start <line> --revision <n> --complete --out <temp>/tfw/<folder ID>/r<n>.jsonl
python .tfw/economics/tfw_economics.py receive --source <temp>/tfw/<folder ID>/r<n>.jsonl \
  --task-root <record folder> --project <project> --task <folder ID> \
  --expected-unit <worker unit> --record <record file with the binding block>
python .tfw/economics/tfw_economics.py report --task-root <record folder> \
  --record <record file> --project <project>
```

Codex uses `--provider codex.rollout` and its CLI version number. Add `--predecessor <previous
received file>` for a later revision of the same source. `--complete` means every line of the
captured prefix was read, not that the work is complete. Keep every received revision.

## 3. Write in the record

One line per revision: revision, line range, cutoff, sha256, total tokens with its split, and
"covers revisions 1–n−1, do not add". Work after the cutoff is an uncounted tail; say so once and
capture nothing for it.

## 4. When capture fails

- Source known, collection fails: run `failure` with the same flags plus `--code` and `--detail`,
  receive it, keep the last good revision and name the unmeasured attempted interval.
- No Python or helper: use an equivalent checked extractor, or write the exact cause and missing
  prerequisite in the record.
- Own source or owner unknown: add to the binding block
  `"binding_outcomes":[{"kind":"binding_unavailable","producer":"…","observed_at":"<offset time>","code":"…","detail":"…","known":{…},"unavailable":{"<field>":"<reason>"},"attempted_extraction":false,"last_good":null}]`.
  `unavailable` is non-empty; `last_good` is the sha256 of an already received numeric file, or null.

None of these blocks the product work.

## 5. Money

When the owner or project states a subscription and nobody asked for a money estimate, write
`Money not valued: subscription.` and look up no prices. If that is unknown, ask once or treat it as
unknown conditions. USD figures that `report` prints from the bundled `rates.json` are a dated API
reference, not a bill, and need no lookup.

When money is valued, follow the README section on quotes: exact-model quote under 30 days old,
official lookup with `quote-store` and `quote-select --task-root <record folder>`, named valuation
kind, conditional scenarios for unknown conditions, last known quote on a failed lookup.
