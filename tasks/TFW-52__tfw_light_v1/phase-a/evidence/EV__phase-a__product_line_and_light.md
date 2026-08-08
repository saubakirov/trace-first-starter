# EV — TFW-52 / Phase A: линейка редакций и стабильный Light

> **Date**: 2026-08-08
> **Author**: Codex (Executor)
> **Task**: TFW-52
> **TS**: [TS Phase A](../TS__phase-a__product_line_and_light.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Microsoft Windows 11 Pro 10.0.26200 build 26200 |
| Language / Runtime | PowerShell 5.1.26100.8655; Python 3.13.5; Git 2.42.0.windows.1 |
| Deploy target | Local Markdown starter roots and two independent Codex tasks outside `steps-framework` |
| CI / Pipeline | Local deterministic checks; pytest + MkDocs integration (`68 passed`) |
| AC-6 live root | `D:\projects\research\tfw52-phase-a-runs\run-1-contradictions` |
| AC-6 Codex thread | `019fe251-0a40-77e1-bc85-c1bbc4d9cd44` |
| AC-7 live root | `D:\projects\research\tfw52-phase-a-runs\run-2-handout` |
| AC-7 Codex thread | `019fe251-16eb-7461-b4a1-a6d6af38446f` |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | The edition guide is 473 words, distinguishes Light/Assisted/Full by work characteristics, names Light's manual limit, marks Assisted as Phase B, and creates no Team directory. The TS Evidence field is N/A because this is a direct document-reading gate. | Repository checkout | N/A | [`editions/README.md`](../../../../editions/README.md); [`verification.txt`](verification.txt) |
| E2 | AC-2 | `01-light` has exactly four files; word limits pass; `AGENTS.md` and `TASKS.md` are byte-identical to TFW-51; recursive diff contains only the allowed installation and edition/version changes; no automation/runtime placeholders exist. | Repository checkout | VERIFIED | [`diff-vs-tfw51.txt`](diff-vs-tfw51.txt) |
| E3 | AC-3 | Both independent sessions started from files copied literally into clean project roots; no `tfw-light-ru` references remain and both completed from the root layout. | Two independent Codex tasks | VERIFIED | [`run-1 tree`](run-1-contradictions/tree.txt); [`run-2 tree`](run-2-handout/tree.txt); [`verification.txt`](verification.txt) |
| E4 | AC-4 | `memory/PROJECT.md` contains filled `Активная редакция = TFW Light` and `Версия редакции = 1.0.0` fields. The TS Evidence field assigns factual runtime use to Phase B, so Phase A live evidence is N/A. | Repository checkout | N/A | [`PROJECT template`](../../../../editions/01-light/memory/PROJECT.md); [`verification.txt`](verification.txt) |
| E5 | AC-5 | Root README contains the editions entry, link, copy-to-root instruction, and explicitly says Assisted is not yet available. The TS Evidence field is N/A because this is a direct documentation gate. | Repository checkout | N/A | [`README.md`](../../../../README.md); [`verification.txt`](verification.txt) |
| E6 | AC-6 | A separate Codex task initialized one clean non-code project with 0 questions and no user file-management intervention, created exactly one task/trace/result, found exactly the two seeded conflicts, kept the committee approval as an aligned requirement, and closed `TASKS.md` as `ГОТОВО`. | Thread `019fe251-0a40-77e1-bc85-c1bbc4d9cd44`; external root above | VERIFIED | [`TRACE.md`](run-1-contradictions/TRACE.md); [`contradictions.md`](run-1-contradictions/contradictions.md); [`TASKS.md`](run-1-contradictions/TASKS.md); [`PROJECT.md`](run-1-contradictions/memory/PROJECT.md); [`tree.txt`](run-1-contradictions/tree.txt) |
| E7 | AC-7 | A second independent Codex task initialized one clean non-code project with 0 questions and no user file-management intervention, created exactly one task/trace/handout, produced a ready 20-minute material with one example, six exercises and six balanced answers, transferred durable knowledge, and closed `TASKS.md` as `ГОТОВО`. | Thread `019fe251-16eb-7461-b4a1-a6d6af38446f`; external root above | VERIFIED | [`TRACE.md`](run-2-handout/TRACE.md); [`handout.md`](run-2-handout/handout.md); [`TASKS.md`](run-2-handout/TASKS.md); [`PROJECT.md`](run-2-handout/memory/PROJECT.md); [`tree.txt`](run-2-handout/tree.txt) |
| E8 | AC-8 | Pre/post SHA-256 hashes of all four TFW-51 files match and `git status` reports no entries under the historical TFW-51 path. | Repository checkout before and after implementation/runs | VERIFIED | [`before hashes`](baseline-sha256-before.txt); [`after hashes`](baseline-sha256-after.txt) |

## Verdict

Evidence verdict: 5/8 VERIFIED, 0 DEFERRED, 0 BLOCKED, 3 N/A

## Attachments

| File | Description |
|------|-------------|
| [`verification.txt`](verification.txt) | Deterministic AC checks, provenance, copy hashes, build result, and the recovered AC-6 editor permission observation. |
| [`diff-vs-tfw51.txt`](diff-vs-tfw51.txt) | Exact Light tree, word counts, immutable-file hashes, and recursive diff against TFW-51. |
| [`baseline-sha256-before.txt`](baseline-sha256-before.txt) / [`baseline-sha256-after.txt`](baseline-sha256-after.txt) | Pre/post integrity manifests for historical TFW-51. |
| [`run-1-contradictions/`](run-1-contradictions/) | AC-6 point-in-time inputs, task state, project memory, trace, result and provenance tree. |
| [`run-2-handout/`](run-2-handout/) | AC-7 point-in-time input, task state, project memory, trace, result and provenance tree. |
| [`ac6-ac7-dispatch.md`](ac6-ac7-dispatch.md) | Exact independent-session prompts, expected outputs and test-agent prohibitions used for dispatch. |

---

*EV — TFW-52 / Phase A: линейка редакций и стабильный Light | 2026-08-08*
