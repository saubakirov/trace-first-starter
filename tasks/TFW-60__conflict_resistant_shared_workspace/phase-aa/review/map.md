# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase AA](../RF__phase-aa__portable_delivery.md)
> TS: [TS Phase AA](../TS__phase-aa__portable_delivery.md) at revision 3
> ONB: [ONB Phase AA](../ONB__phase-aa__portable_delivery.md) — eight blocking questions, all answered
> Master HL at contract baseline: `2123de1` (after amendment A4)

## Understanding

The framework could not deliver its own tooling. `gen_index.py` and `migrate_board.py` lived
in `docs/scripts/`, which `/tfw-update` does not copy, so a receiving project was told by
`conventions.md` and the CHANGELOG to run files it did not have — and the tools resolved the
project root as `parents[2]`, which made their location load-bearing. Phase AA moves the four
scripts into `.tfw/scripts/` with `git mv`, replaces depth arithmetic with a marker search,
and writes `.tfw/migrations/2.0.0.md` — the one new file — as a procedure for a project that
is not this repository.

Around that move, ten field-report findings close: the board's location and heading become
inputs on the same code path that made a committed revision the default source; a directory
whose name the identifier grammar rejects is reported as unresolved instead of being called a
backlog idea; the carrier validator names the key it rejected instead of printing
`ScannerError`; `update.md` gains the pristine-tag diff, the `task_containers` decision and a
`team/` creation step; three adapter sources stop routing `/tfw-research` at a file that has
never existed. Under owner revision R3 the phase **subtracts**: two files the coordinator had
proposed are withdrawn before creation, three templates leave the flat namespace for
directories mirroring their output, and `--check` / `--validate` / `--doctor` collapse into
one flag with three subjects, deleting the five-line config comment that existed only because
the names failed.

Three commits carry the work (`f14f744`, `80c2ed5`, `1079020`); a fourth (`440d6fd`)
strengthened the AC-3 evidence after the RF was filed. The phase's declared outcome —
an external project completing the update from the payload alone — is reported **unmet** on
its acceptance half and handed back to the owner, exactly as the ONB Q1 ruling and TS §7
require.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — tooling ships inside the payload; root by marker, not depth | §3 ✅, E1–E5; depth test run at three placements inside a real fixture | ✅ |
| AC-2 — a major release ships a migration guide, routed from `update.md` Step 3 | §3 ✅, E6–E10 | ✅ |
| AC-3 — migration finds a board wherever the project keeps it; parser untouched | §3 ✅, E11–E13 | ✅ |
| AC-4 — an unmatched directory is reported, never described | §3 ✅, E14–E18, on the corpus that produced the finding | ✅ |
| AC-5 — a person can hand-author the carrier correctly | §3 ✅, E19–E22 | ⚠️ partial — see verify.md V4 |
| AC-6 — `task_containers` presented as a decision; `initial_seq` named for removal | §3 ✅, E23–E24 | ✅ |
| AC-7 — `team/` delivered, not assumed; no README template | §3 ✅, E25–E27 | ✅ |
| AC-8 — migration reads a stable input; refuses rather than falling back | §3 ✅, E28–E32 | ✅ |
| AC-9 — one flag, three subjects; reports and exits | §3 ✅, E33–E38 | ✅ |
| AC-10 — the pristine-tag diff, and whose tag it is | §3 ✅, E39–E41 | ✅ |
| AC-11 — shipped instructions name files that exist | §3 ✅, E42–E44 | ✅ |
| AC-12 — the session name carries the task once it exists | §3 ✅, E45–E46 | ✅ |
| AC-13 half one — development fixture | §3 ✅, E47–E50 | ✅ |
| AC-13 half two — acceptance evidence | §3 ❌ **UNMET**, E51 DEFERRED, handed back to the owner | ✅ — reported exactly as TS §7 requires |
| AC-14 — the release describes what shipped | §3 ✅, E52–E57 | ⚠️ partial — see verify.md V4 |

## Deviations from TS

Four, all raised in `census.md` **before acting** rather than discovered afterwards:

| Deviation | RF's account | Reviewer's read |
|---|---|---|
| `docs/mkdocs.yml` listed in TS §4, **not changed** | `gen-files` runs `scripts/gen_docs.py` relative to `docs/`; the move does not reach it. Modify becomes 25, not 26 | Correct. The census had already flagged it conditionally: *"modified only if the build requires it"* |
| Three `.agents/skills/` entries listed, **not changed** | Codex skills route by path and copy no workflow content; all 11 byte-identical | Verified independently — 11/11 identical |
| Four files modified that TS §4 does not enumerate — `.tfw/workflows/knowledge.md` + its two copies, and `team/README.md` | All four are reached only through R3's own template moves; raised under the return-to-coordinator rule and proceeded because no limit was crossed | Correct handling. The group is a consequence of a decision taken two hours before the census, not a discovery |
| `.tfw/templates/project_config.yaml` changed beyond a path reference — `build.verify` became a real command | A receiving project can run it from the moment the payload lands | In scope: AC-9's third bullet makes `build.verify` the `--check tasks` gate, and a placeholder there would have shipped the AC unmet |

TS items **not** addressed in RF: none. Every AC is answered, including the one answered `UNMET`.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3? — all 15 AC rows, above
- [x] Read HL §7 Principles — can I state the design philosophy? — pain before mechanism; task locality; one normal writer; stable paths; local truth with derived views; filesystem first with Git preserved; the coordinator logs management; consolidation is a boundary; no trace deletion during simplification; every phase pays for its release surface. Phase AA is principle 10 made concrete: the phase that exists because a release surface went unpaid.
- [x] Read ONB — were blocking questions resolved? — eight questions, all answered; Q6's answer explicitly **superseded** at TS R3 and the ONB says so in place, which is why the RF implements `--check {index,tasks,project}` rather than `--doctor`

Stage complete: YES
