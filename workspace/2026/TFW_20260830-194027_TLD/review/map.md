# Map — "What was done?"

> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF__TFW_20260830-194027_TLD](../RF__TFW_20260830-194027_TLD.md)
> TS: [TS__TFW_20260830-194027_TLD](../TS__TFW_20260830-194027_TLD.md)
> Contract baseline: `80e9bed` → `c153895`
> Executor commit: `dfba46f`

## Understanding

The root `TECH_DEBT.md` — 132 lines, 121 rows, 77 of them open and never acted on — was moved whole by
`git mv` to `tasks/DEBT-SNAPSHOT.md`, given a 28-line header declaring it history, and left unread. Every
canonical surface that wrote, read, installed or named it stopped doing so: five workflows, four templates,
the conventions, the glossary, the compilation contract, three adapter sets, both marker blocks, three
READMEs, two release checklists and the documentation build. In its place `review.md` Step 5 gained a
**disposition gate** — every captured item is `paid` as a phase, `promoted` to a task, or ruled `not
material` on the record, and the task cannot reach `DONE` with an item undisposed — plus the literal search
that lists every captured item across REVIEW files, which returns 243 rows on this corpus.
`.tfw/migrations/2.0.0.md` gained step 6 so a receiving project can do the same from prose alone, with one
carve-out for safety rules written after an incident, routed through a question to the user. Released as
2.1.0. Nothing was created to replace the registry: maintained root artifacts fall 8 → 7.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 sealed verbatim, out of the root | §3 AC-1: snapshot exists, root file gone, `diff` empty, `md5` matched, 121 rows, header states counts + revision + the unexamined warning | ✅ |
| AC-2 no canonical text instructs an append | §3 AC-2: 33 hits, each classified by file and line as history, retirement record or snapshot path | ✅ |
| AC-3 exactly one debt write, inside the task | §3 AC-3: Steps 5–6 carry no second write; search written literally, returns 243 | ✅ *(with a delivery defect — see verify.md D1)* |
| AC-4 disposed before closing | §3 AC-4: three outcomes in `review.md`, `REVIEW.md` §5/§6 and `judge.md` row 3; walked against a real closed review; honest ceremony verdict given | ✅ |
| AC-5 deferral is not a way to finish | §3 AC-5: two instructions of that shape found, both quoted with replacements; post-change scan returns only prohibitions | ✅ |
| AC-6 every `TD-N` still resolves | §3 AC-6: row 9 deleted per amendment, `TD-{N}` → snapshot, suite green, site builds, 219 pages carry a resolved link, browser check | ✅ |
| AC-7 a receiver can retire from prose alone | §3 AC-7: all eight points met, dry run against two registries of opposite shapes, six un-gated implications named, two material ones fixed | ✅ |
| AC-8 one safety class, and the user decides | §3 AC-8: one class, heading-level recognition, asks and does nothing on silence, one task on a yes, walked against the one project that has such a section | ✅ |
| AC-9 net −1 | §3 AC-9: root artifacts 8 → 7, no config key, no script, no flag | ✅ |
| AC-10 one release | §3 AC-10: 24 copies `cmp`-verified, `TFW:CLAUDE` block **and its template source**, `TFW:CODEX` a stated no-op, three READMEs + `KNOWLEDGE.md` + glossary carry the date, retired wording verbatim, `VERSION` 2.1.0 | ✅ |
| AC-11 this repository is its own first consumer | §3 AC-11: suite green, `--check tasks` green, index regenerated, fourth bullet handed to the reviewer | ✅ |
| DoD 1–13 (HL §5) | Each maps onto an AC above; DoD 9 was dropped by amendment A1 and DoD 13 replaced it | ✅ |

## Deviations from TS

| # | Deviation | Direction | Stated in RF? | Judgement |
|---|---|---|---|---|
| 1 | `docs/scripts/test_integration.py` edited — not in TS §4 | +1 file | Yes, §1 Modified table, with the reason: it asserted `/reference/tech-debt/` in the built site and would have failed | Legitimate. The TS's own AC-6 requires the suite to pass; the test was a consumer of the retired path |
| 2 | `.tfw/project_config.yaml` edited — not in TS §4 | +1 file | Yes, §1 and §3 AC-9 | Legitimate and required: `tfw.version` is the release marker `--check project` reads. **No key added** — one value changed, verified in the diff |
| 3 | `workspace/00-INDEX.md` regenerated | +1 file | Yes, marked derived | Legitimate. The index is derived and AC-11 requires it to regenerate |
| 4 | `AGENTS.md` **not** edited despite TS §4 listing it | −1 file | Yes, §2 decision 8 | Legitimate. Neither `AGENTS.md` nor `.tfw/adapters/codex/AGENTS.md.template` ever named the registry; the coordinator ruled at ONB inconsistency 2 that a no-op is to be *stated*, never manufactured |
| 5 | Manifest row 9 **deleted** rather than repointed | design | Yes, §2 decision 2 | Not a deviation: TS AC-6 bullet 2 was **amended** to require exactly this after ONB Q2 |
| 6 | `compilable_contract.md` *Where references appear* corrected from `REVIEW.md §3` to `§5` | +1 line, out of scope | No — not called out separately | Pre-existing error fixed in passing, inside a line the task had to touch anyway. One word. Recorded here rather than treated as scope creep |

No stop-and-report was triggered and none was required: measured 42 modified · 1 renamed · 6 added in
`dfba46f`, against ceilings of 50 files / 50 new / 50 modified / 5 000 LOC. Changed lines excluding the
task's own trace artifacts: **702** (RF says ~706).

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely? — and §6-§9
- [x] Read TS DoD and matched each item to RF §3? — table above, 11 ACs plus HL DoD 1–13
- [x] Read HL §7 Principles — can I state the design philosophy? — subtraction is the deliverable; capture where the finding is; dispose before closing, never defer; an open channel is a permission; history is preserved verbatim; nothing a receiver must run; one release surface
- [x] Read ONB — were blocking questions resolved? — four questions, all answered by the coordinator on 2026-09-02; three of the answers amended the TS in place; the DoF 2 self-report (risk 7) was ruled not a breach with a bound written for the rest of the task

Stage complete: **YES**
