# Обслуживание TFW Assisted 1.6

Обслуживание выполняется агентом через чтение, сравнение, одно явное человеческое решение и обычные файловые операции. В Assisted нет программы обновления, maintenance runtime, автоматического зеркала или статической authority-схемы. Source читается как данные; его код до Gate не исполняется.

## Кто выбирает source

Каждый publisher хранит human-readable инструкцию о своей release shelf вне replaceable Assisted package. При каждом обновлении человек указывает или подтверждает один exact versioned object: локальную папку или архив, объект Drive-like источника, GitHub-like commit/archive/asset либо другую доступную форму. Сначала этот объект материализуется в отдельное безопасное закрытое дерево.

Обязательный общий минимум:

- подтверждённые человеком publisher и locator;
- фактическая форма доступа и точная версия из `VERSION`;
- совместимость по `CHANGELOG.md` и `MIGRATION.md`;
- normalized observed manifest `relative path + size + SHA-256` для закрытого дерева;
- archive digest, если вход является архивом;
- strongest stable object identifier, provider digest или независимая attestation, когда источник их предоставляет;
- явное описание отсутствующих assurance signals.

Локально вычисленный SHA-256 доказывает целостность наблюдавшихся байтов и обнаруживает последующий drift. Сам по себе он не аутентифицирует publisher и не превращает mutable locator в неизменяемый release. Подписанный trust root относится к отдельному security-контракту.

## Классы target

| Authority | Что к ней относится | Правило |
|---|---|---|
| public core | service-документы, skills, metadata и stock navigation | менять только из подтверждённого, закрытого и повторно проверенного versioned source |
| customizable | шаблоны и пассивные assets | неизменённый stock можно обновить; пользовательскую версию сохранить либо вынести на отдельный Gate |
| protected downstream | `PROJECT.md`, `workspace/`, `team/`, `knowledge/`, персонализация и неизвестные пути | сохранять, кроме точной version-specific migration с отдельными preconditions |
| retired known stock | точно названный устаревший service path | удалять только при совпавшем baseline и наличии действия в migration map |
| unresolved | путь без единственной доказанной authority | остановиться до записи |

Один путь получает одно итоговое действие. Неизвестный source path, collision, unsafe link, mixed schema, непроверяемый baseline или drift означает `stop`, а не догадку.

## Public → downstream

Запустите `/tfw-update` в корне downstream-проекта и укажите exact versioned source.

1. **Acquire.** Подтвердите publisher/locator, материализуйте safe closed tree и зафиксируйте доступные provider/object/digest evidence.
2. **Compare.** Статически прочитайте `VERSION`, `CHANGELOG.md`, `MIGRATION.md` и service set; снимите observed source/target/protected manifests.
3. **Classify.** Назначьте каждому пути `create`, `replace`, `delete`, `preserve` или `stop` по точной source-version карте.
4. **Plan.** Покажите человеку полный закрытый список путей, protected baselines, риски, восстановление и ожидаемые postconditions.
5. **Explicit gate.** Человек одной явной репликой одобряет именно этот план. До Gate записей нет.
6. **Recheck.** Повторно разрешите и прочитайте provider source, closed tree, каждый изменяемый target и весь protected set. Любое отличие возвращает к Compare и требует нового Gate.
7. **Write.** Меняйте только одобренные пути из повторно проверенного closed tree, по одному контролируемому действию с post-read.
8. **Verify.** After-manifest должен показать новую версию public core, побайтовое сохранение protected/customized state и ноль необъяснённых изменений.

Частичный результат фиксируется как `partial`, останавливается и передаётся на проверку. Он не называется атомарной или распределённой транзакцией. Device-local Full, Assisted и legacy binding files не являются source/target migration и не входят в manifests.

## Downstream → public

Обратный поток — promotion, а не синхронизация.

1. Агент сравнивает downstream с известным public baseline без изменения downstream или public core.
2. Полезное обобщается до capability/rule; private paths, contents, digests, exact counts/times, people, roles, organization, brand, project history и unique context исключаются.
3. Privacy-clean generic candidate создаётся в явно выбранном новом каталоге вне source, target и public core.
4. Другой Reviewer независимо проверяет смысл, provenance и privacy.
5. Public core меняется только в отдельной задаче и отдельном release decision; promotion candidate никогда не мутирует его напрямую.

Field/downstream source и соседние сохранённые версии остаются read-only. Обслуживание не выполняет push, не создаёт или меняет tag и не публикует release.

## Текущая publisher capability этого репозитория

Эта инструкция — durable publisher-owned route. Она не объявляет существующим GitHub Release, Drive folder, digest, immutable object или attestation, пока такой объект отдельно не выбран, не материализован и не проверен на release stage. Replaceable `02-assisted/` остаётся provider-neutral и не содержит publisher locator.

## Минимальный отчёт

Отчёт содержит publisher/locator, source/target versions, доступные и отсутствующие assurance signals, before/after observed manifests, классификацию каждого изменённого пути, точную формулировку Gate, фактические действия, protected equality, отклонения, итог `verified | partial | blocked` и решение по candidate/review.
