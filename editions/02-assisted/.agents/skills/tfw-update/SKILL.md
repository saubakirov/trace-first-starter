---
name: tfw-update
description: Команда /tfw-update получает целый пакет TFW, проверяет version-specific migration и после одного согласования обновляет service set, сохраняя project identity, персонализацию, valid profile identifiers, workspace/knowledge/team и исключая device-local bindings Full/Assisted; применяет только доказанную migration map.
---

# /tfw-update

Обнови набор целиком после одного согласования на запись. Это prompt-only процесс: самостоятельно выбирай доступные инструменты среды и не требуй конкретную ОС, runtime, shell, архиватор, браузер или коннектор.

## Service set

`AGENTS.md`, `PROJECT.md`, `README.md`, `MIGRATION.md`, `VERSION`, `CHANGELOG.md`, `шаблоны/`, `.agents/skills/`.

Опубликованные clean packages 1.4, 1.5 и 1.6 не содержат `.codex/` или local bindings. Существующая `.codex/` является пользовательской областью, кроме точной version-specific cleanup-карты прежних TFW hooks ниже. Unrelated entries и файлы сохраняются.

## Protected set

`workspace/`, `knowledge/`, `team/` не меняются, если migration конкретной версии одновременно не:

1. перечислена в `CHANGELOG.md` пакета;
2. показана точной картой исходных/целевых путей и hash-preconditions;
3. отдельно включена в единственный Gate записи;
4. окружена manifests до/после по относительным путям, размерам и SHA-256.

Task ID никогда не переписывается. Новая версия меняет только схему будущих задач; legacy task folders остаются на стабильных путях.

`project_id` и profile schema относятся к protected project identity. Их version-specific migration допустима только по точной карте changelog и единственному Gate. Machine-local registries TFW Full и Assisted не являются частью проекта: их не ищут в пакете/project root, не читают как migration source, не копируют между namespace/устройствами, не публикуют и не включают в shared manifests.

## 1. Получи целый пакет и выбери договор

1. Прочитай текущие `VERSION`/`CHANGELOG.md`. Если источник не дан, задай ровно один вопрос: «Где находится пакет новой версии — путь, архив, ссылка, вложение, облачный объект или другое доступное представление?»
2. Если исходная версия 1.2 и пользователь явно поручил применить `tfw-update/SKILL.md` из пакета 1.4, используй этот договор как bootstrap. Локальный updater 1.2 не имеет полномочий на required protected migration и не может объявить полный успех 1.2→1.4.
3. Для исходной 1.3 используй установленный prompt-only updater 1.3, проверяя package 1.4 и его changelog.
4. Для исходной 1.4 и целевой 1.5 используй только договор целого опубликованного пакета 1.5 с точной картой 1.4→1.5. Проектная папка с `VERSION=1.5-candidate` не является опубликованным источником и не может быть установлена в другой проект как релиз.
5. Для исходной 1.5 и целевой 1.6 используй только договор целого опубликованного пакета 1.6 с точной картой 1.5→1.6. Персонализированный проект или частичный overlay не является release source.
6. Получи источник в новую безопасную временную область вне обновляемого проекта. Не исполняй никакой код источника, включая scripts и макросы; не записывай токены и параметры доступа.
7. Приведи источник к одному файловому дереву целого пакета. Запрети выход путей, абсолютные/дублирующиеся нормализованные пути, reparse/symlink наружу, спецфайлы и подмену корня.
8. Недоступный, закрытый, повреждённый, candidate-only или неполный источник отклони с точной причиной без изменения проекта.

## 2. Статическая проверка до Gate

