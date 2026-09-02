# Переход с Light на Assisted

Это проверка сохранности одного проекта, а не универсальная система миграций. Переход выполняется один раз и не удаляет первичный след.

## Опубликованный Assisted 1.6

Версия 1.6 поставляется только как целый нейтральный starter package с `VERSION=1.6`, exact versioned source object и dynamic observed manifest. Персонализированная папка, частичный service set или package с `workspace/`, human profiles, `project_id`, local bindings, task/pilot evidence, temp/conflict copies либо reparse points не является допустимым update source.

### Переход установленного 1.5 → 1.6

Точная формулировка пользователю:

`Используй /tfw-update и обнови этот проект из доверенного пакета 1.6 <точный путь, архив, URL или объект>`

До единственного Gate записи updater показывает:

- полный service manifest пакета и проекта, versions `1.5 → 1.6` и exact additions/changes/removals;
- protected manifest `workspace/`, `knowledge/`, `team/` и exact stock knowledge targets из version-specific карты;
- дословно сохраняемые canonical `project_id`, карточку, цели, professional AI role, mental model, task IDs/owners/results и valid profile filenames/identifiers;
- source-version preconditions для exact stock knowledge targets либо отдельный точный records Gate для кастомизированного target; приватные имена и hashes не публикуются как общая норма;
- доказательство, что package имеет `Состояние: НЕ ИНИЦИАЛИЗИРОВАН`, не содержит `project_id`, human profiles, `workspace/`, inbox, `.codex/`, identity helper или local state;
- local-state exclusion: Full `bindings.yaml`, canonical Assisted `assisted/bindings.yml` и legacy `tfw-assisted/bindings.yml` не читаются из package/project root, не копируются, не изменяются и не входят ни в один manifest;
- условия остановки при изменившемся baseline, parallel writer, conflict copy, target collision, невалидной schema или необъяснённом protected diff.

После Gate:

1. Замените полный service set 1.6: `AGENTS.md`, `PROJECT.md`, `README.md`, `MIGRATION.md`, `VERSION`, `CHANGELOG.md`, `шаблоны/`, `.agents/skills/`.
2. Верните дословно единственный валидный `project_id`, таблицу «Карточка проекта», цели, professional AI role и mental model установленного проекта. Package ID отсутствует и не создаёт новую identity.
3. Не меняйте valid human/automation profile filenames, identifiers или обе role-строки. Версия 1.6 не содержит profile migration; missing/duplicate/mixed/invalid schema блокирует запись.
4. Сохраните `workspace/`, `team/` и knowledge побайтово, кроме exact stock knowledge targets из принятой version-specific карты. При совпадении hash обновите только их; кастомизация без отдельного Gate останавливает запись.
5. Примените prompt-only identity overlay целиком: активные contract/user guide/skill/metadata согласованы, `.agents/skills/tfw-identity/scripts/tfw_identity.py`, каталог `scripts/` и активные helper references отсутствуют. Обычному пользователю не требуются Python, Git, shell или исполняемый helper.
6. Не читайте и не меняйте machine-local bindings. Состояние каждого компьютера остаётся вне shared/project/package scope.
7. Повторите service/protected manifests и проверьте scenario matrix: uninitialized package; existing/new participant; missing/ambiguous surname; surname collision; shared computer; unsafe local store/session-only; autonomous handoff/review; сохранение valid identifiers; отсутствие Full writes, helper и local state в package.
8. Докажите нулевой необъяснённый protected diff, только разрешённые knowledge changes, совпадение common active/package files кроме нейтрализованного `PROJECT.md`, package cleanliness и неизменность выбранного source object. Локальный post-read не является доказательством завершённой удалённой синхронизации.

Source/package collision, partial source, reparse/symlink наружу, изменившийся baseline, duplicate project ID, invalid profile schema, кастомизированный stock target без отдельного решения или unexplained protected diff останавливают обновление; частичный результат не объявляется успехом.

## Опубликованный Assisted 1.5

Версия 1.5 поставлялась как целый нейтральный starter package с `VERSION=1.5`. Персонализированная папка, marker candidate, частичный service set или пакет с legacy-source `work/`, human profiles, `project_id` и local bindings не являются допустимым update source.

### Переход установленного 1.4 → 1.5

Точная формулировка пользователю:

`Используй /tfw-update и обнови этот проект из доверенного пакета 1.5 <точный путь, архив, URL или объект>`

До единственного Gate записи updater показывает:

- полный service manifest пакета и проекта;
- protected manifest legacy-source `work/`, `knowledge/`, `people/` и one-to-one targets `workspace/`, `team/`;
- дословно сохраняемые карточку проекта, цели, knowledge, legacy task state при переносе `work/ → workspace/`, professional AI role и mental model;
- точные profile/project schema transformations и stock hash preconditions;
- local-state exclusion: Full `bindings.yaml`, canonical Assisted `assisted/bindings.yml` и legacy `tfw-assisted/bindings.yml` не читаются, не копируются и не входят в manifests;
- условия остановки до изменения проекта.

После Gate:

