# Antigravity source procedure

Use the common [economics contract](README.md) for Daily/Full checkpoints, identities
and failures. First identify the running surface; the following are distinct.

| Surface | Binding and support boundary |
|---|---|
| CLI `agy` 1.2.16 | Supported as `antigravity.cli` / `Antigravity-CLI-1.2.16`. Its invocation result/stream supplies the exact conversation UUID; the own runtime log identifies the app-data root. Observed root is the runtime user's `.gemini/antigravity-cli`, with `conversations/<UUID>.db`. Verify the actual runtime root and only that exact file. |
| Legacy IDE | `antigravity --version` can report the VS Code base, not IDE product version. Resolve the executable's `resources/app/product.json` and actual native conversation identity/root. Only the previously observed `antigravity.ide` / `Antigravity-IDE-2.17.0` mapping is supported; observed IDE 1.23.2/base 1.107.0 is not silently relabelled. |
| Desktop App | Installed package version 2.26.0 and outer runtime 44.4.3 are different axes. Desktop source location and decoding are not established by CLI/IDE data. Obtain exact own identity/store from this surface's runtime evidence; otherwise return the bounded missing facts. No generic Desktop decoder is claimed. |

A model can know its own UUID from runtime context before an outer result exists.
Verify that binding rather than reading another conversation or selecting the latest
DB. Child launch/return metadata supplies its own UUID and separate DB; bind that
child's actual unit. In one CLI 1.2.16 experiment the parent excluded its child;
declare actual inclusion and count each attributable invocation once. No formal
role label is needed to preserve an authorized helper's economics.

## Read only and preserve categories

The helper opens only the exact filename matching `--source-id`, takes one
read-only SQLite backup, and selects `gen_metadata.idx/data` (layout idx,data,size).
For the two named formats, outer protobuf field 1 contains usage field 4, model
field 19 and generation duration field 11. Usage fields 2/5/3/9/10 are fresh/cache/
output/thinking/content. Output must equal thinking + content. Missing proto3
counters beside reported ones are zero; a row with no counters is unmeasured.
Missing usage, changed model encoding or relations refuse extraction. CLI displayed
total excludes cache reads; TFW total includes them. Thinking is inside output,
never added twice. Generation duration is model time, not agent/envelope time.
No proved date join exists here: dates remain unknown. Private mappings are
observations at these versions, not compatibility promises for newer versions.

## One operation per continuation

Use common `collect` flags with the exact supported provider/version, DB and UUID,
task/unit identity, timezone, increasing revision and a new `--out` path.
`--start`/`--end` select `[idx,idx)` bounds; omitting end binds the snapshot's last
index plus one. `--complete` needs grounds for the selected range.

At the first capture, return validated JSONL and its hash/bounds/cutoff. On each
continuation, repeat `--prior` for every selected immutable disjoint fact, keep
`--start` at the original task boundary and use `--complete`. The helper checks
prior source/unit/task/version/offset/inclusion, every exported aggregate group
and event membership against the same snapshot, then writes only the new interval.
Its JSON result lists selected hashes and `current` cumulative token/duration
groups. Return those checked totals and all required bytes, not a sum of previous
cumulative reports. With no new events it returns `file:null` and the checked
current view; no empty receipt is invented. Preserve prior files unchanged.

This operation supports contiguous, positive measured events. Zero-only, missing,
unmeasured or noncontiguous prior/new membership refuses when proof is insufficient;
retain last-good facts and the exact error. Changed categories, model/date/effort,
duration/availability, membership or disposition refuse even if grand totals match.
Harmless nonnumeric changes can pass when exported groups and membership remain
equal; this is not per-event value immutability. `--prior` and `--predecessor` cannot
be combined. Existing covering successors still require identical raw-prefix
hashes; their digest meaning is unchanged. Native continuation can rewrite old
nonnumeric bytes, so a covering successor may correctly refuse while checked
disjoint collection works. Never relabel or rewrite a historical receipt.

## Failures and native execution

Record surface/version, runtime-root/identity evidence, exact locator checked and
actual command/tool result. Known locator, source denial, unsupported version and
missing binding are different facts; use the common exact gap/failure forms.
Native CLI SUCCESS/exit 0 may include denied actions: inspect them before claiming
self-capture. Observer extraction can preserve numeric evidence but cannot prove
the agent executed its own Daily/Full return. Use only granted command/file access;
do not loop denied actions or change persistent permissions. Unavailable Desktop
interaction remains a separate dependency; CLI success cannot satisfy it.