1. Найди ровно один корень с `PROJECT.md`, `AGENTS.md`, `VERSION`, `CHANGELOG.md`; проверь Assisted / 1.0 и ожидаемую версию.
2. Статически прочитай service set, все `tfw-*` skills и metadata. Убедись, что `.agents/skills/tfw-update/` содержит только `SKILL.md` и `agents/openai.yaml`, а clean package не содержит `.codex/`, `workspace/`, inbox, human profiles, `project_id`, персонализированную карточку, task/pilot evidence, local binding registry, temp/conflict copies или reparse points; `PROJECT.md` обязан быть `НЕ ИНИЦИАЛИЗИРОВАН`. Для 1.6 дополнительно проверь, что `tfw-identity` содержит только `SKILL.md` и `agents/openai.yaml`, без helper и `scripts/`.
3. Составь manifests текущего и нового service set; перечисли additions/changes/removals.
4. Составь manifest всех `workspace/`, `knowledge/`, `team/`; повторно сними его непосредственно перед записью.
5. Из `CHANGELOG.md` выбери только карту, соответствующую точной исходной версии.

### 1.5 → 1.6

- источник — только целый нейтральный package `VERSION=1.6` с точной картой changelog; package `PROJECT.md` имеет `Состояние: НЕ ИНИЦИАЛИЗИРОВАН` и не содержит `project_id`;
- существующий единственный canonical UUID `project_id`, таблица «Карточка проекта», цели, professional AI role и mental model сохраняются дословно; missing/duplicate/invalid project state блокирует запись;
- valid human/automation profile filenames, identifiers и обе role-строки сохраняются без пересчёта и переименования; 1.5→1.6 не выполняет profile migration, а mixed/duplicate/invalid schema является blocker;
- `workspace/`, `team/` и knowledge сохраняются побайтово, кроме точных stock knowledge targets, названных version-specific картой пакета и совпавших с опубликованными исходными SHA-256, либо по отдельному точному records Gate; приватные имена и хэши не становятся общей нормой;
- identity change set применяется целиком: active contract/user guide/skill/metadata согласованы, `tfw_identity.py`, `tfw-identity/scripts/` и активные helper references отсутствуют; обычному пользователю не требуются Python, Git, shell или исполняемый helper;
- local bindings TFW Full и Assisted не читаются из package/project root, не изменяются, не копируются между namespace/устройствами и не входят в manifests;
- установленный 1.5 не требует legacy cleanup; историческая карта ниже применяется только к точной source-version 1.2/1.3/pre-acceptance 1.4;
- postconditions: `VERSION=1.6`, uninitialized clean package, нулевой необъяснённый protected diff, только точные разрешённые knowledge changes при выполненных preconditions, сохранение персонализации/valid identifiers и common active/package equality кроме нейтрализованного `PROJECT.md`;
- scenario matrix включает existing/new participant, missing/ambiguous surname, surname collision, shared device, unsafe local store/session-only, autonomous handoff/review, отсутствие Full writes/helper/local state в package и неизменность source starter.

### 1.4 → опубликованный 1.5

- этот маршрут недоступен, пока источник имеет marker `1.5-candidate` или не содержит принятую точную migration map;
- существующий единственный валидный UUID `project_id` сохраняется; при отсутствии после Gate генерируется новый UUID конкретного проекта, но package ID/путь/имя человека не используются;
- карточка проекта, цели, knowledge, legacy-source `work/` с one-to-one target `workspace/`, task IDs, владельцы, professional AI role и mental model сохраняются;
- каждый legacy human profile с ровно одним полем `Роль: <текст>` преобразуется one-to-one в `Роль в компании: <тот же текст>` и `Роль в проекте: не указана`; валидная новая schema, filename и identifier сохраняются, даже если identifier появился по прежней naming-норме; mixed/duplicate/invalid profile блокирует запись;
- новая surname-based naming-норма применяется только к новым профилям; отсутствие фамилии и фамильная коллизия требуют уточнения. Переименование существующего filename/identifier допустимо только как отдельное явно согласованное исправление конкретного невалидного профиля с pre/post manifest, не как массовая migration;
- stock knowledge targets обновляются только при exact source-version SHA-256 из changelog либо по отдельному точному records Gate; приватные имена и digests в публичный договор не встраиваются;
- local bindings TFW Full и legacy Assisted `tfw-assisted/bindings.yml` не читаются, не мигрируют и не входят в manifests; canonical Assisted использует `%LOCALAPPDATA%\tfw\assisted\bindings.yml` или `~/.tfw/assisted/bindings.yml` и создаёт запись заново через human gate;
- postconditions включают uninitialized, 0/1/3/large profiles, new/existing profile, surname Cyrillic/Latin, missing surname, surname collision с подтверждённым уточнением, fixed/ask/missing/invalid/duplicate binding, foreign lock, shared-store rejection, сохранение valid identifiers, manual/auto task roles, arbitrary task type, отсутствие Full writes и local state/hard-coded participant names в package.