1. Замените полный service set 1.5 и верните персонализацию. Package `PROJECT.md` не содержит `project_id`; его нельзя использовать как identity проекта.
2. Сохраните существующий единственный валидный `project_id`; если его нет, сгенерируйте новый UUID именно для проекта. Несколько/невалидное значение блокируют запись.
3. Legacy human profile с ровно одним `Роль: <текст>` преобразуйте one-to-one в `Роль в компании: <тот же текст>` и `Роль в проекте: не указана`. Уже валидную новую схему, filename и identifier сохраняйте, даже если identifier появился по прежней naming-норме. Mixed/duplicate/invalid profile блокирует migration.
4. Не выполняйте массовый surname-rename. Новая naming-норма применяется только к новым профилям. Переименование существующего filename/identifier допустимо лишь как отдельное явно согласованное исправление конкретного невалидного профиля с manifest до/после.
5. Не меняйте task IDs, владельцев, traces, результаты, общую карточку или knowledge, кроме exact stock knowledge targets из принятой source-version карты. Кастомизация требует отдельного решения; приватные имена и hashes не входят в общий договор.
6. Не читайте и не копируйте local bindings из пакета, project root, Full `bindings.yaml`, canonical Assisted `assisted/bindings.yml` или legacy `tfw-assisted/bindings.yml`. Canonical Assisted entry создаётся на каждом устройстве отдельно после human gate.
7. Повторите pre/post manifests и scenario matrix из `CHANGELOG.md`, включая кириллицу/латиницу, missing surname, однофамильцев, invalid/locked/duplicate binding, сохранение valid identifiers и доказательство отсутствия Full writes/local state в package.

Unexpected protected change, duplicate project ID, surname/target collision, conflict copy, parallel writer, неполный package или изменённый stock target останавливают обновление; частичное обновление не объявляется успехом.

## Исторические обновления установленного Assisted до 1.4

Этот раздел применяется вместо Light-перехода, если в корне уже есть `PROJECT.md` с маркерами Assisted / 1.0 и файл `VERSION` равен 1.2, 1.3 либо материализованной pre-acceptance 1.4.

### Из 1.3

Точная формулировка пользователю:

`Используй /tfw-update и обнови этот проект из доверенного пакета 1.4 <точный путь, архив, URL или объект>`

Установленный prompt-only updater 1.3 получает целый пакет 1.4, статически читает changelog, показывает service manifest и version-specific protected migration, после чего ждёт одно согласование. Legacy-source `work/<legacy-ID>/` переносится one-to-one в `workspace/<legacy-ID>/`; карточка проекта, роли, ID, владельцы и результаты сохраняются.

### Из 1.2

Точная bootstrap-формулировка:

`Примени .agents/skills/tfw-update/SKILL.md из доверенного пакета 1.4 <точный путь, архив, URL или объект> к этому проекту 1.2 и выполни прямое обновление до 1.4`

Локальный updater 1.2 запрещает изменения legacy-source `work/`, `knowledge/`, `people/`, поэтому не может быть договором полного прямого обновления. Договор берётся из целого проверенного пакета до Gate; код источника не исполняется.

После одного согласования каждый legacy-source `work/<status>/<legacy-ID>/` переносится one-to-one в `workspace/<legacy-ID>/` только при уникальном ID, совпадающих полях ID/статуса, существующем trace и свободном target. Нормализуются только обязательные поля и живые пути; исторический текст, ID, владельцы и результаты не переписываются.

### Из pre-acceptance 1.4

Если `VERSION=1.4`, но присутствуют прежние TFW hook payload-файлы, примените исправленный пакет 1.4 тем же `/tfw-update`. Service set сверяется как same-version correction, а hooks удаляются по карте ниже. Неизвестное central или project divergence вне объявленного change set блокирует merge/overwrite.

### Очистка legacy TFW hooks

Ранние сборки 1.2, 1.3 и pre-acceptance 1.4 содержали экспериментальные TFW hooks. Их удалили после проблем с надёжностью; исправленный clean payload 1.4 не содержит:

- `.codex/hooks.json`;
- `.codex/hooks/tfw-hook.ps1`;
- `.codex/hooks/tfw-hook.sh`.

Stock SHA-256 для автоматического удаления без второго вопроса после Gate обновления:

| Source | `hooks.json` | `tfw-hook.ps1` | `tfw-hook.sh` |
|---|---|---|---|
| 1.2 | `044013a5cb31ca8c29708b0f83d5ef0e53aecb83d12091c60434a750735043ce` | `85191702eef52dc5191e27485ac50c8e27dd334e2a6bc30d82d14711829361c7` | `18039f1631375d7bea2332ffa0c55fdb602315d69ffa98f76f3875fca9eb5a1a` |
| 1.3 | `c09d0de4c7043691d9cbbae270aaa058793e9e1503d39d4f177937d938a6e374` | `c09e9ac226e242075ab2d06fd8bedd2ae24a0c0efd3e45676978a3f34ab43842` | `c21e2cf54566f9a3ea02f769a7bd11af1ccec046a4a66cc135ded614386fda86` |
| pre-acceptance 1.4 | `c09d0de4c7043691d9cbbae270aaa058793e9e1503d39d4f177937d938a6e374` | `c29b66b3565741d9b86e76a24ad8620b9809f8c6682f630c7564315ef9e2d58d` | `e05076eeae03b980f9db7d0ccac02ad859e7a56c5393d06e3245d4dfd94ae49a` |

