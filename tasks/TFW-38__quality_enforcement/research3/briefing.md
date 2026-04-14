# Briefing — Iteration 3
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: (A) Verify TS over-specification problem — does coordinator write implementation instead of requirements? (B) Finalize review stage/mode naming via systematic comparison.
> Predecessors: [RES iter 1](../RES__TFW-38__quality_enforcement.md), [RES iter 2](../RES__iter2__quality_enforcement.md)

## Predecessor Decisions to Build On
- D6: 4-stage review: Comprehend → Verify → Assess → Synthesize
- D7: 3 review modes: code, prose, spec
- D8: Stages as sections in REVIEW (no separate files)

## User-Injected Directions (post-RES2)

### Thread A: TS Over-Specification
"Проверить что координатор в ТС не ставит задачу слишком детально, так что уже почти выполняет её. Оставляет ли он на креатив исполнителя, пишет требования, или реализацию готовую. Мне иногда кажется, что в ТС полная реализация лежит и зря потрачены токены."

### Thread B: Naming
- "prose мне непонятно вообще"
- "между assess и judge мне больше нравится judge, намерение явное"
- "надо посмотреть на наши валью конвенции опыт и знания, исходя из чего мы выбираем названия"

## Research Plan

### Gather
- Thread A: Sample 8-10 TS files across projects. Measure: how much is requirements (WHAT) vs implementation details (HOW). Are there code snippets? File paths? Line-by-line instructions?
- Thread B: Re-read TFW conventions, glossary, philosophy. Extract naming principles. Build candidate matrix for stage names and mode names.

### Extract
- Thread A: Classify TS content types (requirement, design direction, implementation detail, code snippet). Quantify the ratio.
- Thread B: Build comparison matrices with pros/cons for each naming candidate. Apply TFW naming principles as filters.

### Challenge
- Thread A: Is over-specification always bad? When does it help? Define the boundary.
- Thread B: Test final naming candidates against international audience, memorability, TFW philosophy alignment.

## Guiding Questions
1. Is TS over-specification consistent across projects, or project-specific?
2. Do executors deviate from over-specified TS steps (proving the detail was wasted)?

---
Stage complete: NO