### 1.3 → 1.4

- существующий legacy-source `work/<legacy-ID>/` переносится one-to-one в `workspace/<legacy-ID>/`; ID, trace semantics и история не переписываются;
- stock knowledge targets заменяются только при совпадении известных исходных SHA-256 из changelog, без публикации приватных имён в общей карте;
- кастомизированный protected-файл является конфликтом и требует отдельного решения;
- остальные protected-файлы должны остаться побайтово неизменными.
- прежние TFW hooks очищаются по version-specific карте раздела «Legacy TFW hook cleanup».

### 1.2 → 1.4

- каждый прямой legacy-source `work/<status>/<legacy-ID>/` переносится one-to-one в `workspace/<legacy-ID>/` только при уникальном ID, совпадении ID/статуса, существующем trace и свободном target;
- в traces допустимы только нормализация обязательных полей и живых путей `work/<status>/<ID>/ → workspace/<ID>/`; историческое описание не переписывается;
- stock knowledge targets обновляются только при exact source-version hashes из changelog и отдельной проверке preconditions;
- остальные protected-файлы и пользовательские артефакты сохраняются побайтово.
- прежние TFW hooks очищаются по version-specific карте раздела «Legacy TFW hook cleanup».

### Pre-acceptance 1.4 → corrected 1.4

- same-version correction разрешена только при доказанном pre-acceptance manifest либо точном service diff;
- task folders, персонализация и protected set не меняются;
- прежние TFW hooks очищаются по карте pre-acceptance 1.4;
- unexpected divergence вне объявленного service diff останавливает merge/overwrite.

### Legacy TFW hook cleanup

Legacy TFW hooks исключены из исправленной 1.4 после проблем с надёжностью. После единственного Gate version-specific обновления их cleanup является частью уже согласованной записи и не требует дополнительного вопроса.

| Source | `.codex/hooks.json` | `.codex/hooks/tfw-hook.ps1` | `.codex/hooks/tfw-hook.sh` |
|---|---|---|---|
| 1.2 | `044013a5cb31ca8c29708b0f83d5ef0e53aecb83d12091c60434a750735043ce` | `85191702eef52dc5191e27485ac50c8e27dd334e2a6bc30d82d14711829361c7` | `18039f1631375d7bea2332ffa0c55fdb602315d69ffa98f76f3875fca9eb5a1a` |
| 1.3 | `c09d0de4c7043691d9cbbae270aaa058793e9e1503d39d4f177937d938a6e374` | `c09e9ac226e242075ab2d06fd8bedd2ae24a0c0efd3e45676978a3f34ab43842` | `c21e2cf54566f9a3ea02f769a7bd11af1ccec046a4a66cc135ded614386fda86` |
| pre-acceptance 1.4 | `c09d0de4c7043691d9cbbae270aaa058793e9e1503d39d4f177937d938a6e374` | `c29b66b3565741d9b86e76a24ad8620b9809f8c6682f630c7564315ef9e2d58d` | `e05076eeae03b980f9db7d0ccac02ad859e7a56c5393d06e3245d4dfd94ae49a` |

Для каждого пути вычисли SHA-256 отдельно:

1. Если hash равен stock hash точной source-version, удали файл автоматически.
2. Если adapter по штатному TFW-пути изменён, до удаления побайтово скопируй его как `.codex/tfw-quarantine/<source-version>/<sha256-prefix>-<basename>` и запиши полный SHA-256 в отчёт. Если target уже существует с тем же полным hash, reuse допустим; с иным содержимым — остановка.
3. Если `hooks.json` изменён, сначала сохрани оригинал по той же quarantine-схеме, затем распарси JSON и удали только command-объекты, где `command` или `commandWindows` ссылается на `.codex/hooks/tfw-hook.ps1` или `.codex/hooks/tfw-hook.sh`. Пустые TFW-only containers можно удалить; unrelated hook entries/events и top-level fields сохрани семантически.
4. Невалидный JSON, неоднозначная структура либо невозможность доказать сохранность unrelated entries останавливает запись. Hash mismatch никогда не разрешает silent destructive delete.
5. Другие файлы/папки `.codex/` сохраняются побайтово. После cleanup три штатных TFW-пути отсутствуют либо `hooks.json` остаётся только с unrelated entries; активных ссылок на TFW adapters нет.

Коллизия, несовпадение status/ID, кастомизированный stock-файл, параллельное изменение, неполный пакет или необъяснённая migration останавливают процесс до записи.

## 3. Единственный Gate записи

Покажи пользователю:

- форму источника и фактические средства доступа;
- версии до/после и корень пакета;
- service manifest: additions/changes/removals;
- точную version-specific protected migration map и hash-preconditions;
- сохранение/создание `project_id`, profile schema/naming map и доказанное исключение обоих local namespaces для 1.4→1.5;
- сохранение `project_id`, персонализации, valid profiles/identifiers, prompt-only identity и доказанное исключение обоих local namespaces для 1.5→1.6;
- точные stock hashes, план stock-delete/custom-quarantine и сохраняемое unrelated `.codex` content;
- сохраняемые карточку проекта, профессиональную роль и ментальную модель;
- проверки после установки и условия остановки.

Запроси одно явное согласование на весь план записи. Если источник или проект изменился после проверки, пересобери manifests и запроси Gate заново.

## 4. Примени после согласования

1. Повтори protected manifest и исходные hashes; остановись при расхождении.
2. Сохрани дословно таблицу «Карточка проекта», пользовательский проектный контекст и два значения раздела «Настройка этого проекта».
3. Замени service set целиком из проверенного пакета; верни персонализацию и маркеры Assisted / 1.0. Не overlay/delete `.codex/` как service directory.
4. Выполни только выбранную и утверждённую migration map. Не переименовывай legacy-ID.
5. Только если выбранная source-version имеет точную legacy cleanup-карту, выполни её: stock-delete или backup/quarantine плюс хирургическое отключение регистрации. Никакой код источника не исполняй.
6. Для будущих задач проверь новый формат `YYYYMMDD-HHMMSS__slug`, обязательного владельца, запрет `__` в slug и отказ от перезаписи при коллизии.
7. Для 1.5 и новее проверь раздельные participant/corporate role/project role/owner/AI role, динамические profiles, surname-based создание только новых identifiers, сохранение уже valid identifiers и то, что оба local binding namespace отсутствуют в package/shared manifests. Для 1.6 также проверь prompt-only identity, отсутствие helper/`scripts/` и обязательной пользовательской runtime-зависимости.
8. Создай manifest после записи. Missing, unexpected и необъяснённо изменённых protected-файлов должно быть ноль; разрешённые version-specific protected changes перечисли отдельно; unrelated `.codex` должно совпасть побайтово или семантически для сохранённых JSON entries.
9. В изолированной доверенной области проверь skills/metadata, trace/result/link/secret checks, version-specific cleanup paths только для соответствующих старых источников, stock/custom/quarantine scenarios, новый/legacy ID, точные имена ролей и version-specific postconditions.
10. Отчитайся manifests, версиями, изменёнными service/protected-файлами, stock hashes, quarantine paths, сохранённой персонализацией/unrelated `.codex`, исключённым local state, проверками и остаточными рисками.

После изменения `AGENTS.md` попроси новую сессию.

## Где остановиться

До записи — на отсутствии/невалидности источника, конфликте либо единственном Gate. После согласия доведи service replacement, только утверждённую migration и проверки до конца. При любом необъяснённом protected change сообщи его первым делом и не объявляй успех.