Для каждого файла hash сверяется отдельно. Точный stock удаляется. Hash mismatch никогда не приводит к silent destructive delete: изменённый adapter сначала побайтово сохраняется как `.codex/tfw-quarantine/<source-version>/<sha256-prefix>-<basename>` с полным hash в отчёте, затем удаляется из активного штатного пути. Кастомизированный валидный `hooks.json` также сохраняется целиком, после чего из него удаляются только command-объекты, чьи `command` или `commandWindows` ссылаются на TFW adapters; unrelated events, hook entries, top-level fields и другие `.codex`-файлы сохраняются. Невалидный JSON или collision quarantine с иным содержимым останавливает запись до безопасного решения.

После correction проверка задач выполняется по действующему контракту `AGENTS.md` и `README.md`.

### Общие условия обоих маршрутов

1. До Gate фиксируются manifests service/protected set с путями, размерами и SHA-256.
2. Exact stock knowledge targets обновляются только при source-version hashes из `CHANGELOG.md`. Кастомизированный файл останавливает запись до отдельного решения.
3. Все остальные существующие `knowledge/` сохраняются побайтово; legacy-source `work/` и `people/` сопоставляются one-to-one с `workspace/` и `team/`, кроме разрешённой нормализации legacy traces 1.2.
4. Новые задачи после обновления получают `YYYYMMDD-HHMMSS__slug` без handle; legacy-ID остаются прежними.
5. После записи обязательны post-manifest, доказательство отсутствия трёх TFW hook payload-путей и активной TFW-регистрации, проверка quarantine/custom preservation, ручная проверка результатов/ссылок/секретов, skills/metadata и одинаковые postconditions 1.4. Missing, unexpected и необъяснённых protected changes должно быть ноль.
6. Коллизия пути, несовпадение status/ID, изменённый stock-файл, параллельная запись, неполный пакет или новая migration map требуют остановки; частичное обновление не объявляется успехом.

## Стоп до любой записи

Сначала прочитайте маркер редакции в `memory/PROJECT.md` и проверьте корень. Если уже существует другой верхнеуровневый `PROJECT.md`, `.tfw/` как активный контракт либо одновременно заявлены две редакции, ничего не копируйте и задайте один вопрос:

**«В корне уже есть другой активный контракт. Какую редакцию оставить единственной: существующую или Assisted?»**

Продолжайте только после однозначного выбора. Не объединяйте два поведенческих контракта.

## Порядок перехода

1. Создайте уникальную папку `migration/light-original-YYYYMMDD-HHMMSS/`.
2. Скопируйте туда исходные `README.md`, `AGENTS.md`, `TASKS.md`, весь `memory/`, legacy-source `work/` и отдельные результаты. Зафиксируйте дерево, размеры и SHA-256. Пока копия не проверена, ничего не заменяйте.
3. Скопируйте служебную часть Assisted: `.agents/skills/`, `team/README.md`, `knowledge/INDEX.md`, корневые инструкции и шаблоны. Clean payload не добавляет `.codex/`; существующее unrelated содержимое этой папки не удаляется. Исходные `README.md` и `AGENTS.md` сохраняются в архиве.
4. Создайте верхнеуровневый `PROJECT.md` с маркерами `Assisted` / `1.0`. Перенесите в него цель, людей, договорённости и ограничения из исходного `memory/PROJECT.md`, не меняя смысл. Исходный файл остаётся в архиве.
5. Для каждой строки исходного `TASKS.md` создайте отдельную стабильную папку `workspace/<ID>/`. ID не использует общий счётчик; исходный статус запишите в поле `Статус` внутри `TRACE.md`. Скопируйте trace и результаты без изменения смысла; при дальнейшей смене статуса папку не перемещайте.
6. В журнале ниже перечислите каждое соответствие «исходный путь → стабильный путь», хэш до и после и принятый статус. Исходный `TASKS.md` остаётся read-only provenance в архиве, а не новым общим task board.
7. Проверьте, что поля `Результат` и внутренние ссылки указывают на существующие пути. Исторические упоминания прежней схемы помечайте как legacy; не оставляйте их действующими инструкциями.
8. Начните новую сессию и вручную сверьте цель, число task ID, traces, результаты, людей, память, обязательные поля, внутренние ссылки и формальные признаки секретов с архивом.

## Журнал конкретного перехода

Статус: переход с Light не выполнялся.

При выполнении замените только этот раздел фактической датой, путём архива, таблицей соответствий, хэшами и результатом проверки. Не записывайте ожидаемое поведение вместо фактов.

## Историческая совместимость

Релизы Assisted до 1.3 могли хранить задачу в legacy-source каталоге `work/<status>/<ID>/`. При миграции target становится `workspace/<ID>/`, статус живёт только в `TRACE.md`, а новый ID не содержит handle владельца. Уже существующие legacy-ID не переписываются.
