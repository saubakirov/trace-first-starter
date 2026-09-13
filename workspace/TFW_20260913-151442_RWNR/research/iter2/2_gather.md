# Gather — Iteration 2: evidence needed for a safe retirement

> **Mindset:** Explorer. Keep alternatives open while fixing the observable facts.
> Parent: [HL-TFW_20260913-151442_RWNR](../../HL-TFW_20260913-151442_RWNR.md)
> Goal: decide whether Resume can be retired without loss of lifecycle safety, trace integrity, or a discoverable recovery path.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1: general return-state inspection | Keep Resume as the inspector | Add a pure pre-route gate to Plan | Repeat guards in each lifecycle workflow | Add another internal dispatcher |
| D2: close/recovery access | Resume owns access | Plan performs close/recovery | Plan names the existing direct conventions contract and stops | Add a new public recovery command |
| D3: stale receiver handling | Manifest omission only | Delete every matching path | Delete only a version-proved framework-owned path and refuse drift | Leave a permanent tombstone |
| D4: history preservation | Require whole-file identity for every historical hit | Allow all history files to change | Split immutable task traces from additive aggregates | Search candidate text for retired terms only |
| D5: instruction accounting | Preserve the unexplained 2,685 number | Use a named byte/text counter on both sides | Count only Plan after retirement | Count every live documentation translation and generated copy |
| D6: Plan's size breach | Ignore the existing breach | Permit net growth below the combined baseline | Reduce Plan itself to the 1,200-word design cap | Extract a continuation helper |

## Findings

### G1: Resume currently supplies pre-route guards that Plan does not

At immutable baseline `a2363fd07253ca92410db149b4301432de79be3b`, `.tfw/workflows/resume.md` resolves exact references through the active-plus-historical union, refuses collisions, stops historical-only references read-only, reads each phase's local state, preserves REVIEW dispositions, asks for phase choice, and recognizes a selected close/recovery request. `.tfw/workflows/plan.md` has none of those pre-route clauses. It begins an existing task with its own status/journal read, then enters the Knowledge Gate and planning algorithm.

The shared state vocabulary supplies the finite cases a candidate gate must cover: `TODO`, `HL_DRAFT`, `RES`, `PHASES`, `TS_DRAFT`, `ONB`, `RF`, `REV`, `KNW`, `DONE`, `BLOCKED`, `REJECTED`, plus verbatim `UNDECLARED`. `PHASES` is not a rollup: every selected or matrix row must use the phase-local `status.md` and `journal/`. An absent, malformed, colliding, or contradictory carrier cannot be normalized by a router.

The relevant product owners already exist:

| Observed state/result | Existing canonical owner |
|---|---|
| new task, `TODO`, `HL_DRAFT`, unapproved `TS_DRAFT`, ruled REVISE | Plan / Coordinator |
| `RES` | Research / Researcher |
| approved `TS_DRAFT`, `ONB` | Handoff / Executor |
| `RF`, incomplete `REV` | Review / Reviewer |
| APPROVE recorded while the carrier is still `REV`, `KNW`, selected close/record repair | `conventions.md` → `Closing and record recovery` / Coordinator |
| `PHASES` without a selected phase | phase-state matrix and human choice; no product workflow starts |
| `BLOCKED`, `UNDECLARED`, malformed/collision, `DONE`, `REJECTED`, historical-only | report the exact condition, owner, or terminal state and stop |

Thus the missing behavior is inspection and navigation, not an unowned product transition. Any candidate still has to prove that its pre-route gate occurs before the Knowledge Gate and before every Plan write.

### G2: close/recovery already has an exact direct address and authority chain

The unique canonical address is `.tfw/conventions.md` → `Closing and record recovery`. Its first paragraph says the authorized Coordinator uses the contract directly; Resume merely also exposes it. The contract itself, rather than Resume or Plan, owns both controlled effects:

