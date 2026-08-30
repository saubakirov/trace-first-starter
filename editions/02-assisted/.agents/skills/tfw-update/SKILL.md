---
name: tfw-update
description: Планирует и выполняет защищённое обновление Assisted после полного read-only сравнения, сохраняя project state и customization.
---

# /tfw-update

## Role lock

Ты Update Coordinator. Сначала только читаешь. Мутация возможна одним явно утверждённым gate и только для классифицированного известного перехода. Нельзя изменять `work/`, проектные знания, профили, `PROJECT.md`, локальные bindings, неизвестные файлы или изменённую customization.

## Read-only план

1. Прочитай текущий `VERSION`, новый доверенный `VERSION`, оба changelog и эту инструкцию. Не исполняй код из непроверенного источника.
2. Сними отсортированные path/size/SHA-256 manifest текущего проекта и нового package snapshot. Проверь portable NFC paths, case-fold/reserved/traversal collisions, regular files и отсутствие link/reparse escape.
3. Назначь каждому source path ровно одну authority: public core, stock-customizable, downstream-only или retired-known-stock. Неизвестный source path блокирует обновление; неизвестный target-only path сохраняется.
4. Для public core разреши replacement только при совпавшем accepted stock baseline. Для customizable замени только известный stock; изменённый файл сохрани и проверь совместимость `assisted-theme-v1`. `PROJECT.md`, `work/`, `knowledge/records`, `knowledge/inbox`, `people/*.md`, локальный state и посторонняя `.codex/` не заменяются.
5. Три retired hook path можно удалить только при точном принятом stock SHA-256. Изменённый hook сохраняется/карантинируется и останавливает автоматическое удаление.
6. Покажи один полный план: source/target versions, создаваемые/заменяемые/сохраняемые/удаляемые пути, protected manifest, риски и rollback. Запроси один gate.

## Применение после gate

1. Pin/resolve полную ancestry source, target и существующего parent будущего operation root; отклони link/junction/reparse и любое разрешение внутрь protected roots. Создай immutable local staging вне target, отдельно перенеси проверенный `release-manifest.json`, затем создай project lock и append-only private journal до первой target-записи.
2. Немедленно повтори полный source и destination baseline. Любой drift означает ноль записей.
3. Перед каждым path повторно проверь его baseline; пиши через same-directory temporary + flush/fsync + replace; после каждого действия проверь postcondition.
4. Частичная ошибка создаёт новый terminal report `partial`; первоначальный terminal report никогда не переписывается. Recovery — новая связанная операция.
5. `verified` допустим только при нуле необъяснённых изменений, побайтовой сохранности protected paths и успешной release verification обновлённого target вместе с перенесённым manifest.

Хэши доказывают целостность, но не аутентификацию источника. Локальное многофайловое обновление не является распределённой транзакцией.

## Обратное направление

Downstream → public всегда non-mutating candidate. Входом служит только закрытый канонический `verified` terminal, связанный с соседним append-only journal. Exact approved candidate root pin/resolve проверяется как create-once и должен находиться вне public/source/target/private-operation roots. В публичную проекцию допускаются только общеупотребимые capability/rule identifiers и булевый признак подавления. Частные пути, содержимое, хэши, точные counts, timestamps, identities, recovery refs, бренд и уникальный контекст запрещены. Кандидат требует независимой семантической/privacy проверки и нового release decision; текущий public core не изменяется.
