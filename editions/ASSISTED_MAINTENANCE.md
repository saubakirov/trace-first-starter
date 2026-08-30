# Обслуживание TFW Assisted

Эта инструкция описывает локальный мост обновлений Assisted. Он обслуживает только публичный payload в `editions/`; TFW Full, корневые инструкции репозитория и другие редакции не являются его источником или целью.

## Источники истины

- `maintenance/release-manifest.json` связывает байты публичного Assisted 1.5, кроме самого manifest.
- `maintenance/maintenance-policy.json` задаёт закрытые prior edges, authority и правила сохранения.
- `02-assisted/VERSION` содержит версию редакции; `02-assisted/CHANGELOG.md` содержит только публичную историю.
- Runtime staging, lock, private journal, terminal report, recovery и candidate directory всегда находятся вне пакета и не входят в manifest.

Manifest и policy — канонический UTF-8 JSON с переводом строки в конце. Дубликаты ключей, unsafe integers, не-NFC или непереносимые пути, case-fold collisions, ссылки, не regular files, пропущенный policy, manifest self-entry и policy cycle останавливают операцию до продуктовой записи. Exact selector имеет приоритет; иначе выбирается единственный самый длинный полный directory prefix. Неизвестный source path запрещён, неизвестный target-only path сохраняется.

## Проверка релиза

Из корня репозитория:

```text
python editions/maintenance/assisted_maintenance.py verify-release --source-root editions
python editions/maintenance/assisted_maintenance.py self-test --source-root editions
```

Обе команды read-only по отношению к source. `self-test` создаёт только изолированные временные fixtures и проверяет V1–V12. Повторный чистый запуск должен дать те же публичные manifest/policy hashes и тот же набор результатов.

## Public → downstream

Сначала выполните сравнение без записи:

```text
python editions/maintenance/assisted_maintenance.py compare --source-root SOURCE_EDITIONS --target-root TARGET_EDITIONS --prior-manifest builtin:1.0
```

Проверьте exact target, prior edge и число планируемых записей. Затем создайте отдельный operation directory вне source и target и явно повторите exact target в approval:

```text
python editions/maintenance/assisted_maintenance.py forward --source-root SOURCE_EDITIONS --target-root TARGET_EDITIONS --prior-manifest builtin:1.0 --operation-dir PRIVATE_OPERATION_DIR --approve-target TARGET_EDITIONS
```

Forward использует один проверенный immutable staging snapshot, полный destination baseline, live OS project lock и per-path recheck. `PROJECT.md`, `work/`, записи knowledge, профили people, local bindings, изменённые шаблоны/overlay, unknown target-only paths, modified stock hooks и unrelated `.codex/` сохраняются. Только три exact hooks из public 1.0 удаляются при совпадении полного stock hash.

Journal создаётся до первой target-записи и дописывается без изменения старых событий. Terminal report создаётся один раз. После частичного отказа повторите forward с новым operation directory и `--recover-from OLD_TERMINAL_JSON`; старый отчёт не меняется. Статус `verified` невозможен при необъяснимом изменении.

## Downstream → public candidate

Обратное направление никогда не изменяет public core. Оно принимает валидный private terminal report и создаёт только закрытую privacy-safe проекцию в новом candidate directory:

```text
python editions/maintenance/assisted_maintenance.py reverse-candidate --private-report PRIVATE_TERMINAL_JSON --candidate-dir NEW_CANDIDATE_DIR
```

Проекция не содержит private path, hash, count, time, participant, operation/recovery ID или детали проекта. Разрешён только boolean `suppressed`. Любое generic изменение переносится отдельно, проходит marker/hash scan и полный независимый review; только человек может принять его как следующую публичную работу. Это promotion, а не зеркало и не двусторонняя синхронизация.

## Граница реальной практики

Смешанный field lineage допустим только как read-only P6 evidence: сравнить, выделить общий candidate, проверить pre/post tree digest. Автоматический P2 forward разрешён только для чистого overlay-separated fixture или проверенного downstream с принятым prior manifest. Не запускайте код из field source и не записывайте туда staging, отчёты или временные файлы.

## Ограничения

Мост не обещает транзакцию удалённой файловой системы, не удаляет foreign lock по возрасту, не угадывает baseline и не публикует release. Push, tag и remote publication — отдельные человеческие действия вне этой команды.