- **Close:** start from the selected state/journal, governing authority and live REVIEW; rule dispositions; run applicable Docs/Knowledge through their existing owners; recheck changed final claims with the separate Reviewer; verify landing/final effects and carriers; only then write `DONE` and the actual transition event.
- **Record repair:** reconstruct unchanged accepted result, oracle, authority, lineage and dependencies; repair only the current carrier; preserve old event bytes; append only a truthful current act; validate and stop. It cannot create product work, a review round, capture cycle, or inferred past event.

The forward authority chain is explicit in `.tfw/workflows/review.md` Steps 6–7: a Reviewer may set `KNW` only after APPROVE, then returns the exact reviewed result and limits to the existing Coordinator, naming `Closing and record recovery`; the Reviewer never writes `DONE`. For an interrupted fresh session, the one general public return entry can inspect `KNW` or the `REV`/APPROVE carrier mismatch, output the same heading address and required Coordinator role, then stop. The user's subsequent selected request is a natural-language invocation of an already canonical direct contract, not an alias, wrapper, command, or Plan permission expansion.

### G3: current update sync is additive, but its authority model admits a bounded retirement migration

`.tfw/adapters/manifest.yaml` currently declares 11 commands for four adapters. `docs/scripts/test_repository_contracts.py::_sync_from_manifest` copies every command that is present in the target manifest; it never enumerates or deletes a command absent from that manifest. Therefore a manifest-only change gives clean receivers ten commands but leaves an existing `tfw-resume` receiver stale.

The installed update workflow already supplies the required boundary: pin one immutable target, read every applicable version-addressed migration guide, preserve project state, merge config key-by-key, remove only retired keys named by the target, apply exact copies or marker-bounded blocks, preserve foreign material, require no missing/extra commands, and require a second-run no-diff result. A retirement guide can specialize that authority without inventing a runtime helper.

The stale command destinations are exactly:

| Adapter | Possible old destination |
|---|---|
| Codex | `.agents/skills/tfw-resume/SKILL.md` |
| Claude Code | `.claude/commands/tfw-resume.md` |
| Cursor | `.cursor/commands/tfw-resume.md` |
| Antigravity | `.agents/workflows/tfw-resume.md` |

The old source payload also includes `.tfw/workflows/resume.md`, `.tfw/adapters/codex/skills/tfw-resume/SKILL.md`, the manifest row, and the exact default config mapping `tfw.workflows.resume: .tfw/workflows/resume.md`. The four persistent adapter templates and their selected receivers need their command/role references refreshed. The tracked singular compatibility root `.agent/rules/agents.md` is not a manifest target, but it contains one `TFW:CODEX` marker-bounded block and a Resume table row; it is therefore a separately named migration subject, not a path to delete wholesale.

Ownership can be determined before mutation from the receiver's installed provenance and the pinned old object: exact old canonical bytes are owned; an absent path is already converged; a differing file or malformed/unmarked root is foreign/drifted and must be preserved and reported rather than guessed. The project config key is removable only when both key and value equal the retired framework default; a customized mapping is project-owned and blocks automatic retirement. This supports an all-preflight-before-write semantic group and an idempotent repeat.

### G4: the history oracle is reproducibly split at the immutable baseline

The iteration-1 count reproduces from Git without using the working tree:

1. At `a2363fd`, union paths whose names match case-insensitive `(tfw-resume|resume\.md)` with paths whose blob text matches case-insensitive extended regex `(/tfw-resume|tfw-resume|resume\.md)`.
2. Exclude the current `TFW_20260913-151442_RWNR` task because it is the decision trace being authored.
3. Classify `^(tasks|workspace)/` as task traces; classify exactly `.tfw/CHANGELOG.md`, `KNOWLEDGE.md`, and `knowledge/stakeholder.md` as aggregates; the remainder is live retirement surface.

This yields exactly 205 paths: 23 live, 179 task traces, and 3 aggregates. Sorting the 179 baseline `git ls-tree -r` entries ordinally, joining them with LF and one final LF, and hashing the UTF-8 bytes gives SHA-256 `ed52c4c26845e90c14a569f867ec2200b18da44374f7df2fd897bf7fb58bef96`. Including the three aggregate tree entries reproduces iteration 1's 182-path digest `9248a1855d64dfbff15840c1cfb4a2fcf12ca07f3fa14c165861d283cdc089b5`.

The three aggregate before-images are independently addressable:

| Aggregate | Baseline Git blob | Baseline logical lines |
|---|---|---:|
| `.tfw/CHANGELOG.md` | `403776ef38da18df21a40d665c1ef75001993ff5` | 2,505 |
| `KNOWLEDGE.md` | `4f3a90aea1280981edadbd09d24f2e9c72bbe5ba` | 290 |
| `knowledge/stakeholder.md` | `692822f36de7dc9a2ca699ce99ee2959dd3bba89` | 26 |

Whole-file equality is appropriate for the 179 task traces. The aggregates need a monotone-line oracle: decode baseline and candidate strictly as UTF-8 and require the complete baseline line sequence, including each original line ending/content and order, to be a subsequence of the candidate; equivalently, a zero-context Git diff may contain additions but no deleted/modified baseline line. Their blob IDs fix the exact before-images. This permits a new changelog/knowledge statement without rewriting any old statement.

### G5: 2,685 has no reproducible source counter; the repository already has one suitable counter

At `a2363fd`, the exact baseline blobs are:

| File | Git blob | Bytes | `re.findall(r"\S+", strict_UTF8_text)` |
|---|---|---:|---:|
| `.tfw/workflows/plan.md` | `81f7d78bd7f270871bc4ee325789a3f457059812` | 14,416 | 2,021 |
| `.tfw/workflows/resume.md` | `31f31594e0b2146c1df71132c4481a3b711ea508` | 5,093 | 716 |
| Combined | — | 19,509 | 2,737 |

The same `\S+` algorithm already exists as `_words` in `docs/scripts/command_entry_eval.py` and `docs/scripts/test_runtime_context.py`. The current working copies are byte-identical to those two baseline blobs. Searching every Git revision of each workflow found no Plan revision with 1,995 and no Resume revision with 690 under this algorithm. No repository source records a different counter that yields both frozen values. Consequently 2,685 is an owner-approved historical claim but cannot be an executable acceptance denominator; using it for the baseline while counting the candidate differently would be a false proof.

The design cap is independently reproducible: current Plan is 2,021 words under the repository counter, above the 1,200-word rule. Git history shows a single-file Plan at `fbdf4434ea2cc6f086bb1228427b3af9b5a59b3c` with 1,195 words, so a sub-1,200 monolith is structurally possible without a helper, though that old revision does not prove preservation of today's behavior.

One comparable candidate formula can be specified in Extract: count the complete candidate Plan under `\S+`, add all newly introduced canonical continuation tokens outside Plan, and prohibit a behavior-bearing adapter/helper. Because the frozen numeric claim would change from 2,685 to the reproducible 2,737, that denominator correction is an amendment proposal, not a free refinement.

## Checkpoint

| Found | Remaining |
|---|---|
| The complete state vocabulary and existing lifecycle owners are source-defined. | Specify a routing-only matrix with a pre-write/no-mutation invariant. |
| The direct non-command close/recovery heading and Reviewer→Coordinator authority chain already exist. | Define the exact fresh-session navigation text and prove it creates no second command. |
| Four receiver destinations, source/config subjects, managed roots, and the additive-sync defect are exact. | Specify ownership outcomes, refusal atomicity, ten-command install, and repeat semantics. |
| The 179-task digest and three aggregate blob before-images reproduce. | Turn them into candidate acceptance oracles. |
| The repository counter reproduces 2,737 and disproves provenance for 2,685; a historical Plan was below 1,200. | Define candidate accounting, Plan cap disposition, and the required frozen amendment/fallback. |

**Sufficiency:**
- [x] External source used? Canonical workflows/conventions, adapter manifest and roots, update/migration contracts, maintainer tests, exact Git objects, and full per-file Git histories.
- [x] Briefing gap closed? Every unknown now has a finite source-derived decision space and a reproducible baseline.
- [x] Dimensions identified? Six independent dimensions with at least three alternatives each.

Stage complete: YES
→ User decision: already fixed by the continuing dispatch; proceed to configuration extraction.
